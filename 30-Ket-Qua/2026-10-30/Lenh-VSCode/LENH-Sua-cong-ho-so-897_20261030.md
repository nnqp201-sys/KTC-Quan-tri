# LỆNH: Sửa cổng hồ sơ KTC-Ra-Soat-897 để không bắt người dùng gửi lại văn bản hệ đã có

- **Người giao:** Trưởng phòng TH-HC&QT (P-THHC)
- **Ngày giao:** 30/10/2026
- **Dự án:** `D:\.CLAUDE code\KTC-Quan-tri`
- **Mã sự cố:** KI-021 (`92-Kinh-Nghiem/05-Known-Issues/Pending.md`)
- **Phạm vi được phép:** sửa **lõi** `2A-KTC-Ra-Soat-897/ktc-ra-soat-897/` (người giao cho phép tại lệnh này), lớp ngoài `29-Cong-Cu/`, ca thử `92-Kinh-Nghiem/02-Regression/Cases/`.
- **Không được:** ghi vào KTC-Database (kho chỉ đọc, hook chặn); hạ chuẩn chặn ảnh/scan (G1); đổi bảng mã, mức, nhãn trình ký; xóa tệp gốc.

---

## 1. Bối cảnh

Ngày 30/10/2026, chạy rà soát chính thức 897 (v4.5) trên Báo cáo thuyết minh phương án sắp xếp CSGDNN (36 trang, kèm Phụ lục I, II). Cổng hồ sơ (`tools/kiem_ke_ho_so.py`, Bước 1) **CHẶN**: 48 văn bản bị báo "thiếu toàn văn", đề nghị người dùng gửi lại. Phần lớn văn bản đó **đã có trong KTC-Database** hoặc người dùng đã cung cấp trong phiên. Việc bắt gửi lại là bất cập, phải sửa.

Tệp tái hiện: `30-Ket-Qua/2026-10-29/Bao-cao/BC_Thuyet-minh-phuong-an-sap-xep-CSGDNN_Truong-CDKT_20261029_v8_ban-sach.docx` (bản đã trình — chỉ dùng để thử, **không sửa**).

## 2. Chẩn đoán đã đo (đừng đoán lại, kiểm lại bằng lệnh ở mục 6)

