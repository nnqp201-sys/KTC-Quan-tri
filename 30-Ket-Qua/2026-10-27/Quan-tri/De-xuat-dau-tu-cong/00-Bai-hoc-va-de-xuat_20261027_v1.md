# Bài học và đề xuất từ phiên làm việc Dự án CLC 2026-2030 (14/10 - 27/10/2026)

Phạm vi: các sản phẩm đã làm cho Dự án "Đầu tư, cải tạo ... trường cao đẳng chất lượng cao giai đoạn 2026 - 2030" (CTMTQG): QĐ 2158/2161, KHLCNT (QĐ 2236), Tờ trình 16, báo cáo giải ngân tháng 9, kiểm tra hồ sơ năng lực, Phiếu trình và QĐ 2374/2375.
Trạng thái: **đề xuất, chưa kích hoạt** — người phụ trách duyệt rồi mới chép vào `.claude/` (xem mục 5).

## 1. Chuỗi việc của một dự án đầu tư công ở giai đoạn chuẩn bị đầu tư (đã chạy thật)

| Bước | Văn bản/việc | Căn cứ hay vướng | Hạn |
|---|---|---|---|
| 1 | QĐ nhiệm vụ và dự toán CBĐT (QĐ 2158) | NĐ 85/2025 (sửa 275/2025), NĐ 206/2026, TT 36/2026/TT-BXD | - |
| 2 | QĐ phân bổ chi tiết vốn (QĐ 2161) | QĐ 805/QĐ-UBND, NQ 56/NQ-HĐND | - |
| 3 | Tờ trình + QĐ phê duyệt KHLCNT (QĐ 2236) | Luật Đấu thầu Đ38, 40; NĐ 214 Đ78-80 | Đăng tải KHLCNT trước khi gửi dự thảo hợp đồng |
| 4 | Đăng ký dự án, khai người có thẩm quyền trên muasamcong | Chủ tịch UBND tỉnh phê duyệt dự án | - |
| 5 | Nhà thầu gửi Đơn xin nhận thầu + hồ sơ năng lực | Đ5 Luật Đấu thầu (a,b,c,d,e,g,i); NĐ 212/2026 | - |
| 6 | Gửi dự thảo hợp đồng trên hệ thống; thương thảo giá | Đ80 NĐ 214; CV 2845/QLĐT-ĐT, 5387/STC-ĐTĐT | - |
| 7 | Phiếu trình + QĐ phê duyệt KQLCNT (QĐ 2374, 2375) | Đ33 NĐ 214; TT 79/2025 (PL 5, PL 4C) | Đăng tải KQ trong 05 ngày làm việc |
| 8 | Ký hợp đồng, quản lý hợp đồng, thanh toán | NĐ 210/2026, kế hoạch vốn từng năm | - |
| 9 | Báo cáo giải ngân hằng tháng (Biểu 04a) | QĐ 64/2026/QĐ-UBND | Trước ngày 02 hằng tháng |

## 2. Lỗi đã xảy ra trong phiên và nguyên nhân gốc

