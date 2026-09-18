# 04-Mappings

## Purpose
Store direct mappings between tasks/document types and system assets (skill, prompt, checklist, template, workflow).

## Mapping theo loại văn bản (Document Type)
| Document Type | Skill (Nhóm B) | Prompt | Checklist chính | Template |
|---|---|---|---|---|
| Quyết định | `07-` | `01-Soan-Thao`, `02-Ra-Soat` | `03-Phap-Ly`, `01-The-Thuc` | `03-Templates/03-01,02-` |
| Kế hoạch | `08-` | `01-`, `06-Tao-Dan-Y` | `02-Noi-Dung` (+ `15-Kiem-Tra-Logic`) | `03-Templates/03-04,05-` |
| Thông báo | `09-` | `01-` | `01-The-Thuc`, `04-Ngon-Ngu` | `03-Templates/03-03-` |
| Báo cáo | `10-` | `06-`, `04-Trich-Xuat` | `02-Noi-Dung` | `03-Templates/03-06-` |
| Tờ trình | `11-` | `01-` | `03-Phap-Ly` | `03-Templates/03-07-` |
| Công văn | `12-` | `01-`, `05-So-Sanh` | `04-Ngon-Ngu` | `03-Templates/03-08-` |
| Biên bản | `13-` | `01-`, `04-Trich-Xuat` | `01-The-Thuc` | `03-Templates/03-09-` |

## Mapping theo Business Domain
| Domain | Skill (Nhóm D) | Prompt |
|---|---|---|
| Đào tạo | `20-` | `05-Prompt-Library/08-Nghiep-Vu-Dao-Tao.md` |
| Tuyển sinh | `21-` | `09-Nghiep-Vu-Tuyen-Sinh.md` |
| Tổ chức - Cán bộ | `22-` | `10-Nghiep-Vu-Can-Bo.md` |
| Tài chính - Kế toán | `23-` | `11-Nghiep-Vu-Tai-Chinh.md` |
| Đảm bảo chất lượng | `24-` | (chưa có prompt riêng — dùng `06-Tao-Dan-Y` + `24-`) |
| Cấp Phòng/Khoa | `25-` | (dùng prompt chung `01-`, `02-`) |
| Đối ngoại | `26-` | (dùng prompt chung `01-`, `05-So-Sanh`) |
| HSSV | (chưa có skill riêng — dùng `09-`, `25-`) | `12-Nghiep-Vu-HSSV.md` |

## Mapping theo tác vụ (Task → Pipeline)
- Soạn mới → `05-Phan-Tich-Yeu-Cau` → Skill Nhóm B/D phù hợp → `01-Soan-Thao` → `02-`/`14-` → `03-` → `04-Chuan-Hoa` → `16-`/`17-` → `19-`
- Rà soát văn bản có sẵn → `02-`, `14-`, `03-`, `15-` (nếu là Kế hoạch/Đề án), `18-` → `19-`
- Chuẩn hóa văn phong → `04-Skill-Chuan-Hoa-Van-Ban`
- Trích xuất thông tin từ văn bản dài → `06-Skill-Tong-Hop-Noi-Dung`
- So sánh nhiều bản dự thảo → Prompt `05-So-Sanh` + `19-Skill-Danh-Gia-Chat-Luong-Van-Ban`
