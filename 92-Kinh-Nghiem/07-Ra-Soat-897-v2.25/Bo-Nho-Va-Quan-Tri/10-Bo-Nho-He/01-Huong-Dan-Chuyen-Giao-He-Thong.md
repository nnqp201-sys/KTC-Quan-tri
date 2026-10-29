# HỒ SƠ TỔNG HỢP TRI THỨC VÀ BÀN GIAO QUẢN HÀNH HỆ THỐNG
## Hệ KTC-Ra-Soat-897-v2-Cai-tien

**Vị trí lưu trữ dự kiến**: `09-Quan-Tri-He/01-Huong-Dan-Chuyen-Giao-He-Thong.md`
**Ngày soạn**: 07/9/2026 · **Phiên bản nguồn**: v2.21 · **Phân loại nguồn**: theo `[FACT]` / `[INFERENCE]` / `[PROPOSAL]` / `[UNKNOWN]` / `[CONFLICT]` như yêu cầu.

> **Lưu ý phạm vi (bắt buộc đọc trước)**: Tài liệu này được soạn theo đúng nguyên tắc ZERO-FABRICATION — chỉ dùng dữ liệu có thật trong `SKILL.md`, `CHANGELOG.md`, `00-README.md`, Nhật ký cập nhật, Mô tả kỹ thuật gửi Anthropic, và các văn bản quy định đã xác nhận (897/TB-CĐKT, 597/TB-CĐKT, NĐ 30/2020/NĐ-CP, HD 05-HD/VPTW, NĐ 34/2016/NĐ-CP). Yêu cầu gốc có đề cập một số nội dung cho Mục 7 (roadmap v3.0) không có căn cứ trong bất kỳ nguồn nào của hệ này ("Gemini 3.6 Flash", "thinking_level", "Connector Mock Engine") — các nội dung này được đánh dấu `[UNKNOWN — CHƯA ĐỦ CĂN CỨ]` tại Mục 7, không được trình bày như sự thật.

---

## 1. TỔNG QUAN HỆ THỐNG VÀ BỐI CẢNH VẬN HÀNH

**[FACT]** Mục đích: rà soát, so sánh, chuẩn hóa văn bản hành chính của Trường Cao đẳng Kon Tum trước khi trình ký, theo Thông báo 897/TB-CĐKT ngày 04/8/2026 của Hiệu trưởng. Hỗ trợ đúng 4 tác vụ: (a) rà soát chính thức, (b) rà soát nhanh, (c) so sánh 2 phiên bản, (d) chuẩn hóa văn phong.

**[FACT]** Triết lý cốt lõi: **KHÔNG soạn thảo văn bản mới**. Khi người dùng yêu cầu soạn mới, hệ phải từ chối và trỏ sang `ktc-tong-hop-van-ban`, `KTC-Bao-Cao`, hoặc `KTC-Ke-Hoach`.

**[FACT]** Đơn vị chủ quản: Phòng Tổng hợp – Hành chính và Quản trị (TH-HC&QT), Trường Cao đẳng Kon Tum. Tài khoản quản trị hiện hành: `phongthhcqt@gmail.com` (chủ sở hữu 2 thư mục gốc `KTC-Database` và `KTC-Ra-Soat-897-v2-Cai-tien` từ 30/8/2026, trước đó là `nnqp201@gmail.com`).

**[FACT]** Kiến trúc đóng gói `.skill` (gói hiện hành `ktc-ra-soat-897-v2.23.skill`, 213.060 bytes):