| # | Lỗi | Nguyên nhân gốc | Cách chặn |
|---|---|---|---|
| 1 | Nói CTMTQG được miễn giới hạn 3 năm của nhóm C (sai, đúng là Điều 57 khoản 2 điểm d) | Suy từ một điểm của Điều 57 mà không đọc cả khoản | Quy tắc: kết luận pháp lý phải trích **nguyên văn điều khoản** từ kho; agent tra luật trả bảng "đã đọc nguyên văn / chỉ từ web" |
| 2 | Ghi "Một giai đoạn một túi hồ sơ" cho chỉ định thầu rút gọn | Nhầm quy trình chỉ định thầu thông thường (Đ79) với rút gọn (Đ80) | Bảng đối chiếu Đ79 và Đ80 trong rule 23 |
| 3 | Viện dẫn chuỗi sửa đổi NĐ 214 sai (165/349) | Không đọc phần "được sửa đổi bởi" của VBHN 36/2026 | Quy tắc: văn bản có VBHN thì chỉ dẫn VBHN, không tách nghị định sửa đổi |
| 4 | Trả lời "chưa thấy văn bản của tỉnh về tiết kiệm 5%" trong khi kho có CV 5387/STC-ĐTĐT và CV 2845/QLĐT-ĐT | Tìm kho theo từ khóa hẹp ("chỉ định thầu") | Agent tra cứu phải tìm theo 3 lớp từ khóa và ghi các từ đã dùng |
| 5 | QĐ 2236 đã ký vẫn có lỗi (ngày 07/10/1026, "bỗ sung", "chỉ tiết", thiếu dấu ngoặc kép) | Không có bước kiểm nhất quán số liệu, chính tả giữa các văn bản trong một bộ | Script kiểm nhất quán (mục 3, agent 4) |
| 6 | Hợp đồng mẫu còn căn cứ NĐ 37/2015, Luật Đấu thầu 43/2013 | Dùng mẫu cũ trong thư mục nhà thầu gửi | Rà căn cứ hợp đồng bằng `ktc-hieu-luc-vien-dan` trước khi ký |
| 7 | Hồ sơ năng lực là bản scan, không có OCR; phải đọc bằng mắt từng ảnh | Chưa có công cụ OCR | Cài OCR (mục 4) |
| 8 | Khẳng định "đã tra cứu" khi người dùng mới xác nhận một phần | Điền câu theo mẫu | Mỗi văn bản giao kèm "danh sách giả định cần anh xác nhận" |
| 9 | Nghị định/thông tư quan trọng không có trong kho (TT 79/2025, NĐ 212/2026) | Kho chưa được cập nhật theo hồ sơ thực tế | Nạp kho (mục 4) |
| 10 | Phòng TC-KT sửa lại cách viện dẫn VBHN trong bản đã ký | Quy tắc viện dẫn chưa phổ biến ngoài Phòng | Gửi bản "Cách viện dẫn" một trang cho TC-KT |

## 3. Quy trình và sub-agent đề xuất (bổ sung, không trùng 7 agent hiện có)

Hiện có: `ktc-tra-cuu-can-cu`, `ktc-hieu-luc-vien-dan`, `ktc-kiem-san-pham`, `ktc-kiem-ho-so-don-vi`, `ktc-xac-minh-minh-chung`, `ktc-tu-hoc`, `ktc-tu-cai-tien` và nhóm `ktc-ra-soat-897`. Đề xuất thêm 5 agent (bản nháp trong thư mục `agents/`):

| Agent | Việc | Quyền | Mô hình đề xuất |
|---|---|---|---|
| `ktc-dau-tu-cong-dieu-phoi` | Giữ chuỗi 9 bước, đọc `du-an.yaml`, cho biết bước kế tiếp, hạn, hồ sơ còn thiếu | Đọc, ghi vào `30-Ket-Qua/` | Opus |
| `ktc-tra-luat-dau-thau` | Tra luật đấu thầu, đầu tư công, xây dựng: kho trước, web sau; gắn nhãn nguồn từng kết luận | Đọc + web | Opus |
| `ktc-kiem-nang-luc-nha-thau` | Đọc hồ sơ năng lực (OCR), lập bảng chứng chỉ, hạng, hạn, so với yêu cầu gói; liệt kê việc phải tra trên hệ thống | Đọc | Sonnet |
| `ktc-kiem-nhat-quan-bo-van-ban` | Đối chiếu số liệu, ngày, tên dự án, giá, số QĐ giữa các văn bản trong một bộ | Đọc | Sonnet |
| `ktc-theo-doi-han-dau-tu-cong` | Cập nhật `Moc-Han.md` khi có QĐ mới (hạn đăng tải 05 ngày, báo cáo trước ngày 02 hằng tháng, hạn chứng chỉ nhân sự) | Đọc, sửa `Moc-Han.md` | Haiku/Sonnet |

