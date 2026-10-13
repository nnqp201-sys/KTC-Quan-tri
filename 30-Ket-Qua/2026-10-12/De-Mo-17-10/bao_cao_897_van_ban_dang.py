# -*- coding: utf-8 -*-
"""Báo cáo rà soát chính thức KTC-897 v2.25 — hệ quy chiếu B (văn bản Đảng) — dự thảo Chương trình công tác tháng 10/2026
của Ban Thường vụ Đảng ủy UBND phường XYZ (văn bản ẩn danh, đã hạ cấp từ một dự thảo thật). Rà soát ngày 12/10/2026."""
import os, sys
sys.path.insert(0, r'H:\My Drive\KTC-Ra-Soat-897-v2-Cai-tien\tools')
import build_ktc897_report as B
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
RA = os.path.join(D, 'Ket-qua-chay-truoc', 'BaoCao_RaSoat-897-v2.25_Chuong-trinh-cong-tac-thang-10-2026_van-ban-Dang_an-danh.docx')
ver, ngay_skill = B._read_skill_version()
b = B.ReportBuilder(ver, ngay_skill)
B.trang_dau(b, 'Dự thảo Chương trình công tác trọng tâm tháng 10 năm 2026 của Ban Thường vụ Đảng ủy Ủy ban nhân dân phường XYZ (văn bản đã ẩn danh phục vụ trình diễn)',
            'Văn phòng Đảng ủy (suy từ mục Nơi nhận, chưa xác nhận)', 'Ban Thường vụ Đảng ủy UBND phường XYZ; T/M Ban Thường vụ, Phó Bí thư', '12/10/2026')

b.h1('PHẦN I. THÔNG TIN CHUNG')
b.bang_2cot(('MỤC', 'NỘI DUNG'), [
 ('Hệ quy chiếu', 'Hệ B - văn bản của Đảng: Hướng dẫn số 05-HD/VPTW ngày 27/5/2026 của Văn phòng Trung ương Đảng (thể thức, kỹ thuật trình bày); Quy định số 399-QĐ/TW ngày 09/01/2026 của Ban Bí thư (thể loại, thẩm quyền); Skill 29 và Phụ lục 2, 3. Căn cứ chọn: Tiêu đề “ĐẢNG CỘNG SẢN VIỆT NAM”, ký hiệu CTr/ĐU, đề ký T/M. KHÔNG áp Nghị định số 30/2020/NĐ-CP'),
 ('Loại văn bản, thẩm quyền', 'Chương trình (CTr). Ban thường vụ đảng ủy được ban hành chương trình theo Quy định số 399-QĐ/TW'),
 ('Quy ước riêng của Trường', 'KHÔNG áp dụng (Checklist 08, Thông báo số 597/TB-CĐKT), vì đây là văn bản của cơ quan khác'),
 ('Đo thể thức', 'Đo trực tiếp trên tệp .docx (lề, cỡ chữ từng thành phần, thụt đầu dòng, cách dòng, cách đoạn, số trang, kiểu chữ) và xem bản in thử 04 trang'),
 ('Nguồn đã đọc', 'Kho 01: Quy định số 399-QĐ/TW, Hướng dẫn số 05-HD/VPTW, Quy định số 208-QĐ/TW, Hướng dẫn số 02-HD/TW. Kho 02: Nghị quyết số 26-NQ/TW ngày 22/8/2026, Nghị quyết số 27-NQ/TW ngày 28/8/2026 (đã mở bản gốc, khớp số, ngày, cơ quan ban hành, trích yếu). Tra cứu Internet ngày 12/10/2026 (báo chí chính thống đăng lại văn bản): Kết luận số 76-KL/TW ngày 28/7/2026, Kết luận số 226-KL/TW ngày 11/12/2025 - khớp số, ngày, cơ quan ban hành, trích yếu; chưa đối chiếu toàn văn'),
 ('Chưa xác minh', 'Văn bản của địa phương được viện dẫn (05-CTr/ĐU, 09-CTr/TU, 25-CTr/ĐU, 11-CTr/ĐU, 1286-KL/ĐU, 10-QC/ĐU, 87-KH/TU): Không có trong kho, số ký hiệu đã được thay khi ẩn danh nên không tra cứu được - chỉ đánh giá tính nhất quán nội tại'),
 ('Giới hạn', 'Văn bản đã ẩn danh và đổi cấp ban hành (tên cơ quan, cơ quan phối hợp là giả định) nên không đánh giá sự phù hợp của tên các cơ quan tham mưu với cơ cấu tổ chức thực tế, không thẩm định chuyên môn nội dung. Dự thảo chưa có số, ngày nên không nêu thiếu số, ngày là lỗi'),
 ('Kết quả', '0 vấn đề Mức 1; 07 Mức 2; 13 Mức 3; 05 Mức 4. Cần chỉnh sửa trước khi trình ký'),
])

