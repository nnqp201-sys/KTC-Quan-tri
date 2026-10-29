---
paths:
  - "11-Du-lieu-Cong-Viec/**"
description: Danh mục nhiệm vụ chuẩn, sản phẩm quy đổi, KPI, khung đánh giá
---

# 11-Du-lieu-Cong-Viec — lớp dữ liệu nền của cả dự án

Không phải một hệ AI, mà là **kho dữ liệu chuẩn** để định lượng công việc; ba nhánh:

| Thư mục | Nội dung |
|---|---|
| `DANH MUC SAN PHAM CONG VIEC/` | **Mã chính thức từ 27/10/2026 — danh mục của phần mềm KPI tỉnh** (`N1_241`, `T4_461`): `danh-muc-spcv-pm-kpi.csv` (455 mã, ánh xạ sang QĐ 2119 để lấy hệ số), mục lục `00-MUC-LUC-DANH-MUC-SPCV-PM-KPI.md`; sinh bằng `29-Cong-Cu/trich_danh_muc_pm_kpi.py`, xuất tệp nạp bằng `29-Cong-Cu/xuat_mau_import_kpi.py`. 39 mã (`T1`–`T6`, `N1_460`) chưa có hệ số → `THIEU_DU_LIEU`, không tự đặt. Nền cũ: `Bang tong hop_phan tich_DANH_MUC_NHIEM_VU_CHUAN...xlsx` — **122 nhiệm vụ chuẩn** (mã `A01`–`S04`, 17 lĩnh vực) gộp từ 1.358 dòng nhiệm vụ gốc của 69 file Biểu số 1; kèm bảng đối chiếu 100% nhiệm vụ gốc → nhiệm vụ chuẩn và phân loại theo 18 loại tài liệu. `Du thao_Danh_muc_SP_theo_loai_van_ban_va_6_truc.xlsx` — **371 sản phẩm** quy đổi, gắn loại văn bản + Nhóm/Điểm/Hệ số + Trục + Nội hàm (**dự thảo lần 4**) |
| `CHI SO KPI/` | **Bộ chỉ số KPI chính thức — QĐ 2164/QĐ-CĐKT ngày 30/9/2026**, 55 phụ lục trong `Bo-chi-so-KPIs/` (I–XI tập thể 11 đơn vị, XII Lãnh đạo Trường, XIII–XXXII cá nhân theo đơn vị, chức danh); tra nhanh `00-MUC-LUC-BO-CHI-SO-KPI-QD2164.md`, `bo-chi-so-kpi-QD2164.csv`. Bộ dự thảo 4 - 8/9 đã lưu trữ, không dùng |
| `KHUNG TIEU CHI DANH GIA...` | Khung đánh giá tập thể 11 đơn vị (mỗi đơn vị 1 `.xlsx` khung + 1 `.docx` phân tích); `Truong_LDT/` — Trường, tập thể Lãnh đạo Trường, Hiệu trưởng, Phó Hiệu trưởng; `Khung cá nhân/` — 6 phụ lục II–VII theo nhóm chức danh |

Đây là nguồn để trả lời "nhiệm vụ này thuộc Trục/Nội hàm nào, quy đổi bao nhiêu điểm, đo bằng KPI nào" —
tra ở đây trước, không tự đặt ra thang điểm hay tiêu chí mới.
