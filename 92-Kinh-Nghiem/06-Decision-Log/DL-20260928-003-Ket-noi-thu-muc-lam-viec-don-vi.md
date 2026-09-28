# DL-20260928-003 — Kết nối thư mục làm việc của đơn vị cho tài khoản thành viên (plugin 1.3.5)

**Ngày:** 28/9/2026 · **Người phụ trách giao:** "Cho phép họ thêm 1 phương thức kết nối với thư mục đầu vào, đầu ra trong
Cowork nhé" (sau câu hỏi: chia sẻ plugin cho người khác, không có `10-Dau-Vao`, `30-Ket-Qua`, quy trình có bảo đảm không).

## Hiện trạng trước 1.3.5 (đã rà trên bản 1.3.4)
- Nguyên tắc 3 đã có đường lui: đầu vào = tệp đính kèm → thư mục dự án → hỏi; kết quả giao trong phiên, người dùng tự gửi
  P-THHC. Kỹ năng KPI tự chứa (mẫu, Danh mục QĐ 2119 trong gói).
- Ba điểm chưa bảo đảm: (1) kho KTC-Database — thành viên phải có quyền đọc và **lối tắt trong Drive của tôi** (plugin không
  thấy "Được chia sẻ với tôi"); (2) hook đo thể thức chỉ chạy trong dự án; (3) khối quy tắc lõi, kỹ năng kế hoạch ghi
  `30-Ket-Qua/` không điều kiện.

## Quyết định
1. **Thư mục làm việc của đơn vị**: người dùng chọn một thư mục trong Cowork (hoặc mở Claude Code trong đó), yêu cầu "kết nối
   thư mục KTC cho đơn vị `<mã>`" → `scripts/ktc_thu_muc.py khoi-tao` tạo `10-Dau-Vao/`, `30-Ket-Qua/`, `00-HUONG-DAN.md`,
   tệp đánh dấu `KTC-THU-MUC-LAM-VIEC.json`. **Dùng đúng tên thư mục của dự án** nên mọi kỹ năng đang ghi đường dẫn tương
   đối `10-Dau-Vao/`, `30-Ket-Qua/` chạy được, không phải sửa từng kỹ năng.
2. Nhận diện bằng tệp đánh dấu (tìm lên tối đa 6 cấp) — không ghi vào thư mục bất kỳ; dự án được ưu tiên nhận trước.
3. Từ chối: kho chuẩn, bên trong dự án, mã ngoài 11 mã chuẩn, thư mục đã kết nối cho đơn vị khác, thư mục con của thư mục đã
   kết nối; không ghi đè tệp đã có.
4. Không tự gửi sản phẩm: người dùng vẫn tự gửi về P-THHC (giữ DL-20260919-001). Kết nối thư mục **không** thay quyền đọc
   kho KTC-Database.
5. Hook đo thể thức, kiểm tra đầu phiên nhận cả thư mục đơn vị; kiểm tra đầu phiên hướng dẫn lối tắt kho khi không thấy kho.
6. Hook nhật ký, tự học **vẫn chỉ** trong dự án (dữ liệu cá nhân — không ghi nhật ký trên máy người khác).

## Kết quả
Plugin **1.3.5**, SHA-256 `228926d5…d929`, commit `ea2d267` + `b0c1824`; hồi quy 22/22 (`test_thu_muc.py` mới, 20 ca gồm ca
ngược); validate --strict đạt; đã cài máy. Khối lõi phải rút gọn để giữ ≤ 2.500 ký tự (bỏ cụm lặp "chỉ hai trạng thái đầu là
đầu ra chính thức" — ý này còn ở mục kiểm tra chất lượng). Nghiệm thu ca 01, 04, 05, 06: 6/8 lượt; 2 lượt ca 01 trượt do
**tiêu chí sai** (lấy `K-KTCN` làm đáp án cho tên "Khoa Kinh tế - Công nghệ" không có trong 11 mã — Bộ công cụ đúng khi không
đoán); đã sửa tiêu chí, chạy lại ca 01: 2/2 lượt đạt. Phiếu nghiệm thu thêm ca **C3** (chỉ Cowork, tài khoản thành viên, ngoài
dự án) — **người phụ trách chạy**; sửa C2 bước 3 (chặn, không còn hỏi). HD v7 thêm 2 đoạn ở mục III.5.

## Chưa làm
- Chưa chạy thật trên Cowork bằng tài khoản thành viên (ca C3).
- Thư mục đơn vị trên Google Drive đồng bộ: dùng được nếu Drive for Desktop đồng bộ về máy; chưa thử.
