# -*- coding: utf-8 -*-
"""Sinh bộ dữ liệu GIẢ ĐỊNH D1–D4 phục vụ trình diễn ngày 17/10/2026 (Cơ quan A, 06 đơn vị).
Chạy: python tao_du_lieu_gia_dinh.py   -> thư mục Du-lieu-gia-dinh/ cạnh tệp này.
Khuôn: Phụ lục Ia/Ib/IIb Thông báo số 736/TB-CĐKT; tệp xuất Hệ thống QLVB&ĐH (office_ca_nhan.py đọc được).
Mọi tên cơ quan, người, số ký hiệu đều là giả định. Lỗi cài sẵn: xem _Dap-an-KHONG-dua-vao-cong-cu/DAP-AN.md.
"""
import datetime as dt
import os
import subprocess
import sys

import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')
GOC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Du-lieu-gia-dinh')
NHAN = 'Dữ liệu giả định phục vụ trình diễn'
CQ = 'CƠ QUAN A'
TRUC = {
    1: 'Trục (1) - Thực hiện mục tiêu phát triển Kinh tế - xã hội và nhiệm vụ chính trị được giao',
    2: 'Trục (2) - Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát',
    3: 'Trục (3) - Thúc đẩy phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số',
    4: 'Trục (4) - Xây dựng đảng và hệ thống chính trị trong sạch, vững mạnh; giữ gìn đoàn kết, thống nhất nội bộ; phòng, chống tham nhũng, lãng phí, tiêu cực',
    5: 'Trục (5) - Phát triển văn hóa, con người, bảo đảm an sinh xã hội, nâng cao đời sống nhân dân',
    6: 'Trục (6) - Củng cố quốc phòng, an ninh, giữ vững ổn định chính trị - xã hội, nâng cao hiệu quả đối ngoại và hội nhập quốc tế',
}
DV = {  # mã: (tên đơn vị, người trực tiếp chỉ đạo)
    'VP': ('Văn phòng', 'Thủ trưởng cơ quan'),
    'TC': ('Phòng Tổ chức cán bộ', 'Thủ trưởng cơ quan'),
    'KT': ('Phòng Kế hoạch - Tài chính', 'Phó Thủ trưởng 1'),
    'N1': ('Phòng Nghiệp vụ 1', 'Phó Thủ trưởng 1'),
    'N2': ('Phòng Nghiệp vụ 2', 'Phó Thủ trưởng 2'),
    'CDS': ('Phòng Thông tin - Chuyển đổi số', 'Phó Thủ trưởng 2'),
}
K, C, T = 'Khó và phức tạp', 'Cao', 'Trung bình'
DUA, TX = 'Đưa vào KH Trường', 'Thường xuyên của đơn vị'

# ---------------------------------------------------------------- D1: kế hoạch Quý IV/2026
# (trục, nội dung, sản phẩm, số lượng, độ khó, thời gian hoàn thành, ghi chú)
D1 = {
 'VP': [
  (1, 'Tổng hợp, xây dựng Chương trình công tác năm 2027 của cơ quan', 'Chương trình', 1, K, 'Tháng 12/2026', DUA),
  (1, 'Tổng hợp, xây dựng Báo cáo kết quả công tác năm 2026', 'Báo cáo', 1, C, 'Tháng 12/2026', DUA),
  (1, 'Tổ chức giao ban tháng, ban hành thông báo kết luận', 'Thông báo', 3, T, 'Hằng tháng', TX),
  (2, 'Xây dựng Quy chế quản lý, sử dụng tài sản công của cơ quan', 'Quyết định', 1, K, 'Tháng 11/2026', DUA),
  (2, 'Sửa đổi, bổ sung Quy chế làm việc của cơ quan', 'Quyết định', 1, C, None, DUA),
  (3, 'Tổ chức tập huấn sử dụng trí tuệ nhân tạo trong công tác văn phòng', 'Lớp tập huấn', 2, C, 'Tháng 11/2026', DUA),
  (3, 'Số hóa hồ sơ, tài liệu lưu trữ giai đoạn 2021 - 2025', 'Hồ sơ', 500, T, 'Tháng 12/2026', TX),
  (4, 'Tham mưu tổ chức Hội nghị cán bộ, công chức, viên chức năm 2026', 'Hội nghị', 1, C, 'Tháng 12/2026', DUA),
  (5, 'Tổ chức các hoạt động chăm lo Tết cho cán bộ, người lao động', None, 1, T, 'Tháng 12/2026', TX),
  (6, 'Kiểm tra công tác phòng cháy, chữa cháy tại trụ sở làm việc', 'Biên bản', 1, T, 'Tháng 10/2026', TX),
 ],
 'TC': [
  (1, 'Xây dựng Kế hoạch đào tạo, bồi dưỡng cán bộ năm 2027', 'Kế hoạch', 1, C, 'Tháng 12/2026', DUA),
  (1, 'Rà soát, bổ sung quy hoạch cán bộ lãnh đạo, quản lý', 'Báo cáo', 1, K, 'Tháng 11/2026', DUA),
  (2, 'Xây dựng Quy định đánh giá, xếp loại chất lượng cán bộ hằng quý', 'Quyết định', 1, K, 'Tháng 10/2026', DUA),
  (2, 'Rà soát vị trí việc làm sau sắp xếp tổ chức bộ máy', 'Đề án', 1, K, None, DUA),
  (3, 'Cập nhật hồ sơ lên cơ sở dữ liệu quốc gia về cán bộ, công chức, viên chức', 'Hồ sơ', 85, T, 'Tháng 11/2026', TX),
  (4, 'Tham mưu đánh giá, xếp loại tổ chức đảng, đảng viên năm 2026', 'Báo cáo', 1, C, 'Tháng 12/2026', DUA),
  (4, 'Tổ chức học tập, quán triệt nghị quyết của cấp ủy cấp trên', 'Hội nghị', 1, T, 'Tháng 10/2026', TX),
  (5, 'Thực hiện chế độ nâng lương, phụ cấp đợt 2 năm 2026', 'Quyết định', 12, T, 'Tháng 12/2026', TX),
  (5, 'Tổng kết công tác thi đua, khen thưởng năm 2026', 'Báo cáo', 1, C, 'Tháng 12/2026', DUA),
  (6, 'Rà soát tiêu chuẩn chính trị cán bộ phục vụ công tác bảo vệ chính trị nội bộ', 'Báo cáo', 1, C, 'Tháng 11/2026', TX),
 ],
 'KT': [
  (1, 'Xây dựng dự toán ngân sách năm 2027', 'Dự toán', 1, K, 'Tháng 10/2026', DUA),
  (1, 'Báo cáo tình hình thực hiện dự toán ngân sách năm 2026', 'Báo cáo', 1, C, 'Tháng 12/2026', DUA),
  (1, 'Quyết toán các nguồn kinh phí quý III/2026', 'Báo cáo', 1, T, 'Tháng 10/2026', TX),
  (2, 'Xây dựng Quy chế quản lý, sử dụng tài sản công', 'Quyết định', 1, K, 'Tháng 11/2026', DUA),
  (2, 'Sửa đổi, bổ sung Quy chế chi tiêu nội bộ', 'Quyết định', 1, C, 'Tháng 12/2026', DUA),
  (2, 'Tự kiểm tra tài chính, kế toán năm 2026', 'Báo cáo', 1, C, None, TX),
  (3, 'Triển khai hóa đơn điện tử, thanh toán không dùng tiền mặt', None, 1, T, 'Tháng 11/2026', TX),
  (4, 'Công khai tài chính, tài sản quý III/2026', 'Thông báo', 1, T, 'Tháng 10/2026', TX),
  (5, 'Chi trả chế độ, chính sách cho cán bộ, người lao động', 'Bảng thanh toán', 3, T, 'Hằng tháng', TX),
  (6, 'Kiểm kê tài sản cuối năm 2026', 'Biên bản', 1, C, 'Tháng 12/2026', DUA),
 ],
 'N1': [
  (1, 'Tham mưu Kế hoạch thực hiện nhiệm vụ trọng tâm năm 2027 của lĩnh vực', 'Kế hoạch', 1, K, 'Tháng 12/2026', DUA),
  (1, 'Báo cáo kết quả thực hiện chỉ tiêu chuyên môn quý IV/2026', 'Báo cáo', 1, C, 'Tháng 12/2026', DUA),
  (1, 'Thẩm định hồ sơ chuyên môn theo đề nghị của cơ sở', 'Hồ sơ', 40, T, 'Hằng tháng', TX),
  (1, 'Tổ chức 02 đoàn khảo sát thực tế tại cơ sở', 'Báo cáo', 2, C, 'Tháng 11/2026', DUA),
  (2, 'Rà soát, đề xuất đơn giản hóa thủ tục hành chính', 'Báo cáo', 1, C, 'Tháng 11/2026', DUA),
  (2, 'Kiểm tra việc thực hiện quy định chuyên môn tại 03 đơn vị cơ sở', 'Kết luận', 3, K, 'Tháng 11/2026', DUA),
  (3, 'Cập nhật cơ sở dữ liệu chuyên ngành', 'Bản ghi', 300, T, 'Tháng 12/2026', TX),
  (4, 'Sinh hoạt chuyên đề chi bộ quý IV/2026', 'Biên bản', 1, T, 'Tháng 11/2026', TX),
  (5, 'Tổ chức hội nghị đối thoại với người dân, doanh nghiệp', 'Hội nghị', 1, C, 'Tháng 11/2026', DUA),
  (6, 'Giải quyết đơn thư, phản ánh, kiến nghị thuộc lĩnh vực', 'Văn bản trả lời', 15, T, 'Hằng tháng', TX),
 ],
 'N2': [
  (1, 'Xây dựng Đề án nâng cao chất lượng dịch vụ công giai đoạn 2027 - 2030', 'Đề án', 1, K, 'Tháng 12/2026', DUA),
  (1, 'Báo cáo sơ kết 01 năm thực hiện chương trình phối hợp', 'Báo cáo', 1, C, 'Tháng 11/2026', DUA),
  (1, 'Hướng dẫn nghiệp vụ cho cơ sở', 'Công văn', 4, T, 'Hằng tháng', TX),
  (2, 'Tham gia góp ý dự thảo văn bản của cấp trên', 'Công văn', 6, T, 'Hằng tháng', TX),
  (2, 'Xây dựng quy trình nội bộ giải quyết công việc của phòng', 'Quy trình', 1, C, 'Tháng 11/2026', TX),
  (3, 'Ứng dụng phần mềm theo dõi nhiệm vụ của phòng', 'Báo cáo', 1, T, 'Tháng 12/2026', TX),
  (4, 'Kiểm điểm, đánh giá đảng viên cuối năm 2026', 'Biên bản', 1, T, 'Tháng 12/2026', TX),
  (5, 'Phối hợp tổ chức chương trình an sinh xã hội cuối năm', 'Chương trình', 1, C, 'Tháng 12/2026', DUA),
  (5, 'Khảo sát mức độ hài lòng của người dân đối với dịch vụ công', 'Báo cáo', 1, C, 'Tháng 11/2026', DUA),
  (6, 'Phối hợp bảo đảm an ninh, trật tự dịp cuối năm', 'Kế hoạch', 1, T, 'Tháng 12/2026', TX),
 ],
 'CDS': [
  (1, 'Báo cáo kết quả chuyển đổi số năm 2026 của cơ quan', 'Báo cáo', 1, C, 'Tháng 12/2026', DUA),
  (2, 'Xây dựng Quy chế sử dụng trí tuệ nhân tạo trong cơ quan', 'Quyết định', 1, K, 'Tháng 11/2026', DUA),
  (3, 'Xây dựng Kế hoạch chuyển đổi số năm 2027', 'Kế hoạch', 1, K, 'Tháng 12/2026', DUA),
  (3, 'Tổ chức tập huấn ứng dụng trí tuệ nhân tạo cho cán bộ, công chức của cơ quan', 'Lớp tập huấn', 2, C, 'Tháng 11/2026', DUA),
  (3, 'Xây dựng kho dữ liệu văn bản dùng chung của cơ quan', 'Kho dữ liệu', 1, K, 'Tháng 12/2026', DUA),
  (3, 'Nâng cấp cổng thông tin điện tử của cơ quan', 'Biên bản nghiệm thu', 1, C, 'Tháng 11/2026', DUA),
  (3, 'Đánh giá an toàn thông tin hệ thống mạng nội bộ', 'Báo cáo', 1, C, 'Tháng 10/2026', DUA),
  (3, 'Hỗ trợ kỹ thuật, bảo trì thiết bị công nghệ thông tin', 'Phiếu hỗ trợ', 60, T, 'Hằng tháng', TX),
  (4, 'Tuyên truyền về công tác xây dựng Đảng trên cổng thông tin điện tử', 'Tin, bài', 12, T, 'Hằng tháng', TX),
  (6, 'Diễn tập ứng cứu sự cố an toàn thông tin', 'Báo cáo', 1, C, 'Tháng 11/2026', DUA),
 ],
}