b.h1('PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT')
H = ['TT', 'NỘI DUNG', 'NHẬN XÉT', 'KIẾN NGHỊ', 'CĂN CỨ', 'MỨC']
R = [
 ['1', '[Điều khoản bắt buộc] Căn cứ thứ hai: “Chương trình số 09-CTr/TU ngày 18/12/2025”', 'Chương trình của Đảng ủy, Ban Thường vụ Đảng ủy UBND phường XYZ nhưng mang ký hiệu “/TU” (ký hiệu của Tỉnh ủy); các văn bản khác của cùng cơ quan mang ký hiệu “/ĐU”', 'Đối chiếu bản gốc; sửa ký hiệu cho đúng cơ quan ban hành', 'Hướng dẫn số 05-HD/VPTW (số và ký hiệu; viện dẫn văn bản)', 'Mức 2'],
 ['2', '[Nội dung] Mục I.1: “Kết luận số 1286-KL/ĐU ngày 02/10/2026”', 'Số văn bản của Đảng ghi liên tục theo từng tên loại trong một nhiệm kỳ; số 1286 sau chưa đầy 01 năm của nhiệm kỳ là bất thường so với các số khác của cùng cơ quan (05, 11, 25-CTr/ĐU; 10-QC/ĐU)', 'Xác minh số, ngày với bộ phận văn thư trước khi trình ký', 'Hướng dẫn số 05-HD/VPTW (số văn bản)', 'Mức 2'],
 ['3', '[Điều khoản bắt buộc] Tiêu đề Mục III và Mục IV.1: “Điều 4, Quy chế số 10-QC/ĐU”', 'Viện dẫn lần đầu thiếu ngày ban hành, cơ quan ban hành, trích yếu; Quy chế là cơ sở phân định thẩm quyền của cả Mục III nhưng không có trong phần căn cứ', 'Ghi đầy đủ ở lần viện dẫn đầu; đưa vào phần căn cứ', 'Hướng dẫn số 05-HD/VPTW (viện dẫn lần đầu ghi đủ tên loại, số, ký hiệu, ngày, cơ quan ban hành, trích yếu)', 'Mức 2'],
 ['4', '[Nội dung] Mục I.1: Câu dài, nhiều chủ thể', 'Một câu nối Chương trình hành động số 11-CTr/ĐU, 03 nghị quyết đại hội và Kết luận số 1286-KL/ĐU bằng từ “và”; không rõ “thực hiện” gắn với văn bản nào', 'Tách thành hai ý: (1) Triển khai Chương trình hành động số 11-CTr/ĐU; (2) thực hiện Kết luận số 1286-KL/ĐU', 'Checklist 02, 04', 'Mức 2'],
 ['5', '[Nội dung] Mục II: 05 nội dung trình Ban Thường vụ Đảng ủy phường', 'Mục III có dòng “Thời gian trình” cho từng nội dung, Mục II không có; thời hạn là yếu tố điều hành chính của một chương trình công tác tháng; Mục I.3 chỉ ghi chung “trong tháng 10/2026”', 'Bổ sung “Thời gian trình” cho từng nội dung của Mục II', 'Checklist 02 (đủ thời hạn, trách nhiệm)', 'Mức 2'],
 ['6', '[Thể thức] Phần căn cứ', 'Căn cứ cuối cùng kết thúc bằng dấu chấm phẩy; hai căn cứ (Chương trình năm và Chương trình quý IV) gộp trong một đoạn', 'Căn cứ cuối kết thúc bằng dấu chấm; mỗi căn cứ một đoạn có gạch ngang đầu dòng', 'Hướng dẫn số 05-HD/VPTW (căn cứ ban hành)', 'Mức 2'],
 ['7', '[Nội dung] Mục III.2, III.3, IV: “Ban Thường vụ Đảng ủy”', 'Văn bản có hai cấp ủy: Đảng ủy phường (cấp nhận trình) và Đảng ủy UBND phường XYZ (cấp ban hành). Cụm “Ban Thường vụ Đảng ủy” không kèm tên dùng xen kẽ với hai tên đầy đủ, ví dụ “Trình Ban Thường vụ Đảng ủy xem xét, cho ý kiến trước thời hạn báo cáo Ban Thường vụ Đảng ủy phường” - người đọc phải suy đoán cấp nào', 'Lần đầu ghi tên đầy đủ kèm cách gọi tắt (ví dụ: Sau đây gọi là Ban Thường vụ Đảng ủy UBND phường), dùng thống nhất đến hết văn bản', 'Checklist 02, 04 (thống nhất tên gọi)', 'Mức 2'],
 ['8', '[Chất lượng soạn thảo] “Ban Xây dựng Đảng Đảng ủy” (II.1, II.4)', 'Lặp từ “Đảng”; Mục III.1 lại viết “Ban Xây dựng Đảng ủy” - tên cơ quan không thống nhất', 'Thống nhất theo tên chính thức', 'Checklist 04', 'Mức 3'],
 ['9', '[Chất lượng soạn thảo] Mục II.3, II.5', 'II.5 dùng nhãn “Cơ quan tham mưu” (các mục khác: “Cơ quan chủ trì tham mưu”), dòng “UBND phường” thiếu dấu chấm; tên nội dung II.3 thiếu dấu chấm cuối câu (II.1, II.2, II.4 có)', 'Thống nhất nhãn và dấu câu', 'Checklist 04', 'Mức 3'],
 ['10', '[Nội dung] Mục III.2: “các nội dung tại Mục II”', 'Mục II gồm cả nội dung 5 (“nếu có”), trùng với Mục III.3', 'Ghi “các nội dung từ 1 đến 4 tại Mục II” hoặc gộp II.5 với III.3', 'Checklist 02', 'Mức 3'],
 ['11', '[Chất lượng soạn thảo] Mục IV.3: “Ban Thường vụ Đảng ủy ủy quyền Thường trực Đảng ủy”', 'Hai chữ “ủy” liền nhau, khó đọc', 'Diễn đạt lại, ví dụ “giao Thường trực Đảng ủy”', 'Checklist 04', 'Mức 3'],
 ['12', '[Điều khoản bắt buộc] Viết tắt “UBND”, “BCH”', '“UBND” dùng ngay từ căn cứ đầu, “BCH” ở Nơi nhận, không có giải thích ở lần đầu', 'Ghi đầy đủ kèm chữ viết tắt ở lần đầu: “Ủy ban nhân dân (UBND)”', 'Hướng dẫn số 05-HD/VPTW (từ viết tắt)', 'Mức 3'],
 ['13', '[Thể thức] Tên loại “CHƯƠNG TRÌNH”', 'Đo được cỡ 14; quy định cỡ 15 - 16', 'Đặt cỡ 15 hoặc 16', 'Phụ lục 2 Hướng dẫn số 05-HD/VPTW, thành phần 5a', 'Mức 3'],
 ['14', '[Thể thức] Cách dòng', 'Toàn bộ 56 đoạn không đặt cách dòng chính xác (đang là cách dòng đơn); quy định 18 - 22 pt (Exactly)', 'Đặt cách dòng chính xác 18 - 22 pt', 'Hướng dẫn số 05-HD/VPTW, Phần II mục 6.2', 'Mức 3'],
 ['15', '[Thể thức] Thụt đầu dòng', 'Đo được 03 mức: 12,5 mm (14 đoạn); 12,7 mm (36 đoạn); 10,39 mm (02 đoạn); quy định khoảng 10 mm', 'Thống nhất khoảng 10 mm', 'Hướng dẫn số 05-HD/VPTW, Phần II mục 6.2', 'Mức 3'],
 ['16', '[Thể thức] Số trang', 'Số trang không đặt cỡ chữ riêng (kế thừa cỡ 15 của kiểu mặc định; quy định cỡ 14); cách mép trên 12,7 mm (quy định 10 mm)', 'Đặt cỡ 14, cách mép trên 10 mm', 'Phụ lục 2 Hướng dẫn số 05-HD/VPTW, thành phần 15; Phần II mục IV', 'Mức 3'],
 ['17', '[Thể thức] Nơi nhận: “- Lưu Văn phòng Đảng ủy.Th”', 'Có ký tự “Th” cỡ 12 dính sau dấu chấm của dòng Lưu, có thể là ký hiệu người soạn thảo gõ nhầm chỗ; ký hiệu người soạn thảo có vị trí riêng, cỡ 11', 'Xóa hoặc chuyển về đúng vị trí, cỡ 11', 'Phụ lục 2 Hướng dẫn số 05-HD/VPTW, thành phần 13', 'Mức 3'],
 ['18', '[Thể thức] Nơi nhận: “- Các cơ quan chuyên trách tham mưu, / giúp việc Đảng ủy;”', 'Một nơi nhận bị ngắt thành hai đoạn, đoạn sau không có gạch đầu dòng', 'Gộp thành một đoạn', 'Hướng dẫn số 05-HD/VPTW (nơi nhận)', 'Mức 3'],
 ['19', '[Thể thức] “T/M BAN THƯỜNG VỤ” dùng kiểu Heading 1', 'Kiểu Heading 1 của tệp khai phông VNI-Times (không phải phông Unicode), chữ hiện đúng nhờ định dạng trực tiếp; dễ lỗi phông khi sao chép, đổi kiểu và có thể lọt vào mục lục tự động', 'Dùng kiểu thường, phông Times New Roman', 'Hướng dẫn số 05-HD/VPTW, Phần II mục IV.1 (phông chữ)', 'Mức 3'],
 ['20', '[Chất lượng soạn thảo] Mục IV.3: Ủy quyền cho Thường trực', 'Nội dung ủy quyền “điều chỉnh thời gian, bổ sung các nhiệm vụ phát sinh” chưa có giới hạn', 'Ghi rõ giới hạn (không điều chỉnh nội dung thuộc thẩm quyền quyết định của tập thể)', 'Quy định số 399-QĐ/TW; Checklist 02', 'Mức 3'],
 ['21', '[Điều khoản bắt buộc] Tên gọi loại hình tổ chức đảng', 'Quy định số 208-QĐ/TW ngày 26/7/2026 thí điểm thống nhất tên gọi tổ chức đảng ở cấp cơ sở; quy định hiện hành tiếp tục áp dụng đến khi có văn bản thay thế', 'Không cần sửa; theo dõi hướng dẫn chính thức', 'Skill 29, Phụ lục 3', 'Mức 4'],
 ['22', '[Nội dung] Mục IV.3: Theo dõi, tổng hợp', 'Văn phòng Đảng ủy chỉ “theo dõi, đôn đốc, tổng hợp”, chưa có kỳ báo cáo Ban Thường vụ', 'Bổ sung kỳ báo cáo', 'Checklist 02', 'Mức 4'],
 ['23', '[Chất lượng soạn thảo] Cách viện dẫn trong phần căn cứ', 'Số, ký hiệu, ngày của 03 chương trình đặt trong ngoặc đơn, in nghiêng sau tên văn bản, khác cách viện dẫn trực tiếp ở Mục I (“Chương trình hành động số 11-CTr/ĐU ngày 14/4/2026 của…”)', 'Nên viện dẫn trực tiếp: Tên loại, số, ký hiệu, ngày, cơ quan ban hành, trích yếu', 'Checklist 03', 'Mức 4'],
 ['24', '[Nội dung] Mục II.5 và Mục III.3', 'Hai mục cùng nói về vấn đề kinh tế - xã hội do UBND phường trình', 'Gộp hoặc phân biệt phạm vi', 'Checklist 02', 'Mức 4'],
 ['25', '[Thể thức] Thuộc tính tệp', 'Thuộc tính tệp ghi tiêu đề “ĐẢNG ỦY PHƯỜNG XYZ” (khác cơ quan ban hành) và tác giả là tên tài khoản máy tính', 'Làm sạch thuộc tính tệp trước khi phát hành văn bản điện tử', 'Checklist 06', 'Mức 4'],
]
b.table(H, R, muc_col=5)

