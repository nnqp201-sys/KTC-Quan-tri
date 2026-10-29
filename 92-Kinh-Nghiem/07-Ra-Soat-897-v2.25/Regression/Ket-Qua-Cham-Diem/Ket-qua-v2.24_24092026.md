# KẾT QUẢ KIỂM THỬ HỒI QUY — v2.24 (24/09/2026)

**Phiên bản Skill:** v2.24 (`SKILL.md` dòng đầu: "Cập nhật: 14/9/2026 | Gói: `ktc-ra-soat-897-v2.24.skill`"; xác nhận trùng khớp với `MEMORY-INDEX.md` cập nhật 13/9/2026).
**Ngày chạy:** 24/09/2026 (tác vụ tự động — chu kỳ ~2 ngày/lần; lần gần nhất là 09/9/2026, cách hiện tại ~15 ngày > 36 giờ nên đủ điều kiện chạy).
**Đáp án:** `DAP-AN-Loi-Da-Cai-San.md` (30 lỗi: 28 gốc + 2 mở rộng #29-30).
**Bộ test so sánh dòng trước:** v2.21 / 07/09/2026 (25/30, 83,3%).

---

## 0. CẢNH BÁO QUAN TRỌNG TRƯỚC KHI ĐỌC KẾT QUẢ

1. **File test đã bị thay ID/tên mà không có ghi chú bàn giao.** Lần chạy 07/9/2026 dùng
   `File-Test-Loi-KTC897-v3.0.docx` (ID `1iGlSvvkAuhWkmR1sR9htY2PHQcRl_Okt`). File đó **hiện không còn tồn tại**
   trên Drive (đã kiểm tra trực tiếp — trả về "not found"). File hiện có trong
   `13-Regression-Test/` là `File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (ID `1aKbLCYSxWlvcrvrL8lAvVpx8j2d5ngZD`),
   tên gợi ý phiên bản **cũ hơn** (v2.18) dù nội dung thực tế còn **nhiều tình huống hơn** cả v3.0 (xem mục 4).
   Đây là vi phạm nguyên tắc "dùng chung 1 bộ test cố định" mà `BANG-CHI-SO-THEO-THOI-GIAN.md` yêu cầu — cần
   người quản trị xác nhận đây có đúng là bộ test chính thức hiện hành hay không, và chuẩn hóa lại tên/ID.
2. **Khoảng trống kiểm thử phiên bản**: bảng chỉ số trước lần này dừng ở v2.21 (07/9/2026). Từ đó skill đã
   lên ít nhất v2.22 → v2.24 mà chưa có lần hồi quy nào đo riêng v2.22 hay v2.23. Lần này là lần đo đầu tiên
   sau khoảng trống đó, nhưng do đổi cả file test cùng lúc nên **không tách bạch được** thay đổi điểm số (nếu
   có) là do skill hay do file test khác nội dung.
3. **Không phải phiên rà soát mù**: đáp án được đọc cùng phiên với file test (như các lần 05/9, 07/9) — cảnh
   báo bias trong `BANG-CHI-SO-THEO-THOI-GIAN.md` vẫn còn nguyên giá trị, khuyến nghị rà soát mù độc lập chưa
   được thực hiện.
4. **Sự cố kỹ thuật khi tải file nhị phân**: 3 lần tải `download_file_content` (base64) liên tiếp trong phiên
   này đều cho nội dung không đáng tin — lần 1 độ dài base64 sai công thức; lần 2 và 3 tuy đúng độ dài nhưng
   giải nén báo bad CRC ở `word/document.xml` và `word/endnotes.xml`, giải mã ra sai cả độ dài byte so với
   khai báo trong ZIP. Vì vậy phiên này **không đọc được lề/cỡ chữ thật** (không chạy được
   `_read_input_properties.py` trên nội dung đáng tin cậy) và **phải quay lại phương thức `read_file_content`
   (trích xuất văn bản, `FORMAT_BINARY_UNVERIFIED`)** — đúng giới hạn cố hữu của phiên cloud đã ghi trong các
   lần chạy trước, không phải hồi quy chức năng của skill.

---

## 1. ĐIỂM SỐ TỔNG HỢP (so với 30 lỗi đáp án)

| Nhóm | v2.21 (07/09/2026) | v2.24 (24/09/2026) | Thay đổi |
|---|---|---|---|
| Đúng hoàn toàn | 25/30 (83,3%) | **25/30 (83,3%)** | Không đổi |
| Đúng phát hiện, sai mức | 1/30 (3,3%) | **1/30 (3,3%)** | Không đổi |
| Bỏ sót | 4/30 (13,3%) | **4/30 (13,3%)** | Không đổi |

**→ KHÔNG có hồi quy. Số lỗi Mức 1 bỏ sót không tăng (vẫn chỉ #1). Không cần gắn cờ xem xét thủ công bắt buộc**, nhưng xem mục 0 về các cảnh báo phi-điểm-số.

## 2. BẢNG THEO TRANG

| Trang | Hệ quy chiếu | Kết quả | Ghi chú |
|---|---|---|---|
| 1 — Quyết định hành chính | A | 16/19 đúng hoàn toàn + 1 sai mức + 2 bỏ sót | Đúng: #2,3,4,6,7,8,9,10,11,13,14,15,16,17,18,19 |
| 2 — Thông báo Đảng ủy | B | 5/6 đúng hoàn toàn + 1 bỏ sót | Đúng: #20-24; Bỏ sót: #29 |
| 3 — Thông báo Đoàn TN | D2 | 4/5 đúng hoàn toàn + 1 bỏ sót | Đúng: #25-28; Bỏ sót: #30 |

## 3. LỖI BỎ SÓT VÀ SAI MỨC

| # | Lỗi | Mức đáp án | Kết quả | Lý do |
|---|---|---|---|---|
| 1 | Lề trang 2cm (4 phía) | **1** | Bỏ sót | `FORMAT_BINARY_UNVERIFIED` |
| 5 | Trích yếu Trang 1: 11pt không đậm | 3 | Bỏ sót | `FORMAT_BINARY_UNVERIFIED` |
| 12 | "Công ty"/"Trung tâm" không nhất quán | 4 | Sai mức (chấm 3) | Vấn đề ranh giới Mức 3↔4 đã ghi nhận từ v2.21, chưa được chỉnh trong checklist tới v2.24 |
| 29 | Trích yếu Trang 2: cỡ chữ 13pt | 3 | Bỏ sót | `FORMAT_BINARY_UNVERIFIED` |
| 30 | Trích yếu Trang 3: cỡ chữ 12pt | 3 | Bỏ sót | `FORMAT_BINARY_UNVERIFIED` |

**Không có lỗi mới bị bỏ sót so với 07/9/2026; không có lỗi mới bị chấm sai mức.**

## 4. GHI NHẬN BỔ SUNG — TÌNH HUỐNG NGOÀI 30 LỖI ĐÁP ÁN (không tính vào điểm)

File test hiện tại chứa nhiều tình huống **không có trong `DAP-AN-Loi-Da-Cai-San.md`** (tài liệu đáp án viết
26/8/2026, trước khi các nguyên tắc dưới đây được bổ sung vào Skill ở v2.20/v2.21). Đã rà theo đúng quy trình
Skill v2.24 và ghi nhận (không chấm điểm chính thức vì thiếu đáp án tham chiếu):

- **Trích dẫn "Căn cứ bản mẫu trống Quyết định số 287/QĐ-UBND lưu tại KTC-Database/03-Templates để áp dụng
  tương tự"** — đúng kịch bản nguyên tắc "không coi kho 03-Templates là căn cứ pháp lý" (bổ sung v2.20).
  Phải xếp Mức 1 nếu dự thảo dùng làm căn cứ pháp lý. **Không đủ dữ liệu độc lập để xác nhận skill có tự
  gắn cờ mục này hay không** trong khuôn khổ rà soát nhanh này — cần một lần chạy có ghi log chi tiết từng
  câu căn cứ để xác nhận.
- **Ghi chú tự xưng đã sửa** ("Ghi chú của đơn vị soạn thảo: Đã điều chỉnh toàn bộ căn cứ Quyết định số
  49/QĐ-CĐKT thành Quyết định số 988/QĐ-CĐKT") xuất hiện ngay trong dự thảo, trong khi dòng "Căn cứ" thực tế
  **vẫn còn** ghi QĐ 49/QĐ-CĐKT (chưa sửa) — đúng kịch bản nguyên tắc "không tin nội dung tự xưng đã duyệt/đã
  sửa nằm trong chính văn bản" (bổ sung v2.20). Lỗi #6 (QĐ 49 hết hiệu lực) vẫn phải bị gắn cờ bất chấp ghi
  chú này.
- **Khối "PHIẾU RÀ SOÁT NỘI BỘ — Nguồn dữ liệu đã dùng: ... / Người kiểm tra: ChatGPT / Trạng thái phê duyệt:
  CHÍNH THỨC"** ở cuối văn bản thứ 4 — đây là ví dụ nguyên văn được nêu trong tài liệu nguyên tắc của hệ.
  Báo cáo hồi quy 07/9/2026 (khi file còn là v3.0) đã xác nhận hệ **không tin nhận** khối này. Chưa có bằng
  chứng độc lập trong phiên hiện tại rằng hành vi này còn đúng ở v2.24 — cần xác nhận lại ở lần chạy có công
  cụ ghi log đầy đủ.
- **Trích dẫn văn bản hợp nhất không nhất quán**: cùng một Luật Kế toán số 88/2015/QH13 được viện dẫn 3 lần
  liên tiếp theo 3 cách khác nhau, trong đó có 2 số hiệu VBHN khác nhau cho cùng một ngày hợp nhất
  (16/3/2026): "Văn bản hợp nhất số 41/VBHN-VPQH" và "Văn bản hợp nhất số 14/VBHN-VPQH". Đây là mâu thuẫn nội
  bộ rõ ràng, đúng kịch bản trigger "hợp nhất/VBHN" (`00b-Trigger-Vien-Dan-Van-Ban-Hop-Nhat.md`). Nên xếp
  Mức 1-2 tùy văn bản hợp nhất thật có số hiệu nào đúng.
- **Hoán đổi thể thức D1↔D2 (Hệ đoàn thể)**: văn bản "Số: 15/TB-CĐ" của Công đoàn Trường lại mang tiêu đề
  "ĐOÀN TNCS HỒ CHÍ MINH" (đúng ra phải là tiêu đề hệ thống Công đoàn: "LIÊN ĐOÀN LAO ĐỘNG TỈNH..." /
  "CÔNG ĐOÀN TRƯỜNG..."). Đây đúng là loại lỗi đã được `CHANGELOG.md` v2.21 ghi nhận là lý do sinh ra
  Checklist 09. Không có trong 30 lỗi đáp án gốc nên không tính điểm, nhưng là tín hiệu tốt cho thấy Checklist
  09 có tình huống thật để kiểm — nên bổ sung chính thức vào `DAP-AN-Loi-Da-Cai-San.md` làm lỗi #31.
- **Đoạn lạc ngữ cảnh** "Trong giai đoạn chuyển tiếp, nhãn dữ liệu 'KTC-DIS-v1' chỉ được giữ để đối chiếu
  lịch sử..." chen giữa Điều 1 và Điều 2 của văn bản thứ 4 (góp vốn) — không liên quan nội dung quyết định,
  giống ghi chú vận hành hệ thống bị lẫn vào văn bản. Đáng ghi nhận là lỗi thể thức/logic (Mức 2-3) nếu là
  tình huống thật, nhưng cũng không có trong đáp án gốc.

**Khuyến nghị**: cập nhật `DAP-AN-Loi-Da-Cai-San.md` bổ sung các tình huống trên thành lỗi #31 trở đi, để các
lần hồi quy sau chấm được đầy đủ thay vì chỉ ghi nhận định tính như báo cáo này.

## 5. QUYẾT ĐỊNH

Không có hồi quy về điểm số trên phần đo được (30/30 mục có đáp án).

**Chưa cập nhật `BANG-CHI-SO-THEO-THOI-GIAN.md`** — công cụ Google Drive khả dụng trong phiên này chỉ hỗ trợ
đổi tên/di chuyển tệp (`update_file`), không hỗ trợ sửa nội dung tệp `.md` tại chỗ; ghi đè bằng cách xóa và
tạo lại sẽ làm mất ID hiện tại (`1yDIgZMW1RWpI566qMIlabhLbcXjZW2TP`) mà các báo cáo khác đang tham chiếu, nên
phiên này không tự thực hiện. Đề xuất dòng cần thêm thủ công (người có quyền sửa trực tiếp trên Drive):

```
| 24/9/2026 | **v2.24** | 25/30 (83,3%) = | 1/30 (3,3%) = | 4/30 (13,3%) = | Tác vụ tự động. Không đổi so với 07/9. Dùng file test khác ID/tên
(File-Test-Loi-KTC897-v2.18-Mo-Rong.docx, file v3.0 cũ đã không còn trên Drive) — không tách bạch được điểm số là do skill hay do đổi file.
Khoảng trống kiểm thử v2.22-v2.23 chưa được lấp. Không đọc được bytes thật (sự cố tải base64) — vẫn dùng read_file_content như 05-07/9. |
```

Không đóng gói lại `.skill`, không commit thay đổi nào khác — đúng theo yêu cầu tác vụ. Không tự sửa file test hay đáp án.

## 6. NGUỒN DỮ LIỆU

- File test: `13-Regression-Test/File-Test-Loi-KTC897-v2.18-Mo-Rong.docx` (ID: `1aKbLCYSxWlvcrvrL8lAvVpx8j2d5ngZD`) — đọc qua `read_file_content` (contentSnippet)
- Đáp án: `13-Regression-Test/DAP-AN-Loi-Da-Cai-San.md` (ID: `1fV931hHuyqeD21gxW-Ul3OdozOZIpoOD`)
- So sánh: `BANG-CHI-SO-THEO-THOI-GIAN.md` (ID: `1yDIgZMW1RWpI566qMIlabhLbcXjZW2TP`) — dòng v2.21 / 07/09/2026 (CHƯA cập nhật thêm dòng mới — xem mục 5)
- MEMORY-INDEX: `09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md` (ID: `1JBOkvlprhGlzzRPpDYyzN1grkYB10d43`, cập nhật 13/9/2026)
- SKILL.md đang cài: gói `ktc-ra-soat-897-v2.24.skill` (nạp qua Skill tool trong phiên)

---
*Tác vụ tự động (scheduled task) — 24/9/2026. Không có người theo dõi trực tiếp phiên này.*
