```yaml
memory_id: PM-20260920-001
created_at: 2026-09-20
memory_type: process
status: open
task_type: bo_sung_va_ra_soat_897_de_an
scope: 1 đề án (De_an_Hang_A_Du_thao_lan_3.docx), 4 tệp đính kèm
project_name: KTC-Quan-tri
```

# Bổ sung và rà soát 897 — Đề án đào tạo, sát hạch lái xe mô tô hạng A (dự thảo lần 3)

**Kết quả:** `30-Ket-Qua/2026-09-20/De-an-Hang-A/` — bản sửa Track Changes (212 thay đổi), nhật ký sửa đổi, báo cáo rà soát 897 (8 phần).
**Kết luận rà soát:** chưa đủ điều kiện trình ký (3 vấn đề Mức 1, 5 Mức 2, 8 Mức 3, 7 Mức 4).

## Nguồn đã đọc
- Đề án lần 3; Thông báo 797/TB-CĐKT (09/7/2026); Biên bản kiểm tra của Sở Xây dựng 10/7/2026 (PDF quét, không có lớp chữ — đọc từ ảnh trích bằng pypdf); Bảng kiểm kê tài sản của Khoa (xlsx).
- KTC-Database kho 01: NĐ 94/2026, TT 14/2025, TT 17/2026, TT 107/2026 (QCVN 15:2026/BCA), TT 108/2026, Luật TTATGT, Luật GDNN; kho 02: QĐ 679, QĐ 1777.
- Internet: Chỉ thị 23-CT/TW, Chỉ thị 10/CT-TTg (chỉ xác minh tồn tại và ngày).

## Phát hiện đáng nhớ
- **Bản dự thảo dùng sai điều kiện sát hạch hạng A.** Nêu trung tâm loại 2, ≥18.000 m², trích từ trang web luật. Văn bản gốc (NĐ 94/2026 khoản 4, 5 Điều 3; Điều 31) cho hạng A sát hạch tại trung tâm loại 3 hoặc sân tập lái để sát hạch mô tô loại 2. Bài học: dữ liệu kỹ thuật do người dùng hoặc AI tra web trước đó phải đối chiếu lại với văn bản gốc trong kho.
- Nhà giáo: chỉ 01/11 có giấy phép lái xe hạng A; giáo viên dạy thực hành cần hạng tương ứng hoặc cao hơn.
- NĐ 94/2026 (20.000/4.000 m²) và QCVN 15:2026/BCA (18.000/3.600 m²) lệch nhau về diện tích trung tâm — chưa có kết luận.
- Đề án tự mâu thuẫn về nguồn vốn ("không phát sinh đầu tư ngoài Giai đoạn 1" so với Bảng 8 và Phụ lục IV).

## Giới hạn
- Không có LibreOffice trên máy: chưa xem trực quan bản Track Changes; cần mở bằng Word. Cỡ chữ mức run chưa đo (nằm ở style).
- QĐ 1944, BC 393, QĐ 1557, BC 116, phương án đầu tư sân (khái toán 13/9/2026) không có trong kho — Mức 4.
- Bảng kiểm kê tài sản chưa hoàn tất (ô thời điểm, ban kiểm kê, chữ ký trống; có dòng trùng).
- Ô "Người kiểm tra" của báo cáo để trống — cần người có thẩm quyền điền.

## Kỹ thuật tái sử dụng
- `ktc_trackchanges.py` chưa có thao tác điền ô bảng, chèn hàng, chèn bảng, chèn đoạn theo đối tượng. Các hàm phụ đã viết trong phiên (thay theo đoạn, đoạn mới có dấu vết ở dấu đoạn, hàng bảng đánh dấu `trPr/ins`, bảng mới sao từ bảng có sẵn) chưa đưa vào mô-đun — cân nhắc bổ sung (chuyển `ktc-tu-cai-tien`).
- Trích văn bản gốc từ `.docx` bằng script tự viết phải đặt giới hạn ký tự đủ lớn: lần đầu giới hạn 9.999 ký tự cắt cụt NĐ 94 và cho kết luận thiếu.
