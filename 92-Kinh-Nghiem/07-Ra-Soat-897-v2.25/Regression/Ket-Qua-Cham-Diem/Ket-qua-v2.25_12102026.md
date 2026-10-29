# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.25 (12/10/2026) ⚠️ CỜ XEM XÉT THỦ CÔNG (vẫn còn từ 30/9)

**Skill:** `ktc-ra-soat-897` — bản đang cài trong phiên chạy này là **v2.25** (SKILL.md 16.380 byte, có mục 3a Checklist 01 và "Danh sách dương tính giả"). Đây là lần đầu bản cài được xác minh trực tiếp là v2.25 (MEMORY-INDEX 29/9 từng ghi phiên nạp là v2.24).
**Tác vụ tự động** — bước 0: file gần nhất `Ket-qua-v2.25_10102026.md` (10/10/2026 20:40 UTC), cách lúc chạy (12/10/2026 20:39 UTC) ≈ 48 giờ > 36 giờ → đủ điều kiện.
**Đầu vào:** `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (31/8, không đổi), `DAP-AN-Loi-Da-Cai-San.md` (31/8, 30 lỗi), MEMORY-INDEX (29/9), Nhật ký (15/9), BANG-CHI-SO (07/9).

## 1. Điểm số

| Nhóm | 07/9 (v2.21) | 10/10 (v2.25) | 12/10 (v2.25) | So với 10/10 |
|---|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | 24/30 (80%) | **24/30 (80%)** | = |
| Đúng phát hiện, sai mức | 1/30 | 2/30 | **2/30** | = |
| Bỏ sót | 4/30 | 4/30 | **4/30** | = |

Phương pháp lần này: rà soát lại phần chữ của file test (đọc nội dung thật từ Drive) đối chiếu 26 lỗi nội dung với quy tắc v2.25; 4 lỗi định dạng nhị phân (#1, #5, #29, #30) **không kiểm chứng được** vì phiên đám mây không tải được tệp .docx nguyên vẹn để chạy `_read_input_properties.py` (chỉ nhận base64 hiển thị, không ghi ra đĩa được) → giữ nhóm bỏ sót `FORMAT_BINARY_UNVERIFIED`. Cảnh báo bias: đáp án đã đọc cùng phiên.

Kết luận: thấp hơn dòng gần nhất trong BANG-CHI-SO (07/9: 25/30) 1 điểm. Số lỗi **Mức 1 bỏ sót KHÔNG tăng** (chỉ #1). Theo bước 5: **không tự sửa**, gắn cờ xem xét thủ công.

## 2. Lỗi bỏ sót / sai mức (số #)
- **Bỏ sót:** #1 (lề 2cm, Mức 1), #5, #29, #30 — `FORMAT_BINARY_UNVERIFIED`.
- **Sai mức:** #12 (đáp án Mức 4; phát hiện Mức 3); #6 (đáp án Mức 1, nhưng theo quy tắc dương tính giả v2.25 + ngày dự thảo 05/02/2026 < 12/05/2026 thì chỉ Mức 4).

## 3. Phát hiện mới so với lần trước
- Không có lỗi mới trong file test.
- **Mới (cấu hình):** (a) Bản cài hiện là v2.25 nhưng MEMORY-INDEX (29/9) vẫn ghi "nạp v2.24 / chưa cài v2.25" và gói v2.25 trên Drive có 2 kích thước khác nhau (236.832 byte trong thư mục chính vs 261.531 byte ghi trong MEMORY-INDEX) — cần người quản trị đối chiếu hash và cập nhật MEMORY-INDEX; các kết quả 28/9–10/10 có thể đo trên v2.24 chứ chưa chắc v2.25. (b) Đáp án #6 ("phải QĐ 988") lỗi thời: MEMORY-INDEX ghi căn cứ đầu tiên hiện là QĐ 1976/QĐ-CĐKT (14/9/2026).
- Vẫn chờ quyết định: #6 (cập nhật đáp án hay đổi ngày file test), #17 (đáp án "THHCQT" ↔ Checklist 08 "Phòng TH-HC&QT").
- BANG-CHI-SO vẫn thiếu các dòng từ 28/9 đến nay — cần cập nhật thủ công.

## 4. Giới hạn
Không đóng gói lại `.skill`, không commit, không sửa file test/đáp án/BANG-CHI-SO.

---
*Tác vụ tự động — 12/10/2026. Bản nháp chỉ có giá trị tham khảo; cần Trưởng/Phó đơn vị phê duyệt. Người kiểm tra: [CẦN ĐIỀN TÊN VÀ CHỨC DANH NGƯỜI THẬT]. Trạng thái: BẢN NHÁP.*
