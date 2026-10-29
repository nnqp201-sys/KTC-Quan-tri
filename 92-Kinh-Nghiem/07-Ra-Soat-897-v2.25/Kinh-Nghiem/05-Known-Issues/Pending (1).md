# Việc đã biết, chưa xử lý

## KI-007 — Metadata số trang có chế độ suy giảm

**Trạng thái:** Chấp nhận có điều kiện · **Ưu tiên:** Thấp

Nếu môi trường không có LibreOffice/soffice và pdfinfo, script không thể dàn trang để đếm số trang thật;
`docProps/app.xml` giữ `Pages=1`. Nội dung và bố cục tài liệu không bị ảnh hưởng. Cần render Word/PDF ở
bước QA cuối khi số trang metadata là tiêu chí bắt buộc.

## KI-008 — Quan hệ NĐ 334/2026 với NĐ 60/2021 và NĐ 111/2025

**Trạng thái:** Chờ xác minh điều khoản chính thức · **Ưu tiên:** Cao khi hồ sơ liên quan

Ghi nhớ cũ có các phát biểu không nhất quán về việc “thay thế” hay “áp dụng song song”. Tệp ghi nhớ đó đã
được loại khỏi runtime. Khi hồ sơ liên quan, phải đọc toàn văn NĐ 334/2026/NĐ-CP và điều khoản chuyển tiếp,
bãi bỏ từ nguồn chính thức tại đúng thời điểm rà soát; không dùng tên tệp hoặc nhật ký cũ làm căn cứ.

## KI-009 — Phạm vi phát hiện tự động còn hẹp

**Trạng thái:** Mở · **Ưu tiên:** Trung bình

`_read_input_properties.py` v1.2 đã đọc mọi section, bảng, header và footer nhưng mới tự động nhận diện một
số thành phần định dạng theo tiền tố. Bộ hồi quy nội dung vẫn cần checklist và phân tích thủ công; không được
diễn giải kết quả script là đã rà soát toàn diện.
