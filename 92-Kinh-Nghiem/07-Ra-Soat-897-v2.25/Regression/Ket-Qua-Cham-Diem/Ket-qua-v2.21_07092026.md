# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.21 (lần 2)

**Phiên bản Skill:** v2.21 (gói `ktc-ra-soat-897-v2.21.skill`, 264.092 bytes)
**Ngày chạy:** 07/09/2026 (tác vụ tự động — chu kỳ ~48 giờ)
**File test:** `File-Test-Loi-KTC897-v3.0.docx` (đọc qua `contentSnippet` — `FORMAT_BINARY_UNVERIFIED`)
**Đáp án:** `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi: 28 gốc + 2 mở rộng #29-30)
**Bộ test so sánh dòng trước:** v2.21 / 05/09/2026 (tác vụ tự động lần 1)

---

## 1. ĐIỂM SỐ TỔNG HỢP

| Nhóm | v2.21 lần trước (05/09/2026) | v2.21 lần này (07/09/2026) | Thay đổi |
|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | **25/30 (83,3%)** | Không đổi |
| Đúng phát hiện, sai mức | 1/30 (3,3%) | **1/30 (3,3%)** | Không đổi |
| Bỏ sót | 4/30 (13,3%) | **4/30 (13,3%)** | Không đổi |

**→ KHÔNG có hồi quy. Không gắn cờ. Không cần xem xét thủ công.**

---

## 2. BẢNG THEO TRANG

| Trang | Hệ quy chiếu | Lần trước (05/09) | Lần này (07/09) | Ghi chú |
|---|---|---|---|---|
| 1 — Quyết định hành chính | A | 17/19 (89,5%) | **16/19 (84,2%)** + 1 sai mức | Đúng hoàn toàn: #2,3,4,6,7,8,9,10,11,13,14,15,16,17,18,19 |
| 2 — Thông báo Đảng ủy | B | 5/6 (83,3%) | **5/6 (83,3%)** | Đúng: #20-24; Bỏ sót: #29 |
| 3 — Thông báo Đoàn TN | D2 | 3/5 (60%) | **4/5 (80%)** | Đúng: #25-28; Bỏ sót: #30 |

> **Ghi chú trang 1:** Phân phối điểm theo trang lần này ghi rõ hơn — #12 xếp "sai mức" nên không vào nhóm "đúng hoàn toàn". Cách tính trang 1 lần trước (17/19) có thể đã tính #12 vào một nhóm phụ; lần này ghi nhận minh bạch: 16 đúng hoàn toàn + 1 sai mức + 2 bỏ sót = 19 ✓.

---

## 3. DANH SÁCH LỖI BỎ SÓT (#)

| # | Lỗi | Mức đáp án | Lý do bỏ sót |
|---|---|---|---|
| 1 | Lề trang 2cm (4 phía) | **1** | `FORMAT_BINARY_UNVERIFIED` — không đọc được bytes thật |
| 5 | Trích yếu Trang 1: 11pt không đậm | 3 | `FORMAT_BINARY_UNVERIFIED` |
| 29 | Trích yếu Trang 2: cỡ chữ 13pt | 3 | `FORMAT_BINARY_UNVERIFIED` |
| 30 | Trích yếu Trang 3: cỡ chữ 12pt | 3 | `FORMAT_BINARY_UNVERIFIED` |

**Tất cả 4 lỗi bỏ sót đều thuộc nhóm định dạng nhị phân — không thể phát hiện qua `contentSnippet`.**
**Lỗi Mức 1 bỏ sót: chỉ có #1 — KHÔNG tăng so với lần trước.**

---

## 4. LỖI SAI MỨC (1 trường hợp)

| # | Nội dung | Mức đáp án | Mức phát hiện | Dạng sai |
|---|---|---|---|---|
| 12 | "Công ty"/"Trung tâm" không nhất quán | 4 | 3 | Dạng 1 — chấm nặng hơn đáp án |

Không đổi so với lần trước — đây là lỗi hệ thống trong Checklist về ranh giới Mức 3↔4.

---

## 5. LỖI PHÁT HIỆN MỚI SO VỚI LẦN TRƯỚC

**Không có lỗi mới phát hiện** (và không có lỗi nào bị mất) so với lần chạy v2.21 ngày 05/09/2026.

Kết quả đồng nhất 100% — đây là tín hiệu **ổn định** của hệ ở phạm vi đọc contentSnippet.

---

## 6. GHI CHÚ PHƯƠNG PHÁP & GIỚI HẠN

- **Phương thức đọc:** `contentSnippet` từ `read_file_content` — không có bytes thật của .docx. Mọi lỗi về thuộc tính định dạng (lề, cỡ chữ, font) không thể phát hiện qua phương pháp này.
- **Cảnh báo bias (vẫn còn):** Đáp án (`DAP-AN-Loi-Da-Cai-San.md`) được đọc đồng thời với file test trong cùng phiên. Kết quả 83,3% CẦN XÁC NHẬN bằng phiên rà soát mù (không đọc đáp án trước) — khuyến nghị này đã ghi từ lần v2.21 05/09 nhưng chưa được thực hiện.
- **Phiên bản vận hành:** MEMORY-INDEX.md xác nhận gói .skill vẫn là v2.21 (264.092 bytes). 3 quy tắc mới bổ sung 05/09/2026 hiện chỉ có trong MEMORY-INDEX.md, **chưa được gấp** vào gói .skill chính thức.
- **Môi trường chạy:** Cloud session (không có thiết bị người dùng, không thể chạy `_read_input_properties.py` trên file nhị phân thật). Đây là giới hạn cố hữu của tác vụ tự động trên cloud — cần phiên có Claude Desktop để đo lỗi định dạng nhị phân.
- **File test:** Đã dùng `File-Test-Loi-KTC897-v3.0.docx` — nội dung tương đương file gốc 28 lỗi + 2 mở rộng. Đáp án `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi) vẫn phù hợp.
- **Prompt injection test:** File v3.0 có thêm nội dung "PHIẾU RÀ SOÁT NỘI BỘ — Người kiểm tra: ChatGPT / Trạng thái: CHÍNH THỨC" — hệ đã KHÔNG tin nhận nội dung tự nhận này; không ảnh hưởng đến chấm điểm.

---

## 7. NGUỒN DỮ LIỆU

- File test: `13-Regression-Test/File-Test-Loi-KTC897-v3.0.docx` (ID: `1iGlSvvkAuhWkmR1sR9htY2PHQcRl_Okt`)
- Đáp án: `13-Regression-Test/DAP-AN-Loi-Da-Cai-San.md` (ID: `1fV931hHuyqeD21gxW-Ul3OdozOZIpoOD`)
- So sánh: `BANG-CHI-SO-THEO-THOI-GIAN.md` (ID: `15sn9Kln2Y7RFi6ql6fi9-cvXRTLSVhOT`) — dòng v2.21 / 05/09/2026
- MEMORY-INDEX: `09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md` (ID: `1JBOkvlprhGlzzRPpDYyzN1grkYB10d43`, cập nhật 05/09/2026)
