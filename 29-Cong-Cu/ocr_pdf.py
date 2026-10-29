# -*- coding: utf-8 -*-
"""OCR tiếng Việt cho PDF scan / ảnh (hồ sơ năng lực nhà thầu, văn bản scan).

Dùng:
    python 29-Cong-Cu/ocr_pdf.py <tep.pdf|anh.png> [--trang 1-5] [--dpi 220] [--ra ket_qua.md]

Cần: Tesseract (winget install UB-Mannheim.TesseractOCR) + dữ liệu tiếng Việt vie.traineddata.
Đường dẫn tìm theo thứ tự: biến môi trường KTC_TESSERACT / KTC_TESSDATA → PATH →
    C:/Program Files/Tesseract-OCR/tesseract.exe ; ~/.ktc-ocr/tessdata (có vie.traineddata).

Quy ước (NT-6 AI không thay dữ liệu gốc): kết quả OCR là BẢN ĐỌC TỰ ĐỘNG, luôn kèm độ tin cậy từng trang và
dòng cảnh báo "cần đối chiếu bản gốc". Số hiệu, ngày, số chứng chỉ, tên người, số tiền phải soi lại trên ảnh.
Trang xoay ngang/ngược: thử xoay 90/180/270° khi độ tin cậy thấp.
"""
import argparse
import csv
import io
import os
import shutil
import subprocess
import sys
import tempfile

import pymupdf
from PIL import Image

CANH_BAO = ("> **OCR tự động, cần đối chiếu bản gốc.** Số hiệu, ngày tháng, số chứng chỉ, tên người, số tiền "
            "phải soi lại trên ảnh trước khi dùng làm căn cứ.")


def tim_tesseract():
    p = os.environ.get("KTC_TESSERACT") or shutil.which("tesseract")
    if p and os.path.exists(p):
        return p
    mac_dinh = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    if os.path.exists(mac_dinh):
        return mac_dinh
    raise SystemExit("Chưa cài Tesseract. Chạy: winget install --id UB-Mannheim.TesseractOCR --source winget")


def tim_tessdata():
    for d in (os.environ.get("KTC_TESSDATA"), os.path.expanduser("~/.ktc-ocr/tessdata"),
              "C:/Program Files/Tesseract-OCR/tessdata"):
        if d and os.path.exists(os.path.join(d, "vie.traineddata")):
            return d
    raise SystemExit("Thiếu vie.traineddata. Tải tessdata_best/vie.traineddata vào ~/.ktc-ocr/tessdata/")


def _chay(tess, tessdata, anh, lang="vie"):
    """Trả (văn bản theo dòng, độ tin cậy trung bình)."""
    r = subprocess.run([tess, anh, "stdout", "--tessdata-dir", tessdata, "-l", lang, "--psm", "3", "tsv"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit("Tesseract lỗi: " + r.stderr[:300])
    dong = {}
    conf = []
    for row in csv.DictReader(io.StringIO(r.stdout), delimiter="\t", quoting=csv.QUOTE_NONE):
        t = (row.get("text") or "").strip()
        try:
            c = float(row.get("conf", "-1"))
        except ValueError:
            c = -1
        if not t or c < 0:
            continue
        key = (row["page_num"], row["block_num"], row["par_num"], row["line_num"])
        dong.setdefault(key, []).append(t)
        conf.append(c)
    van = "\n".join(" ".join(v) for v in dong.values())
    return van, (sum(conf) / len(conf) if conf else 0.0)


def ocr_anh(im, tess, tessdata):
    """Thử góc 0°, rồi 90/270/180° nếu độ tin cậy < 60. Trả (văn bản, độ tin cậy, góc)."""
    tot = None
    with tempfile.TemporaryDirectory() as tmp:
        for goc in (0, 90, 270, 180):
            x = im.rotate(-goc, expand=True) if goc else im
            p = os.path.join(tmp, f"t{goc}.png")
            x.save(p)
            van, c = _chay(tess, tessdata, p)
            if tot is None or c > tot[1]:
                tot = (van, c, goc)
            if tot[1] >= 60:
                break
    return tot


def doc_khoang(s, n):
    if not s:
        return list(range(n))
    out = []
    for phan in s.split(","):
        if "-" in phan:
            a, b = phan.split("-")
            out += list(range(int(a) - 1, int(b)))
        else:
            out.append(int(phan) - 1)
    return [i for i in out if 0 <= i < n]


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tep")
    ap.add_argument("--trang", default="", help="vd 1-5,9 (mặc định: tất cả)")
    ap.add_argument("--dpi", type=int, default=220)
    ap.add_argument("--ra", default="", help="ghi kết quả ra tệp .md (mặc định: in ra màn hình)")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    tess, tessdata = tim_tesseract(), tim_tessdata()

    trang = []
    if a.tep.lower().endswith(".pdf"):
        d = pymupdf.open(a.tep)
        for i in doc_khoang(a.trang, len(d)):
            pm = d[i].get_pixmap(dpi=a.dpi)
            trang.append((i + 1, Image.frombytes("RGB", (pm.width, pm.height), pm.samples)))
    else:
        trang.append((1, Image.open(a.tep).convert("RGB")))

    out = [f"# OCR: {os.path.basename(a.tep)}", "", CANH_BAO, ""]
    for so, im in trang:
        van, c, goc = ocr_anh(im, tess, tessdata)
        nhan = f"## Trang {so} (độ tin cậy {c:.0f}%" + (f", xoay {goc}°" if goc else "") + ")"
        if c < 60:
            nhan += " — THẤP, đọc lại bằng mắt"
        out += [nhan, "", van, ""]
        print(f"  trang {so}: {c:.0f}%", file=sys.stderr)
    kq = "\n".join(out)
    if a.ra:
        with open(a.ra, "w", encoding="utf-8") as f:
            f.write(kq)
        print(a.ra)
    else:
        print(kq)


if __name__ == "__main__":
    main(sys.argv[1:])
