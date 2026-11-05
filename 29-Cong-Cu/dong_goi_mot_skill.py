# -*- coding: utf-8 -*-
"""Dong goi lai MOT goi .skill tu thu muc nguon cua he — dung lap lai duoc.

Goi .skill la zip tu chua: <ten-skill>/SKILL.md + 00-README.md + references/**.
Script nay thay viec zip tay, giu dung 3 quy tac da chot:

  1. Chuan hoa xuong dong LF truoc khi nen (1.3.13) — nen lai cung nguon cho cung so bam.
  2. Bo qua rac: __pycache__, .DS_Store, desktop.ini (tep cua Google Drive), *.skill long nhau.
  3. Doc phien ban TU KHAI trong SKILL.md, khong suy dien tu ten tep (bai hoc 18/9/2026).

Dung:
    python 29-Cong-Cu/dong_goi_mot_skill.py 26-KTC-Soan-Thao-VB ktc-soan-thao-vb
    python 29-Cong-Cu/dong_goi_mot_skill.py 26-KTC-Soan-Thao-VB ktc-soan-thao-vb --kiem

--kiem chi so sanh nguon voi goi hien co, KHONG ghi gi.
"""
import argparse
import io
import os
import re
import sys
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BO_QUA_TEN = {"__pycache__", ".DS_Store", "desktop.ini", "Thumbs.db", ".gitignore"}
BO_QUA_DUOI = (".skill", ".pyc", ".tmp", "~$")
VAN_BAN = (".md", ".txt", ".json", ".csv", ".py", ".yaml", ".yml")


# Thu muc duoc dong vao goi .skill. Ngoai danh sach nay thi khong lay (thu muc nguon cua he
# con chua .skill cu, ban nhap, he con khac — vd 28-KTC-KPI/Tu-Danh-Gia/ la MOT SKILL RIENG).
THU_MUC_GOI = ("references", "assets", "tools", "scripts", "bin", "core")


def phien_ban(skill_md: str) -> str:
    """Doc phien ban tu SKILL.md. Hai cach khai dang dung trong du an:
       a) '**Phien ban: 1.16 — ...**' (ke-hoach, theo-doi-cv, the-thuc, quan-tri, kpi, soan-thao)
       b) dong tieu de '# KTC-Bao-Cao / KTC-RIS v3.21' (bao-cao)
    KHONG suy dien tu ten tep (bai hoc 18/9/2026)."""
    s = io.open(skill_md, encoding="utf-8").read()
    m = re.search(r"\*{0,2}Phi[êe]n b[ảa]n:?\*{0,2}\s*:?\s*v?([0-9]+(?:\.[0-9]+)+)", s)
    if m:
        return m.group(1)
    m = re.search(r"^#.*\bv([0-9]+(?:\.[0-9]+)+)\s*$", s, re.MULTILINE)
    if m:
        return m.group(1)
    raise SystemExit(f"✗ {skill_md}: khong doc duoc phien ban tu noi dung — khong suy dien tu ten tep")


def thu_tep(goc: str):
    """Liet ke (duong dan that, duong dan trong goi) theo thu tu on dinh."""
    ket_qua = []
    # Moi tep .md o GOC thu muc he (SKILL.md, 00-README*.md, CHANGELOG.md…). Truoc chi lay
    # SKILL.md + 00-README.md nen goi quan-tri mat 00-README-ktc-quan-tri.md va CHANGELOG.md.
    for tep in sorted(os.listdir(goc)):
        if tep.endswith(".md") and os.path.isfile(os.path.join(goc, tep)):
            ket_qua.append((os.path.join(goc, tep), tep))
    for ten_tm in THU_MUC_GOI:
        for thu_muc, dirs, files in os.walk(os.path.join(goc, ten_tm)):
            dirs[:] = sorted(d for d in dirs if d not in BO_QUA_TEN)
            for f in sorted(files):
                if f in BO_QUA_TEN or f.endswith(BO_QUA_DUOI) or f.startswith("~$"):
                    continue
                p = os.path.join(thu_muc, f)
                ket_qua.append((p, os.path.relpath(p, goc).replace(os.sep, "/")))
    return ket_qua


def noi_dung(p: str) -> bytes:
    """Doc tep; tep van ban thi chuan hoa xuong dong ve LF."""
    b = io.open(p, "rb").read()
    if p.lower().endswith(VAN_BAN):
        b = b.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("he", help="thu muc he, vd 26-KTC-Soan-Thao-VB")
    ap.add_argument("ten_skill", help="ten thu muc goc trong goi, vd ktc-soan-thao-vb")
    ap.add_argument("--kiem", action="store_true", help="chi so sanh, khong ghi")
    a = ap.parse_args()

    goc = os.path.join(DU_AN, a.he)
    if not os.path.isdir(goc):
        raise SystemExit(f"✗ Khong thay thu muc he: {goc}")
    skill_md = os.path.join(goc, "SKILL.md")
    if not os.path.isfile(skill_md):
        raise SystemExit(f"✗ Thieu {skill_md}")

    pb = phien_ban(skill_md)
    tep = thu_tep(goc)
    dich = os.path.join(goc, f"{a.ten_skill}-v{pb}.skill")

    # So voi goi hien co (neu co) de bao ro se thay doi gi
    # Chon goi gan nhat theo THOI GIAN SUA — so chuoi thi "v1.9" > "v1.15", sai thu tu
    cu = sorted((os.path.join(goc, f) for f in os.listdir(goc) if f.endswith(".skill")),
                key=os.path.getmtime)
    if cu:
        with zipfile.ZipFile(cu[-1]) as z:
            trong_goi = {n.split("/", 1)[1] for n in z.namelist() if "/" in n and not n.endswith("/")}
        moi = {t[1] for t in tep} - trong_goi
        mat = trong_goi - {t[1] for t in tep}
        print(f"── So voi {os.path.basename(cu[-1])}: +{len(moi)} tep moi, -{len(mat)} tep bo ──")
        for f in sorted(moi):
            print(f"  + {f}")
        for f in sorted(mat):
            print(f"  - {f}")
        # CHOT CHAN: dong goi KHONG BAO GIO duoc am tham lam goi nho di. Loi that 5/11/2026:
        # ban dau chi lay SKILL.md + references/ nen kpi-lap-ke-hoach tu 19 con 12 tep
        # (mat assets/ mau .xlsx), the-thuc tu 5 con 3 — khong co gi bao.
        if mat:
            print()
            print(f"✗ DUNG: goi moi thieu {len(mat)} tep ma goi cu co. Neu CO Y bo thi xoa khoi")
            print("  thu muc nguon truoc, hoac them thu muc vao THU_MUC_GOI trong script nay.")
            raise SystemExit(1)

    print(f"── {a.ten_skill} v{pb} — {len(tep)} tep ──")
    if a.kiem:
        print(f"  (--kiem) se ghi: {dich}")
        return 0

    with zipfile.ZipFile(dich, "w", zipfile.ZIP_DEFLATED) as z:
        for that, trong in tep:
            # date_time co dinh -> nen lai cung nguon cho cung so bam (1.3.13)
            info = zipfile.ZipInfo(f"{a.ten_skill}/{trong}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, noi_dung(that))
    print(f"  ✓ {dich}")
    print("  Nho: cap nhat GOI_NGUON trong 29-Cong-Cu/dong_goi_plugin.py neu doi so phien ban.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
