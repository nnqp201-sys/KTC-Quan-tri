# GOAL — Skill `tiep-nhan-office` và tác vụ định kỳ nối VNPT Office → KTC-Quan-tri

> **Lưu tại dự án ngày 28/9/2026** — nguyên văn lệnh người phụ trách giao (tệp đính kèm `GOAL-tiep-nhan-office_v1.1.md`).
> Kế hoạch thực hiện đã duyệt: `Ke-hoach-Tiep-nhan-VNPT-Office_20260928_v1.md` (cùng thư mục). **Chưa thực hiện — chỉ chạy
> khi người phụ trách yêu cầu.** Các quyết định phỏng vấn ngày 28/9/2026 trong kế hoạch được ưu tiên hơn lệnh gốc khi khác nhau
> (vd: giai đoạn 1 chỉ Chế độ B; công cụ trong dự án, chưa vào plugin).

> **Phiên bản lệnh:** v1.1 · **Ngày:** 28/9/2026 · Hiệu chỉnh theo **cấu trúc** các file mẫu xuất ngày 28/9/2026
> **Lưu ý dữ liệu mẫu:** 4 tệp mẫu chỉ dùng để lấy **cấu trúc** (cột, định dạng, cách trình bày). **Không nạp nội dung** của chúng vào Sổ tiếp nhận hay Master Task Register, và không dùng nội dung đó làm căn cứ nghiệp vụ.
> **Người giao:** Nguyễn Ngọc Quang Phục, Phó Trưởng phòng TH-HC&QT, người phụ trách hệ
> **Nơi thực hiện:** Claude Code (VS Code), mở tại thư mục gốc dự án `KTC-Quan-tri/`
> **Quy tắc dùng lệnh:** Mục đánh dấu **[CHỜ]** là chưa có dữ liệu. Nếu có giá trị mặc định thì dùng tạm giá trị đó và ghi rõ trong kế hoạch; nếu không có thì dừng lại và hỏi. Không tự đoán.

---

## 0. Việc phải làm trước khi viết bất kỳ dòng nào

1. Đọc theo thứ tự: `CLAUDE.md` → `90-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md` → `92-Kinh-Nghiem/05-Known-Issues/Pending.md` → `91-Tai-Lieu-Thiet-Ke/Ke-hoach-hop-nhat-KTC-Ke-Hoach-KTC-Bao-Cao-KTC-Theo-Doi.md`.
2. Đọc chuẩn gốc trong `20-Chuan-Chung/`: `00-Nguyen-Tac-Chung.md`, `10-Tu-Dien-Truong-Du-Lieu.md`, `11-Quy-Tac-Task-ID.md`, `12-Vong-Doi-Trang-Thai.md`, `13-Bang-Ma-Don-Vi.md`.
3. Đọc các skill liên quan: `23-KTC-Ke-Hoach/SKILL.md` (Skill 34, 36), `24-KTC-Theo-doi-CV/SKILL.md` (Skill 40, 42, 43) và `.claude/rules/*`.
4. Đọc **4 tệp mẫu (chỉ lấy cấu trúc)** tại `10-Dau-Vao/05-VNPT-Office/2026-09-28/` (anh Phục chép vào trước khi chạy lệnh):
   - `DanhSachCongViecDaGiao_20260928100144.xlsx`
   - `DanhSachVanBan_20260928093028.pdf`
   - `Van_ban_da_xu_ly_Phuc_Cong_22.06-25.09.2026.xlsx`
   - `EMAIL_SU_DUNG_TAI_KHOAN_CLAUDE_AI_TEAM_CAP_NHAT.docx`
5. Chạy `python 29-Cong-Cu/kiem_tra_he_thong.py` để lấy mốc trước khi sửa.
6. Lập kế hoạch thực hiện (kèm đề xuất số thư mục nguồn cho skill mới) và **trình người giao duyệt** trước khi tạo tệp.

## 1. Mục tiêu

