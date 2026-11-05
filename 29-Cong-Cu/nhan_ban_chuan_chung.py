# -*- coding: utf-8 -*-
"""Nhan ban quy tac dung chung tu 20-Chuan-Chung/ xuong BAN SAO TRONG NGUON ROI cua cac he.

CLAUDE.md: "20-Chuan-Chung/ giu ban GOC; cac he giu ban SAO. Sua o 20-Chuan-Chung/ truoc,
roi nhan ban xuong tai buoc build."

Buoc build cua plugin da tu nhan ban (dong_goi_plugin.py: nhan_ban_chuan_chung). Nhung ban sao
trong NGUON ROI <he>/references/ thi khong ai cap nhat -> goi .skill dong tu nguon roi mang quy
tac CU. Tai khoan Chat/Cowork nhan tep .skill TRUC TIEP, khong qua plugin, nen dung quy tac cu
that su (phat hien 5/11/2026: ban goc sua 29/10, goi .skill dong 29/9 — lech mot thang,
kiem_tra_he_thong.py bao 93 loi C5).

Chay:  python 29-Cong-Cu/nhan_ban_chuan_chung.py            # nhan ban
       python 29-Cong-Cu/nhan_ban_chuan_chung.py --kiem     # chi liet ke, khong ghi
"""
import argparse
import hashlib
import io
import os
import shutil
import sys

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOC_DIR = os.path.join(DU_AN, "20-Chuan-Chung")

# KHONG cham vao:
#   2A-KTC-Ra-Soat-897  — loi ban hanh cua Hieu truong, khoa bam tung byte (TB 1206 muc 6)
#   29-Cong-Cu/_trung_gian, 99-Luu-Tru, 31-Plugin — ban trung gian / ban dung / ban luu
#   30-Ket-Qua — san pham da giao, khong sua hoi to
LOAI_TRU = ("2A-KTC-Ra-Soat-897", "_trung_gian", "99-Luu-Tru", "31-Plugin", "30-Ket-Qua",
            ".git", ".kilo", "20-Chuan-Chung")


def bam(p):
    """So bam bo qua khac biet xuong dong (CRLF/LF khong phai khac noi dung)."""
    return hashlib.sha256(io.open(p, "rb").read().replace(b"\r\n", b"\n")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kiem", action="store_true", help="chi liet ke, khong ghi")
    a = ap.parse_args()

    # MOT nguon su that cho danh sach tep dung chung va bang DOI TEN: lay thang tu bo kiem
    # kiem_tra_he_thong.py. He quan-tri doi ten ban sao (00-Nguyen-Tac-Chung -> 01-...,
    # 19-Quy-Tac-KPI -> 30-KPI-Va-Xep-Loai); khop theo ten tran se bo sot dung nhung tep do.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from kiem_tra_he_thong import CHUNG, HE, duong_dan_chung

    lech = []
    for f in CHUNG:
        goc = os.path.join(GOC_DIR, f)
        if not os.path.isfile(goc):
            continue
        for ten_he, (thu_muc, _) in HE.items():
            rel = duong_dan_chung(ten_he, f)
            if rel is None:
                continue
            p = os.path.join(DU_AN, thu_muc, *rel.split("/"))
            if os.path.isfile(p) and bam(p) != bam(goc):
                lech.append((p, goc, f))

    if not lech:
        print("✓ Mọi bản sao trong nguồn rời đã khớp bản gốc 20-Chuan-Chung/")
        return 0

    he_anh_huong = sorted({os.path.relpath(p, DU_AN).split(os.sep)[0] for p, _, _ in lech})
    print(f"── {len(lech)} bản sao lệch bản gốc, thuộc {len(he_anh_huong)} hệ ──")
    for p, g, f in lech:
        print(f"  {'(kiểm)' if a.kiem else '✓'} {os.path.relpath(p, DU_AN)} ← 20-Chuan-Chung/{f}")
        if not a.kiem:
            shutil.copyfile(g, p)
    print()
    print("Hệ cần ĐÓNG GÓI LẠI (nâng phiên bản trong SKILL.md trước khi đóng):")
    for h in he_anh_huong:
        print(f"  · {h}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
