# NHẬT KÝ CẬP NHẬT HỆ KTC-RA-SOAT-897-v2-CAI-TIEN
## Tài liệu chia sẻ kiến thức — Dành cho người dùng mới và Team Claude
### Phiên bản: 2.0 | Ngày: 29/9/2026 | Đồng bộ theo `ktc-ra-soat-897-v2.25.skill`
### Đơn vị ban hành: Phòng Tổng hợp – Hành chính và Quản trị, Trường Cao đẳng Kon Tum

---

## PHẦN I. GIỚI THIỆU HỆ THỐNG

Hệ KTC-Ra-Soat-897-v2-Cai-tien là hệ thống AI chuyên dụng rà soát, so sánh và chuẩn hóa văn bản hành chính của Trường Cao đẳng Kon Tum trước khi trình ký, theo Thông báo 897/TB-CĐKT ngày 04/8/2026 của Hiệu trưởng.

**Chỉ rà soát — không soạn mới.** Để soạn mới dùng: `ktc-soan-thao-vb`, `ktc-bao-cao`, `ktc-ke-hoach`.

- File .skill hiện hành: `ktc-ra-soat-897-v2.25.skill` (28/9/2026 — vá lỗi dương tính giả "Ban hành kèm theo" ở văn bản điện tử)
- Script chính: `build_ktc897_report.py` **v3.4**
- Chủ sở hữu: `truong.cdkontum@gmail.com` và `phongthhcqt@gmail.com` sở hữu/đồng sở hữu (cập nhật 09/9/2026). Tài khoản cũ `nnqp201@gmail.com` **đã hết quyền sở hữu / đã chuyển giao**

---

## PHẦN II. NGUYÊN TẮC CỐT LÕI

### 1. Bước 0 — Xác định hệ quy chiếu TRƯỚC MỌI VIỆC KHÁC

| Hệ | Loại văn bản | Áp dụng |
|---|---|---|
| **A** | Hành chính nhà nước | NĐ 30/2020/NĐ-CP + TB 597/TB-CĐKT |
| **B** | Văn bản của Đảng | HD 05-HD/VPTW — TUYỆT ĐỐI không áp NĐ 30 |
| **C** | Văn bản quy phạm pháp luật | Luật Ban hành VBQPPL |
| **D** | Văn bản đoàn thể | 3 tiểu-hệ: Công đoàn (có Quốc hiệu), Đoàn TN (tiêu đề riêng + 3 sao), Hội SV (không dòng tiêu đề) — **từ v2.21 có Checklist 09 riêng, đầy đủ D1/D2/D3** |

**Đồng thời từ v2.15**: chạy `tools/_read_input_properties.py` — đọc lề/cỡ chữ THẬT của file đầu vào. **Từ v2.17**: đã vá lỗi làm tròn ngưỡng (round+EPS cho cả 4 lề), kiểm thử 3 test case + chạy thật, đo được cải thiện tỷ lệ đúng hoàn toàn từ 28,6% → 40%.

### 2. Viện dẫn văn bản hợp nhất (từ v2.16)

Khi gặp cụm từ "hợp nhất"/"VBHN"/"văn bản hợp nhất" — **bắt buộc dừng lại, đọc `references/Skill-Library/Skill-Vien-Dan-Van-Ban-Hop-Nhat.md`** trước khi viết bất kỳ căn cứ pháp lý nào. Kích hoạt qua `00b-Trigger-Vien-Dan-Van-Ban-Hop-Nhat.md`, áp dụng cho cả 6 hệ (ktc-ra-soat-897, ktc-database, ktc-bao-cao, ktc-dis-tong-hop-vb, ktc-ke-hoach, ktc-van-ban).

### 3. Nghị định 334/2026/NĐ-CP — mốc hiệu lực 05/10/2026

**NĐ 60/2021 + NĐ 111/2025 vẫn còn hiệu lực. NĐ 334/2026 KHÔNG bãi bỏ hai nghị định đó** — đã kiểm từ
chính văn: Điều 16 không có khoản bãi bỏ; Điều 7.3.a còn dẫn chiếu ngược về NĐ 60/111.

