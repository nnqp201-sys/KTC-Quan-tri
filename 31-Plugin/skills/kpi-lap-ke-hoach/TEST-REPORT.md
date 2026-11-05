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

## 3. Kiểm định tuyến (kích hoạt skill) — phân tích tĩnh 24/9; câu 1–5 ĐÃ CHẠY THẬT 25/9 (xem mục 4.3)

Môi trường Claude Code không nạp skill này nên **không đo được** việc kích hoạt thật. Bảng dưới so câu hỏi với
`description` của skill này và các skill lân cận (`quan-tri`, `bao-cao`, `ke-hoach`). **Cần chạy lại trên Chat/Cowork
sau khi cài** rồi sửa cột "Thật".

| # | Câu hỏi | Mong đợi | Căn cứ trong description | Thật |
|---|---|---|---|---|
| 1 | "Lập KPI quý IV cho tôi, giáo vụ khoa Y-Dược" | Kích hoạt | "lập KPI quý", "giáo vụ khoa" | ĐẠT (25/9) |
| 2 | "Làm Phụ lục kèm Bản cam kết KPI quý IV" | Kích hoạt | "Phụ lục kèm Bản cam kết KPI" | ĐẠT (25/9) |
| 3 | "Chấm điểm KPI quý III của tôi" | KHÔNG kích hoạt | "KHÔNG dùng để chấm điểm, tự đánh giá, xếp loại"; `quan-tri` có "quy đổi KPI và xếp loại" | ĐẠT — vào `kpi-tu-danh-gia` (25/9) |
| 4 | "Tính % KPI theo Trục của khoa tháng 9" | KHÔNG kích hoạt (→ `bao-cao`) | "KHÔNG dùng cho KPI đơn vị theo Trục … TB 736"; `bao-cao` có "tính % KPI theo Trục" | ĐẠT — vào `bao-cao` (25/9) |
| 5 | "Sửa kế hoạch KPI đã duyệt vì có nhiệm vụ đột xuất" (biên, Đ13.4) | Kích hoạt, lập bản đề nghị điều chỉnh, không sửa đè | "sửa kế hoạch KPI đã duyệt"; SKILL.md bước 7 | ĐẠT (25/9) — kích hoạt; hành vi bước 7 chưa chạy |
| 6 | "Hệ số của đầu việc này là bao nhiêu?" | Hỏi phương án, không trả A×B | SKILL.md bước 3, ví dụ 2 | chưa chạy (hành vi, không phải định tuyến) |

Rủi ro đã thấy khi phân tích: câu 3 có từ "KPI" và "quý" như skill này — phụ thuộc vào vế loại trừ; nếu chạy thật
kích hoạt nhầm, thêm "chấm điểm KPI" vào vế KHÔNG ở đầu description.

## 4. Giai đoạn 2 — skill `ktc-kpi-tu-danh-gia` v1.0 (25/9/2026)

### 4.1. Ca thử tự động — `test_kpi_danh_gia.py` ĐẠT (0 ca sai)

- Dò cấu trúc sheet Đánh giá **cả 6 mẫu**: 3 nhóm A = 30 (≥ 5/nhóm), 6 Trục = 70, khối II, dòng III, nhận đúng nhóm từ
  tiêu đề. Hai mẫu lệch dòng và lệch cột kết quả điều kiện (VC-Hanh-Chinh lệch 1 dòng; cột D/E) — dò động xử lý được.
- Ca ngược cấu trúc: xóa "Trục (3)" hoặc dòng III → `LoiCauTruc`, dừng, không đoán.
- Trọn quy trình trên 6 nhóm: sinh bảng hỏi → **dừng khi còn trống** → điền → đánh giá → xuất; không ghi đè kế hoạch.
- **Excel thật (COM) tính lại** tệp ra: tổng điểm khớp Python; % Trục có chặn trần khớp Python (87,1795%) trong khi công
  thức gốc của mẫu cho 169,23%.
- Ngưỡng 89,99/90 · 69,99/70 · 49,99/50; hiển thị 89,996 → "89,99" (không làm tròn lên).
- Điều kiện: bảng kiểm "Chưa có kết quả" → "Thiếu dữ liệu" (không tự cho Đạt); giờ giảng 60% → không đạt HTXS/HTT,
  đạt HT; bảng kiểm Không đạt → Đ19.1d; không có việc vượt mức → điều kiện 30% HTXS Không đạt (ca ngược: đều vượt → Đạt).
