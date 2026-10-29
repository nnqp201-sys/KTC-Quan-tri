# PM-20260913-Ke-hoach-trien-khai-QD141-Bao-ve-bi-mat-nha-nuoc

- **Tác vụ**: (a) Rà soát chính thức trước khi trình ký
- **Hồ sơ**: Dự thảo Kế hoạch triển khai thực hiện QĐ 141/2026/QĐ-UBND ngày 24/8/2026 của UBND tỉnh Quảng Ngãi ban hành Quy chế bảo vệ bí mật nhà nước (số .../KH-CĐKT, chưa cấp số)
- **Ngày**: 13/9/2026
- **Phiên bản đã dùng**: Skill ktc-ra-soat-897 v2.22; Checklist 01,02,03,04,05,07,08; script tools/build_ktc897_report.py; tools/_read_input_properties.py

## Các bước đã chạy
1. Bước 0a — xác định hệ quy chiếu: HỆ HÀNH CHÍNH NHÀ NƯỚC (ký hiệu /KH-CĐKT không chứa năm; khối đầu đúng Mẫu 2.1 TB 597). Không áp hệ Đảng, không áp hệ đoàn thể.
2. Bước 0b — đọc thuộc tính định dạng thật: A4 ngang 297x210; lề 20/20/30/20mm; Normal = Times New Roman 14pt; cỡ chữ 16 thành phần thể thức khớp bảng TB 597 (Checklist 08 mục 4) → ĐẠT.
3. Tra kho 01-04 (Google Drive), đọc nội dung thật:
   - TÌM THẤY: Luật BVBMNN 117/2025/QH15 ("17. Luat Bao ve bi mat nha nuoc.docx", 01-Legal-Database); TB 1019/TB-CĐKT ngày 07/9/2026; QĐ 1868/QĐ-CĐKT ngày 26/8/2026; QĐ 1763/QĐ-CĐKT ngày 13/8/2026.
   - KHÔNG CÓ TRONG KHO: NĐ 63/2026/NĐ-CP ngày 28/02/2026; QĐ 141/2026/QĐ-UBND ngày 24/8/2026 + Quy chế kèm theo (chỉ có bản người dùng đính kèm phiên).
4. Đọc toàn văn 4 tệp đính kèm; đối chiếu từng nhiệm vụ của dự thảo với Điều 3–19 Quy chế 141, Điều 3–14 NĐ 63/2026, Điều 5–26 Luật 117/2025/QH15.
5. Xuất báo cáo 8 phần bằng build_ktc897_report.py.

## Phát hiện chính
- Tổng 36 mục kiểm tra: **05 Mức 1**, 19 Mức 2, 10 Mức 3, 01 Mức 4, 01 Đạt.
- **Mức 1**:
  - (4) Sai thẩm quyền: dự thảo giao Trường "thanh tra nội bộ" — Điều 15.1 Quy chế 141 giao Công an tỉnh CHỦ TRÌ thanh tra; Trường chỉ tự kiểm tra và phối hợp.
  - (8) Thiếu hẳn nhóm nhiệm vụ xác định BMNN và độ mật (Điều 3 Quy chế; Điều 10 Luật).
  - (9) Thiếu nhiệm vụ tách bạch máy tính/dữ liệu mật khỏi hạ tầng đám mây và công cụ AI — xung đột trực tiếp với TB 1019 mục II.1 (Google Drive/OneDrive dùng chung) và II.6 (đẩy mạnh AI); Điều 5 khoản 2, 7, 10 Luật 117/2025/QH15 nghiêm cấm.
  - (10) Thiếu hệ thống sổ quản lý BMNN (Sổ đăng ký đi/đến, Sổ sao chụp, Sổ chuyển giao — Điều 4.10, 5 Quy chế; Phụ lục II, III NĐ 63).
  - (16) Nhiệm vụ báo cáo định kỳ thiếu nơi nhận (Công an tỉnh qua Phòng An ninh chính trị nội bộ) và mốc chốt số liệu 15/12 năm trước → 14/12 năm báo cáo; diễn đạt "trước 16/12" sai sắc thái so với "chậm nhất vào ngày 16/12".
- Mâu thuẫn nội tại quan trọng: QĐ 1868/QĐ-CĐKT (26/8/2026) bãi bỏ Nội quy BVBMNN 1340/QĐ-CĐKT "để thống nhất thực hiện theo QĐ 141", nhưng nhiệm vụ 3 của dự thảo lại giao xây dựng "Quy chế/Quy định BVBMNN nội bộ" → cần đổi thành quy trình/hướng dẫn cụ thể hóa.
- Sai logic tiến độ ngân sách: lập dự toán tháng 02/2027 là sau khi năm ngân sách 2027 đã bắt đầu (Điều 16.2 Quy chế).
- Thể thức và cỡ chữ ĐẠT toàn bộ — nhóm lỗi thường gặp nhất lần này không có.

## Quyết định phân loại đáng lưu ý
- KHÔNG bắt lỗi "thiếu căn cứ QĐ 988/QĐ-CĐKT": Checklist 08 mục 1 chỉ áp dụng cho QUYẾT ĐỊNH thuộc thẩm quyền Hiệu trưởng; đây là Kế hoạch → chỉ nêu Mức 4 góp ý.
- KHÔNG bắt lỗi "Các đoàn thể nhà trường" ở Nơi nhận thành lỗi Mức 1/2 — chỉ Mức 3 (lệch mẫu TB 597, nên tách riêng từng tổ chức).
- Trường KHÔNG có thẩm quyền lập danh mục BMNN (Điều 9 Luật) → kiến nghị viết là "rà soát, đối chiếu danh mục do Thủ tướng ban hành", không phải "lập danh mục".

## Nội dung người dùng chỉnh/bác bỏ
Chưa có phản hồi tại thời điểm ghi.

## Vấn đề còn mở
- Chưa xác minh hiệu lực hiện hành của NĐ 63/2026/NĐ-CP và QĐ 141/2026/QĐ-UBND trên https://phapluat.gov.vn/ — đề nghị bộ phận pháp chế tra.
- Cần nạp NĐ 63/2026/NĐ-CP và QĐ 141/2026/QĐ-UBND vào 01-Legal-Database (dùng Skill ktc-database).
- Cần xác minh tên gọi chính thức của "Bộ phận Thiết bị" (không có trong bảng 18 đơn vị TB 597).
- Cần đối chiếu dải điểm chấm công việc 100–200 và hệ số 1,0–2,0 với Phụ lục V QĐ 1763/QĐ-CĐKT.

## Hành động tiếp theo
Phòng TH-HC&QT hoàn thiện theo 12 bước tại Phần VII báo cáo, dứt điểm trong tuần 15–19/9/2026 để kịp mốc 25/9/2026 theo TB 1019/TB-CĐKT.

## ID đầu ra
Bao_cao_ra_soat_KTC897_Ke_hoach_trien_khai_QD141_BVBMNN_20260913.docx (8 phần, A4 ngang, 62.892 bytes)
