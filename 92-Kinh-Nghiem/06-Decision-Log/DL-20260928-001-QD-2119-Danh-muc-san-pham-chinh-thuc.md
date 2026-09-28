# DL-20260928-001 — QĐ 2119/QĐ-CĐKT: Danh mục sản phẩm, công việc CHÍNH THỨC (thay thế dự thảo TB 1052)

**Ngày:** 28/9/2026 · **Người phụ trách nhấn mạnh:** "văn bản rất quan trọng", "ban hành chính thức, thay thế cho danh
mục trước đây, ghi nhớ thật kỹ lưỡng".

## Văn bản

- **Quyết định số 2119/QĐ-CĐKT ngày 28/9/2026** của Hiệu trưởng (Lê Trí Khải) ban hành Danh mục sản phẩm, công việc;
  hiệu lực từ ngày ký; nơi nhận gồm các đơn vị (Điều 5), lưu VT, TCCB.
  Kho: `KTC-Database/02-KTC-Regulations/02-01- Quy che - quy dinh - huong dan chung/QD-2119-QD-CDKT_Ban-hanh-Danh-muc-san-pham-cong-viec_20260928_v1.docx`.
- **Phụ lục** `PL-2119-QD-CDKT_Danh-muc-san-pham-chuan-hoa_20260928_v1.xlsx` (cùng thư mục): sheet `Danh_muc_san_pham`
  (cột STT · Mã sản phẩm · Tên · Mô tả · Sản phẩm minh chứng · Nhóm · Hệ số · Sản phẩm chuẩn), sheet `Ma_van_ban`
  (28 mã loại VB; quy tắc mã `[Trục].[Nội hàm].[Mã VB].[STT]`, vd `1.3.QD01.12`).
- Căn cứ: QĐ 1976/QĐ-CĐKT; QĐ 366-QĐ/TW; HD 43-HD/BTCTW; HD 02-HD/BTCTW; NĐ 233/2026/NĐ-CP; QĐ 399-QĐ/TU (sửa bởi 507-QĐ/TU);
  HD 01-HD/TU; HD 02-HD/ĐU; TB 817/TB-CĐKT; KH 663/KH-CĐKT; QĐ 1923/QĐ-CĐKT; TB 1052/TB-CĐKT.
- Điều 2: cơ sở xây dựng kế hoạch công tác, đánh giá xếp loại viên chức, người lao động theo quý, năm.
  Điều 3: rà soát, cập nhật hằng năm; đơn vị phản ánh về Phòng TCCB&CTHSSV.

## Số liệu phụ lục (đo 28/9/2026)

- 416 sản phẩm; 38 dòng nội hàm (khớp TB 817); theo Trục: 1 = 134 · 2 = 57 · 3 = 49 · 4 = 68 · 5 = 75 · 6 = 33; không trùng mã.
- Nhóm → hệ số theo **từng sản phẩm**: Nhóm 1 = 0,3 (1) · 0,5 (125) · 1,0 (93); Nhóm 2 = 1,2 (36) · 1,5 (86) · 2,0 (57);
  Nhóm 3 = 2,5 (11); Nhóm 4 = 3,5 (4); Nhóm 5 = 4,5 (3). 8 sản phẩm gắn "Sản phẩm chuẩn".
- So với dự thảo lần 4 (371 sản phẩm, `11-Du-lieu-Cong-Viec/.../Du thao_Danh_muc_SP_...xlsx`): 361 trùng tên, 55 mới,
  10 bị bỏ, 6 đổi hệ số (vd quy chế tuyển sinh 2,5 → 2,0; bản ghi nhớ hợp tác quốc tế 1,0 → 2,0).

## Quyết định

1. QĐ 2119 là **nguồn duy nhất** cho mã sản phẩm và hệ số quy đổi từ 28/9/2026. Dự thảo TB 1052 và thang
   50/120/250/350/450 **hết dùng**, chỉ còn giá trị lịch sử (không xóa tệp dự thảo — còn được tham chiếu).
2. Hệ số lấy **đúng theo từng sản phẩm**, không suy từ nhãn Nhóm; sản phẩm ngoài danh mục → `THIEU_DU_LIEU`.
3. **KI-014 đóng về căn cứ**: hai thang cũ hợp nhất trong một bảng hệ số (giá trị thang 4 mức nằm trong Nhóm 1–2).
4. Mã sản phẩm QĐ 2119 ≠ mã nhiệm vụ chuẩn `A01`–`S04` ≠ Task_ID.
5. Đọc phụ lục thẳng từ kho (không chép về dự án — C12).

## Đã cập nhật ngay (28/9/2026)
`CLAUDE.md` (bảng nguồn + đoạn thang điểm) · bộ nhớ lâu dài `qd-2119-danh-muc-san-pham-chinh-thuc` · `MEMORY-INDEX.md`
· `Pending.md` KI-014 · `11-Du-lieu-Cong-Viec/00-README.md` · `22-KTC-Dieu-Phoi/references/13-Danh-Muc-Nhiem-Vu-Va-San-Pham.md`
(cảnh báo C5: bản trong gói `ktc-quan-tri.skill` chưa có ghi chú — đồng bộ ở bước 2).

