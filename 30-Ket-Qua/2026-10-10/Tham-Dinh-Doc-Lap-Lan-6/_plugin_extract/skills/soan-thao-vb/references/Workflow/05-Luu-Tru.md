# 05-Luu-Tru — Lưu trữ

**Viết lại 14/9/2026.**

## Mục đích
Đưa văn bản đã ban hành vào kho `KTC-Database` sao cho **tra cứu lại được** và **dùng lại được**.

## Nguyên tắc
`KTC-Database` là **kho chỉ đọc đối với các hệ AI** — hook chặn mọi thao tác ghi. Hệ này chỉ **chuẩn bị**
bộ hồ sơ nộp lưu và đề xuất metadata; việc đưa vào kho do người có thẩm quyền thực hiện.

## Bước 1 — Xác định đúng kho

| Kho | Nhận loại tài liệu nào |
|---|---|
| `01-Legal-Database` | Văn bản quy phạm pháp luật (trung ương, tỉnh) |
| `02-KTC-Regulations` | Quy chế, quy định nội bộ · chiến lược · kế hoạch năm/quý/tháng · kế hoạch chuyên đề · đề án đã ban hành |
| `03-Templates(1)` | Biểu mẫu trống `.dotx`/`.xltx`. **Không** nộp văn bản có dữ liệu thật vào đây |
| `04-Good-Documents` | Văn bản đã ban hành đạt chất lượng — dùng học văn phong, bố cục |
| `05-De-an-De-tai` | Hồ sơ đề án theo từng vòng góp ý |

⚠️ `03-Templates` (không có dấu ngoặc) đã bị đánh dấu "CẦN XỬ LÝ / Không dùng" — không nộp vào đó.

⚠️ Tiền lệ đã xảy ra: hai tệp đặt tên là "mẫu" trong `KTC-Bao-Cao` thực chất là **phụ lục tháng 7 có dữ
liệu thật**. Đặt văn bản có dữ liệu vào chỗ dành cho biểu mẫu trống sẽ khiến kỳ sau kéo nhầm dữ liệu cũ.

## Bước 2 — Đặt tên tệp
`<Loại>-<số>_<Trích yếu không dấu, gạch nối>_<YYYYMMDD>_v<N>.<đuôi>`
Ví dụ: `BC-375_Bao-cao-ket-qua-thang-8-2026_20260906_v1.docx`.

## Bước 3 — Gắn metadata
11 trường bắt buộc + 2 trường theo loại + **3 trường trách nhiệm**: nguồn dữ liệu đã dùng · người kiểm tra ·
trạng thái phê duyệt. Xem `references/Skill-Library/00-Metadata-Schema.md`.

Quy trình nạp **2 tầng**: Tầng 1 là bản nháp metadata, Tầng 2 là bản đã được người có thẩm quyền xác nhận.

## Bước 4 — Cập nhật chỉ mục
Bổ sung dòng vào `KTC-DIS-Master-Index`. Chỉ mục hiện đang lạc hậu (bản v1.2 ngày 30/8/2026 chưa có
`03-Templates(1)`) — nộp lưu mà không cập nhật chỉ mục thì tài liệu coi như không tồn tại với các hệ khác.

## Bước 5 — Nêu rõ việc người dùng phải tự làm
Drive connector chỉ đọc và tạo tệp mới, **không xóa hay di chuyển được tệp cũ**. Liệt kê rõ tệp gốc nào ở
`11-Input` cần người dùng tự xóa. **Không báo "đã dọn sạch" nếu chưa thực sự xóa được.**

## Đầu ra
Bộ tệp đã đặt tên đúng quy ước · phiếu metadata đề xuất · dòng bổ sung cho chỉ mục · danh sách tệp cần xóa
thủ công.
