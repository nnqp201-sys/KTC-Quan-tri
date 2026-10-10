# Cách từng hệ thống AI đọc tệp — gửi gì, kiểm thế nào, xử lý khi bị cắt

**Nguyên tắc chung:** Không tin lời “đã đọc hết” của bất kỳ hệ nào. Sau khi tải tệp, luôn gửi **Bước 0** trong tệp câu lệnh và đối
chiếu với `MA-KIEM-DOC-TEP.md`: Mỗi tệp văn bản kết thúc bằng một mã kiểm 6 ký tự; hệ trả đúng mã thì đã đọc tới cuối tệp.

Thông tin về giới hạn của từng hệ dưới đây là hiểu biết chung, **chưa kiểm trên tài khoản của Trường** và thay đổi theo gói dịch vụ;
kết quả Bước 0 mới là căn cứ.

| Hệ | Cách đọc tệp | Gửi | Khi Bước 0 sai mã |
|---|---|---|---|
| NotebookLM | Lập chỉ mục toàn văn từng nguồn, trả lời kèm trích dẫn; không chạy mã, không mở .zip | 36 tệp `Goi-A-Doc/` | Xóa nguồn lỗi, tải lại riêng tệp đó |
| ChatGPT Work | Giải nén và đọc bằng Python; **chỉ đọc phần nó chủ động mở** | 1 tệp `.zip` | Yêu cầu mở lại đúng tệp bằng Python |
| Copilot | Đọc tệp đính kèm theo ngữ cảnh; tệp dài dễ bị cắt phần cuối | 5 tệp `Goi-Gop-Copilot/` | Chuyển sang `Goi-Gop-nho/`, gửi nhiều lượt |
| Grok | Như Copilot | 5 tệp `Goi-Gop-Copilot/` | Chuyển sang `Goi-Gop-nho/` |
| Gemini | Như Copilot; ngữ cảnh lớn hơn | 5 tệp `Goi-Gop-Copilot/` | Chuyển sang `Goi-Gop-nho/` |

## 1. NotebookLM (Google)

- **Cách đọc:** Mỗi tệp tải lên là một “nguồn”. NotebookLM lập chỉ mục toàn bộ nội dung, khi trả lời chỉ lấy các đoạn liên quan và
  gắn số trích dẫn. Đây là hệ đọc **đủ nhất**, nhưng không tính được mã băm, không chạy được mã, không mở được tệp .zip.
- **Định dạng:** Nhận PDF, .md, .txt. Gửi nguyên 36 tệp trong `Goi-A-Doc/` (dưới giới hạn 50 nguồn mỗi sổ tay).
- **Cách gửi:** Tạo sổ tay mới → Thêm nguồn → chọn cả 36 tệp → chờ từng nguồn hiện dấu đã xử lý. Nguồn nào báo lỗi thì tải lại
  riêng nguồn đó.
- **Lưu ý:** Bảng trong PDF đọc được nhưng có thể mất cột; khi cần số liệu trong bảng, nhắc NotebookLM dẫn N15 (dạng văn bản) thay
  vì PDF. Tích chọn đủ mọi nguồn ở cột bên trái trước khi hỏi; nguồn bỏ tích sẽ không được dùng.

## 2. ChatGPT Work (OpenAI)

- **Cách đọc:** Tệp .zip được đưa vào môi trường chạy mã; ChatGPT phải **tự viết Python để giải nén và mở từng tệp**. Nó không tự
  “biết” nội dung; tệp nào nó không mở thì coi như chưa đọc. Vì vậy câu lệnh yêu cầu in dòng cuối của từng tệp.
- **Định dạng:** Gửi một tệp `Goi-day-du-tham-dinh-lan-6.zip`. Trong gói có 36 nguồn, tệp plugin .zip (lồng bên trong), tệp kết quả
  nghiệm thu .json.
- **Cách gửi:** Bấm dấu `+` → tải tệp .zip → chọn mô hình suy luận mạnh nhất → gửi Bước 0.
- **Lưu ý:** Phiên chạy mã có thể hết hạn sau một thời gian không dùng, tệp đã giải nén bị mất: Khi ChatGPT báo không tìm thấy
  tệp, tải lại tệp .zip trong cùng cuộc hội thoại và nói “giải nén lại rồi làm tiếp”. PDF đọc qua thư viện Python nên chậm; ưu tiên
  để nó đọc các tệp .md.

## 3. Copilot (Microsoft)

- **Cách đọc:** Tệp đính kèm được đưa vào ngữ cảnh của cuộc hội thoại. Tệp vượt giới hạn thường bị **cắt phần cuối mà không báo**;
  đây là lý do báo cáo Copilot các lần trước chung chung.
- **Định dạng:** PDF, .txt, .docx. Tệp .md có thể không nhận nên gói gộp dùng .txt. Không gửi .zip.
- **Cách gửi:**
  - Microsoft 365 Copilot (tài khoản Trường, thẻ Work): Gõ `/` rồi gõ tên tệp để chọn từ OneDrive
    (`1 Claude AI\Lan 6_ho-so-tham-dinh\Goi-Gop-Copilot\`).
  - copilot.microsoft.com: Bấm dấu `+` → tải tệp.
- **Khi sai mã:** Dùng `Goi-Gop-nho/` (mỗi tệp tối đa khoảng 120 nghìn ký tự). Gửi theo lượt: Lượt 1 gồm GOP-0 và Bước 0; mỗi lượt sau
  2 - 3 tệp kèm câu “Đây là phần tiếp theo của hồ sơ, đọc hết, trả mã kiểm từng tệp, chưa thẩm định”; gửi xong tất cả mới gửi Câu 1.

## 4. Grok (xAI)

- **Cách đọc, định dạng:** Như Copilot — tệp đính kèm vào ngữ cảnh; nhận PDF, .txt; không dựa vào .zip.
- **Cách gửi:** grok.com → biểu tượng đính kèm → chọn 5 tệp `Goi-Gop-Copilot/` → chọn chế độ suy luận sâu.
- **Khi sai mã:** Chuyển sang `Goi-Gop-nho/`, gửi theo lượt như Copilot.

## 5. Gemini (Google)

- **Cách đọc, định dạng:** Tệp đính kèm vào ngữ cảnh; nhận PDF, .txt; mỗi lượt thường tối đa khoảng 10 tệp. Ngữ cảnh lớn nên nhiều
  khả năng đọc đủ 5 tệp gộp trong một lượt.
- **Cách gửi:** gemini.google.com (tài khoản Google của Trường) → dấu `+` → Tải tệp lên → chọn 5 tệp `Goi-Gop-Copilot/` → chọn mô
  hình suy luận mạnh nhất.
- **Lưu ý riêng:** Lần 5 Gemini nêu tên tệp có thật nhưng nội dung nhận định không đúng. Sau Bước 0, nếu Gemini trả mã kiểm sai mà
  vẫn khẳng định đã đọc, dừng lại và chuyển sang `Goi-Gop-nho/`.

## Ghi lại để tiếp thu

Với mỗi hệ, lưu câu trả lời Bước 0 vào đầu tệp báo cáo (hoặc chụp màn hình). Khi tiếp thu, phát hiện của hệ nào về một tệp mà hệ đó
không trả được mã kiểm sẽ được xếp “không xác minh được”.
