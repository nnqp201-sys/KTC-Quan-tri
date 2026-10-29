```yaml
memory_id: PM-20260909-QD-Quan-ly-sang-kien
created_at: 2026-09-09T07:40:00+07:00
memory_type: process
status: closed
task_type: formal_review
document_type: Quyết định (kèm Quy định) - hành chính nhà nước
document_title: Quyết định ban hành Quy định quản lý sáng kiến (thay thế QĐ 1229/QĐ-CĐKT ngày 10/9/2024)
draft_version: dự thảo 09/9/2026 (chưa có số/ngày ký)
responsible_unit: Phòng Quản lý khoa học công nghệ và Hợp tác phát triển
scope: Rà soát chính thức trước khi trình ký (tác vụ a)
project_name: KTC-Ra-Soat-897-v2-Cai-tien

input_files:
  - name: Quyet_dinh_ban_hanh_quy_dinh_quan_ly_sang_kien__09.9.2026.docx
    drive_id_or_link: (file người dùng đính kèm trực tiếp vào chat, không có Drive ID)
    version_or_date: 09/9/2026
    role: dự thảo cần rà soát

control_versions:
  skill_package: ktc-ra-soat-897-v2.22.skill
  skill_md: v2.22 (09/9/2026)
  checklist_08: v2.9 (31/8/2026)
  other_checklists: (không dùng thêm Checklist 01/05 trong ca này - không phát hiện dấu hiệu cần kiểm sâu thêm ngoài phạm vi Checklist 08 và _read_input_properties.py)
  prompt: assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx (khung 897 gốc)
  script: tools/build_ktc897_report.py (v3.4 tương đương) + tools/_read_input_properties.py (v1.1)
  template: ReportBuilder tự dựng theo đặc tả (không load trực tiếp .dotx - đúng cách dùng đã tài liệu hóa của script)

sources_verified:
  - source: Quyết định 988/QĐ-CĐKT (12/5/2026)
    status: verified
    checked_at: "2026-09-09"
    note: căn cứ đầu tiên đúng vị trí theo Checklist 08 mục 1
  - source: Luật Khoa học, công nghệ và đổi mới sáng tạo 93/2025/QH15
    status: verified
    checked_at: "2026-09-09"
    note: đối chiếu qua VBHN Luật KHCN&ĐMST trong Drive, xác nhận đúng thay Luật KHCN 2013 cũ
  - source: Luật Thi đua, khen thưởng 2022 + Luật sửa đổi 06/2026/QH16
    status: verified
    checked_at: "2026-09-09"
    note: hai văn bản Luật gốc đúng, nhưng thiếu nghị định/thông tư hướng dẫn thi hành hiện hành (xem key_findings F1)
  - source: Nghị định 13/2012/NĐ-CP (Điều lệ sáng kiến)
    status: verified
    checked_at: "2026-09-09"
    note: Điều 5 dự thảo trích đúng điểm a khoản 4 Điều 7; Điều 4.2 đúng Điều 8 khoản 2 (đại diện Công đoàn)
  - source: Nghị quyết 10/2026/NQ-HĐND, Hướng dẫn 2244/HD-HĐSK, Quyết định 1428/QĐ-CĐKT
    status: verified
    checked_at: "2026-09-09"
    note: cả ba xác nhận là văn bản thật, còn hiệu lực, đúng nội dung trích dẫn
  - source: Nghị định 152/2025/NĐ-CP, Thông tư 15/2025/TT-BNV (nghi vấn thay NĐ98/2023, TT01/2024)
    status: unverified
    checked_at: "2026-09-09"
    note: chỉ xác nhận gián tiếp qua việc HD 2244/HD-HĐSK (2025) tự trích dẫn 2 văn bản này; công cụ WebSearch bị proxy từ chối (HTTP 403) nên KHÔNG xác minh được hiệu lực/phạm vi thay thế thật từ nguồn bên ngoài
  - source: Quyết định 1229/QĐ-CĐKT (10/9/2024) - bản bị thay thế
    status: verified
    checked_at: "2026-09-09"
    note: dùng để so sánh trực tiếp nội dung Điều 4.2 và mục Nơi nhận

process_steps:
  - step: "Bước 0"
    action: "Xác định hệ quy chiếu + chạy tools/_read_input_properties.py"
    result: "Hệ Hành chính nhà nước (mẫu 2.1 TB597); 0 phát hiện định lượng (lề 20/20/30/20mm đều đạt, font Normal 12pt)"
    evidence: "output JSON rỗng từ read_input_properties(draft.docx)"
  - step: "Đối chiếu kho 01-04"
    action: "Google Drive search_files + read_file_content trên ~10 văn bản liên quan"
    result: "Xác nhận kết nối hoạt động thật (không chỉ dựa vào danh sách tool), đọc được nội dung thật"
    evidence: "các fileId đã đọc: QĐ988, QĐ1229/2024, QĐ1428, NQ10/2026, HD2244, TB1019, ND13/2012, VBHN Luat KHCN, Luat sua doi TDKT"
  - step: "Quét chính tả hệ thống"
    action: "Quét toàn bộ 399 đoạn văn tìm 'đảm bảo' (nên là 'bảo đảm'), 'CỘNG HOÀ', 'UỶ BAN'"
    result: "0 lỗi phát hiện"
    evidence: "script python-docx quét paragraph.text"
  - step: "Kiểm tra font Nơi nhận"
    action: "Đọc run.font.size/bold/italic của bảng chứa mục Nơi nhận (table index 1)"
    result: "Nhãn 'Nơi nhận:' kế thừa 12pt mặc định, đậm+nghiêng; danh sách 11pt - đúng Checklist 08 mục 4"
    evidence: "in trực tiếp run properties qua python-docx"
  - step: "Xây báo cáo .docx"
    action: "Chạy gen_report.py dùng ReportBuilder từ build_ktc897_report.py"
    result: "Xuất file .docx 8 trang, xác nhận qua soffice convert-to-pdf + pdfinfo + kiểm tra app.xml/settings.xml"
    evidence: "Pages=8, Words=2696, Paragraphs=159 ghi đúng vào docProps/app.xml; zoom w:percent hiện diện"

key_findings:
  - id: F1
    location: "Phần căn cứ pháp lý (đoạn 6-8) đối chiếu Điều 12-13, Phụ lục IV-V"
    issue: "Thiếu căn cứ nghị định/thông tư hướng dẫn thi hành Luật Thi đua, khen thưởng hiện hành"
    level: 2
    basis: "HD 2244/HD-HĐSK (19/10/2025) tự trích NĐ152/2025 và TT15/2025; quy tắc 'cặp văn bản gốc-sửa đổi' trong SKILL.md"
    recommendation: "Bổ sung căn cứ sau khi xác minh chính xác số hiệu qua nguồn bên ngoài"
    status: open
  - id: F2
    location: "Khối Số/ngày ban hành trang đầu"
    issue: "Số hiệu và ngày ký còn để trống"
    level: 4
    basis: "Đặc điểm bình thường của dự thảo chưa trình ký"
    recommendation: "Điền đầy đủ trước khi ban hành chính thức, kiểm tra không trùng số"
    status: open
  - id: F3
    location: "Mục Nơi nhận (Công đoàn cơ sở Trường / Đoàn Thanh niên)"
    issue: "Tên gọi khớp Checklist 08 mục 3.4 (tên đầy đủ) nhưng khác thông lệ thực tế nhiều văn bản cũ (tên rút gọn Công đoàn Trường/Đoàn Trường)"
    level: 4
    basis: "Hai khả năng đều có căn cứ - áp dụng quy tắc đúc kết 'không tự kết luận khi có ≥2 khả năng đều có căn cứ' (SKILL.md)"
    recommendation: "Đề nghị Phòng TH-HC&QT xác nhận quy ước thống nhất"
    status: open

user_feedback: []

decisions:
  - decision: "Không nêu lỗi cho việc Điều 4.2 dùng 'Công đoàn cơ sở Trường' trong THÂN VĂN BẢN (khác với mục Nơi nhận)"
    reason: "Đối chiếu QĐ 1229/2024 cho thấy đây là cụm từ kế thừa nguyên vẹn từ bản cũ, không phải lỗi mới; đúng NĐ13/2012 Điều 8.2"
    evidence: "So sánh trực tiếp văn bản 2 bản qua Google Drive"
    made_by: AI
  - decision: "Không nâng F1 lên Mức 1"
    reason: "Luật gốc (khung pháp lý cao nhất) đã được trích dẫn đúng và đầy đủ; chỉ thiếu văn bản hướng dẫn thi hành, không phải sai căn cứ hay trái luật"
    evidence: "Đối chiếu 6 căn cứ khác đều chính xác, đây là thiếu sót bổ sung không làm sai lệch nội dung cốt lõi"
    made_by: AI
  - decision: "Không kết luận F3 là lỗi hay Đạt tuyệt đối - xếp Mức 4 chờ xác nhận"
    reason: "Áp dụng đúng quy tắc 6 trong Bộ quy tắc đúc kết SKILL.md (hai khả năng đều có căn cứ -> hỏi người dùng/Mức 4)"
    evidence: "Checklist 08 mục 3.4 (tên đầy đủ) vs. QĐ1229/2024, QĐ1428/2026, TB1019/2026 (tên rút gọn)"
    made_by: AI

outputs:
  - name: Bao_cao_ra_soat_QD_Quan_ly_sang_kien_20260909.docx
    drive_id_or_link: "(giao trực tiếp cho người dùng qua chat - chưa upload lên Drive theo yêu cầu)"
    version: v1
    status: "BẢN NHÁP - chờ người có thẩm quyền xác nhận (Người kiểm tra chưa điền tên thật, theo đúng quy tắc không được ghi tên công cụ AI)"

unresolved_items:
  - item: "F1 - số hiệu chính xác của nghị định/thông tư hướng dẫn thi hành TĐKT hiện hành"
    reason: "WebSearch bị proxy từ chối (HTTP 403) trong phiên này"
    needed_evidence: "Tra cứu Cổng thông tin điện tử Chính phủ hoặc xác nhận của Phòng TH-HC&QT"
  - item: "F3 - quy ước tên gọi Nơi nhận thống nhất (đầy đủ vs rút gọn)"
    reason: "Checklist 08 và thông lệ thực tế mâu thuẫn, chưa có quyết định chính thức nào giải quyết"
    needed_evidence: "Xác nhận của Phòng TH-HC&QT, có thể cần cập nhật lại Checklist 08 mục 3.4 nếu tên rút gọn mới là chuẩn hiện hành"
  - item: "Người kiểm tra thật (tên + chức danh)"
    reason: "Người dùng chưa cung cấp tên người chịu trách nhiệm xác nhận kết quả"
    needed_evidence: "Cần Trưởng/Phó đơn vị hoặc người có thẩm quyền cung cấp tên trước khi chuyển trạng thái ĐÃ PHÊ DUYỆT"

lessons: []

supersedes:
superseded_by:
next_action: "Chờ người dùng/Phòng TH-HC&QT phản hồi 3 mục unresolved_items trước khi hoàn tất trình ký; nếu có phản hồi xác nhận/bác bỏ phát hiện, cập nhật bản ghi này (không tạo bản mới trừ khi có báo cáo rà soát lần 2)."
```
