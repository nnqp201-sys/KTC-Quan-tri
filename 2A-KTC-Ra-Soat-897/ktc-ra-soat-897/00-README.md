# ktc-ra-soat-897 – v4.5 (27/10/2026)

Skill rà soát, so sánh, chuẩn hóa dự thảo văn bản của Trường Cao đẳng Kon Tum trước khi trình ký (không soạn mới). Từ v4.0, kết quả được cố định bằng script và bảng quy tắc để giống nhau giữa các lần chạy và các tài khoản.

## Nội dung gói
- `SKILL.md` – quy trình 8 bước (0–7), quy tắc ổn định kết quả, định dạng đầu ra.
- `tools/` – `kiem_ke_ho_so.py` (cổng hồ sơ), `kiem_tra_the_thuc.py` (đo thể thức), `so_sanh_ban.py` (so sánh hai bản), `tao_bao_cao.py` (dựng báo cáo .docx, tự tính nhãn); `README.md`; `legacy/` (tham khảo).
- `references/Quy-Tac-KTC/` – 01 bảng thông số thể thức; 02 bảng mã – mức – nhãn; 03 đơn vị, cơ sở, thẩm quyền; 04 viện dẫn văn bản hợp nhất; 05 cổng hồ sơ; 06 điểm thay thế Mẫu prompt.
- `references/Kho-Du-Lieu-897/` – 36 văn bản nền tảng (35 .docx, 1 PDF scan chỉ tham khảo), bản text của 35 tệp .docx, `kho_manifest.json`, chỉ mục.
- `references/Lich-Su-Khong-Ap-Dung/` – hướng dẫn sử dụng cũ v2.x (14/8/2026), chỉ lưu tư liệu, không áp dụng.
- `references/Skill-Library/`, `Prompt-Library/`, `Checklist/`, `Nguyen-Tac/` – hướng dẫn chuyên đề (đã gắn ghi chú ưu tiên v4.0–v4.5).
- `assets/` – Mẫu prompt chính thức; `Mau-Du-Lieu-Bao-Cao.json`; template báo cáo trống (tham khảo).
- `references/CHANGELOG.md` – thay đổi theo phiên bản, điểm đề nghị Hiệu trưởng xem lại.

## Cài đặt
Tải tệp `ktc-ra-soat-897-v4.5.skill` lên mục Skills (thay bản trước). Môi trường cần Python 3 với `lxml`, `python-docx`; LibreOffice và poppler giúp đo số trang, kiểm PDF (thiếu thì phần đó ghi “chưa kiểm”).

## Quan hệ với hệ khác
- Kho 01-04 đầy đủ trên Drive (nếu có kết nối) bổ sung cho Kho đóng gói; Kho đóng gói là nguồn tối thiểu.
- Soạn văn bản mới dùng các skill soạn thảo của Trường; CTĐT, giáo trình, KHBG, NHCH dùng skill riêng.
