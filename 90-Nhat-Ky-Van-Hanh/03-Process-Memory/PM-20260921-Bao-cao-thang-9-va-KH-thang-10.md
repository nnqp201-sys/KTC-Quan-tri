# PM-20260921 — Báo cáo kết quả tháng 9 và kế hoạch tháng 10/2026 (cấp Trường)

**Loại:** dựng sản phẩm kỳ thật (đầu vào thật đầu tiên có cột Ib/IIb/IIa cùng kỳ) · **Kết quả:** `30-Ket-Qua/2026-09-21/Bao-cao-thang-9/` (docx + 2 xlsx + ghi chú đối soát)

## Đã làm
- Phụ lục T9 = KH-834 (47+6 nhiệm vụ) + KPI từ IIb; chỉ khớp 10/47, 24 nhiệm vụ đơn vị chủ trì chưa nộp, 13 "không thấy" — không kết luận chưa làm.
- KH T10 (31 nhiệm vụ) từ Ib "Đưa vào KH Trường" + lãnh đạo Trường chỉ đạo, CTCT năm 2026 mục tháng 10, TB 1019, IIb TCCB.
- Tường thuật docx **soạn tay** từ 10 IIa; `build_bc2.py` (ghép mảnh tự động) ra văn phong kém — không dùng lại cho kỳ sau.

## Phát hiện
- Đầu vào hiện thiếu P-QLĐT (cả 3 loại), K-KTNL (IIb, Ib), CĐCS, ĐTN, Phòng TH-HC&QT (IIb chỉ tên nhiệm vụ).
- `trich_tuong_thuat.py` gom đơn vị theo thư mục con — cấu trúc nộp mới (theo loại tệp, tên tệp = đơn vị) làm nó gom sai; Khoa KTCN dùng mẫu IIa không chia Trục nên parser ra 0 ý.
- Ghi chú Ib có giá trị mới "Kế hoạch của Trường" ngoài "Đưa vào KH Trường"; 4 Khoa để trống cột này.
- Kế hoạch quý IV chưa có; KH-834 lỗi mẫu: dòng lạc dòng 6, khối "Nơi nhận" lặp, "Đàng ủy".
- Tệp làm việc nằm ở scratchpad (`t9_*.py`), chưa đưa vào `29-Cong-Cu/`.

## Còn mở
Danh sách yêu cầu nộp bổ sung, xác nhận đối chiếu gần đúng, số hiệu/ngày, rà soát 897, `tra_hieu_luc.py` — xem `00-Ghi-chu-doi-soat-thang-9-va-KH-thang-10.md`.
