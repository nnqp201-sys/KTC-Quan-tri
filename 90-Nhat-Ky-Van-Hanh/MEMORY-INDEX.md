# MEMORY-INDEX — KTC-Quan-tri

**Cập nhật:** 18/9/2026
**Phạm vi:** sự thật vận hành hiện hành; không lưu lịch sử chi tiết tại đây.
**Mô hình kế thừa:** `KTC-Ra-Soat-897-v2-Cai-tien/09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md`

## Điểm nạp — đọc theo thứ tự này khi mở phiên làm việc

1. Đọc tệp này.
2. Đọc `SKILL.md`.
3. Đọc tài liệu được `SKILL.md` định tuyến theo tác vụ (a)–(e).
4. Đọc Process Memory gần nhất cùng loại tác vụ, nếu có.
5. Đọc tệp đầu vào hiện tại.

Không nạp toàn bộ changelog, decision log hay Process Memory khi chưa có nhu cầu cụ thể.

## Sự thật vận hành ổn định

- Hệ này **điều phối**, không thay thế ba hệ Kế hoạch – Theo dõi – Báo cáo.
- Một nhiệm vụ – một Task_ID – một dòng dữ liệu gốc; chỉ `KTC-Ke-Hoach` được cấp Task_ID.
- Mã `A01`–`S04` là **loại** nhiệm vụ, không phải định danh lần giao việc.
- Danh mục 122 nhiệm vụ chuẩn **chỉ phủ 5 Phòng**; sáu Khoa chưa có dữ liệu, sẽ bổ sung sau.
- Phụ lục Ia/Ib chưa có cột `Task_ID` → mọi đối chiếu kế hoạch ↔ báo cáo là **gần đúng** và phải tự khai
  như vậy.
- Đơn vị luôn ghi bằng mã chuẩn; cột "Đơn vị chủ trì" trong dữ liệu thật còn chứa bộ môn, ban, chức danh —
  bảng mã cần cấp thứ hai.
- Thang điểm 50/120/250/350/450 là **bảng gợi ý** xây danh mục, **không phải** danh sách giá trị hợp lệ.
  Kiểm tra bằng công thức `hệ số = điểm × 1%`, không kiểm tra bằng danh sách.
- Mẫu Phụ lục IIb có ~8 dòng tiêu đề nhóm; không loại ra thì đếm thừa ~30%.
- Kho `KTC-Database` **chỉ đọc** — hook chặn ghi. Đề xuất sửa kho viết ra `30-Ket-Qua/`.
- Thiếu kho dữ liệu nền → dừng và hỏi. Thiếu riêng bộ nhớ vận hành → chạy tiếp, ghi cảnh báo.
- **Nguồn rời trong `references/` và nội dung trong `.skill` KHÔNG mặc nhiên đồng bộ — gói có thể MỚI HƠN.**
  Trước khi đóng gói phải so từng tệp; tệp nào trong gói mới hơn thì **gộp**, không ghi đè. Tiền lệ: Skill 33
  trong gói là v3.0 còn bản rời chỉ v2.3. Dùng `29-Cong-Cu/dong_goi_skill.py` (kiểm frontmatter, liên kết gãy,
  đối chiếu danh sách tệp trước/sau).
- **Không hệ nào được sao chép bộ quy tắc của hệ khác để "cho đầy đủ".** Bản sao không có cơ chế đồng bộ
  chắc chắn sẽ lệch, và **bản lệch nguy hiểm hơn bản thiếu** vì nó trông như có. Bằng chứng: `KTC-DIS-Tong-Hop-VB`
  chép checklist của 897, sau một tháng **28/28 tệp** đều tụt lại sau bản gốc (`03-Phap-Ly.md` còn 357 b so
  với 10.513 b). Ngoại lệ duy nhất: 5 tệp dùng chung, bản gốc ở `20-Chuan-Chung/`, nhân bản tại bước đóng gói.
- **Họ hệ thống KTC không có hệ "làm được mọi việc".** Mỗi hệ một vai: soạn thảo (`ktc-soan-thao-vb`) · rà soát
  (`ktc-ra-soat-897`) · kế hoạch (`ktc-ke-hoach`) · báo cáo (`ktc-bao-cao`) · kho dữ liệu (`ktc-database`).
- **Đối chiếu tệp giữa hai hệ phải so theo ĐƯỜNG DẪN, không theo tên tệp.** So theo tên cho kết quả sai:
  `99-Luu-Tru/He-da-thay-the/KTC-DIS-Tong-Hop-VB/references/Prompt-Library/02-Ra-Soat/01-Quyet-Dinh.md`
  bị tính là "đã chuyển" chỉ vì tồn tại
  `99-Luu-Tru/He-da-thay-the/KTC-DIS-Tong-Hop-VB/references/Prompt-Library/01-Soan-Thao/01-Quyet-Dinh.md`.
