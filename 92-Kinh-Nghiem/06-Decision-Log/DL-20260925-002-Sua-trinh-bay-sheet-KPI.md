# DL-20260925-002 — Sửa trình bày sheet KPI: hết che chữ, đủ cột C–F

**Ngày:** 25/9/2026 · **Căn cứ:** lệnh sửa `LENH-SUA-Loi-trinh-bay-va-thieu-cot-sheet-KPI.md` (Phòng TH-HC&QT, người dùng gửi
vào phiên) · **Kết quả:** `kpi-lap-ke-hoach` 1.2, `kpi-tu-danh-gia` 1.1, plugin 1.2.1. **Không đổi số nào** — ca T9 ghim
tổng điểm, điểm A, điểm B của 6 nhóm trước khi sửa.

## Đối chiếu nguyên nhân trong lệnh với mã và mẫu thật

| Điều lệnh nêu | Thực tế | Xử lý |
|---|---|---|
| L1: `xuong_dong` bỏ qua ô công thức → cột B sheet KPI không được nâng chiều cao | **Đúng** | Hàm mới `gia_tri_hien_thi` đọc chữ ô được trỏ tới |
| L1: openpyxl gộp cột thành một khóa `min–max` | **Đúng** — sheet KPI gộp C–F, I–N, S–Y | `do_rong_cot()` mở rộng từng khóa |
| L2: KPI!C–F bị `xoa_thuc_te` xóa; F ở mẫu là công thức `='Ke Hoach'!E` | **Không đúng** — trong cả 6 mẫu C–F **trống sẵn**; `xoa_thuc_te` chỉ xóa K/L/N/P. Hậu quả (4 cột trống) vẫn đúng | Ghi C–F; F dựng công thức theo lệnh |
| KH17 miễn cho nhóm `ho-tro` "vì mẫu không có cột" | **Không đúng** — mẫu `ho-tro` có cột "Người phối hợp" | KH17 dò theo **tiêu đề cột của mẫu**; ca thử ngược: xóa tiêu đề cột → không KH17 |

## Quyết định

1. Chiều cao dòng = cực đại mọi ô có chữ trong dòng, ký tự × 1,2 / độ rộng (ô gộp cộng độ rộng), × cỡ chữ × 1,3 + 6 pt;
   trần 409 pt kèm KH19. Ước lượng **thiên an toàn**: kiểm bằng ảnh chụp Excel thấy dòng dài có dư khoảng trống dưới, không
   dòng nào bị che.
2. Chỉ nâng chiều cao, không hạ dưới chiều cao đo được; chỉ dòng việc đang hiện, cả "Ke Hoach" và "KPI"; `danh-gia` đo lại.
3. Người phối hợp **không có mặc định** (không tự bịa) — KH17 cảnh báo. Người chỉ đạo mặc định = cấp trình, đơn vị tham
   mưu mặc định = đơn vị công tác (lệnh mục 3.1.2).
4. KH18 (LỖI) bắt ô F trống hoặc công thức trỏ dòng trống/sai; giá trị chữ gõ tay (tệp đơn vị tự điền) chấp nhận.
5. `test_validate_plan.py` từng đếm cứng "990 công thức" → vỡ khi thêm cột F có chủ đích. Đổi thành: 990 công thức của mẫu
   còn nguyên đúng ô + công thức mới chỉ là cột F, đúng một ô mỗi đầu việc.

## Kiểm chứng

- `test_kpi_trinh_bay.py` viết **trước**, chạy thấy 18 ca sai, sửa xong 0 ca sai; các bộ cũ đạt.
- `kiem_the_thuc.py` trên tệp kế hoạch và tệp tự đánh giá: chỉ còn Mức 4 TX04 (in dọc — Known-Issues #9, ngoài phạm vi).
- **Hiển thị:** chụp vùng sheet KPI bằng Excel (COM → ảnh PNG) trên tệp thử dữ liệu giả: nội dung 9 dòng hiện đủ, C–F có
  giá trị. **Chưa kiểm bằng mắt trên tệp thật của người dùng** — chờ ảnh chụp theo mục 7 của lệnh.
- `assets/` không đổi byte.

## Ngoài phạm vi, ghi lại

- TX04 (bảng KPI 19–25 cột in dọc) — đề xuất riêng nếu cần (lệnh mục 6.4).
