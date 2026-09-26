# PHIẾU RÀ SOÁT KTC-897 — VÒNG 2 (PHẢN BIỆN)

**Văn bản**: Tài liệu hướng dẫn sử dụng chi tiết bộ công cụ (plugin) KTC-Quan-tri, kèm theo dự thảo Thông báo hướng dẫn sử dụng plugin KTC-Quan-tri
**Tệp rà soát**: `30-Ket-Qua/2026-09-26/Ra-Soat/HD_v4_ban-sau-sua-vong-1_de-ra-soat-vong-2.docx` (58.584 byte, chữ ký ZIP `504b0304` hợp lệ; bản sạch, không có Track Changes trong `document.xml`, `footer1.xml`)
**Tệp đối chiếu**: phiếu vòng 1 `PHIEU-RA-SOAT-897-VONG-1_HD-v4.md`; bản trước sửa `HD_v4_ban-sau-sua_de-ra-soat.docx`; Thông báo đi kèm `TB_v5_ban-sau-sua-vong-2.docx`; phiếu vòng 2 TB `PHIEU-RA-SOAT-897-VONG-2_TB-v5.md`; bản theo dõi thay đổi `30-Ket-Qua/2026-09-26/Soan-Thao/HD_Huong-dan-chi-tiet-su-dung-KTC-Quan-tri_20260926_v4_TrackChanges.docx`
**Công cụ**: Skill `ktc-ra-soat-897:review` (Core v3.0 + baseline v2.24), rà soát chính thức vòng 2
**Mục đích**: Vòng 2/2 theo điểm b Mục 8 Thông báo số 1056/TB-CĐKT ngày 16/9/2026 — **đổi vai trò phản biện, không mặc định kết quả vòng 1 là đúng**
**Ngày rà soát**: 27/9/2026 · Tệp **không bị sửa**

---

## PHẦN I. THÔNG TIN CHUNG

| Mục | Nội dung |
|---|---|
| Hệ quy chiếu | Hệ A (NĐ 30/2020/NĐ-CP, TB 597/TB-CĐKT, Checklist 08) áp ở mức tài liệu kèm theo, giữ như vòng 1. Không áp thành phần thể thức riêng của văn bản chính |
| Cách kiểm | So khớp văn bản toàn văn bản trước sửa với bản sau sửa (bóc chữ từ XML, chấp nhận thay đổi) → 47 đoạn khác nhau, đều thuộc các mã vòng 1; đọc lại toàn văn bản sau sửa; đối chiếu từng khẳng định chung với TB v5 bản sau sửa vòng 2 |
| Nguồn kho 01–04 đã đọc (nội dung thật) | TB 1056/TB-CĐKT (`H:/My Drive/KTC-Database/02-KTC-Regulations/1056-TB-CDKT_Huong-dan-su-dung-Skill-tao-Skill-va-Prompt_20260916_v1.docx`): điểm a Mục 2 (ví dụ “Skill “ktc-ra-soat-897” dùng để rà soát văn bản hành chính”), Mục 4, Mục 7 (bảo mật: nền tảng AI công cộng, chuyển dữ liệu cá nhân ra nước ngoài), điểm b Mục 8, Mục 9 |
| Đối chiếu mã thật plugin | `31-Plugin/hooks/hooks.json` (SessionStart gọi `python …/ktc_quan_tri_doctor.py`); `31-Plugin/scripts/ktc_quan_tri_doctor.py` dòng 79, 81: chuỗi “guard: CHƯA HOẠT ĐỘNG” chỉ in khi Python chạy được nhưng tự thử chặn ghi thất bại |
| Đo thể thức (byte thật) | `ktc897_properties.py`: 1 section, A4 210×297 mm, lề 20/20/30/20 mm. `kiem_the_thuc.py`: 2 gợi ý Mức 3 (TT05: **30** đoạn chữ màu, tăng 2 so với vòng 1 do “X. TÀI LIỆU THAM KHẢO” nay là Heading 1; TT11). python-docx: “X. TÀI LIỆU THAM KHẢO” kiểu Heading 1; `sectPr` có `footerReference type="first"` (footer2.xml rỗng) nhưng **không có `<w:titlePg/>`** |
| Track Changes | Bản rà soát là bản sạch. Bản nguồn `…_v4_TrackChanges.docx` (Soan-Thao) có 170 thẻ `w:ins`/`w:del` ngày 27/9/2026, chứa 16 lần “SAO CHÉP”, 5 lần “ktc-ra-soat-897” → lần sửa có theo dõi thay đổi, đạt nguyên tắc 8 |
| Nguồn không tìm thấy | TB 948/TB-CĐKT (17/8/2026): quét lại kho 02, không có (như vòng 1) |

## PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT

### A. Kiểm tra xử lý các vấn đề vòng 1

| Mã vòng 1 | Hướng xử lý của đơn vị soạn thảo | Đánh giá vòng 2 | Bằng chứng (trích nguyên văn bản sau sửa) | Ghi chú phản biện |
|---|---|---|---|---|
| M2-01 | Sửa | **Đã sửa đúng** | “DAT, DAT_CO_DIEU_KIEN - được dùng làm cơ sở để người lập, Lãnh đạo đơn vị kiểm tra, hoàn thiện sản phẩm chính thức” | Hết mâu thuẫn với Phần IX, FAQ; khớp nghĩa TB v5 (“được dùng làm cơ sở để đơn vị, người soạn thảo kiểm tra, hoàn thiện sản phẩm chính thức”). Còn lệch nhẹ với TB ở cách xử lý DOI_CHIEU_GAN_DUNG → N3-04 |
| M2-02 | Sửa | **Đã sửa**, còn tồn dư câu chữ | “thao tác chặn ghi kho dữ liệu, nhật ký mặc định không ghi nội dung chỉ có từ phiên bản này” | Nghĩa đã đúng mã thật, nhưng chuỗi “không ghi nội dung chỉ có từ” đọc được hai cách → N3-02 (cùng lỗi N3-03 phiếu vòng 2 TB) |
| M2-03 | Sửa | **Đã sửa đúng** | “Phòng TH-HC&QT phối hợp Phòng QLKHCN&HTPT tạm dừng phân phối phiên bản lỗi ở cấp tổ chức, báo cáo Lãnh đạo Trường” | Khớp Mục 2 Phần III tài liệu và phân công tại TB v5 Mục III.2. TB v5 Mục III.1 điểm d chưa ghi “phối hợp” → góp ý N4-04 |
| M2-04 | Sửa | **Đã sửa**, phát sinh vấn đề mới | “Trên tài khoản cá nhân chỉ xử lý văn bản đã ban hành, công khai hoặc dữ liệu giả lập; không xử lý dữ liệu nội bộ, dữ liệu cá nhân (điểm (2), điểm (3) đoạn Phân loại dữ liệu, Phần IX).” | (1) Điểm (3) Phần IX không có giới hạn “chỉ trong tài khoản Team” nên dẫn chiếu không khớp → N3-05. (2) TB v5 Mục I.2 vẫn nêu tài khoản Pro, Max là điều kiện đủ, không có giới hạn này → mâu thuẫn giữa văn bản chính và tài liệu kèm theo → **N2-02** |
| M3-01 | Sửa (thống nhất theo TB 1056) | **Đã sửa đúng** | 5 chỗ: “bằng Skill “ktc-ra-soat-897””, “(dùng Skill “ktc-ra-soat-897”)”, “checklist của Skill “ktc-ra-soat-897””, “Dùng Skill “ktc-ra-soat-897” theo Thông báo số 948/TB-CĐKT” | Đã kiểm kho: TB 1056 điểm a Mục 2 gọi đúng “Skill “ktc-ra-soat-897””; khớp TB v5 Mục I.1, II.4. Không còn “KTC-Ra-Soat-897-v2-Cai-tien”. Chữ “Skill” viết hoa ở đây là tên riêng theo TB 1056 — chấp nhận, nhưng làm rõ thêm nhu cầu xử lý M3-10 |
| M3-02 | Chấp nhận theo ý kiến vòng 1 | **Chấp nhận có điều kiện** | 30 đoạn chữ màu (TT05) | Ý kiến vòng 1 chỉ chấp nhận khi phát hành dạng tệp điện tử. TB v5 Mục I.3 Lưu ý ghi tài liệu “kèm theo Thông báo này” — nếu Văn thư ký số kèm Thông báo thì phải đổi chữ về đen. Người có thẩm quyền cần chốt hình thức phát hành trước khi ký |
| M3-03 | Chấp nhận theo ý kiến vòng 1 | **Chưa xử lý phần bắt buộc — lý do chưa đủ** | `sectPr` có chân trang trang đầu (footer2.xml rỗng) nhưng thiếu `<w:titlePg/>` → bìa vẫn hiện “KTC-Quan-tri - Hướng dẫn sử dụng 1.3.0 \| Trang 1” | Vòng 1 kết luận: “trong mọi trường hợp nên ẩn số trang ở bìa”. “Chấp nhận theo ý kiến vòng 1” chỉ bao phần giữ số trang ở chân trang, không bao phần ẩn số trang ở bìa. Chân trang rỗng cho trang đầu đã có sẵn, chỉ cần bật “Different First Page”. Giữ Mức 3 |
| M3-04 | (không nêu) | **Đã xử lý** | `footer1.xml` không còn `w:ins`/`w:del`; chữ “KTC-Quan-tri - Hướng dẫn sử dụng 1.3.0 \| Trang” | Đạt |
| M3-05 | Sửa | **Đã sửa đúng** | “X. TÀI LIỆU THAM KHẢO” — kiểu Heading 1; mục lục có dòng “X. TÀI LIỆU THAM KHẢO 16” | Đạt. Số trang trong mục lục chưa kiểm bằng kết xuất (xem Kiểm tra chưa chạy) |
| M3-06 | Sửa | **Đã sửa đúng** | “6. Sử dụng trên ChatGPT, Gemini (đối chiếu chéo)” (tiêu đề và mục lục); “sử dụng trên ChatGPT, Gemini”; “ChatGPT, Gemini (Mục 6 Phần III)” | Không còn “cài phụ”; khớp TB v5 Mục I.3 điểm d |
| M3-07 | Sửa | **Đã sửa đúng** | 8 lần “LỆNH RÚT GỌN - SAO CHÉP NGUYÊN VĂN”, 8 lần “LỆNH ĐẦY ĐỦ - SAO CHÉP VÀ ĐIỀN PHẦN TRONG [ ]” | Không còn “COPY” |
| M3-08 | Sửa | **Đã sửa đúng** | “HƯỚNG DẪN SỬ DỤNG NHANH” | Đạt |
| M3-09 | Sửa | **Đã sửa**, phát sinh vấn đề mới | “II. PLUGIN, KỸ NĂNG VÀ CÁC NỀN TẢNG SỬ DỤNG” (tiêu đề và mục lục) | Tiêu đề phần nay dùng “KỸ NĂNG”, tiểu mục ngay dưới vẫn “1. Plugin và skill” → N3-01 |
| M3-10 | **Bảo lưu** (để lần sửa sau thống nhất toàn bộ thuật ngữ skill/kỹ năng) | **Bảo lưu — lý do đủ một phần** | Còn “1. Plugin và skill”; “là skill đơn lẻ”; “tích hợp nhiều skill”; Phần X “plugin dùng được trên Chat, Cowork, Claude Code” | Đủ lý do với phần tên nền tảng (Chat/trò chuyện) và các nhãn trong bảng — việc rộng, không làm lệch nghĩa. **Chưa đủ lý do** với 3 chỗ ở Mục 1 Phần II: lần sửa M3-09 đã đưa “KỸ NĂNG” vào tiêu đề phần, nay tiêu đề phần và tiểu mục dùng hai từ khác nhau cho cùng khái niệm; thêm dạng thứ ba “Skill” (tên riêng) do M3-01. TB v5 đã có cách làm mẫu: chú thích “kỹ năng – skill” một lần rồi dùng “kỹ năng”. Đề nghị sửa ngay phần tối thiểu → N3-01 |
| M3-11 | Sửa | **Đã sửa đúng** | “cài một lần là dùng được các thành phần mà từng nền tảng hỗ trợ (Mục 2 Phần này)” | Dẫn chiếu “Mục 2 Phần này” đúng (Mục 2 Phần II “Ba nền tảng Claude”) |
| M3-12 | Sửa (diễn đạt khác đề xuất) | **Đã sửa đúng** | “nếu không hiện dòng “guard: HOẠT ĐỘNG” (hiện “CHƯA HOẠT ĐỘNG”, hoặc cả phần kiểm tra đầu phiên không hiện do máy không có Python)” | Khớp mã thật (`ktc_quan_tri_doctor.py` dòng 79, 81; hooks.json gọi `python`). Nhưng TB v5 vẫn giữ mô tả cũ → **N2-01** |
| M3-13 | Sửa | **Đã sửa đúng** | “Với việc lập, tự đánh giá KPI cá nhân” | Khớp TB v5 (“đối với việc lập, tự đánh giá KPI cá nhân”) |
| M3-14 | Sửa | **Đã sửa đúng** | Bìa: “TÀI LIỆU HƯỚNG DẪN SỬ DỤNG CHI TIẾT” | Khớp TB v5 (“Tài liệu hướng dẫn sử dụng chi tiết Bộ công cụ KTC-Quan-tri”). Chân trang giữ “Hướng dẫn sử dụng 1.3.0” → góp ý N4-05 |
| M3-15 | Sửa | **Đã sửa đúng** | “Chỉ đưa văn bản đã ban hành, công khai hoặc dữ liệu giả lập lên các nền tảng này.” | Phù hợp TB 1056 Mục 7 |
| M4-01 → M4-08 | Không nêu | Không xử lý (góp ý) | — | Chấp nhận; M4-03 (TB 948) vẫn chưa xác minh được |

