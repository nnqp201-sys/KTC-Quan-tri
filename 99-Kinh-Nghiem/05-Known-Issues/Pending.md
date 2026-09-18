# Known Issues — KTC-Quan-tri

Lỗi và khoảng trống **đã biết nhưng chưa xử lý**. Ghi lại để không quên và không tốn công phát hiện lại.

**Cập nhật:** 13/9/2026

---

## Đã giải quyết

Xem lịch sử ở cuối tệp (mục "Resolved"). Danh sách còn mở dưới đây.

## KI-001 — Phụ lục Ia/Ib chưa có cột `Task_ID`

**Status:** Open · **Priority:** Cao — chặn toàn bộ khả năng đối chiếu tự động

Nguồn dữ liệu kế hoạch (Phụ lục Ia/Ib của TB736) không có cột mã nhiệm vụ, nên kế hoạch và báo cáo chỉ đối
chiếu được **gần đúng** theo Trục + so khớp tên nhiệm vụ.

**Đã chứng minh tác hại thật:** khi duyệt ngược 19 nhiệm vụ đến hạn tháng 8/2026, có 7 nhiệm vụ "không tìm
thấy", trong đó nhiệm vụ 2.8 thực tế **đã hoàn thành** (QĐ 1923/QĐ-CĐKT ngày 30/8/2026) — chỉ là tên trong
báo cáo diễn đạt khác.

**Cách khắc phục:** `KTC-Ke-Hoach` bổ sung cột `Task_ID` vào Phụ lục Ia/Ib → `KTC-Bao-Cao` sửa
`read_bc736_excel.py` dùng cột này làm khóa nối.

**Workaround hiện tại:** mọi kết quả đối chiếu bắt buộc tự khai là "đối chiếu gần đúng".

**Bằng chứng định lượng bổ sung 14/9/2026** (`PM-20260914-Chay-thu-KH-thang-9`): đối chiếu `KH-834` với
Kế hoạch quý III cho **5 cặp khớp giả** ở ngưỡng 63–80% — khác số hiệu văn bản nhưng cùng khuôn chữ:
TT 64/2026 vs TT 43/2026 · TT 66/2026 vs TT 43/2026 · TT 59/2026 vs TT 43/2026 · NĐ 271/2026 vs
NĐ 159/2026 · Chiến lược Khoa KHCB vs Chiến lược Khoa Sư phạm.

Nếu lấy ngưỡng 60% làm chuẩn khớp thì cả 5 đều bị tính nhầm là "đã có trong kế hoạch quý". Nguyên nhân:
nhiệm vụ hành chính dùng khuôn chữ lặp lại, phần phân biệt chỉ là số hiệu và ngày ban hành — chiếm tỷ lệ
nhỏ trong câu. **Kết luận: không dùng ngưỡng dưới 100% cho bất kỳ đối chiếu tự động nào.**

---

## KI-002 — Danh mục 122 nhiệm vụ chuẩn chưa phủ 6 Khoa

**Status:** Open — người dùng xác nhận **sẽ bổ sung sau** · **Priority:** Cao

1.358 nhiệm vụ gốc chỉ đến từ 5 Phòng (TH-HC&QT 402, QLKHCN&HTPT 387, QLĐT&BĐCL 366, Phòng Tổ chức 126,
TC-KT 77). Lĩnh vực `S. Nhiệm vụ chuyên môn nhà giáo` chỉ có 4 mã, sinh từ viên chức Phòng có giảng dạy.

**Workaround:** nhiệm vụ của Khoa không khớp mã nào thì để trống `Ma_NV_Chuan`, đề nghị bổ sung mã mới.
Tuyệt đối không ép về mã gần đúng.

---

## KI-003 — Bảng mã đơn vị chỉ có một cấp

**Status:** Open · **Priority:** Trung bình

Cột "Đơn vị chủ trì" trong dữ liệu thật chứa cả bộ phận nội bộ và nhóm người: `Ban Truyền thông` (19×),
`Nhà giáo` (6×), `Các bộ môn và nhà giáo` (4×), `Bộ môn CK&XD` (4×), `Giáo vụ khoa` (3×), `Chi bộ khoa` (2×),
`Các lớp sinh viên` (2×)… — tổng 60 dòng ở 4 đơn vị không ánh xạ được.