b.h1('PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ')
for t in [
 'Thẩm quyền, đề ký: Ban thường vụ đảng ủy được ban hành chương trình; đề ký “T/M BAN THƯỜNG VỤ”, chức vụ in hoa không đậm, họ tên in thường đậm, không ghi học hàm, học vị.',
 'Phần đầu: Tiêu đề “ĐẢNG CỘNG SẢN VIỆT NAM” cỡ 15 đậm, có đường kẻ; tên cơ quan cấp trên cỡ 14, tên cơ quan ban hành cỡ 14 đậm, có dấu sao; số và ký hiệu đúng dạng “Số …-CTr/ĐU”; địa danh, ngày tháng cỡ 14 nghiêng.',
 'Tên loại, trích yếu: Trích yếu cỡ 14 đậm; có 05 dấu gạch nối phía dưới; phần căn cứ có gạch ngang đầu dòng.',
 'Trình bày: Khổ A4; lề trên 20 - dưới 20 - trái 30 - phải 15 mm đúng con số cố định; nội dung cỡ 14, phông Times New Roman, dàn đều hai lề; cách đoạn 6 pt; trang đầu không hiện số trang; nội dung kết thúc bằng dấu chấm.',
 'Nơi nhận: Từ “Nơi nhận” cỡ 14 có gạch chân; tên cơ quan nhận cỡ 12.',
 'Viện dẫn văn bản của Trung ương: Nghị quyết số 26-NQ/TW, 27-NQ/TW khớp bản gốc trong kho; Kết luận số 76-KL/TW, Kết luận số 226-KL/TW khớp số, ngày, cơ quan ban hành, trích yếu theo nguồn báo chí chính thống.',
 'Bố cục 04 phần (nhiệm vụ trọng tâm; nội dung trình cấp trên; nội dung trình theo quy chế; tổ chức thực hiện) hợp lý; mỗi nội dung trình có phân công chỉ đạo, cơ quan chủ trì, cơ quan phối hợp.',
]:
    b.para('- ' + t)

