# Known Issues — KTC-Quan-tri

Lỗi và khoảng trống **đã biết nhưng chưa xử lý**. Ghi lại để không quên và không tốn công phát hiện lại.

**Cập nhật:** 20/9/2026

**Mốc hạn** của các việc đang mở ghi riêng tại `Moc-Han.md` (bảng, một dòng một mốc) — tự cảnh báo đầu mỗi phiên
qua `29-Cong-Cu/kiem_moc_han.py`. Có hạn mới thì thêm dòng vào đó, không chỉ ghi trong văn xuôi dưới đây.

---

## Đã giải quyết

Các mục đã đóng ghi trạng thái "Resolved"/"ĐÃ ĐÓNG" ngay trong mục của nó (ví dụ `KI-004`, `KI-009`,
`KI-012`, `KI-013`) — không có mục riêng ở cuối tệp. Danh sách còn mở dưới đây.

## KI-001 — Phụ lục Ia/Ib chưa có cột `Task_ID`

**Status:** Đã quyết 18/9/2026 — Lãnh đạo Trường thống nhất (`DL-20260918-003`); `read_bc736_excel.py` v3.3 đã đọc
được cột. **Còn chờ:** văn bản điều chỉnh mẫu + kỳ áp dụng (phòng TH-HC&QT), dữ liệu thật đầu tiên có cột · **Priority:** Cao — chặn toàn bộ khả năng đối chiếu tự động

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

**Đề xuất kỹ thuật đầy đủ 18/9/2026** (vị trí cột, định dạng, cách sửa `read_bc736_excel.py`, lộ trình áp
dụng — không hồi tố dữ liệu cũ):
`30-Ket-Qua/2026-09-18/De-xuat/De-xuat-Bo-sung-Cot-Task_ID-Phu-luc-TB736.md`.

---

## KI-002 — Danh mục 122 nhiệm vụ chuẩn chưa phủ 6 Khoa

**Status:** Open — người dùng xác nhận lại 18/9/2026 **sẽ hoàn thiện sau**, không xử lý trong đợt dọn việc
mở này · **Priority:** Cao

1.358 nhiệm vụ gốc chỉ đến từ 5 Phòng (TH-HC&QT 402, QLKHCN&HTPT 387, QLĐT&BĐCL 366, Phòng Tổ chức 126,
TC-KT 77). Lĩnh vực `S. Nhiệm vụ chuyên môn nhà giáo` chỉ có 4 mã, sinh từ viên chức Phòng có giảng dạy.

**Workaround:** nhiệm vụ của Khoa không khớp mã nào thì để trống `Ma_NV_Chuan`, đề nghị bổ sung mã mới.
Tuyệt đối không ép về mã gần đúng.

---

## KI-003 — Bảng mã đơn vị chỉ có một cấp

**Status:** Open — người dùng xác nhận 18/9/2026 **sẽ hoàn thiện sau**, không xử lý trong đợt dọn việc mở
này · **Priority:** Trung bình

Cột "Đơn vị chủ trì" trong dữ liệu thật chứa cả bộ phận nội bộ và nhóm người: `Ban Truyền thông` (19×),
`Nhà giáo` (6×), `Các bộ môn và nhà giáo` (4×), `Bộ môn CK&XD` (4×), `Giáo vụ khoa` (3×), `Chi bộ khoa` (2×),
`Các lớp sinh viên` (2×)… — tổng 60 dòng ở 4 đơn vị không ánh xạ được.

**Cần:** cấp mã thứ hai (bộ môn · tổ · ban · chức danh), mỗi giá trị trỏ về đúng một mã đơn vị cấp một.

---

## KI-015 — Hai đầu mối đoàn thể chưa có mã chuẩn

**Status:** Mở · **Phát hiện:** 19/9/2026, bởi `29-Cong-Cu/doi_soat_so_lieu.py` (DS06) trên `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/`

`20-Chuan-Chung/13-Bang-Ma-Don-Vi.md` ghi 13 đầu mối nộp báo cáo: 11 đơn vị cấp một, Công đoàn cơ sở, và Đoàn Thanh
niên – Hội Sinh viên. Bảng chỉ có mã cho 11 đơn vị cấp một. Thư mục nộp thực tế đang dùng `DT-CDCS` và `DT-DTN`, là
mã tự đặt, chưa được chốt.

**Cần người phụ trách hệ quyết:** chấp nhận hai mã này hay đặt mã khác. Sau đó bổ sung vào bảng mã và Master Task Register
(`02-Danh-muc-tra-cuu`). Trong lúc chờ, công cụ đối soát báo Mức 3 nhưng vẫn xử lý dữ liệu. Văn bản Đảng và đoàn
thể theo hệ quy chiếu B/D, không áp NĐ 30.

---

## KI-016 — Hồ sơ Đề án Trung tâm Đăng kiểm đã trình UBND tỉnh: chờ thẩm định, còn 7 điểm lệch chưa sửa

**Status:** Mở · **Cập nhật:** 20/9/2026 · **Priority:** Trung bình — chỉ xử lý khi UBND/Sở yêu cầu chỉnh hồ sơ

