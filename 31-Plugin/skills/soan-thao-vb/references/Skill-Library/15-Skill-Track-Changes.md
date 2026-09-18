# 15 — Skill Track Changes và Nhật ký sửa đổi

**Ban hành:** 13/9/2026 · **Thi hành cho:** `20-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md` NT-2
**Mô-đun:** `29-Cong-Cu/ktc_trackchanges.py` · **Kiểm thử:** `92-Kinh-Nghiem/02-Regression/Cases/test_trackchanges.py`

---

## Điều kiện kích hoạt

Kích hoạt **ngay, không hỏi lại**, khi gặp một trong các dấu hiệu sau:

| Nhóm | Dấu hiệu |
|---|---|
| **Từ khóa trực tiếp** | "track changes", "trackchanges", "theo dõi thay đổi", "bật theo dõi" |
| **Từ khóa nhật ký** | "ghi nhật ký sửa đổi", "nhật ký thay đổi", "bảng kê sửa đổi", "đã sửa những gì" |
| **Bản chất tác vụ** | sửa · chỉnh · góp ý · hoàn thiện · biên tập · tiếp thu · rà lại **một văn bản đã tồn tại** |

**Chỉ được bỏ qua** khi người dùng nói minh thị "không cần track changes". Bỏ qua thì phải ghi lý do đó
lên sản phẩm.

**Điều kiện nền tảng:** mô-đun cần `python-docx` + `lxml` → **chỉ chạy trên Claude Code**. Trên Chat/Cowork
phải nói thẳng là không thi hành được, không mô tả suông rồi giao file sửa trắng.

---

## Quy trình bốn bước

### Bước 1 — Lấy đúng file gốc

Tìm theo thứ tự: file người dùng vừa gửi → `KTC-Database` kho 01–05 → `11-Input/` → thư mục dự án.

**Không tìm được file gốc thì DỪNG và hỏi.** Tuyệt đối không soạn lại từ đầu rồi trình bày như bản sửa —
người dùng mất hoàn toàn khả năng kiểm soát nội dung thay đổi. Đây là vi phạm nặng nhất của NT-2, và có
hàm `doi_chieu_goc()` chuyên để phát hiện nó.

### Bước 2 — Sửa có dấu vết

```python
import sys; sys.path.insert(0, r"D:\.CLAUDE code\KTC-Quan-tri\tools")
from ktc_trackchanges import TrackChanges, kiem_tra, nhat_ky_sua_doi, doi_chieu_goc

tc = TrackChanges("KH-834_goc.docx")          # luôn mở file GỐC
tc.thay("2.000 học sinh", "2.150 học sinh")   # điều chỉnh: del+ins cùng author
tc.xoa_cum("đã tham mưu cho Lãnh đạo Trường ")# bỏ
tc.them_sau("Mục 3", "3.1. Nội dung bổ sung.")# bổ sung
tc.xoa_hang(bang=0, hang=1)                   # bỏ hàng bảng
tc.luu("KH-834_sua_20260913.docx")            # chặn ghi đè file gốc
```

| Hàm | Việc | Author mặc định → màu Word |
|---|---|---|
| `xoa_cum(cụm, tất_cả=False)` | Xóa thuần | `Nội dung bỏ (Claude)` |
| `thay(cũ, mới, tất_cả=False)` | Thay thế — cặp `del`+`ins` **cùng author** | `Nội dung điều chỉnh (Claude)` |
| `them_sau(mốc, text)` | Chèn đoạn mới sau đoạn chứa `mốc` | `Nội dung bổ sung (Claude)` |
| `xoa_hang(bảng, hàng)` | Xóa hàng bảng đúng cơ chế `w:trPr/w:del` | `Nội dung bỏ (Claude)` |

Word tô màu **theo `w:author`**, không ép được mã màu qua XML. Mỗi **đợt sửa có tính chất riêng** thì
truyền author riêng để người đọc phân biệt đợt nào chỉ bằng màu:

