# Trả lời kịch bản v2.0 — duyệt chạy thử, chốt Việc 3, giảm thời gian chờ

**Ngày:** 21/9/2026 · **Gửi:** tài khoản `phongthhcqt@gmail.com`
**Tiếp theo:** `Tra-loi-Buoc-1-va-Quyet-ba-viec-KTC-Database.md`

---

## Nhận lỗi trước

Ba yêu cầu về chạy ngắt quãng **đã có sẵn trong v1.0**. Em đặt chúng thành "điều kiện bắt buộc chưa ai
nêu" là sai — em đọc báo cáo tóm tắt rồi kết luận về mã nguồn mà không đọc mã. Bên thực hiện nói thẳng ra
là đúng, và việc đó nên được ghi nhận chứ không nên bỏ qua.

Phần duy nhất thật sự thiếu là tệp trạng thái, nay đã có.

---

## KHUNG TRẢ LỜI — dán từ đây trở xuống

Đã đọc v2.0. **Duyệt chạy `chayThu()`.** Bốn việc kèm theo.

### 1. Việc 3 — giữ nguyên phương án của v2.0: KHÔNG ghi sidecar nào

Lập luận "2 trường thật + 9 trường *Cần xác minh* vẫn đẩy phủ lên 100%" là đúng, và đúng hơn phương án
trước. Cái bẫy không nằm ở chỗ sidecar rỗng hay đầy, mà ở chỗ **tồn tại một tệp sidecar** là đã đủ để mọi
phép đếm coi tệp đó "đã có metadata".

**Không bật dòng cấu hình ghi sidecar.** Hai trường đọc được để trong `CHI-MUC.jsonl` là đúng chỗ — ở đó
chúng là dữ liệu chỉ mục, không phải tuyên bố đã lập hồ sơ. Tỷ lệ phủ tiếp tục báo 4,4%.

Khi nào người thật ngồi xác minh và điền thì sidecar mới sinh ra — và lúc đó con số phủ tăng lên mới có
nghĩa.

### 2. Cảm ơn vì tách hai con số thời gian

"30–60 phút" gộp thời gian máy chạy với thời gian chờ là chỗ dễ gây quyết định sai. Từ nay mọi ước tính
tách đôi như v2.0 đã làm.

**Thời gian chờ ~3–6 giờ có thể rút ngắn mà không tốn thêm hạn mức.** Hiện trigger 10 phút/lần nhưng mỗi
lần chỉ làm 4,5 phút — hơn nửa thời gian là nằm chờ. Đổi trigger xuống **5 phút/lần**, giảm mức tự thoát
xuống **4 phút**, và bọc thân hàm bằng `LockService` để hai lần chạy không chồng lên nhau. Tổng thời gian
máy chạy **không đổi**, nên hạn mức không đổi; chỉ thời gian chờ giảm còn khoảng một nửa.

Nếu `LockService` làm mã phức tạp thêm đáng kể thì bỏ qua đề xuất này — chờ lâu không nguy hiểm, chạy
chồng mới nguy hiểm.

### 3. Hạn mức 90 phút/ngày — tách PDF sang lượt riêng

Ước tính 50–80 phút nằm sát mép 90 phút là rủi ro thật. Giảm rủi ro bằng cách **chia làm hai lượt riêng
biệt**, không chạy lẫn:

- **Lượt 1: nhóm `.docx` và `.xlsx`.** Đây là phần mang gần hết giá trị.
- **Lượt 2 (ngày sau): 53 tệp PDF cần OCR.** Chuyển đổi OCR là phần nặng và khó đoán nhất — riêng tệp
  12,2 MB đã có thể ngốn nhiều phút.

Lý do không chỉ là hạn mức: **nếu hết hạn mức giữa chừng, thứ dở dang là nhóm nào cũng phải rõ.** Chạy
lẫn thì tệp trạng thái chỉ nói "412/1198", không nói nhóm nào đã xong.

Thứ tự "chạy `02-KTC-Regulations` trước" giữ nguyên — đúng như nhận định, 361 tệp là để đo tốc độ thật
trước khi cam kết cả kho.

### 4. Ngưỡng 200 ký tự — thêm một điều kiện

Cách đọc thẳng `.docx` trước, giữ `<w:ins>` bỏ `<w:del>`, rồi mới rơi xuống chuyển đổi là **đúng**: nhãn
`docx-truc-tiep` trung thực với bản đang lưu, và đó là thứ người tra cứu cần.

Một chỗ ngưỡng 200 có thể bắt nhầm: văn bản **ngắn thật** (giấy mời, phiếu chuyển, thông báo một đoạn) sẽ
bị coi là đọc hỏng và đem đi chuyển đổi vô ích — tốn hạn mức, lại bị dán nhãn `docs-convert` sai.

Thêm điều kiện: chỉ rơi xuống chuyển đổi khi **dưới 200 ký tự VÀ tệp lớn hơn ~30 KB**. Tệp `.docx` thật sự
ngắn thì kích thước cũng nhỏ; tệp nhỏ chữ mà nặng mới là dấu hiệu chữ bị giấu trong Track Changes — đúng
kiểu QĐ-1710.

### Chạy thử — xin đọc kỹ bốn kết quả

Việc in cả 600 ký tự cuối là ý hay; đó đúng là câu hỏi mà bảng số liệu không trả lời được. Khi đọc kết
quả, bốn điều cần kết luận rõ ràng, không để mơ hồ:

1. **QĐ-1710** — có ra chữ không, và ra bằng `docx-truc-tiep` hay phải `docs-convert`? Nếu đọc thẳng
   được thì ngưỡng 200 đang hoạt động đúng.
2. **PDF 12,2 MB** — 600 ký tự cuối có phải là **cuối văn bản thật**, hay cụt giữa chừng? Cụt thì phải
   biết cụt ở đâu và ghi vào `CAN-XAC-MINH.md`, không được để nó nằm trong chỉ mục như tệp đã trích đủ.
3. **Chữ tiếng Việt có dấu trong cả 3 PDF** — sai lác đác thì chấp nhận được; sai tới mức không tìm ra
   được bằng từ khóa thông thường thì báo lại, đừng chạy tiếp.
4. **Thời gian thật mỗi tệp**, tách riêng `.docx` và PDF. Đây là con số để tính lại hạn mức cho đúng.

**Chưa chạy `khoiDong()` cho tới khi bốn điều trên được trả lời.**

---

## Ghi chú cho người gửi (không nằm trong lệnh)

- Thao tác thuộc về người vận hành: dán kịch bản vào `script.google.com`, bật **Drive API v3** trong
  Services, chạy **`chayThu`** — không phải `khoiDong`.
- `chayThu` có ghi ra Drive (tạo `06-Chi-Muc/` và tệp kết quả). Đây là thư mục mới, tách khỏi 01–05, đúng
  thiết kế — nhưng cần biết trước để không bất ngờ.
- Nếu về sau chuyển kho sang tài khoản Workspace của Trường thì hạn mức script rộng hơn nhiều và cả bài
  toán 90 phút/ngày biến mất. Đáng cân nhắc riêng.
