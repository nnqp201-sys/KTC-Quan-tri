# BẢNG CHỈ SỐ THEO THỜI GIAN — KTC-Quan-tri

Theo dõi chất lượng sản phẩm qua từng phiên bản, dùng **một bộ dữ liệu cố định** để so sánh được giữa các
lần đóng gói. Mô hình kế thừa: `KTC-Ra-Soat-897/13-Regression-Test/BANG-CHI-SO-THEO-THOI-GIAN.md`.

## Bộ dữ liệu và đáp án

| Vai trò | Nguồn |
|---|---|
| **Đầu vào** | `25-KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/` — 13 đơn vị · 13 `.docx` (Phụ lục IIa) + 27 `.xlsx` (IIb/Ib) |
| **Nguồn mục I** | `KH-Cap-Tren/Ke_hoach_cong_tac_Quy_III_2026_..._CHUAN.xlsx` — 85 nhiệm vụ |
| **Đáp án** báo cáo | `BC-375/BC-CĐKT` ngày 20/8/2026 |
| **Đáp án** phụ lục | `PL-375` — 39 nhiệm vụ |
| **Đáp án** kế hoạch | `KH-834/KH-CĐKT` ngày 28/8/2026 — 53 nhiệm vụ |

Điểm mạnh của bộ này: **đáp án là văn bản Trường đã thực sự ban hành**, không phải đáp án tự dựng.

## Cách chạy

```bash
python 29-Cong-Cu/trich_tuong_thuat.py && python 29-Cong-Cu/build_bc2.py && python 29-Cong-Cu/build_xl.py
python 29-Cong-Cu/chay_thu_ky.py --ghi
```

## Bảng tổng

| Ngày | Phiên bản | Đạt | Thể thức | 3 phần | Nhãn mục con | Văn phong | Quy mô PL | Quy mô KH | Công thức | Gộp ô PL | Gộp ô KH |
|---|---|---|---|---|---|---|---|---|---|---|---|
<!-- DONG-MOI -->
| 13/09/2026 | v1.0 | **2/9** | ✗ lệch (13pt, không thụt đầu dòng) | ✗ 6 mục | ✗ tự sinh nhãn | ✗ 6 vi phạm | ✗ 313 so với 39 | ✗ 175 so với 53 | ✓ | — | — |
| 14/09/2026 sáng | v1.1 | **6/9** | ✓ | ✓ | ✗ 5/28 = 18% | ✓ 0 | ✗ 211 so với 39 (lệch 441%) | ✗ 91 so với 53 | ✓ 211/211 | ✓ | ✓ |
| 14/09/2026 chiều | v1.2 | **9/9** | ✓ | ✓ | ✓ 18/18 = 100% | ✓ 0 | ✓ 41 so với 39 (lệch 5%) | ✓ 52 so với 53 (lệch 2%) | ✓ 41/41 | ✓ | ✓ |

## Ba bước nhảy — và nguyên nhân gốc của từng bước

### 2/9 → 6/9 : dựng từ văn bản đã ban hành, không từ mẫu trống

Bản đầu dựng từ mẫu trống `.dotx` nên sai thể thức (13pt thay vì 14pt, không có thụt đầu dòng 1,27cm) và
thiếu mục. Sửa bằng cách **mở chính `BC-375` rồi thay nội dung** — thể thức khớp tuyệt đối mà không phải
chỉnh tay. Đồng thời phát hiện bỏ sót **13 tệp `.docx`** (Phụ lục IIa) — nguồn duy nhất của văn tường thuật.

### 6/9 → 8/9 : nhãn mục con lấy từ mẫu, không tự sinh

Bản v1.1 tự sinh nhãn từ tên nội hàm TB 817 → chỉ **5/28 = 18%** nhãn nằm trong danh mục mẫu, kèm 12 lần
"Công tác khác". Trong khi **mẫu đã quy định sẵn** 6/2/0/3/4/3 mục con và từng mục lấy từ đơn vị nào.

Sửa: `29-Cong-Cu/chuan_bao_cao.py` **rút danh mục thẳng từ tệp mẫu**, không gõ tay — mẫu đổi thì code đổi theo.
Kết quả 18/18 = 100%, số mục con giảm 71 → 46 (BC-375 có ~50).

### 8/9 → 9/9 : lấy đúng nguồn cho phụ lục và kế hoạch

Sai nghiêm trọng nhất, và là sai **về bản chất chứ không phải mức độ**: gom toàn bộ nhiệm vụ từ báo cáo đơn
vị (211) trong khi phụ lục cấp Trường **báo cáo lại kế hoạch công tác của chính Trường**.

Bằng chứng dẫn tới kết luận: phụ lục tháng 7 khớp Kế hoạch quý III **39/41 = 95%**; chính tiêu đề mục I của
`KH-834` ghi *"nhiệm vụ theo kế hoạch công tác đã đề ra **từ đầu quý**"*.

Sửa: mục I lấy từ Kế hoạch quý (lọc theo cột "Thời gian hoàn thành" bao trùm tháng) → **41 nhiệm vụ tháng 8**
so với 39 của `PL-375`, **lệch 5%**.

## Điều đã KHÔNG làm, và vì sao

Mục II của phụ lục (*"Các nhiệm vụ chưa hoàn thành"*) **để trống có chủ đích**.

Thử đối sánh văn bản để suy ra nhiệm vụ nào chưa hoàn thành: cho **22/41** — hơn một nửa, trong khi
`PL-375` thật chỉ có khoảng 6. Phép đối sánh quá thô, tỷ lệ báo nhầm cao.

Quan trọng hơn: **"không tìm thấy trong báo cáo" không đồng nghĩa "chưa làm"** — đã có tiền lệ nhiệm vụ 2.8
hoàn thành thật (QĐ 1923/QĐ-CĐKT) nhưng không xuất hiện trong báo cáo đơn vị. Đưa 22 nhiệm vụ vào mục "chưa
hoàn thành" của văn bản chính thức là **quy kết sai cho đơn vị**.

Danh sách nghi ngờ xuất ra tệp riêng `Nghi-chua-hoan-thanh-thang-8.md`, ghi rõ là **nghi ngờ, cần đơn vị xác
nhận**, không đưa vào phụ lục.

## Chỉ số này KHÔNG đo được gì

Chín chỉ số đo **cấu trúc, thể thức, quy mô, văn phong** — đều là thứ máy kiểm được. Chúng **không** đo:

- **Độ nén và số liệu định lượng.** `BC-375` có "8 chương trình", "61 sản phẩm truyền thông", "tự chủ 23%".
  Bản sinh ra không có, vì **đơn vị không nộp số liệu tổng hợp** trong báo cáo tháng. Đây là giới hạn của
  dữ liệu đầu vào, muốn khắc phục phải sửa biểu mẫu nộp của đơn vị.
- **Nội dung có đúng sự thật không.** Chỉ người có thẩm quyền xác nhận được.
- **Chất lượng biên tập.** Cần người đọc.

Đạt 9/9 nghĩa là **sản phẩm đúng khuôn và đúng nguồn**, chưa nghĩa là dùng được ngay mà không biên tập.

## Quy tắc ghi bảng

- Mỗi lần đóng gói `.skill` phải có **một dòng số liệu mới**. Không có dòng mới thì không biết sửa xong có
  tốt lên hay không.
- Ghi kèm **phiên bản gói** đã dùng, không chỉ ghi ngày.
- Dòng mới chèn ngay dưới mốc `<!-- DONG-MOI -->` (mới nhất ở trên).
- Chỉ số tụt so với lần trước là **hồi quy** — phải tìm nguyên nhân trước khi phát hành.