# ---------------------------------------------------------------- D3: kế hoạch và kết quả tháng 9/2026
# kế hoạch tháng của cơ quan: (trục, nội dung, đơn vị chủ trì, sản phẩm, số lượng, độ khó, thời gian)
KH9 = [
 (1, 'Tổng hợp báo cáo kết quả công tác quý III/2026', 'VP', 'Báo cáo', 1, C, '25/9/2026'),
 (1, 'Tổ chức giao ban tháng 9, ban hành thông báo kết luận', 'VP', 'Thông báo', 1, T, '10/9/2026'),
 (2, 'Ban hành Quy chế văn thư, lưu trữ (sửa đổi)', 'VP', 'Quyết định', 1, C, '30/9/2026'),
 (3, 'Ban hành Kế hoạch bảo đảm an toàn thông tin tháng cao điểm', 'CDS', 'Kế hoạch', 1, C, '15/9/2026'),
 (1, 'Tổ chức 02 lớp bồi dưỡng kỹ năng soạn thảo văn bản', 'TC', 'Lớp bồi dưỡng', 2, C, '20/9/2026'),
 (2, 'Trình ban hành Kế hoạch tuyển dụng viên chức năm 2026', 'TC', 'Kế hoạch', 1, K, '25/9/2026'),
 (4, 'Sinh hoạt chuyên đề quý III về học tập và làm theo tư tưởng, đạo đức, phong cách Hồ Chí Minh', 'TC', 'Biên bản', 1, T, '20/9/2026'),
 (5, 'Xét nâng bậc lương thường xuyên đợt 2', 'TC', 'Quyết định', 8, T, '30/9/2026'),
 (1, 'Lập báo cáo tài chính quý III/2026', 'KT', 'Báo cáo', 1, C, '30/9/2026'),
 (1, 'Rà soát, điều chỉnh dự toán chi thường xuyên', 'KT', 'Tờ trình', 1, C, '20/9/2026'),
 (4, 'Công khai dự toán điều chỉnh', 'KT', 'Thông báo', 1, T, '25/9/2026'),
 (5, 'Chi trả lương, phụ cấp tháng 9', 'KT', 'Bảng thanh toán', 1, T, '10/9/2026'),
 (1, 'Thẩm định hồ sơ chuyên môn theo đề nghị của cơ sở', 'N1', 'Hồ sơ', 14, T, '30/9/2026'),
 (2, 'Kiểm tra chuyên môn tại đơn vị cơ sở B', 'N1', 'Kết luận', 1, K, '25/9/2026'),
 (1, 'Báo cáo chuyên đề 9 tháng thuộc lĩnh vực', 'N1', 'Báo cáo', 1, C, '25/9/2026'),
 (6, 'Giải quyết đơn thư, phản ánh, kiến nghị', 'N1', 'Văn bản trả lời', 5, T, '30/9/2026'),
 (1, 'Hướng dẫn nghiệp vụ cho cơ sở', 'N2', 'Công văn', 2, T, '30/9/2026'),
 (2, 'Góp ý dự thảo văn bản của cấp trên', 'N2', 'Công văn', 3, T, '30/9/2026'),
 (5, 'Khảo sát nhu cầu hỗ trợ của người dân tại 02 địa bàn', 'N2', 'Báo cáo', 1, C, '25/9/2026'),
 (1, 'Sơ kết 9 tháng thực hiện chương trình phối hợp', 'N2', 'Báo cáo', 1, C, '28/9/2026'),
 (3, 'Đánh giá mức độ chuyển đổi số quý III/2026', 'CDS', 'Báo cáo', 1, C, '30/9/2026'),
 (3, 'Triển khai chữ ký số cho 100% lãnh đạo phòng', 'CDS', 'Chứng thư số', 12, C, '20/9/2026'),
 (3, 'Hỗ trợ kỹ thuật, bảo trì thiết bị', 'CDS', 'Phiếu hỗ trợ', 20, T, '30/9/2026'),
 (4, 'Đăng tin, bài về xây dựng Đảng trên cổng thông tin', 'CDS', 'Tin, bài', 4, T, '30/9/2026'),
]
# kết quả đơn vị báo cáo: (trục, nội dung, sản phẩm, SL, độ khó, tỷ lệ khối lượng, chất lượng, tiến độ)
D3 = {
 'VP': [
  (1, 'Tổng hợp báo cáo kết quả công tác quý III/2026 (Báo cáo số 318/BC-CQA ngày 24/9/2026)', 'Báo cáo', 1, C, 1, 1, 1),
  (1, 'Tổ chức giao ban tháng 9, ban hành Thông báo kết luận số 301/TB-CQA ngày 09/9/2026', 'Thông báo', 1, T, 1, 1, 1),
  (3, 'Ban hành Kế hoạch bảo đảm an toàn thông tin tháng cao điểm (Kế hoạch số 305/KH-CQA ngày 14/9/2026)', 'Kế hoạch', 1, C, 1, 1, 1),
  (1, 'Phối hợp tổ chức 02 lớp bồi dưỡng kỹ năng soạn thảo văn bản, 120 lượt người tham dự', 'Lớp bồi dưỡng', 2, C, 1, 1, 1),
 ],
 'TC': [
  (1, 'Tổ chức 02 lớp bồi dưỡng kỹ năng soạn thảo văn bản, 112 lượt người tham dự', 'Lớp bồi dưỡng', 2, C, 1, 1, 1),
  (2, 'Trình ban hành Kế hoạch tuyển dụng viên chức năm 2026 (đã trình, đang chờ phê duyệt)', 'Kế hoạch', 1, K, 1, 0.75, 0.75),
  (4, 'Sinh hoạt chuyên đề quý III về học tập và làm theo tư tưởng, đạo đức, phong cách Hồ Chí Minh', 'Biên bản', 1, T, 1, 1, 1),
  (5, 'Xét nâng bậc lương thường xuyên đợt 2 cho 08 trường hợp', 'Quyết định', 8, T, 1, 1, 1),
 ],
 'KT': [
  (1, 'Lập báo cáo tài chính quý III/2026', 'Báo cáo', 1, C, 1, 1, 0.75),
  (1, 'Rà soát, điều chỉnh dự toán chi thường xuyên (Tờ trình số 44/TTr-KHTC ngày 18/9/2026)', 'Tờ trình', 1, C, 1, 1, 1),
  (4, 'Công khai dự toán điều chỉnh', 'Thông báo', 1, T, 1, 1, 1),
  (5, 'Chi trả lương, phụ cấp tháng 9', 'Bảng thanh toán', 1, T, 1, 1, 1),
 ],
 'N1': [
  (1, 'Thẩm định hồ sơ chuyên môn theo đề nghị của cơ sở: 12/14 hồ sơ', 'Hồ sơ', 14, T, '12/14', 1, 1),
  (1, 'Báo cáo chuyên đề 9 tháng thuộc lĩnh vực', 'Báo cáo', 1, C, 1, 0.75, 1),
  (6, 'Giải quyết đơn thư, phản ánh, kiến nghị: 05/05 đơn', 'Văn bản trả lời', 5, T, 1, 1, 1),
 ],
 'N2': [
  (1, 'Hướng dẫn nghiệp vụ cho cơ sở: 02 công văn', 'Công văn', 2, T, 1, 1, 1),
  (2, 'Góp ý dự thảo văn bản của cấp trên: 03 công văn', 'Công văn', 3, T, 1, 1, 1),
  (5, 'Khảo sát nhu cầu hỗ trợ của người dân tại 02 địa bàn', 'Báo cáo', 1, C, 1, 1, 0.75),
  (1, 'Sơ kết 9 tháng thực hiện chương trình phối hợp', 'Báo cáo', 1, C, 1, 1, 1),
 ],
 'CDS': [
  (3, 'Ban hành Kế hoạch bảo đảm an toàn thông tin tháng cao điểm (Kế hoạch số 305/KH-CQA ngày 14/9/2026)', 'Kế hoạch', 1, C, 1, 1, 1),
  (3, 'Triển khai chữ ký số cho lãnh đạo phòng: 10/12 chứng thư số', 'Chứng thư số', 12, C, '10/12', 1, 0.75),
  (3, 'Hỗ trợ kỹ thuật, bảo trì thiết bị: 23 lượt', 'Phiếu hỗ trợ', 20, T, 1, 1, 1),
  (4, 'Đăng 04 tin, bài về xây dựng Đảng trên cổng thông tin', 'Tin, bài', 4, T, 1, 1, 1),
 ],
}

