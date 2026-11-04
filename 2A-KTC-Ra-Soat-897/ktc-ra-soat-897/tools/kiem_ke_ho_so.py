#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kiem_ke_ho_so.py – CỔNG HỒ SƠ (bước 0) của Skill ktc-ra-soat-897 v4.6

Kiểm kê hồ sơ trước khi rà soát. Kết quả chỉ có HAI giá trị:
  * ĐỦ ĐIỀU KIỆN RÀ SOÁT  (mã thoát 0)
  * CHẶN – CHƯA ĐỦ HỒ SƠ  (mã thoát 2)  -> dừng hẳn, không rà soát tạm.

Quy tắc (chỉ đạo của Hiệu trưởng ngày 26/10/2026):
  1. Chỉ nhận .docx, .xlsx; .pdf chỉ nhận khi có lớp chữ (text layer).
     Có dù chỉ 1 tệp ảnh/bản chụp/PDF scan/.doc/.xls/.rtf/.odt -> CHẶN.
  2. Thiếu dự thảo, thiếu phụ lục/văn bản kèm theo mà dự thảo nhắc tới -> CHẶN.
  3. Thiếu toàn văn bất kỳ văn bản nào được đề cập trong dự thảo (kể cả mọi
     luật, nghị định ở phần căn cứ) mà Kho dữ liệu của Skill không có -> CHẶN.
  4. Từ lần rà soát thứ 2: phải có Báo cáo tiếp thu, giải trình (tệp riêng,
     lập sau báo cáo rà soát lần trước) + dự thảo đã sửa -> thiếu là CHẶN.

Cách dùng:
  python3 kiem_ke_ho_so.py <thư mục hoặc tệp ...> [--vong auto|1|2|3...]
          [--du-thao <tệp>] [--kho <đường dẫn kho_manifest.json>] [--json out.json]
