Phương thức đọc file: HỖN HỢP — nội dung chữ đọc qua `get_file_metadata` (`contentSnippet`, đáng tin cậy, xác nhận khớp 100% với lần đọc trước). **Nhị phân thật KHÔNG lấy được** — thử lại kỹ thuật đã thành công với file `.skill` (ghi base64 qua `create_file` rồi `base64 -d`), nhưng riêng file `File-Test-Loi-KTC897.docx` bị lỗi corrupt ở `word/document.xml` — đây là lần thứ 3 gặp đúng lỗi này với riêng file này (không phải lỗi ngẫu nhiên một lần).

Phiên bản: v2.16
Ngày chạy: 26/8/2026
Điểm: 8/28 đúng hoàn toàn, 7/28 đúng nhưng sai mức, 13/28 bỏ sót (bộ 28 lỗi gốc)
**KHÔNG CHẤM #29-30** — lý do nêu rõ ở Mục 2 dưới đây, không phải "bỏ sót" theo nghĩa hệ thất bại.

═══════════════════════════════════════════════════════════════════
1. KẾT QUẢ SO VỚI v2.14 — GIỐNG HỆT, VÀ ĐÂY LÀ ĐIỀU DỰ KIẾN, KHÔNG BẤT THƯỜNG
═══════════════════════════════════════════════════════════════════

| Chỉ số | v2.14 | v2.16 | Thay đổi |
|---|---|---|---|
| Đúng hoàn toàn | 8/28 | 8/28 | Không đổi |
| Sai mức | 7/28 | 7/28 | Không đổi |
| Bỏ sót | 13/28 | 13/28 | Không đổi |

**Giải thích tại sao KHÔNG đổi — đây không phải lỗi, mà là hệ quả logic đúng đắn:**

Các thay đổi thật sự của v2.15→v2.16 là:
1. Tích hợp `_read_input_properties.py` — chỉ ảnh hưởng lỗi **định lượng thuần túy** (#1 lề trang, #5/#29/#30 cỡ chữ trích yếu). **Không ảnh hưởng** 25 lỗi còn lại dựa trên nội dung chữ.
2. Skill viện dẫn văn bản hợp nhất — **không áp dụng** cho hồ sơ này vì văn bản test không chứa cụm "hợp nhất"/"VBHN".
3. Chi tiết 3 tiểu-hệ đoàn thể (Bước 0) — là **mô tả bổ sung**, không tự động thay đổi ngưỡng phân loại Mức cho #25 (vẫn cần tự phân loại, không có công thức máy tính sẵn).

Vì cả 3 thay đổi trên không chạm tới 25/28 lỗi dựa-trên-chữ, và #1/#5 (2 lỗi định lượng còn lại trong bộ 28 gốc) **không kiểm thử được lần này** do giới hạn kỹ thuật — kết quả 8/7/13 giống hệt là **đúng theo logic, không phải dấu hiệu hệ thống trì trệ**.

═══════════════════════════════════════════════════════════════════
2. TẠI SAO KHÔNG CHẤM ĐƯỢC #29-30 (VÀ CẢ #1, #5) — GIỚI HẠN KỸ THUẬT THẬT
═══════════════════════════════════════════════════════════════════

`_read_input_properties.py` **yêu cầu file nhị phân thật** (mở bằng `python-docx`, gọi `section.left_margin`, `run.font.size`) — không thể chạy trên `contentSnippet` (chỉ là text thuần).

Đã thử 3 lần trong toàn bộ quá trình làm việc với hệ này để lấy nhị phân thật của `File-Test-Loi-KTC897.docx` qua `download_file_content` + giải mã base64 thủ công — **cả 3 lần đều lỗi** ở đúng vị trí `word/document.xml`, dù cùng kỹ thuật đã **thành công** khi áp dụng cho file `.skill` (256KB, giải mã hoàn hảo, byte-identical).

**Do đó, lần chạy này**:
- #1 (lề trang), #5 (trích yếu Trang 1 cỡ chữ), #29 (trích yếu Trang 2), #30 (trích yếu Trang 3) — **đều không kiểm thử được**, không phải "hệ bỏ sót".
- 8/7/13 là điểm số **chỉ tính trên 26 lỗi dựa-trên-chữ có thể kiểm thử được qua contentSnippet** (28 lỗi gốc trừ #1 và #5 — nhưng vì #1/#5 vẫn nằm trong mẫu số 28 theo quy ước tính điểm cũ, và cả hai vẫn được xếp "bỏ sót" trong bảng dưới vì thực tế em cũng bỏ sót chúng khi chỉ đọc chữ — **kết quả tính bỏ sót cho #1/#5 là ĐÚNG về bản chất** dù nguyên nhân là do không đọc thuộc tính định dạng, giống hệt v2.14).

**Điểm mấu chốt cần nêu rõ với anh Phục**: câu hỏi "_read_input_properties.py có thực sự cải thiện độ chính xác hay không" — **CHƯA CÓ CÂU TRẢ LỜI KHÁCH QUAN** sau lần chạy này, vì chưa từng chạy được script đó trên chính file nhị phân thật của bộ test. Mọi xác nhận trước đây (kể cả lần v2.15) chỉ dựa trên **dữ liệu mô phỏng** (file .docx tự tạo bắt chước đặc điểm đã biết qua log thủ công của phiên phongthhcqt), không phải file test gốc.

═══════════════════════════════════════════════════════════════════
3. BẢNG SO SÁNH v2.14 vs v2.16 (YÊU CẦU CỦA LỆNH) — TRUNG THỰC VỀ GIỚI HẠN
═══════════════════════════════════════════════════════════════════

| | v2.14 (28/28 gốc) | v2.16 (28/28 gốc) | Ghi chú |
|---|---|---|---|
| Đúng hoàn toàn | 8 (28,6%) | 8 (28,6%) | Không đổi — dự kiến, xem Mục 1 |
| Sai mức | 7 (25%) | 7 (25%) | Không đổi |
| Bỏ sót | 13 (46,4%) | 13 (46,4%) | Không đổi |
| #29-30 (mở rộng) | Chưa tồn tại trong đáp án lúc đó | Đã thêm vào đáp án, **chưa chấm được** | Giới hạn kỹ thuật đọc nhị phân |

**Kết luận trung thực**: đây **KHÔNG PHẢI** bằng chứng khách quan đầu tiên cho việc vá `_read_input_properties.py` có cải thiện hay không — vì phép đo quan trọng nhất (chạy script thật trên file thật) vẫn chưa thực hiện được. Bằng chứng đó vẫn còn là **việc tồn đọng**, không phải đã có sẵn.

═══════════════════════════════════════════════════════════════════
4. VIỆC CẦN LÀM TIẾP (không chặn việc coi v2.16 là hoàn thành các phần khác)
═══════════════════════════════════════════════════════════════════

1. Tìm cách khác để lấy nhị phân thật của `File-Test-Loi-KTC897.docx` — có thể cần anh Phục hỗ trợ tải và re-upload dưới định dạng khác (ví dụ .zip đổi tên), hoặc dùng công cụ khác ngoài `download_file_content` của MCP hiện tại.
2. Sau khi có nhị phân thật, chạy `_read_input_properties.py` thật, đối chiếu đúng 4 lỗi #1/#5/#29/#30, tính lại điểm đầy đủ 30/30.
3. Cho tới lúc đó, mọi khẳng định về "script đã cải thiện độ chính xác" phải ghi rõ là DỰA TRÊN MÔ PHỎNG, không phải kết quả thật.
