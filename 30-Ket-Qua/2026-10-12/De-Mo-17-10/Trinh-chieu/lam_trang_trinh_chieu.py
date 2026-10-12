# -*- coding: utf-8 -*-
"""Dựng bộ trang trình chiếu (PDF + PNG 1920x1080) cho phần trình bày 30 phút ngày 17/10/2026.
Dùng lại hàm vẽ trang của Video 1 để đồng bộ hình thức. Sửa nội dung trong danh sách TRANG rồi chạy lại: python lam_trang_trinh_chieu.py
Dòng bắt đầu bằng "#" là số liệu nổi bật, "!" là dòng nhấn mạnh."""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(D, '..', '..', '..', '2026-10-11', 'De-Mo-17-10', 'Video')))
import lam_video1 as V
from PIL import Image

TRANG = [
 ('Ứng dụng trí tuệ nhân tạo trong công tác tham mưu, tổng hợp',
  ['Phần 1.  Quản lý, theo dõi, đôn đốc nhiệm vụ: Tổng hợp kế hoạch công tác quý, tháng', 'Phần 2.  Tổng hợp số liệu, xây dựng báo cáo tháng, quý',
   'Phần 3.  Soạn thảo, rà soát văn bản bằng hệ KTC-Ra-Soat-897', '!Phòng Tổng hợp – Hành chính và Quản trị, Trường Cao đẳng Kon Tum  ·  17/10/2026']),
 ('Ba nguyên tắc sử dụng',
  ['Công cụ đọc, đối chiếu, dự thảo  —  người có thẩm quyền quyết định', 'Mọi kết quả truy được về văn bản nguồn, dữ liệu nguồn',
   'Không đưa tài liệu thuộc bí mật nhà nước vào công cụ', '!Nền móng trước, công cụ sau: Kho dữ liệu nền  →  Công cụ  →  Người kiểm tra  →  Ban hành']),
 ('Phần 1. Tổng hợp kế hoạch công tác quý từ dự thảo của các đơn vị',
  ['#06 đơn vị  ·  60 nhiệm vụ  ·  06 tệp bảng tính', '01 đơn vị nộp nhầm mẫu kế hoạch tháng  →  trả lại',
   '05 nhiệm vụ thiếu thời hạn hoặc sản phẩm; 01 cặp trùng rõ, 02 cặp nghi trùng', '02 nhiệm vụ cấp trên đã giao, có thời hạn, chưa đơn vị nào đăng ký',
   '!Công cụ không tự sửa nội dung của đơn vị; mỗi nhiệm vụ trong kế hoạch tổng hợp đều ghi nguồn']),
 ('Tra cứu Hệ thống quản lý văn bản và điều hành',
  ['Lấy danh mục văn bản chỉ đạo, kế hoạch năm, quý, thông báo kết luận, kế hoạch chuyên đề trong kỳ', 'Đối chiếu với dự thảo kế hoạch: Việc nào đã giao mà chưa ai nhận',
   'Gợi ý văn bản đã ban hành làm minh chứng cho báo cáo', '!Công cụ chỉ đọc trong phiên người dùng đã đăng nhập; không nhập mật khẩu, không bấm xử lý']),
 ('Phần 2. Xây dựng báo cáo tháng từ báo cáo của các đơn vị',
  ['#24 nhiệm vụ theo kế hoạch  ·  21 có báo cáo  ·  03 chưa có thông tin', '01 số liệu không thống nhất giữa hai đơn vị (112 và 120 lượt người)',
   '01 kết quả hai đơn vị cùng nhận  →  chỉ tính một lần', '01 nhiệm vụ “quên báo cáo”: Đã có quyết định ban hành trên Hệ thống',
   '!Công cụ ghi “chưa có thông tin”, không tự kết luận “chưa làm”; báo cáo phát triển từ báo cáo kỳ trước đã ban hành']),
 ('Phần 3. Rà soát văn bản của Đảng trước khi trình ký',
  ['Tự nhận ra văn bản của Đảng: Áp Hướng dẫn số 05-HD/VPTW, không áp Nghị định số 30/2020/NĐ-CP', 'Đo thể thức trên tệp thật: Cỡ chữ, lề, thụt đầu dòng, số trang',
   'Đối chiếu từng văn bản viện dẫn; ghi rõ phần chưa xác minh', '#25 phát hiện:  0 Mức 1  ·  07 Mức 2  ·  13 Mức 3  ·  05 Mức 4',
   '!Còn vấn đề Mức 1 thì không trình ký']),
 ('Hệ rà soát công khai cả giới hạn của mình',
  ['Kiểm thử định kỳ trên tệp cài sẵn 30 lỗi', '#24 lỗi phát hiện đúng  ·  02 sai mức  ·  04 bỏ sót',
   'Ngay trong buổi này: 01 cặp nhiệm vụ bị nghi trùng nhầm, 01 gợi ý minh chứng không đúng', '!Ô “Người kiểm tra” luôn là người thật; công cụ không tự phê duyệt']),
 ('Kinh nghiệm thực tế tại phòng',
  ['Thông báo kết luận được ráp ngay trong khi cuộc họp đang diễn ra', 'Một quyết định: Từ tra cứu đến khi ký khoảng 10 ngày; người có nghiệp vụ bắt được 02 lỗi căn cứ',
   'Sửa 132 vị trí trong 04 văn bản, có dấu vết để người duyệt xem từng chỗ', 'Đọc 40 tệp của 13 đơn vị, hơn 300 nhiệm vụ, chỉ ra tệp nộp nhầm mẫu',
   '!Phát hiện đề án dùng sai điều kiện nhờ đối chiếu văn bản gốc trong kho']),
 ('Đề xuất để bắt đầu',
  ['Lập kho dữ liệu nền trước: Văn bản chỉ đạo còn hiệu lực, quy chế, chương trình công tác, văn bản tốt, mẫu văn bản của Đảng',
   'Chọn 01 – 02 việc lặp lại hằng tháng để làm trước: Tổng hợp kế hoạch, báo cáo; rà soát thể thức', 'Quy định rõ loại dữ liệu không đưa vào công cụ; ai là người kiểm tra',
   '!Trường Cao đẳng Kon Tum sẵn sàng chia sẻ bộ quy tắc rà soát văn bản của Đảng và cách tổ chức kho']),
 ('Trân trọng cảm ơn', ['Phần thảo luận: Đoàn công tác có thể đề nghị chạy trực tiếp 01 thao tác', '!Dữ liệu trình diễn là dữ liệu giả định; văn bản rà soát đã ẩn danh']),
]

V.CANH = TRANG      # để đánh số trang i/n
ra = os.path.join(D, 'trang'); os.makedirs(ra, exist_ok=True)
anh = []
for i, (td, dong) in enumerate(TRANG, 1):
    p = os.path.join(ra, f'trang-{i:02d}.png'); V.ve(i, td, dong, p); anh.append(Image.open(p).convert('RGB'))
pdf = os.path.join(D, 'Trinh-chieu_Ung-dung-AI-tham-muu-tong-hop_17.10.2026_v1.pdf')
anh[0].save(pdf, save_all=True, append_images=anh[1:], resolution=150)
print(len(anh), 'trang ->', pdf)
