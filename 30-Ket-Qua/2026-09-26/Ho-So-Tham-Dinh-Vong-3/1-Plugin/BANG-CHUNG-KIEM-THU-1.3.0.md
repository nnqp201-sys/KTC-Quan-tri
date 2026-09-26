# Bằng chứng kiểm thử — plugin ktc-quan-tri 1.3.0

**Lập tự động** bởi `29-Cong-Cu/lap_bang_chung_plugin.py` lúc 26/09/2026 20:13 — mọi con số lấy từ nhật ký trong thư mục này.

## 1. Artifact

| Mục | Giá trị |
|---|---|
| Tệp | `ktc-quan-tri-1.3.0.zip` (260 tệp) |
| SHA-256 | `2d0c795a79a0afb906183f31ef6c3841e5b9faddb4ed558052a81e1ecd5b4c87` (tính lại khớp tệp `.sha256`) |
| Lặp lại được | `log-dung-*-lan-2.txt` nếu có (dòng cuối ghi mã của hai lần dựng) |
| Danh mục tệp | `DANH-MUC-TEP-1.3.0.md` (SHA-256 từng tệp) |
| So với bản trước | `ktc-quan-tri-1.2.1.zip` SHA-256 `4876e3753e20d6709d2624e1bdabc12495d4f02b6f60a5acc78f3f9bc57eea73`; thêm 2 tệp: `scripts/ktc_guard.py`, `skills/quan-tri/CHANGELOG.md`; bỏ 1 tệp: `scripts/ktc_backup_github.py` |
| Không chứa | `.git/`, `KPI-ca-nhan/`, `*.jsonl`, `ktc_backup_github.py` |

## 2. Hooks — trước và sau

| Bản trước | Bản này |
|---|---|
| SessionStart: ktc_quan_tri_doctor.py | SessionStart: ktc_quan_tri_doctor.py |
| SessionStart: ktc_nhat_ky.py nap | SessionStart: ktc_nhat_ky.py nap |
| SessionStart: ktc_backup_github.py --neu-can | PreToolUse: ktc_guard.py |
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
| Git | `c95507e` — mã nguồn dựng plugin sạch (không có thay đổi chưa commit trong 11 thư mục nguồn): bản dựng truy về đúng commit này |

## 4. Kết quả

| Phép kiểm | Kết quả | Nhật ký |
|---|---|---|
| `claude plugin validate ./31-Plugin --strict` | ĐẠT (mã 0) | `log-validate-strict-1.3.0.txt` |
| Kiểm tra tĩnh toàn hệ | KẾT LUẬN: 0 LỖI · 0 cảnh báo (mã 0) | `log-kiem-tra-he-thong-1.3.0.txt` |
| Bộ hồi quy | 20/20 bộ mã thoát 0 | `log-hoi-quy/` |

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
