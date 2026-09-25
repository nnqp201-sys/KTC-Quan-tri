# LỆNH SỬA LỖI — Sheet KPI bị che chữ và thiếu 4 cột (bộ skill KPI)

**Gửi**: Claude Code (VS Code), làm việc trong thư mục dự án `KTC-Quan-tri`
**Người giao**: Phòng TH-HC&QT, Trường Cao đẳng Kon Tum
**Ngày lập**: 25/9/2026
**Phạm vi**: sửa `28-KTC-KPI/scripts/kpi_mau.py` (và bản sao trong `28-KTC-KPI/Tu-Danh-Gia/scripts/`), thêm ca thử,
đóng gói lại hai skill `kpi-lap-ke-hoach` và `kpi-tu-danh-gia`.
**Không thuộc phạm vi**: hệ số, điểm, quy tắc chấm (không đổi số nào); nội dung biểu mẫu chính thức trong `assets/`.

## 0. Đọc trước

1. `CLAUDE.md`, `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`, `92-Kinh-Nghiem/05-Known-Issues/Pending.md`.
2. `28-KTC-KPI/references/Known-Issues-Bieu-Mau.md` (đã có mục #10–#12 về dòng ví dụ và ẩn dòng; lỗi dưới đây là lỗi mới,
   ghi tiếp thành #13 và #14).
3. `.claude/rules/22-kiem-thu-va-dong-goi.md` — chạy `python 29-Cong-Cu/kiem_tra_he_thong.py` trước và sau khi sửa.

## 1. Triệu chứng người dùng thấy (tệp `KH-KPI-Q3-2026_*.xlsx` và `TDG-KPI-Q3-2026_*.xlsx`, sheet **KPI**)

| # | Triệu chứng | Nơi thấy |
|---|---|---|
| L1 | **Dòng mất chữ**: cột "Nội dung công việc" bị cắt, chỉ thấy 1–2 dòng chữ, dòng sau bị che; dòng nhiệm vụ dài nhất bị che nặng nhất | Sheet KPI, cột B, mọi đầu việc có nội dung dài |
| L2 | **Thiếu thông tin**: 4 cột đầu của khối "Nhiệm vụ đề ra kế hoạch" để trống — *Người trực tiếp chỉ đạo, Người phối hợp, Đơn vị tham mưu, Sản phẩm dự kiến hoàn thành* | Sheet KPI, cột C, D, E, F |
| L3 | Các ô "thực tế hoàn thành/KPI" hiện 0,00 hoặc trống khi chỉ có tệp kế hoạch | Sheet KPI, cột L–Q. **Không phải lỗi**: số thực tế chỉ có sau khi chạy `kpi_danh_gia.py danh-gia`. Chỉ cần ghi rõ trong đầu ra của `kpi_mau.py` |

Đối chiếu: tệp kế hoạch KPI quý của một Phó Trưởng phòng do người dùng tự điền (đơn vị đã dùng đúng mẫu) có đủ cột
C–F ở từng dòng và cột B là công thức `='Ke Hoach'!B<dòng>`.

## 2. Nguyên nhân gốc (đã đọc mã, không suy đoán)

**L1.** `kpi_mau.py`, hàm `xuong_dong` (khoảng dòng 240–259) bỏ qua mọi ô có giá trị bắt đầu bằng `=`:
`if c.value in (None, "") or str(c.value).startswith("="): continue`. Cột B của sheet KPI là **công thức** trỏ về sheet
Ke Hoach, nên chiều dài chữ thật của nội dung **không bao giờ được tính** vào chiều cao dòng. Ngoài ra:
- `rong = sh.column_dimensions[col].width or 10` chỉ đọc khóa cột đơn lẻ. Openpyxl gộp cột liền nhau thành một khóa
  (`min`–`max`), nên cột nằm giữa nhóm nhận `None` và bị coi là rộng 10 — sai;
- hệ số `1.1 * 12 / co` tính số ký tự mỗi dòng theo phông chữ, nhưng không cộng phần dư: chữ tiếng Việt có dấu nên
  thực tế xuống dòng sớm hơn ước tính → dòng thấp hơn cần thiết.

**L2.** `ghi_ke_hoach` (dòng 276–345) đầu tiên xóa ô ví dụ ở sheet KPI (`xoa_thuc_te`, dòng cột C–F cũng bị xóa với mẫu nhóm
"hành chính" vì mẫu điền sẵn), rồi ghi đầu việc chỉ vào sheet **Ke Hoach** (cột B–J). Cấu trúc JSON `dau_viec` không có
trường cho *người chỉ đạo, người phối hợp, đơn vị tham mưu*, và mã không ghi gì vào KPI!C–F. Kết quả: 4 cột trống vĩnh viễn.
Cột F ở mẫu gốc là công thức `='Ke Hoach'!E<dòng>` (sản phẩm), nhưng bị xóa cùng đợt và không được dựng lại.

## 3. Việc phải làm

### 3.1. Sửa L2 (thiếu cột) — làm trước

1. Thêm ba trường **tùy chọn** vào cấu trúc `dau_viec`: `nguoi_chi_dao`, `nguoi_phoi_hop`, `don_vi_tham_muu`
   (cập nhật docstring `ghi_ke_hoach` và mô tả JSON trong `SKILL.md`, mục 5 bước 4).
2. Trong `ghi_ke_hoach`, với mỗi đầu việc ghi vào sheet KPI, dòng `kpi_dong[r]`:
   - `KPI!C` ← `nguoi_chi_dao`, mặc định = `cap_trinh` (Ke Hoach!C) nếu không truyền;
   - `KPI!D` ← `nguoi_phoi_hop`; `KPI!E` ← `don_vi_tham_muu`, mặc định = đơn vị công tác trong `ca_nhan.don_vi`;
   - `KPI!F` ← công thức `='Ke Hoach'!E<dòng>` (khôi phục công thức mẫu, không ghi giá trị cứng).
   **Không tự bịa** người phối hợp: không truyền thì để trống nhưng phải **cảnh báo** `KH17` (mã mới): "Dòng <n> thiếu
   người phối hợp — cần người dùng bổ sung" — trừ khi nhóm vị trí là `ho-tro` (mẫu không có cột này).
3. Bật `wrap_text` và căn `vertical="top"` cho C–F như cột B.
4. `scripts/validate_plan.py`: thêm phép kiểm KH17 (cảnh báo) và KH18 (LỖI): ô KPI!F là công thức hợp lệ, không tham chiếu
   dòng trống của sheet Ke Hoach.

### 3.2. Sửa L1 (mất chữ)

Viết lại `xuong_dong` (hoặc thay bằng hàm `chinh_chieu_cao(ws_kh, ws_kpi)` gọi **sau khi đã ghi hết dữ liệu**):

1. **Giải công thức trỏ chéo sheet**: ô có dạng `='Ke Hoach'!<ô>` thì lấy văn bản của ô được trỏ tới để đo chiều dài.
2. **Đọc độ rộng cột đúng**: dựng bản đồ `{chỉ_số_cột: độ_rộng}` bằng cách duyệt mọi `column_dimensions`, mở rộng từng
   khóa theo `min`–`max` (không tra khóa đơn lẻ). Với ô gộp, cộng độ rộng các cột trong vùng gộp.
3. **Tính số dòng dư an toàn**: số ký tự mỗi dòng = độ rộng × 1,0 (không × 1,1), nhân số ký tự của mỗi đoạn với **1,2**
   (chữ có dấu); chiều cao = `số_dòng × cỡ_chữ × 1,3 + 6` pt; giới hạn tối đa 409 pt (giới hạn của Excel). Nếu vượt 409 pt
   thì **không im lặng cắt**: in cảnh báo `KH19` nêu số dòng và gợi ý rút gọn nội dung hoặc nới rộng cột.
4. Áp cho **cả hai sheet** Ke Hoach và KPI, chỉ với dòng nhìn thấy (bỏ dòng ẩn), và **lấy cực đại của mọi cột** trong dòng
   (nội dung, cột người phối hợp, cột minh chứng, cột ghi chú).
5. Sheet Ke Hoach: cột Ghi chú (J) của mẫu rất hẹp (~6–7 ký tự) nên ghi chú dài làm dòng cao bất thường. Nới độ rộng
   cột này lên khoảng 24–26 (chỉ ở bản sao đầu ra, không đụng `assets/`).
6. `kpi_danh_gia.py`: sau khi ghi số thực tế vào sheet KPI (cột K, N, P, S…) phải gọi lại `chinh_chieu_cao` cho cả hai
   sheet, vì nội dung cột K (sản phẩm thực tế, danh sách số ký hiệu văn bản) và cột S (nguồn minh chứng) làm dòng cao hơn.
   Nếu tệp ra bị Excel khóa (`PermissionError`), báo rõ "tệp đang mở trong Excel, hãy đóng hoặc đặt tên mới" thay vì để
   lộ traceback.

### 3.3. Ghi rõ L3

Cuối đầu ra của `kpi_mau.py`, thêm một dòng: "Số thực tế, KPI, điểm: chưa có — sinh sau khi chạy kpi_danh_gia.py danh-gia".

## 4. Ca thử (viết **trước** khi sửa, xác nhận thất bại, rồi mới sửa — theo quy tắc thêm phép kiểm phải có ca thử ngược)

Thêm vào `92-Kinh-Nghiem/02-Regression/Cases/` tệp `test_kpi_trinh_bay.py`, dùng **dữ liệu giả** (không dùng họ tên, số
liệu của người thật; ghi `#riêng` khi cần dán số liệu thật để thử):

| Ca | Nội dung | Kỳ vọng |
|---|---|---|
| T1 | Đầu việc có `noi_dung` 300 ký tự ở nhóm `hanh-chinh` | Chiều cao dòng KPI!B ≥ số dòng ước tính (300 × 1,2 / rộng cột) × cỡ chữ × 1,3; **thử ngược**: bản cũ cho chiều cao thấp hơn |
| T2 | Cột nằm giữa một nhóm `column_dimensions` gộp (min–max) | Độ rộng đọc ra bằng độ rộng của nhóm, không phải 10 |
| T3 | Đầu việc truyền đủ `nguoi_chi_dao`, `nguoi_phoi_hop`, `don_vi_tham_muu` | KPI!C, D, E có giá trị; KPI!F là công thức `='Ke Hoach'!E<dòng>` |
| T4 | Đầu việc không truyền người phối hợp, nhóm `hanh-chinh` | KPI!D trống **và** có cảnh báo KH17; nhóm `ho-tro` thì không cảnh báo |
| T5 | Nội dung quá dài khiến chiều cao > 409 pt | Có cảnh báo KH19, không cắt im lặng |
| T6 | Chạy `kpi_danh_gia.py danh-gia` xong | Chiều cao dòng KPI đủ cho cột K và S (đo lại sau khi ghi số thực tế) |
| T7 | Ghi ra tệp đang bị khóa (giả lập bằng mở tệp ở chế độ độc quyền) | Thông báo tiếng Việt rõ ràng, mã thoát khác 0, không có traceback |
| T8 | Chạy cả 6 nhóm vị trí | Cả 6 nhóm: cột C–F đúng theo cấu trúc mẫu của nhóm đó (nhóm không có cột thì bỏ qua) |

## 5. Tiêu chí nghiệm thu

- [ ] `python 29-Cong-Cu/kiem_tra_he_thong.py` mã thoát 0, cả trước và sau khi đóng gói.
- [ ] `test_kpi_trinh_bay.py` và các ca cũ (`test_kpi_calc.py`, `test_kpi_danh_gia.py`, `test_validate_plan.py`) đều qua.
- [ ] Tệp ra đo bằng `29-Cong-Cu/kiem_the_thuc.py`: không còn lỗi Mức 1–3.
- [ ] Mở tệp mẫu đầu ra trong Excel: không dòng nào bị che chữ; nội dung ở cả cột B (KPI) đọc được đủ; cột C–F có giá trị.
  (Claude Code không tự kiểm được bằng mắt: ghi `HIEN_THI_CHUA_KIEM_CHUNG_BANG_MAT` trong báo cáo và nhờ người dùng chụp lại
  màn hình một tệp thật để xác nhận. Nếu có LibreOffice, xuất PDF để kiểm và đính kèm.)
- [ ] Không có số nào trong hệ số, điểm, tổng, mức xếp loại thay đổi so với trước khi sửa (so sánh trên tệp thử cố định).
- [ ] `assets/` không đổi byte nào (so `git diff --stat 28-KTC-KPI/assets`).
- [ ] Đóng gói lại `ktc-kpi-lap-ke-hoach-v1.2.skill` và `ktc-kpi-tu-danh-gia-v1.1.skill`, cập nhật dòng phiên bản trong
  `SKILL.md` của cả hai, dựng lại plugin bằng `29-Cong-Cu/dong_goi_plugin.py`, ghi Decision Log `DL-20260925-00x` và
  Process Memory, cập nhật `Known-Issues-Bieu-Mau.md` (#13 L1, #14 L2), cập nhật `MEMORY-INDEX.md` dòng phiên bản.

## 6. Ràng buộc

1. Không sửa biểu mẫu chính thức trong `assets/`; mọi chỉnh sửa áp lên **bản sao** đầu ra.
2. Không đưa họ tên, điểm, nhận xét của cá nhân vào mã, ca thử, tài liệu hay nhật ký. Dữ liệu KPI cá nhân chỉ ở
   `30-Ket-Qua/<ngày>/KPI-ca-nhan/` (đã loại khỏi git).
3. Không tự đổi cách tính điểm, hệ số, ngưỡng xếp loại; nếu thấy nghi ngờ thì ghi vào Câu hỏi mở, không sửa.
4. Chỉ sửa đúng phạm vi ở đầu lệnh. Việc khác phát hiện thêm (ví dụ khổ in ngang TX04) ghi thành đề xuất, không làm chung.
5. Báo cáo cuối: nêu tệp đã sửa, kết quả từng ca thử, những gì **chưa kiểm chứng** (đặc biệt phần hiển thị trong Excel).

## 7. Dữ liệu thử thật (người dùng sẽ cung cấp riêng khi cần)

Sau khi sửa xong, người dùng chạy lại lệnh dựng kế hoạch và tự đánh giá quý III cho một chuyên viên và chụp màn hình sheet
KPI để đối chiếu. Đầu ra kỳ vọng: 12 đầu việc, 4 cột C–F đủ thông tin, mọi dòng đọc được nội dung đầy đủ, tổng điểm không
đổi so với lần chạy trước khi sửa.
