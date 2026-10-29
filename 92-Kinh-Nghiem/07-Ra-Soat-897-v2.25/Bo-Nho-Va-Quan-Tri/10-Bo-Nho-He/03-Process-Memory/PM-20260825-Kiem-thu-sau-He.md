# PM-20260825-Kiem-thu-sau-He
## Process Memory — Ca kiểm thử sâu toàn hệ KTC-Ra-Soat-897-v2

| Trường | Nội dung |
|---|---|
| **Ngày** | 25/8/2026 |
| **Tác vụ** | (a) Rà soát chính thức trước khi trình ký + kiểm thử toàn hệ + vá lỗi + đóng gói |
| **Hồ sơ** | `File-Test-Loi-KTC897.docx` — 03 văn bản: QĐ 45/QĐ-CĐKT, TB 12/TB-ĐU, TB 08/TB-ĐTN |
| **Phiên bản đã dùng** | Skill v2.14 · Checklist 08 v2.8 · Skill-Tu-hoc v1.4 · script `build_ktc897_report.py` v3.0 |
| **Đầu ra** | `Bao_cao_ra_soat_File-Test-Loi-KTC897_20260825.docx` (8 trang, A4 ngang) |

---

## 1. Các bước đã chạy

1. Đọc `MEMORY-INDEX.md` → phát hiện CONFLICT phiên bản giữa 4 tài liệu điều khiển.
2. Kiểm tra thực tế trên Drive (`parentId` query) → phát hiện `build_ktc897_report.py` **không tồn tại**, `10-Bo-Nho-He/` nằm sai vị trí so với mô tả.
3. Bước 0 — tách 03 hệ quy chiếu của hồ sơ đầu vào.
4. Tra `Checklist 08` TRƯỚC khi xác định căn cứ lỗi hình thức.
5. Hợp nhất script v3.0, viết `run_review.py` dựng báo cáo thật.
6. Render PDF, rasterize 12 trang, soi trực quan → **phát hiện lỗi width bảng**.
7. Vá lỗi (`autofit=False` + `tblLayout fixed` + `gridCol w:w`), chạy lại → còn 8 trang.
8. Cập nhật SKILL.md v2.14, đóng gói `.skill`, ghi đè 4 tài liệu điều khiển lên Drive.

## 2. Nguồn/căn cứ đã kiểm tra
`01-Legal-Database`: NĐ 30/2020, NĐ 60/2021 + NĐ 111/2025, QĐ 10/2026/QĐ-TTg · `02-KTC-Regulations`: QĐ 988, QĐ 1299, QĐ 1355, TB 597 · `references/Checklist/08-Quy-Uoc-Rieng-CDKT.md` · HD 05-HD/VPTW · QĐ 208-QĐ/TW.

## 3. Phát hiện chính trên hồ sơ đầu vào

| Mức | Số lượng | Nội dung tiêu biểu |
|---|---|---|
| **Mức 1** | 7 | Căn cứ QĐ 49 đã bị QĐ 988 thay thế · NĐ 60/2021 thiếu NĐ 111/2025 · sai số hiệu 1229 (đúng: 1299) · tên cũ Cơ sở 4 · định mức photocopy vượt 16 máy do làm tròn lẻ · TB đoàn thể dùng Quốc hiệu thay vì "ĐOÀN TNCS HỒ CHÍ MINH" · TB đoàn thể thiếu hoàn toàn người ký |
| **Mức 2** | 6 | "K/T." thay vì "KT." · ngày 5/2 không thêm số 0 · "UỶ BAN"/"CỘNG HOÀ" thiếu dấu hỏi · nơi nhận sai và lặp · thể thức ký VB Đảng · mâu thuẫn ngày ban hành vs "hè 2026" |
| **Mức 3** | 3 | Viết thường sau ":" (TB 597 Mục 3.1) · lẫn "Công ty"/"Trung tâm" · câu cụt "theo định" |
| **Mức 4** | 3 | Văn phong Điều 3 · tên gọi tổ chức Đảng chờ xác minh |

**Điểm chất lượng hồ sơ**: 47/100 — CHƯA ĐẠT, CHƯA SẴN SÀNG TRÌNH KÝ.

## 4. Quyết định phân loại mức đáng ghi nhớ

- **Viết thường sau ":"** → xếp **Mức 3** (quy ước TB 597), KHÔNG phải Mức 2 (NĐ 30). Đây là lần thứ ba quy tắc này được áp đúng — đã ổn định.
- **Tên gọi tổ chức Đảng** → xếp **Mức 4** và ghi "chờ xác minh", không tự kết luận dù có hai khả năng đều có căn cứ.
- **TB đoàn thể dùng Quốc hiệu** → **Mức 1** vì sai hệ thể thức gốc, không phải lỗi trình bày nhỏ.

## 5. Lỗi của chính Hệ đã phát hiện và tự sửa trong ca này

| # | Lỗi | Cách phát hiện | Đã sửa |
|---|---|---|---|
| 1 | `build_ktc897_report.py` được khai là script chính trong 3 tài liệu nhưng không tồn tại trên Drive | Truy vấn `parentId` thư mục `tools/` | Hợp nhất và tạo thật, v3.0 |
| 2 | Width bảng không áp dụng — bảng co còn ~87%, báo cáo phình 12 trang | Render PDF và soi trực quan từng trang | Thêm `autofit=False` + `tblLayout fixed` + `gridCol w:w` → về 8 trang |
| 3 | `10-Bo-Nho-He/` được mô tả ở thư mục gốc, thực tế nằm trong `09-Quan-Tri-He/` | Tìm kiếm Drive theo tên | Đính chính trong SKILL.md, README, MEMORY-INDEX |
| 4 | v2.13 đóng gói nhưng changelog để trống | Đọc SKILL.md đính kèm | Bổ sung ngược changelog tại v2.14 |

## 6. Vấn đề còn mở

1. Bù các bản ghi Process Memory còn thiếu cho hơn 15 ca rà soát trước.
2. Tạo Skill/Checklist đầy đủ cho hệ quy chiếu đoàn thể — hiện chỉ dựa mẫu 3.1–3.3 TB 597.
3. Bổ sung 3 quy tắc mới vào Checklist 08 / 03-Phap-Ly / 02-Noi-Dung (trích số kèm ngày · cặp văn bản gốc–sửa đổi · định mức tính gộp).
4. Xác minh tên gọi tổ chức Đảng với Ban Tổ chức Tỉnh ủy.
5. Dọn kho `03-Templates` — 10/11 thư mục con chứa văn bản thật thay vì mẫu trống.

## 7. Hành động tiếp theo
Ưu tiên mục 3 (bổ sung Checklist) vì ba lỗi Mức 1 trong ca này đều thuộc nhóm đó và sẽ tái diễn nếu không đưa vào checklist chính thức.

## 8. Liên kết đầu ra
- Gói Skill: `ktc-ra-soat-897-v2.14.skill` (thư mục gốc)
- Script: `tools/build_ktc897_report.py` v3.0
- Báo cáo rà soát: `12-Output/Bao_cao_ra_soat_File-Test-Loi-KTC897_20260825.docx`

## 9. Quan hệ thay thế
`supersedes`: không · `superseded_by`: chưa có
