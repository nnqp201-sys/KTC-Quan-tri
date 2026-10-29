# PM-20260905-KH-Trien-Khai-TT64

```yaml
memory_id: PM-20260905-KH-Trien-Khai-TT64
created_at: 2026-09-05T08:45:00+07:00
memory_type: process
status: closed
task_type: formal_review
document_type: Kế hoạch (phân công nhiệm vụ)
document_title: Kế hoạch triển khai thực hiện Thông tư số 64/2026/TT-BGDĐT (dự thảo)
draft_version: dự thảo (chưa có số, chưa có ngày)
responsible_unit: Phòng Tổ chức cán bộ và Công tác học sinh - sinh viên
scope: Trường Cao đẳng Kon Tum
project_name: KTC-Ra-Soat-897-v2-Cai-tien

input_files:
  - name: Kh_trien_khai_Thong_tu_64.docx
    drive_id_or_link: "(người dùng tải lên trực tiếp qua chat, không qua Drive)"
    version_or_date: dự thảo, không ngày
    role: văn bản cần rà soát
  - name: 64_2026_TT-BGDDT_m_719305.docx
    drive_id_or_link: "(người dùng tải lên trực tiếp qua chat)"
    version_or_date: 10/8/2026
    role: văn bản gốc làm căn cứ đối chiếu

control_versions:
  skill_package: ktc-ra-soat-897 v2.21
  skill_md: v2.21
  checklist_08: v2.9 (31/8/2026)
  other_checklists: 01-The-Thuc, 05-Hinh-Thuc, 07-Theo-Loai-Van-Ban
  prompt: Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx
  script: build_ktc897_report.py v3.4
  template: KTC-Ra-Soat-897_Template_Trong.dotx

sources_verified:
  - source: "TT 64/2026/TT-BGDĐT (KTC-Database/01-Legal-Database, ID 15JnwJfjxfFo8K0a0KhatIdGDRfjMc6lO)"
    status: verified
    checked_at: 2026-09-05
    note: "Trích yếu thật khớp file gốc người dùng cung cấp"
  - source: "QĐ 988/QĐ-CĐKT (ID 1c-_hZIo3ytXqqMN3BYytJRGJ-kl-JGYq)"
    status: verified
    checked_at: 2026-09-05
  - source: "QĐ 543/QĐ-UBND (ID 1NmQZ6tb5duSrNaKsLygZ0TRXhwh5Y_S4)"
    status: verified
    checked_at: 2026-09-05
    note: "Trích yếu dự thảo dùng không đúng nguyên văn (Mức 2)"
  - source: "Công cụ tra cứu web (vbpl.vn...)"
    status: unverified
    checked_at: 2026-09-05
    note: "Không có công cụ tra cứu web trong phiên này - đã kiểm tra danh sách công cụ, không có browser/web_search"

process_steps:
  - step: 1
    action: Đọc MEMORY-INDEX.md, Nhật ký, SKILL.md, Checklist 08 trước khi rà soát
    result: Không phát hiện xung đột
    evidence: MEMORY-INDEX.md (16agpCDsDEchXw15D9mDvHoCnmmXmZFgZ)
  - step: 2
    action: Xác định Bước 0 - hệ quy chiếu và loại kế hoạch
    result: Hệ A (hành chính nhà nước); Kế hoạch phân công (không áp cấu trúc Căn cứ-Mục tiêu-Nhiệm vụ-Giải pháp-Tổ chức thực hiện)
    evidence: Checklist 07 mục Checklist Kế hoạch; quy tắc vận hành đã xác nhận (memory)
  - step: 3
    action: Chạy _read_input_properties.py trên file đầu vào
    result: 0 findings - lề/khổ giấy đạt
    evidence: top=20mm bottom=20mm left=30mm right=20mm, landscape (hợp lệ do bảng rộng)
  - step: 4
    action: Đối chiếu KTC-Database/01-Legal-Database qua Google Drive connector cho 3 căn cứ chính (TT64, QĐ988, QĐ543)
    result: Phát hiện TT64 bị mô tả sai trích yếu (Mức 1); QĐ543 mô tả không đúng nguyên văn (Mức 2); QĐ988 và QĐ1299 viện dẫn đúng
    evidence: search_files + contentSnippet đối chiếu trực tiếp
  - step: 5
    action: Đối chiếu trực tiếp nội dung bảng phân công và văn bản bằng python-docx
    result: Phát hiện nhảy số TT (thiếu số 5), lặp cụm từ ở câu kết, "Lưu:" dùng sai cột viết tắt
    evidence: python-docx paragraph/table dump
  - step: 6
    action: Dựng báo cáo 8 phần bằng build_ktc897_report.py v3.4, validate.py, render PDF kiểm tra trực quan
    result: Validate PASSED, 8 trang, bảng đúng màu/độ rộng
    evidence: "/mnt/user-data/outputs/Bao_cao_ra_soat_KH_trien_khai_TT64_20260905.docx"

key_findings:
  - id: F1
    location: "Căn cứ thứ nhất (đoạn văn 5)"
    issue: "Trích yếu TT 64/2026/TT-BGDĐT ghi sai, thiếu ngày ban hành"
    level: Mức 1
    basis: "Đối chiếu file gốc + KTC-Database"
    recommendation: "Sửa trích yếu + bổ sung ngày 10/8/2026"
    status: open
  - id: F2
    location: "Căn cứ thứ hai (đoạn văn 6)"
    issue: "Trích yếu QĐ 543/QĐ-UBND không đúng nguyên văn"
    level: Mức 2
    basis: "Đối chiếu bản gốc QĐ 543 + QĐ 988"
    recommendation: "Sửa trích yếu đúng nguyên văn"
    status: open
  - id: F3
    location: "Bảng phân công nhiệm vụ, cột TT"
    issue: "Nhảy số thứ tự, thiếu số 5"
    level: Mức 2
    basis: "Đối chiếu trực tiếp bảng"
    recommendation: "Đánh số lại liên tục"
    status: open
  - id: F4
    location: "Nơi nhận - dòng Lưu"
    issue: "Dùng sai cột viết tắt TCCB&CTHSSV thay vì TCCB"
    level: Mức 2
    basis: "Checklist 08 mục 3.4"
    recommendation: "Sửa thành Lưu: VT, TCCB."
    status: open
  - id: F5
    location: "Câu kết văn bản"
    issue: "Lặp cụm từ Kế hoạch triển khai thực hiện"
    level: Mức 3
    basis: "Đối chiếu trực tiếp đoạn văn"
    recommendation: "Bỏ cụm lặp"
    status: open

user_feedback: []

decisions:
  - decision: "Không áp cấu trúc Căn cứ-Mục tiêu-Nhiệm vụ-Giải pháp-Tổ chức thực hiện"
    reason: "Đây là kế hoạch phân công dạng bảng, không phải kế hoạch chiến lược/năm/chuyên đề"
    evidence: "Checklist 07 + quy tắc vận hành đã xác nhận trước đây"
    made_by: AI
  - decision: "Không kích hoạt Phần V Thẩm định chuyên môn"
    reason: "Không có số liệu tài chính/định mức KT-KT/chương trình đào tạo/y tế/thông số kỹ thuật cần thẩm định"
    evidence: "Nội dung dự thảo chỉ là bảng phân công nhiệm vụ nhân sự"
    made_by: AI

outputs:
  - name: Bao_cao_ra_soat_KH_trien_khai_TT64_20260905.docx
    drive_id_or_link: "/mnt/user-data/outputs/Bao_cao_ra_soat_KH_trien_khai_TT64_20260905.docx (chưa tải lên Drive)"
    version: "1"
    status: "BẢN NHÁP - chờ Phó Trưởng phòng TH-HC&QT phê duyệt"

unresolved_items:
  - item: "Chưa xác minh hiệu lực pháp luật của TT 64/2026/TT-BGDĐT qua nguồn web bên ngoài"
    reason: "Không có công cụ tra cứu web trong phiên này"
    needed_evidence: "Tra cứu vbpl.vn/Công báo Chính phủ khi có công cụ web"
  - item: "Số hiệu Công văn hướng dẫn của Sở GD&ĐT chưa có"
    reason: "Dự thảo chưa điền"
    needed_evidence: "Văn bản chính thức từ Sở GD&ĐT"

lessons: []
supersedes:
superseded_by:
next_action: "Chờ đơn vị soạn thảo (Phòng TCCB&CTHSSV) chỉnh sửa theo báo cáo, có thể rà soát lại bản đã sửa nếu được yêu cầu."
```
