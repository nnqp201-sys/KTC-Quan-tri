# Giới hạn theo nền tảng — Chat, Cowork, Claude Code

Cùng một yêu cầu cho kết quả **tin cậy khác nhau** tùy nền tảng đang chạy. Phải biết mình đang ở đâu và
trung thực ghi nhận giới hạn, thay vì kết luận sai.

| Nền tảng | Công cụ có | Làm được gì | Giới hạn phải ghi nhận |
|---|---|---|---|
| **Claude (trò chuyện)** | Skills; môi trường thực thi mã khi tính năng được bật; connector người dùng cho phép. **Không có hook, agent** | Đọc tệp đính kèm, phân loại, đối chiếu quy tắc, dự thảo; chạy script đi kèm skill trong môi trường thực thi mã nếu có | Không truy cập ổ đĩa máy người dùng. Chưa kiểm chứng đầy đủ việc chạy `kiem_the_thuc.py`, Track Changes trong môi trường này — không chạy được thì ghi `FORMAT_BINARY_UNVERIFIED`; không có thao tác chặn ghi của plugin |
| **Cowork** | Skills + agent + hook + connector + tệp trong thư mục người dùng chọn | Đọc tệp thật, chạy agent kiểm tra, hook chặn ghi kho chuẩn (plugin 1.3.0) | Phụ thuộc quyền thư mục, connector được cấp; hook cần Python trên máy. Chưa có biên bản nghiệm thu |
| **Claude Code** | Skills + agent + hook + script cục bộ | Nền tảng **đã kiểm thử đầy đủ**: đo thuộc tính thật (`python-docx`, `openpyxl`), Track Changes, hook chặn ghi | Không có giao diện đồ họa; thao tác trên tệp đã đồng bộ về máy |

## Quy tắc bắt buộc

1. **Không suy đoán số đo từ nội dung text.** Nếu không chạy được công cụ đọc thuộc tính thật, ghi
   `FORMAT_BINARY_UNVERIFIED` — không nói "lề 2cm" chỉ vì văn bản trông có vẻ vậy.
2. **Nói rõ nền tảng khi kết quả phụ thuộc nền tảng.** Ví dụ: "Trên Chat chưa xác minh được định dạng thật
   của tệp; cần chạy lại trên Claude Code để đo".
3. **Không tự nâng mức tin cậy.** Kết quả đọc gián tiếp không được trình bày ngang với kết quả đo trực tiếp.

## Ba tính chất của kho dữ liệu cần nhớ

- Kho `KTC-Database` **chỉ đọc**. Trên Cowork và Claude Code, plugin từ bản 1.3.0 có hook chặn ghi
  (`ktc_guard.py`); trên Claude (trò chuyện) không có hook nên chỉ dựa vào quy tắc bất biến 5. Phát hiện gì cần sửa kho thì viết đề
  xuất ra thư mục output của dự án, không tự sửa.
- Công cụ kết nối Google Drive **chỉ đọc và tạo tệp mới** — không sửa, đổi tên, di chuyển, xóa tệp đã có.
  Cần dọn thì liệt kê để người dùng tự làm; **không báo "đã hoàn tất"** khi tệp gốc thực tế vẫn còn.
- Gói `.skill` là zip **tự chứa**. Các tệp quy tắc dùng chung buộc phải có bản sao bên trong gói; xóa bản
  sao để "khử trùng lặp" sẽ làm hỏng skill khi đóng gói lại.
