# 01 – Bảng thông số thể thức cố định của Trường Cao đẳng Kon Tum (v4.5, 27/10/2026)

Bảng này là **thước đo duy nhất** khi kiểm thể thức. **Phạm vi (quyết định của Hiệu trưởng ngày 26/10/2026, điểm 2): bảng A chỉ áp cho văn bản chính quyền; văn bản Đảng theo bảng B (HD 05-HD/VPTW), kể cả dòng chỉ dẫn dưới tiêu đề phụ lục.** Mỗi thông số là **một giá trị cố định** (hoặc một khoảng đóng có hai đầu), không diễn giải lại theo trí nhớ, không dùng khoảng rộng của Nghị định 30 khi Trường đã quy định con số cụ thể.

## Thứ tự ưu tiên căn cứ (văn bản chính quyền)
1. Chỉ đạo của Hiệu trưởng ngày 26/10/2026 (văn bản “Nội dung cập nhật Skill ktc-ra-soat-897”, 26/10/2026) và các quyết định của Hiệu trưởng về Skill ngày 26/10/2026 và 27/10/2026.
2. **Thông báo số 597/TB-CĐKT ngày 19/5/2026** (thể thức, kỹ thuật trình bày văn bản hành chính của Trường).
3. **Quyết định số 1355/QĐ-CĐKT ngày 03/6/2026** (tên, địa chỉ các cơ sở; cách viết tên đơn vị, tổ chức).
4. Quyết định số 389/QĐ-CĐKT ngày 26/02/2026 (Quy chế công tác văn thư, lưu trữ) – **chỉ cho các phần TB 597 dẫn chiếu sang**: dấu, chữ ký số (TB 597 mục 8) và các thành phần khác của văn bản (TB 597 mục 10).
5. **Nghị định số 30/2020/NĐ-CP** và Phụ lục I – chỉ áp dụng cho nội dung mà mục 1–4 không quy định.

Văn bản Đảng: Quy định 208-QĐ/TW (26/7/2026) → Hướng dẫn 05-HD/VPTW (27/5/2026) → Quy định 399-QĐ/TW (09/01/2026); mẫu đầu văn bản của Đảng bộ Trường theo Phụ lục TB 597/TB-CĐKT. KHÔNG áp bảng A cho văn bản Đảng.

Script đo: `tools/kiem_tra_the_thuc.py` (mã quy tắc ở cột “Mã”). Mức xếp loại theo `02-Quy-Tac-Xep-Muc.md`.

## A. Văn bản hành chính (chính quyền)

### A1. Trang, lề, phông
| Mã | Thông số | Giá trị bắt buộc | Twips / đơn vị XML | Căn cứ |
|---|---|---|---|---|
| TT-01 | Khổ giấy | **A4** (210 × 297 mm), không dùng Letter | w:pgSz 11906 × 16838 | Chỉ đạo 26/10/2026; NĐ 30 PL I mục I.1 |
| TT-02 | Lề trên / dưới | **2 cm / 2 cm** | 1134 / 1134 (±20) | Chỉ đạo 26/10/2026 |
| TT-02 | Lề trái / phải | **3 cm / 2 cm** | 1701 / 1134 (±20) | Chỉ đạo 26/10/2026 |
| TT-03 | Header / Footer | **1,27 cm / 1,27 cm** | 720 / 720 (±20) | Chỉ đạo 26/10/2026 |
| TT-04 | Phông chữ | Times New Roman (Unicode TCVN 6909:2001) | w:rFonts | NĐ 30 PL I mục I.2 |

