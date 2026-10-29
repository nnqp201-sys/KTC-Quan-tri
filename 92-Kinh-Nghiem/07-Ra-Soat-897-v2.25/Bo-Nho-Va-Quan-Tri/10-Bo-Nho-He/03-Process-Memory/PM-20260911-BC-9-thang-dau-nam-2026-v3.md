# PM-20260911-BC-9-thang-dau-nam-2026-v3

- **Tác vụ**: (a) Rà soát chính thức trước khi trình ký.
- **Hồ sơ**: Báo cáo kết quả công tác 9 tháng đầu năm; kế hoạch công tác 3 tháng cuối năm 2026 — Trường Cao đẳng Kon Tum, kính gửi Sở Tài chính. Bản v3 (chưa cấp số). Kế thừa trực tiếp từ PM-20260909-BC-9-thang-dau-nam-2026.md (rà soát bản v1, 54 vấn đề).
- **Hệ quy chiếu**: Hệ A — Hành chính nhà nước (NĐ 30/2020/NĐ-CP + TB 597/TB-CĐKT, Mẫu 2.1).
- **Phiên bản đã dùng**: Skill ktc-ra-soat-897 v2.22; Checklist 08; tools `_read_input_properties.py`, `build_ktc897_report.py`.

## Các bước đã chạy
1. Bước 0a/0b — xác định hệ A; đo lề (trái 3,0cm, phải/trên/dưới 2,0cm — đạt), khổ A4 đứng; đo font/bold/italic từng thành phần thể thức bằng python-docx (bao gồm kiểm tra style Heading 2 mặc định Word và XML run của "HIỆU TRƯỞNG").
2. Đối chiếu kho 01-04: đọc toàn văn QĐ 38/2026/QĐ-UBND (khớp — "nhiệm kỳ 2026-2031"); tìm CV 9016/UBND-KTTH — KHÔNG có trong kho.
3. Đọc lại toàn bộ Process Memory kỳ trước (PM-20260909) và đối chiếu từng phát hiện cũ (54 vấn đề) với nội dung bản v3.
4. Phát hiện CONFLICT: nhiều bản MEMORY-INDEX.md trên Drive (bản đúng v2.22 tại 09-Quan-Tri-He/10-Bo-Nho-He/; các bản "v3.0 AUTHORITATIVE RUNTIME ARTIFACT" khả nghi tại thư mục lạ "stage-a-memory-index" và nơi khác — không công nhận).
5. Xuất báo cáo .docx 8 phần, A4 ngang.

## Đối chiếu với PM-20260909 (bản v1 → v3) — đã khắc phục
B1 (nhiệm kỳ QĐ38 sai) — ĐÃ SỬA. D1 (tên cũ Khoa KT-CN) — ĐÃ SỬA. F1 (nêu tên cá nhân + buộc tội tranh chấp đất) — ĐÃ SỬA. A1 (tên đơn vị ban hành 14pt không đậm) — ĐÃ SỬA (nay 13pt đậm). D2 (Khoa Y Dược thiếu gạch nối), D3 (Nông lâm), E1 (bộ nhiệm), E2 (uỷ quyền), E3 (xe ô con), E4 (MIMONMI), E6 (Y sỹ) — ĐÃ SỬA. C3 (mâu thuẫn 117tr/500tr) — ĐÃ SỬA (nay diễn đạt tách bạch). C4 (thiếu "I."), C7 (mốc 10 năm 2 năm khác nhau) — ĐÃ SỬA. A4 (trích yếu có dấu chấm cuối) — ĐÃ SỬA.

