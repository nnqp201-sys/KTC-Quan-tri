#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tao_bao_cao.py – Dựng báo cáo rà soát .docx theo khuôn cố định (Skill ktc-ra-soat-897 v4.6)

Người rà soát (AI) chỉ điền DỮ LIỆU (tệp JSON); script:
  * nhập nguyên kết quả đo thể thức của kiem_tra_the_thuc.py (không cho sửa mức),
  * nhập kết quả cổng hồ sơ của kiem_ke_ho_so.py (từ chối dựng nếu cổng CHẶN),
  * kiểm tính hợp lệ (mã, mức, bằng chứng hai phía, 6 giá trị ma trận…),
  * TỰ TÍNH Bảng 1, Bảng 2, mức độ tuân thủ và NHÃN KẾT LUẬN theo
    references/Quy-Tac-KTC/02-Quy-Tac-Xep-Muc.md,
  * dựng .docx với cấu trúc, định dạng cố định.

Cách dùng:
  python3 tao_bao_cao.py du_lieu.json --cong cong.json --the-thuc tt.json [--the-thuc tt2.json] -o bao_cao.docx
  python3 tao_bao_cao.py du_lieu.json ... --chi-kiem      (chỉ kiểm hợp lệ, không dựng tệp)
Mẫu dữ liệu: assets/Mau-Du-Lieu-Bao-Cao.json
"""
import sys, os, json, re, argparse, datetime, unicodedata, hashlib, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # v4.6.4: không ghi __pycache__ vào thư mục Skill
import nhan_dien_chung as ND  # v4.6: đối chiếu trích dẫn, chuẩn hóa dùng chung
import kiem_ke_ho_so as KK  # v4.6.1: cùng quy tắc khóa số hiệu với cổng (gắn trích dẫn với văn bản nguồn)
import kiem_kieu_du_lieu as KD  # v4.6.2 (F01, F02): hợp đồng kiểu dữ liệu, kiểm trước mọi xử lý
import subprocess, tempfile, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

PHIEN_BAN = 'ktc-ra-soat-897 v4.6.4 (03/11/2026 – bản hoàn thiện sau nghiệm thu độc lập lần 3 và quyết định Q1–Q5 của người phụ trách, đã tự kiểm của người sửa, Hiệu trưởng phê duyệt chính thức ngày 03/11/2026)'
PHIEN_BAN_DU_LIEU = 'ktc-ra-soat-897 v4.6.4'
_nd = ND.noi_dung  # v4.6.3 (mục 5): nội dung sau chuẩn hóa khoảng trắng (bỏ zero-width, mọi khoảng trắng Unicode)  # kết quả cổng/đo phải cùng phiên bản (KTS-24)
TRANG_THAI = 'BẢN NHÁP RÀ SOÁT – CHƯA ĐƯỢC PHÊ DUYỆT CHÍNH THỨC'

# ---- mức cho phép theo mã (02-Quy-Tac-Xep-Muc.md mục 2) ----
MUC_CHO_PHEP = {
    'TT-34': {2, 3}, 'TB-01': {3}, 'TB-02': {4}, 'TB-03': {3},
    'TD-01': {2}, 'TD-02': {2}, 'TD-05': {2}, 'TD-06': {2}, 'TD-03': {3}, 'TD-04': {3}, 'TD-07': {3},
    'CC-01': {1}, 'CC-02': {2}, 'CC-03': {1}, 'CC-04': {1}, 'CC-05': {1, 2}, 'CC-06': {2},
    'TQ-01': {1}, 'TQ-02': {2},
    # v4.6 (KTS-18 – quyết định của người phụ trách 02/11/2026): DC-02 được Mức 1 khi trái pháp luật/văn bản cấp trên, như DC-01, DC-03
    'DC-01': {1, 2}, 'DC-02': {1, 2}, 'DC-03': {1, 2}, 'DC-04': {2}, 'DC-05': {2}, 'DC-06': {2},
    'ND-01': {1, 2}, 'ND-02': {1}, 'ND-03': {2},
    'VP-01': {2, 3}, 'GY-01': {4}, 'DG-01': {2}, 'DG-02': {2},
}
# mã TT, TB, TD, CC do script đo (bảng 01, 02) – chỉ các mã này được nhập từ script hoặc thêm tay có lý do
MA_SCRIPT = {'TT-%02d' % k for k in list(range(1, 5)) + list(range(10, 25)) + list(range(30, 47)) + [50, 51]} | \
            {'TB-01', 'TB-02', 'TB-03', 'TD-01', 'TD-02', 'TD-03', 'TD-04', 'TD-05', 'CC-01', 'CC-02', 'CC-06'}
NHOM = {'TT': 'Thể thức', 'TB': 'Thể thức', 'TD': 'Thể thức', 'DG': 'Thể thức',
        'CC': 'Nội dung', 'TQ': 'Nội dung', 'DC': 'Nội dung', 'ND': 'Nội dung',
        'VP': 'Chất lượng soạn thảo', 'GY': 'Chất lượng soạn thảo'}
NHOM_LIST = ['Thể thức', 'Nội dung', 'Điều khoản bắt buộc', 'Chất lượng soạn thảo']
MA_TRAN_GT = ['Khớp', 'Mâu thuẫn', 'Hẹp hơn', 'Rộng hơn', 'Văn bản liên quan không quy định', 'Chưa kiểm']
TRANG_THAI_DC = ['Đã sửa đạt', 'Sửa một phần', 'Chưa sửa', 'Không tiếp thu – có giải trình', 'Không còn áp dụng',
                 'Kiến nghị lần trước không còn phù hợp']  # PB-09
NGOAC = re.compile(r'[“"«].+[”"»]', re.S)
NGOAC2 = re.compile(r'[“"«][^”"»]+[”"»]')
TRONG_YEU = ['thẩm quyền', 'thời hạn', 'điều cấm', 'cho phép', 'đối tượng', 'hiệu lực']
TEN_MUC = {1: 'Mức 1 – Bắt buộc sửa', 2: 'Mức 2 – Cần sửa', 3: 'Mức 3 – Nên sửa', 4: 'Mức 4 – Góp ý nâng cao'}


def muc_so(v):
    """v4.6 (KTS-20): chỉ nhận đúng giá trị 1–4 (số nguyên hoặc “Mức n”); “Mức 12”, chuỗi lạ → None (bị từ chối)."""
    if isinstance(v, bool): return None
    if isinstance(v, int): return v if v in (1, 2, 3, 4) else None
    m = re.fullmatch(r'\s*(?:mức\s*)?([1-4])\s*', str(v or ''), re.I)
    return int(m.group(1)) if m else None


def nhom_cua(ma):
    if ma == 'ND-02': return 'Điều khoản bắt buộc'
    return NHOM.get(ma.split('-')[0], 'Nội dung')


TEP_IDS = []  # tên tệp dự thảo/văn bản kèm theo theo cổng hồ sơ – đặt trong kiem() (v4.5, PB5-WORK-14)


def tep_cua(v):
    t = unicodedata.normalize('NFC', v or '')
    hit = [x for x in TEP_IDS if x and x in t]
    return max(hit, key=len) if hit else None


CAP_VT = ('pl', 'chuong', 'muc', 'dieu', 'khoan', 'diem', 'doan')
NEO_VT = ('pl', 'chuong', 'muc', 'dieu', 'doan')


def norm_vt(v):
    """v4.6 (KTS-19): địa chỉ CẤU TRÚC của vị trí – {tệp, phần văn bản, phụ lục, chương, mục, điều, khoản, điểm, đoạn}.
    “Quy định, Điều 7 khoản 2” và “Điều 7, khoản 2 Quy định” là một vị trí (PB2-12); vị trí ghi tên tệp thì tệp là một phần của vị trí."""
    tp = tep_cua(v)
    t = unicodedata.normalize('NFC', (v or '').replace(tp, ' ') if tp else (v or '')).lower()
    dc = {}
    if tp: dc['tep'] = tp
    for pat, ten in ((r'phụ lục\s*([ivxlc]+|\d+)\b', 'pl'), (r'chương\s*([ivxlc]+|\d+)\b', 'chuong'), (r'(?<!tiểu )mục\s*(\d+|[ivxlc]+)\b', 'muc'),
                     (r'điều\s*(\d+)', 'dieu'), (r'khoản\s*(\d+)', 'khoan'), (r'điểm\s*([a-zđ])\b', 'diem'), (r'đoạn\s*(\d+)', 'doan')):
        m = re.search(pat, t)
        if m: dc[ten] = m.group(1)
    phan = [x for x in ('quy định', 'quy chế', 'quyết định', 'kế hoạch', 'điều lệ', 'nội quy') if x in t]
    if phan: dc['phan'] = frozenset(phan)
    if not any(k in dc for k in CAP_VT): return re.sub(r'\s+', ' ', t.strip())
    return dc


def trung_vt(a, b):
    """v4.6 (KTS-19): hai vị trí trùng hoặc cha – con khi mọi cấp cùng có đều bằng nhau VÀ có chung ít nhất một cấp neo
    (phụ lục, chương, mục, điều, đoạn). “Chương I khoản 1” ≠ “Chương II khoản 1”; “Điều 7” chứa “Điều 7 khoản 2”."""
    if isinstance(a, dict) and isinstance(b, dict):
        if a.get('tep') and b.get('tep') and a['tep'] != b['tep']: return False
        if a.get('phan') and b.get('phan') and not (a['phan'] & b['phan']): return False
        chung = [k for k in CAP_VT if k in a and k in b]
        if any(a[k] != b[k] for k in chung): return False
        return any(k in NEO_VT for k in chung)
    return a == b


def chuan_nv(s_):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s_ or '').replace('…', ' ').strip(' “”"«».')).strip().lower()


TRAI = [('cấm', 'cho phép'), ('cấm', 'được phép'), ('bắt buộc', 'khuyến khích'), ('tối đa', 'tối thiểu'), ('tăng', 'giảm')]
DV_TG = ('giờ', 'ngày', 'tuần', 'tháng', 'quý', 'năm', 'phút')
SO_CHU = {'một': 1, 'hai': 2, 'ba': 3, 'bốn': 4, 'tư': 4, 'năm': 5, 'sáu': 6, 'bảy': 7, 'tám': 8, 'chín': 9, 'mười': 10, 'mươi': 10}
NEG_RE = r'(?<!\w)(không|chưa|chẳng|cấm|thiếu)(?!\w)'


def dau_hieu(s_):
    """v4.5: chữ ký so sánh của một phía – (i) dãy (số, đơn vị) THEO THỨ TỰ, bỏ số dẫn Điều/khoản/điểm/Chương/Mục/Phụ lục/số hiệu và năm;
    số viết bằng chữ (“năm ngày”) được đổi ra số; (ii) dãy phủ định theo từng vế (tách ở dấu phẩy, chấm phẩy, “và”, “nhưng”, “còn”)."""
    t = chuan_nv(s_)
    so = []
    for m in re.finditer(r'(?<![\w/])(\d+(?:[.,]\d+)?|' + '|'.join(SO_CHU) + r')\s*(' + '|'.join(DV_TG) + r')?(?!\w)', t):
        truoc = t[max(0, m.start() - 12):m.start()]
        if re.search(r'(điều|khoản|điểm|chương|mục|phụ lục|số|năm|lần|ngày)\s*$', truoc) and not m.group(2): continue
        v = m.group(1)
        if v in SO_CHU:
            if not m.group(2): continue  # chữ số chỉ tính khi đi kèm đơn vị (“năm ngày”), tránh nhầm “năm” (năm học)
            v = str(SO_CHU[v])
        so.append((str(int(float(v.replace(',', '.')))) if re.match(r'^\d+([.,]0+)?$', v) else v, m.group(2) or ''))
    ve = [x for x in re.split(r',|;|(?<!\w)(?:và|nhưng|còn|song)(?!\w)', t) if x.strip()]
    pd = [bool(re.search(NEG_RE, x)) for x in ve]
    return so, pd


def trai_nghia(a_, b_):
    """v4.4 (PB4-GPT-07), v4.5 (PB5-GPT-03, PB5-WORK-15): dấu hiệu hai phía không khớp. Trả về mô tả hoặc ''."""
    sa, pa = dau_hieu(a_); sb, pb = dau_hieu(b_)
    if (sa or sb) and sa != sb:
        return 'khác số liệu/đơn vị theo thứ tự (%s / %s)' % (', '.join(' '.join(x).strip() for x in sa) or 'không có', ', '.join(' '.join(x).strip() for x in sb) or 'không có')
    if len(pa) == len(pb) and pa != pb: return 'khác phủ định theo từng vế'
    if len(pa) != len(pb) and sum(pa) != sum(pb): return 'khác số vế phủ định'
    A, B = chuan_nv(a_), chuan_nv(b_)
    def co(s_, w_): return re.search(r'(?<!\w)' + w_ + r'(?!\w)', s_) is not None
    for x, y in TRAI:
        if (co(A, x) and co(B, y) and not co(B, x)) or (co(A, y) and co(B, x) and not co(A, x)):
            return 'trái nghĩa (“%s” / “%s”)' % (x, y)
    return ''


GIAI_TRINH = []


DOI_CHIEU = {'so_trich': 0, 'kho_dir': None}


DOI_CHIEU['chua_kiem_dieu'] = []


def kho_van_ban(cong):
    """v4.6.1 (N20, N21): bản chữ THEO TỪNG NGUỒN để gắn mỗi trích dẫn với đúng văn bản được dẫn (không gộp mọi nguồn thành một chuỗi).
    → (DT: [(nhãn, chữ)] tệp dự thảo + văn bản kèm theo; HS: {tên tệp: chữ} tệp khác của hồ sơ; KHO: [(khóa số hiệu/tên luật, nhãn, chữ)];
       QT: [(nhãn, chữ)] quy tắc của Skill (references/**/*.md); thiếu: tệp không đọc lại được). v4.6.2: mục Kho thêm khóa chính."""
    dt, hs, thieu = [], {}, []
    vt = cong.get('vai_tro', {})
    for ten, duong in (cong.get('duong_dan') or {}).items():
        t = ND.doc_chu(duong) if os.path.exists(duong) else None
        if t is None: thieu.append(ten); continue
        if vt.get(ten) in ('du_thao', 'kem_theo'): dt.append((ten, t))
        elif vt.get(ten) == 'lien_quan': hs[ten] = t
    kho = []
    kp = cong.get('kho') or KK.KHO_DEFAULT
    if os.path.exists(kp):
        kd = os.path.dirname(os.path.abspath(kp))
        for v in json.load(open(kp, encoding='utf-8')).get('van_ban', []):
            f_ = os.path.join(kd, v.get('file', ''))
            md = os.path.join(kd, 'text', os.path.splitext(os.path.basename(v.get('file', '')))[0] + '.md')
            t = ND.doc_chu(md) if os.path.exists(md) else (ND.doc_chu(f_) if v.get('file') and os.path.exists(f_) else None)
            if not t: continue
            k = set()
            for x in [v.get('so_hieu', '')] + list(v.get('tu_khoa', [])):
                k |= khoa_so(x)
            for x in (v.get('ten_luat'), v.get('so_hieu') if (v.get('so_hieu') or '').upper().startswith(('LUẬT', 'PHÁP LỆNH', 'BỘ LUẬT')) else None):
                if x: k.add('TEN:' + ND.chuan_ten_luat(x))
            kho.append((k, 'Kho: %s' % v.get('so_hieu', v.get('file')), t, khoa_so(v.get('so_hieu', ''))))  # v4.6.2: khóa chính để ưu tiên như cổng
    qt = []
    goc = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references')
    for f in glob.glob(os.path.join(goc, '**', '*.md'), recursive=True):
        if 'Lich-Su-Khong-Ap-Dung' in f or 'Kho-Du-Lieu' in f: continue
        t = ND.doc_chu(f)
        if t: qt.append((os.path.relpath(f, goc), t))
    return dt, hs, kho, qt, thieu


def khoa_so(s_):
    """Các khóa số hiệu (cùng quy tắc cổng) trong một chuỗi; bỏ chuỗi chỉ là ngày (16/10/2026)."""
    out = set()
    for m in re.finditer(KK.SO, ND.chuan_so_hieu(s_ or '')):
        k = KK.key_so(m.group(1))
        if re.search(r'[A-Za-zĐđ]', k): out.add(k)
    return out


# v4.6.2: bỏ _MAU_QT, dieu_cua(), vung_dieu() của v4.6.1 (tìm câu trên MỌI tệp quy tắc; chỉ lấy Điều đầu tiên; gộp mọi Điều cùng số) –
# thay bằng nguon_cua() một nguồn, chi_dinh_vi_tri(), phan_van_ban(), vung_vi_tri() (F03, F04, F09, F10).


_TU_SAU_TEN_LUAT = {'SO', 'NGAY', 'NAM', 'DIEU', 'KHOAN', 'DIEM', 'CHUONG', 'MUC', 'PHAN', 'PHU', 'VA', 'HOAC', 'HOP', 'VBHN', 'VAN', 'TAI',
                    'THEO', 'DA', 'DUOC', 'SUA', 'HIEN'}  # v4.6.3: chữ được phép đứng ngay sau tên luật trong dòng dẫn


KHOA_GHI_CHU = re.compile(r'^_(?:huong_dan|ghi_chu|vi_du\w*)$')  # khóa chú thích của mẫu dữ liệu – được phép, không có tác dụng


def khoa_danh_rieng(x, duong='dữ liệu'):
    """v4.6.1 (N25): khóa bắt đầu “_” (ví dụ _nguon, _ss, _id) dành cho script – dữ liệu người nhập không được đặt (đặt “_nguon”: “script”
    từng làm phát hiện tự miễn kiểm trích dẫn). Chỉ cho phép khóa chú thích _huong_dan, _ghi_chu, _vi_du_….  → danh sách lỗi.
    v4.6.2 (F06): kiểm ở MỌI cấp, kể cả bên trong giá trị của khóa chú thích. Nghiệm thu chỉ thấy khóa lọt; chưa chứng minh khóa lọt
    dưới chú thích từng được dùng để can thiệp trạng thái nội bộ (v4.6.1 không đọc nội dung chú thích)."""
    out = []
    if isinstance(x, dict):
        for k, v in x.items():
            if isinstance(k, str) and k.startswith('_') and not KHOA_GHI_CHU.match(k):
                out.append('Khóa “%s” ở %s dành cho script, dữ liệu người nhập không được đặt – xóa khóa này.' % (k, duong))
            else:  # v4.6.2 (F06): đệ quy cả vào giá trị của khóa chú thích (_vi_du_…, _ghi_chu, _huong_dan) – chú thích vẫn được phép,
                # nhưng khóa dành cho script nằm BÊN TRONG chú thích cũng bị phát hiện (cam kết “mọi cấp”)
                out += khoa_danh_rieng(v, '%s.%s' % (duong, k))
    elif isinstance(x, list):
        for i, v in enumerate(x, 1): out += khoa_danh_rieng(v, '%s[%d]' % (duong, i))
    return out


def chuan_ma_cu(x):
    return re.sub(r'\s+', '', unicodedata.normalize('NFC', str(x or ''))).upper()


def danh_muc_ma_cu(duong_dans):
    """v4.6.1 (N31): danh mục mã cũ của báo cáo rà soát lần trước. (1) Có bảng Phần II (hàng tiêu đề có “STT” và “Mã”) → mỗi hàng là
    “<Mã>#<STT>”; (2) không có bảng → mọi mã dạng M<số>-<số>. → (tập mã, mô tả cách lập)."""
    dm, cach = set(), []
    for p in duong_dans:
        bang = set()
        if p.lower().endswith('.docx') and os.path.exists(p):
            try:
                for t in Document(p).tables:
                    if not t.rows: continue
                    hd = [unicodedata.normalize('NFC', c.text).strip() for c in t.rows[0].cells]
                    if 'STT' in hd and 'Mã' in hd:
                        i_s, i_m = hd.index('STT'), hd.index('Mã')
                        for row in t.rows[1:]:
                            cs = [c.text.strip() for c in row.cells]
                            if len(cs) > max(i_s, i_m) and cs[i_m] and re.fullmatch(r'\d+', cs[i_s]) and cs[i_s] != 'STT':
                                bang.add(chuan_ma_cu('%s#%s' % (cs[i_m], cs[i_s])))
            except Exception:
                pass
        if bang:
            dm |= bang; cach.append('bảng Phần II của %s' % os.path.basename(p))
        else:
            ma = {chuan_ma_cu(m.group(0)) for m in re.finditer(r'(?<![\w-])M\d+-\d+(?![\w-])', ND.chuan_trinh_bay(ND.doc_chu(p) or ''))}
            if ma: dm |= ma; cach.append('mã M<số>-<số> trong %s' % os.path.basename(p))
    return dm, '; '.join(cach) or 'không nhận ra mã'


