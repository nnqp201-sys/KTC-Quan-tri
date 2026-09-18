# LL-20260914-001 — Một phép kiểm nhìn nhầm chỗ nguy hiểm hơn một phép kiểm hỏng

**Ngày:** 14/9/2026 · **Nguồn:** đợt rà gói `.skill` theo `CP-20260914-001`

## Chuyện đã xảy ra

Phép kiểm C5 in `✓ 30-Skill-Phan-Loai-6-Truc.md — khớp ở mọi hệ` suốt nhiều đợt, trong khi bản nằm trong
`ktc-bao-cao-v3.5.skill` chỉ bằng **một nửa** bản gốc (4.515 / 9.034 byte) và gọi Trục 4 bằng tên cũ.

C5 chạy đúng, không ngoại lệ, không cảnh báo. Nó chỉ so **bản rời** — mà bản rời thì khớp thật. Thứ chạy
trên Chat/Cowork là gói `.skill` thì nó chưa bao giờ mở ra xem.

## Bài học

Một phép kiểm hỏng thì im lặng. Một phép kiểm **nhìn nhầm chỗ** thì in dấu ✓ — nó tạo bằng chứng dương
tính giả, khiến người ta tin tưởng nhiều hơn là khi không có phép kiểm nào.

Khi viết hoặc đọc một phép kiểm, hỏi thêm một câu ngoài "nó có chạy đúng không": **"nó đang soi đúng cái
vật đang chạy thật, hay soi một bản sao của vật đó?"**

Trong dự án này, "vật đang chạy thật" là gói `.skill` — không phải thư mục nguồn rời, không phải
`01-Chuan-Chung/`.

## Dấu hiệu nhận biết sớm

- Một phép kiểm **chưa bao giờ báo đỏ** kể từ khi viết. Không có nghĩa là hệ sạch; nhiều khả năng nó chưa
  từng được thử trên một ca biết chắc là sai.
- Hệ có **hai bản của cùng một thứ** (nguồn rời ↔ gói đóng, bản gốc ↔ bản sao) mà phép kiểm chỉ chạm vào
  một bản.
- Kết luận in `0 LỖI` kèm hàng chục dòng cảnh báo mà không ai bắt buộc phải mở ra xem.

## Cách đã xử lý

Sửa phép kiểm **trước**, sửa dữ liệu **sau** — và lấy *"phép kiểm phải báo đỏ trên dữ liệu hiện tại"* làm
điều kiện nghiệm thu của bước sửa phép kiểm. Nếu sửa xong mà vẫn xanh thì bản sửa chưa ăn.

Kèm ca thử ngược `test_c5_soi_trong_goi.py` dựng một gói giả chứa bản cũ, khẳng định C5 **phải** báo lỗi —
để lần sau C5 có mù lại thì có thứ bắt được.

*Nối tiếp `BH-02` của gói kinh nghiệm KTC-RIS: "lỗi nguy hiểm nhất là lỗi không báo lỗi".*

**Liên quan:** `DL-20260914-002` · `CP-20260914-001` · `02-Regression/Cases/test_c5_soi_trong_goi.py`
