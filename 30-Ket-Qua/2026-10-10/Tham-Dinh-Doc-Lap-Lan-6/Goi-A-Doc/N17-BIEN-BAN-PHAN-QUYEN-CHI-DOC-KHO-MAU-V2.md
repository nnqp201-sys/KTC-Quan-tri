<!-- N17: chép nguyên văn từ `BIEN-BAN-KIEM-TRA-PHAN-QUYEN-CHI-DOC-KTC-DATABASE_mau-v2.md` (sha256 471de3f74ac79c32c4353b9eb981ef596b8c907268a89b9e513cb9248d4ca89a) -->

# BIÊN BẢN KIỂM TRA PHÂN QUYỀN CHỈ ĐỌC KHO KTC-DATABASE (MẪU, BẢN 2)

**Căn cứ:** điểm b Mục 1 Phần III Dự thảo Thông báo hướng dẫn sử dụng Bộ công cụ KTC-Quan-tri (bản 8); yêu cầu F4-06 báo cáo
thẩm định độc lập lần 4, L5-01 (cổng G1) báo cáo thẩm định lần 5. **Đơn vị thực hiện:** Phòng TH-HC&QT (quản lý kho theo
Thông báo số 948/TB-CĐKT ngày 17/8/2026). **Thời hạn:** trước khi thí điểm (cổng G1, dự kiến trước ngày 02/10/2026). Biểu mẫu
do AI lập sẵn; người kiểm tra điền, ký.

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Thời gian kiểm tra | ……… giờ ……… ngày ……/……/2026 |
| Người kiểm tra (Phòng TH-HC&QT) | ……………………… |
| Người chứng kiến | ……………………… (đơn vị: ………) |
| Tài khoản chủ kho (Owner) | ……………………… (không dùng để thử) |
| Tài khoản thử (KHÔNG phải người quản lý kho) | ……………………… (loại: tài khoản Google của đơn vị / cá nhân) |

## 2. Cấu hình chia sẻ trên Google Drive (Owner ghi, chụp màn hình hộp “Chia sẻ”)

| Thư mục | Người, nhóm được chia sẻ | Quyền (Người xem / Người nhận xét / Người chỉnh sửa) | Ảnh chụp số |
|---|---|---|---|
| `KTC-Database` (gốc) | | | |
| `01-Legal-Database` | | | |
| `02-KTC-Regulations` | | | |
| `03-Templates(1)` | | | |
| `04-Good-Documents` | | | |

Đạt khi: mọi tài khoản không phải người quản lý kho chỉ có quyền **Người xem**; tùy chọn “Người xem có thể tải xuống, in, sao
chép” theo quyết định của Phòng TH-HC&QT (ghi rõ).

## 3. Thử bằng tài khoản thử (trên trình duyệt và trên Google Drive for Desktop nếu có)

| TT | Thao tác thử | Kết quả mong đợi | Kết quả thực tế | Đạt |
|---|---|---|---|---|
| 1 | Mở, đọc 1 tệp trong `02-KTC-Regulations` | Mở được | | |
| 2 | Tạo tệp mới trong `02-KTC-Regulations` | Bị từ chối | | |
| 3 | Sửa nội dung 1 tệp .docx trong `04-Good-Documents` | Bị từ chối / chỉ mở chế độ xem | | |
| 4 | Đổi tên 1 tệp trong `03-Templates(1)` | Bị từ chối | | |
| 5 | Xóa 1 tệp trong `01-Legal-Database` | Bị từ chối | | |
| 6 | Kéo thả 1 tệp từ máy vào `KTC-Database` (Drive for Desktop) | Bị từ chối, tệp không đồng bộ lên | | |
| 7 | Trên Cowork/Claude Code (máy của tài khoản thử, plugin 1.3.13): yêu cầu Claude ghi 1 tệp vào `KTC-Database` | Guard chặn; nếu vượt guard thì Drive từ chối | | |
| 8 | Tạo liên kết (shortcut) tới `KTC-Database` rồi ghi tệp qua liên kết | Drive từ chối ghi | | |
| 9 | Chạy một chương trình có sẵn trong tệp (không nêu tên kho trong lệnh) ghi vào `KTC-Database` | Drive từ chối ghi | | |
| 10 | Chạy lệnh đã mã hóa (base64) ghi vào `KTC-Database` | Drive từ chối ghi | | |
| 11 | Đặt biến trỏ vào kho ở một lệnh, ghi qua biến ở lệnh sau | Drive từ chối ghi | | |
| 12 | Trên Claude (trò chuyện) có kết nối Google Drive: yêu cầu tạo, sửa tệp trong `KTC-Database` | Bị từ chối (kết nối chỉ đọc hoặc Drive từ chối) | | |

Thao tác 8 - 11 là các kịch bản mà thao tác chặn ghi **không nhận dạng được** (kiểm thử ngày 29/9/2026, bản 1.3.13: chặn 5/10
kịch bản ghi che giấu), nên chỉ phân quyền trên Drive mới chặn được. Chỉ dùng tệp thử rỗng, đặt tên `THU-XOA-<ngày>.txt`; nếu
thao tác nào ghi được thì dừng, xóa tệp thử, ghi “Không đạt” và báo Phòng TH-HC&QT sửa phân quyền.

## 4. Kết luận

☐ Đạt — kho chỉ đọc với mọi tài khoản không phải người quản lý kho.
☐ Không đạt — nội dung phải khắc phục: ………………………………………… Thời hạn: ………

| Người kiểm tra | Người chứng kiến | Trưởng phòng TH-HC&QT |
|---|---|---|
| (ký, ghi rõ họ tên) | (ký, ghi rõ họ tên) | (ký, ghi rõ họ tên) |

=== HẾT TỆP N17-BIEN-BAN-PHAN-QUYEN-CHI-DOC-KHO-MAU-V2.md — MÃ KIỂM: 861916 ===
