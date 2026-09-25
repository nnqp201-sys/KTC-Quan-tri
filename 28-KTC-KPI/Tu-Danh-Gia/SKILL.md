---
name: ktc-kpi-tu-danh-gia
description: "Tự đánh giá, chấm điểm và đề xuất mức xếp loại chất lượng CÁ NHÂN theo quý của viên chức, người lao động Trường Cao đẳng Kon Tum theo QĐ 1923/QĐ-CĐKT (Quy chế đánh giá gắn KPI), điền Bản tự đánh giá, xếp loại cá nhân quý (sheet Đánh giá của mẫu Kế hoạch + KPI theo 6 nhóm vị trí). Từ kế hoạch KPI đã duyệt: sinh bảng hỏi Excel (điểm 3 nhóm tiêu chí chung, số lượng, chất lượng, tiến độ thực tế từng chỉ tiêu, điều kiện kèm theo, trường hợp đặc thù), tính điểm A 30 + B 70 có chặn trần 100% từng chỉ tiêu, đối chiếu ngưỡng 90/70/50 và điều kiện Điều 19. Dùng khi người dùng nói 'tự đánh giá KPI quý', 'chấm điểm KPI của tôi', 'quý này tôi xếp loại mức nào', 'tôi có được Hoàn thành xuất sắc không', 'điền Bản tự đánh giá'. Chỉ ra ĐỀ XUẤT của cá nhân, không quyết định thay Trưởng đơn vị, Hiệu trưởng. KHÔNG lập kế hoạch KPI đầu quý (dùng kpi-lap-ke-hoach); KHÔNG xếp loại tập thể, tổng hợp xếp loại cả đơn vị, trần tỷ lệ HTXS; KHÔNG tính % KPI theo Trục trong báo cáo tháng/quý của đơn vị (dùng bao-cao)."
---

# KTC-KPI — Tự đánh giá, đề xuất xếp loại cá nhân theo quý

## Phiên bản: v1.1 — 25/9/2026

> v1.1 (25/9/2026, lệnh sửa trình bày): đo lại chiều cao dòng sheet KPI sau khi ghi số thực tế (sản phẩm
> thực tế, minh chứng); tệp ra đang mở trong Excel → báo rõ, không lộ lỗi kỹ thuật. Không đổi số nào.
> v1.0: giai đoạn 2 theo lệnh 25/9/2026. Lập kế hoạch KPI: skill `kpi-lap-ke-hoach`. Tổng hợp xếp loại cấp đơn vị,
> trần tỷ lệ HTXS: giai đoạn 3 (chưa có skill).

## 1. Mục đích

Giúp viên chức, người lao động (hoặc Trưởng đơn vị làm cùng người trong đơn vị) **tự đánh giá quý** trên đúng mẫu
Bản tự đánh giá, xếp loại cá nhân: chấm 3 nhóm tiêu chí chung (30 điểm), tính kết quả KPI (70 điểm) từ số liệu
thực tế, đối chiếu ngưỡng điểm và điều kiện kèm theo, ghi **mức cá nhân tự đề xuất**.
Skill **không** chấm thay người dùng, **không** quyết định mức xếp loại — thẩm quyền của Hiệu trưởng trên cơ sở đánh giá
của Trưởng đơn vị và Phòng TCCB&CTHSSV [QĐ 1923, Đ14.3c]. Kết quả quý không phải quyết định xếp loại [QĐ 1923, Đ19.3].

## 2. Phạm vi và ngoại lệ

| Làm | Không làm (chuyển đi đâu) |
|---|---|
| Tự đánh giá quý, 6 nhóm vị trí, từ kế hoạch KPI đã duyệt | Lập, sửa kế hoạch KPI đầu quý → `kpi-lap-ke-hoach` |
| Đề xuất của cá nhân theo ngưỡng điểm + bảng điều kiện | Xếp loại tập thể, tổng hợp cả đơn vị, trần tỷ lệ HTXS [Đ19.2] → giai đoạn 3 (chưa có skill; báo người dùng) |
| Cảnh báo người đứng đầu cao hơn tập thể (khi đã có kết quả tập thể) | % KPI theo Trục trong báo cáo tháng/quý của đơn vị → `bao-cao` |

