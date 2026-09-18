# 90-Nhat-Ky-Van-Hanh — Bộ nhớ quá trình cấp dự án

Lớp này lưu **quá trình**: đã làm gì, vì sao quyết định như vậy, gặp vấn đề gì, rút ra bài học nào. Khác với
`20-Chuan-Chung/` (lưu *cách làm* — quy tắc tĩnh) và `21-Master-Task-Register/` (lưu *dữ liệu*).

Mục tiêu theo mục IX Kế hoạch hợp nhất: hệ thống **nhớ được quá trình**, không chỉ nhớ kết quả.

## Không thiết kế mới — kế thừa lớp Memory đã chín của KTC-RIS

Gói `25-KTC-Bao-Cao/ktc-bao-cao-v2_5_1-memory.skill` đã hiện thực hóa đúng thứ này ở cấp một hệ, gồm 6 tệp và
3 nguyên tắc ghi. Lớp cấp dự án kế thừa nguyên mô hình đó:

| Tệp | Đọc khi nào | Vì sao |
|---|---|---|
| `TRANG-THAI.md` | **Mở đầu mọi phiên làm việc** | Biết đang ở kỳ nào, bước nào, còn treo việc gì — không đọc dễ làm lại việc đã xong hoặc bỏ sót việc dở |
| `01-Nhat-Ky-Chay.md` | **Kết thúc mỗi kỳ** (bắt buộc ghi) | Trả lời câu hỏi hay gặp nhất đầu mỗi kỳ: "kỳ trước mình làm thế nào?" |
| `02-So-Dang-Ky-Loi.md` | Khi script báo lỗi hoặc ra kết quả lạ | Tra lỗi đã biết chưa, vá ở bản nào, còn lỗi nào đang mở |
| `03-Chat-Luong-Du-Lieu-Don-Vi.md` | Trước khi thu thập, kiểm tra đơn vị | Biết trước đơn vị nào hay nộp sai kiểu gì → nhắc trúng chỗ |
| `04-Nhat-Ky-Quyet-Dinh.md` | Khi định thay đổi thiết kế/quy trình | Biết vì sao chỗ đó đang được làm như hiện tại — tránh phá bỏ quyết định có lý do |
| `05-Bai-Hoc.md` | Khi thấy mình sắp mắc lỗi cũ | Các lỗi đã trả giá |

Mục mới thêm lên **đầu tệp**, không thêm xuống cuối.

## Ba nguyên tắc ghi

1. **Ghi sự việc, không ghi cảm nhận.** "Khoa KT-CN nộp phụ lục IIb thiếu cột 11–16" chứ không phải
   "Khoa KT-CN làm ẩu".
2. **Phân biệt rõ ĐÃ XÁC MINH và CHƯA XÁC MINH.** Ghi nhầm phỏng đoán thành sự thật còn hại hơn không ghi
   gì, vì kỳ sau sẽ tin theo. Dùng nhãn `[CHƯA XÁC MINH]`.
3. **Ghi cả lý do, không chỉ kết luận.** Quyết định không kèm lý do sẽ bị người sau phá bỏ vì tưởng là tùy tiện.

## Ba cơ chế nhật ký đang rời rạc — chưa gộp

| Nơi | Dạng | Phạm vi |
|---|---|---|
| `25-KTC-Bao-Cao/memory/` | 6 tệp `.md` | Riêng hệ báo cáo — mô hình chín nhất |
| `23-KTC-Ke-Hoach/00-Nhat-Ky-Van-Hanh.xlsx` | Excel | Riêng hệ kế hoạch |
| `24-KTC-Theo-doi-CV/02. Nhật ký liên thông KTC-Theo-dõi-CV.xlsx` | Excel | Riêng hệ theo dõi |

**Chưa gộp trong đợt này** — gộp là việc đụng dữ liệu vận hành thật, cần đối chiếu nội dung từng nơi trước.
Ba việc theo thứ tự: (1) đọc và đối chiếu nội dung ba nguồn; (2) chọn dạng đích — `.md` cho tường thuật,
Excel cho bảng phiên xử lý 16 trường ở mục IX Kế hoạch hợp nhất; (3) chuyển và để lại tệp trỏ đường ở vị
trí cũ.
