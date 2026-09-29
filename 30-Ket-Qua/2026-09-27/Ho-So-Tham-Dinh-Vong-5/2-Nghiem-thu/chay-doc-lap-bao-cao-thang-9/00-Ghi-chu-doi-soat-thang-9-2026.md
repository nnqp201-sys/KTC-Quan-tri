# Ghi chú đối soát — Báo cáo tháng 9 và Kế hoạch tháng 10 năm 2026 (cấp Trường)

**Lập:** 28/9/2026 · **Người lập:** P-THHC (bản nháp do KTC-Quan-tri / bao-cao v3.18 dựng) · **Trạng thái:** `DAT_CO_DIEU_KIEN`, chưa đủ điều kiện trình ký (xem mục 9)
**Căn cứ mẫu:** Thông báo số 736/TB-CĐKT (Phụ lục Ib, IIa, IIb) · **Đầu vào:** `10-Dau-Vao/2026-09/` (29 tệp)

## 1. Sản phẩm và bản gốc phát triển

| Tệp | Nội dung | Phát triển từ (bản đã ban hành, chỉ đọc) |
|---|---|---|
| `BC_Ket-qua-cong-tac-thang-9-ke-hoach-thang-10-2026_DU-THAO_20260928.docx` | I. Kết quả tháng 9 · II. Đánh giá chung · III. Nhiệm vụ trọng tâm tháng 10 | BC 375/BC-CĐKT ngày 20/8/2026 |
| `PL_KPI-Ket-qua-cong-tac-thang-9-2026_DU-THAO_20260928.xlsx` | 53 nhiệm vụ của KH 834 (47 ở mục I, 6 ở mục II); công thức KPI (8)–(16) | PL-KPI kèm BC 375 |
| `KH_Ke-hoach-cong-tac-thang-10-2026_DU-THAO_20260928.xlsx` | 30 nhiệm vụ mới và 9 nhiệm vụ chuyển tiếp | KH 834/KH-CĐKT ngày 28/8/2026 |
| `00-Ghi-chu-doi-soat-thang-9-2026.md` | Tệp này | — |

Nguồn bổ trợ đã đọc: TB 1019, 1047, 1071, 1092/TB-CĐKT (kết luận giao ban tuần 07/9–04/10/2026); BC 407/BC-CĐKT ngày 17/9/2026 (Quý III, định hướng Quý IV); QĐ 311/QĐ-CĐKT ngày 04/02/2026 và Phụ lục Chương trình công tác trọng tâm năm 2026; CV 5884/VP-KTTH.

Các cột "Ghi chú đối soát" (cột Q của phụ lục, cột L của kế hoạch) nằm ngoài vùng in và **phải xóa trước khi ban hành**.

## 2. Tình hình nộp hồ sơ (13 đầu mối, theo `12-Bang-Ma-Don-Vi.md`)

| Đầu mối | IIa (docx) | IIb (xlsx) | Ib (xlsx) | Nhận xét |
|---|---|---|---|---|
| P-QLĐT&BĐCL | ✗ | ✗ | ✗ | **CHƯA NỘP**. Là đầu mối tuyển sinh, đào tạo, khảo thí, BĐCL; chủ trì 13/53 nhiệm vụ của KH 834 |
| Công đoàn cơ sở | ✗ | ✗ | ✗ | **CHƯA NỘP**; chủ trì KH 834 dòng 3.3, 4.6, 4.8 |
| Đoàn TN – Hội SV | ✗ | ✗ | ✗ | **CHƯA NỘP**; chủ trì KH 834 dòng 1.6, 4.3, 4.4, 5.1 |
| P-THHC (Phòng TH-HC&QT) | chỉ có Ban TT | Ban TT + `P.THHCQT.xlsx` | chỉ có Ban TT | **Thiếu IIa và Ib của Phòng**. IIb của Phòng (8 dòng) bỏ trống toàn bộ cột KPI. Lặp lại vấn đề kỳ tháng 8 |
| K-KTNL | ✓ | ✗ | ✗ | **Thiếu IIb, Ib** |
| P-TCCB | ✓ (thiếu nhiều mục) | ✓ | ✓ | Xem mục 3 |
| P-QLKH, P-TCKT, K-KHCB, K-KTCN, K-SUPH, K-YDUOC, K-DTSHLX | ✓ | ✓ | ✓ | Xem lỗi ở mục 3 |
| Bộ phận Văn phòng Đảng ủy (ngoài danh sách 13) | — | — | — | Chủ trì 5 nhiệm vụ KH 834 (4.2, 4.12, 4.13, II.4, II.5), không có kênh báo cáo |

