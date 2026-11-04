# Đối chiếu bản ChatGPT — Quy trình Dự án nhóm C (Trường CLC, vốn CTMTQG) — 28/10/2026

Chưa thực hiện rà soát theo KTC-Ra-Soat-897. Trạng thái: `DAT_CO_DIEU_KIEN`. Bản ChatGPT: `Downloads/Cong bo gia/ChatGPT. Quy-trinh-du-an-nhom-C_Truong-CLC_CTMTQG_20261028.docx` (75 dòng, 8 cột, 6 giai đoạn A–F).

## 1. Kết luận
Cơ chế nguồn đúng: đây là **vốn đầu tư công**, không áp quy trình chi thường xuyên. Mọi điều luật tôi kiểm được trên toàn văn đều khớp. Tôi chỉ bổ sung 6 đoạn (Track Changes), không viết lại bảng.

## 2. Đã kiểm khớp (toàn văn trong kho KTC-Database)
- Luật Đầu tư công VBHN 03/2026: khoản 5 Điều 9 và khoản 4 Điều 11 (giáo dục, nhóm C dưới 90 tỷ); điểm a, d khoản 6 Điều 19 (nhiệm vụ chuẩn bị đầu tư và dự án CTMTQG không cần quyết định chủ trương riêng); Điều 38; Điều 57 (nhóm C không quá 03 năm, không tính chuẩn bị đầu tư và quyết toán).
- NĐ 387/2026 Điều 52, 53 (hiệu lực 12/10/2026; chuyển tiếp khoản 1, 2); NĐ 358/2025 Điều 6, 9, 10, 16–22 (dự án đặc thù, không áp cho dự án này), 45–50, 58.
- QĐ 64/2026/QĐ-UBND: đơn vị quản lý vốn báo cáo hằng tháng **trước ngày 02 của tháng báo cáo** (gửi Sở Tài chính), đúng như bản ChatGPT.
- NĐ 217 (khoản 2 Điều 27, Điều 31, 39), 206, 207, 210/2026; NĐ 214/2025 hợp nhất (khoản 4 Điều 78): đã kiểm ở đợt chi thường xuyên.
- Số liệu dự án khớp tệp `29-Cong-Cu/dau_tu_cong/du-an_CLC-2026-2030.yaml`: 24.894.000.000 · 1.519.778.268 (= 852.345.246 + 667.433.022, đã cộng lại) · 260 triệu (200 + 60) · ngày ký các quyết định.

## 3. Đã kiểm trên nguồn chính thức, chưa có trong kho
NĐ 193/2026 (01/6/2026, hiệu lực 01/7/2026; Điều 21 nhóm C: lập hồ sơ 04 tháng, thẩm tra 02 tháng, phê duyệt 07 ngày; bãi bỏ Điều 30–47 NĐ 254/2025); TT 73/2026/TT-BTC (25/6/2026; mẫu 01–12/QTDA). Đề nghị nạp vào kho 01.

## 4. Tôi bổ sung (tác giả "Nội dung bổ sung (Claude)")
1. **Vốn 2026 chỉ bằng ~17% dự toán chuẩn bị** (260 triệu so với 1.519,78 triệu; chênh 1.259.778.268 đồng) — bản ChatGPT nêu số nhưng không nêu khoảng hụt và hệ quả với hai hợp đồng.
2. **NĐ 387 Điều 53 khoản 5, 6, 7**: rà soát danh mục dự án trong 90 ngày làm việc kể từ 12/10/2026; kế hoạch 2027 theo cơ chế trước hợp nhất.
3. **Ranh giới với đề xuất CTMTQG hiện đại hóa GD&ĐT** (cùng mục tiêu ký túc xá, thiết bị): bản ChatGPT không nhắc; tri thức chuyên đề ghi TB 916 yêu cầu tránh trùng lắp.
4. **Gia hạn vốn nhóm C** (khoản 3 Điều 57; điểm đ cho dự án không cần chủ trương).
5. **Trạng thái đăng tải kết quả LCNT**: sổ nội bộ ghi hạn trước 03/11; ChatGPT ghi đã đăng 27/10 theo tệp Hệ thống. Chỉ coi là đã đăng khi có bản chụp có dấu thời gian.
6. Đoạn ghi trạng thái đối chiếu từng nguồn.

## 5. Chưa kiểm được / cần người có thẩm quyền
- QĐ 2158, 2161, 2236, 2374, 2375, phụ lục S022, dự thảo hợp đồng, báo cáo giải ngân tháng 10: **không có trong kho**; số liệu lấy từ bản ChatGPT và tệp yaml (hai nguồn khớp nhau). Cần đối chiếu bản ký.
- Người quyết định đầu tư và duyệt BCKTKT: Điều 38.3.c Luật ĐTC chỉ nêu dự án đã có quyết định chủ trương; dự án CTMTQG không có → cần văn bản phân cấp của tỉnh.
- Phạm vi chuyển tiếp Điều 53 NĐ 387 và mã nội dung Chương trình; tên dự án (2026–2030) lệch phụ lục vốn (2026–2028).
- Hợp đồng đã ký và ngày hiệu lực (120 ngày tư vấn tính từ hiệu lực).
- Số lượng ba con số tổng chỉ tiêu đào tạo (12.365/12.635/12.625) trong BC 326 không liên quan quy trình này, chỉ lưu ý không dùng ra ngoài.

## 6. Thể thức
`kiem_the_thuc.py`: bản sạch **0 gợi ý**; bản Track Changes còn TT20 Mức 3 (không viết hoa sau dấu hai chấm — cố ý giữ nguyên vì là bản dấu vết). Đã đưa chữ lên cỡ 14, giữ quốc hiệu và tên cơ quan cỡ 13, ẩn đầu trang ở trang 1. Chưa xem trang bằng PDF.
