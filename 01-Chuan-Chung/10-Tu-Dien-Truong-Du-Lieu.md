# Từ điển trường dữ liệu dùng chung — Master Task Register

**Trạng thái:** Dự thảo để chốt · **Lập ngày:** 13/9/2026

Đây là bộ trường mà cả ba hệ Kế hoạch – Theo dõi – Báo cáo cùng đọc/ghi. Hợp nhất từ ba nguồn: 8 nhóm dữ
liệu ở mục VII Kế hoạch hợp nhất, 17 trường theo dõi tối thiểu ở mục V.2, và các cột thật của Phụ lục I
kèm Quyết định 1923/QĐ-CĐKT.

## Nhóm A — Định danh

| Trường | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| `Task_ID` | Chuỗi | ✔ | Khóa chính. Quy tắc: `11-Quy-Tac-Task-ID.md` |
| `Parent_Task_ID` | Chuỗi | | Rỗng nếu là nhiệm vụ gốc |
| `Ma_NV_Chuan` | Chuỗi | | `A01`–`S04`. Rỗng nếu danh mục chưa có mã phù hợp — **không ép về mã gần đúng** |
| `Plan_ID` | Chuỗi | ✔ | Kế hoạch sinh ra nhiệm vụ |
| `Report_ID` | Chuỗi | | Điền khi đã đưa vào báo cáo |

## Nhóm B — Nội dung

| Trường | Kiểu | Bắt buộc |
|---|---|---|
| `Ten_Nhiem_Vu` | Văn bản | ✔ |
| `Mo_Ta` | Văn bản | |
| `Muc_Tieu` | Văn bản | |
| `San_Pham_Yeu_Cau` | Văn bản | ✔ |
| `So_Luong` | Số | |

## Nhóm C — Căn cứ

| Trường | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| `Can_Cu_So_Hieu` | Chuỗi | ✔ | Số/ký hiệu văn bản giao nhiệm vụ |
| `Can_Cu_Ngay` | Ngày | ✔ | |
| `Can_Cu_Co_Quan` | Chuỗi | ✔ | |
| `Can_Cu_Dieu_Khoan` | Chuỗi | | Điều/khoản cụ thể |
| `Nguon_Phat_Sinh` | Chuỗi | | Bắt buộc với nhiệm vụ phát sinh |

## Nhóm D — Trách nhiệm

| Trường | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| `Don_Vi_Chu_Tri` | Mã đơn vị | ✔ | Dùng **mã chuẩn** tại `13-Bang-Ma-Don-Vi.md`, không ghi tên tự do |
| `Don_Vi_Phoi_Hop` | Danh sách mã | | Ngăn cách bằng dấu `;` |
| `Nguoi_Phu_Trach` | Chuỗi | | |
| `Nguoi_Chi_Dao` | Chuỗi | | Theo cột "Người trực tiếp chỉ đạo" của Phụ lục I |
| `Cap_Phe_Duyet` | Chuỗi | | |

## Nhóm E — Thời gian

| Trường | Kiểu | Bắt buộc |
|---|---|---|
| `Ky_Ke_Hoach` | Chuỗi | ✔ |
| `Ngay_Bat_Dau` | Ngày | |
| `Han_Hoan_Thanh` | Ngày | ✔ |
| `Ngay_Hoan_Thanh_Thuc_Te` | Ngày | |

## Nhóm F — Tiến độ

| Trường | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| `Trang_Thai` | Danh mục | ✔ | 7 trạng thái chính, xem `12-Vong-Doi-Trang-Thai.md` |
| `Trang_Thai_Phu` | Danh mục | | Tạm dừng/Điều chỉnh/Chuyển kỳ/Hủy |
| `Phan_Tram_Tien_Do` | Số 0–100 | ✔ | |
| `Muc_Rui_Ro` | Danh mục | | Xanh/Vàng/Đỏ — **hệ thống tính**, không nhập tay |
| `Canh_Bao` | Danh sách | | 8 loại, hệ thống tính |

## Nhóm G — Kết quả và quy đổi

| Trường | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| `Ket_Qua_Thuc_Te` | Văn bản | | |
| `San_Pham_Dat_Duoc` | Văn bản | | |
| `Minh_Chung` | Đường dẫn | | Bắt buộc khi `Trang_Thai` = Đã hoàn thành |
| `Truc` | 1–6 | ✔ | |
| `Noi_Ham` | Chuỗi | ✔ | Luôn ghi kèm Trục — số nội hàm đánh lại từ 1 trong mỗi Trục |
| `Nhom_Quy_Doi` | 1–5 | | |
| `Diem_Cham` | Số | | 50/120/250/350/450 theo nhóm |
| `He_So_Quy_Doi` | Số | | 0,5/1,2/2,5/3,5/4,5 theo nhóm |
| `Do_Kho` | Văn bản | | Cột "Độ khó, mới, phức tạp; phạm vi tác động" của Phụ lục I |

## Nhóm H — Báo cáo và vết

| Trường | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| `Da_Bao_Cao` | Có/Không | ✔ | |
| `Ky_Bao_Cao` | Chuỗi | | |
| `Ket_Luan_Danh_Gia` | Văn bản | | |
| `Vuong_Mac` | Văn bản | | |
| `De_Xuat` | Văn bản | | |
| `Ngay_Cap_Nhat` | Ngày | ✔ | |
| `Nguoi_Cap_Nhat` | Chuỗi | ✔ | |
| `Lich_Su` | Danh sách | ✔ | Mỗi thay đổi 1 dòng, xem quy tắc ghi lịch sử |

## Ba quy ước bắt buộc

1. **Không sao chép nhiệm vụ sang nhiều bảng.** Ba hệ cùng trỏ về một dòng gốc qua `Task_ID`; mỗi hệ chỉ
   được ghi vào nhóm trường thuộc quyền của mình (Kế hoạch: A–E · Theo dõi: F, G · Báo cáo: H).
2. **Trường danh mục chỉ nhận giá trị trong danh mục.** Đơn vị, Trục, Nội hàm, Trạng thái, Nhóm quy đổi —
   nhập giá trị lạ thì báo lỗi, không tự suy diễn về giá trị gần nhất.
3. **`Muc_Rui_Ro` và `Canh_Bao` do hệ thống tính**, mọi giá trị nhập tay ở hai trường này đều bị ghi đè.
