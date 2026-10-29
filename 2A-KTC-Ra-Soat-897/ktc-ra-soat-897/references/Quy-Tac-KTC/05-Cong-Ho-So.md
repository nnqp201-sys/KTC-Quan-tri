# 05 – Cổng hồ sơ bắt buộc (v4.5, 27/10/2026)

Căn cứ: chỉ đạo của Hiệu trưởng ngày 26/10/2026 (mục “cửa chặn bắt buộc” và trả lời điểm 3); QĐ 2073/QĐ-CĐKT Điều 17 khoản 2, Điều 18 (đơn vị chủ trì phải báo cáo bằng văn bản việc tiếp thu, giải trình); quyết định của Hiệu trưởng ngày 26/10/2026 (điểm 3 – so sánh hai bản; điểm 4 – tài liệu mật do người dùng tự bảo đảm).

## 1. Nguyên tắc
- Cổng chạy **trước mọi bước rà soát** với tác vụ rà soát chính thức, rà soát lại (lần 2 trở đi) và so sánh hai bản dự thảo.
- Kết quả chỉ có hai giá trị: **ĐỦ ĐIỀU KIỆN RÀ SOÁT** hoặc **CHẶN – CHƯA ĐỦ HỒ SƠ**.
- Khi CHẶN: **dừng hẳn**. Không rà soát tạm, không rà soát “phần đã có”, không lập báo cáo, không gán nhãn, không đưa lựa chọn “vẫn làm tiếp”. Kể cả khi người dùng yêu cầu làm tiếp, trả lời lại đúng thông báo chặn.
- Chạy bằng script, không tự đánh giá bằng mắt:
  ```
  python3 <thư mục skill>/tools/kiem_ke_ho_so.py <thư mục hoặc các tệp người dùng gửi> [--tac-vu ra-soat|so-sanh|chuan-hoa] [--vong 1|2|...] [--du-thao <tệp>] [--vai-tro "<tên tệp>=<vai trò>" …] [--xuat-anh <thư mục>] --json cong.json
  ```
  Mã thoát 0 = ĐỦ; 2 = CHẶN. Kết quả script đưa nguyên văn vào Phần I.7 của báo cáo (khi ĐỦ) hoặc gửi nguyên văn mục “Thông báo gửi người dùng” (khi CHẶN).