def cac_trich(s_):
    """Các đoạn trích trong ngoặc kép; không có ngoặc kép → cả chuỗi."""
    x = [m.strip('“”"«»') for m in NGOAC2.findall(s_ or '')]
    return [y for y in x if y.strip(' ….')] or ([s_.strip()] if (s_ or '').strip() else [])


# ---------------------------------------------------------------- v4.6.2: dòng dẫn → MỘT nguồn (F03, F04, F05, F09); Điều theo phần/chương (F10)
_TOKEN_TEP = re.compile(r'[^\s,;()\[\]“”"«»]+\.(?:docx|xlsx|pdf|doc|xls|rtf|odt|md|txt)(?![\w])', re.I)
_MAU_CHUNG_QT = re.compile(r'(?i)quy[\s_-]*t[ắa]c|b[ảa]ng\s+th[ôo]ng\s+s[ốo]|\bKTC\b|references|nguy[êe]n[\s_-]*t[ắa]c|checklist')


def _k(s_):
    """v4.6.3: khóa so tên tệp – cùng chuẩn trình bày với dòng dẫn (khoảng trắng Unicode, gạch Pd, ký tự vô hình) để tên tệp
    có gạch ngang/khoảng trắng không ngắt vẫn khớp đúng tệp thật."""
    return ND.chuan_trinh_bay(unicodedata.normalize('NFC', s_ or '').replace('\\', '/')).casefold()


def tim_ten_tep(c, ten_map):
    """Tên tệp đã biết (ten_map: {tên đã casefold: [định danh]}) xuất hiện trong c – ưu tiên tên dài nhất, không chồng lấn; ranh giới:
    trước tên không là chữ/số/“-”/“_”/“.”/“/”, sau tên không là chữ/số. → [(đầu, cuối, tên, [định danh])]. Không đoán tên gần đúng."""
    ck, spans = _k(c), []
    for ten in sorted(ten_map, key=len, reverse=True):
        i = 0
        while True:
            j = ck.find(ten, i)
            if j < 0: break
            e = j + len(ten)
            tr, sa = (ck[j - 1] if j else ''), (ck[e] if e < len(ck) else '')
            if not (tr and (tr.isalnum() or tr in '-_./')) and not (sa and sa.isalnum()) and not any(a < e and j < b for a, b, _, _ in spans):
                spans.append((j, e, ten, ten_map[ten]))
            i = j + 1
    return sorted(spans)


MAIN_TL = ('QUYẾT ĐỊNH', 'THÔNG BÁO', 'NGHỊ QUYẾT', 'TỜ TRÌNH', 'BÁO CÁO', 'CÔNG VĂN', 'LUẬT', 'BỘ LUẬT', 'PHÁP LỆNH', 'NGHỊ ĐỊNH',
           'THÔNG TƯ', 'THÔNG TƯ LIÊN TỊCH', 'CHỈ THỊ', 'KẾT LUẬN', 'VĂN BẢN HỢP NHẤT') + ND.LOAI_KEM_TEN
_TD_DIEU = re.compile(r'^\s*Điều\s+(\d+)\s*[.:]')
_TD_CHUONG = re.compile(r'(?i)^chương\s+([IVXLC]+|\d+)\b')
_PL_TD = re.compile(r'(?i)^phụ lục\s+(?:số\s+)?([IVXLC]+|\d+)\s*(?:[.:–\-]\s*\S.*)?$')


def so_la_ma(x):
    x = (x or '').upper()
    if x.isdigit(): return int(x)
    gt, tong, truoc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}, 0, 0
    for ch in reversed(x):
        v = gt.get(ch, 0); tong += -v if v < truoc else v; truoc = max(truoc, v)
    return tong


def phan_van_ban(chu):
    """Chia văn bản thành các PHẦN (văn bản chính; văn bản kèm theo QUY ĐỊNH/QUY CHẾ…; Phụ lục) và các Điều có tiêu đề dạng chữ.
    Ranh giới phần chỉ được giữ khi đánh số Điều BẮT ĐẦU LẠI (tiêu đề in hoa giữa thân mà số Điều chạy tiếp thì không tách phần);
    dòng in hoa ngay sau “Chương/Mục/Phần …” là tên chương (“QUY ĐỊNH CHUNG”), không phải văn bản kèm theo.
    → [dict(loai, so, dieu=[(số Điều, chương, chữ của Điều)])]"""
    dong = [ND.chuan_trinh_bay(l) for l in (chu or '').split('\n')]
    moc, td, truoc = [(0, None, None)], [], ''   # mốc: (dòng bắt đầu, loại, số phụ lục)
    for i, l in enumerate(dong):
        if not l: continue
        m_pl = _PL_TD.match(l) if len(l) < 120 else None
        lk = ND.loai_tieu_de_kem(l)
        if m_pl and not re.match(r'(?i)^(chương|mục|phần)\s', truoc):
            moc.append((i, 'PHỤ LỤC', m_pl.group(1).upper()))
        elif lk and not re.match(r'(?i)^(chương|mục|phần)\s|^điều\s+\d', truoc):
            moc.append((i, lk, None))
        elif l.rstrip(':').strip() in MAIN_TL and moc[0][1] is None and len(moc) == 1:
            moc[0] = (0, l.rstrip(':').strip(), None)
        m = _TD_DIEU.match(l)
        if m: td.append((i, int(m.group(1))))
        truoc = l
    # gộp mốc giả: khối không có Điều hoặc Điều chạy tiếp → thuộc phần trước (trừ Phụ lục)
    that = [moc[0]]
    for k, (b, loai, so) in enumerate(moc[1:], 1):
        e = moc[k + 1][0] if k + 1 < len(moc) else len(dong)
        d_trong = [n for i, n in td if b <= i < e]
        d_truoc = [n for i, n in td if that[-1][0] <= i < b]
        if loai == 'PHỤ LỤC':
            that.append((b, loai, so))
        elif not d_truoc and that[-1][1] is None:
            that[-1] = (that[-1][0], loai, so)          # tiêu đề tên loại của chính phần đang mở (văn bản chính)
        elif d_trong and ((d_truoc and d_trong[0] <= max(d_truoc)) or (not d_truoc and that[-1][1] == 'PHỤ LỤC')):
            that.append((b, loai, so))                  # đánh số Điều bắt đầu lại → văn bản kèm theo thật
    out = []
    for k, (b, loai, so) in enumerate(that):
        e = that[k + 1][0] if k + 1 < len(that) else len(dong)
        chuong, ds = None, []
        tds = [(i, n) for i, n in td if b <= i < e]
        for i in range(b, e):
            mc = _TD_CHUONG.match(dong[i]) if dong[i] and len(dong[i]) < 120 else None
            if mc: chuong = so_la_ma(mc.group(1))
            for j, (ii, n) in enumerate(tds):
                if ii == i:
                    het = tds[j + 1][0] if j + 1 < len(tds) else e
                    ds.append((n, chuong, '\n'.join(dong[ii:het])))
        out.append(dict(loai=loai, so=so, dieu=ds))
    return out


_LOAI_PHAN_HOA = r'(?<!\w)(Quy định|Quy chế|Điều lệ|Nội quy|Kế hoạch|Danh mục|Chương trình|Đề án|Hướng dẫn|Quy trình|QUY ĐỊNH|QUY CHẾ|ĐIỀU LỆ|NỘI QUY|KẾ HOẠCH|DANH MỤC|CHƯƠNG TRÌNH|ĐỀ ÁN|HƯỚNG DẪN|QUY TRÌNH)(?!\w)'
_DIEU_DS = re.compile(r'(?i)(?<!\w)Điều\s+(\d+)((?:\s*(?:,|;|và|hoặc|đến|tới|–|-)\s*(?:Điều\s+)?\d+(?![\d/]))*)')


def chi_dinh_vi_tri(c):
    """Từ dòng dẫn (đã bỏ tên tệp): tập Điều được dẫn (“Điều 1 và Điều 2”, “Điều 1, 3”, “Điều 2 đến Điều 4”) và phạm vi:
    phần kèm theo (“Quy chế”, “Quy định”… – viết hoa chữ đầu; động từ “quy định” viết thường không tính), văn bản chính (“Quyết định”…,
    chỉ dùng để phân biệt khi số Điều lặp), Phụ lục, Chương."""
    so = []
    for m in _DIEU_DS.finditer(c):
        ds = [int(m.group(1))]
        for sep, n in re.findall(r'(,|;|và|hoặc|đến|tới|–|-)\s*(?:Điều\s+)?(\d+)', m.group(2)):
            n = int(n)
            if sep in ('đến', 'tới', '–', '-') and ds[-1] < n <= ds[-1] + 50: ds += list(range(ds[-1] + 1, n + 1))
            else: ds.append(n)
        so += ds
    kem = {unicodedata.normalize('NFC', x).upper() for x in re.findall(_LOAI_PHAN_HOA, c)}
    chinh = bool(re.search(r'(?i)(?<!\w)(quyết định|thông báo|nghị quyết|tờ trình|văn bản chính|luật|nghị định|thông tư)(?!\w)', c))
    pl = re.search(r'(?i)(?<!\w)phụ lục\s+(?:số\s+)?([IVXLC]+|\d+)(?!\w)', c)
    ch = re.search(r'(?i)(?<!\w)chương\s+([IVXLC]+|\d+)(?!\w)', c)
    return sorted(set(so)), dict(kem=kem, chinh=chinh, pl=pl.group(1).upper() if pl else None, chuong=so_la_ma(ch.group(1)) if ch else None,
                                 chuong_txt=ch.group(1).upper() if ch else None)


def vung_vi_tri(nguon, ns, qd):
    """Vùng chữ của các Điều ns trong nguồn [(nhãn, chữ, là văn bản chính?)] theo phạm vi qd. → (vùng | None, lỗi | None, chưa_kiểm)."""
    P = []
    for nh, chu, la_chinh in nguon:
        for k, p in enumerate(phan_van_ban(chu)): P.append(dict(p, nhan=nh, chinh=(la_chinh and k == 0)))
    if not any(p['dieu'] for p in P): return None, None, True   # không có tiêu đề Điều dạng chữ (đánh số tự động) – giữ hành vi “chưa kiểm vị trí”
    C, pv = list(P), []
    if qd['pl']:
        C = [p for p in C if p['loai'] == 'PHỤ LỤC' and p['so'] == qd['pl']]; pv.append('Phụ lục %s' % qd['pl'])
        if not C: return None, 'không có Phụ lục %s' % qd['pl'], False
    if qd['kem']:
        C2 = [p for p in C if p['loai'] in qd['kem']]
        if C2 or len(P) > 1:
            if not C2: return None, 'không có phần %s' % '/'.join(x.capitalize() for x in sorted(qd['kem'])), False
            C = C2; pv.append('/'.join(x.capitalize() for x in sorted(qd['kem'])))
    if not any(p['dieu'] for p in C): return None, None, True
    if qd['chuong']:
        pv.append('Chương %s' % qd['chuong_txt'])
        if not any(ch == qd['chuong'] for p in C for _, ch, _ in p['dieu']): return None, 'không có Chương %s%s' % (qd['chuong_txt'], (' trong phần ' + pv[-2]) if len(pv) > 1 else ''), False
    vung = []
    for n in ns:
        R = [(p, t) for p in C for n_, ch, t in p['dieu'] if n_ == n and (not qd['chuong'] or ch == qd['chuong'])]
        if not R:
            return None, 'không có Điều %d%s' % (n, (' thuộc ' + ', '.join(pv)) if pv else ''), False
        if len(R) > 1 and qd['chinh']:
            R2 = [x for x in R if x[0]['chinh']]
            if len(R2) == 1: R = R2
        if len(R) > 1:
            vd = [(p['loai'] or 'văn bản chính').capitalize() for p, _ in R]
            return None, 'Điều %d xuất hiện ở nhiều phần (%s) – dòng dẫn mơ hồ; ghi rõ phần, ví dụ %s' % (
                n, '; '.join('%s – %s' % (p['nhan'], (p['loai'] or 'văn bản').capitalize()) for p, _ in R)[:200], ' hoặc '.join('“%s, Điều %d”' % (x, n) for x in dict.fromkeys(vd))), False
        vung.append(R[0][1])
    return '\n'.join(vung), None, False


