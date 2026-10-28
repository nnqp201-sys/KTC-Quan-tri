---
name: ktc-dau-tu-cong
description: Soạn và kiểm bộ văn bản của dự án đầu tư công giai đoạn chuẩn bị đầu tư tại Trường Cao đẳng Kon Tum: QĐ nhiệm vụ và dự toán, phân bổ vốn, kế hoạch lựa chọn nhà thầu, tờ trình, phiếu trình, QĐ phê duyệt kết quả chỉ định thầu rút gọn, biên bản thương thảo, báo cáo giải ngân tháng (QĐ 64/2026/QĐ-UBND, Biểu 04a). Dùng khi người dùng nhắc "chuẩn bị đầu tư", "chỉ định thầu", "KHLCNT", "kết quả lựa chọn nhà thầu", "báo cáo giải ngân", "phiếu trình ký".
---

# Quy trình

1. Đọc `.claude/rules/23-dau-tu-cong-dau-thau.md` và `29-Cong-Cu/dau_tu_cong/du-an_CLC-2026-2030.yaml` (nguồn sự thật duy nhất).
2. Phát triển từ văn bản tương đồng đã ban hành (Nguyên tắc 7): QĐ 2236 (KHLCNT), QĐ 2374/2375 (KQLCNT), Phiếu trình theo QĐ 1622/QĐ-CĐKT, Tờ trình 16/TTr-THHCQT. Không dựng từ mẫu trống.
3. Dựng bằng script trong `29-Cong-Cu/dau_tu_cong/` (xem `00-README.md`): `lap_pt_qd_kqlcnt.py` đọc `du-an_CLC-2026-2030.yaml` (nguồn sự thật duy nhất); `lap_ttr_khlcnt.py`, `build_khlcnt_v5.py`, `lap_bc_giai_ngan_t9.py`, `lap_bieu_04a_t9.py` còn số liệu trong script. Hồ sơ scan: `29-Cong-Cu/ocr_pdf.py` (OCR tiếng Việt, luôn kèm độ tin cậy, phải đối chiếu bản gốc).
4. Chạy `kiem_the_thuc.py`, `kiem_vien_dan.py`; xem PDF từng trang; chạy `29-Cong-Cu/dau_tu_cong/kiem_nhat_quan_du_an.py` trên cả bộ và giao agent `ktc-kiem-nhat-quan-bo-van-ban` đọc kết quả.
5. Giao kèm: danh sách giả định cần xác nhận; việc kế tiếp; mốc hạn (agent `ktc-theo-doi-han-dau-tu-cong`).
6. Rà soát 897 trước trình ký là bước riêng; ghi rõ "chưa thực hiện rà soát theo KTC-Ra-Soat-897" khi chưa chạy.
