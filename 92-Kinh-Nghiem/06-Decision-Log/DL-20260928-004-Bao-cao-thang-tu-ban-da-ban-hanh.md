# DL-20260928-004 — Báo cáo tháng cấp Trường dựng từ bản đã ban hành; mọi công cụ cần thiết nằm trong plugin (1.3.6)

**Ngày:** 28/9/2026 · **Người phụ trách:** "Phải sửa ngay lập tức" · "tất cả nội dung phải được chứa đựng trong Plugin để phát
huy tối đa yêu cầu".

## Sự việc
Người phụ trách chạy thử báo cáo tháng 9 trên tài khoản `phongthhcqt@gmail.com` (Claude Code và Cowork, plugin 1.3.5). Sản
phẩm (lưu tại `30-Ket-Qua/2026-09-21/Bao-cao-thang-9/`, tiền tố `Code.28.9.`, `Cowork. 28.9.2026.`) kém bản chạy 21/9:

| | 21/9 | Cowork 28/9 | Code 28/9 |
|---|---|---|---|
| Báo cáo Word | 6.069 chữ, đủ 7 mục tường thuật | 5.023 chữ, nhiều `[CẦN BỔ SUNG]`, "(Nguồn: …)" trong thân | 2.373 chữ, thẻ `[CẦN BỔ SUNG [PHAN_I]…]`, % thay tường thuật |
| Phụ lục | Mẫu PL-375, 47+9 nhiệm vụ, 300 công thức | 5 sheet tự đặt, 0 công thức, Calibri (Mức 2) | 2 sheet tổng hợp |
| Kế hoạch tháng 10 | Có | Không | Không |

Dữ liệu đầu vào như nhau.

## Nguyên nhân (đã kiểm chứng)
1. `SKILL.md` bao-cao bước 6: "Xuất .docx qua `fill_bc736.py`" (mẫu trắng); cách đúng (BƯỚC 0D — phát triển từ BC-375) chỉ
   nằm trong tham chiếu. Ngày 21/9 phiên chạy trong dự án đọc Skill 33 và dùng `build_bc2.py`, `build_xl.py`, `vanphong.py`,
   `trich_tuong_thuat.py` — **chỉ có trong `29-Cong-Cu/`, không có trong plugin**.
2. Mẫu trắng có sẵn lỗi: "nhiệm kỳ 2021-2026" (BC-375 đã ban hành: 2026-2031), "Báo cáo báo cáo", "tháng 7".
3. Quy tắc lõi 1.3.0 ("thiếu → THIEU_DU_LIEU") + QĐ-01 cũ ("tuyệt đối không suy diễn") bị hiểu thành "đầu mối chưa nộp thì bỏ
   trống", trong khi 21/9 tổng hợp từ báo cáo của các khoa có ghi nguồn. Bản Code còn loại cả 3 đơn vị vì vài dòng sai công
   thức KPI (tác tử kiểm hồ sơ kết luận "TRẢ LẠI ĐƠN VỊ").
4. Câu lệnh mẫu mục VI.2 Tài liệu hướng dẫn hướng vào kiểm lỗi, tính %, "chỉ đưa kết quả có nguồn và minh chứng", đầu ra
   không gồm kế hoạch tháng sau.
5. Rà rộng: `ktc_trackchanges.py` (Nguyên tắc 8) chỉ có trong kỹ năng soạn thảo, không ở tầng plugin.

## Quyết định
1. Quy trình chính báo cáo tháng cấp Trường: **4 sản phẩm** (Word, phụ lục KPI, kế hoạch tháng sau, ghi chú đối soát) **dựng
   từ bản đã ban hành** bằng công cụ chung `bc_thang.py` (tổng quát hóa từ cách làm 21/9, không ghi cứng kỳ, tên tệp,
   người). `fill_bc736.py` + mẫu trắng chỉ còn dự phòng. Tài liệu: `25-KTC-Bao-Cao/references/Skill-Library/37-…md`.
2. QĐ-08 (Memory bao-cao): tổng hợp từ nguồn khác có ghi nguồn không phải bịa; `[CẦN BỔ SUNG]` chỉ khi không có nguồn nào.
   Nguồn ghi ở tệp ghi chú đối soát, không chèn vào thân. Lỗi công thức dòng → bỏ số KPI dòng đó, giữ đơn vị.
