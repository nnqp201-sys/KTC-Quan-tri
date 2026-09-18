# 11-Theo-Doi-Vong-Doi — Quy trình 6 bước
## Phiên bản: v1.0 — 14/9/2026

## Trước khi bắt đầu
1. Đọc `references/Skill-Library/00-Nguyen-Tac-Chung.md`.
2. Mở `01. Bộ dữ liệu vận hành KTC-Theo-dõi-CV.xlsx` — kiểm bảng Nhiệm vụ có bao nhiêu dòng.
   **Nếu 0 dòng: mọi kết quả sau đó là dữ liệu mẫu, phải tự khai rõ.**

## Sáu bước

| Bước | Việc | Skill | Đầu ra |
|---|---|---|---|
| 1 | Tiếp nhận nhiệm vụ đã có `Task_ID`, chạy 4 phép kiểm cổng vào | 40 | Dòng mới ở bảng Nhiệm vụ, trạng thái *Mới* |
| 2 | Phân công chủ trì, phối hợp, thời hạn; **khóa baseline** | 40 | Trạng thái *Đã giao*, `Khóa baseline = Có` |
| 3 | Cập nhật tiến độ theo kỳ | 41 | Dòng ở bảng Cập nhật tiến độ |
| 4 | Quét và phát 8 cảnh báo | 42 | Danh sách cảnh báo gửi đơn vị / lãnh đạo |
| 5 | Thu nhận và xác minh minh chứng | 43 | Dòng ở bảng Minh chứng, tình trạng *Đã xác minh* |
| 6 | Chốt kỳ, bàn giao cho `ktc-bao-cao` | 44 | Gói bàn giao 4 thành phần |

Đề nghị điều chỉnh baseline chen ngang bất cứ lúc nào — Skill 44 phần A.

## Hai chốt chặn không được nới
1. *Đã hoàn thành* **bắt buộc có minh chứng đã xác minh**. Thiếu → giữ ở *Chờ kết quả*.
2. Baseline chỉ đổi sau khi đề nghị điều chỉnh **đã được duyệt**.

## Sau khi chốt kỳ — nghĩa vụ ghi nhớ
Ghi một mục Process Memory tại `03-Nhat-Ky-Van-Hanh/03-Process-Memory/` theo mẫu
`03-Nhat-Ky-Van-Hanh/02-Mau-Process-Memory.md`: kỳ nào, bao nhiêu nhiệm vụ, bao nhiêu cảnh báo,
lệch chuẩn ở đâu. Ghi cuối phiên là quá muộn — phiên kết thúc thì mất ngữ cảnh.

## Liên kết ba hệ
```
ktc-ke-hoach ──Task_ID──▶ ktc-theo-doi-cv ──gói bàn giao──▶ ktc-bao-cao ──▶ ktc-ra-soat-897 ──▶ trình ký
```
