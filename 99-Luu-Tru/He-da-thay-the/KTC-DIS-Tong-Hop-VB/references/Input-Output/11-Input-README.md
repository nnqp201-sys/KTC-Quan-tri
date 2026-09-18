# 11-Input

## Mục đích
Thư mục tiếp nhận — nơi người dùng thả (upload) các file mới muốn bổ sung vào cơ sở dữ liệu của hệ thống (`01-Legal-Database`, `02-KTC-Regulations`, `03-Templates`, `04-Good-Documents`). Đây là bước "hàng chờ" giúp làm giàu dữ liệu liên tục mà không làm xáo trộn cấu trúc 4 thư mục dữ liệu nền đang vận hành.

## Cấu trúc con
Khớp 1-1 với 4 thư mục dữ liệu nền để việc phân loại rõ ràng ngay từ khi thả file:
- `11-Input/01-Legal-Database/` — văn bản pháp luật mới (luật, nghị định, thông tư, công văn hướng dẫn...)
- `11-Input/02-KTC-Regulations/` — văn bản nội bộ mới của Trường (quy chế, quy định, quy trình, kế hoạch...)
- `11-Input/03-Templates/` — mẫu văn bản mới muốn bổ sung vào kho mẫu chuẩn
- `11-Input/04-Good-Documents/` — văn bản tốt/đã ban hành muốn dùng làm dữ liệu học văn phong

## Quy tắc vận hành (đã hiệu chỉnh theo giới hạn kỹ thuật thật — xem `06-Skill-Library/00-Nguyen-Tac-Chung.md`)
**Mỗi khi một tác vụ được thực hiện xong** (soạn thảo, rà soát, chuẩn hóa, trích xuất... — bất kỳ tác vụ nào có sử dụng hệ thống), nếu tại thời điểm đó `11-Input/` đang có file chưa xử lý, AI phải:

1. **Phân loại & rà soát nhanh** từng file trong `11-Input/` — xác định file có phù hợp, có trùng lặp với dữ liệu đã có không (đối chiếu tên, số hiệu văn bản).
2. **Gắn Metadata** — áp dụng đúng schema đã định nghĩa tại `00-Metadata-Schema.md` của thư mục đích (Tên văn bản, Loại, Đơn vị ban hành, Ngày, Lĩnh vực, Người ký, Từ khóa, Căn cứ pháp lý, Đối tượng, Hiệu lực, Văn bản liên quan).
3. **Tạo bản sao đã xử lý** vào đúng thư mục con của thư mục dữ liệu đích tương ứng (ví dụ: từ `11-Input/01-Legal-Database/` → `01-Legal-Database/01-04- VB cua Chinh Phu/` nếu là nghị định của Chính phủ) — dùng công cụ tạo file (create_file qua connector Drive), **không phải di chuyển**.
4. **KHÔNG tự xóa được file gốc khỏi `11-Input/`** — công cụ hiện có không hỗ trợ xóa/di chuyển file trên Drive. Sau bước 3, AI phải liệt kê rõ cho người dùng: file nào đã tạo bản sao ở đâu, và file gốc nào trong `11-Input` cần người dùng tự xóa để hoàn tất.
5. Nếu một file không phù hợp bổ sung vào hệ thống (trùng lặp, sai định dạng, không liên quan), báo rõ lý do và đề nghị người dùng tự xóa khỏi `11-Input` — AI không tự xóa được.
6. **Báo cáo rõ ràng cho người dùng** sau mỗi lần xử lý Input: file nào đã tạo bản sao vào đâu, file gốc nào còn cần tự xóa, file nào bị bỏ qua và lý do. Không báo "đã làm sạch" hoặc "đã hoàn tất" nếu file gốc trên thực tế vẫn còn trong `11-Input`.

Quy tắc này áp dụng **độc lập với tác vụ chính** đang được yêu cầu — nghĩa là dù người dùng đang yêu cầu soạn một Quyết định hay rà soát một Báo cáo, nếu `11-Input/` có file đang chờ, bước xử lý này vẫn được thực hiện trong cùng lượt xử lý (thường sau khi hoàn thành tác vụ chính, trước khi kết thúc lượt).

## Lưu ý
- Không dùng `11-Input` làm nơi lưu trữ lâu dài — đây chỉ là điểm trung chuyển. Vì AI không tự xóa được, người dùng cần chủ động dọn định kỳ theo báo cáo AI đã cung cấp.
- Đặt tên file rõ ràng, dễ nhận diện (tương tự quy tắc tại `02-05-Huong-dan-AI-Ra-Soat`: [Số hiệu (nếu có)]_[Tên loại văn bản]_[Trích yếu ngắn gọn]) để việc phân loại được nhanh chóng, chính xác.
