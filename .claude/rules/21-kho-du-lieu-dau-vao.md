---
paths:
  - "10-Dau-Vao/**"
description: Bốn nhánh của kho đầu vào và ba quy tắc nạp liệu
---

# Kho dữ liệu đầu vào dùng chung — `10-Dau-Vao/`

Từ 14/9/2026, đầu vào của **mọi hệ** nằm chung một chỗ, tổ chức theo **nguồn gốc dữ liệu** chứ không theo
hệ tiêu thụ. Đọc `10-Dau-Vao/00-README.md` trước khi nạp liệu.

| Nhánh | Chứa gì |
|---|---|
| `01-Dau-Moi-Nop/<kỳ>/<mã>/` | Hồ sơ 13 đầu mối nộp theo kỳ — kế hoạch và báo cáo để **chung**, vì đơn vị nộp gộp |
| `02-Cap-Truong/<nhóm kỳ>/<kỳ>/` | Văn bản cấp Trường đã ban hành |
| `03-Ket-Luan-Giao-Ban/<năm>/` | Thông báo kết luận giao ban tuần của Lãnh đạo Trường |

> `<nhóm kỳ>` của `02-Cap-Truong/`: `01-Nam/` (kỳ `YYYY`) · `02-Quy/` (`YYYY-Qn`) · `03-Thang/` (`YYYY-MM`) · `04-Chuyen-De/` (`YYYY-CD-<tên-ngắn>`). Văn bản cấp trên **không** lưu ở `10-Dau-Vao` — đọc tại `KTC-Database/01-Legal-Database/` (DL-20260918-005).


Ba quy tắc: **chỉ tạo thư mục khi có dữ liệu** (thư mục rỗng không còn nghĩa là "chưa nộp") · tên thư mục
đầu mối dùng **mã chuẩn** · tên kỳ theo `YYYY` / `YYYY-Qn` / `YYYY-MM` / `YYYY-CD-<tên-ngắn>`.

Đây là **nguồn đầu vào duy nhất** kể từ 14/9/2026 — `Nhap_Ke_Hoach/` và `Nhap_Bao_Cao/` đã chuyển hết,
60 thư mục rỗng còn lại chờ xóa thủ công (`30-Ket-Qua/2026-09-14/Danh-muc-can-don-toan-he.md`).