### B. Vấn đề mới phát hiện ở vòng 2

| Mã | Vị trí (trích nguyên văn) | Mô tả vấn đề | Mức | Đề xuất (nguyên văn) | Căn cứ |
|---|---|---|---|---|---|
| N2-01 | **TB v5** Mục I.1 điểm b, gạch đầu dòng “Các thao tác tự động (hooks)…”: “không chạy khi máy thiếu Python (đầu phiên báo “guard: CHƯA HOẠT ĐỘNG”)”; đối chiếu **HD** Mục 5 Phần III: “hoặc cả phần kiểm tra đầu phiên không hiện do máy không có Python” | Mâu thuẫn trực tiếp giữa văn bản chính và tài liệu kèm theo về dấu hiệu nhận biết mất bảo vệ ghi kho. Mã thật: thiếu Python thì hook `python …doctor.py` không chạy, **không có dòng nào**; “CHƯA HOẠT ĐỘNG” chỉ in khi Python chạy nhưng tự thử chặn ghi thất bại. HD (sau M3-12) đúng; TB sai. Người dùng làm theo TB, không thấy cảnh báo, sẽ tưởng vẫn được bảo vệ — ảnh hưởng an toàn dữ liệu | 2 | Sửa ở **TB v5**: “không chạy khi máy thiếu Python (đầu phiên báo “guard: CHƯA HOẠT ĐỘNG”)” → “không chạy khi máy thiếu Python (khi đó đầu phiên không hiện dòng “guard: HOẠT ĐỘNG”)” | Core severity (Mức 2: mâu thuẫn logic ảnh hưởng thực hiện); Skill 15, 18; Core `mandatory_rules` 8 (kiểm thực tế); `31-Plugin/scripts/ktc_quan_tri_doctor.py` dòng 79, 81; `31-Plugin/hooks/hooks.json` |
| N2-02 | **TB v5** Mục I.2: “Tài khoản Claude AI Team do nhà trường cấp theo Thông báo số 924/TB-CĐKT ngày 11 tháng 8 năm 2026, hoặc tài khoản Claude trả phí (Pro, Max).”; đối chiếu **HD** Mục 4 Phần III: “Trên tài khoản cá nhân chỉ xử lý văn bản đã ban hành, công khai hoặc dữ liệu giả lập; không xử lý dữ liệu nội bộ, dữ liệu cá nhân” và Phần IX điểm (2): “dữ liệu nội bộ (kế hoạch, báo cáo đơn vị) - chỉ dùng trong tài khoản Claude AI Team của Trường” | TB nêu tài khoản Pro, Max ngang hàng tài khoản Team là điều kiện đủ để dùng Bộ công cụ cho toàn chu kỳ (kế hoạch, báo cáo đơn vị, KPI cá nhân) và Mục I.1 điểm c ghi Claude “phù hợp lập kế hoạch, báo cáo của đơn vị”; HD cấm xử lý đúng các dữ liệu đó trên tài khoản cá nhân. Văn bản chính và tài liệu kèm theo quy định khác nhau về phạm vi dữ liệu. Vòng 1 (cả phiếu TB và HD) bỏ sót; lần sửa M2-04 làm lộ rõ | 2 | Sửa ở **TB v5**: “hoặc tài khoản Claude trả phí (Pro, Max).” → “hoặc tài khoản Claude trả phí (Pro, Max); trên tài khoản cá nhân chỉ xử lý văn bản đã ban hành, công khai hoặc dữ liệu giả lập, không xử lý dữ liệu nội bộ, dữ liệu cá nhân.” | Skill 18 (thống nhất văn bản chính – tài liệu kèm theo); TB 1056 Mục 7; Core severity Mức 2 |
| N3-01 | Mục 1 Phần II (tiêu đề và mục lục): “1. Plugin và skill”; đoạn đầu: “là skill đơn lẻ”, “một gói tích hợp nhiều skill” | Phát sinh do sửa M3-09: tiêu đề Phần II dùng “KỸ NĂNG”, tiểu mục ngay dưới dùng “skill”; cùng tài liệu còn “kỹ năng”, “Skill” (tên riêng). Phần tối thiểu của M3-10, không nên để lần sau | 3 | “1. Plugin và skill” → “1. Plugin và kỹ năng” (cả mục lục); “là skill đơn lẻ” → “là kỹ năng (skill) đơn lẻ”; “một gói tích hợp nhiều skill” → “một gói tích hợp nhiều kỹ năng” | Skill 18; Checklist 04; cách dùng tại TB v5 Mục I.1 điểm b (“kỹ năng – skill”) |
| N3-02 | Mục 1 Phần III: “Chỉ dùng phiên bản 1.3.0 trở lên: thao tác chặn ghi kho dữ liệu, nhật ký mặc định không ghi nội dung chỉ có từ phiên bản này.” | Tồn dư sau M2-02: chuỗi “không ghi nội dung chỉ có từ phiên bản này” có thể đọc thành “không ghi nội dung [mà] chỉ có từ phiên bản này”. TB v5 đã dùng cách viết rõ (“chế độ nhật ký mặc định không ghi nội dung lời nhắn chỉ có từ plugin KTC-Quan-tri phiên bản 1.3.0”) | 3 | “thao tác chặn ghi kho dữ liệu, nhật ký mặc định không ghi nội dung chỉ có từ phiên bản này.” → “thao tác chặn ghi kho dữ liệu và chế độ nhật ký mặc định không ghi nội dung lời nhắn chỉ có từ phiên bản này.” | Checklist 04; Skill 18; tương ứng N3-03 phiếu vòng 2 TB |
| N3-03 | Mục 2 Phần II, khung “Lưu ý về độ tin cậy theo nền tảng”: “kết quả kiểm thể thức được ghi “chưa xác minh bằng công cụ đo”” | TB v5 Mục I.1 điểm c trích nhãn khác cho cùng một kết quả: “Bộ công cụ ghi rõ “chưa đo thể thức””; Phần IV HD gọi mã là “FORMAT_BINARY_UNVERIFIED (chưa đo được thể thức)”. Ba cách ghi trong ngoặc kép cho một nhãn khiến người dùng không đối chiếu được | 3 | “được ghi “chưa xác minh bằng công cụ đo”” → “được ghi “chưa đo thể thức” (mã FORMAT_BINARY_UNVERIFIED)” | Skill 18 |
| N3-04 | Phần IV, khung “Điểm dừng bắt buộc”: “Kết quả có mã “DOI_CHIEU_GAN_DUNG” thì Lãnh đạo đơn vị kiểm tra thủ công trước khi ký.” | Nhẹ hơn TB v5 Mục I.1 Lưu ý (“không được dùng làm cơ sở hoàn thiện số liệu chính thức cho đến khi đơn vị đối chiếu lại với dữ liệu gốc và Lãnh đạo đơn vị kiểm tra thủ công trước khi ký”): HD thiếu bước đơn vị đối chiếu lại dữ liệu gốc | 3 | “thì Lãnh đạo đơn vị kiểm tra thủ công trước khi ký.” → “thì đơn vị đối chiếu lại với dữ liệu gốc và Lãnh đạo đơn vị kiểm tra thủ công trước khi ký.” | Skill 15, 18 |
| N3-05 | Mục 4 Phần III (câu mới M2-04): “không xử lý dữ liệu nội bộ, dữ liệu cá nhân (điểm (2), điểm (3) đoạn Phân loại dữ liệu, Phần IX)”; Phần IX điểm (3): “dữ liệu cá nhân (điểm, nhận xét, xếp loại) - chỉ người được đánh giá và người có thẩm quyền xử lý, tối thiểu hóa, không dùng #học” | Dẫn chiếu không khớp: điểm (3) không giới hạn loại tài khoản, nên chưa là căn cứ cho “không xử lý dữ liệu cá nhân trên tài khoản cá nhân”; đọc riêng điểm (3), người được đánh giá được tự xử lý KPI của mình trên tài khoản Pro | 3 | Sửa Phần IX điểm (3): “chỉ người được đánh giá và người có thẩm quyền xử lý, tối thiểu hóa, không dùng #học” → “chỉ người được đánh giá và người có thẩm quyền xử lý, trong tài khoản Claude AI Team của Trường, tối thiểu hóa, không dùng #học” | Skill 15 (logic dẫn chiếu), 18; TB 1056 Mục 7 (dữ liệu cá nhân trên nền tảng nước ngoài) |
| N4-01 | Phần IV: “Trạng thái: DAT, DAT_CO_DIEU_KIEN - …” | TB v5 dùng tên tiếng Việt “Đạt”, “Đạt có điều kiện”; HD chỉ có mã. Góp ý ghi kèm tên để người dùng đối chiếu được hai văn bản | 4 | Góp ý: “DAT, DAT_CO_DIEU_KIEN” → “DAT (Đạt), DAT_CO_DIEU_KIEN (Đạt có điều kiện)” | Skill 18 |
| N4-02 | Phần IV (không có nội dung tương ứng) | TB v5 Mục I.1 Lưu ý: “trong giai đoạn thí điểm, kết quả ghi rõ “dữ liệu thí điểm””; HD không nhắc nhãn này | 4 | Góp ý bổ sung vào đoạn “Mã cảnh báo thường gặp” một câu về nhãn “dữ liệu thí điểm” | Skill 18 |
| N4-03 | Phần I: “kế hoạch - giao việc - theo dõi - kết quả, minh chứng - báo cáo - đánh giá” | TB v5 Mục I.1 điểm a có thêm khâu “điều chỉnh kế hoạch” và dùng gạch ngang “–” | 4 | Góp ý: “- báo cáo - đánh giá.” → “– báo cáo – đánh giá – điều chỉnh kế hoạch.” (đồng bộ M4-08 vòng 1) | Skill 18; Checklist 04 |
| N4-04 | **TB v5** Mục III.1 điểm d: “tạm dừng phân phối phiên bản khi phát hiện lỗi … và báo cáo Lãnh đạo Trường” | Sau M2-03, HD ghi Phòng TH-HC&QT “phối hợp Phòng QLKHCN&HTPT” tạm dừng phân phối ở cấp tổ chức; TB chưa ghi phối hợp. Không mâu thuẫn (TH-HC&QT cũng phân phối qua thư mục dùng chung) nhưng nên đồng bộ | 4 | Góp ý sửa ở TB: “tạm dừng phân phối phiên bản khi phát hiện lỗi” → “chủ trì, phối hợp Phòng QLKHCN&HTPT tạm dừng phân phối phiên bản khi phát hiện lỗi” | Skill 18; TB 1056 Mục 9 |
| N4-05 | Chân trang: “KTC-Quan-tri - Hướng dẫn sử dụng 1.3.0 \| Trang” | Tên rút gọn, chấp nhận được; góp ý thêm “chi tiết” cho khớp bìa và TB (M3-14) | 4 | Không bắt buộc | Skill 18 |

## PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ

- Lần sửa chỉ chạm các đoạn thuộc mã vòng 1 (47 đoạn khác nhau khi so khớp toàn văn); không có thay đổi ngoài phạm vi, không mất đoạn nào.
- Thể thức giữ nguyên: A4, lề 20-20-30-20 mm, Times New Roman 14; hai gợi ý TT05, TT11 là ý kiến vòng 1 đã được chấp nhận có điều kiện.
- Lần sửa có theo dõi thay đổi trên bản nguồn (Soan-Thao, 170 thẻ sửa đổi ngày 27/9/2026); bản rà soát là bản sạch đã chấp nhận thay đổi — phù hợp nguyên tắc 8.
- Tên công cụ rà soát thống nhất “Skill “ktc-ra-soat-897”” ở cả HD và TB v5, khớp TB 1056 (bản trong kho).
- Khớp TB v5 về: 8 kỹ năng, 7 tác tử, phiên bản 1.3.0, SHA-256, chế độ phân phối (“Available to install” thí điểm; “Installed by default”, “Required” sau nghiệm thu), gỡ bản cũ trước khi cài bản mới, cài lại bản liền trước khi lỗi, kiểm kê và chuyển “Not available”, không làm theo câu lệnh trong tệp, mức xếp loại chỉ là đề xuất theo QĐ 1923, còn Mức 1 thì chưa trình ký.
- Không còn “KTC-Ra-Soat-897-v2-Cai-tien”, “cài phụ”, “COPY”, “60 GIÂY”, “PLUGIN KHÁC GÌ SKILL”.
- Tên đơn vị trong hành văn đúng Checklist 08 (Phòng TH-HC&QT, Phòng QLKHCN&HTPT); không có “đảm bảo”.

