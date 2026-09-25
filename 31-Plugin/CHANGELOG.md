# Changelog — KTC-Quan-tri Plugin

## 1.2.0 — 2026-09-25

- **Skill mới `kpi-tu-danh-gia`** (v1.0, `DL-20260925-001`): tự đánh giá, đề xuất xếp loại cá nhân theo quý (QĐ 1923).
  Từ kế hoạch KPI đã duyệt sinh **bảng hỏi Excel** (điểm tiêu chí chung, số thực tế 3 chiều, điều kiện, trường hợp đặc
  thù), rồi tính A 30 + B 70 **chặn trần 100% từng chỉ tiêu** [Đ11.6], đối chiếu ngưỡng 90/70/50 và điều kiện Đ19; xuất
  Bản tự đánh giá (`TDG-KPI-...xlsx`). Không quyết định mức xếp loại; không tính trần tỷ lệ HTXS (giai đoạn 3).
- `scripts/kpi_danh_gia.py` (mới); `kpi_mau.cau_truc_danh_gia()` dò động sheet Đánh giá cả 6 mẫu.
- skill `kpi-lap-ke-hoach` **1.1**: xóa số thực tế ví dụ của mẫu ở sheet KPI (L=4, N=100, P=100 — bản 1.0 để sót), tự
  xuống dòng, ẩn dòng trống; KH16; nhận đúng nhóm Trưởng/Phó đơn vị từ tiêu đề mẫu (bản 1.0 không nhận → KH10 bỏ sót).
- skill `quan-tri` **1.12**: đồng bộ quy tắc KPI gốc (Đ10.5 theo nhóm, Đ21.4/Đ21.6).
- Manifest qua `claude plugin validate --strict` (lần đầu chạy được).


## 1.1.2 — 2026-09-24

- Bảo mật nhật ký (`CP-20260924-001`, phương án A + C): lời nhắn bắt đầu bằng **`#riêng`** (hoặc `#rieng`) thì hook
  `ktc_nhat_ky.py` chỉ ghi mốc thời gian, không ghi nội dung, không đánh dấu tín hiệu học. Nhật ký tự động của dự án
  (`90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/`) ra khỏi git — backup tối không còn đẩy lời người dùng lên GitHub.

## 1.1.1 — 2026-09-24

- `scripts/doi_soat_so_lieu.py` đọc mục **ánh xạ bổ sung máy đọc** của bảng mã đơn vị: Ban Truyền thông → `P-THHC`
  (quyết định 14/9/2026, cấp hai), biến thể tên tệp có bằng chứng (`P.THHCQT`, `P QLKHCN`, `SP`, `Ban TT`). Kỳ 2026-09 hết
  đơn vị `?…`; DS06 chỉ còn K-KTNL chưa nộp Phụ lục Excel. Vẫn chỉ khớp chính xác.
- skill quan-tri **1.11**: bản sao `12-Bang-Ma-Don-Vi.md` đồng bộ bản gốc.

## 1.1.0 — 2026-09-24

- **Skill mới `kpi-lap-ke-hoach`** (v1.0, `DL-20260924-001`): lập kế hoạch và danh mục KPI cá nhân theo quý theo
  QĐ 1923/QĐ-CĐKT, 6 mẫu Kế hoạch + KPI (03-Templates/03-12). Hệ số quy đổi **không có mặc định** — bắt chọn phương
  án (mức độ: có văn bản · A theo TB 1052: dự thảo · A×B: chưa có văn bản · nhập tay). Giai đoạn 1: chỉ lập kế hoạch.
- Công cụ dùng chung `scripts/kpi_calc.py`, `kpi_mau.py`, `validate_plan.py` (KH01–KH15, mỗi lỗi dẫn Điều).
- skill quan-tri **1.10**: `references/30-KPI-Va-Xep-Loai.md` thành bản sao của quy tắc gốc
  `20-Chuan-Chung/19-Quy-Tac-KPI.md`; lập KPI cá nhân chuyển sang skill mới.

