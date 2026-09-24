# Lỗi đã biết trong biểu mẫu

Biểu mẫu trong `assets/` **giữ nguyên byte** (không sửa biểu mẫu chính thức của Trường). Lỗi ghi ở đây để skill cảnh báo
khi người dùng dùng đúng mẫu tương ứng. Tệp xuất ra là **bản sao đã điền** — được xóa dòng ví dụ và chuẩn hóa phông.

Đo trực tiếp trên tệp ngày 24/9/2026.

| # | Mẫu | Lỗi | Skill xử lý | Giai đoạn |
|---|---|---|---|---|
| 1 | PL VI (tập thể Khoa Sư phạm), PL VII (Khoa các Khoa học cơ bản) — QĐ 2078 | Nhóm A chép từ Phòng TCCB ("kế hoạch… của Phòng", "lĩnh vực tổ chức cán bộ, chính trị tư tưởng, công tác HSSV") | Cảnh báo khi dùng mẫu | 2 |
| 2 | PL V (tập thể Phòng TC-KT) — QĐ 2078 | Cột cạnh "Điểm tối đa" có số trùng — có thể là điểm đạt điền sẵn | Cảnh báo, xin xác nhận | 2 |
| 3 | Tệp PL XVII — QĐ 2078 | Tiêu đề trong sheet ghi "Phụ lục XII" | Cảnh báo | 2 |
| 4 | Cả 6 mẫu Kế hoạch Quý III | Sheet "Ke Hoach" còn dòng ví dụ "Tổ chức thi và hoàn thiện hồ sơ lớp bồi dưỡng tiếng dân tộc thiểu số Bahnar…"; ghi chú mức độ có cụm "tác động lớn, sâu rộng trong toàn Đảng" (chép từ văn bản Đảng) | `kpi_mau.py` xóa vùng đầu việc trước khi điền; `validate_plan.py` KH06 bắt dòng ví dụ còn sót. Ghi chú mức độ: nêu khi người dùng hỏi nghĩa mức "Khó, phức tạp" | 1 |
| 5 | Cả 6 mẫu Kế hoạch Quý III | Sheet "KPI" ghi "Phụ lục II (Kèm theo Quyết định số:      /QĐ-CĐKT…)" — ô số Quyết định để trống; sheet "Ke Hoach" ghi "Phụ lục I"; sheet "Đánh giá" ghi Phụ lục III–VIII của một Quyết định chưa điền số | `validate_plan.py` KH13 (cảnh báo). Không tự điền số Quyết định | 1 |
| 6 | Sheet "KPI" cả 6 mẫu Quý III | 10–14 ô phông Calibri (thể thức Mức 2 theo `kiem_the_thuc.py` TX02) | `kpi_mau.py` chuẩn hóa sang Times New Roman trên tệp ra | 1 |
| 7 | Sheet "KPI" cả 6 mẫu Quý III | Chiều chất lượng, tiến độ tính trên số thực tế chưa chặn trần → % Trục có thể > 100% (trái QĐ 1923 Đ11.6) | Câu hỏi mở số 9 | 2 |
| 8 | Mẫu Phụ lục kèm Bản cam kết KPI (TB 1052) | Ghi chú (2) yêu cầu "tổng trọng số 100%" nhưng bảng không có cột trọng số | Câu hỏi mở số 3 | 1 |
| 9 | Sheet "KPI" và "Đánh giá" cả 6 mẫu | Bảng 19–25 cột đặt in dọc, không co vừa trang (`kiem_the_thuc.py` TX04, Mức 4) | Không sửa — góp ý | 1 |
