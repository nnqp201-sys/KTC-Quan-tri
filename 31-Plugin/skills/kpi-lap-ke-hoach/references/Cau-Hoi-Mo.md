# Câu hỏi mở — skill phải DỪNG HỎI khi gặp

Quy tắc chưa có căn cứ văn bản hoặc văn bản mâu thuẫn nhau. Không tự giả định, không chọn thay người có thẩm quyền.
Người cần xác nhận: **Phòng TCCB&CTHSSV** (đơn vị chủ trì KPI, quản lý phần mềm — QĐ 1923 Đ25.1) và **Phòng TH-HC&QT**.

Cập nhật: 24/9/2026. Đóng câu hỏi nào thì ghi ngày, văn bản trả lời, người xác nhận — không xóa dòng.

| # | Câu hỏi | Gặp ở đâu | Hành vi khi chưa có trả lời |
|---|---|---|---|
| 1 | **Hệ số quy đổi đầu việc tính theo cách nào?** Có văn bản: 4 mức độ 1,0/1,2/1,5/2,0 [QĐ 1923, Phụ lục II]. Dự thảo: hệ số sản phẩm theo Danh mục TB 1052. Chưa có văn bản: A × B (quy ước Phòng TH-HC&QT ghi nhận 24/9/2026). Chưa biết phần mềm KPI tính cách nào. Liên quan KI-014 | Lập kế hoạch, bước 3 | `kpi_calc.py --phuong-an {muc-do, A, AxB, nhap-tay}` — **không có mặc định**. Hỏi người dùng; mọi đầu ra ghi phương án và trạng thái |
| 2 | Danh mục TB 1052 là **dự thảo** (hạn góp ý 20/9/2026, chưa ban hành); 204/371 dòng hệ số lệch giá trị chuẩn của Nhóm; dòng 29.22 hệ số 50. Sản phẩm không có trong Danh mục xử lý thế nào? | Phương án `A`, `AxB` | In cảnh báo "hệ số dự thảo" và dòng lệch. Sản phẩm không khớp chính xác → dừng hỏi, không tự gán A |
| 3 | Trọng số từng chỉ tiêu (trong 70 điểm) có tính theo tỷ lệ số lượng quy đổi không? Mẫu Quý III đặt sẵn điểm tối đa theo **Trục**; trong một Trục, các đầu việc cộng theo số lượng quy đổi. Phụ lục kèm Bản cam kết yêu cầu "tổng trọng số 100%" nhưng **không có cột trọng số** | Lập kế hoạch khi người dùng dùng mẫu Phụ lục Bản cam kết | Dùng điểm tối đa theo Trục của mẫu nhóm vị trí; không tự đặt trọng số từng chỉ tiêu. Người dùng muốn trọng số riêng → nhập tay, ghi rõ |
| 4 | **Hai mốc đầu quý:** chỉ tiêu KPI cá nhân trình Trưởng đơn vị trong 05 ngày làm việc đầu quý [Đ13.1]; kế hoạch công tác theo mẫu PL I, PL II gửi Phòng TCCB&CTHSSV trước ngày 05 tháng đầu quý [Đ15.3a]. Có phải hai sản phẩm, hai hạn? Với Quý IV/2026 hai mốc là 07/10 và trước 05/10 | Lập kế hoạch, bước 1 | Nêu cả hai mốc từ tệp quý. Quý có văn bản hướng dẫn riêng thì theo văn bản đó (Quý III: CV 694 — cùng 27/9/2026) |
| 5 | Hướng dẫn Quý IV/2026 chưa có | Tệp `quy/2026-Q4.yaml` | Dùng mốc chuẩn của Quy chế; báo "chưa có hướng dẫn quý" |
| 6 | QĐ 2078/QĐ-CĐKT (văn bản chính) và Phụ lục XXIV, XXVI–XXVIII; PL I của CV 694; Bảng kiểm sĩ số; Tiêu chí chuyển đổi số | Giai đoạn 2 (tự đánh giá), 3 (tổng hợp) | Giai đoạn 1 không dùng. Người dùng hỏi tự đánh giá → báo chưa có mẫu, dừng |
| 7 | **Mẫu số của trần HTXS cá nhân:** Đ19.2a (và CV 694 mục II.4a) ghi "20% số được xếp Hoàn thành tốt **trở lên**"; lưu ý tại Đ16.2 ghi "20% cá nhân được xếp Hoàn thành tốt". Hai cách cho kết quả khác nhau | Giai đoạn 3 | Nêu cả hai; CV 694 đang vận dụng theo Đ19.2a. Không tự chọn |
| 8 | **"01 quý Không hoàn thành → không HTXS cả năm":** lưu ý tại Đ19.1a ghi cho mọi cá nhân; Đ19.5 chỉ bắt buộc với viên chức quản lý, người không giữ chức vụ "khuyến khích, không bắt buộc" | Giai đoạn 2–3 | Nêu cả hai điều khoản; không kết luận |
| 9 | Mẫu Quý III tính chiều chất lượng và tiến độ trên số **thực tế** chưa chặn trần (`=I*L*N/100`) — làm vượt số lượng thì % Trục có thể vượt 100%, trái Đ11.6 | Giai đoạn 2 (chấm điểm) | `kpi_calc.diem_chi_tieu` luôn chặn trần 100%; báo chênh lệch với tệp Excel nếu có |
