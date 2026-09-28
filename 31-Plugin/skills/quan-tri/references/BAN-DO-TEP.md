# Bảng đối chiếu tên tệp — bản gốc (dự án) → vị trí trong plugin

Sinh tự động khi dựng plugin 1.3.9 (`dong_goi_plugin.py`, so nội dung sha256). Tài liệu nhắc tên thư mục
dự án (`20-Chuan-Chung/…`, `29-Cong-Cu/…`): tra bảng này, **không xin quyền thư mục dự án**.

| Bản gốc trên máy phát triển | Bản sao trong plugin |
|---|---|
| `20-Chuan-Chung/00-Metadata-Schema.md` | `skills/bao-cao/references/Skill-Library/00-Metadata-Schema.md` · `skills/ke-hoach/references/Skill-Library/00-Metadata-Schema.md` · `skills/soan-thao-vb/references/Skill-Library/00-Metadata-Schema.md` |
| `20-Chuan-Chung/00-Nguyen-Tac-Chung.md` | `skills/bao-cao/references/Skill-Library/00-Nguyen-Tac-Chung.md` · `skills/ke-hoach/references/Skill-Library/00-Nguyen-Tac-Chung.md` · `skills/quan-tri/references/01-Nguyen-Tac-Chung.md` (+2) |
| `20-Chuan-Chung/04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` | `skills/bao-cao/references/Skill-Library/04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` · `skills/ke-hoach/references/Skill-Library/04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` · `skills/soan-thao-vb/references/Skill-Library/04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` |
| `20-Chuan-Chung/10-Tu-Dien-Truong-Du-Lieu.md` | `skills/quan-tri/references/20-Tu-Dien-Truong-Du-Lieu.md` |
| `20-Chuan-Chung/11-Quy-Tac-Task-ID.md` | `skills/quan-tri/references/21-Quy-Tac-Task-ID.md` |
| `20-Chuan-Chung/12-Vong-Doi-Trang-Thai.md` | `skills/quan-tri/references/22-Vong-Doi-Va-Canh-Bao.md` |
| `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` | `skills/quan-tri/references/12-Bang-Ma-Don-Vi.md` |
| `20-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md` | `skills/soan-thao-vb/references/Skill-Library/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md` |
| `20-Chuan-Chung/15-Skill-Track-Changes.md` | `skills/soan-thao-vb/references/Skill-Library/15-Skill-Track-Changes.md` |
| `20-Chuan-Chung/17-Quy-Tac-Vien-Dan.md` | `skills/bao-cao/references/Skill-Library/17-Quy-Tac-Vien-Dan.md` · `skills/ke-hoach/references/Skill-Library/17-Quy-Tac-Vien-Dan.md` · `skills/quan-tri/references/17-Quy-Tac-Vien-Dan.md` (+2) |
| `20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md` | `skills/bao-cao/references/Skill-Library/18-Chuan-The-Thuc-San-Pham.md` · `skills/ke-hoach/references/Skill-Library/18-Chuan-The-Thuc-San-Pham.md` · `skills/quan-tri/references/18-Chuan-The-Thuc-San-Pham.md` (+3) |
| `20-Chuan-Chung/19-Quy-Tac-KPI.md` | `skills/kpi-lap-ke-hoach/references/Skill-Library/19-Quy-Tac-KPI.md` · `skills/kpi-tu-danh-gia/references/Skill-Library/19-Quy-Tac-KPI.md` · `skills/quan-tri/references/30-KPI-Va-Xep-Loai.md` |
| `20-Chuan-Chung/30-Skill-Phan-Loai-6-Truc.md` | `skills/bao-cao/references/Skill-Library/30-Skill-Phan-Loai-6-Truc.md` · `skills/ke-hoach/references/Skill-Library/30-Skill-Phan-Loai-6-Truc.md` · `skills/quan-tri/references/11-Skill-Phan-Loai-6-Truc.md` (+2) |
| `20-Chuan-Chung/Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` | `skills/bao-cao/references/Skill-Library/Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` · `skills/ke-hoach/references/Skill-Library/Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` · `skills/soan-thao-vb/references/Skill-Library/Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` |
| `20-Chuan-Chung/20-Quy-Tac-Bat-Bien-Va-Khuon-Dau-Ra.md` | `skills/*/references/00-Quy-Tac-Bat-Bien-Day-Du.md` |
| `29-Cong-Cu/<công cụ>.py` | `scripts/<công cụ>.py` (và bản trong kỹ năng nếu có) |
| `23-KTC-Ke-Hoach/references/ktc-tu-hoc-ke-hoach.skill` | `skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/` |

## Không nằm trong plugin — đúng thiết kế

| Loại | Ở đâu | Khi không có |
|---|---|---|
| Mẫu `.dotx`/`.xltx`, `00-Template-Registry-KTC-DIS.docx`, `KTC-DIS-Master-Index_*.xlsx`, văn bản đã ban hành (BC/PL/KH tháng, TB giao ban, CTCT năm) | Kho **KTC-Database** (Google Drive, chỉ đọc) — `scripts/duong_dan.py` | Hỏi người dùng đính kèm; `THIEU_DU_LIEU` |
| Checklist, Skill-Library của rà soát 897 (`Checklist/0x-….md`, `19-Skill-Danh-Gia-Chat-Luong-Van-Ban.md`, `31-Quy-Tac-Van-Hanh-Theo-Tinh-Huong.md`, `17-Skill-Kiem-Tra-Tham-Quyen.md`, `29-Skill-Van-Ban-Dang.md`, mẫu prompt 897) | Plugin **ktc-ra-soat-897** cài kèm | Nêu rõ chưa rà soát theo 897 |
| `MEMORY-INDEX.md`, `Pending.md`, `TRI-THUC.md`, `90-Nhat-Ky-Van-Hanh/`, `92-Kinh-Nghiem/`, `10-Dau-Vao/` của dự án, công cụ phát triển (`kiem_tra_he_thong.py`, `dong_goi_*.py`, `test_*.py`) | Chỉ máy quản trị P-THHC | Bỏ qua — không cần khi chạy |