```python
tc.thay("23%", "27%", author="Làm sạch số liệu tài chính (Claude)")
```

### Bước 3 — Kiểm tra trước khi giao

```python
kq = kiem_tra("KH-834_sua_20260913.docx")
assert kq["dat"], kq["loi"]
print(doi_chieu_goc("KH-834_goc.docx", "KH-834_sua_20260913.docx"))
```

`kiem_tra()` bắt bảy lỗi, trong đó bốn lỗi đã có tiền lệ thực tế:

1. `<w:del>` không nằm **cuối** `<w:trPr>` → hỏng schema, Word báo lỗi file.
2. Run trong `<w:del>` còn `<w:t>` thay vì `<w:delText>`.
3. Run trong `<w:ins>` lại có `<w:delText>`.
4. `<w:rPr>` lồng trong `<w:rPr>`.
5. Một run chứa cả `<w:t>` và `<w:delText>`.
6. `<w:ins>`/`<w:del>` thiếu `w:id` / `w:author` / `w:date`.
7. Trùng `w:id` (cảnh báo).

`doi_chieu_goc()` là **bộ phát hiện gian lận NT-2**: từ chối hết thay đổi thì phải ra **đúng** bản gốc.
`ty_le_khoi_phuc` < 0,9 → `nghi_soan_lai_tu_dau = True`. Đã kiểm chứng: bản sửa hợp lệ cho **1.0**, bản
soạn lại từ đầu cho **0.333**.

### Bước 4 — Giao kèm nhật ký sửa đổi

```python
open("Nhat-ky-sua-doi.md", "w", encoding="utf-8").write(tc.bao_cao())
```

- `tc.bao_cao()` — nhật ký của **phiên làm việc hiện tại**.
- `nhat_ky_sua_doi(file)` — đọc **bất kỳ** `.docx` có track changes, kể cả file do **người sửa trong Word**.
  Dùng khi người dùng đưa một file đã có vết sửa và hỏi "đã sửa những gì".

Bảng kê gồm: STT · loại (Bỏ / Bổ sung / Điều chỉnh / Bỏ hàng bảng) · vị trí · nội dung cũ · nội dung mới,
kèm dòng tổng theo loại. Hai `<w:del>` + `<w:ins>` liền kề **cùng author** được ghép thành một dòng
"Điều chỉnh" thay vì đếm thành hai thay đổi rời.

---

## Ba điều kỹ thuật dễ mắc lỗi

1. **`paragraph.text` của python-docx bỏ sót nội dung đã đánh dấu.** Nó chỉ đọc `<w:r>` là con trực tiếp;
   run nằm trong `<w:ins>`/`<w:del>` không được tính. Mọi thao tác đọc lại file có track changes phải dùng
   `_text_day_du(el, chap_nhan)` của mô-đun, không dùng `.text`.
2. **Thứ tự phần tử trong `<w:trPr>`**: `<w:del>` phải là phần tử cuối cùng, sau `<w:trHeight>` nếu có.
3. **Xóa hàng bảng cần hai việc**: đánh dấu ở `<w:trPr>` **và** bọc toàn bộ run trong hàng bằng `<w:del>`.
   Thiếu việc thứ hai thì hàng không hiện gạch ngang khi xem trước.

---

## Liên quan

- `14-Nguyen-Tac-Soan-Thao-Bat-Bien.md` — NT-2 (nguyên tắc gốc)
- `KTC-Ra-Soat-897-v2-Cai-tien/references/Skill-Library/Bo-Sung-Chuan-Hoa-TrackChanges-MauChu-PhienBanSkill_20260825.md`
  — chuẩn kỹ thuật gốc do hệ 897 đúc kết 25/8/2026; mô-đun này là bản **thi hành** của chuẩn đó
- `92-Kinh-Nghiem/05-Known-Issues/Pending.md` — `KI-009` (đã đóng bằng mô-đun này)