- Dừng không tự chấm: đặc thù Đ21.6a, Đ21.4; điểm tiêu chí vượt tối đa; mức nhóm chọn lệch tổng (Đ10.5); trọng tâm lệch Đ18.
- Cấu trúc mẫu nhóm A < 5 điểm → cảnh báo lỗi mẫu (ca ngược: mẫu đúng → không cảnh báo).
- Người đứng đầu cao hơn tập thể → cảnh báo Đ14.4 (ca ngược: cấp phó không áp); tự đề xuất HTXS khi 87 điểm → cảnh báo.
- Bảo mật: `TDG-*.xlsx` trong `KPI-ca-nhan/` bị `.gitignore`; `git add -A --dry-run` không đưa vào.
- Giai đoạn 1 (cùng lượt): kế hoạch xuất ra không còn L9=4/N9=100 của mẫu; dòng trống ẩn; KH16 bắt số ví dụ của mẫu,
  không báo nhầm tệp Quý III thật có số thực tế.

### 4.2. Đối chiếu sheet Đánh giá với Phụ lục QĐ 2078 trong kho

| Nhóm | Phụ lục | Kết quả |
|---|---|---|
| `truong-pho-don-vi` | XXIII | **Khớp hoàn toàn**: 17 tiêu chí con (nội dung + điểm), 6 Trục (40/7/8/5/5/5), 4 điều kiện khối II |
| `nha-giao` | XXV | **Khớp hoàn toàn**: 17 tiêu chí con, 6 Trục (40/5/10/5/5/5), 4 điều kiện |
| `bo-mon`, `giao-vu`, `hanh-chinh`, `ho-tro` | XXIV, XXVI, XXVII, XXVIII | **Chưa đối chiếu trực tiếp** — Phụ lục chưa có trong kho; đầu ra ghi rõ |

### 4.3. Kích hoạt — CHẠY THẬT 25/9/2026 (Claude Code headless, không phải Chat)

`claude -p "<câu>" --plugin-dir <plugin tạm>` (claude.exe đi kèm extension VS Code 2.1.282), đọc lời gọi `Skill` đầu
tiên. Plugin đang cài (`ktc-quan-tri` 1.9: quan-tri, bao-cao, ke-hoach…) cùng nạp — là đối thủ cạnh tranh thật.
Chi phí 16 lượt ≈ 3,8 USD. **Chưa chạy trên Claude Chat/Cowork** — cần chạy lại sau khi cài plugin 1.2.0.

| # | Câu | Mong đợi | (b) hai skill | (a) một skill gộp |
|---|---|---|---|---|
| P1 | Lập KPI quý IV cho tôi, giáo vụ khoa Y-Dược | lập kế hoạch | kpi-lap-ke-hoach ✓ | kpi-ca-nhan ✓ |
| P2 | Làm Phụ lục kèm Bản cam kết KPI quý IV | lập kế hoạch | kpi-lap-ke-hoach ✓ | kpi-ca-nhan ✓ |
| P3 | Chấm điểm KPI quý III của tôi | tự đánh giá | kpi-tu-danh-gia ✓ | kpi-ca-nhan ✓ |
| P4 | Tính % KPI theo Trục của khoa tháng 9 | không (→ bao-cao) | bao-cao ✓ | bao-cao ✓ |
| P5 | Sửa kế hoạch KPI đã duyệt vì có nhiệm vụ đột xuất | lập kế hoạch | kpi-lap-ke-hoach ✓ | kpi-ca-nhan ✓ |
| P6 | Tự đánh giá xếp loại quý IV, tôi là giáo vụ khoa | tự đánh giá | kpi-tu-danh-gia ✓ | kpi-ca-nhan ✓ |
| P7 | Tôi được Hoàn thành xuất sắc không? | tự đánh giá | kpi-tu-danh-gia ✓ | kpi-ca-nhan ✓ |
| P8 | Xếp loại tập thể Phòng tôi thế nào? | không (giai đoạn 3) | quan-tri ✓ | quan-tri ✓ |

Cả hai 8/8 ở mức chọn skill; ở (a) việc tách lập/tự đánh giá dồn vào thân SKILL.md và chưa đo. Chọn (b) — lý do tại
`DL-20260925-001`. Hành vi sau kích hoạt (P7 không khẳng định HTXS, P8 báo ngoài phạm vi) chưa đo tự động.
