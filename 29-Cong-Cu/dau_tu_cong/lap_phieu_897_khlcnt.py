# -*- coding: utf-8 -*-
"""Lập Báo cáo rà soát 897 (mẫu 8 phần) cho QĐ phê duyệt KHLCNT giai đoạn CBĐT — bản v5, 07/10/2026."""
import copy, docx
from docx.text.paragraph import Paragraph

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from du_an import ket_qua  # noqa: E402

MAU = os.path.join(os.path.expanduser("~"), ".claude", "plugins", "marketplaces", "local-desktop-app-uploads",
                   "ktc-ra-soat-897", "core", "templates", "Mau_Bao_cao_ra_soat_KTC897_8phan.docx").replace("\\", "/")
OUT = ket_qua("2026-10-07", "Soan-Thao-VB", "Bao-cao-ra-soat-897_QD-KHLCNT-CBDT_20261007.docx")
d = docx.Document(MAU)

def set_text(par, text):
    rs = par.runs
    rs[0].text = text
    for r in rs[1:]:
        r.text = ""

def para_start(prefix):
    for p in d.paragraphs:
        if p.text.strip().startswith(prefix):
            return p
    raise ValueError(prefix)

def add_after(par, text):
    new = copy.deepcopy(par._p)
    par._p.addnext(new)
    np_ = Paragraph(new, par._parent)
    set_text(np_, text)
    return np_

def fill_row(row, vals):
    for c, v in zip(row.cells, vals):
        set_text(c.paragraphs[0], v)

# ---- đầu trang ----
set_text(para_start("[TÊN BỘ HỒ SƠ"), "Quyết định phê duyệt Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư Dự án “Đầu tư, cải tạo các công trình phục vụ người học, nhà giáo và mua sắm bổ sung thiết bị đáp ứng mục tiêu xây dựng Trường Cao đẳng Kon Tum trở thành trường cao đẳng chất lượng cao giai đoạn 2026 - 2030” (bản v9)")
set_text(para_start("Ngày rà soát"), "Ngày rà soát: 07/10/2026  |  Đơn vị soạn thảo: Phòng Tổng hợp - Hành chính và Quản trị  |")
set_text(para_start("Thẩm quyền"), "Thẩm quyền: Hiệu trưởng")

# ---- Phần I ----
t1 = d.tables[0]
thong_tin = {
 "1.": "Hành chính nhà nước (hệ A, Nghị định 30/2020/NĐ-CP; quy ước Trường)",
 "2.": "Quyết định (cá biệt) của Hiệu trưởng, kèm Phụ lục (bảng Kế hoạch lựa chọn nhà thầu)",
 "3.": "Tệp: QD-KHLCNT-giai-doan-CBDT_Du-an-CLC-2026-2030_20261007_v9-sach.docx (bản trình ký) và bản bôi đỏ điều chỉnh v9.docx",
 "4.": "Rà soát chính thức trước khi trình ký, lần 1, trên bản v9 (dựng từ bản v4 do người soạn sửa ngày 07/10/2026)",
 "5.": "Kho KTC-Database 01–02, 04; Exa, Perplexity (đối chiếu VBHN 36/2026 và chuỗi sửa đổi); QĐ 2158, QĐ 2161, Mẫu 02-TT185 do người dùng cung cấp",
 "6.": "Rà soát theo bốn nhóm: thể thức · căn cứ, hiệu lực pháp lý · logic, số liệu · ngôn ngữ",
}
for row in t1.rows[1:]:
    k = row.cells[0].text.strip()[:2]
    if k in thong_tin:
        set_text(row.cells[1].paragraphs[0], thong_tin[k])

