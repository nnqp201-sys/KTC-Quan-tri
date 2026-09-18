# DL-20260918-004 — Kết cấu lại thư mục theo nhóm INPUT / PROCESS / OUTPUT

**Ngày:** 18/9/2026 · **Người quyết định:** người dùng (chủ dự án) — chọn phương án A trong 3 phương án đề xuất
(A: nhóm bằng số đầu tên, cây phẳng · B: 3 thư mục cha · C: không dời, chỉ thêm bản đồ).

| Cũ | Mới | Nhóm |
|---|---|---|
| `11-Du-Lieu-Dau-Vao/` | `10-Dau-Vao/` | INPUT |
| `Du-lieu-Cong-Viec/` | `11-Du-lieu-Cong-Viec/` | INPUT |
| `01-Chuan-Chung/` | `20-Chuan-Chung/` | PROCESS |
| `02-Master-Task-Register/` | `21-Master-Task-Register/` | PROCESS |
| `SKILL.md`, `references/`, `ktc-quan-tri.skill`, `00-README-ktc-quan-tri.md` (gốc) | `22-Dieu-Phoi/` | PROCESS |
| `KTC-Ke-Hoach/` · `KTC-Theo-doi-CV/` · `KTC-Bao-Cao/` · `KTC-Soan-Thao-VB/` | `23-` · `24-` · `25-` · `26-` + tên cũ | PROCESS |
| `tools/` | `29-Cong-Cu/` | PROCESS |
| `12-Output/` | `30-Ket-Qua/` | OUTPUT |
| `plugin/` | `31-Plugin/` | OUTPUT |
| `03-Nhat-Ky-Van-Hanh/` · `04-Tai-Lieu-Thiet-Ke/` · `99-Kinh-Nghiem/` | `90-` · `91-` · `92-` | Quản trị hệ |

**Lý do:** nhìn cây thư mục thấy ngay luồng dữ liệu 1x → 2x → 3x; không thêm tầng đường dẫn (Drive/Windows).
Làm trước khi dữ liệu vận hành thật (Task_ID) chảy vào để giảm số hồ sơ phải dời.

**Kèm theo (yêu cầu cùng lúc của người dùng):** plugin sẽ cài cấp Team; tài khoản phòng/khoa/bộ môn không có
`10-Dau-Vao/` → thêm **Nguyên tắc 3** vào `20-Chuan-Chung/00-Nguyen-Tac-Chung.md` (nhân xuống 5 gói): đầu vào lấy
theo thứ tự tệp đính kèm trong phiên → thư mục dự án → hỏi; kết quả trả về để tải xuống.

**Cách làm:** `git mv` (giữ lịch sử) · thay đường dẫn bằng regex có ranh giới trong 105 tệp `.md/.py/.json`
(không đụng `99-Luu-Tru/`, `30-Ket-Qua/` — hồ sơ lịch sử giữ nguyên chữ) · đóng gói lại 5 skill · plugin 0.4.0
· cập nhật Task Scheduler. Kiểm: Tầng 1 0 lỗi, 6/6 ca hồi quy đạt.

**Sự cố trong lúc làm:** quy tắc thay `plugin` bắt nhầm cả chữ "plugin" trong câu văn (11 tệp) — đã rà và
trả lại; chỉ giữ `31-Plugin` ở chỗ là đường dẫn. `12-Output/` rỗng còn sót do Windows khóa — người dùng xóa tay.
