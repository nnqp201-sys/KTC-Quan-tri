# N14 — NHẬT KÝ KIỂM TRA PLUGIN 1.3.13 (nguyên văn)

Gộp nguyên văn các tệp nhật ký trong thư mục `1-Plugin/` và `1-Plugin/log-hoi-quy/` của hồ sơ vòng 6. Mỗi mục ghi tên tệp gốc và SHA-256 để đối chiếu.

## 1-Plugin/log-validate-strict-1.3.13.txt (sha256 `26811cff82df1ee54d46f734c3ac181b1aaa535b2b5f34667511cb9998d3f33f`)

````text
# Lệnh: claude plugin validate ./31-Plugin --strict
# CLI: 2.1.283 (Claude Code)
# Thời điểm: 29/09/2026 11:19
Validating plugin manifest: D:\.CLAUDE code\KTC-Quan-tri\31-Plugin\.claude-plugin\plugin.json

✔ Validation passed

# Mã thoát: 0
````

## 1-Plugin/log-kiem-tra-he-thong-1.3.13.txt (sha256 `fd0ee5fed471e0ec129ee1197cc17a041d308c3d8416f2ecf6abc613bc7d4aa2`)

````text
============================================================================
KIỂM TRA TOÀN HỆ hệ thống KTC — Tầng 1 (tĩnh, tất định)
Dự án: D:\.CLAUDE code\KTC-Quan-tri
============================================================================

────────────────────────────────────────────────────────────────────────────
C1. Gói .skill — cấu trúc và frontmatter
────────────────────────────────────────────────────────────────────────────
  ✓ ktc-bao-cao        52 tệp, hợp lệ
  ✓ ktc-ke-hoach       30 tệp, hợp lệ
  ✓ ktc-soan-thao-vb   95 tệp, hợp lệ
  ✓ ktc-theo-doi-cv    13 tệp, hợp lệ
  ✓ ktc-quan-tri       21 tệp, hợp lệ
  ✓ ktc-the-thuc       5 tệp, hợp lệ
  ✓ ktc-kpi-lap-ke-hoach 19 tệp, hợp lệ
  ✓ ktc-kpi-tu-danh-gia 16 tệp, hợp lệ

────────────────────────────────────────────────────────────────────────────
C2. Liên kết trong gói — đường dẫn references/ có tồn tại không
────────────────────────────────────────────────────────────────────────────
  ✓ ktc-bao-cao        không có liên kết gãy
  ✓ ktc-ke-hoach       không có liên kết gãy
  ✓ ktc-soan-thao-vb   không có liên kết gãy
  ✓ ktc-theo-doi-cv    không có liên kết gãy
  ✓ ktc-quan-tri       không có liên kết gãy
  ✓ ktc-the-thuc       không có liên kết gãy
  ✓ ktc-kpi-lap-ke-hoach không có liên kết gãy
  ✓ ktc-kpi-tu-danh-gia không có liên kết gãy

────────────────────────────────────────────────────────────────────────────
C3. Đường dẫn nêu trong tài liệu cấp dự án có thật không
────────────────────────────────────────────────────────────────────────────
  ✓ CLAUDE.md                                mọi đường dẫn đều tồn tại
  ✓ 00-README.md                             mọi đường dẫn đều tồn tại
  ✓ 22-KTC-Dieu-Phoi/SKILL.md                mọi đường dẫn đều tồn tại
  ✓ 20-Chuan-Chung/00-README.md              mọi đường dẫn đều tồn tại
  ✓ 90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md      mọi đường dẫn đều tồn tại

────────────────────────────────────────────────────────────────────────────
C4. Nguồn rời ↔ nội dung trong gói (gói CÓ THỂ mới hơn nguồn rời)
────────────────────────────────────────────────────────────────────────────
  ✓ ktc-bao-cao        đồng bộ hoàn toàn
  ✓ ktc-ke-hoach       đồng bộ hoàn toàn
  ✓ ktc-soan-thao-vb   đồng bộ hoàn toàn
  ✓ ktc-theo-doi-cv    đồng bộ hoàn toàn
  ✓ ktc-quan-tri       đồng bộ hoàn toàn
  ✓ ktc-the-thuc       đồng bộ hoàn toàn
  ✓ ktc-kpi-lap-ke-hoach đồng bộ hoàn toàn
  ✓ ktc-kpi-tu-danh-gia đồng bộ hoàn toàn

────────────────────────────────────────────────────────────────────────────
C5. 5 tệp dùng chung — khớp bản gốc 20-Chuan-Chung (soi cả bản rời lẫn bản TRONG GÓI)
────────────────────────────────────────────────────────────────────────────
  ✓ 00-Nguyen-Tac-Chung.md                         khớp ở mọi bản rời và 5 gói
  ✓ 00-Metadata-Schema.md                          khớp ở mọi bản rời và 3 gói
  ✓ 04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md       khớp ở mọi bản rời và 3 gói
  ✓ 30-Skill-Phan-Loai-6-Truc.md                   khớp ở mọi bản rời và 5 gói
  ✓ Skill-Vien-Dan-Van-Ban-Hop-Nhat.md             khớp ở mọi bản rời và 3 gói
  ✓ 17-Quy-Tac-Vien-Dan.md                         khớp ở mọi bản rời và 5 gói
  ✓ 18-Chuan-The-Thuc-San-Pham.md                  khớp ở mọi bản rời và 6 gói
  ✓ 19-Quy-Tac-KPI.md                              khớp ở mọi bản rời và 3 gói
  ✓ 10-Tu-Dien-Truong-Du-Lieu.md                   khớp ở mọi bản rời và 1 gói
  ✓ 11-Quy-Tac-Task-ID.md                          khớp ở mọi bản rời và 1 gói
  ✓ 12-Vong-Doi-Trang-Thai.md                      khớp ở mọi bản rời và 1 gói
  ✓ 13-Bang-Ma-Don-Vi.md                           khớp ở mọi bản rời và 1 gói

────────────────────────────────────────────────────────────────────────────
C6. Tên hệ đã bỏ còn sót (định tuyến gãy)
────────────────────────────────────────────────────────────────────────────
  ✓ không hệ nào còn trỏ tới tên đã bỏ

────────────────────────────────────────────────────────────────────────────
C7. Cụm từ hạ cấp chốt chặn bắt buộc
────────────────────────────────────────────────────────────────────────────
  ✓ không có chỗ nào hạ cấp 897 thành tùy chọn

────────────────────────────────────────────────────────────────────────────
C8. Sao chép chéo hệ — tệp trùng tên khác nội dung
────────────────────────────────────────────────────────────────────────────
  · 13 tệp chỉ trùng tên (giống < 50%) — không phải bản sao, bỏ qua
  · biến thể đã biết: 00b-Trigger-Vien-Dan-Van-Ban-Hop-Nhat.md — ktc-bao-cao thêm 1 đoạn lưu ý riêng (trùng số 33); bản 897/KTC-Database còn tên hệ cũ KTC-DIS — hệ ngoài, sửa tại hệ đó
  ✓ không có tệp trùng tên khác nội dung giữa các hệ

────────────────────────────────────────────────────────────────────────────
C9. Công cụ Python — import và tự kiểm
────────────────────────────────────────────────────────────────────────────
  ✓ ktc_trackchanges     import được, có kiem_tra()
  ✓ vanphong             import được, có cap_truong()
  ✓ noi_ham              import được, có trich()
  ✓ dong_goi_skill       import được, có kiem_frontmatter()
  ✓ kiem_vien_dan        import được, có kiem_tra()
  ✓ kiem_the_thuc        import được, có kiem_tep()
  ✓ tra_hieu_luc         import được, có quet()
  ✓ doi_soat_so_lieu     import được, có doi_soat()
  ✓ kiem_minh_chung      import được, có kiem()
  ✓ vanphong: 3/3 ca thử đạt

────────────────────────────────────────────────────────────────────────────
C11. Không tệp nào chỉ tồn tại bên trong gói .skill
────────────────────────────────────────────────────────────────────────────
  ✓ ktc-bao-cao        mọi tệp đều có bản nguồn ngoài zip
  ✓ ktc-ke-hoach       mọi tệp đều có bản nguồn ngoài zip
  ✓ ktc-soan-thao-vb   mọi tệp đều có bản nguồn ngoài zip
  ✓ ktc-theo-doi-cv    mọi tệp đều có bản nguồn ngoài zip
  ✓ ktc-quan-tri       mọi tệp đều có bản nguồn ngoài zip
  ✓ ktc-the-thuc       mọi tệp đều có bản nguồn ngoài zip
  ✓ ktc-kpi-lap-ke-hoach mọi tệp đều có bản nguồn ngoài zip
  ✓ ktc-kpi-tu-danh-gia mọi tệp đều có bản nguồn ngoài zip

────────────────────────────────────────────────────────────────────────────
C12. Đầu vào trùng KTC-Database (Nguyên tắc 4.4 — trỏ thay vì chép)
────────────────────────────────────────────────────────────────────────────
  ✓ 80 tệp đầu vào · 18 trùng thuộc ngoại lệ đã duyệt

────────────────────────────────────────────────────────────────────────────
C13. Không ghi cứng đường dẫn ổ đĩa (Nguyên tắc 4.2)
────────────────────────────────────────────────────────────────────────────
  ✓ 0 chỗ ghi cứng ổ đĩa

────────────────────────────────────────────────────────────────────────────
C14. Script agent viện dẫn đều được đóng vào plugin
────────────────────────────────────────────────────────────────────────────
  ✓ 0 script agent viện dẫn nhưng chưa đóng gói (2 agent nội bộ được miễn)

────────────────────────────────────────────────────────────────────────────
C10. Bộ hồi quy có chạy được không
────────────────────────────────────────────────────────────────────────────
  ✓ test_bc_thang.py                   chạy xong (mã 0)
  ✓ test_c11_ban_goc_trong_zip.py      chạy xong (mã 0)
  ✓ test_c12_c13_kho_va_o_dia.py       chạy xong (mã 0)
  ✓ test_c14_cong_cu_agent.py          chạy xong (mã 0)
  ✓ test_c5_soi_trong_goi.py           chạy xong (mã 0)
  ✓ test_doi_soat_so_lieu.py           chạy xong (mã 0)
  ✓ test_dung_lap_lai.py               chạy xong (mã 0)
  ✓ test_he_ngoai.py                   chạy xong (mã 0)
  ✓ test_kiem_minh_chung.py            chạy xong (mã 0)
  ✓ test_kiem_the_thuc.py              chạy xong (mã 0)
  ✓ test_kiem_tra_he_thong.py          chạy xong (mã 0)
  ✓ test_kiem_vien_dan.py              chạy xong (mã 0)
  ✓ test_kpi_calc.py                   chạy xong (mã 0)
  ✓ test_kpi_danh_gia.py               chạy xong (mã 0)
  ✓ test_kpi_trinh_bay.py              chạy xong (mã 0)
  ✓ test_plugin_130.py                 chạy xong (mã 0)
  ✓ test_plugin_131.py                 chạy xong (mã 0)
  ✓ test_plugin_nhat_ky_backup.py      chạy xong (mã 0)
  ✓ test_task_id_bc736.py              chạy xong (mã 0)
  ✓ test_thu_muc.py                    chạy xong (mã 0)
  ✓ test_tra_hieu_luc.py               chạy xong (mã 0)
  ✓ test_trackchanges.py               chạy xong (mã 0)
  ✓ test_tu_du_plugin.py               chạy xong (mã 0)
  ✓ test_tu_hoc.py                     chạy xong (mã 0)
  ✓ test_validate_plan.py              chạy xong (mã 0)

============================================================================
KẾT LUẬN: 0 LỖI · 0 cảnh báo
============================================================================
````

## 1-Plugin/log-dung-lai-1.3.13-tu-commit-16215a8.txt (sha256 `fd282a6c7ad9bbb9340f2c3356988ad923c50853741a62b0ea69ac019ed8f0da`)

````text
── Giai nen 8 goi .skill da xac minh vao 31-Plugin/skills/ ──
  ✓ quan-tri       <- 22-KTC-Dieu-Phoi\ktc-quan-tri.skill  (21 tep)
  ✓ bao-cao        <- 25-KTC-Bao-Cao\ktc-bao-cao-v3.20.skill  (52 tep)
  ✓ ke-hoach       <- 23-KTC-Ke-Hoach\ktc-ke-hoach-v3.12.skill  (30 tep)
  ✓ soan-thao-vb   <- 26-KTC-Soan-Thao-VB\ktc-soan-thao-vb-v1.15.skill  (95 tep)
  ✓ theo-doi-cv    <- 24-KTC-Theo-doi-CV\ktc-theo-doi-cv-v1.10.skill  (13 tep)
  ✓ the-thuc       <- 27-KTC-The-Thuc\ktc-the-thuc-v1.3.skill  (5 tep)
  ✓ kpi-lap-ke-hoach <- 28-KTC-KPI\ktc-kpi-lap-ke-hoach-v1.4.skill  (19 tep)
  ✓ kpi-tu-danh-gia <- 28-KTC-KPI\Tu-Danh-Gia\ktc-kpi-tu-danh-gia-v1.3.skill  (16 tep)