## 3. Lỗi dữ liệu của đơn vị (không tự sửa tệp gốc; đề nghị đơn vị điều chỉnh)

**Lỗi công thức KPI.** Kiểm bằng `read_bc736_excel.py`. Các dòng sai chỉ bị loại số KPI của dòng đó, đơn vị vẫn được tổng hợp.

| Đơn vị | Dòng | Lỗi | Giá trị đúng |
|---|---|---|---|
| Ban TT (P-THHC) | 1.1 "Tham mưu văn bản… truyền thông" | Cột (16) = 1,1 | = Hệ số × (15) = 0,75 |
| P-QLKH | hàng 34 "Tham dự Hội nghị tập thể nhân sự chủ chốt…" | Cột (14) = 1,0 | = 0,3. Điểm chấm 30 cũng không thuộc thang 100/120/150/200 (các hàng 32–34) |
| P-TCKT | 1.5 "Xây dựng kế hoạch và tổ chức thẩm mức…" | Hệ số = 2,0 (đúng 1,0); SL quy đổi = 2,0 (theo hệ số ghi thì = 4,0) | — |
| P-TCKT | 1.5 (trùng STT) "TB thu học phí K8C…" | SL quy đổi = 3,0 | = 1,0 |
| P-TCKT | 1.7 "Trích lập quỹ học bổng…" | Hệ số = 4,0 (đúng 1,0); (10), (12) sai; ô (13) trống | — |
| P-TCKT | 2.2 "Ban hành định mức…" | Hệ số = 1,0 | = 1,2 (điểm 120) |

Không dòng nào ở trên thuộc 9 dòng được dùng KPI trong phụ lục.

**Lỗi cấu trúc, nội dung và kỳ báo cáo:**
- **K-KTCN, IIa:** không theo khung TB 736 (tự đặt mục 1–6 theo lĩnh vực), nên công cụ không trích được theo Trục. Nội dung đã đọc tay và đưa vào báo cáo. IIb có 2 dòng STT "2,.2" và dòng trùng nội dung (3.2 = 2.2; 2 dòng "Bếp ăn" ở hàng 27, 30). Lỗi IIb sai cấu trúc kỳ tháng 8 **đã khắc phục** kỳ này.
- **P-TCCB:** IIa để trống các mục 1.4, 1.6, 2, II, III. Còn nguyên dòng mẫu "2.1. Chỉ thị …..", "(Chi tiết … tháng/quý … năm 20…)". IIb có 8 dòng "…" (Khó và phức tạp, SL trống). Ib có 10 dòng "…" gắn "Đưa vào KH Trường" nhưng không có nội dung. Tiêu đề IIb ghi "ĐƠN VỊ:…......."; tiêu đề Ib dính chữ "CTHSSVKẾ HOẠCH". Ô Ib dòng 1.2 dính nội dung dòng 1.1.
- **K-KHCB, IIa:** mục kết quả Trục 2 ghi "Trong tháng 8, Khoa hoàn thiện…", có thể chép từ kỳ trước. Mục kế hoạch Trục 4 ghi "nội dung trọng tâm tháng 9/2026" trong kế hoạch tháng 10. Nhãn lĩnh vực lệch nội dung (nhãn "Công tác tuyển sinh" gắn với nội dung đào tạo). Ib không dùng giá trị chuẩn "Đưa vào KH Trường"/"Thường xuyên của đơn vị" ở cột (11).
- **P-TCKT:** IIa ghi "thanh toán chế độ chính sách cho HSSV tháng 7/2026", IIb ghi "tháng 8/2026", nên báo cáo không nêu tháng. IIa mục kế hoạch Trục 5 lặp nội dung đã làm tháng 8 ("truy lĩnh phụ cấp tháng 1-7/2026; thanh toán lương tháng 8"), nên không đưa vào tháng 10. IIa có lỗi gõ "tháng 9/226". Ib có 3 dòng ghi chú "Kế hoạch của Trường" (không phải giá trị chuẩn).
- **K-YDUOC, Ib tháng 10:** hầu hết thời hạn là ngày tháng 9 (05/09, 20/09, 22/09…), có "19/09/2029" (lỗi năm) và "21/07/2026". IIa dẫn "Thông báo số 1006/TB-CĐKT ngày 03/6/2026", số và ngày không khớp dãy số tháng 9. Tệp ghi "Unisort" (đúng là Unisoft).
- **K-DTSHLX:** ký hiệu văn bản sai: "Quyết định số 1977/TB-CĐKT", "Quyết định số 1929/TBCĐKT", "Biên bản số 186/BC-CĐKT", "Văn bản số 40/PT-CĐKT". Báo cáo Word không dẫn các số này. Ib không có dòng "Đưa vào KH Trường"; 6 dòng cuối thiếu người chỉ đạo, đơn vị chủ trì.
- **P-QLKH:** nhiều sản phẩm IIb mang ngày tháng 8 (19/8–27/8). Chấp nhận vì kỳ báo cáo tính từ sau ngày 20/8 (BC 375). Số hiệu KH 837/KH-CĐKT ngày 12/9/2026 nhỏ hơn KH 848 ngày 03/9, không khớp thứ tự, cần xác minh. Báo cáo Word không dẫn số này. Hai dòng IIb 4 và 5 (hàng 27, 28) trùng nhau (QĐ 1844).
- **Ban TT:** IIb dòng 3.2 và 5.1 tự ghi chỉ tiêu (1; 2) thấp hơn KH 834 giao (3; 5).
- **Phông chữ (hook the-thuc):** `IIb/QLKHCNHTPT.xlsx` (1 ô Calibri), `Ib/KHCB.xlsx` (13 ô), `Ib/SP.xlsx` (4 ô). Đây là tệp gốc của đơn vị nên không sửa.