def kiem(d, cong, tts):
    loi = []
    del GIAI_TRINH[:]
    DOI_CHIEU['so_trich'] = 0
    # v4.6 (KTS-24): kết quả cổng và đo thể thức phải do CÙNG phiên bản tạo – không trộn bản vá rời với trình dựng khác phiên bản
    if cong is not None and not str(cong.get('phien_ban', '')).startswith(PHIEN_BAN_DU_LIEU):
        loi.append('Kết quả cổng hồ sơ do phiên bản “%s” tạo, khác phiên bản trình dựng (%s) – chạy lại kiem_ke_ho_so.py của cùng gói.' % (cong.get('phien_ban', 'không rõ'), PHIEN_BAN_DU_LIEU))
    for t in tts:
        if not str(t.get('phien_ban', '')).startswith(PHIEN_BAN_DU_LIEU):
            loi.append('Kết quả đo thể thức “%s” do phiên bản “%s” tạo – chạy lại kiem_tra_the_thuc.py của cùng gói.' % (t.get('_ten_tep', ''), t.get('phien_ban', 'không rõ')))
    # v4.6 (KTS-21): tệp phải còn nguyên như lúc chạy cổng (tính lại mã băm từ đường dẫn cổng ghi)
    if cong is not None:
        dd = cong.get('duong_dan') or {}
        if not dd:
            loi.append('Kết quả cổng hồ sơ không có đường dẫn tệp (“duong_dan”) – chạy lại kiem_ke_ho_so.py v4.6 để script kiểm được tệp chưa bị sửa.')
        for ten, duong in dd.items():
            try: h_ = hashlib.sha256(open(duong, 'rb').read()).hexdigest()
            except Exception: h_ = None
            if h_ is None:
                loi.append('Không đọc lại được tệp “%s” (%s) đã qua cổng – chạy lại cổng hồ sơ.' % (ten, duong))
            elif h_ != (cong.get('sha256') or {}).get(ten):
                loi.append('Tệp “%s” đã thay đổi sau khi chạy cổng hồ sơ (mã băm khác) – chạy lại kiem_ke_ho_so.py và kiem_tra_the_thuc.py cho bản hiện hành.' % ten)
    TEP_IDS[:] = sorted(((cong or {}).get('sha256') or {}).keys(), key=len, reverse=True)
    if cong is None:
        loi.append('Thiếu kết quả cổng hồ sơ (--cong). Phải chạy kiem_ke_ho_so.py trước.')
    elif cong.get('ket_luan') != 'DU':
        loi.append('Cổng hồ sơ CHẶN – không được lập báo cáo. Gửi nguyên văn thông báo chặn cho người dùng.')
    if not tts:
        loi.append('Thiếu kết quả đo thể thức (--the-thuc). Phải chạy kiem_tra_the_thuc.py cho dự thảo (và từng tệp phụ lục riêng nếu có).')
    if cong is not None:
        # v4.3 (TH-11): kết quả đo thể thức phải thuộc đúng hồ sơ đã qua cổng (khớp mã băm tệp)
        sha_cong = cong.get('sha256') or {}
        if not sha_cong:
            loi.append('Kết quả cổng hồ sơ không có mã băm tệp (chạy lại kiem_ke_ho_so.py của gói v4.6).')
        for t in tts:
            if not t.get('sha256'):
                loi.append('Kết quả đo thể thức “%s” không có mã băm tệp (chạy lại kiem_tra_the_thuc.py của gói v4.6).' % t.get('_ten_tep', ''))
            elif sha_cong and t['sha256'] not in sha_cong.values():
                loi.append('Kết quả đo thể thức “%s” (tệp %s) không thuộc hồ sơ đã qua cổng – phải đo đúng tệp dự thảo/phụ lục của hồ sơ này.' % (t.get('_ten_tep', ''), t.get('tep', '?')))
        vt_c = cong.get('vai_tro', {})
        da_do = {t.get('sha256') for t in tts}  # v4.4 (PB4-WORK-07): đối chiếu theo mã băm từng tệp, không theo tên tệp
        for ten, v in vt_c.items():
            if v in ('du_thao', 'kem_theo') and ten.lower().endswith('.docx') and sha_cong.get(ten) not in da_do:
                loi.append('Chưa đo thể thức tệp “%s” (%s) – chạy kiem_tra_the_thuc.py và truyền thêm --the-thuc.' % (ten, 'dự thảo' if v == 'du_thao' else 'phụ lục/văn bản kèm theo'))
        # v4.3 (TH-04, quyết định PB2-07 ngày 27/10/2026): mọi tệp “PHẢI XEM ẢNH” phải có kết luận xem ảnh
        xa = {x.get('tep'): x for x in d.get('xem_anh', [])}
        for ten, so_anh, _ in cong.get('anh_can_xem', []):
            x = xa.get(ten)
            if not x or x.get('ket_luan') not in ('so_do', 'van_ban_chup') or int(x.get('so_anh_da_xem', 0)) < so_anh or not _nd(x.get('mo_ta')):
                loi.append('Tệp “%s” có %d ảnh “PHẢI XEM ẢNH” nhưng “xem_anh” chưa có kết luận đủ (tep, so_anh_da_xem ≥ %d, ket_luan = so_do | van_ban_chup, mo_ta).' % (ten, so_anh, so_anh))
            elif x.get('ket_luan') == 'van_ban_chup':
                loi.append('Tệp “%s” chứa ảnh văn bản chụp/scan → hồ sơ CHẶN theo G1: không lập báo cáo; gửi thông báo yêu cầu bản chữ.' % ten)
    # v4.6 (KTS-13): bản chữ để ĐỐI CHIẾU trích dẫn – không chỉ kiểm trường có/không
    DOI_CHIEU['chua_kiem_dieu'] = []
    NG_DT, NG_HS, NG_KHO, NG_QT, _thieu = kho_van_ban(cong) if (cong and cong.get('duong_dan')) else ([], {}, [], [], [])
    co_doi_chieu = bool(NG_DT)
    dinh_danh = (cong or {}).get('dinh_danh')
    if cong is not None and cong.get('duong_dan') and dinh_danh is None:
        loi.append('Kết quả cổng hồ sơ không có định danh từng tệp (“dinh_danh”) – chạy lại kiem_ke_ho_so.py v4.6.4.')
        dinh_danh = {}
    if cong is not None and cong.get('duong_dan') and not co_doi_chieu:
        loi.append('Không đọc được chữ của tệp dự thảo đã qua cổng – không đối chiếu được trích dẫn.')
    # v4.6.2 (F03, F04, F05, F09): MỘT bảng tên nguồn – mọi tệp hồ sơ (tên như cổng ghi, tên ngắn của tệp trùng tên, đường dẫn tuyệt đối)
    # và mọi tệp quy tắc của Skill (đường dẫn tương đối trong references/, “references/…”, tên tệp). Tệp gộp trùng nội dung là MỘT nguồn.
    VT_ = (cong or {}).get('vai_tro') or {}
    DD_ = (cong or {}).get('duong_dan') or {}
    GOP_ = {}
    for g_ in (cong or {}).get('gop_trung_noi_dung') or []:
        for t_ in g_.get('tep', []): GOP_[t_] = g_.get('dung') or g_['tep'][0]
    TEXT_ = {('tep', n): t for n, t in NG_DT}
    TEXT_.update({('tep', n): t for n, t in NG_HS.items()})
    TEXT_.update({('qt', r): t for r, t in NG_QT})
    TEN_VT = {'du_thao': 'dự thảo', 'du_thao_cu': 'dự thảo lần trước', 'bao_cao_ra_soat': 'báo cáo rà soát lần trước', 'bc_tiep_thu': 'báo cáo tiếp thu, giải trình',
              'kem_theo': 'phụ lục/văn bản kèm theo', 'lien_quan': 'văn bản liên quan'}
    SO_SANH_ = (cong or {}).get('tac_vu') == 'so-sanh'  # v4.6.3 (D10): cổng đã TÍNH LẠI từ tệp – tác vụ đáng tin
    TEN_MAP = {}
    def _them(ten, idt):
        lst = TEN_MAP.setdefault(_k(ten), [])
        if idt not in lst: lst.append(idt)
    for n_ in VT_:
        idt = ('tep', GOP_.get(n_, n_))
        _them(n_, idt)
        if os.path.basename(n_) != n_: _them(os.path.basename(n_), idt)
        if DD_.get(n_): _them(DD_[n_], idt)
    for r_, _ in NG_QT:
        r2 = r_.replace(os.sep, '/'); _them(r2, ('qt', r_)); _them('references/' + r2, ('qt', r_)); _them(os.path.basename(r2), ('qt', r_))
    def nhan_id(i):
        return {'tep': 'tệp “%s”', 'qt': 'quy tắc của Skill “%s”', 'kho': '%s'}[i[0]] % i[1]

    def nguon_cua(dan, ben):
        """v4.6.2: dòng dẫn (vblq, can_cu, vi_tri…) phải chỉ tới MỘT nguồn. → ([(nhãn, chữ, là văn bản chính)], lỗi | None, dòng dẫn đã bỏ tên tệp).
        Phía dự thảo (ben = 'dt'): tên tệp ghi ở vị trí phải là tệp dự thảo/văn bản kèm theo của hồ sơ – không fallback khi tên sai (F05);
        không ghi tên tệp thì tìm trên các tệp dự thảo/văn bản kèm theo (hành vi v4.6.1). Phía nguồn (ben = 'ng'): tên tệp như cổng ghi, tên
        tệp quy tắc .md (không hiểu thành số hiệu – F03), số hiệu đã qua cổng/Kho, hoặc tên luật; nhiều nguồn (“A hoặc B”, “A, B”) → từ chối
        (F04); từ chung “quy tắc”, “KTC”… → từ chối (F09); tên ngắn trùng nhiều tệp → từ chối, đề nghị ghi đường dẫn."""
        c = unicodedata.normalize('NFC', ND.chuan_trinh_bay(dan or ''))
        spans = tim_ten_tep(c, TEN_MAP)
        rem = list(c)
        for a_, b_, _, _ in spans: rem[a_:b_] = [' '] * (b_ - a_)
        rem = ''.join(rem)
        ten_neu = []
        for a_, b_, _, ids in spans:
            if len(ids) > 1:
                return [], 'tên “%s” trùng %d tệp (%s) – ghi đường dẫn như cổng hồ sơ ghi để chỉ đúng một tệp' % (c[a_:b_], len(ids), '; '.join(x[1] for x in ids)[:200]), rem
            if ids[0] not in ten_neu: ten_neu.append(ids[0])
        la = [m.group(0) for m in _TOKEN_TEP.finditer(rem)]
        if la:
            return [], 'tên tệp “%s” không có trong hồ sơ đã qua cổng%s – ghi đúng tên tệp như cổng hồ sơ ghi' % (la[0], '' if ben == 'dt' else ' hay trong quy tắc của Skill (references/)'), rem
        if ben == 'dt':
            sai = [i for i in ten_neu if not (i[0] == 'tep' and VT_.get(i[1]) in ('du_thao', 'kem_theo'))]
            if sai:
                i = sai[0]
                return [], '%s là %s, không phải dự thảo/văn bản kèm theo của hồ sơ – vị trí phải ghi tên tệp dự thảo như cổng hồ sơ ghi' % (
                    nhan_id(i), TEN_VT.get(VT_.get(i[1]), 'tài liệu ngoài hồ sơ') if i[0] == 'tep' else 'tệp quy tắc của Skill'), rem
            if len(ten_neu) > 1:
                return [], 'vị trí chỉ tới nhiều tệp (%s) – mỗi vị trí ghi một tệp' % '; '.join(x[1] for x in ten_neu), rem
            if ten_neu:
                n_ = ten_neu[0][1]
                if ten_neu[0] not in TEXT_: return [], 'không đọc lại được tệp “%s”' % n_, rem
                return [(n_, TEXT_[ten_neu[0]], VT_.get(n_) == 'du_thao')], None, rem
            if SO_SANH_:  # v4.6.3 (D10 – quyết định 02/11/2026, ưu tiên số 2): tác vụ so sánh BẮT BUỘC chỉ rõ bản bằng tên tệp
                return [], 'tác vụ so sánh hai bản (D10): vị trí phía dự thảo phải ghi tên tệp của đúng bản như cổng hồ sơ ghi (ví dụ “%s – Điều 2”) – thiếu định danh tệp; script không tìm ngầm trên cả hai bản' % (
                    (cong or {}).get('cac_ban_du_thao') or ['<tên tệp>'])[0], rem
            return [(n_, t_, VT_.get(n_) == 'du_thao') for n_, t_ in NG_DT], None, rem
        for i in ten_neu:
            if i[0] == 'tep' and VT_.get(i[1]) != 'lien_quan':
                return [], '%s là %s – không phải văn bản nguồn (văn bản liên quan) của hồ sơ' % (nhan_id(i), TEN_VT.get(VT_.get(i[1]), 'tài liệu')), rem
        nguon = list(ten_neu)
        so_ = khoa_so(rem)
        tep_ = [i for i in ten_neu if i[0] == 'tep']
        # v4.6.3 (nghiệm thu lần 3 – mục 2, D6/F04): kiểm TẤT CẢ định danh trong dòng dẫn. Số hiệu thuộc chính tệp đã ghi tên là đồng nghĩa
        # (cùng nguồn); số hiệu KHÔNG thuộc tệp đó là nguồn thứ hai → từ chối (v4.6.2 chỉ cần MỘT số hiệu khớp tệp, số còn lại bị bỏ qua).
        for i in tep_:
            ks_ = set(dinh_danh.get(i[1], []))
            la_ = sorted(so_ - ks_)
            if la_:
                return [], 'tệp “%s” không mang số hiệu %s (tệp mang: %s) – một dòng dẫn chỉ một nguồn (D6): số hiệu của văn bản khác ghi ở trường khác' % (
                    i[1], ', '.join(la_), ', '.join(k for k in ks_ if not k.startswith('TEN:')) or 'không có số hiệu'), rem
        if so_ and not tep_:
            for k in sorted(so_):
                hs_ = sorted({('tep', GOP_.get(x, x)) for x, ks in dinh_danh.items() if VT_.get(x) == 'lien_quan' and k in ks})
                if len(hs_) > 1:
                    return [], 'số hiệu %s ứng với %d tệp khác nội dung trong hồ sơ (%s) – ghi tên tệp như cổng hồ sơ ghi' % (k, len(hs_), '; '.join(x[1] for x in hs_)), rem
                if hs_: idt = hs_[0]
                else:
                    kh = [(nh, t) for ks, nh, t, kc in NG_KHO if k in kc] or [(nh, t) for ks, nh, t, kc in NG_KHO if k in ks]
                    if not kh:
                        return [], 'không có văn bản số %s trong hồ sơ (tệp liên quan) hay Kho' % k, rem
                    if len({nh for nh, _ in kh}) > 1:
                        return [], 'số hiệu %s ứng với nhiều văn bản trong Kho (%s) – ghi đủ số, ký hiệu' % (k, '; '.join(sorted({nh for nh, _ in kh}))), rem
                    idt = ('kho', kh[0][0]); TEXT_[idt] = kh[0][1]
                if idt not in nguon: nguon.append(idt)
        # v4.6.3 (mục 2, F04): tên luật LUÔN được quét (cả khi đã có tên tệp/số hiệu). Mỗi CỤM tên luật trong dòng dẫn (không chồng lấn,
        # cụm dài hơn trùm cụm ngắn ở cùng chỗ: “Luật Giáo dục nghề nghiệp” không sinh thêm “Luật Giáo dục”) là một định danh; cụm ngắn
        # chỉ khớp phần đầu của một tên dài hơn chưa biết (“Luật Giáo dục nghề nghiệp” khi chỉ có “Luật Giáo dục”) → không xác định.
        ten_l = ND.khong_dau(ND.chuan_ten_luat(rem)).upper()
        ung_luat = []
        for x, ks in dinh_danh.items():
            for k in ks:
                if k.startswith('TEN:') and VT_.get(x) == 'lien_quan':
                    ung_luat.append((ND.khong_dau(k[4:]).upper(), ('tep', GOP_.get(x, x)), None))
        for ks, nh, t, kc in NG_KHO:
            for k in ks:
                if k.startswith('TEN:'): ung_luat.append((ND.khong_dau(k[4:]).upper(), ('kho', nh), t))
        cum = []
        for ten_k, idt, t in ung_luat:
            if not ten_k: continue
            for m in re.finditer(r'(?<![A-Z0-9])' + re.escape(ten_k) + r'(?![A-Z0-9])', ten_l):
                cum.append((m.start(), m.end(), ten_k, idt, t))
        chon = []
        for c_ in sorted(cum, key=lambda c_: (-(c_[1] - c_[0]), c_[0])):
            if any(c_[0] < b and a < c_[1] for a, b, _, _, _ in chon if (a, b) != (c_[0], c_[1])): continue
            chon.append(c_)
        theo_cho = {}
        for a, b, ten_k, idt, t in sorted(chon):
            theo_cho.setdefault((a, b), []).append((ten_k, idt, t))
        for (a, b), ds in theo_cho.items():
            sau_ = ten_l[b:].lstrip()
            tu_ = re.match(r'[A-Z]+', sau_)
            if tu_ and tu_.group(0) not in _TU_SAU_TEN_LUAT:
                return [], 'tên luật “%s” trong dòng dẫn còn chữ tiếp theo (“%s…”) – không khớp đúng tên luật nào trong hồ sơ/Kho (chỉ khớp phần đầu); ghi đúng tên luật hoặc tên tệp như cổng hồ sơ ghi' % (
                    ds[0][0].title(), sau_[:30].lower()), rem
            if any(x[1][0] == 'tep' for x in ds): ds = [x for x in ds if x[1][0] == 'tep']  # hồ sơ trước Kho (như cổng)
            ids_ = sorted({x[1] for x in ds})
            if len(ids_) > 1:
                return [], 'tên luật ứng với nhiều tệp/văn bản (%s) – ghi tên tệp như cổng hồ sơ ghi' % '; '.join(nhan_id(i) for i in ids_), rem
            for x in ds:
                if x[2] is not None: TEXT_[x[1]] = x[2]
            if ids_[0] not in nguon: nguon.append(ids_[0])
        if not nguon:
            if _MAU_CHUNG_QT.search(rem):
                return [], 'dòng dẫn chỉ ghi chung, chưa chỉ ra tài liệu nguồn cụ thể – ghi tên tệp quy tắc (ví dụ “02-Quy-Tac-Xep-Muc.md”, “Quy-Tac-KTC/05-Cong-Ho-So.md”), tên tệp như cổng hồ sơ ghi, số hiệu hoặc tên luật', rem
            return [], 'không xác định được văn bản nguồn – ghi tên tệp như cổng hồ sơ ghi, số hiệu hoặc tên luật có trong hồ sơ/Kho, hoặc tên tệp quy tắc của Skill', rem
        if len(nguon) > 1:
            return [], 'dòng dẫn chỉ tới nhiều nguồn (%s) – chưa xác định nguồn duy nhất; mỗi đoạn trích ghi một nguồn' % '; '.join(nhan_id(i) for i in nguon)[:220], rem
        i = nguon[0]
        if i not in TEXT_: return [], 'không đọc lại được %s' % nhan_id(i), rem
        return [(nhan_id(i), TEXT_[i], True)], None, rem

    def kiem_trich(s_, ben, nhan, dan=None):
        """Mỗi đoạn trích phải có thật trong ĐÚNG văn bản được dẫn; khi dòng dẫn ghi Điều (một hay nhiều Điều, kèm phần/Chương) thì phải
        nằm trong (một trong) các Điều đó của đúng phần (v4.6.2 – F10). ben = 'dt' dự thảo/văn bản kèm theo (dan = vị trí); 'ng' văn bản nguồn."""
        if not co_doi_chieu: return
        ng_, loi_ng, rem = nguon_cua(dan, ben)
        trs = cac_trich(s_)
        if loi_ng:
            DOI_CHIEU['so_trich'] += len(trs)
            loi.append('%s: %s (dòng dẫn “%s”) – không đối chiếu được đoạn trích.' % (nhan, loi_ng, (dan or '')[:100])); return
        ns, qd = chi_dinh_vi_tri(rem)
        nhan_ng = '; '.join(x for x, _, _ in ng_)[:160]
        pv = ', '.join([('Phụ lục ' + qd['pl']) if qd['pl'] else ''] + ['/'.join(x.capitalize() for x in sorted(qd['kem']))] + [('Chương ' + qd['chuong_txt']) if qd['chuong'] else ''])
        pv = ', '.join(x for x in pv.split(', ') if x)
        ds_dieu = 'Điều ' + ', '.join(str(n) for n in ns) + ((' (%s)' % pv) if pv else '')
        for tr in trs:
            DOI_CHIEU['so_trich'] += 1
            co = [x for x in ng_ if ND.tim_trich_dan(tr, x[1])]
            if not co:
                loi.append('%s: đoạn trích “%s” không tìm thấy trong %s – không được dùng làm bằng chứng (sửa đúng nguyên văn hoặc đúng văn bản được dẫn).' % (
                    nhan, tr[:80], nhan_ng if ben == 'ng' else ('tệp dự thảo/văn bản kèm theo %s' % nhan_ng)))
                continue
            if not ns: continue
            vung, loi_v, chua = vung_vi_tri(ng_, ns, qd)
            if chua:
                DOI_CHIEU['chua_kiem_dieu'].append('%s: “%s” – %s không có tiêu đề Điều dạng chữ (đánh số tự động), chưa kiểm được thuộc %s.' % (nhan, tr[:60], nhan_ng, ds_dieu))
                continue
            if loi_v:
                loi.append('%s: %s – %s (dòng dẫn “%s”); sửa đúng vị trí.' % (nhan, nhan_ng[:120], loi_v, (dan or '')[:80])); continue
            if not ND.tim_trich_dan(tr, vung):
                loi.append('%s: đoạn trích “%s” không nằm trong %s của %s (dòng dẫn “%s”) – sửa đúng vị trí.' % (nhan, tr[:80], ds_dieu, nhan_ng[:120], (dan or '')[:80]))
    # v4.6 (KTS-20): trường bắt buộc và phát hiện trùng – báo ngay ở --chi-kiem, không để vỡ khi dựng Word
    da_thay = {}
    for i, f in enumerate(d.get('phat_hien', []), 1):
        if f.get('_nguon') == 'script': continue
        thieu_tr = [k for k in ('ma', 'muc', 'vi_tri', 'mo_ta', 'kien_nghi') if not (str(f.get(k) or '').strip() if k == 'muc' else _nd(f.get(k)))]  # v4.6.3: sau chuẩn hóa khoảng trắng
        if thieu_tr: loi.append('Phát hiện %d (%s): thiếu trường bắt buộc %s.' % (i, f.get('ma', '?'), ', '.join(thieu_tr)))
        kh = (f.get('ma'), re.sub(r'\s+', ' ', str(f.get('vi_tri') or '')).strip().lower(), re.sub(r'\s+', ' ', str(f.get('mo_ta') or '')).strip().lower())
        if kh in da_thay:
            loi.append('Phát hiện %d trùng phát hiện %d (cùng mã, vị trí, mô tả) – một vấn đề một dòng; gộp vị trí thay vì lặp dòng.' % (i, da_thay[kh]))
        else: da_thay[kh] = i
    for i, f in enumerate(d.get('phat_hien', []), 1):
        ma = f.get('ma', '')
        if not re.match(r'^(TT|TB|TD|CC|TQ|DC|ND|VP|GY|DG)-\d{2}$', ma):
            loi.append('Phát hiện %d: mã “%s” không hợp lệ.' % (i, ma)); continue
        if ma.startswith('TT-') and f.get('_nguon') != 'script' and not _nd(f.get('thu_cong_ly_do')):
            loi.append('Phát hiện %d (%s): mã TT do script đo; chỉ thêm tay khi script không đo được hạng mục này – phải ghi “thu_cong_ly_do” và số đo cụ thể.' % (i, ma))
        if ma not in MUC_CHO_PHEP and ma not in MA_SCRIPT:
            loi.append('Phát hiện %d: mã “%s” không có trong bảng mã 02-Quy-Tac-Xep-Muc.md – không tự đặt mã mới.' % (i, ma)); continue
        m = muc_so(f.get('muc'))
        cho = MUC_CHO_PHEP.get(ma, {2} if ma.startswith('TT-') else None)
        if m is None: loi.append('Phát hiện %d (%s): thiếu mức.' % (i, ma))
        elif cho and m not in cho:
            loi.append('Phát hiện %d (%s): mức %d không đúng bảng mã (cho phép: %s).' % (i, ma, m, ', '.join('Mức %d' % x for x in sorted(cho))))
        if m in (1, 2):
            if not _nd(f.get('nguyen_van_du_thao')):
                loi.append('Phát hiện %d (%s, Mức %d): thiếu nguyên văn/số đo của dự thảo.' % (i, ma, m))
            if not _nd(f.get('nguyen_van_can_cu')) or not _nd(f.get('can_cu')):
                loi.append('Phát hiện %d (%s, Mức %d): thiếu căn cứ hoặc nguyên văn căn cứ.' % (i, ma, m))
            elif f.get('_nguon') != 'script' and not ma.startswith(('TT-', 'TB-', 'TD-')):
                kiem_trich(f.get('nguyen_van_du_thao'), 'dt', 'Phát hiện %d (%s), nguyên văn dự thảo' % (i, ma), f.get('vi_tri'))
                kiem_trich(f.get('nguyen_van_can_cu'), 'ng', 'Phát hiện %d (%s), nguyên văn căn cứ' % (i, ma), f.get('can_cu'))
    for i, r in enumerate(d.get('ma_tran', []), 1):
        kq = r.get('ket_qua', '')
        base = kq if kq in MA_TRAN_GT else ('Chưa kiểm' if kq.startswith('Chưa kiểm') else ('Khớp' if kq == 'Khớp – có điều khoản thay thế' else None))
        if base is None:
            loi.append('Ma trận dòng %d: kết quả “%s” ngoài 6 giá trị cho phép.' % (i, kq))
        if base in ('Khớp', 'Mâu thuẫn', 'Hẹp hơn', 'Rộng hơn'):
            if not _nd(r.get('du_thao_nguyen_van')) or not _nd(r.get('vblq_nguyen_van')):
                loi.append('Ma trận dòng %d (%s): thiếu nguyên văn hai phía.' % (i, kq))
            else:
                kiem_trich(r.get('du_thao_nguyen_van'), 'dt', 'Ma trận dòng %d, nguyên văn dự thảo' % i, r.get('du_thao_vi_tri'))
                kiem_trich(r.get('vblq_nguyen_van'), 'ng', 'Ma trận dòng %d, nguyên văn văn bản liên quan' % i, r.get('vblq'))
                if r.get('nguyen_van_thay_the'):  # v4.6.1: điều khoản thay thế gắn với văn bản chứa nó (“vblq_thay_the”)
                    if not _nd(r.get('vblq_thay_the')):
                        loi.append('Ma trận dòng %d (Khớp – có điều khoản thay thế): ghi “vblq_thay_the” – văn bản chứa điều khoản thay thế (tên tệp/số hiệu, Điều) để đối chiếu nguyên văn.' % i)
                    else:
                        kiem_trich(r.get('nguyen_van_thay_the'), 'ng', 'Ma trận dòng %d, nguyên văn điều khoản thay thế' % i, r.get('vblq_thay_the'))
                if isinstance(r.get('yeu_to_khop'), dict):
                    for k_, v_ in r['yeu_to_khop'].items():
                        q_ = [m.strip('“”"«»') for m in NGOAC2.findall(str(v_))]
                        if len(q_) >= 2:
                            kiem_trich('“%s”' % q_[0], 'dt', 'Ma trận dòng %d, yếu tố khớp “%s” (phía dự thảo)' % (i, k_), r.get('du_thao_vi_tri'))
                            kiem_trich('“%s”' % q_[1], 'ng', 'Ma trận dòng %d, yếu tố khớp “%s” (phía văn bản liên quan)' % (i, k_), r.get('vblq'))
        if base in ('Mâu thuẫn', 'Hẹp hơn', 'Rộng hơn'):
            mp = (r.get('ma_phat_hien') or '').split('#')[0]
            can = {'Mâu thuẫn': 'DC-01', 'Hẹp hơn': 'DC-02', 'Rộng hơn': 'DC-03'}[base]
            if mp != can:  # v4.3 (TH-06): đúng mã theo loại kết quả
                loi.append('Ma trận dòng %d (%s): phải chuyển thành phát hiện %s ở Phần II (trường “ma_phat_hien” = “%s”, hiện “%s”).' % (i, kq, can, can, mp or 'trống'))
            elif not any(f.get('ma') == can and muc_so(f.get('muc')) in (1, 2) for f in d.get('phat_hien', [])):
                loi.append('Ma trận dòng %d (%s): không có phát hiện %s Mức 1–2 tương ứng ở Phần II.' % (i, kq, can))
            elif len((cong or {}).get('cac_ban_du_thao') or []) > 1 and not tep_cua(r.get('du_thao_vi_tri')):  # v4.5 (PB5-WORK-14)
                loi.append('Ma trận dòng %d (%s): hồ sơ có %d bản – “du_thao_vi_tri” phải ghi tên tệp như cổng hồ sơ ghi (ví dụ “%s – Điều 7 khoản 2”).' % (
                    i, kq, len(cong['cac_ban_du_thao']), cong['cac_ban_du_thao'][0]))
            elif not any(f.get('ma') == can and muc_so(f.get('muc')) in (1, 2) and trung_vt(norm_vt(r.get('du_thao_vi_tri')), norm_vt(f.get('vi_tri')))
                         for f in d.get('phat_hien', [])):  # v4.4 (PB4-GPT-06, PB4-WORK-10)
                loi.append('Ma trận dòng %d (%s, “%s”): phát hiện %s ở Phần II phải đặt CÙNG vị trí (hoặc vị trí cha – con) với dòng ma trận; hiện các phát hiện %s ở: %s.' % (
                    i, kq, r.get('du_thao_vi_tri'), can, can, '; '.join(f.get('vi_tri', '') for f in d.get('phat_hien', []) if f.get('ma') == can)[:200]))
    # PB-11 / B2 đề xuất 6, 7: “Khớp” phải trích nguyên văn trong ngoặc kép và nêu yếu tố khớp
    vt_loi = [norm_vt(f.get('vi_tri')) for f in d.get('phat_hien', []) if f.get('vi_tri')]
    for i, r in enumerate(d.get('ma_tran', []), 1):
        kq = r.get('ket_qua', '')
        if kq.startswith('Khớp') or kq in ('Mâu thuẫn', 'Hẹp hơn', 'Rộng hơn'):
            if not NGOAC.search(r.get('du_thao_nguyen_van') or '') or not NGOAC.search(r.get('vblq_nguyen_van') or ''):
                loi.append('Ma trận dòng %d (%s): nguyên văn hai phía phải đặt trong ngoặc kép “…”.' % (i, kq))
        if kq == 'Khớp – có điều khoản thay thế':  # v4.5: ngoại lệ bảng 02 mục 4 – nguyên văn điều khoản thay thế thay cho yeu_to_khop
            if not NGOAC.search(r.get('nguyen_van_thay_the') or ''):
                loi.append('Ma trận dòng %d (Khớp – có điều khoản thay thế): phải ghi “nguyen_van_thay_the” – nguyên văn điều khoản thay thế/sửa đổi trong ngoặc kép.' % i)
        elif kq.startswith('Khớp'):
            ytk = r.get('yeu_to_khop')
            thieu = [k for k in ('chu_the', 'hanh_vi', 'muc_thoi_han') if not isinstance(ytk, dict) or not _nd(ytk.get(k))]
            if thieu:
                loi.append('Ma trận dòng %d (Khớp): “yeu_to_khop” phải là bảng {chu_the, hanh_vi, muc_thoi_han} có đủ 3 yếu tố của hai bên (thiếu: %s).' % (i, ', '.join(thieu)))
            elif any(re.search(r'trùng từ khóa|tương tự|gần giống|na ná', str(v), re.I) for v in ytk.values()):
                loi.append('Ma trận dòng %d (Khớp): yếu tố khớp chỉ là “trùng từ khóa/tương tự” – không đủ để ghi Khớp.' % i)
            elif any(len(NGOAC2.findall(str(v))) < 2 for v in ytk.values()):  # v4.3 (TH-12)
                loi.append('Ma trận dòng %d (Khớp): mỗi yếu tố khớp (chủ thể, hành vi, mức/thời hạn) phải trích HAI PHÍA trong ngoặc kép (dự thảo “…”; văn bản liên quan “…”).' % i)
            else:
                gt = r.get('giai_trinh_khop') or {}
                for k_, v_ in ytk.items():  # v4.4–v4.5: hai phía khác số/đơn vị theo thứ tự, khác phủ định, trái nghĩa thì không phải Khớp
                    ly = trai_nghia(*[x.strip('“”"«»') for x in NGOAC2.findall(str(v_))[:2]])
                    if not ly: continue
                    if isinstance(gt, dict) and len(_nd(gt.get(k_))) >= 20:  # quyết định F2: giải trình, in ở Bảng 3
                        GIAI_TRINH.append(dict(dong=i, yeu_to=k_, dau_hieu=ly, giai_trinh=gt[k_].strip()))
                        continue
                    loi.append('Ma trận dòng %d (Khớp), yếu tố “%s”: hai phía %s – không được ghi Khớp; xem lại thành Mâu thuẫn/Hẹp hơn/Rộng hơn (DC-01…03), hoặc nếu đọc nghĩa vẫn khớp thì ghi “giai_trinh_khop”: {“%s”: “lý do ≥ 20 ký tự”} (quyết định F2 – in ở Bảng 3).' % (i, k_, ly, k_))
        # v4.6 (KTS-19): kiểm va chạm cho MỌI dạng Khớp, kể cả “Khớp – có điều khoản thay thế”
        if kq.startswith('Khớp') and any(trung_vt(norm_vt(r.get('du_thao_vi_tri')), v) for v in vt_loi):
            loi.append('Ma trận dòng %d: vị trí “%s” ghi Khớp nhưng lại có phát hiện ở Phần II.' % (i, r.get('du_thao_vi_tri')))
    for f in d.get('dat', []):
        if f.get('nhom') in ('Nội dung', 'Điều khoản bắt buộc') and not _nd(f.get('vi_tri')):
            loi.append('Mục Đạt “%s” (nhóm %s): thiếu vị trí trong dự thảo (“vi_tri”).' % (f.get('noi_dung', '')[:40], f.get('nhom')))
        if f.get('vi_tri') and any(trung_vt(norm_vt(f.get('vi_tri')), v) for v in vt_loi):
            loi.append('Mục Đạt “%s” (vị trí %s) trùng vị trí có phát hiện ở Phần II – một vị trí không vừa lỗi vừa Đạt.' % (f.get('noi_dung', '')[:40], f.get('vi_tri')))
    # PB-12: cấu trúc
    vong = (cong or {}).get('vong', 1)
    che_do = unicodedata.normalize('NFC', str(d.get('che_do', 'ĐL')))
    if che_do not in ('ĐL', 'ĐC'):  # v4.6.1 (N33)
        loi.append('“che_do” = “%s” không hợp lệ – chỉ nhận ĐL (độc lập) hoặc ĐC (đối chiếu việc tiếp thu).' % d.get('che_do'))
    elif che_do == 'ĐL' and d.get('kieu_bao_cao', 'chinh_thuc') == 'chinh_thuc' and isinstance(vong, int) and vong >= 2 and \
            len(_nd(d.get('yeu_cau_doc_lap'))) < 20:  # v4.6.1 (N32): ĐL từ lần 2 chỉ khi người dùng yêu cầu rà soát lại toàn bộ (SKILL.md)
        loi.append('Cổng hồ sơ ghi lần rà soát %s nhưng dữ liệu chọn chế độ ĐL: phải ghi “yeu_cau_doc_lap” – nguyên văn yêu cầu “rà soát lại toàn bộ” của người dùng (≥ 20 ký tự, in ở I.7); không có yêu cầu đó thì dùng chế độ ĐC.' % vong)
    if d.get('che_do') == 'ĐC':
        if vong < 2:
            loi.append('Chế độ ĐC nhưng cổng hồ sơ ghi lần rà soát %s – chế độ ĐC chỉ dùng từ lần 2.' % vong)
        hq = [r for r in d.get('hoi_quy', []) if _nd(r.get('ma_cu')) and _nd(r.get('ket_qua'))]
        if not hq or len(hq) < len(d.get('hoi_quy', [])):
            loi.append('Chế độ ĐC: II.C Kiểm hồi quy (“hoi_quy”) phải có ít nhất một dòng và mọi dòng có đủ “ma_cu”, “ket_qua”.')
    n_uu = len(d.get('uu_tien', []))
    can = min(3, len(d.get('phat_hien', [])))
    if n_uu > 5 or n_uu < can:
        loi.append('Phần VI: nêu %d–5 vấn đề ưu tiên (hiện %d).' % (can, n_uu))
    for i, r in enumerate(d.get('doi_chieu', []), 1):
        if r.get('trang_thai') in ('Sửa một phần', 'Chưa sửa'):
            mp = (r.get('ma_phat_hien') or '').split('#')[0]
            if not mp or not any(f.get('ma') == mp for f in d.get('phat_hien', [])):
                loi.append('Đối chiếu dòng %d (%s): phần còn lại phải ghi thành phát hiện ở Phần II (trường “ma_phat_hien”).' % (i, r.get('trang_thai')))
        if r.get('trang_thai') == 'Kiến nghị lần trước không còn phù hợp' and not _nd(r.get('can_cu_dung')):
            loi.append('Đối chiếu dòng %d: “Kiến nghị lần trước không còn phù hợp” phải nêu căn cứ đúng (“can_cu_dung”).' % i)
    for i, r in enumerate(d.get('doi_chieu', []), 1):
        if r.get('trang_thai') not in TRANG_THAI_DC:
            loi.append('Đối chiếu dòng %d: trạng thái “%s” không hợp lệ.' % (i, r.get('trang_thai')))
        if r.get('trang_thai') in ('Đã sửa đạt', 'Sửa một phần', 'Chưa sửa') and not _nd(r.get('nguyen_van_hien_hanh')):
            loi.append('Đối chiếu dòng %d: thiếu nguyên văn/số đo bản hiện hành.' % i)
        elif NGOAC2.search(r.get('nguyen_van_hien_hanh') or ''):
            kiem_trich(r.get('nguyen_van_hien_hanh'), 'dt', 'Đối chiếu dòng %d, nguyên văn bản hiện hành' % i, r.get('vi_tri_hien_hanh'))
    if d.get('che_do') == 'ĐC' and not d.get('doi_chieu'):
        loi.append('Chế độ ĐC nhưng chưa có bảng đối chiếu việc sửa (“doi_chieu”).')
    for f in d.get('dat', []):
        if not (_nd(f.get('nguyen_van')) or _nd(f.get('so_do'))):
            loi.append('Mục Đạt “%s”: thiếu nguyên văn/số đo – không được ghi Đạt.' % f.get('noi_dung', '')[:50])
        elif _nd(f.get('nguyen_van')):
            kiem_trich(f.get('nguyen_van'), 'dt', 'Mục Đạt “%s”, nguyên văn' % f.get('noi_dung', '')[:40], f.get('vi_tri'))
    for k in ('ten_du_thao', 'don_vi_soan_thao', 'loai_van_ban', 'nguoi_kiem_tra'):
        if not _nd(d.get(k)): loi.append('Thiếu trường “%s” (hoặc chỉ có khoảng trắng).' % k)
    kieu = d.get('kieu_bao_cao', 'chinh_thuc')
    if kieu not in KIEU:
        loi.append('“kieu_bao_cao” chỉ nhận: %s.' % ', '.join(KIEU))
    tv = (cong or {}).get('tac_vu', 'ra-soat')
    # v4.6 (KTS-15): bảng ánh xạ tác vụ cổng ↔ loại báo cáo; cổng chuẩn hóa không lập báo cáo rà soát (SKILL Bước 7, tác vụ d)
    hop_le_tv = {'chinh_thuc': 'ra-soat', 'nhanh': 'ra-soat', 'so_sanh': 'so-sanh'}
    if tv == 'chuan-hoa':
        loi.append('Cổng hồ sơ chạy cho tác vụ chuẩn hóa văn phong – tác vụ này không lập báo cáo rà soát, không gán nhãn trình ký; chạy lại cổng với --tac-vu ra-soat.')
    elif kieu in hop_le_tv and hop_le_tv[kieu] != tv:
        loi.append('Kiểu báo cáo “%s” không khớp tác vụ của cổng hồ sơ (“%s”).' % (kieu, tv))
    # v4.6 (KTS-14): ma trận bắt buộc với (a), (c) – luôn gồm QĐ 1976/QĐ-CĐKT và QĐ 2073/QĐ-CĐKT (SKILL Bước 4.2)
    if kieu in ('chinh_thuc', 'so_sanh'):
        mt_ = d.get('ma_tran', [])
        for so_ in ('1976', '2073'):
            if not any(re.search(r'(?<!\d)' + so_ + r'\s*/\s*QĐ', ND.chuan_trinh_bay(r.get('vblq') or '')) for r in mt_):
                loi.append('Ma trận đối chiếu chưa có dòng đối chiếu với QĐ %s/QĐ-CĐKT – bắt buộc với rà soát chính thức và so sánh (SKILL Bước 4.2); ghi kết quả thật (kể cả “Văn bản liên quan không quy định” hoặc “Chưa kiểm (lý do)”).' % so_)
    # v4.6 (KTS-13): phải ghi kết quả kiểm tra chất lượng thật (Bước 6)
    if not [x for x in d.get('kiem_tra_chat_luong', []) if _nd(x.get('hang_muc')) and _nd(x.get('ket_qua'))]:
        loi.append('Thiếu “kiem_tra_chat_luong” – phải ghi kết quả phản biện độc lập (Bước 6) đã thực hiện.')
    # v4.6 (KTS-16): chế độ ĐC phải có bản dự thảo cũ trong hồ sơ và bảng thay đổi cũ → mới của đúng hai tệp
    if d.get('che_do') == 'ĐC':
        sha_c = (cong or {}).get('sha256') or {}
        vt_c2 = (cong or {}).get('vai_tro') or {}
        cu = [sha_c.get(t_) for t_, v_ in vt_c2.items() if v_ == 'du_thao_cu']
        moi = [sha_c.get(t_) for t_, v_ in vt_c2.items() if v_ == 'du_thao']
        ss_ = d.get('_ss') or {}
        if not cu:
            loi.append('Chế độ ĐC: hồ sơ không có dự thảo lần trước (vai trò du_thao_cu) – không đủ chứng cứ đối chiếu việc sửa; không lập bảng II.A.')
        elif not ss_:
            loi.append('Chế độ ĐC: thiếu bảng thay đổi cũ → mới (--so-sanh ss.json do so_sanh_ban.py tạo cho bản lần trước và bản hiện hành).')
        elif ss_.get('sha256_cu') not in cu or ss_.get('sha256_moi') not in moi:
            loi.append('Chế độ ĐC: bảng thay đổi (--so-sanh) không lập cho đúng bản lần trước và bản hiện hành đã qua cổng.')
        # v4.6.1 (N31 – quyết định 02/11/2026): danh mục mã cũ lấy từ báo cáo lần trước, đối chiếu PHỦ HAI CHIỀU
        bc_cu = [((cong or {}).get('duong_dan') or {}).get(t_, '') for t_, v_ in vt_c2.items() if v_ == 'bao_cao_ra_soat']
        if not bc_cu:
            loi.append('Chế độ ĐC: hồ sơ không có báo cáo rà soát lần trước (vai trò bao_cao_ra_soat) – không lập được danh mục mã cũ để đối chiếu.')
        else:
            dm, cach = danh_muc_ma_cu(bc_cu)
            co = {}
            for i, r in enumerate(d.get('doi_chieu', []), 1):
                m_ = chuan_ma_cu(r.get('ma_cu'))
                if not m_: loi.append('Đối chiếu dòng %d: thiếu “ma_cu”.' % i); continue
                if m_ in co: loi.append('Đối chiếu dòng %d: mã cũ “%s” trùng dòng %d.' % (i, m_, co[m_]))
                co.setdefault(m_, i)
                if dm and m_ not in dm:
                    loi.append('Đối chiếu dòng %d: mã cũ “%s” không có trong danh mục mã của báo cáo rà soát lần trước (%s).' % (i, r.get('ma_cu'), cach))
            if not dm:
                loi.append('Chế độ ĐC: không nhận ra mã nào trong báo cáo rà soát lần trước (không có bảng Phần II “STT – Mã”, không có mã dạng M<số>-<số>) – không chứng minh được đã đối chiếu đủ; không dùng chế độ ĐC với báo cáo này.')
            else:
                thieu_ = sorted(dm - set(co), key=lambda x: [int(n_) if n_.isdigit() else n_ for n_ in re.split(r'(\d+)', x)])
                if thieu_:
                    loi.append('Chế độ ĐC: chưa đối chiếu các mã cũ: %s (%s) – mỗi mã cũ một dòng ở “doi_chieu”; mã không còn phù hợp ghi trạng thái “Không còn áp dụng” hoặc “Kiến nghị lần trước không còn phù hợp”.' % (', '.join(thieu_), cach))
    if kieu == 'so_sanh':
        if not _nd((d.get('so_sanh') or {}).get('ket_luan')):
            loi.append('So sánh hai bản: thiếu “so_sanh.ket_luan” (bản nào hợp lý hơn, vì sao).')
        if not d.get('_ss'):
            loi.append('So sánh hai bản: thiếu bảng thay đổi (--so-sanh ss.json do so_sanh_ban.py tạo).')
        else:  # v4.5 (PB5-WORK-16): bảng thay đổi phải của đúng hai bản đã qua cổng
            hai = {(cong or {}).get('sha256', {}).get(x) for x in ((cong or {}).get('cac_ban_du_thao') or [])}
            ss_ = d['_ss']
            if not ss_.get('sha256_cu') or not ss_.get('sha256_moi'):
                loi.append('So sánh hai bản: bảng thay đổi không có mã băm hai tệp (chạy lại so_sanh_ban.py của gói v4.6).')
            elif {ss_['sha256_cu'], ss_['sha256_moi']} != hai:
                loi.append('So sánh hai bản: bảng thay đổi (--so-sanh) lập cho cặp tệp khác với hai bản đã qua cổng hồ sơ (%s) – chạy lại so_sanh_ban.py cho đúng hai bản.' % '; '.join((cong or {}).get('cac_ban_du_thao') or []))
    if d.get('nhan_ket_luan'):
        loi.append('Không điền “nhan_ket_luan” – nhãn do script tự tính.')
    # v4.3 (TH-05), v4.4 (PB4-GPT-02, PB4-WORK-06; quyết định E2 của Hiệu trưởng ngày 27/10/2026): bỏ qua dương tính giả phải chỉ đúng
    # từng phát hiện (tệp + mã + vị trí) script báo, lý do cụ thể; Mức 1 phải có nguyên văn ĐÚNG LÀ CHỮ của đoạn script báo (≥ 15 ký tự)
    for b in d.get('bo_qua_the_thuc', []):
        k = (b.get('ma'), b.get('vi_tri', ''))
        if not _nd(b.get('vi_tri')):
            loi.append('Bỏ qua %s: phải ghi “vi_tri” đúng từng phát hiện của script (không bỏ cả mã ở mọi vị trí).' % b.get('ma')); continue
        if len(tts) > 1 and not _nd(b.get('tep')):
            loi.append('Bỏ qua %s tại “%s”: hồ sơ có %d tệp đã đo – phải ghi “tep” (tên tệp như cổng hồ sơ ghi) để không bỏ nhầm phát hiện của tệp khác.' % (k + (len(tts),))); continue
        tt_ = tep_khop(tts, b.get('tep'))
        if _nd(b.get('tep')) and tt_ is None:
            loi.append('Bỏ qua %s tại “%s”: “tep” = “%s” không chỉ đúng MỘT tệp đã đo (ghi tên tệp như cổng hồ sơ ghi, ví dụ “A/Ho_so.docx”).' % (k + (b.get('tep'),))); continue
        hit = [x for t in ([tt_] if tt_ is not None else tts) for x in t.get('loi', []) if (x['ma'], x['vi_tri']) == k]
        if not hit:
            loi.append('Bỏ qua %s tại “%s”%s: không khớp phát hiện nào script đã báo.' % (k + ((' (tệp %s)' % b['tep']) if b.get('tep') else '',)))
        elif len(_nd(b.get('ly_do'))) < 20:
            loi.append('Bỏ qua %s tại “%s”: lý do phải cụ thể (nêu vì sao là dương tính giả).' % k)
        elif muc_so(hit[0].get('muc')) == 1:
            nv = chuan_nv(b.get('nguyen_van') or '')
            if not NGOAC.search(b.get('nguyen_van') or '') or len(nv) < 15:
                loi.append('Bỏ qua %s Mức 1 tại “%s”: phải có “nguyen_van” trích trong ngoặc kép (≥ 15 ký tự) từ chính đoạn script báo.' % k)
            elif not hit[0].get('doan_goc'):
                loi.append('Bỏ qua %s Mức 1 tại “%s”: kết quả đo không có nguyên văn đoạn (chạy lại kiem_tra_the_thuc.py của gói v4.6).' % k)
            elif nv not in chuan_nv(hit[0]['doan_goc']):
                loi.append('Bỏ qua %s Mức 1 tại “%s”: “nguyen_van” không phải chữ của đoạn script báo – không được dùng làm bằng chứng dương tính giả.' % k)
    return loi


