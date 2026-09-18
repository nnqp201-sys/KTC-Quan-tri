# DL-20260918-001 — Bốn gói `.skill` đã build xong từ 15/9 nhưng chưa gắn vào hệ: xác minh và trỏ chính thức

**Ngày:** 18/9/2026 · **Trạng thái:** ✅ **ĐÃ THỰC HIỆN**

## Câu hỏi

`python tools/kiem_tra_he_thong.py` báo **12 lỗi C5** (5 tệp dùng chung lệch bản gốc trong gói) + cảnh báo
C11 (1 tệp mồ côi). Sửa bằng cách nào: đóng gói lại từ đầu, hay có sẵn bản đã đúng?

## Phát hiện

Trên đĩa đã có 4 gói `.skill` **mới hơn** gói mà `tools/kiem_tra_he_thong.py` đang trỏ tới, build cùng một
đợt (14–15/9/2026), nhưng **không có bất kỳ dấu vết vận hành nào** ghi nhận đợt build đó: không Process
Memory, không Decision Log, không cập nhật `MEMORY-INDEX.md`, và công cụ kiểm tra vẫn trỏ gói cũ.

| Hệ | Gói cũ (checker đang trỏ) | Gói mới có sẵn, chưa dùng | Giờ build |
|---|---|---|---|
| ktc-bao-cao | `ktc-bao-cao-v3.6.skill` | `ktc-bao-cao-v3.7.skill` | 15/9 08:28 |
| ktc-ke-hoach | `ktc-ke-hoach-v3.2.skill` | `ktc-ke-hoach-v3.3.skill` | 15/9 08:28 |
| ktc-soan-thao-vb | `ktc-soan-thao-vb.skill` (v1.0) | `ktc-soan-thao-vb-v1.1.skill` | 15/9 08:28 |
| ktc-theo-doi-cv | `ktc-theo-doi-cv-v1.0.skill` | `ktc-theo-doi-cv-v1.1.skill` | 14/9 19:01 |

## Xác minh trước khi dùng (không suy diễn từ tên tệp — nguyên tắc bất biến #6)

1. **Frontmatter + liên kết**: cả 4 gói qua `dong_goi_skill.kiem_frontmatter()` / `kiem_lien_ket()` — sạch.
2. **Tự khai phiên bản trong `SKILL.md`** khớp tên tệp: `ktc-ke-hoach` "Phiên bản: 3.3 — 14/9/2026",
   `ktc-soan-thao-vb` "Phiên bản: v1.1 — 14/9/2026", `ktc-theo-doi-cv` "Phiên bản: 1.1 — 14/9/2026",
   `ktc-bao-cao` "# KTC-Bao-Cao / KTC-RIS v3.7".
3. **5 tệp dùng chung trong gói khớp byte-for-byte với `01-Chuan-Chung/`** — đây chính là lỗi C5, nay đã hết.
4. **Toàn bộ nội dung gói khớp byte-for-byte với nguồn rời `references/`** tương ứng của từng hệ — 0 lệch,
   0 tệp mồ côi (cảnh báo C11 cũng hết).
5. **So sánh danh sách tệp cũ → mới**: chỉ có **thêm tệp** (RUN-RECORD-SCHEMA, trigger viện dẫn văn bản
   hợp nhất, patch notes, test hồi quy, Prompt-Library preflight…) và **đổi đúng 1 tệp**:
   `00d-Ghi-Nho-ND-334-2026-Thay-The-ND-60-111.md` (mồ côi, không có nguồn rời — chính là cảnh báo C11) →
   `00d-Ghi-Nho-ND-334-2026-Pham-Vi-Co-So-GDNN.md` (có nguồn rời khớp hoàn toàn ở cả 3 hệ, 6170 b). Không
   tệp nào bị mất so với gói cũ.

Kết luận: đợt build 14–15/9 làm đúng, chỉ chưa hoàn tất bước cuối (gắn vào hệ + ghi nhận).

## Đã làm

| Bước | Kết quả |
|---|---|
| Trỏ `tools/kiem_tra_he_thong.py` (dict `HE`) | 4 hệ → gói mới ở bảng trên; `ktc-quan-tri` giữ nguyên (đã đồng bộ) |
| Cập nhật `03-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md` | Bảng "Phiên bản hiện hành" ghi đúng gói mới; sửa mâu thuẫn nội bộ "10 phép kiểm" → khớp "11 phép kiểm" |
| Sửa 3 đường dẫn tắt không kiểm chứng được (C3) | `CLAUDE.md` (`Checklist/…` → `KTC-Ra-Soat-897-v2-Cai-tien/references/Checklist/…`), `00-README.md` (tên tệp viết tắt `...md` → tên đầy đủ), `MEMORY-INDEX.md` (`897/…` → `KTC-Ra-Soat-897-v2-Cai-tien/…`; 2 đường dẫn ví dụ trong bài học thêm tiền tố hệ đã thay thế) |
| Gói cũ | **Giữ nguyên trên đĩa**, không xoá/di chuyển — đúng quy ước đã có cho `ktc-bao-cao-v3.6` (giữ để hoàn tác) |
| Xác nhận lại | `python tools/kiem_tra_he_thong.py --chi-tiet` → 0 lỗi; bộ thử ngược `test_kiem_tra_he_thong.py` chạy mã 0 |

## Bài học ghi lại

1. **Một gói `.skill` build xong không có nghĩa là hệ đang dùng nó.** Phải cập nhật đồng thời: công cụ
   kiểm tra tĩnh (`HE` trong `kiem_tra_he_thong.py`) và `MEMORY-INDEX.md`. Thiếu một trong hai thì gói mới
   coi như không tồn tại đối với các phiên sau.
2. **Trước khi bỏ, so sánh danh sách tệp cũ → mới**, không chỉ so 5 tệp dùng chung. Việc build có thể vừa
   sửa đúng lỗi đang tìm, vừa đổi thêm nội dung khác (ở đây là tệp `00d-…`) — phải xác nhận không có tệp
   nào biến mất trước khi coi gói mới là an toàn để thay thế.
3. **Đường dẫn tắt trong tài liệu cấp dự án (`Checklist/…`, `897/…`) không kiểm chứng được bằng công cụ.**
   Viết đường dẫn đầy đủ từ gốc dự án hoặc gốc `D:\.CLAUDE code\` để C3 xác minh được, thay vì dựa vào ngữ
   cảnh câu văn xung quanh.

## Còn ngoài phạm vi

Không đụng tới `99-Kinh-Nghiem/05-Known-Issues/Pending.md` — các việc mở ở đó (KI-001, 002, 003, 006, 007,
008, 010, 011, 014) cần dữ liệu từ đơn vị hoặc người có thẩm quyền quyết định, không phải lỗi kỹ thuật của
việc đóng gói.
