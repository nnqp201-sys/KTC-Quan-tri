# Kiểm hồ sơ đơn vị nộp — Kỳ tháng 9/2026 (kết quả T9 + kế hoạch T10)

Nguồn: `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/` — 3 thư mục con, 29 tệp (10 `.xlsx` IIb, 10 `.docx` IIa, 9 `.xlsx` Ib).
Công cụ: `read_bc736_excel.py` (v3.3) qua `29-Cong-Cu/doi_soat_so_lieu.py` (đối soát KH↔KQ, Task_ID, % KPI theo Trục,
mã đơn vị) + kiểm tay từng tệp bằng `openpyxl`/`python-docx` (đọc phần đầu tệp, sheet, header) +
`29-Cong-Cu/kiem_the_thuc.py` (thể thức).

Mức vấn đề dùng theo quy ước 4 mức của KTC-Ra-Soat-897 (1 bắt buộc sửa → 4 góp ý). Kết luận theo skill
32/skill kiểm hồ sơ: **ĐỦ ĐIỀU KIỆN TỔNG HỢP** = 0 lỗi Mức 1–2; ngược lại **TRẢ LẠI ĐƠN VỊ**.

---

## A. Bảng kiểm theo tệp

### A.1 — `1. BAO CAO PL IIB\` (Phụ lục IIb, kết quả tháng 9/2026, có KPI)