b.h1('PHẦN IV. BẢNG TỔNG HỢP')
b.table(['NHÓM', 'MỨC 1', 'MỨC 2', 'MỨC 3', 'MỨC 4', 'CỘNG'], [
 ['Thể thức', '0', '1', '7', '1', '9'],
 ['Nội dung', '0', '4', '1', '2', '7'],
 ['Điều khoản bắt buộc', '0', '2', '1', '1', '4'],
 ['Chất lượng soạn thảo', '0', '0', '4', '1', '5'],
 ['Cộng', '0', '7', '13', '5', '25'],
])

b.h1('PHẦN V. THẨM ĐỊNH CHUYÊN MÔN (NẾU CÓ)')
b.para('Không thẩm định chuyên môn: Văn bản đã ẩn danh, đổi cấp ban hành để trình diễn nên nội dung công tác không phản ánh một cơ quan cụ thể.')

b.h1('PHẦN VI. ĐÁNH GIÁ TỔNG THỂ')
b.para('Dự thảo đúng hệ thể thức văn bản của Đảng ở các thành phần chính (tiêu đề, tên cơ quan, số ký hiệu, đề ký, lề trang, nơi nhận). Không có vấn đề Mức 1. Các vấn đề Mức 2 tập trung ở viện dẫn văn bản (ký hiệu, số, viện dẫn thiếu thành phần), cách gọi tên hai cấp ủy và việc thiếu thời gian trình; các vấn đề Mức 3 chủ yếu là thông số trình bày đo được trên tệp. Mức tuân thủ: Đạt có điều kiện.')

