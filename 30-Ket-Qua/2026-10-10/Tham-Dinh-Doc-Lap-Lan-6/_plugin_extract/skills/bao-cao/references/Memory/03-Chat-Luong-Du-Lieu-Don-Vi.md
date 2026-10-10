# SỔ CHẤT LƯỢNG DỮ LIỆU THEO ĐƠN VỊ

Đọc trước Bước 1-2 mỗi kỳ. Mục đích: **nhắc trúng chỗ ngay từ đầu** thay vì phát hiện lại
cùng một vấn đề vào mỗi tháng, khi đã sát hạn nộp.

Ký hiệu: 🔴 lặp lại nhiều kỳ · 🟡 xảy ra 1 kỳ · ✅ đã khắc phục
Mọi mục đều ghi rõ mức độ chắc chắn: **[ĐÃ XÁC MINH]** hoặc **[CHƯA XÁC MINH]**.

---

## Vấn đề đang theo dõi

### 🟡 Khoa Kỹ thuật và Công nghệ — Excel IIb sai cấu trúc
- **[ĐÃ XÁC MINH]** Kỳ tháng 8/2026: nộp file IIb không đúng chuẩn, **không xử lý được**
  để tính cascade KPI.
- Hệ quả: nhiệm vụ của Khoa không vào được phần tính % KPI cấp Trường.
- **Việc cần làm kỳ sau:** gửi kèm file mẫu IIb chuẩn khi phát checklist Bước 0; kiểm file
  Khoa này **ngay khi nhận**, không đợi đến Bước 2.
- Cách kiểm nhanh: chạy `read_appendix()`, nếu `kind=None` hoặc `so_nhiem_vu=0` → sai cấu trúc
  (xem `02-So-Dang-Ky-Loi.md` để phân biệt nguyên nhân).

### 🟡 Phòng TH-HC&QT — nộp thiếu báo cáo đơn vị
- **[ĐÃ XÁC MINH]** Kỳ tháng 8/2026: chỉ nộp báo cáo của **Ban Truyền thông**, không có báo cáo
  của Phòng với tư cách đơn vị.
- Hệ quả: thiếu dữ liệu mảng hành chính - quản trị trong tổng hợp cấp Trường.
- **Việc cần làm kỳ sau:** trong checklist Bước 0, tách rõ 2 dòng riêng — "Phòng TH-HC&QT"
  và "Ban Truyền thông" — để tránh nộp gộp/nộp nhầm.

### ⬜ Phòng TC-KT và Khoa Sư phạm
- **[CHƯA XÁC MINH]** Bản `PATCH-NOTES-v2.5.1.md` mục D có nêu 2 đơn vị này gặp lỗi dữ liệu
  kỳ tháng 8 (TC-KT có dòng KPI dị thường; Khoa Sư phạm hỏng công thức ở Trục 5).
  **Chưa đối chiếu được với file gốc trong phiên 19/08/2026.**
- **Việc cần làm:** mở lại file IIb tháng 8 của 2 đơn vị này để xác nhận hoặc gỡ bỏ mục này.
  Không dùng thông tin này để nhắc đơn vị cho đến khi xác minh — nhắc sai làm mất uy tín checklist.

---

## Bảng theo dõi 14 đơn vị

Cập nhật sau mỗi kỳ. Ô trống = chưa ghi nhận vấn đề.

| Đơn vị | T7/2026 | T8/2026 | T9/2026 | Vấn đề hay gặp |
|---|---|---|---|---|
| Khoa Kỹ thuật và Công nghệ | | 🟡 IIb sai cấu trúc | | Cấu trúc file |
| Phòng TH-HC&QT | | 🟡 Thiếu BC đơn vị | | Nộp thiếu |
| Phòng TC-KT | | ⬜ cần xác minh | | — |
| Khoa Sư phạm | | ⬜ cần xác minh | | — |
| *(các đơn vị còn lại)* | | | | |

> Danh sách 14 đơn vị lấy từ checklist Bước 0 (Skill 35). Bổ sung đủ tên khi chạy kỳ tiếp theo.

---

## Cách dùng sổ này

1. **Đầu kỳ:** đọc mục "Vấn đề đang theo dõi", đưa các việc "cần làm kỳ sau" vào checklist Bước 0.
2. **Khi nhận báo cáo:** đơn vị nào có 🔴/🟡 thì kiểm trước, kiểm kỹ.
3. **Cuối kỳ:** cập nhật bảng theo dõi. Đơn vị 2 kỳ liên tiếp sạch lỗi → hạ xuống ✅.
4. **Ghi vấn đề mới:** nêu *hiện tượng cụ thể* và *hệ quả*, kèm việc cần làm kỳ sau.
   Tránh quy kết thái độ — sổ này để phòng ngừa, không phải để đánh giá đơn vị.
