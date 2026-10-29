# LỆNH CẬP NHẬT HỆ KTC-RA-SOAT-897 — v2.22 (ghi đè) · 09/9/2026

> **Cách dùng**: Chủ Team mở một phiên chat mới trong Project *KTC-Ra-soat-897-v2 (dùng chung)*,
> copy toàn bộ phần trong khung "LỆNH DÁN VÀO PHIÊN CHAT" bên dưới và dán vào.
> Phần còn lại của tệp này là hồ sơ lưu, không cần dán.

---

## LỆNH DÁN VÀO PHIÊN CHAT

```
Kích hoạt Skill ktc-ra-soat-897. Đây là phiên KIỂM TRA SAU CẬP NHẬT v2.22 (bản ghi đè 09/9/2026),
không phải phiên rà soát văn bản. Làm đúng 5 việc sau, theo thứ tự, không bỏ bước:

1. Đọc 09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md (mục 9 và mục 10), rồi đọc SKILL.md.
   Báo lại: SKILL.md bao nhiêu byte, có bao nhiêu quy tắc vận hành, có mục "Tra cứu Internet" không.

2. Xác nhận 4 điểm đã vào SKILL.md — trả lời CÓ/KHÔNG cho từng điểm, trích đúng câu làm bằng chứng:
   a) Nguyên tắc 1 có ghi "ĐỌC NỘI DUNG từng văn bản viện dẫn" và "xác nhận kết nối KHÔNG tính
      là đã đối chiếu" không?
   b) Có quy tắc vận hành #21 về nhân quả giả không?
   c) Mục "Tra cứu Internet" có đặt https://phapluat.gov.vn/ là nguồn tra TRƯỚC TIÊN không?
   d) Bảng thể thức có ghi bảng Phần II là 10/44/97/53/29/19 mm = 252mm không?
      (Nếu còn thấy 45/100/55/30/20 = 260mm thì gói CHƯA được nạp lại — dừng và báo ngay.)

3. Tự kiểm tra danh mục công cụ khả dụng THẬT của phiên này (tìm công cụ với từ khóa
   "web search browser internet"), rồi ghi cụ thể kết quả. KHÔNG ghi chung chung
   "phiên không có công cụ tra cứu web" nếu chưa thực sự kiểm tra.

4. Nhắc lại bằng lời của bạn: khi thiếu công cụ tra cứu web thì kênh nào vẫn PHẢI làm đầy đủ,
   kênh nào được phép ghi "Chưa xác minh"? Vì sao hai kênh này độc lập với nhau?

5. Đọc references/Checklist/03-Phap-Ly.md, cho biết bảng xác minh hiệu lực (mục 6) hiện có
   bao nhiêu trạng thái và liệt kê đủ.

Sau 5 việc trên, KHÔNG xuất file .docx (đây là phiên kiểm tra, không phải ca rà soát chính thức).
Chỉ trả lời trong chat. Nếu bất kỳ điểm nào ở việc 2 trả lời KHÔNG, dừng lại và báo rõ điểm đó.
```

---

## Hồ sơ lưu — những gì đã thay đổi trong đợt 09/9/2026

Bản ghi đè, **KHÔNG tăng số phiên bản**, theo quyết định của Phòng TH-HC&QT.

### A. Dọn gói và tối ưu cấu trúc
| # | Thay đổi |
|---|---|
| 1 | Xóa 2 assets thừa: bản trùng MD5 tuyệt đối `786cdb34783ddc34b3d0ceb5bb12146a`, và bản `.docx` trung gian mà chính SKILL.md đã tuyên bố không phải chuẩn áp dụng |
| 2 | Thêm 3 chỉ mục Prompt-Library — 14 tệp prompt con trước đó là tệp mồ côi, không tệp nào trỏ đích danh |
| 3 | Tách phần kể lịch sử sự cố khỏi SKILL.md sang tệp mới `references/Quan-Tri-He/Ghi-Chu-Ky-Thuat.md` |
| 4 | Vá 5 đường dẫn tham chiếu sai (Skill-Library 14/15/18 trỏ `08-Checklist/` từ thời còn trong KTC-Database; 06-Metadata thiếu `../`; 03-Chuan-Hoa/README thiếu một cấp) → **0 tham chiếu gãy** |
| 5 | Gỡ 3 tham chiếu treo trỏ vào tệp không còn tồn tại |