**Cần:** cấp mã thứ hai (bộ môn · tổ · ban · chức danh), mỗi giá trị trỏ về đúng một mã đơn vị cấp một.

---

## KI-004 — Ban Truyền thông chưa có mã đơn vị

**Status:** Resolved 13/9/2026 · **Xem:** `00. Mau bao cao thang (cap Truong).docx`, mục "Công tác Truyền
thông: […lấy kết quả thực hiện công tác truyền thông của Ban Truyền thông, thuộc phòng TH-HC&QT]"

Mẫu báo cáo chính thức cấp Trường xác nhận: **Ban Truyền thông là bộ phận cấp hai, trực thuộc Phòng
TH-HC&QT** — không phải đơn vị cấp một, không cần mã riêng.

**ĐÓNG HOÀN TOÀN 14/9/2026.** Người phụ trách hệ xác nhận: tệp `Phong-THHCQT/BAN TT.xlsx` **nằm đúng chỗ
theo chủ đích** — nhiệm vụ của Ban Truyền thông được tổng hợp chung vào thư mục của Phòng TH-HC&QT để lấy
thông tin, dữ liệu về công tác truyền thông. Quy ước đã chốt: **đơn vị cấp hai nộp vào cùng thư mục đơn vị
cấp một**, không dùng thư mục con riêng.

Đã ghi vào `01-Chuan-Chung/13-Bang-Ma-Don-Vi.md`. Ban Truyền thông **không phải đầu mối nộp báo cáo riêng**
— số đầu mối là **13**, không phải 14.

---

## KI-005 [ĐÃ ĐÓNG 14/9/2026 — hợp nhất thành `ktc-bao-cao-v3.5.skill`, 36 tệp, là tập cha của cả hai nhánh]

## KI-005 (nội dung gốc) — Hai nhánh `.skill` của KTC-Bao-Cao chưa hợp nhất

**Status:** Open · **Priority:** Trung bình · **Xem:** `DL-20260913-001`

`ktc-bao-cao-v3.4.skill` có nghiệp vụ mới hơn (Skill 31 đọc Excel TB736); `ktc-bao-cao-v2_5_1-memory.skill`
cập nhật muộn hơn 2 ngày và giữ trọn lớp `references/Memory/` mà bản kia không có. Nhật ký bên trong nhánh
memory tự ghi *"Còn treo: Gộp v3.1"*.

**Workaround:** giữ cả hai, không lưu trữ bản nào. Xem `KTC-Bao-Cao/00-TRANG-THAI-GOI-SKILL.md`.

---

## KI-006 — Bốn lỗi thể thức hồ sơ tháng 8/2026 chưa khắc phục

**Status:** Open · **Priority:** Cao — chặn việc chốt kỳ tháng 8 · **Xem:** `PM-20260913-001`

| Đơn vị | Lỗi |
|---|---|
| Phòng TH-HC&QT | Thư mục chỉ có báo cáo của Ban Truyền thông (mảng truyền thông), chưa thấy báo cáo của Phòng với tư cách đơn vị — mảng văn thư, hành chính, quản trị, cơ sở vật chất. *Vị trí tệp là đúng chủ đích, xem `KI-004`; vấn đề là thiếu phần còn lại.* |
| Phòng TCCB | Nộp "BÁO CÁO kết quả tháng 9" thay vì kế hoạch tháng 9; dùng sai Phụ lục IIb |
| Khoa KT-CN | Sai cấu trúc cột — cột (8) là "Thời gian hoàn thành" thay vì "Điểm chấm công việc" |
| Khoa Sư phạm | Tiêu đề tự chế, chỉ 7 nhiệm vụ so với trung bình 25 |

Kèm theo: Khoa CKHCB và Khoa KT-NL thiếu mục Trục 2 và Trục 5; 5 tệp còn để nguyên sheet mẫu trống.

---

## KI-007 — Sai lệch số liệu trong danh mục sản phẩm

**Status:** Open · **Priority:** Thấp

