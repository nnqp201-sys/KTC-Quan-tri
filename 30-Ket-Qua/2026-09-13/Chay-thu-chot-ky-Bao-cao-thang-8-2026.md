# Chạy thử: chốt kỳ và dựng báo cáo tháng 8/2026

**Ngày chạy:** 13/9/2026 · **Tác vụ:** (d) Chốt kỳ và dựng báo cáo + (c) Đối chiếu ba hệ
**Gói dùng:** `ktc-quan-tri.skill` v1.0 · **Nguồn:** `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/`

> **Đây là bản chạy thử để kiểm chứng quy trình, không phải báo cáo trình ký.** Mọi kết quả đối chiếu dưới
> đây là **đối chiếu gần đúng** — Phụ lục Ia/Ib chưa có cột `Task_ID` nên không nối 1-1 được.

---

## Bước 0 — Xác định trước khi xử lý

| Mục | Kết quả |
|---|---|
| Tác vụ | (d) chốt kỳ và dựng báo cáo, kèm (c) đối chiếu |
| Kỳ | Tháng 8/2026 (báo cáo kết quả), kèm tháng 9/2026 (kế hoạch) |
| Dữ liệu thật | **Có** — 40 tệp, 14 thư mục đơn vị. Không phải chạy trên dữ liệu mẫu |
| Bộ nhớ vận hành | **Chưa có** — `03-Nhat-Ky-Van-Hanh/` mới có thiết kế, chưa có mục nào. Theo quy tắc hai lớp: chạy tiếp, ghi cảnh báo |

---

## Phần I — Tiếp nhận và nhận dạng

**328 nhiệm vụ thực** trong báo cáo tháng 8, từ 13 thư mục đơn vị. Con số thô là 428 dòng; **100 dòng là
tiêu đề nhóm** (`Các nhiệm vụ theo kế hoạch`, `Trục (1)`–`Trục (6)`, `Các nhiệm vụ đột xuất, phát sinh`),
không phải nhiệm vụ. Sai lệch ±4 tùy cách nhận dạng dòng tiêu đề.

| Mã | Thư mục | NV thực t8 | KH t9 | Ghi chú |
|---|---|---|---|---|
| P-QLKH | Phong-QLKHCN-HTPT | 59 | 23 | |
| K-DTSHLX | Khoa-DT-SHLX | 36 | 38 | |
| P-TCCB | Phong-TCCB-CTHHSV | 33 | **0** | ⚠️ xem lỗi 1 |
| K-KHCB | Khoa-CKHCB | 32 | 22 | ⚠️ thiếu Trục 2, 5 |
| K-KTNL | Khoa-KT-NL | 30 | 22 | ⚠️ thiếu Trục 2, 5 |
| K-KTCN | Khoa-KT-CN | 26 | 35 | ⚠️ xem lỗi 3 |
| DT-CDCS | Cong-Doan | 20 | 25 | |
| P-QLDT | Phong-QLDT-BDCL | 19 | 16 | |
| P-THHC | Phong-THHCQT | 19 | 29 | ⚠️ xem lỗi 2 |
| P-TCKT | Phong-TC-KT | 17 | 23 | |
| K-YDUOC | Khoa-Y-Duoc | 16 | 21 | |
| DT-DTN | Doan-TN | 14 | 20 | |
| K-SUPH | Khoa-Su-Pham | **7** | 12 | báo cáo gần như rỗng |
| | **Tổng** | **328** | **286** | |

### Độ phủ thực tế: 10/11 đơn vị chuẩn, không phải 11

Thư mục `Phong-THHCQT` chứa tệp `BAN TT.xlsx`, bên trong ghi rõ **"ĐƠN VỊ: BAN TRUYỀN THÔNG"**. Đây là báo
cáo của Ban Truyền thông, không phải của Phòng Tổng hợp - Hành chính và Quản trị.

**Hệ quả: Phòng TH-HC&QT chưa có báo cáo tháng 8.** Đây là đơn vị nộp nhiều nhiệm vụ gốc nhất trong danh
mục nhiệm vụ chuẩn (402/1.358 dòng), nên khoảng trống này đáng kể.

