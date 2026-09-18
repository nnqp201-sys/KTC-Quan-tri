# 07-Metadata

## Vai trò
Gắn metadata dùng chung 1 schema 11 trường, chỉ khác 2 trường bổ sung riêng mỗi loại — dùng 1 prompt tổng quát, thay cho 7 file riêng trước đây (đã hợp nhất theo Phương án B, 07/8/2026).

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy gắn metadata cho văn bản sau:
- Loại văn bản: [...] — Văn bản nguồn: [...]

Trường bắt buộc (11 trường): Tên văn bản, Loại, Đơn vị ban hành, Ngày, Lĩnh vực, Người ký, Từ khóa, Căn cứ pháp lý, Đối tượng, Hiệu lực, Văn bản liên quan.

Trường bổ sung theo loại: Quyết định (Loại QĐ; Thẩm quyền ký) | Kế hoạch (Loại KH; Giai đoạn) | Thông báo (Nguồn gốc; Phạm vi) | Báo cáo (Kỳ; Cấp nhận) | Tờ trình (Cấp trình; Cấp phê duyệt) | Công văn (Cơ quan nhận; Mục đích) | Biên bản (Loại sự việc; Biểu quyết).

Output: bảng metadata đầy đủ + trường còn thiếu/cần xác minh.