# ---------------------------------------------------------------- D2: danh mục văn bản trên Hệ thống QLVB&ĐH (giả định)
# (số ký hiệu, loại, trích yếu, ngày ban hành, cơ quan ban hành, người soạn thảo, vai trò)
CT, A = 'Cơ quan cấp trên (giả định)', 'Cơ quan A'
D2 = [
 ('12/CTr-CQCT', 'Chương trình', 'Chương trình công tác năm 2026 của Cơ quan cấp trên', '15/01/2026', CT, '', 'Nhận để thực hiện'),
 ('05/KH-CQA', 'Kế hoạch', 'Kế hoạch công tác năm 2026 của Cơ quan A', '20/01/2026', A, 'Chuyên viên Văn phòng 1', 'Xử lý chính'),
 ('188/KH-CQA', 'Kế hoạch', 'Kế hoạch công tác quý III/2026 của Cơ quan A', '02/7/2026', A, 'Chuyên viên Văn phòng 1', 'Xử lý chính'),
 ('1105/CQCT-VP', 'Công văn', 'V/v đăng ký nhiệm vụ trọng tâm 6 tháng cuối năm 2026', '06/7/2026', CT, '', 'Nhận để thực hiện'),
 ('201/TB-CQA', 'Thông báo', 'Kết luận của Thủ trưởng cơ quan tại cuộc họp giao ban tháng 7/2026', '10/7/2026', A, 'Chuyên viên Văn phòng 2', 'Xử lý chính'),
 ('74/KH-CQCT', 'Kế hoạch', 'Kế hoạch chuyển đổi số, ứng dụng trí tuệ nhân tạo trong các cơ quan năm 2026', '21/7/2026', CT, '', 'Nhận để thực hiện'),
 ('224/KH-CQA', 'Kế hoạch', 'Kế hoạch triển khai chữ ký số trong Cơ quan A', '28/7/2026', A, 'Chuyên viên Phòng Thông tin - Chuyển đổi số', 'Phối hợp'),
 ('1260/CQCT-TC', 'Công văn', 'V/v rà soát vị trí việc làm sau sắp xếp tổ chức bộ máy, báo cáo trước ngày 30/11/2026', '04/8/2026', CT, '', 'Nhận để thực hiện'),
 ('246/TB-CQA', 'Thông báo', 'Kết luận của Thủ trưởng cơ quan tại cuộc họp giao ban tháng 8/2026', '08/8/2026', A, 'Chuyên viên Văn phòng 2', 'Xử lý chính'),
 ('252/BC-CQA', 'Báo cáo', 'Báo cáo kết quả công tác tháng 7/2026', '10/8/2026', A, 'Chuyên viên Văn phòng 1', 'Xử lý chính'),
 ('88/KH-CQCT', 'Kế hoạch', 'Kế hoạch tổ chức đối thoại với người dân, doanh nghiệp năm 2026', '18/8/2026', CT, '', 'Nhận để thực hiện'),
 ('270/KH-CQA', 'Kế hoạch', 'Kế hoạch công tác tháng 9/2026 của Cơ quan A', '28/8/2026', A, 'Chuyên viên Văn phòng 1', 'Xử lý chính'),
 ('1391/CQCT-KH', 'Công văn', 'V/v xây dựng dự toán ngân sách năm 2027, gửi trước ngày 20/10/2026', '03/9/2026', CT, '', 'Nhận để thực hiện'),
 ('284/BC-CQA', 'Báo cáo', 'Báo cáo kết quả công tác tháng 8/2026', '05/9/2026', A, 'Chuyên viên Văn phòng 1', 'Xử lý chính'),
 ('301/TB-CQA', 'Thông báo', 'Kết luận của Thủ trưởng cơ quan tại cuộc họp giao ban tháng 9/2026', '09/9/2026', A, 'Chuyên viên Văn phòng 2', 'Xử lý chính'),
 ('305/KH-CQA', 'Kế hoạch', 'Kế hoạch bảo đảm an toàn thông tin tháng cao điểm', '14/9/2026', A, 'Chuyên viên Phòng Thông tin - Chuyển đổi số', 'Phối hợp'),
 ('96/KH-CQCT', 'Kế hoạch', 'Kế hoạch tổng rà soát, sắp xếp trụ sở làm việc của các cơ quan, đơn vị; báo cáo kết quả trước ngày 30/11/2026', '15/9/2026', CT, '', 'Nhận để thực hiện'),
 ('44/TTr-KHTC', 'Tờ trình', 'Tờ trình điều chỉnh dự toán chi thường xuyên năm 2026', '18/9/2026', A, 'Chuyên viên Phòng Kế hoạch - Tài chính', 'Phối hợp'),
 ('1482/CQCT-VP', 'Công văn', 'V/v báo cáo kết quả thực hành tiết kiệm, chống lãng phí năm 2026, gửi trước ngày 15/11/2026', '22/9/2026', CT, '', 'Nhận để thực hiện'),
 ('215/QĐ-CQA', 'Quyết định', 'Quyết định ban hành Quy chế văn thư, lưu trữ của Cơ quan A (sửa đổi)', '24/9/2026', A, 'Chuyên viên Văn phòng 2', 'Xử lý chính'),
 ('318/BC-CQA', 'Báo cáo', 'Báo cáo kết quả công tác quý III/2026', '24/9/2026', A, 'Chuyên viên Văn phòng 1', 'Xử lý chính'),
 ('102/KH-CQCT', 'Kế hoạch', 'Kế hoạch tập huấn sử dụng trí tuệ nhân tạo cho cán bộ, công chức quý IV/2026', '25/9/2026', CT, '', 'Nhận để thực hiện'),
 ('322/QĐ-CQA', 'Quyết định', 'Quyết định nâng bậc lương thường xuyên đợt 2 năm 2026', '28/9/2026', A, 'Chuyên viên Phòng Tổ chức cán bộ', 'Phối hợp'),
 ('1533/CQCT-TC', 'Công văn', 'V/v đánh giá, xếp loại chất lượng cán bộ, công chức, viên chức năm 2026', '30/9/2026', CT, '', 'Nhận để thực hiện'),
 ('330/KH-CQA', 'Kế hoạch', 'Kế hoạch kiểm tra chuyên môn tại các đơn vị cơ sở quý IV/2026', '02/10/2026', A, 'Chuyên viên Phòng Nghiệp vụ 1', 'Phối hợp'),
 ('336/TB-CQA', 'Thông báo', 'Kết luận của Thủ trưởng cơ quan tại cuộc họp giao ban tháng 10/2026: Giao các đơn vị gửi dự thảo kế hoạch quý IV trước ngày 08/10/2026', '06/10/2026', A, 'Chuyên viên Văn phòng 2', 'Xử lý chính'),
 ('1590/CQCT-VP', 'Công văn', 'V/v xây dựng Chương trình công tác năm 2027, gửi trước ngày 10/12/2026', '07/10/2026', CT, '', 'Nhận để thực hiện'),
 ('341/CQA-VP', 'Công văn', 'V/v đôn đốc gửi báo cáo tháng 9 và dự thảo kế hoạch quý IV/2026', '08/10/2026', A, 'Chuyên viên Văn phòng 1', 'Xử lý chính'),
]


