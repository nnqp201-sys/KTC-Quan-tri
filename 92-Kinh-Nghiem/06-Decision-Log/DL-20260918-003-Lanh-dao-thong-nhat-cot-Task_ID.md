# DL-20260918-003 — Lãnh đạo Trường thống nhất bổ sung cột Task_ID vào Phụ lục TB736 (KI-001)

**Ngày:** 18/9/2026 · **Người quyết định:** Lãnh đạo Trường (người dùng báo lại: "Lãnh đạo Trường đã thống
nhất việc 2") · **Căn cứ trình:** `30-Ket-Qua/2026-09-18/De-xuat/Phieu-de-xuat_Bo-sung-cot-Task_ID-Phu-luc-TB736.docx`

| Trường | Giá trị |
|---|---|
| Giá trị cũ | Phụ lục Ia/Ib/IIb/IIc không có cột mã nhiệm vụ; đối chiếu KH ↔ BC gần đúng theo tên |
| Giá trị mới | Thêm cột `Task_ID` vào **cuối** bảng: Ia/Ib cột L, IIb/IIc cột R; mã `KTC-<năm>-<kỳ>-<5 số>` |
| Lý do | Kỳ 8/2026: 7/19 nhiệm vụ không đối chiếu được, có nhiệm vụ đã hoàn thành thật |
| Chưa chốt | Thời điểm áp dụng (kỳ nào) và văn bản điều chỉnh mẫu TB736 — chưa có thông tin; phòng TH-HC&QT tham mưu |

## Đã thực hiện phần thuộc hệ (18/9/2026)
- `read_bc736_excel.py` v3.3 (gói `ktc-bao-cao-v3.8.skill`): đọc cột theo **tên tiêu đề** (không theo chỉ số
  cố định — bền hơn thiết kế `row[11]/row[16]` trong đề xuất, cho kết quả như nhau khi cột ở cuối); cảnh báo
  sai định dạng/trùng mã; tệp chưa có cột → `task_id = None`, giữ đối chiếu gần đúng.
- Phát hiện kèm và sửa: nhiệm vụ có số TT mà nội dung bắt đầu "Tổng hợp/Tổng kết…" bị coi là dòng cộng và
  **bỏ mất** (2 nhiệm vụ thật của DT-CDCS kỳ 9/2026).
- Hồi quy `test_task_id_bc736.py`: 26 tệp thật — không mất gì so với v3.2, lấy lại đúng 2 nhiệm vụ, 2 ca ngược.

## Chưa làm (chờ)
- Đổi hành vi đối chiếu mặc định sang khóa `Task_ID`: chờ bộ dữ liệu thật đầu tiên có cột.
- `KTC-Ke-Hoach` cấp mã: từ kỳ áp dụng do Lãnh đạo/phòng TH-HC&QT xác định.
