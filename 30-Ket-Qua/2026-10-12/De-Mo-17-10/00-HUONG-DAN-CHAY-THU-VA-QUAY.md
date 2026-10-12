# Hướng dẫn chạy thử và quay 04 thao tác (việc của người trình bày)

Mọi thứ còn lại đã chuẩn bị sẵn trong thư mục này. Chỉ còn 02 việc cần người làm trên Claude Cowork: **chạy thử** và **quay màn hình**.

## Đã có sẵn

| Thứ | Ở đâu |
|---|---|
| Bộ dữ liệu giả định D1–D4 | `Du-lieu-gia-dinh/` (KHÔNG kéo thư mục `_Dap-an-KHONG-dua-vao-cong-cu` vào Cowork) |
| Kết quả chạy trước của cả 3 phần (để mở khi trình diễn, kể cả khi mất mạng) | `Ket-qua-chay-truoc/` |
| Giọng thuyết minh 04 đoạn (AI, giọng nữ tiếng Việt) | `Video-thao-tac/T1…T4_*.mp3` |
| Công cụ ghép video | `Video-thao-tac/ghep_video.py` |

## Bước 1 — Chạy thử trên Claude Cowork (khoảng 30 phút)

Mở Cowork, kết nối thư mục `Du-lieu-gia-dinh`, mỗi thao tác một cuộc hội thoại mới:

| Thao tác | Kéo vào | Gõ lệnh |
|---|---|---|
| T1 | Thư mục `D1-Ke-hoach-quy-IV-2026` | Kiểm tra hồ sơ kế hoạch quý của các đơn vị trong thư mục này, rồi tổng hợp thành dự thảo Kế hoạch công tác quý IV năm 2026 của cơ quan |
| T2 | Tệp trong `D2-He-thong-QLVB` (cùng cuộc hội thoại T1) | Từ danh mục văn bản này, liệt kê văn bản chỉ đạo, kế hoạch năm, quý, thông báo kết luận, kế hoạch chuyên đề trong kỳ; nhiệm vụ nào cấp trên đã giao mà chưa đơn vị nào đưa vào kế hoạch? |
| T3 | Thư mục `D3-Bao-cao-thang-9-2026` | Lập báo cáo kết quả công tác tháng 9 năm 2026 của cơ quan từ báo cáo các đơn vị, đối chiếu với kế hoạch tháng, phát triển từ báo cáo tháng 8 đã ban hành |
| T4 | Tệp `Du-thao_Chuong-trinh-cong-tac-thang-10-2026_van-ban-Dang_an-danh.docx` | Rà soát chính thức dự thảo này theo KTC-Ra-Soat-897. Đây là văn bản của cơ quan khác, không áp quy ước riêng của Trường |

So kết quả với `Du-lieu-gia-dinh/_Dap-an-KHONG-dua-vao-cong-cu/DAP-AN.md`. Công cụ bỏ sót hoặc nêu thêm là bình thường — ghi lại để nói thật khi trình diễn.

## Bước 2 — Quay phần đầu mỗi thao tác (mỗi đoạn 30–45 giây)

1. Đặt độ phân giải màn hình 1920×1080, phóng chữ Claude Desktop 125%.
2. Mở **Snipping Tool → Ghi (Record)**, quét cửa sổ Claude Desktop, bấm Bắt đầu.
3. Kéo tệp vào, gõ lệnh, để công cụ bắt đầu làm việc khoảng 20–30 giây (thấy công cụ đọc tệp, gọi kỹ năng) rồi dừng. Không cần nói.
4. Lưu vào `Video-thao-tac/quay/` với tên **T1.mp4, T2.mp4, T3.mp4, T4.mp4**.

## Bước 3 — Ghép (01 lệnh, khoảng 01 phút)

```
python Video-thao-tac/ghep_video.py
```

Kết quả ở `Video-thao-tac/xuat/`: 04 video có giọng thuyết minh và dòng “Dữ liệu giả định phục vụ trình diễn”. Hoặc nhắn Claude Code: “ghép 4 video thao tác”.

## Khi trình diễn

Chiếu video thao tác (30–45 giây) → mở tệp tương ứng trong `Ket-qua-chay-truoc/` → nói các điểm trong `DAP-AN.md`.
