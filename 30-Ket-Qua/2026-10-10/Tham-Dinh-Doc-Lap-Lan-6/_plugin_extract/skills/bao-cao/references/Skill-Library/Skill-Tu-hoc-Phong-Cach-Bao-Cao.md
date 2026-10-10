# Skill-Tu-hoc-Phong-Cach-Bao-Cao
## Skill tự học suốt đời về hành văn, lập luận và tổng hợp báo cáo cho KTC-RIS
### Nguồn học mở: KTC-Database/04-Good-Documents/04-06- Bao cao và các báo cáo tốt được xác nhận trong tương lai
### Cập nhật: 18/08/2026

## 0. NGUYÊN TẮC TIÊN QUYẾT — Xác định cấp báo cáo TRƯỚC KHI soạn bất kỳ câu nào
### [MỚI 18/08/2026 — bắt buộc, không có ngoại lệ]

**Trước khi viết, phải xác định rõ: đây là báo cáo ở CẤP NÀO?**

| Cấp báo cáo | Ai gửi cho ai | Chủ thể ngữ pháp bắt buộc |
|---|---|---|
| Cấp đơn vị | Phòng/Khoa/Trung tâm báo cáo nội bộ lên Trường | Tên đơn vị đó (VD: "Phòng QLĐT&BĐCL đã tổ chức...") |
| **Cấp Trường** | Trường báo cáo lên cấp trên (UBND tỉnh, Sở, Bộ...) | **"Nhà trường" / "Trường"** — KHÔNG BAO GIỜ dùng tên đơn vị trực thuộc làm chủ ngữ |
| Cấp khác | Liên ngành, liên Trường... | Xác định theo văn bản cụ thể, không suy diễn |

### Vì sao đây là lỗi nghiêm trọng, không phải lỗi văn phong nhỏ
Khi tổng hợp báo cáo cấp Trường, các đơn vị (Phòng/Khoa) là **đối tượng thực hiện công việc**, không phải **chủ thể của văn bản báo cáo**. Trường là pháp nhân báo cáo, chịu trách nhiệm trước cấp trên — nên toàn bộ hành văn phải đứng ở góc nhìn của Trường, dù công việc cụ thể do đơn vị nào triển khai.

### Ví dụ SAI (nhầm cấp — lỗi đã xảy ra thực tế, cần tránh lặp lại)
> "Phòng QLĐT&BĐCL tổ chức thi học kỳ II năm học 2025-2026 bằng hình thức thi trắc nghiệm online..."

Đây là câu văn phong **cấp đơn vị**, không được dùng khi tổng hợp báo cáo cấp Trường — dù đúng sự thật là Phòng đó trực tiếp làm việc này.

### Ví dụ ĐÚNG (đúng cấp Trường)
> "Nhà trường tổ chức thi học kỳ II năm học 2025-2026 bằng hình thức thi trắc nghiệm online..."

Nếu cần nêu rõ đơn vị thực hiện (không bắt buộc, chỉ khi có giá trị thông tin), đưa đơn vị vào **thành phần phụ**, không làm chủ ngữ chính:
> "Nhà trường chỉ đạo Phòng QLĐT&BĐCL tổ chức thi học kỳ II năm học 2025-2026..."
> "Thực hiện chỉ đạo của Nhà trường, Phòng QLĐT&BĐCL đã tổ chức..."

### Quy tắc kiểm tra bắt buộc — áp dụng cho MỌI Skill tạo nội dung báo cáo (Skill 33, `fill_bc736.py` content_map, mọi văn bản tổng hợp cấp Trường khác)