Đồng thời **Ban Truyền thông là đơn vị thứ 12**, không có trong bảng 11 mã đơn vị chuẩn — cần bổ sung mã
hoặc xác định nó trực thuộc đơn vị nào.

---

## Phần II — Bốn lỗi thể thức của đơn vị

### Lỗi 1 — Phòng TCCB: nộp báo cáo tháng 9 thay vì kế hoạch tháng 9

Tệp `KH t9. P TCCB.xlsx` — tên tệp là kế hoạch tháng 9, nhưng bên trong dùng **Phụ lục IIb (mẫu báo cáo
kết quả)** với tiêu đề *"BÁO CÁO kết quả thực hiện công tác tháng 9 năm 2026"*.

Tháng 9/2026 chưa kết thúc tại thời điểm chạy, nên không thể có kết quả thực hiện. Đơn vị dùng nhầm mẫu:
đáng lẽ Phụ lục Ib (kế hoạch tháng). **Phòng TCCB hiện chưa có kế hoạch tháng 9 hợp lệ.**

### Lỗi 2 — Ban Truyền thông đặt nhầm thư mục

Đã nêu ở Phần I.

### Lỗi 3 — Khoa KT-CN: sai cấu trúc cột

`KTCN.xlsx` có tiêu đề *"BÁO CÁO kết quả thực hiện"* nhưng hàng tiêu đề cột lại theo **mẫu kế hoạch**: cột
(8) là `Thời gian hoàn thành` thay vì `Điểm chấm công việc`. Toàn bộ 26 nhiệm vụ vì thế **không có điểm
chấm ở đúng vị trí**, và 26 dòng cho kết quả sai khi kiểm tra công thức quy đổi.

Đây là lỗi cấu trúc, không phải lỗi nhập liệu — không sửa được bằng cách điền thêm, phải nhập lại theo
đúng Phụ lục IIb.

### Lỗi 4 — Khoa Sư phạm: tiêu đề tự chế

`SP.xlsx` ghi *"Phụ lục KẾT QUẢ THỰC HIỆN CÔNG TÁC THÁNG 8 NĂM 2026"* thay vì tiêu đề chuẩn của Phụ lục
IIb. Dữ liệu vẫn đọc được, nhưng tệp không khớp mẫu và chỉ có **7 nhiệm vụ** — thấp bất thường so với
trung bình 25 nhiệm vụ/đơn vị.

### Ngoài ra

- **`K-KHCB` và `K-KTNL` thiếu hẳn mục Trục 2 và Trục 5** trong báo cáo — 4/6 Trục có mặt.
- **5 tệp còn để nguyên sheet mẫu trống** (`Mẫu BC QUÝ`, `Mẫu KH Quý`) với dòng `ĐƠN VỊ:…......` chưa xóa:
  K-DTSHLX (2), K-SUPH, K-YDUOC (2), P-TCCB.

---

## Phần III — Kiểm tra số liệu

### Đạt: công thức hệ số quy đổi

`Hệ số quy đổi = Điểm chấm × 1%` — **đúng trên 300/301 dòng** có đủ hai giá trị. Dữ liệu nhất quán nội bộ.

**Một lỗi tính thật:** `P-QLKH` dòng 66 *"Đề xuất chủ đề Hội thảo khoa học quốc tế…"* — KPI quy đổi ghi
`1`, tính đúng phải là `1.5`.

### Phát hiện quan trọng: thang điểm thực tế khác thang trong danh mục dự thảo

| | Giá trị |
|---|---|
| Thang trong `Du thao_Danh_muc_SP...xlsx` (dự thảo lần 4) | 50 · 120 · 250 · 350 · 450 |
| **Điểm chấm thực tế các đơn vị đang dùng** | **30 · 100 · 120 · 150 · 200** |

Phân bố thực tế: điểm 100 (170 dòng) · 120 (65) · 150 (40) · 200 (20) · 30 (6). Chỉ giá trị **120** trùng
nhau giữa hai thang.