**Đọc trước khi làm:** `references/Skill-Library/19-Quy-Tac-KPI.md` mục D–F (có dẫn Điều) · `references/Cau-Hoi-Mo.md`
(#8–#13 thuộc giai đoạn này) · `references/Known-Issues-Bieu-Mau.md` (#7, #12).

## 3. Đầu vào

Theo thứ tự: tệp đính kèm trong phiên → thư mục dự án → hỏi người dùng.

1. **Tệp kế hoạch KPI quý đã duyệt** (.xlsx, 1 trong 6 mẫu Kế hoạch + KPI; tệp do `kpi-lap-ke-hoach` xuất hoặc tệp đơn vị
   tự điền). Không có → hỏi; **không dựng lại kế hoạch từ trí nhớ**.
2. **Nhóm vị trí** — công cụ tự nhận từ tiêu đề sheet Đánh giá; không nhận được thì hỏi (6 nhóm như `kpi-lap-ke-hoach`).
3. **Quý, năm** → `references/quy/<YYYY>-Q<n>.yaml`: in hạn nộp hồ sơ tự đánh giá [QĐ 1923, Đ15.3b].
4. **Bảng hỏi đã điền** (bước 2 dưới đây) — mọi số liệu chấm đều từ đây.

## 4. Lưu ý bảo mật

- Điểm chi tiết, nhận xét, minh chứng chỉ cho người có thẩm quyền, người được đánh giá và người liên quan theo chức
  năng [QĐ 1923, Đ23.2]. Dữ liệu này nhạy cảm hơn kế hoạch (điểm phẩm chất chính trị, đạo đức).
- Trong dự án: lưu tại `30-Ket-Qua/<YYYY-MM-DD>/KPI-ca-nhan/` (đã loại khỏi git, có ca thử). Trên Claude.ai/Cowork: giao
  tệp trực tiếp, không đưa điểm của người khác vào ví dụ. Trong Claude Code: nhắc người dùng gõ `#riêng` ở đầu tin nhắn
  khi dán điểm, nhận xét.

## 5. Quy trình

1. **Đọc kế hoạch, dò cấu trúc.** Công cụ dò động sheet Đánh giá của cả 6 mẫu (các mẫu lệch dòng, lệch cột). Dò không
   được một khối (mục A, 6 Trục, khối II, dòng III) → **dừng, báo**, không đoán cấu trúc.
2. **Sinh bảng hỏi** — một tệp Excel, ô vàng để điền, danh sách chọn sẵn; không hỏi rời từng câu trong hội thoại:
   ```
   python scripts/kpi_danh_gia.py sinh-bang-hoi --ke-hoach <KH.xlsx> --quy IV --nam 2026 --ra <Bang-hoi.xlsx>
   ```
   - Sheet A: điểm tự chấm từng tiêu chí con (≤ điểm tối đa); mức nhóm tùy chọn [Đ10.5 — mức xét theo tổng nhóm].
   - Sheet B: mỗi chỉ tiêu — sản phẩm, số lượng thực tế, % chất lượng, % tiến độ, kết quả nhiệm vụ (vượt mức / đúng hạn /
     chậm tiến độ / không hoàn thành), nhiệm vụ trọng tâm theo Đ18, minh chứng. Số thực tế đã có trong tệp thì điền sẵn.
   - Sheet C: trường hợp đặc thù [Đ21.4, Đ21.6]; căn cứ Không hoàn thành [Đ19.1d]; khắc phục hạn chế kỳ trước; với viên
     chức quản lý: kết quả đơn vị, phiếu tín nhiệm, người đứng đầu + xếp loại tập thể [Đ14.4, Đ19.4]; điều kiện khối II của
     mẫu (bảng kiểm sĩ số, giờ giảng, NCKH…); quý trước dưới mức tối thiểu [Đ19.1a, Đ19.5]; **mức tự đề xuất**.
3. **Người dùng điền bảng hỏi.** Không điền thay. Người dùng hỏi "chấm giúp mục A" → giải thích khung mức Đ10.5, để
   người dùng tự chọn điểm.
4. **Đánh giá, xuất tệp:**
   ```
   python scripts/kpi_danh_gia.py danh-gia --ke-hoach <KH.xlsx> --bang-hoi <Bang-hoi.xlsx> --quy IV --nam 2026 \
          --ra 30-Ket-Qua/<ngày>/KPI-ca-nhan/TDG-KPI-Q<n>-<năm>_<ho-ten-khong-dau>.xlsx
   ```
   Mã thoát **2** = bảng hỏi thiếu/sai hoặc thuộc trường hợp đặc thù → đọc thông báo, hỏi người dùng, **không tự chấm**.
   **1** = đã xuất, còn điều kiện "Không đạt" hoặc cảnh báo cần trình bày. **0** = sạch.
   Công cụ tính: mục A theo điểm người dùng; mục B = % hoàn thành × điểm tối đa Trục, **chặn trần 100% từng chỉ tiêu**
   [Đ11.6] (mẫu không chặn — Known-Issues #7; tệp ra thay công thức % Trục bằng công thức có chặn); tổng A + B; mức theo
   ngưỡng 90/70/50 [Đ19.1] trên giá trị chính xác, hiển thị cắt 2 chữ số (không làm tròn lên). **Không tự nhẩm điểm.**
5. **Trình bày** theo mục 6. Điều kiện "Thiếu dữ liệu" → người dùng tự xác nhận; không tự cho "Đạt".
6. **Thể thức:** có `kiem_the_thuc.py` thì đo tệp ra (phông đã chuẩn hóa Times New Roman).

## 6. Định dạng đầu ra

1. **Tệp Excel** `TDG-KPI-Q<n>-<năm>_<họ-tên-không-dấu>.xlsx` — bản sao tệp kế hoạch: sheet KPI có số thực tế, sheet Đánh
   giá có điểm mục A, điều kiện khối II, mục III (mức cá nhân tự đề xuất). Mục IV (Lãnh đạo đơn vị) để trống.
2. **Bảng tóm tắt**: điểm A từng nhóm (kèm mức Đ10.5), điểm từng Trục (kèm %), tổng A + B, mức theo ngưỡng điểm thuần
   túy, mức cá nhân tự đề xuất.
3. **Bảng điều kiện** của mức theo điểm và các mức thấp hơn: Đạt / Không đạt / Thiếu dữ liệu / Không áp dụng, kèm Điều.
   Trường hợp "Không hoàn thành dù đủ điểm" [Đ19.1d] nêu riêng.
4. **Ghi chú căn cứ**: nguồn còn thiếu (bảng kiểm sĩ số, hướng dẫn hằng quý/năm, tiêu chí chuyển đổi số — Câu hỏi mở
   #13). Nhóm `bo-mon`, `giao-vu`, `hanh-chinh`, `ho-tro`: "Đối chiếu qua mẫu Kế hoạch+KPI Quý III/2026, chưa đối chiếu
   trực tiếp QĐ 2078 (Phụ lục XXIV/XXVI/XXVII/XXVIII chưa có trong kho)".
5. Dòng cuối bắt buộc: *"Đề xuất của cá nhân — chưa phải kết luận của Trưởng đơn vị và Hiệu trưởng [QĐ 1923, Đ14.3c].
   Trần tỷ lệ Hoàn thành xuất sắc theo nhóm tương đồng chưa được đối chiếu ở bước này [Đ19.2]."*

## 7. Checklist chất lượng

- [ ] Mọi điểm, % do người dùng khai trong bảng hỏi; không có số nào mô hình tự chấm.
- [ ] Mã thoát 2 đã hỏi lại người dùng, không bỏ qua.
- [ ] Chặn trần 100% từng chỉ tiêu; chênh lệch với công thức gốc của mẫu đã nêu.
- [ ] Điều kiện thiếu nguồn ghi "Thiếu dữ liệu", không ghi "Đạt".
- [ ] Không kết luận mức xếp loại; có dòng cuối bắt buộc; nhắc trần tỷ lệ HTXS thuộc giai đoạn 3.
- [ ] Hai điều khoản chưa nhất quán (Đ19.1a lưu ý / Đ19.5 — Câu hỏi mở #8) nêu cả hai khi gặp, không chọn.
- [ ] Tệp lưu đúng thư mục `KPI-ca-nhan/`; không ghi đè kế hoạch đã duyệt, không ghi vào `assets/`.

## 8. Ví dụ

**Người dùng:** "Chấm điểm KPI quý III của tôi." (kèm tệp kế hoạch quý III)
**Làm:** chạy `sinh-bang-hoi`, giao bảng hỏi, giải thích ba sheet; người dùng gửi lại → `danh-gia` → trả tệp, bảng tóm tắt,
bảng điều kiện, dòng cuối bắt buộc.

**Người dùng:** "Tôi có được Hoàn thành xuất sắc không?"
**Làm:** không trả lời "có/không". Nếu đã có kết quả `danh-gia`: nêu tổng điểm so với ngưỡng 90, điều kiện HTXS nào Đạt /
Không đạt / Thiếu dữ liệu, và nhắc trần 20% theo nhóm tương đồng [Đ19.2] tính ở cấp Trường (giai đoạn 3). Chưa có →
làm bước 2.

**Người dùng:** "Xếp loại tập thể Phòng tôi thế nào?" → Ngoài phạm vi: xếp loại tập thể, tổng hợp cả đơn vị là giai đoạn 3
(PL II CV 694), chưa có skill.
