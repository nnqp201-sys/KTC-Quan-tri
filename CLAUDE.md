# KTC-Quan-tri — Dự án quản trị nhiệm vụ hợp nhất

Thư mục gốc của dự án hợp nhất ba hệ **KTC-Kế-Hoạch → KTC-Theo-Dõi → KTC-Báo-Cáo** thành một chu trình
quản trị nhiệm vụ khép kín cho Trường Cao đẳng Kon Tum, kèm hệ soạn thảo văn bản hành chính
`KTC-Soan-Thao-VB` và kho dữ liệu nền định lượng `11-Du-lieu-Cong-Viec`.

Chu trình đích:
> Chủ trương/Văn bản → Nhiệm vụ → Kế hoạch → Giao việc → Theo dõi → Kết quả/Bằng chứng → Báo cáo →
> **Rà soát (KTC-Ra-Soat-897)** → Trình ký/Ban hành → Đánh giá → Điều chỉnh kế hoạch

Đây **không phải kho mã nguồn**. Nội dung chủ yếu là tài liệu nghiệp vụ (`.md`, `.docx`, `.xlsx`) và gói
Claude Skill (`.skill`), đồng bộ qua Google Drive for Desktop.

## Đọc trước khi làm việc

Mở đầu **mỗi phiên**: đọc mục 1 rồi mục 2 trước — sự thật vận hành và việc còn mở không ghi tại tệp này.

| Thứ tự | Tài liệu | Nội dung |
|---|---|---|
| 1 | `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md` | Sự thật vận hành hiện hành, phiên bản đang dùng, thứ tự ưu tiên nguồn |
| 2 | `92-Kinh-Nghiem/05-Known-Issues/Pending.md` | Việc đang mở; không lặp lại trạng thái ở đây |
| 3 | `91-Tai-Lieu-Thiet-Ke/Ke-hoach-hop-nhat-KTC-Ke-Hoach-KTC-Bao-Cao-KTC-Theo-Doi.md` | Kiến trúc hợp nhất, Master Task Register, lộ trình 6 giai đoạn — tài liệu điều khiển chính |
| 4 | `20-Chuan-Chung/11-Quy-Tac-Task-ID.md` | Phân biệt Task_ID với mã nhiệm vụ chuẩn `A01`–`S04` — nhầm chỗ này là hỏng gốc |
| 5 | `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` | 11 mã đơn vị chuẩn và mức lệch dữ liệu thật đang có |
| 6 | `91-Tai-Lieu-Thiet-Ke/Mo-Ta-Chi-Tiet-He-KTC-DIS-Chat-Cowork-Code.md` | Toàn cảnh 5 Hệ thống KTC, khác biệt Chat/Cowork/Code, các khoảng lệch cần xử lý |
| 7 | `91-Tai-Lieu-Thiet-Ke/GHI-CHU-CAU-NOI-3-HE.md` | Kiểm chứng khóa liên kết Theo-dõi-CV ↔ Báo-Cáo. **Lưu ý**: kết luận "tên đơn vị khớp 100%" dựa trên dữ liệu mẫu, đã bị đối chiếu thật bác bỏ — lấy theo mục 5 |
| 8 | `<mỗi hệ con>/00-README.md` | Phạm vi, quy trình và ràng buộc riêng của từng hệ |

## Cấu trúc

