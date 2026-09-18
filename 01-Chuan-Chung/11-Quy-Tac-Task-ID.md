# Quy tắc Task_ID — KTC-Quan-tri

**Trạng thái:** Dự thảo để chốt · **Lập ngày:** 13/9/2026

## Vấn đề phải giải quyết trước tiên: hai lớp mã dễ bị nhầm

Dự án đang có sẵn hai hệ mã hoàn toàn khác bản chất. Nhầm hai lớp này sẽ làm hỏng toàn bộ Master Task Register.

| | Mã nhiệm vụ chuẩn | Task_ID |
|---|---|---|
| Ví dụ | `A01`, `E07`, `S04` | `KTC-2026-Q3-00125` |
| Trả lời câu hỏi | Đây là **loại** nhiệm vụ gì? | Đây là **lần giao việc** nào? |
| Số lượng | 122, cố định, thay đổi hiếm | Tăng liên tục theo mỗi kỳ |
| Ai sinh ra | `Du-lieu-Cong-Viec` (danh mục) | `KTC-Ke-Hoach` khi lập kế hoạch |
| Vòng đời | Không có trạng thái | Có trạng thái, có tiến độ, có minh chứng |
| Quan hệ | 1 mã chuẩn ↔ **N** Task_ID | 1 Task_ID ↔ **1** mã chuẩn (hoặc rỗng) |

**Mã nhiệm vụ chuẩn là thuộc tính phân loại của Task_ID, không phải định danh thay thế.** Hai nhiệm vụ khác
đơn vị, khác kỳ nhưng cùng bản chất công việc sẽ có **cùng** mã chuẩn `A01` và **khác** Task_ID.

## Cấu trúc Task_ID đề xuất

```
KTC-<năm>-<kỳ>-<số thứ tự>
KTC-2026-Q3-00125
```

| Thành phần | Quy tắc |
|---|---|
| `KTC` | Cố định |
| `<năm>` | 4 chữ số, năm của **kỳ kế hoạch**, không phải năm tạo bản ghi |
| `<kỳ>` | `Q1`–`Q4` (quý) · `T01`–`T12` (tháng) · `NAM` (nhiệm vụ cả năm) · `CD` (chuyên đề) |
| `<số thứ tự>` | 5 chữ số, cấp tuần tự **liên tục trong toàn Trường**, không cấp riêng theo đơn vị, không dùng lại số đã cấp kể cả khi nhiệm vụ bị hủy |

### Vì sao đánh số liên tục toàn Trường, không theo đơn vị

Nếu cấp số theo đơn vị (`...-THHC-001`), khi nhiệm vụ chuyển chủ trì từ Phòng này sang Phòng khác thì
hoặc phải đổi mã (vi phạm "một nhiệm vụ – một mã"), hoặc mã mang thông tin sai. Đơn vị chủ trì là **trường
dữ liệu**, không đưa vào mã.

## Bốn quy tắc bất biến

1. **Cấp một lần, không đổi, không tái sử dụng.** Nhiệm vụ bị hủy hoặc chuyển kỳ vẫn giữ nguyên Task_ID
   gốc; việc chuyển kỳ ghi ở trường trạng thái và lịch sử, không cấp mã mới.
2. **Chỉ `KTC-Ke-Hoach` được cấp Task_ID.** Theo dõi và Báo cáo không tự sinh mã.
3. **Nhiệm vụ phát sinh vẫn phải có Task_ID**, cấp sau khi đã ghi đủ nguồn, căn cứ, ngày phát sinh, đơn vị
   giao, đơn vị thực hiện, thời hạn, sản phẩm. Không đưa nhiệm vụ chưa có mã vào báo cáo.
4. **Nhiệm vụ con** dùng Task_ID riêng và trỏ về cha qua trường `Parent_Task_ID` — không dùng hậu tố kiểu
   `...-00125.1`, vì hậu tố khiến việc tách/gộp nhiệm vụ về sau phải sửa mã.

## Lỗ hổng đang tồn tại — chưa xử lý được

Phụ lục Ia/Ib của TB736 (nguồn dữ liệu kế hoạch mà `KTC-Bao-Cao` đang đọc) **không có cột mã nhiệm vụ**.
Vì vậy hiện chỉ đối chiếu được **gần đúng** giữa kế hoạch và báo cáo (theo Trục + so khớp tên nhiệm vụ),
chưa đối chiếu 1-1 chính xác.

Việc cần làm, theo đúng thứ tự: `KTC-Ke-Hoach` bổ sung cột `Task_ID` vào Phụ lục Ia/Ib → `KTC-Bao-Cao`
sửa `read_bc736_excel.py` để đọc và dùng cột này làm khóa nối. Đây là thay đổi nhỏ nhưng mở khóa toàn bộ
khả năng đối chiếu tự động của ba hệ.

Chi tiết kiểm chứng: `04-Tai-Lieu-Thiet-Ke/GHI-CHU-CAU-NOI-3-HE.md`.
