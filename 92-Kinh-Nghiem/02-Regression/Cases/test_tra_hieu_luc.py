# -*- coding: utf-8 -*-
"""Hoi quy tra_hieu_luc.py — DL-20260919-004. Kho gia trong thu muc tam, khong phu thuoc Drive.

Ca thu nguoc lay tu loi that 19/9/2026:
- "Nghi dinh 85/2025" tung khop nham tep "275-2025 sua doi ND 85"
- "Thong tu 36/2026/TT-BXD" tung khop nham "Quyet dinh 36/2026/QD-TTg" (vi "TT" nam trong "TTG")
- QD 1951 (07/9/2026) dan Luat Xay dung ma metadata kho ghi het hieu luc tu 01/7/2026
- So hieu van ban Dang dang "198-KL/TW", "366-QD/TW", "05-HD/VPTW" bi bo sot hoan toan (khong trich duoc
  dong nao) vi RE_SO chi nhan dang gach cheo; loai "Ket luan" cung chua co trong LOAI/TU_LOAI (20/9/2026)
"""
import os
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import tra_hieu_luc as t  # noqa: E402

sai = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


KHO = tempfile.mkdtemp(prefix="ktc_kho_")
tep = {
    "01-Legal-Database/01-04/14. Nghị-định-85-2025-NĐ-CP hướng dẫn Luat dau tu cong.docx": None,
    "01-Legal-Database/01-04/14. Nghị-định-275-2025-NĐ-CP sua doi ND 85.docx": None,
    "01-Legal-Database/01-04/23. Quyết-định-36-2026-QĐ-TTg Tieu chi.docx": None,
    "01-Legal-Database/01-05/10. Thông-tư-36-2026-TT-BXD DINH MUC.docx": None,
    "01-Legal-Database/01-01/33. Luat xay dung 02-VBHN-VPQH.docx":
        "- Tình trạng: SẮP HẾT HIỆU LỰC — HẾT HIỆU LỰC TOÀN BỘ kể từ ngày 01/7/2026\n",
    "01-Legal-Database/01-04/01. Nghi dinh so 30_2020_ND-CP_436532.docx":
        "- Tình trạng: Đang có hiệu lực\n",
    "01-Legal-Database/01-01/LUAT-12-2026-QH16_Pho-bien-giao-duc-phap-luat_2026_v1.docx": None,
    "01-Legal-Database/01-01/12. Luat Giao duc -72-VBHN-VPQH.docx": None,
    "01-Legal-Database/01-01/09. Luat Giao duc nghe nghiep 2025.docx": None,
    "01-Legal-Database/01-02/Ket luan 198-KL-TW Bo Chinh tri.docx": None,
    "02-KTC-Regulations/Ke hoach 198-KH-CDKT.docx": None,
}
for rel, meta in tep.items():
    p = os.path.join(KHO, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "wb").write(b"x")
    if meta:
        open(os.path.splitext(p)[0] + ".metadata.md", "w", encoding="utf-8").write(meta)
os.makedirs(os.path.join(KHO, "02-KTC-Regulations"), exist_ok=True)
kho = t.Kho(KHO)

du_thao = [
    "Căn cứ Quyết định số 988/QĐ-CĐKT ngày 12/5/2026 của Hiệu trưởng;",
    "Căn cứ Luật Xây dựng ngày 18 tháng 6 năm 2014;",
    "Căn cứ Nghị định số 85/2025/NĐ-CP ngày 08/4/2025 của Chính phủ;",
    "Căn cứ Thông tư số 36/2026/TT-BXD của Bộ Xây dựng;",
    "Căn cứ NĐ 30/2020/NĐ-CP về công tác văn thư;",
    "Căn cứ Thông báo số 916/TB-UBND ngày 01/9/2026.",
    "Căn cứ Kết luận số 198-KL/TW ngày 05/8/2026 của Bộ Chính trị;",
    "Căn cứ Quyết định số 366-QĐ/TW của Ban Chấp hành Trung ương;",
    "Thực hiện Hướng dẫn số 05-HD/VPTW của Văn phòng Trung ương Đảng;",
    "Kế hoạch phát triển giai đoạn 2021-2025 và Nghị quyết Đại hội XIV.",
]
vbs = t.trich(du_thao)
kq = {(v["loai"], v["so"] or v["ten"]): t.phan_loai(v, kho, {}) for v in vbs}


