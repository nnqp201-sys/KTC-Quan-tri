# Tra cứu Hỏi đáp Chính sách

**Phiên bản:** 2.0.0 (04/11/2026)  
**Dự án:** KTC-Quan-tri — Trường Cao đẳng Kon Tum

---

## Tổng quan

Module tra cứu hỏi đáp chính sách từ kho `KTC-Database/07-Hoi-Dap-Chinh-Sach`.

**Dữ liệu được cập nhật tự động** bởi routine ở tài khoản `phongthhcqt@gmail.com` (KTC-Database), chạy 14:00 thứ 7 hằng tuần.

## Cấu trúc

```
29-Cong-Cu/hoi_dap_chinh_sach/
├── tra_cuu.py        ← Module tra cứu
├── README.md         ← Tài liệu này
└── _archive/         ← Script cũ (không dùng)
```

## Sử dụng

### Trong Python

```python
from hoi_dap_chinh_sach.tra_cuu import tim_kiem, thong_ke

# Tìm kiếm theo từ khóa
ket_qua = tim_kiem('viên chức')

# Tìm theo Trục
ket_qua = tim_kiem('lương', truc=5)

# Thống kê
stats = thong_ke()
print(f"Tổng: {stats['tong']} bản ghi")
```

### Trong agent

```
Gọi agent: ktc-hoi-dap-chinh-sach
Prompt: "Tìm hỏi đáp về chế độ viên chức giáo dục"
```

## Nguồn dữ liệu

| Nguồn | Cập nhật |
|-------|----------|
| KTC-Database/07-Hoi-Dap-Chinh-Sach | Tự động, thứ 7 hằng tuần |
| chinhsachonline.chinhphu.vn | Qua routine |
| moet.gov.vn | Qua routine |
| Perplexity, Exa | Qua routine |

## Phân loại 6 Trục TB 817

| Trục | Nội dung |
|------|----------|
| 1 | Đào tạo, tuyển sinh, chất lượng |
| 2 | Thể chế, cải cách hành chính |
| 3 | KHCN, chuyển đổi số |
| 4 | Xây dựng Đảng |
| 5 | Tài chính, nhân sự, tài sản |
| 6 | Quốc phòng, an ninh, đối ngoại |

## Lưu ý

- **Chỉ đọc** — không thu thập tại KTC-Quan-tri
- **Dữ liệu tham khảo** — không thay thế văn bản quy phạm pháp luật
- **Routine chạy ở KTC-Database** — liên hệ admin nếu cần cập nhật

## Changelog

### v2.0.0 (04/11/2026)
- Chuyển sang chỉ tra cứu (không crawl)
- Dữ liệu cập nhật tự động từ KTC-Database
- Lược bỏ script thu thập

### v1.1.0 (04/11/2026)
- Phiên bản crawl đầy đủ (đã archive)