── Giải nén gói .skill lồng trong kỹ năng ──
── Ghi .claude-plugin/plugin.json ──
  ✓ plugin.json
── Ghi hooks/hooks.json (doctor + nhật ký + guard chặn ghi kho chuẩn) ──
  ✓ hooks.json
── Ghi scripts/ktc_quan_tri_doctor.py ──
  ✓ ktc_quan_tri_doctor.py
── Chép script/agent viết tay từ 29-Cong-Cu/plugin_src/ ──
  - scripts/ktc_backup_github.py (chỉ dùng nội bộ, không đóng vào plugin)
  ✓ scripts/ktc_guard.py
  ✓ scripts/ktc_nhat_ky.py
  ✓ scripts/ktc_the_thuc_hook.py
  ✓ scripts/ktc_thu_muc.py
  ✓ agents/ktc-hieu-luc-vien-dan.md
  ✓ agents/ktc-kiem-ho-so-don-vi.md
  ✓ agents/ktc-kiem-san-pham.md
  ✓ agents/ktc-tra-cuu-can-cu.md
  ✓ agents/ktc-tu-cai-tien.md
  ✓ agents/ktc-tu-hoc.md
  ✓ agents/ktc-xac-minh-minh-chung.md
  ✓ scripts/tra_hieu_luc.py (từ 29-Cong-Cu)
  ✓ scripts/kiem_vien_dan.py (từ 29-Cong-Cu)
  ✓ scripts/duong_dan.py (từ 29-Cong-Cu)
  ✓ scripts/doi_soat_so_lieu.py (từ 29-Cong-Cu)
  ✓ scripts/kiem_minh_chung.py (từ 29-Cong-Cu)
  ✓ scripts/kiem_the_thuc.py (từ 29-Cong-Cu)
  ✓ scripts/kpi_calc.py (từ 29-Cong-Cu)
  ✓ scripts/kpi_mau.py (từ 29-Cong-Cu)
  ✓ scripts/validate_plan.py (từ 29-Cong-Cu)
  ✓ scripts/kpi_danh_gia.py (từ 29-Cong-Cu)
  ✓ scripts/bc_thang.py (từ 29-Cong-Cu)
  ✓ scripts/vanphong.py (từ 29-Cong-Cu)
  ✓ scripts/trich_tuong_thuat.py (từ 29-Cong-Cu)
  ✓ scripts/ktc_trackchanges.py (từ 29-Cong-Cu)
── Lập bảng đối chiếu tên tệp (bản gốc dự án → vị trí trong plugin) ──
  ✓ skills\quan-tri\references\BAN-DO-TEP.md (17 dòng)
── Chèn chuẩn chung (lõi) vào mọi skill và agent; bản đầy đủ vào references/ của skill ──
  ✓ agents\ktc-hieu-luc-vien-dan.md          đã chèn
  ✓ agents\ktc-kiem-ho-so-don-vi.md          đã chèn
  ✓ agents\ktc-kiem-san-pham.md              đã chèn
  ✓ agents\ktc-tra-cuu-can-cu.md             đã chèn
  ✓ agents\ktc-tu-cai-tien.md                đã chèn
  ✓ agents\ktc-tu-hoc.md                     đã chèn
  ✓ agents\ktc-xac-minh-minh-chung.md        đã chèn
  ✓ skills\bao-cao\SKILL.md                  đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md · tách 13 mục lịch sử
  ✓ skills\ke-hoach\SKILL.md                 đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\kpi-lap-ke-hoach\SKILL.md         đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\kpi-tu-danh-gia\SKILL.md          đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\quan-tri\SKILL.md                 đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\soan-thao-vb\SKILL.md             đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\the-thuc\SKILL.md                 đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\theo-doi-cv\SKILL.md              đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
── Kiểm độ dài mô tả (plugin ≤ 500, skill/agent ≤ 1024 ký tự) ──
  ✓ mọi mô tả trong giới hạn
── Chuẩn hóa xuống dòng (dựng lặp lại được từ mọi bản checkout) ──
  ✓ 66 tệp đổi xuống dòng
── Đóng gói .zip (lặp lại được) ──
  ✓ 30-Ket-Qua\2026-09-29\Plugin\ktc-quan-tri-1.3.13.zip  (291 tệp, 1468987 bytes)
    sha256 d7c34a51e85f02278ec0e5a38c02089c0d7ae58280c8f59af6d0f673f9fbdd7e

Đã dựng 31-Plugin tại: C:\Users\nnqp2\AppData\Local\Temp\claude\d---CLAUDE-code-KTC-Quan-tri\8716a292-16a0-493e-a6ed-2b82091b40b1\scratchpad\wt\31-Plugin
````

## 1-Plugin/log-dung-lai-1.3.12-tu-commit-5d98f2b.txt (sha256 `20bb71063f1495b54ff9cb86c8c62a02308603c5b6e2e94d605d476c306b0925`)

````text
── Giai nen 8 goi .skill da xac minh vao 31-Plugin/skills/ ──
  ✓ quan-tri       <- 22-KTC-Dieu-Phoi\ktc-quan-tri.skill  (21 tep)
  ✓ bao-cao        <- 25-KTC-Bao-Cao\ktc-bao-cao-v3.20.skill  (52 tep)
  ✓ ke-hoach       <- 23-KTC-Ke-Hoach\ktc-ke-hoach-v3.12.skill  (30 tep)
  ✓ soan-thao-vb   <- 26-KTC-Soan-Thao-VB\ktc-soan-thao-vb-v1.15.skill  (95 tep)
  ✓ theo-doi-cv    <- 24-KTC-Theo-doi-CV\ktc-theo-doi-cv-v1.10.skill  (13 tep)
  ✓ the-thuc       <- 27-KTC-The-Thuc\ktc-the-thuc-v1.3.skill  (5 tep)
  ✓ kpi-lap-ke-hoach <- 28-KTC-KPI\ktc-kpi-lap-ke-hoach-v1.4.skill  (19 tep)
  ✓ kpi-tu-danh-gia <- 28-KTC-KPI\Tu-Danh-Gia\ktc-kpi-tu-danh-gia-v1.3.skill  (16 tep)
── Giải nén gói .skill lồng trong kỹ năng ──
── Ghi .claude-plugin/plugin.json ──
  ✓ plugin.json
── Ghi hooks/hooks.json (doctor + nhật ký + guard chặn ghi kho chuẩn) ──
  ✓ hooks.json
── Ghi scripts/ktc_quan_tri_doctor.py ──
  ✓ ktc_quan_tri_doctor.py
── Chép script/agent viết tay từ 29-Cong-Cu/plugin_src/ ──
  - scripts/ktc_backup_github.py (chỉ dùng nội bộ, không đóng vào plugin)
  ✓ scripts/ktc_guard.py
  ✓ scripts/ktc_nhat_ky.py
  ✓ scripts/ktc_the_thuc_hook.py
  ✓ scripts/ktc_thu_muc.py
  ✓ agents/ktc-hieu-luc-vien-dan.md
  ✓ agents/ktc-kiem-ho-so-don-vi.md
  ✓ agents/ktc-kiem-san-pham.md
  ✓ agents/ktc-tra-cuu-can-cu.md
  ✓ agents/ktc-tu-cai-tien.md
  ✓ agents/ktc-tu-hoc.md
  ✓ agents/ktc-xac-minh-minh-chung.md
  ✓ scripts/tra_hieu_luc.py (từ 29-Cong-Cu)
  ✓ scripts/kiem_vien_dan.py (từ 29-Cong-Cu)
  ✓ scripts/duong_dan.py (từ 29-Cong-Cu)
  ✓ scripts/doi_soat_so_lieu.py (từ 29-Cong-Cu)
  ✓ scripts/kiem_minh_chung.py (từ 29-Cong-Cu)
  ✓ scripts/kiem_the_thuc.py (từ 29-Cong-Cu)
  ✓ scripts/kpi_calc.py (từ 29-Cong-Cu)
  ✓ scripts/kpi_mau.py (từ 29-Cong-Cu)
  ✓ scripts/validate_plan.py (từ 29-Cong-Cu)
  ✓ scripts/kpi_danh_gia.py (từ 29-Cong-Cu)
  ✓ scripts/bc_thang.py (từ 29-Cong-Cu)
  ✓ scripts/vanphong.py (từ 29-Cong-Cu)
  ✓ scripts/trich_tuong_thuat.py (từ 29-Cong-Cu)
  ✓ scripts/ktc_trackchanges.py (từ 29-Cong-Cu)
── Lập bảng đối chiếu tên tệp (bản gốc dự án → vị trí trong plugin) ──
  ✓ skills\quan-tri\references\BAN-DO-TEP.md (7 dòng)
── Chèn chuẩn chung (lõi) vào mọi skill và agent; bản đầy đủ vào references/ của skill ──
  ✓ agents\ktc-hieu-luc-vien-dan.md          đã chèn
  ✓ agents\ktc-kiem-ho-so-don-vi.md          đã chèn
  ✓ agents\ktc-kiem-san-pham.md              đã chèn
  ✓ agents\ktc-tra-cuu-can-cu.md             đã chèn
  ✓ agents\ktc-tu-cai-tien.md                đã chèn
  ✓ agents\ktc-tu-hoc.md                     đã chèn
  ✓ agents\ktc-xac-minh-minh-chung.md        đã chèn
  ✓ skills\bao-cao\SKILL.md                  đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md · tách 13 mục lịch sử
  ✓ skills\ke-hoach\SKILL.md                 đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\kpi-lap-ke-hoach\SKILL.md         đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\kpi-tu-danh-gia\SKILL.md          đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\quan-tri\SKILL.md                 đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\soan-thao-vb\SKILL.md             đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\the-thuc\SKILL.md                 đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
  ✓ skills\theo-doi-cv\SKILL.md              đã chèn · 00-Quy-Tac-Bat-Bien-Day-Du.md
── Kiểm độ dài mô tả (plugin ≤ 500, skill/agent ≤ 1024 ký tự) ──
  ✓ mọi mô tả trong giới hạn
── Đóng gói .zip (lặp lại được) ──
  ✓ 30-Ket-Qua\2026-09-29\Plugin\ktc-quan-tri-1.3.12.zip  (291 tệp, 1469974 bytes)
    sha256 d5fb75fea6706dd97bad11bccb7669066b59503a626b09d2463accfab0fff4d8

Đã dựng 31-Plugin tại: C:\Users\nnqp2\AppData\Local\Temp\claude\d---CLAUDE-code-KTC-Quan-tri\8716a292-16a0-493e-a6ed-2b82091b40b1\scratchpad\wt\31-Plugin
````

## 1-Plugin/log-hoi-quy/00-TONG-HOP.txt (sha256 `830f1589fc67bc7e2781573448df50b17f16b4addc7a6feac1870f7af5e9a1fd`)

````text
# Tổng hợp bộ hồi quy — kết luận theo MÃ THOÁT (0 = đạt). Cột OK đếm dòng 'OK' in ra;
# bộ in theo định dạng khác (OK=0) xem nhật ký riêng. Dòng ✗ trong ca thử ngược là lỗi cài cố ý.
test_bc_thang ma=0 OK=6
test_c11_ban_goc_trong_zip ma=0 OK=0
test_c12_c13_kho_va_o_dia ma=0 OK=6
test_c14_cong_cu_agent ma=0 OK=5
test_c5_soi_trong_goi ma=0 OK=0
test_doi_soat_so_lieu ma=0 OK=24
test_dung_lap_lai ma=0 OK=0
test_he_ngoai ma=0 OK=6
test_kiem_minh_chung ma=0 OK=15
test_kiem_the_thuc ma=0 OK=38
test_kiem_tra_he_thong ma=0 OK=0
test_kiem_vien_dan ma=0 OK=24
test_kpi_calc ma=0 OK=51
test_kpi_danh_gia ma=0 OK=59
test_kpi_trinh_bay ma=0 OK=27
test_plugin_130 ma=0 OK=94
test_plugin_131 ma=0 OK=133
test_plugin_nhat_ky_backup ma=0 OK=34
test_task_id_bc736 ma=0 OK=7
test_thu_muc ma=0 OK=19
test_tra_hieu_luc ma=0 OK=17
test_trackchanges ma=0 OK=0
test_tu_du_plugin ma=0 OK=33
test_tu_hoc ma=0 OK=12
test_validate_plan ma=0 OK=27
````

## 1-Plugin/log-hoi-quy/test_bc_thang.txt (sha256 `f8bcae38d688814c956a0011c7f8ed398d45fe60db909e7fababdb583d6869e6`)

````text
== A. Bản sao trong gói kỹ năng báo cáo trùng nguồn ==
  OK 25-KTC-Bao-Cao/references/Skill-Library/bc_thang.py trùng byte 29-Cong-Cu/bc_thang.py
  OK 25-KTC-Bao-Cao/references/Skill-Library/vanphong.py trùng byte 29-Cong-Cu/vanphong.py
  OK 25-KTC-Bao-Cao/references/Skill-Library/trich_tuong_thuat.py trùng byte 29-Cong-Cu/trich_tuong_thuat.py
  OK 25-KTC-Bao-Cao/references/Skill-Library/duong_dan.py trùng byte 29-Cong-Cu/duong_dan.py