Không bỏ sót và không để trễ hạn nhiệm vụ được giao qua **Hệ thống QLVB&ĐH VNPT Office** của Trường. Phạm vi là toàn Trường (11 đơn vị); Phòng TH-HC&QT tham mưu tổng hợp.

**Tiêu chí thành công sau 1 tháng vận hành:**
- 100% công việc trong kỳ ở mục "Quản lý công việc" có mặt trong Sổ tiếp nhận, không có dòng trùng.
- Không có nhiệm vụ nào quá hạn mà chưa được cảnh báo trước.
- Tỷ lệ công việc quá hạn "do chưa cập nhật" giảm dần qua các tuần (mốc lấy từ lượt chạy thật đầu tiên, không lấy từ file mẫu).

## 2. Ba nguồn dữ liệu và vai trò của từng nguồn

| Nguồn (file xuất) | Vai trò trong hệ | Ghi chú từ dữ liệu thật |
|---|---|---|
| **Quản lý công việc** (`DanhSachCongViecDaGiao_*.xlsx`) | **Nguồn nhiệm vụ chính.** Đây là việc đã được giao, đã có chủ trì, ngày giao, hạn và tình trạng | Trên file mẫu, cột "Kết quả thực hiện" và "Kết quả đánh giá" đều trống, nên **không coi "Tình trạng" trên Office là tiến độ thật** |
| **Văn bản đến** (`DanhSachVanBan_*`) | **Nguồn căn cứ, dùng để rà khoảng trống.** Phát hiện văn bản có yêu cầu thực hiện mà chưa có công việc tương ứng, rồi đề xuất cho Trưởng phòng giao việc | **Không có cột bút phê**; cột "Ngày hết hạn" phần lớn để trống. Không dùng nguồn này để sinh nhiệm vụ tự động |
| **Văn bản đi/đã xử lý** (`Van_ban_da_xu_ly_*.xlsx`) | **Nguồn gợi ý minh chứng** cho công việc đã có sản phẩm | Văn bản đi ban hành sau ngày giao việc có thể là sản phẩm của công việc mà Office chưa cập nhật |

## 3. Luồng nghiệp vụ đã chốt

| Bước | Chủ thể | Thời điểm | Nội dung |
|---|---|---|---|
| 1. Lấy dữ liệu | **Chế độ A:** Claude đọc trực tiếp Office qua Claude in Chrome khi phiên đã đăng nhập sẵn (mục 5A). **Chế độ B (dự phòng):** Nguyễn Ngọc Quang Phục, dự phòng Đỗ Thành Công, xuất file | 7h55 và 13h55, thứ Hai–thứ Sáu | Chế độ A: đọc bảng trên trang, lưu bản chụp dữ liệu vào `10-Dau-Vao/05-VNPT-Office/<YYYY-MM-DD>/`. Chế độ B: xuất 3 file vào cùng thư mục, giữ nguyên tên file Office sinh ra |
| 2. Tiếp nhận | Skill `tiep-nhan-office`, chạy theo lịch | 8h10 và 14h10, thứ Hai–thứ Sáu | Đọc file mới nhất của từng loại, lọc theo kỳ, chuẩn hóa, loại trùng, ghi vào Sổ tiếp nhận Office |
| 3. Duyệt | Trưởng phòng TH-HC&QT; Hiệu trưởng khi cần xin ý kiến | Trong ngày | Duyệt từng dòng: công việc Office cần cấp Task_ID, và đề xuất giao việc phát sinh từ văn bản đến |
| 3b. Giao ban | Anh Phục | Sau giao ban tuần | Cập nhật theo Kết luận giao ban qua nhánh `10-Dau-Vao/03-Ket-Luan-Giao-Ban/` (đã có) |
| 4. Cấp Task_ID | `ktc-ke-hoach` | Sau khi duyệt | Chỉ dòng `Đã duyệt` mới được cấp Task_ID và ghi nhóm A–E vào Master Task Register |
| 5. Cảnh báo | `ktc-theo-doi-cv` (Skill 42) | Lượt 8h10 | Tạo thư nháp Gmail trong `truong.cdkontum@gmail.com`. **Giai đoạn 1 (danh bạ chưa phân công):** 1 thư tổng hợp gửi `phongthhcqt@gmail.com`. **Giai đoạn 2 (có danh bạ):** gửi đơn vị chủ trì, CC `phongthhcqt@gmail.com` |
| 6. Gửi | Anh Phục | Sau khi rà | Người gửi tự bấm gửi. **Hệ không tự gửi email.** |

