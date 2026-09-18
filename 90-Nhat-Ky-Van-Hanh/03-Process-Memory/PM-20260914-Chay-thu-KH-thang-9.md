# PM-20260914 — Chạy thử KTC-Ke-Hoach, kỳ kế hoạch tháng 9/2026

**Ngày:** 14/9/2026 · **Hệ:** `KTC-Ke-Hoach` (KTC-PIS) v3.1 · **Nền tảng:** Claude Code
**Loại:** Chạy thử kỹ thuật, không phải kỳ vận hành thật
**Sản phẩm:** `23-KTC-Ke-Hoach/Xuat_Ke_Hoach/output_KH-Thang/2026-09-14_Chay-thu-KH-Thang-9-2026/01. Bao cao chay thu KH thang 9-2026 - KTC-Ke-Hoach v3.1.docx`

## Vì sao chạy

Ba hệ `KTC-Ke-Hoach`, `KTC-Soan-Thao-VB`, `KTC-Theo-doi-CV` chưa có sản phẩm chạy thử nào lưu lại —
`KTC-Bao-Cao` là hệ duy nhất có. `SKILL.md` của `KTC-Ke-Hoach` tự khai *"sửa quy trình sau đợt chạy thử
kế hoạch tháng 9/2026"*, tức là đợt chạy **đã diễn ra nhưng không giữ sản phẩm**. Đợt này chạy lại có
lưu vết, đồng thời kiểm chứng quy tắc v3.1 trên dữ liệu thật (`KI-010`).

## Cách làm

Không dựng bản kế hoạch cạnh tranh với `KH-834` (đã ban hành 6/9/2026). Thay vào đó lấy bản đã ban hành
làm chuẩn, truy ngược từng nhiệm vụ về các nguồn mà v3.1 quy định. **Chỉ tính KHỚP khi trùng tuyệt đối.**

Dữ liệu đã đối chiếu thật: `KH-834` (47 nhiệm vụ, từ `KTC-Database/02-KTC-Regulations`) · Kế hoạch quý III
(54) · Chương trình công tác năm 2026 (97) · 12 tệp kế hoạch tháng 9 của đơn vị (150 nhiệm vụ).

## Kết quả

| Phép đo | Kết quả |
|---|---|
| Điều kiện lọc cấp Trường | **Xác nhận** — 47/47 và 54/54 = 100% trên hai văn bản đã ban hành |
| Giả thuyết A (v3.1: trích từ KH quý) | Chỉ giải thích **14/47 = 30%** |
| Giả thuyết B (cách cũ: gộp từ đơn vị) | **3/28**; gộp từ dưới lên + lọc cấp Trường cho **99** so với 47 thật — bác bỏ lại lần nữa |
| Chương trình công tác năm 2026 | **0** nhiệm vụ khớp |
| Không truy được về nguồn nội bộ nào | **30/47 = 64%** |

**Nguồn thứ ba chưa được mô hình hóa.** Trong 28 nhiệm vụ không truy được về kế hoạch quý: 8 trích dẫn
một văn bản cấp trên **ban hành sau** kế hoạch quý (KH 295/KH-UBND, KH 303/KH-UBND, KH 101-KH/TU,
NĐ 308/2026/NĐ-CP, TT 63/2026/TT-BGDĐT, NQ 398/NQ-UBTVQH16); 20 là việc điều hành phát sinh (chuyển đổi
số và AI 6, cơ sở vật chất 5, tài chính 3, tổ chức - cán bộ 3).

## Lệch chuẩn / bất thường

1. **Con số trong Skill 36 v2.0 sai.** Skill ghi `KH-834` có **53** nhiệm vụ; đếm thật được **47**.
   Chênh 6 đúng bằng số dòng tiêu đề Trục rỗng của Mục II — nhiều khả năng đợt trước đếm cả dòng tiêu đề.
2. **Hai nhiệm vụ đến hạn Tháng 9 trong kế hoạch quý không có ở `KH-834`** — Trục 2.3 (Phương án giá dịch
   vụ đào tạo) và Trục 4.5 (Báo cáo sơ kết quý III của Đảng ủy). Chưa rõ bỏ sót hay chủ động lùi.
   **Không suy diễn** — cần người tổng hợp kế hoạch xác nhận.
