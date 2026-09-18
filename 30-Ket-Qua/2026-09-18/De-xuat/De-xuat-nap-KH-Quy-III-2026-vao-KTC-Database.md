# Đề xuất nạp KH công tác Quý III/2026 (điều chỉnh, bổ sung) vào KTC-Database

**Ngày:** 18/9/2026 · **Căn cứ:** Nguyên tắc 4.1 (`20-Chuan-Chung/00-Nguyen-Tac-Chung.md`), `DL-20260918-005`
**Người thực hiện:** người có quyền ghi KTC-Database (AI không ghi vào kho — kho chỉ đọc)

| Mục | Nội dung |
|---|---|
| Tệp nguồn | `KTC-Quan-tri/10-Dau-Vao/02-Cap-Truong/02-Quy/2026-Q3/KH-cong-tac-Quy-III-2026-dieu-chinh-bo-sung.xlsx` |
| Kiểm trùng | Đã so mã băm với toàn bộ KTC-Database 18/9/2026: **chưa có** bản nào trùng |
| Đích đề xuất | `KTC-Database/02-KTC-Regulations/02-03- Ke hoach nam, quy, thang/` (thư mục con kế hoạch QUÝ) |
| Cách nạp | Chép tệp vào `KTC-Database/11-Input/02-KTC-Regulations/`, rồi chạy quy trình nạp 2 tầng của skill `ktc-database` (kiểm trùng, sidecar `.metadata.md`) |
| Metadata cần xác minh trước khi nạp | Số hiệu, ngày ban hành, người ký của văn bản điều chỉnh — **tệp Excel không ghi**, cần lấy từ văn bản ban hành kèm theo |

Sau khi nạp: giữ bản trong `10-Dau-Vao` theo ngoại lệ "dữ liệu gốc năm 2026" và thêm dòng vào bảng ngoại lệ của
`10-Dau-Vao/02-Cap-Truong/00-Danh-Muc-Tro-KTC-Database.md` — nếu không, phép kiểm C12 sẽ báo trùng.
