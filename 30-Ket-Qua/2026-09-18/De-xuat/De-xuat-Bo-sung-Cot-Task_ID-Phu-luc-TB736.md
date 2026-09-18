# Đề xuất bổ sung cột Task_ID vào Phụ lục Ia/Ib/IIb/IIc (TB736)

**Ngày dựng:** 18/9/2026 · **Loại:** Đề xuất kỹ thuật, chưa áp dụng · **Giải quyết:** `KI-001`
**Người/đơn vị cần quyết định:** đơn vị chủ trì `KTC-Ke-Hoach` + `KTC-Bao-Cao` (thay đổi ảnh hưởng biểu mẫu
dùng chung toàn Trường, cần thống nhất trước khi áp dụng cho kỳ kế hoạch tiếp theo)

> **⚠️ Chưa đối chiếu với kho 01-04 để xin phép sửa mẫu** — đây là đề xuất kỹ thuật dựa trên đối chiếu cấu
> trúc mẫu đã ban hành và mã nguồn đang chạy, không phải văn bản có hiệu lực. Không tự áp dụng vào mẫu
> chính thức hay vào `KTC-Ke-Hoach` khi chưa có xác nhận.

## Vấn đề

`KI-001`: Phụ lục Ia/Ib (nguồn kế hoạch) không có cột mã nhiệm vụ, nên `KTC-Bao-Cao` chỉ đối chiếu được
**gần đúng** kế hoạch ↔ báo cáo (theo Trục + so khớp tên). Đã đo tác hại thật: 7/19 nhiệm vụ đến hạn tháng
8/2026 "không tìm thấy" khi đối chiếu, trong đó có nhiệm vụ đã hoàn thành thật. `01-Chuan-Chung/11-Quy-Tac-Task-ID.md`
đã nêu hướng khắc phục ở mức nguyên tắc; đề xuất này cụ thể hoá thành thiết kế sẵn sàng áp dụng.

## Đối chiếu cấu trúc mẫu thật (đọc trực tiếp `06. TB 736 Phu luc Ia,Ib,IIb,IIc - Mau ke hoach, bao cao.xlsx`
tại `KTC-Database/02-KTC-Regulations/`, 18/9/2026)

| Phụ lục | Số cột hiện tại | Cột cuối hiện tại | Dòng tiêu đề bảng |
|---|---|---|---|
| Ia (KH Quý) | 11 (A–K) | K = Ghi chú | Dòng 6 |
| Ib (KH tháng) | 11 (A–K) | K = Ghi chú | Dòng 6 |
| IIb (BC tháng) | 17 (A–Q) | Q = (không tiêu đề, thuộc nhóm KPI tiến độ) | Dòng 6–7 (tiêu đề gộp 2 dòng) |
| IIc (BC quý) | 17 (A–Q) | Q | Dòng 6–7 |

`KTC-Bao-Cao/references/Skill-Library/read_bc736_excel.py` (v3.2) đọc dữ liệu theo **chỉ số cột cố định**
(`row[0]`…`row[10]` cho Ia/Ib, `row[0]`…`row[15]` cho IIb/IIc), không đọc theo tên tiêu đề. => **Chèn cột
mới ở giữa bảng sẽ làm lệch toàn bộ chỉ số và phá script đang chạy.** Đây là ràng buộc kỹ thuật quan trọng
nhất của đề xuất này.

## Thiết kế đề xuất

**Thêm cột `Task_ID` làm cột cuối cùng mới** của cả 4 mẫu — không chèn giữa bảng:

| Phụ lục | Cột `Task_ID` mới | Chỉ số đọc mới trong `read_bc736_excel.py` |
|---|---|---|
| Ia, Ib | L (cột thứ 12) | `row[11]` |
| IIb, IIc | R (cột thứ 18) | `row[16]` |

Vì chỉ **thêm vào cuối**, mọi chỉ số `row[0]`…`row[15]` hiện có của script **không đổi** — đây là thay đổi
cộng thêm, không phải thay đổi phá vỡ. Khi cột chưa tồn tại (file kỳ cũ), `row[11]`/`row[16]` tự nhiên là
`None` — script chỉ cần xử lý `None` như "chưa có Task_ID", không lỗi.