### B. Thay đổi hành vi — cần đọc kỹ
| # | Thay đổi | Vì sao |
|---|---|---|
| 6 | **Tách Nguyên tắc 1 thành 2 lớp**: thiếu **kho 01-04** → dừng và hỏi; thiếu **bộ nhớ vận hành** → chạy tiếp, ghi cảnh báo Phần I | Bộ nhớ vận hành là lớp 4–5, không phải căn cứ pháp lý. Gộp chung khiến trục trặc lớp 5 chặn cả ca rà soát |
| 7 | **Nguyên tắc 1 viết lại chặt**: "ĐỌC NỘI DUNG từng văn bản viện dẫn"; xác nhận kết nối **không tính** là đã đối chiếu; chỉ 2 trạng thái hợp lệ, trạng thái thứ ba "đã kết nối nhưng không tra" là lỗi | Từ "đối chiếu" cũ đủ lỏng để hiểu thành "đã ngó qua" — đã gây lỗi thật |
| 8 | **Quy tắc #18** — luôn xuất báo cáo 8 phần ngay khi phân tích xong, không hỏi lại | Hệ quả trực tiếp của Nguyên tắc 2, không phải bước tùy chọn |
| 9 | **Quy tắc #19** — trước khi ghi "chưa xác minh", phải tự kiểm tra công cụ khả dụng thật và ghi cụ thể kết quả | |
| 10 | **Quy tắc #20** — giới hạn tải tệp nhị phân lớn qua base64, kèm cách xử lý | |
| 11 | **Quy tắc #21 — chống nhân quả giả**: cấm mượn giới hạn của kênh này để bỏ việc của kênh khác. 3 kênh độc lập: kho 01-04 (Drive, không cần web) · bộ nhớ vận hành (Drive, không cần web) · xác minh hiệu lực bên ngoài (cần web) | Phát hiện qua chạy thử thật của Chủ Team — xem mục C |
| 12 | **`https://phapluat.gov.vn/` thành nguồn tra cứu ưu tiên số 1**, trước `vbpl.vn` và Công báo. Thư viện pháp luật chỉ dùng tìm manh mối, không dùng kết luận | Theo yêu cầu Phòng TH-HC&QT |
| 13 | Bảng xác minh hiệu lực (Checklist 03 mục 6) bổ sung 2 trạng thái còn thiếu: **Hết hiệu lực một phần** và **Chưa có hiệu lực** | Nghị định bị sửa đổi một số điều mà đánh "Còn" hoặc "Hết" đều sai |
| 14 | Đính chính spec tự mâu thuẫn: bảng Phần II ghi 10/45/100/55/30/20 mm = **260mm = 26,0cm**, tự vượt chính ngưỡng 25,7cm ghi ngay phía trên → sửa thành **10/44/97/53/29/19 mm = 252mm** theo tệp mẫu thật đã trình ký | |

### C. Lỗi thật bắt được qua chạy thử (nguồn gốc quy tắc #21)

Báo cáo chạy thử ghi:

> *"Kho 01-04 (KTC-Database) — đã xác nhận kết nối, chưa tra cứu chi tiết từng văn bản viện dẫn cụ thể
> (số hiệu Luật, VBHN, Luật Doanh nghiệp...) do phiên không có công cụ tra cứu web"*

**Ba lỗi chồng nhau:**

1. **Nhân quả giả** — kho 01-04 nằm trên Google Drive, không cần công cụ web. Thiếu web không giải thích
   được việc không tra kho. Đây là lỗi **nguy hiểm hơn cả bỏ sót**, vì nó biến một thiếu sót sửa được
   thành "giới hạn kỹ thuật", khiến người đọc chấp nhận và không ai đi sửa. Đúng dạng lỗi mà
   `Ghi-Chu-Ky-Thuat.md` mục 2 đã cảnh báo với binary DOCX.
2. **Vi phạm Nguyên tắc 1** — "xác nhận kết nối" không phải "đối chiếu"; rơi vào trạng thái thứ ba mà
   quy tắc không cho phép: đã kết nối nhưng không tra, cũng không dừng hỏi.
3. **Vi phạm quy tắc #19** — ghi "phiên không có công cụ tra cứu web" như một khẳng định, không kèm
   bằng chứng đã tự kiểm tra.

**Cách viết đúng — tách bạch hai dòng, mỗi dòng một kênh:**

> *Kho 01-04: đã tra `01-Legal-Database` cho từng văn bản viện dẫn. Tìm thấy: [...]. Không có trong kho: [...].*
>
> *Xác minh hiệu lực bên ngoài: đã kiểm tra công cụ khả dụng của phiên — không có công cụ tra cứu web.
> Các văn bản không có trong kho ghi "Chưa xác minh" tại bảng Checklist 03 mục 6, đề nghị bộ phận
> pháp chế tra tại phapluat.gov.vn.*

