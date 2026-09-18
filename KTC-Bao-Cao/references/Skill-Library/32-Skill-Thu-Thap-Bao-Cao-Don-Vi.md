# 32-Skill-Thu-Thap-Bao-Cao-Don-Vi
## Phiên bản: v2.5 — cập nhật 14/9/2026

## Purpose
Kiểm tra báo cáo công tác định kỳ (tháng/quý/6 tháng/năm) do từng Phòng/Khoa/Trung tâm nộp — đủ mẫu, đủ kỳ, gắn đúng Trục/Nội hàm, **đúng công thức KPI** — trước khi đưa vào bước tổng hợp cấp Trường.

## Khi nào dùng
Khi có 1 hoặc nhiều báo cáo đơn vị mới nộp (qua kho `13-Unit-Reports` hoặc đính kèm trực tiếp), cần kiểm tra trước khi tổng hợp.

## Định dạng bắt buộc — Excel Phụ lục TB736 (xem `31-Skill-Phu-Luc-TB736-Excel.md`)
Đơn vị nộp báo cáo/kế hoạch **phải ở định dạng Excel** đúng 1 trong 4 mẫu:
- **Ia** (KH Quý) / **Ib** (KH Tháng) — 11 cột, KHÔNG có KPI.
- **IIb** (KQ Tháng) / **IIc** (KQ Quý) — 16 cột, **CÓ** hệ thống KPI 3 chiều.

## [SỬA v2.5] Mỗi đơn vị nộp HAI tệp — phải thu đủ cả hai

Quy định cũ ghi *"không nhận văn bản tường thuật tự do thay cho Excel Phụ lục"* — **diễn đạt này gây hiểu
sai và đã dẫn đến bỏ sót dữ liệu thật.** Bản tường thuật không phải "tự do": nó là **Phụ lục IIa**, một
biểu mẫu chính thức, và là **nguồn duy nhất của văn phong**.

| Tệp | Mẫu | Vai trò | Thiếu thì hỏng gì |
|---|---|---|---|
| `.docx` | **Phụ lục IIa** — báo cáo tường thuật | Nguồn **văn tường thuật** cho Phần I/II/III của báo cáo Trường. Đơn vị đã chia sẵn theo 6 Trục, có mục Nghị quyết và mục Đánh giá chung | Phải tự ghép văn từ cột "Nội dung công việc" của bảng → **văn rời rạc, không thành câu** |
| `.xlsx` | **Phụ lục IIb/IIc** — bảng nhiệm vụ | Nguồn **số liệu**: sản phẩm, số lượng, điểm chấm, hệ số, KPI | Không tính được KPI |

**Quy tắc bắt buộc:** đếm **số loại tệp** mỗi đơn vị nộp trước khi đọc. Đơn vị nộp thiếu một trong hai →
ghi vào Checklist (Skill 35) là **nộp thiếu**, không coi là đã nộp đủ.

**Tiền lệ:** kỳ tháng 8/2026 có 13 tệp `.docx` và 27 tệp `.xlsx`; đợt tổng hợp đầu chỉ đọc `.xlsx`, bỏ sót
toàn bộ **198 ý kết quả** và **130 ý kế hoạch** đã viết thành văn trong `.docx`.

Điều **vẫn giữ nguyên**: không nhận bảng nhiệm vụ ở dạng văn xuôi thay cho Excel Phụ lục IIb/IIc.

## Nhiệm vụ

1. Kiểm tra đúng mẫu theo loại file (Ia/Ib/IIb/IIc), đủ cột theo bảng ở mục "Định dạng bắt buộc".
2. Kiểm tra đủ kỳ báo cáo (đúng tháng/quý/6 tháng/năm đang yêu cầu).
3. Với mỗi nhiệm vụ, xác định đúng 1 trong 6 Trục kết quả trọng tâm + Nội hàm cụ thể (dùng `30-Skill-Phan-Loai-6-Truc.md`).
4. Phát hiện nhiệm vụ không rõ Trục/Nội hàm — đánh dấu `[CẦN XÁC ĐỊNH LẠI]`, không tự đoán.
5. **Kiểm tra công thức KPI cascade** (chỉ áp dụng Phụ lục IIb/IIc):

