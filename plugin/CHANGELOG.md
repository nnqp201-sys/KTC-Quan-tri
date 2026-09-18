# Changelog — KTC-Quan-tri Plugin

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
