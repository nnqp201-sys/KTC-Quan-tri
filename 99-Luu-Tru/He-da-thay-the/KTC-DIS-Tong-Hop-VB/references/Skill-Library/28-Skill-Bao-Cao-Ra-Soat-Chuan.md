# 28-Skill-Bao-Cao-Ra-Soat-Chuan

## Purpose
Tạo ra một **Báo cáo rà soát văn bản** đầy đủ, chi tiết, có căn cứ — đây là skill "đầu ra chuẩn" cho toàn bộ hoạt động rà soát trong hệ thống, thay thế cho việc chỉ trả lời ngắn gọn "văn bản có X lỗi". Chuẩn mực tham chiếu: file mẫu `Bao_cao_ra_soat_De_an_Dang_kiem_CDKT_lan4_v6.docx` (lưu tại `10-Training-Data/07-Starter-Pack/`).

## When to use
- Người dùng yêu cầu "rà soát", "kiểm tra", "thẩm định" một văn bản/dự thảo/đề án bất kỳ, đặc biệt văn bản dài, nhiều căn cứ pháp lý, hoặc có tính chất quan trọng (Đề án, Tờ trình, Quyết định, Kế hoạch lớn).
- Không dùng cho các yêu cầu chỉnh sửa nhanh, cục bộ (một câu, một đoạn) — khi đó dùng trực tiếp `02-`, `03-`, `04-` mà không cần đóng gói thành báo cáo đầy đủ.

## Inputs
- Toàn văn bản/dự thảo cần rà soát (bắt buộc)
- Tất cả tài liệu đối chiếu do người dùng cung cấp: luật, nghị định, thông tư, quy chế nội bộ, báo cáo tiếp thu giải trình các lần trước, hồ sơ thực tế (giấy tờ đất đai, biên bản, sơ đồ...)
- Bối cảnh: loại văn bản, cơ quan soạn thảo, cơ quan phê duyệt, lĩnh vực chuyên môn, phạm vi rà soát mong muốn

## Cấu trúc báo cáo bắt buộc (7 phần + mục kiểm tra cuối)

### PHẦN I. THÔNG TIN CHUNG
1. Hệ quy chiếu pháp lý/thể thức đã xác định (Bước 0) — xác định văn bản là loại gì (hành chính nhà nước / văn bản Đảng / VBQPPL...) và **nêu rõ căn cứ xác định**, không mặc định.
2. Loại văn bản cụ thể.
3. Cơ quan soạn thảo/đề nghị ban hành; cơ quan có thẩm quyền phê duyệt (nếu khác).
4. Hình thức văn bản (giấy/điện tử ký số) — nếu người dùng không ghi rõ, nêu rõ đang áp dụng giả định nào.
5. Lĩnh vực chuyên môn liên quan (có thể nhiều lĩnh vực cùng lúc).
6. Phạm vi rà soát: liệt kê đầy đủ các phần/phụ lục được rà soát và **giới hạn phạm vi rõ ràng** (ví dụ: không thẩm định chuyên môn tài chính/kỹ thuật sâu, chỉ đối chiếu logic nội bộ).
7. Danh mục đầy đủ tài liệu đã dùng để đối chiếu (liệt kê từng văn bản, có số hiệu, ngày ban hành).
8. Phạm vi và thời điểm xác minh hiệu lực văn bản: ghi rõ ngày rà soát; với văn bản được viện dẫn nhưng KHÔNG có trong hồ sơ cung cấp, phải nêu rõ KHÔNG có điều kiện xác minh độc lập (nếu không có công cụ tra cứu) và đây là khoảng trống cần đơn vị soạn thảo/pháp chế tự xác minh — không suy diễn, không khẳng định hiệu lực khi chưa có căn cứ.
9. Ghi chú về tài liệu tham khảo bổ sung: nếu người dùng cung cấp báo cáo rà soát khác (kể cả do AI khác thực hiện), **không dùng các báo cáo đó làm nguồn căn cứ** — chỉ dựa trên đối chiếu trực tiếp với văn bản gốc.

### PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT
Bảng 7 cột: `STT | Nhóm nội dung | Vị trí | Mô tả vấn đề | Căn cứ nhận xét | Kiến nghị sửa | Mức độ`
- Nhóm nội dung dùng 4 nhóm chuẩn: **Thể thức | Nội dung | Điều khoản bắt buộc | Chất lượng soạn thảo**.
- Vị trí: nêu chính xác trang/phần/mục/bảng/phụ lục.
- Mô tả vấn đề: khách quan, dựa trên đối chiếu, không suy diễn.
- Căn cứ nhận xét: trích dẫn điều/khoản/điểm cụ thể của văn bản pháp luật hoặc tài liệu đối chiếu, có ghi ngày xác minh khi liên quan đến hiệu lực.
- Kiến nghị sửa: cụ thể, khả thi, người soạn có thể áp dụng ngay.
- Mức độ (4 mức, xem thang bên dưới).
- Thứ tự trình bày theo độ ưu tiên: tính hợp pháp → thẩm quyền ban hành → hiệu lực văn bản viện dẫn → điều khoản/nội dung bắt buộc → tính thống nhất nội bộ → thể thức trình bày → chất lượng diễn đạt.

### PHẦN III. CÁC NỘI DUNG KHÔNG PHÁT HIỆN VẤN ĐỀ
Liệt kê rõ theo từng nhóm (Thể thức, Nội dung, Căn cứ đã xác minh chính xác...) những gì đã kiểm tra và ĐẠT — không bỏ qua, vì đây là bằng chứng cho thấy báo cáo rà soát toàn diện chứ không chỉ chăm chăm tìm lỗi.

### PHẦN IV. BẢNG TỔNG HỢP
- Bảng 1: Số lỗi theo nhóm nội dung (Thể thức/Nội dung/Điều khoản bắt buộc/Chất lượng soạn thảo + Tổng cộng).
- Bảng 2: Số lỗi theo mức độ (Mức 1-4).

### PHẦN V. ĐÁNH GIÁ TỔNG THỂ
1. Mức độ tuân thủ pháp luật: Đạt / Đạt có điều kiện / Chưa đạt — kèm lập luận tổng hợp (không chỉ là một câu kết luận trơ, phải liên kết lại các vấn đề Mức 1 quan trọng nhất).
2. Mức độ sẵn sàng phát hành: Sẵn sàng / Cần chỉnh sửa trước khi trình ký / Chưa sẵn sàng — kèm lý do cụ thể.

### PHẦN VI. KẾT LUẬN
- Ưu điểm nổi bật.
- Tồn tại chính cần ưu tiên xử lý (đánh số thứ tự ưu tiên, vấn đề nghiêm trọng nhất nêu trước).
- Mức độ rủi ro nếu không chỉnh sửa (theo từng mức độ vấn đề).
- Kiến nghị chung (ai cần phối hợp, bước tiếp theo).

### PHẦN VII. PHÂN TÍCH TÍNH KHẢ THI VÀ RỦI RO (chỉ khi có yêu cầu bổ sung)
Ghi rõ ngay đầu phần: "Các nhận định dưới đây mang tính tư vấn, dựa trên kinh nghiệm thực tiễn, không phải là lỗi vi phạm quy định." Gồm: (1) Tính khả thi tổng thể; (2) Tính khả thi về nguồn lực (nhân lực, tài chính); (3) Rủi ro khi triển khai; (4) Tính nhất quán của tư duy quản lý; (5) Góc nhìn người thực thi.

### KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG (bắt buộc, luôn để cuối báo cáo)
Tự kiểm tra và ghi lại minh bạch:
- Đã rà soát đủ 4 nhóm tiêu chí chưa.
- Đã đối chiếu với các lần rà soát/tiếp thu trước đó (nếu có) để xác nhận nội dung nào đã được tiếp thu.
- Đã phân biệt rõ "lỗi" (Phần II) / "không phát hiện vấn đề" (Phần III) / "nhận định tư vấn" (Phần VII) — không lẫn lộn.
- Đã ghi rõ nội dung nào CHƯA đủ căn cứ kết luận thay vì suy diễn.
- Không có hai dòng trùng lặp cùng một vấn đề; không có hai kiến nghị mâu thuẫn nhau.
- Nếu văn bản có quy mô rất lớn, nêu rõ đã ưu tiên rà soát sâu phần nào và giới hạn phạm vi ở đâu.

## Khai thác kho Nền tảng dữ liệu (01-04) — bắt buộc, chi tiết theo từng phần báo cáo

Báo cáo rà soát chính thức (dùng Mẫu prompt 897) phải khai thác sâu 4 thư mục dữ liệu nền, không chỉ dựa vào kiến thức chung về Nghị định 30. Áp dụng cụ thể vào từng phần báo cáo như sau:

**Trước khi viết báo cáo (bước chuẩn bị, tương ứng Nguyên tắc 1 tại `00-Nguyen-Tac-Chung.md`):**
1. Xác định loại văn bản, lĩnh vực chuyên môn, đơn vị ban hành của dự thảo.
2. Tìm trong `01-Legal-Database`: (a) văn bản pháp luật quy định trực tiếp thẩm quyền/thủ tục/nội dung bắt buộc của loại văn bản này; (b) văn bản pháp luật thuộc lĩnh vực chuyên môn của dự thảo (ví dụ: dự thảo về tuyển sinh → tìm quy chế tuyển sinh của Bộ).
3. Tìm trong `02-KTC-Regulations`: quy chế/quy định/quy trình nội bộ Trường điều chỉnh trực tiếp nội dung dự thảo (ví dụ: dự thảo tờ trình kinh phí → quy chế chi tiêu nội bộ).
4. Tìm trong `03-Templates`: mẫu chuẩn cùng loại văn bản, dùng để đối chiếu cấu trúc, các trường thông tin bắt buộc.
5. Tìm trong `04-Good-Documents`: văn bản tốt cùng loại/cùng lĩnh vực đã được Trường ban hành, dùng để đối chiếu văn phong, mức độ chi tiết, cách xử lý tình huống tương tự.
6. Ghi lại danh sách đầy đủ các file đã tìm và dùng — đây chính là nội dung mục I.7 (Danh mục tài liệu đối chiếu) của Phần I.

**Áp dụng vào Phần II (Kết quả rà soát chi tiết):**
- Cột "Căn cứ nhận xét" phải ưu tiên trích dẫn cụ thể từ tài liệu tìm được trong 01-02 (số hiệu, điều/khoản) — không trích dẫn khái quát kiểu "theo Nghị định 30" nếu có thể trích đến điều/khoản cụ thể.
- Khi phát hiện dự thảo lệch cấu trúc so với mẫu trong `03-Templates`, ghi rõ tên mẫu đối chiếu và điểm khác biệt cụ thể.
- Khi văn phong/cách trình bày một nội dung khác biệt đáng kể so với các văn bản tốt cùng loại trong `04-Good-Documents`, nêu rõ ví dụ đối chiếu (tên văn bản, cách xử lý) làm cơ sở kiến nghị — không chỉ nói "văn phong chưa chuẩn" mà không có ví dụ đối chiếu.
- Khi một quy chế nội bộ trong `02-KTC-Regulations` có nội dung xung đột hoặc chặt hơn quy định pháp luật chung, ưu tiên áp dụng quy chế nội bộ khi quy chế đó không vi phạm pháp luật, và nêu rõ trong báo cáo là đang áp dụng theo quy chế nội bộ nào.

**Áp dụng vào Phần III (Không phát hiện vấn đề):**
- Khi một nội dung đã được đối chiếu và khớp đúng với văn bản pháp luật (01), quy chế nội bộ (02), mẫu chuẩn (03), hoặc thông lệ tốt (04), ghi rõ đã đối chiếu với tài liệu nào — không chỉ ghi "đạt" mà không nêu đã đối chiếu với gì.

**Khi không tìm thấy tài liệu đối chiếu trong 01-04:**
- Không suy diễn là "không có quy định liên quan" — phải ghi rõ "chưa tìm thấy tài liệu đối chiếu trong kho 01-04 tại thời điểm rà soát" và liệt kê vào phần giới hạn phạm vi (Phần I.6/I.8), đề nghị đơn vị pháp chế/chuyên môn bổ sung xác minh.
- Nếu phiên làm việc hiện tại không có quyền truy cập kho 01-04 (ví dụ chat không kết nối Drive, không có file đính kèm liên quan), phải nói rõ điều này với người dùng trước khi tiến hành rà soát chỉ dựa trên tri thức đóng gói sẵn trong Prompt/Skill Library.

