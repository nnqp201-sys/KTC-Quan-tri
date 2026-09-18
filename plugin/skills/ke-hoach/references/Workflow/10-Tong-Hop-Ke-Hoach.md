# 10-Tong-Hop-Ke-Hoach (Workflow của KTC-Ke-Hoach / KTC-PIS)
**Phiên bản: 3.1 — 14/9/2026**

## Điều kiện tiên quyết
- Đọc `references/Skill-Library/00-Nguyen-Tac-Chung.md`
- Đọc `references/Skill-Library/34-Skill-Nhan-Ke-Hoach-Preflight.md`
- Xác nhận Google Drive connector đang hoạt động

## 7 Bước thực hiện

### Bước 0 — Pre-flight Check *(BẮT BUỘC — có quyền CHẶN toàn bộ)*
**Skill:** 34 | **Prompt:** `00-Preflight-Check.md`

Kiểm tra 4 điều kiện:
1. Đủ đơn vị nộp file vào đúng thư mục (13 đơn vị kỳ định kỳ; `KH-Truong/` bắt buộc kỳ chuyên đề)
2. Tên file đúng quy ước Luồng A/B/C và đúng định dạng `.docx`/`.xlsx`
3. Có KH cấp trên trong `KH-Cap-Tren/` đúng phạm vi kỳ (bắt buộc khi lập tháng/quý)
4. Kết nối kho 01-04 hoạt động

**Ba trạng thái:**
- ✅ **PASS** → chạy Bước 1
- ⚠️ **PASS-PARTIAL** (≤3 đơn vị thiếu, người có thẩm quyền xác nhận) → ghi "kết quả sơ bộ"
- ❌ **FAIL** → **DỪNG TOÀN BỘ**

### Bước 1 — Thu thập đề xuất
- Luồng A: `11-Du-Lieu-Dau-Vao/01-Dau-Moi-Nop/<kỳ>/<mã>/DX_[kỳ]_[kỳ-cụ-thể]_[mã]_v[N].docx`
- Luồng B: `11-Du-Lieu-Dau-Vao/02-Cap-Truong/<kỳ>/` hoặc `04-Van-Ban-Cap-Tren/<năm>/` — `KH_[kỳ]_[kỳ-cụ-thể]_[Don-vi]_[So-hieu].docx`
- Luồng C: tên Luồng B + `_HOITRO`
- Chỉ chấp nhận `.docx` và `.xlsx`.

### Bước 2 — Kiểm tra đề xuất đơn vị
**Skill:** 35 | **Prompt:** `01-Thu-Thap-Kiem-Tra.md`
- Kiểm tra đủ cột mẫu TB736 (Phụ lục Ia/Ib)
- Gắn đúng Trục (1-6) + Nội hàm (dùng `30-Skill-Phan-Loai-6-Truc.md`)
- Kiểm tra phù hợp kỳ
- Thiếu chỉ tiêu → [CẦN BỔ SUNG] | Mô tả mơ hồ → [CẦN XÁC ĐỊNH LẠI]

### Bước 3 — Tổng hợp cấp Trường
**Skill:** 36 | **Prompt:** `02-Tong-Hop-Cap-Truong.md`

**[SỬA v3.1] Nguồn khác nhau theo loại kỳ** (Skill 36 BƯỚC 0):

| Kỳ | Nguồn |
|---|---|
| **Quý / Năm** | Gộp đề xuất đơn vị (Bước 2) + nhiệm vụ cấp trên giao + chiến lược, đề án |
| **Tháng** | **Trích từ Kế hoạch quý đã ban hành** (nhiệm vụ đến hạn trong tháng) + nhiệm vụ phát sinh. **Không gộp lại từ kế hoạch tháng của đơn vị** |

Đo trên bản đã ban hành: phụ lục tháng 7 khớp Kế hoạch quý III **39/41 = 95%**; `KH-834` có **53** nhiệm vụ
trong khi gộp từ 13 đơn vị cho **94**. Làm từ dưới lên sẽ đẩy việc thường xuyên của đơn vị lên cấp Trường.

