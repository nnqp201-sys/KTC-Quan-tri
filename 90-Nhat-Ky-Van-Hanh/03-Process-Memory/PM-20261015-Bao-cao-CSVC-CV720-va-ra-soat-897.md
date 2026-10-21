# PM-20261015 — Báo cáo CSVC, nhu cầu đầu tư theo CV 720/CĐKT-QLĐT và rà soát 897

**Ca:** phòng TH-HC&QT nhận phần việc II.5, III.3, Biểu 04 của Đề cương kèm CV 720 (Đề án nâng cao chất lượng nguồn nhân lực ngoài hệ thống chính trị; CV 4954/SGDĐT-GDNNQLĐT). Dựng báo cáo từ Đề án 07, BC 405, BC 326, BC 427; rà soát 897; sửa bằng Track Changes.
**Kết quả:** `30-Ket-Qua/2026-10-15/Bao-cao/` (v1, v2_TrackChanges, v2_ban-sach, ghi chú đối soát); `30-Ket-Qua/2026-10-15/Ra-Soat/BC-RA-SOAT-897_…docx` — 2 Mức 1, 5 Mức 2, 6 Mức 3 đã sửa; 5 Mức 4 chờ người quyết.

## Bài học

1. **Tên Cơ sở 4, Cơ sở 5 trong hồ sơ cũ (Đề án 07, BC 405) là tên cũ** — chép nguyên sang văn bản mới là Mức 1 (Checklist 08 mục 3.5). Khi lấy số từ hồ sơ đã gửi, đổi tên đơn vị, cơ sở theo Checklist 08 mục 3.2 trước.
2. **Người dùng có thể sửa tệp bằng Word (Track Changes) giữa hai lượt.** Đọc lại `nhat_ky_sua_doi` trước khi sửa; không ghi đè. Word lưu lại tách gạch nối không ngắt dòng thành run `[noBreakHyphen, t]`: công cụ `ktc_trackchanges.py` sẽ nhân đôi dấu gạch nếu cắt run đó. Cách xử lý đã dùng (`scratchpad/sua_theo_897.py`): đổi tạm thành U+2011, sửa, rồi đổi lại thành `w:noBreakHyphen`; chạy `doi_chieu_goc` được 0,927. Nên đưa vào công cụ.
3. **"Giải ngân 100%" chỉ đúng cho phạm vi nguồn nêu** (BC 326: 58.244 + 7.311), không áp cho tổng 78.920 — đối chiếu câu kết luận với phạm vi số trong văn bản gốc.
4. **`tra_hieu_luc.py` khớp số hiệu không kèm cơ quan ban hành:** QĐ 1951/QĐ-CĐKT bị khớp với QĐ 1951/QĐ-TTg. Luôn đối chiếu thủ công đơn vị ban hành.
5. **Tệp QĐ 805/QĐ-UBND trong kho là bản dự thảo (chưa số, ngày)** — số hiệu, ngày chỉ có từ BC 427 và tên tệp (Mức 4).
6. **Thông tư 35/2021/TT-BLĐTBXH:** Luật GDNN 124/2025/QH15 (hiệu lực 01/01/2026) khiến hiệu lực chưa rõ trong kho; người dùng xác nhận còn hiệu lực (15/10/2026), chưa tra nguồn ngoài — giữ viện dẫn.
7. **Hạn trong CV 720 (17 giờ 14/10/2026) đã quá khi bắt đầu làm (15/10).** Nêu ngay đầu báo cáo kết quả.