| Tệp | Mã đơn vị | Kỳ trong tệp | Kết luận | Lý do (vị trí cụ thể) |
|---|---|---|---|---|
| `BAN TT.xlsx` | P-THHC (bộ phận 2 — Ban TT) | tháng 9/2026 ✓ | **TRẢ LẠI** (Mức 2) | Sheet "Mẫu BC tháng", dòng "Tham mưu văn bản, đề xuất có liên quan đến cô…" (Trục có liên quan): **[SAI CT (16)]** KPI tiến độ-QĐ ghi 1.1, đúng phải = Hệ số×(15) = 0.75. Thể thức: TX04 Mức 4 (bảng in dọc, không vừa trang — góp ý). |
| `KHCB.xlsx` | K-KHCB | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 32 nhiệm vụ, 0 cảnh báo công thức KPI. Có 7 nhiệm vụ ở Mục II (chưa hoàn thành, chuyển sang tháng sau) — không phải lỗi, chỉ lưu ý khi viết báo cáo. TX04 Mức 4 (góp ý). |
| `KTCN.xlsx` | K-KTCN | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | Sheet "BC KQ -T9", 17 nhiệm vụ, **0 cảnh báo** — đã đọc được đúng cấu trúc, công thức KPI khớp toàn bộ. **Đã kiểm chứng độc lập, KHÔNG xác nhận lại cảnh báo cũ "Excel IIb sai cấu trúc"** của kỳ trước — tệp kỳ này (9/2026) đúng mẫu, đọc trọn vẹn. TX04 Mức 4 (góp ý). |
| `P.THHCQT.xlsx` | P-THHC | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 14 nhiệm vụ, 0 cảnh báo. Đầu tệp ghi rõ "ĐƠN VỊ: PHÒNG TH-HC&QT" — đây là báo cáo cấp Phòng, tách biệt với `BAN TT.xlsx`. TX04 Mức 4. |
| `QLKHCNHTPT.xlsx` | P-QLKH | tháng 9/2026 ✓ | **TRẢ LẠI** (Mức 2) | Dòng "Tham dự Hội nghị tập thể nhân sự chủ chốt của…": **[SAI CT (14)]** KPI chất lượng-QĐ ghi 1.0, đúng phải = Hệ số×(13) = 0.3. Thêm TX02 Mức 2: 1 ô dùng font Calibri thay vì Times New Roman. |
| `SƯ PHẠM.xlsx` | K-SUPH | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 12 nhiệm vụ, 0 cảnh báo, 0 lỗi thể thức. |
| `TCCB.xlsx` | P-TCCB | tháng 9/2026 ✓ | **TRẢ LẠI** (Mức 2) | Dòng 3 đầu tệp: **"ĐƠN VỊ:…......."** — ô bắt buộc "Đơn vị" bị bỏ trống (không điền "PHÒNG TCCB&CTHSSV"), chỉ còn dấu chấm mẫu. Mã đơn vị hiện suy được nhờ tên tệp `TCCB.xlsx`, nhưng ô này bắt buộc phải điền theo mẫu TB736. 20 nhiệm vụ, công thức KPI không sai. |
| `TCKT.xlsx` | P-TCKT | tháng 9/2026 ✓ | **TRẢ LẠI** (Mức 2 — nhiều lỗi) | 7 cảnh báo công thức: dòng "Xây dựng kế hoạch và tổ chức thẩm mức kinh tế…" **[SAI CT (9)]** Hệ số=2.0 (đúng=Điểm×1%=1.0) và **[SAI CT (10)]** SL quy đổi=2.0 (đúng=SL×Hệ số=4.0); dòng "TB Thu học phí các lớp K8C GDMN VLVH…" **[SAI CT (10)]** SL quy đổi=3.0 (đúng=1.0); dòng "Trích lập quỹ học bổng khuyến khích học tập…" **[SAI CT (9)]** Hệ số=4.0 (đúng=1.0), **[SAI CT (10)]** SL quy đổi=4.0 (đúng=16.0), **[SAI CT (12)]** KPI SL-QĐ=4.0 (đúng=16.0); dòng "Ban hành định mức kinh tế kỹ thuật…" **[SAI CT (9)]** Hệ số=1.0 (đúng=1.2). |
| `Y DƯỢC.xlsx` | K-YDUOC | tháng 9/2026 (sheet chính) | **TRẢ LẠI** (Mức 2) | Sheet "Mẫu BC tháng" (22 nhiệm vụ) sạch — 0 cảnh báo. NHƯNG workbook còn **sheet thứ hai "Mẫu BC QUÝ"** — đây là mẫu **Phụ lục IIc** (báo cáo kết quả **Quý**), phần đầu vẫn để nguyên placeholder ("ĐƠN VỊ:…......", "Quý … năm 20…") và nội dung dòng là **văn mẫu chưa điền** (ví dụ "…", tên người chỉ đạo lặp lại giống hệt mẫu gốc "Hiệu trưởng"/"PHT Nguyễn Trung Hiếu"…) — **sheet mẫu trống chưa xóa**, sai loại Phụ lục so với yêu cầu nộp (IIb tháng), cần xóa trước khi tổng hợp. |
| `ĐTSHLX.xlsx` | K-DTSHLX | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 27 nhiệm vụ, 0 cảnh báo công thức. TX04 Mức 4. |

### A.2 — `2. BAO CAO IIA\` (Phụ lục IIa, báo cáo tường thuật)

| Tệp | Mã đơn vị | Kỳ trong tệp | Kết luận | Lý do |
|---|---|---|---|---|
| `BAN TT.docx` | P-THHC (bộ phận 2) | **tháng 8/2026** ✗ | **TRẢ LẠI** (Mức 1) | Dòng tiêu đề: "BÁO CÁO kết quả công tác **tháng 8 năm 2026**, và kế hoạch công tác **tháng 9 năm 2026**" — đây là **tệp của kỳ trước (8/2026)**, không phải kỳ đang nộp (9/2026). Đã kiểm chứng độc lập trực tiếp trên nội dung tệp, không chỉ dựa tên tệp/thư mục. Cần đơn vị nộp lại đúng bản tháng 9/2026. |
| `KHCB.docx` | K-KHCB | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |
| `KTCN.docx` | K-KTCN | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** (kèm góp ý Mức 3) | TT05: 189 đoạn chữ có màu khác đen (NĐ 30 yêu cầu màu đen) — không chặn tổng hợp (Mức 3), nhưng nên sửa trước khi dùng làm căn cứ trình ký. |
| `KTNL.docx` | K-KTNL | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |
| `P QLKHCN.docx` | P-QLKH | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |
| `P TCCB.docx` | P-TCCB | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |
| `P TCKT.docx` | P-TCKT | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |
| `SƯ PHẠM.docx` | K-SUPH | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |
| `Y DƯỢC.docx` | K-YDUOC | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |
| `ĐTSHLX.docx` | K-DTSHLX | tháng 9/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 0 lỗi thể thức. |

