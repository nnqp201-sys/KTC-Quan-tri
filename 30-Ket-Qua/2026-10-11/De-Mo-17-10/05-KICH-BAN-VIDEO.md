# Kịch bản video minh họa — buổi làm việc ngày 17/10/2026

Hai video, khớp Phương án bản 5 (mục 3 và mục 5). Quan điểm: Chỉ quay những việc công cụ làm tốt, có sản phẩm thật. Khung hình 1920×1080, chữ tối thiểu cỡ 32 để đọc được trên máy chiếu
hội trường; mọi màn hình có dòng nhỏ góc dưới: **"Dữ liệu giả định phục vụ trình diễn"** (trừ cảnh giới thiệu kho, chỉ
quay cây thư mục và 01 tệp mô tả văn bản đã công khai).

## Cách làm — ai làm phần nào

| Phần | Em làm được trên máy này | Anh (hoặc đồng chí Công) làm |
|---|---|---|
| Video 1 — Giới thiệu nhanh 03 hệ (≈5 phút) | Dựng trọn: trang trình chiếu + lời đọc giọng nữ tiếng Việt + phụ đề → tệp `.mp4` | Xem, duyệt lời đọc |
| Video 2 — Trình diễn (≈20 phút, 3 đoạn) | Kịch bản từng cảnh, lời đọc, trang tiêu đề, ghép, phụ đề, xuất `.mp4` | **Quay màn hình** khi chạy Cowork trên bộ dữ liệu giả định (em không điều khiển được màn hình Claude Desktop của anh) |

**Quay màn hình (Video 2):** Windows 11 có sẵn — mở **Snipping Tool**, chọn **Ghi (Record)**, quét vùng cửa sổ Claude
Desktop, bấm Bắt đầu; hoặc phím **Win + Alt + R** (Xbox Game Bar). Mỗi cảnh quay một tệp, đặt tên `C2-01.mp4`, `C2-02.mp4`…
vào thư mục `Video/quay/`. Không cần lời nói khi quay — em lồng lời đọc sau. Đặt độ phân giải màn hình 1920×1080,
phóng chữ Claude Desktop lên 125%.

**Công cụ em cần cài (cần anh đồng ý):** `imageio-ffmpeg` (bộ ghép video), `Pillow` (vẽ trang), `edge-tts` (giọng đọc
tiếng Việt `vi-VN-HoaiMyNeural` của Microsoft — **lời đọc được gửi lên máy chủ Microsoft để chuyển thành giọng nói**; lời
đọc chỉ là nội dung công khai trong kịch bản, không có dữ liệu nội bộ). Không dùng giọng máy thì anh tự đọc, ghi âm bằng
điện thoại, em ghép.

## Video 1 — Giới thiệu nhanh 03 hệ (khoảng 05 phút)

| Cảnh | Thời lượng | Hình | Lời đọc |
|---|---|---|---|
| 1.1 | 0:20 | Tiêu đề: "Ba hệ hỗ trợ tham mưu bằng trí tuệ nhân tạo — Phòng TH-HC&QT, Trường Cao đẳng Kon Tum" | Kính thưa các đồng chí, phòng Tổng hợp – Hành chính và Quản trị xin giới thiệu nhanh ba hệ đang dùng hằng ngày: kho dữ liệu nền, hệ rà soát văn bản và bộ công cụ quản trị nhiệm vụ. |
| 1.2 | 0:30 | Sơ đồ: Kho dữ liệu nền → Công cụ → Người kiểm tra → Ban hành | Nguyên tắc của chúng tôi là: nền móng trước, công cụ sau. Trí tuệ nhân tạo chỉ tham mưu đúng khi được đọc đúng văn bản của chính cơ quan. |
| 1.3 | 1:00 | Cây thư mục 05 kho + số văn bản từng kho (557 · 582 · 41 · 130 · 49) | Kho KTC-Database lưu trên Google Drive, gồm năm kho: văn bản pháp luật; quy chế, kế hoạch, báo cáo của Trường; mẫu văn bản; văn bản tốt làm mẫu văn phong; đề án. Tổng cộng khoảng một nghìn ba trăm văn bản, mỗi văn bản có tệp mô tả số hiệu, ngày, hiệu lực và văn bản thay thế. |
| 1.4 | 0:30 | Một câu hỏi tra cứu căn cứ → câu trả lời dẫn đúng văn bản trong kho | Khi soạn một kế hoạch, công cụ tìm căn cứ trong kho, dẫn đúng số hiệu, ngày ban hành, và cảnh báo văn bản đã hết hiệu lực. Kho chỉ cho phép đọc; công cụ còn có cơ chế chặn ghi. |
| 1.5 | 0:20 | Gợi ý cấu trúc kho cho cơ quan Đảng: văn bản cấp trên · quy chế làm việc · chương trình công tác · văn bản tốt · mẫu văn bản của Đảng · danh mục đơn vị, đầu mối | Đối với Đảng ủy Ủy ban nhân dân tỉnh, chúng tôi đề xuất thiết lập kho tương tự trước khi triển khai công cụ, không đưa tài liệu thuộc bí mật nhà nước vào kho. |
| 1.6 | 0:30 | Thư mục hệ KTC-Ra-Soat-897 bản 2.25: 09 bảng kiểm tra, thư viện kỹ năng, câu lệnh, bộ kiểm thử, mẫu báo cáo 08 phần | Hệ rà soát KTC-Ra-Soat-897 là bộ quy tắc rà soát dự thảo trước khi trình ký theo Thông báo 897 của Trường: bốn hệ quy chiếu, trong đó có riêng văn bản của Đảng; chín bảng kiểm tra; báo cáo tám phần, xếp vấn đề theo bốn mức. Còn vấn đề mức một thì không trình ký. |
| 1.7 | (chuyển sang Phần 3) | Bảng kiểm thử 10/10/2026: 24/30 đúng hoàn toàn · 02 sai mức · 04 bỏ sót | Hệ được kiểm thử định kỳ trên một tệp cài sẵn ba mươi lỗi: lần gần nhất phát hiện đúng hai mươi bốn lỗi. Chúng tôi công khai cả phần chưa đạt, vì vậy luôn cần người kiểm tra. |
| 1.8 | 1:00 | Sơ đồ chu trình: Kế hoạch → Giao việc → Theo dõi → Báo cáo → Rà soát → Trình ký; 08 kỹ năng, 07 tác tử | Bộ công cụ KTC-Quan-tri khép kín chu trình quản trị nhiệm vụ: tám kỹ năng, bảy tác tử kiểm tra độc lập. Trong mười ngày làm việc gần đây, phòng đã dùng thật cho hai mươi sáu phiên, chín trăm hai mươi bốn thao tác, hỗ trợ dựng ba mươi lăm văn bản. |
| 1.9 | 0:20 | 01 trang kinh nghiệm thực chiến (từ kết quả lệnh tại `01-LENH-…`) | (Lời đọc viết sau khi có kết quả tổng hợp kinh nghiệm thực chiến.) |

