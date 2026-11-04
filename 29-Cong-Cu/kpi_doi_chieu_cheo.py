# -*- coding: utf-8 -*-
"""Doi chieu CHEO nhieu ho so tu danh gia KPI — tim cung mot viec khai lech nhau (lenh 28/10/2026, muc 2.5).

Su co that (Quy III/2026): viec mua sam thuoc cua Phong Kham xuat hien o ca ho so Nguyen Ngoc Quang Phuc (B25)
va Do Thanh Cong (dot 2, dot 3) voi so lieu khac nhau; diem cua Phuc doi 97,20 -> 100 -> 97,20 vi khong co nguon
duy nhat va khong doi chieu cheo.

Gom viec theo HAI khoa:
  1. so hieu van ban trong cot minh chung / so hieu (vd "1745/QĐ-CĐKT") — khoa chac chan
  2. noi dung viec da chuan hoa (bo dau, bo dau cau, gop khoang trang) — khoa goi y

Bao cac viec xuat hien o >= 2 ho so ma SL thuc te, % chat luong, % tien do hoac Ket qua nhiem vu khac nhau.
KHONG tu sua tep, KHONG chon ben nao dung — nguoi co tham quyen quyet (nguyen tac 6 cua du an).

Chay:
  python 29-Cong-Cu/kpi_doi_chieu_cheo.py <tep1.xlsx> <tep2.xlsx> [...] [--csv <tep.csv>] [--tat-ca]
Ma thoat: 1 = co lech can xem · 0 = khong thay lech.
"""
import argparse
import csv
import os
import re
import sys
import unicodedata
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kpi_mau as km   # noqa: E402

SO_HIEU = re.compile(r"\b(\d{1,5})\s*/\s*([A-ZĐƯƠÂÊÔ]{2,}(?:[-–][A-ZĐƯƠÂÊÔ]{2,})*)\b")
SO_SANH = ("L", "N", "P", "ket_qua")
TEN_COT = {"L": "SL thực tế", "N": "% chất lượng", "P": "% tiến độ", "ket_qua": "Kết quả nhiệm vụ"}


