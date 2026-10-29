# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.25 (04/10/2026) ⚠️ CỜ XEM XÉT THỦ CÔNG (còn nguyên từ 30/9)

**Skill:** `ktc-ra-soat-897` v2.25 (SKILL.md "Cập nhật 28/9/2026"; gói Drive 236.832 byte, sửa lần cuối 29/9 — không đổi).
**Tác vụ tự động** — bước 0: file gần nhất `Ket-qua-v2.25_02102026.md` (02/10/2026 20:43 UTC), cách lúc chạy (04/10/2026 20:39 UTC) ≈ 48 giờ > 36 giờ → đủ điều kiện.
**File test** `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (sửa 31/8, không đổi) · **Đáp án** `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi, không đổi) · MEMORY-INDEX (29/9) đã đọc. Chưa đọc Nhật ký (nhiều bản trùng tên; MEMORY-INDEX đã nêu lệch) và chưa đọc nội dung kho 01-04.

## 1. Điểm số

| Nhóm | BANG-CHI-SO (07/9, v2.21) | 02/10 (v2.25) | 04/10 (v2.25) | So với 02/10 |
|---|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | 24/30 (80%) | **24/30 (80%)** | = |
| Đúng phát hiện, sai mức | 1/30 (3,3%) | 2/30 (6,7%) | **2/30 (6,7%)** | = |
| Bỏ sót | 4/30 (13,3%) | 4/30 (13,3%) | **4/30 (13,3%)** | = |

**Kết luận:** bằng lần 02/10; thấp hơn dòng gần nhất trong BANG-CHI-SO (07/9: 25/30) do #6 vẫn bị hạ mức. Số lỗi Mức 1 bỏ sót KHÔNG tăng (chỉ #1). Theo bước 5: **DỪNG, KHÔNG tự sửa, giữ cờ xem xét thủ công.**

## 2. Lỗi bỏ sót / sai mức (số #)

- **Bỏ sót:** #1 (lề 2cm, Mức 1), #5, #29, #30 (cỡ chữ trích yếu) — cả 4 là `FORMAT_BINARY_UNVERIFIED`: phiên đám mây không chạy được `_read_input_properties.py` trên tệp thật (tiền lệ lỗi chép tay base64 ngày 02/10; không thử lặp).
- **Sai mức #12** (Công ty/Trung tâm): đáp án Mức 4, phát hiện Mức 3.
- **Sai mức #6** (căn cứ QĐ 49): đáp án Mức 1; theo Checklist 08 mục 1 + danh sách dương tính giả ("căn cứ bị thay thế sau ngày ban hành" — dự thảo ngày 05/02/2026) chỉ Mức 4. Vẫn bắt ghi chú "đã điều chỉnh 49→988" mâu thuẫn nội dung (Mức 2).
- Phát hiện đúng: #2-4, 7-11, 13-28 (nội dung text).

## 3. Phát hiện mới so với lần trước

- **Không có phát hiện mới về điểm số** so với 02/10.
- Vẫn chờ người quản trị quyết định: **#6** (đáp án đang mâu thuẫn quy tắc dương tính giả v2.25 — cập nhật đáp án hay đổi ngày file test; lưu ý sau 14/9/2026 căn cứ đúng là QĐ 1976) và **#17** (đáp án "THHCQT" ↔ Checklist 08 mục 3.4 "Phòng TH-HC&QT"; chấm #17 là đúng để giữ so sánh được).
- Tình huống ngoài đáp án (#31+: bản mẫu trống 03-Templates, khối "PHIẾU RÀ SOÁT… ChatGPT… CHÍNH THỨC", VBHN 41 vs 14, "KTC-DIS-v1", hoán đổi thể thức Công đoàn↔Đoàn TN) chưa có đáp án, không tính điểm.
- Lưu ý: BANG-CHI-SO còn thiếu các dòng 28/9, 30/9, 02/10; đề xuất dòng thủ công: `| 04/10/2026 | v2.25 | 24/30 (80%) ▼ so với 07/9 (= 02/10) | 2/30 (6,7%) | 4/30 (13,3%) = | Tác vụ tự động. #6 sai mức do quy tắc dương tính giả; FORMAT_BINARY_UNVERIFIED: #1,5,29,30. Giữ cờ xem xét thủ công. |`

## 4. Giới hạn

Không phải rà soát mù (đáp án đọc cùng phiên) — điểm có xu hướng lạc quan. Đầu vào và phiên bản skill không đổi từ 30/9 nên kết quả lặp lại. Không đóng gói lại `.skill`, không commit, không sửa file test/đáp án/BANG-CHI-SO.

---
*Tác vụ tự động — 04/10/2026. Bản nháp chỉ có giá trị tham khảo; cần Trưởng/Phó đơn vị phê duyệt. Người kiểm tra: [CẦN ĐIỀN TÊN VÀ CHỨC DANH NGƯỜI THẬT]. Trạng thái: BẢN NHÁP.*