### D. Sửa tệp mẫu — đóng KI-001

Đo lại bằng `python-docx`, ghi nhận cũ *"2 file mẫu gốc, 3/5 bảng vượt nhẹ 25,8-26cm"* **không đúng**:

| Tệp | Thực tế | Đã xử lý |
|---|---|---|
| `Mau_Bao_cao_ra_soat_KTC897_8phan.docx` | **Không phải lỗi vượt khổ** — `tblGrid` hỏng nặng: khai 10 cột cho bảng 6 cột, có width **âm** (−94,115cm), 3 `gridSpan` không hợp lệ (`7`/`0`/`0`). Word có thể **từ chối mở** | Dựng lại `tblGrid`, gỡ `gridSpan` sai |
| `assets/KTC-Ra-Soat-897_Template_Trong.docx` | 3/3 bảng vượt (25,743 · 25,993 · 25,743cm) | Co về 25,698cm |
| `assets/KTC-Ra-Soat-897_Template_Trong.dotx` (**bản chuẩn**) | Width đạt nên trước nay không ai để ý, nhưng cả 3 bảng `autofit=True`, **thiếu `tblLayout="fixed"`** — vi phạm ràng buộc 3 bước của chính SKILL.md | Thêm `fixed`, `autofit=False` |

Kết quả: **11/11 bảng** của 3 tệp đều ≤25,7cm · `tblLayout=fixed` · `autofit=False` · không còn width âm.

> **Ghi chú Track Changes**: quy tắc #8 buộc bật Track Changes khi sửa `.docx` đã có. Lần này
> **không áp dụng được** — sửa `tblGrid`/`gridSpan` là sửa cấu trúc lưới bảng, OOXML không có cơ chế
> track cho phần này và ép vào sẽ làm hỏng tệp. Dựa vào lịch sử phiên bản Google Drive thay thế.
> **Nội dung chữ không đổi một ký tự nào.**

### E. Việc còn mở đã đóng trong đợt này
- **#1** KI-001 khổ giấy bảng biểu — xong (mục D)
- **#6** Đồng bộ Nhật ký — xong, nay ở **v1.8**. Kèm đính chính: MEMORY-INDEX từng ghi sai nhật ký ở "v1.6, tồn đọng từ 30/8", tệp thật đã lên v1.7 từ 06/9
- **#7** Chạy hồi quy 30 lỗi — không còn là việc mở, bộ hồi quy **chạy tự động hằng ngày**
- **#11** Gấp 3 quy tắc từ MEMORY-INDEX vào SKILL.md — xong, thành #18/#19/#20

### F. Việc còn mở, CHƯA xử lý
| # | Việc | Ưu tiên |
|---|---|---|
| 2 | Chạy `validate.py` trên `12-Output/` diện rộng | Trung bình |
| 3 | Bù các bản ghi Process Memory còn thiếu (nợ kỹ thuật từ 23/8) | Trung bình |
| 9 | 2 bản `Pending.md` trùng tên khác nội dung trong `99-Kinh-Nghiem/05-Known-Issues/` | Chưa xử lý |
| 12 | Báo cáo VTVL lên `12-Output/` — Phòng TH-HC&QT đã quyết **không cần làm** | Đã bỏ |

### G. Giới hạn phải công bố
Phiên thực hiện đợt cập nhật này **không xác minh độc lập được** cổng `phapluat.gov.vn`:
`WebSearch` trả HTTP 403, `WebFetch` bị `robots.txt` chặn. Nguồn của khẳng định "cổng có giá trị
cao nhất" là **Phòng TH-HC&QT** — thông tin ở lớp bài học, **chưa thăng hạng** thành sự thật đã
kiểm chứng độc lập. Ghi nhận theo đúng quy tắc #19 và Quy tắc thăng hạng.

### H. Trạng thái đồng bộ sau đợt cập nhật
Tất cả khớp **v2.22**: `SKILL.md` (trong gói + bản rời trên Drive) · `Checklist/06-Metadata.md` ·
`CHANGELOG.md` · `MEMORY-INDEX.md` · `00-README.md` · Nhật ký **v1.8** · tên tệp `.skill`.

Project instructions trên Claude Team đã thay bằng **bản rút gọn ~3,4KB** thay vì sao chép lại
`SKILL.md`. Từ nay nâng cấp Skill **không cần sửa Project instructions**.

---
*Phòng Tổng hợp – Hành chính và Quản trị, Trường Cao đẳng Kon Tum · phongthhcqt@gmail.com*
*Đồng bộ theo `ktc-ra-soat-897-v2.22.skill` (218KB, 69 tệp) · 09/9/2026*