def kd(s):
    t = unicodedata.normalize("NFD", str(s or "").lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn").replace("đ", "d")
    return " ".join(re.sub(r"[^\w\s]", " ", t).split())


def _so(v):
    if v in (None, ""):
        return None
    try:
        return float(str(v).replace(",", ".").replace("%", "").strip())
    except (TypeError, ValueError):
        return None


def so_hieu_trong(*truong):
    ra = []
    for t in truong:
        for m in SO_HIEU.finditer(str(t or "")):
            ra.append(f"{int(m.group(1))}/{m.group(2)}")
    return sorted(set(ra))


def doc_ho_so(p):
    """Doc mot ho so (bang hoi .xlsx hoac TDG/ke hoach .xlsx) -> danh sach viec. DE DAI: mau la van doc duoc."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        wb = km.mo(p)
    nguon = os.path.basename(p)
    ds = []
    if "B-KPI" in wb.sheetnames:                      # bang hoi do sinh-bang-hoi tao
        ws = wb["B-KPI"]
        for row in ws.iter_rows(min_row=5, values_only=True):
            ma = str(row[0] or "").strip()
            if not re.fullmatch(r"B\d+", ma):
                continue
            r = list(row) + [None] * 20
            ds.append({"nguon": nguon, "ma": ma, "noi_dung": str(r[2] or "").strip(), "G": _so(r[4]),
                       "L": _so(r[8]), "N": _so(r[9]), "P": _so(r[10]), "ket_qua": str(r[11] or "").strip(),
                       "minh_chung": " ".join(str(x or "") for x in (r[7], r[13], r[18]))})
    elif "KPI" in wb.sheetnames and "Ke Hoach" in wb.sheetnames:
        kh, kp = wb["Ke Hoach"], wb["KPI"]
        cot_mc = None
        for c in kp[3]:
            if "minh chứng" in str(c.value or "").lower():
                cot_mc = c.column_letter
        for r in kp.iter_rows(min_row=7):
            b = str(r[1].value or "")
            m = re.match(r"='Ke Hoach'!B(\d+)$", b)
            nd = str(kh[f"B{int(m.group(1))}"].value or "").strip() if m else b.strip()
            if not nd or nd.startswith("="):
                continue
            rk = r[0].row
            if str(r[0].value or "").strip().upper() in ("A", "B", "I", "II", "III", "IV", "V", "VI"):
                continue
            sl_kh = kh[f"F{int(m.group(1))}"].value if m else kp[f"G{rk}"].value
            ds.append({"nguon": nguon, "ma": f"KPI!{rk}", "noi_dung": nd, "G": _so(sl_kh),
                       "L": _so(kp[f"L{rk}"].value), "N": _so(kp[f"N{rk}"].value), "P": _so(kp[f"P{rk}"].value),
                       "ket_qua": "", "minh_chung": " ".join(str(x or "") for x in
                                                             (kp[f"K{rk}"].value,
                                                              kp[f"{cot_mc}{rk}"].value if cot_mc else ""))})
    else:
        raise SystemExit(f"✗ {nguon}: không phải bảng hỏi (sheet B-KPI) cũng không phải tệp Kế hoạch + KPI.")
    return ds


def gom(ds):
    """{khoa: [viec]} — khoa so hieu truoc, con lai gom theo noi dung chuan hoa."""
    theo = {}
    for v in ds:
        khoa = [("số hiệu", s) for s in so_hieu_trong(v["minh_chung"])]
        if not khoa:
            khoa = [("nội dung", kd(v["noi_dung"])[:90])]
        for k in khoa:
            theo.setdefault(k, []).append(v)
    return theo


def lech(nhom):
    """Tra ve danh sach truong lech giua cac ho so trong cung mot nhom."""
    ra = []
    for truong in SO_SANH:
        gia_tri = {}
        for v in nhom:
            if v.get(truong) in (None, ""):
                continue
            gia_tri.setdefault(v[truong], []).append(f"{v['nguon']} [{v['ma']}]")
        if len(gia_tri) > 1:
            ra.append((truong, gia_tri))
    return ra


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("tep", nargs="+", help="các tệp bảng hỏi hoặc TDG cần đối chiếu (≥ 2 tệp)")
    ap.add_argument("--csv", help="ghi kết quả ra tệp CSV")
    ap.add_argument("--tat-ca", action="store_true", help="in cả việc trùng khớp, không chỉ việc lệch")
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(a.tep) < 2:
        print("✗ Cần ít nhất 2 tệp để đối chiếu chéo.")
        return 2

    ds = []
    for p in a.tep:
        ds += doc_ho_so(p)
    theo = gom(ds)

    hang, n_lech = [], 0
    for (loai, khoa), nhom in sorted(theo.items()):
        nguon = {v["nguon"] for v in nhom}
        if len(nguon) < 2:
            continue
        ls = lech(nhom)
        if not ls and not a.tat_ca:
            continue
        n_lech += bool(ls)
        for truong, gia_tri in (ls or [("—", {"(khớp)": [f"{v['nguon']} [{v['ma']}]" for v in nhom]})]):
            hang.append({"khoa": f"{loai}: {khoa}", "truong": TEN_COT.get(truong, truong),
                         "gia_tri": " | ".join(f"{g}: {', '.join(n)}" for g, n in gia_tri.items()),
                         "viec": nhom[0]["noi_dung"][:80], "so_ho_so": len(nguon)})

    print(f"Đối chiếu {len(a.tep)} hồ sơ · {len(ds)} dòng việc · "
          f"{sum(1 for k, v in theo.items() if len({x['nguon'] for x in v}) > 1)} việc xuất hiện ở ≥ 2 hồ sơ.")
    print()
    if not hang:
        print("Không thấy việc nào khai lệch giữa các hồ sơ.")
    else:
        print("| Khóa đối chiếu | Việc | Trường lệch | Giá trị từng hồ sơ |")
        print("|---|---|---|---|")
        for h in hang:
            print(f"| {h['khoa']} | {h['viec']} | {h['truong']} | {h['gia_tri']} |")
        print()
        print(f"**{n_lech} việc khai lệch giữa các hồ sơ** — công cụ không chọn bên nào đúng. Người thực hiện và "
              "người phối hợp đối chiếu lại số liệu gốc, ghi lịch sử thay đổi (giá trị cũ → lý do → căn cứ → "
              "người đổi) trước khi sửa hồ sơ.")
    if a.csv:
        os.makedirs(os.path.dirname(os.path.abspath(a.csv)) or ".", exist_ok=True)
        with open(a.csv, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["khoa", "viec", "truong", "gia_tri", "so_ho_so"])
            w.writeheader()
            w.writerows(hang)
        print(f"\n✓ CSV: {a.csv}")
    return 1 if n_lech else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
