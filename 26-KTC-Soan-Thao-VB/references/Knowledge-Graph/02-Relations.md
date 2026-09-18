# 02-Relations

## Purpose
Store the relationships between entities, cụ thể hóa cho hệ thống KTC.

## Core relations
- **Legal Document → supports → Internal Regulation**: mỗi quy chế/quy định của Trường phải dẫn chiếu ít nhất một Luật/Nghị định/Thông tư làm căn cứ.
- **Internal Regulation → overrides → general guidance**: khi Trường đã có quy định cụ thể (ví dụ định mức chi tiêu), ưu tiên áp dụng quy định nội bộ trước, miễn không trái luật.
- **Document Type → has → Template**: mỗi loại văn bản có ít nhất một mẫu tương ứng trong `03-Templates`.
- **Document Type → has → Skill (Nhóm B)**: Quyết định↔`07-`, Kế hoạch↔`08-`, Thông báo↔`09-`, Báo cáo↔`10-`, Tờ trình↔`11-`, Công văn↔`12-`, Biên bản↔`13-`.
- **Document Type → has → Checklist**: mỗi loại văn bản kích hoạt bộ checklist tương ứng trong `08-Checklist` (xem `04-Mappings.md`).
- **Business Domain → has → Skill (Nhóm D)**: Đào tạo↔`20-`, Tuyển sinh↔`21-`, Cán bộ↔`22-`, Tài chính↔`23-`, Đảm bảo chất lượng↔`24-`, Cấp Phòng↔`25-`, Đối ngoại↔`26-`.
- **Business Domain → has → Prompt**: mỗi lĩnh vực có prompt nghiệp vụ riêng trong `05-Prompt-Library/08-12`.
- **Prompt → activates → Skill**: prompt xác định ý định, skill thực thi hành vi.
- **Skill → produces → Draft/Review output**: mỗi skill có input/output rõ ràng (xem từng file skill).
- **Skill (Nhóm C) → validates → Draft output**: skill kiểm tra xuyên suốt (14-19) áp dụng cho MỌI loại văn bản, không riêng loại nào.
- **Workflow → sequences → Prompt + Skill usage**: thứ tự sử dụng theo `07-Workflow/01-06`.
- **Checklist → validates → Workflow output**: checklist là cổng kiểm soát trước khi chuyển bước tiếp theo trong workflow.
- **Good Document → supports → style learning (Skill 01, 04)**: văn bản tốt trong `04-Good-Documents` là dữ liệu tham chiếu văn phong cho Skill Soạn thảo và Chuẩn hóa.
- **Role/Authority → signs → Document Type**: xác định bởi `17-Skill-Kiem-Tra-Tham-Quyen.md`, tham chiếu quy chế làm việc trong `02-KTC-Regulations`.
- **Use Case → chains → multiple Skills**: một use case thực tế thường gọi tuần tự nhiều skill (xem `05-Use-Cases.md`).