```
KTC-Quan-tri/
├── CLAUDE.md · README.md · .claude/ · .claude-plugin/   (bắt buộc ở gốc)
│
│   ── INPUT (1x) ──────────────────────────────────────────────
├── 10-Dau-Vao/               Kho đầu vào DÙNG CHUNG — 4 nhánh theo nguồn gốc dữ liệu
├── 11-Du-lieu-Cong-Viec/     Dữ liệu nền định lượng — danh mục nhiệm vụ/sản phẩm, KPI, khung đánh giá
│
│   ── PROCESS (2x) ────────────────────────────────────────────
├── 20-Chuan-Chung/           Bản GỐC của quy tắc và bảng mã dùng chung
├── 21-Master-Task-Register/  Sổ dữ liệu trung tâm của 3 hệ — ưu tiên số 1
├── 22-KTC-Dieu-Phoi/             Skill cấp dự án `ktc-quan-tri`: SKILL.md (tham chiếu) · references/ (nguồn rời) · .skill
├── 23-KTC-Ke-Hoach/          Hệ PIS — lập kế hoạch, sinh nhiệm vụ chuẩn (nguồn gốc Task_ID)
├── 24-KTC-Theo-doi-CV/       Control tower — vòng đời nhiệm vụ, tiến độ, cảnh báo, minh chứng
├── 25-KTC-Bao-Cao/           Hệ RIS — tổng hợp kết quả, đối chiếu kế hoạch, dự thảo báo cáo
├── 26-KTC-Soan-Thao-VB/      Hệ soạn thảo văn bản hành chính (7 loại VB + 6 lĩnh vực nghiệp vụ)
├── 27-KTC-The-Thuc/         Skill `the-thuc` — chuẩn thể thức MỌI sản phẩm .docx/.xlsx, chồng lên skill docx/xlsx
├── 29-Cong-Cu/               Script Python · `plugin_src/` (nguồn hook/agent) · `_trung_gian/` (xóa được)
│
│   ── OUTPUT (3x) ─────────────────────────────────────────────
├── 30-Ket-Qua/YYYY-MM-DD/<loại>/   Kết quả xuất ra
├── 31-Plugin/                Bản dựng plugin — sinh bởi `29-Cong-Cu/dong_goi_plugin.py`, không sửa tay
│
│   ── QUẢN TRỊ HỆ (9x) ────────────────────────────────────────
├── 90-Nhat-Ky-Van-Hanh/      Bộ nhớ quá trình — đọc MEMORY-INDEX.md đầu mỗi phiên
├── 91-Tai-Lieu-Thiet-Ke/     Tài liệu kiến trúc và ghi chú kiểm chứng
├── 92-Kinh-Nghiem/           Bài học · quyết định · lỗi đã biết · hồi quy
└── 99-Luu-Tru/               Bản trùng, bản thay thế
```

### Lớp chuẩn chung — đọc trước khi sửa bất cứ quy tắc dùng chung nào

`20-Chuan-Chung/` giữ **bản gốc**; các hệ giữ **bản sao**. Gói `.skill` là zip tự chứa nên bản sao trong
`<hệ>/references/Skill-Library/` là **bắt buộc** — xóa để "khử trùng lặp" sẽ làm hỏng skill khi đóng gói
lại. Sửa ở `20-Chuan-Chung/` trước, rồi nhân bản xuống tại bước build.

### Đầu vào khi dùng qua plugin Team (tài khoản thành viên)

Tài khoản phòng/khoa/bộ môn dùng plugin cấp Team **không có** thư mục `10-Dau-Vao/`. Mọi skill lấy đầu vào
theo thứ tự: **tệp đính kèm trong phiên** ("Add files and photos" — Chat/Cowork/Code) → thư mục dự án nếu có →
hỏi người dùng. Không từ chối xử lý chỉ vì thiếu thư mục. Đặc tả: `20-Chuan-Chung/00-Nguyen-Tac-Chung.md`.

## Bộ mã và phân loại dùng chung

Không nhớ bảng tại đây. Đọc bản gốc rồi mới phân loại hay quy đổi:

| Nội dung | Đọc |
|---|---|
| 6 Trục / 38 Nội hàm (TB 817) | `20-Chuan-Chung/30-Skill-Phan-Loai-6-Truc.md` · `22-KTC-Dieu-Phoi/references/10-Sau-Truc-38-Noi-Ham.md` |
| 17 lĩnh vực, mã `A01`–`S04`, danh mục sản phẩm | `22-KTC-Dieu-Phoi/references/13-Danh-Muc-Nhiem-Vu-Va-San-Pham.md` |
| Quy đổi KPI và xếp loại chất lượng (QĐ 1923) | `20-Chuan-Chung/19-Quy-Tac-KPI.md` · lập KPI cá nhân: hệ `28-KTC-KPI/` · tự đánh giá cá nhân quý: `28-KTC-KPI/Tu-Danh-Gia/` |
| Mã đơn vị | `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` |
| Căn cứ, viện dẫn văn bản (NĐ 30 · Pháp lệnh hợp nhất · quy ước Trường) — **VBHC: Luật không ghi số hiệu** | `20-Chuan-Chung/17-Quy-Tac-Vien-Dan.md` · tự kiểm `29-Cong-Cu/kiem_vien_dan.py` · quét hiệu lực `29-Cong-Cu/tra_hieu_luc.py` (agent `ktc-hieu-luc-vien-dan`) |
| **Thể thức sản phẩm .docx/.xlsx** — dựng từ `04-Good-Documents`/`03-Templates(1)`, A4, lề 2-2-3-2, TNR 14; đo trước khi giao | `20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md` · skill `the-thuc` · `29-Cong-Cu/kiem_the_thuc.py` |

Số nội hàm đánh lại từ 1 trong từng Trục — luôn ghi kèm Trục, không dùng số nội hàm đứng một mình.

**Hai thang điểm — không trộn.** Cùng khái niệm quy đổi khối lượng công việc đang có hai thang
(`KI-014`, chưa có văn bản phân định). Thang đang xuất hiện trên dữ liệu vận hành (cột điểm/hệ số Phụ lục
TB736) nằm trong `20-Chuan-Chung/30-Skill-Phan-Loai-6-Truc.md`. Thang 5 nhóm 50/120/250/350/450 trong
danh mục sản phẩm là **bảng gợi ý** (dự thảo lần 4; đã gửi đơn vị rà soát theo TB 1052/TB-CĐKT ngày 15/9/2026, **chưa ban hành**), không phải danh sách giá trị hợp lệ — xem
`22-KTC-Dieu-Phoi/references/13-Danh-Muc-Nhiem-Vu-Va-San-Pham.md`. Không dùng thang 5 nhóm để kiểm dữ liệu vận hành.
Không tự đặt quy tắc chuyển đổi giữa hai thang.

**Cơ quan chủ quản trong thể thức**: `UBND TỈNH QUẢNG NGÃI` – `TRƯỜNG CAO ĐẲNG KON TUM` (nhất quán trong toàn
bộ khung đánh giá hiện hành, sau sáp nhập tỉnh). Không dùng "UBND tỉnh Kon Tum" ở văn bản mới.

Hai hệ liên quan nằm **ngoài** thư mục này (không ghi cứng ổ đĩa — Nguyên tắc 4):
- `KTC-Database` — nguồn chính thức của dữ liệu văn bản nội bộ (kho 01–04 + Input/Output). Mọi hệ trong dự án đều dùng chung.
- `KTC-Ra-Soat-897-v2-Cai-tien` — lớp kiểm soát chất lượng **bắt buộc trước khi trình ký**, và là
  **bộ quy tắc soạn thảo dùng ngay từ lúc bắt đầu viết** (nguyên tắc 9). Dùng hai chiều:
  *khi đang viết* — `KTC-Ra-Soat-897-v2-Cai-tien/references/Checklist/07-Theo-Loai-Van-Ban.md` (checklist
  riêng cho Kế hoạch và Báo cáo), `KTC-Ra-Soat-897-v2-Cai-tien/references/Checklist/08-Quy-Uoc-Rieng-CDKT.md`
  (tên đơn vị chuẩn, thông số thể thức), `KTC-Ra-Soat-897-v2-Cai-tien/references/Checklist/04-Ngon-Ngu.md`
  (chuẩn hóa từ ngữ);
  *trước khi trình ký* — toàn bộ quy trình rà soát. Còn vấn đề **Mức 1** thì **không được trình**.
  Không hệ nào được giữ bản sao bộ quy tắc của 897 — trỏ tới bản gốc.

## Chạy thử hệ thống

```bash
python 29-Cong-Cu/kiem_tra_he_thong.py      # Tầng 1 — tĩnh, 13 phép kiểm, mã thoát 0/1
```

