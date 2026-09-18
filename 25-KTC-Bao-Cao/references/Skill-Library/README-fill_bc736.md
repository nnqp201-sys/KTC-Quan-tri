# fill_bc736.py — Công cụ điền mẫu Báo cáo tháng cấp Trường (TB736)
## Cập nhật 19/08/2026 (v3.2) — GHÉP với bản vá độc lập, xem PATCH-NOTES-v3.2.md

## ⚠️ LỖI ĐÃ PHÁT HIỆN VÀ SỬA (đọc trước khi dùng)

Đối chiếu với file mẫu Word thật (`00. Mau bao cao thang (cap Truong).docx` do Anh Phục cung cấp
18/08/2026), phát hiện: nhiều đoạn bôi vàng trong mẫu **giống hệt nhau về text** dù nằm ở
vị trí khác nhau — ví dụ "công tác tuyển sinh...phòng QLĐT&BĐCL" xuất hiện **y hệt** ở cả
Phần I (kết quả) lẫn Phần III (kế hoạch); cả **8 Nghị quyết Bộ Chính trị** dùng chung 1 đoạn
bôi vàng. Bản `fill_bc736.py` cũ dùng 1 `content_map` chung khớp theo text bôi vàng — nên
**nội dung Phần I có thể bị chèn nhầm sang Phần III, và 8 Nghị quyết nhận cùng 1 nội dung.**

**Đã sửa:** khóa khớp giờ là `(PHẦN, NHÃN)` — đã kiểm chứng cho 45/45 vị trí trong mẫu thật
đều duy nhất, không còn trùng lặp. Xem chi tiết `31-Skill-Phu-Luc-TB736-Excel.md` mục nhật ký sửa lỗi
và code trong `fill_bc736.py`.

## Nguyên tắc màu sắc trong mẫu (Trường quy định)
- **Chữ màu đỏ (EE0000)**: toàn bộ là hướng dẫn/yêu cầu định dạng — không phải nội dung báo cáo.
- **Bôi vàng**: thẻ đánh dấu "loại nội dung cần lấy + đơn vị chủ trì".
- Câu `{Lưu ý nguyên tắc: chuyển văn phong từ Phòng sang Trường...}` là hướng dẫn viết văn phong.

## ⚠️ Nguyên tắc chủ thể — BẮT BUỘC đọc trước khi viết nội dung

Đây là báo cáo **cấp Trường** gửi UBND tỉnh — chủ thể mọi câu PHẢI là **"Nhà trường"**, không phải
tên Phòng/Khoa. Chi tiết: `Skill-Tu-hoc-Phong-Cach-Bao-Cao.md` Mục 0.

| SAI | ĐÚNG |
|---|---|
| "Phòng QLĐT&BĐCL tổ chức thi..." | "Nhà trường tổ chức thi..." |

## Cách dùng (API MỚI — content_by_phase, KHÔNG còn content_map đơn)

```python
from fill_bc736 import fill_report

content_by_phase = {
    "PHAN_I": {
        # Nội dung KẾT QUẢ đã qua (VD tháng 7) — 27 vị trí, xem danh sách bên dưới
        "Công tác tuyển sinh": "Nhà trường tổ chức công bố danh sách trúng tuyển đợt 1...",
        "Nghị quyết số 59-NQ/TW": "Nhà trường tổ chức quán triệt nội dung Nghị quyết...",
        # ... (không cần liệt kê đủ 27, thiếu thì tự đánh dấu [CẦN BỔ SUNG])
    },
    "PHAN_II": {
        # 2 vị trí: Đánh giá chung
        "kết quả đạt được": "...",
        "tồn tại, hạn chế": "...",
    },
    "PHAN_III": {
        # Nội dung KẾ HOẠCH tháng tới (VD tháng 8) — 16 vị trí, xem danh sách bên dưới
        # LƯU Ý: PHẢI viết nội dung KHÁC với PHAN_I dù nhãn trùng tên (VD "Công tác tuyển sinh")
        "Công tác tuyển sinh": "Nhà trường tiếp tục triển khai kế hoạch tuyển sinh đợt 2...",
    },
}

result = fill_report(
    template_path="00__Mau_bao_cao_thang__cap_Truong_.docx",
    output_path="BC_thang_X_2026.docx",
    content_by_phase=content_by_phase,
    thang_ket_qua=7, thang_ke_hoach=8, nam=2026,
)
print(result["filled"], "đoạn đã điền —", result["missing"], "đoạn còn thiếu")
for phase, label in result["missing_list"]:
    print(f"  Thiếu: [{phase}] {label}")
```

## Cơ chế khớp nhãn — quan trọng để viết đúng khóa
- Khóa (`"Công tác tuyển sinh"`, v.v.) chỉ cần khớp GẦN ĐÚNG (so khớp 2 chiều, không phân biệt hoa/thường,
  bỏ dấu `*`, `.`, `:`) với nhãn tiêu đề thật trong mẫu — không cần chép chính xác từng ký tự.
- Với các mục KHÔNG có nhãn cùng đoạn (VD Trục 3, Mục 6 Phần III), hệ tự dùng **tiêu đề đậm gần nhất phía trước**
  làm nhãn — chỉ cần khóa của bạn chứa một phần tiêu đề đó là khớp được.
- Mỗi Phần (`PHAN_I` / `PHAN_II` / `PHAN_III`) có không gian khóa **độc lập hoàn toàn** — dùng cùng tên khóa
  ở 2 Phần khác nhau (VD "Công tác tuyển sinh") là AN TOÀN, sẽ điền đúng vào đúng chỗ, không đụng nhau.

