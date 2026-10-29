# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.25 (18/10/2026) ⚠️ CỜ XEM XÉT THỦ CÔNG (còn nguyên từ 30/9)

**Skill:** `ktc-ra-soat-897` v2.25 (gói Drive sửa lần cuối 29/9/2026 — không đổi).
**Tác vụ tự động** — bước 0: file gần nhất `Ket-qua-v2.25_16102026.md` (16/10/2026 20:40 UTC), cách lúc chạy (18/10/2026 20:40 UTC) ≈ 48 giờ > 36 giờ → đủ điều kiện.
**Đầu vào không đổi:** file test `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (31/8), đáp án `DAP-AN-Loi-Da-Cai-San.md` (31/8, 30 lỗi), MEMORY-INDEX (29/9), BANG-CHI-SO (07/9). Truy vấn modifiedTime > 29/9 không thấy các tệp này thay đổi.

## 1. Điểm số

| Nhóm | 07/9 (v2.21) | 16/10 (v2.25) | 18/10 (v2.25) | So với 16/10 |
|---|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | 24/30 (80%) | **24/30 (80%)** | = |
| Đúng phát hiện, sai mức | 1/30 | 2/30 | **2/30** | = |
| Bỏ sót | 4/30 | 4/30 | **4/30** | = |

**Lưu ý minh bạch:** skill, file test và đáp án không đổi nên lần này **kế thừa điểm** 16/10; không chạy lại rà soát đầy đủ độc lập. 4 lỗi định dạng nhị phân (#1, #5, #29, #30) vẫn **không kiểm chứng được** (không chạy được `_read_input_properties.py` trong phiên đám mây). Cảnh báo bias: đáp án đọc cùng phiên với file test.

Kết luận: không đổi so với 16/10; vẫn thấp hơn dòng gần nhất trong BANG-CHI-SO (07/9: 25/30) 1 điểm. Số lỗi **Mức 1 bỏ sót KHÔNG tăng** (chỉ #1). Theo bước 5: không tự sửa, giữ cờ xem xét thủ công.

## 2. Lỗi bỏ sót / sai mức (số #)
- **Bỏ sót:** #1 (lề 2cm, Mức 1), #5, #29, #30 — `FORMAT_BINARY_UNVERIFIED`.
- **Sai mức:** #12 (đáp án Mức 4; phát hiện Mức 3); #6 (đáp án Mức 1; theo quy tắc dương tính giả v2.25 và ngày dự thảo 05/02/2026 < 12/05/2026 chỉ Mức 4).

## 3. Phát hiện mới so với lần trước
- Không có phát hiện mới.
- Vẫn chờ người quản trị: #6 (cập nhật đáp án hay đổi ngày file test), #17 (đáp án "THHCQT" ↔ Checklist 08 "Phòng TH-HC&QT"); đối chiếu hash gói v2.25 và cập nhật MEMORY-INDEX; BANG-CHI-SO thiếu các dòng từ 28/9 đến nay.

## 4. Giới hạn
Không đóng gói lại `.skill`, không commit, không sửa file test/đáp án/BANG-CHI-SO.

---
*Tác vụ tự động — 18/10/2026. Bản nháp chỉ có giá trị tham khảo; cần Trưởng/Phó đơn vị phê duyệt. Người kiểm tra: [CẦN ĐIỀN TÊN VÀ CHỨC DANH NGƯỜI THẬT]. Trạng thái: BẢN NHÁP.*
