# LỆNH THỰC HIỆN (BẢN SỬA) — Xây bộ skill KPI, giai đoạn 1

**Gửi**: Claude Code (VS Code), làm việc trong thư mục dự án `KTC-Quan-tri`
**Người giao**: Phòng TH-HC&QT, Trường Cao đẳng Kon Tum
**Ngày lập**: 24/9/2026 · **Thay cho**: lệnh "Xây bộ skill KPI" cùng ngày (bản gốc)
**Mục tiêu dùng thật**: lập KPI **Quý IV/2026**. Theo QĐ 1923 Đ13.1, hạn là 05 ngày làm việc đầu quý, tức
**07/10/2026**. Quý III/2026 (hạn 27/9 theo CV 694) nằm ngoài phạm vi lệnh này.

## Những gì đã đổi so với bản gốc

| # | Bản gốc | Bản sửa | Lý do |
|---|---|---|---|
| 1 | Repo riêng `ktc-kpi/` có `shared/` và `build.py` riêng | Một hệ trong KTC-Quan-tri: `28-KTC-KPI/`. Quy tắc gốc đặt ở `20-Chuan-Chung/`, dùng chung cơ chế build và kiểm tra hiện có | Skill `quan-tri` đã có `30-KPI-Va-Xep-Loai.md` dựng từ QĐ 1923. Hai bộ quy tắc KPI song song sẽ lệch nhau (bài học số 4 mà bản gốc viện dẫn) |
| 2 | Hệ số = A × B, "vẫn áp dụng" | A × B là **câu hỏi mở số 1**, chỉ là một phương án tùy chọn, không phải quy tắc mặc định | A thuộc thang 5 nhóm (Danh mục TB 1052, **chưa ban hành**, 204/371 dòng lệch Nhóm). B là giá trị thang 4 mức. Nhân hai thang là việc KI-014 cấm tự đặt. Quy ước chưa có văn bản, vi phạm nguyên tắc 1 của chính bản gốc |
| 3 | Người dùng tải tệp về `sources/` | Đọc thẳng KTC-Database qua `29-Cong-Cu/duong_dan.py`. Chỉ chép biểu mẫu vào `assets/` ở bước đóng gói | Claude Code đọc được Google Drive (`<ổ>:/My Drive/KTC-Database`). CLAUDE.md cấm chép dữ liệu kho sang dự án |
| 4 | Xây 3 skill cùng lúc | Giai đoạn 1 chỉ xây skill `lap-ke-hoach` cùng lớp quy tắc và script | Thiếu QĐ 2078 và PL XXIV, XXVI–XXVIII, nên skill tự đánh giá không phục vụ được Nhóm 2, 3, 4. Tổng hợp xếp loại phụ thuộc tự đánh giá |
| 5 | Chưa tính đến nhật ký và sao lưu | Thêm mục 6 về bảo mật dữ liệu cá nhân | Hook nhật ký ghi lời người dùng. `ktc_backup_github.py` chạy `git add -A` rồi đẩy lên GitHub, nên điểm cá nhân có thể bị sao lưu ra ngoài (Đ23) |
| 6 | Chuẩn `tao-skill-va-prompt-chuan` v5 | Dùng skill `skill-creator` nếu người dùng không cung cấp tệp chuẩn v5 | Skill v5 không có trong môi trường này |

---

## 0. Vai trò và nguyên tắc (giữ nguyên bản gốc, bổ sung)

Bạn là kỹ sư xây skill. Bạn **không** tự lập kế hoạch hay chấm điểm KPI cho ai; bạn chỉ đóng gói quy tắc thành skill.

