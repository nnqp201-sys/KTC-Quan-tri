# 29-Cong-Cu — Công cụ Python

Thư mục chứa script Python của dự án KTC-Quan-tri. Tất cả chạy từ thư mục gốc dự án.

## Entrypoint chính

| Script | Mục đích | Mã thoát |
|---|---|---|
| `doctor.py` | **Kiểm tra sức khỏe hệ thống** — gọi 5 bước kiểm tra, in kết luận ĐẠT/KHÔNG ĐẠT | 0/1 |
| `kiem_tra_he_thong.py` | Tầng 1: 13 phép kiểm tĩnh (gói skill, liên kết, tệp trùng) | 0/1 |
| `dong_goi_plugin.py` | Đóng gói plugin `ktc-quan-tri` vào `31-Plugin/` | 0/1 |
| `dong_goi_ra_soat_897.py` | Đóng gói `ktc-ra-soat-897` cá nhân | 0/1 |

## Kiểm tra / đo lường

| Script | Mục đích |
|---|---|
| `kiem_the_thuc.py` | Đo thể thức .docx (lề, phông, cỡ chữ) — hook gọi tự động |
| `kiem_vien_dan.py` | Kiểm viện dẫn văn bản (VD01–VD12) |
| `kiem_thuat_ngu.py` | Kiểm thuật ngữ pháp lý (TN01–TN04) |
| `kiem_minh_chung.py` | Kiểm minh chứng nhiệm vụ (MC01–MC07) |
| `doi_soat_so_lieu.py` | Đối soát số liệu kế hoạch/báo cáo đơn vị (DS01–DS06) |
| `tra_hieu_luc.py` | Quét hiệu lực văn bản viện dẫn |

## Báo cáo / kế hoạch

| Script | Mục đích |
|---|---|
| `bc_thang.py` | Dựng báo cáo tháng cấp Trường (nguon, trich, word, phu-luc, ke-hoach) |
| `fill_bc736.py` | Điền mẫu TB 736 (dự phòng) |
| `vanphong.py` | Chuẩn văn phong cấp Trường |

## KPI cá nhân

| Script | Mục đích |
|---|---|
| `kpi_calc.py` | Tính điểm KPI theo phương án A, A×B |
| `kpi_danh_gia.py` | Tự đánh giá KPI cuối quý |
| `kpi_nhat_quan.py` | Kiểm nhất quán hồ sơ KPI (NQ01–NQ10) |
| `lap_ho_so_minh_chung.py` | Lập bảng tổng hợp hồ sơ, minh chứng |
| `kpi_doi_chieu_cheo.py` | Đối chiếu chéo nhiều hồ sơ KPI |

## Tiện ích

| Script | Mục đích |
|---|---|
| `duong_dan.py` | Dò đường dẫn KTC-Database (Drive, biến môi trường) |
| `ktc_trackchanges.py` | Track Changes mức OOXML |
| `xuat_mau_import_kpi.py` | Xuất tệp nạp phần mềm KPI tỉnh |

## Thư mục con

- `plugin_src/` — Nguồn hook, agent, script đóng vào plugin
- `hoi_dap_chinh_sach/` — Thu thập hỏi đáp chính sách từ web
- `web_app/` — Web app rà soát 897 (Flask)
- `_trung_gian/` — Tệp tạm, xóa được

## Quy ước

- Mọi script có docstring và `--help`.
- Mã thoát: 0 = thành công, 1 = lỗi/cảnh báo nghiêm trọng, 2 = không hỗ trợ.
- Không ghi vào KTC-Database, 03-Templates(1), 04-Good-Documents.
