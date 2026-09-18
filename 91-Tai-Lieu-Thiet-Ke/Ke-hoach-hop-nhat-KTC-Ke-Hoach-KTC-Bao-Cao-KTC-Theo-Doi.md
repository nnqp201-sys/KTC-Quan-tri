# KẾ HOẠCH HỢP NHẤT HỆ THỐNG KTC-KẾ-HOẠCH + KTC-BÁO-CÁO + KTC-THEO-DÕI

**Phiên bản:** 1.0  
**Ngày xây dựng:** 10/09/2026  
**Phạm vi:** Trường Cao đẳng Kon Tum  
**Mục tiêu:** Hợp nhất ba hệ thống thành một chu trình quản trị nhiệm vụ khép kín, có dữ liệu dùng chung, truy vết được và hỗ trợ AI.

---

## I. MỤC ĐÍCH

Hợp nhất:

1. **KTC-Kế-Hoạch** – lập và quản trị kế hoạch.
2. **KTC-Theo-Dõi** – theo dõi nhiệm vụ, tiến độ, hạn hoàn thành, kết quả và bằng chứng.
3. **KTC-Báo-Cáo** – thu thập kết quả, đối chiếu kế hoạch và lập báo cáo.

Ba hệ thống không hoạt động như ba kho dữ liệu độc lập mà tạo thành một hệ thống thống nhất:

> **Chủ trương/Văn bản → Nhiệm vụ → Kế hoạch → Giao việc → Theo dõi → Kết quả/Bằng chứng → Báo cáo → Đánh giá → Điều chỉnh kế hoạch**

---

# II. NGUYÊN TẮC KIẾN TRÚC

## 1. Một nguồn dữ liệu dùng chung

Mỗi nhiệm vụ chỉ có **một mã định danh duy nhất**.

Không tạo lại cùng một nhiệm vụ ở Kế hoạch, Theo dõi và Báo cáo.

Ví dụ:

`KTC-2026-Q3-00125`

Mã này được sử dụng xuyên suốt:

- kế hoạch;
- giao nhiệm vụ;
- theo dõi;
- cập nhật tiến độ;
- minh chứng;
- báo cáo;
- đánh giá;
- lịch sử xử lý.

## 2. Kế hoạch là nguồn gốc của nhiệm vụ

KTC-Kế-Hoạch tạo ra **nhiệm vụ chuẩn**.

KTC-Theo-Dõi không tự tạo nhiệm vụ mới nếu nhiệm vụ đã tồn tại trong Kế hoạch; chỉ được:

- tiếp nhận;
- phân công;
- cập nhật;
- theo dõi;
- ghi nhận thay đổi.

KTC-Báo-Cáo lấy dữ liệu thực hiện từ nhiệm vụ đã được quản lý.

## 3. Báo cáo phải truy ngược được

Mọi kết quả trong báo cáo phải có khả năng truy ngược:

**Báo cáo → Nhiệm vụ → Kế hoạch → Người/đơn vị thực hiện → Kết quả → Minh chứng**

Không đưa vào báo cáo các kết quả không xác định được nguồn.

## 4. Theo dõi là lớp trung gian

KTC-Theo-Dõi đóng vai trò **control tower**:

- nhận nhiệm vụ từ KTC-Kế-Hoạch;
- theo dõi trạng thái;
- cảnh báo quá hạn;
- thu nhận kết quả;
- xác định nhiệm vụ chưa hoàn thành;
- cung cấp dữ liệu cho KTC-Báo-Cáo.

## 5. AI không thay thế dữ liệu gốc

AI có nhiệm vụ:

- đọc;
- đối chiếu;
- phân loại;
- phát hiện thiếu/sai;
- tổng hợp;
- đề xuất;
- dự thảo.

Quyết định chính thức vẫn thuộc người có thẩm quyền.

---

# III. KIẾN TRÚC TỔNG THỂ

