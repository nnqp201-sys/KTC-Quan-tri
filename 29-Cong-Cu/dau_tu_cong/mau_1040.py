# -*- coding: utf-8 -*-
"""Đọc mẫu hợp đồng xây dựng công bố kèm QĐ 1040/QĐ-BXD ngày 26/6/2026 (tệp Word trong kho KTC-Database, thư mục 11-Input).

Chỉ ĐỌC kho. Trả về, theo từng Phụ lục, các phần: dkc (Điều kiện chung, theo Điều), dkct (Điều kiện cụ thể, theo Điều).
Dùng trong lap_hop_dong_1040.py để dựng hợp đồng đúng bố cục 4 phần của mẫu.
"""
import os
import re
import sys

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PHU_LUC = {"I": "PHỤ LỤC I", "II": "PHỤ LỤC II", "III": "PHỤ LỤC III", "IV": "PHỤ LỤC IV", "V": "PHỤ LỤC V",
           "VI": "PHỤ LỤC VI", "VII": "PHỤ LỤC VII"}


_REL = ("01-Legal-Database", "01-05- VB cua cac Bo", "01-05-03- Bo Xay dung + Bo GTVT",
        "QD-1040-QD-BXD_Cong-bo-mau-hop-dong-xay-dung_20260626_v1.docx")


def duong_dan_qd1040():
    """QĐ 1040/QĐ-BXD trong kho chính thức (01-05-03); tạm thời còn tìm ở 11-Input nếu chưa được xếp kho."""
    try:
        from duong_dan import kho  # noqa
        p = kho(*_REL)
        if os.path.exists(p):
            return p
        q = kho("11-Input", "Quyết-định-1040-QĐ-BXD.docx")
        if os.path.exists(q):
            return q
    except Exception:
        pass
    for goc in (r"H:\My Drive\KTC-Database", os.environ.get("KTC_DATABASE_DIR", "")):
        if goc:
            p = os.path.join(goc, *_REL)
            if os.path.exists(p):
                return p
    raise FileNotFoundError("Không thấy QĐ 1040/QĐ-BXD trong KTC-Database (01-05-03)")


def doc_dong(path=None):
    d = Document(path or duong_dan_qd1040())
    out = []
    for el in d.element.body.iterchildren():
        if el.tag.endswith("}p"):
            for t in Paragraph(el, d).text.split("\n"):  # một đoạn Word có thể chứa nhiều dòng (ngắt dòng mềm)
                t = t.strip()
                if t:
                    out.append(t)
        elif el.tag.endswith("}tbl"):
            for r in Table(el, d).rows:
                out.append(" | ".join(dict.fromkeys(c.text.strip() for c in r.cells)))
    return out


def _tim(dong, mau, tu=0):
    for i in range(tu, len(dong)):
        if re.match(mau, dong[i]):
            return i
    raise ValueError(mau)


def tach(dong, ma):
    """Tách một Phụ lục: trả dict(dkc={so: [dòng]}, dkct={so: [dòng]}, phan1=[...], phan2=[...], tieu_de=str, ky=[...])."""
    i0 = _tim(dong, r"^" + PHU_LUC[ma] + r"$")
    # phụ lục kế tiếp (hoặc hết tệp)
    keys = list(PHU_LUC)
    k = keys.index(ma)
    i_end = len(dong)
    if k + 1 < len(keys):
        try:
            i_end = _tim(dong, r"^" + PHU_LUC[keys[k + 1]] + r"$", i0 + 1)
        except ValueError:
            pass
    sec = dong[i0:i_end]
    tieu_de = sec[1].strip()
    # bỏ phần mục lục: lấy lần xuất hiện thứ hai của "PHẦN 1."
    ds = [i for i, t in enumerate(sec) if re.match(r"^PHẦN 1\.", t)]
    p1 = ds[1] if len(ds) > 1 else ds[0]
    p2 = _tim(sec, r"^PHẦN 2\.", p1)
    p3 = _tim(sec, r"^PHẦN 3\b", p2)
    p4 = _tim(sec, r"^PHẦN 4\b", p3)
    # khối chữ ký cuối phần 4: dòng chứa "BÊN GIAO THẦU" (bảng)
    ky = None
    for i in range(p4, len(sec)):
        if "BÊN GIAO THẦU" in sec[i] and "|" in sec[i]:
            ky = i
            break
    p4_end = ky if ky is not None else len(sec)

    def theo_dieu(lines):
        r, cur = {}, None
        for t in lines:
            m = re.match(r"^Điều (\d+)\.\s*(.*)$", t)
            if m:
                cur = int(m.group(1))
                r[cur] = {"ten": m.group(2).strip(), "dong": []}
            elif cur is not None:
                r[cur]["dong"].append(t)
        return r

    return dict(
        tieu_de=tieu_de,
        phan1=sec[p1 + 1:p2], phan2=sec[p2 + 1:p3],
        dkc=theo_dieu(sec[p3 + 1:p4]), dkct=theo_dieu(sec[p4 + 1:p4_end]),
    )


if __name__ == "__main__":
    dg = doc_dong()
    for ma in ("II", "III", "V"):
        t = tach(dg, ma)
        print(ma, t["tieu_de"], "| ĐKC:", len(t["dkc"]), "Điều | ĐKCT:", sorted(t["dkct"]))
