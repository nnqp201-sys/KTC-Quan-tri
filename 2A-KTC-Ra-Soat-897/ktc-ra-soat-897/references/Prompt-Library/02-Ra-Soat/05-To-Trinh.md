# 02-Ra-Soat / Tờ trình

> **Cập nhật v4.0 (26/10/2026):** trước khi dùng prompt này phải qua cổng hồ sơ (`references/Quy-Tac-KTC/05-Cong-Ho-So.md`); thông số thể thức theo `01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước NĐ 30); mức theo bảng mã `02-Quy-Tac-Xep-Muc.md`. Phần nào trong prompt dưới đây khác thì theo các tệp đó.

> **Cập nhật v4.2 (27/10/2026):** khi dùng cho tác vụ (b) rà soát nhanh, dựng báo cáo bằng `tools/tao_bao_cao.py` với `"kieu_bao_cao": "nhanh"` – tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, **không gán nhãn trình ký**.


## Prompt purpose
Rà soát một Tờ trình về tính cụ thể của nội dung đề nghị và tính đúng thẩm quyền.

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy rà soát văn bản Tờ trình sau đây:

[dán nội dung Tờ trình]

Kiểm tra theo các nhóm:
1. Nội dung đề nghị có đủ cụ thể để cấp có thẩm quyền phê duyệt trực tiếp không (không mơ hồ).
2. Đề nghị có vượt thẩm quyền của cấp trình hoặc cấp nhận không.
3. Căn cứ pháp lý và căn cứ thực tiễn (sự cần thiết) có đủ không.
4. Hồ sơ/văn bản kèm theo có được liệt kê đầy đủ không.
5. Thể thức theo Nghị định 30.

Output: bảng vấn đề (Nhóm | Mô tả | Căn cứ | Kiến nghị sửa | Mức độ), theo đúng chuẩn Skill 28.
