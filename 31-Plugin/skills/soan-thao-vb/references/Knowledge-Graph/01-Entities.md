# 01-Entities

## Purpose
Store the key objects (entities) in the hệ thống KTC system, with concrete instances relevant to Trường Cao đẳng Kon Tum (KTC).

## Entity types

### 1. Legal Document (Văn bản pháp luật)
Instances: Luật Giáo dục nghề nghiệp, Luật Giáo dục, Luật Viên chức, Luật Ban hành VBQPPL, Nghị định 30/2020/NĐ-CP, Nghị định 111, Thông tư của Bộ Nội vụ/Bộ GDĐT/Bộ LĐTBXH, Chỉ thị 21-CT/TW, Nghị quyết 71-NQ/TW.
Source folder: `01-Legal-Database`.

### 2. Provincial Document (Văn bản của tỉnh)
Instances: Quy chế làm việc UBND tỉnh, quy định phân cấp, quy định quản lý tài sản/tài chính, kế hoạch/chương trình của UBND tỉnh.
Source folder: `01-Legal-Database` (nhóm văn bản tỉnh) và `02-KTC-Regulations` (khi Trường ban hành kế hoạch triển khai văn bản tỉnh).

### 3. Internal Regulation (Quy chế/Quy định nội bộ Trường)
Instances: Quy chế tổ chức hoạt động, quy chế làm việc, quy chế chi tiêu nội bộ, quy chế dân chủ, quy chế văn thư, quy định/quy trình ISO, quy định trình ký, quy định ban hành văn bản, quy định lưu trữ.
Source folder: `02-KTC-Regulations`.

### 4. Document Type (Loại văn bản)
Instances: Quyết định (quy phạm / cá biệt), Kế hoạch (chiến lược/trung hạn/năm/quý/tháng/chuyên đề), Thông báo, Báo cáo (định kỳ/chuyên đề/giải trình), Tờ trình, Công văn, Biên bản, Giấy mời, Chương trình, Quy chế, Quy định, Đề án, Báo cáo tổng kết, Tham luận.

### 5. Template (Mẫu văn bản)
Source folder: `03-Templates`, tổ chức theo từng Document Type con (ví dụ `03-01-`, `03-03-`, `03-04-`...).

### 6. Good Document (Văn bản mẫu chất lượng)
Source folder: `04-Good-Documents` — dùng để học văn phong, cấu trúc, cách diễn đạt, phong cách điều hành của Ban Giám hiệu Trường.

### 7. Prompt
Source folder: `05-Prompt-Library` — 12 nhóm hiện có (soạn thảo, rà soát, chuẩn hóa, trích xuất, so sánh, tạo dàn ý, và 5 nhóm nghiệp vụ: đào tạo, tuyển sinh, cán bộ, tài chính, HSSV).

### 8. Skill
Source folder: `06-Skill-Library` — 26 skill, 4 nhóm (Core, Theo loại văn bản, Kiểm tra xuyên suốt, Nghiệp vụ). Xem `06-Skill-Library/27-Metadata.md`.

### 9. Workflow Step
Source folder: `07-Workflow` — Soạn thảo → Rà soát → Trình ký → Ban hành → Lưu trữ → Cập nhật.

### 10. Checklist
Source folder: `08-Checklist` — Thể thức, Nội dung, Pháp lý, Ngôn ngữ, Hình thức.

### 11. Role / Authority (Chức danh / Thẩm quyền)
Instances: Hiệu trưởng, Phó Hiệu trưởng (theo lĩnh vực phụ trách), Trưởng phòng/Khoa/Trung tâm, Hội đồng trường, Hội đồng khoa học và đào tạo.

### 12. Business Domain (Lĩnh vực nghiệp vụ)
Instances: Đào tạo, Tuyển sinh, Tổ chức - Cán bộ, Tài chính - Kế toán, Đảm bảo chất lượng, Đối ngoại - Hợp tác, Hành chính - Văn thư (cấp Phòng).

### 13. User Request (Yêu cầu người dùng)
Đầu vào tự nhiên từ người dùng — điểm khởi đầu của toàn bộ pipeline, được xử lý bởi `06-Skill-Library/05-Skill-Phan-Tich-Yeu-Cau.md`.
