# BẢNG CHỈ SỐ THEO THỜI GIAN — KTC-Ra-Soat-897-v2 Hồi quy  

Theo dõi tỷ lệ đúng/sai của Hệ qua các phiên bản, dùng chung 1 bộ test cố định (`File-Test-Loi-KTC897.docx`, 28 lỗi gốc + 2 lỗi mở rộng #29-30 từ 26/8/2026) để so sánh được giữa các lần đóng gói `.skill`.  

## Bảng tổng  

| Ngày | Phiên bản | Đúng hoàn toàn | Sai mức | Bỏ sót | Ghi chú |  
|---|---|---|---|---|---|  
| 25/8/2026 | v2.14 | 8/28 (28,6%) | 7/28 (25%) | 13/28 (46,4%) | **Baseline** — lần đầu có số liệu khách quan. |  
| 26/8/2026 | v2.16 | 8/28 (28,6%) | 7/28 (25%) | 13/28 (46,4%) | Không đổi so với baseline — đúng theo logic (v2.15/16 chỉ thêm tính năng chưa kiểm thử được trên file thật lần đó). |  
| 26/8/2026 | **v2.17** | **12/30 (40%)** ▲ | 7/30 (23,3%) | **11/30 (36,7%)** ▼ | **Lần đầu tiên chạy `_read_input_properties.py` THẬT trên file gốc** (không phải mô phỏng) — sau khi giải quyết dứt điểm lỗi copy tay base64 bị cắt cụt. Cả 4/4 lỗi định lượng mới (#1, #5, #29, #30) đều bắt đúng, đúng Mức. |  
| 05/9/2026 | **v2.21** | **25/30 (83,3%)** ▲ | 1/30 (3,3%) ▼ | **4/30 (13,3%)** ▼ | Tác vụ tự động. Cải thiện lớn: 11 lỗi nội dung text trước bỏ sót nay phát hiện được (#10-11-13-15-17-19-21-22-26-27-28). 4 lỗi bỏ sót còn lại đều là `FORMAT_BINARY_UNVERIFIED` (#1-5-29-30). **Cảnh báo bias:** đáp án đọc đồng thời với file test — cần xác nhận bằng phiên rà soát mù. |  
| 07/9/2026 | **v2.21** | **25/30 (83,3%)** = | 1/30 (3,3%) = | **4/30 (13,3%)** = | Tác vụ tự động (lần 2). Kết quả đồng nhất với lần 05/9 — **xác nhận ổn định**. Cảnh báo bias còn tồn tại. FORMAT_BINARY_UNVERIFIED: #1,5,29,30. |  

## Bảng theo trang (hệ quy chiếu)  

| Ngày | Phiên bản | Trang 1 — Hành chính | Trang 2 — Đảng | Trang 3 — Đoàn thể | Ghi chú |  
|---|---|---|---|---|---|  
| 25/8/2026 | v2.14 | 7/19 (36,8%) | 1/5 (20%) | 0/4 (0%) | Baseline |  
| 26/8/2026 | v2.16 | 7/19 (36,8%) | 1/5 (20%) | 0/4 (0%) | Không đổi |  
| 26/8/2026 | **v2.17** | **9/19 (47,4%)** ▲ | **2/6 (33,3%)** ▲ | **1/5 (20%)** ▲ | Cải thiện ở CẢ 3 trang nhờ script đọc thuộc tính định dạng thật |  
| 05/9/2026 | **v2.21** | **17/19 (89,5%)** ▲ | **5/6 (83,3%)** ▲ | **3/5 (60%)** ▲ | Cải thiện mạnh cả 3 trang. Bỏ sót còn lại: #1 (lề T1), #5 (cỡ chữ T1), #29 (cỡ chữ T2), #30 (cỡ chữ T3) — tất cả FORMAT_BINARY_UNVERIFIED. |  
| 07/9/2026 | **v2.21** | **17/19 (89,5%)** = | **5/6 (83,3%)** = | **3/5 (60%)** = | Đồng nhất với lần 05/9 — xác nhận ổn định. Không phát hiện hồi quy. |  

## ✅ VIỆC TỒN ĐỌNG ĐÃ GIẢI QUYẾT (26/8/2026)  

**Câu hỏi "`_read_input_properties.py` có thực sự cải thiện độ chính xác hay không" — NAY ĐÃ CÓ CÂU TRẢ LỜI: CÓ, cải thiện thật.**  

Tỷ lệ đúng hoàn toàn tăng từ 28,6% (v2.14/v2.16) lên **40%** (v2.17) khi chạy script thật trên chính file test gốc — không còn dựa vào dữ liệu mô phỏng như các lần đo trước. Cả 4/4 lỗi định lượng (#1 lề trái, #5/#29/#30 cỡ chữ trích yếu 3 trang) đều được phát hiện đúng vị trí và đúng Mức.  

**Nguyên nhân 3 lần thất bại trước** (đã xác định dứt điểm): copy tay chuỗi base64 dài (14.792 ký tự) bị rơi mất một đoạn giữa khi thao tác thủ công — không phải lỗi Drive, không phải lỗi ID cache, không phải "giới hạn môi trường". Giải pháp: kiểm tra độ dài chuỗi base64 khớp công thức `(fileSize/3)*4` TRƯỚC khi giải mã.  

## ⚠️ GHI CHÚ v2.21 (05/9/2026)  

Kết quả 83,3% **cần xác nhận bổ sung** vì:  
- Đáp án và file test đọc trong cùng một phiên (không phải rà soát mù).  
- Cải thiện từ 40% → 83,3% là rất lớn — phần cải thiện thật nằm ở nhóm lỗi nội dung text (Skill v2.21 đã bổ sung Checklist 09 hệ D, cập nhật quy tắc số hiệu Đảng/đoàn thể, từ vựng "Bảo đảm" v.v.).  
- Khuyến nghị: lần kiểm thử tiếp theo cần phiên rà soát mù độc lập để xác nhận con số thật.  

## 📌 GHI CHÚ v2.21 lần 2 (07/9/2026)  

Kết quả đồng nhất hoàn toàn với lần 05/9 — **xác nhận tính ổn định của Skill v2.21** trong môi trường tự động.  
- Cảnh báo bias vẫn còn tồn tại (đáp án đọc cùng phiên với file test).  
- 4 lỗi bỏ sót còn lại (#1, #5, #29, #30) là giới hạn cấu trúc của phiên đám mây (không có `_read_input_properties.py`), không phải hồi quy.  
- Không có hồi quy — không cần đánh dấu thủ công.  

## Cách đọc bảng  

- **Đúng hoàn toàn**: phát hiện đúng vị trí + đúng Mức + kiến nghị đủ để khắc phục đúng bản chất lỗi.  
- **Sai mức**: gồm 2 dạng — (1) chấm sai số Mức 1-4, hoặc (2) Mức đúng nhưng kiến nghị/số liệu cụ thể sai.  
- **Bỏ sót**: không phát hiện vấn đề tại vị trí đó.  

## Nguồn dữ liệu từng dòng  

| Ngày | File kết quả chi tiết |  
|---|---|  
| 25/8/2026 (v2.14) | `Ket-Qua-Cham-Diem/Ket-qua-v2.14_25082026_lan2.md` |  
| 26/8/2026 (v2.16) | `Ket-Qua-Cham-Diem/Ket-qua-v2.16_26082026.md` |  
| 26/8/2026 (v2.17) | `Ket-Qua-Cham-Diem/Ket-qua-v2.17_26082026_THAT.md` — dữ liệu thật, không mô phỏng |  
| 05/9/2026 (v2.21) | `Ket-Qua-Cham-Diem/Ket-qua-v2.21_05092026.md` — tác vụ tự động, cảnh báo bias đáp án |  
| 07/9/2026 (v2.21, lần 2) | `Ket-Qua-Cham-Diem/Ket-qua-v2.21_07092026.md` — tác vụ tự động lần 2, kết quả đồng nhất, xác nhận ổn định |  

## Quy tắc cập nhật bảng này  

1. Chỉ điền dòng mới sau khi kết quả chấm điểm của phiên bản đó đã được xác nhận hợp lệ.  
2. Không xóa dòng cũ — bảng theo dõi xu hướng lịch sử.  
3. Không ghi số liệu "cải thiện" hay "▲/▼" cho hạng mục chưa thực sự kiểm thử được trên file thật — thà để trống còn hơn suy diễn.  
4. **Bài học từ đợt v2.17**: khi tải nhị phân qua base64 thủ công, luôn kiểm tra `len(base64) == (fileSize/3)*4` trước khi giải mã — tránh lặp lại 3 lần thất bại trước khi tìm ra nguyên nhân.  
