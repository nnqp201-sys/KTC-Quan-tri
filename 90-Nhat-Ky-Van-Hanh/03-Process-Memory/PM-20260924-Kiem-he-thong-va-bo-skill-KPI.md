```yaml
memory_id: PM-20260924-001
created_at: 2026-09-24
memory_type: process
status: closed
task_type: kiem_tra_he_thong_va_xay_skill
project_name: KTC-Quan-tri
```

# Phiên 23–24/9/2026 — sửa công cụ sau đợt đổi bố cục đầu vào, xây skill KPI giai đoạn 1

**Kết quả:** 9 commit (`2c44bca` … `2a9d5c4`); plugin 1.0.0 → **1.1.1**; skill mới `ktc-kpi-lap-ke-hoach` v1.0
(`DL-20260924-001`); sổ mốc hạn + hook đầu phiên; CP bảo mật nhật ký chờ duyệt (`CP-20260924-001`).

## Bài học — dùng lại cho lần sau

1. **Đổi bố cục thư mục đầu vào làm hỏng công cụ một cách im lặng.** Commit 54a2476 (21/9) đổi
   `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/<mã đơn vị>/KH-….xlsx` thành `1. BAO CAO PL IIB/KHCB.xlsx`. Hậu quả:
   `doi_soat_so_lieu.py` gộp 10 đơn vị thành một, xếp `KHCB.xlsx` (báo cáo) là kế hoạch — **vẫn thoát mã 0**; một ca
   hồi quy đọc thư mục đang sống thì vỡ. Cách sửa đã dùng: (a) công cụ nhận đơn vị/loại/kỳ **từ phần đầu tệp** khi tên
   không theo quy ước; (b) ca hồi quy **ghim dữ liệu vào một commit git**, không đọc thư mục đang sống.
   → Khi thấy đầu vào đổi cách đặt tên, chạy `doi_soat_so_lieu.py` và xem DS06 trước khi tin kết quả.
2. **Trước khi nói "chưa có mã/chưa có quyết định", đọc hết tệp chuẩn.** Đã báo sai nhiều lượt rằng Ban Truyền thông
   "chưa có mã (KI-015)" — thực ra `13-Bang-Ma-Don-Vi.md` đã ghi quyết định 14/9/2026: cấp hai thuộc `P-THHC`. Quyết
   định viết bằng văn xuôi thì máy không đọc được → đã thêm mục "Ánh xạ bổ sung — máy đọc".
3. **Trùng tên tệp không có nghĩa là bản sao.** 12/14 cảnh báo C8 là trùng tên ngẫu nhiên (prompt soạn và prompt rà soát
   cùng tên `01-Quyet-Dinh.md`). C8 nay đo độ giống theo dòng (≥ 50% mới là bản sao lệch).
4. **Đọc toàn văn trước khi tin tóm tắt — kể cả tóm tắt của chính mình.** Lệnh sửa 24/9 giả định hai mốc đầu quý thuộc
   hai sản phẩm khác nhau; đọc toàn văn thấy QĐ 1923 Đ15.3a áp cho **cả cá nhân**. Cũng nhờ đọc Phụ lục II QĐ 1923 mới
   biết thang hệ số 4 mức **có văn bản** — điều KI-014 chưa ghi.
5. **Mẫu Excel của Trường chứa sẵn cách tính** (sheet KPI: J = SL × hệ số; % Trục = trung bình 3 chiều ÷ SL quy đổi;
   điểm Trục = % × điểm tối đa theo nhóm vị trí). Script phải khớp mẫu, điền vào **bản sao** và giữ công thức — không
   dựng bảng mới.
6. **Kỹ thuật:** thay chuỗi bằng `str.replace` trong heredoc không báo khi không khớp → ca thử tưởng đã thêm mà chưa.
   Dùng `assert old in s` hoặc công cụ Edit. Hook 897 chặn `rm -rf` — dùng thư mục tạm mới thay vì xóa.

## Việc còn mở (không lặp trạng thái ở đây — xem nơi gốc)

`Moc-Han.md` (MH-001…005) · `28-KTC-KPI/references/Cau-Hoi-Mo.md` (9 câu) · `CP-20260924-001` · định tuyến skill KPI
trên Chat chưa chạy (`28-KTC-KPI/TEST-REPORT.md` mục 3) · `BAN TT.docx` kỳ 2026-09 là báo cáo **tháng 8** (có thể
nộp nhầm tệp) · K-KTNL chưa nộp Phụ lục Excel kỳ 2026-09.
