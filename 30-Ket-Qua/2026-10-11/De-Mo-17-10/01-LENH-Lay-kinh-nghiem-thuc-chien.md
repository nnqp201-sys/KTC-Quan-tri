# Lệnh lấy nội dung, kinh nghiệm thực chiến để minh họa (tài khoản nnqp201)

Dùng cho buổi làm việc với Đoàn Đảng ủy UBND tỉnh ngày 17/10/2026 (trang "Kinh nghiệm thực chiến" ở phần giới thiệu
KTC-Quan-tri và phần kết thúc). Chạy lần lượt trên từng nền tảng, lưu mỗi kết quả thành tệp `.md` vào thư mục này
(`02-KQ-Chat.md`, `03-KQ-Cowork.md`), rồi báo em để gộp thành 01 trang trình chiếu.

---

## Lệnh 1 — Claude (trò chuyện), tài khoản nnqp201

> Điều kiện: bật **Cài đặt → Khả năng → Tìm kiếm và tham chiếu các cuộc trò chuyện trước** (nếu chưa bật, Claude chỉ
> thấy cuộc trò chuyện hiện tại). Mở **một cuộc trò chuyện mới**, dán nguyên văn khung dưới đây.

```
Tôi chuẩn bị trình bày kinh nghiệm thực tế dùng Claude trong công việc văn phòng, tổng hợp tại Phòng Tổng hợp – Hành
chính và Quản trị, Trường Cao đẳng Kon Tum, trước đoàn công tác của Đảng ủy UBND tỉnh. Hãy TÌM TRONG CÁC CUỘC TRÒ
CHUYỆN TRƯỚC ĐÂY của tôi (từ tháng 7/2026 đến nay) và tổng hợp KINH NGHIỆM THỰC CHIẾN theo 3 nhóm:
(1) quản lý, theo dõi, đôn đốc nhiệm vụ; (2) tổng hợp số liệu, xây dựng báo cáo; (3) soạn thảo, rà soát văn bản.

Với mỗi tình huống (tối đa 12 tình huống, ưu tiên tình huống có sản phẩm thật), lập một dòng bảng gồm:
| Nhóm | Việc cần làm | Claude đã làm gì | Người phải kiểm tra, sửa gì | Kết quả (sản phẩm, số hiệu văn bản nếu đã ban hành) | Thời gian ước tính trước / sau khi dùng AI | Ngày, tên cuộc trò chuyện làm nguồn |

Sau bảng, viết riêng:
A. 05 lỗi điển hình Claude từng mắc trong các cuộc trò chuyện của tôi (bịa căn cứ, sai số liệu, sai thể thức, hiểu sai
   yêu cầu…) và tôi đã phát hiện bằng cách nào.
B. 05 bài học ngắn (mỗi bài một câu) để người mới bắt đầu dùng ngay.
C. Những gì Claude KHÔNG nên được giao.

Yêu cầu bắt buộc:
- Chỉ nêu điều có trong các cuộc trò chuyện; mỗi dòng ghi nguồn. Không tìm thấy thì ghi "không có dữ liệu", không bịa.
- Thời gian ước tính: chỉ ghi khi tôi đã từng nói trong cuộc trò chuyện; nếu không, để trống.
- KHÔNG đưa: họ tên, số điện thoại, email, thông tin cá nhân của người khác; số liệu nội bộ chưa công khai; nội dung tài
  liệu mật. Thay bằng mô tả chung (ví dụ "một đơn vị", "một viên chức").
- Viết tiếng Việt, ngắn gọn, để trình chiếu.
```

---

## Lệnh 2 — Claude Cowork (Claude Desktop), tài khoản nnqp201

> Cowork không đọc lịch sử phiên trước. Lệnh này cho Cowork đọc **sản phẩm đã tạo** trong thư mục làm việc. Kết nối thư
> mục dự án `KTC-Quan-tri` (hoặc thư mục Cowork anh hay dùng), dán khung dưới đây.

```
Thư mục đang kết nối là nơi tôi lưu kết quả làm việc với Claude (thư mục 30-Ket-Qua theo ngày, nhật ký trong
90-Nhat-Ky-Van-Hanh, quyết định trong 92-Kinh-Nghiem). Hãy đọc (KHÔNG sửa, KHÔNG xóa, KHÔNG tạo tệp nào ngoài tệp kết quả)
và tổng hợp KINH NGHIỆM THỰC CHIẾN dùng Claude Cowork từ tháng 9/2026 đến nay theo 3 nhóm: (1) quản lý, theo dõi, đôn đốc
nhiệm vụ; (2) tổng hợp số liệu, báo cáo; (3) soạn thảo, rà soát văn bản.

Lập bảng tối đa 12 tình huống: | Nhóm | Việc | Claude Cowork đã làm gì | Người kiểm tra, sửa gì | Sản phẩm (tên tệp, đường dẫn) | Ngày |
Sau bảng: A. 05 lỗi điển hình đã gặp và cách phát hiện (lấy trong 92-Kinh-Nghiem: Lessons, Known-Issues, Decision-Log);
B. 05 bài học ngắn; C. Khác biệt khi dùng Cowork so với trò chuyện thông thường (đọc, ghi tệp, đo thể thức…).

Yêu cầu: mỗi dòng ghi tệp nguồn; không bịa; không đưa thông tin cá nhân, số liệu nội bộ chưa công khai, nội dung tài
liệu mật. Ghi kết quả vào tệp 30-Ket-Qua/2026-10-11/De-Mo-17-10/03-KQ-Cowork.md.
```

---

## Lệnh 3 — Claude Code (máy Phòng TH-HC&QT)

Không cần anh chạy: em đọc trực tiếp nhật ký tự động, Decision Log, bài học và thống kê vận hành
(`29-Cong-Cu/thong_ke_van_hanh.py`) trên máy này. Anh chỉ cần nhắn: **"Em tổng hợp kinh nghiệm thực chiến trên Claude
Code"**. Kết quả: `04-KQ-Code.md`.

---

## Sau khi có đủ 3 kết quả

Nhắn em: **"Gộp kinh nghiệm thực chiến thành trang trình chiếu"**. Em sẽ: đối chiếu chéo (chỉ giữ điều có nguồn), bỏ
trùng, chọn 05–06 tình huống tiêu biểu khớp 3 nội dung của Công văn số 2868-CV/ĐU, viết 01 trang trình chiếu và lời nói
kèm (khoảng 01 phút).
