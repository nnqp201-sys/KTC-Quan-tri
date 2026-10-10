# Chốt kỳ và dựng báo cáo

## Nguyên tắc gốc

Báo cáo **không** bắt đầu bằng việc yêu cầu các đơn vị "viết lại từ đầu". Hệ thống lấy dữ liệu đã có từ
theo dõi, đối chiếu với kế hoạch, rồi dựng báo cáo. Đơn vị chỉ bổ sung phần dữ liệu còn thiếu.

## Quy trình 12 bước của chu trình hợp nhất

| Bước | Việc | Hệ chịu trách nhiệm |
|---|---|---|
| 1 | Tiếp nhận nguồn (văn bản chỉ đạo, kế hoạch cấp trên, nhiệm vụ phát sinh) | Kế hoạch |
| 2 | Chuẩn hóa: nhiệm vụ, sản phẩm, chủ trì, phối hợp, thời hạn, căn cứ | Kế hoạch |
| 3 | Cấp Task_ID | Kế hoạch |
| 4 | Giao nhiệm vụ vào hệ theo dõi | Kế hoạch → Theo dõi |
| 5 | Cập nhật định kỳ: tiến độ, kết quả, khó khăn, minh chứng | Theo dõi |
| 6 | Phát cảnh báo: sắp hạn, quá hạn, thiếu dữ liệu, rủi ro | Theo dõi |
| 7 | **Chốt kỳ** — khóa dữ liệu sau khi kiểm tra | Theo dõi |
| 8 | Dựng báo cáo từ dữ liệu đã khóa | Báo cáo |
| 9 | Kiểm tra: Kế hoạch ↔ Theo dõi ↔ Kết quả ↔ Minh chứng ↔ Báo cáo | Báo cáo |
| 10 | Trình người có thẩm quyền phê duyệt | Lãnh đạo |
| 11 | Đánh giá: hoàn thành, chưa hoàn thành, nguyên nhân, trách nhiệm, hiệu quả | Lãnh đạo |
| 12 | Phản hồi về kế hoạch — đầu vào cho chu kỳ tiếp theo | Kế hoạch |

Bước 7 là **chốt chặn**: sau khi khóa, mọi thay đổi phải đi qua trạng thái "Điều chỉnh" và ghi lịch sử,
không sửa trực tiếp.

## Đọc tệp báo cáo của đơn vị — loại dòng tiêu đề nhóm trước khi đếm

Mẫu Phụ lục IIb có sẵn các **dòng tiêu đề nhóm** không phải nhiệm vụ. Không loại chúng ra thì số liệu
đội lên khoảng **30%**. Trên bộ dữ liệu thật tháng 8/2026: 428 dòng thô nhưng chỉ **328 nhiệm vụ thực** —
100 dòng là tiêu đề.

Dấu hiệu nhận biết dòng tiêu đề nhóm: cột "Nội dung công việc" có chữ nhưng **mọi cột còn lại đều rỗng**
(không sản phẩm, không đơn vị chủ trì, không người chỉ đạo, không điểm chấm). Các mẫu thường gặp:

- `Các nhiệm vụ theo kế hoạch (chương trình) công tác đã đề ra`
- `Trục (1)` … `Trục (6)` — sáu dòng
- `Các nhiệm vụ đột xuất, phát sinh khác ngoài kế hoạch (nếu có)`
- `CÁC NHIỆM VỤ CHƯA HOÀN THÀNH, ĐANG TRIỂN KHAI THỰC HIỆN`

Ba dòng tiêu đề cuối chính là chỉ dẫn sẵn có để phân nhiệm vụ vào **Phần 1 / Phần 3 / Phần 2** của báo cáo
— dùng chúng thay vì tự phân loại lại.

**Kiểm tra kèm:** đủ 6 dòng `Trục (1)`–`Trục (6)` không? Thiếu Trục nào nghĩa là đơn vị bỏ trống mục đó
trong báo cáo — phải nêu ra, đừng lặng lẽ bỏ qua.

## Chuyển văn phong cấp đơn vị sang cấp Trường — BẮT BUỘC

**Căn cứ:** lưu ý nguyên tắc in ngay trong mẫu `00. Mau bao cao thang (cap Truong).docx`, lặp lại ở cả 4
mục lớn:

> *"Chuyển văn phong từ Phòng sang văn phong cấp Trường, không dùng các từ/cụm từ như: Tham mưu cho Lãnh
> đạo Trường…, phối hợp với {các đơn vị thuộc Trường…}"*

**Lý do:** ở cấp Trường, Nhà trường là chủ thể duy nhất. Nhà trường không thể "tham mưu cho chính mình",
và việc phối hợp giữa các đơn vị nội bộ là chuyện bên trong, không nêu trong báo cáo gửi UBND tỉnh.

