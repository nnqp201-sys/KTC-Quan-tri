# DL-20260918-005 — Quy ước đầu vào với KTC-Database và Google Drive

**Ngày:** 18/9/2026 · **Người quyết định:** người dùng (chủ dự án)

## Quyết định
1. **Đồng ý 4 quy ước** (ghi thành Nguyên tắc 4, `20-Chuan-Chung/00-Nguyen-Tac-Chung.md`, nhân xuống 5 gói):
   mỗi loại tài liệu một nơi lưu · tìm KTC-Database không qua ổ đĩa · quy tắc Google Drive · kiểm trùng.
2. **Giữ cả hai nơi** cho 2 tệp gốc năm 2026 trùng KTC-Database (CTCT năm 2026 + QĐ ban hành) — "dữ liệu gốc
   của năm 2026". Ghi thành ngoại lệ tại `10-Dau-Vao/02-Cap-Truong/00-Danh-Muc-Tro-KTC-Database.md`.
3. **Môi trường:** `.CLAUDE code/` là một thư mục Google Drive dùng chung (tra cứu, quản trị). Bản trên ổ `D:` chỉ
   để chạy code, **sẽ bị xóa**; về sau chỉ dùng trên Drive. ⇒ Không chỗ nào được phụ thuộc ký tự ổ đĩa.
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

## Việc còn lại khi chuyển hẳn lên Google Drive (chưa làm — chờ người dùng)
- **Git + GitHub backup:** không nên để thư mục `.git` trong thư mục Drive đồng bộ (Drive có thể làm hỏng kho git
  khi đồng bộ nhiều tệp nhỏ đang ghi). Khi bỏ bản `D:`, cần chọn: giữ một bản làm việc cục bộ ngoài Drive cho
  code/backup, hoặc bỏ backup GitHub.
- **Task Scheduler** backup 21:00 đang trỏ `D:\…` — phải trỏ lại hoặc tắt khi xóa bản `D:`.
- Hook nhật ký/doctor tự dò dự án theo thư mục làm việc — không phụ thuộc ổ đĩa.
