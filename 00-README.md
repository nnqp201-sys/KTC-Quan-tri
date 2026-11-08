# KTC-Quan-tri
## Dự án hợp nhất quản trị nhiệm vụ — Trường Cao đẳng Kon Tum

Hợp nhất ba hệ **Kế hoạch – Theo dõi – Báo cáo** thành một chu trình khép kín, dữ liệu dùng chung, truy vết
được từ chủ trương đến kết quả cuối cùng:

> Chủ trương/Văn bản → Nhiệm vụ → Kế hoạch → Giao việc → Theo dõi → Kết quả/Bằng chứng → Báo cáo → Đánh giá → Điều chỉnh kế hoạch

Mục tiêu cuối: **một nhiệm vụ – một mã – một dòng dữ liệu gốc – một lịch sử – nhiều góc nhìn.**

## Cấu trúc

```
KTC-Quan-tri/
├── CLAUDE.md · 00-README.md · README.md
│
├── INPUT     10-Dau-Vao/ · 11-Du-lieu-Cong-Viec/
├── PROCESS   20-Chuan-Chung/ · 21-Master-Task-Register/ · 22-KTC-Dieu-Phoi/ (skill ktc-quan-tri)
│             23-KTC-Ke-Hoach/ · 24-KTC-Theo-doi-CV/ · 25-KTC-Bao-Cao/ · 26-KTC-Soan-Thao-VB/ · 2A-KTC-Ra-Soat-897/ (ktc-ra-soat-897 v4.5 cá nhân) · 29-Cong-Cu/
├── OUTPUT    30-Ket-Qua/YYYY-MM-DD/ · 31-Plugin/
└── QUẢN TRỊ  90-Nhat-Ky-Van-Hanh/ · 91-Tai-Lieu-Thiet-Ke/ · 92-Kinh-Nghiem/ · 99-Luu-Tru/
```

## Đọc theo thứ tự này

| # | Tài liệu | Để biết |
|---|---|---|
| 1 | `CLAUDE.md` | Quy ước làm việc, nguyên tắc bất biến, cách liên kết `KTC-Database` |
| 2 | `91-Tai-Lieu-Thiet-Ke/Ke-hoach-hop-nhat-KTC-Ke-Hoach-KTC-Bao-Cao-KTC-Theo-Doi.md` | Kiến trúc hợp nhất, lộ trình 6 giai đoạn — tài liệu điều khiển chính |
| 3 | `20-Chuan-Chung/11-Quy-Tac-Task-ID.md` | Phân biệt Task_ID với mã nhiệm vụ chuẩn — nhầm chỗ này là hỏng gốc |
| 4 | `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` | 11 mã đơn vị và mức lệch dữ liệu đang có |
| 5 | `21-Master-Task-Register/00-README.md` | Bộ 46 trường, phân quyền ghi, việc cần xong trước v1.0 |
| 6 | `91-Tai-Lieu-Thiet-Ke/Mo-Ta-Chi-Tiet-He-hệ thống KTC-...md` | Toàn cảnh 5 Hệ thống KTC, khác biệt Chat/Cowork/Code |

**Mở đầu mỗi phiên làm việc:** đọc `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md` trước tiên — sự thật vận hành hiện
hành, phiên bản đang dùng, thứ tự ưu tiên nguồn. Việc đang mở xem
`92-Kinh-Nghiem/05-Known-Issues/Pending.md`.

## Gói Claude Skill cấp dự án

`ktc-quan-tri.skill` (v1.0 — 13/9/2026) chạy trực tiếp trên Claude Chat và Cowork, phủ 5 tác vụ: chuẩn hóa
và cấp Task_ID · theo dõi và cảnh báo · đối chiếu ba hệ · chốt kỳ và dựng báo cáo · quy đổi KPI và xếp loại.

Cài bằng nút **Save skill** trên Claude. Gói **không mang theo dữ liệu** — vẫn cần Project kết nối Google
Drive tới `KTC-Quan-tri/` và `KTC-Database/`.

`22-KTC-Dieu-Phoi/SKILL.md` là **bản tham chiếu**; bản chính thức nằm trong gói `.skill`. Bốn tệp tham chiếu `12`,
`20`, `21`, `22` trong gói là bản sao của `20-Chuan-Chung/` — sửa ở bản gốc trước, rồi đóng gói lại.

## Nguồn dữ liệu ngoài dự án

- **`../KTC-Database`** — kho nền pháp lý và quy định dùng chung (519 tệp pháp lý, 244 quy định nội bộ).
  **Chỉ đọc**, hook chặn ghi. Điểm vào: `KTC-DIS-Master-Index_20260830_v1.2.xlsx`.
- **`2A-KTC-Ra-Soat-897/`** (trong dự án) — bản tích hợp cá nhân của `ktc-ra-soat-897` **v4.5** (lõi nguyên bản TB 1206/TB-CĐKT + lớp bổ sung): lớp kiểm soát chất lượng bắt buộc **trước khi trình ký**.

## Trạng thái hiện tại

**Đã phát hành chính thức:** TB 1153/TB-CĐKT ngày 12/10/2026.

- **Plugin `ktc-quan-tri` 1.4.2** — 8 skill, 38 agent, hook chặn ghi kho chuẩn + nhật ký + đo thể thức.
- **`ktc-ra-soat-897` v4.6.4** — bản chính thức toàn Trường.
- Phân phối qua tài khoản `phongthhcqt`, cài từ marketplace `ktc-local`.

Trạng thái chi tiết: `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`. Việc đang mở: `92-Kinh-Nghiem/05-Known-Issues/Pending.md`.