```text
                    ┌───────────────────────┐
                    │  CHỦ TRƯƠNG / VĂN BẢN │
                    │  KTC-DATABASE         │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │    KTC-KẾ-HOẠCH       │
                    │ Lập / tổng hợp / giao │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │     KTC-THEO-DÕI       │
                    │ Control Tower nhiệm vụ │
                    └───────┬───────┬───────┘
                            │       │
                 tiến độ ◄─┘       └─► kết quả
                            │
                            ▼
                    ┌───────────────────────┐
                    │ KẾT QUẢ + MINH CHỨNG  │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │     KTC-BÁO-CÁO        │
                    │ Tổng hợp / phân tích   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ ĐÁNH GIÁ / ĐIỀU CHỈNH │
                    │      KẾ HOẠCH          │
                    └───────────┬───────────┘
                                │
                                └──────► chu kỳ mới
```

---

# IV. VAI TRÒ CỦA TỪNG HỆ

## A. KTC-KẾ-HOẠCH

### Chức năng chính

- Tiếp nhận nhiệm vụ từ chủ trương, văn bản, chương trình.
- Xây dựng kế hoạch năm/quý/tháng/chuyên đề.
- Chuẩn hóa nhiệm vụ.
- Phân loại theo lĩnh vực/trục công tác.
- Xác định:
  - nội dung;
  - sản phẩm;
  - đơn vị chủ trì;
  - đơn vị phối hợp;
  - thời hạn;
  - yêu cầu;
  - căn cứ;
  - chỉ tiêu;
  - minh chứng dự kiến.

### Đầu ra

- Kế hoạch dự thảo.
- Kế hoạch đã ban hành.
- Danh mục nhiệm vụ.
- Bảng phân công.
- Dữ liệu nhiệm vụ chuẩn cho KTC-Theo-Dõi.

---

# V. KTC-THEO-DÕI

## 1. Vai trò

KTC-Theo-Dõi là **trung tâm vận hành nhiệm vụ**.

Mỗi nhiệm vụ có vòng đời:

```text
Mới
 ↓
Đã giao
 ↓
Đang thực hiện
 ↓
Chờ kết quả
 ↓
Đã hoàn thành
 ↓
Đã kiểm tra
 ↓
Đã báo cáo
```

Có thể bổ sung:

- Tạm dừng
- Điều chỉnh
- Hủy
- Quá hạn
- Chuyển kỳ

## 2. Theo dõi tối thiểu

Mỗi nhiệm vụ cần có:

| Trường | Nội dung |
|---|---|
| Task_ID | Mã nhiệm vụ duy nhất |
| Kỳ kế hoạch | Năm/quý/tháng |
| Nội dung | Nhiệm vụ |
| Căn cứ | Văn bản/chủ trương |
| Chủ trì | Đơn vị/cá nhân |
| Phối hợp | Đơn vị liên quan |
| Sản phẩm | Kết quả phải tạo |
| Hạn | Ngày hoàn thành |
| Trạng thái | Trạng thái hiện tại |
| % tiến độ | Tiến độ |
| Kết quả | Kết quả thực tế |
| Minh chứng | File/liên kết |
| Vướng mắc | Khó khăn |
| Đề xuất | Kiến nghị |
| Ngày cập nhật | Lần cập nhật gần nhất |
| Người cập nhật | Người ghi nhận |
| Lịch sử | Các lần thay đổi |

## 3. Cảnh báo

Hệ thống cần phát hiện:

- sắp đến hạn;
- quá hạn;
- chưa bắt đầu;
- không cập nhật;
- tiến độ thấp;
- thiếu sản phẩm;
- thiếu minh chứng;
- nhiệm vụ có nguy cơ không hoàn thành.

---

# VI. KTC-BÁO-CÁO

## 1. Nguyên tắc

Báo cáo không bắt đầu từ việc yêu cầu các đơn vị "viết lại từ đầu".

Hệ thống lấy dữ liệu từ KTC-Theo-Dõi để:

1. đối chiếu kế hoạch;
2. xác định nhiệm vụ đã hoàn thành;
3. xác định nhiệm vụ chưa hoàn thành;
4. xác định nhiệm vụ phát sinh;
5. xác định nhiệm vụ điều chỉnh;
6. xác định nhiệm vụ quá hạn;
7. tổng hợp kết quả theo lĩnh vực/trục/đơn vị/kỳ.

