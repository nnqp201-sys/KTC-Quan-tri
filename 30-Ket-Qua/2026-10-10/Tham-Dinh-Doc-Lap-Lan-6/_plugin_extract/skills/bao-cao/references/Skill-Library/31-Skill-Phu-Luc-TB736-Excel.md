# 31-Skill-Phu-Luc-TB736-Excel — Phụ lục Excel nhiệm vụ (Ia/Ib/IIb/IIc)
## Cập nhật 18/08/2026 — đối chiếu file thật, sửa 2 lỗi quan trọng

## 1. Vì sao file này tồn tại
Thông báo 736/TB-CĐKT không chỉ có mẫu báo cáo Word tường thuật (`00__Mau_bao_cao_thang__cap_Truong_.docx`) mà còn **4 mẫu Excel Phụ lục** để từng đơn vị (Phòng/Khoa) kê khai nhiệm vụ ở mức chi tiết nhất — đây là **nguồn dữ liệu gốc**, mẫu Word cấp Trường chỉ là bản tường thuật tổng hợp từ dữ liệu này.

Nguồn: `03-Templates/03-06-Bao-cao/5. TB 736. Phu luc Ia, Ib, IIb, IIc - Mau ke hoach, bao cao cong tac thang, quy.xlsx`

## 2. Bốn Phụ lục — phân biệt rõ

| Phụ lục | Loại | Kỳ | Có cột KPI? |
|---|---|---|---|
| **Ia** | Kế hoạch | Quý | Không |
| **Ib** | Kế hoạch | Tháng | Không |
| **IIb** | Kết quả (báo cáo) | Tháng | **Có** |
| **IIc** | Kết quả (báo cáo) | Quý | **Có** |

Mỗi Phụ lục dùng ở **cấp đơn vị** (Phòng/Khoa nộp lên), Skill 33 mới tổng hợp thành bản cấp Trường.

## 3. Cấu trúc cột — Phụ lục Ia / Ib (Kế hoạch, 11 cột, không KPI)
`(1) TT | (2) Nội dung công việc | (3) Người trực tiếp chỉ đạo | (4) Đơn vị chủ trì | (5) Sản phẩm/công việc | (6) Số lượng | (7) Độ khó | (8) Thời gian hoàn thành | (9) Điểm chấm công việc | (10) Hệ số quy đổi | (11) Ghi chú`

Cấu trúc 2 mục:
- **Mục I**: Các nhiệm vụ theo kế hoạch (chương trình) đã đề ra từ đầu quý/tháng — chia theo 6 Trục.
- **Mục II**: Ý NGHĨA KHÁC NHAU tùy loại Phụ lục — **xác nhận từ file thật 18/08/2026**:
  - **Ia/Ib (Kế hoạch)**: "phát sinh ngoài KH + từ kỳ trước chuyển sang" — nhiệm vụ MỚI cần làm.
  - **IIb/IIc (Kết quả)**: "**CÁC NHIỆM VỤ CHƯA HOÀN THÀNH, ĐANG TRIỂN KHAI THỰC HIỆN (CHUYỂN SANG THÁNG SAU)**" — nhiệm vụ đã có trong Mục I nhưng CHƯA XONG, không phải việc mới.
  - **⚠️ Quan trọng**: trong file KQ thật, các nhiệm vụ ở Mục II liệt kê tuần tự (1, 2, 3...) KHÔNG kèm Trục con — khác hẳn Mục I (có "Trục (N)..." trước mỗi nhóm). `read_bc736_excel.py` xử lý riêng: khi gặp Mục II, ngừng gán Trục tự động, thu vào danh sách `muc_ii_items` riêng — **KHÔNG ép vào Trục cuối cùng của Mục I** (lỗi tiềm ẩn đã phát hiện và sửa 18/08/2026).

Cột Ghi chú (11) có 2 giá trị chuẩn: **"Đưa vào KH Trường"** (nhiệm vụ đủ tầm ảnh hưởng để lên báo cáo cấp Trường) hoặc **"Thường xuyên của đơn vị"** (chỉ ở cấp Phòng/Khoa, không đưa lên Trường). — **Skill 33 dùng cột này để lọc nhiệm vụ nào cần tổng hợp lên báo cáo cấp Trường.**

## 4. Cấu trúc cột — Phụ lục IIb / IIc (Kết quả, 16 cột, có KPI)
`(1) TT | (2) Nội dung | (3) Người chỉ đạo | (4) Đơn vị chủ trì | (5) Sản phẩm | (6) Số lượng | (7) Độ khó | (8) Điểm chấm | (9) Hệ số quy đổi | (10) Số lượng quy đổi | (11)(12) KPI số lượng [TT/QĐ] | (13)(14) KPI chất lượng [TT/QĐ] | (15)(16) KPI tiến độ [TT/QĐ]`

