# -*- coding: utf-8 -*-
"""kiem_kieu_du_lieu.py – kiểm KIỂU và CẤU TRÚC dữ liệu báo cáo (du_lieu.json) TRƯỚC mọi bước xử lý của tao_bao_cao.py (v4.6.2 – F01, F02).

Nguyên nhân gốc F01/F02 (nghiệm thu độc lập lần 2): trình dựng dùng trực tiếp giá trị người nhập (.strip(), duyệt, nối, băm, so regex)
mà không kiểm kiểu → danh sách/đối tượng/số/null gây TypeError, AttributeError (Traceback) hoặc được coi là “có nội dung” (mo_ta là
danh sách vẫn HỢP LỆ). Mô-đun này khai báo MỘT bảng hợp đồng kiểu cho mọi trường trình dựng đọc – kể cả đối tượng lồng và phần tử
danh sách – và trả về danh sách lỗi có ĐƯỜNG DẪN TRƯỜNG (chỉ số danh sách đếm từ 1) và KIỂU HỢP LỆ. Có lỗi kiểu → trình dựng dừng có
kiểm soát, không dựng tệp.

Quy ước null (tạm thời – bảng hợp đồng kiểu trường tùy chọn đang CHỜ người phụ trách quyết định, xem F12):
- Trường đơn (chuỗi, số, đúng/sai) mang null → coi như KHÔNG CÓ trường (hành vi v4.6.1: `(x or '')`), không báo lỗi kiểu;
  trường bắt buộc vẫn bị các kiểm “thiếu trường” hiện hành từ chối.
- Trường danh sách/đối tượng mang null → LỖI KIỂU (v4.6.1 gây Traceback), TRỪ `chua_kiem` (v4.6.1 nhận null ở --chi-kiem) – giữ nhận,
  coi như danh sách rỗng.
- `hoi_quy` chỉ được kiểm khi `che_do` = “ĐC” (ngoài ĐC trường này không được dùng – giữ hành vi v4.6.1).
Khóa bắt đầu “_” không kiểm kiểu ở đây (khóa chú thích tự do; khóa dành cho script do khoa_danh_rieng() kiểm).

v4.6.3 (nghiệm thu độc lập lần 3): quy ước null ở trên là bảng D7 ĐÃ QUYẾT ĐỊNH (phiếu 02/11/2026), không còn “tạm thời”.
- Chuỗi số (`so_anh_da_xem`) chỉ nhận chữ số ASCII 0–9 (≤ 6 chữ số): chữ số Unicode khác (“²”, “٣”, “３”) bị từ chối thay vì để int() vỡ;
  số nguyên ≤ 10^6; true/false không phải số.
- Trường bắt buộc CÓ NỘI DUNG được kiểm SAU chuẩn hóa khoảng trắng (nhan_dien_chung.noi_dung: bỏ zero-width, mọi khoảng trắng Unicode):
  chỉ gồm khoảng trắng/ký tự vô hình → coi như trống. Trường tùy chọn/null theo D7 giữ nguyên là tùy chọn."""
import re
import nhan_dien_chung as ND

S, MUC, SO_NGUYEN, INT_STR, BOOL = 'chuoi', 'muc', 'so_nguyen', 'so_hoac_chuoi', 'dung_sai'


def L(x): return ('list', x)


def O(fields, bat_buoc=()): return ('obj', fields, tuple(bat_buoc))


def M(x): return ('map', x)  # đối tượng có khóa tự do, mọi giá trị cùng kiểu x


PH = O({'ma': S, 'muc': MUC, 'vi_tri': S, 'mo_ta': S, 'kien_nghi': S, 'nguyen_van_du_thao': S, 'can_cu': S, 'nguyen_van_can_cu': S,
        'chac_chan': S, 'thu_cong_ly_do': S, 'nhom': S})
MT = O({'chu_de': S, 'du_thao_vi_tri': S, 'du_thao_nguyen_van': S, 'vblq': S, 'vblq_nguyen_van': S, 'ket_qua': S, 'ma_phat_hien': S,
        'yeu_to_khop': M(S), 'giai_trinh_khop': M(S), 'nguyen_van_thay_the': S, 'vblq_thay_the': S, 'trong_yeu': BOOL})
