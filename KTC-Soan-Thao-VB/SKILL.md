---
name: ktc-soan-thao-vb
description: "Soan thao van ban hanh chinh moi cho Truong Cao dang Kon Tum theo tung loai van ban (Quyet dinh, Ke hoach, Thong bao, Bao cao, To trinh, Cong van, Bien ban) va tung linh vuc nghiep vu (dao tao, tuyen sinh, to chuc can bo, tai chinh, hoc sinh sinh vien, bao dam chat luong, doi ngoai). Bao gom phan tich yeu cau, tao dan y, soan thao, chuan hoa van phong, trich xuat thong tin co cau truc, gan metadata va quy trinh trinh ky - ban hanh - luu tru. Dung the thuc Nghi dinh 30/2020/ND-CP, Thong bao 597/TB-CDKT va Quyet dinh 389/QD-CDKT. KHONG dung skill nay de ra soat van ban truoc khi trinh ky (dung ktc-ra-soat-897), de dung ke hoach cong tac theo 6 Truc (dung ktc-ke-hoach), de tong hop bao cao cong tac dinh ky (dung ktc-bao-cao), hay de quan tri kho du lieu (dung ktc-database)."
---

# KTC-Soan-Thao-VB — Hệ soạn thảo văn bản hành chính

## Phiên bản: v1.1 — 14/9/2026

Kế thừa từ `KTC-DIS-Tong-Hop-VB`, **thu hẹp có chủ đích** về đúng năng lực soạn thảo.
Căn cứ quyết định: `99-Kinh-Nghiem/06-Decision-Log/DL-20260914-001-Vai-tro-KTC-DIS-Tong-Hop-VB.md`.

## Vai trò trong họ 5 Hệ thống KTC — và khi nào KHÔNG dùng hệ này

| Việc cần làm | Dùng hệ |
|---|---|
| **Soạn thảo văn bản hành chính mới** — Quyết định, Kế hoạch, Thông báo, Báo cáo, Tờ trình, Công văn, Biên bản | **Hệ này** |
| **Chuẩn hóa văn phong, tạo dàn ý, trích xuất thông tin, gắn metadata** cho một văn bản đơn lẻ | **Hệ này** |
| **Rà soát dự thảo trước khi trình ký** | `ktc-ra-soat-897` |
| **Dựng kế hoạch công tác** tháng/quý/năm theo 6 Trục | `ktc-ke-hoach` |
| **Tổng hợp báo cáo công tác** định kỳ theo 6 Trục | `ktc-bao-cao` |
| **Nạp, phân loại, gắn metadata cho kho dữ liệu** | `ktc-database` |

> **Không có hệ "làm được mọi việc".** Bản tiền nhiệm từng tự khai là "đầy đủ nhất" và hướng dẫn *"chưa rõ
> dùng hệ nào thì dùng hệ này"*. Hệ quả: nó mang một bản sao bộ quy tắc rà soát của `ktc-ra-soat-897`, và
> sau một tháng **28/28 tệp đều tụt lại sau bản gốc** — có tệp chỉ còn 357 byte so với 10.513 byte. Người
> dùng phân vân bị đẩy tới bộ quy tắc cũ nhất. Quy tắc rút ra ghi ở `references/Workflow/06-Cap-Nhat.md`
> Bước 3: **không hệ nào được sao chép bộ quy tắc của hệ khác.**

## NGUYÊN TẮC BẤT BIẾN

**Chỉ tạo kết quả sau khi đã đối chiếu thật với kho 01–04 của `KTC-Database`.** Không truy cập được kho →
**DỪNG và hỏi**, không suy diễn. Người dùng yêu cầu cứ làm → ghi ngay đầu sản phẩm:
`⚠️ Chưa đối chiếu với kho 01-04 — độ tin cậy hạn chế`.

Chi tiết: `references/Skill-Library/00-Nguyen-Tac-Chung.md`.

## Bốn nguyên tắc soạn thảo bắt buộc

Đặc tả đầy đủ: `KTC-Quan-tri/01-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`.

1. **Phát triển từ văn bản cùng loại đã ban hành**, không dựng từ mẫu trống. Mẫu trống có bố cục nhưng
   **không chứa văn phong, độ nén, cách nêu số liệu**. Thứ tự nguồn: cùng loại cùng kỳ đã ban hành →
   kỳ gần nhất trong `04-Good-Documents/` → cùng loại khác cấp → mẫu trống `.dotx` (chỉ lấy số đo).
