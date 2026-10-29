# PM-20260825-Cap-nhat-He-v2.14
## Process Memory — Cập nhật Hệ KTC-Ra-Soat-897-v2-Cai-tien lên v2.14

```yaml
memory_id: PM-20260825-SYSTEM-v2.14
created_at: 2026-08-25T22:57:00+07:00
memory_type: process
status: closed
task_type: system_update
project_name: KTC-Ra-Soat-897-v2-Cai-tien
target_version: v2.14
previous_version: v2.13
```

## 1. Yêu cầu cập nhật
Người dùng yêu cầu cập nhật Hệ KTC-Ra-Soat-897 lên phiên bản v2.14 ngày 25/8/2026 và ghi nhớ các thay đổi vận hành bắt buộc.

## 2. Trạng thái thực tế đã kiểm tra trên Google Drive
- Gói hiện hành tại thư mục gốc: `ktc-ra-soat-897-v2.14.skill`.
- `SKILL.md`: v2.14.
- `00-README.md`: v2.14.
- Nhật ký cập nhật: tài liệu v1.3, ngày 25/8/2026, đồng bộ theo `ktc-ra-soat-897-v2.14.skill`.
- `MEMORY-INDEX.md`: cập nhật 25/8/2026, trạng thái Hệ v2.14.
- Script duy nhất trong `tools/`: `build_ktc897_report.py`; script `build_tcdm_review_fixed.py` không còn trong thư mục `tools/`.

## 3. Điểm nạp bắt buộc đầu mỗi phiên
1. `09-Quan-Tri-He/10-Bo-Nho-He/MEMORY-INDEX.md`
2. Nhật ký cập nhật mới nhất trong `09-Quan-Tri-He/`
3. `SKILL.md`
4. `references/Checklist/08-Quy-Uoc-Rieng-CDKT.md`
5. Sau đó xác nhận phiên bản và trạng thái sẵn sàng.

## 4. Thay đổi vận hành v2.14 phải nhớ
1. Script chính duy nhất: `tools/build_ktc897_report.py` v3.0.
2. `build_tcdm_review_fixed.py` đã bị loại bỏ hoàn toàn — không gọi, không tham chiếu.
3. Bộ nhớ vận hành nằm tại `09-Quan-Tri-He/10-Bo-Nho-He/`, không nằm ở thư mục gốc.
4. Sau mỗi ca rà soát chính thức phải tạo Process Memory theo `02-Mau-Process-Memory.md`, đặt tại `03-Process-Memory/`.
5. Thứ tự ưu tiên nguồn 7 lớp; không dùng lớp 5–7 ghi đè lớp 1–4.
6. NĐ 60/2021/NĐ-CP luôn tra cùng NĐ 111/2025/NĐ-CP khi liên quan.
7. Khi trích số hiệu văn bản nội bộ phải kèm ngày ban hành; đặc biệt 1229 và 1299 là hai văn bản khác nhau.
8. Định mức thiết bị tính gộp một lần trên toàn Trường, không làm tròn lẻ từng đơn vị rồi cộng.
9. Kho `03-Templates` có thể chứa văn bản thật, không được mặc định coi là mẫu trống.
10. Khi tạo bảng trong báo cáo bằng python-docx: bắt buộc `autofit=False` + `w:tblLayout type="fixed"` + đặt `w:w` trên từng `w:gridCol`.
11. Tổng chiều rộng bảng không vượt quá 25,7 cm.
12. Kiểm tra file thực tế trên Drive trước khi coi phiên bản là chính thức; nếu 4 tài liệu điều khiển không đồng bộ thì gắn `CONFLICT`, không tự hợp nhất.

## 5. Bốn điểm kiểm tra phiên bản
- SKILL.md: ghi v2.14.
- 00-README.md: ghi v2.14.
- Nhật ký: bản tài liệu v1.3 nhưng ghi rõ đồng bộ theo v2.14 và file Skill hiện hành v2.14.
- MEMORY-INDEX.md: ghi v2.14.

Kết luận: KHÔNG có CONFLICT về phiên bản Hệ. Số `v1.3` của Nhật ký là phiên bản riêng của tài liệu Nhật ký, không phải phiên bản của Hệ.

## 6. Phạm vi thao tác
- Đã xác minh và đồng bộ ngữ cảnh vận hành của Hệ theo Drive v2.14.
- Không thể thao tác trực tiếp trên Claude.ai để Upload Skill hoặc gỡ Skill v2.13 từ môi trường ChatGPT này. Người vận hành Claude phải thực hiện bước cài/gỡ trên Claude.ai.
- Kết nối Google Drive trong phiên ChatGPT hiện tại đã đọc được thư mục KTC-Ra-Soat-897-v2-Cai-tien; quyền trên Claude phải được người vận hành kiểm tra riêng.

## 7. Quyết định
Từ thời điểm này, mọi tác vụ KTC-Ra-Soat-897 trong Project phải coi v2.14 là phiên bản hiện hành và dùng các quy tắc trên, trừ khi Drive xuất hiện phiên bản mới hơn đã được kiểm chứng.

## 8. Supersession
- `ktc-ra-soat-897-v2.13.skill` → superseded_by: `ktc-ra-soat-897-v2.14.skill` (25/8/2026)
- `build_tcdm_review_fixed.py` → superseded_by: `build_ktc897_report.py v3.0` (25/8/2026)

## 9. Nguồn kiểm chứng
- Google Drive thư mục gốc `KTC-Ra-Soat-897-v2-Cai-tien/`
- `SKILL.md` v2.14
- `00-README.md` v2.14
- `Nhat-Ky-Cap-Nhat-KTC-Ra-Soat-897-v2.md` v1.3 / đồng bộ v2.14
- `MEMORY-INDEX.md` v2.14
- `tools/build_ktc897_report.py`

## 10. Next action
Áp dụng v2.14 cho ca rà soát tiếp theo; sau mỗi rà soát chính thức phải tạo Process Memory mới.
