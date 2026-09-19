---
name: ktc-the-thuc
description: "Chuan the thuc, ky thuat trinh bay BAT BUOC cho moi tep .docx va .xlsx cua Truong Cao dang Kon Tum (KTC): quyet dinh, ke hoach, bao cao, to trinh, cong van, thong bao, bien ban, giay moi, phu luc, bang KPI, ke hoach cong tac thang/quy. Dung CUNG VOI skill docx/xlsx moi khi tao hoac sua tep Word/Excel cho Truong, cho P-THHC, cho cac Phong/Khoa/Trung tam, hoac khi skill ktc-quan-tri/ke-hoach/bao-cao/soan-thao-vb/theo-doi-cv xuat san pham. Quy dinh: dung tu van ban tuong dong 04-Good-Documents hoac mau .dotx/.xltx 03-Templates(1) (khong dung tu tep trong), kho A4, le 2-2-3-2 cm, Times New Roman, co 14, phan dau UBND TINH QUANG NGAI - TRUONG CAO DANG KON TUM; do lai bang kiem_the_thuc.py truoc khi giao. Ghi de mac dinh cua skill docx (le 2,54 cm) va xlsx (cho phep Arial). KHONG ra soat noi dung truoc trinh ky - dung ktc-ra-soat-897; KHONG ap cho van ban Dang (HD 05)."
---

# KTC-The-Thuc — Chuẩn thể thức sản phẩm .docx/.xlsx

**Phiên bản: 1.0 — 19/9/2026** — Ban hành theo DL-20260919-003.

Skill này là **lớp chuẩn của Trường chồng lên skill `docx`/`xlsx`**. Cách tạo và sửa tệp vẫn theo `docx`/`xlsx`.
Thể thức, số đo và bước kiểm thì theo skill này. Khi hai bên khác nhau, **skill này thắng**:

| Điểm | Mặc định của `docx`/`xlsx` | Chuẩn KTC (bắt buộc) |
|---|---|---|
| Lề trang Word | 2,54 cm cả bốn lề | **trên 2 · dưới 2 · trái 3 · phải 2 cm** (DXA `1134/1134/1701/1134`) |
| Khổ giấy | A4 (docx-js); **Letter** nếu dùng `docx.Document()` rỗng | **A4**, không dựng từ tệp rỗng |
| Phông | Theo mẫu, hoặc Arial/Times New Roman | **Times New Roman**, Unicode, cỡ nội dung **14** |
| Nguồn dựng | Tạo mới | Văn bản tương đồng đã ban hành → mẫu `.dotx`/`.xltx` → chỉ sau cùng mới tạo mới |

## Quy trình — 4 bước, không bỏ bước

1. **Chọn nguồn** theo `references/18-Chuan-The-Thuc-San-Pham.md` mục 1–2:
   - Tìm văn bản cùng loại trong `KTC-Database/04-Good-Documents/`.
   - Không có thì dùng mẫu trống trong `KTC-Database/03-Templates(1)/`.
   - Tài khoản không đọc được Drive: xin người dùng đính kèm mẫu ("Add files and photos"). Vẫn không có thì dựng
     mới theo đủ số đo mục 3–4.
2. **Mở mẫu thành tệp làm việc:** `python scripts/kiem_the_thuc.py --tao <mẫu.dotx|.xltx> <đích.docx|.xlsx>`.
   Sau đó soạn nội dung bằng skill `docx`/`xlsx` **trên tệp đó**, giữ style, lề và bảng thể thức của mẫu.
   Mẫu ghi "UBND TỈNH KON TUM" thì đổi thành **UBND TỈNH QUẢNG NGÃI**.
3. **Đo:** `python scripts/kiem_the_thuc.py <tệp>` với **từng** tệp trước khi giao. Còn Mức 1–2 thì sửa rồi đo lại.
   Không giao tệp còn lỗi Mức 1–2.
4. **Báo kết quả đo** cuối câu trả lời, hoặc trong phiếu tự kiểm của đơn vị:
   `Thể thức: đạt (kiem_the_thuc, 0 lỗi Mức 1–2)`. Không chạy được Python thì ghi `FORMAT_BINARY_UNVERIFIED`,
   không được tuyên bố đạt chuẩn.

## Tài liệu

| Việc | Tệp |
|---|---|
| Thứ tự nguồn, bảng chọn mẫu theo loại, số đo .docx/.xlsx, mã kiểm TT/TX, lỗi đã biết của mẫu | `references/18-Chuan-The-Thuc-San-Pham.md` |
| Công cụ tạo từ mẫu và đo thể thức | `scripts/kiem_the_thuc.py` |
| Cỡ chữ từng thành phần (số ký hiệu, trích yếu, chữ ký…) | `KTC-Ra-Soat-897-v2-Cai-tien/references/Checklist/08-Quy-Uoc-Rieng-CDKT.md` mục 4 (bản gốc, không chép) |

## Giới hạn

- Chỉ áp cho **văn bản hành chính** (hệ A). Văn bản Đảng theo HD 05-HD/VPTW, dùng `ktc-ra-soat-897`.
- Không thay rà soát 897 trước trình ký. Còn Mức 1 theo 897 thì không được trình.
- Không sửa kho `KTC-Database` (chỉ đọc). Lỗi của chính mẫu thì ghi đề xuất ra `30-Ket-Qua/`.