**Không có tệp `.docx` IIa nào đứng tên chính Phòng TH-HC&QT (`P-THHC`)** — chỉ có `BAN TT.docx` (bộ phận Ban
Truyền thông, phạm vi hẹp mảng truyền thông) và bản đó lại sai kỳ. Xem mục B.

### A.3 — `2. Phu luc Ib\` (Phụ lục Ib, kế hoạch tháng 10/2026, không KPI)

Lưu ý: kỳ trong các tệp Ib đúng là **"tháng 10 năm 2026"**, không phải "tháng 9" — vì đây là **kế hoạch của
tháng kế tiếp**, nộp kèm kết quả tháng 9 theo đúng chu kỳ nộp hồ sơ (KQ tháng N + KH tháng N+1). **Đây không
phải lỗi.**

| Tệp | Mã đơn vị | Kỳ trong tệp | Kết luận | Lý do |
|---|---|---|---|---|
| `BAN TT.xlsx` | P-THHC (bộ phận 2) | tháng 10/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 20 nhiệm vụ, 0 cảnh báo. |
| `KHCB.xlsx` | K-KHCB | tháng 10/2026 ✓ | **TRẢ LẠI** (Mức 2) | **14/14 nhiệm vụ** ở sheet "Mẫu KH tháng" **để trống cột Ghi chú** (cột 11) — không xác định được nhiệm vụ nào "Đưa vào KH Trường" hay "Thường xuyên của đơn vị" (ví dụ dòng "Triển khai kế hoạch xây dựng, rà soát và cập…", "Dự giờ chuyên môn nhà giáo, học kỳ I…"…). Thêm TX02 Mức 2: 13 ô dùng Calibri thay Times New Roman. |
| `KTCN.xlsx` | K-KTCN | tháng 10/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | Sheet "KH-T10", 18 nhiệm vụ, 0 cảnh báo. |
| `QLKHCNHTPT.xlsx` | P-QLKH | tháng 10/2026 ✓ | **ĐỦ ĐIỀU KIỆN TỔNG HỢP** | 23 nhiệm vụ, 0 cảnh báo, 0 lỗi thể thức. |
| `SP.xlsx` | K-SUPH | tháng 10/2026 ✓ | **TRẢ LẠI** (Mức 2) | **6/6 nhiệm vụ để trống cột Ghi chú** (ví dụ "Xây dựng và triển khai kế hoạch báo cáo tập h…", "Phối hợp với Phòng QLĐT&BĐCL và các đơn vị th…"). TX02 Mức 2: 4 ô Calibri. |
| `TCCB.xlsx` | P-TCCB | tháng 10/2026 ✓ | **TRẢ LẠI** (Mức 2) | Sheet "Mẫu KH tháng" và "Mẫu KH Quý" đều có 1 dòng để trống Ghi chú (nội dung ghi "…", chưa điền rõ). Ngoài ra sheet **"Mẫu KH Quý" là mẫu Phụ lục Ia (kế hoạch Quý) còn nguyên placeholder** ("ĐƠN VỊ:…......", "Quý … năm 20…", nội dung toàn "…" và tên người chỉ đạo mẫu gốc) — **sheet mẫu trống chưa xóa**, không thuộc phạm vi nộp Ib tháng. |
| `TCKT.xlsx` | P-TCKT | tháng 10/2026 ✓ | **TRẢ LẠI** (Mức 2) | 3 dòng cột Ghi chú ghi **"Kế hoạch của Trường"** — không thuộc 4 giá trị hợp lệ ("Đưa vào KH Trường"/"Thường xuyên của đơn vị"/"Bổ sung ngoài KH quý"/"Kết luận giao ban"); các dòng: "Phối hợp Sở Tài chính thực hiện thẩm tra phê…", "Tham mưu Kế hoạch và thẩm định định mức kinh t…", "Thực hiện theo dõi và báo cáo thường xuyên tì…". Thêm 1 **[SAI CÔNG THỨC]**: dòng "Tham mưu ban hành định mức kinh tế - kỹ thuật…" Hệ số=1.0 nhưng Điểm×1%=1.2. |
| `Y DƯỢC.xlsx` | K-YDUOC | tháng 10/2026 ✓ | **TRẢ LẠI** (Mức 2) | Sheet "Mẫu KH tháng": **15/16 nhiệm vụ để trống Ghi chú**. Sheet "Mẫu KH Quý" cũng 1 dòng trống Ghi chú và **là sheet mẫu Phụ lục Ia còn placeholder chưa điền** (giống mô tả ở `TCCB.xlsx` — cùng một mẫu gốc dùng chung, chưa xóa). |
| `ĐTSHLX.xlsx` | K-DTSHLX | tháng 10/2026 ✓ | **TRẢ LẠI** (Mức 2) | Sheet "Mẫu KH tháng": **15/32 nhiệm vụ để trống Ghi chú**. Sheet "Mẫu KH Quý" cũng có mẫu Phụ lục Ia còn placeholder chưa điền (như trên) và 1 dòng trống Ghi chú. |

