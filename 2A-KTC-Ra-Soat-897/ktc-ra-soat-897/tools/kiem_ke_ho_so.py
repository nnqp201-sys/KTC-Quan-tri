#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kiem_ke_ho_so.py – CỔNG HỒ SƠ (bước 0) của Skill ktc-ra-soat-897 v4.5

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
import sys, os, re, json, zipfile, subprocess, argparse, unicodedata, hashlib
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
    """Canh lề của từng đoạn thân văn bản, cùng thứ tự với docx_paras (v4.5 – PB5-WORK-10)."""
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    out = []
    for p in root.iter(W + 'p'):
        jc = p.find(W + 'pPr/' + W + 'jc')
        out.append(jc.get(W + 'val') if jc is not None else None)
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
    with zipfile.ZipFile(path) as z:
        names = [n for n in z.namelist() if n.startswith('xl/sharedStrings') or n.startswith('xl/worksheets/sheet')]
        txt = []
        for n in names:
            root = ET.fromstring(z.read(n))
            txt += [x.text or '' for x in root.iter() if x.tag.endswith('}t') or x.tag.endswith('}v')]
    return [norm(' '.join(txt))]


def pdf_info(path):
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
KEM_TITLE = re.compile(r'^(QUY ĐỊNH|QUY CHẾ|ĐIỀU LỆ|NỘI QUY|KẾ HOẠCH|DANH MỤC|CHƯƠNG TRÌNH|ĐỀ ÁN|HƯỚNG DẪN|QUY TRÌNH)(?:\s+[^a-zà-ỹđ]*)?$')
KEM_LOAI = r'(Quy định|Quy chế|Điều lệ|Nội quy|Kế hoạch|Danh mục|Chương trình|Đề án|Hướng dẫn|Quy trình)'
LUON_KEM = ('QUY ĐỊNH', 'QUY CHẾ', 'ĐIỀU LỆ', 'NỘI QUY', 'DANH MỤC', 'QUY TRÌNH')  # các tên loại chỉ ban hành kèm theo văn bản khác
STOP_TY = set('của và các về việc trong tại theo đối với cho trường cao đẳng kon tum này năm được là thuộc ban hành'.split())


def loai_kem(title):
    m = KEM_TITLE.match(title or '')
    return m.group(1) if m else None


def tu_trich(s_):
    return {w for w in re.findall(r'\w+', nfc(s_).lower()) if w not in STOP_TY and not w.isdigit()}


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
        if lk: out.append((lk, (P[i][len(lk):] + ' ' + trich_sau(P, i)).strip()))
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
        if KEM_TITLE.match(p): return ('kem_theo', p, (p[len(loai_kem(p)):] + ' ' + trich_sau(dau, i)).strip())
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


def trich_dan(paras):
    """Trả về danh sách văn bản được đề cập: {'loai','so','ten','doan','ngu_canh','can_cu'}"""
    out, seen = [], set()
    idx = {}
    def da_co(k, t, m):
        """đã ghi khóa k: cập nhật cờ “chỉ nêu việc thay thế” (mọi lần nhắc đều là câu thay thế mới giữ True)."""
        if k in idx and not la_cau_thay_the(t, m.start(), m.end()): out[idx[k]]['neu_thay_the'] = False
        return k in seen
    def them(k, d, t, m):
        seen.add(k); idx[k] = len(out); d['neu_thay_the'] = la_cau_thay_the(t, m.start(), m.end()); out.append(d)
    for i, t in enumerate(paras):
        if not t: continue
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
        cands += [m for m in re.finditer(r'\b(Bộ luật|Luật|Pháp lệnh)\s+((?:[A-ZĐÀ-Ỹ][^\s;,.()]*)(?:\s+(?!ngày|số\s*:?\s*\d|năm|đã|được|sửa|và|của|các|hiện)[^\s;,.()]+){0,9}?)(?=\s+(?:ngày|số\s*:?\s*\d|năm|đã|được|sửa đổi|và|của|hiện hành|mới nhất|quy định|tại|theo)|[;,.()]|$)', t) if not any(a <= m.start() < b for a, b in spans)]
        for m in cands:
            ten = norm(m.group(1) + ' ' + m.group(2))
            cat = re.split(r'\s+(?:và|hoặc|,)\s+(?=(?:Nghị định|Thông tư|Quyết định|Luật|Bộ luật|Pháp lệnh|Nghị quyết|Chỉ thị|Thông báo)\b)', ten)
            bi_cat = len(cat) > 1
            ten = norm(cat[0])
            if re.match(r'^(Luật|Bộ luật|Pháp lệnh) (này|số)\b', ten): continue
            if len(ten.split()) < 2: continue
            k = 'TEN:' + ten.upper()
            if da_co(k, t, m) or any(x.startswith('TEN:') and k.startswith(x + ' ') for x in seen): continue
            if len(ten.split()) > 12: continue
            # đã có số hiệu ngay sau tên thì bỏ (đã bắt ở trên)
            after = t[m.end():m.end() + 25]
            if not bi_cat and re.match(r'\s*số\s*\d', after): continue
            them(k, {'loai': m.group(1), 'so': None, 'key': k, 'ten': ten, 'doan': i + 1,
                     'ngu_canh': t[max(0, m.start() - 10):m.end() + 60], 'can_cu': is_cc}, t, m)
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
    for p in paras[:60]:
        m = re.search(r'ngày\s+(\d{1,2})\s+tháng\s+(\d{1,2})\s+năm\s+(\d{4})', p)
        if m: return (int(m.group(3)), int(m.group(2)), int(m.group(1)))
    return None


