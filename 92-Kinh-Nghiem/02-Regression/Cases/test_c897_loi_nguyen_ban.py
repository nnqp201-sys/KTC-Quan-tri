# -*- coding: utf-8 -*-
"""Thu NGUOC phep kiem C-897 (loi ktc-ra-soat-897 v4.5 nguyen ban).

Ly do: phep kiem moi ma luon bao "sach" thi chua chung to no bat duoc loi. Ca nay chep ban tich
hop sang thu muc tam, sua 1 byte tep loi / them tep la / sua SKILL.md ngoai ranh gioi -> C-897
phai bao loi; ban nguyen ban va ban chi them lop bo sung phai sach.

Chay: python 92-Kinh-Nghiem/02-Regression/Cases/test_c897_loi_nguyen_ban.py
"""
import os
import shutil
import sys
import tempfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "29-Cong-Cu"))
import dong_goi_ra_soat_897 as G  # noqa: E402

that_bai = []


def kiem(ten, dk, mo_ta):
    print(f"  {'OK ' if dk else ' X '} {ten:46s} {mo_ta}")
    if not dk:
        that_bai.append(ten)


def ban_sao():
    g = tempfile.mkdtemp(prefix="ktc_c897_")
    shutil.copytree(os.path.join(DU_AN, G.HE), os.path.join(g, G.HE),
                    ignore=shutil.ignore_patterns("*.skill", "SHA256SUMS"))
    shutil.copytree(os.path.join(DU_AN, G.GOC_DIR), os.path.join(g, G.GOC_DIR))
    return g


def sua_byte(g, rel):
    p = os.path.join(g, G.HE, G.TEN_SKILL, *rel.split("/"))
    b = bytearray(open(p, "rb").read())
    b[len(b) // 2] ^= 0x01
    open(p, "wb").write(bytes(b))


def noi_dung(g, rel, them=b"", thay=None):
    p = os.path.join(g, G.HE, G.TEN_SKILL, *rel.split("/"))
    b = open(p, "rb").read()
    if thay:
        assert thay[0] in b
        b = b.replace(thay[0], thay[1], 1)
    open(p, "wb").write(b + them)


kiem("du_an_that_sach", G.kiem_loi(DU_AN) == [], "bản tích hợp thật: 0 lỗi")

g = ban_sao()
kiem("ban_sao_sach", G.kiem_loi(g) == [], "bản sao nguyên trạng: 0 lỗi")

# CA BIET CHAC SAI 1: sua 1 byte tools/tao_bao_cao.py (ca nghiem thu so 4)
g = ban_sao(); sua_byte(g, "tools/tao_bao_cao.py")
ds = G.kiem_loi(g)
kiem("bat_sua_1_byte_tao_bao_cao", any("tools/tao_bao_cao.py" in x for x in ds), f"{len(ds)} lỗi")

# CA 2: sua 1 byte tep checklist
g = ban_sao(); sua_byte(g, "references/Checklist/01-The-Thuc.md")
kiem("bat_sua_checklist", any("01-The-Thuc.md" in x for x in G.kiem_loi(g)), "lệch mã băm")

# CA 3: tep la ngoai Bo-Sung-Ca-Nhan
g = ban_sao()
open(os.path.join(g, G.HE, G.TEN_SKILL, "references", "Checklist", "99-Them.md"), "w").write("x")
kiem("bat_tep_la", any("tệp lạ" in x for x in G.kiem_loi(g)), "tệp ngoài lõi và ngoài Bo-Sung-Ca-Nhan")

# CA 4: thieu tep loi
g = ban_sao(); os.remove(os.path.join(g, G.HE, G.TEN_SKILL, "tools", "so_sanh_ban.py"))
kiem("bat_thieu_tep", any("thiếu tệp lõi" in x for x in G.kiem_loi(g)), "")

# CA 5: sua noi dung SKILL.md o phan loi (Buoc 1)
g = ban_sao(); noi_dung(g, "SKILL.md", thay=("Cổng hồ sơ – bắt buộc, chặn hẳn".encode(), "Cổng hồ sơ – tùy chọn".encode()))
kiem("bat_sua_skill_md_loi", any("KHÔNG khớp từng byte" in x for x in G.kiem_loi(g)), "")

# CA 6: SKILL.md them noi dung SAU muc bo sung la hop le (nam trong muc), nhung them muc ## moi la sai
g = ban_sao(); noi_dung(g, "SKILL.md", them="\n## Mục lạ\nx\n".encode())
kiem("bat_muc_sau_muc_bo_sung", any("mục ## cuối cùng" in x for x in G.kiem_loi(g)), "")

# CA 7: them tep vao lop bo sung la hop le
g = ban_sao()
open(os.path.join(g, G.HE, G.TEN_SKILL, "references", "Bo-Sung-Ca-Nhan", "08-Them.md"), "w", encoding="utf-8").write(
    "# 08\n**Nguồn:** a\n**Phạm vi:** b\n*" + G.DONG_CO_DINH + "*\n")
kiem("cho_phep_them_lop_bo_sung", G.kiem_loi(g) == [], "tệp mới đúng khối mở đầu trong Bo-Sung-Ca-Nhan: hợp lệ")

# CA 8: tep bo sung thieu dong co dinh
g = ban_sao()
open(os.path.join(g, G.HE, G.TEN_SKILL, "references", "Bo-Sung-Ca-Nhan", "08-Them.md"), "w", encoding="utf-8").write("# 08\nx\n")
kiem("bat_thieu_khoi_mo_dau", any("khối mở đầu" in x for x in G.kiem_loi(g)), "")

print(f"\n{'ĐẠT' if not that_bai else 'KHÔNG ĐẠT'}: {len(that_bai)} ca sai")
sys.exit(1 if that_bai else 0)