Quan hệ là **chuyên ngành – chung**: NĐ 334 cho cơ sở GDĐH/GDNN, NĐ 60/111 cho mọi ĐVSNCL.

**Quy tắc viện dẫn**: tùy **nội dung tự chủ cụ thể**, **đơn vị soạn thảo** xem xét và viện dẫn nghị định phù
hợp, đúng quy định với nội dung đó. **Hệ không tự quyết thay.**

**Khi rà soát**: không nêu "căn cứ hết hiệu lực" với NĐ 60/111; không tự đổi căn cứ; thấy dấu hiệu nghị định
viện dẫn chưa khớp nội dung tự chủ → nêu **Mức 4**, đề nghị đơn vị soạn thảo rà lại và tự quyết.

Chi tiết và bảng định hướng: `references/Skill-Library/00d-Ghi-Nho-ND-334-2026-Pham-Vi-Co-So-GDNN.md`.

### 4. Cơ chế tự kích hoạt (từ 26/8/2026)

File `00c-Co-Che-Tu-Kich-Hoat.md` gộp 4 bước bắt buộc (đọc MEMORY-INDEX, quét cụm "hợp nhất", chạy Bước 0 + script định lượng, kích hoạt Skill-Tu-hoc) — chạy **tự động khi Skill nạp**, không phụ thuộc người dùng nhắc lại.

### 5. Tra Checklist 08 TRƯỚC khi áp NĐ 30

| Lỗi | Sai khi áp | Đúng phải áp |
|---|---|---|
| Viết thường sau dấu ":" | NĐ 30 → Mức 2 | TB 597 Mục 3.1 → **Mức 3** |
| Tên cơ sở sai | NĐ 30 → Mức 2 | Checklist 08 Mục 3.5 → **Mức 1** |

### 6. Kiểm tra file thực tế trên Drive trước khi coi phiên bản là chính thức

Không suy diễn từ tên file hay lời khẳng định "đã cập nhật". **Bài học lặp lại nhiều lần (26/8–06/9/2026)**: SKILL.md (bản đóng gói trong `.skill`) và các tài liệu điều khiển khác (00-README, Nhật ký, MEMORY-INDEX) từng phân kỳ nhiều lần theo cả hai hướng — không chỉ một bên cũ hơn. Luôn đối chiếu byte thật (`testzip()`, kích thước, nội dung) trước khi kết luận đồng bộ.

---

## PHẦN III. ĐỊNH DẠNG CHUẨN BÁO CÁO RÀ SOÁT

| Thành phần | Quy định |
|---|---|
| Font | Times New Roman — **14pt** thân bài/tiêu đề bảng, **13pt** nội dung ô bảng |
| Khổ giấy | A4 **ngang** (297×210mm) |
| Lề | **20mm đều bốn phía** |
| Cột MỨC | Tô **đỏ đậm** khi là Mức 1 |
| Bảng | `tblHeader` lặp tiêu đề · **tổng width ≤ 25,5cm** |
| **Chặn tràn khổ (từ v3.4)** | `raise ValueError` THẬT nếu bảng vượt ngưỡng |
| **Metadata file (từ v3.4)** | `_fix_app_xml_metadata()` tự tính lại Pages/Words/Paragraphs thật sau khi lưu |
| Trạng thái | "BẢN NHÁP RÀ SOÁT – CHƯA ĐƯỢC PHÊ DUYỆT CHÍNH THỨC" |

### Kết cấu 8 Phần chuẩn

I. Thông tin chung → II. Kết quả rà soát chi tiết → III. Nội dung đạt → **IV. Bảng tổng hợp** → V. Thẩm định chuyên môn (bắt buộc có điều kiện) → VI. Đánh giá tổng thể → VII. Kết luận → VIII. Phân tích khả thi (tùy chọn).

---

## PHẦN IV. QUY ƯỚC RIÊNG TRƯỜNG

### Tên 5 cơ sở — kiểm tra tất cả

