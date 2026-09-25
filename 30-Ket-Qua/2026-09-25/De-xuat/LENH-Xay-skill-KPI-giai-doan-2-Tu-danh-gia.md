# LỆNH THỰC HIỆN — Xây bộ skill KPI, giai đoạn 2: Tự đánh giá, xếp loại cá nhân theo quý

**Gửi**: Claude Code (VS Code/Desktop), làm việc trong thư mục dự án `KTC-Quan-tri`
**Người giao**: Phòng TH-HC&QT, Trường Cao đẳng Kon Tum
**Ngày lập**: 25/9/2026
**Nối tiếp**: `30-Ket-Qua/2026-09-24/De-xuat/LENH-SUA-Xay-bo-skill-KPI-giai-doan-1.md` (đã hoàn thành, skill
`ktc-kpi-lap-ke-hoach` v1.0, plugin 1.1.0). Lệnh này xây skill mới `ktc-kpi-tu-danh-gia` — phần "Giai đoạn sau"
đã nêu ở cuối lệnh giai đoạn 1.
**Phạm vi dùng thật**: **toàn thể Lãnh đạo và viên chức, người lao động của Trường** — không riêng Phòng
TH-HC&QT. Mọi ví dụ, dữ liệu mẫu, quy ước cứng theo một đơn vị cụ thể đều là lỗi thiết kế của lượt này.

---

## 0. Vai trò và nguyên tắc (giữ nguyên lệnh giai đoạn 1, mục 0)

Bạn là kỹ sư xây skill. Bạn **không** tự chấm điểm hay xếp loại thay ai; bạn đóng gói quy tắc và dựng công cụ hỗ
trợ người dùng tự đánh giá, đúng theo "Hai điều bắt buộc khi dùng" ở cuối `20-Chuan-Chung/19-Quy-Tac-KPI.md`.

