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

## Runtime support (mô tả theo năng lực — chưa có biên bản nghiệm thu Claude, Cowork)

- **Claude Code:** đầy đủ skill + agent + hook + script trong `scripts/`; nền tảng **đã kiểm thử đầy đủ** (đo lề/cỡ
  chữ thật từ `.docx`, Track Changes mức OOXML, hook chặn ghi).
- **Cowork:** skill + agent + hook + connector + thư mục người dùng chọn; hook cần Python trên máy. Chưa nghiệm thu.
- **Claude (trò chuyện):** chỉ skill (không hook, không agent); script đi kèm skill chạy được khi môi trường thực thi mã
  được bật — chưa kiểm chứng; không có thao tác chặn ghi. Chưa nghiệm thu (xem `KI-010`, `KI-019`).

## Chuẩn chung trong mọi skill và agent (1.3.0)

Khối **quy tắc bất biến, ranh giới dữ liệu, khuôn đầu ra 6 trạng thái** (`DAT` · `DAT_CO_DIEU_KIEN` · `CAN_BO_SUNG` ·
`CAN_XAC_MINH` · `DUNG` · `KHONG_DAT`) được chèn khi dựng từ bản gốc
`20-Chuan-Chung/20-Quy-Tac-Bat-Bien-Va-Khuon-Dau-Ra.md` vào 8 `SKILL.md` và 7 agent. Đây là **chính sách mô hình**;
lớp thực thi ở ranh giới công cụ là guard dưới đây.

## Hooks

| Sự kiện | Script | Việc |
|---|---|---|
| `SessionStart` | `ktc_quan_tri_doctor.py` | In phiên bản; **tự thử guard** (báo HOẠT ĐỘNG / CHƯA HOẠT ĐỘNG); báo Python, KTC-Database, thư viện docx/openpyxl |
| `SessionStart` | `ktc_nhat_ky.py nap` | Nạp tóm tắt nhật ký 2 ngày + tri thức tự học; **xóa nhật ký cũ hơn 30 ngày** |
| `PreToolUse` | `ktc_guard.py` | **Chặn ghi, xóa** `KTC-Database`, `03-Templates(1)`, `04-Good-Documents` (Write, Edit, MultiEdit, NotebookEdit, lệnh shell Bash/PowerShell) |
| `UserPromptSubmit` | `ktc_nhat_ky.py yeu-cau` | **Mặc định chỉ ghi độ dài + nhãn tín hiệu học**; nội dung (≤ 600 ký tự, đã che số định danh, số điện thoại, email) chỉ khi chọn: mở đầu `#học`, hoặc chủ máy đặt `KTC_NHAT_KY_NOI_DUNG=1` (khi đó chỉ ghi lời có tín hiệu học); `#riêng` không ghi |
| `PostToolUse` | `ktc_nhat_ky.py ghi` | Ghi 1 dòng mỗi thao tác Write/Edit/Bash/PowerShell/Skill/Agent (không ghi nội dung tệp) |
| `PostToolUse` | `ktc_the_thuc_hook.py` | Đo thể thức tệp .docx/.xlsx vừa ghi |
| `SessionEnd` | `ktc_nhat_ky.py ket-phien` | Đánh dấu kết thúc phiên |

Nhật ký: `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/YYYY-MM-DD.jsonl` — **không đưa lên git** (`CP-20260924-001`).
Chỉ ghi khi đang làm việc trong KTC-Quan-tri.

## Guard chặn ghi — phạm vi và giới hạn

- **Fail-closed** khi chạy được: dữ liệu hook hỏng hoặc lỗi nội bộ → chặn (mã 2).
- **Giới hạn đã biết:** (1) không phân tích mã Python/JS nhúng trong lệnh shell — script tự ghi vào kho thì guard
  không thấy; (2) máy không có Python thì hook không chạy được — doctor báo "guard: CHƯA HOẠT ĐỘNG", khi đó không
  được coi là có bảo vệ ghi; (3) Claude (trò chuyện) không có hook. Phân quyền chỉ đọc trên Google Drive vẫn là
  lớp bảo vệ chính.
- Ca thử: `92-Kinh-Nghiem/02-Regression/Cases/test_plugin_130.py` (14 ca chặn, 7 ca cho qua, 2 ca fail-closed).

## Sao lưu GitHub — KHÔNG thuộc plugin (từ 1.3.0)

Plugin **không còn** hook sao lưu. Sao lưu là tác vụ theo lịch của quản trị viên trên máy phát triển: Task Scheduler
`KTC-Quan-tri-Backup-GitHub` 21:00 chạy `29-Cong-Cu/plugin_src/scripts/ktc_backup_github.py` (script này không đóng
vào plugin). Commit + push thường, không force-push; dừng nếu tệp có tên giống bí mật **hoặc nội dung có số định danh
cá nhân**. Xem lần cuối: `python 29-Cong-Cu/plugin_src/scripts/ktc_backup_github.py --trang-thai`.

## Xác thực

`claude plugin validate ./31-Plugin --strict` — **ĐẠT** 26/9/2026 với bản 1.3.0 (`claude.exe` 2.1.283 đi kèm extension
VS Code). Bản 1.2.1 **không đạt** với CLI 2.1.283 do mô tả agent `ktc-kiem-san-pham` làm hỏng YAML (đã sửa, và
`dong_goi_plugin.py` nay tự chặn). Chạy lại sau mỗi lần dựng. Bằng chứng kiểm thử từng bản:
`30-Ket-Qua/<ngày>/Plugin/BANG-CHUNG-KIEM-THU-<phiên bản>.md`.

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
