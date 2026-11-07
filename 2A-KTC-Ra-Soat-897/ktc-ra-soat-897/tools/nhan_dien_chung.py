# -*- coding: utf-8 -*-
"""nhan_dien_chung.py – các hàm nhận diện DÙNG CHUNG cho kiem_ke_ho_so.py, kiem_tra_the_thuc.py, tao_bao_cao.py (v4.6).

Nguyên tắc (báo cáo kiểm toán 01/11/2026 – KTS-01, KTS-26, PH-01; yêu cầu sửa 02/11/2026):
- Xử lý Unicode theo THUỘC TÍNH ký tự (unicodedata.category, chuẩn hóa NFC), không dùng dải mã hay danh sách ký tự cố định.
- Bản chuẩn hóa chỉ dùng để SO KHỚP; chứng cứ (nguyên văn, vị trí) luôn lấy từ bản gốc.
- Khoảng trắng trình bày (dấu cách thường, khoảng trắng không ngắt, tab, ngắt dòng mềm, zero-width) và các dấu gạch tương đương
  không làm đổi định danh số, ký hiệu; nhưng không xóa mọi khoảng trắng của văn bản (tránh ghép nhầm hai số hiệu).
"""
import re
import unicodedata

__all__ = ['nfc', 'chuan_trinh_bay', 'chuan_so_hieu', 'khong_dau', 'la_in_hoa', 'chuan_ten_luat',
           'LOAI_KEM_TEN', 'loai_tieu_de_kem', 'ngay_hop_le', 'tim_trich_dan', 'co_noi_dung', 'noi_dung',
           'doc_json_an_toan', 'GIOI_HAN_JSON', 'ky_tu_khong_hop_le', 'cung_tep_kho', 'ghi_tep_an_toan', 'kiem_duong_dan_ghi']

# v4.6.3 (nghiệm thu lần 3 – mục 1, F01): giới hạn CÔNG BỐ khi đọc mọi tệp JSON (dữ liệu báo cáo, kết quả cổng, đo, so sánh).
# Vượt giới hạn → từ chối có kiểm soát, chỉ rõ giới hạn bị vi phạm; không tăng giới hạn đệ quy/số của Python, không bắt Exception rồi coi là hợp lệ.
GIOI_HAN_JSON = dict(
    du_lieu_mb=16,      # tệp dữ liệu báo cáo (du_lieu.json) tối đa 16 MB
    trung_gian_mb=64,   # kết quả cổng/đo/so sánh do script tạo tối đa 64 MB
    do_sau=64,          # độ sâu lồng {…}/[…] tối đa 64 cấp (mẫu dữ liệu dùng ≤ 5 cấp; chú thích _vi_du… được lồng trong giới hạn này)
    chu_so=15,          # số nguyên tối đa 15 chữ số (|n| < 10^15); số thực phải hữu hạn, tối đa 40 ký tự
)


def noi_dung(v):
    """v4.6.3 (mục 5): nội dung của một trường chữ SAU chuẩn hóa khoảng trắng – bỏ ký tự định dạng vô hình (Cf: zero-width…),
    mọi khoảng trắng Unicode (Z*, tab, xuống dòng) coi là dấu cách, rồi cắt hai đầu. Không phải chuỗi → ''."""
    return chuan_trinh_bay(v) if isinstance(v, str) else ''


def co_noi_dung(v):
    return bool(noi_dung(v))


def ky_tu_khong_hop_le(s):
    """Ký tự không ghi được vào tệp Word/XML hoặc không in được: nửa cặp thay thế (surrogate, category Cs), ký tự điều khiển C0/C1
    trừ tab/xuống dòng, U+FFFE/U+FFFF. → mô tả ký tự đầu tiên vi phạm hoặc None."""
    for i, ch in enumerate(s):
        o = ord(ch)
        if 0xD800 <= o <= 0xDFFF:
            return 'nửa cặp thay thế U+%04X ở ký tự thứ %d' % (o, i + 1)
        if (o < 0x20 and ch not in '\t\n\r') or 0x7F <= o <= 0x9F or o in (0xFFFE, 0xFFFF):
            return 'ký tự điều khiển U+%04X ở ký tự thứ %d' % (o, i + 1)
    return None


