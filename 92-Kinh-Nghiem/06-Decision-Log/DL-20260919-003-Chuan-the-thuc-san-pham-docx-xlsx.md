# DL-20260919-003 — Chuẩn thể thức sản phẩm .docx/.xlsx; skill `the-thuc` chồng lên `docx`/`xlsx`

**Ngày:** 19/9/2026 · **Người quyết định:** người dùng (chủ dự án)

**Yêu cầu:**
- *"Mọi sản phẩm của KTC-quan-tri dưới dạng docx hoặc xlsx phải đạt chuẩn thể thức, kỹ thuật, template trình bày
  như tại 03-Templates(1) hoặc 04-Good-Documents."*
- Bổ sung trong lượt: *"can thiệp vào skill docx, xlsx sẵn có để giải quyết yêu cầu này"*.

**Vì sao không sửa thẳng skill `docx`/`xlsx`:** hai skill này là skill của Anthropic, đồng bộ từ claude.ai về
`~/.claude/skills/synced/`.
- Sửa tại máy thì lần đồng bộ sau sẽ ghi đè. Máy của thành viên Team cũng không nhận được bản sửa.
- `LICENSE.txt` của hai skill là độc quyền ("All rights reserved"), nên không được chép vào plugin của Trường.

→ **Can thiệp bằng một lớp chồng lên:**
- skill **`the-thuc`**, kích hoạt cùng `docx`/`xlsx` khi sinh tệp cho Trường;
- **hook** tự đo trong Code;
- **Nguyên tắc 6** trong quy tắc chung của cả 5 skill.

Những điểm KTC ghi đè mặc định của Anthropic:
- `docx` để lề 2,54 cm cả bốn lề; KTC: 2-2-3-2 cm.
- `xlsx` cho dùng Arial; KTC: Times New Roman.
- `docx.Document()` rỗng ra khổ Letter; KTC: cấm dựng từ tệp rỗng.

**Đo thật (không suy diễn):**
- **16 mẫu trong `03-Templates(1)`:** 15 `.dotx` đều A4, lề 2/2/3/2 cm, Times New Roman, nội dung cỡ 14.
  `05B.xltx` là A4 ngang, Times New Roman 14.
- **73 tệp** (mẫu, văn bản tốt, sản phẩm KTC-Quan-tri): 47 tệp đạt. Lỗi thật tìm được:
  - `.VnTime`;
  - lề 0,6 cm;
  - "UBND TỈNH KON TUM" trong văn bản trước sáp nhập và trong mẫu `10-Giay-moi`;
  - **sản phẩm của chính hệ** `Phieu-de-xuat_Bo-sung-cot-Task_ID…docx` ra khổ Letter.
- **Báo nhầm đã sửa:** hàng trăm đoạn bị báo "Calibri Light". Nguyên nhân là theme có `themeFontLang = vi-VN`,
  nên Word hiển thị phông script "Viet" = Times New Roman. Công cụ nay giải phông theo đúng cách đó.

**Đã làm:**
- `20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md` (bản gốc):
  - thứ tự nguồn: văn bản tốt → mẫu → tạo mới;
  - bảng chọn mẫu theo 17 loại sản phẩm;
  - số đo .docx/.xlsx và mã kiểm TT01–TT11, TX01–TX04;
  - lỗi đã biết của mẫu.
  Đã nhân bản xuống 5 hệ và skill `the-thuc`.
- `00-Nguyen-Tac-Chung.md` Nguyên tắc 6.
- `29-Cong-Cu/kiem_the_thuc.py`: đo và `--tao` (mở `.dotx`/`.xltx` thành tệp làm việc). Checker C9 kiểm import.
- Skill mới **`27-KTC-The-Thuc/`** (`ktc-the-thuc-v1.0.skill`); trong plugin đặt tên `the-thuc`.
- Hook `ktc_the_thuc_hook.py` (PostToolUse): chỉ chạy trong dự án KTC. Còn Mức 1–2 thì trả mã 2 để Claude sửa
  trước khi giao.
- Ca hồi quy `test_kiem_the_thuc.py`: 17 ca, gồm ca thử ngược và mẫu thật trên Drive.
- Sản phẩm lỗi: tạo `…_v2-A4.docx`, bản gốc giữ nguyên.
- Đề xuất sửa mẫu và Master Index: `30-Ket-Qua/2026-09-19/De-xuat/De-xuat-sua-mau-10-Giay-moi-va-Master-Index.md`.
- Phiên bản gói: quan-tri 1.8 · ke-hoach 3.9 · theo-doi-cv 1.7 · bao-cao 3.14 · soan-thao-vb 1.9 · **the-thuc 1.0**.
  Plugin **0.6.0**.

**Giới hạn còn lại:**
- Chat, và Cowork khi không chạy được Python, không đo được byte. Skill yêu cầu ghi `FORMAT_BINARY_UNVERIFIED`.
- Hook chỉ có tác dụng trong Claude Code.
- Tài khoản không đọc được Drive phải đính kèm mẫu, hoặc dựng theo số đo mục 3–4.