---

## B. Đơn vị chưa nộp / nộp thiếu — đối chiếu 13 đầu mối bắt buộc

13 đầu mối = 11 đơn vị cấp một (`20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`) + Công đoàn cơ sở (`DT-CDCS`) +
Đoàn Thanh niên – Hội Sinh viên (`DT-DTN`). **KI-015: hai mã `DT-CDCS`/`DT-DTN` là mã tạm, chưa chốt chính
thức trong bảng mã chuẩn** — dưới đây vẫn liệt kê là thiếu nộp nhưng không quy kết sai mã.

| Đơn vị | IIb (KQ tháng, có KPI) | IIa (BC tường thuật) | Ib (KH tháng) | Ghi chú |
|---|---|---|---|---|
| `P-TCCB` | ✓ | ✓ | ✓ | Đủ 3 loại. |
| `P-QLDT` (Phòng QLĐT&BĐCL) | **✗ thiếu** | **✗ thiếu** | **✗ thiếu** | **Không có tệp nào ở cả 3 thư mục** — vắng mặt hoàn toàn kỳ này. |
| `P-THHC` (Phòng TH-HC&QT, cấp Phòng) | ✓ (`P.THHCQT.xlsx`) | **✗ thiếu** | **✗ thiếu** | IIb có báo cáo cấp Phòng đầy đủ. Nhưng IIa và Ib **không có báo cáo nào đứng tên Phòng** — chỉ có `BAN TT.xlsx`/`BAN TT.docx` (Ban Truyền thông, bộ phận cấp 2, phạm vi hẹp mảng truyền thông theo `13-Bang-Ma-Don-Vi.md`). **Xác nhận độc lập lại cảnh báo cũ "P-THHC nộp thiếu báo cáo đơn vị"**: đúng một phần — IIb đã có đủ (khác kỳ trước), nhưng IIa/Ib vẫn thiếu phần Phòng, và bản IIa Ban TT hiện có còn sai kỳ (tháng 8). |
| `P-QLKH` | ✓ | ✓ | ✓ | Đủ 3 loại. |
| `P-TCKT` | ✓ | ✓ | ✓ | Đủ 3 loại (nhưng có lỗi KPI/Ghi chú — xem mục A). |
| `K-KHCB` | ✓ | ✓ | ✓ | Đủ 3 loại. |
| `K-SUPH` | ✓ | ✓ | ✓ | Đủ 3 loại. |
| `K-KTNL` (Khoa Kinh tế và Nông Lâm) | **✗ thiếu** | ✓ (`KTNL.docx`) | **✗ thiếu** | Chỉ nộp bản tường thuật (IIa); **thiếu cả Phụ lục IIb (kết quả, có KPI) và Ib (kế hoạch)** — không tính được KPI, không đối chiếu được kế hoạch. |
| `K-KTCN` | ✓ | ✓ | ✓ | Đủ 3 loại — đã kiểm chứng lại, không còn cảnh báo cấu trúc. |
| `K-YDUOC` | ✓ | ✓ | ✓ | Đủ 3 loại (nhiều lỗi Ghi chú — xem mục A). |
| `K-DTSHLX` | ✓ | ✓ | ✓ | Đủ 3 loại (nhiều lỗi Ghi chú — xem mục A). |
| `DT-CDCS` (Công đoàn cơ sở) | ✗ | ✗ | ✗ | Không có tệp nào — mã `DT-CDCS` chưa chốt chính thức (KI-015), nhưng đầu mối này vẫn cần đối chiếu tay với P-THHC/lãnh đạo. |
| `DT-DTN` (Đoàn TN – HSV) | ✗ | ✗ | ✗ | Như trên (KI-015). |

