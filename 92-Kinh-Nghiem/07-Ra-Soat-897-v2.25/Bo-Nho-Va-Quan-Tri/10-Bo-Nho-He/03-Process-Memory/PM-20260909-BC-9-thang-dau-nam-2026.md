# PM-20260909-BC-9-thang-dau-nam-2026

- **Tác vụ**: (a) Rà soát chính thức trước khi trình ký.
- **Hồ sơ**: Báo cáo tình hình thực hiện nhiệm vụ 9 tháng đầu năm 2026; nhiệm vụ chủ yếu 3 tháng cuối năm 2026 (dự thảo v1, chưa số) — Trường Cao đẳng Kon Tum, Kính gửi Sở Tài chính tỉnh Quảng Ngãi.
- **Hệ quy chiếu**: Hành chính nhà nước (NĐ 30/2020/NĐ-CP + TB 597/TB-CĐKT, Mẫu 2.1). Đã kiểm tra chéo cả 3 tiểu-hệ đoàn thể và hệ văn bản Đảng — không thuộc các hệ này.
- **Phiên bản đã dùng**: Skill ktc-ra-soat-897 v2.22; Checklist 08 (bản đính chính 09/9/2026); Skill-Tu-hoc-Phong-Cach-Bao-Cao-ra-soat v1.3; tools `_read_input_properties.py` v1.1 và `build_ktc897_report.py`.

## Các bước đã chạy
1. Bước 0a — xác định hệ quy chiếu; 0b — chạy `read_input_properties()` (0 phát hiện nhóm lề) và đo bổ sung `font.size`/`bold`/`italic` từng run cho 13 thành phần thể thức.
2. Đối chiếu kho 01-04 (Nguyên tắc 1): truy cập được cả 4 kho; đọc **toàn văn** bản gốc QĐ 38/2026/QĐ-UBND trong 01-Legal-Database; đọc **toàn văn** BC 6 tháng đầu năm 2026 trong 04-Good-Documents.
3. Đối chiếu bộ nhớ vận hành: MEMORY-INDEX.md (bản 05/9/2026, sửa cuối 09/9/2026) — **không** chứa quy tắc riêng cho rà soát báo cáo công tác định kỳ.
4. Đối chiếu Checklist 01–08 + Skill-Tu-hoc (6 khối cấu trúc + bộ phát hiện lỗi ngôn ngữ).
5. Xuất báo cáo rà soát .docx đủ 8 phần, A4 ngang, đủ 3 trường trách nhiệm.

## Căn cứ đã kiểm tra
- **Xác minh được trong kho**: QĐ 38/2026/QĐ-UBND (toàn văn), QĐ 1299/QĐ-CĐKT 27/5/2026, TB 736/TB-CĐKT 25/6/2026, QĐ 1355/QĐ-CĐKT 03/6/2026, TB 597/TB-CĐKT 19/5/2026.
- **Xác minh khớp bằng đối chiếu nội dung**: NQ 71-NQ/TW 22/8/2025; NQ 57-NQ/TW 22/12/2024; NQ 68-NQ/TW 04/5/2025; NQ 59-NQ/TW 24/01/2025; NQ 66-NQ/TW 30/4/2025; NQ 72-NQ/TW 09/9/2025.
- **Chưa xác minh được** (không có trong kho 01-04; đã thử WebSearch **2 lần**, bị proxy từ chối **HTTP 403**; phiên chỉ dùng được Google Drive và Microsoft 365): CV 9016/UBND-KTTH 03/9/2026; CT 07-CT/TW 13/7/2026; CT 02-CT/TW 31/01/2026; KL 226-KL/TW; QĐ 182-QĐ/TU; KH 82-KH/TU; NĐ 63/2026, 159/2026, 182/2026, 233/2026, 234/2026, 235/2026, 259/2026/NĐ-CP; TT 03/2026, 05/2026, 38/2026, 55/2026, 59/2026, 64/2026/TT-BGDĐT, TT 18/2025/TT-BGDĐT, TT 17/2026/TT-BXD; KH 321/KH-UBND; QĐ 287/QĐ-UBND 29/4/2026. Điểm cần soát nhất: **TT 31/2016/TT-BGDĐT** gắn nội dung "bổ nhiệm chức danh, xếp lương nhà giáo" — số hiệu 2016 nằm giữa chuỗi văn bản 2025–2026.

## Phát hiện chính — 54 vấn đề (4 Mức 1 · 21 Mức 2 · 23 Mức 3 · 6 Mức 4)

