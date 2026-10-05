# N01 — TÌNH TRẠNG ĐẾN NGÀY 05/10/2026, DANH MỤC LỖI ĐÃ BIẾT

Đơn vị soạn thảo: Phòng TH-HC&QT. Nội dung dưới đây là **tự khai** của đơn vị soạn thảo; bên thẩm định đối chiếu với nguồn gốc.

## 1. Thay đổi sau ngày 29/9/2026

| Ngày | Nội dung | Ảnh hưởng tới đối tượng thẩm định |
|---|---|---|
| 29/9 | Rà soát toàn văn hồ sơ theo bộ quy tắc KTC-Ra-Soat-897 (N08): 0 vấn đề Mức 1; 03 Mức 2, 11 Mức 3 đã sửa bằng Track Changes; sửa theo quy ước riêng của Trường (viện dẫn lần sau, viết hoa sau dấu hai chấm: 132 vị trí) | Văn bản N04 đến N07 là bản sau khi sửa |
| 30/9 | Hiệu trưởng ban hành Quyết định số 2164/QĐ-CĐKT ngày 30/9/2026 về Bộ chỉ số KPI đối với tập thể, cá nhân (55 phụ lục, 1.972 chỉ số; không có trọng số, chỉ tiêu — xác định khi ký Bản cam kết, tổng trọng số mỗi bộ bằng 100%) | Plugin 1.3.13 **chưa** gợi ý chỉ số theo Quyết định này (xem mục 4, lỗi K-06) |
| 30/9 - 04/10 | Mã nguồn: 03 tệp tham chiếu bổ sung một dòng dẫn Quyết định số 2164/QĐ-CĐKT; **chưa đóng gói** | Tệp phát hành 1.3.13 **không đổi** (SHA-256 như N10) |
| 03/10 | Phòng QLKHCN&HTPT trình kết quả thẩm định (N02) | — |
| 04/10 | Lãnh đạo Phòng QLKHCN&HTPT, Hiệu trưởng cho ý kiến (N02) | Căn cứ tổ chức lần thẩm định này |

Không thay đổi chức năng plugin từ ngày 29/9/2026 (đóng băng chức năng trong thí điểm, N04 mục 7).

## 2. Trạng thái 04 cổng quyết định (N04 mục 9)

| Cổng | Mốc dự kiến tại N04 | Trạng thái ngày 05/10/2026 |
|---|---|---|
| G0 — Kỹ thuật | 29/9 | Đạt có ghi chú (N11, N12, N15) |
| G1 — Dữ liệu: Biên bản phân quyền chỉ đọc kho KTC-Database | 02/10 | **Chưa thực hiện** — quá mốc; mốc mới đề xuất tại N19 |
| Kiểm kê, thu hồi phiên bản cũ cấp tổ chức (Phòng QLKHCN&HTPT) | 03/10 | **Chưa thực hiện** — quá mốc; mốc mới đề xuất tại N19 |
| G2 — Môi trường: Nghiệm thu Claude 15 ca, Cowork 18 ca | 07/10 | **Chưa thực hiện**; phiếu sẵn (N16) |
| G3 — Thí điểm | Kỳ báo cáo tháng 10/2026 | Chưa bắt đầu; dự thảo Kế hoạch tại N19 |

## 3. Đối chiếu Phiếu trình (N02) với hồ sơ

Số liệu trong Phiếu trình khớp hồ sơ, trừ 02 chỗ diễn đạt (không đề nghị sửa văn bản đã có ý kiến của Lãnh đạo):

| Phiếu trình ghi | Hồ sơ |
|---|---|
| “Kiểm thử kích hoạt đúng 8/8 kỹ năng KPI trên Claude Code” | 8/8 **câu hỏi thử** kích hoạt đúng cho **02** kỹ năng KPI |
| “Haiku 4.5 nhận căn cứ không có nguồn làm căn cứ xử lý” | Haiku 4.5 nhận **checklist nội bộ** (“Checklist 07”) làm căn cứ khi có dự thảo, không cảnh báo lỗi Mức 1 (N04 mục 2.7, N15) |

## 4. Danh mục lỗi, giới hạn đã biết (không nêu lại tại Phần D)

| Mã | Nội dung | Xử lý |
|---|---|---|
| K-01 | Thao tác chặn ghi không nhận dạng 05/10 kịch bản ghi che giấu: Lệnh mã hóa base64 không lộ tên kho, mã Python mã hóa, biến đặt từ phiên trước, chương trình có sẵn trong tệp, liên kết tạo từ trước | Bảo vệ chính là phân quyền chỉ đọc (cổng G1); chặn lệnh giải mã base64 chuyển vào lần cập nhật sau thí điểm |
| K-02 | Thao tác chặn ghi chặn nhầm lệnh chỉ đọc khi thư mục làm việc nằm trong kho và chuỗi văn bản có ký tự “>” | Chặn về phía an toàn; sửa sau thí điểm |
| K-03 | Haiku 4.5 nhận checklist nội bộ làm căn cứ (2/2 lượt) | Không dùng Haiku 4.5 soạn văn bản, phần căn cứ |
| K-04 | Ca 13 (viện dẫn Luật) trượt 01/02 lượt do giám khảo AI chấm | Giữ nguyên kết quả, không sửa tiêu chí |
| K-05 | Công cụ đo thể thức và kỹ năng soạn thảo chưa kiểm, chưa tự viết hoa chữ đầu sau dấu hai chấm (quy ước riêng của Trường); ngày 29/9 phải sửa tay 132 vị trí | Sau thí điểm |
| K-06 | Kỹ năng lập KPI, tự đánh giá KPI chưa gợi ý chỉ số theo phụ lục Quyết định số 2164/QĐ-CĐKT đúng chức danh, chưa kiểm tổng trọng số 100% | Sau thí điểm; trong thí điểm người dùng tra phụ lục gốc |
| K-07 | Câu lệnh mẫu chưa có dòng ghi chú phạm vi văn bản hành chính, văn bản Đảng (GM-6) | Sau thí điểm |
| K-08 | Chưa nghiệm thu Claude (trò chuyện), Cowork; chưa có biên bản phân quyền; chưa kiểm kê cấp tổ chức | Tồn tại (2), (3) |
| K-09 | Quy ước nhân hệ số sản phẩm (Quyết định số 2119/QĐ-CĐKT) với hệ số mức độ công việc (Quyết định số 1923/QĐ-CĐKT) chưa có ý kiến của Phòng TCCB&CTHSSV | Tồn tại (5); dự thảo Phiếu xin ý kiến tại N29 |
| K-10 | Chưa có dữ liệu vận hành tại đơn vị khác ngoài Phòng TH-HC&QT | Thí điểm (N19) |