**Kỳ:** tuần tính từ thứ Hai đến thứ Sáu; tháng và quý theo lịch dương. Chỉ xử lý dữ liệu trong kỳ, không quét lại số tồn.

## 4. Ràng buộc bất biến

1. **Không tự đăng nhập VNPT Office**, không dùng mật khẩu, không tự động hóa trình duyệt vào Office. Đầu vào duy nhất là file do người xuất.
2. **Skill mới không cấp Task_ID và không ghi Master Task Register.** Skill chỉ ghi vào Sổ tiếp nhận (vùng chờ).
3. **Không tự gửi email**, chỉ tạo thư nháp (scope `gmail.compose`, không xin scope gửi).
4. **Không so khớp mờ để kết luận.**
   - Nối văn bản với công việc chỉ theo số hiệu trích được từ nội dung, so khóa chính xác gồm `số + ký hiệu cơ quan đầu tiên`. Ví dụ: `4357/SNV` khớp cả `4357/SNV-CCHC` và `4357/SNV-CCHCTN&VTLT`.
   - Khớp theo chủ đề (ví dụ công việc 7 với văn bản 4494/SGDĐT "Tuần lễ học tập suốt đời") chỉ được ghi là **gợi ý**, phải có người xác nhận (bài học KI-001).
5. **Gợi ý minh chứng từ văn bản đi không tự đóng nhiệm vụ.** Chỉ ghi `Minh_Chung_Goi_Y`; việc chuyển trạng thái đi qua Skill 43 và cần người xác nhận.
6. **Đơn vị ghi bằng mã chuẩn** theo `13-Bang-Ma-Don-Vi.md`. Chủ trì trên Office là **tên người**, nên phải quy đổi qua Danh bạ người → đơn vị (mục 6.3). Không quy đổi được thì gắn cờ `Chưa ánh xạ`, không đoán.
7. **Văn bản chỉ để biết** vẫn ghi sổ với trạng thái `Loại` kèm lý do (lịch làm việc, thông báo, quyết định không giao việc…).
8. **Mọi thay đổi có lịch sử** theo Nguyên tắc 5. Kho `KTC-Database` chỉ đọc. Không sao chép quy tắc của hệ khác.

## 5. Nền tảng: thống nhất trên Google

| Lớp | Nền tảng |
|---|---|
| Dữ liệu nền (`KTC-Database`) | Google Drive, chỉ đọc (giữ nguyên) |
| Sổ tiếp nhận Office, Master Task Register | **Google Sheets** thuộc sở hữu `truong.cdkontum@gmail.com`. Chuyển `Master-Task-Register_20260913_v0.1.xlsx` sang Sheets, giữ 4 sheet và 46 cột; bản .xlsx cũ đưa vào `99-Luu-Tru/` |
| Thư nháp cảnh báo | Gmail `truong.cdkontum@gmail.com` |
| Thư mục nhận file | Google Drive, đồng bộ xuống máy chạy bằng Google Drive for Desktop |

**Phân quyền:** 11 tài khoản đơn vị chỉ xem (hoặc nhận xét); người duyệt và người phụ trách hệ được sửa. Dùng bảo vệ vùng để khóa nhóm cột theo hệ (A–E / F–G / H / vùng duyệt).

