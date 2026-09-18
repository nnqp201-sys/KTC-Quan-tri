# CP-20260914-001 — Phương án đóng khoảng lệch giữa gói `.skill` và bản chuẩn

**Ngày lập:** 14/9/2026 · **Trạng thái:** ✅ **ĐÃ THỰC HIỆN** cùng ngày — xem mục 6 ·
**Tiếp nối:** `CP-20260913-001` ĐX-1
**Phạm vi kiểm tra:** 5 gói `.skill` đang có × toàn bộ nguồn rời × `01-Chuan-Chung/`

---

## 1. Kết quả kiểm tra — bốn phát hiện

### PH-1 (Chặn) — Phép kiểm C5 báo "sạch" trong khi hệ đang lệch

`tools/kiem_tra_he_thong.py` phép kiểm **C5** in ra:

```
✓ 30-Skill-Phan-Loai-6-Truc.md    khớp ở mọi hệ
✓ 00-Metadata-Schema.md           khớp ở mọi hệ
✓ 04-Nguyen-Tac-Nap-Van-Ban...    khớp ở mọi hệ
```

**Cả ba dòng đều sai.** Đối chiếu trực tiếp bằng md5:

| Tệp dùng chung | `01-Chuan-Chung` (gốc) | Trong `ktc-bao-cao-v3.5.skill` | Trong `ktc-ke-hoach-v3.1.skill` |
|---|---|---|---|
| `30-Skill-Phan-Loai-6-Truc.md` | 9.034 B | **4.515 B — LỆCH** | **6.823 B — LỆCH** |
| `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` | 3.569 B | **1.218 B — LỆCH** | **2.138 B — LỆCH** |
| `00-Metadata-Schema.md` | 3.018 B | **1.527 B — LỆCH** | **2.906 B — LỆCH** |
| `00-Nguyen-Tac-Chung.md` | 7.469 B | 7.469 B — khớp | 7.469 B — khớp |
| `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` | 4.338 B | *(không có trong gói)* | *(không có trong gói)* |

**Nguyên nhân — không phải lỗi mã, mà là lệch phạm vi.** Đọc `c5_tep_dung_chung()` (dòng 211–231):
hàm chỉ so `01-Chuan-Chung/<tệp>` với `<hệ>/references/Skill-Library/<tệp>` — tức là **chỉ so bản rời**.
Nó không mở tệp `.skill` bao giờ. Bản rời thì đúng là khớp 100% ở mọi hệ. Nhưng **bản rời không phải thứ
chạy trên Claude Chat/Cowork** — gói `.skill` mới là.

Đây đúng loại lỗi mà chính dự án đã cảnh báo: *"Một phép kiểm hỏng luôn báo sạch."* C5 không hỏng, C5
**nhìn nhầm chỗ** — hệ quả giống hệt, mà còn nguy hiểm hơn vì nó in dấu ✓.

### PH-2 (Chặn) — Hệ quả nghiệp vụ: gói đang chạy phân loại theo tên Trục 4 cũ

Không phải lệch số byte vô hại. So mục lục hai bản `30-Skill-Phan-Loai-6-Truc.md`:

| | Trục 4 gọi là |
|---|---|
| Bản chuẩn `01-Chuan-Chung` (56 dòng) | "Xây dựng Đảng và hệ thống chính trị trong sạch, vững mạnh; **giữ gìn đoàn kết, thống nhất**" |
| Bản trong `ktc-bao-cao-v3.5.skill` (43 dòng) | "Xây dựng Đảng và hệ thống chính trị trong sạch, vững mạnh; **phòng, chống tham nhũng**" |

Bản trong gói còn thiếu hẳn 4 mục: `Trigger conditions` · `Cách áp dụng khi soạn Kế hoạch/Báo cáo công
tác` · `Severity categories (khi rà soát)` · `Related`; và giữ một mục đã bị bỏ: `Thang điểm chấm công
việc (theo KH tháng thực tế)`.

