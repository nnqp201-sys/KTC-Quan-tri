---
name: ktc-bao-cao
description: "Tổng hợp, viết và kiểm tra báo cáo kết quả công tác tháng, quý, 6 tháng, năm của Trường Cao đẳng Kon Tum và các đơn vị (mẫu Phụ lục TB 736, 6 Trục kết quả trọng tâm theo TB 817, KPI số lượng - chất lượng - tiến độ). Dùng khi người dùng viết hoặc sửa đoạn đánh giá, nhận xét kết quả thực hiện nhiệm vụ; nêu tỷ lệ hoàn thành của đơn vị; tổng hợp bảng kết quả, tiến độ do đơn vị nộp (tệp Excel hoặc bảng dán trong khung chat); kiểm tra công thức KPI; đối chiếu kết quả với kế hoạch cùng kỳ; dựng báo cáo cấp Trường. Không dùng để soạn văn bản hành chính khác (dùng ktc-soan-thao-vb) hoặc rà soát trước trình ký (dùng ktc-ra-soat-897)."
---

# KTC-Bao-Cao / KTC-RIS v3.20

> **v3.20** (28/9/2026) — Tự đủ trong plugin (rà soát 28/9/2026): mẫu trắng báo cáo tháng (dự phòng, đã sửa 3 lỗi) vào `assets/`.

> **v3.19** (28/9/2026) — Chạy thật plugin 1.3.6 (Claude Code, thư mục thành viên): bỏ số hiệu dị dạng của bản gốc ('Số375BC-CĐKT'), đổi kỳ ở tiêu đề nhóm, Trục của phụ lục; bộ nhớ quá trình không ghi vào tệp plugin khi chạy ngoài dự án (ghi vào ghi chú đối soát).

> **v3.18** (28/9/2026) — Quy trình chính báo cáo tháng cấp Trường: 4 sản phẩm phát triển từ bản đã ban hành bằng `bc_thang.py` (Skill 37); đầu mối chưa nộp thì tổng hợp từ nguồn khác có ghi nguồn; lỗi công thức dòng không loại cả đơn vị; `fill_bc736.py` chỉ còn dự phòng (chạy thử 28/9/2026 kém bản 21/9).

> **v3.17** (28/9/2026) — Nguyên tắc 3: kết nối thư mục làm việc của đơn vị (Cowork, Claude Code ngoài dự án) — đọc `10-Dau-Vao/`, lưu `30-Ket-Qua/` trong thư mục đó (plugin 1.3.5).

> **v3.16** (28/9/2026) — Chuẩn 6 Trục: căn cứ Quyết định số 1923/QĐ-CĐKT Phụ lục I, II cho cột Điểm chấm, Hệ số quy đổi; quan hệ với Danh mục sản phẩm, công việc theo Quyết định số 2119/QĐ-CĐKT (DL-20260928-002).

> **v3.15** (27/9/2026) — Mô tả kích hoạt viết lại có dấu, nêu tình huống viết đoạn đánh giá, tổng hợp bảng kết quả dán trong khung chat: nghiệm thu 1.3.1 cho thấy các yêu cầu này không kích hoạt skill (thẩm định lần 3, DL-20260927-001).

> **v3.14** (19/9/2026) — Nguyên tắc 6 — chuẩn thể thức sản phẩm .docx/.xlsx theo 03-Templates(1)/04-Good-Documents, dùng kèm skill the-thuc (DL-20260919-003).

> **v3.13** (19/9/2026) — Quy tắc viện dẫn văn bản: NĐ 30 · Pháp lệnh hợp nhất · quy ước Trường; VBHC không ghi số hiệu Luật (DL-20260919-002).

> **v3.12** (19/9/2026) — Đơn vị nộp qua khung chat: tên tệp trả về chuẩn + phiếu tự kiểm, tải về gửi P-THHC (DL-20260919-001).

> **v3.11** (18/9/2026) — KTC-Database đọc bản gốc trên Google Drive (ổ Drive), bản chép cục bộ có thể cũ — đính chính DL-20260918-005.

> **v3.10** (18/9/2026) — Nguyên tắc 4 — nơi lưu đầu vào, tìm KTC-Database không qua ổ đĩa, Google Drive (DL-20260918-005).

> **v3.9** (18/9/2026) — Kết cấu lại thư mục theo nhóm INPUT/PROCESS/OUTPUT (DL-20260918-004); thêm Nguyên tắc 3 — đầu vào từ tệp đính kèm cho tài khoản Team.