1. Trước khi xuất bất kỳ đoạn văn nào vào báo cáo cấp Trường, đọc lại và xác định **chủ ngữ ngữ pháp của từng câu**.
2. Nếu chủ ngữ là tên riêng 1 Phòng/Khoa/Trung tâm cụ thể → **SAI**, phải viết lại với chủ ngữ "Nhà trường".
3. Tên đơn vị chỉ được xuất hiện ở vị trí bổ ngữ/thành phần phụ, hoặc trong bảng phân công/phụ lục liệt kê theo đơn vị (nơi bản chất văn bản là bảng phân công, không phải câu tường thuật báo cáo).
4. Không có ngoại lệ cho quy tắc này khi đang soạn báo cáo/kế hoạch cấp Trường gửi cấp trên.
5. **Trước khi bắt đầu bất kỳ tác vụ tổng hợp báo cáo nào (Skill 33, fill_bc736.py, hoặc tương tự), Claude phải tự hỏi và xác nhận rõ: "Đây là báo cáo cấp nào?" rồi mới chọn văn phong/chủ thể tương ứng — không suy diễn ngầm.**

---

## 1. Mục tiêu
Chuẩn hóa cách KTC-RIS viết báo cáo theo phong cách báo cáo của UBND tỉnh Quảng Ngãi: hành văn hành chính cấp cao, logic, khoa học, có khả năng tổng hợp lớn, ưu tiên số liệu, so sánh, đánh giá theo mục tiêu/kế hoạch, chỉ rõ nguyên nhân và chuyển hóa thành nhiệm vụ điều hành.

## 2. Ba nguồn chuẩn đã học
1. Báo cáo kết quả thực hiện Kế hoạch phát triển kinh tế - xã hội, quốc phòng, an ninh năm 2025.
2. Báo cáo tình hình thực hiện Kế hoạch phát triển kinh tế - xã hội, quốc phòng, an ninh năm 2026 và dự kiến kế hoạch năm 2027.
3. Báo cáo kiểm điểm công tác chỉ đạo, điều hành 06 tháng đầu năm 2026 và nhiệm vụ trọng tâm 06 tháng cuối năm 2026.

## 3. DNA cấu trúc bắt buộc

### 3.1. Mở đầu
- Nêu căn cứ trực tiếp.
- Xác định bối cảnh kỳ báo cáo.
- Chỉ ra đồng thời thời cơ, thuận lợi, khó khăn, thách thức.
- Nêu tinh thần chỉ đạo/điều hành và các quyết sách đã triển khai.
- Kết thúc đoạn mở đầu bằng nhận định tổng quát có kiểm chứng về kết quả chung.

### 3.2. Khối chỉ tiêu
- Ưu tiên chỉ tiêu định lượng trước diễn giải dài.
- Luôn so với ít nhất một chuẩn: kế hoạch, kỳ trước, cùng kỳ, báo cáo trước, chỉ tiêu cấp trên giao.
- Phân loại rõ: vượt / đạt / chưa đạt.
- Nếu số liệu thay đổi so với báo cáo trước phải nêu rõ số cũ, số mới và nguyên nhân nếu có.
- Không dùng tính từ tích cực/tiêu cực nếu không có dữ liệu hoặc minh chứng.

### 3.3. Khối kết quả theo lĩnh vực
Mỗi lĩnh vực nên đi theo chuỗi:
**Kết quả chính → số liệu → so sánh → mức độ hoàn thành → hành động quản lý/điều hành đã thực hiện → vấn đề còn lại.**

### 3.4. Khối tồn tại, hạn chế
- Không liệt kê chung chung.
- Mỗi hạn chế phải gắn với biểu hiện thực tế, chỉ tiêu, tiến độ hoặc sản phẩm đầu ra.
- Tránh lặp lại nguyên văn phần kết quả.
- Ưu tiên nhóm hóa theo nguyên nhân hệ thống thay vì vụ việc rời rạc.

### 3.5. Khối nguyên nhân
Tách nếu đủ dữ liệu:
- Nguyên nhân khách quan.
- Nguyên nhân chủ quan.
- Nguyên nhân về tổ chức thực hiện, phối hợp, tiến độ, nguồn lực, năng lực hoặc dữ liệu.

### 3.6. Khối nhiệm vụ, giải pháp
Mỗi nhiệm vụ nên có tối thiểu 3 yếu tố:
**việc phải làm + đối tượng/lĩnh vực tác động + kết quả hoặc trạng thái cần đạt.**
Khi có thể bổ sung:
**đơn vị chủ trì/phối hợp + thời hạn + chỉ tiêu/minh chứng.**

