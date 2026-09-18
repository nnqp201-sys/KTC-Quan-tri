# KTC-Theo-doi-CV — Control Tower nhiệm vụ

Hệ trung gian giữa `KTC-Ke-Hoach` và `KTC-Bao-Cao`: nhận nhiệm vụ đã có Task_ID từ kế hoạch, theo dõi vòng
đời, phát cảnh báo, thu nhận kết quả và minh chứng, rồi cung cấp dữ liệu cho báo cáo.

**Không tự tạo nhiệm vụ mới** nếu nhiệm vụ đã tồn tại trong kế hoạch — chỉ tiếp nhận, phân công, cập nhật,
ghi nhận thay đổi.

## Nội dung thư mục

| Tệp | Nội dung |
|---|---|
| `SKILL.md` · `ktc-theo-doi-cv-v1.0.skill` | Gói skill v1.0 (14/9/2026) |
| `references/Skill-Library/` | 5 skill 40–44 + 2 tệp chuẩn dùng chung |
| `references/Workflow/11-Theo-Doi-Vong-Doi.md` | Quy trình 6 bước |
| `00-Template-Routing-KTC-Theo-doi-CV.docx` | Mẫu định tuyến nhiệm vụ |
| `01. Bộ dữ liệu vận hành KTC-Theo-dõi-CV.xlsx` | Bảng "Nhiệm vụ" 19 cột — **hiện đang rỗng**, trạng thái Thiết kế, tổng nhiệm vụ = 0 |
| `02. Nhật ký liên thông KTC-Theo-dõi-CV.xlsx` | Nhật ký liên thông giữa các hệ |

## Trạng thái phát triển — đọc kỹ trước khi dùng

**Cập nhật 14/9/2026:** đã có `SKILL.md` và gói `ktc-theo-doi-cv-v1.0.skill` (10 tệp, 5 skill nghiệp vụ
40–44 + quy trình 6 bước). Hệ nay chạy được trên Claude Chat/Cowork như bốn hệ còn lại.

**Còn lại đúng một khoảng trống, nhưng là khoảng trống lớn nhất:** bộ dữ liệu vận hành **chưa có dòng
nào** — 0 nhiệm vụ, 0 cập nhật tiến độ, 0 minh chứng, 0 đề nghị điều chỉnh.

Hệ quả trực tiếp: mọi kiểm thử cầu nối giữa hệ này và `KTC-Bao-Cao` cho tới nay đều chạy trên **dữ liệu mẫu
tự tạo**, không phải dữ liệu vận hành thật. Kết luận "tên đơn vị khớp 100%" trong
`04-Tai-Lieu-Thiet-Ke/GHI-CHU-CAU-NOI-3-HE.md` thuộc diện này — đối chiếu trên dữ liệu thật cho kết quả
khác, xem `01-Chuan-Chung/13-Bang-Ma-Don-Vi.md`.

## Vai trò trong chu trình hợp nhất

```
KTC-Ke-Hoach ──cấp Task_ID──> KTC-Theo-doi-CV ──kết quả + minh chứng──> KTC-Bao-Cao
                                     │
                                     └── cảnh báo: sắp hạn · quá hạn · chưa bắt đầu ·
                                         không cập nhật · tiến độ thấp · thiếu sản phẩm ·
                                         thiếu minh chứng · nguy cơ không hoàn thành
```

Quyền ghi vào Master Task Register: **nhóm F (Tiến độ) và G (Kết quả)**. Các nhóm A–E chỉ đọc.

Chi tiết vòng đời 7 trạng thái chính + 5 trạng thái phụ và điều kiện phát 8 cảnh báo:
`01-Chuan-Chung/12-Vong-Doi-Trang-Thai.md`.

## Việc cần làm tiếp

1. Nạp dữ liệu nhiệm vụ thật vào `01. Bộ dữ liệu vận hành` — chừng nào còn rỗng thì chưa kiểm chứng
   được gì. **Đây là việc chặn mọi việc còn lại.**
2. Đối chiếu 19 cột hiện có với 46 trường của Master Task Register, xác định trường thiếu/thừa.
3. ~~Viết `SKILL.md` và đóng gói `.skill`~~ — **xong 14/9/2026.**
4. Chạy thử quy trình 6 bước trên một kỳ thật, ghi Process Memory.

## Chốt chặn bắt buộc: `ktc-ra-soat-897`

Vòng đời nhiệm vụ kết thúc ở sản phẩm — và **mọi sản phẩm là văn bản đều phải qua `ktc-ra-soat-897` trước
khi trình ký**. Đây là chốt chặn, không phải bước tùy chọn. Còn vấn đề **Mức 1 (bắt buộc sửa)** thì không
được trình.

```
KTC-Ke-Hoach → KTC-Theo-doi-CV → KTC-Bao-Cao → KTC-Ra-Soat-897 → Trình ký / Ban hành
```

Hệ theo dõi **không tự rà soát** và không giữ bản sao bộ quy tắc của 897 — trỏ tới bản gốc.
