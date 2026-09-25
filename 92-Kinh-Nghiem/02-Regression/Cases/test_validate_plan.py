# -*- coding: utf-8 -*-
"""Hoi quy validate_plan.py + kpi_mau.ghi_ke_hoach — skill ktc-kpi-lap-ke-hoach.

Dung tep THAT tu mau trong 28-KTC-KPI/assets (ghi vao thu muc tam), cai loi tung loai roi kiem:
moi ma loi phai BAT dung ca sai va BO QUA ca sach (mot phep kiem hong luon bao sach).
Kiem them: ghi_ke_hoach khong ghi de mau, giu nguyen cong thuc sheet KPI, xoa dong vi du.
"""
import hashlib
import os
import shutil
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import kpi_calc as kc        # noqa: E402
import kpi_mau as km         # noqa: E402
import validate_plan as vp   # noqa: E402

sai = []
T = tempfile.mkdtemp(prefix="ktc_kpi_")


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


def ma(kq):
    return {x["ma"] for x in kq["loi"]}


def dv(truc, nd, **k):
    d = {"truc": truc, "noi_dung": nd, "cap_trinh": "Trưởng phòng", "muc_do": "Cao", "san_pham": "Báo cáo",
         "so_luong": 1, "thoi_han": "30/11/2026", "minh_chung": "Văn bản trên hệ thống Office"}
    d.update(k)
    return d


def lap(nhom, ds, ten, pa="muc-do", ca_nhan=None):
    kh = {"ca_nhan": ca_nhan or {"ho_ten": "Nguyễn Văn A", "don_vi": "Phòng TH-HC&QT"}, "dau_viec": ds}
    kh = dict(kh, dau_viec=kc.quy_doi_ke_hoach(kh, pa)["dau_viec"], phuong_an=pa)
    p = os.path.join(T, ten)
    km.ghi_ke_hoach(nhom, kh, p, "IV", "2026")
    return p


SACH = [dv(1, "Tổng hợp báo cáo công tác tháng của Trường", muc_do="Trung bình", so_luong=3),
        dv(2, "Góp ý dự thảo Quy chế chi tiêu nội bộ", muc_do="Thấp"),
        dv(3, "Số hóa hồ sơ lưu trữ năm 2025", muc_do="Khó và phức tạp", san_pham="Hồ sơ chuyên môn", so_luong=200),
        dv(4, "Tham gia sinh hoạt chi bộ định kỳ", muc_do="Thấp", san_pham="Biên bản", so_luong=3),
        dv(5, "Tham gia phong trào văn hóa, văn nghệ của Công đoàn", muc_do="Thấp", san_pham="Báo cáo"),
        dv(6, "Tham gia diễn tập phòng cháy, chữa cháy", muc_do="Thấp", san_pham="Biên bản")]

# --- mau khong bi ghi de; ban ra giu cong thuc
goc = km.tep_mau("hanh-chinh")
h0 = hashlib.sha256(open(goc, "rb").read()).hexdigest()
p = lap("hanh-chinh", SACH, "sach.xlsx")
kiem(hashlib.sha256(open(goc, "rb").read()).hexdigest() == h0, "ghi_ke_hoach: mẫu trong assets/ giữ nguyên byte")
wb = km.mo(p)
# Moi cong thuc cua mau con nguyen o dung o; cong thuc them chi la cot F (san pham ='Ke Hoach'!E<dong>, lenh sua
# 25/9/2026) — dung 1 o moi dau viec. (Truoc day dem cung "990" -> vo khi them cot F co chu dich.)
ct_mau = {c.coordinate: c.value for r in km.mo(goc)["KPI"].iter_rows() for c in r if str(c.value or "").startswith("=")}
ct_ra = {c.coordinate: c.value for r in wb["KPI"].iter_rows() for c in r if str(c.value or "").startswith("=")}
them_moi = {k: v for k, v in ct_ra.items() if k not in ct_mau}
kiem(len(ct_mau) == 990 and all(ct_ra.get(k) == v for k, v in ct_mau.items()),
     "ghi_ke_hoach: giữ nguyên đủ 990 công thức của mẫu, đúng ô")
kiem(len(them_moi) == len(SACH) and all(k.startswith("F") and "'Ke Hoach'!E" in v for k, v in them_moi.items()),
     f"công thức thêm mới chỉ là cột F sản phẩm, {len(them_moi)} ô = {len(SACH)} đầu việc")
try:
    km.ghi_ke_hoach("hanh-chinh", {"dau_viec": []}, os.path.join(km.thu_muc_mau(), "x.xlsx"))
    kiem(False, "NGƯỢC: ghi vào assets/ phải bị chặn")
except ValueError:
    kiem(True, "NGƯỢC: ghi vào assets/ bị chặn")

# --- ca sach
kq = vp.kiem(p, "hanh-chinh", "muc-do")
kiem(not [x for x in kq["loi"] if x["muc"] == "LOI"], f"Kế hoạch sạch → 0 LỖI ({sorted(ma(kq))})")
kiem("KH06" not in ma(kq), "Dòng ví dụ đã xóa → không báo KH06")
kiem(kq["nhom"] == "hanh-chinh" and vp.kiem(p)["nhom"] == "hanh-chinh", "Tự nhận nhóm từ tiêu đề sheet Đánh giá")

