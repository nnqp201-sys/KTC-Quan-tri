# Du-lieu-Cong-Viec — Kho dữ liệu nền định lượng

Không phải một hệ AI, mà là **kho dữ liệu chuẩn** để định lượng công việc: nhiệm vụ nào thuộc Trục/Nội hàm
nào, quy đổi bao nhiêu điểm, đo bằng chỉ số KPI nào, đánh giá theo khung tiêu chí nào.

Tra ở đây trước — **không tự đặt ra thang điểm hay tiêu chí mới**.

## Ba nhánh nội dung

| Thư mục | Nội dung |
|---|---|
| `DANH MUC SAN PHAM CONG VIEC/` | `Bang tong hop_phan tich_DANH_MUC_NHIEM_VU_CHUAN...xlsx` — **122 nhiệm vụ chuẩn** (mã `A01`–`S04`, 17 lĩnh vực) gộp từ 1.358 dòng nhiệm vụ gốc của 69 tệp Biểu số 1, kèm bảng đối chiếu 100% nhiệm vụ gốc → nhiệm vụ chuẩn và phân loại theo 18 loại tài liệu. `Du thao_Danh_muc_SP_theo_loai_van_ban_va_6_truc.xlsx` — **371 sản phẩm** quy đổi, gắn loại văn bản (29 loại) + Nhóm/Điểm/Hệ số + Trục + Nội hàm |
| `CHI SO KPI/` | KPI cấp Trường phân bổ cho Lãnh đạo Trường; KPI cá nhân dùng chung theo 9 chức danh; 5 bộ KPI cá nhân riêng theo phòng và chủ nhiệm/quản lý phòng xưởng |
| `KHUNG TIEU CHI DANH GIA...` | Khung đánh giá tập thể 11 đơn vị (mỗi đơn vị 1 `.xlsx` khung + 1 `.docx` phân tích); `Truong_LDT/` — Trường, tập thể Lãnh đạo Trường, Hiệu trưởng, Phó Hiệu trưởng; `Khung cá nhân/` — 6 phụ lục II–VII theo nhóm chức danh |

## Văn bản gốc — trích dẫn văn bản, không trích tệp Excel

Toàn bộ dữ liệu ở đây là **dẫn xuất**. Khi cần căn cứ, trích văn bản gốc trong
`KTC-Database/02-KTC-Regulations/`:

| Văn bản | Vai trò |
|---|---|
| Thông báo 817/TB-CĐKT | Nguồn gốc 6 Trục và 38 Nội hàm, cụ thể hóa HD 02-HD/BTCTW ngày 22/5/2026 |
| Quyết định **1923/QĐ-CĐKT ngày 30/8/2026** (Hiệu trưởng Lê Trí Khải) | Ban hành Quy chế đánh giá, xếp loại chất lượng gắn KPI — căn cứ pháp lý của toàn bộ khung đánh giá |
| Phụ lục I, II, III kèm QĐ 1923 | Mẫu kế hoạch công tác quý đơn vị · mẫu kế hoạch/danh mục công việc cá nhân · mẫu phiếu đánh giá xếp loại |

Phụ lục I có đúng hai cột `Điểm chấm công việc` và `Hệ số quy đổi` — tức thang 5 nhóm dưới đây được áp
trực tiếp trên biểu mẫu chính thức.

## Bộ mã dùng chung

- **6 Trục** kết quả trọng tâm, dưới đó **38 Nội hàm** (số nội hàm đánh lại từ 1 trong từng Trục — luôn ghi
  kèm Trục, không dùng số nội hàm đứng một mình).
- **5 nhóm quy đổi**: Nhóm 1 = 50 điểm/hệ số 0,5 · Nhóm 2 = 120/1,2 · Nhóm 3 = 250/2,5 · Nhóm 4 = 350/3,5 ·
  Nhóm 5 = 450/4,5.
- **17 lĩnh vực** nhiệm vụ chuẩn A–S (không có chữ J và O).
- **4 mức xếp loại**: Hoàn thành xuất sắc nhiệm vụ (≥ 90 điểm) · Hoàn thành tốt nhiệm vụ (70–89) ·
  Hoàn thành nhiệm vụ (50–69) · Không hoàn thành nhiệm vụ (< 50). Thang 100 điểm = 30 điểm tiêu chí chung
  + 70 điểm tiêu chí kết quả thực hiện nhiệm vụ.

Bảng giá trị hợp lệ đầy đủ: `02-Master-Task-Register/Master-Task-Register_20260913_v0.1.xlsx`,
sheet `02-Danh-muc-tra-cuu`.

## Ba cảnh báo về chất lượng dữ liệu

1. **Độ phủ mới đạt 5/11 đơn vị.** 1.358 nhiệm vụ gốc chỉ đến từ Phòng TH-HC&QT (402), QLKHCN&HTPT (387),
   QLĐT&BĐCL (366), Phòng Tổ chức (126), TC-KT (77). **Sáu Khoa hoàn toàn vắng mặt** — lĩnh vực
   `S. Nhiệm vụ chuyên môn nhà giáo` chỉ có 4 nhiệm vụ, sinh ra từ viên chức Phòng có tham gia giảng dạy.
   Do đó **không được coi 122 nhiệm vụ chuẩn là danh mục đầy đủ**.
2. **Danh mục 371 sản phẩm mới ở mức dự thảo lần 4** — điểm và hệ số quy đổi chưa phải bản ban hành. Khi
   trích dẫn phải ghi rõ là dự thảo.
3. **Bảng tổng hợp tự mâu thuẫn ở Trục 1**: sheet `Tong hop theo Truc` ghi 102 sản phẩm, nhưng chính dòng
   đó cộng theo nhóm ra 103 (54+37+7+4+1), và đếm trực tiếp trên sheet dữ liệu cũng ra 103. Lệch 1 sản phẩm,
   chưa rõ nguyên nhân.

## Ghi chú kỹ thuật

Tên ba thư mục con hiện dùng chữ hoa + khoảng trắng + lẫn dấu tiếng Việt
(`KHUNG TIEU CHI DANH GIA TAP THE VÀ CA NHAN`, còn `thuuoc` gõ sai ở thư mục cấp 3). Điều này khác quy ước
không dấu của cả workspace và **làm vỡ lệnh shell** khi xử lý hàng loạt. Việc đổi tên xếp vào nhóm cần sửa
kèm, chưa thực hiện.
