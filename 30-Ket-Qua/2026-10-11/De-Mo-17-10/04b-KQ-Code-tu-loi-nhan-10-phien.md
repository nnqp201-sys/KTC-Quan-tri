# Kinh nghiệm thực chiến trên Claude Code — bổ sung từ lời nhắn thật trong 10 phiên nhóm "KTC-Quan-tri"

**Vì sao có tệp này:** `04-KQ-Code.md` dựng từ nhật ký tự động, Process Memory, Decision Log — các nguồn này không lưu lời nhắn. Tệp này đọc thẳng bản ghi các phiên Claude Code (lời người dùng và câu trả lời của Claude) để bổ sung ba thứ còn thiếu: việc thật theo từng phiên, văn bản đã được ký, lời sửa sai nguyên văn.
**Nguồn:** bản ghi phiên của dự án `KTC-Quan-tri` trên máy Phòng TH-HC&QT, 13/9 - 11/10/2026; 10 phiên trong nhóm "KTC-Quan-tri" ở thanh bên, cộng 01 phiên xây dựng bộ công cụ (ngoài nhóm, ghi rõ khi dùng).
**Quy tắc đã áp dụng:** chỉ nêu điều có trong bản ghi; không nêu họ tên, điểm số cá nhân, số tiền chi tiết; cột thời gian để trống vì trong các phiên người dùng không nói thời gian trước, sau khi dùng AI.

## 1. Bảng tình huống (12 tình huống)