## 4. Nguồn từng ý — báo cáo Word

Viết tắt: IIa/IIb/Ib + mã đơn vị; kq = mục kết quả, kh = mục kế hoạch.

**I.1 Tuyển sinh:** BC 407 mục I.1 (560 chỉ tiêu, 47,1%, tính đến 05/9/2026); IIa P-QLKH kq (nhập học đợt 2, HS K9T đăng ký GDTX); IIa K-KHCB kq (đợt 1, 2, nền tảng số); IIa K-YDUOC kq; IIb K-DTSHLX 1.19 (TB 1053); IIa Ban TT kq T1. `DOI_CHIEU_GAN_DUNG`: "K9T" được hiểu là "trình độ trung cấp, khóa tuyển sinh năm 2026", suy từ "K9C tuyển sinh năm 2026" trong IIa K-YDUOC.
**I.1 Đào tạo:** IIa K-KHCB, IIa K-KTNL, IIa K-KTCN (đọc tay), IIa/IIb K-YDUOC (10 lớp, 313 SV; 5 SV K6C), IIa/IIb K-SUPH, IIa/IIb K-DTSHLX, IIa P-QLKH kq; TB 1047 và BC 407 (Lễ Khai giảng); BC 407 (QĐ 1865/QĐ-CĐKT ngày 25/8/2026 về CTĐT GDMN).
**I.1 Khảo thí:** IIa K-KTCN mục 5; IIb K-KHCB 1.4; IIa K-KHCB, K-KTNL (NĐ 63); IIb K-DTSHLX 1.12, 2.2.
**I.1 BĐCL:** IIa/IIb K-SUPH 1.1; TB 1019 (TB 963/TB-CĐKT); IIb K-KHCB 1.7; IIa K-KTCN mục 5.
**I.1 Kế hoạch, tổng hợp:** BC 407 (tệp kho); IIa/IIb P-TCKT (BC 406); IIb P-THHCQT 1.1–1.3, 4.1 (**IIb không có số liệu trạng thái**, nên dùng động từ "xây dựng/hoàn thiện", không ghi "hoàn thành"); TB 1019–1092 (Tổ Kiểm tra).
**I.1 Tổ chức, cán bộ:** IIa/IIb P-TCCB; IIb P-QLKH hàng 34 (hội nghị nhân sự); IIa P-QLKH, K-KTCN (tọa đàm KPI); IIb K-KHCB II.5 (tập huấn KPI); IIb K-YDUOC 1.5 (hợp đồng Phòng khám).
**I.2 Thể chế:** IIa/IIb P-TCCB (QC tổ chức và hoạt động, Quy chế làm việc, Tổ kiểm toán); IIb P-TCKT 2.1, 2.2 và BC 407 (Quy chế kiểm toán nội bộ; "Quyết định (8 nghề)"); IIb P-QLKH 2 (KH 866); IIb P-THHCQT 4.2 (bãi bỏ QĐ 1340, **không có trạng thái**, nên ghi "xây dựng").
**I.2 Kiểm tra, giám sát:** IIb K-KHCB 2.1; IIa/IIb K-YDUOC 2.1; IIa K-KTNL, K-KTCN (camera); IIb K-DTSHLX 2.1; TB 1019/1047/1071/1092 (BC 36–39/BC-TKT).
**I.3:** IIb P-QLKH (KH 848, TB 1020, 1044, 1046, 959, KH 797, BB 180, 182, TB 1008, QĐ 1844, CV 609, 626, 658, PC 795); IIa K-KHCB, K-KTNL (Claude AI Team, SCORM/xAPI, bồi dưỡng CĐS); IIb K-KHCB 3.1 (43 chứng nhận NQ 57); IIb P-THHCQT 3.1; IIb P-TCCB (VNPT KPI); IIb K-YDUOC 3.1; IIa K-DTSHLX (phần mềm mô phỏng TT 17). Riêng "QĐ ban hành Phương án ứng cứu sự cố" và "Google Drive" lấy từ IIa P-QLKH, đơn vị ghi "tham mưu/đề xuất", nên báo cáo ghi "xây dựng/đề xuất".
**I.4 Xây dựng Đảng:** IIa K-KHCB, K-KTNL kq T4; IIa/IIb P-QLKH (BC 103-BC/ĐU; QĐ 114; đoàn đồng chí Y Ngọc).
**I.4 Kỷ cương:** IIa K-KHCB, K-KTNL, K-SUPH; TB 1019 (định dạng tệp, AI); TB 1047 (trang phục, hội trường). Câu "chưa ghi nhận vụ việc" được giới hạn trong phạm vi báo cáo của các đơn vị đã nộp.
**I.4 Đảng, CĐ, Đoàn:** BC 407 mục I.4 (chương trình Đoàn, Hội; sinh hoạt chính trị đầu khóa); IIb K-KHCB 5.1 và TB 1071 (Trung thu); IIa Ban TT kq T2, T4; IIa K-KTCN mục 4 (SV 5 tốt).
**I.5 CSVC:** IIb P-THHCQT 2.2; IIb K-KTCN 1.3, 5.1; IIa K-KTCN mục 3; IIb K-DTSHLX 1.13, 1.15; IIb K-KHCB 1.15–1.18.
**I.5 Tài chính:** IIa/IIb P-TCKT (các số TB 972, QĐ 1829–1846, KH vật tư 838–905); IIa/IIb K-YDUOC 1.4 (QĐ 2723/QĐ-SYT).
**I.5 An sinh:** IIa K-KTCN mục 4; IIa P-QLKH kq T1 (Vì Tầm vóc Việt, học bổng khai giảng); IIa K-KHCB, K-KTNL kq T5; IIa K-SUPH kq T5.
**I.5 Truyền thông:** IIa Ban TT kq (72 sản phẩm); IIa K-KHCB, K-KTNL kq T5.
**I.6:** IIa các khoa kq T6; IIb K-DTSHLX 6.1; IIa K-YDUOC; IIb P-QLKH mục 6 (KH 878, CV 625, BC 379); IIa K-KTCN (Daun Penh Argico); IIa/IIb P-QLKH mục 5, 2.
**I.7 Nghị quyết:** 59, 66, 68, 71 lấy từ IIa P-QLKH nq_kq cùng IIa K-KHCB, K-KTNL nq_kq; 70 và 80 lấy từ IIa K-KHCB, K-KTNL; 79 lấy từ IIb P-TCKT 1.8; 72 lấy từ IIa/IIb K-YDUOC 1.4, 1.5 và IIa P-TCCB. `DOI_CHIEU_GAN_DUNG`: xếp các hoạt động của Phòng khám vào NQ 72 là phân loại của người tổng hợp.
**II. Đánh giá chung:** tổng hợp từ mục I. Phần tồn tại lấy từ TB 1019 (trễ hạn TT 55), TB 1019/1047 (sân tập lái xe), IIb P-TCCB (tiến độ 50%), IIb P-QLKH (TB 1020 gia hạn), TB 1092 mục II.6 (cam kết ngoại ngữ), IIa K-KTCN (sinh viên vi phạm). BC 407 ghi "Tồn tại: Không" cho Quý III, khác với nhận định trong báo cáo này, cần Lãnh đạo lưu ý.
**III. Nhiệm vụ tháng 10:** nguồn từng dòng xem cột L của tệp kế hoạch. Phần Word lấy thêm từ IIa các đơn vị (mục kh), TB 1092, BC 407 mục III, CTCT tháng 10. `DOI_CHIEU_GAN_DUNG`: "thực hiện quy trình bổ nhiệm Trưởng khoa KT&NL" (suy từ TB 1092 giao lập kế hoạch trước 30/9) và "cuộc họp nâng cao hiệu quả Phòng khám" (TB 1071/1092).

