# CHANGELOG – Skill ktc-ra-soat-897

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
