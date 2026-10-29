```yaml
memory_id: PM-20260907-CV-Bao-cao-thuyet-minh-Du-an-CTMTQG
created_at: 2026-09-07T00:00:00+07:00
memory_type: process
status: closed
task_type: formal_review_deep
document_type: "Công văn (báo cáo, thuyết minh) kèm Phụ lục I (trong .docx) và Phụ lục II, III (trong .xlsx riêng)"
document_title: "V/v báo cáo, thuyết minh để hoàn thiện phương án phân bổ vốn ngân sách trung ương giai đoạn 2026-2030... thực hiện CTMTQG hiện đại hóa, nâng cao chất lượng GDĐT giai đoạn 2026-2035, giai đoạn I"
draft_version: "Số: /CĐKT-THHCQT, dự thảo ngày .../9/2026 (chưa có số hiệu)"
responsible_unit: "phòng Tổng hợp - Hành chính và Quản trị (theo 'Lưu: VT, THHCQT')"
scope: "Rà soát chính thức, SÂU trước khi gửi — Công văn + Phụ lục I (.docx) + Phụ lục II, III (.xlsx)"
project_name: KTC-Ra-Soat-897-v2-Cai-tien

input_files:
  - name: "08_9_26__CĐ_Kon_Tum-_Gui_bao_cao_thuyet_minh_Du_an.docx"
    role: "Công văn + Phụ lục I"
  - name: "CĐKT__Phu_luc_-kinh-phi-2-3.xlsx"
    role: "Phụ lục II (số liệu minh chứng) và Phụ lục III (kế hoạch vốn)"

control_versions:
  skill_package: "ktc-ra-soat-897 v2.21"
  script: "tools/build_ktc897_report.py v3.4"

sources_verified:
  - source: "CV 5903/BGDĐT-KHTC (03/9/2026), QĐ 1888/QĐ-BGDĐT (30/6/2026), QĐ 36/2026/QĐ-TTg (14/7/2026, đọc toàn văn 15 Điều)"
    status: verified
    note: "Khớp tuyệt đối số hiệu/ngày/trích yếu qua 01-Legal-Database"
  - source: "NQ 71-NQ/TW (22/8/2025)"
    status: verified
    note: "Xác nhận chéo qua 4 văn bản độc lập khác trong kho"
  - source: "NQ 249/2025/QH15 (10/12/2025)"
    status: verified_indirect
    note: "Chưa tìm bản gốc, nhưng xác nhận chéo qua 3 văn bản độc lập khác (QĐ1888, QĐ36, TT112) cùng trích dẫn giống hệt"
  - source: "PL kèm CV 7415/UBND-KGVX (29/7/2026, UBND tỉnh Quảng Ngãi)"
    status: verified
    note: "Số liệu 192,857/150,000 tỷ Dự án 2 khớp với dự thảo hiện tại — xác nhận tính nhất quán với báo cáo cấp tỉnh trước đó"
  - source: "10 văn bản khác (NQ 46/2026/QH16, VB 6095/UBND-KGVX, TB 916/TB-UBND, v.v.)"
    status: unverified
    note: "Không tìm thấy trong kho; đã tự kiểm tra qua tool_search — phiên này không có công cụ tra cứu web"

process_steps:
  - step: "Đối chiếu số liệu chéo docx/xlsx"
    result: "Khớp 100% (162 nhà giáo, 41 CBQL, 2.666 SV, 192,857143/150/21,428571 tỷ...)"
  - step: "Tính lại độc lập phân kỳ vốn theo năm"
    result: "192,857143 - 0,642857 - 25,714286 = 166,5 tỷ — khớp đúng dòng Giai đoạn 2028-2030"
  - step: "Đọc toàn văn QĐ 36/2026/QĐ-TTg Điều 5, Điều 11, Điều 12 và áp dụng công thức Pi vào số liệu Trường tự cung cấp"
    result: "Pi = Hdt(1,0) x Hqm(3,0) x Hcl(2,0) x Hng(1,5) = 9,0 -> Nhóm 3 -> tỷ lệ đối ứng đúng = 5% (~9,64 tỷ), khác với 11,11% (~21,43 tỷ) dự thảo nêu"
  - step: "Kiểm tra đơn vị số liệu câu dẫn Mục 5 Phụ lục I"
    result: "Phát hiện lỗi nghiêm trọng: '192.857.143 triệu đồng' sai gấp 1.000 lần so với bảng liền kề ghi 'ĐVT: Tỷ đồng' = 192,857143"

key_findings:
  - id: II.B-1
    issue: "Câu dẫn Mục 5 Phụ lục I sai đơn vị/định dạng số: '192.857.143 triệu đồng' thay vì '192,857143 tỷ đồng'"
    level: "Mức 1"
    status: open
  - id: II.B-2
    issue: "Tỷ lệ vốn đối ứng nhà trường (11,11%, chia đều 50/50 với địa phương) không khớp mức 5% theo Điều 12 QĐ 36/2026/QĐ-TTg dựa trên Pi=9,0 (Nhóm 3) tính từ chính số liệu Trường cung cấp"
    level: "Mức 1"
    status: open
  - id: II.B-3
    issue: "Mục 6.1: 'tổng nhu cầu kinh phí chuẩn bị đầu tư là .... triệu đồng' còn để trống"
    level: "Mức 2"
    status: open

decisions:
  - decision: "Áp dụng quy tắc mới (05/9/2026): xuất báo cáo 8 phần ngay, không hỏi xác nhận trước khi xuất"
    made_by: AI
  - decision: "Không upload báo cáo lên 12-Output trong phiên này (đã biết giới hạn base64 nhị phân lớn từ DL-20260905-001) — chỉ trình trực tiếp cho người dùng qua present_files"
    reason: "Tránh lặp lại thất bại đã xác nhận trước đó, tiết kiệm thời gian"
    made_by: AI

outputs:
  - name: "Bao_cao_ra_soat_CV-Bao-cao-thuyet-minh-Du-an-CTMTQG_20260907.docx"
    status: "Bản nháp — chưa được Phó Trưởng phòng TH-HC&QT phê duyệt; chưa lưu vào 12-Output"

unresolved_items:
  - item: "10 căn cứ chưa xác minh qua kho"
  - item: "Báo cáo chưa lưu vào 12-Output/2026-09-07/02-Ra-Soat/ do giới hạn kỹ thuật base64 đã biết (DL-20260905-001)"
    needed_evidence: "Người dùng tự tải lên, hoặc thử ở phiên có khả năng ghi Drive trực tiếp (Claude Code/Desktop)"

next_action: "Chờ Phòng Kế hoạch - Tài chính xác nhận lại tỷ lệ vốn đối ứng theo đúng Điều 11, 12 QĐ 36/2026/QĐ-TTg trước khi Trường gửi Sở GDĐT."
```