```
ktc-ra-soat-897/
├── SKILL.md                          ← YAML frontmatter (name, description) + nội dung hành vi
├── references/
│   ├── Checklist/                    ← 01–08 (viết lại tiếng Việt, số liệu định lượng) + 09 (mới v2.21, Hệ D)
│   ├── Skill-Library/                ← Skill 02,14,17,18,19,28,29,30,31,
│   │                                    Skill-Vien-Dan-Van-Ban-Hop-Nhat và 00b-Trigger
│   ├── Prompt-Library/                ← khuôn prompt theo 4 tác vụ và loại văn bản
│   └── Quan-Tri-He/CHANGELOG.md      ← lịch sử chi tiết (tách khỏi SKILL.md từ v2.21)
├── tools/
│   ├── build_ktc897_report.py        ← v3.5, script CHÍNH THỨC DUY NHẤT xuất báo cáo
│   └── _read_input_properties.py     ← v1.2, đọc thuộc tính định dạng THẬT của file .docx đầu vào
└── assets/
    ├── KTC-Ra-Soat-897_Template_Trong.dotx  ← chuẩn DUY NHẤT áp dụng
    └── Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx
```
*(*) Skill 30 được `SKILL.md` tham chiếu 2 lần nhưng — xem Mục 6 — file này **không tồn tại thật** trên Drive tại thời điểm soạn tài liệu này; đây là tham chiếu treo cần người tiếp quản xử lý.*

**[FACT]** Quan hệ với KTC-DIS: đây là 1 trong 6 hệ (`ktc-ra-soat-897`, `ktc-database`, `ktc-bao-cao`, `ktc-ke-hoach`, `ktc-dis-tong-hop-van-ban`, `ktc-van-ban`), dùng chung kho dữ liệu 01–04 trên `KTC-Database` và Skill viện dẫn văn bản hợp nhất dùng chung.

**[INFERENCE]** Số lượng 6 hệ (thay vì 5 như từng ghi nhận ở một số tài liệu cũ) được xác nhận sau khi phát hiện `ktc-van-ban` từng bị hiểu nhầm là thư mục legacy — cần rà lại các tài liệu cũ còn ghi "5 hệ" nếu gặp.

---

## 2. MA TRẬN 4 HỆ QUY CHIẾU THỂ THỨC (CORE LOGIC)

**[FACT]** Bước 0 là bước bắt buộc thực hiện đầu tiên, trước mọi nội dung khác — xác định đúng 1 trong 4 hệ, không áp lẫn.

| Hệ | Căn cứ | Tài liệu tra cứu | Đặc điểm nhận dạng |
|---|---|---|---|
| **A — Hành chính nhà nước** | NĐ 30/2020/NĐ-CP + Phụ lục I; TB 597/TB-CĐKT | Skill 02, 14; Checklist 01–05, 07, 08 | Ký hiệu **không chứa năm** (vd `988/QĐ-CĐKT`) |
| **B — Đảng** | HD 05-HD/VPTW (27/5/2026, thể thức/trình bày); QĐ 399-QĐ/TW (09/01/2026, thể loại/thẩm quyền) | Skill 29 + `29-Phu-Luc-2` + `29-Phu-Luc-3`; Checklist 02,03,04,08 — **KHÔNG dùng Checklist 01 và 05** | Không dùng Quốc hiệu/Tiêu ngữ |
| **C — Quy phạm pháp luật (VBQPPL)** | Luật Ban hành VBQPPL; NĐ 34/2016/NĐ-CP sửa đổi bởi NĐ 154/2020 | Skill 30 (*xem ghi chú tham chiếu treo, Mục 6*); Checklist 02,03,04 | Ký hiệu **có chứa năm ban hành** (vd `38/2026/QĐ-UBND`) |
| **D — Đoàn thể** (3 tiểu-hệ, KHÔNG dùng chung 1 mẫu) | Mẫu 3.1–3.3 TB 597 mục III; QĐ 933/QĐ-TLĐ (14/5/2024, riêng Công đoàn) | **Checklist 09** (mới v2.21) | Xem bảng con dưới |

**[FACT]** 3 tiểu-hệ D — đặc thù KHÔNG được báo là lỗi:

| Tiểu-hệ | Quốc hiệu/Tiêu ngữ | Dòng thay thế | Ký hiệu số |
|---|---|---|---|
| D1 Công đoàn | **CÓ** | — | `Số: .../...-CĐCS` (kiểu hành chính) |
| D2 Đoàn Thanh niên | KHÔNG | `ĐOÀN TNCS HỒ CHÍ MINH` + 3 dấu sao (`***`) | `Số -...../ĐTN` (kiểu Đảng) |
| D3 Hội Sinh viên | KHÔNG | **Không có dòng tiêu đề nào** (khác D2) — theo đúng mẫu 3.3 TB 597, đây là đặc thù trình bày đã xác nhận, **KHÔNG được nêu là lỗi Mức 1/2** | `Số -...../HSV` (kiểu Đảng) |

**[FACT]** Lỗi thường gặp nhất đã xác nhận thật: hoán đổi thể thức D1↔D2 (dùng nhầm tiêu đề/Quốc hiệu của tiểu-hệ này cho tiểu-hệ kia).

**[UNKNOWN — CHƯA ĐỦ CĂN CỨ]** Nguồn cấp Trung ương riêng cho D2 (Đoàn Thanh niên) và D3 (Hội Sinh viên) tương đương QĐ 933/QĐ-TLĐ của Công đoàn — chưa xác nhận có tồn tại trong kho 01-04 hay không.

---

## 3. BẢN ĐỒ BỘ NHỚ VÀ QUY TRÌNH QUẢN LÝ TRẠNG THÁI

**[FACT]** Điểm nạp đầu tiên mỗi phiên làm việc, theo đúng thứ tự bắt buộc:
1. `09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md` — chỉ mục sự thật hiện hành
2. `SKILL.md` — bộ định tuyến và chốt an toàn
3. `references/Checklist/08-Quy-Uoc-Rieng-CDKT.md`
4. Skill/Checklist/Prompt theo loại văn bản đang xử lý
5. Process Memory gần nhất cùng hồ sơ
6. Tệp đầu vào hiện tại

Nếu gặp "hợp nhất"/"VBHN", nạp `00b-Trigger-Vien-Dan-Van-Ban-Hop-Nhat.md`.
Nếu gặp tình huống chuyên biệt, nạp `31-Quy-Tac-Van-Hanh-Theo-Tinh-Huong.md`.

**[FACT]** Thứ tự ưu tiên nguồn (không được đảo): (1) văn bản pháp luật/nội bộ đã kiểm chứng → (2) SKILL.md/Mẫu prompt/Checklist → (3) quy ước riêng Trường → (4) Nhật ký cập nhật → (5) Process Memory → (6) lịch sử hội thoại AI → (7) suy luận mô hình. **Không dùng lớp 5–7 để ghi đè lớp 1–4.**

**[FACT]** Nguyên tắc `superseded`/`superseded_by`: không xóa lịch sử nếu cần truy vết. Khi một quy tắc/tệp hết hiệu lực, gắn `superseded`, ghi `superseded_by`, ghi ngày thay thế. Không dùng nội dung hết hiệu lực cho kết luận hiện hành. Ví dụ thật đã áp dụng: Nhật ký v1.6 → `superseded_by` Nhật ký v1.7.

**[FACT]** "Temporal legal check" (kiểm tra hiệu lực theo thời gian): mọi quan hệ thay thế, sửa đổi,
bãi bỏ hoặc chuyển tiếp phải được đọc từ văn bản chính thức tại thời điểm rà soát. Không dùng tên tệp,
ghi nhớ cũ hoặc lịch sử hội thoại để kết luận. Trường hợp NĐ 334/2026/NĐ-CP đang được quản lý tại KI-008.

**[CONFLICT]** Cơ chế Single Source of Truth (SSOT) cho số phiên bản: **hiện KHÔNG có** — đây là khoảng trống kiến trúc thật, không phải đề xuất lý thuyết. Bằng chứng: đã xảy ra **ít nhất 6 lần** CONFLICT phiên bản giữa `SKILL.md` (trong `.skill` đã đóng gói), `SKILL.md` rời, `00-README.md`, và Nhật ký — bao gồm 1 lần "phân kỳ hai chiều" (06/9/2026: bản đóng gói v2.21 có Checklist 09/6 Nguyên tắc mà bản rời chưa có, NHƯNG bản rời lại có nhắc `99-Kinh-Nghiem/`/`00c-Co-Che-Tu-Kich-Hoat.md` mà bản đóng gói bị thiếu). Quy tắc 19 trong `SKILL.md` v2.21 ghi nhận: **không đủ để chỉ so sánh số phiên bản — phải đọc đối chiếu nội dung từng mục khi hợp nhất**.