1. Mọi quy tắc phải dẫn tới văn bản nguồn và điều khoản cụ thể, ghi dạng `[QĐ 1923, Đ11.6]`. Không có nguồn thì không viết thành quy tắc. **Áp dụng cả với quy ước nội bộ**, kể cả quy ước do Phòng TH-HC&QT ghi nhận.
2. Quy tắc chưa xác nhận ghi vào mục Câu hỏi mở (mục 4). Skill phải dừng lại hỏi khi gặp tình huống liên quan.
3. Không đưa dữ liệu của một quý cụ thể vào `SKILL.md`. Dữ liệu theo quý đặt trong tệp cấu hình quý.
4. Không sửa biểu mẫu chính thức. Biểu mẫu trong `assets/` giữ nguyên byte; lỗi đã biết ghi trong `known-issues.md`.
5. Mọi phép tính (hệ số, điểm, xếp loại, tỷ lệ) làm bằng script có ca thử, không để mô hình tự nhẩm.
6. Viết tiếng Việt theo quy ước của Trường: "bảo đảm", viết hoa sau dấu hai chấm, tên đơn vị theo Checklist 08 của
   897 và mã đơn vị theo `20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`.
7. **Đọc `CLAUDE.md`, `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md`, `92-Kinh-Nghiem/05-Known-Issues/Pending.md` trước.**
   Đọc riêng `KI-014` trước khi động vào hệ số.

---

## 1. Đọc nguồn

Lấy đường dẫn kho qua `duong_dan.ktc_database()`. Không đọc được kho thì **dừng và hỏi**.

### Bắt buộc (đã xác nhận có trong kho ngày 24/9/2026)
| Văn bản | Vị trí trong KTC-Database |
|---|---|
| QĐ 1923/QĐ-CĐKT, Quy chế KPI, 28 Điều | `02-KTC-Regulations/Quy-che-danh-gia-KPI-tap-the-ca-nhan_Truong-CDKT_lan-3_2026_v1.docx` |
| PL I, II, III của QĐ 1923 | `02-KTC-Regulations/QD1923_PL-*` |
| TB 1052, kèm Mẫu Bản cam kết KPI và Danh mục sản phẩm quy đổi | `02-KTC-Regulations/02-01-…/TB-1052-TB-CDKT_*` (3 tệp và METADATA) |
| QĐ 2073/QĐ-CĐKT, Quy chế làm việc, Chương III | `02-KTC-Regulations/02-01-…/QD-2073-*` |
| CV 694/CĐKT-TCCB và PL II | `03-Templates/03-12- Danh gia xep loai va KPI/` |
| 6 mẫu `Mau-KeHoach-DanhGia_*_QuyIII-2026_*.xlsx` | cùng thư mục |
| `QUY-UOC_He-so-quy-doi-KPI-AxB_20260924.md`, `00-INDEX-METADATA_Bo-KPI-QuyIII-2026_20260924.md` | cùng thư mục |

CV 694 là tệp `.doc` định dạng cũ, cần chuyển sang dạng đọc được. Không đọc được toàn văn thì báo, không suy đoán.

### Không bắt buộc ở giai đoạn 1
QĐ 2078 và các Phụ lục khung tiêu chí, PL I của CV 694, Bảng kiểm sĩ số, Tiêu chí chuyển đổi số. Các nguồn này
dành cho giai đoạn 2 và 3. Chỉ ghi vào mục Câu hỏi mở.

Cuối bước này, in ra: danh sách tệp đã đọc, số Điều hoặc số sheet đã xử lý, tệp chưa đọc được.

---

## 2. Vị trí trong dự án

