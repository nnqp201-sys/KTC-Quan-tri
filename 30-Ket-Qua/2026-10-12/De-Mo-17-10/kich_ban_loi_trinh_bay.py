# -*- coding: utf-8 -*-
"""Dựng tệp Word: Kịch bản lời trình bày 30 phút (08 giờ 40 - 09 giờ 10 ngày 17/10/2026), theo từng phút: chiếu gì, mở tệp nào, nói gì."""
import os, sys
import docx
from docx.shared import Cm, Pt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tao_du_lieu_gia_dinh as G
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH


def bang(d, td, hang, rong):
    t = d.add_table(rows=1, cols=len(td)); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, x in enumerate(td):
        G.o_bang(t.cell(0, j), [(x, True, False, 13)])
    for h in hang:
        r = t.add_row()
        for j, x in enumerate(h):
            G.o_bang(r.cells[j], [(x, False, False, 13)], can=WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT)
    G.rong(t, rong)
    G.doan(d, '', sau=0)
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))

d = docx.Document()
s = d.sections[0]
s.page_width, s.page_height = Cm(21), Cm(29.7)
s.top_margin, s.bottom_margin, s.left_margin, s.right_margin = Cm(2), Cm(2), Cm(3), Cm(2)
st = d.styles['Normal']; st.font.name = 'Times New Roman'; st.font.size = Pt(14)
st.element.rPr.rFonts.set(docx.oxml.ns.qn('w:eastAsia'), 'Times New Roman')
G.doan(d, 'KỊCH BẢN LỜI TRÌNH BÀY', dam=True, can='giua', sau=0)
G.doan(d, 'Trình diễn ứng dụng trí tuệ nhân tạo, 08 giờ 40 - 09 giờ 10 ngày 17/10/2026', dam=True, can='giua', sau=0); G.ke(d)
G.doan(d, 'Người trình bày: Đồng chí Nguyễn Ngọc Quang Phục. Người thao tác máy: Đồng chí Đỗ Thành Công. Mọi tệp nằm trong thư mục '
          'BAN-TRINH-DIEN-17-10, đánh số theo thứ tự mở. Lời nói dưới đây là gợi ý, người trình bày nói theo cách của mình.')

