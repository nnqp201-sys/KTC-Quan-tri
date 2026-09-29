# PHIẾU RÀ SOÁT KTC-897 — VÒNG 3 (BỔ SUNG, PHẦN SỬA ĐỔI LẦN 3 VÀ LẦN 4)

**Văn bản**: Dự thảo Thông báo hướng dẫn sử dụng bộ công cụ trí tuệ nhân tạo (plugin) trong xây dựng kế hoạch, báo cáo định kỳ và quản trị nhiệm vụ (KTC-Quan-tri) — bản 7
**Tệp rà soát**: `30-Ket-Qua/2026-09-27/Ra-Soat/TB_v7_ban-sach_de-ra-soat-vong-3.docx` (bản sạch của `Soan-Thao/TB_…_20260927_v7_TrackChanges.docx`)
**So với**: bản 5 đã qua 2 vòng rà soát (`30-Ket-Qua/2026-09-26/Soan-Thao/TB_…_20260926_v5_TrackChanges.docx`, đã chấp nhận thay đổi) và phiếu `PHIEU-RA-SOAT-897-VONG-{1,2}_TB-v5.md`
**Công cụ**: Skill `ktc-ra-soat-897:review` (Core v3.0 + baseline v2.24; đã nạp `00-RUNTIME-INVARIANTS` → `10-…-v3-Core` → `20-…-v2.24-BASELINE`)
**Căn cứ tổ chức rà soát**: điểm b Mục 8 Thông báo số 1056/TB-CĐKT ngày 16/9/2026 — vòng bổ sung cho phần sửa sau 2 vòng, theo đề nghị của thẩm định độc lập lần 3, lần 4 (ChatGPT, Grok)
**Ngày rà soát**: 27/9/2026 · Tệp gốc **không bị sửa** trong khi rà soát; phần sửa theo phiếu được thực hiện sau đó bằng Track Changes, tác giả “Rà soát 897 vòng 3 (Claude)”

---

## PHẦN I. THÔNG TIN CHUNG

| Mục | Nội dung |
|---|---|
| Loại văn bản | Thông báo (`/TB-CĐKT`), số, ngày để trống (giai đoạn dự thảo); người ký: Hiệu trưởng |
| Hệ quy chiếu | **Hệ A** (NĐ 30/2020/NĐ-CP, TB 597/TB-CĐKT, Checklist 08). Phần sửa không làm thay đổi hệ |
| Phạm vi (đo bằng so sánh văn bản từng đoạn, từng ô) | 6 đoạn: I.1.b gạch 1 (gọi đích danh kỹ năng khi làm báo cáo); I.1.b gạch 3 (thao tác tự động, phiên bản, thao tác chặn ghi); I.3.a (dữ liệu trong giai đoạn thí điểm); Lưu ý I.3 (phiên bản 1.3.2); III.1.b (phân quyền chỉ đọc); III.1.d (thí điểm, báo cáo hậu thí điểm). Căn cứ, trích yếu, Mục II, Nơi nhận **không đổi** |
| Nguồn kho đã đọc | TB 1056/TB-CĐKT ngày 16/9/2026 (`02-KTC-Regulations/1056-TB-CDKT_…_v1.docx`) — Mục 7 (bảo mật dữ liệu), Mục 8 (hồ sơ, thẩm định); TB 924/TB-CĐKT ngày 11/8/2026 (bản gốc người dùng cung cấp 27/9/2026, `10-Dau-Vao/09-Chua-Phan-Loai/`) — quy định dữ liệu không được đưa vào Claude AI; TB 948/TB-CĐKT ngày 17/8/2026 (bản gốc) |
| Nguồn chưa có trong kho | TB 917, 924, 948 chưa nạp vào kho 02 (đề xuất bổ sung tại `30-Ket-Qua/2026-09-27/De-Xuat-Kho/`); đã đối chiếu bản gốc ngày 27/9/2026, khớp số, ngày, trích yếu |
| Đo thể thức (byte thật) | `ktc897_properties.py`: chữ ký ZIP `504b0304` hợp lệ, 1 section, A4 210×297 mm, lề 20/20/30/20 mm; `kiem_the_thuc.py`: đạt các phép kiểm TT/TX; `kiem_vien_dan.py`: 0 lỗi VD01–VD12 |
| Track Changes | Tệp có vết `Soan-Thao/TB_…_v7_TrackChanges.docx`: 12 đánh dấu (10 “Tiếp thu thẩm định lần 4”, 2 “Rà soát 897 vòng 3”), nền là bản người phụ trách đã chấp nhận thay đổi lần 3 |

## PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT

| Mã | Vị trí | Bằng chứng (nguyên văn bản rà soát) | Vấn đề | Căn cứ | Mức | Kiến nghị | Xử lý |
|---|---|---|---|---|---|---|---|
| M2-01 | I.3.a, câu cuối | “Trong giai đoạn thí điểm, dữ liệu nội bộ, dữ liệu cá nhân chỉ được xử lý trên nền tảng đã có biên bản nghiệm thu và sau khi kho KTC-Database đã được phân quyền chỉ đọc” | Câu có thể hiểu là **cho phép** đưa dữ liệu nội bộ, dữ liệu cá nhân vào Claude khi đủ hai điều kiện, rộng hơn TB 924 (điểm 2, 3 phần quy định sử dụng: không đưa thông tin cá nhân nhạy cảm, tài liệu nội bộ chưa được phép công bố; xử lý ẩn danh khi cần) và Mục 7 TB 1056 | TB 924/TB-CĐKT; Mục 7 TB 1056/TB-CĐKT; Checklist 02 (thống nhất với văn bản đã ban hành) | 2 | Giới hạn phạm vi: “(trong phạm vi được phép theo Thông báo số 924/TB-CĐKT)” | **Đã sửa** (Track Changes) |
| M3-01 | I.1.b gạch 3 | “…trên Claude Cowork và Claude Code, từ phiên bản 1.3.2: tự kiểm tra phiên bản; …” | “từ phiên bản 1.3.2” gắn cho cả danh sách thao tác tự động, trong khi nhiều thao tác có từ trước (tự kiểm tra phiên bản, đo thể thức) — sai lệch thông tin | Checklist 02 (chính xác nội dung) | 3 | “(đầy đủ từ phiên bản 1.3.2)” | **Đã sửa** |
| M3-02 | I.1.b gạch 3 | “chặn cả thao tác không xác định được nơi ghi nhưng có dấu hiệu ghi vào kho” | Diễn đạt tự mâu thuẫn (“không xác định nơi ghi” nhưng “ghi vào kho”) | Checklist 04 (rõ nghĩa) | 3 | “chặn cả lệnh có nhắc tới kho, có dấu hiệu ghi nhưng không xác định được nơi ghi” | **Đã sửa** |
| M3-03 | III.1.d | “Tổ chức thí điểm, kiểm thử Bộ công cụ trên 3 nền tảng…” | I.3.a đặt điều kiện “biên bản nghiệm thu” nhưng Mục III chưa giao ai lập biên bản | Checklist 07 — Thông báo: rõ ai làm gì | 3 | Bổ sung “lập biên bản nghiệm thu trên từng nền tảng có đại diện Phòng TCCB&CTHSSV và đơn vị thí điểm” | **Đã sửa** |
| M3-04 | III.1.d | “sau mỗi kỳ thí điểm, báo cáo số phiên sử dụng…” | Chưa nêu báo cáo gửi ai | Checklist 07 | 3 | “báo cáo Lãnh đạo Trường” | **Đã sửa** |
| M4-01 | III.1.d | “tỷ lệ kích hoạt đúng kỹ năng” | Thuật ngữ kỹ thuật khó hiểu với người đọc hành chính | Checklist 04 | 4 | “tỷ lệ Bộ công cụ chọn đúng kỹ năng” | **Đã sửa** |
| M4-02 | III.1.b | “thư mục biểu mẫu chuẩn” | Có thể nêu tên thư mục (03-Templates(1), 04-Good-Documents) như Tài liệu hướng dẫn | Checklist 04 | 4 | Tùy người soạn; giữ nguyên chấp nhận được (Tài liệu hướng dẫn đã nêu tên) | Giữ nguyên |

### II.1. Kiểm lại vấn đề của vòng 1, vòng 2 trong phần bị sửa

Các vấn đề vòng 1, 2 đã đóng tại các đoạn bị sửa (tên công cụ rà soát theo TB 1056; tài khoản cá nhân; dấu hiệu máy thiếu
Python) — kiểm lại nguyên văn bản 7: **không tái phát**. Câu về máy thiếu Python nay nhất quán với Tài liệu hướng dẫn bản 6
(“chỉ đọc, soạn nháp, không để AI ghi, sửa tệp”).

## PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ

- Mô tả thao tác chặn ghi đúng bản chất (biện pháp hỗ trợ; phân quyền chỉ đọc là biện pháp chính) — không còn tuyên bố tuyệt đối.
- Phiên bản, điều kiện không phân phối bản cũ (1.3.1 trở về trước) nhất quán giữa I.1.b và Lưu ý I.3.
- Giao trách nhiệm phân quyền chỉ đọc cho Phòng TH-HC&QT (đơn vị quản lý kho theo TB 948) — đúng thẩm quyền quản lý kho.
- Viết tắt tên đơn vị trong hành văn đúng cột phải bảng 3.4 Checklist 08 (“Phòng TH-HC&QT”, “Phòng TCCB&CTHSSV”).
- Không phát sinh căn cứ mới; không có số liệu mới cần kiểm.

## PHẦN IV. BẢNG TỔNG HỢP

| Mức | Số lượng | Đã sửa | Còn lại |
|---|---:|---:|---:|
| Mức 1 | 0 | 0 | 0 |
| Mức 2 | 1 | 1 | 0 |
| Mức 3 | 4 | 4 | 0 |
| Mức 4 | 2 | 1 | 1 (giữ nguyên, chấp nhận được) |

## PHẦN V. THẨM ĐỊNH CHUYÊN MÔN (NẾU CÓ)

Không có nội dung chuyên môn cần thẩm định riêng trong phần sửa đổi (nội dung kỹ thuật của Bộ công cụ đã qua 4 vòng thẩm định
độc lập; phiếu này không thay kết luận của các vòng đó).

## PHẦN VI. ĐÁNH GIÁ TỔNG THỂ

Phần sửa đổi lần 3, lần 4 đúng thể thức Hệ A, không phát sinh căn cứ mới. Vấn đề đáng kể duy nhất (M2-01) là câu về dữ liệu
khi thí điểm có thể đọc thành nới rộng so với TB 924 — đã giới hạn lại. Sau sửa, phần thay đổi nhất quán với Tài liệu
hướng dẫn bản 6 và các văn bản đã ban hành (TB 924, TB 948, TB 1056).

## PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ

**Kết luận:** Phần sửa đổi lần 3, lần 4 của Dự thảo Thông báo **không còn vấn đề Mức 1, Mức 2** sau khi sửa theo phiếu.
Điều kiện trình ký của toàn văn bản vẫn theo các phiếu vòng 1, 2 và các điều kiện của hồ sơ (nghiệm thu Claude, Cowork;
biên bản phân quyền chỉ đọc; kiểm kê cấp tổ chức) — phiếu này **không** kết luận văn bản đủ điều kiện ban hành.

Thứ tự xử lý: (1) người soạn xem, chấp nhận hoặc từ chối 12 đánh dấu trong bản Track Changes; (2) đính kèm phiếu vòng 1, 2, 3
vào hồ sơ trình ký.

## KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG

- Hệ quy chiếu: Hệ A, không áp nhầm hệ khác — đạt.
- Đo byte DOCX: có (ktc897_properties, kiem_the_thuc) — đạt.
- Finding Mức 2 có nguồn, vị trí, trích nguyên văn — đạt.
- Không dùng pháp luật hết hiệu lực; không bịa metadata — đạt.
- Viết hoa sau dấu hai chấm (Checklist 08 mục 2b) trong phần sửa: không có trường hợp phải viết hoa — đạt.

## THÔNG TIN TRÁCH NHIỆM

| Trường | Nội dung |
|---|---|
| Nguồn dữ liệu đã dùng | TB 1056/TB-CĐKT (kho 02); TB 924, 948/TB-CĐKT (bản gốc người dùng cung cấp 27/9/2026); Checklist 02, 04, 07, 08 (KTC-Ra-Soat-897-v2-Cai-tien); bản 5 đã qua 2 vòng; phiếu vòng 1, 2 |
| Người kiểm tra | ……………………… (Phòng TH-HC&QT — người được giao kiểm tra, ký xác nhận) |
| Trạng thái phê duyệt | Bản nháp — chờ người có thẩm quyền xem xét |
