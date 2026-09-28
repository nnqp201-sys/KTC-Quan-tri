# Bảng kiểm theo đơn vị — Kỳ tháng 9/2026 (kết quả T9 + kế hoạch T10)

Nguồn: `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/` (29 tệp). Kiểm bằng `read_bc736_excel.py` v3.3 +
`kiem_the_thuc.py` qua agent `ktc-kiem-ho-so-don-vi`, báo cáo đầy đủ (vị trí dòng/cột cụ thể):
`30-Ket-Qua/2026-09-28/Kiem-Ho-So/2026-09/Kiem-ho-so_2026-09.md`.

| Mã đơn vị | Tên đơn vị | IIb (KQ, có KPI) | IIa (tường thuật) | Ib (KH tháng 10) | Kết luận | Lý do chính |
|---|---|---|---|---|---|---|
| P-TCCB | Phòng Tổ chức cán bộ và CT HSSV | Có, 0 lỗi CT | Có, 0 lỗi | Có | **TRẢ LẠI** (Mức 2) | IIb: ô "ĐƠN VỊ:" đầu trang bỏ trống |
| P-QLDT | Phòng Quản lý Đào tạo và BĐCL | **THIẾU** | **THIẾU** | **THIẾU** | **THIẾU HỒ SƠ** | Không có tệp nào ở cả 3 loại |
| P-THHC | Phòng TH-HC&QT (cấp Phòng) | Có, 0 lỗi (`P.THHCQT.xlsx`) | **THIẾU** (chỉ có Ban TT, sai kỳ T8) | **THIẾU** (chỉ có Ban TT) | **TRẢ LẠI + THIẾU** | IIa/Ib chưa có bản đứng tên Phòng; `BAN TT.docx` nộp nhầm bản tháng 8 |
| P-QLKH | Phòng QLKHCN&HTPT | Có, 1 lỗi CT | Có, 0 lỗi | Có, 0 lỗi | **TRẢ LẠI** (Mức 2) | IIb dòng "Tham dự Hội nghị tập thể nhân sự…": KPI CL-QĐ sai (ghi 1.0, đúng 0.3) |
| P-TCKT | Phòng Tài chính - Kế toán | Có, 7 lỗi CT | Có, 0 lỗi | Có, 3 Ghi chú sai + 1 lỗi CT | **TRẢ LẠI** (Mức 2) | Nhiều lỗi Hệ số/SL quy đổi/KPI; Ghi chú "Kế hoạch của Trường" không hợp lệ |
| K-KHCB | Khoa các Khoa học cơ bản | Có, 0 lỗi CT | Có, 0 lỗi | **TRẢ LẠI** (14/14 Ghi chú trống) | TRẢ LẠI một phần (Ib) | Ib: toàn bộ 14 dòng bỏ trống cột Ghi chú |
| K-SUPH | Khoa Sư phạm | Có, 0 lỗi CT | Có, 0 lỗi | **TRẢ LẠI** (6/6 Ghi chú trống) | TRẢ LẠI một phần (Ib) | Ib: toàn bộ 6 dòng bỏ trống cột Ghi chú |
| K-KTNL | Khoa Kinh tế và Nông Lâm | **THIẾU** | Có, 0 lỗi | **THIẾU** | **THIẾU HỒ SƠ** | Chỉ có Phụ lục IIa; thiếu IIb (không tính được KPI) và Ib |
| K-KTCN | Khoa Kỹ thuật và Công nghệ | Có, 0 lỗi CT | Có (góp ý Mức 3: màu chữ) | Có, 0 lỗi | **ĐỦ ĐIỀU KIỆN** | Không còn lỗi cấu trúc của kỳ trước — đã kiểm chứng lại độc lập |
| K-YDUOC | Khoa Y - Dược | **TRẢ LẠI** (sheet mẫu IIc thừa) | Có, 0 lỗi | **TRẢ LẠI** (15/16 Ghi chú trống + sheet mẫu Ia thừa) | **TRẢ LẠI** (Mức 2) | Còn sheet mẫu chưa xóa; thiếu Ghi chú hầu hết các dòng Ib |
| K-DTSHLX | Khoa Đào tạo và Sát hạch lái xe | Có, 0 lỗi CT | Có, 0 lỗi | **TRẢ LẠI** (15/32 Ghi chú trống + sheet mẫu Ia thừa) | TRẢ LẠI một phần (Ib) | Ib: 15/32 dòng bỏ trống Ghi chú; còn sheet mẫu Phụ lục Ia thừa |
| DT-CDCS | Công đoàn cơ sở (mã tạm, KI-015) | THIẾU | THIẾU | THIẾU | **THIẾU HỒ SƠ** | Không có tệp nào — mã chưa chốt chính thức |
| DT-DTN | Đoàn TN – Hội SV (mã tạm, KI-015) | THIẾU | THIẾU | THIẾU | **THIẾU HỒ SƠ** | Không có tệp nào — mã chưa chốt chính thức |