class _LoiGioiHan(ValueError):
    pass


def _do_sau_toi_da(text, gioi_han):
    """Độ sâu lồng tối đa của văn bản JSON, quét tuần tự (không đệ quy), bỏ qua chữ trong chuỗi. Dừng sớm khi vượt giới hạn."""
    sau, toi_da, trong_chuoi, thoat = 0, 0, False, False
    for ch in text:
        if trong_chuoi:
            if thoat: thoat = False
            elif ch == '\\': thoat = True
            elif ch == '"': trong_chuoi = False
            continue
        if ch == '"': trong_chuoi = True
        elif ch in '[{':
            sau += 1
            if sau > toi_da:
                toi_da = sau
                if toi_da > gioi_han: return toi_da
        elif ch in ']}':
            sau -= 1
    return toi_da


class _GiaTriLoi(object):
    """Giá trị số vượt giới hạn – giữ lại để báo kèm ĐƯỜNG DẪN TRƯỜNG khi duyệt (không chuyển int()/float() số khổng lồ)."""
    def __init__(self, mo_ta): self.mo_ta = mo_ta


def _so_nguyen(s):
    n = len(s.lstrip('-'))
    if n > GIOI_HAN_JSON['chu_so']:
        return _GiaTriLoi('số nguyên %s… có %d chữ số – phải là số có tối đa %d chữ số' % (s[:12], n, GIOI_HAN_JSON['chu_so']))
    return int(s)


def _so_thuc(s):
    import math
    if len(s) > 40:
        return _GiaTriLoi('số thực %s… dài %d ký tự – phải là số có tối đa 40 ký tự' % (s[:12], len(s)))
    v = float(s)
    if not math.isfinite(v):
        return _GiaTriLoi('số thực %s vượt miền giá trị (vô hạn) – phải là số hữu hạn' % s[:20])
    return v


def _hang_so(s):
    return _GiaTriLoi('giá trị %s không phải JSON chuẩn (NaN/Infinity không được nhận) – phải là số hữu hạn' % s)


def _doi_tuong(cap):
    out = {}
    for k, v in cap:
        if k in out:
            raise _LoiGioiHan('khóa “%s” lặp lại trong cùng một đối tượng' % k[:40])
        out[k] = v
    return out


def _kiem_chuoi(o):
    """Duyệt KHÔNG đệ quy (độ sâu đã giới hạn) mọi khóa, chuỗi, số; → lỗi đầu tiên theo thứ tự tệp (đường dẫn trường như
    kiem_kieu_du_lieu: “phat_hien[1].muc”, chỉ số từ 1) hoặc None."""
    st = [(o, '')]
    while st:
        x, d = st.pop()
        ten = d or 'gốc'
        if isinstance(x, _GiaTriLoi):
            return 'trường “%s”: %s' % (ten, x.mo_ta)
        if isinstance(x, str):
            v = ky_tu_khong_hop_le(x)
            if v: return 'trường “%s”: chuỗi có %s' % (ten, v)
        elif isinstance(x, dict):
            con = []
            for k, y in x.items():
                v = ky_tu_khong_hop_le(k)
                if v: return 'trường “%s”: tên khóa có %s' % (ten, v)
                con.append((y, ('%s.%s' % (d, k)) if d else k))
            st.extend(reversed(con))
        elif isinstance(x, list):
            st.extend(reversed([(y, '%s[%d]' % (d, i)) for i, y in enumerate(x, 1)]))
    return None


