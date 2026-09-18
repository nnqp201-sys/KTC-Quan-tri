# DL-20260914-003 — Gộp đầu vào của mọi hệ về một kho, tổ chức theo nguồn gốc dữ liệu

**Ngày:** 14/9/2026 · **Loại:** APPLY · **Người quyết định:** người phụ trách hệ
**Phạm vi ảnh hưởng:** từ hai hệ trở lên → bắt buộc ghi Decision Log

## Bối cảnh

Đầu vào trước đây tách theo **hệ tiêu thụ**: `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_<kỳ>/` và
`KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/`. Thiết kế này đúng khi dự án chỉ có hai hệ. Nay đã mở rộng
sang Theo dõi và Soạn thảo, và ba vấn đề đã đo được:

| Vấn đề | Bằng chứng |
|---|---|
| Tệp nằm sai nhánh so với hệ cần dùng | 12 tệp kế hoạch tháng 9/2026 nằm ở `Nhap_Bao_Cao/`, vì đơn vị nộp gộp báo cáo tháng 8 và kế hoạch tháng 9 cùng một lần |
| Thư mục dựng sẵn phần lớn bỏ trống | `input-KH_Nam` 14/15 rỗng · `input-KH_Quy` 13/14 rỗng · `input-KH_Thang` 1/1 rỗng — tổng **28 thư mục rỗng** |
| Nguồn dữ liệu mới không có chỗ | Kết luận giao ban tuần của Lãnh đạo Trường — nguồn thứ 3 của kế hoạch tháng — không thuộc nhánh nào |

## Quyết định

Lập **`11-Du-Lieu-Dau-Vao/`** cấp dự án, tổ chức theo **nguồn gốc dữ liệu**, không theo hệ tiêu thụ:
`01-Dau-Moi-Nop/` · `02-Cap-Truong/` · `03-Ket-Luan-Giao-Ban/` · `04-Van-Ban-Cap-Tren/` ·
`09-Chua-Phan-Loai/`.

Bốn nguyên tắc kèm theo:

1. **Một tệp nằm đúng một chỗ**; hệ nào cần thì đọc từ đó, không nhân bản sang nhánh riêng.
2. **Kế hoạch và báo cáo của cùng đầu mối, cùng kỳ để CHUNG** — không tách hai nhánh.
3. **Chỉ tạo thư mục khi có dữ liệu.** Thư mục rỗng không còn nghĩa là "chưa nộp".
4. **Tên thư mục đầu mối dùng mã chuẩn**, không ghi tên tự do.

## Lý do từng nguyên tắc

**Nguyên tắc 2** đến từ hành vi thật của đơn vị, không từ mong muốn thiết kế: họ nộp một lần cả hai loại.
Tách ra tạo việc phân loại thủ công mà không ai được lợi, và đã sinh đúng lỗi ở kỳ tháng 9/2026.

**Nguyên tắc 3** đến từ một lỗi đọc sai đã thực sự xảy ra. Cây thư mục dựng sẵn 14 đơn vị khiến người đọc
kết luận "13 đơn vị chưa nộp kế hoạch năm", trong khi sự thật là kỳ đó chưa mở. Thư mục rỗng **nói dối**
một cách im lặng — cùng loại lỗi với `BH-02` (lỗi không báo lỗi).

**Nguyên tắc 4** vì cùng một đơn vị đang có ba kiểu viết tên trong dự án, một kiểu sai chính tả
(`Phong-TCCB-CTHHSV` thừa chữ `H`). Dùng mã chuẩn ngay từ thư mục là chỗ rẻ nhất để chặn.

## Hệ quả kèm theo

- `Skill 34` (Pre-flight), `Workflow 10`, `Prompt 00` và `SKILL.md` của `KTC-Ke-Hoach` đã sửa đường dẫn;
  gói `ktc-ke-hoach-v3.2.skill` đã đóng lại.
- **Pre-flight đổi cách kiểm:** trước đây đếm thư mục con để biết ai chưa nộp; nay phải đối chiếu với
  **danh sách 13 mã**, vì thư mục chỉ tồn tại khi có dữ liệu.
- 3 tệp thật của nhánh kế hoạch đã chép sang `02-Cap-Truong/`, tên chuẩn hóa theo quy ước tiếng Việt không
  dấu. Tên cũ `01. CTCT n#U0103m 2026 update.xlsx` là lỗi mã hóa của Google Drive (`#U0103` = `ă`).
- 28 thư mục rỗng để người dùng tự xóa — danh sách tại
  `12-Output/2026-09-14/Danh-muc-can-don-thu-muc-input-KH.md`.

## Việc CHƯA làm — nói rõ để không tưởng đã xong

`KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/` còn **khoảng 40 tệp dữ liệu thật** của kỳ tháng 8–9/2026,
**chưa chuyển**. Ba lý do: đây là dữ liệu vận hành đang dùng; hai công cụ `tools/trich_tuong_thuat.py` và
`tools/build_xl.py` ghi cứng đường dẫn cũ; và cần quy ước đặt tên để phân biệt tệp kế hoạch với tệp báo
cáo khi hai loại nằm chung một thư mục đầu mối.

**Trong thời gian quá độ, kho mới chưa phải nguồn duy nhất.** Mọi kết quả đọc từ đầu vào phải nói rõ đang
đọc kho nào.

**Liên quan:** `PM-20260914-Chay-thu-KH-thang-9` · `KI-004` · `KI-006` ·
`36-Skill-Tong-Hop-Ke-Hoach-Truong.md` (bảng Bốn nguồn) · `11-Du-Lieu-Dau-Vao/00-README.md`
