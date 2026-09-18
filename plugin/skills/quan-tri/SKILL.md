---
name: quan-tri
description: "Quản trị nhiệm vụ hợp nhất của Trường Cao đẳng Kon Tum theo chu trình Kế hoạch → Theo dõi → Kết quả/Minh chứng → Báo cáo → Đánh giá. Dùng khi cần chuẩn hóa nhiệm vụ và cấp Task_ID, phân loại vào 6 Trục và 38 Nội hàm theo Thông báo 817/TB-CĐKT, quy đổi điểm và hệ số theo 5 nhóm, theo dõi vòng đời nhiệm vụ và phát cảnh báo quá hạn hoặc thiếu minh chứng, đối chiếu kế hoạch với kết quả thực hiện, chốt kỳ và dựng báo cáo có truy vết, hoặc quy đổi KPI và xếp loại chất lượng theo Quyết định 1923/QĐ-CĐKT. Đây là hệ KTC-Quan-tri, lớp điều phối trên ba hệ KTC-Ke-Hoach, KTC-Theo-doi-CV, KTC-Bao-Cao. KHÔNG dùng để soạn thảo văn bản hành chính mới - dùng ktc-soan-thao-vb; KHÔNG dùng để rà soát thể thức trước trình ký - dùng ktc-ra-soat-897."
---

# KTC-Quan-tri — Hệ quản trị nhiệm vụ hợp nhất
**Phiên bản: 1.1 — 13/9/2026** (sau đợt chạy thử báo cáo tháng 8/2026 trên dữ liệu thật)

## Vai trò trong kiến trúc hệ thống KTC

Đây là **lớp điều phối** đặt trên ba hệ nghiệp vụ, không thay thế hệ nào:

```
KTC-Ke-Hoach ──> KTC-Theo-doi-CV ──> KTC-Bao-Cao
      └──────── KTC-Quan-tri ────────┘
              (một Task_ID xuyên suốt)
```

Nguyên tắc gốc: **một nhiệm vụ – một mã – một dòng dữ liệu gốc – một lịch sử – nhiều góc nhìn.**

## 6 Nguyên tắc bắt buộc

Đọc `references/01-Nguyen-Tac-Chung.md` trước khi bắt đầu bất kỳ tác vụ nào.

1. **Một nhiệm vụ – một Task_ID**, dùng xuyên suốt kế hoạch → theo dõi → báo cáo → minh chứng. Không tạo
   lại cùng một nhiệm vụ ở nhiều hệ.
2. **Kế hoạch là nguồn sinh nhiệm vụ.** Chỉ `KTC-Ke-Hoach` được cấp Task_ID. Theo dõi và Báo cáo chỉ tiếp
   nhận, cập nhật, tổng hợp.
3. **Báo cáo phải truy ngược được** tới nhiệm vụ → kế hoạch → đơn vị → kết quả → minh chứng. Không đưa vào
   báo cáo kết quả không xác định được nguồn.
4. **Nhiệm vụ phát sinh** phải ghi đủ nguồn, căn cứ, ngày phát sinh, đơn vị giao, đơn vị thực hiện, thời
   hạn, sản phẩm — rồi mới cấp Task_ID.
5. **Mọi thay đổi phải có lịch sử**: giá trị cũ → lý do → căn cứ → người thay đổi → thời gian → giá trị mới.
   Không ghi đè giá trị cũ.
6. **AI không thay thế dữ liệu gốc và không quyết định thay người có thẩm quyền.** Vai trò: đọc, đối chiếu,
   phân loại, phát hiện thiếu/sai, tổng hợp, đề xuất, dự thảo.

## Bước 0 — BẮT BUỘC làm đầu tiên, không bỏ qua

Trước mọi tác vụ, xác định đủ ba điều và **nói rõ ra** trước khi xử lý:

| # | Xác định | Nếu không xác định được |
|---|---|---|
| 1 | **Tác vụ nào** trong 5 tác vụ ở bảng dưới | Hỏi lại, không đoán |
| 2 | **Kỳ nào** — năm/quý/tháng/chuyên đề | Hỏi lại; kỳ sai làm hỏng toàn bộ đối chiếu |
| 3 | **Có đọc được dữ liệu thật không** — Master Task Register, kho 01–04 của `KTC-Database` | **Dừng và hỏi**, xem quy tắc thiếu nguồn bên dưới |

