# KTC-Quan-tri Plugin

Plugin Claude Code/Cowork cho chu trình quản trị nhiệm vụ khép kín của Trường Cao đẳng Kon Tum:
Kế hoạch → Theo dõi → Kết quả/Bằng chứng → Báo cáo, kèm soạn thảo văn bản hành chính, chuẩn thể thức và KPI cá
nhân theo QĐ 1923/QĐ-CĐKT.

**Phiên bản hiện hành: xem `.claude-plugin/plugin.json` và `CHANGELOG.md`** — README không ghi số phiên bản để
khỏi lệch.

**Nguồn dựng:** các gói `.skill` hiện hành mà `29-Cong-Cu/kiem_tra_he_thong.py` kiểm (danh sách `GOI_NGUON` trong
`29-Cong-Cu/dong_goi_plugin.py`) — không dựng lại từ đầu, không đọc lại nguồn rời, tránh lệch bản giữa hai đường
đóng gói (`DL-20260918-001`).

## 8 skill trong plugin

| Skill | Vai trò |
|---|---|
| `quan-tri` | Điều phối, định tuyến tác vụ, chuẩn chung (Task_ID, mã đơn vị, 6 Trục), quy đổi KPI và xếp loại |
| `ke-hoach` | Tổng hợp kế hoạch công tác năm/quý/tháng (KTC-PIS) |
| `theo-doi-cv` | Theo dõi vòng đời nhiệm vụ, cảnh báo, minh chứng (control tower) |
| `bao-cao` | Tổng hợp báo cáo công tác tháng/quý/6 tháng/năm (KTC-RIS) |
| `soan-thao-vb` | Soạn thảo văn bản hành chính mới (7 loại × 6 lĩnh vực nghiệp vụ) |
| `the-thuc` | Chuẩn thể thức mọi sản phẩm .docx/.xlsx (dùng kèm skill docx/xlsx) |
| `kpi-lap-ke-hoach` | Lập kế hoạch và danh mục KPI cá nhân đầu quý (6 nhóm vị trí) |
| `kpi-tu-danh-gia` | Tự đánh giá, đề xuất xếp loại cá nhân cuối quý — chỉ đề xuất, không quyết định |

Gọi bằng `<tên-plugin>:<tên-skill>`, ví dụ `ktc-quan-tri:bao-cao`.

## 7 agent

| Agent | Việc |
|---|---|
| `ktc-tu-hoc` | Rút tri thức từ nhật ký (sửa sai, quy ước, quyết định) vào `TRI-THUC.md` |
| `ktc-tu-cai-tien` | Viết đề xuất cải tiến `CP-...` chờ duyệt — không tự sửa |
| `ktc-kiem-ho-so-don-vi` | Kiểm hồ sơ kế hoạch/báo cáo đơn vị nộp (Phụ lục TB 736) |
| `ktc-tra-cuu-can-cu` | Tra căn cứ, chủ trương trong KTC-Database |
| `ktc-kiem-san-pham` | Kiểm tra cuối, độc lập sản phẩm .docx/.xlsx trước khi giao |
| `ktc-hieu-luc-vien-dan` | Quét hiệu lực và cách viện dẫn văn bản |
| `ktc-xac-minh-minh-chung` | Kiểm sơ bộ minh chứng trước khi chốt kỳ |

## Runtime support

- **Claude Code:** đầy đủ skill + agent + hook + script trong `scripts/`. Nền tảng duy nhất chạy được Track Changes
  mức OOXML và đo lề/cỡ chữ thật từ `.docx`.
- **Cowork:** skill + subagent + connector + công cụ tệp cục bộ khi được cấp quyền; hook `SessionStart` chạy được.
- **Claude Chat:** chưa thử nghiệm qua đường plugin (xem `KI-010`). Kích hoạt hai skill KPI mới thử bằng Claude Code
  headless (`28-KTC-KPI/TEST-REPORT.md` mục 4.3).

## Hooks

| Sự kiện | Script | Việc |
|---|---|---|
| `SessionStart` | `ktc_quan_tri_doctor.py` | In phiên bản plugin và phiên bản tự khai của từng skill |
| `SessionStart` | `ktc_nhat_ky.py nap` | Nạp tóm tắt nhật ký 2 ngày + tri thức tự học vào context |
| `SessionStart` | `ktc_backup_github.py --neu-can` | Backup bù nếu đã quá 24h (chỉ khi từng push thành công) |
| `UserPromptSubmit` | `ktc_nhat_ky.py yeu-cau` | Ghi lời người dùng (≤ 600 ký tự) + tín hiệu học; bắt đầu `#riêng` thì không ghi nội dung |
| `PostToolUse` | `ktc_nhat_ky.py ghi` | Ghi 1 dòng mỗi thao tác Write/Edit/Bash/PowerShell/Skill/Agent (không ghi nội dung tệp) |
| `PostToolUse` | `ktc_the_thuc_hook.py` | Đo thể thức tệp .docx/.xlsx vừa ghi |
| `SessionEnd` | `ktc_nhat_ky.py ket-phien` | Đánh dấu kết thúc phiên |

Nhật ký: `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/YYYY-MM-DD.jsonl` — **không đưa lên git** (`CP-20260924-001`).
Chỉ ghi khi đang làm việc trong KTC-Quan-tri.

## Backup GitHub hằng ngày

Task Scheduler `KTC-Quan-tri-Backup-GitHub` chạy 21:00 (chạy bù khi máy bật lại). Commit + push thường, không bao
giờ force-push. Dừng nếu phát hiện tệp tên giống bí mật. Trạng thái: `.git/ktc-backup.json`. Xem lần cuối:
`python 29-Cong-Cu/plugin_src/scripts/ktc_backup_github.py --trang-thai`.

## Không có guard chặn ghi

**Không có** `PreToolUse` guard chặn ghi `KTC-Database` — plugin `ktc-ra-soat-897` cung cấp guard đó khi được cài
cùng. Chạy plugin này một mình thì quy ước "kho chỉ đọc" trong `CLAUDE.md` vẫn có hiệu lực, nhưng **không được hook
chặn tự động**.

## Xác thực — ĐẠT

`claude plugin validate ./31-Plugin --strict` chạy được từ 25/9/2026 (bản 1.2.0, `claude.exe` đi kèm extension VS
Code) — **Validation passed**. Chạy lại sau mỗi lần dựng; `dong_goi_plugin.py` tự chặn mô tả plugin > 500 ký tự và mô
tả skill > 1024 ký tự.

## Build lại

```bash
python 29-Cong-Cu/dong_goi_plugin.py
```

Chạy từ gốc dự án `KTC-Quan-tri`. Script chỉ dọn và dựng lại các thư mục sinh tự động (`skills/`, `.claude-plugin/`,
`hooks/`, `scripts/`, `agents/`) — **không đụng tới** `README.md`/`CHANGELOG.md` này (viết tay) và không sửa tay tệp
nào trong `31-Plugin/skills/`.

## Cập nhật bản đã cài trên máy

Bản cài cục bộ nằm ở `~/.claude/ktc-marketplace/ktc-quan-tri` (marketplace `ktc-local`) và **không tự cập nhật** khi
build. Kiểm: dòng đầu banner `SessionStart doctor` in phiên bản plugin. Cập nhật: chép đè thư mục `31-Plugin` vào
đó (xóa bản cũ trước), rồi mở phiên mới. Hoặc cài từ marketplace GitHub `nnqp201-sys/KTC-Quan-tri`.
