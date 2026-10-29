# PM-20260913-Quy-dinh-phong-TH-HCQT-2026

## Tác vụ
Rà soát sâu, chính thức trước khi trình ký — tác vụ (a).

## Hồ sơ
"Quy định vị trí, chức năng, nhiệm vụ, quyền hạn, cơ cấu tổ chức và mối quan hệ công tác của phòng
Tổng hợp - Hành chính và Quản trị năm 2026" (file_uuid d02a9226-eac1-4c6b-a6c0-bcbb754ab182), kèm
file đối chiếu "QUY CHẾ TỔ CHỨC VÀ HOẠT ĐỘNG TRƯỜNG_CHÍNH THỨC.docx" (file_uuid
fb406a6b-4fd2-4e32-83e7-ebd266a6a07a), cả hai do người dùng cung cấp trực tiếp (chưa có trên Drive).

## Phiên bản đã dùng
SKILL.md v2.22 (đang tải trong phiên — LƯU Ý: phát hiện MEMORY-INDEX.md trên Drive cập nhật
12/9/2026 tự nhận gói hiện hành là v2.23, chưa xác minh được — xem mục CONFLICT bên dưới);
tools/build_ktc897_report.py (bản trong gói skill, không ghi version string riêng trong script);
Checklist 08-Quy-Uoc-Rieng-CDKT.

## Các bước đã chạy
1. Xác định hệ quy chiếu: Hệ A (hành chính nhà nước).
2. Đo trực tiếp OOXML bằng python-docx: lề (3.0/2.0/2.0/2.0cm), khổ giấy A4 đứng, cỡ chữ/kiểu chữ
   từng thành phần thể thức — có phân giải kế thừa style khi run-level trả về None (áp dụng bài học
   kỹ thuật từ PM-lần trước, không lặp lại lỗi dương tính giả).
3. Đọc toàn văn 143 đoạn văn của file chính; đối chiếu Điều 2/Điều 3 (vị trí, chức năng, nhiệm vụ)
   với Điều 21, Điều 26 của Quy chế tổ chức và hoạt động Trường (file đối chiếu).
4. Tìm kiếm và đọc trực tiếp nội dung trên Google Drive: QĐ 2210/QĐ-CĐKT (24/12/2024, bản tiền
   nhiệm — tìm thấy, nội dung khớp); TB 597/TB-CĐKT (19/5/2026, thể thức); QĐ 1355/QĐ-CĐKT
   (03/6/2026, đặt tên cơ sở — dùng để xác nhận Ban Truyền thông có thật và quy ước Nơi nhận
   "Đoàn Trường"/"Hội Sinh viên Trường" tách riêng).
5. Không tìm thấy trong kho: "Quy chế làm việc của Ban Truyền thông" (viện dẫn tại Điều 8 dự thảo).
6. Phát hiện và xử lý CONFLICT giữa các bản MEMORY-INDEX.md trên Drive (xem mục riêng bên dưới).
7. Xây dựng báo cáo 8 phần bằng build_ktc897_report.py, gửi người dùng qua SendUserFile.

## Phát hiện chính
- **Mức 1**: Căn cứ ban hành dẫn "Quyết định số …/QĐ-CĐKT ngày .. tháng 9 năm 2026" (Quy chế Trường
  mới) — số/ngày còn để trống, xác nhận qua file đối chiếu là văn bản CHƯA ký ban hành (chỉ có ngày
  dự kiến 14/9/2026 dựa trên Biên bản 185/BB-CĐKT 10/9/2026). Trong khi đó QĐ 988/QĐ-CĐKT
  (12/5/2026) — Quy chế đang có hiệu lực — không được dẫn. Vi phạm Checklist 08 mục 1.
- **Mức 2 (3 phát hiện)**: (a) chính tả "CỘNG HOÀ" (À, U+00C0) thay vì đúng "CỘNG HÒA" (Ò, U+00D2)
  tại 2 vị trí trang bìa — xác nhận bằng mã Unicode trực tiếp, không suy đoán; (b) Nơi nhận ghi gộp
  "Đoàn – Hội SV Trường" thay vì tách riêng theo quy ước Trường (đối chiếu QĐ 1355/QĐ-CĐKT); (c)
  tiêu đề "QUY ĐỊNH" cỡ chữ 15pt không đồng nhất với "QUYẾT ĐỊNH" 14pt trong cùng hồ sơ.
