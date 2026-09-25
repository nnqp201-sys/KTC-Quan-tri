---
name: ktc-kpi-lap-ke-hoach
description: "Lập kế hoạch công tác quý và danh mục sản phẩm/chỉ tiêu KPI CÁ NHÂN của viên chức, người lao động Trường Cao đẳng Kon Tum theo QĐ 1923/QĐ-CĐKT (Quy chế đánh giá gắn KPI), TB 1052/TB-CĐKT và mẫu Kế hoạch + KPI quý theo 6 nhóm vị trí (Trưởng/Phó phòng, khoa; Trưởng/Phó bộ môn, Phòng Khám; nhà giáo; giáo vụ khoa; viên chức hành chính; nhân viên hỗ trợ, phục vụ). Xác định Trục kết quả, mức độ, hệ số quy đổi, số lượng quy đổi, xuất tệp Excel đúng mẫu và bảng cảnh báo (thiếu sản phẩm, thời hạn, minh chứng; Trục chính dưới 40%; quản lý thiếu Trục 4; kết quả tập thể bị quy thành KPI cá nhân; dòng ví dụ chưa xóa). Dùng khi người dùng nói 'lập KPI quý', 'danh mục sản phẩm cá nhân', 'kế hoạch KPI', 'Phụ lục kèm Bản cam kết KPI', 'sửa kế hoạch KPI đã duyệt'. KHÔNG dùng để chấm điểm, tự đánh giá, xếp loại (dùng kpi-tu-danh-gia); KHÔNG dùng cho KPI đơn vị theo Trục trong báo cáo tháng/quý Phụ lục TB 736 (dùng bao-cao, theo-doi-cv); KHÔNG soạn kế hoạch công tác cấp Trường (dùng ke-hoach)."
---

# KTC-KPI — Lập kế hoạch và KPI cá nhân theo quý

## Phiên bản: v1.1 — 25/9/2026

