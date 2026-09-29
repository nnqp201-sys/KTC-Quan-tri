---
name: ktc-the-thuc
description: "Chuan the thuc, ky thuat trinh bay BAT BUOC cho moi tep .docx va .xlsx cua Truong Cao dang Kon Tum (KTC): quyet dinh, ke hoach, bao cao, to trinh, cong van, thong bao, bien ban, giay moi, phu luc, bang KPI, ke hoach cong tac thang/quy. Dung CUNG VOI skill docx/xlsx moi khi tao hoac sua tep Word/Excel cho Truong, cho P-THHC, cho cac Phong/Khoa/Trung tam, hoac khi skill ktc-quan-tri/ke-hoach/bao-cao/soan-thao-vb/theo-doi-cv xuat san pham. Quy dinh: dung tu van ban tuong dong 04-Good-Documents hoac mau .dotx/.xltx 03-Templates(1) (khong dung tu tep trong), kho A4, le 2-2-3-2 cm, Times New Roman, co 14, phan dau UBND TINH QUANG NGAI - TRUONG CAO DANG KON TUM; do lai bang kiem_the_thuc.py truoc khi giao. Ghi de mac dinh cua skill docx (le 2,54 cm) va xlsx (cho phep Arial). KHONG ra soat noi dung truoc trinh ky - dung ktc-ra-soat-897; KHONG ap cho van ban Dang (HD 05)."
---

# KTC-The-Thuc — Chuẩn thể thức sản phẩm .docx/.xlsx

**Phiên bản: 1.2 — 29/9/2026** — Ban hành theo DL-20260919-003. 1.2: nguyên tắc sửa văn bản tương tự hoặc ráp nội
dung vào mẫu `03-Templates(1)`; khung dựng lại từ mẫu 03A; bước xem trang thật; phép đo TT11b (số trang ở trang 1),
chuẩn hóa NFC. 1.1: khung `assets/Khung-the-thuc-VBHC.docx` (`--khung`); phép đo TT12–TT19 ánh xạ 897.

Skill này là **lớp chuẩn của Trường chồng lên skill `docx`/`xlsx`**. Cách tạo và sửa tệp vẫn theo `docx`/`xlsx`.
Thể thức, số đo và bước kiểm thì theo skill này. Khi hai bên khác nhau, **skill này thắng**:

| Điểm | Mặc định của `docx`/`xlsx` | Chuẩn KTC (bắt buộc) |
|---|---|---|
| Lề trang Word | 2,54 cm cả bốn lề | **trên 2 · dưới 2 · trái 3 · phải 2 cm** (DXA `1134/1134/1701/1134`) |
| Khổ giấy | A4 (docx-js); **Letter** nếu dùng `docx.Document()` rỗng | **A4**, không dựng từ tệp rỗng |
| Phông | Theo mẫu, hoặc Arial/Times New Roman | **Times New Roman**, Unicode, cỡ nội dung **14** |
| Nguồn dựng | Tạo mới | Văn bản tương đồng đã ban hành → mẫu `.dotx`/`.xltx` → chỉ sau cùng mới tạo mới |

## Quy trình — 5 bước, không bỏ bước

1. **Chọn nguồn** theo `references/18-Chuan-The-Thuc-San-Pham.md` mục 1–2. Nguyên tắc: **tìm văn bản tốt, văn bản
   tương tự mà sửa lại; hoặc lấy mẫu `03-Templates(1)` mà ráp nội dung vào** (chỉ đạo 28/9/2026). Thứ tự:
   1. Văn bản cùng loại đã ban hành trong `KTC-Database/04-Good-Documents/`, `02-KTC-Regulations/`: sao tệp, sửa chữ.
   2. Mẫu trống cùng loại trong `KTC-Database/03-Templates(1)/`: `--tao`, rồi ráp nội dung.
   3. Không đọc được Drive (Cowork, Chat, tài khoản thành viên): **xin người dùng đính kèm** mẫu `03-Templates(1)`
      cùng loại hoặc một văn bản tương tự đã ban hành.
   4. Chỉ khi vẫn không có: khung trong skill `assets/Khung-the-thuc-VBHC.docx` (`--khung`), dựng từ mẫu 03A đã
      sửa lỗi.
   - **Cấm dựng bảng tiêu đề, bảng chữ ký bằng tay** (`add_table`, docx-js), và cấm ghép phần của nhiều văn bản. Ngày
     28/9/2026 bảng tự dựng làm quốc hiệu xuống dòng; bản ghép từ TB 1060 hiện số "1" ở trang 1, lệch đường kẻ.