3. **Mọi công cụ quy trình cần phải nằm trong plugin**: đóng thêm `bc_thang.py`, `vanphong.py`, `trich_tuong_thuat.py`,
   `ktc_trackchanges.py` vào `scripts/`; bản sao trong gói kỹ năng báo cáo (gói đơn lẻ tự đủ). Nguồn phụ trợ (Chương trình
   công tác năm, kế hoạch quý, kết luận giao ban) đọc từ kho KTC-Database — `bc_thang.py nguon` tự liệt kê.
4. Sửa 3 lỗi mẫu trắng (bản cũ lưu `99-Luu-Tru/Ban-nhap-bi-thay-the/`); tác tử kiểm hồ sơ ghi rõ trả lại ≠ loại khỏi báo cáo.
5. Câu lệnh mẫu VI.2 viết lại theo mục tiêu (4 sản phẩm, phát triển từ bản đã ban hành).

## Kiểm chứng
- `test_bc_thang.py` 28 ca (gồm ca ngược); dựng lại nội dung 21/9 bằng `bc_thang.py word`: trùng 100% chữ; 3 tệp đạt thể thức.
- Plugin 1.3.6, SHA-256 `1438c624…a64b`, commit `3987468`; hồi quy 23/23; validate --strict đạt; đã cài máy.
- Chạy độc lập như tài khoản thành viên (thư mục ngoài dự án, đã kết nối P-THHC, câu lệnh mẫu mới): xem mục "Kết quả chạy
  độc lập" dưới đây.

## Kết quả chạy độc lập (plugin 1.3.6, 28/9/2026)
Claude Code tài khoản `nnqp201`, thư mục làm việc ngoài dự án (kết nối P-THHC), không có CLAUDE.md dự án, câu lệnh mẫu mới.
Sản phẩm lưu `30-Ket-Qua/2026-09-28/Nghiem-thu/Chay-doc-lap-BC9-plugin-1.3.6/`.

| | Số chữ Word | `[CẦN BỔ SUNG]` | Lỗi của mẫu | Công thức phụ lục | KH tháng 10 | Lỗi Mức 1–2 |
|---|---:|---:|---|---:|---|---:|
| 21/9 (trong dự án) | 5.916 | 0 | không | 300 | có | 0 |
| Cowork 28/9 (1.3.5) | 4.872 | 20 | 2021-2026, Báo cáo báo cáo, "(Nguồn:" | 0 | không | 5 |
| Code 28/9 (1.3.5) | 2.222 | 34 | 2021-2026, Báo cáo báo cáo, PHAN_I | 0 | không | 0 |
| **Code 1.3.6 độc lập** | **8.720** | **14** | không | **261** | **có** | **0** |

14 chỗ `[CẦN BỔ SUNG]` đều nằm **sau** nội dung đã tổng hợp của mục, chỉ nêu đúng chi tiết không có nguồn (số liệu tuyển
sinh đến hết tháng 9, kết quả Công đoàn, Đoàn chưa nộp, số ngày quyết định…). Phiên chạy tự phát hiện 7 mâu thuẫn giữa nguồn
(ví dụ Lễ tốt nghiệp 26/9 theo TB 1071 hay tháng 10 theo CTCT) và đưa vào việc người có thẩm quyền quyết.

**Lỗi lộ ra, đã sửa ở 1.3.7** (bao-cao 3.19, SHA-256 `e104d9a6…e786`): số hiệu dị dạng "Số375BC-CĐKT" của bản gốc bị giữ;
tiêu đề mục II phụ lục còn "tháng 8"; phiên ghi "bộ nhớ quá trình" vào chính tệp plugin đã cài (guard nay chặn, kỹ năng ghi
vào ghi chú đối soát); hook đo thể thức đo nhầm tệp đơn vị trong `10-Dau-Vao/`.

**Còn lại:** chạy lại trên tài khoản `phongthhcqt` (Claude Code và Cowork, bản 1.3.7, mô hình mạnh nhất) để so cùng điều kiện
với lần chạy sáng 28/9; cập nhật hồ sơ thẩm định vòng 5 sau khi có kết quả đó.
