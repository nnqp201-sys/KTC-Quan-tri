# 14 — Nguyên tắc soạn thảo bất biến

**Ban hành:** 13/9/2026 · **Nguồn:** quy ước người phụ trách hệ, chốt sau đợt chạy thử báo cáo tháng 8/2026
**Hiệu lực:** áp dụng cho **mọi** tác vụ sinh văn bản của KTC-Quan-tri, không cần nhắc lại ở từng lượt.

Bốn nguyên tắc dưới đây là **bất biến**: chỉ được bỏ qua khi người dùng nói minh thị, và khi bỏ qua phải
ghi rõ lý do trên sản phẩm.

---

## NT-1. Phát triển từ file tương đồng, không dựng từ mẫu trống

**Quy tắc:** trước khi tạo bất kỳ văn bản nào, phải tìm **bản cùng loại đã ban hành** để phát triển lên.
Mẫu trống chỉ dùng để kiểm số đo thể thức, **không** dùng làm khung soạn thảo.

**Lý do:** mẫu trống chứa bố cục nhưng **không chứa văn phong, độ nén, cách nêu số liệu, cách phân mục**.
Đợt chạy thử 13/9/2026 dựng báo cáo tháng 8 từ mẫu trống `.dotx` và bị bác bỏ toàn bộ về "biểu mẫu, thể
thức, kỹ thuật trình bày, văn phong" — trong khi báo cáo thật `BC-375` của chính tháng đó đã nằm sẵn trong
kho. Xem `99-Kinh-Nghiem/01-Lessons-Learned/LL-20260913-002.md`.

**Thứ tự nguồn — dừng ở bậc cao nhất tìm được:**

| Bậc | Nguồn | Cho ta điều gì |
|---|---|---|
| 1 | Văn bản **cùng loại, cùng kỳ** đã ban hành | Toàn bộ: bố cục, văn phong, số đo, cách phân mục |
| 2 | Cùng loại, **kỳ gần nhất** — `02-KTC-Regulations/`, `04-Good-Documents/` | Như trên, chỉ khác số liệu |
| 3 | Cùng loại **khác cấp/khác đơn vị** | Bố cục và thể thức; văn phong phải chuyển cấp |
| 4 | Mẫu trống `.dotx`/`.xltx` ở `03-Templates(1)/` | Chỉ số đo thể thức |
| 5 | `Checklist 08-Quy-Uoc-Rieng-CDKT.md` mục 4 · TB 597 | Kiểm chứng số đo |

**Cách làm:** mở bản đã ban hành, **đo thật** bằng `python-docx`/`openpyxl` (khổ giấy, lề, phông, cỡ, thụt
đầu dòng, số bảng), rồi dựng bản mới khớp đúng các số đo đó. Không mô tả định dạng bằng mắt.

**Tự khai bắt buộc:** ghi trên sản phẩm đã phát triển từ văn bản nào (số hiệu, ngày). Nếu phải dùng bậc 4
trở xuống, ghi rõ: *"Chưa tìm được văn bản cùng loại đã ban hành để đối chiếu văn phong."*

---

## NT-2. Track Changes — khi soạn trên văn bản đã có

**Kích hoạt:** người dùng nhắc tới **"track changes"** hoặc **"ghi nhật ký sửa đổi"**, **hoặc** tác vụ là
sửa/góp ý/hoàn thiện một văn bản **đã tồn tại** (trong kho hoặc do người dùng cung cấp).
Danh sách dấu hiệu đầy đủ: `15-Skill-Track-Changes.md`.

**Quy tắc ba bước, không được rút gọn:**

1. **Lấy đúng file gốc làm điểm xuất phát.** Không soạn lại từ đầu rồi trình bày như bản sửa — người dùng
   mất khả năng kiểm soát nội dung thay đổi. Không tìm được file gốc thì **dừng và hỏi**.
2. **Bật Track Changes trong suốt quá trình soạn**, dùng `<w:ins>`/`<w:del>` OOXML. Tuyệt đối không sửa
   trực tiếp không dấu vết.
3. **Giao kèm bản đối chiếu**: nêu rõ đã sửa bao nhiêu chỗ, thuộc loại nào.

