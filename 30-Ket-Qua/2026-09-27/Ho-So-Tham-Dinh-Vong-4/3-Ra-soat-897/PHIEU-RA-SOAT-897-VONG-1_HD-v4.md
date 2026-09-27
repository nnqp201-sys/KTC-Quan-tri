# PHIẾU RÀ SOÁT KTC-897 — VÒNG 1

**Văn bản**: Tài liệu hướng dẫn sử dụng chi tiết bộ công cụ (plugin) KTC-Quan-tri, kèm theo dự thảo Thông báo hướng dẫn sử dụng plugin KTC-Quan-tri
**Tệp**: `30-Ket-Qua/2026-09-26/Ra-Soat/HD_v4_ban-sau-sua_de-ra-soat.docx` (58.402 byte, chữ ký ZIP `504b0304` hợp lệ)
**Công cụ**: Skill `ktc-ra-soat-897:review` (Core v3.0 + baseline v2.24), rà soát chính thức vòng 1
**Mục đích**: Vòng 1/2 theo điểm b Mục 8 Thông báo số 1056/TB-CĐKT ngày 16/9/2026, phần tài liệu hướng dẫn sử dụng
**Ngày rà soát**: 27/9/2026 · Tệp gốc **không bị sửa**

---

## PHẦN I. THÔNG TIN CHUNG

| Mục | Nội dung |
|---|---|
| Loại tài liệu | Tài liệu hướng dẫn kỹ thuật kèm theo Thông báo; có bìa, mục lục (trường TOC), 33 bảng, câu lệnh mẫu; không có Quốc hiệu, số ký hiệu, chữ ký |
| Hệ quy chiếu | **Hệ A (văn bản hành chính, NĐ 30/2020/NĐ-CP, TB 597/TB-CĐKT, Checklist 08), áp ở mức tài liệu kèm theo (tương đương phụ lục)**. Lý do: tài liệu là thành phần của Thông báo hành chính do Hiệu trưởng ký, không phải văn bản Đảng (B), VBQPPL (C) hay đoàn thể (D). Áp đủ: khổ giấy, lề, phông, cỡ chữ, văn phong, tên đơn vị, viện dẫn, tính thống nhất với văn bản chính. **Không áp**: các thành phần thể thức riêng của văn bản chính (Quốc hiệu, số ký hiệu, trích yếu, nơi nhận, chữ ký). Các yếu tố trình bày đặc thù của tài liệu kỹ thuật (màu tiêu đề, ô tô nền, số trang chân trang) đánh giá ở Mức 3–4, không coi là lỗi thể thức Mức 1–2 |
| Nguồn kho 01–04 đã đọc (nội dung thật) | TB 1056/TB-CĐKT ngày 16/9/2026 (`02-KTC-Regulations/1056-TB-CDKT_...docx`): Mục 2, 7, 8, 9; Checklist 08 (tên đơn vị, "nhà trường", viết hoa sau hai chấm); Checklist 01 (dòng "Kèm theo", số trang phụ lục). Số, ngày TB 736, 817, QĐ 1923, QĐ 1976 đã đối chiếu ở phiếu vòng 1 của TB v5 cùng ngày |
| Đối chiếu thực tế plugin (byte thật) | `31-Plugin/.claude-plugin/plugin.json` (1.3.0); `skills/` 8 kỹ năng; `agents/` 7 tác tử; `hooks/hooks.json`; `scripts/ktc_quan_tri_doctor.py` (chuỗi "SessionStart doctor", "guard: HOẠT ĐỘNG", "guard: CHƯA HOẠT ĐỘNG"); `scripts/ktc_nhat_ky.py` (chỉ ghi khi thư mục có `90-Nhat-Ky-Van-Hanh/`, xóa sau 30 ngày, nội dung chỉ khi `#học`/`KTC_NHAT_KY_NOI_DUNG=1`); `CHANGELOG.md` 1.3.0; mã trạng thái, mã cảnh báo trong `skills/*/SKILL.md` |
| Đo thể thức (byte thật) | `ktc897_properties.py`: 1 section, A4 210×297 mm, lề 20/20/30/20 mm. `kiem_the_thuc.py`: 2 gợi ý Mức 3 (TT05: 28 đoạn chữ màu; TT11: không có số trang ở lề trên). python-docx: Normal TNR 14; tiêu đề Heading 1/2 TNR, màu 1F4E78/17365D; chữ trong bảng cỡ 11–13; chân trang "KTC-Quan-tri - Hướng dẫn sử dụng 1.3.0 \| Trang {PAGE}" cỡ 10 màu 666666, không có `titlePg` (bìa cũng hiện số trang); **footer1.xml còn 1 cặp Track Changes chưa chấp nhận** (xóa "1.2.1", chèn "1.3.0"); thân văn bản không có Track Changes |
| Nguồn không tìm thấy | TB 948/TB-CĐKT (17/8/2026): không có trong kho (như phiếu TB v5) |

## PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT

| Mã | Vị trí (trích nguyên văn) | Mô tả vấn đề | Mức | Đề xuất (nguyên văn) | Căn cứ |
|---|---|---|---|---|---|
| M2-01 | Phần IV, đoạn "Mỗi kết quả kết thúc bằng khối gồm…": "DAT, DAT_CO_DIEU_KIEN - được dùng làm sản phẩm chính thức" | Mâu thuẫn nội bộ với Phần IX ("Kết quả AI là tài liệu hỗ trợ; người lập và Lãnh đạo đơn vị chịu trách nhiệm…") và FAQ Phần VIII; trái điểm a Mục 8 TB 1056. Cùng lỗi M2-01 phiếu TB v5 — phải sửa đồng bộ hai tài liệu | 2 | "DAT, DAT_CO_DIEU_KIEN - được dùng làm sản phẩm chính thức" → "DAT, DAT_CO_DIEU_KIEN - được dùng làm cơ sở để người lập, Lãnh đạo đơn vị kiểm tra, hoàn thiện sản phẩm chính thức" | Core severity (Mức 2: logic ảnh hưởng); Skill 15, 18; TB 1056 điểm a Mục 8 |
| M2-02 | Phần III Mục 1, đoạn "Phòng TH-HC&QT cung cấp…": "nhật ký không ghi nội dung chỉ có từ phiên bản này" | Mô tả tuyệt đối, mâu thuẫn với bảng Mục 1 Phần II (nội dung ghi khi mở đầu bằng #học hoặc đặt `KTC_NHAT_KY_NOI_DUNG=1`) và Phần IX ("mặc định không ghi"); khớp mã thật `ktc_nhat_ky.py`. Cùng lỗi M2-03 phiếu TB v5 | 2 | "nhật ký không ghi nội dung chỉ có từ phiên bản này" → "nhật ký mặc định không ghi nội dung chỉ có từ phiên bản này" | Skill 18; Core `mandatory_rules` 8 (kiểm thực tế) |
| M2-03 | Phần IX, đoạn "Sự cố…": "Phòng TH-HC&QT tạm dừng phân phối phiên bản lỗi, báo cáo Lãnh đạo Trường" | Việc phân phối, nạp, cập nhật ở cấp tổ chức thuộc Phòng QLKHCN&HTPT (điểm b Mục 9 TB 1056; chính Mục 2 Phần III tài liệu này). Giao Phòng TH-HC&QT tự tạm dừng phân phối là sai phân công | 2 | "Phòng TH-HC&QT tạm dừng phân phối phiên bản lỗi, báo cáo Lãnh đạo Trường" → "Phòng TH-HC&QT phối hợp Phòng QLKHCN&HTPT tạm dừng phân phối phiên bản lỗi ở cấp tổ chức, báo cáo Lãnh đạo Trường" | TB 1056 điểm b Mục 9, Mục 4; Skill 18 |
| M2-04 | Phần III Mục 4 (tài khoản cá nhân Pro, Max): "Tài khoản Claude miễn phí không dùng được plugin." | Mục 4 hướng dẫn cài và dùng trên tài khoản cá nhân mà không giới hạn dữ liệu, mâu thuẫn Phần IX điểm (2) "dữ liệu nội bộ… chỉ dùng trong tài khoản Claude AI Team của Trường" và điểm (3) dữ liệu cá nhân; liên quan yêu cầu bảo mật Mục 7 TB 1056 | 2 | "Tài khoản Claude miễn phí không dùng được plugin." → "Tài khoản Claude miễn phí không dùng được plugin. Trên tài khoản cá nhân chỉ xử lý văn bản đã ban hành, công khai hoặc dữ liệu giả lập; không xử lý dữ liệu nội bộ, dữ liệu cá nhân (điểm (2), điểm (3) đoạn Phân loại dữ liệu, Phần IX)." | TB 1056 Mục 7; Skill 15 (logic), 18 |
| M3-01 | Khung "DÙNG NHANH…", khung "Bộ công cụ không thực hiện", Phần IV bước 6, FAQ Phần VIII: "KTC-Ra-Soat-897-v2-Cai-tien" (4 lần); Phần VI.6: "checklist KTC-Ra-Soat-897" | Ba cách gọi cùng một công cụ, dùng tên thư mục kỹ thuật có hậu tố phiên bản; TB 1056 Mục 2 gọi Skill "ktc-ra-soat-897". Sửa đồng bộ với M3-01 phiếu TB v5 sau khi đối chiếu TB 948 | 3 | "KTC-Ra-Soat-897-v2-Cai-tien" → "Skill “ktc-ra-soat-897”" (cả 4 chỗ); "checklist KTC-Ra-Soat-897" → "bộ quy tắc của Skill “ktc-ra-soat-897”" | Skill 18; Checklist 04 |
| M3-02 | Toàn văn: tiêu đề bìa, MỤC LỤC, Heading 1/2, dòng đầu các khung (28 đoạn màu 17365D, 1F3864, 1F4E78, 555555) | Ý kiến về cảnh báo TT05: NĐ 30 quy định chữ màu đen cho văn bản và phụ lục. Với tài liệu hướng dẫn kỹ thuật dùng chủ yếu trên màn hình, chữ xanh đậm ở tiêu đề và nền ô nhạt ở đầu bảng **chấp nhận được** nếu tài liệu phát hành dạng tệp điện tử kèm Thông báo; **nên đổi chữ về đen** (giữ nền ô) nếu tài liệu được ký số/đóng dấu như phụ lục hoặc in lưu hồ sơ. Không phải lỗi Mức 1–2 | 3 | Phương án khuyến nghị: đổi màu chữ tiêu đề, dòng đầu khung sang đen (000000), giữ in đậm và nền ô D9EAF7/EAF2F8 | NĐ 30 Phụ lục I; `kiem_the_thuc.py` TT05; Checklist 01 |
| M3-03 | Chân trang: "KTC-Quan-tri - Hướng dẫn sử dụng 1.3.0 \| Trang [PAGE]" | Ý kiến về cảnh báo TT11: NĐ 30 đặt số trang giữa lề trên, không hiện ở trang 1. Với tài liệu kỹ thuật có bìa, số trang chân trang kèm tên tài liệu, phiên bản **chấp nhận được** (giúp nhận diện phiên bản khi in rời). Hai điểm nên sửa: (1) bìa đang hiện "Trang 1" do thiếu thiết lập trang đầu khác (`titlePg`) — nên ẩn; (2) nếu tài liệu được ký số như phụ lục thì chuyển số trang lên giữa lề trên, cỡ 13–14 | 3 | Bật "Different First Page" để bìa không có số trang; giữ chân trang hiện tại, hoặc chuyển số trang lên lề trên nếu phát hành như phụ lục ký số | NĐ 30 Phụ lục I; `kiem_the_thuc.py` TT11; Checklist 01 dòng Phụ lục |
| M3-04 | `word/footer1.xml`: Track Changes chưa chấp nhận (xóa "KTC-Quan-tri - Hướng dẫn sử dụng 1.2.1 \| Trang ", chèn "… 1.3.0 \| Trang ") | Còn sửa đổi tồn đọng ở chân trang; nếu mở chế độ hiện đánh dấu sẽ thấy hai số phiên bản. Phải chấp nhận trước khi phát hành | 3 | Chấp nhận thay đổi ở chân trang (Accept All) trước khi phát hành, giữ bản có Track Changes làm hồ sơ | Core rule 14 (Track Changes); Skill 18 |
| M3-05 | "X. TÀI LIỆU THAM KHẢO" | Đoạn dùng kiểu Normal in đậm, không phải Heading 1 như 9 phần còn lại: không cùng màu, cỡ; khi cập nhật mục lục (trường TOC `\o "1-2"`) Phần X sẽ mất khỏi mục lục | 3 | Gán kiểu Heading 1 cho "X. TÀI LIỆU THAM KHẢO" rồi cập nhật mục lục | Skill 14 (kỹ thuật trình bày), Skill 18 |
| M3-06 | Mục lục và tiêu đề Mục 6 Phần III: "6. Cài phụ trên ChatGPT, Gemini (đối chiếu chéo)"; bảng Mục 1 Phần III: "cài phụ trên ChatGPT, Gemini"; bảng Phần V: "(cài phụ, Mục 6 Phần III)" | "Cài phụ" không phải thuật ngữ hành chính; đồng bộ với M3-04 phiếu TB v5 | 3 | "6. Cài phụ trên ChatGPT, Gemini (đối chiếu chéo)" → "6. Sử dụng trên ChatGPT, Gemini (đối chiếu chéo)"; "cài phụ trên ChatGPT, Gemini" → "sử dụng trên ChatGPT, Gemini"; "(cài phụ, Mục 6 Phần III)" → "(Mục 6 Phần III)" | Checklist 04 |
| M3-07 | Tiêu đề 16 khung câu lệnh: "LỆNH RÚT GỌN - COPY NGUYÊN VĂN" (8 lần), "LỆNH ĐẦY ĐỦ - COPY VÀ ĐIỀN PHẦN TRONG [ ]" (8 lần) | Dùng từ tiếng Anh khi đã có từ tiếng Việt | 3 | "COPY NGUYÊN VĂN" → "SAO CHÉP NGUYÊN VĂN"; "COPY VÀ ĐIỀN PHẦN TRONG [ ]" → "SAO CHÉP VÀ ĐIỀN PHẦN TRONG [ ]" | Checklist 04 (tiếng nước ngoài) |
| M3-08 | Khung trên bìa: "DÙNG NHANH TRONG 60 GIÂY" | Khẩu ngữ, cam kết thời gian không kiểm chứng | 3 | "DÙNG NHANH TRONG 60 GIÂY" → "HƯỚNG DẪN SỬ DỤNG NHANH" | Checklist 04 (văn phong hành chính) |
| M3-09 | Tiêu đề Phần II và mục lục: "II. PLUGIN KHÁC GÌ SKILL - BA NỀN TẢNG SỬ DỤNG" | Tiêu đề dạng câu hỏi, khẩu ngữ, trộn tiếng Anh | 3 | "II. PLUGIN KHÁC GÌ SKILL - BA NỀN TẢNG SỬ DỤNG" → "II. PLUGIN, KỸ NĂNG VÀ CÁC NỀN TẢNG SỬ DỤNG" (sửa cả mục lục) | Checklist 04; Skill 18 |
| M3-10 | Tiêu đề Mục 1 Phần II "1. Plugin và skill"; đoạn đầu Phần II "skill đơn lẻ", "nhiều skill"; bảng Phần I "CHỨC NĂNG (KỸ NĂNG)"; bìa "trên Claude, Cowork, Claude Code" so với "Claude (trò chuyện…)", Phần X "Chat, Cowork, Claude Code" | Thuật ngữ không thống nhất: "skill"/"kỹ năng"/"chức năng"; tên nền tảng Claude/Chat/trò chuyện. TB v5 dùng "kỹ năng – skill" | 3 | Chú thích một lần "kỹ năng (skill)" ở đoạn đầu Phần II, sau đó dùng thống nhất "kỹ năng"; "1. Plugin và skill" → "1. Plugin và kỹ năng"; thống nhất tên nền tảng "Claude (trò chuyện)", "Cowork", "Claude Code" | Skill 18; Checklist 04 |
| M3-11 | Đoạn đầu Phần II: "cài một lần là dùng được toàn bộ" | Mâu thuẫn Mục 2 Phần II: trên Claude (trò chuyện) không có tác tử, thao tác tự động | 3 | "cài một lần là dùng được toàn bộ" → "cài một lần là dùng được các thành phần mà từng nền tảng hỗ trợ (Mục 2 Phần này)" | Skill 15, 18 |
| M3-12 | Mục 5 Phần III, đoạn "Kiểm tra:": "(thường do máy không có Python)" | Không khớp mã thật: doctor là script Python (`hooks.json` gọi `python …ktc_quan_tri_doctor.py`), máy không có Python thì **không hiện dòng nào**, không hiện "CHƯA HOẠT ĐỘNG". Người dùng có thể hiểu sai điều kiện bảo vệ | 3 | "nếu hiện “guard: CHƯA HOẠT ĐỘNG” (thường do máy không có Python)" → "nếu không hiện dòng này (thường do máy không có Python) hoặc hiện “guard: CHƯA HOẠT ĐỘNG”" | Core `mandatory_rules` 8 (kiểm thực tế) |
| M3-13 | Bảng Mục 1 Phần II, dòng 8 kỹ năng: "Với việc KPI cá nhân" | Thiếu động từ, tối nghĩa (đồng bộ M3-03 phiếu TB v5) | 3 | "Với việc KPI cá nhân" → "Với việc lập, tự đánh giá KPI cá nhân" | Checklist 04 |
| M3-14 | Bìa: "TÀI LIỆU HƯỚNG DẪN SỬ DỤNG"; chân trang "Hướng dẫn sử dụng 1.3.0" | TB v5 gọi tài liệu này là "Tài liệu hướng dẫn sử dụng chi tiết"; tên gọi phải thống nhất giữa văn bản chính và tài liệu kèm theo | 3 | "TÀI LIỆU HƯỚNG DẪN SỬ DỤNG" → "TÀI LIỆU HƯỚNG DẪN SỬ DỤNG CHI TIẾT" (hoặc bỏ "chi tiết" ở TB — chọn một) | Skill 18 |
| M3-15 | Khung "Giới hạn khi dùng ChatGPT, Gemini": "Kết quả chỉ dùng đối chiếu chéo, không thay kết quả trên Claude." | Chưa giới hạn loại dữ liệu đưa lên nền tảng ngoài tài khoản Team, trong khi Phần IX điểm (2) chỉ cho dữ liệu nội bộ trong tài khoản Claude AI Team | 3 | "Kết quả chỉ dùng đối chiếu chéo, không thay kết quả trên Claude." → "Kết quả chỉ dùng đối chiếu chéo, không thay kết quả trên Claude; chỉ đưa lên văn bản đã ban hành, công khai hoặc dữ liệu giả lập." | TB 1056 Mục 7; Skill 18 |
| M4-01 | Bìa (không có dòng chỉ dẫn văn bản chính) | Checklist 01: dòng "Kèm theo…" chỉ bắt buộc với văn bản giấy, văn bản điện tử ký số không phải ghi — **không phải lỗi**. Góp ý thêm để tài liệu in rời vẫn truy được về Thông báo | 4 | Góp ý thêm dưới tên tài liệu: "(Kèm theo Thông báo số      /TB-CĐKT ngày    tháng    năm 2026 của Trường Cao đẳng Kon Tum)" | Checklist 01 dòng Phụ lục |
| M4-02 | Phần I, Phần IV, Phần VI.5, Phần VIII, khung ChatGPT: "Thông báo số 736/TB-CĐKT", "Thông báo số 817/TB-CĐKT", "Quyết định số 1923/QĐ-CĐKT", "Thông báo số 948/TB-CĐKT", "Mục 7 Thông báo số 1056/TB-CĐKT" | Lần đầu viện dẫn chưa ghi ngày; chấp nhận được vì văn bản chính (TB v5) đã viện dẫn đầy đủ. Góp ý ghi ngày ở lần đầu nếu tài liệu có thể được dùng rời | 4 | Không bắt buộc | Checklist 08 mục 5.4 |
| M4-03 | FAQ Phần VIII: "theo Thông báo số 948/TB-CĐKT" | TB 948 không có trong kho — chưa xác minh (như M4-03 phiếu TB v5) | 4 | Cung cấp TB 948 để đối chiếu | Cổng nguồn v2.24 |
| M4-04 | Mục 2 Phần III ("Organization settings > Plugins & skills…", "tối đa 50 MB"), Mục 4 ("Tài khoản Claude miễn phí không dùng được plugin"), Mục 6 (đường dẫn ChatGPT, Gemini), Phần X (3 URL, truy cập 26/9/2026) | Chi tiết giao diện, giới hạn, gói dịch vụ của nhà cung cấp không kiểm được bằng kho; có thể thay đổi | 4 | Kiểm lại trên giao diện thật ngay trước khi phát hành; ghi ngày kiểm | Core `uncertainty_handling` |
| M4-05 | Bảng Phần VII, dòng Thể thức: "phụ lục Excel khổ ngang" | Chuẩn thể thức sản phẩm: bảng trên 6 cột dùng A4 ngang **hoặc** đặt vừa chiều rộng trang; ghi tuyệt đối "khổ ngang" hẹp hơn chuẩn | 4 | "phụ lục Excel khổ ngang" → "phụ lục Excel A4, bảng nhiều cột đặt khổ ngang" | `20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md` (TX04) |
| M4-06 | Phần IX: "chỉ mở đầu bằng #học khi muốn Bộ công cụ ghi lại một quy ước để tự học" | Mã thật chỉ ghi nhật ký trong thư mục dự án KTC-Quan-tri (máy Phòng TH-HC&QT, như Phần IX đã nêu); với người dùng các đơn vị, #học không có tác dụng. Góp ý nói rõ phạm vi để tránh hiểu nhầm | 4 | Không bắt buộc | Đối chiếu `ktc_nhat_ky.py` |
| M4-07 | Bìa: "TRƯỜNG CAO ĐẲNG KON TUM" (không có "UBND TỈNH QUẢNG NGÃI") | Tài liệu kèm theo không bắt buộc cơ quan chủ quản; góp ý thêm dòng trên cho nhất quán bộ nhận diện sau sáp nhập | 4 | Không bắt buộc | Quy ước dự án (cơ quan chủ quản) |
| M4-08 | Toàn văn: dấu gạch nối "-" dùng làm gạch ngang ("Kế hoạch - theo dõi - báo cáo định kỳ", "Bước 4 - cập nhật", "DAT… - được dùng") | Góp ý dùng gạch ngang "–" có cách hai bên cho quan hệ liệt kê, giải thích; giữ gạch nối trong tên riêng (TH-HC&QT, Task_ID) | 4 | Không bắt buộc | Checklist 04 |

## PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ

- Khổ A4, lề 20-20-30-20 mm; nội dung Times New Roman 14; tiêu đề TNR; chữ trong bảng cỡ 11–13 (chấp nhận cho bảng, câu lệnh).
- Số liệu kỹ thuật **khớp byte thật plugin**: phiên bản 1.3.0; 8 kỹ năng (tên, mô tả khớp `skills/`); 7 tác tử (khớp `agents/`); chuỗi kiểm tra đầu phiên "KTC-Quan-tri Plugin <phiên bản> — SessionStart doctor", "guard: HOẠT ĐỘNG", "guard: CHƯA HOẠT ĐỘNG"; nhật ký chỉ ghi trong thư mục dự án, xóa sau 30 ngày, nội dung chỉ khi `#học`/`KTC_NHAT_KY_NOI_DUNG=1`; 6 mã trạng thái và 6 mã cảnh báo khớp `SKILL.md`; 8 loại cảnh báo theo dõi; phần A 30 + phần B 70 điểm, chặn trần 100%; Trục chính từ 40%.
- Tham chiếu chéo nội bộ đúng: "Phần III", "Phần VI", "Mục 2 Phần II", "Bước 3, Bước 4 tại Mục 3", "Mục 6 Phần III", "bảng tại Phần I".
- Tên đơn vị trong hành văn đúng cột phải bảng 3.4 Checklist 08: Phòng TH-HC&QT, Phòng QLKHCN&HTPT; tên đầy đủ "Phòng Tổng hợp - Hành chính và Quản trị"; mã đơn vị ví dụ P-THHC, K-KTCN có trong bảng mã chuẩn.
- "nhà trường" viết thường (đúng Checklist 08 mục 2); không có "đảm bảo".
- Phân công QLKHCN&HTPT quản trị Claude AI Team, nạp cấp tổ chức (Mục 2 Phần III): khớp Mục 4, điểm b Mục 9 TB 1056 (trừ M2-03).
- Nguyên tắc AI không quyết định thay người có thẩm quyền, mức xếp loại chỉ là đề xuất (FAQ, Phần IX) nhất quán với QĐ 1923 và TB 1056 (trừ M2-01).
- Dẫn Mục 7 TB 1056 về bảo mật khi dùng nền tảng nước ngoài: đúng nội dung Mục 7.
- Task_ID ví dụ đúng dạng `KTC-YYYY-Qn-NNNNN`.
- Thân văn bản không có Track Changes tồn đọng (chỉ chân trang, M3-04).

## PHẦN IV. BẢNG TỔNG HỢP

| Mức | Số vấn đề | Mã |
|---|---|---|
| Mức 1 — Bắt buộc sửa | 0 | — |
| Mức 2 — Cần sửa | 4 | M2-01 → M2-04 |
| Mức 3 — Nên sửa | 15 | M3-01 → M3-15 |
| Mức 4 — Góp ý / Cần xác minh | 8 | M4-01 → M4-08 |
| **Tổng** | **27** | |

## PHẦN V. THẨM ĐỊNH CHUYÊN MÔN

Không có nội dung thẩm định chuyên môn trong phạm vi phiếu này (thể thức, văn phong, tính thống nhất, không mâu thuẫn). Thẩm định logic vận hành của plugin thuộc điểm (i) điểm b Mục 8 TB 1056.

## PHẦN VI. ĐÁNH GIÁ TỔNG THỂ

Tài liệu trình bày rõ, số liệu kỹ thuật khớp thực tế plugin 1.3.0, tên đơn vị chuẩn. Vấn đề chính: **hai mâu thuẫn nội bộ** về giá trị kết quả AI (M2-01) và nhật ký (M2-02), **một chỗ sai phân công** so với TB 1056 (M2-03), **một khoảng hở bảo mật dữ liệu** với tài khoản cá nhân (M2-04). Nhóm Mức 3 chủ yếu là thống nhất thuật ngữ với TB v5 và văn phong khẩu ngữ ở tiêu đề.

**Ý kiến về hai cảnh báo của công cụ đo**: chữ màu ở tiêu đề, dòng đầu bảng và số trang ở chân trang **chấp nhận được** với loại tài liệu hướng dẫn kỹ thuật phát hành dạng tệp điện tử (Mức 3, không chặn trình). Nếu tài liệu được ký số, đóng dấu như phụ lục của Thông báo thì nên đưa về chữ đen và số trang giữa lề trên; trong mọi trường hợp nên ẩn số trang ở bìa (M3-03).

## PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ

**Kết luận vòng 1**: **Không có vấn đề Mức 1.** Chưa đủ điều kiện phát hành cùng Thông báo cho đến khi xử lý 4 vấn đề Mức 2.

Thứ tự xử lý:
1. Sửa M2-01 → M2-04 trên chính tệp v4, bật Track Changes (nguyên tắc 8); sửa đồng bộ với TB v5 (M2-01, M2-03 phiếu TB).
2. Chấp nhận Track Changes ở chân trang (M3-04), gán Heading 1 cho Phần X và cập nhật mục lục (M3-05).
3. Thống nhất tên công cụ rà soát, "cài phụ", tên tài liệu với TB v5 (M3-01, M3-06, M3-14); xử lý các Mức 3 còn lại.
4. Chạy **vòng 2** phản biện độc lập, không mặc định kết quả vòng 1 là đúng.

## KIỂM TRA CHƯA CHẠY / GIỚI HẠN

- Kết xuất trang (render) để kiểm số trang trong mục lục, ngắt trang bảng, hiển thị màu khi in đen trắng: **chưa chạy** (tốn thời gian; mục lục là trường TOC, số trang hiện có chưa xác minh).
- Agent `ktc897-hieu-luc`, `legal-reviewer`: không gọi — tài liệu không có phần Căn cứ; viện dẫn chỉ ở dạng tham chiếu.
- TB 948/TB-CĐKT: không có trong kho, chưa xác minh (M4-03).
- Giao diện Claude/ChatGPT/Gemini, URL Phần X, giới hạn 50 MB, điều kiện gói dịch vụ: không kiểm được (M4-04).
- Báo cáo DOCX 8 phần (`ktc897_build.py`) và Process Memory: không xuất, theo yêu cầu ghi phiếu Markdown.

## THÔNG TIN TRÁCH NHIỆM

| Trường | Nội dung |
|---|---|
| Nguồn dữ liệu đã dùng | Tệp HD v4 (byte thật); KTC-Database `H:/My Drive/KTC-Database` kho 02 (TB 1056); Checklist 01, 04, 08 và Core ktc-ra-soat-897; `31-Plugin/` (plugin.json, hooks.json, scripts, skills, agents, CHANGELOG); `20-Chuan-Chung/13`, `18`; tệp TB v5 và phiếu vòng 1 TB v5 cùng thư mục |
| Người kiểm tra | ……………… (người có trách nhiệm của Phòng TH-HC&QT ghi) |
| Trạng thái phê duyệt | Bản nháp vòng 1, chờ người có thẩm quyền xem xét |

---
Hệ KTC-Ra-Soat-897 v3.0 | Skill ktc-ra-soat-897 v3.0
