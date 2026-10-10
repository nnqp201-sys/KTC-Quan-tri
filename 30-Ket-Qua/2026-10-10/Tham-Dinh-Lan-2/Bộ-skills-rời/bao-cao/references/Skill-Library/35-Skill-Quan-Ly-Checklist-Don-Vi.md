# 35-Skill-Quan-Ly-Checklist-Don-Vi
## Phiên bản: v1.0 — tạo mới 12/08/2026

## Purpose
Tạo và duy trì danh sách kiểm soát (Checklist) đơn vị phải nộp báo cáo theo từng kỳ — theo dõi trạng thái từ "Chưa nộp" đến "Hoàn tất", phát hiện chủ động đơn vị thiếu trước khi bước Tổng hợp (Skill 33) bị gián đoạn.

## Khi nào dùng
- **Bắt buộc** tại Bước 0 (đầu kỳ): tạo Checklist trống trước khi mở cổng tiếp nhận.
- **Cập nhật liên tục** tại Bước 1 (tiếp nhận), Bước 2 (kiểm tra), Bước 3 (tổng hợp).
- **Chốt và lưu** tại Bước 7 (kết thúc kỳ).

## Nhiệm vụ

### Tác vụ A — Tạo Checklist đầu kỳ
Yêu cầu người dùng cung cấp:
1. Kỳ báo cáo (VD: Tháng 7/2026 / Quý III/2026 / 6 tháng đầu năm 2026).
2. Danh sách đơn vị bắt buộc nộp kỳ này (tên Phòng/Khoa/Trung tâm).
3. Hạn chót nộp (deadline).

Tạo bảng Checklist với cấu trúc chuẩn (xem mục Format bên dưới).

### Tác vụ B — Cập nhật trạng thái
Khi nhận thông tin "Đơn vị X đã nộp" hoặc kết quả từ Skill 32:
- Cập nhật cột "Trạng thái" theo thang 4 mức: `Chưa nộp` → `Đã nộp` → `Đã kiểm tra` → `Vấn đề`.
- Ghi cột "Ghi chú" nếu có vấn đề (thiếu cột, sai mẫu, không rõ Trục...).
- Không tự đánh dấu "Đã kiểm tra" nếu chưa qua Skill 32.

### Tác vụ C — Báo cáo tình trạng tức thời
Khi được hỏi "tình trạng nộp báo cáo đến nay" hoặc trước khi chạy Skill 33:
- Tổng hợp: X/N đơn vị đã nộp · Y đã kiểm tra · Z có vấn đề · W chưa nộp.
- Liệt kê cụ thể tên đơn vị chưa nộp — đây là dữ liệu Skill 33 cần để ghi "chưa nộp" trong báo cáo.
- Cảnh báo nếu deadline đã qua mà còn đơn vị chưa nộp.

### Tác vụ D — Checklist kết thúc kỳ (Bước 7)
Sau khi xuất .docx:
- Tổng kết toàn kỳ: số đơn vị hoàn thành / vấn đề còn tồn.
- Liệt kê file gốc trong `11-Input` và `13-Unit-Reports` cần xóa thủ công (kèm đường dẫn cụ thể).
- Liệt kê link đến toàn bộ file output của kỳ: Báo cáo tổng hợp / Bảng đối chiếu / Phụ lục / Checklist.

## Ràng buộc
- Không tự thêm hoặc bỏ đơn vị khỏi danh sách bắt buộc — chỉ người dùng mới được điều chỉnh.
- Không tự đánh dấu "Đã kiểm tra" khi chưa có kết quả Skill 32 xác nhận.
- Nếu deadline đã qua mà đơn vị chưa nộp — đánh dấu `Trễ hạn`, không tự loại khỏi danh sách.

## Format Checklist chuẩn

```
# Checklist Báo cáo — [Kỳ] — Hạn chót: [DD/MM/YYYY]
Tạo: [YYYY-MM-DD] | Cập nhật lần cuối: [YYYY-MM-DD HH:MM]

| # | Đơn vị | Trạng thái | Ngày nộp | Ghi chú Skill 32 | Ghi chú tổng hợp |
|---|--------|-----------|----------|------------------|-----------------|
| 1 | Phòng TH-HC&QT | Đã kiểm tra | 05/08/2026 | Đủ mẫu, 12 NV | — |
| 2 | Phòng TC-KT | Đã nộp | 06/08/2026 | Chờ Skill 32 | — |
| 3 | Khoa Kinh tế | Vấn đề | 04/08/2026 | Thiếu cột Hệ số | Cần bổ sung |
| 4 | TT Ngoại ngữ | Chưa nộp | — | — | Trễ hạn |

## Tổng kết tức thời
- Đã kiểm tra: 1/4 (25%)
- Đã nộp (chờ KT): 1/4
- Có vấn đề: 1/4
- Chưa nộp: 1/4 ⚠ Trễ hạn
```

## Output
File `Checklist-Don-Vi-[Ky]-[YYYY-MM-DD].md` — lưu vào `30-Ket-Qua/[YYYY-MM-DD]/checklist/`.
Cập nhật in-place (tạo phiên bản mới cùng ngày nếu có thay đổi lớn).

## PROCESS MEMORY / AUDIT TRAIL — BẮT BUỘC
KTC-RIS không chỉ lưu INPUT và OUTPUT. Mỗi lần thực hiện Skill này phải tạo hoặc bổ sung **Run Record** trong `25-KTC-Bao-Cao/memory`.

Trường tối thiểu: `run_id`; thời gian; kỳ/loại báo cáo; Skill+phiên bản; `sources[]` (tên + Drive File ID/URI); `operations[]`; `decisions[]` (căn cứ+lý do+mức tin cậy); `exceptions[]`; `outputs[]`; `qa[]`; `learning_candidates[]`; `status`.

Chuỗi truy vết bắt buộc: `Source → Evidence → Transformation → Decision → Output → QA`.

`learning_candidates` không tự động thành Skill. Chỉ promote khi có provenance, đã kiểm chứng, không xung đột quy định cao hơn, xác định phạm vi áp dụng và có cơ chế `superseded/deprecated`.

Trước khi tuyên bố hoàn thành phải cập nhật Run Record; nếu không thể ghi thì nêu `PROCESS_MEMORY_NOT_WRITTEN`.

