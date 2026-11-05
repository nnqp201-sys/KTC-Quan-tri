# Kho 07 — Hỏi đáp Chính sách

**Mục đích:** Lưu trữ hỏi đáp chính sách từ nguồn chính thức, phục vụ tra cứu tham mưu.

## Cấu trúc

```
07-Hoi-Dap-Chinh-Sach/
├── 00-README.md          ← Tài liệu này
└── hoi_dap_index.json    ← Index tra cứu (agent đọc trực tiếp)
```

## Nguồn dữ liệu

| Nguồn | URL |
|-------|-----|
| Chính sách Online | chinhsachonline.chinhphu.vn |
| Bộ GD&ĐT | moet.gov.vn |
| AI Tools | Perplexity, Exa, Consensus (qua routine) |

## Phân loại

Dữ liệu được phân loại theo **6 Trục TB 817/TB-CĐKT**.

## Cập nhật

- **Thủ công:** `python 29-Cong-Cu/hoi_dap_chinh_sach/run.py`
- **Tự động:** Cloud routine chạy 14:00 thứ 7 hằng tuần

## Tra cứu từ agent

```python
from duong_dan import ktc_database
from pathlib import Path
import json

index_path = Path(ktc_database()) / '07-Hoi-Dap-Chinh-Sach/hoi_dap_index.json'
with open(index_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# data['records'] chứa danh sách hỏi đáp
```

---
*Cập nhật: 04/11/2026*