```
Hệ số quy đổi          = Điểm chấm × 1%
Số lượng quy đổi        = Số lượng × Hệ số
KPI số lượng (TT)       = Số lượng × [Tỷ lệ hoàn thành khối lượng]
KPI số lượng (QĐ)       = Hệ số × KPI số lượng (TT)
KPI chất lượng (TT)     = KPI số lượng (TT) × [Tỷ lệ hoàn thành chất lượng]
KPI chất lượng (QĐ)     = Hệ số × KPI chất lượng (TT)
KPI tiến độ (TT)        = KPI số lượng (TT) × [Tỷ lệ hoàn thành tiến độ]
KPI tiến độ (QĐ)        = Hệ số × KPI tiến độ (TT)
```

Nếu số liệu đơn vị nộp lệch công thức trên (sai số > làm tròn hợp lý) → đánh dấu `[SAI CÔNG THỨC KPI]` tại dòng đó, nêu rõ giá trị đúng theo công thức để đơn vị đối chiếu — **không tự sửa số liệu đơn vị đã nộp**.

Dùng script `read_bc736_excel.py` (hàm `read_appendix()`) để tự động đọc file và phát hiện sai công thức, thay vì rà tay từng dòng.

6. **Kiểm tra cột Ghi chú** (chỉ áp dụng Phụ lục Ia/Ib):
   - Giá trị hợp lệ: **"Đưa vào KH Trường"** hoặc **"Thường xuyên của đơn vị"**.
   - Dòng nào bỏ trống cột này → đánh dấu `[CẦN XÁC ĐỊNH: Đưa vào KH Trường hay không?]`, không tự suy đoán — vì đây là căn cứ để Skill 33 quyết định lọc nhiệm vụ lên báo cáo Trường.

## Ràng buộc
- Không tự sửa nội dung báo cáo của đơn vị — chỉ kiểm tra và gắn nhãn Trục/Nội hàm.
- Không tự tính điểm chấm công việc nếu đơn vị chưa xác định mức độ khó/phức tạp.
- Không tự sửa số liệu KPI dù phát hiện sai công thức — chỉ nêu giá trị đúng để đơn vị tự điều chỉnh.
- Nếu báo cáo thiếu cột bắt buộc, liệt kê rõ thiếu gì, không tự điền.
- Đây là báo cáo **cấp đơn vị** — chủ thể là tên đơn vị đó, không đổi sang "Nhà trường" (khác Skill 33 ở cấp Trường).

## Output
Bảng: Nhiệm vụ | Trục/Nội hàm gán | Đủ mẫu? | KPI đúng công thức? | Ghi chú Trường/Đơn vị | Vấn đề (nếu có).

## PROCESS MEMORY / AUDIT TRAIL — BẮT BUỘC
KTC-RIS không chỉ lưu INPUT và OUTPUT. Mỗi lần thực hiện Skill này phải tạo hoặc bổ sung **Run Record** trong `KTC-Bao-Cao/memory`.

Trường tối thiểu: `run_id`; thời gian; kỳ/loại báo cáo; Skill+phiên bản; `sources[]` (tên + Drive File ID/URI); `operations[]`; `decisions[]` (căn cứ+lý do+mức tin cậy); `exceptions[]`; `outputs[]`; `qa[]`; `learning_candidates[]`; `status`.

Chuỗi truy vết bắt buộc: `Source → Evidence → Transformation → Decision → Output → QA`.

`learning_candidates` không tự động thành Skill. Chỉ promote khi có provenance, đã kiểm chứng, không xung đột quy định cao hơn, xác định phạm vi áp dụng và có cơ chế `superseded/deprecated`.

Trước khi tuyên bố hoàn thành phải cập nhật Run Record; nếu không thể ghi thì nêu `PROCESS_MEMORY_NOT_WRITTEN`.

