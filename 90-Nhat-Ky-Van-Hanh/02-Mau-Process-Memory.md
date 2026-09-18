# Mẫu Process Memory — KTC-Quan-tri

> Mỗi ca quan trọng tạo 01 bản sao của mẫu này, lưu tại `03-Process-Memory/PM-YYYYMMDD-[Ten-ca].md`.
> **Không ghi đè bản ghi cũ.** Có bản sau thì dùng `superseded_by`, giữ nguyên tệp cũ.

```yaml
memory_id: PM-YYYYMMDD-NNN
created_at: YYYY-MM-DDTHH:MM:SS+07:00
memory_type: process
status: open | closed | superseded
task_type: chuan_hoa_cap_ma | theo_doi_canh_bao | doi_chieu_ba_he | chot_ky_bao_cao | kpi_xep_loai
ky:                          # Tháng 8/2026 · Quý III/2026 · Năm 2026
scope:                       # phạm vi đơn vị, số tệp
project_name: KTC-Quan-tri

input_files:
  - name:
    version_or_date:
    role:

control_versions:
  skill_package:             # ktc-quan-tri.skill vX.Y
  bang_ma_don_vi:
  master_task_register:

sources_verified:
  - source:
    status: verified | unverified | superseded
    note:

process_steps:
  - step:
    action:
    result:

key_findings:
  - id:
    location:
    issue:
    hệ_quả:
    status: open | fixed | partially_fixed | rejected

decisions:
  - decision:
    reason:
    made_by: AI | user | approved_source

outputs:
  - name:
    status:

unresolved_items:
  - item:
    needed_evidence:

lessons:
  - issue:
    correction:
    scope:
    approval_status: proposed | confirmed | incorporated
    lesson_ref:                # LL-YYYYMMDD-NNN nếu đã nâng thành Lesson

supersedes:
superseded_by:
next_action:
```

## Năm hướng dẫn ghi

### 1. Không chỉ ghi "đã làm xong"

Ghi các bước **có giá trị tái lập**: đã đọc nguồn nào, ánh xạ đơn vị bằng bảng nào, loại dòng tiêu đề ra
sao, dùng khóa nối nào để đối chiếu.

### 2. Ghi cả quyết định "không kết luận"

Ví dụ: *"7 nhiệm vụ không tìm thấy trong báo cáo — không kết luận là chưa thực hiện, vì đối chiếu chỉ ở
mức gần đúng"*. Đây là loại ghi chép quan trọng nhất, giúp lần sau không lặp lại kết luận vội.

### 3. Ghi phản hồi người dùng

Nếu người dùng nói "chỗ này sai": ghi phản hồi → xác định căn cứ → sửa phạm vi → đề xuất nâng thành Lesson.
Chỉ cập nhật quy tắc chung sau khi đã xác nhận.

### 4. Ghi xung đột giữa hai nguồn

Ví dụ: *"Tên tệp ghi ngày 29/8 nhưng văn bản ghi ngày 30/8"*. Ghi **cả hai**, nêu rõ đã lấy theo nguồn nào
và vì sao — không lặng lẽ chọn một bên.

### 5. Khi kết thúc

Đổi `status: closed` · điền `outputs` · điền `unresolved_items` · điền `next_action`. Nếu bài học đủ khái
quát để dùng cho ca khác, nâng thành `92-Kinh-Nghiem/01-Lessons-Learned/LL-YYYYMMDD-NNN.md` và ghi liên kết
hai chiều.
