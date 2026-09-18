---
name: ktc-ke-hoach
description: "Thu thap, tong hop, xay dung ke hoach cong tac nam/quy/thang cua Truong Cao dang Kon Tum tu de xuat nhiem vu cua cac Phong/Khoa/Trung tam, theo cau truc 6 Truc ket qua trong tam (Thong bao 817/TB-CDKT) va mau chuan TB736. Dam bao ke hoach thang bam dung ke hoach quy, ke hoach quy bam dung ke hoach nam. Day la He KTC Planning Intelligence System (KTC-PIS). KHONG dung de soan van ban hanh chinh thong thuong hoac ra soat - dung ktc-soan-thao-vb hoac ktc-ra-soat-897 cho viec do."
---

# KTC-Ke-Hoach (KTC-PIS) — Hệ xây dựng kế hoạch công tác

> **v3.1 — cập nhật 14/9/2026.** Sửa quy trình sau đợt chạy thử kế hoạch tháng 9/2026, đối chiếu với
> `KH-834` và Kế hoạch quý III đã ban hành:
> - **Kế hoạch tháng KHÔNG gộp từ kế hoạch tháng của đơn vị** — nó là bản **chi tiết hóa Kế hoạch quý**
>   (nhiệm vụ đến hạn trong tháng) cộng nhiệm vụ phát sinh. Gộp từ dưới lên cho 94 nhiệm vụ, bản đã ban
>   hành có 53. Xem Skill 36 BƯỚC 0.
> - Chỉ giữ nhiệm vụ do **lãnh đạo cấp Trường** trực tiếp chỉ đạo (đúng 100% trên `PL-375` và `KH-834`).
> - Phân Trục/Nội hàm **theo TB 817**, không theo tên trục trong file danh mục Excel (đang lệch — `KI-011`).
> - Dựng `.xlsx` bằng cách phát triển từ bản đã ban hành; **gỡ vùng gộp ô trước khi xóa hàng**.
> - **Không tự sửa lỗi dữ liệu của đơn vị** — ghi vào cột Ghi chú.

**Phiên bản: 3.5 — 18/9/2026** — Nguyên tắc 4 — nơi lưu đầu vào, tìm KTC-Database không qua ổ đĩa, Google Drive (DL-20260918-005); `02-Cap-Truong/<nhóm kỳ>/`, văn bản cấp trên đọc tại KTC-Database/01. Trước đó 3.4: Kết cấu lại thư mục theo nhóm INPUT/PROCESS/OUTPUT (DL-20260918-004); thêm Nguyên tắc 3 — đầu vào từ tệp đính kèm cho tài khoản Team

## Vai trò trong kiến trúc tổng thể
Hệ chuyên biệt thứ 3 trong hệ thống KTC, **dùng chung** kho dữ liệu do `ktc-database` quản lý. Đối xứng ngược với `ktc-bao-cao` (RIS): PIS nhìn về tương lai (sẽ làm gì), RIS nhìn về quá khứ (đã làm được gì) — cả 2 dùng chung khung 6 Trục để Kế hoạch và Báo cáo luôn đối chiếu được với nhau.

## Nguyên tắc bắt buộc — ĐỌC TRƯỚC KHI LÀM BẤT KỲ VIỆC GÌ
Đọc `references/Skill-Library/00-Nguyen-Tac-Chung.md`. Hai nguyên tắc cốt lõi:
1. **Bắt buộc đối chiếu kho 01-04** (ktc-database) — nếu không có kết nối Google Drive connector → Skill 34 báo FAIL ngay, DỪNG.
2. **Bắt buộc xuất kết quả cuối thành file .docx** lưu vào `30-Ket-Qua/YYYY-MM-DD/<loại thao tác>/`
   — nơi xuất DUY NHẤT của toàn dự án (`20-Chuan-Chung/00-Nguyen-Tac-Chung.md`). Thư mục riêng
   `Xuat_Ke_Hoach/` **đã bỏ** ngày 14/9/2026.

