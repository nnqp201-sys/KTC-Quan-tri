# Đánh giá markitdown — và đề nghị đổi kênh lần thứ hai

**Ngày:** 22/9/2026 · **Đo trên máy `nnqp201-sys`, không phải ước tính**
**Liên quan:** `Tra-loi-v2.0-Duyet-chay-thu-KTC-Database.md`

---

## Kết luận ngắn

**Đừng chạy Apps Script.** Kho KTC-Database **đã có sẵn trên máy này** dưới dạng thư mục đọc được bình
thường. Trích toàn bộ tại chỗ mất **khoảng 28 phút, một lần chạy, không hạn mức, không token, không trigger,
không tệp tạm nào sinh trên Drive.**

Toàn bộ bài toán 90 phút/ngày, chờ 3–6 giờ, `LockService`, ghi tiến độ, chia hai lượt — **biến mất**.

---

## 1. Kho có sẵn tại chỗ — đây là phát hiện làm đổi mọi thứ

```
I:\.shortcut-targets-by-id\18ZNI-vS4HO4T0ZOmOYChu62GQB8cRJEE\KTC-Database
```

Mã `18ZNI-vS4HO4T0ZOmOYChu62GQB8cRJEE` **trùng khớp** mã thư mục gốc mà phiên bên kia báo. Google Drive for
Desktop đã đồng bộ thư mục dùng chung này về máy; nó không hiện trong `My Drive` mà nằm ở nhánh
`.shortcut-targets-by-id`, nên dễ tưởng là không có.

Đếm tại chỗ: **830 `.docx` · 233 `.md` · 54 `.xlsx` · 53 `.pdf` · 33 `.doc` · 15 `.dotx`**.

> **Sửa số liệu 22/9/2026.** Bản đầu của tài liệu này ghi 826 `.docx` / 212 `.md` / 36 `.doc`. Sai, do lần
> đếm đầu chạy khi Google Drive chưa liệt kê xong thư mục. Đếm lại bằng cùng một bộ luật loại trừ trên cả
> hai ổ cho kết quả khớp nhau. Con số đúng là ở trên; ước tính thời gian bên dưới không đổi đáng kể.

**Tốc độ đo thật, mẫu ngẫu nhiên 40 tệp:**

| Cách đọc | Mỗi tệp | Toàn bộ 830 `.docx` |
|---|---|---|
| Qua Drive API (phiên kia đo) | 27,5 giây | **~7,3 giờ** |
| Đọc thẳng XML tại chỗ | **0,78 giây** | **~11 phút** |
| Qua markitdown tại chỗ | ~2 giây | **~28 phút** |

Chênh **35–40 lần**. Không phải markitdown nhanh — mà là **đọc tại chỗ** nhanh. Con số 1,2 giây trong lệnh
gốc không sai; nó chỉ bị hiểu nhầm là đo qua API.

---

## 2. markitdown làm được gì — đo từng ca

### 2.1 Track Changes: giải quyết triệt để, không cần Google Docs

Dựng một tệp `.docx` có kiểm soát: một câu thường, một đoạn `<w:ins>`, một đoạn `<w:del>`, một câu kết.

| Bộ đọc | Kết quả |
|---|---|
| **markitdown** | `'CAU BINH THUONG…\n\nDOAN MOI THEM VAO…\n\nCau ket.'` — **giữ `<w:ins>`, bỏ `<w:del>`** |
| **python-docx** (đang dùng) | `['CAU BINH THUONG…', '', '', 'Cau ket.']` — **hai đoạn giữa ra rỗng** |

markitdown cho đúng **nội dung sau khi chấp nhận sửa đổi** — thứ mà v2.0 phải chuyển đổi qua Google Docs
mới lấy được. Vậy:

- **Bỏ toàn bộ nhánh chuyển đổi Google Docs.** Không sinh tệp tạm trên Drive, không cần `06-Chi-Muc/_tam/`.
- **Nhãn `nguon_chu` chỉ còn hai giá trị**: `docx-truc-tiep` và `OCR`. Bỏ `docs-convert`.
- Ngưỡng 200 ký tự và điều kiện kích thước 30 KB không còn cần thiết.