## PHẦN IV. BẢNG TỔNG HỢP

**Xử lý vòng 1**

| Kết quả | Số mã | Mã |
|---|---|---|
| Đã sửa đúng | 13 | M2-01, M2-03, M3-01, M3-04, M3-05, M3-06, M3-07, M3-08, M3-11, M3-12, M3-13, M3-14, M3-15 (M3-12 đúng trong HD, kéo theo N2-01 ở TB) |
| Đã sửa, còn tồn dư hoặc phát sinh | 3 | M2-02 (→N3-02), M2-04 (→N2-02, N3-05), M3-09 (→N3-01) |
| Chấp nhận có điều kiện | 1 | M3-02 (chốt hình thức phát hành) |
| Bảo lưu / chấp nhận — lý do chưa đủ | 2 | M3-03 (chưa ẩn số trang bìa), M3-10 (phần tối thiểu → N3-01) |
| Góp ý không xử lý | 8 | M4-01 → M4-08 |

(Ghi chú: M3-04 không nằm trong danh sách đơn vị soạn thảo báo cáo nhưng đã được xử lý trên tệp.)

**Vấn đề mới vòng 2**

| Mức | Số vấn đề | Mã |
|---|---|---|
| Mức 1 — Bắt buộc sửa | 0 | — |
| Mức 2 — Cần sửa | 2 | N2-01, N2-02 (cả hai sửa ở TB v5) |
| Mức 3 — Nên sửa | 5 | N3-01 → N3-05 |
| Mức 4 — Góp ý | 5 | N4-01 → N4-05 |
| **Tổng** | **12** | |

