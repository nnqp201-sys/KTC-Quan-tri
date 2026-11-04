# Đề xuất Giải pháp Lưu trữ Hỏi đáp Chính sách

**Ngày:** 04/11/2026  
**Người đề xuất:** Agent ktc-hoi-dap-chinh-sach  
**Trạng thái:** Chờ duyệt

---

## 1. Vấn đề

Cần lưu trữ cơ sở dữ liệu hỏi đáp chính sách sao cho:
- Không mất dữ liệu khi cập nhật
- Các agent có thể tra cứu nhanh
- Đồng bộ với Google Drive
- Tuân thủ cấu trúc KTC-Database

## 2. Đề xuất Cấu trúc

```
KTC-Database/
├── Input/
│   └── hoi-dap-chinh-sach/           ← THƯ MỤC MỚI
│       ├── 00-README.md              ← Mô tả kho
│       ├── hoi_dap_index.json        ← Index tra cứu nhanh
│       ├── data/
│       │   ├── 2026-11.json          ← Dữ liệu theo tháng
│       │   ├── 2026-10.json
│       │   └── ...
│       └── archive/
│           └── full_backup_YYYYMMDD.xlsx  ← Backup định kỳ
│
├── 06-Hoi-Dap-Chinh-Sach/            ← KHO MỚI (song song 01-05)
│   ├── 00-README.md
│   ├── 06-01-Giao-duc-Dao-tao/       ← Theo lĩnh vực
│   ├── 06-02-Tai-chinh-Ngan-sach/
│   ├── 06-03-Lao-dong-Vien-chuc/
│   ├── 06-04-Tai-san-Dau-thau/
│   └── 06-05-Chuyen-doi-so/
```

## 3. Quy tắc Lưu trữ

### 3.1. Lưu tăng dần
- Mỗi lần chạy: đọc dữ liệu cũ → merge bản ghi mới → ghi lại
- Hash nội dung để khử trùng
- Giữ ngày thu thập ban đầu

### 3.2. Phân chia file
| Loại | Định dạng | Mục đích |
|------|-----------|----------|
| Index | JSON | Tra cứu nhanh, agent đọc |
| Data | JSON theo tháng | Lưu trữ chi tiết |
| Backup | Excel | Sao lưu, chia sẻ |
| Archive | Excel nén | Lưu trữ dài hạn |

### 3.3. Đồng bộ Google Drive
- Thư mục `KTC-Database` nằm trên Google Drive (`H:\My Drive\KTC-Database`)
- Tự động đồng bộ khi ghi file
- Không cần script đồng bộ riêng

## 4. Tích hợp với Agent

### 4.1. Tra cứu
```python
# Agent đọc index
from duong_dan import KTC_DATABASE_DIR
index_path = KTC_DATABASE_DIR / 'Input/hoi-dap-chinh-sach/hoi_dap_index.json'
```

### 4.2. Cập nhật
```bash
# Chạy từ agent hoặc thủ công
python 29-Cong-Cu/hoi_dap_chinh_sach/run.py
```

## 5. Quyền hạn

| Thao tác | Ai được phép |
|----------|--------------|
| Đọc | Tất cả agent |
| Ghi Input/ | Agent ktc-hoi-dap-chinh-sach |
| Ghi 06-*/ | Chỉ người dùng (qua đề xuất) |
| Xóa | Không tự động |

## 6. Kế hoạch Triển khai

| Bước | Nội dung | Trạng thái |
|------|----------|------------|
| 1 | Tạo thư mục Input/hoi-dap-chinh-sach/ | Chờ duyệt |
| 2 | Cập nhật script xuất JSON | ✓ Đã làm |
| 3 | Chạy thử lần đầu | Chờ bước 1 |
| 4 | Tạo kho 06 (nếu cần) | Tương lai |

## 7. Quyết định cần

**Anh xác nhận:**
1. [ ] Cho phép tạo thư mục `Input/hoi-dap-chinh-sach/` trong KTC-Database
2. [ ] Cho phép agent ghi vào thư mục này
3. [ ] Có cần tạo kho 06 riêng không?

---

*Đề xuất này chờ người dùng duyệt trước khi triển khai.*
