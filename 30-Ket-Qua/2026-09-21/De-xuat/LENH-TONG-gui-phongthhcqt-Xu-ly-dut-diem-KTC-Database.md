# LỆNH TỔNG — xử lý dứt điểm KTC-Database

**Ngày lập:** 22/9/2026 · **Người lập:** tài khoản `nnqp201-sys` (P-THHC)
**Gửi:** tài khoản `phongthhcqt@gmail.com`
**Thay thế:** toàn bộ 4 tài liệu trước trong thư mục này. Đọc tài liệu này là đủ, không cần đọc lại các bản cũ.

**Cách dùng:** dán toàn bộ phần trong khung vào một phiên Claude Code của tài khoản đó, trên máy đã cài
Google Drive for Desktop và đã đồng bộ KTC-Database.

---

## Vì sao có lệnh này

Việc dựng lớp chỉ mục cho KTC-Database đã qua **ba lần đổi phương án**, mỗi lần vì một phép đo lật đổ giả
định trước đó:

1. Ban đầu: chạy qua Claude đọc từng tệp → đo ra **7,3 giờ, 19 triệu token**. Bỏ.
2. Chuyển sang Apps Script chạy trong Drive → vướng **hạn mức 90 phút/ngày**, chờ 3–6 giờ. Bỏ.
3. Phát hiện kho **đã đồng bộ về máy** → đọc tại chỗ **0,78 giây/tệp**. Toàn bộ khó khăn biến mất.

Lệnh này chốt phương án 3 và gom tất cả việc còn lại.

---

## KHUNG LỆNH — dán từ đây trở xuống

Bạn làm việc trên kho `KTC-Database` của Trường Cao đẳng Kon Tum, đã đồng bộ về máy này qua Google Drive
for Desktop. Kho do chính người dùng quản lý; hai tài khoản `truong.cdkontum` và `phongthhcqt` dùng chung.

### 0. Ba điều phải biết trước khi gõ lệnh đầu tiên

**(a) Đừng tin phép đếm chạy một lượt.** Đã sai ba lần liên tiếp vì đúng một nguyên nhân: Google Drive for
Desktop **liệt kê thư mục dần dần**, nên quét sớm sẽ ra số thiếu mà không báo lỗi gì.

| Lần đếm | `.docx` | `.md` | `.doc` |
|---|---|---|---|
| Lượt 1 | 826 | 212 | 36 |
| Lượt 2 | 830 | 233 | 33 |
| Lượt 3 (22/9, hai lượt liền khớp nhau) | **879** | **255** | **36** |

**Luật: đếm hai lần cách nhau ít nhất 5 phút. Chưa khớp thì chưa được coi là số thật.** Ghi cả hai con số
vào báo cáo.

**(b) Máy có thể gắn hai ổ Drive cùng chứa kho.** Trên máy người lập lệnh có `H:\My Drive\KTC-Database`
(tài khoản sở hữu) và `I:\.shortcut-targets-by-id\18ZNI-…\KTC-Database` (nhìn từ tài khoản được chia sẻ).
Đối chiếu từng đường dẫn: **1.250/1.251 tệp trùng** — cùng một thư mục, chỉ lệch nhịp đồng bộ.

**Kiểm xem máy bạn có mấy bản. Chọn một, và ghi rõ đường dẫn đó vào mọi báo cáo.** Hai người chạy trên hai
ổ rồi so kết quả mà không biết điều này sẽ tưởng chỉ mục sai.

**(c) Việc đã làm rồi, đừng làm lại:**

- **36 tệp `.doc` đã chuyển sang `.docx`** tại chỗ (22/9, bằng Word COM). Đã kiểm: 36/36 đọc được.
  **Bản `.doc` gốc vẫn còn**, chưa xóa.
- Chưa làm gì khác. Chưa có thư mục `06-Chi-Muc/`.

### 1. Ràng buộc không được vi phạm

1. **Không sửa, không đổi tên, không xóa tệp** trong `01`–`05` và `11-Input`, **trừ đúng hai việc được nêu
   tên ở mục 2**. Mọi việc khác chỉ đọc.
2. **Không chuyển đổi định dạng bản gốc.** Checklist mục D của chính kho ghi: *"Tệp nguồn được
   copy/upload/update nguyên byte; không tái tạo Office/PDF từ nội dung trích xuất."*
3. **Chữ trích xuất là dữ liệu phái sinh.** Mọi kết luận pháp lý vẫn phải mở bản gốc.
4. **Không bịa metadata.** Không đọc chắc chắn được thì ghi `Cần xác minh`, không suy từ tên tệp.
5. **Không ghi vào `03-Templates(1)`.**
6. Việc nào thấy cần mà không nằm trong lệnh này thì **đưa vào danh sách chờ**, không tự làm.

