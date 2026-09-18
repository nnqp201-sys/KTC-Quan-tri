# BÀI HỌC KINH NGHIỆM KTC-RIS

Các lỗi đã trả giá. Đọc khi thấy mình sắp làm điều tương tự.
Mỗi bài: chuyện đã xảy ra → bài học → dấu hiệu nhận biết sớm.

---

## BH-01 — Số hiệu phiên bản cao hơn KHÔNG có nghĩa là ít lỗi hơn
**Xảy ra:** 19/08/2026. Bản v3.0 trông mới hơn v2.5.1, nhưng kiểm thử cho thấy nó giữ nguyên
13/14 lỗi cũ, trong đó có 3 lỗi làm sai số liệu KPI và điền sai nội dung báo cáo.

**Bài học:** Hai bản phát triển song song từ cùng một gốc sẽ có tập lỗi khác nhau, không phải
tập lỗi lồng nhau. Phải **chạy kiểm thử rồi mới kết luận**, không suy từ số hiệu.

**Dấu hiệu:** Hai bản có cùng ngày cập nhật, hoặc nhánh nào đó tách ra trước một đợt vá lớn.

## BH-02 — Lỗi nguy hiểm nhất là lỗi không báo lỗi
**Xảy ra:** 19/08/2026. Script v2.3 gặp nhãn `Trục 1.` thì đọc ra **0 nhiệm vụ** và vẫn báo thành công.
Người tổng hợp sẽ tưởng đơn vị không có việc gì.

**Bài học:** Với script xử lý dữ liệu báo cáo, "trả về rỗng" phải bị coi là **bất thường cần cảnh báo**,
không phải kết quả hợp lệ. Đã đưa vào v2.5.1: cảnh báo `[DỪNG]` khi đọc được 0 nhiệm vụ.

**Dấu hiệu:** Hàm trả về kết quả rỗng/None mà không kèm lý do.

## BH-03 — Kiểm thử trên fixture mô phỏng không thay được file thật
**Xảy ra:** 19/08/2026. Bản vá v2.5.1 đạt 15/15 phép kiểm trên fixture, nhưng vẫn dính BUG-15
(Mục II) — lỗi chỉ lộ ra khi nhìn cấu trúc file thật, mà v3.0 đã phát hiện nhờ đối chiếu file thật.

**Bài học:** Fixture chỉ kiểm được những gì mình đã nghĩ tới. File thật chứa các biến thể ngoài
dự liệu. Phải chạy trên file thật trước khi tin là đã xong.

**Dấu hiệu:** Câu "đã kiểm thử đầy đủ" mà chưa hề mở một file thật nào.

## BH-04 — Kiểm tra quyền thực tế, đừng đoán
**Xảy ra:** 19/08/2026. Đã kết luận sai rằng thư mục skill không ghi được, khiến người dùng
mất công thao tác thủ công. Thử một lệnh `touch` là biết ngay — thư mục ghi được bình thường.

**Bài học:** Khi định nói "không làm được", **thử trước rồi hãy nói**. Nói sai theo hướng
"không làm được" gây tốn công người khác và làm mất lòng tin.

**Dấu hiệu:** Sắp phát biểu về giới hạn hệ thống mà chưa hề kiểm chứng trong phiên hiện tại.

## BH-05 — Bám sát mẫu gốc, đừng sáng tạo thể thức
**Xảy ra:** trước 14/08/2026. Các bản báo cáo đầu tiên lệch khỏi mẫu chuẩn TB736, phải dựng lại từ đầu.

**Bài học:** Thể thức văn bản hành chính là ràng buộc pháp lý, không phải gợi ý thiết kế.
Bảng KPI thuộc về Phụ lục Excel, **không** nhúng vào thân báo cáo Word.

**Dấu hiệu:** Đang "cải tiến" bố cục mà chưa mở file mẫu gốc ra đối chiếu.

## BH-06 — Bản vá trong phiên sẽ biến mất
**Xảy ra:** 19/08/2026. Vá script trực tiếp trong thư mục skill — có hiệu lực ngay, nhưng mất
khi phiên kết thúc nếu không đóng gói lại thành `.skill` và cài qua giao diện.

**Bài học:** Sửa xong phải **đóng gói ngay trong cùng phiên**, đừng để lần sau.

**Dấu hiệu:** Đầu phiên thấy `SKILL.md` ghi số hiệu cũ hơn mong đợi → bản vá đã mất.

---

## Cách thêm bài học

Chỉ ghi khi **đã thực sự trả giá** — mất thời gian, phải làm lại, hoặc suýt ra sản phẩm sai.
Nguyên tắc chung chưa từng gây hậu quả thì thuộc về `Skill-Library/`, không thuộc file này.
Luôn kèm **dấu hiệu nhận biết sớm** — đó mới là phần dùng được lần sau.
