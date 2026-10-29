# BÁO CÁO CẬP NHẬT HỆ KTC-RA-SOAT-897 — Phiên bản v2.3 đến v2.5

**Ngày**: 18/8/2026 · **Căn cứ**: Báo cáo kiểm tra Hệ KTC-Ra-Soat-897 ngày 18/8/2026; bộ văn bản về tái cơ cấu tổ chức Đảng; bản PDF đầy đủ của Thông báo 597/TB-CĐKT

---

## 1. Bối cảnh

Báo cáo kiểm tra ngày 18/8/2026 phát hiện **12 vấn đề** trong gói Skill `ktc-ra-soat-897` phiên bản v2.2, trong đó **4 vấn đề Mức 1 – Bắt buộc sửa**. Toàn bộ đã được xử lý qua ba đợt cập nhật v2.3, v2.4 và v2.5.

Đặc điểm chung: **không phải thiếu dữ liệu** (mọi tài liệu chuẩn đều đã có trong KTC-Database hoặc trong gói Skill), mà là **dữ liệu chưa được chuyển hóa thành quy tắc kiểm tra ở lớp Skill và Checklist**. Bốn vấn đề Mức 1 đều nằm ở tệp `SKILL.md` — lớp điều phối được đọc đầu tiên mỗi lần chạy, nên sai lệch tại đây lan xuống toàn bộ sản phẩm đầu ra.

---

## 2. Bảng xử lý 12 vấn đề

| # | Vấn đề | Mức | Cách xử lý | Phiên bản |
|---|---|---|---|---|
| 1 | SKILL.md chỉ khai báo 3 mức phân loại lỗi, trong khi Mẫu prompt 897 và Skill 28 quy định 4 mức | **1** | Sửa thành đủ 4 mức, định nghĩa lấy nguyên từ Mẫu prompt 897 | v2.3 |
| 2 | SKILL.md ghi Phần IV là "Kiểm chứng chuyên môn", đúng ra là "Bảng tổng hợp" | **1** | Sửa thành "Bảng tổng hợp" (Bảng 1 theo nhóm, Bảng 2 theo mức độ) | v2.3 |
| 3 | Lề trang ghi "Trái 2cm / Phải 2cm" — vi phạm NĐ 30 (lề trái tối thiểu 30mm) | **1** | Sửa thành trái 30–35mm, phải 15–20mm; sửa cả script `build_tcdm_review_fixed.py` | v2.3 |
| 4 | Không nêu Bước 0 xác định hệ quy chiếu | 2 | Bổ sung mục "Bước 0 — bắt buộc thực hiện đầu tiên" | v2.3, mở rộng v2.5 |
| 5 | Mô tả chuẩn văn bản Đảng ghi sai là QĐ 399-QĐ/TW | 2 | Sửa thành HD 05-HD/VPTW ngày 27/5/2026 | v2.3 |
| 6 | Không có skill nào cho hệ văn bản quy phạm pháp luật (mục 1C Mẫu prompt 897) | 2 | Tạo `Skill-Library/30-Skill-Van-Ban-Quy-Pham-Phap-Luat.md` | v2.4 |
| 7 | Quy ước riêng của Trường chỉ nằm trong tệp .docx, chưa mã hóa vào Skill/Checklist | **1** | Tạo `Checklist/08-Quy-Uoc-Rieng-CDKT.md`, khai báo bắt buộc ở cả 4 tác vụ | v2.3, mở rộng v2.5 |
| 8 | 5/7 checklist viết tiếng Anh, chỉ nêu nguyên tắc trừu tượng, không có con số | 2 | Viết lại toàn bộ checklist 01–05 bằng tiếng Việt kèm số liệu định lượng của NĐ 30 và TB 597 | v2.4 |
| 9 | Tệp asset "v2.0-KTC-Enhanced" có MD5 trùng hệt bản gốc, không phải bản nâng cấp | 2 | Ghi chú rõ trong SKILL.md, chuyển chỉ định "Mẫu chuẩn cao nhất" về bản gốc | v2.3 |
| 10 | Không công bố giới hạn khi phiên làm việc không có công cụ tra cứu web | 2 | Bổ sung mục bắt buộc công bố "Chưa được xác minh bằng nguồn bên ngoài" | v2.3 |
| 11 | Phần VII chưa ghi rõ là tùy chọn và thiếu câu miễn trừ | 3 | Ghi rõ TÙY CHỌN kèm câu miễn trừ bắt buộc | v2.3 |
| 12 | Thiếu bảng cỡ chữ/kiểu chữ văn bản Đảng theo Phụ lục 2 HD 05-HD/VPTW | 2 | Tạo `Skill-Library/29-Phu-Luc-2-Co-Chu-Kieu-Chu-VB-Dang.md` đủ 15 thành phần | v2.4 |

**Kết quả**: 12/12 vấn đề đã xử lý. Không còn chuỗi tiếng Anh nào trong thư mục Checklist; script Python kiểm tra cú pháp đạt.