Không dùng tỷ lệ KPI trong phần Word (theo Skill 37).

## 5. Đối soát phụ lục kết quả

- Danh mục lấy đúng 53 dòng KH 834 (47 ở mục I, 6 ở mục II "đột xuất, phát sinh, từ tháng trước chuyển sang"). Tiêu đề mục II được sửa lại theo KH 834, vì bản tháng 8 mang tiêu đề "chưa hoàn thành, chuyển sang tháng sau".
- **9/53 dòng có KPI** từ IIb hợp lệ: 1.7, 2.1, 2.3, 3.1, 4.1, 4.7, 4.9, 4.11, 5.3. **44 dòng ghi "chưa có kết quả"**: 13 do P-QLĐT&BĐCL chưa nộp; 12 do CĐCS (3), Đoàn – Hội SV (4), BPVPĐU (5); 4 do Phòng TH-HC&QT không có dòng/KPI (5.5, 5.6, 5.7, 5.10); 2 do lệch chỉ tiêu (3.2, 6.2 Ban TT, `CAN_XAC_MINH`); 13 dòng còn lại do đơn vị chủ trì đã nộp nhưng không báo cáo dòng tương ứng hoặc báo gia hạn. Không dòng nào bị kết luận "chưa hoàn thành" chỉ vì thiếu báo cáo. Nguồn và lý do của từng dòng ghi ở cột Q.
- Tổng quy đổi theo Trục (tính kiểm bằng script, công thức trong tệp giữ nguyên): Trục 1 có SL quy đổi kế hoạch 13,6 và KPI tiến độ quy đổi 1,5; Trục 2 là 5,7/2,25; Trục 3 là 12,0/1,5; Trục 4 là 17,0/3,15; Trục 5 là 14,7/1,5; Trục 6 là 13,0/0. **Không nên diễn giải thành % hoàn thành theo Trục**, vì 83% số dòng chưa có kết quả.
- Đã kiểm: mọi công thức hàng dữ liệu chỉ tham chiếu đúng hàng của nó; dải SUM của 6 Trục và mục II khớp khối dòng. **Chưa mở bằng Excel/LibreOffice để tính lại** (máy không có bộ tính). Mở tệp một lần bằng Excel trước khi dùng để có giá trị hiển thị (`FORMAT_BINARY_UNVERIFIED`).

