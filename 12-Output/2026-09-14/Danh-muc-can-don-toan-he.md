# Danh mục cần dọn thủ công — sau đợt tối ưu cấu trúc 14/9/2026

**Ngày lập:** 14/9/2026 · **Căn cứ:** `DL-20260914-003`, `DL-20260914-004`

Theo quy ước của dự án, tệp và thư mục trên Drive **chỉ do người dùng xóa thủ công**.
Mọi mục dưới đây đã được kiểm: **không còn tệp dữ liệu nào** (ngoài `desktop.ini` của
Google Drive, sẽ tự biến mất khi xóa thư mục cha).

---

## 1. Hai nhánh đầu vào/đầu ra cũ — đã chuyển hết nội dung

**61 thư mục rỗng.** Nội dung đã sang `11-Du-Lieu-Dau-Vao/` và `12-Output/`;
bảng ánh xạ từng tệp tại `Anh-xa-chuyen-Nhap_Bao_Cao.md` cùng thư mục này.

Xóa được **cả cây** — chỉ cần xóa 5 thư mục gốc sau là hết:

| # | Thư mục gốc | Số thư mục con rỗng bên trong |
|---|---|---|
| 1 | `KTC-Bao-Cao/Nhap_Bao_Cao/` | 18 |
| 2 | `KTC-Bao-Cao/Xuat_Bao_Cao/` | 5 |
| 3 | `KTC-Bao-Cao/memory/` | 0 |
| 4 | `KTC-Ke-Hoach/Nhap_Ke_Hoach/` | 31 |
| 5 | `KTC-Ke-Hoach/Xuat_Ke_Hoach/` | 2 |

<details><summary>Danh sách đầy đủ để đối chiếu</summary>

- `KTC-Bao-Cao/Nhap_Bao_Cao/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Chuyen_de/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Nam/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Quy/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Cong-Doan/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Doan-TN/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/KH-Cap-Tren/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Khoa-CKHCB/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Khoa-DT-SHLX/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Khoa-KT-CN/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Khoa-KT-NL/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Khoa-Su-Pham/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Khoa-Y-Duoc/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Phong-QLDT-BDCL/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Phong-QLKHCN-HTPT/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Phong-TC-KT/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Phong-TCCB-CTHHSV/`
- `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/Phong-THHCQT/`
- `KTC-Bao-Cao/Xuat_Bao_Cao/`
- `KTC-Bao-Cao/Xuat_Bao_Cao/output_BC-Chuyen_de/`
- `KTC-Bao-Cao/Xuat_Bao_Cao/output_BC-Nam/`
- `KTC-Bao-Cao/Xuat_Bao_Cao/output_BC-Quy/`
- `KTC-Bao-Cao/Xuat_Bao_Cao/output_BC-Thang/`
- `KTC-Bao-Cao/Xuat_Bao_Cao/output_BC-Thang/2026-08-14_Chay-thu-BC-Thang-7-2026_DUNG-MAU-TB736/`
- `KTC-Bao-Cao/memory/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Cong-Doan/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Doan-TN/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/KH-Cap-Tren/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Khoa-CKHCB/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Khoa-DT-SHLX/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Khoa-KT-CN/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Khoa-KT-NL/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Khoa-Su-Pham/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Khoa-Y-Duoc/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Phong-QLDT-BDCL/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Phong-QLKHCN-HTPT/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Phong-TC-KT/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Phong-TCCB-CTHHSV/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/Phong-THHCQT/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Cong-Doan/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Doan-TN/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Khoa-CKHCB/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Khoa-DT-SHLX/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Khoa-KT-CN/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Khoa-KT-NL/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Khoa-Su-Pham/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Khoa-Y-Duoc/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Phong-QLDT-BDCL/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Phong-QLKHCN-HTPT/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Phong-TC-KT/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Phong-TCCB-CTHHSV/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Quy/Phong-THHCQT/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Thang/`
- `KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Thang/Phong-THHCQT/`
- `KTC-Ke-Hoach/Xuat_Ke_Hoach/`
- `KTC-Ke-Hoach/Xuat_Ke_Hoach/output_KH-Thang/`
- `KTC-Ke-Hoach/Xuat_Ke_Hoach/output_KH-Thang/2026-09-14_Chay-thu-KH-Thang-9-2026/`

</details>

---

## 2. Hệ đã thay thế — `KTC-DIS-Tong-Hop-VB/`

**123 tệp / 22 thư mục con.** Đã được thay bằng `KTC-Soan-Thao-VB/` (xem `DL-20260914-001`).
`CLAUDE.md` đã ghi *"hệ cũ, ĐÃ THAY THẾ, chờ dọn thủ công"* từ trước.

Đây là **mục chiếm chỗ lớn nhất** của dự án — bằng cả `KTC-Soan-Thao-VB` và `KTC-Bao-Cao` cộng lại.

**Trước khi xóa, kiểm hai điều:**

1. `KTC-Soan-Thao-VB/` có đủ 90 tệp và đã đóng gói — ✅ đã kiểm, phép kiểm C1/C11 xanh.
2. Không tệp nào ngoài hệ này còn trỏ vào nó — ⚠️ **còn 4 tệp trỏ tới**, xem bảng dưới.

| Tệp còn nhắc tới | Loại nhắc |
|---|---|
| `CLAUDE.md` | Ghi chú "hệ cũ, đã thay thế, chờ dọn" — giữ lại cho tới khi xóa xong |
| `99-Kinh-Nghiem/06-Decision-Log/DL-20260914-001-...` | Ghi lịch sử quyết định — **giữ nguyên**, không sửa |
| `12-Output/2026-09-14/Danh-muc-can-don-KTC-DIS-Tong-Hop-VB.md` | Danh mục dọn chi tiết đã lập trước |
| `99-Kinh-Nghiem/06-Decision-Log/DL-20260914-002b-...` | Giải thích vì sao giữ tên này |

Không mục nào là **định tuyến đang chạy** — đều là ghi chú lịch sử. Xóa an toàn.

Chi tiết từng tệp bên trong: `Danh-muc-can-don-KTC-DIS-Tong-Hop-VB.md`.

---

## 3. Sau khi xóa xong

Chạy lại `python tools/kiem_tra_he_thong.py` — phải vẫn **0 lỗi**. Nếu C2/C3 báo liên kết gãy
thì có tệp nào đó đang trỏ vào thư mục vừa xóa; sửa tham chiếu chứ đừng khôi phục thư mục.

Sau đó cập nhật `CLAUDE.md`: bỏ dòng `(KTC-DIS-Tong-Hop-VB/ — hệ cũ, ĐÃ THAY THẾ, chờ dọn thủ công)`.
