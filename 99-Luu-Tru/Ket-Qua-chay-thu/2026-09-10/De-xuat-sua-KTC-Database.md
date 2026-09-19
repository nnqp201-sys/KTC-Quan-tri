# Đề xuất chỉnh sửa KTC-Database — phát hiện khi liên kết dữ liệu cho KTC-Quan-tri

**Ngày lập:** 10/9/2026
**Người thực hiện:** Claude Code (phiên liên kết `KTC-Quan-tri` ↔ `KTC-Database`)
**Trạng thái:** Đề xuất — **chưa áp dụng vào kho**. Kho `KTC-Database` đang ở chế độ chỉ đọc
(hook chặn ghi), nên toàn bộ nội dung dưới đây cần người có thẩm quyền tự áp vào Drive.

Tất cả dữ liệu dưới đây đọc trực tiếp từ toàn văn tệp gốc, không suy diễn.

---

## 1. Kho `03-Templates` — chỉ mục lạc hậu so với thực tế

**Phát hiện:** `KTC-DIS-Master-Index_20260830_v1.2.xlsx` không có dòng nào cho thư mục
`03-Templates(1)`, trong khi đây mới là kho biểu mẫu trống thật.

| Thư mục | Thực tế | Master Index v1.2 |
|---|---|---|
| `03-Templates` | 19 tệp, hầu hết là **văn bản thật đã ban hành**, chỉ 01 mẫu trống | Có, đã đánh dấu "CẦN XỬ LÝ / Không dùng" — mô tả đúng |
| `03-Templates(1)` | 17 tệp: **16 biểu mẫu trống** `.dotx`/`.xltx` + `00-Template-Registry-KTC-DIS.docx` | **Không có dòng nào** |

**Danh mục 16 biểu mẫu trong `03-Templates(1)`:** Quyết định ban hành quy chế · Quyết định cá biệt
(phê duyệt nhiệm vụ dự toán / bổ nhiệm) · Thông báo (hướng dẫn đăng ký kế hoạch báo cáo / kết luận giao ban) ·
Kế hoạch trung hạn · Kế hoạch thực hiện công việc · Kế hoạch công tác tháng (`.xltx`) · Báo cáo (nội bộ /
theo Quy chế làm việc / chuyên đề / hướng dẫn xây dựng kế hoạch báo cáo) · Tờ trình · Công văn · Biên bản · Giấy mời.

**Đề xuất xử lý — chọn một trong hai:**

- **Cách A (khuyến nghị):** đổi tên `03-Templates(1)` thành tên có nghĩa (ví dụ `03-Bieu-Mau-Trong`),
  bổ sung dòng tương ứng vào Master Index, nâng phiên bản chỉ mục lên `20260910_v1.3`. Giữ nguyên
  `03-Templates` với nhãn "CẦN XỬ LÝ" cho tới khi phân loại xong số văn bản thật nằm trong đó
  (chuyển sang `04-Good-Documents` nếu đạt chất lượng).
- **Cách B:** gộp 16 biểu mẫu vào đúng các thư mục con `03-01`…`03-10` hiện có, rồi xóa
  `03-Templates(1)`. Cách này sạch hơn về lâu dài nhưng phải sửa mọi tham chiếu đang trỏ tới tên cũ.

**Dòng cần thêm vào Master Index (nếu chọn Cách A):**

| Mã | Tên thư mục | Cấp | Nhóm | Chứa tài liệu gì | Tra cứu khi nào | Skill dùng chính | Ghi chú |
|---|---|---|---|---|---|---|---|
| 03B | 03-Bieu-Mau-Trong | 1 | Biểu mẫu | 16 biểu mẫu trống .dotx/.xltx + Template Registry | Cần mẫu trống đúng thể thức để soạn văn bản mới | Mọi skill | Kho biểu mẫu thật; thay thế vai trò danh nghĩa của 03-Templates |

---

## 2. `METADATA_Quy-che_Danh-gia-KPI_20260903.md` — bản điền đầy đủ

Bản hiện hành để trống 6 trường ("Không xác định"), trong khi mọi dữ liệu đều có sẵn trong chính văn bản.
**Nội dung thay thế toàn bộ tệp:**

````markdown
# METADATA — Quy-che_Danh-gia-KPI-tap-the-ca-nhan_Truong-CDKT