**Thêm một số liệu ngoài dự đoán:** quét cả 826 tệp đọc được tìm tệp có trên 20 dấu vết Track Changes — **không có
tệp nào**. Bản dự thảo QĐ-1710 mà phiên kia thử nghiệm **không nằm trong kho này**. Vấn đề Track Changes
với KTC-Database là **giả định, không phải sự thật đã đo**. Dù vậy vẫn nên dùng markitdown, vì nó xử lý
đúng mà không tốn gì thêm.

### 2.2 PDF: chỉ 11 tệp cần OCR, không phải 53

Chạy `pdfminer` trên cả 53 tệp:

| | Số tệp |
|---|---|
| **Có lớp chữ, đọc được ngay** | **42** |
| Không có lớp chữ, cần OCR | **11** |

Con số "12/12 mẫu không có lớp chữ" của lệnh gốc là **mẫu rơi trúng đúng nhóm xấu**. Thực tế **79% khối PDF
đọc được ngay**, kể cả tệp 12,2 MB — nó ra **497.342 ký tự** và đoạn cuối là danh mục tài liệu tham khảo
hoàn chỉnh, tức **không cụt**. Câu hỏi "tệp 12,2 MB có bị OCR cụt giữa chừng không" vì vậy không còn.

**Phép kiểm đầu của em cũng sai một ca và phải sửa.** Lần đầu em chỉ đọc 3 trang đầu mỗi tệp cho nhanh →
báo 12 tệp thiếu chữ. Đọc lại toàn bộ trang thì tệp `QD-2664` có chữ đầy đủ; 3 trang đầu chỉ là bìa ảnh.
**Phép đo nhanh tạo ra một báo động giả 8%.** Số đúng là 11, không phải 12.

Trong 11 tệp đó có ít nhất **3 cặp trùng nội dung khác tên** (`QD-635` hai bản, `QD-543`/`543 QDUB`,
`CV-1400` hai bản) — thực chất khoảng **8 văn bản**. OCR 8 tệp là việc vặt.

### 2.3 Chỗ markitdown KHÔNG làm được — 36 tệp `.doc`

```
LOI UnsupportedFormatException: No converter attempted a conversion
```

Định dạng `.doc` cũ (Word 97-2003) **không được hỗ trợ**. Kho có **33 tệp** loại này, gồm cả văn bản đáng
kể như *Kế hoạch hợp tác doanh nghiệp giai đoạn 2025-2030*.

Cách xử lý, theo thứ tự ưu tiên: dùng LibreOffice chuyển hàng loạt sang `.docx` **đặt ở thư mục khác**,
không đụng bản gốc; hoặc mở bằng Word rồi lưu lại — 33 tệp, làm tay được, nhưng **là thao tác ghi đè lên
vùng bản gốc**. Chưa xử lý thì **ghi cả 33 tệp vào `CAN-XAC-MINH.md`**, đừng để rơi im lặng.

### 2.4 `.xlsx`: chạy được, chất lượng thấp

Đọc được, nhưng đầu ra lẫn nhiều `Unnamed: 1`, `NaN` từ ô trống. Đủ để **tìm**, không đủ để **đọc**. Với 54
tệp thì chấp nhận được; đừng kỳ vọng hơn.

---

## 3. Về lệnh cài đặt trong câu hỏi

```bash
git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
```

Ba điểm:

1. **`git@github.com:` là đường SSH — máy này không có khóa SSH GitHub.** Lệnh clone sẽ hỏng ngay. Dùng
   `https://github.com/microsoft/markitdown.git` nếu thật sự cần mã nguồn.
2. **Không cần clone.** `pip install` thẳng từ PyPI là đủ. `-e` (editable) chỉ dành cho người sửa mã
   markitdown.
3. **`[all]` kéo thừa rất nhiều** — nhận dạng giọng nói, YouTube, Azure Document Intelligence. Cho việc này
   chỉ cần:

```powershell
pip install "markitdown[docx,pdf,xlsx]"
```

**Hai lỗi thật đã gặp khi cài, để khỏi mất thời gian:**

- markitdown kéo theo `magika` → `onnxruntime`, có tệp đường dẫn rất dài. Cài vào thư mục sâu thì
  **hỏng giữa chừng** với `OSError [Errno 2]`. Cài vào đường dẫn ngắn, hoặc bật Long Path của Windows.