> **v3.8** (18/9/2026) — `read_bc736_excel.py` v3.3: đọc cột `Task_ID` ở cuối bảng Phụ lục (KI-001, Lãnh đạo
> thống nhất 18/9/2026, `DL-20260918-003`) — mỗi nhiệm vụ có trường `task_id` (None nếu tệp chưa có cột, giữ
> đối chiếu gần đúng); cảnh báo `[TASK_ID SAI ĐỊNH DẠNG]` / `[TASK_ID TRÙNG]`, không tự sửa mã. Sửa lỗi nhiệm
> vụ có số TT bắt đầu bằng "Tổng hợp/Tổng kết…" bị coi là dòng cộng và bỏ mất.
## Trường Cao đẳng Kon Tum | Cập nhật: 14/9/2026
> **v3.5** = hợp nhất nhánh v3.4 (nghiệp vụ) + nhánh v2.5.1-memory (lớp Bộ nhớ),
> kèm sửa quy trình 14/9/2026 — xem `references/Skill-Library/PATCH-NOTES-v3.5.md`.

## [MỚI v3.4] NGUYÊN TẮC TIÊN QUYẾT — Xác định cấp báo cáo TRƯỚC KHI soạn
Trước khi soạn/tổng hợp BẤT KỲ báo cáo/kế hoạch nào, phải tự hỏi: "Đây là báo cáo cấp nào?"
- **Cấp Trường** (gửi UBND tỉnh/Sở/Bộ...) → chủ thể ngữ pháp TOÀN VĂN BẢN phải là **"Nhà trường"** — TUYỆT ĐỐI không dùng tên Phòng/Khoa làm chủ ngữ, dù việc đó do đơn vị nào thực hiện.
- **Cấp đơn vị** (Phòng/Khoa báo cáo nội bộ lên Trường) → chủ thể là tên đơn vị đó.
Chi tiết + ví dụ SAI/ĐÚNG: `references/Skill-Library/Skill-Tu-hoc-Phong-Cach-Bao-Cao.md` Mục 0.

## Bối cảnh Trường — số liệu nền bắt buộc biết
Trước khi tổng hợp bất kỳ báo cáo nào, AI phải nắm:

| Chỉ số | 2023 | 2024 | 2025 |
|--------|------|------|------|
| Tuyển sinh (tổng) | 1.786 | 2.664 | 2.551 |
| — Cao đẳng | 484 | 691 | 1.049 |
| — Trung cấp | 599 | 625 | 379 |
| — BD ngắn hạn | 165 | 655 | 933 |
| — Liên kết ĐH | 281 | 205 | 127 |

Quy mô đào tạo: 3.156 → 4.220 → 3.795 HSSV. Tốt nghiệp: 1.404 + 1.346 = 2.750.
Xu hướng cốt lõi: CĐ tăng mạnh (+117%), BD ngắn hạn tăng đột biến, TC và liên kết ĐH giảm.

## Vai trò trong kiến trúc hệ thống KTC
Hệ thứ 4 trong hệ thống KTC — **dùng chung kho 01-04** do `ktc-database` quản lý. Đối xứng ngược với `ktc-ke-hoach` (PIS): RIS nhìn về quá khứ, PIS nhìn về tương lai — cùng khung 6 Trục.

## 2 Nguyên tắc bắt buộc
Đọc `references/Skill-Library/00-Nguyen-Tac-Chung.md` trước mọi tác vụ.

## [MỚI v3.4] Định dạng nguồn dữ liệu — Excel Phụ lục TB736
Đơn vị nộp báo cáo **bắt buộc dạng Excel** đúng 1 trong 4 mẫu Phụ lục TB736 — xem `references/Skill-Library/31-Skill-Phu-Luc-TB736-Excel.md` **trước khi dùng Skill 32/33/34**:

| Phụ lục | Loại | Kỳ | Có KPI? |
|---|---|---|---|
| Ia | Kế hoạch | Quý | Không |
| Ib | Kế hoạch | Tháng | Không |
| IIb | Kết quả | Tháng | **Có** |
| IIc | Kết quả | Quý | **Có** |

Phụ lục IIb/IIc có hệ thống **KPI 3 chiều** (số lượng/chất lượng/tiến độ) với công thức cascade — không tự tính tay, dùng `read_bc736_excel.py`.