# --- mau nguyen ban (chua xoa vi du, chua dien ho ten)
t = os.path.join(T, "nguyen-ban.xlsx")
shutil.copyfile(goc, t)
kq = vp.kiem(t, "hanh-chinh", "muc-do")
kiem("KH06" in ma(kq), "NGƯỢC: mẫu nguyên bản → KH06 dòng ví dụ 'Bahnar' chưa xóa")
kiem("KH15" in ma(kq), "NGƯỢC: mẫu nguyên bản → KH15 chưa điền họ tên, đơn vị")
kiem("KH13" in ma(kq), "Mẫu Quý III: ô số Quyết định trống → KH13 (cảnh báo)")

# --- thieu san pham / thoi han / so luong
p = lap("hanh-chinh", SACH + [dv(1, "Việc thiếu sản phẩm", san_pham=""), dv(1, "Việc thiếu hạn", thoi_han=None)],
        "thieu.xlsx")
kq = vp.kiem(p, "hanh-chinh", "muc-do")
kiem({"KH01", "KH02"} <= ma(kq), "NGƯỢC: thiếu sản phẩm → KH01, thiếu thời hạn → KH02 (Đ12.4)")
wb = km.mo(p); wb["Ke Hoach"]["F14"].value = "vài"; wb.save(p)
kiem("KH03" in ma(vp.kiem(p, "hanh-chinh", "muc-do")), "NGƯỢC: số lượng 'vài' → KH03 không đo lường được")

# --- he so khong khop muc do
p = lap("hanh-chinh", SACH, "lech.xlsx")
wb = km.mo(p); wb["Ke Hoach"]["I14"].value = 2; wb.save(p)
kiem("KH05" in ma(vp.kiem(p, "hanh-chinh", "muc-do")), "NGƯỢC: mức 'Trung bình' mà hệ số 2 → KH05")
kiem("KH05" not in ma(vp.kiem(p, "hanh-chinh", "nhap-tay")), "Phương án nhập tay → không áp KH05")

# --- quan ly thieu Truc 4
khong4 = [d for d in SACH if d["truc"] != 4]
p = lap("truong-pho-don-vi", khong4, "ql.xlsx")
kiem("KH10" in ma(vp.kiem(p, "truong-pho-don-vi", "muc-do")), "NGƯỢC: Trưởng/Phó đơn vị không có Trục 4 → KH10 (Đ12.1)")
p = lap("hanh-chinh", khong4, "khong-ql.xlsx")
kq = vp.kiem(p, "hanh-chinh", "muc-do")
kiem("KH10" not in ma(kq) and "KH11" in ma(kq), "Không giữ chức vụ thiếu Trục 4 → không KH10, chỉ cảnh báo KH11")

# --- ket qua tap the
p = lap("hanh-chinh", SACH + [dv(1, "Bảo đảm 100% viên chức toàn khoa hoàn thành nhiệm vụ")], "tapthe.xlsx")
kiem("KH09" in ma(vp.kiem(p, "hanh-chinh", "muc-do")), "NGƯỢC: '100% viên chức toàn khoa' → KH09 (Đ4.8)")

# --- trung lap
p = lap("hanh-chinh", SACH + [dv(2, "Góp ý dự thảo Quy chế chi tiêu nội bộ", muc_do="Thấp")], "trung.xlsx")
kiem("KH14" in ma(vp.kiem(p, "hanh-chinh", "muc-do")), "NGƯỢC: đầu việc trùng nội dung → KH14 (Đ11.4a)")

# --- phuong an A: san pham ngoai Danh muc
ds_a = [dict(d, san_pham="Chiến lược, Đề án phát triển Trường giai đoạn trung, dài hạn") for d in SACH]
p = lap("hanh-chinh", ds_a, "phuong-an-A.xlsx", pa="A")
kiem("KH08" not in ma(vp.kiem(p, "hanh-chinh", "A")), "Phương án A, sản phẩm có trong Danh mục → không KH08")
wb = km.mo(p); wb["Ke Hoach"]["E14"].value = "Sản phẩm tự đặt"; wb.save(p)
kiem("KH08" in ma(vp.kiem(p, "hanh-chinh", "A")), "NGƯỢC: phương án A, sản phẩm ngoài Danh mục TB 1052 → KH08")

# --- vuot 20 dong / Truc
try:
    lap("hanh-chinh", [dv(1, f"Việc {i}") for i in range(21)], "21.xlsx")
    kiem(False, "NGƯỢC: 21 đầu việc/Trục phải bị chặn")
except ValueError:
    kiem(True, "NGƯỢC: 21 đầu việc trong 1 Trục bị chặn (không tự chèn dòng làm lệch công thức)")

# --- 6 mau deu doc duoc cau truc dung QD 1923
for n in km.NHOM:
    ct = km.cau_truc(km.mo(km.tep_mau(n)))
    kiem(len(ct["truc"]) == 6 and sum(ct["diem_truc"].values()) == 70 and ct["nhom_a"] == [13, 12, 5]
         and not kc.kiem_trong_so_truc(ct["diem_truc"], 1),
         f"Mẫu {n}: 6 Trục × 20 dòng, tổng 70, Trục chính ≥ 40%, nhóm chung 13/12/5")

shutil.rmtree(T, ignore_errors=True)
print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