DAT = O({'nhom': S, 'noi_dung': S, 'nguyen_van': S, 'so_do': S, 'nguon': S, 'vi_tri': S})
CK = O({'noi_dung': S, 'ly_do': S, 'trong_yeu': BOOL, 'nguoi_xac_minh': S}, bat_buoc=('noi_dung', 'ly_do'))  # v4.6.1 dựng .docx đọc x['noi_dung'], x['ly_do']
XA = O({'tep': S, 'so_anh_da_xem': SO_NGUYEN, 'ket_luan': S, 'mo_ta': S})
DC = O({'ma_cu': S, 'noi_dung_cu': S, 'vi_tri_hien_hanh': S, 'nguyen_van_hien_hanh': S, 'trang_thai': S, 'muc_con_lai': S,
        'ma_phat_hien': S, 'can_cu_dung': S})
HQ = O({'ma_cu': S, 'ket_qua': S})
BQ = O({'tep': S, 'ma': S, 'vi_tri': S, 'ly_do': S, 'nguyen_van': S})
KT = O({'hang_muc': S, 'ket_qua': S})
GOC = O({'ten_du_thao': S, 'loai_van_ban': S, 'don_vi_soan_thao': S, 'nguoi_kiem_tra': S, 'he': S, 'tac_vu': S, 'kieu_bao_cao': S,
         'che_do': S, 'lan_ra_soat': INT_STR, 'ngay_ra_soat': S, 'pham_vi': S, 'ghi_chu': S, 'rui_ro': S, 'kien_nghi_chung': S, 'kha_thi': S,
         'yeu_cau_doc_lap': S, 'da_ban_hanh': BOOL, 'tai_lieu_da_dung': L(S), 'uu_tien': L(S),
         'phat_hien': L(PH), 'ma_tran': L(MT), 'dat': L(DAT), 'chua_kiem': L(CK), 'xem_anh': L(XA), 'doi_chieu': L(DC), 'hoi_quy': L(HQ),
         'bo_qua_the_thuc': L(BQ), 'kiem_tra_chat_luong': L(KT), 'so_sanh': O({'ket_luan': S})})
NULL_LA_RONG = {'chua_kiem'}  # F12 – D7 đã quyết định 02/11/2026 (giữ hành vi v4.6.1)
CHI_KIEM_KHI_DC = {'hoi_quy'}


def ten_kieu(t):
    if isinstance(t, tuple):
        if t[0] == 'list': return 'danh sách [ %s ]' % ten_kieu(t[1])
        if t[0] == 'map': return 'đối tượng {khóa: %s}' % ten_kieu(t[1])
        return 'đối tượng {…}'
    return {S: 'chuỗi', MUC: 'số nguyên 1–4 hoặc chuỗi “Mức n”', SO_NGUYEN: 'số nguyên 0–1.000.000 (hoặc chuỗi chữ số ASCII 0–9)', INT_STR: 'số nguyên hoặc chuỗi',
            BOOL: 'true/false'}[t]


def ten_gia_tri(v):
    if v is None: return 'null'
    if isinstance(v, bool): return 'true/false'
    if isinstance(v, int): return 'số nguyên'
    if isinstance(v, float): return 'số thực'
    if isinstance(v, str): return 'chuỗi'
    if isinstance(v, list): return 'danh sách'
    if isinstance(v, dict): return 'đối tượng'
    return type(v).__name__


def _vo_huong(v, t):
    if t == S: return isinstance(v, str)
    if t == BOOL: return isinstance(v, bool)
    if t in (MUC, INT_STR): return isinstance(v, str) or (isinstance(v, int) and not isinstance(v, bool))
    if t == SO_NGUYEN:  # v4.6.3: miền giá trị khớp phép chuyển int() của trình dựng – chỉ chữ số ASCII
        return (isinstance(v, int) and not isinstance(v, bool) and 0 <= v <= 10 ** 6) or (isinstance(v, str) and re.fullmatch(r'[0-9]{1,6}', v.strip()) is not None)
    return False