Hồ sơ ký 25/8/2026 (Tờ trình 22/TTr-CĐKT, Đề án 08/ĐA-CĐKT, BC 382 và 384) đã trình UBND tỉnh. Tri thức, số liệu chốt và danh sách 7 điểm
lệch (Quốc hiệu "CỘNG HOÀ", cụm "góp vốn bằng tài sản được cho phép" còn trong Tờ trình/Quyết định, Bảng 12 còn dòng QSDĐ 7.820…):
`90-Nhat-Ky-Van-Hanh/07-Tri-Thuc-Chuyen-De/De-an-Trung-tam-Dang-kiem-XCG.md`. Hồ sơ đã ký — không tự sửa; **ngày gửi thực tế** cần người dùng cung cấp.

---

## KI-017 — Hồ sơ CTMTQG hiện đại hóa GD&ĐT: số liệu đầu vào lệch, QĐ 1951 sai đơn vị, metadata kho sai

**Status:** Mở · **Cập nhật:** 20/9/2026 · **Priority:** Cao với điểm 1 (số liệu đã chốt 30/6/2026, ảnh hưởng hệ số Hqm theo QĐ 36)

Tri thức và 14 điểm lệch: `90-Nhat-Ky-Van-Hanh/07-Tri-Thuc-Chuyen-De/CTMTQG-Hien-dai-hoa-GDDT-2026-2030.md` (mục 8). Nổi bật: (1) quy mô đào tạo cao đẳng
2.666 ≠ 3.296 ≠ 3.147; (2) QĐ 1951 ghi tổng mức "192.857.143 **triệu** đồng" (đúng: nghìn); (3) metadata kho ghi CV 5903 "chưa rõ số/ngày" và BC 48 "ngày không
xác định" — kho chỉ đọc, cần người có thẩm quyền sửa trên Drive. Hồ sơ đã gửi — không tự sửa; **người dùng quyết** có chỉnh hay không. Ranh giới hạng mục giữa
CTMTQG hiện đại hóa và CTMTQG NTM-GNBV chưa có văn bản phân định.

---

## KI-018 — CTMTQG NTM–GNBV–DTTS: vốn giao 2026 thấp xa nhu cầu, 5 điểm lệch số liệu

**Status:** Mở · **Cập nhật:** 20/9/2026 · **Priority:** Cao — ảnh hưởng mọi báo cáo về dự án

Chi tiết và nguồn ở `90-Nhat-Ky-Van-Hanh/07-Tri-Thuc-Chuyen-De/CTMTQG-NTM-GNBV-DTTS-2026-2030.md` (mục 6):
(1) NQ 56 giao Trường 260 triệu vs dự toán CBĐT 6.249,856 triệu (QĐ 1899) — cần người có thẩm quyền quyết cách xử lý;
(2) ngày họp GM 930 lệch giữa CV 10965 (9/9) và gói cũ (11/9); (3) BC 326 lần 2 vẫn số 326, tệp "TRACK-CHANGES" không có thay đổi
theo dõi nào, chưa rõ đã ký/gửi; (4) chỉ tiêu đào tạo 12.365 (văn bản) / 12.635 (bảng) / 12.625 (cộng thành phần);
(5) 75.000 triệu đối ứng NS tỉnh chỉ có trong CV 10965. Còn: TB 916, GM 930, CV 7524, QĐ 417 chưa có trong kho.

---

## KI-019 [ĐÃ ĐÓNG 20/9/2026] — Plugin `ktc-ra-soat-897` đang chạy dẫn quy chế đã hết hiệu lực (QĐ 988)

**Status:** Đã đóng · **Phát hiện:** 20/9/2026 · **Priority:** Cao — 897 là chốt chặn bắt buộc trước trình ký (Nguyên tắc 9)

Plugin 897 có **hai nhánh alpha song song**, cả hai cùng mang nhãn `0.1.0-alpha.2` cho hai nội dung khác nhau:
nhánh nguồn trên Drive (15/9/2026, có nghiệp vụ v2.24 + sửa QĐ 988 → **QĐ 1976/QĐ-CĐKT** ở 9 tệp) và nhánh
đang cài/đang chạy (2/9/2026, có mẫu báo cáo 8 phần + evaluation + `ktc-eval`, nhưng **0 tệp** nhắc QĐ 1976).
Không bản nào là tập cha của bản kia. Bản đang chạy vì vậy đối chiếu quy chế đã hết hiệu lực từ 14/9/2026 —
xác nhận độc lập bằng `29-Cong-Cu/tra_hieu_luc.py` trên kho KTC-Database.

**Đã xử lý 20/9/2026:** khôi phục bố cục hosted-safe cho cây nguồn; vá guard xóa đệ quy đã chết từ 28/8/2026;
thêm `tools/kiem_dong_bo_addon.py` phát hiện lệch ba bản.

**ĐÃ QUYẾT 20/9/2026** — người phụ trách hệ chốt: (1) mẫu báo cáo rà soát là **8 phần**; (2) checklist lấy
theo bản **v2.24 đã khóa SHA-256**; (3) lấy **nhánh v2.24** làm gốc. Đã hợp nhất thành **alpha.7**: nghiệp vụ
theo v2.24 (gồm QĐ 1976), kỹ thuật theo alpha.3–6 (mẫu 8 phần, `core/evaluation/`, `ktc-eval`, dựng lặp lại
được). Bản đang chạy nay có 8 tệp nhắc QĐ 1976 (trước: 0). `UNIVERSAL_VALIDATION=PASS`.