**Kết nối:**
- Kiểm tra trước tiên kết nối Drive, Sheets và Gmail (tạo nháp) bằng OAuth của `truong.cdkontum@gmail.com`.
- Ứng dụng OAuth phải ở chế độ *In production*; nếu để *Testing* thì token hết hạn sau 7 ngày.
- Token lưu ngoài dự án. Tài khoản chung phải bật xác minh 2 bước.
- Nếu không kết nối được thì dừng và báo.

## 5A. Chế độ A — Claude tự truy cập VNPT Office (đọc trực tiếp)

| Được làm | Không được làm |
|---|---|
| Đọc trang Office trong Chrome **khi phiên đã được người dùng đăng nhập sẵn** (Claude in Chrome) | Nhập mật khẩu, bấm "Đăng nhập", dùng "Sử dụng Token", lưu hoặc đọc mật khẩu đã lưu của trình duyệt |
| Mở các mục Văn bản đến, Quản lý công việc, Văn bản đã xử lý; đọc bảng bằng đọc văn bản trang; chuyển trang danh sách | Bấm nút xử lý, chuyển, ký, trả lại, đánh giá, xóa trên Office — **chỉ đọc** |
| Lưu bản chụp dữ liệu đã đọc vào thư mục đầu vào | Tải file về máy mà không có người xác nhận |

**Quy trình một lượt đọc:** (1) kiểm tra phiên: về màn hình đăng nhập thì **dừng**, ghi `Phiên hết hạn`, nhắc đăng nhập lại, chuyển Chế độ B nếu có file; (2) đọc bảng theo từng trang đến hết kỳ; (3) chuẩn hóa về cấu trúc cột mục 6.2.

**Kết quả thử ngày 28/9/2026:** 2 lần mở "Văn bản đến" đều bị chuyển về trang đăng nhập. **[CHỜ C-15]** nguyên nhân: phiên hết hạn nhanh, hay liên kết menu làm mất tham số phiên. Thử lại khi người giao đang đăng nhập; ghi kết luận vào `92-Kinh-Nghiem/`.

**Giới hạn vận hành:** chỉ chạy khi máy bật, Chrome mở, Office còn phiên; không dùng trong phiên đám mây; phiên hết hạn thường xuyên thì Chế độ B là đường chính.

## 6. Đặc tả dữ liệu đầu vào (theo cấu trúc file mẫu)

### 6.1. `DanhSachCongViecDaGiao_YYYYMMDDHHMMSS.xlsx` — nguồn chính
- Sheet `Report`. Dòng 1–4 là tiêu đề. **Dòng tiêu đề cột là dòng có ô "STT" và "Tên công việc"**; dò động, không cài cứng dòng 5.
- Cột: `STT` · `Mức độ công việc` · `Ngày giao việc` (dd/mm/yyyy, **chuỗi**) · `Ngày hết hạn` (chuỗi) · `Chủ trì` (tên người) · `Tên công việc` · `Tình trạng` · `Kết quả thực hiện` · `Người giao đánh giá` · `Kết quả đánh giá` · `Nội dung trao đổi`.
- **Khóa trùng:** `Ngày giao việc + Chủ trì + băm(Tên công việc đã chuẩn hóa khoảng trắng)`; **không dùng STT**.
- **Cờ bắt buộc:** `Hạn trong nội dung khác hạn hệ thống` · `Nhiều mốc trong nội dung` · `Chủ trì ngoài 11 đơn vị` · `Quá hạn nhưng chưa có kết quả`.
- **Tình trạng Office** chỉ lưu vào `Tinh_Trang_Office`, không thay trạng thái vòng đời của hệ.

