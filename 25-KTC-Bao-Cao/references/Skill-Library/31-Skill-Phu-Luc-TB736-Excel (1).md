# 31-Skill-Phu-Luc-TB736-Excel — Phụ lục Excel nhiệm vụ (Ia/Ib/IIb/IIc)
## [MỚI] Bổ sung 17/08/2026 — bắt buộc đọc trước khi dùng Skill 32/33/34

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
- **Mục II**: Nhiệm vụ đột xuất/phát sinh (Ia: "phát sinh ở Quý trước chuyển sang"; Ib: "phát sinh ngoài KH + từ tháng trước chuyển sang").

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

## 5. Liên kết với các Skill hiện có — BẮT BUỘC cập nhật cách hiểu

### Skill 32 (Kiểm tra báo cáo đơn vị) — bổ sung
- Đơn vị nộp báo cáo/kế hoạch **phải ở định dạng Excel Phụ lục Ia/Ib/IIb/IIc**, không phải văn bản .docx tự do.
- Kiểm tra thêm: (a) Hệ số quy đổi có đúng = Điểm/100 không; (b) với IIb/IIc, Số lượng quy đổi và 3 KPI có đúng công thức cascade không; (c) cột Ghi chú có ghi rõ "Đưa vào KH Trường" hay "Thường xuyên của đơn vị" không.

### Skill 33 (Tổng hợp cấp Trường) — bổ sung quan trọng nhất
- **Chỉ tổng hợp lên báo cáo cấp Trường các dòng có Ghi chú = "Đưa vào KH Trường"** trong Phụ lục Ia/Ib; các dòng "Thường xuyên của đơn vị" giữ ở cấp Phòng/Khoa, không đưa vào báo cáo Trường.
- Với Phụ lục IIb/IIc (kết quả), gom nhóm theo Trục, cộng dồn (6),(10) và 3 KPI của TẤT CẢ đơn vị → ra được bức tranh kết quả cấp Trường theo từng Trục.
- **Đây chính là nguồn để sinh nội dung Phần I của báo cáo Word (`fill_bc736.py` content_map)** — thay vì viết tay, có thể tự động tóm tắt: liệt kê các nhiệm vụ nổi bật trong Trục + tỷ lệ % hoàn thành 3 chiều KPI, chuyển thành văn phong cấp Trường.

### Skill 34 (Đối chiếu tiến độ) — bổ sung
- Đối chiếu giờ có 2 lớp: (a) so khớp từng nhiệm vụ Kế hoạch (Ib) với Kết quả (IIb) theo Trục — như hiện tại; (b) **đối chiếu % KPI 3 chiều theo Trục** (đã tính sẵn ở dòng tổng IIb/IIc) làm chỉ số định lượng khách quan cho mức hoàn thành, không cần suy diễn định tính.

### Workflow (09-Tong-Hop-Bao-Cao) — Bước 1 cập nhật
Bước 1 "Tiếp nhận báo cáo đơn vị" nay ghi rõ: đơn vị nộp **file Excel đúng mẫu Phụ lục Ia/Ib (kế hoạch) hoặc IIb/IIc (kết quả)** vào `13-Unit-Reports/`, không nộp văn bản tường thuật tự do.

## 6. Việc cần làm tiếp (đề xuất cho Anh Phục)
1. Cập nhật `32-Skill-Thu-Thap-Bao-Cao-Don-Vi.md` và `33-Skill-Tong-Hop-Bao-Cao-Truong.md` để trích dẫn rõ file này.
2. Viết thêm hàm Python đọc Excel Phụ lục IIb/IIc bằng `openpyxl`, tự động gom nhóm theo Trục và sinh `content_map` cho `fill_bc736.py` — giảm phần lớn công sức nhập tay mỗi tháng.
3. Đóng gói lại `.skill` v2.2 sau khi các Skill 32/33/34 tham chiếu đúng file này.