Sheet `Tong hop theo Truc` ghi Trục 1 có **102** sản phẩm, nhưng cộng theo nhóm trên chính dòng đó ra
**103** (54+37+7+4+1), và đếm trực tiếp trên sheet dữ liệu cũng ra 103. Lệch 1 sản phẩm, chưa rõ nguyên
nhân. Không tự ý sửa nguồn.

---

## KI-008 — Chưa xác minh "phần mềm KPI"

**Status:** Đã xác định tên, còn treo phạm vi · **Priority:** Cao trước khi số hóa quy trình
**Cập nhật 14/9/2026** (từ `PM-20260914-Chay-thu-KH-thang-9`): `KH-834/KH-CĐKT` ngày 6/9/2026 có nhiệm vụ
*"Ban hành kế hoạch triển khai phần mềm **VNPT KPI** - Hệ thống quản lý đánh giá, xếp loại..."*.

→ Phần mềm KPI mà QĐ 1923 dẫn chiếu là **VNPT KPI**. Tính đến 6/9/2026 Trường **mới đang lập kế hoạch
triển khai**, chưa vận hành — nên nguy cơ Master Task Register làm trùng chức năng là **chưa xảy ra**,
nhưng sẽ xảy ra nếu VNPT KPI đi vào vận hành trước khi Register chốt.

**Còn phải xác minh:** VNPT KPI quản lý tới đâu (chỉ chấm điểm cá nhân, hay cả giao việc và theo dõi tiến
độ?), và có API/xuất dữ liệu được không. Chưa có tài liệu nào trong kho trả lời.

<details><summary>Nội dung gốc</summary>

**Status:** Open · **Priority:** Cao trước khi số hóa quy trình

Quy chế ban hành kèm QĐ 1923/QĐ-CĐKT dẫn chiếu việc viên chức tự đánh giá và cho điểm "thực hiện trên
**phần mềm KPI**". Chưa biết phần mềm đó là gì và quản lý tới đâu. Nếu nó đã quản lý chỉ tiêu KPI theo quý
thì Master Task Register có nguy cơ làm trùng chức năng.

</details>

---

## KI-011 — Danh mục nhiệm vụ chuẩn lệch tên Trục/Nội hàm với TB 817

**Status:** Open · **Priority:** Cao — ảnh hưởng mọi phân loại

`KTC-Du-lieu-Cong-Viec/DANH MUC SAN PHAM CONG VIEC/Bang tong hop_phan tich_DANH_MUC_NHIEM_VU_CHUAN_TRUC_NOI_HAM_HE_SO.xlsx`
(122 nhiệm vụ, dự thảo lần 4) dùng tên Trục và Nội hàm **khác** `TB 817/TB-CĐKT` ngày 14/7/2026.
Ví dụ Trục 1: TB 817 ghi "Thực hiện mục tiêu phát triển kinh tế – xã hội và nhiệm vụ chính trị được giao",
file danh mục ghi "Lãnh đạo thực hiện nhiệm vụ chính trị". Nội hàm 3 Trục 4 cũng khác tên.

Hiện lấy TB 817 làm chuẩn (văn bản đã ban hành; BC-375 cũng đặt tiêu đề theo TB 817). Cần rà soát, cập nhật
file danh mục cho khớp, hoặc xác nhận đây là hai hệ phân loại khác nhau dùng cho hai mục đích khác nhau.

---

## KI-012 — Tiêu chí chọn nhiệm vụ vào phụ lục cấp Trường

**Status:** ĐÃ GIẢI 14/9/2026 bằng bằng chứng đo được — đã ghi vào Skill 33 v2.4 và Skill 36 v2.0

**Kết luận:** phụ lục cấp Trường **không tổng hợp từ báo cáo đơn vị** mà báo cáo lại **kế hoạch công tác của
chính Trường** (dẫn xuất từ Kế hoạch quý). Phụ lục tháng 7 khớp Kế hoạch quý III **39/41 = 95%**; tháng 8
khớp 26/40 = 65%, phần còn lại là nhiệm vụ phát sinh. Kèm điều kiện lọc: chỉ nhiệm vụ do lãnh đạo cấp Trường
trực tiếp chỉ đạo (đúng 100% trên cả ba văn bản đã ban hành).