# ---- Phần II.A ----
set_text(para_start("II.A."), "II.A. Quyết định và Phụ lục — các phát hiện và xử lý")
t2 = d.tables[1]
F = [
 ("Căn cứ · QĐ 2158 (Điều 1 khoản 5) và QĐ 2161 (Phụ lục) — Thời gian thực hiện dự án",
  "QĐ 2158 ghi dự án thực hiện giai đoạn 2026-2030 (5 năm); Phụ lục QĐ 2161 ghi 2026-2028 (3 năm). Dự án là nhóm C nên thời gian bố trí vốn thực hiện dự án không quá 03 năm (không tính chuẩn bị đầu tư và quyết toán); gia hạn tối đa 01 năm. Điểm a khoản 2 Điều 57 chỉ nói về bản thân Chương trình mục tiêu quốc gia, không miễn mốc 03 năm cho dự án nhóm C. (Nhận định ở bản v4 của người soạn rằng dự án được hưởng thời hạn của Chương trình là chưa đúng, đã bỏ.)",
  "Người có thẩm quyền chốt lại thời gian thực hiện dự án; nếu theo nhóm C thì khoản 5 Điều 1 QĐ này phải sửa cho khớp (đồng thời sửa QĐ 2158). Thời gian thực hiện dự án do cấp có thẩm quyền phê duyệt trong quyết định đầu tư nhưng không vượt thời gian bố trí vốn. Ở v9, gói số 2 ghi theo thời gian thực hiện dự án được phê duyệt, không nêu năm kết thúc.",
  "Điều 57 khoản 1, 2 (điểm a, d), 3 Luật Đầu tư công (VBHN 03); Điều 47 NĐ 85/2025; Perplexity", "Mức 2 · CÒN MỞ"),
 ("Điều 1, Phụ lục — Kế hoạch vốn và điều kiện chỉ định thầu rút gọn",
  "Kế hoạch vốn 2026 của dự án theo QĐ 2161 chỉ 260 triệu đồng (200 NSTW + 60 NSĐP), trong khi giá hai gói thầu 1.519.778.268 đồng.",
  "Phòng TC-KT xác nhận phần vốn còn lại đã có kế hoạch bố trí trước khi tổ chức chỉ định thầu; đã thêm Điều 2 khoản 3 (ký, thanh toán trong phạm vi vốn được giao).",
  "Điều 80 khoản 2 và điểm b khoản 2 Điều 79 NĐ 214/2025 (VBHN 36/2026)", "Mức 2 · CÒN MỞ"),
 ("Phụ lục, gói thầu số 2 — Phạm vi và thời gian thực hiện hợp đồng",
  "Gói tư vấn quản lý dự án thực hiện từ chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án (người dùng chỉ đạo 07/10/2026); giá 667.433.022 đồng tính theo định mức chi phí quản lý dự án của cả dự án, nên khớp phạm vi này. Thời gian dài hơn 01 năm.",
  "ĐÃ SỬA v8: tóm tắt công việc và thời gian “từ ngày hợp đồng có hiệu lực đến khi quyết toán hoàn thành dự án ”; Ghi chú nêu giá gói xác định trên toàn bộ thời gian. Không nêu năm kết thúc; phụ thuộc điểm thời gian dự án.",
  "Khoản 2 Điều 37, khoản 7 Điều 39 Luật Đấu thầu (VBHN 74); Điều 46 NĐ 217/2026 (thuê tư vấn QLDA thực hiện một phần hoặc toàn bộ nội dung quản lý dự án)", "Mức 3 · đã sửa"),
 ("Phụ lục, gói thầu số 1 — Gộp khảo sát và lập BCKTKT",
  "Gộp hai khoản mục của QĐ 2158 (93.995.981 + 758.349.265 = 852.345.246 đồng; 30 + 90 = 120 ngày). Không thấy quy định cấm gộp; quy định cấm là chia nhỏ để chỉ định thầu; giá gói vẫn dưới 03 tỷ đồng.",
  "ĐÃ XỬ LÝ: thêm ghi chú truy vết về hai khoản mục tại Phụ lục QĐ 2158. Nên nêu lý do gộp (một nhà thầu, đồng bộ số liệu khảo sát và thiết kế) trong tờ trình.",
  "Điều 37 khoản 3, 4 và Điều 16 Luật Đấu thầu; khoản 4 Điều 78 NĐ 214/2025", "Mức 4 · đã xử lý"),
 ("Căn cứ — NĐ 214/2025 và chuỗi sửa đổi",
  "Bản trước ghi sai chuỗi sửa đổi (NĐ 165/2026 và 349/2026); VBHN 36/2026 liệt kê NĐ 165/2026, 170/2026, 349/2026.",
  "ĐÃ SỬA: ghi “(hợp nhất tại Văn bản hợp nhất số 36/2026/VBHN-NĐ-BTC ngày 23/9/2026 của Bộ Tài chính)”.",
  "VBHN 36/2026/VBHN-NĐ-BTC (kho 01-04, tệp BanCoChu 03/10/2026); Perplexity; Điều 4 Pháp lệnh Hợp nhất", "Mức 3 · đã sửa"),
 ("Căn cứ — Luật Đấu thầu, Luật Đầu tư công (văn bản hợp nhất)",
  "Chưa viện dẫn văn bản hợp nhất đã có trong kho (VBHN 74 ký xác thực 25/3/2026; VBHN 03 ký xác thực 05/2/2026).",
  "ĐÃ SỬA theo chỉ đạo người phụ trách 07/10/2026: viện dẫn văn bản hợp nhất — Luật Đấu thầu (hợp nhất tại VBHN 74/VBHN-VPQH ngày 25/3/2026), Luật Đầu tư công (hợp nhất tại VBHN 03/VBHN-VPQH ngày 05/2/2026); không ghi số hiệu Luật; không liệt kê luật sửa đổi.",
  "VBHN 74, VBHN 03 (kho 01); 17-Quy-Tac-Vien-Dan.md", "Mức 3 · đã sửa"),
 ("Phụ lục — Hình thức, phương thức lựa chọn nhà thầu",
  "Cột hình thức ghi “Chỉ định thầu”; cột phương thức ghi “Quy trình rút gọn” (là quy trình, không phải phương thức). Bản v6 từng ghi “Một giai đoạn một túi hồ sơ” là sai: điểm c khoản 1 Điều 30 Luật Đấu thầu áp dụng cho chỉ định thầu (quy trình thông thường có hồ sơ yêu cầu), không áp cho quy trình rút gọn.",
  "ĐÃ SỬA: hình thức “Chỉ định thầu rút gọn”; cột phương thức để trống (chỉ định thầu rút gọn không quy định phương thức); khoản 8 Điều 1 nêu rõ.",
  "Điều 80 NĐ 214/2025 (rút gọn: dự thảo hợp đồng, hoàn thiện, phê duyệt, ký — không có hồ sơ yêu cầu); Điều 30, khoản 4 Điều 39 Luật Đấu thầu; Perplexity; hướng dẫn trong kho (QĐ 1589/QĐ-BYT) — chỉ tham khảo, không phải căn cứ pháp lý", "Mức 3 · đã sửa"),
 ("Căn cứ — NĐ 85/2025, NĐ 206/2026, TT 36/2026; thiếu NĐ 358/2025, QĐ 2161",
  "Ba văn bản về chi phí không phục vụ việc phê duyệt KHLCNT; NĐ 85/2025 có thêm NĐ 224/2026 sửa đổi chưa xác minh đủ; thiếu căn cứ kế hoạch vốn.",
  "ĐÃ SỬA: bỏ ba văn bản; thêm NĐ 358/2025 (quản lý CTMTQG) và QĐ 2161/QĐ-CĐKT (phân bổ vốn). Giữ NĐ 217/2026 cho gói lập BCKTKT.",
  "Điều 38 khoản 1 Luật Đấu thầu; QĐ 2161; kho 01-04", "Mức 3 · đã sửa"),
 ("Điều 1 — Cơ sở thẩm quyền và hình thức chỉ định thầu",
  "Chưa nêu căn cứ thẩm quyền Hiệu trưởng và hạn mức chỉ định thầu.",
  "ĐÃ SỬA: thêm khoản 8 (điểm a khoản 1 Điều 38, khoản 2 Điều 40 Luật Đấu thầu; khoản 4 Điều 78, Điều 80 NĐ 214/2025). Đã đọc: tư vấn thuộc dự án ≤ 03 tỷ đồng.",
  "VBHN 74 Điều 38, 40; VBHN 36/2026 Điều 78, 80", "Mức 3 · đã sửa"),
 ("Điều 2 — Giao việc",
  "Thiếu giao đăng tải Kế hoạch lên Hệ thống mạng đấu thầu quốc gia; thiếu ràng buộc vốn khi ký hợp đồng.",
  "ĐÃ SỬA: thêm Điều 2 khoản 3, 4. (Nên đối chiếu số điều quy định đăng tải trước khi viện dẫn cụ thể.)",
  "Luật Đấu thầu (VBHN 74); QĐ 2158 Điều 2 khoản 4", "Mức 3 · đã sửa"),
 ("Thể thức — viết hoa sau dấu hai chấm; bảng Phụ lục",
  "“giai đoạn I: từ năm” viết thường ở 03 chỗ; bảng Phụ lục rộng 26,5 cm vượt vùng chữ ngang 25,7 cm; chưa lặp hàng tiêu đề.",
  "ĐÃ SỬA: viết hoa “Từ”; co lưới bảng về 14.572 twip; bật lặp hai hàng tiêu đề.",
  "Checklist 08 (viết hoa sau dấu hai chấm); đo bằng ktc897_properties.py, python-docx", "Mức 3 · đã sửa"),
 ("Phụ lục — cột “Phương thức”, “Tên chủ đầu tư”; Điều 1 “Cơ quan tổ chức chuẩn bị dự án”",
  "Ghi “Quy trình rút gọn” ở cột phương thức; dùng “chủ đầu tư” ở Phụ lục nhưng “cơ quan tổ chức chuẩn bị dự án” ở Điều 1.",
  "Giữ theo mẫu 03 Quyết định KHLCNT đã ban hành của Trường (2021, 2024, 2026); Mẫu 02-TT185 ghi Trường là chủ đầu tư. Người soạn xem xét nếu muốn thống nhất thuật ngữ.",
  "Mẫu QĐ KHLCNT của Trường; Mẫu số 02-MSNS-BTC (02/10/2026)", "Mức 4 · giữ nguyên"),
 ("Kho KTC-Database — văn bản chưa có bản",
  "QĐ 1976, QĐ 2158, QĐ 2161/QĐ-CĐKT chưa có trong kho 01–02; ngày VBHN 36 giữa bản scan (23/9) và bản chữ (nạp 03-04/10) cần xác nhận.",
  "Nạp các QĐ nội bộ vào kho để đối chiếu; người có thẩm quyền xác nhận ngày VBHN 36 trên cổng chính thức.",
  "Kết quả quét ktc897-hieu-luc", "Mức 4"),
]
tpl = t2.rows[1]._tr
for r in list(t2.rows)[1:]:
    t2._tbl.remove(r._tr)
