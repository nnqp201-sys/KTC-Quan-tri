# Danh mục nhiệm vụ chuẩn và quy đổi sản phẩm

**Nguồn:** `KTC-Du-lieu-Cong-Viec/DANH MUC SAN PHAM CONG VIEC/` — hai tệp Excel.
**Căn cứ gốc:** Quyết định 1923/QĐ-CĐKT ngày 30/8/2026 và các Phụ lục I, II, III kèm theo.

## 1. Danh mục 122 nhiệm vụ chuẩn — 17 lĩnh vực

Mã dạng một chữ cái + hai chữ số (`A01`–`S04`), gộp từ 1.358 dòng nhiệm vụ gốc của 69 tệp Biểu số 1.

| Mã | Lĩnh vực | Số NV | | Mã | Lĩnh vực | Số NV |
|---|---|---|---|---|---|---|
| A | Lãnh đạo, quản lý, điều hành | 15 | | L | Chuyển đổi số, công nghệ thông tin | 4 |
| B | Văn thư, lưu trữ, hành chính | 9 | | M | Truyền thông | 5 |
| C | Tổ chức cán bộ, chế độ chính sách | 7 | | N | Tài chính, kế toán | 9 |
| D | Công tác Đảng, đoàn thể | 4 | | P | Quản trị cơ sở vật chất, tài sản | 7 |
| E | Quản lý đào tạo | 11 | | Q | An ninh, quốc phòng, an toàn | 6 |
| F | Khảo thí, văn bằng chứng chỉ | 6 | | R | Công tác học sinh, sinh viên | 6 |
| G | Bảo đảm chất lượng, kiểm định | 8 | | S | Nhiệm vụ chuyên môn nhà giáo | 4 |
| H | Tuyển sinh, hướng nghiệp, việc làm | 6 | | | | |
| I | Hợp tác doanh nghiệp, hợp tác quốc tế | 7 | | | | |
| K | Khoa học công nghệ, sáng kiến | 8 | | | | |

**Không có chữ J và O** — bỏ qua để tránh nhầm với số 1 và số 0.

### Cảnh báo độ phủ — đọc kỹ trước khi gán mã

1.358 nhiệm vụ gốc **chỉ đến từ 5 Phòng**: TH-HC&QT (402 dòng), QLKHCN&HTPT (387), QLĐT&BĐCL (366),
Phòng Tổ chức (126), TC-KT (77). **Sáu Khoa hoàn toàn vắng mặt** — dự kiến bổ sung sau. Lĩnh vực
`S. Nhiệm vụ chuyên môn nhà giáo` chỉ có 4 mã, sinh ra từ viên chức Phòng có tham gia giảng dạy, không
phải từ khảo sát các Khoa.

**Hệ quả bắt buộc tuân thủ:** khi nhiệm vụ của một Khoa không khớp mã nào, để **trống** `Ma_NV_Chuan`, ghi
rõ "danh mục chưa có mã phù hợp" và đề nghị bổ sung mã mới. **Không ép về mã gần đúng** — làm vậy tạo dữ
liệu sai mà về sau không ai phát hiện được.

## 2. Danh mục 371 sản phẩm quy đổi

Mỗi sản phẩm gắn: loại văn bản (29 loại) · Nhóm 1–5 · Điểm · Hệ số · Trục · Nội hàm.

**Trạng thái: dự thảo lần 4** — điểm và hệ số chưa phải bản ban hành. Khi trích dẫn phải ghi rõ là dự thảo.

### Thang quy đổi 5 nhóm — là bảng GỢI Ý, không phải danh sách giá trị hợp lệ

| Nhóm | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Điểm chấm | 50 | 120 | 250 | 350 | 450 |
| Hệ số quy đổi | 0,5 | 1,2 | 2,5 | 3,5 | 4,5 |

**Không dùng bảng này để kiểm tra dữ liệu vận hành.** Đây là thang gợi ý khi xây dựng danh mục sản phẩm
(dự thảo lần 4), không phải danh sách giá trị hợp lệ của cột "Điểm chấm công việc".

Đối chiếu trên 328 nhiệm vụ thật của báo cáo tháng 8/2026 (13 đơn vị) cho thấy các đơn vị đang dùng thang
**hoàn toàn khác**: 100 (170 dòng) · 120 (65) · 150 (40) · 200 (20) · 30 (6). Chỉ giá trị 120 trùng nhau.