| # | Nguyên nhân | Vị trí | Bằng chứng |
|---|---|---|---|
| N1 | Regex `SO` không cho khoảng trắng quanh `/` → "Số: 287 /QĐ-UBND", "Số: 175 /BC-CĐKT", "Số: 657 /QĐ-CĐKT" không tạo được khóa | `kiem_ke_ho_so.py` dòng ~147 (`SO`), `ma_dinh_danh()` dòng ~429 | `ma_dinh_danh()` trả `set()` cho QĐ 287, BC 175; trả đúng cho 153, 464, 295, 339, NQ 42 (không có dấu cách) |
| N2 | Dự thảo dùng `<w:noBreakHyphen/>` → `_ptext()` chỉ lấy `w:t`, `w:tab`, `w:br`, **bỏ mất gạch** → "5394/SGDĐT-GDNNQLĐT" đọc thành "5394/SGDĐTGDNNQLĐT", không khớp tệp nguồn | `_ptext()` dòng ~44 | 14 `noBreakHyphen` trong BC v8; cổng ghi khóa `5394/SGDDTGDNNQLDT`, `7056/VPNC`, `635/QĐLĐTBXH` |
| N3 | Cổng chỉ tra **hồ sơ + kho nội bộ 36 văn bản** (`references/Kho-Du-Lieu-897/kho_manifest.json`), **không tra KTC-Database** | khối "đối chiếu văn bản được đề cập" dòng ~703–768 | Văn bản có trong KTC-Database (QĐ 287, BC 175, GCN 57...) vẫn "THIẾU" khi chưa chép vào hồ sơ |
| N4 | Văn bản trong kho chỉ có bản PDF scan (QĐ 1671, QĐ 543, QĐ 335, QĐ 417) → nếu chép vào hồ sơ thì bị chặn G1 | khối kiểm định dạng dòng ~500–532 | Gom thử: 335, 417 chép vào → "PDF không có lớp chữ" |
| N5 | Không phân biệt **căn cứ / viện dẫn trong lời văn** với **văn bản chỉ dẫn trong bảng số liệu, phụ lục thống kê** (hợp đồng, kế hoạch tiếp nhận người học ở Phụ lục II) → mọi số hợp đồng đều đòi toàn văn | `trich_dan()` dòng ~297 | 15 hợp đồng, 2 kế hoạch, "TB 393" ở Phụ lục II bị đòi toàn văn |
| N6 | "Phụ lục 06" báo thiếu do câu "phụ lục **06 học sinh**" (số lượng, không phải số phụ lục) | regex `phụ lục\s+(?:số\s+)?([IVXLC]+\|\d+)\b` dòng ~665 | Ngữ cảnh: "HĐ Naseed… năm 2026 và phụ lục 06 học sinh." |
| N8 | Số hiệu **văn bản Đảng** khác chính quyền (HD 05-HD/VPTW): dạng `Số 25-NQ/TW`, `Số 12-BC/ĐU`, `Số 05-HD/VPTW` — **số – ký hiệu tên loại / cơ quan ban hành**, gạch nối sau số, không có năm, thường **không có dấu hai chấm** sau "Số"; cơ quan có thể dài (`UBKTTW`, `BTCTW`, `ĐUK`), có thể nhiều cấp (`HD/BTGTW`). Cổng hiện khớp chủ yếu theo mẫu chính quyền `số/ký hiệu tên loại-cơ quan` | `SO` (~147), regex phụ dòng ~319 (`\d{1,4}-[A-ZĐ]{1,6}/[A-ZĐ]{1,6}` — giới hạn 4 chữ số, 6 ký tự), `ma_dinh_danh()` (~429), `cung_loai()` (~292), `HAU_TO` | Chưa có ca thử cho văn bản Đảng; cần kiểm cả hai chiều: dự thảo chính quyền viện dẫn văn bản Đảng (vd "Nghị quyết số 19-NQ/TW") và dự thảo Đảng viện dẫn văn bản chính quyền |
| N7 | (lớp dự án, không phải lõi) Công cụ soạn của dự án **chèn** `noBreakHyphen` | `scratchpad/sua_bc_v2.py: tra_nbh()`, các script dùng `h()` | Nguồn gốc của N2 |

## 3. Việc phải làm

### 3.1. Sửa lõi `kiem_ke_ho_so.py` (N1, N2, N6)
1. **N2** – `_ptext()`: coi `w:noBreakHyphen` là `-`, `w:softHyphen` là chuỗi rỗng. Áp tương tự cho `kiem_tra_the_thuc.py`, `so_sanh_ban.py` nếu có hàm đọc riêng (rà toàn bộ `tools/`).
2. **N1** – Chuẩn hóa trước khi khớp `SO`: bỏ khoảng trắng kề `/` và `-` trong dòng "Số:" (`re.sub(r'\s*([/-])\s*', r'\1', …)`). Áp cho cả `ma_dinh_danh()` (tệp hồ sơ) và `trich_dan()` (viện dẫn trong dự thảo).
3. **N6** – Không coi là "nhắc phụ lục" khi sau số là danh từ đơn vị đếm (`học sinh|sinh viên|người|HSSV|trang|bản|…`). Viết danh sách đơn vị đếm thành hằng số, có chú thích.

