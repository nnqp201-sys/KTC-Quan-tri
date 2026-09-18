# PATCH NOTES — KTC-Bao-Cao v2.5 · KTC-Ke-Hoach v3.1 (14/9/2026)

**Nguồn sửa:** đợt chạy thử báo cáo tháng 8 và kế hoạch tháng 9/2026, đối chiếu với bốn văn bản đã ban
hành: `BC-375`, `PL-375`, `KH-834`, và phụ lục tháng 7 (`00. Phu luc chi tiet ket qua cong tac thang`).

## Ba lỗi ở tầng quy trình, không phải lỗi một lần chạy

### L1 — Skill 32 loại bỏ nhầm nguồn văn phong

Skill 32 ghi *"Không nhận văn bản tường thuật tự do thay cho Excel Phụ lục"*. Câu này khiến bỏ qua **13 tệp
`.docx`** mà đơn vị nộp. Chúng không phải văn bản tự do — chúng là **Phụ lục IIa**, biểu mẫu chính thức, đã
chia sẵn theo 6 Trục, và là **nguồn duy nhất của văn tường thuật**.

*Hệ quả đo được:* bỏ sót **198 ý kết quả** và **130 ý kế hoạch**; phần tường thuật phải ghép từ cột "Nội
dung công việc" của bảng nên rời rạc, không thành câu.

*Sửa:* Skill 32 v2.5 + Workflow 09 Bước 1 — mỗi đơn vị nộp **hai tệp**, thiếu một là nộp thiếu.

### L2 — Sai nguồn của phụ lục và kế hoạch tháng cấp Trường

Skill 33 và 36 đều định nghĩa sản phẩm cấp Trường là *"gộp từ nhiều đơn vị"*. Sai.

| Phép đo trên văn bản đã ban hành | Kết quả |
|---|---|
| Phụ lục tháng 7 khớp Kế hoạch quý III | **39/41 = 95%** |
| Phụ lục tháng 8 (`PL-375`) khớp Kế hoạch quý III | 26/40 = 65% |
| Phụ lục tháng 8 khớp phụ lục tháng 7 | 14/40 — không phải chép kỳ trước |
| Quy mô phụ lục tháng 7 · tháng 8 | 39 · 39 |
| Cách cũ (gộp từ đơn vị) | **211** — sai hơn 5 lần |
| `KH-834` (kế hoạch tháng 9) so với gộp từ 13 đơn vị | 53 so với **94** |

Phụ lục cấp Trường **báo cáo lại kế hoạch công tác của chính Trường**, không tổng hợp mọi việc đơn vị đã
làm. Kế hoạch tháng là **bản chi tiết hóa kế hoạch quý**, không phải bản gộp từ dưới lên.

*Sửa:* Skill 33 BƯỚC 0A, Skill 36 BƯỚC 0, Workflow 09 Bước 3, Workflow 10 Bước 3.

*Điều kiện lọc kèm theo:* chỉ nhiệm vụ do **lãnh đạo cấp Trường** trực tiếp chỉ đạo — kiểm chứng **100%**
trên cả ba văn bản, không một dòng nào do Trưởng khoa/Phó Trưởng khoa chỉ đạo.

### L3 — Danh mục mục con bị tự sinh thay vì lấy từ mẫu

Mẫu `00. Mau bao cao thang (cap Truong).docx` quy định **sẵn** từng mục con và lấy từ đơn vị nào. Bản chạy
tự sinh nhãn từ tên nội hàm TB 817 → ra `* Công tác pháp chế, thanh tra, kiểm tra và kiểm soát nội bộ` và
**12 lần** `* Công tác khác`. Đáp án đã có sẵn trong mẫu.

*Sửa:* Skill 33 BƯỚC 0B — bảng danh mục cố định 6/2/0/3/4/3 mục con + 8 Nghị quyết theo đúng thứ tự.

## Bốn bẫy kỹ thuật đã ghi thành quy tắc

| # | Bẫy | Nơi ghi |
|---|---|---|
| 1 | `delete_rows` của openpyxl **không gỡ vùng gộp ô** → vùng gộp cũ trượt xuống, tràn ngang bảng | Skill 33 BƯỚC 0D · Skill 36 |
| 2 | Đoạn nội dung gồm **hai run**; gộp một run làm **cả đoạn đậm nghiêng** | Skill 33 BƯỚC 0D |
| 3 | Luật đổi chủ ngữ chứa từ trần (`Ban`) nuốt chữ trong *"**Ban hành** Kế hoạch"* | Skill 33 BƯỚC 0C |
| 4 | Cắt `phối hợp với <đơn vị>` bằng mẫu chung ăn lan, **xóa sạch nội dung câu** | Skill 33 BƯỚC 0C |

## Cảnh báo mới

`00. Phu luc chi tiet ket qua cong tac thang (cap Truong).xlsx` và `.xltx` **không phải mẫu trống** — sheet
tên `BC Kết quả tháng 7`, chứa 39 nhiệm vụ thật kèm tên người chỉ đạo. `.docx` và `.dotx` là cùng một nội
dung. Dùng làm mẫu trống sẽ kéo dữ liệu tháng 7 vào sản phẩm mới.

## Tệp đã sửa

| Tệp | Phiên bản |
|---|---|
| `KTC-Bao-Cao/references/Skill-Library/32-Skill-Thu-Thap-Bao-Cao-Don-Vi.md` | v2.4 → **v2.5** |
| `KTC-Bao-Cao/references/Skill-Library/33-Skill-Tong-Hop-Bao-Cao-Truong.md` | v2.3 → **v2.4** |
| `KTC-Bao-Cao/references/Workflow/09-Tong-Hop-Bao-Cao.md` | v2.4 → **v2.5** |
| `KTC-Ke-Hoach/references/Skill-Library/36-Skill-Tong-Hop-Ke-Hoach-Truong.md` | v1 → **v2.0** |
| `KTC-Ke-Hoach/references/Workflow/10-Tong-Hop-Ke-Hoach.md` | v3.0 → **v3.1** |

**Chưa làm:** đóng gói lại `.skill`. Nguồn rời đã sửa, gói `.skill` vẫn là bản cũ — xem `KI-013`.