def doc_json_an_toan(path, ten, loai='du_lieu'):
    """v4.6.3 (F01): đọc JSON có kiểm soát. → (đối tượng, lỗi | None). Kiểm: tồn tại, kích thước, mã hóa UTF-8, độ sâu lồng,
    số nguyên quá lớn, số thực vô hạn/NaN, khóa lặp, ký tự không hợp lệ trong chuỗi. Mọi lỗi nêu đúng giới hạn bị vi phạm."""
    import os, json
    mb = GIOI_HAN_JSON['du_lieu_mb' if loai == 'du_lieu' else 'trung_gian_mb']
    try:
        n = os.path.getsize(path)
    except FileNotFoundError:
        return None, 'Không có tệp %s “%s”.' % (ten, path)
    except OSError as e:
        return None, 'Không đọc được tệp %s “%s” (%s).' % (ten, path, e.strerror or e)
    if n > mb * 1024 * 1024:
        return None, 'Tệp %s “%s” có %.1f MB – vượt giới hạn %d MB của Skill; tách hoặc rút gọn dữ liệu.' % (ten, path, n / 1048576, mb)
    try:
        with open(path, 'rb') as f: raw = f.read()
        text = raw.decode('utf-8-sig')
    except UnicodeDecodeError as e:
        return None, 'Tệp %s “%s” không phải văn bản UTF-8 (byte lỗi ở vị trí %d).' % (ten, path, e.start)
    except OSError as e:
        return None, 'Không đọc được tệp %s “%s” (%s).' % (ten, path, e.strerror or e)
    sau = _do_sau_toi_da(text, GIOI_HAN_JSON['do_sau'])
    if sau > GIOI_HAN_JSON['do_sau']:
        return None, 'Tệp %s “%s”: cấu trúc lồng sâu hơn %d cấp – vượt giới hạn độ sâu %d cấp của Skill.' % (ten, path, GIOI_HAN_JSON['do_sau'], GIOI_HAN_JSON['do_sau'])
    try:
        o = json.loads(text, parse_int=_so_nguyen, parse_float=_so_thuc, parse_constant=_hang_so, object_pairs_hook=_doi_tuong)
    except _LoiGioiHan as e:
        return None, 'Tệp %s “%s”: %s (giới hạn của Skill).' % (ten, path, e)
    except json.JSONDecodeError as e:
        return None, 'Tệp %s “%s” không phải JSON hợp lệ (%s).' % (ten, path, e)
    except (ValueError, RecursionError, MemoryError) as e:
        return None, 'Tệp %s “%s” không đọc được dưới giới hạn của Skill (%s).' % (ten, path, type(e).__name__)
    loi = _kiem_chuoi(o)
    if loi:
        return None, 'Tệp %s “%s”: %s (giới hạn/ràng buộc của Skill; không dựng báo cáo).' % (ten, path, loi)
    return o, None


def _thuc(p):
    import os
    return os.path.normcase(os.path.realpath(os.path.abspath(p)))


def cung_tep_kho(p, mac_dinh):
    """v4.6.3 (D2): đường dẫn Kho p có THỰC SỰ là Kho của gói (mac_dinh) không – so đường dẫn thực đã chuẩn hóa theo hệ điều hành
    (giải liên kết tượng trưng, “..”, “.”, hoa thường trên Windows). Bản sao Kho ở nơi khác, liên kết tới thư mục khác → không cùng."""
    try:
        return _thuc(p) == _thuc(mac_dinh)
    except (OSError, ValueError, TypeError):
        return False


def kiem_duong_dan_ghi(out, dau_vao, duoi=None):
    """v4.6.3: tệp kết quả không được trùng tệp đầu vào (ghi đè dự thảo/hồ sơ), thư mục phải có sẵn, đúng đuôi. → lỗi | None."""
    import os
    o = _thuc(out)
    for x in dau_vao:  # kiểm nguy cơ ghi đè TRƯỚC (lý do quan trọng nhất), rồi mới đến đuôi tệp, thư mục
        if x and _thuc(x) == o:
            return 'tệp kết quả “%s” trùng tệp đầu vào – không ghi đè tệp đầu vào; chọn tên tệp kết quả khác' % out
    if duoi and not out.lower().endswith(duoi):
        return 'tệp kết quả “%s” phải có đuôi %s' % (out, duoi)
    thu_muc = os.path.dirname(os.path.abspath(out))
    if not os.path.isdir(thu_muc):
        return 'thư mục của tệp kết quả “%s” không tồn tại' % out
    if os.path.isdir(out):
        return '“%s” là thư mục, không phải tệp kết quả' % out
    return None