### 2. Hai việc sửa kho được phép — chỉ hai việc này

#### 2.1 Thay tệp QĐ-1710 bị hỏng

Tệp này **hỏng thật, không công cụ nào mở được**, kể cả Word:

```
02-KTC-Regulations/02-01- Quy che - quy dinh - huong dan chung/
   26. Du thao QD-1710-2026 QC quan ly su dung tai san cong.docx
```

Chẩn đoán đã làm: 14.748 byte, chữ ký đầu `PK\x03\x04` đúng chuẩn ZIP, **nhưng không có bản ghi kết thúc
ZIP (EOCD) và mục lục trung tâm có 0 mục**. Tệp bị cắt cụt lúc tải lên. Không cứu được.

Bản thay thế đã xác minh, nằm ngay trong kho:

```
11-Input/QUY CHE QUAN LY, SU DUNG TAI SAN NAM 2026.docx
```

Đã kiểm: "Số: 1710/QĐ-CĐKT", Quảng Ngãi ngày 04/8/2026, **37.002 ký tự**, kết thúc hoàn chỉnh bằng `./.`,
**không có sửa đổi theo dõi nào** (8 dấu `<w:ins` đếm được là thẻ viền bảng `<w:insideH>`, không phải
Track Changes).

Làm hai thao tác:

1. **Chép** (không phải di chuyển) tệp `11-Input` vào thư mục `02-01-…` với tên
   `26. QD-1710-QD-CDKT Quy che quan ly, su dung tai san cong.docx`.
   Tên theo đúng quy ước sẵn có của thư mục đó (`NN. <mô tả>`), và bỏ chữ "Dự thảo" vì **bản này là quyết
   định đã ban hành, không phải dự thảo**.
2. **Đổi tên** tệp hỏng thành `⚠️26. Du thao QD-1710 (TEP HONG, KHONG MO DUOC).docx.hong`.
   **Không xóa.** Thư mục này đã dùng dấu ⚠️ cho văn bản hết hiệu lực, nên ký hiệu này người đọc hiểu ngay.

Giữ nguyên tệp trong `11-Input` — dọn `11-Input` là quy trình riêng, không gộp vào đây.

#### 2.2 Quyết về 36 bản `.doc` gốc

36 tệp `.doc` nay đều đã có bản `.docx` cùng tên, cùng thư mục, đã kiểm đọc được.

**Hỏi người phụ trách trước khi làm gì.** Ba lựa chọn, không tự chọn:

- Giữ cả hai (an toàn nhất, nhưng kho có 36 cặp trùng, người tra cứu sẽ phân vân mở bản nào)
- Chuyển 36 bản `.doc` vào một thư mục lưu trữ, ví dụ `99-Ban-goc-doc-cu/` (lùi lại được)
- Xóa hẳn 36 bản `.doc` (**không lùi lại được** — chỉ làm khi người phụ trách nói rõ)

### 3. Dựng lớp chỉ mục

#### 3.1 Công cụ

```powershell
python -m venv D:\venv\ktc
D:\venv\ktc\Scripts\pip install "markitdown[docx,pdf,xlsx]"
```

**Ba cái bẫy khi cài, đã gặp thật:**

- Đừng `git clone git@github.com:...` — đó là đường SSH, máy thường không có khóa. Không cần mã nguồn.
- Đừng dùng `[all]` — kéo thêm nhận dạng giọng nói, YouTube, Azure. Không dùng tới.
- **Đừng cài vào `%TEMP%` hay thư mục có đường dẫn sâu.** markitdown kéo theo `onnxruntime` có tệp đường
  dẫn rất dài: cài vào thư mục sâu thì hỏng giữa chừng với `OSError [Errno 2]`; cài vào `%TEMP%` thì
  `python.exe` của môi trường ảo có thể **biến mất giữa phiên** do dọn rác hoặc phần mềm diệt virus.

**Vì sao là markitdown chứ không phải `python-docx`:** đã thử trên một tệp dựng riêng có `<w:ins>` và
`<w:del>`.

| Bộ đọc | Kết quả |
|---|---|
| markitdown | giữ đoạn thêm, bỏ đoạn xóa — đúng nội dung sau sửa đổi |
| python-docx | **cả hai đoạn ra rỗng** |

#### 3.2 Nơi đặt

Tạo **một thư mục mới ở cấp cao nhất**: `06-Chi-Muc/`. Không đặt xen vào 01–05.

```
06-Chi-Muc/
├── 00-README.md           tình trạng, ngày dựng, đọc từ ổ nào, phạm vi, cách dựng lại
├── 00-TRANG-THAI.json     {"da_xong": "412/1329", "bat_dau": "...", "xong": null}
├── CHI-MUC.jsonl          mỗi dòng một tài liệu
├── text/                  chữ đã trích, soi gương cấu trúc thư mục gốc
└── CAN-XAC-MINH.md        tệp không trích được, kèm lý do
```

