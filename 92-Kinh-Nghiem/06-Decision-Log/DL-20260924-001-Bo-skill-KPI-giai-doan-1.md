# DL-20260924-001 — Bộ skill KPI, giai đoạn 1: `ktc-kpi-lap-ke-hoach`

**Ngày:** 24/9/2026 · **Yêu cầu:** lệnh "Xây bộ skill KPI" của Phòng TH-HC&QT, đã sửa và được duyệt:
`30-Ket-Qua/2026-09-24/De-xuat/LENH-SUA-Xay-bo-skill-KPI-giai-doan-1.md`.

## Quyết định

1. **Một hệ trong KTC-Quan-tri** (`28-KTC-KPI/`), không lập repo riêng. **Quy tắc KPI gốc duy nhất:**
   `20-Chuan-Chung/19-Quy-Tac-KPI.md`. `22-KTC-Dieu-Phoi/references/30-KPI-Va-Xep-Loai.md` trở thành bản sao (DOI_TEN),
   C5 kiểm cả 2 gói.
2. **Hệ số quy đổi không có mặc định.** Script bắt chọn 1 trong 4 phương án; đầu ra ghi phương án và trạng thái căn cứ.
3. **Chỉ giai đoạn 1** (lập kế hoạch). Tự đánh giá và tổng hợp xếp loại chờ QĐ 2078 và các Phụ lục còn thiếu.
4. **Bảo mật:** `30-Ket-Qua/*/KPI-ca-nhan/` vào `.gitignore` (không sao lưu GitHub), có ca thử.

## Phát hiện khi đọc nguồn (đo thật, 24/9/2026)

- **Thang 4 mức có văn bản đã ban hành:** Phụ lục II của QĐ 1923 (mẫu kế hoạch cá nhân) ghi hệ số theo mức độ
  1,0/1,2/1,5/2,0; Phụ lục I có cột Điểm chấm 100/120/150/200 và Hệ số quy đổi. Điều này làm rõ một phần KI-014:
  thang 4 mức **không chỉ** là tập quán dữ liệu mà có trong Phụ lục của Quy chế. Thang 5 nhóm (Danh mục TB 1052) vẫn
  là dự thảo. Không tự kết luận thang nào thay thang nào.
- **Hai mâu thuẫn nội tại QĐ 1923** (ghi Câu hỏi mở số 7, 8): mẫu số trần HTXS cá nhân (Đ19.2a "Hoàn thành tốt trở
  lên" và Đ16.2 "Hoàn thành tốt"); phạm vi "01 quý Không hoàn thành → không HTXS cả năm" (Đ19.1a mọi cá nhân và Đ19.5
  chỉ bắt buộc với quản lý).
- **Hai mốc đầu quý cho cá nhân:** Đ13.1 (05 ngày làm việc, trình Trưởng đơn vị) và Đ15.3a (trước ngày 05 tháng đầu
  quý, gửi Phòng TCCB) — Quý IV/2026 là 07/10 và 04/10. Lệnh sửa từng giả định đây là hai sản phẩm khác nhau — đã đính
  chính: Đ15.3a áp cho **cả tập thể và cá nhân**.
- **Lỗi biểu mẫu mới:** mẫu Phụ lục kèm Bản cam kết đòi tổng trọng số 100% nhưng không có cột trọng số; sheet KPI của
  6 mẫu Quý III tính chất lượng, tiến độ trên số thực tế chưa chặn trần (trái Đ11.6); 10–14 ô Calibri.
- Căn cứ "người đứng đầu không cao hơn đơn vị": QĐ 1923 Đ14.4 dẫn lại khoản 7 Điều 12 NĐ 233/2026/NĐ-CP — ghi cả hai.

## Sản phẩm

| Tệp | Vai trò |
|---|---|
| `20-Chuan-Chung/19-Quy-Tac-KPI.md` | Quy tắc gốc, mỗi dòng dẫn Điều |
| `28-KTC-KPI/` (SKILL.md, references/, scripts/, assets/, `ktc-kpi-lap-ke-hoach-v1.0.skill`) | Hệ mới |
| `29-Cong-Cu/kpi_calc.py`, `kpi_mau.py`, `validate_plan.py`, `trich_danh_muc_tb1052.py`, `dong_goi_kpi.py` | Công cụ nguồn |
| `92-Kinh-Nghiem/02-Regression/Cases/test_kpi_calc.py`, `test_validate_plan.py` | 44 + 26 ca, có ca ngược |
| `28-KTC-KPI/TEST-REPORT.md` | Kết quả thử; định tuyến **chưa chạy thật** trên Chat |
| skill quan-tri 1.10, plugin 1.1.0 | Tích hợp |

## Còn mở — gửi Phòng TCCB&CTHSSV xác nhận

Câu hỏi mở 1–4 (`28-KTC-KPI/references/Cau-Hoi-Mo.md`), 7–9 khi làm giai đoạn 2–3. Kiểm định tuyến trên Chat/Cowork
sau khi cài. Cơ chế loại dữ liệu KPI cá nhân khỏi hook nhật ký: đề xuất riêng, chưa làm. Repo GitHub Private: chưa
xác minh được (máy chưa đăng nhập `gh`).
