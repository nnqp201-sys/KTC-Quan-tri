# 37 — Báo cáo tháng cấp Trường: dựng từ bản đã ban hành (quy trình chính, từ v3.18)

**Ban hành:** 28/9/2026 · **Lý do:** chạy thử 28/9/2026 trên Cowork, Claude Code cho sản phẩm kém bản 21/9/2026 — dựng từ
mẫu trắng `00. Mau bao cao thang (cap Truong).docx` qua `fill_bc736.py`, để lại thẻ `[CẦN BỔ SUNG [PHAN_I] …]`, mang theo lỗi
của mẫu ("nhiệm kỳ 2021-2026", "Báo cáo báo cáo", "tháng 7"), thay tường thuật bằng tỷ lệ %, bỏ cả đơn vị vì vài dòng sai
công thức KPI, thiếu kế hoạch tháng sau. Bản 21/9 đạt vì phát triển từ bản đã ban hành (Nguyên tắc 7) và tổng hợp từ mọi
báo cáo có nguồn. Quy trình này đóng gói cách làm đạt đó vào công cụ `bc_thang.py`.

## 1. Sản phẩm mặc định

"Báo cáo tháng N" cấp Trường theo Quy chế làm việc = **kết quả tháng N và kế hoạch tháng N+1**. Mặc định giao **4 tệp**:

| Tệp | Nội dung | Phát triển từ |
|---|---|---|
| `BC_…thang-N…_DU-THAO_<ngày>.docx` | I. Kết quả tháng N · II. Đánh giá chung · III. Nhiệm vụ trọng tâm tháng N+1 | Báo cáo tháng N−1 **đã ban hành** |
| `PL_…ket-qua…thang-N…_DU-THAO_<ngày>.xlsx` | Phụ lục kết quả tháng N: danh mục = kế hoạch tháng N của Trường; kết quả từ Phụ lục IIb; công thức KPI | Phụ lục tháng N−1 **đã ban hành** |
| `KH_…thang-N+1…_DU-THAO_<ngày>.xlsx` | Kế hoạch công tác tháng N+1 | Kế hoạch tháng N **đã ban hành** |
| `00-Ghi-chu-doi-soat-thang-N….md` | Nguồn từng ý, dòng chưa khớp, lỗi dữ liệu đơn vị, việc cần người có thẩm quyền xác nhận | — |

Người dùng chỉ yêu cầu một phần thì làm phần đó, nhưng **nói rõ** các tệp chưa làm. Tài khoản thành viên: giao trong phiên,
tên chuẩn theo Nguyên tắc 3.

## 2. Các bước (công cụ: `bc_thang.py`, cùng thư mục với tệp này hoặc `scripts/` ở gốc plugin)

0. **Nguồn:** `python bc_thang.py nguon --ky YYYY-MM --dau-vao <thư mục nộp>` → bản đã ban hành (BC, PL tháng N−1; KH tháng
   N), phân loại tệp đơn vị (IIa, IIb, Ib) và mã đơn vị. Kho không có bản đã ban hành nào → mới dùng mẫu trắng
   (`fill_bc736.py`), ghi rõ lý do trong ghi chú đối soát.
1. **Trích:** `python bc_thang.py trich --dau-vao <thư mục nộp> --ra trich.json` rồi **đọc hết**: tường thuật IIa theo Trục
   (`kq`, `kh`, `nq_kq`, `nq_kh`, `dat`, `chua`) và các dòng IIb, Ib. Tường thuật IIa là nguồn chính của phần Word.
2. **Kiểm hồ sơ** (Skill 32, tác tử `ktc-kiem-ho-so-don-vi`): ghi lỗi vào ghi chú đối soát. **Dòng sai công thức KPI → chỉ
   không dùng số KPI của dòng đó**; vẫn dùng tường thuật và các dòng đúng của đơn vị. "Trả lại đơn vị" là yêu cầu đơn vị sửa,
   **không** phải loại đơn vị khỏi báo cáo.
3. **Soạn nội dung** (`bc.json`, `pl.json`, `kh.json` — cấu trúc ở mục 4):
   - Chủ thể "Nhà trường"; văn phong cấp Trường (`Skill-Tu-hoc-Phong-Cach-Bao-Cao.md`, Skill 33 BƯỚC 0C); nhãn mục con
     **cố định** (mục 3) — không tự đặt.
   - **Mỗi ý phải có nguồn** — ghi vào tệp ghi chú đối soát, **không** chèn "(Nguồn: …)" vào thân văn bản.
   - **Đầu mối chưa nộp** (ví dụ Phòng QLĐT&BĐCL cho tuyển sinh, đào tạo): tổng hợp từ báo cáo của các đơn vị khác (khoa báo
     cáo khai giảng, nhập học, thực tập…), kế hoạch tháng N đã ban hành, Chương trình công tác năm, thông báo kết luận giao ban
     trong kho. Đây là **tổng hợp có nguồn, không phải suy diễn**; ghi nguồn vào ghi chú đối soát. Chỉ khi **không có nguồn
     nào** mới ghi `[CẦN BỔ SUNG: <nội dung>, <đơn vị>]`, đồng thời nêu ở "Tồn tại, hạn chế".
   - Tỷ lệ KPI theo Trục thuộc **phụ lục**; phần Word chỉ nêu gọn ở "Đánh giá chung" nếu cần. **Không** thay tường thuật bằng
     tỷ lệ %.
   - Kế hoạch tháng N+1: dòng Ib đánh dấu "Đưa vào KH Trường" **và** do lãnh đạo cấp Trường chỉ đạo (Skill 33 BƯỚC 0A);
     Chương trình công tác năm (mục tháng N+1); thông báo kết luận giao ban; nhiệm vụ tháng N chưa xong → mục II "từ tháng trước
     chuyển sang". Dòng không đủ điều kiện → liệt kê trong ghi chú đối soát, không tự đưa vào.