```
20-Chuan-Chung/
  19-Quy-Tac-KPI.md              ← BẢN GỐC quy tắc KPI (mới). Hợp nhất nội dung
                                   22-KTC-Dieu-Phoi/references/30-KPI-Va-Xep-Loai.md vào đây
28-KTC-KPI/                      ← hệ mới
  00-README.md
  SKILL.md                       ← skill ktc-kpi-lap-ke-hoach
  references/
    Skill-Library/19-Quy-Tac-KPI.md   ← bản sao, đồng bộ lúc build (C5 kiểm)
    Cau-Hoi-Mo.md                 ← mục 4
    Known-Issues-Bieu-Mau.md      ← mục 5
    Thuat-Ngu.md
    quy/2026-Q3.yaml · quy/2026-Q4.yaml
    data/he-so-san-pham-TB1052.csv   ← SINH bởi script trích, kèm sha256 của tệp nguồn
  assets/                        ← 6 mẫu Kế hoạch, chép từ kho lúc build, giữ nguyên byte
  ktc-kpi-lap-ke-hoach-v1.0.skill
29-Cong-Cu/
  kpi_calc.py · validate_plan.py · trich_danh_muc_tb1052.py
92-Kinh-Nghiem/02-Regression/Cases/
  test_kpi_calc.py · test_validate_plan.py   ← kiểu ca thử của dự án, có ca thử ngược
```

Việc bắt buộc đi kèm:
- Thêm `ktc-kpi-lap-ke-hoach` vào `HE` và thêm `19-Quy-Tac-KPI.md` vào `CHUNG` trong `29-Cong-Cu/kiem_tra_he_thong.py`.
- Thêm gói mới vào `GOI_NGUON` và `kpi_calc.py`, `validate_plan.py` vào `CONG_CU_CHO_AGENT` trong `29-Cong-Cu/dong_goi_plugin.py`.
- `30-KPI-Va-Xep-Loai.md` của skill `quan-tri` được thay bằng bản sao của `19-Quy-Tac-KPI.md` (theo cách của `DOI_TEN`), hoặc chỉ còn trỏ tới bản gốc. **Không để hai bản nội dung khác nhau.**
- Mô tả skill phải phân biệt KPI **cá nhân** (QĐ 1923) với "KPI 3 chiều theo Trục" của `bao-cao` và `theo-doi-cv`, vốn là KPI **đơn vị** theo Phụ lục TB 736.

---

## 3. Nội dung `19-Quy-Tac-KPI.md`

Giữ nhóm A–F của bản gốc (thứ bậc văn bản, lập kế hoạch, chấm điểm, xếp loại, bảo mật). **Đối chiếu từng dòng với
toàn văn.** Ngày 24/9 đã kiểm tra khớp các điểm sau: trục chính từ 40% trở lên (Đ12); mỗi nhóm tiêu chí chung không
thấp hơn 05 điểm, tổng không quá 30 (Đ10); trần 25% (Đ7); "05 ngày làm việc đầu quý" (Đ13.1); 28 Điều.

Các điểm đã đổi hoặc phải xử lý:
- **Nhóm C (Hệ số quy đổi) bỏ khỏi quy tắc.** Chỉ ghi: "Hệ số quy đổi khối lượng: chưa có văn bản của Trường quy
  định cách tính. Xem Câu hỏi mở số 1 và KI-014."
- **Người đứng đầu không cao hơn tập thể.** Bản cũ của dự án dẫn khoản 7 Điều 12 NĐ 233/2026; bản gốc của lệnh dẫn
  QĐ 1923 Đ14.4, Đ19.4. Đối chiếu cả hai, ghi cả hai nếu đều đúng. Kiểm hiệu lực NĐ 233 bằng `tra_hieu_luc.py`.
- **Trần tỷ lệ HTXS.** Tách riêng trần của **đơn vị** (Đ7: 20%, tối đa 25%) với trần của **cá nhân theo nhóm tương
  đồng** (Đ19.2). Không gộp làm một.

---

## 4. Câu hỏi mở — skill phải dừng hỏi khi gặp

