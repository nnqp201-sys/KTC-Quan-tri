# N01 — TÌNH TRẠNG ĐẾN NGÀY 06/10/2026, DANH MỤC LỖI ĐÃ BIẾT

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

## 2. Trạng thái 05 tồn tại theo Phiếu trình (N02, điểm c Mục 4) — căn cứ duy nhất để đóng hồ sơ

Lộ trình 04 cổng G0 - G3 tại N04 mục 9 được thay bằng việc hoàn thành 05 tồn tại theo ý kiến của Phòng QLKHCN&HTPT.

| Tồn tại | Trạng thái ngày 06/10/2026 |
|---|---|
| (1) Thẩm định độc lập xác nhận khắc phục trên bản 1.3.13 | Đang thực hiện — chính là lần thẩm định này |
| (2) Kiểm thử trên Claude (trò chuyện), Claude Cowork | **Giải trình của đơn vị soạn thảo:** Người phụ trách xác nhận (06/10/2026) đã kiểm thử bản 1.3.13 trên tài khoản cá nhân và tài khoản của Phòng TH-HC&QT, cả hai nền tảng; không kiểm thử lại theo phiếu N16. Sản phẩm dùng thật trên Claude (trò chuyện) có lưu: Dự thảo Kế hoạch tham dự Hội nghị Báo cáo viên (19/9/2026), Đề án đào tạo sát hạch lái xe Hạng A dự thảo lần 3 có Track Changes (20/9/2026) — **hai sản phẩm này làm trên các bản trước 1.3.13**. Chưa có tệp kết quả lưu riêng cho lượt kiểm thử 1.3.13 |
| (3) Biên bản phân quyền chỉ đọc kho; kiểm kê, thu hồi bản cũ cấp tổ chức | **Giải trình:** Kho KTC-Database do người phụ trách (Phòng TH-HC&QT) trực tiếp quản lý, phân quyền — không lập biên bản riêng. Các bản cũ **chưa từng cài ở cấp tổ chức** (chỉ cài ở chế độ người dùng tự cài), nên không có bản cần thu hồi |
| (4) Thao tác chặn ghi chưa nhận dạng 5/10 kịch bản | Giữ là biện pháp hỗ trợ; bảo vệ chính là phân quyền chỉ đọc do người phụ trách quản lý (tồn tại (3)) |
| (5) Quy ước nhân hệ số sản phẩm × mức độ | **Đã đóng 06/10/2026**: Phòng TCCB&CTHSSV trả lời trên Phiếu xin ý kiến (N29): Chỉ theo hệ số sản phẩm Quyết định số 2119/QĐ-CĐKT, từ Quý IV/2026, không nhân hệ số mức độ; mẫu Phụ lục I, II Quyết định số 1923/QĐ-CĐKT giữ thang 4 mức; trọng số Bản cam kết chấp nhận cả 3 cách. Plugin 1.3.13 chưa đặt mặc định (đóng băng) — người dùng chọn phương án `A` |

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
| K-08 | Không lập biên bản phân quyền, không kiểm kê cấp tổ chức; kiểm thử Claude, Cowork trên 1.3.13 chưa có tệp kết quả lưu riêng | Giải trình tại mục 2, tồn tại (2), (3) |
| K-09 | Plugin chưa đặt phương án `A` làm mặc định theo ý kiến Phòng TCCB&CTHSSV ngày 06/10/2026 | Sau thí điểm (đóng băng) |
| K-10 | Chưa có dữ liệu vận hành tại đơn vị khác ngoài Phòng TH-HC&QT | Thí điểm (N19) |