4. **Dựng:** `bc_thang.py word|phu-luc|ke-hoach --goc <bản đã ban hành> --noi-dung <json> --ra <tệp>`. Đọc JSON tự kiểm:
   `con_can_bo_sung`, `ky_cu_o_dau_cuoi`, `vi_pham_van_phong`, `muc_con_chua_co_trong_phan_I_III` — khác 0 thì sửa nội dung
   hoặc giải trình trong ghi chú đối soát.
5. **Thể thức:** `kiem_the_thuc.py` từng tệp (0 lỗi Mức 1–2). Cột ghi chú đối soát nằm ngoài vùng in — xóa trước khi ban hành.
6. **Trước trình ký:** rà soát `ktc-ra-soat-897`. Số, ngày văn bản để trống cho Văn thư.

## 3. Nhãn mục con cố định (phần I và III)

| Mục | Mục con, đúng thứ tự |
|---|---|
| 1 | Công tác tuyển sinh · Công tác đào tạo · Công tác khảo thí · Công tác bảo đảm chất lượng · Công tác kế hoạch, tổng hợp · Công tác tổ chức, cán bộ |
| 2 | Về thể chế · Công tác Kiểm tra, giám sát |
| 3 | **Không có mục con** — một đoạn (nhãn `null`) |
| 4 | Công tác xây dựng Đảng · Chấp hành kỷ cương hành chính · Công tác Đảng, Công đoàn, Đoàn Thanh niên |
| 5 | Công tác quản lý cơ sở vật chất · Công tác Tài chính · Công tác an sinh giáo dục · Công tác truyền thông |
| 6 | Về Quốc phòng - An ninh · Về hoạt động Đối ngoại và Hợp tác · Về hoạt động hợp tác phát triển |
| 7 | Nghị quyết của Bộ Chính trị — ghi số: 59 · 66 · 68 · 79 · 70 · 71 · 72 · 80 (công cụ tự điền tên đầy đủ, đúng thứ tự) |

## 4. Cấu trúc JSON nội dung

```json
// bc.json
{"ky": {"thang": 9, "nam": 2026},                // ky_sau mặc định tháng kế tiếp
 "ket_qua":  {"1": [["Công tác tuyển sinh", "Nhà trường ..."], ...], "3": [[null, "Nhà trường ..."]], "7": [["59", "..."]]},
 "danh_gia": {"dat": "Trong tháng 9 năm 2026, Nhà trường ...", "ton_tai": "..."},
 "nhiem_vu": {"1": [["Công tác tuyển sinh", "Nhà trường tiếp tục ..."], ...], "7": [["59", "..."]]}}

// pl.json — danh mục theo kế hoạch tháng N của Trường
{"ky": {"thang": 9, "nam": 2026},
 "truc": {"1": {"dong": [{"nd": "...", "cd": "Hiệu trưởng", "ct": "Phòng ...", "sp": "Kế hoạch", "sl": 1, "dk": "Trung bình",
                          "ket_qua": {"sl": 1, "cl": 1, "td": 1},        // tỷ lệ 0..1 từ IIb; null = chưa có kết quả
                          "doi_soat": "Nguồn: P-TCCB Phụ lục IIb dòng 1.2 — đối chiếu gần đúng"}]}},
 "dot_xuat": [ ...dòng như trên... ]}

// kh.json — kế hoạch tháng N+1
{"ky": {"thang": 10, "nam": 2026}, "ngay": "Quảng Ngãi, ngày     tháng 9 năm 2026",
 "can_cu": "        Căn cứ ...;\n        Nhà trường ban hành Kế hoạch công tác tháng 10 năm 2026, cụ thể như sau:",
 "truc": {"1": {"dong": [{"nd": "...", "cd": "...", "ct": "...", "sp": "...", "sl": 1, "dk": "Trung bình",
                          "thoi_han": "Chậm nhất ngày 31/10/2026", "ghi_chu": "Đơn vị đề xuất", "doi_soat": "Nguồn: ..."}]}},
 "chuyen_tiep": [ ...nhiệm vụ tháng trước chuyển sang... ]}
```

## 5. Không làm

- Không dựng từ mẫu trắng khi kho có bản đã ban hành; không để thẻ `[CẦN BỔ SUNG [PHAN_…]]` của `fill_bc736.py`.
- Không chép lỗi của mẫu cũ; không để sót kỳ cũ ở tiêu đề, câu mở đầu, câu kết.
- Không loại cả đơn vị vì lỗi công thức vài dòng; không tự sửa số liệu đơn vị (ghi vào ghi chú đối soát).
- Không cấp Task_ID; không kết luận "chưa hoàn thành" cho dòng chưa có báo cáo (ghi "chưa có kết quả", chờ xác nhận).