> **Đính chính 14/9/2026 (mục 6, GĐ2):** nhận định "thang điểm này thuộc bản dự thảo lần 4" là **SAI**.
> Đo trên dữ liệu thật cho thấy đây là thang **đang dùng** ở mọi cấp. Đã khôi phục vào bản gốc; xem `KI-014`.

**Nối thẳng với `KI-011`** (danh mục nhiệm vụ chuẩn lệch tên Trục/Nội hàm với TB 817). KI-011 mới ghi nhận
lệch giữa *tệp Excel danh mục* và *TB 817*. Nay xác định thêm: **chính gói skill đang chạy cũng dùng tên
Trục 4 cũ**. Tức là lệch ở ba nơi, không phải hai.

### PH-3 (Cao) — 10 tệp tri thức của `ktc-quan-tri.skill` chỉ tồn tại bên trong tệp zip

Dự án **không có thư mục `references/` ở gốc**. Gói cấp dự án `ktc-quan-tri.skill` chứa 15 tệp tham chiếu;
đối chiếu md5 với `01-Chuan-Chung/`:

| Trạng thái | Số tệp | Danh sách |
|---|---|---|
| Trùng khớp bản gốc ở `01-Chuan-Chung` | 4 | `11-Skill-Phan-Loai-6-Truc` · `12-Bang-Ma-Don-Vi` · `20-Tu-Dien-Truong-Du-Lieu` · `21-Quy-Tac-Task-ID` · `22-Vong-Doi-Va-Canh-Bao` |
| **Không có bản sao ở bất kỳ đâu ngoài zip** | **10** | `01-Nguyen-Tac-Chung` · `02-Chi-Muc-KTC-Database` · `10-Sau-Truc-38-Noi-Ham` · `13-Danh-Muc-Nhiem-Vu-Va-San-Pham` · `23-Doi-Chieu-Ba-He` · `24-Chot-Ky-Va-Bao-Cao` · `30-KPI-Va-Xep-Loai` · `40-Process-Memory` · `41-Gioi-Han-Nen-Tang` · `README` |

Mười tệp này là **nội dung nghiệp vụ thật**, tổng khoảng 490 dòng: quy tắc đối chiếu ba hệ, quy trình chốt
kỳ, quy đổi KPI và xếp loại theo QĐ 1923, giới hạn theo nền tảng. Không phải bản sao của gì cả.

Điều này mâu thuẫn với quy tắc của chính dự án — *"`01-Chuan-Chung/` giữ bản gốc, các hệ giữ bản sao"*.
Ở đây **bản gốc nằm trong zip**. Hệ quả: muốn sửa một quy tắc thì phải giải nén, sửa, đóng lại; và nếu tệp
`.skill` hỏng hoặc mất trên Drive thì mất luôn phần tri thức đó — không có nơi nào chép lại được.

*Lưu ý phân biệt:* `SKILL.md` trong gói **khớp 100%** với `SKILL.md` ở gốc dự án — chỗ đó đúng quy ước.
Riêng `00-README.md` thì lệch (gói 3.514 B / gốc dự án 5.143 B), cần xác định bản nào đúng.

### PH-4 (Trung bình) — Kết luận "0 LỖI" che 73 cảnh báo, trong đó có việc chặn

Phép kiểm **C4** *có* so gói với nguồn rời và *có* phát hiện 25 tệp lệch ở `ktc-bao-cao`, 11 ở
`ktc-ke-hoach`. Nhưng kết quả xếp vào `canh_bao`, nên dòng kết luận in:

```
KẾT LUẬN: 0 LỖI · 73 cảnh báo        (mã thoát 0)
```

Mã thoát 0 nghĩa là "được phép đóng gói tiếp". Một việc đang chặn nằm lẫn trong 73 dòng cảnh báo mà người
chạy không bắt buộc phải mở ra xem (`--chi-tiet` là tùy chọn).

### Một tin tốt — hai chỗ không có vấn đề

