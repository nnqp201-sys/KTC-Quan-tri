# -*- coding: utf-8 -*-
"""Dựng v5 QĐ phê duyệt KHLCNT giai đoạn CBĐT từ bản v4 do người dùng đã sửa (07/10/2026).
Chạy: python build_khlcnt_v5.py <mau|sach>  — 'mau' bôi đỏ phần điều chỉnh, 'sach' để chữ đen."""
import sys, copy, docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph

CHE_DO = sys.argv[1] if len(sys.argv) > 1 else "mau"
MAU = CHE_DO == "mau"
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from du_an import ket_qua  # noqa: E402

SRC = ket_qua("2026-09-29", "Soan-Thao-VB", "QD-KHLCNT-giai-doan-CBDT_Du-an-CLC-2026-2030_20260929_v4.docx")
OUT = ket_qua("2026-10-07", "Soan-Thao-VB", "QD-KHLCNT-giai-doan-CBDT_Du-an-CLC-2026-2030_20261007_v9" + ("" if MAU else "-sach") + ".docx")

d = docx.Document(SRC)

def to_do(r):
    if not MAU:
        return
    rPr = r.find(qn("w:rPr"))
    if rPr is None:
        rPr = OxmlElement("w:rPr"); r.insert(0, rPr)
    for c in rPr.findall(qn("w:color")):
        rPr.remove(c)
    col = OxmlElement("w:color"); col.set(qn("w:val"), "FF0000")
    # w:color phải đứng trước w:sz theo schema
    sz = rPr.find(qn("w:sz"))
    if sz is not None:
        sz.addprevious(col)
    else:
        rPr.append(col)

def make_run(base_r, text, red):
    r = copy.deepcopy(base_r)
    for ch in list(r):
        if ch.tag != qn("w:rPr"):
            r.remove(ch)
    t = OxmlElement("w:t"); t.text = text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    r.append(t)
    if red:
        to_do(r)
    return r

def rebuild(par, segs):
    """Dựng lại đoạn từ danh sách (text, red) theo định dạng run đầu tiên."""
    base = par.runs[0]._r
    new = [make_run(base, t, red) for t, red in segs]
    for r in list(par._p.findall(qn("w:r"))):
        par._p.remove(r)
    for r in new:
        par._p.append(r)

def find(prefix):
    for p in d.paragraphs:
        if p.text.strip().startswith(prefix):
            return p
    raise ValueError(prefix)

def insert_after(par, segs, style_src=None):
    src = style_src or par
    new_p = copy.deepcopy(src._p)
    par._p.addnext(new_p)
    np_ = Paragraph(new_p, par._parent)
    rebuild(np_, segs)
    return np_

def remove(par):
    par._p.getparent().remove(par._p)

def split_replace(par, old, new):
    for r in par.runs:
        if old in r.text:
            a, b = r.text.split(old, 1)
            r_a = make_run(r._r, a, False); r_n = make_run(r._r, new, True); r_b = make_run(r._r, b, False)
            r._r.addprevious(r_a); r._r.addprevious(r_n); r._r.addprevious(r_b)
            r._r.getparent().remove(r._r)
            return
    raise ValueError(old)

# ---------------- CĂN CỨ ----------------
LUAT_90 = ("Luật sửa đổi, bổ sung một số điều của Luật Đấu thầu, Luật Đầu tư theo phương thức đối tác công tư, Luật Hải quan, "
           "Luật Thuế giá trị gia tăng, Luật Thuế xuất khẩu, thuế nhập khẩu, Luật Đầu tư, Luật Đầu tư công, Luật Quản lý, sử dụng tài sản công ngày 25/6/2025")
p_dauthau = find("Căn cứ Luật Đấu thầu")
rebuild(p_dauthau, [("Căn cứ Luật Đấu thầu ngày 23/6/2023", False),
                    (" (hợp nhất tại Văn bản hợp nhất số 74/VBHN-VPQH ngày 25/3/2026 của Văn phòng Quốc hội)", True), (";", False)])