## 2. Điều kiện chặn
| Mã | Điều kiện | Xử lý |
|---|---|---|
| G1 | (v4.4–v4.5, PB4-GPT-05, PB5-WORK-09: tệp Word ngắn có chữ thật – phụ lục danh mục vài dòng, kể cả có biểu trưng nhỏ – được nhận; chỉ chặn “gần như không có chữ” khi dưới 15 ký tự, hoặc dưới 200 ký tự **và** có ảnh ≥ 1/4 trang) Có **dù chỉ 1** tệp ảnh (.png, .jpg, .jpeg, .tif, .bmp, .gif, .webp, .heic), bản chụp, PDF scan (không có lớp chữ), tệp Word chỉ chứa ảnh hoặc **chủ yếu là ảnh** (mỗi ảnh ≥ 1/4 trang ứng với dưới 3.000 ký tự chữ, hoặc có ảnh ≥ 80% trang – script chặn), hoặc **tệp nén** (.zip, .rar, .7z…). Tệp Word **nhiều chữ** có ảnh ≥ 1/4 trang: script ghi “PHẢI XEM ẢNH” (trường `anh_can_xem`; ảnh xuất ra thư mục `--xuat-anh`); AI **bắt buộc mở xem từng ảnh**: ảnh là văn bản chụp/scan (trang văn bản, phiếu, chữ ký, bảng chữ) → CHẶN G1; ảnh là sơ đồ, biểu đồ, hình minh họa → nhận, ghi ở I.7 (quyết định của Hiệu trưởng 27/10/2026, PB2-07) | CHẶN |
| G2 | Có tệp định dạng không nhận (.doc, .xls, .rtf, .odt…) | CHẶN – đề nghị lưu lại sang .docx/.xlsx |
| G3 | Không xác định được dự thảo cần rà soát, hoặc nhiều dự thảo mà không biết bản hiện hành | CHẶN – đề nghị chỉ rõ |
| G4 | Dự thảo nhắc tới Phụ lục (I, II…) hoặc văn bản ban hành kèm theo (Quy định, Quy chế…; nhận cả “Ban hành kèm theo Quyết định/Thông báo/Tờ trình này …”, không phân biệt hoa thường) mà hồ sơ không có. v4.3: phụ lục, văn bản kèm theo nộp thành **tệp riêng** được nhận theo tiêu đề đầu tệp (“Phụ lục I”, “PHỤ LỤC I. …”; “QUY ĐỊNH”, “QUY CHẾ”… không có quốc hiệu, số văn bản) – vai trò “kem_theo”, không đòi dòng “(Kèm theo…)”; tệp có dòng “(Kèm theo <văn bản> số …)” đã điền số là phụ lục của văn bản đã ban hành → văn bản liên quan. Chỉ coi là “có phụ lục” khi có tiêu đề phụ lục thật, không phải câu lời văn (“Phụ lục I là bộ phận …”). **v4.4 (PB4-GPT-01, PB4-WORK-02):** mỗi văn bản kèm theo mà **chính bản** dự thảo ban hành (“ban hành kèm theo Quyết định này Quy định …”) phải có trong bản (sau “Nơi nhận”) hoặc là tệp riêng **cùng tên loại và cùng trích yếu** (≥ 60 % từ có nghĩa trùng nhau); tệp khác loại hoặc khác chủ đề không bù được – CHẶN, nêu tên tệp không khớp. **v4.5 (phản biện lần 5; quyết định F1):** (a) một câu liệt kê nhiều văn bản (“Quy định A và Quy chế B”) được tách và kiểm **từng** văn bản; (b) ghép **1:1** – một tệp chỉ đáp ứng một văn bản kèm theo; (c) khớp trích yếu: từ có nghĩa của bên này phải nằm trọn trong bên kia, từ phủ định (không/chưa/cấm/thiếu) phải có ở cả hai bên; tệp kèm **không có trích yếu** không tự khớp; (d) khi tệp cùng tên loại nhưng trích yếu không khớp/không có (viết tắt…) mà người rà soát xác định đúng là văn bản kèm theo: chạy lại với `--xac-nhan-kem "<tệp>=<lý do ≥ 20 ký tự>"` – cổng ĐỦ, ghi `xac_nhan_kem_thu_cong`, báo cáo in ở I.7; **khác tên loại thì vẫn CHẶN**; `--vai-tro "<tệp>=kem_theo"` chỉ sửa vai trò, không bỏ kiểm khớp. Văn bản kèm theo của văn bản **đã ban hành** (dòng “Kèm theo <văn bản> …” có số – có hay không có chữ “số”, kể cả viết tắt “QĐ 1355/QĐ-CĐKT” (v4.5) – hoặc có ngày đã điền) là văn bản liên quan. Tệp có dòng DỰ THẢO mà tên loại có thể đứng riêng (Kế hoạch, Chương trình, Đề án, Hướng dẫn) và không có dòng “(Kèm theo …)” vẫn là dự thảo (PB4-WORK-09). Phụ lục **của văn bản khác** (“Phụ lục I NĐ 30/2020/NĐ-CP”, “Phụ lục kèm theo QĐ …”, kể cả viết tắt NĐ, QĐ, TT, TB, HD, KH, NQ, CT) không tính | CHẶN |
| G5 | Thiếu toàn văn **bất kỳ** văn bản nào được dự thảo đề cập (căn cứ, lời văn và **chú thích**; viết đủ, viết tắt như “QĐ 2307/QĐ-CĐKT”, hay không có chữ “số”), **kể cả toàn văn mọi luật, nghị định ở phần căn cứ**, mà Kho dữ liệu của Skill không có – quét cả **tệp phụ lục/văn bản kèm theo riêng** (v4.3). Viện dẫn chỉ có số (“NĐ 356”, “Quyết định 2307”, “TB 597”) được khớp với văn bản duy nhất cùng loại, cùng số trong hồ sơ/Kho; không xác định được → CHẶN, đề nghị ghi đủ số, ký hiệu (v4.3). v4.4 (PB4-WORK-01): dạng chỉ có số/rút gọn chỉ gộp vào viện dẫn đầy đủ **cùng loại** (“Nghị định 356/2025/NĐ-CP” không thay cho “Quyết định 356”), không phụ thuộc thứ tự đoạn; v4.5 (PB5-WORK-01): dạng rút gọn (“Nghị định 9090/2026”) chỉ được coi là có toàn văn khi hồ sơ/Kho có văn bản **cùng loại** cùng số, năm; hai viện dẫn rút gọn khác loại cùng số được kiểm riêng. Script nhận cả dạng rút gọn (“Nghị định 13/2023”, “NĐ 356”), số hiệu có chữ thường sau gạch (“749/QĐ-TTg”), luật nêu tên đứng trước văn bản có số (“Luật … và Nghị định số …”), luật kèm “hiện hành/mới nhất” | CHẶN |
| G6 | Lần rà soát thứ 2 trở đi: thiếu báo cáo rà soát lần trước | CHẶN |
| G7 | Lần rà soát thứ 2 trở đi: thiếu **Báo cáo tiếp thu, giải trình** các ý kiến trong báo cáo rà soát lần trước, **lập thành văn bản riêng**, kèm dự thảo đã chỉnh lý | CHẶN |
| G8 | Báo cáo tiếp thu, giải trình lập trước ngày của báo cáo rà soát lần trước (không phải báo cáo tiếp thu kết quả rà soát) | CHẶN |


