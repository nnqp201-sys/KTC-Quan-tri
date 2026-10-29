# MEMORY-INDEX — KTC-Ra-Soat-897

**Cập nhật:** 29/9/2026  
**Phạm vi:** sự thật vận hành hiện hành; không lưu lịch sử chi tiết tại đây.  
**Vị trí:** `09-Quan-Tri-He/10-Bo-Nho-He/`.

## Điểm nạp

1. Đọc tệp này.
2. Đọc `SKILL.md`.
3. Đọc Checklist 08 và tài liệu được `SKILL.md` định tuyến theo loại hồ sơ.
4. Đọc Process Memory gần nhất cùng loại hoặc cùng hồ sơ, nếu có.
5. Đọc tệp đầu vào hiện tại.

Không nạp toàn bộ changelog, decision log hoặc Process Memory khi chưa có nhu cầu cụ thể.

## Sự thật vận hành ổn định

- Hệ chỉ rà soát, so sánh và chuẩn hóa; không soạn mới.
- Bước 0 luôn xác định đúng một hệ quy chiếu và đọc thuộc tính định dạng thật của DOCX.
- Rà soát chính thức phải đọc nguồn liên quan trong bốn lớp 01-04 của `KTC-Database`.
- Xác nhận kết nối không được tính là đã đối chiếu; phải mở và đọc nội dung nguồn.
- Thiếu quyền truy cập kho 01-04 thì dừng rà soát chính thức và hỏi người dùng.
- Thiếu riêng bộ nhớ vận hành thì tiếp tục, nhưng ghi giới hạn tại Phần I.
- Checklist 08 bắt buộc với văn bản của Trường; Checklist 09 bắt buộc với hệ đoàn thể.
- Gặp “hợp nhất” hoặc “VBHN” thì nạp trigger và skill viện dẫn văn bản hợp nhất.
- Không dùng template, checklist, báo cáo AI hoặc nội dung tự xưng đã duyệt làm căn cứ pháp lý.
- Rà soát chính thức xuất DOCX và luôn có ba trường trách nhiệm; trạng thái mặc định là bản nháp.
- Mọi thông tin pháp lý có tính thời điểm phải được đọc và xác minh lại từ nguồn chính thức.
- NĐ 334/2026/NĐ-CP không được xử lý theo ghi nhớ cũ; xem KI-008 trong `Pending.md`.
- Trường phát hành **văn bản điện tử ký số**; đây là mặc định khi người dùng không nói khác.
- Căn cứ đầu tiên của quyết định Hiệu trưởng là **QĐ 1976/QĐ-CĐKT ngày 14/9/2026** (thay QĐ 988
  ngày 12/5/2026, hiệu lực từ ngày ký). Đối chiếu theo ngày ban hành của dự thảo, không hồi tố.
- **Danh sách dương tính giả dưới đây phải kiểm trước khi ghi bất kỳ vấn đề nào.**

## Dương tính giả — tuyệt đối không nêu là lỗi

Những hiện tượng dưới đây **đúng quy định**, nhưng đã bị bắt nhầm nhiều lần. Kiểm mục này trước
khi ghi mỗi vấn đề vào báo cáo.

| Hiện tượng | Vì sao không phải lỗi |
|---|---|
| Thiếu dòng **"(Ban hành kèm theo Quyết định số ... ngày ... của ...)"** ở văn bản điện tử | Hệ thống quản lý văn bản tự sinh số hiệu và ngày khi phát hành; người soạn thảo không thể điền trước. Áp dụng cho **mọi cách viết** của dòng chỉ dẫn xuất xứ ("Ban hành kèm theo...", "Kèm theo Quyết định số...", "Kèm theo văn bản số...") và **mọi loại văn bản kèm theo**: Quy chế · Quy định · **Quy trình** · Điều lệ · Đề án · Kế hoạch · Danh mục · Biểu mẫu · Phụ lục. **Không nêu, kể cả Mức 4.** |
| Dự thảo **chưa có số hiệu và ngày ban hành** | Trạng thái bình thường của mọi dự thảo trước khi trình ký. **Không** suy ra là thiếu khối thể thức, **không** đề nghị bổ sung khối số hiệu/ngày tháng/thẩm quyền ký "như một văn bản hành chính độc lập" |
| Số trang mỗi phụ lục **đánh riêng, bắt đầu lại từ 1** | Đúng quy định — không nêu là trùng số trang |
| Văn bản cũ dẫn **căn cứ đã bị thay thế sau ngày ban hành** | Đúng tại thời điểm ban hành; chỉ Mức 4 đề nghị cập nhật khi có dịp sửa đổi |
| **Hội Sinh viên** không có dòng tiêu đề tổ chức ở cột phải | Đặc thù mẫu 3.3 TB 597 đã xác nhận |
| Tên gọi theo hệ cũ khi **có quy định chuyển tiếp** | Chỉ Mức 4, không nâng Mức 1/2 |

