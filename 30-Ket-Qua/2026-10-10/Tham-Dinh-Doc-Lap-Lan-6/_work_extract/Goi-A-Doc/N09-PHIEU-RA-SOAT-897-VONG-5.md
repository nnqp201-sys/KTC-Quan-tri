<!-- N09: chép nguyên văn từ `PHIEU-RA-SOAT-897-VONG-5_TB-v8_HD-v8_BC-v7_TT5-v1.md` (sha256 4089266a01c2ac5464dd0d2ae69b2b3151ad21efbbeeab532a66357486d95c92) -->

# PHIẾU RÀ SOÁT KTC-897 — VÒNG 5 (BỔ SUNG, PHẦN SỬA ĐỔI THEO THẨM ĐỊNH LẦN 5)

**Văn bản** (4 văn bản, rà từng văn bản):
1. Dự thảo Thông báo hướng dẫn sử dụng bộ công cụ trí tuệ nhân tạo KTC-Quan-tri — bản 8.
2. Tài liệu hướng dẫn sử dụng chi tiết Bộ công cụ KTC-Quan-tri (kèm theo Dự thảo Thông báo) — bản 8.
3. Báo cáo quá trình xây dựng bộ công cụ trí tuệ nhân tạo KTC-Quan-tri — bản 7.
4. Báo cáo tiếp thu, giải trình ý kiến thẩm định độc lập lần 5 — bản 1 (văn bản mới, rà toàn văn).

**Tệp rà soát:** `30-Ket-Qua/2026-09-29/Soan-Thao/` — (1), (2), (3) tệp `_TrackChanges` và `_ban-sach`; (4) tệp duy nhất.
**Phạm vi:** (1), (2), (3) chỉ các vị trí có đánh dấu của tác giả “Tiếp thu thẩm định lần 5, bản 1.3.13 (Claude)”:
Dự thảo Thông báo 5 đoạn (15 đánh dấu), Tài liệu hướng dẫn 6 đoạn và chân trang (14 đánh dấu), Báo cáo quá trình 17 đoạn, ô bảng (150
đánh dấu). Phần còn lại đã qua vòng 1 - 4 (phiếu trong `3-Ra-soat-897/`). (4) rà toàn văn.
**Công cụ:** Skill `ktc-ra-soat-897:review` (Core v3.0 + baseline v2.24; nạp `00-RUNTIME-INVARIANTS` →
`10-…-v3-Core` → `20-…-v2.24-BASELINE`; Checklist 01, 02, 04, 05, 08).
**Căn cứ tổ chức rà soát:** điểm b Mục 8 Thông báo số 1056/TB-CĐKT ngày 16/9/2026 — vòng bổ sung cho phần sửa sau các vòng trước.
**Ngày rà soát:** 29/9/2026.

---

## PHẦN I. THÔNG TIN CHUNG

| Mục | Nội dung |
|---|---|
| Loại văn bản | (1): Thông báo của Trường (mẫu 2.1, Hiệu trưởng ký); (2): Tài liệu hướng dẫn kèm theo Thông báo; (3), (4): Báo cáo của Phòng TH-HC&QT gửi Lãnh đạo Trường (mẫu 2.2) |
| Hệ quy chiếu | **Hệ A** cho cả 4 văn bản (văn bản hành chính; NĐ 30/2020/NĐ-CP, Thông báo số 597/TB-CĐKT ngày 19/5/2026). Không có văn bản Đảng, đoàn thể, VBQPPL |
| Nguồn kho đã đọc | Kho 01: `ND-334-2026-ND-CP_v1.docx` (đối chiếu ý kiến Gemini 5.3 — không có quy định, thuật ngữ về minh chứng); kho 02: `PL-2119-QD-CDKT_Danh-muc-san-pham-chuan-hoa_20260928_v1.xlsx` (mã băm khớp tệp dữ liệu trong plugin); Thông báo số 924/TB-CĐKT, 1056/TB-CĐKT (đã đối chiếu bản gốc ở vòng 3). Bộ quy tắc: Checklist 08 mục 2b (viết hoa sau dấu hai chấm) đọc bản gốc trên Drive ngày 29/9/2026 |
| Nguồn không cần tra Internet | Phần sửa không viện dẫn văn bản mới ngoài Trường |
| Đo thể thức (byte thật) | `ktc897_properties.py`: chữ ký ZIP `504b0304` hợp lệ cả 7 tệp; `kiem_the_thuc.py` (TT01 - TT19): (1), (3), (4) 0 gợi ý; (2) 0 lỗi Mức 1 - 2, còn TT05, TT11 Mức 3 — có từ bản 3, đã chấp nhận ở vòng 2 - 4 |
| Xem trang thật | Xuất PDF bằng Word: (1) 7 trang, (4) 9 trang, (3) trang 15 - 17, (2) trang 5 - 7 — phát hiện khối chữ ký (1), (3) bị tách trang, đã sửa (M3-02) |
| Quét viện dẫn | `kiem_vien_dan.py` (VD01 - VD12): 0 gợi ý cả 4 văn bản |

## PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT

| Mã | Văn bản, vị trí | Bằng chứng | Vấn đề | Căn cứ | Mức | Kiến nghị | Xử lý |
|---|---|---|---|---|---|---|---|
| M2-01 | (4) Mục 7, gạch đầu dòng “Dữ liệu” | “trước khi có biên bản phân quyền chỉ đọc (cổng G1), chỉ dùng dữ liệu giả lập …; sau đó xử lý dữ liệu nội bộ trong phạm vi được phép theo Thông báo số 924/TB-CĐKT” | Đọc thành chỉ cần cổng G1 là được xử lý dữ liệu nội bộ — rộng hơn Dự thảo Thông báo (điểm a Mục 3 Phần I: cần **cả** phân quyền chỉ đọc **và** nền tảng đã có biên bản nghiệm thu) | Checklist 02 (thống nhất giữa các văn bản trong hồ sơ); bài học PM-20260927 mục 1 | 2 | “dữ liệu nội bộ chỉ xử lý khi đã đạt cổng G1 và trên nền tảng đã có biên bản nghiệm thu (cổng G2), trong phạm vi …” | **Đã sửa** |
| M3-01 | (3) Mục 7, đoạn “Các nội dung chưa thực hiện”, ý (iv) | “(iv) rà soát … phần sửa đổi lần 3 … (… vòng 4 …; vòng 5 … đã rà soát)” | Ý thuộc danh sách “chưa thực hiện” nhưng liệt kê các vòng đã làm — tự mâu thuẫn | Checklist 04 (logic câu) | 3 | “(iv) rà soát … phần sửa đổi tiếp theo của các văn bản trong hồ sơ, nếu có (đã thực hiện: …)” | **Đã sửa** |
| M3-02 | (1) trang 6 - 7; (3) trang 16 - 17 | Khối Nơi nhận, người ký tách khỏi câu kết (lần xuất đầu) | Khối chữ ký tách trang | Thông báo số 597/TB-CĐKT (bố cục khối ký); chuẩn 18 mục 1 (xem trang thật) | 3 | Không tách hàng bảng chữ ký, giữ liền câu kết | **Đã sửa** — đã xuất lại PDF kiểm |
| M3-03 | (2) Bảng “Thành phần”, ô “Thao tác tự động” | “không kiểm được chương trình do AI viết sẵn trong tệp” | Chưa khớp đoạn đã sửa ở Phần III cùng tài liệu (kết quả thử 10 kịch bản) | Checklist 02 (thống nhất trong văn bản) | 3 | Dùng cùng cách diễn đạt với (1) | **Đã sửa** |
| M3-04 | (4) Mục 1, nội dung 2.5 | Mã SHA-256 64 ký tự trong câu | Dãn chữ bất thường trên trang 2 - 3 (căn đều hai bên) | Checklist 05 (trình bày) | 3 | Rút gọn trong câu, ghi đầy đủ một lần (mục 7) | **Đã sửa** |
| M4-01 | (3), (4) | “commit”, “checkout”, “base64” | Thuật ngữ kỹ thuật tiếng Anh trong văn bản trình Lãnh đạo | Checklist 04 | 4 | Có giải thích trong ngoặc ở lần đầu | Giữ nguyên — không có từ tương đương ngắn; lần đầu đã giải nghĩa “bản lấy sạch (checkout)” |
| M4-02 | (2) Đoạn “Kết quả nghiệm thu gắn với phiên bản, mô hình” | Câu dài, nhiều dấu hai chấm lồng nhau | Khó đọc | Checklist 04 | 4 | Tách thành bảng khi cập nhật tài liệu sau thí điểm | Giữ nguyên |

**Cách xử lý:** các điểm M2-01, M3-01 đến M3-04 nằm trong phần chèn của chính đợt sửa lần này (chưa có người duyệt), nên
được sửa thẳng vào nội dung của đợt rồi dựng lại Track Changes trên bản sạch đã qua vòng 4. Tác giả đánh dấu giữ là “Tiếp
thu thẩm định lần 5, bản 1.3.13 (Claude)”. M3-02 là thay đổi bố cục (không tách hàng, giữ liền đoạn), không đổi chữ.

### II.1. Kiểm lại vấn đề vòng 1 - 4 trong phần bị sửa

Giới hạn dữ liệu theo Thông báo số 924/TB-CĐKT (sau khi sửa M2-01), không ghi “đã nghiệm thu 3 nền tảng”, không ghi “đã đủ
điều kiện” khi chưa có biên bản, tên Skill “ktc-ra-soat-897”: **không tái phát**. Số hiệu, ngày các Thông báo số 924, 1056,
597/TB-CĐKT, Quyết định số 1923, 2119/QĐ-CĐKT giữ đúng. Viết hoa sau dấu hai chấm (Checklist 08 mục 2b — chỉ bắt buộc khi
sau dấu là tên cơ quan, đơn vị, chức danh, văn bản, tên riêng): phần sửa đúng quy ước.

## PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ

- Số liệu trong 4 văn bản khớp tệp nguồn trong hồ sơ: mã SHA-256 bản 1.3.12, 1.3.13; commit `5d98f2b`, `16215a8`; so từng
  tệp 241 / 47 / 3; nghiệm thu đợt 11 (Opus 29/30 lượt, Sonnet 6/6, Haiku 4/6); chi phí trung vị 0,22 USD; ST-01 chặn 5/10;
  25/25 bộ ca thử hồi quy; thử tải 2,7 MB, tối đa 2,3 giây. Các số nghiệm thu được đọc thẳng từ tệp kết quả khi dựng văn bản.
- Lượt trượt được trình bày trung thực: 01 lượt ca 13 (Opus) ghi rõ giám khảo chấm oan nhưng **giữ nguyên kết quả**; Haiku
  trượt 2/2 lượt ca 15 ghi là lỗi của mô hình, kèm khuyến nghị; đợt 10 lỗi hạ tầng ghi không hợp lệ, không xóa.
- Ý kiến không tiếp thu (Gemini 5.1 - 5.5, 5.9) đều có bằng chứng kiểm được (mã nguồn, mã băm, văn bản trong kho, số đo).
- Dự thảo Thông báo: bỏ gắn số phiên bản cài đặt cụ thể; giao việc có chủ thể, nội dung đo được (đo thời gian, chất lượng,
  ghi mô hình; không đổi chức năng trong thí điểm).
- Không có “đảm bảo”, “nhà trường” viết thường sai vị trí trong phần sửa.

## PHẦN IV. BẢNG TỔNG HỢP

| Mức | Số lượng | Đã sửa | Còn lại |
|---|---:|---:|---:|
| Mức 1 | 0 | 0 | 0 |
| Mức 2 | 1 | 1 | 0 |
| Mức 3 | 4 | 4 | 0 |
| Mức 4 | 2 | 0 | 2 (góp ý) |

## PHẦN V. THẨM ĐỊNH CHUYÊN MÔN (NẾU CÓ)

Không có nội dung chuyên môn cần thẩm định riêng trong phần sửa. Kết luận kỹ thuật (dựng lại từ mã nguồn, nghiệm thu) có
tệp bằng chứng trong hồ sơ để bên thẩm định kiểm lại.

## PHẦN VI. ĐÁNH GIÁ TỔNG THỂ

Phần sửa theo thẩm định lần 5 bám đúng ý kiến, có bằng chứng; vấn đề đáng kể nhất là một câu về dữ liệu nội bộ có thể đọc
rộng hơn Dự thảo Thông báo — đã sửa. Bố cục khối chữ ký đã kiểm trên trang thật.

## PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ

- **Không còn vấn đề Mức 1, Mức 2** trong phần sửa của 3 văn bản và toàn văn Báo cáo tiếp thu lần 5.
- 2 góp ý Mức 4 để lần cập nhật sau thí điểm.
- Kết luận chỉ cho phần rà soát nêu trên; điều kiện trình ký Dự thảo Thông báo do người có thẩm quyền quyết định sau cổng G1,
  G2 (Báo cáo tiếp thu lần 5, mục 7).

## KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG

| Mục | Kết quả |
|---|---|
| Phân hệ từng văn bản | Hệ A cả 4 văn bản, có căn cứ |
| Đo byte thật | Đã chạy `ktc897_properties.py`, `kiem_the_thuc.py`, `kiem_vien_dan.py`; xem trang PDF |
| Áp nhầm NĐ 30 cho Đảng, đoàn thể | Không có |
| Pháp luật hết hiệu lực làm khung hiện hành | Không có |
| Finding có bằng chứng, vị trí | Có |
| Metadata, người kiểm tra tự bịa | Không |

## THÔNG TIN TRÁCH NHIỆM

| Mục | Nội dung |
|---|---|
| Nguồn dữ liệu đã dùng | Kho KTC-Database 01 (Nghị định số 334/2026/NĐ-CP), 02 (Phụ lục Quyết định số 2119/QĐ-CĐKT); bộ quy tắc KTC-Ra-Soat-897-v2-Cai-tien (Checklist 01, 02, 04, 05, 08); tệp Track Changes, bản sạch của 3 văn bản và Báo cáo tiếp thu lần 5; tệp kết quả nghiệm thu, bằng chứng dựng lại trong hồ sơ |
| Người kiểm tra | [Người phụ trách Phòng TH-HC&QT — ký xác nhận] |
| Trạng thái phê duyệt | Bản nháp — chờ người có thẩm quyền xem xét |

=== HẾT TỆP N09-PHIEU-RA-SOAT-897-VONG-5.md — MÃ KIỂM: DE08A0 ===
