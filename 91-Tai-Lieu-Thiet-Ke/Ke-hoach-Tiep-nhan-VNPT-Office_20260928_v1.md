# Kế hoạch — Tiếp nhận VNPT Office → KTC-Quan-tri (GOAL `tiep-nhan-office` v1.1)

## Context
Người phụ trách giao lệnh GOAL v1.1 (28/9/2026): nối Hệ thống QLVB&ĐH VNPT Office với KTC-Quan-tri để không bỏ sót,
không trễ hạn nhiệm vụ giao qua Office (toàn Trường, Phòng TH-HC&QT tổng hợp). Yêu cầu: xem xét, phỏng vấn, đánh giá khả
thi; phần khả thi làm ngay, phần chưa khả thi để giai đoạn sau.

## Kết luận khả thi
| Hạng mục | Kết luận |
|---|---|
| Bộ đọc 3 loại file xuất (Chế độ B), Sổ tiếp nhận, loại trùng, cờ dữ liệu, rà khoảng trống, gợi ý minh chứng, cảnh báo, lịch chạy, kiểm thử theo Phụ lục A | **Khả thi — làm ngay** (cấu trúc 3 tệp mẫu khớp mục 6: công việc 23 dòng, tiêu đề dòng 5; văn bản đi 60 dòng, tiêu đề dòng 3) |
| Claude phân loại văn bản đến + trích hạn theo lịch (`claude -p` không tương tác) | **Khả thi — làm ngay** |
| Google Sheets (Sổ + MTR) và thư nháp Gmail qua OAuth | **Khả thi nhưng phụ thuộc anh** tạo ứng dụng OAuth (~15 phút, không làm thay được). Mã viết sẵn, tự chuyển sang Sheets/Gmail khi có tệp thông tin xác thực; trước đó ghi .xlsx trên Drive + thư nháp dạng tệp |
| Chế độ A (Claude đọc Office qua Chrome); thư theo từng đơn vị (chờ danh bạ); đưa vào plugin | **Giai đoạn 2** |

## Quyết định đã phỏng vấn (28/9/2026)
1. Giai đoạn 1 **chỉ dùng file xuất** (Chế độ B) — khớp §4.1; Chế độ A để giai đoạn 2 sau khi làm rõ C-15.
2. **Làm đủ nền Google theo lệnh**: Sổ tiếp nhận + Master Task Register lên Google Sheets, thư nháp Gmail (`gmail.compose`, không quyền gửi).
3. **Claude phân loại theo lịch**, kể cả văn bản Đảng (vẫn giữ C-13: gắn nhãn `VB Đảng`, không tạo đề xuất giao việc).
4. **Công cụ trong dự án, chưa vào plugin** (plugin giữ 1.3.2 đang chờ thẩm định vòng 5).
5. Dữ liệu Office và bản lưu Sổ **không lên git**. 6. Chạy lịch trên **máy này**.

## Bước 0 — Hoàn tất việc hôm trước (chưa commit)
Chạy lại `kiem_tra_he_thong.py` (lần trước bị ngắt), rồi commit: 28 ngoại lệ ở
`10-Dau-Vao/02-Cap-Truong/00-Danh-Muc-Tro-KTC-Database.md`; gom bản ≤ 1.3.1 vào `99-Luu-Tru/Can-Xoa/`; `.gitignore`.
Ghi Pending: anh tự quản lý tài khoản kho (phân quyền chỉ đọc), nghiệm thu Chat/Cowork do anh làm.

## Giai đoạn 1 — Làm ngay

**Vị trí:** nguồn skill `24-KTC-Theo-doi-CV/Tiep-Nhan-Office/` (theo mẫu `28-KTC-KPI/Tu-Danh-Gia/`: `SKILL.md`,
`references/`, `cau-hinh.json`); script tất định ở `29-Cong-Cu/`; đầu vào `10-Dau-Vao/05-VNPT-Office/<YYYY-MM-DD>/`
(cập nhật `10-Dau-Vao/00-README.md`, `.claude/rules/21-kho-du-lieu-dau-vao.md`; thêm vào `.gitignore`). Chép 3 tệp mẫu
từ `~/Downloads` vào `…/2026-09-28/` (thiếu `EMAIL_SU_DUNG_TAI_KHOAN…docx` — không cần cho bộ đọc).