Quy trình thêm vào skill `ktc-dau-tu-cong` (thư mục `skill-ktc-dau-tu-cong/`): một tệp `du-an.yaml` làm **nguồn sự thật duy nhất** (tên dự án, TMĐT, giá gói, số/ngày QĐ, nhà thầu, mã KHLCNT); các script dựng văn bản (Tờ trình, QĐ KHLCNT, Phiếu trình, QĐ KQLCNT, báo cáo giải ngân) đọc từ tệp này thay vì gõ số vào từng script.

## 4. Việc nền cần làm
1. Nạp vào kho 01-05: TT 79/2025/TT-BTC (cả phụ lục) và NĐ 212/2026/NĐ-CP; nạp vào kho 02: QĐ 2158, 2161, 2236, 2374, 2375.
2. Cài OCR cho tiếng Việt (Tesseract + dữ liệu `vie`, hoặc gói OCR trong Python) để đọc bản scan; ghi kết quả OCR kèm cảnh báo "cần đối chiếu bản gốc".
3. Thêm 3 phép kiểm vào `kiem_vien_dan.py`: (a) NĐ 214 phải kèm VBHN 36/2026; (b) không dẫn riêng nghị định đã nằm trong VBHN; (c) VBHN không ghi "của Văn phòng Quốc hội/Bộ Tài chính".
4. Thêm phép kiểm vào `kiem_the_thuc.py` hoặc `kiem_san_pham`: ngày hợp lý (năm 2026 ± 1), tổng giá gói bằng dự toán, tên dự án khớp NQ 46/QĐ 805.
5. Thêm các mốc vào `Moc-Han.md`: đăng tải KQLCNT trước 03/11/2026; báo cáo giải ngân tháng 10 (trước 02/11); ký hợp đồng với 2 nhà thầu; hạn chứng chỉ Huỳnh Tấn Cao (08/8/2027), Nguyễn Quốc Phương (08/7/2027).

## 5. Cách thiết lập trên VS Code Claude Code
1. Chép `agents/*.md` vào `.claude/agents/` của dự án (agent cấp dự án; cùng tên với plugin thì bản dự án thắng).
2. Chép `rules/23-dau-tu-cong-dau-thau.md` vào `.claude/rules/` (nạp khi đụng thư mục `30-Ket-Qua/` đầu tư công hoặc `LCNT`; đổi `paths` nếu cần).
3. Chép `skill-ktc-dau-tu-cong/SKILL.md` vào `.claude/skills/ktc-dau-tu-cong/SKILL.md` (hoặc đóng vào plugin bằng `dong_goi_plugin.py` sau khi duyệt).
4. Hook: thêm vào `.claude/settings.json` một hook `PostToolUse` chạy `kiem_vien_dan.py` và kiểm nhất quán khi ghi `.docx` vào `30-Ket-Qua/**/Soan-Thao-VB/` (đã có hook thể thức trong plugin; không nhân đôi).
5. Chạy `python 29-Cong-Cu/kiem_tra_he_thong.py` sau khi thêm agent và skill (bắt buộc theo `.claude/rules/22`).
6. Thử trên bộ hồ sơ Dự án CLC: cho `ktc-kiem-nhat-quan-bo-van-ban` quét QĐ 2158, 2161, 2236, 2374, 2375; kết quả kỳ vọng bắt được lỗi ngày/giá/chính tả đã biết (đối chứng).

## 6. Không đề xuất (và lý do)
- Không tạo agent tự duyệt hoặc tự đánh giá "đủ điều kiện ký": theo Nguyên tắc 6, quyết định thuộc người có thẩm quyền.
- Không tạo agent tự đăng tải lên muasamcong (cần tài khoản chủ đầu tư, chữ ký số; việc của người phụ trách).