# ================================================================= tiện ích Excel
F = lambda dam=False, nghieng=False, co=12: Font(name='Times New Roman', size=co, bold=dam, italic=nghieng)
VIEN = Border(*(Side(style='thin'),) * 4)
GIUA = Alignment(horizontal='center', vertical='center', wrap_text=True)
TRAI = Alignment(horizontal='left', vertical='center', wrap_text=True)
DIEM = '=IF(G{r}="Khó và phức tạp",200,IF(G{r}="Cao",150,IF(G{r}="Trung bình",120,100)))'


def o(ws, toa_do, gia_tri, dam=False, can=TRAI, vien=True, nghieng=False):
    c = ws[toa_do]
    c.value, c.font, c.alignment = gia_tri, F(dam, nghieng), can
    if vien:
        c.border = VIEN
    return c


def dau_trang(ws, so_cot, phu_luc, don_vi, ten, cot_phai):
    cuoi = get_column_letter(so_cot)
    ws.merge_cells(f'A1:{cuoi}1')
    o(ws, 'A1', f'{phu_luc} — {NHAN}', nghieng=True, can=Alignment(horizontal='right'), vien=False)
    o(ws, 'A2', CQ, dam=True, vien=False)
    o(ws, f'{cot_phai}2', 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', dam=True, can=GIUA, vien=False)
    o(ws, 'A3', f'ĐƠN VỊ: {don_vi}', dam=True, vien=False)
    o(ws, f'{cot_phai}3', 'Độc lập - Tự do - Hạnh phúc', dam=True, can=GIUA, vien=False)
    ws.merge_cells(f'{cot_phai}2:{cuoi}2'); ws.merge_cells(f'{cot_phai}3:{cuoi}3')
    ws.merge_cells(f'A4:{cuoi}4')
    o(ws, 'A4', ten, dam=True, can=GIUA, vien=False)
    ws.row_dimensions[4].height = 40
    ws.page_setup.orientation, ws.page_setup.paperSize = 'landscape', 9
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.oddFooter.center.text = NHAN


def tieu_de_cot(ws, cot, rong):
    for i, (ten, r) in enumerate(zip(cot, rong), 1):
        ch = get_column_letter(i)
        ws.merge_cells(f'{ch}6:{ch}7')
        o(ws, f'{ch}6', ten, dam=True, can=GIUA); ws[f'{ch}7'].border = VIEN
        o(ws, f'{ch}8', f'({i})', can=GIUA, nghieng=True)
        ws.column_dimensions[ch].width = r
    ws.row_dimensions[6].height = 34


def ke_hoach(tep, phu_luc, don_vi, ten, muc_i, hang, cot_dv=None):
    """Phụ lục Ia/Ib: 11 cột. hang: (trục, nội dung, [đơn vị], sản phẩm, SL, độ khó, thời gian, ghi chú)."""
    wb = Workbook(); ws = wb.active; ws.title = phu_luc.split('—')[0].strip()[:28]
    dau_trang(ws, 11, phu_luc, don_vi, ten, 'E')
    tieu_de_cot(ws, ['TT', 'NỘI DUNG CÔNG VIỆC', 'Người trực tiếp chỉ đạo', 'Đơn vị chủ trì', 'Sản phẩm/ công việc', 'Số lượng',
                     'Độ khó, mới, phức tạp; phạm vi tác động', 'Thời gian hoàn thành', 'Điểm chấm công việc', 'Hệ số quy đổi', 'Ghi chú'],
                [6, 46, 17, 20, 15, 9, 16, 15, 10, 9, 18])
    r = 9
    ws.merge_cells(f'B{r}:K{r}'); o(ws, f'A{r}', 'I', dam=True, can=GIUA); o(ws, f'B{r}', muc_i, dam=True)
    for t in range(1, 7):
        r += 1
        ws.merge_cells(f'B{r}:K{r}'); o(ws, f'A{r}', t, dam=True, can=GIUA); o(ws, f'B{r}', TRUC[t], dam=True)
        for i, h in enumerate([x for x in hang if x[0] == t], 1):
            r += 1
            ma, nd, dv, sp, sl, dk, tg, gc = h
            vals = [f'{t}.{i}', nd, DV[dv][1], DV[dv][0], sp, sl, dk, tg, DIEM.format(r=r), f'=I{r}*0.01', gc]
            for j, v in enumerate(vals, 1):
                o(ws, f'{get_column_letter(j)}{r}', v, can=TRAI if j in (2, 5, 11) else GIUA)
    r += 1
    ws.merge_cells(f'B{r}:K{r}'); o(ws, f'A{r}', 'II', dam=True, can=GIUA)
    o(ws, f'B{r}', 'Các nhiệm vụ đột xuất, phát sinh ở kỳ trước phải thực hiện sang kỳ sau (nếu có): Không', dam=True)
    o(ws, f'H{r + 2}', 'LÃNH ĐẠO ĐƠN VỊ', dam=True, can=GIUA, vien=False)
    os.makedirs(os.path.dirname(tep), exist_ok=True); wb.save(tep)


def ket_qua(tep, don_vi, ma, hang):
    """Phụ lục IIb: 16 cột có KPI."""
    wb = Workbook(); ws = wb.active; ws.title = 'PL IIb'
    dau_trang(ws, 16, 'Phụ lục IIb', don_vi, 'BÁO CÁO\nkết quả thực hiện công tác tháng 9 năm 2026', 'G')
    cot = ['TT', 'NỘI DUNG CÔNG VIỆC', 'Người trực tiếp chỉ đạo', 'Đơn vị chủ trì', 'Sản phẩm/ Công việc', 'Số lượng',
           'Độ khó, mới, phức tạp; phạm vi tác động', 'Điểm chấm công việc', 'Hệ số quy đổi', 'Số lượng quy đổi']
    rong = [6, 50, 16, 18, 14, 8, 15, 9, 8, 9, 10, 9, 10, 9, 10, 9]
    for i, ten in enumerate(cot, 1):
        ch = get_column_letter(i)
        ws.merge_cells(f'{ch}6:{ch}7'); o(ws, f'{ch}6', ten, dam=True, can=GIUA); ws[f'{ch}7'].border = VIEN
    for ch1, ch2, ten in (('K', 'L', 'KPI (số lượng)'), ('M', 'N', 'KPI (chất lượng)'), ('O', 'P', 'KPI (tiến độ)')):
        ws.merge_cells(f'{ch1}6:{ch2}6'); o(ws, f'{ch1}6', ten, dam=True, can=GIUA); ws[f'{ch2}6'].border = VIEN
        o(ws, f'{ch1}7', 'Thực tế hoàn thành', dam=True, can=GIUA); o(ws, f'{ch2}7', 'Quy đổi', dam=True, can=GIUA)
    ghi = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)= (8)* 1%', '(10)= (6)* (9)', '(11)=(6)* [Tỷ lệ hoàn thành khối lượng]',
           '(12)= (9)* (11)', '(13)=(11)*[Tỷ lệ hoàn thành chất lượng]', '(14)= (9)* (13)', '(15)=(11)*[Tỷ lệ hoàn thành tiến độ]', '(16)= (9)* (15)']
    for i, (g, w) in enumerate(zip(ghi, rong), 1):
        ch = get_column_letter(i)
        o(ws, f'{ch}8', g, can=GIUA, nghieng=True); ws.column_dimensions[ch].width = w
    ws.row_dimensions[6].height = 30; ws.row_dimensions[7].height = 30; ws.row_dimensions[8].height = 60
    r = 9
    ws.merge_cells(f'B{r}:P{r}'); o(ws, f'A{r}', 'I', dam=True, can=GIUA)
    o(ws, f'B{r}', 'Các nhiệm vụ theo kế hoạch (chương trình) công tác đã đề ra từ đầu tháng', dam=True)
    for t in range(1, 7):
        ds = [x for x in hang if x[0] == t]
        r += 1; rt = r
        ws.merge_cells(f'B{r}:E{r}'); o(ws, f'A{r}', t, dam=True, can=GIUA); o(ws, f'B{r}', TRUC[t], dam=True)
        for ch in 'FGHIJKLMNOP':
            o(ws, f'{ch}{r}', None, dam=True, can=GIUA)
        for i, (_, nd, sp, sl, dk, kl, cl, td) in enumerate(ds, 1):
            r += 1
            vals = [f'{t}.{i}', nd, DV[ma][1], don_vi, sp, sl, dk, DIEM.format(r=r), f'=H{r}*0.01', f'=F{r}*I{r}',
                    f'=F{r}*{kl}', f'=K{r}*I{r}', f'=K{r}*{cl}', f'=I{r}*M{r}', f'=K{r}*{td}', f'=I{r}*O{r}']
            for j, v in enumerate(vals, 1):
                c = o(ws, f'{get_column_letter(j)}{r}', v, can=TRAI if j in (2, 5) else GIUA)
                if j >= 9:
                    c.number_format = '0.00'
        if ds:
            for ch in 'FJKLMNOP':
                ws[f'{ch}{rt}'].value = f'=SUM({ch}{rt + 1}:{ch}{r})'; ws[f'{ch}{rt}'].number_format = '0.00'
    r += 1
    ws.merge_cells(f'B{r}:P{r}'); o(ws, f'A{r}', 'II', dam=True, can=GIUA)
    o(ws, f'B{r}', 'CÁC NHIỆM VỤ CHƯA HOÀN THÀNH, ĐANG TRIỂN KHAI THỰC HIỆN (CHUYỂN SANG THÁNG SAU): Không', dam=True)
    o(ws, f'M{r + 2}', 'LÃNH ĐẠO ĐƠN VỊ', dam=True, can=GIUA, vien=False)
    os.makedirs(os.path.dirname(tep), exist_ok=True); wb.save(tep)