## 2. Cấu trúc báo cáo

### Phần 1 – Kết quả thực hiện

- nhiệm vụ hoàn thành;
- sản phẩm đạt được;
- chỉ tiêu;
- kết quả nổi bật.

### Phần 2 – Nhiệm vụ chưa hoàn thành

- nhiệm vụ;
- nguyên nhân;
- trách nhiệm;
- thời hạn mới;
- giải pháp.

### Phần 3 – Nhiệm vụ phát sinh

Phải ghi rõ:

- nguồn phát sinh;
- căn cứ;
- thời điểm;
- đơn vị thực hiện;
- kết quả.

### Phần 4 – Khó khăn, vướng mắc

Phân loại:

- pháp lý;
- tài chính;
- nhân sự;
- phối hợp;
- tiến độ;
- dữ liệu;
- kỹ thuật.

### Phần 5 – Kiến nghị

Chỉ đưa kiến nghị có căn cứ từ dữ liệu theo dõi.

---

# VII. DỮ LIỆU CHUNG

Đề xuất xây dựng một **KTC Master Task Register**.

Đây là bảng dữ liệu trung tâm của ba hệ.

## Các nhóm dữ liệu

### Nhóm A – Định danh

- Task_ID
- Parent_Task_ID
- Plan_ID
- Report_ID

### Nhóm B – Nội dung

- tên nhiệm vụ;
- mô tả;
- mục tiêu;
- sản phẩm.

### Nhóm C – Căn cứ

- văn bản;
- số/ký hiệu;
- ngày;
- cơ quan ban hành;
- điều/khoản liên quan.

### Nhóm D – Trách nhiệm

- chủ trì;
- phối hợp;
- người phụ trách;
- cấp phê duyệt.

### Nhóm E – Thời gian

- ngày bắt đầu;
- hạn;
- ngày hoàn thành;
- kỳ kế hoạch.

### Nhóm F – Tiến độ

- trạng thái;
- % hoàn thành;
- mức rủi ro;
- cảnh báo.

### Nhóm G – Kết quả

- kết quả;
- sản phẩm;
- chỉ tiêu;
- minh chứng.

### Nhóm H – Báo cáo

- đã báo cáo;
- kỳ báo cáo;
- nội dung báo cáo;
- kết luận đánh giá.

---

# VIII. QUAN HỆ DỮ LIỆU

```text
1 Văn bản
   ↓
N Nhiệm vụ
   ↓
1 Task_ID
   ↓
N lần cập nhật tiến độ
   ↓
N minh chứng
   ↓
N báo cáo
   ↓
N lần đánh giá
```

Không nên sao chép dữ liệu nhiệm vụ sang nhiều bảng độc lập.

Thay vào đó dùng:

- ID;
- khóa liên kết;
- trạng thái;
- lịch sử thay đổi.

---

# IX. PROCESS MEMORY / AUDIT TRAIL

Một thành phần quan trọng là **Nhật ký vận hành**.

Đề xuất duy trì Google Sheet:

**“Nhật ký vận hành KTC-Kế-Hoạch”**

Mỗi phiên xử lý = một dòng.

## Trường đề xuất

| Trường | Nội dung |
|---|---|
| Session_ID | Mã phiên |
| Thời gian | Thời điểm xử lý |
| Hệ thống | Kế hoạch/Theo dõi/Báo cáo |
| Người yêu cầu | Người khởi tạo |
| Input | Dữ liệu đầu vào |
| Nhiệm vụ | Task_ID liên quan |
| AI/Agent | Hệ thống AI sử dụng |
| Thao tác | Công việc đã thực hiện |
| Nguồn | Nguồn dữ liệu |
| Kết quả | Output |
| Quyết định | Người phê duyệt |
| Thay đổi | Nội dung thay đổi |
| Lỗi | Lỗi phát sinh |
| Cách xử lý | Cách khắc phục |
| Link | File/bằng chứng |
| Trạng thái | Hoàn tất/chờ xử lý |

Mục tiêu là hệ thống **nhớ được quá trình**, không chỉ nhớ kết quả.

---

# X. QUY TRÌNH HỢP NHẤT CHUẨN

