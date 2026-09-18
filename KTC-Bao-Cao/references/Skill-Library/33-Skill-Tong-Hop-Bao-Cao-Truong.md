# 33-Skill-Tong-Hop-Bao-Cao-Truong
## Phiên bản: v3.5 — cập nhật 14/9/2026
> Hợp nhất: nội dung nghiệp vụ v3.0 trong gói `.skill` + bốn BƯỚC 0A–0D bổ sung 14/9/2026.
> Bản rời trước đó là v2.3, **cũ hơn** bản trong gói — đã gộp thay vì ghi đè.

## Purpose
Dựng báo cáo công tác cấp Trường gồm **hai sản phẩm có hai nguồn khác nhau** (xem BƯỚC 0A):
phần **tường thuật** tổng hợp từ Phụ lục IIa của đơn vị, và **phụ lục kết quả** báo cáo lại kế hoạch công
tác của chính Trường. Kèm phát hiện số liệu mâu thuẫn giữa các đơn vị và tính % hoàn thành KPI cấp Trường.

> **Không phải** "gộp mọi nhiệm vụ của mọi đơn vị". Đó là cách hiểu của bản ≤ v2.3 và đã cho kết quả sai
> gấp hơn 5 lần quy mô thật.

## [MỚI v2.3] BƯỚC 0 — Xác định cấp báo cáo TRƯỚC KHI làm bất cứ điều gì khác

**Đây là bước bắt buộc đầu tiên, không được bỏ qua.**

Trước khi tổng hợp, phải xác nhận: báo cáo này gửi cho ai?
- Nếu gửi lên cấp trên của Trường (UBND tỉnh, Sở, Bộ...) → đây là **báo cáo cấp Trường**. Chủ thể ngữ pháp của TOÀN BỘ nội dung phải là **"Nhà trường"**, không phải tên Phòng/Khoa cụ thể.
- Nếu là báo cáo nội bộ 1 đơn vị gửi lên Trường → đây là **báo cáo cấp đơn vị**, chủ thể là tên đơn vị đó — không thuộc phạm vi Skill này (Skill này CHỈ tổng hợp cấp Trường).

Xem chi tiết nguyên tắc và ví dụ SAI/ĐÚNG tại `Skill-Tu-hoc-Phong-Cach-Bao-Cao.md` — Mục 0.

**Lỗi thực tế đã xảy ra (18/08/2026) cần tránh lặp lại:** khi tổng hợp báo cáo cấp Trường từ dữ liệu 2 đơn vị QLĐT&BĐCL và QLKHCN&HTPT, đã viết "Phòng QLĐT&BĐCL tổ chức thi..." — đây là văn phong cấp đơn vị bị lẫn vào báo cáo cấp Trường. Đúng phải là "Nhà trường tổ chức thi...".


## [SỬA v2.4] BƯỚC 0A — Báo cáo tháng cấp Trường là HAI sản phẩm, HAI NGUỒN KHÁC NHAU

**Đây là sửa đổi quan trọng nhất của v2.4.** Bản cũ coi mọi thứ đều là "gộp báo cáo của nhiều đơn vị".
Đối chiếu ba kỳ văn bản đã ban hành cho thấy **không phải vậy**:

| Sản phẩm | Nguồn ĐÚNG | Nguồn SAI (bản cũ làm) |
|---|---|---|
| **Báo cáo `.docx`** — Phần I, II, III | Tổng hợp **văn tường thuật** từ Phụ lục IIa (`.docx`) của các đơn vị | — (đúng) |
| **Phụ lục kết quả `.xlsx`** | **Kế hoạch công tác của chính Trường** (kế hoạch tháng, dẫn xuất từ Kế hoạch quý) — báo cáo lại kết quả thực hiện từng nhiệm vụ đã đề ra | Gộp toàn bộ nhiệm vụ từ Phụ lục IIb của các đơn vị |

**Bằng chứng — không suy đoán:**

