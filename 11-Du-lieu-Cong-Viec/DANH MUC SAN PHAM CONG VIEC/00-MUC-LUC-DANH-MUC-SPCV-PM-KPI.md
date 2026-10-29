# Danh mục Sản phẩm/Công việc trên phần mềm KPI tỉnh — mã `N1_241`, `T4_461`

Từ **27/10/2026**, Trường đăng ký kế hoạch công tác và kê khai kết quả trên **phần mềm KPI tỉnh Quảng Ngãi**
(VNPT – ĐGCB, `https://kpi.quangngai.dcs.vn`). Phần mềm định danh sản phẩm bằng **mã riêng của nó**, nên từ
nay mã này là **mã chính** của sản phẩm trong toàn hệ KTC; mã QĐ 2119 (`1.1.KH01.04`) giữ làm **mã tham chiếu**
để tra hệ số và Trục/Nội hàm.

| Nguồn | Tệp |
|---|---|
| Danh mục gốc do phần mềm phát hành | `11-Du-lieu-Cong-Viec/27.10.2026.Import kế hoạch moi.xlsx` (sheet `SPCV` 455 mã · sheet `Mẫu import` bố cục tệp nạp) |
| Video hướng dẫn cấu hình, đăng ký kế hoạch quý | `11-Du-lieu-Cong-Viec/27.10.2026.Huong Dan Cau Hinh va Dang Ky Ke Hoach Quy Moi.mp4` — **chỉ trên Google Drive**, không đưa lên git |
| Tài liệu HDSD phần mềm (8 PDF + slide tập huấn) | `91-Tai-Lieu-Thiet-Ke/TL HDSD Phan mem KPI/` |
| **Dẫn xuất dùng để tra** | `danh-muc-spcv-pm-kpi.csv` (455 dòng, 12 cột) + `.nguon.txt` (sha256 hai nguồn) |
| Hệ số, Trục, Nội hàm | **QĐ 2119/QĐ-CĐKT ngày 28/9/2026** — `KTC-Database/02-KTC-Regulations/02-01-…/PL-2119-QD-CDKT_…xlsx` (chỉ đọc) |

Sinh lại dẫn xuất: `python 29-Cong-Cu/trich_danh_muc_pm_kpi.py`

## Quy tắc mã

Phần mềm sinh mã theo quy tắc **"Mã nhóm SPCV_số thứ tự tăng dần"**, trong đó *Nhóm SPCV* là một trường danh
mục do quản trị đơn vị khai báo (HDSD VNPT–ĐGCB v2.0, mục IV.2.4.2.2, tr. 35). Mã **không sửa được sau khi tạo**.

| Tiền tố | Nghĩa | Số mã | Hệ số |
|---|---|---|---|
| `N1`–`N5` | **Nhóm 1–5 theo QĐ 2119** | 220 · 179 · 11 · 4 · 3 = 417 | Lấy đúng theo từng sản phẩm trong PL-2119 |
| `T1`–`T6` | Sáu nhóm Trường khai thêm cho sản phẩm **chưa có trong QĐ 2119** | 8 · 2 · 3 · 15 · 9 · 1 = 38 | **THIEU_DU_LIEU** — chưa có văn bản |

**Đối chiếu ngày 27/10/2026**: 416/455 mã khớp tên với PL-2119, và **nhóm khớp 100% — 0 mã lệch** (`N3_34` ↔
Nhóm 3, `N5_10` ↔ Nhóm 5…). Hai sản phẩm được đổi tên khi đưa lên phần mềm, cột `ghi_chu` đánh dấu:

| Mã mới | Tên trên phần mềm | Mã QĐ 2119 | Tên trong PL-2119 |
|---|---|---|---|
| `N2_319` | Nghị quyết Hội nghị viên chức và người lao động | `4.5.NQ01.03` | Nghị quyết Hội nghị CBVC |
| `N2_340` | Đề xuất, quyết định công nhận **HSSV** được hưởng chế độ, chính sách | `5.2.QD01.08` | …công nhận **SV**… |

## 39 mã chưa có hệ số — không tự đặt

38 mã `T1`–`T6` và `N1_460` (*Báo cáo năm thực hiện quy chế dân chủ ở cơ sở*) **không có trong PL-2119**, nên
cột `he_so` để trống và `ghi_chu` ghi `THIEU_DU_LIEU`. Không được suy hệ số từ tiền tố (CLAUDE.md — hệ số lấy
đúng theo từng sản phẩm).