### 6.2. `DanhSachVanBan_YYYYMMDDHHMMSS` — văn bản đến
- Cột: `STT` · `Số đến` · `Đơn vị soạn thảo` · `Đơn vị ban hành` · `Số ký hiệu` · `Trích yếu` · `Nơi nhận` · `Ngày hết hạn`.
- **Ưu tiên bản Excel.** PDF làm dính chữ các cột "Nơi nhận", "Đơn vị ban hành", "Số ký hiệu". **[CHỜ C-10]** Office có xuất Excel cho mục này không. Chỉ có PDF thì dùng `pdfplumber` theo tọa độ; dòng lỗi gắn `Tách PDF lỗi`.
- **Khóa trùng:** `Số đến + Số ký hiệu` (VB Đảng dãy 7xx song song dãy chính quyền 3xxx).
- **Phân loại (đề xuất, cần duyệt):** `Có yêu cầu thực hiện` (triển khai, báo cáo, đề nghị, góp ý, đăng ký, khảo sát, cung cấp số liệu) · `Mời họp` → lịch · `Để biết` → `Loại`.
- **Rà khoảng trống:** `Có yêu cầu thực hiện` mà chưa có công việc trích dẫn số hiệu → **"Đề xuất giao việc"**.

### 6.3. Danh bạ người → đơn vị
- Sheet `Danh-ba`: `Ho_Ten | Tai_Khoan_Office | Ma_Don_Vi | Can_Cu | Da_Xac_Nhan`. **Hiện chưa phân công** (quyết định 28/9/2026): để trống, không tự điền; `Ma_Don_Vi` trống → cờ `Chưa ánh xạ`; cảnh báo **Giai đoạn 1**. Có danh bạ xác nhận → Giai đoạn 2.

### 6.4. `Van_ban_da_xu_ly_*.xlsx` — văn bản đi
- Dòng 1–2 tiêu đề; tiêu đề cột dòng 3: `STT` · `Số ký hiệu` · `Loại văn bản` · `Trích yếu` · `Ngày soạn thảo` · `Ngày ban hành` · `Người soạn thảo` · `STT trên hệ thống` · `Ghi chú`; có sheet `Tổng hợp`.
- File mẫu đã lọc theo người soạn; chạy thật lấy bản xuất gốc.
- Gợi ý minh chứng: văn bản ban hành **sau** ngày giao, trích yếu chứa cụm danh từ chính của tên công việc — luôn nhãn "gợi ý".

## 7. Hạng mục công việc

### 7.1. Sổ tiếp nhận Office (Google Sheets)
- Sheet: `01-Cong-viec-Office` · `02-Van-ban-den` · `03-De-xuat-giao-viec` · `04-Goi-y-minh-chung` · `Danh-ba` · `Danh-muc` · `Lich-su-thay-doi` · `Nhat-ky-luot-chay`.
- Mô tả trường bổ sung thành mục mới trong `20-Chuan-Chung/10-Tu-Dien-Truong-Du-Lieu.md`, không sửa trường cũ.
- Trường tối thiểu `01-Cong-viec-Office`: `Ma_Tiep_Nhan` · `Khoa_Trung` · `Ngay_Giao` · `Han_He_Thong` · `Han_Trong_Noi_Dung` · `Chu_Tri_Ten` · `Ma_Don_Vi` · `Ten_Cong_Viec` · `Muc_Do` · `Tinh_Trang_Office` · `Ket_Qua_Office` · `Can_Cu_VB_Den` · `Minh_Chung_Goi_Y` · `Canh_Bao_Du_Lieu` · `Trang_Thai_Duyet` · `Nguoi_Duyet` · `Task_ID` · `File_Nguon` · `Thoi_Diem_Tiep_Nhan`.

### 7.2. Skill `tiep-nhan-office`
- Nguồn trong thư mục `2x-…` (đề xuất khi lập kế hoạch); bản build `31-Plugin/skills/tiep-nhan-office/` (kế hoạch đã duyệt: **chưa vào plugin**).
- Script đọc file **tất định** (Python) tại `29-Cong-Cu/`. AI chỉ phân loại văn bản đến và trích mốc hạn, kèm độ tin cậy.
- `description`: KHÔNG cấp Task_ID, KHÔNG gửi email, KHÔNG soạn văn bản.