**Bắt buộc chạy sau mỗi lần sửa skill và trước/sau mỗi lần đóng gói.** Ba tầng kiểm thử đầy đủ và quy tắc
đóng gói: `.claude/rules/22-kiem-thu-va-dong-goi.md` (tự nạp khi chạm `29-Cong-Cu/` hoặc tệp `.skill`).

## Nguyên tắc bất biến

1. **Một nhiệm vụ – một Task_ID** (dạng `KTC-2026-Q3-00125`), dùng xuyên suốt kế hoạch → theo dõi → báo cáo → minh chứng. Không tạo lại cùng một nhiệm vụ ở nhiều hệ.
2. **Kế hoạch là nguồn sinh nhiệm vụ.** KTC-Theo-Dõi và KTC-Báo-Cáo chỉ tiếp nhận, cập nhật, tổng hợp — không tự tạo nhiệm vụ mới nếu nhiệm vụ đã tồn tại trong kế hoạch.
3. **Báo cáo phải truy ngược được** tới nhiệm vụ → kế hoạch → đơn vị thực hiện → kết quả → minh chứng. Không đưa vào báo cáo kết quả không xác định được nguồn.
4. **Nhiệm vụ phát sinh** phải ghi rõ nguồn, căn cứ, ngày phát sinh, đơn vị giao, đơn vị thực hiện, thời hạn, sản phẩm — rồi mới cấp Task_ID và đưa vào hệ.
5. **Mọi thay đổi phải có lịch sử**: giá trị cũ → lý do → căn cứ → người thay đổi → thời gian → giá trị mới.
6. **AI không thay thế dữ liệu gốc và không quyết định thay người có thẩm quyền.** Vai trò AI: đọc, đối chiếu, phân loại, phát hiện thiếu/sai, tổng hợp, đề xuất, dự thảo.
7. **Phát triển từ file tương đồng đã ban hành**, không dựng văn bản từ mẫu trống. Mẫu trống chỉ cho số đo thể thức, không chứa văn phong.
8. **Soạn trên văn bản đã có thì phải bật Track Changes** và xuất phát từ chính file gốc — không soạn lại rồi trình bày như bản sửa. Kích hoạt khi nghe "track changes" hoặc "ghi nhật ký sửa đổi"; công cụ: `29-Cong-Cu/ktc_trackchanges.py`, quy trình: `20-Chuan-Chung/15-Skill-Track-Changes.md`.
9. **Bộ quy tắc `KTC-Ra-Soat-897` dùng từ lúc bắt đầu viết**, không đợi đến bước rà soát cuối. Chốt chặn trước trình ký vẫn giữ nguyên.
10. **`KTC-Database` là cơ sở dữ liệu tham mưu quản trị** — phải tìm kiếm sâu chiến lược, đề án, kế hoạch/báo cáo chuyên đề, quy định để có cơ sở, không chỉ tra cứu một văn bản lẻ.

Bốn nguyên tắc 7–10 được đặc tả đầy đủ tại **`20-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`** — đọc
trước mọi tác vụ sinh văn bản.

## Nguồn dữ liệu chuẩn (khi hai nơi mâu thuẫn, lấy theo cột này)

| Loại dữ liệu | Hệ nguồn chuẩn |
|---|---|
| Văn bản pháp lý, quy định, mẫu | `KTC-Database` (kho 01–04) |
| Danh mục nhiệm vụ chuẩn, sản phẩm, điểm/hệ số, KPI, khung đánh giá | `11-Du-lieu-Cong-Viec` |
| Nhiệm vụ, baseline kế hoạch | `KTC-Ke-Hoach` |
| Trạng thái, % tiến độ, minh chứng | `KTC-Theo-doi-CV` |
| Kết quả đã xác nhận theo kỳ | `KTC-Bao-Cao` |

Internet chỉ dùng để kiểm chứng hiệu lực/cập nhật văn bản hoặc khi nội bộ thiếu dữ liệu; ưu tiên nguồn chính
thống và phải ghi rõ nguồn trong kết quả.

## Liên kết dữ liệu với KTC-Database