| Cơ sở | Tên đúng |
|---|---|
| CS4 | **Khoa Kỹ thuật - Công nghệ và Đào tạo - Sát hạch lái xe** |

### Văn bản đã thay thế — luôn kiểm tra trước khi viện dẫn

| Văn bản cũ | Thay bởi | Từ ngày |
|---|---|---|
| QĐ 49/QĐ-CĐKT | QĐ 988/QĐ-CĐKT | 12/5/2026 |
| **QĐ 988/QĐ-CĐKT** | **QĐ 1976/QĐ-CĐKT** (Quy chế tổ chức và hoạt động) | **14/9/2026** |
| QĐ 50/QĐ-CĐKT | QĐ 1299/QĐ-CĐKT | 27/5/2026 |
| Pháp lệnh 01/2012/UBTVQH13 (bản gốc) | Hợp nhất tại VBHN 118/VBHN-VPQH, sửa đổi bởi PL 01/2026/UBTVQH16 | 01/7/2026 |

> ⚠️ **NĐ 334/2026 KHÔNG nằm trong bảng này** — nó **không bãi bỏ** NĐ 60/2021 + NĐ 111/2025.
> Quan hệ ở đây là **phạm vi đối tượng**: NĐ 334 dành cho cơ sở giáo dục nghề nghiệp, nên văn bản của Trường về tự chủ
> tài chính ban hành từ 05/10/2026 nên viện dẫn NĐ 334. Xem Phần II mục 3 và `Checklist/03-Phap-Ly.md`.

> ⚠️ **Cảnh báo trùng số**: QĐ **1229**/QĐ-CĐKT là văn bản khác — KHÁC HOÀN TOÀN QĐ **1299**/QĐ-CĐKT (Quy chế làm việc).

---

## PHẦN V. BỘ NHỚ VẬN HÀNH

Kho bộ nhớ: `09-Quan-Tri-He/10-Bo-Nho-He/`. Thứ tự ưu tiên nguồn: văn bản pháp luật đã kiểm chứng → SKILL.md/Checklist → quy ước Trường → Nhật ký → Process Memory → lịch sử hội thoại → suy luận mô hình. **Không dùng lớp 5–7 ghi đè lớp 1–4.**

**[Mới 09/9/2026] Thiếu nguồn — 2 lớp xử lý KHÁC NHAU, không gộp chung:**

| Thiếu cái gì | Xử lý |
|---|---|
| **Kho 01-04** (căn cứ pháp lý, quy định Trường) | **Dừng và hỏi** — giữ nguyên Nguyên tắc 1, không đổi. Không có căn cứ thì không được kết luận Mức 1/2 |
| **Bộ nhớ vận hành** (MEMORY-INDEX, Nhật ký, Process Memory — lớp 4–5) | **Chạy tiếp**, ghi vào Phần I: *"Chưa đối chiếu được bộ nhớ vận hành — kết quả có thể chưa kế thừa bài học các ca rà soát trước."* |

Lý do tách: bộ nhớ vận hành là lớp 4–5, không phải căn cứ pháp lý. Gộp chung khiến một trục trặc kết nối ở lớp 5 chặn cả ca rà soát.

---

### Vòng tự cải tiến (mới 29/9/2026)

Bốn tầng, có cổng người duyệt — chi tiết tại `MEMORY-INDEX.md` mục "Vòng tự cải tiến" và
`99-Kinh-Nghiem/03-Change-Proposals/CP-20260929-001.md`:

| Tầng | Nơi ghi | Khi nào |
|---|---|---|
| Bắt | `99-Kinh-Nghiem/05-Known-Issues/False-Positive.md` | **Ngay trong lượt** người dùng bác bỏ một phát hiện, không đợi cuối phiên |
| Thăng hạng | `MEMORY-INDEX.md` mục "Dương tính giả" | Khi `Số lần bị nhắc` **≥2** |
| Đúc kết | `99-Kinh-Nghiem/01-Lessons-Learned/` | Mỗi **10 bản Process Memory** mới, quét tìm pattern lặp |
| Cổng duyệt | `99-Kinh-Nghiem/03-Change-Proposals/` | Khi **≥3**, đề xuất gấp vào gói — **người duyệt** |

