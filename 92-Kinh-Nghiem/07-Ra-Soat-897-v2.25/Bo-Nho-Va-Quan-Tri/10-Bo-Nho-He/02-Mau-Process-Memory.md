# 02-Mau-Process-Memory — KTC-Ra-Soat-897-v2
## Mẫu ghi nhớ quá trình cho mỗi ca rà soát/so sánh/chuẩn hóa

> Mỗi ca quan trọng tạo 01 bản sao của mẫu này. Không ghi đè bản ghi cũ.

```yaml
memory_id: PM-YYYYMMDD-XXX
created_at: YYYY-MM-DDTHH:MM:SS+07:00
memory_type: process
status: open | closed | superseded
task_type: formal_review | quick_review | compare | standardize
document_type:
document_title:
draft_version:
responsible_unit:
scope:
project_name: KTC-Ra-Soat-897-v2-Cai-tien

input_files:
  - name:
    drive_id_or_link:
    version_or_date:
    role:

control_versions:
  skill_package:
  skill_md:
  checklist_08:
  other_checklists:
  prompt:
  script:
  template:

sources_verified:
  - source:
    status: verified | unverified | superseded
    checked_at:
    note:

process_steps:
  - step:
    action:
    result:
    evidence:

key_findings:
  - id:
    location:
    issue:
    level:
    basis:
    recommendation:
    status: open | fixed | partially_fixed | rejected

user_feedback:
  - time:
    feedback:
    effect_on_result:
    promoted_to_lesson: false

decisions:
  - decision:
    reason:
    evidence:
    made_by: AI | user | approved_source

outputs:
  - name:
    drive_id_or_link:
    version:
    status:

unresolved_items:
  - item:
    reason:
    needed_evidence:

lessons:
  - issue:
    correction:
    scope:
    approval_status: proposed | confirmed | incorporated

supersedes:
superseded_by:
next_action:
```

## Hướng dẫn ghi

### 1. Không chỉ ghi “đã rà soát”
Phải ghi các bước có giá trị tái lập, ví dụ:
- đã tra Checklist 08 trước;
- đã kiểm tra hiệu lực văn bản;
- đã so sánh tên cơ sở với nguồn chuẩn;
- đã đối chiếu bản sau sửa với báo cáo vòng trước.

### 2. Ghi cả quyết định “không nêu lỗi”
Ví dụ: “Dự thảo chưa có số — không ghi lỗi vì chưa đến bước cấp số”.
Đây là Process Memory quan trọng để Hệ không lặp lại lỗi đánh giá ở lần sau.

### 3. Ghi phản hồi người dùng
Nếu người dùng nói “phân loại sai”, không chỉ sửa kết quả cuối:
- ghi phản hồi;
- xác định căn cứ;
- sửa phạm vi;
- đề xuất nâng thành Lesson;
- chỉ cập nhật quy tắc chung khi đã được xác nhận.

### 4. Ghi xung đột
Ví dụ: Nhật ký ghi v2.12 nhưng Drive chỉ thấy v2.11.
Phải ghi cả hai, kiểm tra rồi mới kết luận trạng thái.

### 5. Kết thúc
Khi tác vụ hoàn thành:
- đổi `status: closed`;
- điền output;
- điền unresolved;
- điền next_action;
- nếu có bản sau thì dùng `superseded_by`, không xóa file cũ.