---

## 3. Nội dung bổ sung ngoài 12 vấn đề

### 3.1. Tái cơ cấu tổ chức Đảng 2026 (v2.3)

Tạo `Skill-Library/29-Phu-Luc-3-Tai-Co-Cau-To-Chuc-Dang-2026.md` và chèn khối cảnh báo đầu `29-Skill-Van-Ban-Dang.md`, theo QĐ 208-QĐ/TW (26/7/2026) và HD 02-HD/TW (07/8/2026).

Hai nguyên tắc được cấu hình cứng vào Skill:
1. **Không tự kết luận** loại hình tổ chức của Đảng bộ/Đảng ủy Trường — hiện có hai khả năng đều có căn cứ, phải hỏi người dùng và ghi vào phạm vi chưa xác minh.
2. Văn bản dùng tên gọi theo hệ cũ **không đương nhiên là lỗi** — QĐ 208 Chương VIII mục 3 cho phép quy định hiện hành tiếp tục áp dụng. Chỉ nêu ở Mức 4.

### 3.2. Rà soát Phụ lục TB 597 và bổ sung hệ đoàn thể (v2.5)

Sau khi đọc bản PDF đầy đủ của TB 597, bổ sung vào `Checklist/08-Quy-Uoc-Rieng-CDKT.md`:

| Nội dung bổ sung | Mục |
|---|---|
| Bảng chữ viết tắt **18 đơn vị**, hai cột dùng riêng biệt (số/ký hiệu vs hành văn) | 3.4 |
| Hình thức ký **TUQ.** (thừa ủy quyền) — trước đây thiếu | 5.1 |
| Mẫu ký hội đồng, ban chỉ đạo **hai tầng chức danh** | 5.2 |
| Quy tắc để trống ngày ban hành, cách **6 ký tự** | 5.3 |
| **9 mẫu thể thức đầu văn bản** thuộc 3 hệ thống | 7 |
| Danh mục **6 cặp văn bản đã bị thay thế** | 8 |

**Phát hiện quan trọng nhất**: Trường ban hành văn bản thuộc **BA hệ thể thức**, không phải hai. Ngoài hành chính nhà nước và Đảng, còn hệ **đoàn thể** — Công đoàn (theo Liên đoàn Lao động tỉnh, dùng Quốc hiệu/Tiêu ngữ), Đoàn Thanh niên và Hội Sinh viên (dùng tiêu đề tổ chức riêng, ba dấu sao, ký hiệu kiểu Đảng). Đã bổ sung thành hệ quy chiếu thứ tư trong Bước 0 của `SKILL.md` và trong `Checklist/03-Phap-Ly.md`, kèm ghi chú Skill chưa có bộ quy tắc đầy đủ nên phải công bố giới hạn.

### 3.3. Kết quả rà soát 4 mẫu văn bản Đảng tại Phụ lục TB 597

**Cả 4 mẫu đều đúng theo HD 05-HD/VPTW.** Điểm dễ bị hiểu nhầm là thiếu nhất quán, nhưng thực chất là đúng:

| Mẫu | Dòng trên | Căn cứ |
|---|---|---|
| 1.1 Đảng ủy Trường | ĐẢNG BỘ UBND tỉnh Quảng Ngãi | HD 05 mục 2.1.2d — ghi tên đảng bộ cấp trên trực tiếp |
| 1.4 Các chi bộ | ĐẢNG BỘ Trường Cao đẳng Kon Tum | HD 05 mục 2.1.2đ — chi bộ ghi tên đảng bộ cấp trên |
| 1.2 Ủy ban Kiểm tra, 1.3 Bộ phận VP Đảng ủy | ĐẢNG ỦY Trường Cao đẳng Kon Tum | HD 05 mục 2.1.3 — cơ quan tham mưu ghi tên cấp ủy trực thuộc |

Dấu sao, ký hiệu `/ĐU`, `/UBKT`, `/BPVPĐU`, `/CB` đều đúng. **Không mẫu nào cần sửa** nếu tên gọi loại hình tổ chức giữ nguyên. Chỉ mẫu 1.1 và 1.4 phải rà lại khi có kết quả xác nhận về tên gọi.

---

## 4. Ba phát hiện cần Phòng TH-HC&QT xử lý

### 4.1. Bản PDF của TB 597 đang lưu hành là bản CŨ

Danh mục bộ môn trong bản PDF vẫn là **14 bộ môn cũ** — có "bộ môn Công nghệ may", "bộ môn Điện và Điện tử", "bộ môn Đào tạo và lái xe mô tô" (thiếu chữ "Sát hạch"), và **không có** bộ môn Công nghệ thông tin, bộ môn Ngoại ngữ. Chỉ bản .docx trong kho 02-01 là bản đã cập nhật đủ 15 bộ môn (17/8/2026). Nếu Phòng còn phát hành bản PDF này, cần thay bằng bản mới.

### 4.2. Mẫu 3.3 Hội Sinh viên thiếu tiêu đề tổ chức

