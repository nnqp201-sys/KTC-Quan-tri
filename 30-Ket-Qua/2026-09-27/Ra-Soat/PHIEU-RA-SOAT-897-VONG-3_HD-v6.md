# PHIẾU RÀ SOÁT KTC-897 — VÒNG 3 (BỔ SUNG, PHẦN SỬA ĐỔI LẦN 3 VÀ LẦN 4)

**Văn bản**: Tài liệu hướng dẫn sử dụng chi tiết Bộ công cụ KTC-Quan-tri (kèm theo Dự thảo Thông báo) — bản 6
**Tệp rà soát**: `30-Ket-Qua/2026-09-27/Ra-Soat/HD_v6_ban-sach_de-ra-soat-vong-3.docx` (bản sạch của `Soan-Thao/HD_…_20260927_v6_TrackChanges.docx`)
**So với**: bản 4 đã qua 2 vòng rà soát (`30-Ket-Qua/2026-09-26/Soan-Thao/HD_…_20260926_v4_TrackChanges.docx`) và phiếu `PHIEU-RA-SOAT-897-VONG-{1,2}_HD-v4.md`
**Công cụ**: Skill `ktc-ra-soat-897:review` (Core v3.0 + baseline v2.24)
**Căn cứ tổ chức rà soát**: điểm b Mục 8 Thông báo số 1056/TB-CĐKT ngày 16/9/2026 — vòng bổ sung cho phần sửa sau 2 vòng
**Ngày rà soát**: 27/9/2026 · Phần sửa theo phiếu thực hiện bằng Track Changes, tác giả “Rà soát 897 vòng 3 (Claude)”

---

## PHẦN I. THÔNG TIN CHUNG

| Mục | Nội dung |
|---|---|
| Loại văn bản | Tài liệu hướng dẫn kèm theo Thông báo (không có số, ký hiệu riêng) |
| Hệ quy chiếu | **Hệ A** (tài liệu kèm văn bản hành chính của Trường); các yếu tố kỹ thuật (bảng màu, tên lệnh) được chấp nhận tại vòng 1, 2 |
| Phạm vi (so sánh từng đoạn, từng ô) | 14 vị trí: bìa (phiên bản, ngày); mục lục và tiêu đề mục 6 Phần III; ô “Kỹ năng”, ô “Thao tác tự động” bảng Phần II; đoạn thí điểm sau bảng “Lưu ý về độ tin cậy”; đoạn tệp cài đặt; đoạn kiểm tra đầu phiên; đoạn xử lý khi bị chặn; khối kết quả và mã cảnh báo; đoạn kết luận trái nhau; mục “Sử dụng tiết kiệm lưu lượng” (5 đoạn); đoạn nhật ký Phần IX; chân trang |
| Nguồn kho đã đọc | TB 1056/TB-CĐKT (Mục 7, 8); TB 924/TB-CĐKT (bản gốc); TB 948/TB-CĐKT (bản gốc) |
| Đo thể thức (byte thật) | Chữ ký ZIP hợp lệ, 1 section, A4, lề 20/20/30/20 mm; `kiem_the_thuc.py`: 0 lỗi Mức 1–2, còn TT05 (chữ màu tiêu đề bảng), TT11 (số trang ở chân trang) — Mức 3, có từ bản 3, đã chấp nhận ở vòng 2 (tài liệu hướng dẫn kỹ thuật); `kiem_vien_dan.py`: 0 lỗi |
| Track Changes | 16 đánh dấu (14 “Tiếp thu thẩm định lần 4”, 2 “Rà soát 897 vòng 3”) |

## PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT

| Mã | Vị trí | Bằng chứng | Vấn đề | Căn cứ | Mức | Kiến nghị | Xử lý |
|---|---|---|---|---|---|---|---|
| M2-01 | Đoạn sau bảng “Lưu ý về độ tin cậy theo nền tảng” | “dữ liệu nội bộ, dữ liệu cá nhân chỉ xử lý trên nền tảng đã có biên bản nghiệm thu …” | Như M2-01 phiếu Thông báo: có thể đọc thành nới rộng so với TB 924 | TB 924; Mục 7 TB 1056 | 2 | Giới hạn “(trong phạm vi được phép theo Thông báo số 924/TB-CĐKT ngày 11/8/2026)” | **Đã sửa** |
| M2-02 | Cùng đoạn | “(Claude Code đã có kết quả nghiệm thu với dữ liệu giả lập)” | Đặt ngay sau điều kiện “đã có biên bản nghiệm thu” nên dễ hiểu là Claude Code **đã đủ điều kiện** xử lý dữ liệu thật; thực tế chưa nền tảng nào có biên bản, và thẩm định lần 4 chưa đồng ý dữ liệu nội bộ | Checklist 02 (logic, không gây hiểu sai); báo cáo thẩm định lần 4 | 2 | “(hiện chưa nền tảng nào có biên bản; Claude Code mới có kết quả kiểm thử với dữ liệu giả lập)” | **Đã sửa** |
| M3-01 | Cùng đoạn (sau sửa M2-01) | “Thông báo số 924/TB-CĐKT” | Lần nhắc đầu trong Tài liệu hướng dẫn chưa kèm ngày ban hành | Checklist 08 (số hiệu nội bộ kèm ngày) | 3 | Thêm “ngày 11/8/2026” | **Đã sửa** |
| M4-01 | Đoạn xử lý khi bị chặn | “ghi sản phẩm vào thư mục kết quả” | Chưa rõ “thư mục kết quả” với người dùng tài khoản Team (không có thư mục dự án) | Checklist 04 | 4 | Có thể thêm “(thư mục làm việc của đơn vị, ngoài kho)” | Giữ nguyên — góp ý cho lần cập nhật sau |
| M4-02 | Mục “Sử dụng tiết kiệm lưu lượng” | “mỗi lần gửi, Claude đọc lại toàn bộ cuộc hội thoại và các tệp đã đính kèm” | Diễn đạt giản lược cơ chế ngữ cảnh; đúng về hệ quả với người dùng | Checklist 04 | 4 | Giữ nguyên | Giữ nguyên |

### II.1. Kiểm lại vấn đề vòng 1, 2 trong phần bị sửa

Tên công cụ rà soát (Skill “ktc-ra-soat-897”), dấu hiệu máy thiếu Python, tài khoản cá nhân: **không tái phát**. Tiêu đề mục 6
Phần III đổi đồng thời ở mục lục tĩnh và thân văn bản — khớp nhau.

## PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ

- Mô tả thao tác chặn ghi, nhật ký nhất quán với Dự thảo Thông báo bản 7 và mã nguồn plugin 1.3.2.
- Hướng dẫn xử lý khi kết quả không có khối trạng thái (kỹ năng chưa kích hoạt) — rõ, có hành động cụ thể.
- Quy tắc khi kỹ năng, tác tử, rà soát 897 kết luận trái nhau giữ nguyên chốt “còn Mức 1 thì chưa trình ký”.
- Tách rõ plugin Claude với việc dùng tài liệu kỹ năng trên ChatGPT, Gemini (không có tác tử, thao tác tự động).

## PHẦN IV. BẢNG TỔNG HỢP

| Mức | Số lượng | Đã sửa | Còn lại |
|---|---:|---:|---:|
| Mức 1 | 0 | 0 | 0 |
| Mức 2 | 2 | 2 | 0 |
| Mức 3 | 1 | 1 | 0 |
| Mức 4 | 2 | 0 | 2 (góp ý) |

## PHẦN V. THẨM ĐỊNH CHUYÊN MÔN (NẾU CÓ)

Không có nội dung chuyên môn cần thẩm định riêng trong phần sửa đổi.

## PHẦN VI. ĐÁNH GIÁ TỔNG THỂ

Phần sửa đổi rõ, đúng mục đích tiếp thu. Hai vấn đề Mức 2 đều ở cùng một đoạn (phạm vi dữ liệu trong thí điểm) — đã sửa để
không nới rộng quá TB 924 và không gây hiểu nhầm về điều kiện của Claude Code.

## PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ

**Kết luận:** Phần sửa đổi lần 3, lần 4 **không còn vấn đề Mức 1, Mức 2** sau khi sửa theo phiếu. Phiếu không kết luận thay
điều kiện ban hành của hồ sơ.

Thứ tự xử lý: (1) người soạn xem 16 đánh dấu; (2) cân nhắc 2 góp ý Mức 4 ở lần cập nhật sau; (3) đính kèm phiếu vòng 1–3.

## KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG

- Hệ A; đo byte DOCX có; finding Mức 2 có nguồn, vị trí, trích nguyên văn; không bịa metadata — đạt.
- Viết hoa sau dấu hai chấm trong phần sửa: “Khi kết luận trái nhau: kết luận…”, “(… : từ 1.3.1; …)” — sau dấu hai chấm không
  phải tên cơ quan, chức danh, văn bản → không bắt buộc viết hoa (Checklist 08 mục 2b) — đạt.

## THÔNG TIN TRÁCH NHIỆM

| Trường | Nội dung |
|---|---|
| Nguồn dữ liệu đã dùng | TB 1056/TB-CĐKT (kho 02); TB 924, 948/TB-CĐKT (bản gốc người dùng cung cấp); Checklist 02, 04, 07, 08; bản 4 đã qua 2 vòng; phiếu vòng 1, 2 |
| Người kiểm tra | ……………………… (Phòng TH-HC&QT — người được giao kiểm tra, ký xác nhận) |
| Trạng thái phê duyệt | Bản nháp — chờ người có thẩm quyền xem xét |
