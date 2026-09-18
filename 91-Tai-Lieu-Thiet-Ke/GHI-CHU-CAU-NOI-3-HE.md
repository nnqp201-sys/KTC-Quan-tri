# Ghi chú kiểm chứng cầu nối KTC-Theo-dõi-CV ↔ KTC-Bao-Cao
## Thực hiện 19/08/2026 — bước 1 trong lộ trình hướng tới hợp nhất 3 hệ

## Mục đích
Kiểm chứng xem 2 khóa liên kết đã thiết kế sẵn (`Mã nhiệm vụ`, `Trục TB817`) có thực sự
đủ để đối chiếu dữ liệu giữa KTC-Theo-dõi-CV và KTC-Bao-Cao hay không — TRƯỚC KHI bàn
hợp nhất vật lý 2 hệ.

## Lưu ý quan trọng: dữ liệu dùng kiểm thử
Sheet "01. Bộ dữ liệu vận hành KTC-Theo-dõi-CV" hiện **đang rỗng** (Trạng thái: Thiết kế,
Tổng nhiệm vụ = 0). Script `bridge_theo_doi_cv.py` được kiểm thử bằng **dữ liệu mẫu tự tạo**,
đúng 19 cột thật của bảng "Nhiệm vụ" — không phải dữ liệu vận hành thật. Khi hệ Theo-dõi-CV
có dữ liệu thật, chỉ cần thay nguồn đọc (từ Google Sheet thay vì list Python), toàn bộ logic
xử lý giữ nguyên.

## 3 phát hiện chính

### ✅ 1. Tổng hợp tiến độ theo Trục — HOẠT ĐỘNG ĐÚNG
Hàm `summarize_tien_do_theo_truc()` gom đúng theo 6 Trục, tính đúng % trung bình, đếm đúng
trạng thái (Hoàn thành/Đang thực hiện/Chậm tiến độ) và mức rủi ro cao — cho ra bảng tương tự
định dạng bảng `%KPI theo Trục` mà Skill 33 của KTC-Bao-Cao đang xuất ra. **Định dạng đầu ra
tương thích tốt, có thể ghép trực tiếp vào báo cáo Skill 34 (đối chiếu tiến độ) trong tương lai.**

Đồng thời hàm tự phát hiện đúng 1 dòng có `Trục TB817` không hợp lệ (test cố tình đưa "Trục 7X")
— không tự suy diễn Trục nào, chỉ cảnh báo.

### ✅ 2. Tên Đơn vị chủ trì — TƯƠNG THÍCH 100% (trên dữ liệu mẫu)
So khớp `Đơn vị chủ trì` giữa nhiệm vụ mẫu (Theo-dõi-CV) và danh sách đơn vị thật đã dùng
trong Excel Phụ lục TB736 (Phòng QLĐT&BĐCL, QLKHCN&HTPT, TC-KT...) — khớp hoàn toàn 100%.
**Đây là tín hiệu tốt**: nếu dữ liệu thật cũng viết tên đơn vị nhất quán như vậy, việc đối
chiếu chéo giữa 2 hệ theo Đơn vị + Trục là khả thi ngay, không cần bảng ánh xạ riêng.
*(Lưu ý: đây mới là kiểm thử trên dữ liệu mẫu do em tự đặt tên — cần xác nhận lại khi có
dữ liệu thật, vì người nhập liệu thực tế có thể viết tên đơn vị không nhất quán.)*

### ⚠️ 3. Đối chiếu CHÍNH XÁC theo Mã nhiệm vụ — CHƯA LÀM ĐƯỢC (lỗ hổng thật)
**Đây là phát hiện quan trọng nhất.** Phụ lục TB736 (Ia/Ib/IIb/IIc) mà KTC-Bao-Cao đang dùng
**không có cột `Mã nhiệm vụ`** — trong khi đây chính là khóa nối chính mà KTC-Theo-dõi-CV
dùng làm trung tâm thiết kế. Hậu quả: hiện tại chỉ đối chiếu được ở mức **gần đúng** (theo
Trục + so khớp tên nhiệm vụ bằng mắt), **không thể tự động đối chiếu 1-1 chính xác**.

## Khuyến nghị cụ thể

1. **Bổ sung cột `Mã nhiệm vụ` vào Phụ lục Ia/Ib (kế hoạch) của TB736** — đây là việc nhỏ
   nhưng có giá trị đòn bẩy cao: chỉ cần thêm 1 cột, toàn bộ 3 hệ sẽ đối chiếu được chính xác
   qua đúng 1 khóa duy nhất, không cần thay đổi gì lớn ở KTC-Bao-Cao hay KTC-Theo-dõi-CV.
2. Việc này nên do **KTC-Ke-Hoach** đảm nhiệm (vì đó là hệ sinh ra `Mã nhiệm vụ` gốc theo đúng
   quy tắc đã định trong Nhật ký liên thông: "Nhiệm vụ/baseline — Hệ nguồn chuẩn: KTC-Ke-Hoach").
3. Sau khi có cột này, `read_bc736_excel.py` (KTC-Bao-Cao) nên đọc thêm cột `Mã nhiệm vụ` và
   dùng nó làm khóa nối thay vì chỉ dựa vào Trục + tên — lúc đó việc đối chiếu tiến độ (Skill 34)
   sẽ chính xác tuyệt đối, không còn phụ thuộc so khớp text gần đúng.

## Kết luận cho câu hỏi "có nên hợp nhất 3 hệ không"
Kết quả kiểm chứng củng cố khuyến nghị đã đưa ra trước đó: **kiến trúc liên kết lỏng hiện tại
là khả thi về mặt kỹ thuật**, chỉ cần 1 điều chỉnh nhỏ (thêm cột Mã nhiệm vụ vào Phụ lục
Ia/Ib) là có thể đối chiếu chính xác giữa các hệ — không cần hợp nhất vật lý ngay.
