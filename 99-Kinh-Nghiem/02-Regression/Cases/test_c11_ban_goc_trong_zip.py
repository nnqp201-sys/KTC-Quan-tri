# -*- coding: utf-8 -*-
"""Thu NGUOC phep kiem C11 — no co phat hien tep chi ton tai trong zip khong?

Ly do ton tai: 14/9/2026 phat hien 9 tep tri thuc GOC cua ktc-quan-tri (~490 dong:
doi chieu ba he, chot ky, quy doi KPI va xep loai, gioi han nen tang) chi nam BEN
TRONG ktc-quan-tri.skill — khong co ban sao o bat ky dau. Quy uoc cua du an la ban
goc nam o thu muc nguon, goi chi la ban dong. Tep .skill hong hoac mat tren Drive
la mat trang phan tri thuc do.

Chay: python 99-Kinh-Nghiem/02-Regression/Cases/test_c11_ban_goc_trong_zip.py
"""
import io
import os
import shutil
import sys
import tempfile
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "tools"))

import kiem_tra_he_thong as K          # noqa: E402

that_bai = []


def kiem(ten, dieu_kien, mo_ta=""):
    print(f"  {'✓' if dieu_kien else '✗'} {ten:58s} {mo_ta}")
    if not dieu_kien:
        that_bai.append(ten)


def chay(tep_trong_goi, tep_co_ban_roi):
    """Dung du an gia roi chay C11. Tra ve so canh bao."""
    tmp = tempfile.mkdtemp()
    he = os.path.join(tmp, "He-Thu")
    os.makedirs(os.path.join(he, "references"), exist_ok=True)
    for t in tep_co_ban_roi:
        p = os.path.join(he, *t.split("/"))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        io.open(p, "w", encoding="utf-8", newline="").write("noi dung")
    with zipfile.ZipFile(os.path.join(he, "he-thu.skill"), "w") as z:
        z.writestr("he-thu/SKILL.md", "---\nname: he-thu\ndescription: \"x\"\n---\n")
        for t in tep_trong_goi:
            z.writestr(f"he-thu/{t}", "noi dung")
    io.open(os.path.join(he, "SKILL.md"), "w", encoding="utf-8", newline="").write(
        "---\nname: he-thu\ndescription: \"x\"\n---\n")
    du_an_cu, he_cu = K.DU_AN, K.HE
    K.DU_AN = tmp
    K.HE = {"he-thu": ("He-Thu", os.path.join("He-Thu", "he-thu.skill"))}
    del K.loi[:], K.canh_bao[:]
    try:
        K.c11_ban_goc_trong_zip()
        return len(K.canh_bao)
    finally:
        K.DU_AN, K.HE = du_an_cu, he_cu
        del K.loi[:], K.canh_bao[:]
        shutil.rmtree(tmp, ignore_errors=True)


print("=" * 74)
print("THỬ NGƯỢC C11 — có phát hiện tệp chỉ tồn tại trong zip không?")
print("=" * 74)

print("\nCa 1 — gói mang 3 tệp, nguồn rời không có tệp nào (đúng lỗi đã mắc):")
n = chay(["references/a.md", "references/b.md", "references/c.md"], [])
kiem("phải cảnh báo đủ 3 tệp", n == 3, f"→ {n} cảnh báo")

print("\nCa 2 — mọi tệp trong gói đều có bản nguồn ngoài zip:")
n = chay(["references/a.md", "references/b.md"], ["references/a.md", "references/b.md"])
kiem("phải sạch", n == 0, f"→ {n} cảnh báo")

print("\nCa 3 — thiếu đúng 1 tệp trong ba:")
n = chay(["references/a.md", "references/b.md", "references/c.md"],
         ["references/a.md", "references/c.md"])
kiem("phải cảnh báo đúng 1 tệp", n == 1, f"→ {n} cảnh báo")

print("\nCa 4 — tệp nằm sâu nhiều cấp thư mục:")
n = chay(["references/Memory/01-Nhat-Ky.md"], [])
kiem("vẫn phải bắt được", n == 1, f"→ {n} cảnh báo")

print("\nCa 5 — nguồn rời THỪA tệp mà gói không có (hợp lệ, không được báo):")
n = chay(["references/a.md"], ["references/a.md", "references/thua.md"])
kiem("không được cảnh báo", n == 0, f"→ {n} cảnh báo")

print("\n" + "=" * 74)
if that_bai:
    print(f"THẤT BẠI: {len(that_bai)} phép kiểm KHÔNG hoạt động đúng")
    for t in that_bai:
        print("   ✗", t)
    print("=" * 74)
    sys.exit(1)
print("ĐẠT — C11 bắt đúng tệp mồ côi trong zip, không báo nhầm")
print("=" * 74)
