# Kết quả chạy lại — Báo cáo tháng 8 và Kế hoạch tháng 9/2026 (giả định)

**Ngày chạy:** 14/9/2026 · **Kỳ:** tháng 8/2026 (kèm kế hoạch tháng 9/2026)
**Căn cứ áp dụng:** `01-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md` (NT-1 → NT-4)
**Đầu vào:** 13 thư mục đơn vị trong `KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang` — **13 tệp `.docx`**
(Phụ lục IIa, báo cáo tường thuật) và **27 tệp `.xlsx`** (Phụ lục IIb/Ib, bảng nhiệm vụ).

---

## Sản phẩm

| Tệp | Phát triển từ | Quy mô |
|---|---|---|
| `BC_Bao-cao-thang-8-va-KH-thang-9-2026_DU-THAO_20260914.docx` | `BC-375/BC-CĐKT` ngày 20/8/2026 | 96 đoạn · 71 mục con · 3 phần I/II/III |
| `PL_Phu-luc-ket-qua-thang-8-2026_DU-THAO_20260914.xlsx` | `PL-375` | 211 nhiệm vụ · 225 hàng · 17 cột · khổ ngang |
| `KH_Ke-hoach-cong-tac-thang-9-2026_DU-THAO_20260914.xlsx` | `KH-834/KH-CĐKT` ngày 28/8/2026 | 94 nhiệm vụ · 111 hàng · 11 cột · khổ ngang |

**Thể thức đo bằng `python-docx`, đối chiếu trực tiếp với BC-375:** khổ 21cm · lề trên 2 · lề trái 3 ·
Times New Roman · 14pt · 2 bảng thể thức — **trùng khớp tuyệt đối**. Đây là hệ quả của việc *mở chính tệp
đã ban hành rồi thay nội dung* (NT-1), không phải dựng lại rồi chỉnh cho giống.

---

## Ba phát hiện làm thay đổi bản chất kết quả so với đợt chạy 13/9

### PH-1. Bỏ sót toàn bộ 13 báo cáo tường thuật `.docx`

Đợt trước chỉ đọc `.xlsx`. Nhưng mỗi đơn vị nộp **hai** tệp: bảng nhiệm vụ (`.xlsx`, Phụ lục IIb) **và
báo cáo tường thuật (`.docx`, Phụ lục IIa)**. Chính tệp `.docx` mới chứa văn tường thuật đã được đơn vị
chia sẵn theo **6 Trục** và theo lĩnh vực `a) b) c)`, kèm mục Nghị quyết 71 và mục Đánh giá chung.

Hệ quả: đợt trước phải ghép văn từ cột "Nội dung công việc" của bảng — nên văn rời rạc, và tôi đã phải tự
ghi nhận là "chưa đạt độ nén như BC-375". Đợt này lấy đúng nguồn văn tường thuật, **198 ý kết quả** và
**130 ý kế hoạch**.

**Bài học:** đếm *số loại tệp* mỗi đơn vị nộp trước khi đọc, đừng dừng ở định dạng đầu tiên tìm thấy.

### PH-2. Phụ lục cấp Trường có tiêu chí lọc — không phải gộp toàn bộ

`PL-375` đã ban hành chỉ có **39 nhiệm vụ**, `KH-834` có **53**. Đợt trước tôi xuất **313** và **175** —
sai không phải về mức độ mà về **bản chất**.

Đối chiếu cột "Người trực tiếp chỉ đạo" của hai bản đã ban hành: **100% là lãnh đạo cấp Trường** (Hiệu
trưởng, Phó Hiệu trưởng, Bí thư/Phó Bí thư Đảng ủy, Chủ tịch Công đoàn, Bí thư ĐTN, Chủ tịch HSV). **Không
có một dòng nào** do Trưởng khoa, Phó Trưởng khoa, Giáo vụ khoa hay Bí thư chi bộ chỉ đạo.

Đã áp dụng bộ lọc này: 211 nhiệm vụ (tháng 8) và 94 (tháng 9). **Vẫn cao hơn 39/53.**

**Kết luận trung thực:** lọc theo cấp chỉ đạo là **điều kiện cần đã kiểm chứng, nhưng chưa đủ**. Phần chênh
còn lại là **chọn lọc biên tập của cấp Trường** — tôi không tái lập được từ dữ liệu và **không tự đặt ra
tiêu chí cắt bớt**, vì cắt sai sẽ làm biến mất công việc có thật. Hai giả thuyết đã cân nhắc và chưa kiểm
chứng được: (a) chỉ lấy nhiệm vụ có trong Kế hoạch quý III; (b) gộp các nhiệm vụ tương tự do nhiều đơn vị
cùng báo cáo. Cần người có thẩm quyền xác nhận tiêu chí thật.

### PH-3. Danh mục nhiệm vụ chuẩn lệch với TB 817

`KTC-Du-lieu-Cong-Viec/.../Bang tong hop_phan tich_DANH_MUC_NHIEM_VU_CHUAN...xlsx` (122 nhiệm vụ) dùng
**tên Trục và Nội hàm khác** với TB 817/TB-CĐKT ngày 14/7/2026:

| | TB 817 (đã ban hành) | File danh mục (dự thảo lần 4) |
|---|---|---|
| Trục 1 | Thực hiện mục tiêu phát triển kinh tế – xã hội và nhiệm vụ chính trị được giao | Lãnh đạo thực hiện nhiệm vụ chính trị |
| Trục 2 | Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát | Xây dựng, hoàn thiện thể chế; nâng cao hiệu lực, hiệu quả quản trị |
| T4 Nội hàm 3 | Công tác tổ chức cán bộ | Công tác tổ chức bộ máy và phát triển nguồn nhân lực |

Đã lấy **TB 817 làm chuẩn** (văn bản đã ban hành, và BC-375 cũng đặt tiêu đề theo TB 817). Đề nghị rà soát
lại file danh mục cho khớp — ghi thành `KI-011`.

**Kèm theo:** điểm chấm trong file danh mục là **150/180**, trong dữ liệu thật là **100/120/150**. Không có
giá trị nào thuộc thang 50/120/250/350/450. Công thức `hệ số = điểm × 1%` đúng **211/211** dòng — củng cố
kết luận ở `LL-20260913-001`.

---

## Chuyển văn phong cấp đơn vị → cấp Trường

Ngoài quy tắc bỏ "tham mưu" và "phối hợp nội bộ" đã có từ trước, đợt này bổ sung **chuẩn hóa chủ ngữ**:
câu mở đầu bằng `Khoa …`, `Phòng …`, `BCH CĐCS Trường …`, `Ban Truyền thông …` được đổi thành **"Nhà
trường"** — dùng lookahead chữ thường để không ăn nhầm tên riêng (`Khoa Kỹ thuật và Công nghệ` giữ nguyên).

**Kết quả kiểm tra trên sản phẩm: 0 vi phạm** trên cả bốn phép kiểm (còn "tham mưu" · phối hợp nội bộ ·
trình/đề xuất Lãnh đạo · chủ ngữ cấp đơn vị).

---

## Lỗi tôi tự mắc và đã sửa trong đợt này

| # | Lỗi | Cách phát hiện |
|---|---|---|
| 1 | Phân loại lĩnh vực **tự do**, khiến mục "Xây dựng Đảng" có mục con "Công tác đào tạo" | Đọc lại bản in ra |
| 2 | Bộ phân loại theo **túi từ + IDF** trên mô tả nội hàm: "tiếp sinh, nhập học thí sinh trúng tuyển" → Trục 5 | Bộ 8 ca thử trước khi áp dụng |
| 3 | Nhãn chọn theo **thứ tự luật** thay vì vị trí khớp trong câu → nhãn lấy từ khóa ở cuối câu | Đọc lại nhãn |
| 4 | Cho nhãn "Công tác truyền thông" xét **trước** nội hàm → nhãn này xuất hiện ở cả 6 Trục, 12 lần | Đếm tần suất nhãn |
| 5 | Regex kiểm tra năm chứa **ký tự backspace 0x08 vô hình** → phép kiểm **không bao giờ khớp**, báo "sạch" giả | `cat -A` khi kết quả sạch một cách đáng ngờ |
| 6 | `phòng CSGT` bị bắt nhầm là đơn vị nội bộ | Rà danh sách vi phạm |

Lỗi số 5 đáng lưu ý nhất: **một phép kiểm tra hỏng luôn báo "không có lỗi"**. Đã ghi thành quy tắc: khi một
phép kiểm mới cho kết quả sạch ngay lần đầu, phải chạy nó trên một ca **biết chắc là sai** để xác nhận nó
thực sự bắt được lỗi.

---

## Lỗi hồ sơ của đơn vị (không tự sửa — cần đơn vị nộp lại)

| Đơn vị | Vấn đề |
|---|---|
| `Khoa-KT-NL` | Báo cáo `.docx` ghi **"tháng 7 năm 2026 và công tác trọng tâm tháng 8 năm 2027"** — sai cả kỳ báo cáo lẫn năm |
| `Khoa-KT-CN` | Không chia theo 6 Trục mà chia theo lĩnh vực tự đặt; phải phân loại lại bằng nội hàm TB 817 |
| `Phong-THHCQT` | Tệp là của **Ban Truyền thông**; các mục 2.1–2.4 còn để nguyên chỗ trống mẫu (`Chỉ thị …..`) |
| 2 dòng kế hoạch | Thời hạn ghi **`30/9/206`** — thiếu chữ số ở năm |
| 3 dòng | Thiếu **Đơn vị chủ trì** |
| 1 dòng | Thiếu **Điểm chấm công việc** |

---

## Giới hạn của bản dự thảo này

1. **Chưa có số liệu định lượng như bản đã ban hành.** BC-375 nêu "8 chương trình", "61 sản phẩm truyền
   thông", "tự chủ 23%". Bản này ghép từ mô tả công việc của đơn vị — đơn vị **không nộp số liệu tổng hợp**
   nên không thể sinh ra con số không có trong nguồn. Đây là giới hạn của dữ liệu đầu vào, không phải của
   quy trình.
2. **Quy mô phụ lục còn lớn hơn bản ban hành 5 lần** — xem PH-2.
3. **Mục con "Công tác khác"** còn 12 lần (6 mỗi phần) — là nhóm không khớp nội hàm nào của Trục tương ứng.
4. Chưa qua `KTC-Ra-Soat-897` — theo quy trình, đây là chốt chặn bắt buộc trước khi trình ký.

**Bản này là DỰ THẢO PHỤC VỤ CHẠY THỬ — không trình ký.**