1. Mọi quy tắc phải dẫn nguồn dạng `[QĐ 1923, Đ19.1]`. Không có nguồn thì không viết thành quy tắc.
2. Quy tắc chưa xác nhận ghi vào Câu hỏi mở (`references/Cau-Hoi-Mo.md`, đã có 8 mục — nối tiếp từ #9).
3. Không đưa dữ liệu riêng một quý vào `SKILL.md`; dữ liệu theo quý đặt trong `references/quy/<YYYY>-Q<n>.yaml`.
4. Không sửa biểu mẫu chính thức trong `assets/`. Lỗi mẫu ghi vào `Known-Issues-Bieu-Mau.md`.
5. Mọi phép tính điểm, ngưỡng, xếp loại làm bằng script có ca thử — không để mô hình tự nhẩm hay tự "làm tròn có
   lợi".
6. Đọc `CLAUDE.md`, `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`, `92-Kinh-Nghiem/05-Known-Issues/Pending.md` trước.
   Đọc riêng `KI-014` (hai thang điểm) trước khi động vào hệ số quy đổi — **giai đoạn 2 không dùng hệ số quy đổi
   sản phẩm**, chỉ dùng % hoàn thành, nên nguy cơ thấp hơn giai đoạn 1 nhưng vẫn phải kiểm không lẫn hai thang.
7. **Không tự quyết định mức xếp loại cuối cùng, không tự phê duyệt.** Đầu ra luôn là **đề xuất của cá nhân**,
   chờ Trưởng đơn vị và Hiệu trưởng quyết định [QĐ 1923, Đ14.3c].

---

## 1. Phát hiện đã có — đọc trước khi làm, đỡ dò lại

Khảo sát ngày 25/9/2026 (sau lệnh giai đoạn 1 một ngày), để lại giá trị dùng ngay cho lệnh này:

1. **`kpi_mau.py` đã có hàm `cau_truc(wb)`** dò **động** vị trí các khối Trục và điểm tối đa trên sheet
   "Đánh giá" (không hardcode số dòng) — trả về `diem_truc`, `nhom_a`, `kpi_dong`. **Tái dùng, không viết lại.**
   Chỉ cần **mở rộng** để dò thêm: vị trí khối "Điều kiện bắt buộc" (mục II) và ô "Tự đề xuất mức xếp loại"
   (mục III).
2. **Tên sheet Đánh giá không đồng nhất giữa 6 mẫu**: `VC-Hanh-Chinh` và `Nha-Giao-Giang-Day-Cac-Khoa` đặt tên
   "Danh Gia" (viết hoa), 4 mẫu còn lại "Danh gia". Đã có `sheet_danh_gia(wb)` xử lý không phân biệt hoa/thường —
   **tái dùng**, không tự đi tìm `wb["Danh gia"]` cố định.
3. **Cấu trúc dòng của sheet Đánh giá khác nhau thật sự giữa 6 mẫu vị trí** — không chỉ khác điểm tối đa từng
   Trục (đúng như mục G của `19-Quy-Tac-KPI.md`) mà cả **số dòng mục A và cách sắp Trục cũng lệch**. Đã thử đọc
   bằng địa chỉ ô cố định (tham khảo cách `truong-pho-don-vi` dùng được ở giai đoạn 1) và bị sai hoàn toàn với
   mẫu `VC-Hanh-Chinh`. **Kết luận: bắt buộc dùng `cau_truc()`/dò động cho cả 6 mẫu, cấm hardcode theo mẫu đã
   quen (`truong-pho-don-vi`).**
4. **QĐ 2078/QĐ-CĐKT** (khung tiêu chí, PL I–XXVIII) — **văn bản chính vẫn chưa có trong kho** tính đến 25/9.
   Đã có thêm Phụ lục so với lúc lệnh giai đoạn 1 ghi nhận (10/28, tăng từ ghi nhận trước đó); đối chiếu 6 vị trí
   skill đang hỗ trợ với chỉ mục `00-INDEX-METADATA_Bo-KPI-QuyIII-2026_20260924.md`:

   | Nhóm vị trí trong skill | Phụ lục QĐ 2078 tương ứng | Có trong kho? |
   |---|---|---|
   | `truong-pho-don-vi` | XXIII | Có |
   | `nha-giao` | XXV | Có |
   | `bo-mon` | XXIV | **Chưa** |
   | `giao-vu` | XXVI | **Chưa** |
   | `hanh-chinh` | XXVII | **Chưa** |
   | `ho-tro` | XXVIII | **Chưa** |

   Sheet "Đánh giá" trong 6 mẫu `Mau-KeHoach-DanhGia_*` (đã dùng ở giai đoạn 1) **có cấu trúc giống PL XXIII khi
   đối chiếu trực tiếp** (đã kiểm với `truong-pho-don-vi`: mục A 13/12/5 = 30 điểm, mục B 40/7/8/5/5/5 = 70 điểm,
   khớp cả hướng dẫn chấm 4 mức trong ô ghi chú). Vì vậy dùng được các mẫu này để xây giai đoạn 2 cho **cả 6
   nhóm** ngay cả khi 4 Phụ lục riêng chưa có — **nhưng phải ghi rõ trong đầu ra**: "chưa đối chiếu được với văn
   bản QĐ 2078 gốc, đối chiếu qua mẫu Kế hoạch+KPI Quý III/2026". Khi kho có đủ QĐ 2078 và 4 Phụ lục còn thiếu,
   phải đối chiếu lại bằng agent `ktc-hieu-luc-vien-dan` hoặc thủ công rồi xóa ghi chú này.
5. **PL II của CV 694** (Mẫu tổng hợp kết quả đánh giá và đề xuất xếp loại, cấp đơn vị) đã có trong kho —
   dành cho **giai đoạn 3**, không dùng ở lệnh này, chỉ ghi nhận vị trí.
6. **Không tìm thấy trong kho**: Bảng kiểm sĩ số HSSV, Tiêu chí đánh giá chuyển đổi số, "Hướng dẫn đánh giá hằng
   quý/năm" riêng của Hiệu trưởng [Đ24.2]. Ba nguồn này cần cho điều kiện bắt buộc kèm xếp loại [Đ19.1] của nhóm
   nhà giáo/lãnh đạo khoa. Ghi vào Câu hỏi mở, **không suy đoán ngưỡng**.
7. Mẫu Kế hoạch+KPI Quý III vẫn còn lỗi wrap-text và ẩn dòng trống như đã vá tay trong phiên làm việc 24–25/9 (số
   liệu cụ thể: cột J toàn bộ 6 Trục thiếu `wrap_text`; Trục (2) dòng 35, 37–54 và Trục (6) toàn bộ 119–138 của
   sheet "Ke Hoach" thiếu `wrap_text` ở cột B/C/D/E). Đưa cách vá này (bật `wrap_text=True` khi ghi `dv["noi_dung"]`
   và `dv["ghi_chu"]`, tính lại `row_dimensions[r].height`, ẩn — không xóa — dòng trống theo khối 20 dòng/Trục)
   **vào thẳng `kpi_mau.py`**, không để người dùng phải tự vá bằng tay lần sau. Ghi bổ sung vào
   `Known-Issues-Bieu-Mau.md` (mục #10, #11).

---

## 2. Đọc nguồn

Lấy đường dẫn kho qua `duong_dan.ktc_database()`. Không đọc được thì **dừng và hỏi**.

### Bắt buộc
| Văn bản | Vị trí |
|---|---|
| QĐ 1923, Đ10, Đ11, Đ14, Đ17, Đ19, Đ21, Đ22, Đ23 | đã trích trong `19-Quy-Tac-KPI.md` mục D–H — đối chiếu lại toàn văn trước khi viết `kpi_danh_gia.py`, đừng chỉ tin bản tóm tắt |
| 6 mẫu `Mau-KeHoach-DanhGia_*_QuyIII-2026_*.xlsx`, sheet "Đánh giá"/"Danh Gia" | đã có trong `28-KTC-KPI/assets/` (và bản build `31-Plugin/skills/kpi-lap-ke-hoach/assets/`) |
| `00-INDEX-METADATA_Bo-KPI-QuyIII-2026_20260924.md` | `KTC-Database/03-Templates/03-12- Danh gia xep loai va KPI/` — đọc trước khi đụng vào bất kỳ Phụ lục nào |
| Các Phụ lục QĐ 2078 đã có (I, V, VI, VII, XIV, XVII, XIX, XXII, XXIII, XXV) | cùng thư mục trên — đối chiếu chéo với sheet "Đánh giá" tương ứng khi trùng vị trí |

### Cố gắng bổ sung trước khi bắt đầu (không bắt buộc phải có mới được làm)
- QĐ 2078/QĐ-CĐKT văn bản chính; PL XXIV, XXVI, XXVII, XXVIII; PL I của CV 694.
- Bảng kiểm sĩ số HSSV; Tiêu chí đánh giá chuyển đổi số; Hướng dẫn đánh giá hằng quý/năm của Hiệu trưởng.

Thiếu các nguồn trên thì **vẫn làm được** phần chấm điểm mục A, B và đề xuất xếp loại theo ngưỡng điểm thuần túy
[Đ19.1 cột điểm]; phần "điều kiện kèm theo" của nhóm nhà giáo/lãnh đạo khoa phải in rõ "thiếu nguồn, chưa kiểm
được điều kiện — người dùng tự xác nhận".

---

## 3. Vị trí trong dự án

```
20-Chuan-Chung/19-Quy-Tac-KPI.md        ← BẢN GỐC, bổ sung mục D–H nếu đối chiếu lại thấy thiếu
28-KTC-KPI/
  SKILL.md                              ← cân nhắc: 1 skill 2 nhiệm vụ (lập KH + tự đánh giá) hay 2 skill riêng — xem mục 7
  references/
    Skill-Library/19-Quy-Tac-KPI.md     ← bản sao, đồng bộ lúc build
    Cau-Hoi-Mo.md                       ← nối tiếp từ mục #9
    Known-Issues-Bieu-Mau.md            ← thêm #10, #11 (mục 1.7 ở trên)
    quy/2026-Q3.yaml, 2026-Q4.yaml      ← dùng lại, không tạo thêm tệp cấu hình
  assets/                               ← dùng lại 6 mẫu đã có, không thêm mẫu mới
29-Cong-Cu/
  kpi_mau.py                            ← mở rộng cau_truc(); thêm hàm ghi_danh_gia() hoặc script riêng kpi_danh_gia.py
  kpi_danh_gia.py                       ← MỚI: tính điểm, đối chiếu ngưỡng, xuất đề xuất xếp loại
92-Kinh-Nghiem/02-Regression/Cases/
  test_kpi_danh_gia.py                  ← MỚI, theo khuôn test_kpi_calc.py, test_validate_plan.py đã có
```

Việc bắt buộc đi kèm: chạy `python 29-Cong-Cu/kiem_tra_he_thong.py` đạt 0 lỗi trước và sau khi thêm tệp.

---

## 4. Bảng hỏi — chuẩn hóa thành bước của skill (không làm tay như phiên 24–25/9)

Trong phiên làm việc trước, các câu hỏi dưới đây đã phải hỏi bằng tay, qua hai bảng Excel dựng thủ công. Lệnh
này yêu cầu **script tự sinh bảng hỏi**, không lặp lại cách làm tay:

| # | Câu hỏi | Áp dụng | Vì sao không tự quyết |
|---|---|---|---|
| 1 | Điểm chấm 3 tiêu chí mục A (phẩm chất/kỷ luật · năng lực/trách nhiệm · đổi mới/sáng tạo), theo 4 mức [Đ10.5] | Mọi vị trí | Nhận định con người, AI không tự chấm thay |
| 2 | % hoàn thành thực tế mỗi chỉ tiêu KPI mục B (số lượng, chất lượng, tiến độ) | Mọi vị trí | Dữ liệu thực tế do người dùng xác nhận |
| 3 | Kết quả điều kiện bắt buộc: bảng kiểm sĩ số, % định mức giờ giảng, định mức NCKH | Chỉ nhóm `nha-giao`, và lãnh đạo khoa nếu có | Thiếu nguồn trong kho; là dữ liệu vận hành theo người |
| 4 | Cá nhân tự đề xuất mức xếp loại (mục III mẫu) | Mọi vị trí | Mẫu yêu cầu người tự đánh giá đề xuất trước |
| 5 | Có thuộc trường hợp đặc thù không (đào tạo tập trung ≥ 2 tháng, nghỉ ốm/thai sản ≥ 2 tháng, mới bổ nhiệm < 1 tháng, đang kiểm tra dấu hiệu vi phạm, điều động, đi học) [Đ21] | Mọi vị trí | Quyết định có xét kỳ này hay chuyển kỳ sau |
| 6 | 01 quý "Không hoàn thành" trước đó — có tính không HTXS cả năm? | Viên chức quản lý bắt buộc; người không giữ chức vụ "khuyến khích" [Đ19.5] — nhưng Đ19.1a lại ghi cho mọi cá nhân | Hai điều khoản chưa nhất quán — Câu hỏi mở #8 đã ghi, script nêu cả hai, không tự chọn |

Script sinh bảng hỏi phải dùng `openpyxl`, cùng phong cách 2 bảng đã dựng tay trong phiên 25/9 (ô vàng để điền,
`DataValidation` cho các câu chọn phương án, để trống = không đổi), rồi đọc lại kết quả người dùng đã điền —
**không hỏi từng câu rời rạc trong hội thoại nếu có thể gộp thành một bảng.**

---

## 5. Quy trình xử lý

1. **Dò cấu trúc mẫu** — mở rộng `cau_truc()`: thêm dò khối "II. Điều kiện bắt buộc" (dòng bắt đầu bằng "TT",
   cột "Điều kiện bắt buộc") và ô "III. Tự đề xuất mức xếp loại". Không hardcode theo mẫu `truong-pho-don-vi`
   (xem phát hiện #3, mục 1).
2. **Sinh bảng hỏi** theo mục 4, đúng nhóm vị trí đang xử lý.
3. **Đọc bảng hỏi người dùng đã điền.**
4. **Tính mục A** — điền điểm theo mức người dùng chọn (không tự suy đoán mức từ mô tả).
5. **Tính mục B** — % hoàn thành × điểm tối đa từng Trục; **chặn trần 100%** (vá lỗi #7 của
   `Known-Issues-Bieu-Mau.md`); phần vượt ghi nhận định tính, không cộng thêm điểm [Đ11.6].
6. **Cộng A + B**, đối chiếu ngưỡng xếp loại [Đ19.1] và điều kiện kèm theo. In rõ điều kiện nào **đủ dữ liệu để
   kiểm** và điều kiện nào **thiếu nguồn, người dùng tự xác nhận**.
7. **Không đối chiếu trần tỷ lệ HTXS theo nhóm tương đồng** [Đ19.2] — in dòng nhắc "trần tỷ lệ tính ở cấp đơn vị/
   Trường, thuộc giai đoạn 3, chưa áp dụng ở đây".
8. **Không tự áp dụng "người đứng đầu không cao hơn tập thể"** [Đ14.4, Đ16.2, Đ19.4] nếu chưa có kết quả xếp
   loại tập thể đơn vị trong kỳ — hỏi người dùng có kết quả đó chưa, có thì đối chiếu, không thì bỏ qua và ghi rõ.
9. **Xuất kết quả** theo mục 6 dưới đây.
10. **Kiểm bằng script riêng** (`92-Kinh-Nghiem/.../test_kpi_danh_gia.py`) trước khi coi là xong.

---

## 6. Định dạng đầu ra

1. Tệp Excel — chính là sheet "Đánh giá"/"Danh Gia" của mẫu vị trí, đã điền mục A, B, điểm tổng, mục III (đề
   xuất của cá nhân). Tên tệp: `TDG-KPI-Q<n>-<năm>_<họ-tên-không-dấu>.xlsx`. Lưu tại
   `30-Ket-Qua/<ngày>/KPI-ca-nhan/`.
2. Bảng tóm tắt trong trả lời: điểm mục A, điểm mục B theo từng Trục, tổng điểm, mức đề xuất theo ngưỡng điểm
   thuần túy.
3. Bảng điều kiện: đủ dữ liệu / thiếu dữ liệu / không đạt, kèm căn cứ Điều.
4. Ghi chú căn cứ: "Đối chiếu qua mẫu Kế hoạch+KPI Quý III/2026, chưa đối chiếu trực tiếp QĐ 2078 (Phụ lục
   [XXIV/XXVI/XXVII/XXVIII] chưa có trong kho)" — chỉ ghi khi đúng vị trí thuộc 4 nhóm còn thiếu Phụ lục riêng.
5. Dòng cuối bắt buộc: *"Đề xuất của cá nhân — chưa phải kết luận của Trưởng đơn vị và Hiệu trưởng [QĐ 1923,
   Đ14.3c]. Trần tỷ lệ Hoàn thành xuất sắc theo nhóm tương đồng chưa được đối chiếu ở bước này [Đ19.2]."*

---

## 7. Một quyết định cần chốt trước khi viết code

**Một skill hay hai skill?** Giai đoạn 1 (`lap-ke-hoach`) và giai đoạn 2 (`tu-danh-gia`) dùng chung mẫu, chung
`cau_truc()`, chung tệp cấu hình quý — nhưng mô tả kích hoạt phải tách rõ ("lập KPI quý" ≠ "tự đánh giá, chấm
điểm KPI quý", đúng như bảng kiểm tra kích hoạt đã lập ngày 24/9). Hai lựa chọn:
- (a) Một skill `ktc-kpi` với hai bước rõ ràng trong cùng `SKILL.md`, mô tả liệt kê đủ hai cụm từ kích hoạt.
- (b) Hai skill riêng `ktc-kpi-lap-ke-hoach` (đã có) và `ktc-kpi-tu-danh-gia` (mới), dùng chung `references/` và
  `scripts/` qua đường dẫn tương đối.

**Dùng bảng kiểm tra kích hoạt của cả hai lựa chọn** (6 câu đã lập cho giai đoạn 1 + câu "Chấm điểm KPI quý III
của tôi" phải kích hoạt đúng skill tự đánh giá) trước khi chốt, ghi lý do chọn vào Decision Log.

---

## 8. Bảo mật dữ liệu cá nhân

Giữ nguyên nguyên tắc giai đoạn 1 (mục 6 lệnh cũ): xuất vào `30-Ket-Qua/<ngày>/KPI-ca-nhan/`, đã có trong
`.gitignore`. Dữ liệu giai đoạn 2 nhạy cảm hơn (điểm chấm phẩm chất chính trị, đạo đức) — kiểm tra lại
`.gitignore` che đúng thư mục, viết ca thử xác nhận `git add -A` không đưa các tệp mới vào git.

---

## 9. Script và kiểm thử

- Mở rộng `cau_truc()` trong `kpi_mau.py` (mục 1.1). Viết ca thử cho cả 6 mẫu vị trí — **không chỉ thử với
  `truong-pho-don-vi`** (bài học từ phát hiện #3, mục 1).
- `kpi_danh_gia.py`: tính điểm, đối chiếu ngưỡng, sinh và đọc bảng hỏi.
- Ca thử tối thiểu: ngưỡng 89,99/90 · 69,99/70 · 49,99/50 (điểm xếp loại); mục A dưới 5 điểm/nhóm tiêu chí (vi
  phạm "không thấp hơn 5 điểm" Đ10.4 — cảnh báo cấu trúc mẫu sai, không phải lỗi người dùng); % hoàn thành >
  100% bị chặn trần; thiếu dữ liệu điều kiện bắt buộc → in "thiếu nguồn", không tự cho "Đạt"; gọi script mà
  chưa điền bảng hỏi → dừng, không tự chấm.
- Mỗi phép kiểm có ca thử ngược (`.claude/rules/22-kiem-thu-va-dong-goi.md`).
- `python 29-Cong-Cu/kiem_tra_he_thong.py` đạt 0 lỗi trước và sau đóng gói.

---

## 10. Chạy thử trước khi bàn giao

Bảng kiểm tra kích hoạt (bổ sung vào `28-KTC-KPI/TEST-REPORT.md`, chạy thật ở phiên mới — 6 câu của giai đoạn 1
vẫn ghi "chưa chạy", lệnh này phải kèm chạy thật, không để nợ tiếp):

| Câu | Kỳ vọng |
|---|---|
| "Chấm điểm KPI quý III của tôi" | Kích hoạt phần tự đánh giá (không phải `quan-tri`, không phải phần lập kế hoạch) |
| "Tự đánh giá xếp loại quý IV, tôi là giáo vụ khoa" | Kích hoạt, hỏi bảng hỏi mục 4 |
| "Tính % KPI theo Trục của khoa tháng 9" | KHÔNG kích hoạt (→ `bao-cao`) |
| "Tôi được Hoàn thành xuất sắc không?" | Tính điểm, đối chiếu ngưỡng, **không tự khẳng định** — nêu rõ chưa đối chiếu trần tỷ lệ |
| "Xếp loại tập thể Phòng tôi thế nào?" | KHÔNG kích hoạt (thuộc giai đoạn 3, thuộc PL II CV 694) |

---

## 11. Đóng gói và bàn giao

1. Đóng gói skill, dựng lại plugin (tăng version), cập nhật `31-Plugin/CHANGELOG.md`.
2. Ghi Decision Log `92-Kinh-Nghiem/06-Decision-Log/DL-<ngày>-Bo-skill-KPI-giai-doan-2.md` — bắt buộc ghi lý do
   chọn một/hai skill (mục 7).
3. Cập nhật `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`.
4. **Không tự tải lên Drive, không tự cài vào Claude.ai.**
5. Báo cáo bàn giao gồm: nguồn đã đọc/chưa đọc được; kết quả đối chiếu 6 mẫu Đánh giá với Phụ lục QĐ 2078 (mục
   nào còn "chưa đối chiếu trực tiếp"); kết quả ca thử; `TEST-REPORT.md`; câu hỏi mở còn tồn; danh sách việc gửi
   Phòng TCCB&CTHSSV xác nhận (đặc biệt: 4 Phụ lục XXIV/XXVI/XXVII/XXVIII, Bảng kiểm sĩ số, Tiêu chí chuyển đổi
   số, Hướng dẫn đánh giá hằng quý/năm).

## 12. Điều kiện dừng ngay

- Phát hiện sheet "Đánh giá" của một mẫu vị trí có cấu trúc `cau_truc()` không dò được (ví dụ thiếu mẫu "Trục
  (n)" hoặc công thức SUM khác dạng đã biết) — dừng, báo, không đoán cấu trúc.
- QĐ 2078 hoặc Phụ lục mới xuất hiện trong kho **trong lúc đang làm** — dừng, đối chiếu lại toàn bộ mục A/B đã
  giả định qua mẫu Kế hoạch+KPI, trước khi tiếp tục.
- Bất kỳ bước nào cần tự quyết định mức xếp loại thay người dùng, hoặc tự tính trần tỷ lệ HTXS.

## Giai đoạn sau (không làm ở lượt này)

- **Giai đoạn 3** `ktc-kpi-tong-hop-xep-loai`: tổng hợp cấp đơn vị bằng PL II (CV 694, đã có trong kho), đối
  chiếu trần tỷ lệ HTXS theo nhóm tương đồng toàn Trường [Đ19.2], áp quy tắc "người đứng đầu không cao hơn tập
  thể" [Đ14.4, Đ16.2, Đ19.4], và rà soát khung tiêu chí khi QĐ 2078 đầy đủ.

*Kết quả do AI xây dựng chỉ có giá trị tham khảo. Quy tắc nghiệp vụ trong skill phải được Phòng TCCB&CTHSSV và
Phòng TH-HC&QT duyệt trước khi dùng chính thức.*
