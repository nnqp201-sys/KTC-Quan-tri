# PATCH-NOTES v3.4 — Kiểm thử sâu, phát hiện & sửa 7 xung đột nội tại
## Ngày: 20/08/2026 | Phạm vi: `read_bc736_excel.py`, `fill_bc736.py`, tài liệu Skill

## Bối cảnh
Sau khi v3.3 đạt 45/45 vị trí PASS, tiến hành kiểm thử SÂU: thay vì chỉ dùng token sạch
(`TOKEN_I_01_xxx`), chuyển sang thử nội dung thật, sai sót thật của người dùng, và đối
chiếu tính nhất quán giữa các thành phần. Phát hiện **7 xung đột** mà bộ test cũ không chạm tới.

## Bảng 7 xung đột

| # | Xung đột | Mức độ | Trạng thái |
|---|---|---|---|
| 1 | `build_content_map_skeleton()` trả dict PHẲNG nhưng `fill_report()` cần dict 3 tầng → crash `AttributeError: 'str' object has no attribute 'items'` (thông báo vô nghĩa). Nghiêm trọng vì **Skill 33 hướng dẫn đúng chuỗi này** | 🔴 Cao | ✅ Đã sửa |
| 2 | `muc_ii_items` (nhiệm vụ CHƯA hoàn thành) được `read_appendix()` tách ra nhưng **KHÔNG hàm nào tiêu thụ** — nguy cơ bỏ sót việc chưa xong khỏi báo cáo | 🔴 Cao | ✅ Đã sửa |
| 3 | Không idempotent: chạy `fill_report()` lần 2 trên file output → không sửa lại được nội dung (placeholder đỏ đã mất) | 🟡 Trung bình | ⚠️ Ghi nhận (xem dưới) |
| 4 | Thiếu hẳn 1 Phần trong `content_by_phase` → chạy bình thường, tự đánh `[CẦN BỔ SUNG]` | 🟢 Thấp | ✅ Hành vi đúng, không cần sửa |
| 5 | Gõ sai tên Phần (`phan_i` thường, `PHANI` thiếu gạch) → **im lặng bỏ qua toàn bộ nội dung**, chỉ báo mơ hồ "gõ sai tên KHÓA" trong khi lỗi thật là sai tên PHẦN | 🔴 Cao | ✅ Đã sửa |
| 6 | Tài liệu ghi "22 khóa" ở 3 nơi, thực tế đã kiểm chứng **45 vị trí** | 🟡 Trung bình | ✅ Đã sửa |
| 7 | Tài liệu còn tham chiếu API cũ `content_map` lẫn với API mới `content_by_phase` | 🟢 Thấp | ✅ Đã rà, giữ lại chỗ nói về lịch sử thay đổi (hợp lý) |

## Chi tiết cách sửa

### Xung đột 1 — sửa ở CẢ 2 đầu
- **Đầu ra**: `build_content_map_skeleton()` nay trả về đúng `{"PHAN_I": {...}, "PHAN_II": {}, "PHAN_III": {}}`, thêm tham số `phase=` để chọn Phần.
- **Đầu vào**: `fill_report()` kiểm tra cấu trúc trước khi chạy, báo `TypeError` **chỉ rõ nguyên nhân và cách sửa** thay vì crash khó hiểu.
- ⚠️ Lưu ý giữ nguyên: khung nháp dùng khóa `__DRAFT__ TrụcN__ĐơnVị` KHÔNG khớp nhãn thật trong mẫu — vẫn **bắt buộc người tổng hợp biên tập lại**. Docstring đã ghi rõ 3 bước phải làm.

### Xung đột 2 — Mục II vào khung nháp
`build_content_map_skeleton()` nay tạo thêm mục `__DRAFT__ MucII__ChuaHoanThanh`, ghi rõ số
nhiệm vụ chưa xong + tên việc + hướng dẫn: đưa vào "Tồn tại, hạn chế" (PHAN_II) hoặc "Nhiệm vụ
kỳ tới" (PHAN_III), **KHÔNG báo cáo là đã hoàn thành**.

### Xung đột 5 — cảnh báo đúng nguyên nhân
Thêm kiểm tra tên Phần hợp lệ (`PHAN_I` / `PHAN_II` / `PHAN_III` / `HEADER`), cảnh báo dạng:
`[TÊN PHẦN SAI] 'phan_i' không hợp lệ — phải là PHAN_I/PHAN_II/PHAN_III (viết HOA, có gạch dưới). Toàn bộ N nội dung trong phần này sẽ KHÔNG được điền.`

### Xung đột 3 — ghi nhận, KHÔNG sửa (có chủ ý)
`fill_report()` thay placeholder đỏ bằng nội dung đen — nên chạy lần 2 trên output sẽ không
tìm thấy placeholder để sửa. Đây là **hành vi đúng về mặt an toàn**: file đã điền là bản thảo
báo cáo, không nên cho phép ghi đè tự động (rủi ro mất nội dung đã biên tập tay).
**Quy trình đúng**: luôn chạy `fill_report()` từ FILE MẪU GỐC với `content_by_phase` đã cập nhật,
không chạy chồng lên output cũ. Đã ghi vào README.

## Kiểm thử — 24/24 PASS
Bổ sung 6 test sâu vào `test_regression_v34.py`:
- skeleton trả đúng 3 tầng + tương thích trực tiếp `fill_report()`
- Mục II có mặt trong khung nháp
- dict phẳng bị chặn với thông báo rõ ràng
- tên Phần sai được cảnh báo đúng nguyên nhân
- nội dung thật (số `1.049/1.200`, `87,4%`, ngoặc, `&`, `<`) giữ nguyên, không lỗi XML

Chạy: `python3 test_regression_v34.py`

## Khuyến nghị vận hành
1. **Luôn đọc mục `canh_bao`** trong kết quả trả về của cả 2 hàm — nhiều lỗi chỉ hiện ở đây, không làm chương trình dừng.
2. **Không chạy `fill_report()` chồng lên file output** — luôn xuất phát từ mẫu gốc.
3. Khung nháp từ `build_content_map_skeleton()` **chỉ là điểm khởi đầu**, không phải nội dung dùng được ngay.