p_dtc = find("Căn cứ Luật Đầu tư công")
rebuild(p_dtc, [("Căn cứ Luật Đầu tư công ngày 29/11/2024", False),
                (" (hợp nhất tại Văn bản hợp nhất số 03/VBHN-VPQH ngày 05/2/2026 của Văn phòng Quốc hội)", True), (";", False)])
p_214 = find("Căn cứ Nghị định số 214/2025/NĐ-CP")
rebuild(p_214, [("Căn cứ Nghị định số 214/2025/NĐ-CP ngày 04/8/2025 của Chính phủ quy định chi tiết một số điều và biện pháp thi hành Luật Đấu thầu về lựa chọn nhà thầu", False),
                (" (hợp nhất tại Văn bản hợp nhất số 36/2026/VBHN-NĐ-BTC ngày 23/9/2026 của Bộ Tài chính)", True), (";", False)])
for pre in ("Căn cứ Nghị định số 85/2025/NĐ-CP", "Căn cứ Nghị định số 206/2026/NĐ-CP", "Căn cứ Thông tư số 36/2026/TT-BXD"):
    remove(find(pre))
p_217 = find("Căn cứ Nghị định số 217/2026/NĐ-CP")
p_358 = insert_after(p_214, [("Căn cứ Nghị định số 358/2025/NĐ-CP ngày 31/12/2025 của Chính phủ quy định cơ chế quản lý, tổ chức thực hiện các chương trình mục tiêu quốc gia;", True)])
p_805 = find("Căn cứ Quyết định số 805/QĐ-UBND")
insert_after(p_805, [("Căn cứ Quyết định số 2161/QĐ-CĐKT ngày 29/9/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum phân bổ chi tiết kế hoạch đầu tư công năm 2026 thực hiện Chương trình mục tiêu quốc gia xây dựng nông thôn mới, giảm nghèo bền vững và phát triển kinh tế - xã hội vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026 - 2035, giai đoạn I: từ năm 2026 đến năm 2030;", True)])

# ---------------- ĐIỀU 1 khoản 7 ----------------
p7 = find("7. Giá trị Kế hoạch")
r0 = p7.runs[0]
r_new = make_run(r0._r, "(bằng chữ: Một tỷ, năm trăm mười chín triệu, bảy trăm bảy mươi tám nghìn, hai trăm sáu mươi tám đồng), gồm 02 gói thầu ", True)
# run đầu kết thúc bằng "đồng " -> chèn sau
if not r0.text.endswith(" "):
    r0.text = r0.text + " "
r0._r.addnext(r_new)

insert_after(p7, [("8. Cơ sở lập, phê duyệt Kế hoạch: gói thầu thực hiện trước khi phê duyệt dự án, do người đứng đầu đơn vị được giao nhiệm vụ chuẩn bị dự án phê duyệt theo điểm a khoản 1 Điều 38 và khoản 2 Điều 40 của Luật Đấu thầu; hình thức chỉ định thầu rút gọn theo khoản 4 Điều 78 (gói thầu dịch vụ tư vấn thuộc dự án có giá gói thầu không quá 03 tỷ đồng) và Điều 80 của Nghị định số 214/2025/NĐ-CP; chỉ định thầu rút gọn không quy định phương thức lựa chọn nhà thầu.", True)], style_src=find("5. Thời gian thực hiện"))

p_k2 = find("2. Giá gói thầu được cập nhật")
p_k3 = insert_after(p_k2, [("3. Việc ký kết, thanh toán hợp đồng chỉ thực hiện trong phạm vi kế hoạch vốn do cấp có thẩm quyền giao và dự toán đã được phê duyệt.", True)])
insert_after(p_k3, [("4. Phòng Tổng hợp - Hành chính và Quản trị đăng tải Kế hoạch lựa chọn nhà thầu trên Hệ thống mạng đấu thầu quốc gia theo quy định.", True)])

# ---------------- BẢNG KHLCNT ----------------
tbl = d.tables[2]
rows = list(tbl.rows)
r_ks, r_bc, r_qlda = rows[2], rows[3], rows[4]

