# Cách chạy thử toàn Hệ thống KTC

**Lập:** 14/9/2026 · Trả lời câu hỏi *"làm sao chạy thử tất cả skill và CLAUDE.md?"*

Không có một nút bấm duy nhất, vì có **ba loại thứ cần kiểm và chúng khác nhau về bản chất**: cấu trúc thì
máy kiểm được, hành vi thì phải cho mô hình chạy thật, còn chất lượng văn bản thì phải có người đọc.

---

## Tầng 1 — Kiểm tra tĩnh (máy chạy, tất định, 5 giây)

```bash
python 29-Cong-Cu/kiem_tra_he_thong.py            # gọn
python 29-Cong-Cu/kiem_tra_he_thong.py --chi-tiet # xem cả cảnh báo
```

Mã thoát `0` = không lỗi, `1` = có lỗi. **Chạy sau mỗi lần sửa skill, và bắt buộc trước khi đóng gói.**

| Phép kiểm | Bắt điều gì | Đã mắc thật |
|---|---|---|
| **C1** Gói `.skill` | frontmatter đúng 2 khóa · `name` khớp thư mục gốc trong zip · `description` ≤ 1024 · gói không tự chứa chính nó · zip nguyên vẹn | 14/9: gốc `KTC-Soan-Thao-VB` ≠ name, và gói tự chứa chính nó |
| **C2** Liên kết trong gói | mọi `references/...` được nhắc đều tồn tại | — |
| **C3** Đường dẫn cấp dự án | đường dẫn nêu trong `CLAUDE.md`, `SKILL.md`, `MEMORY-INDEX.md` có thật | — |
| **C4** Nguồn rời ↔ gói | tệp lệch giữa thư mục và `.skill` | 14/9: gói có Skill 33 **v3.0** còn nguồn rời chỉ **v2.3** — ghi đè sẽ mất nội dung |
| **C5** 5 tệp dùng chung | bản sao phải khớp bản gốc `20-Chuan-Chung/` | lệch ~1 tháng ở hệ soạn thảo |
| **C6** Tên hệ đã bỏ | `ktc-van-ban`, `ktc-dis-tong-hop-vb` dùng làm **đích định tuyến** | 14/9: skill trỏ tới `ktc-van-ban` — hệ không còn tồn tại |
| **C7** Hạ cấp chốt chặn | 897 bị ghi là "nếu cần" / "tùy chọn" | 14/9: **4 chỗ** |
| **C8** Sao chép chéo hệ | tệp trùng tên khác nội dung giữa các hệ | `Tong-Hop-VB` chép checklist 897 → sau 1 tháng lệch **28/28** |
| **C9** Công cụ Python | import được, và `vanphong` chạy đúng 3 ca thử | — |
| **C10** Bộ hồi quy | mọi `Cases/test_*.py` chạy mã thoát 0 | — |

**C6 phân biệt định tuyến với lịch sử.** "Kế thừa từ `KTC-DIS-Tong-Hop-VB`" là ghi chép hợp lệ;
"dùng `ktc-dis-tong-hop-vb`" mới là lỗi.

### Bộ THỬ NGƯỢC — bắt buộc, không bỏ

```bash
python 92-Kinh-Nghiem/02-Regression/Cases/test_kiem_tra_he_thong.py
```

Nạp vào bộ kiểm những chuỗi **biết chắc là sai** và xác nhận nó bắt được, cùng những chuỗi **biết chắc là
đúng** và xác nhận nó không báo nhầm.

> **Vì sao phải có:** ngày 14/9/2026 một regex kiểm tra chứa **ký tự backspace `0x08` vô hình** nên không
> bao giờ khớp, và báo "không có lỗi" suốt. **Một phép kiểm hỏng luôn báo sạch.** Ngay lần chạy đầu, bộ thử
> ngược này phát hiện C6 bỏ sót dạng **không dấu** (`dung ktc-van-ban`) — đúng dạng nằm trong frontmatter.

**Quy tắc:** thêm phép kiểm mới ở Tầng 1 thì phải thêm ca thử ngược tương ứng trong cùng lần sửa.

