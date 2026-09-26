# -*- coding: utf-8 -*-
"""Hoi quy kpi_calc.py — skill ktc-kpi-lap-ke-hoach (lenh sua 24/9/2026, muc 8).

Ca bien moi nguong xep loai [QD 1923 D19.1], tran 100% [D11.6], truc chinh 40% [D12.3], nhom tieu chi chung
05 diem [D10.4], muc trong tam [D18], va ca NGUOC: goi thieu phuong an he so phai BAO LOI, khong tu chon;
san pham khong co trong Danh muc TB 1052 phai BAO LOI, khong tu gan A.
"""
import os
import sys

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import kpi_calc as kc  # noqa: E402

sai = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


def bao_loi(f, *a):
    try:
        f(*a)
    except kc.LoiKPI as e:
        return str(e)
    return None


# Xep loai theo diem — bien
for t, muc in ((100, "Hoàn thành xuất sắc"), (90, "Hoàn thành xuất sắc"), (89.99, "Hoàn thành tốt"),
               (70, "Hoàn thành tốt"), (69.99, "Hoàn thành nhiệm vụ"), (50, "Hoàn thành nhiệm vụ"),
               (49.99, "Không hoàn thành"), (0, "Không hoàn thành")):
    kiem(kc.xep_loai_theo_diem(t)["muc_theo_diem"].startswith(muc), f"Đ19.1: {t} điểm → {muc}")
kiem(bao_loi(kc.xep_loai_theo_diem, 100.01) is not None, "Đ19.1: tổng > 100 bị chặn (ngoài thang)")
kiem("chưa kiểm" in kc.xep_loai_theo_diem(95)["luu_y"], "Xếp loại theo điểm luôn kèm lưu ý điều kiện chưa kiểm")

# Diem chi tieu — tran 100%
d = kc.diem_chi_tieu(130, 45)
kiem(d["diem"] == 45 and abs(d["vuot_muc"] - 30) < 1e-9, "Đ11.6: 130% × 45 điểm → 45 (trần), ghi nhận vượt 30%")
kiem(kc.diem_chi_tieu(100, 45)["diem"] == 45, "Đ11.6: 100% → đủ điểm tối đa")
kiem(abs(kc.diem_chi_tieu(80, 45)["diem"] - 36) < 1e-9, "Đ11.6: 80% × 45 = 36")

# Truc chinh 40%
ok = kc.kiem_trong_so_truc({1: 28, 2: 14, 3: 14, 4: 14}, 1)
kiem(not ok, "Đ12.3: Trục chính 28/70 = 40,00% → đạt")
lech = kc.kiem_trong_so_truc({1: 27.993, 2: 14.007, 3: 14, 4: 14}, 1)
kiem(any(m == "KP02" for m, *_ in lech), "Đ12.3: Trục chính 39,99% → báo KP02")
kiem(any(m == "KP01" for m, *_ in kc.kiem_trong_so_truc({1: 40, 2: 20}, 1)), "Đ11.3: tổng 60 ≠ 70 → báo KP01")

# Nhom tieu chi chung
kiem(not kc.kiem_tieu_chi_chung([13, 12, 5]), "Đ10.4: 13/12/5 (mẫu Quý III) → đạt")
kiem(any(m == "KP04" for m, *_ in kc.kiem_tieu_chi_chung([15.01, 10, 4.99])), "Đ10.4: nhóm 4,99 điểm → báo KP04")
kiem(any(m == "KP05" for m, *_ in kc.kiem_tieu_chi_chung([15, 12, 5])), "Đ10.4: tổng 32 > 30 → báo KP05")

# Muc do tieu chi chung, trong tam
kiem([kc.muc_tieu_chi_chung(x) for x in (90, 89.99, 70, 69.99, 50, 49.99)] == [1, 2, 2, 3, 3, 4], "Đ10.5: 4 mức, biên")
kiem([kc.muc_trong_tam(x) for x in (90, 89.99, 60, 59.99)] == [1, 2, 2, 3], "Đ18: 3 mức, biên 90/60")

# He so — KHONG co mac dinh
kiem(bao_loi(kc.he_so, None, "Cao") is not None, "NGƯỢC: gọi hệ số thiếu phương án → báo lỗi, không tự chọn")
kiem(bao_loi(kc.he_so, "mac-dinh", "Cao") is not None, "NGƯỢC: phương án lạ → báo lỗi")
for chu, v in (("Thấp", 1.0), ("Trung bình", 1.2), ("Cao", 1.5), ("Khó và phức tạp", 2.0),
               ("Thường xuyên, nhiệm vụ chủ yếu là thống kê (mức độ thấp)", 1.0),
               ("Phân tích, đánh giá số liệu, không quá khó và phức tạp (mức độ cao)", 1.5)):
    kiem(kc.he_so("muc-do", chu)["he_so"] == v, f"PL II QĐ 1923: '{chu[:40]}' → {v}")