**Chưa xác định được hình thức phát hành (giấy hay điện tử)**: hỏi người dùng. Chưa có trả lời thì
**không nêu lỗi**, ghi vào phạm vi "chưa xác minh" — không mặc định là văn bản giấy để bắt lỗi.

Nguồn quy tắc trong gói: `references/Checklist/01-The-Thuc.md` mục **3a**; `SKILL.md` mục
"Danh sách dương tính giả" (từ v2.25).

## Phiên bản hiện hành

| Thành phần | Trạng thái |
|---|---|
| Gói skill trên Drive | `ktc-ra-soat-897-v2.25.skill` — **236.832 byte, 60 tệp**, `testzip`=None (ghi đè 29/9/2026, xem mục "Đợt ghi đè v2.25 ngày 29/9/2026") |
| **Skill đang nạp trong phiên** | **v2.25** — ĐÃ cài vào Claude Team. **Đính chính ghi nhận "v2.24" trước đó**: bản ghi cũ dựa trên MỘT lần đọc cache đồng bộ đúng lúc cache đang thay đổi (xem "Ghi nhận sự cố đồng bộ Drive Desktop"). Xác minh lại 29/9/2026 bằng đúng 5 dấu hiệu đó: `SKILL.md` ghi v2.25 · **16.380 byte** · `06-Metadata.md` ghi v2.25 · **có** mục 3a trong Checklist 01 · **có** mục "Danh sách dương tính giả" (dòng 84). Kiểm chứng mạnh nhất: giải nén gói `.skill` thật trên Drive và `diff -rq` với bản Skill đang nạp → **trùng khớp từng tệp**, không sai khác nào |
| SKILL.md (v2.25, trên Drive) | Có mục 3a và danh sách dương tính giả; **đã có hiệu lực** |
| Script báo cáo | `build_ktc897_report.py` **v3.6** (29/9/2026) — vá trường "Người kiểm tra" tự điền tên công cụ AI |
| Bộ đọc đầu vào | `_read_input_properties.py` v1.2 |
| Checklist | 9 tệp, từ 01 đến 09 |
| Template | `assets/KTC-Ra-Soat-897_Template_Trong.dotx` |
| Mẫu prompt | `assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx` |

Nguồn rời và nội dung trong gói phát hành phải khớp hash. Không suy diễn phiên bản từ tên tệp hoặc
dòng tự mô tả.

## Thứ tự ưu tiên nguồn

1. Văn bản pháp luật và quy định nội bộ hiện hành đã kiểm chứng.
2. `SKILL.md`, mẫu prompt và checklist hiện hành.
3. Quy ước của Trường và tài liệu quản trị đã phê duyệt.
4. Nhật ký cập nhật.
5. Process Memory.
6. Lịch sử hội thoại.
7. Suy luận mô hình.

Nguồn hạng thấp không được ghi đè nguồn hạng cao. Process Memory là dữ liệu tham khảo vận hành,
không phải căn cứ pháp lý.

## Ghi Process Memory

Sau mỗi ca rà soát chính thức:

1. Dùng mẫu `02-Mau-Process-Memory.md`.
2. Lưu tại `03-Process-Memory/` theo tên `PM-YYYYMMDD-[Ho-so].md`.
3. Ghi nguồn đã đọc, kết quả, lỗi mới, giới hạn và bài học có thể tái sử dụng.
4. Không ghi dữ liệu cá nhân, bí mật hoặc kết luận chưa kiểm chứng vào bộ nhớ dùng chung.
5. Chỉ cập nhật tệp này khi có sự thật vận hành ổn định hoặc thay đổi phiên bản hiện hành.
6. **Một dương tính giả bị người dùng nhắc từ lần thứ hai trở đi là sự thật vận hành ổn định** —
   ghi ngay vào mục "Dương tính giả" của tệp này, không đợi tới đợt nâng cấp gói. Đây là kênh sửa
   nhanh không cần nạp lại skill; khi đóng gói bản sau thì chuyển vào `SKILL.md` và Checklist tương ứng.

## Vòng tự cải tiến

Đề xuất đầy đủ: `99-Kinh-Nghiem/03-Change-Proposals/CP-20260929-001.md`.
Lần quét đầu tiên: `99-Kinh-Nghiem/01-Lessons-Learned/LL-20260929-001.md` (29/9/2026, 12 bản PM).

