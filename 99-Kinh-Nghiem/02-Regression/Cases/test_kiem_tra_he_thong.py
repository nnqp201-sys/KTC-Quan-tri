# -*- coding: utf-8 -*-
"""Thu NGUOC bo kiem tra he thong — no co that su bat duoc loi khong?

Ly do ton tai: 14/9/2026 mot regex kiem tra chua ky tu backspace 0x08 vo hinh
nen KHONG BAO GIO khop, va bao "khong co loi" suot. Mot phep kiem hong luon
bao sach. Vi vay: moi phep kiem phai duoc thu tren ca BIET CHAC LA SAI.

Chay: python 99-Kinh-Nghiem/02-Regression/Cases/test_kiem_tra_he_thong.py
"""
import os
import re
import sys
import tempfile
import io

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "tools"))

import kiem_tra_he_thong as K          # noqa: E402
from dong_goi_skill import kiem_frontmatter  # noqa: E402

that_bai = []


def kiem(ten, dieu_kien, mo_ta):
    print(f"  {'✓' if dieu_kien else '✗'} {ten:56s} {mo_ta}")
    if not dieu_kien:
        that_bai.append(ten)


def bat(s):
    """Bo kiem C7 co bat chuoi nay khong?"""
    for rx, _ in K.CUM_CAM:
        for m in re.finditer(rx, s, re.I):
            if not K.MIEN.search(m.group(0)):
                return True
    return False


def bat_ten(s, cu):
    """Bo kiem C6 co coi day la dinh tuyen gay khong?"""
    return bool(re.search(rf"(dùng|dung|chuyển sang|chuyen sang|chuyển qua|gọi|goi|→|->)\s*`?{cu}", s, re.I))


print("=" * 74)
print("THỬ NGƯỢC — bộ kiểm có bắt được lỗi thật không?")
print("=" * 74)

# ---------------------------------------------------- C7: hạ cấp chốt chặn
print("\nC7 — cụm hạ cấp chốt chặn 897 (PHẢI bắt):")
for s in ["| 5 | Rà soát chính thức trước khi trình ký (nếu cần) | ktc-ra-soat-897 |",
          "Rà soát trước khi trình ký (dùng `ktc-ra-soat-897` nếu cần).",
          "### Bước 5 — Rà soát chính thức *(tùy chọn)* Dùng hệ `ktc-ra-soat-897`.",
          "Có thể dùng 897 nếu cần thiết."]:
    kiem(f"bắt: {s[:46]}", bat(s), "")

print("\nC7 — câu ĐÚNG, không được báo nhầm (PHẢI bỏ qua):")
for s in ["**897 là chốt chặn bắt buộc, không phải bước tùy chọn.**",
          "Rà soát bắt buộc bằng ktc-ra-soat-897 — không bỏ qua.",
          "Dùng hệ `ktc-ra-soat-897`. Đây là chốt chặn, không phải bước tùy chọn."]:
    kiem(f"bỏ qua: {s[:46]}", not bat(s), "")

# ---------------------------------------------------- C6: tên hệ đã bỏ
print("\nC6 — tên hệ đã bỏ dùng làm đích định tuyến (PHẢI bắt):")
for s, cu in [("dùng `ktc-van-ban` / `ktc-ra-soat-897`", "ktc-van-ban"),
              ("KHONG dung de soan van ban - dung ktc-van-ban cho viec do", "ktc-van-ban"),
              ("chuyển sang ktc-dis-tong-hop-vb", "ktc-dis-tong-hop-vb")]:
    kiem(f"bắt: {s[:46]}", bat_ten(s, cu), "")

print("\nC6 — nhắc lại lịch sử, KHÔNG phải định tuyến (PHẢI bỏ qua):")
for s, cu in [("Kế thừa từ `KTC-DIS-Tong-Hop-VB`, thu hẹp có chủ đích.", "ktc-dis-tong-hop-vb"),
              ("*Tiền lệ:* hệ `KTC-DIS-Tong-Hop-VB` từng chép checklist của 897.", "ktc-dis-tong-hop-vb")]:
    kiem(f"bỏ qua: {s[:46]}", not bat_ten(s, cu), "")

# ---------------------------------------------------- C1: frontmatter
print("\nC1 — frontmatter hỏng (PHẢI bắt):")
TMP = tempfile.mkdtemp()
CA = [
    ("thiếu frontmatter", "# Skill\n\nNội dung.\n", True),
    ("name viết hoa", '---\nname: KTC-Bao-Cao\ndescription: "x"\n---\n# a\n', True),
    ("thừa khóa version", '---\nname: a-b\ndescription: "x"\nversion: 1\n---\n# a\n', True),
    ("description quá 1024", '---\nname: a-b\ndescription: "' + "x" * 1100 + '"\n---\n# a\n', True),
    ("hợp lệ", '---\nname: ktc-bao-cao\ndescription: "Mô tả hợp lệ."\n---\n# a\n', False),
]
for ten, noi_dung, phai_loi in CA:
    p = os.path.join(TMP, "SKILL.md")
    io.open(p, "w", encoding="utf-8").write(noi_dung)
    co_loi = bool(kiem_frontmatter(p))
    kiem(f"{'bắt' if phai_loi else 'bỏ qua'}: {ten}", co_loi == phai_loi,
         f"→ {kiem_frontmatter(p)[:1] if co_loi else 'hợp lệ'}")

# ---------------------------------------------------- tổng kết
print("\n" + "=" * 74)
if that_bai:
    print(f"THẤT BẠI: {len(that_bai)} phép kiểm KHÔNG hoạt động đúng")
    for t in that_bai:
        print("   ✗", t)
    print("=" * 74)
    sys.exit(1)
print("ĐẠT — mọi phép kiểm đều bắt đúng ca sai và bỏ qua đúng ca đúng")
print("=" * 74)
