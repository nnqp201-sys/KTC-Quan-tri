# Vòng đời và trạng thái nhiệm vụ — KTC-Quan-tri

**Trạng thái:** Dự thảo để chốt · **Lập ngày:** 13/9/2026 · **Nguồn:** mục V Kế hoạch hợp nhất

## Bảy trạng thái chính — đi theo một chiều

```
Mới → Đã giao → Đang thực hiện → Chờ kết quả → Đã hoàn thành → Đã kiểm tra → Đã báo cáo
```

| Trạng thái | Ý nghĩa | Điều kiện chuyển sang trạng thái này |
|---|---|---|
| Mới | Đã có Task_ID, chưa phân công | Kế hoạch đã cấp mã |
| Đã giao | Đã xác định đơn vị chủ trì và thời hạn | Có chủ trì + có hạn |
| Đang thực hiện | Đơn vị đã bắt đầu | Có ít nhất 1 lần cập nhật tiến độ |
| Chờ kết quả | Đã làm xong phần việc, đang chờ sản phẩm/xác nhận | % tiến độ ≥ 90 nhưng chưa có sản phẩm |
| Đã hoàn thành | Có sản phẩm đúng yêu cầu | Có sản phẩm **và** có minh chứng |
| Đã kiểm tra | Đã đối chiếu sản phẩm với yêu cầu trong kế hoạch | Người kiểm tra xác nhận |
| Đã báo cáo | Đã đưa vào một kỳ báo cáo cụ thể | Có mã kỳ báo cáo |

**"Đã hoàn thành" bắt buộc có minh chứng.** Nhiệm vụ tự khai hoàn thành nhưng không có minh chứng thì
giữ ở "Chờ kết quả" — đây là chốt chặn để báo cáo truy ngược được.

## Năm trạng thái phụ — rẽ nhánh, không nối tiếp

| Trạng thái | Khi nào dùng | Bắt buộc ghi kèm |
|---|---|---|
| Tạm dừng | Dừng có chủ đích, sẽ làm tiếp | Lý do, người quyết định, dự kiến tiếp tục |
| Điều chỉnh | Đổi nội dung, thời hạn hoặc đơn vị | Giá trị cũ → lý do → căn cứ → giá trị mới |
| Chuyển kỳ | Không xong trong kỳ, đẩy sang kỳ sau | Kỳ cũ, kỳ mới, lý do. **Giữ nguyên Task_ID** |
| Hủy | Không thực hiện nữa | Căn cứ hủy, cấp quyết định |
| Quá hạn | Quá thời hạn mà chưa "Đã hoàn thành" | Hệ thống tự gán, không nhập tay |

**"Quá hạn" là trạng thái do hệ thống tính, không phải do người nhập.** Nó chồng lên trạng thái chính chứ
không thay thế: một nhiệm vụ có thể vừa "Đang thực hiện" vừa "Quá hạn".

## Tám loại cảnh báo

| Cảnh báo | Điều kiện phát hiện |
|---|---|
| Sắp đến hạn | Còn ≤ 7 ngày, chưa "Đã hoàn thành" |
| Quá hạn | Đã qua hạn, chưa "Đã hoàn thành" |
| Chưa bắt đầu | Đã qua 1/3 thời gian, vẫn ở "Mới" hoặc "Đã giao" |
| Không cập nhật | Quá 30 ngày không có lần cập nhật nào |
| Tiến độ thấp | % tiến độ < % thời gian đã trôi qua, chênh ≥ 30 điểm |
| Thiếu sản phẩm | Ở "Đã hoàn thành" nhưng trường sản phẩm rỗng |
| Thiếu minh chứng | Có sản phẩm nhưng không có minh chứng |
| Nguy cơ không hoàn thành | Cùng lúc dính ≥ 2 cảnh báo trên |

Ba mức màu trên Dashboard: **xanh** đúng tiến độ · **vàng** có nguy cơ · **đỏ** quá hạn hoặc rủi ro cao.

## Quy tắc ghi lịch sử

Mọi lần đổi trạng thái hoặc đổi giá trị trường đều ghi một dòng lịch sử theo đúng chuỗi:

```
Giá trị cũ → Lý do thay đổi → Nguồn/căn cứ → Người thay đổi → Thời gian → Giá trị mới
```

Không ghi đè giá trị cũ. Không có dòng lịch sử thì thay đổi đó coi như chưa hợp lệ.
