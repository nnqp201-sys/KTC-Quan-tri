# Bảng mã đơn vị dùng chung — KTC-Quan-tri

**Lập ngày:** 13/9/2026 · **Nguồn tên chính thức:** cột "Đơn vị:" trong 11 tệp Khung tiêu chí đánh giá
tập thể (`11-Du-lieu-Cong-Viec/KHUNG TIEU CHI.../Khung tieu chi danh gia Tap the.../*.xlsx`) — đọc trực
tiếp từ tệp, không suy diễn từ tên tệp.

## Vì sao cần bảng này

Cùng một đơn vị đang được viết theo **ba kiểu khác nhau** ở ba nơi trong dự án. Không có bảng ánh xạ thì
không thể đối chiếu tự động giữa KTC-Ke-Hoach ↔ KTC-Theo-doi-CV ↔ KTC-Bao-Cao. Đây là điều kiện kỹ thuật
bắt buộc trước khi chốt Master Task Register.

## Bảng chuẩn

| Mã chuẩn | Tên chính thức (dùng trong văn bản) | Biến thể trong `23-KTC-Ke-Hoach/` | Biến thể trong `11-Du-lieu-Cong-Viec/` | Biến thể trong dữ liệu Excel thật |
|---|---|---|---|---|
| `P-TCCB` | Phòng Tổ chức cán bộ và Công tác học sinh, sinh viên | `Phong-TCCB-CTHHSV` ⚠️ | `Phong_TCCB_CTHSSV` | `Phòng Tổ chức` ⚠️ |
| `P-QLDT` | Phòng Quản lý Đào tạo và Bảo đảm chất lượng | `Phong-QLDT-BDCL` | `Phong_QLDT_BDCL` | `Phòng QLĐT&BĐCL` |
| `P-THHC` | Phòng Tổng hợp - Hành chính và Quản trị | `Phong-THHCQT` | `Phong_TH_HCQT` | `Phòng TH-HC&QT` |
| `P-QLKH` | Phòng Quản lý khoa học công nghệ và Hợp tác phát triển | `Phong-QLKHCN-HTPT` | `Phong_QLKHCNHTPT` | `Phòng QLKHCN&HTPT` |
| `P-TCKT` | Phòng Tài chính - Kế toán | `Phong-TC-KT` | `Phong_TC_KT` | `Phòng TC-KT` |
| `K-KHCB` | Khoa các Khoa học cơ bản | `Khoa-CKHCB` | `Khoa_KHCB` | *(chưa có dữ liệu)* |
| `K-SUPH` | Khoa Sư phạm | `Khoa-Su-Pham` | `Khoa_Su_pham` | *(chưa có dữ liệu)* |
| `K-KTNL` | Khoa Kinh tế và Nông Lâm | `Khoa-KT-NL` | `Khoa_KTNL` | *(chưa có dữ liệu)* |
| `K-KTCN` | Khoa Kỹ thuật và Công nghệ | `Khoa-KT-CN` | `Khoa_KTCN` | *(chưa có dữ liệu)* |
| `K-YDUOC` | Khoa Y - Dược | `Khoa-Y-Duoc` | `Khoa_Y_Duoc` | *(chưa có dữ liệu)* |
| `K-DTSHLX` | Khoa Đào tạo và Sát hạch lái xe | `Khoa-DT-SHLX` | `Khoa_DTSHLX` | *(chưa có dữ liệu)* |

## Cấp thứ hai — bộ phận và chức danh (chưa có mã, cần bổ sung)

Đối chiếu trên 328 nhiệm vụ thật của báo cáo tháng 8/2026 cho thấy cột "Đơn vị chủ trì" **không chỉ chứa
11 đơn vị cấp Trường**. 60 dòng ở 4 đơn vị điền bằng bộ phận nội bộ hoặc nhóm người:

`Ban Truyền thông` (19×) · `Nhà giáo` (6×) · `Các bộ môn và nhà giáo` (4×) · `Bộ môn CK&XD` (4×) ·
`Giáo vụ khoa` (3×) · `Chi bộ khoa` (2×) · `Các lớp sinh viên` (2×) · `Toàn thể viên chức, nhà giáo` (2×)…

Bảng một cấp hiện tại không nối được các giá trị này. Cần bổ sung **cấp thứ hai** (bộ môn · tổ · ban ·
chức danh) và quy tắc: mỗi giá trị cấp hai phải trỏ về đúng một mã đơn vị cấp một.

### Ban Truyền thông — bộ phận cấp hai thuộc `P-THHC` (đã chốt 14/9/2026)

Báo cáo tháng 8/2026 của **Ban Truyền thông** (tệp ghi rõ `ĐƠN VỊ: BAN TRUYỀN THÔNG`) đặt trong thư mục
của Phòng TH-HC&QT. **Đây là chủ đích, không phải đặt nhầm chỗ.**

Người phụ trách hệ xác nhận 14/9/2026: Ban Truyền thông **trực thuộc Phòng TH-HC&QT**; nhiệm vụ của Ban
được tổng hợp chung vào thư mục của Phòng để lấy thông tin, dữ liệu về công tác truyền thông. Mẫu báo cáo
cấp Trường cũng ghi tương ứng: *"lấy kết quả thực hiện công tác truyền thông của Ban Truyền thông, thuộc
phòng TH-HC&QT"*.