def tep_khop(tts, ten):
    """v4.5 (PB5-WORK-06): tệp đo thể thức mà “tep” chỉ tới – tên như cổng hồ sơ ghi (_id); tên ngắn chỉ nhận khi duy nhất."""
    ten = (ten or '').strip()
    if not ten: return None
    a_ = [t for t in tts if t.get('_id') == ten]
    if len(a_) == 1: return a_[0]
    b_ = [t for t in tts if t.get('tep') == ten]
    return b_[0] if len(b_) == 1 else None


def nhap_the_thuc(tts, bo_qua):
    out, dat, chua, loai = [], [], [], []
    def bq_cua(t, x):
        for b in bo_qua:
            if not _nd(b.get('vi_tri')) or (b.get('ma'), b.get('vi_tri')) != (x['ma'], x['vi_tri']): continue  # v4.6.3: cùng chuẩn với kiem()
            if _nd(b.get('tep')) and tep_khop(tts, b.get('tep')) is not t: continue
            if not _nd(b.get('tep')) and len(tts) > 1: continue  # v4.4 (PB4-WORK-06): nhiều tệp thì phải chỉ đúng tệp
            return b
        return None
    for t in tts:
        nm = t.get('_id') or t.get('tep') or t.get('_ten_tep', '')
        for x in t.get('loi', []):
            b = bq_cua(t, x)
            if b:
                loai.append(dict(tep=nm, ma=x['ma'], vi_tri=x['vi_tri'], muc=x['muc'], nguyen_van=b.get('nguyen_van', ''), ly_do=b.get('ly_do', '')))
                continue
            out.append(dict(ma=x['ma'], _nguon='script', vi_tri=(nm + ' – ' if len(tts) > 1 else '') + x['vi_tri'],
                            mo_ta=x['hang_muc'], nguyen_van_du_thao='đo được ' + x['do'],
                            can_cu=x['can_cu'], nguyen_van_can_cu='Yêu cầu: ' + x['yeu_cau'], kien_nghi='Sửa thành: ' + x['yeu_cau'],
                            muc=x['muc'], chac_chan='chắc chắn'))
        for x in t.get('dat', []):
            dat.append(dict(nhom='Thể thức', noi_dung=x['hang_muc'], so_do=x['do'], nguon=x['can_cu']))
        for x in t.get('chua_kiem', []):
            chua.append(dict(noi_dung=x['hang_muc'], ly_do=x['ly_do'], nguoi_xac_minh='Người soạn thảo kiểm tra bằng Word'))
    return out, dat, chua, loai


