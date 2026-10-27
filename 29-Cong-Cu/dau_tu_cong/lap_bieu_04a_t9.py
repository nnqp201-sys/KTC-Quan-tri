# -*- coding: utf-8 -*-
"""Lap Bieu 04a/CTMTQG-DT (PL II kem QD 64/2026/QD-UBND) - ky bao cao thang 9/2026 cua Truong CDKT.
Nguon mau: sheet 'Bieu 04a-CTMTQG-DT' trich tu PL-III_QD-64-2026 (kho 01-06) -> scratchpad b04a.xlsx."""
import sys, copy
sys.stdout.reconfigure(encoding="utf-8")
import openpyxl

SRC = sys.argv[1]
OUT = sys.argv[2]
wb = openpyxl.load_workbook(SRC, keep_links=False)
ws = wb.active
for _n in list(wb.defined_names):
    del wb.defined_names[_n]
for _n in list(ws.defined_names):
    del ws.defined_names[_n]

for rng in list(ws.merged_cells.ranges):
    if rng.min_row >= 12:
        ws.unmerge_cells(str(rng))

def snap(r):
    return {c: copy.copy(ws.cell(r, c)._style) for c in range(1, 18)}, ws.row_dimensions[r].height

CT = ("Chương trình MTQG xây dựng nông thôn mới, giảm nghèo bền vững và phát triển kinh tế - xã hội "
      "vùng đồng bào DTTS và miền núi giai đoạn 2026 - 2035, giai đoạn I: từ năm 2026 đến năm 2030")
DA = ("Dự án đầu tư, cải tạo các công trình phục vụ người học, nhà giáo và mua sắm bổ sung thiết bị đáp ứng mục tiêu "
      "xây dựng Trường Cao đẳng Kon Tum trở thành trường cao đẳng chất lượng cao giai đoạn 2026 - 2030")
GHI_CHU_DA = "Dự án đang chuẩn bị đầu tư; chưa phát sinh giải ngân"

# (so dong mau, STT, noi dung, von ke hoach UBND giao; None = dong tieu de khong co so)
plan = [
    (12, None, "Tổng số", 260),
    (13, "A", "PHẦN SỐ LIỆU TỔNG HỢP", 260),
    (14, None, "Vốn trong nước", 260),
    (16, "A.I", "Vốn NSNN", 260),
    (17, "I", "Vốn cân đối ngân sách địa phương (cấp tỉnh, cấp xã)", 60),
    (18, None, "Trong đó:", None),
    (20, None, CT, 60),
    (35, "II", "Vốn ngân sách trung ương", 200),
    (36, None, "Trong đó:", None),
    (37, 1, CT, 200),
    (38, None, "Vốn trong nước", 200),
    (52, "B", "PHẦN SỐ LIỆU CHI TIẾT", 260),
    (53, "B.1", "Dự án do cấp tỉnh quản lý", 260),
    (54, None, "Vốn trong nước", 260),
    (56, "B.1.1", "Vốn NSNN", 260),
    (57, "I", "Vốn cân đối ngân sách địa phương", 60),
    (59, "a", CT, 60),
    (60, None, DA, 60),
    (86, "II", "Vốn ngân sách trung ương", 200),
    (89, 1, CT, 200),
    (90, "a", "Vốn trong nước", 200),
    (91, None, DA, 200),
]
styles = {r: snap(r) for r, *_ in plan}
sig_style = {c: copy.copy(ws.cell(181, c)._style) for c in range(1, 18)}
sig_style2 = {c: copy.copy(ws.cell(182, c)._style) for c in range(1, 18)}

ws.delete_rows(12, ws.max_row - 11)

r = 12
last_da = []
for (src, stt, nd, von) in plan:
    st, h = styles[src]
    for c in range(1, 18):
        ws.cell(r, c)._style = copy.copy(st[c])
        ws.cell(r, c).value = None
    if h:
        ws.row_dimensions[r].height = h
    ws.cell(r, 1).value = stt
    ws.cell(r, 2).value = nd
    for c in range(1, 18):
        f = copy.copy(ws.cell(r, c).font)
        f.color = None
        ws.cell(r, c).font = f
    for c in range(1, 18):
        a = copy.copy(ws.cell(r, c).alignment)
        a.vertical = "center"
        if c == 2:
            a.wrap_text = True
        ws.cell(r, c).alignment = a
    if nd == CT:
        ws.row_dimensions[r].height = 105
    elif nd == DA:
        ws.row_dimensions[r].height = 105
        al17 = copy.copy(ws.cell(r, 17).alignment)
        al17.wrap_text = True
        ws.cell(r, 17).alignment = al17
    if von is not None:
        vals = {3: von, 4: 0, 5: von, 6: von, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        for c, v in vals.items():
            ws.cell(r, c).value = v
        if nd in (DA,):
            ws.cell(r, 17).value = GHI_CHU_DA
            last_da.append(r)
    r += 1

r += 1
for i, (txt, sty) in enumerate((("THỦ TRƯỞNG ĐƠN VỊ", sig_style), ("(Ký, đóng dấu, ghi rõ họ tên)", sig_style2))):
    for c in range(1, 18):
        ws.cell(r + i, c)._style = copy.copy(sty[c])
    ws.cell(r + i, 14).value = txt
    ws.merge_cells(start_row=r + i, start_column=14, end_row=r + i, end_column=16)

ws["A1"].value = "ĐƠN VỊ BÁO CÁO: TRƯỜNG CAO ĐẲNG KON TUM"
ws["A3"].value = "BÁO CÁO KẾT QUẢ GIẢI NGÂN VỐN ĐẦU TƯ CÔNG CHƯƠNG TRÌNH MỤC TIÊU QUỐC GIA KẾ HOẠCH NĂM 2026 - THÁNG 9"
ws["A4"].value = "(Kèm theo Báo cáo số      /BC-CĐKT ngày 15 tháng 10 năm 2026 của Trường Cao đẳng Kon Tum)"
ws["G7"].value = "Lũy kế giải ngân từ ngày 01 tháng 01 năm 2026 đến hết ngày 31/8/2026"
ws["N7"].value = "Ước lũy kế giải ngân từ ngày 01 tháng 01 năm 2026 đến hết ngày 30/9/2026"

ws.print_area = f"A1:Q{r+1}"
ws.page_setup.orientation = "landscape"
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0
ws.sheet_properties.pageSetUpPr = openpyxl.worksheet.properties.PageSetupProperties(fitToPage=True)
wb.save(OUT)
print("OK", OUT, "dong cuoi", r + 1)
