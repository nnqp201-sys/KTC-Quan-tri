# DL-20260914-001 — Vai trò của `KTC-DIS-Tong-Hop-VB`: giữ hay bỏ?

**Ngày:** 14/9/2026 · **Câu hỏi:** hệ này còn cần không, hay điều chỉnh thành `KTC-Soan-Thao-VB`?
**Trạng thái:** ✅ **ĐÃ THỰC HIỆN 14/9/2026** — người phụ trách hệ đồng ý, làm trong `KTC-Quan-tri/`.

**Kết quả:** hệ mới `KTC-Soan-Thao-VB/` — **90 tệp** (hệ cũ 122), gói `ktc-soan-thao-vb.skill` 120 KB,
frontmatter hợp lệ · 0 liên kết gãy · 46/46 đường dẫn trong `SKILL.md` đều tồn tại. Bốn workflow chung chung
đã viết lại có căn cứ. Hệ cũ **giữ nguyên**, 32 tệp cần dọn thủ công — danh mục ở
`12-Output/2026-09-14/Danh-muc-can-don-KTC-DIS-Tong-Hop-VB.md`.

## Trả lời ngắn

**Cần giữ, nhưng phải đổi vai và thu hẹp.** Nửa "rà soát" của nó đã lạc hậu và kém hơn hẳn
`KTC-Ra-Soat-897`; nửa "soạn thảo" thì **không hệ nào khác có**. Đổi tên thành `KTC-Soan-Thao-VB` đúng với
giá trị thật còn lại.

## Số liệu khảo sát

Đối chiếu md5 toàn bộ `references/` của 5 hệ:

| Hệ | Số tệp |
|---|---|
| KTC-DIS-Tong-Hop-VB | **76** |
| KTC-Ra-Soat-897 | 44 |
| KTC-Bao-Cao | 29 |
| KTC-Ke-Hoach | 19 |
| KTC-Database | 11 |

| Phép đo trên 76 tệp của Tổng-hợp-VB | Kết quả |
|---|---|
| Trùng **tên** với hệ khác | 34 |
| Trùng **md5** (giống y hệt) | **chỉ 8** |
| → Trùng tên nhưng **khác nội dung** | **26** — lệch âm thầm |
| Riêng có | 42 |

## Phát hiện quyết định: nửa rà soát đã lạc hậu toàn diện

31 tệp trùng tên với `KTC-Ra-Soat-897`, trong đó 28 khác nội dung. **Cả 28/28 đều là 897 mới hơn** — không
một ngoại lệ. Tổng-hợp-VB dừng ở **10/8/2026**, 897 đã đi tiếp tới 9–13/9/2026.

Chênh lệch không phải vài dòng mà là **một bên chỉ có tiêu đề**:

| Tệp checklist | Tổng-hợp-VB | RaSoat897 | Tỷ lệ |
|---|---|---|---|
| `03-Phap-Ly.md` | **357 b** | 10.513 b | 29× |
| `02-Noi-Dung.md` | **328 b** | 8.584 b | 26× |
| `01-The-Thuc.md` | **375 b** | 7.076 b | 19× |
| `04-Ngon-Ngu.md` | **314 b** | 6.210 b | 20× |
| `05-Hinh-Thuc.md` | **319 b** | 4.777 b | 15× |
| `28-Skill-Bao-Cao-Ra-Soat-Chuan.md` | 14.799 b | 22.549 b | 1,5× |

Bảy tệp checklist ở Tổng-hợp-VB chỉ là **khung rỗng**, không dùng rà soát thật được.

### Đây là rủi ro đang hoạt động, không chỉ là dư thừa

`SKILL.md` của hệ này tự khai là *"hệ tổng hợp, đầy đủ nhất trong họ 5 hệ"* và hướng dẫn:
*"chưa rõ nên dùng hệ nào → dùng hệ này"*.

Nghĩa là **người dùng phân vân sẽ bị đẩy tới bộ quy tắc rà soát cũ nhất và sơ sài nhất**. Tuyên bố "đầy đủ
nhất" đúng về **số lượng tệp** (76 so với 44) nhưng sai về **chất lượng**.

## Phần chỉ hệ này có — và chất lượng thật của nó

| Nhóm | Số tệp | Dung lượng | Đánh giá |
|---|---|---|---|
| **A. Soạn thảo (lõi)** — phân tích yêu cầu, soạn thảo, chuẩn hóa, tổng hợp nội dung, đề xuất quy trình trình ký | 5 | 8 KB | **Thực chất, không hệ nào khác có** |
| **B. Soạn theo loại văn bản** — Quyết định · Kế hoạch · Thông báo · Báo cáo · Tờ trình · Công văn · Biên bản · VB cấp Phòng · VB đối ngoại | 9 | 12 KB | **Thực chất** |
| **C. Nghiệp vụ chuyên ngành** — Đào tạo · Tuyển sinh · Cán bộ · Tài chính · ĐBCL · HSSV | 6 | 8 KB | **Thực chất** |
| **F. Prompt soạn thảo** theo 7 loại văn bản | 7 | 9 KB | **Thực chất** |
| **E. Knowledge-Graph** — Entities · Relations · Rules · Mappings · Use-Cases | 6 | 13 KB | Thực chất; riêng `06-Metadata.md` = 187 b, sơ sài |
| **D. Vòng đời văn bản** — Soạn thảo → Rà soát → Trình ký → Ban hành → Lưu trữ → Cập nhật | 6 | 6 KB | **4/6 là khung rỗng**: Trình ký 454 b · Ban hành 356 b · Lưu trữ 375 b · Cập nhật 432 b |

