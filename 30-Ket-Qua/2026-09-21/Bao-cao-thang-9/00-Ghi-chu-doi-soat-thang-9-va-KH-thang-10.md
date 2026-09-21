# Ghi chú đối soát — Báo cáo tháng 9 và Kế hoạch tháng 10 năm 2026 (cấp Trường)

**Lập:** 21/9/2026 · **Trạng thái:** DỰ THẢO — chưa qua rà soát 897, chưa trình ký · **Người chốt:** Phòng TH-HC&QT

## 1. Ba sản phẩm đã dựng

| Tệp | Nội dung | Phát triển từ |
|---|---|---|
| `BC_Bao-cao-ket-qua-thang-9-va-KH-thang-10-2026_DU-THAO_20260921.docx` | Báo cáo I (kết quả T9) · II (đánh giá chung) · III (nhiệm vụ T10) | BC-375 (báo cáo tháng 8 đã ban hành) |
| `PL_Phu-luc-ket-qua-cong-tac-thang-9-2026_DU-THAO_20260921.xlsx` | Phụ lục kết quả T9 cấp Trường — 47 nhiệm vụ mục I + 9 mục II, công thức KPI theo PL-375 | PL-375 (phụ lục tháng 8 đã ban hành) |
| `KH_Ke-hoach-cong-tac-thang-10-2026_DU-THAO_20260921.xlsx` | Kế hoạch công tác tháng 10 — 27 nhiệm vụ mục I + 4 mục II | KH-834 (kế hoạch tháng 9 đã ban hành) |

Thể thức: cả ba đạt `kiem_the_thuc.py` (0 lỗi Mức 1–2); docx qua `kiem_vien_dan.py` (0 lỗi) và kiểm văn phong cấp Trường (0 vi phạm). Cột **L** (KH) và cột **Q** (PL) là ghi chú đối soát nằm ngoài vùng in — **xóa trước khi ban hành**.
Chưa chạy được LibreOffice trên máy này nên công thức Excel chưa có giá trị đệm; Excel sẽ tự tính khi mở.

## 2. Đầu vào thực nhận (thư mục `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/`)

| Đầu mối | IIa (tường thuật) | IIb (kết quả T9) | Ib (kế hoạch T10) |
|---|---|---|---|
| P-THHC | Ban TT ✓ · Phòng ✗ | Ban TT ✓ · Phòng: mới ghi 8 tên nhiệm vụ, chưa điền | Ban TT ✓ · Phòng ✗ |
| **P-QLDT** | ✗ | ✗ | ✗ |
| P-QLKH · P-TCKT · K-KHCB · K-KTCN · K-YDUOC · K-DTSHLX | ✓ | ✓ | ✓ |
| P-TCCB | ✓ | ✓ (còn ~12 dòng mẫu "…") | ✓ (2 sheet KH Quý + KH tháng; ~10 dòng "…") |
| K-SUPH | ✓ | ✓ | ✓ (6 nhiệm vụ) |
| **K-KTNL** | ✓ | ✗ | ✗ |
| **DT-CDCS** · **DT-DTN** | ✗ | ✗ | ✗ |

Hệ quả: Trục 4 (Đảng, Công đoàn, Đoàn) và mục con "Công tác khảo thí/tuyển sinh" của Phòng QLĐT&BĐCL mỏng; **24/47 nhiệm vụ của KH-834 không có báo cáo từ đơn vị chủ trì** vì đơn vị chưa nộp.
Cách nộp cũng lệch quy ước (`DL-20260919-001`): tệp đặt tên theo đơn vị, chưa có `<mã>_<loại>_<kỳ>_v<N>` và phiếu tự kiểm.

## 3. Phụ lục kết quả T9 — cách dựng và độ tin cậy

Theo Skill 33 BƯỚC 0A: danh mục = **kế hoạch tháng 9 của chính Trường (KH-834, 47 + 6 nhiệm vụ)**, kết quả điền từ Phụ lục IIb của đơn vị.
Vì chưa có `Task_ID` (KI-001) nên đối chiếu là **gần đúng** — chỉ tính khớp khi nội dung gần như trùng và cùng đơn vị chủ trì:

