# 00-Nguyen-Tac-Chung — Nguyên tắc bắt buộc áp dụng cho MỌI skill

Đây là các nguyên tắc nền, áp dụng cho **tất cả** skill trong `06-Skill-Library` (01-29), không riêng skill nào. Mọi skill khi được gọi phải tuân theo các nguyên tắc này trước khi coi là hoàn thành nhiệm vụ.

## NGUYÊN TẮC BẤT BIẾN — Điều kiện tiên quyết để thực thi

**KTC-Van-Ban (skill/hệ thống này) chỉ được tạo ra kết quả khi đã đối chiếu thật với kho "Nền tảng dữ liệu" (01-04).** Đây là điều kiện tiên quyết, không phải bước tùy chọn hay "cố gắng làm nếu có thể".

Trước khi bắt đầu bất kỳ tác vụ nào (soạn thảo, rà soát, chuẩn hóa, trích xuất, gắn metadata...):

1. **Kiểm tra quyền truy cập 01-04** — xác nhận đang có: (a) file liên quan được đính kèm trực tiếp vào cuộc chat/Project knowledge, HOẶC (b) kết nối Google Drive connector đang hoạt động và có thể tìm/đọc được nội dung 01-04 thật.
2. **Nếu có quyền truy cập**: tìm và đọc tài liệu liên quan trong 01-04 trước khi thực hiện tác vụ, theo hướng dẫn ở Nguyên tắc 1 dưới đây.
3. **Nếu KHÔNG có quyền truy cập, hoặc không tìm thấy dữ liệu liên quan trong 01-04**: **DỪNG LẠI, không tạo kết quả**, và yêu cầu người dùng một trong hai:
   - Gửi bổ sung file Knowledge liên quan vào Project/cuộc chat, HOẶC
   - Kết nối/liên kết (connector) tới kho 01-04 trước khi tiếp tục.
4. Chỉ khi người dùng xác nhận rõ ràng muốn tiếp tục dù không có đối chiếu (ví dụ: "cứ làm tạm, tôi biết chưa đối chiếu được") thì mới được tạo kết quả — và khi đó PHẢI ghi chú nổi bật ngay đầu kết quả: "⚠️ Kết quả này chưa được đối chiếu với kho 01-04 theo yêu cầu của người dùng — độ tin cậy hạn chế."

Ngoại lệ hợp lý: câu hỏi thuần lý thuyết không liên quan văn bản cụ thể của Trường (ví dụ "Nghị định 30 quy định thế nào về thể thức chung") có thể trả lời trực tiếp từ Prompt/Skill Library mà không cần chặn, vì không phải là "tạo kết quả" cho một văn bản/tác vụ cụ thể của Trường.

## Nguyên tắc 1 — Đối chiếu kỹ với kho "Nền tảng dữ liệu" (01-04)

Khi đã xác nhận có quyền truy cập (theo Nguyên tắc bất biến ở trên), đối chiếu cụ thể như sau — không chỉ dựa vào nội dung đã có sẵn trong `05-Prompt-Library`/`06-Skill-Library`:

| Thư mục | Đối chiếu để làm gì |
|---|---|
| `01-Legal-Database` | Xác định đúng luật/nghị định/thông tư đang có hiệu lực áp dụng cho loại văn bản, lĩnh vực đang xử lý; lấy đúng số hiệu, ngày ban hành, nội dung điều khoản để trích dẫn làm căn cứ. |
| `02-KTC-Regulations` | Xác định quy chế, quy định, quy trình nội bộ của Trường có liên quan (ví dụ: quy chế chi tiêu nội bộ khi soạn tờ trình kinh phí, quy chế đào tạo khi soạn văn bản đào tạo) — đây là căn cứ mang tính đặc thù của Trường mà kho pháp luật chung không có. |
| `03-Templates` | Đối chiếu cấu trúc, bố cục, các trường thông tin bắt buộc của mẫu văn bản chuẩn cùng loại — để bản soạn thảo/kết quả rà soát bám đúng khung mẫu Trường đang dùng, không chỉ đúng Nghị định 30 một cách chung chung. |
| `04-Good-Documents` | Đối chiếu văn phong, cách xử lý tình huống, mức độ chi tiết của các văn bản tốt đã được Trường ban hành cùng loại/cùng lĩnh vực — để kết quả nhất quán với "khẩu vị" thực tế của Trường, không chỉ đúng lý thuyết. |

