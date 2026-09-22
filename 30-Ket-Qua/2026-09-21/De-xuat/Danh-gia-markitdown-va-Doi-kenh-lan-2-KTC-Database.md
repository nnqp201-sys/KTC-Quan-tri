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

Đếm tại chỗ: **826 `.docx` · 212 `.md` · 54 `.xlsx` · 53 `.pdf` · 36 `.doc` · 15 `.dotx`** — khớp số liệu
Bước 0.

**Tốc độ đo thật, mẫu ngẫu nhiên 40 tệp:**

| Cách đọc | Mỗi tệp | Toàn bộ 826 `.docx` |
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

**Thêm một số liệu ngoài dự đoán:** quét cả 826 tệp tìm tệp có trên 20 dấu vết Track Changes — **không có
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

Định dạng `.doc` cũ (Word 97-2003) **không được hỗ trợ**. Kho có **36 tệp** loại này, gồm cả văn bản đáng
kể như *Kế hoạch hợp tác doanh nghiệp giai đoạn 2025-2030*.

Cách xử lý, theo thứ tự ưu tiên: mở bằng Word rồi lưu lại thành `.docx` (36 tệp, làm tay được, nhưng **là
thao tác ghi — phải do chủ kho quyết**); hoặc dùng LibreOffice chuyển hàng loạt sang bản `.docx` **đặt ở
thư mục khác**, không đụng bản gốc. Chưa xử lý thì **ghi cả 36 tệp vào `CAN-XAC-MINH.md`**, đừng để rơi im
lặng.

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

**Một việc phải làm rõ trước:** tài khoản này **chỉ đọc** với KTC-Database. Vậy chỉ mục dựng ra đặt ở đâu?
Hai cách, cần chủ kho chọn:

- **(a)** Dựng tại chỗ rồi giao thư mục `06-Chi-Muc/` cho chủ kho tự đặt vào. Sạch về thẩm quyền, nhưng
  mỗi lần cập nhật lại phải chuyển tay.
- **(b)** Chủ kho chạy đúng kịch bản đó trên máy của họ — kho cũng đồng bộ về máy họ như vậy. Dựng xong là
  nằm đúng chỗ, tự cập nhật được về sau.

Em nghiêng về **(b)**, vì chỉ mục cần dựng lại định kỳ, mà cách (a) sẽ thành việc chuyển tay hàng tháng —
kiểu việc chắc chắn bị bỏ quên, và **chỉ mục lệch nguy hiểm hơn chỉ mục thiếu**.

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
