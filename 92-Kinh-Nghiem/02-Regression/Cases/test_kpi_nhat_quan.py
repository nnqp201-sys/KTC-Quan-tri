# -*- coding: utf-8 -*-
"""Hoi quy bo kiem nhat quan NQ01-NQ10 — skill ktc-kpi-tu-danh-gia (lenh 28/10/2026, muc 2.4).

Ca thu lay tu su co THAT cua phien lam ho so Quy III/2026:
  (a) B25: khai "Hoan thanh dung han" nhung % tien do 75, SL 5/7  -> NQ01 LOI
  (b) 7 viec khai "Vuot muc" khong co can cu                      -> NQ03
  (c) tu de xuat HTXS khi chi 8/30 viec vuot muc                  -> NQ04
  (d) bang hoi cu (v1.3, thieu 6 cot moi) van doc duoc, khong thanh LOI
  (e) mau Phu luc II/VII (so dong KPI khong khop Ke Hoach)        -> bao ro, ma thoat 2, KHONG KeyError
Va ca NGUOC: so lieu khop thi KHONG bao loi; "khong yeu cau minh chung" thi NQ07 im.
"""
import datetime
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import kpi_nhat_quan as nq      # noqa: E402
import kpi_danh_gia as kd       # noqa: E402

sai = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


def ma_co(ds, ma, muc=None):
    return any(m == ma and (muc is None or mc == muc) for m, mc, _ in ds)


def viec(ma="B01", truc=1, **kw):
    d = {"ma": ma, "truc": truc, "noi_dung": "Việc thử", "G": 1, "L": 1, "N": 100, "P": 100,
         "ket_qua": nq.DUNG_HAN, "so_hieu": "123/QĐ-CĐKT"}
    d.update(kw)
    return d


print("== (a) NQ01 — khai đúng hạn nhưng số liệu chưa trọn (ca B25 thật) ==")
b25 = viec("B25", noi_dung="Chỉ đạo mua sắm thuốc, hóa chất, vật tư y tế", G=7, L=5, N=75, P=75,
           ket_qua=nq.DUNG_HAN)
ds = nq.kiem({}, {}, [b25])
kiem(ma_co(ds, "NQ01", nq.LOI), "B25 khai 'Hoàn thành đúng hạn' với 75%, SL 5/7 → NQ01 LỖI")
kiem("SL thực 5 < SL kế hoạch 7" in " ".join(t for _, _, t in ds), "NQ01 nêu rõ cả hai lý do (tiến độ và số lượng)")
kiem(not ma_co(nq.kiem({}, {}, [viec("B25", G=7, L=5, N=75, P=75, ket_qua=nq.CHAM)]), "NQ01"),
     "NGƯỢC: khai 'Hoàn thành chậm tiến độ' với cùng số liệu → NQ01 im (đúng như hồ sơ đã sửa)")
kiem(not ma_co(nq.kiem({}, {}, [viec()]), "NQ01"), "NGƯỢC: số liệu trọn vẹn → NQ01 im")

print("== (b) NQ03 — 'Vượt mức' không có căn cứ ==")
vm = [viec(f"B{i}", ket_qua=nq.VUOT) for i in range(18, 25)]
ds = nq.kiem({}, {}, vm)
kiem(sum(1 for m, mc, _ in ds if m == "NQ03" and mc == nq.LOI) == 7, "7 việc 'Vượt mức' thiếu căn cứ → 7 lỗi NQ03")
kiem(not ma_co(nq.kiem({}, {}, [viec(ket_qua=nq.VUOT, loai_vuot="số lượng",
                                     can_cu_vuot="Kế hoạch 1, thực hiện 3 báo cáo")]), "NQ03"),
     "NGƯỢC: có Loại vượt + Căn cứ kèm số liệu → NQ03 im")
kiem(ma_co(nq.kiem({}, {}, [viec(ket_qua=nq.VUOT, loai_vuot="rất tốt", can_cu_vuot="vượt nhiều")]), "NQ03"),
     "NGƯỢC: Loại vượt ngoài 4 giá trị cho phép → vẫn bắt NQ03")

