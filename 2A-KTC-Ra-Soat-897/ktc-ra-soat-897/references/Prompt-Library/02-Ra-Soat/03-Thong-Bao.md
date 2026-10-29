# 02-Ra-Soat / Thông báo

> **Cập nhật v4.0 (26/10/2026):** trước khi dùng prompt này phải qua cổng hồ sơ (`references/Quy-Tac-KTC/05-Cong-Ho-So.md`); thông số thể thức theo `01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước NĐ 30); mức theo bảng mã `02-Quy-Tac-Xep-Muc.md`. Phần nào trong prompt dưới đây khác thì theo các tệp đó.

> **Cập nhật v4.2 (27/10/2026):** khi dùng cho tác vụ (b) rà soát nhanh, dựng báo cáo bằng `tools/tao_bao_cao.py` với `"kieu_bao_cao": "nhanh"` – tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, **không gán nhãn trình ký**.


## Prompt purpose
Rà soát một Thông báo về tính ngắn gọn, đúng nội dung đã thống nhất, và rõ trách nhiệm thực hiện.

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy rà soát văn bản Thông báo sau đây:

[dán nội dung Thông báo]

Kiểm tra theo các nhóm:
1. Trích yếu có phản ánh đúng nội dung thông báo không.
2. Nếu là thông báo kết luận cuộc họp: nội dung có khớp với kết luận đã thống nhất không, có bị diễn giải thêm không.
3. Có nêu rõ ai làm gì, khi nào không.
4. Nơi nhận có đủ và đúng (để thực hiện/biết/báo cáo) không.
5. Thể thức theo Nghị định 30.

Output: bảng vấn đề (Nhóm | Mô tả | Căn cứ | Kiến nghị sửa | Mức độ), theo đúng chuẩn Skill 28.