Đây **không phải lỗi của đơn vị**. Cột "Điểm chấm công việc" trên Phụ lục I là ô số tự do, và hệ số luôn
được tính đúng bằng điểm×1%. Nghĩa là **bảng 5 nhóm trong danh mục sản phẩm là bảng gợi ý khi xây dựng
danh mục, không phải danh sách giá trị hợp lệ để kiểm tra dữ liệu vận hành.**

Gói skill v1.0 đang hiểu sai điểm này — xem Phần V.

### Cột "Đơn vị chủ trì" đang được điền bằng bộ phận nội bộ

60 dòng ở 4 đơn vị ghi đơn vị chủ trì bằng tên bộ phận hoặc nhóm người, không phải đơn vị cấp Trường:

`Ban Truyền thông` (19×) · `Nhà giáo` (6×) · `Các bộ môn và nhà giáo` (4×) · `Bộ môn CK&XD` (4×) ·
`Giáo vụ khoa` (3×) · `Chi bộ khoa` (2×) · `Các lớp sinh viên` (2×)…

Bảng mã đơn vị hiện chỉ có một cấp (11 đơn vị thuộc Trường). Thực tế cần **cấp thứ hai** — bộ môn, tổ,
ban, chức danh — nếu muốn nối dữ liệu tự động.

---

## Phần IV — Đối chiếu ngược với kế hoạch (tìm nhiệm vụ bỏ sót)

Nguồn: `Ke_hoach_cong_tac_Quy_III_2026_dieu_chinh_bo_sung_CHUAN.xlsx` — 55 nhiệm vụ có mã, trong đó
**19 nhiệm vụ đến hạn tháng 8**.

Duyệt ngược từ kế hoạch sang báo cáo, so khớp tên nhiệm vụ ở ngưỡng 0,60:

- **Tìm thấy: 12/19**
- **Không tìm thấy: 7/19** — nghi bỏ sót

| Mã | Đơn vị chủ trì | Nhiệm vụ | Khớp cao nhất |
|---|---|---|---|
| 5.6 | BCH CĐCS | Triển khai Kế hoạch tham gia Giải bóng chuyền nam, nữ công… | 0,59 |
| 2.8 | Phòng TCCB&CTHSSV | Ban hành Quy định đánh giá, xếp loại chất lượng viên chức… | 0,56 |
| 4.11 | Phòng TH-HC&QT; BCH CĐ | Xây dựng Kế hoạch liên tịch triển khai phong trào xanh hoá… | 0,56 |
| 3.3 | Khoa ĐT&SHLX | Xây dựng phần mềm kiểm tra mô phỏng tình huống giao thông | 0,55 |
| 4.6 | BPVPĐU | Công nhận mô hình, điển hình "Dân vận khéo" cấp cơ sở | 0,53 |
| 1.23 | Phòng TCCB&CTHSSV | Kế hoạch tổ chức tọa đàm về đánh giá viên chức lãnh đạo… | 0,43 |
| 4.3 | Các chi bộ trực thuộc | Tham mưu xây dựng/bổ sung phương hướng, nhiệm vụ… | 0,38 |

### Đọc kết quả này cho đúng

**Nhiệm vụ 2.8 gần như chắc chắn đã hoàn thành.** Đó chính là Quyết định 1923/QĐ-CĐKT ngày 30/8/2026 ban
hành Quy chế đánh giá, xếp loại chất lượng gắn KPI — văn bản đang nằm trong `KTC-Database`. Nhiệm vụ đã
làm xong nhưng **không xuất hiện trong báo cáo tháng 8 của Phòng TCCB**.

Đây là minh chứng sống cho hai điều:

1. **"Không tìm thấy" ≠ "chưa thực hiện".** Bảy dòng trên là *nghi vấn cần đối chiếu*, tuyệt đối không được
   trình bày như danh sách đơn vị chưa hoàn thành nhiệm vụ.
2. **Đối chiếu theo tên nhiệm vụ không đủ tin cậy.** Chừng nào Phụ lục Ia/Ib chưa có cột `Task_ID`, mọi kết
   quả đối chiếu đều phải kèm cảnh báo này.