print("== (c) NQ04 — tự đề xuất HTXS khi tỷ lệ vượt mức dưới 30% ==")
ds30 = [viec(f"B{i}", ket_qua=nq.VUOT, loai_vuot="số lượng", can_cu_vuot="Kế hoạch 1, thực hiện 2")
        for i in range(8)] + [viec(f"C{i}") for i in range(22)]
ds = nq.kiem({}, {}, ds30, tu_de_xuat=nq.HTXS)
kiem(ma_co(ds, "NQ04", nq.LOI), "8/30 vượt mức (26,67%) + tự đề xuất HTXS → NQ04 LỖI")
kiem(not ma_co(nq.kiem({}, {}, ds30, tu_de_xuat="Hoàn thành tốt nhiệm vụ"), "NQ04"),
     "NGƯỢC: không tự đề xuất HTXS → NQ04 im")
ds9 = [viec(f"B{i}", ket_qua=nq.VUOT, loai_vuot="số lượng", can_cu_vuot="Kế hoạch 1, thực hiện 2")
       for i in range(9)] + [viec(f"C{i}") for i in range(21)]
kiem(not ma_co(nq.kiem({}, {}, ds9, tu_de_xuat=nq.HTXS), "NQ04"), "NGƯỢC: 9/30 = 30% → NQ04 im (biên)")

print("== NQ02, NQ05, NQ06, NQ07 ==")
kiem(ma_co(nq.kiem({}, {}, [viec(ket_qua=nq.CHAM, P=100)]), "NQ02", nq.CANH_BAO),
     "NQ02: khai chậm tiến độ nhưng % tiến độ = 100 → cảnh báo")
muon = viec(ket_qua=nq.VUOT, loai_vuot="tiến độ", can_cu_vuot="Hoàn thành sớm 5 ngày",
            thoi_han=datetime.date(2026, 9, 21), ngay_hoan_thanh=datetime.date(2026, 9, 30))
kiem(ma_co(nq.kiem({}, {}, [muon]), "NQ05", nq.LOI), "NQ05: 'Vượt mức' mà hoàn thành sau thời hạn → LỖI")
kiem(not ma_co(nq.kiem({}, {}, [dict(muon, thoi_han="Quý III/2026")]), "NQ05"),
     "NGƯỢC: thời hạn dạng 'Quý III/2026' không so được ngày → NQ05 im, không đoán")
kiem(ma_co(nq.kiem({}, {}, [viec(minh_chung="Văn bản DỰ THẢO")], ban_nop=True), "NQ06", nq.LOI),
     "NQ06: còn 'DỰ THẢO' trong bản nộp → LỖI")
kiem(ma_co(nq.kiem({}, {}, [viec(minh_chung="Văn bản DỰ THẢO")]), "NQ06", nq.CANH_BAO),
     "NQ06: bản nội bộ chỉ cảnh báo")
kiem(ma_co(nq.kiem({}, {}, [viec(so_hieu=None, minh_chung=None)]), "NQ07", nq.CANH_BAO),
     "NQ07: không số hiệu, không lý do → cảnh báo")
kiem(not ma_co(nq.kiem({}, {}, [viec(so_hieu=None, minh_chung=None,
                                     ly_do_chua="Việc thường xuyên, không yêu cầu minh chứng")]), "NQ07"),
     "NGƯỢC: ghi 'không yêu cầu minh chứng' → NQ07 im")

print("== NQ08, NQ09, NQ10 ==")
v1 = viec("B01", G=2, L=2, N=100, P=100)
v1["J"], v1["tb"] = 2.0, 2.0
kiem(ma_co(nq.kiem({}, {}, [v1], truc={1: {"pt": 80.0}}), "NQ08", nq.LOI),
     "NQ08: % Trục ghi 80% trong khi tính lại 100% → LỖI")
kiem(not ma_co(nq.kiem({}, {}, [v1], truc={1: {"pt": 100.0}}), "NQ08"), "NGƯỢC: khớp → NQ08 im")
kiem(ma_co(nq.kiem({}, {"_muc_theo_diem": "Hoàn thành tốt nhiệm vụ", "C": {}}, [viec()], tu_de_xuat=nq.HTXS),
           "NQ09", nq.CANH_BAO), "NQ09: tự đề xuất cao hơn mức theo ngưỡng điểm → cảnh báo")