**Tóm tắt thiếu nộp**: `P-QLDT` thiếu hoàn toàn cả 3 loại; `K-KTNL` thiếu Phụ lục IIb và Ib (chỉ có IIa);
`P-THHC` thiếu báo cáo cấp Phòng ở IIa và Ib (bản Ban Truyền thông không thay thế được); `DT-CDCS`, `DT-DTN`
thiếu hoàn toàn (mã chưa chốt).

---

## C. Đối soát chéo cấp Trường (DS02–DS06, `doi_soat_so_lieu.py`)

- **DS06 (mã đơn vị)**: không có lỗi — toàn bộ 19 tệp `.xlsx` map được về đúng 1 mã chuẩn (không có mã lạ `?...`).
- **DS04 (Task_ID trùng)**: không có — hiện các tệp **chưa có cột Task_ID** (chưa triển khai KI-001 ở đợt nộp
  này), nên không phát sinh trùng, cũng không có gì để đối chiếu Task_ID.
- **DS03 (KH ↔ KQ cùng kỳ)**: không có cặp cùng kỳ để so — đúng như thiết kế (IIb là KQ tháng 9, Ib là KH
  tháng 10, khác kỳ). Không phải lỗi.
- **DS02 (truy vết tổng hợp cấp Trường)**: không chạy được — kỳ này **chưa có tệp tổng hợp cấp Trường** để đối
  chiếu (không truyền `--tong-hop`).
- **DS05 (% KPI theo Trục, tính lại từ toàn bộ đơn vị đã nộp)** — số tham chiếu, **không quy đổi giữa hai
  thang điểm (KI-014)**:

| Trục | Số NV | SL quy đổi | % số lượng | % chất lượng | % tiến độ |
|---|---|---|---|---|---|
| 1 | 92 | 353.2 | 95.3 | 92.1 | 94.3 |
| 2 | 27 | 42.6 | 100.0 | 93.5 | 95.9 |
| 3 | 18 | 93.5 | 100.0 | 97.7 | 100.0 |
| 4 | 17 | 30.1 | 100.0 | 83.2 | 100.0 |
| 5 | 24 | 23.1 | 100.0 | 85.3 | 100.0 |
| 6 | 14 | 11 | 100.0 | 90.9 | 100.0 |

Không có Trục nào báo "lệch thang (KI-014)". Số này **chưa loại trừ các lỗi công thức đã nêu ở mục A** (ví dụ
TCKT, QLKHCNHTPT, BAN TT) — vì công cụ chỉ cộng dồn số liệu **đơn vị đã ghi**, không tự sửa theo công thức
đúng. Dùng để tham khảo, không dùng để chấm KPI chính thức khi còn lỗi Mức 1–2 chưa sửa.

---

## D. Tổng số lỗi theo mức (toàn bộ 29 tệp)