### Mức 1
- **B1** — Viện dẫn sai tên văn bản căn cứ: dự thảo ghi QĐ 38/2026/QĐ-UBND ban hành Quy chế làm việc UBND tỉnh Quảng Ngãi *"nhiệm kỳ 2021-2026"*. Bản gốc trong kho ghi **"nhiệm kỳ 2026 - 2031"** (thống nhất ở tiêu đề, phần mở đầu, Điều 1, Điều 3). Cụm "nhiệm kỳ 2021 - 2026" trong bản gốc chỉ xuất hiện **1 lần tại Điều 2 khoản 2**, chỉ QĐ 16/2025/QĐ-UBND 15/7/2025 **đã bị thay thế**. → dự thảo gắn tên văn bản hết hiệu lực vào số hiệu văn bản đang có hiệu lực. **Lỗi kế thừa**: BC 6 tháng đầu năm 2026 chép cùng chuỗi sai.
- **C1** — Mục "Hạn chế, khó khăn, vướng mắc và nguyên nhân: Không." trống 2 khối bắt buộc (Skill-Tu-hoc 1.4, 1.5) và tự mâu thuẫn với 5 hạn chế do chính báo cáo nêu (Y-Dược 144/190 = 76%; "các ngành còn đạt tỷ lệ thấp"; tranh chấp đất Khu thực nghiệm và CS5; "tháo gỡ khó khăn" của PKĐK; CSVC xuống cấp) và với 3 tồn tại đã nêu tại BC 6 tháng đầu năm 2026 (HSSV vùng sâu vắng học; hồ sơ giáo vụ Khoa ĐT lái xe; CSVC xuống cấp) mà không có nội dung nào chứng minh đã khắc phục.
- **C2** — Thiếu chuẩn so sánh cho **toàn bộ** chỉ tiêu; nghiêm trọng nhất: nêu 1.190 chỉ tiêu nhưng **không nêu tổng số đã tuyển được toàn Trường** và tỷ lệ %, chỉ nêu riêng khoa Y - Dược.
- **D1** — Dùng tên cũ đã bị cấm tại Checklist 08 mục 3.5: "Khoa KT-CN và Các Trung tâm" (2 chỗ) và "Kỹ thuật - Công nghệ và các Trung tâm" (1 chỗ). Tên đúng: **Cơ sở 4: Khoa Kỹ thuật - Công nghệ và Đào tạo - Sát hạch lái xe** (Khoa KT-CN&ĐT-SHLX / CS4).

### Mức 2 (21)
A1 tên đơn vị ban hành 14pt không đậm (phải 13pt đậm) · A2 "BÁO CÁO" không đậm · A3 "HIỆU TRƯỞNG" không đậm · B2 dùng "Căn cứ" cho công văn · B3 viện dẫn gộp "NĐ 233, 234, 235/2026/NĐ-CP" và "TT 18/2025, 05/2026, 64/2026, 59/2026, 03/2026/TT-BGDĐT" không kèm ngày · B4 KH 321/KH-UBND ghi sai chủ thể ("của Chủ tịch UBND tỉnh") · C3 mâu thuẫn số liệu tài trợ 117 triệu vs ~500 triệu · C4 Phần II thiếu tiêu đề cấp "I." (có "II." mà không có "I.") · C5 trùng lặp 6 nhiệm vụ giữa đoạn không tiêu đề và tiểu mục "Công tác tuyển sinh và đào tạo" · C6 nhiệm vụ Q4 chứa việc đã qua mốc (QĐ công nhận kết quả học tập "trong tháng 8/2026"; lắp đặt PTN ISO/IEC 17025 đợt 1 đã nghiệm thu ở Phần I) · C7 mốc kỷ niệm 10 năm đặt ở 2 năm khác nhau (24/10/2027 vs Q4/2026) · C8 Nơi nhận thiếu 3/4 cơ quan được kiến nghị · C9 tiêu đề mục II.2 trùng nguyên văn mục 7 Phần II, nội dung "Không có." · D2 "Khoa Y Dược" thiếu gạch nối · D3 "Nông lâm" phải là "Nông Lâm" · E1 "bộ nhiệm" · E2 "uỷ quyền" · E3 "xe ô con" · E4 MIMONMI vs MOMIMO trong cùng đoạn · E5 K7C vs K7T · F1 nêu họ tên cá nhân kèm kết luận "hành vi ngang nhiên xâm chiếm trái phép".

### Mức 3 (23) · Mức 4 (6)
A4 trích yếu có dấu chấm cuối · A5 Nơi nhận gộp dòng và đảo thứ tự so mẫu TB 597 · C10–C17 (tiêu đề mục 7 lệch; trùng lặp trong 1 đoạn; trùng lặp giữa đoạn liền kề; lặp ý trong 1 câu; kể việc thiếu kết quả; danh sách phẳng; tính từ không minh chứng; "hơn 606") · D4 "Nhà trường" hoa 10 lần / thường 7 lần · D5 hoa-thường "khoa"/"Trung tâm" · E6–E16 (Y sĩ/Y sỹ; Ba-Na/Bahnar; Kiểm toán Nhà nước/nhà nước; "hoá chất"; "Miền Nam"; ngoặc kép thiếu và nháy đơn/kép; 2 dấu cách; chấm phẩy sai; 8 chữ viết tắt không mở ngoặc; gạch ngang "2026 – 2030"; "Trường Cao đẳng Cộng đồng Kon Tum") · Mức 4: B5 danh mục căn cứ chưa xác minh · F2 tên ngày 07/4 · F3 tên sản phẩm thương mại · F4 khung tiêu đề mượn từ BC KT-XH cấp tỉnh · F5 chưa chốt mốc số liệu · G1 metadata tệp (author "Bùi Như Quỳnh", modified_by "phuc Nguyen").

