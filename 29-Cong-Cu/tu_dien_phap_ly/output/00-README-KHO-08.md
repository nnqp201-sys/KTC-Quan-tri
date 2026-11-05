# Kho 08 — Từ điển Pháp lý

Kho thuật ngữ pháp lý phục vụ công tác tham mưu, soạn thảo văn bản của Trường Cao đẳng Kon Tum.

## Cấu trúc

```
08-Tu-Dien-Phap-Ly/
├── 00-README.md              # File này
├── tu_dien_index.json        # Index chính (merge từ các file tăng dần)
├── Tu-dien-phap-ly.xlsx      # Bản Excel xuất từ index
└── tu_dien_moi_YYYY-MM-DD.json  # File tăng dần hằng tuần
```

## Nguồn thu thập

- luatvietnam.vn/thuat-ngu-phap-ly.html
- thuvienphapluat.vn/page/ThuatNguPhapLy.aspx
- phapdien.gov.vn (Pháp điển quốc gia)
- VBQPPL có phần "Giải thích từ ngữ"
- Sách, giáo trình pháp luật

## Cấu trúc thuật ngữ

| Trường | Mô tả |
|--------|-------|
| STT | Số thứ tự |
| Thuật ngữ | Tên thuật ngữ pháp lý |
| Mô tả | Giải thích ngắn gọn |
| Định nghĩa | Định nghĩa đầy đủ theo nguồn |
| Tình trạng hiệu lực | Còn hiệu lực / Hết hiệu lực |
| Nguồn | Văn bản, tài liệu nguồn |
| Trục | Trục TB 817 (1-6) |
| Lĩnh vực | 12 lĩnh vực chuyên sâu |
| Ghi chú | Ghi chú bổ sung |

## Cập nhật

- **Routine:** 14:00 thứ 7 hằng tuần (phongthhcqt@gmail.com)
- **Merge:** Chạy `29-Cong-Cu/tu_dien_phap_ly/merge_va_xuat.py` để gộp và xuất Excel

## Sử dụng

Gọi agent `ktc-tu-dien-phap-ly` hoặc dùng module `29-Cong-Cu/tu_dien_phap_ly/tra_cuu.py`.

## Quy ước trích dẫn

- Icon: 📖
- Màu: RGB(0,112,192)
- Format: `📖 [Thuật ngữ]: [Định nghĩa] — Nguồn: [Nguồn]`
