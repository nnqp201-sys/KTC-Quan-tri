---
name: "ktc-ra-soat-897"
description: "Rà soát chính thức hoặc sơ bộ, so sánh hai bản (hai phiên bản) dự thảo, kiểm tra tiếp thu sau báo cáo rà soát, chuẩn hóa văn phong cho văn bản hành chính, văn bản Đảng của Trường CĐ Kon Tum (quyết định, quy chế, quy định, kế hoạch, tờ trình, báo cáo, công văn, thông báo). Không dùng cho chương trình đào tạo, đề cương, giáo trình, giáo án, kế hoạch bài giảng, ngân hàng câu hỏi, soạn văn bản mới."
---

# KTC Rà soát 897 — rà soát dự thảo văn bản trước khi trình ký (v4.4, 27/10/2026)

## Mục đích
Kiểm tra dự thảo văn bản của Trường Cao đẳng Kon Tum trước khi trình ký: thể thức, căn cứ, nội dung, thẩm quyền, tính thống nhất với văn bản đã ban hành của Trường. Kết quả **phải giống nhau giữa các lần chạy và giữa các tài khoản** với cùng hồ sơ: thông số cố định, đo bằng script, mức theo bảng mã, nhãn do script tính. Căn cứ có thể thay đổi: kiểm tra hiệu lực tại thời điểm sử dụng. Kết quả AI chỉ để tham khảo, không thay trách nhiệm của người soạn thảo, người kiểm tra, người ký.

## Thứ tự ưu tiên căn cứ và tài liệu
1. Tệp này (SKILL.md) → `references/Quy-Tac-KTC/` (01–06) → Mẫu prompt `assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897-v2.0-KTC-Enhanced.docx` → các tệp khác trong `references/`. Tệp đứng trước thắng khi mâu thuẫn. Thư mục `references/Lich-Su-Khong-Ap-Dung/` không dùng.
2. Văn bản chính quyền: chỉ đạo của Hiệu trưởng ngày 26/10/2026 → **TB 597/TB-CĐKT** và **QĐ 1355/QĐ-CĐKT** → **NĐ 30/2020/NĐ-CP** (chỉ phần Trường chưa quy định). QĐ 389/QĐ-CĐKT chỉ dùng cho phần TB 597 dẫn chiếu sang (dấu, chữ ký số; thành phần khác). Tổ chức, thẩm quyền: **QĐ 1976/QĐ-CĐKT**, **QĐ 2073/QĐ-CĐKT**, QĐ chức năng nhiệm vụ 2041–2054.
3. Văn bản Đảng: **QĐ 208-QĐ/TW** → **HD 05-HD/VPTW** → QĐ 399-QĐ/TW; mẫu đầu văn bản tại Phụ lục TB 597. Đảng bộ Trường là **đảng bộ trực thuộc cơ sở** – áp dụng thẳng, không hỏi lại. Các quy tắc thể thức riêng của Trường ngày 26/10/2026 (A4–A7 bảng 01) **chỉ áp cho văn bản chính quyền**; văn bản Đảng theo HD 05, kể cả dòng chỉ dẫn dưới tiêu đề phụ lục.

## Phạm vi & ngoại lệ
- Dùng cho: (a) rà soát chính thức trước khi trình ký – chế độ **ĐL** (độc lập) hoặc **ĐC** (đối chiếu việc tiếp thu, từ lần 2); (b) rà soát nhanh; (c) so sánh hai bản dự thảo; (d) chuẩn hóa văn phong.
- KHÔNG dùng cho: soạn văn bản mới; chương trình đào tạo, giáo trình, đề cương (`ktc-ktrs-ctdt-gtdt`); giáo án, kế hoạch bài giảng (`ktc-khbg`); ngân hàng câu hỏi thi (`ktc-xay-dung-nhch`); định mức, học phí (`xddm-ktkt-gia-hp-gdnn`); thay thẩm định pháp lý của người có thẩm quyền.
- Trường hợp biên:
  - Câu hỏi chung về một quy định thể thức, không kèm dự thảo → trả lời theo `01-Bang-Thong-So-The-Thuc-KTC.md`, không chạy cổng, không lập báo cáo.
  - Văn bản đã ban hành → vẫn rà; dữ liệu báo cáo ghi `"da_ban_hanh": true`, script gán nhãn “Kiến nghị sửa đổi, bổ sung”.
  - Có báo cáo rà soát lần trước nhưng người dùng yêu cầu “rà soát lại toàn bộ” → chế độ ĐL, vẫn áp cổng lần ≥ 2 (G6–G8).
  - “So sánh hai bản, bản nào hợp lý hơn” → tác vụ (c), không đòi báo cáo rà soát, Báo cáo tiếp thu; cần ĐÚNG HAI bản dự thảo, chỉ chặn khi thiếu (hoặc thừa) bản, thiếu phụ lục hoặc văn bản kèm theo (quyết định của Hiệu trưởng ngày 27/10/2026, PB2-15).

