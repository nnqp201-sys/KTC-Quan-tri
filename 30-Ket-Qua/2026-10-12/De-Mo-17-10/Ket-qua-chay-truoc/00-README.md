# Kết quả chạy trước — mở khi trình diễn

Dựng ngày 12/10/2026 trên Claude Code từ chính bộ dữ liệu `Du-lieu-gia-dinh/` (không đọc tệp đáp án). Dùng để trình chiếu sau mỗi đoạn video thao tác,
và làm phương án dự phòng khi mất mạng. Khi chạy trực tiếp trên Claude Cowork, câu chữ và cách trình bày sẽ khác; nội dung phát hiện cần tương đương.

| Tệp | Phần | Nội dung | Kết quả chính |
|---|---|---|---|
| `Phan-1_Tong-hop-ke-hoach-quy-IV-2026_ket-qua-chay-truoc.xlsx` | 1 | 05 trang tính: Bảng kiểm hồ sơ 06 đơn vị; nhiệm vụ thiếu thông tin; nhiệm vụ trùng; đối chiếu văn bản chỉ đạo; dự thảo kế hoạch quý của cơ quan | 01 đơn vị sai mẫu (trả lại); 05 nhiệm vụ thiếu thời hạn hoặc sản phẩm; 01 cặp trùng rõ, 02 cặp nghi trùng (01 cặp đúng, 01 cặp không trùng — cần người xem); 02 nhiệm vụ cấp trên giao chưa ai đăng ký; dự thảo kế hoạch 35 nhiệm vụ có ghi nguồn |
| `Phan-2_Doi-chieu-ke-hoach-bao-cao-thang-9-2026_ket-qua-chay-truoc.xlsx` | 2 | Đối chiếu 24 nhiệm vụ kế hoạch tháng với báo cáo 06 đơn vị; tỷ lệ theo 06 trục | 21 có báo cáo; 03 chưa có thông tin (01 đã có Quyết định số 215/QĐ-CQA trên Hệ thống); 01 số liệu lệch (112 và 120 lượt người); 01 nội dung hai đơn vị cùng nhận |
| `Phan-2_Du-thao-Bao-cao-thang-9-2026_Co-quan-A_ket-qua-chay-truoc.docx` | 2 | Dự thảo báo cáo tháng 9 của cơ quan, cùng bố cục báo cáo tháng 8, mỗi nội dung ghi nguồn, chỗ cần xác nhận được đánh dấu | Bản nháp để người tổng hợp biên tập |
| `BaoCao_RaSoat-897-v2.25_Chuong-trinh-cong-tac-thang-10-2026_van-ban-Dang_an-danh.docx` | 3 | Báo cáo rà soát 08 phần, hệ quy chiếu văn bản của Đảng | 25 phát hiện: 0 Mức 1, 07 Mức 2, 13 Mức 3, 05 Mức 4 |

**Hai điểm nên nói thật khi trình diễn** (cho thấy vì sao luôn cần người kiểm tra):
- Phần 1: Công cụ nêu cặp “Sửa đổi Quy chế chi tiêu nội bộ” và “Sửa đổi Quy chế làm việc” là nghi trùng — thực tế là hai việc khác nhau.
- Phần 2: Với nhiệm vụ “Kiểm tra chuyên môn tại đơn vị cơ sở B” chưa có báo cáo, công cụ gợi ý Kế hoạch số 330/KH-CQA (kế hoạch kiểm tra quý IV) làm minh chứng — gợi ý này không đúng, người tổng hợp phải loại.

Phép so khớp nhiệm vụ dùng thuật toán cố định (độ giống theo cặp từ): từ 0,60 là khớp rõ; 0,45–0,59 là nghi vấn; dưới 0,45 là không khớp. Sinh lại: `python ket_qua_chay_truoc.py`.