Nội dung 6 nhóm `T` khớp rất sát **6 Trục TB 817** — T1 đào tạo · T2 thể chế, công khai · T3 chuyển đổi số, AI ·
T4 xây dựng Đảng, tổ chức cán bộ, đoàn thể · T5 văn hóa, an sinh, HSSV, cơ sở vật chất · T6 đối ngoại, hội nhập.
Đây là **giả thuyết có bằng chứng nội dung, chưa có văn bản xác nhận**: cột `truc` của các dòng `T` ghi theo giả
thuyết này để tra cứu, không dùng làm căn cứ. **Việc cần làm**: đề nghị P-TCCB xác nhận nghĩa nhóm `T` và bổ
sung 39 sản phẩm vào lần rà soát danh mục hằng năm (Điều 3 QĐ 2119, Phòng TCCB&CTHSSV tổng hợp).

## Cấu trúc `danh-muc-spcv-pm-kpi.csv`

`ma_spcv` · `ten_spcv` · `nhom_pm` · `ma_qd2119` · `nhom_qd2119` · `he_so` · `truc` · `noi_ham` · `ma_vb` ·
`san_pham_minh_chung` · `mo_ta` · `ghi_chu`

## Xuất tệp nạp lên phần mềm

```bash
# bảng trống để đơn vị tự điền số lượng (giống hệt mẫu phát hành)
python 29-Cong-Cu/xuat_mau_import_kpi.py --don-vi "Khoa các Khoa học cơ bản" --ra <tệp.xlsx>

# từ kế hoạch đã có: CSV 3 cột ma_spcv,so_luong,mo_ta — in kèm tổng điểm quy đổi
python 29-Cong-Cu/xuat_mau_import_kpi.py --don-vi "Phòng TH-HC&QT" --ke-hoach kh.csv --ra <tệp.xlsx>

# lọc khi xuất bảng trống
python 29-Cong-Cu/xuat_mau_import_kpi.py --don-vi "…" --nhom N1,N2 --truc 1,3 --ra <tệp.xlsx>
```

Bố cục tệp do phần mềm quy định, **không được đổi số cột**: dòng 1 đơn vị áp dụng · dòng 2 tiêu đề · dòng 3–6
ghi chú · dòng 8–9 tiêu đề cột gộp (`TT(*) | Sản phẩm/công việc(*) | Số lượng giao(*) | Mô tả`) · dòng 10 trở đi
là dữ liệu; cột B phải ghi **`<mã> - <tên>`** đúng từng ký tự. Dữ liệu dòng 1–9 không được nạp vào hệ thống.
Công cụ đã kiểm: tệp sinh ra trùng khít mẫu phát hành (0 ô lệch, merge trùng).

Mã không có trong danh mục → công cụ **dừng**, không tự đặt mã.

Nạp lên: *Quản lý công việc / Cá nhân CBCCVC / Đăng ký kế hoạch công tác* → **[Thêm từ file]**.
Quản trị đơn vị nạp cả bảng danh mục: *Quản lý công việc / Danh mục sản phẩm / Import sản phẩm/công việc*.

## Chu trình trên phần mềm (đối chiếu hệ KTC)

| Bước phần mềm | Tương ứng trong hệ KTC |
|---|---|
| Đăng ký kế hoạch công tác (đầu kỳ) → cấp trên phê duyệt | `ke-hoach`, `kpi-lap-ke-hoach` — kế hoạch quý, chỉ tiêu KPI |
| Quản lý công việc cá nhân (trong kỳ): tiến độ %, minh chứng | `theo-doi-cv` |
| Theo dõi, thực hiện công việc hàng tháng → [Tính điểm] | `bao-cao`, Master Task Register |
| Tự đánh giá theo KPI → xếp loại | `kpi-tu-danh-gia`, QĐ 1923 · QĐ 2164 |

Phần mềm tự chấm **Điểm số lượng, tiến độ, chất lượng**; hệ số quy đổi lấy từ danh mục sản phẩm đã khai. Mỗi
chu kỳ mỗi người **chỉ một phiếu**. Công việc đồng bộ tự động từ iOffice **không sửa, không xóa** được.
