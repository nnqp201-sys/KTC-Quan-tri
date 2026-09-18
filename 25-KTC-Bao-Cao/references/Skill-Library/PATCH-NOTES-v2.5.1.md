# PATCH-NOTES v2.5.1 — Vá lỗi script KTC-RIS
## Ngày vá: 19/08/2026 | Phạm vi: `read_bc736_excel.py`, `fill_bc736.py`
Bản sao lưu bản cũ: `read_bc736_excel.py.v2.3.bak`, `fill_bc736.py.v2.3.bak`

## Vì sao có bản vá này
Kiểm thử sâu bằng 5 fixture Excel + 1 fixture Word mô phỏng đúng cấu trúc TB736
(gồm các tình huống biên có thật) cho thấy script v2.3 **âm thầm trả về kết quả sai**
mà không báo lỗi — nguy hiểm nhất là 3 lỗi khiến báo cáo cấp Trường sai số liệu
hoặc mất nội dung mà người tổng hợp không hề biết.

---

## A. `read_bc736_excel.py` — 9 lỗi

| Mã | Mức | Lỗi | Hậu quả thực tế | Cách vá |
|---|---|---|---|---|
| BUG-01 | **Nghiêm trọng** | `_detect_kind()` chỉ đọc đúng 1 hàng chứa "TT". Chữ "KPI" trong mẫu thật nằm ở **hàng gộp (merged) phía trên** | `kind=None` → toàn bộ nhánh KQ không chạy → **không đọc được KPI nào**, `summarize_truc_kpi()` trả 0, `filter_truong_level()` báo lỗi | Quét cửa sổ 3 hàng (2 hàng trên + hàng TT); thêm nhánh dự phòng theo số cột (≥15 = KQ, 10-12 = KH) kèm cảnh báo |
| BUG-02 | **Nghiêm trọng** | Regex nhận diện Trục bắt buộc có **số thứ tự dẫn đầu** (`1. Trục 1`). Mẫu thật thường ghi thẳng `Trục 1.` | Không nhận ra Trục nào → `current_truc=None` → **bỏ toàn bộ nhiệm vụ, trả về 0 dòng, không báo lỗi** | Regex mới cho số thứ tự tuỳ chọn, chấp nhận `Trục 1` / `1) Trục (1)` / `TRỤC 1 -`; dò cả cột 0 và cột 1 |
| BUG-03 | **Nghiêm trọng** | Dòng "Tổng cộng Trục N" bị đọc **thành một nhiệm vụ** | Cộng dồn KPI **gấp đôi** → % hoàn thành sai toàn bộ báo cáo | Hàm `_is_sum_row()` tách riêng dòng Tổng, không tính vào danh sách nhiệm vụ |
| BUG-04 | Cao | `truc_tong` lấy số liệu từ chính **dòng tiêu đề Trục** (vốn rỗng) thay vì dòng SUM | `truc_tong` luôn rỗng, mất số liệu đối chiếu cho Skill 34 | Lấy đúng từ dòng Tổng; thêm đối chiếu dòng Tổng với tổng tính lại, lệch thì cảnh báo (không tự sửa) |
| BUG-05 | Cao | Đọc được 0 dòng vẫn trả về "thành công", không cảnh báo | Người tổng hợp tưởng đơn vị không có nhiệm vụ | Thêm cảnh báo `[DỪNG]` khi `so_nhiem_vu = 0` và khi `kind=None` |
| BUG-06 | Cao | Chỉ kiểm công thức cột (9) Hệ số | Sai ở (10), (12), (14), (16) lọt hết | Kiểm **toàn bộ chuỗi cascade**: (9),(10),(12),(14),(16) + cảnh báo khi KPI thực tế > số lượng kế hoạch |
| BUG-07 | Trung bình | Cảnh báo "Ghi chú lạ" với `Bổ sung ngoài KH quý` / `Kết luận giao ban` — **trái với SKILL.md** (đây là phát sinh hợp lệ) | Nhiễu cảnh báo giả, lâu dần bị bỏ qua cả cảnh báo thật | Bổ sung 4 giá trị hợp lệ; thêm cảnh báo riêng khi **để trống** Ghi chú |
| BUG-08 | Trung bình | `filter_truong_level()` so khớp **tuyệt đối** chuỗi | Ghi chú thừa dấu cách/khác hoa-thường → **bị loại khỏi báo cáo Trường** | Chuẩn hoá NFC + bỏ khoảng trắng thừa + về chữ thường trước khi so |
| BUG-09 | Thấp | Không chặn số Trục ngoài 1-6 | `KeyError` làm dừng cả quy trình | Kiểm tra phạm vi, ghi cảnh báo và bỏ qua |

