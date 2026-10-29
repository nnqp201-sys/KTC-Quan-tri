# LỆNH TỔNG HỢP — Xử lý Mục 1, 4, 5, 6
## 30/8/2026 — Gửi kèm file 09-Quy-Uoc-Doan-The-CDKT.md

---

## MỤC 6 — ĐÃ LÀM XONG, CHỈ CẦN TẢI LÊN ĐÚNG VỊ TRÍ

File đính kèm `09-Quy-Uoc-Doan-The-CDKT.md` đã soạn xong, dựa trên 2 nguồn thật đã xác minh trực tiếp trên Drive (không suy đoán):
1. Phụ lục TB 597/TB-CĐKT mục III (3.1–3.3) — bảng mẫu thể thức đầu văn bản cho cả 3 tiểu-hệ.
2. QĐ 933/QĐ-TLĐ (14/5/2024) — quy tắc chuyên sâu riêng cho Công đoàn.

**Việc cần làm**: Tải file này vào `references/Checklist/` (cùng cấp với `08-Quy-Uoc-Rieng-CDKT.md`), rồi thêm 1 dòng trong `SKILL.md` mục Bước 0 / hệ D: *"Đối chiếu chi tiết theo `09-Quy-Uoc-Doan-The-CDKT.md`"*. Sau đó chạy lại 4 lỗi liên quan hệ đoàn thể trong bộ hồi quy 30 lỗi (#25–28) để đo cải thiện thật, ghi vào `BANG-CHI-SO-THEO-THOI-GIAN.md`.

---

## MỤC 1 — Đồng bộ `tools/build_ktc897_report.py` rời lên v3.4

Xác nhận thật (30/8/2026): file rời trong `tools/` trên Drive (ID `1F3boP0D54A666uBVG5igvu8QxV0EVXh9`) vẫn là **v3.3** — chưa có 5 bản vá đã xác nhận trong `.skill` v2.18 (kiểm tra khổ bảng thật, vá metadata Pages/Words, vá lỗi `zoom`, vá thứ tự schema `tblLayout`/`tcMar`/`shd`).

**Việc cần làm**: Lấy đúng nội dung script v3.4 từ bên trong `ktc-ra-soat-897-v2.18.skill` (giải nén `tools/build_ktc897_report.py`), tạo file mới thay thế file rời trong `tools/` — dùng `copy_file` hoặc giải nén trực tiếp trên Drive, **không transcribe tay** (đúng quy tắc 17). Xác nhận lại bằng cách so sánh checksum giữa file rời và file trong `.skill` — phải khớp tuyệt đối.

---

## MỤC 4 — Đồng bộ với kho `99-Kinh-Nghiem/`

Phát hiện: nhiều nội dung em vừa làm hôm nay (đồng bộ script, sửa khổ giấy 2 file mẫu, xác nhận NĐ 334) trùng lặp một phần với các Change Proposal/Known Issues đã có sẵn trong `99-Kinh-Nghiem/`.

**Việc cần làm**:
1. Đọc `99-Kinh-Nghiem/05-Known-Issues/` — đối chiếu xem "khổ giấy 2 file mẫu gốc" và "script rời v3.3 vs v3.4" đã được ghi làm Known Issue chưa; nếu chưa, bổ sung.
2. Nếu đã có, cập nhật trạng thái thành "đã xử lý 30/8/2026", tránh để 2 nơi (phiên làm việc và kho kinh nghiệm) cùng lúc coi là "đang mở".
3. Ghi 1 Decision Log mới: quyết định dùng nguồn TB 597 Phụ lục + QĐ 933/QĐ-TLĐ cho Checklist đoàn thể (Mục 6), thay vì tự soạn quy tắc mới — để các phiên sau không lặp lại việc tìm nguồn.

---

## MỤC 5 — Rà lại tài liệu ghi "5 hệ" → sửa thành "6 hệ"

Xác nhận: KTC-DIS thực chất là **6 hệ** (ktc-ra-soat-897, ktc-database, ktc-bao-cao, ktc-dis-tong-hop-vb, ktc-ke-hoach, **ktc-van-ban** — hệ thứ 6 từng bị hiểu nhầm là thư mục legacy).

**Việc cần làm**: Tìm và sửa tất cả chỗ còn ghi "5 hệ KTC-DIS" thành "6 hệ". Ưu tiên kiểm tra:
1. `LENH-CAP-NHAT-v2.17-26082026.md` (đã đọc, xác nhận có ghi "cả 5 hệ KTC-DIS" ở mục 5 — **đây là thông tin cũ, cần đính chính** nếu tài liệu này còn được tham chiếu).
2. Bất kỳ `SKILL.md` nào của 5 hệ còn lại có nhắc số lượng hệ.
3. `00b-Trigger-Vien-Dan-Van-Ban-Hop-Nhat.md` và các file liên quan tới Skill viện dẫn văn bản hợp nhất — xác nhận đã nhân bản đủ cho **cả 6 hệ**, không chỉ 5 (đúng theo Nhật ký v1.6 đã ghi "áp dụng cho 6 hệ" — kiểm tra xem hệ `ktc-van-ban` đã thực sự có bản sao chưa, hay mới chỉ *nói* là có).

**Xác nhận lại**: liệt kê rõ đã tìm thấy bao nhiêu chỗ ghi "5 hệ", đã sửa được bao nhiêu, còn chỗ nào chưa sửa được (do khác quyền sở hữu) thì ghi rõ để làm sau.

---

## XÁC NHẬN CHUNG

Báo cáo theo đúng thứ tự 6 → 1 → 4 → 5, mỗi mục nêu rõ kết quả thật (ID file, kiểm tra bằng gì), không dùng "đã xong" nếu chưa đối chiếu trực tiếp với Drive.