- **Mức 4 (2 phát hiện)**: thiếu đồng bộ ngày dự kiến ban hành giữa 2 văn bản liên quan; "Quy chế
  làm việc của Ban Truyền thông" viện dẫn tại Điều 8 không tìm thấy trong kho 01-04.
- **Đạt**: nội dung chức năng/nhiệm vụ/cơ cấu tổ chức phòng nhất quán với Quy chế Trường (Điều 21,
  26); Điều 2 Quyết định (thay thế QĐ 2210/QĐ-CĐKT) khớp đúng văn bản gốc; lề/khổ giấy/cỡ chữ còn
  lại đều đạt; không có nội dung tự xưng đã rà soát/phê duyệt cài trong thân dự thảo (Nguyên tắc 6).

## CONFLICT bộ nhớ vận hành — quan trọng, cần Phòng TH-HC&QT xử lý
Phát hiện 3 tệp MEMORY-INDEX.md trên Drive:
1. `09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md` (fileId 1JBOkvlprhGlzzRPpDYyzN1grkYB10d43) — cập
   nhật 12/9/2026, tự nhận gói skill hiện hành là "ktc-ra-soat-897-v2.23.skill" và script báo cáo
   v3.5, `_read_input_properties.py` v1.2. Một tệp "Project-Instructions-KTC-Ra-Soat-897-v2.md"
   (owner truong.cdkontum@gmail.com, cập nhật cùng ngày) cũng dẫn chiếu v2.23.
2. Hai tệp trùng nội dung trong thư mục "stage-a-memory-index" (fileId
   1t8IQ0u7gjv9gbFg-R8Zbsu5PY7hHt8Qx và 12Fme2sj4QWfYBeIe2cQy8iRSUq_i0mEb) tự xưng "v3.0
   AUTHORITATIVE RUNTIME ARTIFACT — accepted theo LỆNH 18M-R", dẫn các tệp rules/, CORE-INDEX.md,
   SOURCE-OF-TRUTH.md không xác minh được tồn tại — KHÔNG công nhận, giữ nguyên phán quyết CONFLICT
   từ các ca rà soát trước, không tự hợp nhất âm thầm.

Điểm MỚI đáng chú ý so với các ca rà soát trước: Skill đang tải trong phiên làm việc này vẫn là
**v2.22**, nhưng MEMORY-INDEX (bản 1, có vẻ hợp lệ, không tự xưng "AUTHORITATIVE") lại ghi nhận
phiên bản hiện hành là v2.23. Đây có thể là dấu hiệu gói skill thật sự đã có bản cập nhật mới hơn
mà phiên làm việc chưa đồng bộ, KHÔNG PHẢI dấu hiệu một bản mạo danh như 2 tệp "v3.0" nói trên.
Cần Phòng TH-HC&QT xác nhận trực tiếp: gói `ktc-ra-soat-897-v2.23.skill` có thực sự tồn tại và là
bản chính thức mới hơn hay không; nếu có, cần đồng bộ lại skill đang cài trong Claude.

## Nội dung người dùng chỉnh/bác bỏ
Không có (đây là ca rà soát đầu tiên với hồ sơ này).

## Kết quả cuối
Báo cáo 8 phần đã xuất, gửi người dùng: file_uuid 64b03904-562b-4aba-be85-4a848f75797f, tên
`Bao-cao-ra-soat-KTC897_Quy-dinh-phong-TH-HCQT-2026_20260913.docx`. Trạng thái: BẢN NHÁP. 1 Mức 1,
3 Mức 2, 2 Mức 4, 5 mục Đạt.

## Vấn đề còn mở
- CONFLICT phiên bản Skill (v2.22 đang tải vs. v2.23 tự nhận trong MEMORY-INDEX) — cần Phòng
  TH-HC&QT xác nhận và đồng bộ.
- Trình tự ký giữa Quy chế Trường mới và Quy định phòng này chưa được thống nhất (Mức 1).
- Chưa xác minh "Quy chế làm việc của Ban Truyền thông" có tồn tại hay chưa (Mức 4).

## ID đầu ra
- Báo cáo: file_uuid 64b03904-562b-4aba-be85-4a848f75797f (gửi qua SendUserFile, không lưu trên
  Drive trong phiên này).