KIEU = {'chinh_thuc': 'rà soát chính thức', 'nhanh': 'rà soát nhanh', 'so_sanh': 'so sánh hai bản'}


def la_trong_yeu(x, khoa='noi_dung'):
    """Chủ đề trọng yếu theo 02-Quy-Tac-Xep-Muc.md (thẩm quyền, thời hạn, điều cấm/cho phép, đối tượng, hiệu lực) hoặc ghi rõ “trong_yeu”: true."""
    return x.get('trong_yeu') is True or any(k in str(x.get(khoa, '') or '').lower() for k in TRONG_YEU)


def tinh(ph, ma_tran, da_ban_hanh=False, kieu='chinh_thuc', chua_kiem=None):
    dem = {m: 0 for m in (1, 2, 3, 4)}
    for f in ph: dem[muc_so(f['muc'])] += 1
    ck_trong_yeu = [r for r in ma_tran if r.get('ket_qua', '').startswith('Chưa kiểm') and la_trong_yeu(r, 'chu_de')]
    # v4.6 (KTS-17): “Chưa kiểm” trọng yếu ghi ở I.8 (chua_kiem) cũng tính vào nhãn – một nguồn dữ liệu thống nhất
    ck_trong_yeu += [x for x in (chua_kiem or []) if la_trong_yeu(x)]
    if dem[1]: nhan, qt = 'Chưa đủ điều kiện ban hành', 'Quy tắc 1: còn %d lỗi Mức 1' % dem[1]
    elif dem[2] or ck_trong_yeu: nhan, qt = 'Cần chỉnh sửa trước khi trình ký', 'Quy tắc 2: 0 Mức 1; %d Mức 2%s' % (dem[2], ('; %d chủ đề trọng yếu “Chưa kiểm”' % len(ck_trong_yeu)) if ck_trong_yeu else '')
    elif dem[3]: nhan, qt = 'Có thể ban hành sau khi chỉnh sửa nhỏ', 'Quy tắc 3: 0 Mức 1, 0 Mức 2; %d Mức 3' % dem[3]
    else: nhan, qt = 'Có thể ban hành ngay', 'Quy tắc 4: 0 Mức 1, 0 Mức 2, 0 Mức 3'
    if da_ban_hanh:  # văn bản đã ban hành: không gán nhãn trình ký (02 mục 5)
        nhan, qt = 'Kiến nghị sửa đổi, bổ sung', 'văn bản đã ban hành – %d Mức 1, %d Mức 2, %d Mức 3, %d Mức 4' % (dem[1], dem[2], dem[3], dem[4])
    if kieu in ('nhanh', 'so_sanh'):  # PB2-21: (b) và (c) không gán nhãn điều kiện trình ký
        nhan, qt = ('Rà soát nhanh – không gán nhãn trình ký' if kieu == 'nhanh' else 'So sánh hai bản – không gán nhãn trình ký'), \
                   'không áp dụng Quy tắc 1–4 của 02-Quy-Tac-Xep-Muc mục 5'
    tuan_thu = 'Chưa đạt' if dem[1] else ('Đạt' if dem[2] else ('Tốt' if dem[3] else 'Rất tốt'))
    nhom = {g: 0 for g in NHOM_LIST}
    for f in ph: nhom[f['nhom']] += 1
    return dem, nhan, qt, tuan_thu, nhom


