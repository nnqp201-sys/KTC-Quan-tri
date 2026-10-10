# 04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet (bổ sung 10/8/2026)

## Phân biệt rõ 2 việc khác nhau — không nhầm lẫn
1. **Dùng Internet để TRẢ LỜI 1 câu hỏi** (đã có quy tắc tại `00-Quy-Tac-Khai-Thac-Internet.md`) — chỉ dùng tạm cho câu trả lời đó, đánh dấu chữ đỏ, không tự động lưu vào kho.
2. **Dùng Internet để NẠP VĨNH VIỄN vào kho 01-04** (nguyên tắc MỚI này) — rủi ro cao hơn nhiều vì văn bản sẽ trở thành "nguồn tin cậy" cho mọi tác vụ sau này. Phải chặt hơn hẳn.

## Điều kiện BẮT BUỘC trước khi nạp 1 văn bản từ Internet vào kho chính thức

1. **Chỉ nhận nguồn Mức 1 hoặc Mức 2** (theo phân loại tại `00-Quy-Tac-Khai-Thac-Internet.md`):
   - Mức 1: **`https://phapluat.gov.vn/` (ưu tiên cao nhất)**, Công báo Chính phủ, vbpl.vn, Cổng TTĐT Chính phủ/Bộ/tỉnh, website chính thức của Trường.
   - Mức 2: Báo Chính phủ, TTXVN, Nhân Dân.
   - **TUYỆT ĐỐI KHÔNG nạp vào kho chính thức** văn bản từ Mức 3 (học thuật), Mức 4 (tham khảo), hoặc bất kỳ nguồn không chính thức nào (blog, diễn đàn, mạng xã hội, Wikipedia) — dù có thể dùng tạm để trả lời 1 câu hỏi, không được lưu vĩnh viễn.
2. **Xác minh còn hiệu lực** tại thời điểm tải — không nạp văn bản đã biết hết hiệu lực/bị thay thế (trừ khi nạp có chủ đích để lưu làm tài liệu lịch sử, phải ghi rõ ràng "ĐÃ HẾT HIỆU LỰC" ngay từ khi nạp).
3. **Kiểm chứng chéo khi có thể** — nếu văn bản quan trọng (dùng làm căn cứ pháp lý chính), đối chiếu ít nhất 1 nguồn Mức 1 khác trước khi nạp.
4. **KHÔNG tự động nạp** — sau khi tìm được văn bản đạt đủ 3 điều kiện trên, phải trình bày cho người dùng: tên văn bản, nguồn, link, ngày tải, đánh giá hiệu lực — và CHỜ người dùng xác nhận "có" mới nạp vào 01-04. Không tự quyết định thay.

## Trường metadata bổ sung — bắt buộc cho văn bản có nguồn gốc Internet
Thêm vào `00-Metadata-Schema.md`, trường thứ 12:
- **Nguồn gốc nạp**: "Do người dùng/Trường cung cấp" (mặc định) HOẶC "Tải từ Internet — [tên nguồn] — [URL] — ngày tải [dd/mm/yyyy]".

Văn bản có "Nguồn gốc nạp = Tải từ Internet" phải được **rà soát lại định kỳ** (gợi ý: mỗi 6 tháng) để xác nhận còn hiệu lực, vì đây là nguồn có rủi ro thay đổi cao hơn văn bản do Trường trực tiếp cung cấp.

## Không áp dụng quy tắc chặt này cho việc gì
- Với `02-KTC-Regulations` (văn bản nội bộ Trường): về bản chất không có trên Internet công khai — nếu tìm thấy văn bản dạng này qua tìm kiếm, đây là dấu hiệu bất thường (rò rỉ dữ liệu nội bộ), phải báo ngay cho người dùng, TUYỆT ĐỐI không tự nạp.
- Với `03-Templates`, `04-Good-Documents`: nếu là mẫu/ví dụ công khai từ nguồn uy tín (ví dụ mẫu văn bản do Bộ ban hành công khai), áp dụng đúng 4 điều kiện như trên.

## Liên quan
- `00-Quy-Tac-Khai-Thac-Internet.md` (phân loại nguồn, mức độ tin cậy)
- `00-Metadata-Schema.md` (trường 12 mới)
- `03-Quy-Trinh-Nap-Lieu-2-Tang.md` — quy trình nạp chung do hệ `ktc-database` quản lý; bước xác nhận với người dùng áp dụng thêm cho trường hợp này. Các hệ khác **chỉ đọc để đối chiếu, không nạp tài liệu vào kho**.
