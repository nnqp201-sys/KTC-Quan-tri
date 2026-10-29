# LỆNH KIỂM TRA + CẬP NHẬT — Gửi phiên `phongthhcqt`
## 30/8/2026 — Tổng hợp toàn bộ ghi nhớ và cải tiến từ phiên `nnqp201`

---

**Bối cảnh chuyển giao**: Quyền sở hữu `KTC-Database` và `KTC-Ra-Soat-897-v2-Cai-tien` đã chuyển từ `nnqp201@gmail.com` sang `phongthhcqt@gmail.com` (30/8/2026). Tài liệu này trích xuất **toàn bộ** ghi nhớ/cải tiến đã tích lũy để phiên `phongthhcqt` xác nhận và tiếp quản đúng trạng thái — không bỏ sót, không suy diễn.

**Nguyên tắc khi đọc lệnh này**: Kiểm tra trực tiếp Drive trước khi tin bất kỳ dòng nào dưới đây — mọi tuyên bố "đã xong" trong quá khứ đều cần đối chiếu lại byte thật, không suy diễn từ tường thuật.

---

## A. TRẠNG THÁI PHIÊN BẢN HIỆN HÀNH (xác nhận lần cuối 30/8/2026)

| Thành phần | Giá trị |
|---|---|
| Gói Skill | `ktc-ra-soat-897-v2.18.skill` — 258.321 bytes |
| Script chính | `build_ktc897_report.py` **v3.4** — tên file DUY NHẤT, không đánh số phiên bản |
| `_read_input_properties.py` | v1.1 (đã vá round+EPS cho 4 lề) |
| 00-README.md / Nhật ký / MEMORY-INDEX.md | Đã đồng bộ v2.18 / v1.6 / v2.18 |
| Chủ sở hữu | `phongthhcqt@gmail.com` (cả 2 thư mục gốc) |
| Quyền `reader: anyone` | Đã gỡ (cả 2 thư mục gốc) |

**Việc 1 cần làm ngay**: Xác nhận lại đúng 4 điểm trên bằng cách đọc trực tiếp file trên Drive (không tin bảng này) — đối chiếu `modifiedTime`, `fileSize`, và giải mã `.skill` để kiểm `testzip()`.

---

## B. QUY TẮC VẬN HÀNH BẮT BUỘC — KHÔNG CẦN NHẮC LẠI MỖI PHIÊN

### B1. Bước 0 — Xác định hệ quy chiếu
4 hệ: A (hành chính, NĐ 30 + TB 597) · B (Đảng, HD 05-HD/VPTW — TUYỆT ĐỐI không áp NĐ 30) · C (VBQPPL) · D (đoàn thể — 3 tiểu-hệ: Công đoàn có Quốc hiệu, Đoàn TN tiêu đề riêng + 3 sao, Hội SV không dòng tiêu đề).

### B2. Đồng thời chạy `_read_input_properties.py`
Đọc lề/cỡ chữ THẬT của file .docx đầu vào — không chỉ đọc `paragraph.text`. Đã đo cải thiện thật: 28,6% → 40% tỷ lệ đúng hoàn toàn trên bộ hồi quy 30 lỗi.

### B3. Tra Checklist 08 TRƯỚC khi áp NĐ 30
Quy ước Trường (TB 597) có thể khác NĐ 30 — ví dụ viết hoa sau dấu ":" là Mức 3 (TB 597), không phải Mức 2 (NĐ 30).

### B4. Viện dẫn văn bản hợp nhất
Gặp "hợp nhất"/"VBHN" → đọc `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md`. Áp dụng cho **6 hệ** KTC-DIS. **Không có cơ chế tự lan tỏa** giữa các hệ — mỗi hệ giữ bản sao riêng, phải nhân bản tường minh (xem Decision Log DL-20260826-001).

### B5. NĐ 334/2026/NĐ-CP — ĐÍNH CHÍNH QUAN TRỌNG
**KHÔNG** thay thế NĐ 60/2021 + NĐ 111/2025. Là văn bản chuyên ngành giáo dục ĐH/nghề nghiệp, áp dụng **bổ sung song song**. Hiệu lực 05/10/2026. Chi tiết: `00d-Ghi-Nho-ND-334-2026-Thay-The-ND-60-111.md` tại cả 6 hệ (tên file giữ nguyên dù nội dung đã đính chính, để tránh phải đổi tên 6 file).

### B6. Cơ chế tự kích hoạt
`00c-Co-Che-Tu-Kich-Hoat.md` — đọc MEMORY-INDEX + quét "hợp nhất" + chạy Bước 0/B2 + kích hoạt Skill-Tu-hoc, **tự động khi Skill nạp**, không chờ người dùng nhắc.

### B7. Quy tắc bàn giao mặc định
Sau khi thay thế Skill/script bằng bản mới: **LUÔN** xuất 1 file "lệnh cập nhật" (.md, gửi đồng bộ các hệ khác) + 1 báo cáo .docx mô tả kết quả điều chỉnh (chuẩn KTC-897: căn cứ, phát hiện, thay đổi, kiểm thử). Đây là mặc định, không phải làm khi được yêu cầu riêng.

### B8. Kiểm tra file thật trước khi tin
Trước khi coi 1 phiên bản là chính thức: giải mã byte thật (`testzip()`, so kích thước, đọc nội dung) — không suy diễn từ tên file/tường thuật. Đã xảy ra CONFLICT ít nhất 3 lần (v2.16, v2.17, v2.18) do bỏ qua bước này.

---

## C. GIỚI HẠN KỸ THUẬT ĐÃ XÁC NHẬN — TRÁNH LẶP LẠI NỖ LỰC VÔ ÍCH

