# Bộ nhớ quá trình KTC-RIS — Chỉ mục

Lớp này lưu **quá trình**: đã làm gì, vì sao quyết định như vậy, gặp vấn đề gì,
rút ra bài học nào. Khác với `Skill-Library/` (lưu *cách làm* — quy tắc tĩnh)
và Drive (lưu *dữ liệu* — đầu vào/đầu ra).

Không đọc hết cả thư mục. Đọc đúng file cần theo bảng dưới.

| Khi nào | Đọc file | Vì sao |
|---|---|---|
| **Mở đầu MỌI phiên làm việc** | `TRANG-THAI.md` | Biết đang ở kỳ nào, bước nào, còn treo việc gì. Không đọc file này dễ làm lại việc đã xong hoặc bỏ sót việc dở dang |
| Trước Bước 1-2 (thu thập, kiểm tra đơn vị) | `03-Chat-Luong-Du-Lieu-Don-Vi.md` | Biết trước đơn vị nào hay nộp sai kiểu gì → nhắc trúng chỗ thay vì phát hiện lại từ đầu mỗi tháng |
| Khi script báo lỗi hoặc chạy ra kết quả lạ | `02-So-Dang-Ky-Loi.md` | Tra xem lỗi đã biết chưa, đã vá ở bản nào, còn lỗi nào đang mở |
| Khi định thay đổi thiết kế/quy trình | `04-Nhat-Ky-Quyet-Dinh.md` | Biết vì sao chỗ đó được làm như hiện tại — tránh phá bỏ quyết định có lý do |
| Khi thấy mình sắp mắc lỗi cũ | `05-Bai-Hoc.md` | Các lỗi đã trả giá, không nên lặp lại |
| **Kết thúc mỗi kỳ báo cáo** | `01-Nhat-Ky-Chay.md` | Ghi lại kỳ vừa chạy — đây là việc BẮT BUỘC, xem mẫu ở `assets/mau-nhat-ky-chay.md` |

## Nguyên tắc ghi bộ nhớ

1. **Ghi sự việc, không ghi cảm nhận.** "Khoa KT-CN nộp IIb thiếu cột 11-16" chứ không phải "Khoa KT-CN làm ẩu".
2. **Phân biệt rõ ĐÃ XÁC MINH và CHƯA XÁC MINH.** Ghi nhầm phỏng đoán thành sự thật còn hại hơn không ghi gì, vì kỳ sau sẽ tin theo. Dùng nhãn `[CHƯA XÁC MINH]`.
3. **Ghi cả lý do, không chỉ kết luận.** Quyết định không kèm lý do sẽ bị người sau (hoặc chính AI phiên sau) phá bỏ vì tưởng là tùy tiện.
4. **Cập nhật ngay trong phiên, không để dồn.** Phiên kết thúc là mất ngữ cảnh.
5. **Không ghi dữ liệu nghiệp vụ vào đây.** Số liệu KPI, nội dung báo cáo thuộc về Drive. Lớp này chỉ ghi *quá trình*.

## Vì sao cần lớp này

Trước khi có nó, mỗi phiên làm việc bắt đầu từ số không: phải hỏi lại đang làm đến đâu,
phát hiện lại các lỗi đơn vị đã gặp tháng trước, và có nguy cơ đảo ngược những quyết định
đã cân nhắc kỹ. Bộ nhớ quá trình biến chuỗi phiên rời rạc thành một mạch công việc liên tục.
