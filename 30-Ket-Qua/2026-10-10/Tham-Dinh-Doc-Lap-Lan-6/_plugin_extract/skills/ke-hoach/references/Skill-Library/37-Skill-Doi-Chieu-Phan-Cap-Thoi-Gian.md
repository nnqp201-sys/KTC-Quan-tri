# 37-Skill-Doi-Chieu-Phan-Cap-Thoi-Gian

## Purpose
Kiểm tra kế hoạch tháng có bám đúng kế hoạch quý, kế hoạch quý có bám đúng kế hoạch năm — phát hiện nhiệm vụ phát sinh ngoài kế hoạch cấp trên.

## Khi nào dùng
Khi lập Kế hoạch tháng/quý, cần đối chiếu với Kế hoạch cấp thời gian lớn hơn đã ban hành.

## Điều kiện tiên quyết
Cần có KH cấp trên trong `KH-Cap-Tren/` đúng phạm vi kỳ. Nếu không có → DỪNG và báo rõ: "Chưa có Kế hoạch [quý/năm] để đối chiếu — không thể xác nhận tính nhất quán."

## Nhiệm vụ
1. Với mỗi nhiệm vụ trong KH cấp trên, kiểm tra đã được phân bổ vào kỳ nhỏ hơn chưa.
2. Với nhiệm vụ trong kỳ nhỏ KHÔNG có trong KH cấp trên → "Phát sinh ngoài KH cấp trên", đề nghị xác nhận.
3. Kiểm tra tổng nguồn lực/mốc thời gian phân bổ không mâu thuẫn giữa các kỳ.

## Ràng buộc
- Không tự quyết nhiệm vụ phát sinh có được chấp nhận — chỉ nêu để người có thẩm quyền quyết.
- Không suy diễn nội dung KH cấp trên nếu chưa đọc được văn bản đó (Nguyên tắc 1).

## Output
Bảng đối chiếu: Nhiệm vụ KH cấp trên | Đã phân bổ vào kỳ nhỏ? | Ghi chú + Danh sách phát sinh ngoài KH cấp trên.
