# Trả lời Bước 1 — quyết ba việc và một điều kiện bắt buộc trước khi chạy

**Ngày:** 21/9/2026 · **Gửi:** tài khoản `phongthhcqt@gmail.com`
**Tiếp theo:** `Lenh-gui-phongthhcqt-Dung-lop-chi-muc-KTC-Database.md`
**Cách dùng:** dán phần trong khung vào chính phiên đã làm Bước 0–1.

---

## Ghi nhận trước

Báo cáo Bước 1 làm đúng điều khó nhất: **dừng vì giả định nền sai, không phải vì gặp khó.** Hai con số
1,2 giây/tệp và 8.648 ký tự/tệp trong lệnh là em đo trên ổ Drive đã đồng bộ về máy — không phải qua API.
Sai số 23 lần là lỗi của người ra lệnh, không phải của người thực hiện. Từ nay mọi con số trong lệnh phải
ghi rõ **đo ở đâu**.

Phát hiện `03-Templates(1)` là kho `.dotx` riêng chứ không phải bản sao cũng là thứ không ai biết trước.

Kết luận **"thiết kế đúng, kênh thực hiện sai"** là đúng. Đổi công cụ, không đổi mục tiêu.

---

## KHUNG TRẢ LỜI — dán từ đây trở xuống

Đã đọc báo cáo Bước 1. Quyết ba việc như sau, kèm **một điều kiện bắt buộc** phải xử lý trước khi chạy.

### Điều kiện bắt buộc — Apps Script không chạy được một mạch

Đây là điểm chưa thấy báo cáo nhắc tới, và nếu bỏ qua thì công việc sẽ hỏng giữa chừng.

**Apps Script có giới hạn cứng khoảng 6 phút cho MỖI LẦN chạy**, và có thêm hạn mức tổng thời gian chạy
mỗi ngày (tài khoản `@gmail.com` thấp hơn tài khoản Workspace). Ước tính 30–60 phút cho 1.198 tệp vì vậy
**không thể là một lần chạy**. Kịch bản viết theo kiểu một vòng lặp chạy hết sẽ bị cắt ngang ở khoảng tệp
thứ 150–300, và để lại đúng thứ nguy hiểm nhất: **một chỉ mục có vẻ hoàn chỉnh nhưng thiếu 3/4.**

Vì vậy, trước khi chạy thật, sửa `ktc-chi-muc.gs` cho đủ ba thứ:

1. **Ghi tiến độ ra ngoài.** Sau mỗi tệp, lưu lại vị trí đang làm (`PropertiesService` hoặc một tệp trạng
   thái trong `06-Chi-Muc/`). Lần chạy sau đọc lên và làm tiếp từ đó.
2. **Tự dừng trước hạn.** Ghi lại thời điểm bắt đầu; quá **4,5 phút** thì thoát sạch sẽ, không làm thêm
   tệp mới. Đừng chờ Google cắt.
3. **Hẹn giờ chạy lại.** Đặt trigger mỗi 10 phút cho tới khi hết danh sách, rồi tự gỡ trigger.

**Và `00-README.md` phải ghi rõ chỉ mục đã chạy xong hay đang dở.** Một tệp trạng thái ghi
`da_xong: 412/1198` là đủ. Không có nó thì không ai biết chỉ mục đang thiếu.

Trước khi tin kịch bản, **chạy thử trên tệp biết chắc là khó**: bản dự thảo QĐ-1710 (14,7 KB nhưng
`document.xml` giãn 382 KB vì Track Changes). Kịch bản báo trích được chữ từ tệp đó thì mới tin. Báo "sạch"
ngay lần đầu trên tệp dễ thì chưa chứng minh được gì.

### Việc 1 — Chạy Apps Script. Đồng ý.

Lý do quyết: 7,3 giờ và 19 triệu token là **vượt khả năng thực hiện**, không phải đắt. Apps Script đọc dữ
liệu ngay tại chỗ, không tệp nào đi qua mô hình — vừa nhanh hơn vừa kín hơn.

**Đồng ý dùng `md5Checksum` thay `sha256`.** Mục đích của trường này là **phát hiện tệp đã đổi**, không
phải chống giả mạo; md5 làm được việc đó, mà lại do Drive cấp sẵn, không phải tải 290 MB về băm. Hai điểm
kèm theo:

- Tệp **Google Docs/Sheets gốc** (không phải `.docx`) **không có** `md5Checksum`. Với nhóm này dùng
  `modifiedTime` + `version` thay thế, và ghi rõ trong `00-README.md` là nhóm đó dò đổi bằng cách khác.
- Điều kiện nghiệm thu "đối chiếu băm trước/sau để chứng minh không tệp gốc nào bị sửa" **giữ nguyên**,
  chỉ đổi thuật toán.

**Việc chuyển đổi qua Google Docs cần một ghi chú thật thà.** Chữ lấy được từ bản chuyển đổi là **nội dung
sau khi chấp nhận sửa đổi** — không phải nội dung bản gốc đang lưu. Với bản dự thảo thì đó là thứ cần;
nhưng người đọc chỉ mục phải biết mình đang đọc bản nào. Vậy:

