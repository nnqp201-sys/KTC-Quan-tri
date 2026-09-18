# 00-Metadata-Schema — Schema chuẩn 11 trường (dùng cho mọi file trong 01-04)

## 11 trường bắt buộc
| # | Trường | Mô tả |
|---|---|---|
| 1 | Tên văn bản | Tên đầy đủ, chính xác |
| 2 | Loại | Luật/Nghị định/Thông tư/Quyết định/Kế hoạch/Thông báo/Báo cáo/Tờ trình/Công văn/Biên bản/Quy chế/Quy định... |
| 3 | Đơn vị ban hành | Tên cơ quan/đơn vị chính xác |
| 4 | Ngày ban hành | dd/mm/yyyy |
| 5 | Lĩnh vực | Đào tạo/Tuyển sinh/Tổ chức-Cán bộ/Tài chính/HSSV/Đảm bảo chất lượng/Đối ngoại/Văn thư/Tổng hợp... |
| 6 | Người ký | Họ tên, chức vụ |
| 7 | Từ khóa | 3-7 từ phản ánh nội dung chính |
| 8 | Căn cứ pháp lý | Văn bản gốc/cấp trên mà văn bản này dựa vào |
| 9 | Đối tượng áp dụng | Ai/đơn vị nào chịu tác động |
| 10 | Hiệu lực | Đang có hiệu lực / Đã hết hiệu lực (ghi rõ văn bản thay thế) / Chưa xác định |
| 11 | Văn bản liên quan | Văn bản khác cùng chủ đề, văn bản đã thay thế/được thay thế |

## 2 trường bổ sung riêng theo loại văn bản (nếu áp dụng)
| Loại | 2 trường bổ sung |
|---|---|
| Quyết định | Loại quyết định (quy phạm/cá biệt); Thẩm quyền ký |
| Kế hoạch | Loại kế hoạch (chiến lược/năm/quý/tháng); Giai đoạn thời gian |
| Thông báo | Nguồn gốc (họp/chỉ đạo); Phạm vi áp dụng |
| Báo cáo | Kỳ báo cáo; Cấp nhận (nội bộ/cấp trên) |
| Tờ trình | Cấp trình; Cấp phê duyệt |
| Công văn | Cơ quan nhận; Mục đích |
| Biên bản | Loại sự việc; Có biểu quyết hay không |

## 3 trường bắt buộc bổ sung cho MỌI kết quả xuất ra (theo Bổ sung 10/8/2026)
- **Nguồn dữ liệu đã dùng** — đã đối chiếu với file/thư mục nào trong 01-04.
- **Người kiểm tra** — để trống rõ ràng nếu chưa xác định, không bỏ qua trường này.
- **Trạng thái phê duyệt** — Bản nháp / Đã duyệt nội bộ / Chính thức.

## Trường thứ 12 — bắt buộc khi văn bản có nguồn gốc từ Internet (bổ sung 10/8/2026)
- **Nguồn gốc nạp**: "Do người dùng/Trường cung cấp" (mặc định, không cần ghi) HOẶC "Tải từ Internet — [tên nguồn] — [URL] — ngày tải [dd/mm/yyyy]". Xem quy tắc đầy đủ tại `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md`.

## Nguyên tắc điền
- Chỉ điền giá trị có căn cứ rõ trong văn bản/nguồn — đánh dấu "Không xác định" cho trường thiếu, không suy diễn.
- Trường "Hiệu lực": nếu phát hiện văn bản có dấu hiệu bị thay thế (đọc thấy câu "thay thế văn bản số..."), phải tạo ghi chú riêng đánh dấu văn bản cũ "ĐÃ HẾT HIỆU LỰC" — xem quy trình tại `03-Quy-Trinh-Nap-Lieu-2-Tang.md`.