**Script mới (tái dùng tiện ích có sẵn):**
- `29-Cong-Cu/office_doc.py` — 3 bộ đọc. Dò dòng tiêu đề động (mẫu `_bang()`, `_k()`, `_ngay()` trong
  `kiem_minh_chung.py`); văn bản đến: Excel nếu có, PDF bằng `pdfplumber` theo tọa độ bảng (cài thêm), dòng lỗi gắn
  `Tách PDF lỗi`. Khóa trùng: công việc `Ngay_Giao + Chu_Tri + băm(tên chuẩn hóa)`; văn bản đến `Số đến + Số ký hiệu`.
  Cờ: `Hạn trong nội dung khác hạn hệ thống`, `Nhiều mốc trong nội dung`, `Chủ trì ngoài 11 đơn vị`, `Quá hạn nhưng chưa có kết quả`.
  Nối căn cứ chỉ theo khóa `số + ký hiệu cơ quan đầu tiên` (vd `4357/SNV`); khớp chủ đề chỉ là gợi ý.
  Mã đơn vị qua `Danh-ba` (đang trống → `Chưa ánh xạ`); dùng `doi_soat_so_lieu.ma_don_vi()` chỉ khi Chủ trì là tên đơn vị.
- `29-Cong-Cu/office_phan_loai.py` — gom văn bản đến **mới** (chưa phân loại), gọi `claude -p` (không công cụ, đầu ra
  JSON theo lược đồ: `Phan_Loai ∈ {Có yêu cầu thực hiện, Mời họp, Để biết}`, `Han_Trich`, `Do_Tin_Cay`, `Ly_Do`), kiểm
  lược đồ; lỗi/hết lượt → `Chưa phân loại` (không đoán). Tiền lọc từ khóa để giảm lượt gọi.