# ---------------------------------------------------------------- docx
def shade(cell, hexcolor='D9EAF7'):
    tcPr = cell._tc.get_or_add_tcPr(); s = OxmlElement('w:shd')
    s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), hexcolor); tcPr.append(s)


def para(doc, text='', bold=False, size=14, align=None, italic=False, color=None, before=6, after=6):
    p = doc.add_paragraph(); r = p.add_run(text); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    if color: r.font.color.rgb = RGBColor(*color)
    if align == 'c': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align in ('j', None):  # v4.2: mọi đoạn lời văn của báo cáo dàn đều, thụt 1 cm (quyết định HT 26/10 số 5; TT-23, TT-24)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.first_line_indent = Cm(1)
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
    if bold: p.paragraph_format.keep_with_next = True  # v4.6 (KTS-28): tiêu đề/nhãn bảng không đứng một mình cuối trang
    return p


_DR = {}


def do_rong(s_, dam=False, co=11):
    """Bề rộng (cm) của chuỗi theo số đo phông tương thích Times New Roman (tools/do_rong_chu_TNR.json – cùng bảng đo của kiem_tra_the_thuc.py)."""
    if not _DR:
        try: _DR.update(json.load(open(os.path.join(HERE, 'do_rong_chu_TNR.json'), encoding='utf-8')))
        except Exception: _DR.update({'r': {}, 'b': {}, 'upm': 2048})
    bang, w = _DR['b' if dam else 'r'], 0
    for ch in unicodedata.normalize('NFC', s_ or ''):
        v = bang.get(str(ord(ch)))
        if v is None: v = bang.get(str(ord(unicodedata.normalize('NFD', ch)[0])), 1100)
        w += v
    return w / _DR.get('upm', 2048) * co / 72 * 2.54


LE_O = 0.45  # cm: lề trái + phải mặc định của ô (≈ 0,19 cm × 2) và dự phòng
TONG_RONG = 16.0  # cm: vùng chữ A4 lề 3/2 cm


def phan_bo_rong(widths, can):
    """v4.6.2 (F07): bảo đảm mỗi cột ≥ bề rộng tối thiểu (từ dài nhất không bẻ được); phần thiếu lấy từ các cột rộng dư, theo tỷ lệ phần dư."""
    w = list(widths)
    if sum(can) > TONG_RONG: can = [c * TONG_RONG / sum(can) for c in can]
    for _ in range(5):
        thieu = sum(max(0, c - x) for x, c in zip(w, can))
        if thieu <= 1e-6: break
        du = [(i, x - c) for i, (x, c) in enumerate(zip(w, can)) if x > c]
        tong_du = sum(v for _, v in du)
        if tong_du <= 0: break
        w = [max(x, c) for x, c in zip(w, can)]
        for i, v in du: w[i] -= thieu * v / tong_du
    return w


def cao_hang(o, w, co):
    """Ước lượng chiều cao (cm) của một hàng – để chỉ đặt “không tách hàng qua trang” cho hàng vừa một trang (hàng cao hơn không bị cắt mất chữ)."""
    h = 0
    for t, x in zip(o, w):
        avail = max(x - LE_O, 0.5)
        dong = sum(max(1, -(-do_rong(l, False, co) // avail)) for l in str(t if t is not None else '').split('\n'))
        h = max(h, dong * co * 1.18 / 72 * 2.54 + 0.2)
    return h


def doan_dem(doc):
    """Đoạn ngăn cách sau bảng (bắt buộc giữa hai bảng liền nhau và ở cuối văn bản): 1 pt, giãn dòng chính xác 1 pt, không cách đoạn –
    v4.6.2 (F07): đoạn đệm cỡ 14 của v4.6.1 bị đẩy sang trang mới khi bảng cuối vừa kín trang (trang cuối chỉ có số trang)."""
    sp_ = doc.add_paragraph(); pf = sp_.paragraph_format
    pf.space_after = Pt(0); pf.space_before = Pt(0); pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(1)
    pPr = sp_._p.get_or_add_pPr(); rpr = OxmlElement('w:rPr'); sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '2'); rpr.append(sz); pPr.append(rpr)
    return sp_


def table(doc, header, rows, widths=None, size=11):
    t = doc.add_table(rows=1, cols=len(header)); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    def _tr_pr(row, tag):  # v4.6 (KTS-28): lặp hàng tiêu đề cột; không tách hàng qua trang
        trPr = row._tr.get_or_add_trPr(); el = OxmlElement(tag); el.set(qn('w:val'), 'true'); trPr.append(el)
    if widths:  # v4.6.2 (F07): bề rộng tối thiểu theo nội dung – “STT”, mã “DC-01”, “Mức 2” không bị bẻ thành “ST/T”, “CC-/04”
        tot = sum(widths); widths = [w * TONG_RONG / tot for w in widths]
        can = []
        for i, h in enumerate(header):
            tu = [do_rong(x, True, size) for x in str(h).split()] + [do_rong(x, False, size) for r in rows for x in str(r[i] if r[i] is not None else '').split()]
            can.append(min(max(tu, default=0) + LE_O, 3.2))
        widths = phan_bo_rong(widths, can)
    _tr_pr(t.rows[0], 'w:tblHeader'); _tr_pr(t.rows[0], 'w:cantSplit')
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]; c.text = ''; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size)
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER; shade(c); c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        c.paragraphs[0].paragraph_format.keep_with_next = True  # v4.6.2 (F07): hàng tiêu đề cột đi cùng hàng dữ liệu đầu tiên
    for row in rows:
        r_ = t.add_row(); cs = r_.cells
        if not widths or cao_hang(row, widths, size) <= 12.0: _tr_pr(r_, 'w:cantSplit')  # hàng cao hơn ~ nửa trang: cho tách, không cắt chữ
        for i, v in enumerate(row):
            cs[i].text = ''; r = cs[i].paragraphs[0].add_run(str(v if v is not None else '')); r.font.size = Pt(size)
            cs[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    if widths:
        t.autofit = False
        grid = t._tbl.tblGrid
        for i, gc in enumerate(grid.findall(qn('w:gridCol'))): gc.set(qn('w:w'), str(int(widths[i] * 567)))
        for i, col in enumerate(t.columns): col.width = Cm(widths[i])
        for row in t.rows:
            for i, w in enumerate(widths): row.cells[i].width = Cm(w)
        tblPr = t._tbl.tblPr; lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    doan_dem(doc)
    return t


def dung(d, cong, ph, dat, chua, out):
    kieu = d.get('kieu_bao_cao', 'chinh_thuc')
    dem, nhan, qt, tuan_thu, nhom = tinh(ph, d.get('ma_tran', []), d.get('da_ban_hanh'), kieu, d.get('chua_kiem', []))
    doc = Document()
    st = doc.styles['Normal']; st.font.name = 'Times New Roman'; st.font.size = Pt(14)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21.0), Cm(29.7); s.orientation = WD_ORIENT.PORTRAIT
        # chuẩn Trường (quyết định của Hiệu trưởng 26/10/2026, điểm 5): lề 2/2/3/2 cm; header/footer 1,27 cm; số trang giữa lề trên, cỡ 14, ẩn trang 1
        s.top_margin = s.bottom_margin = Cm(2); s.left_margin = Cm(3); s.right_margin = Cm(2)
        s.header_distance = s.footer_distance = Cm(1.27)
        s.different_first_page_header_footer = True
        hp = s.header.paragraphs[0]; hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        f1 = OxmlElement('w:fldSimple'); f1.set(qn('w:instr'), 'PAGE')
        rr = OxmlElement('w:r'); rpr = OxmlElement('w:rPr'); sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '28'); rpr.append(sz); rr.append(rpr)
        tt_ = OxmlElement('w:t'); tt_.text = '2'; rr.append(tt_); f1.append(rr); hp._p.append(f1)
    st.paragraph_format.space_before = Pt(6); st.paragraph_format.space_after = Pt(6)
    para(doc, 'TRƯỜNG CAO ĐẲNG KON TUM', True, 13, 'c', before=0)
    tieu = {'chinh_thuc': 'BÁO CÁO RÀ SOÁT DỰ THẢO VĂN BẢN TRƯỚC KHI TRÌNH KÝ', 'nhanh': 'BÁO CÁO RÀ SOÁT NHANH DỰ THẢO VĂN BẢN',
            'so_sanh': 'BÁO CÁO SO SÁNH HAI BẢN DỰ THẢO VĂN BẢN'}[d.get('kieu_bao_cao', 'chinh_thuc')]
    para(doc, tieu, True, 15, 'c')
    para(doc, d['ten_du_thao'], True, 14, 'c')
    para(doc, TRANG_THAI, True, 13, 'c', color=(192, 0, 0))
    # Kết luận điều hành
    chan = [f for f in ph if muc_so(f['muc']) == 1]
    kl = 'KẾT LUẬN: %s. Số phát hiện: %d Mức 1, %d Mức 2, %d Mức 3, %d Mức 4 (%s).' % (nhan.upper(), dem[1], dem[2], dem[3], dem[4], qt)
    if chan: kl += ' Mục chặn trình ký: ' + '; '.join('%s (%s)' % (f['ma'], f['vi_tri'][:60]) for f in chan[:8]) + '.'
    if dem[1]: kl += ' Văn bản chưa nên phát hành cho đến khi các lỗi bắt buộc được khắc phục.'
    para(doc, kl, True, 14, 'j', color=(192, 0, 0))

    para(doc, 'PHẦN I. THÔNG TIN CHUNG', True)
    he = {'chinh_quyen': 'Văn bản hành chính (chính quyền) – TB 597/TB-CĐKT, QĐ 1355/QĐ-CĐKT, NĐ 30/2020/NĐ-CP', 'dang': 'Văn bản của Đảng – QĐ 208-QĐ/TW, HD 05-HD/VPTW, QĐ 399-QĐ/TW'}.get(d.get('he'), d.get('he', ''))
    table(doc, ['Mục', 'Nội dung'], [
        ['1. Dự thảo', d['ten_du_thao']], ['2. Loại văn bản', d['loai_van_ban']], ['3. Đơn vị soạn thảo', d['don_vi_soan_thao']],
        ['4. Hệ văn bản', he], ['5. Tác vụ, chế độ', '%s – chế độ %s' % (KIEU.get(d.get('kieu_bao_cao', 'chinh_thuc')), d.get('che_do', 'ĐL'))],
        ['6. Lần rà soát', str(d.get('lan_ra_soat', cong.get('vong', 1)))], ['7. Ngày rà soát', d.get('ngay_ra_soat', datetime.date.today().strftime('%d/%m/%Y'))],
        ['8. Phiên bản Skill', PHIEN_BAN], ['9. Phạm vi', d.get('pham_vi', 'Toàn bộ dự thảo, văn bản kèm theo và phụ lục')],
        ['10. Ghi chú', d.get('ghi_chu', '')]], [4.5, 12.5])
    para(doc, 'I.7. Kiểm kê hồ sơ (kết quả kiem_ke_ho_so.py: ĐỦ ĐIỀU KIỆN RÀ SOÁT)', True)
    vt = cong.get('vai_tro', {})
    table(doc, ['#', 'Tệp', 'Vai trò', 'Tình trạng'], [[i, t[0], {'du_thao': 'Dự thảo hiện hành', 'du_thao_cu': 'Dự thảo lần trước', 'bao_cao_ra_soat': 'Báo cáo rà soát lần trước', 'bc_tiep_thu': 'Báo cáo tiếp thu, giải trình', 'kem_theo': 'Phụ lục/văn bản kèm theo', 'lien_quan': 'Văn bản liên quan'}.get(vt.get(t[0], ''), '—'), t[2]] for i, t in enumerate(cong.get('tep', []), 1)], [1, 9, 4, 3])
    table(doc, ['#', 'Văn bản được dự thảo đề cập', 'Đoạn', 'Nguồn toàn văn'], [[i, x.get('ten') or ('%s số %s' % (x['loai'], x['so'])), x['doan'], '%s – %s' % (x['trang_thai'], x['nguon'])] for i, x in enumerate(cong.get('van_ban_de_cap', []), 1)], [1, 8, 1.5, 6.5])
    if cong.get('xac_nhan_kem_thu_cong'):  # v4.5 – quyết định F1 của Hiệu trưởng ngày 27/10/2026
        para(doc, 'Văn bản kèm theo do người rà soát xác nhận thủ công (trích yếu không khớp hoặc không có – quyết định F1):', True, 13, color=(192, 0, 0))
        table(doc, ['Bản', 'Văn bản kèm theo dự thảo ban hành', 'Tệp được xác nhận', 'Tiêu đề tệp', 'Lý do xác nhận'],
              [[x.get('ban'), x.get('van_ban_kem_theo'), x.get('tep'), x.get('tieu_de_tep'), x.get('ly_do')] for x in cong['xac_nhan_kem_thu_cong']], [2.5, 4, 2.5, 4, 4], 10)
    if cong.get('xac_nhan_toan_van_thu_cong'):  # v4.6.4 – quyết định Q5 của người phụ trách ngày 03/11/2026
        para(doc, 'Văn bản nguồn rất ngắn do người rà soát xác nhận thủ công là toàn văn (cổng không xác định được thân văn bản theo cấu trúc – quyết định Q5):', True, 13, color=(192, 0, 0))
        table(doc, ['Tệp', 'Lý do xác nhận', 'Ký tự thân nhận được'], [[x.get('tep'), x.get('ly_do'), x.get('so_ky_tu_than_nhan_duoc')] for x in cong['xac_nhan_toan_van_thu_cong']], [5, 9, 3], 10)
    if d.get('yeu_cau_doc_lap'):  # v4.6.1 (N32)
        para(doc, 'Chế độ ĐL ở lần rà soát %s theo yêu cầu của người dùng: %s' % (cong.get('vong', ''), d['yeu_cau_doc_lap'].strip()), False, 13)
    for x in cong.get('vbhn_thay_luat_goc') or []:  # v4.6.1: ghi việc dùng VBHN thay Luật gốc (quy tắc 02/11/2026)
        para(doc, 'Dùng Văn bản hợp nhất số %s (tệp %s) thay toàn văn Luật gốc theo quy tắc người phụ trách xác nhận bằng lời ngày 02/11/2026 (chưa có văn bản); VBHN là bản hợp nhất phục vụ tra cứu.' % (x.get('vbhn'), x.get('tep')), False, 13)
    for x in cong.get('gop_trung_noi_dung') or []:  # v4.6.1 (N46); v4.6.2: in ĐỦ đường dẫn các tệp gộp (kể cả ở nhiều thư mục)
        para(doc, 'Các tệp %s %s – coi là một văn bản, dùng “%s”. Đường dẫn các tệp đã gộp: %s.' % (
            ', '.join('“%s”' % t for t in x.get('tep', [])), x.get('kieu', ''), x.get('dung'), '; '.join(x.get('duong_dan', [])) or '(cổng không ghi)'), False, 13)
    ts_ = cong.get('tham_so') or {}
    if ts_:  # v4.6.2 (F11): tham số chạy cổng – trình dựng đã TÍNH LẠI cổng từ tệp với đúng các tham số này; người ký thấy mọi chỉ định thủ công
        kho_md = ND.cung_tep_kho(ts_.get('kho', ''), KK.KHO_DEFAULT)  # v4.6.3: cách viết tương đương của Kho gói = mặc định (Kho ngoài gói đã bị từ chối – D2)
        para(doc, 'Tham số chạy cổng hồ sơ (trình dựng đã tính lại kết quả cổng từ tệp với các tham số này): tác vụ %s; lần rà soát %s; --vai-tro: %s; --du-thao: %s; --xac-nhan-kem: %s; Kho: %s.' % (
            ts_.get('tac_vu'), ts_.get('vong'), '; '.join(ts_.get('vai_tro') or []) or 'không', ts_.get('du_thao') or 'không',
            '; '.join((ts_.get('xac_nhan_kem') or []) + ['toàn văn: ' + x for x in ts_.get('xac_nhan_toan_van') or []]) or 'không', 'Kho của Skill (mặc định)' if kho_md else ('KHÁC MẶC ĐỊNH – ' + ts_.get('kho', ''))), False, 13,
             color=None if kho_md else (192, 0, 0))
    gc_ = [x for x in cong.get('ghi_chu') or [] if not str(x).startswith('Các tệp ') and 'thay toàn văn Luật gốc' not in str(x)]
    if gc_:  # v4.6.2: ghi chú của cổng đưa NGUYÊN VĂN vào I.7 (05-Cong-Ho-So mục 1)
        para(doc, 'Ghi chú của cổng hồ sơ (nguyên văn):', True, 13)
        for x in gc_: para(doc, '– ' + str(x), False, 13)
    if d.get('xem_anh'):
        table(doc, ['Tệp có ảnh ≥ 1/4 trang', 'Số ảnh đã xem', 'Kết luận', 'Mô tả'], [[x.get('tep'), x.get('so_anh_da_xem'), {'so_do': 'Sơ đồ/hình minh họa – nhận'}.get(x.get('ket_luan'), x.get('ket_luan')), x.get('mo_ta')] for x in d['xem_anh']], [5, 2.5, 4, 5.5])
    para(doc, 'I.8. Nội dung chưa kiểm được', True)
    ck = chua + d.get('chua_kiem', [])
    if ck: table(doc, ['#', 'Nội dung', 'Lý do', 'Ai cần xác minh'], [[i, x['noi_dung'], x['ly_do'], x.get('nguoi_xac_minh', '')] for i, x in enumerate(ck, 1)], [1, 6, 6, 4])
    else: para(doc, 'Không có.')

    para(doc, 'PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT', True)
    if d.get('che_do') == 'ĐC':
        para(doc, 'II.A. Theo dõi các mục của báo cáo rà soát lần trước', True)
        table(doc, ['Mã cũ', 'Nội dung lần trước', 'Vị trí bản hiện hành', 'Nguyên văn/số đo bản hiện hành', 'Trạng thái', 'Mức còn lại'],
              [[r.get('ma_cu'), r.get('noi_dung_cu'), r.get('vi_tri_hien_hanh'), (r.get('nguyen_van_hien_hanh') or '') + (('\nCăn cứ đúng: ' + r['can_cu_dung']) if r.get('can_cu_dung') else ''), r.get('trang_thai'), (r.get('muc_con_lai') or '') + ((' → ' + r['ma_phat_hien']) if r.get('ma_phat_hien') else '')] for r in d['doi_chieu']], [1.6, 3.6, 2.6, 4.6, 2.4, 2.2], 10)
        para(doc, 'II.B. Danh sách phát hiện hiện hành (tồn tại và mới)', True)
    rows = []
    for i, f in enumerate(ph, 1):
        rows.append([i, f['ma'], f['nhom'], f['vi_tri'], f['mo_ta'] + ('\nDự thảo: ' + f['nguyen_van_du_thao'] if f.get('nguyen_van_du_thao') else ''),
                     f.get('can_cu', '') + ('\n' + f['nguyen_van_can_cu'] if f.get('nguyen_van_can_cu') else ''), f.get('kien_nghi', ''),
                     'Mức %d\n%s' % (muc_so(f['muc']), f.get('chac_chan', 'chắc chắn'))])
    if rows: table(doc, ['STT', 'Mã', 'Nhóm', 'Vị trí', 'Mô tả vấn đề', 'Căn cứ nhận xét', 'Kiến nghị sửa', 'Mức độ'], rows, [0.9, 1.3, 1.7, 2.3, 4.0, 3.2, 2.6, 1.4], 10)
    else: para(doc, 'Không phát hiện vấn đề.')
    if d.get('che_do') == 'ĐC' and d.get('hoi_quy'):
        para(doc, 'II.C. Kiểm hồi quy', True)
        table(doc, ['Mã cũ', 'Kết quả kiểm lại'], [[r.get('ma_cu'), r.get('ket_qua')] for r in d['hoi_quy']], [3, 14])
    if kieu == 'so_sanh':
        para(doc, 'II.D. Bảng thay đổi giữa hai bản (so_sanh_ban.py)', True)
        ssd = d.get('_ss') or {}
        tk = ssd.get('thong_ke', {})
        para(doc, 'Bản cũ: %s; bản mới: %s; %s sửa, %s thêm, %s xóa; vị trí bị ảnh hưởng: %s.' % (
            ssd.get('_ten_cu', ''), ssd.get('_ten_moi', ''), tk.get('Sửa', 0), tk.get('Thêm', 0), tk.get('Xóa', 0), ', '.join(ssd.get('vi_tri', [])) or 'không có'), align='j')
        rows_ss = [[k, r['loai'], r.get('doan_cu') or '', r.get('doan_moi') or '', r.get('vi_tri', ''), r.get('noi_dung', '')[:700]] for k, r in enumerate(ssd.get('thay_doi', []), 1)]
        if rows_ss: table(doc, ['#', 'Loại', 'Đoạn cũ', 'Đoạn mới', 'Vị trí', 'Nội dung thay đổi'], rows_ss, [0.8, 1.3, 1.3, 1.3, 2.3, 10], 10)
        para(doc, 'Kết luận so sánh: ' + d['so_sanh']['ket_luan'], True, align='j')

    para(doc, 'PHẦN III. CÁC NỘI DUNG KHÔNG PHÁT HIỆN VẤN ĐỀ', True)
    allok = dat + d.get('dat', [])
    for g in NHOM_LIST:
        items = [x for x in allok if x.get('nhom') == g]
        para(doc, '%s (%d mục)' % (g, len(items)), True, 14)
        if items: table(doc, ['#', 'Nội dung', 'Số đo / nguyên văn', 'Nguồn đối chiếu'], [[i, x.get('noi_dung', ''), x.get('so_do') or x.get('nguyen_van'), x.get('nguon', '')] for i, x in enumerate(items, 1)], [1, 5, 7, 4], 10)
        else: para(doc, 'Không có mục Đạt kèm bằng chứng.', italic=True)

    para(doc, 'PHẦN IV. BẢNG TỔNG HỢP', True)
    para(doc, 'Bảng 1. Số phát hiện theo nhóm', True, 14)
    table(doc, ['Nhóm', 'Số phát hiện'], [[g, nhom[g]] for g in NHOM_LIST] + [['Tổng cộng', sum(nhom.values())]], [10, 4])
    para(doc, 'Bảng 2. Số phát hiện theo mức', True, 14)
    table(doc, ['Mức', 'Số phát hiện'], [[TEN_MUC[m], dem[m]] for m in (1, 2, 3, 4)] + [['Tổng cộng', sum(dem.values())]], [10, 4])
    l1 = [x for x in d.get('_da_loai', []) if muc_so(x['muc']) == 1]
    if l1:  # v4.4 – quyết định E2 của Hiệu trưởng ngày 27/10/2026: Mức 1 của script đã loại phải in rõ để người ký xem lại
        para(doc, 'Bảng 2a. Phát hiện Mức 1 của script đã loại khỏi kết luận (người rà soát xác định là báo oan) – người ký xem lại', True, 14, color=(192, 0, 0))
        table(doc, ['#', 'Tệp', 'Mã', 'Vị trí', 'Nguyên văn chứng minh', 'Lý do loại'], [[i, x['tep'], x['ma'], x['vi_tri'][:120], x['nguyen_van'], x['ly_do']] for i, x in enumerate(l1, 1)], [0.8, 2.6, 1.3, 4, 4.3, 4], 10)
    para(doc, 'Bảng 3. Ma trận đối chiếu chéo', True, 14)
    mt = d.get('ma_tran', [])
    if mt:
        table(doc, ['STT', 'Chủ đề', 'Dự thảo: vị trí + nguyên văn', 'Văn bản liên quan + nguyên văn', 'Kết quả', 'Phát hiện'],
              [[i, r.get('chu_de'), '%s: %s' % (r.get('du_thao_vi_tri', ''), r.get('du_thao_nguyen_van', '')), '%s: %s' % (r.get('vblq', ''), r.get('vblq_nguyen_van', '')), r.get('ket_qua') + (('\nĐiều khoản thay thế: ' + r['nguyen_van_thay_the']) if r.get('nguyen_van_thay_the') else ''), r.get('ma_phat_hien', '')] for i, r in enumerate(mt, 1)], [0.9, 2.4, 5, 5, 2, 1.7], 10)
        if GIAI_TRINH:  # v4.5 – quyết định F2: “Khớp” mà script thấy dấu hiệu khác nhau, AI giải trình vẫn khớp
            para(doc, 'Giải trình “Khớp” khi script phát hiện dấu hiệu khác nhau giữa hai phía (quyết định F2) – người ký xem lại:', True, 13, color=(192, 0, 0))
            table(doc, ['Dòng', 'Yếu tố', 'Dấu hiệu script phát hiện', 'Giải trình'], [[x['dong'], x['yeu_to'], x['dau_hieu'], x['giai_trinh']] for x in GIAI_TRINH], [1.2, 2.3, 5.5, 8], 10)
        tk = {g: sum(1 for r in mt if r.get('ket_qua', '').startswith(g)) for g in MA_TRAN_GT}
        para(doc, 'Tổng hợp ma trận: ' + '; '.join('%s: %d' % (g, n) for g, n in tk.items()) + '.', size=14, align='j')
    else: para(doc, 'Không có văn bản liên quan cùng chủ đề để đối chiếu (đã xác nhận tại I.7).', italic=True)

    para(doc, 'PHẦN V. ĐÁNH GIÁ TỔNG THỂ', True)
    para(doc, 'Mức độ tuân thủ pháp luật: %s (gán theo số lượng Mức 1–3, 02-Quy-Tac-Xep-Muc.md mục 5).' % tuan_thu, align='j')
    para(doc, 'Mức độ sẵn sàng phát hành: %s – %s.' % (nhan, qt), True, align='j')

    para(doc, 'PHẦN VI. KẾT LUẬN', True)
    for i, x in enumerate(d.get('uu_tien', []), 1): para(doc, '%d. %s' % (i, x), align='j')
    if d.get('rui_ro'): para(doc, 'Rủi ro nếu không sửa: ' + d['rui_ro'], align='j')
    if d.get('kien_nghi_chung'): para(doc, 'Kiến nghị chung: ' + d['kien_nghi_chung'], align='j')

    para(doc, 'KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG', True)
    # v4.6 (KTS-13): ghi đúng việc script đã làm – kiểm đủ trường và ĐỐI CHIẾU đoạn trích với tệp; KHÔNG khẳng định đã đánh giá nghĩa
    kc = [['Nhãn kết luận do script tính từ Bảng 2 và “Chưa kiểm” trọng yếu', 'Đạt (tự động)'],
          ['Mức 1–2 nội dung có đủ trường bằng chứng hai phía; đoạn trích trong ngoặc kép có thật trong ĐÚNG văn bản được dẫn và đúng Điều đã ghi',
           'Đạt (script đối chiếu %d đoạn trích với văn bản mà dòng dẫn chỉ tới; việc đánh giá nghĩa do người rà soát chịu trách nhiệm)' % DOI_CHIEU['so_trich']
           + ('' if not DOI_CHIEU['chua_kiem_dieu'] else '. Chưa kiểm được vị trí Điều (văn bản đánh số Điều tự động): ' + ' | '.join(DOI_CHIEU['chua_kiem_dieu'][:6]))],
          ['Ma trận chỉ dùng 6 giá trị; “Khớp” có nguyên văn hai phía', 'Đạt (script kiểm cấu trúc và đối chiếu đoạn trích)']]
    kc += [[x.get('hang_muc', ''), x.get('ket_qua', '')] for x in d.get('kiem_tra_chat_luong', [])]  # v4.6.2: trường tùy chọn vắng không làm vỡ khi dựng
    kc += [['Bỏ qua phát hiện của script: %s – %s' % (b.get('ma', ''), b.get('vi_tri', '')), 'Lý do: ' + b.get('ly_do', '')] for b in d.get('bo_qua_the_thuc', [])]
    table(doc, ['Hạng mục kiểm', 'Kết quả'], kc, [10, 7])
    if d.get('kha_thi'):
        para(doc, 'PHẦN VII. PHÂN TÍCH TÍNH KHẢ THI VÀ RỦI RO (theo yêu cầu)', True)
        para(doc, d['kha_thi'], align='j')

    para(doc, 'THÔNG TIN TRÁCH NHIỆM', True)
    table(doc, ['Trường', 'Nội dung'], [
        ['Nguồn dữ liệu đã dùng', '; '.join(d.get('tai_lieu_da_dung', [])) or '; '.join(t[0] for t in cong.get('tep', []))],
        ['Người kiểm tra', d['nguoi_kiem_tra']],
        ['Trạng thái phê duyệt', TRANG_THAI + '. Kết quả AI chỉ có giá trị tham khảo; Trưởng/Phó đơn vị phê duyệt trước khi dùng chính thức.']], [5, 12])
    doc.core_properties.title = 'Báo cáo rà soát – ' + d['ten_du_thao'][:120]
    doc.core_properties.author = 'Skill ' + PHIEN_BAN
    doc.save(out)
    return dem, nhan, qt, tuan_thu