| Kết quả đối chiếu | Số nhiệm vụ |
|---|---|
| Khớp, đã điền KPI từ IIb (10) | 1.7 · 2.1 · 2.3 · 3.1 · 3.2 · 4.1 · 4.7 · 4.9 · 4.11 · 5.3 |
| Đơn vị chủ trì chưa nộp / chưa điền | 24 |
| Đơn vị đã nộp nhưng **không thấy** nhiệm vụ trong IIb | 13 — *không đồng nghĩa chưa làm* (tiền lệ nhiệm vụ 2.8 tháng 8) |
| Mục II (đột xuất) | 6 nhiệm vụ của KH-834 chưa có kết quả + 3 nhiệm vụ Phòng TC-KT tự khai (Hiệu trưởng chỉ đạo) |

Phụ lục **không** tự kết luận "chưa hoàn thành" cho các dòng trống. Cần P-THHC/đơn vị xác nhận trước khi chốt kỳ.

**KPI tham chiếu** (`doi_soat_so_lieu.py`, tính lại từ 192 dòng IIb của 9 đơn vị, chưa lọc theo kế hoạch Trường; không phải số của phụ lục):

| Trục | Số dòng | % số lượng | % chất lượng | % tiến độ |
|---|---|---|---|---|
| 1 | 92 | 95,3 | 92,1 | 94,3 |
| 2 | 27 | 100 | 93,5 | 95,9 |
| 3 | 18 | 100 | 97,7 | 100 |
| 4 | 17 | 100 | 83,2 | 100 |
| 5 | 24 | 100 | 85,3 | 100 |
| 6 | 14 | 100 | 90,9 | 100 |

Lỗi công thức KPI của đơn vị (không tự sửa): Phòng TC-KT có 3 dòng hệ số/SL quy đổi sai (dòng "thẩm mức kinh tế kỹ thuật…", "Thông báo thu học phí K8C…"); Ban TT 1 dòng KPI tiến độ 1,1 (đúng 0,75); Phòng QLKHCN&HTPT 1 dòng KPI chất lượng 1,0 (đúng 0,3).
Phòng TCCB: các dòng 1.2–1.4 và VNPT KPI có KPI chất lượng/tiến độ 0,5–0,75 — số của đơn vị, phụ lục giữ nguyên.

## 4. Kế hoạch T10 — nguồn và tiêu chí

Kế hoạch quý IV **chưa có** (chỉ có mẫu đăng ký ngày 15/9), nên nhiệm vụ lấy từ 4 nguồn, mỗi dòng ghi nguồn ở cột Ghi chú (11):

1. Phụ lục Ib đánh dấu **"Đưa vào KH Trường" / "Kế hoạch của Trường"** và do **lãnh đạo cấp Trường** chỉ đạo (23 dòng);
2. **Chương trình công tác năm 2026** (QĐ 311/QĐ-CĐKT), mục Tháng 10 và hai nhiệm vụ xếp tháng 9 nhưng hạn tháng 10 (6 dòng);
3. **TB 1019/TB-CĐKT** (giao ban 07–13/9): hạn 30/10 (khung, danh mục dữ liệu), 09/10 (Đề án vị trí việc làm), tồn đọng sân tập lái xe;
4. Phụ lục IIb T9 của Phòng TCCB (Tuần lễ học tập suốt đời 01–07/10).

Mục II ("từ tháng trước chuyển sang") gồm nhiệm vụ có hạn gốc ≤ 30/9/2026 mà đơn vị đưa sang T10: CV 2514-CV/ĐU, QĐ thay thế QĐ 1259, Bộ tiêu chí khởi nghiệp, sân tập lái xe.