## Nguyên tắc khai thác Internet
Đọc `references/Skill-Library/04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md`. Chỉ chấp nhận nguồn Mức 1–2. Bắt buộc ghi trường metadata thứ 12. KHÔNG tự nạp — phải xác nhận trước.

## Quy trình 7 bước
Đọc `references/Workflow/10-Tong-Hop-Ke-Hoach.md`.

| Bước | Skill / Prompt | Nội dung |
|---|---|---|
| **0** | Skill 34 / Prompt 00 | **Pre-flight Check** — kiểm soát cổng vào, phân kỳ định kỳ vs chuyên đề |
| 1 | — | Thu thập đề xuất theo kỳ vào `10-Dau-Vao/01-Dau-Moi-Nop/<kỳ>/` |
| 2 | Skill 35 / Prompt 01 | Kiểm tra đề xuất đơn vị, gắn Trục/Nội hàm |
| 3 | Skill 36 / Prompt 02 | Tổng hợp thành Kế hoạch cấp Trường |
| 4 | Skill 37 / Prompt 03 | Đối chiếu phân cấp thời gian (tháng↔quý↔năm) |
| 5 | ktc-ra-soat-897 | **Rà soát bắt buộc trước khi trình ký** — chốt chặn, không bỏ qua |
| 6 | — | Xuất .docx → lưu `30-Ket-Qua/YYYY-MM-DD/<loại thao tác>/` |

**Bước 0 bắt buộc — có quyền CHẶN toàn bộ:** FAIL → không chạy Bước 2.

## 4 Skill của hệ PIS
| Skill | Prompt tương ứng | Chức năng |
|---|---|---|
| **34**-Skill-Nhan-Ke-Hoach-Preflight | `16-Tong-Hop-Ke-Hoach/00-Preflight-Check.md` | Kiểm soát cổng vào — phân biệt kỳ định kỳ vs chuyên đề |
| 35-Skill-Thu-Thap-De-Xuat-Don-Vi | `.../01-Thu-Thap-Kiem-Tra.md` | Kiểm tra đề xuất đơn vị đủ mẫu, gắn Trục/Nội hàm |
| 36-Skill-Tong-Hop-Ke-Hoach-Truong | `.../02-Tong-Hop-Cap-Truong.md` | Gộp nhiều đơn vị thành Kế hoạch Trường |
| 37-Skill-Doi-Chieu-Phan-Cap-Thoi-Gian | `.../03-Doi-Chieu-Phan-Cap.md` | Đối chiếu tháng↔quý↔năm |

Cả 4 dùng `30-Skill-Phan-Loai-6-Truc.md` (6 Trục, 38 nội hàm, TB 817).

---

## Dữ liệu đầu vào — kho dùng chung `10-Dau-Vao/`

> **[SỬA 14/9/2026]** Thư mục riêng `Nhap_Ke_Hoach/input-KH_*` **đã bỏ**. Đầu vào của mọi hệ nay nằm chung
> ở `10-Dau-Vao/` cấp dự án. Đọc `10-Dau-Vao/00-README.md` trước khi chạy Bước 0.

| Nhánh | Chứa gì | Luồng |
|---|---|---|
| `01-Dau-Moi-Nop/<kỳ>/<mã>/` | Hồ sơ 13 đầu mối nộp theo kỳ | **A** |
| `02-Cap-Truong/<nhóm kỳ>/<kỳ>/` | Văn bản cấp Trường đã ban hành — CTCT năm, KH quý, KH tháng, BC | **B** · nguồn 1 |
| `KTC-Database/01-Legal-Database/` (nạp qua `KTC-Database/11-Input/`) | Văn bản chỉ đạo của UBND tỉnh, Tỉnh ủy, Bộ… — **không** lưu trong `10-Dau-Vao` | **B/C** · nguồn 2 |
| `03-Ket-Luan-Giao-Ban/<năm>/` | Thông báo kết luận giao ban tuần của Lãnh đạo Trường | nguồn 3 |

> `<nhóm kỳ>` của `02-Cap-Truong/`: `01-Nam/` (kỳ `YYYY`) · `02-Quy/` (`YYYY-Qn`) · `03-Thang/` (`YYYY-MM`) · `04-Chuyen-De/` (`YYYY-CD-<tên-ngắn>`). Văn bản cấp trên **không** lưu ở `10-Dau-Vao` — đọc tại `KTC-Database/01-Legal-Database/` (DL-20260918-005).