- `29-Cong-Cu/office_luu_tru.py` — hai phần lưu trữ cùng giao diện: `SheetsBackend` (google-api-python-client; token
  ngoài dự án tại `%APPDATA%\KTC-Quan-tri\google\`) và `XlsxBackend` (tệp trên Google Drive đồng bộ) — tự chọn theo có/không
  có thông tin xác thực. `tao_thu_nhap()` qua Gmail API; chưa có OAuth → ghi thư nháp ra tệp `.txt/.eml`.
- `29-Cong-Cu/office_tiep_nhan.py` — điều phối một lượt: tệp khóa chống chạy chồng; lấy tệp mới nhất từng loại theo dấu
  thời gian trong tên; lọc kỳ (tuần T2–T6, tháng, quý dương lịch); ghi 8 sheet của Sổ (`01-Cong-viec-Office` … `Nhat-ky-luot-chay`)
  kèm `Lich-su-thay-doi`; rà khoảng trống → `03-De-xuat-giao-viec`; văn bản đi sau ngày giao có cụm danh từ trùng →
  `04-Goi-y-minh-chung` (nhãn gợi ý); cảnh báo quá hạn / sắp đến hạn (ngưỡng **3 ngày làm việc** trong `cau-hinh.json` —
  ghi rõ khác ngưỡng ≤ 7 ngày của Skill 42); **Giai đoạn 1**: lượt 8h10 tạo 1 thư nháp gửi `phongthhcqt@gmail.com`, nhóm theo
  người chủ trì, văn phong nhắc cập nhật; công việc Công đoàn/Đoàn/Tổ chỉ liệt kê. Thiếu đầu vào 2 lượt liên tiếp → dòng nhắc
  đầu bản tóm tắt. Không cấp Task_ID, không ghi MTR, không gửi thư.
- `29-Cong-Cu/chuyen_mtr_sang_sheets.py` — tạo Google Sheet MTR giữ 4 sheet, 46 cột; chuyển `.xlsx` vào `99-Luu-Tru/`;
  `kiem_minh_chung.py` thêm đọc từ Sheets (hiện MTR chưa có dữ liệu, chỉ script này đọc) — **chạy khi có OAuth**.

**Lịch:** `chay_tiep_nhan_office.cmd` → Task Scheduler 2 tác vụ `KTC-Tiep-Nhan-Office-0810/1410` (T2–T6, Asia/Ho_Chi_Minh,
chạy bù khi máy bật trễ): Python tiếp nhận → `office_phan_loai.py` → cập nhật Sổ; nhật ký theo `90-Nhat-Ky-Van-Hanh/`.
Dự phòng Cowork: chỉ tài liệu thiết kế, không bật.

**Chuẩn, tài liệu:** mục mới cho trường Sổ trong `20-Chuan-Chung/10-Tu-Dien-Truong-Du-Lieu.md` (không sửa trường cũ);
`SKILL.md` (description: KHÔNG cấp Task_ID, KHÔNG gửi email, KHÔNG soạn văn bản); DL-2026092x (nền Google, Chế độ B, AI
theo lịch, không plugin); mốc mới trong `Moc-Han.md` (OAuth do anh tạo; đánh giá sau 1 tháng 28/10/2026); Hướng dẫn 1 trang
người xuất file (.docx theo skill `the-thuc`); hướng dẫn tạo OAuth từng bước; Báo cáo kiểm thử bộ đọc.

## Giai đoạn 1b — Khi anh tạo xong OAuth (em hướng dẫn từng bước)
Anh: Google Cloud (tài khoản `truong.cdkontum@gmail.com`, bật 2 bước) → dự án → bật Sheets/Drive/Gmail API → màn hình
đồng ý **In production** → scope `spreadsheets`, `drive.file`, `gmail.compose` → OAuth client *Desktop* → lưu JSON vào
`%APPDATA%\KTC-Quan-tri\google\`. Em: lần chạy đầu mở trình duyệt để anh đồng ý; tạo Sổ trên Sheets + chia quyền xem 11
đơn vị; chạy `chuyen_mtr_sang_sheets.py`; thử tạo 1 thư nháp; báo cáo lượt chạy thật đầu tiên.

## Giai đoạn 2 — Để sau
Chế độ A (thử C-15 khi anh đang đăng nhập); thư theo từng đơn vị khi `Danh-ba` được xác nhận; đưa skill vào plugin (1.4.0)
sau 1 tháng vận hành và thẩm định vòng 5.

## Kiểm chứng
- `92-Kinh-Nghiem/02-Regression/Cases/test_tiep_nhan_office.py` (ngày giả `28/09/2026`): đáp án Phụ lục A — 23 công việc;
  12 quá hạn / 7 sắp đến hạn / 4 còn hạn; 0 có kết quả; cờ STT 3, STT 2, STT 8; nối STT 21 ↔ 3052, `4357/SNV`; 263 văn bản
  đến (đếm riêng dòng lỗi tách PDF), 3 có ngày hết hạn; gợi ý STT 13 ↔ 945/KH-CĐKT (nếu có trong tệp văn bản đi). Tệp mẫu
  không lên git: thiếu tệp → ca thử báo **bỏ qua có cảnh báo**, không báo sạch.
- Bộ thử tổng hợp: thiếu cột · chạy 2 lần không trùng · STT đổi giữa 2 lần xuất · chủ trì không có trong danh bạ · văn bản
  ngoài kỳ · không có đầu vào · hai lượt chạy chồng · PDF tách lỗi · Claude trả sai lược đồ → `Chưa phân loại`.
- `kiem_tra_he_thong.py`: phép kiểm mới (cấu hình, lược đồ Sổ khớp Từ điển, import script) + ca thử ngược; mã thoát 0
  trước và sau.
- Chạy tay một lượt đầy đủ trên tệp mẫu → xem Sổ (.xlsx) và thư nháp tệp; sau 1b: kiểm Sheet, thư nháp trong Gmail.