## 1.0.1 — 2026-09-24

- **`scripts/doi_soat_so_lieu.py`**: nhận mã đơn vị, loại KH/KQ và kỳ từ phần đầu tệp khi tên tệp/thư mục không theo quy
  ước (bố cục `10-Dau-Vao` ngày 21/9: `1. BAO CAO PL IIB/KHCB.xlsx`). Bản 1.0.0 gộp 10 đơn vị thành một và xếp
  `KHCB.xlsx` là kế hoạch mà vẫn thoát mã 0. Khớp mã chỉ chính xác theo bảng biến thể `13-Bang-Ma-Don-Vi.md`; không khớp
  thì tách riêng `?<tên>` và DS06 báo. Ảnh hưởng agent `ktc-kiem-ho-so-don-vi`, `ktc-kiem-san-pham`.
- skill soan-thao-vb **1.10**: đồng bộ quy tắc khai thác Internet với bản gốc 897 (tra `phapluat.gov.vn` trước tiên).

## 0.9.1 — 2026-09-19

- Cập nhật TB 1052/TB-CĐKT (`DL-20260919-007`): danh mục 371 sản phẩm đã gửi đơn vị rà soát (hạn 20/9), chưa ban hành;
  quy đổi STT 38 lĩnh vực → Trục/nội hàm. skill quan-tri 1.9.

## 0.9.0 — 2026-09-19

- Agent mới **`ktc-xac-minh-minh-chung`** (tổng 7) + công cụ `scripts/kiem_minh_chung.py` (MC01–MC07) — `DL-20260919-006`.
- Công cụ dùng chung **`scripts/doi_soat_so_lieu.py`** (DS01–DS06) — `ktc-kiem-ho-so-don-vi` và `ktc-kiem-san-pham` bắt buộc
  gọi, không tự cộng. Không tách agent đối soát riêng (tránh 3 agent cho 3 kết luận về cùng một con số).

## 0.8.1 — 2026-09-19

- Sửa lỗi Cowork từ chối tải lên: mô tả `plugin.json` 554 → 336 ký tự (giới hạn 500). Bản dựng tự chặn mô tả plugin > 500
  và mô tả skill/agent > 1024 ký tự.

## 0.8.0 — 2026-09-19

- **Vòng tự học** (`DL-20260919-005`): hook `UserPromptSubmit` ghi lời người dùng + tín hiệu học; agent mới **`ktc-tu-hoc`**
  rút tri thức vào `90-Nhat-Ky-Van-Hanh/05-Tri-Thuc-Tu-Hoc/TRI-THUC.md`; hook SessionStart nạp tri thức + nhắc tín hiệu chưa
  học; hook thể thức ghi cảnh báo làm bằng chứng. `ktc-tu-cai-tien` đọc mục `→ CP`. Tổng 6 agent.

## 0.7.0 — 2026-09-19

- **4 agent mới** (tổng 5, `DL-20260919-004`): `ktc-kiem-ho-so-don-vi`, `ktc-tra-cuu-can-cu`, `ktc-kiem-san-pham`,
  `ktc-hieu-luc-vien-dan`. Chỉ đọc, chỉ ghi báo cáo vào `30-Ket-Qua/<ngày>/…`; không lặp reviewer của 897.
- **Quét hiệu lực pháp lý + viện dẫn**: `scripts/tra_hieu_luc.py` (kèm `kiem_vien_dan.py`, `duong_dan.py`) — trích văn bản
  viện dẫn, đối chiếu kho 01–02 và chuỗi văn bản đã thay thế; không tự kết luận hết hiệu lực khi thiếu nguồn.

## 0.6.0 — 2026-09-19