### A2. Phần đầu văn bản
| Mã | Thành phần | Cỡ | Kiểu | Ghi chú | Căn cứ |
|---|---|---|---|---|---|
| TT-12 | UBND TỈNH QUẢNG NGÃI | 13 | in hoa, đứng, **không đậm** | dòng riêng, không ghép chung đoạn với tên trường | TB 597 mục 2.2 |
| TT-13 | TRƯỜNG CAO ĐẲNG KON TUM | 13 | in hoa, đứng, **đậm** | đường kẻ dưới 1/3–1/2 dòng chữ | TB 597 mục 2.2 |
| TT-10 | CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM | 13 | in hoa, đứng, đậm | | TB 597 mục 1.2 |
| TT-11 | Độc lập - Tự do - Hạnh phúc | 14 | in thường, đứng, đậm | gạch nối (-) có cách chữ; đường kẻ bằng Draw, dài bằng dòng chữ | TB 597 mục 1.2 |
| TT-14 | Số, ký hiệu | 13 | đứng | sau “Số:” để trống **tối thiểu 6 ký tự**; số < 10 thêm 0 | TB 597 mục 3.1, 3.2 |
| TT-15 | Địa danh, ngày tháng | 14 | in thường, **nghiêng** | “Quảng Ngãi, ngày ␣␣␣␣␣␣ tháng …” – ngày để trống 6 ký tự; ngày < 10, tháng 1, 2 thêm 0 | TB 597 mục 4 |
| TT-16 | Tên loại văn bản | 14 | in hoa, đứng, đậm | | TB 597 mục 5.2 |
| TT-17 | Trích yếu | 14 | in thường, đứng, đậm | đường kẻ dưới 1/3–1/2 dòng chữ | TB 597 mục 5.2 |
| TT-17 | Trích yếu công văn (V/v) | 13 | in thường, đứng (v4.5 đo, trong hoặc ngoài bảng đầu văn bản) | cách số, ký hiệu 6 pt | TB 597 mục 5.2 |

### A3. Phần nội dung
| Mã | Thông số | Giá trị bắt buộc | XML | Căn cứ |
|---|---|---|---|---|
| TT-20 | Cỡ chữ lời văn | **14** (cùng một cỡ cho toàn bộ lời văn) | w:sz 28 | TB 597 mục 6; Chỉ đạo 26/10/2026 |
| TT-21 | Khoảng cách đoạn | Before **≥ 6 pt** và After **≥ 6 pt** | w:spacing before/after ≥ 120 | Chỉ đạo 26/10/2026; TB 597 mục 6 |
| TT-22 | Giãn dòng | từ **Single** đến **1,5 lines**, chỉ **kiểu theo dòng** (Single, 1,5 lines, Multiple 1,0–1,5); **Exactly, At least → TT-22** | lineRule auto: 240–360; exact/atLeast: lỗi | Chỉ đạo 26/10/2026; TB 597 mục 6 (đính chính ngày 27/10/2026); quyết định E1 |
| TT-23 | Thụt đầu dòng | **1 cm – 1,27 cm** | w:ind firstLine 567–720 | TB 597 mục 6 |
| TT-24 | Canh lề lời văn | dàn đều hai lề (Justify) | w:jc both | TB 597 mục 6 |