Đường dẫn: **bản gốc trên Google Drive** `My Drive/KTC-Database` — ngoài thư mục dự án; bản chép cạnh dự án sẽ bị xóa và **đã cũ**. Script lấy qua `29-Cong-Cu/duong_dan.py` (`KTC_DATABASE_DIR` → ổ Google Drive → thư mục ngang cấp). Nơi lưu từng loại đầu vào: `20-Chuan-Chung/00-Nguyen-Tac-Chung.md`, Nguyên tắc 4. Kho nền pháp lý và quy
định dùng chung. Đọc trực tiếp, **không sao chép dữ liệu sang KTC-Quan-tri**.

**Chỉ mục đầy đủ 8 kho, văn bản gốc chống lưng, cảnh báo về kho 03, quy tắc metadata:**
`22-KTC-Dieu-Phoi/references/02-Chi-Muc-KTC-Database.md` — đọc tệp đó trước khi tra kho, đừng duyệt cây thư mục mò.

Ba ràng buộc **luôn có hiệu lực**, không đợi đọc chỉ mục:

- **Kho chỉ đọc.** Hook chặn mọi thao tác ghi, kể cả sửa metadata cho đúng hơn. Cần sửa kho thì viết đề
  xuất ra `30-Ket-Qua/YYYY-MM-DD/` để người có thẩm quyền tự áp vào Drive; không tìm cách lách.
- **Chỉ tạo kết quả sau khi đã đối chiếu thật** với kho 01–04. Không đọc được kho → **dừng lại và hỏi**.
  Nếu người dùng yêu cầu cứ làm, ghi ngay đầu kết quả: "⚠️ Chưa đối chiếu với kho 01-04 — độ tin cậy hạn chế".
- **Tuyệt đối không trích dẫn file mẫu/checklist nội bộ làm "Căn cứ" pháp lý** — theo quy tắc của
  KTC-Ra-Soat-897, đây luôn là lỗi Mức 1.
- **Trích dẫn cụ thể** số hiệu, ngày ban hành, tên mẫu — không chỉ nêu tên tệp.
- **Kết quả hoàn chỉnh xuất `.docx`** vào `30-Ket-Qua/YYYY-MM-DD/<loại thao tác>/`, **đạt chuẩn thể thức** (`kiem_the_thuc.py`, 0 lỗi Mức 1–2).

## Quy ước khi làm việc trong thư mục này

- **Đơn vị luôn ghi bằng mã chuẩn** (`P-THHC`, `K-KTCN`…) theo `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` — không ghi tên tự do. Cùng một đơn vị hiện đang tồn tại ba kiểu viết khác nhau trong dự án, một kiểu sai chính tả.
- **Phân loại nghiệp vụ dùng chung**: 6 Trục kết quả trọng tâm theo TB 817; 4 hệ quy chiếu thể thức A (hành chính, NĐ 30) / B (Đảng, HD 05-HD/VPTW — tuyệt đối không áp NĐ 30) / C (VBQPPL) / D (đoàn thể); 4 mức vấn đề khi rà soát (1 bắt buộc sửa → 4 góp ý).
- **File `.skill` là gói đã đóng** — không sửa trực tiếp. Sửa nguồn trong `references/` của hệ tương ứng rồi đóng gói lại.
- **`desktop.ini`** là file của Google Drive for Desktop — không sửa, không xóa, không đưa vào tài liệu.
- **Đo định dạng `.docx`**: Claude Code là nền tảng duy nhất đọc được lề/cỡ chữ thật (python-docx). Nếu không chạy được script đo, ghi `FORMAT_BINARY_UNVERIFIED` — không suy đoán từ nội dung text.
- **Tên file/thư mục** dùng tiếng Việt không dấu, có gạch nối; giữ tiền tố số thứ tự (`00-`, `01-`) khi thư mục đã dùng quy ước đó.
- Không xóa/di chuyển tài liệu gốc trên Drive. Khi cần dọn, liệt kê danh sách để người dùng tự xóa thủ công.

## Trạng thái đang mở

Không ghi trạng thái tại đây — sẽ cũ. Lấy tại:

- `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md` — sự thật vận hành hiện hành, phiên bản đang dùng
- `92-Kinh-Nghiem/05-Known-Issues/Pending.md` — việc còn mở
