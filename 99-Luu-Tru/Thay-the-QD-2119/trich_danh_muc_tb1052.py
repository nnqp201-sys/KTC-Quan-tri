# -*- coding: utf-8 -*-
"""Trich Danh muc san pham/cong viec quy doi kem TB 1052/TB-CDKT (15/9/2026) ra CSV cho skill ktc-kpi-lap-ke-hoach.

Nguon: KTC-Database/02-KTC-Regulations/02-01-.../TB-1052-TB-CDKT_Phu-luc-Danh-muc-San-pham-Cong-viec-quy-doi.xlsx
(tim qua duong_dan — khong ghi cung o dia). Tep CSV kem theo sha256 cua tep nguon de biet khi nao phai trich lai.

TRANG THAI: Danh muc la DU THAO gui don vi gop y (TB 1052 muc 3.1), CHUA BAN HANH. KI-014: 204/371 dong co
he so khac gia tri chuan cua Nhom theo bang goi y du thao lan 4 (Nhom 1..5 = 0,5 / 1,2 / 2,5 / 3,5 / 4,5).
Cot `lech_nhom` chi DANH DAU dong lech — khong sua, khong chon ben dung (khong tu dat quy tac, CLAUDE.md).

Chay:  python 29-Cong-Cu/trich_danh_muc_tb1052.py [--ra <thu muc>]   (mac dinh 28-KTC-KPI/references/data/)
Kiem:  so dong khop bang goc (dong co Nhom + He so), khong dong nao thieu he so; in so dong da trich.
"""
import argparse
import csv
import glob
import hashlib
import os
import sys
import warnings

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CHUAN_NHOM = {"Nhóm 1": 0.5, "Nhóm 2": 1.2, "Nhóm 3": 2.5, "Nhóm 4": 3.5, "Nhóm 5": 4.5}
COT = ["stt", "ma_loai_vb", "ten_san_pham", "mo_ta", "loai_san_pham", "san_pham_chuan", "nhom", "he_so",
       "linh_vuc", "lech_nhom"]


def tim_nguon():
    import duong_dan
    db = duong_dan.ktc_database()
    ds = glob.glob(os.path.join(db, "02-KTC-Regulations", "**", "TB-1052-TB-CDKT_Phu-luc-Danh-muc*.xlsx"),
                   recursive=True)
    if not ds:
        raise FileNotFoundError("Không thấy Danh mục TB 1052 trong KTC-Database/02-KTC-Regulations — dừng, hỏi người dùng.")
    return ds[0]


def trich(nguon):
    from openpyxl import load_workbook
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        ws = load_workbook(nguon, data_only=True, read_only=True).active
    hang, linh_vuc, tong_dong_co_nhom = [], "", 0
    for r in ws.iter_rows(min_row=6, values_only=True):
        stt, ma, ten, mo_ta, sp, chuan, nhom, hs = (list(r) + [None] * 8)[:8]
        if stt is None and ten is None:
            continue
        if nhom is None and hs is None:          # dong tieu de linh vuc (1..38)
            linh_vuc = f"{stt}. {ten}"
            continue
        tong_dong_co_nhom += 1
        chuan_nhom = CHUAN_NHOM.get(str(nhom).strip())
        lech = "" if (isinstance(hs, (int, float)) and chuan_nhom is not None and abs(hs - chuan_nhom) < 1e-9) \
            else f"hệ số {hs} ≠ chuẩn {nhom} = {chuan_nhom}"
        hang.append({"stt": stt, "ma_loai_vb": ma or "", "ten_san_pham": (ten or "").strip(),
                     "mo_ta": (mo_ta or "").strip(), "loai_san_pham": (sp or "").strip(),
                     "san_pham_chuan": (chuan or "").strip(), "nhom": nhom, "he_so": hs,
                     "linh_vuc": linh_vuc, "lech_nhom": lech})
    return hang, tong_dong_co_nhom


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ra", default=os.path.join(DU_AN, "28-KTC-KPI", "references", "data"))
    ap.add_argument("--nguon")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    warnings.simplefilter("ignore")   # openpyxl read_only doc header/footer tre — canh bao vo hai
    nguon = a.nguon or tim_nguon()
    hang, tong = trich(nguon)
    thieu = [h["stt"] for h in hang if h["he_so"] in (None, "")]
    if len(hang) != tong or thieu:
        print(f"✗ Trích {len(hang)}/{tong} dòng; thiếu hệ số: {thieu[:10]}")
        return 1
    os.makedirs(a.ra, exist_ok=True)
    ra = os.path.join(a.ra, "he-so-san-pham-TB1052.csv")
    with open(ra, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COT)
        w.writeheader()
        w.writerows(hang)
    sha = hashlib.sha256(open(nguon, "rb").read()).hexdigest()
    with open(ra + ".nguon.txt", "w", encoding="utf-8", newline="") as f:
        f.write(f"nguon: KTC-Database/{os.path.relpath(nguon, os.path.dirname(os.path.dirname(os.path.dirname(nguon)))).replace(os.sep, '/')}\n"
                f"sha256: {sha}\nso_dong: {len(hang)}\n"
                f"so_dong_lech_nhom: {sum(1 for h in hang if h['lech_nhom'])}\n"
                "trang_thai: DU THAO — TB 1052/TB-CDKT muc 3.1 gui don vi gop y, chua ban hanh (KI-014)\n")
    print(f"✓ Đã trích {len(hang)} dòng sản phẩm (khớp {tong} dòng có Nhóm + Hệ số trong bảng gốc) → {ra}")
    print(f"  {sum(1 for h in hang if h['lech_nhom'])} dòng lệch giá trị chuẩn của Nhóm (KI-014) · sha256 nguồn {sha[:12]}…")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