- **Khi đóng gói `.skill`: thư mục gốc trong zip phải TRÙNG với `name` của frontmatter**, và phải loại trừ
  chính tệp `.skill` khỏi zip — nếu không gói sẽ tự chứa bản cũ của nó.
- **Chạy thử hệ thống**: `python 29-Cong-Cu/kiem_tra_he_thong.py` (Tầng 1, 11 phép kiểm) và bộ thử ngược
  `92-Kinh-Nghiem/02-Regression/Cases/test_kiem_tra_he_thong.py`. Ba tầng kiểm thử mô tả ở
  `92-Kinh-Nghiem/02-Regression/README.md`. Chạy sau mỗi lần sửa skill và **cả trước lẫn sau** khi đóng gói.
- **Thêm phép kiểm mới thì phải thêm ca THỬ NGƯỢC trong cùng lần sửa** — nạp chuỗi biết chắc sai để xác nhận
  nó bắt được. Ngay lần đầu, bộ thử ngược đã phát hiện phép kiểm C6 bỏ sót dạng không dấu `dung ktc-van-ban`.
- **Không suy diễn phiên bản từ tên tệp.** Phải mở tệp đọc nội dung tự khai. Bài học: hai gói `.skill` của
  `KTC-Bao-Cao` đặt tên gây hiểu nhầm thứ tự phiên bản.
- **Dựng văn bản: tìm bản cùng loại ĐÃ BAN HÀNH trước, đừng dựng từ mẫu trống.** Thứ tự nguồn: (1) văn bản
  cùng loại cùng kỳ đã ban hành → (2) kỳ gần nhất trong `04-Good-Documents/` → (3) mẫu trống `.dotx`/`.xltx`
  → (4) mẫu có chú thích hướng dẫn → (5) `Checklist 08`/TB 597 để kiểm số đo. Mẫu trống **không chứa văn
  phong**. Xem `LL-20260913-002`.
- **Thể thức văn bản hành chính của Trường** (TB 597): A4, lề trên 2 – dưới 2 – trái 3 – phải 2 cm; nội dung
  Times New Roman **cỡ 14**, dàn đều hai lề, thụt đầu dòng **1,27cm**, cách đoạn ≥ 6pt; Quốc hiệu cỡ 13 hoa
  đậm, tiêu ngữ cỡ 14 đậm; "Nơi nhận" cỡ 12 nghiêng đậm, danh sách nơi nhận cỡ 11; chức vụ người ký cỡ 14
  hoa đậm. Phụ lục Excel để **khổ ngang**.
- **Bốn nguyên tắc soạn thảo bất biến** (`20-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`) — áp dụng
  mặc định, không cần người dùng nhắc lại: **NT-1** phát triển từ file tương đồng đã ban hành · **NT-2**
  Track Changes khi soạn trên văn bản đã có, xuất phát từ file gốc · **NT-3** dùng bộ quy tắc 897 ngay từ
  lúc bắt đầu viết · **NT-4** KTC-Database là CSDL tham mưu, phải tìm kiếm sâu chiến lược/đề án/chuyên đề.
- **Track Changes đã có công cụ thi hành**: `29-Cong-Cu/ktc_trackchanges.py`, kích hoạt theo
  `20-Chuan-Chung/15-Skill-Track-Changes.md` khi người dùng nói "track changes" hoặc "ghi nhật ký sửa
  đổi", hoặc khi tác vụ là sửa/góp ý/hoàn thiện một văn bản đã tồn tại. Chạy được **chỉ trên Claude Code**.
- **`paragraph.text` của python-docx bỏ sót nội dung trong `<w:ins>`/`<w:del>`** — đọc file có track
  changes phải dùng `_text_day_du()`, không dùng `.text`, nếu không sẽ kết luận sai là file rỗng/khác gốc.
- **Không viết lại quy tắc đã có ở hệ khác.** Chuẩn kỹ thuật Track Changes đã thành văn đầy đủ tại
  `KTC-Ra-Soat-897-v2-Cai-tien/references/Skill-Library/Bo-Sung-Chuan-Hoa-TrackChanges-MauChu-PhienBanSkill_20260825.md`
  — trỏ tới, không chép lại, để khi hệ 897 cập nhật thì hệ này không lệch.
