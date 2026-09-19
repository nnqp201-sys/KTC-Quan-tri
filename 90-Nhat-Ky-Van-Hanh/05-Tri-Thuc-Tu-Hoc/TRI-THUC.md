# TRI-THUC — Kho tri thức tự học của hệ KTC-Quan-tri

Agent `ktc-tu-hoc` rút tri thức từ nhật ký tự động và ghi vào đây (DL-20260919-005). Hook nạp các mục **hiệu lực**
và **chờ duyệt** vào context đầu mỗi phiên (tối đa 25 mục mới nhất).

Quy tắc giữ kho sạch:
- Chỉ ghi điều **có bằng chứng**: lời người dùng nguyên văn, Decision Log, hoặc kết quả kiểm chứng thật.
- **Không** chép lại sự thật vận hành đã có trong `MEMORY-INDEX.md`; chỉ trỏ tới.
- Mục mới mâu thuẫn mục cũ thì đổi mục cũ sang `đã thay (TT-…)`, không xóa.
- Không ghi mật khẩu, token, thông tin cá nhân.

**Trạng thái:**
- `hiệu lực`: người dùng nói rõ, hoặc đã kiểm chứng.
- `chờ duyệt`: tự suy ra, người dùng xác nhận thì chuyển sang `hiệu lực`.
- `đã thay (TT-…)` / `bị bác`: không còn áp dụng.

Mục có cột Chuyển = `→ CP` cần sửa quy tắc hoặc skill; agent `ktc-tu-cai-tien` sẽ viết đề xuất.

| Mã | Loại | Điều đã học | Bằng chứng | Phạm vi | Trạng thái | Chuyển |
|---|---|---|---|---|---|---|
| TT-20260919-01 | sự thật | Pháp lệnh Hợp nhất VBQPPL 01/2012 do **Ủy ban Thường vụ Quốc hội** ban hành, không phải Quốc hội; người dùng từng gọi là "pháp lệnh của Quốc hội" | VBHN 118/VBHN-VPQH (kho 01-02); DL-20260919-002 | viện dẫn | hiệu lực | — |
| TT-20260919-02 | kỹ thuật | Trong Bash heredoc, `\\` bị gộp thành `\` (đã gặp nhiều lần ngày 18–19/9; lần gần nhất biến `\b` thành ký tự backspace trong regex của tra_hieu_luc.py). Mã Python có dấu `\` phải ghi bằng Write/Edit, không dùng heredoc | nhật ký 19/9: tra_hieu_luc.py, repack; bộ nhớ phiên | Code | hiệu lực | — |
| TT-20260919-03 | kỹ thuật | Ghi tệp bằng `open(p, "w")` trên Windows đổi LF thành CRLF, làm regex dòng phiên bản không khớp khi đóng gói lại skill. Phải dùng `newline=""` hoặc Edit | đóng gói soan-thao-vb v1.7 bị dừng, 19/9 | đóng gói | hiệu lực | → CP |
| TT-20260919-04 | sự thật | Mẫu `.dotx` có `themeFontLang=vi-VN`: phông "major" của theme hiển thị là **Times New Roman** (script Viet), không phải Calibri Light | đo 73 tệp, DL-20260919-003 | thể thức | hiệu lực | — |
| TT-20260919-05 | sửa sai | Thư mục ghi "xóa được" (`_trung_gian/`) vẫn có tệp do git quản lý (`00-README.md`, `narrative.json`). Trước khi xóa phải chạy `git ls-files <thư mục>` | xóa nhầm rồi khôi phục, 19/9 | dọn hệ | hiệu lực | → CP |
| TT-20260919-06 | quy ước | Không sửa trực tiếp skill `docx`/`xlsx` của Anthropic (bị đồng bộ ghi đè, giấy phép độc quyền); chuẩn của Trường thì đặt ở lớp chồng lên (skill `the-thuc`) | yêu cầu người dùng 19/9; DL-20260919-003 | skill | hiệu lực | — |
| TT-20260919-07 | quy ước | Khi 897 có hai chỗ mâu thuẫn nhau, người dùng lấy theo **checklist** (`02-Noi-Dung.md`), không lấy theo mẫu ví dụ trong Skill-Library | "897 đã quy định rất rõ, VBHC thì viện dẫn Luật không ghi số hiệu", 19/9 | viện dẫn | chờ duyệt | — |
| TT-20260919-08 | sửa sai | Cowork từ chối plugin có mô tả trong `plugin.json` > **500 ký tự** (mô tả skill/agent ≤ 1024). Mô tả plugin chỉ nêu phạm vi và danh sách thành phần; không nối thêm theo từng phiên bản | Lỗi upload 0.8.0 (554 ký tự), ảnh chụp người dùng 19/9; `dong_goi_plugin.py` nay tự chặn | đóng gói plugin | hiệu lực | — |
