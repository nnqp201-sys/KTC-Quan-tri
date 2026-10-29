# 07 – Doanh nghiệp, vốn nhà nước, đất đai, tài sản công

**Nguồn:** gói v3.0, SKILL.md, khối `<mandatory_rules>` mục 13 (28/8/2026). Danh mục văn bản đối chiếu tại KTC-Database ngày 29/10/2026.
**Phạm vi:** dự thảo liên quan thành lập doanh nghiệp, góp vốn, vốn nhà nước, quyền sử dụng đất, tài sản công.
*Ghi chú tham khảo — không thay đổi mã, mức, nhãn của v4.5.*

## Nhắc nhở (nguồn v3.0)

Quyết định liên quan **thành lập doanh nghiệp, góp vốn, vốn nhà nước hoặc quyền sử dụng đất** cần được đối chiếu với: pháp luật về doanh nghiệp; pháp luật quản lý vốn nhà nước; pháp luật về đất đai và tài sản công phù hợp. **Nghị định về tự chủ (NĐ 60/2021, 111/2025, 334/2026) không đủ làm căn cứ một mình** cho các nội dung này (xem `04-Thoi-Diem-ND-334-2026.md`).

Mô-đun này không tạo mã mới, không đổi mức. Kết quả ghi vào `kiem_tra_chat_luong` dạng `[Bổ sung – tham khảo] Doanh nghiệp – vốn – đất`: dự thảo có chạm nội dung nào, các văn bản bên dưới đã đối chiếu hay chưa.

## Văn bản có trong KTC-Database để đối chiếu

| Lĩnh vực | Văn bản (tên tệp trong kho) | Ghi chú kho |
|---|---|---|
| Doanh nghiệp | VBHN 67/VBHN-VPQH Luật Doanh nghiệp, 15/8/2025 | Đang có hiệu lực |
| Vốn nhà nước tại doanh nghiệp | Luật 68/2025/QH15 Quản lý, đầu tư vốn nhà nước tại doanh nghiệp, 14/6/2025; NĐ 366/2025/NĐ-CP; NĐ 181/2026/NĐ-CP (quản lý người đại diện vốn nhà nước) | Luật 68 đang có hiệu lực; nội dung từng NĐ phải đọc chính văn trước khi viện dẫn |
| Đất đai | VBHN 44/VBHN-VPQH Luật Đất đai, 16/3/2026 | Đang có hiệu lực; QĐ 120/2026/QĐ-UBND và QĐ 122/2026/QĐ-UBND của tỉnh Quảng Ngãi về phân cấp, thủ tục đất đai |
| Tài sản công | VBHN 97/VBHN-VPQH Luật Quản lý, sử dụng tài sản công; NĐ 186/2025/NĐ-CP; NĐ 127/2025/NĐ-CP; TT 120/2025/TT-BTC; QĐ 46/2025/QĐ-UBND tỉnh | Đối chiếu theo nội dung cụ thể |
| Chuyển đơn vị sự nghiệp công lập thành doanh nghiệp | NĐ 373/2026/NĐ-CP | Đọc chính văn xác định phạm vi; **không mặc định** là căn cứ cho thủ tục góp vốn |

Tên tệp đầy đủ: thư mục `01-Legal-Database/01-01- Luat Viet Nam`, `01-04- VB cua Chinh Phu`, `01-05- VB cua cac Bo`, `01-06- VB cua Tinh uy - Dang uy UBND tinh`. Số hiệu, ngày chi tiết của từng văn bản lấy từ tệp metadata cùng thư mục; bảng này chỉ là chỉ dẫn tra cứu.

## Khi áp dụng

1. Quét dự thảo tìm: "thành lập doanh nghiệp", "góp vốn", "vốn nhà nước", "vốn điều lệ", "quyền sử dụng đất", "tài sản công", "giao đất", "thuê đất".
2. Có → ghi vào `kiem_tra_chat_luong` từng lĩnh vực chạm tới và việc đối chiếu đã làm / chưa làm.
3. Văn bản cần đối chiếu mà chưa có toàn văn trong hồ sơ hoặc Kho của lõi → cổng G5 của v4.5 chặn, theo quy tắc lõi. Ghi chú này **không nới** cổng.