**Còn lại để kiểm chứng khi có dữ liệu:** cần một kỳ có đủ cả Kế hoạch tháng của Trường và Phụ lục kết quả
cùng kỳ để xác nhận tỷ lệ khớp ~100%. Hiện chỉ có Kế hoạch quý làm trung gian.

<details><summary>Nội dung cũ</summary>

**Status:** Open · **Priority:** Cao — chặn việc tự động hóa chốt kỳ

Lọc theo "người trực tiếp chỉ đạo là lãnh đạo cấp Trường" cho **211** nhiệm vụ tháng 8, trong khi `PL-375`
đã ban hành chỉ có **39**; kế hoạch tháng 9 cho 94 so với 53 của `KH-834`. Tiêu chí lọc đã kiểm chứng là
**cần nhưng chưa đủ**.

Hai giả thuyết chưa kiểm chứng: (a) chỉ lấy nhiệm vụ có trong Kế hoạch quý III đã duyệt; (b) gộp nhiệm vụ
trùng nội dung do nhiều đơn vị cùng báo cáo. **Không được tự đặt tiêu chí cắt bớt** — cắt sai làm biến mất
công việc có thật. Cần hỏi người trực tiếp tổng hợp báo cáo tháng của Trường.

→ *Giả thuyết (a) đã được xác nhận bằng phép đo.*

</details>

---

## KI-013 — Gói `.skill` chưa đóng lại sau khi sửa nguồn

**Status:** ĐÃ ĐÓNG 14/9/2026 — ba gói đã đóng lại: `ktc-bao-cao-v3.6.skill`, `ktc-ke-hoach-v3.2.skill`,
`ktc-soan-thao-vb.skill`. Nguyên nhân gốc (phép kiểm C5 không soi vào trong gói) đã sửa kèm ca thử ngược —
xem `DL-20260914-002`. Cảnh báo C4 còn lại là hành vi bình thường của cơ chế đóng gói, không phải lỗi.

<details><summary>Nội dung gốc</summary>

**Status:** Open · **Priority:** Cao

Đã sửa 5 tệp nguồn của `KTC-Bao-Cao` và `KTC-Ke-Hoach` (xem `PATCH-NOTES-v2.5.md`). Các gói
`ktc-bao-cao-v3.4.skill`, `ktc-bao-cao-v2_5_1-memory.skill`, `ktc-ke-hoach.skill` **vẫn là bản cũ** — chạy
trên Claude Chat/Cowork sẽ dùng quy tắc sai. Cần đóng gói lại, và xử lý luôn `KI-005` (hai nhánh
`ktc-bao-cao` chưa hợp nhất).

</details>

---

## KI-014 — Hai thang điểm quy đổi cùng tồn tại, chưa có văn bản phân định

**Status:** Open · **Priority:** Cao — ảnh hưởng mọi phép quy đổi khối lượng công việc
**Phát hiện:** 14/9/2026, khi đồng bộ `30-Skill-Phan-Loai-6-Truc.md` giữa bản gốc và gói `.skill`

Dự án đang mang **hai thang điểm khác nhau** cho cùng khái niệm "quy đổi khối lượng công việc":

| | Thang 4 mức | Thang 5 nhóm |
|---|---|---|
| Điểm | 100 · 120 · 150 · 200 | 50 · 120 · 250 · 350 · 450 |
| Hệ số | 1,0 · 1,2 · 1,5 · 2,0 | 0,5 · 1,2 · 2,5 · 3,5 · 4,5 |
| Nguồn | Bản `30-Skill-Phan-Loai-6-Truc.md` nằm trong `ktc-bao-cao.skill` | `CLAUDE.md` và `Du thao_Danh_muc_SP_theo_loai_van_ban_va_6_truc.xlsx` |

**Đã đo trên dữ liệu thật (14/9/2026):** thang 4 mức xuất hiện ở **mọi cấp** — 800 dòng của 27 tệp đơn vị
kỳ T8–T9/2026, phụ lục cấp Trường 39 nhiệm vụ, và Kế hoạch công tác Quý III/2026 đã duyệt. **Thang 5 nhóm
không xuất hiện dòng nào** trong dữ liệu vận hành.

