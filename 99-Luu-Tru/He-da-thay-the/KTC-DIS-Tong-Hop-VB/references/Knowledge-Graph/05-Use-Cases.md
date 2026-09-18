# 05-Use-Cases

## Purpose
Store example scenarios that show how the system should reason end-to-end, gắn với ví dụ thực tế của KTC.

## Use case 1 — Soạn Quyết định bổ nhiệm lại cán bộ
Yêu cầu: "Soạn quyết định bổ nhiệm lại Trưởng phòng X."
Pipeline: `05-Phan-Tich-Yeu-Cau` (nhận diện: Quyết định cá biệt, lĩnh vực Cán bộ) → `22-Skill-Nghiep-Vu-Can-Bo` (kiểm tra đủ căn cứ quy trình nhân sự: biên bản họp, đề nghị đơn vị) → `07-Skill-Van-Ban-Quyet-Dinh` (soạn theo cấu trúc quyết định cá biệt) → `01-Soan-Thao` → `02-`/`14-` (thể thức, trình bày) → `17-Skill-Kiem-Tra-Tham-Quyen` (xác nhận Hiệu trưởng ký) → `19-` (chấm điểm trước khi trình ký).

## Use case 2 — Rà soát Kế hoạch phát triển đội ngũ 2026-2030 trước khi trình
Yêu cầu: "Rà soát lại Kế hoạch phát triển đội ngũ viên chức 2026-2030."
Pipeline: `02-Skill-Kiem-Tra-The-Thuc` + `14-Ky-Thuat-Trinh-Bay` → `15-Kiem-Tra-Logic` (kiểm tra chuỗi mục tiêu-nhiệm vụ-giải pháp-phân công-thời gian) → `03-Kiem-Tra-Can-Cu` (đối chiếu Nghị quyết 71-NQ/TW, kế hoạch tỉnh liên quan) → `18-Kiem-Tra-Tinh-Thong-Nhat` (tên đơn vị/chương trình) → `19-` (đánh giá tổng thể).

## Use case 3 — Kiểm tra căn cứ pháp lý cho Thông báo hướng dẫn sử dụng AI trong CTĐT
Yêu cầu: "Kiểm tra căn cứ cho thông báo hướng dẫn sử dụng AI trong chương trình đào tạo."
Pipeline: `05-Phan-Tich-Yeu-Cau` → `20-Skill-Nghiep-Vu-Dao-Tao` (đúng thuật ngữ GDNN) → `03-Skill-Kiem-Tra-Can-Cu` (tìm căn cứ: quy chế đào tạo, hướng dẫn của Bộ nếu có) → `09-Skill-Van-Ban-Thong-Bao` (đúng thể thức thông báo, không phải quyết định).

## Use case 4 — Chuẩn hóa văn phong một Báo cáo tổng kết năm học
Yêu cầu: "Viết lại báo cáo này cho đúng văn phong hành chính."
Pipeline: `06-Skill-Tong-Hop-Noi-Dung` (nếu nguồn là nhiều tài liệu rời) → `10-Skill-Van-Ban-Bao-Cao` (đúng cấu trúc báo cáo) → `04-Skill-Chuan-Hoa-Van-Ban` (văn phong) → `18-` (tính thống nhất tên gọi) → `19-`.

## Use case 5 — Đề xuất quy trình trình ký cho Tờ trình xin kinh phí mua sắm tài sản
Yêu cầu: "Tờ trình này cần trình theo quy trình nào?"
Pipeline: `23-Skill-Nghiep-Vu-Tai-Chinh` (kiểm tra định mức, nguồn kinh phí) → `11-Skill-Van-Ban-To-Trinh` → `16-Skill-De-Xuat-Quy-Trinh-Trinh-Ky` (xác định có cần họp, xin ý kiến, trình Hiệu trưởng hay cấp trên) → `17-Kiem-Tra-Tham-Quyen`.

## Use case 6 — Soạn Biên bản họp Hội đồng Khoa học và Đào tạo
Yêu cầu: "Soạn biên bản phiên họp Hội đồng Khoa học và Đào tạo lần 3."
Pipeline: `13-Skill-Van-Ban-Bien-Ban` → `01-Soan-Thao` (từ ghi chú cuộc họp) → `02-`/`14-` (thể thức) → kiểm tra đủ chữ ký thành viên Hội đồng bắt buộc.