- `ktc-soan-thao-vb.skill`: **90/90 tệp khớp tuyệt đối** với nguồn rời. Đây là hệ duy nhất sạch hoàn toàn,
  và là bằng chứng quy trình đóng gói *có thể* chạy đúng — nên lấy làm mẫu.
- `ktc-ke-hoach.skill` (bản cũ 12/8) so với `ktc-ke-hoach-v3.1.skill`: v3.1 là **tập cha đúng nghĩa** —
  không tệp nào chỉ có ở bản cũ, 4 tệp lệch đều theo hướng v3.1 đầy đủ hơn. **Không lặp lại tình trạng
  phân kỳ của `KI-005`.** Bản cũ chỉ cần xếp lưu trữ.

---

## 2. Vì sao lệch — cơ chế, không phải sự cẩu thả

Đọc `tools/dong_goi_skill.py` thì rõ: quy trình đóng gói **không phải** "gom thư mục nguồn rời rồi nén".
Nó là:

```
giai_nen(gói cũ → thư mục tạm)
   → sao_nguon(chép MỘT DANH SÁCH TỆP ĐƯỢC LIỆT KÊ TAY từ nguồn rời vào)
      → dong_goi(nén lại)
```

Nghĩa là **gói cũ là nền, nguồn rời chỉ phủ lên những tệp được gọi tên**. Tệp nào không nằm trong danh sách
`tep` truyền vào `sao_nguon()` thì giữ nguyên bản cũ trong gói — vĩnh viễn, qua mọi lần đóng gói.

Đây là thiết kế **có lý do đúng** (nó bảo vệ lớp `Memory/` và các tệp chỉ có trong gói khỏi bị xóa), nhưng
thiếu một nửa: không có bước nào rà xem *có tệp nào đáng lẽ phải được phủ mà bị bỏ quên không*. Ba tệp
dùng chung ở PH-1 rơi đúng vào khe đó.

> Điều chỉnh lại nhận định của `CP-20260913-001` ĐX-1: đóng gói lại **không** làm mất lớp `Memory/` — công
> cụ giải nén gói cũ ra trước nên `Memory/` an toàn. Rủi ro thật là **ngược lại**: bản sửa ở nguồn rời
> không bao giờ vào được gói nếu không được liệt kê tay.

---

## 3. Phương án — ba giai đoạn

### Giai đoạn 1 — Sửa phép kiểm trước, sửa dữ liệu sau (nửa ngày)

Làm theo thứ tự này, không đảo: nếu sửa dữ liệu trước thì không có gì chứng minh đã sửa đúng.

**1.1. Mở rộng C5 để soi vào trong gói.** Đổi `c5_tep_dung_chung()` thành so bản gốc `01-Chuan-Chung` với
**cả hai** nơi: bản rời và bản nằm trong `.skill`. Lệch ở bản rời → cảnh báo (còn kịp sửa trước khi đóng
gói). Lệch ở trong gói → **LỖI**, vì đó là thứ đang chạy thật.

**1.2. Nâng C4 từ cảnh báo thành lỗi ở đúng một trường hợp:** tệp dùng chung trong gói khác bản gốc. Các
trường hợp lệch khác (tệp chỉ có trong gói, tệp gói mới hơn) **giữ nguyên mức cảnh báo** — chúng là hành vi
bình thường của cơ chế ở mục 2, biến chúng thành lỗi sẽ khiến phép kiểm luôn đỏ và mất tác dụng.

**1.3. Đổi dòng kết luận** để cảnh báo không bị chôn: in riêng số cảnh báo **thuộc nhóm chặn đóng gói**.

**1.4. Ca thử ngược bắt buộc** — `99-Kinh-Nghiem/02-Regression/Cases/test_c5_soi_trong_goi.py`: dựng một
gói giả chứa bản cũ của một tệp dùng chung, khẳng định C5 **phải** báo lỗi. Không có ca này thì lần sau C5
lại mù mà không ai biết. *(Theo quy tắc: thêm phép kiểm mới thì thêm ca thử ngược trong cùng lần sửa.)*

### Giai đoạn 2 — Đóng khoảng lệch dữ liệu (nửa ngày)

