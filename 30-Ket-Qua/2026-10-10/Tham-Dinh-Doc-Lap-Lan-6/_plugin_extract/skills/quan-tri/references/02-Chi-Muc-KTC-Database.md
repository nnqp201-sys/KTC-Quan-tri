# Chỉ mục kho KTC-Database

Kho nền pháp lý và quy định dùng chung của toàn bộ hệ thống KTC. **Chỉ đọc** — không sửa, không đổi tên, không
di chuyển, không xóa tệp đã có.

**Điểm vào bắt buộc:** `KTC-DIS-Master-Index_20260830_v1.2.xlsx` — chỉ mục 58 dòng, mỗi thư mục có cột
"Chứa tài liệu gì" và "Tra cứu khi nào". Đọc chỉ mục trước, đừng duyệt cây thư mục mò.

## Tám kho

| Kho | Quy mô | Nội dung | Tra khi |
|---|---|---|---|
| `01-Legal-Database` | 519 tệp | VBQPPL trung ương và tỉnh: 01-01 Luật · 01-02 Quốc hội · 01-03 TW Đảng · 01-04 Chính phủ · 01-05 các Bộ · 01-06 Tỉnh ủy/UBND tỉnh | Kiểm tra căn cứ pháp lý, xác minh còn/hết hiệu lực |
| `02-KTC-Regulations` | 244 tệp | Quy chế, quy định nội bộ · chiến lược · kế hoạch năm/quý/tháng · kế hoạch chuyên đề · đề án đã ban hành | Đối chiếu quy định nội bộ trước khi soạn — **kho quan trọng nhất với hệ này** |
| `03-Templates` | 19 tệp | ⚠️ Xem cảnh báo bên dưới | Không dùng làm nguồn biểu mẫu |
| `03-Templates(1)` | 17 tệp | Bộ biểu mẫu trống thật: 16 tệp `.dotx`/`.xltx` + `00-Template-Registry-KTC-DIS.docx` | Cần mẫu trống đúng thể thức |
| `04-Good-Documents` | 109 tệp | Văn bản đã ban hành đạt chất lượng, 14 loại | Học văn phong, bố cục, cách lập luận |
| `05-De-an-De-tai` | 54 tệp | Hồ sơ đề án đang triển khai theo từng vòng góp ý | Theo dõi đề án |
| `11-Input` / `12-Output` (của KTC-Database) | | Tệp chờ nạp vào kho / báo cáo vận hành kho theo ngày — **không** phải `30-Ket-Qua` của KTC-Quan-tri | Nạp liệu, lấy lại kết quả |
| `references` | 10 tệp | Quy tắc của skill `ktc-database`: nguyên tắc chung, metadata schema, quy trình nạp liệu | Trước khi nạp hoặc gắn metadata |

## Văn bản gốc chống lưng cho hệ này

Nằm ở gốc `02-KTC-Regulations/`. Khi cần căn cứ, **trích văn bản gốc chứ không trích tệp Excel dẫn xuất**:

| Văn bản | Vai trò |
|---|---|
| `05. TB-817-Noi-ham-06-Truc-Ket-qua-trong-tam-Truong-CDKT.docx` | Nguồn gốc 6 Trục và 38 Nội hàm |
| `Quy-che_Danh-gia-KPI-tap-the-ca-nhan_Truong-CDKT_20260829_v1.docx` | QĐ 1923/QĐ-CĐKT — Quy chế đánh giá KPI. **Lưu ý: tên tệp ghi 0829 nhưng văn bản ghi ngày 30/8/2026** |
| `QD1923_PL-I/II/III_...` | Mẫu kế hoạch công tác quý đơn vị · mẫu kế hoạch/danh mục công việc cá nhân · mẫu phiếu đánh giá xếp loại |
| `KH-834_Ke-hoach-cong-tac-thang-9-2026...xlsx` | Kế hoạch tháng hiện hành — dữ liệu thật |
| `BC-375_...` + `PL-375_Phu-luc-chi-tiet...xlsx` | Báo cáo tháng 8/2026 kèm phụ lục chi tiết — dữ liệu thật |
| `QD-543-QD-UBND_Chuyen-ve-UBND-tinh-Quang-Ngai_20250630_v1.pdf` | Căn cứ Trường chuyển về UBND tỉnh Quảng Ngãi (30/6/2025) |

## Hai cảnh báo về kho 03

1. **`03-Templates` không phải kho biểu mẫu.** Master Index đánh dấu "CẦN XỬ LÝ / Không dùng": hầu hết là
   văn bản thật đã ban hành, chỉ có đúng 01 mẫu trống. Bộ mẫu thật nằm ở **`03-Templates(1)`**.
2. **Master Index v1.2 chưa có `03-Templates(1)`** — chỉ mục lạc hậu so với thực tế. Khi tra mẫu, kiểm tra
   trực tiếp thư mục thay vì tin chỉ mục.

Tuyệt đối **không trích dẫn tệp mẫu hoặc checklist nội bộ làm "Căn cứ" pháp lý** — theo quy tắc của
`ktc-ra-soat-897`, đây luôn là lỗi Mức 1.

## Metadata khi nạp tài liệu

11 trường bắt buộc + 2 trường theo loại văn bản + 3 trường trách nhiệm (nguồn dữ liệu đã dùng · người kiểm
tra · trạng thái phê duyệt). Quy trình nạp 2 tầng, Tầng 1 = bản nháp. Chi tiết:
`KTC-Database/references/00-Metadata-Schema.md`.

Nguyên tắc điền: **chỉ điền giá trị có căn cứ rõ trong văn bản; đánh dấu "Không xác định" cho trường thiếu,
không suy diễn.**

## Thể thức — cơ quan chủ quản

`UBND TỈNH QUẢNG NGÃI` – `TRƯỜNG CAO ĐẲNG KON TUM`. Không dùng "UBND tỉnh Kon Tum" ở văn bản mới.
