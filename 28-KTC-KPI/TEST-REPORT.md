# TEST-REPORT — ktc-kpi-lap-ke-hoach v1.0 (24/9/2026)

Không đóng gói tệp này vào `.skill` (`dong_goi_kpi.py` bỏ qua).

## 1. Ca thử tự động — ĐẠT

| Bộ | Kết quả | Nội dung chính |
|---|---|---|
| `92-Kinh-Nghiem/02-Regression/Cases/test_kpi_calc.py` | 44/44 ĐẠT | Biên xếp loại 100/90/89,99/70/69,99/50/49,99/0; trần 100% (Đ11.6); Trục chính 40,00% / 39,99% (Đ12.3); nhóm chung 4,99 điểm, tổng 32 (Đ10.4); 4 mức Đ10.5, 3 mức Đ18; thiếu phương án hệ số → lỗi; mức độ lạ → lỗi; A, A×B (4,5 × 2,0 = 9,0), dòng lệch Nhóm, dòng 29.22; sản phẩm ngoài Danh mục → lỗi; gợi ý Danh mục so từ nguyên vẹn; thư mục `KPI-ca-nhan/` bị git bỏ qua |
| `92-Kinh-Nghiem/02-Regression/Cases/test_validate_plan.py` | 26/26 ĐẠT | Mẫu không bị ghi đè, giữ 990 công thức; chặn ghi vào `assets/`; kế hoạch sạch 0 LỖI; KH01–KH03, KH05, KH06, KH08–KH10, KH13–KH15 bắt đúng ca sai, bỏ qua ca sạch; 21 đầu việc/Trục bị chặn; 6 mẫu đọc đúng cấu trúc |
| `29-Cong-Cu/kiem_tra_he_thong.py` | 0 lỗi · 0 cảnh báo | C1 gói hợp lệ, C2 không liên kết gãy, C4 gói khớp nguồn, C5 `19-Quy-Tac-KPI.md` khớp mọi bản rời và 2 gói |

Ca của lệnh chưa có: tập thể < 70%, HTXS vượt 20%, 01 quý Không hoàn thành — thuộc giai đoạn 2–3 (chấm điểm, tổng
hợp), chưa có script `tong_hop.py`.

## 2. Chạy trọn quy trình trên mẫu thật — ĐẠT

| Tình huống | Lệnh | Kết quả |
|---|---|---|
| Không chọn phương án hệ số | `kpi_mau.py --nhom hanh-chinh …` (thiếu `--phuong-an`) | Mã 2, "Chưa chọn phương án … không có mặc định. Hỏi người dùng." |
| Giáo vụ khoa Y-Dược, Quý IV, phương án `A`, sản phẩm ghi loại chung ("Kế hoạch") | `kpi_mau.py --nhom giao-vu --phuong-an A` | Mã 2, liệt kê 4 dòng không khớp Danh mục — dừng hỏi, không tự gán |
| Như trên, phương án `muc-do` | `kpi_mau.py --nhom giao-vu --phuong-an muc-do --quy IV --nam 2026` | Mã 0; tệp đúng mẫu, tiêu đề "QUÝ IV NĂM 2026"; cảnh báo KH09 bắt "100% viên chức toàn khoa"; KH07, KH11, KH13 đúng; `kiem_the_thuc.py` 0 lỗi Mức 1–2 |
| Viên chức hành chính, Quý IV | `kpi_mau.py --nhom hanh-chinh --phuong-an muc-do` | Mã 0; 990 công thức, 26/21/61 vùng gộp ô, danh sách chọn giữ nguyên; điểm chấm 100/120/150/200 khớp hệ số |

## 3. Kiểm định tuyến (kích hoạt skill) — PHÂN TÍCH TĨNH, CHƯA CHẠY TRÊN CLAUDE CHAT

Môi trường Claude Code không nạp skill này nên **không đo được** việc kích hoạt thật. Bảng dưới so câu hỏi với
`description` của skill này và các skill lân cận (`quan-tri`, `bao-cao`, `ke-hoach`). **Cần chạy lại trên Chat/Cowork
sau khi cài** rồi sửa cột "Thật".

| # | Câu hỏi | Mong đợi | Căn cứ trong description | Thật |
|---|---|---|---|---|
| 1 | "Lập KPI quý IV cho tôi, giáo vụ khoa Y-Dược" | Kích hoạt | "lập KPI quý", "giáo vụ khoa" | chưa chạy |
| 2 | "Làm Phụ lục kèm Bản cam kết KPI quý IV" | Kích hoạt | "Phụ lục kèm Bản cam kết KPI" | chưa chạy |
| 3 | "Chấm điểm KPI quý III của tôi" | KHÔNG kích hoạt | "KHÔNG dùng để chấm điểm, tự đánh giá, xếp loại"; `quan-tri` có "quy đổi KPI và xếp loại" | chưa chạy |
| 4 | "Tính % KPI theo Trục của khoa tháng 9" | KHÔNG kích hoạt (→ `bao-cao`) | "KHÔNG dùng cho KPI đơn vị theo Trục … TB 736"; `bao-cao` có "tính % KPI theo Trục" | chưa chạy |
| 5 | "Sửa kế hoạch KPI đã duyệt vì có nhiệm vụ đột xuất" (biên, Đ13.4) | Kích hoạt, lập bản đề nghị điều chỉnh, không sửa đè | "sửa kế hoạch KPI đã duyệt"; SKILL.md bước 7 | chưa chạy |
| 6 | "Hệ số của đầu việc này là bao nhiêu?" | Hỏi phương án, không trả A×B | SKILL.md bước 3, ví dụ 2 | chưa chạy |

Rủi ro đã thấy khi phân tích: câu 3 có từ "KPI" và "quý" như skill này — phụ thuộc vào vế loại trừ; nếu chạy thật
kích hoạt nhầm, thêm "chấm điểm KPI" vào vế KHÔNG ở đầu description.
