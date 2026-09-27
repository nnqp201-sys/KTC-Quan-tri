# Bằng chứng kiểm thử — plugin ktc-quan-tri 1.3.2

**Lập tự động** bởi `29-Cong-Cu/lap_bang_chung_plugin.py` lúc 27/09/2026 20:31 — mọi con số lấy từ nhật ký trong thư mục này.

## 1. Artifact

| Mục | Giá trị |
|---|---|
| Tệp | `ktc-quan-tri-1.3.2.zip` (269 tệp) |
| SHA-256 | `83cd2815113ce30de0a7af64c6f1eee99c83907fca18a180312516848ffa7959` (tính lại khớp tệp `.sha256`) |
| Lặp lại được | `log-dung-*-lan-2.txt` nếu có (dòng cuối ghi mã của hai lần dựng) |
| Danh mục tệp | `DANH-MUC-TEP-1.3.2.md` (SHA-256 từng tệp) |
| So với bản trước | `ktc-quan-tri-1.3.1.zip` SHA-256 `e7af7718bbbf1a9181668ad346f4eefc1359ef48b1227172b2972618b7dc4821`; thêm 0 tệp: —; bỏ 0 tệp: — |
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
| Git | `93df213` — mã nguồn dựng plugin sạch (không có thay đổi chưa commit trong 11 thư mục nguồn): bản dựng truy về đúng commit này |

## 4. Kết quả

| Phép kiểm | Kết quả | Nhật ký |
|---|---|---|
| `claude plugin validate ./31-Plugin --strict` | ĐẠT (mã 0) | `log-validate-strict-1.3.2.txt` |
| Kiểm tra tĩnh toàn hệ | KẾT LUẬN: 28 LỖI · 0 cảnh báo (mã 1) | `log-kiem-tra-he-thong-1.3.2.txt` |
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
| `test_plugin_131` | 0 | 105 |
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

## Ghi chú kiểm tra tĩnh "28 LỖI"

Cả 28 lỗi là phép kiểm **C12**: 28 tệp đầu vào người phụ trách nạp vào `10-Dau-Vao/04-Chuyen-de/` ngày 27/9/2026 đã có sẵn
trong KTC-Database (quy tắc: trỏ, không chép). Không có tệp nào thuộc plugin. Danh mục chờ quyết định:
`30-Ket-Qua/2026-09-27/Van-hanh/DANH-MUC-28-TEP-DAU-VAO-TRUNG-KHO_cho-duyet.md`. Kiểm tra toàn hệ **chưa xanh** cho đến khi
người phụ trách quyết định.

## Nghiệm thu Claude Code cho bản 1.3.2

| Đợt | Bản dựng | Ca, lượt đạt | Ghi chú |
|---|---|---|---|
| dot4 | 1.3.1 (`e7af7718…4821`) | 15/15 ca, 30/30 lượt | Nội dung 8 skill, 7 agent giống 1.3.2 trừ 1 câu đường dẫn quy tắc cho agent |
| dot5 | 1.3.2 trước sửa sed (`864d9063…0d43`, commit `2fc003f`) | 11/15 ca, 26/30 lượt | 1 lượt quá thời gian chờ (ca 14); 1 giám khảo AI chấm oan (ca 01); ca 12 lượt 2 không kích hoạt kỹ năng báo cáo (thiếu mã cảnh báo, nội dung an toàn); ca 13 lượt 2 đưa kèm phương án ghi số hiệu Luật trái quy ước (có cảnh báo) |

Bản phát hành 1.3.2 (`83cd2815…7959`) khác bản chạy dot5 đúng: `scripts/ktc_guard.py` (sed/perl -i chỉ xét tệp đích),
`CHANGELOG.md`, `README.md`; 8 skill, 7 agent giống từng byte (`diff -rq`, cờ `defaultEnabled` do script nghiệm thu bật
trên bản sao). `runsPerCase` trong `dot5-ket-qua.json` = 2, khớp số lượt chạy (F4-04).
