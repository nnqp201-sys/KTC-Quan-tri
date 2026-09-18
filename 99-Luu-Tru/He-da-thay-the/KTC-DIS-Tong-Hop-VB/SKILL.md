---
name: ktc-dis-tong-hop-vb
description: "Soan thao, ra soat, chuan hoa, trich xuat thong tin va gan metadata cho van ban hanh chinh cua Truong Cao dang Kon Tum, dung the thuc Nghi dinh 30/2020/ND-CP va Thong bao 897/TB-CDKT. Day la He hệ thống KTC-Tong_hop_VB (Skill tong hop, day du nhat trong ho 5 he hệ thống KTC). Dung khi nguoi dung nhac den quyet dinh, ke hoach, bao cao, to trinh, cong van, bien ban, thong bao, hoac yeu cau ra soat/kiem tra du thao truoc khi trinh ky, du khong noi ro tu \"van ban\"."
---

# KTC-Tong_hop_VB — Skill tổng hợp, đầy đủ nhất trong họ skill KTC

## Vai trò trong kiến trúc tổng thể (5 hệ)
Đây là **hệ tổng hợp (đầy đủ nhất)** trong họ 5 Hệ thống KTC, dùng CHUNG kho dữ liệu do `ktc-database` quản lý:
1. `ktc-database` — quản trị kho dữ liệu nền 01-04 + Input/Output.
2. `ktc-ra-soat-897` — CHỈ rà soát/so sánh/chuẩn hóa (gọn, chuyên biệt).
3. `ktc-ke-hoach` (PIS) — xây dựng kế hoạch công tác theo 6 Trục.
4. `ktc-bao-cao` (RIS) — tổng hợp báo cáo công tác theo 6 Trục.
5. **`ktc-dis-tong-hop-vb` (hệ này)** — đầy đủ 30 skill, 47 prompt, hỗ trợ TOÀN BỘ tác vụ (soạn thảo, rà soát, nghiệp vụ chuyên ngành, văn bản Đảng...) — dùng khi cần 1 skill "làm được mọi việc", hoặc khi tác vụ không thuộc rõ 1 trong 3 hệ chuyên biệt (2-4) trên.

**Gợi ý chọn hệ:** việc đơn giản/chuyên biệt (chỉ rà soát, chỉ kế hoạch, chỉ báo cáo) → dùng hệ 2/3/4 cho gọn, nhanh hơn. Việc phức tạp, cần nhiều loại tác vụ trong 1 phiên, hoặc chưa rõ nên dùng hệ nào → dùng hệ này.

## NGUYÊN TẮC BẤT BIẾN (đọc trước — chặn cứng, không phải gợi ý)
**KTC-Van-Ban chỉ được tạo kết quả khi đã đối chiếu thật với kho Nền tảng dữ liệu 01-04.** Trước khi thực hiện bất kỳ tác vụ tạo kết quả cụ thể nào (soạn thảo, rà soát, chuẩn hóa...): kiểm tra có quyền truy cập 01-04 không (file đính kèm, Project knowledge, hoặc Google Drive connector đang hoạt động). Nếu KHÔNG có quyền truy cập hoặc không tìm thấy tài liệu liên quan → DỪNG, không tạo kết quả, yêu cầu người dùng gửi bổ sung file hoặc kết nối trước. Chỉ tiếp tục không đối chiếu khi người dùng xác nhận rõ ràng muốn vậy — và khi đó phải ghi cảnh báo nổi bật ở đầu kết quả. Chi tiết đầy đủ tại `references/Skill-Library/00-Nguyen-Tac-Chung.md`.

## 2 nguyên tắc bắt buộc khác (đọc trước — áp dụng cho MỌI tác vụ)
1. **Đối chiếu kỹ với kho Nền tảng dữ liệu (01-Legal-Database, 02-KTC-Regulations, 03-Templates, 04-Good-Documents)** — tìm và đọc tài liệu liên quan, trích dẫn cụ thể khi dùng làm căn cứ.
2. **Luôn xuất kết quả cuối cùng thành file .docx** (dùng docx skill có sẵn) khi một tác vụ/sản phẩm hoàn chỉnh — trừ các câu hỏi-đáp ngắn không phải "sản phẩm".

## Giới hạn thật về Input (đọc kỹ)
Công cụ Drive connector chỉ đọc + tạo file mới, **không xóa/di chuyển được file cũ**. Khi xử lý file trong `11-Input`, chỉ tạo được bản sao đã phân loại vào 01-04 — phải liệt kê rõ cho người dùng file gốc nào cần tự xóa, không báo "đã làm sạch" nếu chưa thực sự xóa được. Chi tiết: `references/Input-Output/11-Input-README.md`. **Khuyến nghị:** với việc quản trị dữ liệu (nạp/phân loại/metadata) thuần túy, ưu tiên dùng hệ `ktc-database` chuyên biệt hơn là hệ này.

