# Đối chiếu Kế hoạch ↔ Theo dõi ↔ Báo cáo

## Điều phải nói rõ trước mọi kết quả đối chiếu

Phụ lục Ia/Ib của TB736 — nguồn dữ liệu kế hoạch mà `KTC-Bao-Cao` đang đọc — **chưa có cột `Task_ID`**.
Vì vậy hiện chỉ đối chiếu được **gần đúng**, bằng Trục + so khớp tên nhiệm vụ. Chưa đối chiếu 1-1 chính xác.

Khi trình bày kết quả đối chiếu, **bắt buộc ghi rõ đây là đối chiếu gần đúng**. Trình bày như đối chiếu
chính xác là sai lệch nghiêm trọng, vì người đọc sẽ dùng nó để kết luận đơn vị nào chưa hoàn thành.

**Cách gỡ:** `KTC-Ke-Hoach` bổ sung cột `Task_ID` vào Phụ lục Ia/Ib → `KTC-Bao-Cao` sửa
`read_bc736_excel.py` đọc và dùng cột này làm khóa nối. Đây là thay đổi nhỏ nhưng mở khóa toàn bộ khả năng
đối chiếu tự động.

## Ba khóa nối, theo thứ tự ưu tiên

| Ưu tiên | Khóa | Độ tin cậy | Khi nào dùng được |
|---|---|---|---|
| 1 | `Task_ID` | Chính xác tuyệt đối | Khi Phụ lục Ia/Ib đã có cột này |
| 2 | `Don_Vi_Chu_Tri` (mã chuẩn) + `Truc` | Gom nhóm đúng, không xác định được từng nhiệm vụ | Luôn dùng được |
| 3 | So khớp tên nhiệm vụ | Gần đúng, có thể sai | Chỉ dùng bổ sung cho khóa 2, không dùng một mình |

**Trước khi so khớp theo đơn vị, bắt buộc ánh xạ tên đơn vị về mã chuẩn** — xem `12-Bang-Ma-Don-Vi.md`.
Cùng một đơn vị hiện được viết ba kiểu khác nhau; so khớp thô theo chuỗi sẽ cho ra kết quả sai.

## Sáu nhóm kết quả cần xác định

| Nhóm | Định nghĩa | Dấu hiệu nhận biết |
|---|---|---|
| Đã hoàn thành | Có trong kế hoạch, `Trang_Thai` = Đã hoàn thành, **có minh chứng** | Đủ cả 3 điều kiện |
| Chưa hoàn thành | Có trong kế hoạch, chưa đạt trạng thái hoàn thành | Phải ghi kèm nguyên nhân, trách nhiệm, thời hạn mới, giải pháp |
| Phát sinh | Có trong theo dõi, **không** có trong kế hoạch | Phải truy được nguồn phát sinh và căn cứ |
| Điều chỉnh | Có ở cả hai nhưng lệch nội dung/thời hạn/đơn vị | Đối chiếu với `Lich_Su` |
| Quá hạn | Qua `Han_Hoan_Thanh`, chưa hoàn thành | Hệ thống tính, không nhập tay |
| Bỏ sót | Có trong kế hoạch, **không** xuất hiện ở theo dõi | Nguy hiểm nhất — dễ lọt vì không ai báo cáo về nó |

Nhóm **Bỏ sót** phải được tìm chủ động bằng cách duyệt ngược từ kế hoạch sang theo dõi. Nếu chỉ duyệt từ
theo dõi lên, nhóm này sẽ vô hình.

## Trình tự đối chiếu

1. **Chốt phạm vi**: kỳ nào, đơn vị nào. Sai kỳ làm hỏng toàn bộ kết quả.
2. **Nạp ba nguồn**: baseline kế hoạch · trạng thái theo dõi · kết quả đã xác nhận.
3. **Chuẩn hóa đơn vị** về mã chuẩn ở cả ba nguồn.
4. **Nối theo khóa ưu tiên cao nhất khả dụng**, ghi rõ đã dùng khóa nào.
5. **Duyệt hai chiều**: kế hoạch → theo dõi (tìm bỏ sót) và theo dõi → kế hoạch (tìm phát sinh).
6. **Phân vào 6 nhóm**, mỗi nhiệm vụ đúng một nhóm.
7. **Liệt kê phần không nối được** — không im lặng bỏ qua. Đây thường là chỗ lộ ra lỗi dữ liệu thật.

## Bốn quy tắc khi kết luận

1. **Không suy diễn trạng thái.** Nhiệm vụ không có dữ liệu theo dõi thì ghi "không có dữ liệu", không ghi
   "chưa thực hiện" — hai điều đó khác nhau.
2. **Không tin nhãn tự khai.** Nhiệm vụ ghi "đã hoàn thành" nhưng không có minh chứng thì xếp vào nhóm
   chưa hoàn thành, kèm ghi chú.
3. **Số liệu phải tính lại độc lập**, không chép số tổng từ báo cáo của đơn vị.
4. **Chênh lệch phải nêu ra**, kể cả khi chưa giải thích được. Ghi `[CHƯA XÁC MINH]` thay vì làm tròn cho khớp.
