# 18 — Chuẩn thể thức, kỹ thuật trình bày sản phẩm .docx/.xlsx

**Ban hành:** 19/9/2026 · **Quyết định:** DL-20260919-003 · **Hiệu lực:** **mọi** tệp `.docx`/`.xlsx` do KTC-Quan-tri
(5 skill và skill `the-thuc`) sinh ra, kể cả khi dựng bằng skill `docx`/`xlsx` của Anthropic.

**Nguồn số đo** (đo byte thật bằng python-docx/openpyxl ngày 19/9/2026, không suy diễn):
- 16 mẫu trống `KTC-Database/03-Templates(1)/` (15 `.dotx` + 1 `.xltx`).
- Văn bản đã ban hành trong `KTC-Database/04-Good-Documents/`.
- NĐ 30/2020/NĐ-CP, Phụ lục I, và TB 597/TB-CĐKT ngày 19/5/2026. Tra hai văn bản này qua 897:
  `Checklist/05-Hinh-Thuc.md` và `Checklist/08-Quy-Uoc-Rieng-CDKT.md` mục 4.

Công cụ đo: `29-Cong-Cu/kiem_the_thuc.py` (bản sao `scripts/kiem_the_thuc.py` trong skill `the-thuc`). Trong Code,
hook `ktc_the_thuc_hook.py` tự đo mọi tệp `.docx`/`.xlsx` vừa sinh ra.

---

## 1. Thứ tự dựng sản phẩm — không bao giờ từ tệp trống

| Ưu tiên | Nguồn | Dùng để |
|---|---|---|
| 1 | **Văn bản cùng loại đã ban hành** trong `04-Good-Documents/` (NT-1, `14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`) | Cấu trúc, văn phong, thể thức |
| 2 | **Mẫu trống** `.dotx`/`.xltx` trong `03-Templates(1)/`, theo bảng mục 2 | Thể thức, style, lề, bảng quốc hiệu |
| 3 | Dựng mới bằng skill `docx`/`xlsx` | **Chỉ khi** không có 1 và 2. Bắt buộc đặt đủ số đo mục 3–4 |

- **Cấm** dùng `docx.Document()` rỗng (python-docx mặc định khổ **Letter**, phông Calibri) hoặc docx-js với lề
  mặc định (2,54 cm cả bốn lề). Sản phẩm `Phieu-de-xuat_Bo-sung-cot-Task_ID…docx` ngày 18/9/2026 ra khổ Letter
  21,6×27,9 cm chính vì lỗi này.
- Mở mẫu `.dotx`/`.xltx` thành tệp làm việc: `python kiem_the_thuc.py --tao <mẫu> <đích.docx|.xlsx>`. Lệnh này
  giữ nguyên style, lề và bảng thể thức. Không mở `.dotx` bằng cách đổi đuôi tên tệp.
- `03-Templates/` (không có `(1)`) **không phải** kho mẫu: phần lớn là văn bản thật. Xem
  `22-KTC-Dieu-Phoi/references/02-Chi-Muc-KTC-Database.md`.

## 2. Bảng chọn mẫu theo loại sản phẩm