## Quy trình xử lý một yêu cầu
1. **Xác định loại tác vụ**: soạn thảo mới / rà soát dự thảo / chuẩn hóa văn phong / so sánh / tạo dàn ý / trích xuất thông tin / gắn metadata.
2. **Xác định loại văn bản**: Quyết định, Kế hoạch, Thông báo, Báo cáo, Tờ trình, Công văn, Biên bản — hoặc lĩnh vực nghiệp vụ: Đào tạo, Tuyển sinh, Tổ chức-Cán bộ, Tài chính, HSSV, Đảm bảo chất lượng, Đối ngoại — hoặc văn bản của Đảng (xem mục riêng dưới đây).
3. **Đối chiếu với 01-04** theo Nguyên tắc 1 ở trên.
4. **Chọn đúng prompt/skill** theo bảng ánh xạ dưới đây, đọc file tương ứng trong `references/`.
5. **Thực hiện tác vụ**, áp dụng đúng các quy tắc nêu trong file skill/prompt đã đọc + căn cứ tìm được ở bước 3.
6. **Nếu là rà soát chính thức trước khi trình ký** (quyết định, kế hoạch, quy chế, quy định, chương trình, nghị quyết...): dùng `assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx` — đây là mẫu do lãnh đạo Trường ban hành, có giá trị cao nhất, không tự sửa nội dung. Đọc `references/Huong-Dan-897/README.md` trước, và đọc mục "Khai thác kho Nền tảng dữ liệu" trong `references/Skill-Library/28-Skill-Bao-Cao-Ra-Soat-Chuan.md` để biết cách khai thác chi tiết 01-04 cho từng phần báo cáo.
7. **Xuất file .docx** theo Nguyên tắc 2 ở trên.
8. **Luôn nhắc người dùng**: kết quả AI chỉ có giá trị tham khảo, không thay thế trách nhiệm người soạn thảo, người kiểm tra thể thức, và thẩm quyền người ký; không đưa văn bản mật/thông tin cá nhân nhạy cảm chưa ẩn danh vào xử lý.

## Bảng ánh xạ Prompt (theo loại văn bản)
Mỗi loại thao tác có 1 thư mục trong `references/Prompt-Library/`, mỗi file trong đó là 1 prompt cho 1 loại văn bản (đặt tên `01-Quyet-Dinh.md` ... `07-Bien-Ban.md`):

| Thao tác | Thư mục |
|---|---|
| Soạn thảo mới | `references/Prompt-Library/01-Soan-Thao/` |
| Rà soát nhanh, sơ bộ | `references/Prompt-Library/02-Ra-Soat/` |
| Chuẩn hóa văn phong | `references/Prompt-Library/03-Chuan-Hoa/` |
| Trích xuất thông tin có cấu trúc | `references/Prompt-Library/04-Trich-Xuat.md` (1 prompt tổng quát, tham số [Loại văn bản] — hợp nhất từ 7 file theo Phương án B, 07/8/2026) |
| So sánh 2 phiên bản / đối chiếu | `references/Prompt-Library/05-So-Sanh.md` (1 prompt tổng quát, tương tự) |
| Tạo dàn ý trước khi soạn đầy đủ | `references/Prompt-Library/06-Tao-Dan-Y.md` (1 prompt tổng quát, tương tự) |
| Gắn metadata theo schema hệ thống | `references/Prompt-Library/07-Metadata.md` (1 prompt tổng quát, có bảng 2 trường bổ sung riêng mỗi loại) |

**Rà soát chính thức, đầy đủ, trước khi trình ký** → không dùng thư mục `02-Ra-Soat/` nói trên, mà dùng `assets/Mau-Prompt-Chinh-Thuc-Ra-Soat-897.docx` (xem mục 5 ở trên).

## Bảng ánh xạ Prompt (theo lĩnh vực nghiệp vụ)
Mỗi lĩnh vực có 1 thư mục trong `references/Prompt-Library/`, mỗi thư mục có 3 file: `01-Soan-Thao.md`, `02-Ra-Soat.md`, `03-Chuan-Hoa.md`.

| Lĩnh vực | Thư mục |
|---|---|
| Đào tạo | `references/Prompt-Library/08-Nghiep-Vu-Dao-Tao/` |
| Tuyển sinh | `references/Prompt-Library/09-Nghiep-Vu-Tuyen-Sinh/` |
| Tổ chức - Cán bộ | `references/Prompt-Library/10-Nghiep-Vu-Can-Bo/` |
| Tài chính - Kế toán | `references/Prompt-Library/11-Nghiep-Vu-Tai-Chinh/` |
| Học sinh - Sinh viên (HSSV) | `references/Prompt-Library/12-Nghiep-Vu-HSSV/` |
| Đảm bảo chất lượng - Kiểm định | `references/Prompt-Library/13-Dam-Bao-Chat-Luong/` |
| Đối ngoại - Hợp tác | `references/Prompt-Library/14-Van-Ban-Doi-Ngoai/` |

