# 10-Dau-Vao — Kho dữ liệu đầu vào dùng chung của KTC-Quan-tri

> **18/9/2026 (`DL-20260918-005`):** `02-Cap-Truong/` chia `01-Nam/02-Quy/03-Thang/04-Chuyen-De`; bỏ
> `04-Van-Ban-Cap-Tren/` (văn bản cấp trên lưu ở `KTC-Database/01-Legal-Database/`). Nơi lưu từng loại, cách tìm
> KTC-Database, quy tắc Google Drive: **Nguyên tắc 4** tại `20-Chuan-Chung/00-Nguyen-Tac-Chung.md`.

**Lập ngày:** 14/9/2026 · **Thay thế:** `23-KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_*`

## Vì sao gộp về một chỗ

Cấu trúc cũ tách đầu vào theo **hệ tiêu thụ**: `Nhap_Ke_Hoach/` cho KTC-Ke-Hoach, `Nhap_Bao_Cao/` cho
KTC-Bao-Cao. Cách này đúng khi dự án chỉ có hai hệ, nhưng nay đã mở rộng sang Theo dõi và Soạn thảo, và
đã lộ ba vấn đề đo được:

| Vấn đề | Bằng chứng |
|---|---|
| Cùng một tệp phục vụ nhiều hệ nhưng chỉ nằm ở một nhánh | 12 tệp kế hoạch tháng 9/2026 nằm trong `25-KTC-Bao-Cao/Nhap_Bao_Cao/`, vì đơn vị nộp gộp báo cáo tháng 8 và kế hoạch tháng 9 cùng một lần |
| Thư mục dựng sẵn theo đơn vị phần lớn bỏ trống | `input-KH_Nam` 14/15 thư mục rỗng · `input-KH_Quy` 13/14 rỗng · `input-KH_Thang` 1/1 rỗng |
| Nguồn dữ liệu mới không có chỗ | Kết luận giao ban tuần của Lãnh đạo Trường — nguồn thứ 3 của kế hoạch tháng — không thuộc nhánh nào |

## Bốn nguyên tắc của kho này

1. **Tổ chức theo NGUỒN GỐC dữ liệu, không theo hệ tiêu thụ.** Một tệp nằm đúng một chỗ; hệ nào cần thì
   đọc từ đó. Không nhân bản sang nhánh của từng hệ.
2. **Đơn vị nộp gì thì để chung kỳ đó.** Không tách kế hoạch và báo cáo thành hai nhánh — thực tế đơn vị
   nộp gộp, tách ra là tạo việc phân loại thủ công không cần thiết.
3. **Chỉ tạo thư mục khi có dữ liệu.** Không dựng sẵn cây thư mục rỗng. Thư mục rỗng làm người đọc tưởng
   đơn vị chưa nộp, trong khi thật ra kỳ đó chưa bắt đầu.
4. **Tên thư mục đầu mối dùng mã chuẩn** theo `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` — không ghi tên tự do.

## Cấu trúc

```
10-Dau-Vao/
├── 00-README.md                 ← tệp này
├── 01-Dau-Moi-Nop/              Hồ sơ do 13 đầu mối nộp, xếp theo kỳ
│   └── <kỳ>/<mã đầu mối>/       ví dụ: 2026-09/P-THHC/
├── 02-Cap-Truong/               Văn bản cấp Trường đã ban hành — bản làm việc theo kỳ
│   ├── 00-Danh-Muc-Tro-KTC-Database.md   đối chiếu với KTC-Database, ngoại lệ đã duyệt
│   └── 01-Nam/<YYYY>/ · 02-Quy/<YYYY-Qn>/ · 03-Thang/<YYYY-MM>/ · 04-Chuyen-De/<YYYY-CD-ten>/
├── 03-Ket-Luan-Giao-Ban/        Thông báo kết luận giao ban tuần của Lãnh đạo Trường
│   └── <năm>/
└── 09-Chua-Phan-Loai/           Chỗ thả tạm — dọn sau mỗi kỳ, không để tồn
```

### Quy ước tên kỳ

| Loại kỳ | Dạng | Ví dụ |
|---|---|---|
| Năm | `YYYY` | `2026` |
| Quý | `YYYY-Qn` | `2026-Q3` |
| Tháng | `YYYY-MM` | `2026-09` |
| Chuyên đề | `YYYY-CD-<tên-ngắn>` | `2026-CD-Tuyen-sinh` |

### 13 đầu mối nộp