- **Skill mới `the-thuc`** + Nguyên tắc 6 (`DL-20260919-003`): mọi sản phẩm .docx/.xlsx đạt chuẩn thể thức theo
  `03-Templates(1)`/`04-Good-Documents` (A4, lề 2-2-3-2 cm, Times New Roman 14, phần đầu UBND TỈNH QUẢNG NGÃI –
  TRƯỜNG CAO ĐẲNG KON TUM); chồng lên skill `docx`/`xlsx`. Công cụ `kiem_the_thuc.py` (đo + `--tao` từ mẫu).
- **Hook mới** `ktc_the_thuc_hook.py` (PostToolUse): tự đo .docx/.xlsx vừa sinh trong dự án KTC, còn Mức 1–2 → báo để sửa.
- 6 skill: quan-tri 1.8 · ke-hoach 3.9 · theo-doi-cv 1.7 · bao-cao 3.14 · soan-thao-vb 1.9 · the-thuc 1.0.

## 0.5.4 — 2026-09-19

- soan-thao-vb 1.8: bỏ bản sao `Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx` (không giữ bản sao quy tắc 897). Dọn hệ: gói/plugin cũ và kết quả chạy thử tháng 7–8 vào `99-Luu-Tru`.

## 0.5.3 — 2026-09-19

- Quy tắc viện dẫn văn bản (`DL-20260919-002`): `17-Quy-Tac-Vien-Dan.md` (NĐ 30 · Pháp lệnh hợp nhất Điều 4 · quy ước
  Trường qua 897) + Nguyên tắc 5. Văn bản hành chính: Luật/Pháp lệnh **không ghi số hiệu**, kể cả khi có VBHN. Công cụ
  tự kiểm `kiem_vien_dan.py` (VD01–VD12). 5 skill: quan-tri 1.7 · ke-hoach 3.8 · theo-doi-cv 1.6 · bao-cao 3.13 ·
  soan-thao-vb 1.7.

## 0.5.2 — 2026-09-19

- Nguyên tắc 3 (`DL-20260919-001`): đơn vị gửi dữ liệu thô vào khung chat, skill xuất sản phẩm trong phiên/project,
  người dùng tải về gửi P-THHC. Tên tệp trả về chuẩn `<mã đơn vị>_<loại>_<kỳ>_v<N>` + phiếu tự kiểm (còn lỗi →
  "chưa nên gửi"). 5 skill: quan-tri 1.6 · ke-hoach 3.7 · theo-doi-cv 1.5 · bao-cao 3.12 · soan-thao-vb 1.6.

## 0.5.1 — 2026-09-18

- Đính chính `DL-20260918-005`: chỉ bản chép KTC-Database trên máy bị xóa (đã cũ: thiếu 163/1.171 tệp). Skill/script
  đọc **bản gốc trên Google Drive** (`duong_dan.py` dò ổ Drive). 5 skill: quan-tri 1.5 · ke-hoach 3.6 · theo-doi-cv 1.4 ·
  bao-cao 3.11 · soan-thao-vb 1.5. C12 so kích thước trước, không tải cả kho từ Drive.

## 0.5.0 — 2026-09-18

- **Nguyên tắc 4** (`DL-20260918-005`) nhân xuống 5 skill: quan-tri 1.4 · ke-hoach 3.5 · theo-doi-cv 1.3 · bao-cao 3.10 ·
  soan-thao-vb 1.4. Mỗi loại đầu vào một nơi lưu; tìm KTC-Database qua `KTC_DATABASE_DIR` → thư mục ngang cấp →
  Google Drive → hỏi (không ghi cứng ổ đĩa — dự án sẽ chỉ còn trên Google Drive); quy tắc làm việc trên Drive.
- `ke-hoach`: `10-Dau-Vao/02-Cap-Truong/<nhóm kỳ>/<kỳ>/` (01-Nam/02-Quy/03-Thang/04-Chuyen-De); văn bản cấp trên
  đọc tại `KTC-Database/01-Legal-Database/` (bỏ nhánh `04-Van-Ban-Cap-Tren`).

## 0.4.1 — 2026-09-18