- Cài vào `%TEMP%` thì **`python.exe` của môi trường ảo biến mất giữa phiên** (dọn rác hoặc phần mềm diệt
  virus). Cài vào chỗ ổn định, ví dụ `D:\venv\markitdown`.

---

## 4. Đề nghị

**Chạy trích xuất tại máy này, không chạy Apps Script.** Ưu điểm không chỉ là nhanh:

| | Apps Script | Chạy tại chỗ |
|---|---|---|
| Thời gian chờ | 3–6 giờ, có thể sang ngày 2 | **~28 phút, một lần** |
| Hạn mức | 90 phút/ngày, sát mép | **không có** |
| Ghi lên Drive khi chạy | tệp tạm cho mỗi lần chuyển đổi | **không ghi gì** |
| Track Changes | phải chuyển đổi qua Google Docs | **đọc thẳng** |
| Rủi ro dở dang | cao — phải ghi tiến độ, hẹn giờ | **thấp** |

### Chuyện thẩm quyền đã rõ — nhưng còn một khóa kỹ thuật

Kho do chính người dùng quản lý; `truong.cdkontum` và `phongthhcqt` dùng chung một Drive. Vậy **không cần
chuyển việc sang tài khoản khác** — chạy ngay tại đây, chủ kho tự quyết.

**Nhưng `guard_destructive.py` của plugin đang chặn cứng:**

```python
if "/KTC-Database/" in path or path.endswith("/KTC-Database"):
    deny("KTC-Database is read-only for the review plugin.")
```

Chặn **mọi** đường dẫn có `KTC-Database`, không phân biệt vùng. Ghi `06-Chi-Muc/` cũng bị chặn.

Đề nghị sửa cho đúng ý định ban đầu thay vì tắt guard: **giữ chặn `01`–`05` và `11-Input`, mở riêng
`06-Chi-Muc/`**. Điều cần bảo vệ là **bản gốc**, không phải cái tên thư mục. Kèm theo, `CLAUDE.md` phải ghi
lại cho khớp — quy tắc và guard nói khác nhau thì sớm muộn một trong hai bị bỏ qua.

Đây là **nới một luật an toàn**, nên phải do người dùng quyết rõ ràng, không tự làm.

### Hai bản kho trên máy — dùng bản nào

Máy này đang gắn **hai ổ Drive**, và cả hai đều có KTC-Database:

| | Đường dẫn | Là gì |
|---|---|---|
| `H:` | `H:\My Drive\KTC-Database` | Drive của tài khoản **sở hữu** kho |
| `I:` | `I:\.shortcut-targets-by-id\18ZNI-…\KTC-Database` | Cùng thư mục đó, nhìn từ tài khoản được chia sẻ |

Đối chiếu từng đường dẫn: **1.250/1.251 tệp trùng khớp**, lệch đúng 3 tệp — tức **cùng một thư mục**, chỉ
lệch nhịp đồng bộ. Không phải hai kho khác nhau.

**Dùng `H:`.** Đó là bản của tài khoản sở hữu, và `duong_dan.py` của hệ vốn đã tự tìm ra đúng đường đó.
Nhưng vì lệch nhịp là có thật, **kịch bản phải ghi rõ nó đọc từ ổ nào** vào `00-README.md` — hai người chạy
trên hai ổ rồi so kết quả mà không biết điều này thì sẽ tưởng chỉ mục sai.

**Kịch bản Apps Script v2.0 không bỏ đi.** Nó vẫn là đường duy nhất nếu về sau ai đó cần dựng chỉ mục mà
không có máy đồng bộ Drive. Giữ lại, ghi rõ là phương án dự phòng.

---

## 5. Việc còn phải kiểm trước khi tin hẳn

- [ ] Chạy markitdown trọn `02-KTC-Regulations` (361 tệp), **đếm số tệp ra dưới 200 ký tự** — đó là danh
      sách tệp nghi trích hỏng, không phải tệp ngắn.
- [ ] So 10 tệp bất kỳ: mở bản gốc, đối chiếu đoạn đầu và đoạn cuối với chữ trích ra.
- [ ] Đo lại phép tìm thật: qua chỉ mục so với chỉ mục sẵn của Drive, trên **ít nhất 5 cụm từ**, rồi mới
      ghi tỷ lệ phủ vào `00-README.md`.
- [ ] Quyết cách xử lý 36 tệp `.doc`.
