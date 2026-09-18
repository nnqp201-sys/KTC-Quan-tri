---
name: ktc-tu-hoc-ke-hoach
description: "Phân tích, học có kiểm soát và áp dụng các mẫu kế hoạch đã được Trường Cao đẳng Kon Tum phê duyệt để tạo, cập nhật hoặc kiểm tra kế hoạch công tác năm, quý, tháng và kế hoạch chuyên đề đúng cấu trúc 6 Trục, đúng quan hệ năm→quý→tháng, đúng thể thức và định dạng Excel/Word của KTC. Dùng khi người dùng yêu cầu học mẫu kế hoạch, chuẩn hóa đầu ra theo mẫu, tạo kế hoạch, kiểm tra độ giống mẫu, cập nhật bộ quy tắc kế hoạch, hoặc tự cải tiến từ phản hồi/sản phẩm được xác nhận. Không dùng cho tổng hợp báo cáo kết quả hoặc rà soát văn bản hành chính nói chung."
---

# KTC tự học Kế hoạch

## Mục tiêu

Học kỹ thuật lập kế hoạch từ nguồn đã được xác nhận, không sao chép dữ liệu nguồn. Duy trì bộ nhớ chuẩn về cấu trúc, định dạng, phân cấp thời gian, 6 Trục, sản phẩm, trách nhiệm và tiến độ để đầu ra sau ngày càng sát mẫu chính thức hơn.

## Tệp phải đọc theo tác vụ


> **Lưu ý (14/9/2026)**: `ktc-tu-hoc-ke-hoach` là **skill độc lập**, đóng gói riêng. Các tệp nêu dưới đây
> nằm trong gói đó, **không** nằm trong gói `ktc-ke-hoach`. Phải nạp cả hai skill mới dùng được đầy đủ.

- Trước mọi tác vụ: đọc `output-contract.md` **của skill `ktc-tu-hoc-ke-hoach`** (gói riêng tại `references/ktc-tu-hoc-ke-hoach.skill`, không nằm trong gói này).
- Khi tạo hoặc định dạng năm/quý/tháng: đọc `template-format-dna.md` và `template-sources.md` **của skill `ktc-tu-hoc-ke-hoach`**; sao chép mẫu tương ứng trực tiếp từ Google Drive. Chỉ dùng `assets/templates/` nếu bản cài đặt cục bộ được người dùng cho phép mang theo mẫu.
- Khi học mẫu mới hoặc nhận phản hồi: đọc `lifelong-learning.md` và `provenance-log.md` **của skill `ktc-tu-hoc-ke-hoach`**.
- Khi cần phân tích OOXML: chạy `scripts/analyze_plan_templates.py` trên bản sao làm việc, không sửa nguồn.

## Quy trình bắt buộc

1. Xác định loại sản phẩm: chương trình năm, kế hoạch quý, kế hoạch tháng, kế hoạch chuyên đề hay quyết định ban hành.
2. Khóa nguồn: ưu tiên Google Drive trong `KTC-Database`, `KTC-Ke-Hoach`, `KTC-Bao-Cao`; không sửa tệp nguồn.
3. Chọn đúng mẫu gốc. Không dựng lại từ đầu khi mẫu tương ứng còn dùng được; sao chép mẫu rồi thay nội dung có kiểm soát.
4. Đối chiếu phân cấp:
   - tháng phải bám quý;
   - quý phải bám năm;
   - nhiệm vụ chuyên đề chỉ thêm khi chưa trùng; nếu chỉ cụ thể hóa thì ghi nguồn/ghi chú;
   - mọi nhiệm vụ phải có chủ trì, sản phẩm và thời hạn kiểm chứng được.
5. Phân loại nhiệm vụ theo 6 Trục kết quả trọng tâm TB 817 dựa trên kết quả chính, không dựa đơn thuần vào tên đơn vị.
6. Tạo sản phẩm đúng DNA định dạng; bảo toàn công thức, vùng gộp, độ rộng cột, chiều cao dòng, thiết lập trang, khối ký và nơi nhận.
7. Kiểm tra nội dung và hiển thị: không lỗi công thức, không cắt chữ, không tràn bảng, không mất đường viền, không sai phân cấp thời gian.
8. Nếu là dự thảo trình ký, chuyển sang `ktc-ra-soat-897` để rà soát chính thức.
9. Lưu đầu ra vào `30-Ket-Qua/YYYY-MM-DD/<loại thao tác>/` hoặc vị trí người dùng chỉ định; giữ nhật ký nguồn và thay đổi.

## Cơ chế tự học có kiểm soát

Không tự thay đổi chuẩn chỉ vì gặp một tệp mới. Thực hiện vòng lặp:

`Nguồn ứng viên → phân tích → so với chuẩn hiện có → đề xuất quy tắc mới → xin xác nhận → cập nhật → kiểm thử hồi quy → ghi provenance`.

Chỉ học khi nguồn được người dùng xác nhận là “chuẩn”, “hay”, “mẫu chính thức”, nằm trong kho mẫu tốt, hoặc là sản phẩm đã trình ký/ban hành. Không tự xóa quy tắc cũ; khi xung đột, ưu tiên nguồn chính thức hơn, mới hơn và đúng loại kế hoạch hơn.

## Quy tắc không được vi phạm

- Không biến dữ liệu ví dụ thành dữ liệu kế hoạch mới.
- Không làm mất nhiệm vụ cấp trên giao hoặc nhiệm vụ chuyển kỳ.
- Không gộp nhiệm vụ khác sản phẩm, khác chủ trì hoặc khác thời hạn chỉ vì nội dung gần nhau.
- Không thêm trùng nhiệm vụ chuyên đề đã được bao hàm trong kế hoạch định kỳ.
- Không tự quyết định đơn vị chủ trì khi có tranh chấp/chồng chéo.
- Không giao sản phẩm chỉ có dữ liệu mà sai định dạng mẫu.
- Không coi “đã ban hành kế hoạch” là đã hoàn thành toàn bộ nhiệm vụ trong kế hoạch.

## Tiêu chí hoàn thành

Chỉ giao khi sản phẩm qua đủ bốn cổng:

1. **Nội dung:** đủ nhiệm vụ, không trùng, đúng nguồn.
2. **Logic:** đúng năm→quý→tháng và đúng 6 Trục.
3. **Trách nhiệm:** rõ chỉ đạo, chủ trì/phối hợp, sản phẩm, số lượng, thời hạn.
4. **Hình thức:** khớp mẫu về font, bố cục, bảng, trang in, khối ký; đã kiểm tra trực quan.