**Không đưa vào (cần người quyết):**
- K-KTCN: 6 dòng đánh dấu "Đưa vào KH Trường" nhưng chỉ đạo *Lãnh đạo Khoa* (trái điều kiện cấp Trường); K-YDUOC 1.7 (Giáo vụ khoa).
- K-SUPH (6 dòng), K-KHCB 3.1 và 6.1, K-DTSHLX 1.14 và phần mềm mô phỏng: lãnh đạo Trường chỉ đạo nhưng **đơn vị để trống cột Ghi chú** — không xác định được có đưa lên Trường.
- ~10 dòng "…" của Phòng TCCB (Bí thư Đảng ủy, ĐTN, HSV…) chưa điền.
- Ngày Phụ nữ Việt Nam 20/10 (KH-834 mục 4.6) và "Khảo sát các bên liên quan" (CTCT, hạn 11/2026): chưa có tín hiệu đưa vào T10.

**Cần xác nhận:** độ khó/điểm của 6 nhiệm vụ từ CTCT là **tạm tính "Trung bình" (120)**; đơn vị chủ trì quy đổi từ tên cũ trong CTCT (P. QLĐT, P. KT&QLCL → Phòng QLĐT&BĐCL; P. QLKHCN&HTPT). Thời hạn để trống ghi tạm 31/10/2026 (14 dòng).
Trục 2 và Trục 4 gần như trống vì Đảng ủy/Công đoàn/Đoàn chưa gửi đề xuất tháng 10.

## 5. Lỗi dữ liệu đơn vị (ghi nhận, không tự sửa)

- Ib K-YDUOC: 15/16 dòng để trống Ghi chú; nhiều thời hạn tháng 9 (05/09, 20/09…) trong kế hoạch tháng 10; 1 dòng ghi `19/09/2029`.
- Ib K-KHCB: 14/14 dòng trống Ghi chú, thời hạn tháng 11–12/2026 xen vào kế hoạch tháng 10. Ib SP/K-DTSHLX: Ghi chú trống.
- Ib Phòng TC-KT: dòng 2.1 hệ số 1 ≠ điểm 120×1% (đã tính lại 1,2 trong KH, có ghi chú); "Bản chủ nhiệm" (Ban chủ nhiệm?).
- IIa Phòng TC-KT: "tháng 9/226", "20226"; lương tháng 10 ghi "tháng 8/2026" ở IIa nhưng Ib ghi tháng 10 — báo cáo dùng theo Ib.
- IIa Phòng QLKHCN&HTPT ghi Nghị quyết số 66 hai lần ("Mục 4 …", "Mục 6 …") như tiêu đề — đã gộp nội dung.
- KH-834 (mẫu gốc) còn dòng lạc "công tác tháng 8 năm 2026" (dòng 6) và khối "Nơi nhận" lặp ở dòng 74–79, lỗi chính tả "Đàng ủy" — bản T10 đã bỏ.

## 6. Việc cần người có thẩm quyền

1. Yêu cầu nộp bổ sung: **P-QLĐT (đủ 3 loại), K-KTNL (IIb, Ib), Phòng TH-HC&QT (IIb điền kết quả, Ib, IIa), CĐCS, ĐTN**.
2. Điền số hiệu/ngày ban hành cho báo cáo và kế hoạch; xác nhận người ký.
3. Xác nhận 13 nhiệm vụ "không thấy" và 10 dòng khớp gần đúng ở phụ lục T9.
4. Quyết các mục không đưa vào KH T10 ở mục 4.
5. Chạy **KTC-Ra-Soat-897** trước khi trình ký (Mức 1 còn thì không trình); kiểm hiệu lực các văn bản viện dẫn trong docx bằng `tra_hieu_luc.py` — chưa chạy.
6. Kiểm chứng số liệu tường thuật với minh chứng: một số số hiệu văn bản trong IIa có dấu hiệu nhập sai (ví dụ "Quyết định số 1977/TB-CĐKT", "Quyết định số 1929/TBCĐKT") — báo cáo **không dẫn** các số hiệu này.
7. Ba ý trong docx mục I suy từ báo cáo của khoa vì Phòng QLĐT&BĐCL chưa nộp: Lễ khai giảng đã tổ chức, đợt nhập học 1–2, hồ sơ xét tốt nghiệp K6C — P-THHC đối chiếu trước khi ký.