**2.1.** Bổ sung 3 tệp dùng chung vào danh sách `sao_nguon()` của cả `ktc-bao-cao` và `ktc-ke-hoach`, đóng
gói lại. Chạy `kiem_tra_he_thong.py` trước và sau — C5 phải chuyển từ ✓-giả sang ✗ rồi về ✓-thật.

**2.2.** Trước khi đóng gói, **đọc lại mục "Thang điểm chấm công việc"** trong bản cũ của
`30-Skill-Phan-Loai-6-Truc.md`. Bản chuẩn đã bỏ mục này. Cần xác nhận đây là chủ ý (thang điểm thuộc dự
thảo lần 4, không phải bản ban hành — đúng như `Trạng thái đang mở` đã ghi) chứ không phải rơi rớt khi biên
tập. **Không tự quyết định** — nếu là rơi rớt thì phải phục hồi vào bản gốc chứ không phải giữ trong gói.

**2.3.** Đưa `ktc-ke-hoach.skill` (bản 12/8/2026) vào `99-Luu-Tru/`, ghi một dòng lý do. Đã kiểm chứng v3.1
là tập cha nên không mất gì. *(Không xóa — theo quy ước, tệp trên Drive chỉ do người dùng xóa thủ công.)*

### Giai đoạn 3 — Đưa 10 tệp gốc của `ktc-quan-tri` ra khỏi zip (một ngày)

**3.1.** Giải nén `ktc-quan-tri.skill`, đặt 10 tệp không có bản sao vào **`01-Chuan-Chung/`** — đúng vai trò
"nơi giữ bản gốc" mà `CLAUDE.md` đã quy định. Giữ nguyên nội dung, chỉ đặt lại tên theo quy ước đánh số
hiện hành của thư mục đó.

**3.2.** Bốn tệp đã trùng khớp bản gốc thì **không chép ra** — chúng đã có nguồn, chỉ cần ghi vào bảng ánh
xạ "tên trong gói ↔ tên bản gốc" để lần đóng gói sau chép đúng chỗ.

**3.3.** Làm rõ `00-README.md`: bản trong gói 3.514 B, bản ở gốc dự án 5.143 B. Xác định bản nào là chuẩn,
rồi đồng bộ một chiều.

**3.4.** Bổ sung phép kiểm **C11 — "không có tệp gốc nào chỉ tồn tại trong zip"**: quét mọi `.skill`, mọi
tệp không tìm được bản sao ngoài zip thì cảnh báo. Kèm ca thử ngược.

---

## 4. Thứ tự và điều kiện dừng

```
GĐ1  sửa C5 + C4 + ca thử ngược   ──►  C5 phải BÁO ĐỎ trên dữ liệu hiện tại
                                        (nếu vẫn xanh thì bản sửa chưa ăn — dừng, sửa tiếp)
        │
GĐ2  bổ sung 3 tệp, đóng gói lại  ──►  C5 xanh THẬT · C4 còn cảnh báo là bình thường
        │
GĐ3  đưa 10 tệp ra 01-Chuan-Chung ──►  C11 xanh
```

**Điều kiện dừng của GĐ1** cố ý là *phép kiểm phải báo đỏ*. Một bản sửa phép kiểm mà chạy xong vẫn xanh
trên dữ liệu đã biết là sai thì bản sửa đó vô dụng — đây chính là bài học `BH-02` của gói kinh nghiệm cũ:
*lỗi nguy hiểm nhất là lỗi không báo lỗi*.

## 5. Việc không làm trong đợt này

- **Không sửa nội dung nghiệp vụ của 3 tệp dùng chung.** Đợt này chỉ đồng bộ bản đã có ở `01-Chuan-Chung`
  xuống gói. Việc rà tên Trục 4 cho khớp TB 817 thuộc `KI-011`, làm riêng, có đối chiếu văn bản gốc.
