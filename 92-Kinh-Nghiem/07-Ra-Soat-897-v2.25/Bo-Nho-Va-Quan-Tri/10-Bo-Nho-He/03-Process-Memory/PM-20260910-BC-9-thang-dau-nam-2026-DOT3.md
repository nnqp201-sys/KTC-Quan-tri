# PM-20260910-BC-9-thang-dau-nam-2026-DOT3

- **Tác vụ**: (a) Rà soát chính thức trước khi trình ký — **ĐỢT 3**, kết hợp (c) so sánh 2 phiên bản.
- **Hồ sơ**: BC 9 tháng đầu năm 2026; nhiệm vụ 3 tháng cuối năm 2026 — Trường Cao đẳng Kon Tum, Kính gửi Sở Tài chính.
- **Tiếp nối**: `PM-20260909-…md` (đợt 1, 54 vấn đề) → `PM-20260910-…DOT2.md` (đợt 2, còn 31) → PM này.
- **Phiên bản đã dùng**: ktc-ra-soat-897 v2.22; Checklist 08 (đính chính 09/9/2026); Skill-Tu-hoc v1.3; Bo-Sung-Chuan-Hoa-TrackChanges… **mục 4**.

## Ba phiên bản
| | v1 | v2 | v3 |
|---|---|---|---|
| Byte | 61.751 | 63.667 | 66.270 |
| Sửa lúc | 09/9 08:41 | 10/9 02:19 | 10/9 03:36 |
| Đoạn văn | 84 | 79 | 83 |
| Vấn đề tồn tại | 54 | 31 | **22** |

## Các bước đã chạy
1. Diff toàn văn v2↔v3 ở **cấp đoạn VÀ cấp ký tự** (difflib SequenceMatcher lồng 2 tầng) — bắt được cả thay đổi vài ký tự.
2. **Đo lại** thuộc tính XML thật trên v3, không dùng lại kết quả đợt 2.
3. Đọc **trọn vẹn** từng đoạn liên quan 31 mục tồn; đọc trọn cả 4 tiểu mục mới.
4. **BƯỚC MỚI**: đối chiếu **danh mục 14 cụm nội dung then chốt** của v2 trong v3 để phát hiện mất/đổi nghĩa khi tái cấu trúc → chính bước này bắt được N15.
5. Tính lại độc lập 5 phép cộng và 6 mốc kỷ niệm.

## Kết quả xử lý 31 vấn đề đợt 2
- **Xong**: 13 (A1, A5, C10, C15, E15, N2, N3, N4, N5, N6, N7, N8, N9)
- **Một phần**: 3 (C7 — 1/2 chỗ; C11 — sai hướng, xem dưới; D4 — còn 4/8)
- **Chưa**: 15 (C1, C2, A2, A3, N1, B3, E5, C14, C16, N10, B5, F2, F3, G1 …)
- 8/10 lỗi mới của đợt 2 (N2–N9) đã sửa xong.

### Sửa tốt nhất của v3
- **A1**: tên đơn vị ban hành nay **13pt + bold** (tồn qua 2 phiên bản).
- **C15**: đoạn ~15 việc tách thành **4 tiểu mục theo NHÓM CHỨC NĂNG** đúng như kiến nghị: "- Đầu tư - mua sắm", "- Quản lý, khai thác tài sản công", "- Xử lý tranh chấp đất", "- Sắp xếp trụ sở sau sáp nhập". Đối chiếu 14 cụm then chốt: **13/14 còn nguyên**, không mất nội dung.
- **A5**: Nơi nhận tách 2 dòng + đảo đúng thứ tự mẫu TB 597.
- **C7 (1 chỗ)**: sửa mâu thuẫn mốc bằng cách **đổi ĐỘNG TỪ** chứ không đổi mốc: "các hoạt động kỷ niệm 10 năm" → "chuẩn bị nội dung phục vụ kỷ niệm 10 năm (24/10/2027)".

## PHÁT HIỆN QUAN TRỌNG NHẤT ĐỢT 3 — 5 lỗi mới + 1 HỒI QUY + 1 sửa sai hướng
Không mục nào phát hiện được nếu chỉ đọc v3 một mình — **phải so với bản liền trước**.