Tài liệu mật, tài liệu không được phép đưa lên AI (QĐ 2307/QĐ-CĐKT): **người dùng tự chịu trách nhiệm không đưa lên** (quyết định của Hiệu trưởng 26/10/2026, điểm 4). Cổng không kiểm điều này; Skill không hỏi lại.

Áp dụng theo tác vụ:
| Tác vụ | Điều kiện áp dụng | Lệnh |
|---|---|---|
| Rà soát chính thức, rà soát nhanh, rà soát lại | G1–G8 | `--tac-vu ra-soat` (mặc định) |
| So sánh hai bản dự thảo | **G1–G4**: định dạng tệp; **đúng hai** bản dự thảo (tài liệu có số văn bản đã điền hoặc tên tệp không ghi dự thảo/phiên bản không được tính là “bản”; v4.4 (PB4-WORK-08): tài liệu **không có dòng “Số”** chỉ được tính khi tên tệp ghi rõ “dự thảo”; tài liệu tham khảo không bao giờ là “bản”; ba bản trở lên → CHẶN, đề nghị chỉ rõ cặp); đủ phụ lục, văn bản kèm theo của **từng** bản (không lấy nội dung bản này làm bằng chứng cho bản kia). Không đòi báo cáo rà soát, Báo cáo tiếp thu (quyết định 26/10/2026 điểm 3). Văn bản được đề cập chưa có toàn văn **không chặn**; đối chiếu với văn bản đó ghi “Chưa kiểm (chưa có toàn văn)” (quyết định 27/10/2026, PB2-15) | `--tac-vu so-sanh` |
| Chuẩn hóa văn phong | G1–G3 | `--tac-vu chuan-hoa` |

Nhận diện vai trò tệp theo **nội dung** phần đầu, thứ tự cố định (v4.3): (1) dòng tên loại “BÁO CÁO” và tối đa 3 dòng trích yếu liền sau (v4.4–v4.5, PB4-WORK-09, PB5-WORK-10: trích yếu là các dòng **canh giữa** liền sau tên loại; dừng ở dòng không canh giữa, câu kết thúc bằng dấu chấm/chấm phẩy/hai chấm, “Kính gửi”, “Căn cứ”, “Thực hiện”, đề mục) có cả “TIẾP THU” và “GIẢI TRÌNH” → Báo cáo tiếp thu, giải trình (câu lời văn ngắn có hai cụm này không làm đổi vai trò) – kể cả khi trích yếu nhắc “Báo cáo rà soát”; (2) có dòng “DỰ THẢO”/“Dự thảo lần …” riêng, hoặc “Số:” để trống (kể cả kiểu số văn bản Đảng “Số   -NQ/ĐU”) → dự thảo – kể cả dự thảo báo cáo “Rà soát, hệ thống hóa văn bản …”; (3) tiêu đề báo cáo của Skill (“BÁO CÁO RÀ SOÁT DỰ THẢO/CHÍNH THỨC/NHANH/LẦN n”, “BÁO CÁO SO SÁNH HAI BẢN”, “BẢN NHÁP RÀ SOÁT”, “KẾT LUẬN ĐIỀU KIỆN TRÌNH KÝ”) → báo cáo rà soát lần trước; (4) tên tệp chỉ dùng khi nội dung không cho tín hiệu. Phiên bản theo tên tệp: “_V2”, “ v3”, “lần 2”, “bản 2”, “BẢN 3”. Script nhận sai vai trò → chạy lại với `--vai-tro "<tên tệp>=du_thao|du_thao_cu|bao_cao_ra_soat|bc_tiep_thu|kem_theo|lien_quan"` (lặp cho từng tệp); việc chỉ định được ghi trong kết quả cổng, đưa vào I.7. v4.4 (PB4-GPT-04, PB4-WORK-07): hai tệp **trùng tên** ở các thư mục con được phân biệt bằng đường dẫn tương đối (“A/du_thao.docx”, “B/du_thao.docx”) tính từ thư mục gốc chung của mọi đầu vào (v4.5: cả khi truyền nhiều thư mục hoặc nhiều tệp) trong mọi kết quả (vai trò, mã băm, danh sách bản); script ghi chú việc trùng tên; khi chỉ định `--vai-tro`, `--du-thao` dùng đường dẫn đó.

