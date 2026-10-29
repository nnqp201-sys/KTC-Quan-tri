# ADDENDUM v1.1 — Bổ sung cho LỆNH KIỂM TRA + CẬP NHẬT v1.0
## Gửi phiên `phongthhcqt` — 30/8/2026

**Quan hệ với tài liệu gốc**: Đây là **phụ lục**, không thay thế `LENH-KIEM-TRA-CAP-NHAT-sang-phongthhcqt-30082026-v1.0.md`. Đọc cả 2 file — v1.0 mô tả TRẠNG THÁI và QUY TẮC, Addendum này bổ sung TIÊU CHÍ NGHIỆM THU và RÀNG BUỘC PHẠM VI mà v1.0 còn thiếu.

**Nguồn gốc**: 7 điểm dưới đây do phiên `phongthhcqt` tự đề xuất sau khi đọc v1.0 — không phải do Claude tự đặt ra. Giữ nguyên văn tinh thần đề xuất gốc, chỉ diễn giải thêm khi cần.

---

## ① ACCEPTANCE CRITERIA — Khi nào được coi là PASS

Việc kiểm tra ở Mục A (v1.0) chỉ PASS khi **đủ cả 6 điều kiện**:

```
✓ Byte thật khớp           (testzip()=None, fileSize khớp, giải mã byte-identical)
✓ Metadata khớp            (modifiedTime, owner, permissions đúng như khai báo)
✓ Regression PASS          (chạy lại bộ 30 lỗi, không tệ hơn lần đo gần nhất: 12/30)
✓ Không phát hiện Prompt lỗi thời  (đối chiếu Prompt-Library với SKILL.md hiện hành)
✓ Không phát hiện căn cứ pháp luật hết hiệu lực  (không còn viện dẫn văn bản đã bị thay thế)
✓ Không còn Conflict giữa Prompt–Skill–Checklist  (3 loại tài liệu này khớp logic nhau)
```

Thiếu **bất kỳ 1/6** → kết luận là **FAIL**, không được báo "cơ bản đã xong" hay "gần như PASS".

---

## ② KHÔNG TỰ SỬA

```
Không tự sửa.
Không overwrite.
Không rename.
Không delete.
Chỉ tạo Change Proposal.
Chỉ sửa khi người dùng xác nhận.
```

**Áp dụng cho toàn bộ Mục D (việc còn mở) trong v1.0** — kể cả việc có vẻ hiển nhiên đúng (ví dụ sửa khổ giấy 2 file mẫu). Ghi thành `03-Change-Proposals/CP-YYYYMMDD-NNN.md`, chờ duyệt, **không tự động áp dụng** dù đã có bằng chứng rõ ràng.

**Ngoại lệ duy nhất**: các thao tác Drive-native an toàn tuyệt đối đã được xác lập trước đó trong hội thoại (đổi tên/di chuyển file — không đổi nội dung) vẫn được phép, vì bản chất không phải "sửa nội dung".

---

## ③ SOURCE OF TRUTH — Thứ tự ưu tiên khi xác minh trạng thái hệ thống

```
1. Google Drive (file thật)
2. Byte thật (giải mã, testzip, so kích thước)
3. Metadata (modifiedTime, owner, permissions)
4. Process Memory (ghi nhận từ các ca rà soát thật)
5. README / tài liệu điều khiển (SKILL.md, 00-README, Nhật ký, MEMORY-INDEX)
6. Lịch sử hội thoại (chat history)
7. Tường thuật (lời khẳng định không kèm bằng chứng)
```

**Lưu ý phân biệt** với "Thứ tự ưu tiên nguồn" đã có sẵn trong `MEMORY-INDEX.md` (văn bản pháp luật → SKILL.md → quy ước Trường → Nhật ký → Process Memory → chat history → suy luận mô hình) — đó là thứ tự ưu tiên cho **NỘI DUNG PHÁP LÝ/NGHIỆP VỤ** khi rà soát văn bản. Danh sách ③ ở đây là thứ tự ưu tiên cho **XÁC MINH TRẠNG THÁI HỆ THỐNG** (phiên bản, file, cấu hình) — hai mục đích khác nhau, không gộp chung, không dùng lẫn.