| # | Câu hỏi | Hành vi khi chưa có trả lời |
|---|---|---|
| 1 | **Hệ số quy đổi đầu việc tính thế nào?** Phương án A × B (quy ước Phòng TH-HC&QT ghi nhận 24/9/2026) nhân hệ số thang 5 nhóm (TB 1052, chưa ban hành) với hệ số thang 4 mức. Chưa có văn bản; Phòng TCCB&CTHSSV chưa xác nhận; chưa biết phần mềm KPI tính cách nào. Liên quan KI-014 | `kpi_calc.py --he-so {nhap-tay, A, AxB}`, **không có mặc định**. Skill hỏi người dùng chọn. Mọi đầu ra ghi phương án đã chọn và trạng thái "chưa có văn bản" |
| 2 | Hệ số A lấy từ Danh mục TB 1052 là **dự thảo**, 204/371 dòng có hệ số lệch Nhóm. Sản phẩm không có trong Danh mục thì xử lý sao? | Dùng A thì in cảnh báo "hệ số dự thảo" kèm dòng lệch nếu có. Sản phẩm không có trong Danh mục thì dừng hỏi, không tự gán |
| 3 | Trọng số điểm KPI (trên 70) có tính theo tỷ lệ "Số lượng quy đổi" của từng chỉ tiêu không? | `--trong-so {nhap-tay, theo-quy-doi}`, mặc định `nhap-tay` |
| 4 | Đ13.1 (KPI **cá nhân**: 05 ngày làm việc đầu quý) và mốc "trước ngày 05 tháng đầu quý" (kế hoạch công tác quý **của đơn vị** gửi Phòng TCCB) có phải hai sản phẩm với hai hạn khác nhau không? | Ghi cả hai hạn theo đúng đối tượng. Chỉ coi là mâu thuẫn nếu toàn văn cho thấy cùng một sản phẩm |
| 5 | Hướng dẫn Quý IV/2026 chưa có | `2026-Q4.yaml` dùng mốc chuẩn QĐ 1923 và ghi `van_ban_huong_dan: null`. Skill báo "chưa có hướng dẫn quý, đang dùng mốc chuẩn của Quy chế" |
| 6 | QĐ 2078, PL I CV 694, Bảng kiểm sĩ số, Tiêu chí chuyển đổi số | Không dùng ở giai đoạn 1. Ghi để làm giai đoạn 2 |

---

## 5. Lỗi đã biết trong biểu mẫu

Giữ nguyên 5 mục của bản gốc (mục 6). Giai đoạn 1 chỉ dùng 6 mẫu Kế hoạch, nên skill chỉ cần cảnh báo mục 4 (dòng
ví dụ "tiếng Bahnar", cụm "sâu rộng trong toàn Đảng") và mục 5 (ô số Quyết định để trống). Các mục còn lại ghi
sẵn cho giai đoạn 2.

---

## 6. Bảo mật dữ liệu cá nhân (mới)

1. Kế hoạch KPI và điểm của cá nhân xuất vào `30-Ket-Qua/<ngày>/KPI-ca-nhan/`. **Thêm đường dẫn này vào
   `.gitignore`** để `ktc_backup_github.py` không đẩy lên GitHub. Viết ca thử chứng minh tệp trong thư mục đó
   không bị `git add -A` đưa vào.
2. Báo cho người dùng biết hook nhật ký ghi lời nhắn vào `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/`. Không tự sửa
   hook ở lượt này: đề xuất cơ chế loại trừ thành một mục riêng, chờ duyệt.
3. Xác nhận repo GitHub `KTC-Quan-tri` đang để **Private**. Không kiểm tra được thì ghi vào báo cáo bàn giao.

---

## 7. Skill `ktc-kpi-lap-ke-hoach`

Giữ mục 4.1 của bản gốc, với các thay đổi sau:
- Bước tính hệ số: hỏi phương án theo Câu hỏi mở số 1 **trước khi** tính.
- Bảng cảnh báo đầu ra bổ sung: phương án hệ số đã dùng và trạng thái của nó; dòng dùng hệ số A đang lệch Nhóm.
- `description` dưới 1024 ký tự, nêu rõ "KPI cá nhân theo QĐ 1923", **không** dùng cho KPI đơn vị theo Trục (thuộc
  `bao-cao` và `theo-doi-cv`).
