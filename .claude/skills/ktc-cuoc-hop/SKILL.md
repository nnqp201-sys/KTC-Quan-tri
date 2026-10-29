---
name: ktc-cuoc-hop
description: Xử lý cuộc họp góp ý, giao ban của Trường Cao đẳng Kon Tum, từ ghi âm, ghi chép tay, bản tóm tắt do AI khác lập (Gemini, NotebookLM...) đến Biên bản họp và Báo cáo tiếp thu, giải trình của Tổ xây dựng Đề án. Lập một bảng ý kiến có đối chiếu nguồn rồi sinh trọn bộ văn bản. Dùng khi người dùng gửi tệp ghi âm (.m4a, .mp3, .wav), dán ý kiến cuộc họp, nhắc "biên bản cuộc họp", "kết luận của Hiệu trưởng", "trả lời các ý kiến", "tiếp thu, giải trình".
---
# Quy trình

Quy ước nền: `.claude/rules/24-de-an.md`, mục 12–14.

1. **Thu nguồn.** Gồm ghi âm, ghi chép của anh và bản tóm tắt của AI khác. Mỗi nguồn ghi rõ là gì, ai lập.
2. **Chép ghi âm** (nếu có): `python 29-Cong-Cu/chep_ghi_am.py <thu_muc_ra> <tệp...>`, chạy nền, khoảng 30–40 phút cho 20 phút ghi âm.
   - Lần đầu phải cài thư viện và mô hình (khoảng 1,6 GB). **Hỏi anh trước khi cài.**
   - Ghi âm hội trường chỉ nghe ra khoảng 30%. Bản chép **chỉ để kiểm**, không làm nguồn duy nhất.
   - Bản chép có dấu thời gian `[mm:ss]` để tra lại.
3. **Lập bảng ý kiến** `bang-y-kien_<ma>.yaml` theo mẫu `29-Cong-Cu/cuoc_hop/mau-bang-y-kien.yaml`.
   - Mỗi ý ghi: `nguon` (ghi_am / ghi_chep / tom_tat_ai), `doi_chieu` (khop / lech / chi_1_nguon), `xu_ly` (TT / GT / KTT) và `tra_loi`.
   - Kết luận của chủ trì để ở một nhóm riêng.
   - Đối chiếu bản tóm tắt AI với **chính văn bản**: bảng số liệu, Tờ trình, Phụ lục. Ví dụ năm cuối giai đoạn phải khớp Bảng 7.
4. **Dừng, hỏi anh** một lần bằng câu hỏi chọn phương án:
   - mọi ý `lech`;
   - mọi ý `chi_1_nguon` thuộc kết luận của chủ trì;
   - con số mà ghi âm không nghe ra.
   Anh giao người khác xác định thì ghi đúng như vậy ("giao khoa … xác định"), không tự đặt số.
5. **Sinh trọn bộ:**
   - Chép mẫu bằng các **lệnh riêng** (hook guard chặn lệnh vừa nhắc kho vừa ghi):
     - `kiem_the_thuc.py --tao <kho>/03-Templates(1)/09-Bien-ban.dotx <ra>/_mau_09.docx`
     - `Copy-Item` BC 344/BC-CĐKT (kho 05, Đề án Đăng kiểm lần 3) thành `<ra>/_mau_bc344.docx`
   - Chạy `python 29-Cong-Cu/cuoc_hop/sinh_bo_van_ban.py <bang.yaml> <ra>/_mau_09.docx <ra>/_mau_bc344.docx <ra>`.
   - Biên bản: Trường ban hành, ký Thư ký + Chủ trì. BC tiếp thu: Tổ ban hành, ký "TM. Tổ – Tổ trưởng".
6. **Kiểm:**
   - `kiem_the_thuc.py` từng tệp, 0 lỗi Mức 1–2.
   - Xem PDF trang đầu và trang cuối (`rap_mau.xuat_pdf`, `rap_mau.chup_trang`): khối chữ ký, trang trắng, đường kẻ.
7. **Giao:**
   - Báo các ô còn "…" mà script liệt kê, và các ý `chi_1_nguon` còn `CAN_XAC_MINH`.
   - Không ghi đè tệp anh đã sửa tay; bản mới đặt hậu tố.
   - Cập nhật `29-Cong-Cu/de_an/de-an_<ten>.yaml` (mục `hop_gop_y`, `viec_mo`).
