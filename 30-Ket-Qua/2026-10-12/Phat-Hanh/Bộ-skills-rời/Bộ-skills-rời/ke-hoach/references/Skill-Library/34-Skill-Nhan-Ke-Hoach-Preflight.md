# 34-Skill-Nhan-Ke-Hoach-Preflight
**Phiên bản: 2.0 — 12/8/2026**

## Purpose
Kiểm soát "cổng vào" của hệ KTC-PIS trước khi chạy Skill 35: xác nhận đủ điều kiện đầu vào (đủ đơn vị nộp theo kỳ, đúng mẫu tên file, có kế hoạch cấp trên, kết nối 01-04), phân loại tài liệu vào đúng luồng (A/B/C). Nếu pre-flight FAIL → chặn, không chạy Skill 35.

## Khi nào dùng
- Bắt đầu một kỳ tổng hợp mới (năm/quý/tháng/chuyên đề).
- Khi đầu mối nộp hồ sơ vào `10-Dau-Vao/01-Dau-Moi-Nop/<kỳ>/`.
- Khi cần nhập hồi tố kế hoạch đã ban hành vào `KH-Cap-Tren/`.

---

## PHẦN A — Vị trí dữ liệu đầu vào

> **[SỬA 14/9/2026] Đổi kho.** Cấu trúc cũ `Nhap_Ke_Hoach/input-KH_<kỳ>/<Tên-Don-Vi>/` **đã bỏ**. Toàn bộ
> dữ liệu đầu vào nay nằm ở kho dùng chung cấp dự án `10-Dau-Vao/` — đọc
> `10-Dau-Vao/00-README.md` trước khi chạy Pre-flight.
>
> Lý do đổi: 14/15 thư mục đơn vị của `input-KH_Nam` và 13/14 của `input-KH_Quy` bỏ trống, trong khi 12 tệp
> kế hoạch tháng 9/2026 thật lại nằm ở nhánh của hệ Báo cáo — vì đơn vị nộp gộp kế hoạch và báo cáo cùng
> một lần. Kho mới tổ chức theo **nguồn gốc dữ liệu**, không theo hệ tiêu thụ.

### A1. Bốn nhánh của kho đầu vào

| Nhánh | Chứa gì | Vai trò với Pre-flight |
|---|---|---|
| `01-Dau-Moi-Nop/<kỳ>/<mã đầu mối>/` | Hồ sơ 13 đầu mối nộp theo kỳ | **Luồng A** — đề xuất của đơn vị |
| `02-Cap-Truong/<nhóm kỳ>/<kỳ>/` | Văn bản cấp Trường đã ban hành (CTCT năm, KH quý, KH tháng, BC) | **Luồng B** — căn cứ cấp trên trực tiếp; nguồn 1 của kế hoạch tháng |
| `KTC-Database/01-Legal-Database/` (nạp qua `KTC-Database/11-Input/`) | Văn bản chỉ đạo của UBND tỉnh, Tỉnh ủy, Bộ… — **không** lưu trong `10-Dau-Vao` | **Luồng B/C** — nguồn 2 của kế hoạch tháng |
| `03-Ket-Luan-Giao-Ban/<năm>/` | Thông báo kết luận giao ban tuần của Lãnh đạo Trường | **Nguồn 3** của kế hoạch tháng — mới, xem Skill 36 |

> `<nhóm kỳ>` của `02-Cap-Truong/`: `01-Nam/` (kỳ `YYYY`) · `02-Quy/` (`YYYY-Qn`) · `03-Thang/` (`YYYY-MM`) · `04-Chuyen-De/` (`YYYY-CD-<tên-ngắn>`). Văn bản cấp trên **không** lưu ở `10-Dau-Vao` — đọc tại `KTC-Database/01-Legal-Database/` (DL-20260918-005).


**Quy ước tên kỳ:** năm `YYYY` · quý `YYYY-Qn` · tháng `YYYY-MM` · chuyên đề `YYYY-CD-<tên-ngắn>`.

### A2. 13 mã đầu mối — dùng MÃ CHUẨN, không dùng tên tự do

`P-THHC` · `P-TCCB` · `P-QLDT` · `P-TCKT` · `P-QLKH` · `K-YDUOC` · `K-KTCN` · `K-KTNL` · `K-SUPH` ·
`K-KHCB` · `K-DTSHLX` · `DT-CDCS` (Công đoàn cơ sở) · `DT-DTN` (Đoàn TN – Hội Sinh viên).

Bảng ánh xạ tên đầy đủ và các biến thể đang tồn tại: `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`.
Ban Truyền thông **không** là đầu mối riêng — hồ sơ để trong `P-THHC/` (xem `KI-004`).

### A3. Kỳ CHUYÊN ĐỀ