| Phép đo | Kết quả |
|---|---|
| Phụ lục tháng 7 khớp với Kế hoạch quý III | **39/41 = 95%** |
| Phụ lục tháng 8 (`PL-375`) khớp với Kế hoạch quý III | 26/40 = 65% (phần còn lại là nhiệm vụ phát sinh trong kỳ) |
| Phụ lục tháng 8 khớp với phụ lục tháng 7 | 14/40 — **không phải chép lại kỳ trước** |
| Quy mô phụ lục tháng 7 · tháng 8 | **39 · 39** nhiệm vụ |
| Gộp từ báo cáo đơn vị (cách cũ) | **211** nhiệm vụ — sai gấp hơn 5 lần |

Chính tiêu đề mục I của biểu mẫu đã nói rõ: *"Các nhiệm vụ theo kế hoạch (chương trình) công tác **đã đề
ra**"* — tức nhiệm vụ đã có trong kế hoạch của Trường, không phải mọi việc đơn vị đã làm.

**Quy tắc:** lấy danh mục nhiệm vụ từ Kế hoạch công tác tháng của Trường; dùng Phụ lục IIb của đơn vị để
**điền kết quả, điểm chấm và KPI** cho từng nhiệm vụ đó. Nhiệm vụ đơn vị làm mà không có trong kế hoạch →
mục **"Nhiệm vụ đột xuất, phát sinh"**, kèm nguồn phát sinh; không trộn vào mục I.

**Điều kiện lọc kèm theo (cần, nhưng chưa đủ một mình):** phụ lục cấp Trường chỉ chứa nhiệm vụ do **lãnh
đạo cấp Trường** trực tiếp chỉ đạo — Hiệu trưởng, Phó Hiệu trưởng, Bí thư/Phó Bí thư Đảng ủy, Chủ tịch Công
đoàn, Bí thư ĐTN, Chủ tịch HSV. Kiểm chứng trên phụ lục tháng 7 và tháng 8: **100%**, không một dòng nào do
Trưởng khoa/Phó Trưởng khoa/Giáo vụ chỉ đạo.

## [MỚI v2.4] BƯỚC 0B — Danh mục mục con là CỐ ĐỊNH, không tự sinh

Mẫu `00. Mau bao cao thang (cap Truong).docx` quy định sẵn **từng mục con và lấy từ đơn vị nào**. Phải dùng
đúng danh mục này, **không** tự đặt tên mục con theo tên nội hàm TB 817.

| Mục | Mục con (đúng thứ tự) | Nguồn |
|---|---|---|
| 1. Mục tiêu phát triển KT-XH và nhiệm vụ chính trị | `* Công tác tuyển sinh` · `* Công tác đào tạo` · `* Công tác khảo thí` · `* Công tác bảo đảm chất lượng` · `* Công tác kế hoạch, tổng hợp` · `* Công tác tổ chức, cán bộ` | 4 mục đầu: QLĐT&BĐCL · kế hoạch tổng hợp: TH-HC&QT · tổ chức cán bộ: TCCB&CTHSSV |
| 2. Hoàn thiện thể chế, phân cấp, kiểm tra giám sát | `* Về thể chế` · `* Công tác Kiểm tra, giám sát` | Các phòng, khoa, Công đoàn, Đoàn TN |
| 3. KH-CN, đổi mới sáng tạo, chuyển đổi số | **KHÔNG có mục con** — viết liền một đoạn | QLKHCN&HTPT |
| 4. Xây dựng Đảng; phòng, chống tham nhũng, tiêu cực | `* Công tác xây dựng Đảng` · `* Chấp hành kỷ cương hành chính` · `* Công tác Đảng, Công đoàn, Đoàn Thanh niên` | Đảng ủy, Công đoàn, Đoàn TN |
| 5. Văn hóa, con người, an sinh xã hội | `* Công tác quản lý cơ sở vật chất` · `* Công tác Tài chính` · `* Công tác an sinh giáo dục` · `* Công tác truyền thông` | TH-HC&QT · TC-KT · TCCB&CTHSSV · Ban Truyền thông (thuộc TH-HC&QT) |
| 6. Quốc phòng, an ninh, đối ngoại, hội nhập | `* Về Quốc phòng - An ninh` · `* Về hoạt động Đối ngoại và Hợp tác` · `* Về hoạt động hợp tác phát triển` | TH-HC&QT · QLKHCN&HTPT |
| 7. Kết quả thực hiện các Nghị quyết của Bộ Chính trị | 8 Nghị quyết, đúng thứ tự: **59 · 66 · 68 · 79 · 70 · 71 · 72 · 80** | Rà thêm ở tất cả đơn vị |

