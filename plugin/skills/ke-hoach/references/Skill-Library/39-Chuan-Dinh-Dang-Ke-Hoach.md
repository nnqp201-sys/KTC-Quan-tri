# DNA định dạng mẫu KTC-Ke-Hoach

## Nguồn chưng cất

Phân tích OOXML bằng Python ngày 14/08/2026 từ bốn tệp chính thức:

- Chương trình công tác trọng tâm năm 2026.
- Kế hoạch công tác Quý III/2026.
- Kế hoạch công tác tháng 8/2026.
- Quyết định ban hành Chương trình công tác trọng tâm năm 2026.

## 1. Chuẩn chung Excel

- Dùng font Times New Roman xuyên suốt; cỡ thân bảng chủ yếu 14 pt.
- Tiêu đề, tên cột, dòng nhóm và tên Trục dùng đậm; tiêu đề căn giữa.
- Nội dung nhiệm vụ căn trái hoặc căn đều, căn giữa theo chiều dọc, bật wrap text.
- Các cột mã/STT, người chỉ đạo, đơn vị, sản phẩm, số lượng, độ khó, thời hạn, điểm, hệ số căn giữa theo mẫu.
- Giữ khối quốc hiệu–tiêu ngữ, số/ký hiệu, địa danh–ngày tháng, tên kế hoạch, căn cứ, bảng nhiệm vụ, nơi nhận và khối ký.
- Giữ nguyên vùng gộp và đường viền của mẫu; không tự động autofit toàn trang.
- Trang in dùng A4 ngang (paper size 9), căn giữa theo chiều ngang.
- Luôn kiểm tra ở tỷ lệ hiển thị khoảng 80–85% và bản in A4 ngang.

## 2. Chương trình công tác năm

- Sheet chuẩn: `CTCT 2026`; vùng dùng A1:I112 trong mẫu gốc.
- Bố cục dữ liệu chính 8 cột A:H; cột I có dữ liệu phụ/kiểm soát ở một số dòng.
- A1:H1 gộp làm tiêu đề phụ lục; Times New Roman 14, đậm, căn giữa, wrap text; chiều cao khoảng 74,45 pt.
- Dòng tiêu đề cột dùng hai dòng (hàng 2–3), từng cột gộp dọc; đậm, căn giữa.
- Các tháng là dòng nhóm gộp A:H, nền xanh nhạt theo theme, chữ đậm; công thức đếm nhiệm vụ dạng `COUNTA` phải được bảo toàn/cập nhật đúng vùng.
- Độ rộng cột chuẩn tham chiếu: A 8,75; B 68,75; C 28,25; D 25,75; E 22,375; F 24,75; G 17,25; H 11,125.
- Dòng nhiệm vụ thường cao 37,5–45 pt; tăng lên 56,25–75 pt khi nội dung dài.
- Trang A4 ngang; zoom 80%; căn giữa ngang; lề xấp xỉ 0,75 inch trái/phải và 1 inch trên/dưới.

## 3. Kế hoạch công tác quý

- Sheet chuẩn: `KH Quý III`; vùng mẫu A1:L82, bảng chính A:K.
- Dòng 1: cơ quan ban hành bên trái A:B; quốc hiệu–tiêu ngữ bên phải E:K.
- Dòng 3: số/ký hiệu A:B, cỡ 13; địa danh–ngày tháng E:K, cỡ 14 nghiêng.
- Dòng 5: tên loại và trích yếu kế hoạch A:K, Times New Roman 14 đậm, căn giữa.
- Dòng 7: căn cứ A:K, cỡ 14, căn đều, căn trên, wrap text; chiều cao theo nội dung (mẫu 157,9 pt).
- Hàng 9–10 là tiêu đề 11 cột, gộp dọc từng cột; hàng 11 ghi số thứ tự cột (1)–(11).
- Cột chuẩn tham chiếu: A 5,75; B 41,75; C 13,75; D 16,25; E 12,75; F 7,375; G 13,375; H 8,375; I 8; J 7,125; K 7,875.
- Dòng nhóm lớn và dòng Trục gộp B:K; chữ đậm. Dòng nhiệm vụ dài tăng chiều cao theo bội 16,5 pt; không để nội dung bị cắt.
- Cuối văn bản: nơi nhận gộp A:B; khối ký gộp F:K; chữ “HIỆU TRƯỞNG” và họ tên đậm.
- A4 ngang, zoom 85%, căn giữa ngang; lề mẫu xấp xỉ 0,815 inch trái/phải, 0,894 inch trên, 0,644 inch dưới.

