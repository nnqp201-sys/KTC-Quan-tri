# Bộ nhớ quá trình — cách ghi và cách đọc

Lớp này lưu **quá trình**: đã làm gì, vì sao quyết định như vậy, gặp vấn đề gì, rút ra bài học nào. Khác với
quy tắc (lưu *cách làm*) và Master Task Register (lưu *dữ liệu*).

Mục tiêu: hệ thống **nhớ được quá trình**, không chỉ nhớ kết quả.

## Đọc gì, khi nào — không đọc hết cả thư mục

| Khi nào | Đọc | Vì sao |
|---|---|---|
| **Mở đầu mọi phiên làm việc** | `TRANG-THAI.md` | Biết đang ở kỳ nào, bước nào, còn treo việc gì. Không đọc dễ làm lại việc đã xong hoặc bỏ sót việc dở dang |
| Trước khi thu thập, kiểm tra đơn vị | `03-Chat-Luong-Du-Lieu-Don-Vi.md` | Biết trước đơn vị nào hay nộp sai kiểu gì → nhắc trúng chỗ thay vì phát hiện lại từ đầu mỗi kỳ |
| Khi script báo lỗi hoặc ra kết quả lạ | `02-So-Dang-Ky-Loi.md` | Tra lỗi đã biết chưa, vá ở bản nào, còn lỗi nào đang mở |
| Khi định thay đổi thiết kế/quy trình | `04-Nhat-Ky-Quyet-Dinh.md` | Biết vì sao chỗ đó đang làm như hiện tại — tránh phá bỏ quyết định có lý do |
| Khi thấy mình sắp mắc lỗi cũ | `05-Bai-Hoc.md` | Các lỗi đã trả giá |
| **Kết thúc mỗi kỳ** | `01-Nhat-Ky-Chay.md` — **bắt buộc ghi** | Trả lời câu hỏi hay gặp nhất đầu mỗi kỳ: "kỳ trước mình làm thế nào?" |

Mục mới thêm lên **đầu tệp**, không thêm xuống cuối.

## Ba nguyên tắc ghi

1. **Ghi sự việc, không ghi cảm nhận.**
   Đúng: "Khoa KT-CN nộp phụ lục IIb thiếu cột 11–16".
   Sai: "Khoa KT-CN làm ẩu".

2. **Phân biệt rõ ĐÃ XÁC MINH và CHƯA XÁC MINH.** Ghi nhầm phỏng đoán thành sự thật còn hại hơn không ghi
   gì, vì kỳ sau sẽ tin theo. Dùng nhãn `[CHƯA XÁC MINH]`.

3. **Ghi cả lý do, không chỉ kết luận.** Quyết định không kèm lý do sẽ bị người sau phá bỏ vì tưởng là tùy
   tiện.

## Ghi sau mỗi tác vụ lớn

Bắt buộc ghi một mục sau khi: chốt kỳ · dựng báo cáo · thay đổi thiết kế hoặc quy trình · phát hiện lỗi dữ
liệu của đơn vị · đưa ra một quyết định có thể bị chất vấn về sau.

Khung một mục nhật ký chạy:

```
## <ngày> — <tên kỳ hoặc loại việc>

**Loại:** ... · **Người thực hiện:** ... · **Sản phẩm:** ...

**Đã làm:**
1. ...

**Lệch chuẩn / bất thường:**
- ...

**Còn treo:** ...
```

Mục **"Lệch chuẩn / bất thường"** quan trọng hơn mục "Đã làm" — đó là chỗ chứa thông tin mà không ai khác
ghi lại.

## Bảng nhật ký vận hành 16 trường

Song song với nhật ký tường thuật, mỗi phiên xử lý ghi một dòng bảng: Session_ID · Thời gian · Hệ thống ·
Người yêu cầu · Input · Task_ID liên quan · AI/Agent · Thao tác · Nguồn · Kết quả · Người phê duyệt ·
Thay đổi · Lỗi · Cách xử lý · Link · Trạng thái.

## Khi không có bộ nhớ vận hành

Thiếu bộ nhớ vận hành **không phải lý do dừng**. Chạy tiếp và ghi cảnh báo vào phần đầu kết quả. Điều này
khác với thiếu kho dữ liệu nền — trường hợp đó phải dừng và hỏi.