Phần III (nhiệm vụ tháng sau) dùng **cùng danh mục**, đổi "kết quả" thành "kế hoạch"; mục 7 đổi tên thành
"Kế hoạch triển khai các Nghị quyết của Bộ Chính trị".

**Không được dùng nhãn "Công tác khác".** Nội dung không rơi vào mục con nào thì xếp vào mục con gần nhất
theo nội dung, hoặc nêu ra để người dùng quyết — không tạo nhãn mới.

**Lỗi đã xảy ra (13/9/2026):** tự sinh nhãn từ tên nội hàm TB 817 nên ra `* Công tác pháp chế, thanh tra,
kiểm tra và kiểm soát nội bộ`, `* Công tác chiến lược, quy hoạch và kế hoạch phát triển`, và **12 lần**
`* Công tác khác` — không khớp mẫu. Đáp án đã có sẵn trong mẫu, không cần tự xây bộ phân loại.

## [MỚI v2.4] BƯỚC 0C — Chuyển văn phong cấp đơn vị sang cấp Trường

Bốn phép kiểm bắt buộc chạy trên **toàn bộ** văn bản trước khi xuất. Căn cứ: lưu ý in trong mẫu, lặp lại ở
cả 4 mục lớn. Đối chiếu `BC-375`: **0 lần** dùng "tham mưu" trên 92 đoạn.

| # | Cấm | Cách sửa |
|---|---|---|
| 1 | `tham mưu cho Lãnh đạo Trường/Hiệu trưởng <động từ> X` | Bỏ cụm, giữ động từ: `ban hành X` |
| 2 | `tham mưu <danh từ>` | `xây dựng <danh từ>` — **chỉ khi theo sau là danh từ**; theo sau là động từ thì bỏ hẳn |
| 3 | `phối hợp với <Phòng/Khoa/Bộ môn nội bộ>` | Bỏ tên đơn vị, **giữ hành động**. Đối tác **ngoài** Trường (doanh nghiệp, UBND xã, Sở, Công an…) thì **giữ nguyên** |
| 4 | `trình/đề xuất Hiệu trưởng, Phó Hiệu trưởng, Lãnh đạo khoa… <động từ>` | Bỏ cụm trình, giữ động từ |
| 5 | Chủ ngữ đầu câu là `Khoa …`, `Phòng …`, `BCH CĐCS Trường …` | Đổi thành **"Nhà trường"** |

**Hai cạm bẫy khi tự động hóa — đã mắc thật:**

- Cắt cụm `phối hợp với <đơn vị>` bằng mẫu chung `(Phòng|Khoa)\s+[^,;.]{1,60}` **ăn lan sang hành động phía
  sau và xóa sạch nội dung câu**. Phải liệt kê tường minh tên 13 đơn vị nội bộ.
- Luật đổi chủ ngữ **không được chứa từ đứng một mình trùng với từ thông thường**. Nhánh `Ban` trần đã nuốt
  chữ "Ban" trong *"**Ban hành** Kế hoạch…"* → *"Nhà trường hành Kế hoạch…"*. Chỉ liệt kê tên đầy đủ
  (`Ban Truyền thông`).

## [MỚI v2.4] BƯỚC 0D — Dựng văn bản: phát triển từ bản đã ban hành

Không dựng báo cáo từ mẫu trống. Mở **chính tệp báo cáo tháng gần nhất đã ban hành**, thay nội dung, giữ
nguyên phần thể thức. Thể thức khi đó khớp tuyệt đối mà không phải chỉnh tay.

**Ba điểm kỹ thuật bắt buộc:**

