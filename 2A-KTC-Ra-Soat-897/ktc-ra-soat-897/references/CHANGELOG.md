# CHANGELOG – Skill ktc-ra-soat-897

## v4.6.13-KTC – 07/11/2026 (bản bổ sung cá nhân – sửa cổng hồ sơ C1–C6, UTF-8 subprocess)

Bản này sửa 6 tình huống chặn sai của cổng hồ sơ và lỗi mã hóa UTF-8, **không nằm trong lõi chính thức** của P-QLKHCN&HTPT.

### A. Lỗi mã hóa UTF-8 subprocess (ưu tiên 1)
- `tao_bao_cao.py`, `kiem_ke_ho_so.py`, `kiem_tra_the_thuc.py`: thêm `sys.stdout.reconfigure(encoding='utf-8', errors='replace')` ngay đầu script.
- Mọi `subprocess.run(..., text=True)` trong `tools/` thêm `encoding='utf-8', errors='replace'`.
- Nguồn byte `0xcd`: trang mã Windows cp1252 của PowerShell/cmd.exe khi in tiếng Việt.

### C1. Phụ lục trong văn bản kèm theo
- Dự thảo nhắc "Phụ lục N" mà văn bản vai trò `kem_theo` có tiêu đề "Phụ lục N" → coi là đủ.
- `kiem_ke_ho_so.py`: thêm `pl_trong_kem` = phụ lục từ `phu_luc_tieu_de()` của tệp `kem_theo`.

### C3. VBHN của Thông tư, Nghị định (không chỉ Luật)
- Mở rộng nhận diện VBHN cho Thông tư, Nghị định, Quyết định (trước đó chỉ nhận Luật).
- Gán `vbhn_key` cho tham chiếu theo số (ví dụ "Thông tư số 14/2025/TT-BXD").

### C4. Ngày VBHN trong bảng chữ ký
- `nhan_dien_chung.py`: thêm `docx_tables_text()` đọc text từ mọi bảng trong tệp docx.
- `thong_tin_vbhn()`: nếu không tìm thấy ngày trong đoạn văn, tìm trong bảng (mẫu "XÁC THỰC VĂN BẢN HỢP NHẤT — Hà Nội, ngày …").

### C5. "pháp luật" trong trích yếu
- Pattern VBHN dùng negative lookbehind `(?<![pP]háp )` để không bắt "luật" trong "pháp luật về giao thông đường bộ".

### C6. Tên văn bản sau dấu chấm phẩy
- Pattern tìm TẤT CẢ tên văn bản trong phần trước "(hợp nhất tại ...)" rồi lấy CÁI CUỐI CÙNG (gần nhất với VBHN).
- Ví dụ: "Nghị định 60/2021/NĐ-CP; khoản 5 Điều 54 Luật Quản lý..." → lấy "Luật Quản lý...".

### Bộ ca kiểm thử
- 5 ca mới C1, C3, C4, C5, C6 tại `30-Ket-Qua/2026-11-07/Lenh/fixtures-cong-897/` — mã thoát mong đợi 0.
- Ca đối chứng chưa tạo (chờ phần F của lệnh).

### Nhóm 6 sub-agent điều phối 897
- Mô tả tại `2A-KTC-Ra-Soat-897/00-README.md` mục "Nhóm 6 sub-agent".
- Đường dẫn: `.claude/agents/ktc-897-*.md`.

## v4.6.12 – 06/11/2026 (sửa lỗi L5 của Báo cáo kiểm lại độc lập v4.6.11; chỉ sửa lỗi này)
- **L5** `tools/track_changes.py`, `xac_minh`: tác giả Comment cũ không còn được dùng để miễn kiểm tác giả của dấu sửa mới (lỗi phát sinh từ bản sửa L2 của v4.6.11). Nay chỉ dấu sửa đã có trong bản gốc (khớp loại `w:ins`/`w:del` + `w:id` + tác giả, đếm cả số lần) và Comment đã có trong bản gốc (khớp id + tác giả) được giữ tên cũ; mọi dấu sửa/Comment khác phải mang tên “KTC Rà soát 897 (AI)”. Trường mới `tac_gia_sai` liệt kê dấu sửa/Comment sai tác giả. Tập tác giả cũ (dấu sửa ∪ Comment) chỉ còn dùng cho `tac_gia_cu_giu`.
- SKILL.md Bước 8 mục 4: ghi quy tắc trên.
- Bộ ca: thêm **L5** (X10, theo `bang_chung/x10_tac_gia_comment_cu.py`): đổi tác giả 1 dấu sửa mới thành “Nguyễn Văn B” (người viết Comment cũ) → `xac-minh` mã 1, `tac_gia_dung = False`; đối chứng bản giao đúng → mã 0. 36 mục: 35 ca cũ giữ 29 đạt · 6 một phần · 0 không đạt; L5 đạt. `x10_tac_gia_comment_cu.py` trên v4.6.11 → mã 0 (KHÔNG ĐẠT), trên v4.6.12 → mã 1 (ĐẠT). `tc_phong_phu.py` có Comment cũ: 16/16; `doi_khang.py`: 28/30 (D3, E5 như trước, ngoài phạm vi).
- Phiên bản dữ liệu: kết quả cổng/đo/so sánh phải do v4.6.12 tạo.

## v4.6.11 – 06/11/2026 (sửa 4 lỗi L1–L4 của Báo cáo nghiệm thu độc lập Bước 3 v4.6.10; chỉ sửa 4 lỗi này)
- **L1** `tools/tao_bao_cao.py`, `DAU_HIEU_CHU_DE['AI']`: thêm trợ lý ảo, chatbot, Claude, A.I., học máy; mẫu “AI” nhận “GenAI”. Mẫu phân biệt hoa/thường nay viết trong `(?-i:…)` và mọi mẫu tìm với `re.I` (bỏ phép so chuỗi mẫu ở `phat_hien_chu_de`): “ai/mai/hai/Ai” tiếng Việt không bị bắt. **Ngoài danh sách được giao:** (1) “học máy” loại trừ “học máy tính” để không bắt nhầm môn tin học; (2) “Claude” chỉ khớp nguyên từ. Không thêm từ nào khác. Ca L1 (A1–A3 → mã 3; đối chứng “ai” viết thường + “học máy tính” → mã 0).
- **L2** `tools/track_changes.py`, `xac_minh`: tập tác giả cũ = tác giả dấu sửa cũ ∪ tác giả Comment cũ của bản gốc. Ca L2 (T5, có và không có Comment cũ → ĐẠT, mã 0).
- **L3** `ap_dung`, `xac_minh` (hàm mới `doc_sua`): tác giả luôn “KTC Rà soát 897 (AI)”; `sua.json` ghi `tac_gia` khác → từ chối, mã thoát 2, không tạo tệp. Ca L3 (X8 “Lê Trí Khải”, “Hiệu trưởng”, tên có khoảng trắng thừa → từ chối; ghi đúng tên → nhận). Ca 18 đổi cách dựng bản gốc có dấu cũ của người khác (đổi tên tác giả trong XML của bản tạm) vì `tac_gia` khác không còn được nhận.
- **L4** `track_changes.py main`: `xac-minh` mã thoát 1 khi “KHÔNG ĐẠT”, 0 khi “ĐẠT (cấu trúc XML)”. SKILL.md Bước 4 mục 2 bỏ câu “script không tự nhận chủ đề”, ghi cho khớp Bước 7 mục 5 (script tự nhận dấu hiệu chủ đề AI); Bước 8 mục 4–5 và `tools/README.md` ghi mã thoát, quy tắc tác giả. Ca L4.
- Bộ ca: 35 mục – 31 ca cũ giữ 25 đạt · 6 một phần · 0 không đạt; 4 ca mới L1–L4 đạt (và đều KHÔNG ĐẠT khi chạy trên v4.6.10). Chạy lại `bang_chung/doi_khang.py`: A1–A3 nay đạt; D3, E5 vẫn như bản nghiệm thu (ngoài phạm vi). `tc_phong_phu.py` có Comment cũ: 16/16.
- Phiên bản dữ liệu: kết quả cổng/đo/so sánh phải do v4.6.11 tạo.

## v4.6.10 – 06/11/2026 (theo quyết định của Hiệu trưởng sau Work lần 4)
- Hiệu trưởng quyết định (06/11/2026): **bỏ hẳn miễn nguồn theo chủ đề, không cần xác nhận**. Mọi dự thảo có dấu hiệu chủ đề AI (nội dung hoặc dẫn chiếu QĐ 2307/2328/2487/2520) mà `chu_de` không khai AI → bắt buộc phủ nguồn AI, không có đường giải trình. `chu_de_giai_trinh` còn trong dữ liệu → báo “không còn hiệu lực” (chưa hoàn tất, mã 3). Cờ `--xac-nhan-mien-nguon` bị bỏ. Cách này đóng triệt để lỗ hổng Work lần 4 (không còn phụ thuộc từ khóa/cấu trúc đoạn).
- Bộ ca P3: d3–d6 (đoạn kể hợp lệ về hình thức, “bố trí trợ lý AI”, tiêu đề, câu của Work) đều → mã 3; d7 cờ cũ bị từ chối; d8 khai chủ đề đầy đủ vẫn hoàn tất.
- Đã chuyển v4.6.9 (có cờ xác nhận) thành lịch sử; v4.6.10 thay thế.

## v4.6.9 – 06/11/2026 (sửa theo Ý KIẾN THẨM ĐỊNH ĐỘC LẬP LẦN 4 của Work; Work KHÔNG thẩm định lần 5 – chuyển Bước 3 nghiệm thu)
- Lỗi chính (Work lần 4): danh sách từ khóa mệnh lệnh để lọt “Điều 1. Mỗi đơn vị bố trí một trợ lý AI.” và tiêu đề “Triển khai trợ lý AI trong toàn Trường” (từ “bố trí” không có trong danh sách) → báo cáo hoàn tất dù chỉ đối chiếu QĐ 1976/2073. Sửa theo hướng CẤU TRÚC, không thêm từ khóa:
  * `doan_chi_nhac_duoc_xet` (tools/tao_bao_cao.py): chỉ đoạn văn kể/nêu sự việc (câu hoàn chỉnh ≥ 40 ký tự, kết thúc bằng dấu câu, không phải tiêu đề/“V/v”/Điều/Khoản/Mục/gạch đầu dòng/đề mục viết hoa) mới được xét miễn; tiêu đề, điều khoản, gạch đầu dòng, đề mục → luôn phải phủ nguồn chủ đề. Kiểm từ khóa mệnh lệnh giữ lại như lớp thứ hai.
  * `--xac-nhan-mien-nguon CHỦ_ĐỀ=HỌ_TÊN`: ngoại lệ miễn nguồn chủ đề CHƯA có xác nhận của người dùng (họ tên trùng `nguoi_xac_nhan`) → không hoàn tất, mã 3. AI KHÔNG được tự đặt cờ này; phải hỏi người dùng sau khi đưa các đoạn trích. Phụ lục A in trạng thái xác nhận.
- Ca 24: thiếu soffice/pdftotext hoặc lỗi chạy công cụ → “CHƯA KIỂM – thiếu công cụ” (không còn FileNotFoundError; tách lỗi công cụ khỏi lỗi tài liệu).
- Bộ ca P3: d5a (không cờ → 3), d5b (có cờ đúng tên → hoàn tất, Phụ lục A in xác nhận), d5c (cờ sai tên → 3), d6 (ca của Work → 3), d7 (hàm cấu trúc). 
- Giới hạn còn lại: chính sách miễn nguồn và dung sai hiển thị chờ Hiệu trưởng; Word chưa kiểm đầu/chân trang, trường PAGE, ảnh, đánh số, tác giả Comment, ca 21 tình huống thật, ca 24 trang.