b.h1('PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ')
b.para('Kết luận: Không có vấn đề Mức 1; còn 07 vấn đề Mức 2 - cần chỉnh sửa trước khi trình ký.')
b.para('Thứ tự xử lý: (1) Xác minh ký hiệu, số, ngày các văn bản viện dẫn (vấn đề số 1, 2, 3); (2) thống nhất cách gọi tên hai cấp ủy, bổ sung thời gian trình ở Mục II, tách câu Mục I.1, sửa dấu câu phần căn cứ (số 4, 5, 6, 7); (3) thống nhất tên cơ quan, nhãn, từ viết tắt (số 8 đến 12, 20); (4) chỉnh thông số trình bày: Tên loại cỡ 15 - 16, cách dòng, thụt đầu dòng, số trang, nơi nhận, kiểu chữ (số 13 đến 19); (5) các góp ý Mức 4 do cơ quan ban hành quyết định.')

b.h1('KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG')
b.para('Đã kiểm: Số phát hiện ở Phần II khớp bảng Phần IV (25 = 07 + 13 + 05); mọi phát hiện thể thức đều có số đo trên tệp; không áp Nghị định số 30/2020/NĐ-CP và quy ước riêng của Trường; không nêu thiếu số, ngày của dự thảo là lỗi; ghi rõ các viện dẫn chưa xác minh; không kết luận về loại hình tổ chức đảng của cơ quan ban hành.')
b.thong_tin_trach_nhiem(
 'Tệp dự thảo .docx (đọc nội dung, đo định dạng); kho KTC-Database 01, 02 (Quy định số 399-QĐ/TW, Hướng dẫn số 05-HD/VPTW, Quy định số 208-QĐ/TW, Hướng dẫn số 02-HD/TW, Nghị quyết số 26-NQ/TW, 27-NQ/TW); báo chí chính thống tra cứu ngày 12/10/2026 (Kết luận số 76-KL/TW, Kết luận số 226-KL/TW - chỉ đối chiếu số, ngày, cơ quan ban hành, trích yếu); Skill 29 và Phụ lục 2, 3, Checklist 02, 03, 04, 06 của Bộ quy tắc KTC-Ra-Soat-897 ' + ver + '.',
 'Nguyễn Ngọc Quang Phục, Phó Trưởng phòng TH-HC&QT')
b.footer_pages()
b.save(RA)
print(RA)
