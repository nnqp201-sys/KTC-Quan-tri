# 02-Ra-Soat / Báo cáo

> **Cập nhật v4.0 (26/10/2026):** trước khi dùng prompt này phải qua cổng hồ sơ (`references/Quy-Tac-KTC/05-Cong-Ho-So.md`); thông số thể thức theo `01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước NĐ 30); mức theo bảng mã `02-Quy-Tac-Xep-Muc.md`. Phần nào trong prompt dưới đây khác thì theo các tệp đó.

> **Cập nhật v4.2 (27/10/2026):** khi dùng cho tác vụ (b) rà soát nhanh, dựng báo cáo bằng `tools/tao_bao_cao.py` với `"kieu_bao_cao": "nhanh"` – tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, **không gán nhãn trình ký**.


## Prompt purpose
Rà soát một Báo cáo về tính nhất quán số liệu, đầy đủ cấu trúc, và tính khả thi của phương hướng đề xuất.

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy rà soát văn bản Báo cáo sau đây (kích hoạt chế độ rà soát đầy đủ theo Skill 28 nếu đây là báo cáo quan trọng):

[dán nội dung Báo cáo]

Kiểm tra theo các nhóm:
1. Số liệu có nhất quán nội bộ (không mâu thuẫn giữa các phần) không.
2. Có đủ 3 phần: kết quả thực hiện, tồn tại/hạn chế/nguyên nhân, phương hướng/kiến nghị không.
3. Phương hướng đề xuất có bám sát tồn tại đã nêu không (không đề xuất chung chung, không liên quan).
4. Đúng cấu trúc mẫu báo cáo chuẩn của Trường không (nếu áp dụng).
5. Thể thức theo Nghị định 30.

Output: bảng vấn đề (Nhóm | Mô tả | Căn cứ | Kiến nghị sửa | Mức độ), theo đúng chuẩn Skill 28.