| Mức | Số lượng | Loại |
|---|---|---|
| **Mức 1** | 1 | `BAN TT.docx` (IIa) sai kỳ hoàn toàn (tháng 8 thay vì tháng 9) |
| **Mức 2** | ~14 nhóm lỗi | Sai công thức KPI cascade (BAN TT.xlsx, QLKHCNHTPT.xlsx, TCKT.xlsx×2 tệp), thiếu/sai cột Ghi chú (KHCB, SP, TCCB, TCKT, Y DƯỢC, ĐTSHLX — Ib), ô "Đơn vị" bỏ trống (TCCB.xlsx IIb), sheet mẫu trống chưa xóa (Y DƯỢC.xlsx IIb; TCCB/Y DƯỢC/ĐTSHLX.xlsx Ib), font sai Times New Roman TX02 (QLKHCNHTPT, KHCB, SP) |
| **Mức 3** | 2 | TT04b cỡ chữ không thống nhất (BAN TT.docx), TT05 màu chữ khác đen (KTCN.docx) |
| **Mức 4** | nhiều | TX04 bảng in dọc không vừa trang A4 ngang (phần lớn tệp `.xlsx` — góp ý kỹ thuật in ấn, không chặn tổng hợp) |

**Kết luận một dòng**: **TRẢ LẠI ĐƠN VỊ** đối với `BAN TT.xlsx`+`BAN TT.docx` (P-THHC/Ban TT), `QLKHCNHTPT.xlsx`
(P-QLKH, cả 2 tệp IIb), `TCCB.xlsx` (P-TCCB, cả IIb và Ib), `TCKT.xlsx` (P-TCKT, cả IIb và Ib), `Y DƯỢC.xlsx`
(K-YDUOC, cả IIb và Ib), `KHCB.xlsx` (K-KHCB, riêng bản Ib), `SP.xlsx` (K-SUPH, Ib), `ĐTSHLX.xlsx` (K-DTSHLX,
riêng bản Ib) — do còn lỗi Mức 1–2 nêu ở mục A. **ĐỦ ĐIỀU KIỆN TỔNG HỢP** đối với các tệp còn lại (0 lỗi Mức
1–2): `KHCB.xlsx`(IIb), `KTCN.xlsx`(IIb, Ib), `P.THHCQT.xlsx`(IIb), `SƯ PHẠM.xlsx`(IIb), `ĐTSHLX.xlsx`(IIb),
`BAN TT.xlsx`(Ib), `QLKHCNHTPT.xlsx`(Ib), và toàn bộ `.docx` IIa trừ `BAN TT.docx`.

---

## E. Đoạn văn gửi đơn vị (P-THHC chép gửi lại)