| Sản phẩm | Mẫu trống `03-Templates(1)/` | Văn bản tốt `04-Good-Documents/` |
|---|---|---|
| Quyết định ban hành quy chế, quy định | `01-Quyet-dinh-ban-hanh-Quy-che.dotx` | `04-01- Quyet dinh ban hanh Quy che, Quy dinh/` · kho `02-KTC-Regulations` |
| Quyết định cá biệt (phê duyệt, dự toán) | `02A-Quyet-dinh-ca-biet-Phe-duyet-nhiem-vu-du-toan.dotx` | `04-02- Quyet dinh ca biet/` |
| Quyết định bổ nhiệm | `02B-Quyet-dinh-ca-biet-Bo-nhiem.dotx` | `04-02- Quyet dinh ca biet/` |
| Thông báo hướng dẫn đăng ký KH/BC | `03A-Thong-bao-Huong-dan-dang-ky-ke-hoach-bao-cao.dotx` | `04-03- Thong bao/06. TB 736…` |
| Thông báo kết luận giao ban | `03B-Thong-bao-Ket-luan-giao-ban.dotx` | `04-03- Thong bao/T5.TBKL…` |
| Kế hoạch trung hạn, chuyên đề | `04-Ke-hoach-trung-han.dotx` | `04-04- Chien luoc + Ke hoach trung han/` · `02-KTC-Regulations/02-04- Ke hoach CHUYEN DE/` |
| Kế hoạch thực hiện công việc | `05A-Ke-hoach-thuc-hien-cong-viec.dotx` | `04-05- Ke hoach thuc hien cong viec/` |
| **Kế hoạch công tác tháng/quý (.xlsx)** | `05B-Ke-hoach-cong-tac-thang.xltx` | `04-03- Thong bao/5. TB 736. Phu luc Ia, Ib, IIb, IIc…xlsx` |
| Báo cáo nội bộ | `06A-Bao-cao-noi-bo.dotx` | `04-06-01- Bao cao noi bo/` |
| **Báo cáo tháng/quý/năm theo Quy chế làm việc** | `06B-Bao-cao-theo-Quy-che-lam-viec.dotx` | `04-06-02-…/BC-375-BC-CDKT…docx`; phụ lục KPI `PL-KPI-BC-375…xlsx` |
| Báo cáo chuyên đề | `06C-Bao-cao-chuyen-de.dotx` | `04-06-03- Bao cao chuyen de/` |
| Hướng dẫn xây dựng KH/BC | `06D-Huong-dan-xay-dung-ke-hoach-bao-cao.dotx` | — |
| Tờ trình | `07-To-trinh.dotx` | `04-07- To trinh/` |
| Công văn | `08-Cong-van.dotx` | `04-08- Cong van/` |
| Biên bản | `09-Bien-ban.dotx` | `04-09- Bien Ban/` |
| Giấy mời | `10-Giay-moi.dotx` ⚠️ lỗi mẫu (mục 6) | `04-10- Giay moi/` |
| Chương trình, phiếu trình, đề án | — (dựng theo mục 3) | `04-11- Chuong trinh/` · `04-13- Phieu trinh/` · `04-12- De an/` |

Báo cáo tổng hợp tháng cấp Trường dùng mẫu chính thức
`25-KTC-Bao-Cao/00. Mau bao cao thang (cap Truong).docx`, khuôn của `fill_bc736.py` và `build_bc2.py`. Mẫu này
được ưu tiên trước `06B`. Mẫu có chữ màu (đánh dấu chỗ cần điền), nên phải đổi sang màu đen trước khi giao (TT05).

## 3. Số đo bắt buộc — .docx (văn bản hành chính, hệ A)

| Thông số | Giá trị | Mã kiểm | Mức khi sai |
|---|---|---|---|
| Khổ giấy | **A4 21×29,7 cm** (docx-js: `width 11906, height 16838` DXA) | TT01 | 2 |
| Lề | **trên 2 · dưới 2 · trái 3 · phải 2 cm** (DXA `1134/1134/1701/1134`); NĐ 30 cho phép trên, dưới 2–2,5 · trái 3–3,5 · phải 1,5–2 | TT02 | 2 nếu ngoài khoảng |
| Phông | **Times New Roman**, Unicode, cho **mọi** đoạn chữ, kể cả trong bảng. Cấm `.VnTime` (TCVN3). Biến thể tên như "Times New Roman Bold" hay "TimesNewRomanPSMT" thì đặt lại đúng tên | TT03 · TT03b | 2 · 3 |
| Cỡ chữ nội dung | **14**, thống nhất một cỡ trong toàn văn bản | TT04 · TT04b | 2 · 3 |
| Màu chữ | Đen | TT05 | 3 |
| Dàn lề nội dung | Đều hai lề; thụt đầu dòng 1–1,27 cm; cách đoạn ≥ 6 pt | TT06 | 3 |
| Cách dòng | Từ single hoặc exactly 15 pt đến 1,5 lines | TT07 | 3 |
| Phần đầu | Bảng hai cột: `UBND TỈNH QUẢNG NGÃI` / **`TRƯỜNG CAO ĐẲNG KON TUM`** (cỡ 13, đậm) · Quốc hiệu cỡ 13, đậm · Tiêu ngữ cỡ 14, đậm, kẻ bằng Draw | TT08 · TT09 | 2 |
| "Nơi nhận" | Cỡ 12, nghiêng, đậm; danh sách nơi nhận cỡ 11 | TT10 | 3 |
| Số trang | Canh giữa ở lề trên, không hiện ở trang 1 | TT11 | 3 |