- **`ktc-bao-cao` và `ktc-ke-hoach` đã chạy thử trên Claude Chat** (tài khoản người phụ trách hệ, trước
  13/9/2026). Hai gói chạy được trên nền Chat, không chỉ trên Code. **Chưa có nhật ký kết quả đợt chạy đó
  trong dự án** — muốn kết luận về chất lượng đầu ra trên Chat thì phải hỏi lại người dùng hoặc lấy
  transcript, không suy đoán.
- **Khác biệt nền tảng phải tính đến khi thiết kế skill**: Chat/Cowork **không chạy được `python-docx`**,
  nên mọi bước đo lề/cỡ chữ thật và mọi thao tác Track Changes ở mức OOXML **chỉ thực hiện được trên Claude
  Code**. Skill chạy trên Chat phải nêu rõ giới hạn này thay vì mô tả định dạng bằng mắt.
- **Mỗi đơn vị nộp HAI loại tệp**: `.docx` = Phụ lục IIa (báo cáo **tường thuật**, đã chia sẵn 6 Trục —
  đây là nguồn văn phong) và `.xlsx` = Phụ lục IIb/Ib (bảng nhiệm vụ, nguồn số liệu). Đọc thiếu `.docx` thì
  phải tự ghép văn từ cột mô tả công việc và văn sẽ rời rạc.
- **Phụ lục kết quả và kế hoạch tháng cấp Trường KHÔNG gộp từ đơn vị.** Phụ lục báo cáo lại **kế hoạch công
  tác của chính Trường**; kế hoạch tháng là **bản chi tiết hóa kế hoạch quý** + nhiệm vụ phát sinh. Bằng
  chứng: phụ lục tháng 7 khớp KH quý III **39/41 = 95%**, tháng 8 khớp 26/40. Đã ghi vào Skill 33 v2.4
  (BƯỚC 0A) và Skill 36 v2.0 (BƯỚC 0); `KI-012` đã đóng.
- **Danh mục mục con của báo cáo tháng là CỐ ĐỊNH theo mẫu** `00. Mau bao cao thang (cap Truong).docx`:
  mục 1 có 6 mục con · mục 2 có 2 · **mục 3 không có** · mục 4 có 3 · mục 5 có 4 · mục 6 có 3 · mục 7 có 8
  Nghị quyết (59·66·68·79·70·71·72·80). Mẫu ghi rõ mỗi mục con lấy từ đơn vị nào. **Không tự sinh nhãn**,
  không dùng "Công tác khác".
- **Hai tệp "mẫu" trong `25-KTC-Bao-Cao/` không phải mẫu trống**: `00. Phu luc chi tiet...xlsx`/`.xltx` có
  sheet `BC Kết quả tháng 7` với 39 nhiệm vụ thật. `.docx`/`.dotx` là cùng một nội dung, khác định dạng lưu.
- **Phụ lục/kế hoạch cấp Trường CHỈ gồm nhiệm vụ do lãnh đạo cấp Trường trực tiếp chỉ đạo** (Hiệu trưởng,
  Phó Hiệu trưởng, Bí thư/Phó Bí thư Đảng ủy, Chủ tịch Công đoàn, Bí thư ĐTN, Chủ tịch HSV). Kiểm chứng:
  PL-375 và KH-834 không có dòng nào do Trưởng khoa/Phó Trưởng khoa chỉ đạo. Đây là điều kiện **cần nhưng
  chưa đủ** — PL-375 chỉ 39 nhiệm vụ, lọc theo tiêu chí này ra 211; phần chênh là chọn lọc biên tập, **chưa
  biết tiêu chí**, không được tự đặt ra.
- **TB 817 là chuẩn của 6 Trục/38 Nội hàm** (8+6+6+7+7+4). File `DANH_MUC_NHIEM_VU_CHUAN...xlsx` dùng tên
  Trục/Nội hàm **khác** TB 817 — lấy TB 817, xem `KI-011`.
- **Điểm chấm thực tế là 100/120/150/180**, không có giá trị nào thuộc thang 50/120/250/350/450. Công thức
  `hệ số = điểm × 1%` đúng 211/211 dòng dữ liệu thật.
- **Phép kiểm tra mới cho kết quả "sạch" ngay lần đầu thì phải nghi ngờ chính phép kiểm.** Đã có tiền lệ:
  regex chứa ký tự backspace `0x08` vô hình nên không bao giờ khớp, báo "không có lỗi" suốt. Luôn chạy thử
  trên một ca **biết chắc là sai** trước khi tin kết quả sạch.
