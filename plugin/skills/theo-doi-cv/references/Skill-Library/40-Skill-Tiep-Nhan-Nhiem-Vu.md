# 40-Skill-Tiep-Nhan-Nhiem-Vu
## Phiên bản: v1.0 — 14/9/2026

## Purpose
Nhận nhiệm vụ đã có `Task_ID` từ `ktc-ke-hoach`, kiểm tính hợp lệ, phân công và **khóa baseline**.

## Trigger conditions
- Kế hoạch kỳ mới được ban hành và đã cấp `Task_ID`.
- Có nhiệm vụ phát sinh vừa được `ktc-ke-hoach` cấp mã.

## Bốn phép kiểm cổng vào — thiếu một là KHÔNG nhận

| # | Kiểm | Không đạt thì làm gì |
|---|---|---|
| 1 | Có `Task_ID` đúng dạng `KTC-YYYY-Qn-NNNNN` | Trả về `ktc-ke-hoach` cấp mã, không tự đặt |
| 2 | `Task_ID` **chưa tồn tại** trong bảng Nhiệm vụ | Đã có → cập nhật, **không tạo dòng mới** |
| 3 | Có đơn vị chủ trì bằng **mã chuẩn** | Ghi `[CẦN XÁC ĐỊNH]`, trạng thái giữ ở *Mới* |
| 4 | Có thời hạn cụ thể | Ghi `[CẦN BỔ SUNG]`, trạng thái giữ ở *Mới* |

> **Một nhiệm vụ – một Task_ID.** Cùng một việc xuất hiện ở hai kế hoạch thì vẫn là một dòng, ghi thêm
> nguồn thứ hai vào cột Ghi chú. Tạo hai dòng là phá vỡ khả năng truy ngược của báo cáo.

## Khóa baseline

Khi chuyển sang *Đã giao*, ghi đồng thời `Hạn baseline` và `Hạn hiện hành` **bằng nhau**, rồi đặt
`Khóa baseline = Có`. Từ lúc đó:

- `Hạn baseline` **không bao giờ sửa trực tiếp** — chỉ đổi qua Skill 44 có phê duyệt.
- `Hạn hiện hành` thay đổi theo quyết định điều chỉnh đã duyệt.
- Chênh lệch giữa hai cột chính là **số lần và mức độ trượt tiến độ** — dữ liệu đầu vào của báo cáo.

Mất baseline là mất khả năng nói "việc này đã lùi hạn mấy lần".

## Nhiệm vụ phát sinh — luồng riêng

Nhiệm vụ chưa có trong kế hoạch **không được nhận thẳng**. Ghi đủ 7 trường rồi chuyển `ktc-ke-hoach`:
nguồn phát sinh · căn cứ · ngày phát sinh · đơn vị giao · đơn vị thực hiện · thời hạn · sản phẩm.

Nguồn phát sinh hợp lệ đã biết: **kết luận giao ban tuần của Lãnh đạo Trường** · văn bản cấp trên ban hành
trong kỳ · chỉ đạo trực tiếp của Hiệu trưởng. Xem `11-Du-Lieu-Dau-Vao/00-README.md` nhánh 03 và 04.

## Related
- `01-Chuan-Chung/11-Quy-Tac-Task-ID.md` — quy tắc cấp mã (bản gốc)
- `01-Chuan-Chung/13-Bang-Ma-Don-Vi.md` — mã đơn vị chuẩn
- `41-Skill-Cap-Nhat-Tien-Do.md` — bước tiếp theo
