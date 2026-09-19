---
name: ktc-bao-cao
description: "Thu thap, tong hop, xay dung bao cao cong tac thang/quy/6-thang/nam cua Truong Cao dang Kon Tum tu bao cao Excel Phu luc TB736 (Ia/Ib/IIb/IIc) cua cac Phong/Khoa/Trung tam, theo cau truc 6 Truc ket qua trong tam (TB 817/TB-CDKT) va he thong KPI 3 chieu (so luong/chat luong/tien do). Quan ly checklist don vi (Skill 35), kiem tra bao cao don vi + cong thuc KPI (Skill 32), tong hop cap Truong theo chuan phong cach cao cap + tinh % KPI theo Truc (Skill 33 + Skill-Tu-hoc), doi chieu tien do voi Ke hoach cung ky (Skill 34 — co nhanh fallback A/B/C khi thieu KH). Tu dong dien mau bao cao Word TB736 cap Truong tu du lieu Excel that (fill_bc736.py + read_bc736_excel.py). Day la He KTC Report Intelligence System (KTC-RIS) v3.4. KHONG dung de soan van ban hanh chinh thong thuong hoac ra soat - dung ktc-soan-thao-vb hoac ktc-ra-soat-897 cho viec do."
---

# KTC-Bao-Cao / KTC-RIS v3.13

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

## Quy trình 7 bước
Xem `references/Workflow/09-Tong-Hop-Bao-Cao.md`:

| Bước | Mô tả | Skill |
|------|-------|-------|
| 0 | Lập Checklist đơn vị đầu kỳ | **Skill 35** |
| 1 | Tiếp nhận Excel Phụ lục từ đơn vị | — |
| 2 | Kiểm tra đủ mẫu/kỳ, gắn Trục/Nội hàm, kiểm KPI + Ghi chú | **Skill 32** |
| 3 | Tổng hợp cấp Trường — lọc "Đưa vào KH Trường", tính % KPI theo Trục | **Skill 33** |
| 4 | Đối chiếu KH cùng kỳ (fallback A/B/C nếu thiếu) | **Skill 34** |
| 5 | **Rà soát BẮT BUỘC trước khi trình ký** — chốt chặn, không bỏ qua | ktc-ra-soat-897 |
| 6 | Xuất .docx qua `fill_bc736.py`, kèm 3 trường trách nhiệm | Nguyên tắc 2 |
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

Cả 4 Skill nghiệp vụ dùng `30-Skill-Phan-Loai-6-Truc.md` (38 nội hàm, TB 817).

## [MỚI v3.4] Công cụ Python — tự động hóa xuất báo cáo Word

| Script | Chức năng |
|---|---|
| `read_bc736_excel.py` | Đọc Excel Phụ lục, kiểm KPI cascade, lọc "Đưa vào KH Trường", tổng hợp % theo Trục, dựng khung `content_map` nháp |
| `fill_bc736.py` | Điền mẫu Word TB736 cấp Trường từ `content_map`, giữ nguyên 100% định dạng gốc (quốc hiệu, chữ ký) |
| `README-fill_bc736.md` | 22 khóa nội dung Phần I/III của báo cáo Word theo 6 Trục |

Quy trình dùng: `read_bc736_excel.py` (dựng khung nháp từ Excel thật) → biên tập văn phong cấp Trường (Skill-Tu-hoc) → `fill_bc736.py` (điền vào mẫu Word) → kiểm tra bằng LibreOffice trước khi trình ký.

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
