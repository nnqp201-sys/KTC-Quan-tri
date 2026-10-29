# False-Positive — Trường hợp Hệ báo sai đã ghi nhận

> **Cách dùng**: đây là tầng BẮT của vòng tự cải tiến. Ngay khi người dùng bác bỏ hoặc sửa một phát hiện
> của Hệ, ghi vào đây **trong cùng lượt làm việc đó**, không đợi cuối phiên. Mỗi mục có trường
> `Số lần bị nhắc` — đây là thứ quyết định khi nào một ghi nhận được thăng hạng thành quy tắc.
>
> **Ngưỡng thăng hạng** (xem `MEMORY-INDEX.md` mục "Vòng tự cải tiến"):
> | Số lần | Hành động |
> |---|---|
> | 1 | Chỉ nằm ở tệp này |
> | **≥2** | Ghi vào mục "Dương tính giả" của `MEMORY-INDEX.md` — tầng luôn được nạp |
> | **≥3** | Tạo `03-Change-Proposals/CP-...md` để gấp vào gói skill ở bản sau |

---

## Đang theo dõi

### FP-001 · Dòng "(Ban hành kèm theo Quyết định số ... ngày ... của ...)" ở văn bản điện tử
- **Số lần bị nhắc: 3+** (người dùng xác nhận "đã nhắc em nhiều lần rồi", 28/9/2026)
- **Hệ báo sai thế nào**: bắt Mức 2 vì thiếu dòng chỉ dẫn xuất xứ, viện dẫn Checklist 01 + NĐ 30 Điều 8.
  Có lần còn suy diễn ngược: đề nghị "bổ sung đầy đủ khối Số hiệu/ngày tháng/thẩm quyền ký như một
  văn bản hành chính độc lập".
- **Vì sao sai**: Trường phát hành văn bản điện tử ký số — hệ thống quản lý văn bản tự sinh số hiệu và
  ngày khi phát hành, người soạn thảo không thể điền trước.
- **Nguyên nhân gốc (chẩn đoán 28/9/2026)**: quy tắc **đã có sẵn** trong `Checklist/01-The-Thuc.md` từ lâu
  nhưng Hệ không tìm ra, vì (a) quy tắc viết cụm *"Kèm theo văn bản số ..."* còn văn bản thật dùng
  *"(Ban hành kèm theo Quyết định số ...)"*; (b) quy tắc nằm ở hàng **"Phụ lục"** còn văn bản bị bắt lỗi
  là một **Quy trình**; (c) bảng chứa nó tên là *"thành phần bổ sung (kiểm tra khi có)"*, đọc như tùy chọn.
- **Trạng thái**: ✅ **Đã thăng hạng đủ 3 cấp** — `Checklist/01-The-Thuc.md` mục 3a (v2.25) ·
  `SKILL.md` mục "Danh sách dương tính giả" (v2.25) · `MEMORY-INDEX.md` mục "Dương tính giả" (28/9).
- **Bài học chung**: *một quy tắc chỉ có tác dụng khi tìm được bằng đúng từ ngữ mà văn bản thật dùng.*
  Khi viết quy tắc mới, luôn liệt kê **mọi cách diễn đạt** của cùng một thành phần.

### FP-002 · Lề trang đúng biên bị báo là ngoài khoảng cho phép
- **Số lần bị nhắc: 1**
- Script `_read_input_properties.py` báo "Lề right = 20.0mm, ngoài khoảng 15-20mm" dù 20.0mm hợp lệ.
  Nguyên nhân: `python-docx` quy đổi có sai số dấu phẩy động (20.0mm đọc lại thành 20.0025mm).
- **Trạng thái**: ✅ Đã sửa ở script v1.1 (`round(val,1)` + `EPS=0.01`). Chi tiết: `CP-20260826-002.md`.

---

## Còn nghi ngờ, chưa đủ căn cứ kết luận

### FP-003 · Bắt đúng lỗi nhưng "nhìn nhầm sang vấn đề khác cùng đoạn"
- **Số lần bị nhắc: 1** (phát hiện qua chạy hồi quy, 27/8/2026)
- Hệ báo "viết thường sau dấu ':'" tại vị trí đúng ra là lỗi #15 (danh mục bộ môn dùng bản cũ).
  Không phải false positive thuần túy — viết thường sau ":" vẫn là lỗi thật theo TB 597 Mục 3.1 —
  nhưng Hệ đã **tìm ra vấn đề gần đúng** thay vì **xác định chính xác vấn đề được cài**.
- **Rủi ro**: khi áp vào hồ sơ thật không có đáp án để đối chiếu, dạng này rất khó phát hiện.
- **Cần**: thêm ca hồi quy chuyên kiểm "định vị đúng vấn đề", không chỉ "có báo lỗi hay không".

### FP-004 · Suy luận mâu thuẫn logic ngoài phạm vi rà soát thể thức
- **Số lần bị nhắc: 1**
- Hệ tự suy ra mâu thuẫn "ban hành tháng 9 nhưng nói về phong trào hè". Logic hợp lý nhưng không thuộc
  lỗi được thiết kế. Chưa rõ là suy luận có giá trị hay Hệ đang diễn giải quá xa.
- **Cần**: người dùng xác nhận có muốn Hệ nêu loại phát hiện này không.