for i, f in enumerate(F, 1):
    tr = copy.deepcopy(tpl)
    t2._tbl.append(tr)
    row = t2.rows[-1]
    fill_row(row, (str(i),) + f)

# ---- Phần III ----
p3 = para_start("[Liệt kê theo nhóm")
set_text(p3, "Thể thức: A4, lề 2,0-2,0-3,0-2,0 cm; Times New Roman; số/ký hiệu cỡ 13; địa danh, ngày tháng cỡ 14 nghiêng; ba đường kẻ (dưới tên Trường, dưới tiêu ngữ, dưới trích yếu); căn cứ nghiêng cỡ 14; khối nơi nhận – chữ ký không tách trang; Phụ lục là section ngang riêng, số trang tính riêng, không có dòng “Kèm theo” (đo bằng ktc897_properties.py, python-docx, kiem_the_thuc.py: 0 gợi ý bản sạch).")
q = add_after(p3, "Viện dẫn: kiem_vien_dan.py 0 gợi ý (VD01–VD12); QĐ 1976 là căn cứ đầu tiên; Luật không ghi số hiệu; số hiệu, ngày, tên của VBHN 74, VBHN 03, VBHN 36/2026, NQ 56, QĐ 805, Luật Xây dựng 135/2025, NĐ 217/2026, NĐ 358/2025 khớp kho 01–04, 01–06.")
q = add_after(q, "Số liệu: 93.995.981 + 758.349.265 = 852.345.246; 852.345.246 + 667.433.022 = 1.519.778.268 đồng, khớp Điều 1 khoản 6, 7, Điều 2, Phụ lục (dòng Tổng cộng), Ghi chú và QĐ 2158; sơ bộ TMĐT 24.894.000.000 đồng, nhóm C khớp QĐ 2158.")
add_after(q, "Thẩm quyền: khoản 2 Điều 40 Luật Đấu thầu (gói thầu thực hiện trước khi phê duyệt dự án, chưa xác định chủ đầu tư) — Hiệu trưởng là người đứng đầu đơn vị được giao nhiệm vụ chuẩn bị dự án.")

