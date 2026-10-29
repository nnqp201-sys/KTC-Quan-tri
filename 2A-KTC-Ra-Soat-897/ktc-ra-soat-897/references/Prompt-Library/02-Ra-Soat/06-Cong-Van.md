# 02-Ra-Soat / Công văn

> **Cập nhật v4.0 (26/10/2026):** trước khi dùng prompt này phải qua cổng hồ sơ (`references/Quy-Tac-KTC/05-Cong-Ho-So.md`); thông số thể thức theo `01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước NĐ 30); mức theo bảng mã `02-Quy-Tac-Xep-Muc.md`. Phần nào trong prompt dưới đây khác thì theo các tệp đó.

> **Cập nhật v4.2 (27/10/2026):** khi dùng cho tác vụ (b) rà soát nhanh, dựng báo cáo bằng `tools/tao_bao_cao.py` với `"kieu_bao_cao": "nhanh"` – tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, **không gán nhãn trình ký**.


## Prompt purpose
Rà soát một Công văn về giọng văn, đúng cấp bậc quan hệ hành chính, và tính đúng loại văn bản.

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy rà soát văn bản Công văn sau đây:

[dán nội dung Công văn]

Kiểm tra theo các nhóm:
1. Giọng văn có lịch sự, đúng cấp bậc quan hệ hành chính không (kính gửi đúng cơ quan/chức danh).
2. Nếu là công văn góp ý dự thảo: nội dung có bám sát dự thảo được hỏi không, có lan man không.
3. Công văn có đang bị dùng sai mục đích (ví dụ dùng để ban hành quyết định/quy định) không.
4. Nơi nhận (chính, để biết/phối hợp) có đúng không.
5. Thể thức theo Nghị định 30.

Output: bảng vấn đề (Nhóm | Mô tả | Căn cứ | Kiến nghị sửa | Mức độ), theo đúng chuẩn Skill 28.
