# PM-20260826-Cap-nhat-He-v2.16
## Process Memory — Cập nhật KTC-Ra-Soat-897-v2-Cai-tien lên v2.16

```yaml
memory_id: PM-20260826-SYSTEM-v2.16
created_at: 2026-08-26T13:42:00+07:00
memory_type: process
status: closed
task_type: system_update
project_name: KTC-Ra-Soat-897-v2-Cai-tien
target_version: v2.16
previous_version: v2.14
```

## 1. Nguồn cập nhật
- `LENH-CAP-NHAT-v2.16-26082026.md`
- `Bao_cao_dieu_chinh_He_v2.16_26082026.docx`
- Trạng thái thực tế Google Drive ngày 26/8/2026.

## 2. Trạng thái thực tế đã kiểm chứng
- Thư mục gốc có `ktc-ra-soat-897-v2.16.skill`.
- `SKILL.md` ghi v2.16.
- `00-README.md` ghi v2.16.
- Nhật ký cập nhật là v1.4, ngày 26/8/2026, đồng bộ theo v2.16.
- `MEMORY-INDEX.md` cập nhật 26/8/2026 (v2.16).
- `references/Skill-Library/` của KTC-Ra-Soat-897 có `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md` và `00b-Trigger-Vien-Dan-Van-Ban-Hop-Nhat.md`.
- Thư mục gốc không còn `ktc-ra-soat-897-v2.14.skill`; việc xóa bản cũ nêu là “còn tồn” trong lệnh cập nhật đã được xử lý thực tế.

## 3. Quy tắc mới bắt buộc từ v2.16
Khi đầu vào hoặc yêu cầu chứa `hợp nhất`, `văn bản hợp nhất`, `VBHN` hoặc `hợp nhất tại Văn bản hợp nhất số` thì phải đọc trigger, sau đó đọc Skill viện dẫn VBHN trước khi viết hoặc đánh giá căn cứ pháp lý/viện dẫn/trích dẫn liên quan.

## 4. Nội dung Skill viện dẫn VBHN phải nhớ
- Áp dụng khi văn bản pháp luật đã có VBHN chính thức do cơ quan có thẩm quyền xác thực.
- Viện dẫn theo đúng 5 trường hợp a–đ của Skill.
- Không coi VBHN là văn bản pháp luật mới.
- Không tự chế cách viện dẫn; phải kiểm tra đúng số hiệu VBHN.
- Nếu viện dẫn phần/chương/mục/điều/khoản/điểm thì dùng số thứ tự trong VBHN.
- Mức 1: văn bản hết hiệu lực toàn bộ hoặc số hiệu VBHN sai/không tồn tại.
- Mức 2: thiếu cụm ngoặc đơn theo mẫu hoặc số điều khoản không khớp VBHN.
- Mức 3: nội dung đúng nhưng thứ tự trình bày gốc/VBHN không đúng mẫu.

## 5. Thay đổi kiến trúc
Không tồn tại một Skill-Library dùng chung duy nhất cho 5 hệ. Mỗi hệ giữ bản sao riêng của Skill/trigger tại vị trí của chính hệ đó. Không dùng `KTC-DIS-v1/06-Skill-Library/` vì đó là legacy.

## 6. Phạm vi đã hoàn thành
- KTC-Ra-Soat-897: hoàn thành đầy đủ v2.16, SKILL.md dẫn chiếu tường minh, gói `.skill` đã có trên Drive.
- 4 hệ khác: theo tài liệu cập nhật, file vật lý đã có; SKILL.md riêng chưa được dẫn chiếu tường minh.

## 7. Supersession
- v2.14 → superseded_by: v2.16 (26/8/2026).
- Giả định `KTC-DIS-v1/06-Skill-Library/` là kho dùng chung → superseded.
- Không sử dụng script cũ `build_tcdm_review_fixed.py`.

## 8. CONFLICT / chênh lệch trạng thái
Không có CONFLICT về phiên bản Hệ.
Chênh lệch đã xử lý: lệnh cập nhật ghi “còn tồn: xóa v2.14”, nhưng kiểm tra trực tiếp thư mục gốc ngày 26/8/2026 cho thấy v2.14 không còn. Trạng thái hiện hành: việc xóa bản cũ đã hoàn tất.

## 9. Quyết định vận hành
Từ sau bản ghi này, KTC-Ra-Soat-897 coi v2.16 là phiên bản hiện hành. Trigger VBHN là bắt buộc. Mỗi rà soát chính thức tiếp tục phải ghi Process Memory.

## 10. Next action
- Giám sát ca rà soát thực tế đầu tiên có từ khóa VBHN để xác nhận trigger hoạt động end-to-end.
- Khi có phiên riêng phụ trách 4 hệ còn lại, bổ sung dẫn chiếu tường minh trong SKILL.md tương ứng.
