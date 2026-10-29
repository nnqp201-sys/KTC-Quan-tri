# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.24 (28/09/2026)

**Skill đã chạy:** `ktc-ra-soat-897` v2.24 (SKILL.md: "Cập nhật 14/9/2026, gói ktc-ra-soat-897-v2.24.skill").
**Tác vụ tự động** — kiểm tra bước 0: file kết quả gần nhất `Ket-qua-v2.24_24092026.md` (24/9/2026 21:02 UTC), cách lúc chạy (28/9/2026 20:40 UTC) ~95 giờ > 36 giờ → đủ điều kiện.
**File test:** `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (ID `1aKbLCYSxWlvcrvrL8lAvVpx8j2d5ngZD`, sửa lần cuối 31/8/2026 — KHÔNG đổi so với lần 24/9). **Đáp án:** `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi).
**Dòng so sánh gần nhất:** v2.24 / 24/9/2026 = 25/30 – 1/30 – 4/30 (trùng dòng v2.21 / 07/9/2026).

## 1. Điểm số

| Nhóm | 24/9 (v2.24) | 28/9 (v2.24) | Thay đổi |
|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | **25/30 (83,3%)** | Không đổi |
| Đúng phát hiện, sai mức | 1/30 (3,3%) | **1/30 (3,3%)** | Không đổi |
| Bỏ sót | 4/30 (13,3%) | **4/30 (13,3%)** | Không đổi |

**Kết luận: KHÔNG hồi quy.** Số lỗi Mức 1 bỏ sót không tăng (vẫn chỉ #1). Không gắn cờ xem xét thủ công bắt buộc.

| Trang | Kết quả |
|---|---|
| 1 — Hành chính (A) | 16/19 đúng + 1 sai mức (#12) + 2 bỏ sót (#1, #5) |
| 2 — Đảng ủy (B) | 5/6 đúng + 1 bỏ sót (#29) |
| 3 — Đoàn TN (D2) | 4/5 đúng + 1 bỏ sót (#30) |

## 2. Lỗi bỏ sót / sai mức (số #)

- **Bỏ sót:** #1 (lề 2cm, Mức 1), #5, #29, #30 (cỡ chữ trích yếu, Mức 3) — cả 4 đều là `FORMAT_BINARY_UNVERIFIED`: phiên cloud chỉ đọc được văn bản qua `read_file_content`, không chạy được `_read_input_properties.py` trên byte thật.
- **Sai mức:** #12 ("Công ty"/"Trung tâm") — đáp án Mức 4, phát hiện xếp Mức 3 (ranh giới 3↔4 đã ghi nhận từ v2.21, checklist chưa chỉnh).

**Phát hiện mới so với lần trước: KHÔNG có** (không lỗi mới bị bỏ sót, không lỗi mới bị chấm sai mức).

## 3. Ghi nhận ngoài điểm số

- Các tình huống ngoài 30 lỗi đáp án (căn cứ "bản mẫu trống 03-Templates", ghi chú tự xưng đã sửa QĐ 49→988, khối "PHIẾU RÀ SOÁT NỘI BỘ – ChatGPT – CHÍNH THỨC", VBHN 41 vs 14/VBHN-VPQH cho cùng Luật Kế toán, hoán đổi thể thức Công đoàn↔Đoàn TN, đoạn lạc ngữ cảnh "KTC-DIS-v1") vẫn hiện diện trong file test; được rà theo nguyên tắc v2.20/v2.21 và ghi nhận định tính như 24/9. Vẫn chưa có đáp án chính thức (#31 trở đi) nên không tính điểm.
- **Đồng bộ phiên bản (cần người quản trị xem):** Skill cài là v2.24 (14/9/2026), nhưng `MEMORY-INDEX.md` (ID `1JBOkvlprhGlzzRPpDYyzN1grkYB10d43`, sửa 28/9/2026) vẫn ghi "cập nhật gần nhất 09/9/2026, gói v2.22"; báo cáo 24/9 khi viện dẫn "MEMORY-INDEX cập nhật 13/9/2026" không khớp nội dung thật của tệp này. Quy tắc "5 nơi khớp phiên bản" của SKILL.md có dấu hiệu chưa được thực hiện. Chưa đọc Nhật ký (có 3 bản trùng tên, khác chủ sở hữu) nên không kết luận thêm.
- Khoảng trống đo v2.22–v2.23 và việc file test đổi tên/ID so với 07/9 (file v3.0 không còn) vẫn tồn tại như cảnh báo 24/9.

## 4. Giới hạn của lượt đo

- Không phải rà soát mù (đáp án đọc cùng phiên); không đọc được thuộc tính định dạng thật; chưa truy cập nội dung thật kho 01-04 trong lượt này (hồi quy chấm trên nội dung văn bản).
- Chưa cập nhật `BANG-CHI-SO-THEO-THOI-GIAN.md` (công cụ Drive không sửa nội dung tại chỗ). Dòng đề xuất thêm thủ công:

`| 28/9/2026 | **v2.24** | 25/30 (83,3%) = | 1/30 (3,3%) = | 4/30 (13,3%) = | Tác vụ tự động, đồng nhất 24/9 và 07/9. FORMAT_BINARY_UNVERIFIED: #1,5,29,30. Sai mức #12. |`

Không đóng gói lại `.skill`, không commit, không sửa file test/đáp án.

---
*Tác vụ tự động (scheduled task) — 28/9/2026. Không có người theo dõi trực tiếp.*
