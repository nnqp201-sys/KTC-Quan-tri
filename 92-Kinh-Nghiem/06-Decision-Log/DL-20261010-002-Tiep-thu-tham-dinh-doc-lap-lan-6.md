# DL-20261010-002 — Tiếp thu thẩm định độc lập lần 6 (5 hệ AI) — KTC-Quan-tri 1.3.13

**Nguồn:** 5 báo cáo tại OneDrive `Tham-dinh-AI-plugin\2 Cac AI khac\Lan 6` (10/10/2026): Codex (OpenAI, thay ChatGPT Work) 74 ·
Copilot 81 · Grok 82 · NotebookLM 92 · Gemini 96. **Cả 5 đồng ý ban hành có điều kiện** (chế độ người dùng tự cài); không hệ nào nêu
Mức 1 kỹ thuật của tệp plugin.

## Độ tin cậy (đã kiểm chứng)
- **Codex — cao:** chạy Python trên tệp phát hành: SHA-256 khớp, 291/291 tệp khớp N13, guard chặn 5/10 + cho qua 5/5 thao tác hợp lệ
  (khớp tự khai), N15 khớp JSON gốc, mô tả plugin/skill/agent trong giới hạn. Mở đủ 36 nguồn.
- **Grok — khá:** đúng 4/4 mã kiểm đọc tệp. **NotebookLM — trung bình:** đúng 4 mã, sai mã N01, sai số trang 5 PDF, bịa 2 tên script
  (`hook_before_run.py`, `kpi_tinh_he_so.py`). **Copilot — thấp:** tự ghi không đọc GOP-2, GOP-3, cuối GOP-1; không có Phần A.
  **Gemini — thấp:** không làm Bước 0; nhận định lệch hồ sơ ("giới hạn đơn vị thí điểm", "tương thích tốt Chat/Cowork").
- Mã kiểm đọc tệp (Bước 0) phân loại được độ tin cậy — **giữ cách này cho các lần sau.**

## Quyết định tiếp thu (15 ý kiến: 9 tiếp thu, 3 một phần, 1 ghi nhận, 2 không)
1. **Điều kiện chung của cả 5 hệ:** chuyển 2 tài khoản (`nnqp201`, `phucdaotaotcnkt`) còn quyền chỉnh sửa kho về quyền xem trước khi
   ký. Kiểm lại Drive chiều 10/10: **chưa chuyển**. Việc của người phụ trách; AI không đổi quyền Drive.
2. Codex: trạng thái tồn tại (2)(3)(4) trong BC khắc phục ghi mạnh hơn bằng chứng → **BC khắc phục v2** ghi lại đúng mức.
3. Grok L6-02: TB thêm câu "Claude Code đã kiểm thử theo bộ ca; Claude, Cowork mới dùng thử". Grok L6-03/Gemini: TB thêm khuyến nghị
   mô hình (HD đã có). Codex/NotebookLM: TB, HD hướng dẫn chọn phương án A, không dùng AxB cho số chính thức; **mã nguồn giữ 1.3.13**,
   đặt mặc định A ở lần cập nhật sau. NotebookLM L6-03: HD thêm bước kiểm thủ công khi `FORMAT_BINARY_UNVERIFIED`.
4. Codex L6-01 (Mức 3): N14, N15 lộ đường dẫn có tên tài khoản máy `nnqp2` → `lap_goi_tham_dinh_doc.py` thêm `che_may()` và phép quét
   đường dẫn tuyệt đối. Gói đã gửi không thu hồi được (không phải khóa, mật khẩu).
5. Một phần: thử ghi bằng tài khoản không quản lý + biên bản (HT chỉ đạo không kiểm thử thêm; thay bằng danh sách quyền đọc trực
   tiếp, đưa kiểm tra quyền vào báo cáo quý). Không tiếp thu: Copilot đòi phiếu nghiệm thu, biên bản kiểm kê; 2 phát hiện Copilot sai
   (HD đã cảnh báo Haiku; TB đã có báo cáo quý).