2. **Mở thành tệp làm việc rồi ráp nội dung** (cách ráp: chuẩn 18 mục 1):
   - Mẫu `.dotx`/`.xltx`: `python scripts/kiem_the_thuc.py --tao <mẫu> <đích.docx|.xlsx>`. Văn bản `.docx`: sao tệp.
   - Khung: `python scripts/kiem_the_thuc.py --khung <đích.docx> <TB|KH|BC|TTr|QĐ|GM|HD|CTr|BB>`.
   - Chỉ thay chữ trong run có sẵn, giữ run chứa đường kẻ. Thêm đoạn bằng cách **nhân bản đoạn cùng vai trò**: lời văn
     từ đoạn lời văn thường, không lấy đoạn tiêu đề mục in đậm. Xóa đoạn giữ chỗ không dùng và section phụ lục đi kèm mẫu.
   - Mẫu lưu chữ dạng Unicode NFD: so, tìm chữ sau `unicodedata.normalize("NFC", …)`.
   - Mẫu ghi "UBND TỈNH KON TUM" thì đổi thành **UBND TỈNH QUẢNG NGÃI**. Lỗi đã biết của từng mẫu: chuẩn 18 mục 6.
3. **Đo:** `python scripts/kiem_the_thuc.py <tệp>` với **từng** tệp trước khi giao. Còn Mức 1–2 thì sửa rồi đo lại.
   Không giao tệp còn lỗi Mức 1–2.
4. **Xem trang thật** (Claude Code có Word): xuất PDF rồi xem. Kiểm khối chữ ký không tách trang, đường kẻ đúng chỗ
   và màu đen, trang 1 không có số trang. Công cụ đo không thay được bước này; không xem được thì ghi rõ "chưa xem trang".
5. **Báo kết quả đo** cuối câu trả lời, hoặc trong phiếu tự kiểm của đơn vị:
   `Thể thức: đạt (kiem_the_thuc, 0 lỗi Mức 1–2)`. Không chạy được Python thì ghi `FORMAT_BINARY_UNVERIFIED`,
   không được tuyên bố đạt chuẩn.

## Tài liệu

| Việc | Tệp |
|---|---|
| Thứ tự nguồn, bảng chọn mẫu theo loại, số đo .docx/.xlsx, mã kiểm TT/TX, lỗi đã biết của mẫu | `references/18-Chuan-The-Thuc-San-Pham.md` |
| Công cụ tạo từ mẫu, tạo từ khung và đo thể thức | `scripts/kiem_the_thuc.py` |
| Khung thể thức văn bản hành chính (khi không đọc được kho) | `assets/Khung-the-thuc-VBHC.docx` |
| Cỡ chữ từng thành phần (số ký hiệu, trích yếu, chữ ký…) | `KTC-Ra-Soat-897-v2-Cai-tien/references/Checklist/08-Quy-Uoc-Rieng-CDKT.md` mục 4 (bản gốc, không chép) |

## Giới hạn

- Chỉ áp cho **văn bản hành chính** (hệ A). Văn bản Đảng theo HD 05-HD/VPTW, dùng `ktc-ra-soat-897`.
- Không thay rà soát 897 trước trình ký. Còn Mức 1 theo 897 thì không được trình.
- Không sửa kho `KTC-Database` (chỉ đọc). Lỗi của chính mẫu thì ghi đề xuất ra `30-Ket-Qua/`.