Kế hoạch chuyên đề do Ban Giám hiệu chỉ đạo hoặc phát sinh đột xuất — **KHÔNG** thu đề xuất từ 5 Phòng và
6 Khoa chuyên môn. Với kỳ `YYYY-CD-<tên-ngắn>`, chỉ chấp nhận:

| Vị trí | Mục đích |
|---|---|
| `01-Dau-Moi-Nop/<kỳ>/DT-CDCS/` | Kế hoạch hoạt động chuyên đề của Công đoàn |
| `01-Dau-Moi-Nop/<kỳ>/DT-DTN/` | Kế hoạch hoạt động chuyên đề của Đoàn Thanh niên |
| `KTC-Database/01-Legal-Database/` | KH/Chỉ thị cấp trên làm căn cứ chuyên đề |
| `02-Cap-Truong/<nhóm kỳ>/<kỳ>/` | Dự thảo KH chuyên đề cấp Trường do Phòng TH-HC&QT chủ trì |

> ⚠️ Nếu thấy thư mục của Phòng/Khoa chuyên môn trong một kỳ chuyên đề → **cảnh báo**, không tự xử lý.

### A4. Thư mục rỗng KHÔNG còn là dấu hiệu "chưa nộp"

Kho mới **chỉ tạo thư mục khi có dữ liệu**. Vì vậy đầu mối chưa nộp thì **không có thư mục**, chứ không
phải có thư mục rỗng. Pre-flight phải đối chiếu với **danh sách 13 mã** ở A2, không đếm thư mục đang có.

---

## PHẦN B — 3 Luồng tiếp nhận

### Luồng A — Đề xuất mới (chưa ban hành)
- Áp dụng: kỳ Năm/Quý/Tháng
- Vị trí: `10-Dau-Vao/01-Dau-Moi-Nop/<kỳ>/<mã đầu mối>/`
- Tên file: `DX_[kỳ]_[YYYY hoặc YYYY-QN hoặc YYYY-MM]_[Ten-Don-Vi]_v[N].docx`
  - Ví dụ: `DX_Thang_2026-09_Phong-THHCQT_v1.docx`
  - Ví dụ: `DX_Quy_2026-Q4_Khoa-Y-Duoc_v1.docx`
- Định dạng chấp nhận: **`.docx` hoặc `.xlsx` chỉ** — từ chối `.pdf` scan, `.md`, `.txt`, ảnh chụp
- Sau pre-flight PASS → Skill 35 xử lý

### Luồng B — Kế hoạch đã ban hành (cấp trên/chỉ đạo, dùng cho Skill 37)
- Áp dụng: mọi kỳ, kể cả Chuyên đề
- Vị trí: `10-Dau-Vao/02-Cap-Truong/<nhóm kỳ>/<kỳ>/` (cấp Trường) hoặc `KTC-Database/01-Legal-Database/` (cấp trên Trường)
- Tên file: `KH_[kỳ]_[kỳ-cụ-thể]_[Don-vi-ban-hanh]_[So-hieu-VB].docx`
  - Ví dụ: `KH_Nam_2026_Truong-CDKT_736-KH-CDKT.docx`
  - Ví dụ: `KH_Quy_2026-Q3_Truong-CDKT_817-KH-CDKT.docx`
- **Metadata bắt buộc** ghi vào đầu file hoặc file `.md` đi kèm cùng tên:
  - `Trạng thái`: Đã ban hành
  - `Số hiệu`: [số hiệu văn bản]
  - `Ngày ký`: [dd/mm/yyyy]
  - `Đơn vị ban hành`: [tên đơn vị]
  - `Phạm vi kỳ`: [Năm YYYY / Quý N-YYYY / Tháng M-YYYY / Chuyên đề: tên]
  - `Nguồn gốc nạp`: "Do Trường cung cấp" hoặc "Tải từ Internet — [nguồn] — [URL] — ngày tải [dd/mm/yyyy]"
- Sau pre-flight PASS → Skill 37 sử dụng trực tiếp

### Luồng C — Nhập hồi tố (kỳ trước thiếu KH cấp trên)
- Áp dụng: khi hệ mới triển khai hoặc phát hiện thiếu KH cấp trên của kỳ đã qua
- Vị trí: `KTC-Database/01-Legal-Database/` — cùng vị trí Luồng B
- Tên file: thêm hậu tố `_HOITRO`: `KH_Nam_2025_Truong-CDKT_XXX_HOITRO.docx`
- Metadata bổ sung: `Ghi chú nạp`: "Nhập hồi tố ngày [dd/mm/yyyy]"
- Sau khi nạp → kiểm tra xem Skill 37 kỳ tương ứng có cần chạy lại không

---

## PHẦN C — 4 Kiểm tra Pre-flight

### Kiểm tra 1 — Đủ đơn vị nộp chưa?

**Kỳ Năm/Quý/Tháng:** Kiểm tra 13 thư mục đơn vị — mỗi thư mục cần ≥1 file Luồng A hợp lệ.