def ghi_tep_an_toan(out, ghi):
    """Ghi qua tệp tạm cùng thư mục rồi thay thế một lần (os.replace): lỗi giữa chừng không để lại tệp dở dang, tệp cũ còn nguyên.
    ghi(path_tam) thực hiện việc ghi. → lỗi | None."""
    import os, tempfile
    thu_muc = os.path.dirname(os.path.abspath(out))
    try:
        fd, tam = tempfile.mkstemp(prefix='.ktc897_', suffix='.tmp', dir=thu_muc)
        os.close(fd)
    except OSError as e:
        return 'không tạo được tệp kết quả trong thư mục “%s” (%s)' % (thu_muc, e.strerror or e)
    try:
        ghi(tam)
        os.replace(tam, out)
        return None
    except (OSError, ValueError) as e:  # ValueError: dữ liệu không ghi được vào XML – báo lỗi, KHÔNG coi là thành công
        return 'không ghi được tệp kết quả “%s” (%s: %s)' % (out, type(e).__name__, (getattr(e, 'strerror', None) or str(e))[:160])
    finally:
        if os.path.exists(tam):
            try: os.remove(tam)
            except OSError: pass


def nfc(s):
    return unicodedata.normalize('NFC', s or '')


def _la_khoang_trang(ch):
    return ch in '\t\n\r\v\f' or unicodedata.category(ch) in ('Zs', 'Zl', 'Zp')


def chuan_trinh_bay(s):
    """NFC; bỏ ký tự định dạng vô hình (category Cf: zero-width, soft hyphen, BOM…); mọi khoảng trắng (Zs, Zl, Zp, tab, xuống dòng) → dấu cách;
    mọi dấu gạch nối/gạch ngang (category Pd) → '-'; gộp khoảng trắng liên tiếp."""
    out = []
    for ch in nfc(s):
        c = unicodedata.category(ch)
        if c == 'Cf':
            continue
        if _la_khoang_trang(ch):
            out.append(' ')
        elif c == 'Pd' or ch == '−':  # U+2212 (dấu trừ, category Sm) thường bị dùng thay gạch nối trong số hiệu
            out.append('-')
        else:
            out.append(ch)
    return re.sub(r' {2,}', ' ', ''.join(out)).strip()


def _ky_tu_ky_hieu(ch):
    """Ký tự có thể đứng sát dấu phân cách trong số, ký hiệu: chữ số hoặc chữ in hoa (theo thuộc tính Unicode)."""
    return bool(ch) and unicodedata.category(ch) in ('Nd', 'Lu')


def chuan_so_hieu(s):
    """chuan_trinh_bay + bỏ khoảng trắng TRÌNH BÀY quanh '/' và '-' trong vùng số, ký hiệu:
      “9090 / QĐ - CĐKT” → “9090/QĐ-CĐKT”; “208 - QĐ/TW” → “208-QĐ/TW”; “115/ VBHN-VPQH” → “115/VBHN-VPQH”.
    Chỉ gộp khi hai bên dấu là chữ số hoặc chữ in hoa; với '-' còn phải có '/' trong cùng cụm (≤ 12 ký tự) để không chạm lời văn
    (“Độc lập - Tự do - Hạnh phúc” giữ nguyên)."""
    t = chuan_trinh_bay(s)
    if '/' not in t and '-' not in t:
        return t
    chars = list(t)
    n = len(chars)
    keep = [True] * n
    for i, ch in enumerate(chars):
        if ch not in '/-':
            continue
        j = i - 1
        while j >= 0 and chars[j] == ' ':
            j -= 1
        k = i + 1
        while k < n and chars[k] == ' ':
            k += 1
        if j < 0 or k >= n or (j == i - 1 and k == i + 1):
            continue
        if not (_ky_tu_ky_hieu(chars[j]) and _ky_tu_ky_hieu(chars[k])):
            continue
        if ch == '-':
            vung = ''.join(chars[max(0, j - 12):j + 1]) + ''.join(chars[k:k + 12])
            if '/' not in vung:
                continue
        for x in range(j + 1, i):
            keep[x] = False
        for x in range(i + 1, k):
            keep[x] = False
    return ''.join(c for c, kp in zip(chars, keep) if kp)


