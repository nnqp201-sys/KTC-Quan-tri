# LỆNH CẬP NHẬT TỰ ĐỘNG — GỬI PHIÊN CLAUDE CỦA CHỦ TEAM MỚI
## Hệ KTC-Ra-Soat-897-v2-Cai-tien — Bàn giao 07-08/9/2026

> **Dùng lệnh này khi nào**: dán nguyên văn lệnh này vào đầu phiên làm việc đầu tiên sau khi chủ Team mới tiếp nhận quyền quản lý hệ thống (hoặc cài Skill lần đầu). Mục tiêu: giúp Claude tự nạp đủ ngữ cảnh bàn giao mà không cần người dùng phải kể lại từ đầu.

---

## BƯỚC 1 — ĐỌC ĐỦ 3 TÀI LIỆU SAU, ĐÚNG THỨ TỰ, TRƯỚC KHI LÀM BẤT KỲ VIỆC GÌ

1. **`Ho-So-Ban-Giao-KTC-Ra-Soat-897-v2.docx`** (gốc thư mục dự án) — hồ sơ bàn giao chính thức, 7 trang: tổng quan hệ thống, trạng thái đã xác nhận trực tiếp, 6 bài học kinh nghiệm, cách vận hành, việc còn mở, định hướng v3.0, đầu mối liên hệ.
2. **`09-Quan-Tri-He/01-Huong-Dan-Chuyen-Giao-He-Thong.md`** — hồ sơ tri thức kỹ thuật đầy đủ hơn (7 mục: kiến trúc, ma trận 4 hệ quy chiếu, bản đồ bộ nhớ, giới hạn công cụ, quy tắc phân loại lỗi, nhật ký sự cố/anti-pattern, hướng dẫn bảo trì). Có phân loại rõ `[FACT]/[INFERENCE]/[PROPOSAL]/[UNKNOWN]` — **tin `[FACT]`, thận trọng với `[UNKNOWN]`, không tự suy diễn thêm**.
3. **`09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md`** — điểm nạp kỹ thuật chi tiết nhất, đọc sau 2 file trên để đối chiếu không có gì lệch.

**Không được tóm tắt qua loa rồi bỏ qua bước này** — 2 tài liệu đầu chứa toàn bộ bài học đã trả giá bằng thời gian thật (gần 1 tháng), bỏ qua sẽ lặp lại đúng những lỗi đã từng xảy ra.

---

## BƯỚC 2 — XÁC NHẬN LẠI TRẠNG THÁI THẬT TRÊN DRIVE (không tin bảng dưới đây, tự kiểm tra)

| Hạng mục | Trạng thái tại thời điểm bàn giao (07/9/2026) |
|---|---|
| `.skill` đang phân phối | `ktc-ra-soat-897-v2.21.skill` — 264.092 bytes |
| Script chính | `build_ktc897_report.py` v3.4 |
| `SKILL.md` rời, `00-README.md`, Nhật ký, `CHANGELOG.md` | Đã đồng bộ v2.21 / v1.7 — vừa vá xong 1 CONFLICT hai chiều + 1 đoạn hỏng ký tự trong `00-README.md` |
| `Mau_Bao_cao_ra_soat_KTC897_8phan.docx` | Đã khôi phục (từng bị mất hoàn toàn khỏi Drive) và sửa đúng tên file (bản upload đầu tiên bị dính nhầm tên "Tôi đang chia sẻ..." của thông báo Drive) |
| `11-Tong-Hop-Nguoi-Dung-KTC897.md` | Đã vá 1 lỗi hỏng ký tự giống hệt lỗi trong `00-README.md` |
| Quyền sở hữu 2 thư mục gốc + file `.skill` chính | Đã chuyển đủ sang `phongthhcqt@gmail.com` — **xác nhận lại xem đã chuyển tiếp sang tài khoản chủ Team mới chưa**, vì bàn giao lần này có thể kèm đổi chủ sở hữu lần nữa |

**Việc bắt buộc**: dùng công cụ Drive kiểm tra trực tiếp `owner`, `modifiedTime`, `fileSize` của tối thiểu 4 file trên — không suy diễn từ bảng này, bảng chỉ là điểm khởi đầu để biết cần kiểm tra gì.

---

## BƯỚC 3 — TÓM TẮT NHỮNG GÌ ĐÃ TRAO ĐỔI VÀ XỬ LÝ TRONG BUỔI BÀN GIAO (chiều 07/9 → sáng 08/9/2026)

Để chủ Team mới không cần hỏi lại "hôm qua đã làm gì":