## Danh sách đầy đủ 45 vị trí thật trong mẫu (đã trích xuất và kiểm chứng 18/08/2026)

### PHẦN I — Kết quả thực hiện (27 vị trí)
Trục 1 (6): Công tác tuyển sinh · Công tác đào tạo · Công tác khảo thí · Công tác bảo đảm chất lượng ·
Công tác kế hoạch, tổng hợp · Công tác tổ chức, cán bộ

Trục 2 (2): Về thể chế · Công tác Kiểm tra, giám sát

Trục 3 (1): Thúc đẩy phát triển KH-CN, đổi mới sáng tạo và chuyển đổi số

Trục 4 (3): Công tác xây dựng Đảng · Chấp hành kỷ cương hành chính (bổ sung ngoài đoạn cố định) ·
Công tác Đảng, Công đoàn, Đoàn Thanh niên

Trục 5 (4): Công tác quản lý cơ sở vật chất · Công tác Tài chính · Công tác an sinh giáo dục ·
Công tác truyền thông

Trục 6 (3): Về Quốc phòng - An ninh · Về hoạt động Đối ngoại và Hợp tác · Về hoạt động hợp tác phát triển

Mục 7 — Nghị quyết Bộ Chính trị (8, PHÂN BIỆT ĐƯỢC theo tiêu đề riêng từng NQ):
Nghị quyết số 59-NQ/TW · 66-NQ/TW · 68-NQ/TW · 79-NQ/TW · 70-NQ/TW · 71-NQ/TW · 72-NQ/TW · 80-NQ/TW

### PHẦN II — Đánh giá chung (2 vị trí)
kết quả đạt được · tồn tại, hạn chế

### PHẦN III — Nhiệm vụ trọng tâm tháng tới (16 vị trí — LƯU Ý: khác cấu trúc Phần I)
Trục 1 (6): Công tác tuyển sinh · Công tác đào tạo · Công tác khảo thí · Công tác bảo đảm chất lượng ·
Công tác kế hoạch, tổng hợp · Công tác tổ chức, cán bộ

Trục 2 (2): Về thể chế · Công tác Kiểm tra, giám sát

Trục 3 (1): Thúc đẩy phát triển KH-CN, đổi mới sáng tạo và chuyển đổi số

Trục 4 (2): Công tác xây dựng Đảng · Công tác Công đoàn, Đoàn Thanh niên
*(khác Phần I: không có mục "Chấp hành kỷ cương hành chính" riêng, tên mục 2 hơi khác — "Công tác Công đoàn,
Đoàn Thanh niên" thay vì "Công tác Đảng, Công đoàn, Đoàn Thanh niên")*

Trục 5 (4): Công tác Quản lý cơ sở vật chất · Công tác Tài chính · Về công tác an sinh, giáo dục ·
Về công tác Truyền thông

Trục 6 (1): **CHỈ 1 vị trí gộp chung** — "6. Củng cố quốc phòng, an ninh..." — khác Phần I có 3 vị trí riêng
(quốc phòng-an ninh / đối ngoại / hợp tác phát triển). Khi viết nội dung Phần III Trục 6, nên gộp cả 3 chủ đề
vào 1 đoạn nếu có đủ dữ liệu, hoặc chỉ viết chủ đề nào có dữ liệu.

**Phần III KHÔNG có Mục 7 (Nghị quyết Bộ Chính trị)** — mục này chỉ xuất hiện ở Phần I.

## 3 loại đoạn được xử lý khác nhau trong code
1. **Nội dung báo cáo** (bôi vàng, khớp theo Phần+nhãn) → điền hoặc `[CẦN BỔ SUNG [PHAN_X] nhãn]`.
2. **Câu kỳ báo cáo** ("tháng […] năm 20[…]" không bôi vàng) → tự động điền số tháng/năm thật.
3. **Số hiệu văn bản / ngày ký** (bảng quốc hiệu) → **giữ nguyên**, do Văn thư điền khi phát hành.

## Quy trình khuyến nghị hàng tháng
1. Skill 32 kiểm tra báo cáo từng đơn vị (Excel Phụ lục Ia/Ib/IIb/IIc).
2. Skill 33 tổng hợp, lọc "Đưa vào KH Trường", tính % KPI theo Trục, chuyển văn phong cấp Trường
   (chủ thể "Nhà trường") — **soạn RIÊNG nội dung cho Phần I (kết quả) và Phần III (kế hoạch)**,
   không dùng chung 1 đoạn cho cả 2 dù chủ đề giống nhau.
3. Dựng `content_by_phase` theo 3 khóa PHAN_I/PHAN_II/PHAN_III, chạy `fill_report()`.
4. Kiểm tra file `.docx` xuất ra bằng LibreOffice trước khi trình ký — rà lại chủ thể từng câu
   VÀ xác nhận Phần I/Phần III không bị lẫn nội dung của nhau.
5. Đoạn nào còn `[CẦN BỔ SUNG]` → báo lại đơn vị phụ trách, KHÔNG tự viết thay.

## Lịch sử
- 17/08/2026: Tạo lần đầu, dùng content_map đơn (có lỗi tiềm ẩn chưa phát hiện).
- 18/08/2026 (sáng): Sửa lỗi chủ thể "Phòng X" → "Nhà trường".
- 18/08/2026 (chiều): **Phát hiện và sửa lỗi nghiêm trọng** — content_map đơn gây trùng khóa
  giữa Phần I/III và giữa 8 Nghị quyết. Đổi sang `content_by_phase` (3 khóa con), khớp theo
  (Phần, nhãn). Đã kiểm chứng 45/45 vị trí duy nhất trên file mẫu thật.
