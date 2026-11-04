# 34-Skill-Doi-Chieu-Tien-Do-KH
## Phiên bản: v2.4 — cập nhật 18/08/2026

## Purpose
Đối chiếu báo cáo (đã tổng hợp qua Skill 33) với Kế hoạch cùng kỳ (do hệ **23-KTC-Ke-Hoach/PIS** tạo ra).

## Lưu ý cấp báo cáo — [MỚI v2.4]
Kết quả đối chiếu thường đưa vào phần "Đánh giá chung" của báo cáo **cấp Trường**. Nếu viết thành câu văn (không chỉ bảng số liệu), chủ thể phải là **"Nhà trường"**, không phải tên đơn vị cụ thể — xem `Skill-Tu-hoc-Phong-Cach-Bao-Cao.md` Mục 0.

## Điều kiện tiên quyết — Kiểm tra TRƯỚC KHI thực hiện

**→ Nếu TÌM THẤY Kế hoạch cùng kỳ**: thực hiện đầy đủ theo mục "Nhiệm vụ chính".

**→ Nếu KHÔNG TÌM THẤY**: KHÔNG tự suy diễn. Thông báo và chờ lựa chọn:

```
⚠ Chưa tìm thấy Kế hoạch [kỳ] trong kho dữ liệu.

Anh/chị muốn xử lý thế nào?
  [A] Cung cấp file Kế hoạch ngay → Skill 34 tiếp tục bình thường.
  [B] Xuất "Báo cáo thô" không đối chiếu (gắn cảnh báo nổi bật).
  [C] Dừng chờ hệ ktc-ke-hoach (PIS) tạo Kế hoạch trước.
```

Không tự chọn thay người dùng.

## Nhiệm vụ chính (khi có Kế hoạch)

1. Với mỗi nhiệm vụ KH, tìm trong Báo cáo: **Hoàn thành** / **Chưa HT** / **Không có trong BC**.
2. Nhiệm vụ trong BC không có trong KH → **Phát sinh ngoài kế hoạch**.
   - Ghi chú "Bổ sung ngoài KH quý" hoặc "Kết luận giao ban" → **Phát sinh hợp lệ có nguồn gốc** (không phải lỗi).
3. Nhiệm vụ khó đối chiếu → `[CẦN XÁC NHẬN]`, trình bày 2 phương án.
4. **[MỚI v2.4] Tính tỷ lệ hoàn thành theo từng Trục — ưu tiên dùng % KPI 3 chiều đã tính sẵn từ Skill 33** (hàm `summarize_truc_kpi()` trong `read_bc736_excel.py`, áp dụng khi có Phụ lục IIb/IIc). Đây là số liệu định lượng khách quan — không tự đánh giá định tính khi đã có số này.

## Ràng buộc
- Không đánh giá "tốt/chưa tốt" — chỉ báo tỷ lệ và trạng thái.
- Không suy diễn lý do chưa HT — ghi "chưa rõ lý do".
- Không bỏ sót nhiệm vụ nào trong Kế hoạch.
- **Nếu diễn giải thành câu văn cho báo cáo Trường: chủ thể "Nhà trường", không phải tên đơn vị.**

## Output (khi có KH)
1. Bảng đối chiếu: Trục | Nhiệm vụ KH | Trạng thái | Lý do | Ghi chú.
2. Bảng tỷ lệ % KPI theo Trục (số lượng/chất lượng/tiến độ nếu có từ Skill 33).
3. Danh sách phát sinh ngoài KH (phân loại: hợp lệ có nguồn gốc / chưa rõ nguồn gốc).
4. Phụ lục [CẦN XÁC NHẬN].

## Output (fallback [B])
Báo cáo thô kèm cảnh báo:
```
⚠ CẢNH BÁO: Báo cáo CHƯA đối chiếu Kế hoạch cùng kỳ.
Tỷ lệ hoàn thành và đánh giá tiến độ: KHÔNG CÓ.
Người dùng xác nhận xuất báo cáo thô [B] ngày [DD/MM/YYYY].
```

## PROCESS MEMORY / AUDIT TRAIL — BẮT BUỘC
KTC-RIS không chỉ lưu INPUT và OUTPUT. Mỗi lần thực hiện Skill này phải tạo hoặc bổ sung **Run Record** trong `25-KTC-Bao-Cao/memory`.

Trường tối thiểu: `run_id`; thời gian; kỳ/loại báo cáo; Skill+phiên bản; `sources[]` (tên + Drive File ID/URI); `operations[]`; `decisions[]` (căn cứ+lý do+mức tin cậy); `exceptions[]`; `outputs[]`; `qa[]`; `learning_candidates[]`; `status`.

Chuỗi truy vết bắt buộc: `Source → Evidence → Transformation → Decision → Output → QA`.

`learning_candidates` không tự động thành Skill. Chỉ promote khi có provenance, đã kiểm chứng, không xung đột quy định cao hơn, xác định phạm vi áp dụng và có cơ chế `superseded/deprecated`.

Trước khi tuyên bố hoàn thành phải cập nhật Run Record; nếu không thể ghi thì nêu `PROCESS_MEMORY_NOT_WRITTEN`.

