# DL-20260914-004 — Tối ưu cấu trúc thư mục toàn hệ

**Ngày:** 14/9/2026 · **Loại:** APPLY · **Phạm vi:** toàn dự án → bắt buộc ghi Decision Log

## Nguyên tắc áp dụng

**Mỗi loại nội dung có đúng một chỗ.** Trước đợt này, ba loại đang nằm rải:

| Loại | Trước — nằm ở đâu | Sau |
|---|---|---|
| Dữ liệu đầu vào | `KTC-Ke-Hoach/Nhap_Ke_Hoach/` + `KTC-Bao-Cao/Nhap_Bao_Cao/` | `11-Du-Lieu-Dau-Vao/` |
| Sản phẩm xuất ra | `12-Output/` + `KTC-Bao-Cao/Xuat_Bao_Cao/` + `KTC-Ke-Hoach/Xuat_Ke_Hoach/` | `12-Output/YYYY-MM-DD/` |
| Bộ nhớ của hệ Báo cáo | `KTC-Bao-Cao/memory/` + `KTC-Bao-Cao/references/Memory/` | `references/Memory/` |

Ba chỗ "thứ hai" đều ra đời vì tiện lúc đó, rồi ở lại. Mỗi chỗ thừa là một chỗ để quên.

## Sáu việc đã làm

1. **Đầu ra về `12-Output/`.** `Xuat_Bao_Cao/` và `Xuat_Ke_Hoach/` bỏ. Đây vốn là mâu thuẫn nội bộ:
   `01-Chuan-Chung/00-Nguyen-Tac-Chung.md` và `CLAUDE.md` **đã** quy định `12-Output/YYYY-MM-DD/` là nơi
   duy nhất, nhưng `KTC-Ke-Hoach/SKILL.md` lại chỉ sang `Xuat_Ke_Hoach/`. Nay thống nhất theo bản gốc.
2. **Đầu vào về `11-Du-Lieu-Dau-Vao/`.** 40 tệp của `Nhap_Bao_Cao` đã chuyển, tên chuẩn hóa theo nội dung
   (`BC-KQ-thang-8-2026.xlsx`, `KH-thang-9-2026.xlsx`), thư mục mang **mã đơn vị chuẩn**. Bảng ánh xạ
   từng tệp: `12-Output/2026-09-14/Anh-xa-chuyen-Nhap_Bao_Cao.md`.
3. **Hai lớp bộ nhớ của KTC-Bao-Cao gộp một.** `RUN-RECORD-SCHEMA.md` → `references/Memory/`;
   `KTC-RIS-Memory-Architecture.docx` → `04-Tai-Lieu-Thiet-Ke/` vì đó là tài liệu kiến trúc, không phải
   quy tắc vận hành — và không nên nhét `.docx` vào gói skill.
4. **`99-Luu-Tru` chia hai nhánh**: `Goi-skill-cu/` và `Ban-nhap-bi-thay-the/<ngày>/`.
5. **`tools/narrative.json` ra khỏi thư mục mã nguồn** → `tools/_trung_gian/`. Dữ liệu trung gian nằm lẫn
   với mã nguồn là chỗ dễ commit nhầm và khó biết xóa được hay không.
6. **Bỏ đường dẫn tuyệt đối trong `tools/`.** `build_xl.py` và `trich_tuong_thuat.py` nay suy ra gốc dự án
   từ vị trí tệp. Đổi chỗ dự án không phải sửa từng tool nữa.

## Kiểm chứng — không chỉ sắp lại rồi tin

Chạy thật cả hai công cụ trên kho mới:

| Công cụ | Kết quả |
|---|---|
| `tools/build_xl.py` | Kế hoạch quý III → tháng 8: 41 nhiệm vụ, tháng 9: 26. Dựng được 2 tệp `.xlsx` |
| `tools/trich_tuong_thuat.py` | **13 đơn vị**, 198 ý kết quả, 130 ý kế hoạch — nay hiện theo **mã chuẩn** (`P-QLKH`, `P-TCCB`…) thay vì tên thư mục tự do |

## Hai phát hiện trong lúc chuyển

1. **Hai bản Kế hoạch quý III cùng tên `_CHUAN`.** Bản ở `Nhap_Bao_Cao/KH-Cap-Tren` có **55 nhiệm vụ và
   4 sheet**; bản ở `input-KH_Quy` chỉ 54 nhiệm vụ, 1 sheet. Lấy bản đầy đủ. Đo lại: tỷ lệ `KH-834` trích
   từ kế hoạch quý tăng **14/47 → 15/47**.
2. **`Doan-TN/DOAN TN.xlsx` là kế hoạch tháng 9, không phải báo cáo.** Tên tệp không theo quy ước nên phép
   quét theo mẫu tên ở đợt chạy thử trước đã bỏ sót — kết luận "Đoàn TN chưa nộp kế hoạch" là **sai**.
   Xác định đúng bằng cách mở tệp ra xem sheet và tiêu đề.

   *Bài học lặp lại lần thứ ba trong ngày: phân loại theo TÊN tệp không đáng tin. Lần một là khớp nhiệm vụ
   theo tên (`KI-001`), lần hai là chọn sheet theo số dòng, lần này là nhận loại tệp theo tên.*

## Việc còn lại — cố ý không tự làm

**61 thư mục rỗng** và **`KTC-DIS-Tong-Hop-VB/` (123 tệp)** để người dùng tự xóa, theo quy ước *"tệp trên
Drive chỉ do người dùng xóa thủ công"*. Danh mục kèm hướng dẫn kiểm trước khi xóa:
`12-Output/2026-09-14/Danh-muc-can-don-toan-he.md`.

## Hệ quả kèm theo

- `KTC-Ke-Hoach`: `SKILL.md`, `Workflow 10`, `Skill 34`, `Skill 38`, `Prompt 00` đã sửa đường dẫn; đóng
  gói lại `ktc-ke-hoach-v3.2.skill`.
- Phép kiểm C4/C11 vẫn xanh cho cả 5 gói sau khi sắp lại.

**Liên quan:** `DL-20260914-003` (kho đầu vào) · `DL-20260914-005` (đóng gói KTC-Theo-doi-CV) ·
`PM-20260914-Chay-thu-KH-thang-9`
