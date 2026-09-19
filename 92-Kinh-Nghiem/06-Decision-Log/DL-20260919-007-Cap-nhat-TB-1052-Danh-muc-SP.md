# DL-20260919-007 — Cập nhật Thông báo 1052/TB-CĐKT và Danh mục sản phẩm/công việc kèm theo

**Ngày:** 19/9/2026 · **Yêu cầu:** "Khẩn: có thông báo mới… nạp 2 file mới vào 11-Du-lieu-Cong-Viec, đọc và cập nhật"

**Hai tệp nhận được:**
- `1052_Thong bao ket luan…(1).docx`: TB 1052/TB-CĐKT ngày 15/9/2026, kết luận Tọa đàm KPI ngày 10/9/2026.
- `1052_DanhmucSP (1).xlsx`: phụ lục Danh mục sản phẩm/công việc quy đổi, 371 dòng.

**Đối chiếu (đo thật):**
1. **Trùng byte** với bản đã có trong KTC-Database, kho 02 (`TB-1052-TB-CDKT_…docx`, `…Phu-luc…xlsx`). Theo Nguyên
   tắc 4.4, dự án không giữ bản chép: đã chuyển vào `99-Luu-Tru/Ban-trung-KTC-Database/` (lấy lại được).
   Tài liệu trỏ tới bản gốc trong kho.
   - Phép kiểm C12 trước đó chỉ quét `10-Dau-Vao` nên **bỏ sót**; nay quét thêm `11-Du-lieu-Cong-Viec`. Đã thử: C12 bắt
     đúng 2 tệp này, không báo nhầm tệp khác.
   - Bản thô `(1)` còn nằm trong `KTC-Database/11-Input/`. Kho chỉ đọc nên để người dùng tự dọn.
2. **Phụ lục = dự thảo lần 4**, ghép 371/371 theo tên sản phẩm: cùng Nhóm, cùng Hệ số. Chỉ bỏ cột Điểm và cột
   Trục/Nội hàm, và đánh STT theo 38 lĩnh vực.
3. **38 lĩnh vực = 38 nội hàm của TB 817**: khớp tên và số sản phẩm 38/38 với `10-Sau-Truc-38-Noi-Ham.md`. Đã ghi
   bảng quy đổi STT lĩnh vực sang Trục và nội hàm.
4. **KI-014 còn nguyên:** 204/371 dòng có hệ số khác giá trị chuẩn của Nhóm. 5 dòng bất thường: 29.22 hệ số 50;
   2.7; 21.1; 10.10; 38.3.

**Trạng thái mới:** danh mục đã **gửi chính thức cho đơn vị rà soát (hạn 20/9/2026)**, **chưa ban hành**. Vẫn không
dùng để kiểm dữ liệu vận hành; vẫn không tự quy đổi giữa hai thang.

**Đã cập nhật:**
- `22-KTC-Dieu-Phoi/references/13-Danh-Muc-Nhiem-Vu-Va-San-Pham.md` và `10-Sau-Truc-38-Noi-Ham.md`;
- `22-KTC-Dieu-Phoi/00-README-ktc-quan-tri.md`, `11-Du-lieu-Cong-Viec/00-README.md`;
- `CLAUDE.md`; KI-014 trong `Pending.md`;
- skill quan-tri 1.9, plugin 0.9.1.

**Sản phẩm cho hạn gấp:**
- Góp ý danh mục để P-THHC gửi Phòng TCCB-CTHSSV trước 20/9: `30-Ket-Qua/2026-09-19/De-xuat/Gop-y-Danh-muc-SP-TB-1052.md`.
- Phiếu nhiệm vụ phát sinh (6 việc, hạn 20/9 · 21/9 · 25/9): `30-Ket-Qua/2026-09-19/Nhiem-vu-phat-sinh/TB-1052-TB-CDKT_Nhiem-vu-phat-sinh.md`.
- Chưa cấp Task_ID; việc cấp do `ktc-ke-hoach` làm.

**Còn thiếu:** mẫu Bản cam kết KPI "kèm theo" không có trong hai tệp, cũng không có trong kho 02.
