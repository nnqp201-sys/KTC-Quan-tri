# DL-20260919-006 — Agent `ktc-xac-minh-minh-chung` và công cụ dùng chung `doi_soat_so_lieu.py`

**Ngày:** 19/9/2026 · **Người quyết định:** người dùng ("Thống nhất như đề xuất của em")

**Bối cảnh:** một bản đánh giá (dựa trên v0.7.0) đề xuất thêm 2 agent: `ktc-xac-minh-minh-chung` và
`ktc-doi-soat-so-lieu`. Mình đề xuất và người dùng đồng ý:
- **thêm agent minh chứng**, vì đây là khoảng trống thật: Skill 43 nói "có liên kết không đồng nghĩa đã xác
  minh", nhưng chưa có bước nào kiểm hàng loạt;
- **không tách agent đối soát**: đã có 2 agent làm việc này (`ktc-kiem-ho-so-don-vi` phép kiểm 6,
  `ktc-kiem-san-pham` phép kiểm 3). Thay bằng một **công cụ Python dùng chung**, để hai agent cho cùng một
  kết quả.

**Đính chính bản đánh giá:**
- bản hiện hành đã có 6 agent (có `ktc-tu-hoc`);
- `evidence-verifier` và `logic-reviewer` là agent của plugin 897, dùng cho rà soát dự thảo, không phải minh
  chứng hay số liệu nhiệm vụ;
- trường minh chứng tên là `Minh_Chung`, không phải `Evidence_Link`;
- agent phải được **tạo** báo cáo (không có Edit), chứ không chặn Write như bản đánh giá đề xuất.

**Đã làm:**
- `29-Cong-Cu/doi_soat_so_lieu.py`, 6 phép kiểm, đối soát **giữa các tệp**. Bổ sung cho `read_bc736_excel.py`
  (vốn chỉ kiểm trong một tệp):
  - DS01: chuyển tiếp cảnh báo trong từng tệp;
  - DS02: truy **từng dòng** tổng hợp cấp Trường về nguồn đơn vị;
  - DS03: KH ↔ KQ **cùng kỳ**;
  - DS04: Task_ID trùng;
  - DS05: % KPI theo Trục; lệch thang KI-014 thì đánh dấu, không quy đổi;
  - DS06: mã đơn vị, thiếu tệp Excel.
- `29-Cong-Cu/kiem_minh_chung.py`, 7 phép kiểm MC01–MC07. Đọc cột theo tên tiêu đề, dùng được cho tệp
  theo dõi và Master Task Register. Không gán "Đã xác minh".
- Agent mới `ktc-xac-minh-minh-chung`. Hai agent kiểm tra **bắt buộc** gọi `doi_soat_so_lieu.py`, không cộng tay.
- Plugin chép 2 công cụ vào `scripts/`; bản trong plugin tự tìm `read_bc736_excel` trong
  `skills/bao-cao/`. Checker C9 kiểm import.
- Ca hồi quy: `test_doi_soat_so_lieu.py` (15 ca), `test_kiem_minh_chung.py` (15 ca).
- Plugin **0.9.0**, **7 agent**.

**Lỗi thiết kế tìm ra khi chạy thật trên 13 đơn vị tháng 9, đã sửa, có ca thử ngược:**
1. So KH tháng 9 với KQ tháng 8, tức là khác kỳ.
2. % KPI ra 300–850% do tệp đơn vị trộn hai thang điểm.
3. So tổng hợp cấp Trường với **tổng** đơn vị, trong khi tổng hợp chỉ lấy nhiệm vụ đưa lên Trường.
4. Nội dung chung chung bị ghép nhầm đơn vị: 12 dòng báo lệch sai.
5. Tệp thuyết minh `.docx` bị coi là lỗi.
6. Chạy mất 56 giây; nay 2,7 giây, kết quả giống hệt.

**Phát hiện thật:**
- KI-015: hai đầu mối đoàn thể (`DT-CDCS`, `DT-DTN`) chưa có mã chuẩn.
- Tệp K-KTCN và P-QLKH tháng 8 có nhiều dòng `SAI CT (10)`, dấu hiệu trộn thang điểm (KI-014).
- Bản tổng hợp nháp 13/9 có 24 dòng không ghi nội dung nhiệm vụ.