> v1.1 (25/9/2026): xóa số thực tế ví dụ của mẫu ở sheet KPI, tự xuống dòng, ẩn dòng trống (Known-Issues #10–#12);
> KH16; nhận đúng nhóm Trưởng/Phó đơn vị từ tiêu đề mẫu. Tự đánh giá: skill `kpi-tu-danh-gia` (giai đoạn 2).
> v1.0: giai đoạn 1 theo lệnh sửa 24/9/2026 — chỉ lập kế hoạch.

## 1. Mục đích

Giúp một viên chức (hoặc Trưởng đơn vị làm cho người trong đơn vị) lập **Kế hoạch thực hiện nhiệm vụ quý và Danh mục
sản phẩm/chỉ tiêu KPI cá nhân** đúng mẫu, đúng QĐ 1923, để **trình Trưởng đơn vị phê duyệt** [QĐ 1923, Đ13.1].
Skill **không** phê duyệt, không chấm điểm, không xếp loại thay người có thẩm quyền.

## 2. Phạm vi và ngoại lệ

| Làm | Không làm (chuyển đi đâu) |
|---|---|
| Kế hoạch + KPI quý cá nhân, 6 nhóm vị trí | Chấm điểm, tự đánh giá, đề xuất xếp loại cá nhân → `kpi-tu-danh-gia`; tổng hợp xếp loại đơn vị → giai đoạn 3 (chưa có skill) |
| Điều chỉnh kế hoạch KPI đã duyệt (lập bản đề nghị điều chỉnh) | KPI đơn vị theo Trục trong báo cáo Phụ lục TB 736 → `bao-cao`, `theo-doi-cv` |
| Tra hệ số, tính số lượng quy đổi bằng script | Kế hoạch công tác cấp Trường → `ke-hoach`; văn bản hành chính → `soan-thao-vb` |

**Đọc trước khi làm:** `references/Skill-Library/19-Quy-Tac-KPI.md` (quy tắc, có dẫn Điều) ·
`references/Cau-Hoi-Mo.md` (điểm chưa có căn cứ — phải dừng hỏi) · `references/Known-Issues-Bieu-Mau.md`.

## 3. Đầu vào

Lấy theo thứ tự: tệp người dùng đính kèm trong phiên → thư mục dự án → hỏi người dùng. Thiếu thư mục không phải lý do
từ chối.

Cần có (thiếu thì hỏi, **không tự điền**):
1. **Nhóm vị trí** — một trong 6: `truong-pho-don-vi` · `bo-mon` · `nha-giao` · `giao-vu` · `hanh-chinh` · `ho-tro`
   [CV 694 mục I.2; QĐ 1923 Đ15.1b]. Không rõ thì hỏi, không đoán theo chức danh gần giống.
2. **Quý, năm** → đọc `references/quy/<YYYY>-Q<n>.yaml`. **Không có tệp quý đó → dừng, hỏi văn bản hướng dẫn quý.**
3. **Kế hoạch công tác quý của đơn vị/Trường, Danh mục sản phẩm chung của đơn vị** (nguồn phân rã [QĐ 1923, Đ12.5,
   Đ15.3a]). Không có thì ghi rõ trong đầu ra "chưa đối chiếu kế hoạch đơn vị".
4. Thông tin cá nhân: họ tên, ngày sinh, chức vụ Đảng/chính quyền/đoàn thể, đơn vị.
5. Danh sách đầu việc: nội dung, Trục, cấp trình, mức độ, sản phẩm, số lượng, thời hạn, **nguồn minh chứng**.
6. **Phương án hệ số** — xem mục 5 bước 3.

## 4. Lưu ý bảo mật

- Điểm chi tiết, nhận xét, minh chứng chỉ dành cho người có thẩm quyền và người được đánh giá [QĐ 1923, Đ23.2].
- Không đưa tên, điểm của người khác vào ví dụ, nhật ký, tệp dùng chung. Trong dự án KTC-Quan-tri, lưu tại
  `30-Ket-Qua/<YYYY-MM-DD>/KPI-ca-nhan/` (đã loại khỏi git); trên Claude.ai/Cowork, giao tệp trực tiếp cho người dùng.
- Không chép số điện thoại, tên người liên hệ trong văn bản hướng dẫn vào đầu ra.

## 5. Quy trình

1. **Xác định nhóm, quý.** Đọc tệp quý: in cho người dùng các hạn nộp của quý (có trường `ghi_chu` thì in kèm). Nếu hai
   mốc đầu quý khác nhau (Câu hỏi mở số 4), nêu **cả hai**, không chọn thay.
2. **Phân rã và xếp Trục.** Mỗi đầu việc gắn với một nhiệm vụ trong kế hoạch đơn vị; xếp vào Trục (1)–(6)
   [QĐ 1923, Đ12.1]. Kiểm ngay:
   - quản lý: có đầu việc Trục (4) [Đ12.1]; kiêm nhiệm, Đảng, đoàn thể ghi riêng, không trùng chuyên môn [Đ11.4];
   - đầu việc là kết quả chung của tập thể → tách phần cá nhân trực tiếp phụ trách [Đ4.8];
   - mỗi Trục tối đa **20 dòng** (mẫu); nhiều hơn thì gộp hoặc hỏi Phòng TCCB&CTHSSV, không chèn dòng.
3. **Chọn phương án hệ số — HỎI người dùng, không có mặc định** (Câu hỏi mở số 1). Trình bày 4 phương án kèm trạng thái:
   - `muc-do` — hệ số theo 4 mức độ 1,0/1,2/1,5/2,0: **có văn bản** (QĐ 1923, Phụ lục II);
   - `A` — hệ số sản phẩm theo Danh mục TB 1052: **dự thảo**, chưa ban hành, 204/371 dòng lệch Nhóm;
   - `AxB` — A × mức độ: **chưa có văn bản**, chờ Phòng TCCB&CTHSSV xác nhận;
   - `nhap-tay` — người dùng tự nhập, tự chịu trách nhiệm căn cứ.
   Với `A`/`AxB`: sản phẩm phải **khớp chính xác** một dòng trong `references/data/he-so-san-pham-TB1052.csv` (theo STT
   hoặc tên). Liệt kê ứng viên cho người dùng chọn: `python scripts/kpi_calc.py tim --tu-khoa "<từ khóa>"`; ghi STT đã
   chọn vào trường `ma_danh_muc` của đầu việc. Không khớp → **dừng hỏi**, không tự gán.
4. **Ghi kế hoạch ra JSON** (cấu trúc tại docstring `scripts/kpi_mau.py` hàm `ghi_ke_hoach`), rồi chạy một lệnh:
   ```
   python scripts/kpi_mau.py --nhom <nhóm> --json ke_hoach.json --phuong-an <pa> --quy IV --nam 2026 --ra <tệp ra.xlsx>
   ```
   Lệnh tính hệ số, số lượng quy đổi (`scripts/kpi_calc.py`), điền vào **bản sao** mẫu trong `assets/`, rồi kiểm
   (`scripts/validate_plan.py`). Mã thoát 2 = thiếu dữ liệu → hỏi người dùng; 1 = đã xuất nhưng còn LỖI; 0 = sạch.
   **Không tự nhẩm hệ số, điểm, tỷ lệ.**
5. **Sửa LỖI, trình bày CẢNH BÁO.** LỖI (KH01–KH06, KH08, KH10, KH12, KH15) phải sửa cùng người dùng rồi chạy lại.
   CẢNH BÁO (KH07, KH09, KH11, KH13, KH14, KH16) trình bày để người dùng quyết.
6. **Thể thức:** có `kiem_the_thuc.py` (skill `the-thuc`/plugin) thì đo tệp ra; còn Mức 1–2 thì sửa.
7. **Điều chỉnh kế hoạch đã duyệt** [QĐ 1923, Đ13.3–13.4]: không sửa đè tệp đã duyệt. Lập bản mới, ghi rõ chỉ tiêu cũ →
   mới, lý do, căn cứ (nhiệm vụ đột xuất, đổi vị trí…), phạm vi, và "không hồi tố bất lợi". Trình Trưởng đơn vị duyệt lại.

## 6. Định dạng đầu ra

1. **Tệp Excel** đúng mẫu nhóm vị trí: sheet "Ke Hoach" đã điền; sheet "KPI" tự nối công thức; sheet "Đánh giá" để trống
   (giai đoạn 2). Tên tệp: `KH-KPI-Q<n>-<năm>_<họ-tên-không-dấu>.xlsx`.
2. **Bảng tóm tắt** trong trả lời:

| Trục | Điểm tối đa (mẫu) | Số đầu việc | SL quy đổi |
|---|---|---|---|

3. **Bảng cảnh báo** (từ `validate_plan.py`): mã · mức · vị trí · nội dung · căn cứ.
4. **Ghi chú căn cứ:** phương án hệ số và trạng thái; câu hỏi mở còn treo; "Chưa đối chiếu kế hoạch đơn vị" nếu thiếu;
   lỗi biểu mẫu đã biết gặp phải.
5. Dòng cuối: *"Bản đề xuất để trình Trưởng đơn vị phê duyệt [QĐ 1923, Đ13.1] — không phải kế hoạch đã duyệt."*

## 7. Checklist chất lượng (tự kiểm trước khi giao)

- [ ] Đã hỏi và ghi phương án hệ số; không có hệ số nào do mô hình tự tính.
- [ ] `validate_plan.py` không còn LỖI; cảnh báo đã trình bày.
- [ ] Mỗi đầu việc có sản phẩm, số lượng, thời hạn, nguồn minh chứng [Đ12.4].
- [ ] Quản lý có Trục (4); không quy kết quả tập thể thành KPI cá nhân.
- [ ] Dòng ví dụ "tiếng Bahnar" đã xóa; mẫu trong `assets/` không bị ghi đè.
- [ ] Hạn nộp lấy từ tệp quý, không từ trí nhớ; mâu thuẫn mốc đã nêu.
- [ ] Không có tên, điểm của người khác; văn phong "bảo đảm", viết hoa sau dấu hai chấm.

## 8. Ví dụ

**Người dùng:** "Lập KPI quý IV cho tôi, giáo vụ khoa Y-Dược."
**Làm:** nhóm `giao-vu`; đọc `quy/2026-Q4.yaml` → báo chưa có hướng dẫn Quý IV, đang dùng mốc chuẩn Quy chế, nêu hai
mốc đầu quý; xin kế hoạch quý của Khoa và danh sách việc; hỏi phương án hệ số; lập JSON; chạy `kpi_mau.py`; trả tệp,
bảng tóm tắt, cảnh báo.

**Người dùng:** "Hệ số của đầu việc này là bao nhiêu?"
**Làm:** không trả lời một con số ngay. Nêu 4 phương án và trạng thái căn cứ; người dùng chọn xong mới chạy
`python scripts/kpi_calc.py he-so --phuong-an <pa> --muc-do "<mức>" [--san-pham "<STT hoặc tên>"]`.

**Người dùng:** "Chấm điểm KPI quý III của tôi." → Ngoài phạm vi: chuyển skill `kpi-tu-danh-gia` (dùng chính tệp kế
hoạch đã duyệt làm đầu vào).