### 7.3. Cảnh báo và thư nháp
- Tái sử dụng Skill 42; ngưỡng "sắp đến hạn" mặc định **3 ngày làm việc**, đặt trong tệp cấu hình.
- **Giai đoạn 1:** 1 thư nháp tổng hợp mỗi ngày gửi `phongthhcqt@gmail.com`, nhóm theo người chủ trì. **Giai đoạn 2:** mỗi đơn vị 1 thư nháp gộp/ngày, CC `phongthhcqt@gmail.com`. Chỉ lượt 8h10.
- **Văn phong nhắc cập nhật**, không kết luận vi phạm: "Đề nghị đơn vị cập nhật kết quả thực hiện trên Hệ thống QLVB&ĐH hoặc phản hồi nếu thông tin chưa chính xác". Có `Minh_Chung_Goi_Y`: "Phòng TH-HC&QT ghi nhận văn bản số … có liên quan, đề nghị đơn vị xác nhận để cập nhật hoàn thành".
- **Địa chỉ nhận:**

| Mã | Đơn vị | Gmail |
|---|---|---|
| P-QLKH | Phòng QLKHCN&HTPT | qlkhcn.cdkt@gmail.com |
| P-THHC | Phòng TH-HC&QT (và là địa chỉ **CC** mọi thư) | phongthhcqt@gmail.com |
| P-TCCB | Phòng TCCB&CTHSSV | phongtccbcdkt@gmail.com |
| P-QLDT | Phòng QLĐT&BĐCL | quanlydaotaocdkt@gmail.com |
| P-TCKT | Phòng TC-KT | phongkehoachtaivucdcd@gmail.com |
| K-KTNL | Khoa Kinh tế và Nông Lâm | khoaktnlcdkontum@gmail.com |
| K-KHCB | Khoa các Khoa học cơ bản | khoackhcb2026@gmail.com |
| K-SUPH | Khoa Sư phạm | khoaspcdcdkt2@gmail.com |
| K-DTSHLX | Khoa Đào tạo và Sát hạch lái xe | khoadtshlx.ktc2026@gmail.com |
| K-KTCN | Khoa Kỹ thuật và Công nghệ | kythuatcongnghe26@gmail.com |
| K-YDUOC | Khoa Y – Dược | khoayduoccdkt@gmail.com |
| — | Tài khoản gửi (nơi tạo thư nháp) | truong.cdkontum@gmail.com |

- Chủ trì ngoài 11 đơn vị (Công đoàn…) không tạo thư, chỉ liệt kê trong bản tóm tắt **[CHỜ C-12]**.

### 7.4. Tác vụ định kỳ
- 8h10 và 14h10, T2–T6, Asia/Ho_Chi_Minh; Windows Task Scheduler trên máy cố định; tệp khóa chống chạy chồng.
- Lấy tệp mới nhất từng loại theo **dấu thời gian trong tên**; không có đầu vào → ghi "không có đầu vào"; thiếu 2 lượt liên tiếp → nhắc đầu bản tóm tắt.
- Dự phòng Cowork: chỉ thiết kế, không bật (Cowork chưa có Gmail → chỉ cập nhật sổ). Nhật ký theo `90-Nhat-Ky-Van-Hanh/`.

### 7.5. Kiểm thử và đóng gói
- Phép kiểm mới trong `kiem_tra_he_thong.py` **kèm ca thử ngược**.
- File mẫu 28/9 **chỉ để kiểm bộ đọc**; Phụ lục A là đáp án kiểm thử; không nạp vào sổ.
- Bộ thử bổ sung: thiếu cột · chạy 2 lần không trùng · STT đổi · chủ trì không có trong danh bạ · văn bản ngoài kỳ · không có đầu vào · hai lượt chạy chồng · PDF tách lỗi.
- Phiên bản plugin 1.4.0 (kế hoạch đã duyệt: **để giai đoạn 2**). `kiem_tra_he_thong.py` mã thoát 0 trước và sau.

