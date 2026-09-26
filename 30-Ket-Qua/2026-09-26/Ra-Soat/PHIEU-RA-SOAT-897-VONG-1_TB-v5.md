# PHIẾU RÀ SOÁT KTC-897 — VÒNG 1

**Văn bản**: Dự thảo Thông báo hướng dẫn sử dụng bộ công cụ trí tuệ nhân tạo (plugin) trong xây dựng kế hoạch, báo cáo định kỳ và quản trị nhiệm vụ (KTC-Quan-tri)
**Tệp**: `30-Ket-Qua/2026-09-26/Ra-Soat/TB_v5_ban-sau-sua_de-ra-soat.docx` (49.827 byte, chữ ký ZIP `504b0304` hợp lệ, không có Track Changes)
**Công cụ**: Skill `ktc-ra-soat-897:review` (Core v3.0 + baseline v2.24), rà soát chính thức vòng 1
**Mục đích**: Vòng 1/2 theo điểm (ii) điểm b Mục 8 Thông báo số 1056/TB-CĐKT ngày 16/9/2026
**Ngày rà soát**: 27/9/2026 · Tệp gốc **không bị sửa**

---

## PHẦN I. THÔNG TIN CHUNG

| Mục | Nội dung |
|---|---|
| Loại văn bản | Thông báo (ký hiệu `/TB-CĐKT`), số, ngày để trống (đúng quy trình dự thảo) |
| Hệ quy chiếu | **Hệ A**: văn bản hành chính (NĐ 30/2020/NĐ-CP, TB 597/TB-CĐKT, Checklist 08). Căn cứ chọn: cơ quan ban hành Trường Cao đẳng Kon Tum, Quốc hiệu và Tiêu ngữ, người ký Hiệu trưởng, không phải văn bản Đảng, đoàn thể hay VBQPPL |
| Thẩm quyền ký | Hiệu trưởng (Lê Trí Khải), ký trực tiếp, đúng với QĐ 1976 và TB 1056 (Hiệu trưởng quyết định ban hành Skill) |
| Nguồn kho 01–04 đã đọc (nội dung thật) | QĐ 1976/QĐ-CĐKT ngày 14/9/2026 (02-01, bản HIỆN HÀNH + metadata); TT 49/2026/TT-BGDĐT ngày 30/06/2026, hiệu lực 15/8/2026 (01-05-01); TB 1056/TB-CĐKT ngày 16/9/2026 (02); metadata TB 736 (25/6/2026), TB 817 (14/7/2026), QĐ 1923 (30/8/2026); TB 736 bản 04-Good-Documents; danh mục mẫu 03-Templates(1) |
| Nguồn ngoài kho 01–04 | KH 848/KH-CĐKT ngày 03/9/2026: **chỉ có tại `11-Input/KẾ HOẠCH QUÝ III/`** (chưa phân loại vào 02), đã đọc nội dung |
| Nguồn KHÔNG tìm thấy | TB 917/TB-CĐKT (10/8/2026), TB 924/TB-CĐKT (11/8/2026), TB 948/TB-CĐKT (17/8/2026): không có trong kho 01–05, 11-Input. Văn bản nội bộ, không có trên Internet → **cần người dùng cung cấp** |
| Đo thể thức (byte thật) | `ktc897_properties.py`: 1 section, A4 210×297 mm, lề trên/dưới/trái/phải 20/20/30/20 mm; `kiem_the_thuc.py`: 0 gợi ý; python-docx: nội dung TNR cỡ 14, căn đều, thụt 1,27 cm, cách đoạn 6 pt; header số trang từ trang 2 (titlePg) |
| Giới hạn | Kết luận về 3 căn cứ/viện dẫn TB 917, 924, 948 là **CHƯA XÁC MINH** (Mức 4) |

## PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT

| Mã | Vị trí (trích nguyên văn) | Mô tả vấn đề | Mức | Đề xuất (nguyên văn) | Căn cứ quy tắc |
|---|---|---|---|---|---|
| M2-01 | Mục I.1, gạch đầu dòng thứ tư của “* Lưu ý”: “chỉ kết quả ở trạng thái “Đạt” hoặc “Đạt có điều kiện” được dùng làm sản phẩm chính thức” | Mâu thuẫn nội dung với Lưu ý cuối Mục II: “Kết quả do AI tạo ra chỉ có giá trị tham khảo”. Một chỗ cho kết quả AI làm “sản phẩm chính thức”, chỗ kia chỉ “giá trị tham khảo”; trái cả điểm c, điểm a Mục 8 TB 1056 (không lấy bản AI làm bản chính thức khi chưa được người chủ trì rà soát, xác nhận) | 2 | “chỉ kết quả ở trạng thái “Đạt” hoặc “Đạt có điều kiện” được dùng làm sản phẩm chính thức” → “chỉ kết quả ở trạng thái “Đạt” hoặc “Đạt có điều kiện” được dùng làm cơ sở để đơn vị, người soạn thảo kiểm tra, hoàn thiện sản phẩm chính thức” | Core `severity_policy` (Mức 2: logic ảnh hưởng); Skill 15 (logic), 18 (thống nhất); TB 1056 điểm c Mục 1, điểm a Mục 8 |
| M2-02 | Mục I.1 điểm b, gạch thứ ba: “ghi nhật ký vận hành chỉ gồm thông tin mô tả, không ghi nội dung lời nhắn, tự xóa sau 30 ngày” | Mô tả tuyệt đối, không khớp cơ chế thật: plugin 1.3.0 (`31-Plugin/CHANGELOG.md`, mục 1.3.0) **có ghi nội dung** khi người dùng gõ `#học` hoặc chủ máy đặt `KTC_NHAT_KY_NOI_DUNG=1`. Nội dung về bảo vệ dữ liệu trong văn bản chính thức phải chính xác | 2 | “ghi nhật ký vận hành chỉ gồm thông tin mô tả, không ghi nội dung lời nhắn, tự xóa sau 30 ngày” → “ghi nhật ký vận hành, theo mặc định chỉ gồm thông tin mô tả, không ghi nội dung lời nhắn (trừ khi người dùng chủ động chọn ghi), tự xóa sau 30 ngày” | Core `mandatory_rules` 8 (không tin nhãn, kiểm thực tế); Checklist 02 (nội dung chính xác) |
| M2-03 | Mục I.3, Lưu ý: “chặn ghi, xóa kho dữ liệu và nhật ký không ghi nội dung chỉ có từ” | Hệ quả của M2-02, cần sửa đồng bộ | 2 | “chặn ghi, xóa kho dữ liệu và nhật ký không ghi nội dung chỉ có từ” → “chặn ghi, xóa kho dữ liệu và nhật ký mặc định không ghi nội dung chỉ có từ” | Skill 18 (tính thống nhất) |
| M2-04 | Trích yếu: “(KTC-Quan-tri)” | Run này định dạng **nghiêng** (đo python-docx: italic=True); phần còn lại đứng. Trích yếu có tên loại phải in thường, **đứng**, đậm, cỡ 14 | 2 | “(KTC-Quan-tri)” [nghiêng, đậm] → “(KTC-Quan-tri)” [đứng, đậm] (chỉ đổi định dạng, không đổi chữ) | Checklist 08 mục 4 (Trích yếu: đứng, đậm, cỡ 14); NĐ 30 Phụ lục I |
| M3-01 | Mục I.1 “* Lưu ý”, gạch thứ hai và Mục II.4: “bằng công cụ KTC-Ra-Soat-897-v2-Cai-tien theo Thông báo số 948/TB-CĐKT” | Tên công cụ dùng tên thư mục kỹ thuật có hậu tố phiên bản; không thống nhất với TB 1056 (điểm a Mục 2, điểm b Mục 8 gọi là Skill “ktc-ra-soat-897”). Cần xác minh cách gọi trong TB 948 | 3 | “bằng công cụ KTC-Ra-Soat-897-v2-Cai-tien theo Thông báo số 948/TB-CĐKT” → “bằng Skill “ktc-ra-soat-897” theo Thông báo số 948/TB-CĐKT” (thay ở cả 2 đoạn, sau khi đối chiếu TB 948) | Skill 18; Checklist 04 |
| M3-02 | Mục I.1 “* Lưu ý”, gạch thứ tư: “thì không dùng làm số liệu chính thức, Lãnh đạo đơn vị kiểm tra thủ công trước khi ký” | Nối hai mệnh đề độc lập bằng dấu phẩy | 3 | “thì không dùng làm số liệu chính thức, Lãnh đạo đơn vị kiểm tra thủ công trước khi ký” → “thì không dùng làm số liệu chính thức; Lãnh đạo đơn vị kiểm tra thủ công trước khi ký” | Checklist 04 (ngôn ngữ) |
| M3-03 | Mục I.1 điểm b, gạch thứ nhất: “đối với việc KPI cá nhân” | Cụm từ thiếu động từ, tối nghĩa | 3 | “đối với việc KPI cá nhân” → “đối với việc lập, tự đánh giá KPI cá nhân” | Checklist 04 |
| M3-04 | Mục I.3: “d) Cài phụ trên nền tảng khác (ChatGPT, Gemini)” | “Cài phụ” không phải thuật ngữ hành chính, khó hiểu | 3 | “d) Cài phụ trên nền tảng khác (ChatGPT, Gemini)” → “d) Sử dụng trên nền tảng khác (ChatGPT, Gemini)” | Checklist 04 |
| M3-05 | Mục I.1 “* Lưu ý:” so với Mục I.2, I.3, II “Lưu ý:” | Cùng một loại chú ý, trình bày hai kiểu (có/không dấu *) | 3 | “* Lưu ý:” → “Lưu ý:” | Skill 14 (kỹ thuật trình bày), Skill 18 |
| M3-06 | Nơi nhận: “- Đoàn TN – Hội SV Trường;” | Viết tắt không theo mẫu Nơi nhận của TB 597 (“- Đoàn Trường;” / “- Hội Sinh viên Trường;”) và không khớp TB 1056 cùng loại | 3 | “- Đoàn TN – Hội SV Trường;” → “- Đoàn Trường, Hội Sinh viên Trường;” (hoặc tách 2 dòng “- Đoàn Trường;” và “- Hội Sinh viên Trường;”) | Checklist 08 mục 3.4 (mẫu Nơi nhận TB 597) |
| M3-07 | Phần căn cứ | TB 1056/TB-CĐKT là văn bản điều chỉnh trực tiếp việc ban hành Skill/plugin (Mục 8) và được dự thảo viện dẫn ở Mục III.2, nhưng không có trong phần căn cứ; đề nghị bổ sung (nhóm căn cứ nội dung, sau KH 848) | 3 | Thêm đoạn căn cứ: “Căn cứ Thông báo số 1056/TB-CĐKT ngày 16 tháng 9 năm 2026 của Trường Cao đẳng Kon Tum hướng dẫn sử dụng Skill “tao-skill-va-prompt-chuan” để xây dựng các Skill chuyên dụng phục vụ công việc tại các đơn vị thuộc Trường;” (khi thêm, Mục III.2 chỉ ghi “Thông báo số 1056/TB-CĐKT”) | NĐ 30 (thứ tự căn cứ); Checklist 08 mục 5.4 (viện dẫn lần đầu ghi đầy đủ) |
| M4-01 | Căn cứ: “Căn cứ Thông báo số 917/TB-CĐKT ngày 10 tháng 8 năm 2026 …” | TB 917 không có trong kho; chỉ khớp cách ghi tại KH 848. **Cần xác minh** số, ngày, trích yếu | 4 | Người dùng cung cấp bản TB 917 để đối chiếu | Core `uncertainty_handling`; Cổng nguồn v2.24 |
| M4-02 | Mục I.2: “Thông báo số 924/TB-CĐKT ngày 11 tháng 8 năm 2026” | Không có trong kho. Cần xác minh | 4 | Cung cấp TB 924 | Như trên |
| M4-03 | Mục I.1 và II.4: “Thông báo số 948/TB-CĐKT ngày 17 tháng 8 năm 2026” | Không có trong kho. Cần xác minh số, ngày và tên công cụ rà soát (liên quan M3-01) | 4 | Cung cấp TB 948 | Như trên |
| M4-04 | Căn cứ: “Căn cứ Kế hoạch số 848/KH-CĐKT ngày 03 tháng 9 năm 2026 …” | Số, ngày, trích yếu **khớp** bản tại `11-Input`; nhưng bản này chưa được nạp vào kho 02 chính thức. Mục I.1 điểm a “nội dung 1 và nội dung 2” tương ứng dòng TT 1, 2 của bảng KH 848 (KTC-Ke-hoach, KTC-Bao-cao): đúng | 4 | Đề nghị P-THHC nạp KH 848 vào `02-KTC-Regulations` | Cổng nguồn v2.24 |
| M4-05 | Mục I.3 điểm a: “Organization settings > Plugins & skills > Marketplaces > Add > Upload a plugin”; Mục I.2: “Tài khoản miễn phí không sử dụng được plugin.” | Đường dẫn giao diện và điều kiện gói dịch vụ của nhà cung cấp không kiểm được bằng nguồn trong kho; giao diện có thể đổi | 4 | Xác minh trên giao diện thật trước khi ký; cân nhắc chuyển chi tiết giao diện sang Tài liệu hướng dẫn chi tiết | Core `uncertainty_handling` |
| M4-06 | Mục I.3 điểm d (nền tảng ChatGPT, Gemini) | Nạp kỹ năng lên nền tảng của nhà cung cấp khác là đưa tài liệu nội bộ ra ngoài; nên dẫn chiếu yêu cầu bảo mật tại Lưu ý Mục II | 4 | Góp ý bổ sung “, tuân thủ yêu cầu bảo mật dữ liệu tại Mục II Thông báo này” | TB 1056 Mục 7 (tham khảo) |
| M4-07 | Mục I.3, Lưu ý: đoạn dài 6 câu | Góp ý tách thành các gạch đầu dòng để dễ đọc | 4 | Không bắt buộc | Skill 19 (chất lượng) |

## PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ

- Phần đầu: `UBND TỈNH QUẢNG NGÃI` / `TRƯỜNG CAO ĐẲNG KON TUM` (mẫu 2.1 TB 597); Quốc hiệu cỡ 13 đậm, Tiêu ngữ cỡ 14 đậm; `Số:           /TB-CĐKT` cỡ 13; địa danh “Quảng Ngãi, ngày … năm 2026” nghiêng cỡ 14.
- Tên loại “THÔNG BÁO” in hoa, đậm, cỡ 14, căn giữa.
- Khổ A4, lề 20-20-30-20 mm; nội dung TNR 14, căn đều, thụt 1,27 cm, cách đoạn 6 pt; số trang từ trang 2.
- Căn cứ in nghiêng; QĐ 1976/QĐ-CĐKT ngày 14/9/2026 là quy chế tổ chức hiện hành (thay QĐ 988), trích yếu khớp bản gốc; TT 49/2026/TT-BGDĐT ngày 30/6/2026 trích yếu khớp bản gốc, còn hiệu lực (từ 15/8/2026); ghi ngày “30 tháng 6” (không có số 0) đúng NĐ 30. Căn cứ cuối kết thúc bằng dấu chấm, thống nhất với TB 1056.
- Viện dẫn TB 736 (25/6/2026), TB 817 (14/7/2026), QĐ 1923 (30/8/2026), TB 1056 (16/9/2026): số, ngày khớp kho. Lần sau chỉ ghi số, ký hiệu: đúng Checklist 08 mục 5.4.
- Tên đơn vị trong hành văn: Phòng TH-HC&QT, Phòng QLKHCN&HTPT, Phòng TCCB&CTHSSV đúng cột phải bảng 3.4 Checklist 08; dòng “Lưu: VT, THHCQT.” đúng cột giữa.
- Không có “đảm bảo”, “Nhà trường” viết hoa sai vị trí, “UỶ/HOÀ”.
- Mô tả plugin đối chiếu byte thật `31-Plugin/`: phiên bản 1.3.0 (plugin.json), 8 kỹ năng, 7 tác tử, “guard: CHƯA HOẠT ĐỘNG”, xóa nhật ký sau 30 ngày: **khớp** (trừ M2-02).
- Phân công QLKHCN&HTPT quản trị Hệ thống Claude AI Team, nạp ở cấp tổ chức: khớp Mục 4, Mục 9 TB 1056.
- Nơi nhận cỡ 11, “Nơi nhận:” nghiêng đậm; chức vụ “HIỆU TRƯỞNG”, họ tên đậm cỡ 14, không học hàm học vị.
- Không có Track Changes tồn đọng trong tệp.

