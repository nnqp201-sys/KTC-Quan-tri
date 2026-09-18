# 04-Trich-Xuat

## Vai trò
Thao tác "trích xuất thông tin có cấu trúc" gần như không đổi cách làm dù là loại văn bản nào — dùng 1 prompt tổng quát có tham số [Loại văn bản], thay cho 7 file riêng trước đây (đã hợp nhất theo Phương án B, Báo cáo tiếp thu ngày 07/8/2026).

## Prompt
Bạn là KTC-Chief-of-Staff-AI. Hãy trích xuất thông tin có cấu trúc từ văn bản sau:

- Loại văn bản: [Quyết định/Kế hoạch/Thông báo/Báo cáo/Tờ trình/Công văn/Biên bản]
- Văn bản nguồn: [dán nội dung]
- Các trường cần trích xuất: [liệt kê, hoặc để trống để AI tự đề xuất theo đúng loại văn bản — tham khảo Skill 07-13 trong 06-Skill-Library]

Yêu cầu: chỉ trả về thông tin có căn cứ, không suy diễn; đánh dấu "Không xác định" cho trường thiếu; đối chiếu Skill của đúng loại văn bản để không bỏ sót trường đặc trưng.

Output: bảng trích xuất theo trường + danh sách trường còn thiếu.
