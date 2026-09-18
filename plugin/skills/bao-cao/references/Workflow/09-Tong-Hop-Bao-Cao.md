# 09-Tong-Hop-Bao-Cao (Workflow của KTC-Bao-Cao/RIS)
## Phiên bản: v2.5 — cập nhật 14/9/2026

## Steps

0. **Lập danh sách kiểm soát đơn vị (Skill 35)** — trước khi mở cổng tiếp nhận:
   - Xác định N đơn vị bắt buộc nộp kỳ này. Ghi rõ deadline và kỳ báo cáo.
   - Tạo Checklist trạng thái: Chưa nộp / Đã nộp / Đã kiểm tra / Vấn đề.
   - Output: `Checklist-Don-Vi-[Ky]-[YYYY-MM-DD].md` → `12-Output/[YYYY-MM-DD]/checklist/`.

1. **[SỬA v2.5]** Các đơn vị nộp **HAI tệp**, thiếu một là **nộp thiếu**:
   - `.docx` — **Phụ lục IIa**, báo cáo tường thuật. **Nguồn duy nhất của văn phong** cho Phần I/II/III.
   - `.xlsx` — **Phụ lục Ia/Ib** (kế hoạch) hoặc **IIb/IIc** (kết quả), đúng mẫu TB736 (xem `31-Skill-Phu-Luc-TB736-Excel.md`). Nguồn số liệu và KPI.

   Nộp vào `13-Unit-Reports`. Cập nhật Checklist → "Đã nộp" **chỉ khi đủ cả hai**.
   *Vẫn giữ:* không nhận bảng nhiệm vụ ở dạng văn xuôi thay cho Excel Phụ lục.
   *Tiền lệ:* kỳ tháng 8/2026 đợt đầu chỉ đọc `.xlsx` → bỏ sót 198 ý kết quả và 130 ý kế hoạch.

2. Skill 32 kiểm tra đủ mẫu/đủ kỳ, gắn Trục/Nội hàm, **kiểm tra công thức KPI cascade** (chỉ IIb/IIc) và **cột Ghi chú** (chỉ Ia/Ib). Cập nhật Checklist → "Đã kiểm tra" hoặc "Vấn đề: [mô tả]".

3. **[SỬA v2.5]** Skill 33 dựng **hai sản phẩm, hai nguồn khác nhau** (Skill 33 BƯỚC 0A):
   - **Phần tường thuật** ← Phụ lục IIa `.docx` của đơn vị; dùng **danh mục mục con cố định** (BƯỚC 0B), không tự sinh nhãn.
   - **Phụ lục kết quả** ← **Kế hoạch công tác tháng của chính Trường**, dùng IIb của đơn vị để điền kết quả/KPI. **Không gộp toàn bộ nhiệm vụ đơn vị** — cách cũ cho 211 nhiệm vụ so với 39 của bản đã ban hành.
   - Chỉ giữ nhiệm vụ do **lãnh đạo cấp Trường** trực tiếp chỉ đạo.

   Kèm phát hiện trùng lặp/mâu thuẫn, **lọc theo Ghi chú "Đưa vào KH Trường"**, **tính % KPI 3 chiều cấp Trường theo Trục**. Chiếu Checklist để ghi đơn vị chưa nộp. **⚠️ Bước 0 của Skill 33: xác định đây là báo cáo cấp Trường → chủ thể "Nhà trường" xuyên suốt (xem Skill-Tu-hoc Mục 0).**

4. Skill 34 đối chiếu với Kế hoạch cùng kỳ:
   - **Có KH**: đối chiếu đầy đủ + dùng % KPI 3 chiều (Skill 33 tính) làm chỉ số khách quan. Ghi chú "Bổ sung ngoài KH quý" / "Kết luận giao ban" = phát sinh hợp lệ.
   - **Không có KH**: hỏi người dùng A/B/C (xem `34-Skill-Doi-Chieu-Tien-Do-KH.md`).

5. **[SỬA v2.5] Rà soát BẮT BUỘC trước khi trình ký** bằng `ktc-ra-soat-897` — đây là chốt chặn, không
   phải bước tùy chọn. Còn vấn đề **Mức 1 (bắt buộc sửa)** thì không được trình. Ngoài ra, bộ quy tắc của
   897 phải được dùng **ngay từ Bước 3 và Bước 6** khi đang viết, không đợi tới đây (nguyên tắc NT-3).

6. Xuất .docx cấp Trường bằng `fill_bc736.py`:
   - Dựng khung nháp `content_map` từ Excel IIb/IIc qua `build_content_map_skeleton()` (`read_bc736_excel.py`).
   - Biên tập lại văn phong cấp Trường (Skill-Tu-hoc) cho từng khóa trong 22 khóa (`README-fill_bc736.md`).
   - **⚠️ Kiểm tra bắt buộc: chủ thể mọi câu phải là "Nhà trường", không phải tên Phòng/Khoa (xem Skill-Tu-hoc Mục 0). Đọc lại từng đoạn trước khi đưa vào content_map.**
   - **[v2.5]** Ưu tiên **phát triển từ chính báo cáo tháng gần nhất đã ban hành** thay vì mẫu trống — thể thức khớp tuyệt đối mà không phải chỉnh tay.
   - **[v2.5]** Mỗi đoạn nội dung gồm **HAI run**: nhãn `* Công tác …:` đậm nghiêng, nội dung **để thường** (đặt tường minh `w:b`/`w:i` = `0`). Gộp một run làm cả đoạn đậm nghiêng. Mục II không có dấu `*`.
   - Gọi `fill_report()` để điền vào mẫu Word, giữ nguyên định dạng gốc.
   - Lưu vào `12-Output/YYYY-MM-DD/`, kèm 3 trường trách nhiệm (Nguồn dữ liệu / Người kiểm tra / Trạng thái phê duyệt).

7. **Checklist kết thúc kỳ**:
   - Liệt kê file gốc trong `11-Input` / `13-Unit-Reports` cần xóa thủ công.
   - Cập nhật Checklist → "Hoàn tất kỳ [tháng/quý/năm]".
   - Thông báo link output: Báo cáo + Bảng % KPI theo Trục + Phụ lục + Checklist.

## Outputs
- Báo cáo tổng hợp cấp Trường (.docx, đúng mẫu TB736)
- Bảng % KPI hoàn thành theo 6 Trục (3 chiều: số lượng/chất lượng/tiến độ)
- Bảng đối chiếu tiến độ theo 6 Trục
- Phụ lục A/B/C vấn đề cần xác nhận
- Checklist-Don-Vi-[Ky] trạng thái cuối kỳ

## Quan hệ với các hệ khác
- `ktc-database`: điều kiện tiên quyết — kho 01-04 phải truy cập được trước mọi bước.
- `ktc-ke-hoach (PIS)`: Skill 34 phụ thuộc — nếu PIS chưa tạo KH cùng kỳ, áp dụng fallback A/B/C.
- `ktc-ra-soat-897`: dùng tại Bước 5 khi cần trình ký chính thức.

## Công cụ Python (Skill-Library)
- `read_bc736_excel.py` — đọc Excel Phụ lục, kiểm KPI, lọc Ghi chú, tổng hợp %, dựng khung content_map.
- `fill_bc736.py` — điền mẫu Word TB736 cấp Trường, giữ nguyên định dạng gốc.
