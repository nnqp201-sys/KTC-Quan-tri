# Kinh nghiệm thực chiến trên Claude Code (máy Phòng TH-HC&QT)

**Phạm vi:** việc thật của Phòng từ 18/9 đến 11/10/2026, do người phụ trách xây dựng bộ công cụ KTC-Quan-tri thực hiện trên Claude Code. Chưa phải kết quả thí điểm tại các đơn vị; không suy ra cho Claude (trò chuyện) và Cowork.
**Nguồn:** `90-Nhat-Ky-Van-Hanh/` (Process Memory, Tri thức tự học, thống kê vận hành), `92-Kinh-Nghiem/` (Lessons, Decision Log, Known Issues), `30-Ket-Qua/`, lịch sử git.
**Quy tắc đã áp dụng:** chỉ nêu điều có nguồn; không nêu họ tên, tài khoản, số liệu nội bộ chi tiết; cột thời gian để trống vì các nguồn không ghi thời gian trước/sau khi dùng AI.

## 1. Bảng tình huống (10 tình huống)

| # | Nhóm | Việc cần làm | Claude Code đã làm gì | Người kiểm tra, sửa gì | Kết quả | Thời gian trước/sau | Nguồn |
|---|---|---|---|---|---|---|---|
| 1 | Theo dõi nhiệm vụ | Chạy thử chốt kỳ báo cáo tháng 8 từ hồ sơ nộp của hơn chục đơn vị | Nhận dạng loại tệp theo tiêu đề sheet (không theo tên tệp); loại dòng tiêu đề trước khi đếm; kiểm công thức quy đổi trên toàn bộ dòng; duyệt ngược từ kế hoạch quý sang báo cáo tháng để tìm nhiệm vụ bỏ sót | Người phụ trách xác nhận các tệp nộp sai mẫu, sai nội dung; phát hiện quy tắc kiểm tra do AI dựng bị sai (xem lỗi 2) | Danh sách bất thường theo đơn vị; bản sửa gói skill v1.1 | | PM-20260913-Chay-thu-BC-thang-8; LL-20260913-001 |
| 2 | Theo dõi nhiệm vụ | Đối chiếu kế hoạch và báo cáo khi phụ lục chưa có mã nhiệm vụ | Đối soát bằng `doi_soat_so_lieu.py`; ghi rõ kết quả là "gần đúng"; lập phiếu đề xuất bổ sung cột Task_ID cho Phụ lục TB 736 | Lãnh đạo xem phiếu và thống nhất bổ sung cột Task_ID | Phiếu đề xuất 1–2 trang có ô ý kiến; Decision Log ghi quyết định | | PM-20260918-Ra-soat-897-CV-KI006-va-Phieu-KI001; DL-20260918-003 |
| 3 | Theo dõi nhiệm vụ | Soạn công văn nhắc các đơn vị bổ sung hồ sơ kế hoạch, báo cáo tháng | Soạn dự thảo; tự rà soát theo 897 bằng cách đo thật (lề, phông, cấu trúc ZIP); đối chiếu căn cứ trong kho; sửa lỗi bằng Track Changes | Người có thẩm quyền quyết các điểm Mức 4 (thời hạn do Lãnh đạo quyết); ô "Người kiểm tra" để trống chờ cán bộ điền | Dự thảo công văn và bản sửa theo rà soát (chưa ban hành) | | PM-20260918-Ra-soat-897-CV-KI006-va-Phieu-KI001 |
| 4 | Số liệu, báo cáo | Báo cáo kết quả tháng 9 và kế hoạch tháng 10 cấp Trường | Ghép phụ lục từ kế hoạch và biểu KPI đơn vị; soạn phần tường thuật; lập ghi chú đối soát | Người phụ trách bổ sung đầu vào còn thiếu; không kết luận "chưa làm" khi đơn vị chưa nộp; công cụ ghép tự động cho văn phong kém nên tường thuật phải soạn tay | Dự thảo báo cáo, 2 phụ lục Excel, ghi chú đối soát (chưa ban hành) | | PM-20260921-Bao-cao-thang-9-va-KH-thang-10 |
| 5 | Số liệu, báo cáo | Dựng báo cáo tháng cấp Trường từ bản đã ban hành của kỳ trước | Viết `bc_thang.py` dựng từ văn bản đã ban hành; chạy thật và sửa 4 lỗi lộ ra | Người phụ trách duyệt quy trình; Decision Log ghi quyết định dùng bản đã ban hành làm nguồn chuẩn | Quy trình dựng báo cáo tháng lặp lại được, có ca hồi quy | | DL-20260928-004; git 28/9 (plugin 1.3.6, 1.3.7) |
| 6 | Số liệu, báo cáo | Lập bản cam kết KPI và danh mục sản phẩm cho viên chức trong Phòng | Điền vào bản sao mẫu Excel của Trường, giữ nguyên công thức; ghi chú cảnh báo thiếu sản phẩm, thiếu minh chứng; đo lại thể thức trước khi giao | Người phụ trách chốt cách xếp Trục (báo cáo, kế hoạch tổng hợp giữ Trục 1; việc quốc phòng xếp Trục 6); bổ sung cả lãnh đạo Phòng vào danh mục; yêu cầu giao bằng Excel thay vì Markdown | Bộ bản cam kết KPI cho toàn Phòng; danh mục bổ sung bằng Excel | | DL-20260924-001; DL-20260925-001; TRI-THUC TT-20260924-02, TT-20260926-02 |
| 7 | Soạn thảo, rà soát | Rà soát đề án (dự thảo lần 3) theo 897 và bổ sung nội dung | Đọc đề án, biên bản kiểm tra, văn bản pháp luật trong kho; sửa bằng Track Changes, lập nhật ký sửa đổi và báo cáo rà soát 8 phần | Người có thẩm quyền điền "Người kiểm tra"; các điểm Mức 4 (nguồn vốn mâu thuẫn, số liệu không có trong kho) để người quyết định | Bản sửa Track Changes, nhật ký sửa đổi, báo cáo rà soát; kết luận "chưa đủ điều kiện trình ký" | | PM-20260920-Ra-soat-897-De-an-Hang-A-lan-3 |
| 8 | Soạn thảo, rà soát | Rà soát 897 hồ sơ trình ban hành bộ công cụ trước khi trình | Rà soát toàn văn; sửa các lỗi Mức 2, Mức 3 bằng Track Changes; chạy `kiem_ho_so.py` trước khi gửi | Người phụ trách ký số, quyết định phương án; giữ bản người phụ trách điều chỉnh là bản chính thức | 0 lỗi Mức 1; sửa 3 Mức 2, 7 Mức 3 (git 10/10) | | git 10/10/2026 "rà soát 897 chính thức hồ sơ trình ban hành"; DL-20261010-001 |
| 9 | Soạn thảo, rà soát | Tiếp thu ý kiến thẩm định độc lập của 5 hệ AI khác | Kiểm từng nhận định trên tệp thật; phân loại độ tin cậy từng hệ theo mã kiểm đọc tệp; viết báo cáo tiếp thu và khắc phục | Người phụ trách quyết định các điều kiện (ví dụ quyền chỉnh sửa tài khoản quản lý kho); AI không đổi quyền Drive | Báo cáo tiếp thu lần 6, báo cáo khắc phục v2, hồ sơ trình thẩm định lần 2 | | DL-20261010-002; PM-20260929-Tiep-thu-tham-dinh-lan-5 |
| 10 | Soạn thảo, rà soát | Giữ chuẩn thể thức văn bản Word, Excel của Trường | Đo thật phông, cỡ chữ, lề bằng `kiem_the_thuc.py`; sửa phông mọi ô ghi vào Excel; xuất PDF xem trang cuối sau mỗi lần sửa Track Changes | Người phụ trách xem bản Word; không mở rồi lưu đè bản Track Changes vì mất dấu vết sửa, lệch mã băm (từ vòng 5 gửi kèm bản sạch, đặt chỉ đọc) | Tệp đo đạt thể thức trước khi giao | | TRI-THUC TT-20260924-06; PM-20260927; PM-20260929 |