**Đối chiếu thực tế:** báo cáo tháng 8/2026 đã ban hành (`BC-375`) có **0 lần** dùng "tham mưu" trên 92
đoạn.

### Bảng chuyển

| Văn phong cấp đơn vị | Cấp Trường |
|---|---|
| tham mưu cho Lãnh đạo Trường **ban hành** X | **ban hành** X |
| tham mưu **văn bản / nội dung / kế hoạch** | **xây dựng** văn bản / nội dung / kế hoạch |
| tham mưu **<động từ khác>** | bỏ hẳn "tham mưu", giữ động từ |
| trình / đề xuất Hiệu trưởng **phê duyệt** X | **phê duyệt** X |
| phối hợp với **Phòng/Khoa/Bộ môn nội bộ** làm X | **làm X** (bỏ tên đơn vị nội bộ) |
| phối hợp với **doanh nghiệp / UBND xã / đối tác ngoài** | **giữ nguyên** — đây là quan hệ đối ngoại, BC-375 vẫn dùng |

### Cạm bẫy khi tự động hóa

Khi cắt cụm "phối hợp với <đơn vị>", phải **liệt kê tường minh tên đơn vị nội bộ** để cắt đúng chỗ. Dùng
mẫu chung kiểu `(Phòng|Khoa)\s+[^,;.]{1,60}` sẽ ăn lan sang cả hành động phía sau và **xóa mất nội dung** —
đã mắc lỗi này một lần.

Tương tự, khi thay "tham mưu" bằng "xây dựng", chỉ thay khi sau đó là **danh từ**; nếu sau đó là động từ thì
bỏ hẳn, nếu không sẽ sinh câu sai ngữ pháp kiểu *"xây dựng đăng ký loại bỏ ngành nghề"*.

## Cấu trúc báo cáo — 5 phần

### Phần 1 — Kết quả thực hiện
Nhiệm vụ hoàn thành · sản phẩm đạt được · chỉ tiêu · kết quả nổi bật.

### Phần 2 — Nhiệm vụ chưa hoàn thành
Với **mỗi** nhiệm vụ phải đủ 5 mục: nhiệm vụ · nguyên nhân · trách nhiệm · thời hạn mới · giải pháp.
Thiếu một mục thì phần đó chưa dùng được.

### Phần 3 — Nhiệm vụ phát sinh
Ghi rõ: nguồn phát sinh · căn cứ · thời điểm · đơn vị thực hiện · kết quả.
**Không đưa nhiệm vụ phát sinh vào báo cáo mà không ghi nguồn.**

### Phần 4 — Khó khăn, vướng mắc
Phân loại theo 7 nhóm: pháp lý · tài chính · nhân sự · phối hợp · tiến độ · dữ liệu · kỹ thuật.

### Phần 5 — Kiến nghị
**Chỉ đưa kiến nghị có căn cứ từ dữ liệu theo dõi.** Kiến nghị không truy được về dữ liệu thì bỏ.

## Checklist 12 điểm — chạy trước khi chốt báo cáo

| # | Câu hỏi | Không đạt thì |
|---|---|---|
| 1 | Nhiệm vụ có trong kế hoạch không? | Xếp vào Phần 3, truy nguồn phát sinh |
| 2 | Có Task_ID không? | Dừng — cấp mã trước |
| 3 | Có đơn vị chủ trì không? | Dừng — không quy được trách nhiệm |
| 4 | Có thời hạn không? | Dừng — không đánh giá được đúng/chậm |
| 5 | Có kết quả không? | Xếp vào Phần 2 |
| 6 | Có minh chứng không? | Không được ghi "đã hoàn thành" |
| 7 | Kết quả có khớp sản phẩm yêu cầu không? | Ghi rõ phần lệch |
| 8 | Có nhiệm vụ quá hạn không? | Liệt kê đủ ở Phần 2 |
| 9 | Có nhiệm vụ bị bỏ sót không? | Duyệt ngược từ kế hoạch |
| 10 | Có nhiệm vụ phát sinh không? | Đưa vào Phần 3 kèm nguồn |
| 11 | Có thay đổi so với kế hoạch không? | Đối chiếu `Lich_Su` |
| 12 | Báo cáo có phản ánh đúng dữ liệu theo dõi không? | Tính lại độc lập, không chép số tổng |

## Trước khi trình ký

Báo cáo hoàn chỉnh phải đi qua `ktc-ra-soat-897` — lớp kiểm soát chất lượng bắt buộc về thể thức và căn cứ
pháp lý. Hệ này **không** thay thế bước đó.

```
KTC-Ke-Hoach → KTC-Theo-doi-CV → KTC-Bao-Cao → KTC-Ra-Soat-897 → Trình ký / Ban hành
```
