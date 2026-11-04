# Đề xuất quy ước — Nguồn duy nhất "danh mục việc đã làm của quý" và gom minh chứng hằng tháng

**Trình:** Trưởng phòng TH-HC&QT duyệt · **Trạng thái:** ĐỀ XUẤT, **chưa áp dụng**
**Căn cứ phát sinh:** lệnh nâng cấp skill `ktc-kpi-tu-danh-gia` ngày 28/10/2026, mục 5.1 và 5.2; phiên làm hồ sơ minh
chứng xếp loại Quý III/2026 theo TB 1105/TB-CĐKT ngày 30/9/2026; Decision Log `DL-20261028-001`.
**Phạm vi đề xuất áp dụng:** toàn thể viên chức, người lao động có hồ sơ tự đánh giá KPI quý — không riêng phòng TH-HC&QT.

---

## 1. Vấn đề

Quý III/2026, mỗi người lập kế hoạch, tự đánh giá và minh chứng ở **ba nơi khác nhau** (sheet Ke Hoach, bảng hỏi, bảng tổng
hợp minh chứng) và gõ lại số liệu ở mỗi nơi. Hệ quả đã xảy ra:

| Sự cố | Hậu quả |
|---|---|
| Cùng một việc (mua sắm thuốc, hóa chất, vật tư y tế Phòng khám) khai ở hai hồ sơ với số khác nhau | Điểm một người đổi 97,20 → 100 → 97,20 trong cùng đợt |
| Minh chứng chỉ được gom khi có TB 1105 | Dồn việc vào vài ngày, bảng tra khớp sai, nhiều dòng “CẦN BỔ SUNG” |
| Số hiệu văn bản điền bằng trí nhớ hoặc suy từ nội dung gần giống | Khó phát hiện khi rà soát, một số hiệu sai làm hỏng cả dòng |

## 2. Đề xuất 1 — Nguồn duy nhất cho mỗi người mỗi quý

1. Mỗi người có **một tệp “Danh mục việc đã làm của quý”**, lấy từ tệp xuất **“Văn bản đã xử lý”** của Hệ thống QLVB&ĐH
   (skill `bao-cao`, Skill 38, công cụ `office_ca_nhan.py`) — số hiệu, ngày, trích yếu là dữ liệu gốc, không gõ lại.
2. Tệp này là nguồn chung cho **kế hoạch** (đối chiếu việc đã đăng ký), **tự đánh giá** (SL thực tế, số hiệu minh chứng) và
   **hồ sơ minh chứng** (bảng tra `ma_viec, so_hieu, nguon` nạp thẳng vào `lap_ho_so_minh_chung.py`).
3. Việc do một người soạn nhưng tính cho người khác (ví dụ việc do viên chức trong phòng soạn được tính trọn vào KPI của
   lãnh đạo phòng phụ trách) được **liên kết** bằng hai cột *Người thực hiện* / *Người phối hợp* — **không gõ lại** ở hồ sơ thứ
   hai. Tính trọn cho ai do Trưởng đơn vị quyết; công cụ chỉ bảo đảm hai hồ sơ dùng **cùng số liệu**.
4. Trước khi nộp hồ sơ của đơn vị, chạy `kpi_doi_chieu_cheo.py` (hoặc tác tử `ktc-doi-chieu-ho-so-cheo`) trên toàn bộ hồ sơ
   của đơn vị; mọi việc khai lệch phải được người thực hiện và người phối hợp thống nhất, **ghi lịch sử thay đổi** (giá trị cũ
   → lý do → căn cứ → người đổi → thời gian → giá trị mới).

## 3. Đề xuất 2 — Gom minh chứng hằng tháng

1. Khi nộp **Phụ lục KPI tháng** (chu trình báo cáo tháng theo TB 736), cột minh chứng của mỗi việc đã hoàn thành trong tháng
   phải **có số hiệu văn bản** (hoặc ghi rõ “không yêu cầu minh chứng”).
2. Cuối quý, hồ sơ minh chứng **ghép từ ba tháng** đã có, không làm mới từ đầu khi có thông báo xếp loại.
3. Số hiệu chỉ được điền khi lấy từ “Văn bản đã xử lý” hoặc do người dùng tự ghi; **không tự điền khi chỉ suy từ nội dung gần
   giống** (tác tử `ktc-xac-minh-minh-chung` ghi mức tin cậy CHẮC / GẦN ĐÚNG / KHÔNG THẤY cho từng cặp).

## 4. Việc cần Trưởng phòng quyết

- [ ] Duyệt áp dụng thử Đề xuất 1 ở phòng TH-HC&QT từ Quý IV/2026 (hồ sơ xếp loại cuối năm).
- [ ] Duyệt đưa yêu cầu “cột minh chứng có số hiệu” vào Phụ lục KPI tháng từ tháng 11/2026.
- [ ] Có đề nghị phòng TCCB&CTHSSV hướng dẫn chung toàn Trường hay không (khi thử đạt).

*Đề xuất của bộ công cụ, chưa phải quy định. Không thay đổi quy trình hiện hành cho đến khi được duyệt.*