`ktc-eval` và `core/evaluation/` đã chốt là **phát hành cho đơn vị**, validator đưa vào danh sách bắt buộc.
Kho nguồn 897 đã lên GitHub: `nnqp201-sys/KTC-Ra-Soat-897-Universal-Plugin` (`c8501d2`, `29616dc`).
Hồ sơ hợp nhất: `KTC-Ra-Soat-897-Universal-Plugin/governance/PHAN-NHANH-ALPHA.md`.

**ĐÃ ĐÓNG 20/9/2026.**

---

## KI-020 — Kho skill trên tài khoản claude.ai giữ bản CŨ của chính các hệ KTC

**Status:** Đã xử lý phía máy 21/9/2026, **còn chờ dọn trên claude.ai** · **Priority:** Cao — ảnh hưởng chốt chặn trước trình ký

Chạy `/doctor` ngày 21/9/2026 phát hiện tài khoản claude.ai (`My Uploads`) đang đồng bộ xuống máy **bản cũ**
của chính hai hệ, và chúng được nạp **song song** với plugin hiện hành:

| Bản đồng bộ từ claude.ai | Phiên bản | Bản hiện hành |
|---|---|---|
| `ktc-ra-soat-897` | **0.1.0-alpha.2** | alpha.7 |
| `ktc-quan-tri` | **0.5.3** | 0.9.1 |
| 7 skill `anthropic-skills:ktc-*` | bản cũ | thuộc plugin `ktc-quan-tri` |

`alpha.2` chính là nhánh **trước hợp nhất**, còn dẫn **QĐ 988 đã hết hiệu lực** (xem `KI-019`). Bộ đếm
`skillUsage` trong `~/.claude.json` cho thấy đã có phiên gọi đúng bản cũ
(`anthropic-skills:ktc-ra-soat-897-universal-0-1-0-alpha-5`, 1 lượt). Đây là rủi ro **pháp lý**, không phải
chuyện gọn nhẹ context: 897 là chốt chặn bắt buộc trước trình ký (Nguyên tắc 9).

**Đã xử lý trên máy 21/9/2026**: tắt 7 skill cũ bằng `skillOverrides` và tắt 3 plugin chưa dùng lần nào
(`data`, `productivity`, `cowork-plugin-management`, cả hai bản `@inline` và `@synced`) trong
`~/.claude/settings.json`; chuyển 3 thư mục sao lưu plugin ra khỏi thư mục marketplace.

**Còn chờ người dùng**: xóa hoặc thay bản cũ **trên chính tài khoản claude.ai** — `skillOverrides` chỉ
chặn ở máy này. Máy khác, hoặc bản Chat/Cowork dùng cùng tài khoản, **vẫn nạp bản alpha.2**. Muốn dứt điểm
phải tải bản alpha.7 lên thay, hoặc gỡ mục cũ khỏi `My Uploads`.

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

Đã ghi vào `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`. Ban Truyền thông **không phải đầu mối nộp báo cáo riêng**
— số đầu mối là **13**, không phải 14.

---

## KI-005 [ĐÃ ĐÓNG 14/9/2026 — hợp nhất thành `ktc-bao-cao-v3.5.skill`, 36 tệp, là tập cha của cả hai nhánh]

## KI-005 (nội dung gốc) — Hai nhánh `.skill` của KTC-Bao-Cao chưa hợp nhất

**Status:** Open · **Priority:** Trung bình · **Xem:** `DL-20260913-001`

`ktc-bao-cao-v3.4.skill` có nghiệp vụ mới hơn (Skill 31 đọc Excel TB736); `ktc-bao-cao-v2_5_1-memory.skill`
cập nhật muộn hơn 2 ngày và giữ trọn lớp `references/Memory/` mà bản kia không có. Nhật ký bên trong nhánh
memory tự ghi *"Còn treo: Gộp v3.1"*.

**Workaround:** giữ cả hai, không lưu trữ bản nào. Xem `25-KTC-Bao-Cao/00-TRANG-THAI-GOI-SKILL.md`.

---

## KI-006 — Bốn lỗi thể thức hồ sơ tháng 8/2026 chưa khắc phục

**Status:** Dự thảo CV đã rà soát chính thức 897 (0 Mức 1) và sửa Mức 2/3 bằng Track Changes 18/9/2026 —
`30-Ket-Qua/2026-09-18/Cong-Van/…_sua-theo-ra-soat.docx`; chờ phòng TH-HC&QT kiểm tra, chốt thời hạn và trình Hiệu
trưởng ký — không tự sửa hồ sơ đơn vị · **Priority:** Cao — chặn việc chốt kỳ tháng 8 · **Xem:** `PM-20260913-001`

