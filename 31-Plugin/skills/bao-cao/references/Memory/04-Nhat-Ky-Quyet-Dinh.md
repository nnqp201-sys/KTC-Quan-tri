# NHẬT KÝ QUYẾT ĐỊNH KTC-RIS

Ghi **vì sao** hệ được làm như hiện tại. Đọc trước khi định thay đổi thiết kế —
một quyết định trông có vẻ tùy tiện thường có lý do đã trả giá để biết.

Mỗi mục: bối cảnh → quyết định → **lý do** → hệ quả kèm theo.

---

## QĐ-01 — Không bao giờ tự bịa nội dung còn thiếu
**Ngày:** trước 14/08/2026 · **Trạng thái:** đang áp dụng

- **Bối cảnh:** Nhiều mục trong mẫu TB736 không có dữ liệu từ Phụ lục đơn vị.
- **Quyết định:** Để nguyên và đánh dấu `[CẦN BỔ SUNG: ...]` in nghiêng màu xám. Tuyệt đối không suy diễn nội dung.
- **Lý do:** Đây là báo cáo trình UBND tỉnh và Hiệu trưởng ký. Một câu bịa trôi chảy nguy hiểm hơn
  một chỗ trống nhìn thấy được — người ký sẽ không biết mà rà.
- **Hệ quả:** Báo cáo trông "thiếu" nhiều chỗ. Đây là **có chủ đích**, không phải khuyết điểm cần che.

## QĐ-02 — Chủ ngữ báo cáo cấp Trường luôn là "Nhà trường"
**Ngày:** trước 14/08/2026 · **Trạng thái:** đang áp dụng

- **Quyết định:** Toàn văn báo cáo cấp Trường dùng "Nhà trường", kể cả khi việc do một Phòng/Khoa cụ thể làm.
- **Lý do:** Báo cáo cấp Trường là tiếng nói của pháp nhân Trường trước UBND tỉnh, không phải bản
  ghép các báo cáo đơn vị. Dùng tên Phòng/Khoa làm chủ ngữ làm sai cấp độ văn bản.
- **Hệ quả:** Khi tổng hợp phải biên tập lại văn phong, không chép nguyên văn từ đơn vị.

## QĐ-03 — Không tự sửa số liệu KPI dù biết chắc sai
**Ngày:** trước 17/08/2026 · **Trạng thái:** đang áp dụng

- **Quyết định:** Phát hiện sai công thức → ghi cảnh báo nêu giá trị đúng, để **đơn vị tự sửa**.
- **Lý do:** Số liệu KPI gắn với đánh giá viên chức. Hệ sửa hộ là tước mất trách nhiệm giải trình
  của đơn vị, và nếu hệ sửa sai thì không ai chịu trách nhiệm.
- **Hệ quả:** `read_bc736_excel.py` chỉ cảnh báo, không bao giờ ghi đè.

## QĐ-04 — Ưu tiên khớp tuyệt đối khi điền nội dung vào mẫu Word
**Ngày:** 19/08/2026 · **Trạng thái:** đang áp dụng (v2.5.1)

- **Bối cảnh:** BUG-10 — khóa "Công tác đào tạo" chiếm chỗ của "Công tác đào tạo nghề cho lao động nông thôn".
- **Quyết định:** Khớp tuyệt đối trước; nếu buộc phải khớp gần đúng thì chọn khóa **dài nhất** và **cảnh báo**.
- **Lý do:** Khớp chuỗi con lấy kết quả đầu tiên phụ thuộc thứ tự dict — kết quả *không ổn định*
  và sai một cách im lặng. Đây là loại lỗi tệ nhất: báo cáo trông bình thường nhưng nội dung sai chỗ.
- **Hệ quả:** Tên khóa trong `content_map` nên đặt trùng khớp với mẫu; hệ sẽ báo `unused_keys` nếu gõ sai.

## QĐ-05 — Gộp v2.5.1 và v3.0 thành v3.1, giữ nguyên logic Mục II của v3.0
**Ngày:** 19/08/2026 · **Trạng thái:** ⏸ **chờ người dùng đồng ý**

- **Bối cảnh:** Kiểm thử đối chứng cho thấy hai bản bù trừ nhau: v2.5.1 vá 14 lỗi nhưng còn
  BUG-15 (Mục II) và BUG-16 (lẫn Phần I/III); v3.0 vá đúng 2 lỗi đó nhưng giữ nguyên 13 lỗi cũ.
- **Quyết định:** Gộp, và khi gộp thì **bê nguyên logic Mục II của v3.0**, không viết lại theo ý mình.
- **Lý do:** Chú thích trong mã v3.0 ghi *"xác nhận từ file thật 18/08/2026"* — phần đó đã được đối chiếu
  với dữ liệu thật, trong khi bản vá v2.5.1 mới chỉ chạy trên fixture mô phỏng. Dữ liệu thật thắng suy luận.
- **Chưa làm:** Chờ ý kiến người dùng.

## QĐ-06 — Lập lớp bộ nhớ quá trình riêng (`references/Memory/`)
**Ngày:** 19/08/2026 · **Trạng thái:** đang áp dụng

- **Bối cảnh:** Hệ nhớ được *cách làm* (Skill-Library) và *dữ liệu* (Drive), nhưng không nhớ
  *đã làm gì, vì sao, gặp gì*. Mỗi phiên bắt đầu lại từ số không.
- **Quyết định:** Tách riêng lớp Memory, theo mô hình phân tầng của Anthropic — SKILL.md chỉ trỏ đường,
  nội dung nằm ở file tham chiếu, chỉ nạp khi cần.
- **Lý do:** Nhồi hết vào SKILL.md sẽ vượt ngưỡng khuyến nghị 500 dòng và làm loãng phần hướng dẫn chính.
  Tách file cho phép đọc đúng cái cần: đầu phiên đọc `TRANG-THAI.md`, gặp lỗi mới mở `02-So-Dang-Ky-Loi.md`.
- **Hệ quả:** Phát sinh nghĩa vụ **ghi nhật ký cuối mỗi kỳ**. Bộ nhớ không được cập nhật sẽ tệ hơn
  không có bộ nhớ, vì tạo cảm giác an tâm giả.

---

## Cách ghi quyết định mới

Cấp mã tiếp theo (QĐ-07...). Bắt buộc có mục **Lý do** — quyết định không lý do sẽ bị phá bỏ.
Khi một quyết định bị thay thế: **giữ lại**, đổi trạng thái thành "đã thay bằng QĐ-xx" kèm lý do thay đổi.
Xóa quyết định cũ là xóa mất bài học.
