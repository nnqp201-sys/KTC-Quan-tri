# 02-Ra-Soat / Kế hoạch

> **Cập nhật v4.0 (26/10/2026):** trước khi dùng prompt này phải qua cổng hồ sơ (`references/Quy-Tac-KTC/05-Cong-Ho-So.md`); thông số thể thức theo `01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597, QĐ 1355 trước NĐ 30); mức theo bảng mã `02-Quy-Tac-Xep-Muc.md`. Phần nào trong prompt dưới đây khác thì theo các tệp đó.

> **Cập nhật v4.2 (27/10/2026):** khi dùng cho tác vụ (b) rà soát nhanh, dựng báo cáo bằng `tools/tao_bao_cao.py` với `"kieu_bao_cao": "nhanh"` – tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, **không gán nhãn trình ký**.


## Prompt purpose
Rà soát một Kế hoạch về tính bám sát chỉ đạo cấp trên, chỉ tiêu đo lường được, và tính khớp với kế hoạch cấp trên/cùng cấp.

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy rà soát văn bản Kế hoạch sau đây:

[dán nội dung Kế hoạch]

Kiểm tra theo các nhóm:
1. Kế hoạch có bám sát chủ trương/văn bản chỉ đạo cấp trên không (nếu có căn cứ).
2. Chỉ tiêu, mốc thời gian có cụ thể, đo lường được không — hay còn dùng ngôn ngữ mơ hồ ("sớm", "kịp thời"...).
3. Kế hoạch tháng/quý có khớp với kế hoạch năm không (nếu có để đối chiếu).
4. Phân công đơn vị/cá nhân thực hiện có rõ ràng, không chồng chéo không.
5. Thể thức theo Nghị định 30.

Output: bảng vấn đề (Nhóm | Mô tả | Căn cứ | Kiến nghị sửa | Mức độ), theo đúng chuẩn Skill 28.
