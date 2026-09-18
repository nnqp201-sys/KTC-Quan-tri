# 44-Skill-Dieu-Chinh-Va-Ban-Giao
## Phiên bản: v1.0 — 14/9/2026

## Purpose
Hai việc cùng một nguyên tắc *"mọi thay đổi phải có lịch sử"*: xử lý đề nghị điều chỉnh baseline, và bàn
giao dữ liệu đã xác nhận cho `ktc-bao-cao`.

---

## A. Đề nghị điều chỉnh baseline

### Ghi đủ 14 trường
`Mã đề nghị` · `Mã nhiệm vụ` · `Loại thay đổi` · `Nội dung baseline` · `Nội dung đề nghị` · `Lý do` ·
`Nguồn/căn cứ` · `Ngày đề nghị` · `Người đề nghị` · `Trạng thái phê duyệt` · `Cấp/người phê duyệt` ·
`Ngày quyết định` · `Số VB/quyết định` · `Ghi chú`.

Thiếu `Lý do` hoặc `Nguồn/căn cứ` → **không tiếp nhận**. Một đề nghị không có căn cứ sẽ bị người sau phá
bỏ vì tưởng là tùy tiện.

### Ba loại thay đổi
| Loại | Ảnh hưởng |
|---|---|
| Đổi thời hạn | `Hạn hiện hành` đổi, `Hạn baseline` **giữ nguyên** |
| Đổi nội dung/sản phẩm | Phải hỏi `ktc-ke-hoach` — có thể là nhiệm vụ khác chứ không phải điều chỉnh |
| Đổi đơn vị chủ trì | Ghi cả đơn vị cũ; lịch sử tiến độ của đơn vị cũ **giữ nguyên**, không xóa |

### Chỉ áp dụng sau khi có phê duyệt
Trạng thái *Chờ duyệt* thì baseline **chưa đổi**. Áp trước khi duyệt là làm sai lệch số liệu trượt tiến độ.

---

## B. Bàn giao cho `ktc-bao-cao`

### Điều kiện bàn giao — nhiệm vụ phải đạt cả ba
1. Trạng thái là *Đã hoàn thành* hoặc *Đã kiểm tra*;
2. Có ít nhất một minh chứng **Đã xác minh**;
3. Có `Task_ID` khớp với kế hoạch kỳ tương ứng.

Nhiệm vụ không đạt vẫn bàn giao — nhưng **xếp riêng** vào nhóm *chưa hoàn thành/chuyển kỳ*, kèm lý do.
Giấu đi là làm báo cáo sai.

### Gói bàn giao gồm
| Thành phần | Nội dung |
|---|---|
| Danh sách nhiệm vụ đã xác nhận | Task_ID · Trục · tên · đơn vị · sản phẩm · minh chứng |
| Danh sách chưa hoàn thành | kèm `% hoàn thành`, lý do, đề nghị chuyển kỳ |
| Bảng trượt tiến độ | `Hạn baseline` ↔ `Hạn hiện hành`, số lần điều chỉnh |
| Ghi chú độ tin cậy | dữ liệu thật hay dữ liệu mẫu — **bắt buộc** |

### Nói rõ giới hạn đối chiếu
Chừng nào Phụ lục Ia/Ib chưa có cột `Mã nhiệm vụ` (`KI-001`), đối chiếu giữa hệ này và `ktc-bao-cao` chỉ
là **gần đúng theo Trục + tên nhiệm vụ**. Đã đo được: khớp theo tên sinh khớp giả ở ngưỡng 63–80% vì văn
bản hành chính dùng khuôn chữ lặp. **Không dùng ngưỡng dưới 100% cho kết luận tự động.**

## Related
- `01-Chuan-Chung/12-Vong-Doi-Trang-Thai.md` · `43-Skill-Minh-Chung.md`