**Đặc tả kỹ thuật đầy đủ — không viết lại ở đây, đọc trực tiếp:**
`KTC-Ra-Soat-897-v2-Cai-tien/references/Skill-Library/Bo-Sung-Chuan-Hoa-TrackChanges-MauChu-PhienBanSkill_20260825.md`

Bốn điểm phải nhớ khi thi hành:

- **Phân biệt màu bằng nhiều `w:author`** — Word tô màu theo author, không ép được mã màu qua XML. Quy ước
  tên: `Nội dung bỏ (Claude)` · `Nội dung bổ sung (Claude)` · `Nội dung điều chỉnh (Claude)`. Mỗi đợt sửa
  có tính chất riêng thì thêm author riêng cho đợt đó.
- **Thay thế nội dung** = cặp `<w:del>` + `<w:ins>` liền nhau, **cùng một author**.
- **Xóa hàng bảng** phải dùng `<w:trPr><w:del .../></w:trPr>`, đặt `<w:del>` là phần tử **cuối cùng** trong
  `<w:trPr>` (sau `<w:trHeight>` nếu có) — sai thứ tự làm hỏng schema; đồng thời wrap text trong hàng bằng
  `<w:del>` để hiện gạch ngang.
- **Kiểm tra trước khi giao**: đối chiếu lại với file gốc, soát lỗi `rPr` lồng nhau và `xml:space` trùng.

**Công cụ:** mô-đun `tools/ktc_trackchanges.py` — sửa có dấu vết, validator OOXML, xuất nhật ký sửa đổi.
Điều kiện kích hoạt và quy trình 4 bước: `15-Skill-Track-Changes.md`. Dùng `python-docx` cho văn bản hành
chính có bảng, không dùng docx-js.

---

## NT-3. Khai thác bộ quy tắc KTC-Ra-Soat-897 trong quản trị

**Quy định:** `KTC-Ra-Soat-897` **không chỉ** là trạm kiểm tra cuối trước khi trình ký. Bộ quy tắc của nó
là **chuẩn soạn thảo dùng ngay từ lúc bắt đầu viết**. Áp dụng sớm rẻ hơn sửa muộn.

| Tệp trong 897 | Dùng ở khâu nào của quản trị |
|---|---|
| `Checklist/01-The-Thuc.md` | Dựng khung văn bản — 9 thành phần thể thức, ký hiệu văn bản, **quyền hạn ký theo QĐ 389 Điều 11** |
| `Checklist/02-Noi-Dung.md` | Viết phần căn cứ và điều khoản; kiểm tính thống nhất nội bộ |
| `Checklist/03-Phap-Ly.md` | Trước khi viện dẫn **bất kỳ** văn bản nào — thứ bậc hiệu lực, **ba hệ quy chiếu không áp lẫn** |
| `Checklist/04-Ngon-Ngu.md` | Chuẩn hóa từ ngữ, loại cụm mơ hồ, chuẩn tên cơ quan/chức danh |
| `Checklist/05-Hinh-Thuc.md` | Đặt khổ giấy, lề, phông, số trang |
| `Checklist/07-Theo-Loai-Van-Ban.md` | **Checklist riêng cho Kế hoạch và Báo cáo** — đọc trước khi dựng hai loại này |
| `Checklist/08-Quy-Uoc-Rieng-CDKT.md` | Quy ước riêng của Trường: cách viết từ ngữ, **tên đơn vị thuộc Trường**, thông số thể thức, viết hoa sau dấu hai chấm |
| `Skill-Library/19-Skill-Danh-Gia-Chat-Luong-Van-Ban.md` | **Tự chấm dự thảo trước khi trình** |
| `Skill-Library/31-Quy-Tac-Van-Hanh-Theo-Tinh-Huong.md` | Xử lý văn bản sửa đổi/hợp nhất, số liệu định mức, tệp nhị phân và Drive |
| `Skill-Library/Skill-Tu-hoc-Phong-Cach-Bao-Cao-ra-soat.md` | DNA cấu trúc báo cáo tốt + bộ phát hiện lỗi hành văn |

**Bốn nguyên tắc rà soát của 897, nâng lên thành nguyên tắc quản trị:**