**Hàng rào an toàn**: `MEMORY-INDEX` là lớp 4, không đè được `SKILL.md` (lớp 2). Vòng này chỉ **thu hẹp**
được ("đừng bắt lỗi X"), không tự sinh quy tắc Mức 1 mới. Học sai thì hậu quả là bỏ sót, không phải bịa lỗi.

**Lần quét đầu tiên (29/9/2026, 12 bản PM)** tìm được 6 pattern tái lặp ≥5/12, trong đó nghẽn
`12-Output` xuất hiện **6/12** và bị `DL-20260905-001` kết luận "không khắc phục được" — đóng băng hơn
một tuần. Đã đính chính tại `DL-20260929-001.md`: ghi tệp lớn qua thư mục Drive kết nối đã thành công
nhiều lần (229–261KB). **Quy tắc mới**: mọi kết luận "không khắc phục được" phải kèm **ngày** và
**điều kiện môi trường**, và phải thử lại khi điều kiện đổi.

---

## PHẦN VI. LỊCH SỬ THAY ĐỔI

### v2.25 — 28/9/2026 (hiện hành)

**Vá một lỗi dương tính giả lặp lại nhiều lần.** Hệ bắt nhầm việc thiếu dòng *"(Ban hành kèm theo
Quyết định số ... ngày ... của ...)"* ở **văn bản điện tử ký số** là lỗi Mức 2, có lần còn suy diễn ngược
là "cần bổ sung khối Số hiệu/ngày tháng/thẩm quyền ký như một văn bản hành chính độc lập".

**Chẩn đoán**: quy tắc đúng **đã tồn tại** trong `Checklist/01-The-Thuc.md` từ lâu, nhưng Hệ không tìm ra
vì ba lý do — (a) quy tắc viết cụm *"Kèm theo văn bản số ..."* còn văn bản thật dùng *"(Ban hành kèm theo
Quyết định số ...)"*; (b) quy tắc nằm ở hàng **"Phụ lục"** còn văn bản bị bắt lỗi là một **Quy trình**;
(c) bảng chứa nó tên là *"thành phần bổ sung (kiểm tra khi có)"*, đọc như tùy chọn.

**Đây là lỗi thiết kế checklist, không phải lỗi thiếu quy tắc.** Bài học: *một quy tắc chỉ có tác dụng
khi tìm được bằng đúng từ ngữ mà văn bản thật dùng* — khi viết quy tắc mới, luôn liệt kê mọi cách diễn đạt.

**Đã sửa 2 chỗ**: (1) `Checklist/01-The-Thuc.md` tách **mục 3a** riêng — 4 cách viết, 9 loại văn bản kèm
theo, bảng phân mức theo hình thức phát hành, mặc định Trường là văn bản điện tử ký số nên không bắt lỗi;
(2) `SKILL.md` thêm mục **"Danh sách dương tính giả"** ngay dưới phần Phân loại vấn đề, gom 6 hiện tượng
đúng quy định nhưng hay bị bắt nhầm — đặt ở tầng luôn được nạp thay vì chỉ nằm trong checklist.

### v2.24 — 14/9/2026

**Đợt cập nhật lớn nhất từ trước tới nay.** Chi tiết đầy đủ: `references/Quan-Tri-He/CHANGELOG.md` mục v2.24.

**1. Đổi căn cứ ban hành**: QĐ 988/QĐ-CĐKT bị **QĐ 1976/QĐ-CĐKT ngày 14/9/2026** thay thế (hiệu lực từ ngày ký). Xác minh từ bản chính, không nghe lại qua mô tả. Sửa 14 tệp. Thêm **bảng chuyển tiếp 3 đời** QĐ 49 → QĐ 988 → QĐ 1976, đối chiếu theo **ngày ban hành của dự thảo** chứ không theo ngày rà soát — thiếu bảng này Hệ bắt lỗi oan mọi văn bản cũ.