> Kính gửi các Phòng/Khoa,
>
> Qua rà soát hồ sơ kế hoạch/báo cáo kỳ tháng 9/2026, P-THHC đề nghị các đơn vị sau kiểm tra và nộp lại:
>
> 1. **Phòng QLĐT&BĐCL**: chưa thấy hồ sơ nào (Phụ lục IIa, IIb, Ib) trong đợt nộp này — đề nghị nộp bổ sung
>    cả 3 loại.
> 2. **Khoa Kinh tế và Nông Lâm**: mới nhận được báo cáo tường thuật (Phụ lục IIa). Đề nghị bổ sung Phụ lục
>    IIb (kết quả tháng 9, có bảng KPI) và Phụ lục Ib (kế hoạch tháng 10).
> 3. **Phòng TH-HC&QT**: đã nhận đủ Phụ lục IIb đứng tên Phòng. Tuy nhiên Phụ lục IIa và Ib hiện chỉ có bản
>    của Ban Truyền thông (phạm vi hẹp mảng truyền thông) — đề nghị bổ sung báo cáo tường thuật và kế hoạch
>    đứng tên Phòng (đầy đủ mảng văn thư, hành chính, quản trị, CSVC). Riêng tệp `BAN TT.docx` hiện nộp là
>    bản **tháng 8/2026** — đề nghị thay bằng đúng bản tháng 9/2026.
> 4. **Phòng TCCB&CTHSSV**: tệp `TCCB.xlsx` (Phụ lục IIb) bỏ trống ô "ĐƠN VỊ:" ở đầu trang — đề nghị điền đủ
>    tên đơn vị.
> 5. **Phòng QLKHCN&HTPT**: tệp `QLKHCNHTPT.xlsx` (IIb), dòng "Tham dự Hội nghị tập thể nhân sự chủ chốt…" —
>    cột KPI chất lượng-QĐ đang ghi 1.0, theo công thức (Hệ số×KPI chất lượng-TT) phải là 0.3 — đề nghị đối
>    chiếu lại.
> 6. **Phòng TC-KT**: tệp `TCKT.xlsx` (cả IIb và Ib) có nhiều dòng lệch công thức Hệ số/Số lượng quy đổi/KPI
>    (chi tiết trong bảng đính kèm) và 3 dòng cột Ghi chú (Ib) ghi "Kế hoạch của Trường" — không thuộc 4 giá
>    trị hợp lệ, đề nghị sửa thành "Đưa vào KH Trường" hoặc giá trị phù hợp khác.
> 7. **Khoa các Khoa học cơ bản, Khoa Sư phạm, Khoa Y - Dược, Khoa ĐT&SHLX**: tệp Phụ lục Ib (kế hoạch tháng
>    10) còn nhiều dòng bỏ trống cột "Ghi chú" — đề nghị điền "Đưa vào KH Trường" hoặc "Thường xuyên của đơn
>    vị" cho từng dòng để P-THHC lọc đúng nhiệm vụ lên báo cáo cấp Trường.
> 8. **Khoa Y - Dược, Phòng TCCB&CTHSSV, Khoa ĐT&SHLX**: các tệp Phụ lục Ib còn giữ nguyên **sheet mẫu Phụ
>    lục Ia (kế hoạch Quý)** chưa điền/chưa xóa trong cùng workbook — đề nghị xóa sheet thừa trước khi nộp;
>    riêng Khoa Y - Dược, tệp Phụ lục IIb cũng còn sheet mẫu Phụ lục IIc (báo cáo Quý) chưa xóa.
>
> P-THHC không tự sửa số liệu của đơn vị. Đề nghị các đơn vị đối chiếu bảng chi tiết và nộp lại bản đã sửa,
> ghi rõ phiên bản (v2, v3…) để tránh nhầm với bản cũ.

---

## Kết thúc — khối 6 mục

**Trạng thái**: `CAN_BO_SUNG` (hồ sơ chung của kỳ) — nhiều tệp đơn lẻ ở mức `TRẢ_LẠI`/`KHONG_DAT` cho việc
tổng hợp ngay, một số tệp `DAT`; 3 đơn vị/nhóm còn thiếu hồ sơ (`CAN_BO_SUNG`).

**Nguồn đã đối chiếu**:
- `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/1. BAO CAO PL IIB/` (10 tệp `.xlsx`), `2. BAO CAO IIA/` (10 tệp `.docx`),
  `2. Phu luc Ib/` (9 tệp `.xlsx`) — đọc trực tiếp byte thật từng tệp (openpyxl/python-docx), không suy diễn
  từ tên tệp.
- `25-KTC-Bao-Cao/references/Skill-Library/31-Skill-Phu-Luc-TB736-Excel.md`,
  `32-Skill-Thu-Thap-Bao-Cao-Don-Vi.md`, `read_bc736_excel.py` (v3.3).
- `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` (bảng mã đơn vị, quyết định Ban Truyền thông 14/9/2026).
- `29-Cong-Cu/doi_soat_so_lieu.py`, `29-Cong-Cu/kiem_the_thuc.py`.
- Không có tệp tổng hợp cấp Trường của kỳ này để chạy DS02 — chưa đối chiếu được bước đó.