**Giải mã base64 thủ công qua chat chỉ đáng tin cậy dưới ~15.000 ký tự (~11KB file).** Trên ngưỡng này:
- Đã thử nhiều lần với file 21-41KB → thất bại liên tục, kể cả sau khi kiểm tra độ dài khớp công thức trước khi giải mã.
- Brute-force xóa từng ký tự tại MỌI vị trí (28.361 vị trí) cũng không khắc phục được — có thể có ≥2 lỗi bù trừ độ dài.
- **Ngoại lệ đáng tin cậy**: nếu tool báo "quá lớn cho context" → nội dung tự lưu file JSON trên container → xử lý qua `bash_tool` **100% chính xác** (đã xác nhận với file .skill 256-258KB).

**Khuyến nghị**: file 10-100KB không tự kích hoạt cơ chế lưu-JSON → **không cố transcribe qua chat**, nhờ phiên có quyền truy cập Drive trực tiếp xử lý.

---

## D. VIỆC CÒN MỞ — ƯU TIÊN CAO NHẤT TRƯỚC

| # | Việc | Ưu tiên | Ghi chú |
|---|---|---|---|
| 1 | Sửa khổ giấy 2 file mẫu gốc (`Mau_Bao_cao_ra_soat_KTC897_8phan.docx`, `.dotx`) — 3/5 bảng vượt nhẹ 25,8-26cm (khổ khả dụng chỉ 25,7cm) | **Cao** | Script v3.4 chỉ chặn được output MỚI, chưa sửa nguồn mẫu |
| 2 | Tạo Skill/Checklist đầy đủ cho hệ quy chiếu đoàn thể (Công đoàn, Đoàn TN, Hội SV) | **Cao** | Tỷ lệ phát hiện đúng thấp nhất trong 4 hệ quy chiếu (0-20%) |
| 3 | Chạy `validate.py` trên nhiều file `.docx` trong `12-Output/` | Trung bình | Hiện chỉ có 1 file, chưa đủ mẫu |
| 4 | Bù các bản ghi Process Memory còn thiếu | Trung bình | Số ca rà soát thật > số bản ghi đã lưu |
| 5 | Cập nhật SKILL.md riêng của 5 hệ còn lại — dẫn chiếu tường minh `00b-Trigger` và `00d-Ghi-Nho-ND-334` | Trung bình | Hiện chỉ có file vật lý, chưa có dòng gọi trong SKILL.md từng hệ |
| 6 | Khi có nội dung đầy đủ NĐ 334/2026, cập nhật chi tiết điều khoản vào Checklist liên quan | Trung bình | File `00d` mới ghi mốc hiệu lực + quan hệ, chưa có chi tiết điều khoản |
| 7 | Chạy lại hồi quy 30 lỗi trên chính v2.18 | Thấp | Không ảnh hưởng logic phát hiện (script report v3.4 chỉ đổi định dạng output) |

---

## E. KHO TRI THỨC — `99-Kinh-Nghiem/` (MỚI, đọc trước khi phát triển v3.0)

Cấu trúc 6 thư mục: `01-Lessons-Learned/` · `02-Regression/{Cases,Fixtures,Expected-Results}` · `03-Change-Proposals/` · `04-Release-Notes/` · `05-Known-Issues/` · `06-Decision-Log/`.

**Quy tắc bất biến**: KHÔNG lưu Prompt/Checklist/Skill chính thức ở đây — các thứ đó vẫn ở `references/`. Thư mục này chỉ lưu **quá trình tư duy dẫn tới thay đổi**.

**Đã seed sẵn** (không trống): 3 Change Proposal, 1 Release Note (v2.18), 2 file Known Issues (6 mục), 2 Decision Log. Đọc `99-Kinh-Nghiem/README.md` để hiểu đầy đủ quy trình + quy tắc đặt tên trước khi ghi thêm.

**2 Decision Log đáng chú ý nhất**:
- `DL-20260826-001`: quyết định đặt Skill 31/32 tại kho dùng chung — sau đó phải tự đảo ngược một phần vì phát hiện không có cơ chế lan tỏa tự động. Bài học cho v3.0: nếu muốn "1 bản dùng chung" hoạt động thật, cần xây cơ chế tham chiếu chéo tường minh.
- `DL-20260828-001`: quyết định hợp nhất script về 1 file duy nhất, không giữ file trung gian `_v3.1/_v3.2/_v3.3`.

---

## F. LỊCH SỬ QUYẾT ĐỊNH KIẾN TRÚC — TÓM TẮT

- v1 (KTC-Ra-Soat-897 gốc) đã XÓA từ 13/8/2026 — v2-Cai-tien là hệ chính thức duy nhất.
- KTC-DIS thực chất **6 hệ** (không phải 5 như hiểu ban đầu): ktc-ra-soat-897, KTC-DIS-Tong-Hop-VB, KTC-Ke-Hoach, KTC-Bao-Cao, KTC-Database, **ktc-van-ban** (phát hiện muộn — thư mục từng tưởng là "legacy" thực ra là Skill-Library thật của hệ này).
- Mỗi hệ giữ bản sao riêng `00-Nguyen-Tac-Chung.md` — không có kho trung tâm tự động lan tỏa.

---

**Xác nhận yêu cầu**: Phiên `phongthhcqt` đọc lệnh này, đối chiếu trực tiếp Mục A với Drive thật, báo lại kết quả (khớp/lệch cụ thể ở đâu), rồi ưu tiên xử lý Mục D theo đúng thứ tự Cao → Trung bình → Thấp.