| Đơn vị | Lỗi |
|---|---|
| Phòng TH-HC&QT | Thư mục chỉ có báo cáo của Ban Truyền thông (mảng truyền thông), chưa thấy báo cáo của Phòng với tư cách đơn vị — mảng văn thư, hành chính, quản trị, cơ sở vật chất. *Vị trí tệp là đúng chủ đích, xem `KI-004`; vấn đề là thiếu phần còn lại.* |
| Phòng TCCB | Nộp "BÁO CÁO kết quả tháng 9" thay vì kế hoạch tháng 9; dùng sai Phụ lục IIb |
| Khoa KT-CN | Sai cấu trúc cột — cột (8) là "Thời gian hoàn thành" thay vì "Điểm chấm công việc" |
| Khoa Sư phạm | Tiêu đề tự chế, chỉ 7 nhiệm vụ so với trung bình 25 |

Kèm theo: Khoa CKHCB và Khoa KT-NL thiếu mục Trục 2 và Trục 5; 5 tệp còn để nguyên sheet mẫu trống (không
xác định được đơn vị nào trong số này — không quy kết đích danh).

**Đã dựng 18/9/2026** — bản dự thảo Công văn (hệ A, phát triển từ văn bản đã ban hành
`KTC-Database/04-Good-Documents/04-08- Cong van/1. CV gop y cac DT TTr, QD, DA Dang kiem lan 4.docx` theo
NT-1, căn cứ Thông báo 736/TB-CĐKT và 817/TB-CĐKT, đã rà soát nhanh theo Checklist 08 — sửa 4 lỗi thể thức
tự phát hiện: sai mẫu ký hiệu công văn, chính tả "CỘNG HOÀ"→"CỘNG HÒA", tên Phòng TCCB lệch giữa hai nguồn
nội bộ, thiếu viết hoa sau dấu hai chấm):
`30-Ket-Qua/2026-09-18/Cong-Van/DU-THAO_CV_Bo-sung-chinh-sua-ho-so-KH-BC-thang-8-9-2026.docx`.

**Còn cần người có thẩm quyền:** điền số/ngày ban hành thật, xác nhận người ký (bản dự thảo tạm để Hiệu
trưởng ký trực tiếp theo đúng mẫu văn bản gốc — chưa xác nhận đây có phải thẩm quyền/cấp ký đúng quy trình
nội bộ cho loại nhắc nhở này hay nên ủy quyền TL./TUQ. cho Trưởng phòng TH-HC&QT), và xác nhận hạn phản hồi
(bản dự thảo đề xuất 24/9/2026, chỉ là gợi ý).

---

## KI-007 — Sai lệch số liệu trong danh mục sản phẩm

**Status:** ĐÃ TÌM RA NGUYÊN NHÂN 18/9/2026 — còn chờ người giữ tệp tự sửa (không tự ý sửa nguồn) ·
**Priority:** Thấp

Tệp xác định: `11-Du-lieu-Cong-Viec/DANH MUC SAN PHAM CONG VIEC/Du thao_Danh_muc_SP_theo_loai_van_ban_va_6_truc.xlsx`,
sheet `Tong hop theo Truc`, ô "Số sản phẩm" dòng Trục 1 = **102** (giá trị gõ cứng, không phải công thức).

**Đã kiểm chứng dứt điểm:**
- Đếm trực tiếp số dòng sản phẩm có `Trục = "Trục 1"` trên sheet `Danh muc san pham`: **103** dòng.
- Cộng theo Nhóm trên chính dòng đó (54+37+7+4+1): **103**.
- Đối chiếu 5 Trục còn lại: cả 5 dòng đều khớp đúng giữa "Số sản phẩm" và tổng theo Nhóm (Trục 2:
  54=27+26+1 · Trục 3: 46=24+21+0+0+1 · Trục 4: 66=37+28+0+0+1 · Trục 5: 71=36+35 · Trục 6: 31=19+12).

**Kết luận:** chỉ một ô duy nhất (Trục 1 / "Số sản phẩm") gõ sai, giá trị đúng là **103**. Không phải lỗi
cấu trúc, không có dòng trùng/lạc. Đề nghị người giữ tệp sửa ô đó thành 103.

**Phát hiện thêm liên quan trực tiếp KI-014** (xem mục đó): trong chính sheet `Danh muc san pham`
(371 dòng), 201/371 dòng (54%) mang nhãn "Nhóm" của thang 5 nhóm nhưng cột Điểm vẫn là giá trị thang 4
mức (100/120/150/200) — nghi là việc gắn nhãn "Nhóm" mới chưa cập nhật hết cột Điểm tương ứng, không phải
hai thang cố ý cùng tồn tại trong nội bộ một tệp. 3 dòng khác có Điểm bất thường không khớp thang nào
(dòng 128, 252, 370 — Điểm = 30/0,5/0,3). 4 dòng vi phạm công thức Hệ số = Điểm × 1% (dòng 21, 252, 305,
370). Đã ghi rõ vị trí dòng để người giữ tệp tự kiểm, không tự sửa.

---

## KI-008 — Chưa xác minh "phần mềm KPI"

**Status:** Đã tra sâu KTC-Database 18/9/2026, vẫn treo phạm vi — cần hỏi bên ngoài · **Priority:** Cao
trước khi số hóa quy trình
**Cập nhật 14/9/2026** (từ `PM-20260914-Chay-thu-KH-thang-9`): `KH-834/KH-CĐKT` ngày 6/9/2026 có nhiệm vụ
*"Ban hành kế hoạch triển khai phần mềm **VNPT KPI** - Hệ thống quản lý đánh giá, xếp loại..."*.