## Lưu ý bảo mật dữ liệu
Người dùng **tự chịu trách nhiệm** không đưa tài liệu mật, tài liệu không được phép lên AI theo **QĐ 2307/QĐ-CĐKT** và **QĐ 2328/QĐ-CĐKT** (quyết định của Hiệu trưởng ngày 26/10/2026, điểm 4); Skill không kiểm và không hỏi lại. Dùng tài khoản Team của Trường.

## Quy trình thực hiện (thứ tự cố định, không bỏ bước)
Đường dẫn `tools/…`, `references/…`, `assets/…` tính từ thư mục chứa SKILL.md. Tệp người dùng gửi thường ở `/mnt/user-data/uploads/` (kể cả thư mục con).

### Bước 0. Xác định tác vụ, hệ văn bản, lần rà soát
1. Chọn đúng một tác vụ (a)–(d).
2. Hệ văn bản: dòng đầu có “CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM” → chính quyền; chỉ có “ĐẢNG CỘNG SẢN VIỆT NAM” → Đảng (script tự nhận, ghi ở Phần I).
3. Lần rà soát (chỉ với (a), (b)): lần 1, hoặc lần ≥ 2 (người dùng nói “rà soát lại”, “sau khi sửa”, “kiểm tra tiếp thu”; hoặc hồ sơ có báo cáo rà soát/dự thảo lần trước).
4. **Quy tắc độc lập (chế độ ĐL)**: trước khi lập xong Phần II nháp, **không mở** báo cáo rà soát lần trước, **tóm tắt rà soát lưu trong Project**, bộ nhớ hội thoại, kết quả tìm kiếm hội thoại cũ hoặc thư mục kết quả cũ về cùng dự thảo. Chỉ mở ở Bước 6 để tìm điều bỏ sót; báo cáo cũ không bao giờ là căn cứ.