- **Không gộp hay xóa gói `.skill` nào ngoài việc lưu trữ bản `ktc-ke-hoach` cũ.**
- **Không đụng `ktc-soan-thao-vb.skill`** — đang sạch, chỉ dùng làm mẫu đối chiếu.
- **Không chạy `test_regression_v34.py` trên dữ liệu thật trong đợt này** — việc đó ở `CP-20260913-001`
  ĐX-4, phụ thuộc gói đã đồng bộ xong.

---

**Liên quan:** `CP-20260913-001` (ĐX-1 được điều chỉnh tại mục 2) · `KI-011` · `KI-013` · `KI-005` (đã đóng)
· `tools/kiem_tra_he_thong.py` C4/C5 · `tools/dong_goi_skill.py`

---

# 6. Kết quả thực hiện — 14/9/2026

**Trạng thái: ĐÃ THỰC HIỆN cả ba giai đoạn.** Ghi lại đúng những gì đã làm và những gì phát sinh.

## GĐ1 — sửa phép kiểm trước

- `c5_tep_dung_chung()` nay soi **cả bản rời lẫn bản nằm trong `.skill`**; lệch trong gói → **LỖI**,
  lệch bản rời → cảnh báo. Vắng mặt ở cả hai nơi = hệ đó không dùng tệp, bỏ qua, không bịa lỗi.
- C4 **giữ nguyên** mức cảnh báo, đúng như đề xuất — quy tắc tệp dùng chung do C5 sở hữu.
- Dòng kết luận in thêm **phân bố cảnh báo theo phép kiểm**.
- Ca thử ngược `test_c5_soi_trong_goi.py` — 5 ca, đạt 5/5.
- **Điều kiện dừng đạt:** chạy trên dữ liệu thật, C5 báo **6 LỖI**, mã thoát 1.

## GĐ2 — đóng khoảng lệch dữ liệu

| Gói | Trước | Sau |
|---|---|---|
| `ktc-bao-cao` | v3.5 | **v3.6** — 3 tệp dùng chung về bản gốc |
| `ktc-ke-hoach` | v3.1 | **v3.2** — 3 tệp dùng chung về bản gốc |
| `ktc-soan-thao-vb` | — | đóng lại, đồng bộ `30-Skill-Phan-Loai-6-Truc.md` |

**Phát sinh 1 — `ktc-soan-thao-vb` cũng mang tệp dùng chung.** Đợt kiểm ban đầu không thấy vì hệ này
đang khớp 100%; chỉ sau khi bản gốc đổi, C5 mới báo. Chính phép kiểm mới phát hiện, không phải con người.

**Phát sinh 2 — mục 2.2 cho kết quả ngược với dự đoán.** "Thang điểm chấm công việc" **không** phải rơi
rớt từ dự thảo. Đếm trên dữ liệu thật: 800 dòng của 27 tệp đơn vị, phụ lục cấp Trường 39 nhiệm vụ, và Kế
hoạch Quý III đã duyệt — **chỉ xuất hiện thang 4 mức** (100/120/150/200, hệ số 1 · 1,2 · 1,5 · 2). Thang
5 nhóm của `CLAUDE.md` không có dòng nào trong dữ liệu vận hành. Đã **khôi phục** mục này vào bản gốc kèm
bảng bằng chứng và ghi chú phân định phạm vi; khoảng lệch hai thang mở thành **`KI-014`**.

## GĐ3 — đưa bản gốc ra khỏi zip

Chọn phương án **`references/` ở gốc dự án** — giống hệt cách 4 hệ con làm, không phải đổi tên tệp nào,
và `dong_goi_skill.py` cùng C4/C5/C11 áp dụng đồng nhất cho cả 5 gói.

- Tách **15 tệp** của `ktc-quan-tri.skill` ra `references/`; tách tiếp **14 tệp** của `ktc-bao-cao`
  (toàn bộ lớp `Memory/`, `assets/`, 2 PATCH-NOTES, 3 tệp kiểm thử) và **1 tệp** của `ktc-ke-hoach`.