- Chỉ giữ nhiệm vụ do **lãnh đạo cấp Trường** trực tiếp chỉ đạo (Hiệu trưởng, Phó Hiệu trưởng, Bí thư/Phó Bí thư Đảng ủy, Chủ tịch Công đoàn, Bí thư ĐTN, Chủ tịch HSV) — kiểm chứng 100% trên `PL-375` và `KH-834`.
- Nhóm theo 6 Trục → trong Trục theo Nội hàm **theo TB 817** (không theo tên trục trong file danh mục Excel — hai nguồn đang lệch, xem `KI-011`).
- Chồng chéo → [CẦN XÁC ĐỊNH ĐƠN VỊ CHỦ TRÌ]
- Lỗi dữ liệu đơn vị → ghi vào cột **Ghi chú**, **không tự sửa**.

### Bước 4 — Đối chiếu phân cấp thời gian
**Skill:** 37 | **Prompt:** `03-Doi-Chieu-Phan-Cap.md`
**Điều kiện:** Phải có KH cấp trên. Nếu thiếu → DỪNG Bước 4, ghi chú, tiếp tục Bước 5+6.
- Nhiệm vụ KH cấp trên chưa phân bổ vào kỳ nhỏ → ghi nhận
- Nhiệm vụ kỳ nhỏ không có trong KH cấp trên → "Phát sinh ngoài KH cấp trên"

### Bước 5 — Rà soát BẮT BUỘC trước khi trình ký
Dùng hệ `ktc-ra-soat-897`. **Đây là chốt chặn, không phải bước tùy chọn.** Còn vấn đề **Mức 1 (bắt buộc
sửa)** thì không được trình.

Bộ quy tắc của 897 còn phải dùng **ngay từ Bước 2 và Bước 3** khi đang lập kế hoạch — `Checklist/07-Theo-Loai-Van-Ban.md`
có checklist riêng cho Kế hoạch, `Checklist/08-Quy-Uoc-Rieng-CDKT.md` có tên đơn vị chuẩn và thông số thể thức.

### Bước 6 — Xuất và lưu kết quả
- Lưu vào: `12-Output/YYYY-MM-DD/<loại thao tác>/KH_[kỳ]_[kỳ-cụ-thể]_Truong-CDKT_[ngay-tao].docx`
- Ghi đủ 3 trường trách nhiệm: Nguồn dữ liệu đã dùng / Người kiểm tra / Trạng thái phê duyệt

## Outputs
- Kế hoạch tổng hợp cấp Trường (chính)
- Bảng đối chiếu phân cấp thời gian (nếu có KH cấp trên)
- Phụ lục vấn đề cần xác nhận (chồng chéo, thiếu chỉ tiêu, phát sinh ngoài KH cấp trên)
- **[v3.1]** Danh sách lỗi dữ liệu đơn vị đã ghi vào cột Ghi chú (không tự sửa)

## Cấu trúc thư mục (tham chiếu nhanh)
```
11-Du-Lieu-Dau-Vao/          ← kho dùng chung cấp dự án (từ 14/9/2026)
  01-Dau-Moi-Nop/<kỳ>/<mã>/  ← hồ sơ 13 đầu mối nộp; chỉ tạo khi có dữ liệu
  02-Cap-Truong/<kỳ>/        ← văn bản cấp Trường đã ban hành
  03-Ket-Luan-Giao-Ban/<năm>/← kết luận giao ban tuần (nguồn 3)
  04-Van-Ban-Cap-Tren/<năm>/ ← văn bản chỉ đạo cấp trên (nguồn 2)
  09-Chua-Phan-Loai/

12-Output/YYYY-MM-DD/<loại thao tác>/   ← nơi xuất DUY NHẤT của toàn dự án
                                          (Xuat_Ke_Hoach/ đã bỏ 14/9/2026)
```

## Liên kết với KTC-Bao-Cao (RIS)
`12-Output/YYYY-MM-DD/` là căn cứ chính thức cho `ktc-bao-cao` đối chiếu tiến độ — 2 hệ khép vòng Kế hoạch ↔ Báo cáo.
