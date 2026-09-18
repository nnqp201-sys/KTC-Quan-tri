# 18-Skill-Kiem-Tra-Tinh-Thong-Nhat

## Purpose
Kiểm tra tính thống nhất về tên gọi trong toàn văn bản và giữa văn bản với hệ thống quy định của Trường: tên đơn vị, tên chức danh, tên chương trình, tên dự án/đề án.

## When to use
- Văn bản dài, nhiều lần nhắc đến tên đơn vị/chương trình/dự án.
- Trước khi ban hành chính thức, để tránh sai tên đơn vị hoặc chức danh đã đổi.

## Inputs
- Toàn văn bản
- Danh mục tên đơn vị/chức danh hiện hành của Trường (nếu có trong Knowledge Graph/Entities)

## Checklist logic
- Tên đơn vị viết đúng và nhất quán trong toàn văn bản (không viết tắt khác nhau ở các đoạn)
- Tên chức danh đúng với cơ cấu tổ chức hiện hành
- Tên chương trình/dự án/đề án giữ nguyên một cách viết xuyên suốt
- Không dùng tên cũ của đơn vị/chương trình đã đổi tên hoặc giải thể

## Output
- Danh sách chỗ không thống nhất (vị trí, cách viết khác nhau, cách viết đúng đề xuất)

## Must not do
- Không tự đổi tên khi chưa chắc chắn tên nào là tên hiện hành — gắn cờ để người soạn xác nhận.

## Related
- Knowledge Graph: `09-Knowledge-Graph/01-Entities.md`
- Checklist: `08-Checklist/04-Ngon-Ngu.md`