## v4.6.8 – 06/11/2026 (sửa theo Ý KIẾN THẨM ĐỊNH ĐỘC LẬP LẦN 3 của Work; CHƯA nghiệm thu)
- `giai_trinh_chu_de_hop_le`: bỏ phép chứa-một-phần; `doan_trich` phải trùng NGUYÊN ĐOẠN với mọi đoạn có dấu hiệu (không thừa, không thiếu); thêm `nguoi_xac_nhan`; đoạn có từ ngữ điều chỉnh/cho phép việc dùng AI (được, không được, phải, sử dụng, hỗ trợ, soạn thảo…) bị từ chối – vẫn phải phủ nguồn chủ đề dù không dẫn chiếu số QĐ (câu của Work “Viên chức được sử dụng hệ thống AI…” nay → mã 3). Giới hạn: danh sách từ khóa là biện pháp thận trọng, có thể chặn cả đoạn chỉ nhắc AI; khi đó khai `chu_de` và phủ nguồn.
- Báo cáo in ngoại lệ miễn nguồn ở Phụ lục A (chủ đề, nguồn bị loại, lý do, đoạn căn cứ, người xác nhận); Skill không xác nhận lý do miễn là đúng.
- Bằng chứng Word gắn tệp: mỗi `caNN.json` khai `tep` {tên: SHA-256}; bộ ca chỉ nhận khi trùng tệp đóng gói tại `tests/ket_qua/word/tep/` (đã đóng gói 10 tệp thử). Ca 15, 17 (bằng chứng cũ không có SHA) hạ về “CHƯA KIỂM phần Word”.
- Ca 19 hạ “ĐẠT MỘT PHẦN” (tệp thử không có đầu/chân trang, trường, ảnh, đánh số). Ca 21: chạy Word Compare trên hai tệp chỉ khác lề – Word báo 1 revision định dạng, KHÔNG phải 0; tình huống “Compare = 0 nhưng ảnh khác” chưa tái hiện → ca 21 “ĐẠT MỘT PHẦN”; Skill vẫn không có so ảnh/dung sai (hoãn theo Hiệu trưởng).
- Bộ ca P3 thêm 7 tình huống hàm giải trình, ca đầu cuối cho câu của Work (mã 3) và ca miễn hợp lệ có in Phụ lục A.


## v4.6.7 – 06/11/2026 (sửa theo Ý KIẾN THẨM ĐỊNH ĐỘC LẬP LẦN 2 của Work; CHƯA nghiệm thu)
- `chu_de_giai_trinh.<chủ đề>` phải là đối tượng `{ly_do ≥ 20 ký tự, doan_trich: […]}` trích nguyên văn mọi đoạn có dấu hiệu; chuỗi trần bị từ chối; dự thảo có dẫn chiếu QĐ AI thì không được miễn (`giai_trinh_chu_de_hop_le`).
- Nhật ký phạm vi: mục ngoài nguồn bắt buộc có `da_doc` ≠ `toan_van` phải có `loai_tru` {ngoai_pham_vi, ly_do ≥ 20}; `toan_van` mà còn `phan_chua_doc` thật là mâu thuẫn (mọi mục).
- `--xac-nhan-phu-luc`: trích bằng chứng phải là tiêu đề phụ lục thật (bắt đầu “Phụ lục X”, không phải ghi chú phủ định/dự kiến/giả định, có đoạn nội dung theo sau); kết quả ghi vị trí và SHA-256 nguồn.
- Tự ghép bản dự thảo (Hiệu trưởng duyệt 06/11/2026): chỉ khi CẢ HAI bản có đơn vị và ký hiệu số trùng và “Dự thảo lần N” khác nhau; thiếu một trong hai → hỏi một lần (`khong_ro`).
- `track_changes.kiem_comment`: so mốc neo ở trạng thái Reject (sửa hợp lệ trong cùng đoạn không bị coi là Comment di chuyển).
- Khóa bộ đệm: bỏ ghi nhớ `_MA_KHO`, băm lại Kho mỗi lần gọi.
- Word thật (06/11/2026 11:41–11:45): ca 14, 18 (Reject theo tác giả), 20 đạt; ca 18 cho thấy Reject All mọi tác giả cũng bỏ dấu cũ của người khác; ca 21 (Word Compare) đạt trên tệp kiểm nhỏ, ca 19 đạt hạn chế (tệp không có đầu/chân trang, trường); ca 24 chưa kiểm.
- Bộ ca: thêm P5 (nguồn ngoài bắt buộc), P6 (sửa + Comment cùng đoạn), mở rộng P2/P3/P4/c12. Chưa kiểm trong Word thật: ca 18–21, hiển thị.

## v4.6.6 – 06/11/2026 (sửa theo Ý KIẾN THẨM ĐỊNH ĐỘC LẬP của Work ngày 06/11/2026; CHƯA nghiệm thu)
Work kết luận v4.6.5 chưa nên sang Bước 3 (16 đạt, 6 một phần, 1 chưa kiểm, 2 không đạt khi Work chạy lại). Các lỗi kỹ thuật đã tái hiện và sửa (không cần quyết định chính sách):
- `danh_gia_hoan_tat`: chủ đề không còn chỉ dựa vào khai báo – nhận dấu hiệu chủ đề AI từ nội dung dự thảo và dẫn chiếu QĐ 2307/2328/2487/2520 (`phat_hien_chu_de`), chưa khai thì vẫn buộc phủ nguồn AI trừ khi có `chu_de_giai_trinh`; `da_doc = toan_van` mà `phan_chua_doc` còn nội dung → chưa hoàn tất (mọi mục nhật ký, kể cả nguồn không bắt buộc).
- Khóa bộ đệm (`_ma_ham_chay`) băm NỘI DUNG toàn bộ tệp Kho và quy tắc, không chỉ manifest; lỗi tạo thư mục tạm trong `_chay_json` được bắt và chẩn đoán.
- `track_changes.xac_minh`: kiểm Comment cũ (id, tác giả, nội dung, mốc neo), Comment mới (nội dung, tác giả, đúng đoạn neo), không Comment thừa; xóa/sửa Comment → KHÔNG ĐẠT.
- `phan_loai_phu_luc`: nhận “được ban hành kèm theo / đã được ban hành tại / đính kèm Quyết định số X”, dẫn chiếu trải đến 3 đoạn.
- Quan hệ giữa các bản dự thảo: so thêm đơn vị ban hành và ký hiệu số (`dau_co_quan`, `quan_he_van_ban`); khác đơn vị → không tự ghép bản cũ–mới. Quy tắc “cùng nội dung” trong mã: tập từ trích yếu (bỏ từ chung) của văn bản ngắn hơn nằm trọn trong văn bản dài hơn và chiếm ≥ 50% (không phải “trùng ≥ 50%” đơn thuần); ngưỡng 50% là lựa chọn kỹ thuật của người sửa, chưa có căn cứ từ văn bản nào – chờ ý kiến.
- `--xac-nhan-phu-luc`: phải kèm trích nguyên văn tiêu đề phụ lục (sau “||”) có trong văn bản chủ quản, ghi đoạn tìm thấy; thừa nhận phụ lục không tồn tại/dẫn chiếu sai bị từ chối.
- Bộ thử: ca 11 không còn phụ thuộc /proc (Linux); ca 14, 18 thêm ca xóa Comment; ca 12 viết lại; thêm ca P1–P4; nhãn “đạt” ca 24 thu hẹp theo phạm vi thực kiểm.
- Đã được Hiệu trưởng quyết định ngày 06/11/2026: (1) phạm vi tự ghép phiên bản như nêu ở mục “Quan hệ giữa các bản dự thảo” (cùng loại, trích yếu, đơn vị, ký hiệu số và có “Dự thảo lần N” khác nhau trong nội dung; còn lại hỏi một lần); (2) dẫn chiếu sai/phụ lục không tồn tại: giữ chặn, không thêm đường gỡ bằng xác nhận; (3) dung sai hiển thị: hoãn đến khi có kết quả kiểm Word thật.
- Việc CÒN MỞ (không khẳng định): nguyên nhân treo 900 giây; Word Compare, Accept/Reject trong Word cho ca 18–20, dựng trang bằng Word; phán đoán nội dung ca 10; dấu hiệu chủ đề chỉ có cho AI. Còn chờ Hiệu trưởng: dung sai hiển thị (hoãn đến khi có kết quả kiểm Word thật).
- Phiên bản dữ liệu: kết quả cổng/đo/so sánh phải do v4.6.6 tạo.

## v4.6.5 – 06/11/2026 (cập nhật theo QĐ 2520/QĐ-CĐKT 05/11/2026 và yêu cầu của Work 05/11/2026; đã chạy bộ ca kiểm thử – xem hồ sơ bàn giao; Hiệu trưởng đã duyệt ba quy tắc mới ngày 06/11/2026)
- QĐ 2520 (Điều 1 kh. 1–3, Điều 2): Kho v4.4 thêm QĐ 2520, ghi chú “đã được sửa đổi” ở QĐ 2307/2328/2487; SKILL.md Lưu ý bảo mật; Bước 4.2 thêm QĐ 2520 vào nguồn bắt buộc chủ đề AI; Bước 3A thủ tục văn bản sửa đổi (YC mục 5).
- YC 1: phụ lục của văn bản được dẫn thuộc văn bản đó (`phan_loai_phu_luc`, `phu_luc_thuoc_van_ban_khac`); không đòi trong hồ sơ, không thay phụ lục của văn bản khác.
- YC 2: định danh dự thảo/lần rà soát bằng nội dung (`dinh_danh_van_ban`, `quan_he_dinh_danh`); tên tệp chỉ cảnh báo; hỏi một lần.
- YC 3–4: tách dữ liệu hợp lệ / hoàn tất rà soát (`danh_gia_hoan_tat`), mã thoát 3, “Chưa đủ cơ sở đánh giá”, `kieu_bao_cao: tien_do`, nhật ký phạm vi và Phụ lục A/B, Phần I dòng 11–12.
- YC 6: `kiem_moi_truong`, `--thu-muc-lam-viec`, chẩn đoán theo bước, bộ đệm theo mã băm, dựng trang bằng Word khi thiếu LibreOffice (cần thử trên máy có Word).
- YC 7: `--xac-nhan-phu-luc` / `--nguoi-xac-nhan` ghi vào kết quả cổng.
- YC 9: Bước 8 và `tools/track_changes.py`.
- Đã được Hiệu trưởng duyệt ngày 06/11/2026: (1) cụm “Chưa đủ cơ sở đánh giá”; (2) tác giả dấu sửa “KTC Rà soát 897 (AI)”; (3) việc chặn dựng báo cáo chính thức khi chưa hoàn tất.
- Phiên bản dữ liệu: kết quả cổng/đo/so sánh phải do v4.6.5 tạo.

## v4.6.4 – 03/11/2026 (v4.6.3 + quyết định Q1–Q5 của người phụ trách ngày 03/11/2026; tự kiểm của người sửa; Hiệu trưởng phê duyệt chính thức ngày 03/11/2026)
- Q1: chủ đề AI – ma trận đối chiếu luôn gồm thêm QĐ 2487/QĐ-CĐKT (SKILL Bước 4.2, checklist, chỉ mục Kho). Người rà soát thực hiện; script không tự nhận chủ đề nên không ép buộc (chỉ ép QĐ 1976, 2073 như trước).
- Q2: đối chiếu Danh mục AI (QĐ 2487) bằng mã sẵn có, không mã mới: ngoài/trái Danh mục → DC-01; rộng hơn (loại dữ liệu, nhóm người dùng, phạm vi) → DC-03; tên công cụ/nhà cung cấp/mức rủi ro khác Danh mục (ví dụ “NotebookLM”) → DC-06; đều Mức 2, Mức 1 nếu trái pháp luật/văn bản cấp trên (SKILL Bước 4 mục 4; 02-Quy-Tac-Xep-Muc DC-06).
- Q3: lưu ý bảo mật (SKILL.md, 05-Cong-Ho-So, 29-Skill-Van-Ban-Dang) dẫn thêm QĐ 2487 – Claude thuộc Danh mục (mục 2), dữ liệu theo Phụ lục I QĐ 2307, gói tổ chức Team/Enterprise.
- Q4: Kho v4.3 bổ sung Luật An ninh mạng 116/2025/QH15, Luật Giáo dục nghề nghiệp 124/2025/QH15, Luật Trí tuệ nhân tạo 134/2025/QH15 (cùng ngày 10/12/2025; tệp do người phụ trách cung cấp, đã kiểm số, ngày, toàn văn có Điều) – 01-Legal-Database, text/, kho_manifest.json, chỉ mục. Không đưa luật cũ vào danh sách “đã bị thay thế” (Luật 74/2014/QH13 hết hiệu lực có ngoại lệ chuyển tiếp) – chưa đổi quy tắc CC-01.
- Q5: cổng `--xac-nhan-toan-van "<tệp>=<lý do>"` cho văn bản nguồn rất ngắn mà cổng không xác định được thân (05-Cong-Ho-So mục 2e); không dùng được cho tệp chỉ có định danh + một đoạn trích yếu; ghi JSON, I.7 chữ đỏ; trình dựng tính lại với tham số này.
- Phiên bản dữ liệu: kết quả cổng/đo/so sánh phải do v4.6.4 tạo (JSON v4.6.3 chạy lại).
- Câu chữ Q3 được THÊM thành câu riêng, giữ nguyên câu cũ (dữ liệu báo cáo cũ trích nguyên văn quy tắc Skill vẫn khớp – ca hồi quy F03-03).
- Kỹ thuật: các công cụ không ghi `__pycache__` vào thư mục Skill (`sys.dont_write_bytecode` trước khi nạp mô-đun dùng chung); `--xac-nhan-toan-van` thiếu “=” → CHẶN, nêu cách ghi.

