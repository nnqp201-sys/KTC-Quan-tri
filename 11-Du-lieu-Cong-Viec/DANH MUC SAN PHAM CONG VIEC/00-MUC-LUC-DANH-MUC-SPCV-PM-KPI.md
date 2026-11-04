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

## Quy tắc mã — hai trường phân loại độc lập

Phần mềm có **hai trường khác nhau**, đừng lẫn (HDSD VNPT–ĐGCB v2.0):

| Trường | Nghĩa | Giá trị của Trường |
|---|---|---|
| **Nhóm SPCV** | *"Phân loại **mức độ phức tạp** của công việc thông qua **điểm tối đa** tương ứng với từng nhóm"* — `N1`=100, `N2`=200, `N3`=300, `N4`=400, `N5`=500 điểm (tr. 30–32) | `N1`–`N5` = **Nhóm 1–5 của QĐ 2119** |
| **Lĩnh vực SPCV** | Lĩnh vực chuyên môn, trường bắt buộc riêng khi tạo sản phẩm (tr. 35) | `T1`–`T6` = **Trục (1)–(6)** theo TB 817 |

Mã sản phẩm sinh theo **"Mã nhóm SPCV_số thứ tự tăng dần"** và **không sửa được sau khi tạo** (tr. 35).

> **Bằng chứng `T` = Trục** (không phải Nhóm): video hướng dẫn 27/10/2026, phút ~2:16 — hộp thoại *Thêm: Danh
> sách công việc* hiển thị sản phẩm `N2_219 "Giảng dạy theo kế hoạch"` với cột **Lĩnh vực SPCV = "T1 - Trục (1)
> THỰC HIỆN MỤC TIÊU PHÁT TRIỂN KINH TẾ - XÃ HỘI VÀ NHIỆM VỤ CHÍNH TRỊ ĐƯỢC GIAO"**. Ảnh lưu
> `91-Tai-Lieu-Thiet-Ke/TL HDSD Phan mem KPI/Bang-chung_Linh-vuc-SPCV-la-Truc_video-27102026-phut-2-16.png`.

| Tiền tố | Số mã | Hệ số |
|---|---|---|
| `N1`–`N5` (Nhóm 1–5) | 220 · 179 · 11 · 4 · 3 = 417 | Lấy đúng theo từng sản phẩm trong PL-2119 |
| `T1`–`T6` (Trục 1–6) | 8 · 2 · 3 · 15 · 9 · 1 = 38 | **THIEU_DU_LIEU** — sản phẩm **chưa được gán Nhóm** nên chưa có hệ số |

**Hệ số trên phần mềm = hệ số QĐ 2119 theo từng sản phẩm** — kiểm chứng bằng số thật trong video (phút ~2:32):
`N2_219` hệ số 1,2 → 50 × 1,2 = **60,00**; `N2_220` hệ số 1,5 → 5 × 1,5 = **7,50**; tổng **67,50** đúng như phần
mềm hiển thị. Ảnh: `…/Bang-chung_He-so-QD2119-khop-quy-doi_video-27102026-phut-2-32.png`.

**Đối chiếu ngày 27/10/2026**: 416/455 mã khớp tên với PL-2119, và **nhóm khớp 100% — 0 mã lệch** (`N3_34` ↔
Nhóm 3, `N5_10` ↔ Nhóm 5…). Hai sản phẩm được đổi tên khi đưa lên phần mềm, cột `ghi_chu` đánh dấu:

| Mã mới | Tên trên phần mềm | Mã QĐ 2119 | Tên trong PL-2119 |
|---|---|---|---|
| `N2_319` | Nghị quyết Hội nghị viên chức và người lao động | `4.5.NQ01.03` | Nghị quyết Hội nghị CBVC |
| `N2_340` | Đề xuất, quyết định công nhận **HSSV** được hưởng chế độ, chính sách | `5.2.QD01.08` | …công nhận **SV**… |

## 39 mã chưa có hệ số — không tự đặt

| Nhóm mã | Vì sao chưa có hệ số |
|---|---|
| 38 mã `T1`–`T6` | **Chưa được gán Nhóm SPCV**. Hệ số gắn theo Nhóm/sản phẩm, nên khi chưa phân nhóm thì chưa có hệ số; mã phải đặt theo Lĩnh vực (Trục) thay cho Nhóm. **Trục của các mã này là chắc chắn** (đọc thẳng từ mã), chỉ thiếu Nhóm và hệ số |
| `N1_460` — *Báo cáo năm thực hiện quy chế dân chủ ở cơ sở* | Thêm sau QĐ 2119 (mã cuối cùng của N1, ngay sau `N1_459` là sản phẩm cuối của phụ lục). Đã **thuộc Nhóm 1** → hệ số nằm trong {0,3; 0,5; 1,0}; sản phẩm cùng họ *Báo cáo 6 tháng thực hiện quy chế dân chủ ở cơ sở* (`4.5.BC01.01`, Trục 4) có hệ số **1,0** |

Cả 39 sản phẩm **không có trong PL-2119 lẫn bảng dự thảo 371** (đối chiếu 0/39) — tức là phát sinh sau
28/9/2026, được thêm thẳng trên phần mềm khi đơn vị, viên chức đăng ký kế hoạch. Không suy hệ số từ tiền tố,
không gán hệ số theo sản phẩm "cùng họ" (CLAUDE.md — hệ số lấy đúng theo từng sản phẩm).

**Việc cần làm:** đề nghị Phòng TCCB&CTHSSV (a) gán Nhóm cho 38 mã `T`, (b) xác nhận hệ số cho cả 39 sản phẩm,
(c) đưa vào lần rà soát, bổ sung danh mục theo **Điều 3 QĐ 2119** (P-TCCB tổng hợp, Hiệu trưởng quyết định).

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
