# PM-20260911-BC-9-thang-dau-nam-2026-v3-lan2

- **Tác vụ**: (a) Rà soát chính thức trước khi trình ký — LẦN THỨ 3 trên cùng hồ sơ (kế thừa PM-20260909 [bản v1] và PM-20260911-...-v3 [bản v3 lần 1]).
- **Hồ sơ**: Báo cáo kết quả công tác 9 tháng đầu năm; kế hoạch công tác 3 tháng cuối năm 2026 — Trường Cao đẳng Kon Tum. Người dùng đã tải lên bản .docx thứ 2 (cùng tên file, nội dung đã chỉnh sửa) trong cùng phiên làm việc.
- **Phương pháp**: so sánh diff trực tiếp (python-docx, difflib) giữa tệp mới và tệp đã rà soát lần trước để xác định chính xác đoạn nào thay đổi, tránh báo trùng các phát hiện đã xử lý.

## Kết quả đối chiếu 12 phát hiện của lần rà soát trước
ĐÃ SỬA (8): số liệu tuyển sinh 886→560 (khớp phép cộng); phông "BÁO CÁO"/trích yếu (Times New Roman đặt cấp run); viết hoa "Trung tâm Đăng kiểm xe cơ giới" nhất quán; bỏ cụm "(thay thế Quyết định số 988/QĐ-CĐKT)" chưa xác minh được; lỗi dấu hai chấm lặp; khoảng trắng thừa + câu trùng ý; Nơi nhận "Đoàn Trường"/"Hội Sinh viên Trường" đúng mẫu TB597; bổ sung ngày ban hành TT 05/2026 và 03/2026/TT-BGDĐT.

CHƯA SỬA (3): mục "Hạn chế... Không." (Mức 1, cốt lõi, tồn tại qua cả 3 lần rà soát); mã lớp K7C/K7T không nhất quán (Mức 2); "HIỆU TRƯỞNG" chưa in đậm (Mức 2, xác nhận lại qua XML).

KHÔNG ĐỔI, còn mở (2): "Căn cứ Công văn 9016..." (Mức 3); "Kính gửi Sở Tài chính" chưa xác minh đầu mối theo CV 9016 (Mức 4) — công văn này vẫn không có trong kho 01-04.

## Quyết định phân loại đáng lưu ý
- Xác nhận kỹ thuật diff-trước-khi-báo là cách hiệu quả để tránh lặp lại toàn bộ 12 mục cũ khi chỉ một phần nhỏ thay đổi — nên áp dụng làm chuẩn cho mọi lần rà soát lại trong cùng phiên (đề xuất bổ sung vào SKILL.md/Skill-Tu-hoc nếu Phòng TH-HC&QT xác nhận).
- Mục "Hạn chế... Không." tồn tại dai dẳng qua 3 lần rà soát — đáng chú ý vì đây là lỗi dễ sửa nhất về mặt kỹ thuật (chỉ cần viết lại 1 câu) nhưng khó nhất về nội dung (đòi hỏi đơn vị tự nhận hạn chế thật). Ghi nhận làm bài học: loại lỗi "tự nhận không có hạn chế" có xu hướng bị bỏ qua nhiều vòng chỉnh sửa hơn lỗi thể thức/chính tả.

## Kết quả cuối
Kết luận: **CHƯA ĐỦ ĐIỀU KIỆN TRÌNH KÝ.** Còn 1 Mức 1 và 2 Mức 2 cần xử lý.

## Vấn đề còn mở
1. Mục "Hạn chế..." — cần Phòng TH-HC&QT/đơn vị soạn thảo chủ động viết nội dung thật, AI không thể tự suy diễn hạn chế thay đơn vị.
2. CV 9016/UBND-KTTH và 2 Thông tư 05/2026, 03/2026/TT-BGDĐT vẫn chưa có trong kho 01-04 — đề nghị nạp qua ktc-database.
3. Trường "Người kiểm tra" trong báo cáo xuất ra còn placeholder.

## ID đầu ra
`Bao-cao-ra-soat-KTC897_BC-9-thang-dau-nam-2026_v3_lan2_20260911.docx` — đã giao người dùng trong phiên.