## 11 trường bắt buộc
1. **Tên văn bản**: Quyết định số 1923/QĐ-CĐKT ban hành Quy chế đánh giá, xếp loại chất lượng tập thể, cá nhân gắn với Chỉ số đánh giá hiệu quả công việc (KPI)
2. **Loại**: Quyết định (ban hành Quy chế)
3. **Đơn vị ban hành**: Trường Cao đẳng Kon Tum (UBND tỉnh Quảng Ngãi)
4. **Ngày ban hành**: 30/8/2026
5. **Lĩnh vực**: Tổ chức - Cán bộ / Đánh giá
6. **Người ký**: Lê Trí Khải, Hiệu trưởng
7. **Từ khóa**: Quy chế, KPI, đánh giá xếp loại chất lượng, tập thể, cá nhân, 6 trục kết quả, bản cam kết KPI
8. **Căn cứ pháp lý** (13 căn cứ):
   - Quyết định số 988/QĐ-CĐKT ngày 12/5/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum ban hành Quy chế tổ chức và hoạt động của Trường;
   - Luật Viên chức ngày 10/12/2025;
   - Nghị định số 233/2026/NĐ-CP ngày 26/6/2026 của Chính phủ quy định về đánh giá, xếp loại chất lượng đối với đơn vị sự nghiệp công lập và viên chức;
   - Nghị định số 259/2026/NĐ-CP ngày 30/6/2026 của Chính phủ quy định về tuyển dụng, sử dụng và quản lý viên chức;
   - Quy định số 366-QĐ/TW ngày 30/8/2025 của Bộ Chính trị về kiểm điểm và đánh giá, xếp loại chất lượng đối với tập thể, cá nhân trong hệ thống chính trị;
   - Quy định số 399-QĐ/TU ngày 27/8/2025 của Ban Thường vụ Tỉnh ủy về đánh giá, xếp loại cán bộ, công chức, viên chức và người lao động;
   - Kết luận số 198-KL/TW ngày 08/10/2025 của Bộ Chính trị về chủ trương đánh giá đối với cán bộ lãnh đạo, quản lý trong hệ thống chính trị;
   - Hướng dẫn số 43-HD/BTCTW ngày 31/10/2025 của Ban Tổ chức Trung ương;
   - Hướng dẫn số 01-HD/TU ngày 11/11/2025 của Ban Thường vụ Tỉnh ủy Quảng Ngãi;
   - Hướng dẫn số 02-HD/ĐU ngày 14/11/2025 của Đảng ủy UBND tỉnh Quảng Ngãi;
   - Hướng dẫn số 02-HD/BTCTW ngày 22/5/2026 của Ban Tổ chức Trung ương về đánh giá định kỳ hằng quý đối với cán bộ lãnh đạo, quản lý;
   - Quyết định số 31/2025/QĐ-UBND ngày 15/10/2025 của UBND tỉnh Quảng Ngãi;
   - Quyết định số 37/2025/QĐ-CTUBND ngày 06/11/2025 của Chủ tịch UBND tỉnh Quảng Ngãi.
9. **Đối tượng áp dụng**: Tập thể các đơn vị thuộc Trường; viên chức, người lao động của Trường Cao đẳng Kon Tum
10. **Hiệu lực**: Đang có hiệu lực, kể từ ngày ký (30/8/2026)
11. **Văn bản liên quan**:
    - **Thay thế**: Quyết định số 1490/QĐ-CĐKT ngày 04/10/2024 (Quy định thực hiện Bộ tiêu chí đánh giá năng lực thực hiện công việc KPIs); Quyết định số 366/QĐ-CĐKT ngày 11/02/2026 (Khung tiêu chí đánh giá tập thể, cá nhân). *Cả hai văn bản bị thay thế hiện không có trong kho 01-04.*
    - **Phụ lục kèm theo**: Phụ lục I, II, III (xem `METADATA_QD1923_Phu-luc_I-II-III_20260903.md`) — Quy chế dẫn chiếu trực tiếp mẫu tại Phụ lục I và Phụ lục II.
    - **Liên quan**: Thông báo số 817/TB-CĐKT (nội hàm 6 trục kết quả trọng tâm) — cụ thể hóa cùng Hướng dẫn 02-HD/BTCTW.

## 2 trường bổ sung riêng theo loại (Quyết định)
- **Loại quyết định**: Cá biệt (ban hành quy chế nội bộ)
- **Thẩm quyền ký**: Hiệu trưởng

## 3 trường trách nhiệm
- **Nguồn dữ liệu đã dùng**: Đọc trực tiếp toàn văn tệp `Quy-che_Danh-gia-KPI-tap-the-ca-nhan_Truong-CDKT_20260829_v1.docx` tại `02-KTC-Regulations/`
- **Người kiểm tra**: (chưa xác định)
- **Trạng thái phê duyệt**: Đã duyệt nội bộ

## Nguồn gốc nạp
Do người dùng/Trường cung cấp (11-Input)

## Ghi chú
- **Lệch ngày giữa tên tệp và văn bản**: tên tệp ghi `20260829` nhưng văn bản ghi rõ "Quảng Ngãi, ngày 30 tháng 8 năm 2026". Lấy theo văn bản: **30/8/2026**.
- Cấu trúc Quy chế: 5 chương, 28 điều.
- Quy chế dẫn chiếu việc chấm điểm thực hiện **trên phần mềm KPI** — cần xác minh phần mềm này khi số hóa quy trình.
````

---

