# Lệnh gửi tài khoản `phongthhcqt` — dựng lớp chỉ mục cho KTC-Database

**Ngày lập:** 21/9/2026 · **Người lập:** tài khoản `nnqp201-sys` (P-THHC)
**Gửi:** người vận hành tài khoản `phongthhcqt@gmail.com` — chủ sở hữu kho `KTC-Database` trên Google Drive
**Cách dùng:** dán toàn bộ phần trong khung dưới vào một phiên Claude của tài khoản đó (Chat, Cowork hoặc Code)
đã kết nối Google Drive.

**Vì sao phải gửi sang tài khoản khác:** kho là **chỉ đọc** với tài khoản `nnqp201-sys` — hook chặn mọi thao
tác ghi. Chỉ tài khoản sở hữu mới ghi được.

---

## Hiện trạng đã đo (21/9/2026)

Đo bằng hai cách độc lập, chênh ~4% do `du` tính theo khối đĩa:

| Chỉ số | Giá trị |
|---|---|
| Tổng | **1.219 tệp · ~300 MB** |
| `.docx` | 818 tệp · 199 MB · trung bình **8.648 ký tự/tệp** |
| `.pdf` | 53 tệp · 75 MB · **12/12 mẫu không có lớp chữ** (nghi ảnh quét) |
| `.md` (metadata sidecar) | 212 tệp · 0,6 MB |
| `.xlsx` | 54 tệp · 1,9 MB |
| Phủ metadata sidecar | **36/818 tệp `.docx` = 4%** |
| Tốc độ đọc `.docx` qua Drive | **~1,2 giây/tệp** → quét toàn kho ≈ **16 phút** |

**Kết luận:** kho **không nặng**. 300 MB là không đáng kể. Ba điểm nghẽn thật là (1) tra cứu nội dung quá
chậm, (2) 199 MB `.docx` chỉ chứa ~7 MB chữ — 96% là bao bì OOXML, (3) 75 MB PDF hiện vô hình với mọi
phép tìm kiếm.

---

## KHUNG LỆNH — dán từ đây trở xuống

Bạn đang làm việc trên kho `KTC-Database` của Trường Cao đẳng Kon Tum, đặt tại Google Drive của tài khoản
này. Nhiệm vụ: **dựng một lớp chỉ mục chữ đặt cạnh kho, không đụng bản gốc.**

### Đọc trước khi làm

Bắt buộc đọc ba tệp quy ước sẵn có trong kho, và làm theo chúng — không tự đặt quy ước mới:

1. `references/00-Metadata-Schema.md` — schema 11 trường + trường theo loại + 3 trường trách nhiệm.
2. `references/01-Checklist-Metadata.md` — checklist A/B/C/D, đặc biệt mục D.
3. `references/03-Quy-Trinh-Nap-Lieu-2-Tang.md` — quy trình nạp hai tầng.

### Ràng buộc không được vi phạm

1. **Không sửa, không đổi tên, không di chuyển, không xóa bất kỳ tệp nào** trong `01-Legal-Database`,
   `02-KTC-Regulations`, `03-Templates`, `03-Templates(1)`, `04-Good-Documents`, `05-De-an-De-tai`,
   `11-Input`. Chỉ **đọc**.
2. **Không chuyển đổi định dạng bản gốc.** Tệp `.docx` đã ký *chính là* văn bản — thể thức, chữ ký số,
   Track Changes nằm trong đó. Checklist mục D của chính kho đã ghi: *"Tệp nguồn được copy/upload/update
   nguyên byte; không tái tạo Office/PDF từ nội dung trích xuất."*
3. **Chữ trích xuất là dữ liệu PHÁI SINH**, không thay thế bản gốc. Mọi kết luận pháp lý vẫn phải mở bản
   gốc đối chiếu.
4. **Không bịa metadata.** Trường nào không xác minh được thì ghi `Cần xác minh` hoặc `Không xác định` —
   đúng mục B của checklist. Không suy diễn từ tên tệp.
5. **Không ghi vào `03-Templates(1)`** (checklist mục A đã cấm).
6. Việc nào cần xóa/đổi tên mà chưa được phép thì **đưa vào danh sách chờ**, không tự làm.

### Nơi đặt chỉ mục

Tạo **một thư mục mới ở cấp cao nhất**: `06-Chi-Muc/`. Không đặt xen vào 01–05.

```
06-Chi-Muc/
├── CHI-MUC.jsonl          mỗi dòng một tài liệu (xem cấu trúc dưới)
├── text/                  chữ đã trích, soi gương cấu trúc thư mục gốc
│   ├── 01-Legal-Database/...
│   └── 02-KTC-Regulations/...
├── CAN-XAC-MINH.md        danh sách tệp không trích được hoặc thiếu dữ liệu
└── 00-README.md           cách dựng lại, ngày dựng, phạm vi
```

Đặt riêng một thư mục để nếu hỏng thì **xóa cả thư mục và dựng lại**, không ảnh hưởng gì tới 01–05.

### Mỗi dòng `CHI-MUC.jsonl` gồm

```json
{
  "duong_dan": "02-KTC-Regulations/02-01-.../TB-1052-TB-CDKT_....docx",
  "ten_tep": "TB-1052-TB-CDKT_Mau-Ban-cam-ket....docx",
  "kho": "02",
  "kich_thuoc": 48213,
  "sha256": "…",
  "ngay_sua": "2026-09-15T10:03:04",
  "so_ky_tu": 8648,
  "tep_chu": "text/02-KTC-Regulations/.../TB-1052….txt",
  "co_sidecar": true,
  "so_hieu": "1052/TB-CĐKT",
  "ngay_ban_hanh": "15/09/2026",
  "trich_yeu": "…",
  "trang_thai_trich": "OK"
}
```