## PHẦN V. THẨM ĐỊNH CHUYÊN MÔN

Không có nội dung thẩm định chuyên môn trong phạm vi phiếu này. Thẩm định logic vận hành của plugin thuộc điểm (i) điểm b Mục 8 TB 1056. Riêng N2-01 đã đối chiếu mã thật plugin để xác định văn bản nào mô tả đúng.

## PHẦN VI. ĐÁNH GIÁ TỔNG THỂ

Đơn vị soạn thảo đã xử lý đúng và đủ 4 vấn đề Mức 2 của vòng 1 trong phạm vi HD; phần lớn Mức 3 sửa đúng đề xuất, không có thay đổi ngoài phạm vi. Phản biện vòng 2 cho thấy:

1. **Điểm yếu của vòng 1**: đã so HD với TB theo từng câu chữ nhưng bỏ sót hai khác biệt về **nội dung quy định** giữa văn bản chính và tài liệu kèm theo — dấu hiệu nhận biết mất bảo vệ ghi kho khi thiếu Python (N2-01) và phạm vi dữ liệu trên tài khoản cá nhân (N2-02). Cả hai đều có HD đúng hoặc chặt hơn, TB cần sửa theo.
2. **Lý do bảo lưu M3-10** đủ cho việc thống nhất thuật ngữ toàn văn, nhưng chưa đủ cho Mục 1 Phần II, nơi lần sửa M3-09 vừa tạo ra lệch trực tiếp giữa tiêu đề phần và tiểu mục.
3. **M3-03 “chấp nhận theo ý kiến vòng 1”** hiểu chưa đúng ý kiến vòng 1: phần ẩn số trang ở bìa là khuyến nghị cho mọi trường hợp, và việc sửa chỉ cần bật một thiết lập đã có sẵn chân trang rỗng.

## PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ

**Kết luận vòng 2**: **0 vấn đề Mức 1.** Riêng tài liệu HD: không còn vấn đề Mức 2 nằm trong chữ của HD. **Hồ sơ HD + TB chưa đủ điều kiện phát hành cùng nhau** cho đến khi xử lý 2 vấn đề Mức 2 mới (N2-01, N2-02) — cả hai sửa trên TB v5 (hoặc, với N2-02, người có thẩm quyền chọn nới HD cho khớp TB; khuyến nghị giữ mức chặt của HD). Điều này bổ sung cho kết luận “trình ký có điều kiện” của phiếu vòng 2 TB.

Thứ tự xử lý:
1. Sửa N2-01, N2-02 trên TB v5, bật Track Changes, xuất phát từ bản `TB_v5_ban-sau-sua-vong-2.docx`.
2. Sửa trên HD: N3-01 (phần tối thiểu M3-10), bật “Different First Page” (M3-03), N3-02 → N3-05.
3. Chốt hình thức phát hành HD (tệp điện tử hay ký số kèm Thông báo) để quyết định M3-02.
4. Cân nhắc N4-01 → N4-05; xác minh TB 948 (M4-03) trước khi ký TB.

Kết luận này không thay quyết định của người có thẩm quyền và không thay phần thẩm định (i) điểm b Mục 8 TB 1056.