"""
import sys, os, re, json, zipfile, subprocess, argparse, unicodedata, hashlib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # v4.6.4: không ghi __pycache__ vào thư mục Skill
import nhan_dien_chung as ND  # v4.6: nhận diện số hiệu, tiêu đề, Unicode dùng chung (KTS-01, KTS-26)
PHIEN_BAN = 'ktc-ra-soat-897 v4.6.4'
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
HERE = os.path.dirname(os.path.abspath(__file__))
KHO_DEFAULT = os.path.join(HERE, '..', 'references', 'Kho-Du-Lieu-897', 'kho_manifest.json')

NHAN = {'.docx', '.xlsx'}
ANH = {'.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp', '.gif', '.webp', '.heic', '.heif'}
CU = {'.doc': '.docx', '.xls': '.xlsx', '.rtf': '.docx', '.odt': '.docx', '.ods': '.xlsx', '.pages': '.docx'}
BO_QUA = {'.ds_store', '.ini', '.tmp', '.lnk', '.skill', '.md', '.json', '.py'}
NEN = {'.zip', '.rar', '.7z', '.tar', '.gz'}
WP = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
A4_EMU2 = 7560000 * 10692000  # diện tích trang A4 (EMU²)


def nfc(s): return unicodedata.normalize('NFC', s or '')
def norm(s): return re.sub(r'\s+', ' ', nfc(s).replace('\xa0', ' ')).strip()


# ---------------------------------------------------------------- đọc tệp
def _ptext(p):
    return norm(''.join((x.text or '') if x.tag == W + 't' else (' ' if x.tag in (W + 'tab', W + 'br') else '')
                        for x in p.iter() if x.tag in (W + 't', W + 'tab', W + 'br')))


def docx_paras(path):
    """Đoạn văn của thân văn bản, rồi đến chú thích cuối trang/cuối văn bản (đánh dấu “[Chú thích]”) – PB-05."""
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('word/document.xml'))
        out = [_ptext(p) for p in root.iter(W + 'p')]
        for nm in ('word/footnotes.xml', 'word/endnotes.xml'):
            if nm in z.namelist():
                r2 = ET.fromstring(z.read(nm))
                for p in r2.iter(W + 'p'):
                    t = _ptext(p)
                    if t: out.append('[Chú thích] ' + t)
    return out


def docx_jc(path):
    """Canh lề HIỆU LỰC của từng đoạn thân văn bản, cùng thứ tự với docx_paras (v4.5 – PB5-WORK-10).
    v4.6 (KTS-08): định dạng trực tiếp → kiểu đoạn (pStyle, chuỗi basedOn) → kiểu mặc định → docDefaults."""
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('word/document.xml'))
        sty = ET.fromstring(z.read('word/styles.xml')) if 'word/styles.xml' in z.namelist() else None
    jc_sty, based, mac_dinh, jc_doc = {}, {}, None, None
    if sty is not None:
        d_ = sty.find(W + 'docDefaults/' + W + 'pPrDefault/' + W + 'pPr/' + W + 'jc')
        if d_ is not None: jc_doc = d_.get(W + 'val')
        for st in sty.findall(W + 'style'):
            if st.get(W + 'type') != 'paragraph': continue
            sid = st.get(W + 'styleId')
            j_ = st.find(W + 'pPr/' + W + 'jc'); b_ = st.find(W + 'basedOn')
            if j_ is not None: jc_sty[sid] = j_.get(W + 'val')
            if b_ is not None: based[sid] = b_.get(W + 'val')
            if st.get(W + 'default') in ('1', 'true'): mac_dinh = sid
    def jc_cua(sid):
        seen = set()
        while sid and sid not in seen:
            seen.add(sid)
            if sid in jc_sty: return jc_sty[sid]
            sid = based.get(sid)
        return None
    out = []
    for p in root.iter(W + 'p'):
        jc = p.find(W + 'pPr/' + W + 'jc')
        if jc is not None: out.append(jc.get(W + 'val')); continue
        ps = p.find(W + 'pPr/' + W + 'pStyle')
        sid = ps.get(W + 'val') if ps is not None else mac_dinh
        out.append(jc_cua(sid) or jc_doc)
    return out


def docx_co_anh(path):
    with zipfile.ZipFile(path) as z:
        x = z.read('word/document.xml')
    return b'<w:drawing' in x or b'<w:pict' in x or b'<w:object' in x


def docx_anh_lon(path, xuat=None):
    """Ảnh trong thân văn bản có diện tích ≥ 25% trang A4 (DrawingML và VML) – PB-06, PB2-07.
    Trả về danh sách (cx, cy, đường dẫn ảnh đã xuất hoặc None)."""
    R_ = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
    out = []
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('word/document.xml'))
        rels = {}
        if 'word/_rels/document.xml.rels' in z.namelist():
            for r in ET.fromstring(z.read('word/_rels/document.xml.rels')):
                rels[r.get('Id')] = r.get('Target')
        def luu(rid, k):
            if not xuat or rid not in rels: return None
            tgt = 'word/' + rels[rid].lstrip('/').replace('word/', '') if not rels[rid].startswith('word/') else rels[rid]
            if tgt not in z.namelist(): return None
            os.makedirs(xuat, exist_ok=True)
            dst = os.path.join(xuat, '%s__anh%d%s' % (os.path.splitext(os.path.basename(path))[0], k, os.path.splitext(tgt)[1]))
            open(dst, 'wb').write(z.read(tgt)); return dst
        k = 0
        for d in root.iter(W + 'drawing'):
            pic = d.find('.//{http://schemas.openxmlformats.org/drawingml/2006/picture}pic')
            e = d.find('.//' + WP + 'extent')
            if pic is None or e is None: continue
            cx, cy = int(e.get('cx', 0)), int(e.get('cy', 0))
            if cx * cy >= 0.25 * A4_EMU2:
                k += 1
                bl = pic.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
                rid = bl.get(R_ + 'embed') if bl is not None else None
                out.append((cx, cy, luu(rid, k)))
        for sh in root.iter('{urn:schemas-microsoft-com:vml}shape'):
            im = sh.find('{urn:schemas-microsoft-com:vml}imagedata')
            if im is None: continue
            st = sh.get('style') or ''
            def pt(key):
                m = re.search(key + r':\s*([\d.]+)(pt|in|cm|mm|px)?', st)
                if not m: return 0
                v = float(m.group(1)); u = m.group(2) or 'pt'
                return v * {'pt': 12700, 'in': 914400, 'cm': 360000, 'mm': 36000, 'px': 9525}[u]
            cx, cy = pt('width'), pt('height')
            if cx * cy >= 0.25 * A4_EMU2:
                k += 1
                out.append((int(cx), int(cy), luu(im.get(R_ + 'id'), k)))
    return out


def xlsx_text(path):
    """v4.6.3: chữ của .xlsx theo TỪNG HÀNG (mỗi hàng một đoạn, các ô cách nhau “ | ”), giải đúng ô chuỗi dùng chung (t="s"), chuỗi
    trong ô (inlineStr), ô số. v4.6.2 nối mọi chữ – kể cả chỉ số chuỗi dùng chung – thành MỘT đoạn: dòng “Số: …” không nhận được số hiệu,
    và cả bảng bị coi là phần định danh khi ô đầu là “Số:”."""
    NS_ = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    with zipfile.ZipFile(path) as z:
        ten = z.namelist()
        ss = []
        if 'xl/sharedStrings.xml' in ten:
            for si in ET.fromstring(z.read('xl/sharedStrings.xml')).iter(NS_ + 'si'):
                ss.append(''.join(t.text or '' for t in si.iter(NS_ + 't')))
        out = []
        for n in sorted(x for x in ten if re.match(r'^xl/worksheets/sheet\d*\.xml$', x)):
            for row in ET.fromstring(z.read(n)).iter(NS_ + 'row'):
                o_ = []
                for c in row.iter(NS_ + 'c'):
                    v = c.find(NS_ + 'v'); kieu = c.get('t')
                    if kieu == 's' and v is not None and (v.text or '').strip().isdigit() and int(v.text) < len(ss): o_.append(ss[int(v.text)])
                    elif kieu == 'inlineStr': o_.append(''.join(t.text or '' for t in c.iter(NS_ + 't')))
                    elif v is not None and v.text: o_.append(v.text)
                o_ = [norm(x) for x in o_ if norm(x)]
                if o_: out.append(' | '.join(o_))
    return out or ['']


def pdf_info(path):
    """v4.6 (KTS-23): thiếu pdftotext/pdfinfo là LỖI MÔI TRƯỜNG, không phải tệp scan → trả ('THIEU_CONG_CU', 0)."""
    if shutil.which('pdftotext') is None:
        return 'THIEU_CONG_CU', 0
    try:
        t = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True, timeout=120).stdout
        n = subprocess.run(['pdfinfo', path], capture_output=True, text=True, timeout=60).stdout
        pages = int(re.search(r'Pages:\s+(\d+)', n).group(1)) if re.search(r'Pages:\s+(\d+)', n) else 1
    except Exception:
        return None, 1
    return t, pages


# ---------------------------------------------------------------- số hiệu
LOAI = r'(?:Nghị định|Thông tư liên tịch|Thông tư|Quyết định|Thông báo|Kế hoạch|Hướng dẫn|Quy định|Chỉ thị|Nghị quyết|Công văn|Pháp lệnh|Văn bản hợp nhất|Kết luận|Quy chế|Luật|Bộ luật|Tờ trình|Báo cáo)'
SO = r'(\d{1,5}(?:[/-][0-9A-Za-zĐđ]+)+(?:[/-][0-9A-Za-zĐđ]+)*)'


def key_so(s):
    s = nfc(s).upper().replace('Đ', 'D').replace('–', '-').strip(' .;,:)(')
    s = re.sub(r'\s+', '', s)
    return s


def loai_theo_ky_hieu(so, mac_dinh='Văn bản'):
    u = nfc(so).upper()
    for pat, ten in ((r'NĐ-CP', 'Nghị định'), (r'/QH\d', 'Luật'), (r'VBHN', 'Văn bản hợp nhất'), (r'/UBTVQH', 'Pháp lệnh/Nghị quyết'),
                     (r'/TT-', 'Thông tư'), (r'TTLT', 'Thông tư liên tịch'), (r'/TB-', 'Thông báo'), (r'/KH-', 'Kế hoạch'), (r'/TTR-', 'Tờ trình'),
                     (r'/BC-', 'Báo cáo'), (r'/CT-', 'Chỉ thị'), (r'^\d+-HD/', 'Hướng dẫn'), (r'/HD-', 'Hướng dẫn'), (r'^\d+-QĐ/TW', 'Quy định/Quyết định (Đảng)'),
                     (r'/QĐ-', 'Quyết định'), (r'^\d+-NQ/', 'Nghị quyết'), (r'/NQ-', 'Nghị quyết'), (r'/CĐKT-', 'Công văn')):
        if re.search(pat, u): return ten
    return mac_dinh


PL_TITLE = re.compile(r'(?i)^phụ lục\s+(?:số\s+)?([IVXLC]+|\d+)\s*(?:[.:–\-]\s*\S.*)?$')
# v4.6 (KTS-26): bỏ KEM_TITLE dùng dải [^a-zà-ỹđ] (dải này chứa cả chữ HOA có dấu) – thay bằng ND.loai_tieu_de_kem (thuộc tính Unicode),
# dùng chung cho văn bản kèm theo nằm trong dự thảo và tệp riêng.
KEM_LOAI = r'(Quy định|Quy chế|Điều lệ|Nội quy|Kế hoạch|Danh mục|Chương trình|Đề án|Hướng dẫn|Quy trình)'
LUON_KEM = ('QUY ĐỊNH', 'QUY CHẾ', 'ĐIỀU LỆ', 'NỘI QUY', 'DANH MỤC', 'QUY TRÌNH')  # các tên loại chỉ ban hành kèm theo văn bản khác
STOP_TY = set('của và các về việc trong tại theo đối với cho trường cao đẳng kon tum này năm được là thuộc ban hành'.split())


def loai_kem(title):
    return ND.loai_tieu_de_kem(title)


def tu_trich(s_):
    # v4.6 (KTS-05): số (năm, kỳ) là dữ kiện phân biệt – giữ lại; chỉ bỏ từ dừng
    return {w for w in re.findall(r'\w+', ND.chuan_trinh_bay(s_).lower()) if w not in STOP_TY}


TU_PHU_DINH = {'không', 'chưa', 'chẳng', 'cấm', 'thiếu'}


def diem_trich(a_, b_):
    """v4.5 (PB5-GPT-01/02, PB5-WORK-02): mức khớp trích yếu dự thảo (a_) – tệp kèm theo (b_); 0 = không khớp.
    Dự thảo không nêu trích yếu → khớp theo tên loại; tệp kèm không có trích yếu → KHÔNG khớp (phải xác nhận thủ công);
    từ phủ định chỉ có ở một bên → không khớp; từ có nghĩa của bên này phải nằm trọn trong bên kia (một bên có thể nêu rộng hơn)."""
    A, B = tu_trich(a_), tu_trich(b_)
    if not A: return 0.5
    if not B: return 0
    if (A & TU_PHU_DINH) != (B & TU_PHU_DINH): return 0
    nho, lon = (A, B) if len(A) <= len(B) else (B, A)
    if not nho <= lon or len(nho) < 0.5 * len(lon): return 0
    return len(A & B) / len(A | B)


def khop_trich(a_, b_):
    return diem_trich(a_, b_) > 0


KEM_LOAI_HOA = r'(Quy định|Quy chế|Điều lệ|Nội quy|Kế hoạch|Danh mục|Chương trình|Đề án|Hướng dẫn|Quy trình)'


def _tach_liet_ke(loai, ty):
    """v4.5 (PB5-WORK-03): “Quy định A và Quy chế B, Kế hoạch C” → [(QUY ĐỊNH, A), (QUY CHẾ, B), (KẾ HOẠCH, C)]."""
    parts = re.split(r'\s*(?:,|;|\svà|\scùng)\s+(?=(?:' + KEM_LOAI_HOA[1:-1] + r')\b)', ty)
    out = [(loai, parts[0])]
    for q_ in parts[1:]:
        m = re.match(KEM_LOAI_HOA + r'\b\s*(.*)$', q_)
        if m: out.append((nfc(m.group(1)).upper(), m.group(2)))
    return out


def kem_can(P):
    """Các văn bản kèm theo mà dự thảo ban hành: [(LOẠI, trích yếu)] – “ban hành kèm theo Quyết định này Quy định …”, “Quy định … ban hành kèm theo Quyết định này”;
    tách từng văn bản khi một câu liệt kê nhiều văn bản (v4.5)."""
    out = []
    for p in P:
        for m in re.finditer(r'(?i)ban hành kèm theo (?:Quyết định|Thông báo|Tờ trình|Nghị quyết) này\s+(?:là\s+)?' + KEM_LOAI + r'\b([^.;:]{0,240})', p):
            ty = re.split(r'\(|,?\s+(?:nội dung|chi tiết|tại Phụ lục|kèm theo|như sau)\b', m.group(2))[0]
            out += _tach_liet_ke(nfc(m.group(1)).upper(), ty)
        for m in re.finditer(r'(?i)' + KEM_LOAI + r'\s+([^.;]{0,240}?)\s*(?:được\s+)?ban hành kèm theo (?:Quyết định|Thông báo|Tờ trình|Nghị quyết) này', p):
            out += _tach_liet_ke(nfc(m.group(1)).upper(), m.group(2))
    seen_, res = set(), []
    for x in out:
        k_ = (x[0], ' '.join(sorted(tu_trich(x[1]))))
        if k_ not in seen_: seen_.add(k_); res.append(x)
    return res


def kem_trong(P):
    """Các văn bản kèm theo đặt trong chính tệp (sau “Nơi nhận”): [(LOẠI, trích yếu)]."""
    ki = next((i for i, p in enumerate(P) if re.match(r'^Nơi nhận\s*(?::|$)', p)), None)
    if ki is None: return []
    out = []
    for i in range(ki, len(P)):
        lk = loai_kem(P[i])
        if lk: out.append((lk, (ND.chuan_trinh_bay(P[i])[len(lk):] + ' ' + trich_sau(P, i)).strip()))
    return out


def trich_sau(P, i):
    t = []
    for p in P[i + 1:i + 4]:
        if not p or p.startswith('(') or re.match(r'^(Chương|Điều|Phần|Mục|[IVX]+\.|\d+\.)', p) or len(p) > 200: break
        t.append(p)
    return ' '.join(t)


def tieu_de_kem(paras):
    """v4.3 (TH-02): tệp là phụ lục / văn bản kèm theo nộp riêng – tiêu đề ở đầu tệp, không có quốc hiệu, số văn bản.
    Trả về ('phu_luc', 'I') | ('kem_theo', 'QUY ĐỊNH') | None."""
    dau = [p for p in paras[:10] if p and not p.startswith('[Chú thích]')]
    # phụ lục/văn bản kèm theo của văn bản ĐÃ BAN HÀNH (dòng “(Kèm theo … số 30/2020/NĐ-CP …)” có số) → văn bản liên quan, không phải tệp kèm của dự thảo
    # v4.4 (PB4-WORK-02): nhận cả dạng không có chữ “số” (“Kèm theo Quyết định 123/QĐ-CĐKT”) và dạng có ngày đã điền
    LOAI2 = r'(?:' + LOAI[3:-1] + r'|QĐ|NĐ|TT|TB|KH|NQ|HD|CT|TTr)'  # v4.5 (PB5-WORK-02): cả dạng viết tắt “QĐ 1355/QĐ-CĐKT”
    if any(re.search(r'(?i)kèm theo\s+' + LOAI2 + r'\s+(?:số\s*)?\d', p) or re.search(r'(?i)kèm theo\s+' + LOAI2 + r'[^)]{0,80}?ngày\s+\d{1,2}\s*(?:tháng|/)\s*\d{1,2}', p) for p in dau): return None
    for p in dau[:5]:
        m = PL_TITLE.match(p)
        if m and len(p) < 120: return ('phu_luc', m.group(1).upper())
    if any(re.match(r'^(CỘNG HÒA|ĐẢNG CỘNG SẢN|Số\b)', p) for p in dau[:8]): return None
    for i, p in enumerate(dau[:4]):
        lk_ = loai_kem(p)
        if lk_: return ('kem_theo', p, (ND.chuan_trinh_bay(p)[len(lk_):] + ' ' + trich_sau(dau, i)).strip())
    return None


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


HAU_TO = {'Nghị định': ('/ND-CP',), 'Thông tư': ('/TT-', 'TTLT'), 'Quyết định': ('/QD-', '-QD/'), 'Thông báo': ('/TB-', '-TB/')}


def cung_loai(k, loai):
    """Khóa số hiệu đầy đủ k (đã chuẩn hóa) có cùng loại văn bản với tên loại “loai” không (v4.4 – PB4-WORK-01)."""
    return any(h in k for h in HAU_TO.get(loai, ()))


TU_NOI = set('trong có tại theo về kể đã được của này thì khi để do với cho từ đến nhưng hoặc mà như các những sau trước hiện mới quy định'.split())


def _mo_rong_rac(k, x):
    """v4.6: tên k = tên x + phần lời văn (“LUẬT TRÍ TUỆ NHÂN TẠO TRONG THỜI HẠN…” = “LUẬT TRÍ TUỆ NHÂN TẠO” + “trong thời hạn…”).
    Tên luật khác thật sự (“LUẬT GIÁO DỤC NGHỀ NGHIỆP” so với “LUẬT GIÁO DỤC”) KHÔNG bị coi là mở rộng rác."""
    if not k.startswith(x + ' ') or k == x: return False
    return any(w.lower() in TU_NOI for w in k[len(x) + 1:].split())


def trich_dan(paras):
    """Trả về danh sách văn bản được đề cập: {'loai','so','ten','doan','ngu_canh','can_cu'}"""
    out, seen = [], set()
    idx = {}
    def da_co(k, t, m):
        """đã ghi khóa k: cập nhật cờ “chỉ nêu việc thay thế” (mọi lần nhắc đều là câu thay thế mới giữ True)."""
        if k in idx and not la_cau_thay_the(t, m.start(), m.end()): out[idx[k]]['neu_thay_the'] = False
        return k in seen
    def them(k, d, t, m):
        d['nguyen_van'] = goc[:300]  # v4.6: giữ nguyên văn đoạn GỐC (chưa chuẩn hóa) làm chứng cứ
        seen.add(k); idx[k] = len(out); d['neu_thay_the'] = la_cau_thay_the(t, m.start(), m.end()); out.append(d)
    for i, goc in enumerate(paras):
        if not goc: continue
        # v4.6 (KTS-01): so khớp trên bản chuẩn hóa trình bày (NBSP, zero-width, xuống dòng, khoảng trắng quanh “/”, “-”, gạch Unicode);
        # chứng cứ lấy từ bản gốc
        t = ND.chuan_so_hieu(goc)
        is_cc = t.startswith('Căn cứ')
        for m in re.finditer(LOAI + r'\s+(?:liên tịch\s+)?(?:số\s*[:]?\s*)' + SO, t):
            so = m.group(1)
            if not re.search(r'\d', so.split('/')[0].split('-')[0]): continue
            k = key_so(so)
            if da_co(k, t, m): continue
            them(k, {'loai': t[m.start():m.start() + 20].split(' số')[0], 'so': so, 'key': k, 'ten': None,
                     'doan': i + 1, 'ngu_canh': t[max(0, m.start() - 10):m.end() + 60], 'can_cu': is_cc}, t, m)
        # số hiệu đứng riêng: “QĐ 2307/QĐ-CĐKT”, “Quyết định 2264/QĐ-CĐKT”, “Nghị định 13/2023/NĐ-CP”, “208-QĐ/TW” (PB-05)
        for m in list(re.finditer(r'(?<![\w/])(\d{1,5}/(?:\d{4}/[A-ZĐ][A-ZĐ0-9]*(?:-[A-ZĐa-zđ0-9]+)*|[A-ZĐ][A-ZĐ0-9]*(?:-[A-ZĐa-zđ0-9]+)+))(?![\w/])', t)) + \
                 list(re.finditer(r'(?<![\w/\-])(\d{1,4}-[A-ZĐ]{1,6}/[A-ZĐ]{1,6})(?![\w/])', t)):
            so = m.group(1)
            if '/' not in so: continue
            k = key_so(so)
            if da_co(k, t, m): continue
            loai = loai_theo_ky_hieu(so)
            them(k, {'loai': loai, 'so': so, 'key': k, 'ten': None,
                     'doan': i + 1, 'ngu_canh': t[max(0, m.start() - 25):m.end() + 50], 'can_cu': is_cc}, t, m)
        # dạng rút gọn “Nghị định 13/2023”, “Thông tư 49/2026” (không có ký hiệu) – PB2-09
        for m in re.finditer(r'\b(Nghị định|Thông tư|NĐ|TT)\s+(?:số\s+)?(\d{1,5}/\d{4})(?![\d/])', t):
            k0 = key_so(m.group(2))
            loai_r = {'NĐ': 'Nghị định', 'TT': 'Thông tư'}.get(m.group(1), m.group(1))
            full = next((x for x in seen if x.startswith(k0 + '/') and cung_loai(x, loai_r)), None)  # v4.4 (PB4-WORK-01): cùng loại
            if full: da_co(full, t, m); continue
            k = 'RG:%s:%s' % (loai_r, k0)  # v4.5 (PB5-WORK-01): khóa rút gọn gồm cả loại – “Nghị định 9090/2026” khác “Thông tư 9090/2026”
            if da_co(k, t, m): continue
            them(k, {'loai': loai_r, 'so': m.group(2), 'key': k, 'ten': None, 'rut_gon': True,
                     'doan': i + 1, 'ngu_canh': t[max(0, m.start() - 10):m.end() + 50], 'can_cu': is_cc}, t, m)
        # v4.3 (TH-03): viện dẫn CHỈ CÓ SỐ, không năm, không ký hiệu: “NĐ 356”, “Quyết định 2307”, “TB 597”
        for m in re.finditer(r'\b(Nghị định|Thông tư|Quyết định|Thông báo|NĐ|TT|QĐ|TB)\s+(?:số\s+)?(\d{1,5})(?![\d/]|[.,]\d|-\w)', t):
            loai = {'NĐ': 'Nghị định', 'TT': 'Thông tư', 'QĐ': 'Quyết định', 'TB': 'Thông báo'}.get(m.group(1), m.group(1))
            so = m.group(2)
            # v4.4 (PB4-WORK-01): chỉ gộp vào viện dẫn đầy đủ CÙNG LOẠI, cùng số (“Nghị định 356/2025/NĐ-CP” không thay cho “Quyết định 356”)
            full = next((x for x in seen if (x.startswith(so + '/') or x.startswith(so + '-')) and cung_loai(x, loai)), None)
            if full: da_co(full, t, m); continue
            k = 'CHISO:%s:%s' % (loai, so)
            if da_co(k, t, m): continue
            them(k, {'loai': loai, 'so': so, 'key': k, 'ten': None, 'chi_so': True,
                     'doan': i + 1, 'ngu_canh': t[max(0, m.start() - 10):m.end() + 50], 'can_cu': is_cc}, t, m)
        # Luật/Bộ luật/Pháp lệnh nêu theo tên (không có số)
        cands = list(re.finditer(r'\b(Bộ luật|Luật|Pháp lệnh)\s+([A-ZĐÀ-Ỹ](?:(?!Luật|Bộ luật|;|\(|\)).){1,90}?)(?=\s+(?:ngày\s+\d|số\s*:?\s*\d|năm\s+\d{4}))', t))
        spans = [(m.start(), m.end()) for m in cands]
        n_chac = len(cands)  # v4.6: tên có mốc “ngày/số/năm” ngay sau là tên CHẮC; tên bắt bằng mẫu thứ hai là tên YẾU (có thể cắt thiếu/thừa)
        cands += [m for m in re.finditer(r'\b(Bộ luật|Luật|Pháp lệnh)\s+((?:[A-ZĐÀ-Ỹ][^\s;,.()]*)(?:\s+(?!ngày|số\s*:?\s*\d|năm|đã|được|sửa|và(?=\s+[A-ZĐÀ-Ỹ]|\s*$)|của|các|hiện)[^\s;,.()]+){0,9}?)(?=\s+(?:ngày|số\s*:?\s*\d|năm|đã|được|sửa đổi|và|của|hiện hành|mới nhất|quy định|tại|theo)|[;,.()]|$)', t) if not any(a <= m.start() < b for a, b in spans)]
        for i_c, m in enumerate(cands):
            ten = norm(m.group(1) + ' ' + m.group(2))
            if i_c >= n_chac:  # v4.6: tên YẾU dừng trước “và” – nếu sau “và” chỉ là 1–4 từ viết thường rồi hết câu/dấu câu thì “và …” thuộc tên
                mv = re.match(r'\s+và((?:\s+[a-zà-ỹđ][^\s;,.()]*){1,4})(?=\s*(?:[;,.()]|$))', t[m.end():])
                if mv: ten = norm(ten + ' và' + mv.group(1))
            cat = re.split(r'\s+(?:và|hoặc|,)\s+(?=(?:Nghị định|Thông tư|Quyết định|Luật|Bộ luật|Pháp lệnh|Nghị quyết|Chỉ thị|Thông báo)\b)', ten)
            bi_cat = len(cat) > 1
            ten = norm(cat[0])
            if re.match(r'^(Luật|Bộ luật|Pháp lệnh) (này|số)\b', ten): continue
            if len(ten.split()) < 2: continue
            k = 'TEN:' + ND.chuan_ten_luat(ten)
            # v4.6 (KTS-03): chỉ bỏ trùng KHỚP ĐÚNG hoặc tên bị cắt ở dấu phẩy (“Luật Thi đua” của “Luật Thi đua, khen thưởng”);
            # không coi “Luật Giáo dục nghề nghiệp” là bản trùng của “Luật Giáo dục”
            if da_co(k, t, m) or any(x.startswith(k + ',') for x in seen if x.startswith('TEN:')): continue
            if any(x.startswith('TEN:') and _mo_rong_rac(k, x) for x in seen): continue  # “Luật X trong thời hạn…” là tên đã có + lời văn
            if len(ten.split()) > 12: continue
            # đã có số hiệu ngay sau tên thì bỏ (đã bắt ở trên)
            after = t[m.end():m.end() + 25]
            if not bi_cat and re.match(r'\s*số\s*\d', after): continue
            them(k, {'loai': m.group(1), 'so': None, 'key': k, 'ten': ten, 'doan': i + 1, 'ten_chac': i_c < n_chac,
                     'ngu_canh': t[max(0, m.start() - 10):m.end() + 60], 'can_cu': is_cc}, t, m)
        # v4.6 (quy tắc người phụ trách xác nhận 02/11/2026 – PH-02): “Luật … ngày … (hợp nhất tại Văn bản hợp nhất số N/VBHN-X ngày …)”
        # → ghép viện dẫn Luật với VBHN; VBHN mang theo tên luật được hợp nhất và ngày để kiểm khớp với tệp trong hồ sơ
        for mh in re.finditer(r'\b(Bộ luật|Luật|Pháp lệnh)\s+(.{2,120}?)\s*(?:ngày\s+\d[^()]{0,40}?)?\(\s*(?:được\s+)?hợp nhất tại\s+'
                              r'(?:Văn bản hợp nhất|VBHN)\s+(?:số\s*:?\s*)?(\d{1,5}/VBHN-[A-ZĐ]+)\s*(?:,?\s*ngày\s+([^)]{0,40}))?\)', t, re.I):
            ten_l = ND.chuan_ten_luat(mh.group(1) + ' ' + re.split(r'\s+(?:ngày|số)\b', mh.group(2))[0])
            kv = key_so(mh.group(3))
            nd_ = re.search(r'(\d{1,2})\s*(?:tháng|/)\s*(\d{1,2})\s*(?:năm|/)\s*(\d{4})', mh.group(4) or '')
            if kv in idx:
                out[idx[kv]].setdefault('luat_hop_nhat', ten_l)
                if nd_: out[idx[kv]].setdefault('ngay_vbhn', [int(nd_.group(3)), int(nd_.group(2)), int(nd_.group(1))])
            kl = 'TEN:' + ten_l
            if kl in idx: out[idx[kl]].setdefault('vbhn_key', kv)
    # v4.6: tên luật bị cắt ở dấu phẩy xuất hiện TRƯỚC tên đầy đủ → bỏ bản cắt (không phụ thuộc thứ tự đoạn)
    ten_du = [x['key'] for x in out if x['key'].startswith('TEN:')]
    out = [x for x in out if not (x['key'].startswith('TEN:') and any(y.startswith(x['key'] + ',') for y in ten_du))]
    # tên YẾU (mẫu thứ hai) là phần đầu hoặc phần mở rộng của một tên khác → bỏ (không phụ thuộc thứ tự đoạn); hai tên CHẮC khác nhau được giữ
    # riêng (“Luật Giáo dục” và “Luật Giáo dục nghề nghiệp” – KTS-03)
    ten_k = [x['key'] for x in out if x['key'].startswith('TEN:')]
    out = [x for x in out if not (x['key'].startswith('TEN:') and (
        any(y != x['key'] and _mo_rong_rac(x['key'], y) for y in ten_k) or                      # tên dài = tên khác + lời văn
        (not x.get('ten_chac') and any(y.startswith(x['key'] + ' VÀ ') for y in ten_k))))]       # tên YẾU bị cắt ở chữ “và” của tên đầy đủ
    # v4.4 (PB4-WORK-01): không phụ thuộc thứ tự đoạn – dạng rút gọn/chỉ số đứng TRƯỚC viện dẫn đầy đủ cùng loại, cùng số thì gộp vào viện dẫn đầy đủ
    day_du = [x for x in out if not x.get('chi_so') and not x.get('rut_gon') and x.get('so')]
    giu = []
    for x in out:
        if x.get('chi_so') or x.get('rut_gon'):
            so_ = x['so']
            f_ = next((y for y in day_du if (y['key'].startswith(key_so(so_) + '/') or y['key'].startswith(key_so(so_) + '-')) and cung_loai(y['key'], x['loai'])), None)
            if f_:
                if not x.get('neu_thay_the', True): f_['neu_thay_the'] = False
                continue
        giu.append(x)
    return giu


# ---------------------------------------------------------------- phân loại tệp
def vai_tro(name, paras, jcs=None):
    """Nhận vai trò theo NỘI DUNG phần đầu; thứ tự cố định (v4.2 – PB2-03, PB2-08, PB2-14):
    1) tiêu đề có “TIẾP THU” và “GIẢI TRÌNH” → Báo cáo tiếp thu, giải trình;
    2) có dấu dự thảo (dòng “DỰ THẢO”/“Dự thảo lần …”, hoặc số văn bản để trống, kể cả kiểu số của văn bản Đảng) → dự thảo;
    3) tiêu đề báo cáo rà soát của Skill (“BÁO CÁO RÀ SOÁT DỰ THẢO…”, “BẢN NHÁP RÀ SOÁT”, “KẾT LUẬN ĐIỀU KIỆN TRÌNH KÝ”) → báo cáo rà soát lần trước;
    4) chỉ khi nội dung không cho tín hiệu mới xét tên tệp. Có thể chỉ định thẳng bằng --vai-tro."""
    # vùng tiêu đề: các đoạn đầu, dừng ở “Kính gửi”, đề mục I./1., hoặc đoạn lời văn dài > 200 ký tự
    vung, vj = [], []
    for k_, p in enumerate(paras[:15]):
        if not p or p.startswith('[Chú thích]'): continue
        if len(p) > 200 or re.match(r'^(Kính gửi|I\.|1\.|Căn cứ)', p): break
        vung.append(p); vj.append(jcs[k_] if jcs and k_ < len(jcs) else None)
    # v4.3 (TH-14): chỉ xét tên loại “BÁO CÁO” và tối đa 3 dòng trích yếu liền sau (không xét câu lời văn ngắn ở đầu)
    bc_i = next((i for i, p in enumerate(vung) if re.match(r'^BÁO CÁO\b', p) and len(p) <= 120), None)
    tieu_de = ''
    if bc_i is not None:  # v4.4 (PB4-WORK-09): trích yếu dừng ở câu lời văn (kết thúc bằng dấu chấm) hoặc đề mục/“Kính gửi”
        tieu_de = vung[bc_i]
        for p, j_ in zip(vung[bc_i + 1:bc_i + 4], vj[bc_i + 1:bc_i + 4]):
            if p.endswith(('.', ':', ';')) or re.match(r'^(Kính gửi|Căn cứ|Thực hiện|Phần|[IVX]+\.|\d+\.)', p) or len(p) > 160: break
            if jcs and j_ != 'center': break  # v4.5 (PB5-WORK-10): trích yếu là các dòng CANH GIỮA liền sau tên loại
            tieu_de += ' ' + p
        tieu_de = tieu_de.upper()
    dau = ' '.join(paras[:40]).upper()
    fn = nfc(name).upper()
    if 'TIẾP THU' in tieu_de and 'GIẢI TRÌNH' in tieu_de:
        return 'bc_tiep_thu'
    so_line = next((p for p in paras[:40] if re.match(r'^Số\b', p)), '')
    trong_so = bool(re.match(r'^Số\s*:?\s*(?:…|\.{2,}|_+)?\s*[/-]', so_line)) or bool(re.match(r'^Số\s*:?\s*$', so_line))
    co_dau_du_thao = any(re.match(r'^(DỰ THẢO|Dự thảo)(\s*(lần|LẦN)\s*\d+)?\s*[)\]]?$', p.strip(' ()[]')) for p in paras[:20] if p and len(p) < 40)
    if co_dau_du_thao or trong_so:
        return 'du_thao'
    if re.search(r'BÁO CÁO RÀ SOÁT (DỰ THẢO|CHÍNH THỨC|NHANH|LẦN \d)|BÁO CÁO SO SÁNH HAI BẢN|BẢN NHÁP RÀ SOÁT|KẾT LUẬN ĐIỀU KIỆN TRÌNH KÝ', dau):
        return 'bao_cao_ra_soat'
    if re.search(r'KTC-RA-SOAT|BAO[\s_-]*CAO[\s_-]*RA[\s_-]*SOAT', fn):
        return 'bao_cao_ra_soat'
    if re.search(r'TIEP[\s_-]*THU|GIAI[\s_-]*TRINH', fn):
        return 'bc_tiep_thu'
    return 'lien_quan'


def ngay_vb(paras):
    """v4.6 (KTS-22): ngày ký của văn bản = dòng “<Địa danh>, ngày … tháng … năm …” (dòng ngắn, ở vùng thể thức),
    không lấy ngày trong câu căn cứ/lời văn; ngày phải hợp lệ theo lịch. Không xác định được → None."""
    for p in paras[:60]:
        t = ND.chuan_trinh_bay(p)
        if len(t) > 90: continue
        m = re.match(r'^[^\W\d_][^,;:.]{0,40},\s*ngày\s+(\d{1,2})\s+tháng\s+(\d{1,2})\s+năm\s+(\d{4})\s*$', t)
        if m and ND.ngay_hop_le(m.group(3), m.group(2), m.group(1)):
            return (int(m.group(3)), int(m.group(2)), int(m.group(1)))
    return None


def _ten_luat_tieu_de(head):
    """v4.6 (PH-01, KTS-08): tên luật từ khối tiêu đề “LUẬT” + các dòng IN HOA liền sau (bỏ qua đoạn trống, nối tối đa 3 dòng,
    dừng ở dòng không in hoa). Không có dòng tên → không tạo khóa (trước đây sinh khóa “TEN:LUẬT ” khớp mọi luật)."""
    out = []
    for i, p in enumerate(head):
        t = ND.chuan_trinh_bay(p)
        if t in ('LUẬT', 'BỘ LUẬT', 'PHÁP LỆNH'):
            dong = []
            for q_ in head[i + 1:i + 8]:
                u = ND.chuan_trinh_bay(q_)
                if not u: continue
                if not ND.la_in_hoa(u) or re.match(r'^(Căn cứ|Chương|Điều|CHƯƠNG)\b', u) or len(dong) >= 3: break
                dong.append(u)
            if dong: out.append(ND.chuan_ten_luat(t + ' ' + ' '.join(dong)))
        else:
            m = re.match(r'^(LUẬT|BỘ LUẬT|PHÁP LỆNH)\s+(\S.*)$', t)
            if m and ND.la_in_hoa(t) and len(t) <= 160: out.append(ND.chuan_ten_luat(t))
    return out


# v4.6.1 (N12 – quyết định người phụ trách 02/11/2026): tệp nguồn chỉ có phần định danh (số, tên loại, trích yếu) không phải toàn văn → CHẶN.
# Tiêu chí chính là CẤU TRÚC (có thân văn bản); ngưỡng ký tự chỉ là điều kiện phụ, TẠM THỜI (vấn đề mở của tác giả).
NGUONG_THAN_TOI_THIEU = 30  # tạm thời – ký tự chữ của thân văn bản, chỉ chặn “thân” gần như trống (ví dụ chỉ có “Điều 1.”)
_DH_THAN = re.compile(r'^(?:(?:Điều|Chương|Mục|Phần|Phụ lục)\s+[\dIVXLC]+|\d+(?:\.\d+)*[.)]\s*\S|[a-zđ]\)\s*\S|[IVXLC]+\.\s*\S|(?:Căn cứ|Thực hiện|Theo đề nghị|Xét đề nghị)\b)', re.I)
_DINH_DANH = re.compile(r'^(?:Số\s*[:.]|Số hiệu\b|CỘNG HÒA|CỘNG HOÀ|Độc lập\s*[-–]|ĐẢNG CỘNG SẢN|Đảng Cộng sản Việt Nam|DỰ THẢO\b|[-–_=*.\s]+$)', re.I)
_DONG_NGAY = re.compile(r'^[^\d]{0,60},?\s*ngày\s+\d{1,2}\s+tháng\s+\d{1,2}\s+năm\s+\d{4}\s*$', re.I)


TRICH_YEU_TOI_DA = 4  # D8 (giữ): trích yếu sau tên loại tối đa 4 đoạn
# v4.6.3 (nghiệm thu lần 3 – mục 3, N12/F08): dấu hiệu CẤU TRÚC kết thúc trích yếu – Điều/Chương/khoản/điểm/gạch đầu dòng, “Kính gửi”,
# khối căn cứ, “Nơi nhận”. Độ dài, căn lề, dấu câu cuối, in hoa hay MỘT cụm mở đầu KHÔNG một mình kết luận đã có thân.
_DH_CAU_TRUC = re.compile(r'^(?:(?:Điều|Chương|Mục|Phần|Phụ lục)\s+[\dIVXLC]+\b|\d+(?:\.\d+)*[.)]\s*\S|[a-zđ]\)\s*\S|[IVXLC]+\.\s*\S|[-–•+*]\s*[^\W_])', re.I)
_CAN_CU = re.compile(r'^(?:Căn cứ|Thực hiện|Theo đề nghị|Xét đề nghị|Xét)\b', re.I)
_KINH_GUI = re.compile(r'^Kính gửi\b', re.I)
_NOI_NHAN = re.compile(r'^Nơi nhận\b', re.I)
_TEN_LOAI_DONG = re.compile(r'(?i)^(?:QUYẾT ĐỊNH|THÔNG BÁO|NGHỊ QUYẾT|TỜ TRÌNH|BÁO CÁO|KẾ HOẠCH|HƯỚNG DẪN|QUY ĐỊNH|QUY CHẾ|CHỈ THỊ|KẾT LUẬN|CHƯƠNG TRÌNH|ĐỀ ÁN|DANH MỤC|BIÊN BẢN|CÔNG VĂN|PHƯƠNG ÁN|QUY TRÌNH|NỘI QUY|ĐIỀU LỆ)(?=\s|$)')
_DAU_CAU = re.compile(r'[.;:!?…]["”»)]*$')
_CANH = {'both': 'deu', 'distribute': 'deu', 'center': 'giua', 'right': 'phai', 'end': 'phai', 'left': 'trai', 'start': 'trai'}


def than_van_ban(paras, jcs=None, chi_tiet=False):
    """→ (có thân văn bản?, số ký tự thân). v4.6.3 (nghiệm thu lần 3 – mục 3; N12, D8):
    1) Phần định danh: quốc hiệu, tiêu ngữ, tên cơ quan in hoa, “Số:”, dòng địa danh – ngày, TÊN LOẠI (in hoa, hoặc viết thường đứng đầu đoạn
       trong vùng đầu văn bản: “Quyết định về việc…”).
    2) Trích yếu: đoạn ĐẦU TIÊN sau tên loại luôn là trích yếu; tiếp theo tối đa TRICH_YEU_TOI_DA đoạn vẫn là trích yếu trừ khi gặp dấu hiệu
       CẤU TRÚC thân (Điều/Chương/khoản/điểm/gạch đầu dòng, “Kính gửi”, khối căn cứ, “Nơi nhận”, dòng in hoa) hoặc một CÂU THÂN rõ ràng =
       kết thúc bằng dấu câu VÀ căn lề khác căn lề của đoạn trích yếu đầu (đọc được căn lề) VÀ không mở đầu bằng chữ thường (dòng tiếp nối).
       Độ dài, căn lề, dấu câu, in hoa hoặc một cụm mở đầu KHÔNG một mình kết luận có thân (v4.6.2 dùng riêng từng dấu hiệu → nhận nhầm).
    3) Thân = phần còn lại, BỎ dòng căn cứ/“Thực hiện…”/“Xét đề nghị…”, dòng in hoa (“QUYẾT ĐỊNH:”, chức danh), dòng “Kính gửi”, và mọi
       thứ từ “Nơi nhận” trở đi; có thân khi đủ NGUONG_THAN_TOI_THIEU ký tự (D8 – điều kiện phụ).
    Văn bản ngắn chỉ có ≤ 4 đoạn văn xuôi sau tên loại, không có dấu hiệu cấu trúc và không có câu thân rõ ràng → KHÔNG xác định được thân
    → coi như thiếu toàn văn (CHẶN, đề nghị cung cấp toàn văn) – giới hạn đã công bố, không tự nhận ĐỦ."""
    jj = list(jcs) if jcs else []
    ps = []
    for k, p in enumerate(paras):
        t = ND.chuan_trinh_bay(p).strip()
        if t: ps.append((t, _CANH.get(jj[k]) if k < len(jj) and jj[k] else None))
    def la_dau_hieu(q):
        return bool(_DH_CAU_TRUC.match(q) or _CAN_CU.match(q) or _KINH_GUI.match(q) or _NOI_NHAN.match(q))
    i, sau_ten_loai, n_vung = 0, False, 0
    while i < len(ps) and i < 14 + TRICH_YEU_TOI_DA:
        p, _ = ps[i]
        if _DINH_DANH.match(p) and not ND.la_in_hoa(p): sau_ten_loai = False; i += 1; continue
        if re.match(r'^V/[vV]\b', p): sau_ten_loai = False; i += 1; continue  # trích yếu công văn “V/v …” thuộc phần định danh
        if la_dau_hieu(p) and not ND.la_in_hoa(p): break
        if _DINH_DANH.match(p) or _DONG_NGAY.match(p) or (ND.la_in_hoa(p) and len(p) <= 160 and not re.match(r'(?i)^(?:Điều|Chương)\s+\d', p)
                                                           and not re.match(r'^[IVXLC]+\.\s', p)):
            sau_ten_loai = ND.la_in_hoa(p) and not _DINH_DANH.match(p); i += 1; continue
        dau_ty = None
        if not sau_ten_loai and _TEN_LOAI_DONG.match(p) and len(p) <= 300 and not _DAU_CAU.search(p):
            dau_ty = ps[i][1]; i += 1; n_ty = 1      # “Quyết định về việc…” viết thường: tên loại + trích yếu cùng một đoạn
        elif sau_ten_loai:
            dau_ty = ps[i][1]; i += 1; n_ty = 1      # đoạn đầu sau tên loại luôn là trích yếu
        else:
            break
        while i < len(ps) and n_ty < TRICH_YEU_TOI_DA:
            q, cq = ps[i]
            if la_dau_hieu(q) or ND.la_in_hoa(q): break
            cau_than = bool(_DAU_CAU.search(q)) and cq is not None and dau_ty is not None and cq != dau_ty and not q[:1].islower()
            if cau_than: break
            i += 1; n_ty += 1
        sau_ten_loai = False; n_vung = max(n_vung, n_ty)
        if i < len(ps) and ND.la_in_hoa(ps[i][0]) and not _DH_CAU_TRUC.match(ps[i][0]):
            continue  # sau trích yếu còn dòng in hoa (thẩm quyền ban hành, “HIỆU TRƯỞNG…”) – vẫn thuộc phần định danh
        break
    than = []
    for p, _ in ps[i:]:
        if _NOI_NHAN.match(p): break
        if _CAN_CU.match(p) or _KINH_GUI.match(p) or ND.la_in_hoa(p): continue
        than.append(p)
    so_ky_tu = sum(len(re.sub(r'\s', '', p)) for p in than)
    if chi_tiet:  # v4.6.4 (Q5): số đoạn sau tên loại ngoài đoạn trích yếu đầu – điều kiện để xác nhận thủ công toàn văn
        return so_ky_tu >= NGUONG_THAN_TOI_THIEU, so_ky_tu, (n_vung - 1 if n_vung else 0) + (1 if so_ky_tu else 0)
    return so_ky_tu >= NGUONG_THAN_TOI_THIEU, so_ky_tu


# v4.6.1 (N46 – quyết định người phụ trách 02/11/2026): hai tệp trùng PHẦN NỘI DUNG (bỏ metadata) là một văn bản; khác chữ vẫn MƠ HỒ.
_PHAN_ND_DOCX = re.compile(r'^word/(?:document|header\d*|footer\d*|footnotes|endnotes|numbering|comments)\.xml$|^word/_rels/document\.xml\.rels$|^word/(?:media|embeddings)/')
_PHAN_ND_XLSX = re.compile(r'^xl/(?:sharedStrings\.xml|worksheets/[^/]+\.xml|_rels/workbook\.xml\.rels|workbook\.xml)$')


def ma_bam_noi_dung(f):
    """Mã băm các phần mang nội dung: .docx – thân, đầu/chân trang, chú thích, đánh số, ảnh nhúng, liên kết; .xlsx – ô, trang tính;
    bỏ docProps (tác giả, ngày tạo/sửa), settings, styles, theme. Định dạng khác → mã băm cả tệp."""
    ext = os.path.splitext(f)[1].lower()
    h = hashlib.sha256()
    try:
        if ext in ('.docx', '.xlsx'):
            mau = _PHAN_ND_DOCX if ext == '.docx' else _PHAN_ND_XLSX
            with zipfile.ZipFile(f) as z:
                for nm in sorted(n for n in z.namelist() if mau.search(n)):
                    h.update(nm.encode('utf-8') + b'\0' + z.read(nm) + b'\0')
            return 'nd:' + h.hexdigest()
        h.update(open(f, 'rb').read()); return 'tep:' + h.hexdigest()
    except Exception:
        return 'loi:' + f


def ma_dinh_danh(name, paras):
    """Các khoá nhận diện một tệp được cung cấp: số hiệu + tên luật. v4.6: số hiệu đọc qua ND.chuan_so_hieu (KTS-01);
    số trong tên tệp chỉ dùng khi nội dung không có dòng “Số:” khác số đó (tên tệp chỉ là ứng viên)."""
    keys = set()
    head = paras[:80]
    so_nd = set()
    for p in head[:40]:
        t = ND.chuan_so_hieu(p)
        if len(t) > 90: continue
        m = re.match(r'^(?:Số|Luật số|Bộ luật số|Pháp lệnh số|Số hiệu)\s*[:]?\s*' + SO, t)
        if m: so_nd.add(key_so(m.group(1)))
    keys |= so_nd
    fn = nfc(os.path.splitext(name)[0])
    so_ten = set()
    for m in re.finditer(r'(\d{1,5})[_\-](\d{4})[_\-]([A-ZĐ]{2,}[A-Z0-9Đ\-]*)', fn):
        a, b, c = m.groups()
        c = c.replace('ND', 'NĐ').replace('_', '-')
        so_ten.add(key_so('%s/%s/%s' % (a, b, c)))
    for m in re.finditer(r'(\d{1,5})[_\-](VBHN)[_\-]([A-Z]+)', fn):
        so_ten.add(key_so('%s/VBHN-%s' % (m.group(1), m.group(3))))
    if not so_nd:
        keys |= so_ten
    for ten in _ten_luat_tieu_de(head):
        keys.add('TEN:' + ten)
    return keys


def thong_tin_vbhn(paras):
    """v4.6 (PH-02): số, ngày, luật được hợp nhất của một tệp VBHN – để kiểm khớp với viện dẫn “(hợp nhất tại VBHN số … ngày …)”."""
    head = paras[:30]
    so, ngay, luat = None, None, None
    for p in head:
        t = ND.chuan_so_hieu(p)
        m = re.match(r'^Số\s*:?\s*(\d{1,5}/VBHN-[A-ZĐ]+)', t)
        if m and so is None: so = key_so(m.group(1))
    ngay = ngay_vb(head)
    ten = _ten_luat_tieu_de(head)
    if ten: luat = ten[0]
    else:
        for p in head[:15]:
            m = re.match(r'^(Bộ luật|Luật|Pháp lệnh)\s+(.{2,120}?)(?:\s+số\b|\s+ngày\b|,\s*có hiệu lực)', ND.chuan_trinh_bay(p))
            if m: luat = ND.chuan_ten_luat(m.group(1) + ' ' + m.group(2)); break
    return {'so': so, 'ngay': list(ngay) if ngay else None, 'luat': luat}


# ---------------------------------------------------------------- chính
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('duong_dan', nargs='*')  # v4.6.1 (N34): không bắt buộc khi chỉ --kiem-moi-truong
    ap.add_argument('--tac-vu', default='ra-soat', choices=['ra-soat', 'so-sanh', 'chuan-hoa'],
                    help='ra-soat: rà soát chính thức/nhanh (G1–G8); so-sanh: so sánh hai bản (G1–G5, không áp G6–G8); chuan-hoa: chỉ G1–G3')
    ap.add_argument('--vong', default='auto')
    ap.add_argument('--vai-tro', action='append', default=[], metavar='TÊN_TỆP=VAI_TRÒ',
                    help='chỉ định vai trò tệp: du_thao | du_thao_cu | bao_cao_ra_soat | bc_tiep_thu | kem_theo | lien_quan (PB2-03, TH-02)')
    ap.add_argument('--xac-nhan-kem', action='append', default=[], metavar='TÊN_TỆP=LÝ_DO',
                    help='v4.5 (quyết định F1): người rà soát xác nhận tệp là văn bản kèm theo của dự thảo khi trích yếu không khớp/không có (cùng tên loại); lý do ≥ 20 ký tự; ghi vào kết quả cổng và báo cáo I.7')
    ap.add_argument('--xac-nhan-toan-van', action='append', default=[], metavar='TÊN_TỆP=LÝ_DO',
                    help='v4.6.4 (Q5 – quyết định 03/11/2026): người rà soát xác nhận tệp nguồn RẤT NGẮN là toàn văn khi cổng không xác định được thân văn bản theo cấu trúc; lý do ≥ 20 ký tự; không dùng được cho tệp chỉ có phần định danh và một đoạn trích yếu; ghi vào kết quả cổng và báo cáo I.7 (chữ đỏ)')
    ap.add_argument('--xuat-anh', default=None, help='thư mục lưu ảnh lớn trong tệp Word để người rà soát mở xem (PB2-07)')
    ap.add_argument('--du-thao', default=None)
    ap.add_argument('--kho', default=KHO_DEFAULT)
    ap.add_argument('--json', default=None)
    ap.add_argument('--kiem-moi-truong', action='store_true', help='v4.6 (KTS-23): in tình trạng công cụ phụ thuộc (python-docx, pdftotext, pdfinfo, soffice) rồi thoát')
    a = ap.parse_args()
    if not a.duong_dan and not a.kiem_moi_truong:
        ap.error('cần ít nhất một đường dẫn hồ sơ (thư mục hoặc tệp), hoặc chỉ dùng --kiem-moi-truong')
    if a.kiem_moi_truong:
        for c_ in ('pdftotext', 'pdfinfo', 'soffice', 'libreoffice'):
            print('%-12s %s' % (c_, shutil.which(c_) or 'THIẾU'))
        try:
            import docx  # noqa: F401
            print('python-docx  có')
        except Exception:
            print('python-docx  THIẾU')
        sys.exit(0)

    # v4.6.2 (F11): ghi tham số chạy THỰC để tao_bao_cao.py tính lại kết quả cổng từ tệp (không tin JSON cổng); đường dẫn đầu vào chuẩn hóa tuyệt đối
    a.duong_dan = [os.path.abspath(x) for x in a.duong_dan]
    THAM_SO = dict(duong_dan=list(a.duong_dan), tac_vu=a.tac_vu, vong=str(a.vong), vai_tro=list(a.vai_tro), xac_nhan_kem=list(a.xac_nhan_kem), xac_nhan_toan_van=list(a.xac_nhan_toan_van),
                   du_thao=a.du_thao, kho=os.path.abspath(a.kho), cwd=os.getcwd())
    files = []
    chan, canh_bao, bang, anh_xem = [], [], [], []
    # v4.6.3 (D2 – quyết định 02/11/2026, ưu tiên số 1): TỪ CHỐI Kho ngoài Kho của gói (v4.6.2 chỉ cảnh báo chữ đỏ). So đường dẫn thực
    # đã chuẩn hóa theo hệ điều hành: cách viết tương đương của CÙNG Kho (“..”, “.”, liên kết tượng trưng tới đúng tệp) được nhận;
    # bản sao Kho, thư mục liên kết tới nơi khác, tệp không tồn tại → từ chối, không nạp Kho đó.
    kho_ngoai = not ND.cung_tep_kho(a.kho, KHO_DEFAULT)
    if kho_ngoai:
        chan.append('Kho “%s” không phải Kho của gói Skill (%s) – từ v4.6.3 Kho ngoài gói bị từ chối (D2); bỏ tùy chọn --kho hoặc trỏ đúng Kho của gói rồi chạy lại cổng.' % (a.kho, os.path.normpath(KHO_DEFAULT)))
    for d in a.duong_dan:
        if os.path.isdir(d):
            for r, _, fs in os.walk(d):
                for f in sorted(fs): files.append(os.path.join(r, f))
        elif os.path.exists(d):
            files.append(d)
        else:  # v4.6 (KTS-07): đầu vào không tồn tại không được bỏ qua im lặng
            chan.append('Đường dẫn đầu vào “%s” không tồn tại – kiểm tra lại tên tệp/thư mục rồi chạy lại cổng.' % d)
    if a.json:  # v4.6.3: tệp kết quả không được trùng tệp hồ sơ/Kho (không ghi đè), thư mục phải có – kiểm TRƯỚC khi xử lý
        e_ = ND.kiem_duong_dan_ghi(a.json, [f for f in files if os.path.splitext(f)[1].lower() not in BO_QUA] + [KHO_DEFAULT], '.json')
        if e_:
            print('LỖI THAM SỐ --json: %s. Cổng không chạy, không ghi kết quả.' % e_); sys.exit(2)
    docs, JC = {}, {}
    # v4.4 (PB4-GPT-04, PB4-WORK-07): định danh tệp = tên tệp; nếu trùng tên ở các thư mục con thì dùng đường dẫn tương đối
    # v4.5 (PB5-WORK-04): đường dẫn tương đối tính từ thư mục gốc CHUNG của mọi đầu vào (kể cả khi truyền nhiều thư mục/tệp)
    try:
        goc_chung = os.path.commonpath([os.path.dirname(os.path.abspath(f)) for f in files]) if files else ''
    except ValueError:
        goc_chung = ''
    def _rel(f):
        af = os.path.abspath(f)
        return os.path.relpath(af, goc_chung).replace(os.sep, '/') if goc_chung else af.replace(os.sep, '/')
    _dem = {}
    for f in files: _dem[os.path.basename(f)] = _dem.get(os.path.basename(f), 0) + 1
    TEN = {f: (os.path.basename(f) if _dem[os.path.basename(f)] == 1 else _rel(f)) for f in files}
    if len(set(TEN.values())) < len(TEN):  # phòng trường hợp đặc biệt: vẫn trùng → dùng đường dẫn tuyệt đối
        TEN = {f: (os.path.basename(f) if _dem[os.path.basename(f)] == 1 else os.path.abspath(f).replace(os.sep, '/')) for f in files}
    for n_, k_ in sorted(_dem.items()):
        if k_ > 1 and not (n_.startswith('~$') or n_.startswith('.')):
            canh_bao.append('Có %d tệp cùng tên “%s” ở các thư mục khác nhau – script phân biệt theo đường dẫn (%s); khi chỉ định --vai-tro, --du-thao dùng đường dẫn này.' % (k_, n_, '; '.join(TEN[f] for f in files if os.path.basename(f) == n_)))
    for f in files:
        name = TEN[f]
        ext = os.path.splitext(name)[1].lower()
        if name.startswith('~$') or name.startswith('.') or ext in BO_QUA:
            bang.append((name, ext, 'bỏ qua (tệp hệ thống/không phải hồ sơ)')); continue
        if ext in NEN:
            chan.append('Tệp nén “%s” – đề nghị giải nén và gửi từng tệp (.docx/.xlsx/PDF có lớp chữ); Skill không nhận tệp nén vì có thể chứa ảnh, bản scan.' % name)
            bang.append((name, ext, 'CHẶN – tệp nén')); continue
        if ext in ANH:
            chan.append('Tệp ảnh/bản chụp “%s” – không nhận ảnh hoặc bản chụp; đề nghị cung cấp bản .docx/.xlsx.' % name)
            bang.append((name, ext, 'CHẶN – ảnh/bản chụp')); continue
        if ext in CU:
            chan.append('Tệp “%s” định dạng %s – đề nghị lưu lại sang %s rồi gửi lại.' % (name, ext, CU[ext]))
            bang.append((name, ext, 'CHẶN – định dạng không nhận')); continue
        if ext == '.pdf':
            t, pages = pdf_info(f)
            if t == 'THIEU_CONG_CU':  # v4.6 (KTS-23): lỗi môi trường, không quy thành tệp scan
                chan.append('Không kiểm được lớp chữ của tệp PDF “%s”: máy chạy Skill thiếu công cụ pdftotext (Poppler) – đây là lỗi môi trường, chưa phải kết luận tệp là bản scan; cài Poppler (chạy kiem_ke_ho_so.py --kiem-moi-truong để kiểm) hoặc cung cấp bản .docx.' % name)
                bang.append((name, ext, 'CHƯA KIỂM – thiếu công cụ pdftotext')); continue
            dens = len(re.sub(r'\s', '', t or '')) / max(pages, 1)
            if t is None or dens < 200:
                chan.append('Tệp PDF “%s” không có lớp chữ (bản scan/ảnh, %.0f ký tự/trang) – đề nghị cung cấp bản .docx hoặc PDF có lớp chữ.' % (name, dens))
                bang.append((name, ext, 'CHẶN – PDF scan')); continue
            paras = [norm(x) for x in t.splitlines()]
            docs[f] = paras; bang.append((name, ext, 'nhận – PDF có lớp chữ (%.0f ký tự/trang)' % dens)); continue
        if ext not in NHAN:
            chan.append('Tệp “%s” định dạng %s không thuộc định dạng được nhận (.docx, .xlsx, .pdf có lớp chữ).' % (name, ext))
            bang.append((name, ext, 'CHẶN – định dạng không nhận')); continue
        try:
            paras = docx_paras(f) if ext == '.docx' else xlsx_text(f)
            if ext == '.docx': JC[f] = docx_jc(f)
        except Exception as e:
            chan.append('Không đọc được tệp “%s” (%s) – đề nghị kiểm tra và gửi lại.' % (name, type(e).__name__))
            bang.append((name, ext, 'CHẶN – lỗi đọc tệp')); continue
        # v4.4 (PB4-GPT-05): tệp Word ngắn (phụ lục danh mục vài dòng) vẫn nhận; chỉ chặn khi ít chữ VÀ có ảnh (ảnh chụp dán vào Word) hoặc gần như trống
        n_chu0 = len(re.sub(r'\s', '', ''.join(paras)))
        # v4.5 (PB5-WORK-09): ảnh nhỏ (biểu trưng, dưới 1/4 trang) không làm tệp bị coi là “không có chữ”
        if ext == '.docx' and (n_chu0 < 15 or (n_chu0 < 200 and docx_co_anh(f) and docx_anh_lon(f))):
            chan.append('Tệp “%s” gần như không có chữ (%d ký tự%s) – đề nghị cung cấp bản có nội dung chữ.' % (name, n_chu0, ', có ảnh dán vào Word' if n_chu0 >= 15 else ''))
            bang.append((name, ext, 'CHẶN – không có lớp chữ')); continue
        if ext == '.docx':
            lon = docx_anh_lon(f, a.xuat_anh)
            n_chu = len(''.join(paras))
            # PB2-07 (quyết định của Hiệu trưởng 27/10/2026): tệp chủ yếu là ảnh → script chặn; tệp nhiều chữ có ảnh ≥ 1/4 trang
            # → người rà soát MỞ XEM ảnh; nếu là văn bản chụp/scan thì chặn (G1), nếu là sơ đồ/hình minh họa thì nhận
            if lon and not (n_chu / len(lon) < 3000 or any(cx * cy >= 0.8 * A4_EMU2 for cx, cy, _ in lon)):
                anh_xem.append((name, len(lon), [p_ for _, _, p_ in lon if p_]))
                canh_bao.append('PHẢI XEM ẢNH: tệp “%s” có %d ảnh ≥ 1/4 trang kèm %d ký tự chữ%s. Người rà soát mở xem từng ảnh: nếu là văn bản chụp/bản scan → coi như CHẶN (G1) và gửi thông báo chặn; nếu là sơ đồ, hình minh họa → nhận.' % (
                    name, len(lon), n_chu, (' – ảnh đã xuất: ' + '; '.join(p_ for _, _, p_ in lon if p_)) if any(p_ for _, _, p_ in lon) else ' (chạy lại với --xuat-anh <thư mục> để xuất ảnh)'))
                lon = []
            if lon:
                chan.append('Tệp “%s” chứa %d ảnh cỡ lớn (ảnh chụp/bản scan dán vào Word, ≥ 1/4 trang) – không nhận ảnh, bản scan; đề nghị cung cấp nội dung dạng chữ.' % (name, len(lon)))
                bang.append((name, ext, 'CHẶN – chứa ảnh chụp/scan')); continue
        docs[f] = paras; bang.append((name, ext, 'nhận'))

    vt = {f: vai_tro(os.path.basename(f), p, JC.get(f)) for f, p in docs.items()}
    kem = {}  # v4.3 (TH-02): phụ lục / văn bản kèm theo nộp thành tệp riêng
    for f, p in docs.items():
        if vt[f] in ('lien_quan', 'du_thao'):
            tk = tieu_de_kem(p)
            # v4.4 (PB4-WORK-09): tệp có dấu DỰ THẢO mà tên loại có thể đứng riêng (Kế hoạch, Chương trình, Đề án, Hướng dẫn)
            # và không có dòng “(Kèm theo …)” vẫn là dự thảo
            if tk and vt[f] == 'du_thao' and tk[0] == 'kem_theo' and loai_kem(tk[1]) not in LUON_KEM and \
                    not any(re.search(r'(?i)\(\s*(?:ban hành\s+)?kèm theo', x) for x in p[:10]):
                tk = None
            if tk: kem[f] = tk; vt[f] = 'kem_theo'
    VAI_HL = ('du_thao', 'du_thao_cu', 'bao_cao_ra_soat', 'bc_tiep_thu', 'kem_theo', 'lien_quan')
    def tim_tep(ten_):  # v4.6 (KTS-07): một bộ phân giải tên tệp duy nhất – trùng tên ngắn hoặc không có thì báo, không chọn ngầm
        ten_ = ten_.strip()
        hit = [f for f in docs if TEN[f] == ten_ or os.path.abspath(f) == os.path.abspath(ten_)]
        if not hit: hit = [f for f in docs if os.path.basename(f) == ten_]
        return hit
    for chi_dinh in a.vai_tro:
        ten_, _, vai_ = chi_dinh.partition('=')
        hit_ = tim_tep(ten_)
        if vai_.strip() not in VAI_HL:
            chan.append('--vai-tro “%s”: vai trò “%s” không hợp lệ (chỉ nhận %s).' % (chi_dinh[:80], vai_.strip(), ', '.join(VAI_HL)))
        elif not hit_:
            chan.append('--vai-tro “%s”: không có tệp “%s” trong hồ sơ đã nhận.' % (chi_dinh[:80], ten_.strip()))
        elif len(hit_) > 1:
            chan.append('--vai-tro “%s”: tên “%s” trùng %d tệp (%s) – ghi đường dẫn tương đối như cổng ghi.' % (chi_dinh[:80], ten_.strip(), len(hit_), '; '.join(TEN[f] for f in hit_)))
        # v4.6.1 (N07): áp vai trò bằng CHÍNH kết quả bộ phân giải đã kiểm (tên như cổng ghi, tên ngắn duy nhất, đường dẫn tuyệt đối)
        if len(hit_) == 1 and vai_.strip() in VAI_HL:
            f = hit_[0]
            vt[f] = vai_.strip(); canh_bao.append('Vai trò “%s” của tệp “%s” do người rà soát chỉ định (--vai-tro).' % (vai_.strip(), TEN[f]))
            if vai_.strip() == 'kem_theo': kem[f] = tieu_de_kem(docs[f]) or ('kem_theo', '(không có tiêu đề tên loại)', '')  # v4.5: chỉ sửa vai trò, vẫn kiểm khớp
            if vai_.strip() != 'kem_theo': kem.pop(f, None)
    if a.du_thao and len(tim_tep(a.du_thao)) != 1:
        chan.append('--du-thao “%s”: %s.' % (a.du_thao, 'không có tệp này trong hồ sơ' if not tim_tep(a.du_thao) else 'tên trùng nhiều tệp – ghi đường dẫn tương đối như cổng ghi'))
    if a.du_thao and len(tim_tep(a.du_thao)) == 1:  # v4.6.1 (N09): dùng cùng bộ phân giải (bỏ khoảng trắng ngoài tên, đường dẫn tuyệt đối)
        chon_ = tim_tep(a.du_thao)[0]
        for f in docs:
            if f == chon_:
                vt[f] = 'du_thao'
            elif vt[f] == 'du_thao':
                vt[f] = 'du_thao_cu'
    du_thao = [f for f in docs if vt[f] == 'du_thao']
    if a.tac_vu == 'so-sanh':
        # so sánh hai bản: ĐÚNG HAI bản dự thảo (quyết định của Hiệu trưởng 26/10/2026 điểm 3; 27/10/2026 – PB2-15; v4.3 – TH-01).
        # Văn bản liên quan chỉ được coi là “bản” khi tên tệp ghi dự thảo/số phiên bản VÀ số văn bản chưa điền.
        du_thao = [f for f in docs if vt[f] in ('du_thao', 'du_thao_cu')]
        if len(du_thao) < 2:
            def ung_vien(f):
                ten = nfc(os.path.splitext(os.path.basename(f))[0]).upper()
                co_ten = re.search(r'DU[\s_-]*THAO|DỰ[\s_-]*THẢO|(?:^|[\s_\-(.])(?:V|LAN|LẦN|BAN|BẢN)\s*\d+', ten)
                so_line = next((p for p in docs[f][:40] if re.match(r'^Số\b', p)), '')
                # v4.4 (PB4-WORK-08): vắng dòng “Số” khác dòng số để trống – vắng thì chỉ nhận khi tên tệp ghi rõ “dự thảo”; tài liệu tham khảo không bao giờ là “bản”
                tham_khao = any('THAM KHẢO' in nfc(p).upper() for p in docs[f][:10] if len(p) < 80)
                co_so_trong = bool(so_line) and not re.match(r'^Số\s*:?\s*\d', so_line)
                ghi_du_thao = re.search(r'DU[\s_-]*THAO|DỰ[\s_-]*THẢO', ten)
                return vt[f] == 'lien_quan' and co_ten and not tham_khao and (co_so_trong or (not so_line and ghi_du_thao))
            du_thao += [f for f in docs if ung_vien(f)]
        for f in du_thao: vt[f] = 'du_thao'
        if len(du_thao) != 2:
            chan.append('So sánh hai bản: cần đúng 2 bản dự thảo (.docx) – hiện nhận diện được %d bản%s; đề nghị chỉ rõ hai tệp cần so sánh (chạy lại với --vai-tro "<tệp>=du_thao" cho hai bản, "<tệp>=lien_quan" cho tệp khác).' % (
                len(du_thao), (' (' + '; '.join(TEN[x] for x in du_thao) + ')') if du_thao else ''))
    elif len(du_thao) > 1:
        def ver(f):
            m = re.findall(r'(?:^|[\s_\-(.])(?:V|LAN|BAN)\s*(\d+)(?![\d/])', ND.khong_dau(os.path.splitext(os.path.basename(f))[0]))  # v4.6 (KTS-06): so không dấu
            return int(m[-1]) if m else -1
        vs = sorted(du_thao, key=ver)
        if ver(vs[-1]) > ver(vs[-2]):
            for f in vs[:-1]: vt[f] = 'du_thao_cu'
            du_thao = [vs[-1]]
            canh_bao.append('Có %d bản dự thảo; xác định bản hiện hành là “%s” (số phiên bản lớn nhất). Nếu không đúng, chạy lại với --du-thao.' % (len(vs), TEN[vs[-1]]))
        else:
            chan.append('Có %d tệp được nhận diện là dự thảo (%s) nhưng không xác định được bản hiện hành – đề nghị nói rõ bản nào cần rà soát.' % (len(du_thao), '; '.join(TEN[x] for x in du_thao)))
    if not du_thao and a.tac_vu != 'so-sanh':
        lq = [f for f in docs if vt[f] == 'lien_quan']
        if len(lq) == 1 and not any(v in ('bao_cao_ra_soat', 'bc_tiep_thu') for v in vt.values()):
            vt[lq[0]] = 'du_thao'; du_thao = lq
            canh_bao.append('Không có tệp ghi “DỰ THẢO”; coi “%s” là dự thảo cần rà soát.' % TEN[lq[0]])
        else:
            chan.append('Không xác định được dự thảo cần rà soát (không tệp nào có chữ “DỰ THẢO” hoặc số văn bản để trống) – đề nghị cung cấp/chỉ rõ tệp dự thảo.')

    # ---- vòng rà soát
    co_bc_rs = [f for f in docs if vt[f] == 'bao_cao_ra_soat']
    co_tt = [f for f in docs if vt[f] == 'bc_tiep_thu']
    co_cu = [f for f in docs if vt[f] == 'du_thao_cu']
    if a.tac_vu != 'ra-soat':
        vong, vong_txt = 1, 'không áp dụng (tác vụ %s)' % a.tac_vu
    elif a.vong == 'auto':
        # v4.6 (KTS-06): so tên tệp KHÔNG DẤU (“lần 2” = “lan 2” = “LẦN 2”), nhận cả số ≥ 10
        vong = 2 if (co_bc_rs or co_cu or any(re.search(r'SUA\s*LAN|SAU\s*TRINH|(?:^|[\s_\-(.])LAN\s*(?:[2-9]|[1-9]\d+)(?!\d)', ND.khong_dau(os.path.basename(f))) for f in du_thao)) else 1
        vong_txt = '%d (tự nhận diện)' % vong
    else:
        vong = int(a.vong); vong_txt = str(vong)
    if vong >= 2:
        if not co_bc_rs:
            chan.append('Rà soát từ lần 2: thiếu Báo cáo rà soát lần trước – đề nghị cung cấp để đối chiếu việc tiếp thu.')
        if not co_tt:
            chan.append('Rà soát từ lần 2: thiếu Báo cáo tiếp thu, giải trình (lập thành văn bản riêng) của đơn vị soạn thảo – đề nghị cung cấp kèm dự thảo đã sửa.')
        if co_bc_rs and co_tt:
            d_rs = max((ngay_vb(docs[f]) or (0, 0, 0)) for f in co_bc_rs)
            d_tt = max((ngay_vb(docs[f]) or (0, 0, 0)) for f in co_tt)
            if d_rs != (0, 0, 0) and d_tt != (0, 0, 0) and d_tt < d_rs:
                chan.append('Báo cáo tiếp thu, giải trình (ngày %02d/%02d/%d) lập TRƯỚC báo cáo rà soát lần trước (ngày %02d/%02d/%d) – chưa phải báo cáo tiếp thu kết quả rà soát; đề nghị cung cấp bản mới.' % (d_tt[2], d_tt[1], d_tt[0], d_rs[2], d_rs[1], d_rs[0]))
            elif d_rs == (0, 0, 0) or d_tt == (0, 0, 0):
                canh_bao.append('Không đọc được ngày của báo cáo rà soát hoặc báo cáo tiếp thu; người rà soát kiểm tra thứ tự thời gian bằng tay.')

    # ---- trích dẫn trong dự thảo, phụ lục
    tdan, pl_thieu, xac_nhan_ghi = [], [], []
    if du_thao and a.tac_vu != 'chuan-hoa':
        pham_vi = du_thao if a.tac_vu == 'so-sanh' else du_thao[:1]
        so_ban_than = {key_so(m.group(1)) for f in du_thao for p in docs[f][:40] for m in [re.match(r'^Số\s*:\s*' + SO, ND.chuan_so_hieu(p))] if m}
        # v4.3 (TH-02a): quét viện dẫn trên dự thảo VÀ mọi tệp phụ lục/văn bản kèm theo nộp riêng; ghi tên tệp
        da = {}
        for f in pham_vi + [g for g in docs if g in kem]:
            for x in trich_dan(docs[f]):
                if x['key'] in so_ban_than: continue
                if x['key'] in da:
                    if not x.get('neu_thay_the', True): da[x['key']]['neu_thay_the'] = False
                    continue
                x['tep'] = TEN[f]; da[x['key']] = x; tdan.append(x)
        pl_tep = {v[1] for g, v in kem.items() if v and v[0] == 'phu_luc'}
        xac_nhan = {}
        for x_ in a.xac_nhan_kem:
            ten_, _, ly_ = x_.partition('=')
            hit_k = [g_ for g_ in tim_tep(ten_) if g_ in kem]  # v4.6.1: cùng bộ phân giải với --vai-tro, --du-thao
            g = hit_k[0] if len(hit_k) == 1 else None
            if g is None:
                chan.append('--xac-nhan-kem: không có tệp văn bản kèm theo tên “%s” trong hồ sơ.' % ten_.strip())
            elif len(ly_.strip()) < 20:
                chan.append('--xac-nhan-kem “%s”: phải ghi lý do cụ thể (≥ 20 ký tự) vì sao tệp này là văn bản kèm theo của dự thảo.' % ten_.strip())
            else:
                xac_nhan[g] = ly_.strip()
        kem_tep = [(g, v) for g, v in kem.items() if v and v[0] == 'kem_theo']
        dung_tep_chung = set()  # v4.6 (KTS-04, A15): một tệp kèm theo chỉ đáp ứng MỘT văn bản kèm theo của MỘT bản (không dùng chung giữa hai bản)
        def phu_luc_nhac(P):
            nhac = set()
            for p in P:
                for m in re.finditer(r'(?i)phụ lục\s+(?:số\s+)?([IVXLC]+|\d+)\b', p):
                    sau = p[m.end():m.end() + 45]
                    if re.match(r'\s*(?:ban hành\s+)?(?:kèm theo\s+|tại\s+|của\s+)?(?:' + LOAI + r'|NĐ|QĐ|TT|TB|HD|KH|NQ|CT)\s*(?:số\s*)?\d', sau) and 'này' not in sau[:30]:
                        continue  # phụ lục của văn bản khác
                    nhac.add(m.group(1).upper())
            return nhac
        def phu_luc_co(P):
            return {m.group(1).upper() for x in P for m in [PL_TITLE.match(x)] if m and len(x) < 120}
        # v4.6 (KTS-04, G09): kiểm ĐỆ QUY – phụ lục được nhắc trong tệp văn bản kèm theo riêng cũng phải có trong hồ sơ
        for g, v in kem_tep:
            co_g = phu_luc_co(docs[g]) | pl_tep | {x for f in pham_vi for x in phu_luc_co(docs[f])}
            for x in sorted(phu_luc_nhac(docs[g])):
                if x not in co_g:
                    pl_thieu.append(x)
                    chan.append('Văn bản kèm theo “%s” nhắc tới Phụ lục %s nhưng hồ sơ không có phụ lục này – đề nghị bổ sung.' % (TEN[g], x))
        for f in pham_vi:
            P = docs[f]; tien_to = ('Bản “%s”: ' % TEN[f]) if a.tac_vu == 'so-sanh' else ''
            nhac = set()
            for p in P:
                for m in re.finditer(r'(?i)phụ lục\s+(?:số\s+)?([IVXLC]+|\d+)\b', p):
                    sau = p[m.end():m.end() + 45]
                    if re.match(r'\s*(?:ban hành\s+)?(?:kèm theo\s+|tại\s+|của\s+)?(?:' + LOAI + r'|NĐ|QĐ|TT|TB|HD|KH|NQ|CT)\s*(?:số\s*)?\d', sau) and 'này' not in sau[:30]:
                        continue  # phụ lục của văn bản khác
                    nhac.add(m.group(1).upper())
            # v4.3 (TH-02c): chỉ coi là “có phụ lục” khi có TIÊU ĐỀ phụ lục thật (dòng “Phụ lục I”, “PHỤ LỤC I. …”), không phải câu lời văn
            co = {m.group(1).upper() for x in P for m in [PL_TITLE.match(x)] if m and len(x) < 120} | pl_tep
            for x in sorted(nhac):
                if x not in co:
                    pl_thieu.append(x)
                    chan.append(tien_to + 'Dự thảo nhắc tới Phụ lục %s nhưng hồ sơ không có phụ lục này – đề nghị bổ sung.' % x)
            # v4.4–v4.5 (PB4-GPT-01, PB4-WORK-02; PB5-GPT-01/02, PB5-WORK-02/03/08; quyết định F1): mỗi văn bản kèm theo mà CHÍNH bản này ban hành
            # phải có trong bản (sau “Nơi nhận”) hoặc là tệp riêng CÙNG TÊN LOẠI và CÙNG TRÍCH YẾU; ghép 1:1 (một tệp chỉ đáp ứng một văn bản);
            # trích yếu không khớp/không có: chỉ nhận khi người rà soát xác nhận --xac-nhan-kem "<tệp>=<lý do>" (cùng tên loại), ghi vào kết quả
            can_ = kem_can(P)
            ung = [('trong', None, l2, t2) for l2, t2 in kem_trong(P)] + [('tep', g, loai_kem(v[1]), v[2] if len(v) > 2 else '') for g, v in kem_tep if g not in dung_tep_chung]
            # v4.6 (KTS-05, G23): ghép 1:1 bằng ĐỐI SÁNH CỰC ĐẠI (đường tăng), không tham lam – kết quả không phụ thuộc thứ tự yêu cầu/tệp
            canh = {ci: sorted((ui for ui, (_, g, l2, t2) in enumerate(ung) if l2 == lk and diem_trich(ty, t2) > 0),
                               key=lambda ui: -diem_trich(ty, ung[ui][3])) for ci, (lk, ty) in enumerate(can_)}
            gan_u = {}
            def tang(ci, tham):
                for ui in canh[ci]:
                    if ui in tham: continue
                    tham.add(ui)
                    if ui not in gan_u or tang(gan_u[ui], tham):
                        gan_u[ui] = ci; return True
                return False
            for ci in canh: tang(ci, set())
            gan = {ci: ui for ui, ci in gan_u.items()}; dung = set(gan_u)
            for ui in dung:
                if ung[ui][0] == 'tep': dung_tep_chung.add(ung[ui][1])
            for ci, (lk, ty) in enumerate(can_):
                if ci in gan: continue
                mo_ta = '%s %s' % (lk.capitalize(), ty.strip()) if ty.strip() else lk.capitalize()
                xn_ = next((ui for ui, (k_, g, l2, t2) in enumerate(ung) if k_ == 'tep' and ui not in dung and l2 == lk and g in xac_nhan), None)
                if xn_ is not None:
                    dung.add(xn_); g = ung[xn_][1]; dung_tep_chung.add(g)
                    xac_nhan_ghi.append(dict(ban=TEN[f], van_ban_kem_theo=mo_ta[:160], tep=TEN[g], tieu_de_tep=(kem[g][1] + ' ' + (kem[g][2] if len(kem[g]) > 2 else '')).strip()[:160], ly_do=xac_nhan[g]))
                    canh_bao.append(tien_to + 'Người rà soát XÁC NHẬN THỦ CÔNG tệp “%s” là văn bản kèm theo “%s” (trích yếu không khớp/không có) – lý do: %s (quyết định F1 ngày 27/10/2026; ghi vào báo cáo I.7).' % (TEN[g], mo_ta[:100], xac_nhan[g]))
                    continue
                lech = [(TEN[g] if g else 'trong dự thảo', l2, t2, ui in dung) for ui, (k_, g, l2, t2) in enumerate(ung)]
                if lech:
                    chan.append(tien_to + 'Dự thảo ban hành kèm theo “%s” nhưng không có văn bản kèm theo khớp tên loại và trích yếu (%s) – đề nghị bổ sung đúng văn bản; nếu đúng là văn bản kèm theo cùng tên loại mà trích yếu ghi khác/không có, người rà soát xác nhận bằng --xac-nhan-kem "<tệp>=<lý do>".' % (
                        mo_ta[:120], '; '.join('%s: %s%s' % (n_, ((l2 or '(không rõ tên loại)') + ' ' + (t2 or '(không có trích yếu)')).strip()[:80], ' – đã ghép với văn bản kèm theo khác' if dg else '') for n_, l2, t2, dg in lech)))
                else:
                    chan.append(tien_to + 'Dự thảo ban hành kèm theo “%s” nhưng không thấy văn bản kèm theo này trong dự thảo hoặc hồ sơ – đề nghị bổ sung.' % mo_ta[:120])

    # ---- đối chiếu văn bản được đề cập
    # v4.6: bộ phân giải nguồn DUY NHẤT – ánh xạ một khóa → NHIỀU ứng viên (KTS-03); Kho chỉ tính là toàn văn khi tệp tồn tại và có
    # bản chữ (text/*.md), PDF scan “chỉ tham khảo” không đủ G5 (KTS-02); mục “Phụ lục … NĐ 30” không ghi đè khóa của Nghị định (KTS-02);
    # tên luật khớp ĐÚNG, không khớp tiền tố (KTS-03, PH-01); VBHN kiểm số, ngày, luật được hợp nhất (PH-02 – quy tắc 02/11/2026).
    kho_path = KHO_DEFAULT if not kho_ngoai else a.kho  # v4.6.3: cách viết tương đương đã được nhận → dùng ĐƯỜNG DẪN CHUẨN của Kho gói (tệp Kho tìm theo thư mục thật)
    kho = {'van_ban': []}
    if not kho_ngoai:
        kho, e_kho = ND.doc_json_an_toan(kho_path, 'danh mục Kho', 'trung_gian')
        if e_kho or not isinstance(kho, dict):
            chan.append('Không đọc được danh mục Kho của gói (%s) – gói Skill bị hỏng; cài lại gói.' % (e_kho or 'không phải đối tượng JSON'))
            kho = {'van_ban': []}
    kho_dir = os.path.dirname(os.path.abspath(kho_path))
    def kho_toan_van(v):
        f_ = os.path.join(kho_dir, v.get('file', ''))
        txt = os.path.join(kho_dir, 'text', os.path.splitext(os.path.basename(v.get('file', '')))[0] + '.md')
        if not v.get('file') or not os.path.exists(f_): return False, 'tệp Kho không tồn tại (%s)' % v.get('file', '')
        if not os.path.exists(txt) and not f_.lower().endswith(('.docx', '.xlsx')): return False, 'Kho chỉ có bản scan/PDF không có bản chữ – chỉ tham khảo'
        return True, ''
    kho_keys = {}  # khóa → [(mức ưu tiên, mục)] ; 0 = số hiệu chính của văn bản, 1 = từ khóa
    for v in kho.get('van_ban', []):
        sh = v.get('so_hieu', '') or ''
        la_pl = bool(re.match(r'(?i)^phụ lục\b', sh))
        m = re.fullmatch(SO, ND.chuan_so_hieu(sh))
        if m and not la_pl: kho_keys.setdefault(key_so(m.group(1)), []).append((0, v))
        for k in v.get('tu_khoa', []):
            m = re.fullmatch(r'(?:\D*?)' + SO, ND.chuan_so_hieu(k or ''))
            if m and not la_pl: kho_keys.setdefault(key_so(m.group(1)), []).append((1, v))
        if sh.upper().startswith(('LUẬT', 'PHÁP LỆNH')):
            kho_keys.setdefault('TEN:' + ND.chuan_ten_luat(sh), []).append((0, v))
        if v.get('ten_luat'):
            kho_keys.setdefault('TEN:' + ND.chuan_ten_luat(v['ten_luat']), []).append((0, v))
    def kho_chon(k):
        lst = kho_keys.get(k) or []
        if not lst: return None
        uu = min(x[0] for x in lst)
        vs = {id(v): v for u, v in lst if u == uu}
        return list(vs.values())
    het = {key_so(x.get('so_hieu', '')): x for x in kho.get('van_ban_het_hieu_luc_hay_gap', []) if isinstance(x, dict)}
    vbhn = kho.get('van_ban_hop_nhat_da_biet', [])
    hs_keys = {}
    vbhn_tt = {}
    sha_tep = {}
    khong_than, khong_than_nd = {}, {}  # v4.6.1 (N12): tệp nguồn chỉ có phần định danh; v4.6.4: số đoạn nghi vấn (Q5)
    for f, pp in docs.items():
        if vt[f] in ('du_thao', 'du_thao_cu', 'bao_cao_ra_soat', 'bc_tiep_thu'): continue
        sha_tep[f] = ma_bam_noi_dung(f)  # v4.6.1 (N46): gộp theo phần nội dung, bỏ metadata
        co_than_, n_, nd_ = than_van_ban(pp, JC.get(f), chi_tiet=True)  # v4.6.2 (F08): căn lề hiệu lực để nhận trích yếu nhiều đoạn theo cấu trúc
        if not co_than_: khong_than[f] = n_; khong_than_nd[f] = nd_
        for k in ma_dinh_danh(os.path.basename(f), pp): hs_keys.setdefault(k, []).append(f)
        if any('/VBHN-' in k for k in hs_keys if f in hs_keys[k]): vbhn_tt[f] = thong_tin_vbhn(pp)
    # v4.6.4 (Q5 – quyết định của người phụ trách 03/11/2026): xác nhận THỦ CÔNG toàn văn cho tệp nguồn rất ngắn mà cổng không xác định được
    # thân theo cấu trúc (tương tự --xac-nhan-kem của quyết định F1). Chỉ nhận khi tệp CÓ nội dung ngoài phần định danh và đoạn trích yếu đầu;
    # tệp chỉ có định danh + một đoạn trích yếu vẫn CHẶN (N12). Ghi vào kết quả cổng và báo cáo I.7 (chữ đỏ) để người ký xem lại.
    xac_nhan_tv_ghi = []
    for x_ in a.xac_nhan_toan_van:
        ten_, co_bang_, ly_ = x_.partition('=')
        if not co_bang_:
            chan.append('--xac-nhan-toan-van “%s”: phải ghi dạng "TÊN_TỆP=LÝ_DO" (lý do ≥ 20 ký tự).' % x_.strip()[:120]); continue
        hit_ = [g_ for g_ in tim_tep(ten_) if g_ in docs]
        g = hit_[0] if len(hit_) == 1 else None
        if g is None:
            chan.append('--xac-nhan-toan-van: không có tệp tên “%s” trong hồ sơ (hoặc tên trùng nhiều tệp – ghi đường dẫn như cổng ghi).' % ten_.strip())
        elif vt.get(g) in ('du_thao', 'du_thao_cu', 'bao_cao_ra_soat', 'bc_tiep_thu'):
            chan.append('--xac-nhan-toan-van “%s”: chỉ dùng cho văn bản nguồn (văn bản liên quan, văn bản kèm theo), không dùng cho tệp vai trò %s.' % (TEN[g], vt.get(g)))
        elif len(ND.noi_dung(ly_)) < 20:
            chan.append('--xac-nhan-toan-van “%s”: phải ghi lý do cụ thể (≥ 20 ký tự) vì sao tệp rất ngắn này là toàn văn.' % TEN[g])
        elif g not in khong_than:
            canh_bao.append('--xac-nhan-toan-van “%s”: cổng đã nhận tệp có thân văn bản – không cần xác nhận, không ghi xác nhận thủ công.' % TEN[g])
        elif khong_than_nd.get(g, 0) < 1:
            chan.append('--xac-nhan-toan-van “%s”: không xác nhận được – tệp chỉ có phần định danh và một đoạn trích yếu, không có nội dung nào khác (N12); đề nghị cung cấp toàn văn.' % TEN[g])
        else:
            xac_nhan_tv_ghi.append(dict(tep=TEN[g], ly_do=ND.noi_dung(ly_), so_ky_tu_than_nhan_duoc=khong_than[g], so_doan_ngoai_trich_yeu_dau=khong_than_nd.get(g)))
            del khong_than[g]
            canh_bao.append('XÁC NHẬN THỦ CÔNG TOÀN VĂN: tệp “%s” rất ngắn, cổng không xác định được thân theo cấu trúc; người rà soát xác nhận là toàn văn (lý do: %s). Người ký xem lại ở I.7.' % (TEN[g], ND.noi_dung(ly_)[:200]))
    gop_ghi, da_gop = [], set()
    def ung_vien(k):
        """Các tệp trong hồ sơ cho khóa k, gộp các tệp trùng PHẦN NỘI DUNG (v4.6.1 – N46); ghi đủ đường dẫn các tệp đã gộp."""
        nhom = {}
        for f in sorted(hs_keys.get(k, []), key=lambda f: TEN[f]): nhom.setdefault(sha_tep.get(f, f), []).append(f)
        for fs in nhom.values():
            if len(fs) > 1 and tuple(fs) not in da_gop:
                da_gop.add(tuple(fs))
                trung_byte = len({hashlib.sha256(open(x, 'rb').read()).hexdigest() for x in fs}) == 1
                gop_ghi.append(dict(tep=[TEN[x] for x in fs], duong_dan=[os.path.abspath(x) for x in fs], dung=TEN[fs[0]], kieu='trùng từng byte' if trung_byte else 'trùng phần nội dung, khác metadata'))
                canh_bao.append('Các tệp %s trùng %s – coi là MỘT văn bản, dùng “%s” (đường dẫn: %s).' % (
                    ', '.join('“%s”' % TEN[x] for x in fs), 'từng byte' if trung_byte else 'phần nội dung (thân, đầu/chân trang, chú thích, ảnh), chỉ khác metadata (tác giả, ngày tạo/sửa)',
                    TEN[fs[0]], '; '.join(os.path.abspath(x) for x in fs)))
        return sorted((fs[0] for fs in nhom.values()), key=lambda f: TEN[f])
    vbhn_ghi = []
    byname_ = {TEN[f]: f for f in docs}
    ket, da_giai = [], set()
    tdan_ten = {x['key']: x for x in tdan}
    def giai_vbhn(x):
        """→ (trạng thái, nguồn, lý do chặn | None) cho viện dẫn VBHN x."""
        uv = ung_vien(x['key'])
        if not uv: return None, '', None
        khop, lech = [], []
        for f in uv:
            tt_ = vbhn_tt.get(f) or thong_tin_vbhn(docs[f])
            ly = []
            if f in khong_than: ly.append('tệp chỉ có phần định danh, không có thân văn bản')  # v4.6.1 (N12)
            if tt_['so'] and tt_['so'] != x['key']: ly.append('tệp ghi số %s' % tt_['so'])
            if x.get('luat_hop_nhat'):
                if not tt_['luat']: ly.append('không xác định được luật được hợp nhất trong tệp')
                elif tt_['luat'] != x['luat_hop_nhat']: ly.append('tệp hợp nhất “%s”, dự thảo dẫn “%s”' % (tt_['luat'].capitalize(), x['luat_hop_nhat'].capitalize()))
            if x.get('ngay_vbhn'):
                if not tt_['ngay']: ly.append('không đọc được ngày của VBHN trong tệp')
                elif list(tt_['ngay']) != list(x['ngay_vbhn']): ly.append('tệp ngày %02d/%02d/%d, dự thảo dẫn ngày %02d/%02d/%d' % (tt_['ngay'][2], tt_['ngay'][1], tt_['ngay'][0], x['ngay_vbhn'][2], x['ngay_vbhn'][1], x['ngay_vbhn'][0]))
            (lech if ly else khop).append((f, ly))
        if len(khop) == 1:
            return 'Có trong hồ sơ', TEN[khop[0][0]], None
        if len(khop) > 1:
            return 'MƠ HỒ – nhiều tệp', '; '.join(TEN[f] for f, _ in khop), ('Có %d tệp khác nội dung cùng là %s (%s) – không tự chọn; đề nghị giữ lại đúng một tệp.' % (len(khop), x['so'], '; '.join(TEN[f] for f, _ in khop)))
        return 'KHÔNG KHỚP', '; '.join(TEN[f] for f, _ in lech), ('Văn bản hợp nhất số %s trong hồ sơ không khớp viện dẫn của dự thảo (%s) – đề nghị cung cấp đúng VBHN được dẫn hoặc sửa viện dẫn (quy tắc người phụ trách xác nhận 02/11/2026: VBHN phải khớp số, ngày, luật được hợp nhất).' % (
            x['so'], '; '.join('%s: %s' % (TEN[f], ', '.join(ly)) for f, ly in lech)))
    for x in tdan:
        st, nguon = None, ''
        ly_do_rieng = None
        if x.get('rut_gon'):  # “Nghị định 13/2023” → khóa đầy đủ “13/2023/NĐ-CP” nếu biết; v4.6 (KTS-03): nhiều ứng viên → mơ hồ, không chọn
            uv_full = sorted({k for bang_k in (hs_keys, kho_keys, het) for k in bang_k if k.startswith(key_so(x['so']) + '/') and cung_loai(k, x['loai'])})
            if len(uv_full) == 1: x = dict(x, key=uv_full[0])
            elif len(uv_full) > 1:
                st = 'MƠ HỒ – nhiều văn bản: ' + ', '.join(uv_full)
                ly_do_rieng = 'Viện dẫn rút gọn “%s %s” (tệp %s, đoạn %d) ứng với %d văn bản khác nhau (%s) – không tự chọn; đề nghị ghi đủ số, ký hiệu.' % (x['loai'], x['so'], x.get('tep', ''), x['doan'], len(uv_full), ', '.join(uv_full))
        if x.get('chi_so'):  # v4.3 (TH-03): “NĐ 356” → khớp DUY NHẤT một văn bản cùng loại, cùng số trong hồ sơ/Kho
            ung = sorted({k for bang_k in (hs_keys, kho_keys, het) for k in bang_k
                          if not k.startswith('TEN:') and (k.startswith(x['so'] + '/') or k.startswith(x['so'] + '-')) and any(h in k for h in HAU_TO.get(x['loai'], ()))})
            if len(ung) == 1:
                x = dict(x, key=ung[0], so=ung[0])
            else:
                st = 'Chưa xác định – viện dẫn chỉ có số (%s)' % ('trùng %d văn bản' % len(ung) if ung else 'không có trong hồ sơ, Kho')
                ly_do_rieng = 'Viện dẫn “%s %s” (tệp %s, đoạn %d: “%s…”) chỉ có số, không xác định được văn bản – đề nghị ghi đủ số, ký hiệu và cung cấp toàn văn.' % (
                    x['loai'], x['so'], x.get('tep', ''), x['doan'], x['ngu_canh'][:70])
        if x['key'] in da_giai: continue
        da_giai.add(x['key'])
        if st is None:
            if '/VBHN-' in x['key']:
                st, nguon, ly_do_rieng = giai_vbhn(x)
                if st == 'Có trong hồ sơ':
                    vbhn_ghi.append(dict(vbhn=x['so'], tep=nguon, luat=x.get('luat_hop_nhat'), ngay=x.get('ngay_vbhn')))
            elif x['key'].startswith('TEN:') and x.get('vbhn_key') and tdan_ten.get(x['vbhn_key']) is not None and \
                    giai_vbhn(tdan_ten[x['vbhn_key']])[0] == 'Có trong hồ sơ':
                # PH-02 (quy tắc 02/11/2026): luật có VBHN – chỉ cần 01 VBHN khớp, không yêu cầu thêm toàn văn Luật gốc
                st, nguon = 'Có trong hồ sơ (qua VBHN %s – không yêu cầu Luật gốc)' % tdan_ten[x['vbhn_key']]['so'], giai_vbhn(tdan_ten[x['vbhn_key']])[1]
                canh_bao.append('%s: dùng Văn bản hợp nhất số %s (tệp %s) thay toàn văn Luật gốc theo quy tắc người phụ trách xác nhận ngày 02/11/2026 (chưa có văn bản). Giới hạn: VBHN là bản hợp nhất phục vụ tra cứu, sử dụng theo Pháp lệnh Hợp nhất VBQPPL; người rà soát ghi việc thay thế này ở I.7.' % (x['ten'], tdan_ten[x['vbhn_key']]['so'], nguon))
            elif x['key'].startswith('TEN:'):
                uv = ung_vien(x['key'])
                vbhn_lech = []
                if x.get('vbhn_key'):
                    # PH-02: luật được dẫn KÈM VBHN – tệp VBHN không khớp viện dẫn (khác số, khác ngày, cũ hơn) không được tính là toàn văn Luật gốc
                    vbhn_lech = [f for f in uv if f in vbhn_tt]
                    uv = [f for f in uv if f not in vbhn_tt]
                if uv:
                    st, nguon = 'Có trong hồ sơ', '; '.join(TEN[f] for f in uv)
                elif vbhn_lech:
                    st = 'THIẾU – chỉ có VBHN không khớp viện dẫn'
                    ly_do_rieng = 'Thiếu toàn văn %s (%sđoạn %d) – hồ sơ chỉ có văn bản hợp nhất không khớp viện dẫn (%s), không thay được Luật gốc; đề nghị cung cấp đúng VBHN được dẫn (quy tắc người phụ trách xác nhận 02/11/2026).' % (
                        x['ten'], ('tệp %s, ' % x['tep']) if x.get('tep') else '', x['doan'], '; '.join(TEN[f] for f in vbhn_lech))
                else:
                    ten = x['key'][4:]
                    vb = next((v for v in vbhn if isinstance(v, dict) and ND.chuan_ten_luat(v.get('luat', '')) == ten), None)
                    if vb and ung_vien(key_so(vb.get('vbhn', ''))):
                        st, nguon = 'Có trong hồ sơ (VBHN)', '; '.join(TEN[f] for f in ung_vien(key_so(vb.get('vbhn', ''))))
                    elif kho_chon(x['key']):
                        v = kho_chon(x['key'])[0]; ok_, ly_ = kho_toan_van(v)
                        if ok_: st, nguon = 'Có trong Kho Skill', v.get('file', '')
                    if st is None:
                        gan_giong = sorted({TEN[f] for k in hs_keys if k.startswith('TEN:') and (k[4:].startswith(ten + ' ') or ten.startswith(k[4:] + ' ')) for f in hs_keys[k]})
                        if gan_giong:
                            st = 'THIẾU – chỉ có luật tên gần giống'
                            ly_do_rieng = 'Thiếu toàn văn %s (%sđoạn %d) – hồ sơ chỉ có luật tên gần giống (%s), không thay thế được; đề nghị cung cấp đúng luật được dẫn.' % (
                                x['ten'], ('tệp %s, ' % x['tep']) if x.get('tep') else '', x['doan'], '; '.join(gan_giong))
            else:
                uv = ung_vien(x['key'])
                if len(uv) == 1:
                    st, nguon = 'Có trong hồ sơ', TEN[uv[0]]
                elif len(uv) > 1:
                    st, nguon = 'MƠ HỒ – nhiều tệp', '; '.join(TEN[f] for f in uv)
                    ly_do_rieng = 'Có %d tệp khác nội dung cùng mang định danh %s (%s) – không tự chọn tệp nào làm toàn văn; đề nghị giữ lại đúng một tệp.' % (len(uv), x['so'], '; '.join(TEN[f] for f in uv))
                elif kho_chon(x['key']):
                    v = kho_chon(x['key'])[0]; ok_, ly_ = kho_toan_van(v)
                    if ok_: st, nguon = 'Có trong Kho Skill', v.get('file', '')
                    else:
                        st = 'THIẾU – ' + ly_
                        ly_do_rieng = 'Thiếu toàn văn %s (%sđoạn %d): %s – đề nghị cung cấp bản .docx/.xlsx hoặc PDF có lớp chữ.' % (
                            x['loai'] + ' số ' + x['so'], ('tệp %s, ' % x['tep']) if x.get('tep') else '', x['doan'], ly_)
        if st and st.startswith('Có trong hồ sơ') and nguon and not ly_do_rieng:  # v4.6.1 (N12)
            tf_ = [byname_.get(n_) for n_ in nguon.split('; ')]
            if tf_ and all(f_ in khong_than for f_ in tf_):
                st = 'THIẾU – tệp chỉ có phần định danh'
                ly_do_rieng = 'Thiếu toàn văn %s (%sđoạn %d) – tệp %s chỉ có phần định danh (số, tên loại, trích yếu), không xác định được thân văn bản theo cấu trúc (%d ký tự ngoài phần định danh, trích yếu, căn cứ); đề nghị cung cấp toàn văn.' % (
                    x['ten'] or (x['loai'] + ' số ' + x['so']), ('tệp %s, ' % x['tep']) if x.get('tep') else '', x['doan'], ', '.join('“%s”' % n_ for n_ in nguon.split('; ')), max(khong_than[f_] for f_ in tf_))
                if vbhn_ghi and vbhn_ghi[-1].get('tep') == nguon: vbhn_ghi.pop()
        if ly_do_rieng and a.tac_vu == 'so-sanh':
            st = (st or '') + ' – không chặn (so sánh); đối chiếu ghi “Chưa kiểm”'
        elif ly_do_rieng:
            chan.append(ly_do_rieng)
        if st is not None: pass
        elif x['key'] in het:
            st, nguon = 'Đã bị thay thế – không cần toàn văn (CC-01)', 'thay bằng ' + het[x['key']].get('thay_bang', '')
        if st is None and a.tac_vu == 'so-sanh':
            # PB2-15 (quyết định của Hiệu trưởng 27/10/2026): so sánh chỉ cần đủ hai bản và phụ lục/văn bản kèm theo
            st = 'Chưa có – không chặn (so sánh); đối chiếu ghi “Chưa kiểm”'
        if st is None:
            st = 'THIẾU'
            chan.append('Thiếu toàn văn %s (%sđoạn %d: “%s…”) – đề nghị cung cấp bản .docx/.xlsx hoặc PDF có lớp chữ.' % (
                x['ten'] or (x['loai'] + ' số ' + x['so']), ('tệp %s, ' % x['tep']) if x.get('tep') else '', x['doan'], x['ngu_canh'][:70]))
        if x['key'] in het:
            if x.get('neu_thay_the'):  # v4.3 (TH-08): mọi lần nhắc đều là câu nêu việc thay thế → không phải viện dẫn sai
                canh_bao.append('%s được nhắc trong câu nêu việc văn bản này đã được thay thế/bãi bỏ (thay bằng %s) – không phải viện dẫn sai, không ghi CC-01.' % (x['so'] or x['ten'], het[x['key']].get('thay_bang', '')))
            else:
                canh_bao.append('%s đã được thay thế bởi %s – dự thảo vẫn viện dẫn/áp dụng; người rà soát xử lý theo mã CC-01 (Mức 1) của kiem_tra_the_thuc.py.' % (x['so'] or x['ten'], het[x['key']].get('thay_bang', '')))
        ket.append(dict(x, trang_thai=st, nguon=nguon))

    ok = not chan
    out = []
    out.append('# CỔNG HỒ SƠ – KIỂM KÊ TRƯỚC RÀ SOÁT (Skill %s)\n' % PHIEN_BAN)
    out.append('**KẾT LUẬN CỔNG: %s**\n' % ('ĐỦ ĐIỀU KIỆN RÀ SOÁT' if ok else 'CHẶN – CHƯA ĐỦ HỒ SƠ'))
    out.append('- Lần rà soát: %s' % vong_txt)
    out.append('- Tác vụ: %s' % {'ra-soat': 'rà soát', 'so-sanh': 'so sánh hai bản', 'chuan-hoa': 'chuẩn hóa văn phong'}[a.tac_vu])
    out.append('- Dự thảo: %s' % ('; '.join(TEN[x] for x in du_thao) if du_thao else '(không xác định)'))
    out.append('')
    out.append('## 1. Danh mục tệp nhận được\n')
    out.append('| # | Tệp | Định dạng | Vai trò | Tình trạng |')
    out.append('|---|---|---|---|---|')
    tenvt = {'du_thao': 'Bản dự thảo (so sánh)' if a.tac_vu == 'so-sanh' else 'Dự thảo hiện hành', 'du_thao_cu': 'Dự thảo lần trước', 'bao_cao_ra_soat': 'Báo cáo rà soát lần trước',
             'bc_tiep_thu': 'Báo cáo tiếp thu, giải trình', 'kem_theo': 'Phụ lục/văn bản kèm theo (tệp riêng)', 'lien_quan': 'Văn bản liên quan'}
    byname = {TEN[f]: f for f in docs}
    for i, (n, e, s) in enumerate(bang, 1):
        out.append('| %d | %s | %s | %s | %s |' % (i, n, e, tenvt.get(vt.get(byname.get(n, ''), ''), '—'), s))
    out.append('\n## 2. Văn bản được đề cập trong dự thảo\n')
    out.append('| # | Văn bản | Tệp | Đoạn | Căn cứ? | Tình trạng | Nguồn |')
    out.append('|---|---|---|---|---|---|---|')
    for i, x in enumerate(ket, 1):
        out.append('| %d | %s | %s | %d | %s | %s | %s |' % (i, x['ten'] or (x['loai'] + ' số ' + x['so']), x.get('tep', ''), x['doan'], 'có' if x['can_cu'] else '', x['trang_thai'], x['nguon']))
    if chan:
        out.append('\n## 3. Lý do chặn\n')
        out += ['%d. %s' % (i, c) for i, c in enumerate(chan, 1)]
        out.append('\n## 4. Thông báo gửi người dùng (dùng nguyên văn)\n')
        out.append('> Hồ sơ chưa đủ điều kiện rà soát theo chỉ đạo của Hiệu trưởng ngày 26/10/2026. Skill dừng tại bước kiểm kê hồ sơ và **không rà soát tạm**. Đề nghị bổ sung:')
        out += ['> - %s' % c for c in chan]
        out.append('> ')
        out.append('> Sau khi bổ sung, đề nghị gửi lại toàn bộ hồ sơ để rà soát.')
    if canh_bao:
        out.append('\n## %d. Ghi chú cho người rà soát\n' % (5 if chan else 3))
        out += ['- %s' % c for c in canh_bao]
    if a.json:
        sha = {}
        for f in docs:  # v4.3 (TH-11): mã băm từng tệp để tao_bao_cao.py kiểm kết quả đo thể thức thuộc đúng hồ sơ
            h = hashlib.sha256(); h.update(open(f, 'rb').read()); sha[TEN[f]] = h.hexdigest()
        kq_json = {'ket_luan': 'DU' if ok else 'CHAN', 'vong': vong, 'tac_vu': a.tac_vu, 'anh_can_xem': anh_xem, 'du_thao': du_thao[0] if du_thao else None,
                   'cac_ban_du_thao': [TEN[f] for f in du_thao], 'tep_kem_theo': {TEN[f]: list(v)[:2] for f, v in kem.items() if v},
                   'sha256': sha, 'xac_nhan_kem_thu_cong': xac_nhan_ghi, 'xac_nhan_toan_van_thu_cong': xac_nhan_tv_ghi, 'phien_ban': PHIEN_BAN,
                   'duong_dan': {TEN[f]: os.path.abspath(f) for f in docs}, 'kho': os.path.abspath(kho_path), 'vbhn_thay_luat_goc': vbhn_ghi,
                   'tep': bang, 'vai_tro': {TEN[k]: v for k, v in vt.items()}, 'van_ban_de_cap': ket,
                   'dinh_danh': {TEN[f]: sorted(k for k, fs in hs_keys.items() if f in fs) for f in docs if any(f in fs for fs in hs_keys.values())},  # v4.6.1 (N20): trình dựng gắn trích dẫn với tệp
                   'gop_trung_noi_dung': gop_ghi, 'tham_so': THAM_SO,
                   'ly_do_chan': chan, 'ghi_chu': canh_bao}
        def _ghi(tam):
            with open(tam, 'w', encoding='utf-8') as f_: json.dump(kq_json, f_, ensure_ascii=False, indent=1)
        e_ = ND.ghi_tep_an_toan(a.json, _ghi)  # v4.6.3: ghi qua tệp tạm – lỗi ghi không để lại JSON dở dang, không Traceback
        if e_:
            print('\n'.join(out)); print('LỖI GHI KẾT QUẢ: %s – kết quả cổng KHÔNG được ghi; không dùng JSON cũ, chạy lại cổng.' % e_); sys.exit(2)
    print('\n'.join(out))
    sys.exit(0 if ok else 2)


if __name__ == '__main__':
    main()
