# -*- coding: utf-8 -*-
"""Thu NGUOC phep kiem C5 — no co soi vao BEN TRONG goi .skill khong?

Ly do ton tai: 14/9/2026 phat hien C5 ban dau chi so 20-Chuan-Chung voi BAN ROI
o <he>/references/Skill-Library/, khong bao gio mo tep .skill. Ban roi khop 100%
nen C5 in "khop o moi he" — trong khi 3/5 tep dung chung BEN TRONG goi la ban cu
(30-Skill-Phan-Loai-6-Truc.md: goc 9.034 B, trong ktc-bao-cao-v3.5.skill 4.515 B,
goi Truc 4 bang ten cu). Goi moi la thu chay tren Chat/Cowork, khong phai ban roi.

Mot phep kiem nhin nham cho cung nguy hiem nhu mot phep kiem hong — con te hon,
vi no in dau tich.

Chay: python 92-Kinh-Nghiem/02-Regression/Cases/test_c5_soi_trong_goi.py
"""
import io
import os
import shutil
import sys
import tempfile
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "29-Cong-Cu"))

import kiem_tra_he_thong as K          # noqa: E402

that_bai = []
TEP = "30-Skill-Phan-Loai-6-Truc.md"
GOC = "# Phan loai 6 Truc\n\nTruc 4 — ...giu gin doan ket, thong nhat\n" + "x" * 400
CU = "# Phan loai 6 Truc\n\nTruc 4 — ...phong, chong tham nhung\n"


def kiem(ten, dieu_kien, mo_ta=""):
    print(f"  {'✓' if dieu_kien else '✗'} {ten:58s} {mo_ta}")
    if not dieu_kien:
        that_bai.append(ten)


def ghi(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def dung_du_an(noi_dung_roi, noi_dung_goi):
    """Dung mot du an gia. noi_dung_goi=None nghia la goi KHONG mang tep nay."""
    tmp = tempfile.mkdtemp()
    ghi(os.path.join(tmp, "20-Chuan-Chung", TEP), GOC)
    he = os.path.join(tmp, "He-Thu")
    if noi_dung_roi is not None:
        ghi(os.path.join(he, "references", "Skill-Library", TEP), noi_dung_roi)
    goi = os.path.join(he, "he-thu.skill")
    os.makedirs(he, exist_ok=True)
    with zipfile.ZipFile(goi, "w") as z:
        z.writestr("he-thu/SKILL.md", "---\nname: he-thu\ndescription: \"x\"\n---\n")
        if noi_dung_goi is not None:
            z.writestr(f"he-thu/references/Skill-Library/{TEP}", noi_dung_goi)
    return tmp


def chay(noi_dung_roi, noi_dung_goi):
    """Chay C5 tren du an gia. Tra ve (so_loi, so_canh_bao)."""
    tmp = dung_du_an(noi_dung_roi, noi_dung_goi)
    du_an_cu, he_cu, chung_cu = K.DU_AN, K.HE, K.CHUNG
    K.DU_AN = tmp
    K.HE = {"he-thu": ("He-Thu", os.path.join("He-Thu", "he-thu.skill"))}
    K.CHUNG = [TEP]
    del K.loi[:], K.canh_bao[:]
    try:
        K.c5_tep_dung_chung()
        return len(K.loi), len(K.canh_bao)
    finally:
        K.DU_AN, K.HE, K.CHUNG = du_an_cu, he_cu, chung_cu
        del K.loi[:], K.canh_bao[:]
        shutil.rmtree(tmp, ignore_errors=True)


print("=" * 74)
print("THỬ NGƯỢC C5 — có soi vào bên trong gói .skill không?")
print("=" * 74)

print("\nCa 1 — BẢN RỜI KHỚP nhưng TRONG GÓI là bản cũ (đúng điểm mù đã mắc):")
n_loi, n_cb = chay(GOC, CU)
kiem("phải báo LỖI, không được báo sạch", n_loi >= 1, f"→ {n_loi} lỗi · {n_cb} cảnh báo")

print("\nCa 2 — trong gói khớp, bản rời lệch (còn kịp sửa trước khi đóng gói):")
n_loi, n_cb = chay(CU, GOC)
kiem("cảnh báo chứ KHÔNG phải lỗi", n_loi == 0 and n_cb >= 1,
     f"→ {n_loi} lỗi · {n_cb} cảnh báo")

print("\nCa 3 — cả hai đều khớp bản gốc:")
n_loi, n_cb = chay(GOC, GOC)
kiem("phải sạch hoàn toàn", n_loi == 0 and n_cb == 0, f"→ {n_loi} lỗi · {n_cb} cảnh báo")

print("\nCa 4 — gói không mang tệp dùng chung này (hợp lệ, không được bịa lỗi):")
n_loi, n_cb = chay(GOC, None)
kiem("không lỗi, không cảnh báo", n_loi == 0 and n_cb == 0, f"→ {n_loi} lỗi · {n_cb} cảnh báo")

print("\nCa 5 — bản rời không tồn tại VÀ trong gói là bản cũ:")
n_loi, n_cb = chay(None, CU)
kiem("vẫn phải báo LỖI ở bản trong gói", n_loi >= 1, f"→ {n_loi} lỗi · {n_cb} cảnh báo")

print("\n" + "=" * 74)
if that_bai:
    print(f"THẤT BẠI: {len(that_bai)} phép kiểm KHÔNG hoạt động đúng")
    for t in that_bai:
        print("   ✗", t)
    print("=" * 74)
    sys.exit(1)
print("ĐẠT — C5 soi đúng cả bản rời lẫn bản nằm trong gói")
print("=" * 74)