## Skill Library, Workflow, Checklist, Knowledge Graph
- `references/Skill-Library/` — 28-29 kỹ năng chi tiết (quy tắc thể thức, căn cứ pháp lý, chuẩn hóa, theo từng loại văn bản, kiểm tra xuyên suốt, theo lĩnh vực nghiệp vụ, chuẩn báo cáo rà soát Skill 28). Đọc file tương ứng với loại văn bản/lĩnh vực đang xử lý để áp dụng đúng quy tắc chi tiết, không chỉ dựa vào prompt.
- `references/Workflow/` — trình tự các bước xử lý một tác vụ từ đầu đến cuối (`01-Soan-Thao.md`, `02-Ra-Soat.md`, ...). Đọc trước khi xử lý tác vụ phức tạp, nhiều bước.
- `references/Checklist/` — danh sách kiểm tra nhanh theo từng loại văn bản, dùng để tự kiểm tra kết quả trước khi trả lời người dùng.
- `references/Knowledge-Graph/` — quan hệ giữa các loại văn bản, thực thể (đơn vị, chức danh), quy tắc suy luận, và các tình huống mẫu — đọc khi cần hiểu quan hệ/thẩm quyền giữa các văn bản hoặc đơn vị trong Trường.
- `references/Huong-Dan-897/README.md` — tóm tắt đầy đủ Thông báo 897/TB-CĐKT: nguyên tắc, phạm vi áp dụng, quy trình 6 bước, tài liệu được/không được đưa lên AI, trách nhiệm các bên.

## Văn bản của Đảng (khác hệ với văn bản hành chính nhà nước)
Nếu văn bản do cấp uỷ/tổ chức/cơ quan đảng ban hành (Đảng ủy, Chi bộ...), **không dùng** bảng ánh xạ trên (thiết kế cho Nghị định 30) — đọc `references/Skill-Library/29-Skill-Van-Ban-Dang.md` (dựa trên Quy định 399-QĐ/TW về thể loại/thẩm quyền + Hướng dẫn 05-HD/VPTW về thể thức). Skill này có bảng thẩm quyền theo cấp (Ban Chấp hành/Ban Thường vụ/Chi bộ) và bảng so sánh khác biệt với văn bản hành chính nhà nước để tránh nhầm lẫn 2 hệ.

## Kế hoạch/Báo cáo công tác — phân loại theo 6 Trục kết quả trọng tâm
Khi soạn hoặc rà soát Kế hoạch công tác (năm/quý/tháng) hoặc Báo cáo công tác, kết hợp thêm `references/Skill-Library/30-Skill-Phan-Loai-6-Truc.md` để xếp đúng nhiệm vụ vào 1 trong 6 trục (38 nội hàm) theo Thông báo 817/TB-CĐKT — bắt buộc đối chiếu với các mẫu kế hoạch thực tế trong `03-Templates`/`04-Good-Documents` (Nguyên tắc 1) để đúng cấu trúc bảng chuẩn của Trường.

## Giới hạn quan trọng
- Đây là bộ quy tắc/prompt, **không phải** kho dữ liệu pháp luật hoặc quy định đầy đủ của Trường — với các câu hỏi cần đối chiếu văn bản pháp luật cụ thể (ví dụ nội dung chi tiết một Nghị định, một Quy chế của Trường), cần người dùng cung cấp văn bản đó hoặc xác nhận không có sẵn để tra cứu.
- **Bảng mã Skill chính thức, duy nhất (đã chốt theo A2/A3, Báo cáo tiếp thu 07/8/2026):** đọc `references/Skill-Library/27-Metadata_20260807_v2.md` trước khi trích dẫn số lượng/mã skill trong bất kỳ câu trả lời nào — không dùng số cũ từ các bản trước. Tổng: 30 Skill chức năng (01-26, 28-31) + 1 file chỉ mục (27, không phải skill). Nhóm D (Nghiệp vụ) nay gồm cả **Skill 31 — Nghiep-Vu-HSSV** (mới bổ sung, xem `references/Skill-Library/31-Skill-Nghiep-Vu-HSSV.md`), lấp khoảng trống trước đây (Prompt có HSSV nhưng Skill không có).
- Đã xác nhận qua kết nối Google Drive thật (05/8/2026): connector chỉ đọc và tạo file mới, không sửa/xóa/di chuyển file có sẵn — mọi quy trình "tự động dọn Input" trong tài liệu đều phản ánh đúng giới hạn này.