Ghi chú A3 (v4.4–v4.5; quyết định D2 của Hiệu trưởng ngày 27/10/2026; phản biện lần 4): script phân vùng theo vai trò rồi đo. Không đo: đầu văn bản, tên loại – trích yếu, vùng tiêu đề đầu mỗi phần (các đoạn canh giữa/phải hoặc in hoa liền nhau ở đầu phần), dòng in hoa toàn bộ, dòng “Số:”, “V/v”, “Kính gửi”, địa danh – ngày, quốc hiệu – tiêu ngữ, vùng “Nơi nhận” (dòng “Nơi nhận:” và các dòng ngắn liền sau – **dừng ở đoạn lời văn dài, đề mục “Điều/Chương/Mục…”, tiêu đề văn bản kèm theo/phụ lục hoặc phần mới**), khối chữ ký (tối đa 5 dòng ngắn sau dòng chức vụ), dòng phụ lục, đề mục canh giữa (“Chương/Mục/Phần …”, tên chương/mục một dòng in đậm hoặc nghiêng toàn bộ). v4.5 (phản biện lần 5): vùng Nơi nhận chỉ gồm dòng danh sách “- …”, dòng chức vụ in hoa, dòng “(…)” và dòng canh giữa/phải ngắn không kết thúc bằng dấu chấm (họ tên) – gặp câu lời văn, kể cả câu ngắn, là dừng; dòng một dòng đậm/nghiêng chỉ được miễn khi là tên đề mục ngay dưới “Chương/Mục/Phần …” hoặc dòng trích yếu ngay dưới tên loại in hoa; bảng chỉ bị coi là bảng Nơi nhận – chữ ký khi có ô bắt đầu bằng “Nơi nhận:” hoặc quốc hiệu. **Đoạn canh giữa/phải trong thân văn bản vẫn đo** (không lấy chính lỗi canh lề, độ đậm hay độ dài làm lý do bỏ đo). TT-20 – TT-23 đo ở mọi đoạn lời văn còn lại, kể cả đề mục “Điều …” và câu ngắn; TT-24 (dàn đều) chỉ xét đoạn **nhiều dòng**: script đếm số dòng thật = ngắt dòng (Shift+Enter) + ngắt dòng tự động theo bề rộng chữ (số đo phông tương thích Times New Roman, tệp tools/do_rong_chu_TNR.json) trên bề rộng vùng chữ (khổ giấy – lề – thụt); đoạn sát ngưỡng một/hai dòng (chữ rộng/hẹp hơn 3 %) ghi “chưa kiểm”. Lời văn trong bảng nội dung (mọi đoạn có chữ thường, kể cả câu ngắn) không đo, ghi số đoạn vào “chưa kiểm”. Mục Đạt ghi số đoạn thực đo “n/n đoạn”. Giãn dòng: TB 597 mục 6 được Hiệu trưởng **đính chính ngày 27/10/2026** – bỏ hẳn cụm “hoặc từ 15 pt (exactly line spacing) trở lên”; chỉ nhận kiểu theo dòng từ Single đến 1,5 lines (quyết định E1) – ghi chú PB2-18 “giữ cận dưới Exactly 15 pt” **hết hiệu lực**.
| TT-18 | Căn cứ ban hành | in thường, **nghiêng**, cỡ 14; mỗi căn cứ một dòng | | TB 597 mục 6 |
| TB-03 | Dấu câu căn cứ | mỗi căn cứ kết thúc “;”, dòng cuối trước “QUYẾT ĐỊNH:” kết thúc “.” | | TB 597 mục 6; NĐ 30 PL I |
| CC-06 | Căn cứ là Luật, Pháp lệnh | chỉ ghi tên loại + tên + ngày; **không ghi số, ký hiệu, cơ quan ban hành** (kể cả khi kèm cụm hợp nhất) | | NĐ 30 PL I Phần II mục 6.a; TB 597 mục 6; quyết định của Hiệu trưởng 26/10/2026 điểm 1 |
| CC-02 | Luật, pháp lệnh đã được sửa đổi, bổ sung và đã có VBHN | viện dẫn theo VBHN mới nhất (xem `04-Vien-Dan-Van-Ban-Hop-Nhat.md`) | | Pháp lệnh 01/2026/UBTVQH16 Điều 4; Chỉ đạo 26/10/2026 |

### A4. Ký, nơi nhận
| Mã | Thành phần | Cỡ | Kiểu | Căn cứ |
|---|---|---|---|---|
| — | Quyền hạn, chức vụ người ký | 14 | in hoa, đứng, đậm | TB 597 mục 7.2 |
| — | Họ tên người ký | 14 | in thường, đứng, đậm | TB 597 mục 7.2 |
| TT-19 | “Nơi nhận:” | **12** | in thường, **nghiêng, đậm**; sau có **dấu hai chấm** (v4.5 kiểm) | TB 597 mục 9 |
| TT-19 | Danh sách nơi nhận | **11** | in thường, **đứng** (chữ nghiêng → TT-19, v4.5); “- …;”, dòng cuối “- Lưu: VT, <đơn vị>.” | TB 597 mục 9 |
| — | “Kính gửi:” và tên nơi gửi | 14 | in thường, đứng | TB 597 mục 9 |