**Cách thực hiện khi có công cụ hỗ trợ (Claude.ai / Project có Google Drive connector):**
1. Tìm trong 4 thư mục các file có tên/metadata khớp với loại văn bản, lĩnh vực, hoặc từ khóa của tác vụ đang xử lý.
2. Đọc nội dung các file tìm được liên quan trực tiếp — không chỉ đọc tên file.
3. Trích dẫn cụ thể (số hiệu văn bản, tên mẫu, tên văn bản tham chiếu) khi dùng làm căn cứ trong kết quả trả về.
4. Nếu không tìm thấy tài liệu liên quan trong 01-04, áp dụng bước 3 của Nguyên tắc bất biến (dừng và hỏi), không suy diễn.

## Nguyên tắc 2 — Bắt buộc xuất kết quả cuối cùng thành file .docx

Khi một tác vụ/sản phẩm được coi là hoàn thành (bản soạn thảo hoàn chỉnh, báo cáo rà soát hoàn chỉnh, bản chuẩn hóa hoàn chỉnh...), **luôn tạo ra một file .docx** chứa kết quả đó, thay vì chỉ trả lời trong khung chat, kể cả khi người dùng không yêu cầu cụ thể "xuất file Word".

Quy tắc áp dụng:
- File .docx trình bày đúng thể thức tương ứng (Nghị định 30 với văn bản hành chính nhà nước; Quy định 399-QĐ/TW + Hướng dẫn 05-HD/VPTW với văn bản Đảng — xem Skill 29).
- Đặt tên file theo quy ước đã có của hệ thống: `[Số hiệu (nếu có)]_[Tên loại văn bản]_[Trích yếu ngắn gọn].docx`.
- Với báo cáo rà soát (Skill 28): file .docx phải có đủ cấu trúc 7 phần + mục kiểm tra chất lượng cuối, dùng định dạng bảng cho Phần II và Phần IV.
- Lưu kết quả vào đúng vị trí quy ước: `12-Output/YYYY-MM-DD/<loại thao tác>/`.
- Ngoại lệ hợp lý: các tác vụ mang tính hỏi-đáp ngắn, giải thích một quy định, hoặc góp ý nhanh một câu/đoạn — không cần đóng gói .docx nếu bản thân kết quả chỉ là vài dòng trả lời, không phải một "sản phẩm" hoàn chỉnh. Khi không chắc, ưu tiên xuất file.

## Giới hạn kỹ thuật thật của bước "nạp vào 11-Input" — ĐỌC KỸ TRƯỚC KHI ÁP DỤNG

Công cụ kết nối Google Drive hiện tại của AI **chỉ đọc và tạo file mới — không có khả năng sửa, đổi tên, di chuyển, hoặc xóa file đã tồn tại**. Vì vậy quy trình xử lý `11-Input` (xem `11-Input/README.md`) chỉ thực hiện được đến bước tạo bản sao đã phân loại/gắn metadata trong đúng thư mục 01-04 đích — **KHÔNG thể tự xóa file gốc khỏi `11-Input`**.

Áp dụng thực tế:
- Sau khi tạo bản sao đã xử lý vào 01-04, phải **liệt kê rõ cho người dùng** danh sách file gốc còn lại trong `11-Input` cần được tự xóa thủ công.
- Không được báo cáo "đã làm sạch 11-Input" hoặc "đã hoàn tất" nếu file gốc trên thực tế vẫn còn đó — chỉ báo cáo "đã tạo bản sao tại [vị trí], bạn cần xóa file gốc tại [vị trí] để hoàn tất".

## Áp dụng
Các nguyên tắc này được tham chiếu (không lặp lại toàn văn) trong từng Workflow ở `07-Workflow/` — xem bước tương ứng trong mỗi file workflow.