# ---- Phần IV ----
tb1, tb2 = d.tables[2], d.tables[3]
nhom = [("Pháp lý, căn cứ, vốn, thời gian dự án", "7", "0"), ("Logic, số liệu, nội dung Phụ lục", "2", "0"), ("Thể thức", "1", "0"), ("Ngôn ngữ, thuật ngữ", "2", "0")]
base = tb1.rows[-1]._tr
for n in nhom:
    tr = copy.deepcopy(base); tb1._tbl.append(tr); fill_row(tb1.rows[-1], n)
tb1._tbl.remove(base)
muc = [("Mức 1", "0", "0%"), ("Mức 2", "2", "17%"), ("Mức 3", "7", "58%"), ("Mức 4", "3", "25%")]
base2 = tb2.rows[-1]._tr
for n in muc:
    tr = copy.deepcopy(base2); tb2._tbl.append(tr); fill_row(tb2.rows[-1], n)
tb2._tbl.remove(base2)

# ---- Phần VI, VII ----
set_text(para_start("[1. Mức độ tuân thủ"), "1. Mức độ tuân thủ pháp luật: Đạt có điều kiện — không còn lỗi Mức 1; căn cứ pháp lý đã đối chiếu kho 01–04 và Internet; còn 02 điểm Mức 2 cần người có thẩm quyền xác nhận.")
set_text(para_start("[2. Mức độ sẵn sàng"), "2. Mức độ sẵn sàng phát hành: Cần chỉnh sửa trước khi trình ký — chốt hai điểm Mức 2 (thời gian dự án 2026-2030 hay 2026-2028, ảnh hưởng mốc kết thúc gói số 2; kế hoạch vốn so với giá gói thầu).")
p7 = para_start("[Ưu điểm")
set_text(p7, "Ưu điểm: số liệu thống nhất giữa Điều 1, Phụ lục và QĐ 2158; căn cứ đã chuẩn hóa theo văn bản hợp nhất; hình thức chỉ định thầu có căn cứ hạn mức rõ.")
q = add_after(p7, "Tồn tại chính theo thứ tự xử lý: (1) thời gian thực hiện dự án 2026-2030 (QĐ 2158) lệch 2026-2028 (QĐ 2161); (2) vốn 2026 chỉ 260 triệu đồng so với giá gói thầu 1,52 tỷ đồng — điều kiện có kế hoạch bố trí vốn của chỉ định thầu rút gọn; (3) Khoản mục tư vấn quản lý dự án 667 triệu đồng trong dự toán chuẩn bị đầu tư (QĐ 2158) là chi phí cả dự án — cần xác nhận nguồn chi theo từng giai đoạn.")
q = add_after(q, "Rủi ro nếu không sửa: Quyết định bị hiểu là chưa đủ điều kiện chỉ định thầu, hoặc mâu thuẫn với QĐ 2161 khi kiểm tra, thanh toán.")
add_after(q, "Kiến nghị chung: người có thẩm quyền chốt các điểm trên; nạp QĐ 1976, 2158, 2161 vào kho; sau khi chốt, rà soát lại nhanh và ký số.")