def set_cell(cell, text, red=True):
    par = cell.paragraphs[0]
    base = par.runs[0]._r
    for r in list(par._p.findall(qn("w:r"))):
        par._p.remove(r)
    par._p.append(make_run(base, text, red))

set_cell(r_ks.cells[2], "Tư vấn khảo sát xây dựng, lập Báo cáo kinh tế - kỹ thuật Dự án")
set_cell(r_ks.cells[3], "Khảo sát xây dựng; lập Báo cáo kinh tế - kỹ thuật, gồm thiết kế bản vẽ thi công của Dự án")
set_cell(r_ks.cells[4], "852.345.246")
set_cell(r_ks.cells[11], "120 ngày")
r_bc._tr.getparent().remove(r_bc._tr)
set_cell(r_qlda.cells[0], "2")
set_cell(r_qlda.cells[3], "Tư vấn quản lý dự án từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án")
set_cell(r_qlda.cells[11], "Từ ngày hợp đồng có hiệu lực đến khi quyết toán hoàn thành dự án, theo thời gian thực hiện dự án được cấp có thẩm quyền phê duyệt")
for hang in (r_ks, r_qlda):
    set_cell(hang.cells[6], "Chỉ định thầu rút gọn")
    set_cell(hang.cells[7], "")

# ---------------- GHI CHÚ ----------------
p_gc = find("Ghi chú: (*)")
split_replace(p_gc, "Tổng giá trị 3 gói thầu", "Tổng giá trị 02 gói thầu")
try:
    split_replace(p_gc, "Cả 3 gói", "Cả 02 gói")
except ValueError:
    pass
p_gc.runs[-1]._r.addnext(make_run(p_gc.runs[-1]._r, " Gói thầu số 1 gồm hai khoản mục khảo sát xây dựng (93.995.981 đồng) và lập Báo cáo kinh tế - kỹ thuật (758.349.265 đồng) tại Phụ lục Quyết định số 2158/QĐ-CĐKT. Gói thầu số 2 thực hiện từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án, có thời gian thực hiện dài hơn 01 năm; giá gói thầu được xác định trên cơ sở toàn bộ thời gian thực hiện gói thầu (khoản 2 Điều 37 Luật Đấu thầu).", True))

# ---------------- CHUẨN HÓA THỂ THỨC (897 format-reviewer) ----------------
# viết hoa chữ cái đầu sau dấu hai chấm: "giai đoạn I: từ năm" -> "giai đoạn I: Từ năm"
for par in list(d.paragraphs):
    for r in par.runs:
        if "I: từ năm" in r.text:
            r.text = r.text.replace("I: từ năm", "I: Từ năm")
# co lưới bảng phụ lục về <= vùng chữ ngang (14.572 twip) và lặp hàng tiêu đề
W = 14572
grid = tbl._tbl.tblGrid
cols = grid.findall(qn("w:gridCol"))
tong = sum(int(c.get(qn("w:w"))) for c in cols)
if tong > W:
    he_so = W / tong
    for c in cols:
        c.set(qn("w:w"), str(int(int(c.get(qn("w:w"))) * he_so)))
    for tc in tbl._tbl.iter(qn("w:tcW")):
        if tc.get(qn("w:type")) in (None, "dxa"):
            tc.set(qn("w:w"), str(int(int(tc.get(qn("w:w"))) * he_so)))
    tw = tbl._tbl.tblPr.find(qn("w:tblW"))
    if tw is not None:
        tw.set(qn("w:type"), "dxa"); tw.set(qn("w:w"), str(W))
for hang in list(tbl.rows)[:2]:
    trPr = hang._tr.get_or_add_trPr()
    if trPr.find(qn("w:tblHeader")) is None:
        trPr.append(OxmlElement("w:tblHeader"))

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
d.save(OUT)
print("saved", OUT)
for p in d.paragraphs:
    if p.text.strip():
        print(p.text.strip()[:150])
for r in d.tables[2].rows:
    print([c.text.strip()[:30] for c in r.cells])
