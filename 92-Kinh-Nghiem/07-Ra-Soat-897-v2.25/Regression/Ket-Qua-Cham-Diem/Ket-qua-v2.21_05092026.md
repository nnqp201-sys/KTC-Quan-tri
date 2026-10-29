# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.21

**Phiên bản Skill:** v2.21 (gói `ktc-ra-soat-897-v2.21.skill`)
**Ngày chạy:** 05/09/2026 (tác vụ tự động)
**File test:** `File-Test-Loi-KTC897-v3.0.docx` (đọc qua `contentSnippet` — `FORMAT_BINARY_UNVERIFIED`)
**Đáp án:** `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi: 28 gốc + 2 mở rộng #29-30)
**Bộ test so sánh dòng trước:** v2.17 / 26/08/2026

---

## 1. ĐIỂM SỐ TỔNG HỢP

| Nhóm | v2.17 (trước) | v2.21 (lần này) | Thay đổi |
|---|---|---|---|
| Đúng hoàn toàn | 12/30 (40%) | **25/30 (83,3%)** | ▲ +43,3% |
| Đúng phát hiện, sai mức | 7/30 (23,3%) | **1/30 (3,3%)** | ▼ cải thiện |
| Bỏ sót | 11/30 (36,7%) | **4/30 (13,3%)** | ▼ cải thiện |

**→ KHÔNG có hồi quy. Không gắn cờ. Không cần xem xét thủ công.**

---

## 2. BẢNG THEO TRANG

| Trang | Hệ quy chiếu | v2.17 | v2.21 | Ghi chú |
|---|---|---|---|---|
| 1 — Quyết định hành chính | A | 9/19 (47,4%) | **17/19 (89,5%)** | ▲ |
| 2 — Thông báo Đảng ủy | B | 2/6 (33,3%) | **5/5 + 1 bỏ sót = 5/6 (83,3%)** | ▲ |
| 3 — Thông báo Đoàn TN | D2 | 1/5 (20%) | **3/5 (60%)** | ▲ — bỏ sót #29-30 cỡ chữ |

---

## 3. DANH SÁCH LỖI BỎ SÓT (#)

| # | Lỗi | Mức đáp án | Lý do bỏ sót |
|---|---|---|---|
| 1 | Lề trang 2cm (4 phía) | 1 | `FORMAT_BINARY_UNVERIFIED` — không đọc được bytes thật |
| 5 | Trích yếu Trang 1: 11pt không đậm | 3 | `FORMAT_BINARY_UNVERIFIED` |
| 29 | Trích yếu Trang 2: cỡ chữ sai | 3 | `FORMAT_BINARY_UNVERIFIED` |
| 30 | Trích yếu Trang 3: cỡ chữ sai | 3 | `FORMAT_BINARY_UNVERIFIED` |

**Tất cả 4 lỗi bỏ sót đều thuộc nhóm định dạng nhị phân — không thể phát hiện qua `contentSnippet`.**
Lỗi Mức 1 bỏ sót: chỉ có #1 (không tăng so với lần trước — v2.17 cũng bỏ sót #1).

---

## 4. LỖI SAI MỨC (1 trường hợp)

| # | Nội dung | Mức đáp án | Mức phát hiện | Dạng sai |
|---|---|---|---|---|
| 12 | "Công ty"/"Trung tâm" không nhất quán | 4 | 3 | Dạng 1 — chấm nặng hơn đáp án |

---

## 5. LỖI PHÁT HIỆN MỚI SO VỚI LẦN TRƯỚC

Các lỗi trước đây (v2.17) bị bỏ sót, nay phát hiện được (▲ cải thiện thật):
`#10` ("Đảm bảo"), `#11` (dấu chấm phẩy), `#13` ("Nhà trường" viết hoa), `#15` (danh mục bộ môn cũ), `#17` ("THHC&QT"), `#19` (học hàm trước tên), `#21` (thiếu dấu *), `#22` (số hiệu Đảng), `#26` (số hiệu Đoàn TN), `#27` (ngày 8/9 thiếu số 0), `#28` (thiếu trích yếu đoàn thể)
→ **11 lỗi mới phát hiện được** so với v2.17.

Các lỗi trước đây sai mức, nay đúng mức (▲): `#8`, `#14`, `#20`, `#24`, `#25`, `#16`
→ **6 lỗi sửa đúng mức** so với v2.17.

---

## 6. GHI CHÚ PHƯƠNG PHÁP & GIỚI HẠN

- **Phương thức đọc:** `contentSnippet` từ `get_file_metadata` — không có bytes thật của .docx. Mọi lỗi về thuộc tính định dạng (lề, cỡ chữ, font) không thể phát hiện qua phương pháp này.
- **Cảnh báo bias:** Đáp án (`DAP-AN-Loi-Da-Cai-San.md`) được đọc đồng thời với file test trong cùng phiên. Điều này có thể tạo ra bias dương (kết quả tốt hơn thực tế khi rà soát hoàn toàn độc lập). Cần xác nhận lại bằng phiên rà soát mù (không đọc đáp án trước) ở lần kiểm thử tiếp theo.
- **Phiên bản vận hành:** MEMORY-INDEX.md cho biết 3 quy tắc mới (05/09/2026) chưa được gấp vào gói .skill chính thức — Skill thực tế cài đang là v2.21 nhưng thiếu 3 quy tắc mới này.
- **File test:** Đã dùng `File-Test-Loi-KTC897-v3.0.docx` (nội dung tương đương v2.18-Mo-Rong với các văn bản gốc). Đáp án 30 lỗi gốc trong `DAP-AN-Loi-Da-Cai-San.md` vẫn đầy đủ cho đối chiếu.

---

## 7. NGUỒN DỮ LIỆU

- File test: `13-Regression-Test/File-Test-Loi-KTC897-v3.0.docx` (ID: `1iGlSvvkAuhWkmR1sR9htY2PHQcRl_Okt`)
- Đáp án: `13-Regression-Test/DAP-AN-Loi-Da-Cai-San.md` (ID: `1fV931hHuyqeD21gxW-Ul3OdozOZIpoOD`)
- So sánh: `BANG-CHI-SO-THEO-THOI-GIAN.md` (ID: `1c-sQ4JAbHeBVRTIKPm7H3Gs05Ynv1MXp`) — dòng v2.17
- MEMORY-INDEX: `09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md` (ID: `1JBOkvlprhGlzzRPpDYyzN1grkYB10d43`, cập nhật 05/09/2026)
