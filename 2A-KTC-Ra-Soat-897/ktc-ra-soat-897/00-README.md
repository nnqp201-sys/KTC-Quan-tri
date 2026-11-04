# ktc-ra-soat-897 – v4.6.4 (03/11/2026 – BẢN HOÀN THIỆN sau nghiệm thu độc lập lần 3 và quyết định Q1–Q5; đã tự kiểm của người sửa; Hiệu trưởng phê duyệt chính thức ngày 03/11/2026)

Skill rà soát, so sánh, chuẩn hóa dự thảo văn bản của Trường Cao đẳng Kon Tum trước khi trình ký (không soạn mới). Từ v4.0, kết quả được cố định bằng script và bảng quy tắc để giống nhau giữa các lần chạy và các tài khoản.

## Nội dung gói
- `SKILL.md` – quy trình 8 bước (0–7), quy tắc ổn định kết quả, định dạng đầu ra.
- `tools/` – `kiem_ke_ho_so.py` (cổng hồ sơ), `kiem_tra_the_thuc.py` (đo thể thức), `so_sanh_ban.py` (so sánh hai bản), `tao_bao_cao.py` (dựng báo cáo .docx, tự tính nhãn); `nhan_dien_chung.py` (hàm nhận diện dùng chung, v4.6); `kiem_kieu_du_lieu.py` (hợp đồng kiểu dữ liệu báo cáo, v4.6.2); `README.md`; `legacy/` (tham khảo).
- `references/Quy-Tac-KTC/` – 01 bảng thông số thể thức; 02 bảng mã – mức – nhãn; 03 đơn vị, cơ sở, thẩm quyền; 04 viện dẫn văn bản hợp nhất; 05 cổng hồ sơ; 06 điểm thay thế Mẫu prompt.
- `references/Kho-Du-Lieu-897/` – 36 văn bản nền tảng (35 .docx, 1 PDF scan chỉ tham khảo), bản text của 35 tệp .docx, `kho_manifest.json`, chỉ mục.
- `references/Lich-Su-Khong-Ap-Dung/` – hướng dẫn sử dụng cũ v2.x (14/8/2026), chỉ lưu tư liệu, không áp dụng.
- `references/Skill-Library/`, `Prompt-Library/`, `Checklist/`, `Nguyen-Tac/` – hướng dẫn chuyên đề (đã gắn ghi chú ưu tiên v4.0–v4.6).
- `assets/` – Mẫu prompt chính thức; `Mau-Du-Lieu-Bao-Cao.json`; template báo cáo trống (tham khảo).
- `references/CHANGELOG.md` – thay đổi theo phiên bản, điểm đề nghị Hiệu trưởng xem lại.

## Cài đặt
Bản v4.6.4 (= v4.6.3 + quyết định Q1–Q5 ngày 03/11/2026: QĐ 2487 vào nhóm AI bắt buộc, quy tắc đối chiếu Danh mục AI bằng mã sẵn có, lưu ý bảo mật dẫn QĐ 2487, Kho thêm 3 luật căn cứ, `--xac-nhan-toan-van`) là **bản sửa hoàn thiện sau nghiệm thu độc lập lần 3** (kết luận lần 3 đối với v4.6.2: CHƯA ĐẠT – giữ nguyên). Theo chỉ đạo của người phụ trách, KHÔNG tổ chức nghiệm thu độc lập lần 4; bản này đã được **người sửa tự kiểm** (không phải nghiệm thu độc lập) trong phạm vi và giới hạn ghi ở `references/CHANGELOG.md`. Quyền quyết định cài thuộc **người phụ trách Skill**. Khi được quyết định cài: sao lưu bản đang dùng và ghi SHA-256; tải gói lên mục Skills; chạy lại toàn bộ chuỗi (cổng → đo → so sánh → dựng) cho mọi hồ sơ đang dở – kết quả JSON của v4.6.3 trở về trước không dùng được; lưu ý thay đổi D2 (Kho ngoài gói bị từ chối) và D10 (so sánh: vị trí phía dự thảo phải ghi tên tệp).

## Quan hệ với hệ khác
- Kho 01-04 đầy đủ trên Drive (nếu có kết nối) bổ sung cho Kho đóng gói; Kho đóng gói là nguồn tối thiểu.
- Soạn văn bản mới dùng các skill soạn thảo của Trường; CTĐT, giáo trình, KHBG, NHCH dùng skill riêng.
