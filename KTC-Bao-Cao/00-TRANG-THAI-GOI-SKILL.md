# Trạng thái gói `.skill` của KTC-Bao-Cao

**Cập nhật:** 14/9/2026 (lần 2 — đồng bộ tệp dùng chung)

## Bản hiện hành: `ktc-bao-cao-v3.6.skill`

**v3.6 (14/9/2026)** = v3.5 + đưa **3 tệp dùng chung** về đúng bản gốc ở `01-Chuan-Chung/`:

| Tệp | Trong v3.5 | Trong v3.6 |
|---|---|---|
| `30-Skill-Phan-Loai-6-Truc.md` | 4.515 B — tên Trục 4 cũ, thiếu Trigger conditions | **11.063 B** |
| `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` | 1.218 B | **3.569 B** |
| `00-Metadata-Schema.md` | 1.527 B | **3.018 B** |

Ba tệp này lệch **âm thầm** suốt nhiều đợt đóng gói vì `sao_nguon()` chỉ phủ những tệp được liệt kê tay,
và phép kiểm C5 khi đó chỉ soi bản rời nên luôn báo ✓. Xem `CP-20260914-001`.
Cùng đợt: `ktc-ke-hoach-v3.2.skill` và `ktc-soan-thao-vb.skill` đã đồng bộ ba tệp tương ứng.

**Bổ sung cùng ngày:** gộp nốt 8 tệp lệch nội dung giữa nguồn rời và gói (`CP-20260914-001` mục 7) —
gồm `fill_bc736.py`, `read_bc736_excel.py`, `README-fill_bc736.md`. Nguồn rời và gói **nay trùng khít**.

> **Lưu ý khi đọc v3.6:** mục "Thang điểm chấm công việc" trong `30-Skill-Phan-Loai-6-Truc.md` đã được
> **khôi phục** vào bản gốc sau khi đo trên dữ liệu thật — thang 4 mức (100/120/150/200) là thang đang
> dùng, không phải thang 5 nhóm. Khoảng lệch giữa hai thang: `KI-014`.

## Bản trước đó — giữ lại để hoàn tác

### `ktc-bao-cao-v3.5.skill`

Bản hợp nhất hai nhánh cũ, `KI-005` đóng. **v3.6 kế thừa toàn bộ nội dung này** — phần mô tả dưới đây vẫn đúng với bản đang dùng.

| | Nội dung |
|---|---|
| Nền | `v3.4` — Skill 31 đọc Excel Phụ lục TB736, xác định cấp báo cáo, 6 skill chuyên biệt, `fill_bc736.py` API mới |
| Cộng | Toàn bộ lớp `references/Memory/` (7 tệp + `kiem_tra_bo_nho.py`) và `assets/mau-nhat-ky-chay.md` của nhánh `v2.5.1-memory` |
| Cộng | Sửa quy trình 14/9/2026 — `PATCH-NOTES-v3.5.md` |
| Quy mô | **36 tệp**, 94 KB — là **tập cha** của cả hai nhánh cũ (24 và 31 tệp), kiểm chứng không mất tệp nào |
| Kiểm tra | frontmatter hợp lệ · 0 liên kết gãy · một thư mục gốc duy nhất · Progressive Disclosure 4,3% |

### Ba thay đổi quy trình từ v3.5 — vẫn hiệu lực ở v3.6

1. **Đơn vị nộp HAI tệp** — `.docx` (Phụ lục IIa, nguồn văn phong) và `.xlsx` (Phụ lục IIb/IIc, nguồn số
   liệu). Quy định cũ *"không nhận văn bản tường thuật tự do"* đã khiến bỏ sót toàn bộ tệp `.docx`.
2. **Phụ lục kết quả báo cáo lại kế hoạch công tác của chính Trường**, không gộp mọi nhiệm vụ của mọi đơn
   vị. Cách cũ cho 211 nhiệm vụ so với 39 của bản đã ban hành.
3. **Danh mục mục con là cố định theo mẫu**, không tự sinh từ tên nội hàm TB 817.

## Các gói cũ — đã được thay thế, giữ lại để hoàn tác

| Gói | Trạng thái |
|---|---|
| `ktc-bao-cao-v3.5.skill` | Nền của v3.6. Giữ nguyên vị trí để hoàn tác được. |
| `ktc-bao-cao-v3.4.skill` | Đã gộp vào v3.5. Giữ nguyên vị trí để hoàn tác được. |
| `ktc-bao-cao-v2_5_1-memory.skill` | Đã gộp vào v3.5. Giữ nguyên vị trí để hoàn tác được. |

**Không tự xóa các gói này** — theo quy ước của dự án, tệp trên Drive chỉ do người dùng xóa thủ công. Sau
khi xác nhận v3.6 chạy đúng trên Claude Chat/Cowork, anh có thể xóa các gói cũ.

## Vì sao trước đây có hai nhánh

Hai gói **phân kỳ**, không phải hai phiên bản nối tiếp: `v3.4` tự khai ngày 17/8/2026 nhưng số hiệu cao
hơn; `v2.5.1-memory` tự khai ngày 19/8/2026 — **mới hơn 2 ngày** nhưng số hiệu thấp hơn. Nhánh memory tách
ra từ v2.5.1 trước khi các tính năng nghiệp vụ v3.x hoàn thành, rồi được sửa tiếp sau đó.

Chính nhật ký trong nhánh memory đã ghi *"Còn treo: Gộp v3.1 (QĐ-05)"* — việc hợp nhất được biết mà chưa
làm. Nay đã làm.

> **Bài học giữ lại:** không suy diễn thứ tự phiên bản từ tên tệp. Phải mở tệp đọc dòng tự khai.

## Cảnh báo khi đóng gói lại

**Nguồn rời trong `references/` và nội dung trong `.skill` KHÔNG mặc nhiên đồng bộ.** Đợt 14/9/2026 phát
hiện `33-Skill-Tong-Hop-Bao-Cao-Truong.md` trong gói là **v3.0**, trong khi bản rời chỉ là **v2.3** — ghi đè
thẳng sẽ làm mất mục API `fill_bc736` mới. Đã gộp thay vì ghi đè.

**Quy tắc:** trước khi đóng gói, so từng tệp giữa nguồn rời và gói; tệp nào trong gói mới hơn thì **gộp**,
không ghi đè. Dùng `tools/dong_goi_skill.py` — có sẵn hàm kiểm frontmatter, kiểm liên kết gãy và đối chiếu
danh sách tệp trước/sau.

## Hai tệp "mẫu" trong thư mục này không phải mẫu trống

`00. Phu luc chi tiet ket qua cong tac thang (cap Truong).xlsx` và bản `.xltx` có sheet tên
**`BC Kết quả tháng 7`**, chứa **39 nhiệm vụ thật** kèm tên người chỉ đạo thật. Dùng làm mẫu trống sẽ kéo
dữ liệu tháng 7 vào sản phẩm mới. `.docx` và `.dotx` là **cùng một nội dung**, chỉ khác định dạng lưu —
nhưng bản `.docx` này chứa chú thích hướng dẫn quý giá: danh mục mục con cố định và quy ước văn phong.
