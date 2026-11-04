# DL-20261028-001 — Nâng cấp skill `ktc-kpi-tu-danh-gia` v1.4 sau phiên hồ sơ minh chứng Quý III/2026

**Yêu cầu:** lệnh `LENH-Nang-cap-skill-KPI-tu-danh-gia-ho-so-minh-chung.md` (phòng TH-HC&QT, 28/10/2026), nối tiếp lệnh
giai đoạn 2 ngày 25/9/2026. Căn cứ phát sinh: phiên làm hồ sơ minh chứng xếp loại Quý III/2026 theo **TB 1105/TB-CĐKT
ngày 30/9/2026** (thư mục `30-Ket-Qua/2026-10-01/KPI-ca-nhan/Ho-so-ra-soat-Q3-*`). Phạm vi dùng thật: toàn Trường.

## Ba quyết định

### 1. Điều kiện “hoàn thành 100% nhiệm vụ” áp cho **cả ba mức**, công cụ không tự gỡ

QĐ 1923 Đ19.1a, b, c đều có điều kiện đơn vị, lĩnh vực trực tiếp quản lý hoàn thành 100% nhiệm vụ (Đ19.1b thêm “đúng hạn,
bảo đảm chất lượng”). Một việc chưa trọn có thể kéo **cả ba mức** xuống “Không đạt”. Công cụ:
- **suy C08, C09 từ sheet B** (đếm việc có SL đủ, chất lượng và tiến độ đạt 100%), không hỏi người dùng Có/Không từ đầu;
- người dùng chỉ **xác nhận** hoặc **nêu ngoại lệ khách quan** — ngoại lệ được chép **nguyên văn** vào bảng điều kiện,
  kết quả ghi “Thiếu dữ liệu — người dùng tự xác nhận”, **không tự chuyển thành “Đạt”**;
- việc gỡ hay không thuộc người có thẩm quyền. Cách hiểu “theo từng mức” chưa có văn bản → Câu hỏi mở số 14.

Lý do: Quý III/2026, câu C08 trả lời tay khiến cả ba mức “Không đạt” vì 1/23 việc chưa trọn (B25 — mua sắm thuốc, hóa chất,
vật tư y tế Phòng khám đợt 2, đợt 3: 5/7 nội dung, 75%). Người dùng biết lý do khách quan nhưng công cụ không có chỗ ghi.

### 2. Không tự suy “vượt mức” — phải có loại vượt và căn cứ kèm số liệu

“Vượt mức” chỉ được tính khi dòng việc có **Loại vượt** (số lượng / chất lượng / tiến độ / hiệu quả) và **Căn cứ vượt mức kèm
số liệu** [TB 1105, mục 2.3]. Thiếu → NQ03 LỖI. Khai “Vượt mức” hoặc “Hoàn thành đúng hạn” mà tiến độ < 100% hoặc SL thực <
SL kế hoạch → NQ01 LỖI. Tự đề xuất HTXS khi tỷ lệ vượt mức < 30% → NQ04 LỖI. Công cụ **không** viết căn cứ thay người dùng.

Lý do: Quý III/2026 các dòng “Vượt mức” phải suy căn cứ từ tính chất việc, và bản dự thảo căn cứ (“DỰ THẢO — anh xác nhận/sửa”)
lọt vào bảng chuẩn bị nộp.

### 3. Bản nộp **chỉ sinh khi sạch cờ**; không có “đã xong” nếu chưa đọc lại tệp

`lap_ho_so_minh_chung.py` sinh hai bản: **nội bộ** (cờ `[CẦN XÁC NHẬN]`, `[SUY LUẬN]`, `[THIẾU DỮ LIỆU]`) và **nộp**. Còn
cờ → không sinh bản nộp, mã thoát 2, in danh sách ô chưa xử lý. Sau khi sinh, công cụ **mở lại tệp**: đếm dòng việc bằng số
việc đầu vào, không còn ô trống, quét chuỗi cấm (`CẦN BỔ SUNG`, `DỰ THẢO`, `em đã`, `TODO`, `[CẦN`). SKILL.md mục 5b bắt buộc
quy trình này trước khi báo kết quả.

Lý do: phiên 1/10/2026 báo “hồ sơ đã đầy đủ” khi chưa đọc lại tệp; bảng tra minh chứng khớp sai (khóa số với khóa chuỗi) làm
hàng loạt dòng “CẦN BỔ SUNG”.

## Minh họa — vì sao cần nguồn duy nhất và lịch sử thay đổi

Điểm tự đánh giá Quý III/2026 của Nguyễn Ngọc Quang Phục đổi **97,20 → 100 → 97,20** trong cùng đợt vì cùng một việc (B25)
được khai ở hai hồ sơ (người trực tiếp phụ trách và người phối hợp) với số liệu khác nhau, không có đối chiếu chéo và không ghi
lịch sử từng lần đổi. Chạy lại ngày 28/10/2026 bằng v1.4 trên bảng hỏi hiện lưu: **97,20 điểm**; C08 suy từ sheet B
**22/23 việc trọn 100%**, chưa trọn B25 → điều kiện 100% nhiệm vụ “Không đạt” ở cả ba mức (trước đây người dùng khai “Có”).
Bản chạy lại **không** thay hồ sơ đã nộp (ngoài phạm vi — mục 8 của lệnh).

## Đã kiểm

- `test_kpi_nhat_quan.py`: 31 phép, có 5 ca bắt buộc của lệnh (a–e) và ca ngược — **ĐẠT**.
- `test_lap_ho_so_minh_chung.py`: 19 phép (khóa chuỗi/số lẫn lộn, đọc lại .docx, thể thức A4, lề 2-2-3-2, TNR 14 trong bảng,
  twips, dòng tiêu đề lặp, không tách dòng, số trang ẩn trang 1) — **ĐẠT**.
- Chạy thật trên hồ sơ Q3 của hai người: mẫu chuẩn → NQ bắt đúng 7 dòng “Vượt mức” chưa có căn cứ (hạ cảnh báo vì bảng hỏi bản
  cũ), 7 dòng còn chữ “DỰ THẢO”, NQ10 bắt C08; mẫu Phụ lục II/VII → báo rõ dòng 18 lệch, mã thoát 2, không `KeyError`.
- `kpi_doi_chieu_cheo.py` trên hai TDG thật: phát hiện 1 việc khai lệch (bảo vệ bí mật nhà nước, SL 1 và 3).

## Chưa làm — không ghi là đã làm

- `doc_mau_phu_luc_vii()` (đọc tự động mẫu Phụ lục II/VII để chạy NQ) — tùy chọn của lệnh, chưa làm; hiện chỉ báo rõ và dừng.
- Plugin chưa dựng lại: gói `.skill` v1.4 đã đóng; phát hành 1.3.14 chờ người phụ trách.
- Ca thử mô phỏng cho 3 tác tử mới (mục 4 của lệnh) mới có ở mức công cụ (script mà tác tử gọi đã có ca thử); chưa có bộ ca
  định tuyến tác tử trên Claude Chat/Cowork.