def tep_qlvb(tep):
    wb = Workbook(); ws = wb.active; ws.title = 'Van ban'
    ws.merge_cells('A1:J1')
    o(ws, 'A1', f'DANH MỤC VĂN BẢN TRÊN HỆ THỐNG QUẢN LÝ VĂN BẢN VÀ ĐIỀU HÀNH — CƠ QUAN A (từ 01/01/2026 đến 10/10/2026) — {NHAN}',
      dam=True, can=GIUA, vien=False)
    cot = ['STT trên hệ thống', 'Số ký hiệu', 'Loại văn bản', 'Trích yếu', 'Cơ quan ban hành', 'Ngày ban hành', 'Người soạn thảo',
           'Vai trò xử lý', 'Độ mật', 'Ghi chú']
    for j, (c, w) in enumerate(zip(cot, [9, 16, 14, 70, 26, 14, 34, 18, 10, 14]), 1):
        ch = get_column_letter(j); o(ws, f'{ch}3', c, dam=True, can=GIUA); ws.column_dimensions[ch].width = w
    for i, (so, loai, ty, ngay, cq, ng, vt) in enumerate(D2, 1):
        d = dt.datetime.strptime(ngay, '%d/%m/%Y')
        for j, v in enumerate([i, so, loai, ty, cq, d, ng, vt, 'Thường', ''], 1):
            c = o(ws, f'{get_column_letter(j)}{3 + i}', v, can=TRAI if j in (4, 5, 7) else GIUA)
            if j == 6:
                c.number_format = 'DD/MM/YYYY'
    ws.page_setup.orientation, ws.page_setup.paperSize = 'landscape', 9
    ws.oddFooter.center.text = NHAN
    os.makedirs(os.path.dirname(tep), exist_ok=True); wb.save(tep)


# ================================================================= tiện ích Word
def tai_lieu(le_trai=3.0):
    d = docx.Document()
    s = d.sections[0]
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.top_margin, s.bottom_margin, s.left_margin, s.right_margin = Cm(2), Cm(2), Cm(le_trai), Cm(2)
    st = d.styles['Normal']; st.font.name = 'Times New Roman'; st.font.size = Pt(14)
    st.element.rPr.rFonts.set(docx.oxml.ns.qn('w:eastAsia'), 'Times New Roman')
    hp = s.header.paragraphs[0]; hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    rr = hp.add_run(NHAN); rr.italic = True; rr.font.size = Pt(10)
    return d


def doan(d, chu, dam=False, nghieng=False, can='deu', co=14, thut=True, sau=6):
    p = d.add_paragraph()
    p.alignment = {'deu': WD_ALIGN_PARAGRAPH.JUSTIFY, 'giua': WD_ALIGN_PARAGRAPH.CENTER, 'trai': WD_ALIGN_PARAGRAPH.LEFT}[can]
    p.paragraph_format.space_after = Pt(sau); p.paragraph_format.space_before = Pt(0)
    if thut and can == 'deu':
        p.paragraph_format.first_line_indent = Cm(1.27)
    r = p.add_run(chu); r.bold, r.italic, r.font.size = dam, nghieng, Pt(co)
    return p


def ke(d):
    """Đường kẻ ngang dưới trích yếu (dài khoảng 1/3 dòng chữ)."""
    p = d.add_paragraph(); p.paragraph_format.left_indent = p.paragraph_format.right_indent = Cm(5.5)
    p.paragraph_format.space_after = Pt(12); p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = Pt(4)
    bdr = docx.oxml.OxmlElement('w:pBdr'); b = docx.oxml.OxmlElement('w:bottom')
    for k, v in (('val', 'single'), ('sz', '6'), ('space', '1'), ('color', '000000')):
        b.set(docx.oxml.ns.qn('w:' + k), v)
    bdr.append(b); p._p.get_or_add_pPr().append(bdr)


def o_bang(cell, dong, can=WD_ALIGN_PARAGRAPH.CENTER):
    cell.text = ''
    for i, (chu, dam, nghieng, co) in enumerate(dong):
        p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        p.alignment = can; p.paragraph_format.space_after = Pt(0)
        r = p.add_run(chu); r.bold, r.italic, r.font.size = dam, nghieng, Pt(co)


def rong(t, cm):
    t.autofit = False
    for row in t.rows:
        for c, w in zip(row.cells, cm):
            c.width = Cm(w)