- Thêm **C11** — "không tệp nào chỉ tồn tại bên trong gói", kèm ca thử ngược
  `test_c11_ban_goc_trong_zip.py` (5 ca, đạt 5/5).
- Thêm `ktc-quan-tri` vào phạm vi kiểm; mở rộng `CHUNG` thêm 4 tệp và thêm bảng `DOI_TEN` để C5 kiểm được
  **bản sao bị đổi tên** trong gói cấp dự án (`30-Skill-Phan-Loai-6-Truc.md` → `11-Skill-...`, v.v.).

**Phát sinh 3 — hai lỗi thật ở gói cấp dự án, lộ ra ngay khi đưa nó vào phạm vi kiểm:**

1. **Định tuyến gãy.** `SKILL.md` và README của gói trỏ tới `ktc-dis-tong-hop-vb` — hệ đã thay bằng
   `ktc-soan-thao-vb`. Nằm cả trong **frontmatter description**, tức là phần dùng để định tuyến. Đã sửa 4 chỗ.
2. **Hai tệp `00-README.md` khác nhau trùng tên** — một là README của dự án (4.070 B), một là README của
   gói skill (2.771 B). Đã tách thành `00-README-ktc-quan-tri.md`.
3. `references/01-Nguyen-Tac-Chung.md` trong gói là **bản cũ** của `01-Chuan-Chung/00-Nguyen-Tac-Chung.md`,
   lệch đúng một dòng và còn giữ tên hệ đã bỏ "KTC-Van-Ban". Đã thay bằng bản gốc.

## Kết quả đo được

| | Trước | Sau |
|---|---|---|
| Lỗi | 0 *(dương tính giả)* | **0 (thật)** |
| Cảnh báo | 73 | **38** |
| C11 — tệp chỉ có trong zip | 30 | **0** |
| C3 — đường dẫn không tìm thấy | 22 | **8** |
| C4 — lệch nguồn rời ↔ gói | 36 | **15** |
| Ca hồi quy | 2 | **4**, đạt 4/4 |
| Phép kiểm | 10 | **11** |

15 cảnh báo C4 còn lại là **lệch nội dung nghiệp vụ từng tệp** (mỗi tệp phải xét bên nào mới hơn) — đúng
phạm vi đã loại trừ ở mục 5, để đợt sau.

**Liên quan:** `DL-20260914-002` · `LL-20260914-001` · `KI-014` (mới) · `KI-013` (đã đóng)

---

# 7. Đợt bổ sung — gộp 15 tệp lệch nội dung (C4 → 0)

Mục 5 đã loại 15 cảnh báo C4 ra khỏi phạm vi vì "mỗi tệp phải xét bên nào mới hơn". Nay đã xét xong.

## Cách xét — không suy từ kích thước

Đọc dòng tự khai phiên bản/ngày của **cả hai bản**, rồi so nội dung thật. Kết quả xác nhận lại `BH-01`
của gói kinh nghiệm cũ: **kích thước không cho biết bản nào mới hơn**. Hai tệp `ktc-ke-hoach` có bản rời
*lớn hơn* nhưng lại là bản **cũ** — bản trong gói ngắn hơn vì được viết lại gọn, đồng thời bổ sung
Pre-flight (Skill 34), thư mục `KH-Cap-Tren/` và bước "DỪNG khi thiếu KH cấp trên".

Mười lăm tệp đều tự khai **cùng một phiên bản** ở hai bên, nên số hiệu cũng vô dụng — chỉ nội dung nói được.

## Phán quyết từng tệp

**Lấy bản trong GÓI (11 tệp)** — gói mang bản vá mà nguồn rời chưa có:

| Tệp | Vì sao gói mới hơn |
|---|---|
| `fill_bc736.py` | Gói có 23 dòng riêng, rời có 0 — tập cha. Thêm kiểm cấu trúc `content_by_phase` và cảnh báo tên Phần sai (v3.4, XUNG ĐỘT 1 và 5) |
| `read_bc736_excel.py` | `build_content_map_skeleton()` của gói trả đúng cấu trúc 3 tầng và **đưa nhiệm vụ Mục II vào khung nháp** — bản rời bỏ quên hoàn toàn (chính là BUG-15) |
| `README-fill_bc736.md` | Gói là v3.2 (19/8), mô tả API mới `content_by_phase` và **45 vị trí thật**; rời còn là 18/8 với API `content_map` cũ — mâu thuẫn với chính script |
| `PATCH-NOTES-v3.4.md` | Gói thêm một câu kết |
| `00-README.md` (KH) | Gói là v3.0: liệt kê đủ 8 Skill + 4 Prompt, quy trình 7 bước, cấu trúc thư mục Drive |
| 3 Prompt `16-Tong-Hop-Ke-Hoach/` | Gói thêm nhãn `[CẦN BỔ SUNG]`, `[CẦN XÁC ĐỊNH ĐƠN VỊ CHỦ TRÌ]` và mục "Điều kiện tiên quyết → DỪNG" |
| `34-Skill-Nhan-Ke-Hoach-Preflight.md` | Gói 8.720 B so với rời 5.507 B, cùng khai v2.0 — gói là bản khai triển đầy đủ |
| `35-Skill-Thu-Thap-De-Xuat-Don-Vi.md` | Gói tham chiếu Pre-flight (Skill 34) và thêm bước 5 |
| `37-Skill-Doi-Chieu-Phan-Cap-Thoi-Gian.md` | Gói yêu cầu KH cấp trên nằm trong `KH-Cap-Tren/` và DỪNG nếu thiếu |

**Giữ bản RỜI (2 tệp)** — gói bị lược mất nội dung:

- `34-Skill-Doi-Chieu-Tien-Do-KH.md` — rời là tập cha, gói không có dòng nào riêng.
- `04-Thu-Thap-Checklist.md` — gói viết gọn lại nhưng **đánh rơi bước "liệt kê file gốc cần xóa trong
  `11-Input`/`13-Unit-Reports`"** ở Tác vụ D. Đó là Bước 7 của quy trình, không phải chữ thừa.

**Gộp hai bên (2 tệp)** — mỗi bên đúng một phần:

- `31-Skill-Phu-Luc-TB736-Excel.md` — lấy tiêu đề của rời (*"Cập nhật 18/08/2026 — đối chiếu file thật"*,
  mới hơn 17/08 của gói) **+** dòng của gói (*"45 vị trí thật"*, đúng với `README-fill_bc736.md` v3.2;
  dòng "22 khóa" của rời đã lỗi thời).
- `read_bc736_excel.py` — lấy bản gói, **+** sửa docstring theo bản rời: gói trả về `muc_ii_items` trong
  mã nhưng docstring không liệt kê nó; bản rời liệt kê đúng.

## Kết quả

| | Đầu phiên | Sau GĐ1-3 | Sau đợt gộp |
|---|---|---|---|
| Lỗi | 0 *(dương tính giả)* | 0 | **0** |
| Cảnh báo | 73 | 38 | **23** |
| C4 — lệch nguồn rời ↔ gói | 36 | 15 | **0** |
| C11 — tệp chỉ có trong zip | 30 | 0 | **0** |

**Cả 4 gói nay đồng bộ hoàn toàn với nguồn rời.** Từ giờ sửa nguồn rời rồi đóng gói lại là thao tác an
toàn — đúng như quy ước của dự án vẫn mô tả, nhưng trước đợt này chưa đúng trên thực tế.

23 cảnh báo còn lại: **C3 = 8** (đường dẫn viết tương đối theo gốc hệ 897 nằm ngoài dự án, và hai tên tệp
rút gọn bằng `...` trong `00-README.md` — phép kiểm quá ngây thơ chứ tài liệu không sai) và **C8 = 15**
(bản sao chéo giữa `ktc-soan-thao-vb` và `ktc-ra-soat-897` — vấn đề kiến trúc riêng, đã có ghi nhận).

Bản gói trước khi gộp lưu tại `99-Luu-Tru/*_20260914_truoc-gop-C4.skill`.