**2. Quy định mới về ngày tháng**: toàn văn chỉ dùng **một** cách trình bày; **dạng ưu tiên là rút gọn `05/3/2026`**. Xen lẫn → Mức 3. Dùng dạng đầy đủ nhất quán không phải lỗi (Mức 4 gợi ý). Ngoại lệ: ngày ban hành dưới Quốc hiệu luôn viết đầy đủ.

**3. Sửa một quy tắc SAI**: Checklist 04 ghi *"ngày <10 và tháng <10 thêm số 0"*. Chính văn NĐ 30 Phụ lục I mục 4 chỉ quy định **ngày <10 và tháng 1, 2**. Quy tắc sai khiến Hệ đòi sửa `tháng 3` thành `tháng 03`.

**4. Hợp nhất `references/` rời vào gói** — khôi phục các quy tắc bị đánh rơi khi rút gọn v2.23: mục 0 "bắt buộc đo bằng công cụ" của Checklist 05, mục "viết hoa sau dấu hai chấm" và "UỶ/ỦY, HOÀ/HÒA" của Checklist 04, hình thức ký **TUQ.**, bản v1.4 của Skill tự học.

**5. Khôi phục 2 quy tắc hành vi** mất khi rút gọn v2.23: xuất báo cáo 8 phần **không hỏi lại**; phải **gọi thử thật công cụ** trước khi ghi "chưa xác minh".

**6. Chốt quy tắc NĐ 334/2026** sau khi đọc chính văn — quan hệ **chuyên ngành – chung**, NĐ 334 **không bãi bỏ** NĐ 60/111; tùy nội dung tự chủ, **đơn vị soạn thảo** tự chọn căn cứ phù hợp (xem Phần II mục 3).

**7. Đồng bộ 4 tệp dùng chung toàn KTC-DIS** — đẩy phần mới của hệ này lên `01-Chuan-Chung` trước, rồi phân phối ngược xuống cả 6 hệ.

---

### v2.23 — 13/9/2026

Dọn nguồn và vá kiểm thử. **Rút gọn `SKILL.md` từ 33.463 xuống 9.866 byte** theo nguyên tắc Progressive Disclosure, chuyển chi tiết xuống `references/`.

> ⚠️ **Bài học**: đợt rút gọn này làm **rơi mất một số quy tắc thật** — phát hiện và khôi phục ở v2.24 (xem mục 4, 5 ở trên). Rút gọn `SKILL.md` là đúng hướng, nhưng **phải đối chiếu từng quy tắc xem đã có nơi tiếp nhận chưa** trước khi xóa khỏi thân chính, không rút gọn bằng cách viết lại từ đầu.

---

### v2.22 (ghi đè) — 09/9/2026

Đợt **tối ưu hóa & dọn gói** theo yêu cầu Phòng TH-HC&QT. Ghi đè, **KHÔNG tăng số phiên bản**. Quy tắc có hiệu lực giữ nguyên, trừ đúng 1 điểm đã được duyệt (mục 4).

**1. Dọn tệp thừa**: xóa `assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897-v2.0-KTC-Enhanced.docx` (trùng MD5 tuyệt đối `786cdb34783ddc34b3d0ceb5bb12146a` với bản gốc — không phải bản nâng cấp) và `assets/KTC-Ra-Soat-897_Template_Trong.docx` (bản trung gian, chính SKILL.md đã tuyên bố không phải chuẩn áp dụng). Assets còn đúng 2 tệp chuẩn.

**2. Chỉ mục Prompt-Library**: thêm `README.md` tại `Prompt-Library/`, `02-Ra-Soat/`, `03-Chuan-Hoa/`. Trước đây 14 tệp prompt con là **tệp mồ côi** — không tệp nào trỏ đích danh nên hệ hay bỏ qua. README gốc có bảng tra 4 tác vụ × 7 loại văn bản + 4 ràng buộc chung.

**3. Rút gọn `SKILL.md`**: 35.762 → 29.478 byte (−18%). Toàn bộ phần kể lịch sử sự cố chuyển sang tệp mới `references/Quan-Tri-He/Ghi-Chu-Ky-Thuat.md` (lịch sử vá script v3.0→v3.4, ghi chú đọc tệp nhị phân LỆNH 7, 3 sự cố sinh ra 4 bước xác minh đóng gói, nợ kỹ thuật Process Memory, đính chính tham chiếu tệp 31/32). Không mất chữ nào, chỉ đổi chỗ.

