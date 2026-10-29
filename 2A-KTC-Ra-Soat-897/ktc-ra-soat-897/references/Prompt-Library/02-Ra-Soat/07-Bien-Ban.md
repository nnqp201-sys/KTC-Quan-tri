# 02-Ra-Soat / Biên bản

> **Cập nhật v4.0 (26/10/2026):** trước khi dùng prompt này phải qua cổng hồ sơ (`references/Quy-Tac-KTC/05-Cong-Ho-So.md`); thông số thể thức theo `01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước NĐ 30); mức theo bảng mã `02-Quy-Tac-Xep-Muc.md`. Phần nào trong prompt dưới đây khác thì theo các tệp đó.

> **Cập nhật v4.2 (27/10/2026):** khi dùng cho tác vụ (b) rà soát nhanh, dựng báo cáo bằng `tools/tao_bao_cao.py` với `"kieu_bao_cao": "nhanh"` – tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, **không gán nhãn trình ký**.


## Prompt purpose
Rà soát một Biên bản về tính trung thực của nội dung ghi nhận và tính đầy đủ chữ ký các bên.

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy rà soát văn bản Biên bản sau đây:

[dán nội dung Biên bản]

Kiểm tra theo các nhóm:
1. Nội dung diễn biến có được ghi trung thực, theo trình tự không, có dấu hiệu diễn giải chủ quan không.
2. Kết luận/thống nhất có khớp với nội dung diễn biến đã ghi không.
3. Thành phần tham dự và chữ ký các bên có đầy đủ theo yêu cầu (đặc biệt với biên bản nghiệm thu/hội đồng) không.
4. Thời gian, địa điểm có được ghi rõ không.
5. Thể thức theo Nghị định 30.

Output: bảng vấn đề (Nhóm | Mô tả | Căn cứ | Kiến nghị sửa | Mức độ), theo đúng chuẩn Skill 28.