Không chặn:
- Văn bản được đề cập đã bị thay thế (danh sách `van_ban_het_hieu_luc_hay_gap`): không đòi toàn văn văn bản cũ; nếu dự thảo vẫn viện dẫn/áp dụng → CC-01 (Mức 1) khi rà soát; nếu chỉ nêu việc văn bản đó đã được thay thế/bãi bỏ (cụm “thay thế/bãi bỏ” đứng ngay trước hoặc “đã được thay thế” ngay sau số hiệu) → không phải lỗi (v4.3, TH-08). Câu **phủ định** (“chưa được thay thế”, “không bị bãi bỏ”, “chưa hết hiệu lực”, “chưa có văn bản thay thế”) không phải câu nêu việc thay thế → vẫn CC-01 (v4.4, PB4-WORK-03). Câu nêu việc thay thế mà phần còn lại của câu vẫn cho áp dụng (“… đã hết hiệu lực nhưng vẫn áp dụng …”, “… tiếp tục áp dụng …”) → vẫn CC-01 (v4.5, PB5-GPT-04, PB5-WORK-05).
- Văn bản có sẵn trong Kho (`kho_manifest.json`): dùng bản trong Kho.
- Đơn vị, ban, tổ có trong `03-Danh-Muc-Don-Vi-Va-Co-So.md`: không đòi văn bản thành lập.
- Báo cáo tiếp thu, giải trình ý kiến **góp ý** của các đơn vị ở lần rà soát đầu tiên: là tài liệu liên quan, không làm hồ sơ thành “lần 2”.

## 3. Xác định lần rà soát
- Người dùng nói rõ “rà soát lần 2/3…”, “rà soát lại sau khi sửa”, “kiểm tra việc tiếp thu” → lần ≥ 2 (`--vong 2`).
- Hồ sơ có báo cáo rà soát lần trước hoặc dự thảo lần trước, hoặc tên tệp có “sửa lần”, “sau trình”, “lần 2…” → script tự nhận là lần ≥ 2.
- Script nhận sai → chạy lại với `--vong` và `--du-thao`; ghi lý do ở Phần I.

## 4. Thông báo chặn (mẫu cố định – dùng nguyên văn kết quả script)
> Hồ sơ chưa đủ điều kiện rà soát theo chỉ đạo của Hiệu trưởng ngày 26/10/2026. Skill dừng tại bước kiểm kê hồ sơ và **không rà soát tạm**. Đề nghị bổ sung:
> - <từng lý do chặn do script liệt kê>
>
> Sau khi bổ sung, đề nghị gửi lại toàn bộ hồ sơ để rà soát.

Liệt kê **đủ mọi** thiếu sót trong **một** tin nhắn. Không kèm nhận xét về nội dung dự thảo.

## 5. Khi script không chạy được
Môi trường không chạy được Python → thực hiện thủ công đúng các điều kiện G1–G8 (theo tác vụ), lập bảng như đầu ra của script (Danh mục tệp; Văn bản được đề cập) và ghi “kiểm kê thủ công” ở Phần I.7. Không vì thế mà bỏ cổng.
