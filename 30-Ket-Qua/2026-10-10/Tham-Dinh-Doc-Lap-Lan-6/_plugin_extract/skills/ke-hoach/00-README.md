# KTC-Ke-Hoach (KTC-PIS — Planning Intelligence System)
**Phiên bản: 3.0 — 12/8/2026**

Hệ chuyên biệt thứ 3 trong kiến trúc hệ thống KTC — xây dựng kế hoạch công tác năm/quý/tháng/chuyên đề từ đề xuất nhiệm vụ của các Phòng/Khoa, theo cấu trúc 6 Trục kết quả trọng tâm (TB 817). Dùng CHUNG kho dữ liệu do `ktc-database` quản lý.

## Nội dung gói
- `SKILL.md` — cấu hình Claude Skill (v3.0)
- `references/Skill-Library/` — các Skill:
  - `00-Nguyen-Tac-Chung.md` (dùng chung)
  - `00-Metadata-Schema.md` (dùng chung)
  - `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` (dùng chung)
  - `30-Skill-Phan-Loai-6-Truc.md` (dùng chung)
  - `34-Skill-Nhan-Ke-Hoach-Preflight.md` (**MỚI** — kiểm soát cổng vào)
  - `35-Skill-Thu-Thap-De-Xuat-Don-Vi.md`
  - `36-Skill-Tong-Hop-Ke-Hoach-Truong.md`
  - `37-Skill-Doi-Chieu-Phan-Cap-Thoi-Gian.md`
- `references/Prompt-Library/16-Tong-Hop-Ke-Hoach/` — 4 Prompt:
  - `00-Preflight-Check.md` (**MỚI**)
  - `01-Thu-Thap-Kiem-Tra.md`
  - `02-Tong-Hop-Cap-Truong.md`
  - `03-Doi-Chieu-Phan-Cap.md`
- `references/Workflow/10-Tong-Hop-Ke-Hoach.md` — quy trình 7 bước (v3.0)

## Cấu trúc thư mục trên Drive (Nhap_Ke_Hoach)
- Kỳ Năm/Quý/Tháng: 13 thư mục đơn vị + `KH-Cap-Tren/` = 14 thư mục con
- Kỳ Chuyên đề: `Cong-Doan/` + `Doan-TN/` + `KH-Cap-Tren/` + `KH-Truong/` = 4 thư mục con

## Quan hệ với hệ khác
- Dùng chung dữ liệu với `ktc-database` (01-04).
- **Kế hoạch do hệ này tạo ra là căn cứ chính thức mà `ktc-bao-cao` (RIS) dùng để đối chiếu tiến độ báo cáo** — 2 hệ khép vòng Kế hoạch ↔ Báo cáo.
- Dùng `ktc-ra-soat-897` khi cần rà soát chính thức kế hoạch trước khi trình ký.

## Cài đặt
Dùng file `ktc-ke-hoach-v3.2.skill` — bấm "Save skill" trên Claude. Cần Project có kết nối Google Drive tới kho dữ liệu chung (ktc-database + KTC-Ke-Hoach).