### Bước 1. Cổng hồ sơ – bắt buộc, chặn hẳn
Chạy:
```
python3 tools/kiem_ke_ho_so.py <thư mục/tệp người dùng gửi> --tac-vu ra-soat|so-sanh|chuan-hoa --json cong.json
```
(thêm `--vong`, `--du-thao` khi cần; `--vai-tro "<tên tệp>=du_thao|du_thao_cu|bao_cao_ra_soat|bc_tiep_thu|kem_theo|lien_quan"` khi script nhận sai vai trò một tệp – lặp lại cho từng tệp, ghi vào I.7; `--xuat-anh <thư mục>` để xuất ảnh cỡ lớn cần xem; `--xac-nhan-kem "<tệp>=<lý do>"` khi người rà soát xác nhận văn bản kèm theo cùng tên loại mà trích yếu ghi khác – quyết định F1). Quy tắc đầy đủ: `references/Quy-Tac-KTC/05-Cong-Ho-So.md`. Điều kiện CHẶN:
- Có dù chỉ 1 tệp ảnh, bản chụp, PDF scan, tệp nén, Word chủ yếu là ảnh (script chặn); hoặc .doc/.xls/.rtf/.odt. Chỉ nhận .docx, .xlsx; PDF chỉ khi có lớp chữ.
- **Word nhiều chữ nhưng có ảnh ≥ 1/4 trang** (script ghi “PHẢI XEM ẢNH”, trường `anh_can_xem`): AI **bắt buộc mở xem từng ảnh** (chạy lại với `--xuat-anh`, đọc ảnh đã xuất). Ảnh là văn bản chụp/scan (trang văn bản, phiếu, chữ ký, bảng chữ) → **CHẶN theo G1**, gửi thông báo yêu cầu bản chữ; ảnh là sơ đồ, biểu đồ, hình minh họa → nhận, ghi ở I.7 (quyết định của Hiệu trưởng ngày 27/10/2026, PB2-07).
- Thiếu dự thảo; thiếu phụ lục hoặc văn bản kèm theo mà dự thảo nhắc tới. Phụ lục, văn bản kèm theo (Quy định, Quy chế…) có thể nằm trong tệp dự thảo hoặc là **tệp riêng** (script nhận theo tiêu đề đầu tệp, vai trò “kem_theo”; không đòi dòng “(Kèm theo…)” – dòng này là lỗi TT-45). Chỉ coi là “có phụ lục” khi có **tiêu đề** phụ lục thật, không phải câu lời văn nhắc phụ lục. Văn bản kèm theo phải **cùng tên loại và cùng trích yếu** với văn bản mà chính bản dự thảo ban hành, ghép 1:1, kiểm từng văn bản khi một câu liệt kê nhiều văn bản; tệp khác chủ đề, khác loại, không có trích yếu, hoặc là văn bản kèm theo của văn bản đã ban hành không bù được (v4.4–v4.5). Cùng tên loại mà trích yếu ghi khác/không có và người rà soát xác định đúng là văn bản kèm theo → `--xac-nhan-kem "<tệp>=<lý do ≥ 20 ký tự>"` (quyết định F1; ghi vào I.7); `--vai-tro` chỉ sửa vai trò. Tệp trùng tên ở hai thư mục con được ghi bằng đường dẫn tương đối.
- Thiếu toàn văn **bất kỳ văn bản nào dự thảo hoặc tệp phụ lục/văn bản kèm theo đề cập** (căn cứ, lời văn, chú thích; viết đủ hay viết tắt; kể cả mọi luật, nghị định) mà Kho của Skill không có. Viện dẫn chỉ có số (“NĐ 356”, “Quyết định 2307”) được khớp với văn bản DUY NHẤT cùng loại, cùng số trong hồ sơ/Kho; không xác định được → CHẶN, đề nghị ghi đủ số, ký hiệu.
- Tác vụ rà soát từ lần 2: thiếu báo cáo rà soát lần trước, hoặc thiếu **Báo cáo tiếp thu, giải trình** lập thành văn bản riêng, sau báo cáo rà soát, kèm dự thảo đã chỉnh lý.
- **Tác vụ so sánh hai bản** (`--tac-vu so-sanh`): chỉ áp G1–G4 (định dạng tệp; **đúng hai** bản dự thảo – tài liệu tham khảo không được tính là “bản”; đủ phụ lục, văn bản kèm theo của **từng** bản). Văn bản được đề cập chưa có toàn văn **không chặn**; mọi đối chiếu với văn bản đó ghi “Chưa kiểm (chưa có toàn văn)”.

Kết quả CHẶN → gửi **nguyên văn** mục “Thông báo gửi người dùng” của script, liệt kê đủ mọi thiếu sót trong một tin nhắn, rồi **dừng**. Không rà soát tạm, không lập báo cáo, không nhận xét nội dung, không đưa lựa chọn “vẫn làm tiếp” – kể cả khi người dùng yêu cầu.

