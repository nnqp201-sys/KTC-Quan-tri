---
paths:
  - "tools/**"
  - "99-Kinh-Nghiem/02-Regression/**"
  - "**/*.skill"
description: Ba tầng kiểm thử và quy tắc đóng gói .skill
---

# Chạy thử hệ thống

```bash
python tools/kiem_tra_he_thong.py      # Tầng 1 — tĩnh, 11 phép kiểm, mã thoát 0/1
python 99-Kinh-Nghiem/02-Regression/Cases/test_kiem_tra_he_thong.py   # thử ngược
```

**Bắt buộc chạy sau mỗi lần sửa skill và trước/sau mỗi lần đóng gói.** Hướng dẫn đầy đủ ba tầng kiểm thử
(tĩnh · hành vi trên dữ liệu thật · định tuyến trên Claude Chat): `99-Kinh-Nghiem/02-Regression/README.md`.

**Một phép kiểm hỏng luôn báo "sạch".** Thêm phép kiểm mới thì phải thêm ca thử ngược trong cùng lần sửa.
