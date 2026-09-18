# DL-20260918-005 — Quy ước đầu vào với KTC-Database và Google Drive

**Ngày:** 18/9/2026 · **Người quyết định:** người dùng (chủ dự án)

## Quyết định
1. **Đồng ý 4 quy ước** (ghi thành Nguyên tắc 4, `20-Chuan-Chung/00-Nguyen-Tac-Chung.md`, nhân xuống 5 gói):
   mỗi loại tài liệu một nơi lưu · tìm KTC-Database không qua ổ đĩa · quy tắc Google Drive · kiểm trùng.
2. **Giữ cả hai nơi** cho 2 tệp gốc năm 2026 trùng KTC-Database (CTCT năm 2026 + QĐ ban hành) — "dữ liệu gốc
   của năm 2026". Ghi thành ngoại lệ tại `10-Dau-Vao/02-Cap-Truong/00-Danh-Muc-Tro-KTC-Database.md`.
3. **Môi trường (người dùng đính chính cùng ngày):** chỉ **bản chép KTC-Database trên ổ `D:`** sẽ bị xóa; bản gốc
   ở Google Drive `My Drive/KTC-Database` (máy này gắn ở `H:`). **KTC-Quan-tri vẫn chạy tại máy** — git, backup
   GitHub, Task Scheduler giữ nguyên. Đo 18/9/2026: bản `D:` thiếu 163/1.171 tệp so với Drive ⇒ đã cho script đọc
   thẳng bản Drive (`duong_dan.py` dò ổ Google Drive), C12 so kích thước trước để không tải cả kho.
4. **`02-Cap-Truong/` chia `01-Nam/` · `02-Quy/` · `03-Thang/` · `04-Chuyen-De/`** (người dùng yêu cầu Nam/Quy/Thang;
   thêm Chuyên đề vì skill kế hoạch đã có kỳ `YYYY-CD-…` dùng nhánh này).

## Đã thực hiện
- Dời 3 tệp vào `01-Nam/2026/`, `02-Quy/2026-Q3/` (`git mv`). Bỏ `04-Van-Ban-Cap-Tren/` (rỗng) — văn bản cấp trên
  đọc tại `KTC-Database/01-Legal-Database/`. Cập nhật skill kế hoạch (Luồng B/C, Pre-flight, Workflow 10).
- `29-Cong-Cu/duong_dan.py`: tìm kho qua `KTC_DATABASE_DIR` → thư mục ngang cấp. Bỏ ghi cứng `D:` ở 5 script và
  quy trình Track Changes; CLAUDE.md dùng `../KTC-Database`.
- Phép kiểm mới **C12** (đầu vào trùng kho, tôn trọng ngoại lệ) và **C13** (cấm đường dẫn ổ đĩa) + hồi quy
  `test_c12_c13_kho_va_o_dia.py` (6 ca, có ca ngược).
- Đề xuất nạp KH Quý III/2026 điều chỉnh (chưa có trong kho): `30-Ket-Qua/2026-09-18/De-xuat/`.

## Trước khi xóa bản chép `D:\…\KTC-Database`
- Kiểm tra thư mục `.CLAUDE code` trên ổ `D:` **không** được Google Drive đồng bộ kiểu "phản chiếu/sao lưu máy tính"
  — nếu có, xóa ở máy sẽ xóa luôn bản trên Drive của mục đó. Bản gốc ở `My Drive/KTC-Database` là thư mục riêng.
- Sau khi xóa: chạy `python 29-Cong-Cu/kiem_tra_he_thong.py` — C12 phải vẫn tìm thấy kho (qua ổ Google Drive).