## v4.6.3 – 03/11/2026 (BẢN SỬA HOÀN THIỆN sau nghiệm thu độc lập lần 3 – đã TỰ KIỂM của người sửa; KHÔNG phải nghiệm thu độc lập; CHƯA được duyệt phát hành, CHƯA cài)
Căn cứ: Tóm tắt nghiệm thu độc lập lần 3 (v4.6.2 CHƯA ĐẠT – giữ nguyên kết luận); phiếu quyết định D1–D11 ngày 02/11/2026 (đã ký xác nhận bổ sung 03/11/2026); chỉ dẫn đợt sửa hoàn thiện 03/11/2026 (không tổ chức nghiệm thu lần 4; thực hiện D2, D10). Số 4.6.3 chỉ là nhãn kỹ thuật.
Thay đổi có chủ đích của hợp đồng (dữ liệu cũ phải chạy lại – xem `Hop_dong_du_lieu_va_thay_doi_tuong_thich.md` trong hồ sơ bàn giao):
- D2: `--kho` khác Kho của gói → cổng CHẶN; trình dựng từ chối JSON cổng ghi Kho ngoài gói (trước: cảnh báo chữ đỏ). Cách viết tương đương của chính Kho gói được nhận.
- D10: tác vụ so sánh – vị trí phía dự thảo dùng đối chiếu trích dẫn phải ghi tên tệp đúng bản; xác định tệp trước, kiểm Điều/phần/chương trong tệp đó (giao thoa D5/D10).
- Phiên bản dữ liệu: kết quả cổng/đo/so sánh phải do v4.6.3 tạo (bảng so sánh nay cũng kiểm phiên bản).
Lỗi cài đặt đã sửa:
- Mục 1 (F01/F02/F06): đọc mọi JSON có kiểm soát – kích thước, độ sâu lồng, số nguyên quá lớn, số thực vô hạn/NaN, khóa lặp, ký tự điều khiển/nửa cặp thay thế (trước: Traceback ở trình dựng, kể cả nhánh dựng .docx); chuỗi số chỉ chữ số ASCII (trước: “²” vỡ int()); lỗi nêu đường dẫn trường và giới hạn; chú thích `_vi_du…` lồng trong giới hạn vẫn dùng được.
- Mục 2 (D6/F04): kiểm TẤT CẢ định danh trong dòng dẫn – số hiệu không thuộc tệp đã ghi tên, tên luật thứ hai (kể cả tên lồng nhau “Luật Giáo dục nghề nghiệp và Luật Giáo dục”), tên luật chỉ khớp phần đầu → từ chối; đồng nghĩa thật (tệp + số hiệu của chính nó, tên luật + số của chính luật đó) được nhận. Khóa so tên tệp cùng chuẩn trình bày với dòng dẫn.
- Mục 3 (N12/F08): quy tắc cấu trúc mới cho trích yếu và thân văn bản (`05-Cong-Ho-So.md` mục 2d) – độ dài, căn lề, dấu câu, một cụm mở đầu không còn một mình kết luận có thân; khối căn cứ, “QUYẾT ĐỊNH:”, Nơi nhận, chữ ký không tính là thân. `.xlsx` đọc theo hàng.
- Mục 4 (F11): trình dựng dùng kết quả tính lại của cổng/đo/so sánh; tên/đường dẫn bản cũ – mới trong JSON so sánh phải đúng tệp thật của mã băm (sửa tên, trỏ tệp khác, đảo tên → từ chối); II.D in tên tệp như cổng ghi; lỗi tiến trình con có chẩn đoán.
- Mục 5: trường bắt buộc có nội dung kiểm sau chuẩn hóa khoảng trắng (zero-width, NBSP, U+3000…): `ten_du_thao`, `loai_van_ban`, `don_vi_soan_thao`, `nguoi_kiem_tra`, `chua_kiem[i].noi_dung/ly_do`, `uu_tien[i]`, các trường bắt buộc của phát hiện, ma trận, đối chiếu, hồi quy, xem ảnh, kiểm tra chất lượng, `yeu_cau_doc_lap`.
- Tệp kết quả: `-o`/`--json`/`--md` không được trùng tệp đầu vào/hồ sơ (trước: có thể ghi đè dự thảo), thư mục phải có, ghi qua tệp tạm; `--json` không ghi được → thông báo, mã 2 (trước: Traceback). Tệp .docx hỏng/không có ở `kiem_tra_the_thuc.py`, `so_sanh_ban.py` → lỗi có kiểm soát.
- D3 (độ ổn định): LibreOffice dùng hồ sơ người dùng riêng cho mỗi lần dựng trang (trước: dùng chung → xung đột với phiên đang mở/tiến trình song song → tính lại khác → từ chối nhầm).
Kho dữ liệu (v4.2 – 03/11/2026): bổ sung QĐ 2487/QĐ-CĐKT ngày 03/11/2026 ban hành Danh mục các hệ thống trí tuệ nhân tạo (AI) được phép sử dụng trong hoạt động của nhà trường (Phụ lục 10 công cụ) – tệp `02-KTC-Regulations/QD-2487-QD-CDKT-Danh-muc-he-thong-AI-duoc-phep-su-dung.docx`, bản chữ `text/`, mục `kho_manifest.json`, chỉ mục `00-Chi-Muc-Metadata.md`. Không thêm quy tắc kiểm mới theo QĐ 2487 (các câu hỏi gửi người phụ trách ghi trong hồ sơ bàn giao).
Giữ nguyên (không đổi nghiệp vụ): D1, D3, D4, D5, D6, D7, D8, D11; QĐ-5, QĐ-7, KTS-25; không kiểm khoản/điểm; Điều đánh số tự động chỉ ghi “chưa kiểm được vị trí Điều”. F11 KHÔNG ghi là đã đóng: `tham_so` sửa tay và người có quyền sửa gói vẫn ngoài khả năng kiểm (D1).

## v4.6.2 – 02/11/2026 (ỨNG VIÊN KỸ THUẬT sau nghiệm thu độc lập lần 2 – CHƯA nghiệm thu, CHƯA phát hành, CHƯA cài)
Căn cứ: Tóm tắt nghiệm thu độc lập lần 2 (v4.6.1 CHƯA ĐẠT; F01–F13). Số phiên bản 4.6.2 chỉ là nhãn kỹ thuật, không phải quyết định ban hành. Không đổi quy tắc nghiệp vụ đã chốt (N12, N46, N31, N32, N33, VBHN, KTS-18, QĐ-5, QĐ-6, QĐ-7).
- F01, F02 (trình dựng): mô-đun mới `tools/kiem_kieu_du_lieu.py` – hợp đồng kiểu cho mọi trường dữ liệu báo cáo (kể cả đối tượng lồng, phần tử danh sách), kiểm TRƯỚC mọi xử lý; sai kiểu → “DỮ LIỆU BÁO CÁO CHƯA HỢP LỆ”, báo đường dẫn trường (chỉ số đếm từ 1) và kiểu hợp lệ, mã thoát 1, không dựng tệp; JSON hỏng/thiếu tệp → từ chối có kiểm soát. `mo_ta`, `kien_nghi`… không phải chuỗi bị từ chối. Quy ước null tạm thời (F12 – chờ quyết định): trường đơn null = không có; danh sách/đối tượng null = lỗi, trừ `chua_kiem`.
- F03, F04, F05, F09 (trình dựng): dòng dẫn phải chỉ tới MỘT nguồn. Tên tệp (như cổng ghi, đường dẫn tuyệt đối, tệp quy tắc `references/…md`) được nhận trước và bỏ khỏi dòng dẫn trước khi rút số hiệu – “02-Quy-Tac-Xep-Muc.md” không còn bị hiểu là số hiệu; từ chối: hai nguồn trở lên (“A hoặc B”, “A, B”, hai số hiệu), tên ngắn trùng nhiều tệp (đề nghị ghi đường dẫn), tên tệp không có trong hồ sơ, tệp sai vai trò (vị trí dự thảo ghi tệp văn bản liên quan; căn cứ ghi tệp dự thảo), dòng dẫn chỉ ghi chung (“quy tắc”, “KTC”, “bảng thông số”, “references/”). Tệp gộp trùng nội dung (N46) là một nguồn. Không ghi tên tệp ở vị trí dự thảo → giữ hành vi tìm trên các tệp dự thảo/văn bản kèm theo.
- F06 (trình dựng): kiểm khóa dành cho script ở MỌI cấp, kể cả bên trong `_vi_du_…`, `_ghi_chu`, `_huong_dan`; chú thích hợp lệ vẫn được nhận.
- F07 (trình dựng): bề rộng cột tối thiểu theo từ dài nhất không bẻ được (STT, mã, “Mức n”); hàng tiêu đề cột giữ cùng hàng dữ liệu đầu; chỉ cấm tách hàng khi hàng vừa một trang; đoạn đệm sau bảng 1 pt (hết trang cuối chỉ có số trang). I.7 in đủ đường dẫn tệp gộp, tham số chạy cổng, ghi chú cổng nguyên văn. Kiểm bằng LibreOffice; CHƯA kiểm bằng Microsoft Word.
- F08 (cổng): trích yếu nhiều đoạn (tối đa 4) sau tên loại được nhận theo cấu trúc (không dấu hiệu thân, không kết thúc bằng dấu câu, không in hoa, không canh đều) – tệp chỉ có định danh + trích yếu hai, ba dòng → CHẶN (N12). Ngưỡng 30 ký tự giữ nguyên (vấn đề mở).
- F10 (trình dựng): nhận nhiều Điều trên một dòng dẫn (“Điều 1 và Điều 2”, “Điều 1, 3”, “từ Điều 2 đến Điều 4”); văn bản có nhiều phần (Quyết định + Quy chế/Quy định kèm theo, Phụ lục) và Chương được phân vùng; “Quy chế, Điều 2”, “Chương II, Điều 5” kiểm đúng phần/chương; Điều lặp ở nhiều phần mà dòng dẫn không ghi phần → từ chối “mơ hồ”; tên văn bản chính (“Quyết định…”) chỉ dùng để phân biệt khi số Điều lặp. Điều đánh số tự động: giữ “chưa kiểm được vị trí Điều”. Khoản, điểm vẫn không kiểm (vấn đề mở D).
- F11 (cổng, đo, so sánh, trình dựng): `kiem_ke_ho_so.py` ghi `tham_so` (đường dẫn tuyệt đối, tác vụ, vòng, `--vai-tro`, `--du-thao`, `--xac-nhan-kem`, Kho, thư mục chạy); `kiem_tra_the_thuc.py` ghi `tham_so`; `tao_bao_cao.py` CHẠY LẠI cổng, đo thể thức, so sánh từ tệp thật với tham số đã ghi và từ chối khi JSON khác kết quả tính lại. Không dùng checksum tự khai hay khóa bí mật. Ranh giới tin cậy mới (tham số chạy là đầu vào hợp lệ, in ở I.7; `--kho` khác mặc định chỉ được cảnh báo) CHỜ người phụ trách quyết định.
- Phiên bản dữ liệu: kết quả cổng/đo phải do v4.6.2 tạo; phiên bản khác → dừng ngay (không xử lý tiếp).