Hệ quả: **Ban Truyền thông không có mã đơn vị cấp một và không phải một đầu mối nộp báo cáo riêng.** Khi
cần mã, dùng mã cấp hai trỏ về `P-THHC` (xem mục cấp thứ hai ở trên). Số đầu mối nộp báo cáo tháng vẫn là
**13** = 11 đơn vị cấp một + Công đoàn cơ sở + Đoàn Thanh niên – Hội Sinh viên.

Kiểm chứng trên tệp thật: toàn bộ nhiệm vụ trong `BAN TT.xlsx` đều ghi `Đơn vị chủ trì = Ban Truyền thông`
và chỉ thuộc mảng truyền thông — không phải báo cáo đầy đủ của Phòng TH-HC&QT.

## Ánh xạ bổ sung — máy đọc (`29-Cong-Cu/doi_soat_so_lieu.py`)

Chỉ ghi **biến thể đã có bằng chứng trên tệp thật** hoặc **quyết định đã chốt**. Công cụ khớp **chính xác** sau khi bỏ
dấu và ký tự đặc biệt (KI-001: không khớp gần đúng). Biến thể chưa có ở đây thì công cụ để riêng `?<tên>` và báo DS06
— không tự gán. Thêm dòng mới phải ghi bằng chứng.

| Biến thể | Mã | Cấp | Bằng chứng / quyết định |
|---|---|---|---|
| `Ban Truyền thông` | `P-THHC` | hai | Quyết định 14/9/2026 (mục "Ban Truyền thông" ở trên) — tổng hợp vào Phòng TH-HC&QT |
| `Ban TT` | `P-THHC` | hai | Tên tệp `BAN TT.xlsx`/`.docx` kỳ 2026-09; đầu tệp ghi "ĐƠN VỊ: BAN TRUYỀN THÔNG" |
| `P.THHCQT` | `P-THHC` | một | Tên tệp `1. BAO CAO PL IIB/P.THHCQT.xlsx` kỳ 2026-09; đầu tệp "PHÒNG TH-HC&QT" |
| `P QLKHCN` | `P-QLKH` | một | Tên tệp `2. BAO CAO IIA/P QLKHCN.docx` kỳ 2026-09; bảng đầu văn bản "PHÒNG QLKHCN&HTPT" |
| `SP` | `K-SUPH` | một | Tên tệp `2. Phu luc Ib/SP.xlsx` kỳ 2026-09; đầu tệp "KHOA SƯ PHẠM" |

## Hai lỗi cần sửa (đánh dấu ⚠️ ở trên)

1. **`Phong-TCCB-CTHHSV` sai chính tả** — thừa một chữ `H`. Đúng phải là `CTHSSV` (Công tác học sinh,
   sinh viên). Thư mục này nằm trong `23-KTC-Ke-Hoach/Nhap_Ke_Hoach/input-KH_Nam/` và `input-KH_Quy/`.
   Đổi tên thư mục sẽ kéo theo phải sửa `23-KTC-Ke-Hoach/SKILL.md` và đóng gói lại `.skill` — xếp vào
   nhóm việc có ràng buộc, không sửa lẻ.

2. **`Phòng Tổ chức` là tên cụt** trong dữ liệu Excel thật (126/1.358 dòng nhiệm vụ gốc). Không khớp với
   bất kỳ tên chính thức nào. Khi nạp vào Master Task Register phải ánh xạ về `P-TCCB`, và nhắc đơn vị
   nhập liệu ghi đủ tên.

## Cảnh báo về độ phủ dữ liệu — quan trọng

1.358 dòng nhiệm vụ gốc (nguồn của 122 nhiệm vụ chuẩn) **chỉ đến từ 5 Phòng**:

| Đơn vị | Số dòng nhiệm vụ gốc |
|---|---|
| Phòng TH-HC&QT | 402 |
| Phòng QLKHCN&HTPT | 387 |
| Phòng QLĐT&BĐCL | 366 |
| Phòng Tổ chức | 126 |
| Phòng TC-KT | 77 |

**Sáu Khoa hoàn toàn vắng mặt.** Do đó danh mục 122 nhiệm vụ chuẩn hiện **chưa phủ khối đào tạo** — lĩnh
vực `S. Nhiệm vụ chuyên môn nhà giáo` chỉ có 4 nhiệm vụ, sinh ra từ viên chức Phòng có tham gia giảng dạy,
không phải từ khảo sát các Khoa.

Hệ quả khi thiết kế Master Task Register: **không được coi 122 nhiệm vụ chuẩn là danh mục đầy đủ**. Khi
một Khoa đăng ký nhiệm vụ không khớp mã nào, đó nhiều khả năng là khoảng trống của danh mục chứ không phải
lỗi của đơn vị — phải mở luồng bổ sung mã mới thay vì ép về mã gần đúng.

## Ghi chú kiểm chứng

Ghi chú `91-Tai-Lieu-Thiet-Ke/GHI-CHU-CAU-NOI-3-HE.md` (19/8/2026) từng kết luận tên đơn vị "khớp hoàn
toàn 100%". Kết luận đó dựa trên **dữ liệu mẫu tự tạo**, và chính ghi chú đã tự lưu ý điều này. Đối chiếu
trên dữ liệu thật ở bảng trên cho thấy **không khớp**: ba kiểu viết cùng tồn tại, một tên sai chính tả,
một tên cụt. Lấy theo bảng này, không lấy theo kết luận cũ.