## 6. Kế hoạch tháng 10: nguồn, loại trừ, thiếu

- **Có trong kế hoạch:** 16 dòng Ib có ghi "Đưa vào KH Trường" và do lãnh đạo cấp Trường chỉ đạo (Ban TT 6 dòng; P-QLKH 1.4–1.6; P-TCCB 1.1, 1.2; P-TCKT 1.1, 1.2, 2.1–2.3); 8 dòng chỉ có nguồn là kết luận giao ban TB 1047/1071/1092; 3 dòng từ CTCT tháng 10; 3 dòng do đơn vị đề xuất trong IIa hoặc từ BC 407/KH 834 (hội thảo CĐS, đoàn công tác Nam Lào, hoạt động 20/10); 9 dòng chuyển tiếp có bằng chứng chưa xong (đơn vị còn ghi trong Ib/IIa tháng 10, IIb báo gia hạn hoặc SL 50%, hoặc BC 407 xếp sang Quý IV).
- **Loại, không đưa vào (Skill 33 BƯỚC 0A):** 6 dòng K-KTCN có "Đưa vào KH Trường" nhưng người chỉ đạo là "Lãnh đạo Khoa"; 1 dòng K-YDUOC (1.7, chỉ đạo "Giáo vụ khoa", hạn 20/9); 10 dòng "…" của P-TCCB (không có nội dung); P-QLKH Ib 1.1–1.3 đã đưa vào mục chuyển tiếp.
- **Không đưa vào vì chưa rõ trạng thái** (hạn tháng 9, chưa có báo cáo; cần đơn vị xác nhận đã xong hay chuyển tiếp): KH 834 dòng 1.1 (CTĐT Y sỹ đa khoa), 1.4, 1.5, 1.8, 1.10, 2.4, 3.5, 4.2, 4.5, 4.10, 4.12, 4.13, 5.4–5.10, II.2–II.6; TB 1019 (KH triển khai QĐ 141/2026/QĐ-UBND; KH triển khai CV 5747/BGDĐT); TB 1047 (TT 72/2026; khắc phục thiết bị Hội trường); TB 1071 (QĐ thay thế QĐ 1305, QĐ 1370); TB 1092 (văn bản đăng ký tập huấn Skill lần 2; KH bổ nhiệm Trưởng khoa KT&NL).
- **Ô ghi "[CẦN BỔ SUNG]"** trong tệp kế hoạch: thời hạn (Ib của Ban TT, P-TCKT bỏ trống), người chỉ đạo và sản phẩm của một số dòng giao ban hoặc đơn vị đề xuất. 14 dòng chưa có độ khó (cột G trống, công thức tạm tính 100 điểm). Phần căn cứ còn thiếu số, ngày Kế hoạch công tác Quý IV/2026 (kho chưa có).
- Chưa có nhiệm vụ tháng 10 của: Phòng TH-HC&QT (chưa nộp Ib), P-QLĐT&BĐCL, CĐCS, Đoàn – Hội SV, K-KTNL.