## Video 2 — Trình diễn trên tình huống giả định (khoảng 20 phút, 3 đoạn)

Mỗi cảnh: anh quay màn hình khi chạy lệnh trên Cowork; em lồng lời đọc, phóng to vùng kết quả, thêm phụ đề.

| Cảnh | Nội dung quay | Lệnh gõ trong Cowork (dự kiến) | Điểm phải thấy rõ trên hình |
|---|---|---|---|
| 2.1 **(trọng tâm Phần 1)** | Tổng hợp dự thảo kế hoạch quý của 06 đơn vị (D1) thành kế hoạch của cơ quan | "Kiểm tra hồ sơ kế hoạch quý của các đơn vị trong thư mục này, rồi tổng hợp thành dự thảo Kế hoạch công tác quý của cơ quan" | Bảng kiểm từng đơn vị; nhiệm vụ trùng; dự thảo kế hoạch xếp theo lĩnh vực, giữ nguồn đơn vị |
| 2.2 | Tra cứu Hệ thống quản lý văn bản và điều hành (D2), đối chiếu với D1 | "Từ danh mục văn bản này, liệt kê văn bản chỉ đạo, kế hoạch năm, quý, thông báo kết luận, kế hoạch chuyên đề trong kỳ; nhiệm vụ nào đã giao mà chưa đơn vị nào đưa vào kế hoạch?" | Nhiệm vụ còn thiếu kèm số, ký hiệu văn bản giao |
| 2.3 (nói nhanh) | Trích nhiệm vụ từ 01 văn bản chỉ đạo; cảnh báo hạn; công văn đôn đốc | Mở 03 kết quả đã chạy | Cột căn cứ; danh sách "cần hỏi lại" |
| 2.4 **(trọng tâm Phần 2)** | Xây dựng báo cáo tháng từ báo cáo 06 đơn vị (D3) | "Lập báo cáo kết quả công tác tháng của cơ quan từ báo cáo các đơn vị, phát triển từ báo cáo tháng trước" | Bộ 04 sản phẩm; tệp ghi chú đối soát nguồn |
| 2.5 | Đối chiếu kế hoạch với kết quả, gợi ý minh chứng từ D2 | "Đối chiếu kế hoạch tháng với báo cáo; nhiệm vụ nào chưa có thông tin; văn bản nào có thể là minh chứng" | Ghi "chưa có thông tin", không kết luận "chưa làm" |
| 2.6 (nói nhanh) | Hỏi nhanh phục vụ giao ban | "Đơn vị nào còn nhiệm vụ tồn đọng, vướng mắc gì?" | Câu trả lời dẫn dòng dữ liệu |
| 2.7 (nói nhanh) | Hai sản phẩm soạn thảo thực tế đã lược thông tin | Mở tệp | Dựng từ văn bản đã ban hành |
| 2.8 **(trọng tâm Phần 3)** | Rà soát dự thảo **văn bản của Đảng** trong D4 (Chương trình công tác tháng 10 của Ban Thường vụ Đảng ủy UBND phường XYZ, đã ẩn danh) bằng KTC-Ra-Soat-897 bản 2.25; mở thư mục hệ | "Rà soát chính thức dự thảo này theo KTC-Ra-Soat-897. Đây là văn bản của cơ quan khác, không áp quy ước riêng của Trường" | Công cụ tự nhận ra văn bản của Đảng, áp Hướng dẫn 05-HD/VPTW, không áp Nghị định 30; đo thể thức trên tệp; báo cáo 08 phần: 25 phát hiện, 0 Mức 1, 07 Mức 2 (kết quả chạy trước ở `Ket-qua-chay-truoc/`) |
| 2.9 | Văn bản có dấu vết thay đổi; bảng kiểm thử 24/30 | Mở tệp | Người duyệt thấy từng chỗ sửa |

Lời đọc Video 2 em viết sau khi có bộ dữ liệu giả định và bản quay thật, để lời khớp đúng hình.

## Lịch

12/10 bộ dữ liệu giả định, văn bản Đảng ẩn danh, báo cáo rà soát chạy trước (đã xong, tại `30-Ket-Qua/2026-10-12/De-Mo-17-10/`) · 13/10 chạy thử trên Cowork · 14/10 anh quay phần đầu 04 thao tác · Video 1 đã dựng bản 1 · 15/10 em ghép Video 2, anh duyệt
· 16/10 chiếu thử trên máy chiếu Hội trường 24-10.