Tổng phần có giá trị thật: khoảng **33 tệp, 50 KB**. Đây là **năng lực soạn thảo**, không phải năng lực
tổng hợp — và đúng là chỗ trống trong họ 5 hệ: `ktc-ke-hoach` chỉ dựng kế hoạch, `ktc-bao-cao` chỉ dựng báo
cáo, `ktc-ra-soat-897` chỉ rà soát, `ktc-database` chỉ quản kho. **Không hệ nào soạn Quyết định, Tờ trình,
Công văn, Biên bản.**

## Đề xuất: đổi vai thành `KTC-Soan-Thao-VB`

### Giữ lại
Nhóm A · B · C · F · E — toàn bộ năng lực soạn thảo và nghiệp vụ chuyên ngành.

### Bỏ, trỏ sang `KTC-Ra-Soat-897`
- `references/Checklist/` — 7 tệp khung rỗng
- `references/Prompt-Library/02-Ra-Soat/` — 7 tệp
- `00-Prompt-Chinh-Thuc-Ra-Soat-897.md` và bản `-full` — 897 giữ bản chuẩn
- `Skill-Library` 02 · 03 · 14 · 15 · 17 · 18 · 19 · 28 · 29 — các skill kiểm tra thể thức, căn cứ, logic,
  thẩm quyền, tính thống nhất, chất lượng, báo cáo rà soát, văn bản Đảng

Quy mô sau khi thu hẹp: **76 → khoảng 45 tệp**.

### Sửa `SKILL.md`
Bỏ tuyên bố *"đầy đủ nhất"* và *"chưa rõ dùng hệ nào thì dùng hệ này"*. Thay bằng vai trò dứt khoát:

> Soạn thảo văn bản hành chính mới theo loại văn bản và lĩnh vực nghiệp vụ.
> Rà soát trước khi trình ký → chuyển sang `ktc-ra-soat-897`.
> Dựng kế hoạch công tác → `ktc-ke-hoach`. Dựng báo cáo công tác → `ktc-bao-cao`.

### Đồng bộ 5 tệp dùng chung
`00-Nguyen-Tac-Chung.md`, `00-Metadata-Schema.md`, `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md`,
`30-Skill-Phan-Loai-6-Truc.md`, `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` — lấy bản gốc từ
`01-Chuan-Chung/`, hiện đang lệch khoảng một tháng.

### Hoàn thiện phần còn dở
Bốn workflow khung rỗng (Trình ký · Ban hành · Lưu trữ · Cập nhật) và `Knowledge-Graph/06-Metadata.md`.

## Vì sao không chọn hai phương án kia

| Phương án | Vì sao loại |
|---|---|
| **Bỏ hẳn hệ** | Mất năng lực soạn thảo 7 loại văn bản + 6 lĩnh vực nghiệp vụ mà không hệ nào thay được. Đây là chỗ trống thật của họ 5 hệ. |
| **Giữ nguyên "hệ tổng hợp làm mọi việc"** | Đã chứng minh không giữ được: chỉ sau một tháng, 28/28 tệp rà soát tụt lại sau 897. Một hệ sao chép quy tắc của hệ khác thì **chắc chắn sẽ lệch** — vấn đề chỉ là bao lâu. |

## Bài học chung cho cả họ skill KTC

**Không hệ nào được sao chép bộ quy tắc của hệ khác để "cho đầy đủ".** Bản sao không có cơ chế đồng bộ sẽ
lệch, và bản lệch nguy hiểm hơn bản thiếu — vì nó trông như có.

Ngoại lệ đã biết và chấp nhận: 5 tệp dùng chung **bắt buộc** nhân bản vào `references/Skill-Library/` của
từng hệ vì `.skill` là zip tự chứa. Với những tệp đó, bản gốc ở `01-Chuan-Chung/` và phải nhân bản lại **tại
bước đóng gói**, không sửa trực tiếp ở từng hệ.

## Ghi chú thực hiện

Không đổi tên thư mục cũ và **không xóa tệp nào** — dựng hệ mới song song, đúng quy ước "tệp trên Drive chỉ
do người dùng xóa thủ công". Hệ cũ còn nguyên nên hoàn tác được bất cứ lúc nào.

<details><summary>Cân nhắc rủi ro trước khi làm (giữ lại)</summary>

Thu hẹp một hệ đang chạy và đổi tên thư mục sẽ ảnh hưởng Google Drive connector
— thuộc nhóm rủi ro cao, cần người phụ trách hệ đồng ý trước.


</details>
