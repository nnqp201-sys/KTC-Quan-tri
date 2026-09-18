# 00-Prompt-Chinh-Thuc-Ra-Soat-897

## Vai trò trong hệ thống
Đây là **Mẫu prompt rà soát dự thảo văn bản chính thức do Trường Cao đẳng Kon Tum ban hành**, kèm theo Thông báo số 897/TB-CĐKT ngày 04/8/2026 (xem `02-KTC-Regulations/02-05-Huong-dan-AI-Ra-Soat/README.md`). Đây là prompt **có giá trị cao nhất** trong toàn bộ `05-Prompt-Library` cho tác vụ rà soát — vượt trên các prompt Rà-soát theo 7 loại văn bản đã tạo ở Batch 1 (`02-Ra-Soat/`), vì:

- Được lãnh đạo Trường chính thức ban hành, không phải do hệ thống AI tự đề xuất.
- Bao phủ **cả 3 hệ thống văn bản**: hành chính nhà nước (NĐ30), văn bản của Đảng (HD 05-HD/VPTW), và văn bản quy phạm pháp luật — trong khi các prompt Rà-soát theo loại văn bản ở Batch 1 chỉ bao phủ văn bản hành chính nhà nước.
- Có cơ chế xác minh hiệu lực văn bản pháp luật qua tra cứu (không dựa vào trí nhớ nội tại), có nguyên tắc ưu tiên khi rà soát, có cấu trúc báo cáo 7 phần chi tiết với 4 mức độ nghiêm trọng.

**Nguyên tắc bắt buộc theo Thông báo 897:** không tự ý sửa nội dung Mẫu prompt gốc; chỉ điền các trường "Thông tin bổ sung". Có 2 dạng file, nội dung giống nhau:
- `00-Prompt-Chinh-Thuc-Ra-Soat-897-goc.docx` — bản .docx gốc, giá trị pháp lý cao nhất khi có mâu thuẫn.
- `00-Prompt-Chinh-Thuc-Ra-Soat-897-full.md` — bản .md, dùng để dán trực tiếp vào khung chat hoặc đưa vào Knowledge/Skill của AI (dễ xử lý hơn định dạng .docx trong nhiều công cụ).

## Khi nào dùng prompt nào
- **Rà soát chính thức, đầy đủ, trước khi trình ký ban hành** (đúng quy trình Thông báo 897): dùng prompt này (`00-Prompt-Chinh-Thuc-Ra-Soat-897-goc.docx` hoặc bản `.md` tương đương), điền đủ "Thông tin bổ sung", đính kèm dự thảo + văn bản mẫu/căn cứ liên quan nếu có.
- **Rà soát nhanh, sơ bộ, nội bộ khi soạn thảo** (chưa phải bước trình ký chính thức): có thể dùng các prompt theo loại văn bản ở `02-Ra-Soat/` (Batch 1) để có phản hồi nhanh gọn hơn.
- Kết quả rà soát bằng AI (dù dùng prompt nào) **luôn chỉ có giá trị tham khảo** — phải qua bước kiểm tra, đối chiếu của con người theo Mục VI của Thông báo 897 trước khi tiếp thu.