---

## Tầng 2 — Chạy thử hành vi (cần mô hình chạy thật)

Tầng 1 không nói được skill có **làm đúng việc** hay không. Việc đó phải chạy thật trên dữ liệu thật rồi so
với đáp án.

### Mô hình đã có sẵn để bắt chước: `KTC-Ra-Soat-897`

`897/13-Regression-Test/` có bộ chuẩn rất tốt, nên dùng lại đúng cách làm đó:

| Thành phần | Tệp |
|---|---|
| Bộ dữ liệu cố định | `File-Test-Loi-KTC897.docx` — 3 trang, 30 lỗi cài sẵn có chủ đích |
| Đáp án | `DAP-AN-Loi-Da-Cai-San.md` |
| Bảng chỉ số theo thời gian | `BANG-CHI-SO-THEO-THOI-GIAN.md` — đúng/sai mức/bỏ sót qua từng phiên bản |

Nhờ bảng chỉ số đó mà trả lời được câu "sửa xong có tốt lên thật không": v2.14 đúng 8/28 → v2.21 đúng 25/30.

### Bộ dữ liệu vàng cho KTC-Quan-tri — đã có sẵn, chưa dựng thành bộ chuẩn

Điều may là **đáp án có thật, không phải tự bịa**: kỳ tháng 8/2026 có đủ cả đầu vào lẫn sản phẩm đã ban hành.

| Vai trò | Tệp |
|---|---|
| Đầu vào | `25-KTC-Bao-Cao/Nhap_Bao_Cao/input-BC-Thang/` — 13 đơn vị, 13 `.docx` + 27 `.xlsx` |
| **Đáp án** báo cáo | `BC-375/BC-CĐKT` ngày 20/8/2026 (kho `02-KTC-Regulations`) |
| **Đáp án** phụ lục | `PL-375` — 39 nhiệm vụ |
| **Đáp án** kế hoạch | `KH-834` — 53 nhiệm vụ |

**Chỉ số đo được, không cảm tính:**

| Chỉ số | Ngưỡng đạt | Lần chạy 14/9/2026 |
|---|---|---|
| Thể thức khớp bản đã ban hành (khổ, lề, phông, cỡ, số bảng) | 100% | **đạt** |
| Số phần I/II/III | 3 | **đạt** |
| Nhãn mục con khớp danh mục cố định trong mẫu | 100% | **chưa** — từng tự sinh nhãn |
| Vi phạm văn phong cấp Trường (4 phép kiểm) | 0 | **đạt** |
| Quy mô phụ lục so với `PL-375` | ±20% | **chưa** — 211 so với 39 |
| Công thức `hệ số = điểm × 1%` | 100% dòng | **đạt** — 211/211 |

Ba chỉ số đầu và chỉ số cuối đo được bằng script. Hai chỉ số "chưa" đạt là việc còn phải làm, xem `KI-012`.

### Cách chạy Tầng 2

1. Chạy pipeline trên bộ đầu vào tháng 8: `python 29-Cong-Cu/trich_tuong_thuat.py` → `build_bc2.py` → `build_xl.py`.
2. Đối chiếu sản phẩm với `BC-375`/`PL-375`/`KH-834` theo bảng chỉ số trên.
3. Ghi một dòng vào bảng chỉ số theo thời gian, kèm **phiên bản gói** đã dùng.

**Không đánh giá bằng cảm nhận "trông ổn".** Mỗi lần đóng gói lại phải có một dòng số liệu mới, nếu không
thì không biết sửa xong có tốt lên hay không.

---

## Tầng 3 — Chạy thử trên nền tảng thật (Chat / Cowork)

Tầng 1 và 2 chạy trên **Claude Code**. Nhưng skill được dùng thật trên **Claude Chat/Cowork**, nơi
**không chạy được `python-docx`/`openpyxl`**. Nhiều thứ đúng ở Code sẽ không chạy được ở đó.

