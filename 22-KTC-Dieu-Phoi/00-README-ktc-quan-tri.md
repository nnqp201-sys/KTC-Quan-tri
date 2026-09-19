# ktc-quan-tri — Hệ quản trị nhiệm vụ hợp nhất
### Phiên bản 1.0 — 13/9/2026 · Trường Cao đẳng Kon Tum

Lớp điều phối đặt trên ba hệ `ktc-ke-hoach`, `KTC-Theo-doi-CV`, `ktc-bao-cao`, thực hiện chu trình quản trị
nhiệm vụ khép kín:

> Chủ trương/Văn bản → Nhiệm vụ → Kế hoạch → Giao việc → Theo dõi → Kết quả/Bằng chứng → Báo cáo → Đánh giá → Điều chỉnh kế hoạch

Nguyên tắc gốc: **một nhiệm vụ – một mã – một dòng dữ liệu gốc – một lịch sử – nhiều góc nhìn.**

## Năm tác vụ

| | Tác vụ |
|---|---|
| (a) | Chuẩn hóa nhiệm vụ, phân loại 6 Trục/38 Nội hàm, cấp Task_ID |
| (b) | Theo dõi vòng đời, phát 8 loại cảnh báo |
| (c) | Đối chiếu Kế hoạch ↔ Theo dõi ↔ Báo cáo |
| (d) | Chốt kỳ, dựng báo cáo 5 phần, checklist 12 điểm |
| (e) | Quy đổi KPI, xếp loại chất lượng theo QĐ 1923/QĐ-CĐKT |

**Không** soạn thảo văn bản hành chính mới (dùng `ktc-soan-thao-vb`) · **không** rà soát thể thức trước
trình ký (dùng `ktc-ra-soat-897`).

## Nội dung gói

```
ktc-quan-tri/
├── SKILL.md          Bộ định tuyến — 6 nguyên tắc, Bước 0, bảng 5 tác vụ, 4 cạm bẫy
├── 00-README.md      Tệp này
└── references/       14 tệp, xem references/README.md
    ├── 01-02  Nguyên tắc và chỉ mục kho KTC-Database
    ├── 10-13  Phân loại: 6 Trục/38 Nội hàm · mã đơn vị · danh mục nhiệm vụ và sản phẩm
    ├── 20-24  Dữ liệu và vòng đời: 46 trường · Task_ID · trạng thái · đối chiếu · chốt kỳ
    ├── 30     KPI và xếp loại
    └── 40-41  Process Memory · giới hạn nền tảng
```

## Cài đặt

Bấm **Save skill** trên Claude với tệp `ktc-quan-tri.skill`. Gói này **không mang theo dữ liệu** — vẫn cần
Project có kết nối Google Drive tới:

- `KTC-Quan-tri/` — Master Task Register, lớp chuẩn chung, 5 hệ con
- `KTC-Database/` — kho nền pháp lý và quy định (chỉ đọc)

## Bốn hạn chế đã biết của phiên bản 1.0

1. **Chưa đối chiếu 1-1 được giữa kế hoạch và báo cáo** — Phụ lục Ia/Ib của TB736 chưa có cột `Task_ID`.
   Mọi kết quả đối chiếu hiện là *gần đúng* và phải được trình bày đúng như vậy.
2. **Danh mục 122 nhiệm vụ chuẩn mới phủ 5/11 đơn vị** — sáu Khoa chưa có dữ liệu, dự kiến bổ sung sau.
3. **Bộ 46 trường và quy tắc Task_ID còn là dự thảo**, chưa đơn vị nào dùng thử.
4. **Bảng hệ số quy đổi 371 sản phẩm đã gửi đơn vị rà soát theo TB 1052/TB-CĐKT (15/9/2026), chưa ban hành**; vẫn lẫn hai thang (KI-014).

## Quan hệ với hệ khác trong hệ thống KTC

| Hệ | Quan hệ |
|---|---|
| `ktc-ke-hoach` (PIS) | Nguồn sinh nhiệm vụ và Task_ID; hệ này điều phối, không thay thế |
| `KTC-Theo-doi-CV` | Control tower — cung cấp trạng thái, tiến độ, minh chứng |
| `ktc-bao-cao` (RIS) | Tiêu thụ dữ liệu đã chốt để dựng báo cáo |
| `ktc-database` | Nguồn văn bản pháp lý và quy định — **chỉ đọc** |
| `ktc-ra-soat-897` | Lớp kiểm soát chất lượng **bắt buộc trước khi trình ký** |
| `ktc-soan-thao-vb` | Dùng khi cần soạn thảo văn bản hành chính mới |