**[PROPOSAL]** Để có SSOT thật, nên áp dụng mô hình: 1 file duy nhất là nguồn số phiên bản (ví dụ chỉ `SKILL.md` trong `.skill` đã đóng gói), mọi file khác (`00-README.md`, Nhật ký, báo cáo xuất ra) đọc số phiên bản **động** tại thời điểm chạy thay vì ghi cứng — cơ chế `_read_skill_version()` trong `build_ktc897_report.py` đã áp dụng đúng ý tưởng này cho báo cáo xuất ra, nhưng chưa mở rộng cho `00-README.md`/Nhật ký (hiện vẫn ghi cứng thủ công).

---

## 4. DIỆN TÍCH BỀ MẶT CÔNG CỤ VÀ KỸ THUẬT XỬ LÝ DỮ LIỆU

**[FACT]** Luồng `tools/_read_input_properties.py` (v1.1): đọc thuộc tính định dạng THẬT của file `.docx` đầu vào — lề trang qua `section.*_margin`, cỡ chữ/đậm qua `run.font.size`/`run.font.bold` — đối chiếu NĐ 30 (lề) và TB 597 (cỡ chữ trích yếu). Đây là bước bổ sung bên cạnh đọc nội dung chữ (`paragraph.text`), **không thay thế** — thiếu bước này sẽ luôn bỏ sót lỗi định lượng bất kể Checklist viết chi tiết đến đâu. Đã vá lỗi làm tròn ngưỡng (v2.17): áp dụng `round(val, 1)` + `EPS=0.01` cho cả 4 lề, có 3 test case xác nhận PASS.

**[FACT]** Luồng `tools/build_ktc897_report.py` (v3.4): xuất báo cáo 8 phần, A4 ngang (297×210mm), lề 20mm đều 4 phía, Times New Roman 14pt. Cấu trúc: I. Thông tin chung → II. Kết quả rà soát chi tiết → III. Nội dung đạt → **IV. Bảng tổng hợp** → **V. Thẩm định chuyên môn (bắt buộc có điều kiện — vẫn in tiêu đề nếu không có, ghi "Không có nội dung cần thẩm định")** → VI. Đánh giá tổng thể → VII. Kết luận → **VIII. Phân tích khả thi (tùy chọn thật — chỉ in khi được yêu cầu)**.

**[FACT]** Ngưỡng an toàn transcribe thủ công qua chat đã xác nhận bằng thực nghiệm lặp lại nhiều lần: dưới **~15.000 ký tự base64 (~11KB file)** tương đối an toàn; 15.000–30.000 ký tự rủi ro cao, kết quả không nhất quán (có lần thành công lệch vài byte vô hại, có lần lệch 22 byte gây lỗi UTF-8 thật); trên khoảng đó (đã thử tới 60.000+ ký tự) **không nên tự tái tạo qua chat** — phải dùng `copy_file` (server-side) hoặc đưa file cho người dùng tự tải lên/xuống trực tiếp.

**[FACT]** File text thuần (Markdown) dùng tham số `textContent` (không qua base64) đã xác nhận đáng tin cậy hơn nhiều so với base64, kể cả với file lớn (~35KB) — vì không có bước mã hóa/giải mã trung gian có thể gây lệch.

**[FACT]** 3 lớp lỗi thứ tự schema OOXML đã xác nhận thật khi dùng `python-docx`, khiến Word thật có thể từ chối mở file dù LibreOffice vẫn hiển thị bình thường:

