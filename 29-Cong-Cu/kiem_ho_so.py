# -*- coding: utf-8 -*-
"""Kiem ho so tham dinh NGAY TRUOC KHI GUI (tham dinh lan 4, ChatGPT F4-03, Copilot, Grok).

Su co that 27/9/2026: 4 tep trong Ho-So-Tham-Dinh-Vong-4/4-Van-ban bi mo trong Word, chap nhan toan bo thay doi va luu
SAU khi lap ho so -> ben tham dinh nhan tep "_TrackChanges" khong con danh dau; ma bam khong con khop danh muc.

Kiem:
  1. Moi tep trong danh muc 00-DANH-MUC-HO-SO.md con ton tai, dung SHA-256 da ghi.
  2. Tep ten co "_TrackChanges" phai con danh dau (w:ins / w:del / rPrChange ...) — 0 danh dau = LOI.
  3. Tep .docx/.zip hop le (chu ky PK, testzip).
  4. --khoa: dat thuoc tinh CHI DOC cho tep _TrackChanges (Windows: attrib +R) de tranh luu de khi mo xem.
Ma thoat: 0 = sach, 1 = co loi.

    python 29-Cong-Cu/kiem_ho_so.py <thu-muc-ho-so> [--khoa]
"""
import argparse
import hashlib
import io
import os
import re
import stat
import sys
import zipfile

DAU_VET = re.compile(rb"<w:(ins|del|moveFrom|moveTo|rPrChange|pPrChange|sectPrChange|tblPrChange|trPrChange)\b")


def dem_dau_vet(p: str) -> int:
    n = 0
    with zipfile.ZipFile(p) as z:
        for ten in z.namelist():
            if ten.startswith("word/") and ten.endswith(".xml"):
                n += len(DAU_VET.findall(z.read(ten)))
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("thu_muc")
    ap.add_argument("--khoa", action="store_true")
    a = ap.parse_args()
    dm = os.path.join(a.thu_muc, "00-DANH-MUC-HO-SO.md")
    loi, dong = [], 0
    if not os.path.isfile(dm):
        raise SystemExit(f"Không thấy {dm}")
    for line in io.open(dm, encoding="utf-8"):
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]{64})`", line)
        if not m:
            continue
        dong += 1
        nhom, ten, co, sha = m.groups()
        p = os.path.join(a.thu_muc, *nhom.split("/"), ten)
        if not os.path.isfile(p):
            loi.append(f"THIẾU: {nhom}/{ten}")
            continue
        b = open(p, "rb").read()
        if hashlib.sha256(b).hexdigest() != sha:
            loi.append(f"MÃ BĂM KHÁC danh mục (tệp đã bị mở, lưu lại?): {nhom}/{ten}")
        if ten.lower().endswith((".docx", ".zip")):
            if not b.startswith(b"PK\x03\x04"):
                loi.append(f"KHÔNG PHẢI ZIP/DOCX hợp lệ: {nhom}/{ten}")
                continue
            try:
                with zipfile.ZipFile(p) as z:
                    if z.testzip() is not None:
                        loi.append(f"ZIP hỏng: {nhom}/{ten}")
            except zipfile.BadZipFile:
                loi.append(f"ZIP hỏng: {nhom}/{ten}")
                continue
        if "_TrackChanges" in ten and ten.lower().endswith(".docx"):
            n = dem_dau_vet(p)
            print(f"  · {ten}: {n} đánh dấu")
            if n == 0:
                loi.append(f"TrackChanges KHÔNG còn đánh dấu (đã bị chấp nhận thay đổi?): {nhom}/{ten}")
            if a.khoa:
                os.chmod(p, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
    print(f"Đã kiểm {dong} tệp trong danh mục.")
    for l in loi:
        print("  ✗", l)
    print("KẾT LUẬN:", "CÓ LỖI — KHÔNG GỬI" if loi else "SẠCH — gửi được" + (" (đã đặt chỉ đọc cho tệp TrackChanges)" if a.khoa else ""))
    return 1 if loi or not dong else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
