# PM-20260905-QD988-QuyChe-TCHD

```yaml
memory_id: PM-20260905-QD988-QuyChe-TCHD
created_at: 2026-09-05T09:20:00+07:00
memory_type: process
status: closed
task_type: formal_review
document_type: Quyết định (ban hành Quy chế tổ chức và hoạt động, thay thế QĐ 988/QĐ-CĐKT)
document_title: Quyết định ban hành Quy chế tổ chức và hoạt động của Trường Cao đẳng Kon Tum
draft_version: dự thảo đang Track Changes (tác giả Hồ Thị Phương Sáu), chưa có số/ngày
responsible_unit: Phòng Tổ chức cán bộ và Công tác học sinh - sinh viên
scope: Trường Cao đẳng Kon Tum
project_name: KTC-Ra-Soat-897-v2-Cai-tien

input_files:
  - name: sua_doi_QD_988_QUY_CHE_TO_CHUC_VA_HOAT_DONG_TRUONG.docx
    drive_id_or_link: "(người dùng tải lên trực tiếp qua chat, không qua Drive)"
    version_or_date: dự thảo Track Changes, 517 đoạn văn, 556 w:ins/516 w:del
    role: văn bản cần rà soát chính thức trước khi trình ký

control_versions:
  skill_package: ktc-ra-soat-897 v2.21
  checklist_08: v2.9 (31/8/2026)
  other_checklists: 01-The-Thuc, 05-Hinh-Thuc, 07-Theo-Loai-Van-Ban
  script: build_ktc897_report.py v3.4

sources_verified:
  - source: "QĐ 988/QĐ-CĐKT gốc (ID 1c-_hZIo3ytXqqMN3BYytJRGJ-kl-JGYq)"
    status: verified
    checked_at: 2026-09-05
  - source: "QĐ 543/QĐ-UBND, QĐ 339/QĐ-UBND (nội dung tham chiếu qua QĐ 988 gốc)"
    status: verified
    checked_at: 2026-09-05
  - source: "TT 63/2026/TT-BGDĐT (ID 1l-Y6AxzNUkFu4nt9hVkvcggtdR_unaqk) - hiệu lực từ 14/9/2026"
    status: verified
    checked_at: 2026-09-05
  - source: "TT 43/2026/TT-BGDĐT (ID 17wm59GcotlOINspwaJ-r0Sfa2XR-lW3_)"
    status: verified
    checked_at: 2026-09-05
  - source: "Luật Nhà giáo 73/2025/QH15 (ID 10zcBECSPrALaiqpzIE1P6jMt9HXrWog0), ngày 16/6/2025"
    status: verified
    checked_at: 2026-09-05
  - source: "TB 950/TB-CĐKT (ID 1Pdq0wxMR2Gxa1_LT2H2sEN08fICOaMNF), ngày 17/8/2026"
    status: verified
    checked_at: 2026-09-05
  - source: "Công cụ tra cứu web"
    status: unverified
    checked_at: 2026-09-05
    note: "Không có công cụ tra cứu web trong phiên này"

process_steps:
  - step: 1
    action: Đọc MEMORY-INDEX.md, Checklist 08 (đã nạp từ tác vụ trước cùng phiên)
    result: Không xung đột
  - step: 2
    action: Trích xuất toàn bộ Track Changes bằng lxml (556 w:ins, 516 w:del), dựng before/after cho từng đoạn văn (517 đoạn)
    result: 343 đoạn có khác biệt nội dung thật
    evidence: script parse trực tiếp word/document.xml
  - step: 3
    action: Kiểm tra tính duy nhất số Điều (1-42) trên toàn văn bản SAU (accepted)
    result: Phát hiện Điều 36 trùng số 2 lần với nội dung khác nhau
    evidence: regex "^Điều\s+(\d+)\." đối chiếu tuần tự
  - step: 4
    action: Kiểm tra tính duy nhất danh sách Căn cứ ở phần mở đầu
    result: Phát hiện QĐ 339/QĐ-UBND và QĐ 287/QĐ-UBND đều bị trích dẫn 2 lần, before=after tại cả 2 vị trí (xác nhận không phải track changes ảo)
    evidence: so sánh nội dung 14 đoạn "Căn cứ" theo thứ tự
  - step: 5
    action: Quét ký tự Unicode bất thường (combining marks đứng sau dấu câu)
    result: Phát hiện lỗi "Quản tri;̣" (dấu nặng tách rời) tại Điều 15
    evidence: quét toàn văn bản SAU cho combining marks U+0300-036F đứng sau ký tự không phải chữ cái
  - step: 6
    action: Đối chiếu KTC-Database cho các căn cứ mới/thay đổi (TT 63/2026, TT 43/2026, Luật Nhà giáo, TB 950, QĐ 543 qua QĐ 988 gốc)
    result: Tất cả khớp đúng số hiệu/ngày/trích yếu; phát hiện TT 63/2026 chỉ hiệu lực từ 14/9/2026 - cảnh báo mốc ký
    evidence: Google Drive search_files, đối chiếu nội dung
  - step: 7
    action: Chạy _read_input_properties.py kiểm tra định lượng lề/khổ giấy
    result: Đạt, không phát hiện sai lệch
  - step: 8
    action: Dựng báo cáo 8 phần, validate.py, render PDF kiểm tra trực quan
    result: Validate PASSED, 8 trang
    evidence: "/mnt/user-data/outputs/Bao_cao_ra_soat_QD988_QuyCheTCHD_20260905.docx"

key_findings:
  - id: F1
    location: "Phần Căn cứ, vị trí 4 và 6"
    issue: "QĐ 339/QĐ-UBND bị trích dẫn 2 lần"
    level: Mức 1
    status: open
  - id: F2
    location: "Phần Căn cứ, vị trí 5 và 11"
    issue: "QĐ 287/QĐ-UBND bị trích dẫn 2 lần"
    level: Mức 1
    status: open
  - id: F3
    location: "Chương VI"
    issue: "Điều 36 trùng số, trùng chủ đề, nội dung cũ chưa xóa"
    level: Mức 1
    status: open
  - id: F4
    location: "Căn cứ Thông tư 63/2026/TT-BGDĐT"
    issue: "Chỉ hiệu lực từ 14/9/2026 - cần xác nhận ngày ký thực tế"
    level: Mức 1
    status: open
  - id: F5
    location: "Điều 15 khoản 3"
    issue: "Lỗi Unicode 'Quản tri;̣'"
    level: Mức 2
    status: open
  - id: F6
    location: "Điều 15 khoản 4"
    issue: "'Khoa Kinh tế và Nông Lâm' viết hoa sai, đúng phải 'Nông lâm'"
    level: Mức 2
    status: open

decisions:
  - decision: "QĐ 988 không cần xuất hiện trong Căn cứ của văn bản này"
    reason: "Văn bản này thay thế QĐ 988, không phải văn bản vận hành dưới thẩm quyền QĐ 988 thiết lập"
    evidence: "Checklist 08 mục 1 (điều kiện áp dụng); QĐ 988 gốc cũng không tự trích QĐ 49 mà nó thay thế"
    made_by: AI

outputs:
  - name: Bao_cao_ra_soat_QD988_QuyCheTCHD_20260905.docx
    drive_id_or_link: "/mnt/user-data/outputs/ (chưa tải lên Drive)"
    version: "1"
    status: "BẢN NHÁP - chờ Phó Trưởng phòng TH-HC&QT phê duyệt"

unresolved_items:
  - item: "Chưa xác minh hiệu lực pháp luật các căn cứ qua nguồn web bên ngoài"
    reason: "Không có công cụ tra cứu web trong phiên này"
  - item: "Chưa rà soát toàn bộ 343 đoạn có thay đổi ở mức chi tiết câu chữ (chỉ rà trọng điểm: căn cứ, số Điều, cơ cấu tổ chức, định dạng)"
    reason: "Khối lượng lớn (846KB XML); ưu tiên rủi ro pháp lý/cấu trúc cao nhất trước"
    needed_evidence: "Rà soát bổ sung nếu người dùng yêu cầu kiểm tra sâu từng Chương IV-V (nhà giáo, tài chính)"

lessons:
  - issue: "Track Changes khối lượng lớn dễ sinh lỗi trùng lặp khi 'di chuyển' nội dung (chèn bản sao ở vị trí mới, quên xóa bản gốc)"
    correction: "Khi rà soát văn bản Track Changes lớn, luôn quét thêm: (a) trùng số Điều/Chương, (b) trùng nội dung câu dài giống hệt (>40 ký tự) xuất hiện nhiều vị trí, (c) ký tự Unicode bất thường quanh vị trí có chỉnh sửa"
    scope: "Áp dụng cho mọi hồ sơ rà soát có Track Changes lớn trong hệ ktc-ra-soat-897"
    approval_status: proposed

next_action: "Chờ đơn vị soạn thảo xử lý 4 vấn đề Mức 1 và 2 vấn đề Mức 2; nhắc lại không ký trước 14/9/2026."
```
