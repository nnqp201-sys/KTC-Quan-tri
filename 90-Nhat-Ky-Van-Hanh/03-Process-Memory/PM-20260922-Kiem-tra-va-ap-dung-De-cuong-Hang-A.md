```yaml
memory_id: PM-20260922-001
created_at: 2026-09-22
memory_type: process
status: open
task_type: doi_chieu_hai_ban_thao_va_ap_dung_track_changes
project_name: KTC-Quan-tri
```

# Đối chiếu "Kiem tra. 22.9.2026" với bản Track Changes 21/9 — áp lại bằng Track Changes

**Kết quả:** `30-Ket-Qua/2026-09-22/De-cuong-Hang-A/De_cuong_De_an_Hang_A_ap-dung-kiem-tra-22-9-2026-TC.docx` (222 thay đổi, 2 tác giả) + nhật ký sửa đổi.
**Nguồn:** so `Kiem tra. 22.9.2026 Du thao De_cuong_De_an_Hang_A.docx` (không có Track Changes, đã chấp nhận/soạn thủ công) với `De_cuong_De_an_Hang_A_dieu-chinh-van-phong-Dang-kiem-TC_20260921.docx` (bản 21/9, **đã bị chỉnh tay thêm** sau khi tôi giao — không còn khớp bản tôi xuất, ví dụ QĐ 679/QĐ-CĐKT → 2047/QĐ-CĐKT đã sửa sẵn ở một chỗ).

## Kỹ thuật đối chiếu — bài học chính

**So theo vị trí đoạn (zip theo index) sai hoàn toàn** khi hai văn bản có số đoạn khác nhau ở giữa (ở đây do TOC chèn/xóa dòng) — toàn bộ phần sau bị lệch chỉ số, in ra hàng trăm dòng "khác nhau" giả. Phải so bằng `difflib.SequenceMatcher` trên danh sách khối (đoạn văn + mỗi hàng bảng là một khối), sau đó so ký tự bên trong từng cặp khối khớp.

**Quy tắc viết hoa "Hạng A"**: người kiểm tra không gõ tay từng chỗ mà dùng Tìm & Thay thế Word cho đúng một chuỗi `hạng A` → `Hạng A` toàn văn (khớp cả bên trong `hạng A1` vì `hạng A` là chuỗi con). Xác nhận bằng cách đếm: 0 chuỗi `hạng A` viết thường còn sót trong bản kiểm tra, đúng bằng tổng số chuỗi trong bản gốc. Việc này để lại 6 lỗi `HHạng` (thừa một chữ H) trong bản kiểm tra — **không chép lại lỗi đó**, chỉ áp đúng quy tắc bằng `tc.thay("hạng A", "Hạng A", tat_ca=True)`.

## Hai lỗi kỹ thuật tự phát hiện khi đối chiếu ngược (quan trọng, tái dùng cho lần sau)

1. **`tc.thay()`/`_tim()` không nhìn thấy nội dung mình vừa chèn trong cùng phiên.** `_runs_text()` chỉ đọc `<w:r>` là con trực tiếp của đoạn; văn bản vừa được `thay()`/`doan_moi_sau()` chèn nằm trong `<w:ins>` (lồng một cấp) nên vòng quét toàn văn chạy **sau đó** trong cùng script sẽ không thấy để sửa tiếp. Hệ quả: nếu tự viết `hạng A` (thường) trong chuỗi thay thế rồi định "dọn" bằng một lượt `tat_ca=True` ở cuối, phần chữ mình vừa chèn **không được dọn** — phải viết đúng hoa/thường ngay trong chuỗi thay thế, không trông chờ bước quét dọn cuối cùng xử lý hộ.
2. **`xoa_cum()` xóa đúng-và-chỉ-đúng chuỗi truyền vào — không phải "xóa đến hết câu".** Từng gõ nhầm `xoa_cum("2. Về phương tiện, thiết bị:")` để định bỏ **dấu hai chấm** cuối tiêu đề, nhưng lệnh này xóa **toàn bộ tiêu đề**, để lại đoạn Heading rỗng (biến mất khỏi bản đã chấp nhận, không còn phát hiện được qua tìm từ khóa). Bỏ một ký tự cuối câu phải dùng `thay(cả_câu_cũ, cả_câu_thiếu_ký_tự)`, không dùng `xoa_cum` với toàn bộ chuỗi.
3. Tương tự, `xoa_cum(" cho ý kiến, giao khoa Đào tạo và Sát hạch lái xe làm việc với Phòng Cảnh sát giao thông")` (cụm quá dài, thừa nghĩ là cần cho khớp duy nhất) đã xóa nhầm luôn phần muốn giữ lại. Sửa: cụm cần xóa phải **chỉ vừa đủ và đúng phần muốn bỏ** (ở đây chỉ `" cho ý kiến,"`), kiểm `text.count(cụm)==1` trước khi gọi.

**Cách bắt lỗi**: sau khi build, phải đối chiếu lại toàn văn bản-đã-chấp-nhận-Track-Changes với bản mục tiêu bằng `_text_day_du(..., True)` (không dùng `paragraph.text`/`cell.text` của python-docx vì bỏ sót nội dung trong `<w:ins>`) — vòng đối chiếu đầu tiên dùng nhầm `cell.text` cho ô bảng khiến tưởng nhầm là lỗi lớn (hàng loạt ô bảng "mất chữ Hạng A"), thật ra XML đúng, chỉ là công cụ kiểm tra sai.

## Nội dung thực chất đã áp dụng (ngoài viết hoa Hạng A)
- QĐ 679/QĐ-CĐKT (14/7/2023) → QĐ 2047/QĐ-CĐKT (21/9/2026), 2 chỗ còn sót trong đoạn "Bộ môn ĐT&SHLX mô tô".
- "Thư ký khoa" → "Giáo vụ khoa" trong cơ cấu tổ chức Khoa.
- Bỏ câu "Nội dung này đề nghị Lãnh đạo Trường cho ý kiến." và câu "Không nêu họ tên, ngày sinh, số căn cước công dân trong Đề án." (trùng lặp/thừa).
- "Trung tâm sát hạch lái xe" → "khoa Đào tạo và Sát hạch lái xe" trong liệt kê nguồn lực kế thừa (Mục tiêu chung).
- Một số chỗ viết hoa chữ đầu sau dấu hai chấm và đầu mục liệt kê (1)(2)(3)... theo văn phong 897.
- Sửa ngày họp Tổ (bảng tiến độ): 22/9/2026 → 21/9/2026.

## Còn treo
- Mục lục (TOC) chưa refresh field — cần mở Word, Ctrl+A rồi F9 (hoặc chuột phải chọn Update Field) trước khi giao bản chính thức.
- Chưa chạy lại rà soát 897 đầy đủ trên bản này (chỉ chạy `kiem_the_thuc.py`: 2 gợi ý Mức 3 kế thừa từ bản gốc, không phải lỗi mới).
- Chưa xác minh QĐ 2047/QĐ-CĐKT (21/9/2026) có trong KTC-Database hay chưa — đây là văn bản rất mới (ký cùng ngày phiên làm việc trước), khả năng chưa kịp nạp kho.
