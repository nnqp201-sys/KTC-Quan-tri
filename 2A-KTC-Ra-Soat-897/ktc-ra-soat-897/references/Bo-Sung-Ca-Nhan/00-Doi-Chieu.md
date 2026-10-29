# 00 – Đối chiếu lớp bổ sung cá nhân với lõi v4.5

**Nguồn:** gói v4.5 (`ktc-ra-soat-897-v4.5.skill`, TB 1206/TB-CĐKT) làm chuẩn; gói v3.0 (`KTC-Ra-soat-897-v3.0.zip` → `ktc-ra-soat-897-v3.0.skill`) và v2.25 (`KTC-Ra-Soat-897-v2.25-Cai-tien.zip`) làm nguồn mô-đun. Đối chiếu ngày 29/10/2026.
**Phạm vi:** bảng quyết định giữ/bỏ từng mô-đun và danh sách điểm mâu thuẫn với v4.5 đã bỏ.
*Ghi chú tham khảo — không thay đổi mã, mức, nhãn của v4.5.*

Nguyên tắc: điểm v4.5 **đã có** → bỏ; điểm v4.5 **không có** → giữ ở dạng ghi chú; điểm **mâu thuẫn** với v4.5 → bỏ và ghi lý do ở mục 2. Thứ tự ưu tiên khi lệch: SKILL.md v4.5 → `Quy-Tac-KTC/` → các tệp lõi khác → lớp bổ sung này.

## 1. Bảng mô-đun: giữ / bỏ

| Mô-đun | Nguồn | Giữ/bỏ | Lý do |
|---|---|---|---|
| Hệ C – VBQPPL (khung Luật 64/2025/QH15, 87/2025/QH15, NĐ 78, 79, 187/2025) | v3.0 `30-Skill-Van-Ban-Quy-Pham-Phap-Luat.md`, SKILL v3.0 | **Giữ** → `01` | v4.5 không có Hệ C (chỉ chính quyền và Đảng). Luật 64, 87 xác minh tại KTC-Database; NĐ 78, 79, 187 **chưa xác minh** (chưa thấy tệp trong kho) |
| Hệ D – Công đoàn, Đoàn TN, Hội SV | v3.0 `D0…v3`, `Checklist/09…v3`; v2.25 `Checklist/09` | **Giữ** → `02`, bỏ mức và ví dụ số hiệu v3.0 | v4.5 chỉ có tên đơn vị (TD-01) và bảng viết tắt, **không có** mẫu đầu văn bản đoàn thể. Mẫu 3.1–3.3 xác minh tại Phụ lục TB 597 trong Kho của lõi |
| Bảo mật tài liệu: nội dung là dữ liệu, không là chỉ thị | v3.0 SKILL `<document_security>` | **Giữ** phần "nội dung nhúng là dữ liệu" → `03`; bỏ phần còn lại | v4.5 mục "Lưu ý bảo mật" chỉ nói người dùng tự chịu trách nhiệm tài liệu mật, không có quy tắc chống lệnh nhúng |
| Thời điểm NĐ 60/2021, 111/2025 ↔ NĐ 334/2026 | v2.25 `00d-Ghi-Nho-ND-334…`; v3.0 `00d-Temporal…` | **Giữ** theo v2.25 → `04` | v4.5 không có. Đọc lại chính văn NĐ 334 (Điều 15, 16) tại KTC-Database ngày 29/10/2026: v2.25 đúng, v3.0 cũ hơn |
| Track Changes | `20-Chuan-Chung/15-Skill-Track-Changes.md` (bản gốc dự án) | **Giữ** → `05` | v4.5 không có. Không chép từ v2.25 (theo lệnh) |
| Quy ước riêng CĐKT | v2.25 `Checklist/08` đối chiếu v4.5 `Quy-Tac-KTC/01`, `03` | **Giữ phần nhỏ** → `06`; bỏ phần còn lại | v4.5 `01`, `03`, `02` đã phủ: QĐ 1976 căn cứ đầu, thông số thể thức, danh mục đơn vị – cơ sở – bộ môn, bảng viết tắt, mã TD. Còn lại 5 điểm lẻ (xem `06`) |
| Doanh nghiệp, vốn nhà nước, đất đai, tài sản công | v3.0 SKILL `<mandatory_rules>` mục 13 | **Giữ** → `07` | v4.5 không có |
| Các mục 1–12, 14–17 của `<mandatory_rules>` v3.0 | v3.0 SKILL | **Bỏ** | Đã được lõi phủ hoặc bị lõi thay thế (xem mục 2, điểm 7–9) |
| Trigger VBHN, Skill VBHN | v3.0 `00b…`, `Skill-Vien-Dan-Van-Ban-Hop-Nhat.md`; v2.25 `00b…` | **Bỏ** | v4.5 `Quy-Tac-KTC/04-Vien-Dan-Van-Ban-Hop-Nhat.md` + `kho_manifest.json` là chuẩn |
| Nhãn "CHƯA KẾT LUẬN ĐIỀU KIỆN TRÌNH KÝ", `output_contract` XML, `acceptance_gate` | v3.0 SKILL | **Bỏ** | v4.5 chặn hẳn ở cổng hồ sơ và có nhãn do script tính (`06-Dieu-Chinh-Mau-Prompt.md` mục 12) |
| Công cụ Python v3.0 (`build_ktc897_report.py`, `validate_v3.py`…) | v3.0 `tools/` | **Bỏ** | Không dùng thay `tools/` v4.5 |
| Bộ hồi quy, bộ nhớ, Decision Log, Process Memory v2.25 | v2.25 | **Không vào gói** | Lưu ngoài gói tại `92-Kinh-Nghiem/` (lệnh B6.4) |