2. **Soạn trên văn bản đã có thì bật Track Changes** và xuất phát từ chính tệp gốc — không soạn lại rồi
   trình bày như bản sửa. Quy trình: `01-Chuan-Chung/15-Skill-Track-Changes.md`; công cụ:
   `KTC-Quan-tri/tools/ktc_trackchanges.py`. Chỉ chạy được trên Claude Code.
3. **Dùng bộ quy tắc `ktc-ra-soat-897` ngay từ lúc bắt đầu viết**, không đợi bước rà soát cuối.
4. **`KTC-Database` là cơ sở dữ liệu tham mưu** — tra sâu chiến lược, đề án, kế hoạch và báo cáo chuyên đề,
   quy định nội bộ để có căn cứ; không chỉ tra một văn bản lẻ.

## Nguyên tắc đầu ra

Kết quả hoàn chỉnh **xuất `.docx`** vào `12-Output/YYYY-MM-DD/`. Dùng `python-docx` cho văn bản hành chính
có bảng, không dùng docx-js.

**Đo định dạng phải bằng script**, không suy đoán bằng mắt. Không chạy được script đo thì ghi
`FORMAT_BINARY_UNVERIFIED`.

## Quy trình xử lý một yêu cầu

1. **Xác định loại tác vụ** — soạn mới · chuẩn hóa văn phong · tạo dàn ý · trích xuất · gắn metadata.
   Nếu là *rà soát*, *dựng kế hoạch* hay *tổng hợp báo cáo* → chuyển hệ theo bảng trên, **không làm ở đây**.
2. **Xác định loại văn bản** và **lĩnh vực nghiệp vụ**.
3. **Tìm văn bản cùng loại đã ban hành** trong kho 01–04 để phát triển lên (Nguyên tắc 1).
4. **Đọc đúng skill và prompt** theo hai bảng ánh xạ dưới đây.
5. **Soạn thảo**, áp quy tắc trong tệp đã đọc + căn cứ tìm được ở bước 3.
6. **Tự kiểm** bằng `Checklist` của `ktc-ra-soat-897` trước khi giao (Nguyên tắc 3).
7. **Xuất `.docx`**, ghi đủ 3 trường trách nhiệm: nguồn dữ liệu đã dùng · người kiểm tra · trạng thái phê duyệt.
8. **Nhắc người dùng**: kết quả AI chỉ có giá trị tham khảo, không thay thế trách nhiệm người soạn thảo,
   người kiểm tra thể thức và thẩm quyền người ký. Không đưa văn bản mật hay thông tin cá nhân chưa ẩn danh
   vào xử lý.

## Bảng ánh xạ theo loại văn bản

| Loại văn bản | Skill | Prompt soạn thảo |
|---|---|---|
| Quyết định | `Skill-Library/07-Skill-Van-Ban-Quyet-Dinh.md` | `Prompt-Library/01-Soan-Thao/01-Quyet-Dinh.md` |
| Kế hoạch | `Skill-Library/08-Skill-Van-Ban-Ke-Hoach.md` | `Prompt-Library/01-Soan-Thao/02-Ke-Hoach.md` |
| Thông báo | `Skill-Library/09-Skill-Van-Ban-Thong-Bao.md` | `Prompt-Library/01-Soan-Thao/03-Thong-Bao.md` |
| Báo cáo | `Skill-Library/10-Skill-Van-Ban-Bao-Cao.md` | `Prompt-Library/01-Soan-Thao/04-Bao-Cao.md` |
| Tờ trình | `Skill-Library/11-Skill-Van-Ban-To-Trinh.md` | `Prompt-Library/01-Soan-Thao/05-To-Trinh.md` |
| Công văn | `Skill-Library/12-Skill-Van-Ban-Cong-Van.md` | `Prompt-Library/01-Soan-Thao/06-Cong-Van.md` |
| Biên bản | `Skill-Library/13-Skill-Van-Ban-Bien-Ban.md` | `Prompt-Library/01-Soan-Thao/07-Bien-Ban.md` |
| Văn bản cấp Phòng | `Skill-Library/25-Skill-Van-Ban-Cap-Phong.md` | — |
| Văn bản đối ngoại | `Skill-Library/26-Skill-Van-Ban-Doi-Ngoai.md` | `Prompt-Library/14-Van-Ban-Doi-Ngoai/` |

**Văn bản của Đảng** không xử lý ở hệ này — hệ quy chiếu B theo HD 05-HD/VPTW, **tuyệt đối không áp NĐ 30**.
Chuyển sang `ktc-ra-soat-897`, skill văn bản Đảng.

## Bảng ánh xạ theo lĩnh vực nghiệp vụ