4. **N8 – Số hiệu văn bản Đảng** (theo HD 05-HD/VPTW; đối chiếu `references/Skill-Library/29-Skill-Van-Ban-Dang.md` và kho văn bản Đảng của Skill trước khi viết regex):
   - Nhận dạng hai họ số hiệu **tách riêng**, không trộn một regex: (a) chính quyền `<số>/<năm>/<ký hiệu>` hoặc `<số>/<loại>-<cơ quan>`; (b) Đảng `<số>-<loại>/<cơ quan>[/<cơ quan cấp trên>]`.
   - `ma_dinh_danh()`: nhận dòng "Số 25-NQ/TW" **có hoặc không** dấu hai chấm, cho khoảng trắng quanh `-` và `/` (chuẩn hóa như N1); nới giới hạn số (≥ 5 chữ số) và độ dài ký hiệu cơ quan (≥ 8 ký tự, có `Đ`).
   - Khóa chuẩn hóa giữ **dấu phân cách gốc** để không trùng nhầm: `19-NQ/TW` ≠ `19/NQ-TW`; `99-QĐ/TW` (Đảng) ≠ `99/QĐ-TTg` (chính quyền).
   - `cung_loai()`, `HAU_TO`: bổ sung hậu tố tên loại văn bản Đảng (`NQ, QĐ, CT, KL, QC, QĐi, HD, BC, TTr, CV, TB, KH, CTr, ĐA, TT, BB…`) và cơ quan (`TW, VPTW, BTCTW, UBKTTW, BTGTW, TU, ĐU, ĐUK, CB…`); "Quy định số 208-QĐ/TW" là loại Quy định (ký hiệu `QĐ`) — không suy là Quyết định chính quyền.
   - Viện dẫn rút gọn chỉ có số ("Nghị quyết 19") vẫn theo quy tắc TH-03 (khớp **duy nhất** cùng loại; mơ hồ → chặn).
   - Không đổi quy tắc thể thức văn bản Đảng (HD 05) — chỉ sửa **nhận dạng số hiệu** ở cổng hồ sơ.

### 3.2. Tra KTC-Database (N3) – không chép kho, chỉ đọc
1. Thêm tham số `--kho-ngoai <thư mục>` (lặp được) và biến môi trường `KTC_DATABASE_DIR`; mặc định lấy qua `29-Cong-Cu/duong_dan.py: ktc_database()` nếu chạy trong dự án, im lặng bỏ qua nếu không tìm thấy (bản Team không có kho).
2. Lập chỉ mục khóa văn bản từ kho ngoài: đọc dòng "Số:" (đã chuẩn hóa N1) trong 40 đoạn đầu **và** tệp `METADATA_*.md` cạnh văn bản (trường "Số hiệu"/tên tệp chuẩn hóa `QD-287-QD-UBND_…`). Có bộ nhớ đệm (cache JSON theo mtime) để không đọc lại toàn kho mỗi lần.
3. Văn bản tìm thấy ở kho ngoài → trạng thái mới **"Có trong KTC-Database"** + đường dẫn; **không chặn**. Ghi đủ vào bảng I.7 của báo cáo (cột nguồn).
4. Bản PDF scan trong kho ngoài (N4): **không** chép vào hồ sơ (tránh G1); nếu kho có bản .docx/PDF có chữ cùng số thì dùng bản đó; nếu chỉ có scan → trạng thái **"Có trong KTC-Database – bản scan, đối chiếu thủ công"**, không chặn, nhưng mọi đối chiếu nội dung với văn bản này ghi "Chưa kiểm (bản scan)" ở I.8.

### 3.3. Phân loại văn bản chỉ dẫn trong bảng số liệu (N5)
1. Viện dẫn nằm **trong ô bảng** thuộc **Phụ lục / văn bản kèm theo** có tiêu đề thống kê (danh sách, tổng hợp, kết quả tiếp nhận...) và **không** đứng trong phần "Căn cứ" → trạng thái **"Chỉ dẫn số liệu – không đòi toàn văn"**; liệt kê ở I.8 để người ký biết chưa đối chiếu.
2. Viện dẫn trong lời văn thân dự thảo, phần căn cứ, kiến nghị → giữ nguyên quy tắc cũ (đòi toàn văn).
3. Không áp ngoại lệ này cho văn bản Đảng và cho dự thảo VBQPPL (giữ chặt).