== B. Mẫu trắng đã sửa lỗi (dự phòng) ==
  OK mẫu trắng không còn 'nhiệm kỳ 2021-2026'
  OK mẫu trắng không còn 'Báo cáo báo cáo'
== C. Tìm nguồn, trích dữ liệu (kho + 10-Dau-Vao tháng 9) ==
  ⚠ BỎ QUA: 10-Dau-Vao/01-Dau-Moi-Nop/2026-09 chỉ còn 4 tệp (cần hồ sơ ≥ 10 đơn vị)

KET LUAN: SACH (có mục bỏ qua)
````

## 1-Plugin/log-hoi-quy/test_c11_ban_goc_trong_zip.txt (sha256 `80ea850f7c56757784a77e12f5db707f0c10a98994f2dd281aed7f9c43781a61`)

````text
==========================================================================
THỬ NGƯỢC C11 — có phát hiện tệp chỉ tồn tại trong zip không?
==========================================================================

Ca 1 — gói mang 3 tệp, nguồn rời không có tệp nào (đúng lỗi đã mắc):

────────────────────────────────────────────────────────────────────────────
C11. Không tệp nào chỉ tồn tại bên trong gói .skill
────────────────────────────────────────────────────────────────────────────
  ⚠ he-thu             3 tệp không có bản nguồn ngoài zip
      references/a.md
      references/b.md
      references/c.md
  ✓ phải cảnh báo đủ 3 tệp                                     → 3 cảnh báo

Ca 2 — mọi tệp trong gói đều có bản nguồn ngoài zip:

────────────────────────────────────────────────────────────────────────────
C11. Không tệp nào chỉ tồn tại bên trong gói .skill
────────────────────────────────────────────────────────────────────────────
  ✓ he-thu             mọi tệp đều có bản nguồn ngoài zip
  ✓ phải sạch                                                  → 0 cảnh báo

Ca 3 — thiếu đúng 1 tệp trong ba:

────────────────────────────────────────────────────────────────────────────
C11. Không tệp nào chỉ tồn tại bên trong gói .skill
────────────────────────────────────────────────────────────────────────────
  ⚠ he-thu             1 tệp không có bản nguồn ngoài zip
      references/b.md
  ✓ phải cảnh báo đúng 1 tệp                                   → 1 cảnh báo

Ca 4 — tệp nằm sâu nhiều cấp thư mục:

────────────────────────────────────────────────────────────────────────────
C11. Không tệp nào chỉ tồn tại bên trong gói .skill
────────────────────────────────────────────────────────────────────────────
  ⚠ he-thu             1 tệp không có bản nguồn ngoài zip
      references/Memory/01-Nhat-Ky.md
  ✓ vẫn phải bắt được                                          → 1 cảnh báo

Ca 5 — nguồn rời THỪA tệp mà gói không có (hợp lệ, không được báo):

────────────────────────────────────────────────────────────────────────────
C11. Không tệp nào chỉ tồn tại bên trong gói .skill
────────────────────────────────────────────────────────────────────────────
  ✓ he-thu             mọi tệp đều có bản nguồn ngoài zip
  ✓ không được cảnh báo                                        → 0 cảnh báo

==========================================================================
ĐẠT — C11 bắt đúng tệp mồ côi trong zip, không báo nhầm
==========================================================================
````

## 1-Plugin/log-hoi-quy/test_c12_c13_kho_va_o_dia.txt (sha256 `4aced7b1a8e0f1c092660df2c2cb236cb760683779aaa1a46466e72dc653367c`)

````text
== C12 ==

────────────────────────────────────────────────────────────────────────────
C12. Đầu vào trùng KTC-Database (Nguyên tắc 4.4 — trỏ thay vì chép)
────────────────────────────────────────────────────────────────────────────
  ✓ 1 tệp đầu vào · 0 trùng thuộc ngoại lệ đã duyệt
  OK tệp không trùng kho -> sạch

────────────────────────────────────────────────────────────────────────────
C12. Đầu vào trùng KTC-Database (Nguyên tắc 4.4 — trỏ thay vì chép)
────────────────────────────────────────────────────────────────────────────
  ✗ 2 tệp đầu vào · 0 trùng thuộc ngoại lệ đã duyệt
  OK ca ngược: tệp trùng kho, không có trong ngoại lệ -> LỖI

────────────────────────────────────────────────────────────────────────────
C12. Đầu vào trùng KTC-Database (Nguyên tắc 4.4 — trỏ thay vì chép)
────────────────────────────────────────────────────────────────────────────
  ✗ 3 tệp đầu vào · 1 trùng thuộc ngoại lệ đã duyệt
  OK tệp trong ngoại lệ đã duyệt -> bỏ qua; tệp ngoài ngoại lệ vẫn LỖI

────────────────────────────────────────────────────────────────────────────
C12. Đầu vào trùng KTC-Database (Nguyên tắc 4.4 — trỏ thay vì chép)
────────────────────────────────────────────────────────────────────────────
  ⚠ không tìm thấy KTC-Database — bỏ qua
  OK không tìm thấy kho -> cảnh báo, không báo sạch giả
== C13 ==

────────────────────────────────────────────────────────────────────────────
C13. Không ghi cứng đường dẫn ổ đĩa (Nguyên tắc 4.2)
────────────────────────────────────────────────────────────────────────────
  ✓ 0 chỗ ghi cứng ổ đĩa
  OK đường dẫn tương đối -> sạch

────────────────────────────────────────────────────────────────────────────
C13. Không ghi cứng đường dẫn ổ đĩa (Nguyên tắc 4.2)
────────────────────────────────────────────────────────────────────────────
  ✗ 2 chỗ ghi cứng ổ đĩa
  OK ca ngược: ổ D: trong .py và ổ G: trong SKILL.md -> 2 LỖI (thực tế 2)
KET LUAN: SACH
````

## 1-Plugin/log-hoi-quy/test_c14_cong_cu_agent.txt (sha256 `962d91a4e680f993ef1ac566f04b13c165536bd1f14a86a500b394822fc6ee4a`)

````text

────────────────────────────────────────────────────────────────────────────
C14. Script agent viện dẫn đều được đóng vào plugin
────────────────────────────────────────────────────────────────────────────
  ✗ 1 script agent viện dẫn nhưng chưa đóng gói (2 agent nội bộ được miễn)
  OK  bat_thieu_script                                     agent gọi kiem_the_thuc.py chưa đóng gói -> phải báo 1 lỗi

────────────────────────────────────────────────────────────────────────────
C14. Script agent viện dẫn đều được đóng vào plugin
────────────────────────────────────────────────────────────────────────────
  ✓ 0 script agent viện dẫn nhưng chưa đóng gói (2 agent nội bộ được miễn)
  OK  khong_bao_nham                                       script đã trong CONG_CU_CHO_AGENT -> không báo lỗi

────────────────────────────────────────────────────────────────────────────
C14. Script agent viện dẫn đều được đóng vào plugin
────────────────────────────────────────────────────────────────────────────
  ✓ 0 script agent viện dẫn nhưng chưa đóng gói (2 agent nội bộ được miễn)
  OK  chap_nhan_trong_31_plugin                            script nằm sẵn trong 31-Plugin/ -> tính là đã đóng gói

────────────────────────────────────────────────────────────────────────────
C14. Script agent viện dẫn đều được đóng vào plugin
────────────────────────────────────────────────────────────────────────────
  ✓ 0 script agent viện dẫn nhưng chưa đóng gói (2 agent nội bộ được miễn)
  OK  mien_agent_noi_bo                                    ktc-tu-cai-tien chỉ chạy trong dự án -> được miễn

────────────────────────────────────────────────────────────────────────────
C14. Script agent viện dẫn đều được đóng vào plugin
────────────────────────────────────────────────────────────────────────────
  ✓ 0 script agent viện dẫn nhưng chưa đóng gói (2 agent nội bộ được miễn)
  OK  du_an_that_sach                                      dự án thật: 0 script agent thiếu

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_c5_soi_trong_goi.txt (sha256 `6c4819edc8f89cedb59313d698a1fd972bd33af6008e02c201960a0614dfaa78`)

````text
==========================================================================
THỬ NGƯỢC C5 — có soi vào bên trong gói .skill không?
==========================================================================

Ca 1 — BẢN RỜI KHỚP nhưng TRONG GÓI là bản cũ (đúng điểm mù đã mắc):

────────────────────────────────────────────────────────────────────────────
C5. 5 tệp dùng chung — khớp bản gốc 20-Chuan-Chung (soi cả bản rời lẫn bản TRONG GÓI)
────────────────────────────────────────────────────────────────────────────
  ✗ 30-Skill-Phan-Loai-6-Truc.md                   he-thu: TRONG GÓI lệch (58b ≠ gốc 463b)
  ✓ phải báo LỖI, không được báo sạch                          → 1 lỗi · 0 cảnh báo

Ca 2 — trong gói khớp, bản rời lệch (còn kịp sửa trước khi đóng gói):

────────────────────────────────────────────────────────────────────────────
C5. 5 tệp dùng chung — khớp bản gốc 20-Chuan-Chung (soi cả bản rời lẫn bản TRONG GÓI)
────────────────────────────────────────────────────────────────────────────
  ⚠ 30-Skill-Phan-Loai-6-Truc.md                   he-thu: rời LỆCH
  ✓ cảnh báo chứ KHÔNG phải lỗi                                → 0 lỗi · 1 cảnh báo

Ca 3 — cả hai đều khớp bản gốc:

────────────────────────────────────────────────────────────────────────────
C5. 5 tệp dùng chung — khớp bản gốc 20-Chuan-Chung (soi cả bản rời lẫn bản TRONG GÓI)
────────────────────────────────────────────────────────────────────────────
  ✓ 30-Skill-Phan-Loai-6-Truc.md                   khớp ở mọi bản rời và 1 gói
  ✓ phải sạch hoàn toàn                                        → 0 lỗi · 0 cảnh báo

Ca 4 — gói không mang tệp dùng chung này (hợp lệ, không được bịa lỗi):

────────────────────────────────────────────────────────────────────────────
C5. 5 tệp dùng chung — khớp bản gốc 20-Chuan-Chung (soi cả bản rời lẫn bản TRONG GÓI)
────────────────────────────────────────────────────────────────────────────
  ✓ 30-Skill-Phan-Loai-6-Truc.md                   khớp ở mọi bản rời (không gói nào mang tệp này)
  ✓ không lỗi, không cảnh báo                                  → 0 lỗi · 0 cảnh báo

Ca 5 — bản rời không tồn tại VÀ trong gói là bản cũ:

────────────────────────────────────────────────────────────────────────────
C5. 5 tệp dùng chung — khớp bản gốc 20-Chuan-Chung (soi cả bản rời lẫn bản TRONG GÓI)
────────────────────────────────────────────────────────────────────────────
  ✗ 30-Skill-Phan-Loai-6-Truc.md                   he-thu: TRONG GÓI lệch (58b ≠ gốc 463b)
  ⚠ 30-Skill-Phan-Loai-6-Truc.md                   he-thu: rời không có
  ✓ vẫn phải báo LỖI ở bản trong gói                           → 1 lỗi · 1 cảnh báo

==========================================================================
ĐẠT — C5 soi đúng cả bản rời lẫn bản nằm trong gói
==========================================================================
````

## 1-Plugin/log-hoi-quy/test_doi_soat_so_lieu.txt (sha256 `a9b53e71fd30a95e3d908a37f1ee1121f273dd2225f6a2dc82b373a4e8c41ca1`)

````text
  OK nhận kỳ từ tên tệp (tháng/quý, có dấu)
  OK DS03: nhiệm vụ KH tháng 8 chưa có kết quả tháng 8 bị bắt
  OK DS03: kết quả không có trong KH bị bắt
  OK DS03: KH tháng 9 KHÔNG bị so với KQ tháng 8 (khác kỳ)
  OK DS02: dòng tổng hợp khớp nguồn không bị báo
  OK DS02: một nguồn, lệch số liệu → báo lệch
  OK DS02: dòng “…” → không truy vết được
  OK DS02: dòng không có nguồn → Nguyên tắc bất biến 3
  OK DS02: nội dung chung ở nhiều đơn vị — có nguồn cùng số thì khớp; không có thì đòi Task_ID, không kết luận lệch
  OK DS04: Task_ID trùng giữa K-KTCN và K-SUPH bị bắt
  OK DS05: KPI 120 / SL 1,2 → đánh dấu lệch thang, không in %
  OK DS05: Trục đúng thang tính % bình thường
  OK DS06: mã đoàn thể DT-CDCS chưa có trong bảng mã bị báo
  OK DS06: đơn vị chỉ nộp .docx bị báo thiếu Excel
  OK DS06: .docx thuyết minh nộp kèm .xlsx KHÔNG bị báo
  OK Bố cục mới: đơn vị lấy từ phần đầu tệp, không lấy tên thư mục (K-KHCB)
  OK Bố cục mới: 'KHCB.xlsx' là báo cáo, KHÔNG xếp là kế hoạch (KQ)
  OK Bố cục mới: kỳ lấy từ tiêu đề trong tệp (('thang', 9, 2026))
  OK Bố cục mới: 'ĐƠN VỊ: PHÒNG TCCB&CTHSSV' + tiêu đề dính chữ -> P-TCCB, KH tháng 10
  OK Bố cục mới: đơn vị chưa có mã tách riêng, không gộp theo thư mục (?TỔ HỌC LIỆU)
  OK Gần giống 'Phòng Tổ chức' KHÔNG được ghép (chỉ khớp chính xác) (?PHÒNG TỔ CHỨC CÁN BỘ)
  OK Kỳ quý số La Mã (('quy', 4, 2026))
  OK Ánh xạ bổ sung: 'BAN TRUYỀN THÔNG' → P-THHC (chốt 14/9/2026) (P-THHC)
  OK NGƯỢC: 'BAN TRUYỀN HÌNH' gần giống KHÔNG được ghép (?BAN TRUYỀN HÌNH)

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_dung_lap_lai.txt (sha256 `6b459ab64c7622297e777a25d7d5bf373789c720f91a700a5895afcfb1a52e3c`)

