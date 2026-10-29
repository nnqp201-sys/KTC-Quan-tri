# PM-20260828-Tao-File-Test-Loi-KTC897-v2.18

```yaml
memory_id: PM-20260828-REGRESSION-FIXTURE-v2.18
created_at: 2026-08-28T13:43:00+07:00
memory_type: process
status: closed
task_type: regression_fixture_creation
project_name: KTC-Ra-Soat-897-v2-Cai-tien
system_version: v2.18
```

## 1. Mục tiêu
Phát triển từ `File-Test-Loi-KTC897.docx` để tạo bộ test hồi quy mở rộng, bao phủ các lỗi/quy tắc người dùng đã yêu cầu cập nhật qua các phiên v2.12–v2.18.

## 2. Nguồn
- File gốc do người dùng cung cấp: `File-Test-Loi-KTC897.docx`.
- `DAP-AN-Loi-Da-Cai-San.md`: 30 lỗi chuẩn gốc.
- `SKILL.md` v2.18 ngày 28/8/2026.
- Skill viện dẫn VBHN và trigger v2.16.
- Lệnh/báo cáo cập nhật v2.17 về `_read_input_properties.py` và làm tròn ngưỡng lề.

## 3. Nguyên tắc xây dựng
- Giữ nguyên toàn bộ 30 lỗi gốc.
- Không sửa các lỗi gốc vì đây là fixture kiểm thử.
- Bổ sung lỗi mới nhưng tránh làm mất tính xác định của lỗi cũ.
- Bổ sung một số control âm tính để đo false positive.
- Không dùng Track Changes vì đây là tạo fixture mới từ bản nguồn, không phải chỉnh sửa nghiệp vụ để trình ký.

## 4. Nhóm lỗi mới đã cài
1. Viện dẫn VBHN như văn bản pháp luật độc lập.
2. Dùng sai số hiệu VBHN Luật Kế toán (14 thay vì 41/VBHN-VPQH).
3. Thiếu ngoặc đơn cho cụm `(hợp nhất tại Văn bản hợp nhất số ...)`.
4. Viện dẫn riêng văn bản sửa đổi dù đã có VBHN.
5. Coi tài liệu trong `KTC-Database/03-Templates` là “mẫu trống” để áp dụng.
6. Không viết hoa sau dấu hai chấm: `Đơn vị thực hiện: phòng...`.
7. Ghi “đã điều chỉnh QĐ49 thành QĐ988” nhưng nội dung thực tế vẫn còn QĐ49.
8. Công đoàn dùng nhầm tiêu đề hệ Đoàn Thanh niên.
9. Section Công đoàn có lề trái 2,99cm (<30mm) để test ngưỡng thật.
10. Quyết định liên quan doanh nghiệp/góp vốn nhưng không dẫn chiếu Luật Doanh nghiệp và pháp luật quản lý vốn nhà nước.
11. `Người kiểm tra: ChatGPT`.
12. AI tự gán `Trạng thái phê duyệt: CHÍNH THỨC`.

## 5. Control âm tính
1. Section Hội Sinh viên có lề trái đúng 3,00cm — không được báo lỗi do sai số float.
2. Hội Sinh viên không có tiêu đề tổ chức ở cột phải — không được áp mẫu Đoàn TN để báo lỗi.
3. `KTC-DIS-v1` chỉ xuất hiện trong ngữ cảnh chuyển tiếp/lịch sử — không tự động coi là lỗi.
4. Metadata chưa có dữ liệu ghi `không xác định` — đúng quy tắc, không suy đoán.

## 6. Kiểm tra kỹ thuật
- DOCX đã render thành 8 trang bằng `render_docx.py`.
- Đã kiểm tra trực quan đủ 8 trang: không clipping, không overlap, bảng không vỡ, không mất glyph.
- File đầu ra: `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx`.
- Drive ID: `1aKbLCYSxWlvcrvrL8lAvVpx8j2d5ngZD`.
- Vị trí: `KTC-Ra-Soat-897-v2-Cai-tien/13-Regression-Test/`.

## 7. Cách dùng
Chạy rà soát chính thức trên file này. Đối chiếu ít nhất 30 lỗi gốc + 12 ca lỗi mới. Theo dõi riêng false positive tại 4 control âm tính.

## 8. Next action
Sau lượt test đầu tiên trên v2.18, ghi kết quả phát hiện/đúng mức/bỏ sót/false positive và dùng để cập nhật BANG-CHI-SO-THEO-THOI-GIAN.
