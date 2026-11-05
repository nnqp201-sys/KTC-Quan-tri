# Công cụ Từ điển Pháp lý

Thu thập và tra cứu thuật ngữ pháp lý phục vụ công tác tham mưu, soạn thảo văn bản của Trường Cao đẳng Kon Tum.

## Cấu trúc

```
tu_dien_phap_ly/
├── 00-README.md          # File này
├── tra_cuu.py            # Module tra cứu (CHỈ ĐỌC)
├── xuat_excel.py         # Xuất Excel với dashboard
└── output/               # Kết quả xuất
```

## Nguồn dữ liệu

Dữ liệu được lưu tại `KTC-Database/08-Tu-Dien-Phap-Ly/`:
- `tu_dien_index.json` — Index chính
- `tu_dien_moi_YYYY-MM-DD.json` — File tăng dần hằng tuần

## Nguồn thu thập

1. **Web chuyên ngành:**
   - https://luatvietnam.vn/thuat-ngu-phap-ly.html
   - https://thuvienphapluat.vn/page/ThuatNguPhapLy.aspx

2. **Pháp điển quốc gia:** phapdien.gov.vn

3. **KTC-Database:** Trích từ phần "Giải thích từ ngữ" trong VBQPPL

4. **Tài liệu xuất bản:** Sách, giáo trình, từ điển pháp luật

5. **Công trình nghiên cứu:** Luận văn, bài báo khoa học

## Cấu trúc thuật ngữ

| Trường | Mô tả |
|--------|-------|
| STT | Số thứ tự |
| Thuật ngữ | Tên thuật ngữ pháp lý |
| Mô tả | Giải thích ngắn gọn |
| Định nghĩa | Định nghĩa đầy đủ theo nguồn |
| Tình trạng hiệu lực | Còn hiệu lực / Hết hiệu lực / Chưa xác định |
| Nguồn | Văn bản, tài liệu nguồn |
| Trục | Trục TB 817 (1-6) |
| Lĩnh vực | 1 trong 12 lĩnh vực |
| Ghi chú | Ghi chú bổ sung |

## Phân loại

### 6 Trục TB 817
1. Đào tạo, tuyển sinh, chất lượng
2. Thể chế, cải cách hành chính
3. KHCN, chuyển đổi số
4. Xây dựng Đảng
5. Tài chính, nhân sự, tài sản
6. Quốc phòng, an ninh, đối ngoại

### 12 Lĩnh vực chuyên sâu
- giao-duc, hssv, vien-chuc, tien-luong
- thue-phi, bao-hiem, dau-thau, tai-san
- xay-dung, thi-dua, khcn, hanh-chinh

## Sử dụng

### Tra cứu trong Python
```python
from tra_cuu import tim_thuat_ngu, thong_ke

# Tìm thuật ngữ
results = tim_thuat_ngu("viên chức", truc="5", linh_vuc="vien-chuc")

# Thống kê
stats = thong_ke()
print(f"Tổng: {stats['total']} thuật ngữ")
```

### Gọi agent
Gọi `ktc-tu-dien-phap-ly` — tự động dispatch sang sub-agent theo lĩnh vực.

## Quy ước trích dẫn

- Icon: 📖
- Màu: RGB(0,112,192) — xanh dương
- Format: `📖 [Thuật ngữ]: [Định nghĩa] — Nguồn: [Nguồn]`

## Cập nhật

- **Routine:** phongthhcqt@gmail.com, 14:00 thứ 7 hằng tuần
- **Liên hệ:** phongthhcqt@gmail.com