## Chưa khắc phục / phát sinh mới ở bản v3
- **C1 (Mức 1, chưa sửa)**: mục "Hạn chế, khó khăn, vướng mắc và nguyên nhân: Không." vẫn còn nguyên, vẫn tự mâu thuẫn với nội dung báo cáo.
- **C2 cũ (Mức 1: thiếu tổng số tuyển toàn Trường) → đã bổ sung số liệu nhưng SAI SỐ HỌC MỚI**: "886 chỉ tiêu (366 cao đẳng, 194 trung cấp)" — 366+194=560≠886. Hạ xuống Mức 2 (đã có số liệu, chỉ còn lỗi số học) nhưng là lỗi mới cần Phòng QLĐT&BĐCL xác minh.
- **A2/A3 (Mức 2)**: "BÁO CÁO"/trích yếu nay dùng style Heading 2 mặc định Word — đã đậm nhưng phông là Cambria (mới phát hiện, PM cũ chưa ghi); "HIỆU TRƯỞNG" đã đúng phông Times New Roman + 14pt nhưng XML xác nhận vẫn thiếu `<w:b/>` — chưa đậm.
- **B2 (Mức 3, chưa sửa)**: vẫn dùng "Căn cứ Công văn số 9016/UBND-KTTH...".
- **Mới phát hiện (chưa có trong PM cũ)**: mã lớp "K7C" tại đoạn khảo thí không khớp "K7T" dùng ở nơi khác; viết hoa không nhất quán "Trung tâm (Đ/đ)ăng kiểm xe cơ giới" (3 lần); đoạn viện dẫn "(thay thế Quyết định số 988/QĐ-CĐKT)" thiếu số/ngày văn bản thay thế — CẦN XÁC MINH có ảnh hưởng đến Checklist 08 mục 1 hay không; Nơi nhận dùng "Đoàn TN Trường"/"Hội SV Trường" (dạng lai, không khớp mẫu TB 597 "Đoàn Trường"/"Hội Sinh viên Trường"); dấu hai chấm lặp "kiểm tra: :"; khoảng trắng thừa trước dấu chấm.

## Phát hiện chính (bản v3) — 12 vấn đề: 1 Mức 1, 6 Mức 2, 3 Mức 3, 2 Mức 4
Xem đầy đủ trong file .docx đã xuất: `Bao-cao-ra-soat-KTC897_BC-9-thang-dau-nam-2026_v3_20260911.docx`.

## Quyết định phân loại đáng lưu ý
- Giữ nguyên phân loại Mức 1 cho mục "Hạn chế... Không." theo đúng phân loại của PM-20260909.
- Hạ C2 cũ từ Mức 1 xuống Mức 2 vì đã có số liệu tổng, chỉ còn sai số học — không phải thiếu hoàn toàn như bản v1.
- KHÔNG lặp lại các phát hiện Mức 3 thuần văn phong đã liệt kê đầy đủ ở PM-20260909 nếu đã xác nhận sửa ở v3 (D2-D5, E-series) — chỉ ghi các trường hợp còn tồn hoặc phát sinh mới để tránh trùng lặp báo cáo.

## CONFLICT bộ nhớ vận hành phát hiện được
Nhiều tệp MEMORY-INDEX.md trên Drive: bản đúng vị trí `09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md` (v2.22) khớp Skill đang cài; các bản khác tự xưng "v3.0 AUTHORITATIVE RUNTIME ARTIFACT" nằm trong thư mục lạ ("stage-a-memory-index" và nơi khác), tham chiếu cấu trúc tệp không tồn tại trong gói Skill thật (rules/, CORE-INDEX.md, SOURCE-OF-TRUTH.md). KHÔNG công nhận các bản này. Đề nghị người dùng xác nhận và dọn dẹp nếu là rác/thử nghiệm cũ.

## Nội dung người dùng chỉnh / bác bỏ
Chưa có — bản này vừa xuất, chờ Phòng TH-HC&QT xác nhận.

## Kết quả cuối
Kết luận: **CHƯA ĐỦ ĐIỀU KIỆN TRÌNH KÝ.** Phải xử lý xong 1 Mức 1 và 6 Mức 2 trước khi phát hành.

## Vấn đề còn mở
1. Trường "Người kiểm tra" trong báo cáo xuất ra còn placeholder — cần điền họ tên, chức danh người chịu trách nhiệm.
2. Chưa đối chiếu được CV 9016/UBND-KTTH ngày 03/9/2026 — đề nghị nạp vào 01-Legal-Database.
3. Cần xác nhận QĐ 988/QĐ-CĐKT còn hiệu lực hay đã có văn bản thay thế (ảnh hưởng Checklist 08 mục 1).
4. Cần người dùng xác nhận/dọn dẹp các bản MEMORY-INDEX.md "v3.0" khả nghi trên Drive (mục CONFLICT ở trên).

## ID đầu ra
`Bao-cao-ra-soat-KTC897_BC-9-thang-dau-nam-2026_v3_20260911.docx` — đã giao cho người dùng trong phiên; đã ghi Process Memory này vào 03-Process-Memory/.