## Tóm tắt

- **Đủ điều kiện tổng hợp hoàn toàn**: chỉ 1/13 đơn vị (K-KTCN).
- **Trả lại đơn vị** (còn lỗi Mức 1–2 ở ít nhất 1 loại tệp): P-TCCB, P-THHC, P-QLKH, P-TCKT, K-KHCB, K-SUPH, K-YDUOC, K-DTSHLX (8/13).
- **Thiếu hồ sơ hoàn toàn hoặc một phần lớn**: P-QLDT (thiếu cả 3 loại), K-KTNL (thiếu IIb+Ib), P-THHC (thiếu IIa+Ib cấp Phòng), DT-CDCS, DT-DTN (4–5/13, một phần trùng với nhóm trả lại).
- **Lỗi Mức 1 (nghiêm trọng)**: `BAN TT.docx` (IIa) — sai kỳ hoàn toàn, ghi "tháng 8/2026" thay vì "tháng 9/2026".

## Kết luận

Trạng thái: `CAN_BO_SUNG`. Số liệu KPI theo 6 Trục ở phụ lục Excel tổng hợp kèm theo cộng dồn **cả 10 đơn vị đã
nộp Phụ lục IIb**, **CHƯA loại trừ** các dòng sai công thức của BAN TT, P-QLKH, P-TCKT (xem cột Ghi chú trong
phụ lục Excel) và **KHÔNG bao gồm** P-QLDT, K-KTNL (chưa nộp Phụ lục IIb) — dùng để tham khảo mức độ hoàn
thành chung, không dùng chấm KPI chính thức. Dự thảo báo cáo Word cấp Trường chỉ đưa số liệu Trục vào phần
tường thuật với ghi chú rõ đơn vị nào bị loại trừ khỏi từng con số, và **chưa qua rà soát `KTC-Ra-Soat-897`**
— bắt buộc rà soát và giải quyết đủ hồ sơ/lỗi Mức 1–2 nêu trên trước khi trình ký (Nguyên tắc 9, CLAUDE.md).

**Nguồn đã đối chiếu**: 29 tệp `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/` (đọc trực tiếp byte thật) ·
`KH-834_Ke-hoach-cong-tac-thang-9-2026_20260906_v1.xlsx` (kho `KTC-Database/02-KTC-Regulations`) ·
`PL-375`/`BC-375` (kết quả tháng 8, kỳ trước, kho `KTC-Database`) · `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`.

**Mã cảnh báo**: `THIEU_DU_LIEU` (P-QLDT, K-KTNL, P-THHC cấp Phòng, DT-CDCS, DT-DTN) ·
`DOI_CHIEU_GAN_DUNG` (đối chiếu kế hoạch KH-834 cấp Trường với kết quả đơn vị — chưa có cột Task_ID, KI-001,
chỉ đối chiếu được gần đúng theo Trục, không khớp từng nhiệm vụ) · `THANG_DIEM_CHUA_PHAN_DINH` — không phát
sinh (DS05 không báo lệch thang, KI-014 đã có QĐ 2119 phân định căn cứ).

**Việc người có thẩm quyền quyết** (P-THHC tổng hợp trình): (1) chấp nhận tổng hợp ngay phần đủ điều kiện
hay chờ đủ hồ sơ cả kỳ; (2) đôn đốc P-QLDT, K-KTNL, P-THHC(cấp Phòng) nộp bổ sung trong kỳ này hay chuyển
"nộp muộn" kỳ sau; (3) chốt mã chính thức `DT-CDCS`/`DT-DTN` (KI-015); (4) có bắt đơn vị nộp lại
`BAN TT.docx` đúng kỳ 9/2026 trước khi dùng cho bất kỳ mục đích nào.