- Mọi dòng có qua chuyển đổi phải ghi `"nguon_chu": "docs-convert"`.
- Tệp gốc đọc thẳng được thì ghi `"nguon_chu": "docx-truc-tiep"`.
- Bản chuyển đổi tạm phải **xóa sau khi lấy xong**, và đặt trong một thư mục tạm riêng — không nằm lẫn
  trong 01–05.

### Việc 2 — 53 tệp PDF: OCR, nhưng đánh dấu rõ độ tin cậy.

Quyết như vậy vì ba lẽ:

- Khối này là **75 MB, một phần tư dung lượng kho**, mà hiện **không phép tìm nào thấy**. Để nguyên là
  giữ một mảng mù lớn.
- Trong Apps Script, OCR không phải việc riêng: chuyển PDF sang Google Docs là **đã** chạy OCR. Chi phí
  thêm gần như bằng không so với việc đã làm.
- 53 tệp đủ ít để **kiểm bằng mắt**, khác hẳn 816 tệp `.docx`.

Ràng buộc đi kèm — đây là văn bản pháp lý, chữ OCR sai là loại sai nguy hiểm:

- Ghi `"nguon_chu": "OCR"` và `"do_tin_cay": "thap"` cho mọi dòng thuộc nhóm này.
- `00-README.md` ghi một câu, đủ mạnh để người đọc không bỏ qua: *chữ OCR chỉ dùng để **tìm ra** tài liệu,
  tuyệt đối không dùng để **trích dẫn**. Trích dẫn phải mở bản gốc.*
- **Chạy thử 3 tệp trước**, xem chữ tiếng Việt có dấu ra thế nào. Sai quá nhiều thì báo lại — chỉ mục đầy
  chữ rác còn tệ hơn không có, vì phép tìm sẽ trả về kết quả nhiễu.

### Việc 3 — Hoãn Bước 3. Đồng ý, và lý do còn mạnh hơn.

Sinh 780 sidecar toàn chữ "Cần xác minh" sẽ làm **tỷ lệ phủ metadata nhảy từ 4% lên 100% trong khi hiểu
biết thật vẫn là 4%**. Từ đó trở đi không ai đo được tiến độ nữa, vì thước đo đã hỏng. Đúng luật mà vô
dụng thì còn đỡ; đây là **đúng luật mà gây hiểu nhầm**.

Thay bằng cách này — vẫn có ích, lại không làm hỏng thước đo:

1. Kịch bản **chỉ ghi sidecar khi đọc được chắc chắn** từ nội dung văn bản (số hiệu, ngày ban hành, trích
   yếu — thường nằm ở phần đầu văn bản, nhận dạng được bằng mẫu).
2. Tệp nào không đủ dữ liệu thì **không tạo sidecar rỗng**, mà đưa tên vào `CAN-XAC-MINH.md`, **xếp theo
   kho và theo mức quan trọng** — thành danh sách việc cho người làm dần.
3. Sidecar máy sinh vẫn ghi `Trạng thái phê duyệt: Bản nháp`, `Người kiểm tra: Chưa xác định` như lệnh cũ.

Như vậy con số phủ metadata vẫn nói thật, và phần còn thiếu biến thành việc xếp sẵn thay vì tệp rỗng.

### Về con số 38%

`5/13` là mẫu nhỏ — đủ để thấy **hướng** (chỉ mục sẵn của Drive bỏ sót nhiều), chưa đủ để coi 38% là con
số chuẩn. Sau khi chỉ mục chạy xong, đo lại trên **ít nhất 5 cụm từ khác nhau** rồi mới ghi tỷ lệ vào
`00-README.md`. Trước đó thì ghi là "ước tính trên mẫu 13 tệp".

### Thứ tự làm

1. Sửa kịch bản cho chạy ngắt quãng được (điều kiện bắt buộc ở trên).
2. Chạy thử trên QĐ-1710 và 3 tệp PDF → **báo lại, chưa chạy tiếp.**
3. Đạt thì chạy `02-KTC-Regulations` trọn vẹn → báo số liệu.
4. Đạt thì chạy phần còn lại.

Vẫn giữ nguyên: **không sửa, không đổi tên, không xóa bất kỳ tệp nào trong 01–05 và `11-Input`.**

---

## Ghi chú cho người gửi (không nằm trong lệnh)

- Giới hạn 6 phút của Apps Script là chỗ hỏng khả năng cao nhất trong toàn bộ việc này. Hạn mức tổng mỗi
  ngày của tài khoản `@gmail.com` thấp hơn Workspace — nên **kiểm hạn mức thật của tài khoản đó** trước
  khi hứa 30–60 phút.
- Nếu về sau chuyển kho sang tài khoản Workspace của Trường thì hạn mức rộng hơn nhiều. Đáng cân nhắc
  riêng, không gộp vào việc này.
- Tệp `CHI-MUC_20260921_v0.1-metadata.jsonl` (1.185 dòng) đã dựng xong là tài sản thật — giữ lại làm mốc
  đối chiếu khi kịch bản chạy, để biết kịch bản có bỏ sót tệp nào không.
