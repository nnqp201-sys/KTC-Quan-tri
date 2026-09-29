# PHIẾU RÀ SOÁT KTC-897 — VÒNG 4 (BỔ SUNG, PHẦN CẬP NHẬT NGÀY 28 - 29/9/2026)

**Văn bản** (3 văn bản, rà từng văn bản):
1. Báo cáo quá trình xây dựng bộ công cụ trí tuệ nhân tạo KTC-Quan-tri — bản 6.
2. Tài liệu hướng dẫn sử dụng chi tiết Bộ công cụ KTC-Quan-tri (kèm theo Dự thảo Thông báo) — bản 7.
3. Báo cáo tiếp thu, giải trình ý kiến thẩm định độc lập lần 4 — bản 2.

**Tệp rà soát:** `30-Ket-Qua/2026-09-28/Soan-Thao/<văn bản>_20260928_v{6,7,2}_TrackChanges.docx` và bản sạch tương ứng.
**Phạm vi:** chỉ các vị trí có đánh dấu của tác giả “Cập nhật 28 - 29/9, bản 1.3.12 (Claude)”: Báo cáo quá trình 57 vị
trí, Tài liệu hướng dẫn 8 vị trí, Báo cáo tiếp thu 3 vị trí. Phần còn lại đã qua vòng 1 - 3 (phiếu trong
`3-Ra-soat-897/`).
**Công cụ:** Skill `ktc-ra-soat-897:review` (Core v3.0 + baseline v2.24; nạp `00-RUNTIME-INVARIANTS` →
`10-…-v3-Core` → `20-…-v2.24-BASELINE`, Checklist 01, 04, 05, 08).
**Căn cứ tổ chức rà soát:** điểm b Mục 8 Thông báo số 1056/TB-CĐKT ngày 16/9/2026 — vòng bổ sung cho phần sửa sau các vòng trước.
**Ngày rà soát:** 29/9/2026.

---

## PHẦN I. THÔNG TIN CHUNG

| Mục | Nội dung |
|---|---|
| Loại văn bản | (1), (3): Báo cáo của Phòng TH-HC&QT gửi Lãnh đạo Trường (mẫu 2.2 — văn bản của đơn vị thuộc Trường); (2): Tài liệu hướng dẫn kèm theo Thông báo |
| Hệ quy chiếu | **Hệ A** cho cả 3 văn bản (văn bản hành chính của Trường; NĐ 30/2020/NĐ-CP, Thông báo số 597/TB-CĐKT ngày 19/5/2026). Không có văn bản Đảng, đoàn thể, VBQPPL |
| Nguồn kho đã đọc | Kho 02: `QD-2119-QD-CDKT_Ban-hanh-Danh-muc-san-pham-cong-viec_20260928_v1.docx` và metadata (ban hành 28/9/2026, Hiệu trưởng ký, còn hiệu lực); `PL-2119-QD-CDKT_Danh-muc-san-pham-chuan-hoa_20260928_v1.xlsx` và metadata; Thông báo số 1056/TB-CĐKT (Mục 5, 8). Bộ quy tắc: Checklist 01, 05, 08 (bản gốc trên Drive, đọc 28/9/2026) |
| Nguồn không cần tra Internet | Các nội dung sửa không viện dẫn văn bản ngoài Trường |
| Đo thể thức (byte thật) | `ktc897_properties.py`: chữ ký ZIP `504b0304` hợp lệ cả 3 tệp; `kiem_the_thuc.py` (TT01 - TT19): (1), (3) 0 gợi ý; (2) 0 lỗi Mức 1 - 2, còn TT05, TT11 Mức 3 — có từ bản 3, đã chấp nhận ở vòng 2, 3 |
| Quét viện dẫn | `kiem_vien_dan.py` (VD01 - VD12): trước sửa (1) có 2 gợi ý VD12; sau sửa 0 gợi ý cả 3 văn bản |
| Track Changes | (1) 202 đánh dấu; (2) 18 (17 cập nhật, 1 “Người phụ trách (sửa trên bản sạch)”); (3) 6 |
| Bổ sung sau rà soát | Dòng 14 bảng kiểm thử của (1) và câu kết quả nghiệm thu 15 ca bản 1.3.12 trong (3), thêm khi có kết quả nghiệm thu ngày 29/9/2026 (`dot9-1312-`, `dot9b-1312-ca15-`). Đã rà trong cùng vòng: số liệu khớp tệp kết quả (14/15 ca, 28/30 lượt; chạy lại ca 15: 2/2), đo lại thể thức, viện dẫn 0 gợi ý; không phát hiện vấn đề |

