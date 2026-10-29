# 01-Kien-Truc-Bo-Nho-Van-Hanh-KTC-Ra-Soat-897-v2
## Kiến trúc bộ nhớ theo cơ chế Memory/Projects của ChatGPT

**Ngày thiết lập:** 23/08/2026  
**Mục tiêu:** Bảo đảm Hệ nhớ không chỉ dữ liệu đầu vào/đầu ra mà còn quá trình làm việc có giá trị tái sử dụng, kiểm tra và truy vết.

## I. Nguyên tắc thiết kế

### 1. Không đồng nhất Memory của ChatGPT với kho nhớ nghiệp vụ
ChatGPT có thể tham chiếu saved memories và lịch sử trò chuyện khi được bật, nhưng không bảo đảm ghi nhớ mọi chi tiết. Vì vậy:
- Memory của ChatGPT = lớp hỗ trợ ngữ cảnh.
- Project = lớp gom chat, file, instructions và lịch sử theo một công việc dài hạn.
- Google Drive/KTC-Database = lớp lưu trữ chuẩn, dùng làm nguồn sự thật.
- Process Memory = lớp ghi lại “đã làm như thế nào”.

### 2. Tách bộ nhớ ổn định và bộ nhớ quá trình
Không nhồi mọi thứ vào Project Instructions hoặc Saved Memory.
- Ổn định: phạm vi Hệ, nguyên tắc, thứ tự ưu tiên nguồn, quy tắc bắt buộc.
- Quá trình: từng ca rà soát, phiên bản đã dùng, quyết định, phản hồi, lỗi bỏ lọt, cách sửa, đầu ra.

### 3. Có khả năng truy vết
Mỗi kết luận quan trọng phải có thể trả lời: dựa trên file nào, phiên bản nào, đã kiểm tra gì, điều gì làm thay đổi kết luận, kết quả nào bị thay thế và quy tắc bắt nguồn từ đâu.

## II. Kiến trúc 6 lớp

### M0 — Project Instructions
Chỉ giữ nguyên tắc bất biến, ngắn và có tính điều khiển:
- Chỉ rà soát/so sánh/chuẩn hóa.
- Không tự bịa căn cứ.
- Ưu tiên nguồn chính thức.
- Tra Checklist 08 trước lỗi hình thức.
- Ghi nhận thiếu dữ liệu thay vì suy đoán.

### M1 — Memory Index
`MEMORY-INDEX.md` lưu phiên bản hiện hành, nguồn ưu tiên, quy tắc ổn định và tài liệu phải nạp.

### M2 — Version & Change Memory
Dùng Nhật ký cập nhật, changelog, phiếu phê duyệt, báo cáo cập nhật để lưu thay đổi phiên bản, lý do, file bị ảnh hưởng, quy tắc mới/cũ và trạng thái hiệu lực.

### M3 — Process Memory
Mỗi tác vụ chính thức hoặc có giá trị học tập phải có một bản ghi riêng theo `02-Mau-Process-Memory.md`.
Ví dụ: `PM-20260823-Quyet-dinh-NHCH-Vong-3.md`.

### M4 — Lessons Learned
Nguồn: người dùng sửa phân loại, AI bỏ lọt lỗi, căn cứ dùng sai, workflow không hiệu quả, cách trình bày được chấp thuận, mẫu đầu ra tốt.
Mỗi lesson phải có: `issue → evidence → correction → scope → approval_status`.

### M5 — Artifact Memory
Bao gồm Input, bản dự thảo từng phiên bản, Output, báo cáo rà soát, tệp đã chỉnh và liên kết/ID Drive.
Artifact Memory phải liên kết sang Process Memory để giải thích quá trình.

## III. Chu trình Đọc – Làm – Ghi

### A. Trước khi làm
1. Đọc Memory Index.
2. Đọc Nhật ký cập nhật mới nhất.
3. Kiểm chứng phiên bản file quan trọng trên Drive.
4. Xác định loại văn bản/tác vụ.
5. Nạp Skill + Prompt + Checklist tương ứng.
6. Tìm Process Memory gần nhất của cùng hồ sơ hoặc cùng loại.
7. Ghi nhận dữ liệu còn thiếu.

### B. Trong khi làm
Ghi tạm:
- nguồn đã đọc;
- quyết định phân loại;
- điểm chưa chắc;
- xung đột nguồn;
- thay đổi do người dùng yêu cầu;
- bước bị bỏ qua và lý do.

### C. Sau khi làm
1. Ghi Process Memory.
2. Liên kết đầu ra.
3. Ghi unresolved items.
4. Nếu có phản hồi quan trọng → ghi Lesson.
5. Nếu Lesson đã được phê duyệt → cập nhật Checklist/Skill/Memory Index phù hợp.
6. Nếu thay phiên bản → cập nhật Change Memory.
7. Không xóa lịch sử; đánh dấu thay thế.

## IV. Quy tắc chống “nhớ sai”
1. **Freshness check:** phiên bản, hiệu lực, pháp luật, cơ cấu tổ chức phải kiểm chứng lại.
2. **Source hierarchy:** chat cũ không được ghi đè văn bản hiện hành.
3. **Conflict flag:** nếu Memory Index, Nhật ký và Drive khác nhau, ghi `CONFLICT`.
4. **No silent reconciliation:** không tự hợp nhất thông tin mâu thuẫn mà không ghi dấu vết.
5. **Supersession:** ghi quan hệ file/quy tắc cũ → mới.
6. **Uncertainty:** nếu chưa đủ căn cứ, dùng “CHƯA ĐỦ CƠ SỞ KẾT LUẬN”.
7. **Minimal sensitive memory:** không lưu mật khẩu, mã truy cập, bí mật nhà nước hoặc dữ liệu không cần thiết.

## V. Tích hợp với ChatGPT Projects
Khuyến nghị:
- Dùng Project riêng cho Hệ.
- Bật các cài đặt Memory phù hợp với tài khoản/workspace.
- Nếu cần cô lập ngữ cảnh KTC-897 khỏi dự án khác, ưu tiên Project-only memory khi khả dụng.
- Giữ Project Instructions ngắn; hồ sơ chi tiết để trong Project files/Drive.
- Không coi Project memory là hệ thống kiểm toán; quyết định cần truy vết phải ghi ra Process Memory.

## VI. Tiêu chí đóng tác vụ
- [ ] Có đầu vào xác định.
- [ ] Có phiên bản Skill/Checklist/Prompt.
- [ ] Có căn cứ/nguồn chính.
- [ ] Có ghi bước đã chạy.
- [ ] Có phát hiện và quyết định phân loại.
- [ ] Có phản hồi người dùng nếu phát sinh.
- [ ] Có đầu ra/đường dẫn.
- [ ] Có vấn đề còn mở.
- [ ] Có Process Memory.
- [ ] Có cập nhật Lesson/Change Memory nếu cần.

## VII. Căn cứ thiết kế từ OpenAI
Thiết kế dựa trên hướng dẫn sản phẩm OpenAI hiện hành:
- Projects gom chat, file và project instructions cho công việc dài hạn.
- Project memory có thể tham chiếu các cuộc trò chuyện trong cùng Project tùy cài đặt.
- Reference saved memories và Reference chat history là hai cơ chế khác nhau.
- ChatGPT không ghi nhớ mọi chi tiết từ lịch sử trò chuyện.
- Người dùng kiểm soát Memory trong Settings > Personalization > Memory.

Khi OpenAI thay đổi chức năng Project/Memory, phải kiểm tra lại tài liệu OpenAI chính thức trước khi cập nhật Hệ.
