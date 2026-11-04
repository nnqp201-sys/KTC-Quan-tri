# Cơ chế tự học suốt đời cho KTC-Ke-Hoach

## Nguồn học hợp lệ

1. Văn bản/kế hoạch chính thức đã ban hành của Trường.
2. Mẫu được người dùng xác nhận là chuẩn hoặc hay.
3. `KTC-Database/04-Good-Documents/` và kho mẫu chính thức.
4. Sản phẩm thực tế trong `KTC-Ke-Hoach/Xuat_Ke_Hoach/` đã được xác nhận, trình ký hoặc ban hành.
5. Phản hồi sửa trực tiếp của người có thẩm quyền.

## Bốn tình huống kích hoạt

- **Mẫu tốt mới:** phân tích cấu trúc, định dạng, logic và kỹ thuật mới.
- **Sản phẩm đã được duyệt:** so với chuẩn hiện tại để nhận ra quy tắc giúp sản phẩm được chấp nhận.
- **Phản hồi sửa:** xác định quy tắc nào sai/thiếu, nhưng không tổng quát hóa từ một sửa đổi tình huống.
- **Lỗi lặp lại:** nếu một dạng lỗi xuất hiện nhiều lần, đề xuất thêm vào bộ tự kiểm.

## Quy trình học có kiểm soát

1. Ghi nhận nguồn và trạng thái thẩm quyền.
2. Chạy phân tích định dạng bằng Python nếu là DOCX/XLSX.
3. Tách bốn lớp: nội dung; logic kế hoạch; định dạng; quy trình/phê duyệt.
4. So với chuẩn hiện có và phân loại:
   - đã có: bỏ qua hoặc thêm ví dụ;
   - biến thể hữu ích: hợp nhất có điều kiện;
   - mới hoàn toàn: lập đề xuất;
   - xung đột: giữ cả hai và xác định phạm vi/ưu tiên.
5. Trình đề xuất cho người dùng xác nhận trước khi cập nhật chuẩn ổn định.
6. Kiểm thử hồi quy trên tối thiểu mẫu năm, quý và tháng.
7. Ghi provenance vào `provenance-log.md`.

## Quy tắc không làm suy giảm

- Không tự xóa quy tắc đã xác lập.
- Không thay chuẩn chung bằng ngoại lệ của một văn bản.
- Không học lỗi chính tả, lỗi định dạng ngẫu nhiên hoặc dữ liệu tình huống.
- Khi xung đột, ưu tiên: nguồn ban hành chính thức > nguồn đã trình ký > mẫu tốt xác nhận > dự thảo; mới hơn > cũ hơn; đúng loại kế hoạch > loại gần giống.
- Học kỹ thuật và cấu trúc, không sao chép dữ liệu mẫu.

## Đầu ra bắt buộc của mỗi lần học

Tạo ít nhất một trong các mục sau:

- quy tắc định dạng mới;
- quy tắc logic/đối chiếu mới;
- mẫu lỗi mới cho bộ tự kiểm;
- biến thể theo loại kế hoạch;
- dòng provenance gồm nguồn, kỹ thuật, phạm vi, ngày, người xác nhận và trạng thái.