1. **Mỗi đoạn nội dung gồm HAI run**: run 1 là nhãn `* Công tác …:` (đậm + nghiêng), run 2 là nội dung
   **để thường**. Gộp thành một run sẽ làm **cả đoạn đậm nghiêng**. Khi tạo run nội dung phải đặt tường
   minh `w:b`/`w:bCs`/`w:i`/`w:iCs` = `0`; để trống là kế thừa từ run mẫu.
2. Mục II (`Kết quả đạt được:`, `Tồn tại, hạn chế:`) **không có dấu `*`**.
3. Với `.xlsx`: `delete_rows` của openpyxl **không gỡ vùng gộp ô**. Phải `unmerge_cells` mọi vùng nằm trong
   vùng dữ liệu **trước khi** xóa hàng, nếu không các vùng gộp cũ sẽ trượt xuống và tràn ngang bảng.
   Kiểm chứng: vùng gộp phần tiêu đề phải **bằng** bản gốc, vùng gộp trong vùng dữ liệu phải **bằng 0**.

## [CẢNH BÁO v2.4] Hai tệp "mẫu" trong `KTC-Bao-Cao/` không phải mẫu trống

`00. Phu luc chi tiet ket qua cong tac thang (cap Truong).xlsx` và bản `.xltx` của nó có sheet tên
**`BC Kết quả tháng 7`** và chứa **39 nhiệm vụ thật** kèm tên người chỉ đạo thật. Dùng làm mẫu trống sẽ kéo
theo dữ liệu tháng 7 vào sản phẩm mới. `.docx` và `.dotx` là cùng một nội dung, chỉ khác định dạng lưu.

## Khi nào dùng
Sau khi các báo cáo đơn vị đã qua Skill 32 (đủ mẫu, đã gắn Trục/Nội hàm, đã kiểm KPI), cần gộp thành 1 báo cáo Trường.

## Bước tiền kiểm tra — Chiếu Checklist (Skill 35) trước khi tổng hợp

Trước khi bắt đầu tổng hợp, lấy Checklist hiện tại (từ Skill 35) và xác nhận:
- Danh sách đơn vị bắt buộc kỳ này: bao nhiêu đơn vị.
- Đơn vị nào đã qua Skill 32 ("Đã kiểm tra").
- Đơn vị nào chưa nộp hoặc còn "Vấn đề" chưa xử lý.

Thông báo rõ trước khi tổng hợp: "Tổng hợp với X/N đơn vị — [danh sách đơn vị thiếu] chưa có báo cáo hoặc chưa qua kiểm tra." Hỏi người dùng có muốn tiếp tục tổng hợp không đầy đủ hay chờ thêm.

## Bước lọc theo cột Ghi chú — CHỈ áp dụng Kế hoạch (Ia/Ib)

**Chỉ đưa vào báo cáo/kế hoạch cấp Trường các dòng có Ghi chú = "Đưa vào KH Trường".**
Các dòng "Thường xuyên của đơn vị" giữ nguyên ở cấp Phòng/Khoa — KHÔNG đưa lên bản tổng hợp Trường.

Dùng hàm `filter_truong_level()` trong `read_bc736_excel.py` (Skill-Library) để lọc tự động.

## Nhiệm vụ

0. **[v2.4]** Chạy BƯỚC 0A–0D trước. Xác định rõ đang dựng phần tường thuật hay phụ lục, và nguồn tương ứng.
1. **Phụ lục**: lấy danh mục nhiệm vụ từ **Kế hoạch công tác tháng của Trường**, rồi dùng Phụ lục IIb của
   đơn vị để điền kết quả/điểm chấm/KPI. Nhóm theo 6 Trục:
   - Mục I: "Các nhiệm vụ theo kế hoạch (chương trình) công tác đã đề ra"
   - Mục II: "Nhiệm vụ đột xuất, phát sinh" — việc đơn vị làm ngoài kế hoạch, **kèm nguồn phát sinh**