→ Phần mềm KPI mà QĐ 1923 dẫn chiếu là **VNPT KPI**. Tính đến 6/9/2026 Trường **mới đang lập kế hoạch
triển khai**, chưa vận hành — nên nguy cơ Master Task Register làm trùng chức năng là **chưa xảy ra**,
nhưng sẽ xảy ra nếu VNPT KPI đi vào vận hành trước khi Register chốt.

**Cập nhật 18/9/2026 — đã tìm sâu theo nguyên tắc bất biến #10** (quét toàn văn 173 tệp `.docx` trong
`KTC-Database/02-KTC-Regulations`, không chỉ tra tên tệp):
- **Đã loại trừ nhầm lẫn quan trọng**: hệ thống "**VNPT-Office / VNPT-iOffice**" xuất hiện trong ~10 văn bản
  (quy chế làm việc, quản lý sáng kiến, đề tài KHCN, lưu hồ sơ dạy học...) là **hệ quản lý văn bản và điều
  hành** do VNPT Quảng Ngãi cung cấp — **khác hoàn toàn** với "VNPT KPI". Không được nhầm hai hệ này khi
  tra cứu tiếp.
- **Không tìm thấy thêm tài liệu nào** trong 173 tệp mô tả phạm vi quản lý hay khả năng xuất dữ liệu của
  riêng VNPT KPI, ngoài câu nhắc trong `KH-834`.
- Có văn bản liên quan gần nhất: `QD-CDKT_Phe-duyet-DM-san-pham-ca-nhan-Lanh-dao-Quy-III-2026` (số
  1883/QĐ-CĐKT, 27/8/2026) — phê duyệt danh mục sản phẩm cá nhân lãnh đạo theo quý, do Phòng TCCB &
  CTHSSV đề nghị. Đây là đầu mối phụ trách đánh giá KPI hiện tại, **có thể** là nơi nắm phạm vi VNPT KPI,
  nhưng phụ lục chi tiết của QĐ này không có trong kho (chỉ có văn bản bìa) nên không kiểm chứng được qua
  tài liệu.

**Còn phải xác minh (không thể làm tiếp bằng tra cứu nội bộ):** VNPT KPI quản lý tới đâu (chỉ chấm điểm cá
nhân, hay cả giao việc và theo dõi tiến độ?), và có API/xuất dữ liệu được không. **Đề xuất:** hỏi trực tiếp
Phòng Tổ chức cán bộ và Công tác học sinh – sinh viên (đầu mối theo QĐ 1923 và QĐ 1883).

<details><summary>Nội dung gốc</summary>

**Status:** Open · **Priority:** Cao trước khi số hóa quy trình

Quy chế ban hành kèm QĐ 1923/QĐ-CĐKT dẫn chiếu việc viên chức tự đánh giá và cho điểm "thực hiện trên
**phần mềm KPI**". Chưa biết phần mềm đó là gì và quản lý tới đâu. Nếu nó đã quản lý chỉ tiêu KPI theo quý
thì Master Task Register có nguy cơ làm trùng chức năng.

</details>

---

## KI-011 — Danh mục nhiệm vụ chuẩn lệch tên Trục/Nội hàm với TB 817

**Status:** Đã dựng xong bảng đối chiếu đầy đủ 18/9/2026 — chờ người giữ tệp áp dụng (không tự sửa nguồn)
· **Priority:** Cao — ảnh hưởng mọi phân loại

`11-Du-lieu-Cong-Viec/DANH MUC SAN PHAM CONG VIEC/Bang tong hop_phan tich_DANH_MUC_NHIEM_VU_CHUAN_TRUC_NOI_HAM_HE_SO.xlsx`
(122 nhiệm vụ, dự thảo lần 4, sheet `2. Phân loại theo loại TL`) dùng tên Trục **khác** TB 817/TB-CĐKT
(số 817/TB-CĐKT, 14/7/2026, đã đọc trực tiếp từ `KTC-Database/02-KTC-Regulations/05. TB-817-...docx`).

**Bảng đối chiếu đầy đủ cả 6 Trục** (không chỉ ví dụ Trục 1 như bản ghi cũ):