## 4. Kế hoạch công tác tháng

- Sheet chuẩn: `KH tháng 8`; vùng mẫu A1:K65.
- Bố cục tương tự kế hoạch quý nhưng căn cứ ngắn hơn và bảng bắt đầu sớm hơn.
- Dòng 1: cơ quan A:B; quốc hiệu E:K. Dòng 3: số A:B; ngày tháng E:K. Dòng 5: tên kế hoạch A:K.
- Dòng 7 chứa căn cứ kế hoạch quý và câu ban hành; cỡ 14, căn đều, wrap text.
- Hàng 8–9 là tiêu đề bảng; hàng 10 là số thứ tự cột.
- Cột chuẩn tham chiếu: A 5,816; B 37,18; C 13,816; D 16,543; E 12; F 7,906; G 9,453; H 8,453; I 7,18; J 5,18; K 12,09.
- Dòng nhóm “nhiệm vụ đầu quý”, tên Trục và “nhiệm vụ đột xuất/chuyển sang” gộp B:K, đậm.
- Cột ghi chú phải thể hiện rõ `Bổ sung ngoài KH quý`, `Kết luận giao ban`, `chuyển từ tháng trước` hoặc căn cứ tương đương.
- Nơi nhận A:B, khối ký E:K; A4 ngang, zoom 85%; lề xấp xỉ 0,5 inch trái/phải/dưới, 0,59 inch trên.

## 5. Quyết định ban hành

- Khổ A4 dọc 21 × 29,7 cm; lề trên 2 cm, dưới 2 cm, trái 3 cm, phải 2 cm.
- Header/footer cách mép khoảng 1,27 cm.
- Font Times New Roman; thân văn bản theo Normal, thường 13–14 pt theo mẫu cơ quan.
- Khối đầu trang dùng bảng 1 hàng × 2 cột, không lộ đường viền: cơ quan/số bên trái, quốc hiệu/ngày tháng bên phải.
- Tên `QUYẾT ĐỊNH` căn giữa, đậm; trích yếu căn giữa, đậm; dòng thẩm quyền căn giữa, đậm.
- Căn cứ và điều khoản căn đều; thụt đầu dòng 1,27 cm; giãn dòng 1,5; khoảng cách trước/sau chủ yếu 6 pt.
- `QUYẾT ĐỊNH:` căn giữa, đậm, khoảng cách trước/sau 12 pt.
- Điều 1–4 và chủ thể trách nhiệm dùng đậm có chọn lọc, không đậm toàn đoạn giải thích.
- Cuối văn bản dùng bảng 1 hàng × 2 cột cho nơi nhận và khối ký; không lộ đường viền.

## 6. Quy tắc bảo toàn khi tạo sản phẩm

1. Sao chép đúng mẫu loại kỳ; không chuyển tháng sang mẫu quý hoặc ngược lại.
2. Giữ tên sheet, cấu trúc gộp, công thức, kích thước cột/dòng, thiết lập in và khối ký.
3. Chỉ chèn thêm dòng trong vùng nhiệm vụ; sao chép đầy đủ định dạng từ dòng cùng vai trò gần nhất.
4. Khi thêm dòng phải mở rộng công thức đếm, vùng in, đường viền và các vùng nhóm có liên quan.
5. Chỉ đổi cơ quan, số/ký hiệu, ngày tháng, căn cứ, nội dung và người ký khi có dữ liệu nguồn hợp lệ.

