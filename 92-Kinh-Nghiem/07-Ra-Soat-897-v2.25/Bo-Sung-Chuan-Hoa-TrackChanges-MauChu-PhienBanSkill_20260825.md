# Bổ sung Hệ KTC-Ra-Soat-897-v2-Cai-tien — Chuẩn hóa Track Changes, màu chữ, hiển thị phiên bản Skill và nguyên tắc rà soát

## Ngày bổ sung: 25/8/2026 — không thay thế SKILL.md gốc, đọc cùng

## 0. Nguồn gốc
Đúc kết từ thực tế soạn thảo/rà soát lặp nhiều vòng Đề án thành lập Trung tâm Đăng kiểm xe cơ giới (Tờ trình, Quyết định, Báo cáo rà soát 897) trong phiên làm việc với Anh Phục (Phó Trưởng phòng TH-HC&QT), 16-25/8/2026. Áp dụng cho mọi tác vụ (a) rà soát chính thức và các tác vụ soạn thảo/chỉnh sửa văn bản .docx liên quan.

## 1. Bắt buộc bật Track Changes khi chỉnh sửa .docx
Mọi thao tác chỉnh sửa nội dung văn bản .docx đã có (Đề án, Tờ trình, Quyết định, Báo cáo...) đều phải thực hiện bằng track changes (`<w:ins>`/`<w:del>` OOXML), **không bao giờ sửa trực tiếp không dấu vết** — kể cả khi người yêu cầu không nhắc lại điều này ở mỗi lượt, trừ khi người yêu cầu minh thị nói "không cần track changes".

## 2. Phân biệt màu chữ theo loại thay đổi — dùng nhiều "author" khác nhau
Word tự gán màu theo từng `w:author` riêng biệt (không thể ép cứng đúng mã màu đỏ/xanh/tím qua XML, nhưng dùng nhiều author sẽ cho nhiều màu phân biệt nhất quán). Quy ước đặt tên author:
- **"Nội dung bỏ (Claude)"** — thuần xóa, không thay thế (dùng `<w:del>` một mình).
- **"Nội dung bổ sung (Claude)"** — thuần thêm mới (dùng `<w:ins>` một mình).
- **"Nội dung điều chỉnh (Claude)"** — xóa + thêm cùng lúc để thay thế nội dung (cặp `<w:del>` + `<w:ins>` liền nhau, cùng author để Word tô cùng 1 màu cho cả xóa và thêm của cùng 1 thay đổi).
- **Đợt "làm sạch" riêng** (sửa lỗi số liệu/kỹ thuật, tách biệt với đợt điều chỉnh nội dung thông thường trước đó): dùng thêm 1 author mới cho riêng đợt đó, ví dụ `"Làm sạch số liệu tài chính (Claude)"`, để người xem phân biệt trực quan "đợt sửa nào" chỉ bằng màu, không cần đọc kỹ mới biết.
- Xóa hẳn 1 hàng bảng: dùng đúng cơ chế OOXML `<w:trPr><w:del w:id=".." w:author=".." w:date=".."/></w:trPr>` (đặt `<w:del>` là phần tử **cuối cùng** trong `<w:trPr>`, sau `<w:trHeight>` nếu có — sai thứ tự phần tử sẽ làm hỏng schema), kết hợp wrap toàn bộ text trong hàng bằng `<w:del>` để hiển thị gạch ngang khi xem trước — không chỉ tô màu chữ mà bỏ qua đánh dấu xóa hàng.
- Trước khi giao file: chạy script `validate.py` (đối chiếu file gốc + từng author) và xuất PDF soi từng trang có thay đổi trọng yếu để xác nhận hiển thị đúng, không có lỗi rPr lồng nhau hay xml:space trùng lặp.

## 3. Báo cáo rà soát 897 phải hiển thị rõ phiên bản Skill đang dùng
Bổ sung bắt buộc tại Phần I "Thông tin chung" (hoặc ngay dưới tiêu đề trang đầu): một dòng ghi rõ tên hệ (**Hệ KTC-Ra-Soat-897-v2-Cai-tien**) kèm **số phiên bản và ngày cập nhật gần nhất** lấy từ mục "Lịch sử cập nhật" cuối SKILL.md tại thời điểm rà soát (ví dụ: "v2.10, cập nhật 19/8/2026"). Mục đích: người đọc nhiều báo cáo theo thời gian biết ngay báo cáo được tạo bằng bộ quy tắc phiên bản nào, tránh so sánh nhầm giữa các đợt rà soát dùng quy tắc khác nhau.

