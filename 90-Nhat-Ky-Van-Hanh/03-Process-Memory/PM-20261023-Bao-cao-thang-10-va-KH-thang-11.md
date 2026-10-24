# PM-20261023 — Rà soát, sửa có dấu vết Báo cáo tháng 10, Phụ lục kết quả và Kế hoạch tháng 11/2026

**Loại:** rà soát và hoàn thiện bản dự thảo sẵn có của người dùng (không dựng từ đầu) · **Kết quả:** `30-Ket-Qua/2026-10-23/Bao-cao-thang-10/` (docx Track Changes + 2 xlsx màu + ghi chú rà soát)

## Đã làm

- Đầu vào do người dùng đặt ở OneDrive (`BC t10 - KH t11`, tách theo loại Ia/IIa/IIb, 10 đơn vị) — không phải `10-Dau-Vao/`.
- Lấy **KH-983** (kế hoạch tháng 10) và **KH-975** (quý IV) từ kho làm chuẩn; đối chiếu 55 nhiệm vụ KH-983 với Phụ lục IIb/IIa các đơn vị → 28 vào phụ lục kết quả, 27 chuyển sang KH tháng 11, không rơi nhiệm vụ nào.
- Docx: `ktc_trackchanges.py` + hai hàm phụ tự viết (chèn trong đoạn, chèn nhãn mục con có đánh dấu dấu đoạn) — từ chối hết thay đổi khôi phục 97/97 đoạn. Xlsx: quy ước màu + sheet "Quy ước màu" + nhật ký.

## Bài học tái sử dụng

- **Cột Điểm/Hệ số của mẫu KH là công thức theo độ khó (G).** Dựng lại bảng bằng openpyxl mà chép công thức cũ thì trỏ nhầm dòng — dòng "Khó và phức tạp" hiện 150 điểm. Phải ghi lại công thức theo số dòng mới; kiểm `điểm = f(độ khó)` trên mọi dòng.
- **Ô văn bản bắt đầu bằng "="** (ví dụ "=SUM(...)" ghi trong sheet nhật ký) bị openpyxl lưu là công thức hỏng → Excel từ chối mở tệp. Đặt `cell.data_type = "s"`.
- Excel COM: truyền đường dẫn bằng dấu `/` hoặc chuỗi PowerShell nháy đơn; trong bash `"\\$v"` thành `\$v` và mở sai tệp. `Open()` thất bại không có nghĩa tệp hỏng — kiểm bằng một tệp openpyxl trắng trước.
- Mẫu mã đơn vị trong bảng Ib/IIb của đơn vị hay nộp **nhầm tệp, nhầm kỳ** (IIb Khoa KHCB là kế hoạch tháng 11; Phòng QLĐT&BĐCL nộp báo cáo kết quả trong tệp Ib; IIb Phòng TC-KT đề "tháng 8"). Nhận dạng bằng tiêu đề sheet và nội dung, không theo tên tệp.
- Mỗi kế hoạch chuyên đề có bảng nhiệm vụ cùng bố cục `STT | Nội dung | Chỉ đạo | Chủ trì | Phối hợp | Sản phẩm | SL | Mức | Thời gian | Điểm | Hệ số` — trích được hàng loạt bằng python-docx để bổ sung KH tháng.
- Thông tư số trùng nhau giữa các tháng dễ lẫn: TT 63/2026 là Điều lệ trường, TT 75 là kiến thức THPT trong chương trình trung học nghề, TT 82 là quy trình biên soạn chương trình môn chung. Tra metadata kho trước khi viện dẫn.

## Còn mở

Xem mục 4–6 của `00-Ghi-chu-ra-soat-BC-thang-10-KH-thang-11.md`: thanh lý tài sản, sơ kết quý III Đảng ủy, học liệu tích hợp, mốc 30/11 đề xuất, đầu vào thiếu của 5 đầu mối, giao ban tuần 05–18/10, rà soát 897 chưa chạy.
