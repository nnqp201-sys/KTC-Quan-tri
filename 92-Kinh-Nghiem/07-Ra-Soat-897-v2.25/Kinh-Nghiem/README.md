# 99-Kinh-Nghiem — README
## "Knowledge Evolution Layer" của Hệ KTC-Ra-Soat-897-v2

**Ngày lập**: 30/8/2026 · **Mở rộng**: 30/8/2026 (từ 3 → 6 thư mục, theo yêu cầu anh Phục)

Đây là **bộ não tiến hóa** của Hệ — nơi duy nhất lưu đầy đủ lịch sử quyết định, kinh nghiệm thực chiến, đề xuất và thay đổi đã kiểm chứng. Khi phát triển v3.0, chỉ cần đọc thư mục này là đủ để kế thừa có chọn lọc, không cần đọc lại toàn bộ lịch sử hội thoại.

---

## 0. QUY TẮC BẤT BIẾN — KHÔNG LƯU PROMPT/CHECKLIST/SKILL CHÍNH THỨC Ở ĐÂY

`99-Kinh-Nghiem/` **chỉ** chứa: kinh nghiệm · quyết định · đề xuất · regression · release notes · bài học.

**KHÔNG** chứa nội dung nghiệp vụ chính thức — các thứ đó vẫn ở đúng vị trí cũ:

| Loại nội dung | Vị trí chính thức (KHÔNG đổi) |
|---|---|
| Prompt chính thức | `references/Prompt-Library/` |
| Checklist chính thức | `references/Checklist/` |
| Skill chính thức | `references/Skill-Library/` |

Lý do: `99-Kinh-Nghiem/` mô tả **quá trình tư duy dẫn tới thay đổi**, không phải bản thân thay đổi đó. Trộn lẫn 2 loại sẽ khiến không rõ đâu là "đang chạy thật" và đâu là "đang được cân nhắc".

---

## 1. CẤU TRÚC ĐẦY ĐỦ

```
99-Kinh-Nghiem/
├── README.md                    ← file này
├── 01-Lessons-Learned/          ← tri thức thực chiến (LL-YYYYMMDD-NNN.md)
├── 02-Regression/
│   ├── Cases/                   ← mô tả từng ca kiểm thử (input, bối cảnh)
│   ├── Fixtures/                ← file .docx/.py dùng làm dữ liệu test cố định
│   ├── Expected-Results/        ← kết quả kỳ vọng cho từng Case (đối chiếu khi chạy lại)
│   └── Regression-Report.md     ← tổng hợp kết quả qua các lần chạy
├── 03-Change-Proposals/         ← đề xuất chờ duyệt (CP-YYYYMMDD-NNN.md)
├── 04-Release-Notes/            ← ghi chú phát hành theo tinh thần Git (vX.Y.Z.md)
├── 05-Known-Issues/             ← lỗi đã biết nhưng CHƯA sửa ngay
└── 06-Decision-Log/             ← quyết định kiến trúc, có lý do + người phê duyệt (DL-YYYYMMDD-NNN.md)
```

---

## 2. VAI TRÒ TỪNG THƯ MỤC

### 01-Lessons-Learned/ — Tri thức thực chiến
Ví dụ: prompt nào hiệu quả hơn · cách phát hiện lỗi mới · quy định pháp luật dễ bị AI hiểu sai · cấu trúc văn bản đặc thù. Đây là **tri thức, không phải code** — không cần cấu trúc chặt, chỉ cần: chuyện gì → tại sao → rút ra được gì.

Tên file: `LL-YYYYMMDD-NNN.md` (NNN = số thứ tự 3 chữ số trong ngày, ví dụ `LL-20260830-001.md`).

### 02-Regression/ — Bộ dữ liệu kiểm thử có cấu trúc
- `Cases/` — mô tả ca kiểm thử (input là gì, bối cảnh)
- `Fixtures/` — file dữ liệu cố định dùng lại được
- `Expected-Results/` — kết quả đúng kỳ vọng, đối chiếu khi chạy lại
- `Regression-Report.md` — tổng hợp qua các lần chạy

Ví dụ 1 Case:
```
Case 031
Input: QuyetDinh.docx
Expected:
  Mức 1: 2
  Mức 2: 5
  Mức 3: 6
```

**Phân biệt với `13-Regression-Test/` đã có từ trước**: `13-Regression-Test/` là bộ hồi quy CHÍNH THỨC cố định (30 lỗi, dùng để đo điểm số qua từng phiên bản — xem `BANG-CHI-SO-THEO-THOI-GIAN.md`). `02-Regression/` ở đây là nơi lưu các **case kiểm thử phát sinh thêm** trong quá trình phát triển (ví dụ case riêng cho 1 Change Proposal cụ thể), không thay thế bộ 30 lỗi chính thức.

### 03-Change-Proposals/ — Hàng chờ trước khi merge
Mọi ý tưởng mới đều vào đây trước, có Regression đính kèm để chứng minh đã kiểm chứng:
```
CP-20260830-015
Đề xuất: Thêm kiểm tra VBHN.
Lý do: ...
Tác động: ...
Regression: Đã PASS.
```
Chỉ merge vào `references/` sau khi Regression PASS và được phê duyệt (ghi vào `06-Decision-Log/`).