```python
# Vị trí bắt buộc theo CT_TblPrBase: ... tblBorders, shd, tblLayout, tblCellMar, tblLook ...
# Vị trí bắt buộc theo CT_TcPrBase: ... tblBorders, shd, noWrap, tcMar, textDirection, tcFitText, vAlign, hideMark ...
# KHÔNG được append() mù ở cuối — phải chèn đúng trước phần tử kế tiếp hợp lệ nếu đã tồn tại.
def _set_tbl_layout_fixed(tbl):
    tblPr = tbl.tblPr
    existing = tblPr.find(qn("w:tblLayout"))
    if existing is not None:
        existing.set(qn("w:type"), "fixed")
        return
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    insert_before = None
    for tag in ("w:tblCellMar", "w:tblLook", "w:tblCaption", "w:tblDescription"):
        found = tblPr.find(qn(tag))
        if found is not None:
            insert_before = found
            break
    if insert_before is not None:
        insert_before.addprevious(layout)
    else:
        tblPr.append(layout)
```

**[FACT]** 2 lỗi python-docx mặc định khác đã vá trong `build_ktc897_report.py` v3.4:
- `docProps/app.xml` để mặc định `Pages=1, Words=0` (thư viện không tự dàn trang) — khiến một số trình xem (thanh trạng thái Word, Windows Explorer) hiển thị sai "chỉ có 1 trang". Vá bằng cách render PDF thật để đếm trang, ghi đè sau khi lưu.
- `<w:zoom>` thiếu thuộc tính `w:percent` bắt buộc.

**[FACT]** Ràng buộc bảng bắt buộc: phải đặt `t.autofit = False` **và** khai `w:tblLayout type="fixed"` **và** ghi `w:w` vào từng `w:gridCol` — thiếu bất kỳ bước nào, Word bỏ qua width đã đặt, bảng co lại và tài liệu phình số trang. Tổng width mọi bảng phải **≤ 25,7cm** (A4 ngang 29,7cm trừ lề 20mm mỗi bên) — script v3.4 từ v3.4 trở đi tự `raise ValueError` thật nếu vượt, không chỉ ghi chú.

---

## 5. BỘ QUY TẮC CẮM CỜ VÀ TIÊU CHÍ PHÂN LOẠI LỖI

**[FACT]** 4 mức phân loại (thống nhất với Mẫu prompt 897 và Skill 28):

| Mức | Định nghĩa |
|---|---|
| **Mức 1 – Bắt buộc sửa** | Trái pháp luật, viện dẫn sai/hết hiệu lực, sai thẩm quyền, sai căn cứ ban hành, thiếu điều khoản bắt buộc, mâu thuẫn làm thay đổi nội dung |
| **Mức 2 – Cần sửa** | Sai thể thức, sai kỹ thuật trình bày, sai logic, sai viện dẫn nội bộ, thiếu tính thống nhất |
| **Mức 3 – Nên sửa** | Văn phong, câu chữ, cách trình bày |
| **Mức 4 – Góp ý nâng cao** | Đề xuất hoàn thiện, không bắt buộc; cũng dùng cho trường hợp chưa đủ căn cứ xác minh |

**[FACT]** Cổng chặn (Release Gate) đã áp dụng thật trong `build_ktc897_report.py` v3.4: `raise ValueError` nếu bảng vượt khổ giấy — đây là cổng chặn kỹ thuật đầu tiên của hệ (trước đó mọi ràng buộc chỉ là ghi chú, không có gì thực sự ngăn lại).

**[FACT]** 3 trường bắt buộc trong mục "Thông tin trách nhiệm" của mọi báo cáo xuất ra:
1. **Nguồn dữ liệu đã dùng** — liệt kê đầy đủ file/văn bản đã đối chiếu
2. **Người kiểm tra** — **KHÔNG được điền chỉ tên công cụ AI kèm trạng thái "Chính thức"** — phải là người thật chịu trách nhiệm; script tự in cảnh báo ra `stdout` nếu gọi hàm thiếu tên người
3. **Trạng thái phê duyệt** — mặc định `"BẢN NHÁP – Kết quả AI chỉ có giá trị tham khảo. Cần phê duyệt chính thức trước khi dùng."`, chỉ đổi thành "ĐÃ PHÊ DUYỆT" khi có xác nhận thật của người có thẩm quyền