Cỡ chữ của các thành phần còn lại (số ký hiệu, tên loại, trích yếu, chữ ký) lấy theo bảng 16 dòng tại 897
`08-Quy-Uoc-Rieng-CDKT.md` mục 4. **Không chép bảng đó vào đây.**

## 4. Số đo bắt buộc — .xlsx (kế hoạch, phụ lục, bảng KPI)

Đo từ `05B-Ke-hoach-cong-tac-thang.xltx` và Phụ lục TB 736:

| Thông số | Giá trị | Mã kiểm | Mức |
|---|---|---|---|
| Khổ in | **A4** (`paperSize = 9`) | TX01 | 2 |
| Phông | **Times New Roman** cho mọi ô có dữ liệu. Skill `xlsx` cho phép Arial, **ở đây không** | TX02 | 2 |
| Cỡ chữ | 12–14 (mẫu 05B: 14 cho dữ liệu, 13 cho ghi chú) | TX03 | 3 |
| Hướng in | Bảng trên 6 cột: **A4 ngang** hoặc đặt vừa chiều rộng trang. Lề mẫu 05B: trên 0,59″ · dưới, trái, phải 0,5″ | TX04 | 4 |
| Cấu trúc | Sửa tệp của đơn vị thì giữ nguyên cột, công thức và vùng gộp của mẫu TB 736. Cột `Task_ID` đọc theo tên tiêu đề (DL-20260918-003) | — | — |

## 5. Kiểm trước khi giao — bắt buộc

1. Chạy `python kiem_the_thuc.py <tệp>` với từng tệp `.docx`/`.xlsx`.
2. Còn **Mức 1–2** thì **sửa rồi đo lại**. Không giao tệp còn lỗi Mức 1–2.
3. Ghi kết quả đo vào phiếu tự kiểm (Nguyên tắc 3) hoặc cuối câu trả lời: `Thể thức: đạt (kiem_the_thuc, 0 lỗi Mức 1–2)`.
4. Nền tảng không chạy được Python thì ghi `FORMAT_BINARY_UNVERIFIED`. Không tuyên bố đạt chuẩn khi chưa đo.
5. Tầng thể thức này **không thay** rà soát 897 trước khi trình ký.

## 6. Lỗi đã biết trong kho mẫu (không tự sửa kho; đề xuất tại `30-Ket-Qua/2026-09-19/De-xuat/`)

| Mẫu | Lỗi | Xử lý khi dùng |
|---|---|---|
| `10-Giay-moi.dotx` | Cơ quan chủ quản ghi "UBND TỈNH KON TUM"; tiêu ngữ lẫn cỡ 13 và 14 | Đổi thành `UBND TỈNH QUẢNG NGÃI`, tiêu ngữ cỡ 14 |
| Nhiều văn bản trong `04-Good-Documents` trước sáp nhập | "UBND TỈNH KON TUM", có tệp còn `.VnTime` | Chỉ lấy văn phong và cấu trúc; thể thức theo mục 3 |

Theme của các mẫu có `themeFontLang = vi-VN`. Vì vậy phông "major" của theme hiển thị là **Times New Roman**, không
phải Calibri Light. `kiem_the_thuc.py` đã giải phông theo cách này, **không** báo lỗi.
