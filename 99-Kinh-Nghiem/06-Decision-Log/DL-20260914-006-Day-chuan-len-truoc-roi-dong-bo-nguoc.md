# DL-20260914-006 — Khi một hệ lệch chuẩn vì nó **mới hơn** chuẩn: đẩy lên trước, đồng bộ sau

**Ngày:** 14/9/2026 · **Trạng thái:** ✅ **ĐÃ THỰC HIỆN** · **Tiếp nối:** `DL-20260914-002`, `CP-20260914-001`

## Câu hỏi

Soi vào trong 6 tệp `.skill`: 5 hệ khớp `01-Chuan-Chung/`, riêng `ktc-ra-soat-897` lệch 4 tệp dùng chung.
Đồng bộ nó về chuẩn là xong — nhưng có đúng không?

## Trả lời ngắn

**Không.** Kiểm tra từng dòng cho thấy hệ 897 lệch vì nó **giữ nội dung mới hơn và đúng hơn** bản chuẩn.
Đồng bộ mù theo chiều "chuẩn → hệ" sẽ **xoá mất quy tắc thật** và còn khôi phục lại một mô tả **sai** trong
bản chuẩn. Thứ tự đúng là: **đẩy phần mới lên chuẩn gốc trước, rồi mới phân phối ngược xuống mọi hệ.**

Điển hình: bản chuẩn cũ ghi *"công cụ Google Drive chỉ đọc và tạo file mới — không sửa, đổi tên, di chuyển
hoặc xoá được"*. Bản của hệ 897 đã đính chính ngày 08/9/2026 **bằng lệnh gọi thật**: có `copy_file`,
`update_file`, `trash_file`; giới hạn thật là **không ghi đè được nội dung tệp đã có**, và đó là giới hạn
kỹ thuật chứ không phải phân quyền. Nếu đồng bộ mù, 5 hệ kia tiếp tục dùng mô tả sai.

## Đã làm

| Bước | Kết quả |
|---|---|
| Sao lưu 4 tệp chuẩn cũ | `99-Luu-Tru/01-Chuan-Chung-truoc-20260914/` |
| Đẩy lên `01-Chuan-Chung` | Bài học connector 08/9 · `phapluat.gov.vn` là nguồn Mức 1 ưu tiên cao nhất · bản VBHN đầy đủ hơn · câu quy tắc kho viết lại cho trung tính |
| Phân phối xuống 6 hệ | Bản rời **và** trong gói `.skill` — md5 còn 0 chỗ lệch |
| Phát hiện thêm | `ktc-bao-cao` thiếu 7 tệp, `ktc-ke-hoach` thiếu 5 tệp so với nguồn rời — trong đó **cả hai đều thiếu `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` và trigger tự kích hoạt của nó**, tức quy tắc viện dẫn văn bản hợp nhất đang **chết** trong hai hệ |
| Sửa liên kết gãy | `38-Skill-Tu-hoc-Ke-Hoach.md` trỏ bằng đường dẫn tương đối vào 5 tệp của skill độc lập `ktc-tu-hoc-ke-hoach` → viết lại thành tham chiếu theo tên skill, kèm lưu ý phải nạp cả hai |
| Sửa số phiên bản | Gói `v3.6` mang `SKILL.md` ghi `v3.5`; gói `v3.2` mang `SKILL.md` ghi `3.1` — vi phạm bước xác minh số 3. Nay cả 6 hệ **số trong SKILL.md khớp tên tệp gói** |

## Bài học ghi lại

1. **Lệch chuẩn không đồng nghĩa với sai.** Trước khi đồng bộ, phải xác định **chiều nào mới hơn** —
   đối chiếu nội dung, không so ngày sửa tệp hay dung lượng.
2. **Bản địa hoá không nên viết đè lên tệp dùng chung.** Nếu một câu chỉ đúng cho một hệ, hãy viết lại
   cho đúng với **mọi** hệ, hoặc tách thành tệp riêng của hệ đó. Cả 4 chỗ bản địa hoá của hệ 897 đều
   diễn đạt lại được thành câu trung tính — không mất gì.
3. **Tệp có trong `references/` rời mà không có trong gói là lỗi, không phải lựa chọn** — trừ
   `desktop.ini`, bản trùng `(1)`, và gói `.skill` lồng nhau.
