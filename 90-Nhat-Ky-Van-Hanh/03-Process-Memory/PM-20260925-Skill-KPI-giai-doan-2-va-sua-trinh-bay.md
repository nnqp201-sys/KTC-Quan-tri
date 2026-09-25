```yaml
memory_id: PM-20260925-001
created_at: 2026-09-25
memory_type: process
status: closed
task_type: xay_skill_va_sua_loi
project_name: KTC-Quan-tri
```

# Phiên 25/9/2026 — skill KPI tự đánh giá (giai đoạn 2), sửa trình bày sheet KPI, plugin 1.2.0 → 1.2.1

**Kết quả:** `ktc-kpi-tu-danh-gia` v1.0 → 1.1 (`DL-20260925-001`), `ktc-kpi-lap-ke-hoach` 1.1 → 1.2 (`DL-20260925-002`),
`quan-tri` 1.12; plugin 1.2.1 qua `claude plugin validate --strict`; bản cài trên máy nâng từ 1.0.0; quyền `git push`.

## Bài học — dùng lại cho lần sau

1. **Lệnh do người/AI khác viết có thể nêu sai nguyên nhân dù triệu chứng đúng.** Lệnh sửa 25/9 cho rằng KPI!C–F bị xóa
   và F vốn là công thức, nhóm `ho-tro` không có cột phối hợp — cả ba sai khi mở 6 mẫu thật. → Đo mẫu trước, sửa theo
   thực tế, ghi bảng "lệnh nêu / thực tế" trong Decision Log.
2. **Phép kiểm đếm cứng vỡ khi thay đổi có chủ đích.** `test_validate_plan` đếm "990 công thức" → thay bằng kiểm bất biến
   thật: công thức của mẫu còn nguyên đúng ô + phần thêm đúng loại, đúng số lượng.
3. **Kiểm hiển thị Excel bằng máy được:** Excel COM `Range.CopyPicture` → dán vào ChartObject → `Chart.Export` PNG, rồi
   đọc ảnh. Không cần LibreOffice/poppler. Kèm: Excel COM `CalculateFull` để so số công thức với Python.
4. **Claude Code headless chạy được từ `claude.exe` trong extension VS Code** → thử kích hoạt skill thật
   (`claude -p ... --plugin-dir`, đọc lời gọi `Skill` trong stream-json; ~0,23 USD/lượt) và `claude plugin validate`.
5. **Plugin cài từ marketplace thư mục chạy từ bộ nhớ đệm** (`plugins/cache/<mp>/<plugin>/<phiên bản>`): chép đè thư mục
   nguồn chưa đủ — phải `claude plugin marketplace update <mp>` rồi `claude plugin update <plugin>@<mp>`.
6. **Đổi số phiên bản trong `kiem_tra_he_thong.py` SAU khi đóng gói**, không trước — đổi trước thì lần kiểm "trước đóng
   gói" báo lỗi giả (thiếu gói).
7. Viết ca thử trước khi sửa: bọc lời gọi hàm chưa tồn tại (`lambda`) để bộ thử báo "sai" chứ không dừng.

## Việc còn mở (xem nơi gốc)

Chụp màn hình sheet KPI trên tệp thật sau khi sửa (lệnh mục 7) · thử kích hoạt trên Chat/Cowork · Câu hỏi mở #8, #10–#13
(`28-KTC-KPI/references/Cau-Hoi-Mo.md`) · KPI quý IV của người dùng chờ dữ liệu · TX04 in ngang (đề xuất riêng).