## 4. Nguyên tắc rà soát/giải trình đã đúc kết qua thực tế

**a) Không mặc nhiên tin lời phản hồi của người có thẩm quyền.**
Khi báo cáo rà soát kỳ trước có phản hồi/chỉ đạo trực tiếp (ví dụ "đã điều chỉnh", "đã bổ sung", "Phản hồi: Đã..."), Claude phải đọc **trọn vẹn** đoạn văn bản thực tế liên quan (không trích dẫn cụt, không dừng ở câu đầu) hoặc tính toán lại độc lập, rồi mới ghi kết luận "Đạt". Trích dẫn thiếu có thể dẫn đến kết luận sai là "chưa xử lý" trong khi thực tế đã xử lý đủ ở phần cuối câu — đã xảy ra thực tế và phải rút kinh nghiệm.

**b) Tự đính chính minh bạch khi tự phát hiện sai sót của chính mình.**
Nếu trong lúc rà soát tự nhận ra một kết luận trước đó của chính Claude là sai (ví dụ do trích dẫn thiếu, tính nhầm công thức), phải ghi rõ trong báo cáo là đã tự phát hiện và đính chính — không lặng lẽ sửa lại như thể chưa từng sai.

**c) Giải trình/tiếp thu ý kiến cơ quan ngoài — chỉ trả lời đúng trọng tâm.**
Khi soạn nội dung tiếp thu, giải trình gửi Sở/ngành/cơ quan bên ngoài, chỉ trả lời đúng phạm vi câu hỏi/ý kiến đã nêu. Không tự suy diễn, mở rộng thêm các lập luận pháp lý khác — dù đúng và đã xác minh trong quá trình trao đổi nội bộ — nếu bên hỏi không yêu cầu. Mở rộng ngoài phạm vi làm loãng nội dung và có thể khiến cơ quan góp ý "hỏi ngược" thêm ở vòng sau.

**d) Nghị định 60/2021/NĐ-CP luôn phải tra kèm Nghị định 111/2025/NĐ-CP.**
Khi tra cứu hoặc trích dẫn NĐ 60/2021/NĐ-CP (cơ chế tự chủ tài chính ĐVSNCL), bắt buộc đối chiếu đồng thời NĐ 111/2025/NĐ-CP (22/5/2025, hiệu lực từ 07/7/2025, sửa đổi bổ sung nhiều điều của NĐ 60/2021) trước khi kết luận về điều kiện áp dụng — không tách rời hai văn bản. Nhiều điều khoản đã thay đổi so với bản gốc 2021 (ví dụ: điều kiện "70% tự bảo đảm chi thường xuyên" tại Điều 24 khoản 3 đã bị bãi bỏ; yêu cầu "ý kiến Thường trực HĐND" tại Điều 25 khoản 2 đã bị bãi bỏ).

**e) Ưu tiên python-docx khi tạo văn bản hành chính dạng bảng.**
Khi cần tạo file .docx theo thể thức hành chính Việt Nam có bảng biểu phức tạp (border tùy chỉnh, merge ô, shading, kiểm soát chính xác định dạng), ưu tiên dùng `python-docx` thay vì thư viện `docx` (Node/docx-js) — độ chính xác định dạng cao hơn theo đánh giá thực tế qua nhiều lần so sánh.

## 5. Liên quan
Đọc cùng SKILL.md gốc, `28-Skill-Bao-Cao-Ra-Soat-Chuan.md` (đặc tả trình bày 8 phần), và bổ sung trước đó `Skill-Tu-hoc-Phong-Cach-Bao-Cao-ra-soat.md`. Khi có phát hiện mới về kỹ thuật track-changes hoặc nguyên tắc rà soát, ghi tiếp vào file này (bổ sung mục 6, 7...), không tạo file rời rạc mới cho cùng chủ đề.