| Trục | TB 817 (chuẩn, 14/7/2026) | File danh mục (dự thảo lần 4) | Mức lệch |
|---|---|---|---|
| 1 | Thực hiện mục tiêu phát triển kinh tế – xã hội và nhiệm vụ chính trị được giao | Lãnh đạo thực hiện nhiệm vụ chính trị | Lớn — thiếu hẳn phần "phát triển kinh tế – xã hội" |
| 2 | Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát | Xây dựng, hoàn thiện thể chế; nâng cao hiệu lực, hiệu quả quản trị và quản lý nhà trường | Trung bình — chung gốc "hoàn thiện thể chế", khác phần còn lại |
| 3 | Thúc đẩy phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số | Phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số | Nhỏ — chỉ thiếu động từ "Thúc đẩy" đầu câu |
| 4 | Xây dựng Đảng và hệ thống chính trị trong sạch, vững mạnh; giữ gìn đoàn kết, thống nhất nội bộ; phòng, chống tham nhũng, lãng phí, tiêu cực | Xây dựng Đảng, hệ thống chính trị; xây dựng đội ngũ cán bộ, viên chức; phát huy sức mạnh đại đoàn kết toàn trường | Lớn — thiếu hẳn phần "phòng, chống tham nhũng, tiêu cực"; thêm phần "đội ngũ cán bộ, viên chức" TB 817 không có ở tên Trục |
| 5 | Phát triển văn hóa, con người, bảo đảm an sinh xã hội, nâng cao đời sống nhân dân | Phát triển văn hóa, con người; quản lý, khai thác, sử dụng hiệu quả các nguồn lực; bảo vệ môi trường và thực hiện trách nhiệm xã hội | Trung bình — chung "phát triển văn hóa, con người", khác hẳn phần sau |
| 6 | Củng cố quốc phòng, an ninh, giữ vững ổn định chính trị - xã hội, nâng cao hiệu quả đối ngoại và hội nhập quốc tế | Tăng cường quốc phòng, an ninh, đối ngoại và hội nhập quốc tế | Nhỏ — bản rút gọn, không sai ý |

**Đã xác nhận không phải lỗi ở nơi khác**: `read_bc736_excel.py` (script đọc Phụ lục TB736 thật) đã dùng
đúng nguyên văn 6 tên Trục của TB 817 — script này KHÔNG bị ảnh hưởng. Vấn đề khoanh vùng đúng vào một
tệp: danh mục 122 nhiệm vụ chuẩn dự thảo lần 4.

Hiện lấy TB 817 làm chuẩn (văn bản đã ban hành; BC-375 cũng đặt tiêu đề theo TB 817). **Việc còn lại không
tự làm được**: quyết định cập nhật tên Trục trong file danh mục cho khớp TB 817, hay xác nhận đây là hai
hệ phân loại cố ý khác nhau — cần người giữ tệp `11-Du-lieu-Cong-Viec` quyết định và áp dụng.

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

**Đã xử lý tạm:** khôi phục thang 4 mức vào `20-Chuan-Chung/30-Skill-Phan-Loai-6-Truc.md` kèm bảng bằng
chứng và ghi chú phân định phạm vi: thang 4 mức dùng cho cột (9)(10) Phụ lục TB736; thang 5 nhóm thuộc
danh mục sản phẩm theo loại văn bản, hiện mới là dự thảo lần 4.

**Chưa giải quyết — cần người có thẩm quyền quyết định:**
1. Hai thang là hai hệ quy đổi độc lập cho hai mục đích khác nhau, hay thang 5 nhóm dự kiến **thay thế**
   thang 4 mức khi danh mục sản phẩm được ban hành? Trả lời khác nhau dẫn tới thiết kế Master Task Register
   khác nhau.
2. Nếu là hai hệ độc lập thì một nhiệm vụ vừa nằm trong Phụ lục TB736 vừa quy đổi theo danh mục sản phẩm
   sẽ có **hai điểm số khác nhau** — cần quy tắc chọn hoặc quy tắc chuyển đổi.

**Không tự đặt quy tắc chuyển đổi giữa hai thang.** Điểm quy đổi gắn với đánh giá viên chức.

**Bằng chứng bổ sung 18/9/2026 — nghiêng về hướng "di chuyển dở dang" hơn là "hai hệ cố ý độc lập"**
(chỉ trình bày dữ kiện, không tự kết luận thay người có thẩm quyền):
- Ngay trong chính tệp đề xuất thang 5 nhóm (`Du thao_Danh_muc_SP_theo_loai_van_ban_va_6_truc.xlsx`, sheet
  `Danh muc san pham`, 371 dòng sản phẩm), có **201/371 dòng (54%)** mang nhãn "Nhóm" (1–5) nhưng cột Điểm
  của chính dòng đó lại là giá trị của thang 4 mức (100/120/150/200), không phải giá trị thang 5 nhóm đúng
  nhãn (50/120/250/350/450). Chỉ **167/371 dòng (45%)** có Điểm khớp đúng thang 5 nhóm theo nhãn Nhóm của
  nó. 3 dòng còn lại có Điểm bất thường (30/0,5/0,3 — có thể là lỗi nhập liệu, xem `KI-007`).
- Công thức `Hệ số = Điểm × 1%` vẫn đúng **367/371 dòng (99%)** bất kể dòng đó mang giá trị của thang nào —
  công thức này không giúp phân định thang, chỉ xác nhận lại phát hiện đã có ở dữ liệu vận hành thật.
- Đã tra `KTC-Database` (173 văn bản `02-KTC-Regulations`): **không tìm thấy Quyết định/Thông báo nào**
  ban hành chính thức thang 5 nhóm hoặc danh mục sản phẩm theo loại văn bản. Có QĐ 1883/QĐ-CĐKT (27/8/2026)
  phê duyệt "Danh mục sản phẩm/công việc Quý III/2026" nhưng là danh mục **cá nhân lãnh đạo** (khung đánh
  giá quý theo Đảng/Nhà nước), khác phạm vi với danh mục sản phẩm 6-Trục toàn Trường đang xét — và phụ lục
  chi tiết của QĐ này không có trong kho để đối chiếu thang điểm.