### Bước 2. Đo thể thức bằng script
Chạy `python3 tools/kiem_tra_the_thuc.py "<dự thảo>.docx" --json tt.json` cho dự thảo và **từng tệp phụ lục/văn bản kèm theo riêng** (với (c) chạy cho cả hai bản); mỗi tệp một tệp JSON. Thước đo: `references/Quy-Tac-KTC/01-Bang-Thong-So-The-Thuc-KTC.md`. Script phân vùng theo vai trò (đầu văn bản, tên loại – trích yếu, Nơi nhận, khối chữ ký, tiêu đề phụ lục, bảng) rồi đo **mọi đoạn lời văn** còn lại, kể cả đề mục “Điều …” và câu ngắn: cỡ chữ (TT-20), khoảng cách đoạn (TT-21), giãn dòng (TT-22), thụt đầu dòng (TT-23); canh đều (TT-24) chỉ xét đoạn **nhiều dòng** – script đếm số dòng thật theo ngắt dòng và bề rộng chữ, đoạn sát ngưỡng ghi “chưa kiểm”; đoạn canh giữa/phải trong thân văn bản vẫn đo; lời văn trong bảng không đo, ghi “chưa kiểm” (quyết định D2 của Hiệu trưởng ngày 27/10/2026). Văn bản chính quyền: giãn dòng chỉ kiểu theo dòng từ Single đến 1,5 lines – Exactly/At least là TT-22 (TB 597 mục 6 được Hiệu trưởng đính chính ngày 27/10/2026, bỏ cụm “hoặc từ 15 pt (exactly line spacing) trở lên”). Văn bản Đảng: khoảng cách thực giữa hai đoạn liền nhau (After đoạn trên + Before đoạn dưới) ≥ 6 pt (quyết định D1), giãn dòng **Exactly** 18–22 pt (HD 05 Phần II mục 6.2.2). Mục “Đạt” ghi số đoạn thực đo. Không đo lại bằng mắt, không sửa mức của script. Dương tính giả → đưa vào `bo_qua_the_thuc` (đúng tệp, đúng vị trí) kèm lý do cụ thể. Mục script báo “chưa kiểm” → Phần I.8, không ghi Đạt, không ghi lỗi.

### Bước 3. Rà soát nội dung (đọc toàn văn mọi văn bản ở bảng I.7)
Theo mục 2, 3, 4 của Mẫu prompt, với các điểm thay thế tại `06-Dieu-Chinh-Mau-Prompt.md`:
1. **Căn cứ**: căn cứ thẩm quyền đứng đầu (QĐ của Hiệu trưởng: QĐ 1976/QĐ-CĐKT); văn bản bị thay thế → CC-01; số, ký hiệu, ngày, trích yếu khớp nguyên văn văn bản được dẫn (CC-03); trích dẫn điều, khoản đúng (CC-04); luật đã sửa đổi viện dẫn theo VBHN mới nhất, theo **mẫu của Trường – không ghi số, ký hiệu luật** (`04-Vien-Dan-Van-Ban-Hop-Nhat.md`, CC-02, CC-06).
2. **Thẩm quyền**: QĐ 1976 Điều 21–22; QĐ 2073 Điều 6 khoản 3, Điều 19; `references/Skill-Library/17-Skill-Kiem-Tra-Tham-Quyen.md`.
3. **Tên đơn vị, cơ sở, tổ chức**: `03-Danh-Muc-Don-Vi-Va-Co-So.md`. Ban Truyền thông (thuộc phòng TH-HC&QT, QĐ 2041), Ban Văn – Thể – Mỹ (QĐ 1997), Tổ Quản trị hệ thống thông tin (QĐ 794, 969) **đã xác minh – không yêu cầu cung cấp văn bản**.
4. **Văn bản Đảng**: `references/Skill-Library/29-Skill-Van-Ban-Dang.md`, `29-Phu-Luc-2…`, `29-Phu-Luc-3…`; không áp NĐ 30 và không áp các quy tắc riêng 26/10/2026 của văn bản chính quyền.
5. **Điều khoản bắt buộc, logic, văn phong** theo loại văn bản; checklist `references/Checklist/`.

### Bước 4. Ma trận đối chiếu chéo (bắt buộc với (a), (c))
1. Rút mọi mệnh đề quy phạm của dự thảo: thời hạn, mốc; con số, tỷ lệ; điều cấm, cho phép, ngoại lệ; thẩm quyền, trách nhiệm, tên đơn vị; định nghĩa; phân loại, danh mục; biểu mẫu, quy trình; hiệu lực, chuyển tiếp.
2. Đối chiếu với **mọi** văn bản liên quan trong hồ sơ và văn bản cùng chủ đề trong Kho – luôn gồm QĐ 1976, QĐ 2073; chủ đề AI, mạng xã hội, an ninh mạng luôn gồm **QĐ 2264, 2307, 2309, 2328**; giao nhiệm vụ cho đơn vị luôn gồm QĐ chức năng nhiệm vụ của đơn vị đó.
3. Kết quả chỉ dùng 6 giá trị: Khớp / Mâu thuẫn / Hẹp hơn / Rộng hơn / Văn bản liên quan không quy định / Chưa kiểm (lý do). “Khớp” chỉ khi cùng **chủ thể, hành vi, mức/thời hạn** (không phải trùng từ khóa) – trích nguyên văn hai phía trong ngoặc kép và ghi `yeu_to_khop`. Mâu thuẫn, Hẹp hơn (chặt hơn), Rộng hơn → DC-01/02/03 **Mức 2** (Mức 1 nếu trái pháp luật/văn bản cấp trên) – kể cả khi dự thảo chặt hơn văn bản đã ban hành như QĐ 2307. Mức, nhóm, tên phân loại không có trong văn bản liên quan cùng chủ đề → DC-06.

