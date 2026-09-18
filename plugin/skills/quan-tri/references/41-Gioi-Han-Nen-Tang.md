# Giới hạn theo nền tảng — Chat, Cowork, Claude Code

Cùng một yêu cầu cho kết quả **tin cậy khác nhau** tùy nền tảng đang chạy. Phải biết mình đang ở đâu và
trung thực ghi nhận giới hạn, thay vì kết luận sai.

| Nền tảng | Công cụ có | Làm được gì | Giới hạn phải ghi nhận |
|---|---|---|---|
| **Claude Chat** | Chỉ Skills | Đọc nội dung text được đính kèm, phân loại, đối chiếu quy tắc, dự thảo | **Không đọc được byte nhị phân** của `.docx`/`.xlsx`. Mọi kiểm tra định lượng (lề, cỡ chữ) phải ghi `FORMAT_BINARY_UNVERIFIED` |
| **Cowork** | Skills + Subagents + Connectors + công cụ tệp cục bộ (khi được cấp quyền) | Đọc tệp thật qua connector, chạy nhiều subagent song song | Phụ thuộc quyền connector được cấp trong phiên. Không có quyền thì lùi về mức như Chat |
| **Claude Code** | Skills + Subagents + Hooks + script | **Nền tảng duy nhất** chạy được script đọc thuộc tính thật (`python-docx`, `openpyxl`), có hook tự kiểm tra môi trường và chặn thao tác phá hoại | Không có giao diện đồ họa; thao tác trên tệp đã đồng bộ về máy |

## Quy tắc bắt buộc

1. **Không suy đoán số đo từ nội dung text.** Nếu không chạy được công cụ đọc thuộc tính thật, ghi
   `FORMAT_BINARY_UNVERIFIED` — không nói "lề 2cm" chỉ vì văn bản trông có vẻ vậy.
2. **Nói rõ nền tảng khi kết quả phụ thuộc nền tảng.** Ví dụ: "Trên Chat chưa xác minh được định dạng thật
   của tệp; cần chạy lại trên Claude Code để đo".
3. **Không tự nâng mức tin cậy.** Kết quả đọc gián tiếp không được trình bày ngang với kết quả đo trực tiếp.

## Ba tính chất của kho dữ liệu cần nhớ

- Kho `KTC-Database` **chỉ đọc**. Trên Claude Code có hook chặn ghi. Phát hiện gì cần sửa kho thì viết đề
  xuất ra thư mục output của dự án, không tự sửa.
- Công cụ kết nối Google Drive **chỉ đọc và tạo tệp mới** — không sửa, đổi tên, di chuyển, xóa tệp đã có.
  Cần dọn thì liệt kê để người dùng tự làm; **không báo "đã hoàn tất"** khi tệp gốc thực tế vẫn còn.
- Gói `.skill` là zip **tự chứa**. Các tệp quy tắc dùng chung buộc phải có bản sao bên trong gói; xóa bản
  sao để "khử trùng lặp" sẽ làm hỏng skill khi đóng gói lại.
