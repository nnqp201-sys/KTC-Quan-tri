# PM-20260910-BC-9-thang-dau-nam-2026-DOT2

- **Tác vụ**: (a) Rà soát chính thức trước khi trình ký — **ĐỢT 2**, kết hợp (c) so sánh 2 phiên bản.
- **Hồ sơ**: BC 9 tháng đầu năm 2026; nhiệm vụ 3 tháng cuối năm 2026 — Trường Cao đẳng Kon Tum, Kính gửi Sở Tài chính.
- **Tiếp nối**: `PM-20260909-BC-9-thang-dau-nam-2026.md` (đợt 1, 54 vấn đề).
- **Phiên bản đã dùng**: ktc-ra-soat-897 v2.22; Checklist 08 (đính chính 09/9/2026); Skill-Tu-hoc v1.3; **Bo-Sung-Chuan-Hoa-TrackChanges... mục 4** (bắt buộc khi đối chiếu phản hồi "đã điều chỉnh").

## Tệp đối chiếu
| | Bản cũ (v1) | Bản mới (v2) |
|---|---|---|
| Dung lượng | 61.751 byte | 63.667 byte |
| Sửa lần cuối | 09/9/2026 08:41 | 10/9/2026 02:19 |
| Đoạn văn | 84 | 79 (giảm 5 do hợp nhất) |
| md5 | `1b3aa62a…` | `94669ace…` |

## Các bước đã chạy
1. Diff **toàn văn** từng đoạn + từng ô bảng giữa 2 phiên bản.
2. **Đo lại** thuộc tính XML thật trên bản mới (`_read_input_properties.py` v1.1 + đo `font.size`/`bold`/`italic` từng run) — KHÔNG dùng lại kết quả đợt 1.
3. Với TỪNG mục trong 54 vấn đề đợt 1: đọc **trọn vẹn** đoạn văn thực tế (Nguyên tắc 4 + mục 4a), quét toàn văn bằng regex từng chuỗi lỗi.
4. Tính lại độc lập 5 phép cộng số liệu và 6 mốc kỷ niệm trên bản mới.
5. Xác minh lại chuỗi "nhiệm kỳ 2026-2031" khớp bản gốc QĐ 38/2026/QĐ-UBND trong kho 01-Legal-Database.

## Kết quả xử lý 54 vấn đề đợt 1
| Mức | Tổng | Xong | Một phần | Chưa | % xong |
|---|---|---|---|---|---|
| Mức 1 | 4 | 2 (B1, D1) | 0 | 2 (**C1, C2**) | 50,0% |
| Mức 2 | 21 | 15 | 1 (B3) | 5 (A1, A2, A3, C7, E5) | 71,4% |
| Mức 3 | 23 | 15 | 5 (C11, C16, D4, E15, E16) | 4 (A5, C10, C14, C15) | 65,2% |
| Mức 4 | 6 | 2 (F4, F5) | 1 (F2) | 3 (B5, F3, G1) | 33,3% |
| **Tổng** | **54** | **33** | **7** | **14** | **61,1%** |

### Xử lý tốt, đáng ghi nhận
- **B1** (Mức 1) xong trọn: "nhiệm kỳ 2026-2031", bỏ luôn dấu phẩy trước "nhiệm kỳ" đúng bản gốc.
- **D1** (Mức 1) xong trọn cả **3 chỗ** → "khoa KT-CN&ĐT-SHLX".
- **C3**: xử lý mâu thuẫn 117tr/500tr bằng cách **tách nguồn** ("riêng" → "bên cạnh đó… còn nhận được") mà **không đổi số liệu nào** — cách làm đúng khi cả 2 số đều đúng nhưng khác loại tài trợ.
- **C8 + C9** giải quyết cùng lúc bằng **một câu định tuyến**: "Đề nghị Sở Tài chính tổng hợp, báo cáo UBND tỉnh chỉ đạo các nội dung sau:" — không phải mở rộng Nơi nhận.
- **C5**: hợp nhất 4 khối trùng lặp ở Phần II mục 1 thành 1 tiểu mục (nguồn chính của việc giảm 5 đoạn văn).
- **F1**: viết lại trung tính, bỏ họ tên cá nhân + từ "ngang nhiên" + kết luận pháp lý.