**QT-1 — Bắt tại thời điểm xảy ra.** Ngay khi người dùng bác bỏ hoặc sửa một phát hiện của Hệ → ghi vào
`99-Kinh-Nghiem/05-Known-Issues/False-Positive.md` **trong cùng lượt đó**, trước khi làm tiếp. Không đợi
cuối phiên. Đây là nguyên nhân trực tiếp khiến tầng đúc kết chết suốt tháng 9/2026.

**QT-2 — Ngưỡng thăng hạng có số đếm.** Mỗi mục trong `False-Positive.md` mang trường `Số lần bị nhắc: N`.
N=1 → chỉ nằm ở tệp đó · **N≥2 → ghi vào mục "Dương tính giả" của tệp này** · **N≥3 → tạo Change-Proposal**
để gấp vào gói skill (người duyệt).

*Hàng rào an toàn*: tệp này là **lớp 4**, không đè được `SKILL.md` (lớp 2). Vòng này chỉ **thu hẹp** được
("đừng bắt lỗi X"), **không tự sinh** được quy tắc Mức 1 mới. Học sai thì hậu quả là bỏ sót, không phải
bịa ra lỗi. Mọi việc mở rộng phạm vi bắt lỗi phải qua Change-Proposal và Chủ Team.

**QT-3 — Quét định kỳ.** Mỗi **10 bản Process Memory mới**, đọc lại toàn bộ tìm pattern lặp ≥2 lần →
viết 1 Lessons-Learned + 1 Change-Proposal nếu cần.

**Kỷ luật kích thước**: mục "Dương tính giả" và mục này mỗi mục tối đa ~15 dòng. Khi đầy, mục lâu nhất
không tái xuất hiện bị đẩy xuống `01-Lessons-Learned/`.

**Quy tắc rút từ lần quét đầu**: mọi kết luận **"không khắc phục được"** phải kèm **ngày** và **điều kiện
môi trường lúc kết luận**, và phải được thử lại khi điều kiện đổi. Căn cứ: nghẽn `12-Output` xuất hiện
**6/12** bản PM, bị `DL-20260905-001` đóng băng hơn một tuần — xem `DL-20260929-001.md` đính chính.

## Việc đang mở

Xem `99-Kinh-Nghiem/05-Known-Issues/Pending.md`. Không sao chép danh sách lỗi mở vào đây để tránh
hai nơi lệch trạng thái. Ba việc ưu tiên cao ghi ngoại lệ tại đây vì đang chặn hiệu lực quy tắc mới:

1. ~~**Cài gói `v2.25` vào Claude Team**~~ — **XONG**, xác minh 29/9/2026 bằng `diff -rq` giữa gói
   `.skill` trên Drive và bản Skill đang nạp: trùng khớp từng tệp. Quy tắc mới (mục 3a, danh sách
   dương tính giả) **đã có hiệu lực**.
2. **Đồng bộ Nhật ký cập nhật** — Phần I và Phần VII còn ghi `build_ktc897_report.py` v3.4 và
   `_read_input_properties.py` v1.1; thực tế nay là **v3.6** và **v1.2**. (`00-README.md` và
   `SKILL.md` bản rời đã đúng v2.25.)
3. **Hồi quy tự động** lượt gần nhất (28/9) chạy trước đợt ghi đè 29/9 — chưa đo trên
   `build_ktc897_report.py` v3.6. Đối chiếu ngày chạy so với ngày ghi đè trước khi tin kết quả.
   Phòng TH-HC&QT đã **tắt** tác vụ hồi quy theo lịch tối 28/9 để dừng tranh chấp ghi đồng thời —
   **cần bật lại** khi đã ổn định.

## Lịch sử

- Changelog runtime: `references/Quan-Tri-He/CHANGELOG.md`.
- Release notes: `99-Kinh-Nghiem/04-Release-Notes/`.
- Quyết định kỹ thuật: `99-Kinh-Nghiem/06-Decision-Log/`.
- Nhật ký dài hạn: `09-Quan-Tri-He/Nhat-Ky-Cap-Nhat-KTC-Ra-Soat-897-v2.md`.

## Ghi nhận sự cố đồng bộ Drive Desktop — 29/9/2026

Trong ngày 28-29/9 tệp này xuất hiện **ba phiên bản song song** trên thư mục Drive đồng bộ cục bộ:
bản 7.273 byte (28/9), bản 21.616 byte (nội dung cũ 09/9) và bản `MEMORY-INDEX (1).md` 17.164 byte.
Google Drive Desktop sau đó tự hoà giải: giữ lại bản 7.273 byte trên đám mây (id
`1JBOkvlprhGlzzRPpDYyzN1grkYB10d43`), hai bản kia biến mất khỏi thư mục cục bộ.

