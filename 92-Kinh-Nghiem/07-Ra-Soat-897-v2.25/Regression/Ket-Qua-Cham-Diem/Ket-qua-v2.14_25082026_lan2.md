Phương thức đọc file: ĐỌC TRỰC TIẾP — dùng `Google Drive:get_file_metadata` trên fileId thật của `File-Test-Loi-KTC897.docx` (13-Regression-Test/), trường `contentSnippet` trả về toàn bộ nội dung text đã trích xuất sẵn từ .docx, không qua giải mã base64 thủ công. Đã xác nhận đọc đủ 3 trang / 3 văn bản.

Phiên bản: v2.14
Ngày chạy: 25/8/2026 (lần 2 — đã hiệu chỉnh số học sau xác nhận #16, #24)
Điểm: 8/28 đúng hoàn toàn, 7/28 đúng nhưng sai mức, 13/28 bỏ sót
Danh sách lỗi bỏ sót: #1, #5, #10, #11, #13, #15, #17, #19, #21, #22, #26, #27, #28
Danh sách false positive: 3 trường hợp
Nhận xét: xem Mục 6, 7, 8

> **Đã hiệu chỉnh so với bản trước cùng tên**: #16 và #24 chuyển từ nhóm phụ "đúng mức nhưng sai chi tiết" vào nhóm chuẩn **"Đúng phát hiện, sai mức"** — quyết định để khớp đúng 3 nhóm chấm điểm gốc trong `DAP-AN-Loi-Da-Cai-San.md`. Nhóm "sai mức" từ 5 tăng lên **7** mục.

═══════════════════════════════════════════════════════════════════
GHI CHÚ PHÂN LOẠI #16 VÀ #24 — 2 DẠNG "SAI MỨC" KHÁC NHAU
═══════════════════════════════════════════════════════════════════

Nhóm "Đúng phát hiện, sai mức" (7 mục) gồm 2 dạng con, cần phân biệt khi đọc lại về sau:

**Dạng 1 — Sai mức về thang phân loại 1-4** (5 mục: #8, #12, #14, #20, #25): hệ chấm sai số Mức (ví dụ đáp án Mức 2, hệ chấm Mức 1). Bản chất: hệ *hiểu đúng* vấn đề nhưng *ước lượng sai mức độ nghiêm trọng*.

**Dạng 2 — Sai mức về nội dung kiến nghị/số liệu** (2 mục: #16, #24): hệ chấm ĐÚNG Mức (số trùng đáp án), nhưng **kiến nghị sửa cụ thể sai hoặc không đủ để khắc phục đúng bản chất lỗi**:
- **#16**: Mức đúng (1=1), nhưng số liệu "đúng" đề xuất là 4, trong khi đáp án ghi tối đa 15 — nếu người dùng làm theo kiến nghị của hệ, kết quả vẫn sai.
- **#24**: Mức đúng (2=2), nhưng kiến nghị "đổi thành T/M. ĐẢNG ỦY" đi xa hơn yêu cầu thực tế (chỉ cần đổi KT.→K/T., giữ nguyên "PHÓ BÍ THƯ") — có thể khiến người dùng sửa nhầm sang cấu trúc thẩm quyền khác.

**Lý do gộp cả 2 dạng vào cùng 1 nhóm "sai mức"** thay vì tạo nhóm thứ 4: bản chất đo lường của thang chấm 3 nhóm là "báo cáo này có dùng được ngay không" — không chỉ đo "có nhận diện đúng vị trí lỗi không". Cả 2 dạng đều có đặc điểm chung: nếu người nhận báo cáo áp dụng kiến nghị mà không tự kiểm tra lại, kết quả cuối vẫn sai. Về hiệu quả sử dụng thực tế, dạng 2 không khác gì "sai mức" theo dạng 1.

═══════════════════════════════════════════════════════════════════
1. ĐỐI CHIẾU ĐẦY ĐỦ 28/28 — THEO TỪNG TRANG (ĐÃ HIỆU CHỈNH)
═══════════════════════════════════════════════════════════════════

## TRANG 1 — Quyết định hành chính (19 lỗi: #1–19)

| # | Nội dung | Mức đáp án | Kết quả |
|---|---|---|---|
| 1 | Lề trang cứng 2cm | 1 | ❌ MISSED |
| 2 | "UỶ BAN" thiếu dấu hỏi | 2 | ✅ CORRECT |
| 3 | "CỘNG HOÀ" thiếu dấu hỏi | 2 | ✅ CORRECT |
| 4 | Ngày 5/2 thiếu số 0 | 2 | ✅ CORRECT |
| 5 | Trích yếu cỡ chữ 11 | 3 | ❌ MISSED |
| 6 | QĐ 49 hết hiệu lực | 1 | ✅ CORRECT — **PASS trọng điểm** |
| 7 | NĐ 60/2021 thiếu NĐ 111/2025 | 1 | ✅ CORRECT |
| 8 | Sai số 1229→1299 | 2 | ⚠️ SAI MỨC — dạng 1 (tôi:1) |
| 9 | Tên Cơ sở 4 cũ | 1 | ✅ CORRECT |
| 10 | "Đảm bảo"/"Bảo đảm" | 3 | ❌ MISSED |
| 11 | Dấu chấm phẩy | 3 | ❌ MISSED |
| 12 | Công ty/Trung tâm | 4 | ⚠️ SAI MỨC — dạng 1 (tôi:3) |
| 13 | Viết hoa "Nhà trường" | 3 | ❌ MISSED |
| 14 | Câu cụt "theo định" | 4 | ⚠️ SAI MỨC — dạng 1 (tôi:3) |
| 15 | Danh mục bộ môn cũ | 3 | ❌ MISSED |
| 16 | Định mức tính sai | 1 | ⚠️ SAI MỨC — **dạng 2** (Mức đúng, số liệu sai: tôi 4, đáp án 15) |
| 17 | Nơi nhận sai cột viết tắt | 2 | ❌ MISSED |
| 18 | "K/T." nên "KT." | 2 | ✅ CORRECT |
| 19 | "TS." học hàm | 2 | ❌ MISSED |

**Trang 1: 7 đúng hoàn toàn / 19 = 36,8%** *(không đổi — #16 chưa từng thuộc nhóm "đúng")*

## TRANG 2 — Thông báo Đảng ủy (5 lỗi: #20–24)

| # | Nội dung | Mức đáp án | Kết quả |
|---|---|---|---|
| 20 | Lặp dòng "ĐẢNG ỦY..." | 2 | ⚠️ SAI MỨC — dạng 1 (tôi:1) |
| 21 | Thiếu dấu sao (*) | 2 | ❌ MISSED |
| 22 | Sai định dạng số hiệu Đảng | 2 | ❌ MISSED |
| 23 | Tự kết luận tổ chức Đảng | 1 (nếu tự kết luận) | ✅ CORRECT — **PASS quan trọng nhất** |
| 24 | "KT. BÍ THƯ" nên "K/T." | 2 | ⚠️ SAI MỨC — **dạng 2** (Mức đúng, kiến nghị sai hướng) |

**Trang 2: 1 đúng hoàn toàn / 5 = 20%** *(giữ nguyên — KHÔNG phải 40% như bản nháp lệnh trước đó ghi nhầm; #24 nằm ở nhóm "sai mức", không phải nhóm "đúng")*

## TRANG 3 — Thông báo Đoàn Thanh niên (4 lỗi: #25–28)

| # | Nội dung | Mức đáp án | Kết quả |
|---|---|---|---|
| 25 | Quốc hiệu cho Đoàn TN | 2 | ⚠️ SAI MỨC — dạng 1 (tôi:1) |
| 26 | Sai định dạng số hiệu đoàn thể | 2 | ❌ MISSED |
| 27 | Ngày 8/9 thiếu số 0 | 2 | ❌ MISSED |
| 28 | Thiếu trích yếu chuẩn đoàn thể | 4 | ❌ MISSED |

**Trang 3: 0 đúng hoàn toàn / 4 = 0%** *(không đổi)*

═══════════════════════════════════════════════════════════════════
2. TỔNG HỢP CUỐI CÙNG (KHỚP 28/28)
═══════════════════════════════════════════════════════════════════

| Nhóm | Số # | Tổng |
|---|---|---|
| Đúng hoàn toàn | 2,3,4,6,7,9,18,23 | 8 |
| Đúng phát hiện, sai mức (dạng 1: 5 mục + dạng 2: 2 mục) | 8,12,14,20,25,16,24 | 7 |
| Bỏ sót hoàn toàn | 1,5,10,11,13,15,17,19,21,22,26,27,28 | 13 |
| **TỔNG** | | **28** ✓ |

═══════════════════════════════════════════════════════════════════
3. BẢNG THEO TRANG — TÍN HIỆU QUAN TRỌNG NHẤT (KHÔNG ĐỔI SO VỚI LẦN TRƯỚC)
═══════════════════════════════════════════════════════════════════

| Trang | Hệ quy chiếu | Số lỗi | Đúng hoàn toàn | Tỷ lệ |
|---|---|---|---|---|
| 1 | Hành chính (A) | 19 | 7 | 36,8% |
| 2 | Đảng (B) | 5 | 1 | 20% |
| 3 | Đoàn thể (D) | 4 | 0 | **0%** |

Việc chuyển #16, #24 sang nhóm "sai mức" **không làm thay đổi bảng theo trang này** — vì cả hai mục chưa bao giờ được tính vào nhóm "đúng hoàn toàn" ở cả 2 phiên bản trước. Sự "giảm dần theo hệ quy chiếu" (36,8% → 20% → 0%) là tín hiệu ổn định, đáng tin cậy qua cả 2 lần tính.

═══════════════════════════════════════════════════════════════════
4-8. (Giữ nguyên nội dung phân tích Bước 0, false positive, kết luận — xem bản gốc lần 2 để tránh trùng lặp; chỉ có bảng số liệu ở trên là phần được hiệu chỉnh chính thức.)
═══════════════════════════════════════════════════════════════════
