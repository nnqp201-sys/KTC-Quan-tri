# Changelog — KTC-Quan-tri Plugin

## 0.1.0 — 2026-09-18

Bản đầu tiên. Gộp 5 hệ KTC (quan-tri, bao-cao, ke-hoach, soan-thao-vb, theo-doi-cv) thành một plugin dùng
chung cho Cowork và Claude Code, thay vì 5 gói `.skill` rời.

- Dựng từ 5 gói `.skill` đã xác minh byte-for-byte cùng ngày (`DL-20260918-001`): `ktc-quan-tri.skill`,
  `ktc-bao-cao-v3.7.skill`, `ktc-ke-hoach-v3.3.skill`, `ktc-soan-thao-vb-v1.1.skill`,
  `ktc-theo-doi-cv-v1.1.skill`.
- Phát hiện và vá 3 lỗ hổng tham chiếu có thật trong `ktc-soan-thao-vb` (tồn tại từ trước, không liên quan
  lần đóng gói này): `14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`, `15-Skill-Track-Changes.md`,
  `tools/ktc_trackchanges.py` được SKILL.md trích dẫn nhưng chưa từng có trong gói `.skill` — nay đã có
  bản trong plugin. **Gói `.skill` gốc (ngoài plugin) vẫn còn thiếu 3 tệp này — chưa sửa, xem ghi chú bàn
  giao.**
- Hook `SessionStart` mới: `scripts/ktc_quan_tri_doctor.py` — in phiên bản tự khai của cả 5 skill.
- Chưa chạy `claude plugin validate --strict` (không có CLI trong môi trường dựng) — chỉ tự kiểm thủ công.