def khong_dau(s):
    """Bỏ dấu tiếng Việt theo thuộc tính (NFD, bỏ dấu kết hợp Mn); Đ/đ → D/d; in hoa. Dùng để so tên tệp (“lần 2” = “lan 2”)."""
    t = unicodedata.normalize('NFD', nfc(s))
    t = ''.join(ch for ch in t if unicodedata.category(ch) != 'Mn')
    return t.replace('Đ', 'D').replace('đ', 'd').upper()


def la_in_hoa(s):
    """Dòng có ít nhất một chữ cái và KHÔNG có chữ thường (category Ll) – nhận đúng mọi chữ hoa có dấu tiếng Việt (KTS-26)."""
    t = nfc(s)
    co_chu = False
    for ch in t:
        c = unicodedata.category(ch)
        if c == 'Ll':
            return False
        if c.startswith('L'):
            co_chu = True
    return co_chu


def chuan_ten_luat(s):
    """Tên luật để so khớp: chuẩn trình bày, in hoa, chuẩn dấu phẩy, bỏ dấu câu cuối. Không cắt, không gộp tiền tố."""
    t = chuan_trinh_bay(s).upper()
    t = re.sub(r'\s*,\s*', ', ', t)
    t = re.sub(r'\s+', ' ', t).strip(' .;:,')
    return t


LOAI_KEM_TEN = ('QUY ĐỊNH', 'QUY CHẾ', 'ĐIỀU LỆ', 'NỘI QUY', 'KẾ HOẠCH', 'DANH MỤC', 'CHƯƠNG TRÌNH', 'ĐỀ ÁN', 'HƯỚNG DẪN', 'QUY TRÌNH')


def loai_tieu_de_kem(dong):
    """Tiêu đề văn bản kèm theo: dòng bắt đầu bằng tên loại (QUY ĐỊNH, DANH MỤC…) và toàn dòng in hoa theo thuộc tính Unicode.
    Dùng CHUNG cho văn bản kèm theo nằm trong tệp dự thảo và tệp riêng (KTS-26). Không giới hạn độ dài (ngưỡng 120 ký tự của
    bản rời v4.5.2 không có căn cứ nghiệp vụ – xem Vấn đề mở). Trả về tên loại hoặc None."""
    t = chuan_trinh_bay(dong)
    if not t or not la_in_hoa(t):
        return None
    for loai in sorted(LOAI_KEM_TEN, key=len, reverse=True):
        if t == loai or t.startswith(loai + ' '):
            return loai
    return None


def ngay_hop_le(y, m, d):
    import datetime
    try:
        datetime.date(int(y), int(m), int(d))
        return True
    except (ValueError, TypeError):
        return False


