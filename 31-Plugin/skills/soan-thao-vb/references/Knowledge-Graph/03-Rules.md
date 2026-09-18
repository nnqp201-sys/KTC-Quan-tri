# 03-Rules

## Purpose
Store reasoning and selection rules used by the system (quy tắc suy luận và lựa chọn).

## Selection rules
- Xác định loại văn bản (Document Type) trước tiên bằng `05-Skill-Phan-Tich-Yeu-Cau.md`, trước khi chọn bất kỳ skill/prompt nào khác.
- Khi văn bản thuộc một Business Domain cụ thể (đào tạo, tuyển sinh, cán bộ, tài chính, đảm bảo chất lượng, đối ngoại, cấp phòng), luôn kết hợp Skill nghiệp vụ (Nhóm D) với Skill theo loại văn bản (Nhóm B) — không dùng riêng lẻ.
- Luôn áp dụng Skill nền (Nhóm A: 01-06) làm khung xử lý chung, bất kể loại văn bản.
- Skill kiểm tra xuyên suốt (Nhóm C: 14-19) áp dụng SAU khi có bản nháp, KHÔNG áp dụng trước khi soạn thảo.

## Priority rules (thứ tự ưu tiên căn cứ pháp lý)
1. Luật > Nghị định > Thông tư (văn bản trung ương)
2. Văn bản chỉ đạo/kế hoạch của tỉnh (khi văn bản của Trường triển khai chủ trương tỉnh)
3. Quy chế/Quy định nội bộ Trường (khi đã có quy định cụ thể và không trái luật)
4. Không có căn cứ rõ ràng → đánh dấu (flag) để người soạn xác minh, KHÔNG tự suy diễn hoặc bịa căn cứ.

## Quality gate rules
- Không cho văn bản qua bước "Đánh giá chất lượng" (`19-`) nếu còn lỗi Critical ở bước thể thức (`02-`, `14-`) hoặc thiếu căn cứ pháp lý bắt buộc (`03-`).
- Không cho văn bản qua bước "Trình ký" nếu `17-Skill-Kiem-Tra-Tham-Quyen.md` kết luận sai thẩm quyền.
- Văn bản nhân sự (`22-`), tài chính (`23-`) luôn cần đủ căn cứ quy trình (biên bản họp, đề nghị, phê duyệt trước) — đây là lĩnh vực nhạy cảm, áp dụng ngưỡng kiểm tra chặt hơn các loại văn bản thông thường.

## Workflow stability rules
- Giữ nguyên thứ tự workflow: Soạn thảo → Rà soát → Trình ký → Ban hành → Lưu trữ → Cập nhật. Không bỏ qua bước Rà soát dù văn bản gấp.
- Sau khi Ban hành, luôn cập nhật Knowledge Graph và Training Data nếu văn bản trở thành "Good Document" mới hoặc phát sinh case lỗi mới (Negative Example).