**Tên kỳ:** năm `YYYY` · quý `YYYY-Qn` · tháng `YYYY-MM` · chuyên đề `YYYY-CD-<tên-ngắn>`.

**13 mã đầu mối:** `P-THHC` `P-TCCB` `P-QLDT` `P-TCKT` `P-QLKH` `K-YDUOC` `K-KTCN` `K-KTNL` `K-SUPH`
`K-KHCB` `K-DTSHLX` `DT-CDCS` `DT-DTN` — dùng mã chuẩn, không ghi tên tự do
(`20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`).

**Kỳ chuyên đề** chỉ nhận hồ sơ của `DT-CDCS`, `DT-DTN`, dự thảo cấp Trường và văn bản cấp trên — 5 Phòng
và 6 Khoa chuyên môn **không** nộp đề xuất riêng.

> ⚠️ **Thư mục rỗng không còn là dấu hiệu "chưa nộp".** Kho mới chỉ tạo thư mục khi có dữ liệu; đầu mối
> chưa nộp thì **không có thư mục**. Bước 0 phải đối chiếu với danh sách 13 mã, không đếm thư mục đang có.

## 3 Luồng tiếp nhận

| Luồng | Nội dung | Vị trí | Tên file |
|---|---|---|---|
| **A** | Đề xuất mới (chưa ban hành) | `01-Dau-Moi-Nop/<kỳ>/<mã>/` | `DX_[kỳ]_[kỳ-cụ-thể]_[mã]_v[N].docx` |
| **B** | KH đã ban hành (dùng Skill 37) | `KH-Cap-Tren/` | `KH_[kỳ]_[kỳ-cụ-thể]_[Don-vi-BH]_[So-hieu].docx` |
| **C** | Nhập hồi tố | `KH-Cap-Tren/` | `KH_..._HOITRO.docx` |

**Định dạng chấp nhận:** `.docx` và `.xlsx` chỉ — từ chối `.pdf` scan, `.md`, `.txt`, ảnh.

## Metadata bắt buộc (Luồng B/C)
Theo `00-Metadata-Schema.md` — ghi vào đầu file hoặc file `.md` đi kèm:
- Trạng thái: Đã ban hành | Số hiệu | Ngày ký | Đơn vị ban hành
- Phạm vi kỳ | Nguồn gốc nạp
- (Luồng C thêm) Ghi chú nạp: "Nhập hồi tố ngày [dd/mm/yyyy]"

## Kết nối ktc-database (01-04)
| Thư mục | Dùng để làm gì trong PIS |
|---|---|
| `01-Legal-Database` | Xác định luật/nghị định làm căn cứ pháp lý cho kế hoạch |
| `02-KTC-Regulations` | Đối chiếu quy chế nội bộ Trường (TB 817, TB 736, HD 02-HD/BTCTW...) |
| `03-Templates` | Lấy mẫu TB736 (Phụ lục Ia/Ib) kiểm tra đề xuất đơn vị |
| `04-Good-Documents` | Tham chiếu kế hoạch tốt đã ban hành — đảm bảo nhất quán văn phong |

## Liên hệ với KTC-Bao-Cao (RIS)
`30-Ket-Qua/YYYY-MM-DD/` là **căn cứ chính thức** cho `ktc-bao-cao` đối chiếu tiến độ báo cáo — 2 hệ khép vòng Kế hoạch ↔ Báo cáo.

## Giới hạn
- Không soạn thảo văn bản hành chính, không rà soát chính thức (dùng `ktc-soan-thao-vb` / `ktc-ra-soat-897`).
- Không tổng hợp báo cáo (dùng `ktc-bao-cao`).
- Không tự quyết định đơn vị chủ trì khi chồng chéo nhiệm vụ.
- Không tự cho phép bỏ qua Pre-flight FAIL — chỉ Trưởng phòng TH-HC&QT xác nhận PASS-PARTIAL.