**Kiểm tra đã chạy**: đúng mẫu Ia/Ib/IIb/IIc theo cấu trúc cột và tiêu đề; đủ ô bắt buộc (Trục, Ghi chú, Đơn
vị); công thức KPI cascade toàn bộ 6 bước (Hệ số, SL quy đổi, 3 KPI TT/QĐ) cho mọi dòng IIb; đối chiếu Ghi
chú với 4 giá trị hợp lệ (Ib); mã đơn vị theo bảng chuẩn (DS06); Task_ID trùng (DS04 — không áp dụng, chưa có
cột); đối chiếu 13 đầu mối bắt buộc; thể thức TT/TX (`kiem_the_thuc.py`) cho cả 29 tệp; kiểm tay phần đầu mỗi
tệp (đơn vị, kỳ, số sheet) để phát hiện sheet mẫu thừa và sai kỳ.

**Kiểm tra chưa chạy**:
- Đối soát Task_ID với Master Task Register (`21-Master-Task-Register/`) — kỳ này các tệp chưa có cột
  Task_ID nên không áp dụng được.
- DS02 (truy vết tổng hợp cấp Trường) — chưa có tệp tổng hợp cấp Trường của kỳ 9/2026 để so.
- DS03 (KH↔KQ cùng kỳ) — không áp dụng được vì Ib (KH tháng 10) và IIb (KQ tháng 9) khác kỳ theo đúng thiết
  kế chu kỳ nộp; chưa có KH tháng 9 (đã nộp ở kỳ 8/2026, ngoài phạm vi thư mục đang kiểm) để đối chiếu chéo
  với KQ tháng 9 hiện tại.
- Đối chiếu nội dung Phụ lục IIa (văn tường thuật) với số liệu Phụ lục IIb cùng đơn vị (khớp Trục, khớp số
  nhiệm vụ) — ngoài phạm vi 5 phép kiểm được giao, cần thêm một lượt riêng nếu cần.
- Xác minh minh chứng đính kèm từng nhiệm vụ — thuộc phạm vi agent `ktc-xac-minh-minh-chung`.

**Mã cảnh báo**: `NGHI_CHI_DAN_TRONG_DU_LIEU` — không có; `DOI_CHIEU_GAN_DUNG` — không dùng (đối chiếu mã
đơn vị theo DS06 là khớp chính xác, không gần đúng); `THIEU_DU_LIEU` — có (P-QLDT thiếu hoàn toàn 3 loại;
K-KTNL thiếu IIb+Ib; P-THHC thiếu IIa+Ib cấp Phòng; DT-CDCS/DT-DTN thiếu hoàn toàn; DS02 không chạy được vì
thiếu tệp tổng hợp cấp Trường); `FORMAT_BINARY_UNVERIFIED` — không, đã đo được thật bằng `kiem_the_thuc.py`;
`THANG_DIEM_CHUA_PHAN_DINH` — không (DS05 không báo lệch thang); `MA_DON_VI_KHONG_HOP_LE` — không (DS06 sạch,
nhưng `DT-CDCS`/`DT-DTN` là mã tạm theo KI-015, chưa chốt chính thức — không tính là "không hợp lệ" mà là
"chưa chuẩn hoá").

**Việc người có thẩm quyền quyết**:
1. Xác nhận có chấp nhận tổng hợp các tệp "ĐỦ ĐIỀU KIỆN TỔNG HỢP" ngay, tách riêng phần "TRẢ LẠI" chờ đơn vị
   sửa, hay giữ nguyên cả kỳ chờ đủ hồ sơ mới tổng hợp.
2. Quyết định cách xử lý 3 đầu mối thiếu hồ sơ (P-QLDT, K-KTNL, P-THHC cấp Phòng ở IIa/Ib) — đôn đốc nộp bổ
   sung trong kỳ này hay ghi nhận "nộp muộn" chuyển kỳ sau.
3. Chốt chính thức mã `DT-CDCS`/`DT-DTN` (KI-015) để không còn là mã tạm khi đối chiếu 13 đầu mối các kỳ sau.
4. Quyết định có cần đơn vị nộp lại `BAN TT.docx` (bản đúng kỳ 9/2026) trước khi dùng bản 8/2026 hiện có cho
   bất kỳ mục đích nào.
