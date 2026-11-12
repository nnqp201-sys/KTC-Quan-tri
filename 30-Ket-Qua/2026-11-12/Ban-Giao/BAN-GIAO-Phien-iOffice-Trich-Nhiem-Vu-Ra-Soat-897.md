# Bàn giao phiên làm việc — iOffice, trích nhiệm vụ, Rà soát 897

**Phiên:** Claude Code (cloud), 24/10 – 12/11/2026 · **Người giao việc:** Nguyễn Ngọc Quang Phục (P-THHC)
**Nhánh:** `claude/charming-cray-lhv264` · PR [nnqp201-sys/KTC-Quan-tri#2](https://github.com/nnqp201-sys/KTC-Quan-tri/pull/2) — **mở, KHÔNG gộp** (chỉ đạo 07/11)

## 1. Đã hoàn thành

| Hạng mục | Sản phẩm | Trạng thái |
|---|---|---|
| Thu thập văn bản iOffice | Skill `29-Cong-Cu/ktc-ioffice/` (+ `tai_file_dinh_kem.js` đoạn mã cố định, chỉ tải ô "File đính kèm") | Thử trên trang mô phỏng đạt 6/6; **chưa chạy trên iOffice thật** |
| Cập nhật CSDL | `29-Cong-Cu/cap_nhat_csdl.py`, `Cap-nhat-CSDL.bat`; `10-Dau-Vao/01-Dau-Moi-Nop/phanloai.py` (luật mở rộng) | Đã chạy thật trên máy (167 VB) |
| Trích nhiệm vụ (AI đọc → máy kiểm → người duyệt) | Skill `29-Cong-Cu/ktc-trich-nhiem-vu/` (mẫu chuẩn TB 1092), `doc_van_ban.py`, `kiem_trich_nhiem_vu.py`, `nap_master.py`, `tong_hop_nhiem_vu.py` | Kiểm đạt trên bộ mẫu; thí điểm 10 VB thật **chưa làm** |
| Rà soát 897 v4.5 bản cá nhân | `2A-KTC-Ra-Soat-897/` (lõi nguyên bản + `Bo-Sung-Ca-Nhan/`), gói `ktc-ra-soat-897-v4.5-ca-nhan.skill` | **Đã vào main** qua [nnqp201-sys/KTC-Quan-tri#1](https://github.com/nnqp201-sys/KTC-Quan-tri/pull/1) |
| Gói gốc 897 | `99-Luu-Tru/KTC-Ra-Soat-897-goc/` (v2.25, v3.0, v4.5, TB 1206, SHA256) | Lưu trữ |

## 2. Quyết định đã chốt
- Trích nhiệm vụ: **AI đọc + script kiểm**, nạp **Master Task Register** sau khi người duyệt (25/10).
- Tải iOffice: chỉ ô **"File đính kèm"**; .docx/.xlsx làm nguồn trích, .pdf ký số làm bản pháp lý; số ký hiệu gắn vào tên tệp lúc tải (28/10).
- 897: **lõi nguyên bản + lớp bổ sung**, không sửa lõi (TB 1206 mục 6); giữ mã `2A-`; không đưa quy ước dấu hai chấm; Hệ C, D **chỉ dùng cá nhân, không gửi** P-QLKH (29/10).
- PR #2: **không gộp** (07/11).

## 3. Việc còn mở (theo thứ tự ưu tiên)
1. **897 đã có v4.6.4** — bản `2A-` (lõi v4.5) đã cũ. Dựng lại trên v4.6.4 theo cùng quy trình (thay lõi, khóa mã băm mới, rà lại lớp bổ sung) khi người phụ trách gửi gói; hoặc bỏ bản cá nhân.
2. Chạy `ktc-ioffice` bản mới trên iOffice thật (upload lại skill), đối chiếu tệp tải với ô "File đính kèm".
3. Thí điểm trích 10 VB thật: đạt khi ≥ 90 % đúng đơn vị + hạn, 0 dòng "nghi bịa", không sót mục.
4. Quyết định số phận PR #2 (giữ mở / đóng); nếu không gộp, công cụ iOffice/trích nhiệm vụ chỉ có trên nhánh.
5. Theo `Pending.md` (main): rà soát đầy đủ thật so bản Team với bản cá nhân; bổ sung NĐ 78, 79, 187/2025 vào KTC-Database; đóng gói lại 1.3.14; kiểm 17 mục lệch kho.
6. Thẩm quyền cấp Task_ID cho `nap_master.py`; Master v0.1 còn dự thảo.

## 4. Mốc hạn quá hạn (sổ `Moc-Han.md`, ngày 12/11/2026)
MH-003 (48 ngày) · MH-004 (39) · MH-005 (36) · **MH-006 (9 ngày — đăng tải kết quả LCNT QĐ 2374, 2375)**. Đã xong thì đóng mốc kèm căn cứ.

## 5. Lưu ý cho phiên sau
- Phiên cloud **không chạm được ổ D:/Drive**; việc trên tệp thật làm bằng Claude Code trên máy.
- Không sửa lõi 897; kiểm bằng `python 29-Cong-Cu/dong_goi_ra_soat_897.py` và `kiem_tra_he_thong.py` (C-897).
- Tệp tải nhầm cũ trong `2026-09/`: `python 29-Cong-Cu/kiem_trich_nhiem_vu.py --tep-nham` để liệt kê, người dùng tự xóa.