### Chưa xử lý — chặn trình ký
- **C1** (Mức 1): "Hạn chế…: Không." **giữ nguyên từng chữ**. Bản mới còn **làm rõ thêm 1 tồn tại**: phòng thí nghiệm ISO/IEC 17025 chuyển sang "đợt 2 năm 2026" → tổng **6 tồn tại có sẵn ngay trong văn bản**. Rủi ro TĂNG so với bản cũ vì mục kiến nghị nay chính thức yêu cầu cấp trên vào việc.
- **C2** (Mức 1): vẫn không có tổng tuyển sinh toàn Trường (F5 đã xong — chốt mốc 05/9/2026).
- **A1, A2, A3** (Mức 2): 3 lỗi in đậm thể thức **không sửa gì**.

## PHÁT HIỆN QUAN TRỌNG NHẤT CỦA ĐỢT 2 — 10 lỗi MỚI (N1–N10)
**8/10 lỗi sinh ra trực tiếp từ động tác sửa một lỗi khác.** Nếu đợt 2 chỉ kiểm lại danh mục lỗi cũ mà không diff toàn văn + đo lại XML thì **toàn bộ 10 lỗi này không bị phát hiện**.

| Mã | Lỗi mới | Sinh từ | Mức |
|---|---|---|---|
| N1 | Trích yếu dòng 1 **mất in đậm** (bản cũ cả 2 dòng đều đậm; nay dòng 1 `bold=False`, dòng 2 `bold=True`) | A4 — xóa dấu chấm cuối trích yếu, **gõ lại dòng** làm mất định dạng | **Mức 2** |
| N2 | Chính tả "đoàn viên, **iên chức**, người lao động" (mất chữ v) | E14 — mở rộng "VC, NLĐ"; lần 1 đúng, lần 2 hỏng | **Mức 2** |
| N3 | Dấu chấm kép "…theo quy định của pháp luật**..**" | F1 — chèn câu mới, chưa xóa dấu chấm câu cũ | **Mức 2** |
| N4 | Tiêu đề "I. NHIỆM VỤ TRỌNG TÂM 3 THÁNG CUỐI NĂM 2026" **trùng nguyên văn** tiêu đề Phần II ngay trên nó | C4 — bổ sung tiêu đề cấp "I." | Mức 3 |
| N5 | Cụm "trong phạm vi Nhà trường" gắn vào **cuối 4 tiêu đề** mục 5, 6 của cả 2 phần → câu tối nghĩa + thêm 4 lần "Nhà trường" hoa (đi ngược D4) | F4 — **kiến nghị đợt 1 KHÔNG nêu vị trí đặt cụm** → đã tự đính chính (mục 4b) | Mức 3 |
| N6 | "Hội đồng **K**hoa học và đào tạo" vs "Hội đồng **k**hoa học và đào tạo" | Sửa lẻ 1 chỗ, không quét toàn văn | Mức 3 |
| N7 | "phòng chống tham nhũng tiêu cực" **mất 2 dấu phẩy** (4 chỗ khác đúng) | E14 — mở rộng "PCTNTC" | Mức 3 |
| N8 | "tiếp tục **thực hiện triển khai**" trùng nghĩa | C16 — bỏ tính từ "quyết liệt" | Mức 3 |
| N9 | Chú thích "(nay là Trường Cao đẳng Kon Tum)" chỉ thêm ở 1/2 chỗ | E16 | Mức 3 |
| N10 | "Kính gửi: Sở Tài chính." **rút ngắn**, bỏ "tỉnh Quảng Ngãi" | Không nằm trong kiến nghị nào của đợt 1 | Mức 3 |

## Tổng vấn đề còn phải xử lý: 31 (2 Mức 1 · 9 Mức 2 · 16 Mức 3 · 4 Mức 4)
Mức 2: A1, A2, A3, **N1, N2, N3**, B3, C7, E5 — trong đó 6 mục (A1, A2, A3, N1, N2, N3) sửa xong trong ~30 phút.