**Định dạng giá trị:** đúng theo `01-Chuan-Chung/11-Quy-Tac-Task-ID.md` đã có sẵn — `KTC-<năm>-<kỳ>-<số thứ
tự 5 chữ số>`, ví dụ `KTC-2026-Q3-00125`. Không định nghĩa lại ở đây.

**Ai điền, điền khi nào** (áp theo nguyên tắc bất biến #1–#2 của dự án — kế hoạch là nguồn sinh nhiệm vụ):
1. `KTC-Ke-Hoach` cấp `Task_ID` khi nhiệm vụ **lần đầu** được đưa vào Phụ lục Ia (kế hoạch quý) hoặc trực
   tiếp vào Ib nếu là nhiệm vụ phát sinh trong tháng, chưa từng có ở kế hoạch quý.
2. Khi kế hoạch quý được chi tiết hoá thành kế hoạch tháng (Ia → Ib), `Task_ID` của nhiệm vụ **giữ nguyên**,
   không cấp lại.
3. `KTC-Theo-doi-CV` và `KTC-Bao-Cao` (Phụ lục IIb/IIc) **chỉ sao chép** `Task_ID` đã có từ kế hoạch tương
   ứng — không tự sinh mã mới, không tự sửa mã.
4. Nhiệm vụ phát sinh không có trong kế hoạch: vẫn phải qua `KTC-Ke-Hoach` cấp mã trước khi đưa vào báo cáo
   (đúng nguyên tắc bất biến #4), không được để trống rồi tự đối chiếu gần đúng như hiện nay.

## Việc cần sửa ở `read_bc736_excel.py` (chỉ mô tả — CHƯA sửa code trong đề xuất này)

- Đọc thêm `row[11]` (Ia/Ib) / `row[16]` (IIb/IIc) làm `task_id`, gắn vào từng nhiệm vụ trong `content_map`.
- Khi `task_id` có giá trị ở cả hai phía kế hoạch và báo cáo: đối chiếu **theo khóa `Task_ID`**, bỏ cách so
  khớp gần đúng theo tên (đang có ngưỡng lỗi giả đã đo được ở `KI-001`/`PM-20260914-Chay-thu-KH-thang-9`).
- Khi `task_id` rỗng ở một hoặc cả hai phía (dữ liệu kỳ cũ, hoặc đơn vị chưa cập nhật mẫu mới): **giữ
  nguyên đường đối chiếu gần đúng hiện tại làm phương án dự phòng**, và bắt buộc tự khai "đối chiếu gần
  đúng" như quy ước đang áp dụng — không thay đổi hành vi đã có cho dữ liệu chưa có mã.
- Cần bộ dữ liệu thật có cột `Task_ID` để viết ca hồi quy trước khi đổi hành vi mặc định.

## Lộ trình áp dụng đề xuất (không tự triển khai)

1. Người có thẩm quyền xác nhận thiết kế cột (vị trí L / R, định dạng mã) — hoặc chỉnh nếu cần.
2. `KTC-Ke-Hoach` thêm cột vào mẫu làm việc nội bộ (không sửa file gốc trong `KTC-Database`, kho đó chỉ
   đọc) và bắt đầu cấp `Task_ID` từ kỳ kế hoạch tiếp theo.
3. Sửa `read_bc736_excel.py` theo mô tả trên, kèm ca hồi quy dùng dữ liệu thật có `Task_ID`.
4. Dữ liệu các kỳ trước khi áp dụng (`BC-375`, `PL-375`, `KH-834`…) **không hồi tố** — tiếp tục đối chiếu
   gần đúng và tự khai như vậy, đúng nguyên tắc "không suy đoán, không tự sửa dữ liệu gốc".

## Nguồn đã đối chiếu

- `KTC-Database/02-KTC-Regulations/06. TB 736 Phu luc Ia,Ib,IIb,IIc - Mau ke hoach, bao cao.xlsx` (đọc trực
  tiếp bằng `openpyxl`, 18/9/2026) — mẫu chính thức, kho chỉ đọc.
- `KTC-Bao-Cao/references/Skill-Library/read_bc736_excel.py` v3.2 (19/08/2026) — mã đang chạy.
- `01-Chuan-Chung/11-Quy-Tac-Task-ID.md` — quy tắc định dạng mã đã có, dùng nguyên, không định nghĩa lại.