## Bước 1 – Tiếp nhận nguồn

Nguồn có thể gồm:

- văn bản chỉ đạo;
- kế hoạch cấp trên;
- nhiệm vụ của tỉnh;
- nhiệm vụ của Bộ/Sở;
- kế hoạch của Trường;
- nhiệm vụ phát sinh.

↓

## Bước 2 – Chuẩn hóa

KTC-Kế-Hoạch xác định:

- nhiệm vụ;
- sản phẩm;
- chủ trì;
- phối hợp;
- thời hạn;
- căn cứ.

↓

## Bước 3 – Tạo Task_ID

Mỗi nhiệm vụ có mã duy nhất.

↓

## Bước 4 – Giao nhiệm vụ

Nhiệm vụ được đưa vào KTC-Theo-Dõi.

↓

## Bước 5 – Theo dõi

Cập nhật định kỳ:

- tiến độ;
- kết quả;
- khó khăn;
- minh chứng.

↓

## Bước 6 – Cảnh báo

Hệ thống tự phát hiện:

- sắp hạn;
- quá hạn;
- thiếu dữ liệu;
- rủi ro.

↓

## Bước 7 – Chốt kỳ

Khi kết thúc tháng/quý:

KTC-Theo-Dõi khóa dữ liệu kỳ báo cáo sau khi kiểm tra.

↓

## Bước 8 – Tạo báo cáo

KTC-Báo-Cáo tự động lấy dữ liệu.

↓

## Bước 9 – Kiểm tra

Đối chiếu:

**Kế hoạch ↔ Theo dõi ↔ Kết quả ↔ Minh chứng ↔ Báo cáo**

↓

## Bước 10 – Phê duyệt

Người có thẩm quyền xem xét và phê duyệt.

↓

## Bước 11 – Đánh giá

Xác định:

- hoàn thành;
- chưa hoàn thành;
- nguyên nhân;
- trách nhiệm;
- hiệu quả.

↓

## Bước 12 – Phản hồi về Kế hoạch

Kết quả đánh giá trở thành dữ liệu đầu vào cho chu kỳ kế hoạch tiếp theo.

---

# XI. DASHBOARD QUẢN TRỊ

Đề xuất một Dashboard hợp nhất.

## Chỉ số tổng quan

- Tổng số nhiệm vụ.
- Đã hoàn thành.
- Đang thực hiện.
- Chưa thực hiện.
- Quá hạn.
- Có nguy cơ quá hạn.
- Tỷ lệ hoàn thành.
- Tỷ lệ có minh chứng.
- Tỷ lệ cập nhật đúng hạn.

## Phân tích

Có thể lọc theo:

- năm;
- quý;
- tháng;
- đơn vị;
- lĩnh vực;
- trục công tác;
- người phụ trách;
- trạng thái.

## Cảnh báo màu

- **Xanh:** đúng tiến độ.
- **Vàng:** có nguy cơ.
- **Đỏ:** quá hạn/rủi ro cao.

---

# XII. PHÂN QUYỀN

## KTC-Kế-Hoạch

Được:

- tạo kế hoạch;
- sửa kế hoạch;
- chuẩn hóa nhiệm vụ;
- điều chỉnh lịch.

## KTC-Theo-Dõi

Được:

- cập nhật tiến độ;
- ghi nhận kết quả;
- ghi nhận vướng mắc;
- cập nhật minh chứng.

## KTC-Báo-Cáo

Được:

- khai thác dữ liệu;
- tổng hợp;
- phân tích;
- dự thảo báo cáo.

## Lãnh đạo

Có quyền:

- xem Dashboard;
- xem nhiệm vụ trọng yếu;
- xem cảnh báo;
- xem báo cáo;
- phê duyệt;
- yêu cầu điều chỉnh.

---

# XIII. TÍCH HỢP AI

## 1. KTC-Kế-Hoạch AI

AI hỗ trợ:

- đọc văn bản;
- trích nhiệm vụ;
- chuẩn hóa;
- phát hiện trùng;
- phân loại;
- lập dự thảo kế hoạch.

## 2. KTC-Theo-Dõi AI