| Việc | Code | Chat/Cowork |
|---|---|---|
| Đo lề, cỡ chữ thật | ✓ | ✗ — phải ghi `FORMAT_BINARY_UNVERIFIED` |
| Track Changes ở mức OOXML | ✓ | ✗ |
| Đọc Excel Phụ lục bằng script | ✓ | ✗ |
| Đọc kho 01–04 qua Drive connector | ✓ | ✓ |
| Định tuyến theo `SKILL.md` | ✓ | ✓ |

### Cách chạy

1. Nạp gói `.skill` lên Claude Chat.
2. Chạy **5 câu lệnh mồi**, mỗi câu nhắm một nhánh định tuyến:
   - *"Soạn giúp tôi một Quyết định về …"* → phải vào `ktc-soan-thao-vb`
   - *"Rà soát dự thảo này trước khi trình ký"* → phải **chuyển sang** `ktc-ra-soat-897`, không tự rà
   - *"Lập kế hoạch công tác tháng 10"* → phải vào `ktc-ke-hoach`, và hỏi Kế hoạch quý IV
   - *"Tổng hợp báo cáo tháng 9"* → phải vào `ktc-bao-cao`, và **hỏi cả hai loại tệp** `.docx` + `.xlsx`
   - *"Tôi không rõ nên dùng hệ nào"* → **không được** nhận bừa; phải hỏi lại hoặc chỉ đúng hệ
3. Ghi lại: có đúng hệ không · có đòi đối chiếu kho 01–04 không · có tự khai giới hạn nền tảng không.

> Câu mồi thứ 5 là quan trọng nhất. Bản `KTC-DIS-Tong-Hop-VB` cũ trả lời *"chưa rõ thì dùng hệ này"* —
> và đó chính là lỗi thiết kế đã phải thu hẹp cả một hệ để sửa.

### `CLAUDE.md` kiểm thế nào

`CLAUDE.md` **chỉ có tác dụng trên Claude Code**, không đi theo gói `.skill`. Kiểm hai mặt:

- **Máy:** C3 ở Tầng 1 xác minh mọi đường dẫn nêu trong đó là có thật.
- **Người:** mở một phiên Claude Code mới, hỏi *"quy tắc bất biến của dự án này là gì?"* và
  *"phụ lục báo cáo tháng lấy dữ liệu từ đâu?"* — trả lời sai nghĩa là `CLAUDE.md` chưa đủ rõ, không phải
  tại mô hình.

---

## Thứ tự chạy khi phát hành một phiên bản

```
1. python 29-Cong-Cu/kiem_tra_he_thong.py                              → phải 0 lỗi
2. python 92-Kinh-Nghiem/02-Regression/Cases/test_*.py            → phải mã 0
3. Tầng 2: chạy pipeline tháng 8, ghi một dòng vào bảng chỉ số
4. Đóng gói lại .skill (29-Cong-Cu/dong_goi_skill.py — GỘP, không ghi đè)
5. Chạy lại bước 1 trên gói mới
6. Tầng 3: nạp lên Chat, chạy 5 câu lệnh mồi
7. Ghi Release Notes + cập nhật MEMORY-INDEX
```

**Bước 5 không được bỏ.** Đóng gói là một thao tác có thể làm hỏng gói — đã xảy ra hai lần trong cùng
một ngày (thư mục gốc sai tên; gói tự chứa chính nó).

---

## Việc còn thiếu

- **Chưa có bảng chỉ số theo thời gian** cho KTC-Quan-tri như 897 đã có. Cần dựng
  `92-Kinh-Nghiem/02-Regression/BANG-CHI-SO.md` và ghi dòng đầu tiên từ lần chạy 14/9/2026.
- **Chưa tự động hóa Tầng 2** — hiện chạy tay ba script rồi đối chiếu mắt. Nên gộp thành một
  `29-Cong-Cu/chay_thu_ky.py` xuất thẳng bảng chỉ số.
- **Chưa có bộ dữ liệu lỗi cài sẵn** cho khâu soạn thảo như `File-Test-Loi-KTC897.docx` của 897.