## PHẦN II. KẾT QUẢ RÀ SOÁT CHI TIẾT

| Mã | Văn bản, vị trí | Bằng chứng | Vấn đề | Căn cứ | Mức | Kiến nghị | Xử lý |
|---|---|---|---|---|---|---|---|
| M2-01 | (1) Mục 7, đoạn “Các nội dung chưa thực hiện”, ý (iv) | “phần cập nhật ngày 28 - 29/9/2026 chưa rà soát bằng Skill “ktc-ra-soat-897”” | Sau vòng này, trạng thái ghi trong báo cáo không còn đúng — thông tin trạng thái sai trong văn bản trình | Checklist 02 (số liệu, trạng thái khớp thực tế) | 2 | “đã rà soát bổ sung (vòng 4) ngày 29/9/2026” | **Đã sửa** |
| M3-01 | (1) Mục 3, ô “Dừng, không tự đặt quy tắc” | “chưa có văn bản phân định (đã có văn bản: …)” | Hai vế liền nhau trái nghĩa, dễ đọc thành mâu thuẫn | Checklist 04 (logic câu) | 3 | “chưa có văn bản phân định (nay đã có: …)” | **Đã sửa** |
| M3-02 | (1) Bảng quá trình dòng 11; bảng trạng thái dòng 18 | “Quyết định số 2119/QĐ-CĐKT ngày 28/9/2026 ban hành Danh mục …” (lần thứ 2, 3 trong văn bản) | Viện dẫn lần sau vẫn ghi đầy đủ ngày ban hành | Checklist 08 mục 5.4; `kiem_vien_dan` VD12 | 3 | Lần sau chỉ ghi tên loại, số, ký hiệu | **Đã sửa** |
| M3-03 | (1) Bảng kiểm thử dòng 13 | “theo Thông báo số 597/TB-CĐKT, số trang” | Lần nhắc đầu trong Báo cáo chưa kèm ngày ban hành | Checklist 08 mục 5.4; quy tắc viện dẫn Trường (số hiệu nội bộ kèm ngày) | 3 | Thêm “ngày 19/5/2026” | **Đã sửa** |
| M3-04 | (1) Bảng kiểm thử, ô 24 bộ ca thử | “(plugin tự đủ, thể thức ánh xạ …, viện dẫn, thể thức, minh chứng …)” | Liệt kê “thể thức” hai lần | Checklist 04 (tính gọn, không lặp) | 3 | Bỏ lần lặp | **Đã sửa** |
| M3-05 | (1) Bảng kiểm thử dòng 13 | “phát hiện lỗi thật”; “đã xem trang bằng Word” | Từ ngữ khẩu ngữ, nêu tên phần mềm không cần thiết | Checklist 04 | 3 | “phát hiện lỗi thể thức”; “đã kiểm tra hiển thị từng trang” | **Đã sửa** |
| M3-06 | (3) Mục kế hoạch xử lý | Không có câu nào về việc rà soát 897 phần cập nhật 28 - 29/9 | Báo cáo tiếp thu thiếu kết quả rà soát bổ sung, không khớp (1) sau sửa M2-01 | Checklist 02 (tính thống nhất giữa các văn bản trong hồ sơ) | 3 | Bổ sung một câu kết quả vòng 4 | **Đã sửa** |
| M4-01 | (2) Đoạn “Soạn văn bản hành chính (từ phiên bản 1.3.11)” | “ráp nội dung vào mẫu cùng loại trong kho 03-Templates(1)” | Dùng tên thư mục kỹ thuật; người dùng đơn vị có thể chưa biết vị trí | Checklist 04 | 4 | Có thể ghi “kho mẫu văn bản (03-Templates(1)) của KTC-Database” | Giữ nguyên — tài liệu hướng dẫn kỹ thuật đã dùng tên thư mục ở các mục khác (chấp nhận vòng 2) |
| M4-02 | (1) Bảng kiểm thử dòng 12; bảng trạng thái dòng 20 | “0 lỗi thể thức Mức 1 - 2” | Cách ghi khoảng mức dùng “ - ” khác chỗ khác dùng “, ” | Checklist 04 | 4 | Thống nhất khi có dịp sửa | Giữ nguyên |

**Cách xử lý:** các điểm M2-01, M3-01 đến M3-05 nằm trong phần chèn của chính đợt cập nhật 28 - 29/9/2026 (chưa có người
duyệt), nên được sửa thẳng vào nội dung chèn của đợt đó rồi dựng lại Track Changes trên bản nền 27/9. Tác giả đánh dấu
vẫn là “Cập nhật 28 - 29/9, bản 1.3.12 (Claude)”. Riêng “viện dẫn, thể thức, minh chứng” (M3-04) là chữ bản nền, được đánh
dấu xóa. M3-06 là câu bổ sung mới trong (3).

