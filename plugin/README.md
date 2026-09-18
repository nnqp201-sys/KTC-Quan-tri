# KTC-Quan-tri Plugin

Plugin Claude Code/Cowork cho chu trình quản trị nhiệm vụ khép kín của Trường Cao đẳng Kon Tum:
Kế hoạch → Theo dõi → Kết quả/Bằng chứng → Báo cáo, kèm hệ soạn thảo văn bản hành chính.

**Nguồn dựng:** 5 gói `.skill` hiện hành theo `tools/kiem_tra_he_thong.py` (xem
`99-Kinh-Nghiem/06-Decision-Log/DL-20260918-001-...md` trong repo dự án) — không dựng lại từ đầu, không
đọc lại nguồn rời, để tránh nguy cơ lệch bản giữa hai đường đóng gói song song.

## 5 skill trong plugin

| Skill | Vai trò |
|---|---|
| `quan-tri` | Điều phối, định tuyến 5 tác vụ, chuẩn chung (Task_ID, mã đơn vị, 6 Trục) |
| `bao-cao` | Tổng hợp báo cáo công tác tháng/quý/6 tháng/năm (KTC-RIS) |
| `ke-hoach` | Tổng hợp kế hoạch công tác năm/quý/tháng (KTC-PIS) |
| `soan-thao-vb` | Soạn thảo văn bản hành chính mới (7 loại × 6 lĩnh vực nghiệp vụ) |
| `theo-doi-cv` | Theo dõi vòng đời nhiệm vụ, cảnh báo, minh chứng (control tower) |

Gọi bằng `<tên-plugin>:<tên-skill>`, ví dụ `ktc-quan-tri:bao-cao`.

## Runtime support

- **Cowork:** Skills + subagents + connectors + local file tools khi được cấp quyền. Hook `SessionStart`
  chạy được.
- **Claude Code:** Đầy đủ Skills + hooks + script trong `scripts/`. Đây là nền tảng duy nhất chạy được
  `skills/soan-thao-vb/references/Skill-Library/ktc_trackchanges.py` (thao tác Track Changes mức OOXML,
  cần `python-docx`) và đo lề/cỡ chữ thật từ `.docx`.
- **Claude Chat:** chưa thử nghiệm qua đường plugin này (Chat trước nay dùng đường Skill rời từng hệ, xem
  `KI-010` trong repo dự án — chưa có nhật ký đợt chạy đó).

## Agent

`ktc-tu-cai-tien` — agent tự cải tiến. Gọi khi muốn hệ "rút kinh nghiệm": nói *"chạy agent tự cải tiến"*.
Chỉ viết đề xuất `CP-...` *Chờ duyệt* vào `99-Kinh-Nghiem/03-Change-Proposals/`, không tự sửa gì.

## Hooks

| Sự kiện | Script | Việc |
|---|---|---|
| `SessionStart` | `ktc_quan_tri_doctor.py` | In phiên bản tự khai 5 skill |
| `SessionStart` | `ktc_nhat_ky.py nap` | Nạp tóm tắt nhật ký 2 ngày gần nhất vào context |
| `SessionStart` | `ktc_backup_github.py --neu-can` | Backup bù nếu đã quá 24h (chỉ khi từng push thành công) |
| `PostToolUse` | `ktc_nhat_ky.py ghi` | Ghi 1 dòng log mỗi thao tác Write/Edit/Bash/Skill/Agent |
| `SessionEnd` | `ktc_nhat_ky.py ket-phien` | Đánh dấu kết thúc phiên |

Nhật ký: `03-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/YYYY-MM-DD.jsonl` — chỉ tên công cụ và đường dẫn/lệnh (cắt
200 ký tự), không ghi nội dung tệp. Chỉ ghi khi đang làm việc trong KTC-Quan-tri.

## Backup GitHub hằng ngày

Task Scheduler `KTC-Quan-tri-Backup-GitHub` chạy 21:00 (chạy bù khi máy bật lại). Commit + push thường,
không bao giờ force-push. Dừng nếu phát hiện tệp tên giống bí mật. Trạng thái: `.git/ktc-backup.json`.
Xem lần cuối: `python tools/plugin_src/scripts/ktc_backup_github.py --trang-thai`.

## Không có guard chặn ghi

**Không có** `PreToolUse` guard chặn ghi `KTC-Database` — plugin `ktc-ra-soat-897` đã
cung cấp guard đó khi được cài cùng; nếu chạy plugin này một mình (không có `ktc-ra-soat-897`), quy ước
"kho chỉ đọc" trong `CLAUDE.md` của dự án vẫn có hiệu lực theo quy ước làm việc, nhưng **không được hook
chặn tự động**.

## Xác thực trước khi bật — CHƯA HOÀN TẤT

Môi trường dựng plugin này **không có `claude` CLI trên PATH**, nên **chưa chạy được**
`claude plugin validate ./plugin --strict`. Đã tự kiểm thủ công: frontmatter 5 SKILL.md hợp lệ, JSON
(`plugin.json`, `hooks.json`) hợp lệ, mọi tham chiếu `${CLAUDE_PLUGIN_ROOT}/...` trỏ đúng tệp có thật, đối
chiếu byte-for-byte với 5 gói `.skill` nguồn không mất nội dung. **Bắt buộc chạy strict validation thật
trước khi coi là sẵn sàng phát hành**, đúng quy tắc runtime của dự án (xem `CORE-INDEX.md` của plugin
`ktc-ra-soat-897` — cùng quy tắc áp dụng chung cho mọi plugin KTC).

## Build lại

```bash
python tools/dong_goi_plugin.py
```

Chạy từ gốc dự án `KTC-Quan-tri`. Script chỉ dọn và tái dựng các thư mục sinh tự động
(`skills/`, `.claude-plugin/`, `hooks/`, `scripts/`) từ 5 gói `.skill` đang được `tools/kiem_tra_he_thong.py`
coi là hiện hành — **không đụng tới** `README.md`/`CHANGELOG.md` này (viết tay) và không sửa tay bất kỳ
tệp nào trong `plugin/skills/`.

Sau khi build, muốn cập nhật bản cài trong marketplace cục bộ thì tự chép đè:

```bash
rm -rf ~/.claude/ktc-marketplace/ktc-quan-tri
cp -r plugin ~/.claude/ktc-marketplace/ktc-quan-tri
```
