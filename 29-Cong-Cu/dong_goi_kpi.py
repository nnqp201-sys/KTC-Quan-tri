# -*- coding: utf-8 -*-
"""Dong bo va dong goi skill ktc-kpi-lap-ke-hoach (28-KTC-KPI) — lenh sua 24/9/2026, muc 2 va 10.

Nguon duy nhat -> ban sao trong he (sua o NGUON, khong sua ban sao):
  20-Chuan-Chung/19-Quy-Tac-KPI.md          -> 28-KTC-KPI/references/Skill-Library/19-Quy-Tac-KPI.md
  29-Cong-Cu/{kpi_calc,kpi_mau,validate_plan}.py -> 28-KTC-KPI/scripts/
  KTC-Database/03-Templates/03-12-.../Mau-KeHoach-DanhGia_*.xlsx (6 tep) -> 28-KTC-KPI/assets/  (giu nguyen byte)
  Danh muc TB 1052 (kho 02)                -> 28-KTC-KPI/references/data/he-so-san-pham-TB1052.csv (trich lai)
Ban sao bi sua tay khac nguon -> BAO LOI, khong ghi de im lang (bai hoc 14/9/2026: goi lech nguon roi).

Chay:  python 29-Cong-Cu/dong_goi_kpi.py --dong-bo            # chi dong bo, kiem hash
       python 29-Cong-Cu/dong_goi_kpi.py --dong-goi [--ghi-de-ban-sao]
"""
import argparse
import glob
import hashlib
import os
import shutil
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DU_AN = os.path.dirname(HERE)
HE = os.path.join(DU_AN, "28-KTC-KPI")
TEN = "ktc-kpi-lap-ke-hoach"
SCRIPT = ["kpi_calc.py", "kpi_mau.py", "validate_plan.py"]
sys.path.insert(0, HERE)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def cap(ghi_de):
    """(nguon, dich) can dong bo."""
    import duong_dan
    ds = [(os.path.join(DU_AN, "20-Chuan-Chung", "19-Quy-Tac-KPI.md"),
           os.path.join(HE, "references", "Skill-Library", "19-Quy-Tac-KPI.md"))]
    ds += [(os.path.join(HERE, s), os.path.join(HE, "scripts", s)) for s in SCRIPT]
    db = duong_dan.ktc_database()
    mau = sorted(glob.glob(os.path.join(db, "03-Templates", "03-12-*", "Mau-KeHoach-DanhGia_*.xlsx")))
    if len(mau) != 6:
        raise SystemExit(f"✗ Kho có {len(mau)} mẫu Kế hoạch, cần đúng 6 — dừng, hỏi người dùng.")
    ds += [(m, os.path.join(HE, "assets", os.path.basename(m))) for m in mau]
    return ds


def dong_bo(ghi_de=False):
    loi = []
    for src, dst in cap(ghi_de):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst) and sha(dst) != sha(src):
            # Ban sao khac nguon: neu ban sao MOI HON nguon (mtime) -> co the bi sua tay
            if os.path.getmtime(dst) > os.path.getmtime(src) and not ghi_de:
                loi.append(f"{os.path.relpath(dst, DU_AN)} khác nguồn và mới hơn nguồn — có thể bị sửa tay. "
                           "Sửa ở nguồn rồi chạy lại, hoặc --ghi-de-ban-sao nếu chắc chắn.")
                continue
        if not os.path.exists(dst) or sha(dst) != sha(src):
            shutil.copy2(src, dst)
            print(f"  ↻ {os.path.relpath(dst, DU_AN)}")
    import trich_danh_muc_tb1052 as t
    if t.main([]) != 0:
        loi.append("Trích Danh mục TB 1052 thất bại")
    return loi


def dong_goi():
    ver = None
    for dong in open(os.path.join(HE, "SKILL.md"), encoding="utf-8"):
        if dong.startswith("## Phiên bản:"):
            ver = dong.split("v", 1)[1].split()[0]
            break
    if not ver:
        raise SystemExit("✗ SKILL.md thiếu dòng '## Phiên bản: vX.Y'")
    ra = os.path.join(HE, f"{TEN}-v{ver}.skill")
    with zipfile.ZipFile(ra, "w", zipfile.ZIP_DEFLATED) as z:
        for r, ds, fs in os.walk(HE):
            ds[:] = sorted(d for d in ds if d not in ("__pycache__",))
            for f in sorted(fs):
                if f in ("desktop.ini", "TEST-REPORT.md") or f.endswith((".skill", ".pyc")):
                    continue
                p = os.path.join(r, f)
                z.write(p, os.path.join(TEN, os.path.relpath(p, HE)).replace(os.sep, "/"))
    print(f"✓ Đóng gói {os.path.relpath(ra, DU_AN)} ({len(zipfile.ZipFile(ra).namelist())} tệp)")
    return ra


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--dong-bo", action="store_true")
    ap.add_argument("--dong-goi", action="store_true")
    ap.add_argument("--ghi-de-ban-sao", action="store_true")
    a = ap.parse_args(argv)
    loi = dong_bo(a.ghi_de_ban_sao)
    if loi:
        print("✗ Đồng bộ có lỗi:\n  " + "\n  ".join(loi))
        return 1
    print("✓ Đồng bộ xong — bản sao khớp nguồn")
    if a.dong_goi:
        dong_goi()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
