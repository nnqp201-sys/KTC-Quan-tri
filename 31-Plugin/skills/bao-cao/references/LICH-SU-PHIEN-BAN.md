# Lịch sử phiên bản (tách khỏi SKILL.md khi dựng plugin 1.3.1 — không nạp khi làm việc)

> **v3.19** (28/9/2026) — Chạy thật plugin 1.3.6 (Claude Code, thư mục thành viên): bỏ số hiệu dị dạng của bản gốc ('Số375BC-CĐKT'), đổi kỳ ở tiêu đề nhóm, Trục của phụ lục; bộ nhớ quá trình không ghi vào tệp plugin khi chạy ngoài dự án (ghi vào ghi chú đối soát).

> **v3.18** (28/9/2026) — Quy trình chính báo cáo tháng cấp Trường: 4 sản phẩm phát triển từ bản đã ban hành bằng `bc_thang.py` (Skill 37); đầu mối chưa nộp thì tổng hợp từ nguồn khác có ghi nguồn; lỗi công thức dòng không loại cả đơn vị; `fill_bc736.py` chỉ còn dự phòng (chạy thử 28/9/2026 kém bản 21/9).

> **v3.17** (28/9/2026) — Nguyên tắc 3: kết nối thư mục làm việc của đơn vị (Cowork, Claude Code ngoài dự án) — đọc `10-Dau-Vao/`, lưu `30-Ket-Qua/` trong thư mục đó (plugin 1.3.5).

> **v3.16** (28/9/2026) — Chuẩn 6 Trục: căn cứ Quyết định số 1923/QĐ-CĐKT Phụ lục I, II cho cột Điểm chấm, Hệ số quy đổi; quan hệ với Danh mục sản phẩm, công việc theo Quyết định số 2119/QĐ-CĐKT (DL-20260928-002).

> **v3.15** (27/9/2026) — Mô tả kích hoạt viết lại có dấu, nêu tình huống viết đoạn đánh giá, tổng hợp bảng kết quả dán trong khung chat: nghiệm thu 1.3.1 cho thấy các yêu cầu này không kích hoạt skill (thẩm định lần 3, DL-20260927-001).

> **v3.14** (19/9/2026) — Nguyên tắc 6 — chuẩn thể thức sản phẩm .docx/.xlsx theo 03-Templates(1)/04-Good-Documents, dùng kèm skill the-thuc (DL-20260919-003).

> **v3.13** (19/9/2026) — Quy tắc viện dẫn văn bản: NĐ 30 · Pháp lệnh hợp nhất · quy ước Trường; VBHC không ghi số hiệu Luật (DL-20260919-002).

> **v3.12** (19/9/2026) — Đơn vị nộp qua khung chat: tên tệp trả về chuẩn + phiếu tự kiểm, tải về gửi P-THHC (DL-20260919-001).

> **v3.11** (18/9/2026) — KTC-Database đọc bản gốc trên Google Drive (ổ Drive), bản chép cục bộ có thể cũ — đính chính DL-20260918-005.

> **v3.10** (18/9/2026) — Nguyên tắc 4 — nơi lưu đầu vào, tìm KTC-Database không qua ổ đĩa, Google Drive (DL-20260918-005).

> **v3.9** (18/9/2026) — Kết cấu lại thư mục theo nhóm INPUT/PROCESS/OUTPUT (DL-20260918-004); thêm Nguyên tắc 3 — đầu vào từ tệp đính kèm cho tài khoản Team.

> **v3.8** (18/9/2026) — `read_bc736_excel.py` v3.3: đọc cột `Task_ID` ở cuối bảng Phụ lục (KI-001, Lãnh đạo
> thống nhất 18/9/2026, `DL-20260918-003`) — mỗi nhiệm vụ có trường `task_id` (None nếu tệp chưa có cột, giữ
> đối chiếu gần đúng); cảnh báo `[TASK_ID SAI ĐỊNH DẠNG]` / `[TASK_ID TRÙNG]`, không tự sửa mã. Sửa lỗi nhiệm
> vụ có số TT bắt đầu bằng "Tổng hợp/Tổng kết…" bị coi là dòng cộng và bỏ mất.
## Quy tắc bất biến và khuôn đầu ra (chuẩn chung KTC-Quan-tri — lõi)
