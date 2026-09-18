# -*- coding: utf-8 -*-
"""Hoi quy C12 (dau vao trung KTC-Database) va C13 (ghi cung o dia) — DL-20260918-005.

Moi phep kiem co ca THU NGUOC (biet chac sai) — LL-20260914-001: phep kiem hong luon bao "sach".
Chay tren du an gia trong thu muc tam, khong dung du an that.
"""
import os
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import kiem_tra_he_thong as k  # noqa: E402

sai = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


def ghi(p, noi_dung, nhi_phan=False):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "wb" if nhi_phan else "w", **({} if nhi_phan else {"encoding": "utf-8"})).write(noi_dung)


def chay(ham, *a, **kw):
    k.loi.clear(); k.canh_bao.clear()
    ham(*a, **kw)
    return list(k.loi), list(k.canh_bao)


with tempfile.TemporaryDirectory() as t:
    du_an = os.path.join(t, "KTC-Quan-tri"); kho = os.path.join(t, "KTC-Database")
    cap = os.path.join(du_an, "10-Dau-Vao", "02-Cap-Truong")
    ghi(os.path.join(kho, "02-KTC-Regulations", "CTCT.xlsx"), b"BAN-GOC-2026", True)
    ghi(os.path.join(kho, "02-KTC-Regulations", "KH-Quy.xlsx"), b"KH-QUY", True)

    print("== C12 ==")
    ghi(os.path.join(du_an, "10-Dau-Vao", "01-Dau-Moi-Nop", "2026-09", "P-THHC", "BC.xlsx"), b"RIENG", True)
    loi, _ = chay(k.c12_trung_kho, du_an, kho)
    kiem(not loi, "tệp không trùng kho -> sạch")

    ghi(os.path.join(cap, "02-Quy", "2026-Q3", "KH.xlsx"), b"KH-QUY", True)
    loi, _ = chay(k.c12_trung_kho, du_an, kho)
    kiem(len(loi) == 1 and "02-Quy" in loi[0], "ca ngược: tệp trùng kho, không có trong ngoại lệ -> LỖI")

    ghi(os.path.join(cap, "01-Nam", "2026", "CTCT.xlsx"), b"BAN-GOC-2026", True)
    ghi(os.path.join(du_an, k.DANH_MUC_TRO),
        "# DM\n\n## Ngoại lệ đã duyệt\n\n| Tệp | Kho |\n|---|---|\n| `01-Nam/2026/CTCT.xlsx` | x |\n\n## Khác\n")
    loi, _ = chay(k.c12_trung_kho, du_an, kho)
    kiem(len(loi) == 1 and "02-Quy" in loi[0], "tệp trong ngoại lệ đã duyệt -> bỏ qua; tệp ngoài ngoại lệ vẫn LỖI")

    loi, cb = chay(k.c12_trung_kho, du_an, os.path.join(t, "khong-co"))
    kiem(not loi and cb, "không tìm thấy kho -> cảnh báo, không báo sạch giả")

    print("== C13 ==")
    ghi(os.path.join(du_an, "29-Cong-Cu", "tot.py"), 'P = os.path.join(ktc_database(), "02")\n')
    loi, _ = chay(k.c13_o_dia_tuyet_doi, du_an)
    kiem(not loi, "đường dẫn tương đối -> sạch")
    ghi(os.path.join(du_an, "29-Cong-Cu", "xau.py"), 'P = r"D:\\.CLAUDE code\\KTC-Database"\n')
    ghi(os.path.join(du_an, "23-KTC-Ke-Hoach", "SKILL.md"), "Đọc `G:/.CLAUDE code/KTC-Database/01`\n")
    loi, _ = chay(k.c13_o_dia_tuyet_doi, du_an)
    kiem(len(loi) == 2, f"ca ngược: ổ D: trong .py và ổ G: trong SKILL.md -> 2 LỖI (thực tế {len(loi)})")

print("KET LUAN:", "CO LOI " + str(sai) if sai else "SACH")
sys.exit(1 if sai else 0)