# ---------------------------------------------------------------- v4.6.2 (F11): JSON trung gian không được tin – tính lại từ tệp và tham số chạy
TRUONG_CONG = ('ket_luan', 'vong', 'tac_vu', 'du_thao', 'cac_ban_du_thao', 'tep_kem_theo', 'sha256', 'xac_nhan_kem_thu_cong', 'xac_nhan_toan_van_thu_cong', 'phien_ban', 'duong_dan',
               'kho', 'vbhn_thay_luat_goc', 'tep', 'vai_tro', 'van_ban_de_cap', 'dinh_danh', 'gop_trung_noi_dung', 'ly_do_chan')


def _j(x):
    return json.dumps(x, ensure_ascii=False, sort_keys=True)


def _ghi_chu_chuan(xs):
    """Bỏ phần phụ thuộc tùy chọn --xuat-anh (thư mục ảnh xuất) khỏi ghi chú cổng trước khi so; sai kiểu → giá trị khác mọi kết quả thật."""
    if not isinstance(xs, list): return ['__SAI_KIEU__', repr(xs)]
    return [re.sub(r'(ký tự chữ).*?(\. Người rà soát)', r'\1\2', str(x)) for x in xs]


def _anh(xs):
    if not isinstance(xs, list): return ['__SAI_KIEU__', repr(xs)]
    return [[x[0], x[1]] if isinstance(x, list) and len(x) >= 2 else ['__SAI_KIEU__', repr(x)] for x in xs]


def _chan_doan(err):
    """v4.6.3 (F11 – chẩn đoán lỗi môi trường): vài dòng cuối có nội dung của stderr tiến trình con (đã lọc ký tự lạ, ≤ 300 ký tự)."""
    ds = [ND.chuan_trinh_bay(x) for x in (err or '').splitlines() if ND.chuan_trinh_bay(x)]
    return (' | '.join(ds[-3:]))[:300]


def _chay_json(argv, cwd=None):
    """→ (mã thoát | None, kết quả JSON | None, chẩn đoán). Không có JSON → chẩn đoán nêu stderr/quá thời gian để người dùng biết nguyên nhân."""
    tmpd = tempfile.mkdtemp(prefix='ktc897_tinh_lai_')
    j = os.path.join(tmpd, 'kq.json')
    try:
        p = subprocess.run(argv + ['--json', j] if '--' not in argv else argv[:argv.index('--')] + ['--json', j] + argv[argv.index('--'):],
                           capture_output=True, text=True, timeout=900, cwd=cwd if cwd and os.path.isdir(cwd) else None)
        kq, e_ = (ND.doc_json_an_toan(j, 'kết quả tính lại', 'trung_gian') if os.path.exists(j) else (None, None))
        cd = _chan_doan(p.stderr) or (e_ or '') or ('không tạo được JSON; stdout: ' + _chan_doan(p.stdout) if not os.path.exists(j) else '')
        return p.returncode, kq, cd
    except subprocess.TimeoutExpired:
        return None, None, 'quá thời gian 900 giây'
    except OSError as e:
        return None, None, 'không chạy được Python/script (%s)' % (e.strerror or e)
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)


def _lech_moi_truong(rc, cd):
    return ('mã thoát %s; chẩn đoán: %s' % (rc, cd or 'không có thông tin')) + ' – nếu là lỗi môi trường (thiếu thư viện/công cụ, khác máy), chạy cả chuỗi kiem_ke_ho_so.py → kiem_tra_the_thuc.py → so_sanh_ban.py → tao_bao_cao.py trong CÙNG một môi trường (D3)'