2. Trong từng Trục, sắp nhiệm vụ theo Nội hàm (theo `30-Skill-Phan-Loai-6-Truc.md`).
3. Phát hiện và xử lý nhiệm vụ trùng lặp giữa các đơn vị theo quy tắc dưới đây.
4. Phát hiện số liệu mâu thuẫn — liệt kê rõ, không tự chọn số nào đúng.
5. Tổng hợp theo đúng mẫu Phụ lục Ia/Ib/IIb/IIc (Thông báo 736).
5b. **[v2.4]** Phần tường thuật: dùng **danh mục mục con cố định** ở BƯỚC 0B, không tự sinh nhãn.
6. Tính % KPI hoàn thành cấp Trường theo Trục (chỉ với Phụ lục IIb/IIc):
   - Cộng dồn cột (6) Số lượng, (10) Số lượng quy đổi, và 6 cột KPI (11)-(16) của TẤT CẢ đơn vị, theo từng Trục.
   - Dùng hàm `summarize_truc_kpi()` trong `read_bc736_excel.py`.
7. **[v2.3] Viết nội dung với chủ thể "Nhà trường"** — xem Bước 0; chạy đủ **5 phép kiểm** ở BƯỚC 0C. Đơn vị chỉ xuất hiện như thành phần bổ trợ, không làm chủ ngữ chính.

## Quy tắc xử lý nhiệm vụ trùng lặp

Khi 2 hoặc nhiều đơn vị báo cáo cùng 1 nhiệm vụ (cùng nội dung, cùng Trục/Nội hàm):

**Bước 1 — Xác định đơn vị chủ trì theo thứ tự ưu tiên:**

| Ưu tiên | Tiêu chí |
|---------|---------|
| 1 | Đơn vị được giao chủ trì trong **Kế hoạch cùng kỳ** (nếu có từ PIS) |
| 2 | Đơn vị có cột **Sản phẩm/công việc cụ thể hơn** |
| 3 | Đơn vị có **Mức độ hoàn thành cao hơn** — dùng % KPI số lượng (TT) nếu có |
| 4 | Đơn vị **ký nhận công việc** |

**Bước 2 — Áp dụng:**
- Nếu một đơn vị thắng rõ ở ưu tiên 1 hoặc 2: gộp dưới đơn vị đó — nhưng khi viết vào báo cáo cấp Trường, chủ thể câu văn vẫn là "Nhà trường" (xem Bước 0), thông tin đơn vị chỉ ghi chú bổ trợ nếu cần.
- Nếu không phân biệt được rõ ràng: đánh dấu `[CẦN XÁC NHẬN ĐƠN VỊ CHỦ TRÌ]`, trình bày cả 2 phương án, chờ người dùng quyết định.
- **Tuyệt đối không tự gộp hoặc xóa nhiệm vụ của đơn vị nào** mà không có xác nhận.

## Nguồn sinh nội dung báo cáo Word (`fill_bc736.py`) — [CẬP NHẬT 18/08/2026, API MỚI]

**⚠️ Thay đổi quan trọng:** `fill_bc736.py` không còn dùng 1 `content_map` chung — lý do: nhiều
đoạn bôi vàng trong mẫu TRÙNG NHAU giữa Phần I và Phần III (VD "Công tác tuyển sinh" xuất hiện
y hệt ở cả 2 Phần), và cả 8 Nghị quyết Bộ Chính trị dùng chung 1 đoạn bôi vàng. Dùng chung 1 dict
sẽ khiến nội dung Phần I (kết quả) bị chèn nhầm sang Phần III (kế hoạch).

Giờ phải soạn `content_by_phase` — **3 khối RIÊNG BIỆT**:
```python
content_by_phase = {
    "PHAN_I":   { "<nhãn>": "<nội dung KẾT QUẢ, chủ thể Nhà trường>", ... },  # 27 vị trí
    "PHAN_II":  { "kết quả đạt được": "...", "tồn tại, hạn chế": "..." },     # 2 vị trí
    "PHAN_III": { "<nhãn>": "<nội dung KẾ HOẠCH, chủ thể Nhà trường>", ... }, # 16 vị trí
}
```