### A5. Số trang
| Mã | Thông số | Giá trị bắt buộc | Căn cứ |
|---|---|---|---|
| TT-31, TT-38 | Vị trí, định dạng | **chính giữa lề trên** (header), chữ số Ả-rập, **cỡ 14** | Chỉ đạo 26/10/2026; NĐ 30 PL I |
| TT-32, TT-33 | Văn bản chính | bắt đầu từ 1; **không hiển thị số ở trang thứ nhất** (Different first page) | NĐ 30 PL I |
| TT-30 | Văn bản kèm theo (Quy định, Quy chế, Điều lệ, Nội quy…) | **ngắt trang và trình bày ở section mới** | Chỉ đạo 26/10/2026 |
| TT-34, TT-35 | Số trang văn bản kèm theo | **đánh liên tục** với văn bản chính (Continue from previous section), **trang đầu của văn bản kèm theo có hiện số** | Chỉ đạo 26/10/2026 (trả lời điểm 1 ngày 26/10/2026) |
| TT-36, TT-37 | Số trang phụ lục | mỗi phụ lục **đánh riêng từ 1**, **hiển thị ở trang đầu**, cỡ 14 | Chỉ đạo 26/10/2026 |
| TT-36 | Phụ lục 1 trang | **không đánh số trang** | Chỉ đạo 26/10/2026 |
| TT-39 | Nhiều phụ lục | mỗi phụ lục một section riêng | Chỉ đạo 26/10/2026 |

### A6. Phụ lục
| Mã | Thông số | Giá trị bắt buộc | Căn cứ |
|---|---|---|---|
| TT-40 | Dòng “Phụ lục …” | cụm từ “Phụ lục” **in thường** (chữ P hoa), số thứ tự **La Mã** (I, II, III…), cỡ 14, đậm, căn giữa | Chỉ đạo 26/10/2026 |
| TT-42 | Tiêu đề phụ lục | **IN HOA**, căn giữa, đậm, cỡ 14 | Chỉ đạo 26/10/2026 |
| TT-43 | Dòng cuối tiêu đề | “**CỦA TRƯỜNG CAO ĐẲNG KON TUM**” – in hoa, đậm, cỡ 14, **một dòng riêng** (chỉ áp dụng cho tiêu đề phụ lục – trả lời điểm 2 ngày 26/10/2026) | Chỉ đạo 26/10/2026 |
| TT-44 | Đường kẻ dưới tiêu đề | đối tượng vẽ (Drawing/Shape), dài **1/3 – 1/2** tiêu đề, căn giữa. Script kiểm **có/không**; độ dài ghi “Chưa kiểm” (người kiểm tra xem bản dựng) | Chỉ đạo 26/10/2026 |
| TT-45 | Dòng “(Kèm theo Quyết định/Thông báo/Tờ trình… số … ngày …)” dưới tiêu đề phụ lục hoặc văn bản kèm theo | **KHÔNG được có** (mọi dự thảo đưa lên AI đều là văn bản ký số) | Chỉ đạo 26/10/2026 (thay quy tắc v3.0 coi dòng này “không phải lỗi”) |
| TD-05 | Viện dẫn phụ lục có số trong lời văn | viết hoa chữ “P”: “Phụ lục I”, “tại Phụ lục II” | Chỉ đạo 26/10/2026 |
| — | Văn bản kèm theo | không có quyền hạn, chức vụ, chữ ký, dấu ở cuối (không phải lỗi) | TB 597 mục 6 |

### A7. Bảng
| Mã | Thông số | Giá trị bắt buộc | XML | Căn cứ |
|---|---|---|---|---|
| TT-50 | Canh bảng | **giữa trang** (Table – Center) | w:tblPr/w:jc = center | Chỉ đạo 26/10/2026 |
| TT-51 | Canh ô | **giữa theo chiều dọc dòng** (Cell – Center) | w:tcPr/w:vAlign = center | Chỉ đạo 26/10/2026 |
| — | Phạm vi | áp dụng cho bảng dữ liệu; không áp dụng cho bảng bố cục không kẻ khung (đầu văn bản, khối chữ ký, nơi nhận) | | |

### A8. Tên đơn vị, cơ sở, từ ngữ
Xem `03-Danh-Muc-Don-Vi-Va-Co-So.md` (mã TD-01, TD-02, TD-03, TD-04).