1. Xác nhận hệ chính thức đang chạy là **v2.21**, ổn định, đã qua kiểm định (bộ hồi quy 30 lỗi, tỷ lệ đúng hoàn toàn 40%, tăng từ baseline 28,6%).
2. Phát hiện và vá dứt điểm 1 CONFLICT "phân kỳ hai chiều" giữa `SKILL.md` đóng gói và bản rời (ghi thành quy tắc 19 trong chính `SKILL.md`, để không lặp lại mù quáng).
3. Phát hiện và vá 2 đoạn văn bị hỏng ký tự thật (mojibake) ở 2 file độc lập (`00-README.md`, `11-Tong-Hop-Nguoi-Dung-KTC897.md`) — đã quét toàn Drive để xác nhận không còn sót thêm.
4. Phát hiện file mẫu gốc `Mau_Bao_cao_ra_soat_KTC897_8phan.docx` từng **bị mất hoàn toàn** khỏi Drive — đã khôi phục, đồng thời sửa lỗi khổ giấy (bảng tràn khổ) và lỗi chính tả ("Biên bản" → "Phiên bản").
5. Bổ sung `CHANGELOG.md` (từng thiếu hẳn các mục v2.19–v2.21).
6. Soạn và xác minh xong 2 tài liệu bàn giao chính thức (xem Bước 1) — cả hai đều đã qua `validate.py` (schema OOXML sạch) và render kiểm tra bằng mắt trước khi giao.
7. Xác nhận rõ: nhánh phát triển **"v3.0"** (thư mục `core/`, skill con `review`/`compare`/`normalize`/`quick-review`) là **định hướng phát triển chính thức** của Phòng TH-HC&QT, **không phải rác kỹ thuật** — nhưng **tạm hoãn có chủ đích** để ưu tiên chạy thực chiến ổn định v2.21 trước.
8. Đã từ chối đưa một số chi tiết kỹ thuật không có căn cứ thật (ví dụ tên mô hình AI, thông số kỹ thuật lạ không khớp hệ sinh thái Claude) vào tài liệu chính thức khi được yêu cầu — giữ đúng nguyên tắc không bịa đặt, đánh dấu rõ là chưa đủ căn cứ thay vì viết như sự thật.

---

## BƯỚC 4 — VIỆC CÒN MỞ, ƯU TIÊN XỬ LÝ NGAY SAU KHI TIẾP QUẢN

| # | Việc | Mức ưu tiên |
|---|---|---|
| 1 | Skill 30 (văn bản quy phạm pháp luật) được `SKILL.md` nhắc tới 2 lần nhưng **không tồn tại file thật** trên Drive — viết nội dung thật hoặc gỡ tham chiếu | **Cao** |
| 2 | Chạy lại bộ hồi quy 30 lỗi sau khi có Checklist 09 (Hệ D đoàn thể, mới v2.21) để đo cải thiện thật | Trung bình |
| 3 | Hệ D — Đoàn Thanh niên và Hội Sinh viên mới chỉ có mẫu nội bộ Trường, chưa có nguồn cấp Trung ương như Công đoàn (đã có QĐ 933/QĐ-TLĐ) | Trung bình |
| 4 | Xác nhận lại quyền sở hữu toàn bộ file sau khi chuyển giao cho chủ Team mới — lưu ý: chuyển quyền thư mục KHÔNG tự động chuyển quyền các file được tạo/tải lên sau đó bởi tài khoản khác (đã xảy ra thật, xem Mục 6 tài liệu tri thức) | Cao |
| 5 | Cân nhắc thời điểm nối lại kế hoạch v3.0 theo đúng gợi ý đã ghi trong hồ sơ bàn giao (làm rõ mức hoàn thiện `core/`, áp dụng SSOT phiên bản ngay từ đầu, dùng bộ hồi quy v2 làm chuẩn kiểm chéo) | Khi Phòng TH-HC&QT quyết định |

---

## BƯỚC 5 — 3 QUY TẮC VẬN HÀNH BẮT BUỘC ÁP DỤNG NGAY, KHÔNG ĐỢI NHẮC LẠI

1. **Không tin lời xác nhận "đã sửa/đã cập nhật"** — luôn đọc lại trực tiếp file thật trên Drive trước khi kết luận.
2. **Sau mỗi lần sửa `SKILL.md`/script/checklist**: phải chạy `validate.py`, đóng gói lại `.skill`, cài đè vào Claude.ai, rồi xác nhận lại bằng cách hỏi Claude phiên bản đang chạy — không dừng ở bước sửa trên Drive.
3. **Không tự tái tạo nội dung file lớn (>15.000 ký tự mã hóa) qua lệnh gọi công cụ trong chat** — dùng thao tác server-side (`copy_file`, `download_file_content`) hoặc đưa file cho người dùng tự tải lên/xuống trực tiếp.

---

## XÁC NHẬN YÊU CẦU

Sau khi đọc xong Bước 1–5, phiên Claude mới cần phản hồi lại đúng theo cấu trúc: (a) xác nhận đã đọc đủ 3 tài liệu, (b) báo cáo kết quả kiểm tra thật ở Bước 2 (khớp/lệch cụ thể ở đâu so với bảng), (c) hỏi chủ Team mới muốn ưu tiên xử lý việc nào trong Bước 4 trước — không tự ý bắt tay làm ngay khi chưa xác nhận ưu tiên.