def tai_tinh_cong(cong):
    """Chạy lại kiem_ke_ho_so.py của CÙNG gói với tham số đã ghi trong JSON cổng (“tham_so”), so mọi trường trình dựng dùng.
    → (kết quả tính lại | None, [lỗi]). Khác → JSON cổng đã bị sửa tay hoặc hồ sơ đã đổi → từ chối."""
    ts = cong.get('tham_so')
    hop = isinstance(ts, dict) and isinstance(ts.get('duong_dan'), list) and ts['duong_dan'] and all(isinstance(x, str) for x in ts['duong_dan']) \
        and ts.get('tac_vu') in ('ra-soat', 'so-sanh', 'chuan-hoa') and isinstance(ts.get('vong'), str) and isinstance(ts.get('kho'), str) \
        and all(isinstance(ts.get(k), list) and all(isinstance(x, str) for x in ts[k]) for k in ('vai_tro', 'xac_nhan_kem', 'xac_nhan_toan_van')) \
        and (ts.get('du_thao') is None or isinstance(ts.get('du_thao'), str)) and (ts.get('cwd') is None or isinstance(ts.get('cwd'), str))
    if not hop:
        return None, ['Kết quả cổng hồ sơ không có tham số chạy hợp lệ (“tham_so”) – không tính lại được để kiểm JSON cổng chưa bị sửa tay; chạy lại kiem_ke_ho_so.py %s và dùng nguyên JSON mới.' % PHIEN_BAN_DU_LIEU[-6:]]
    # v4.6.3 (D2 – quyết định 02/11/2026, ưu tiên số 1): Kho phải là Kho của gói; so đường dẫn thực đã chuẩn hóa (bản sao, liên kết tới nơi khác bị từ chối)
    if not ND.cung_tep_kho(ts['kho'], KK.KHO_DEFAULT):
        return None, ['Kết quả cổng hồ sơ chạy với Kho “%s” – không phải Kho của gói Skill (%s); từ v4.6.3 Kho ngoài gói bị TỪ CHỐI (D2). Chạy lại kiem_ke_ho_so.py không dùng --kho (hoặc --kho trỏ đúng Kho của gói).' % (
            ts['kho'], os.path.normpath(KK.KHO_DEFAULT))]
    argv = [sys.executable, os.path.join(HERE, 'kiem_ke_ho_so.py'), '--tac-vu', ts['tac_vu'], '--vong', ts['vong'], '--kho', ts['kho']]
    for x in ts['vai_tro']: argv += ['--vai-tro', x]
    for x in ts['xac_nhan_kem']: argv += ['--xac-nhan-kem', x]
    for x in ts['xac_nhan_toan_van']: argv += ['--xac-nhan-toan-van', x]  # v4.6.4 (Q5)
    if ts.get('du_thao'): argv += ['--du-thao', ts['du_thao']]
    rc, moi, cd = _chay_json(argv + ['--'] + ts['duong_dan'], ts.get('cwd'))
    if rc not in (0, 2) or not isinstance(moi, dict):
        return None, ['Không tính lại được kết quả cổng hồ sơ từ tệp và tham số đã ghi (%s) – chạy lại kiem_ke_ho_so.py rồi dựng lại.' % _lech_moi_truong(rc, cd)]
    lech = [k for k in TRUONG_CONG if _j(cong.get(k)) != _j(moi.get(k))]
    if _j(_anh(cong.get('anh_can_xem') or [])) != _j(_anh(moi.get('anh_can_xem') or [])):
        lech.append('anh_can_xem')
    if _j(_ghi_chu_chuan(cong.get('ghi_chu'))) != _j(_ghi_chu_chuan(moi.get('ghi_chu'))): lech.append('ghi_chu')
    if _j({k: v for k, v in ts.items() if k != 'cwd'}) != _j({k: v for k, v in (moi.get('tham_so') or {}).items() if k != 'cwd'}): lech.append('tham_so')
    if lech:
        return moi, ['Kết quả cổng hồ sơ không khớp kết quả tính lại từ tệp và tham số chạy đã ghi (khác ở: %s) – JSON cổng đã bị sửa tay hoặc hồ sơ đã đổi sau khi chạy cổng; chạy lại kiem_ke_ho_so.py, dùng nguyên JSON mới, không sửa tay.' % ', '.join(lech)]
    return moi, []


def tai_tinh_the_thuc(tts, cong):
    """Chạy lại kiem_tra_the_thuc.py trên đúng tệp (tìm theo mã băm trong cổng đã tính lại) với tham số đã ghi; so loi/dat/chua_kiem.
    v4.6.3 (F11): → (lỗi, danh sách kết quả TÍNH LẠI) – trình dựng dùng kết quả tính lại (nguồn đã xác minh), không dùng JSON người đưa."""
    loi, moi_ds = [], []
    tep_sha = {sha: (cong.get('duong_dan') or {}).get(ten) for ten, sha in (cong.get('sha256') or {}).items()}
    for t in tts:
        ts = t.get('tham_so')
        if not (isinstance(ts, dict) and ts.get('he') in ('auto', 'chinh_quyen', 'dang')):
            loi.append('Kết quả đo thể thức “%s” không có tham số chạy hợp lệ (“tham_so”) – không tính lại được để kiểm JSON đo chưa bị sửa tay; chạy lại kiem_tra_the_thuc.py %s.' % (t.get('_ten_tep', ''), PHIEN_BAN_DU_LIEU[-6:])); continue
        p = tep_sha.get(t.get('sha256')) if isinstance(t.get('sha256'), str) else None
        if not p: moi_ds.append(t); continue  # kiem() báo “không thuộc hồ sơ đã qua cổng”
        rc, moi, cd = _chay_json([sys.executable, os.path.join(HERE, 'kiem_tra_the_thuc.py'), p, '--he', ts['he']] + (['--khong-dung-ban'] if ts.get('khong_dung_ban') else []))
        if not isinstance(moi, dict):
            loi.append('Không tính lại được kết quả đo thể thức “%s” (%s).' % (t.get('_ten_tep', ''), _lech_moi_truong(rc, cd))); continue
        lech = [k for k in ('he', 'sha256', 'phien_ban', 'loi', 'dat', 'chua_kiem') if _j(t.get(k)) != _j(moi.get(k))]
        if lech:
            loi.append('Kết quả đo thể thức “%s” không khớp kết quả tính lại từ tệp (khác ở: %s) – JSON đo đã bị sửa tay hoặc tệp đã đổi; chạy lại kiem_tra_the_thuc.py, không sửa tay.' % (t.get('_ten_tep', ''), ', '.join(lech)))
            continue
        moi['_ten_tep'] = t.get('_ten_tep', ''); moi_ds.append(moi)
    return loi, moi_ds


def tai_tinh_so_sanh(ss, cong):
    """v4.6.3 (nghiệm thu lần 3 – mục 4): tính lại bảng thay đổi từ hai tệp theo mã băm; tên/đường dẫn bản cũ, bản mới trong JSON phải
    trỏ ĐÚNG tệp thật của mã băm đó (sửa tên, đảo tên, trỏ tệp khác → từ chối). → (lỗi, bảng tính lại kèm tên hiển thị lấy từ cổng)."""
    if not str(ss.get('phien_ban', '')).startswith(PHIEN_BAN_DU_LIEU):
        return ['Bảng thay đổi (--so-sanh) do phiên bản “%s” tạo – chạy lại so_sanh_ban.py của cùng gói.' % ss.get('phien_ban', 'không rõ')], None
    ten_sha = {}
    for ten, sha in (cong.get('sha256') or {}).items(): ten_sha.setdefault(sha, []).append(ten)
    dd = cong.get('duong_dan') or {}
    ten_c, ten_m = ten_sha.get(ss.get('sha256_cu')) or [], ten_sha.get(ss.get('sha256_moi')) or []
    if not ten_c or not ten_m: return [], None  # kiem() báo bảng thay đổi không thuộc hồ sơ
    loi = []
    for k_, ds_ in (('cu', ten_c), ('moi', ten_m)):
        v_ = ss.get(k_)
        if not isinstance(v_, str) or not any(ND.cung_tep_kho(v_, dd.get(t_, '')) for t_ in ds_):
            loi.append('Bảng thay đổi (--so-sanh): trường “%s” = “%s” không phải tệp thật có mã băm %s… (tệp trong hồ sơ: %s) – tên/đường dẫn nguồn trong JSON đã bị sửa; chạy lại so_sanh_ban.py, không sửa tay.' % (
                k_, str(v_)[:120], str(ss.get('sha256_' + k_))[:12], '; '.join(ds_)))
    if loi: return loi, None
    rc, moi, cd = _chay_json([sys.executable, os.path.join(HERE, 'so_sanh_ban.py'), dd[ten_c[0]], dd[ten_m[0]]])
    if not isinstance(moi, dict): return ['Không tính lại được bảng thay đổi so sánh hai bản (%s).' % _lech_moi_truong(rc, cd)], None
    lech = [k for k in ('sha256_cu', 'sha256_moi', 'thong_ke', 'vi_tri', 'thay_doi') if _j(ss.get(k)) != _j(moi.get(k))]
    if lech:
        return ['Bảng thay đổi so sánh hai bản (--so-sanh) không khớp kết quả tính lại từ hai tệp (khác ở: %s) – JSON đã bị sửa tay hoặc tệp đã đổi; chạy lại so_sanh_ban.py, không sửa tay.' % ', '.join(lech)], None
    moi['_ten_cu'], moi['_ten_moi'] = ten_c[0], ten_m[0]  # tên hiển thị: tên tệp như cổng hồ sơ ghi (nguồn đã xác minh)
    return [], moi


def doc_json(p, ten, loai='trung_gian'):
    return ND.doc_json_an_toan(p, ten, loai)  # v4.6.3 (F01): giới hạn kích thước, độ sâu, số; không Traceback


def kiem_cau_truc_do(t, ten):
    """Kết quả đo thể thức phải đúng cấu trúc trước khi nhập (nhap_the_thuc đọc trực tiếp các khóa)."""
    if not isinstance(t, dict): return ['Kết quả đo thể thức “%s”: phải là đối tượng JSON (hiện là %s).' % (ten, KD.ten_gia_tri(t))]
    loi = ['Kết quả đo thể thức “%s”: trường “%s” phải là chuỗi – chạy lại kiem_tra_the_thuc.py, không sửa tay.' % (ten, k)
           for k in ('sha256', 'phien_ban', 'tep', 'he') if k in t and not isinstance(t[k], str)]
    for k, khoa in (('loi', ('ma', 'vi_tri', 'muc', 'hang_muc', 'do', 'can_cu', 'yeu_cau')), ('dat', ('hang_muc', 'do', 'can_cu')), ('chua_kiem', ('hang_muc', 'ly_do'))):
        v = t.get(k, [])
        if not isinstance(v, list) or not all(isinstance(x, dict) and all(isinstance(x.get(q), str) for q in khoa) for x in v):
            loi.append('Kết quả đo thể thức “%s”: trường “%s” phải là danh sách đối tượng có %s là chuỗi – chạy lại kiem_tra_the_thuc.py, không sửa tay.' % (ten, k, ', '.join(khoa)))
    return loi


def dung_lai(loi):
    print('DỮ LIỆU BÁO CÁO CHƯA HỢP LỆ – không dựng tệp:')
    for x in loi: print(' -', x)
    sys.exit(1)


def main():
    try:  # v4.6.3: ký tự không in được trên bàn điều khiển không làm vỡ thông báo
        sys.stdout.reconfigure(errors='backslashreplace')
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument('du_lieu'); ap.add_argument('--cong'); ap.add_argument('--the-thuc', action='append', default=[])
    ap.add_argument('-o', '--out', default='bao_cao_ra_soat.docx'); ap.add_argument('--chi-kiem', action='store_true')
    ap.add_argument('--so-sanh', default=None, help='JSON do so_sanh_ban.py tạo (bắt buộc với kieu_bao_cao = so_sanh)')
    a = ap.parse_args()
    if not a.chi_kiem:  # v4.6.3: kiểm tệp kết quả TRƯỚC – không ghi đè tệp đầu vào, thư mục phải có
        e = ND.kiem_duong_dan_ghi(a.out, [a.du_lieu, a.cong, a.so_sanh] + list(a.the_thuc), '.docx')
        if e: dung_lai(['Tham số -o: ' + e + '.'])
    d, e = doc_json(a.du_lieu, 'dữ liệu báo cáo', 'du_lieu')
    if e: dung_lai([e])
    # v4.6.2 (F01, F02): kiểm KIỂU, CẤU TRÚC mọi trường trước mọi xử lý; sai kiểu → dừng có kiểm soát, báo đường dẫn trường và kiểu hợp lệ
    loi_kieu, chuan_null = KD.kiem_du_lieu(d)
    loi_khoa = khoa_danh_rieng(d) if isinstance(d, dict) else []  # v4.6.1 (N25), v4.6.2 (F06): kiểm TRƯỚC khi trình dựng tự thêm _ss, _nguon
    if loi_kieu: dung_lai(loi_kieu + loi_khoa)
    chuan_null()
    loi_dau = []
    cong = None
    if a.cong:
        cong, e = doc_json(a.cong, 'kết quả cổng hồ sơ')
        if e: loi_dau.append(e)
        elif not isinstance(cong, dict): loi_dau.append('Kết quả cổng hồ sơ “%s”: phải là đối tượng JSON (hiện là %s).' % (a.cong, KD.ten_gia_tri(cong))); cong = None
    tts = []
    for p in a.the_thuc:
        t, e = doc_json(p, 'kết quả đo thể thức')
        ten = os.path.basename(p).replace('.json', '')
        if e: loi_dau.append(e); continue
        l_ = kiem_cau_truc_do(t, ten)
        if l_: loi_dau += l_; continue
        t['_ten_tep'] = ten; tts.append(t)
    if a.so_sanh:
        ss, e = doc_json(a.so_sanh, 'bảng thay đổi (--so-sanh)')
        if e: loi_dau.append(e)
        elif not isinstance(ss, dict): loi_dau.append('Bảng thay đổi (--so-sanh): phải là đối tượng JSON.')
        else:
            sai_ = [k for k, ty in (('sha256_cu', str), ('sha256_moi', str), ('cu', str), ('moi', str), ('thong_ke', dict), ('vi_tri', list), ('thay_doi', list))
                    if k in ss and not isinstance(ss[k], ty)]
            if sai_ or not all(isinstance(r, dict) for r in ss.get('thay_doi', [])):
                loi_dau.append('Bảng thay đổi (--so-sanh): sai cấu trúc ở %s – chạy lại so_sanh_ban.py, không sửa tay.' % (', '.join(sai_) or 'thay_doi'))
            else: d['_ss'] = ss
    # v4.6 (KTS-24) – v4.6.2: kết quả cổng/đo của phiên bản khác → dừng NGAY (không xử lý tiếp cấu trúc JSON của phiên bản khác, tránh Traceback)
    if cong is not None and not str(cong.get('phien_ban', '')).startswith(PHIEN_BAN_DU_LIEU):
        loi_dau.append('Kết quả cổng hồ sơ do phiên bản “%s” tạo, khác phiên bản trình dựng (%s) – chạy lại kiem_ke_ho_so.py của cùng gói.' % (cong.get('phien_ban', 'không rõ'), PHIEN_BAN_DU_LIEU))
    for t in tts:
        if not str(t.get('phien_ban', '')).startswith(PHIEN_BAN_DU_LIEU):
            loi_dau.append('Kết quả đo thể thức “%s” do phiên bản “%s” tạo – chạy lại kiem_tra_the_thuc.py của cùng gói.' % (t.get('_ten_tep', ''), t.get('phien_ban', 'không rõ')))
    if loi_dau: dung_lai(loi_dau + loi_khoa)
    # v4.6.2 (F11): không tin JSON trung gian – tính lại cổng, đo thể thức, bảng thay đổi từ tệp thật và tham số chạy đã ghi
    # v4.6.3: sau khi khớp, trình dựng DÙNG kết quả tính lại (tên, đường dẫn, vai trò, bảng thay đổi hiển thị lấy từ nguồn đã xác minh)
    if cong is not None:
        moi, l_ = tai_tinh_cong(cong)
        if l_: dung_lai(l_ + loi_khoa)
        cong = moi
        l_, tts = tai_tinh_the_thuc(tts, cong)
        if d.get('_ss'):
            l2_, ss_moi = tai_tinh_so_sanh(d['_ss'], cong)
            l_ += l2_
            if ss_moi is not None: d['_ss'] = ss_moi
        if l_: dung_lai(l_ + loi_khoa)
        if not a.chi_kiem:  # v4.6.3: tệp kết quả không được trùng tệp hồ sơ đã qua cổng
            e = ND.kiem_duong_dan_ghi(a.out, list((cong.get('duong_dan') or {}).values()), '.docx')
            if e: dung_lai(['Tham số -o: ' + e + '.'])
    sha_id = {}
    for k_, v_ in ((cong or {}).get('sha256') or {}).items(): sha_id.setdefault(v_, []).append(k_)
    for t in tts:  # v4.4 (PB4-WORK-07): tên tệp theo cổng hồ sơ (đường dẫn tương đối khi trùng tên), xác định bằng mã băm
        ids = sha_id.get(t.get('sha256'), [])
        t['_id'] = (t.get('tep') if t.get('tep') in ids else ids[0]) if ids else t.get('tep', t['_ten_tep'])
    sp, sdat, schua, sloai = nhap_the_thuc(tts, d.get('bo_qua_the_thuc', []))
    d['_da_loai'] = sloai
    ph = sp + d.get('phat_hien', [])
    for f in ph: f['nhom'] = nhom_cua(str(f.get('ma') or ''))  # v4.6.1 (N24): thiếu mã → kiem() từ chối có thông báo, không vỡ
    ph.sort(key=lambda f: (muc_so(f.get('muc')) or 9, NHOM_LIST.index(f['nhom']), str(f.get('ma') or '')))  # thứ tự cố định
    loi = loi_khoa + kiem(dict(d, phat_hien=ph), cong, tts)
    if loi: dung_lai(loi)
    if a.chi_kiem:
        dem, nhan, qt, tt = tinh(ph, d.get('ma_tran', []), d.get('da_ban_hanh'), d.get('kieu_bao_cao', 'chinh_thuc'), d.get('chua_kiem', []))[:4]
    else:  # v4.6.3: ghi qua tệp tạm rồi thay thế – từ chối/lỗi giữa chừng không để lại tệp dở dang, không đổi tệp cũ
        kq_ = {}
        e = ND.ghi_tep_an_toan(a.out, lambda tam: kq_.update(r=dung(d, cong, ph, sdat, schua, tam)))
        if e: dung_lai(['Không dựng được báo cáo: ' + e + '.'])
        dem, nhan, qt, tt = kq_['r']
    n_l1 = sum(1 for x in sloai if muc_so(x['muc']) == 1)
    print('HỢP LỆ. Nhãn: %s (%s). Mức 1/2/3/4 = %d/%d/%d/%d. Tuân thủ: %s.%s%s' % (nhan, qt, dem[1], dem[2], dem[3], dem[4], tt,
          (' Đã loại %d phát hiện Mức 1 của script (in ở Bảng 2a).' % n_l1) if n_l1 else '', '' if a.chi_kiem else ' Đã ghi: ' + a.out))


if __name__ == '__main__':
    main()
