# CP-20260913-001 — Tiếp thu gói kinh nghiệm KTC-RIS và 6 đề xuất phát triển hệ

**Ngày lập:** 13/9/2026 · **Trạng thái:** Chờ duyệt
**Nguồn khảo sát:** `D:\.CLAUDE code\kinh nghiem bao cao\` — 45 tệp, ~230 KB, gồm `KTC-RIS-Transfer-Pack/`
(8 phần + 26 tệp Knowledge + 5 script) và 6 tệp bản rời ở gốc.

---

## 1. Gói đó là gì

Là **gói chuyển giao hệ KTC-Bao-Cao (KTC-RIS) v2.5.1 từ Claude sang ChatGPT**, lập ngày 13/9/2026.
Không phải phiên bản mới của hệ, mà là bản *kết tinh tri thức* của hệ tại thời điểm 19/8/2026, đóng theo
cấu trúc 8 phần: kiểm kê khả năng truy xuất → instructions → knowledge base → workflow → ví dụ đúng/sai →
checklist 12 bước tái tạo → 20 bài test nghiệm thu → script.

Phát hiện trung tâm của gói (mục 0.4): **Project "KTC-Bao-Cao" trên Claude rỗng — 0 tài liệu, 0 byte.**
Toàn bộ năng lực nằm ở gói `.skill` và kho Drive. Đây chính là kết luận mà dự án này đã đi tới một cách
độc lập khi lập lớp `01-Chuan-Chung/`.

## 2. Đối chiếu với hiện trạng — phần lớn đã vượt qua

| Nội dung trong gói | Hiện trạng KTC-Quan-tri | Kết luận |
|---|---|---|
| Skill v2.5.1, 6 skill nghiệp vụ | `ktc-bao-cao-v3.5.skill` — 36 tệp, là tập cha của cả hai nhánh cũ | **Đã vượt** |
| Lớp `references/Memory/` 7 tệp | Đã nằm trong v3.5 (gộp 14/9/2026) | **Đã tiếp thu** |
| BUG-15 (Mục II gộp nhầm vào Trục cuối) | Đã vá — `read_bc736_excel.py` v3.2 mang logic tách Mục II của v3.1 | **Đã đóng** |
| Số liệu nền Trường 2023–2025 | `BOI-CANH-TRUONG-CDKT-So-lieu-nen-KTC-RIS.md` | **Đã có** |
| 16 mục chuẩn phong cách (B36) | `Skill-Tu-hoc-Phong-Cach-Bao-Cao.md` + bản bổ sung 16/8/2026 | **Đã có, đầy đủ hơn** |
| BH-01 "số hiệu cao hơn ≠ ít lỗi hơn" | Đã tự rút ra, ghi ở `00-TRANG-THAI-GOI-SKILL.md` | **Trùng khớp** |

**Kết luận:** gói không mang lại nghiệp vụ mới. Giá trị còn lại nằm ở **cơ chế** — cách hệ tự nhớ, tự kiểm,
tự bàn giao — và ở **một vài dữ kiện cụ thể** dự án đang thiếu. Sáu đề xuất dưới đây chỉ lấy phần đó.

---

## 3. Sáu đề xuất, xếp theo mức chặn

### ĐX-1 (P0) — Đồng bộ ngược nguồn rời ↔ gói `.skill` của KTC-Bao-Cao

**Vấn đề đã đo được, không phải suy đoán.** So từng tệp giữa `ktc-bao-cao-v3.5.skill` và thư mục nguồn rời
`KTC-Bao-Cao/references/`:

- **14 tệp có trong gói, KHÔNG có ở nguồn rời** — toàn bộ `references/Memory/` (7 tệp + `kiem_tra_bo_nho.py`),
  `assets/mau-nhat-ky-chay.md`, `PATCH-NOTES-v2.5.1.md`, `PATCH-NOTES-v3.5.md`, `make_fixtures_test.py`,
  `test_regression_v251.py`, `test_regression_v34.py`.
- **11 tệp lệch kích thước**, nghiêm trọng nhất là hai script chính:
  `read_bc736_excel.py` (gói 22.531 B / rời 20.458 B) và `fill_bc736.py` (gói 15.970 B / rời 14.101 B).
  Bản trong gói xử lý Mục II nhiều hơn (17 lần nhắc `muc_ii` so với 13 ở bản rời).

**Hậu quả nếu không xử lý:** quy ước của dự án là *"sửa nguồn trong `references/` rồi đóng gói lại"*. Làm
đúng quy ước đó ngay bây giờ sẽ **xóa mất lớp Memory và làm thoái lui hai script chính** — tức là tái tạo
lại BUG-15. `00-TRANG-THAI-GOI-SKILL.md` đã cảnh báo nguy cơ này ở dạng định tính; nay có số đo cụ thể.

**Đề nghị làm:**
1. Bung gói v3.5 ra nguồn rời theo nguyên tắc *gói mới hơn thì gộp, không ghi đè ngược*.
2. Bổ sung vào `tools/dong_goi_skill.py` một bước **bắt buộc chặn**: so danh sách tệp và kích thước giữa
   nguồn rời và gói hiện hành; phát hiện tệp thiếu hoặc tệp trong gói lớn hơn → **dừng, không đóng gói**.
3. Ca hồi quy đi kèm: `99-Kinh-Nghiem/02-Regression/Cases/test_dong_goi_khong_thoai_lui.py`.

> Theo quy tắc của dự án: *"thêm phép kiểm mới thì phải thêm ca thử ngược trong cùng lần sửa"*.

---

### ĐX-2 (P0) — Chốt danh sách đầu mối nộp báo cáo tháng

> **Đính chính 14/9/2026.** Bản đầu của mục này kết luận **14 đầu mối** bằng cách đếm Ban Truyền thông
> thành một đầu mối riêng, và cho rằng đã giải được con số 14 mà gói chuyển giao bỏ ngỏ. **Sai.** Người
> phụ trách hệ xác nhận Ban Truyền thông là bộ phận **cấp hai** thuộc Phòng TH-HC&QT, nhiệm vụ được tổng
> hợp chung vào thư mục của Phòng. Số đầu mối đúng là **13**. Con số 14 của gói cũ **vẫn chưa giải thích
> được** — không ép dữ liệu cho khớp. Xem `KI-004` (đã đóng) và `01-Chuan-Chung/13-Bang-Ma-Don-Vi.md`.

Gói chuyển giao liệt kê đây là hạng mục `[KHÔNG THỂ TRUY XUẤT]` số 6: *"Danh sách đầy đủ 14 đơn vị phải nộp
báo cáo — cần anh/chị điền tay"*. **Dữ liệu thật trong dự án này trả lời được câu đó.**

Đếm thư mục nộp thật tại `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/`: 5 Phòng + 6 Khoa (khớp đúng 11 mã của
`13-Bang-Ma-Don-Vi.md`) + `Cong-Doan` + `Doan-TN` = **13 đầu mối**. Ban Truyền thông **không** tính riêng —
tệp `BAN TT.xlsx` nằm trong `Phong-THHCQT/` là đúng chủ đích, vì Ban trực thuộc Phòng.

**Hệ quả phải xử lý ngay:** Công đoàn cơ sở và Đoàn Thanh niên – Hội Sinh viên **nộp báo cáo nhưng không có
trong bảng 11 mã đơn vị**. Đây là tổ chức đoàn thể — thuộc hệ quy chiếu thể thức **D**, không phải A. Bảng
mã hiện hành không có chỗ cho chúng.

**Đề nghị làm:** bổ sung vào `01-Chuan-Chung/13-Bang-Ma-Don-Vi.md` một mục *"Đầu mối nộp báo cáo"* tách khỏi
mục *"Đơn vị hành chính cấp Trường"*, gồm 2 loại đầu mối: đơn vị cấp một (11 mã) · tổ chức đoàn thể (2 đầu
mối, cần cấp mã, đề xuất `DT-CDCS`, `DT-DTN`) — cộng một mục riêng cho bộ phận cấp hai (Ban Truyền thông),
**không** phải đầu mối. *(Phần Ban Truyền thông đã làm 14/9/2026 khi đóng `KI-004`.)*

Đây là điều kiện để `KI-006` không tái diễn: checklist Bước 0 phải có đủ **13** dòng, không phải 11.

---

### ĐX-3 (P1) — Lập sổ chất lượng dữ liệu theo đơn vị, ghi liên tục qua các kỳ

Gói có `E04-Chat-Luong-Du-Lieu-Don-Vi.md`: bảng theo dõi từng đơn vị × từng kỳ, ký hiệu 🔴 lặp nhiều kỳ /
🟡 một kỳ / ✅ đã khắc phục, mỗi mục bắt buộc nhãn `[ĐÃ XÁC MINH]` hoặc `[CHƯA XÁC MINH]`.

Dự án hiện ghi cùng loại thông tin ở `KI-006` — nhưng đó là **ảnh chụp một kỳ**, không phải sổ liên tục.
Không trả lời được câu hỏi quan trọng nhất đầu mỗi kỳ: *"đơn vị nào hay sai kiểu gì, sai mấy kỳ liền?"*

**Đề nghị làm:** lập `03-Nhat-Ky-Van-Hanh/04-Chat-Luong-Du-Lieu-Don-Vi.md` với bảng 13 đầu mối × các kỳ, nạp
sẵn dữ liệu đã có (T8/2026 từ `KI-006`, T7/2026 từ gói cũ), và đưa vào quy trình: **Bước 0 đọc sổ này trước
khi phát checklist; chốt kỳ thì cập nhật sổ ngay trong phiên.**

Giữ nguyên hai quy tắc của gói vì chúng đã trả giá để có:
- *"Ghi sự việc, không ghi cảm nhận"* — ghi "nộp IIb thiếu cột 11–16", không ghi "làm ẩu".
- *"Không dùng thông tin `[CHƯA XÁC MINH]` để nhắc đơn vị"* — nhắc sai làm mất uy tín checklist.

---

### ĐX-4 (P1) — Tách sổ đăng ký lỗi script khỏi `05-Known-Issues/`

`05-Known-Issues/Pending.md` hiện trộn hai loại: khoảng trống **nghiệp vụ** (KI-001 thiếu cột Task_ID,
KI-011 lệch tên Trục) và lỗi **công cụ** (KI-013 gói chưa đóng lại). Gói cũ tách riêng, và phần đáng giá
nhất của nó là **bảng triệu chứng → nghi lỗi → cách kiểm**:

| Triệu chứng | Nghi lỗi | Kiểm bằng cách |
|---|---|---|
| `kind=None` | BUG-01 | Xem chữ "KPI" nằm ở hàng nào so với hàng chứa "TT" |
| `so_nhiem_vu=0` | BUG-02 | Xem nhãn Trục có đúng dạng `Trục <số>` không |
| KPI cao gấp ~2 lần | BUG-03 | Đếm xem dòng "Tổng cộng" có bị tính là nhiệm vụ không |
| Trục 6 nhiều việc bất thường | BUG-15 | Xem có việc nào thuộc Mục II bị kéo vào không |
| Phần III giống hệt Phần I | BUG-16 | Đối chiếu nội dung hai phần |

Bảng này biến một buổi truy lỗi thành một phép kiểm 30 giây. Hiện dự án **không có**.

**Đề nghị làm:** `99-Kinh-Nghiem/05-Known-Issues/BUG-Registry-Scripts.md` — nhập 16 mã BUG cũ kèm cột "bản
nào đã vá", mở rộng cho các script hiện có của dự án (`tools/` 11 tệp + `Skill-Library/` 6 tệp), giữ nguyên
quy tắc cấp mã: **mô tả hậu quả thực tế, không chỉ mô tả kỹ thuật**.

Kèm một việc kiểm chứng: BH-03 của gói ghi *"kiểm thử trên fixture mô phỏng không thay được file thật"* —
15/15 phép kiểm vẫn để lọt BUG-15. Dự án nay **có hơn 40 tệp Excel/Word thật của 14 đầu mối**. Đề nghị chạy
`test_regression_v34.py` trên dữ liệu thật này rồi ghi kết quả — đó là việc treo số 3 của gói cũ, nay làm được.

---

### ĐX-5 (P2) — Chuẩn hóa "gói bàn giao" thành một năng lực của dự án

Cấu trúc 8 phần của `KTC-RIS-Transfer-Pack` là một **mẫu tái dùng được**, không chỉ để chuyển sang ChatGPT:

| Dùng cho | Vì sao cần |
|---|---|
| Bàn giao người kế nhiệm | Tri thức vận hành hiện nằm trong đầu một người và trong các gói `.skill` |
| Chạy hệ trên nền khác | `KI-010` ghi rõ: đã chạy thử trên Claude Chat nhưng không có ghi chép nào |
| Sao lưu tri thức | Drive hỏng hoặc mất quyền là mất trắng |

Hai thành phần đáng lấy nguyên: **PART 0 — bảng kiểm kê `[KHÔNG THỂ TRUY XUẤT]` kèm cách lấy thủ công**
(trung thực về giới hạn, không giả vờ đầy đủ), và **PART 6 — 20 bài test nghiệm thu sau khi tái tạo**.

**Đề nghị làm:** `tools/xuat_goi_ban_giao.py` — nhận tên một hệ con, sinh gói 8 phần vào
`12-Output/YYYY-MM-DD/Ban-giao/`. Ưu tiên thấp: chỉ làm sau khi ĐX-1 xong, vì xuất gói từ nguồn đang lệch
là nhân bản cái lệch.

---

### ĐX-6 (P2) — Nhập 6 quyết định và 6 bài học vào lớp tiến hóa tri thức

Gói có `E05` (QĐ-01…06) và `E06` (BH-01…06), mỗi mục bắt buộc có **lý do** và **dấu hiệu nhận biết sớm**.
Dự án hiện có 2 Decision Log và 3 Lessons Learned — tức là gói cũ giàu hơn ở lớp này.

Ánh xạ đề nghị (ghi rõ nguồn kế thừa, không trình bày như tự rút ra):

| Nguồn | Nội dung | Đích |
|---|---|---|
| QĐ-01 | Không bịa nội dung thiếu — đánh dấu `[CẦN BỔ SUNG]` | `06-Decision-Log/DL-20260913-002` |
| QĐ-02 | Chủ ngữ báo cáo cấp Trường luôn là "Nhà trường" | như trên (đã có trong Skill, cần ghi **lý do**) |
| QĐ-03 | Không tự sửa số liệu KPI dù biết chắc sai | như trên — gắn nguyên tắc bất biến 6 |
| QĐ-04 | Khớp tuyệt đối trước khi khớp gần đúng khi điền mẫu Word | như trên |
| BH-02 | Lỗi nguy hiểm nhất là lỗi không báo lỗi | `01-Lessons-Learned/LL-20260913-004` |
| BH-03 | Fixture không thay được file thật | `LL-20260913-005` — nối với ĐX-4 |
| BH-05 | Bám mẫu gốc, đừng sáng tạo thể thức | `LL-20260913-006` — nối nguyên tắc bất biến 7 |

QĐ-05 (gộp v3.1) và QĐ-06 (lập lớp Memory) **đã thực hiện xong** — nhập dưới dạng lịch sử, trạng thái
"đã đóng". BH-01, BH-04, BH-06 đã có tương đương trong dự án — chỉ ghi liên kết, không nhân bản.

---

## 4. Thứ tự thực hiện đề nghị

```
ĐX-1 (đồng bộ nguồn ↔ gói)  ──┐  phải xong trước mọi việc đóng gói lại
ĐX-2 (chốt 14 đầu mối)      ──┤  chặn Bước 0 của kỳ tháng 9/2026
                              ▼
