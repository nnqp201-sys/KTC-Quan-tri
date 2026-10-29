```yaml
memory_id: PM-20260904-VTVL-Quan-ly-cac-lop-lai-xe-oto
created_at: 2026-09-04T00:00:00+07:00
memory_type: process
status: closed
task_type: formal_review
document_type: Quyết định (kèm Quy định nội bộ + Phụ lục Bản mô tả công việc VTVL)
document_title: "Quyết định ban hành Quy định về vị trí việc làm quản lý các khóa đào tạo lái xe ô tô tại khoa Đào tạo và Sát hạch lái xe"
draft_version: "Số: /QĐ-CĐKT, dự thảo ngày 03/9/2026 (chưa có số hiệu)"
responsible_unit: "Khoa Đào tạo và Sát hạch lái xe (chủ trì); phối hợp phòng Tổ chức cán bộ và Công tác học sinh – sinh viên, phòng Tài chính – Kế toán"
scope: "Rà soát chính thức trước khi trình ký (tác vụ a) — toàn văn Quyết định + Quy định kèm theo (5 Chương, 21 Điều) + Phụ lục Bản mô tả công việc VTVL"
project_name: KTC-Ra-Soat-897-v2-Cai-tien

input_files:
  - name: "1_Quyet_dinh_ban_hanh_VTVL_quan_ly_cac_lop_lai_xe_oto.docx"
    drive_id_or_link: "do người dùng tải lên trực tiếp trong hội thoại (không qua Drive)"
    version_or_date: "03/9/2026"
    role: "dự thảo cần rà soát"

control_versions:
  skill_package: "ktc-ra-soat-897 v2.21 (đọc từ /mnt/skills/user/ktc-ra-soat-897/SKILL.md)"
  skill_md: "v2.21, 31/8/2026"
  checklist_08: "v2.9, 31/8/2026"
  other_checklists: "không dùng Checklist 09 (không phải Hệ D)"
  prompt: "Mẫu prompt rà soát chính thức (assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx) — dùng làm khung tham chiếu, không đính kèm trực tiếp"
  script: "tools/build_ktc897_report.py v3.4; tools/_read_input_properties.py v1.1"
  template: "assets/KTC-Ra-Soat-897_Template_Trong.dotx (đặc tả cấu trúc 8 phần)"

sources_verified:
  - source: "MEMORY-INDEX.md (09-Quan-Tri-He/10-Bo-Nho-He/)"
    status: verified
    checked_at: "2026-09-04"
    note: "Phát hiện 2 bản MEMORY-INDEX.md trùng tên khác nội dung trong cùng thư mục (id 13ovQPhlbMIAhPw8uhS2lIskk_nOg7rNY, v2.21, tạo 01/9; và id 1BuaWVRs_XXWF9HBt8AV72bfMkEO4C9mG, v2.18, tạo 30/8) — đã gắn CONFLICT, dùng bản v2.21 (mới hơn, khớp SKILL.md), CHƯA tự hợp nhất/xóa bản cũ."
  - source: "QĐ 988/QĐ-CĐKT ngày 12/5/2026"
    status: verified
    checked_at: "2026-09-04"
    note: "Khớp Checklist 08 mục 1 — đúng vị trí căn cứ đầu tiên"
  - source: "NĐ 232/2026/NĐ-CP, NĐ 235/2026/NĐ-CP, NĐ 259/2026/NĐ-CP"
    status: verified
    checked_at: "2026-09-04"
    note: "Đọc toàn văn tại 01-Legal-Database/01-04, khớp chính xác số hiệu/ngày/trích yếu dự thảo nêu"
  - source: "TT 14/2025/TT-BXD, TT 17/2026/TT-BXD"
    status: verified
    checked_at: "2026-09-04"
    note: "Đọc toàn văn tại 01-Legal-Database/01-05, khớp chính xác"
  - source: "QĐ 287/QĐ-UBND (29/4/2026), QĐ 1370/QĐ-CĐKT (05/6/2026), QĐ 1086/QĐ-CĐKT (14/11/2025), TB 866/TB-CĐKT (27/7/2026)"
    status: verified
    checked_at: "2026-09-04"
    note: "Đối chiếu qua văn bản gốc/trích dẫn chéo trong kho, khớp chính xác"
  - source: "QĐ 1518/QĐ-CĐKT, QĐ 547/QĐ-UBND, Giấy phép 6099/SXD-VTPT, Luật BHXH 29/6/2024"
    status: unverified
    checked_at: "2026-09-04"
    note: "Không tìm thấy bản gốc trong kho 01-04 để đối chiếu độc lập; không dùng công cụ tra cứu web bên ngoài trong phiên này"

process_steps:
  - step: "Bước 0 — xác định hệ quy chiếu"
    action: "Đọc khối đầu văn bản, ký hiệu số, thẩm quyền ban hành"
    result: "Hệ A — hành chính nhà nước (NĐ 30/2020 + TB 597)"
    evidence: "Khối đầu 'UBND TỈNH QUẢNG NGÃI/TRƯỜNG CAO ĐẲNG KON TUM' + Quốc hiệu/Tiêu ngữ; ký hiệu 'Số: /QĐ-CĐKT' không chứa năm"
  - step: "Đọc thuộc tính định dạng thật của file đầu vào"
    action: "Chạy tools/_read_input_properties.py + kiểm độc lập bằng python-docx (section margins, run.font.size)"
    result: "0 lỗi định lượng — lề 20/20/30/20mm, font Times New Roman 14pt toàn văn bản, đúng chuẩn"
    evidence: "Output script: 0 findings; kiểm tra chéo bằng docx.Document(...).sections[0]"
  - step: "Đối chiếu kho 01-04 (Nguyên tắc 1)"
    action: "Google Drive search_files/read_file_content cho 13 căn cứ pháp lý nêu trong dự thảo"
    result: "9/13 xác minh khớp tuyệt đối; 4/13 không tìm thấy bản gốc trong kho"
    evidence: "Xem sources_verified ở trên"
  - step: "Tính toán lại độc lập số liệu Điều 10"
    action: "Tính lại lưu lượng đào tạo (12×B tự động + 17×B cơ khí + 8×C1) và dự toán kinh phí theo đơn giá nêu trong dự thảo"
    result: "Khớp chính xác 1.770-1.890 học viên/năm và 1.128.590.000 đồng/năm như dự thảo nêu — không phát hiện sai số"
    evidence: "Phép tính thủ công, ghi tại Phần III báo cáo"
  - step: "Đối chiếu logic nội bộ Điều 9 và Điều 11"
    action: "So sánh mô tả số lượng nhân sự hiện đang đảm nhận việc quản lý khóa đào tạo"
    result: "Phát hiện mâu thuẫn: Điều 9.3 nói '2 giáo vụ' đảm nhận, Điều 11 nói '01 giáo vụ + 01 HĐLĐ' đảm nhận"
    evidence: "Trích dẫn nguyên văn 2 đoạn, ghi finding II.B-5 Mức 2"
  - step: "Đối chiếu định nghĩa nhóm vị trí việc làm"
    action: "So sánh mô tả nhiệm vụ Điều 4-8 với định nghĩa Điều 3 khoản 7, 8 NĐ 232/2026/NĐ-CP"
    result: "Phân loại 'Chuyên môn' tại Phụ lục Mục I.2 có thể chưa khớp — cần xác minh thêm, không kết luận thay cơ quan chuyên môn"
    evidence: "Trích dẫn nguyên văn NĐ 232 Điều 3.7, 3.8; ghi finding II.B-6 Mức 4"
  - step: "Xuất báo cáo .docx 8 phần"
    action: "build_ktc897_report.py v3.4 qua ReportBuilder"
    result: "Xuất thành công, validate.py PASSED, metadata Pages=9/Words=3217 đã vá đúng"
    evidence: "stdout 'Đã xuất: ...docx'; validate.py 'All validations PASSED!'"

key_findings:
  - id: II.A-1
    location: "Khối đầu Quyết định và khối đầu Quy định kèm theo (Quốc hiệu)"
    issue: "Chính tả cũ 'CỘNG HOÀ' thay vì 'CỘNG HÒA'"
    level: "Mức 2"
    basis: "SKILL.md Bộ quy tắc đúc kết mục 12"
    recommendation: "Sửa thành 'CỘNG HÒA' ở cả 2 vị trí"
    status: open
  - id: II.A-2
    location: "Địa danh, ngày tháng khối đầu Quyết định"
    issue: "Đã điền ngày '03' cụ thể trong khi Số còn để trống — không nhất quán quy ước để trống ngày"
    level: "Mức 2"
    basis: "Checklist 08 mục 5.2"
    recommendation: "Để trống phần ngày, chỉ giữ tháng/năm, trừ khi đã chắc chắn ngày ký"
    status: open
  - id: II.A-3
    location: "Phụ lục Mục III và Mục V"
    issue: "Viết hoa 'Phòng...' không thống nhất với văn bản chính (viết thường)"
    level: "Mức 3"
    basis: "Checklist 08 mục 3.1"
    recommendation: "Sửa 'Phòng' → 'phòng' tại 3 vị trí trong Phụ lục"
    status: open
  - id: II.A-4
    location: "Toàn văn bản — tên đơn vị ghép"
    issue: "Dùng lẫn gạch nối '-' và gạch ngang '–'"
    level: "Mức 3"
    basis: "Checklist 08 mục 3.4"
    recommendation: "Thống nhất dùng '–' (en-dash) toàn văn bản"
    status: open
  - id: II.B-5
    location: "Điều 9 khoản 3 và đoạn mở đầu Điều 11"
    issue: "Mâu thuẫn số liệu nhân sự hiện có (2 giáo vụ vs. 1 giáo vụ + 1 HĐLĐ)"
    level: "Mức 2"
    basis: "Skill 15 (logic) — đối chiếu nội bộ"
    recommendation: "Làm rõ, thống nhất số liệu trước khi trình ký"
    status: open
  - id: II.B-6
    location: "Phụ lục Mục I.2 (Nhóm vị trí việc làm)"
    issue: "Phân loại 'Chuyên môn' có thể chưa khớp định nghĩa 'Hỗ trợ' theo NĐ 232/2026 Điều 3.7-3.8"
    level: "Mức 4"
    basis: "NĐ 232/2026/NĐ-CP Điều 3 khoản 7, 8"
    recommendation: "Đề nghị phòng TCCB&CTHSSV xác minh lại phân nhóm"
    status: open

user_feedback: []

decisions:
  - decision: "Dùng widths [1.0, 4.3, 9.7, 5.3, 2.9, 2.0]cm (tổng 25.2cm) cho bảng Phần II thay vì đúng tỷ lệ TT10/NỘIDUNG45/NHẬNXÉT100/KIẾNNGHỊ55/CĂNCỨ30/MỨC20mm (tổng 26.0cm) nêu trong SKILL.md"
    reason: "Script build_ktc897_report.py v3.4 raise ValueError thật nếu tổng > 25.7cm — thông số mm trong SKILL.md (tổng 26.0cm) vượt ngưỡng cứng của chính script cùng phiên bản. Đã co tỷ lệ theo hệ số ~0.98 để giữ đúng tỷ lệ tương đối giữa các cột."
    evidence: "table() raise ValueError khi total_w > 25.7cm — đọc trực tiếp code v3.4"
    made_by: AI
  - decision: "Không kết luận đúng/sai về phân loại nhóm vị trí việc làm (finding II.B-6), chỉ nêu điểm cần xác minh thêm ở Mức 4"
    reason: "Đây là nội dung cần chuyên môn tổ chức - cán bộ quyết định, không phải lỗi thể thức/pháp lý rõ ràng"
    evidence: "NĐ 232/2026 Điều 3.7-3.8 định nghĩa mở, cần đối chiếu thực tế phân công nhiệm vụ"
    made_by: AI

outputs:
  - name: "Bao_cao_ra_soat_VTVL_quan_ly_cac_lop_lai_xe_oto_20260904.docx"
    drive_id_or_link: "chưa tải lên Drive trong phiên này — hiện chỉ có trong /mnt/user-data/outputs/ của phiên hội thoại; cần tải lên 12-Output nếu người dùng yêu cầu lưu vào kho"
    version: "1.0"
    status: "Bản nháp — chưa được Phó Trưởng phòng TH-HC&QT phê duyệt"

unresolved_items:
  - item: "4 căn cứ pháp lý chưa xác minh qua kho (QĐ 1518/QĐ-CĐKT, QĐ 547/QĐ-UBND, Giấy phép 6099/SXD-VTPT, Luật BHXH 29/6/2024)"
    reason: "Không tìm thấy bản gốc trong 01-Legal-Database/01-Legal-Database"
    needed_evidence: "Bản gốc hoặc metadata các văn bản này, hoặc xác nhận bằng tra cứu web bên ngoài (vbpl.vn)"
  - item: "Báo cáo chưa được tải lên 12-Output của KTC-Database"
    reason: "Phiên làm việc chỉ xuất file cho người dùng tải về trực tiếp, chưa nhận yêu cầu lưu vào kho dùng chung"
    needed_evidence: "Xác nhận của người dùng có muốn lưu báo cáo vào 12-Output hay không"
  - item: "2 bản MEMORY-INDEX.md trùng tên khác nội dung chưa được xử lý/hợp nhất"
    reason: "Phát hiện ngoài phạm vi tác vụ rà soát văn bản hiện tại — đã gắn CONFLICT nhưng chưa xóa/hợp nhất theo đúng nguyên tắc 'không tự hợp nhất âm thầm'"
    needed_evidence: "Xác nhận của Phòng TH-HC&QT bản nào là chính thức trước khi xóa bản còn lại"

lessons: []

supersedes: null
superseded_by: null
next_action: "Chờ phản hồi người dùng: (1) có cần lưu báo cáo vào 12-Output không; (2) có cần xử lý 2 bản MEMORY-INDEX.md trùng lặp không."
```
