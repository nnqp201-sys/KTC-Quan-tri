# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.25 (02/10/2026) ⚠️ CỜ XEM XÉT THỦ CÔNG (còn nguyên từ 30/9)

**Skill đã chạy:** `ktc-ra-soat-897` **v2.25** (SKILL.md "Cập nhật 28/9/2026"; gói Drive `ktc-ra-soat-897-v2.25.skill` 236.832 byte, sửa lần cuối 29/9 — không đổi so với lần đo 30/9).
**Tác vụ tự động** — bước 0: file kết quả gần nhất `Ket-qua-v2.25_30092026.md` (30/9/2026 20:40 UTC), cách lúc chạy (02/10/2026 20:39 UTC) ≈ 48 giờ > 36 giờ → đủ điều kiện.
**File test:** `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (sửa lần cuối 31/8/2026, không đổi). **Đáp án:** `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi, không đổi).
**Nguồn đã đọc:** MEMORY-INDEX (29/9), BANG-CHI-SO, kết quả 30/9, đáp án, file test (nội dung text), SKILL.md v2.25, Checklist 08. Chưa đọc Nhật ký (nhiều bản trùng tên khác chủ sở hữu; MEMORY-INDEX đã nêu Nhật ký lệch v3.4/v1.1). Chưa đọc nội dung kho 01-04.

## 1. Điểm số

| Nhóm | BANG-CHI-SO (07/9, v2.21) | 30/9 (v2.25) | 02/10 (v2.25) | So với 30/9 |
|---|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | 24/30 (80%) | **24/30 (80%)** | = |
| Đúng phát hiện, sai mức | 1/30 (3,3%) | 2/30 (6,7%) | **2/30 (6,7%)** | = |
| Bỏ sót | 4/30 (13,3%) | 4/30 (13,3%) | **4/30 (13,3%)** | = |

**Kết luận:** bằng lần 30/9 (không xấu thêm) nhưng **thấp hơn dòng gần nhất trong BANG-CHI-SO (07/9: 25/30)** vì #6 vẫn bị hạ mức. BANG-CHI-SO chưa có dòng nào sau 07/9. Theo bước 5: **DỪNG, KHÔNG TỰ SỬA, giữ cờ xem xét thủ công.** Số lỗi Mức 1 bỏ sót không tăng (chỉ #1).

## 2. Lỗi bỏ sót / sai mức (số #)

- **Bỏ sót (không đổi):** #1 (lề 2cm, Mức 1), #5, #29, #30 (cỡ chữ trích yếu) — cả 4 là `FORMAT_BINARY_UNVERIFIED`. Lần này đã tải lại base64 của .docx (fileSize 11.423 → cần 15.232 ký tự) nhưng chép tay ra shell bị lệch (15.305 ký tự, giải mã 11.478 byte, không phải ZIP hợp lệ) → **không dựng lại được tệp, không chạy được `_read_input_properties.py`**. Đây lại là đúng lỗi "copy tay base64" đã ghi ở bảng chỉ số; không thử lặp.
- **Sai mức #12** ("Công ty"/"Trung tâm"): đáp án Mức 4, phát hiện Mức 3 — như các lần trước.
- **Sai mức #6** (căn cứ QĐ 49/QĐ-CĐKT): đáp án Mức 1; theo Checklist 08 mục 1, dự thảo ngày 05/02/2026 (trước 12/5/2026) dẫn QĐ 49 là **đúng tại thời điểm ban hành → không nêu lỗi**. Kết quả: Mức 4 / không bắt Mức 1. Vẫn bắt được: ghi chú "đã điều chỉnh 49→988" mâu thuẫn nội dung (Mức 2) và mốc ngày VBHN 16/3/2026 muộn hơn ngày dự thảo.

## 3. Phát hiện mới so với lần trước

- **Không có phát hiện mới về điểm số** so với 30/9.
- **Ứng viên xung đột đáp án ↔ quy tắc thứ hai (chưa tính vào điểm, để người quản trị xem xét): #17.** Đáp án ghi "Nơi nhận phải dùng THHCQT". Checklist 08 mục 3.4 (bổ sung 08/9/2026) nay quy định cột giữa (THHCQT) chỉ dùng cho số/ký hiệu và dòng `Lưu:`, không dùng cho đơn vị được nhận; hành văn dùng **"Phòng TH-HC&QT"** (có gạch nối). Dự thảo ghi "Phòng THHC&QT" vẫn sai (Mức 2, thiếu gạch nối) nhưng kiến nghị sửa của v2.25 khác đáp án. Tôi chấm #17 là **đúng** (đúng vị trí, đúng mức) để giữ so sánh được với 30/9; nếu chấm nghiêm theo kiến nghị trong đáp án thì thành 23/30 đúng, 3/30 sai mức.
- Mâu thuẫn #6 vẫn **chờ Chủ Team/người quản trị quyết định**: (a) cố ý đúng pháp lý → cập nhật đáp án #6 hoặc đổi ngày file test sau 12/5/2026 (lưu ý: sau 14/9/2026 thì căn cứ đúng là QĐ 1976); (b) hồi quy ngoài ý muốn. Hệ không tự kết luận.
- Tình huống ngoài đáp án (#31+: bản mẫu trống 03-Templates, khối "PHIẾU RÀ SOÁT… ChatGPT… CHÍNH THỨC", VBHN 41 vs 14, "KTC-DIS-v1", hoán đổi thể thức Công đoàn↔Đoàn TN) vẫn hiện diện; chưa có đáp án nên không tính điểm.

## 4. Giới hạn của lượt đo

- Không phải rà soát mù (đáp án đọc cùng phiên) — điểm có xu hướng lạc quan. Kết quả các mục khác được chấm lại trên cùng đầu vào, cùng phiên bản skill như 30/9 (gói, file test, đáp án đều không đổi từ trước 30/9), nên không kỳ vọng khác biệt.
- Không đọc được thuộc tính định dạng thật; chưa truy cập nội dung thật kho 01-04.
- Đề xuất dòng thêm thủ công vào `BANG-CHI-SO-THEO-THOI-GIAN.md` (không sửa tại chỗ; bảng còn thiếu cả dòng 28/9 và 30/9):
`| 02/10/2026 | **v2.25** | 24/30 (80%) ▼ so với 07/9 (= so với 30/9) | 2/30 (6,7%) | 4/30 (13,3%) = | Tác vụ tự động, lần 2 trên v2.25. #6 vẫn sai mức (quy tắc "căn cứ bị thay thế sau ngày ban hành"). FORMAT_BINARY_UNVERIFIED: #1,5,29,30. Ứng viên xung đột mới: #17. **Giữ cờ xem xét thủ công.** |`
- Không đóng gói lại `.skill`, không commit, không sửa file test/đáp án.

---
*Tác vụ tự động (scheduled task) — 02/10/2026. Không có người theo dõi trực tiếp. Bản nháp chỉ có giá trị tham khảo; cần Trưởng/Phó đơn vị phê duyệt. Người kiểm tra: [CẦN ĐIỀN TÊN VÀ CHỨC DANH NGƯỜI THẬT]. Trạng thái: BẢN NHÁP.*