## 7. 14 chỗ "[CẦN BỔ SUNG]" trong báo cáo Word

Kết quả tháng 9 (9 chỗ):
1. Số liệu tuyển sinh, nhập học đến hết 9/2026 (P-QLĐT)
2. Kết quả Lễ tốt nghiệp ngày 26/9/2026 (P-QLĐT)
3. Kế hoạch khảo thí năm học 2026-2027 (P-QLĐT)
4. Tự đánh giá chuẩn cơ sở GDNN theo TT 38 (P-QLĐT)
5. Số, ngày QĐ Quy chế tổ chức và hoạt động, Quy chế làm việc; Quy định vị trí, chức năng các đơn vị (P-TCCB)
6. Sơ kết Quý III của Đảng ủy; "Dân vận khéo" (BPVPĐU)
7. Hoạt động tháng 9 của CĐCS, Đoàn – Hội SV
8. 5 nhiệm vụ CSVC của KH 834 (Phòng TH-HC&QT, K-DTSHLX)
9. Kết quả thực hiện NQ 79 tháng 9 (P-TCKT)

Nhiệm vụ tháng 10 (5 chỗ):
10. Khảo thí tháng 10 (P-QLĐT)
11. Nhiệm vụ Đảng ủy (BPVPĐU)
12. Nhiệm vụ CĐCS, Đoàn – Hội SV
13. CSVC, hành chính – quản trị (Phòng TH-HC&QT)
14. NQ 79 (P-TCKT)