### 3.4. Lớp dự án (N7) và công cụ gom
1. Bỏ việc chèn `noBreakHyphen` trong công cụ soạn: tìm mọi chỗ dùng `tra_nbh`, `h()` (U+2011 → `w:noBreakHyphen`) trong `29-Cong-Cu/` và script mẫu; sau Track Changes thì trả về gạch nối thường. Ghi chú vào `20-Chuan-Chung/15-Skill-Track-Changes.md`.
2. `29-Cong-Cu/gom_ho_so_897.py` (đã có bản thô 30/10): sau khi lõi tra được kho ngoài thì rút gọn thành công cụ **báo cáo** (liệt kê văn bản thiếu thật sự, gợi ý nơi có thể tìm), bỏ chép tệp. Giữ `--chuan-hoa-gach` cho dự thảo cũ.

### 3.5. Khóa lõi, đóng gói, tài liệu
1. Cập nhật `2A-KTC-Ra-Soat-897/LOI-V45.sha256` cho các tệp lõi đã sửa; ghi rõ **lệch bản Trường (TB 1206)** ở `2A-KTC-Ra-Soat-897/00-README.md` và `references/CHANGELOG.md` (mục "v4.5-ca-nhan.1 – 30/10/2026": nội dung, lý do KI-021, người giao).
2. Đóng gói lại bằng `29-Cong-Cu/dong_goi_ra_soat_897.py`; sửa phép kiểm C-897 nếu nó so với mã băm cũ (giữ tác dụng: lõi khác mã băm mới vẫn phải báo lỗi).
3. Viết Decision Log `92-Kinh-Nghiem/06-Decision-Log/DL-20261030-001-Sua-cong-ho-so-897.md` (giá trị cũ → lý do → căn cứ → người quyết → thời gian → giá trị mới).
4. Soạn **đề xuất gửi đơn vị quản lý Skill bản Trường** (Phòng QLKHCN&HTPT) đưa N1, N2, N3, N5, N6, N8 vào bản chính thức kế tiếp: `30-Ket-Qua/2026-10-30/De-xuat/DX-Sua-cong-ho-so-897_20261030.docx`, đúng thể thức (skill `the-thuc`, đo `kiem_the_thuc.py`).

## 4. Ca thử bắt buộc (`92-Kinh-Nghiem/02-Regression/Cases/test_cong_ho_so_897.py`)

Mỗi ca có **thử thuận** và **thử ngược** (quy tắc: thêm phép kiểm thì thêm ca ngược).

| Ca | Đầu vào (tạo tệp .docx tạm trong test) | Kỳ vọng |
|---|---|---|
| T1 | Dự thảo viện dẫn "Công văn số 5394/SGDĐT‑GDNNQLĐT" bằng `noBreakHyphen`; hồ sơ có tệp nguồn "Số: 5394/SGDĐT-GDNNQLĐT" | "Có trong hồ sơ" |
| T1-ngược | Như T1 nhưng tệp nguồn số 5395 | "THIẾU" |
| T2 | Tệp nguồn "Số: 287 /QĐ-UBND" (có dấu cách) | khóa `287/QD-UBND` được tạo |
| T3 | Văn bản không trong hồ sơ, có trong thư mục `--kho-ngoai` giả lập | "Có trong KTC-Database", không chặn |
| T3-ngược | Thư mục kho ngoài rỗng | "THIẾU", chặn |
| T4 | Kho ngoài chỉ có PDF scan cùng số | "bản scan, đối chiếu thủ công", không chặn, ghi I.8; hồ sơ **không** bị chặn G1 |
| T5 | "HĐ 99/HĐ-CĐKT-KTP" trong ô bảng của "Phụ lục II – Danh sách…" | "Chỉ dẫn số liệu – không đòi toàn văn" |
| T5-ngược | Cùng chuỗi trong phần "Căn cứ" của thân dự thảo | "THIẾU", chặn |
| T6 | Câu "và phụ lục 06 học sinh" | không báo thiếu Phụ lục 06 |
| T6-ngược | Câu "chi tiết tại Phụ lục 06" khi không có tiêu đề Phụ lục 06 | báo thiếu Phụ lục 06 |
| T8 | Dự thảo chính quyền viện dẫn "Nghị quyết số 19-NQ/TW"; hồ sơ có tệp Đảng dòng "Số 19-NQ/TW" (không dấu hai chấm) | "Có trong hồ sơ" |
| T8-ngược | Hồ sơ chỉ có tệp chính quyền "Số: 19/NQ-CP" | "THIẾU" — không khớp nhầm khác họ số hiệu |
| T9 | Dự thảo Đảng viện dẫn "Quy định số 208-QĐ/TW" và "Hướng dẫn số 05-HD/VPTW"; tệp nguồn "Số 208 - QĐ/TW" (có dấu cách) | cả hai "Có trong hồ sơ"; 208 xếp loại Quy định |
| T9-ngược | Hồ sơ có "Số: 208/QĐ-UBND" | "THIẾU" cho 208-QĐ/TW |
| T10 | Tệp Đảng cấp cơ sở "Số 12-BC/ĐU" và cơ quan dài "Số 1234-CV/UBKTTW" | tạo đúng khóa `12-BC/DU`, `1234-CV/UBKTTW` |
| T7 | Ca vàng: chạy cổng trên BC v8 (mục 1) với `--kho-ngoai` = KTC-Database | số văn bản THIẾU giảm từ 48 xuống chỉ còn văn bản **không có** trong kho; in danh sách so sánh trước/sau |