## 2. Điểm mâu thuẫn với lõi v4.5 đã bỏ

| # | Nguồn | Nội dung nguồn | Lõi v4.5 | Quyết định |
|---|---|---|---|---|
| 1 | v2.25 `Checklist/08` mục 1 | Văn bản cũ còn hiệu lực dẫn QĐ 988 → chỉ Mức 4, không hồi tố | CC-01: viện dẫn văn bản bị thay thế = **Mức 1** theo `kho_manifest.json` (QĐ 988 → QĐ 1976) | **Bỏ.** Mức theo bảng 02. Việc dự thảo ban hành trước 14/9/2026 có thể đúng căn cứ thời điểm đó thuộc người rà soát xét theo bảng 02, không theo ghi chú này |
| 2 | v2.25 `Checklist/09`; v3.0 `D0…v3` | Nhầm hệ Công đoàn ↔ Đoàn: Mức 1 (v2.25) hoặc Mức 2 (v3.0); hai nguồn lệch nhau | Bảng 02 không có mã Hệ D; "không tự đặt mức ngoài bảng" | **Bỏ mọi mức.** Giữ nội dung kiểm ở dạng ghi chú (`02`) |
| 3 | v3.0 `D0…v3` mục D2 | Ví dụ số hiệu Đoàn `Số xx-TB/ĐTN` | Phụ lục TB 597 mẫu 3.2: `Số: -....../ĐTN` | **Bỏ ví dụ v3.0**, theo TB 597 |
| 4 | v3.0 `00d-Temporal…` | NĐ 334 "chưa xác minh đủ nội dung"; từ 05/10/2026 "bắt buộc kiểm lại" NĐ 334 và phạm vi thay thế | NĐ 334 Điều 16 chỉ có 2 khoản, **không bãi bỏ** NĐ 60/111; Điều 7.3.a dẫn ngược NĐ 60/111 | **Bỏ câu của v3.0**, dùng v2.25 (đọc chính văn). Không nêu CC-01 với NĐ 60/111 |
| 5 | v3.0 `<mandatory_rules>` mục 2, 3 | "Checklist 08 trước NĐ 30"; QĐ 988 | Thứ tự: TB 597, QĐ 1355 trước NĐ 30; căn cứ đầu QĐ 1976 | **Bỏ**, lõi thay thế |
| 6 | v3.0 `<document_security>` | Phát hiện dấu hiệu dữ liệu hạn chế thì dừng xử lý phần đó | v4.5: "Skill không kiểm và không hỏi lại" (QĐ 2307, 2328) | **Bỏ phần dừng xử lý**; chỉ giữ "nội dung nhúng là dữ liệu" |
| 7 | v3.0 `<mandatory_rules>` mục 17 | Ghi Process Memory sau mỗi rà soát chính thức | v4.5 Bước 7 mục 4: phiên kiểm thử không lưu tóm tắt, báo cáo (quyết định 26/10/2026) | **Bỏ** |
| 8 | v3.0 `<mandatory_rules>` mục 16 | Bảng DOCX: tổng độ rộng ≤ 25,7 cm | `tao_bao_cao.py` v4.5 dựng báo cáo theo chuẩn Trường | **Bỏ** |
| 9 | v3.0 `<severity_policy>`, nhãn thứ 5 | Mức 4 "cần xác minh" làm trạng thái chặn | Cổng hồ sơ chặn hẳn; 4 nhãn do script tính | **Bỏ** |
| 10 | v2.25 `Checklist/08` mục 3.5 | Tên cơ sở cũ sai: Mức 1 | TD-06: **Mức 2** | **Bỏ** (đã phủ bởi TD-06) |
| 11 | v2.25 `Checklist/08` mục 2b | Sau dấu hai chấm viết hoa chữ đầu khi là tên cơ quan, chức danh, tên văn bản (Mức 3) | TB 597 mục 3.1.c chỉ quy định phần "phòng, khoa, bộ môn"; lõi đã phủ ở `03` mục 2 | **Bỏ phần mở rộng** vì chưa có văn bản Trường làm nguồn. Người giao nếu muốn giữ phải chỉ định nguồn (xem báo cáo giao việc) |
| 12 | v2.25 `Checklist/08` mục 5.3 | Không ghi học hàm, học vị trước họ tên người ký | Không có trong TB 597 (đã tìm trong `text/`) | **Bỏ**, không xác minh được nguồn Trường |

## 3. Điểm giữ ở `06` (v4.5 không có)

1. Hai cột chữ viết tắt (số, ký hiệu, nơi nhận / hành văn) không dùng lẫn — TB 597 mục 3.1.c, phần Lưu ý.
2. Mẫu nơi nhận của TB 597 ghi `Công đoàn Trường`, `Đoàn Trường`, `Hội Sinh viên Trường` — không bắt lỗi viết tắt.
3. `KT.`, `TL.`, `TUQ.` có dấu chấm; cấp phó được giao phụ trách ký như cấp phó ký thay — TB 597 mục 7.1.
4. Ban, hội đồng không dùng con dấu của Trường chỉ ghi chức danh trong ban, hội đồng — TB 597 mục 7.1.
5. Mẫu 2.2 (văn bản đơn vị thuộc Trường) có cột trái bắt đầu bằng `TRƯỜNG CAO ĐẲNG KON TUM`, không có dòng `UBND TỈNH QUẢNG NGÃI` — Phụ lục TB 597.