def _chuan_doi_chieu(s):
    t = chuan_trinh_bay(s).casefold()
    t = re.sub(r'[“”"«»‘’\']', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def tim_trich_dan(trich, van_ban):
    """Nguyên văn trích (có thể có “…” để lược) có nằm trong văn bản không. So sau khi chuẩn trình bày, không phân biệt hoa thường,
    bỏ dấu ngoặc kép. Mỗi đoạn tách bởi “…”/“...” phải có mặt theo đúng thứ tự. Trả về True/False."""
    phan = [p for p in re.split(r'…|\.\.\.', _chuan_doi_chieu(trich)) if p.strip(' .,;:')]
    if not phan:
        return False
    vb = _chuan_doi_chieu(van_ban)
    vt = 0
    for p in phan:
        p = p.strip(' ,;:')
        k = vb.find(p, vt)
        if k < 0:
            return False
        vt = k + len(p)
    return True


def doc_chu(path):
    """Toàn bộ chữ của một tệp để đối chiếu trích dẫn (v4.6 – KTS-13): .docx (thân, bảng, chú thích), .xlsx, .pdf có lớp chữ, .md/.txt.
    Lỗi đọc → None (người gọi phải coi là CHƯA đối chiếu được, không coi là có)."""
    import os, zipfile, subprocess, shutil
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == '.docx':
            with zipfile.ZipFile(path) as z:
                parts = []
                for nm in ('word/document.xml', 'word/footnotes.xml', 'word/endnotes.xml'):
                    if nm in z.namelist():
                        x = z.read(nm).decode('utf-8', 'ignore')
                        x = re.sub(r'<w:tab/>|<w:br/>|<w:br [^>]*/>', ' ', x)
                        x = re.sub(r'</w:p>', '\n', x)
                        parts.append(re.sub(r'<[^>]+>', '', x))
            import html
            return html.unescape('\n'.join(parts))
        if ext == '.xlsx':
            with zipfile.ZipFile(path) as z:
                import html
                return html.unescape(' '.join(re.sub(r'<[^>]+>', ' ', z.read(n).decode('utf-8', 'ignore')) for n in z.namelist() if n.startswith('xl/sharedStrings') or n.startswith('xl/worksheets/sheet')))
        if ext == '.pdf':
            if shutil.which('pdftotext') is None: return None
            return subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=120).stdout
        if ext in ('.md', '.txt'):
            return open(path, encoding='utf-8', errors='ignore').read()
    except Exception:
        return None
    return None


# ----------------------------------------------------------------------------
# v4.6.5 (YC mục 6): kiểm tra sớm môi trường THỰC SẼ DÙNG – đọc nguồn, tạo–đọc–ghi tệp tạm, tiến trình con, công cụ dựng trang.
# Mỗi phép thử ghi rõ bước, tệp, thời gian, lỗi; KHÔNG suy đoán nguyên nhân (chỉ nêu lỗi quan sát được).
# ----------------------------------------------------------------------------
def tien_do(msg):
    """Ghi tiến độ ra stderr khi KTC_TIEN_DO=1 (hoặc luôn khi gọi từ kiem_moi_truong) để không im lặng chờ lâu rồi chỉ báo “quá thời gian”."""
    import os, sys
    if os.environ.get('KTC_TIEN_DO') == '1':
        sys.stderr.write('[tiến độ] %s\n' % msg); sys.stderr.flush()