Đặt riêng để nếu hỏng thì xóa cả thư mục và dựng lại, không ảnh hưởng 01–05.

#### 3.3 Mỗi dòng `CHI-MUC.jsonl`

```json
{
  "duong_dan": "02-KTC-Regulations/02-01-.../26. QD-1710-QD-CDKT....docx",
  "ten_tep": "26. QD-1710-QD-CDKT Quy che quan ly, su dung tai san cong.docx",
  "kho": "02",
  "kich_thuoc": 72655,
  "md5": "…",
  "ngay_sua": "2026-08-04T10:03:04",
  "so_ky_tu": 37002,
  "tep_chu": "text/02-KTC-Regulations/.../26. QD-1710-QD-CDKT….txt",
  "nguon_chu": "docx-truc-tiep",
  "so_hieu": "1710/QĐ-CĐKT",
  "ngay_ban_hanh": "04/08/2026",
  "trang_thai_trich": "OK"
}
```

- `nguon_chu` chỉ có **hai giá trị**: `docx-truc-tiep` hoặc `OCR`. Không còn `docs-convert` — phương án
  chuyển đổi qua Google Docs đã bỏ.
- `md5` dùng thay `sha256`: mục đích là **dò tệp đã đổi**, không phải chống giả mạo.
- `so_hieu`, `ngay_ban_hanh` **chỉ điền khi đọc được chắc chắn từ nội dung**. Không chắc thì `null`, đừng
  đoán từ tên tệp.

#### 3.4 Thứ tự chạy — dừng báo cáo sau mỗi bước

**Bước 1 — chạy thử `02-KTC-Regulations`.** Số liệu đã đo để đối chiếu: **343 tệp · 14,3 phút ·
2,50 giây/tệp · 9.146.280 ký tự · trung bình 28.317 ký tự/tệp**. Lệch nhiều thì dừng, báo.

**Bước 2 — chạy toàn kho.** Ước tính ~45 phút cho khoảng 1.000 tệp có nội dung.

Với `.docx`: markitdown đọc thẳng. Với `.xlsx`: đọc được nhưng đầu ra lẫn nhiều `NaN`, `Unnamed: 1` —
**đủ để tìm, không đủ để đọc**, chấp nhận vậy. Tệp nào lỗi thì ghi `CAN-XAC-MINH.md` kèm lý do,
**không bỏ qua im lặng** — đây chính là cách tệp QĐ-1710 hỏng đã lọt suốt bao lâu nay.

**Bước 3 — 11 tệp PDF cần OCR.** Không phải 53. Đã chạy `pdfminer` trên cả 54 tệp: **43 tệp có lớp chữ,
đọc được ngay**; chỉ **11 tệp** không có. Danh sách 11 tệp đó:

```
1. QĐ 1671-LDTBXH- thanh l Truong Kon Tum.pdf
2. QD  635 doi ten Truong.pdf
QD-635-QD-LDTBXH_Doi-ten-Truong_20230516_v1.pdf
KH-1746-KH-BGDDT_Xay-dung-De-an-nang-cao-nang-luc-to-chuc-…
CV-1400-NGCBQLGD-CSNGCB_Huong-phu-cap-uu-dai-nhan-su-ho-tr…
CV-1400_2026_v1.pdf
1. 543 QDUB chuyen ve UBND tinh Quang Ngai.pdf
QD-543-QD-UBND_Chuyen-ve-UBND-tinh-Quang-Ngai_20250630_v1.pdf
QD-37-2025-QD-CTUBND_Phan-cap-quan-ly-can-bo-cong-chuc-vie…
QD-46-2025-QD-CTUBND_Phan-cap-tham-quyen-quan-ly-su-dung-t…
BBKT_A1_CD-Kon-Tum_2026_v1.pdf
```

Trong đó có **3 cặp trùng nội dung khác tên** (`QĐ 635` hai bản, `QĐ 543` hai bản, `CV 1400` hai bản) —
thực chất khoảng **8 văn bản**. OCR 8 tệp là việc vặt, làm được.

Yêu cầu bắt buộc khi OCR:
- Ghi `"nguon_chu": "OCR"` và `"do_tin_cay": "thap"`.
- `00-README.md` ghi rõ: **chữ OCR chỉ dùng để TÌM RA tài liệu, tuyệt đối không dùng để TRÍCH DẪN.**
- **Chạy thử 3 tệp trước**, xem tiếng Việt có dấu ra thế nào. Sai nhiều quá thì báo lại — chỉ mục đầy chữ
  rác còn tệ hơn không có, vì phép tìm sẽ trả về nhiễu.