ĐX-3 (sổ chất lượng đơn vị) · ĐX-4 (sổ lỗi script + chạy trên dữ liệu thật)
                              ▼
ĐX-6 (nhập QĐ/BH)  →  ĐX-5 (công cụ xuất gói bàn giao)
```

ĐX-1 và ĐX-2 nên làm ngay: một cái đang **chặn thao tác đóng gói lại**, một cái đang **chặn Bước 0 của kỳ
tháng 9/2026** — kỳ này theo `E01` của gói cũ là "chưa bắt đầu".

## 5. Việc KHÔNG đề nghị làm

- **Không sao chép 26 tệp Knowledge của gói vào dự án.** Chúng là bản v2.5.1, cũ hơn v3.5 đang chạy.
  Sao chép vào sẽ tạo đúng loại phân kỳ mà `KI-005` vừa mất công đóng.
- **Không dùng `07_SCRIPTS/` của gói.** Cùng tên tệp nhưng cũ hơn bản trong v3.5.
- **Không chuyển hệ sang ChatGPT** như gói dự tính. Dự án đã chọn nền Claude Code vì đây là nền duy nhất
  đọc được số đo định dạng `.docx` thật — tiền đề của cả hệ 897. Giữ gói như **tài liệu tham khảo về giới
  hạn nền tảng**: mục 0.7 vẫn đúng và hữu ích.

---

**Liên quan:** `KI-005` (đã đóng) · `KI-006` · `KI-010` · `KI-013` · `DL-20260913-001` ·
`KTC-Bao-Cao/00-TRANG-THAI-GOI-SKILL.md`