- **Dữ kiện, không phải kết luận:** số liệu cho thấy bản dự thảo lần 4 có thể đang ở giữa chừng một đợt gắn
  lại nhãn "Nhóm" mới lên dữ liệu cũ mà chưa cập nhật hết cột Điểm — nhưng đây chỉ là một cách đọc dữ kiện,
  không loại trừ khả năng thang 5 nhóm được cố ý thiết kế khác và 201 dòng kia đúng là cần sửa theo hướng
  ngược lại. Không đủ căn cứ để AI chọn thay.

**Đề xuất quy trình quyết định** (không phải quyết định): người có thẩm quyền (đơn vị giữ
`11-Du-lieu-Cong-Viec`, phối hợp Phòng TCCB & CTHSSV) xác nhận 1 trong 3 hướng — (a) thang 4 mức là chuẩn
chính thức, thang 5 nhóm chỉ là bản nháp chưa hoàn thiện việc gắn nhãn; (b) thang 5 nhóm sẽ thay thế thang
4 mức khi danh mục sản phẩm được ban hành chính thức, cần hoàn thiện lại 201 dòng lệch trước; (c) hai thang
độc lập thật, cần quy tắc chọn tường minh khi một nhiệm vụ rơi vào cả hai. Sau khi chọn, mới cập nhật
Master Task Register và các skill liên quan.

**Liên quan:** `KI-011` (lệch tên Trục/Nội hàm) · `KI-007` (cùng tệp, lỗi đếm 102/103) ·
`CP-20260914-001` mục 2.2

---

**Cập nhật 24/9/2026 — thang 4 mức có trong văn bản đã ban hành** (`DL-20260924-001`):
- Phụ lục II của **QĐ 1923/QĐ-CĐKT** (30/8/2026, mẫu kế hoạch cá nhân) ghi hệ số theo 4 mức độ 1,0/1,2/1,5/2,0;
  Phụ lục I có cột Điểm chấm 100/120/150/200 và Hệ số quy đổi. Thang 4 mức vì vậy **có căn cứ văn bản** cho kế hoạch
  KPI, không chỉ là tập quán dữ liệu TB 736. Thang 5 nhóm (TB 1052) vẫn là dự thảo.
- Quy ước A × B (Phòng TH-HC&QT ghi nhận 24/9/2026) nhân hai thang — **chưa có văn bản**. Skill `ktc-kpi-lap-ke-hoach`
  không đặt mặc định, bắt người lập chọn phương án (Câu hỏi mở số 1, `28-KTC-KPI/references/Cau-Hoi-Mo.md`).
- Vẫn cần người có thẩm quyền chọn hướng (a)/(b)/(c) ở trên. AI không tự chọn.

**Cập nhật 19/9/2026 — TB 1052/TB-CĐKT (15/9/2026):**
- Danh mục sản phẩm đã được **gửi chính thức** cho đơn vị rà soát; hạn góp ý **20/9/2026**, sau đó trình ban hành.
- Đối chiếu từng dòng: phụ lục trùng hoàn toàn dự thảo lần 4 nhưng **bỏ cột Điểm**, chỉ giữ Hệ số.
- 204/371 dòng có hệ số khác giá trị chuẩn của Nhóm, và dòng 29.22 hệ số 50.
- **Cửa sổ để phân định hai thang là trước khi ban hành.** Góp ý đã soạn sẵn:
  `30-Ket-Qua/2026-09-19/De-xuat/Gop-y-Danh-muc-SP-TB-1052.md`.
- AI vẫn không tự đặt quy tắc chuyển đổi.

---

## KI-009 — Chưa có công cụ dựng Track Changes dùng lại được

**Status:** ĐÃ ĐÓNG 13/9/2026 — `29-Cong-Cu/ktc_trackchanges.py` + `20-Chuan-Chung/15-Skill-Track-Changes.md`

Chuẩn kỹ thuật Track Changes đã thành văn đầy đủ trong hệ 897
(`Bo-Sung-Chuan-Hoa-TrackChanges-MauChu-PhienBanSkill_20260825.md`), nhưng **không có script dựng sẵn**:
thư mục `897/tools/` chỉ có `_read_input_properties.py`, `build_ktc897_report.py` và hai tệp test. Chính
tài liệu chuẩn có nhắc chạy `validate.py` trước khi giao file — **tệp này không tồn tại trong kho**.

Hệ quả: mỗi lần cần Track Changes phải viết lại thao tác OOXML từ đầu, trong khi tài liệu đã cảnh báo hai
lỗi dễ mắc (thứ tự phần tử trong `<w:trPr>`; `rPr` lồng nhau / `xml:space` trùng). Rủi ro tái phạm cao.

**Đã làm:** mô-đun `29-Cong-Cu/ktc_trackchanges.py` — 4 thao tác sửa, validator 7 lỗi (thay cho `validate.py`
còn thiếu), `nhat_ky_sua_doi()` đọc được cả file do người sửa trong Word, `doi_chieu_goc()` phát hiện
trường hợp soạn lại từ đầu. Regression: `92-Kinh-Nghiem/02-Regression/Cases/test_trackchanges.py`.

