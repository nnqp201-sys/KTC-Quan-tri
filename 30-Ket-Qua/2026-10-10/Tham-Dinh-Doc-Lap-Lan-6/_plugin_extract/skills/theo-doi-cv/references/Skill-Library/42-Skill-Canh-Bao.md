# 42-Skill-Canh-Bao
## Phiên bản: v1.0 — 14/9/2026

## Purpose
Tính và phát 8 loại cảnh báo. **Cảnh báo do hệ thống tính, không nhập tay.**

## Tám cảnh báo

| # | Cảnh báo | Điều kiện |
|---|---|---|
| 1 | Sắp đến hạn | Còn ≤ 7 ngày, chưa *Đã hoàn thành* |
| 2 | Quá hạn | Đã qua `Hạn hiện hành`, chưa *Đã hoàn thành* |
| 3 | Chưa bắt đầu | Đã qua 1/3 thời gian, vẫn ở *Mới* hoặc *Đã giao* |
| 4 | Không cập nhật | Quá 30 ngày không có lần cập nhật nào |
| 5 | Tiến độ thấp | `% hoàn thành` < `% thời gian đã trôi`, chênh ≥ 30 điểm |
| 6 | Thiếu sản phẩm | *Chờ kết quả* quá 15 ngày mà chưa có sản phẩm |
| 7 | Thiếu minh chứng | Tự khai hoàn thành nhưng bảng Minh chứng không có dòng nào |
| 8 | Nguy cơ không hoàn thành | Còn ≤ 1/4 thời gian mà `% hoàn thành` < 50 |

## Ba quy tắc phát cảnh báo

1. **Không dồn cuối kỳ.** Quét theo lịch cố định; dồn đến lúc chốt kỳ thì cảnh báo mất tác dụng phòng ngừa.
2. **Gửi đúng người.** Cảnh báo 1–5 gửi đơn vị chủ trì; 6–8 gửi kèm lãnh đạo phụ trách.
3. **Cảnh báo là dữ kiện, không phải đánh giá.** Ghi *"quá hạn 12 ngày, `% hoàn thành` = 40"*, không ghi
   *"đơn vị chậm trễ"*.

## Chống nhiễu — bài học đã trả giá

Cảnh báo giả lặp lại làm người nhận bỏ qua **cả cảnh báo thật**. Đã xảy ra ở hệ Báo cáo: ghi chú hợp lệ
*"Kết luận giao ban"* bị báo là lỗi (BUG-07), lâu dần không ai đọc cảnh báo nữa.

Vì vậy: trước khi thêm một điều kiện cảnh báo mới, phải thử trên dữ liệu thật và đo **tỷ lệ báo nhầm**.
Điều kiện nào báo nhầm > 20% thì không đưa vào.

## Không tự xử lý thay
Cảnh báo **không** kéo theo tự động lùi hạn, tự đóng hay tự chuyển kỳ. Mọi thay đổi baseline đi qua
Skill 44 và phải có phê duyệt.

## Related
- `41-Skill-Cap-Nhat-Tien-Do.md` · `44-Skill-Dieu-Chinh-Va-Ban-Giao.md`