````text
── Chuẩn hóa xuống dòng ──
── Chuẩn hóa xuống dòng (dựng lặp lại được từ mọi bản checkout) ──
  ✓ 3 tệp đổi xuống dòng
  ✓ .md CRLF → LF                                              
  ✓ .json CRLF → LF                                            
  ✓ .py LF giữ nguyên                                          
  ✓ .cmd → CRLF (Windows cần)                                  
  ✓ tệp nhị phân không đụng tới                                
  ✓ so băm bảng đối chiếu bỏ qua CR                            
── Gói phát hành hiện hành ──
  ✓ không tệp văn bản nào mang CRLF                            []
  ✓ BAN-DO-TEP đủ dòng 20-Chuan-Chung (≥ 14)                   15 dòng
── Guard chịu tải nội dung Markdown lớn (Gemini L5 1.2) ──
  ✓ Write bảng 3000×30 (~2,7 MB)                               mã 0, 0.15 giây (giới hạn hook 30 giây)
  ✓ Write nội dung dị dạng                                     mã 0, 0.07 giây (giới hạn hook 30 giây)
  ✓ Edit bảng lớn                                              mã 0, 0.08 giây (giới hạn hook 30 giây)
  ✓ Bash heredoc bảng lớn                                      mã 0, 0.26 giây (giới hạn hook 30 giây)
  ✓ PowerShell here-string bảng lớn                            mã 0, 1.99 giây (giới hạn hook 30 giây)
  ✓ Write bảng lớn vào kho → vẫn CHẶN                          mã 2, 0.06 giây (giới hạn hook 30 giây)

ĐẠT
````

## 1-Plugin/log-hoi-quy/test_he_ngoai.txt (sha256 `bb6286e934f7e26abda8afe65347cd2f8f1895c40d5c364b29b061e8917c1bc3`)

````text
  OK  ten_bia_tra_None                       tên hệ không có thật -> None, không đoán bừa
  OK  uu_tien_bien_moi_truong                biến môi trường KTC_<TEN> được ưu tiên trước
  OK  khong_phai_he_ngoai                    đường dẫn trong chính dự án -> không xử như hệ ngoài
  OK  mot_doan_khong_tinh                    chỉ mỗi tên hệ, không có tệp -> False
  OK  he_ngoai_khong_co_tep                  ca ngược: hệ có thật nhưng tệp KHÔNG có -> vẫn phải báo thiếu
  OK  he_ngoai_co_tep                        hệ ngoài có thật + tệp có thật -> nhận

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_kiem_minh_chung.txt (sha256 `c1da57b5eda09d4b4bb044dd8725693013e32b6defc5fdd135019ad2627ef2d3`)

````text
  OK đọc cột theo tên tiêu đề: 4 nhiệm vụ, 5 minh chứng + 1 dòng cập nhật (được 4, 6)
  OK sheet “Cập nhật tiến độ” KHÔNG bị đọc nhầm thành sheet nhiệm vụ (không ghi đè trạng thái)
  OK MC01: NV4 hoàn thành không có minh chứng → Mức 1
  OK MC01: NV1 có minh chứng thật → không báo (thử ngược)
  OK MC01: NV3 đang thực hiện → không đòi minh chứng
  OK MC03: đường dẫn không tồn tại → Mức 2
  OK MC03: URL Drive → chuyển mở qua Google Drive, không tự kết luận
  OK MC04: minh chứng phát sinh sau hạn
  OK MC04: thiếu ngày phát sinh
  OK MC05: “Đã xác minh” thiếu người/ngày → xác minh hình thức
  OK MC06: minh chứng trỏ tới nhiệm vụ không tồn tại
  OK MC07: một liên kết dùng cho nhiều nhiệm vụ
  OK MC02: minh chứng không có liên kết
  OK Master Task Register: bỏ dòng mô tả “(bắt buộc)”
  OK Master Task Register: MC01 đúng nhiệm vụ thiếu Minh_Chung

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_kiem_the_thuc.txt (sha256 `cfc3c1fbe7788a4b020d0858aebcc3c4562f1774db94cf959a29189ad470317a`)

````text
  OK TT01 Document() rỗng bị bắt khổ Letter
  OK TT02 lề mặc định (trái 3,18 / 2,54 cm) bị bắt
  OK TT03 phông Calibri mặc định bị bắt
  OK văn bản dựng từ khung: 0 gợi ý (được: [])
  OK --khung BC: đổi tên loại và ký hiệu
  OK TT08 cơ quan chủ quản “UBND TỈNH KON TUM” bị bắt
  OK TT09 Quốc hiệu cỡ 12 bị bắt
  OK TT03 .VnTime bị bắt
  OK TT04 nội dung cỡ 13 bị bắt
  OK TT12 bảng tiêu đề chia đôi 8 + 8 cm bị bắt
  OK TT14 thiếu đường kẻ dưới tên Trường, tiêu ngữ bị bắt
  OK TT13 “UBND TỈNH QUẢNG NGÃI” in đậm bị bắt
  OK TT15 dòng địa danh in đậm bị bắt
  OK TT16 đoạn căn cứ không thụt đầu dòng bị bắt
  OK mẫu 2.2: tên Trường là chủ quản (không đậm) + Phòng đậm → không báo (lỗi báo nhầm BC quá trình 29/9)
  OK mẫu 2.2: tên Phòng (đơn vị ban hành) không đậm → TT17
  OK TT11b chữ số “1” ở đầu trang thứ nhất bị bắt (lỗi bản v2 ngày 28/9)
  OK TT11b không báo nhầm văn bản dựng từ khung (ẩn số trang 1)
  OK TT18 thiếu đường kẻ dưới trích yếu bị bắt
  OK TT17 tên cơ quan chủ quản cỡ 14 (TB 597: 13) bị bắt
  OK TT19 học hàm, học vị trước họ tên người ký bị bắt
  OK TT19 ký thay “K/T” (hệ Đảng) bị bắt
  OK “KT. HIỆU TRƯỞNG” không bị bắt nhầm
  OK tệp thật Cowork 28/9 (bảng tiêu đề dựng tay): bắt đủ 7 loại lỗi (được ['TT12', 'TT13', 'TT14', 'TT15', 'TT16', 'TT17', 'TT18'])
  OK TT03b biến thể TimesNewRomanPSMT chỉ Mức 3
  OK TX02 xlsx phông Arial bị bắt (skill xlsx cho phép, KTC thì không)
  OK xlsx TNR, A4 ngang đạt
  OK tao_tu_mau giữ lề trái 3 cm của mẫu
  OK hook: tệp sai trong dự án KTC → mã 2, báo TT08
  OK hook: tệp đúng → mã 0
  OK hook: ngoài dự án KTC → không can thiệp
  OK 11 mẫu 03-Templates(1) (trừ 5 mẫu có lỗi đã biết) không bị báo Mức 1–2: {}
  OK lỗi đã biết của 06D (số trang ở trang 1) vẫn bị bắt
  OK 06A (mẫu 2.2: tên Trường là chủ quản, không đậm) không bị báo nhầm
  OK lỗi đã biết của 01-Quyet-dinh-ban-hanh-Quy-che.dotx (tên Trường sai cỡ/kiểu) vẫn bị bắt
  OK lỗi đã biết của 07-To-trinh.dotx (tên Trường sai cỡ/kiểu) vẫn bị bắt
  OK lỗi đã biết của 10-Giay-moi vẫn bị bắt
  OK lỗi đã biết của 02A (thiếu đường kẻ dưới tên Trường) vẫn bị bắt

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_kiem_tra_he_thong.txt (sha256 `05c526d61deb9e82e664c545874038c9efbd3dc908cb0eb735c400c75930c5a6`)

````text
==========================================================================
THỬ NGƯỢC — bộ kiểm có bắt được lỗi thật không?
==========================================================================

