# 11-Input (v2 — cập nhật 05/8/2026, sửa theo đúng khả năng kỹ thuật thật)

## Mục đích
Thư mục tiếp nhận — nơi người dùng thả (upload) các file mới muốn bổ sung vào cơ sở dữ liệu của hệ thống (01-Legal-Database, 02-KTC-Regulations, 03-Templates, 04-Good-Documents).

## Cấu trúc con
- 11-Input/01-Legal-Database/
- 11-Input/02-KTC-Regulations/
- 11-Input/03-Templates/
- 11-Input/04-Good-Documents/

## Quy tắc vận hành THẬT (đã sửa — KHÔNG còn mô tả là "tự động làm sạch hoàn toàn")

Lý do sửa: Google Drive connector của Claude CHỈ đọc và TẠO file mới — KHÔNG thể sửa, đổi tên, di chuyển, hay xóa file đã có sẵn. Vì vậy bước "làm sạch 11-Input" KHÔNG thể tự động 100% như văn bản mô tả trước đây.

Quy trình thật, mỗi khi có tác vụ chạy và 11-Input không rỗng:

1. Claude quét file trong 11-Input, phân loại theo loại dữ liệu (01-04).
2. Claude gắn metadata theo đúng schema (00-Metadata-Schema.md của thư mục đích).
3. Claude TẠO một bản sao đã gắn metadata vào đúng thư mục con của 01-04 (đây là việc Claude LÀM ĐƯỢC qua connector).
4. Claude KHÔNG xóa được file gốc khỏi 11-Input — Claude phải liệt kê rõ: "Đã tạo bản sao đã xử lý tại [đường dẫn]. Đề nghị bạn tự xóa file gốc sau đây khỏi 11-Input sau khi xác nhận: [tên file]."
5. Người dùng tự xóa file gốc trên Drive (thao tác thủ công, ngoài khả năng của Claude).
6. Nếu một file không phù hợp bổ sung (trùng lặp, sai định dạng, không liên quan), Claude nêu rõ lý do và đề nghị người dùng tự xóa — Claude không tự loại bỏ được.

## Lưu ý
- Không dùng 11-Input làm nơi lưu trữ lâu dài.
- Đặt tên file rõ ràng: [Số hiệu (nếu có)]_[Tên loại văn bản]_[Trích yếu ngắn gọn].
- Xem thêm giới hạn kỹ thuật đầy đủ tại 06-Skill-Library/00-Nguyen-Tac-Chung.md.
