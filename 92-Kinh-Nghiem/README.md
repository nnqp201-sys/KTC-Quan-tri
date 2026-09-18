# 92-Kinh-Nghiem — Lớp tiến hóa tri thức của KTC-Quan-tri

**Ngày lập:** 13/9/2026 · **Mô hình kế thừa:** `KTC-Ra-Soat-897-v2-Cai-tien/92-Kinh-Nghiem/` (lập 30/8/2026)

Nơi lưu **quá trình tư duy dẫn tới thay đổi**: kinh nghiệm thực chiến, quyết định kiến trúc, đề xuất chờ
duyệt, kết quả hồi quy, lỗi đã biết. Khi phát triển phiên bản sau, đọc thư mục này là đủ để kế thừa có chọn
lọc, không cần đọc lại toàn bộ lịch sử hội thoại.

## 0. Quy tắc bất biến — không lưu nội dung nghiệp vụ chính thức ở đây

Thư mục này **chỉ** chứa: kinh nghiệm · quyết định · đề xuất · hồi quy · release notes · lỗi đã biết.

**KHÔNG** chứa nội dung nghiệp vụ chính thức — những thứ đó ở đúng vị trí của chúng:

| Loại nội dung | Vị trí chính thức (không đổi) |
|---|---|
| Quy tắc, bảng mã, từ điển dữ liệu dùng chung | `20-Chuan-Chung/` |
| Sổ dữ liệu nhiệm vụ | `21-Master-Task-Register/` |
| Bộ nhớ vận hành từng ca | `90-Nhat-Ky-Van-Hanh/` |
| Tài liệu kiến trúc | `91-Tai-Lieu-Thiet-Ke/` |
| Gói skill và tham chiếu của nó | `SKILL.md`, `ktc-quan-tri.skill` |

Lý do: trộn lẫn hai loại sẽ khiến không phân biệt được đâu là "đang chạy thật" và đâu là "đang được cân nhắc".

## 1. Cấu trúc

```
92-Kinh-Nghiem/
├── README.md                 ← tệp này
├── 01-Lessons-Learned/       tri thức thực chiến      LL-YYYYMMDD-NNN.md
├── 02-Regression/
│   ├── Cases/                mô tả ca kiểm thử
│   ├── Fixtures/             dữ liệu test cố định
│   └── Expected-Results/     kết quả kỳ vọng
├── 03-Change-Proposals/      đề xuất chờ duyệt        CP-YYYYMMDD-NNN.md
├── 04-Release-Notes/         ghi chú phát hành        vX.Y.md
├── 05-Known-Issues/          lỗi đã biết chưa sửa     Pending.md / KI-YYYYMMDD-NNN.md
└── 06-Decision-Log/          quyết định kiến trúc     DL-YYYYMMDD-NNN.md
```

`NNN` = số thứ tự 3 chữ số, đếm riêng theo từng ngày trong từng thư mục.

## 2. Luồng xử lý chuẩn

```
Phát hiện (lỗi dữ liệu / quy tắc sai / cách làm tốt hơn)
        │
        ▼
01-Lessons-Learned/     ghi ngay, không chờ quyết định
        │
        ▼  (nếu có đề xuất thay đổi cụ thể)
03-Change-Proposals/    kèm ca kiểm thử tại 02-Regression/Cases/
        │
        ▼  (chạy hồi quy)
        ├── PASS + được duyệt ──► 06-Decision-Log/ (ghi APPLY)
        │            │
        │            ▼  áp dụng vào 20-Chuan-Chung/ và gói skill
        │            ▼  04-Release-Notes/
        │
        └── không duyệt / hoãn ─► 06-Decision-Log/ (ghi REJECT/DEFER kèm lý do)
                     │
                     ▼  (nếu là lỗi thật nhưng chưa sửa ngay)
               05-Known-Issues/
```

## 3. Bắt buộc ghi Decision Log khi

- Đổi kiến trúc thư mục hoặc bộ trường dữ liệu.
- Quyết định **không** áp dụng một đề xuất — từ chối cũng là quyết định, phải ghi lý do.
- Chọn giữa từ hai phương án kỹ thuật tương đương trở lên.
- Thay đổi ảnh hưởng từ hai hệ con trở lên.

## 4. Quan hệ với `90-Nhat-Ky-Van-Hanh/`

Hai lớp khác nhau, đừng trộn:

| | `90-Nhat-Ky-Van-Hanh/` | `92-Kinh-Nghiem/` |
|---|---|---|
| Ghi cái gì | **Từng ca vận hành** — kỳ này làm gì, đọc nguồn nào, ra kết quả gì | **Tri thức rút ra** qua nhiều ca |
| Nhịp ghi | Mỗi lần chốt kỳ, dựng báo cáo | Khi phát hiện điều đáng nhớ hoặc ra quyết định |
| Ví dụ | "Chốt kỳ tháng 8/2026: 328 nhiệm vụ, 4 lỗi thể thức" | "Thang điểm trong danh mục dự thảo không phải ràng buộc kiểm tra" |

Một mục Process Memory có thể **sinh ra** một Lesson Learned; khi đó ghi rõ liên kết hai chiều.
