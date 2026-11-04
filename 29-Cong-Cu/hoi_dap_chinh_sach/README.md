# Công cụ Thu thập Hỏi đáp Chính sách

**Phiên bản:** 1.1.0 (04/11/2026)  
**Dự án:** KTC-Quan-tri — Trường Cao đẳng Kon Tum

---

## Tổng quan

Bộ công cụ thu thập, phân loại và tra cứu hỏi đáp chính sách từ các nguồn chính thức, phục vụ công tác tham mưu.

## Cấu trúc

```
29-Cong-Cu/hoi_dap_chinh_sach/
├── crawl_hoi_dap.py      ← Script thu thập chính
├── config.json           ← Cấu hình nguồn
├── requirements.txt      ← Thư viện Python
├── run.py                ← Điểm khởi động
├── README.md             ← Tài liệu này
├── DE_XUAT_LUU_TRU_KTC_DATABASE.md  ← Đề xuất lưu trữ
└── output/               ← Kết quả xuất ra
    └── Co_so_du_lieu_*.xlsx
```

## Cài đặt

```bash
cd "D:/.CLAUDE code/KTC-Quan-tri/29-Cong-Cu/hoi_dap_chinh_sach"
pip install -r requirements.txt
```

## Sử dụng

### Thu thập dữ liệu

```bash
# Nhanh (5 trang, ~2 phút)
python run.py --quick

# Đầy đủ (30 trang, ~15 phút)
python run.py --full

# Chỉ xuất từ dữ liệu cũ
python run.py --export-only
```

### Sử dụng qua Agent

```
Gọi agent: ktc-hoi-dap-dieu-phoi
  → Điều phối tự động
  → Tra cứu dữ liệu có sẵn
  → Gọi AI (Consensus/Exa/Perplexity) khi cần
```

## Nguồn dữ liệu

| Nguồn | URL | Trạng thái |
|-------|-----|------------|
| Chính sách Online | chinhsachonline.chinhphu.vn | ✓ Hoạt động |
| Bộ GD&ĐT | moet.gov.vn | ✓ Hoạt động |
| Bộ Tài chính | mof.gov.vn | ○ Chưa triển khai |
| Thư viện pháp luật | thuvienphapluat.vn | ○ Chưa triển khai |
| **AI Tools** | Consensus, Exa, Perplexity | ✓ Qua agent |

## Phân loại

Dữ liệu được phân loại theo **6 Trục TB 817/TB-CĐKT**:

| Trục | Nội dung | Từ khóa |
|------|----------|---------|
| 1 | Đào tạo, tuyển sinh, chất lượng | đào tạo, sinh viên, giảng viên |
| 2 | Thể chế, cải cách hành chính | quy chế, thủ tục, thanh tra |
| 3 | KHCN, chuyển đổi số | công nghệ, phần mềm, dữ liệu |
| 4 | Xây dựng Đảng | đảng viên, chi bộ, thi đua |
| 5 | Tài chính, nhân sự, tài sản | lương, thuế, đấu thầu, mua sắm |
| 6 | Quốc phòng, an ninh, đối ngoại | bảo vệ, hợp tác quốc tế |

## Đầu ra

### Excel
- Sheet `TẤT CẢ`: toàn bộ bản ghi
- Sheet `Trục 1-6`: theo phân loại
- Sheet `TỔNG QUAN`: thống kê
- Sheet `METADATA`: thông tin phiên bản

### JSON (cho agent)
- `KTC-Database/Input/hoi-dap-chinh-sach/hoi_dap_index.json`

## Agent liên quan

| Agent | Nhiệm vụ |
|-------|----------|
| `ktc-hoi-dap-dieu-phoi` | Điều phối tổng thể |
| `ktc-hoi-dap-chinh-sach` | Chạy script Python |
| `ktc-nghien-cuu-chinh-sach` | Tìm kiếm bằng AI (Consensus, Exa, Perplexity) |

## Lưu ý

1. **Lưu trữ tăng dần**: Mỗi lần chạy merge với dữ liệu cũ, không mất bản ghi
2. **Khử trùng**: Hash nội dung để không lưu trùng
3. **Nguồn chính thức**: Ưu tiên nguồn Chính phủ, Bộ ngành
4. **Hỏi đáp là tham khảo**: Không thay thế văn bản quy phạm pháp luật

## Changelog

### v1.1.0 (04/11/2026)
- Lưu trữ tăng dần (merge dữ liệu cũ)
- Phân loại theo 6 Trục TB 817
- Bổ sung nguồn moet.gov.vn
- Tích hợp agent điều phối
- Hỗ trợ Consensus, Exa, Perplexity qua subagent