### 3.6.1. [MỚI 19/08/2026 — xác nhận từ Báo cáo kiểm điểm 6 tháng UBND tỉnh] Cấu trúc lồng 2 tầng cho khối nhiệm vụ lớn
Khi có nhiều nhóm nhiệm vụ trọng tâm (VD 6-7 nhóm cho 1 kỳ báo cáo dài), dùng cấu trúc:
- **Tầng 1**: đánh số nhóm lớn (1, 2, 3...), mỗi nhóm là 1 lĩnh vực/mục tiêu chiến lược.
- **Tầng 2**: trong mỗi nhóm lớn, đánh số hành động cụ thể bằng ngoặc đơn (1), (2), (3)...
Cấu trúc này giúp người đọc vừa nắm được bức tranh lớn (tầng 1) vừa thấy được hành động cụ thể (tầng 2),
phù hợp khi nhiệm vụ phong phú, tránh liệt kê phẳng gây rối mắt. Áp dụng cho báo cáo kỳ dài (quý, 6 tháng,
năm) — báo cáo tháng nên giữ đơn giản (không lồng tầng) vì khối lượng nhiệm vụ nhỏ hơn.

## 4. Công thức hành văn cấp cao

### 4.1. Câu đánh giá tổng hợp
Dùng cấu trúc:
- "Nhìn chung, ... tiếp tục ...; một số ... đạt/vượt ...; tuy nhiên, ... vẫn còn ..."
- Không tô hồng; luôn cân bằng kết quả và vấn đề.

### 4.2. Câu có số liệu
Ưu tiên:
**Chỉ tiêu + kết quả thực hiện + mức tăng/giảm + chuẩn so sánh + mức đạt kế hoạch.**

Ví dụ cấu trúc:
"X đạt A, tăng B% so với cùng kỳ, bằng C% kế hoạch."

### 4.3. Câu điều hành
Dùng động từ mạnh:
**tập trung, chỉ đạo, rà soát, đôn đốc, tháo gỡ, hoàn thiện, triển khai, kiểm tra, giám sát, xử lý, đẩy nhanh, bảo đảm.**

### 4.4. Câu chuyển logic
Ưu tiên các từ nối:
**theo đó, bên cạnh đó, đồng thời, tuy nhiên, qua tổng hợp, trên cơ sở đó, để bảo đảm, nhằm, trong đó, đặc biệt, nhất là.**

**[MỚI 18/08/2026 — xác nhận từ đối chiếu file thật]** Kỹ thuật "Tóm lại": kết thúc khối Đánh giá chung bằng 1 đoạn ngắn bắt đầu "Tóm lại, ..." — tổng kết lại tinh thần chung (ghi nhận kết quả + nhận thức rõ hạn chế + cam kết khắc phục) trước khi chuyển sang phần Nhiệm vụ trọng tâm. Đây là cầu nối giúp người đọc không bị "rơi" đột ngột từ đánh giá sang kế hoạch.

## 5. Nguyên tắc suy luận
1. Không suy luận vượt dữ liệu nguồn.
2. Mọi kết luận xu hướng phải dựa trên chuỗi số liệu hoặc nhiều minh chứng.
3. Khi một chỉ tiêu tăng/giảm bất thường, phải kiểm tra: thay đổi phạm vi tính; thay đổi mẫu số; thay đổi phương pháp thống kê; yếu tố thời điểm; thay đổi chính sách hoặc tổ chức bộ máy.
4. Phân biệt "kết quả hoạt động" và "kết quả điều hành".
5. Không đồng nhất "đã ban hành văn bản" với "đã hoàn thành nhiệm vụ".
6. Khi tổng hợp nhiều đơn vị, ưu tiên kết quả cấp Trường và loại bỏ mô tả trùng lặp cấp đơn vị.
7. Một nhận định chỉ được nâng lên cấp Trường khi có đủ độ bao phủ hoặc có giá trị trọng yếu.
8. **[MỚI] Xem Mục 0 — chủ thể ngữ pháp phải đúng cấp báo cáo, kiểm tra trước khi xuất mọi đoạn văn.**

