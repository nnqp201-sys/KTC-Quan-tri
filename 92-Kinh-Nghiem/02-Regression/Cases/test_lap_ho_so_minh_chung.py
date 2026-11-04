# -*- coding: utf-8 -*-
"""Hoi quy lap_ho_so_minh_chung.py (lenh 28/10/2026, muc 3.3).

Su co that (phien 1/10/2026): bang tra minh chung khop SAI vi khoa so ('1', 3 lan lon trong cung mot cot nhu
tep cua Do Thanh Cong) -> hang loat dong bao "CẦN BỔ SUNG"; va bao "da day du" khi CHUA doc lai tep.
Ca thu nay khoa hai dieu do: khoa tra cuu luon chuan hoa ve chuoi, va bat buoc doc lai .docx (dem dong,
quet chuoi cam, khong con o trong).
"""
import os
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import lap_ho_so_minh_chung as lh   # noqa: E402

sai = []
TMP = tempfile.mkdtemp(prefix="ktc_hs_")


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


print("== Khóa tra cứu — chuẩn hóa kiểu (ca lỗi thật 1/10/2026) ==")
kiem(lh.khoa("B25") == lh.khoa(" b25 ") == "B25", "khóa 'B25', ' b25 ' chuẩn hóa về 'B25'")
kiem(lh.khoa(25) == lh.khoa("25") == "B25", "khóa số 25 và chuỗi '25' cùng về 'B25' (cột stt lẫn kiểu)")
kiem(lh.khoa(None) == "" and lh.khoa("") == "", "ô trống → khóa rỗng, không vỡ")

csv_p = os.path.join(TMP, "tra.csv")
with open(csv_p, "w", encoding="utf-8-sig", newline="") as f:
    f.write("ma_viec,so_hieu,nguon\n")
    f.write("1,100/QĐ-CĐKT,Hồ sơ công việc\n")          # khoa so dang chuoi
    f.write("B2,101/BC-CĐKT,Hồ sơ công việc\n")          # khoa chuoi
    f.write(" b3 ,102/KH-CĐKT,Hồ sơ công việc\n")        # khoa co khoang trang
tra = lh.doc_tra_minh_chung(csv_p)
kiem(set(tra) == {"B1", "B2", "B3"}, "CSV có khóa lẫn số và chuỗi → đọc ra đủ 3 khóa chuẩn")
kiem(tra["B1"]["so_hieu"] == "100/QĐ-CĐKT", "khóa số '1' tra được bằng 'B1'")
kiem(lh.doc_tra_minh_chung(None) == {}, "không có bảng tra → trả về rỗng, không vỡ")

print("== Dựng .docx và ĐỌC LẠI (mục 3.4) ==")
tt = [("Họ và tên", "Nguyễn Văn A"), ("Chức vụ, đơn vị", "Chuyên viên, phòng Thử nghiệm")]
I = [("Tổng điểm đánh giá đạt từ 90 điểm trở lên", "Đạt — 95,00/100 điểm", "Bản tự đánh giá", None),
     ("Điều kiện thiếu nguồn", "Thiếu dữ liệu — người dùng tự xác nhận", "QĐ 1923, Đ19.1a", "[THIẾU DỮ LIỆU]")]
II = [(str(i % 6 + 1), f"Việc thử số {i}", "1/1", "Hoàn thành đúng hạn", f"Văn bản {100 + i}/BC-CĐKT", None)
      for i in range(7)]
noi_bo = lh.dung_docx(os.path.join(TMP, "noi-bo.docx"), tt, I, II, ["Ghi chú thử"], "Quý III năm 2026",
                      noi_bo=True)
loi = lh.kiem_dau_ra(noi_bo, len(II), ban_nop=False)
kiem(not loi, f"Bản nội bộ đọc lại: đủ {len(II)} dòng việc, không ô trống ({loi})")
kiem(lh.kiem_dau_ra(noi_bo, len(II) + 1, ban_nop=False), "NGƯỢC: đếm lệch số dòng việc → báo lỗi")
kiem(any("chuỗi cấm" in x for x in lh.kiem_dau_ra(noi_bo, len(II), ban_nop=True)),
     "NGƯỢC: bản nội bộ (có cờ [THIẾU DỮ LIỆU]) không được dùng làm bản nộp")

nop = lh.dung_docx(os.path.join(TMP, "nop.docx"), tt, [(a, b, c, None) for a, b, c, _ in I], II,
                   ["Ghi chú thử"], "Quý III năm 2026", noi_bo=False)
kiem(not lh.kiem_dau_ra(nop, len(II), ban_nop=True), "Bản nộp sạch: không chuỗi cấm, không cờ, đủ dòng")

II_du_thao = II + [("1", "Việc còn nháp", "1/1", "Vượt mức", "Căn cứ DỰ THẢO — chờ xác nhận", None)]
nop2 = lh.dung_docx(os.path.join(TMP, "nop2.docx"), tt, [(a, b, c, None) for a, b, c, _ in I], II_du_thao,
                    ["Ghi chú thử"], "Quý III năm 2026", noi_bo=False)
kiem(any("DỰ THẢO" in x for x in lh.kiem_dau_ra(nop2, len(II_du_thao), ban_nop=True)),
     "NGƯỢC: còn 'DỰ THẢO' trong bảng → bản nộp bị chặn (bài học 1/10/2026)")

print("== Thể thức: A4, lề 2-2-3-2, Times New Roman 14 kể cả trong bảng ==")
import docx  # noqa: E402
from docx.shared import Cm  # noqa: E402
d = docx.Document(noi_bo)
s = d.sections[0]
kiem(abs(s.page_width - Cm(21)) < 1000 and abs(s.page_height - Cm(29.7)) < 2000, "Khổ A4")
kiem((round(s.top_margin.cm, 1), round(s.bottom_margin.cm, 1), round(s.left_margin.cm, 1),
      round(s.right_margin.cm, 1)) == (2.0, 2.0, 3.0, 2.0), "Lề 2-2-3-2 cm")
co = {r.font.size.pt for t in d.tables for row in t.rows for c in row.cells
      for p in c.paragraphs for r in p.runs if r.font.size}
kiem(co == {14.0}, f"Mọi chữ trong bảng cỡ 14 (đo được: {co})")
ten = {r.font.name for t in d.tables for row in t.rows for c in row.cells
       for p in c.paragraphs for r in p.runs if r.font.name}
kiem(ten == {"Times New Roman"}, f"Phông trong bảng là Times New Roman ({ten})")
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
tc = d.tables[1].rows[1].cells[0]._tc.find(f"{W}tcPr/{W}tcW")
kiem(tc is not None and tc.get(f"{W}type") == "dxa" and int(tc.get(f"{W}w")) > 100,
     "Độ rộng cột ghi bằng TWIPS (dxa), không phải EMU")
kiem(d.tables[1].rows[0]._tr.find(f"{W}trPr/{W}tblHeader") is not None, "Dòng tiêu đề lặp lại mỗi trang")
kiem(d.tables[1].rows[1]._tr.find(f"{W}trPr/{W}cantSplit") is not None, "Dòng không bị tách trang")
kiem(s.different_first_page_header_footer is True, "Số trang ẩn ở trang 1")

print("\n" + ("ĐẠT: 0 ca sai" if not sai else f"KHÔNG ĐẠT: {len(sai)} ca sai\n- " + "\n- ".join(sai)))
sys.exit(1 if sai else 0)
