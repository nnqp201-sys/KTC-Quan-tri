# PATCH-NOTES v3.2 — Ghép v3.1 + v2.5.1, sửa thêm 3 lỗi mới phát hiện khi ghép
## Ngày: 19/08/2026 | Phạm vi: `read_bc736_excel.py`, `fill_bc736.py`

## Bối cảnh
Anh Phục gửi độc lập file `ktc-bao-cao-v2_5_1.skill` (vá 9 lỗi ở `read_bc736_excel.py`
+ 5 lỗi ở `fill_bc736.py`, kèm PATCH-NOTES-v2.5.1.md và bộ test riêng). Trước khi tin
theo mô tả, Claude tự chạy kiểm chứng độc lập:

1. Chạy bộ test của v2.5.1 → 15/15 PASS trên chính code của họ.
2. Chạy fixture của họ bằng **code của mình (v3.1)** → phát hiện 2 claim ĐÚNG (BUG-01
   nhận diện KQ khi KPI ở hàng gộp; mở rộng của BUG-03 "Tổng cộng Trục N" có kèm số).
3. Phát hiện v2.5.1 vá trên nền **v2.3** (trước khi có fix Mục II và tách Phần I/III của
   v3.1) → **2 lỗi nghiêm trọng nhất đã "sống lại"**: lẫn nội dung Phần I/III, gán nhầm
   Mục II vào Trục cuối cùng của Mục I.

## Quyết định: GHÉP thay vì chọn 1 bên
Giữ nền code v2.5.1 (chất lượng cao hơn: `_replace_yellow_runs`, `_match_key` ưu tiên
khớp dài nhất, chuẩn hoá Unicode, quét cả bảng, kiểm cascade đầy đủ), cấy thêm 2 cơ chế
của v3.1 (Mục II, tách Phần I/III qua `content_by_phase`).

## 3 lỗi MỚI phát sinh trong quá trình ghép — chỉ lộ ra khi kiểm thử trên file THẬT

| # | Lỗi | Nguyên nhân | Cách phát hiện | Cách sửa |
|---|---|---|---|---|
| **GHÉP-01** | `id(p)` không ổn định giữa 2 lần duyệt `doc.paragraphs` | `python-docx` tạo `Paragraph` wrapper **mới** mỗi lần gọi property `doc.paragraphs`, kể cả `id(p._element)` cũng không đáng tin cậy nếu 2 lần gọi property tách rời | Test tách Phần I/III thất bại trên file mẫu thật (dù đúng trên file test đơn giản) | Bỏ hẳn cơ chế "pre-pass xây phase_map rồi tra cứu lại" — theo dõi Phần **ngay trong** vòng lặp chính, chỉ 1 lần duyệt duy nhất |
| **GHÉP-02** | `_replace_yellow_runs` chỉ xoá run bôi vàng, để sót phần chữ đỏ KHÔNG bôi vàng bao quanh | Trên file mẫu thật, cụm hướng dẫn màu đỏ thường DÀI HƠN phần bôi vàng (VD "[…lấy kết quả thực hiện" + "công tác tuyển sinh" (vàng) + "của phòng X]. {Lưu ý...}" — tất cả đỏ, chỉ 1 đoạn giữa được bôi vàng thêm) | So sánh output thực tế: câu hướng dẫn gốc còn nguyên trong báo cáo, chỉ có 1 cụm nhỏ được thay | Đổi hàm xoá **toàn bộ run đỏ** (không chỉ phần vàng), chỉ giữ nguyên run đen |
| **GHÉP-03** | Nối `black_prefix + last_heading` làm 2 số Nghị quyết cùng khớp được, chọn nhầm theo thứ tự dict | Cấu trúc mẫu thật KHÔNG đồng nhất: có Nghị quyết nhãn CÙNG đoạn placeholder (NQ59, 66, 72, 80), có Nghị quyết nhãn Ở ĐOẠN RIÊNG (NQ68, 70, 71, 79). Nối chung 2 nguồn khiến `last_heading` CŨ (còn sót từ NQ trước) và `black_prefix` MỚI cùng match, độ dài nhãn bằng nhau (2 chữ số) → `_match_key` chọn nhầm | Test đủ 8/8 Nghị quyết (test ban đầu chỉ thử 2/8 nên không lộ) → NQ79 bị ghi đè lên vị trí của NQ70 | Ưu tiên `black_prefix` nếu đủ nghĩa; CHỈ dùng `last_heading` khi `black_prefix` rỗng/vô nghĩa — không bao giờ nối cả 2 |

## Kết quả kiểm thử cuối — 30/30 PASS
- 11 test gốc `read_bc736_excel.py` của v2.5.1 (BUG-01 → BUG-08)
- 2 test Mục II của v3.1 trên file mẫu thật
- 4 test gốc `fill_bc736.py` của v2.5.1 (BUG-10 → BUG-13)
- 13 test MỚI: tách Phần I/III + đủ 8/8 Nghị quyết phân biệt đúng, trên file mẫu THẬT
  (không phải fixture mô phỏng)

Chạy lại bất cứ lúc nào: `python3 test_regression_v32.py`

## API thay đổi — LƯU Ý khi dùng
`fill_report()` đổi tham số `content_map` (dict phẳng) → `content_by_phase` (dict 3 khóa
con `PHAN_I` / `PHAN_II` / `PHAN_III`). Xem `README-fill_bc736.md` để biết cách dùng mới
và danh sách đầy đủ 45 vị trí thật (27 ở Phần I, 2 ở Phần II, 16 ở Phần III).

## Bài học rút ra
1. **Không tin claim (kể cả của chính mình) khi chưa tự chạy lại được** — 2/4 claim ban
   đầu về v3.0 hoá ra sai khi tự kiểm chứng, nhưng 2/4 khác lại đúng.
2. **Test trên fixture tự tạo không thay thế được test trên file thật** — cả 3 lỗi GHÉP
   01-03 đều KHÔNG lộ ra qua fixture đơn giản, chỉ lộ khi chạy trên file mẫu TB736 thật.
3. **Test đủ số lượng, không test mẫu nhỏ rồi suy rộng** — lỗi GHÉP-03 chỉ lộ khi test
   đủ 8/8 Nghị quyết; test 2/8 (dù chọn ngẫu nhiên) đã "may mắn" pass.