Mẫu 3.2 Đoàn Thanh niên có `ĐOÀN TNCS HỒ CHÍ MINH` ở cột phải; mẫu 3.3 Hội Sinh viên chỉ có địa danh và ngày, đáng lẽ phải có `HỘI SINH VIÊN VIỆT NAM`. **Mức 2 – Cần sửa.** Đề nghị xác minh với Hội Sinh viên tỉnh Quảng Ngãi rồi đính chính.

### 4.3. Đối chiếu hai bản QĐ 389/QĐ-CĐKT — nội dung giống nhau

Đã đọc toàn văn cả hai bản. **Không bản nào thiếu nội dung** — cả hai đủ Chương I–V, Điều 1–42, cùng số hiệu, ngày, căn cứ, người ký.

| | Bản trong kho (73.658 byte) | Bản cung cấp 18/8 (64.201 byte) |
|---|---|---|
| `docProps/thumbnail.emf` | Có (~25 KB ảnh xem trước) | Không có |
| Hyperlink tới cơ sở dữ liệu pháp luật ở căn cứ NĐ 99/2016 | Có | Không có |
| `word/document.xml` | Nhỏ hơn | 542 KB — lớn hơn do phân mảnh định dạng |

Bản cung cấp có dấu vết chỉnh sửa thủ công (số, ngày, số điều bị tách thành nhiều đoạn định dạng rời). **Khuyến nghị**: giữ bản trong kho làm bản chính thức, không cần thay thế.

---

## 5. Cấu trúc gói sau cập nhật

| Thư mục | v2.2 | v2.5 |
|---|---|---|
| `references/Checklist/` | 7 checklist + README | **8 checklist** + README (01–05 viết lại tiếng Việt kèm số liệu) |
| `references/Skill-Library/` | 14 tệp | **17 tệp** (thêm 29-Phu-Luc-2, 29-Phu-Luc-3, 30-Skill-VBQPPL) |

---

## 6. Lỗi tự phát hiện và đã sửa

Khi rà lại kho, phát hiện checklist `03-Phap-Ly.md` (do chính đợt cập nhật này soạn) ghi **sai số hiệu**: Quy chế làm việc là **QĐ 1299/QĐ-CĐKT** (27/5/2026), không phải 1229. QĐ 1229/QĐ-CĐKT (22/9/2023) là Quy chế đào tạo GDNN — văn bản hoàn toàn khác, hai số chỉ lệch một chữ số. Đã sửa và thêm cảnh báo phân biệt tại cả `03-Phap-Ly.md` và `08-Quy-Uoc-Rieng-CDKT.md`.

---

## 7. Việc còn lại cần Phòng TH-HC&QT xử lý

1. **Kéo-thả 2 tệp .docx** vào `01-Legal-Database/01-03`: QĐ 208-QĐ/TW và HD 02-HD/TW (connector không tải được tệp .docx dung lượng lớn; hồ sơ metadata đã nạp sẵn).
2. **Xin ý kiến xác nhận** của Đảng bộ UBND tỉnh Quảng Ngãi hoặc Ban Tổ chức Tỉnh ủy về tên gọi loại hình tổ chức áp dụng cho Đảng bộ Trường.
3. **Rà lại mẫu 1.1 và 1.4** tại Phụ lục TB 597 sau khi có xác nhận.
4. **Thay bản PDF TB 597** đang lưu hành bằng bản đã cập nhật 15 bộ môn.
5. **Xác minh mẫu 3.3 Hội Sinh viên** với Hội Sinh viên tỉnh.
6. **Xác minh chênh lệch NĐ 30**: bản trong kho 858.080 byte, bản cung cấp 866.121 byte — lệch 8.041 byte, chưa đối chiếu.
7. **Phê duyệt** các tệp mới — hiện đều ở trạng thái bản nháp.

---

## 8. Khuyến nghị về quy trình

Trong hai lần trước, các báo cáo cập nhật Skill ghi nhận đã hoàn thành phiên bản v2.4 và v2.6 nhưng kiểm tra thực tế cho thấy **các thay đổi chưa tồn tại** trong gói đang chạy. Đề nghị sau mỗi lần cập nhật Skill, thực hiện bước xác minh: kiểm tra tệp mới có tồn tại thật, và lịch sử phiên bản trong `SKILL.md` có ghi nhận đúng hay không, trước khi coi là đã hoàn thành.

---

**Nguồn dữ liệu đã dùng**: gói Skill ktc-ra-soat-897; KTC-Database (01-Legal-Database, 02-KTC-Regulations, 03-Templates, 04-Good-Documents, 11-Input); 13 tệp do người dùng cung cấp ngày 18/8/2026

**Phạm vi chưa xác minh**: hiệu lực hiện hành của các văn bản pháp luật được viện dẫn — phiên làm việc không có công cụ tra cứu web

**Người kiểm tra**: chưa xác định · **Trạng thái phê duyệt**: bản nháp, chưa phê duyệt
