# 43-Skill-Minh-Chung
## Phiên bản: v1.0 — 14/9/2026

## Purpose
Thu nhận, phân loại và xác minh minh chứng — điều kiện để nhiệm vụ được công nhận *Đã hoàn thành*.

## Vì sao bắt buộc

Nguyên tắc bất biến 3: **báo cáo phải truy ngược được** tới nhiệm vụ → kế hoạch → đơn vị → kết quả →
minh chứng. Không có minh chứng thì kết quả không vào được báo cáo, dù đơn vị đã khai hoàn thành.

## Mỗi minh chứng ghi đủ 10 trường

`Mã minh chứng` · `Mã nhiệm vụ` · `Loại minh chứng` · `Mô tả` · `Ngày phát sinh` · `Liên kết Drive` ·
`Tình trạng xác minh` · `Người xác minh` · `Ngày xác minh` · `Ghi chú`.

**Ưu tiên ghi Drive File ID hơn tên tệp.** Tên tệp đổi được, ID thì không — truy vấn theo `parentId`
đáng tin hơn theo tên.

## Ba tình trạng xác minh

| Tình trạng | Nghĩa | Dùng được cho báo cáo? |
|---|---|---|
| Chưa xác minh | Đơn vị vừa nộp | **Không** |
| Đã xác minh | Người có thẩm quyền đã mở tệp và xác nhận đúng nội dung | Có |
| Không hợp lệ | Tệp hỏng, sai nội dung, hoặc không liên quan nhiệm vụ | Không — yêu cầu nộp lại |

> **"Có liên kết" không đồng nghĩa "đã xác minh".** Phải thực sự mở tệp ra xem. Đây là chỗ dễ làm hình
> thức nhất của cả hệ.

## Loại minh chứng thường gặp
Văn bản đã ban hành (ưu tiên cao nhất — có số, có ngày) · biên bản · hình ảnh sự kiện · báo cáo của đơn
vị · tệp dữ liệu · liên kết bài đăng.

## Không suy diễn
Nhiệm vụ không tìm thấy minh chứng **không đồng nghĩa chưa làm**. Đã có tiền lệ: nhiệm vụ 2.8 hoàn thành
thật bằng QĐ 1923/QĐ-CĐKT ngày 30/8/2026 nhưng không xuất hiện trong báo cáo đơn vị. Ghi là **nghi ngờ**,
để đơn vị xác nhận — không kết luận thay.

## Related
- `41-Skill-Cap-Nhat-Tien-Do.md` — ngưỡng chuyển *Đã hoàn thành*
- `44-Skill-Dieu-Chinh-Va-Ban-Giao.md` — bàn giao cho báo cáo