## v4.6.1 – 02/11/2026 (bản sửa sau nghiệm thu độc lập lần 1 – CHƯA nghiệm thu lại, chưa cài thay bản chính thức)
Căn cứ: Báo cáo nghiệm thu độc lập v4.6 ngày 02/11/2026 (kết luận CHƯA ĐẠT, 57/69 ca; 12 ca chưa đạt); quyết định của người phụ trách cùng ngày về N12, N46, N31, N32.
- N07, N09 (cổng): `--vai-tro`, `--du-thao`, `--xac-nhan-kem` kiểm và áp dụng cùng một bộ phân giải (đường dẫn tuyệt đối, khoảng trắng ngoài tên).
- N12 (cổng – quyết định 02/11/2026): tệp nguồn chỉ có phần định danh, không có thân văn bản → CHẶN (cả VBHN); tiêu chí cấu trúc, ngưỡng 30 ký tự chỉ là điều kiện phụ tạm thời.
- N46 (cổng – quyết định 02/11/2026): gộp tệp trùng phần nội dung (bỏ metadata), ghi đủ đường dẫn; khác chữ vẫn MƠ HỒ.
- N34 (cổng): `--kiem-moi-truong` chạy được không cần đường dẫn (đúng lệnh trong README, SKILL.md).
- N20, N21 (trình dựng): đoạn trích nguồn đối chiếu với đúng văn bản dòng dẫn chỉ tới (tên tệp, số hiệu, tên luật, quy tắc Skill), tên tệp phải mang số hiệu ghi kèm, và nằm trong Điều đã ghi; phía dự thảo theo vị trí; dòng dẫn không chỉ ra văn bản → từ chối; văn bản đánh số Điều tự động → ghi “chưa kiểm được vị trí Điều”. “Khớp – có điều khoản thay thế” cần `vblq_thay_the`.
- N24 (trình dựng): phát hiện thiếu `ma` → từ chối có thông báo, không vỡ chương trình.
- N25 (trình dựng): dữ liệu người nhập không được đặt khóa bắt đầu “_” (dành cho script: `_nguon`, `_ss`…), trừ chú thích `_huong_dan`, `_ghi_chu`, `_vi_du_…`.
- N31 (trình dựng – quyết định 02/11/2026): danh mục mã cũ từ bảng Phần II của báo cáo lần trước (`<Mã>#<STT>`) hoặc mã `M<số>-<số>`; phủ hai chiều; không nhận ra mã → không dùng ĐC.
- N32, N33 (trình dựng – quyết định 02/11/2026): `che_do` chỉ ĐL/ĐC; ĐL ở lần ≥ 2 phải có `yeu_cau_doc_lap` (≥ 20 ký tự, in ở I.7).
- I.7 ghi việc dùng VBHN thay Luật gốc và các tệp đã gộp (nhận xét của nghiệm thu).
- Phiên bản dữ liệu: kết quả cổng/đo phải do v4.6.1 tạo (có `dinh_danh`).

## v4.6 – 02/11/2026 (bản sửa – CHƯA nghiệm thu độc lập, chưa cài thay bản chính thức)
Căn cứ: Báo cáo kiểm toán độc lập Skill ktc-ra-soat-897 ngày 01/11/2026 (28 mã KTS-01…28); phát hiện mới ở Giai đoạn 0 (PH-01, PH-02); phát hiện bổ sung F-X; quyết định của người phụ trách ngày 02/11/2026:
- Quy tắc VBHN (xác nhận bằng lời trong phiên làm việc, chưa có văn bản): luật có VBHN chỉ cần 01 VBHN khớp số, ngày, luật được hợp nhất; VBHN khác hoặc cũ hơn không thỏa; ghi việc thay thế, nguồn và giới hạn (`Quy-Tac-KTC/04` mục 5).
- KTS-18: DC-02 được Mức 1 khi trái pháp luật/văn bản cấp trên.
- Giữ nguyên: CC-01 cho dạng rút gọn cùng loại (KTS-12 F09); không đưa `--dinh-danh` của bản rời v4.5.2 (KTS-27).

F-X: kết luận SAI qua nhật ký 2 lần chạy (02/11/2026) – lần chạy có VBHN 115 trong hồ sơ, cổng khớp đúng; không sửa riêng. Hiện tượng chặn 2251/319 ở lần đầu tái hiện được khi số hiệu có khoảng trắng trình bày → xử lý chung ở KTS-01.

Thay đổi theo từng điểm:
- KTS-01 (Cao): mô-đun mới `tools/nhan_dien_chung.py` – chuẩn hóa số, ký hiệu chịu khoảng trắng thường/không ngắt/zero-width/xuống dòng, quanh “/” và “-”; Unicode theo thuộc tính ký tự; chứng cứ giữ nguyên văn gốc.
- KTS-02 (Cao): Kho chỉ tính có toàn văn khi tệp có thật và đọc được chữ; mục “Phụ lục …” không thay văn bản chính.
- KTS-03 (Cao), PH-01: nhiều ứng viên khác nội dung → “MƠ HỒ”, CHẶN; tên luật khớp đúng, không khớp tiền tố; tên luật ở tiêu đề tệp luật ghép tối đa 3 dòng in hoa, bỏ đoạn trống.
- KTS-04 (Cao): so sánh hai bản – một tệp kèm theo riêng chỉ đáp ứng một văn bản kèm theo của MỘT bản (không dùng chung giữa hai bản); phụ lục được nhắc trong tệp kèm theo riêng cũng phải có (kiểm đệ quy). Hai bản thật sự dùng chung một tệp kèm theo thì phải nộp hai bản sao – cơ chế khai báo dùng chung chưa làm (chờ quyết định).
- KTS-05 (Cao): ghép phụ lục, văn bản kèm theo 1:1 tối ưu (không phụ thuộc thứ tự); trích yếu giữ chữ số.
- KTS-06 (TB): nhận lần rà soát theo tên tệp không phân biệt dấu; “lần 10” không nhầm “lần 1”.
- KTS-07 (TB): kiểm đầu vào – đường dẫn, `--vai-tro`, `--du-thao`, `--xac-nhan-kem` sai thì dừng, báo lỗi.
- KTS-08 (TB): cổng đọc căn lề theo kế thừa kiểu (style, docDefaults) khi nhận vai trò tệp theo dòng canh giữa.
- KTS-09 (TB): đo cả đoạn trong `w:sdt`; TT-20 xét mọi run có chữ.
- KTS-10 (TB): vùng đầu văn bản gồm các dòng ngắn ngoài bảng trong 15 đoạn đầu; nhãn “Nơi nhận:” văn bản Đảng cỡ 14, đứng, gạch chân.
- KTS-11 (TB): không dựng được trang → TT-32/36/37 “chưa kiểm”; mục Đạt ghi rõ là cấu hình XML.
- KTS-12 (TB): F08 – CC-01 dạng rút gọn chỉ khớp cùng loại văn bản; F09 giữ quy tắc hiện hành.
- KTS-13 (Cao): đối chiếu mọi đoạn trích (phát hiện Mức 1–2 do AI lập, ma trận kể cả yeu_to_khop, mục Đạt, đối chiếu) với chữ của tệp thật.
- KTS-14 (TB): ma trận chính thức/so sánh phải có QĐ 1976, QĐ 2073.
- KTS-15 (TB): `kieu_bao_cao` phải khớp tác vụ cổng; cổng chuẩn hóa không lập báo cáo.
- KTS-16 (Cao): chế độ ĐC bắt buộc du_thao_cu, `--so-sanh` đúng cặp bản; mã cũ phải có trong báo cáo lần trước.
- KTS-17 (TB): “Chưa kiểm” trọng yếu ở I.8 (`trong_yeu`) tính vào nhãn.
- KTS-18 (TB): DC-02 cho phép Mức 1 (quyết định 02/11/2026).
- KTS-19 (Cao): trùng vị trí theo cấu trúc (Phụ lục/Chương/Mục/Điều/khoản/điểm/đoạn, tên tệp); kiểm cả dòng “Khớp – có điều khoản thay thế”.
- KTS-20 (TB): mức chỉ nhận 1/2/3; trường bắt buộc; phát hiện trùng bị từ chối ngay ở `--chi-kiem`.
- KTS-21 (Cao): tính lại mã băm từ tệp thật (cổng ghi `duong_dan`) – tệp sửa sau cổng bị từ chối.
- KTS-22 (TB): ngày tài liệu chỉ lấy ở dòng địa danh – ngày hợp lệ.
- KTS-23 (TB): thiếu pdftotext → CHẶN vì lỗi môi trường; thêm `--kiem-moi-truong`.
- KTS-24 (TB): thống nhất phiên bản v4.6 ở SKILL.md, README, script; trình dựng từ chối kết quả cổng/đo của phiên bản khác.
- KTS-25: chưa đủ căn cứ – không sửa (cần ý kiến pháp lý).
- KTS-26 (Cao): một cách nhận diện tiêu đề văn bản kèm theo (in hoa theo thuộc tính Unicode, không giới hạn độ dài) cho tệp dự thảo và tệp riêng.
- KTS-27: không đưa `--dinh-danh` (chưa có căn cứ).
- KTS-28 (Thấp): bảng trong báo cáo có hàng tiêu đề lặp lại, không tách dòng qua trang; đề mục đậm giữ cùng trang với đoạn sau.
- PH-02: quy tắc VBHN 02/11/2026 (số, ngày, luật được hợp nhất).
- Tự kiểm trên Kho: bỏ việc gộp tiền tố tên luật làm sót “Luật Giáo dục nghề nghiệp”, “Luật Giáo dục quốc phòng và an ninh”, “Luật Đầu tư công”; bỏ tên luật bị cắt (“Luật Khám bệnh”); tên luật yếu kéo dài qua “và” viết thường.

Tương thích dữ liệu cũ: kết quả cổng v4.5 thiếu `duong_dan`, `phien_ban` v4.6 → trình dựng từ chối; chạy lại ba script của cùng gói. Dữ liệu báo cáo v4.5 dùng lại được nếu nguyên văn trích đúng chữ tệp thật, có `kiem_tra_chat_luong`, mức là 1/2/3.

## v4.5 – 27/10/2026
Căn cứ: 2 báo cáo phản biện lần 5 (ChatGPT 6 điểm PB5-GPT-01…06; Work 17 điểm PB5-WORK-01…17 – cả hai chạy thử) và báo cáo tổng hợp, kiểm chứng của Claude ngày 27/10/2026 (18 vấn đề độc lập sau khi gộp 5 cặp trùng, đều tái hiện được trên v4.4); 2 quyết định của Hiệu trưởng ngày 27/10/2026:
- F1 – Văn bản kèm theo cùng tên loại nhưng trích yếu không khớp hoặc không có, người rà soát xác định đúng là văn bản kèm theo: cho xác nhận bằng --xac-nhan-kem "<tệp>=<lý do ≥ 20 ký tự>"; cổng ĐỦ, kết quả cổng và báo cáo I.7 ghi “xác nhận thủ công”; khác tên loại thì vẫn CHẶN; --vai-tro chỉ sửa vai trò.
- F2 – Ô “Khớp” mà script thấy dấu hiệu khác nhau (số – đơn vị theo thứ tự, phủ định, trái nghĩa) nhưng AI đọc nghĩa vẫn khớp: cho ghi Khớp kèm giai_trinh_khop ≥ 20 ký tự cho đúng yếu tố đó; giải trình in ở Bảng 3.