C7 — cụm hạ cấp chốt chặn 897 (PHẢI bắt):
  ✓ bắt: | 5 | Rà soát chính thức trước khi trình ký (n      
  ✓ bắt: Rà soát trước khi trình ký (dùng `ktc-ra-soat-      
  ✓ bắt: ### Bước 5 — Rà soát chính thức *(tùy chọn)* D      
  ✓ bắt: Có thể dùng 897 nếu cần thiết.                      

C7 — câu ĐÚNG, không được báo nhầm (PHẢI bỏ qua):
  ✓ bỏ qua: **897 là chốt chặn bắt buộc, không phải bước t   
  ✓ bỏ qua: Rà soát bắt buộc bằng ktc-ra-soat-897 — không    
  ✓ bỏ qua: Dùng hệ `ktc-ra-soat-897`. Đây là chốt chặn, k   

C6 — tên hệ đã bỏ dùng làm đích định tuyến (PHẢI bắt):
  ✓ bắt: dùng `ktc-van-ban` / `ktc-ra-soat-897`              
  ✓ bắt: KHONG dung de soan van ban - dung ktc-van-ban       
  ✓ bắt: chuyển sang ktc-dis-tong-hop-vb                     

C6 — nhắc lại lịch sử, KHÔNG phải định tuyến (PHẢI bỏ qua):
  ✓ bỏ qua: Kế thừa từ `KTC-DIS-Tong-Hop-VB`, thu hẹp có c   
  ✓ bỏ qua: *Tiền lệ:* hệ `KTC-DIS-Tong-Hop-VB` từng chép    

C1 — frontmatter hỏng (PHẢI bắt):
  ✓ bắt: thiếu frontmatter                                   → ['Thiếu YAML frontmatter']
  ✓ bắt: name viết hoa                                       → ["name không hợp lệ: '25-KTC-Bao-Cao'"]
  ✓ bắt: thừa khóa version                                   → ["Khóa frontmatter phải đúng name+description, đang có ['name', 'description', 'version']"]
  ✓ bắt: description quá 1024                                → ['description dài 1100 > 1024']
  ✓ bỏ qua: hợp lệ                                           → hợp lệ

C8 — bản sao lệch 1 dòng (PHẢI bắt, giống >= 50%):
  ✓ bắt: bản sao lệch 1/12 dòng                              → giống 0.92
  ✓ bắt: chỉ khác CRLF/LF vẫn là cùng tệp                    → giống 1.00

C8 — chỉ trùng tên, nội dung khác (PHẢI bỏ qua):
  ✓ bỏ qua: tệp trùng tên khác chủ đề                        → giống 0.00

==========================================================================
ĐẠT — mọi phép kiểm đều bắt đúng ca sai và bỏ qua đúng ca đúng
==========================================================================
````

## 1-Plugin/log-hoi-quy/test_kiem_vien_dan.txt (sha256 `9c06c0e1e02cf49afa0bf8b87e1200987b5bc74dbbcc6c182a30d8258b6f3430`)

````text
  OK dự thảo chuẩn không bị bắt lỗi (được: [])
  OK VD01 căn cứ Luật có số hiệu
  OK VD01 Luật có số hiệu kể cả khi kèm VBHN
  OK VD01 viện dẫn trong nội dung cũng không ghi số hiệu luật
  OK VD01 Pháp lệnh có số hiệu
  OK VD01 không bắt nghị định có số hiệu
  OK VD02 căn cứ luật thiếu ngày
  OK VD02 ngày dạng dd/mm/yyyy được chấp nhận
  OK VD03 VBHN làm căn cứ chính
  OK VD04 Pháp lệnh 'của Quốc hội'
  OK VD04 không bắt UBTVQH
  OK VD05 chỉ dẫn luật sửa đổi
  OK VD06 dấu cuối dòng giữa sai
  OK VD06 dòng cuối thiếu dấu chấm
  OK VD07 gạch đầu dòng
  OK VD08 QĐ Hiệu trưởng thiếu QĐ 1976 đầu tiên
  OK VD08 không áp cho kế hoạch
  OK VD09 văn bản Trường đã bị thay thế
  OK VD09 không nhầm QĐ 1229 (quy chế đào tạo) với QĐ 1299
  OK VD09 không bắt điều khoản thay thế/bãi bỏ (thử thật trên kho 02, 19/9/2026)
  OK VD06 không áp cho câu 'Căn cứ…' trong phần nội dung (ngoài khối căn cứ đầu văn bản)
  OK VD10 dẫn checklist làm căn cứ
  OK VD11 'điều' viết thường
  OK VD12 viện dẫn lần sau vẫn ghi đầy đủ

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_kpi_calc.txt (sha256 `0bf7863ce46b6c284c4050fd3d79db2cfd2867eb66f9b70e98b2af3bff19b162`)

````text
  OK Đ19.1: 100 điểm → Hoàn thành xuất sắc
  OK Đ19.1: 90 điểm → Hoàn thành xuất sắc
  OK Đ19.1: 89.99 điểm → Hoàn thành tốt
  OK Đ19.1: 70 điểm → Hoàn thành tốt
  OK Đ19.1: 69.99 điểm → Hoàn thành nhiệm vụ
  OK Đ19.1: 50 điểm → Hoàn thành nhiệm vụ
  OK Đ19.1: 49.99 điểm → Không hoàn thành
  OK Đ19.1: 0 điểm → Không hoàn thành
  OK Đ19.1: tổng > 100 bị chặn (ngoài thang)
  OK Xếp loại theo điểm luôn kèm lưu ý điều kiện chưa kiểm
  OK Đ11.6: 130% × 45 điểm → 45 (trần), ghi nhận vượt 30%
  OK Đ11.6: 100% → đủ điểm tối đa
  OK Đ11.6: 80% × 45 = 36
  OK Đ12.3: Trục chính 28/70 = 40,00% → đạt
  OK Đ12.3: Trục chính 39,99% → báo KP02
  OK Đ11.3: tổng 60 ≠ 70 → báo KP01
  OK Đ10.4: 13/12/5 (mẫu Quý III) → đạt
  OK Đ10.4: nhóm 4,99 điểm → báo KP04
  OK Đ10.4: tổng 32 > 30 → báo KP05
  OK Đ10.5: 4 mức, biên
  OK Đ18: 3 mức, biên 90/60
  OK NGƯỢC: gọi hệ số thiếu phương án → báo lỗi, không tự chọn
  OK NGƯỢC: phương án lạ → báo lỗi
  OK PL II QĐ 1923: 'Thấp' → 1.0
  OK PL II QĐ 1923: 'Trung bình' → 1.2
  OK PL II QĐ 1923: 'Cao' → 1.5
  OK PL II QĐ 1923: 'Khó và phức tạp' → 2.0
  OK PL II QĐ 1923: 'Thường xuyên, nhiệm vụ chủ yếu là thống ' → 1.0
  OK PL II QĐ 1923: 'Phân tích, đánh giá số liệu, không quá k' → 1.5
  OK NGƯỢC: mức độ ngoài 4 mức → báo lỗi, không đoán
  OK Phương án mức độ ghi trạng thái 'Có văn bản'
  OK QĐ 2119 mã 1.1.DA01.01 (Đề án phát triển Trường) → A = 4,5, ghi 'Có văn bản: … QĐ 2119'
  OK tra theo STT phụ lục '1.1' → cùng sản phẩm, A = 4,5
  OK tra theo tên chính xác → A = 4,5
  OK Phương án A (QĐ 2119 chính thức) → KHÔNG còn mã THANG_DIEM_CHUA_PHAN_DINH
  OK Quy chế tuyển sinh: QĐ 2119 = 2,0 (dự thảo cũ 2,5) → lấy 2,0
  OK Bản ghi nhớ hợp tác quốc tế: QĐ 2119 = 2,0 (dự thảo cũ 1,0) → lấy 2,0
  OK A×B: 4,5 × 2,0 = 9,0, ghi CHƯA CÓ VĂN BẢN (phép nhân)
  OK Phương án A×B → vẫn mã THANG_DIEM_CHUA_PHAN_DINH (phép nhân chưa có văn bản)
  OK ca ngược: phương án mức độ (QĐ 1923 có văn bản) → không cảnh báo thang điểm
  OK Danh mục nạp đủ 416 sản phẩm QĐ 2119
  OK NGƯỢC: sản phẩm không có trong Danh mục QĐ 2119 → báo lỗi, không tự gán A
  OK ca ngược: dòng hệ số ngoài tập Nhóm, > 10 → cảnh báo lệch và bất thường
  OK NGƯỢC: nhập tay thiếu hệ số → báo lỗi
  OK Gợi ý Danh mục: mọi dòng trả về chứa đủ từ khóa (['3.29', '3.46'])
  OK NGƯỢC: từ 'thi' không khớp nhầm vào 'cải thiện' (so từ nguyên vẹn)
  OK NGƯỢC: từ khóa không có → danh sách rỗng, không đoán gần đúng
  OK SL quy đổi = 3 × 1,2 = 3,6 (mẫu: J = G × I)
  OK NGƯỢC: số lượng trống → báo lỗi (Đ12.4 đo lường được)
  OK Bảo mật: 30-Ket-Qua/<ngày>/KPI-ca-nhan/ bị git bỏ qua (không sao lưu GitHub)
  OK NGƯỢC: thư mục kết quả khác vẫn được git theo dõi

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_kpi_danh_gia.txt (sha256 `80d525fce6f7a547d3b57fb01e722980dcd4bea6003848890f4eed043346b11a`)

````text
== 1. cau_truc_danh_gia — ca 6 mau ==
  OK truong-pho-don-vi: 3 nhóm A = 30 (≥5/nhóm), 6 Trục = 70, khối II (4 điều kiện), III
  OK truong-pho-don-vi: nhận đúng nhóm từ tiêu đề mẫu (không cần --nhom)
  OK bo-mon: 3 nhóm A = 30 (≥5/nhóm), 6 Trục = 70, khối II (4 điều kiện), III
  OK bo-mon: nhận đúng nhóm từ tiêu đề mẫu (không cần --nhom)
  OK nha-giao: 3 nhóm A = 30 (≥5/nhóm), 6 Trục = 70, khối II (4 điều kiện), III
  OK nha-giao: nhận đúng nhóm từ tiêu đề mẫu (không cần --nhom)
  OK giao-vu: 3 nhóm A = 30 (≥5/nhóm), 6 Trục = 70, khối II (1 điều kiện), III
  OK giao-vu: nhận đúng nhóm từ tiêu đề mẫu (không cần --nhom)
  OK hanh-chinh: 3 nhóm A = 30 (≥5/nhóm), 6 Trục = 70, khối II (1 điều kiện), III
  OK hanh-chinh: nhận đúng nhóm từ tiêu đề mẫu (không cần --nhom)
  OK ho-tro: 3 nhóm A = 30 (≥5/nhóm), 6 Trục = 70, khối II (1 điều kiện), III
  OK ho-tro: nhận đúng nhóm từ tiêu đề mẫu (không cần --nhom)
  OK hai mẫu lệch dòng và lệch cột kết quả điều kiện — dò động, không ghi cứng
== 2. Ca ngược cấu trúc: thiếu khối -> dừng, không đoán ==
  OK xóa Trục (3) -> LoiCauTruc: Sheet 'Danh Gia': không dò được mục B (6 Trục có điểm tối đa) — dừng, báo người 
  OK xóa III -> LoiCauTruc: Sheet 'Danh Gia': không dò được dòng III. Tự đề xuất mức xếp loại — dừng, báo ng
== 3. Giai đoạn 1: xóa số thực tế ví dụ của mẫu (Known-Issues #12), ẩn dòng trống, KH16 ==
  OK kế hoạch xuất ra không còn L9=4/N9=100 của mẫu
  OK ca ngược: mẫu gốc vẫn có L9=4 (không sửa assets)
  OK dòng trống trong khối Trục bị ẩn, dòng có việc không ẩn
  OK ô nội dung đầu việc bật xuống dòng
  OK KH16 không báo kế hoạch sạch
  OK ca ngược: KH16 bắt số ví dụ trong mẫu gốc
== 4. Trọn quy trình trên cả 6 nhóm (sinh bảng hỏi -> dừng khi trống -> điền -> đánh giá -> xuất) ==
  OK truong-pho-don-vi: đủ điểm = 100,00, mức theo điểm HTXS, ghi mục A/III, KPI R chặn trần
  OK truong-pho-don-vi: Excel tính lại tổng = 100, khớp Python 100
  OK bo-mon: đủ điểm = 100,00, mức theo điểm HTXS, ghi mục A/III, KPI R chặn trần
  OK nha-giao: đủ điểm = 100,00, mức theo điểm HTXS, ghi mục A/III, KPI R chặn trần
  OK giao-vu: đủ điểm = 100,00, mức theo điểm HTXS, ghi mục A/III, KPI R chặn trần
  OK hanh-chinh: đủ điểm = 100,00, mức theo điểm HTXS, ghi mục A/III, KPI R chặn trần
  OK hanh-chinh: Excel tính lại tổng = 100, khớp Python 100
  OK ho-tro: đủ điểm = 100,00, mức theo điểm HTXS, ghi mục A/III, KPI R chặn trần
== 5. Ngưỡng điểm (không làm tròn có lợi) ==
  OK 89.99 -> Hoàn thành tốt nhiệm vụ
  OK 90 -> Hoàn thành xuất sắc nhiệm vụ
  OK 69.99 -> Hoàn thành nhiệm vụ
  OK 70 -> Hoàn thành tốt nhiệm vụ
  OK 49.99 -> Không hoàn thành nhiệm vụ
  OK 50 -> Hoàn thành nhiệm vụ
  OK hiển thị cắt 89,996 -> 89,99 (không làm tròn lên 90)
== 6. Vượt 100% bị chặn trần theo chỉ tiêu; công thức gốc của mẫu thì không ==
  OK Trục 1: công thức mẫu 169,23% -> chặn 87,17% (việc vượt không bù cho việc thiếu)
  OK cảnh báo nêu Đ11.6 và chênh lệch với mẫu
  OK Excel tính lại % Trục 1 = 87.1795 = Python 87.1795 (công thức chặn trần)
== 7. Điều kiện thiếu nguồn -> 'Thiếu dữ liệu', không tự cho Đạt ==
  OK bảng kiểm 'Chưa có kết quả' -> điều kiện HTT: Thiếu dữ liệu
  OK ca ngược: đủ dữ liệu, đều đạt -> điều kiện HTT: Đạt
  OK giờ giảng 60%: không đạt điều kiện HTXS/HTT, đạt điều kiện HT (≥50%)
  OK bảng kiểm Không đạt -> trường hợp Đ19.1d
  OK không có việc vượt mức -> điều kiện HTXS (≥30% vượt mức) Không đạt
  OK ca ngược: mọi việc vượt mức, đủ dữ liệu -> điều kiện HTXS Đạt
== 8. Dừng, không tự chấm ==
  OK đào tạo tập trung ≥ 2 tháng (Đ21.6a) -> dừng, không chấm
  OK ≥1/2 quý (Đ21.4) -> dừng, không chấm
  OK điểm tiêu chí vượt tối đa -> dừng
  OK mức nhóm chọn không khớp tổng điểm nhóm -> dừng [Đ10.5]
  OK ca ngược: mức nhóm chọn khớp -> chấm bình thường
  OK nhiệm vụ trọng tâm: % không khớp mức Đ18 -> dừng
== 9. Cảnh báo cấu trúc mẫu (nhóm A < 5 điểm) là lỗi mẫu, không phải lỗi người dùng ==
  OK nhóm 3 = 4 điểm < 5 -> cảnh báo cấu trúc mẫu
  OK ca ngược: mẫu đúng -> không cảnh báo
== 10. Người đứng đầu không cao hơn tập thể; tự đề xuất cao hơn mức theo điểm ==
  OK đứng đầu: HTXS theo điểm > tập thể HTT -> cảnh báo Đ14.4
  OK ca ngược: cấp phó -> không áp
  OK tự đề xuất HTXS khi điểm 87,00 -> cảnh báo
== 11. Bảo mật: tệp tự đánh giá không vào git (QĐ 1923 Đ23.2) ==
  OK 30-Ket-Qua/<ngày>/KPI-ca-nhan/TDG-*.xlsx nằm trong .gitignore
  OK git add -A --dry-run không đưa tệp tự đánh giá vào git
  OK ca ngược: thư mục kết quả khác vẫn được git theo dõi

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_kpi_trinh_bay.txt (sha256 `b317fe6989b876175f43aa563127b2416f888143a9e0498b8813c8bea9715d88`)

````text
== T1. Nội dung 300 ký tự (hanh-chinh): dòng KPI đủ cao cho cột B (công thức trỏ Ke Hoach) ==
  OK KPI dòng 9: cao 193.2 pt ≥ ước 187.2 pt (300 ký tự, cột B rộng 32.2852)
== T2. Độ rộng cột nằm giữa nhóm column_dimensions gộp (min–max) ==
  OK KPI cột D (giữa nhóm C–F) = 8.7109375; cột U (giữa nhóm S–Y) = 30.0
== T3. Truyền đủ người chỉ đạo, phối hợp, đơn vị tham mưu -> KPI!C–E; KPI!F là công thức ==
  OK KPI!C/D/E = 'Phó Hiệu trưởng X', 'Các phòng', 'Phòng Y'
  OK KPI!F9 = "='Ke Hoach'!E14"
  OK C–F xuống dòng, căn trên
  OK ca ngược: đủ trường -> không KH17/KH18
== T4. Không truyền người phối hợp -> để trống + KH17; mặc định C = cấp trình, E = đơn vị ==
  OK KPI!D trống, có KH17 (không tự bịa)
  OK mặc định C = cấp trình, E = đơn vị
  OK ca ngược: mẫu không có cột Người phối hợp -> không KH17
  OK KPI!F trỏ dòng trống của Ke Hoach -> KH18 (LỖI)
== T5. Nội dung quá dài (> 409 pt) -> KH19, không cắt im lặng ==
  OK cảnh báo KH19 ở cả kpi_mau và validate_plan
  OK chiều cao không vượt 409 pt
== T6. Sau danh-gia: dòng KPI đủ cao cho sản phẩm thực tế (K) và minh chứng (S) ==
  OK KPI dòng 9: cao 409 pt ≥ ước cho cột K 409 pt
== T7. Tệp ra đang bị khóa (như Excel đang mở) -> thông báo tiếng Việt, mã ≠ 0, không traceback ==
  OK kpi_mau: mã 2, thông báo: 'aect\\dang_mo.xlsx: tệp đang mở trong Excel (hoặc bị khóa) — hãy đóng tệp hoặc đặt tên mới.'
  OK kpi_danh_gia: mã 2, thông báo: 'aect\\dang_mo.xlsx: tệp đang mở trong Excel (hoặc bị khóa) — hãy đóng tệp hoặc đặt tên mới.'
== T8. Cả 6 nhóm: C–F đúng theo tiêu đề cột của mẫu ==
  OK truong-pho-don-vi: C, E, F đúng ở Trục 1 và 4; không KH18
  OK bo-mon: C, E, F đúng ở Trục 1 và 4; không KH18
  OK nha-giao: C, E, F đúng ở Trục 1 và 4; không KH18
  OK giao-vu: C, E, F đúng ở Trục 1 và 4; không KH18
  OK hanh-chinh: C, E, F đúng ở Trục 1 và 4; không KH18
  OK ho-tro: C, E, F đúng ở Trục 1 và 4; không KH18
== T9. Không số nào đổi: tổng điểm, A, B, từng Trục, mức theo điểm = trước khi sửa ==
  OK truong-pho-don-vi: tổng 74.282353 = 74.282353
  OK bo-mon: tổng 72.549020 = 72.54902
  OK nha-giao: tổng 72.549020 = 72.54902
  OK giao-vu: tổng 78.184314 = 78.184314
  OK hanh-chinh: tổng 78.184314 = 78.184314
  OK ho-tro: tổng 83.521569 = 83.521569

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_plugin_130.txt (sha256 `6282453da60f0d0f041a6896d8afa2a2b01d899bd07ae6533ecd044fbe74322f`)

````text
== A. ktc_guard.py ==
  OK chặn: Write vào KTC-Database
  OK chặn: Edit mẫu 03-Templates(1) (dấu \)
  OK chặn: MultiEdit 04-Good-Documents
  OK chặn: NotebookEdit (chữ thường)
  OK chặn: Bash rm
  OK chặn: Bash chuyển hướng >
  OK chặn: Bash chuyển hướng >>
  OK chặn: Bash cp VÀO kho
  OK chặn: Bash mv RA khỏi kho (xóa nguồn)
  OK chặn: Bash sed -i
  OK chặn: PowerShell Remove-Item
  OK chặn: PowerShell Set-Content
  OK chặn: PowerShell Copy-Item -Destination vào kho
  OK chặn: PowerShell Out-File sau ống
  OK cho qua: Write vào 30-Ket-Qua
  OK cho qua: Bash đọc kho
  OK cho qua: Bash liệt kê kho, 2>/dev/null
  OK cho qua: Bash cp TỪ kho ra ngoài
  OK cho qua: PowerShell Copy-Item từ kho ra ngoài
  OK cho qua: Bash ghi log ngoài kho
  OK cho qua: Read (không thuộc phạm vi guard)
  OK fail-closed: dữ liệu hook hỏng -> chặn
  OK fail-closed: JSON không phải đối tượng -> chặn
== B. Bản dựng 31-Plugin ==
  OK plugin.json version 1.3.x (đang 1.3.13)
  OK mô tả plugin không còn nói backup
  OK hooks.json không còn gọi backup GitHub
  OK hooks.json có PreToolUse gọi ktc_guard.py
  OK matcher guard phủ Write, Edit, MultiEdit, NotebookEdit, Bash, PowerShell
  OK script backup KHÔNG nằm trong plugin phân phối
  OK script guard có trong plugin
  OK đủ 8 skill, 7 agent (đang 8, 7)
  OK skills\bao-cao\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\bao-cao\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\bao-cao\SKILL.md: khối nằm sau frontmatter
  OK skills\ke-hoach\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\ke-hoach\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\ke-hoach\SKILL.md: khối nằm sau frontmatter
  OK skills\kpi-lap-ke-hoach\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\kpi-lap-ke-hoach\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\kpi-lap-ke-hoach\SKILL.md: khối nằm sau frontmatter
  OK skills\kpi-tu-danh-gia\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\kpi-tu-danh-gia\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\kpi-tu-danh-gia\SKILL.md: khối nằm sau frontmatter
  OK skills\quan-tri\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\quan-tri\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\quan-tri\SKILL.md: khối nằm sau frontmatter
  OK skills\soan-thao-vb\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\soan-thao-vb\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\soan-thao-vb\SKILL.md: khối nằm sau frontmatter
  OK skills\the-thuc\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\the-thuc\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\the-thuc\SKILL.md: khối nằm sau frontmatter
  OK skills\theo-doi-cv\SKILL.md: có khối chuẩn chung + 6 trạng thái
  OK skills\theo-doi-cv\SKILL.md: khối chuẩn chung không bị chèn lặp
  OK skills\theo-doi-cv\SKILL.md: khối nằm sau frontmatter
  OK agents\ktc-hieu-luc-vien-dan.md: có khối chuẩn chung + 6 trạng thái
  OK agents\ktc-hieu-luc-vien-dan.md: khối chuẩn chung không bị chèn lặp
  OK agents\ktc-hieu-luc-vien-dan.md: khối nằm sau frontmatter
  OK agents\ktc-kiem-ho-so-don-vi.md: có khối chuẩn chung + 6 trạng thái
  OK agents\ktc-kiem-ho-so-don-vi.md: khối chuẩn chung không bị chèn lặp
  OK agents\ktc-kiem-ho-so-don-vi.md: khối nằm sau frontmatter
  OK agents\ktc-kiem-san-pham.md: có khối chuẩn chung + 6 trạng thái
  OK agents\ktc-kiem-san-pham.md: khối chuẩn chung không bị chèn lặp
  OK agents\ktc-kiem-san-pham.md: khối nằm sau frontmatter
  OK agents\ktc-tra-cuu-can-cu.md: có khối chuẩn chung + 6 trạng thái
  OK agents\ktc-tra-cuu-can-cu.md: khối chuẩn chung không bị chèn lặp
  OK agents\ktc-tra-cuu-can-cu.md: khối nằm sau frontmatter
  OK agents\ktc-tu-cai-tien.md: có khối chuẩn chung + 6 trạng thái
  OK agents\ktc-tu-cai-tien.md: khối chuẩn chung không bị chèn lặp
  OK agents\ktc-tu-cai-tien.md: khối nằm sau frontmatter
  OK agents\ktc-tu-hoc.md: có khối chuẩn chung + 6 trạng thái
  OK agents\ktc-tu-hoc.md: khối chuẩn chung không bị chèn lặp
  OK agents\ktc-tu-hoc.md: khối nằm sau frontmatter
  OK agents\ktc-xac-minh-minh-chung.md: có khối chuẩn chung + 6 trạng thái
  OK agents\ktc-xac-minh-minh-chung.md: khối chuẩn chung không bị chèn lặp
  OK agents\ktc-xac-minh-minh-chung.md: khối nằm sau frontmatter
  OK skills\bao-cao\SKILL.md: frontmatter description hợp lệ YAML
  OK skills\ke-hoach\SKILL.md: frontmatter description hợp lệ YAML
  OK skills\kpi-lap-ke-hoach\SKILL.md: frontmatter description hợp lệ YAML
  OK skills\kpi-tu-danh-gia\SKILL.md: frontmatter description hợp lệ YAML
  OK skills\quan-tri\SKILL.md: frontmatter description hợp lệ YAML
  OK skills\soan-thao-vb\SKILL.md: frontmatter description hợp lệ YAML
  OK skills\the-thuc\SKILL.md: frontmatter description hợp lệ YAML
  OK skills\theo-doi-cv\SKILL.md: frontmatter description hợp lệ YAML
  OK agents\ktc-hieu-luc-vien-dan.md: frontmatter description hợp lệ YAML
  OK agents\ktc-kiem-ho-so-don-vi.md: frontmatter description hợp lệ YAML
  OK agents\ktc-kiem-san-pham.md: frontmatter description hợp lệ YAML
  OK agents\ktc-tra-cuu-can-cu.md: frontmatter description hợp lệ YAML
  OK agents\ktc-tu-cai-tien.md: frontmatter description hợp lệ YAML
  OK agents\ktc-tu-hoc.md: frontmatter description hợp lệ YAML
  OK agents\ktc-xac-minh-minh-chung.md: frontmatter description hợp lệ YAML
  OK ca ngược: mô tả có ': ' không trong ngoặc bị phát hiện
  OK ca ngược: mô tả trong ngoặc được chấp nhận
  OK ca ngược: tệp thiếu khối bị phát hiện
KET LUAN: SACH
````

## 1-Plugin/log-hoi-quy/test_plugin_131.txt (sha256 `1c09808ad43425cb3860c05c64853962d1c2d6ad9fd41d425850b92dfb976250`)

````text
== A. Guard 2 tầng ==
  OK chặn: python -c open(..., 'w') [ChatGPT L3] (được: chan)
  OK chặn: python3 open mode='a' (đường dẫn \) (được: chan)
  OK chặn: heredoc Path().write_text (được: chan)
  OK chặn: Path().unlink (được: chan)
  OK chặn: powershell -Command Set-Content [ChatGPT L3] (được: chan)
  OK chặn: pwsh -c Remove-Item (được: chan)
  OK chặn: cmd /c del (được: chan)
  OK chặn: bash -c rm (được: chan)
  OK chặn: -EncodedCommand (không phân tích được) (được: chan)
  OK chặn: cd vào kho rồi > tệp tương đối (được: chan)
  OK chặn: Set-Location vào kho rồi Remove-Item (được: chan)
  OK chặn: đường dẫn UNC (được: chan)
  OK chặn: Write (giữ nguyên từ 1.3.0) (được: chan)
  OK chặn: rm trực tiếp (giữ nguyên) (được: chan)
  OK chặn (đích không xác định): shutil.copy vào kho (đích trong tham số) (được: chan)
  OK chặn (đích không xác định): biến trỏ kho + os.remove (được: chan)
  OK chặn (đích không xác định): node fs.writeFileSync qua biến (được: chan)
  OK chặn 1.3.2: biến d + shutil.copy [ChatGPT L4 F4-01] (được: chan)
  OK chặn 1.3.2: ln -s tạo liên kết tới kho (được: chan)
  OK chặn 1.3.2: New-Item SymbolicLink tới kho (được: chan)
  OK chặn 1.3.2: cmd mklink /D tới kho (được: chan)
  OK cho qua 1.3.2: cd vào kho, ghi RA C:\… (đường dẫn Windows tuyệt đối) (được: qua)
  OK cho qua 1.3.2: ln -s ngoài kho (được: qua)
  OK cho qua 1.3.2: sed -i biểu thức nhắc kho, tệp ngoài kho [chặn nhầm thật 27/9] (được: qua)
  OK cho qua 1.3.2: sed -i -e biểu thức nhắc kho, tệp ngoài kho (được: qua)
  OK cho qua 1.3.2: perl -pi -e biểu thức nhắc kho, tệp ngoài kho (được: qua)
  OK cho qua 1.3.3: python đọc kho, str.replace [chặn nhầm thật 28/9] (được: qua)
  OK cho qua 1.3.3: python os.path.join + str.replace, chỉ đọc (được: qua)
  OK cho qua 1.3.3: pandas DataFrame.rename, chỉ đọc (được: qua)
  OK chặn 1.3.3 (ca ngược): Path qua biến .rename (được: chan)
  OK chặn 1.3.3 (ca ngược): Path(ngoài).replace(đích trong kho) (được: chan)
  OK chặn 1.3.3 (ca ngược): os.replace vào kho (được: chan)
  OK 1.3.6: Write vào Memory của plugin → chan (được: chan)
  OK 1.3.6: Edit vào bộ đệm .claude/plugins → chan (được: chan)
  OK 1.3.6: Write vào thư mục làm việc (ngoài plugin) → qua (được: qua)
  OK cho qua 1.3.4: đứng trong kho, heredoc Python có `if i > 45:` [chặn nhầm thật 28/9] (được: qua)
  OK chặn 1.3.4 (ca ngược): thân heredoc đưa cho bash, ghi tương đối trong kho (được: chan)
  OK chặn 1.3.4 (ca ngược): thân heredoc Python ghi tệp trong kho (tầng 2) (được: chan)
  OK chặn 1.3.4 (ca ngược): cat > tệp tương đối trên dòng heredoc (được: chan)
  OK cho qua: python đọc tệp trong kho (được: qua)
  OK cho qua: cd vào kho, chỉ tìm (được: qua)
  OK cho qua: cd vào kho, ghi RA đường dẫn tuyệt đối ngoài kho (được: qua)
  OK cho qua: python ghi ngoài kho (được: qua)
  OK cho qua: powershell -Command ghi ngoài kho (được: qua)
  OK cho qua: lệnh thường (được: qua)
  OK cho qua: cp TỪ kho ra ngoài (giữ nguyên) (được: qua)
== B. Nhật ký PostToolUse không lưu lệnh thô ==
  OK mặc định: không lưu lệnh Bash, mô tả Agent, mẫu Grep [ChatGPT L3 P0-1]
  OK mặc định: email trong mô tả Agent không vào nhật ký
  OK Bash được phân loại hành động (không lưu lệnh)
  OK Agent: chỉ lưu loại agent
  OK Write: lưu đường dẫn tương đối trong dự án
  OK chọn ghi (KTC_NHAT_KY_NOI_DUNG=1): lệnh được che số định danh, email
  OK ca ngược: chuỗi chứa marker bị phát hiện
== C. SessionStart nạp gọn ==
  OK nạp mặc định ≤ 4500 ký tự (được 768)
  OK nạp mặc định không in lệnh thô
  OK ca ngược: vượt ngân sách bị phát hiện
== D. Bản dựng 31-Plugin 1.3.1 ==
  OK plugin.json 1.3.x (đang 1.3.13)
  OK skills\bao-cao\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\bao-cao\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\bao-cao\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\bao-cao\SKILL.md: không còn dòng lịch sử phiên bản
  OK skills\ke-hoach\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\ke-hoach\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\ke-hoach\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\ke-hoach\SKILL.md: không còn dòng lịch sử phiên bản
  OK skills\kpi-lap-ke-hoach\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\kpi-lap-ke-hoach\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\kpi-lap-ke-hoach\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\kpi-lap-ke-hoach\SKILL.md: không còn dòng lịch sử phiên bản
  OK skills\kpi-tu-danh-gia\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\kpi-tu-danh-gia\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\kpi-tu-danh-gia\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\kpi-tu-danh-gia\SKILL.md: không còn dòng lịch sử phiên bản
  OK skills\quan-tri\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\quan-tri\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\quan-tri\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\quan-tri\SKILL.md: không còn dòng lịch sử phiên bản
  OK skills\soan-thao-vb\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\soan-thao-vb\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\soan-thao-vb\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\soan-thao-vb\SKILL.md: không còn dòng lịch sử phiên bản
  OK skills\the-thuc\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\the-thuc\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\the-thuc\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\the-thuc\SKILL.md: không còn dòng lịch sử phiên bản
  OK skills\theo-doi-cv\SKILL.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK skills\theo-doi-cv\SKILL.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK skills\theo-doi-cv\SKILL.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK skills\theo-doi-cv\SKILL.md: không còn dòng lịch sử phiên bản
  OK agents\ktc-hieu-luc-vien-dan.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK agents\ktc-hieu-luc-vien-dan.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK agents\ktc-hieu-luc-vien-dan.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK agents\ktc-hieu-luc-vien-dan.md: không còn dòng lịch sử phiên bản
  OK agents\ktc-kiem-ho-so-don-vi.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK agents\ktc-kiem-ho-so-don-vi.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK agents\ktc-kiem-ho-so-don-vi.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK agents\ktc-kiem-ho-so-don-vi.md: không còn dòng lịch sử phiên bản
  OK agents\ktc-kiem-san-pham.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK agents\ktc-kiem-san-pham.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK agents\ktc-kiem-san-pham.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK agents\ktc-kiem-san-pham.md: không còn dòng lịch sử phiên bản
  OK agents\ktc-tra-cuu-can-cu.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK agents\ktc-tra-cuu-can-cu.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK agents\ktc-tra-cuu-can-cu.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK agents\ktc-tra-cuu-can-cu.md: không còn dòng lịch sử phiên bản
  OK agents\ktc-tu-cai-tien.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK agents\ktc-tu-cai-tien.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK agents\ktc-tu-cai-tien.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK agents\ktc-tu-cai-tien.md: không còn dòng lịch sử phiên bản
  OK agents\ktc-tu-hoc.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK agents\ktc-tu-hoc.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK agents\ktc-tu-hoc.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK agents\ktc-tu-hoc.md: không còn dòng lịch sử phiên bản
  OK agents\ktc-xac-minh-minh-chung.md: khối lõi ≤ 2500 ký tự (được 2495)
  OK agents\ktc-xac-minh-minh-chung.md: khối lõi có quy tắc xử lý bất đồng skill–agent
  OK agents\ktc-xac-minh-minh-chung.md: có khối <plugin_paths> (không xin quyền thư mục dự án), đặt sau khối lõi
  OK agents\ktc-xac-minh-minh-chung.md: không còn dòng lịch sử phiên bản
  OK skills\bao-cao: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK skills\ke-hoach: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK skills\kpi-lap-ke-hoach: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK skills\kpi-tu-danh-gia: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK skills\quan-tri: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK skills\soan-thao-vb: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK skills\the-thuc: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK skills\theo-doi-cv: có references/00-Quy-Tac-Bat-Bien-Day-Du.md
  OK bao-cao: lịch sử v3.8–v3.14 được giữ trong references/LICH-SU-PHIEN-BAN.md
== E. kiem_vien_dan đọc tệp văn bản nhiều bảng mã (1.3.2, Gemini L4) ==
  OK utf-8: đọc được, phát hiện lỗi viện dẫn (VD02)
  OK utf-16: đọc được, phát hiện lỗi viện dẫn (VD02)
  OK cp1258: đọc được, phát hiện lỗi viện dẫn (VD02)
  OK ca ngược: kết quả sạch không chứa mã lỗi
== F. kiem_ho_so.py: bắt tệp TrackChanges đã bị chấp nhận thay đổi / sai mã băm (1.3.2, F4-03) ==
  OK hồ sơ đúng: TrackChanges còn đánh dấu, mã băm khớp → sạch
  OK ca ngược: tệp bị chấp nhận thay đổi sau khi lập hồ sơ → lỗi
  OK ca ngược: tệp tên TrackChanges nhưng 0 đánh dấu → lỗi
KET LUAN: SACH
````

## 1-Plugin/log-hoi-quy/test_plugin_nhat_ky_backup.txt (sha256 `2e2d8a95e7e1803dcebb17da555f8697504990ff6b38628c0d0944925a71ebd3`)

````text
== ktc_nhat_ky.py ==
  OK ghi được thao tác trong dự án
  OK không ghi nội dung tệp vào log
  OK ca ngược: ngoài dự án không tạo log
  OK ca ngược: stdin hỏng vẫn thoát 0
  OK nạp context liệt kê tệp đã sửa
  OK #riêng/#rieng: không ghi nội dung lời nhắn
  OK #riêng: vẫn ghi mốc thời gian, không tín hiệu học
  OK 1.3.0: lời nhắn thường KHÔNG ghi nội dung (mặc định)
  OK 1.3.0: lời nhắn thường vẫn ghi độ dài (thông tin mô tả)
  OK 1.3.0: có tín hiệu học vẫn KHÔNG ghi nội dung, chỉ ghi nhãn tín hiệu
  OK ca ngược: mở đầu #học -> ghi nội dung (bỏ nhãn #học)
  OK chọn ghi (biến môi trường) + có tín hiệu học -> ghi nội dung
  OK ca ngược: chọn ghi nhưng KHÔNG có tín hiệu học -> không ghi nội dung
  OK nội dung được ghi đã che số điện thoại, số định danh, email
  OK số hiệu văn bản "Quyết định số …" không bị tính là tín hiệu quyết định
  OK lời dưới 5 từ ("ok chốt nhé") không gắn tín hiệu
  OK 1.3.0: nhật ký cũ hơn 30 ngày bị xóa khi mở phiên
  OK ca ngược: nhật ký hôm nay không bị xóa
== ktc_backup_github.py ==
  OK chưa có remote: bỏ qua, thoát 0
  OK có remote: commit + push thành công
  OK --neu-can trong 24h: không chạy lại
  OK ca ngược: tệp tên giống bí mật -> dừng, không push
  OK không xóa tệp của người dùng khi dừng
  OK 1.3.0: tệp tên thường chứa số định danh -> dừng, không push
  OK git() truyền stdin=DEVNULL (bắt buộc cho pythonw/Task Scheduler)
  OK ca ngược: không tạo thư mục 04-Nhat-Ky-Tu-Dong trong kho khác
  OK kho khác: nhật ký backup rơi vào .git/ (không bị theo dõi)
  OK ca ngược: không chỉ định --du-an, kho thiếu 90-Nhat-Ky-Van-Hanh -> im lặng, không đẩy
  OK chỉ định rõ --du-an: backup được kho không phải KTC-Quan-tri
  OK ca ngược: chỉ định thư mục không phải kho git -> báo lỗi, thoát 1
  OK chạy dưới pythonw.exe: push thành công (mã 0, 2 commit)
  OK ca ngược: kiểm thử không ghi gì vào nhật ký THẬT của dự án
  OK nhật ký tự động nằm trong .gitignore
  OK không còn tệp nhật ký tự động nào được git theo dõi
KET LUAN: SACH
````

## 1-Plugin/log-hoi-quy/test_task_id_bc736.txt (sha256 `d350789581018bc0d118d9b4d2a02a28235178ca298e072fcff7b9267f0e25d1`)

````text
  OK có hồ sơ thật để thử (26 tệp)
  OK tệp chưa có cột Task_ID: không mất gì so với v3.2 []
  OK lấy lại đúng 2 nhiệm vụ 'Tổng hợp/Tổng kết…' v3.2 bỏ sót (thực tế: 2)
  OK đọc được Task_ID ở cột cuối (dò theo tên tiêu đề)
  OK ca ngược: mã trùng -> cảnh báo
  OK ca ngược: mã sai định dạng -> cảnh báo
  OK tệp gốc không có cột -> không cảnh báo Task_ID
KET LUAN: SACH
````

## 1-Plugin/log-hoi-quy/test_thu_muc.txt (sha256 `c752c523c69ba06706d44f0d3d1c3b1cec25b6dcdadd15c7edaf7ce1dc4a90dd`)

````text
== A. Khởi tạo, nhận diện ==
  OK thư mục chưa kết nối → chế độ 'khong'
  OK tạo 10-Dau-Vao/, 30-Ket-Qua/
  OK tệp đánh dấu ghi mã chuẩn (chữ hoa) P-TCCB
  OK có 00-HUONG-DAN.md
  OK thư mục con nhận đúng gốc đơn vị (tìm lên cha)
  OK khởi tạo lại: không ghi đè tệp đã có
== B. Ca ngược — phải từ chối ==
  OK NGƯỢC: thư mục đã của P-TCCB, khởi tạo mã khác → từ chối
  OK NGƯỢC: thư mục không tồn tại → từ chối
  OK NGƯỢC: mã ngoài 11 mã chuẩn → từ chối, không đoán
  OK NGƯỢC: trong KTC-Database → từ chối
  OK NGƯỢC: không tạo tệp nào trong kho
  OK NGƯỢC: trong dự án KTC-Quan-tri → từ chối
  OK dự án vẫn nhận là 'du-an' (ưu tiên)
  OK NGƯỢC: thư mục con của thư mục đã kết nối → từ chối (dùng gốc)
== C. CLI ==
  OK CLI kiem trả JSON đúng
  OK NGƯỢC: CLI khởi tạo mã sai → mã thoát 2
== D. Hook đo thể thức chạy trong thư mục đơn vị ==
  OK tệp .docx lệch chuẩn trong thư mục đơn vị → hook đo, báo (mã 2)
  OK NGƯỢC: thư mục chưa kết nối → hook im lặng như trước (mã 0)
== E. Bản sao trong kỹ năng điều phối khớp nguồn ==
  OK 22-KTC-Dieu-Phoi/scripts/ktc_thu_muc.py trùng byte với 29-Cong-Cu/plugin_src/scripts/

KET LUAN: SACH
````

## 1-Plugin/log-hoi-quy/test_tra_hieu_luc.txt (sha256 `949e741e7d6c1f0d1a1a4232fc66e32174345e64e82fa759a384c54a89e8e524`)

````text
  OK trích đủ 9 văn bản, kể cả viết tắt “NĐ 30/2020/NĐ-CP” và 3 số hiệu Đảng (được 9)
  OK QĐ 988 → THAY_THE (chuỗi đã biết)
  OK Luật Xây dựng → KHO_GHI_HET_HIEU_LUC từ metadata
  OK NĐ 85/2025 khớp đúng tệp, KHÔNG khớp “275-2025 sửa đổi NĐ 85”
  OK TT 36/2026/TT-BXD không khớp nhầm QĐ 36/2026/QĐ-TTg
  OK NĐ 30/2020 (tên tệp dạng 30_2020_ND-CP) có trong kho
  OK TB 916 không có trong kho → CẦN XÁC MINH
  OK “Luật Giáo dục” chỉ khớp đúng luật, không khớp “Phổ biến, giáo dục pháp luật” hay “Giáo dục nghề nghiệp” (được ['12. Luat Giao duc -72-VBHN-VPQH.docx'])
  OK “Luật Giáo dục nghề nghiệp” khớp đúng tệp
  OK trích được “Kết luận số 198-KL/TW” (loại Kết luận + số hiệu Đảng)
  OK trích được “Quyết định số 366-QĐ/TW”
  OK trích được “Hướng dẫn số 05-HD/VPTW”
  OK KL 198-KL/TW khớp đúng tệp Kết luận, KHÔNG khớp “Kế hoạch 198-KH-CĐKT” (được ['Ket luan 198-KL-TW Bo Chinh tri.docx'])
  OK “giai đoạn 2021-2025” không bị nhận nhầm là số hiệu
  OK không đọc được kho → mọi văn bản là CẦN XÁC MINH, không kết luận
  OK tệp .md vẫn được kiểm viện dẫn (được 3 gợi ý, phải > 0)
  OK ca ngược: không còn giới hạn kiểm viện dẫn theo đuôi .docx

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_trackchanges.txt (sha256 `ba98affe244a475333eddc66d91837e7c8a725f251f97c5fb945fb4638644aed`)

````text
Goc: 3 doan, 3 hang bang

--- Nhat ky phien lam viec ---
# Nhật ký sửa đổi — `D:\.CLAUDE code\KTC-Quan-tri\92-Kinh-Nghiem\02-Regression\Cases\..\Fixtures\goc.docx`

**Tổng số thay đổi:** 5

Bỏ: **1** · Bỏ hàng bảng: **1** · Bổ sung: **1** · Điều chỉnh: **2**

| # | Loại | Vị trí | Nội dung cũ | Nội dung mới |
|---|---|---|---|---|
| 1 | Điều chỉnh | đoạn 2 | 2.000 hoc sinh | 2.150 hoc sinh |
| 2 | Điều chỉnh | đoạn 2 | 80% | 86% |
| 3 | Bỏ | đoạn 3 | da tham muu cho Lanh dao Truong  | — |
| 4 | Bổ sung | sau đoạn 1 | — | 3.1. Cong tac tu van huong nghiep duoc trien khai som. |
| 5 | Bỏ hàng bảng | bảng 1, hàng 2 | O10 \| O11 \| O12 | — |

--- Validator ---
DAT: True
  thong ke: {'theo_author': {'Nội dung bổ sung (Claude)': 1, 'Nội dung điều chỉnh (Claude)': 4, 'Nội dung bỏ (Claude)': 5}, 'tong_danh_dau': 10}

--- nhat_ky_sua_doi() doc lai tu file ---
# Nhật ký sửa đổi — `D:\.CLAUDE code\KTC-Quan-tri\92-Kinh-Nghiem\02-Regression\Cases\..\Fixtures\sua.docx`

**Tổng số thay đổi:** 5

Bỏ: **1** · Bỏ hàng bảng: **1** · Bổ sung: **1** · Điều chỉnh: **2**

| # | Loại | Vị trí | Nội dung cũ | Nội dung mới |
|---|---|---|---|---|
| 1 | Bổ sung | đoạn 2 | — | 3.1. Cong tac tu van huong nghiep duoc trien khai som. |
| 2 | Điều chỉnh | đoạn 3 | 2.000 hoc sinh | 2.150 hoc sinh |
| 3 | Điều chỉnh | đoạn 3 | 80% | 86% |
| 4 | Bỏ | đoạn 4 | da tham muu cho Lanh dao Truong  | — |
| 5 | Bỏ hàng bảng | bảng 1, hàng 2 | O10 \| O11 \| O12 | — |

--- doi_chieu_goc ---
{'doan_goc': 3, 'doan_sau_khi_tu_choi_het': 3, 'doan_khop': 3, 'ty_le_khoi_phuc': 1.0, 'danh_dau': 10, 'nghi_soan_lai_tu_dau': False}

Reload OK — file hop le voi python-docx
Chan ghi de goc: OK - Không được ghi đè file gốc — đổi tên đầu ra.

--- Ca thu: soan lai tu dau ---
{'doan_goc': 3, 'doan_sau_khi_tu_choi_het': 3, 'doan_khop': 1, 'ty_le_khoi_phuc': 0.333, 'danh_dau': 0, 'nghi_soan_lai_tu_dau': True}

============================================================
CA THU NGUOC — xoa nguyen doan / khoang doan / bang
============================================================
  ✓ xoa_tu_den bo dung 6 doan (Phan I -> truoc Phan II)  -> 6
  ✓ xoa_doan bo dung 1 doan                              -> 1
  ✓ xoa_bang bo dung 3 hang                              -> 3
  ✓ validator OOXML dat (dat <w:del> dung cho trong pPr) []
  ✓ sau khi chap nhan chi con 2 doan                     -> ['Phan II', 'Giu lai dong nay']
  ✓ khong con doan RONG sot lai                          
  ✓ sau khi tu choi tro ve du 9 doan                     -> 9
  ✓ xoa_doan: moc sai bao ValueError                     
  ✓ xoa_tu_den: moc sai bao ValueError                   

DAT — 3 phuong thuc xoa hoat dong dung va bao loi dung cho
````

## 1-Plugin/log-hoi-quy/test_tu_du_plugin.txt (sha256 `b8af706796bdeb6af99f06842dc4bd9ce36e56bfa4132d21c9114002bc43a055`)

````text
== A. Không có SKILL.md lồng, không còn gói .skill lồng trong zip ==
  OK chỉ có SKILL.md ở skills/<tên>/ (lồng: [])
  OK zip ktc-quan-tri-1.3.13.zip không mang gói .skill lồng
== B. Phần trước chỉ có trong dự án nay có trong gói ==
  OK có skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/references/output-contract.md
  OK có skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/references/template-format-dna.md
  OK có skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/scripts/analyze_plan_templates.py
  OK có skills/theo-doi-cv/assets/00-Template-Routing-KTC-Theo-doi-CV.docx
  OK có skills/bao-cao/assets/00. Mau bao cao thang (cap Truong).docx
  OK có scripts/bc_thang.py
  OK có scripts/ktc_trackchanges.py
  OK có scripts/ktc_thu_muc.py
  OK có skills/quan-tri/references/BAN-DO-TEP.md
== C. Bảng đối chiếu tên tệp ==
  OK bảng đối chiếu: 13-Bang-Ma-Don-Vi (gốc) → 12-Bang-Ma-Don-Vi (trong gói)
  OK bảng đối chiếu có ≥ 10 chuẩn chung
  OK bảng ghi rõ tệp ở plugin 897 và kho KTC-Database
== D. Công cụ .py được kỹ năng, tác tử bảo chạy phải có trong gói ==
  OK mọi lệnh `python …py` trong SKILL.md, tác tử đều có công cụ trong gói (thiếu: [])
== E. Khối đường dẫn, phạm vi tác tử chỉ-dự-án ==
  OK skills\bao-cao\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK skills\ke-hoach\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK skills\kpi-lap-ke-hoach\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK skills\kpi-tu-danh-gia\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK skills\quan-tri\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK skills\soan-thao-vb\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK skills\the-thuc\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK skills\theo-doi-cv\SKILL.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents\ktc-hieu-luc-vien-dan.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents\ktc-kiem-ho-so-don-vi.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents\ktc-kiem-san-pham.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents\ktc-tra-cuu-can-cu.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents\ktc-tu-cai-tien.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents\ktc-tu-hoc.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents\ktc-xac-minh-minh-chung.md: khối <plugin_paths> trỏ BAN-DO-TEP
  OK agents/ktc-tu-hoc.md: ghi rõ chỉ chạy trong dự án, không xin quyền thư mục
  OK agents/ktc-tu-cai-tien.md: ghi rõ chỉ chạy trong dự án, không xin quyền thư mục
== F. Không giữ bản sao bộ quy tắc 897 ==
  OK không có tệp của bộ quy tắc 897 trong gói (có: [])

KET LUAN: SACH
````

## 1-Plugin/log-hoi-quy/test_tu_hoc.txt (sha256 `ee7f257773186195aa9be74445d5d10a95ed6f240bcb63f85b35d042396e5af5`)

````text
  OK ghi 4 lời người dùng, bỏ lệnh nội bộ /compact và <command…> (được 4)
  OK “từ nay… lưu ý” → tín hiệu quy-uoc
  OK “sai… sửa lại” → tín hiệu sua-sai
  OK lời thường không gắn tín hiệu (thử ngược)
  OK 1.3.0: mặc định không ghi nội dung, kể cả khi có tín hiệu học (R2-02)
  OK #học + lời dài: ghi nội dung, cắt ≤ 600 ký tự
  OK ngoài dự án KTC: không ghi
  OK nạp mục hiệu lực và chờ duyệt vào context
  OK không nạp mục bị bác/đã thay (thử ngược)
  OK đếm đúng 2 tín hiệu học chưa xử lý và nhắc gọi ktc-tu-hoc
  OK sau lượt học (mốc mới) không còn nhắc
  OK không ghi nhầm lời thử vào nhật ký THẬT

ĐẠT: 0 ca sai
````

## 1-Plugin/log-hoi-quy/test_validate_plan.txt (sha256 `a2ebb9c59e45747cf6565ea4829528d9bbea6d1a275d037a82ce59adb6588d5c`)

````text
  OK ghi_ke_hoach: mẫu trong assets/ giữ nguyên byte
  OK ghi_ke_hoach: giữ nguyên đủ 990 công thức của mẫu, đúng ô
  OK công thức thêm mới chỉ là cột F sản phẩm, 6 ô = 6 đầu việc
  OK NGƯỢC: ghi vào assets/ bị chặn
  OK Kế hoạch sạch → 0 LỖI (['KH13', 'KH17'])
  OK Dòng ví dụ đã xóa → không báo KH06
  OK Tự nhận nhóm từ tiêu đề sheet Đánh giá
  OK NGƯỢC: mẫu nguyên bản → KH06 dòng ví dụ 'Bahnar' chưa xóa
  OK NGƯỢC: mẫu nguyên bản → KH15 chưa điền họ tên, đơn vị
  OK Mẫu Quý III: ô số Quyết định trống → KH13 (cảnh báo)
  OK NGƯỢC: thiếu sản phẩm → KH01, thiếu thời hạn → KH02 (Đ12.4)
  OK NGƯỢC: số lượng 'vài' → KH03 không đo lường được
  OK NGƯỢC: mức 'Trung bình' mà hệ số 2 → KH05
  OK Phương án nhập tay → không áp KH05
  OK NGƯỢC: Trưởng/Phó đơn vị không có Trục 4 → KH10 (Đ12.1)
  OK Không giữ chức vụ thiếu Trục 4 → không KH10, chỉ cảnh báo KH11
  OK NGƯỢC: '100% viên chức toàn khoa' → KH09 (Đ4.8)
  OK NGƯỢC: đầu việc trùng nội dung → KH14 (Đ11.4a)
  OK Phương án A, sản phẩm có trong Danh mục → không KH08
  OK NGƯỢC: phương án A, sản phẩm ngoài Danh mục QĐ 2119 → KH08
  OK NGƯỢC: 21 đầu việc trong 1 Trục bị chặn (không tự chèn dòng làm lệch công thức)
  OK Mẫu truong-pho-don-vi: 6 Trục × 20 dòng, tổng 70, Trục chính ≥ 40%, nhóm chung 13/12/5
  OK Mẫu bo-mon: 6 Trục × 20 dòng, tổng 70, Trục chính ≥ 40%, nhóm chung 13/12/5
  OK Mẫu nha-giao: 6 Trục × 20 dòng, tổng 70, Trục chính ≥ 40%, nhóm chung 13/12/5
  OK Mẫu giao-vu: 6 Trục × 20 dòng, tổng 70, Trục chính ≥ 40%, nhóm chung 13/12/5
  OK Mẫu hanh-chinh: 6 Trục × 20 dòng, tổng 70, Trục chính ≥ 40%, nhóm chung 13/12/5
  OK Mẫu ho-tro: 6 Trục × 20 dòng, tổng 70, Trục chính ≥ 40%, nhóm chung 13/12/5

ĐẠT: 0 ca sai
````

=== HẾT TỆP N14-NHAT-KY-KIEM-TRA-1.3.13.md — MÃ KIỂM: EA8B95 ===