## A. Năm lỗi điển hình Claude đã mắc

| # | Lỗi | Phát hiện bằng cách nào | Nguồn |
|---|---|---|---|
| 1 | **Dựng báo cáo từ mẫu trống** thay vì mở văn bản cùng loại đã ban hành trong kho: sai cỡ chữ, sai bố cục, sai chủ ngữ, thiếu một mục lớn, phụ lục để khổ dọc | Người phụ trách bác bỏ sản phẩm vì "không đạt thể thức, văn phong"; đối chiếu với báo cáo đã ban hành | LL-20260913-002 |
| 2 | **Biến bảng gợi ý của dự thảo thành quy tắc kiểm tra**, làm khoảng ba phần tư dòng dữ liệu thật bị báo "vi phạm" | Thấy tỷ lệ vi phạm quá cao nên nghi quy tắc; truy về nguồn thì đó là bảng gợi ý trong dự thảo, không phải quy định ban hành | LL-20260913-001 |
| 3 | **Phép kiểm nhìn nhầm chỗ**: in dấu ✓ "khớp" trong khi gói đang chạy thật chỉ có một nửa nội dung | Rà từng gói đóng gói, so với bản gốc; sửa phép kiểm trước, buộc nó phải báo đỏ trên dữ liệu hiện tại | LL-20260914-001 |
| 4 | **Đọc cắt cụt, không đọc hết tệp chuẩn**: mất quy ước văn phong cấp Trường nằm cuối chú thích; báo sai "chưa có mã/chưa có quyết định" cho một bộ phận trong khi tệp chuẩn đã ghi | Người phụ trách nhắc lại quy ước, kiểm lại thấy đúng; đọc toàn văn tệp chuẩn | LL-20260913-003; TRI-THUC TT-20260924-01 |
| 5 | **Dùng số liệu, căn cứ tra từ web chưa đối chiếu văn bản gốc**: đề án nêu sai điều kiện sát hạch hạng A | Đối chiếu với văn bản gốc trong kho dữ liệu pháp lý của Trường | PM-20260920-Ra-soat-897-De-an-Hang-A-lan-3 |

