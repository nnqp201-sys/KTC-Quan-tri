# LỆNH THỰC HIỆN — Nâng cấp skill `ktc-kpi-tu-danh-gia` và dựng quy trình hồ sơ minh chứng xếp loại

**Gửi**: Claude Code (VS Code/Desktop), làm việc trong thư mục dự án `KTC-Quan-tri`
**Người giao**: Phòng TH-HC&QT, Trường Cao đẳng Kon Tum
**Ngày lập**: 28/10/2026
**Nối tiếp**: `30-Ket-Qua/2026-09-25/De-xuat/LENH-Xay-skill-KPI-giai-doan-2-Tu-danh-gia.md` (skill
`ktc-kpi-tu-danh-gia` v1.3, nguồn `28-KTC-KPI/Tu-Danh-Gia/`).
**Căn cứ phát sinh**: phiên làm hồ sơ minh chứng xếp loại Quý III/2026 theo TB 1105/TB-CĐKT (30/9/2026) cho
Nguyễn Ngọc Quang Phục và Đỗ Thành Công (thư mục `30-Ket-Qua/2026-10-01/KPI-ca-nhan/Ho-so-ra-soat-Q3-*`).
**Phạm vi dùng thật**: toàn thể Lãnh đạo, viên chức, người lao động của Trường — không riêng P-THHC. Mọi ví dụ,
quy ước cứng theo một đơn vị hay một người là lỗi thiết kế.

---

## 0. Vai trò và nguyên tắc

Bạn là kỹ sư nâng cấp skill. Bạn không chấm điểm, không xếp loại, không quyết định thay người có thẩm quyền; bạn
làm công cụ để người dùng tự đánh giá **đúng, nhất quán, có căn cứ**.

1. Đọc trước: `CLAUDE.md`, `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`, `92-Kinh-Nghiem/05-Known-Issues/Pending.md`,
   `20-Chuan-Chung/19-Quy-Tac-KPI.md`, `28-KTC-KPI/Tu-Danh-Gia/SKILL.md`.
2. Mọi quy tắc dẫn nguồn dạng `[QĐ 1923, Đ19.1]` hoặc `[TB 1105, mục 2.2]`. Không nguồn thì không thành quy tắc;
   ghi vào `references/Cau-Hoi-Mo.md`.
3. Mọi phép tính, ngưỡng, kiểm tra nhất quán làm bằng script có ca thử trong
   `92-Kinh-Nghiem/02-Regression/Cases/`. Không để mô hình tự nhẩm.
4. Không sửa biểu mẫu chính thức trong `assets/`. Sửa nguồn rồi đóng gói lại; sau mỗi lần sửa chạy
   `python 29-Cong-Cu/kiem_tra_he_thong.py` và các ca hồi quy; không sửa `31-Plugin/` bằng tay.
5. **Không có "đã xong" nếu chưa đọc lại tệp đầu ra.** Mỗi sản phẩm sinh ra phải được mở lại, đếm dòng, quét chuỗi
   cấm (mục 3.4) trước khi báo cáo.
6. Mọi thay đổi số liệu giữa các lần chạy phải ghi lịch sử (giá trị cũ, lý do, căn cứ, người đổi) — nguyên tắc 5
   của dự án.

---

## 1. Bài học từ phiên Quý III/2026 (nền của lệnh này)

| # | Sự cố thật | Nguyên nhân gốc | Hướng xử lý (mục) |
|---|---|---|---|
| 1 | B25 (mua thuốc PKĐK) khai "Hoàn thành đúng hạn" nhưng % tiến độ chỉ 75, SL 5/7; công cụ vẫn tính "12/12 đúng hạn" | `danh-gia` tin trường "Kết quả nhiệm vụ" mà không đối chiếu với %, SL | 2.1 |
| 2 | Câu C08 (Có/Không) khiến cả 3 mức xếp loại "Không đạt" chỉ vì 1/23 việc chưa trọn | Điều kiện nhị phân do người trả lời tay, không suy từ dữ liệu việc | 2.1, 2.2 |
| 3 | Cùng một việc ở hai hồ sơ (Phục B25, Công đợt 2/đợt 3) lệch số liệu; điểm Phục đổi 97,20 → 100 → 97,20 | Không có nguồn duy nhất; không đối chiếu chéo; không ghi lịch sử đổi | 2.5, 4.1 |
| 4 | `sinh-bang-hoi` báo `KeyError` với mẫu Phụ lục II/VII của Công | Chỉ dò được 6 mẫu chuẩn; không nhận diện mẫu lạ | 2.3 |
| 5 | "Vượt mức" không có trường dữ liệu; phải suy từ tính chất việc; người dùng không có cột ngày hoàn thành thực tế | Bảng hỏi thiếu ngày thực tế, căn cứ vượt mức | 2.2 |
| 6 | Bảng tra minh chứng khớp sai (khóa số với khóa chuỗi) → hàng loạt dòng "CẦN BỔ SUNG"; báo "đã đầy đủ" khi chưa đọc lại tệp | Không có ca thử; không quy trình đọc lại | 3.3, 3.4 |
| 7 | Chữ "DỰ THẢO", "em đã…" lọt vào bảng sẽ nộp TCCB | Không tách bản nội bộ và bản nộp | 3.2 |
| 8 | python-docx ghi độ rộng cột sai đơn vị (EMU thay vì twips); hook bắt cỡ chữ bảng ≠ 14 (TT04) và thiếu dàn đều (TT06); openpyxl làm mất dropdown mở rộng của mẫu import | Script viết rời, ném ở thư mục tạm | 3.1 |

