# DL-20260914-002b — Bỏ thuật ngữ "KTC-DIS"

**Ngày:** 14/9/2026 · **Loại:** APPLY · **Người quyết định:** người phụ trách hệ

## Quyết định

Không dùng thuật ngữ **`KTC-DIS`** nữa. Thay bằng **"hệ thống KTC"** ở mọi văn bản mô tả.

## Phạm vi đã áp dụng

**61 chỗ / 41 tệp** `.md` và `.py`. Các cách diễn đạt được chuẩn hóa luôn:

| Cụm cũ | Cụm mới |
|---|---|
| `kiến trúc KTC-DIS` | `kiến trúc hệ thống KTC` |
| `họ KTC-DIS` | `họ skill KTC` |
| `Hệ KTC-DIS (skill/hệ thống này)` | `Skill này` |
| `kiến trúc KTC-DIS mở rộng` | `kiến trúc hệ thống KTC` |

## GIỮ NGUYÊN — tên thật của tệp và thư mục

Bốn tên sau **không đổi**, vì đổi sẽ làm gãy tham chiếu tới hiện vật có thật:

| Tên | Vì sao giữ |
|---|---|
| `KTC-DIS-Master-Index_20260830_v1.2.xlsx` | Tệp thật trong `KTC-Database` — kho **chỉ đọc**, không sửa được |
| `00-Template-Registry-KTC-DIS.docx` | Tệp thật trong `KTC-Database/03-Templates(1)` |
| `KTC-DIS-Tong-Hop-VB/` | Thư mục của hệ đã thay thế, đang chờ dọn thủ công |
| `Mo-Ta-Chi-Tiet-He-KTC-DIS-Chat-Cowork-Code.md` | Tên tệp tài liệu thiết kế; `CLAUDE.md` đang trỏ tới |

## Lý do tách hai loại

Thuật ngữ mô tả thì đổi được tự do. **Tên hiện vật thì không** — đổi tên trong văn bản mà hiện vật giữ tên
cũ sẽ tạo ra tham chiếu gãy, đúng loại lỗi mà phép kiểm C3 đang bắt. Với `KTC-Database` còn thêm một lý do
cứng: đó là kho chỉ đọc, hook chặn mọi thao tác ghi.

Nếu sau này muốn đổi cả tên hiện vật, phải làm thành một đợt riêng: đổi tên tệp trước, rồi mới sửa tham
chiếu — và với hai tệp nằm trong `KTC-Database` thì phải do người có thẩm quyền tự áp vào Drive.

**Liên quan:** `DL-20260914-001-Vai-tro-KTC-DIS-Tong-Hop-VB` · `CLAUDE.md`