Tên file: `CP-YYYYMMDD-NNN.md`.

### 04-Release-Notes/ — Đúng tinh thần Git
```
v2.18.3
Added: ...
Fixed: ...
Changed: ...
Removed: ...
Regression: ...
Known Issues: ...
```
Tên file: `vX.Y.Z.md` (khớp đúng số phiên bản `.skill`/SKILL.md tương ứng).

### 05-Known-Issues/ — Lỗi đã biết, CHƯA sửa ngay
Không phải bug nào cũng sửa ngay — ghi lại để không quên, không lặp lại công sức phát hiện.
```
KI-007
DOCX nhiều section.
Status: Known
Priority: Medium
Workaround: ...
```
Có thể gộp theo chủ đề (`False-Positive.md`, `False-Negative.md`, `Pending.md`) hoặc tách file riêng `KI-YYYYMMDD-NNN.md` tùy số lượng — ưu tiên gộp khi còn ít mục.

### 06-Decision-Log/ — QUAN TRỌNG NHẤT
Mỗi quyết định kiến trúc đều phải ghi — để không còn câu hỏi "tại sao lúc đó lại sửa như vậy":
```
DL-20260830-001
Quyết định: Không merge Prompt v3 vào v2.
Lý do: ...
Ảnh hưởng: ...
Người phê duyệt: ...
```
Tên file: `DL-YYYYMMDD-NNN.md`.

**Bắt buộc ghi Decision Log khi**: đổi kiến trúc thư mục · quyết định KHÔNG áp dụng 1 đề xuất (từ chối cũng là quyết định, phải ghi lý do) · chọn giữa ≥2 phương án kỹ thuật tương đương · thay đổi ảnh hưởng ≥2 hệ trong KTC-DIS.

---

## 3. LUỒNG XỬ LÝ CHUẨN (END-TO-END)

```
Phát hiện (lỗi/prompt tốt hơn/quy tắc pháp lý/kỹ thuật/false positive)
        │
        ▼
01-Lessons-Learned/  (ghi ngay, không cần chờ quyết định)
        │
        ▼ (nếu có đề xuất thay đổi cụ thể)
03-Change-Proposals/  ──── kèm test case tại 02-Regression/Cases/
        │
        ▼ (chạy Regression, ghi kết quả vào Regression-Report.md)
        │
        ├── PASS + được duyệt ──► 06-Decision-Log/ (ghi quyết định APPLY)
        │         │
        │         ▼
        │   Áp dụng vào references/ (Prompt/Checklist/Skill thật)
        │         │
        │         ▼
        │   04-Release-Notes/ (ghi vào bản phát hành tương ứng)
        │         │
        │         ▼
        │   09-Quan-Tri-He/Nhat-Ky-Cap-Nhat...md (ghi lịch sử chính thức)
        │
        └── KHÔNG duyệt / hoãn ──► 06-Decision-Log/ (ghi quyết định REJECT/DEFER, kèm lý do)
                  │
                  ▼ (nếu là lỗi thật nhưng chưa sửa ngay)
            05-Known-Issues/ (ghi để không quên)
```

---

## 4. QUY TẮC ĐẶT TÊN FILE — TÓM TẮT

| Loại | Định dạng | Ví dụ |
|---|---|---|
| Lessons Learned | `LL-YYYYMMDD-NNN.md` | `LL-20260830-001.md` |
| Change Proposal | `CP-YYYYMMDD-NNN.md` | `CP-20260830-015.md` |
| Known Issue | `KI-YYYYMMDD-NNN.md` hoặc gộp theo chủ đề | `KI-007` (trong file gộp) |
| Decision Log | `DL-YYYYMMDD-NNN.md` | `DL-20260830-001.md` |
| Release Notes | `vX.Y.Z.md` | `v2.18.3.md` |
| Regression Case | Đặt tên tự do trong `Cases/`, đánh số "Case NNN" trong nội dung | `Case-031-QuyetDinh.md` |

**NNN** = số thứ tự 3 chữ số, đếm riêng theo từng ngày trong từng thư mục (không đếm chung toàn hệ thống).

---

## 5. GHI CHÚ LỊCH SỬ CẤU TRÚC

- **30/8/2026 (khởi tạo)**: 3 thư mục — `01-Lessons-Learned/`, `02-Regression/` (phẳng), `03-Change-Proposals/`.
- **30/8/2026 (mở rộng, cùng ngày)**: thêm `04-Release-Notes/`, `05-Known-Issues/`, `06-Decision-Log/`; tái cấu trúc `02-Regression/` thành `Cases/`/`Fixtures/`/`Expected-Results/`; đổi tên 3 Change Proposal đầu tiên từ dạng mô tả (`CP-20260826-gioi-han-transcribe-base64.md`) sang dạng số thứ tự chuẩn (`CP-20260826-001.md`) để nhất quán quy ước đặt tên.