## Quyết định của người phụ trách (10/10/2026, tối) — thay mục 1 ở trên
**Giữ quyền chỉnh sửa cho 2 tài khoản `nnqp201`, `phucdaotaotcnkt`**: do người phụ trách kho (Phó Trưởng phòng TH-HC&QT) trực tiếp
quản lý, dùng để cập nhật văn bản thường xuyên, mọi lúc, mọi nơi. Kho có **4 tài khoản quản lý** (1 chủ sở hữu + 3 chỉnh sửa), 32 tài
khoản người dùng chỉ xem. Điều kiện "chuyển 2 tài khoản về quyền xem" của 5 hệ AI: **tiếp thu một phần** (BC tiếp thu lần 6 nội dung
2.1; BC khắc phục v2 dòng 3, 4). Rủi ro đã ghi trong báo cáo: trên 4 tài khoản quản lý, guard là lớp bảo vệ duy nhất khi dùng plugin;
người quản lý chịu trách nhiệm, khôi phục bằng lịch sử phiên bản Drive. **Không còn việc chặn ban hành.** Không nhắc lại đề nghị hạ
quyền 2 tài khoản này. Trình Phòng QLKHCN&HTPT: Thứ Hai 12/10/2026.

## Điều chỉnh của người phụ trách (10/10/2026, tối) — trạng thái tồn tại (2)
Thay mọi chỗ ghi "đã dùng thử; kiểm thử đầy đủ bổ sung trong vận hành" / "mới dùng thử, chưa kiểm thử theo bộ ca" bằng **"Đã kiểm
thử trên 02 tài khoản (cá nhân và phòng TH-HC&QT)"** — theo khẳng định của người phụ trách xây dựng (người trực tiếp kiểm thử trên
Claude trò chuyện, Cowork). Đã sửa: BC khắc phục v2 (dòng 2), BC tiếp thu lần 6 (3.2, 4.1, 6.1, 6.2, mục 7, mục 8), TB v9 (điểm c
Mục 1 Phần I), HD v9 (Mục 1 Phần II), báo cáo 897 (dòng 2). Nội dung 3.2 (Codex) chuyển thành **tiếp thu một phần** → tổng hợp:
7 tiếp thu, 5 một phần, 1 ghi nhận, 2 không. Lưu ý: Hồ sơ không kèm kết quả kiểm thử trên hai nền tảng này (BC tiếp thu ghi rõ
"không lập hồ sơ kết quả riêng"); mục 3 ở trên (câu Grok L6-02) đã được thay bằng câu mới.

## Sản phẩm
`30-Ket-Qua/2026-10-10/Soan-Thao/`: BC tiếp thu, giải trình lần 6 v1 (6 trang) · BC khắc phục v2 · TB v9, HD v9 (Track Changes 3 tác
giả: "Khắc phục tồn tại…", "Sửa theo rà soát 897…", "Tiếp thu thẩm định lần 6") + bản sạch. Hồ sơ lần 2:
`30-Ket-Qua/2026-10-10/Tham-Dinh-Lan-2/` (16 tệp, có 5 báo cáo AI). BC khắc phục v1 → `99-Luu-Tru/Ban-nhap-bi-thay-the/`.
Phần bổ sung sau rà soát 897 mới qua kiểm tự động (0 gợi ý), chưa rà lại toàn văn. Gói AI lần 6 **không dựng lại** (giữ đúng bản đã gửi).

## Kỹ thuật
`TrackChanges.thay()` không tìm được chữ nằm trong đoạn đã chèn (w:ins) của lượt trước → phải sửa ở bước gốc rồi chạy lại cả chuỗi
(`chay_chuoi_v9.sh` trong scratchpad: sua_v9 → the thức HD → chân trang → 897 → lần 6 → bản sạch).