## Thang mức độ (Mức độ nghiêm trọng)
- **Mức 1 – Bắt buộc sửa**: sai căn cứ pháp lý cốt lõi, sai thẩm quyền, thiếu điều khoản bắt buộc, ảnh hưởng trực tiếp tính hợp pháp/khả thi pháp lý. Văn bản KHÔNG được phát hành khi còn Mức 1.
- **Mức 2 – Cần sửa**: lỗi thể thức/nội dung có ảnh hưởng nhưng không làm mất hiệu lực pháp lý ngay.
- **Mức 3 – Nên sửa**: lỗi trình bày, chính tả, thuật ngữ, tính thống nhất nhỏ.
- **Mức 4 – Góp ý nâng cao**: khuyến nghị cải thiện, không phải lỗi.

## Rules (nguyên tắc bắt buộc)
- Mọi nhận xét phải có căn cứ trích dẫn cụ thể (điều/khoản/điểm, số hiệu văn bản, ngày ban hành) — không nhận xét chung chung.
- Khi không có tài liệu để xác minh, PHẢI nói rõ "chưa có điều kiện xác minh" thay vì im lặng bỏ qua hoặc suy diễn có/không hiệu lực.
- Không dùng báo cáo rà soát của công cụ AI khác hoặc bên thứ ba làm nguồn căn cứ pháp lý hoặc số liệu.
- Ghi rõ ngày thực hiện xác minh cho các nội dung liên quan đến hiệu lực văn bản pháp luật.
- Tách bạch nghiêm ngặt giữa lỗi thực sự (Phần II), nội dung đạt yêu cầu (Phần III) và nhận định tư vấn không bắt buộc (Phần VII).
- Với văn bản có phần số liệu tài chính/kỹ thuật chuyên sâu ngoài phạm vi kiểm tra thể thức-pháp lý, chỉ rà soát logic nội bộ (khớp tổng số, khớp tỷ lệ, khớp đánh số), không thẩm định chuyên môn sâu trừ khi được yêu cầu và có đủ căn cứ.

## Must not do
- Không kết luận "đạt" hoặc "không đạt" khi thiếu căn cứ xác minh rõ ràng.
- Không bỏ qua Phần III (nội dung đạt) — báo cáo chỉ liệt kê lỗi sẽ mất tính khách quan và thiếu thuyết phục.
- Không trộn lẫn nhận định tư vấn (Phần VII) vào kết luận về mức độ sẵn sàng phát hành (Phần V).
- Không tạo Mục Kiểm tra chất lượng cuối cùng một cách hình thức — phải phản ánh đúng thực tế đã làm.

## Related
- Prompt: `05-Prompt-Library/02-Ra-Soat.md`
- Skill nền: `02-`, `03-`, `14-`, `15-`, `17-`, `18-`, `19-` (báo cáo này là lớp tổng hợp kết quả của các skill kiểm tra xuyên suốt)
- Template: `03-Templates/03-11- Bao cao ra soat/` (cấu trúc 7 phần)
- Mẫu chuẩn tham chiếu: `10-Training-Data/07-Starter-Pack/02-Bao-Cao-Ra-Soat-Chuan-Sample.md`


## Mẫu con 4.1-4.4 khi trình bày đối chiếu 01-04 trong Phần II (rút từ báo cáo gốc "Đề án Đăng kiểm", bản đối chiếu 01-04 đầy đủ nhất trong hệ thống)
Khi Phần II có nội dung đối chiếu 01-04, nên chia thành 4 tiểu mục thay vì liệt kê rời rạc:
- **4.1 Đối chiếu THỂ THỨC với mẫu tốt (04-Good-Documents):** bảng 4 cột — Tiêu chí | Dự thảo | Mẫu tốt tham chiếu | Đánh giá.
- **4.2 Đối chiếu CĂN CỨ PHÁP LÝ với 01-Legal-Database:** bảng 3 cột — Văn bản trong dự thảo | Có trong 01- không? | Ghi chú vị trí file.
- **4.3 Đối chiếu QUY ĐỊNH NỘI BỘ với 02-KTC-Regulations:** liệt kê quy chế/quyết định nội bộ dự thảo đã trích và đề nghị bổ sung nếu thiếu.
- **4.4 Đối chiếu CẤU TRÚC & NỘI DUNG với 03-Templates + 04-Good-Documents:** bảng 4 cột — Nội dung | Dự thảo | Mẫu tốt/Template | Nhận xét.

Lưu ý: nếu 03-Templates và 04-Good-Documents cùng chứa bản sao của 1 văn bản (mẫu thiết kế cố ý), chỉ cần đối chiếu 1 lần, không lặp lại ở cả 4.1 và 4.4.