### Quy tắc thiếu nguồn — hai lớp xử lý khác nhau

- Thiếu **kho dữ liệu nền** (`KTC-Database` 01–04, Master Task Register): **dừng lại, không tạo kết quả**,
  yêu cầu người dùng đính kèm tệp hoặc kết nối Drive. Nếu người dùng yêu cầu cứ làm, phải ghi ngay đầu kết
  quả: `⚠️ Chưa đối chiếu với dữ liệu gốc — độ tin cậy hạn chế`.
- Thiếu **bộ nhớ vận hành** (nhật ký, Process Memory): **chạy tiếp** và ghi cảnh báo vào phần đầu kết quả.

## 5 tác vụ — bảng định tuyến

| Tác vụ | Khi người dùng muốn | Đọc thêm |
|---|---|---|
| **(a) Chuẩn hóa & cấp mã** | Đưa nhiệm vụ từ văn bản/kế hoạch vào hệ, phân loại, cấp Task_ID | `references/21-Quy-Tac-Task-ID.md` → `references/10-Sau-Truc-38-Noi-Ham.md` + `references/11-Skill-Phan-Loai-6-Truc.md` → `references/13-Danh-Muc-Nhiem-Vu-Va-San-Pham.md` |
| **(b) Theo dõi & cảnh báo** | Rà tiến độ, tìm nhiệm vụ quá hạn/rủi ro/thiếu minh chứng | `references/22-Vong-Doi-Va-Canh-Bao.md` |
| **(c) Đối chiếu 3 hệ** | So kế hoạch với thực hiện; tìm việc hoàn thành/chưa/phát sinh/điều chỉnh | `references/23-Doi-Chieu-Ba-He.md` |
| **(d) Chốt kỳ & dựng báo cáo** | Khóa dữ liệu kỳ, dựng báo cáo 5 phần, kiểm tra trước khi trình | `references/24-Chot-Ky-Va-Bao-Cao.md` |
| **(e) Quy đổi KPI & xếp loại** | Tính điểm quy đổi, xếp loại chất lượng tập thể/cá nhân | `references/30-KPI-Va-Xep-Loai.md` |

Với **mọi** tác vụ, khi chạm tới tên đơn vị: bắt buộc tra `references/12-Bang-Ma-Don-Vi.md`.
Khi chạm tới trường dữ liệu: tra `references/20-Tu-Dien-Truong-Du-Lieu.md`.

## Nguồn dữ liệu chuẩn — khi hai nơi mâu thuẫn, lấy theo cột phải

| Loại dữ liệu | Hệ nguồn chuẩn |
|---|---|
| Văn bản pháp lý, quy định, mẫu | `KTC-Database` kho 01–04 |
| Danh mục nhiệm vụ chuẩn, sản phẩm, điểm/hệ số, KPI, khung đánh giá | `Du-lieu-Cong-Viec` |
| Nhiệm vụ, baseline kế hoạch | `KTC-Ke-Hoach` |
| Trạng thái, % tiến độ, minh chứng | `KTC-Theo-doi-CV` |
| Kết quả đã xác nhận theo kỳ | `KTC-Bao-Cao` |

Internet chỉ dùng để kiểm chứng hiệu lực/cập nhật văn bản hoặc khi nội bộ thiếu dữ liệu; ưu tiên nguồn
chính thống và **ghi rõ nguồn** trong kết quả. Chi tiết chỉ mục kho:
`references/02-Chi-Muc-KTC-Database.md`.

### Thứ tự ưu tiên nguồn — nguồn hạng thấp không được ghi đè nguồn hạng cao

1. Văn bản pháp luật và quy định nội bộ hiện hành **đã kiểm chứng**.
2. `SKILL.md` và các tệp `references/` của gói này.
3. **Dữ liệu vận hành thật** — báo cáo, kế hoạch đơn vị đã nộp.
4. Quy ước của Trường và tài liệu quản trị đã phê duyệt.
5. Nhật ký cập nhật, Release Notes.
6. Process Memory.
7. Suy luận mô hình.

Process Memory là dữ liệu tham khảo vận hành, **không phải căn cứ pháp lý**.