**Nguyên tắc soạn:**
- Nội dung Phần I và Phần III PHẢI khác nhau dù cùng nhãn (VD cùng "Công tác tuyển sinh" nhưng
  Phần I nói KẾT QUẢ tháng đã qua, Phần III nói KẾ HOẠCH tháng tới) — không được sao chép qua lại.
- Đoạn văn = tóm tắt số liệu thật (số nhiệm vụ hoàn thành, % KPI 3 chiều) + 2-3 sản phẩm tiêu biểu
  (nguyên văn từ cột Sản phẩm/công việc) + chuyển văn phong cấp Trường: **chủ thể "Nhà trường"**.
- Nếu 1 nhãn không có dữ liệu nguồn → để `fill_report()` tự đánh dấu `[CẦN BỔ SUNG [PHAN_X] nhãn]`.
- Xem đầy đủ danh sách 45 vị trí thật (27+2+16) tại `README-fill_bc736.md`.
- Dùng hàm `build_content_map_skeleton()` trong `read_bc736_excel.py` để dựng khung nháp (theo Trục,
  không theo Phần) — khung nháp chỉ là điểm khởi đầu, PHẢI phân loại lại vào đúng PHAN_I hay PHAN_III
  và chuyển chủ thể "Nhà trường" trước khi đưa vào `content_by_phase`.

## [MỚI v2.3] Kiểm tra cuối trước khi gọi `fill_report()`

Trước khi đưa `content_map` vào `fill_report()`, rà lại TỪNG giá trị:
1. Câu đầu tiên của đoạn có bắt đầu bằng tên 1 Phòng/Khoa cụ thể không? Nếu có → sửa lại, chủ ngữ phải là "Nhà trường".
2. Tên đơn vị (nếu xuất hiện) chỉ ở vị trí bổ ngữ, không phải chủ ngữ chính.
3. Không có câu nào đọc như báo cáo nội bộ của 1 Phòng.

## Ràng buộc
- Không tự quyết định đơn vị nào đúng khi có mâu thuẫn số liệu.
- Không bỏ sót nhiệm vụ của đơn vị nào — ghi rõ "Đơn vị X: chưa nộp báo cáo kỳ này" (lấy từ Checklist Skill 35).
- Không tự gán 1 nhóm (Trục, Đơn vị) vào đúng 1 trong 22 khóa nội dung nếu Nội dung công việc không rõ nội hàm — để `[CẦN XÁC ĐỊNH]`.
- Đối chiếu Nguyên tắc 1 — nếu cần căn cứ, tìm trong kho dữ liệu; không suy diễn.
- **Không dùng tên đơn vị làm chủ ngữ chính trong bất kỳ câu nào của báo cáo cấp Trường.**

## Output
1. Báo cáo tổng hợp cấp Trường đầy đủ theo mẫu TB736 — chủ thể "Nhà trường" xuyên suốt.
2. Bảng % KPI hoàn thành theo 6 Trục.
3. Phụ lục các vấn đề cần xác nhận (A: trùng lặp, B: mâu thuẫn số liệu, C: đơn vị chưa nộp).

## PROCESS MEMORY / AUDIT TRAIL — BẮT BUỘC
KTC-RIS không chỉ lưu INPUT và OUTPUT. Mỗi lần thực hiện Skill này phải tạo hoặc bổ sung **Run Record** trong `KTC-Bao-Cao/memory`.

Trường tối thiểu: `run_id`; thời gian; kỳ/loại báo cáo; Skill+phiên bản; `sources[]` (tên + Drive File ID/URI); `operations[]`; `decisions[]` (căn cứ+lý do+mức tin cậy); `exceptions[]`; `outputs[]`; `qa[]`; `learning_candidates[]`; `status`.

Chuỗi truy vết bắt buộc: `Source → Evidence → Transformation → Decision → Output → QA`.

`learning_candidates` không tự động thành Skill. Chỉ promote khi có provenance, đã kiểm chứng, không xung đột quy định cao hơn, xác định phạm vi áp dụng và có cơ chế `superseded/deprecated`.

Trước khi tuyên bố hoàn thành phải cập nhật Run Record; nếu không thể ghi thì nêu `PROCESS_MEMORY_NOT_WRITTEN`.