1. **Không mặc nhiên tin lời phản hồi**, kể cả của người có thẩm quyền. Đơn vị báo "đã hoàn thành" thì phải
   đọc trọn vẹn hoặc tính lại độc lập rồi mới ghi "Đạt". Trích dẫn cụt đã gây kết luận sai trong thực tế.
2. **Tự đính chính minh bạch** khi phát hiện sai sót của chính mình — ghi rõ đã tự phát hiện, không lặng lẽ
   sửa như chưa từng sai.
3. **Giải trình chỉ trả lời đúng trọng tâm** — không mở rộng lập luận ngoài phạm vi được hỏi.
4. **Ghi rõ phiên bản bộ quy tắc** đang dùng trên sản phẩm, để các đợt khác nhau không bị so sánh nhầm.

**Chốt chặn giữ nguyên:** mọi kế hoạch/báo cáo vẫn phải qua 897 trước khi trình ký. Dùng sớm không thay thế
bước này.

---

## NT-4. KTC-Database là cơ sở dữ liệu để tham mưu quản trị

**Quy định:** `KTC-Database` không phải kho lưu trữ tra cứu thụ động. Đây là **cơ sở dữ liệu tham mưu** —
nguồn để trả lời "Trường đã có chủ trương gì, đã cam kết chỉ tiêu nào, đã giao cho ai" trước khi đề xuất
bất cứ điều gì.

**Tìm kiếm sâu — bắt buộc trước khi dựng kế hoạch, báo cáo hoặc đề xuất:**

| Loại tài liệu | Vị trí | Trả lời câu hỏi |
|---|---|---|
| **Chiến lược phát triển** | `02-KTC-Regulations/` | Định hướng dài hạn, chỉ tiêu đã cam kết — nhiệm vụ mới phải quy được về đây |
| **Đề án đang triển khai** | `05-De-an-De-tai/` | Việc gì đang chạy, đến vòng góp ý nào |
| **Kế hoạch năm / quý / tháng** | `02-KTC-Regulations/` | Baseline để duyệt ngược tìm nhiệm vụ bỏ sót |
| **Kế hoạch chuyên đề** | `02-KTC-Regulations/` | Nhiệm vụ chuyên sâu không nằm trong kế hoạch chung |
| **Báo cáo chuyên đề** | `02-KTC-Regulations/`, `04-Good-Documents/` | Số liệu nền và kết quả đã báo cáo — **không được mâu thuẫn với số liệu mới** |
| **Quy chế, quy định nội bộ** | `02-KTC-Regulations/` | Thẩm quyền, quy trình, định mức |
| **VBQPPL** | `01-Legal-Database/` | Căn cứ pháp lý và hiệu lực |

**Điểm vào:** `KTC-DIS-Master-Index_20260830_v1.2.xlsx`. Đọc chỉ mục trước, đừng duyệt cây thư mục mò.
Lưu ý chỉ mục chưa có `03-Templates(1)` — kiểm trực tiếp thư mục đó khi cần mẫu.

**Ba mức khai thác, không dừng ở mức 1:**

1. *Tra cứu* — tìm một văn bản cụ thể.
2. *Đối chiếu* — kiểm dự thảo có mâu thuẫn với văn bản đã ban hành không.
3. **Tham mưu** — tổng hợp nhiều văn bản để trả lời câu hỏi quản trị: nhiệm vụ này đã được giao cho ai bằng
   văn bản nào, chỉ tiêu còn thiếu bao nhiêu, chủ trương nào chưa có kế hoạch triển khai.

**Ràng buộc bất biến giữ nguyên:**

- Chỉ tạo kết quả **sau khi đã đối chiếu thật** với kho 01–04. Không đọc được kho → **dừng và hỏi**. Người
  dùng yêu cầu cứ làm → ghi ngay đầu sản phẩm: *"⚠️ Chưa đối chiếu với kho 01-04 — độ tin cậy hạn chế"*.
- **Kho chỉ đọc.** Hook chặn mọi thao tác ghi. Cần sửa kho thì viết đề xuất ra `12-Output/YYYY-MM-DD/`.
- **Trích dẫn cụ thể** số hiệu, ngày ban hành — không chỉ nêu tên tệp.
- **Không trích dẫn mẫu/checklist nội bộ làm "Căn cứ" pháp lý** — luôn là lỗi Mức 1 theo 897.
