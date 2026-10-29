Phiên bản: v2.14
Ngày chạy: 25/8/2026
Điểm: 8/28 đúng hoàn toàn, 5/28 đúng nhưng sai mức, 13/28 bỏ sót
Danh sách lỗi bỏ sót: #1, #5, #10, #11, #13, #15, #17, #19, #21, #22, #26, #27, #28
Danh sách false positive: 3 trường hợp — xem Mục 4
Nhận xét: xem Mục 5 (đặc biệt #6 và #23)

═══════════════════════════════════════════════════════════════════
CHI TIẾT ĐỐI CHIẾU — 19 phát hiện thực tế vs 28 lỗi đáp án
═══════════════════════════════════════════════════════════════════

## 1. Đúng hoàn toàn (đúng phát hiện + đúng mức) — 8/28

| # đáp án | Nội dung | Mức | Kết quả |
|---|---|---|---|
| 2 | "UỶ BAN NHÂN DÂN" thiếu dấu hỏi | 2 | ✅ Đúng (gộp chung 1 dòng báo cáo với #3) |
| 3 | "CỘNG HOÀ..." thiếu dấu hỏi | 2 | ✅ Đúng (gộp chung dòng với #2) |
| 4 | Ngày 5/2 thiếu số 0 | 2 | ✅ Đúng |
| 6 | QĐ 49 hết hiệu lực | 1 | ✅ Đúng — **PASS bài test trọng điểm** |
| 7 | NĐ 60/2021 thiếu NĐ 111/2025 | 1 | ✅ Đúng |
| 9 | Tên Cơ sở 4 sai | 1 | ✅ Đúng |
| 18 | "K/T." nên "KT." (hành chính) | 2 | ✅ Đúng |
| 23 | Không tự kết luận tổ chức Đảng | 4 | ✅ Đúng — **PASS bài test quan trọng nhất** |

## 2. Đúng phát hiện, sai mức — 5/28 (tính nửa điểm theo thang chấm)

| # đáp án | Nội dung | Mức đáp án | Mức tôi chấm | Lệch |
|---|---|---|---|---|
| 8 | Sai số hiệu 1229→1299 | 2 | **1** | Chấm nặng hơn — coi lỗi trích dẫn sai số là ảnh hưởng hiệu lực pháp lý, nhưng đáp án xếp là lỗi chất lượng |
| 12 | Công ty/Trung tâm không nhất quán | 4 | **3** | Chấm nặng hơn |
| 14 | Câu cụt "theo định" | 4 | **3** | Chấm nặng hơn |
| 20 | Cấp trên trực tiếp ghi trùng tên (VB Đảng) | 2 | **1** | Chấm nặng hơn |
| 25 | Quốc hiệu cho Đoàn TN | 2 | **1** | Chấm nặng hơn |

**Nhận xét mẫu số lệch**: cả 5/5 trường hợp đều bị hệ chấm **NẶNG HƠN** đáp án kỳ vọng (không có trường hợp nào chấm nhẹ hơn). Đây là tín hiệu Checklist đang thiên về an toàn quá mức ở nhóm lỗi ngôn ngữ/thể thức thứ yếu — cần hiệu chỉnh ranh giới Mức 1↔2 và Mức 3↔4 rõ hơn.

## 3. Đúng mức nhưng sai chi tiết — 2 trường hợp (không tính vào 2 nhóm chính, ghi riêng)

| # đáp án | Vấn đề |
|---|---|
| 16 | Định mức tính sai — đúng bản chất lỗi (làm tròn lẻ rồi cộng dồn) và đúng Mức 1, nhưng **số liệu "đúng" tôi tính ra là 4** trong khi đáp án ghi rõ **"định mức tối đa cho phép là 15"**. Đây là sai số nghiêm trọng về công thức/tỷ lệ định mức máy photocopy — cần tra lại đúng Phụ lục QĐ 10/2026/QĐ-TTg, không được giữ nguyên giả định tỷ lệ 1/15 đã dùng trong các ca trước. |
| 24 | Phát hiện đúng vị trí lỗi (thẩm quyền ký văn bản Đảng sai kiểu) và đúng Mức 2, nhưng **kiến nghị sai hướng**: tôi đề xuất đổi "KT. BÍ THƯ" thành "T/M. ĐẢNG ỦY", trong khi đáp án chỉ yêu cầu sửa thành "K/T. BÍ THƯ" (giữ nguyên chức danh, chỉ đổi kiểu ký hiệu từ dấu chấm sang gạch chéo). |

## 4. Bỏ sót hoàn toàn — 13/28

| # đáp án | Nội dung | Mức | Nhóm nguyên nhân |
|---|---|---|---|
| 1 | Lề trang cứng 2cm (thuộc tính file, không phải chữ hiển thị) | 1 | Không kiểm tra thuộc tính XML của file đầu vào, chỉ đọc nội dung text |
| 5 | Trích yếu cỡ chữ 11 không đậm | 3 | Không kiểm tra định dạng font/cỡ chữ của file đầu vào |
| 10 | "Đảm bảo" nên "Bảo đảm" | 3 | Checklist 08 chưa có mục từ vựng dùng sai |
| 11 | Dấu chấm phẩy nên dấu phẩy khi liệt kê | 3 | Checklist 08 chưa có quy tắc dấu câu khi liệt kê |
| 13 | Viết hoa "Nhà trường" giữa câu | 3 | Checklist 08 chưa có quy tắc viết hoa từ thông dụng |
| 15 | Danh mục bộ môn dùng bản cũ (thiếu CNTT) | 3 | **Nghiêm trọng**: không có nguồn tham chiếu danh mục 15 bộ môn hiện hành để đối chiếu |
| 17 | Nơi nhận dùng sai cột viết tắt | 2 | Có phát hiện tại vị trí này nhưng nội dung khác — không match |
| 19 | Ghi học hàm/học vị trước tên người ký | 2 | Checklist 08 chưa có quy tắc này |
| 21 | Thiếu dấu sao dưới tên cơ quan (VB Đảng) | 2 | Skill 29/HD 05-HD/VPTW chưa đủ chi tiết thể thức trình bày |
| 22 | Sai định dạng số hiệu Đảng ("12/TB-ĐU" → "12-TB/ĐU") | 2 | **Nghiêm trọng**: chưa có quy tắc phân biệt định dạng số hiệu hành chính (dấu hai chấm) và Đảng (dấu gạch nối, gạch chéo) |
| 26 | Sai định dạng số hiệu đoàn thể | 2 | Cùng nhóm nguyên nhân với #22, áp cho hệ đoàn thể |
| 27 | Ngày 8/9 thiếu số 0 | 2 | Có kiểm tra ngày ở VB khác nhưng bỏ sót ở VB này |
| 28 | Thiếu trích yếu đúng chuẩn đoàn thể | 4 | Hệ quy chiếu đoàn thể thật sự chưa có Checklist đầy đủ (đã tự nhận trong SKILL.md) |

**Nhóm nguyên nhân gộp — ưu tiên khắc phục theo thứ tự:**
1. **Số hiệu văn bản Đảng/đoàn thể sai định dạng** (#22, #26) — quy tắc hoàn toàn chưa có, mất 2/28 điểm liền
2. **Danh mục 15 bộ môn hiện hành** (#15) — thiếu nguồn tham chiếu, có thể gây sai lặp lại nhiều lần
3. **Thuộc tính file thật (lề trang, font, cỡ chữ)** (#1, #5) — hệ hiện chỉ đọc nội dung text, không kiểm tra XML/định dạng gốc của file đầu vào
4. **Nhóm từ vựng/dấu câu/viết hoa vụn** (#10, #11, #13, #19) — 4 lỗi nhỏ nhưng cộng dồn ảnh hưởng điểm

## 5. False positive — 3 trường hợp

| Phát hiện của tôi | Vị trí | Đánh giá |
|---|---|---|
| "Viết thường sau dấu ':' " tại danh mục bộ môn | QĐ 45 — Danh sách bộ môn | Có căn cứ thật (TB 597 Mục 3.1) nhưng **không phải lỗi được cố ý cài tại vị trí này** — lỗi thật sự cài ở đó là #15 (danh mục bộ môn cũ). Tôi đã nhìn nhầm sang một vấn đề khác cùng đoạn văn, dẫn đến vừa bỏ sót #15 vừa tạo phát hiện phụ không thuộc phạm vi test. |
| Mâu thuẫn ngày ban hành 8/9 vs "phong trào hè 2026" | TB 08/TB-ĐTN | Logic suy luận có cơ sở nhưng không phải lỗi được đáp án công nhận — có thể do tôi đọc nội dung theo hướng suy diễn quá xa so với ý đồ bài test. |
| Văn phong "Nhà trường giao..." tại Điều 3 (Mức 4, góp ý) | QĐ 45 — Điều 3 | Không trùng với lỗi #13 thật (viết hoa "Nhà trường" giữa câu) dù cùng đối tượng — đây là góp ý phong cách tự phát sinh, không gây hại nhưng không đúng trọng tâm. |

**Đánh giá chung về false positive**: cả 3 trường hợp đều **không sai về bản chất pháp lý**, chỉ là không trùng với đúng lỗi được thiết kế tại vị trí đó. Rủi ro thực tế thấp, nhưng cho thấy hệ có xu hướng "tìm ra vấn đề gần đúng" thay vì "xác định chính xác vấn đề đã được thiết kế" — cần cảnh giác khi áp dụng vào hồ sơ thật, vì hồ sơ thật không có "đáp án" để đối chiếu.

## 6. Nhận xét đặc biệt theo yêu cầu (#6 và #23)

**#6 — PASS.** Báo cáo tra đúng ngày hiệu lực: nhận diện QĐ 49/QĐ-CĐKT (24/7/2025) đã bị QĐ 988/QĐ-CĐKT (12/5/2026) thay thế, không chỉ dừng ở nhận diện mẫu số hiệu quen thuộc. Đây là bằng chứng Checklist 08 Mục 1 hoạt động đúng thiết kế.

**#23 — PASS, quan trọng nhất.** Báo cáo **không tự kết luận** loại hình tổ chức Đảng của Trường dù văn bản khẳng định chắc chắn "Đảng bộ trực thuộc cơ sở". Đã xếp Mức 4, ghi rõ "chưa xác minh", đề nghị xác minh với Ban Tổ chức Tỉnh ủy trước khi ban hành — đúng kỷ luật "không suy luận khi có ≥2 khả năng pháp lý" mà Skill 29 Phụ lục 3 và Quy tắc 32 mục (f) yêu cầu.

## 7. Kết luận tổng thể

Tỷ lệ đúng hoàn toàn **8/28 (28,6%)** là **THẤP**, chưa đạt mức tin cậy để dùng làm căn cứ duy nhất cho rà soát chính thức có tính pháp lý cao. Điểm mạnh: hệ **pass cả 2 bài test trọng điểm nhất** (#6 tra hiệu lực căn cứ, #23 kỷ luật không suy luận) — cho thấy các nguyên tắc cốt lõi trong SKILL.md hoạt động đúng. Điểm yếu: hệ **bỏ sót toàn bộ nhóm lỗi thể thức chi tiết** của văn bản Đảng và đoàn thể (số hiệu, dấu sao, cấu trúc số hiệu), và **không kiểm tra thuộc tính file thật** (lề, font, cỡ chữ) mà chỉ dựa vào nội dung text hiển thị.

**Khuyến nghị**: không dùng kết quả rà soát của Hệ làm căn cứ duy nhất cho văn bản Đảng/đoàn thể cho đến khi hoàn thiện Checklist chuyên biệt (xem việc còn mở #2 trong MEMORY-INDEX.md). Với văn bản hành chính nhà nước thuần túy, tỷ lệ đúng cao hơn đáng kể (7/19 lỗi trang 1 đúng hoàn toàn, một số lỗi bổ sung khác đúng nhưng lệch mức) — mức tin cậy khá hơn nhưng vẫn cần kiểm tra chéo con người trước khi trình ký, đúng như SKILL.md đã khuyến cáo.
