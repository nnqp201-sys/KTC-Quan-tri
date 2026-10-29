# dau_tu_cong — bộ công cụ dựng và kiểm văn bản dự án đầu tư công

Nguồn sự thật: `du-an_CLC-2026-2030.yaml` (tên dự án, vốn, số/ngày văn bản, gói thầu, nhà thầu, nhân sự). Sửa ở đó rồi dựng lại; không gõ số vào script. Dự án khác: sao chép tệp YAML, đặt tên `du-an_<ma>.yaml`, chạy với `--yaml` hoặc biến `KTC_DU_AN`.

| Tệp | Việc |
|---|---|
| `du_an.py` | Nạp YAML |
| `lap_pt_qd_kqlcnt.py` | Phiếu trình ký + QĐ phê duyệt kết quả LCNT (chỉ định thầu rút gọn): `--out`, `--goi KS\|QLDA\|all`, `--chi pt\|qd` |
| `kiem_nhat_quan_du_an.py` | Đối chiếu văn bản (.docx) với YAML: ngày vô lý, ngày/số hiệu lệch, tên dự án, số tiền lạ, lỗi gõ đã gặp |
| `lap_ttr_khlcnt.py`, `build_khlcnt_v5.py`, `lap_phieu_897_khlcnt.py` | Tờ trình, QĐ KHLCNT, phiếu rà soát 897 (đợt 07/10/2026; còn số liệu trong script, chưa chuyển sang YAML) |
| `lap_bc_giai_ngan_t9.py`, `lap_bieu_04a_t9.py` | Báo cáo giải ngân tháng 9 (Track Changes) và Biểu 04a (đợt 14/10/2026; chưa chuyển sang YAML) |

Công cụ liên quan ngoài thư mục: `29-Cong-Cu/ocr_pdf.py` (OCR tiếng Việt cho bản scan), `kiem_the_thuc.py`, `kiem_vien_dan.py` (VD13-VD15).

Ví dụ:
```
python 29-Cong-Cu/dau_tu_cong/lap_pt_qd_kqlcnt.py --out 30-Ket-Qua/<ngày>/Soan-Thao-VB
python 29-Cong-Cu/dau_tu_cong/kiem_nhat_quan_du_an.py <tep1.docx> <tep2.docx>
python 29-Cong-Cu/ocr_pdf.py <ho-so-nang-luc.pdf> --trang 1-10 --ra ket-qua-ocr.md
```
Lưu ý: các script chỉ đọc mẫu từ kho dữ liệu nền và thư mục OneDrive của P-THHC; không ghi vào kho.