## Bộ nhớ quá trình — đọc TRƯỚC KHI làm bất cứ việc gì

Hệ lưu 3 loại ký ức, đừng nhầm lẫn:
- **Cách làm** (quy tắc tĩnh) → `references/Skill-Library/`
- **Dữ liệu** (đầu vào/đầu ra) → Google Drive
- **Quá trình** (đã làm gì, vì sao, gặp gì) → `references/Memory/` ← lớp này

**Mở đầu mọi phiên, chạy:**
```bash
python3 references/Memory/kiem_tra_bo_nho.py
```
In ra phiên bản đang cài, việc còn treo, lỗi đang mở, đơn vị cần lưu ý. Nếu báo lệch phiên bản
→ bản vá phiên trước đã mất, phải cài lại `.skill` trước khi làm tiếp.

Sau đó đọc `references/Memory/TRANG-THAI.md`. Chỉ mở các file còn lại khi cần —
xem bảng "khi nào đọc file nào" trong `references/Memory/README.md`.

**Nghĩa vụ ghi nhớ (bỏ qua là hỏng cả lớp bộ nhớ):**
| Thời điểm | Việc phải làm |
|---|---|
| Kết thúc mỗi kỳ báo cáo | Ghi mục mới vào `01-Nhat-Ky-Chay.md` theo `assets/mau-nhat-ky-chay.md` |
| Phát hiện đơn vị nộp sai/thiếu | Cập nhật `03-Chat-Luong-Du-Lieu-Don-Vi.md` ngay |
| Quyết định khác thông lệ | Ghi `04-Nhat-Ky-Quyet-Dinh.md`, **bắt buộc nêu lý do** |
| Phát hiện lỗi script mới | Cấp mã BUG mới trong `02-So-Dang-Ky-Loi.md` |
| Trả giá vì một sai lầm | Ghi `05-Bai-Hoc.md` kèm dấu hiệu nhận biết sớm |
| Bất kỳ thay đổi trạng thái nào | Cập nhật `TRANG-THAI.md` **ngay trong phiên** |

Ghi cuối phiên là quá muộn — phiên kết thúc thì ngữ cảnh mất. Bộ nhớ cũ không được cập nhật
nguy hiểm hơn không có bộ nhớ, vì nó tạo cảm giác an tâm giả.

**Ghi ở đâu (v3.18):** các tệp `references/Memory/` chỉ được **ghi** khi đang làm việc trong dự án KTC-Quan-tri (thư
mục `25-KTC-Bao-Cao/`). Chạy qua plugin, gói kỹ năng, Cowork, tài khoản thành viên: **không sửa tệp của plugin** (bản
phát hành — sửa sẽ mất khi cập nhật và lệch giữa các máy; guard chặn). Khi đó ghi nhật ký chạy, lỗi dữ liệu đơn vị, lỗi
công cụ vào **tệp ghi chú đối soát** của kỳ trong `30-Ket-Qua/<ngày>/<loại>/` (hoặc nêu trong câu trả lời) để Phòng
TH-HC&QT đưa vào bộ nhớ gốc.

## Báo cáo tháng cấp Trường — QUY TRÌNH CHÍNH (v3.18, bắt buộc)

**Đọc `references/Skill-Library/37-Quy-Trinh-Bao-Cao-Thang-Tu-Ban-Da-Ban-Hanh.md` trước khi làm.** Tóm tắt:

- **Sản phẩm mặc định (4 tệp):** báo cáo Word (kết quả tháng N + nhiệm vụ tháng N+1) · phụ lục kết quả tháng N có công thức
  KPI · kế hoạch công tác tháng N+1 (.xlsx) · ghi chú đối soát (.md). Chỉ được yêu cầu một phần thì làm phần đó và nói rõ
  phần chưa làm.
- **Phát triển từ bản ĐÃ BAN HÀNH** trong kho (báo cáo, phụ lục tháng N−1; kế hoạch tháng N) bằng công cụ
  `references/Skill-Library/bc_thang.py` (`nguon` → `trich` → `word` / `phu-luc` / `ke-hoach`). **Không** dựng từ mẫu trắng
  `00. Mau bao cao thang (cap Truong).docx` / `fill_bc736.py` khi kho có bản đã ban hành.