## Quyết định phân loại đáng lưu ý
- Lỗi **cỡ chữ / in đậm** sai bảng số cứng TB 597 mục 4 → **Mức 2** (sai thể thức, kỹ thuật trình bày), KHÔNG hạ xuống Mức 3.
- Lỗi **hành văn, hoa–thường, tên gọi** theo quy ước riêng TB 597 → **Mức 3** (Skill-Tu-hoc mục 3 nguyên tắc 6).
- **D1 giữ Mức 1** đúng bảng Checklist 08 mục 3.5, dù chỉ là tên gọi, vì công bố ra cơ quan ngoài một tên tổ chức không còn tồn tại.
- **KHÔNG** bắt lỗi thiếu căn cứ QĐ 988/QĐ-CĐKT (Checklist 08 mục 1 không áp dụng cho báo cáo).
- **KHÔNG** bắt lỗi "- Công đoàn Trường;" / "- Đoàn TN – Hội SV Trường;" trong Nơi nhận (Checklist 08 mục 3.4, bổ sung 08/9/2026) — chỉ nêu việc gộp dòng và đảo thứ tự ở Mức 3.
- Áp dụng Nguyên tắc 4: tính toán lại độc lập 6 mốc kỷ niệm và 5 phép cộng số liệu → đều đúng, đưa vào Phần III (Đạt), không kết luận "Đạt" từ lời văn.

## Nội dung người dùng chỉnh / bác bỏ
Chưa có — bản này vừa xuất, chờ Phòng TH-HC&QT xác nhận.

## Kết quả cuối
- **Kết luận: CHƯA ĐỦ ĐIỀU KIỆN TRÌNH KÝ.** Phải xử lý xong 4 Mức 1 và 21 Mức 2 trước khi phát hành.
- Phần VII nêu **14 bước xử lý** theo thứ tự, đặt trước 2 việc cần dữ liệu từ đơn vị khác (C2 — Phòng QLĐT&BĐCL; C3 — Phòng QLKHCN&HTPT).

## Vấn đề còn mở
1. Trường "Người kiểm tra" trong báo cáo xuất ra còn **placeholder** — cần điền họ tên và chức danh người chịu trách nhiệm.
2. Chưa đối chiếu được **CV 9016/UBND-KTTH ngày 03/9/2026** — văn bản đặt ra khung yêu cầu báo cáo. Nên nạp vào kho 01-Legal-Database.
3. Lỗi kế thừa "nhiệm kỳ 2021-2026" cần sửa tại **biểu mẫu báo cáo dùng chung** và kho 03-Templates, không chỉ ở tệp này (đã qua ít nhất 2 kỳ báo cáo).
4. Chưa tải được báo cáo rà soát lên `12-Output/` — theo giới hạn tải tệp nhị phân lớn (SKILL.md quy tắc 20), cần người dùng tự tải lên.
5. Bộ nhớ vận hành **thiếu** quy tắc riêng cho rà soát báo cáo công tác định kỳ — 2 pattern lỗi mới đề xuất ghi vào Skill-Tu-hoc (xem dưới), chờ xác nhận Phó Trưởng phòng TH-HC&QT.

## Hành động tiếp theo — đề xuất ghi Skill-Tu-hoc (Tình huống D, chờ xác nhận)
- **Pattern lỗi mới 1** — "khai không có hạn chế trong khi chính báo cáo và báo cáo kỳ trước đã nêu hạn chế". Kỹ thuật phát hiện: đối chiếu **ngược** từ mục kiến nghị và từ mục tồn tại của **kỳ liền trước**, không chỉ đọc mục đánh giá chung. Phân loại: **Mức 1**.
- **Pattern lỗi mới 2** — "chồng bản soạn thảo". Dấu hiệu: (i) đoạn không tiêu đề đặt trước tiểu mục có tiêu đề cùng chủ đề; (ii) cùng một sự kiện nêu 3 lần trong 1 đoạn; (iii) nhiệm vụ đã báo hoàn thành ở phần trước xuất hiện lại ở phần nhiệm vụ. Phân loại: **Mức 2** (trùng lặp làm sai kỳ báo cáo) hoặc Mức 3 (trùng lặp thuần hành văn).
- **Pattern tốt (mục 2.7)** — "gắn mỗi nghị quyết Trung ương với một nội dung triển khai cụ thể của đơn vị trong ngoặc đơn": vừa chứng minh đã quán triệt, vừa chứng minh đã cụ thể hóa. Nguồn: BC 9 tháng 2026 đoạn #46. Ngày 09/9/2026.

## ID đầu ra
- `Bao-cao-ra-soat-KTC897_BC-9-thang-2026_20260909.docx` (77 KB; A4 ngang; 8 phần; 14 bảng, bảng rộng nhất 25,5cm ≤ 25,7cm) — đã giao cho người dùng trong phiên, **chưa** tải lên Drive (xem vấn đề còn mở #4).