---

## 2. Việc 1 — Nâng cấp `kpi_danh_gia.py` và bảng hỏi (ưu tiên cao nhất)

### 2.1 Bộ kiểm nhất quán (`kiem_nhat_quan`, mã `NQ01`–`NQ10`)

Thêm lệnh con `kiem-nhat-quan` và tự chạy trong `danh-gia`. Mức: **LỖI** chặn xuất sản phẩm chính thức (mã thoát
2), **CẢNH_BÁO** vẫn xuất nhưng ghi trong bảng điều kiện.

| Mã | Kiểm | Mức |
|---|---|---|
| NQ01 | "Kết quả nhiệm vụ" = *Hoàn thành đúng hạn* hoặc *Vượt mức* nhưng % tiến độ < 100 hoặc SL thực < SL kế hoạch | LỖI |
| NQ02 | "Hoàn thành chậm tiến độ" nhưng % tiến độ = 100 | CẢNH_BÁO |
| NQ03 | "Vượt mức" mà không có **căn cứ vượt mức** (loại + số liệu) — theo TB 1105 mục 2.3 | LỖI |
| NQ04 | Tỷ lệ việc vượt mức < 30% khi người dùng tự đề xuất HTXS [TB 1105, mục 2.2] | LỖI |
| NQ05 | Việc "vượt mức" có ngày hoàn thành thực tế muộn hơn thời hạn | LỖI |
| NQ06 | Còn chuỗi cấm trong bản nộp (mục 3.4) | LỖI |
| NQ07 | Việc không có số hiệu minh chứng và không ghi lý do "không yêu cầu minh chứng" | CẢNH_BÁO |
| NQ08 | Tổng % theo Trục lệch quá 0,01 so với công thức mẫu sau khi chặn trần | LỖI |
| NQ09 | Mức tự đề xuất cao hơn mức theo ngưỡng điểm | CẢNH_BÁO |
| NQ10 | Điều kiện C08 khai "Có" nhưng có việc chưa 100% | CẢNH_BÁO (nêu cả hai, không tự chọn) |

### 2.2 Bảng hỏi mới

- **Sheet B**, thêm cột: *Ngày hoàn thành thực tế*, *Loại vượt* (số lượng / chất lượng / tiến độ / hiệu quả, chọn từ
  danh sách), *Căn cứ vượt mức (số liệu cụ thể)*, *Lý do chưa đạt 100%* (khách quan / chủ quan + mô tả),
  *Số hiệu văn bản minh chứng*, *Nơi lưu minh chứng*.
- **Sheet C**: C08 và C09 **tự suy** từ sheet B (số việc trọn 100% / tổng; danh sách việc chưa trọn kèm lý do) và
  chỉ hỏi người dùng **xác nhận hoặc nêu ngoại lệ**, không hỏi lại từ đầu. Khi có ngoại lệ khách quan, ghi nguyên văn
  lý do vào bảng điều kiện. Nêu rõ trong tài liệu skill: điều kiện "đơn vị, lĩnh vực hoàn thành 100%" của QĐ 1923
  Đ19.1 áp **cho cả ba mức** — một việc chưa trọn có thể kéo cả ba mức xuống; **không tự gỡ**, chuyển người có
  thẩm quyền (ghi Câu hỏi mở).
- Giữ tương thích ngược: bảng hỏi cũ (v1.3) vẫn đọc được, cột mới để trống thì cảnh báo thay vì lỗi.

### 2.3 Nhận diện mẫu lạ

- Trước khi `cau_truc()` chạy, nhận diện mẫu: 6 mẫu chuẩn (theo `assets/`) hay mẫu **Phụ lục II + Phụ lục VII**
  (cột "Người trực tiếp chỉ đạo / Người phối hợp / Đơn vị tham mưu", sheet `Ke Hoach / KPI / Danh Gia`, số dòng mỗi
  Trục không cố định).
- Mẫu lạ: **không chạy `sinh-bang-hoi`**; in thông báo rõ "mẫu Phụ lục II/VII — chưa hỗ trợ tự động" thay vì
  `KeyError`.