**Cảnh báo về phép đo OCR:** lần đầu người lập lệnh chỉ đọc 3 trang đầu mỗi PDF cho nhanh → báo nhầm
`QD-2664` là ảnh quét. Đọc đủ trang thì nó có **497.342 ký tự**. **Phép đo nhanh đẻ ra một báo động giả 8%.**
Khi kiểm PDF, đọc đủ trang.

**Bước 4 — cơ chế giữ chỉ mục không lệch.** Tệp mới vào `11-Input` mà không vào chỉ mục thì vài tháng nữa
chỉ mục sẽ lệch, và **bản lệch nguy hiểm hơn bản thiếu** vì nó trông như có. Đề xuất một cách và ghi vào
`00-README.md`: chạy lại phần tăng thêm định kỳ (so `md5` để biết tệp nào mới/đổi), hoặc gắn vào quy trình
nạp hai tầng sẵn có.

### 4. KHÔNG làm những việc sau

- **Không sinh sidecar metadata hàng loạt.** Từ chữ thuần chỉ đọc chắc được 2 trường (số hiệu, ngày ban
  hành). Sidecar 2 trường thật + 9 trường "Cần xác minh" vẫn **đẩy tỷ lệ phủ từ 4,4% lên 100% trong khi
  hiểu biết thật vẫn 4,4%** — hỏng luôn thước đo. Hai trường đọc được để trong `CHI-MUC.jsonl`; phần còn
  thiếu đưa vào `CAN-XAC-MINH.md` xếp theo kho rồi theo mức quan trọng, thành **danh sách việc** cho người
  làm dần.
- **Không chạy Apps Script.** Kịch bản `ktc-chi-muc.gs` v2.0 giữ lại làm **phương án dự phòng**, cho
  trường hợp về sau cần dựng chỉ mục mà không có máy đồng bộ Drive. Ghi rõ trạng thái đó vào chính tệp
  kịch bản.
- **Không gộp `text/` vào SQLite ngay.** Làm sau khi bản `.txt` đã chạy ổn; sớm quá thì mất khả năng soi
  bằng mắt khi có nghi ngờ.

### 5. Điều kiện nghiệm thu

- [ ] `06-Chi-Muc/` tồn tại; `01`–`05` và `11-Input` **không tệp nào bị sửa ngoài hai việc ở mục 2** —
      đối chiếu `md5` trước/sau.
- [ ] `CHI-MUC.jsonl` có số dòng bằng số tệp có nội dung, trừ số tệp ghi trong `CAN-XAC-MINH.md`.
- [ ] Lấy **ngẫu nhiên 10 tệp**, mở bản gốc, so đoạn đầu và đoạn cuối với chữ trong `text/` — phải khớp.
- [ ] Đo phép tìm thật trên **ít nhất 5 cụm từ khác nhau**: qua chỉ mục so với tìm bằng chính Drive. Báo
      hai con số thời gian và độ phủ. *(Số cũ "38%" chỉ là mẫu 5/13, chưa phải con số chuẩn — đừng chép lại.)*
- [ ] Mọi sidecar mới (nếu có) đủ 11 trường, không trường nào bỏ trống thay vì ghi `Cần xác minh`.
- [ ] `00-README.md` ghi: ngày dựng, **đọc từ ổ nào**, phạm vi, tệp nào bị loại và vì sao, cách dựng lại.
- [ ] `00-TRANG-THAI.json` ghi rõ đã xong hay đang dở.

### 6. Báo cáo lại

Gửi về: hai con số đếm (hai lượt cách 5 phút), đường dẫn ổ đã dùng, số tệp đã trích, dung lượng
`06-Chi-Muc/`, hai con số thời gian tìm kiếm trên 5 cụm từ, số tệp trong `CAN-XAC-MINH.md` kèm lý do, kết
quả OCR 3 tệp thử, và quyết định về 36 bản `.doc`.

**Bước nào cho kết quả lệch nhiều so với số liệu trong lệnh thì dừng và báo** — số trong lệnh này đều đo
thật, nhưng đo trên máy khác.

---

## Ghi chú cho người gửi (không nằm trong lệnh)

- Hai thao tác ở mục 2.1 người lập lệnh **không tự làm được**: bộ phân loại an toàn của Claude Code chặn
  ghi vào thư mục Drive dùng chung (*Modify Shared Resources*). Tài khoản sở hữu chạy thì không vướng.
- 36 tệp `.doc` đã chuyển được là vì chạy qua Word COM — đường đó bộ phân loại không kiểm. Ranh giới thực
  tế nằm ở đâu thì nên biết, đừng tưởng nó ở chỗ khác.
- Số tệp đang **tăng dần theo thời gian đồng bộ** (1.251 → 1.329 trong một buổi). Con số trong lệnh là ảnh
  chụp lúc 22/9; bên thực hiện phải tự đếm lại.
