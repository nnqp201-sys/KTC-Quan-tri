# Ghi chú kèm 2 Quyết định — điều chỉnh sau khi bỏ hạng mục lập HSMT/thẩm định

**Cập nhật 29/9/2026 (lần 2):** anh chỉ ra đúng — gói Tư vấn quản lý dự án đã chọn **chỉ định thầu theo
quy trình rút gọn**, nên không cần hạng mục "Lập HSMT, đánh giá HSDT, thẩm định HSMT, thẩm định KQLCNT".
Đã tra cứu xác nhận: theo Nghị định 214/2025/NĐ-CP, quy trình chỉ định thầu (kể cả rút gọn) dùng **"hồ sơ
yêu cầu"/"hồ sơ đề xuất"**, không phải "hồ sơ mời thầu"/"hồ sơ dự thầu" (thuật ngữ đó chỉ dùng cho đấu thầu
rộng rãi/hạn chế); và **thẩm định hồ sơ yêu cầu, kết quả chỉ định thầu không bắt buộc** — chủ đầu tư có
quyền quyết định, không mặc định phát sinh chi phí. → Đã sửa cả 2 văn bản.

## 1. Quyết định phê duyệt nhiệm vụ và dự toán CBĐT — sửa bằng Track Changes

Văn bản gốc **đã được Hiệu trưởng ký** (29/9/2026) nên sửa theo Nguyên tắc 8 (bắt buộc Track Changes,
xuất phát từ đúng file gốc), không soạn lại từ đầu.

- **Tệp:** `30-Ket-Qua/2026-09-29/Track-Changes/QD-nhiem-vu-du-toan-CBDT_sua-bo-chi-dinh-thau_20260929.docx`
- **Nhật ký sửa đổi:** `Nhat-ky-sua-doi_QD-nhiem-vu-du-toan-CBDT_20260929.md` (6 thay đổi)
- **Nội dung sửa:** xóa 3 hàng trong Phụ lục II (Lập HSMT và đánh giá HSDT — 5.446.254đ; Thẩm định HSMT —
  2.000.000đ; Thẩm định kết quả lựa chọn nhà thầu — 3.000.000đ); cập nhật dự toán CBĐT từ
  **1.530.224.522 → 1.519.778.268 đồng** (khoản 11 Điều 1 và "Bằng chữ" ở Phụ lục).
- **Kiểm chứng:** `doi_chieu_goc` → `ty_le_khoi_phuc = 1.0` (bỏ hết các đánh dấu sửa tái tạo đúng 100%
  bản gốc); `kiem_tra` → đạt; `kiem_the_thuc.py` và `kiem_vien_dan.py` → 0 gợi ý cả hai.
- **Lưu ý:** đây vẫn là **bản dự thảo sửa đổi**, chưa ban hành. Vì QĐ gốc đã có hiệu lực (ký 29/9/2026),
  việc sửa nội dung dự toán đã duyệt cần ban hành dưới hình thức quyết định sửa đổi/thay thế chính thức
  (không chỉ lưu hành bản Track Changes nội bộ) — Trường quyết định hình thức cụ thể (QĐ đính chính, QĐ
  sửa đổi, hay ký lại toàn văn).

## 2. Quyết định phê duyệt Kế hoạch lựa chọn nhà thầu — sửa trực tiếp (chưa ban hành)

Đây là bản do tôi soạn trong phiên này, chưa ban hành nên sửa trực tiếp, không cần Track Changes.

- **Tệp:** `30-Ket-Qua/2026-09-29/Soan-Thao-VB/QD-KHLCNT-giai-doan-CBDT_Du-an-CLC-2026-2030_20260929_v2.docx`
  (thay cho bản `_20260929.docx` cũ — bản cũ đang mở trong Word trên máy anh nên không ghi đè được, giữ
  nguyên làm bản tham khảo lịch sử, **dùng bản `_v2` để trình ký**).
- **Nội dung sửa:** bỏ gói thầu số 4; Điều 1 và Ghi chú Phụ lục đổi tổng giá trị **1.530.224.522 →
  1.519.778.268 đồng**; Điều 2 rút còn 2 khoản (bỏ khoản nói về gói số 4).
- **Kết quả — còn 3 gói thầu, đều chỉ định thầu/quy trình rút gọn:**

| TT | Gói thầu | Giá gói thầu (đồng) |
|---|---|---|
| 1 | Tư vấn khảo sát xây dựng phục vụ lập Báo cáo kinh tế - kỹ thuật | 93.995.981 |
| 2 | Tư vấn lập Báo cáo kinh tế - kỹ thuật (gồm thiết kế bản vẽ thi công) | 758.349.265 |
| 3 | Tư vấn quản lý dự án | 667.433.022 |
| | **Tổng** | **1.519.778.268** |

- **Kiểm chứng:** `kiem_the_thuc.py` và `kiem_vien_dan.py` trên bản `_v2` → 0 gợi ý cả hai.

## 3. Điểm còn cần Phòng THHC&QT / Phòng TC-KT xác nhận trước khi trình ký (không đổi so với lần trước)

1. Thời gian tổ chức lựa chọn nhà thầu ("Không quá 07 ngày", "Quý IV năm 2026") và thời gian thực hiện
   hợp đồng (30/45 ngày; "90 ngày" cho gói QLDA) là số đề xuất theo tập quán 3 mẫu tham khảo, chưa phải số
   thật — cần Phòng xác nhận lại, đặc biệt mốc 90 ngày.
2. Số/ngày của Quyết định phê duyệt nhiệm vụ và dự toán CBĐT còn để trống ở cả 2 văn bản — điền khi có số
   chính thức (và với QĐ nhiệm vụ/dự toán, cần xác nhận hình thức ban hành sửa đổi như mục 1 nêu).
3. Bản dự thảo **chưa qua rà soát chính thức KTC-Ra-Soat-897** trước khi trình ký (Nguyên tắc 9).
4. **Chưa cập nhật lại** bảng tính `Tinh-kinh-phi-chuan-bi-dau-tu_24894-trieu_20260924.xlsx` (dựng ở phiên
   trước) theo số 1.519.778.268 — nếu Trường còn dùng bảng đó làm hồ sơ tính toán CBĐT thì cần sửa thêm.