**Còn treo:** đề xuất đưa ngược mô-đun về `897/tools/` để hệ 897 dùng chung — chưa làm.

---

## KI-010 — Chưa có nhật ký đợt chạy thử trên Claude Chat

**Status:** Open — đã xác nhận 18/9/2026 không thể tự xử lý, cần người dùng cung cấp · **Priority:** Trung
bình

Người phụ trách hệ cho biết `ktc-bao-cao` và `ktc-ke-hoach` **đã chạy thử trên Claude Chat**. Dự án
**chưa có bất kỳ ghi chép nào** về đợt chạy đó: chạy tác vụ gì, đầu vào nào, đầu ra đạt/không đạt ở đâu.

Đây là dữ liệu vận hành có giá trị cao nhất hiện có (bằng chứng thật về hành vi của skill trên nền tảng
khác Code) nhưng đang nằm ngoài hệ. Không được suy đoán kết quả.

**Đã xác nhận (18/9/2026):** đây là việc AI không tự làm được — cần transcript hoặc mô tả lại từ chính
phiên Claude Chat đó, dữ liệu này chỉ người dùng có. Không có cách tra cứu nội bộ nào thay thế được.

**Cần làm:** lấy transcript hoặc ghi lại theo mẫu `90-Nhat-Ky-Van-Hanh/02-Mau-Process-Memory.md`, chú ý ghi
rõ điểm skill **không chạy được trên Chat** do thiếu `python-docx`/`openpyxl` (đo lề/cỡ chữ thật, thao tác
Track Changes mức OOXML) — đây là thông tin có giá trị cao nhất cần lấy từ đợt chạy đó.

---

## KI-019 — Thẩm định độc lập lần 1 plugin 1.2.1: 4 lỗi Mức 1 chờ bản 1.3.0; hồ sơ gửi đi có thể chứa dữ liệu cá nhân

**Status:** Mở · **Phát hiện:** 26/9/2026 · **Priority:** Cao

Báo cáo tiếp thu, giải trình (phát triển từ mẫu `04-06-01/BAO CAO TIEP THU GIAI TRINH KE HOACH THANG 8 OK.docx`):
`30-Ket-Qua/2026-09-26/Soan-Thao/BC_Tiep-thu-giai-trinh-tham-dinh-lan-1-KTC-Quan-tri_20260926_v1.docx`; kèm dự thảo
SKILL.md quan-tri 1.13 và TB v4 (Track Changes). **Chưa sửa nguồn** — chờ duyệt mẫu SKILL.md.

- Mức 1 đã kiểm chứng trên mã: `ktc_backup_github.py --neu-can` trong SessionStart của plugin; `ktc_nhat_ky.py` ghi 600 ký tự
  lời người dùng; 0/8 SKILL.md có ranh giới dữ liệu không tin cậy; không có PreToolUse guard (README tự ghi nhận).
- **Hồ sơ vòng 1 — ĐÃ GIẢI TRÌNH 26/9/2026** (người dùng): thư mục dự án là thư mục làm việc cá nhân; sản phẩm chia sẻ chỉ
  gồm plugin .zip, .skill phát hành và văn bản kèm theo (ChatGPT xác nhận zip 1.2.1 sạch) → không ảnh hưởng. Từ vòng 2 chỉ gửi
  zip plugin phát hành + văn bản. Đã đưa vào BC tiếp thu v2 (nội dung 6.3) và BC quá trình xây dựng v2 (Mục 6), cả hai Track Changes.
- Chờ Lãnh đạo quyết: phương án nhật ký (metadata mặc định, trích đoạn ≤200 ký tự khi có tín hiệu học, xóa sau 30 ngày),
  đơn vị thí điểm, giữ sao lưu theo lịch.
- Gemini (2 báo cáo) sai đối tượng — không dùng; vòng 2 gửi lại đúng hồ sơ.

**Cập nhật 26/9/2026 (thẩm định lần 2):** 4 lỗi Mức 1 đã khắc phục **trên sản phẩm** — plugin 1.3.0 (`DL-20260926-001`, bằng chứng `30-Ket-Qua/2026-09-26/Plugin/BANG-CHUNG-KIEM-THU-1.3.0.md`). Phương án nhật ký đổi sang chọn ghi (`#học`/`KTC_NHAT_KY_NOI_DUNG=1`). Báo cáo tiếp thu lần 2, TB v5, HD v4, BC quá trình v3 (Track Changes) tại `30-Ket-Qua/2026-09-26/Soan-Thao/`. **Còn mở:** nghiệm thu Chat/Cowork (5–6 ca/nền tảng, trước 05/10); rà soát 897 hai vòng TB v5 + HD v4 (trước 03/10); kiểm kê + chuyển bản cũ sang "Not available" ở cấp tổ chức (Phòng QLKHCN&HTPT); thẩm định vòng 3 trên zip 1.3.0; mã `THANG_DIEM_CHUA_PHAN_DINH` vào đầu ra `kpi_calc.py`; HD thiếu số trang (TT11); commit git.