## 3. `METADATA_QD1923_Phu-luc_I-II-III_20260903.md` — bản điền đầy đủ

Bản hiện hành để trống 4 trường và không nhận ra Phụ lục thuộc chính Quyết định 1923 đã có metadata riêng.
**Nội dung thay thế toàn bộ tệp:**

````markdown
# METADATA — QD1923 Phụ lục I, II, III

## 11 trường bắt buộc
1. **Tên văn bản**: Phụ lục I, II, III kèm theo Quyết định số 1923/QĐ-CĐKT ngày 30/8/2026 — Mẫu kế hoạch thực hiện nhiệm vụ công tác quý của đơn vị (PL I); Mẫu kế hoạch/danh mục công việc cá nhân (PL II); Mẫu phiếu đánh giá, xếp loại chất lượng viên chức/người lao động (PL III)
2. **Loại**: Phụ lục / Mẫu biểu
3. **Đơn vị ban hành**: Trường Cao đẳng Kon Tum (UBND tỉnh Quảng Ngãi)
4. **Ngày ban hành**: 30/8/2026 (theo Quyết định 1923)
5. **Lĩnh vực**: Tổ chức - Cán bộ / Kế hoạch / Đánh giá
6. **Người ký**: Lê Trí Khải, Hiệu trưởng (ký Quyết định 1923 ban hành kèm)
7. **Từ khóa**: Phụ lục, QĐ 1923, mẫu kế hoạch công tác quý, danh mục công việc cá nhân, phiếu đánh giá, KPI, điểm chấm, hệ số quy đổi
8. **Căn cứ pháp lý**: Quyết định số 1923/QĐ-CĐKT ngày 30/8/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum (xem đầy đủ 13 căn cứ tại `METADATA_Quy-che_Danh-gia-KPI_20260903.md`)
9. **Đối tượng áp dụng**: Các đơn vị thuộc Trường; viên chức, người lao động Trường Cao đẳng Kon Tum
10. **Hiệu lực**: Đang có hiệu lực, theo hiệu lực của Quyết định 1923 (từ 30/8/2026)
11. **Văn bản liên quan**: Quyết định số 1923/QĐ-CĐKT và Quy chế đánh giá KPI ban hành kèm theo — Quy chế dẫn chiếu trực tiếp: "Tập thể, cá nhân lập kế hoạch công tác theo mẫu tại Phụ lục I, Phụ lục II".

## 3 trường trách nhiệm
- **Nguồn dữ liệu đã dùng**: Đọc trực tiếp 3 tệp phụ lục và toàn văn Quyết định 1923 tại `02-KTC-Regulations/`
- **Người kiểm tra**: (chưa xác định)
- **Trạng thái phê duyệt**: Đã duyệt nội bộ

## Nguồn gốc nạp
Do người dùng/Trường cung cấp (11-Input)

## Ghi chú — cấu trúc dữ liệu của Phụ lục I
Bảng mẫu kế hoạch quý gồm các cột: TT · Nội dung công việc · Người trực tiếp chỉ đạo · Đơn vị chủ trì ·
Sản phẩm/công việc · Số lượng · Độ khó, mới, phức tạp, phạm vi tác động · Thời gian hoàn thành ·
**Điểm chấm công việc** · **Hệ số quy đổi**.

Hai cột cuối chính là nơi áp thang quy đổi 5 nhóm (50/120/250/350/450 điểm ↔ hệ số 0,5/1,2/2,5/3,5/4,5)
trong `KTC-Quan-tri/KTC-Du-lieu-Cong-Viec/DANH MUC SAN PHAM CONG VIEC/`. Phụ lục II là biểu mẫu sinh ra
1.358 dòng nhiệm vụ gốc đã được tổng hợp thành 122 nhiệm vụ chuẩn.
````

---

## 4. Việc cần làm thêm (chưa xử lý trong phiên này)

| # | Việc | Lý do |
|---|---|---|
| 1 | Đổi tên tệp `Quy-che_Danh-gia-KPI-..._20260829_v1.docx` → `..._20260830_v1.docx` | Tên tệp sai ngày ban hành so với văn bản |
| 2 | Tìm và nạp QĐ 1490/QĐ-CĐKT (04/10/2024) và QĐ 366/QĐ-CĐKT (11/02/2026) vào kho, đánh dấu **ĐÃ HẾT HIỆU LỰC** | `00-Metadata-Schema.md` yêu cầu tạo ghi chú hết hiệu lực cho văn bản bị thay thế; hiện cả hai không có trong kho nên chưa có cảnh báo nào |
| 3 | Phân loại lại số văn bản thật đang nằm trong `03-Templates` | Đang bị đánh dấu "CẦN XỬ LÝ" từ Master Index v1.2 (30/8/2026), chưa xử lý |
| 4 | Xác minh "phần mềm KPI" mà Quy chế dẫn chiếu | Ảnh hưởng trực tiếp tới thiết kế Master Task Register của KTC-Quan-tri |
