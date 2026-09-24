# 28-KTC-KPI — Hệ KPI cá nhân (skill `ktc-kpi-lap-ke-hoach`)

Lập kế hoạch công tác quý và danh mục sản phẩm/chỉ tiêu KPI cá nhân theo QĐ 1923/QĐ-CĐKT. Giai đoạn 1 theo
`30-Ket-Qua/2026-09-24/De-xuat/LENH-SUA-Xay-bo-skill-KPI-giai-doan-1.md`.

## Nguồn và bản sao — sửa ở NGUỒN, không sửa bản sao

| Bản sao trong hệ | Nguồn duy nhất | Đồng bộ bằng |
|---|---|---|
| `references/Skill-Library/19-Quy-Tac-KPI.md` | `20-Chuan-Chung/19-Quy-Tac-KPI.md` | `dong_goi_kpi.py` (C5 kiểm) |
| `scripts/kpi_calc.py`, `kpi_mau.py`, `validate_plan.py` | `29-Cong-Cu/` cùng tên | `dong_goi_kpi.py` |
| `assets/Mau-KeHoach-DanhGia_*.xlsx` (6 tệp) | KTC-Database `03-Templates/03-12- Danh gia xep loai va KPI/` | `dong_goi_kpi.py` (sha256) |
| `references/data/he-so-san-pham-TB1052.csv` | Danh mục kèm TB 1052, KTC-Database kho 02 | `trich_danh_muc_tb1052.py` |

Viết tay trong hệ: `SKILL.md`, `references/Cau-Hoi-Mo.md`, `Known-Issues-Bieu-Mau.md`, `Thuat-Ngu.md`,
`references/quy/*.yaml`.

## Chạy

```bash
python 29-Cong-Cu/dong_goi_kpi.py --dong-bo            # đồng bộ, kiểm hash, trích lại Danh mục
python 92-Kinh-Nghiem/02-Regression/Cases/test_kpi_calc.py
python 92-Kinh-Nghiem/02-Regression/Cases/test_validate_plan.py
python 29-Cong-Cu/kiem_tra_he_thong.py
python 29-Cong-Cu/dong_goi_kpi.py --dong-goi           # đóng gói ktc-kpi-lap-ke-hoach-v<phiên bản>.skill
```

Thêm quý mới: tạo `references/quy/<YYYY>-Q<n>.yaml` theo văn bản hướng dẫn của quý (không có văn bản thì mốc chuẩn
QĐ 1923 và `van_ban_huong_dan: null`).

## Giai đoạn sau

- **2** `ktc-kpi-tu-danh-gia` — khi có QĐ 2078 (văn bản chính) và PL XXIV, XXVI–XXVIII, PL I CV 694.
- **3** `ktc-kpi-tong-hop-xep-loai` và rà soát khung tiêu chí — sau khi giai đoạn 2 chạy thật một quý.