## 5. Tiêu chí nghiệm thu

1. Các ca thử ở mục 4 đều đạt; `python 29-Cong-Cu/kiem_tra_he_thong.py` mã thoát 0; `python 92-Kinh-Nghiem/02-Regression/Cases/test_kiem_tra_he_thong.py` đạt.
2. Ca vàng T7: in bảng "48 trước → N sau", mỗi văn bản còn thiếu có lý do (không có trong kho / chỉ có scan / chỉ dẫn số liệu).
3. Không có thay đổi nào ở: bảng mã `02-Quy-Tac-Xep-Muc.md`, quy tắc nhãn, chặn G1 với ảnh/scan **trong hồ sơ người dùng gửi**.
4. Gói `.skill` mới đóng được, `dong_goi_ra_soat_897.py` không báo lỗi; mã băm mới đã ghi.
5. Báo cáo ngắn kết quả gửi người giao: tệp đã sửa, ca thử, số liệu ca vàng, phần lệch bản Trường, tệp đề xuất.

## 6. Lệnh tái hiện nhanh (chạy trước khi sửa để xác nhận chẩn đoán)

```bash
python -X utf8 29-Cong-Cu/gom_ho_so_897.py "30-Ket-Qua/2026-10-29/Bao-cao/BC_Thuyet-minh-phuong-an-sap-xep-CSGDNN_Truong-CDKT_20261029_v8_ban-sach.docx" --ra "%TEMP%/rs897-tai-hien" --chuan-hoa-gach
```

Kết quả 30/10/2026 (để so): cổng lần 1 thiếu 39 (sau khi chuẩn hóa gạch); gom 10 tệp từ kho; cổng lần 2 còn thiếu 34; 5 văn bản được nhận (464, 339, 295, 153, NQ 42); QĐ 287, BC 175 gom được nhưng không nhận (N1); 335, 417 là PDF scan (N4).

## 7. Lưu ý khi làm

- Đọc trước: `CLAUDE.md`, `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`, `2A-KTC-Ra-Soat-897/00-README.md`, `.claude/rules/22-kiem-thu-va-dong-goi.md`.
- Hook `ktc_guard` chặn lệnh shell vừa nhắc đường dẫn kho vừa có thao tác ghi: tách bước đọc kho và bước ghi thành hai lệnh riêng, hoặc dùng công cụ Edit/Write.
- Không xóa tệp; tệp thay thế đưa vào `99-Luu-Tru/`.
- Commit theo từng nhóm việc (lõi; lớp dự án; ca thử; tài liệu), thông điệp tiếng Việt.
