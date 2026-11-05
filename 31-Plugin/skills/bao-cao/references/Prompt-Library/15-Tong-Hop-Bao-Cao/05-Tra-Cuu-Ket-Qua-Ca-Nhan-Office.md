# 05-Tra-Cuu-Ket-Qua-Ca-Nhan-Office (Prompt cho Skill 38)
## Phiên bản: v1.0 — 10/10/2026

## Câu lệnh mẫu — Claude Cowork tự đọc trên trang (Đường A)

> Tôi đã đăng nhập Hệ thống quản lý văn bản và điều hành tại https://office.quangngai.gov.vn/ trong trình duyệt.
> Hãy tra cứu **văn bản đã xử lý** và **công việc được giao** của **[Họ tên]**, từ ngày **[dd/mm/yyyy]** đến ngày
> **[dd/mm/yyyy]**, vai trò **[xử lý chính / phối hợp / cả hai]**. Chỉ đọc, không bấm nút xử lý, không mở tệp đính kèm.
> Lập bảng kết quả .xlsx để tôi làm báo cáo cá nhân **[tháng … / Quý …]**.

## Câu lệnh mẫu — có tệp xuất (Đường B)

> [Đính kèm tệp Excel xuất từ mục Văn bản đã xử lý, Quản lý công việc]
> Lập bảng kết quả cá nhân của **[Họ tên]** từ ngày … đến ngày …, vai trò … để làm báo cáo cá nhân.

## Việc Claude phải làm

1. Đọc `38-Skill-Tra-Cuu-Ket-Qua-Ca-Nhan-Office.md`. Thiếu người, kỳ, vai trò, phạm vi → hỏi.
2. Đường A: kiểm tra phiên → đọc danh sách, kiểm đếm → ghi bản chụp .json. Về màn hình đăng nhập → dừng, đề nghị đăng nhập
   lại hoặc gửi tệp xuất.
3. Chạy `office_ca_nhan.py` → bảng 4 sheet.
4. Điền các cột đề xuất (Trục, Nội hàm, sản phẩm chuẩn và hệ số theo Quyết định số 2119/QĐ-CĐKT), cột gợi ý nhiệm vụ liên
   quan; ghi rõ là đề xuất, chờ người báo cáo xác nhận.
5. Trả lời ngắn: số văn bản, số công việc theo vai trò; số loại ra và lý do; điều cần xác nhận; nhắc đây là một nguồn,
   việc ngoài hệ thống cần bổ sung.

## Không làm

Không nhập mật khẩu, không bấm nút xử lý trên hệ thống, không đọc văn bản có độ mật, không chấm điểm hay xếp loại, không
cấp Task_ID, không gửi thư.
