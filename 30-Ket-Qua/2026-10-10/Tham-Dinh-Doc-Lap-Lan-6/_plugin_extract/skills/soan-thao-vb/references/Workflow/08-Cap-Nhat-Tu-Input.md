# 08-Cap-Nhat-Tu-Input

## Purpose
Làm giàu cơ sở dữ liệu (`01-Legal-Database`, `02-KTC-Regulations`, `03-Templates`, `04-Good-Documents`) từ các file người dùng thả vào `11-Input/`, thực hiện ngay sau mỗi tác vụ để dữ liệu được cập nhật liên tục thay vì phải chờ một đợt xử lý riêng.

## Giới hạn thật (đọc trước khi thực hiện)
Khi truy cập Drive qua Google Drive connector, Claude **chỉ có thể đọc và tạo file mới — không thể xóa, đổi tên, hay di chuyển file đã có sẵn**. Vì vậy quy trình dưới đây là **bán tự động**: AI xử lý phân loại + tạo bản sao ở đúng vị trí, nhưng bước dọn sạch `11-Input/` cần người dùng xác nhận và tự xóa. Không mô tả quy trình này là "tự động hoàn toàn" trong bất kỳ tài liệu nào khác của hệ thống.

## Trigger
Chạy sau khi hoàn thành **bất kỳ tác vụ nào** trong hệ thống (soạn thảo, rà soát, chuẩn hóa, trích xuất, gắn metadata...), nếu `11-Input/` không rỗng tại thời điểm đó.

## Steps
1. Quét toàn bộ file hiện có trong `11-Input/01-Legal-Database/`, `11-Input/02-KTC-Regulations/`, `11-Input/03-Templates/`, `11-Input/04-Good-Documents/`.
2. Với mỗi file: kiểm tra trùng lặp với dữ liệu đã có (theo tên/số hiệu văn bản).
3. Gắn metadata theo đúng schema của thư mục đích (`00-Metadata-Schema.md` tương ứng).
4. **Tạo bản sao** file (đã gắn metadata) vào đúng thư mục con của thư mục dữ liệu đích — dùng công cụ tạo file (create_file), không phải "di chuyển".
5. Báo cáo lại cho người dùng: danh sách file đã tạo bản sao (kèm vị trí mới), file bị loại vì trùng lặp/không phù hợp (kèm lý do), và **đề nghị người dùng tự xóa file gốc tương ứng trong `11-Input/`** sau khi xác nhận bản sao đúng.
6. Không tự coi `11-Input/` là "đã sạch" cho đến khi người dùng xác nhận đã xóa — nếu người dùng chưa phản hồi, giữ nguyên trạng thái file gốc, không giả định đã xử lý xong.

## Outputs
- Bản sao đã gắn metadata được tạo trong 01-04
- Danh sách file cần người dùng tự xóa khỏi `11-Input/` (kèm lý do/vị trí bản sao mới)
- Tóm tắt thay đổi báo cáo lại cho người dùng

## Related
- [[11-Input/README.md]] — quy tắc vận hành đầy đủ
- [[00-Master-Index.md]] — Operating sequence