Thay đổi theo từng điểm:
- PB5-GPT-01, PB5-WORK-02 (A11), PB5-WORK-08 (Cao): tệp kèm không có trích yếu không tự khớp; --vai-tro kem_theo không còn bỏ kiểm khớp; xác nhận thủ công theo F1.
- PB5-GPT-02, PB5-WORK-02 (A13) (Cao): ghép 1:1 – một tệp chỉ đáp ứng một văn bản kèm theo; khớp trích yếu: từ có nghĩa của bên này nằm trọn trong bên kia.
- PB5-WORK-03 (Cao): câu liệt kê nhiều văn bản kèm theo (“Quy định A và Quy chế B”) được tách, kiểm từng văn bản.
- PB5-WORK-02 (A22, A25) (Cao): từ phủ định phải có ở cả hai bên; văn bản kèm theo của văn bản đã ban hành ghi tắt (“Kèm theo QĐ 1355/QĐ-CĐKT…”) là văn bản liên quan.
- PB5-GPT-05 (TB): trích yếu viết tắt – xử lý theo F1 (xác nhận thủ công có kiểm, có ghi).
- PB5-WORK-01 (Cao): viện dẫn rút gọn khóa theo loại (“RG:Nghị định:9090/2026”); chỉ nhận toàn văn cùng loại; hai viện dẫn rút gọn khác loại cùng số được kiểm riêng.
- PB5-WORK-04 (Cao): định danh tệp trùng tên theo thư mục gốc chung của mọi đầu vào (nhiều thư mục, nhiều tệp).
- PB5-GPT-04, PB5-WORK-05 (Cao): la_cau_thay_the (hai script) không miễn câu nêu việc thay thế mà phần còn lại vẫn “áp dụng/tiếp tục áp dụng/thực hiện/căn cứ”.
- PB5-WORK-06 (Cao): bo_qua_the_thuc – “tep” phải chỉ đúng MỘT tệp đã đo (tên như cổng ghi; tên ngắn chỉ nhận khi duy nhất), áp cùng một quy tắc khi kiểm và khi loại.
- PB5-WORK-07 (Cao): câu một dòng đậm/nghiêng trong thân văn bản vẫn đo; chỉ miễn tên đề mục ngay dưới “Chương/Mục/Phần” hoặc dòng trích yếu ngay dưới tên loại in hoa.
- PB5-WORK-09 (TB): phụ lục chữ thật ngắn có biểu trưng nhỏ không bị chặn; chỉ chặn khi có ảnh ≥ 1/4 trang.
- PB5-WORK-10 (TB): trích yếu sau “BÁO CÁO” là các dòng canh giữa; dừng cả ở dấu chấm phẩy.
- PB5-WORK-11 (TB): vùng Nơi nhận chỉ gồm dòng danh sách, chức vụ, “(…)”, họ tên – dừng ở câu lời văn, kể cả câu ngắn.
- PB5-WORK-12 (TB): TT-19 khi nhãn “Nơi nhận” thiếu dấu hai chấm, khi danh sách nơi nhận có chữ nghiêng (văn bản chính quyền).
- PB5-WORK-13 (TB): bảng chỉ bị coi là bảng Nơi nhận – chữ ký khi có ô bắt đầu bằng “Nơi nhận:” hoặc quốc hiệu; bảng có cột “Nơi nhận hồ sơ” vẫn ghi “chưa kiểm”.
- PB5-WORK-14 (TB): vị trí ghi tên tệp là một phần của vị trí (khác tệp không trùng vị trí); tác vụ so sánh: dòng ma trận phải ghi tên tệp.
- PB5-GPT-03, PB5-WORK-15 (Cao/TB): kiểm “Khớp” theo dãy (số, đơn vị) theo thứ tự (bỏ số dẫn Điều/khoản, năm; “năm ngày” = 5 ngày), phủ định theo từng vế, cặp trái nghĩa; khác biệt → từ chối hoặc giải trình theo F2.
- PB5-WORK-16 (TB): so_sanh_ban.py ghi mã băm hai tệp; tao_bao_cao.py chỉ nhận bảng thay đổi của đúng hai bản đã qua cổng.
- PB5-WORK-17 (TB): đo TT-17 cho trích yếu công văn “V/v” (cỡ 13, in thường, đứng), trong hoặc ngoài bảng.
- PB5-GPT-06 (Thấp): sửa chú thích cũ (ngưỡng 100 ký tự) trong kiem_tra_the_thuc.py.
- Điểm Work ghi “đáng ngờ”: “Khớp – có điều khoản thay thế” nay ghi nguyen_van_thay_the thay cho yeu_to_khop; tab đếm theo điểm dừng tab riêng của đoạn (hoặc mặc định 1,27 cm).
- Phát hiện khi tự kiểm trên Kho: chữ trong run ở dạng tổ hợp (NFD) làm nhãn “Nơi nhận:” bị tính vào danh sách nơi nhận (TT-19 “cỡ 12” báo oan ở QĐ 1976, QĐ 2307, QĐ 969, QĐ 1355, TB 597) và bỏ sót kiểm nhãn (QĐ 2073 nhãn cỡ 11) – đã chuẩn hóa NFC trước khi so.

Kết quả hồi quy v4.5: 34 ca kiểm chứng phản biện lần 5 – không còn tái hiện; 6 ca đối chứng (F1 khác tên loại, F1 lý do ngắn, câu “chấm dứt áp dụng”, F2 có giải trình in Bảng 3, F2 giải trình ngắn, “1 ngày/1 năm”) đúng; 34 ca phản biện lần 4: 0 tái hiện; 20 ca bổ sung v4.4: 20/20 (N01, N22 đổi theo F1 và quy tắc tên tệp khi so sánh); bộ ca T, G 27/27; 21 ca phản biện lần 3: 0 tái hiện; bộ ca dựng báo cáo 25/25 (R18 ghi tên tệp ở vị trí); hồ sơ thật V1, V2, Q1: vai trò, lý do chặn, phát hiện thể thức không đổi; 35 văn bản Kho chạy không lỗi, khác v4.4 ở 8 tệp: bớt 5 TT-19 báo oan, thêm 1 TT-19 đúng (QĐ 2073), 2 văn bản không phải của Trường (NĐ 356, Phụ lục I NĐ 30) thêm TT-19.

## v4.4 – 27/10/2026
Căn cứ: 2 báo cáo phản biện lần 4 (ChatGPT 8 điểm PB4-GPT-01…08; Work 13 điểm PB4-WORK-01…13 – cả hai chạy thử) và báo cáo tổng hợp, kiểm chứng của Claude ngày 27/10/2026 (21/21 điểm tái hiện được trên v4.3 bằng 32 ca tự dựng); chỉ đạo đính chính và 2 quyết định của Hiệu trưởng ngày 27/10/2026:
- Đính chính TB 597/TB-CĐKT mục 6: cụm từ “hoặc từ 15 pt (exactly line spacing) trở lên” là sai sót trong quá trình tham mưu, loại bỏ hẳn; đúng là “khoảng cách giữa các dòng hay cách dòng (line spacing) chọn tối thiểu từ cách dòng đơn (single line spacing);”.
- E1 – Văn bản chính quyền: giãn dòng chỉ nhận kiểu theo dòng (Single, 1,5 lines, Multiple 1,0–1,5); Exactly, At least → TT-22 Mức 2. Ghi chú PB2-18 (giữ cận dưới Exactly 15 pt) hết hiệu lực.
- E2 – Phát hiện Mức 1 của script (CC-01) được loại khỏi kết luận khi script kiểm được nguyên văn trích đúng là chữ của đoạn bị báo, đúng tệp; báo cáo in riêng Bảng 2a “Phát hiện Mức 1 của script đã loại” kèm lý do để người ký xem lại.

Thay đổi theo từng điểm:
- PB4-GPT-01, PB4-WORK-02 (Cao): kiem_ke_ho_so.py: bỏ cờ “có tệp kèm” dùng chung; mỗi văn bản kèm theo mà chính bản dự thảo ban hành phải có trong bản hoặc là tệp riêng cùng tên loại và cùng trích yếu (≥ 60 % từ có nghĩa trùng nhau); không khớp → CHẶN, nêu tệp không khớp; chỉ định --vai-tro "<tệp>=kem_theo" được coi là khớp. Văn bản kèm theo của văn bản đã ban hành (“Kèm theo Quyết định 123/QĐ-CĐKT…”, có hay không chữ “số”, hoặc có ngày đã điền) là văn bản liên quan.
- PB4-GPT-02, PB4-WORK-06 (Cao): tao_bao_cao.py: bỏ qua theo tệp + mã + vị trí (ghi “tep” khi có từ hai tệp đã đo); Mức 1 kiểm nguyên văn đúng chữ của đoạn (kiem_tra_the_thuc.py ghi “doan_goc”); in Bảng 2a (quyết định E2).
- PB4-GPT-03, PB4-WORK-05 (Cao): kiem_tra_the_thuc.py: TT-24 xét theo số dòng thật (ngắt dòng Shift+Enter và ngắt dòng tự động theo bề rộng chữ – bảng do_rong_chu_TNR.json – trên bề rộng vùng chữ); sát ngưỡng một/hai dòng → “chưa kiểm”; bỏ ngưỡng 100 ký tự.
- PB4-GPT-04, PB4-WORK-07 (Cao): kiem_ke_ho_so.py: tệp trùng tên ở các thư mục con ghi bằng đường dẫn tương đối trong vai trò, mã băm, danh sách bản; tao_bao_cao.py đối chiếu kết quả đo theo mã băm từng tệp.
- PB4-GPT-05 (Cao): kiem_ke_ho_so.py: tệp Word ngắn có chữ thật được nhận; chỉ chặn khi dưới 15 ký tự, hoặc dưới 200 ký tự và có ảnh dán vào.
- PB4-WORK-01 (Cao): kiem_ke_ho_so.py: viện dẫn chỉ có số/rút gọn chỉ gộp vào viện dẫn đầy đủ cùng loại, cùng số; gộp sau khi quét hết văn bản (không phụ thuộc thứ tự đoạn).
- PB4-WORK-03 (Cao): la_cau_thay_the (hai script): câu phủ định (“chưa được thay thế”, “không bị bãi bỏ”, “chưa hết hiệu lực”, “chưa có văn bản thay thế”) không phải câu nêu việc thay thế → CC-01.
- PB4-WORK-04 (Cao): kiem_tra_the_thuc.py: đoạn canh giữa/phải trong thân văn bản vẫn đo; chỉ miễn vùng tiêu đề đầu phần, đề mục (Chương/Mục/Phần, tên chương một dòng in đậm/nghiêng), khối chữ ký, quốc hiệu – tiêu ngữ, “V/v”.
- PB4-GPT-06, PB4-WORK-10 (TB): tao_bao_cao.py: dòng ma trận Mâu thuẫn/Hẹp hơn/Rộng hơn phải có phát hiện DC đúng mã đặt cùng vị trí hoặc vị trí cha – con.
- PB4-GPT-07 (TB): tao_bao_cao.py: “Khớp” bị từ chối khi hai phía một yếu tố khác con số, khác đơn vị thời gian, có cặp trái nghĩa hoặc một phía phủ định.
- PB4-GPT-08 (TB): kiem_tra_the_thuc.py: vùng Nơi nhận dừng ở đoạn lời văn dài, đề mục, tiêu đề văn bản kèm theo/phụ lục hoặc phần mới; lời văn đặt sau Nơi nhận được đo.
- PB4-WORK-08 (TB): kiem_ke_ho_so.py (so sánh): tài liệu không có dòng “Số” chỉ được tính là “bản” khi tên tệp ghi rõ “dự thảo”; tài liệu tham khảo không bao giờ là “bản”.
- PB4-WORK-09 (TB): kiem_ke_ho_so.py: trích yếu sau “BÁO CÁO” dừng ở câu lời văn; tệp có dòng DỰ THẢO là Kế hoạch/Chương trình/Đề án/Hướng dẫn không có dòng “(Kèm theo…)” vẫn là dự thảo.
- PB4-WORK-11 (TB): kiem_tra_the_thuc.py: “chưa kiểm” lời văn trong bảng đếm mọi đoạn có chữ thường, kể cả câu ngắn.
- PB4-WORK-12 (TB): kiem_tra_the_thuc.py: tệp mở đầu bằng tiêu đề phụ lục/văn bản kèm theo, không có quốc hiệu, “Số:” được đo theo vai trò phụ lục/văn bản kèm theo (không TT-33); văn bản kèm theo nộp riêng ghi “chưa kiểm” đánh số liên tục.
- PB4-WORK-13 (TB): kiem_tra_the_thuc.py: đo TT-19 cho danh sách nơi nhận đặt ngoài bảng.
- Phát hiện khi tự kiểm (đo lại tài liệu do phiên xây dựng lập): dòng “Nơi nhận” chỉ nhận khi có dấu hai chấm hoặc đứng riêng (“Nơi nhận:”), tránh nhận nhầm ô bảng bắt đầu bằng chữ “Nơi nhận …” (cả hai script); đoạn canh giữa có quốc hiệu – tiêu ngữ hoặc “V/v” (dòng mẫu minh họa trong TB 597) không đo như lời văn.
- Đính chính TB 597 mục 6 (E1): PROFILE chính quyền bỏ cận Exactly; bảng 01 (TT-22, ghi chú A3), checklist, Skill-Library 14; bản chữ TB 597 trong Kho thêm ghi chú (tệp gốc giữ nguyên); kho_manifest.json thêm trường “dinh_chinh”.

Kết quả hồi quy v4.4: 34 ca kiểm chứng phản biện lần 4 – không còn tái hiện (32 ca lỗi + 2 ca đối chứng); 20 ca bổ sung v4.4 (đối chứng đúng/sai ở biên) 20/20 đạt; bộ ca T, G 27/27 đạt (T12b đổi kỳ vọng theo E1: Exactly 15 pt → TT-22); 28 ca phản biện lần 3: chỉ còn R7 (ghi chú tài liệu); bộ ca dựng báo cáo 25/25 đạt; hồ sơ thật V1, V2, Q1: vai trò, lý do chặn, phát hiện thể thức không đổi; so sánh V2 ↔ V3 thật: ĐỦ, đúng hai bản; 35 văn bản Kho chạy không lỗi, khác v4.3 ở 3 tệp – QĐ 1976 (2 đoạn Exactly 17,2 pt) và Pháp lệnh 01/2026 thêm TT-22 theo E1; Phụ lục I NĐ 30 (tệp riêng) đo theo vai trò phụ lục.