def ma_dinh_danh(name, paras):
    """Các khoá nhận diện một tệp được cung cấp: số hiệu + tên luật."""
    keys = set()
    head = paras[:80]
    for p in head[:40]:
        if len(p) > 90: continue
        m = re.match(r'^(?:Số|Luật số|Bộ luật số|Pháp lệnh số|Số hiệu)\s*[:]?\s*' + SO, p)
        if m: keys.add(key_so(m.group(1)))
    fn = nfc(os.path.splitext(name)[0])
    for m in re.finditer(r'(\d{1,5})[_\-](\d{4})[_\-]([A-ZĐ]{2,}[A-Z0-9Đ\-]*)', fn):
        a, b, c = m.groups()
        c = c.replace('ND', 'NĐ').replace('_', '-')
        keys.add(key_so('%s/%s/%s' % (a, b, c)))
    for m in re.finditer(r'(\d{1,5})[_\-](VBHN)[_\-]([A-Z]+)', fn):
        keys.add(key_so('%s/VBHN-%s' % (m.group(1), m.group(3))))
    # tiêu đề luật: "LUẬT" + dòng in hoa kế tiếp
    for i, p in enumerate(head):
        if p in ('LUẬT', 'BỘ LUẬT', 'PHÁP LỆNH') and i + 1 < len(head):
            keys.add('TEN:' + (p + ' ' + head[i + 1]).upper())
        m = re.match(r'^(LUẬT|BỘ LUẬT|PHÁP LỆNH)\s+([A-ZĐÀ-Ỹ ,]+)$', p)
        if m: keys.add('TEN:' + norm(p).upper())
    return keys


