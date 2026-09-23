# Ghi chú rà soát — Kế hoạch công tác Quý IV năm 2026

**Tệp rà soát:** `C:\Users\nnqp2\Downloads\Copy of Ke_hoach_cong_tac_Quy_IV_2026 V1.xlsx` (sheet "KH Quý IV", A1:K83)
**Ngày rà soát:** 22/9/2026 · **Phạm vi:** đối chiếu KTC-Database 01-02 (căn cứ), mẫu Phụ lục Ia/TB736, `kiem_the_thuc.py`
**Không sửa trực tiếp tệp gốc** — chỉ ghi chú theo yêu cầu.

Phân mức theo quy ước KTC-Ra-Soat-897 (1 bắt buộc sửa → 4 góp ý).

---

## Mức 1 — bắt buộc sửa trước khi trình ký

1. **Sai số hiệu văn bản viện dẫn (A8, dòng căn cứ thứ 1).**
   Ghi: *"Quyết định số 1299/QĐ-CĐKT ngày 27/5/2026 ... ban hành Quy chế làm việc của Trường Cao đẳng Kon Tum"*.
   Đối chiếu `KTC-Database/02-KTC-Regulations/02-01-.../08. Quy che lam viec cua Truong.docx`: văn bản này có
   **Số: 1229/QĐ-CĐKT, ngày 27 tháng 5 năm 2026** — đúng ngày nhưng **sai số hiệu** (1299 → phải là **1229**,
   nhiều khả năng gõ nhầm hoán vị hai chữ số 2↔9).
   → **Sửa "1299" thành "1229".**

2. **Hạn hoàn thành nghịch lý ở nhiều dòng thuộc Mục II ("Các nhiệm vụ quý trước chuyển sang").**
   Quý IV/2026 chạy từ 01/10 đến 31/12/2026, nhưng 10/23 dòng ở Mục II vẫn ghi hạn **"Chậm nhất ngày
   30/9/2026"** — là ngày cuối Quý III, tức đã qua trước khi kế hoạch Quý IV có hiệu lực:
   dòng 59, 60, 61, 67, 72, 73, 75, 78, 80, 81 (mục 1, 2, 3, 9, 14, 15, 17, 20, 22, 23).
   Nếu đây là nhiệm vụ **thật sự chuyển sang Quý IV** (chưa xong ở Quý III) thì phải có **hạn mới nằm trong
   Quý IV**; nếu đã hoàn thành đúng hạn 30/9 thì **không thuộc diện "chuyển sang"** và không nên đưa vào
   kế hoạch Quý IV.
   → **Rà lại từng dòng, cập nhật hạn hoàn thành thực tế hoặc loại khỏi danh sách.**