**4. Tách Nguyên tắc 1 thành 2 lớp** — điểm thay đổi hành vi duy nhất, đã được duyệt. Chi tiết ở Phần V.

**5. Gấp 3 quy tắc từ MEMORY-INDEX vào `SKILL.md`** (đóng việc còn mở #11): quy tắc vận hành **#18** luôn xuất báo cáo 8 phần không hỏi lại · **#19** tự kiểm tra công cụ khả dụng trước khi ghi "chưa xác minh" · **#20** giới hạn tải tệp nhị phân lớn qua base64. Trước đó 3 quy tắc chỉ sống trong MEMORY-INDEX trên Drive — mà thay đổi ở mục 4 lại cho phép chạy tiếp khi thiếu bộ nhớ vận hành, tức tự tạo ra một lỗ hổng. Gấp vào SKILL.md để bịt đúng lỗ hổng đó.

**6. Thêm mục "Tra cứu Internet" vào `SKILL.md`**: trước đây SKILL.md **không hề trỏ tới** `references/Nguyen-Tac/00-Quy-Tac-Khai-Thac-Internet.md` và `references/Skill-Library/04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` dù cả 2 đã có sẵn trong gói. Nay ghi rõ **kho 01-04 trước, Internet sau**; tách 2 việc khác nhau (dùng để trả lời một câu hỏi vs nạp vĩnh viễn vào kho); giữ nguyên yêu cầu định dạng chữ đỏ và kiểm chứng chéo tối thiểu 2 nguồn độc lập.

**7. Đóng KI-001 — sửa bảng biểu 3 tệp mẫu.** Đo lại bằng `python-docx`, ghi nhận cũ *"3/5 bảng vượt nhẹ 25,8-26cm"* **không đúng**: `Mau_Bao_cao_ra_soat_KTC897_8phan.docx` thực ra có `tblGrid` **hỏng nặng** (10 cột cho bảng 6 cột, width **âm** −94,115cm; 3 `gridSpan` không hợp lệ `7`/`0`/`0`) — Word có thể từ chối mở, nặng hơn nhiều so với "vượt nhẹ"; `assets/KTC-Ra-Soat-897_Template_Trong.docx` có **3/3 bảng vượt**; và bản chuẩn `.dotx` tuy width đạt nhưng cả 3 bảng `autofit=True`, thiếu `tblLayout=fixed` — vi phạm đúng ràng buộc 3 bước của chính SKILL.md. Đã vá cả 3: **11/11 bảng** đạt ≤25,7cm, fixed layout, không còn width âm/gridSpan sai. Kèm đính chính spec bảng Phần II trong SKILL.md (10/45/100/55/30/20mm = 26,0cm tự vượt ngưỡng → 10/44/97/53/29/19mm = 25,2cm theo tệp mẫu thật).

**8. Đính chính quyền sở hữu Drive** và gỡ 3 tham chiếu treo trong `SKILL.md` (`tools/build_tcdm_review_fixed.py` không có trong gói + 2 ghi chú về assets vừa xóa).

**Xác nhận trước khi công bố** (đúng 4 bước bắt buộc): `testzip`=None · `SKILL.md` mở đầu bằng `---` YAML frontmatter · phiên bản khớp v2.22 giữa SKILL.md / 06-Metadata.md / CHANGELOG.md / MEMORY-INDEX.md / 00-README.md / tên tệp `.skill` · changelog ghi cụ thể từng tệp đổi kèm lý do. Bổ sung: 0 tham chiếu gãy, UTF-8 sạch 69 tệp, `py_compile` OK cả 2 script.

**Đính chính**: 3 việc từng ghi "còn tồn" ở changelog v2.22 thực ra **đã được vá từ trước** — `06-Metadata.md` đã ghi v2.22, `Checklist/README.md` đã ghi "9 checklist", `07-Theo-Loai-Van-Ban.md` đã trỏ sang Checklist 09.

### v2.19–v2.21 — 31/8/2026 đến 06/9/2026

**1. v2.21 (31/8/2026)**: Tách "Lịch sử cập nhật" khỏi `SKILL.md` sang `references/Quan-Tri-He/CHANGELOG.md` (Progressive Disclosure). Thêm `references/Checklist/09-Checklist-He-D-Doan-The.md` — Hệ D (đoàn thể) lần đầu có bộ quy tắc đầy đủ D1 Công đoàn/D2 Đoàn TN/D3 Hội SV, dựa trên mẫu 3.1–3.3 TB 597 + QĐ 933/QĐ-TLĐ, kèm 1 lỗi thật bắt được (hoán đổi thể thức D1↔D2).

**2. Đóng CONFLICT phiên bản (06/9/2026)** — phát hiện `SKILL.md` rời tham chiếu ở gốc thư mục bị mắc kẹt ở dòng đầu ghi "v2.18" dù thân bài đã có nội dung v2.21 (Checklist 09, 6 Nguyên tắc); ĐỒNG THỜI bản đóng gói trong `.skill` lại thiếu phần nhắc `99-Kinh-Nghiem/`/`00c-Co-Che-Tu-Kich-Hoat.md` mà bản rời có — phân kỳ theo **hai hướng khác nhau**, không phải một bên đơn thuần cũ hơn. Đã hợp nhất thủ công cả hai, ghi thành quy tắc 19 trong `SKILL.md` để tránh lặp lại.

**3. Phát hiện thêm (06/9/2026)**: `00-README.md` có đoạn văn bị hỏng ký tự thật trong mục changelog v2.20 (xác nhận qua 2 phương thức tra cứu độc lập, không phải lỗi thao tác chép tay) — cần sửa lại riêng.

### v2.18 — 30/8/2026

**1. Script nâng lên v3.4** — vá 5 lỗi xác nhận qua `validate.py` thật: chặn thật (`ValueError`) khi bảng vượt 25,7cm; giảm width cứng `bang_2cot()` xuống 25,5cm; thêm `_fix_app_xml_metadata()`; vá lỗi schema `<w:zoom>`; vá 3 lỗi thứ tự schema OOXML (`tblLayout`/`tcMar`/`shd`).

**2. Chuyển quyền sở hữu** — `KTC-Database` và `KTC-Ra-Soat-897-v2-Cai-tien` từ `nnqp201@gmail.com` sang `phongthhcqt@gmail.com`.

**3. Gỡ quyền `reader: anyone`** trên cả 2 thư mục gốc.

**4. Ghi nhận Nghị định 334/2026/NĐ-CP** (28/8/2026) — khi đó kết luận là "bổ sung song song, không bãi bỏ" NĐ 60/111. *(Kết luận này đã bị **bác ngày 14/9/2026**: NĐ 334 **thay thế** NĐ 60/111 kể từ 05/10/2026 — xem Phần II mục 3. Giữ lại dòng này làm ghi chép lịch sử, không phải quy tắc đang áp dụng.)*

### v2.17 — 26/8/2026
Vá lỗi làm tròn ngưỡng lề (round+EPS cho cả 4 lề). Giải quyết dứt điểm lỗi truy xuất nhị phân file test — nguyên nhân thật: copy tay base64 dài bị cắt cụt. Chạy hồi quy THẬT lần đầu trên file gốc: 12/30 đúng hoàn toàn (40%, tăng từ 28,6% baseline).

### v2.16 — 26/8/2026
Tạo Skill viện dẫn văn bản hợp nhất, nhân bản vào các hệ KTC-DIS (sau phát hiện hệ thứ 6 — ktc-van-ban).

### v2.15 — 25/8/2026
Tích hợp `tools/_read_input_properties.py` vào Bước 0.

### v2.14 — 25/8/2026
Hợp nhất script về `build_ktc897_report.py` v3.0; vá lỗi width bảng; chuẩn hóa bộ nhớ vận hành 7 lớp.

### v2.0–v2.13 — 12–25/8/2026
Xem chi tiết trong `references/Quan-Tri-He/CHANGELOG.md`.

---

## PHẦN VII. CẤU TRÚC THƯ MỤC

```
KTC-Ra-Soat-897-v2-Cai-tien/
├── 00-README.md, SKILL.md, ktc-ra-soat-897-v2.25.skill
├── assets/
├── references/
│   ├── Checklist/ (01–08 + 09 mới — Hệ D đoàn thể)
│   ├── Skill-Library/ (+ Skill-Vien-Dan-Van-Ban-Hop-Nhat + 00b/00c/00d)
│   ├── Prompt-Library/ (+ README chỉ mục — mới v2.22)
│   ├── Nguyen-Tac/
│   └── Quan-Tri-He/CHANGELOG.md + Ghi-Chu-Ky-Thuat.md (mới v2.22)
├── tools/
│   ├── build_ktc897_report.py ← v3.4
│   ├── _read_input_properties.py ← v1.1
│   └── test_margin_boundary.py
├── 12-Output/
├── 13-Regression-Test/
└── 09-Quan-Tri-He/
    ├── Nhat-Ky-Cap-Nhat-KTC-Ra-Soat-897-v2.md ← file này (v2.0)
    └── 10-Bo-Nho-He/
        ├── MEMORY-INDEX.md
        ├── 02-Mau-Process-Memory.md
        └── 03-Process-Memory/
```

---

## PHẦN VIII. VĂN BẢN PHÁP LÝ THAM CHIẾU

| Văn bản | Ghi chú |
|---|---|
| NĐ 30/2020/NĐ-CP | Hệ quy chiếu chính — tra sau TB 597 |
| TB 597/TB-CĐKT | Tra trước NĐ 30 khi gặp lỗi hình thức |
| NĐ 60/2021 + NĐ 111/2025 | Tự chủ tài chính ĐVSNCL — luôn tra cặp |
| **NĐ 334/2026/NĐ-CP** (ban hành 20/8/2026, hiệu lực 05/10/2026) | Quy định **chuyên ngành** cho cơ sở GDĐH, GDNN. **Điều 16 không bãi bỏ** NĐ 60/2021 + NĐ 111/2025; Điều 7.3.a còn dẫn chiếu ngược về hai nghị định đó. Tùy nội dung tự chủ, đơn vị soạn thảo tự chọn căn cứ phù hợp *(đã đọc chính văn 15/9/2026)* |
| Pháp lệnh 01/2012/UBTVQH13 + 01/2026/UBTVQH16 | Hợp nhất VBQPPL — VBHN 118/VBHN-VPQH |
| HD 05-HD/VPTW | Văn bản Đảng — KHÔNG áp NĐ 30 |
| TB 897/TB-CĐKT | Nền tảng pháp lý của Hệ |
| QĐ 933/QĐ-TLĐ | Thể thức chuyên sâu Công đoàn (Hệ D, mới v2.21) |

---

## PHẦN IX. HƯỚNG DẪN NGƯỜI DÙNG MỚI

**Cài Skill**: Tải `ktc-ra-soat-897-v2.25.skill` → Claude.ai → Settings → Capabilities → Skills → Upload skill.

**Kích hoạt**:
```
Kích hoạt Skill KTC-Ra-Soat-897-v2. Đọc MEMORY-INDEX.md trong
09-Quan-Tri-He/10-Bo-Nho-He/ trước, sau đó đọc SKILL.md và xác nhận sẵn sàng.
```

**4 tác vụ**: (a) Rà soát chính thức · (b) Rà soát nhanh · (c) So sánh 2 phiên bản · (d) Chuẩn hóa văn phong.

---

## PHẦN X. LIÊN HỆ

**Phòng TH-HC&QT, Trường Cao đẳng Kon Tum** | phongthhcqt@gmail.com

---
*Phiên bản 2.0 — 29/9/2026 — Đồng bộ theo `ktc-ra-soat-897-v2.25.skill`. Thay thế Nhật ký v1.9 (`superseded_by`).*