`P-THHC` · `P-TCCB` · `P-QLDT` · `P-QLKH` · `P-TCKT` · `K-KHCB` · `K-SUPH` · `K-KTNL` · `K-KTCN` ·
`K-YDUOC` · `K-DTSHLX` · `DT-CDCS` (Công đoàn cơ sở) · `DT-DTN` (Đoàn TN – Hội Sinh viên).

Ban Truyền thông **không** là đầu mối riêng — hồ sơ của Ban để trong `P-THHC/` (xem `KI-004`).

## Bốn nhánh dùng để làm gì

| Nhánh | Ai nạp | Hệ nào đọc |
|---|---|---|
| `01-Dau-Moi-Nop/` | Đầu mối nộp theo kỳ | Kế hoạch (đề xuất), Báo cáo (kết quả), Theo dõi (tiến độ, minh chứng) |
| `02-Cap-Truong/` | Phòng TH-HC&QT sau khi văn bản được ban hành | Kế hoạch (nguồn 1: trích kế hoạch quý), Báo cáo (đối chiếu), Theo dõi (baseline) |
| `03-Ket-Luan-Giao-Ban/` | Phòng TH-HC&QT, hằng tuần | Kế hoạch (**nguồn 3**), Báo cáo (căn cứ nhiệm vụ phát sinh) |
| ~~`04-Van-Ban-Cap-Tren/`~~ → `KTC-Database/01-Legal-Database/` | Nạp qua `KTC-Database/11-Input/` (18/9/2026, `DL-20260918-005`) | Kế hoạch (**nguồn 2**), Soạn thảo (căn cứ) |

> Hai nhánh `03` và `04` là **nguồn 2 và 3 của kế hoạch tháng** — xem
> `23-KTC-Ke-Hoach/references/Skill-Library/36-Skill-Tong-Hop-Ke-Hoach-Truong.md`, bảng "Bốn nguồn".
> Trước 14/9/2026 hai nguồn này không có chỗ lưu, nên khi dựng kế hoạch tháng phải đi tìm thủ công.

## Quan hệ với `KTC-Database`

`KTC-Database` là **kho đã ban hành, chỉ đọc** — văn bản pháp lý, quy chế, mẫu, văn bản tốt.
`10-Dau-Vao` là **kho đang xử lý** — hồ sơ nhận vào, chưa qua tổng hợp.

Một tệp đi từ đây sang `KTC-Database` khi đã ban hành và được nạp chính thức. Không đi ngược lại.

## Trạng thái di chuyển (14/9/2026)

| Nguồn cũ | Trạng thái |
|---|---|
| `23-KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/KH Truong/` (2 tệp) | ✅ đã chuyển sang `02-Cap-Truong/01-Nam/2026/` |
| `23-KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/KH-Truong/` (1 tệp) | ✅ đã chuyển sang `02-Cap-Truong/02-Quy/2026-Q3/` |
| `25-KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/` (40 tệp thật) | ✅ **đã chuyển** 14/9/2026 — bảng ánh xạ đầy đủ tại `30-Ket-Qua/2026-09-14/Anh-xa-chuyen-Nhap_Bao_Cao.md` |
| 60 thư mục rỗng còn lại của hai nhánh cũ | ⏸ chờ người dùng xóa thủ công — `30-Ket-Qua/2026-09-14/Danh-muc-can-don-toan-he.md` |

**Kho này nay là nguồn đầu vào DUY NHẤT.** Hai công cụ `29-Cong-Cu/build_xl.py` và
`29-Cong-Cu/trich_tuong_thuat.py` đã trỏ sang đây và chạy đúng trên dữ liệu thật (13 đơn vị, 198 ý kết quả,
130 ý kế hoạch).

### Đã sửa khi chuyển — hai việc đáng ghi

1. **Chọn đúng bản Kế hoạch quý III.** Có hai bản cùng tên `..._CHUAN`: bản trong `input-KH_Quy` có 54
   nhiệm vụ / 1 sheet, bản trong `Nhap_Bao_Cao/KH-Cap-Tren` có **55 nhiệm vụ / 4 sheet** (thêm
   `Nhật ký thay đổi`, `Nguồn đối chiếu`, `Quy ước màu`). Lấy bản đầy đủ. Phép đo lại: tỷ lệ `KH-834`
   trích từ kế hoạch quý tăng từ 14/47 lên **15/47**.
2. **`Doan-TN/DOAN TN.xlsx` là kế hoạch tháng 9, không phải báo cáo** — xác định bằng cách mở tệp. Tên
   không theo quy ước chung nên phép quét theo mẫu tên ở đợt chạy thử trước đã bỏ sót. Nay đã đặt đúng tên.