def phan_dau(d, co_quan_tren, co_quan, so, dia_danh_ngay, quoc_hieu2='Độc lập - Tự do - Hạnh phúc'):
    t = d.add_table(rows=2, cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    rong(t, (5.4, 10.8))
    o_bang(t.cell(0, 0), [(co_quan_tren, False, False, 13), (co_quan, True, False, 13)] if co_quan_tren else [(co_quan, True, False, 13)])
    o_bang(t.cell(0, 1), [('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', True, False, 13), (quoc_hieu2, True, False, 14)])
    o_bang(t.cell(1, 0), [(so, False, False, 13)])
    o_bang(t.cell(1, 1), [(dia_danh_ngay, False, True, 14)])
    return t


def phan_ky(d, noi_nhan, quyen, chuc_vu, ten):
    t = d.add_table(rows=1, cols=2)
    rong(t, (7.0, 9.0))
    o_bang(t.cell(0, 0), [('Nơi nhận:', True, True, 12)] + [(x, False, False, 11) for x in noi_nhan], can=WD_ALIGN_PARAGRAPH.LEFT)
    o_bang(t.cell(0, 1), [(quyen, True, False, 14), (chuc_vu, True, False, 14), ('', False, False, 14), ('', False, False, 14),
                          ('', False, False, 14), (ten, True, False, 14)])


def bc_thang_8(tep):
    d = tai_lieu()
    phan_dau(d, '', CQ, 'Số: 284/BC-CQA', 'Quảng Ngãi, ngày 05 tháng 9 năm 2026')
    doan(d, '', sau=0)
    doan(d, 'BÁO CÁO', dam=True, can='giua', sau=0)
    doan(d, 'Kết quả công tác tháng 8, nhiệm vụ trọng tâm tháng 9 năm 2026', dam=True, can='giua', sau=0)
    ke(d)
    doan(d, 'Thực hiện Kế hoạch công tác năm 2026, Kế hoạch công tác quý III/2026, Cơ quan A báo cáo kết quả công tác tháng 8, '
            'nhiệm vụ trọng tâm tháng 9 năm 2026 như sau:')
    doan(d, 'I. KẾT QUẢ THỰC HIỆN NHIỆM VỤ THÁNG 8', dam=True)
    for td, nd in [
        ('1. Thực hiện mục tiêu phát triển kinh tế - xã hội và nhiệm vụ chính trị được giao',
         'Cơ quan hoàn thành 21/23 nhiệm vụ theo kế hoạch tháng, đạt 91,3%. Đã ban hành Báo cáo kết quả công tác tháng 7; thẩm định 16 hồ '
         'sơ chuyên môn theo đề nghị của cơ sở; hướng dẫn nghiệp vụ cho cơ sở bằng 03 công văn. Còn 02 nhiệm vụ chuyển sang tháng 9: '
         'Kiểm tra chuyên môn tại đơn vị cơ sở B; sửa đổi Quy chế văn thư, lưu trữ.'),
        ('2. Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát',
         'Hoàn thành rà soát 14 quy chế, quy định nội bộ; đề xuất sửa đổi 03 văn bản. Tham gia góp ý 04 dự thảo văn bản của cấp trên, đúng hạn.'),
        ('3. Thúc đẩy phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số',
         'Tỷ lệ văn bản đi được ký số đạt 96%; 100% văn bản đến được xử lý trên Hệ thống quản lý văn bản và điều hành. Triển khai Kế hoạch '
         'chữ ký số cho lãnh đạo phòng: Đã cấp 06/12 chứng thư số.'),
        ('4. Xây dựng Đảng và hệ thống chính trị trong sạch, vững mạnh',
         'Tổ chức sinh hoạt chi bộ định kỳ; công khai tài chính, tài sản theo quy định; không phát sinh đơn thư tố cáo.'),
        ('5. Phát triển văn hóa, con người, bảo đảm an sinh xã hội',
         'Chi trả đầy đủ, kịp thời chế độ, chính sách cho cán bộ, người lao động; thăm hỏi 02 trường hợp ốm đau.'),
        ('6. Củng cố quốc phòng, an ninh, giữ vững ổn định chính trị - xã hội',
         'Giải quyết 06/06 đơn thư, phản ánh, kiến nghị; bảo đảm an ninh, trật tự, an toàn phòng cháy, chữa cháy tại trụ sở.')]:
        doan(d, td, dam=True); doan(d, nd)
    doan(d, 'II. TỒN TẠI, HẠN CHẾ', dam=True)
    doan(d, 'Một số đơn vị gửi báo cáo tháng chậm so với thời hạn; 02 nhiệm vụ chưa hoàn thành trong tháng phải chuyển sang tháng 9.')
    doan(d, 'III. NHIỆM VỤ TRỌNG TÂM THÁNG 9', dam=True)
    doan(d, 'Tổng hợp báo cáo kết quả công tác quý III; ban hành Quy chế văn thư, lưu trữ (sửa đổi); tổ chức 02 lớp bồi dưỡng kỹ năng soạn '
            'thảo văn bản; hoàn thành kiểm tra chuyên môn tại đơn vị cơ sở B; triển khai chữ ký số cho 100% lãnh đạo phòng; đánh giá mức độ '
            'chuyển đổi số quý III.')
    doan(d, 'Trên đây là Báo cáo kết quả công tác tháng 8, nhiệm vụ trọng tâm tháng 9 năm 2026 của Cơ quan A./.')
    phan_ky(d, ['- Cơ quan cấp trên (báo cáo);', '- Lãnh đạo cơ quan;', '- Các đơn vị trực thuộc;', '- Lưu: VT, VP.'],
            'THỦ TRƯỞNG CƠ QUAN', '', 'Nguyễn Văn A')
    os.makedirs(os.path.dirname(tep), exist_ok=True); d.save(tep)


def d4_cong_van(tep):
    """Công văn — 05 lỗi cài sẵn (1–5 trong DAP-AN.md)."""
    d = tai_lieu(le_trai=2.0)                                                        # lỗi 1: lề trái 2 cm
    phan_dau(d, 'CƠ QUAN CẤP TRÊN', CQ, 'Số:      /CQA-VP', 'Quảng Ngãi, ngày      tháng 10 năm 2026',
             quoc_hieu2='Độc lập - Tự do - Hạnh Phúc')                               # lỗi 3: viết hoa sai quốc hiệu
    doan(d, 'V/v đôn đốc gửi báo cáo kết quả thực hành tiết kiệm, chống lãng phí năm 2026', can='trai', co=12, thut=False)
    doan(d, 'Kính gửi: Các đơn vị trực thuộc Cơ quan A.', can='giua', sau=12)
    for x in [
        'Thực hiện Công văn số 1482/CQCT-VP ngày 22/9/2026 của Cơ quan cấp trên về việc báo cáo kết quả thực hành tiết kiệm, chống lãng '
        'phí năm 2026; căn cứ Nghị định số 30/2020/NĐ-CP ngày 05/3/2021 của Chính phủ về công tác văn thư, Cơ quan A đề nghị các đơn vị '
        'trực thuộc thực hiện các nội dung sau:',                                    # lỗi 4: sai ngày ban hành (đúng: 05/3/2020)
        '1. Rà soát, báo cáo kết quả thực hành tiết kiệm, chống lãng phí năm 2026 của đơn vị theo đề cương gửi kèm; số liệu tính từ ngày '
        '01/01/2026 đến ngày 31/10/2026.',
        '2. Báo cáo gửi về Văn phòng trước ngày 20/10/2026 để tổng hợp, đồng thời gửi tệp điện tử qua Hệ thống quản lý văn bản và điều hành.',
        '3. Giao Văn phòng chủ trì, phối hợp với Phòng Kế hoạch - Tài chính tổng hợp, tham mưu Thủ trưởng cơ quan báo cáo Cơ quan cấp trên '
        'đúng thời hạn.',
        'Đề nghị các đơn vị nghiêm túc thực hiện, gửi báo cáo chậm nhất ngày 25/10/2026./.']:  # lỗi 5: hai thời hạn mâu thuẫn (20/10 và 25/10)
        doan(d, x, co=12)                                                            # lỗi 2: cỡ chữ nội dung 12
    phan_ky(d, ['- Như trên;', '- Thủ trưởng cơ quan (báo cáo);', '- Lưu: VT, VP.'], 'KT. THỦ TRƯỞNG CƠ QUAN', 'PHÓ THỦ TRƯỞNG', 'Trần Văn B')
    os.makedirs(os.path.dirname(tep), exist_ok=True); d.save(tep)


def d4_ke_hoach(tep):
    """Kế hoạch chuyên đề — 05 lỗi cài sẵn (6–10 trong DAP-AN.md)."""
    d = tai_lieu()
    phan_dau(d, 'CƠ QUAN CẤP TRÊN', CQ, 'Số:      /KH-CQA', 'Quảng Ngãi, ngày      tháng 10 năm 2026')
    doan(d, '', sau=0)
    doan(d, 'KẾ HOẠCH', dam=True, can='giua', sau=0)
    doan(d, 'Tập huấn sử dụng trí tuệ nhân tạo trong công tác văn phòng quý IV năm 2026', dam=True, can='giua', sau=0)
    ke(d)
    doan(d, 'Căn cứ Nghị định số 110/2004/NĐ-CP ngày 08 tháng 4 năm 2004 của Chính phủ về công tác văn thư;', nghieng=True)  # lỗi 6: hết hiệu lực
    doan(d, 'Căn cứ Kế hoạch số 102/KH-CQCT ngày 25 tháng 9 năm 2026 của Cơ quan cấp trên về tập huấn sử dụng trí tuệ nhân tạo cho cán '
            'bộ, công chức quý IV/2026;', nghieng=True)
    doan(d, 'Căn cứ Mẫu kế hoạch số 05 trong bộ biểu mẫu nội bộ của Văn phòng;', nghieng=True)                                   # lỗi 7: mẫu nội bộ làm căn cứ
    doan(d, 'Cơ quan A ban hành Kế hoạch tập huấn sử dụng trí tuệ nhân tạo trong công tác văn phòng quý IV năm 2026 như sau:')
    doan(d, 'I. MỤC ĐÍCH, YÊU CẦU', dam=True)
    doan(d, '1. Mục đích: Trang bị kỹ năng sử dụng công cụ trí tuệ nhân tạo trong tổng hợp, soạn thảo, rà soát văn bản cho cán bộ, công '
            'chức của cơ quan.')
    doan(d, '2. Yêu cầu: bảo đảm an toàn thông tin; không đưa tài liệu thuộc bí mật nhà nước vào công cụ; tổ chức thiết thực, tiết kiệm.')  # lỗi 10a: viết thường sau dấu hai chấm
    doan(d, 'II. NỘI DUNG, THỜI GIAN', dam=True)
    doan(d, '1. Đối tượng: 60 cán bộ, công chức của 06 đơn vị trực thuộc, chia 02 lớp.')
    doan(d, '2. Thời gian: Lớp 1 từ ngày 01/12/2026 đến ngày 03/12/2026; lớp 2 từ ngày 04/12/2026 đến ngày 05/12/2026.')
    doan(d, '3. Tổng kết, báo cáo kết quả tập huấn về Cơ quan cấp trên trước ngày 30/11/2026.')                                 # lỗi 9: tổng kết trước khi tập huấn
    doan(d, 'III. KINH PHÍ', dam=True)
    doan(d, 'Kinh phí thực hiện từ nguồn chi thường xuyên năm 2026, dự kiến như sau:')
    t = d.add_table(rows=5, cols=3); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    rong(t, (1.5, 9.5, 5.0))
    for i, (a, b, c) in enumerate([('TT', 'Nội dung chi', 'Số tiền (triệu đồng)'), ('1', 'Thuê giảng viên, báo cáo viên', '45'),
                                   ('2', 'Tài liệu, văn phòng phẩm', '30'), ('3', 'Giải khát giữa giờ, phục vụ', '18'),
                                   ('', 'Tổng cộng', '98')]):                        # lỗi 8: 45 + 30 + 18 = 93, không phải 98
        for j, v in enumerate((a, b, c)):
            o_bang(t.cell(i, j), [(v, i in (0, 4), False, 13)])
    doan(d, '', sau=0)
    doan(d, 'IV. TỔ CHỨC THỰC HIỆN', dam=True)
    doan(d, '1. Phòng Thông tin - Chuyển đổi số chủ trì xây dựng nội dung, tài liệu; phối hợp Văn phòng tổ chức lớp.')
    doan(d, '2. Phòng Tài chính - Kế hoạch bố trí kinh phí, hướng dẫn thanh, quyết toán theo quy định.')                       # lỗi 10b: sai tên đơn vị
    doan(d, '3. Các đơn vị trực thuộc cử cán bộ, công chức tham gia đầy đủ, đúng thành phần.')
    doan(d, 'Trên đây là Kế hoạch tập huấn sử dụng trí tuệ nhân tạo trong công tác văn phòng quý IV năm 2026 của Cơ quan A./.')
    phan_ky(d, ['- Cơ quan cấp trên (báo cáo);', '- Lãnh đạo cơ quan;', '- Các đơn vị trực thuộc;', '- Lưu: VT, VP.'],
            'THỦ TRƯỞNG CƠ QUAN', '', 'Nguyễn Văn A')
    os.makedirs(os.path.dirname(tep), exist_ok=True); d.save(tep)


DAP_AN = f"""# ĐÁP ÁN bộ dữ liệu giả định D1–D4 — KHÔNG đưa tệp này vào công cụ khi trình diễn

Dùng để người trình bày đối chiếu công cụ phát hiện được bao nhiêu. Mọi tên cơ quan, người, số ký hiệu là giả định.

## D1 — Dự thảo kế hoạch công tác quý IV/2026 của 06 đơn vị (60 nhiệm vụ)

| Loại cài sẵn | Chi tiết |
|---|---|
| 01 đơn vị nộp nhầm mẫu | **Phòng Nghiệp vụ 2** nộp theo Phụ lục **Ib** (mẫu kế hoạch THÁNG, tiêu đề "công tác tháng 10 năm 2026") thay vì Phụ lục Ia (quý), trong khi nội dung trải cả quý |
| 02 nhiệm vụ trùng giữa hai đơn vị | (1) "Xây dựng Quy chế quản lý, sử dụng tài sản công": **Văn phòng** và **Phòng Kế hoạch - Tài chính** cùng đăng ký chủ trì. (2) Tập huấn trí tuệ nhân tạo (02 lớp, tháng 11): **Văn phòng** và **Phòng Thông tin - Chuyển đổi số** cùng đăng ký, câu chữ khác nhau |
| 05 nhiệm vụ thiếu thời hạn hoặc sản phẩm | Thiếu thời hạn (03): Văn phòng "Sửa đổi, bổ sung Quy chế làm việc"; Tổ chức cán bộ "Rà soát vị trí việc làm"; Kế hoạch - Tài chính "Tự kiểm tra tài chính, kế toán". Thiếu sản phẩm (02): Văn phòng "Chăm lo Tết"; Kế hoạch - Tài chính "Hóa đơn điện tử" |
| 02 nhiệm vụ cấp trên đã giao (có trong D2) nhưng không đơn vị nào đăng ký | (1) Công văn số 1482/CQCT-VP ngày 22/9/2026: Báo cáo kết quả thực hành tiết kiệm, chống lãng phí năm 2026, trước 15/11/2026. (2) Kế hoạch số 96/KH-CQCT ngày 15/9/2026: Tổng rà soát, sắp xếp trụ sở làm việc, báo cáo trước 30/11/2026 |

Lưu ý thêm (không cài, nhưng công cụ có thể nêu): Công văn số 1260/CQCT-TC yêu cầu báo cáo rà soát vị trí việc làm trước 30/11/2026 — nhiệm vụ này Phòng Tổ chức cán bộ có đăng ký nhưng để trống thời hạn.

## D2 — Tệp xuất Hệ thống quản lý văn bản và điều hành ({len(D2)} văn bản, 15/01 – 08/10/2026)

Không cài lỗi. Dùng để: (a) liệt kê văn bản chỉ đạo, kế hoạch năm, quý, thông báo kết luận, kế hoạch chuyên đề; (b) tìm nhiệm vụ còn thiếu của D1; (c) gợi ý minh chứng cho D3.

## D3 — Kế hoạch tháng 9/2026 của cơ quan (24 nhiệm vụ), báo cáo tháng 9 của 06 đơn vị, báo cáo tháng 8 của cơ quan

| Loại cài sẵn | Chi tiết |
|---|---|
| 01 số liệu không thống nhất | 02 lớp bồi dưỡng kỹ năng soạn thảo văn bản: **Phòng Tổ chức cán bộ** ghi 112 lượt người, **Văn phòng** ghi 120 lượt người |
| 01 nội dung trùng lặp | "Ban hành Kế hoạch bảo đảm an toàn thông tin tháng cao điểm" (Kế hoạch số 305/KH-CQA): **Văn phòng** và **Phòng Thông tin - Chuyển đổi số** cùng báo cáo là kết quả của mình (kế hoạch tháng giao Phòng Thông tin - Chuyển đổi số chủ trì) |
| 03 nhiệm vụ có trong kế hoạch tháng 9 nhưng không thấy trong báo cáo | (1) Văn phòng: "Ban hành Quy chế văn thư, lưu trữ (sửa đổi)" — **đã có Quyết định số 215/QĐ-CQA ngày 24/9/2026 trong D2**, tức là đã làm nhưng quên báo cáo. (2) Phòng Nghiệp vụ 1: "Kiểm tra chuyên môn tại đơn vị cơ sở B" — không có thông tin (tháng 8 đã chuyển sang). (3) Phòng Thông tin - Chuyển đổi số: "Đánh giá mức độ chuyển đổi số quý III/2026" — không có thông tin |

Lưu ý thêm: Phòng Tổ chức cán bộ báo cáo "Trình ban hành Kế hoạch tuyển dụng" là đã trình, chưa ban hành (tỷ lệ chất lượng, tiến độ 75%); Phòng Nghiệp vụ 1 thẩm định 12/14 hồ sơ; chữ ký số 10/12.

## D4 — Tệp chính: Dự thảo Chương trình công tác tháng 10/2026 (văn bản Đảng, đã ẩn danh)

Tệp `Du-thao_Chuong-trinh-cong-tac-thang-10-2026_van-ban-Dang_an-danh.docx` ẩn danh từ một dự thảo thật: Tên tỉnh đổi thành "tỉnh A",
tên người ký thành "Nguyễn Văn A", số ký hiệu văn bản của địa phương đã đổi (giữ nguyên kiểu ký hiệu), thuộc tính tệp đã thay; định dạng
giữ nguyên từng thông số. Số ký hiệu văn bản của Trung ương giữ nguyên. **Không cài thêm lỗi** — mọi phát hiện là của chính dự thảo.

Kết quả chạy trước (Hệ KTC-Ra-Soat-897 v2.25, hệ quy chiếu B — văn bản Đảng, ngày 11/10/2026, đã ẩn danh tương ứng):
`../Ket-qua-chay-truoc/BaoCao_RaSoat-897-v2.25_Chuong-trinh-cong-tac-thang-10-2026_van-ban-Dang_an-danh.docx` — **26 phát hiện: 0 Mức 1,
06 Mức 2, 15 Mức 3, 05 Mức 4**; kết luận "Cần chỉnh sửa trước khi trình ký". Sáu phát hiện Mức 2 nên nêu khi trình diễn:
(1) Chương trình của Đảng ủy nhưng mang ký hiệu "/TU"; (2) số Kết luận bất thường so với chuỗi số của Đảng ủy; (3) Quy chế viện dẫn
thiếu tên, ngày, cơ quan ban hành; (4) câu Mục I.1 dài, nhiều chủ thể; (5) Mục II thiếu "Thời gian trình"; (6) căn cứ cuối kết thúc
bằng dấu chấm phẩy. Đã đo lại trên bản ẩn danh ngày 12/10/2026: 08 phát hiện thể thức đều khớp (lề 20/20/30/15 mm; tên loại cỡ 14;
thụt đầu dòng 12,5 - 12,7 - 10,39 mm; số trang cách mép 12,7 mm; ký tự thừa sau dòng "Lưu"; mục Nơi nhận bị ngắt đoạn; kiểu Heading 1 ở
"T/M BAN THƯỜNG VỤ"; dấu chấm phẩy ở căn cứ cuối).

Lưu ý khi trình diễn: Hệ rà soát áp Hướng dẫn về thể thức văn bản của Đảng, **không áp Nghị định số 30/2020/NĐ-CP** và không áp quy ước
riêng của Trường cho văn bản này; các viện dẫn văn bản của địa phương được ghi "chưa xác minh" vì không có trong kho của Trường.

## D4 — Dự phòng: Hai dự thảo văn bản hành chính cài 10 lỗi

**Dự thảo Công văn đôn đốc (05 lỗi)**

| TT | Lỗi | Vị trí | Mức gợi ý |
|---|---|---|---|
| 1 | Lề trái 2 cm (quy định 3 – 3,5 cm) | Toàn văn bản | Mức 2 |
| 2 | Cỡ chữ nội dung 12 (quy định 13 – 14) | Phần nội dung | Mức 2 |
| 3 | Tiêu ngữ viết "Hạnh Phúc" (đúng: "Hạnh phúc") | Phần đầu | Mức 3 |
| 4 | Nghị định số 30/2020/NĐ-CP ghi ngày 05/3/2021 (đúng: 05/3/2020) | Đoạn mở đầu | Mức 1 |
| 5 | Hai thời hạn mâu thuẫn: "trước ngày 20/10/2026" và "chậm nhất ngày 25/10/2026" | Mục 2 và câu kết | Mức 1 |

**Dự thảo Kế hoạch tập huấn (05 lỗi)**

| TT | Lỗi | Vị trí | Mức gợi ý |
|---|---|---|---|
| 6 | Căn cứ Nghị định số 110/2004/NĐ-CP đã hết hiệu lực (được thay bằng Nghị định số 30/2020/NĐ-CP) | Căn cứ 1 | Mức 1 |
| 7 | Lấy "Mẫu kế hoạch số 05" nội bộ làm căn cứ | Căn cứ 3 | Mức 1 |
| 8 | Bảng kinh phí cộng sai: 45 + 30 + 18 = 93, ghi 98 | Mục III | Mức 1 |
| 9 | Thời gian không hợp lý: Tổng kết trước 30/11/2026 trong khi tập huấn 01 – 05/12/2026 | Mục II | Mức 1 |
| 10 | Tên đơn vị không thống nhất ("Phòng Tài chính - Kế hoạch", đúng: "Phòng Kế hoạch - Tài chính"); viết thường sau dấu hai chấm ("Yêu cầu: bảo đảm") | Mục IV; Mục I | Mức 3 |

Lưu ý thêm (không cài): Kế hoạch dùng nguồn chi thường xuyên năm 2026 cho lớp tổ chức tháng 12; lớp 2 chỉ 02 ngày trong khi lớp 1 là 03 ngày — công cụ có thể nêu ở Mức 4.

Ngoài 10 lỗi cài sẵn, hai dự thảo được dựng giản lược (không đánh số trang, không có đường kẻ dưới tên cơ quan và Quốc hiệu, tên cơ quan là giả định) nên công cụ có thể nêu thêm các gợi ý thể thức — đó là phát hiện đúng, không phải báo sai. Khi trình diễn, đối chiếu theo 10 lỗi trong bảng.
"""

README = f"""# Bộ dữ liệu giả định phục vụ trình diễn ngày 17/10/2026

**{NHAN}.** Cơ quan A và 06 đơn vị (Văn phòng; Phòng Tổ chức cán bộ; Phòng Kế hoạch - Tài chính; Phòng Nghiệp vụ 1; Phòng Nghiệp vụ 2;
Phòng Thông tin - Chuyển đổi số) là giả định; mọi tên người, số ký hiệu, số liệu không có thật.

| Thư mục | Nội dung | Dùng ở phần |
|---|---|---|
| `D1-Ke-hoach-quy-IV-2026/` | 06 tệp dự thảo kế hoạch quý IV/2026 của các đơn vị (khuôn Phụ lục Ia) | Phần 1 |
| `D2-He-thong-QLVB/` | 01 tệp xuất danh mục văn bản từ Hệ thống quản lý văn bản và điều hành | Phần 1, Phần 2 |
| `D3-Bao-cao-thang-9-2026/` | Kế hoạch tháng 9 của cơ quan; 06 báo cáo tháng 9 của đơn vị (khuôn Phụ lục IIb); báo cáo tháng 8 của cơ quan | Phần 2 |
| `D4-Du-thao-can-ra-soat/` | **Tệp chính của Phần 3:** 01 dự thảo Chương trình công tác tháng 10/2026 của Ban Thường vụ Đảng ủy (văn bản Đảng, hệ quy chiếu B, đã ẩn danh từ một dự thảo thật). Dự phòng: 01 dự thảo công văn, 01 dự thảo kế hoạch chuyên đề (văn bản hành chính, cài 10 lỗi) | Phần 3 |
| `_Dap-an-KHONG-dua-vao-cong-cu/` | Danh sách chi tiết cài sẵn — chỉ người trình bày xem | — |

Cột Ghi chú giữ giá trị chuẩn của khuôn mẫu (“Đưa vào KH Trường” = đưa vào kế hoạch của cơ quan) để công cụ lọc đúng.

Sinh lại: `python tao_du_lieu_gia_dinh.py` (tệp cạnh thư mục này).
"""


def main():
    d1 = os.path.join(GOC, 'D1-Ke-hoach-quy-IV-2026')
    for ma, hang in D1.items():
        ten = DV[ma][0]
        h = [(t, nd, ma, sp, sl, dk, tg, gc) for t, nd, sp, sl, dk, tg, gc in hang]
        if ma == 'N2':   # nộp nhầm mẫu: Phụ lục Ib (kế hoạch tháng)
            ke_hoach(os.path.join(d1, f'{ma}_Ke-hoach-quy-IV-2026_du-thao.xlsx'), 'Phụ lục Ib', ten,
                     'KẾ HOẠCH\ncông tác tháng 10 năm 2026', 'Các nhiệm vụ theo kế hoạch (chương trình) công tác đã đề ra từ đầu tháng', h)
        else:
            ke_hoach(os.path.join(d1, f'{ma}_Ke-hoach-quy-IV-2026_du-thao.xlsx'), 'Phụ lục Ia', ten,
                     'KẾ HOẠCH\ncông tác Quý IV năm 2026', 'Các nhiệm vụ theo kế hoạch (chương trình) công tác đã đề ra từ đầu năm', h)
    tep_qlvb(os.path.join(GOC, 'D2-He-thong-QLVB', 'Danh-muc-van-ban-QLVB_Co-quan-A_01.01-10.10.2026.xlsx'))
    d3 = os.path.join(GOC, 'D3-Bao-cao-thang-9-2026')
    ke_hoach(os.path.join(d3, '00_Ke-hoach-thang-9-2026_Co-quan-A.xlsx'), 'Phụ lục Ib', 'Toàn cơ quan (Kế hoạch số 270/KH-CQA ngày 28/8/2026)',
             'KẾ HOẠCH\ncông tác tháng 9 năm 2026', 'Các nhiệm vụ theo kế hoạch (chương trình) công tác đã đề ra từ đầu tháng',
             [(t, nd, dv, sp, sl, dk, tg, DUA) for t, nd, dv, sp, sl, dk, tg in KH9])
    for ma, hang in D3.items():
        ket_qua(os.path.join(d3, f'{ma}_Bao-cao-thang-9-2026.xlsx'), DV[ma][0], ma, hang)
    bc_thang_8(os.path.join(d3, '00_Bao-cao-thang-8-2026_Co-quan-A_da-ban-hanh.docx'))
    d4 = os.path.join(GOC, 'D4-Du-thao-can-ra-soat')
    d4_cong_van(os.path.join(d4, 'Du-thao_Cong-van-don-doc-bao-cao-tiet-kiem.docx'))
    d4_ke_hoach(os.path.join(d4, 'Du-thao_Ke-hoach-tap-huan-tri-tue-nhan-tao.docx'))
    da = os.path.join(GOC, '_Dap-an-KHONG-dua-vao-cong-cu'); os.makedirs(da, exist_ok=True)
    open(os.path.join(da, 'DAP-AN.md'), 'w', encoding='utf-8', newline='\n').write(DAP_AN)
    open(os.path.join(GOC, '00-README.md'), 'w', encoding='utf-8', newline='\n').write(README)
    # Excel mở, tính lại công thức và lưu — để tệp có giá trị tính sẵn như tệp đơn vị nộp thật
    subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
                    os.path.join(os.path.dirname(GOC), 'tinh_lai_cong_thuc.ps1'), '-ThuMuc', GOC], check=True, stdout=subprocess.DEVNULL)
    n = sum(len(f) for _, _, f in os.walk(GOC))
    print(f'Đã sinh {n} tệp tại {GOC}; D1 {sum(len(v) for v in D1.values())} nhiệm vụ; D2 {len(D2)} văn bản; '
          f'KH tháng 9: {len(KH9)}; báo cáo đơn vị: {sum(len(v) for v in D3.values())} dòng')


if __name__ == '__main__':
    main()