| Mã | Nội dung | Sinh từ | Mức |
|---|---|---|---|
| **N15** | **ĐỔI NGHĨA**: "**phê duyệt danh mục, số lượng thuốc** phục vụ KCB BHYT tại PKĐK (Đợt 2/2026)" → "**Cung cấp thuốc** phục vụ KCB BHYT…". Hai hành vi khác chế độ pháp lý: phê duyệt danh mục là hành vi quản lý thuộc thẩm quyền Hiệu trưởng (có VB phê duyệt, gắn dự toán/quyết toán BHYT); cung cấp thuốc là hoạt động chuyên môn dược thuộc phạm vi giấy phép KCB — mà chính báo cáo này đang **xin Sở Y tế mở rộng** danh mục thuốc và phạm vi hoạt động. Còn bị xếp nhầm dưới tiểu mục "Đầu tư - mua sắm". | C15 — **rút gọn câu khi gom vào tiểu mục** | **Mức 2** |
| **B3** | **HỒI QUY**: v1 "Nghị định số 233, 234, 235/2026/NĐ-CP" → v2 đã sửa đúng "233/2026/NĐ-CP, 234/2026/NĐ-CP, 235/2026/NĐ-CP" → v3 **quay lại dạng sai của v1**. Dấu hiệu điển hình của **sửa từ bản gốc cũ thay vì bản mới nhất**. | Sửa nhầm phiên bản gốc | **Mức 2** |
| **C11** | **SỬA SAI HƯỚNG**: trùng lặp an toàn thông tin **tăng 2 → 3 lần**. v3 **chèn thêm** câu vào cuối Phần I mục 3 (đoạn #34) trùng nguyên văn đoạn #72 (Phần II "An ninh mạng:") mà **không xóa** đoạn #72; cộng đoạn #46 (Phần I mục 6) đã có sẵn. | Chuyển nội dung nhưng chỉ chèn, không xóa nơi cũ | **Mức 2** |
| N11 | "tiêu **cựctrong** 9 tháng" — mất dấu cách (phần thêm dấu phẩy thì ĐÚNG) | N7 | Mức 3 |
| N12 | "( tại Khu thực nghiệm thuộc Cơ sở 2 và Cơ sở 5)" — thừa cách sau "(", và cụm địa điểm đặt sau "theo quy định của pháp luật" nên bổ nghĩa sai | C15 | Mức 3 |
| N13 | "…thuộc Trường**.T**hực hiện Phương án…" — mất dấu cách sau dấu chấm | C15 | Mức 3 |
| N16 | Nhãn "- Đầu tư - mua sắm:" có 2 dấu gạch cùng dòng, 2 chức năng khác nhau | C15 — đặt tên tiểu mục | Mức 4 |

## 22 vấn đề còn phải xử lý
- **Mức 1 (2)**: C1, C2 — **chưa động đến qua CẢ BA phiên bản**.
- **Mức 2 (7)**: A2, A3, N1 (3 lỗi in đậm, sửa 3 phút), N15, B3, C11, E5.
- **Mức 3 (8)**: N11, N12, N13, N10, C7 (chỗ còn lại), C14, C16, D4.
- **Mức 4 (5)**: B5, F2, F3, G1, N16.

### C1 — mâu thuẫn TĂNG theo từng bản
Mục "Hạn chế…: Không." giữ nguyên từng chữ, nhưng số tồn tại nêu ngay trong thân báo cáo **tăng dần**: v1 có 6 → v2 thêm "ISO/IEC 17025 chuyển sang đợt 2" → v3 lập hẳn **tiểu mục riêng "- Xử lý tranh chấp đất"**. Nay **7 tồn tại** có sẵn trong văn bản. Rủi ro cũng tăng vì mục kiến nghị (từ v2) đã chính thức yêu cầu cấp trên vào việc.

## Quan sát về thứ tự xử lý qua 3 đợt
Lỗi **hình thức** được xử lý nhanh và gần hết (thể thức, bố cục, hành văn, chính tả). Hai vấn đề **nội dung Mức 1** không nhúc nhích qua cả ba bản — và đó lại là hai nội dung cơ quan nhận báo cáo quan tâm nhất, đồng thời là hai nội dung **duy nhất không sửa được bằng biên tập**.

## Nội dung người dùng chỉnh / bác bỏ
Chưa có phản hồi bằng lời; phản hồi gián tiếp là bản v3.

## Kết quả cuối
**VẪN CHƯA ĐỦ ĐIỀU KIỆN TRÌNH KÝ.** Phần VII nêu 10 bước; bước 3–7 (khôi phục N15, B3, bật in đậm 3 chỗ, bỏ trùng C11, sửa 3 lỗi dấu cách) mất ~15 phút và xử lý xong 6/7 vấn đề Mức 2.

## Vấn đề còn mở
1. Trường "Người kiểm tra" trong báo cáo xuất ra còn **placeholder**.
2. C1, C2 cần **dữ liệu và quyết định nội dung**.
3. B5 chưa xác minh — WebSearch bị proxy từ chối **HTTP 403**. Ưu tiên soát **TT 31/2016/TT-BGDĐT**.
4. Lỗi kế thừa "nhiệm kỳ 2021-2026" đã sửa ở tệp nhưng **chưa sửa tại biểu mẫu dùng chung và kho 03-Templates**.
5. Chưa tải 3 báo cáo rà soát lên `12-Output/` (giới hạn tải tệp nhị phân, SKILL.md quy tắc 20).
6. **Cần xác định đơn vị soạn thảo đang sửa trên bản nào** — hồi quy B3 cho thấy có thể tồn tại nhiều bản song song.

## Hành động tiếp theo — đề xuất ghi Skill-Tu-hoc (Tình huống D, chờ xác nhận Phó Trưởng phòng TH-HC&QT)

### MỞ RỘNG "Pattern lỗi phát sinh khi sửa lỗi" (đã đề xuất ở đợt 2) — thêm 3 dạng mới
4. **Sửa trên bản cũ → HỒI QUY**: nội dung đã sửa đúng ở bản trước quay lại dạng sai. Nhận biết: chỉ phát hiện được khi diff với bản liền trước. Căn cứ: B3, v2→v3.
5. **Rút gọn khi di chuyển → ĐỔI NGHĨA**: gom câu vào tiểu mục kèm rút gọn làm mất bản chất pháp lý của hành vi. Nhận biết: đối chiếu danh mục cụm nội dung then chốt trước/sau tái cấu trúc. Căn cứ: N15 (phê duyệt danh mục thuốc → cung cấp thuốc). **Phân loại Mức 2**.
6. **Chèn mà không xóa → TRÙNG LẶP TĂNG**: chuyển nội dung sang chỗ mới nhưng chỗ cũ vẫn còn. Căn cứ: C11, trùng lặp 2→3 lần.

### Bổ sung QUY TRÌNH rà soát đợt sau (bắt buộc)
- Diff với **BẢN LIỀN TRƯỚC** ở cả cấp đoạn và **cấp ký tự**, không chỉ kiểm lại danh mục lỗi.
- **Kiểm danh mục cụm nội dung then chốt** mỗi khi có tái cấu trúc đoạn dài — bước này bắt được N15 mà mọi bước khác bỏ sót.
- Trong **kết luận** báo cáo rà soát, **tách bạch** nhóm sửa được bằng biên tập và nhóm cần dữ liệu, để đơn vị soạn thảo khởi động sớm nhóm thứ hai (quan sát qua 3 đợt: nhóm hình thức xử lý gần hết, nhóm nội dung không nhúc nhích).

### Khuyến nghị quy trình cho ĐƠN VỊ SOẠN THẢO (4 quy tắc)
1. Luôn sửa trên **bản mới nhất**, không mở lại bản gốc cũ (→ B3).
2. Khi tách/gom đoạn, **KHÔNG rút gọn câu**, chỉ di chuyển nguyên văn (→ N15).
3. Khi chuyển nội dung sang phần khác, **xóa nơi cũ ngay trong cùng thao tác** (→ C11).
4. Sau mỗi lần sửa, **đọc lại trọn câu mới kèm dấu câu và khoảng trắng hai đầu** (→ N11, N12, N13).

### Pattern tốt (mục 2.7) — bổ sung 3 mục, nguồn: bản v3 ngày 10/9/2026
1. **"Tách tiểu mục theo NHÓM CHỨC NĂNG"** thay vì cắt theo độ dài — người đọc cấp trên nhận ra ngay việc trọng tâm.
2. **"Sửa mâu thuẫn mốc thời gian bằng cách đổi ĐỘNG TỪ, không đổi mốc"**: "các hoạt động kỷ niệm 10 năm" → "chuẩn bị nội dung phục vụ kỷ niệm 10 năm (24/10/2027)" — giữ nguyên nhiệm vụ mà hết mâu thuẫn.
3. **"Đối chiếu danh mục cụm nội dung then chốt trước/sau tái cấu trúc"** — nên thành bước bắt buộc mỗi khi tái cấu trúc một đoạn dài.

## ID đầu ra
- `Bao-cao-ra-soat-KTC897_BC-9-thang-2026_DOT-3_20260910.docx` (A4 ngang; 8 phần; 12 bảng, bảng rộng nhất 25,5cm ≤ 25,7cm) — đã giao cho người dùng trong phiên, **chưa** tải lên Drive (vấn đề còn mở #5).