3. **Dòng 56 (Mục I, Trục 6, nhiệm vụ 6.1)** — "Duy trì ổn định chính trị nội bộ..." ghi hạn **"01
   lần/tháng; chậm nhất 30/9/2026"** trong khi toàn bộ Mục I còn lại là nhiệm vụ Quý IV (hạn 10, 11,
   12/2026). Đây là nhiệm vụ định kỳ hằng tháng nên hạn phải đặt trong Quý IV (ví dụ "01 lần/tháng, trong
   Quý IV/2026" hoặc hạn cuối 31/12/2026), không phải mốc đã qua của Quý III.
   → **Sửa lại mốc hạn cho khớp phạm vi Quý IV.**

---

## Mức 2 — nên sửa

4. **Tiêu đề Mục II không khớp mẫu chuẩn.** File ghi *"II. Các nhiệm vụ quý trước chuyển sang"*. Đối chiếu
   mẫu gốc `Phụ lục Ia — TB736` (`04-Good-Documents/04-03-.../5. TB 736...xlsx`, sheet "PL Ia. Mẫu KH Quý"),
   tiêu đề đúng là: **"Các nhiệm vụ đột xuất, phát sinh ở Quý trước phải thực hiện sang Quý sau (nếu có)"**
   — phạm vi hẹp hơn (chỉ nhiệm vụ đột xuất/phát sinh dở dang), không phải mọi nhiệm vụ quý trước nói
   chung. Cách đặt tên hiện tại có thể đã kéo theo lỗi Mức 1 số 2 ở trên (đưa cả nhiệm vụ đã hết hạn vào
   mà không cập nhật).
   → **Đổi tên mục II theo đúng mẫu, và rà lại xem 23 dòng trong mục này có đúng là "đột xuất, phát sinh
   dở dang" hay là nhiệm vụ thường kỳ bị gộp nhầm.**

5. **1 ô sai phông chữ (TX02, đo bằng `kiem_the_thuc.py`):** ô **F52** (cột "Số lượng", dòng 5.4 — "Kế
   hoạch triển khai các hoạt động chào mừng Ngày Nhà giáo Việt Nam 20/11") dùng **Calibri**, không phải
   Times New Roman như toàn bộ phần còn lại.
   → **Đổi phông ô F52 sang Times New Roman.**

---

## Mức 3–4 — góp ý, nên rà thêm

6. **Kiểu dữ liệu cột TT (cột A) không nhất quán.** Các mã `1.1`…`6.1` phần lớn lưu dạng **văn bản**, nhưng
   5 ô sau lưu dạng **số thực**: A37 (3.2), A38 (3.3), A39 (3.4), A40 (3.5), A57 (6.2). Không sai nội dung
   nhưng khác kiểu ô có thể gây lệch khi lọc/sắp xếp bảng.
   → Đổi 5 ô này về định dạng văn bản (Text) như các ô còn lại, để đồng nhất.

7. **Tên đơn vị "Đoàn TN - Hội SV" viết không thống nhất** giữa các dòng: `"Đoàn TN- Hội SV "` (dòng 44),
   `"Đoàn TN - Hội SV"` (dòng 51, 52), `"Đoàn TN- Hội SV"` (dòng 53), `"Đoàn TN;\nHội SV"` (dòng 70, 71) —
   4 cách viết khác nhau cho cùng một đơn vị.
   → Thống nhất một cách viết duy nhất trong toàn bộ tệp.

8. **Khoảng trắng thừa** trong tên đơn vị "Phòng  TCCB&CTHSSV" (hai khoảng trắng) ở dòng 56 và 74, trong
   khi các dòng khác (43, 50, 68, 76) ghi đúng "Phòng TCCB&CTHSSV" (một khoảng trắng).
   → Xoá khoảng trắng thừa.

9. **Ô F23 (cột "Số lượng", dòng 1.9)** ghi chữ **"Theo số lượng thực tế"** thay vì một con số, khác với
   toàn bộ các dòng còn lại trong cột này. Có thể là chủ ý (số lượng Quyết định phụ thuộc số ngành nghề
   phát sinh) nhưng nên ghi rõ hơn hoặc thống nhất cách trình bày (ví dụ để trống + ghi chú ở cột K thay vì
   ghi chữ trong cột số).

10. **Lề trang lệch nhẹ so với mẫu 05B** (chuẩn: trên 0,59″; dưới/trái/phải 0,5″). Tệp đang đo: trên 0,6″ ·
    dưới 0,5″ · **trái 0,7″ · phải 0,7″** (lệch mã TX04, mức 4 — chỉ nhắc, không bắt buộc sửa vì bảng vẫn
    vừa khổ A4 ngang).

---

## Đã đối chiếu và xác nhận đúng

- **Số 1976/QĐ-CĐKT ngày 14/9/2026** (Quy chế tổ chức và hoạt động) — khớp hồ sơ `KTC-Database`, đang hiệu
  lực (tệp đánh dấu `HIEN-HANH`).
- **Số 311/QĐ-CĐKT ngày 04/02/2026** (Chương trình công tác trọng tâm năm 2026) — khớp hồ sơ gốc.
- **Thang điểm/hệ số quy đổi** (100/1,0 · 120/1,2 · 150/1,5 · 200/2,0 theo mức Thấp/Trung bình/Cao/Khó và
  phức tạp) — đúng thang đang vận hành thật theo `20-Chuan-Chung/30-Skill-Phan-Loai-6-Truc.md`, **không**
  phải thang 5 nhóm dự thảo (50/120/250/350/450) — không nhầm lẫn hai thang.
- **Khổ giấy A4 ngang** — đúng chuẩn.
- **Phần "Căn cứ các Kế hoạch, Hướng dẫn của Tỉnh ủy, Đảng ủy UBND tỉnh, UBND tỉnh..."** (dòng 3 của A8)
  không nêu số hiệu cụ thể — đây là kiểu viện dẫn chung chấp nhận được cho nhóm căn cứ "chủ trương định
  hướng" (không phải căn cứ thẩm quyền trực tiếp), nhưng cách viết "Tỉnh ủy, Đảng ủy UBND tỉnh, UBND tỉnh"
  hơi tối nghĩa — **gợi ý** diễn đạt lại rõ hơn, ví dụ tách ba nhóm cơ quan bằng dấu phẩy rõ ràng hơn hoặc
  liệt kê cụ thể văn bản nếu có.

## Đối khớp với Kế hoạch năm / quý trước / dữ liệu công việc — bổ sung 22/9/2026

Đối chiếu 3 nguồn: **CTCT năm 2026** (`10-Dau-Vao/02-Cap-Truong/01-Nam/2026/CTCT-nam-2026-update.xlsx`), **KH
Quý III/2026 điều chỉnh, bổ sung** (`10-Dau-Vao/02-Cap-Truong/02-Quy/2026-Q3/...xlsx`), và thang điểm/hệ số ở
`11-Du-lieu-Cong-Viec`. Chưa có Kế hoạch tháng 10/11/12 vì Quý IV chưa bắt đầu (đúng quy trình).

### Với CTCT năm 2026 (Tháng 10-12, 12 nhiệm vụ trọng tâm)

10/12 nhiệm vụ trọng tâm khớp đúng nội dung, người chỉ đạo, đơn vị và Trục với KH Quý IV — **tốt**. 2 lệch:

- **Dòng 15** ("Đánh giá ngoài chất lượng CTĐT"): CTCT năm ghi người chỉ đạo **PHT Dương Văn Anh Dũng**, KH
  Quý IV ghi **PHT Huỳnh Văn Chung**.
- **Dòng 16** ("Thẩm định, ban hành quy trình BĐCL đợt 2"): CTCT năm ghi **PHT Dương Văn Anh Dũng**, KH Quý IV
  ghi **Hiệu trưởng**.
- **Dòng 17** (khảo sát các bên liên quan): CTCT năm ghi giai đoạn "lập kế hoạch khảo sát", KH Quý IV ghi
  "báo cáo kết quả khảo sát" nhưng cột sản phẩm vẫn để "Kế hoạch" — lệch pha tên việc/sản phẩm.

→ Cần xác nhận lại với các Phó Hiệu trưởng phụ trách xem CTCT năm hay KH Quý IV đúng.

### Với KH Quý III/2026 (điều chỉnh, bổ sung) — đối chiếu Mục II "chuyển sang"

Đối chiếu từng dòng trong Mục II của KH Quý IV với KH Quý III cho thấy **phần lớn các dòng có hạn "30/9/2026"
đều là nhiệm vụ Quý III chưa hoàn thành bị copy nguyên hạn cũ**, xác nhận rõ hơn phát hiện Mức 1 đã nêu ở
trên:

| Dòng KH Quý IV | Khớp với KH Quý III | Hạn gốc ở Quý III | Vấn đề |
|---|---|---|---|
| 59 | Mục I, 1.9 — Lễ tốt nghiệp | Tháng 9 | Hạn chưa cập nhật sang Quý IV |
| 60 | Mục I, 1.12 — Rà soát ngành nghề | Tháng 9 | Hạn chưa cập nhật |
| 61 | Mục III, BS-1.11 — ĐK đánh giá ngoài Lâm sinh | Tháng 8-9 | Hạn chưa cập nhật |
| 67 | Mục III, BS-3.05 — Bộ tiêu chí khởi nghiệp | Quý III | Hạn chưa cập nhật; tên việc cũng đổi khác |
| 81 | Mục III, BS-6.01 — Huấn luyện ATVSLĐ khóa V | Quý III | Hạn chưa cập nhật |
| 72 | Mục I, 5.7 — Ngày Phụ nữ VN 20/10 | Tháng 9 (chuẩn bị) | **Nghiêm trọng hơn**: sự kiện chính diễn ra 20/10 (Quý IV) nhưng hạn ghi 30/9 — hạn đứng TRƯỚC ngày sự kiện |

Ngoài ra:
- **Dòng 68** ("Đề án vị trí việc làm"): khớp Mục I 1.5 của Quý III, nhưng Quý III xếp **Trục 1**, KH Quý IV ghi
  **Trục 4** — lệch phân trục giữa hai kỳ (hạn đã cập nhật đúng sang Quý IV, chỉ trục bị lệch).
- **Dòng 76** ("Rà soát, đánh giá, thanh lý tài sản"): khớp Mục III BS-1.08 của Quý III (Trục 1, người chỉ đạo
  PHT Huỳnh Văn Chung), nhưng KH Quý IV đổi người chỉ đạo thành **Hiệu trưởng** và trục thành **Trục 5** — hai
  điểm lệch cùng lúc.
- **Dòng 75, 78**: không tìm thấy nhiệm vụ tương ứng trong KH Quý III (Mục I/II/III) theo tên việc — có thể là
  nhiệm vụ mới phát sinh bị xếp nhầm vào Mục II (dành cho nhiệm vụ chuyển từ quý trước), nên rà lại nguồn gốc.
- Phát hiện thêm: **KH Quý III/2026 (điều chỉnh, bổ sung) cũng ghi "1299/QĐ-CĐKT"** ở phần Căn cứ — xác nhận
  lỗi số hiệu đã lặp lại từ kỳ trước, không phải lỗi phát sinh riêng ở bản Quý IV. Nên báo P-THHC sửa dứt điểm
  cả nguồn Quý III lưu trữ.

### Với dữ liệu công việc (`11-Du-lieu-Cong-Viec`)

Thang điểm/hệ số quy đổi (100/1,0 · 120/1,2 · 150/1,5 · 200/2,0) khớp đúng thang đang vận hành thật — đã xác
nhận ở lượt rà soát trước, không phát hiện thêm sai lệch mới.

Đã cập nhật các ghi chú đối khớp trên vào cột L (GHI CHÚ RÀ SOÁT) của file `.xlsx` — ghi chú cũ giữ nguyên,
ghi chú mới nối thêm bằng dấu `||`.

## Ghi chú thêm

- Phát hiện phụ (ngoài phạm vi tệp này): kho `KTC-Database` có **hai hồ sơ khác nhau cùng dùng số 1229**
  — `08. Quy che lam viec cua Truong.docx` (Số 1229/QĐ-CĐKT, 27/5/2026) và một tệp metadata cũ
  `Metadata_QD-1229-QD-CDKT_Quan-ly-sang-kien_...CU-DA-THAY-THE-cho-xoa.md` (chủ đề khác, 19/8/2026, đã
  đánh dấu thay thế/chờ xoá). Không ảnh hưởng đến kết luận Mức 1 số 1 ở trên (tài liệu Quy chế làm việc là
  bản hiện hành, đã xác minh trực tiếp trong file .docx), nhưng nên báo P-THHC kiểm tra lại việc trùng số
  hiệu trong kho.
- Chưa chạy rà soát chính thức KTC-Ra-Soat-897 (chốt chặn bắt buộc trước khi trình ký) — đây mới là bước
  rà soát sơ bộ theo yêu cầu, cần chạy 897 sau khi đã sửa các mục Mức 1–2 ở trên.
