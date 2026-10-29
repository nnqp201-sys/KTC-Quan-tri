# PM-20260911-BC-9-thang-dau-nam-2026-v3-lan3

- **Tác vụ**: (a) Rà soát chính thức — cập nhật sau phản hồi trực tiếp của Phòng TH-HC&QT trên báo cáo rà soát lần 2.
- **Nội dung người dùng chỉnh / bác bỏ** (rất quan trọng — đọc trước khi rà soát báo cáo công tác tiếp theo):
  1. **K7C và K7T là 2 lớp/hệ đào tạo khác nhau** — không phải lỗi thiếu nhất quán mã lớp. Hệ đã RÚT LẠI phát hiện này. Bài học: mã lớp dạng "K<số><chữ>" không tự động suy luận "chữ cuối phải giống nhau nếu cùng khóa" — cần hỏi đơn vị nghiệp vụ khi nghi ngờ, không tự kết luận là lỗi.
  2. **Dòng "HIỆU TRƯỞNG" đã in đậm — hệ kiểm tra SAI.** Nguyên nhân gốc: phương pháp kiểm tra bold/italic/size qua python-docx (run.font.bold) chỉ đọc thuộc tính ở CẤP RUN, không tự động resolve kế thừa từ paragraph style. Trong file này, "HIỆU TRƯỞNG" dùng `pStyle w:val="Heading1"` và chính style "Heading 1" có `<w:b/>` ở cấp style — nên hiển thị đậm dù run không có `<w:b/>` riêng. Lỗi kiểm tra này lặp lại ở CẢ 2 lần rà soát trước (09/9 và 11/9) vì chỉ xem run XML mà không kiểm tra `d.styles[style_name].font.bold` khi run-level trả về None.
  3. **CV 9016/UBND-KTTH có nêu rõ Sở Tài chính là đầu mối nhận báo cáo** — "Kính gửi: Sở Tài chính" là đúng, không cần xác minh thêm qua kho 01-04 khi Phòng TH-HC&QT đã xác nhận trực tiếp bằng lời.

## BÀI HỌC KỸ THUẬT BẮT BUỘC CHO CÁC LẦN RÀ SOÁT SAU (đề xuất bổ sung SKILL.md / Ghi-Chu-Ky-Thuat.md)
Khi đo cỡ chữ/đậm/nghiêng bằng python-docx (`run.font.bold`, `.italic`, `.size` trả về `None`):
- `None` ở cấp run KHÔNG có nghĩa là "không có định dạng" — nó có nghĩa "không ghi đè, kế thừa từ paragraph style".
- PHẢI tra tiếp `paragraph.style` (và style cha qua `base_style` nếu cần) để lấy giá trị thực sự áp dụng, trước khi kết luận một thành phần thể thức "sai".
- Quy trình đúng: `val = run.font.bold; if val is None: val = paragraph.style.font.bold` (lặp lại cho toàn bộ chuỗi `base_style` nếu vẫn None).
- Đây là lỗi đã gây SAI 2 lần liên tiếp (09/9 và 11/9) trên cùng 1 điểm kiểm tra — cần vá `tools/_read_input_properties.py` hoặc quy trình đo Bước 0b để tự động resolve kế thừa style, tránh lặp lại.

## Kết quả sau khi tiếp thu phản hồi
Chỉ còn 2 vấn đề: 1 Mức 1 ("Hạn chế... Không." — vẫn tồn tại qua cả 3 lần rà soát, đơn vị soạn thảo cần tự viết nội dung thật) và 1 Mức 3 tùy chọn ("Căn cứ" → "Thực hiện" cho công văn).

Kết luận: **CHƯA ĐỦ ĐIỀU KIỆN TRÌNH KÝ** — chỉ còn 1 lỗi Mức 1 bắt buộc xử lý.

## ID đầu ra
`Bao-cao-ra-soat-KTC897_BC-9-thang-dau-nam-2026_v3_lan3_20260911.docx`