**Không suy diễn phiên bản từ tên tệp.** Trong họ skill KTC, số phiên bản *script* và số phiên bản *nghiệp vụ*
đi riêng nhau; đã có trường hợp gói có số hiệu thấp hơn lại được cập nhật muộn hơn và chứa tính năng mà gói
kia không có. Phải mở tệp đọc dòng tự khai mới kết luận.

## Bốn cạm bẫy đã biết — kiểm tra trước khi kết luận

1. **Nhầm hai lớp mã.** `A01`–`S04` là *loại* nhiệm vụ (122 mã, cố định); `KTC-2026-Q3-00125` là *lần giao
   việc* (tăng liên tục). Một mã chuẩn ứng với nhiều Task_ID. Nhầm chỗ này làm hỏng toàn bộ sổ.
2. **Danh mục nhiệm vụ chuẩn chưa đầy đủ.** 122 mã chỉ tổng hợp từ 5 Phòng; **sáu Khoa chưa có dữ liệu**
   (dự kiến bổ sung sau). Nhiệm vụ của Khoa không khớp mã nào thì **để trống** `Ma_NV_Chuan` và đề nghị bổ
   sung mã mới — **không ép về mã gần đúng**.
3. **Tên đơn vị đang tồn tại ba kiểu viết**, một kiểu sai chính tả, một kiểu bị cụt. Luôn ánh xạ về mã
   chuẩn trước khi so khớp giữa hai hệ.
4. **Chưa đối chiếu 1-1 được giữa kế hoạch và báo cáo.** Phụ lục Ia/Ib của TB736 chưa có cột `Task_ID`, nên
   hiện chỉ đối chiếu *gần đúng* theo Trục + tên nhiệm vụ. Khi báo cáo kết quả đối chiếu, **phải nói rõ đây
   là đối chiếu gần đúng**, không được trình bày như đối chiếu chính xác.

## Phân quyền ghi — không hệ nào ghi chồng lên hệ khác

| Hệ | Được ghi nhóm trường | Chỉ đọc |
|---|---|---|
| `KTC-Ke-Hoach` | A Định danh · B Nội dung · C Căn cứ · D Trách nhiệm · E Thời gian | F, G, H |
| `KTC-Theo-doi-CV` | F Tiến độ · G Kết quả | A–E |
| `KTC-Bao-Cao` | H Báo cáo | A–G |

Hai trường `Muc_Rui_Ro` và `Canh_Bao` **do hệ thống tính**, mọi giá trị nhập tay đều bị ghi đè.

## Ghi bộ nhớ vận hành sau mỗi tác vụ lớn

Sau mỗi lần chốt kỳ, dựng báo cáo, hoặc thay đổi thiết kế: ghi một mục vào bộ nhớ quá trình theo
`references/40-Process-Memory.md`. Ba nguyên tắc ghi: ghi sự việc không ghi cảm nhận · phân biệt rõ
`ĐÃ XÁC MINH` và `[CHƯA XÁC MINH]` · ghi cả lý do chứ không chỉ kết luận.

## Giới hạn theo nền tảng

Cùng một yêu cầu cho kết quả tin cậy khác nhau tùy nền tảng — xem `references/41-Gioi-Han-Nen-Tang.md`.
Tóm tắt: chỉ Claude Code đọc được thuộc tính nhị phân thật của `.docx`; trên Chat phải ghi rõ
`FORMAT_BINARY_UNVERIFIED` thay vì suy đoán.

## Quan hệ với hệ khác

- `ktc-ke-hoach`, `ktc-bao-cao` — hai hệ nghiệp vụ mà hệ này điều phối, không thay thế.
- `ktc-database` — nguồn văn bản pháp lý và quy định; **chỉ đọc**.
- `ktc-ra-soat-897` — lớp kiểm soát chất lượng **bắt buộc trước khi trình ký** kế hoạch/báo cáo.
- `ktc-soan-thao-vb` — dùng khi cần soạn thảo văn bản hành chính mới.

## Không làm gì

Không soạn thảo văn bản hành chính mới · không rà soát thể thức trình ký · không tự quyết định mức xếp
loại thay người có thẩm quyền · không tự sửa dữ liệu gốc trong kho `KTC-Database`.
