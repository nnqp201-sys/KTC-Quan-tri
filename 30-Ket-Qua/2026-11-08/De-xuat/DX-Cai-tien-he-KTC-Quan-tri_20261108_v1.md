# Đề xuất cải tiến hệ KTC-Quan-tri

| Trường | Nội dung |
|---|---|
| Mã | DX-20261108-01 |
| Ngày lập | 08/11/2026 |
| Người lập | Trợ lý AI (Claude Code) — bản nháp, chưa qua thẩm định |
| Trạng thái | **ĐÃ THỰC HIỆN** P0, P1, P3 (08/11/2026) |
| Phạm vi | Hệ KTC-Quan-tri: tài liệu quản trị + plugin `ktc-quan-tri` (v1.4.2) + công cụ `29-Cong-Cu/` |
| Cách tiếp cận | Chỉ đọc; đề xuất — **không tự sửa** skill, quy tắc hay dữ liệu (nguyên tắc bất biến #6) |

**Nguồn đã đọc để lập báo cáo:** `00-README.md` · `CLAUDE.md` · `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`
· `92-Kinh-Nghiem/05-Known-Issues/Pending.md` · `31-Plugin/README.md` · `31-Plugin/CHANGELOG.md`
· `.claude-plugin/plugin.json` · `.claude-plugin/marketplace.json` · `.claude/settings.json`
· `.claude/rules/{20,21,22,24}` · `91-Tai-Lieu-Thiet-Ke/Mo-Ta-Chi-Tiet-He-KTC-DIS-Chat-Cowork-Code.md`
· `29-Cong-Cu/kiem_tra_he_thong.py` · `.gitignore` · `git status`.

---

## I. Kết luận nhanh

Hệ KTC-Quan-tri đã trưởng thành về nghiệp vụ (đã ban hành chính thức **TB 1153/TB-CĐKT ngày 12/10/2026**,
plugin **1.4.2** đang dùng, có 3 tầng kiểm thử, hook guard chặn ghi kho chuẩn, doctor tự chẩn đoán, nhật ký
/Process Memory/Decision Log). Rủi ro hiện nay **không nằm ở nghiệp vụ mà ở kỷ luật đồng bộ tài liệu và
tự động hoá kiểm tra**: các tệp khai báo phiên bản/README đã lệch nhau, còn nhiều đường dẫn cũ, và chưa có
cửa kiểm tra/CI hợp nhất. Bốn nhóm việc dưới đây xử lý đúng các lỗ hổng đó.

---

## II. Hiện trạng (đã kiểm chứng)

- **Không phải repo mã nguồn thuần** — đây là hệ quản trị nghiệp vụ (`.md/.docx/.xlsx` + Python tools +
  Claude plugin/skill), đồng bộ qua Google Drive for Desktop, sao lưu GitHub private.
- **Đã phát hành chính thức:** TB 1153/TB-CĐKT (12/10/2026); phân phối qua tài khoản `phongthhcqt`.
- **Plugin `ktc-quan-tri`: 1.4.2** — 8 skill, 38 agent, hook chặn ghi kho chuẩn + nhật ký + đo thể thức.
- **Điểm mạnh kỷ luật:** 3 tầng kiểm thử (`92-Kinh-Nghiem/02-Regression/`), bộ `test_*` rộng;
  `kiem_tra_he_thong.py` (Tầng 1, 13 phép kiểm); phân tách nguồn sự thật (`20-Chuan-Chung/`,
  `11-Du-lieu-Cong-Viec/`, `2A-KTC-Ra-Soat-897/`).

---

## III. Vấn đề phát hiện (kèm bằng chứng)

| # | Nhóm | Bằng chứng cụ thể |
|---|---|---|
| A | **Phiên bản & CHANGELOG lệch** | `plugin.json` + `marketplace.json` = **1.4.2**, nhưng `31-Plugin/CHANGELOG.md` chỉ có mục **1.4.0** rồi tới khối **"Chưa phát hành — dồn cho 1.3.14"** (số hiệu 1.3.14 đã lỗi thời). Thiếu mục 1.4.1, 1.4.2 dù `PLUGIN_VERSION` trong `29-Cong-Cu/dong_goi_plugin.py` ghi rõ 2 bản này (5/11/2026). |
| B | **README plugin lỗi thời** | `31-Plugin/README.md` ghi **"## 7 agent"** + bảng 7 dòng, trong khi `plugin.json`/`marketplace.json` nói **38 agent**. Mục Runtime support vẫn ghi "chưa nghiệm thu". |
| C | **README gốc lỗi thời** | `00-README.md` mục "Trạng thái hiện tại" còn ghi *"Giai đoạn chuẩn hóa (1/6)… chưa chốt Master Task Register"* — mâu thuẫn `MEMORY-INDEX.md` (đã ban hành TB 1153, plugin 1.3.13 chia sẻ Team). `README.md` ở gốc chỉ có 1 dòng tiêu đề (stub). |
| D | **Đường dẫn cũ còn sót** | Nhiều tệp tham chiếu còn trỏ `KTC-Ra-Soat-897-v2-Cai-tien/...` (đã đổi thành `2A-KTC-Ra-Soat-897/`); `Pending.md` tự ghi *"31-Plugin còn tham chiếu… dồn cho 1.3.14"*. |
| E | **Cây làm việc bẩn / chưa commit** | `git status` cho thấy nhiều tệp modified + **deleted** (vd `2A-KTC-Ra-Soat-897/LOI-V464.sha256`, loạt `.docx` trong `Ban-Track-Changes/`), trong khi `Pending.md` còn việc *"cập nhật `LOI-V45.sha256`"*. |
| F | **Trùng lặp bản sao gây nhiễu kiểm tra** | `.kilo/worktrees/` chứa bản sao **toàn kho**; `kiem_tra_he_thong.py` phải hard-code bỏ qua (`BO_QUA = (..., ".kilo", "_trung_gian")`) và từng báo 13 lỗi C7 giả từ đây. |
| G | **Doctor phân mảnh** | Có ≥3 "doctor": `ktc_quan_tri_doctor.py` (SessionStart plugin), `kiem_tra_he_thong.py` (Tầng 1), `test_doctor_897.py`. **Không có một lệnh/entrypoint thống nhất** chạy hết và in 1 kết luận. |
| H | **Không có CI** | Kiểm thử chạy tay; tự động hoá duy nhất là backup GitHub 21:00 (Task Scheduler). Không có GitHub Actions chạy Tầng 1 + regression khi push. |
| I | **Việc mở tồn đọng** | KI-010 (thiếu nhật ký chạy thử Chat), 39 mã `THIEU_DU_LIEU` chờ P-TCCB, 6 Khoa chưa có dữ liệu, KI-019 mở, plugin chưa dựng lại cho `kpi-tu-danh-gia` 1.4. |
| J | **Khả năng khám phá công cụ** | `29-Cong-Cu/` có **~60 script** ở mức gốc, không thấy `README.md` mức thư mục → khó biết script nào là entrypoint. |

---

## IV. Kế hoạch cải tiến đề xuất (ưu tiên P0 → P3)

### P0 — Đồng bộ tài liệu & "nguồn sự thật" (rủi ro thấp, giá trị cao)

1. **Cập nhật `31-Plugin/CHANGELOG.md`**: thêm mục 1.4.1, 1.4.2; gộp khối "Chưa phát hành — dồn cho
   1.3.14" vào đúng bản đã phát hành (1.4.0) hoặc đổi nhãn thành "dồn cho 1.4.3".
   *Kiểm chứng:* số hiệu trong CHANGELOG khớp `PLUGIN_VERSION` (`dong_goi_plugin.py`) và `plugin.json`.
2. **Sửa `31-Plugin/README.md`**: `"7 agent"` → số thật (38); rà lại mục Runtime support.
   *Kiểm chứng:* `grep "7 agent"` không còn kết quả.
3. **Sửa `00-README.md` mục "Trạng thái hiện tại"** cho khớp `MEMORY-INDEX.md`; cân nhắc gộp `README.md`
   (stub) vào `00-README.md` hoặc để lại dòng trỏ dẫn.
4. **Quét & thay `KTC-Ra-Soat-897-v2-Cai-tien` → `2A-KTC-Ra-Soat-897`** trong tệp nguồn
   `31-Plugin/skills/**` + `2A-KTC-Ra-Soat-897/references/**` (không sửa bản cài trên máy).

### P1 — Hợp nhất "doctor" + cửa kiểm tra một đầu mối

5. **Tạo entrypoint `29-Cong-Cu/doctor.py`** (hoặc `ktc-doctor`): gọi tuần tự
   (a) `kiem_tra_he_thong.py`; (b) so `PLUGIN_VERSION` repo ↔ `plugin.json` ↔ `marketplace.json`;
   (c) so bản cài `~/.claude/ktc-marketplace/ktc-quan-tri` ↔ `31-Plugin`; (d) tự thử guard;
   (e) chạy nhanh các `test_*` trọng yếu — rồi in **một dòng kết luận `ĐAT/KHONG_DAT`** + mã thoát 0/1.
   *Kiểm chứng:* thêm `92-Kinh-Nghiem/02-Regression/Cases/test_doctor.py` (có **ca thử ngược**, theo
   yêu cầu trong `.claude/rules/22-kiem-thu-va-dong-goi.md`).
6. **Cập nhật `.claude/rules/22-kiem-thu-va-dong-goi.md`** để `doctor.py` là bước duy nhất cần nhớ.

### P2 — Tự động hoá & dọn nhiễu

7. **GitHub Actions CI** (`.github/workflows/kiem-tra.yml`): chạy `python 29-Cong-Cu/kiem_tra_he_thong.py`
   + regression Tầng 1/2 trên push/PR. `.gitignore` đã loại `30-Ket-Qua/*/KPI-ca-nhan/`,
   `04-Nhat-Ky-Tu-Dong/` → CI không cần dữ liệu nhạy cảm.
8. **Commit & đẩy phần đang dở** (nhóm E): chốt các sửa hiện có, cập nhật `LOI-V45.sha256`, dọn
   `99-Luu-Tru/Can-Xoa/` theo đúng quy trình "người dùng tự xóa".
9. **Giảm nhiễu `.kilo/worktrees`**: thêm vào `.gitignore`, hoặc tài liệu hoá + giữ ngoại lệ trong
   `BO_QUA` (đã có), tránh tái phát "lỗi ảo".

### P3 — Khám phá & việc mở

10. **Sinh `29-Cong-Cu/README.md` (chỉ mục công cụ)** từ docstring/argparse: tên script · mục đích ·
    entrypoint · mã thoát. Nên tự sinh bằng script để không lệch (đồng bộ triết lý "một nguồn sự thật").
11. **Mẫu nạp cho KI-010**: tạo phiên bản "Chat trial" của `90-Nhat-Ky-Van-Hanh/02-Mau-Process-Memory.md`
    để người dùng chỉ việc điền.
12. **Đóng nợ 1.3.14 → 1.4.3**: dựng lại plugin với `kpi-tu-danh-gia` 1.4 + các mục 27–28/10 (cần người
    phụ trách quyết).

---

## V. Đánh giá công sức / rủi ro

| Nhóm | Công sức | Rủi ro | Ghi chú |
|---|---|---|---|
| P0 (tài liệu) | Thấp | Rất thấp | Làm ngay được, không chạm dữ liệu gốc |
| P1 (doctor) | Trung bình | Thấp | Cần thêm ca thử ngược theo quy tắc dự án |
| P2 (CI + dọn) | Trung bình | Trung bình | Cần xác nhận phạm vi commit; CI phải tôn trọng `.gitignore` |
| P3 (chỉ mục + mẫu) | Thấp–TB | Thấp | Không đổi hành vi hệ |

---

## VI. Giới hạn phương pháp & đề nghị

- Báo cáo lập **chỉ bằng đọc tài liệu/cấu trúc + `git status`**; **chưa chạy** `kiem_tra_he_thong.py`
  hay các `test_*`. Các con số "38 agent", mức lệch phiên bản… lấy theo tệp khai báo.
- Trước khi thực thi, **đề nghị chạy `python 29-Cong-Cu/kiem_tra_he_thong.py`** (và sau này là `doctor.py`)
  để xác nhận hiện trạng thật.
- Mọi thay đổi tài liệu/skill đề xuất ở đây **không tự thực hiện** — chờ người có thẩm quyền xem xét
  (đúng nguyên tắc bất biến #6 của `CLAUDE.md`).

---

## VII. Bước tiếp theo

1. Người phụ trách chọn nhóm ưu tiên (P0 → P3) để thi hành.
2. Với P0: sửa 4 điểm tài liệu (A–D) + chạy `kiem_tra_he_thong.py` làm bằng chứng trước/sau.
3. Với P1: viết `doctor.py` + `test_doctor.py`, cập nhật `rules/22`.
4. Với P2: thêm workflow CI, chốt commit và dọn `99-Luu-Tru/Can-Xoa/`.
5. Ghi Process Memory theo `90-Nhat-Ky-Van-Hanh/02-Mau-Process-Memory.md` sau mỗi ca.

---

*Bản nháp do trợ lý AI lập ngày 08/11/2026, phục vụ xem xét nội bộ. Không phải căn cứ pháp lý.*

