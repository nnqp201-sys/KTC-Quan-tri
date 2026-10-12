# Nguyên liệu giao Veo 3 — và phần nào không nên giao

## Khuyến nghị: dùng Veo 3 cho cảnh dẫn, không dùng cho nội dung

Veo 3 tạo **đoạn phim ngắn (khoảng 8 giây mỗi lần)** từ lời mô tả. Ba giới hạn khiến Veo 3 không làm được "toàn bộ" video này:

| Việc | Veo 3 | Cách làm thay |
|---|---|---|
| Chữ tiếng Việt, số liệu trên hình (557, 582, 24/30…) | Hay sai dấu, sai số, mỗi lần tạo ra một khác | Trang hình do `Video/lam_video1.py` vẽ — đúng từng chữ, sửa được |
| Màn hình thật của Claude, thư mục kho, báo cáo rà soát | Không thấy được màn hình của anh; sẽ **vẽ ra một màn hình không có thật** | Quay màn hình thật (Snipping Tool) |
| Lời thuyết minh tiếng Việt dài 3–5 phút, đúng thuật ngữ | Chỉ có lời thoại ngắn trong từng đoạn 8 giây | Giọng đọc AI tiếng Việt, đã lồng trong Video 1 |

Trình chiếu trước Đoàn công tác một màn hình "do AI vẽ ra" như thể là công cụ thật là rủi ro lớn nhất, nên phần nội dung phải
là hình thật. Veo 3 dùng tốt cho **03 cảnh dẫn không có chữ** dưới đây (mỗi cảnh 8 giây), em ghép vào đầu, giữa, cuối video.

## 03 lời mô tả giao Veo 3 (dán nguyên văn, tiếng Anh cho kết quả ổn định)

Thiết lập chung: tỷ lệ **16:9**, 1080p, **không có chữ trên hình**, không có nhân vật nhận diện được, không logo.

**Cảnh mở đầu (8 giây)**
```
Cinematic slow aerial push-in over a modern Vietnamese vocational college campus in the Central Highlands at early morning,
soft golden light, green hills in the background, red-tiled roofs, calm and professional mood. No text, no logos, no captions,
no identifiable faces. Gentle ambient sound only, no speech. 16:9.
```

**Cảnh chuyển — "kho dữ liệu nền" (8 giây)**
```
Smooth macro shot gliding along neatly organized paper document folders on shelves that gradually transform into glowing
abstract digital folders flowing into a single orderly archive, deep blue and white color palette, clean, trustworthy,
government-office feel. No text, no letters, no numbers, no logos. Soft ambient sound only, no speech. 16:9.
```

**Cảnh kết — "người quyết định" (8 giây)**
```
Close-up over-the-shoulder shot of an office worker's hands reviewing a printed official document with a pen beside a laptop,
warm daylight, shallow depth of field, the worker nods and signs the paper, calm and confident mood. The screen and the paper
are out of focus so no text is readable. No logos, no identifiable face. Soft ambient sound only, no speech. 16:9.
```

Tải 03 tệp về, đặt tên `veo-mo-dau.mp4`, `veo-chuyen.mp4`, `veo-ket.mp4` trong thư mục `Video/veo/`, nhắn em ghép.
Không có 03 cảnh này video vẫn dùng được.

## Nguyên liệu đã có sẵn (dùng cho bất kỳ công cụ dựng video nào)

| Nguyên liệu | Ở đâu |
|---|---|
| Video 1 đã dựng (≈2 phút 40 giây, 08 cảnh, giọng nữ tiếng Việt) | `Video/Video-1_Gioi-thieu-nhanh-03-he_v1.mp4` |
| 08 trang hình 1920×1080 và 08 tệp giọng đọc rời | `Video/_tam/c01…c08.png`, `.mp3` |
| Lời đọc từng cảnh, sửa được rồi dựng lại bằng một lệnh | `Video/lam_video1.py` (danh sách `CANH`) |
| Kịch bản 02 video, câu lệnh từng cảnh quay | `05-KICH-BAN-VIDEO.md` |
| 06 tình huống thực tế | `04c-KQ-Code-6-tinh-huong-trinh-dien.md` |

## 04 đoạn video thao tác (theo ý anh: chỉ quay đoạn đầu, giọng AI, rồi trình diễn kết quả)

Mỗi đoạn 30–45 giây. Anh hoặc đồng chí Công quay màn hình Claude Cowork từ lúc đưa tệp, gõ lệnh đến khi công cụ bắt đầu
làm việc (thấy được công cụ đọc tệp, gọi kỹ năng) rồi dừng. Em cắt, lồng giọng thuyết minh, thêm dòng "Dữ liệu giả định".

| Đoạn | Quay gì | Lời thuyết minh (giọng AI, em lồng) |
|---|---|---|
| T1 — Tổng hợp kế hoạch | Kéo thư mục D1 vào Cowork, gõ lệnh tổng hợp, công cụ bắt đầu kiểm tra hồ sơ từng đơn vị | Người dùng đưa dự thảo kế hoạch quý của sáu đơn vị. Công cụ kiểm tra từng hồ sơ: đúng mẫu chưa, nhiệm vụ nào thiếu thời hạn, thiếu sản phẩm, nhiệm vụ nào trùng nhau, rồi mới tổng hợp thành kế hoạch của cơ quan. |
| T2 — Tra cứu hệ thống quản lý văn bản | Đưa tệp D2 (hoặc công cụ mở trang đã đăng nhập), gõ lệnh đối chiếu | Công cụ lấy danh mục văn bản chỉ đạo, kế hoạch, thông báo kết luận trong kỳ, và chỉ ra nhiệm vụ đã được giao nhưng chưa đơn vị nào đưa vào kế hoạch. Công cụ chỉ đọc, không thao tác trên hệ thống. |
| T3 — Báo cáo tháng | Kéo thư mục D3, gõ lệnh lập báo cáo, công cụ đọc báo cáo đơn vị | Công cụ đọc báo cáo của các đơn vị, phát triển từ báo cáo tháng trước đã ban hành, và ghi nguồn của từng nội dung để kiểm tra lại. |
| T4 — Rà soát văn bản của Đảng | Đưa tệp dự thảo Chương trình công tác (D4, đã ẩn danh), gọi lệnh rà soát, công cụ nhận ra văn bản của Đảng, chọn hệ quy chiếu và đo thể thức | Trước khi trình ký, dự thảo được rà soát bằng hệ rà soát dùng chung của Trường. Công cụ nhận ra đây là văn bản của Đảng, nên áp hướng dẫn về thể thức văn bản của Đảng, không áp quy định của văn bản hành chính. Công cụ đo thể thức trên tệp thật, đối chiếu từng văn bản được viện dẫn, và ghi rõ phần chưa xác minh được. |

Điều kiện để quay: bộ dữ liệu D1–D4 đã có tại `30-Ket-Qua/2026-10-12/De-Mo-17-10/Du-lieu-gia-dinh/`; cần chạy thử trên Cowork trước khi quay.