# ---- Phần VIII: bỏ ----
p8 = para_start("PHẦN VIII")
for p in list(d.paragraphs):
    if p.text.strip().startswith("Các nhận định dưới đây") or p.text.strip().startswith("[Chỉ in phần này"):
        p._p.getparent().remove(p._p)
p8._p.getparent().remove(p8._p)

# ---- Kiểm tra chất lượng cuối, trách nhiệm ----
set_text(para_start("[Tự kiểm tra"), "Đủ bốn nhóm tiêu chí; đã đối chiếu kho 01–04 và Internet; phân biệt lỗi, đạt, tư vấn; chưa rà soát bằng quy trình người thứ hai. Phiếu này không thay thế quyết định của người có thẩm quyền.")
t5 = d.tables[4]
fill_row(t5.rows[0], ("Nguồn dữ liệu đã dùng", "KTC-Database: VBHN 74, VBHN 03, VBHN 36/2026 (BanCoChu), NĐ 358/2025, NQ 56, QĐ 805, Luật Xây dựng 135/2025; Exa, Perplexity; QĐ 2158 (đã ký), QĐ 2161, Mẫu 02-TT185, 03 mẫu QĐ KHLCNT của Trường; bản v4 (người dùng sửa 07/10/2026)"))
fill_row(t5.rows[1], ("Người kiểm tra", "(chưa xác định — người có thẩm quyền của Trường điền)"))
fill_row(t5.rows[2], ("Trạng thái phê duyệt", "Bản nháp — chưa phê duyệt"))

d.save(OUT)
print("saved", OUT)
