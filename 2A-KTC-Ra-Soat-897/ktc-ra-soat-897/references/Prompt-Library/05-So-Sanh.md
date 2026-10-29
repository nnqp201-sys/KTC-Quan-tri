# 05-So-Sanh

> **Cập nhật v4.1 (26/10/2026):** chạy cổng `tools/kiem_ke_ho_so.py … --tac-vu so-sanh` (không đòi báo cáo rà soát, Báo cáo tiếp thu – quyết định của Hiệu trưởng 26/10/2026, điểm 3); lập bảng thay đổi bằng `tools/so_sanh_ban.py <bản cũ> <bản mới>`; đo thể thức từng bản bằng `kiem_tra_the_thuc.py`; đối chiếu chéo theo SKILL.md Bước 4. Mức theo `references/Quy-Tac-KTC/02-Quy-Tac-Xep-Muc.md`.

> **Cập nhật v4.2 (27/10/2026):** cổng chỉ áp G1–G4 (đúng hai bản dự thảo, đủ phụ lục, văn bản kèm theo của từng bản – v4.3); văn bản được đề cập chưa có toàn văn không chặn, đối chiếu ghi “Chưa kiểm (chưa có toàn văn)” (quyết định của Hiệu trưởng 27/10/2026). Dựng báo cáo bằng `tools/tao_bao_cao.py … --so-sanh ss.json` với `"kieu_bao_cao": "so_sanh"` và `so_sanh.ket_luan`; báo cáo có II.D bảng thay đổi, “Kết luận so sánh”, **không gán nhãn trình ký**.


## Vai trò
So sánh 2 phiên bản/đối chiếu dự thảo với văn bản gốc — dùng 1 prompt tổng quát có tham số [Loại văn bản], thay cho 7 file riêng trước đây (đã hợp nhất theo Phương án B, 07/8/2026).

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy so sánh 2 văn bản sau:
- Loại văn bản: [...]
- Bản A: [...] — Bản B: [...]

So sánh theo: cấu trúc/thể thức; nội dung cốt lõi theo đúng loại văn bản (đối chiếu Skill 07-13); điểm còn thiếu; khác biệt về ý nghĩa (không chỉ câu chữ). Tách rõ khác biệt nội dung và hình thức; không mặc định bản nào tốt hơn nếu chưa có căn cứ.

Output: tóm tắt so sánh → khác biệt chính → rủi ro/lưu ý → khuyến nghị.
