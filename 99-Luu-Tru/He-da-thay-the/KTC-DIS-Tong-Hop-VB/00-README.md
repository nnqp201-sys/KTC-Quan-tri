# KTC-Tong_hop_VB

Hệ tổng hợp, đầy đủ nhất trong họ 5 Hệ thống KTC — 30 skill, 47 prompt, hỗ trợ toàn bộ tác vụ soạn thảo/rà soát/chuẩn hóa/nghiệp vụ chuyên ngành/văn bản Đảng. Dùng CHUNG kho dữ liệu do `ktc-database` quản lý.

## Vị trí trong họ 5 hệ
1. `ktc-database` — quản trị kho dữ liệu nền 01-04 + Input/Output.
2. `ktc-ra-soat-897` — CHỈ rà soát/so sánh/chuẩn hóa (gọn, chuyên biệt).
3. `ktc-ke-hoach` (PIS) — kế hoạch công tác theo 6 Trục.
4. `ktc-bao-cao` (RIS) — báo cáo công tác theo 6 Trục.
5. **`ktc-dis-tong-hop-vb`** (gói này) — đầy đủ nhất, dùng khi việc phức tạp hoặc chưa rõ nên dùng hệ nào trong 3 hệ chuyên biệt (2-4).

## Nội dung gói
- `SKILL.md`
- `references/Prompt-Library/` — 47 prompt (theo 7 loại văn bản + 7 lĩnh vực nghiệp vụ + Mẫu 897)
- `references/Skill-Library/` — 30 skill + Nguyên tắc chung + Metadata Schema + Nguyên tắc nạp Internet (dùng chung)
- `references/Workflow/`, `references/Checklist/`, `references/Knowledge-Graph/`, `references/Input-Output/`
- `assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897-goc.docx`

## Cài đặt
Dùng file `.skill` riêng (`ktc-dis-tong-hop-vb.skill`) — bấm "Save skill". Vẫn cần Project có kết nối Google Drive tới kho dữ liệu chung (nay là thư mục `KTC-Database` sau khi tách).

## Lịch sử đổi tên
Đây là bản đổi tên/chuẩn hóa của Skill `ktc-van-ban` (tên cũ) để khớp họ tên với 4 hệ còn lại, sau khi kiến trúc được tách thành 5 hệ (10/8/2026).