kiem(bao_loi(kc.he_so, "muc-do", "Rất khó") is not None, "NGƯỢC: mức độ ngoài 4 mức → báo lỗi, không đoán")
kiem("Có văn bản" in kc.he_so("muc-do", "Cao")["trang_thai"], "Phương án mức độ ghi trạng thái 'Có văn bản'")

# He so A / AxB — Danh muc TB 1052
h = kc.he_so("A", san_pham="1.1")
kiem(h["he_so"] == 4.5 and "DỰ THẢO" in h["trang_thai"], "TB 1052 STT 1.1 (Đề án phát triển) → A = 4,5, ghi DỰ THẢO")
h = kc.he_so("AxB", "Khó và phức tạp", "1.1")
kiem(h["he_so"] == 9.0 and "CHƯA CÓ VĂN BẢN" in h["trang_thai"], "A×B: 4,5 × 2,0 = 9,0 (khớp ví dụ trong QUY-UOC), ghi CHƯA CÓ VĂN BẢN")
kiem(any("lệch" in c for c in kc.he_so("A", san_pham="1.3")["canh_bao"]), "TB 1052 STT 1.3 (Nhóm 2, hệ số 1,5) → cảnh báo lệch Nhóm")
kiem(any("bất thường" in c for c in kc.he_so("A", san_pham="29.22")["canh_bao"]), "TB 1052 STT 29.22 hệ số 50 → cảnh báo bất thường")
kiem(any(c.startswith("THANG_DIEM_CHUA_PHAN_DINH") for c in kc.he_so("A", san_pham="1.1")["canh_bao"]), "Phương án A (dự thảo TB 1052) → mã THANG_DIEM_CHUA_PHAN_DINH")
kiem(any(c.startswith("THANG_DIEM_CHUA_PHAN_DINH") for c in kc.he_so("AxB", "Cao", "1.1")["canh_bao"]), "Phương án A×B → mã THANG_DIEM_CHUA_PHAN_DINH")
kiem(not kc.he_so("muc-do", "Cao")["canh_bao"], "ca ngược: phương án mức độ (QĐ 1923 có văn bản) → không cảnh báo thang điểm")
kiem(bao_loi(kc.he_so, "A", None, "Sản phẩm không có trong danh mục") is not None,
     "NGƯỢC: sản phẩm không có trong Danh mục TB 1052 → báo lỗi, không tự gán A")
kiem(bao_loi(kc.he_so, "nhap-tay", None, None, None) is not None, "NGƯỢC: nhập tay thiếu hệ số → báo lỗi")

# Goi y Danh muc — chi liet ke, khong tu gan
import re  # noqa: E402
g = kc.tim_danh_muc("học lại")
kiem(g and all({"hoc", "lai"} <= set(re.findall(r"\w+", kc._kd(x["ten"] + " " + kc.danh_muc()["stt:" + x["stt"]]["mo_ta"])))
               for x in g), f"Gợi ý Danh mục: mọi dòng trả về chứa đủ từ khóa ({[x['stt'] for x in g]})")
kiem(all("thien" not in kc._kd(x["ten"]) or "thi" in re.findall(r"\w+", kc._kd(x["ten"]))
         for x in kc.tim_danh_muc("thi")), "NGƯỢC: từ 'thi' không khớp nhầm vào 'cải thiện' (so từ nguyên vẹn)")
kiem(kc.tim_danh_muc("từ khóa không tồn tại xyz") == [], "NGƯỢC: từ khóa không có → danh sách rỗng, không đoán gần đúng")

# So luong quy doi
kiem(kc.so_luong_quy_doi(3, 1.2) == 3.6, "SL quy đổi = 3 × 1,2 = 3,6 (mẫu: J = G × I)")
kiem(bao_loi(kc.so_luong_quy_doi, None, 1.2) is not None, "NGƯỢC: số lượng trống → báo lỗi (Đ12.4 đo lường được)")

# Bao mat (QD 1923 D23.2; lenh sua muc 6.1): thu muc KPI ca nhan khong vao git -> ktc_backup_github.py (git add -A)
# khong day len GitHub. Kiem ca nguoc: thu muc ket qua khac van duoc theo doi.
import subprocess  # noqa: E402


def bi_bo_qua(rel):
    return subprocess.run(["git", "-C", GOC, "check-ignore", "-q", rel]).returncode == 0


kiem(bi_bo_qua("30-Ket-Qua/2026-10-05/KPI-ca-nhan/KH-KPI-Q4-2026_nguyen-van-a.xlsx"),
     "Bảo mật: 30-Ket-Qua/<ngày>/KPI-ca-nhan/ bị git bỏ qua (không sao lưu GitHub)")
kiem(not bi_bo_qua("30-Ket-Qua/2026-10-05/De-xuat/x.md"), "NGƯỢC: thư mục kết quả khác vẫn được git theo dõi")

print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