- **Nguồn nội dung chính là tường thuật Phụ lục IIa của mọi đơn vị** — đọc hết. Đầu mối chưa nộp → tổng hợp từ báo cáo đơn
  vị khác, kế hoạch đã ban hành, Chương trình công tác năm, thông báo kết luận giao ban (tổng hợp có nguồn, không phải suy
  diễn); chỉ ghi `[CẦN BỔ SUNG: …]` khi không có nguồn nào.
- Nguồn từng ý ghi ở **tệp ghi chú đối soát**, không chèn "(Nguồn: …)" vào thân văn bản. Tỷ lệ KPI theo Trục để ở phụ lục,
  không thay tường thuật.
- Dòng sai công thức KPI → chỉ bỏ số KPI của dòng đó; **không loại cả đơn vị**, không tự sửa số liệu đơn vị.
- Công cụ tự kiểm: còn `[CẦN BỔ SUNG`, còn kỳ cũ, vi phạm văn phong, thiếu mục con — phải về 0 hoặc giải trình. Đo thể thức
  mọi tệp; rà soát `ktc-ra-soat-897` trước trình ký.

## Quy trình 7 bước (khung chung — bước 6 theo quy trình chính ở trên)
Xem `references/Workflow/09-Tong-Hop-Bao-Cao.md`:

| Bước | Mô tả | Skill |
|------|-------|-------|
| 0 | Lập Checklist đơn vị đầu kỳ | **Skill 35** |
| 1 | Tiếp nhận hồ sơ đơn vị (IIa tường thuật, IIb/IIc kết quả, Ia/Ib kế hoạch) — `bc_thang.py nguon`, `trich` | — |
| 2 | Kiểm tra đủ mẫu/kỳ, gắn Trục/Nội hàm, kiểm KPI + Ghi chú (lỗi dòng nào bỏ số dòng đó, giữ đơn vị) | **Skill 32** |
| 3 | Tổng hợp cấp Trường — lọc "Đưa vào KH Trường", tính % KPI theo Trục (cho phụ lục) | **Skill 33** |
| 4 | Đối chiếu KH cùng kỳ (fallback A/B/C nếu thiếu) | **Skill 34** |
| 5 | **Rà soát BẮT BUỘC trước khi trình ký** — chốt chặn, không bỏ qua | ktc-ra-soat-897 |
| 6 | Xuất 4 tệp từ bản đã ban hành bằng `bc_thang.py` (mẫu trắng + `fill_bc736.py` chỉ khi kho không có bản đã ban hành) | Skill 37 |
| 7 | Checklist kết thúc kỳ — liệt kê file cần xóa, link output | **Skill 35** |

## 6 Skill chuyên biệt (v3.4)

| Skill | Prompt | Chức năng |
|---|---|---|
| **31**-Skill-Phu-Luc-TB736-Excel | — | [MỚI v3.4] Cấu trúc + công thức KPI 4 Phụ lục Excel — đọc trước Skill 32/33/34 |
| **Skill-Tu-hoc-Phong-Cach-Bao-Cao** | — | Chuẩn phong cách báo cáo cấp cao — 16 nguyên tắc, tự học từ báo cáo tốt |
| **35**-Skill-Quan-Ly-Checklist-Don-Vi | `04-Thu-Thap-Checklist.md` | Tạo/cập nhật/chốt Checklist (4 tác vụ A/B/C/D) |
| **32**-Skill-Thu-Thap-Bao-Cao-Don-Vi | `01-Thu-Thap-Kiem-Tra.md` | Kiểm tra báo cáo đơn vị đủ mẫu TB736, gắn Trục/Nội hàm, **kiểm công thức KPI** |
| **33**-Skill-Tong-Hop-Bao-Cao-Truong | `02-Tong-Hop-Cap-Truong.md` | Gộp nhiều đơn vị, chiếu Checklist, xử lý trùng lặp, **tính % KPI theo Trục** |
| **34**-Skill-Doi-Chieu-Tien-Do-KH | `03-Doi-Chieu-Tien-Do.md` | Đối chiếu KH — fallback A/B/C, dùng % KPI làm chỉ số khách quan |
| **37**-Quy-Trinh-Bao-Cao-Thang-Tu-Ban-Da-Ban-Hanh | — | **Quy trình chính báo cáo tháng cấp Trường** — 4 sản phẩm từ bản đã ban hành, công cụ `bc_thang.py` |