## 8. Sản phẩm bàn giao
1. Skill `tiep-nhan-office` (nguồn) cùng các script đọc file.
2. Sổ tiếp nhận Office trên Google Sheets và Master Task Register đã chuyển sang Sheets.
3. Cấu hình tác vụ định kỳ (chính và dự phòng) kèm hướng dẫn bật/tắt.
4. Mẫu thư nháp cảnh báo.
5. **Hướng dẫn 1 trang cho người xuất file** (anh Phục, anh Công).
6. **Báo cáo kiểm thử bộ đọc** (đối chiếu Phụ lục A) và **báo cáo lượt chạy thật đầu tiên**.
7. Quyết định vào `92-Kinh-Nghiem/` (mã `DL-…`, gồm quyết định chuyển sang nền Google) và mốc hạn mới vào `Moc-Han.md`.

## 9. Điều kiện dừng và hỏi
Thiếu file đầu vào hoặc cấu trúc cột khác mục 6 · không kết nối được Google · trang Office về màn hình đăng nhập (Chế độ A),
hoặc sắp tạo thư gửi đơn vị khi danh bạ chưa xác nhận · lệnh mâu thuẫn `CLAUDE.md`/`20-Chuan-Chung/` (ưu tiên bản gốc dự án).

## 10. Danh sách [CHỜ] và các mục đã chốt

| Mã | Nội dung | Trạng thái |
|---|---|---|
| C-09 | Danh bạ người → đơn vị | **Đã chốt:** tạm thời chưa phân công → cảnh báo Giai đoạn 1 |
| C-10 | Nguồn "Văn bản đến" | Lệnh gốc: Chế độ A; **kế hoạch 28/9: giai đoạn 1 chỉ Chế độ B** |
| C-11 | Văn bản đi toàn Trường | Lấy qua Chế độ A hoặc B khi chạy thật |
| C-12 | Công việc do Công đoàn, Đoàn, Tổ… chủ trì | Mặc định: nêu trong thư tổng hợp gửi Phòng TH-HC&QT |
| C-13 | Văn bản Đảng (dãy số đến 7xx) | Mặc định: ghi sổ, nhãn `VB Đảng`, không tạo đề xuất giao việc |
| C-14 | Độ phủ dữ liệu | **Đã chốt:** file 28/9 chỉ là mẫu cấu trúc |
| C-15 | Office chuyển về trang đăng nhập khi mở menu | **Chờ** thử lại khi người giao đang đăng nhập |
| — | Hộp thư 11 đơn vị | **Đã chốt:** danh sách mục 7.3 |

## Phụ lục A — Đáp án kiểm thử bộ đọc trên file mẫu 28/9/2026

> Chỉ dùng để kiểm bộ đọc và quy tắc tính hạn. **Không nạp nội dung vào sổ.**

Ngày chạy 28/9/2026 (thứ Hai), ngưỡng 3 ngày làm việc (29/9, 30/9, 01/10):

| Chỉ tiêu | Kỳ vọng |
|---|---|
| Số công việc đọc được | 23 |
| Quá hạn (`Han_He_Thong` < 28/9) | 12 (STT 1–12) |
| Sắp đến hạn (hạn 30/9) | 7 (STT 13–19) |
| Còn hạn, chưa đến ngưỡng | 4 (STT 20–23; hạn 09/10 và 30/10) |
| Có "Kết quả thực hiện" | 0 |
| Cờ `Hạn trong nội dung khác hạn hệ thống` | ít nhất STT 3 |
| Cờ `Nhiều mốc trong nội dung` | ít nhất STT 2 |
| Cờ `Chủ trì ngoài 11 đơn vị` | STT 8 (Công đoàn); STT 6 cần xác nhận (Tổ quản trị HTTT) |
| Gợi ý minh chứng | STT 13 ↔ 945/KH-CĐKT ngày 25/9/2026 |
| Nối căn cứ văn bản đến theo số hiệu | STT 21 ↔ Số đến 3052, 4357/SNV |
| Văn bản đến đọc được | 263 (dòng lỗi tách PDF phải được đếm riêng) |
| Văn bản đến có "Ngày hết hạn" | 3 (Số đến 3254, 3228, 3148) |
