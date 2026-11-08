---
paths:
  - "29-Cong-Cu/**"
  - "92-Kinh-Nghiem/02-Regression/**"
  - "**/*.skill"
description: Ba tầng kiểm thử và quy tắc đóng gói .skill
---

# Chạy thử hệ thống

```bash
python 29-Cong-Cu/doctor.py                 # Entrypoint hợp nhất — 5 bước, mã thoát 0/1
python 29-Cong-Cu/doctor.py --nhanh         # Bỏ qua pytest

# Hoặc chạy riêng:
python 29-Cong-Cu/kiem_tra_he_thong.py      # Tầng 1 — tĩnh, 13 phép kiểm
```

**Bắt buộc chạy `doctor.py` sau mỗi lần sửa skill và trước/sau mỗi lần đóng gói.** Hướng dẫn đầy đủ ba tầng kiểm thử
(tĩnh · hành vi trên dữ liệu thật · định tuyến trên Claude Chat): `92-Kinh-Nghiem/02-Regression/README.md`.

**Một phép kiểm hỏng luôn báo "sạch".** Thêm phép kiểm mới thì phải thêm ca thử ngược trong cùng lần sửa.
