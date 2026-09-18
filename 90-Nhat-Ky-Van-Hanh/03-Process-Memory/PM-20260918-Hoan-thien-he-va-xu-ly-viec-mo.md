# PM-20260918-Hoan-thien-he-va-xu-ly-viec-mo

```yaml
memory_id: PM-20260918-001
created_at: 2026-09-18T00:00:00+07:00
memory_type: process
status: closed
task_type: bao_tri_he_thong   # ngoài 5 giá trị mẫu hiện có (chuan_hoa_cap_ma | theo_doi_canh_bao |
                               # doi_chieu_ba_he | chot_ky_bao_cao | kpi_xep_loai) — không loại nào khớp
                               # một ca dọn nợ kỹ thuật + xử lý Known Issues + soạn 1 văn bản. Đề xuất bổ
                               # sung giá trị này vào mẫu nếu ca dạng này lặp lại.
ky: Tháng 9/2026
scope: Toàn dự án KTC-Quan-tri — 5 gói .skill, tài liệu vận hành, 7 Known Issues (KI-001, 006, 007, 008,
  010, 011, 014); KI-002/003 hoãn theo yêu cầu người dùng
project_name: KTC-Quan-tri

input_files:
  - name: 92-Kinh-Nghiem/05-Known-Issues/Pending.md
    version_or_date: 13/9/2026 (trước khi sửa)
    role: danh sách việc mở đầu vào
  - name: 11-Du-lieu-Cong-Viec/DANH MUC SAN PHAM CONG VIEC/Du thao_Danh_muc_SP_theo_loai_van_ban_va_6_truc.xlsx
    version_or_date: đọc trực tiếp 18/9/2026
    role: nguồn số liệu KI-007 và bằng chứng bổ sung KI-014
  - name: KTC-Database/02-KTC-Regulations/05. TB-817-Noi-ham-06-Truc-Ket-qua-trong-tam-Truong-CDKT.docx
    version_or_date: số 817/TB-CĐKT, 14/7/2026
    role: chuẩn đối chiếu KI-011
  - name: KTC-Database/02-KTC-Regulations/05. TB 736 Huong dan dang ky ke hoach, bao cao.docx
    version_or_date: số 736/TB-CĐKT, 25/6/2026
    role: căn cứ Công văn KI-006 + đề xuất KI-001
  - name: KTC-Database/04-Good-Documents/04-08- Cong van/1. CV gop y cac DT TTr, QD, DA Dang kiem lan 4.docx
    version_or_date: số 504/CĐKT-THHCQT, 29/7/2026
    role: văn bản gốc phát triển Công văn KI-006 (NT-1)

control_versions:
  skill_package: ktc-quan-tri.skill (đóng gói lại 18/9/2026, đồng bộ 00-Nguyen-Tac-Chung.md)
  bang_ma_don_vi: 20-Chuan-Chung/13-Bang-Ma-Don-Vi.md (13/9/2026) — phát hiện lệch với Checklist 08 của 897
    ở tên Phòng TCCB, xem key_findings
  master_task_register: không đụng tới trong ca này

sources_verified:
  - source: 4 gói .skill mới (ktc-bao-cao-v3.7, ktc-ke-hoach-v3.3, ktc-soan-thao-vb-v1.1, ktc-theo-doi-cv-v1.1)
    status: verified
    note: build sẵn 14-15/9/2026 nhưng chưa gắn vào hệ; xác minh byte-for-byte trước khi trỏ — xem DL-20260918-001
  - source: KTC-Ra-Soat-897 Checklist 08 (core/references/Checklist/08-Quy-Uoc-Rieng-CDKT.md)
    status: verified
    note: phê duyệt 18/8/2026 bởi Phó Trưởng phòng TH-HC&QT — nguồn thể thức có thẩm quyền cao hơn
      20-Chuan-Chung/13 cho việc soạn văn bản

process_steps:
  - step: 1. Khởi động — đọc MEMORY-INDEX + Pending.md, chạy kiem_tra_he_thong.py
    action: chạy python 29-Cong-Cu/kiem_tra_he_thong.py --chi-tiet
    result: 12 lỗi C5 ban đầu — tất cả cùng gốc, gói .skill cũ chưa đồng bộ 20-Chuan-Chung
  - step: 2. Điều tra + đóng nợ đóng gói skill dở dang
    action: xác minh 4 gói mới có sẵn trên đĩa, trỏ HE dict trong kiem_tra_he_thong.py, phát hiện thêm
      ktc-quan-tri.skill cũng lệch, đồng bộ và đóng gói lại
    result: 0 lỗi, 14 cảnh báo C8 còn lại (khác biệt có chủ đích) — xem DL-20260918-001, commit e5e8b88
  - step: 3. KI-007 — điều tra lệch số liệu danh mục sản phẩm
    action: đếm trực tiếp bằng openpyxl, đối chiếu Số sản phẩm vs tổng theo Nhóm cho cả 6 Trục
    result: chỉ 1 ô (Trục 1, gõ cứng 102) sai; giá trị đúng 103, đã kiểm chứng bằng 2 cách độc lập
  - step: 4. KI-014 — định lượng mức lẫn hai thang điểm trong chính tệp dự thảo lần 4
    action: đối chiếu Nhóm-nhãn vs Điểm-thực trên 371 dòng sản phẩm với cả hai thang đã biết
    result: 201/371 dòng (54%) nhãn Nhóm mới nhưng Điểm vẫn giá trị thang cũ — dữ kiện, không tự kết luận
      thang nào đúng
  - step: 5. KI-011 — đối chiếu tên Trục với TB 817 gốc
    action: đọc bảng Phụ lục TB 817 (3 bảng, 45 dòng) bằng python-docx, so với 6 nhãn Trục trong file dự
      thảo lần 4
    result: dựng bảng đối chiếu đầy đủ 6/6 Trục kèm mức lệch; xác nhận read_bc736_excel.py không bị ảnh
      hưởng (đã dùng đúng tên TB 817)
  - step: 6. KI-008 — quét toàn văn KTC-Database tìm VNPT KPI
    action: quét 173 tệp .docx trong 02-KTC-Regulations tìm "vnpt", "danh mục sản phẩm", "quy đổi"...
    result: loại trừ nhầm lẫn VNPT-Office/VNPT-iOffice (hệ khác); không tìm thêm tài liệu nào về VNPT KPI
      ngoài KH-834 đã biết; tìm được đầu mối khả dĩ (Phòng TCCB, theo QĐ 1883)
  - step: 7. KI-001 — dựng đề xuất kỹ thuật thêm cột Task_ID
    action: đọc cấu trúc thật mẫu Phụ lục Ia/Ib/IIb/IIc (TB736) bằng openpyxl, đối chiếu chỉ số cột cố
      định trong read_bc736_excel.py
    result: đề xuất thêm cột cuối (L cho Ia/Ib, R cho IIb/IIc) — cộng thêm, không phá chỉ số cũ; xuất
      30-Ket-Qua/2026-09-18/De-xuat/
  - step: 8. KI-006 — soạn Công văn nhắc 6 đơn vị
    action: copy văn bản Công văn đã ban hành làm nền (NT-1), thay nội dung bằng python-docx (giữ run
      formatting), rà soát nhanh theo Checklist 08, sửa 4 lỗi tự phát hiện
    result: bản dự thảo hoàn chỉnh, đã kiểm ZIP signature + testzip(), đánh dấu rõ "DỰ THẢO — CHƯA BAN
      HÀNH" trong chính văn bản

key_findings:
  - id: F1
    location: 11-Du-lieu-Cong-Viec/.../Du thao_Danh_muc_SP_theo_loai_van_ban_va_6_truc.xlsx, sheet
      "Tong hop theo Truc", ô B2
    issue: "Số sản phẩm" Trục 1 ghi 102 (gõ cứng), đúng phải 103
    hệ_quả: không ảnh hưởng dữ liệu vận hành thật (dòng chi tiết đã đúng), chỉ sai ở ô tổng hợp hiển thị
    status: open   # đã tìm ra nguyên nhân, chưa tự sửa nguồn — chờ người giữ tệp
  - id: F2
    location: cùng tệp, sheet "Danh muc san pham", 371 dòng
    issue: 201/371 dòng (54%) nhãn Nhóm (thang 5 nhóm) nhưng Điểm vẫn là giá trị thang 4 mức cũ
    hệ_quả: củng cố nghi vấn "di chuyển dở dang" cho KI-014, nhưng KHÔNG đủ để AI tự kết luận thang nào
      là chuẩn — chỉ trình bày dữ kiện
    status: open
  - id: F3
    location: 20-Chuan-Chung/13-Bang-Ma-Don-Vi.md dòng 17 vs Checklist 08 mục 3.4 (897)
    issue: tên Phòng TCCB ghi khác nhau — "...Công tác học sinh, sinh viên" (dấu phẩy) vs "...học sinh –
      sinh viên" (gạch nối), Checklist 08 mới hơn và đã phê duyệt 18/8/2026
    hệ_quả: nếu dùng nhầm nguồn khi soạn văn bản sẽ sai tên đơn vị trong "Kính gửi"
    status: open   # chưa sửa 20-Chuan-Chung/13 — ngoài phạm vi ca này, chỉ ghi nhận
  - id: F4
    location: Công văn dự thảo KI-006 trước khi rà soát
    issue: 4 lỗi thể thức (ký hiệu sai mẫu "CV-...", chính tả "CỘNG HOÀ", thiếu viết hoa sau hai chấm x5,
      tên đơn vị lệch — xem F3)
    hệ_quả: nếu không rà soát trước khi đưa người dùng sẽ mang lỗi thể thức ra ngoài
    status: fixed

decisions:
  - decision: Trỏ 29-Cong-Cu/kiem_tra_he_thong.py vào 4 gói .skill mới thay vì đóng gói lại từ đầu
    reason: đã xác minh byte-for-byte gói mới khớp nguồn rời và 20-Chuan-Chung, không mất nội dung so
      với gói cũ
    made_by: AI
  - decision: Không tự chọn thang điểm nào đúng cho KI-014, không tự đổi tên Trục trong KI-011, không tự
      sửa số liệu KI-007
    reason: nguyên tắc bất biến #6 — AI không thay dữ liệu gốc, không quyết định thay người có thẩm quyền
    made_by: AI
  - decision: Hoãn KI-002 (dữ liệu 6 Khoa) và KI-003 (mã đơn vị cấp hai)
    reason: người dùng xác nhận trực tiếp "sẽ hoàn thiện sau"
    made_by: user

outputs:
  - name: 92-Kinh-Nghiem/06-Decision-Log/DL-20260918-001-Hoan-tat-dot-dong-goi-15-9-con-do-dang.md
    status: hoàn chỉnh
  - name: 30-Ket-Qua/2026-09-18/De-xuat/De-xuat-Bo-sung-Cot-Task_ID-Phu-luc-TB736.md
    status: hoàn chỉnh, chờ người có thẩm quyền xác nhận trước khi áp dụng
  - name: 30-Ket-Qua/2026-09-18/Cong-Van/DU-THAO_CV_Bo-sung-chinh-sua-ho-so-KH-BC-thang-8-9-2026.docx
    status: dự thảo hoàn chỉnh, đã rà soát nhanh, chờ Phòng TH-HC&QT kiểm tra + trình ký

unresolved_items:
  - item: KI-014 — hai thang điểm, cần người có thẩm quyền chọn hướng (a)/(b)/(c)
    needed_evidence: quyết định của đơn vị giữ 11-Du-lieu-Cong-Viec + Phòng TCCB
  - item: KI-011 — cập nhật tên Trục trong danh mục 122 nhiệm vụ chuẩn hay xác nhận cố ý khác
    needed_evidence: quyết định của người giữ tệp 11-Du-lieu-Cong-Viec
  - item: KI-008 — phạm vi quản lý và khả năng xuất dữ liệu của phần mềm VNPT KPI
    needed_evidence: xác nhận từ Phòng TCCB & CTHSSV (đầu mối khả dĩ theo QĐ 1883)
  - item: KI-010 — nhật ký chạy thử trên Claude Chat
    needed_evidence: transcript hoặc mô tả lại từ người dùng — AI không có cách nào tự lấy được

lessons:
  - issue: Gói .skill có thể build xong nhưng "vô hình" với hệ nếu không cập nhật đồng thời công cụ kiểm
      tra tĩnh VÀ tài liệu vận hành
    correction: khi phát hiện gói mới hơn gói đang trỏ, luôn xác minh 3 việc trước khi coi là an toàn để
      dùng — (1) frontmatter/liên kết, (2) tự khai phiên bản khớp tên tệp, (3) so danh sách tệp cũ→mới để
      chắc không mất nội dung
    scope: toàn dự án, mọi lần đóng gói trong tương lai
    approval_status: proposed
    lesson_ref:
  - issue: Rà soát nhanh (897) áp dụng cả cho văn bản AI tự soạn từ file tương đồng, không chỉ văn bản có
      sẵn — bắt được 4 lỗi thể thức thật trong lần đầu áp dụng
    correction: luôn chạy quick-review trước khi bàn giao văn bản outward-facing, kể cả khi tự tin đã theo
      đúng mẫu gốc — mẫu gốc (văn bản đã ban hành) chính nó cũng có thể mang lỗi cũ (vd. "CỘNG HOÀ")
    scope: mọi văn bản soạn mới trong dự án
    approval_status: proposed
    lesson_ref:

supersedes:
superseded_by:
next_action: Chờ người dùng chọn tiếp — (a) quyết định hướng KI-014, (b) xác nhận/ký Công văn KI-006,
  (c) chuyển sang việc nghiệp vụ khác (chốt kỳ, dựng kế hoạch/báo cáo tháng)
```
