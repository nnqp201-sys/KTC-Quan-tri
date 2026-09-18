# 02-Ra-Soat

## Purpose
Define the review workflow for format, basis, and language checks.

## Steps
1. Receive the draft from the drafting workflow.
2. Run `02-Skill-Kiem-Tra-The-Thuc`.
3. Run `03-Skill-Kiem-Tra-Can-Cu` if legal basis is present or required.
4. Run `04-Skill-Chuan-Hoa-Van-Ban` if wording needs cleanup.
5. Consolidate the review result.
6. Decide whether the document is ready for approval.

## Outputs
- Review summary
- Issues list
- Revision instructions

## Cập nhật theo Thông báo 897/TB-CĐKT (04/8/2026) — Rà soát dự thảo văn bản bằng AI trước khi ban hành

Kể từ 04/8/2026, đối với dự thảo trình ký chính thức (đặc biệt: quyết định, kế hoạch, quy chế, quy định, chương trình, nghị quyết...), bước rà soát nói trên nên được thực hiện theo đúng quy trình 6 bước chính thức của Trường, thay vì chỉ chạy các skill nội bộ đơn lẻ:

1. **Chuẩn bị dự thảo** — hoàn thiện tương đối đầy đủ về nội dung và thể thức trước khi đưa lên AI.
2. **Xác định thông tin dự thảo** — hệ thống văn bản (hành chính nhà nước/Đảng/quy phạm pháp luật), loại văn bản, hình thức, cơ quan ban hành, mục đích/đối tượng, căn cứ pháp lý, lĩnh vực chuyên môn.
3. **Đối chiếu sâu với kho Nền tảng dữ liệu (01-04)** trước khi rà soát — bắt buộc theo `06-Skill-Library/00-Nguyen-Tac-Chung.md` (Nguyên tắc 1). Với báo cáo rà soát chính thức, đây không phải bước tùy chọn: phải chủ động tìm và đọc trong `01-Legal-Database`, `02-KTC-Regulations`, `03-Templates`, `04-Good-Documents` các tài liệu liên quan trực tiếp đến văn bản đang rà soát, và đưa kết quả đối chiếu này vào Phần II của báo cáo (xem chi tiết hướng dẫn khai thác từng thư mục tại `06-Skill-Library/28-Skill-Bao-Cao-Ra-Soat-Chuan.md`, mục "Khai thác kho Nền tảng dữ liệu").
4. **Rà soát bằng AI** — dùng đúng `05-Prompt-Library/00-Prompt-Chinh-Thuc-Ra-Soat-897-goc.docx` (Mẫu prompt chính thức do Trường ban hành), không tự sửa nội dung prompt; đính kèm dự thảo + văn bản mẫu/căn cứ liên quan (kể cả tài liệu tìm được ở bước 3).
5. **Kiểm tra, đối chiếu kết quả rà soát (bắt buộc, con người)** — đối chiếu từng nội dung với quy định thực tế; tự tra cứu xác minh hiệu lực văn bản pháp luật tại nguồn chính thống; xin ý kiến bộ phận pháp chế (phòng TH-HC&QT) với nội dung liên quan thẩm quyền/tính hợp pháp.
6. **Chỉnh sửa dự thảo** — tiếp thu nội dung đã xác nhận đúng; báo cáo cấp thẩm quyền với nội dung còn ý kiến khác nhau.
7. **Xuất báo cáo rà soát hoàn chỉnh thành file .docx** (Nguyên tắc 2, `06-Skill-Library/00-Nguyen-Tac-Chung.md`), đủ cấu trúc 7 phần theo Skill 28, lưu vào `12-Output/YYYY-MM-DD/02-Ra-Soat/`.
8. **Trình ký, ban hành** theo quy trình hiện hành — việc đã rà soát AI không làm giảm nhẹ trách nhiệm kiểm tra của văn thư và người ký.

**Lưu ý bắt buộc:** kết quả rà soát AI chỉ có giá trị tham khảo; không đưa văn bản mật/bí mật công tác hoặc thông tin cá nhân nhạy cảm chưa ẩn danh lên AI; chỉ dùng công cụ AI được Trường cho phép.

Chi tiết đầy đủ: `02-KTC-Regulations/02-05-Huong-dan-AI-Ra-Soat/README.md`.