- `quan-tri` 1.3: sửa chỉ mục KTC-Database — `12-Output` của kho bị đổi nhầm thành `30-Ket-Qua` trong đợt
  kết cấu thư mục (`DL-20260918-004`). Rà toàn bộ diff đợt đó: chỉ 1 chỗ nhầm.

## 0.4.0 — 2026-09-18

- Kết cấu lại thư mục dự án theo nhóm INPUT (1x) / PROCESS (2x) / OUTPUT (3x) / quản trị hệ (9x)
  (`DL-20260918-004`). Bản dựng plugin nay ở `31-Plugin/`; nguồn hook/agent ở `29-Cong-Cu/plugin_src/`.
- 5 skill đóng gói lại: quan-tri 1.2 · ke-hoach 3.4 · theo-doi-cv 1.2 · bao-cao 3.9 · soan-thao-vb 1.3 — thêm
  **Nguyên tắc 3**: tài khoản Team (phòng/khoa/bộ môn) không có thư mục dự án → lấy đầu vào từ tệp đính kèm
  trong phiên, trả kết quả để tải về.
- Hook nhật ký nhận diện dự án qua `90-Nhat-Ky-Van-Hanh/`; ở máy thành viên không có thư mục này → không ghi.

## 0.3.0 — 2026-09-18

- `bao-cao` nâng lên **v3.8** (gói `ktc-bao-cao-v3.8.skill`): đọc cột `Task_ID` (KI-001, Lãnh đạo thống nhất,
  `DL-20260918-003`); sửa lỗi nhiệm vụ "Tổng hợp/Tổng kết…" bị bỏ mất. `quan-tri`: cập nhật quy tắc Task_ID.

## 0.2.2 — 2026-09-18

- Sửa lỗi nhật ký: khi hook báo thư mục làm việc nằm ngoài dự án, script vẫn lùi về thư mục đang chạy và
  ghi nhầm vào nhật ký KTC-Quan-tri (phát hiện qua dòng "Write a" do kiểm thử sinh ra). Nay chỉ lùi về khi
  hook không báo thư mục nào. Không ghi dòng rỗng khi dữ liệu hook hỏng.
- Hồi quy thêm ca ngược: chạy kiểm thử từ chính thư mục dự án và kiểm nhật ký thật không đổi (ca này thất bại
  với bản cũ, đạt với bản mới). Đã dọn 10 dòng rác khỏi nhật ký 18/9.

## 0.2.1 — 2026-09-18

- Thư mục dữ liệu nền đổi tên `11-Du-lieu-Cong-Viec` → `11-Du-lieu-Cong-Viec` (yêu cầu người dùng). Cập nhật
  mọi tham chiếu còn hiệu lực (CLAUDE.md, README, 20-Chuan-Chung, references, agent); đóng gói lại
  `ktc-quan-tri.skill` từ nguồn rời. Hồ sơ lịch sử trong `30-Ket-Qua/` giữ nguyên tên cũ.
- `Claude outputs/` (tệp ứng dụng Claude xuất ra) đưa vào `.gitignore` — không lên backup GitHub.

## 0.2.0 — 2026-09-18

Thêm 3 cơ chế theo yêu cầu người dùng. Nguồn viết tay ở `29-Cong-Cu/plugin_src/` (script build chép vào, không sửa
trong `31-Plugin/`). Hồi quy: `92-Kinh-Nghiem/02-Regression/Cases/test_plugin_nhat_ky_backup.py` — 10 ca, có ca ngược.