### Bước 5. Chế độ ĐC (lần ≥ 2) và tác vụ so sánh
1. So sánh hai bản bằng `python3 tools/so_sanh_ban.py <bản cũ>.docx <bản mới>.docx --json ss.json` (thuật toán cố định). Quét lỗi mới quanh mọi đoạn thay đổi; chạy lại Bước 2 trên bản mới. Tác vụ (c) dùng bảng thay đổi này làm nền cho nhận xét và Bước 4.
2. Lập danh sách mục của báo cáo lần trước, giữ mã cũ. Trạng thái mỗi mục chỉ dùng: Đã sửa đạt / Sửa một phần / Chưa sửa / Không tiếp thu – có giải trình / Không còn áp dụng / Kiến nghị lần trước không còn phù hợp. “Đã sửa đạt” chỉ khi tệp thực đã khắc phục **nguyên nhân cốt lõi** (đo lại hoặc trích nguyên văn mới). Sửa một phần, Chưa sửa → phần còn lại ghi thành phát hiện ở Phần II (`ma_phat_hien`).
3. Không lấy lời khẳng định trong Báo cáo tiếp thu, giải trình thay việc kiểm tệp. Đánh giá lý do “không tiếp thu”: hợp lệ → đóng mục; không hợp lệ → giữ mức, nêu căn cứ.
4. Trước khi kế thừa kiến nghị cũ, kiểm lại với văn bản nguồn; kiến nghị cũ sai → “Kiến nghị lần trước không còn phù hợp” kèm căn cứ đúng (`can_cu_dung`).
5. Bắt buộc kiểm hồi quy (II.C) mọi mục đã đạt ở các lần trước; kiểm Báo cáo tiếp thu khớp số điều, nội dung bản hiện hành.

### Bước 6. Phản biện độc lập
Đổi vai thành người rà soát thứ hai, không mặc định các bước trước đúng: mọi Mức 1–2 có bằng chứng hai phía; mọi Đạt/Khớp có nguyên văn; còn văn bản nào ở I.7 chưa mở; có lỗi nào bị hạ mức; hai dòng trùng vấn đề; hai kiến nghị trái nhau; một vị trí vừa lỗi vừa Đạt. Lúc này mới được mở báo cáo, tóm tắt cũ để tìm điều bỏ sót. Ghi kết quả thật vào `kiem_tra_chat_luong`.