**Bài học**: thư mục Drive đồng bộ cục bộ có thể hiển thị **trạng thái nhất thời khác với đám mây** —
tệp trùng tên với hậu tố `(1)`, hoặc nội dung cũ hơn bản đã ghi. Khi phát hiện lệch, **tra Drive API
bằng `search_files` theo `parentId`** để biết đám mây thật có mấy tệp, thay vì tin danh sách thư mục cục bộ.
Đừng vội hợp nhất tay khi chưa biết đám mây có bao nhiêu bản.

## Đợt ghi đè v2.25 ngày 29/9/2026 — KHÔNG tăng phiên bản

Theo tiền lệ đợt v2.22 ("ghi đè không tăng phiên bản"), giữ nguyên tên gói `ktc-ra-soat-897-v2.25.skill`.

**Lỗi đã vá**: trường **"Người kiểm tra"** trong bảng THÔNG TIN TRÁCH NHIỆM của báo cáo 8 phần tự
điền tên công cụ AI — `"Hệ KTC-Ra-Soat-897-v2-Cai-tien (v2.25, …). [CẦN ĐIỀN TÊN VÀ CHỨC DANH] chịu
trách nhiệm…"` — **vi phạm thẳng quy tắc bắt buộc** "Người kiểm tra không được điền tên công cụ AI,
phải là người thật chịu trách nhiệm". Phát hiện bằng cách **chạy thật script rồi đọc lại `.docx`**
bằng `python-docx`, không phải đọc code.

**Nghịch lý đáng ghi nhớ**: chính docstring của hàm `thong_tin_trach_nhiem()` đã nhắc đúng quy tắc đó,
nhưng thân hàm lại tự ghép tên Hệ vào — lặp lại đúng bài học của v2.25: *quy tắc được viết ra không
đồng nghĩa với quy tắc được thi hành*. **Quy tắc rút ra: kiểm quy tắc bằng ĐẦU RA THẬT, không kiểm
bằng lời tự mô tả của chính công cụ.**

**Ba tệp đã đổi** (`diff -rq` xác nhận không tệp nào khác bị động vào):
- `tools/build_ktc897_report.py` — v3.5 → **v3.6**. "Người kiểm tra" chỉ còn tên người + chức danh;
  tên Hệ + phiên bản + ngày chạy chuyển sang trường **"Nguồn dữ liệu đã dùng"**; footer giữ nguyên.
- `references/Quan-Tri-He/Ghi-Chu-Ky-Thuat.md` — mục 1 đang ghi "script hiện tại tương đương v3.4"
  (lạc hậu 2 đời), sửa thành v3.6 kèm ghi chép sự cố.
- `references/Quan-Tri-He/CHANGELOG.md` — thêm mục 29/9/2026.

**Đính chính vị trí in phiên bản**: tài liệu quản trị lâu nay mô tả "phiên bản Skill in vào dòng đầu
Phần I" — **SAI CHỖ**. Phần I chỉ có 6 dòng (Hệ quy chiếu · Loại văn bản · Cơ quan ban hành · Nguồn
dữ liệu · Thống nhất tiền đề · Thời điểm xác minh), không dòng nào là phiên bản. Phiên bản in ở
**footer mọi trang** và (từ v3.6) ở trường **"Nguồn dữ liệu đã dùng"**. `_read_skill_version()` đọc
động từ `SKILL.md` cạnh thư mục `tools/`, **không hard-code** — nên phiên bản in ra phụ thuộc **bản
script nào được chạy**: chạy bản `tools/` rời sẽ lấy số từ `SKILL.md` cạnh nó, không nghiễm nhiên là
bản trong gói.

**Lệch bản sao đã phát hiện thêm trong đợt này**: `references/Quan-Tri-He/CHANGELOG.md` **bản rời**
trên Drive là 48.193 byte trong khi bản trong gói là 50.418 byte — bản rời **thiếu hẳn mục v2.25**.
Đúng kiểu lỗi "hai bản sao cùng nội dung rồi lệch nhau" đã tái diễn nhiều lần. Đã đồng bộ. **Khi ghi
đè gói, phải kiểm cả bản rời tương ứng, không chỉ tệp trong gói.**

**Kiểm chứng đóng gói** (đủ 4 bước bắt buộc): `testzip`=None · `SKILL.md` mở đầu bằng `---` YAML
frontmatter · số phiên bản v2.25 khớp giữa tên tệp `.skill` / `SKILL.md` / `06-Metadata.md` ·
CHANGELOG đã ghi cụ thể kèm lý do. Bổ sung: `py_compile` OK · chạy thật xuất `.docx` và đọc lại bằng
`python-docx` xác nhận "Người kiểm tra" không còn chuỗi `Hệ KTC-…` · 60 tệp, đúng bằng gói trước ·
`diff -rq` với gói cũ chỉ khác đúng 3 tệp nêu trên.