## v4.3 – 27/10/2026
Căn cứ: 4 báo cáo phản biện lần 3 (ChatGPT, Work – chạy thử; Grok, NotebookLM – chỉ đọc mã) và báo cáo tổng hợp, kiểm chứng của Claude ngày 27/10/2026 (17 vấn đề TH-01…TH-17, 26/28 ca kiểm chứng tái hiện được trên v4.2); 2 quyết định của Hiệu trưởng ngày 27/10/2026:
- D1 – Văn bản Đảng: đo “khoảng cách giữa các đoạn văn bản (Spacing) tối thiểu 6pt” (HD 05 Phần II mục 6.2.2) bằng khoảng cách thực giữa hai đoạn liền nhau = After đoạn trên + Before đoạn dưới ≥ 6 pt.
- D2 – TT-24 (dàn đều) chỉ áp đoạn dài hơn một dòng; mọi đoạn lời văn khác (kể cả đề mục “Điều …”, câu ngắn) vẫn đo cỡ chữ, khoảng cách, giãn dòng, thụt đầu dòng; lời văn trong bảng ghi “chưa kiểm”.

Thay đổi theo từng vấn đề:
- TH-01 (Cao – Sửa): kiem_ke_ho_so.py: tác vụ so sánh chỉ nhận bản có dấu dự thảo/phiên bản; tài liệu liên quan chỉ được tính là “bản” khi tên tệp ghi dự thảo/số phiên bản và số văn bản chưa điền; khác đúng 2 bản → CHẶN, đề nghị chỉ rõ cặp bằng --vai-tro.
- TH-02 (Cao – Sửa): kiem_ke_ho_so.py: vai trò mới “kem_theo” – nhận theo tiêu đề đầu tệp (Phụ lục N; QUY ĐỊNH, QUY CHẾ… không quốc hiệu, không số), không đòi dòng “(Kèm theo…)”; tệp phụ lục của văn bản đã ban hành (dòng “Kèm theo … số …” có số) vẫn là văn bản liên quan; quét viện dẫn trên dự thảo và mọi tệp kèm (ghi tên tệp); chỉ tính “có phụ lục” khi có tiêu đề phụ lục thật; kiểm G4 riêng từng bản.
- TH-03 (Cao – Sửa): kiem_ke_ho_so.py nhận “Nghị định/Thông tư/Quyết định/Thông báo/NĐ/TT/QĐ/TB + số”; khớp duy nhất một văn bản cùng loại, cùng số trong hồ sơ/Kho thì gắn vào; không xác định được → CHẶN (so sánh: không chặn, ghi “Chưa kiểm”). Sửa tệp 05, CHANGELOG.
- TH-04 (Cao – Sửa theo quyết định PB2-07): tao_bao_cao.py: mọi tệp trong anh_can_xem phải có xem_anh {tep, so_anh_da_xem, ket_luan = so_do | van_ban_chup, mo_ta}; thiếu → từ chối; van_ban_chup → từ chối, nhắc gửi thông báo CHẶN G1; kết luận xem ảnh in ở mục I.7. SKILL.md Bước 7, mẫu dữ liệu.
- TH-05 (Cao – Sửa): tao_bao_cao.py: chỉ bỏ từng phát hiện đúng vi_tri script ghi; lý do ≥ 20 ký tự; phát hiện Mức 1 phải kèm nguyen_van trong ngoặc kép; bỏ hẳn cách bỏ cả mã. Bảng 02 mục 5, SKILL.md.
- TH-06 (Cao – Sửa): tao_bao_cao.py: Mâu thuẫn → DC-01, Hẹp hơn → DC-02, Rộng hơn → DC-03, phải có phát hiện đúng mã Mức 1–2. Bảng 02 mục 4.
- TH-07 (Cao – Sửa theo quyết định D2): kiem_tra_the_thuc.py phân vùng theo vai trò (đầu văn bản, tên loại – trích yếu, dòng in hoa, “Số:”, “Kính gửi”, địa danh – ngày, vùng Nơi nhận đến hết phần, khối chữ ký, dòng phụ lục, đoạn canh giữa/phải ≤ 100 ký tự hoặc đậm/nghiêng toàn bộ) rồi đo; TT-20…23 ở mọi đoạn lời văn còn lại kể cả đề mục và câu ngắn; TT-24 chỉ đoạn > 100 ký tự; lời văn trong bảng nội dung ghi “chưa kiểm”. Bảng 01 ghi chú A3, SKILL.md Bước 2.
- TH-08 (Cao – Sửa): Hai script dùng chung quy tắc la_cau_thay_the: chỉ miễn khi CHÍNH lần nhắc nằm trong cụm “thay thế/bãi bỏ … <số hiệu>” (cách tối đa 4 từ) hoặc “<số hiệu> đã được thay thế/hết hiệu lực”; ranh giới ký hiệu đầy đủ; dạng rút gọn nhận cả ở cuối đoạn; cổng ghi “không phải viện dẫn sai” khi mọi lần nhắc đều là câu thay thế. Tệp 05.
- TH-09 (Cao – Sửa): kiem_tra_the_thuc.py: văn bản Đảng bắt buộc kiểu Exactly 18–22 pt; Single, Multiple, At least → TT-22. Bảng 01 mục B.
- TH-10 (TB – Sửa theo quyết định D1): kiem_tra_the_thuc.py: văn bản Đảng đo khoảng cách thực giữa hai đoạn lời văn liền nhau = After đoạn trên + Before đoạn dưới ≥ 6 pt; văn bản chính quyền giữ Before ≥ 6 và After ≥ 6. Bảng 01 mục B.
- TH-11 (TB – Sửa): Cổng và bộ đo ghi tên, mã băm SHA-256 từng tệp; tao_bao_cao.py từ chối kết quả đo của tệp ngoài hồ sơ và đòi đo đủ mọi tệp dự thảo, phụ lục/văn bản kèm theo. SKILL.md Bước 7.
- TH-12 (TB – Sửa): tao_bao_cao.py: so vị trí theo quan hệ cha – con (Điều 7 ⊃ Điều 7 khoản 2), không vừa lỗi vừa Đạt/Khớp; mỗi yếu tố khớp phải trích hai phía trong ngoặc kép. Mẫu dữ liệu, bảng 02 mục 4.
- TH-13 (TB – Sửa): kiem_tra_the_thuc.py: dòng đầu tiên của phần (section) mới khớp mẫu phụ lục được nhận là dòng phụ lục bất kể canh lề, rồi báo lỗi canh lề như phụ lục.
- TH-14 (TB – Sửa): kiem_ke_ho_so.py: chỉ xét dòng tên loại “BÁO CÁO” và tối đa 3 dòng trích yếu liền sau. Tệp 05.
- TH-15 (Thấp – Sửa): TT-38 → HD 05 mục IV.5.1; TT-39 → HD 05 mục IV.5.2; TT-40 (thiếu số phụ lục) → HD 05 Phần II mục 1.1 cho văn bản Đảng.
- TH-16 (Thấp – Sửa): SKILL.md Bước 2, Bước 7, checklist; tools/README; mẫu dữ liệu (ví dụ xem_anh, bo_qua_the_thuc); Prompt 05-So-Sanh.
- TH-17 (Thấp – Sửa (quy trình)): Đóng gói bằng zipfile của Python (gắn cờ UTF-8 cho tên tiếng Việt); ca hồi quy kiểm đủ tập mã; CHANGELOG v4.3 ghi rõ việc sửa lời khẳng định sai ở v4.2; chỉ ghi điều đã có ca chạy chứng minh.

Sửa lời khẳng định sai ở v4.2: CHANGELOG v4.2 (PB2-06) và tệp 05 ghi cổng đã nhận dạng “NĐ 356” – thực tế v4.2 chỉ nhận dạng có năm (“Nghị định 13/2023”); dạng chỉ có số được bổ sung ở v4.3 (TH-03).
Kết quả hồi quy v4.3: 28 ca kiểm chứng của phản biện lần 3 (V01–V21, R1–R7) – lỗi không còn tái hiện (R1–R7 kiểm lại bằng bộ R mới); bộ ca v4.2 (T, G) 27/27 đạt; bộ ca dựng báo cáo v4.3 25/25 đạt (gồm đo lại thể thức 5 báo cáo dựng ra: 0 phát hiện); dự thảo thật V1, V2, V3, Q1: phát hiện thể thức không đổi; cổng V1, V2, Q1: lý do chặn không đổi (thiếu toàn văn văn bản căn cứ; V2 thiếu Báo cáo tiếp thu); so sánh V2 ↔ V3: ĐỦ, đúng hai bản; 35 văn bản Kho chạy không lỗi.

## v4.2 – 27/10/2026
Căn cứ: báo cáo phản biện lần 2 (27/10/2026, 21 điểm PB2-01…PB2-21) và 2 quyết định của Hiệu trưởng ngày 27/10/2026:
1. PB2-15 – So sánh hai bản: **chỉ đủ hai bản**. Chặn khi thiếu một trong hai bản, phụ lục hoặc văn bản kèm theo; văn bản được đề cập chưa có toàn văn không chặn, đối chiếu ghi “Chưa kiểm”.
2. PB2-07 – Word nhiều chữ kèm ảnh chụp: **script lọc, AI xem ảnh**. Tệp chủ yếu là ảnh: script chặn; tệp nhiều chữ có ảnh ≥ 1/4 trang: AI bắt buộc xem – văn bản chụp/scan → chặn G1, sơ đồ → nhận.

