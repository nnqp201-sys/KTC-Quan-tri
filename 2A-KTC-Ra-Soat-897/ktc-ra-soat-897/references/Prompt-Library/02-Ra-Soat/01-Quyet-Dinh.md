# 02-Ra-Soat / Quyết định

> **Cập nhật v4.0 (26/10/2026):** trước khi dùng prompt này phải qua cổng hồ sơ (`references/Quy-Tac-KTC/05-Cong-Ho-So.md`); thông số thể thức theo `01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước NĐ 30); mức theo bảng mã `02-Quy-Tac-Xep-Muc.md`. Phần nào trong prompt dưới đây khác thì theo các tệp đó.

> **Cập nhật v4.2 (27/10/2026):** khi dùng cho tác vụ (b) rà soát nhanh, dựng báo cáo bằng `tools/tao_bao_cao.py` với `"kieu_bao_cao": "nhanh"` – tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, **không gán nhãn trình ký**.


## Prompt purpose
Rà soát một Quyết định về thẩm quyền, căn cứ, thể thức Nghị định 30, và tính rõ ràng của đối tượng/hiệu lực thi hành.

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy rà soát văn bản Quyết định sau đây và trả về danh sách vấn đề phát hiện được, kèm mức độ nghiêm trọng (1: bắt buộc sửa → 4: góp ý nâng cao):

[dán nội dung Quyết định]

Kiểm tra theo các nhóm:
1. Thẩm quyền ký có đúng thẩm quyền không (Hiệu trưởng/HĐT/Trưởng phòng).
2. Căn cứ pháp lý có đủ, đúng thứ tự ưu tiên (Luật/Nghị định > quy định Bộ > quy chế Trường) không.
3. Thể thức theo Nghị định 30/2020/NĐ-CP (quốc hiệu, tiêu ngữ, số ký hiệu, trích yếu, nơi nhận, chữ ký).
4. Nội dung các Điều có rõ đối tượng thi hành và hiệu lực không.
5. Nếu là quyết định quy phạm: có dẫn đúng Nghị định 30 và văn bản kèm theo không.

Output: bảng vấn đề (Nhóm | Mô tả | Căn cứ | Kiến nghị sửa | Mức độ), theo đúng chuẩn Skill 28 (Báo cáo rà soát).