### Bước 7. Dựng báo cáo bằng script
1. Điền dữ liệu theo `assets/Mau-Du-Lieu-Bao-Cao.json` (phát hiện nội dung, ma trận, mục Đạt kèm vị trí, chưa kiểm, đối chiếu, hồi quy, 3–5 vấn đề ưu tiên, kiểm tra chất lượng). **Không điền nhãn, Bảng 1, Bảng 2.** Ghi `kieu_bao_cao`: `chinh_thuc` (tác vụ a), `nhanh` (b), `so_sanh` (c) – phải khớp tác vụ của cổng. Mã phát hiện chỉ lấy trong bảng 02 (script từ chối mã lạ); “Khớp” ghi `yeu_to_khop` dạng `{chu_the, hanh_vi, muc_thoi_han}`, mỗi yếu tố trích **hai phía trong ngoặc kép**; dòng ma trận Mâu thuẫn/Hẹp hơn/Rộng hơn trỏ đúng DC-01/DC-02/DC-03 Mức 1–2 **đặt cùng vị trí (hoặc cha – con)** với dòng ma trận; “Khớp” mà hai phía khác dãy số – đơn vị theo thứ tự, khác phủ định theo từng vế hoặc trái nghĩa bị script từ chối – nếu đọc nghĩa vẫn khớp (ví dụ 3 ngày = 72 giờ) thì ghi `giai_trinh_khop` {<yếu tố>: lý do ≥ 20 ký tự}, in ở Bảng 3 (quyết định F2); “Khớp – có điều khoản thay thế” ghi `nguyen_van_thay_the`; tác vụ (c): vị trí ở ma trận, phát hiện ghi tên tệp như cổng hồ sơ ghi; một vị trí (kể cả vị trí cha – con: “Điều 7” và “Điều 7 khoản 2”) không vừa lỗi vừa Đạt/Khớp. Cổng ghi “PHẢI XEM ẢNH” → điền `xem_anh` cho từng tệp (`tep`, `so_anh_da_xem`, `ket_luan` = `so_do` | `van_ban_chup`, `mo_ta`); có `van_ban_chup` thì hồ sơ CHẶN G1, không lập báo cáo. `bo_qua_the_thuc` chỉ bỏ **từng** phát hiện (đúng `tep` – bắt buộc khi có từ hai tệp đã đo; tên ngắn chỉ nhận khi chỉ đúng một tệp –, đúng `vi_tri` script ghi, `ly_do` cụ thể); phát hiện Mức 1 (CC-01) thêm `nguyen_van` trong ngoặc kép **trích đúng chữ của đoạn script báo**; Mức 1 đã loại được in ở Bảng 2a để người ký xem lại (quyết định E2 ngày 27/10/2026).
2. Chạy `python3 tools/tao_bao_cao.py du_lieu.json --cong cong.json --the-thuc tt.json [--the-thuc tt_quy_dinh.json --the-thuc tt_phu_luc.json …] --chi-kiem` (truyền đủ kết quả đo của mọi tệp dự thảo và phụ lục/văn bản kèm theo; script đối chiếu mã băm tệp với kết quả cổng, từ chối kết quả đo của tệp ngoài hồ sơ); sửa dữ liệu đến khi “HỢP LỆ”; rồi chạy lại với `-o "KTC-Ra-Soat-897_<ten-ngan>_<ddmmyyyy>_BanNhap.docx"`. Tác vụ (c) thêm `--so-sanh ss.json` và điền `so_sanh.ket_luan` (bản nào hợp lý hơn, vì sao).
3. Giao tệp; trả lời ngắn trong khung chat: nhãn, số lỗi theo mức, các mục chặn trình ký, nội dung chưa kiểm được.
4. **Phiên kiểm thử**: khi người dùng nêu “kiểm thử”, “chạy thử”, “ca vàng” hoặc “không lưu Project” → không lưu tóm tắt, báo cáo vào Project hay bộ nhớ (quyết định của Hiệu trưởng ngày 26/10/2026, điểm 6).
Đầu ra theo tác vụ: (a) báo cáo đủ cấu trúc, nhãn trình ký do script tính; (b) cùng khuôn, tiêu đề “BÁO CÁO RÀ SOÁT NHANH…”, kết luận “Rà soát nhanh – không gán nhãn trình ký”; (c) tiêu đề “BÁO CÁO SO SÁNH HAI BẢN…”, thêm II.D bảng thay đổi và “Kết luận so sánh”, không gán nhãn trình ký; (d) trả văn bản chuẩn hóa theo `references/Prompt-Library/03-Chuan-Hoa/`, không lập báo cáo. Prompt chuyên đề: (b) `02-Ra-Soat/`, (c) `05-So-Sanh.md` + Bước 4 + Bước 5 mục 1; vẫn áp bảng thông số, bảng mã mức và quy tắc bằng chứng.

## Quy tắc ổn định kết quả
1. Một hồ sơ – một trình tự: Bước 0 → 7, không đảo, không bỏ.
2. Thông số thể thức là giá trị cố định trong bảng KTC; không dùng khoảng của NĐ 30 khi Trường đã quy định.
3. Mức theo **bảng mã** `02-Quy-Tac-Xep-Muc.md`; mỗi phát hiện có mã; không tự đặt mức ngoài bảng.
4. **Không có bằng chứng hai phía thì không có Mức 1–2**; suy luận, trí nhớ, tóm tắt, báo cáo khác không phải bằng chứng.
5. Một vấn đề = một dòng; gộp vị trí cùng lỗi; không tách để tăng số đếm.
6. Nhãn do script tính theo thứ tự: còn Mức 1 → “Chưa đủ điều kiện ban hành”; còn Mức 2 hoặc “Chưa kiểm” chủ đề trọng yếu → “Cần chỉnh sửa trước khi trình ký”; còn Mức 3 → “Có thể ban hành sau khi chỉnh sửa nhỏ”; còn lại → “Có thể ban hành ngay”. Văn bản đã ban hành: “Kiến nghị sửa đổi, bổ sung”. Không dùng nhãn khác.
7. Từ lượt rà soát thứ 3 cùng văn bản trong một phiên: ghi ở Phần I, khuyến nghị chạy lượt tiếp ở phiên mới.

