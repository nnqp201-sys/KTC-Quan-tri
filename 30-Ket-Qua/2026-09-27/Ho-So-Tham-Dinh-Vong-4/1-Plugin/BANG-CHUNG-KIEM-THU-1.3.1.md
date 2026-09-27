# Bằng chứng kiểm thử — plugin ktc-quan-tri 1.3.1

**Lập tự động** bởi `29-Cong-Cu/lap_bang_chung_plugin.py` lúc 27/09/2026 11:29 — mọi con số lấy từ nhật ký trong thư mục này.

## 1. Artifact

| Mục | Giá trị |
|---|---|
| Tệp | `ktc-quan-tri-1.3.1.zip` (269 tệp) |
| SHA-256 | `e7af7718bbbf1a9181668ad346f4eefc1359ef48b1227172b2972618b7dc4821` (tính lại khớp tệp `.sha256`) |
| Lặp lại được | `log-dung-*-lan-2.txt` nếu có (dòng cuối ghi mã của hai lần dựng) |
| Danh mục tệp | `DANH-MUC-TEP-1.3.1.md` (SHA-256 từng tệp) |
| So với bản trước | `ktc-quan-tri-1.3.0.zip` SHA-256 `2d0c795a79a0afb906183f31ef6c3841e5b9faddb4ed558052a81e1ecd5b4c87`; thêm 9 tệp: `skills/bao-cao/references/00-Quy-Tac-Bat-Bien-Day-Du.md`, `skills/bao-cao/references/LICH-SU-PHIEN-BAN.md`, `skills/ke-hoach/references/00-Quy-Tac-Bat-Bien-Day-Du.md`, `skills/kpi-lap-ke-hoach/references/00-Quy-Tac-Bat-Bien-Day-Du.md`, `skills/kpi-tu-danh-gia/references/00-Quy-Tac-Bat-Bien-Day-Du.md`, `skills/quan-tri/references/00-Quy-Tac-Bat-Bien-Day-Du.md`, `skills/soan-thao-vb/references/00-Quy-Tac-Bat-Bien-Day-Du.md`, `skills/the-thuc/references/00-Quy-Tac-Bat-Bien-Day-Du.md`, `skills/theo-doi-cv/references/00-Quy-Tac-Bat-Bien-Day-Du.md`; bỏ 0 tệp: — |
| Không chứa | `.git/`, `KPI-ca-nhan/`, `*.jsonl`, `ktc_backup_github.py` |

## 2. Hooks — trước và sau

| Bản trước | Bản này |
|---|---|
| SessionStart: ktc_quan_tri_doctor.py | SessionStart: ktc_quan_tri_doctor.py |
| SessionStart: ktc_nhat_ky.py nap | SessionStart: ktc_nhat_ky.py nap |
| PreToolUse: ktc_guard.py | PreToolUse: ktc_guard.py |
| PostToolUse: ktc_nhat_ky.py ghi | PostToolUse: ktc_nhat_ky.py ghi |
| PostToolUse: ktc_the_thuc_hook.py | PostToolUse: ktc_the_thuc_hook.py |
| UserPromptSubmit: ktc_nhat_ky.py yeu-cau | UserPromptSubmit: ktc_nhat_ky.py yeu-cau |
| SessionEnd: ktc_nhat_ky.py ket-phien | SessionEnd: ktc_nhat_ky.py ket-phien |

## 3. Môi trường

| Thành phần | Phiên bản |
|---|---|
| Hệ điều hành | Windows-11-10.0.26200-SP0 |
| Python | 3.13.15 |
| python-docx | 1.2.0 |
| openpyxl | 3.1.5 |
| lxml | 6.1.2 |
| Claude Code CLI | 2.1.283 (Claude Code) |
| Git | `0d9188d` — mã nguồn dựng plugin sạch (không có thay đổi chưa commit trong 11 thư mục nguồn): bản dựng truy về đúng commit này |

## 4. Kết quả

| Phép kiểm | Kết quả | Nhật ký |
|---|---|---|
| `claude plugin validate ./31-Plugin --strict` | ĐẠT (mã 0) | `log-validate-strict-1.3.1.txt` |
| Kiểm tra tĩnh toàn hệ | KẾT LUẬN: 28 LỖI · 0 cảnh báo (mã 1) | `log-kiem-tra-he-thong-1.3.1.txt` |
| Bộ hồi quy | 21/21 bộ mã thoát 0 | `log-hoi-quy/` |

| Bộ | Mã thoát | Dòng OK |
|---|---:|---:|
| `test_c11_ban_goc_trong_zip` | 0 | 0 |
| `test_c12_c13_kho_va_o_dia` | 0 | 6 |
| `test_c14_cong_cu_agent` | 0 | 5 |
| `test_c5_soi_trong_goi` | 0 | 0 |
| `test_doi_soat_so_lieu` | 0 | 24 |
| `test_he_ngoai` | 0 | 6 |
| `test_kiem_minh_chung` | 0 | 15 |
| `test_kiem_the_thuc` | 0 | 17 |
| `test_kiem_tra_he_thong` | 0 | 0 |
| `test_kiem_vien_dan` | 0 | 24 |
| `test_kpi_calc` | 0 | 47 |
| `test_kpi_danh_gia` | 0 | 59 |
| `test_kpi_trinh_bay` | 0 | 27 |
| `test_plugin_130` | 0 | 94 |
| `test_plugin_131` | 0 | 89 |
| `test_plugin_nhat_ky_backup` | 0 | 34 |
| `test_task_id_bc736` | 0 | 7 |
| `test_tra_hieu_luc` | 0 | 17 |
| `test_trackchanges` | 0 | 0 |
| `test_tu_hoc` | 0 | 12 |
| `test_validate_plan` | 0 | 27 |

## 5. Chưa thực hiện (không trình bày như đã đạt)

- Nghiệm thu trên Claude (trò chuyện) và Claude Cowork.
- Kiểm kê, thu hồi bản cũ ở cấp tổ chức (Phòng QLKHCN&HTPT, quyền Owner).
- Guard không phân tích mã Python/JS nhúng trong lệnh shell; máy không có Python thì hook không chạy.
- Kiểm thử dùng dữ liệu giả lập hoặc mẫu biểu; chưa có dữ liệu vận hành thật.

## Ghi chú về "28 LỖI" của kiểm tra tĩnh

Cả 28 lỗi là phép kiểm **C12** (tệp đầu vào trùng KTC-Database): 29 tệp kế hoạch người dùng nạp ngày 27/9/2026 vào
`10-Dau-Vao/04-Chuyen-de/` đã có sẵn trong kho (C12 yêu cầu trỏ thay vì chép). Không có tệp nào thuộc plugin; mọi phép
kiểm còn lại đạt, 0 cảnh báo. Việc giữ hay xóa bản chép do người dùng quyết định (CLAUDE.md: không tự xóa tài liệu).

## Nghiệm thu Claude Code (đợt cuối, sau mọi sửa đổi)

`30-Ket-Qua/2026-09-27/Nghiem-thu/dot4-ket-qua.json`: 15/15 ca, 30/30 lượt đạt · CLI 2.1.283 · 6,90 USD · 868 giây.
Các đợt trước giữ làm bằng chứng quá trình: `dot1-` (dừng ở ca 05 do hạn mức phiên — lỗi hạ tầng, không tính),
`dot3-` (ca 10–15: 2/6 ca đạt → sửa mô tả `bao-cao` 3.15 và bộ chấm ca 13, 14).
