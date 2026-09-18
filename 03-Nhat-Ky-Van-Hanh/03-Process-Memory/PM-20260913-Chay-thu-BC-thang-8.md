# PM-20260913-Chay-thu-BC-thang-8

```yaml
memory_id: PM-20260913-001
created_at: 2026-09-13T07:15:00+07:00
memory_type: process
status: closed
task_type: chot_ky_bao_cao          # (d) trong 5 tác vụ
ky: Tháng 8/2026 (kèm kế hoạch tháng 9/2026)
scope: 13 thư mục đơn vị, 40 tệp
project_name: KTC-Quan-tri

input_files:
  - name: input-BC-Thang/ (13 thư mục đơn vị)
    version_or_date: nộp trước 13/9/2026
    role: nguồn báo cáo tháng 8 và kế hoạch tháng 9 của đơn vị
  - name: Ke_hoach_cong_tac_Quy_III_2026_dieu_chinh_bo_sung_CHUAN.xlsx
    role: baseline kế hoạch để duyệt ngược tìm nhiệm vụ bỏ sót

control_versions:
  skill_package: ktc-quan-tri.skill v1.0 (chạy thử) → v1.1 (sau khi sửa)
  bang_ma_don_vi: 01-Chuan-Chung/13-Bang-Ma-Don-Vi.md
  master_task_register: v0.1 (sổ trống, chưa dùng)

sources_verified:
  - source: 328 nhiệm vụ thực trong báo cáo tháng 8 của 13 đơn vị
    status: verified
    note: đọc trực tiếp bằng openpyxl, không qua trung gian
  - source: QĐ 1923/QĐ-CĐKT ngày 30/8/2026 trong KTC-Database
    status: verified
    note: dùng để đối chứng nhiệm vụ 2.8 nghi bỏ sót

process_steps:
  - step: 1
    action: Bước 0 — xác định tác vụ, kỳ, khả năng đọc dữ liệu thật
    result: đủ điều kiện chạy; bộ nhớ vận hành chưa có → chạy tiếp kèm cảnh báo
  - step: 2
    action: Nhận dạng loại tệp theo tiêu đề sheet, không theo tên tệp
    result: phát hiện 3 tệp có tên và nội dung không khớp nhau
  - step: 3
    action: Loại dòng tiêu đề nhóm trước khi đếm
    result: 428 dòng thô → 328 nhiệm vụ thực (100 dòng tiêu đề)
  - step: 4
    action: Kiểm tra công thức quy đổi trên toàn bộ dòng
    result: hệ số = điểm×1% đúng 300/301 dòng
  - step: 5
    action: Duyệt ngược từ Kế hoạch Quý III sang báo cáo tháng 8
    result: 19 nhiệm vụ đến hạn tháng 8 → tìm thấy 12, không thấy 7

key_findings:
  - id: F1
    location: Phong-THHCQT/BAN TT.xlsx
    issue: Tệp ghi "ĐƠN VỊ: BAN TRUYỀN THÔNG" — không phải Phòng TH-HC&QT
    hệ_quả: Phòng TH-HC&QT chưa có báo cáo tháng 8; Ban Truyền thông là đơn vị thứ 12 chưa có mã
    status: open
  - id: F2
    location: Phong-TCCB-CTHHSV/KH t9. P TCCB.xlsx
    issue: Tên tệp là kế hoạch tháng 9 nhưng nội dung là BÁO CÁO kết quả tháng 9 (kỳ chưa kết thúc), dùng sai Phụ lục IIb
    status: open
  - id: F3
    location: Khoa-KT-CN/KTCN.xlsx
    issue: Tiêu đề là báo cáo nhưng cấu trúc cột theo mẫu kế hoạch — cột (8) là "Thời gian hoàn thành" thay vì "Điểm chấm công việc"; 26 nhiệm vụ mất điểm chấm
    status: open
  - id: F4
    location: Khoa-Su-Pham/SP.xlsx
    issue: Tiêu đề tự chế, không theo Phụ lục IIb; chỉ 7 nhiệm vụ so với trung bình 25
    status: open
  - id: F5
    location: Khoa-CKHCB, Khoa-KT-NL
    issue: Báo cáo thiếu hẳn mục Trục 2 và Trục 5
    status: open
  - id: F6
    location: P-QLKH dòng 66
    issue: KPI quy đổi ghi 1, tính đúng phải là 1.5
    status: open

decisions:
  - decision: Không kết luận 7 nhiệm vụ "không tìm thấy" là chưa thực hiện
    reason: nhiệm vụ 2.8 chứng minh ngược lại — đã hoàn thành (QĐ 1923) nhưng không xuất hiện trong báo cáo
    made_by: AI, theo quy tắc "đối chiếu gần đúng phải tự khai" trong SKILL.md
  - decision: Không chốt kỳ tháng 8/2026
    reason: checklist 12 điểm trượt ở mục 2, 3, 5, 6, 9
    made_by: AI

outputs:
  - name: 12-Output/2026-09-13/Chay-thu-chot-ky-Bao-cao-thang-8-2026.md
    status: hoàn thành
  - name: 12-Output/2026-09-13/Phu-luc-chi-tiet-KQ-cong-tac-thang-8-2026_DU-THAO_20260913.xlsx
    status: hoàn thành — 328 dòng, 85 dòng có cảnh báo chất lượng, sheet tổng hợp KPI theo đơn vị
  - name: 12-Output/2026-09-13/Bao-cao-thang-8-2026_DU-THAO_20260913.docx
    status: hoàn thành — dự thảo theo đúng mẫu cấp Trường, đóng dấu DỰ THẢO/KHÔNG TRÌNH KÝ, 4 lỗi đơn vị nêu rõ trong mục II

unresolved_items:
  - item: 7 nhiệm vụ nghi bỏ sót cần đối chiếu lại với từng đơn vị
    needed_evidence: xác nhận từ đơn vị chủ trì hoặc minh chứng sản phẩm
  - item: Phòng TH-HC&QT chưa nộp báo cáo tháng 8
  - item: Phòng TCCB chưa có kế hoạch tháng 9 hợp lệ

lessons:
  - issue: Thang điểm 50/120/250/350/450 bị dùng như ràng buộc kiểm tra
    correction: đó là bảng gợi ý; kiểm tra bằng công thức hệ số = điểm×1%
    scope: references/13-Danh-Muc-Nhiem-Vu-Va-San-Pham.md
    approval_status: incorporated       # đã sửa vào skill v1.1
    lesson_ref: LL-20260913-001
  - issue: Không loại dòng tiêu đề nhóm khiến đếm thừa 30%
    correction: bổ sung quy tắc nhận dạng dòng tiêu đề
    scope: references/24-Chot-Ky-Va-Bao-Cao.md
    approval_status: incorporated
  - issue: Bảng mã đơn vị chỉ có một cấp
    correction: cần cấp hai cho bộ môn/ban/chức danh
    approval_status: proposed

next_action: Yêu cầu 4 đơn vị nộp lại theo đúng mẫu, sau đó chạy chốt kỳ lần 2 và cấp số chính thức cho báo cáo
```

