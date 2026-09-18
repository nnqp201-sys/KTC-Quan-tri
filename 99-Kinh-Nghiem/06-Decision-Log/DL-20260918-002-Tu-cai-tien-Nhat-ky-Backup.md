# DL-20260918-002 — Thêm agent tự cải tiến, tự ghi nhật ký, tự backup GitHub vào plugin

**Ngày:** 18/9/2026 · **Trạng thái:** ✅ Đã thực hiện (backup còn chờ URL repo) · **Plugin:** `ktc-quan-tri` 0.2.0
**Yêu cầu:** người dùng — "thêm Agent Self-improving, cơ chế tự log và lưu vào context, cơ chế tự backup mỗi ngày lên GitHub"

## Quyết định thiết kế

| Thành phần | Chọn | Lý do |
|---|---|---|
| Agent tự cải tiến | **Chỉ đề xuất** (`CP-...` *Chờ duyệt*), chặn `Edit`, chỉ tạo tệp trong `03-Change-Proposals/` | Nguyên tắc bất biến #6: AI không tự quyết thay người có thẩm quyền. Hệ "tự sửa quy tắc của chính nó" không có người duyệt là đúng kiểu lỗi đã gặp (`DL-20260914-006`: đồng bộ mù xoá quy tắc thật) |
| Nhật ký | JSONL theo ngày, chỉ tên công cụ + đối tượng, không ghi nội dung | Log phục vụ truy vết, không được thành bản sao thứ hai của dữ liệu đơn vị; lại còn được đẩy lên GitHub |
| Nạp vào context | `SessionStart` in tóm tắt 2 ngày (≤ ~30 dòng) | Đủ để phiên mới biết phiên trước làm gì mà không tốn context |
| Phạm vi log | Chỉ khi thư mục có `03-Nhat-Ky-Van-Hanh/` | Plugin bật ở cấp người dùng — không được ghi log vào dự án khác |
| Lịch backup | Task Scheduler 21:00 + `StartWhenAvailable`; `SessionStart` chạy bù nếu > 24h | Không phụ thuộc việc có mở Claude hay không |
| An toàn backup | Không force-push/rebase/reset; `GIT_TERMINAL_PROMPT=0`; dừng khi có tệp tên giống bí mật; bù giữa phiên chỉ khi đã từng push thành công | Tác vụ chạy ngầm không được treo, không được ghi đè lịch sử, không được lộ bí mật |
| Nguồn script | `tools/plugin_src/` — build chép vào `plugin/` | Giữ đúng nguyên tắc "không sửa tay trong gói đã build" |

## Kiểm chứng

`99-Kinh-Nghiem/02-Regression/Cases/test_plugin_nhat_ky_backup.py` — 10/10 ca đạt, gồm 4 ca ngược (ngoài dự án
không ghi log · stdin hỏng không vỡ · tệp tên giống bí mật thì dừng và không push · không xoá tệp của người
dùng). Tác vụ lên lịch đã chạy thử: kết quả 0, bỏ qua đúng vì chưa có remote.

## Còn chờ người dùng

1. **URL repo GitHub PRIVATE.** Repo sẽ chứa hồ sơ đơn vị nộp (`11-Du-Lieu-Dau-Vao/`), bản dự thảo văn bản,
   nhật ký — **không được để public**.
2. Lần push đầu tiên chạy tay một lần để Git Credential Manager lưu đăng nhập.