## 6. Nguyên tắc nén thông tin
- Gom các hoạt động cùng mục tiêu thành một cụm kết quả.
- Không liệt kê hội họp, văn bản, hoạt động thường xuyên nếu không tạo ra kết quả quản trị hoặc sản phẩm cụ thể.
- Một đoạn nên trả lời được ít nhất một trong các câu hỏi: (1) Đã đạt gì? (2) So với mục tiêu ra sao? (3) Vì sao? (4) Còn vướng gì? (5) Tiếp theo làm gì?

## 7. Chuẩn logic cho KTC-RIS
Khi tổng hợp báo cáo cấp Trường, ưu tiên pipeline:
**Bối cảnh → Chỉ tiêu → Kết quả theo 6 Trục → Đánh giá tổng hợp → Hạn chế → Nguyên nhân → Nhiệm vụ kỳ tới.**

Trong từng Trục:
**Mục tiêu/nội hàm → kết quả nổi bật → số liệu/minh chứng → mức hoàn thành → tồn tại → việc tiếp theo.**

Toàn bộ pipeline này viết với chủ thể "Nhà trường" — xem Mục 0.

## 8. Quy tắc dùng số liệu
- Kiểm tra tổng thành phần trước khi dùng tổng số.
- Kiểm tra tỷ lệ phần trăm bằng phép tính nếu có mẫu số.
- Ghi rõ "ước", "thực hiện", "lũy kế", "đến ngày..." nếu nguồn có phân biệt.
- Không trộn số liệu chính thức với số ước mà không ghi chú.
- Khi số liệu mới khác số liệu báo cáo trước, phải ưu tiên số mới nhưng lưu dấu thay đổi nếu có ý nghĩa phân tích.

## 8.1. [MỚI 19/08/2026] Câu tổng hợp cân bằng trước khi chuyển sang phần tiếp theo
Trước khi kết thúc 1 khối đánh giá lớn (VD hết phần "Đánh giá chung"), nên có 1 câu/đoạn tổng hợp
ngắn theo mẫu: "Tóm lại, [chủ thể] tiếp tục phát huy kết quả đạt được, đồng thời nhận thức [rõ/sâu sắc]
các tồn tại, hạn chế nêu trên — đặc biệt là nguyên nhân chủ quan — sẽ tiếp tục có biện pháp khắc phục,
đổi mới nhằm [mục tiêu hướng tới]." Kỹ thuật này tạo điểm neo tâm lý cân bằng: vừa ghi nhận nỗ lực,
vừa không né tránh hạn chế, vừa hướng đến hành động — tránh kết thúc đột ngột hoặc chỉ dừng ở liệt kê.

## 9. Những lỗi phải tránh
- Kể việc thay vì báo cáo kết quả.
- Dùng quá nhiều tính từ "tích cực, hiệu quả, quyết liệt" mà thiếu số liệu/minh chứng.
- Danh sách dài nhưng không có tầng ưu tiên.
- Nhiệm vụ kỳ tới lặp lại y nguyên hạn chế.
- Tồn tại không gắn nguyên nhân.
- Số liệu không có chuẩn so sánh.
- Nhận định cấp Trường chỉ dựa trên một đơn vị.
- Trùng nội dung giữa các Trục.
- Nhầm văn bản chỉ đạo với sản phẩm hoàn thành.
- **[MỚI] Dùng tên đơn vị (Phòng/Khoa) làm chủ ngữ chính trong báo cáo cấp Trường — xem Mục 0.**

## 10. Cách áp dụng trong KTC-Bao-Cao
Skill 33 khi tổng hợp cấp Trường phải đọc file này trước khi viết bản thảo cuối — **đặc biệt Mục 0**.
Skill 34 khi đối chiếu tiến độ phải dùng chuẩn "kết quả – kế hoạch – chênh lệch – nguyên nhân – hành động".
Bước 6 trước khi xuất DOCX phải kiểm tra thêm:
- **Chủ thể ngữ pháp đúng cấp báo cáo (Mục 0) — kiểm tra từng câu.**
- logic mục lớn/mục nhỏ;
- mỗi nhận định quan trọng có dữ liệu/minh chứng;
- nhiệm vụ kỳ sau có tính hành động;
- không để báo cáo biến thành danh sách hoạt động.