- **Agent `ktc-tu-cai-tien`** (`agents/`): đọc nhật ký tự động, Process Memory, Known Issues, Decision Log, kết
  quả `kiem_tra_he_thong.py` → viết đề xuất `CP-YYYYMMDD-NNN` trạng thái *Chờ duyệt* vào
  `92-Kinh-Nghiem/03-Change-Proposals/`. **Không tự sửa** skill/quy tắc/dữ liệu (nguyên tắc bất biến #6);
  bị chặn công cụ `Edit`.
- **Tự ghi nhật ký + nạp vào context** (`scripts/ktc_nhat_ky.py`): `PostToolUse` ghi 1 dòng JSONL cho mỗi
  Write/Edit/Bash/PowerShell/Skill/Agent vào `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/YYYY-MM-DD.jsonl` (chỉ
  tên công cụ + đối tượng, **không** ghi nội dung tệp); `SessionStart` in tóm tắt 2 ngày gần nhất vào
  context; `SessionEnd` đánh dấu kết thúc phiên. Chỉ hoạt động trong thư mục KTC-Quan-tri.
- **Tự backup GitHub** (`scripts/ktc_backup_github.py`): commit + push thường (không force), Task Scheduler
  21:00 hằng ngày (`KTC-Quan-tri-Backup-GitHub`, chạy bù khi máy bật lại) + `SessionStart` chạy bù nếu quá
  24h. Dừng nếu có tệp tên giống bí mật. **Chưa nối remote** — cần người dùng cung cấp URL repo private.

## 0.1.1 — 2026-09-18

- `ktc-soan-thao-vb` nâng lên **v1.2** ở nguồn (gói `.skill` gốc, không chỉ trong plugin): thêm hẳn
  `14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`, `15-Skill-Track-Changes.md`, `ktc_trackchanges.py` vào
  `references/Skill-Library/` của chính hệ đó, sửa 3 trích dẫn trong `SKILL.md` trỏ đúng vị trí trong gói
  (`references/Skill-Library/...`, không còn cần `${CLAUDE_PLUGIN_ROOT}`).
- `29-Cong-Cu/dong_goi_plugin.py` bỏ hàm vá riêng cho plugin (`vas_lo_hong_soan_thao_vb`) — không còn cần vì đã
  sửa tận gốc; script build lại đơn giản như 4 hệ còn lại (giải nén thuần túy, không vá thêm).
- Sửa lỗi build script: `don_sach()` từng xoá cả `README.md`/`CHANGELOG.md` viết tay ở gốc `31-Plugin/` vì dọn
  nguyên thư mục gốc — nay chỉ dọn các thư mục sinh tự động (`skills/`, `.claude-plugin/`, `hooks/`,
  `scripts/`), giữ nguyên tài liệu viết tay.
- Kiểm lại: 0 lỗi, 0 tệp thiếu/thừa so với 5 gói `.skill` nguồn, không còn tham chiếu
  `${CLAUDE_PLUGIN_ROOT}` nào trong toàn bộ 5 SKILL.md.

## 0.1.0 — 2026-09-18

Bản đầu tiên. Gộp 5 hệ KTC (quan-tri, bao-cao, ke-hoach, soan-thao-vb, theo-doi-cv) thành một plugin dùng
chung cho Cowork và Claude Code, thay vì 5 gói `.skill` rời.

- Dựng từ 5 gói `.skill` đã xác minh byte-for-byte cùng ngày (`DL-20260918-001`): `ktc-quan-tri.skill`,
  `ktc-bao-cao-v3.7.skill`, `ktc-ke-hoach-v3.3.skill`, `ktc-soan-thao-vb-v1.1.skill`,
  `ktc-theo-doi-cv-v1.1.skill`.
- Phát hiện 3 lỗ hổng tham chiếu có thật trong `ktc-soan-thao-vb` (tồn tại từ trước, không liên quan lần
  đóng gói này) và vá tạm riêng cho plugin. **Đã thay bằng bản sửa tận gốc ở 0.1.1**, xem mục trên.
- Hook `SessionStart` mới: `scripts/ktc_quan_tri_doctor.py` — in phiên bản tự khai của cả 5 skill.
- Chưa chạy `claude plugin validate --strict` (không có CLI trong môi trường dựng) — chỉ tự kiểm thủ công.