### Công thức cascade (bắt buộc hiểu đúng trước khi tính hộ đơn vị)
```
(9)  Hệ số quy đổi        = (8) Điểm chấm × 1%          [200→2, 150→1.5, 120→1.2, 100→1]
(10) Số lượng quy đổi     = (6) Số lượng × (9) Hệ số
(11) KPI số lượng - TT    = (6) Số lượng × [Tỷ lệ hoàn thành khối lượng]
(12) KPI số lượng - QĐ    = (9) Hệ số × (11)
(13) KPI chất lượng - TT  = (11) × [Tỷ lệ hoàn thành chất lượng]
(14) KPI chất lượng - QĐ  = (9) Hệ số × (13)
(15) KPI tiến độ - TT     = (11) × [Tỷ lệ hoàn thành tiến độ]
(16) KPI tiến độ - QĐ     = (9) Hệ số × (15)
```
**Quy tắc trừ điểm mẫu** (đơn vị có thể điều chỉnh, không suy diễn nếu chưa rõ):
- Thiếu 1 sản phẩm so với kế hoạch → tỷ lệ hoàn thành khối lượng = 75% (trừ 0,25)
- Sửa đổi 1-2 lần → tỷ lệ hoàn thành chất lượng = 75% (trừ 0,25)
- Chậm tiến độ → tỷ lệ hoàn thành tiến độ = 75% (trừ 0,25)

### Dòng tổng theo Trục
Mỗi Trục có 1 dòng tổng (SUM) các cột (6),(10),(11)-(16) — đây là **% hoàn thành cấp Trục theo 3 chiều KPI**, dùng trực tiếp cho Skill 34 (đối chiếu tiến độ) thay vì phải so sánh thủ công từng dòng.

## 5. Liên kết với các Skill hiện có

### Skill 32 (Kiểm tra báo cáo đơn vị)
- Đơn vị nộp báo cáo/kế hoạch **phải ở định dạng Excel Phụ lục Ia/Ib/IIb/IIc**, không phải văn bản .docx tự do.
- Kiểm tra thêm: (a) Hệ số quy đổi có đúng = Điểm/100 không; (b) với IIb/IIc, Số lượng quy đổi và 3 KPI có đúng công thức cascade không; (c) cột Ghi chú có ghi rõ "Đưa vào KH Trường" hay "Thường xuyên của đơn vị" không.
- Dùng `read_bc736_excel.py` (hàm `read_appendix()`) để tự động phát hiện sai công thức.

### Skill 33 (Tổng hợp cấp Trường)
- **Chỉ tổng hợp lên báo cáo cấp Trường các dòng có Ghi chú = "Đưa vào KH Trường"** trong Phụ lục Ia/Ib; các dòng "Thường xuyên của đơn vị" giữ ở cấp Phòng/Khoa. Dùng hàm `filter_truong_level()`.
- Với Phụ lục IIb/IIc (kết quả), gom nhóm theo Trục, cộng dồn (6),(10) và 3 KPI của TẤT CẢ đơn vị → ra được bức tranh kết quả cấp Trường theo từng Trục. Dùng hàm `summarize_truc_kpi()`.
- **Đây chính là nguồn để sinh nội dung Phần I của báo cáo Word (`fill_bc736.py` content_map)** — dùng hàm `build_content_map_skeleton()` để dựng khung nháp, sau đó biên tập lại theo văn phong cấp Trường (Skill-Tu-hoc) trước khi dùng thật.

### Skill 34 (Đối chiếu tiến độ)
- Đối chiếu giờ có 2 lớp: (a) so khớp từng nhiệm vụ Kế hoạch (Ib) với Kết quả (IIb) theo Trục; (b) **đối chiếu % KPI 3 chiều theo Trục** (đã tính sẵn ở dòng tổng IIb/IIc, hoặc qua `summarize_truc_kpi()`) làm chỉ số định lượng khách quan cho mức hoàn thành.

### Workflow (09-Tong-Hop-Bao-Cao) — Bước 1
Bước 1 "Tiếp nhận báo cáo đơn vị" nay ghi rõ: đơn vị nộp **file Excel đúng mẫu Phụ lục Ia/Ib (kế hoạch) hoặc IIb/IIc (kết quả)** vào `13-Unit-Reports/`, không nộp văn bản tường thuật tự do.

## 6. Công cụ liên quan trong Skill-Library
- `read_bc736_excel.py` — đọc Excel Phụ lục, kiểm tra công thức KPI, lọc theo Ghi chú, tổng hợp % theo Trục, dựng khung content_map nháp, tách riêng Mục II. Đã kiểm thử 17/08 và 18/08/2026 (đối chiếu file thật).
- `fill_bc736.py` — điền mẫu Word TB736 cấp Trường từ content_map đã biên tập.
- `README-fill_bc736.md` — danh sách đầy đủ **45 vị trí thật** trong mẫu Word (27 ở Phần I, 2 ở Phần II, 16 ở Phần III), đã kiểm chứng bằng test tự động.

## 7. Nhật ký sửa lỗi — đối chiếu file thật (18/08/2026)
Anh Phục cung cấp 2 file mẫu thật (`00. Mau bao cao thang (cap Truong).docx` và `00. Phu luc chi tiet ket qua cong tac thang (cap Truong).xlsx`) để đối chiếu. Phát hiện và sửa 2 lỗi:

1. **Regex nhận diện "Trục" sai** — dữ liệu tự tạo trước đó dùng tiền tố "1. Trục (1)...", nhưng file thật dùng đúng "Trục (1)..." KHÔNG có tiền tố số. Regex cũ chỉ khớp dạng có tiền tố → bỏ sót toàn bộ Trục khi đọc file thật. Đã sửa regex chấp nhận cả 2 dạng.
2. **Mục II bị gán nhầm Trục** — nhiệm vụ "chưa hoàn thành" ở Mục II (Phụ lục KQ) không có Trục con kèm theo, nhưng code cũ vẫn gán chúng vào Trục cuối cùng còn hiệu lực từ Mục I (sai). Đã sửa: khi vào Mục II, dừng gán Trục, thu vào `muc_ii_items` riêng.