| # | Nhóm | Việc cần làm | Claude đã làm gì | Người phải kiểm tra, sửa gì | Kết quả | Thời gian trước / sau | Ngày, phiên nguồn |
|---|---|---|---|---|---|---|---|
| 1 | Theo dõi nhiệm vụ | Rà soát dự thảo Kế hoạch công tác Quý IV và tháng 10 (Excel), đối khớp kế hoạch năm, quý, tháng và các kế hoạch chuyên đề | Kiểm từng dòng, ghi đề xuất sửa ở cột bên phải ngay trong tệp; bổ sung nhiệm vụ từ kế hoạch chuyên đề theo quy ước màu như Track Changes | Người dùng yêu cầu ghi chú trong chính tệp Excel (không tách tệp riêng), bỏ cụm "Chậm nhất ngày" ở cột thời gian; tự hoàn thiện bản V2 rồi mới giao rà soát 897 | Tệp kế hoạch có ghi chú, đánh dấu màu; số hiệu ban hành: không có dữ liệu | | 22 - 27/9, "Báo-cáo-Kế-hoạch-Quý" |
| 2 | Theo dõi nhiệm vụ | Cụ thể hóa nhiệm vụ của Phòng thành danh mục sản phẩm, công việc và phụ lục cam kết KPI cho viên chức trong Phòng | Đọc quy định chức năng, nhiệm vụ và thông báo phân công; lập danh mục bổ sung; điền phụ lục cam kết theo mẫu của Trường | Người dùng yêu cầu giao bằng Excel thay vì bản ghi chú; phát hiện thiếu lãnh đạo Phòng; yêu cầu bổ sung nhóm việc chương trình, dự án, đề án | Danh mục bổ sung (Excel) và bộ phụ lục cam kết KPI của Phòng | | 19 - 21/9, "Quan-tri-cong-viec-kpi-p.THHCQT" |
| 3 | Theo dõi nhiệm vụ | Lập kế hoạch và tự đánh giá KPI quý của cá nhân từ bảng thống kê văn bản đã xử lý | Điền mẫu kế hoạch, đánh giá; tạo "bảng hỏi" Excel để người dùng trả lời những ô AI không tự biết; tính điểm, ghi rõ "chỉ là đề xuất của cá nhân" | Người dùng chốt cách xếp Trục, trả lời bảng hỏi, yêu cầu sửa lỗi trình bày nhiều lượt (chữ bị che, ô trống) | Bộ kế hoạch và bản tự đánh giá KPI quý III; từ đó hình thành 02 kỹ năng KPI | | 24 - 25/9, "Đánh giá KPI cá nhân Quý" |
| 4 | Theo dõi nhiệm vụ | Lập hồ sơ minh chứng phục vụ đánh giá, xếp loại quý III theo thông báo của Trường | Đọc thông báo, lập bảng tổng hợp minh chứng theo từng nhiệm vụ, bổ sung cột nguồn minh chứng; làm tương tự cho một viên chức khác | Người dùng quyết định nhiệm vụ nào không cần minh chứng, mức vượt; yêu cầu chỉnh thể thức bảng; phát hiện điểm tổng bị đổi (xem lỗi 2) | Hồ sơ minh chứng quý III của 02 viên chức | | 01/10, "Đánh giá KPI cá nhân Quý" |
| 5 | Theo dõi nhiệm vụ | Chuyển danh sách công việc đã giao thành tệp nhập kế hoạch thực hiện nhiệm vụ lên hệ thống của tỉnh | Đưa nội dung từ danh sách công việc vào đúng cột của tệp mẫu nhập | Người dùng kiểm trước khi nhập lên hệ thống | Tệp nhập kế hoạch của Phòng | | 05/10, "Đánh giá KPI cá nhân Quý" |
| 6 | Số liệu, báo cáo | Báo cáo kết quả tháng 9 và kế hoạch tháng 10 cấp Trường theo mẫu Phụ lục TB 736 từ hồ sơ các đơn vị nộp | Tổng hợp phụ lục Excel, soạn báo cáo Word, lập ghi chú đối soát nêu rõ đơn vị chưa nộp | Người dùng chạy lại trên tài khoản khác thì sản phẩm kém bản đầu, yêu cầu "sửa ngay" (xem lỗi 5) | Dự thảo báo cáo, phụ lục, kế hoạch tháng 10; số hiệu ban hành: không có dữ liệu | | 21/9, "Báo-cáo-Kế-hoạch-tháng"; 28/9, phiên xây dựng bộ công cụ |
| 7 | Số liệu, báo cáo | Điều chỉnh hồ sơ chuẩn bị đầu tư một dự án thuộc chương trình mục tiêu quốc gia khi quy mô giảm mạnh | Xác định lại nhóm dự án; sửa quyết định bằng Track Changes; lập bảng tính kinh phí chuẩn bị đầu tư | Người dùng yêu cầu tên dự án đúng nghị quyết và quyết định của tỉnh, chi phí khảo sát giảm theo tỷ lệ quy mô; tự cân đối số liệu cuối | Quyết định phê duyệt nhiệm vụ và dự toán chuẩn bị đầu tư: người dùng báo Hiệu trưởng đã phê duyệt (29/9) | | 24 - 29/9, "CTMTGQ TÍCH HỢP" |
| 8 | Số liệu, báo cáo | Gom tri thức, số liệu, văn bản của 02 chương trình mục tiêu quốc gia và 01 đề án để các phiên sau dùng lại | Đọc hồ sơ người dùng gửi và kho văn bản, viết tệp tri thức chuyên đề | Người dùng đính chính số hiệu nghị định (nêu nhầm rồi sửa lại), yêu cầu tra thêm quy định của tỉnh | 03 tệp tri thức chuyên đề trong dự án | | 20/9 - 07/10, "CTMTQG HIỆN ĐẠI HOÁ GD", "CTMTGQ TÍCH HỢP", "Đề án Trung tâm Đăng kiểm xe cơ giới" |
| 9 | Soạn thảo, rà soát | Soạn Quyết định phê duyệt kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư và Tờ trình kèm theo | Tra kho văn bản và công cụ tìm kiếm; soạn dự thảo; rà soát 897; chuẩn hóa viện dẫn văn bản hợp nhất; qua nhiều bản (đến v8) | Người dùng bắt 02 lỗi căn cứ pháp lý (xem lỗi 1), chê thể thức bản đầu, yêu cầu gộp gói thầu, đổi hình thức lựa chọn nhà thầu; tự chốt bản v9 | **Quyết định số 2236** — người dùng báo Hiệu trưởng đã ký (08/10/2026) | | 29/9 - 08/10, "CTMTGQ TÍCH HỢP" |
| 10 | Soạn thảo, rà soát | Soạn Kế hoạch tổ chức cuộc họp, rồi Thông báo kết luận ngay trong lúc cuộc họp diễn ra | Dựng kế hoạch từ thông báo kết luận giao ban và văn bản mẫu; trong cuộc họp, ráp nội dung chỉ đạo vào dự thảo, tự bỏ tên người, bỏ so sánh với cơ sở khác, nêu chỗ ghi chưa rõ nghĩa để hỏi lại | Người dùng chỉnh kế hoạch rồi cho rà soát 897; để trống hạn thực hiện chờ bổ sung; 02 lần trả lại vì "văn bản chưa bảo đảm", yêu cầu trau chuốt văn phong theo các thông báo kết luận trước | Dự thảo kế hoạch; Thông báo kết luận qua nhiều bản Track Changes; số hiệu ban hành: không có dữ liệu | | 23/9, 06 - 09/10, "Xây-dựng-Kế-hoạch" |
| 11 | Soạn thảo, rà soát | Bổ sung và rà soát 897 đề án, đề cương đề án đào tạo lái xe mô tô; đối chiếu bản người kiểm tra đã sửa tay | Đọc đề án, biên bản kiểm tra, văn bản pháp luật; sửa bằng Track Changes; học văn phong từ một đề án đã hoàn chỉnh; so hai bản và áp lại thay đổi | Người dùng làm sạch đề cương để xin ý kiến Lãnh đạo; sửa tay rồi giao đối chiếu; các điểm chưa đủ căn cứ để người có thẩm quyền quyết | Các bản Track Changes kèm nhật ký sửa đổi; kết luận rà soát "chưa đủ điều kiện trình ký" ở dự thảo lần 3 | | 20 - 22/9, 04/10, "Đề-án-Mô-tô-hạng-A" |
| 12 | Soạn thảo, rà soát | Tiếp thu ý kiến thẩm định của các hệ AI khác và của phòng chuyên môn đối với bộ công cụ; hoàn thiện Thông báo, Hướng dẫn | Kiểm từng nhận định, viết báo cáo tiếp thu, sửa văn bản bằng Track Changes, rà soát 897 trước khi gửi | Người dùng quyết định tiếp thu hay không, quản lý quyền kho dữ liệu, tự chỉnh và gửi hồ sơ | Hồ sơ trình thẩm định lần 2 — người dùng báo đã gửi (10/10/2026) | | 26/9 - 10/10, phiên xây dựng bộ công cụ (ngoài nhóm) |