- Đầu ra Excel dựng từ đúng mẫu trong `assets/` bằng `openpyxl`, **đạt `kiem_the_thuc.py`**, không ghi đè mẫu.

---

## 8. Script và kiểm thử

- `kpi_calc.py`: giữ yêu cầu của bản gốc (mục 7), thêm tham số `--he-so` theo Câu hỏi mở số 1.
- `validate_plan.py`: mã lỗi, vị trí dòng, căn cứ.
- Ca thử theo kiểu `92-Kinh-Nghiem/02-Regression/Cases/`: các ngưỡng 89,99 / 90 / 69,99 / 70 / 49,99 / 50; vượt
  100%; trục chính 39,99% và 40%; nhóm tiêu chí chung 4,99 điểm; sản phẩm không có trong Danh mục; gọi `--he-so`
  mà không chọn phương án thì phải báo lỗi, không tự chọn.
- **Mỗi phép kiểm phải có ca thử ngược** (quy tắc `.claude/rules/22-kiem-thu-va-dong-goi.md`).
- `python 29-Cong-Cu/kiem_tra_he_thong.py` phải đạt 0 lỗi trước và sau khi đóng gói.

---

## 9. Chạy thử trước khi bàn giao

Giữ bảng của bản gốc cho `lap-ke-hoach`:
- nên kích hoạt: "Lập KPI quý IV cho tôi, giáo vụ khoa Y-Dược";
- không nên kích hoạt: "Chấm điểm KPI quý III của tôi";
- tình huống biên: "Sửa kế hoạch KPI đã duyệt vì có nhiệm vụ đột xuất" (Đ13.4).

Thêm 2 ca:
- "Tính % KPI theo Trục của khoa tháng 9": phải **không** kích hoạt skill này (thuộc `bao-cao`);
- "Hệ số của đầu việc này là bao nhiêu?": phải hỏi phương án hệ số, không tự trả lời A × B.

Ghi kết quả vào `28-KTC-KPI/TEST-REPORT.md`.

---

## 10. Đóng gói và bàn giao

1. Đóng gói `ktc-kpi-lap-ke-hoach-v1.0.skill`, dựng lại plugin (lên 1.1.0 vì có skill mới), cập nhật `31-Plugin/CHANGELOG.md`.
2. Ghi Decision Log `92-Kinh-Nghiem/06-Decision-Log/DL-<ngày>-…-Bo-skill-KPI.md` và cập nhật `MEMORY-INDEX.md`.
3. **Không tự tải lên Drive, không tự cài vào Claude.ai.**
4. Báo cáo bàn giao gồm:
   - tệp nguồn đã đọc và chưa đọc được;
   - số quy tắc đã trích, mỗi quy tắc kèm Điều;
   - kết quả ca thử;
   - `TEST-REPORT.md`;
   - câu hỏi mở còn tồn;
   - danh sách việc gửi Phòng TCCB&CTHSSV xác nhận (Câu hỏi mở 1–4).

## 11. Điều kiện dừng ngay

Giữ nguyên mục 10 của bản gốc, thêm hai điều kiện:
- Phát hiện hai bản quy tắc KPI khác nhau trong dự án mà chưa hợp nhất được.
- Bất kỳ bước nào cần chọn quy tắc chuyển đổi giữa hai thang điểm.

## Giai đoạn sau (không làm ở lượt này)
- **Giai đoạn 2** `ktc-kpi-tu-danh-gia`: khi có QĐ 2078 và PL XXIV, XXVI–XXVIII, PL I CV 694.
- **Giai đoạn 3** `ktc-kpi-tong-hop-xep-loai` và rà soát khung tiêu chí: khi giai đoạn 2 đã chạy thật một quý.

*Kết quả do AI xây dựng chỉ có giá trị tham khảo. Quy tắc nghiệp vụ trong skill phải được Phòng TCCB&CTHSSV và
Phòng TH-HC&QT duyệt trước khi dùng chính thức.*
