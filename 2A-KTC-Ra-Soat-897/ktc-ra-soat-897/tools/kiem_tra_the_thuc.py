#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kiem_tra_the_thuc.py – Đo thể thức, kỹ thuật trình bày của dự thảo .docx
Gói ktc-ra-soat-897 v4.5 (27/10/2026)

Đo trực tiếp từ XML của tệp .docx (không ước lượng từ bản hiển thị) theo
"Bảng thông số thể thức KTC" (references/Quy-Tac-KTC/01-Bang-Thong-So-The-Thuc-KTC.md).
Mỗi phát hiện gắn mã quy tắc và mức đề xuất theo 02-Quy-Tac-Xep-Muc.md.

Cách dùng:
    python3 kiem_tra_the_thuc.py <du_thao.docx> [--he auto|chinh_quyen|dang]
                                 [--json ket_qua.json] [--khong-dung-ban]

  --he              hệ văn bản (mặc định auto: có "ĐẢNG CỘNG SẢN VIỆT NAM" → dang)
  --json            ghi thêm kết quả dạng JSON
  --khong-dung-ban  không dựng PDF bằng LibreOffice (khi đó không đếm được số trang
                    từng phần; các mục cần số trang ghi "Chưa kiểm")

Kết quả in ra dạng Markdown: bảng phát hiện (Mã | Hạng mục | Vị trí | Đo được |
Yêu cầu | Căn cứ | Mức) và bảng các mục đạt (kèm số đo) để đưa vào Phần III.
"""
import sys, os, re, json, zipfile, argparse, subprocess, tempfile, shutil, unicodedata
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS = {'w': W, 'r': R}
def q(t): return '{%s}%s' % (W, t)

# ----------------------------------------------------------------------------
# Thông số chuẩn
# ----------------------------------------------------------------------------
TOL = 20  # dung sai twips (≈ 0,035 cm) – khớp bảng 01 mục C
PROFILE = {
    'chinh_quyen': dict(
        ten='Văn bản hành chính (Chính quyền) – TB 597/TB-CĐKT, QĐ 1355/QĐ-CĐKT, chỉ đạo của Hiệu trưởng ngày 26/10/2026; phần chưa quy định theo NĐ 30/2020/NĐ-CP',
        top=1134, bottom=1134, left=1701, right=1134, header=720, footer=720,
        body_sz=28, num_sz=28, hide_first=True, phu_luc_so='la_ma',
        line_min_auto=240, line_max_auto=360, line_min_exact=None, line_max_exact=None,  # v4.4: TB 597 mục 6 đính chính 27/10/2026 – chỉ kiểu theo dòng
        indent_min=567, indent_max=720, noi_nhan_sz=22, noi_nhan_label_sz=24,
        ten_loai_sz=(28,), trich_yeu_sz=(28,), body_szs=(28,),
    ),
    'dang': dict(
        ten='Văn bản của Đảng – HD 05-HD/VPTW, QĐ 399-QĐ/TW, QĐ 208-QĐ/TW; mẫu đầu văn bản tại Phụ lục TB 597/TB-CĐKT',
        top=1134, bottom=1134, left=1701, right=850, header=567, footer=None,
        body_sz=28, num_sz=28, hide_first=True, phu_luc_so='a_rap',
        line_min_auto=None, line_max_auto=None, line_min_exact=360, line_max_exact=440,
        indent_min=540, indent_max=600, noi_nhan_sz=24, noi_nhan_label_sz=28,
        ten_loai_sz=(30, 32), trich_yeu_sz=(28, 30), body_szs=(28, 30),
    ),
}

def twip_cm(v):
    return '%.2f cm' % (v / 566.93) if v is not None else '—'
def hp_pt(v):
    return '%g pt' % (v / 2) if v is not None else '—'

def norm(s):
    s = unicodedata.normalize('NFC', s or '')
    return re.sub(r'\s+', ' ', s).strip()

# ----------------------------------------------------------------------------
# Đọc tệp và phân giải kiểu (style)
# ----------------------------------------------------------------------------
class Doc:
    def __init__(self, path):
        self.path = path
        self.z = zipfile.ZipFile(path)
        self.doc = etree.fromstring(self.z.read('word/document.xml'))
        self.body = self.doc.find(q('body'))
        self.styles = {}
        self.default_pstyle = None
        self.def_ppr = None
        self.def_rpr = None
        self.theme = {}
        th = [n for n in self.z.namelist() if n.startswith('word/theme/') and n.endswith('.xml')]
        if th:
            A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
            tr = etree.fromstring(self.z.read(th[0]))
            for k in ('major', 'minor'):
                e = tr.find('.//' + A + k + 'Font/' + A + 'latin')
                if e is not None: self.theme[k] = e.get('typeface')
        if 'word/styles.xml' in self.z.namelist():
            st = etree.fromstring(self.z.read('word/styles.xml'))
            dd = st.find(q('docDefaults'))
            if dd is not None:
                self.def_rpr = dd.find('.//' + q('rPrDefault') + '/' + q('rPr'))
                self.def_ppr = dd.find('.//' + q('pPrDefault') + '/' + q('pPr'))
            for s in st.findall(q('style')):
                sid = s.get(q('styleId'))
                based = s.find(q('basedOn'))
                self.styles[sid] = dict(type=s.get(q('type')),
                                        based=based.get(q('val')) if based is not None else None,
                                        ppr=s.find(q('pPr')), rpr=s.find(q('rPr')))
                if s.get(q('type')) == 'paragraph' and s.get(q('default')) in ('1', 'true'):
                    self.default_pstyle = sid
        self.rels = {}
        rp = 'word/_rels/document.xml.rels'
        if rp in self.z.namelist():
            rr = etree.fromstring(self.z.read(rp))
            for r_ in rr:
                self.rels[r_.get('Id')] = r_.get('Target')
        self._hf_cache = {}

    def style_chain(self, sid):
        out, seen = [], set()
        while sid and sid in self.styles and sid not in seen:
            seen.add(sid); out.append(self.styles[sid]); sid = self.styles[sid]['based']
        return out  # gần nhất trước

    def hf_xml(self, rid):
        if rid in self._hf_cache: return self._hf_cache[rid]
        tgt = self.rels.get(rid)
        x = None
        if tgt:
            p = 'word/' + tgt.lstrip('/').replace('word/', '')
            if p in self.z.namelist():
                x = etree.fromstring(self.z.read(p))
        self._hf_cache[rid] = x
        return x

def onoff(el):
    if el is None: return None
    v = el.get(q('val'))
    return not (v in ('0', 'false', 'off'))

def para_props(D, p):
    """Thuộc tính đoạn hiệu lực: spacing before/after/line/lineRule, ind firstLine/hanging, jc."""
    res = dict(before=None, after=None, line=None, rule=None, first=None, hanging=None, jc=None,
               keep=None, pagebreak_before=False, ind_l=0, ind_r=0)
    layers = []
    if D.def_ppr is not None: layers.append(D.def_ppr)
    ppr = p.find(q('pPr'))
    sid = None
    if ppr is not None and ppr.find(q('pStyle')) is not None:
        sid = ppr.find(q('pStyle')).get(q('val'))
    else:
        sid = D.default_pstyle
    for st in reversed(D.style_chain(sid)):
        if st['ppr'] is not None: layers.append(st['ppr'])
    if ppr is not None: layers.append(ppr)
    for L in layers:
        sp = L.find(q('spacing'))
        if sp is not None:
            for a, k in (('before', 'before'), ('after', 'after'), ('line', 'line'), ('lineRule', 'rule')):
                v = sp.get(q(a))
                if v is not None:
                    res[k] = v if k == 'rule' else int(float(v))
            if sp.get(q('beforeAutospacing')) in ('1', 'true'): res['before'] = 280
            if sp.get(q('afterAutospacing')) in ('1', 'true'): res['after'] = 280
        ind = L.find(q('ind'))
        if ind is not None:
            fl = ind.get(q('firstLine')); hg = ind.get(q('hanging'))
            if fl is not None: res['first'] = int(float(fl)); res['hanging'] = None
            if hg is not None: res['hanging'] = int(float(hg)); res['first'] = None
            for a_, k_ in (('left', 'ind_l'), ('start', 'ind_l'), ('right', 'ind_r'), ('end', 'ind_r')):
                if ind.get(q(a_)) is not None:
                    try: res[k_] = int(float(ind.get(q(a_))))
                    except ValueError: pass
        jc = L.find(q('jc'))
        if jc is not None: res['jc'] = jc.get(q('val'))
        if L.find(q('pageBreakBefore')) is not None:
            res['pagebreak_before'] = onoff(L.find(q('pageBreakBefore')))
    if res['rule'] is None and res['line'] is not None: res['rule'] = 'auto'
    return res, sid

def run_props(D, p, r, psid):
    res = dict(sz=None, b=False, i=False, caps=False, font=None, u=False)
    layers = []
    if D.def_rpr is not None: layers.append(D.def_rpr)
    for st in reversed(D.style_chain(psid)):
        if st['rpr'] is not None: layers.append(st['rpr'])
    rpr = r.find(q('rPr'))
    if rpr is not None and rpr.find(q('rStyle')) is not None:
        for st in reversed(D.style_chain(rpr.find(q('rStyle')).get(q('val')))):
            if st['rpr'] is not None: layers.append(st['rpr'])
    if rpr is not None: layers.append(rpr)
    for L in layers:
        s = L.find(q('sz'))
        if s is not None and s.get(q('val')): res['sz'] = int(float(s.get(q('val'))))
        for tag, key in (('b', 'b'), ('i', 'i'), ('caps', 'caps')):
            e = L.find(q(tag))
            if e is not None: res[key] = onoff(e)
        u = L.find(q('u'))
        if u is not None: res['u'] = u.get(q('val')) not in (None, 'none')
        f = L.find(q('rFonts'))
        if f is not None:
            v = f.get(q('ascii')) or f.get(q('hAnsi'))
            if v: res['font'] = v
            elif f.get(q('asciiTheme')):
                tn = f.get(q('asciiTheme'))
                res['font'] = D.theme.get('major' if 'major' in tn.lower() else 'minor') or '(theme:%s)' % tn
    return res

def p_text(p):
    out = []
    for el in p.iter():
        if el.tag == q('t'): out.append(el.text or '')
        elif el.tag == q('tab'): out.append('\t')
        elif el.tag == q('br') and el.get(q('type')) not in ('page', 'column'): out.append(' ')
    return ''.join(out)

def p_runs(p):
    # các run có chữ (kể cả trong hyperlink/ins), bỏ run trong textbox
    for r in p.iter(q('r')):
        anc = r.getparent()
        skip = False
        while anc is not None and anc is not p:
            if anc.tag in (q('txbxContent'),): skip = True; break
            anc = anc.getparent()
        if skip: continue
        t = ''.join((x.text or '') for x in r.findall(q('t')))
        if t.strip(): yield r, t

HERE = os.path.dirname(os.path.abspath(__file__))
_DR = None
def _do_rong():
    global _DR
    if _DR is None:
        try: _DR = json.load(open(os.path.join(HERE, 'do_rong_chu_TNR.json'), encoding='utf-8'))
        except Exception: _DR = {}
    return _DR

def _w_ch(ch, bold):
    t = _do_rong().get('b' if bold else 'r') or {}
    v = t.get(str(ord(ch)))
    if v is None:
        nf = unicodedata.normalize('NFD', ch)
        v = t.get(str(ord(nf[0])), t.get('110', 1000)) if nf else 1000
    return v

def so_dong(D, P, sect):
    """v4.4 (quyết định D2; PB4-GPT-03, PB4-WORK-05): số dòng hiển thị của đoạn – đếm ngắt dòng (Shift+Enter) và
    ngắt dòng tự động theo bề rộng chữ thực (số đo phông tương thích Times New Roman) trên bề rộng vùng chữ (khổ giấy –
    lề – thụt). Trả về (ít nhất, nhiều nhất) khi chữ rộng/hẹp hơn 3 %; khác nhau là sát ngưỡng → “chưa kiểm”."""
    dr = _do_rong()
    if not dr or sect is None: return None
    pg = sect.find(q('pgSz')); mar = sect.find(q('pgMar'))
    if pg is None or mar is None: return None
    try:
        rong = int(float(pg.get(q('w')))) - int(float(mar.get(q('left'), 0))) - int(float(mar.get(q('right'), 0)))
    except (TypeError, ValueError):
        return None
    pr = P.props
    rong -= (pr.get('ind_l') or 0) + (pr.get('ind_r') or 0)
    dau = rong - (pr['first'] or 0) + (pr['hanging'] or 0)
    upm = dr.get('upm', 2048)
    segs, cur, tu, cach = [], [], 0.0, 0.0
    def chot():
        nonlocal tu, cach
        if tu or cach: cur.append((tu, cach))
        tu, cach = 0.0, 0.0
    for r in P.el.iter(q('r')):
        rp = run_props(D, P.el, r, P.sid)
        k = (rp['sz'] or 24) / 2.0 * 20.0 / upm  # twips trên đơn vị font
        for ch in r:
            if ch.tag == q('t'):
                for c in (ch.text or ''):
                    if c in ' \u00a0':
                        cach += _w_ch(' ', rp['b']) * k
                    else:
                        if cach: chot()
                        tu += _w_ch(c, rp['b']) * k
            elif ch.tag == q('tab'):
                chot(); cur.append(('TAB', 0.0))  # v4.5: nhảy tới điểm dừng tab kế tiếp (tab riêng của đoạn hoặc mặc định 1,27 cm)
            elif (ch.tag == q('br') and ch.get(q('type')) not in ('page', 'column')) or ch.tag == q('cr'):
                chot(); segs.append(cur); cur = []
    chot(); segs.append(cur)
    dung_tab = []
    tabs_el = P.el.find(q('pPr') + '/' + q('tabs'))
    if tabs_el is not None:
        for t_ in tabs_el.findall(q('tab')):
            try:
                if t_.get(q('val')) not in ('clear', 'bar'): dung_tab.append(int(float(t_.get(q('pos')))) - (pr.get('ind_l') or 0))
            except (TypeError, ValueError): pass
    dung_tab.sort()
    def dem(he_so):
        n, dau_doan = 0, True
        for seg in segs:
            n += 1; x = 0.0; cap = dau if dau_doan else rong; dau_doan = False
            for w_, sp_ in seg:
                if w_ == 'TAB':
                    nx = next((t_ for t_ in dung_tab if t_ > x + 1), None)
                    if nx is None: nx = (int(x // 720) + 1) * 720
                    if nx > cap: n += 1; x = 0.0; cap = rong
                    else: x = float(nx)
                    continue
                w_ *= he_so
                if x > 0 and x + w_ > cap:
                    n += 1; x = 0.0; cap = rong
                while w_ > cap > 0:
                    n += 1; w_ -= cap
                x += w_ + sp_ * he_so
        return n
    return dem(0.97), dem(1.03)

def vung_noi_nhan(paras):
    """v4.4 (PB4-GPT-08, PB4-WORK-13): vùng “Nơi nhận” ngoài bảng = dòng “Nơi nhận:” và các dòng ngắn liền sau
    (danh sách nơi nhận, chữ ký) – dừng ở đoạn lời văn dài, đề mục “Điều/Chương/Mục…”, tiêu đề văn bản kèm theo/phụ lục hoặc phần mới.
    Trả về (tập chỉ số đoạn của vùng, danh sách đoạn là dòng nơi nhận “- …”)."""
    vung, ds = set(), []
    for P in paras:
        if P.in_table or not re.match(r'^Nơi nhận\s*(?::|$)', P.text): continue
        vung.add(P.idx)
        for Q in paras[P.idx + 1:]:
            if Q.sec != P.sec: break
            if Q.in_table: continue
            if not Q.text: vung.add(Q.idx); continue
            # v4.5 (PB5-WORK-11): chỉ giữ dòng danh sách (“- …”), dòng in hoa (chức vụ), dòng “(…)”, dòng canh giữa/phải ngắn
            # không kết thúc bằng dấu chấm (họ tên người ký); gặp câu lời văn – kể cả câu ngắn – là dừng
            la_ds = re.match(r'^[-–+•]\s*\S', Q.text) or Q.text.upper() == Q.text or Q.text.startswith('(') or \
                (Q.props['jc'] in ('center', 'right') and len(Q.text) <= 60 and not Q.text.endswith('.'))
            if not la_ds: break
            if len(Q.text) > 100 or re.match(r'^(Điều\s+\d|Chương\s|Mục\s+\d|Phần\s|[IVX]+\.\s|\d+\.\s|Phụ lục\b|PHỤ LỤC\b|QUY ĐỊNH$|QUY CHẾ$|ĐIỀU LỆ$|NỘI QUY$|HƯỚNG DẪN$|QUY TRÌNH$)', Q.text):
                break
            vung.add(Q.idx)
            if re.match(r'^[-–+•]\s*\S', Q.text): ds.append(Q)
    return vung, ds

class Line:
    __slots__ = ('text', 'raw', 'runs', 'all_runs', 'idx', 'in_table', 'props', 'el')

def lines_of(D, P):
    """Tách một đoạn thành các dòng theo ngắt dòng (Shift+Enter); mỗi dòng giữ thuộc tính run."""
    out, cur_t, cur_r = [], [], []
    def flush():
        L = Line(); L.raw = ''.join(cur_t); L.text = norm(L.raw); L.all_runs = list(cur_r); L.runs = [x for x in cur_r if x[1].strip()]
        L.idx = P.idx; L.in_table = P.in_table; L.props = P.props; L.el = P.el
        if L.text: out.append(L)
    for r in P.el.iter(q('r')):
        rp = None
        for ch in r:
            if ch.tag == q('t'):
                if rp is None: rp = run_props(D, P.el, r, P.sid)
                cur_t.append(ch.text or ''); cur_r.append((rp, ch.text or ''))
            elif ch.tag == q('tab'):
                cur_t.append('\t')
            elif (ch.tag == q('br') and ch.get(q('type')) not in ('page', 'column')) or ch.tag == q('cr'):
                flush(); cur_t, cur_r = [], []
    flush()
    return [y for L in out for y in _split_anchor(L)]

_ANCHORS = [r'TRƯỜNG CAO ĐẲNG KON TUM$', r'Độc lập\s*[-–]\s*Tự do', r'ĐẢNG BỘ TRƯỜNG', r'CHI BỘ ', r'\*$']

def _split_anchor(L):
    """Tách các dòng bị gộp vào một đoạn chỉ nhờ tự xuống dòng (vd. “UBND TỈNH QUẢNG NGÃI TRƯỜNG CAO ĐẲNG KON TUM”)."""
    t = L.raw
    cut = None
    for a in _ANCHORS:
        m = re.search(r'\s(' + a.rstrip('$') + ')', t)
        if m and m.start(1) > 3 and t[:m.start(1)].strip():
            cut = m.start(1); break
    if cut is None: return [L]
    parts = []
    for seg_start, seg_end in ((0, cut), (cut, len(t))):
        M = Line(); M.raw = t[seg_start:seg_end]; M.text = norm(M.raw)
        M.idx, M.in_table, M.props, M.el = L.idx, L.in_table, L.props, L.el
        pos, M.runs = 0, []
        allr = [x for x in L.runs]
        # dựng lại vị trí từng run trong raw
        k = 0
        for rp, tx in _runs_with_pos(L):
            a, b = tx
            if b > seg_start and a < seg_end and t[max(a,seg_start):min(b,seg_end)].strip():
                M.runs.append((rp, t[max(a,seg_start):min(b,seg_end)]))
        if M.text: parts.append(M)
    return parts

def _runs_with_pos(L):
    out, pos = [], 0
    t = L.raw
    for rp, tx in L.all_runs:
        i = t.find(tx, pos) if tx else pos
        if i < 0: i = pos
        out.append((rp, (i, i + len(tx)))); pos = i + len(tx)
    return out

# ----------------------------------------------------------------------------
# Duyệt thân văn bản: đoạn, bảng, section
# ----------------------------------------------------------------------------
class Para:
    __slots__ = ('el', 'text', 'idx', 'sec', 'in_table', 'tbl', 'props', 'sid', 'runs', 'la_trich_yeu')

def walk(D):
    paras, tables, sections = [], [], []
    sec = 0
    idx = 0
    def add_par(p, in_table, tbl):
        nonlocal idx
        P = Para(); P.el = p; P.text = norm(p_text(p)); P.idx = idx; P.sec = sec; P.la_trich_yeu = False
        P.in_table = in_table; P.tbl = tbl
        P.props, P.sid = para_props(D, p)
        P.runs = [(run_props(D, p, r, P.sid), t) for r, t in p_runs(p)]
        paras.append(P); idx += 1
        return P
    for ch in D.body:
        if ch.tag == q('p'):
            add_par(ch, False, None)
            sp = ch.find(q('pPr') + '/' + q('sectPr'))
            if sp is not None:
                sections.append(sp); sec += 1
        elif ch.tag == q('tbl'):
            tid = len(tables); tables.append((ch, sec))
            for p in ch.iter(q('p')):
                add_par(p, True, tid)
        elif ch.tag == q('sectPr'):
            sections.append(ch)
    return paras, tables, sections

# ----------------------------------------------------------------------------
# Dựng PDF để biết trang bắt đầu của mỗi phần (tùy chọn)
# Cách làm: chèn một mốc chữ nhỏ (§§Sn§§) vào đoạn đầu của mỗi phần trên bản sao
# tạm, dựng PDF bằng LibreOffice, tìm trang chứa mốc. Tệp gốc không bị sửa.
# ----------------------------------------------------------------------------
def render_section_pages(path, paras, n_sec):
    soffice = shutil.which('soffice') or shutil.which('libreoffice')
    if not soffice or not shutil.which('pdftotext'):
        return None, None
    tmp = tempfile.mkdtemp()
    try:
        zin = zipfile.ZipFile(path)
        doc = etree.fromstring(zin.read('word/document.xml'))
        body = doc.find(q('body'))
        # đoạn đầu (theo thứ tự) của mỗi phần, kể cả trong bảng
        all_p = list(body.iter(q('p')))
        first_idx = {}
        for P in paras:
            if P.sec not in first_idx: first_idx[P.sec] = P.idx
        for si, pi in first_idx.items():
            if pi < len(all_p):
                pe = all_p[pi]
                r = etree.SubElement(pe, q('r'))
                pr = pe.find(q('pPr'))
                if pr is not None:
                    pe.remove(r); pr.addnext(r)
                else:
                    pe.remove(r); pe.insert(0, r)
                t = etree.SubElement(r, q('t')); t.text = 'SSMARK%dSS' % si
        out = os.path.join(tmp, 'mark.docx')
        zout = zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED)
        for it in zin.infolist():
            data = zin.read(it.filename)
            if it.filename == 'word/document.xml':
                data = etree.tostring(doc, xml_declaration=True, encoding='UTF-8', standalone=True)
            zout.writestr(it, data)
        zout.close()
        subprocess.run([soffice, '--headless', '--convert-to', 'pdf', '--outdir', tmp, out],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
        pdf = os.path.join(tmp, 'mark.pdf')
        if not os.path.exists(pdf): return None, None
        txt = subprocess.run(['pdftotext', pdf, '-'], capture_output=True, timeout=120).stdout.decode('utf-8', 'ignore')
        pages = txt.split('\f')
        if pages and not pages[-1].strip(): pages = pages[:-1]
        start = {}
        for si in range(n_sec):
            for i, pg in enumerate(pages):
                if 'SSMARK%dSS' % si in pg.replace(' ', ''):
                    start[si] = i + 1; break
        return len(pages), start
    except Exception:
        return None, None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

# ----------------------------------------------------------------------------
# Kiểm tra
# ----------------------------------------------------------------------------
class Result:
    def __init__(self):
        self.loi = []   # phát hiện
        self.dat = []   # mục đạt (kèm số đo)
        self.chua = []  # chưa kiểm được
    def add(self, ma, hang_muc, vi_tri, do, yeu_cau, can_cu, muc):
        self.loi.append(dict(ma=ma, hang_muc=hang_muc, vi_tri=vi_tri, do=do, yeu_cau=yeu_cau, can_cu=can_cu, muc=muc))
    def ok(self, hang_muc, do, can_cu):
        self.dat.append(dict(hang_muc=hang_muc, do=do, can_cu=can_cu))
    def na(self, hang_muc, ly_do):
        self.chua.append(dict(hang_muc=hang_muc, ly_do=ly_do))

CC_TB = 'TB 597/TB-CĐKT'
CC_HT = 'Chỉ đạo của Hiệu trưởng ngày 26/10/2026 (bảng thông số KTC)'
CC_ND = 'NĐ 30/2020/NĐ-CP, Phụ lục I'
CC_HD = 'HD 05-HD/VPTW'


PHU_DINH = r'(?:chưa|không|chẳng)'


def la_cau_thay_the(text, s, e):
    """v4.3 (TH-08), v4.4 (PB4-WORK-03), v4.5 (PB5-GPT-04, PB5-WORK-05): lần nhắc số hiệu này nằm trong câu NÊU VIỆC văn bản đã bị
    thay thế/bãi bỏ/hết hiệu lực (cụm “thay thế/bãi bỏ” đứng ngay trước, tối đa 4 từ, hoặc “đã được thay thế/hết hiệu lực” ngay sau số hiệu).
    Câu PHỦ ĐỊNH (“chưa được thay thế”, “không bị bãi bỏ”, “chưa hết hiệu lực”, “chưa có văn bản thay thế”) KHÔNG phải câu thay thế.
    Câu nêu việc thay thế mà phần còn lại của câu vẫn cho áp dụng (“… đã hết hiệu lực nhưng vẫn áp dụng …”) cũng KHÔNG được miễn."""
    truoc = re.split(r'[.;]', text[max(0, s - 90):s])[-1].lower()
    sau = text[e:e + 45].lower()
    con_lai = re.split(r'[.;]', text[e:e + 300])[0].lower()
    for mm in re.finditer(r'(?<!\w)(vẫn|tiếp tục)\s+(?:được\s+)?(?:áp dụng|thực hiện|căn cứ|sử dụng|dùng|theo)(?!\w)', con_lai):
        if not re.search(r'(?<!\w)(không|chưa|chấm dứt|thôi|ngừng)(?!\w)[^,]{0,12}$', con_lai[:mm.start()]):
            return False
    m = re.search(r'((?:\S+\s+){0,4})(thay thế|bãi bỏ|hết hiệu lực)(\s+cho)?\s+(?:\S+\s+){0,4}$', truoc + ' ')
    if m and not re.search(r'(?<!\w)' + PHU_DINH + r'(?!\w)', m.group(1)):
        return True
    m2 = re.match(r'^[\s,()]*(?:\S+\s+)?(?:đã\s+)?(?:được\s+|bị\s+)?(?:thay thế|bãi bỏ)|^[\s,()]*(?:\S+\s+)?(?:đã\s+)?hết hiệu lực', sau)
    return bool(m2) and not re.search(r'(?<!\w)' + PHU_DINH + r'(?!\w)', m2.group(0))

PL_RE = re.compile(r'^(phụ lục)(?:\s+(?:số\s+)?([IVXLCDM]+|\d+))?\s*(?:[.:–-]\s*(.+))?$', re.I)

def pl_match(text, jc=None):
    """Nhận dòng tiêu đề phụ lục: “Phụ lục I”, “PHỤ LỤC I”, “PHỤ LỤC I. DANH MỤC …”, “Phụ lục I. Danh mục …” (PB-03, PB2-02).
    Viết liền chữ thường chỉ nhận khi đoạn canh giữa (tránh nhận nhầm câu văn bắt đầu bằng “Phụ lục …”)."""
    t = (text or '').strip()
    if len(t) > 160: return None
    m = PL_RE.match(t)
    if not m: return None
    tail = m.group(3)
    if tail and tail.upper() != tail and jc != 'center': return None
    if not m.group(2) and tail is None and t.lower() != 'phụ lục': return None
    return m

_KHO = None
def load_kho():
    """Đọc kho_manifest.json của gói (một nguồn duy nhất cho văn bản bị thay thế và VBHN – PB-18)."""
    global _KHO
    if _KHO is None:
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'Kho-Du-Lieu-897', 'kho_manifest.json')
        try: _KHO = json.load(open(p, encoding='utf-8'))
        except Exception: _KHO = {}
    return _KHO

def sec_kind(paras, si, n_sec):
    """Loại phần: chinh / kem_theo / phu_luc (dựa vào nội dung đầu phần)."""
    texts = [P for P in paras if P.sec == si and P.text]
    if si == 0:
        # v4.4 (PB4-WORK-12): tệp riêng mở đầu bằng tiêu đề phụ lục / văn bản kèm theo, không có quốc hiệu, “Số:” → không phải văn bản chính
        if not any(re.search(r'CỘNG H(?:ÒA|OÀ) XÃ HỘI|ĐẢNG CỘNG SẢN VIỆT NAM|^Số\b', P.text) for P in texts[:12]):
            ngoai = [P for P in texts if not P.in_table][:5]
            if ngoai and pl_match(ngoai[0].text, 'center'): return 'phu_luc', ngoai[0]
            for P in ngoai[:3]:
                if re.match(r'^(QUY ĐỊNH|QUY CHẾ|ĐIỀU LỆ|NỘI QUY|HƯỚNG DẪN|QUY TRÌNH|CHƯƠNG TRÌNH|KẾ HOẠCH|ĐỀ ÁN|DANH MỤC)\b', P.text) and P.text.upper() == P.text:
                    return 'kem_theo', P
        return 'chinh', texts[0] if texts else None
    for k_, P in enumerate(texts[:12]):
        # v4.3 (TH-13): dòng đầu tiên của phần (section) mới nhận là dòng phụ lục bất kể canh lề
        if pl_match(P.text, 'center' if k_ == 0 and not P.in_table else P.props['jc']): return 'phu_luc', P
    for P in texts[:12]:
        if re.match(r'^(QUY ĐỊNH|QUY CHẾ|ĐIỀU LỆ|NỘI QUY|HƯỚNG DẪN|QUY TRÌNH|CHƯƠNG TRÌNH|KẾ HOẠCH|ĐỀ ÁN|DANH MỤC)\b', P.text) and P.text.upper() == P.text:
            return 'kem_theo', P
    return 'khac', texts[0] if texts else None

def hf_refs(sect):
    out = {}
    for t in ('headerReference', 'footerReference'):
        for e in sect.findall(q(t)):
            out[(t, e.get(q('type')))] = e.get(q('id'), e.get('{%s}id' % R))
    return out

def has_page_field(x):
    if x is None: return False
    for e in x.iter():
        if e.tag == q('fldSimple') and 'PAGE' in (e.get(q('instr')) or '').upper().split():
            return True
        if e.tag == q('instrText') and re.search(r'\bPAGE\b', (e.text or '').upper()):
            return True
    return False

def page_field_props(D, x):
    """Cỡ chữ và canh lề của đoạn chứa trường PAGE trong header/footer."""
    if x is None: return None
    for p in x.iter(q('p')):
        found = False
        for e in p.iter():
            if (e.tag == q('fldSimple') and 'PAGE' in (e.get(q('instr')) or '').upper()) or \
               (e.tag == q('instrText') and re.search(r'\bPAGE\b', (e.text or '').upper())):
                found = True
        if found:
            pr, sid = para_props(D, p)
            sz = None
            for r in p.iter(q('r')):
                rp = run_props(D, p, r, sid)
                if rp['sz']: sz = rp['sz']
            return dict(jc=pr['jc'], sz=sz)
    return None

def check(path, he='auto', do_render=True):
    D = Doc(path)
    paras, tables, sections = walk(D)
    R_ = Result()
    full = ' '.join(P.text for P in paras)
    if he == 'auto':
        head = [L.text.upper() for P in paras[:15] for L in lines_of(D, P)]
        has_dang = any(t.strip() == 'ĐẢNG CỘNG SẢN VIỆT NAM' for t in head)
        has_qh = any(re.search(r'CỘNG H(?:ÒA|OÀ) XÃ HỘI CHỦ NGHĨA VIỆT NAM', t) for t in head)
        he = 'dang' if (has_dang and not has_qh) else 'chinh_quyen'
    S = PROFILE[he]
    cc_main = CC_HD if he == 'dang' else CC_TB
    n_sec = len(sections)
    kind0 = sec_kind(paras, 0, n_sec)[0]  # v4.4 (PB4-WORK-12): tệp phụ lục/văn bản kèm theo nộp riêng

    # ---------------- 1. Khổ giấy, lề, header/footer ----------------
    for si, sp in enumerate(sections):
        pgSz = sp.find(q('pgSz')); pgMar = sp.find(q('pgMar'))
        lab = 'Phần %d/%d' % (si + 1, n_sec)
        if pgSz is not None:
            w_, h_ = int(pgSz.get(q('w'), 0)), int(pgSz.get(q('h'), 0))
            orient = pgSz.get(q('orient'))
            dims = sorted([w_, h_])
            if abs(dims[0] - 11906) > 30 or abs(dims[1] - 16838) > 30:
                R_.add('TT-01', 'Khổ giấy', lab, '%d × %d twips' % (w_, h_), 'A4 (11906 × 16838 twips; không dùng Letter)', (CC_HD + ' mục IV') if he == 'dang' else (CC_ND + ' mục I.1; ' + CC_HT), 'Mức 2')
            else:
                R_.ok('Khổ giấy (%s)' % lab, 'A4 %d × %d twips%s' % (w_, h_, ', ngang' if orient == 'landscape' else ''), (CC_HD + ' mục IV') if he == 'dang' else (CC_ND + ' mục I.1'))
        if pgMar is not None:
            m = {k: int(float(pgMar.get(q(k), 0))) for k in ('top', 'bottom', 'left', 'right', 'header', 'footer')}
            land = pgSz is not None and pgSz.get(q('orient')) == 'landscape'
            want = dict(top=S['top'], bottom=S['bottom'], left=S['left'], right=S['right'])
            bad = [k for k in want if abs(abs(m[k]) - want[k]) > TOL]
            if land:
                R_.na('Lề trang %s (trang ngang)' % lab, 'Phần trình bày ngang: đối chiếu theo vùng trình bày dọc, người kiểm tra xem bản dựng')
            elif bad:
                R_.add('TT-02', 'Lề trang', lab,
                       'trên %s, dưới %s, trái %s, phải %s' % tuple(twip_cm(abs(m[k])) for k in ('top', 'bottom', 'left', 'right')),
                       'trên %s, dưới %s, trái %s, phải %s' % tuple(twip_cm(want[k]) for k in ('top', 'bottom', 'left', 'right')),
                       (CC_HD + ' mục IV.4') if he == 'dang' else (CC_HT + '; ' + CC_ND + ' mục I.3'), 'Mức 2')
            else:
                R_.ok('Lề trang (%s)' % lab, 'trên %s, dưới %s, trái %s, phải %s' % tuple(twip_cm(abs(m[k])) for k in ('top', 'bottom', 'left', 'right')),
                      (CC_HD + ' mục IV.4') if he == 'dang' else CC_HT)
            hf_bad = []
            if S['header'] is not None and abs(m['header'] - S['header']) > TOL: hf_bad.append('header %s' % twip_cm(m['header']))
            if S['footer'] is not None and abs(m['footer'] - S['footer']) > TOL: hf_bad.append('footer %s' % twip_cm(m['footer']))
            if hf_bad:
                R_.add('TT-03', 'Khoảng cách header/footer', lab, ', '.join(hf_bad),
                       ('header 1,00 cm (số trang cách mép trên 10 mm)' if he == 'dang' else 'header 1,27 cm, footer 1,27 cm'),
                       (CC_HD + ' mục IV.5.1') if he == 'dang' else CC_HT, 'Mức 2')
            else:
                R_.ok('Header/footer (%s)' % lab, 'header %s, footer %s' % (twip_cm(m['header']), twip_cm(m['footer'])), CC_HT if he != 'dang' else CC_HD)

    # ---------------- 2. Phông chữ ----------------
    bad_font = {}
    for P in paras:
        for rp, t in P.runs:
            f = rp['font']
            if f and 'Times New Roman' not in f:
                bad_font.setdefault(f, []).append(P.idx)
    if bad_font:
        for f, ids in bad_font.items():
            R_.add('TT-04', 'Phông chữ', 'Đoạn %s%s' % (', '.join(str(i + 1) for i in ids[:6]), '…' if len(ids) > 6 else ''),
                   f, 'Times New Roman, Unicode', (CC_HD + ' Phụ lục 2') if he == 'dang' else (CC_ND + ' mục I.4'), 'Mức 2')
    else:
        R_.ok('Phông chữ', 'Mọi đoạn có chữ dùng Times New Roman (theo kiểu hoặc định dạng trực tiếp)', (CC_HD + ' Phụ lục 2') if he == 'dang' else (CC_ND + ' mục I.4'))

    # ---------------- 3. Nhận diện các thành phần thể thức ----------------
    def runs_sz(P):
        szs = [rp['sz'] for rp, t in P.runs if rp['sz']]
        return max(set(szs), key=szs.count) if szs else None
    def all_bold(P): return bool(P.runs) and all(rp['b'] for rp, t in P.runs)
    def all_ital(P): return bool(P.runs) and all(rp['i'] for rp, t in P.runs)
    def any_bold(P): return any(rp['b'] for rp, t in P.runs)

    def expect(P, ma, ten, sz=None, bold=None, ital=None, can_cu=cc_main, muc='Mức 2'):
        loi = []
        s = runs_sz(P)
        szs_ok = tuple(sz) if isinstance(sz, (tuple, list)) else ((sz,) if sz is not None else None)
        if szs_ok and s is not None and s not in szs_ok: loi.append('cỡ %s (yêu cầu %s)' % (hp_pt(s), '–'.join(hp_pt(x) for x in szs_ok)))
        if bold is True and not all_bold(P): loi.append('chưa đậm toàn bộ')
        if bold is False and any_bold(P): loi.append('có chữ đậm (yêu cầu không đậm)')
        if ital is True and not all_ital(P): loi.append('chưa nghiêng toàn bộ')
        if ital is False and any(rp['i'] for rp, t in P.runs): loi.append('có chữ nghiêng (yêu cầu đứng)')
        if loi:
            R_.add(ma, ten, 'Đoạn %d: “%s”' % (P.idx + 1, P.text[:60]), '; '.join(loi),
                   '%s%s%s' % (('cỡ %s' % '–'.join(hp_pt(x) for x in szs_ok)) if szs_ok else '', ', đậm' if bold else (', không đậm' if bold is False else ''), ', nghiêng' if ital else ''),
                   can_cu, muc)
        else:
            R_.ok(ten, '“%s” – cỡ %s%s%s' % (P.text[:50], hp_pt(s), ', đậm' if all_bold(P) else '', ', nghiêng' if all_ital(P) else ''), can_cu)

    first = lambda pred: next((P for P in paras if pred(P)), None)
    head_lines = [L for P in paras[:40] if P.in_table for L in lines_of(D, P)]
    firstL = lambda pred: next((L for L in head_lines if pred(L)), None)
    if he == 'chinh_quyen':
        P = firstL(lambda P: re.search(r'CỘNG H(?:ÒA|OÀ) XÃ HỘI CHỦ NGHĨA VIỆT NAM', P.text.upper()))
        if P: expect(P, 'TT-10', 'Quốc hiệu', 26, True, False, CC_TB + ' mục 1.2')
        P = firstL(lambda P: re.match(r'^Độc lập\s*[-–]\s*Tự do\s*[-–]\s*Hạnh phúc', P.text))
        if P:
            expect(P, 'TT-11', 'Tiêu ngữ', 28, True, False, CC_TB + ' mục 1.2')
            if '–' in P.text:
                R_.add('TT-11', 'Tiêu ngữ – dấu gạch nối', 'Đoạn %d' % (P.idx + 1), '“%s” dùng gạch ngang dài (–)' % P.text, 'gạch nối (-): “Độc lập - Tự do - Hạnh phúc”', CC_TB + ' mục 1.2', 'Mức 2')
        P = firstL(lambda P: P.text.upper().startswith('UBND TỈNH'))
        if P:
            if P.text.strip().upper() != 'UBND TỈNH QUẢNG NGÃI':
                R_.add('TT-12', 'Tên cơ quan chủ quản', 'Đoạn %d' % (P.idx + 1), P.text, 'UBND TỈNH QUẢNG NGÃI', CC_TB + ' mục 2.1', 'Mức 2')
            expect(P, 'TT-12', 'Tên cơ quan chủ quản', 26, False, False, CC_TB + ' mục 2.2')
        P = firstL(lambda P: P.text.strip().upper() == 'TRƯỜNG CAO ĐẲNG KON TUM')
        if P: expect(P, 'TT-13', 'Tên đơn vị ban hành', 26, True, False, CC_TB + ' mục 2.2')
        P = firstL(lambda P: P.text.startswith('Số:'))
        if P:
            expect(P, 'TT-14', 'Số, ký hiệu', 26, None, False, CC_TB + ' mục 3.2')
            raw = P.raw
            mm = re.match(r'Số:(\s*)(\d*)\s*/', raw)
            if mm and not mm.group(2) and len(mm.group(1).replace('\t', '      ')) < 6:
                R_.add('TT-14', 'Khoảng trống sau “Số:”', 'Đoạn %d' % (P.idx + 1), '%d ký tự trống' % len(mm.group(1)), 'tối thiểu 6 ký tự trống', CC_TB + ' mục 3.1 (lưu ý)', 'Mức 2')
        P = firstL(lambda P: re.search(r', ngày', P.text) and 'tháng' in P.text)
        if P:
            if not P.text.startswith('Quảng Ngãi'):
                R_.add('TT-15', 'Địa danh', 'Đoạn %d' % (P.idx + 1), P.text[:40], 'Quảng Ngãi, ngày … tháng … năm …', CC_TB + ' mục 4.1', 'Mức 2')
            expect(P, 'TT-15', 'Địa danh, ngày tháng', 28, False, True, CC_TB + ' mục 4.2')
            raw = P.raw
            mm = re.search(r'ngày(\s*)(\d*)\s*tháng', raw)
            if mm and not mm.group(2) and len(mm.group(1)) < 6:
                R_.add('TT-15', 'Khoảng trống ngày', 'Đoạn %d' % (P.idx + 1), '%d ký tự trống giữa “ngày” và “tháng”' % len(mm.group(1)), '6 ký tự trống', CC_TB + ' mục 4.1 (lưu ý)', 'Mức 2')
    else:
        P = first(lambda P: 'ĐẢNG CỘNG SẢN VIỆT NAM' in P.text.upper())
        if P: expect(P, 'TT-10', 'Tiêu đề “ĐẢNG CỘNG SẢN VIỆT NAM”', 30, True, False, CC_HD + ' Phụ lục 2')

    # Tên loại + trích yếu (phần đầu văn bản chính, ngoài bảng)
    TEN_LOAI = r'^(QUYẾT ĐỊNH|THÔNG BÁO|KẾ HOẠCH|BÁO CÁO|TỜ TRÌNH|QUY ĐỊNH|QUY CHẾ|HƯỚNG DẪN|CHƯƠNG TRÌNH|ĐỀ ÁN|PHƯƠNG ÁN|BIÊN BẢN|NGHỊ QUYẾT|KẾT LUẬN|CHỈ THỊ)$'
    tl = first(lambda P: not P.in_table and P.sec == 0 and re.match(TEN_LOAI, P.text))
    if tl:
        expect(tl, 'TT-16', 'Tên loại văn bản', S['ten_loai_sz'], True, False, (CC_TB + ' mục 5.2') if he != 'dang' else CC_HD + ' Phụ lục 2 mục 5a')
        nxt = [P for P in paras if P.idx > tl.idx and not P.in_table and P.text][:3]
        for P in nxt:
            # trích yếu: chỉ các đoạn CANH GIỮA liền ngay sau tên loại; gặp đoạn không canh giữa là hết (PB-02)
            if P.props['jc'] != 'center': break
            if P.text.isupper() or P.text.startswith('Căn cứ') or P.text.startswith('Kính gửi') or P.text.startswith('-----'): break
            expect(P, 'TT-17', 'Trích yếu', S['trich_yeu_sz'], True, False, (CC_TB + ' mục 5.2') if he != 'dang' else CC_HD + ' Phụ lục 2 mục 5a')
            P.la_trich_yeu = True
            if P.text.endswith('.'): break
    # v4.5 (PB5-WORK-17): trích yếu công văn “V/v …” – cỡ 13, in thường, đứng (trong hoặc ngoài bảng đầu văn bản)
    if he != 'dang':
        vv = next((P for P in paras[:40] if P.sec == 0 and re.match(r'^V/v\b', P.text)), None)
        if vv: expect(vv, 'TT-17', 'Trích yếu công văn (V/v)', 26, False, False, CC_TB + ' mục 5.2')
    # Căn cứ
    cc = [P for P in paras if P.sec == 0 and not P.in_table and P.text.startswith('Căn cứ')]
    if cc and he != 'dang':
        bad_i = [P for P in cc if not all_ital(P)]
        bad_s = [P for P in cc if runs_sz(P) not in (None, S['body_sz'])]
        if bad_i or bad_s:
            R_.add('TT-18', 'Định dạng căn cứ ban hành', 'Đoạn %s' % ', '.join(str(P.idx + 1) for P in (bad_i + bad_s)[:6]),
                   ('%d đoạn chưa nghiêng' % len(bad_i) if bad_i else '') + (('; %d đoạn sai cỡ chữ' % len(bad_s)) if bad_s else ''),
                   'in thường, nghiêng, cỡ 14', CC_TB + ' mục 6', 'Mức 2')
        else:
            R_.ok('Căn cứ ban hành', '%d đoạn căn cứ: nghiêng, cỡ 14' % len(cc), CC_TB + ' mục 6')
        # dấu câu cuối mỗi căn cứ
        lenh = next((P for P in paras if P.sec == 0 and not P.in_table and re.match(r'^(QUYẾT ĐỊNH|QUYẾT NGHỊ|BAN HÀNH)\s*:', P.text)), None)
        seq = [P for P in paras if lenh is not None and P.idx < lenh.idx and P.sec == 0 and not P.in_table and (P.text.startswith('Căn cứ') or P.text.startswith('Xét đề nghị') or P.text.startswith('Theo đề nghị'))]
        for k, P in enumerate(seq):
            want = '.' if k == len(seq) - 1 else ';'
            if not P.text.rstrip().endswith(want):
                R_.add('TB-03', 'Dấu câu cuối căn cứ', 'Đoạn %d: “…%s”' % (P.idx + 1, P.text[-30:]), 'kết thúc bằng “%s”' % P.text.rstrip()[-1:], 'mỗi căn cứ kết thúc “;”, dòng cuối (trước “QUYẾT ĐỊNH:”) kết thúc “.”', 'NĐ 30/2020/NĐ-CP Phụ lục I mục II.6', 'Mức 3')
    # Nơi nhận
    vung_nn, ds_nn = vung_noi_nhan(paras)
    for P in paras:
        if re.match(r'^Nơi nhận\s*(?::|$)', P.text):
            s = runs_sz(P)
            if he != 'dang' and not re.match(r'^Nơi nhận\s*:', P.text):  # v4.5 (PB5-WORK-12)
                R_.add('TT-19', 'Từ “Nơi nhận:”', 'Đoạn %d' % (P.idx + 1), 'thiếu dấu hai chấm (“%s”)' % P.text[:20], '“Nơi nhận:” – sau có dấu hai chấm', CC_TB + ' mục 9', 'Mức 2')
            if he != 'dang':
                runs_nn = [(rp, t) for rp, t in P.runs if 'Nơi' in unicodedata.normalize('NFC', t)]
                if runs_nn and (runs_nn[0][0]['sz'] != S['noi_nhan_label_sz'] or not runs_nn[0][0]['b'] or not runs_nn[0][0]['i']):
                    R_.add('TT-19', 'Từ “Nơi nhận:”', 'Đoạn %d' % (P.idx + 1), 'cỡ %s%s%s' % (hp_pt(runs_nn[0][0]['sz']), ', đậm' if runs_nn[0][0]['b'] else ', không đậm', ', nghiêng' if runs_nn[0][0]['i'] else ', đứng'),
                           'cỡ 12, nghiêng, đậm', CC_TB + ' mục 9', 'Mức 2')
                else:
                    R_.ok('Từ “Nơi nhận:”', 'cỡ 12, nghiêng, đậm', CC_TB + ' mục 9')
            # danh sách nơi nhận: các run sau nhãn
            after, nghieng, nhan_xong, acc = [], [], False, ''
            for rp, t in P.runs:
                if not nhan_xong:  # bỏ các run thuộc nhãn “Nơi nhận:” (kể cả dấu hai chấm tách run riêng)
                    acc += unicodedata.normalize('NFC', t)  # v4.5: chữ trong run có thể ở dạng tổ hợp (NFD)
                    if ':' in acc or len(acc.strip()) > len('Nơi nhận') + 2: nhan_xong = True
                    if 'Nơi nhận' in acc or not acc.strip() or acc.strip() in ('Nơi', 'Nơi nhận'): continue
                if t.strip() and t.strip() != ':': after.append(rp['sz']); nghieng.append(rp['i'])
            same_cell = []
            if P.in_table:
                cell = P.el.getparent()
                for p2 in cell.findall(q('p')):
                    if p2 is P.el or re.match(r'^Nơi nhận', norm(p_text(p2))): continue  # v4.5: không tính chính dòng nhãn
                    pr2, sid2 = para_props(D, p2)
                    for r2, t2 in p_runs(p2):
                        rp2 = run_props(D, p2, r2, sid2); same_cell.append(rp2['sz']); nghieng.append(rp2['i'])
            if not P.in_table:  # v4.4 (PB4-WORK-13): danh sách nơi nhận đặt ngoài bảng – đo từng dòng “- …”
                same_cell = [rp['sz'] for Q in ds_nn if Q.idx > P.idx for rp, t in Q.runs if t.strip()]
                nghieng += [rp['i'] for Q in ds_nn if Q.idx > P.idx for rp, t in Q.runs if t.strip()]
            if he != 'dang' and any(nghieng):  # v4.5 (PB5-WORK-12): TB 597 mục 9 – danh sách nơi nhận kiểu chữ đứng
                R_.add('TT-19', 'Danh sách nơi nhận – kiểu chữ', 'Đoạn %d trở đi' % (P.idx + 1), 'có chữ nghiêng', 'cỡ 11, kiểu chữ đứng', CC_TB + ' mục 9', 'Mức 2')
            szs = [x for x in after + same_cell if x]
            if szs:
                badn = [x for x in szs if x != S['noi_nhan_sz']]
                if badn:
                    R_.add('TT-19', 'Danh sách nơi nhận', 'Đoạn %d trở đi' % (P.idx + 1), 'cỡ %s' % ', '.join(sorted(set(hp_pt(x) for x in badn))), 'cỡ %s' % hp_pt(S['noi_nhan_sz']), cc_main + ' (Nơi nhận)', 'Mức 2')
                else:
                    R_.ok('Danh sách nơi nhận', 'cỡ %s' % hp_pt(S['noi_nhan_sz']), cc_main)
            break

    # ---------------- 4. Đoạn lời văn: canh lề, cỡ chữ, giãn đoạn, giãn dòng, thụt đầu dòng ----------------
    # Quyết định D2 của Hiệu trưởng 27/10/2026; v4.4–v4.5 (phản biện lần 4, lần 5): phân vùng theo VAI TRÒ trước khi đo.
    #   Không đo: đầu văn bản, tên loại – trích yếu, vùng tiêu đề đầu mỗi phần, dòng in hoa, “Số:”, “V/v”, “Kính gửi”, địa danh – ngày,
    #   quốc hiệu – tiêu ngữ, vùng “Nơi nhận” (dòng danh sách, chức vụ, họ tên; dừng ở câu lời văn đầu tiên), khối chữ ký, dòng phụ lục,
    #   đề mục canh giữa “Chương/Mục/Phần …” và TÊN của đề mục đó (một dòng đậm/nghiêng ngay dưới).
    #   Đo cỡ chữ, khoảng cách đoạn, giãn dòng, thụt đầu dòng ở MỌI đoạn lời văn còn lại (kể cả đề mục “Điều …”, câu ngắn, đoạn canh giữa/phải);
    #   TT-24 (dàn đều) chỉ xét đoạn NHIỀU DÒNG theo số dòng thật (so_dong); sát ngưỡng → chưa kiểm. Lời văn trong bảng: không đo, ghi “chưa kiểm”.
    dau_phan = {}
    for P in paras:
        if P.text and not P.in_table and P.sec not in dau_phan: dau_phan[P.sec] = P.idx
    if dau_phan.get(0) is not None and kind0 == 'chinh': dau_phan.pop(0)  # văn bản chính: dòng đầu không phải dòng phụ lục
    tieu_de_phan = set()  # các đoạn canh giữa/phải liên tiếp ở đầu mỗi phần (tên loại, trích yếu, dòng “(Ban hành kèm theo…)”)
    for si_ in range(n_sec):
        for P in [P for P in paras if P.sec == si_ and not P.in_table]:
            if not P.text: continue
            if P.props['jc'] in ('center', 'right') or P.text.upper() == P.text: tieu_de_phan.add(P.idx)
            else: break
    chu_ky = set()
    for P in paras:
        if not P.in_table and P.text and P.text.upper() == P.text and len(P.text) <= 80 and \
                re.search(r'(HIỆU TRƯỞNG|GIÁM ĐỐC|BÍ THƯ|CHỦ TỊCH|TRƯỞNG|T/M|TM\.|KT\.|TL\.|TUQ\.|Q\. )', P.text):
            for Q in paras[P.idx + 1:P.idx + 6]:
                if Q.in_table or Q.sec != P.sec: break
                if not Q.text: continue
                if len(Q.text) > 60 or Q.props['jc'] in ('both', 'distribute'): break
                chu_ky.add(Q.idx)
    def toan_bo(P, key):
        rr = [rp for rp, t in P.runs if t.strip()]
        return bool(rr) and all(rp.get(key) for rp in rr)
    def la_dong_pl(P):
        return bool(pl_match(P.text, 'center' if dau_phan.get(P.sec) == P.idx else P.props['jc']))
    _sd = {}
    def dong(P):
        if P.idx not in _sd: _sd[P.idx] = so_dong(D, P, sections[P.sec] if P.sec < len(sections) else (sections[-1] if sections else None))
        return _sd[P.idx]
    def mot_dong(P):
        d_ = dong(P)
        return d_[1] == 1 if d_ else len(P.text) <= 100
    _td_kem = set()
    def la_loi_van(P):
        if not P.text or P.in_table or P.la_trich_yeu or P.idx in vung_nn or P.idx in tieu_de_phan or P.idx in chu_ky: return False
        if P.text.upper() == P.text: return False  # dòng tiêu đề in hoa, “QUYẾT ĐỊNH:”
        if la_dong_pl(P): return False
        if re.match(r'^(Số\s*:|Số\s+\S*-|Kính gửi|Quảng Ngãi, ngày|Kon Tum, ngày|\(|\*)', P.text): return False
        if P.props['jc'] in ('center', 'right') and re.search(r'^V/v\b|CỘNG H(?:ÒA|OÀ) XÃ HỘI CHỦ NGHĨA|Độc lập\s*[-–]\s*Tự do|ĐẢNG CỘNG SẢN VIỆT NAM', P.text):
            return False  # trích yếu công văn, quốc hiệu – tiêu ngữ (kể cả dòng mẫu minh họa)
        if P.props['jc'] in ('center', 'right'):
            if re.match(r'^(Chương|Mục|Phần|Tiểu mục)\s', P.text): return False  # đề mục canh giữa
            # v4.5 (PB5-WORK-07): một dòng đậm/nghiêng chỉ miễn khi là TÊN của đề mục “Chương/Mục/Phần” đứng ngay trên và không kết thúc bằng dấu chấm
            #   hoặc dòng trích yếu (đậm/nghiêng toàn bộ) ngay dưới dòng tên loại in hoa (QUY ĐỊNH, QUYẾT ĐỊNH…) hoặc dưới một dòng trích yếu như thế
            truoc_ = next((Q for Q in reversed(paras[:P.idx]) if Q.text and not Q.in_table), None)
            if (toan_bo(P, 'b') or toan_bo(P, 'i')) and not re.search(r'[^.…]\.$', P.text) and truoc_ is not None:  # dấu chấm kết câu (không tính “……”)
                if mot_dong(P) and re.match(r'^(Chương|Mục|Phần|Tiểu mục)\s+\S+$', truoc_.text, re.I): return False
                if len(P.text) <= 200 and (truoc_.text.upper() == truoc_.text or truoc_.idx in _td_kem): _td_kem.add(P.idx); return False
        return True
    body = [P for P in paras if la_loi_van(P)]
    _tbl_cache = {}
    def bang_noi_dung(P):  # bảng nội dung (không phải bảng đầu văn bản, bảng Nơi nhận – chữ ký)
        t_ = P.el
        while t_ is not None and t_.tag != q('tbl'): t_ = t_.getparent()
        if t_ is None: return False
        if id(t_) not in _tbl_cache:
            ds_ = [norm(p_text(p_)) for p_ in t_.iter(q('p'))]  # v4.5 (PB5-WORK-13): chỉ loại bảng đầu văn bản, bảng Nơi nhận – chữ ký
            _tbl_cache[id(t_)] = not any(re.match(r'^(Nơi nhận\s*(?::|$)|CỘNG H(?:ÒA|OÀ) XÃ HỘI|ĐẢNG CỘNG SẢN|Độc lập\s*[-–])', x) for x in ds_)
        return _tbl_cache[id(t_)]
    # v4.4 (PB4-WORK-11): mọi đoạn có chữ (không chỉ số thứ tự, không in hoa toàn bộ) trong bảng nội dung, kể cả câu ngắn
    n_bang = sum(1 for P in paras if P.in_table and re.search(r'[a-zà-ỹđ]', P.text) and bang_noi_dung(P))
    if n_bang:
        R_.na('Lời văn trong bảng', '%d đoạn chữ trong bảng không đo TT-20…TT-24 (bảng theo TT-50, TT-51) – quyết định D2 ngày 27/10/2026' % n_bang)
    bad_sz, bad_bef, bad_aft, bad_line, bad_ind, bad_jc, bad_gap = [], [], [], [], [], [], []
    sat_nguong, co_nhieu = [], []
    for P in body:
        s = runs_sz(P)
        if s is not None and s not in S['body_szs']:
            bad_sz.append((P, s))
        pr = P.props
        d_ = dong(P)  # v4.4 (D2): TT-24 chỉ đoạn nhiều dòng – đếm số dòng thật; sát ngưỡng một/hai dòng → chưa kiểm
        nhieu = (d_[0] > 1) if d_ else (len(P.text) > 100)
        if d_ and d_[0] == 1 and d_[1] > 1: sat_nguong.append(P)
        if nhieu: co_nhieu.append(P)
        if nhieu and pr['jc'] not in ('both', 'distribute'): bad_jc.append((P, pr['jc'] or 'left'))
        if he != 'dang':
            if pr['before'] is None or pr['before'] < 120: bad_bef.append(P)
            if pr['after'] is None or pr['after'] < 120: bad_aft.append(P)
        line, rule = pr['line'], pr['rule'] or 'auto'
        if he == 'dang':  # v4.3 (TH-09): HD 05 Phần II mục 6.2.2 – “từ 18pt đến 22pt (Exactly)”
            if line is None: bad_line.append((P, 'Single (mặc định)'))
            elif rule != 'exact': bad_line.append((P, ('%.2f dòng' % (line / 240)) if rule == 'auto' else '%g pt %s' % (line / 20, rule)))
            elif line < S['line_min_exact'] or line > S['line_max_exact']: bad_line.append((P, '%g pt exactly' % (line / 20)))
        elif line is None:
            pass
        elif rule == 'auto':
            if (S['line_min_auto'] and line < S['line_min_auto']) or (S['line_max_auto'] and line > S['line_max_auto']):
                bad_line.append((P, '%.2f dòng' % (line / 240)))
        else:  # v4.4: TB 597 mục 6 (đính chính của Hiệu trưởng ngày 27/10/2026) – chỉ kiểu theo dòng; Exactly/At least là TT-22
            bad_line.append((P, '%g pt %s' % (line / 20, {'exact': 'Exactly', 'atLeast': 'At least'}.get(rule, rule))))
        fl = pr['first']
        if fl is None or fl < S['indent_min'] - TOL or fl > S['indent_max'] + TOL:
            bad_ind.append((P, fl))
    n_gap = 0
    if he == 'dang':  # v4.3 (TH-10, quyết định D1 ngày 27/10/2026): khoảng cách thực giữa hai đoạn liền nhau = After đoạn trên + Before đoạn dưới ≥ 6 pt
        for P, Q in zip(body, body[1:]):
            if Q.idx != P.idx + 1: continue
            n_gap += 1
            gap = (P.props['after'] or 0) + (Q.props['before'] or 0)
            if gap < 120: bad_gap.append((P, gap))
    n = len(body)
    n_jc = len(co_nhieu)
    if sat_nguong:
        R_.na('Canh đều đoạn sát ngưỡng một dòng', 'Đoạn %s: số dòng hiển thị sát ngưỡng một/hai dòng, không kết luận TT-24 – người soạn thảo xem trong Word' % ', '.join(str(P.idx + 1) for P in sat_nguong[:8]))
    def ids(lst): return ', '.join(str((x[0] if isinstance(x, tuple) else x).idx + 1) for x in lst[:8]) + ('…' if len(lst) > 8 else '')
    cc_lv = (CC_HD + ' Phần II mục 6.2.2') if he == 'dang' else (CC_TB + ' mục 6')
    if n == 0:
        R_.na('Đoạn lời văn', 'không nhận được đoạn lời văn nào – người kiểm tra xem tệp')
    if bad_jc:
        R_.add('TT-24', 'Canh lề lời văn', 'Đoạn %s (%d/%d đoạn dài hơn một dòng)' % (ids(bad_jc), len(bad_jc), n_jc), 'canh %s' % ', '.join(sorted(set(v for _, v in bad_jc))),
               'dàn đều hai lề (Justify)', cc_lv, 'Mức 2')
    elif n_jc:
        R_.ok('Canh lề lời văn', 'dàn đều hai lề ở %d/%d đoạn lời văn dài hơn một dòng' % (n_jc, n_jc), cc_lv)
    if bad_sz:
        R_.add('TT-20', 'Cỡ chữ phần nội dung', 'Đoạn %s (%d/%d đoạn)' % (ids(bad_sz), len(bad_sz), n), 'cỡ %s' % ', '.join(sorted(set(hp_pt(s) for _, s in bad_sz))),
               ('cỡ 14–15 (HD 05 Phụ lục 2 mục 6a)' if he == 'dang' else 'cỡ 14 cho toàn bộ phần lời văn'), (CC_HD + ' Phụ lục 2') if he == 'dang' else (CC_TB + ' mục 6; ' + CC_HT), 'Mức 2')
    elif n:
        R_.ok('Cỡ chữ phần nội dung', '%d/%d đoạn lời văn cỡ %s' % (n, n, '14–15' if he == 'dang' else '14'), (CC_HD + ' Phụ lục 2') if he == 'dang' else (CC_TB + ' mục 6'))
    if he == 'dang':
        if bad_gap:
            R_.add('TT-21', 'Khoảng cách giữa các đoạn', 'Sau đoạn %s (%d/%d cặp đoạn liền nhau)' % (ids(bad_gap), len(bad_gap), n_gap), ', '.join(sorted(set('%g pt' % (g / 20) for _, g in bad_gap))),
                   'After đoạn trên + Before đoạn dưới ≥ 6 pt (Spacing tối thiểu 6 pt)', CC_HD + ' Phần II mục 6.2.2; quyết định D1 của Hiệu trưởng ngày 27/10/2026', 'Mức 2')
        elif n_gap:
            R_.ok('Khoảng cách giữa các đoạn', '≥ 6 pt ở %d/%d cặp đoạn liền nhau' % (n_gap, n_gap), CC_HD + ' Phần II mục 6.2.2')
    elif bad_bef or bad_aft:
        R_.add('TT-21', 'Khoảng cách đoạn (Before/After)', 'Before <6pt: %d đoạn (%s); After <6pt: %d đoạn (%s) – trên %d đoạn lời văn' % (len(bad_bef), ids(bad_bef), len(bad_aft), ids(bad_aft), n),
               'xem số đoạn', 'Before ≥ 6 pt và After ≥ 6 pt', CC_HT + '; ' + CC_TB + ' mục 6', 'Mức 2')
    elif n:
        R_.ok('Khoảng cách đoạn', 'Before và After ≥ 6 pt ở %d/%d đoạn lời văn' % (n, n), CC_HT)
    if bad_line:
        R_.add('TT-22', 'Giãn dòng', 'Đoạn %s (%d/%d đoạn)' % (ids(bad_line), len(bad_line), n), ', '.join(sorted(set(v for _, v in bad_line)))[:80],
               ('Exactly 18–22 pt' if he == 'dang' else 'từ Single đến tối đa 1,5 lines, kiểu theo dòng (Single, 1,5 lines, Multiple 1,0–1,5); không dùng Exactly/At least'), (CC_HD + ' Phần II mục 6.2.2') if he == 'dang' else (CC_TB + ' mục 6 (đính chính ngày 27/10/2026)'), 'Mức 2')
    elif n:
        R_.ok('Giãn dòng', 'trong giới hạn ở %d/%d đoạn lời văn' % (n, n), (CC_TB + ' mục 6') if he != 'dang' else (CC_HD + ' Phần II mục 6.2.2'))
    if bad_ind:
        R_.add('TT-23', 'Thụt đầu dòng', 'Đoạn %s (%d/%d đoạn)' % (ids(bad_ind), len(bad_ind), n), ', '.join(sorted(set(twip_cm(v) if v is not None else 'không thụt' for _, v in bad_ind)))[:80],
               ('khoảng 10 mm' if he == 'dang' else '1 cm – 1,27 cm'), (CC_TB + ' mục 6') if he != 'dang' else (CC_HD + ' Phần II mục 6.2.2'), 'Mức 2')
    elif n:
        R_.ok('Thụt đầu dòng', 'đúng ở %d/%d đoạn lời văn' % (n, n), (CC_TB + ' mục 6') if he != 'dang' else (CC_HD + ' Phần II mục 6.2.2'))

    # ---------------- 5. Bố cục phần: văn bản kèm theo, phụ lục, số trang ----------------
    kinds = []
    for si in range(n_sec):
        k, P0 = sec_kind(paras, si, n_sec)
        kinds.append((k, P0))
    # văn bản kèm theo/phụ lục nằm chung phần với văn bản chính?
    ns_idx = next((P.idx for P in paras if re.match(r'^Nơi nhận\s*(?::|$)', P.text)), None)
    if ns_idx is not None and he != 'dang':  # quy tắc section 26/10/2026: chỉ văn bản chính quyền
        for P in paras:
            if P.idx <= ns_idx or P.in_table or P.sec != paras[ns_idx].sec: continue
            if re.match(r'^(QUY ĐỊNH|QUY CHẾ|ĐIỀU LỆ|NỘI QUY|HƯỚNG DẪN|QUY TRÌNH)$', P.text) or la_dong_pl(P):
                R_.add('TT-30', 'Tách phần (section) cho văn bản kèm theo/phụ lục', 'Đoạn %d “%s”' % (P.idx + 1, P.text),
                       'cùng phần (section) với văn bản chính', 'ngắt trang và trình bày theo section mới', CC_HT, 'Mức 2')
                break
    # đoạn trống liên tiếp dùng thay ngắt trang
    run_, best, at = 0, 0, None
    for P in paras:
        if P.in_table: continue
        empty = not P.text and P.el.find('.//' + q('drawing')) is None and P.el.find('.//' + q('pict')) is None and P.el.find('.//' + q('sectPr')) is None
        if empty:
            run_ += 1
            if run_ > best: best, at = run_, P.idx - run_ + 2
        else:
            run_ = 0
    if best >= 5:
        R_.add('TB-01', 'Đoạn trống liên tiếp', 'Bắt đầu từ đoạn %d' % at, '%d đoạn trống liên tiếp' % best, 'dùng ngắt trang/section, không dùng phím Enter', 'Kỹ thuật trình bày', 'Mức 3')

    # số trang theo phần
    n_pages_total, start_page = (render_section_pages(path, paras, n_sec) if do_render else (None, None))
    start_page = start_page or {}
    def hdr_for(si, kind):
        # header hiệu lực (kế thừa từ phần trước nếu không khai báo)
        for j in range(si, -1, -1):
            refs = hf_refs(sections[j])
            if ('headerReference', kind) in refs:
                return D.hf_xml(refs[('headerReference', kind)])
            if kind == 'first' and j == si:
                continue
        return None
    def ftr_any(si):
        for j in range(si, -1, -1):
            refs = hf_refs(sections[j])
            for (t, k), rid in refs.items():
                if t == 'footerReference' and has_page_field(D.hf_xml(rid)): return True
        return False
    for si, (k, P0) in enumerate(kinds):
        sp = sections[si]
        lab = 'Phần %d (%s)' % (si + 1, {'chinh': 'văn bản chính', 'kem_theo': 'văn bản kèm theo', 'phu_luc': 'phụ lục', 'khac': 'khác'}[k])
        titlePg = sp.find(q('titlePg')) is not None and onoff(sp.find(q('titlePg'))) is not False
        pnt = sp.find(q('pgNumType'))
        start = int(pnt.get(q('start'))) if pnt is not None and pnt.get(q('start')) else None
        fmt = pnt.get(q('fmt')) if pnt is not None else None
        if si == 0 and k != 'chinh' and start is None: start = 1  # tệp riêng: số trang mặc định bắt đầu từ 1
        h_def = hdr_for(si, 'default')
        h_first = None
        for j in range(si, -1, -1):
            rj = hf_refs(sections[j])
            if ('headerReference', 'first') in rj:
                h_first = D.hf_xml(rj[('headerReference', 'first')]); break
        has_num_default = has_page_field(h_def)
        shows_first = (not titlePg and has_num_default) or (titlePg and has_page_field(h_first))
        # số trang của phần (từ bản dựng)
        sec_pages = None
        if si in start_page:
            nxt = [start_page[j] for j in start_page if j > si]
            end = (min(nxt) - 1) if nxt else n_pages_total
            sec_pages = end - start_page[si] + 1 if end else None
        cc_st = (CC_HD + ' mục IV.5.1') if he == 'dang' else (CC_ND + ' mục I.7')  # PB2-19
        if ftr_any(si) and not has_num_default:
            R_.add('TT-31', 'Vị trí số trang', lab, 'số trang đặt ở chân trang (footer)', 'giữa lề trên (header)', cc_st, 'Mức 2')
        if k == 'chinh':
            if not has_num_default and (sec_pages or 2) > 1:
                R_.add('TT-32', 'Đánh số trang văn bản chính', lab, 'không có trường số trang ở header', 'đánh số từ 1, giữa lề trên, cỡ 14', cc_st + ('' if he == 'dang' else '; ' + CC_HT), 'Mức 2')
            elif has_num_default:
                if S['hide_first'] and not titlePg:
                    R_.add('TT-33', 'Trang thứ nhất hiển thị số trang', lab, 'không bật “Different first page”', 'không hiển thị số trang thứ nhất', cc_st, 'Mức 2')
                elif titlePg and has_page_field(h_first):
                    R_.add('TT-33', 'Trang thứ nhất hiển thị số trang', lab, 'header trang đầu có trường số trang', 'không hiển thị số trang thứ nhất', cc_st, 'Mức 2')
                else:
                    R_.ok('Số trang văn bản chính', 'header giữa trang; trang 1 không hiển thị (titlePg)', cc_st)
                if start not in (None, 1):
                    R_.add('TT-32', 'Số bắt đầu văn bản chính', lab, 'start=%d' % start, 'bắt đầu từ 1', cc_st, 'Mức 2')
        elif k == 'kem_theo' and si == 0:
            R_.na('Số trang %s' % lab, 'văn bản kèm theo nộp thành tệp riêng – không kiểm được việc đánh số liên tục với văn bản chính; người kiểm tra xem khi ghép tệp')
        elif k == 'kem_theo' and he != 'dang':
            # quy tắc KTC: đánh LIÊN TỤC với Quyết định, hiển thị ở trang đầu của văn bản kèm theo
            if start == 1:
                R_.add('TT-34', 'Đánh số trang văn bản kèm theo', lab, 'pgNumType start=1 (đánh lại từ 1)', 'đánh liên tục với số trang của văn bản chính (Continue from previous section)', CC_HT, 'Mức 2')
            elif start is not None:
                exp = start_page.get(si)
                if exp is None:
                    R_.add('TT-34', 'Đánh số trang văn bản kèm theo', lab, 'pgNumType start=%d (đặt cứng)' % start, 'Continue from previous section (đánh liên tục)', CC_HT, 'Mức 3')
                elif exp != start:
                    R_.add('TT-34', 'Đánh số trang văn bản kèm theo', lab, 'start=%d nhưng phần bắt đầu ở trang %d của bản dựng' % (start, exp), 'đánh liên tục (Continue from previous section)', CC_HT, 'Mức 2')
                else:
                    R_.add('TT-34', 'Đánh số trang văn bản kèm theo – cách thiết lập', lab, 'start=%d (đúng trang hiện tại nhưng đặt cứng)' % start, 'chọn Continue from previous section để không lệch khi sửa văn bản chính', CC_HT, 'Mức 3')
            else:
                R_.ok('Số trang văn bản kèm theo', 'đánh liên tục (không đặt lại số bắt đầu)', CC_HT)
            if not shows_first and has_num_default:
                R_.add('TT-35', 'Trang đầu văn bản kèm theo không hiện số', lab, 'titlePg bật, header trang đầu không có số trang', 'hiển thị số trang liên tục (ví dụ trang 4)', CC_HT, 'Mức 2')
            if not has_num_default:
                R_.add('TT-34', 'Đánh số trang văn bản kèm theo', lab, 'không có trường số trang', 'đánh liên tục với văn bản chính, giữa lề trên, cỡ 14', CC_HT, 'Mức 2')
        elif k == 'phu_luc':
            one_page = sec_pages == 1 and he != 'dang'
            if one_page:
                if has_num_default or shows_first:
                    R_.add('TT-36', 'Số trang phụ lục chỉ một trang', lab, 'phụ lục chỉ một trang vẫn có số trang', 'phụ lục chỉ một trang thì không đánh số trang', CC_HT, 'Mức 2')
                else:
                    R_.ok('Số trang phụ lục chỉ một trang', 'không đánh số (đúng)', CC_HT)
            else:
                if he == 'dang':
                    if start not in (1,):
                        R_.add('TT-36', 'Số trang phụ lục', lab, 'start=%s' % start, 'đánh riêng cho từng phụ lục (từ 1)', CC_HD + ' mục IV.5.2', 'Mức 2')
                else:
                    if start != 1:
                        R_.add('TT-36', 'Số trang phụ lục – bắt đầu', lab, 'start=%s' % ('không đặt (chạy tiếp)' if start is None else start), 'đánh riêng, bắt đầu từ 1', CC_HT + '; ' + CC_ND + ' mục III.1.đ', 'Mức 2')
                    if not shows_first:
                        R_.add('TT-37', 'Số trang phụ lục – trang đầu', lab, 'trang đầu phụ lục không hiển thị số', 'hiển thị số ở trang đầu tiên của phụ lục', CC_HT, 'Mức 2')
                    if sec_pages is None:
                        R_.na('Số trang của %s' % lab, 'không dựng được bản PDF để đếm trang (quy tắc “phụ lục chỉ có một trang”)')
                    if start == 1 and shows_first:
                        R_.ok('Số trang phụ lục (%s)' % lab, 'bắt đầu từ 1, hiển thị trang đầu', CC_HT)
        # cỡ chữ, canh lề số trang
        pf = page_field_props(D, h_def) if has_num_default else None
        if pf:
            bad = []
            if pf['jc'] not in ('center',): bad.append('canh %s' % (pf['jc'] or 'trái'))
            if pf['sz'] and pf['sz'] != S['num_sz']: bad.append('cỡ %s' % hp_pt(pf['sz']))
            if bad:
                R_.add('TT-38', 'Định dạng số trang', lab, ', '.join(bad), 'giữa, cỡ 14, đứng', (CC_HD + ' mục IV.5.1') if he == 'dang' else (CC_HT + '; ' + CC_ND + ' mục I.7'), 'Mức 2')
    # nhiều phụ lục trong một phần
    pl_heads = [P for P in paras if not P.in_table and la_dong_pl(P)]
    by_sec = {}
    for P in pl_heads: by_sec.setdefault(P.sec, []).append(P)
    for s_, lst in by_sec.items():
        if len(lst) > 1:
            R_.add('TT-39', 'Nhiều phụ lục chung một phần', 'Phần %d: %s' % (s_ + 1, ', '.join('“%s”' % P.text for P in lst)), 'không tách section', 'mỗi phụ lục một section để đánh số trang riêng từ 1', (CC_HD + ' mục IV.5.2') if he == 'dang' else (CC_HT + '; ' + CC_ND + ' mục III.1.đ'), 'Mức 2')

    # ---------------- 6. Trình bày phụ lục ----------------
    roman = re.compile(r'^[IVXLCDM]+$')
    for P in pl_heads:
        m_ = pl_match(P.text, 'center' if dau_phan.get(P.sec) == P.idx else P.props['jc'])
        so = m_.group(2)
        inline = m_.group(3)
        pos = 'Đoạn %d “%s”' % (P.idx + 1, P.text[:60])
        if not P.text.startswith('Phụ lục') and he != 'dang':
            R_.add('TT-40', 'Chữ “Phụ lục”', pos, P.text[:40], '“Phụ lục” in thường (chỉ viết hoa chữ P)', CC_HT, 'Mức 2')
        if inline and he != 'dang':
            R_.add('TT-42', 'Tiêu đề phụ lục', pos, 'tiêu đề viết liền dòng “%s %s”' % (m_.group(1), so or ''), 'dòng “Phụ lục I” riêng; tiêu đề in hoa ở dòng dưới, canh giữa', CC_HT + '; ' + CC_ND + ' mục III.1.b', 'Mức 2')
        if so:
            if he != 'dang' and not roman.match(so):
                R_.add('TT-40', 'Số thứ tự phụ lục', pos, so, 'chữ số La Mã (I, II, …)', CC_HT + '; ' + CC_ND + ' mục III.1.a', 'Mức 2')
            if he == 'dang' and not so.isdigit():
                R_.add('TT-40', 'Số thứ tự phụ lục', pos, so, 'chữ số Ả-rập', CC_HD + ' Phần II mục 1.1', 'Mức 2')
        elif len(pl_heads) > 1:
            R_.add('TT-40', 'Số thứ tự phụ lục', pos, 'không có số', 'có từ hai phụ lục trở lên phải đánh số', (CC_HD + ' Phần II mục 1.1') if he == 'dang' else (CC_ND + ' mục III.1.a'), 'Mức 2')
        cc_pl = (CC_HD + ' Phần II mục 1.2') if he == 'dang' else (CC_ND + ' mục III.1.b')
        expect(P, 'TT-41', 'Dòng “Phụ lục …”', 28, True, False, cc_pl)
        if P.props['jc'] != 'center':
            R_.add('TT-41', 'Canh lề dòng “Phụ lục …”', pos, 'canh %s' % (P.props['jc'] or 'trái'), 'canh giữa', cc_pl, 'Mức 2')
        # tiêu đề phụ lục: các đoạn liền sau, in hoa, canh giữa
        tit = []
        for P2 in paras[P.idx + 1:P.idx + 8]:
            if P2.in_table or not P2.text:
                if tit: break
                continue
            if P2.text.upper() == P2.text and not P2.text.startswith('('):
                tit.append(P2)
            else:
                break
        if he != 'dang':
            if not tit and inline:
                R_.add('TT-43', 'Dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM” cuối tiêu đề phụ lục', pos, 'không có dòng riêng', '“CỦA TRƯỜNG CAO ĐẲNG KON TUM” in hoa, đậm, cỡ 14, một dòng riêng ở cuối tiêu đề', CC_HT, 'Mức 2')
            elif not tit:
                R_.add('TT-42', 'Tiêu đề phụ lục', pos, 'không thấy tiêu đề in hoa dưới dòng “Phụ lục”', 'tiêu đề in hoa, đậm, canh giữa', CC_HT + '; ' + CC_ND + ' mục III.1.b', 'Mức 2')
            else:
                for P2 in tit:
                    if P2.props['jc'] != 'center' or not all_bold(P2):
                        R_.add('TT-42', 'Tiêu đề phụ lục', 'Đoạn %d “%s”' % (P2.idx + 1, P2.text[:50]), ('canh %s' % (P2.props['jc'] or 'trái')) + ('' if all_bold(P2) else ', chưa đậm'), 'in hoa, đậm, canh giữa', CC_HT, 'Mức 2')
                last = tit[-1]
                raw_lines = []
                for e in last.el.iter():
                    if e.tag == q('t'): raw_lines.append(e.text or '')
                    elif e.tag in (q('br'), q('cr')): raw_lines.append('\n')
                last_line = norm(''.join(raw_lines).split('\n')[-1])
                if last.text.strip() != 'CỦA TRƯỜNG CAO ĐẲNG KON TUM' and last_line == 'CỦA TRƯỜNG CAO ĐẲNG KON TUM':
                    R_.ok('Dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM” (%s)' % P.text, 'dòng riêng (ngắt dòng trong cùng đoạn), in hoa', CC_HT)
                elif last.text.strip() != 'CỦA TRƯỜNG CAO ĐẲNG KON TUM':
                    joined = ' '.join(t.text for t in tit)
                    hint = 'cụm từ nằm chung dòng với tiêu đề' if 'CỦA TRƯỜNG CAO ĐẲNG KON TUM' in joined else 'không có cụm từ'
                    R_.add('TT-43', 'Dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM” cuối tiêu đề phụ lục', pos, hint, '“CỦA TRƯỜNG CAO ĐẲNG KON TUM” in hoa, đậm, cỡ 14, một dòng riêng ở cuối tiêu đề', CC_HT, 'Mức 2')
                else:
                    if runs_sz(last) != 28 or not all_bold(last):
                        R_.add('TT-43', 'Dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM”', 'Đoạn %d' % (last.idx + 1), 'cỡ %s%s' % (hp_pt(runs_sz(last)), '' if all_bold(last) else ', chưa đậm'), 'in hoa, đậm, cỡ 14', CC_HT, 'Mức 2')
                    else:
                        R_.ok('Dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM” (%s)' % P.text, 'dòng riêng, in hoa, đậm, cỡ 14', CC_HT)
                # đường kẻ dưới tiêu đề
                zone = paras[last.idx:last.idx + 3]
                has_line = any(P3.el.find('.//' + q('drawing')) is not None or P3.el.find('.//' + q('pict')) is not None for P3 in zone)
                if not has_line:
                    R_.add('TT-44', 'Đường kẻ dưới tiêu đề phụ lục', pos, 'không thấy đối tượng vẽ (Draw) ngay dưới tiêu đề', 'đường kẻ (Draw) dài 1/3–1/2 tiêu đề', CC_HT, 'Mức 2')
                else:
                    R_.ok('Đường kẻ dưới tiêu đề phụ lục – có đối tượng vẽ (%s)' % P.text[:30], 'có đối tượng vẽ (Draw) ngay dưới tiêu đề', CC_HT)
                    R_.na('Độ dài đường kẻ dưới tiêu đề %s' % P.text[:30], 'script không đo độ dài 1/3–1/2 tiêu đề; người kiểm tra xem bản dựng')
        # dòng chỉ dẫn "Kèm theo ..."
        if he == 'dang':
            if not any(re.match(r'^\(?\s*(kèm|ban hành kèm) theo', P2.text, re.I) for P2 in paras[P.idx + 1:P.idx + 10]):
                R_.add('TT-46', 'Chỉ dẫn phụ lục (văn bản Đảng)', pos, 'không thấy dòng chỉ dẫn dưới tiêu đề phụ lục', 'dưới tiêu đề phụ lục ghi chỉ dẫn: số, ký hiệu, ngày ban hành và cơ quan ban hành văn bản', CC_HD + ' Phần II mục 1.2', 'Mức 2')
            continue
        for P2 in paras[P.idx + 1:P.idx + 10]:
            if re.match(r'^\(?\s*(Kèm|Ban hành kèm) theo', P2.text, re.I):
                R_.add('TT-45', 'Dòng chỉ dẫn “(Kèm theo …)” dưới tiêu đề', 'Đoạn %d “%s”' % (P2.idx + 1, P2.text[:60]), 'có dòng chỉ dẫn', 'không ghi dòng này (văn bản ký số); thay bằng dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM”', CC_HT, 'Mức 2')
                break
    # Dòng "Kèm theo" dưới tiêu đề văn bản kèm theo
    for k, P0 in kinds:
        if k == 'kem_theo' and P0 is not None and he != 'dang':
            for P2 in paras[P0.idx + 1:P0.idx + 8]:
                if re.match(r'^\(?\s*(Kèm|Ban hành kèm) theo', P2.text, re.I):
                    R_.add('TT-45', 'Dòng chỉ dẫn “(Ban hành kèm theo …)” dưới tiêu đề văn bản kèm theo', 'Đoạn %d' % (P2.idx + 1), P2.text[:70], 'không ghi dòng này (văn bản ký số)', CC_HT, 'Mức 2')
                    break
    # viện dẫn "phụ lục I" viết thường
    for P in (paras if he != 'dang' else []):
        for m_ in re.finditer(r'(?<![.:]\s)(?<!^)\bphụ lục\s+([IVXLCDM]+|\d+)\b', P.text):
            R_.add('TD-05', 'Viết hoa “Phụ lục” khi gắn số', 'Đoạn %d: “…%s…”' % (P.idx + 1, P.text[max(0, m_.start() - 25):m_.end() + 5]), m_.group(0), '“Phụ lục %s”' % m_.group(1), CC_HT, 'Mức 2')
            break

    # ---------------- 7. Bảng ----------------
    for tid, (tbl, sec_) in enumerate(tables if he != 'dang' else []):
        txt = norm(' '.join(p_text(p) for p in tbl.iter(q('p'))))
        TU = txt.upper()
        if re.search(r'CỘNG H(?:ÒA|OÀ) XÃ HỘI|ĐẢNG CỘNG SẢN|NƠI NHẬN', TU) or ('SỐ:' in TU and re.search(r'UBND|TRƯỜNG CAO ĐẲNG|ĐẢNG BỘ|ĐẢNG ỦY', TU)):
            continue  # bảng bố cục (đầu văn bản, chữ ký)
        if re.search(r'^(KT|TM|TL|Q)\.\s|HIỆU TRƯỞNG|\(CHỮ KÝ|BÍ THƯ', TU) and len(txt) < 400:
            continue  # bảng chữ ký mẫu
        tblPr = tbl.find(q('tblPr'))
        _sty = tblPr.find(q('tblStyle')) if tblPr is not None else None
        _bd = tblPr.find(q('tblBorders')) if tblPr is not None else None
        if (_bd is None and _sty is None) or (_bd is not None and all((c.get(q('val')) in ('nil', 'none')) for c in _bd)):
            continue  # bảng không kẻ khung = bảng bố cục
        jc = tblPr.find(q('jc')).get(q('val')) if tblPr is not None and tblPr.find(q('jc')) is not None else None
        borders = tblPr.find(q('tblBorders')) if tblPr is not None else None
        cells = list(tbl.iter(q('tc')))
        not_mid = 0
        for tc in cells:
            tcPr = tc.find(q('tcPr'))
            va = tcPr.find(q('vAlign')).get(q('val')) if tcPr is not None and tcPr.find(q('vAlign')) is not None else 'top'
            if va != 'center': not_mid += 1
        lab = 'Bảng %d (phần %d): “%s…”' % (tid + 1, sec_ + 1, txt[:40])
        if jc not in ('center',):
            R_.add('TT-50', 'Canh bảng giữa trang', lab, 'canh %s' % (jc or 'trái (mặc định)'), 'bảng canh giữa trang (Table – Center)', CC_HT, 'Mức 2')
        if not_mid:
            R_.add('TT-51', 'Canh ô giữa theo chiều dọc', lab, '%d/%d ô chưa canh giữa dòng' % (not_mid, len(cells)), 'các ô canh giữa theo chiều dọc dòng (Cell – Center)', CC_HT, 'Mức 2')
        if jc == 'center' and not not_mid:
            R_.ok('Bảng %d' % (tid + 1), 'canh giữa trang, ô canh giữa dòng', CC_HT)

    # ---------------- 8. Viết tên đơn vị, viết hoa, từ ngữ (theo TB 597, QĐ 1355) ----------------
    if he != 'dang':
        CANON = [
            (r'ban truyền thông', 'Ban Truyền thông'),
            (r'ban văn\s*[-–]\s*thể\s*[-–]\s*mỹ', 'Ban Văn – Thể – Mỹ'),
            (r'tổ quản trị hệ thống thông tin', 'Tổ Quản trị hệ thống thông tin'),
            (r'phòng khám đa khoa', 'Phòng khám Đa khoa'),
            (r'nhà thuốc phòng khám đa khoa', 'Nhà thuốc Phòng khám Đa khoa'),
            (r'hội sinh viên', 'Hội Sinh viên'),
            (r'đoàn thanh niên', 'Đoàn Thanh niên'),
        ]
        found_td = set()
        for P in paras:
            t = P.text
            for pat, good in CANON:
                for m_ in re.finditer(pat, t, re.I):
                    s_ = t[m_.start():m_.end()]
                    if s_ != good and not s_.isupper() and (good, s_) not in found_td:
                        found_td.add((good, s_))
                        R_.add('TD-01', 'Cách viết tên đơn vị', 'Đoạn %d: “…%s…”' % (P.idx + 1, t[max(0, m_.start() - 20):m_.end() + 10]), s_, good, CC_TB + ' mục 3.1.c; QĐ 1355/QĐ-CĐKT Điều 2', 'Mức 2')
            # "Phòng/Khoa/Bộ môn" viết hoa giữa câu
            if sum(1 for x in R_.loi if x['ma'] == 'TD-02') >= 12: pass
            else:
              for m_ in re.finditer(r'(?<=[a-zà-ỹ,;)]\s)(Phòng|Khoa|Bộ môn)\s+(Tổng hợp|Tổ chức cán bộ|Tài chính|Quản lý Đào tạo|Quản lý khoa học|Sư phạm|Y\s*[-–]\s*Dược|các Khoa học cơ bản|Kinh tế và Nông Lâm|Kỹ thuật và Công nghệ|Đào tạo và Sát hạch)', t):
                key = ('cap', m_.group(1))
                R_.add('TD-02', 'Viết hoa từ “%s” giữa câu' % m_.group(1), 'Đoạn %d: “…%s…”' % (P.idx + 1, t[max(0, m_.start() - 20):m_.end() + 25]), m_.group(1), '“%s” viết thường giữa câu (chỉ viết hoa khi đứng đầu dòng, sau dấu chấm, sau dấu hai chấm)' % m_.group(1).lower(), CC_TB + ' mục 3.1.c', 'Mức 2')
            for m_ in re.finditer(r'(?<=[a-zà-ỹ,]\s)Nhà trường\b', t):
                R_.add('TD-03', 'Viết hoa “Nhà trường” giữa câu', 'Đoạn %d' % (P.idx + 1), 'Nhà trường', 'nhà trường', 'Quy ước của Trường (Mẫu prompt chính thức mục 4)', 'Mức 3')
                break
            if re.search(r'\bđảm bảo\b', t, re.I):
                R_.add('TD-04', 'Từ “đảm bảo”', 'Đoạn %d' % (P.idx + 1), 'đảm bảo', 'bảo đảm', 'Mẫu prompt chính thức mục 4', 'Mức 3')
        # giới hạn số dòng TD-02 lặp
    # ---------------- 9. Căn cứ: văn bản bị thay thế, văn bản hợp nhất (nguồn: kho_manifest.json) ----------------
    KHO = load_kho()
    het = {x['so_hieu']: x for x in KHO.get('van_ban_het_hieu_luc_hay_gap', [])}
    da_bao = set()
    # PB2-09: quét cả chú thích cuối trang/cuối văn bản; nhận cả dạng viết tắt “Nghị định 13/2023”
    class _N: pass
    notes = []
    for nm in ('word/footnotes.xml', 'word/endnotes.xml'):
        if nm in D.z.namelist():
            for k_, p_ in enumerate(etree.fromstring(D.z.read(nm)).iter(q('p'))):
                t_ = norm(p_text(p_))
                if t_:
                    o = _N(); o.text = t_; o.idx = -1; o.nhan = 'Chú thích (%s)' % ('cuối trang' if 'foot' in nm else 'cuối văn bản'); notes.append(o)
    def mau_so(so):
        m_ = re.match(r'^(\d+)/(\d{4})/(.+)$', so)
        # v4.3 (TH-08): ranh giới ký hiệu đầy đủ (không khớp tiền tố “13/2023/NĐ-CPX”); dạng rút gọn nhận cả ở cuối đoạn
        if not m_: return re.escape(so) + r'(?![\w/\-])'
        loai = {'NĐ': r'(?:Nghị định|NĐ)', 'QĐ': r'(?:Quyết định|QĐ)', 'TT': r'(?:Thông tư|TT)'}.get(re.split(r'[-/]', m_.group(3))[0], None)
        if loai:
            return r'(?:' + re.escape(so) + r'(?![\w/\-])|(?<![\d/])' + m_.group(1) + '/' + m_.group(2) + r'(?![\d/\w]))'
        return re.escape(so) + r'(?![\w/\-])'
    for P in list(paras) + notes:  # PB-18: quét mọi đoạn, không chỉ đoạn “Căn cứ”
        for so, x in het.items():
            pat = mau_so(so)
            for m_ in re.finditer(r'(?<![\d/])' + pat, P.text):
                if not m_.group(0).endswith(so) and not re.search(r'(Nghị định|NĐ|Quyết định|QĐ|Thông tư|TT)\s+(số\s+)?$', P.text[max(0, m_.start() - 20):m_.start()]):
                    continue  # dạng rút gọn “13/2023” chỉ nhận khi đứng sau tên loại văn bản
                if la_cau_thay_the(P.text, m_.start(), m_.end()):
                    continue  # v4.3 (TH-08): CHÍNH lần nhắc này nằm trong cụm nêu việc thay thế/bãi bỏ – không phải viện dẫn sai
                if (so, P.idx, P.text[:30]) in da_bao: continue
                da_bao.add((so, P.idx, P.text[:30]))
                vt_ = getattr(P, 'nhan', None) or 'Đoạn %d' % (P.idx + 1)
                R_.add('CC-01', 'Viện dẫn văn bản đã bị thay thế', '%s: “…%s…”' % (vt_, P.text[max(0, m_.start() - 40):m_.end() + 30]), so,
                       'thay bằng ' + x.get('thay_bang', ''), 'kho_manifest.json (van_ban_het_hieu_luc_hay_gap)', 'Mức 1')
                R_.loi[-1]['doan_goc'] = P.text  # v4.4 (PB4-GPT-02, quyết định E2): nguyên văn đoạn để kiểm “bo_qua_the_thuc” Mức 1
    vbhn = KHO.get('van_ban_hop_nhat_da_biet', [])
    def ngay_key(t):
        m_ = re.search(r'(\d{1,2})\s*(?:tháng|/)\s*(\d{1,2})\s*(?:năm|/)\s*(\d{4})', t or '')
        return (int(m_.group(3)), int(m_.group(2)), int(m_.group(1))) if m_ else None
    for P in [P for P in paras if P.text.startswith('Căn cứ')]:
        t = P.text
        # CC-06: căn cứ là Luật, Pháp lệnh ghi số, ký hiệu (quyết định của Hiệu trưởng 26/10/2026 – văn bản hành chính theo NĐ 30)
        if he != 'dang':
            for m_ in re.finditer(r'\b(Luật|Bộ luật|Pháp lệnh)\s+(?:(?!ngày|bởi)[^;()]){2,90}?\s+số\s*:?\s*(\d+/\d{4}/[A-ZĐ0-9]+)', t):
                R_.add('CC-06', 'Căn cứ là Luật/Pháp lệnh ghi số, ký hiệu', 'Đoạn %d: “…%s…”' % (P.idx + 1, t[m_.start():m_.end() + 5][:90]), 'ghi “số %s”' % m_.group(2),
                       'Luật, Pháp lệnh chỉ ghi tên loại, tên và ngày thông qua; không ghi số, ký hiệu, cơ quan ban hành', 'NĐ 30/2020/NĐ-CP Phụ lục I Phần II mục 6.a; TB 597/TB-CĐKT mục 6', 'Mức 2')
        liet_ke = re.search(r'luật sửa đổi, bổ sung một số điều của (?:các )?luật|được sửa đổi, bổ sung (?:bởi|theo|tại)|các luật sửa đổi(?:, bổ sung)?', t, re.I)
        da_bao_cc02 = False
        for v in vbhn:
            law = v['luat']
            m_law = re.search(r'\b' + re.escape(law) + r'(?=\s+(?:số\s|ngày|năm\s+\d{4}|và các luật|\())', t)
            if not m_law: continue
            hn = re.search(r'hợp nhất tại Văn bản hợp nhất số\s*(\d+/VBHN-[A-ZĐ]+)([^)]*)', t, re.I)
            if hn:
                if hn.group(1).upper() != v['vbhn'].upper():
                    d1, d2 = ngay_key(hn.group(2)), ngay_key(v['ngay_vbhn'])
                    if d1 and d2 and d1 < d2:
                        R_.add('CC-02', 'Viện dẫn văn bản hợp nhất chưa phải bản mới nhất', 'Đoạn %d: “%s…”' % (P.idx + 1, t[:90]), 'VBHN %s' % hn.group(1),
                               'VBHN mới nhất đã biết: %s ngày %s' % (v['vbhn'], v['ngay_vbhn']), 'Pháp lệnh 01/2026/UBTVQH16 (Điều 4 sửa đổi); ' + CC_HT, 'Mức 2')
                        da_bao_cc02 = True
                    else:
                        R_.na('VBHN của %s (đoạn %d)' % (law, P.idx + 1), 'dự thảo dẫn %s – khác VBHN đã biết %s; người rà soát kiểm bản VBHN trong hồ sơ' % (hn.group(1), v['vbhn']))
                else:
                    R_.ok('Viện dẫn VBHN %s' % law, 'đúng VBHN mới nhất đã biết: %s' % v['vbhn'], 'kho_manifest.json')
            else:
                R_.add('CC-02', 'Luật đã có VBHN nhưng chưa viện dẫn theo VBHN', 'Đoạn %d: “%s…”' % (P.idx + 1, t[:90]), 'liệt kê luật sửa đổi' if liet_ke else 'không có “(hợp nhất tại Văn bản hợp nhất số …)”',
                       '“Căn cứ %s ngày %s (hợp nhất tại Văn bản hợp nhất số %s ngày %s);”' % (law, v['ngay_luat_goc'], v['vbhn'], v['ngay_vbhn']),
                       'Pháp lệnh 01/2026/UBTVQH16 (Điều 4 sửa đổi); ' + CC_HT, 'Mức 2')
                da_bao_cc02 = True
        if liet_ke and not da_bao_cc02 and 'hợp nhất tại' not in t.lower():
            # PB-07: chưa biết luật đã có VBHN hay chưa → không kết luận lỗi
            R_.na('VBHN – đoạn %d' % (P.idx + 1), 'căn cứ liệt kê luật sửa đổi (“%s…”); chưa xác định được VBHN mới nhất trong Kho/hồ sơ – không kết luận lỗi, ghi Phần I.8' % t[:60])

    # ---------------- 10. Thuộc tính tệp ----------------
    try:
        core = etree.fromstring(D.z.read('docProps/core.xml'))
        title = core.find('{http://purl.org/dc/elements/1.1/}title')
        if title is not None and title.text and re.search(r'KON TUM', title.text.upper()) and 'UBND TỈNH KON TUM' in title.text.upper():
            R_.add('TB-02', 'Thuộc tính tệp (Title)', 'docProps/core.xml', title.text, 'tên dự thảo hoặc để trống (không ghi tên cơ quan cũ)', 'Kỹ thuật – metadata', 'Mức 4')
    except Exception:
        pass

    return he, S, R_, dict(n_sections=n_sec, kinds=[k for k, _ in kinds], pages=n_pages_total, start_page=start_page)

# ----------------------------------------------------------------------------
def to_md(path, he, S, R_, info):
    out = []
    out.append('# Kết quả đo thể thức: %s' % os.path.basename(path))
    out.append('')
    out.append('- Hệ văn bản: **%s**' % S['ten'])
    out.append('- Số phần (section): %d → %s' % (info['n_sections'], ', '.join(info['kinds'])))
    out.append('- Bản dựng PDF (LibreOffice): %s' % ('%d trang; trang bắt đầu các phần: %s' % (info['pages'], ', '.join('phần %d→tr.%d' % (k + 1, v) for k, v in sorted(info['start_page'].items()))) if info['pages'] else 'không dựng được – các mục cần số trang ghi “Chưa kiểm”'))
    out.append('- Số trang lấy từ bản dựng LibreOffice, có thể lệch khi mở bằng Word.')
    out.append('')
    out.append('## A. Phát hiện (%d)' % len(R_.loi))
    out.append('')
    out.append('| Mã | Hạng mục | Vị trí | Đo được | Yêu cầu | Căn cứ | Mức đề xuất |')
    out.append('|---|---|---|---|---|---|---|')
    for x in R_.loi:
        out.append('| %s | %s | %s | %s | %s | %s | %s |' % tuple(str(x[k]).replace('|', '/') for k in ('ma', 'hang_muc', 'vi_tri', 'do', 'yeu_cau', 'can_cu', 'muc')))
    out.append('')
    out.append('## B. Các mục đạt (đưa vào Phần III kèm số đo)')
    out.append('')
    out.append('| Hạng mục | Số đo | Căn cứ |')
    out.append('|---|---|---|')
    for x in R_.dat:
        out.append('| %s | %s | %s |' % (x['hang_muc'], x['do'], x['can_cu']))
    if R_.chua:
        out.append('')
        out.append('## C. Chưa kiểm được (đưa vào Phần I.8)')
        out.append('')
        for x in R_.chua:
            out.append('- %s: %s' % (x['hang_muc'], x['ly_do']))
    out.append('')
    out.append('Ghi chú: Mức đề xuất theo 02-Quy-Tac-Xep-Muc.md. AI vẫn phải mở vị trí trong tệp để xác nhận trước khi đưa vào Phần II; không tự hạ mức.')
    return '\n'.join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx')
    ap.add_argument('--he', default='auto', choices=['auto', 'chinh_quyen', 'dang'])
    ap.add_argument('--json')
    ap.add_argument('--khong-dung-ban', action='store_true')
    a = ap.parse_args()
    if not a.docx.lower().endswith('.docx'):
        print('LỖI: chỉ đo được tệp .docx. Tệp .doc/.pdf/ảnh phải được chuyển thành .docx trước (xem Cổng hồ sơ).'); sys.exit(2)
    he, S, R_, info = check(a.docx, a.he, not a.khong_dung_ban)
    print(to_md(a.docx, he, S, R_, info))
    if a.json:
        import hashlib  # v4.3 (TH-11): tên và mã băm tệp đo để tao_bao_cao.py kiểm cùng hồ sơ với cổng
        sha = hashlib.sha256(open(a.docx, 'rb').read()).hexdigest()
        json.dump(dict(he=he, tep=os.path.basename(a.docx), sha256=sha, phien_ban='ktc-ra-soat-897 v4.5', loi=R_.loi, dat=R_.dat, chua_kiem=R_.chua, info={k: v for k, v in info.items()}), open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)

if __name__ == '__main__':
    main()