## KIỂM TRA CHƯA CHẠY / GIỚI HẠN

- Kết xuất trang (render) để kiểm số trang trong mục lục, ngắt trang bảng, hiển thị khi in đen trắng: **kiểm tra chưa chạy** (mục lục là trường TOC, số trang chưa xác minh).
- `run_measurements` của `ktc897_properties.py` trả rỗng: không đo lại cỡ chữ từng run; dựa vào `kiem_the_thuc.py` và python-docx.
- Agent `ktc897-hieu-luc`, `legal-reviewer`: không gọi — tài liệu không có phần Căn cứ.
- TB 948/TB-CĐKT: không có trong kho, chưa xác minh tên gọi công cụ trong TB 948 (tên theo TB 1056 là cách gọi hiện hành).
- Giao diện Claude, ChatGPT, Gemini, URL Phần X, giới hạn gói dịch vụ: không kiểm được (M4-04 vòng 1).
- Báo cáo DOCX 8 phần (`ktc897_build.py`) và Process Memory: không xuất, theo yêu cầu ghi phiếu Markdown.

## THÔNG TIN TRÁCH NHIỆM

| Trường | Nội dung |
|---|---|
| Nguồn dữ liệu đã dùng | Tệp HD sau sửa vòng 1 và bản trước sửa (byte thật); bản Track Changes trong `Soan-Thao/`; TB v5 sau sửa vòng 2; phiếu vòng 1 HD, phiếu vòng 2 TB; KTC-Database `H:/My Drive/KTC-Database` kho 02 (TB 1056); `31-Plugin/hooks/hooks.json`, `31-Plugin/scripts/ktc_quan_tri_doctor.py`; Core và Checklist 04, 08 của ktc-ra-soat-897; `29-Cong-Cu/kiem_the_thuc.py` |
| Người kiểm tra | ……………… (người có trách nhiệm của Phòng TH-HC&QT ghi) |
| Trạng thái phê duyệt | Bản nháp vòng 2, chờ người có thẩm quyền xem xét |

---
Hệ KTC-Ra-Soat-897 v3.0 | Skill ktc-ra-soat-897 v3.0