- Tùy chọn (làm nếu đủ thời gian): viết `doc_mau_phu_luc_vii()` đọc mẫu này để chạy được `kiem-nhat-quan` và dựng
  bảng tổng hợp minh chứng; dùng tệp thật của Đỗ Thành Công
  (`30-Ket-Qua/2026-10-01/KPI-ca-nhan/Ho-so-ra-soat-Q3-DT.Cong/TDG-KPI-Q3-2026_Do-Thanh-Cong.xlsx`) làm ca thử.
- Ghi vào `Known-Issues-Bieu-Mau.md` các mục mới: mẫu Phụ lục II/VII; công thức `R8` dùng Calibri 13 (TX02);
  ô số thứ tự dạng chuỗi lẫn số trong cùng cột.

### 2.4 Ca thử bắt buộc (`test_kpi_nhat_quan.py`)

Ít nhất: (a) B25 khai "đúng hạn" với 75% → NQ01 LỖI; (b) 7/23 vượt mức không căn cứ → NQ03; (c) 8/30 → NQ04;
(d) bảng hỏi cũ v1.3 vẫn đọc được; (e) mẫu Phụ lục II/VII → thông báo rõ, mã thoát 2, không `KeyError`.

### 2.5 Đối chiếu chéo hồ sơ (cơ sở cho agent mục 4.1)

Viết `29-Cong-Cu/kpi_doi_chieu_cheo.py`: nhận nhiều bảng hỏi/TDG, gom theo **số hiệu văn bản** và theo **nội dung
việc chuẩn hóa**, báo các việc xuất hiện ở ≥2 hồ sơ mà SL thực tế, % hoặc kết quả khác nhau. Đầu ra bảng Markdown
và CSV. Không tự sửa.

---

## 3. Việc 2 — Bộ dựng hồ sơ minh chứng chuẩn

### 3.1 Script dùng lại

Viết `29-Cong-Cu/lap_ho_so_minh_chung.py` (thay các script rời đã dùng ở thư mục tạm của phiên 1/10):
- Đầu vào: TDG (.xlsx) + bảng hỏi (.xlsx) + bảng tra minh chứng (CSV: `ma_viec, so_hieu, nguon`).
- Đầu ra `.docx` theo thể thức `the-thuc`: A4, lề 2-2-3-2, Times New Roman **14 cho mọi chữ kể cả trong bảng**, đoạn
  nội dung dàn đều hai lề và thụt đầu dòng 1,25 cm, số trang giữa lề trên và ẩn ở trang 1, bảng cố định độ rộng
  (twips = `Cm(w).twips`, không dùng EMU), dòng tiêu đề lặp lại mỗi trang, dòng không bị tách trang.
- Nội dung: thông tin cá nhân; bảng đối chiếu điều kiện TB 1105 mục 2.2 (a/b theo chức vụ); bảng danh mục việc và
  minh chứng; ghi chú; ký.

### 3.2 Hai bản đầu ra

- **Bản nội bộ**: có cờ `CẦN XÁC NHẬN`, `SUY LUẬN`, `THIẾU DỮ LIỆU`, kèm nguồn từng ô.
- **Bản nộp**: sạch, chỉ sinh được khi không còn cờ; nếu còn thì dừng và in danh sách ô chưa xử lý.

### 3.3 Ca thử (`test_lap_ho_so_minh_chung.py`)

Khóa tra cứu **chuẩn hóa kiểu** (luôn `int` hoặc luôn `str`); ca thử với dữ liệu có `stt` lẫn chuỗi và số (như tệp
của Công: `'1'` … `3`). Ca thử đọc lại `.docx`, đếm dòng bằng số việc đầu vào, không còn ô trống.

### 3.4 Quy trình đọc lại bắt buộc trước khi báo "xong"

Thêm vào `SKILL.md` một mục "Kiểm đầu ra": mở lại tệp, đếm dòng/số việc, quét chuỗi cấm (`CẦN BỔ SUNG`, `DỰ THẢO`,
`em đã`, `TODO`, `[CẦN`) trong bản nộp, chạy `kiem_the_thuc.py` (0 lỗi Mức 1–2), rồi mới báo kết quả.

---

## 4. Việc 3 — Sub-agent (làm sau khi xong mục 2–3)

Đặt nguồn trong `29-Cong-Cu/plugin_src/agents/`, dựng qua `dong_goi_plugin.py`. Mỗi agent **chỉ đọc**, không sửa
tệp, mô tả ≤ 1024 ký tự, ghi rõ "không kết luận thay người có thẩm quyền".

1. **`ktc-doi-chieu-ho-so-cheo`** — dùng `kpi_doi_chieu_cheo.py`; báo lệch giữa các hồ sơ cùng việc (ca B25 làm
   mẫu); nêu đủ các bên, không chọn bên nào.