(Thẻ 5 gồm hai ý. Công cụ đếm đúng 14 thẻ.)

Các nội dung này **không tự đặt**; đã nêu gộp ở "Tồn tại, hạn chế" ("một số đơn vị chưa gửi báo cáo"). Phải về 0 trước khi trình ký.

## 8. Mâu thuẫn giữa các nguồn — `CAN_XAC_MINH`, người có thẩm quyền quyết

| # | Nội dung | Các bên | Đề xuất xử lý |
|---|---|---|---|
| 1 | Thời điểm Lễ tốt nghiệp 2026 | TB 1071: 26/9/2026 · CTCT năm: Tháng 10/2026 · BC 407 III: Quý IV · Ib Ban TT, IIa K-KTCN tháng 10 vẫn ghi | P-QLĐT xác nhận. Nếu đã tổ chức ngày 26/9 thì điền kết quả vào I.1 và bỏ "(lễ Tốt nghiệp,…)" ở dòng 1.11 kế hoạch |
| 2 | Chiến lược phát triển Khoa CKHCB | IIb K-KHCB 1.5: hoàn thành (CL 75%) · IIa K-KHCB kh: "hoàn thành trước 30/9" (vẫn là nhiệm vụ) | K-KHCB xác nhận số, ngày ban hành |
| 3 | Hội thảo "Chuyển đổi số toàn diện…" | BC 375 (tháng 8) và BC 407 mục I ghi đã tổ chức · IIa P-QLKH và BC 407 mục III ghi sẽ tổ chức trước 11/10 | P-QLKH làm rõ (có thể là sinh hoạt chuyên đề và hội thảo chính thức) |
| 4 | Hội thảo CTCT tháng 10 (AI, bán dẫn…) và hội thảo CĐS | Có thể là một sự kiện hoặc hai | Lãnh đạo quyết định giữ một hay hai dòng |
| 5 | Phương án sân tập lái xe (KH 834 dòng 5.9) | TB 1019/1047: tồn đọng · TB 1071: 2 việc tồn đọng đã xong (không nêu tên) | K-DTSHLX xác nhận |
| 6 | Tên cơ quan đối tác Lào | "Sở Giáo dục và Thể thao" (KH 878, BC 407) · "Sở Giáo dục đào tạo và Thanh niên" (IIa P-QLKH, BC 375) | P-QLKH xác nhận; báo cáo đang dùng "Sở Giáo dục và Thể thao" |
| 7 | Tồn tại Quý III | BC 407: "Không" · báo cáo tháng 9 nêu các việc trễ hạn theo TB giao ban | Lãnh đạo lưu ý tính nhất quán |

## 9. Tự kiểm và việc còn lại trước khi trình ký

- `bc_thang.py` tự kiểm Word: 0 kỳ cũ ở đầu/cuối, đủ mục con phần I và III, 0 vi phạm văn phong (lần đầu có 1 cảnh báo nhầm với "Phòng Cảnh sát giao thông", đã viết lại). Còn 14 thẻ CẦN BỔ SUNG (mục 7).
- `kiem_the_thuc.py`: cả 3 tệp đạt, 0 gợi ý.
- **Lỗi công cụ đã phát hiện:** BC 375 gốc ghi số hiệu "Số375BC-CĐKT" (thiếu ":" và "/"), nên biểu thức `Số:\s*\d+/` của `bc_thang.py` không bắt được và **số 375 bị giữ lại** trong bản dựng. Đã sửa tay thành "Số:      /BC-CĐKT". Đề nghị vá công cụ (đăng ký lỗi mới).
- Phần căn cứ của báo cáo Word giữ nguyên từ BC 375 (QĐ 38/2026/QĐ-UBND). **Chưa chạy** tác tử `ktc-hieu-luc-vien-dan` để kiểm hiệu lực các văn bản được viện dẫn.
- **Chưa chạy:** rà soát `ktc-ra-soat-897` (bắt buộc trước trình ký); kiểm độc lập `ktc-kiem-san-pham`; tính lại công thức bằng Excel.
- Trước khi ban hành: bổ sung 14 thẻ; xóa cột Q (phụ lục) và cột L (kế hoạch); để trống số, ngày cho Văn thư.