tl10 = {"C": {"C08": "Có"}}
kiem(ma_co(nq.kiem({}, tl10, [viec("B01"), viec("B25", G=7, L=5, N=75, P=75, ket_qua=nq.CHAM)]), "NQ10"),
     "NQ10: C08 khai 'Có' nhưng còn việc chưa trọn → cảnh báo, nêu cả hai")
kiem(not ma_co(nq.kiem({}, tl10, [viec("B01"), viec("B02")]), "NQ10"), "NGƯỢC: mọi việc trọn 100% → NQ10 im")

print("== suy_c08 — nguồn của C08, C09 ==")
sy = nq.suy_c08([viec("B01"), viec("B25", G=7, L=5, N=75, P=75, ket_qua=nq.CHAM, ly_do_chua="Khách quan: chờ báo giá")])
kiem(sy["tong"] == 2 and sy["tron"] == 1 and sy["ket_luan"] == "Không", "suy_c08 đếm đúng 1/2 trọn, kết luận 'Không'")
kiem(sy["chua_tron"][0][2] == "Khách quan: chờ báo giá", "suy_c08 giữ nguyên văn lý do người dùng ghi")
kiem(nq.suy_c08([viec("B01", L=None)])["ket_luan"] is None, "NGƯỢC: thiếu số liệu → không kết luận, không đoán")

print("== (d) bảng hỏi cũ v1.3 vẫn đọc được ==")
BH = os.path.join(GOC, "30-Ket-Qua", "2026-10-01", "KPI-ca-nhan", "Ho-so-ra-soat-Q3-NNQ.Phuc",
                  "Bang-hoi-TDG-Q3-2026_Nguyen-Ngoc-Quang-Phuc.xlsx")
if os.path.exists(BH):
    tl = kd.doc_bang_hoi(BH)
    kiem(tl["ban_cu"] is True and len(tl["B"]) > 10, "Bảng hỏi v1.3 đọc được, nhận ra là bản cũ")
    kiem(all(tl["B"][m]["loai_vuot"] is None for m in tl["B"]), "Cột mới của bản cũ trả về None, không vỡ")
    ds = nq.kiem({}, tl, [viec(ket_qua=nq.VUOT)], ban_cu=True)
    kiem(ma_co(ds, "NQ03", nq.CANH_BAO) and not ma_co(ds, "NQ03", nq.LOI),
         "Bản cũ: NQ03 hạ xuống CẢNH_BÁO, không chặn người dùng")
else:
    print("  ! bỏ qua (d): không có hồ sơ Q3 trong 30-Ket-Qua")

print("== (e) mẫu Phụ lục II/VII — báo rõ, không KeyError ==")
KH = os.path.join(GOC, "30-Ket-Qua", "2026-10-01", "KPI-ca-nhan", "Ho-so-ra-soat-Q3-DT.Cong",
                  "TDG-KPI-Q3-2026_Do-Thanh-Cong.xlsx")
if os.path.exists(KH):
    try:
        kd.doc_ke_hoach(KH)
        kiem(False, "Mẫu Phụ lục II/VII phải dừng, không đọc tiếp")
    except kd.Dung as e:
        kiem("Phụ lục II/VII" in str(e) and "CHƯA HỖ TRỢ TỰ ĐỘNG" in str(e),
             "Mẫu lạ → thông báo rõ 'Phụ lục II/VII — chưa hỗ trợ tự động'")
        kiem("dòng 18" in str(e), "Thông báo chỉ đúng dòng việc không khớp (dòng 18)")
    except KeyError as e:
        kiem(False, f"Vẫn còn KeyError: {e}")
    kiem(kd.main(["sinh-bang-hoi", "--ke-hoach", KH, "--ra",
                  os.path.join(os.environ.get("TEMP", "."), "_bo.xlsx")]) == 2, "Mã thoát 2 với mẫu lạ")
else:
    print("  ! bỏ qua (e): không có hồ sơ Q3 trong 30-Ket-Qua")

print("\n" + ("ĐẠT: 0 ca sai" if not sai else f"KHÔNG ĐẠT: {len(sai)} ca sai\n- " + "\n- ".join(sai)))
sys.exit(1 if sai else 0)