- **Nhãn mục con của báo cáo cấp Trường phải lấy từ nội hàm CỦA CHÍNH TRỤC đó** (TB 817), không phân loại
  tự do — nếu không sẽ sinh mục "Xây dựng Đảng" chứa mục con "Công tác đào tạo".
- **`delete_rows` của openpyxl KHÔNG gỡ vùng gộp ô.** Khi phát triển từ biểu mẫu `.xlsx` đã ban hành,
  các vùng `merge` của vùng dữ liệu cũ sẽ **trượt xuống** và rơi vào hàng dữ liệu mới, sinh ô tràn ngang
  bảng. Bắt buộc `unmerge_cells` mọi vùng có `min_row >= hàng dữ liệu đầu` **trước khi** xóa hàng; giữ
  nguyên vùng gộp của phần tiêu đề. Kiểm chứng: đếm vùng gộp phần tiêu đề phải **bằng** bản gốc, vùng gộp
  trong vùng dữ liệu phải **bằng 0**.
- **Không đưa từ chung chung vào luật chuẩn hóa chủ ngữ.** Nhánh `Ban` trần đã nuốt chữ "Ban" trong
  "**Ban hành** Kế hoạch…" → "Nhà trường hành Kế hoạch". Chỉ liệt kê tên đơn vị đầy đủ (`Ban Truyền thông`),
  không dùng từ đứng một mình trùng với động từ/danh từ thông thường.
- **Lỗi dữ liệu của đơn vị thì ghi vào cột "Ghi chú", không tự sửa** (ví dụ thời hạn `30/9/206`). Sửa hộ
  làm mất dấu vết để đơn vị rút kinh nghiệm và có thể sửa sai ý họ.
- **Đoạn nội dung của BC cấp Trường gồm HAI run**: run 1 là nhãn `* Công tác …:` (đậm + nghiêng), run 2 là
  nội dung **để thường**. Nhân bản đoạn mẫu rồi gộp thành một run sẽ làm **cả đoạn đậm nghiêng**. Khi tạo
  run nội dung phải đặt tường minh `w:b`/`w:bCs`/`w:i`/`w:iCs` = `0`, vì bỏ trống là kế thừa từ run mẫu.
  Mục II ("Kết quả đạt được", "Tồn tại, hạn chế") **không có dấu `*`**.
