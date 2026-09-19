# DL-20260919-001 — Đơn vị xử lý dữ liệu thô trong khung chat, tải về, gửi P-THHC

**Ngày:** 19/9/2026 · **Người quyết định:** người dùng (chủ dự án)

**Bối cảnh:** plugin sẽ cài cấp Team; tài khoản phòng/khoa/bộ môn không thấy `10-Dau-Vao/`. Đã đề xuất 2 cách
hộp nhận tự động (Google Form có tải tệp · thư mục Drive dùng chung) → **người dùng không chọn**.

**Quyết định:** đơn vị gửi dữ liệu thô lên khung chat (Chat/Cowork, phiên hoặc Project) → skill xuất sản phẩm
ngay trong phiên/project → người dùng **tải về và tự gửi phòng TH-HC&QT** để tổng hợp. Không có hộp nhận tự động.

**Bổ sung để khâu tổng hợp nhẹ hơn** (Nguyên tắc 3, `20-Chuan-Chung/00-Nguyen-Tac-Chung.md`):
- Tên tệp trả về chuẩn `<mã đơn vị>_<loại>_<kỳ>_v<N>` — P-THHC xếp vào `10-Dau-Vao/01-Dau-Moi-Nop/<kỳ>/<mã>/`
  không cần mở tệp.
- Phiếu tự kiểm kèm tệp (đúng mẫu, số nhiệm vụ theo Trục, lỗi công thức, ô trống); còn lỗi → nói "chưa nên gửi".