## Bổ sung 13/9/2026 — đã xuất sản phẩm thật

Ban đầu chỉ dừng ở báo cáo phát hiện (`.md`), chưa xuất theo đúng Nguyên tắc 2 (bắt buộc xuất `.docx` cho
kết quả hoàn thành). Đã bổ sung hai sản phẩm, dựng theo đúng mẫu chính thức của `KTC-Bao-Cao`:

- **Phụ lục Excel tổng hợp** — 328 dòng dữ liệu thật, đúng cấu trúc cột TB736, cột "Ghi chú chất lượng"
  đánh dấu 85 dòng thuộc 4 đơn vị có lỗi hồ sơ. Sheet tổng hợp KPI theo đơn vị.
- **Báo cáo Word dự thảo** — theo đúng khuôn `00. Mau bao cao thang (cap Truong).docx`: quốc hiệu, số hiệu
  để trống kèm nhãn DỰ THẢO, 6 mục Trục ở Phần I (nội dung là trích dẫn "sản phẩm" thật từ báo cáo đơn vị,
  không phải văn tường thuật tự bịa), Phần II nêu đúng 5 tồn tại đã phát hiện, Phần III tổng hợp kế hoạch
  tháng 9.

**Sửa một lỗi tự mắc phải khi soạn báo cáo:** bản nháp đầu gộp nhầm hai nhiệm vụ khác nhau (1.23 và 2.8)
thành một dòng trong mục "tồn tại". Phát hiện khi rà lại — đã tách rõ: chỉ nhiệm vụ 2.8 có bằng chứng xác
nhận hoàn thành (QĐ 1923), sáu nhiệm vụ còn lại (gồm 1.23) **chưa xác minh**, không được gộp chung mức độ
chắc chắn.