## A. Năm lỗi điển hình Claude đã mắc (theo lời người dùng trong phiên)

| # | Lỗi | Người dùng phát hiện bằng cách nào | Nguồn |
|---|---|---|---|
| 1 | **Sai căn cứ pháp lý.** Dẫn điều khoản của "chỉ định thầu" cho trường hợp "chỉ định thầu rút gọn"; nhận định dự án nhóm C thuộc chương trình mục tiêu quốc gia được miễn mốc thời gian bố trí vốn 03 năm | Người dùng nắm nghiệp vụ, hỏi lại đúng chỗ ("sẽ khác hoàn toàn"; "có phải không quá 3 năm không?") và yêu cầu tra thêm nguồn; Claude đối chiếu lại điều luật và thừa nhận nhận định sai | 29/9, 07/10, "CTMTGQ TÍCH HỢP" |
| 2 | **Tự đổi số liệu để hai hồ sơ khớp nhau.** Khi lập hồ sơ thứ hai, Claude thấy mâu thuẫn và sửa luôn kết quả một nhiệm vụ ở hồ sơ thứ nhất, làm điểm tổng thay đổi | Người dùng nhớ kết quả đã có, thấy điểm tổng khác và hỏi; yêu cầu quay về số cũ | 01/10, "Đánh giá KPI cá nhân Quý" |
| 3 | **Sai thể thức, hiểu hẹp quy ước của Trường.** Quyết định dự thảo "không đạt về thể thức"; 04 văn bản viết thường sau dấu hai chấm, phải sửa 132 vị trí | Người dùng đọc bản Word ("sau dấu : phải viết hoa cơ mà"); sau đó Claude quét lại toàn bộ bằng công cụ | 29/9, "CTMTGQ TÍCH HỢP"; 28 - 29/9, phiên xây dựng bộ công cụ |
| 4 | **Lỗi trình bày Excel lặp lại.** Dòng che mất chữ, ô để trống, phải nhắc nhiều lượt; có lượt Claude báo đã sửa nhưng chưa tự xem lại trên Excel | Người dùng mở tệp, chụp hình gửi lại ("chưa khắc phục lỗi ở hình gửi lúc nãy") | 25/9, "Đánh giá KPI cá nhân Quý", "Quan-tri-cong-viec-kpi-p.THHCQT" |
| 5 | **Chất lượng không ổn định giữa các lần chạy; hiểu chưa đúng yêu cầu.** Cùng dữ liệu, bản báo cáo tháng chạy lại kém bản đầu; giao bản ghi chú khi người dùng cần Excel; sửa Track Changes chưa đúng tệp người dùng gửi | Người dùng đặt 03 bản cạnh nhau để so; nhắc lại định dạng, tệp cần làm | 28/9, phiên xây dựng bộ công cụ; 19 - 22/9, "Quan-tri-cong-viec-kpi-p.THHCQT", "Báo-cáo-Kế-hoạch-Quý"; 09/10, "Xây-dựng-Kế-hoạch" |

