# KTC-Bao-Cao (KTC-RIS — Report Intelligence System)
## Phiên bản: v2.0 — cập nhật 12/08/2026

Hệ chuyên biệt thứ 4 trong kiến trúc hệ thống KTC — tổng hợp báo cáo công tác tháng/quý/6 tháng/năm từ báo cáo các Phòng/Khoa/Trung tâm, theo cấu trúc 6 Trục kết quả trọng tâm (TB 817). Dùng CHUNG kho dữ liệu do `ktc-database` quản lý.

## Nội dung gói

- `SKILL.md` — cấu hình Claude Skill (v2.0: 4 skill, 7 bước, có nhánh fallback)
- `references/Skill-Library/` — 00-Nguyen-Tac-Chung, 00-Metadata-Schema, 04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet (dùng chung) + 30-Skill-Phan-Loai-6-Truc (dùng chung) + **4 skill riêng của RIS**: 32 (Thu thập-kiểm tra), 33 (Tổng hợp cấp Trường), 34 (Đối chiếu tiến độ — có fallback A/B/C), **35 (Quản lý Checklist đơn vị — MỚI)**
- `references/Prompt-Library/15-Tong-Hop-Bao-Cao/` — **4 prompt** tương ứng 4 skill trên
- `references/Workflow/09-Tong-Hop-Bao-Cao.md` — quy trình **7 bước** (v2.0)

## Quy trình tóm tắt (7 bước)

| Bước | Mô tả | Skill |
|------|-------|-------|
| 0 | Lập Checklist đơn vị đầu kỳ | 35 |
| 1 | Tiếp nhận báo cáo đơn vị | — |
| 2 | Kiểm tra đủ mẫu/kỳ, gắn Trục/Nội hàm | 32 |
| 3 | Tổng hợp cấp Trường theo 6 Trục | 33 |
| 4 | Đối chiếu Kế hoạch cùng kỳ (fallback A/B/C nếu thiếu) | 34 |
| 5 | **Rà soát bắt buộc trước khi trình ký** — chốt chặn, không bỏ qua | ktc-ra-soat-897 |
| 6 | Xuất .docx + 3 trường trách nhiệm | Nguyên tắc 2 |
| 7 | Checklist kết thúc kỳ, liệt kê file cần xóa thủ công | 35 |

## Quan hệ với hệ khác

- Dùng chung dữ liệu với `ktc-database` (01-04, Input/Output) — điều kiện tiên quyết bắt buộc.
- **Skill 34 cần Kế hoạch cùng kỳ do `ktc-ke-hoach` (PIS) tạo ra** — nếu thiếu, hỏi người dùng 3 lựa chọn [A/B/C], không tự dừng cứng.
- Dùng `ktc-ra-soat-897` khi cần rà soát chính thức báo cáo trước khi trình ký.

## Cài đặt

Dùng file `.skill` đóng gói riêng (`ktc-bao-cao.skill`) — bấm "Save skill" trên Claude. Vẫn cần Project có kết nối Google Drive tới kho dữ liệu chung.

## Lưu ý vận hành

- AI chỉ **tạo** file mới trên Drive — không thể sửa, di chuyển hoặc xóa file đã có.
- Sau mỗi kỳ: xóa thủ công file gốc trong `11-Input` / `13-Unit-Reports` theo danh sách Skill 35 Tác vụ D liệt kê.