AI hỗ trợ:

- phát hiện chậm;
- dự báo nguy cơ;
- nhắc việc;
- phân tích nguyên nhân;
- xác định nhiệm vụ cần lãnh đạo can thiệp.

## 3. KTC-Báo-Cáo AI

AI hỗ trợ:

- tổng hợp;
- so sánh;
- phân tích chênh lệch;
- phát hiện thiếu;
- lập dự thảo báo cáo.

## 4. KTC-Rà-Soát-897

Có thể đặt thành **lớp kiểm soát chất lượng** trước khi:

- trình ký kế hoạch;
- trình ký báo cáo;
- ban hành văn bản quan trọng.

Luồng:

```text
KTC-Kế-Hoạch
      ↓
KTC-Theo-Dõi
      ↓
KTC-Báo-Cáo
      ↓
KTC-Rà-Soát-897
      ↓
Trình ký / Ban hành
```

---

# XIV. NGUỒN DỮ LIỆU

Theo nguyên tắc đã thống nhất:

- **KTC-Database** là nguồn chính thức cho dữ liệu văn bản nội bộ.
- **KTC-Kế-Hoạch** là nguồn chính của dữ liệu kế hoạch.
- **KTC-Báo-Cáo** là nguồn kết quả báo cáo đã xác nhận.
- **KTC-Theo-Dõi** là nguồn trạng thái thực hiện.
- Internet chỉ bổ sung khi cần kiểm chứng hiệu lực/cập nhật văn bản hoặc nội bộ thiếu dữ liệu; ưu tiên nguồn chính thống.

Các nguồn phải được phân biệt rõ trong kết quả AI.

---

# XV. GOOGLE DRIVE

Đề xuất cấu trúc logic:

```text
KTC-Database/
├── Kho 01
├── Kho 02
├── Kho 03
└── Kho 04

23-KTC-Ke-Hoach/
├── Ke-hoach-Nam
├── Ke-hoach-Quy
├── Ke-hoach-Thang
├── Ke-hoach-Chuyen-de
└── Nhiem-vu

25-KTC-Bao-Cao/
├── Bao-cao-Thang
├── Bao-cao-Quy
├── Bao-cao-Nam
└── Minh-chung

KTC-Theo-Doi/
├── Master-Task
├── Dashboard
├── Canh-bao
└── Nhat-ky-van-hanh
```

Không tự động mở rộng phạm vi truy cập sang các thư mục khác nếu chưa được phép.

---

# XVI. LỘ TRÌNH TRIỂN KHAI

## Giai đoạn 1 – Chuẩn hóa

- thống nhất thuật ngữ;
- thống nhất Task_ID;
- thống nhất trạng thái;
- thống nhất trường dữ liệu;
- thống nhất nguồn.

## Giai đoạn 2 – Hợp nhất dữ liệu

- lập Master Task Register;
- liên kết kế hoạch;
- liên kết theo dõi;
- liên kết báo cáo;
- xây dựng nhật ký.

## Giai đoạn 3 – Hợp nhất quy trình

Triển khai chu trình:

> Kế hoạch → Theo dõi → Kết quả → Báo cáo.

## Giai đoạn 4 – Dashboard

Xây dựng:

- Dashboard lãnh đạo;
- Dashboard đơn vị;
- Dashboard nhiệm vụ;
- Dashboard cảnh báo.

## Giai đoạn 5 – AI

Tích hợp AI vào:

- trích nhiệm vụ;
- kiểm tra;
- cảnh báo;
- tổng hợp;
- dự thảo.

## Giai đoạn 6 – Kiểm soát

Kết nối KTC-Rà-Soát-897 để kiểm tra chất lượng trước trình ký.

---

# XVII. QUY TẮC KIỂM SOÁT CHẤT LƯỢNG

Trước khi chốt một báo cáo, hệ thống phải kiểm tra:

1. Có nhiệm vụ trong kế hoạch không?
2. Có Task_ID không?
3. Có đơn vị chủ trì không?
4. Có thời hạn không?
5. Có kết quả không?
6. Có minh chứng không?
7. Kết quả có khớp sản phẩm yêu cầu không?
8. Có nhiệm vụ quá hạn không?
9. Có nhiệm vụ bị bỏ sót không?
10. Có nhiệm vụ phát sinh không?
11. Có thay đổi so với kế hoạch không?
12. Báo cáo có phản ánh đúng dữ liệu theo dõi không?

