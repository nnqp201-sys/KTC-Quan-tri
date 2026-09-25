# DL-20260925-001 — Bộ skill KPI giai đoạn 2: tự đánh giá, đề xuất xếp loại cá nhân theo quý

**Ngày:** 25/9/2026 · **Căn cứ giao việc:** `30-Ket-Qua/2026-09-25/De-xuat/LENH-Xay-skill-KPI-giai-doan-2-Tu-danh-gia.md`
(người dùng gửi lệnh vào phiên, hiểu là yêu cầu thực hiện — cùng cách với lệnh sửa giai đoạn 1) · **Trạng thái:** đã
thực hiện; quy tắc nghiệp vụ chờ Phòng TCCB&CTHSSV và Phòng TH-HC&QT duyệt trước khi dùng chính thức.

## 1. Quyết định chính — HAI skill riêng (phương án b), không gộp

Đã chạy thật 8 câu cho cả hai phương án (`28-KTC-KPI/TEST-REPORT.md` mục 4.3): **cả hai 8/8** ở mức chọn skill. Vì kích
hoạt ngang nhau, chọn theo các tiêu chí còn lại:

| Tiêu chí | (a) một skill `ktc-kpi-ca-nhan` | (b) `kpi-lap-ke-hoach` + `kpi-tu-danh-gia` |
|---|---|---|
| Mô tả | 1009/1024 ký tự — hết chỗ cho cụm kích hoạt mới | 988 và 1003, mỗi mô tả một việc |
| Tách lập / tự đánh giá | Dồn vào thân SKILL.md dài hơn — **chưa đo được** | Do bộ chọn skill làm — **đã đo 8/8** |
| Người đã cài 1.1.x | Đổi tên skill → bản `.skill` cũ trên Claude.ai thành trùng | Giữ nguyên tên `ktc-kpi-lap-ke-hoach` |
| Giai đoạn 3 (tổng hợp đơn vị, người dùng khác) | Phải tách lại | Thêm skill thứ ba cùng khuôn |
| Chi phí | Một bản mẫu, một bản script | 6 mẫu + script nhân đôi (~300 KB) — `dong_goi_kpi.py` đồng bộ có kiểm hash; C4/C5 bắt lệch |

**Bố trí:** nguồn skill mới tại `28-KTC-KPI/Tu-Danh-Gia/` (gói `.skill` phải tự chứa → bản sao do công cụ đồng bộ; C4
đòi mọi tệp trong gói có bản rời trùng hash). Gói `kpi-lap-ke-hoach` loại thư mục `Tu-Danh-Gia/`.

## 2. Quyết định kỹ thuật

1. **Chặn trần theo từng chỉ tiêu, trên trung bình 3 chiều** [QĐ 1923, Đ11.6: "mức độ hoàn thành một chỉ tiêu vượt quá
   100%"]. Mẫu Quý III cộng dồn cả Trục không chặn (Known-Issues #7) → chỉ tiêu vượt bù cho chỉ tiêu thiếu. Tệp ra thay công
   thức % Trục bằng `SUMPRODUCT` có chặn; in chênh lệch. Excel thật tính lại khớp Python. Câu hỏi mở #12 chờ xác nhận.
2. **Mục A nhận điểm từng tiêu chí con, mức xét theo tổng nhóm** — đọc toàn văn Đ10.5 thấy mức áp cho *nhóm nội dung*,
   bản tóm tắt không nói rõ; mẫu lại chấm theo tiêu chí con. Người dùng chọn mức nhóm thì tổng phải nằm đúng khung. Công cụ
   không chọn điểm trong khung thay người dùng (Câu hỏi mở #10).
3. **Một bảng hỏi Excel, ba sheet** thay hỏi rời (lệnh mục 4): ô vàng, `DataValidation`; thiếu ô bắt buộc → mã thoát 2,
   liệt kê ô thiếu.
4. **Không kết luận mức**: in mức theo ngưỡng điểm + bảng điều kiện (Đạt / Không đạt / Thiếu dữ liệu / Không áp dụng)
   cho mức đó và các mức thấp hơn; mục III ghi mức **người dùng** tự đề xuất, không ghi mức công cụ tính.
5. **So ngưỡng trên giá trị chính xác** (khử nhiễu dấu phẩy động 1e-6), hiển thị **cắt** 2 chữ số — 89,996 hiện 89,99.
6. **"Vượt mức"** (điều kiện 30% HTXS) do người dùng khai từng nhiệm vụ; cảnh báo khi khai vượt mà số liệu ≤ 100%
   (Câu hỏi mở #11).
7. Trường hợp đặc thù Đ21.4, Đ21.6 → dừng trước khi chấm.

## 3. Phát hiện kèm theo, đã sửa cùng lượt (giai đoạn 1)

- **Sheet KPI của cả 6 mẫu có số thực tế ví dụ** (L=4, N=100, P=100). `ghi_ke_hoach` v1.0 chỉ xóa dòng ví dụ ở "Ke Hoach"
  → kế hoạch xuất ra mang số "thực tế" giả, % Trục 1 sai khi mở bằng Excel. Sửa + KH16 (Known-Issues #12). KH16 lần đầu
  viết thành LỖI cho mọi số thực tế — chạy trên tệp Quý III thật báo nhầm (Quý III lập và đánh giá cùng lúc, số là thật)
  → thu hẹp: chỉ bắt khi trùng đúng số ví dụ của mẫu.
- **`nhan_nhom()` không nhận mẫu Trưởng/Phó đơn vị** (tiêu đề "TRƯỞNG/PHÓ CÁC ĐƠN VỊ", mã tìm "trưởng, phó") →
  `validate_plan.py` không truyền `--nhom` thì bỏ sót KH10 (lãnh đạo thiếu Trục 4). Sửa + ca thử cả 6 mẫu.
- Vá xuống dòng, ẩn dòng trống (Known-Issues #10, #11) vào thẳng `kpi_mau.py` — phiên 24–25/9 phải vá tay.

## 4. Chưa làm / chờ

- Chạy kích hoạt trên **Claude Chat/Cowork** (mới chạy Claude Code headless).
- Phòng TCCB&CTHSSV: Câu hỏi mở #8, #10–#13; PL XXIV, XXVI–XXVIII; Bảng kiểm sĩ số; Tiêu chí chuyển đổi số; Hướng dẫn
  đánh giá hằng quý/năm [Đ24.2].
- Giai đoạn 3 `ktc-kpi-tong-hop-xep-loai` (PL II CV 694, trần HTXS Đ19.2, người đứng đầu ≤ tập thể).