**Đã xử lý tạm:** khôi phục thang 4 mức vào `01-Chuan-Chung/30-Skill-Phan-Loai-6-Truc.md` kèm bảng bằng
chứng và ghi chú phân định phạm vi: thang 4 mức dùng cho cột (9)(10) Phụ lục TB736; thang 5 nhóm thuộc
danh mục sản phẩm theo loại văn bản, hiện mới là dự thảo lần 4.

**Chưa giải quyết — cần người có thẩm quyền quyết định:**
1. Hai thang là hai hệ quy đổi độc lập cho hai mục đích khác nhau, hay thang 5 nhóm dự kiến **thay thế**
   thang 4 mức khi danh mục sản phẩm được ban hành? Trả lời khác nhau dẫn tới thiết kế Master Task Register
   khác nhau.
2. Nếu là hai hệ độc lập thì một nhiệm vụ vừa nằm trong Phụ lục TB736 vừa quy đổi theo danh mục sản phẩm
   sẽ có **hai điểm số khác nhau** — cần quy tắc chọn hoặc quy tắc chuyển đổi.

**Không tự đặt quy tắc chuyển đổi giữa hai thang.** Điểm quy đổi gắn với đánh giá viên chức.

**Liên quan:** `KI-011` (lệch tên Trục/Nội hàm) · `CP-20260914-001` mục 2.2

---

## KI-009 — Chưa có công cụ dựng Track Changes dùng lại được

**Status:** ĐÃ ĐÓNG 13/9/2026 — `tools/ktc_trackchanges.py` + `01-Chuan-Chung/15-Skill-Track-Changes.md`

Chuẩn kỹ thuật Track Changes đã thành văn đầy đủ trong hệ 897
(`Bo-Sung-Chuan-Hoa-TrackChanges-MauChu-PhienBanSkill_20260825.md`), nhưng **không có script dựng sẵn**:
thư mục `897/tools/` chỉ có `_read_input_properties.py`, `build_ktc897_report.py` và hai tệp test. Chính
tài liệu chuẩn có nhắc chạy `validate.py` trước khi giao file — **tệp này không tồn tại trong kho**.

Hệ quả: mỗi lần cần Track Changes phải viết lại thao tác OOXML từ đầu, trong khi tài liệu đã cảnh báo hai
lỗi dễ mắc (thứ tự phần tử trong `<w:trPr>`; `rPr` lồng nhau / `xml:space` trùng). Rủi ro tái phạm cao.

**Đã làm:** mô-đun `tools/ktc_trackchanges.py` — 4 thao tác sửa, validator 7 lỗi (thay cho `validate.py`
còn thiếu), `nhat_ky_sua_doi()` đọc được cả file do người sửa trong Word, `doi_chieu_goc()` phát hiện
trường hợp soạn lại từ đầu. Regression: `99-Kinh-Nghiem/02-Regression/Cases/test_trackchanges.py`.

**Còn treo:** đề xuất đưa ngược mô-đun về `897/tools/` để hệ 897 dùng chung — chưa làm.

---

## KI-010 — Chưa có nhật ký đợt chạy thử trên Claude Chat

**Status:** Open · **Priority:** Trung bình

Người phụ trách hệ cho biết `ktc-bao-cao` và `ktc-ke-hoach` **đã chạy thử trên Claude Chat**. Dự án
**chưa có bất kỳ ghi chép nào** về đợt chạy đó: chạy tác vụ gì, đầu vào nào, đầu ra đạt/không đạt ở đâu.

Đây là dữ liệu vận hành có giá trị cao nhất hiện có (bằng chứng thật về hành vi của skill trên nền tảng
khác Code) nhưng đang nằm ngoài hệ. Không được suy đoán kết quả.

**Cần làm:** lấy transcript hoặc ghi lại theo mẫu `03-Nhat-Ky-Van-Hanh/02-Mau-Process-Memory.md`, đặc biệt
ghi các điểm skill **không chạy được trên Chat** do thiếu `python-docx`/`openpyxl`.