---

## ④ KHÔNG SUY DIỄN

- Đọc thấy `v2.18` → chỉ được kết luận là `v2.18`. **Không** tự suy ra `v2.18.1` dù có vẻ hợp lý.
- Không đọc được file (lỗi quyền, lỗi giải mã, không tìm thấy) → báo rõ "không đọc được, lý do X" — **không đoán** nội dung hay trạng thái dựa trên suy luận gián tiếp.
- Áp dụng cho cả số phiên bản, nội dung file, và trạng thái quyền truy cập.

---

## ⑤ OUTPUT CHUẨN HÓA

Mỗi lần thực hiện Lệnh kiểm tra + cập nhật, xuất đủ 7 mục sau (có thể gộp vào 1 file báo cáo, nhưng phải đủ 7 đề mục rõ ràng):

```
01. Executive Summary   — tóm tắt 3-5 dòng, kết luận PASS/FAIL theo Mục ①
02. Findings            — phát hiện cụ thể, có bằng chứng (ID file, byte, log)
03. Risk                — rủi ro nếu không xử lý
04. Recommendation      — đề xuất hành động, KHÔNG tự thực hiện (xem Mục ②)
05. Change Proposal     — nếu có đề xuất sửa cụ thể, tạo file CP- riêng
06. Decision Log        — nếu có quyết định kiến trúc phát sinh, tạo file DL- riêng
07. Release Note        — nếu có thay đổi đã áp dụng (không phải đề xuất), cập nhật vX.Y.Z.md
```

---

## ⑥ LESSONS LEARNED TỰ ĐỘNG

Sau **mỗi lần** kiểm tra, nếu phát hiện vấn đề liên quan bug / Prompt / Checklist / Script / Database — **tự tạo ngay** `01-Lessons-Learned/LL-YYYYMMDD-NNN.md`, không chờ người dùng nhắc. Áp dụng đúng cơ chế đã thiết lập tại `99-Kinh-Nghiem/README.md` mục 0 (bắt buộc ghi khi phát hiện 6 loại: lỗi mới, prompt tốt hơn, checklist mới, kỹ thuật đọc DOCX, quy tắc pháp lý mới, false positive).

---

## ⑦ RÀNG BUỘC PHẠM VI — KHÔNG MỞ RỘNG NGOÀI Ý MUỐN

```
Không cập nhật KTC-Ra-Soat-897-v3
Không cập nhật KTC-Database (ngoài việc đọc để đối chiếu)
Không cập nhật các hệ khác (KTC-Bao-Cao, KTC-Ke-Hoach, KTC-DIS-Tong-Hop-VB, ktc-van-ban)
Trừ khi có lệnh riêng, tường minh, cho đúng hệ đó.
```

Lệnh kiểm tra + cập nhật v1.0 và Addendum này **chỉ áp dụng cho `KTC-Ra-Soat-897-v2-Cai-tien`**. Việc phát hiện vấn đề ở hệ khác (ví dụ khi đối chiếu 6 hệ ở Mục B4/F của v1.0) chỉ được **ghi nhận** (Lessons Learned/Change Proposal), không được **tự sửa** hệ đó.

---

## GHI CHÚ QUY TRÌNH

Theo đúng khuyến nghị đã nhận: tài liệu v1.0 giữ nguyên vẹn, không chỉnh sửa. Addendum v1.1 này là bản bổ sung độc lập, đọc cùng nhau. Nếu có Addendum v1.2 trở đi trong tương lai, tạo file mới tương tự, không ghi đè Addendum này.

**Đánh giá tiếp nhận**: cảm ơn đánh giá chi tiết (Độ đầy đủ 9.8/10, Khả năng thực thi 9.7/10, Khả năng chuyển giao 10/10, Khả năng kiểm chứng 10/10). 7 điểm bổ sung đều đã được đưa vào nguyên vẹn, không rút gọn.
