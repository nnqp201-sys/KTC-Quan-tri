# KTC-Quan-tri Plugin

Plugin Claude Code/Cowork cho chu trình quản trị nhiệm vụ khép kín của Trường Cao đẳng Kon Tum:
Kế hoạch → Theo dõi → Kết quả/Bằng chứng → Báo cáo, kèm hệ soạn thảo văn bản hành chính.

**Nguồn dựng:** 5 gói `.skill` đã xác minh byte-for-byte ngày 18/9/2026 (xem
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
  `scripts/ktc_trackchanges.py` (thao tác Track Changes mức OOXML, cần `python-docx`) và đo lề/cỡ chữ thật
  từ `.docx`.
- **Claude Chat:** chưa thử nghiệm qua đường plugin này (Chat trước nay dùng đường Skill rời từng hệ, xem
  `KI-010` trong repo dự án — chưa có nhật ký đợt chạy đó).

## Hooks

Chỉ có `SessionStart` → `scripts/ktc_quan_tri_doctor.py`: in banner phiên bản tự khai của cả 5 skill khi
phiên khởi động, để phát hiện sớm tình trạng "gói build xong nhưng chưa gắn vào hệ" (nguyên nhân của
`DL-20260918-001`). **Không có** `PreToolUse` guard chặn ghi `KTC-Database` — plugin `ktc-ra-soat-897` đã
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

Chạy từ gốc dự án `KTC-Quan-tri`. Script tái dựng toàn bộ `plugin/` từ 5 gói `.skill` đang được
`tools/kiem_tra_he_thong.py` coi là hiện hành — không sửa tay bất kỳ tệp nào trong `plugin/skills/`.
