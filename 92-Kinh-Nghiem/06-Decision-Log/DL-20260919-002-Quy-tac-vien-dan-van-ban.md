# DL-20260919-002 — Quy tắc viện dẫn văn bản: NĐ 30 · Pháp lệnh hợp nhất · quy ước Trường

**Ngày:** 19/9/2026 · **Người quyết định:** người dùng (chủ dự án)

**Bối cảnh:** người dùng yêu cầu tìm hiểu ba nguồn quy tắc viện dẫn và áp dụng vào KTC-Quan-tri:
- viện dẫn luật theo NĐ 30;
- viện dẫn văn bản hợp nhất theo Pháp lệnh hợp nhất (do **Ủy ban Thường vụ Quốc hội** ban hành, không phải
  Quốc hội);
- quy ước của Trường trong KTC-Ra-Soat-897-v2.

Trước đó KTC-Quan-tri chỉ có bản sao `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md`, khớp byte với 897. Chưa có tệp
nào gom quy tắc căn cứ theo NĐ 30 với quy ước Trường. Chỉ gói soạn thảo có trỏ tới quy tắc hợp nhất.

**Đối chiếu chính văn** trên Google Drive (`KTC-Database/01-Legal-Database/`):
- Phụ lục I của NĐ 30/2020, Phần I, Mục II, khoản 6. Điểm a: căn cứ ban hành, *"riêng Luật, Pháp lệnh không
  ghi số, ký hiệu, cơ quan ban hành"*. Điểm b: viện dẫn lần đầu, các lần sau.
- Phụ lục II của NĐ 30, Mục V, khoản 7: viết hoa Điều, Chương khi viện dẫn.
- VBHN 118/VBHN-VPQH ngày 25/6/2026, Điều 4: điểm a quy định luật, pháp lệnh ghi **số, ký hiệu** kèm
  "(hợp nhất tại …)".

**Xung đột và chốt của người dùng (trong phiên):** NĐ 30 và 897 (`02-Noi-Dung.md` mục 1 dòng 4) quy định
luật và pháp lệnh không ghi số hiệu. Pháp lệnh Điều 4 khoản 2 điểm a lại yêu cầu ghi số khi viện dẫn qua
VBHN. Người dùng chốt:
> "KTC-ra-soat-897-v2-cai-tien đã quy định rất rõ, Văn bản hành chính thì viện dẫn Luật không ghi số hiệu"

→ **Văn bản hành chính: Luật, Pháp lệnh không ghi số hiệu, kể cả khi đã có VBHN.** Chỉ ghi tên và ngày ban
hành. Số điều, khoản lấy theo VBHN (điểm đ). Cách viện dẫn VBHN theo Pháp lệnh vẫn áp cho nghị định, thông
tư và văn bản địa phương (điểm b, c).

**Lệch phát hiện trong 897 (không sửa):** mẫu ở mục 5 của `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` ghi số hiệu
Pháp lệnh, trái với `02-Noi-Dung.md` dòng 4. 897 đang treo chỉnh sửa theo DL-20260909-002 của 897, nên chỉ
ghi nhận để người phụ trách 897 xử lý. Bản sao trong KTC-Quan-tri giữ khớp byte với 897. Tệp 17 nêu rõ
trường hợp này thì lấy theo dòng 4.

**Đã làm:**
- `20-Chuan-Chung/17-Quy-Tac-Vien-Dan.md`, bản gốc mới:
  - ba lớp quy tắc và cách xử lý xung đột;
  - bảng VBHN đang có trong kho 01;
  - chuỗi văn bản Trường đã bị thay thế;
  - bảng tự kiểm VD01–VD12.
  Đã thêm vào `CHUNG` của checker và nhân bản xuống 5 hệ.
- `00-Nguyen-Tac-Chung.md`: thêm **Nguyên tắc 5**, trỏ tới tệp 17 và nêu ba điểm hay sai nhất.
- `29-Cong-Cu/kiem_vien_dan.py`, gồm 12 phép kiểm VD01–VD12. Công cụ chỉ gợi ý, không sửa tệp và không tra
  hiệu lực. Có bản sao trong Skill-Library của gói soạn thảo. Checker C9 đã kiểm import.
- Thử thật trên 25 quyết định ở kho 02. Đã sửa ba loại báo nhầm:
  - câu "Căn cứ…" trong phần nội dung;
  - điều khoản "thay thế Quyết định số 215…";
  - VD08 báo trùng với VD09.
  Ca hồi quy: `test_kiem_vien_dan.py`.
- Phiên bản gói: quan-tri 1.7, ke-hoach 3.8, theo-doi-cv 1.6, bao-cao 3.13, soan-thao-vb 1.7. Plugin 0.5.3.

**Phát hiện trên văn bản đã ban hành** (chỉ ghi nhận, không sửa kho):
- QĐ 1884 (Sổ tay BĐCL) ghi *"Luật Giáo dục nghề nghiệp số 124/2025/QH15"*.
- QĐ 1951 ghi *"… theo Luật số 90/2025/QH15"*.
- Nhiều quyết định ban hành trước 14/9/2026 dẫn QĐ 988 hoặc QĐ 49. Các văn bản này hợp lệ tại ngày ban hành,
  nhưng khi dùng làm **file tương đồng** (Nguyên tắc 7) thì phải đổi sang QĐ 1976.