# ---------------------------------------------------------------- chính
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('duong_dan', nargs='+')
    ap.add_argument('--tac-vu', default='ra-soat', choices=['ra-soat', 'so-sanh', 'chuan-hoa'],
                    help='ra-soat: rà soát chính thức/nhanh (G1–G8); so-sanh: so sánh hai bản (G1–G5, không áp G6–G8); chuan-hoa: chỉ G1–G3')
    ap.add_argument('--vong', default='auto')
    ap.add_argument('--vai-tro', action='append', default=[], metavar='TÊN_TỆP=VAI_TRÒ',
                    help='chỉ định vai trò tệp: du_thao | du_thao_cu | bao_cao_ra_soat | bc_tiep_thu | kem_theo | lien_quan (PB2-03, TH-02)')
    ap.add_argument('--xac-nhan-kem', action='append', default=[], metavar='TÊN_TỆP=LÝ_DO',
                    help='v4.5 (quyết định F1): người rà soát xác nhận tệp là văn bản kèm theo của dự thảo khi trích yếu không khớp/không có (cùng tên loại); lý do ≥ 20 ký tự; ghi vào kết quả cổng và báo cáo I.7')
    ap.add_argument('--xuat-anh', default=None, help='thư mục lưu ảnh lớn trong tệp Word để người rà soát mở xem (PB2-07)')
    ap.add_argument('--du-thao', default=None)
    ap.add_argument('--kho', default=KHO_DEFAULT)
    ap.add_argument('--json', default=None)
    a = ap.parse_args()

    files = []
    for d in a.duong_dan:
        if os.path.isdir(d):
            for r, _, fs in os.walk(d):
                for f in sorted(fs): files.append(os.path.join(r, f))
        elif os.path.exists(d):
            files.append(d)
    chan, canh_bao, bang, anh_xem = [], [], [], []
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
    for chi_dinh in a.vai_tro:
        ten_, _, vai_ = chi_dinh.partition('=')
        for f in docs:
            if (TEN[f] == ten_.strip() or (os.path.basename(f) == ten_.strip() and _dem[os.path.basename(f)] == 1)) and vai_.strip() in ('du_thao', 'du_thao_cu', 'bao_cao_ra_soat', 'bc_tiep_thu', 'kem_theo', 'lien_quan'):
                vt[f] = vai_.strip(); canh_bao.append('Vai trò “%s” của tệp “%s” do người rà soát chỉ định (--vai-tro).' % (vai_.strip(), ten_.strip()))
                if vai_.strip() == 'kem_theo': kem[f] = tieu_de_kem(docs[f]) or ('kem_theo', '(không có tiêu đề tên loại)', '')  # v4.5: chỉ sửa vai trò, vẫn kiểm khớp
                if vai_.strip() != 'kem_theo': kem.pop(f, None)
    if a.du_thao:
        for f in docs:
            if os.path.abspath(f) == os.path.abspath(a.du_thao) or TEN[f] == a.du_thao:
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
            m = re.findall(r'(?:^|[\s_\-(.])(?:V|LAN|LẦN|BAN|BẢN)\s*(\d+)(?![\d/])', nfc(os.path.splitext(os.path.basename(f))[0]).upper())
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
        vong = 2 if (co_bc_rs or co_cu or any(re.search(r'SUA\s*LAN|SAU\s*TRINH|LAN\s*[2-9]', nfc(os.path.basename(f)).upper()) for f in du_thao)) else 1
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
        so_ban_than = {key_so(m.group(1)) for f in du_thao for p in docs[f][:40] for m in [re.match(r'^Số\s*:\s*' + SO, p)] if m}
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
            g = next((g for g in kem if TEN[g] == ten_.strip() or (os.path.basename(g) == ten_.strip() and _dem[os.path.basename(g)] == 1)), None)
            if g is None:
                chan.append('--xac-nhan-kem: không có tệp văn bản kèm theo tên “%s” trong hồ sơ.' % ten_.strip())
            elif len(ly_.strip()) < 20:
                chan.append('--xac-nhan-kem “%s”: phải ghi lý do cụ thể (≥ 20 ký tự) vì sao tệp này là văn bản kèm theo của dự thảo.' % ten_.strip())
            else:
                xac_nhan[g] = ly_.strip()
        kem_tep = [(g, v) for g, v in kem.items() if v and v[0] == 'kem_theo']
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
            ung = [('trong', None, l2, t2) for l2, t2 in kem_trong(P)] + [('tep', g, loai_kem(v[1]), v[2] if len(v) > 2 else '') for g, v in kem_tep]
            cap = sorted(((diem_trich(ty, t2), ci, ui) for ci, (lk, ty) in enumerate(can_) for ui, (_, g, l2, t2) in enumerate(ung) if l2 == lk and diem_trich(ty, t2) > 0), reverse=True)
            gan, dung = {}, set()
            for sc, ci, ui in cap:
                if ci in gan or ui in dung: continue
                gan[ci] = ui; dung.add(ui)
            for ci, (lk, ty) in enumerate(can_):
                if ci in gan: continue
                mo_ta = '%s %s' % (lk.capitalize(), ty.strip()) if ty.strip() else lk.capitalize()
                xn_ = next((ui for ui, (k_, g, l2, t2) in enumerate(ung) if k_ == 'tep' and ui not in dung and l2 == lk and g in xac_nhan), None)
                if xn_ is not None:
                    dung.add(xn_); g = ung[xn_][1]
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
    kho = json.load(open(a.kho, encoding='utf-8')) if os.path.exists(a.kho) else {'van_ban': []}
    kho_keys = {}
    for v in kho.get('van_ban', []):
        for k in [v.get('so_hieu', '')] + v.get('tu_khoa', []):
            m = re.search(SO, k or '')
            if m: kho_keys[key_so(m.group(1))] = v
        if v.get('so_hieu', '').upper().startswith(('LUẬT', 'PHÁP LỆNH')):
            kho_keys['TEN:' + v['so_hieu'].upper()] = v
        if v.get('ten_luat'):
            kho_keys['TEN:' + nfc(v['ten_luat']).upper()] = v
    het = {key_so(x.get('so_hieu', '')): x for x in kho.get('van_ban_het_hieu_luc_hay_gap', []) if isinstance(x, dict)}
    vbhn = kho.get('van_ban_hop_nhat_da_biet', [])
    hs_keys = {}
    for f, pp in docs.items():
        if vt[f] in ('du_thao', 'du_thao_cu', 'bao_cao_ra_soat', 'bc_tiep_thu'): continue
        for k in ma_dinh_danh(os.path.basename(f), pp): hs_keys.setdefault(k, f)
    ket, da_giai = [], set()
    for x in tdan:
        st, nguon = None, ''
        if x.get('rut_gon'):  # “Nghị định 13/2023” → khóa đầy đủ “13/2023/NĐ-CP” nếu biết
            for bang_k in (hs_keys, kho_keys, het):  # v4.5 (PB5-WORK-01): chỉ nhận văn bản CÙNG LOẠI
                full = next((k for k in bang_k if k.startswith(key_so(x['so']) + '/') and cung_loai(k, x['loai'])), None)
                if full: x = dict(x, key=full); break
        if x.get('chi_so'):  # v4.3 (TH-03): “NĐ 356” → khớp DUY NHẤT một văn bản cùng loại, cùng số trong hồ sơ/Kho
            ung = sorted({k for bang_k in (hs_keys, kho_keys, het) for k in bang_k
                          if not k.startswith('TEN:') and (k.startswith(x['so'] + '/') or k.startswith(x['so'] + '-')) and any(h in k for h in HAU_TO.get(x['loai'], ()))})
            if len(ung) == 1:
                x = dict(x, key=ung[0], so=ung[0])
            else:
                st = 'Chưa xác định – viện dẫn chỉ có số (%s)' % ('trùng %d văn bản' % len(ung) if ung else 'không có trong hồ sơ, Kho')
        if x['key'] in da_giai: continue
        da_giai.add(x['key'])
        if st and a.tac_vu == 'so-sanh':
            st += ' – không chặn (so sánh); đối chiếu ghi “Chưa kiểm”'
        elif st:
            chan.append('Viện dẫn “%s %s” (tệp %s, đoạn %d: “%s…”) chỉ có số, không xác định được văn bản – đề nghị ghi đủ số, ký hiệu và cung cấp toàn văn.' % (
                x['loai'], x['so'], x.get('tep', ''), x['doan'], x['ngu_canh'][:70]))
        if x['key'] in hs_keys:
            st, nguon = 'Có trong hồ sơ', TEN[hs_keys[x['key']]]
        elif x['key'] in kho_keys:
            st, nguon = 'Có trong Kho Skill', kho_keys[x['key']].get('file', '')
        elif x['key'].startswith('TEN:'):
            ten = x['key'][4:]
            hit = next((k for k in hs_keys if k.startswith('TEN:') and (k[4:] == ten or k[4:].startswith(ten + ' ') or ten.startswith(k[4:]))), None)
            if hit: st, nguon = 'Có trong hồ sơ', TEN[hs_keys[hit]]
            else:
                vb = next((v for v in vbhn if isinstance(v, dict) and nfc(v.get('luat', '')).upper() == ten), None)
                if vb:
                    k2 = key_so(vb.get('vbhn', ''))
                    if k2 in hs_keys: st, nguon = 'Có trong hồ sơ (VBHN)', TEN[hs_keys[k2]]
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
    out.append('# CỔNG HỒ SƠ – KIỂM KÊ TRƯỚC RÀ SOÁT (Skill ktc-ra-soat-897 v4.5)\n')
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
    print('\n'.join(out))
    if a.json:
        sha = {}
        for f in docs:  # v4.3 (TH-11): mã băm từng tệp để tao_bao_cao.py kiểm kết quả đo thể thức thuộc đúng hồ sơ
            h = hashlib.sha256(); h.update(open(f, 'rb').read()); sha[TEN[f]] = h.hexdigest()
        json.dump({'ket_luan': 'DU' if ok else 'CHAN', 'vong': vong, 'tac_vu': a.tac_vu, 'anh_can_xem': anh_xem, 'du_thao': du_thao[0] if du_thao else None,
                   'cac_ban_du_thao': [TEN[f] for f in du_thao], 'tep_kem_theo': {TEN[f]: list(v)[:2] for f, v in kem.items() if v},
                   'sha256': sha, 'xac_nhan_kem_thu_cong': xac_nhan_ghi, 'phien_ban': 'ktc-ra-soat-897 v4.5',
                   'tep': bang, 'vai_tro': {TEN[k]: v for k, v in vt.items()}, 'van_ban_de_cap': ket,
                   'ly_do_chan': chan, 'ghi_chu': canh_bao}, open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sys.exit(0 if ok else 2)


if __name__ == '__main__':
    main()
