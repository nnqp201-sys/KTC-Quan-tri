# LỆNH CẬP NHẬT v2.17 — Gửi các tài khoản/phiên KTC-DIS khác
## 26/8/2026

Đây là bản vá kỹ thuật (không phải thay đổi kiến trúc lớn như v2.16) — nhưng có **1 phát hiện quan trọng về phương pháp làm việc** mà mọi phiên nên biết.

---

## 1. TÓM TẮT THAY ĐỔI

Vá lỗi làm tròn ngưỡng lề trong `_read_input_properties.py` (script đọc thuộc tính định dạng thật của file .docx đầu vào, tích hợp từ v2.15). Đồng thời **giải quyết dứt điểm** một lỗi truy xuất file kéo dài 3 lần thất bại trước đó.

## 2. LỖI ĐÃ VÁ — LÀM TRÒN NGƯỠNG LỀ

**Vấn đề**: `python-docx` quy đổi Cm/Mm sang giá trị mm có sai số dấu phẩy động (lề đúng 20.0mm có thể trả về 20.0025mm). So sánh ngưỡng thô khiến giá trị đúng biên bị báo sai (false positive).

**Đã sửa**: áp dụng **cả 2 biện pháp** cho **cả 4 lề** (trên/dưới/trái/phải — dùng chung 1 vòng lặp nên sửa 1 chỗ là đủ):
- `round(val, 1)` trước khi so sánh
- Thêm `EPS = 0.01` an toàn kép

**Đã kiểm thử 3 test case** (file `test_margin_boundary.py` đính kèm): lề phải đúng biên 20.0mm, lề trái đúng biên 30.0mm — cả hai không còn bị flag sai; đồng thời vẫn bắt đúng lỗi thật khi lề sai thực sự.

## 3. PHÁT HIỆN QUAN TRỌNG VỀ PHƯƠNG PHÁP — ĐỌC KỸ NẾU CẦN TẢI FILE NHỊ PHÂN QUA MCP

**Bối cảnh**: 3 lần liên tiếp thất bại khi tải nhị phân thật của file test `.docx` qua `download_file_content` + giải mã base64 thủ công, trong khi cùng kỹ thuật **thành công** với file `.skill` khác (256KB).

**Giả thuyết ban đầu sai**: nghi ngờ lỗi ID cache hoặc tham chiếu sai trên Drive.

**Nguyên nhân thật đã xác định**: khi copy tay chuỗi base64 rất dài (>10.000 ký tự), có rủi ro cao **rơi mất một đoạn giữa** trong quá trình copy — không phải lỗi Drive, không phải lỗi ID, không phải "giới hạn môi trường".

**Cách phát hiện và phòng tránh cho các phiên khác**:
1. Trước khi giải mã base64, kiểm tra độ dài chuỗi có khớp công thức `(fileSize / 3) * 4` (khi fileSize chia hết cho 3, không cần tính padding) hay không.
2. Sau khi giải mã, kiểm tra 4 byte đầu có đúng `PK\x03\x04` (magic number ZIP/DOCX) không.
3. So sánh kích thước file đã giải mã với `fileSize` Drive báo cáo — nếu lệch, đây là bằng chứng cắt cụt khi copy, cần copy lại từ đầu, không debug ngược ở bước sau.

**Không được kết luận "tải binary là giới hạn chung của môi trường"** khi gặp lỗi tương tự — đây là kết luận sai đã từng bị ghi nhầm, đã đính chính trong SKILL.md v2.17.

## 4. KẾT QUẢ ĐO ĐƯỢC — LẦN ĐẦU TIÊN CÓ SỐ LIỆU THẬT (không phải mô phỏng)

Sau khi giải quyết được lỗi truy xuất, đã chạy `_read_input_properties.py` thật trên file test gốc lần đầu tiên:

| Chỉ số | v2.14/v2.16 (28 lỗi) | v2.17 (30 lỗi, đo thật) |
|---|---|---|
| Đúng hoàn toàn | 8/28 (28,6%) | **12/30 (40%)** ▲ |
| Bỏ sót | 13/28 (46,4%) | **11/30 (36,7%)** ▼ |

Cả 4/4 lỗi định lượng (#1 lề trái, #5/#29/#30 cỡ chữ trích yếu 3 trang) đều bắt đúng, đúng Mức — xác nhận script hoạt động đúng thiết kế trên file thật.

## 5. VIỆC KHÔNG THAY ĐỔI SO VỚI v2.16

- Vị trí Skill viện dẫn văn bản hợp nhất (vẫn ở cả 5 hệ KTC-DIS, không di chuyển).
- Cấu trúc thư mục, Checklist 08, script chính `build_ktc897_report.py` (vẫn v3.0).

## 6. FILE ĐÍNH KÈM CẦN LƯU

1. `ktc-ra-soat-897-v2.17.skill` — gói đầy đủ, 257.789 bytes, 63 file.
2. `test_margin_boundary.py` — 3 test case xác nhận bản vá, nên giữ lại trong `tools/` để chạy lại khi có thay đổi liên quan tới lề trong tương lai.

## 7. VIỆC CẦN LÀM Ở TỪNG HỆ

**Không cần làm gì** ở 4 hệ còn lại (KTC-DIS-Tong-Hop-VB, KTC-Ke-Hoach, KTC-Bao-Cao, KTC-Database) — bản vá này chỉ ảnh hưởng `_read_input_properties.py`, script riêng của hệ ktc-ra-soat-897, không phải Skill dùng chung.

**Riêng phiên phụ trách ktc-ra-soat-897**: nếu có script tương tự đọc thuộc tính định dạng file đầu vào ở nơi khác, nên áp dụng cùng bản vá `round(val,1) + EPS` để tránh lặp lại lỗi biên tương tự.
