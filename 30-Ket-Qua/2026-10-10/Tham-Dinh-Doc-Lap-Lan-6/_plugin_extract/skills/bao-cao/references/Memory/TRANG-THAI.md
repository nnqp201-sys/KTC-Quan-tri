# TRẠNG THÁI HỆ KTC-RIS

> **Đọc file này ĐẦU TIÊN mỗi phiên.** Cập nhật ngay khi có thay đổi, không để cuối kỳ.
> Cập nhật lần cuối: **19/08/2026** — bởi phiên làm việc rà soát/vá script.

---

## 1. Phiên bản đang dùng

| Hạng mục | Trạng thái |
|---|---|
| Bản cài trong thư mục skill | **v2.5.1** (vá trong phiên 19/08/2026) |
| Bản đã đóng gói chờ cài vĩnh viễn | `ktc-bao-cao-v2_5_1.skill` |
| Bản khác đang có | `v3.0` (người dùng cung cấp 19/08/2026, chưa cài) |
| **CẢNH BÁO** | Bản vá trong phiên **KHÔNG tự lưu**. Nếu `SKILL.md` ghi v2.3 → bản vá đã mất, phải cài lại file `.skill` |

## 2. Việc đang treo — ưu tiên từ cao xuống thấp

| # | Việc | Trạng thái | Ghi chú |
|---|---|---|---|
| 1 | **Gộp v2.5.1 + v3.0 → v3.1** | ⏸ Chờ người dùng đồng ý | Đã phân tích xong, xem `04-Nhat-Ky-Quyet-Dinh.md` QĐ-05. Mỗi bản sửa được lỗi bản kia còn |
| 2 | Cài vĩnh viễn bản đã gộp | ⏸ Phụ thuộc #1 | Phải bấm "Save skill", gỡ bản cũ trước |
| 3 | Chạy kiểm thử trên **file Excel THẬT** của 14 đơn vị | ❌ Chưa làm | Toàn bộ 15 phép kiểm hiện chỉ chạy trên fixture mô phỏng |
| 4 | Xử lý tồn đọng dữ liệu kỳ tháng 8 | ❌ Chưa làm | Xem `03-Chat-Luong-Du-Lieu-Don-Vi.md` |
| 5 | Chuẩn bị kỳ tháng 9/2026 | ❌ Chưa bắt đầu | Bước 0 (checklist đơn vị) |

## 3. Kỳ báo cáo

| Kỳ | Trạng thái | Ghi chú |
|---|---|---|
| Tháng 7/2026 | ✅ Đã xuất báo cáo Word cấp Trường | Dựng thủ công bằng docx-js, **không qua script** → không dính 14 lỗi đã vá |
| Tháng 8/2026 | ⚠️ Đã có sản phẩm, còn tồn đọng dữ liệu | 2 đơn vị có vấn đề đã xác minh |
| Tháng 9/2026 | ⬜ Chưa bắt đầu | "Nhiệm vụ trọng tâm tháng 9" đã được nêu trong báo cáo tháng 8 |

## 4. Đang ở bước nào trong quy trình 7 bước

Hiện **ngoài chu kỳ báo cáo** — đang ở giai đoạn bảo trì công cụ (vá lỗi, tối ưu bộ nhớ).
Khi bắt đầu kỳ tháng 9, vào **Bước 0** (lập checklist đơn vị).

## 5. Ràng buộc môi trường cần nhớ

- Thư mục skill **ghi được trong phiên** nhưng **mất khi phiên kết thúc**. Muốn giữ: đóng gói `.skill` và cài qua giao diện.
- AI **chỉ tạo được file mới** trên Drive, không sửa/xóa/di chuyển được file có sẵn.
- Truy vấn Drive theo `parentId` (ID thư mục) đáng tin hơn theo `title`.

---

## Cách cập nhật file này

Sửa trực tiếp, giữ nguyên 5 mục trên. Mỗi lần sửa, đổi dòng "Cập nhật lần cuối".
Khi một việc treo hoàn thành: chuyển sang `01-Nhat-Ky-Chay.md` rồi xóa khỏi mục 2 —
để danh sách việc treo luôn ngắn và thật.