- **Báo cáo tháng cấp Trường**: Phần I có **7 mục** (6 trục + "Kết quả thực hiện các Nghị quyết của Bộ Chính
  trị"), mục con chia theo **lĩnh vực công tác** (`* Công tác tuyển sinh:`…) chứ không theo đơn vị, chủ ngữ
  là **"Nhà trường"**. Phụ lục đánh số phân cấp `I → 1 (Trục) → 1.1, 1.2…` có dòng cộng theo trục.

## Phiên bản hiện hành

| Thành phần | Trạng thái |
|---|---|
| Gói skill dự án | `ktc-quan-tri.skill` v1.1 (13/9/2026) |
| Gói `ktc-theo-doi-cv` | **`ktc-theo-doi-cv-v1.1.skill`** (14/9/2026 19:01) — trỏ chính thức 18/9/2026 (`DL-20260918-001`), thay `v1.0`. Bộ dữ liệu vận hành **vẫn rỗng**, mọi kết luận là dữ liệu mẫu |
| Kho đầu vào | **`10-Dau-Vao/`** (14/9/2026) — dùng chung mọi hệ, 4 nhánh theo nguồn gốc. `Nhap_Ke_Hoach/` đã bỏ; `Nhap_Bao_Cao/` **chưa chuyển** — `DL-20260914-003` |
| Thuật ngữ | **Bỏ `KTC-DIS`**, dùng "hệ thống KTC". Tên hiện vật giữ nguyên — `DL-20260914-002b` |
| Nguồn kế hoạch tháng | **4 nguồn**: KH quý · văn bản cấp trên trong kỳ · **kết luận giao ban tuần** · điều hành phát sinh. Đo được: KH quý chỉ phủ 30% — `PM-20260914-Chay-thu-KH-thang-9` |
| Gói `ktc-quan-tri` | **`ktc-quan-tri.skill`** (14/9/2026) — nguồn rời nay ở `references/` tại gốc dự án, 15 tệp |
| Bộ kiểm tra Tầng 1 | **11 phép kiểm**, 4 ca hồi quy. C5 soi cả bản trong `.skill` — `DL-20260914-002` |
| Gói `ktc-bao-cao` | **`ktc-bao-cao-v3.9.skill`** (18/9/2026) — v3.8 (Task_ID, `DL-20260918-003`) + kết cấu thư mục mới và Nguyên tắc 3 (`DL-20260918-004`). Gói cũ giữ để hoàn tác, **không dùng** |
| Gói `ktc-ke-hoach` | **`ktc-ke-hoach-v3.3.skill`** (15/9/2026) — cùng đợt hoàn tất 18/9/2026 (`DL-20260918-001`). Gói cũ (`v3.2` trở về trước) giữ lại để hoàn tác, **không dùng** |
| Cấu trúc thư mục | Nhóm theo số (18/9/2026, `DL-20260918-004`): 1x INPUT · 2x PROCESS · 3x OUTPUT · 9x quản trị. Gói: quan-tri 1.2 (`22-Dieu-Phoi/`), ke-hoach 3.4, theo-doi-cv 1.2, soan-thao-vb 1.3 |
| Plugin `ktc-quan-tri` | **0.4.0** (18/9/2026, đã cài vào cache) — 5 skill + agent `ktc-tu-cai-tien` (chỉ đề xuất) + hook tự ghi nhật ký `04-Nhat-Ky-Tu-Dong/` và nạp vào context + backup GitHub 21:00 (Task Scheduler `KTC-Quan-tri-Backup-GitHub`). Remote: `github.com/nnqp201-sys/KTC-Quan-tri` (private, tài khoản `nnqp201-sys`), push lần đầu 18/9/2026 — `DL-20260918-002`. Thư mục dữ liệu nền nay là `11-Du-lieu-Cong-Viec` (bỏ tiền tố KTC). `Claude outputs/` không backup. Build: `29-Cong-Cu/dong_goi_plugin.py` |
| Gói soạn thảo | **`ktc-soan-thao-vb-v1.2.skill`** (18/9/2026) — vá 3 tham chiếu gãy có từ trước (nguyên tắc soạn thảo bất biến, quy trình + công cụ Track Changes chưa từng nằm trong gói). Gói cũ (`v1.1` trở về trước) giữ để hoàn tác. Hệ `ktc-dis-tong-hop-vb` cũ chờ dọn thủ công |
| SKILL.md | v1.1 — bộ định tuyến 5 tác vụ |
| Lớp chuẩn chung | `20-Chuan-Chung/` — 9 tệp, 4 tệp riêng còn ở trạng thái dự thảo |
| Master Task Register | `Master-Task-Register_20260913_v0.1.xlsx` — 46 trường, sổ trống |
| Bảng mã đơn vị | 11 mã cấp một; **chưa có cấp hai**, chưa có mã cho Ban Truyền thông |

Nguồn rời và nội dung trong gói phát hành phải khớp nhau. Không suy diễn phiên bản từ tên tệp hoặc dòng
tự mô tả.

## Thứ tự ưu tiên nguồn — nguồn hạng thấp không ghi đè nguồn hạng cao

1. Văn bản pháp luật và quy định nội bộ hiện hành đã kiểm chứng.
2. `SKILL.md` và các tệp trong `20-Chuan-Chung/`.
3. Dữ liệu vận hành thật (báo cáo, kế hoạch đơn vị đã nộp).
4. Quy ước của Trường và tài liệu quản trị đã phê duyệt.
5. Nhật ký cập nhật và Release Notes.
6. Process Memory.
7. Suy luận mô hình.

Process Memory là dữ liệu tham khảo vận hành, **không phải căn cứ pháp lý**.

## Ghi Process Memory

Sau mỗi ca chốt kỳ, dựng báo cáo, hoặc thay đổi thiết kế:

1. Dùng mẫu `02-Mau-Process-Memory.md`.
2. Lưu tại `03-Process-Memory/` theo tên `PM-YYYYMMDD-[Ten-ca].md`.
3. Ghi nguồn đã đọc, kết quả, lỗi mới, giới hạn, bài học tái sử dụng được.
4. Không ghi dữ liệu cá nhân, thông tin nhạy cảm hay kết luận chưa kiểm chứng vào bộ nhớ dùng chung.
5. Chỉ cập nhật tệp MEMORY-INDEX này khi có **sự thật vận hành ổn định** hoặc đổi phiên bản hiện hành.

## Việc đang mở

Xem `92-Kinh-Nghiem/05-Known-Issues/Pending.md`. Không sao chép danh sách sang đây để tránh hai nơi lệch
trạng thái.

## Lịch sử

- Quyết định kiến trúc: `92-Kinh-Nghiem/06-Decision-Log/`
- Release notes: `92-Kinh-Nghiem/04-Release-Notes/`
- Bài học: `92-Kinh-Nghiem/01-Lessons-Learned/`
- Kết quả chạy thử: `30-Ket-Qua/<ngày>/`
