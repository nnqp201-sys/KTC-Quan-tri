# 20-Chuan-Chung — Lớp chuẩn dùng chung của KTC-Quan-tri

Nơi giữ **bản gốc** của mọi quy tắc và bảng mã mà từ hai hệ con trở lên cùng dùng. Sửa ở đây trước, rồi mới
lan xuống các hệ.

## Quy tắc quan trọng nhất — đọc trước khi dọn trùng lặp

**Không được xóa bản sao 5 tệp dùng chung nằm trong `<hệ>/references/Skill-Library/`.**

Gói `.skill` là một tệp zip tự chứa, upload lên Claude và chạy độc lập — nó *bắt buộc* mang theo bản sao
các tệp quy tắc. Xóa bản sao trong hệ để "khử trùng lặp" sẽ làm hỏng skill ngay lần đóng gói lại kế tiếp.

Cách làm đúng:

```
20-Chuan-Chung/<tệp>.md          ← sửa ở đây (nguồn gốc)
        ↓ nhân bản tại bước đóng gói
23-KTC-Ke-Hoach/references/Skill-Library/<tệp>.md
25-KTC-Bao-Cao/references/Skill-Library/<tệp>.md
KTC-DIS-Tong-Hop-VB/references/Skill-Library/<tệp>.md
```

Tại thời điểm lập thư mục này (13/9/2026), 5 tệp dưới đây đang **trùng md5 y hệt** ở cả 3 hệ — tức đang
đồng bộ. Nhưng chưa có cơ chế nào giữ cho chúng tiếp tục đồng bộ; đây vẫn là nhân bản thủ công.

## Nội dung

### Nhóm kế thừa — bản gốc của tệp đang nhân bản ở 3 hệ

| Tệp | Nội dung |
|---|---|
| `00-Nguyen-Tac-Chung.md` | Nguyên tắc bất biến: phải đối chiếu kho 01–04 trước khi tạo kết quả; bắt buộc xuất `.docx` |
| `00-Metadata-Schema.md` | 11 trường bắt buộc + 2 trường theo loại + 3 trường trách nhiệm |
| `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` | Điều kiện và cách ghi nguồn khi nạp văn bản từ Internet |
| `30-Skill-Phan-Loai-6-Truc.md` | Cách phân loại nhiệm vụ vào 6 Trục |
| `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` | Quy tắc viện dẫn văn bản hợp nhất (VBHN) |

### Nhóm mới — chuẩn riêng của KTC-Quan-tri

| Tệp | Nội dung | Trạng thái |
|---|---|---|
| `10-Tu-Dien-Truong-Du-Lieu.md` | 46 trường của Master Task Register, chia 8 nhóm A–H; ai được ghi nhóm nào | Dự thảo để chốt |
| `11-Quy-Tac-Task-ID.md` | Cấu trúc `KTC-<năm>-<kỳ>-<số>`; phân biệt Task_ID với mã nhiệm vụ chuẩn `A01`–`S04` | Dự thảo để chốt |
| `12-Vong-Doi-Trang-Thai.md` | 7 trạng thái chính + 5 trạng thái phụ + 8 loại cảnh báo | Dự thảo để chốt |
| `13-Bang-Ma-Don-Vi.md` | 11 mã đơn vị chuẩn và ánh xạ sang 3 kiểu viết đang tồn tại | **Đã đối chiếu nguồn thật** |
| `14-Nguyen-Tac-Soan-Thao-Bat-Bien.md` | NT-1 phát triển từ file tương đồng · NT-2 Track Changes · NT-3 khai thác bộ quy tắc 897 · NT-4 KTC-Database là CSDL tham mưu | **Bất biến — đọc trước mọi tác vụ sinh văn bản** |
| `15-Skill-Track-Changes.md` | Điều kiện kích hoạt + quy trình 4 bước dùng `29-Cong-Cu/ktc_trackchanges.py`; thi hành NT-2 | **Đã kiểm thử** |

## Thứ tự đọc khi bắt đầu thiết kế Master Task Register

1. `11-Quy-Tac-Task-ID.md` — hiểu hai lớp mã trước, tránh nhầm lẫn gốc rễ
2. `13-Bang-Ma-Don-Vi.md` — biết dữ liệu đơn vị đang lệch tới mức nào
3. `10-Tu-Dien-Truong-Du-Lieu.md` — bộ trường
4. `12-Vong-Doi-Trang-Thai.md` — trạng thái và cảnh báo