---

## 6. NHẬT KÝ SỰ CỐ, ANTI-PATTERNS VÀ BÀI HỌC VẬN HÀNH

**[FACT]** Danh sách lỗi kiến trúc đã gặp thật, theo thời gian:

| Thời điểm | Lỗi | Bản chất |
|---|---|---|
| v2.13 (25/8) | Lỗi nạp YAML | `SKILL.md` không bắt đầu đúng `---` frontmatter — Claude.ai từ chối nạp Skill |
| v2.4, v2.6 | Báo "hoàn thành" nhưng thay đổi chưa tồn tại thật trong gói `.skill` | Chưa đối chiếu byte thật trước khi công bố |
| 26/8 (3 lần liên tiếp) | Đứt gãy Base64 khi copy tay | Ban đầu bị hiểu nhầm là "giới hạn môi trường", sau xác minh lại bằng magic bytes/EOCD record mới xác định đúng là lỗi copy tay chuỗi dài |
| v2.17–v2.18 | Khoảng trễ giữa `.skill` và `README/SKILL.md` rời | Đóng gói xong nhưng tài liệu điều khiển vệ tinh chưa cập nhật kịp |
| 06/9 (v2.21) | **Phân kỳ hai chiều** | Xem chi tiết Mục 3 — lỗi CONFLICT phức tạp nhất đã gặp, không giải quyết được bằng "chọn bản có số cao hơn" |
| 07/9 | Lỗi hỏng ký tự thật (mojibake) lặp lại giống hệt ở 2 file độc lập (`00-README.md`, `11-Tong-Hop-Nguoi-Dung-KTC897.md`) | Nguyên nhân gốc chưa xác định — nghi ngờ phát sinh từ một thao tác copy/paste chung nguồn |
| Nhiều lần | 5 lỗi thứ tự schema OOXML (`tblLayout`, `tcMar`, `shd`, `docProps/app.xml`, `<w:zoom>`) | Chỉ phát hiện được khi chủ động chạy `validate.py` — không thấy được bằng mắt qua LibreOffice |

**[FACT]** Anti-patterns cần tránh khi duy trì/nâng cấp:
- Tin lời xác nhận "đã điều chỉnh" mà không đọc lại trực tiếp file/Drive.
- Coi "đã sửa trên Drive" = "đã cập nhật trong Claude.ai" (2 khái niệm khác nhau — phải đóng gói lại `.skill` và cài đè).
- Tự tái tạo nội dung file lớn qua chat (base64 hoặc text dài) thay vì dùng `copy_file`/API hoặc đưa file cho người dùng tự chuyển.
- Ghi cứng số phiên bản ở nhiều nơi tách rời mà không có SSOT.
- Kết luận "Đạt" dựa trên trích dẫn cụt hoặc suy diễn thay vì đọc trọn văn bản/tính toán lại độc lập.

---

## 7. HƯỚNG DẪN BẢO TRÌ, CẬP NHẬT VÀ LỘ TRÌNH NÂNG CẤP

**[FACT]** Quy trình 4 bước bắt buộc khi cập nhật Skill/script/checklist:
1. Sửa nội dung trực tiếp trên Drive.
2. Chạy `validate.py` (schema XSD) trên mọi file `.docx` được tạo ra.
3. Đóng gói lại thành `.skill` mới, tăng số phiên bản.
4. Cài đè bản `.skill` mới vào Claude.ai — xác nhận lại bằng cách hỏi Claude phiên bản đang chạy.