**KI-004 được giải quyết bằng bằng chứng thật**, không suy diễn: mẫu báo cáo cấp Trường tự nó ghi rõ "Ban
Truyền thông, thuộc phòng TH-HC&QT" — xác nhận đây là bộ phận cấp hai.

## Bổ sung lần 2 (13/9/2026) — dựng lại sản phẩm sau phản hồi bác bỏ

Người dùng bác bỏ bản đầu: *"không đạt yêu cầu về biểu mẫu, thể thức, kỹ thuật trình bày, văn phong"*. Đúng.
Nguyên nhân gốc: dựng từ **mẫu trống** trong khi kho đã có **báo cáo tháng 8/2026 thật do Trường ban hành**
(`BC-375` + `PL-375`) mà tôi đã nhìn thấy từ phiên trước nhưng không mở ra đối chiếu. Xem `LL-20260913-002`.

Nguồn đã đọc để dựng lại: `BC-375...docx` (toàn văn, 92 đoạn) · `PL-375...xlsx` · mẫu chính thức
`03-Templates(1)/06B-Bao-cao-theo-Quy-che-lam-viec.dotx` · `Checklist 08-Quy-Uoc-Rieng-CDKT.md` mục 4
(thông số thể thức TB 597) · `Skill-Tu-hoc-Phong-Cach-Bao-Cao-ra-soat.md`.

Sản phẩm bản v2:

- `BC_Bao-cao-ket-qua-thang-8-2026_DU-THAO-v2_20260913.docx`
- `PL_Phu-luc-chi-tiet-KQ-thang-8-2026_DU-THAO-v2_20260913.xlsx`

Kiểm chứng thể thức đối chiếu trực tiếp với BC-375: **khớp 100%** — khổ 21×29,7cm, lề 2/2/3/2cm, Times New
Roman 14pt, thụt đầu dòng 1,27cm, 2 bảng thể thức (đầu trang và nơi nhận/chữ ký).

**Giới hạn còn lại, đã ghi rõ trên chính văn bản:** nội dung các mục là ghép nguyên văn cột "Nội dung công
việc" của đơn vị, **chưa chuyển sang văn phong cấp Trường** như BC-375 (câu ghép, có số liệu, chủ ngữ "Nhà
trường" xuyên suốt). Việc chuyển văn phong cần người biên tập hoặc một bước xử lý riêng — không tự nhận là
đã đạt.

## Ghi chú ngoài mẫu

**Điều đáng giá nhất của đợt chạy này không phải con số 328 nhiệm vụ, mà là việc quy tắc "đối chiếu gần
đúng phải tự khai là gần đúng" đã ngăn một kết luận sai.** Nếu không có quy tắc đó, bảy nhiệm vụ ở bước
duyệt ngược rất dễ bị trình bày thành "danh sách đơn vị chưa hoàn thành nhiệm vụ" — trong khi ít nhất một
trong số đó đã hoàn thành và có văn bản chứng minh nằm ngay trong kho.

**Ba trong bảy nhiệm vụ nghi bỏ sót thuộc hai đơn vị có lỗi hồ sơ (F1, F2).** Nhiều khả năng đây là hệ quả
của việc nộp thiếu hoặc nộp nhầm mẫu, không phải không làm việc. Cần đối chiếu trước khi đưa vào mục "chưa
hoàn thành" của báo cáo cấp Trường.