def kiem_moi_truong(nguon=None, thu_muc_lam_viec=None, thoi_han=20):
    """→ (ds, dat) ; ds = [(phép thử, 'ĐẠT'|'LỖI'|'THIẾU'|'CÓ', chi tiết, giây)]. dat=False nếu một phép BẮT BUỘC lỗi.
    nguon: danh sách tệp/thư mục sẽ đọc; thu_muc_lam_viec: nơi ghi tệp tạm (có thể nằm NGOÀI cây hồ sơ đầu vào)."""
    import os, sys, time, shutil, subprocess, tempfile
    ds, dat = [], True

    def ghi(ten, tt, ct, t0):
        ds.append((ten, tt, ct, round(time.time() - t0, 2)))
    # 1) đọc nguồn
    for p in (nguon or []):
        t0 = time.time()
        try:
            if os.path.isdir(p):
                n = sum(len(f) for _, _, f in os.walk(p)); ghi('đọc nguồn', 'ĐẠT', '%s (%d tệp)' % (p, n), t0)
            else:
                with open(p, 'rb') as f: f.read(4096)
                ghi('đọc nguồn', 'ĐẠT', p, t0)
        except OSError as e:
            dat = False; ghi('đọc nguồn', 'LỖI', '%s: %s' % (p, e.strerror or e), t0)
    # 2) tạo–đọc–ghi tệp tạm (ở thư mục chỉ định hoặc thư mục tạm hệ thống)
    nen = thu_muc_lam_viec or tempfile.gettempdir()
    t0 = time.time()
    try:
        os.makedirs(nen, exist_ok=True)
        d = tempfile.mkdtemp(prefix='ktc897_', dir=nen)
        try:
            f1 = os.path.join(d, 'thu.txt')
            with open(f1, 'w', encoding='utf-8') as f: f.write('kiểm tra ghi')
            with open(f1, 'a', encoding='utf-8') as f: f.write(' + ghi thêm')
            with open(f1, encoding='utf-8') as f: ok = f.read() == 'kiểm tra ghi + ghi thêm'
            os.remove(f1)
            ghi('tạo–đọc–ghi tệp tạm', 'ĐẠT' if ok else 'LỖI', nen if ok else 'đọc lại khác nội dung đã ghi: ' + nen, t0)
            dat = dat and ok
        finally:
            shutil.rmtree(d, ignore_errors=True)
    except OSError as e:
        dat = False; ghi('tạo–đọc–ghi tệp tạm', 'LỖI', '%s: %s' % (nen, e.strerror or e), t0)
    # 3) tiến trình con
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, '-c', 'print(1+1)'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=thoi_han)
        ok = r.returncode == 0 and r.stdout.strip() == '2'
        dat = dat and ok
        ghi('tiến trình con (Python)', 'ĐẠT' if ok else 'LỖI', sys.executable if ok else 'mã %s; %s' % (r.returncode, (r.stderr or '')[-200:]), t0)
    except subprocess.TimeoutExpired:
        dat = False; ghi('tiến trình con (Python)', 'LỖI', 'quá %ds' % thoi_han, t0)
    except OSError as e:
        dat = False; ghi('tiến trình con (Python)', 'LỖI', e.strerror or str(e), t0)
    # 4) công cụ (không bắt buộc, nhưng ảnh hưởng số trang/trích xuất)
    for c in ('pdftotext', 'pdfinfo', 'soffice', 'libreoffice'):
        t0 = time.time(); w = shutil.which(c)
        ghi('công cụ ' + c, 'CÓ' if w else 'THIẾU', w or '', t0)
    try:
        import docx  # noqa: F401
        ghi('python-docx', 'CÓ', '', time.time())
    except Exception:
        ghi('python-docx', 'THIẾU', '', time.time())
    # 5) Microsoft Word (phương án dựng trang khi thiếu LibreOffice) – chỉ báo có/không; thử THỰC mở–lưu–xuất ở dung_word_dung_trang
    w = word_san_co()
    ghi('Microsoft Word', 'CÓ' if w else 'THIẾU', w or 'không thấy WINWORD.EXE/COM trên máy chạy Skill', time.time())
    return ds, dat


def word_san_co():
    import os, shutil
    if os.name != 'nt': return None
    w = shutil.which('winword') or shutil.which('WINWORD.EXE')
    if w: return w
    for base in (os.environ.get('ProgramFiles'), os.environ.get('ProgramFiles(x86)')):
        if not base: continue
        for sub in ('Microsoft Office\\root\\Office16', 'Microsoft Office\\Office16', 'Microsoft Office\\Office15'):
            p = os.path.join(base, sub, 'WINWORD.EXE')
            if os.path.exists(p): return p
    return None


def dung_word_xuat_pdf(docx_path, pdf_path, thoi_han=180):
    """Phương án khi thiếu LibreOffice (chỉ Windows có Word): mở BẢN SAO bằng Word qua PowerShell COM, xuất PDF. → (ok, mô tả công cụ/lỗi).
    Không sửa tệp gốc; người gọi phải ghi “công cụ dựng trang: Microsoft Word” vào kết quả."""
    import subprocess, os
    if not word_san_co(): return False, 'không có Microsoft Word'
    ps = ("$w=New-Object -ComObject Word.Application;$w.Visible=$false;$w.DisplayAlerts=0;try{$d=$w.Documents.Open('%s',$false,$true);"
          "$d.ExportAsFixedFormat('%s',17);$d.Close($false)}finally{$w.Quit()}") % (docx_path.replace("'", "''"), pdf_path.replace("'", "''"))
    try:
        r = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=thoi_han)
        if r.returncode == 0 and os.path.exists(pdf_path): return True, 'Microsoft Word (COM)'
        return False, 'Word lỗi mã %s: %s' % (r.returncode, (r.stderr or '')[-200:])
    except subprocess.TimeoutExpired:
        return False, 'Word quá %ds' % thoi_han
    except OSError as e:
        return False, e.strerror or str(e)