PHAN = [
 ('MỞ ĐẦU (05 phút: 08 giờ 40 - 08 giờ 45)', [
  ['00:00', 'Trang trình chiếu 1', 'Kính thưa các đồng chí. Phòng TH-HC&QT xin trình bày 03 nội dung theo đề nghị của Đoàn: Tổng hợp kế hoạch; xây dựng báo cáo; soạn thảo, rà soát văn bản.'],
  ['00:30', 'Trang trình chiếu 2', 'Ba nguyên tắc: Công cụ đọc, đối chiếu, dự thảo - người có thẩm quyền quyết định; mọi kết quả truy được về nguồn; không đưa tài liệu mật vào công cụ.'],
  ['01:00', 'Video 1 (03 phút 44 giây)', 'Không nói - để video chạy. Video giới thiệu kho dữ liệu nền, hệ rà soát 897, bộ công cụ KTC-Quan-tri với 08 kỹ năng, 07 trợ lý AI.'],
 ]),
 ('PHẦN 1. TỔNG HỢP KẾ HOẠCH CÔNG TÁC QUÝ (08 phút: 08 giờ 45 - 08 giờ 53)', [
  ['00:00', 'Trang trình chiếu 3', 'Tình huống: Bộ phận tổng hợp nhận dự thảo kế hoạch quý IV của 06 đơn vị, 60 nhiệm vụ. Dữ liệu là giả định.'],
  ['00:30', 'Video T1 (01 phút 11 giây)', 'Để video chạy: Chọn thư mục dữ liệu, giao việc, công cụ làm việc, cuối video là tệp kết quả. Nói chen: “Công cụ đang đọc từng tệp, kiểm tra mẫu, thời hạn, sản phẩm.”'],
  ['01:15', 'Mở tệp 11 (kết quả Cowork)', 'Chỉ 03 điểm: (1) Phòng Nghiệp vụ 2 nộp nhầm mẫu kế hoạch tháng - công cụ còn dẫn đúng Thông báo kết luận yêu cầu nộp kế hoạch quý; (2) hai cặp nhiệm vụ trùng giữa các đơn vị; (3) nhiệm vụ thiếu thời hạn - công cụ tự đề xuất tháng 11 vì công văn cấp trên yêu cầu báo cáo trước 30/11.'],
  ['03:00', 'Vẫn tệp 11 - kéo tới dòng 1.4', '“Công cụ cũng có chỗ chưa tốt: 06 dòng trong bảng bị mất dữ liệu. Bảng tính do công cụ dựng vẫn phải được người tổng hợp kiểm tra.”'],
  ['03:45', 'Trang trình chiếu 4, Video T2 (56 giây, cuối video là bảng đối chiếu)', 'Tra cứu Hệ thống quản lý văn bản và điều hành: Công cụ chỉ đọc trong phiên người dùng đã đăng nhập, không nhập mật khẩu, không bấm xử lý.'],
  ['04:45', 'Mở tệp 12 (kết quả chạy trước, trang tính 4)', 'Hai nhiệm vụ cấp trên đã giao, có thời hạn, chưa đơn vị nào đăng ký: Báo cáo tiết kiệm, chống lãng phí (hạn 15/11); sắp xếp trụ sở (hạn 30/11).'],
  ['06:00', 'Nói, không chiếu', 'Bài học thật: Khi chạy đối chiếu ở một cuộc hội thoại riêng, không đưa kèm dự thảo kế hoạch, công cụ nêu tới 09 việc “chưa ai nhận” - thực tế chỉ 02. Công cụ có cảnh báo phạm vi, nhưng người dùng phải đưa đủ hồ sơ.'],
  ['07:00', 'Nói nhanh', 'Theo dõi, đôn đốc: Cảnh báo sắp đến hạn, quá hạn; dự thảo công văn đôn đốc. Tình huống thực tế: Thông báo kết luận được ráp ngay khi cuộc họp đang diễn ra.'],
 ]),
 ('PHẦN 2. XÂY DỰNG BÁO CÁO THÁNG (07 phút: 08 giờ 53 - 09 giờ 00)', [
  ['00:00', 'Trang trình chiếu 5', 'Tình huống: Báo cáo tháng 9 của 06 đơn vị, kế hoạch tháng 24 nhiệm vụ, báo cáo tháng 8 đã ban hành.'],
  ['00:30', 'Video T3 (01 phút 02 giây)', 'Để video chạy, cuối video là dự thảo báo cáo và phụ lục đối chiếu; nói chen: “Công cụ phát triển từ báo cáo tháng trước, giữ lời văn của cơ quan.”'],
  ['01:15', 'Mở tệp 21 (báo cáo Cowork) và tệp 22 (bảng đối chiếu)', 'Chỉ 03 điểm: (1) 03 nhiệm vụ chưa có trong báo cáo - công cụ ghi “chưa có thông tin”, không kết luận “chưa làm”; (2) tự nhận ra 02 việc tồn từ tháng 8; (3) số liệu hai đơn vị lệch nhau 112 và 120 lượt người.'],
  ['03:30', 'Mở tệp 23 (kết quả chạy trước)', 'Khi đưa thêm danh mục văn bản: Công cụ tìm được Quyết định đã ban hành làm minh chứng cho việc đơn vị quên báo cáo; chỉ ra hai đơn vị cùng nhận một kết quả - lượt chạy nhanh đã bỏ sót điểm này.'],
  ['05:30', 'Nói nhanh', 'Hỏi nhanh phục vụ giao ban: “Đơn vị nào còn tồn đọng?” - câu trả lời dẫn đúng dòng dữ liệu. Tình huống thực tế: Đọc 40 tệp của 13 đơn vị, hơn 300 nhiệm vụ.'],
 ]),
 ('PHẦN 3. SOẠN THẢO, RÀ SOÁT VĂN BẢN (08 phút: 09 giờ 00 - 09 giờ 08)', [
  ['00:00', 'Trang trình chiếu 8', 'Nói nhanh: Soạn từ văn bản tương tự đã ban hành, không từ mẫu trống; một quyết định đi từ tra cứu đến khi ký khoảng 10 ngày, người có nghiệp vụ bắt được 02 lỗi căn cứ của công cụ.'],
  ['02:00', 'Trang trình chiếu 6, Video T4 (01 phút 01 giây, cuối video là báo cáo rà soát)', 'Văn bản rà soát là một dự thảo văn bản của Đảng đã đổi tên cơ quan, đổi cấp để ẩn danh. Công cụ tự nhận ra văn bản của Đảng, áp Hướng dẫn số 05-HD/VPTW, không áp Nghị định số 30/2020/NĐ-CP.'],
  ['03:00', 'Mở tệp 31 (báo cáo rà soát đầy đủ)', '25 phát hiện, 0 Mức 1, 07 Mức 2. Chỉ 03 điểm: Chương trình của đảng ủy nhưng ký hiệu “/TU”; tên loại cỡ 14, quy định 15 - 16 (đo trên tệp thật); cụm “Ban Thường vụ Đảng ủy” không rõ là cấp nào.'],
  ['05:00', 'Mở tệp 32 (lượt chạy nhanh trên Cowork)', 'Cùng văn bản, lượt chạy nhanh chỉ ra 06 phát hiện, trong đó 01 phát hiện sai. Mỗi lượt có điểm mạnh, điểm sai - vì vậy rà soát chính thức phải chạy đủ quy trình và luôn có người kiểm tra.'],
  ['06:30', 'Trang trình chiếu 7', 'Hệ rà soát công khai giới hạn: Kiểm thử trên tệp cài sẵn 30 lỗi - đúng 24, sai mức 02, bỏ sót 04. Ô “Người kiểm tra” luôn là người thật.'],
 ]),
 ('KẾT THÚC (02 phút: 09 giờ 08 - 09 giờ 10)', [
  ['00:00', 'Trang trình chiếu 9', 'Đề xuất để bắt đầu: Lập kho dữ liệu nền trước; chọn 01 - 02 việc lặp lại hằng tháng; quy định rõ dữ liệu không đưa vào công cụ và ai là người kiểm tra.'],
  ['01:00', 'Trang trình chiếu 10, 11', 'Trường Cao đẳng Kon Tum sẵn sàng chia sẻ, hỗ trợ mọi công cụ khi nhận được thông tin đầu vào và yêu cầu sản phẩm đầu ra. Trân trọng cảm ơn các đồng chí.'],
 ]),
]
for td, hang in PHAN:
    G.doan(d, td, dam=True)
    bang(d, ['Mốc', 'Chiếu, mở', 'Lời trình bày (gợi ý)'], hang, (1.6, 4.4, 10.0))
G.doan(d, 'DỰ PHÒNG', dam=True)
for x in ['- Video không phát: Mở thẳng tệp kết quả, đọc lời thuyết minh.',
          '- Quá giờ: Bỏ các dòng “Nói nhanh”; giữ 03 nội dung trọng tâm.',
          '- Đoàn đề nghị chạy trực tiếp ở phần thảo luận: Dùng thư mục Du-lieu-gia-dinh, KHÔNG kéo thư mục đáp án vào; chạy trong cùng một cuộc hội thoại.']:
    G.doan(d, x, thut=False)
ra = os.path.join(D, 'KICH-BAN-LOI-TRINH-BAY_17.10.2026.docx'); d.save(ra); print(ra)
