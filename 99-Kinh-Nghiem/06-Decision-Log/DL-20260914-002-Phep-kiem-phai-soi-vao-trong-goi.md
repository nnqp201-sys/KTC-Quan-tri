# DL-20260914-002 — Phép kiểm tệp dùng chung phải soi vào bên trong gói `.skill`

**Ngày:** 14/9/2026 · **Loại:** APPLY · **Đề xuất gốc:** `CP-20260914-001` GĐ1–GĐ2

## Bối cảnh

Phép kiểm **C5** của `tools/kiem_tra_he_thong.py` so bản gốc `01-Chuan-Chung/` với bản sao ở
`<hệ>/references/Skill-Library/`. Bản rời khớp 100% ở mọi hệ nên C5 in `✓ khớp ở mọi hệ`.

Nhưng thứ chạy trên Claude Chat/Cowork là gói `.skill`, không phải bản rời. Trong gói:

| Tệp | Bản gốc | `ktc-bao-cao-v3.5` | `ktc-ke-hoach-v3.1` |
|---|---|---|---|
| `30-Skill-Phan-Loai-6-Truc.md` | 9.034 B | 4.515 B | 6.823 B |
| `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` | 3.569 B | 1.218 B | 2.138 B |
| `00-Metadata-Schema.md` | 3.018 B | 1.527 B | 2.906 B |

Không phải lệch vô hại: bản trong gói gọi **Trục 4** là *"…phòng, chống tham nhũng"* trong khi bản chuẩn
theo TB 817 là *"…giữ gìn đoàn kết, thống nhất"*, và thiếu hẳn mục `Trigger conditions`.

## Quyết định

1. **C5 soi cả hai nơi.** Lệch ở bản rời → cảnh báo (còn kịp sửa trước khi đóng gói).
   Lệch ở bản **trong gói** → **LỖI**, vì đó là thứ đang chạy thật.
2. **Không nâng C4 thành lỗi.** C4 phát hiện mọi lệch giữa nguồn rời và gói, trong đó phần lớn là hành vi
   **bình thường** của cơ chế đóng gói (xem mục "Vì sao lệch"). Biến C4 thành lỗi sẽ khiến phép kiểm luôn
   đỏ và mất tác dụng. Quy tắc tệp dùng chung do C5 sở hữu, không nhân đôi sang C4.
3. **In phân bố cảnh báo theo phép kiểm** ở dòng kết luận, để một việc đang chặn không lẫn trong hàng chục
   dòng cảnh báo mà người chạy không bắt buộc mở `--chi-tiet` ra xem.

## Lý do

C5 **không hỏng** — nó nhìn nhầm chỗ. Hệ quả giống hệt một phép kiểm hỏng, nhưng nguy hiểm hơn vì nó in
dấu ✓: người chạy có bằng chứng dương tính giả rằng hệ đang sạch.

## Vì sao lệch — cơ chế, không phải sự cẩu thả

`tools/dong_goi_skill.py` không gom thư mục nguồn rời rồi nén. Nó chạy:

```
giai_nen(gói cũ → thư mục tạm) → sao_nguon(chép MỘT DANH SÁCH TỆP LIỆT KÊ TAY) → dong_goi(nén lại)
```

Gói cũ là **nền**; nguồn rời chỉ phủ lên những tệp được gọi tên. Tệp không nằm trong danh sách thì giữ
nguyên bản cũ trong gói — vĩnh viễn, qua mọi lần đóng gói. Thiết kế này **đúng** (nó bảo vệ lớp `Memory/`
và các tệp chỉ có trong gói khỏi bị xóa) nhưng thiếu vế kiểm: không có bước nào rà xem có tệp nào đáng lẽ
phải được phủ mà bị bỏ quên. Ba tệp trên rơi đúng vào khe đó.

*Đính chính `CP-20260913-001` ĐX-1:* đóng gói lại **không** làm mất lớp `Memory/`. Rủi ro thật là chiều
ngược lại — bản sửa ở nguồn rời không bao giờ vào được gói nếu không được liệt kê tay.

## Hệ quả kèm theo

- Ca thử ngược bắt buộc: `99-Kinh-Nghiem/02-Regression/Cases/test_c5_soi_trong_goi.py` — 5 ca, gồm ca
  "bản rời khớp nhưng trong gói là bản cũ" (đúng điểm mù đã mắc) và ca "gói không mang tệp này" để C5
  không bịa lỗi.
- **Điều kiện nghiệm thu cố ý là phép kiểm phải BÁO ĐỎ trước.** Một bản sửa phép kiểm mà chạy xong vẫn
  xanh trên dữ liệu đã biết là sai thì bản sửa đó vô dụng. C5 đã báo 6 lỗi trước khi đồng bộ dữ liệu.
- Đồng bộ xong sinh ba gói mới: `ktc-bao-cao-v3.6.skill`, `ktc-ke-hoach-v3.2.skill`, và
  `ktc-soan-thao-vb.skill` đóng lại (hệ này **cũng** mang tệp dùng chung — chính C5 mới sửa phát hiện ra,
  bản cũ lưu tại `99-Luu-Tru/`).

**Liên quan:** `CP-20260914-001` · `LL-20260914-001` · `KI-014` · `KI-013`