**[FACT]** Bộ hồi quy 30 lỗi (`13-Regression-Test/`, `File-Test-Loi-KTC897.docx`): dùng để đo khách quan qua các phiên bản thay vì chỉ mô tả định tính. Kết quả đã ghi nhận: baseline 8/28 đúng hoàn toàn (28,6%) → sau khi tích hợp `_read_input_properties.py` và vá lỗi làm tròn ngưỡng: 12/30 (40%). **[UNKNOWN — CHƯA ĐỦ CĂN CỨ]**: chưa chạy lại bộ hồi quy sau khi bổ sung Checklist 09 (Hệ D, v2.21) — chưa có số liệu đo cải thiện thật cho phần này.

**[FACT]** Định hướng nâng cấp v3.0: đã phát hiện một bộ tệp dùng kiến trúc khác (thư mục `core/`, các skill con dạng plugin: `review`, `compare`, `normalize`, `quick-review`, cơ chế tag XML kiểu `<system_context>`). Đây là **định hướng phát triển chính thức** do Phòng TH-HC&QT chủ trương cho giai đoạn tiếp theo, **không phải rác kỹ thuật**. Quyết định hiện hành: ưu tiên chạy thực chiến ổn định v2.21 trước; kế hoạch nâng cấp v3.0 **tạm hoãn có chủ đích** để nhường thời gian cho bàn giao và vận hành thử thực tế.

**[UNKNOWN — CHƯA ĐỦ CĂN CỨ]** Các chi tiết kỹ thuật cụ thể của v3.0 như "tích hợp Gemini 3.6 Flash", "thinking_level", "tối ưu hóa XML Tags", "Connector Mock Engine" — **không có căn cứ trong bất kỳ nguồn nào đã xác nhận của hệ này** (SKILL.md, CHANGELOG.md, Mô tả kỹ thuật gửi Anthropic, Nhật ký cập nhật). Không đưa vào như sự thật. Nếu người tiếp quản có nguồn riêng xác nhận các chi tiết này (ví dụ trao đổi trực tiếp với bên phát triển nhánh v3.0), cần bổ sung nguồn cụ thể trước khi đưa vào tài liệu chính thức.

**[PROPOSAL]** Gợi ý cho người tiếp quản khi tiếp tục v3.0 (dựa trên bài học từ v2, không phải thông số kỹ thuật của v3.0):
- Làm rõ mức độ hoàn thiện thật của các file `core/` hiện có trước khi phát triển tiếp — chưa được kiểm định kỹ như v2.21.
- Áp dụng mô hình SSOT cho số phiên bản ngay từ đầu (xem Mục 3) — nguyên nhân gốc của phần lớn CONFLICT đã gặp ở v2.
- Dùng bộ hồi quy 30 lỗi của v2 làm chuẩn kiểm định chéo khi v3.0 đủ chín muồi, tránh thụt lùi độ chính xác so với v2 đã đạt.

---

## KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG (theo đúng 4 tiêu chí đã yêu cầu)

1. **Có bịa đặt thông số API/lệnh không có trong nguồn không?** → Không. Riêng nội dung "Gemini 3.6 Flash/thinking_level/Connector Mock Engine" mà yêu cầu gốc đề nghị đưa vào Mục 7 đã bị từ chối đưa vào như sự thật, đánh dấu `[UNKNOWN — CHƯA ĐỦ CĂN CỨ]` thay vì bịa ra.
2. **Đã phân loại đúng `[FACT]/[INFERENCE]/[PROPOSAL]/[UNKNOWN]/[CONFLICT]` chưa?** → Có, áp dụng xuyên suốt cả 7 mục.
3. **Đã làm rõ quy trình xử lý lỗi schema OOXML và nguyên tắc SSOT phiên bản chưa?** → Có — Mục 4 (kèm code thật đã dùng) và Mục 3 (nêu rõ đây là `[CONFLICT]` — khoảng trống thật, chưa phải đã giải quyết xong).
4. **Đã đảm bảo không ghi tên AI/Claude vào trường "Người kiểm tra" chưa?** → Có, nêu rõ tại Mục 5 kèm cơ chế cảnh báo tự động đã có trong script.
