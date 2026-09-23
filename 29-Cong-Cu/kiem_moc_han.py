# -*- coding: utf-8 -*-
"""Canh bao moc han viec dang mo — doc 92-Kinh-Nghiem/05-Known-Issues/Moc-Han.md.

Chi doc bang (mot dong mot moc), khong quet van xuoi Pending.md: van xuoi tron lan ngay phat hien,
ngay cap nhat voi ngay han, quet regex ra canh bao gia.

Phan loai (chi xet trang thai "Mo" va "Chua ro"):
  QUA HAN      han < hom nay          ("Chua ro" -> can xac nhan da lam chua, khong tu ket luan chua lam)
  SAP DEN HAN  0 <= con lai <= N ngay (mac dinh N = 3)

Chay:  python 29-Cong-Cu/kiem_moc_han.py [--gon] [--ngay dd/mm/yyyy] [--truoc N] [--ma-thoat]
  --gon       chi in khi co canh bao (dung cho hook SessionStart)
  --ngay      gia lap hom nay (de thu)
  --ma-thoat  tra ma 1 neu co moc qua han (mac dinh luon 0 de hook khong chan phien)
"""
import argparse
import datetime as dt
import os
import sys

DU_AN = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SO = os.path.join(DU_AN, "92-Kinh-Nghiem", "05-Known-Issues", "Moc-Han.md")
CON_MO = ("mở", "chưa rõ")


def doc_so(p):
    """Tra ve danh sach dict tu bang markdown dau tien co cot 'Hạn'."""
    hang, tieu_de = [], None
    for dong in open(p, encoding="utf-8"):
        dong = dong.strip()
        if not dong.startswith("|"):
            if tieu_de and hang:
                break
            continue
        o = [x.strip() for x in dong.strip("|").split("|")]
        if tieu_de is None:
            if "Hạn" in o:
                tieu_de = o
            continue
        if set("".join(o)) <= set("-: "):
            continue
        hang.append(dict(zip(tieu_de, o)))
    return hang


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gon", action="store_true")
    ap.add_argument("--ngay")
    ap.add_argument("--truoc", type=int, default=3)
    ap.add_argument("--ma-thoat", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    hom_nay = dt.datetime.strptime(a.ngay, "%d/%m/%Y").date() if a.ngay else dt.date.today()

    if not os.path.exists(SO):
        print(f"[moc han] Khong thay so moc han: {os.path.relpath(SO, DU_AN)}")
        return 0
    qua, sap, loi = [], [], []
    for h in doc_so(SO):
        if h.get("Trạng thái", "").lower() not in CON_MO:
            continue
        try:
            han = dt.datetime.strptime(h["Hạn"], "%d/%m/%Y").date()
        except (KeyError, ValueError):
            loi.append(f"{h.get('Mã', '?')}: hạn không đọc được '{h.get('Hạn', '')}'")
            continue
        con = (han - hom_nay).days
        if con < 0:
            qua.append((con, h))
        elif con <= a.truoc:
            sap.append((con, h))

    if a.gon and not (qua or sap or loi):
        return 0
    print(f"=== Mốc hạn việc đang mở ({hom_nay:%d/%m/%Y}) — 92-Kinh-Nghiem/05-Known-Issues/Moc-Han.md ===")
    for con, h in sorted(qua, key=lambda x: x[0]):
        them = " — CẦN XÁC NHẬN đã làm chưa" if h["Trạng thái"].lower() == "chưa rõ" else ""
        print(f"  ✗ QUÁ HẠN {-con} ngày · {h['Mã']} · {h['Đơn vị']} · hạn {h['Hạn']} · {h['Việc']}{them}")
    for con, h in sorted(sap, key=lambda x: x[0]):
        khi = "HÔM NAY" if con == 0 else f"còn {con} ngày"
        print(f"  ⚠ {khi} · {h['Mã']} · {h['Đơn vị']} · hạn {h['Hạn']} · {h['Việc']}")
    for x in loi:
        print(f"  ? {x}")
    if not (qua or sap or loi):
        print(f"  ✓ Không có mốc quá hạn hay đến hạn trong {a.truoc} ngày tới")
    print("  Đóng mốc: đổi Trạng thái sang Xong/Hủy + ghi căn cứ vào Ghi chú, không xóa dòng.")
    return 1 if (a.ma_thoat and qua) else 0


if __name__ == "__main__":
    sys.exit(main())
