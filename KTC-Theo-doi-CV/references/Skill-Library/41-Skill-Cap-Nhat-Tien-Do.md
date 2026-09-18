# 41-Skill-Cap-Nhat-Tien-Do
## Phiên bản: v1.0 — 14/9/2026

## Purpose
Ghi nhận tiến độ và chuyển trạng thái **đúng chiều**, không nhảy cóc, không lùi im lặng.

## Quy tắc chuyển trạng thái

```
Mới → Đã giao → Đang thực hiện → Chờ kết quả → Đã hoàn thành → Đã kiểm tra → Đã báo cáo
```

| Quy tắc | Nội dung |
|---|---|
| Không nhảy cóc | Từ *Đã giao* không nhảy thẳng sang *Đã hoàn thành*. Thiếu bước giữa → cảnh báo, hỏi lại |
| Lùi trạng thái phải có lý do | Ghi rõ lý do và người quyết định vào bảng Cập nhật tiến độ |
| Trạng thái phụ không thay trạng thái chính | *Tạm dừng*, *Điều chỉnh*, *Chuyển kỳ*, *Hủy*, *Quá hạn* là nhánh rẽ, ghi song song |
| `% hoàn thành` chỉ tăng | Giảm phải có lý do — thường là do phát hiện khai khống kỳ trước |

## Ba ngưỡng suy ra trạng thái

| Điều kiện | Trạng thái |
|---|---|
| Có ≥ 1 lần cập nhật tiến độ | *Đang thực hiện* |
| `% hoàn thành` ≥ 90 nhưng chưa có sản phẩm | *Chờ kết quả* |
| Có sản phẩm **và** có minh chứng đã xác minh | *Đã hoàn thành* |

> **Chốt chặn:** có sản phẩm mà **chưa có minh chứng** thì giữ ở *Chờ kết quả*. Không nới.

## Mỗi lần cập nhật phải ghi đủ

`Mã cập nhật` · `Mã nhiệm vụ` · `Ngày cập nhật` · `Trạng thái` · `% hoàn thành` ·
`Kết quả đã thực hiện` · `Khó khăn/vướng mắc` · `Hành động tiếp theo` · `Người cập nhật`.

Hai cột tùy chọn: `Đề xuất hạn mới` (nếu có → tự sinh một đề nghị điều chỉnh, Skill 44) và
`Liên kết minh chứng`.

## Không tự sửa số liệu đơn vị

Phát hiện `% hoàn thành` mâu thuẫn với `Kết quả đã thực hiện` → **ghi cảnh báo, nêu giá trị nghi đúng**,
để đơn vị tự sửa. Hệ sửa hộ là tước mất trách nhiệm giải trình của đơn vị.

## Related
- `42-Skill-Canh-Bao.md` · `43-Skill-Minh-Chung.md`
- `01-Chuan-Chung/12-Vong-Doi-Trang-Thai.md` — bản gốc định nghĩa 12 trạng thái