**Kỳ Chuyên đề:** Kiểm tra riêng:
- `Cong-Doan/` — có file Luồng A không? (nếu chuyên đề liên quan)
- `Doan-TN/` — có file Luồng A không? (nếu chuyên đề liên quan)
- `KH-Truong/` — có dự thảo KH chuyên đề không? (**bắt buộc**)
- Không kiểm tra 11 Phòng/Khoa còn lại (không có thư mục)

Kết quả:
- ✅ Đủ → ghi nhận, tiếp tục
- ⚠️ **PASS-PARTIAL** — thiếu ≤3 đơn vị (kỳ định kỳ), người có thẩm quyền xác nhận chạy tạm → ghi rõ "kết quả sơ bộ, chưa đủ tất cả đơn vị"
- ❌ **FAIL** — thiếu >3 đơn vị hoặc `KH-Truong/` trống (kỳ chuyên đề) → DỪNG

### Kiểm tra 2 — Tên file đúng quy ước và định dạng?
- Đúng quy ước Luồng A/B/C và đúng định dạng `.docx`/`.xlsx` → ✅ pass
- Sai quy ước tên → [TÊN FILE SAI QUY ƯỚC], yêu cầu đổi tên
- Sai định dạng (`.pdf`, `.md`, `.txt`, ảnh) → [ĐỊNH DẠNG KHÔNG HỢP LỆ], yêu cầu chuyển đổi
- **Không tự đổi tên hoặc chuyển định dạng** — chỉ liệt kê để người dùng xử lý

### Kiểm tra 3 — Có KH cấp trên chưa? (điều kiện tiên quyết Skill 37)
Kiểm tra `10-Dau-Vao/02-Cap-Truong/<nhóm kỳ>/<kỳ>/` và `KTC-Database/01-Legal-Database/` có ≥1 file Luồng B/C đúng phạm vi:
- Lập tháng → cần KH quý tương ứng
- Lập quý → cần KH năm tương ứng
- Lập năm → không bắt buộc (kỳ đầu)
- Lập chuyên đề → cần văn bản chỉ đạo/KH cấp trên liên quan
- ✅ Có → Skill 37 sẵn sàng
- ⚠️ Thiếu → cảnh báo: "Skill 37 KHÔNG CHẠY được — chưa có KH cấp trên kỳ [...]". Vẫn cho phép Skill 35+36 nhưng ghi chú "chưa đối chiếu phân cấp thời gian".

### Kiểm tra 4 — Kết nối kho 01-04 có sẵn sàng?
Xác nhận Google Drive connector hoạt động, đọc được `ktc-database` (01-04).
- ✅ Có → tiếp tục
- ❌ Không → DỪNG theo Nguyên tắc bất biến (`00-Nguyen-Tac-Chung.md`)

---

## PHẦN D — Output và Kết luận Pre-flight

| Kiểm tra | Kết quả | Chi tiết |
|---|---|---|
| Đủ đơn vị nộp | ✅/⚠️/❌ | Danh sách đơn vị thiếu (nếu có) |
| Tên file + định dạng | ✅/⚠️ | Danh sách file sai tên/sai định dạng |
| Có KH cấp trên (Skill 37) | ✅/⚠️ | Tên file KH cấp trên tìm được |
| Kết nối kho 01-04 | ✅/❌ | Trạng thái connector |

**Kết luận:**
- ✅ **PASS** → "Được phép chạy Skill 35."
- ⚠️ **PASS-PARTIAL** → "Chạy Skill 35 với [N] đơn vị đã nộp. Kết quả sơ bộ — chưa đủ: [danh sách thiếu]."
- ❌ **FAIL** → "DỪNG. Cần khắc phục trước khi tiếp tục: [danh sách cụ thể]."

---

## PHẦN E — Ràng buộc
- Không tự cho phép bỏ qua đơn vị thiếu — chỉ Trưởng phòng TH-HC&QT xác nhận PASS-PARTIAL.
- Không tự đổi tên file hoặc chuyển định dạng.
- Không tự nạp file Internet vào `KH-Cap-Tren/` khi chưa được người dùng xác nhận (`04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md`).
- Kỳ Chuyên đề: KHÔNG yêu cầu 11 Phòng/Khoa nộp — không đánh dấu FAIL vì lý do này.

## Liên hệ
- `00-Nguyen-Tac-Chung.md` — nguyên tắc bất biến
- `35-Skill-Thu-Thap-De-Xuat-Don-Vi.md` — chạy sau PASS
- `37-Skill-Doi-Chieu-Phan-Cap-Thoi-Gian.md` — cần KH-Cap-Tren pass KT3
- `00-Metadata-Schema.md` — metadata Luồng B/C
- `04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md` — khi file Luồng B/C từ Internet
