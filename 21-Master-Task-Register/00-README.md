# 21-Master-Task-Register

Sổ dữ liệu trung tâm của ba hệ Kế hoạch – Theo dõi – Báo cáo. Đây là hạng mục **ưu tiên số 1** trong lộ
trình hợp nhất (mục XXII Kế hoạch hợp nhất).

**Bản hiện hành:** `Master-Task-Register_20260913_v0.1.xlsx` — dự thảo, sổ trống, bộ trường **chưa chốt**.

## Cấu trúc sổ

| Sheet | Nội dung |
|---|---|
| `00-Huong-dan` | Quyền ghi theo nhóm trường · 4 quy tắc bất biến · cảnh báo độ phủ danh mục · mốc chuyển định dạng |
| `01-Master-Task-Register` | 46 cột theo `20-Chuan-Chung/10-Tu-Dien-Truong-Du-Lieu.md`. Hàng 2 ghi nhóm A–H, hàng 3 đánh dấu trường bắt buộc |
| `02-Danh-muc-tra-cuu` | Giá trị hợp lệ: 11 đơn vị · 6 Trục + 38 Nội hàm · 7 trạng thái chính · 5 trạng thái phụ · 5 nhóm quy đổi · 8 cảnh báo |
| `03-Lich-su-thay-doi` | Mỗi thay đổi một dòng: giá trị cũ → lý do → căn cứ → người → thời gian → giá trị mới |

## Phân quyền ghi — không chồng lấn

| Hệ | Được ghi | Chỉ đọc |
|---|---|---|
| `KTC-Ke-Hoach` | A Định danh · B Nội dung · C Căn cứ · D Trách nhiệm · E Thời gian | F, G, H |
| `KTC-Theo-doi-CV` | F Tiến độ · G Kết quả | A–E |
| `KTC-Bao-Cao` | H Báo cáo | A–G |

Đây là cách hiện thực nguyên tắc "một nhiệm vụ – một dòng dữ liệu gốc – nhiều góc nhìn": ba hệ cùng nhìn
một dòng, mỗi hệ chỉ ghi phần thuộc trách nhiệm mình, không hệ nào sao chép nhiệm vụ sang bảng riêng.

## Vì sao chọn `.xlsx` ở giai đoạn này

Mục IX Kế hoạch hợp nhất đề xuất Google Sheet, và đó là đích đến đúng. Nhưng ràng buộc *hiện tại* là **lặp
nhanh trên schema** chứ chưa phải nhiều người ghi đồng thời — sổ đang trống và bộ trường còn thay đổi.
`.xlsx` cho phép sinh lại và kiểm tra tất định bằng script, khớp cách ba hệ đang làm việc, và theo được quy
ước phiên bản `_YYYYMMDD_vN` của `KTC-Database`.

**Mốc chuyển sang Google Sheet:** khi bộ trường được chốt và bắt đầu có từ hai đơn vị trở lên cùng cập nhật
tiến độ trong một kỳ. Chuyển sớm hơn sẽ phải sửa cấu trúc trên bản nhiều người đang dùng — tốn hơn.

## Trước khi chốt bản v1.0, cần xong bốn việc

1. **Chốt bộ trường** — 46 trường hiện tại là dự thảo hợp nhất từ ba nguồn, chưa có đơn vị nào dùng thử.
2. **Chốt quy tắc Task_ID** — xem `20-Chuan-Chung/11-Quy-Tac-Task-ID.md`.
3. **Bổ sung cột `Task_ID` vào Phụ lục Ia/Ib của TB736** — chừng nào chưa có, kế hoạch và báo cáo vẫn chỉ
   đối chiếu gần đúng theo Trục + tên nhiệm vụ, không đối chiếu 1-1 được.
4. **Xác minh "phần mềm KPI"** mà Quy chế ban hành kèm Quyết định 1923/QĐ-CĐKT dẫn chiếu — nếu phần mềm đó
   đã quản lý chỉ tiêu KPI theo quý thì phải xác định ranh giới, tránh làm trùng chức năng.

## Cảnh báo khi nạp dữ liệu

122 nhiệm vụ chuẩn `A01`–`S04` **chỉ tổng hợp từ 5 Phòng, không có Khoa nào** (chi tiết:
`20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`). Khi một Khoa đăng ký nhiệm vụ không khớp mã nào, để trống
`Ma_NV_Chuan` và đề nghị bổ sung mã mới — **không ép về mã gần đúng**, vì làm vậy sẽ tạo dữ liệu sai mà
không ai phát hiện được về sau.

## Quan hệ với `ktc-ra-soat-897`

Master Task Register là **sổ dữ liệu**, không phải văn bản — bản thân nó không qua rà soát. Nhưng mọi
**sản phẩm sinh ra từ sổ này** (kế hoạch, báo cáo, phụ lục trình ký) đều phải qua `ktc-ra-soat-897` trước
khi trình ký. Đây là chốt chặn bắt buộc.

Hai trường có liên quan trực tiếp: `Minh_Chung` (đường dẫn bằng chứng — 897 kiểm tính xác thực của căn cứ)
và `Can_Cu` (số hiệu văn bản làm căn cứ — 897 kiểm hiệu lực và thẩm quyền).