**Bổ sung mới:** trường `thong_ke` (số nhiệm vụ / số dòng Tổng / dòng tiêu đề);
`_num()` chấp nhận số kiểu Việt Nam `1,5`; cảnh báo khi file chứa công thức
chưa được Excel tính sẵn (đọc ra toàn `None`); `summarize_truc_kpi()` đếm thêm số nhiệm vụ
và báo khi bị truyền nhầm file không phải Phụ lục kết quả.

---

## B. `fill_bc736.py` — 5 lỗi

| Mã | Mức | Lỗi | Hậu quả thực tế | Cách vá |
|---|---|---|---|---|
| BUG-10 | **Nghiêm trọng** | Khớp khóa bằng `k in key_norm or key_norm in k`, lấy **kết quả đầu tiên** theo thứ tự dict | Khóa ngắn "Công tác đào tạo" **chiếm chỗ** khóa dài "Công tác đào tạo nghề cho lao động nông thôn" → **điền sai nội dung, không báo lỗi** | Ưu tiên khớp tuyệt đối → nếu phải khớp chuỗi con thì chọn khóa **dài nhất** và **cảnh báo**; báo rõ khi nhập nhằng |
| BUG-11 | **Nghiêm trọng** | `clear_paragraph_runs()` xoá **toàn bộ** run, kể cả nhãn in đậm đen | Mất nhãn "* Công tác tuyển sinh: " → **sai thể thức báo cáo** | Hàm `_replace_yellow_runs()` chỉ thay run bôi vàng, giữ nguyên nhãn đậm |
| BUG-12 | Cao | Chỉ duyệt `doc.paragraphs`, **bỏ qua bảng** | Nội dung nằm trong bảng không được điền; `skipped_control` luôn = 0 (khối Số:/ngày ký nằm trong bảng) | `iter_all_paragraphs()` duyệt cả bảng và bảng lồng nhau |
| BUG-13 | Cao | Không báo khóa `content_map` thừa | Gõ sai tên khóa → nội dung **im lặng biến mất** khỏi báo cáo | Trả về `unused_keys` + cảnh báo |
| BUG-14 | Trung bình | `is_document_control_line()` chỉ bắt dạng `[…]`, lệ thuộc chuỗi "Quảng Ngãi" | Dòng ngày ký dạng `ngày … tháng … năm 20…` có thể **bị điền nhầm** | Regex nhận cả `[…]` và `…`, bỏ phụ thuộc địa danh |

**Bổ sung mới:** xoá hàm chết `fill_period_brackets()` (viết dở, luôn `return None`);
`fill_report()` trả thêm `unused_keys` và `canh_bao`.

---

## C. Kết quả kiểm thử đối chứng

| Tình huống | v2.3 | v2.5.1 |
|---|---|---|
| IIb nhãn `Trục 1.`, KPI ở hàng gộp | `kind=None`, **0 nhiệm vụ** | `kind=KQ`, 4 nhiệm vụ, 2 dòng Tổng |
| IIb có dòng Tổng | Trục 1 = **3 dòng** (lẫn dòng Tổng) | Trục 1 = 2 nhiệm vụ + Tổng tách riêng |
| Cộng dồn KPI Trục 1 | không tính được | SLQĐ = 3,5 (đúng); %CL = 89,3% |
| Cộng dồn 2 đơn vị | — | SLQĐ = 7,0 (đúng) |
| Lọc "Đưa vào KH Trường" | **0 dòng** | 2 dòng (kể cả dòng thừa dấu cách) |
| Ghi chú "Kết luận giao ban" | báo lỗi giả | không báo (đúng) |
| Phát hiện hệ số sai (200→1,0) | không phát hiện | `[SAI CT (9)]` chính xác |
| Nhãn "* Công tác tuyển sinh: " | **bị xoá mất** | giữ nguyên, còn in đậm |
| Khóa dài/ngắn trùng tiền tố | **điền sai nội dung** | điền đúng từng khóa |
| Nội dung trong bảng | bỏ sót | điền đúng |
| Khóa gõ sai | im lặng | báo `unused_keys` |

Chạy lại kiểm thử bất cứ lúc nào: `python3 test_regression_v251.py`

---

## D. Việc CHƯA làm — cần ưu tiên kỳ sau
1. **Chưa kiểm thử trên file Excel/Word THẬT** của Trường (mới chỉ dùng fixture mô phỏng
   đúng đặc tả). Cần chạy lại trên bộ file thật của 14 đơn vị để xác nhận.
2. 4 lỗi dữ liệu tồn đọng kỳ tháng 8 chưa xử lý: Phòng TC-KT (dòng KPI dị thường
   SL=1 kết quả=267), Khoa Kỹ thuật và Công nghệ (cấu trúc cột không chuẩn),
   Khoa Sư phạm (công thức hỏng ở Trục 5), Phòng THHCQT (thiếu dữ liệu đơn vị mẹ).
3. `build_content_map_skeleton()` vẫn chưa ánh xạ tự động sang 22 khóa TB736 —
   vẫn cần người tổng hợp gán thủ công (đúng thiết kế, không nên tự đoán).