## 11. Mức ưu tiên nguồn
Khi phong cách giữa các nguồn khác nhau:
1. Báo cáo chính thức của UBND tỉnh/HĐND tỉnh.
2. Báo cáo tổng hợp cấp Trường đã được phê duyệt.
3. Báo cáo chuyên đề mẫu tốt.
4. Báo cáo đơn vị.

## 12. Nguyên tắc bảo toàn nội dung nguồn
Học phong cách không đồng nghĩa sao chép nội dung.
KTC-RIS phải:
- giữ nguyên sự thật, số liệu và thuật ngữ của nguồn Trường;
- chỉ học cách tổ chức, lập luận, nén thông tin và diễn đạt;
- không đưa bối cảnh cấp tỉnh vào báo cáo Trường nếu nguồn Trường không hỗ trợ.

---
Tài liệu này là chuẩn điều khiển phong cách cho KTC-RIS và phải được sử dụng cùng 30-Skill-Phan-Loai-6-Truc và 33-Skill-Tong-Hop-Bao-Cao-Truong.

## 13. Cơ chế "tự học suốt đời"
- Phạm vi học không giới hạn ở báo cáo UBND tỉnh. KTC-RIS được phép học từ báo cáo chính thức, chất lượng tốt của Trường, UBND tỉnh và các nguồn mẫu tốt khác trong `04-Good-Documents/04-06- Bao cao`.
- Không hấp thụ máy móc toàn bộ một văn bản. Mỗi nguồn phải được phân tích để nhận diện điểm mạnh riêng: cấu trúc, logic, nén thông tin, số liệu, câu chuyển, lập luận, đánh giá, kiến nghị, cách phục vụ đối tượng nhận báo cáo.
- Quy tắc mới chỉ được bổ sung khi làm tăng chất lượng; không được làm suy giảm hoặc xung đột với quy tắc tốt đã xác lập. Khi xung đột, ưu tiên nguồn chính thức hơn, mới hơn và phù hợp loại báo cáo hơn.
- Mỗi lần học phải giữ provenance: tên báo cáo/nhóm nguồn, kỹ thuật rút ra, phạm vi áp dụng và ngày cập nhật.
- Học phong cách, không sao chép nội dung; không biến dữ liệu của nguồn mẫu thành dữ liệu của Trường.

## 14. Bổ sung từ các báo cáo chính thức của Trường Cao đẳng Kon Tum

### 14.1. Báo cáo tổng kết năm học
Học kỹ thuật thiết lập bối cảnh trước đánh giá: liên kết chỉ đạo của Trung ương, tỉnh, Sở với điều kiện thực tế của Trường; sau đó tổ chức kết quả theo các lĩnh vực quản trị/chuyên môn.

### 14.2. Báo cáo tháng và kế hoạch tháng sau
Học kỹ thuật tổng hợp từ cấp đơn vị lên cấp Trường theo trục/nội hàm quản trị; loại bỏ sự trùng lặp giữa các đơn vị; **chuyển chủ thể từ đơn vị sang Nhà trường (xem Mục 0)**; ưu tiên kết quả đầu ra và trạng thái hoàn thành hơn mô tả quá trình.

### 14.3. Báo cáo đánh giá hiệu quả hoạt động
Học kỹ thuật chứng minh bằng chuỗi lịch sử → hiện trạng → số lượng/tỷ lệ → kết quả đầu ra → nhận định.

### 14.4. Báo cáo tóm tắt phục vụ lãnh đạo cấp trên
Học kỹ thuật nén thông tin: tổng quan ngắn nhưng đủ vị trí pháp lý, tổ chức, nguồn lực; sau đó chọn kết quả nổi bật, vấn đề then chốt.