Cả 4 Skill nghiệp vụ dùng `30-Skill-Phan-Loai-6-Truc.md` (38 nội hàm, TB 817).

## [MỚI v3.4] Công cụ Python — tự động hóa xuất báo cáo Word

| Script | Chức năng |
|---|---|
| `bc_thang.py` | **Công cụ chính (v3.18):** tìm bản đã ban hành, trích IIa/IIb/Ib, dựng báo cáo Word, phụ lục KPI, kế hoạch tháng sau từ bản đã ban hành, tự kiểm (kèm `vanphong.py`, `trich_tuong_thuat.py`, `duong_dan.py`) |
| `read_bc736_excel.py` | Đọc Excel Phụ lục, kiểm KPI cascade, lọc "Đưa vào KH Trường", tổng hợp % theo Trục, dựng khung `content_map` nháp |
| `fill_bc736.py` | **Dự phòng** — chỉ khi kho không có báo cáo tháng đã ban hành: điền mẫu trắng TB736 từ `content_map` |
| `README-fill_bc736.md` | 22 khóa nội dung Phần I/III của báo cáo Word theo 6 Trục |

Quy trình dùng: `bc_thang.py nguon` → `trich` → soạn nội dung JSON (văn phong cấp Trường, Skill-Tu-hoc) → `bc_thang.py word`, `phu-luc`, `ke-hoach` → `kiem_the_thuc.py` → rà soát 897. `read_bc736_excel.py` dùng để kiểm KPI cascade, tính % theo Trục cho phụ lục.

## Chuẩn phong cách — BẮT BUỘC đọc trước Bước 3 và Bước 6
`references/Skill-Library/Skill-Tu-hoc-Phong-Cach-Bao-Cao.md` — 16 phần, học từ báo cáo UBND tỉnh Quảng Ngãi và Trường CĐKT.

## Điều kiện Skill 34 — fallback v2.0
Nếu không có KH cùng kỳ, hỏi người dùng:
- **[A]** Cung cấp file KH ngay → tiếp tục bình thường
- **[B]** Xuất báo cáo thô + cảnh báo nổi bật
- **[C]** Dừng chờ hệ `ktc-ke-hoach` (PIS)

## Ghi chú hợp lệ trong KH tháng (điều chỉnh HT)
Cột Ghi chú (11) trong Phụ lục Ia/Ib ghi "Bổ sung ngoài KH quý" hoặc "Kết luận giao ban" = **phát sinh hợp lệ**, KHÔNG phải lỗi. Riêng giá trị chuẩn "Đưa vào KH Trường" / "Thường xuyên của đơn vị" dùng để lọc phạm vi báo cáo Trường (xem Skill 31/33).


## Quan hệ bắt buộc với `ktc-ra-soat-897`

**897 là chốt chặn bắt buộc, không phải bước tùy chọn.** Hai chiều sử dụng:

| Khi nào | Dùng gì của 897 |
|---|---|
| **Ngay từ lúc bắt đầu viết** (Bước 3, Bước 6) | `Checklist/07-Theo-Loai-Van-Ban.md` — checklist riêng cho Báo cáo · `Checklist/04-Ngon-Ngu.md` — chuẩn hóa từ ngữ · `Checklist/08-Quy-Uoc-Rieng-CDKT.md` — tên đơn vị chuẩn, thông số thể thức |
| **Tự chấm dự thảo trước khi trình** | `Skill-Library/19-Skill-Danh-Gia-Chat-Luong-Van-Ban.md` |
| **Trước khi trình ký** (Bước 5) | Toàn bộ quy trình rà soát 897. Còn vấn đề **Mức 1 (bắt buộc sửa)** thì **không được trình** |

Áp dụng sớm rẻ hơn sửa muộn. Hệ này **không** giữ bản sao bộ quy tắc của 897 — trỏ tới bản gốc, vì bản sao
không có cơ chế đồng bộ chắc chắn sẽ lệch.

## Giới hạn
- Không soạn thảo văn bản hành chính → `ktc-soan-thao-vb`; không rà soát chính thức → `ktc-ra-soat-897`
- Không tự đánh giá "tốt/chưa tốt" — báo tỷ lệ/% KPI để người thẩm quyền đánh giá
- Không tự sửa số liệu KPI dù phát hiện sai công thức — chỉ nêu giá trị đúng để đơn vị điều chỉnh
- Không tự xóa file Drive — liệt kê để người dùng xóa thủ công