### Quy tắc kiểm tra ĐÚNG — dùng công thức, không dùng danh sách

Cột "Điểm chấm công việc" trên Phụ lục I/IIb là **ô số tự do**. Điều kiểm tra được là các công thức in sẵn
trên chính biểu mẫu:

| Cột | Công thức | Ghi chú |
|---|---|---|
| (9) Hệ số quy đổi | `= (8) × 1%` | Tức hệ số = điểm ÷ 100. Kiểm chứng đúng 300/301 dòng thật |
| (10) Số lượng quy đổi | `= (6) × (9)` | Số lượng × hệ số |
| (12) KPI quy đổi | `= (9) × (11)` | Hệ số × KPI thực tế hoàn thành |

Điểm chấm lệch khỏi thang 5 nhóm **không phải lỗi**. Hệ số sai so với `điểm × 1%` **mới là lỗi**.

### 29 loại văn bản — mã và số sản phẩm sử dụng

| Mã | Loại văn bản | SP | | Mã | Loại văn bản | SP |
|---|---|---|---|---|---|---|
| 1 | Nghị quyết | 1 | | 9.1 | Báo cáo tuần, tháng, quý, 6 tháng | 14 |
| 2 | Quyết định | 21 | | 9.2 | Báo cáo năm | 15 |
| 3 | Quy chế, Quy định | 40 | | 9.3 | Báo cáo giai đoạn | 5 |
| 3.1 | Công văn nội bộ Trường | 32 | | 9.4 | Báo cáo tiếp thu, giải trình | 32 |
| 3.2 | Công văn ra ngoài Trường | 34 | | 9.5 | Báo cáo khác | 14 |
| 4 | Thông báo | 2 | | 10 | Biên bản | 2 |
| 5 | Hướng dẫn | 33 | | 11 | Phiếu gửi, Phiếu chuyển, Phiếu báo | 1 |
| 6 | Thông cáo, Công điện | 0 | | 12 | Tờ trình | 1 |
| 7.1 | Chương trình, kế hoạch công tác tháng, quý | 3 | | 13 | Hợp đồng | 2 |
| 7.2 | Chương trình, kế hoạch công tác năm | 26 | | 14 | Bản ghi nhớ, Bản thỏa thuận | 4 |
| 7.3 | Chương trình, kế hoạch công tác giai đoạn | 6 | | 15 | Giấy ủy quyền/mời/giới thiệu/nghỉ phép/đi đường, Thư công | 1 |
| 7.4 | Kế hoạch triển khai công việc nội bộ | 20 | | 16 | Chuyên môn *(không phải văn bản hành chính)* | 25 |
| 7.5 | Kế hoạch triển khai văn bản cấp trên | 5 | | 17 | Phục vụ *(không phải văn bản hành chính)* | 17 |
| 8 | Phương án, Đề án, Dự án | 11 | | 18 | Lãnh đạo, điều hành *(không phải văn bản hành chính)* | 2 |
| | | | | 19 | Sản phẩm truyền thông *(không phải văn bản hành chính)* | 1 |

Bốn loại 16–19 **không phải văn bản hành chính** — đó là hoạt động chuyên môn, phục vụ, chỉ đạo điều hành
và ấn phẩm truyền thông. Đưa vào danh mục để đo được khối lượng công việc không sinh ra văn bản.

## 3. Trình tự gán mã cho một nhiệm vụ

1. Xác định **Trục** và **Nội hàm** theo `10-Sau-Truc-38-Noi-Ham.md`.
2. Tra **mã nhiệm vụ chuẩn** trong 122 mã. Không khớp → để trống, đề nghị bổ sung (xem cảnh báo trên).
3. Xác định **sản phẩm đầu ra** và **loại văn bản** tương ứng.
4. Từ sản phẩm suy ra **Nhóm** → điền `Diem_Cham` và `He_So_Quy_Doi` theo bảng thang.
5. Ghi `Do_Kho` — độ khó, mới, phức tạp, phạm vi tác động (cột của Phụ lục I).

Nếu bước 3 hoặc 4 không xác định được từ danh mục, **ghi rõ là chưa xác định** thay vì ước lượng điểm.