## Quyết định phân loại đáng lưu ý
- Lỗi mới phân loại theo **bản chất lỗi**, KHÔNG nặng thêm vì là lỗi phát sinh: N1 (sai thể thức TB 597) và N2, N3 (chính tả, dấu câu) → Mức 2; N4–N10 → Mức 3.
- **Tránh báo lỗi sai**: cụm "các Trung tâm GDNN-GDTX Sa Thầy, Ngọc Hồi, Kon Plong, Đăk Glei" (đoạn #17) là tên trung tâm **ngoài Trường** → KHÔNG phải lỗi D1; gạch ngang dài ở cặp mốc ngày "(24/10/2017 – 24/10/2027)" và liệt kê chủ thể "Trường – Chính quyền – Doanh nghiệp" là **chấp nhận được**, chỉ thống nhất các cụm "giai đoạn 20xx-20yy" (E15).
- **Tự đính chính (mục 4b)**: kiến nghị F4 đợt 1 gợi ý thêm cụm giới hạn phạm vi nhưng không nêu vị trí đặt → gây lỗi N5. Đã ghi rõ trong báo cáo, không lặng lẽ sửa.

## Nội dung người dùng chỉnh / bác bỏ
Chưa có phản hồi trực tiếp bằng lời; phản hồi gián tiếp là chính bản chỉnh sửa v2 — đã phân tích ở trên.

## Kết quả cuối
**VẪN CHƯA ĐỦ ĐIỀU KIỆN TRÌNH KÝ.** Phần VII nêu 10 bước; bước 3 và 4 (bật in đậm 4 chỗ + sửa 2 lỗi mới) mất ~7 phút và xử lý xong 6 trong 9 vấn đề Mức 2.

## Vấn đề còn mở
1. Trường "Người kiểm tra" trong báo cáo xuất ra còn **placeholder**.
2. C1 và C2 cần **dữ liệu và quyết định nội dung**, không sửa được bằng biên tập câu chữ.
3. B5 vẫn chưa xác minh được — WebSearch bị proxy từ chối **HTTP 403** (đã thử 2 lần ở đợt 1). Cần nạp các văn bản 2026 vào kho 01-Legal-Database. Điểm cần soát nhất: **TT 31/2016/TT-BGDĐT** gắn nội dung "bổ nhiệm chức danh, xếp lương nhà giáo".
4. Lỗi kế thừa "nhiệm kỳ 2021-2026" đã sửa ở tệp này nhưng **chưa sửa tại biểu mẫu báo cáo dùng chung và kho 03-Templates**.
5. Chưa tải được báo cáo rà soát lên `12-Output/` (giới hạn tải tệp nhị phân, SKILL.md quy tắc 20) — cần người dùng tự tải lên.

## Hành động tiếp theo — đề xuất ghi Skill-Tu-hoc (Tình huống D, chờ xác nhận Phó Trưởng phòng TH-HC&QT)
**Pattern lỗi mới 3 — "LỖI PHÁT SINH KHI SỬA LỖI"** (bài học lớn nhất của ca này). Ba dạng lặp lại nhiều nhất, đều phát hiện được bằng một lượt kiểm sau khi sửa:
1. **Gõ lại một dòng thay vì chỉ thay đổi thuộc tính** → mất in đậm/nghiêng (N1).
2. **Mở rộng chữ viết tắt bằng cách gõ tay** → sai chính tả hoặc mất dấu phẩy (N2, N7).
3. **Sửa lẻ một chỗ mà không quét toàn văn** → biến một lỗi thống nhất thành lỗi bất nhất mới (N6, N9).

**Quy tắc rà soát đợt 2 (bắt buộc)**: luôn (i) **diff toàn văn** hai phiên bản và (ii) **đo lại thuộc tính XML**, KHÔNG chỉ kiểm lại danh mục lỗi cũ. Căn cứ thực chứng: ca này nếu chỉ kiểm danh mục cũ thì bỏ sót 10 lỗi mới, trong đó 3 lỗi Mức 2.

**Quy tắc viết kiến nghị trong báo cáo rà soát**: khi kiến nghị **thêm hoặc bớt một cụm từ**, phải nêu rõ **VỊ TRÍ** đặt cụm đó. Căn cứ: kiến nghị F4 đợt 1 thiếu điểm này → gây lỗi N5.

**Pattern tốt (mục 2.7) — bổ sung 2 mục, nguồn: bản chỉnh sửa BC 9 tháng 2026, ngày 10/9/2026:**
1. **"Tách nguồn thay vì sửa số"**: khi hai số liệu mâu thuẫn trong một phép tổng nhưng cả hai đều đúng, sửa từ nối để tách thành hai nguồn độc lập ("riêng" → "bên cạnh đó… còn nhận được") thay vì thay đổi số liệu.
2. **"Định tuyến kiến nghị bằng một câu mở đầu"**: khi báo cáo gửi một cơ quan nhưng kiến nghị nhiều cơ quan, mở mục kiến nghị bằng câu "Đề nghị <cơ quan nhận> tổng hợp, báo cáo <cấp trên> chỉ đạo các nội dung sau:" — giữ đúng nguyên tắc gửi văn bản đến cơ quan có thẩm quyền tổng hợp, không phải mở rộng Nơi nhận.

## ID đầu ra
- `Bao-cao-ra-soat-KTC897_BC-9-thang-2026_DOT-2_20260910.docx` (A4 ngang; 8 phần; 13 bảng, bảng rộng nhất 25,5cm ≤ 25,7cm) — đã giao cho người dùng trong phiên, **chưa** tải lên Drive (vấn đề còn mở #5).