## B. Năm bài học ngắn cho người mới

1. Câu trả lời về pháp lý của AI chỉ là bản nháp: hỏi lại đúng điều, khoản và bắt nó đối chiếu văn bản gốc.
2. Bảo AI sửa bằng Track Changes hoặc ghi chú ngay trong tệp, để mình thấy từng thay đổi.
3. Dặn rõ: thấy số liệu mâu thuẫn thì dừng lại hỏi, không tự sửa cho khớp.
4. Để AI lập "bảng hỏi" những gì nó không biết, mình trả lời, thay vì để nó tự điền.
5. Luôn mở sản phẩm ra xem; thấy lỗi thì chụp hình gửi lại, và so với bản tốt đã có.

## C. Những gì không nên giao cho Claude

- Kết luận cuối cùng về căn cứ pháp lý, thời gian thực hiện dự án, hình thức lựa chọn nhà thầu: người có chuyên môn chốt (lỗi 1).
- Quyết định số liệu nào đúng khi hai nguồn mâu thuẫn; chấm điểm, xếp loại viên chức: Claude chỉ đề xuất (lỗi 2; tình huống 3).
- Hạn thực hiện, nội dung chỉ đạo chưa nghe rõ trong cuộc họp: để trống, hỏi người chủ trì (tình huống 10).
- Chốt bản cuối, trình ký, gửi hồ sơ: người dùng luôn tự làm (tình huống 9, 12).
- Quản lý quyền truy cập kho dữ liệu, tài khoản (tình huống 12).

## D. Chưa có dữ liệu

- Thời gian ước tính trước, sau khi dùng AI: người dùng chưa từng nêu trong các phiên.
- Số hiệu ban hành của báo cáo tháng 9, kế hoạch Quý IV, kế hoạch tháng 10, kế hoạch tổ chức cuộc họp, thông báo kết luận: không có trong bản ghi (cần anh bổ sung nếu đã ban hành).
- Số hiệu Quyết định phê duyệt nhiệm vụ và dự toán chuẩn bị đầu tư: bản ghi chỉ có lời báo "đã phê duyệt", chưa đủ để ghi số.
- Phiên "KTC-quan-tri công việc thường xuyên": chỉ có một yêu cầu khảo sát, không có sản phẩm nên không đưa vào bảng.
