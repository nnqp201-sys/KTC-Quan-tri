# -*- coding: utf-8 -*-
"""Hoi quy kiem_vien_dan.py — DL-20260919-002 (quy tac 20-Chuan-Chung/17-Quy-Tac-Vien-Dan.md).

Moi ma loi co ca THU NGUOC (biet chac sai) va ca DUNG (khong duoc bat) — LL-20260914-001.
Chot 19/9/2026: van ban hanh chinh vien dan Luat/Phap lenh KHONG ghi so hieu, ke ca khi co VBHN.
"""
import os
import sys

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
from kiem_vien_dan import kiem_tra  # noqa: E402

sai = []


def ma(doan):
    return {x[1] for x in kiem_tra(doan)}


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


# Du thao dung chuan — khong duoc co goi y nao
DUNG = [
    "QUYẾT ĐỊNH",
    "Về việc ban hành Kế hoạch tuyển sinh năm 2026",
    "HIỆU TRƯỞNG TRƯỜNG CAO ĐẲNG KON TUM",
    "Căn cứ Quyết định số 1976/QĐ-CĐKT ngày 14/9/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum ban hành "
    "Quy chế tổ chức và hoạt động của Trường;",
    "Căn cứ Luật Giáo dục nghề nghiệp ngày 10 tháng 12 năm 2025;",
    "Căn cứ Luật Giáo dục ngày 14 tháng 6 năm 2019;",
    "Căn cứ Nghị định số 143/2013/NĐ-CP ngày 24 tháng 10 năm 2013 của Chính phủ quy định về bồi hoàn học "
    "bổng và chi phí đào tạo (hợp nhất tại Văn bản hợp nhất số 01/VBHN-BGDĐT);",
    "Xét đề nghị của Trưởng phòng Tổng hợp - Hành chính và Quản trị.",
    "",
    "Điều 1. Thực hiện theo điểm a khoản 2 Điều 4 của Quyết định số 1976/QĐ-CĐKT.",
]
kiem(ma(DUNG) == set(), f"dự thảo chuẩn không bị bắt lỗi (được: {sorted(ma(DUNG))})")

# Chot 19/9: Luat co so hieu -> VD01, ke ca khi co ngoac hop nhat
kiem("VD01" in ma(["Căn cứ Luật Giáo dục số 43/2019/QH14 ngày 14 tháng 6 năm 2019;"]),
     "VD01 căn cứ Luật có số hiệu")
kiem("VD01" in ma(["Căn cứ Luật Giáo dục số 43/2019/QH14 (hợp nhất tại Văn bản hợp nhất số 72/VBHN-VPQH);"]),
     "VD01 Luật có số hiệu kể cả khi kèm VBHN")
kiem("VD01" in ma(["Theo quy định tại Luật Nhà giáo số 73/2025/QH15, nhà giáo được…"]),
     "VD01 viện dẫn trong nội dung cũng không ghi số hiệu luật")
kiem("VD01" in ma(["Căn cứ Pháp lệnh Hợp nhất văn bản quy phạm pháp luật số 01/2012/UBTVQH13;"]),
     "VD01 Pháp lệnh có số hiệu")
kiem("VD01" not in ma(["Căn cứ Nghị định số 30/2020/NĐ-CP ngày 05/3/2020 của Chính phủ về công tác văn thư;"]),
     "VD01 không bắt nghị định có số hiệu")

kiem("VD02" in ma(["Căn cứ Luật Giáo dục;"]), "VD02 căn cứ luật thiếu ngày")
kiem("VD02" not in ma(["Căn cứ Luật Giáo dục ngày 14/6/2019;"]), "VD02 ngày dạng dd/mm/yyyy được chấp nhận")
kiem("VD03" in ma(["Căn cứ Văn bản hợp nhất số 72/VBHN-VPQH;"]), "VD03 VBHN làm căn cứ chính")
kiem("VD04" in ma(["Pháp lệnh Hợp nhất văn bản quy phạm pháp luật của Quốc hội quy định…"]),
     "VD04 Pháp lệnh 'của Quốc hội'")
kiem("VD04" not in ma(["Pháp lệnh … của Ủy ban Thường vụ Quốc hội"]), "VD04 không bắt UBTVQH")
kiem("VD05" in ma(["Căn cứ Luật số 123/2025/QH15 ngày 10 tháng 12 năm 2025;"]), "VD05 chỉ dẫn luật sửa đổi")
kiem("VD06" in ma(["Căn cứ Luật Giáo dục ngày 14/6/2019.", "Xét đề nghị của Trưởng phòng Đào tạo."]),
     "VD06 dấu cuối dòng giữa sai")
kiem("VD06" in ma(["Căn cứ Luật Giáo dục ngày 14/6/2019;"]), "VD06 dòng cuối thiếu dấu chấm")
kiem("VD07" in ma(["- Căn cứ Luật Giáo dục ngày 14/6/2019."]), "VD07 gạch đầu dòng")
kiem("VD08" in ma(["QUYẾT ĐỊNH", "HIỆU TRƯỞNG TRƯỜNG CAO ĐẲNG KON TUM",
                   "Căn cứ Luật Giáo dục ngày 14/6/2019."]), "VD08 QĐ Hiệu trưởng thiếu QĐ 1976 đầu tiên")
kiem("VD08" not in ma(["KẾ HOẠCH", "Căn cứ Luật Giáo dục ngày 14/6/2019."]),
     "VD08 không áp cho kế hoạch")
kiem("VD09" in ma(["Căn cứ Quyết định số 988/QĐ-CĐKT ngày 12/5/2026 của Hiệu trưởng."]),
     "VD09 văn bản Trường đã bị thay thế")
kiem("VD09" not in ma(["Căn cứ Quyết định số 1229/QĐ-CĐKT ngày 22/9/2023."]),
     "VD09 không nhầm QĐ 1229 (quy chế đào tạo) với QĐ 1299")
kiem("VD09" not in ma(["Điều 2. Quyết định này có hiệu lực kể từ ngày ký và thay thế Quyết định số "
                       "215/QĐ-CĐKT ngày 15/02/2024 của Hiệu trưởng."]),
     "VD09 không bắt điều khoản thay thế/bãi bỏ (thử thật trên kho 02, 19/9/2026)")
kiem("VD06" not in ma(["QUYẾT ĐỊNH", "Căn cứ Luật Giáo dục ngày 14/6/2019;", "Xét đề nghị của Trưởng phòng Đào tạo."]
                      + ["nội dung"] * 70 + ["Căn cứ vào báo cáo của đơn vị, Hội đồng xem xét"]),
     "VD06 không áp cho câu 'Căn cứ…' trong phần nội dung (ngoài khối căn cứ đầu văn bản)")
kiem("VD10" in ma(["Căn cứ Checklist 02-Noi-Dung.md của hệ rà soát."]), "VD10 dẫn checklist làm căn cứ")
kiem("VD11" in ma(["Thực hiện theo khoản 2 điều 4 Luật Giáo dục."]), "VD11 'điều' viết thường")
kiem("VD12" in ma(["Căn cứ Quyết định số 389/QĐ-CĐKT ngày 26/02/2026 của Hiệu trưởng.",
                   "Thực hiện Quyết định số 389/QĐ-CĐKT ngày 26/02/2026 của Hiệu trưởng về…",
                   "Theo Quyết định số 389/QĐ-CĐKT ngày 26/02/2026 của Hiệu trưởng về…"]),
     "VD12 viện dẫn lần sau vẫn ghi đầy đủ")

print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