## Không phải lỗi
- Văn bản kèm theo không có quyền hạn, chức vụ, chữ ký, dấu ở cuối (TB 597 mục 6).
- Phụ lục đánh số trang riêng từ 1 (đúng quy định).
- Căn cứ là Luật, Pháp lệnh không ghi số, ký hiệu, cơ quan ban hành (NĐ 30 PL I Phần II mục 6.a; TB 597 mục 6) – đây là cách viết đúng.
Lưu ý: dòng “(Kèm theo Quyết định… số… ngày…)” dưới tiêu đề phụ lục/văn bản kèm theo **là lỗi** đối với văn bản chính quyền (TT-45, Mức 2); văn bản Đảng thì **phải có** chỉ dẫn phụ lục (HD 05, TT-46).

## Định dạng đầu ra
Báo cáo .docx do `tools/tao_bao_cao.py` dựng theo chuẩn Trường (A4 dọc, Times New Roman 14, lề 2/2/3/2 cm, header/footer 1,27 cm, số trang giữa lề trên cỡ 14, ẩn trang 1; bảng 10–11 pt), trạng thái “BẢN NHÁP RÀ SOÁT – CHƯA ĐƯỢC PHÊ DUYỆT CHÍNH THỨC”, thứ tự cố định: Kết luận điều hành → Phần I (thông tin chung; I.7 kiểm kê hồ sơ; I.8 chưa kiểm được) → Phần II (bảng 8 cột: STT | Mã | Nhóm | Vị trí | Mô tả vấn đề + nguyên văn dự thảo | Căn cứ + nguyên văn căn cứ | Kiến nghị sửa | Mức độ; chế độ ĐC: II.A theo dõi mục cũ → II.B phát hiện → II.C hồi quy; tác vụ (c) thêm II.D bảng thay đổi) → Phần III (mục Đạt kèm số đo/nguyên văn, theo 4 nhóm) → Phần IV (Bảng 1 theo nhóm, Bảng 2 theo mức, Bảng 3 ma trận) → Phần V (mức tuân thủ và nhãn, tự tính) → Phần VI (3–5 vấn đề ưu tiên, rủi ro, kiến nghị) → Kiểm tra chất lượng cuối cùng → Phần VII (khả thi, rủi ro – chỉ khi được yêu cầu) → Thông tin trách nhiệm (Nguồn dữ liệu đã dùng; Người kiểm tra; Trạng thái phê duyệt).
Không chạy được Python → dựng báo cáo thủ công đúng cấu trúc trên, tự tính nhãn theo quy tắc 6 và ghi “dựng thủ công” ở Phần I.

## Checklist chất lượng (trước khi giao)
- [ ] Cổng hồ sơ ĐỦ với đúng `--tac-vu` (đầu ra script ở I.7); nếu CHẶN thì chỉ gửi thông báo chặn.
- [ ] Chế độ ĐL: chưa mở báo cáo, tóm tắt cũ trước khi xong Phần II.
- [ ] Đã chạy `kiem_tra_the_thuc.py` cho dự thảo và mọi tệp phụ lục riêng; không sửa mức của script.
- [ ] Ma trận gồm mọi văn bản liên quan; nhóm AI/MXH/ATTT có QĐ 2264, 2307, 2309, 2328; mọi “Khớp” có `yeu_to_khop`.
- [ ] Mọi Mức 1–2 có nguyên văn/số đo hai phía; mọi Đạt/Khớp có nguyên văn.
- [ ] Ảnh “PHẢI XEM ẢNH” đã được mở xem, ghi `xem_anh` (chặn G1 hoặc nhận).
- [ ] Đã đo thể thức mọi tệp dự thảo và phụ lục/văn bản kèm theo riêng, truyền đủ `--the-thuc`.
- [ ] `tao_bao_cao.py --chi-kiem` báo HỢP LỆ; `kieu_bao_cao` khớp tác vụ; nhãn do script tính.
- [ ] Không hỏi xác minh Ban Truyền thông, Ban Văn – Thể – Mỹ, Tổ Quản trị hệ thống thông tin; không hỏi tên cấp tổ chức đảng.