Ba trong bảy nhiệm vụ nghi bỏ sót thuộc **Phòng TCCB** và **Phòng TH-HC&QT** — hai đơn vị có vấn đề về hồ
sơ nộp (lỗi 1 và lỗi 2). Nhiều khả năng đây là hệ quả của việc nộp thiếu/nhầm, không phải không làm việc.

---

## Phần V — Ba điều cần sửa trong gói skill v1.0

Chạy thử này làm lộ ra ba chỗ gói skill hiểu sai hoặc thiếu:

| # | Vấn đề | Sửa ở đâu |
|---|---|---|
| 1 | **Thang điểm 50/120/250/350/450 bị mô tả như giá trị hợp lệ.** Thực tế vận hành dùng 30/100/120/150/200; đó là bảng gợi ý xây danh mục, không phải ràng buộc kiểm tra | `references/13-Danh-Muc-Nhiem-Vu-Va-San-Pham.md` |
| 2 | **Thiếu quy tắc loại dòng tiêu đề nhóm.** Mẫu Phụ lục IIb có ~8 dòng tiêu đề (`Trục (1)`–`Trục (6)`, `Các nhiệm vụ theo kế hoạch`, `Các nhiệm vụ đột xuất`). Không loại thì đếm thừa 30% | `references/24-Chot-Ky-Va-Bao-Cao.md` |
| 3 | **Bảng mã đơn vị chỉ có một cấp.** Thực tế cột "Đơn vị chủ trì" được điền bằng bộ môn, ban, chức danh. Cần cấp thứ hai và một mã cho Ban Truyền thông | `references/12-Bang-Ma-Don-Vi.md` và `01-Chuan-Chung/13-Bang-Ma-Don-Vi.md` |

Điểm được: quy tắc **"đối chiếu gần đúng phải tự khai là gần đúng"** đã phát huy đúng tác dụng — nếu không
có nó, bảy dòng ở Phần IV rất dễ bị trình bày thành kết luận về đơn vị chưa hoàn thành nhiệm vụ.

---

## Phần VI — Chưa làm được trong lần chạy này

| Việc | Vì sao |
|---|---|
| Gán `Ma_NV_Chuan` cho 328 nhiệm vụ | Danh mục 122 mã chưa phủ 6 Khoa; gán bây giờ sẽ tạo dữ liệu sai |
| Cấp `Task_ID` | Quy tắc còn dự thảo, chưa chốt |
| Tính KPI và xếp loại đơn vị | Cần đủ 4 quý theo Điều 9 Quy chế; đây mới là 1 tháng |
| Đối chiếu chính xác 1-1 | Thiếu cột `Task_ID` ở Phụ lục Ia/Ib |
| Xuất `.docx` báo cáo cấp Trường | Còn 4 lỗi thể thức chưa xử lý; chốt kỳ bây giờ là chốt trên dữ liệu lỗi |

---

## Kết luận: chưa đủ điều kiện chốt kỳ tháng 8/2026

Checklist 12 điểm không qua ở các mục 2, 3, 5, 6, 9. Bốn việc cần làm trước khi chốt lại:

1. **Phòng TH-HC&QT nộp báo cáo tháng 8** — hiện chưa có.
2. **Phòng TCCB nộp lại kế hoạch tháng 9** theo đúng Phụ lục Ib, và bổ sung các nhiệm vụ đã hoàn thành
   nhưng chưa báo cáo (ít nhất là nhiệm vụ 2.8 — QĐ 1923).
3. **Khoa KT-CN nhập lại báo cáo** theo đúng cấu trúc cột Phụ lục IIb.
4. **Khoa CKHCB và Khoa KT-NL bổ sung mục Trục 2 và Trục 5**; Khoa Sư phạm rà lại vì chỉ có 7 nhiệm vụ.

Sau đó đối chiếu lại 7 nhiệm vụ nghi bỏ sót ở Phần IV với từng đơn vị trước khi đưa bất kỳ dòng nào vào
mục "chưa hoàn thành" của báo cáo cấp Trường.
