# PM-20260927 — Rà soát 897 vòng 3 (phần sửa) và tiếp thu thẩm định lần 4

**Ca:** rà soát bổ sung phần sửa lần 3, 4 của Dự thảo Thông báo (bản 7) và Tài liệu hướng dẫn (bản 6), Hệ A.
**Kết quả:** 0 Mức 1; Mức 2: câu "dữ liệu nội bộ, dữ liệu cá nhân chỉ được xử lý trên nền tảng đã có biên bản…" đọc thành
nới rộng so với TB 924 (cấm thông tin cá nhân nhạy cảm, tài liệu nội bộ chưa được phép công bố) → giới hạn "trong phạm vi
được phép theo TB 924"; câu "Claude Code đã có kết quả nghiệm thu" dễ hiểu là đủ điều kiện dữ liệu thật.

## Bài học

1. **Khi thêm điều kiện "được phép … khi …", đối chiếu văn bản cấm đã ban hành** (TB 924, Mục 7 TB 1056) — câu điều kiện
   dễ bị đọc thành cho phép rộng hơn.
2. **Rà soát phần sửa theo diff từng đoạn/ô** so với bản đã qua rà soát, không đọc lại cả văn bản — phạm vi rõ, nhanh.
3. **Người phụ trách mở tệp trong thư mục hồ sơ để đọc rồi lưu** → mất Track Changes, lệch mã băm. Từ vòng 5: gửi kèm bản
   sạch, đặt chỉ đọc tệp TrackChanges, chạy `kiem_ho_so.py` ngay trước khi gửi.
4. **Hàm thêm hàng bảng Track Changes chép hàng vừa chèn** → hàng mới mang nhiều `w:ins` trong `trPr`; chấp nhận thay đổi
   chỉ gỡ một → "bản sạch" còn 1 revision. Đã sửa cả hai phía (scratchpad `tc_them.py`; nếu đưa vào `29-Cong-Cu/` phải mang
   theo sửa này).
5. **Nghiệm thu mô hình dao động** giữa các đợt (30/30 → 26/30 trên cùng nội dung skill) — báo cáo đủ các đợt, phân loại
   từng lượt trượt (hạ tầng / giám khảo chấm oan / lỗi thật), không chọn đợt đẹp.