## Bước 2 — cập nhật mã, kỹ năng (người phụ trách cho làm 28/9/2026 — ĐÃ XONG, xem mục cuối)
1. `kpi_calc.py` (3 bản: `29-Cong-Cu/`, `28-KTC-KPI/scripts/`, `28-KTC-KPI/Tu-Danh-Gia/scripts/`): bỏ mã
   `THANG_DIEM_CHUA_PHAN_DINH` với phương án A/A×B; tra hệ số theo mã/tên sản phẩm từ PL-2119; lệch hệ số → cảnh báo.
2. `validate_plan.py` KH08: đối chiếu "Danh mục QĐ 2119" thay "Danh mục TB 1052".
3. Chuẩn gốc `20-Chuan-Chung/19-Quy-Tac-KPI.md`, `30-Skill-Phan-Loai-6-Truc.md`, `20-Quy-Tac-Bat-Bien-Va-Khuon-Dau-Ra.md`
   (mô tả mã `THANG_DIEM_CHUA_PHAN_DINH`) → đồng bộ bản sao, đóng gói lại 6–7 gói `.skill`; kỹ năng KPI (SKILL.md, Thuật ngữ,
   Câu hỏi mở), agent `ktc-kiem-ho-so-don-vi`, `ktc-kiem-san-pham`.
4. Ca thử `test_kpi_calc.py` theo hệ số chính thức; plugin **1.3.3**; bằng chứng; cài máy.
5. Không đổi số liệu KPI đã chấm (quý III) — chỉ áp cho kế hoạch, đánh giá từ ngày QĐ có hiệu lực, trừ khi Phòng
   TCCB&CTHSSV hướng dẫn khác (câu hỏi cần xác nhận).

## Kết quả bước 2 (28/9/2026)

- Plugin **1.3.3**, SHA-256 `c1609207bdb910047f9af0b9932d0da986316be0b493506e074700b71e90ec1b` (dựng 2 lần trùng mã), commit `720b853`; validate --strict đạt; kiểm tra hệ thống 0 lỗi,
  0 cảnh báo; hồi quy 21/21; đã cài máy (bản 1.3.2 lưu `ktc-marketplace/ktc-quan-tri.bak-1.3.2`).
- `trich_danh_muc_qd2119.py` → `28-KTC-KPI/references/data/he-so-san-pham-QD2119.csv` (416 dòng, 0 lệch tập hệ số Nhóm);
  `dong_goi_kpi.py` trích lại mỗi lần đồng bộ. CSV, script dự thảo TB 1052 → `99-Luu-Tru/Thay-the-QD-2119/`.
- `kpi_calc.py`: `A` = "Có văn bản" (không còn `THANG_DIEM_CHUA_PHAN_DINH`); `AxB` vẫn cảnh báo (phép nhân chưa có văn bản).
  Tra theo mã sản phẩm, STT phụ lục hoặc tên chính xác. KH08 dẫn QĐ 2119. Câu hỏi mở KPI #2 đóng.
- Skill kpi-lap-ke-hoach 1.3, kpi-tu-danh-gia 1.2, quan-tri 1.14 (cách trích dẫn mới trong `13-Danh-Muc…`).
- Chuẩn `20-Quy-Tac-Bat-Bien…`: `THANG_DIEM_CHUA_PHAN_DINH` chỉ còn cho cách quy đổi chưa có văn bản (A × B, thang dự thảo).
- Guard: `.replace(`/`.rename(` chỉ là ghi khi có `Path(...)` hoặc `os.`; chạy lại 2.241 lệnh thật trong nhật ký phiên:
  1.3.2 chặn 76, 1.3.3 chặn 54 — bỏ 22 chặn nhầm (lệnh chỉ đọc kho), 0 chặn mới; 54 còn lại là mã nhúng vừa nhắc kho vừa
  ghi tệp (đích không xác định — chặn theo thiết kế tầng 2).
- Nghiệm thu `claude plugin eval` ca 05, 07, 08, 09 (tiêu chí 05, 07 cập nhật theo QĐ 2119): 8/8 lượt đạt; ca 05, 07 trả lời
  nêu đúng QĐ 2119 thay thế thang dự thảo.
- Hồ sơ thẩm định vòng 5 chuyển sang 1.3.3: Báo cáo quá trình v6, Hướng dẫn v7, Báo cáo tiếp thu lần 4 v2 (Track Changes +
  bản sạch); sửa số liệu nghiệm thu 1.3.2 ghi nhầm "15/15 ca, 30/30 lượt" (của 1.3.1) → 11/15 ca, 26/30 lượt. Phần cập
  nhật chưa rà soát 897.
- **Chưa làm (chờ quyết định):** `30-Skill-Phan-Loai-6-Truc.md` — cột (9)(10) Phụ lục TB736 vẫn thang 4 mức.