3. **Phép đo đầu tiên của chính đợt này SAI.** Hàm đọc bảng lấy `worksheets[0]`, nên 3 tệp có sheet
   `Mẫu KH Quý` đứng trước bị đọc nhầm sheet rỗng → ra 126 nhiệm vụ / 9 đơn vị thay vì 150 / 12. Sửa bằng
   cách chọn sheet có nhiều dòng nhất — **vẫn sai**, vì Khoa Sư phạm để nguyên 4 dòng mẫu điền dấu `…` ở
   sheet quý trong khi sheet tháng chỉ có 2 nhiệm vụ thật. Phải đếm dòng **có nội dung thật**.
   Đúng `BH-02`: trả về rỗng phải bị coi là bất thường, không phải kết quả hợp lệ.

## Chất lượng dữ liệu đơn vị ghi nhận được

| Đơn vị | Hiện tượng |
|---|---|
| Khoa Sư phạm | Chỉ 2 nhiệm vụ thật; còn nguyên 4 dòng mẫu `…` ở sheet quý |
| Khoa ĐT&SHLX · Khoa Y - Dược | Để nguyên sheet `Mẫu KH Quý` trống trong tệp kế hoạch tháng |
| Phòng QLKHCN&HTPT | Tệp kế hoạch tháng 9 nhưng sheet tên `KE HOACH CONG TAC THANG  8` |
| Phòng TCCB&CTHSSV | Dùng mẫu **Báo cáo** cho tệp kế hoạch — lặp lại lỗi đã ghi ở `KI-006` |
| Đoàn TN - Hội SV | Chưa thấy tệp kế hoạch tháng 9 |

## Phát hiện ngoài dự kiến

- **`KI-008` có lời giải.** `KH-834` có nhiệm vụ *"Ban hành kế hoạch triển khai phần mềm VNPT KPI - Hệ
  thống quản lý đánh giá, xếp loại..."*. Phần mềm KPI được nhắc trong QĐ 1923 chính là **VNPT KPI**, và
  tính đến 6/9/2026 Trường **mới đang lập kế hoạch triển khai**, chưa vận hành.
- **`KI-001` có bằng chứng định lượng.** 5 cặp nhiệm vụ đạt độ giống 63–80% nhưng là **khớp giả** — khác
  số hiệu văn bản (TT 64 vs TT 43, NĐ 271 vs NĐ 159, Khoa KHCB vs Khoa Sư phạm). Nhiệm vụ hành chính dùng
  khuôn chữ lặp, phần phân biệt chỉ là số hiệu chiếm tỷ lệ nhỏ trong câu.
- **Dữ liệu kế hoạch đang nằm nhầm hệ.** 12 tệp kế hoạch tháng 9 của đơn vị nằm ở
  `25-KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/`, không ở `KTC-Ke-Hoach`, do đơn vị nộp gộp báo cáo tháng 8
  và kế hoạch tháng 9 cùng lần. Thư mục `input-KH_Thang/` của `KTC-Ke-Hoach` chỉ có 1 thư mục con và rỗng.

## Việc chưa làm

- Bước 0 Pre-flight (Skill 34) chưa chạy đúng quy trình — đợt này đi thẳng vào đối chiếu.
- Bước 5 (`KTC-Ra-Soat-897`) không áp dụng: sản phẩm không phải văn bản trình ký.
- Chưa sửa Skill 36 theo kết quả — cần quyết định, xem mục dưới.

## Đề nghị xử lý

1. Sửa con số `53 → 47` trong `36-Skill-Tong-Hop-Ke-Hoach-Truong.md` (rõ ràng, sửa được ngay).
2. Bổ sung **nguồn thứ ba** vào BƯỚC 0 của Skill 36: *văn bản cấp trên ban hành trong kỳ* — cần soạn quy
   tắc rà quét, chưa làm trong đợt này.
3. Hỏi người tổng hợp kế hoạch về 2 nhiệm vụ đến hạn tháng 9 bị thiếu.
4. Thống nhất nơi nộp kế hoạch tháng của đơn vị — hiện đang lẫn vào thư mục của hệ Báo cáo.

**Liên quan:** `KI-001` · `KI-006` · `KI-008` · `KI-010` · `36-Skill-Tong-Hop-Ke-Hoach-Truong.md` v2.0
