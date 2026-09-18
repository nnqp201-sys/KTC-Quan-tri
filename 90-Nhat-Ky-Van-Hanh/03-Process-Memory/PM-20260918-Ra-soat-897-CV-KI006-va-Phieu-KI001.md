# PM-20260918 — Rà soát chính thức 897 dự thảo CV (KI-006) + Phiếu đề xuất Task_ID (KI-001)

**Ngày:** 18/9/2026 · **Yêu cầu:** người dùng — "làm ngay 2 việc theo hướng em đề xuất"

## KI-006 — Công văn nhắc 6 đơn vị
- Rà soát chính thức KTC-897 v3.0, Hệ A. Đo bytes thật (ZIP hợp lệ, lề 20/20/30/20, TNR).
- Đối chiếu kho: TB 736/TB-CĐKT ngày 25/6/2026, TB 817/TB-CĐKT ngày 14/7/2026 (kho 02-01) — khớp;
  người ký Hiệu trưởng Lê Trí Khải — khớp QĐ 1763/QĐ-CĐKT ngày 13/8/2026 (00-Metadata-Index).
- Kết quả: Mức 1 = 0 · Mức 2 = 5 (cỡ chữ số ký hiệu, trích yếu, nơi nhận; 2 ghi chú soạn thảo) · Mức 3 = 1
  (viết hoa "phòng/khoa" giữa câu) · Mức 4 = 3 (số liệu "trung bình 25 nhiệm vụ" chưa dẫn nguồn; thời hạn
  24/9 do Lãnh đạo quyết; Checklist 08 tự dùng lẫn "-" và "–").
- Đã sửa Mức 2 + Mức 3 bằng Track Changes (`_sua-theo-ra-soat.docx`, kiem_tra OOXML đạt). Mức 4 để người có
  thẩm quyền quyết.
- Báo cáo: `30-Ket-Qua/2026-09-18/Ra-Soat/BC-Ra-Soat-897_CV-Bo-sung-ho-so-KH-BC-thang-8-9-2026.docx`.
  Trường "Người kiểm tra" để trống chờ cán bộ phòng THHCQT điền (AI không tự điền).

## KI-001 — Phiếu đề xuất
- `30-Ket-Qua/2026-09-18/De-xuat/Phieu-de-xuat_Bo-sung-cot-Task_ID-Phu-luc-TB736.docx` — tóm tắt 1–2 trang
  cho Lãnh đạo, có ô ý kiến (Đồng ý / Điều chỉnh / Chưa đồng ý). Tài liệu tham mưu nội bộ, không số hiệu.

## Bài học
- Công cụ `ktc_trackchanges.py` chỉ theo dõi thay đổi chữ; đổi cỡ chữ phải tự gắn `w:rPrChange` để giữ
  dấu vết định dạng — cân nhắc bổ sung hàm `doi_dinh_dang()` vào công cụ.