## PHẦN IV. BẢNG TỔNG HỢP

| Mức | Số vấn đề | Mã |
|---|---|---|
| Mức 1 — Bắt buộc sửa | 0 | — |
| Mức 2 — Cần sửa | 4 | M2-01, M2-02, M2-03, M2-04 |
| Mức 3 — Nên sửa | 7 | M3-01 → M3-07 |
| Mức 4 — Góp ý / Cần xác minh | 7 | M4-01 → M4-07 |
| **Tổng** | **18** | |

## PHẦN V. THẨM ĐỊNH CHUYÊN MÔN

Không có nội dung cần thẩm định chuyên môn ngoài phạm vi thể thức, văn phong, tính thống nhất. Thẩm định nội dung chuyên môn của plugin thuộc điểm (i) điểm b Mục 8 TB 1056 (2 vòng AI độc lập khác nhà cung cấp), không thuộc phiếu này.

## PHẦN VI. ĐÁNH GIÁ TỔNG THỂ

Dự thảo đạt thể thức Hệ A, căn cứ chính (QĐ 1976, TT 49) đúng và còn hiệu lực, tên đơn vị chuẩn. Vấn đề chính là **một mâu thuẫn nội dung** về giá trị của kết quả AI (M2-01), **một mô tả chưa chính xác** về nhật ký (M2-02, M2-03) và **một lỗi kiểu chữ trích yếu** (M2-04). Ba văn bản nội bộ được viện dẫn (TB 917, 924, 948) chưa có trong kho nên chưa xác minh được.

## PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ

**Kết luận vòng 1**: **KHÔNG có vấn đề Mức 1** — không có yếu tố chặn trình ký. **Chưa đủ điều kiện trình ký** cho đến khi xử lý 4 vấn đề Mức 2 và xác minh M4-01 → M4-03 (kết luận chính thức có điều kiện do thiếu 3 nguồn nội bộ).

Thứ tự xử lý:
1. Sửa M2-01 → M2-04 (bật Track Changes theo nguyên tắc 8, sửa trên chính tệp v5).
2. Cung cấp TB 917, 924, 948 để đối chiếu (M4-01 → M4-03); chốt tên công cụ rà soát (M3-01).
3. Xử lý các Mức 3; cân nhắc Mức 4.
4. Chạy **vòng 2** với vai trò phản biện độc lập, không mặc định kết quả vòng 1 là đúng (điểm b Mục 8 TB 1056).

## KIỂM TRA CHƯA CHẠY / GIỚI HẠN

- Agent `ktc897-hieu-luc` và `legal-reviewer`: **không gọi** (tối ưu thời gian); thay bằng đối chiếu trực tiếp QĐ 1976, TT 49 trong kho 01–02.
- Báo cáo DOCX 8 phần (`ktc897_build.py`) và Process Memory: **không xuất**, theo yêu cầu ghi phiếu Markdown.
- Tra Internet cho TB 917, 924, 948: không áp dụng (văn bản nội bộ).
- Đường dẫn giao diện Claude và điều kiện gói dịch vụ (M4-05): không kiểm được.
- Kiểm hiển thị (render trang) của sơ đồ “ĐỐI TƯỢNG SỬ DỤNG / CHU TRÌNH QUẢN TRỊ NHIỆM VỤ”: chưa thực hiện.

## THÔNG TIN TRÁCH NHIỆM

| Trường | Nội dung |
|---|---|
| Nguồn dữ liệu đã dùng | Tệp dự thảo (byte thật); KTC-Database `H:/My Drive/KTC-Database` kho 01, 02, 03-Templates(1), 04 và 11-Input (liệt kê tại Phần I); `31-Plugin/` (plugin.json, CHANGELOG, README, scripts); Checklist 08 và Core ktc-ra-soat-897 |
| Người kiểm tra | ……………… (người có trách nhiệm của Phòng TH-HC&QT ghi) |
| Trạng thái phê duyệt | Bản nháp vòng 1, chờ người có thẩm quyền xem xét |

---
Hệ KTC-Ra-Soat-897 v3.0 | Skill ktc-ra-soat-897 v3.0