## B. Năm bài học ngắn cho người mới

1. Có văn bản cùng loại đã ban hành thì mở ra học trước, đừng dựng từ mẫu trống.
2. Bảng số trong dự thảo chỉ là gợi ý; chỉ quy định đã ban hành mới được dùng làm tiêu chí kiểm tra.
3. Căn cứ pháp lý, số liệu phải đối chiếu văn bản gốc; không tin tra cứu web hay tóm tắt của chính AI.
4. Thiếu dữ liệu thì ghi rõ "đối chiếu gần đúng", "không thấy", không kết luận "chưa làm".
5. Kiểm đúng sản phẩm đang chạy thật, đọc toàn văn, và để AI sửa bằng Track Changes để người duyệt thấy từng thay đổi.

## C. Những việc không nên giao cho Claude

- Điền tên người kiểm tra, ký, ký số: để người có thẩm quyền làm (PM-20260918).
- Quyết định các điểm Mức 4 (thời hạn do Lãnh đạo quyết, mâu thuẫn giữa văn bản chưa có kết luận): chỉ nêu, không tự chọn (PM-20260920).
- Kết luận một đơn vị "chưa làm" khi hồ sơ nộp chưa đủ (PM-20260921).
- Chốt cách xếp Trục, điểm KPI của cá nhân khi quy định chưa rõ: người phụ trách chốt (TT-20260926-02).
- Đổi quyền truy cập kho dữ liệu, tài khoản: việc của người phụ trách (DL-20261010-002).
- Xử lý thông tin cá nhân nhạy cảm, tài liệu nội bộ chưa được phép đưa lên nền tảng AI: theo giới hạn của TB 924 (PM-20260927).

## D. Khác biệt khi dùng Claude Code so với trò chuyện thông thường

| Khía cạnh | Claude Code (máy Phòng) | Nguồn |
|---|---|---|
| Đọc, ghi tệp | Làm trực tiếp trong thư mục dự án; chạy được công cụ đo (thể thức, viện dẫn, minh chứng, đối soát số liệu) | `29-Cong-Cu/` |
| Truy vết | Nhật ký tự động theo ngày, lịch sử git, Process Memory sau mỗi ca; lời nhắn có thể ghi chế độ không lưu nội dung (`#riêng`) | TT-20260924-07; CP-20260924-001 |
| Tự học | Kho tri thức gom sửa sai, quy ước, quyết định để nạp vào đầu phiên sau | `05-Tri-Thuc-Tu-Hoc/TRI-THUC.md` |
| Rào chắn | Hook chặn thao tác nguy hiểm (xóa hàng loạt, sửa đè); đã chặn nhầm một số lệnh hợp lệ nên phải chỉnh | PM-20260924; git 27/9, 28/9 |
| Giới hạn | Chưa đo token theo tác vụ; nhật ký chỉ ghi khi làm trong thư mục dự án | `thong_ke_van_hanh.py` mục 5 |

## E. Số liệu vận hành (chỉ dùng nếu anh đồng ý công khai)

Theo `thong_ke_van_hanh.py` (18/9 đến 11/10/2026): 22 ngày làm việc, 59 phiên, 3.865 thao tác công cụ, 210 lượt yêu cầu, 152 lần cập nhật mã nguồn, 0 lỗi do hook ghi nhận. Tín hiệu học: 16 sửa sai, 45 quy ước, 33 quyết định. Số lần gọi kỹ năng là cận dưới. Lưu ý: "0 lỗi" chỉ là lỗi công cụ báo về, không phải lỗi nghiệp vụ.

## F. Chưa có dữ liệu

- Thời gian ước tính trước và sau khi dùng AI: không có trong nguồn.
- Số hiệu văn bản đã ban hành do sản phẩm này tạo ra: chưa có (các sản phẩm đều ở trạng thái dự thảo hoặc đang trình).
- Kết quả thí điểm tại các đơn vị: chưa có (kế hoạch thí điểm chưa triển khai).
- Skill tra cứu kết quả cá nhân trên hệ thống QLVB&ĐH: chưa chạy thật, nên không đưa vào bảng.