## B. Văn bản của Đảng (Đảng bộ Trường = đảng bộ trực thuộc cơ sở)
| Thông số | Giá trị | Căn cứ |
|---|---|---|
| Khổ giấy | A4 | HD 05 mục IV |
| Lề | trên 2 cm, dưới 2 cm, trái 3 cm, phải 1,5 cm | HD 05 mục IV |
| Số trang | Ả-rập, canh giữa, cách mép trên 10 mm, không hiện trang 1; phụ lục đánh số riêng | HD 05 mục IV |
| “ĐẢNG CỘNG SẢN VIỆT NAM” | 15, in hoa, đứng, đậm | HD 05 Phụ lục 2 |
| Tên cấp trên / tên cơ quan ban hành | 14 in hoa đứng / 14 in hoa đứng đậm | HD 05 Phụ lục 2 |
| Thể loại / trích yếu | 15–16 đậm / 14–15 đậm | HD 05 Phụ lục 2 |
| Nội dung | 14–15, đứng | HD 05 Phụ lục 2 |
| Lời văn (TT-21 – TT-24) | dàn đều hai lề; thụt đầu dòng khoảng 10 mm; **khoảng cách đoạn (Spacing) tối thiểu 6 pt** – đo bằng khoảng cách thực giữa hai đoạn liền nhau: After đoạn trên + Before đoạn dưới ≥ 6 pt (quyết định D1 ngày 27/10/2026); giãn dòng **Exactly** 18–22 pt (kiểu At least, Single, Multiple là TT-22) | HD 05 Phần II mục 6.2.2 |
| “Nơi nhận:” / danh sách | 14 đứng gạch chân / 12 đứng | HD 05 Phụ lục 2 |
| Phụ lục (TT-40, TT-41, TT-46) | “Phụ lục 1, 2…” (Ả-rập); tiêu đề dưới dòng “Phụ lục”; **dưới tiêu đề phải có chỉ dẫn phụ lục kèm theo văn bản** (số, ký hiệu, ngày, cơ quan ban hành) | HD 05 Phần II mục 1.1, 1.2 |
| Không áp | các quy tắc A4–A7 riêng của Trường ngày 26/10/2026 (văn bản kèm theo đánh số liên tục, dòng “CỦA TRƯỜNG CAO ĐẲNG KON TUM”, bỏ dòng “(Kèm theo…)”, căn bảng, viết hoa “Phụ lục I”) | quyết định của Hiệu trưởng 26/10/2026, điểm 2 |

Đầu văn bản của Trường (mẫu tại Phụ lục TB 597):
- Đảng ủy Trường: “ĐẢNG BỘ UBND TỈNH QUẢNG NGÃI” / “ĐẢNG ỦY TRƯỜNG CAO ĐẲNG KON TUM” / * / “Số …-…/ĐU”.
- Ủy ban Kiểm tra: “ĐẢNG ỦY TRƯỜNG CAO ĐẲNG KON TUM” / “ỦY BAN KIỂM TRA” / * / “Số …-…/UBKT”.
- Bộ phận Văn phòng Đảng ủy: “ĐẢNG ỦY TRƯỜNG CAO ĐẲNG KON TUM” / “BỘ PHẬN VĂN PHÒNG ĐẢNG ỦY” / * / “Số …-…/BPVPĐU”.
- Chi bộ: “ĐẢNG BỘ TRƯỜNG CAO ĐẲNG KON TUM” / “CHI BỘ …” / * / “Số …-…/CB”.
- Địa danh: “Quảng Ngãi, ngày … tháng … năm …”.

Chi tiết cỡ chữ: `references/Skill-Library/29-Phu-Luc-2-Co-Chu-Kieu-Chu-VB-Dang.md`; tên gọi cấp tổ chức: `29-Phu-Luc-3-Tai-Co-Cau-To-Chuc-Dang-2026.md`.

## C. Quy tắc đo
1. Đo bằng script từ XML (`kiem_tra_the_thuc.py`); không ước lượng bằng mắt, không lấy từ báo cáo khác.
2. Số trang thực tế (trang bắt đầu của từng section) lấy từ bản dựng LibreOffice bằng phương pháp chèn mốc; ghi rõ “dựng bằng LibreOffice, có thể lệch khi mở bằng Word”.
3. Kết quả “chưa kiểm” của script (mục C của báo cáo script) **không được** ghi thành lỗi Mức 1–2 và **không được** ghi “Đạt”; ghi vào Phần I.8.
4. Ngưỡng dung sai: lề, header/footer ±20 twips (≈ 0,035 cm); cỡ chữ không dung sai.
