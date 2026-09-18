# Changelog — KTC-Quan-tri Plugin

## 0.3.0 — 2026-09-18

- `bao-cao` nâng lên **v3.8** (gói `ktc-bao-cao-v3.8.skill`): đọc cột `Task_ID` (KI-001, Lãnh đạo thống nhất,
  `DL-20260918-003`); sửa lỗi nhiệm vụ "Tổng hợp/Tổng kết…" bị bỏ mất. `quan-tri`: cập nhật quy tắc Task_ID.

## 0.2.2 — 2026-09-18

- Sửa lỗi nhật ký: khi hook báo thư mục làm việc nằm ngoài dự án, script vẫn lùi về thư mục đang chạy và
  ghi nhầm vào nhật ký KTC-Quan-tri (phát hiện qua dòng "Write a" do kiểm thử sinh ra). Nay chỉ lùi về khi
  hook không báo thư mục nào. Không ghi dòng rỗng khi dữ liệu hook hỏng.
- Hồi quy thêm ca ngược: chạy kiểm thử từ chính thư mục dự án và kiểm nhật ký thật không đổi (ca này thất bại
  với bản cũ, đạt với bản mới). Đã dọn 10 dòng rác khỏi nhật ký 18/9.

## 0.2.1 — 2026-09-18

- Thư mục dữ liệu nền đổi tên `KTC-Du-lieu-Cong-Viec` → `Du-lieu-Cong-Viec` (yêu cầu người dùng). Cập nhật
  mọi tham chiếu còn hiệu lực (CLAUDE.md, README, 01-Chuan-Chung, references, agent); đóng gói lại
  `ktc-quan-tri.skill` từ nguồn rời. Hồ sơ lịch sử trong `12-Output/` giữ nguyên tên cũ.
- `Claude outputs/` (tệp ứng dụng Claude xuất ra) đưa vào `.gitignore` — không lên backup GitHub.

## 0.2.0 — 2026-09-18

Thêm 3 cơ chế theo yêu cầu người dùng. Nguồn viết tay ở `tools/plugin_src/` (script build chép vào, không sửa
trong `plugin/`). Hồi quy: `99-Kinh-Nghiem/02-Regression/Cases/test_plugin_nhat_ky_backup.py` — 10 ca, có ca ngược.

- **Agent `ktc-tu-cai-tien`** (`agents/`): đọc nhật ký tự động, Process Memory, Known Issues, Decision Log, kết
  quả `kiem_tra_he_thong.py` → viết đề xuất `CP-YYYYMMDD-NNN` trạng thái *Chờ duyệt* vào
  `99-Kinh-Nghiem/03-Change-Proposals/`. **Không tự sửa** skill/quy tắc/dữ liệu (nguyên tắc bất biến #6);
  bị chặn công cụ `Edit`.
- **Tự ghi nhật ký + nạp vào context** (`scripts/ktc_nhat_ky.py`): `PostToolUse` ghi 1 dòng JSONL cho mỗi
  Write/Edit/Bash/PowerShell/Skill/Agent vào `03-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/YYYY-MM-DD.jsonl` (chỉ
  tên công cụ + đối tượng, **không** ghi nội dung tệp); `SessionStart` in tóm tắt 2 ngày gần nhất vào
  context; `SessionEnd` đánh dấu kết thúc phiên. Chỉ hoạt động trong thư mục KTC-Quan-tri.
- **Tự backup GitHub** (`scripts/ktc_backup_github.py`): commit + push thường (không force), Task Scheduler
  21:00 hằng ngày (`KTC-Quan-tri-Backup-GitHub`, chạy bù khi máy bật lại) + `SessionStart` chạy bù nếu quá
  24h. Dừng nếu có tệp tên giống bí mật. **Chưa nối remote** — cần người dùng cung cấp URL repo private.

## 0.1.1 — 2026-09-18

- `ktc-soan-thao-vb` nâng lên **v1.2** ở nguồn (gói `.skill` gốc, không chỉ trong plugin): thêm hẳn
  `14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`, `15-Skill-Track-Changes.md`, `ktc_trackchanges.py` vào
  `references/Skill-Library/` của chính hệ đó, sửa 3 trích dẫn trong `SKILL.md` trỏ đúng vị trí trong gói
  (`references/Skill-Library/...`, không còn cần `${CLAUDE_PLUGIN_ROOT}`).
- `tools/dong_goi_plugin.py` bỏ hàm vá riêng cho plugin (`vas_lo_hong_soan_thao_vb`) — không còn cần vì đã
  sửa tận gốc; script build lại đơn giản như 4 hệ còn lại (giải nén thuần túy, không vá thêm).
- Sửa lỗi build script: `don_sach()` từng xoá cả `README.md`/`CHANGELOG.md` viết tay ở gốc `plugin/` vì dọn
  nguyên thư mục gốc — nay chỉ dọn các thư mục sinh tự động (`skills/`, `.claude-plugin/`, `hooks/`,
  `scripts/`), giữ nguyên tài liệu viết tay.
- Kiểm lại: 0 lỗi, 0 tệp thiếu/thừa so với 5 gói `.skill` nguồn, không còn tham chiếu
  `${CLAUDE_PLUGIN_ROOT}` nào trong toàn bộ 5 SKILL.md.

## 0.1.0 — 2026-09-18

Bản đầu tiên. Gộp 5 hệ KTC (quan-tri, bao-cao, ke-hoach, soan-thao-vb, theo-doi-cv) thành một plugin dùng
chung cho Cowork và Claude Code, thay vì 5 gói `.skill` rời.

- Dựng từ 5 gói `.skill` đã xác minh byte-for-byte cùng ngày (`DL-20260918-001`): `ktc-quan-tri.skill`,
  `ktc-bao-cao-v3.7.skill`, `ktc-ke-hoach-v3.3.skill`, `ktc-soan-thao-vb-v1.1.skill`,
  `ktc-theo-doi-cv-v1.1.skill`.
- Phát hiện 3 lỗ hổng tham chiếu có thật trong `ktc-soan-thao-vb` (tồn tại từ trước, không liên quan lần
  đóng gói này) và vá tạm riêng cho plugin. **Đã thay bằng bản sửa tận gốc ở 0.1.1**, xem mục trên.
- Hook `SessionStart` mới: `scripts/ktc_quan_tri_doctor.py` — in phiên bản tự khai của cả 5 skill.
- Chưa chạy `claude plugin validate --strict` (không có CLI trong môi trường dựng) — chỉ tự kiểm thủ công.