| Lĩnh vực | Skill | Prompt (mỗi thư mục có Soạn thảo · Rà soát · Chuẩn hóa) |
|---|---|---|
| Đào tạo | `Skill-Library/20-Skill-Nghiep-Vu-Dao-Tao.md` | `Prompt-Library/08-Nghiep-Vu-Dao-Tao/` |
| Tuyển sinh | `Skill-Library/21-Skill-Nghiep-Vu-Tuyen-Sinh.md` | `Prompt-Library/09-Nghiep-Vu-Tuyen-Sinh/` |
| Tổ chức – Cán bộ | `Skill-Library/22-Skill-Nghiep-Vu-Can-Bo.md` | `Prompt-Library/10-Nghiep-Vu-Can-Bo/` |
| Tài chính | `Skill-Library/23-Skill-Nghiep-Vu-Tai-Chinh.md` | `Prompt-Library/11-Nghiep-Vu-Tai-Chinh/` |
| Học sinh, sinh viên | `Skill-Library/31-Skill-Nghiep-Vu-HSSV.md` | `Prompt-Library/12-Nghiep-Vu-HSSV/` |
| Bảo đảm chất lượng | `Skill-Library/24-Skill-Dam-Bao-Chat-Luong.md` | `Prompt-Library/13-Dam-Bao-Chat-Luong/` |

## Skill dùng chung

| Việc | Tệp |
|---|---|
| Phân tích yêu cầu trước khi soạn | `Skill-Library/05-Skill-Phan-Tich-Yeu-Cau.md` |
| Soạn thảo (khung chung) | `Skill-Library/01-Skill-Soan-Thao.md` |
| Tổng hợp nội dung từ nhiều nguồn | `Skill-Library/06-Skill-Tong-Hop-Noi-Dung.md` |
| Chuẩn hóa văn phong | `Skill-Library/04-Skill-Chuan-Hoa-Van-Ban.md` · `Prompt-Library/03-Chuan-Hoa/` |
| Tạo dàn ý trước khi soạn đầy đủ | `Prompt-Library/06-Tao-Dan-Y.md` |
| Trích xuất thông tin có cấu trúc | `Prompt-Library/04-Trich-Xuat.md` |
| Gắn metadata | `Skill-Library/00-Metadata-Schema.md` · `Prompt-Library/07-Metadata.md` |
| Phân loại nhiệm vụ vào 6 Trục | `Skill-Library/30-Skill-Phan-Loai-6-Truc.md` |
| Viện dẫn văn bản hợp nhất | `Skill-Library/Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` |
| Đề xuất quy trình trình ký | `Skill-Library/16-Skill-De-Xuat-Quy-Trinh-Trinh-Ky.md` |

## Vòng đời văn bản

`Workflow/01-Soan-Thao.md` → *(rà soát: chuyển `ktc-ra-soat-897`)* → `Workflow/03-Trinh-Ky.md` →
`Workflow/04-Ban-Hanh.md` → `Workflow/05-Luu-Tru.md`

Cập nhật chính bộ quy tắc của hệ: `Workflow/06-Cap-Nhat.md`.

## Thể thức văn bản hành chính của Trường (TB 597)

A4 · lề trên 2 – dưới 2 – trái 3 – phải 2 cm · Times New Roman **cỡ 14** · dàn đều hai lề · thụt đầu dòng
**1,27 cm** · cách đoạn ≥ 6 pt. Quốc hiệu cỡ 13 hoa đậm; tiêu ngữ cỡ 14 đậm; "Nơi nhận" cỡ 12 nghiêng đậm;
danh sách nơi nhận cỡ 11; chức vụ người ký cỡ 14 hoa đậm. Phụ lục Excel để **khổ ngang**.

Cơ quan chủ quản: `UBND TỈNH QUẢNG NGÃI` – `TRƯỜNG CAO ĐẲNG KON TUM`.

Bảng cỡ chữ đầy đủ và tên đơn vị chuẩn: `ktc-ra-soat-897` → `Checklist/08-Quy-Uoc-Rieng-CDKT.md`.

## Giới hạn thật

- Drive connector **chỉ đọc và tạo tệp mới**, không xóa hay di chuyển được tệp cũ. Xử lý `11-Input` thì phải
  liệt kê rõ tệp gốc nào người dùng cần tự xóa — **không báo "đã dọn sạch" nếu chưa thực sự xóa được**.
- Đo lề, cỡ chữ thật bằng `python-docx` **chỉ chạy được trên Claude Code**, không chạy được trên Chat/Cowork.
- Hệ này **không thay thế** bước rà soát chính thức trước khi trình ký.