2. **`ktc-kiem-ho-so-tdg`** — kiểm độc lập sau khi sinh (kiểu "người soạn không tự chấm bài"): đọc lại xlsx/docx,
   chạy NQ01–NQ10, thể thức, so với nguồn.
3. **`ktc-ho-so-xep-loai-don-vi`** (giai đoạn 3) — tổng hợp cấp đơn vị: trần HTXS không quá 20% số HT tốt trở lên
   theo nhóm tương đồng [TB 1105, mục 1.3; QĐ 1923, Đ19.2]; người đứng đầu không cao hơn tập thể [Đ14.4, Đ19.4];
   tập thể HTXS cần 100% viên chức HT và ≥80% HT tốt [TB 1105, mục 2.1d]; danh sách trường hợp vi phạm, giải trình
   cần rà soát [mục 4]. Đối chiếu Phụ lục tổng hợp PL II của CV 694 (đã có trong kho).
4. Mở rộng agent **`ktc-xac-minh-minh-chung`** (đã có) để khớp việc với số hiệu trong "Văn bản đã xử lý" xuất từ
   QLVB&ĐH, ghi mức tin cậy từng cặp; **không tự điền số hiệu khi chỉ suy từ nội dung gần giống**.

Mỗi agent có ca thử mô phỏng (dữ liệu giả, không dùng điểm thật của người).

---

## 5. Quy trình và ghi nhận (làm song song)

1. **Nguồn duy nhất**: đề xuất quy ước — mỗi người một "danh mục việc đã làm của quý" từ xuất QLVB&ĐH, làm nguồn
   chung cho kế hoạch, tự đánh giá, minh chứng. Việc của Công tính cho Phục (`memory: kpi-phuc-gom-viec-do-thanh-cong`)
   được **liên kết** bằng cột "người thực hiện / người phối hợp", không gõ lại. Viết thành đề xuất
   `30-Ket-Qua/2026-10-28/De-xuat/` để Trưởng phòng duyệt, chưa áp dụng.
2. **Gom minh chứng hằng tháng** vào chu trình báo cáo tháng (khi nộp PL KPI tháng, cột minh chứng đã có số
   hiệu), để hồ sơ cuối quý không dồn vào ngày có TB như TB 1105.
3. **Decision Log** `DL-20261028-00x`: ghi quyết định cho ba điểm — C08 áp cho cả ba mức; không tự suy "vượt mức";
   bản nộp chỉ sinh khi sạch cờ. Kèm lịch sử đổi điểm Phục 97,20 → 100 → 97,20 làm minh họa.
4. **TRI-THUC / Known-Issues**: ghi các bài học kỹ thuật ở bảng mục 1 (twips/EMU; khóa chuỗi/số; mất dropdown x14
   khi openpyxl lưu — sửa XML trực tiếp; heredoc Bash — viết script ra tệp). Chạy agent `ktc-tu-hoc` xử lý 49 tín
   hiệu học còn treo.

---

## 6. Điều kiện dừng — hỏi người giao, không tự quyết

- Khi cần chốt cách hiểu điều kiện "hoàn thành 100%" của Đ19.1 (cho cả ba mức hay theo từng mức) — nêu cả hai cách
  hiểu, ghi Câu hỏi mở, chờ P-TCCB.
- Khi phải đổi số liệu thật của một người để cho khớp — dừng, hỏi.
- Khi mẫu lạ khác Phụ lục II/VII xuất hiện — báo, không đoán cấu trúc.

## 7. Tiêu chí hoàn thành

- `python 29-Cong-Cu/kiem_tra_he_thong.py` mã thoát 0; các ca hồi quy mới (mục 2.4, 3.3) đạt.
- Chạy lại hồ sơ Phục (mẫu chuẩn): NQ01 bắt B25 khi khai sai; bảng hỏi mới đủ cột; bản nộp sạch.
- Mẫu Phụ lục II/VII: thông báo rõ, không `KeyError`.
- Gói `ktc-kpi-tu-danh-gia` đóng lại bằng `dong_goi_kpi.py` (tăng phiên bản, ghi `CHANGELOG`), nguồn ở
  `28-KTC-KPI/Tu-Danh-Gia/`.
- Đầu ra cuối: khối 6 mục (Trạng thái · Nguồn đã đối chiếu · Kiểm tra đã chạy · Chưa chạy · Mã cảnh báo · Việc người
  có thẩm quyền quyết).

## 8. Ngoài phạm vi lượt này

Hệ thống chấm tự động xếp loại; sửa kết quả đã chốt của Phục, Công; xếp loại tập thể (chỉ dựng agent hỗ trợ, không
kết luận); nạp dữ liệu lên phần mềm KPI tỉnh.