## Ví dụ minh họa
**Cổng hồ sơ.** Người dùng gửi dự thảo QĐ kèm tệp Word chứa ảnh chụp phiếu góp ý.
- Sai: rà soát dự thảo, ghi “phiếu góp ý chưa đọc được”.
- Đúng: tệp chủ yếu là ảnh → script báo CHẶN (G1). Tệp nhiều chữ kèm ảnh ½ trang → script ghi “PHẢI XEM ẢNH”; AI xem ảnh, thấy là trang văn bản chụp → CHẶN G1; gửi nguyên văn thông báo yêu cầu bản chữ; dừng.

**Số trang văn bản kèm theo.** Quy định kèm theo Quyết định ở section 2, `pgNumType start="1"`.
- Sai: “Đạt – Quy định đánh số riêng”.
- Đúng: TT-34 Mức 2 – phải đánh liên tục với Quyết định; nếu đặt cứng `start="4"` và bản dựng cho thấy Quy định bắt đầu đúng trang 4 → TT-34 Mức 3 (cách thiết lập).

**Đối chiếu chéo** (dự thảo giả định). Dự thảo quy định báo cáo sự cố “trong vòng 24 giờ”; QĐ 2307/QĐ-CĐKT Điều 5 khoản 1 quy định báo “chậm nhất trong ngày làm việc kể từ khi phát hiện”.
- Đúng: ma trận “Mâu thuẫn” kèm nguyên văn hai phía → DC-01 Mức 2 → nhãn “Cần chỉnh sửa trước khi trình ký” (nếu không còn Mức 1).

## Tài nguyên trong gói
- `tools/`: `kiem_ke_ho_so.py` (cổng), `kiem_tra_the_thuc.py` (đo thể thức), `so_sanh_ban.py` (so sánh hai bản), `tao_bao_cao.py` (dựng báo cáo), `README.md`; `legacy/` chỉ tham khảo.
- `references/Quy-Tac-KTC/`: 01 bảng thông số; 02 bảng mã – mức – nhãn; 03 đơn vị, cơ sở, thẩm quyền; 04 viện dẫn VBHN; 05 cổng hồ sơ; 06 điểm thay thế Mẫu prompt.
- `references/Kho-Du-Lieu-897/`: 36 văn bản (35 .docx và 1 PDF scan chỉ tham khảo – HD 02-HD/TW) trong 01-Legal-Database, 02-KTC-Regulations, 03-Don-Vi-Truc-Thuoc, gồm cả Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và NĐ 356/2025/NĐ-CP; bản text của 35 tệp .docx tại `text/`; danh mục máy đọc `kho_manifest.json` (một nguồn duy nhất cho văn bản bị thay thế và VBHN); chỉ mục `00-Chi-Muc-Metadata.md`.
- `references/Skill-Library/`, `references/Checklist/`, `references/Prompt-Library/`, `references/Nguyen-Tac/`: hướng dẫn chuyên đề (phần mâu thuẫn với tệp này thì theo tệp này). `references/Lich-Su-Khong-Ap-Dung/`: hướng dẫn cũ v2.x, không dùng.
- `assets/`: Mẫu prompt chính thức; `Mau-Du-Lieu-Bao-Cao.json` (có ví dụ `xem_anh`, `bo_qua_the_thuc`); template báo cáo trống (tham khảo).
- `references/CHANGELOG.md`: lịch sử phiên bản.

## Quan hệ với hệ khác và giới hạn
- Kho dữ liệu do Phòng TH-HC&QT cập nhật; khi có văn bản mới thay thế văn bản trong Kho hoặc VBHN mới, cập nhật `kho_manifest.json` và bảng 04 (script đọc trực tiếp từ `kho_manifest.json`).
- Báo cáo .docx cần Trưởng/Phó đơn vị phê duyệt trước khi dùng chính thức.
