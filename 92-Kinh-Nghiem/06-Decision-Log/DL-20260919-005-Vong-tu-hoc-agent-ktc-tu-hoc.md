# DL-20260919-005 — Vòng tự học: ghi lời người dùng, agent `ktc-tu-hoc`, kho TRI-THUC nạp lại mỗi phiên

**Ngày:** 19/9/2026 · **Người quyết định:** người dùng (chủ dự án)

**Yêu cầu:** *"Phát triển thêm agent: tự log và lưu vào context để tự học những điều mới, lưu thông tin để tự cải tiến."*

**Hiện trạng trước khi làm:**
- Hook chỉ ghi thao tác công cụ (tên công cụ, đối tượng). **Không ghi lời người dùng**, nên các chỉnh sửa và quy
  ước anh đưa ra bị mất sau mỗi phiên.
- Có `ktc-tu-cai-tien` (viết đề xuất sửa quy tắc) nhưng **chưa có kho tri thức** được nạp lại vào phiên sau.

**Quyết định — tách hai tầng:**
1. **Tự học** (nhanh): quy ước, sửa sai, sự thật đã kiểm chứng, kinh nghiệm kỹ thuật được ghi ngay vào
   `90-Nhat-Ky-Van-Hanh/05-Tri-Thuc-Tu-Hoc/TRI-THUC.md`, có bằng chứng. Hook SessionStart nạp lại các mục
   `hiệu lực` và `chờ duyệt`. Điều agent tự suy ra luôn là `chờ duyệt`.
2. **Tự cải tiến** (có kiểm soát): mục cần sửa quy tắc hoặc skill được đánh dấu `→ CP`. `ktc-tu-cai-tien` viết đề
   xuất và người dùng duyệt (Nguyên tắc bất biến 6).

**Đã làm:**
- `ktc_nhat_ky.py`:
  - chế độ `yeu-cau` (hook **UserPromptSubmit**): ghi lời người dùng, cắt ≤ 600 ký tự, bỏ lệnh nội bộ
    `/…` và `<command…>`, gắn tín hiệu `sua-sai`, `quy-uoc`, `quyet-dinh`;
  - chế độ `nap`: in thêm tri thức tự học và số tín hiệu chưa xử lý kể từ `.lan-hoc-cuoi`.
- `ktc_the_thuc_hook.py`: ghi `canh-bao-the-thuc` vào nhật ký, làm bằng chứng lỗi lặp lại.
- Agent mới `ktc-tu-hoc`: chỉ ghi được trong `05-Tri-Thuc-Tu-Hoc/`. `ktc-tu-cai-tien` đọc thêm các mục `→ CP`.
- Khởi tạo kho: 7 mục có bằng chứng từ phiên 18–19/9, trong đó 2 mục `→ CP` (ghi tệp làm mất LF; kiểm
  `git ls-files` trước khi xóa).
- Ca hồi quy `test_tu_hoc.py`: 11 ca, gồm thử ngược và kiểm tra không ghi nhầm vào nhật ký thật.
- Plugin **0.8.0**, tổng **6 agent**.

**Giới hạn:**
- Hook không tự gọi agent: Claude Code không cho hook khởi chạy agent. Thay vào đó, đầu phiên in nhắc "⟳ N tín
  hiệu chưa xử lý" để gọi `ktc-tu-hoc`.
- Nhận diện tín hiệu dùng từ khóa, nên có báo thừa; agent lọc lại theo ngữ cảnh.
- Lời người dùng được lưu trong repo GitHub **riêng tư**. Không gõ mật khẩu hoặc token vào khung chat.
- Hook chạy trong Claude Code; Cowork có chạy hook và agent của plugin hay không thì chưa kiểm chứng.