Thay đổi theo từng điểm phản biện:
- PB2-01 (Cao – Sửa): kiem_tra_the_thuc.py mục 4 viết lại: đo cỡ chữ, khoảng cách đoạn, giãn dòng, thụt đầu dòng trên MỌI đoạn lời văn (ngoài bảng, dài trên 25 ký tự, không phải trích yếu, không căn giữa/phải, không in hoa toàn bộ, không phải dòng phụ lục); thêm mã TT-24 “Canh lề lời văn” Mức 2; mục Đạt ghi “n/n đoạn”, không có đoạn nào thì ghi “chưa kiểm”. Bảng 01, 02, SKILL.md Bước 2 bổ sung.
- PB2-02 (Cao – Sửa): pl_match nhận mọi kiểu chữ; đuôi chữ thường chỉ nhận khi đoạn căn giữa (tránh nhận nhầm câu lời văn “Phụ lục I. …” canh đều). Mọi chỗ gọi truyền thuộc tính căn lề của đoạn.
- PB2-03 (Cao – Sửa): kiem_ke_ho_so.py: thứ tự cố định – (1) vùng tiêu đề có “TIẾP THU” và “GIẢI TRÌNH” → Báo cáo tiếp thu; (2) dấu dự thảo; (3) tiêu đề báo cáo của Skill; (4) tên tệp. Vùng tiêu đề dừng ở “Kính gửi”, đề mục I./1. hoặc đoạn dài (tránh báo cáo rà soát có câu “cập nhật Báo cáo giải trình tiếp thu” ở phần kết luận bị nhận nhầm). Thêm --vai-tro TÊN_TỆP=VAI_TRÒ (lặp được, ghi vào kết quả cổng).
- PB2-04 (Cao – Sửa): Nhận “ban hành kèm theo” không phân biệt hoa thường, với Quyết định/Thông báo/Tờ trình này; thiếu văn bản kèm theo → CHẶN G4.
- PB2-05 (Cao – Sửa): Kiểm khoảng cách đoạn ≥ 6 pt, canh đều, thụt khoảng 10 mm, giãn dòng Exactly 18–22 pt cho văn bản Đảng, dẫn HD 05 Phần II mục 6.2.2. Bảng 01 mục B thêm dòng lời văn, bỏ “khoảng cách đoạn” khỏi dòng “Không áp”.
- PB2-06 (Cao – Sửa): Tách tên luật ở “và/hoặc/,” khi sau đó là văn bản khác; số hiệu cho phép chữ thường sau gạch (QĐ-TTg); nhận đuôi “hiện hành, mới nhất, quy định, tại, theo”; thêm dạng rút gọn “Nghị định 13/2023”, “NĐ 356” (khớp về số hiệu đầy đủ trong hồ sơ, Kho).
- PB2-07 (TB – Sửa theo quyết định): Theo quyết định của Hiệu trưởng 27/10/2026: script chặn tệp chủ yếu là ảnh (giữ ngưỡng cũ); tệp nhiều chữ có ảnh ≥ 1/4 trang → “PHẢI XEM ẢNH” (trường anh_can_xem), --xuat-anh xuất ảnh; AI bắt buộc xem: văn bản chụp/scan → CHẶN G1, sơ đồ → nhận. Đếm cả ảnh VML (w:pict). SKILL.md Bước 1, ví dụ, checklist; 05 G1.
- PB2-08 (TB – Sửa): Dấu dự thảo (dòng DỰ THẢO, số để trống) xét trước tiêu đề báo cáo của Skill; nhận diện báo cáo của Skill chỉ theo tiêu đề đặc trưng (BÁO CÁO RÀ SOÁT DỰ THẢO/CHÍNH THỨC/NHANH/LẦN n, BÁO CÁO SO SÁNH HAI BẢN, BẢN NHÁP RÀ SOÁT, KẾT LUẬN ĐIỀU KIỆN TRÌNH KÝ).
- PB2-09 (TB – Sửa): CC-01 quét thêm footnotes.xml, endnotes.xml (vị trí “Chú thích (cuối trang)”); nhận dạng rút gọn khi đứng sau Nghị định/NĐ/Quyết định/QĐ/Thông tư/TT (không nhận “số liệu 13/2023”). Cổng nhận dạng rút gọn (PB2-06). Không báo khi câu nêu việc văn bản cũ đã được thay thế, bãi bỏ (trước hoặc ngay sau số hiệu, trong cùng vế câu).
- PB2-10 (TB – Sửa): Bỏ qua phụ lục của văn bản khác cả khi viết tắt NĐ, QĐ, TT, TB, HD, KH, NQ, CT; loại văn bản suy theo ký hiệu (loai_theo_ky_hieu).
- PB2-11 (TB – Sửa): Mã phải có trong bảng mức cố định hoặc tập mã script đo (TT-01…04, 10…24, 30…46, 50, 51; TB-01…03; TD-01…05; CC-01, 02, 06); mã lạ bị từ chối. Bảng 02 mục 5 ghi rõ.
- PB2-12 (TB – Sửa): yeu_to_khop bắt buộc dạng {chu_the, hanh_vi, muc_thoi_han}, từ chối “trùng từ khóa/tương tự”; so vị trí theo tập Điều, khoản, điểm, phụ lục, phần văn bản (không theo chuỗi); mục Đạt nhóm Nội dung, Điều khoản bắt buộc phải có vi_tri. Mẫu dữ liệu cập nhật.
- PB2-13 (Thấp – Sửa): Mỗi dòng hồi quy phải có ma_cu và ket_qua; in II.A → II.B → II.C.
- PB2-14 (Thấp – Sửa): Phiên bản theo tên tệp nhận “bản/BẢN n”; số để trống kiểu văn bản Đảng (“Số   -NQ/ĐU”) là dấu dự thảo.
- PB2-15 (Thấp – Sửa theo quyết định): Theo quyết định của Hiệu trưởng 27/10/2026 “chỉ đủ hai bản”: so sánh áp G1–G4 (định dạng, đủ hai bản, phụ lục, văn bản kèm theo); văn bản được đề cập chưa có → “Chưa có – không chặn (so sánh); đối chiếu ghi “Chưa kiểm””. SKILL.md, 05, 05-So-Sanh.
- PB2-16 (Thấp – Sửa): Ghép cặp theo độ giống tốt nhất (≥ 0,5, giữ thứ tự); đọc endnotes; vị trí ghi “Quy định – Điều N”, “Văn bản chính – Điều N”, “Phụ lục I – …”, “Chú thích”.
- PB2-17 (Thấp – Sửa): Nhận tên luật đứng trước “năm …”, “và các luật”, “(”; nhận cụm “các luật sửa đổi(, bổ sung)” là liệt kê luật sửa đổi. Tệp 04 mục 2 bổ sung.
- PB2-18 (Thấp – Không sửa – có lý do; **hết hiệu lực từ v4.4 do Hiệu trưởng đính chính TB 597 mục 6 ngày 27/10/2026**): Giữ cận dưới Exactly 15 pt vì TB 597/TB-CĐKT mục 6 của Trường cho phép “từ 15 pt (exactly) trở lên”; Trường đã quy định thì theo quy định của Trường (SKILL.md quy tắc ổn định 2). Ghi lý do ở bảng 01 mục A3. Đề nghị Hiệu trưởng xem lại nếu muốn nâng cận dưới.
- PB2-19 (Thấp – Sửa): Văn bản Đảng: TT-01, TT-04 dẫn HD 05; TT-40 dẫn “HD 05 Phần II mục 1.1”; TT-41 dẫn HD 05 Phần II mục 1.2; lời văn dẫn HD 05 Phần II mục 6.2.2.
- PB2-20 (Thấp – Sửa): Chuỗi phiên bản v4.2 trong 4 script, mẫu dữ liệu, 01–06, SKILL.md, README; thang 4 mức thay Critical/Major/Minor ở Skill-Library 02, 19; 29-Skill-Van-Ban-Dang dẫn đúng SKILL.md và Mẫu prompt trong assets, quy tắc bảo mật theo quyết định 4; bỏ “quyết định 15/9/2026” ở TT-45 và bảng 01; CHANGELOG ghi đúng Kho 36 văn bản (35 .docx, 1 PDF).
- PB2-21 (Thấp – Sửa): tao_bao_cao.py thêm kieu_bao_cao = chinh_thuc | nhanh | so_sanh (phải khớp tác vụ của cổng); (b), (c) có tiêu đề riêng, không gán nhãn trình ký; (c) bắt buộc --so-sanh ss.json và so_sanh.ket_luan, in II.D bảng thay đổi và “Kết luận so sánh”. Mọi đoạn lời văn của báo cáo dàn đều, thụt 1 cm.

Kết quả hồi quy: bộ ca theo Mục 6 báo cáo phản biện lần 2 – 27/27 ca đo thể thức và cổng (T01–T12, G02b–G13b), 16/16 ca dựng báo cáo (R01–R08) đạt; dự thảo V1, V3, Q1 thật cho cùng phát hiện thể thức như v4.1; cổng V1, Q1 cho cùng kết quả như v4.1, cổng V2 nay nhận đúng báo cáo rà soát lần 2 (v4.1 cũng đúng; bản sửa đầu tiên của PB2-03 làm sai và đã được chặn lại bằng ca này); 35 văn bản .docx trong Kho chạy không lỗi; báo cáo do tao_bao_cao.py dựng đo lại bằng kiem_tra_the_thuc.py: 0 phát hiện.
Điểm không sửa: PB2-18 (giữ Exactly ≥ 15 pt theo TB 597 mục 6) – đề nghị Hiệu trưởng xem lại nếu muốn nâng cận dưới.

## v4.1 – 26/10/2026
Căn cứ: báo cáo phản biện độc lập Phiên B (26/10/2026, 27 điểm PB-01…PB-27) và 6 quyết định của Hiệu trưởng ngày 26/10/2026:
1. Viện dẫn VBHN theo **mẫu của Trường** (văn bản hành chính theo NĐ 30 – Luật, Pháp lệnh không ghi số, ký hiệu; cách ghi số theo Pháp lệnh 01/2026 dành cho văn bản quy phạm pháp luật).
2. Quy tắc thể thức mới ngày 26/10/2026 **chỉ áp cho văn bản chính quyền**; văn bản Đảng theo HD 05 (kể cả chỉ dẫn dưới tiêu đề phụ lục).
3. Tác vụ so sánh hai bản **không** đòi báo cáo rà soát lần trước và Báo cáo tiếp thu; chỉ kiểm định dạng tệp và đủ văn bản.
4. Tài liệu mật: **người dùng tự chịu trách nhiệm** không đưa lên AI; Skill không kiểm (bỏ G9).
5. Báo cáo rà soát theo **chuẩn Trường** (lề 2/2/3/2 cm, số trang giữa lề trên).
6. Áp dụng đề xuất 8 của B2: chế độ ĐL không mở tóm tắt cũ trước khi xong Phần II; phiên kiểm thử không lưu tóm tắt vào Project.

Thay đổi theo từng điểm phản biện:
- PB-01 (Cao – Sửa): kiem_tra_the_thuc.py: thông số theo hệ (thể loại 15–16, trích yếu 14–15, lời văn 14–15 cho văn bản Đảng); các quy tắc riêng 26/10/2026 (khoảng cách đoạn, section văn bản kèm theo, dòng “CỦA TRƯỜNG…”, TT-45, căn bảng, “Phụ lục I”) chỉ áp cho chính quyền; thêm TT-46 kiểm văn bản Đảng PHẢI có chỉ dẫn phụ lục (HD 05 Phần II mục 1.2). Bảng 01 mục B, 02, 06, SKILL.md ghi rõ phạm vi.
- PB-02 (Cao – Sửa): Trích yếu chỉ gồm các đoạn CANH GIỮA liền sau tên loại; gặp đoạn không canh giữa là dừng. Đoạn trích yếu không bị tính vào cỡ chữ lời văn (TT-20).
- PB-03 (Cao – Sửa): Hàm pl_match nhận dòng phụ lục cả khi in hoa và viết liền tiêu đề; phần đó được xếp là phụ lục (đánh số riêng từ 1); báo TT-40 (“Phụ lục” phải in thường), TT-42 (tiêu đề phải ở dòng riêng), TT-43 (thiếu dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM”). Không nhận nhầm câu văn bắt đầu bằng “Phụ lục …”.
- PB-04 (Cao – Sửa): kiem_ke_ho_so.py thêm --tac-vu so-sanh: không tự nâng lần rà soát, không áp G6–G8, cần đủ 2 bản; trích dẫn của cả hai bản đều được đối chiếu. SKILL.md Bước 1, 05 ghi lệnh theo tác vụ.
- PB-05 (Cao – Sửa): Đọc thêm footnotes.xml, endnotes.xml; nhận mọi số hiệu đứng riêng (“QĐ 2307/QĐ-CĐKT”, “Quyết định 2264/QĐ-CĐKT”, “Nghị định 13/2023/NĐ-CP”, “208-QĐ/TW”, “125/2025/QH15”).
- PB-06 (Cao – Sửa (a, b); bỏ G9 theo quyết định 4): (a) Chặn .docx chủ yếu là ảnh chụp/scan: có ảnh trong thân văn bản ≥ 1/4 trang A4 mà tệp có dưới 3.000 ký tự chữ cho mỗi ảnh, hoặc có ảnh ≥ 80% trang; tệp nhiều chữ kèm sơ đồ (như Phụ lục I NĐ 30) chỉ ghi chú cho người rà soát; (b) chặn tệp nén .zip, .rar, .7z…; (c) G9 bỏ khỏi cổng: người dùng tự chịu trách nhiệm không đưa tài liệu mật lên AI – ghi ở SKILL.md mục Bảo mật và 05.
- PB-07 (Cao – Sửa): CC-02 viết lại: đọc danh sách VBHN từ kho_manifest.json; chỉ báo Mức 2 khi luật đã có VBHN đã biết; nhận “Luật Sửa đổi/sửa đổi” không phân biệt hoa thường; báo VBHN cũ hơn bản mới nhất; luật chưa biết VBHN → “chưa kiểm” (Phần I.8), không kết luận lỗi.
- PB-08 (Cao – Sửa theo quyết định 1): Theo mẫu của Trường: văn bản hành chính theo NĐ 30 (PL I Phần II mục 6.a) – Luật, Pháp lệnh không ghi số, ký hiệu; cách ghi số theo Pháp lệnh 01/2026 dành cho văn bản quy phạm pháp luật. Bỏ ghi chú “Mức 4”; thêm CC-06 (ghi số, ký hiệu luật trong căn cứ → Mức 2), script tự phát hiện.
- PB-09 (Cao – Sửa): Thêm trạng thái thứ 6, bắt buộc kèm căn cứ đúng (can_cu_dung); hiển thị ở II.A.
- PB-10 (Cao – Sửa theo quyết định 6): SKILL.md Bước 0 mục 4: chế độ ĐL không mở báo cáo, tóm tắt trong Project, bộ nhớ, tìm kiếm hội thoại cũ, thư mục kết quả cũ trước khi xong Phần II (chỉ mở ở Bước 6); Bước 7 mục 4: phiên kiểm thử không lưu tóm tắt vào Project, bộ nhớ.
- PB-11 (TB – Sửa): tao_bao_cao.py: “Khớp” bắt buộc nguyên văn hai phía trong ngoặc kép và trường yeu_to_khop (chủ thể, hành vi, mức/thời hạn); vị trí có phát hiện ở Phần II không được ghi Khớp hay Đạt.
- PB-12 (TB – Sửa): Chế độ ĐC bắt buộc có hoi_quy và cổng phải ghi lần ≥ 2; Phần VI phải có 3–5 vấn đề ưu tiên (ít hơn 3 chỉ khi số phát hiện ít hơn 3).
- PB-13 (TB – Sửa): Dữ liệu ghi "da_ban_hanh": true → script gán nhãn “Kiến nghị sửa đổi, bổ sung” kèm số lượng theo mức; 02 mục 5 và SKILL quy tắc 6 ghi rõ đây là nhãn riêng của trường hợp này.
- PB-14 (TB – Sửa): SKILL.md ví dụ và assets/Mau-Du-Lieu-Bao-Cao.json trích đúng nguyên văn: “… chậm nhất trong ngày làm việc kể từ khi phát hiện.”; ghi rõ dự thảo trong ví dụ là giả định.
- PB-15 (TB – Sửa): Exactly 15–24 pt (24 pt ≈ 1,5 lines của chữ 14); bảng 01 cập nhật.
- PB-16 (TB – Sửa description; K1–K6 chuyển Phiên C): Description theo đề xuất 4 của B2: liệt kê tác vụ (rà soát chính thức/sơ bộ, so sánh hai bản, kiểm tra tiếp thu, chuẩn hóa), loại văn bản và vế loại trừ viết đủ (chương trình đào tạo, giáo trình, giáo án, kế hoạch bài giảng, ngân hàng câu hỏi, soạn mới). Việc nạp skill chỉ đo được trong phiên chat thật nên K1–K6 đưa vào Phiên C.
- PB-17 (TB – Sửa): Thêm tools/so_sanh_ban.py (difflib theo đoạn, chi tiết từ ngữ, Điều bị ảnh hưởng); SKILL Bước 5 dùng script này cho ĐC và tác vụ so sánh.
- PB-18 (TB – Sửa): Script đọc danh sách từ kho_manifest.json (một nguồn); CC-01 quét mọi đoạn, bỏ qua câu “thay thế/bãi bỏ … QĐ cũ”.
- PB-19 (TB – Sửa): Script dùng ±20 twips, khớp bảng 01 mục C.
- PB-20 (TB – Sửa): Script chỉ ghi Đạt “có đối tượng vẽ”; độ dài 1/3–1/2 ghi “chưa kiểm” (Phần I.8).
- PB-21 (TB – Sửa): Vai trò xác định theo nội dung phần đầu (tiêu đề BÁO CÁO RÀ SOÁT/BẢN NHÁP RÀ SOÁT; tiêu đề TIẾP THU – GIẢI TRÌNH; dòng “DỰ THẢO” riêng hoặc “Số:” để trống); tên tệp chỉ dùng khi nội dung không có tín hiệu. Nhận phiên bản “_V2”, “ v3”, “lần 2”, “bản 2”.
- PB-22 (Thấp – Sửa): Chuyển vào references/Lich-Su-Khong-Ap-Dung/ kèm README ghi rõ “không áp dụng” và các điểm đã bị thay thế; SKILL.md, 00-README nêu thư mục này không dùng.
- PB-23 (Thấp – Sửa): Thống nhất: VBHN mới nhất, hiệu lực chỉ xác định từ hồ sơ và Kho; kết quả tra Internet (nếu có) chỉ ghi tham khảo ở Phần I.8, không làm căn cứ kết luận lỗi.
- PB-24 (Thấp – Sửa): 29-Skill-Van-Ban-Dang: thay bằng mức theo bảng mã 02 (TQ-01 Mức 1; DG-01, DG-02, thể thức Mức 2; văn phong Mức 3). 29-Phu-Luc-3 mục 3: danh mục thể loại theo QĐ 399 là căn cứ chính thức.
- PB-25 (Thấp – Sửa): Nêu rõ QĐ 389 chỉ dùng cho phần TB 597 dẫn chiếu sang (dấu, chữ ký số – TB 597 mục 8; thành phần khác – mục 10).
- PB-26 (Thấp – Sửa): Ghi đúng: Kho 34 văn bản = 33 .docx + 1 PDF scan; 33 bản text (số liệu trước khi bổ sung Luật 91/2025/QH15 và NĐ 356/2025/NĐ-CP; sau bổ sung: 36 văn bản = 35 .docx + 1 PDF, 35 bản text); số tệp và số mục của gói v4.1 ghi trong bảng xử lý.
- PB-27 (Thấp – Sửa theo quyết định 5): Báo cáo theo chuẩn Trường: lề 2/2/3/2 cm, header/footer 1,27 cm, số trang giữa lề trên cỡ 14, ẩn trang 1, khoảng cách đoạn 6 pt.

Bổ sung Kho (26/10/2026, theo thông tin của Hiệu trưởng): thêm Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 (hiệu lực 01/01/2026) và Nghị định số 356/2025/NĐ-CP ngày 31/12/2025 (hiệu lực 01/01/2026); ghi NĐ 13/2023/NĐ-CP vào danh sách văn bản đã bị thay thế (NĐ 356 Điều 42 khoản 2) → dự thảo còn viện dẫn NĐ 13/2023 bị báo CC-01 Mức 1; cổng không đòi toàn văn hai văn bản mới vì đã có trong Kho. Kho nay 36 văn bản (35 .docx, 1 PDF).

Kết quả hồi quy: dự thảo V1, V3, Q1 thật cho cùng phát hiện thể thức như v4.0 (không phát sinh lỗi mới); cổng V1, V2, Q1 vẫn CHẶN vì thiếu toàn văn văn bản căn cứ (V2: thêm thiếu Báo cáo tiếp thu); 33 văn bản .docx trong Kho chạy không lỗi.

## v4.0 – 26/10/2026
Căn cứ: văn bản “Nội dung cập nhật Skill ktc-ra-soat-897 (ngày 26.10.2026)” và trả lời 5 điểm của Hiệu trưởng ngày 26/10/2026; báo cáo kiểm thử B2 Skill v3.0 (24/10/2026, kết luận CHƯA ĐẠT).

### Ổn định kết quả
- Thêm 3 script: `tools/kiem_ke_ho_so.py` (cổng hồ sơ), `tools/kiem_tra_the_thuc.py` (đo thể thức từ XML, dựng trang bằng LibreOffice), `tools/tao_bao_cao.py` (dựng báo cáo, tự tính Bảng 1, Bảng 2, mức tuân thủ, nhãn).
- Thêm `references/Quy-Tac-KTC/` 01–06: bảng thông số cố định; bảng mã → mức; danh mục đơn vị, cơ sở; viện dẫn VBHN; cổng hồ sơ; điểm thay thế Mẫu prompt.
- Nhãn kết luận còn 4; bỏ nhãn “CHƯA KẾT LUẬN ĐIỀU KIỆN TRÌNH KÝ – thiếu hồ sơ”. Mức tuân thủ pháp luật gán cố định theo số lượng Mức 1–3.
- Ma trận đối chiếu chỉ 6 giá trị; “Khớp” bắt buộc nguyên văn hai phía. Không có bằng chứng hai phía thì không có Mức 1–2.
- Phát hiện sắp xếp cố định (mức → nhóm → mã).

### Cổng hồ sơ (chặn hẳn)
- Chỉ nhận .docx, .xlsx; PDF có lớp chữ. Có 1 tệp ảnh/scan/.doc → chặn.
- Thiếu dự thảo, phụ lục, văn bản kèm theo, toàn văn mọi văn bản được đề cập (kể cả luật, nghị định ở căn cứ) → chặn.
- Từ lần 2: thiếu báo cáo rà soát lần trước hoặc Báo cáo tiếp thu, giải trình bằng văn bản riêng → chặn.
- Bỏ lựa chọn “vẫn làm tiếp” khi thiếu hồ sơ.

### Thể thức (văn bản chính quyền)
- Thứ tự ưu tiên: TB 597/TB-CĐKT, QĐ 1355/QĐ-CĐKT trước; NĐ 30/2020/NĐ-CP sau.
- A4; lề 2/2/3/2 cm; header/footer 1,27 cm; lời văn 14; Before/After ≥ 6 pt; giãn dòng Single–1,5 lines; số trang giữa lề trên cỡ 14.
- Văn bản kèm theo: section mới, đánh số **liên tục** (điểm 1). Phụ lục: La Mã, “Phụ lục” in thường, tiêu đề in hoa căn giữa, dòng riêng “CỦA TRƯỜNG CAO ĐẲNG KON TUM” (chỉ tiêu đề phụ lục – điểm 2), đường kẻ 1/3–1/2, đánh số riêng từ 1 có hiện trang đầu, phụ lục 1 trang không đánh số; “Phụ lục I” viết hoa khi viện dẫn.
- Dòng “(Kèm theo …)” dưới tiêu đề phụ lục/văn bản kèm theo: từ “không phải lỗi” (v3.0) thành **lỗi TT-45, Mức 2**.
- Bảng canh giữa trang, ô canh giữa theo chiều dọc.
- Tên đơn vị theo TB 597 mục 3.1.c; tên, địa chỉ cơ sở theo QĐ 1355.

### Nội dung, căn cứ
- Dự thảo chặt hơn văn bản đã ban hành của Trường (ví dụ QĐ 2307) → Mức 2 (điểm 4).
- Viện dẫn luật đã sửa đổi theo VBHN mới nhất (Pháp lệnh 01/2026/UBTVQH16).
- Thẩm quyền ký theo QĐ 2073/QĐ-CĐKT (Quy chế làm việc 23/9/2026).
- Ban Truyền thông thuộc phòng TH-HC&QT theo QĐ 2041/QĐ-CĐKT năm 2026 (điểm 5); Ban Văn – Thể – Mỹ (QĐ 1997), Tổ Quản trị hệ thống thông tin (QĐ 794, 969): không yêu cầu xác minh.
- Văn bản Đảng: Đảng bộ Trường là đảng bộ trực thuộc cơ sở – chốt, không hỏi lại; sai → Mức 2.

### Kho dữ liệu
- Thêm: Pháp lệnh 01/2026/UBTVQH16; TT 63/2026/TT-BGDĐT; QĐ 2073, 2264, 2307, 2309, 2328; QĐ 2041–2054; QĐ 794, 969, 1997, 101; QĐ 344/2021, 1387/2020 (lịch sử).
- Đổi tên tệp `Thong-bao-897-…` thành `TB-597-TB-CDKT-Huong-dan-the-thuc-ky-thuat-trinh-bay-VB-2026.docx`; chuyển QĐ 1355 vào `02-KTC-Regulations`; bỏ thư mục `04-Good-Documents` và các bản PDF trùng nội dung với .docx; gỡ phông nhúng của QĐ 2054, QĐ 969 (nội dung giữ nguyên).
- Thêm `text/` (bản text toàn văn) và `kho_manifest.json` (danh mục máy đọc, VBHN đã biết, văn bản đã bị thay thế).
- Bỏ tệp trùng: template trống ở thư mục gốc, `assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx`; chuyển `build_tcdm_review_fixed.py` vào `tools/legacy/`.

### Điểm đề nghị Hiệu trưởng xem lại
1. (Đã quyết ở v4.1) Mẫu viện dẫn VBHN của Trường không ghi số luật; dự thảo ghi số luật → CC-06 Mức 2.
2. Mức xếp loại: toàn bộ lỗi thể thức đo được xếp Mức 2 (nên nhãn thường là “Cần chỉnh sửa trước khi trình ký” cho đến khi thể thức đạt hết); đoạn trống thay ngắt trang, số trang đặt cứng nhưng hiển thị đúng, dấu câu căn cứ xếp Mức 3.
3. Các QĐ 2307, 2309, 2328 đã ký chưa đáp ứng một số quy tắc mới 26/10/2026 (section, dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM”, số trang) – do quy tắc mới, không phải lỗi khi ký.
4. Cổng chặn khi thiếu toàn văn mọi luật, nghị định ở căn cứ: hồ sơ thực tế (ví dụ dự thảo Quy tắc ứng xử AI có 20 căn cứ) cần chuẩn bị đủ tệp trước khi rà soát.

## v3.0 – 10/2026
Chế độ ĐL/ĐC; cổng hồ sơ H1–H6 (cho phép làm tiếp với nhãn “chưa kết luận”); ma trận đối chiếu chéo; tiêu chí kết luận cứng 5 nhãn; quy tắc bằng chứng.

## v2.8 – 14/9/2026
Thay QĐ 988 bằng QĐ 1976/QĐ-CĐKT; Kho dữ liệu 897 đóng gói cục bộ (9 văn bản).

## v2.x – 08–09/2026
Bổ sung văn bản Đảng (QĐ 399, HD 05, QĐ 208); quyết định 15/9/2026 về dòng chỉ dẫn “Kèm theo …”.