---

# XVIII. NGUYÊN TẮC ĐỐI VỚI NHIỆM VỤ PHÁT SINH

Không được đưa nhiệm vụ phát sinh trực tiếp vào báo cáo mà không ghi nhận nguồn.

Nhiệm vụ phát sinh phải có:

- nguồn;
- căn cứ;
- ngày phát sinh;
- người/đơn vị giao;
- đơn vị thực hiện;
- thời hạn;
- sản phẩm;
- kết quả.

Sau đó mới tạo Task_ID và đưa vào hệ thống.

---

# XIX. CƠ CHẾ ĐIỀU CHỈNH KẾ HOẠCH

Mọi thay đổi phải có lịch sử:

```text
Giá trị cũ
    ↓
Lý do thay đổi
    ↓
Nguồn/căn cứ
    ↓
Người thay đổi
    ↓
Thời gian
    ↓
Giá trị mới
```

Phân loại:

- bổ sung;
- điều chỉnh thời gian;
- điều chỉnh nội dung;
- điều chỉnh đơn vị;
- tạm dừng;
- hủy;
- chuyển kỳ.

---

# XX. MÔ HÌNH QUẢN TRỊ CUỐI CÙNG

Mô hình đề xuất:

```text
                    LÃNH ĐẠO
                       │
              ┌────────▼────────┐
              │ KTC CONTROL TOWER│
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 KTC-KẾ-HOẠCH    KTC-THEO-DÕI    KTC-BÁO-CÁO
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              MASTER TASK REGISTER
                       │
                       ▼
              PROCESS MEMORY /
                AUDIT TRAIL
                       │
                       ▼
              KTC-RÀ-SOÁT-897
                       │
                       ▼
                TRÌNH KÝ / BAN HÀNH
```

---

# XXI. KẾT QUẢ KỲ VỌNG

Sau khi hợp nhất, Trường có một chu trình quản trị:

**Một nhiệm vụ – Một mã – Một dòng dữ liệu gốc – Một lịch sử – Nhiều góc nhìn.**

Cụ thể:

- Kế hoạch biết **phải làm gì**.
- Theo dõi biết **đang làm đến đâu**.
- Báo cáo biết **đã làm được gì**.
- Minh chứng chứng minh **đã làm như thế nào**.
- AI phân tích **có vấn đề gì**.
- Lãnh đạo biết **cần quyết định gì**.
- Process Memory ghi lại **đã xử lý ra sao**.

Mục tiêu cuối cùng không phải chỉ là "tự động hóa lập kế hoạch và báo cáo", mà là xây dựng **hệ thống quản trị nhiệm vụ và kết quả thống nhất của Trường Cao đẳng Kon Tum**, có khả năng truy vết từ chủ trương đến kết quả cuối cùng.

---

## XXII. ĐỀ XUẤT BƯỚC TIẾP THEO

Ưu tiên triển khai theo thứ tự:

1. **Chốt Master Task Register.**
2. **Chốt bộ trường dữ liệu dùng chung.**
3. **Chốt mã Task_ID.**
4. **Chốt trạng thái vòng đời nhiệm vụ.**
5. **Thiết kế Google Sheet/Drive làm lớp dữ liệu vận hành.**
6. **Kết nối KTC-Kế-Hoạch → KTC-Theo-Dõi.**
7. **Kết nối KTC-Theo-Dõi → KTC-Báo-Cáo.**
8. **Thiết lập Dashboard.**
9. **Thiết lập Process Memory/Audit Trail.**
10. **Kết nối KTC-Rà-Soát-897 làm lớp kiểm soát chất lượng.**

**Ưu tiên kiến trúc:** dữ liệu và quy trình trước, AI sau.

**Nguyên tắc triển khai:** không phá vỡ các hệ hiện có; hợp nhất bằng chuẩn dữ liệu, ID và luồng xử lý chung.