### 14.5. Bản sắc báo cáo của Trường cần bảo tồn
- Luôn làm rõ vị trí, chức năng và đặc thù cơ sở GDNN khi bối cảnh yêu cầu.
- Ưu tiên số liệu tuyển sinh, quy mô đào tạo, tốt nghiệp, đội ngũ, chương trình, bảo đảm chất lượng, doanh nghiệp/việc làm, khoa học-công nghệ/chuyển đổi số và nguồn lực khi có liên quan.
- Kết nối kết quả chuyên môn với mục tiêu phát triển Trường.
- Khi báo cáo cho cấp trên, phải phân biệt rõ nội dung Trường tự giải quyết và nội dung cần kiến nghị/tháo gỡ.

## 15. Nhật ký tri thức nguồn hiện tại

### [CẬP NHẬT 18/08/2026] Nguồn tại KTC-Database/04-Good-Documents/04-06-Bao-cao/04-06-04-Bao-cao-tham-khao-chuan
Đã đối chiếu trực tiếp (đọc toàn văn, không chỉ khớp tên file) 1/3 file — xác nhận nội dung khớp đúng với các nguyên tắc Mục 3-4 đã đúc kết:
- **`BC-kiem-diem-chi-dao-dieu-hanh-6-thang-dau-nam-2026.docx`** (Số 188/BC-UBND, 18/6/2026) — Báo cáo kiểm điểm công tác chỉ đạo, điều hành 6 tháng đầu năm 2026. Đã đọc toàn văn 18/08/2026 — xác nhận đúng cấu trúc: bối cảnh → số liệu có so sánh → 3 lĩnh vực (kinh tế/văn hóa-xã hội/nội chính-QP-AN-đối ngoại) → Đánh giá chung (Ưu điểm/Khó khăn hạn chế/Nguyên nhân khách quan-chủ quan) → "Tóm lại..." → Nhiệm vụ trọng tâm (đánh số, mỗi việc có động từ mạnh + đối tượng + kết quả cần đạt).
- **`1. UBND bao cao BTC du thao KH KTXH 2027 (lan 1).docx`** — tương ứng nguồn #2 (Mục 2) — chưa đọc lại toàn văn lần này, chỉ xác nhận qua tên file khớp với nguồn đã ghi trước đó.
- **`1. BC UBND_BC HDND cap nhat KTXH 2025 (so lieu den 31.12.2025).docx`** — tương ứng nguồn #1 (Mục 2) — chưa đọc lại toàn văn lần này, chỉ xác nhận qua tên file khớp với nguồn đã ghi trước đó.

### Nguồn khác đã học trước đây
- Trường Cao đẳng Kon Tum — báo cáo tổng kết năm học 2025-2026: học bối cảnh năm học và tổng hợp đa lĩnh vực.
- Trường Cao đẳng Kon Tum — báo cáo công tác tháng 7/kế hoạch tháng 8: học tổng hợp theo trục/nội hàm và chuyển tiếp kế hoạch.
- Trường Cao đẳng Kon Tum — báo cáo đánh giá hiệu quả hoạt động: học chứng minh hiệu quả bằng chuỗi số liệu lịch sử và hiện trạng.
- Trường Cao đẳng Kon Tum — báo cáo tóm tắt tình hình hoạt động: học kỹ thuật nén thông tin phục vụ lãnh đạo cấp trên.
- **[18/08/2026] Phản hồi trực tiếp của Anh Phục: phát hiện lỗi dùng tên đơn vị làm chủ thể trong báo cáo cấp Trường (bản chạy thử tháng 7-8/2026) — đã sửa và bổ sung Mục 0 làm nguyên tắc tiên quyết.**

### Việc còn lại
Chưa đọc toàn văn 2/3 file còn lại trong `04-06-04-Bao-cao-tham-khao-chuan` để xác nhận 100% (chỉ khớp qua tên file). Nếu Anh Phục muốn chắc chắn tuyệt đối, có thể yêu cầu đọc nốt 2 file này ở phiên sau.

## 16. Quy tắc kích hoạt tự học
Khi người dùng chỉ định một báo cáo là "hay", "chuẩn", "tham khảo tốt", hoặc khi báo cáo được đặt trong `KTC-Database/04-Good-Documents/04-06- Bao cao`, KTC-RIS phải xem xét nó như ứng viên học. Chỉ cập nhật Skill này sau khi phân tích và xác nhận có kỹ thuật mới hoặc biến thể hữu ích.