### II.1. Kiểm lại vấn đề vòng 1 - 3 trong phần bị sửa

Tên công cụ rà soát (Skill “ktc-ra-soat-897”), giới hạn dữ liệu theo Thông báo số 924/TB-CĐKT, không ghi “đã đủ điều kiện”
khi chưa có biên bản: **không tái phát**. Số hiệu, ngày Thông báo số 1056/TB-CĐKT, 1052/TB-CĐKT giữ đúng.

## PHẦN III. NỘI DUNG ĐẠT / KHÔNG PHÁT HIỆN VẤN ĐỀ

- Số liệu kiểm chứng được bằng tệp trong hồ sơ, khớp nguồn: mã SHA-256 bản 1.3.12, 24/24 bộ ca thử, 434 văn bản đã ban
  hành, 16 mẫu trống, 2.289 lệnh chạy lại, 8.720 chữ/261 công thức (chạy độc lập), số lượt nghiệm thu từng đợt.
- Quyết định số 2119/QĐ-CĐKT viện dẫn đúng số, ký hiệu, ngày (đối chiếu bản trong kho 02); không dùng làm căn cứ ngoài phạm vi.
- Phân biệt rõ việc đã làm và chưa làm (nghiệm thu trên Claude, Cowork; thu hồi bản cũ cấp tổ chức; phân quyền kho).
- Tài liệu hướng dẫn: đoạn “Plugin tự đủ”, “Soạn văn bản hành chính” đúng với cách vận hành của bản 1.3.12; giữ chốt “người
  soạn vẫn mở tệp xem lại trước khi trình ký”.
- Quét toàn bộ phần cập nhật: không có “đảm bảo”, không có “nhà trường”/“Nhà trường”; viết hoa sau dấu hai chấm đúng Checklist 08 mục 2b.

## PHẦN IV. BẢNG TỔNG HỢP

| Mức | Số lượng | Đã sửa | Còn lại |
|---|---:|---:|---:|
| Mức 1 | 0 | 0 | 0 |
| Mức 2 | 1 | 1 | 0 |
| Mức 3 | 6 | 6 | 0 |
| Mức 4 | 2 | 0 | 2 (góp ý) |

## PHẦN V. THẨM ĐỊNH CHUYÊN MÔN (NẾU CÓ)

Không có nội dung chuyên môn cần thẩm định riêng trong phần cập nhật.

## PHẦN VI. ĐÁNH GIÁ TỔNG THỂ

Phần cập nhật ngày 28 - 29/9/2026 rõ, có số liệu và bằng chứng kèm theo; các vấn đề phát hiện chủ yếu là cách viện dẫn lần
sau, lặp ý và một thông tin trạng thái sẽ sai sau khi rà soát. Đã sửa hết Mức 2, Mức 3.

## PHẦN VII. KẾT LUẬN VÀ THỨ TỰ XỬ LÝ

- **Không còn vấn đề Mức 1, Mức 2** trong phần cập nhật của 3 văn bản.
- 2 góp ý Mức 4 để lần cập nhật sau.
- Kết luận này chỉ cho phần cập nhật ngày 28 - 29/9/2026; điều kiện trình ký của cả hồ sơ do người có thẩm quyền quyết định
  sau thẩm định độc lập vòng 5.

## KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG

| Mục | Kết quả |
|---|---|
| Phân hệ từng văn bản | Hệ A cả 3 văn bản, có căn cứ |
| Đo byte thật | Đã chạy `ktc897_properties.py`, `kiem_the_thuc.py` |
| Áp nhầm NĐ 30 cho Đảng, đoàn thể | Không có |
| Pháp luật hết hiệu lực làm khung hiện hành | Không có |
| Finding có bằng chứng, vị trí | Có |
| Metadata, người kiểm tra tự bịa | Không |

## THÔNG TIN TRÁCH NHIỆM

| Mục | Nội dung |
|---|---|
| Nguồn dữ liệu đã dùng | Kho KTC-Database 02 (Quyết định số 2119/QĐ-CĐKT, phụ lục, metadata; Thông báo số 1056/TB-CĐKT); bộ quy tắc KTC-Ra-Soat-897-v2-Cai-tien (Checklist 01, 04, 05, 08); tệp Track Changes và bản sạch của 3 văn bản |
| Người kiểm tra | [Người phụ trách Phòng TH-HC&QT — ký xác nhận] |
| Trạng thái phê duyệt | Bản nháp — chờ người có thẩm quyền xem xét |
