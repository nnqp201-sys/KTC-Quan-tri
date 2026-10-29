# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.25 (30/09/2026)  ⚠️ CỜ XEM XÉT THỦ CÔNG

**Skill đã chạy:** `ktc-ra-soat-897` **v2.25** (SKILL.md dòng phiên bản "Cập nhật 28/9/2026"; có mục "Danh sách dương tính giả" và dẫn mục 3a Checklist 01). Đây là **lần đo đầu tiên trên v2.25** (28/9 và các lần trước đo trên v2.24). Phiên này nạp skill v2.25, khác với ghi chú MEMORY-INDEX 29/9 ("đang nạp v2.24, chưa cài v2.25") → v2.25 nay đã có hiệu lực.
**Tác vụ tự động** — bước 0: file kết quả gần nhất `Ket-qua-v2.24_28092026.md` (28/9/2026 20:40 UTC), cách lúc chạy (30/9/2026 20:39 UTC) ≈ 48 giờ > 36 giờ → đủ điều kiện.
**File test:** `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (ID `1aKbLCYSxWlvcrvrL8lAvVpx8j2d5ngZD`, sửa lần cuối 31/8/2026 — không đổi). **Đáp án:** `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi). **Nguồn đã đọc:** MEMORY-INDEX (29/9), BANG-CHI-SO, kết quả 28/9, đáp án, file test. Chưa đọc Nhật ký (nhiều bản trùng tên khác chủ sở hữu) và chưa đọc nội dung kho 01-04 trong lượt này.

## 1. Điểm số

| Nhóm | 28/9 (v2.24) | 30/9 (v2.25) | Thay đổi |
|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | **24/30 (80%)** | ▼ −1 |
| Đúng phát hiện, sai mức | 1/30 (3,3%) | **2/30 (6,7%)** | ▲ +1 (#6) |
| Bỏ sót | 4/30 (13,3%) | **4/30 (13,3%)** | Không đổi |

**Kết luận: ĐIỂM THẤP HƠN LẦN TRƯỚC → DỪNG, KHÔNG TỰ SỬA, GẮN CỜ XEM XÉT THỦ CÔNG.** Số lỗi Mức 1 *bỏ sót* không tăng (vẫn chỉ #1), nhưng xuất hiện **một lỗi Mức 1 bị hạ mức** (#6) — cùng loại rủi ro với điều tiêu chí bước 5 muốn bắt.

## 2. Lỗi bỏ sót / sai mức (số #)

- **Bỏ sót (không đổi):** #1 (lề 2cm, Mức 1), #5 (cỡ chữ trích yếu T1), #29 (T2), #30 (T3) — cả 4 là `FORMAT_BINARY_UNVERIFIED` (phiên cloud chỉ đọc văn bản qua Drive; tải base64 nhưng không dựng lại được tệp đáng tin để chạy `_read_input_properties.py`).
- **Sai mức #12** ("Công ty"/"Trung tâm"): đáp án Mức 4, phát hiện Mức 3 — như các lần trước.
- **Sai mức MỚI #6** (căn cứ QĐ 49/QĐ-CĐKT): đáp án **Mức 1**, nhưng v2.25 cho kết quả **Mức 4 / không bắt Mức 1**.

## 3. Phát hiện mới so với lần trước: CÓ — xung đột đáp án ↔ quy tắc v2.25

Dòng "Văn bản cũ dẫn căn cứ đã bị thay thế sau ngày ban hành → đúng tại thời điểm ban hành, chỉ Mức 4" (Danh sách dương tính giả, thêm ở v2.25) **mâu thuẫn trực tiếp với đáp án #6**. Dự thảo test ghi ngày **05/02/2026**, trong khi QĐ 988 ban hành 12/5/2026 (và theo MEMORY-INDEX, QĐ 1976 ngày 14/9/2026 đã thay 988). Theo quy tắc "đối chiếu theo ngày ban hành của dự thảo, không hồi tố", QĐ 49 tại ngày 05/02/2026 không còn là căn cứ sai → v2.25 không còn bắt #6 ở Mức 1.
Đây có thể là: (a) thay đổi **cố ý** đúng pháp lý → đáp án #6 cần được người có thẩm quyền cập nhật (ví dụ đổi ngày trong file test sau 12/5/2026 để bài test còn giá trị); hoặc (b) hồi quy ngoài ý muốn làm mất khả năng bắt lỗi căn cứ hết hiệu lực. **Cần Chủ Team/người quản trị quyết định — Hệ không tự kết luận.**
Điểm còn bắt được dù áp dụng quy tắc mới: ghi chú nội bộ "đã điều chỉnh 49→988" mâu thuẫn với nội dung thật (vẫn ghi 49) (Mức 2) và mốc ngày nhiều căn cứ (VBHN 16/3/2026) muộn hơn ngày dự thảo (05/2/2026).
Các mục khác của danh sách dương tính giả (không bắt "Ban hành kèm theo…", dự thảo chưa số hiệu, Hội Sinh viên không tiêu đề) **không chạm lỗi nào trong 30 lỗi đáp án** → không ảnh hưởng điểm. Tình huống ngoài đáp án (#31+: bản mẫu trống 03-Templates, khối "PHIẾU RÀ SOÁT… ChatGPT… CHÍNH THỨC", VBHN 41 vs 14, đoạn "KTC-DIS-v1", hoán đổi thể thức Công đoàn↔Đoàn TN) vẫn hiện diện; ghi nhận định tính, chưa có đáp án nên không tính điểm.

## 4. Giới hạn của lượt đo

- Không phải rà soát mù (đáp án đọc cùng phiên) — điểm có xu hướng lạc quan; việc chấm #6 dựa trên áp dụng quy tắc v2.25 như văn bản, có thể tranh luận.
- Không đọc được thuộc tính định dạng thật; chưa truy cập nội dung thật kho 01-04.
- Chưa cập nhật `BANG-CHI-SO-THEO-THOI-GIAN.md` (không sửa tại chỗ). Dòng đề xuất thêm thủ công:
`| 30/9/2026 | **v2.25** | 24/30 (80%) ▼ | 2/30 (6,7%) ▲ | 4/30 (13,3%) = | Tác vụ tự động, lần đo đầu trên v2.25. Sai mức mới #6 do quy tắc "căn cứ bị thay thế sau ngày ban hành" (xung đột đáp án). FORMAT_BINARY_UNVERIFIED: #1,5,29,30. **Gắn cờ xem xét thủ công.** |`
- Không đóng gói lại `.skill`, không commit, không sửa file test/đáp án.

---
*Tác vụ tự động (scheduled task) — 30/9/2026. Không có người theo dõi trực tiếp. Bản nháp chỉ có giá trị tham khảo.*