`so_hieu`, `ngay_ban_hanh`, `trich_yeu` **chỉ điền khi đọc được chắc chắn từ nội dung**; không chắc thì để
`null`, đừng đoán từ tên tệp.

### Làm theo 5 bước, dừng lại báo cáo sau mỗi bước

**Bước 0 — tự đo lại.** Đừng tin số ở trên. Đếm lại số tệp theo đuôi và theo thư mục, so với bảng hiện
trạng. Lệch nhiều thì báo trước khi làm tiếp.

**Bước 1 — chạy thử trên một kho con.** Làm `02-KTC-Regulations` (361 tệp) trước. Đo và báo: thời gian
trích toàn bộ, tổng dung lượng thư mục `text/` sinh ra, số tệp trích lỗi. Sau đó **đo lại một phép tìm
thật**: tìm cụm "cam kết thực hiện nhiệm vụ" bằng chỉ mục so với quét trực tiếp `.docx`, ghi rõ hai con số
thời gian. Chưa thấy chênh lệch rõ thì dừng, báo lại — đừng làm tiếp cả kho.

**Bước 2 — trích toàn bộ 01–05.** Với `.docx` đọc `word/document.xml`, lấy cả nội dung trong bảng và trong
`<w:ins>`/`<w:del>` (tệp có Track Changes mà chỉ đọc `paragraph.text` sẽ ra rỗng hoặc thiếu — lỗi này đã
có tiền lệ thật). Với `.xlsx` trích theo sheet. Tệp nào lỗi thì ghi vào `CAN-XAC-MINH.md` kèm lý do, **không
bỏ qua im lặng**.

**Bước 3 — bù metadata sidecar.** Hiện chỉ 4% tệp `.docx` có sidecar. Với mỗi tệp chưa có, tạo
`<tên cơ sở>.metadata.md` theo đúng schema 11 trường. Quy tắc: trường nào **đọc được từ chính nội dung văn
bản** thì điền; trường nào không thì ghi `Cần xác minh`. `Người kiểm tra` ghi `Chưa xác định`.
`Trạng thái phê duyệt` ghi `Bản nháp` — vì đây là bản máy sinh, chưa ai duyệt. **Không đánh dấu
`Chính thức`.**

**Bước 4 — quyết về 53 tệp PDF.** Mẫu 12 tệp đều không có lớp chữ. Trước khi bỏ công OCR, hỏi người phụ
trách: *53 tệp này có cần tra cứu theo nội dung không, hay chỉ cần lưu trữ?* Chỉ lưu trữ thì để nguyên,
ghi rõ trong `00-README.md` rằng khối này không nằm trong chỉ mục. Cần tra cứu thì OCR và đưa vào `text/`,
đánh dấu `"nguon_chu": "OCR"` trong `CHI-MUC.jsonl` để người đọc biết độ tin cậy thấp hơn.

**Bước 5 — cơ chế giữ chỉ mục không lệch.** Tệp mới vào `11-Input` mà không vào chỉ mục thì vài tháng nữa
chỉ mục sẽ lệch với kho — và **bản lệch nguy hiểm hơn bản thiếu**, vì nó trông như có. Đề xuất một trong
hai và ghi vào `00-README.md`:
- chạy lại phần tăng thêm theo định kỳ (so `sha256` để biết tệp nào mới/đổi), hoặc
- gắn vào đúng quy trình nạp hai tầng sẵn có.

### Điều kiện nghiệm thu

- [ ] `06-Chi-Muc/` tồn tại, 01–05 và `11-Input` **không có tệp nào bị sửa** — đối chiếu `sha256` trước/sau.
- [ ] `CHI-MUC.jsonl` có số dòng bằng số tệp `.docx` + `.xlsx` trong 01–05, trừ số tệp ghi ở `CAN-XAC-MINH.md`.
- [ ] Lấy **ngẫu nhiên 10 tệp**, mở bản gốc và so với chữ trong `text/` — phải khớp đoạn đầu và đoạn cuối.
- [ ] Báo được **hai con số thời gian** cho cùng một phép tìm: qua chỉ mục và quét trực tiếp.
- [ ] Sidecar mới đều có đủ 11 trường, không trường nào bị bỏ trống thay vì ghi `Cần xác minh`.
- [ ] `00-README.md` ghi rõ: ngày dựng, phạm vi, tệp nào bị loại và vì sao, cách dựng lại.

### Báo cáo lại

Gửi về bản tóm tắt gồm: số tệp đã trích, dung lượng `06-Chi-Muc/`, hai con số thời gian tìm kiếm, số tệp
trong `CAN-XAC-MINH.md` kèm lý do, và quyết định về khối PDF.

**Nếu bước 1 cho thấy chênh lệch tốc độ không đáng kể thì dừng lại và báo** — không làm tiếp chỉ vì đã
bắt đầu.

---

## Ghi chú cho người gửi (không nằm trong lệnh)

- Ước tính: `text/` cho toàn bộ 818 tệp `.docx` vào khoảng **7 MB**, tức **+2%** dung lượng kho. Rất rẻ so
  với việc rút thời gian tìm kiếm từ ~16 phút xuống dưới 1 giây.
- Lớp chữ thuần này **chạy được trên Chat và Cowork** — hai nền không chạy được `python-docx`, nên hiện gần
  như không đọc được kho.
- Nếu muốn nhẹ hơn nữa, có thể gom `text/` thành một tệp `SQLite` duy nhất: Drive chỉ phải tải một tệp thay
  vì hàng trăm. Đổi lại là khó soi bằng mắt. Nên làm sau khi bản `.txt` đã chạy ổn.
- Khối 53 PDF là câu hỏi đáng quyết sớm: 75 MB, chiếm **một phần tư dung lượng kho**, mà hiện không tra
  cứu được.