def _kiem(v, t, duong, loi, chuan):
    """chuan: danh sách (cha, khóa) của trường đơn mang null – trình dựng xóa đi (null ≡ không có)."""
    if isinstance(t, tuple):
        if t[0] == 'list':
            if not isinstance(v, list):
                loi.append('Trường “%s”: phải là %s (hiện là %s).' % (duong, ten_kieu(t), ten_gia_tri(v))); return
            for i, x in enumerate(v, 1):
                _kiem(x, t[1], '%s[%d]' % (duong, i), loi, chuan)
            return
        if not isinstance(v, dict):
            loi.append('Trường “%s”: phải là %s (hiện là %s).' % (duong, ten_kieu(t), ten_gia_tri(v))); return
        if t[0] == 'map':
            for k, x in v.items():
                if isinstance(k, str) and k.startswith('_'): continue
                if x is None and not isinstance(t[1], tuple): chuan.append((v, k)); continue
                _kiem(x, t[1], '%s.%s' % (duong, k), loi, chuan)
            return
        fields, bat_buoc = t[1], t[2]
        for k in bat_buoc:
            if v.get(k) is None:
                loi.append('Trường “%s.%s”: thiếu (bắt buộc, phải là %s).' % (duong, k, ten_kieu(fields[k])))
            elif isinstance(v.get(k), str) and not ND.co_noi_dung(v[k]):  # v4.6.3 (mục 5): chỉ có khoảng trắng/ký tự vô hình = trống
                loi.append('Trường “%s.%s”: trống sau khi bỏ khoảng trắng/ký tự vô hình (bắt buộc có nội dung).' % (duong, k))
        for k, tk in fields.items():
            if k not in v or k in bat_buoc and v.get(k) is None: continue
            x = v[k]
            if x is None and not isinstance(tk, tuple): chuan.append((v, k)); continue
            _kiem(x, tk, '%s.%s' % (duong, k), loi, chuan)
        return
    if not _vo_huong(v, t):
        loi.append('Trường “%s”: phải là %s (hiện là %s%s).' % (duong, ten_kieu(t), ten_gia_tri(v), (' ' + repr(v)[:30]) if isinstance(v, (bool, int, float)) else ''))


def kiem_du_lieu(d):
    """→ (danh sách lỗi kiểu, hàm chuẩn hóa null). Lỗi rỗng ↔ mọi trường trình dựng đọc đúng kiểu."""
    loi, chuan = [], []
    if not isinstance(d, dict):
        return ['Dữ liệu gốc: phải là đối tượng JSON {…} theo assets/Mau-Du-Lieu-Bao-Cao.json (hiện là %s).' % ten_gia_tri(d)], lambda: None
    fields = GOC[1]
    che_do = d.get('che_do') if isinstance(d.get('che_do'), str) else None
    for k, tk in fields.items():
        if k not in d: continue
        if k in CHI_KIEM_KHI_DC and che_do != 'ĐC': continue
        x = d[k]
        if x is None:
            if k in NULL_LA_RONG or not isinstance(tk, tuple): chuan.append((d, k)); continue
        _kiem(x, tk, k, loi, chuan)

    # v4.6.3 (mục 5): trường gốc bắt buộc có nội dung và phần tử danh sách bắt buộc có nội dung – kiểm sau chuẩn hóa khoảng trắng
    for k in ('ten_du_thao', 'loai_van_ban', 'don_vi_soan_thao', 'nguoi_kiem_tra'):
        if isinstance(d.get(k), str) and not ND.co_noi_dung(d[k]):
            loi.append('Trường “%s”: trống sau khi bỏ khoảng trắng/ký tự vô hình (bắt buộc có nội dung).' % k)
    if isinstance(d.get('uu_tien'), list):
        for i, x in enumerate(d['uu_tien'], 1):
            if isinstance(x, str) and not ND.co_noi_dung(x):
                loi.append('Trường “uu_tien[%d]”: trống sau khi bỏ khoảng trắng/ký tự vô hình – mỗi vấn đề ưu tiên phải có nội dung.' % i)

    def ap_dung():
        for cha, k in chuan:
            if cha.get(k) is None: cha.pop(k, None)
    return loi, ap_dung