def lay(loai, khoa):
    return kq.get((loai, khoa), ("(không trích được)", [], ""))


kiem(len(vbs) == 9, f"trích đủ 9 văn bản, kể cả viết tắt “NĐ 30/2020/NĐ-CP” và 3 số hiệu Đảng (được {len(vbs)})")
kiem(lay("Quyết định", "988/QĐ-CĐKT")[0] == "THAY_THE", "QĐ 988 → THAY_THE (chuỗi đã biết)")
kiem(lay("Luật", "Xây dựng")[0] == "KHO_GHI_HET_HIEU_LUC", "Luật Xây dựng → KHO_GHI_HET_HIEU_LUC từ metadata")
p85 = lay("Nghị định", "85/2025/NĐ-CP")
kiem(p85[0] == "CO_TRONG_KHO" and all("275" not in os.path.basename(x) for x in p85[1]),
     "NĐ 85/2025 khớp đúng tệp, KHÔNG khớp “275-2025 sửa đổi NĐ 85”")
p36 = lay("Thông tư", "36/2026/TT-BXD")
kiem(p36[1] and all("TT-BXD" in x for x in p36[1]), "TT 36/2026/TT-BXD không khớp nhầm QĐ 36/2026/QĐ-TTg")
kiem(lay("Nghị định", "30/2020/NĐ-CP")[0] == "CO_TRONG_KHO", "NĐ 30/2020 (tên tệp dạng 30_2020_ND-CP) có trong kho")
kiem(lay("Thông báo", "916/TB-UBND")[0] == "KHONG_CO_TRONG_KHO", "TB 916 không có trong kho → CẦN XÁC MINH")
gd = kho.tim({"loai": "Luật", "so": None, "ten": "Giáo dục"})
kiem([os.path.basename(x) for x in gd] == ["12. Luat Giao duc -72-VBHN-VPQH.docx"],
     f"“Luật Giáo dục” chỉ khớp đúng luật, không khớp “Phổ biến, giáo dục pháp luật” hay “Giáo dục nghề nghiệp” (được {[os.path.basename(x) for x in gd]})")
gdnn = kho.tim({"loai": "Luật", "so": None, "ten": "Giáo dục nghề nghiệp"})
kiem(len(gdnn) == 1 and "nghe nghiep" in gdnn[0], "“Luật Giáo dục nghề nghiệp” khớp đúng tệp")
# --- So hieu van ban Dang (dang "198-KL/TW") va loai "Ket luan" — 20/9/2026 ---
kiem(("Kết luận", "198-KL/TW") in kq, "trích được “Kết luận số 198-KL/TW” (loại Kết luận + số hiệu Đảng)")
kiem(("Quyết định", "366-QĐ/TW") in kq, "trích được “Quyết định số 366-QĐ/TW”")
kiem(("Hướng dẫn", "05-HD/VPTW") in kq, "trích được “Hướng dẫn số 05-HD/VPTW”")
kl = lay("Kết luận", "198-KL/TW")
kiem(kl[0] == "CO_TRONG_KHO" and all("Ket luan" in os.path.basename(x) for x in kl[1]),
     f"KL 198-KL/TW khớp đúng tệp Kết luận, KHÔNG khớp “Kế hoạch 198-KH-CĐKT” (được {[os.path.basename(x) for x in kl[1]]})")
kiem(not any(v["so"] and "2021-2025" in v["so"] for v in vbs),
     "“giai đoạn 2021-2025” không bị nhận nhầm là số hiệu")

kiem(t.phan_loai({"loai": "Nghị định", "so": "85/2025/NĐ-CP", "ten": None}, None, {})[0] == "KHONG_CO_TRONG_KHO",
     "không đọc được kho → mọi văn bản là CẦN XÁC MINH, không kết luận")

print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
