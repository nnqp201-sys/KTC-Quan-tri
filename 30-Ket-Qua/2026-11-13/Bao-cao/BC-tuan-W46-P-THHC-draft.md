# BÁO CÁO TUẦN W46 (09–13/11/2026) — P-THHC — BẢN DỰ THẢO

> ⚠️ **Dự thảo tự động, chờ người phụ trách duyệt.** Chưa rà soát KTC-Ra-Soat-897, chưa đối chiếu KTC-Database. Dữ liệu chỉ lấy từ kho dự án (git, `30-Ket-Qua/`, `90-Nhat-Ky-Van-Hanh/`, `Moc-Han.md`) — **không có dữ liệu Theo-dõi-CV/Office của tuần**; các mục "cần bổ sung" do người phụ trách điền.
> Cửa sổ dữ liệu: 06–13/11/2026. Mẫu: TB 736 Phụ lục IIb (cấu trúc 3 phần; chưa đối chiếu toàn văn mẫu trong kho).

## 1. Dữ liệu thu thập
- **Mốc hạn (`Moc-Han.md`)**: không có mốc nào đóng trong tuần. 4 mốc còn `Mở` và đều quá hạn (xem mục 3).
- **Nhật ký vận hành (`90-…`)**: không có Process-Memory mới trong 7 ngày (mới nhất `PM-20261023`).
- **Sản phẩm xuất (`30-Ket-Qua/`)**: có thư mục 07/11, 08/11. Hồ sơ Đề án Hạng A nằm trong thư mục 02–03/11 (bản v12 ghi ngày 06/11). Không có thư mục 09–13/11.
- **Git (7 ngày)**: 5 commit, 07–08/11 (xem mục 2, Trục 3).

## 2. Tổng hợp theo 6 Trục (TB 817)
| Trục | Nội dung ghi nhận trong tuần | Nguồn |
|---|---|---|
| 1. Đào tạo, tuyển sinh | Không ghi nhận | — |
| 2. Thể chế, cải cách HC | Không ghi nhận riêng. (Hồ sơ Đề án Hạng A — phương án vay, tài chính — chủ yếu xuất 02–06/11; cần người phụ trách xác nhận phân Trục và tiến độ tuần này) | `30-Ket-Qua/2026-11-03/De-an-Hang-A_Ho-so-phuong-an/` |
| 3. KHCN, chuyển đổi số | • Nâng skill `ktc-ra-soat-897` lên v4.6.13-KTC: sửa cổng C1–C6, UTF-8, 6 sub-agent, xử lý PDF scan/chữ ký số, sửa dương tính giả thể thức (07/11) • Cải tiến hệ KTC-Quan-tri P0–P3: `doctor.py`, README, CI (08/11) • Đề xuất cải tiến `DX-Cai-tien-he-KTC-Quan-tri_20261108_v1.md` | git `b04bfd4`…`3d8c2ec`; `30-Ket-Qua/2026-11-08/De-xuat/` |
| 4. Xây dựng Đảng | Không ghi nhận | — |
| 5. Tài chính, nhân sự, tài sản | Không ghi nhận riêng (xem Trục 2 về Đề án Hạng A và mục 3 về đấu thầu) | — |
| 6. QP-AN, đối ngoại | Không ghi nhận (báo cáo hội nghị hợp tác giáo dục lập 04/11, ngoài tuần) | — |

## 3. Nội dung báo cáo

### 3.1. Kết quả nổi bật
1. Hoàn thành nâng cấp công cụ rà soát `ktc-ra-soat-897` v4.6.13-KTC và đợt cải tiến hệ thống (07–08/11) — nền cho khâu rà soát trước trình ký.
2. *(Người phụ trách bổ sung kết quả nghiệp vụ tuần 09–13/11 — kho không có dữ liệu.)*

### 3.2. Việc chưa hoàn thành và nguyên nhân
| Mã | Việc | Hạn | Quá hạn (13/11) | Ghi chú |
|---|---|---|---|---|
| MH-004 | Gửi kế hoạch công tác Quý IV/2026 (PL I, II – QĐ 1923) về P-TCCB&CTHSSV | 04/10 | 40 ngày | Chưa có hướng dẫn Quý IV; mâu thuẫn mốc với MH-005 (Câu hỏi mở số 4) — *cần xác nhận đã làm chưa* |
| MH-005 | Trình chỉ tiêu KPI Quý IV (Phụ lục Bản cam kết) cho Trưởng đơn vị | 07/10 | 37 ngày | *cần xác nhận* |
| MH-006 | Đăng tải kết quả lựa chọn nhà thầu 2 gói (QĐ 2374, 2375/QĐ-CĐKT) lên mạng đấu thầu quốc gia | 03/11 | 10 ngày | Căn cứ: Đ20 TT 79/2025/TT-BTC; K5 Đ33 NĐ 214/2025/NĐ-CP — *cần xác nhận đã đăng chưa* |
| MH-003 | (P-TCCB) Rà soát, trình ký Bản cam kết KPI | 25/09 | 49 ngày | Việc đơn vị khác, phụ thuộc MH-002 — chỉ theo dõi |

Ghi chú: sổ chưa đóng các mốc này; nếu đã làm trên thực tế thì cần cập nhật `Moc-Han.md` (Trạng thái + căn cứ), không xóa dòng.
Việc còn mở khác (`Pending.md`): cập nhật `LOI-V45.sha256`; đóng gói plugin 1.3.14; chờ P-TCCB gán Nhóm/hệ số 39 mã SPCV; kiểm 17 mục lệch kho 897; xóa thủ công worktree bỏ quên.

### 3.3. Kế hoạch tuần tới (W47, 16–20/11/2026) — đề xuất
1. Xử lý/đóng 3 mốc quá hạn của P-THHC (MH-004, 005, 006), ưu tiên MH-006 (đăng tải kết quả lựa chọn nhà thầu).
2. Báo cáo giải ngân tháng 11 (hạn trước ngày 02 tháng sau, QĐ 64/2026/QĐ-UBND) — chuẩn bị số liệu.
3. Hoàn tất tồn đọng công cụ: `LOI-V45.sha256`, đóng gói 1.3.14.
4. Tiếp tục hồ sơ Đề án Hạng A theo chỉ đạo *(người phụ trách xác nhận)*.
5. Chạy `29-Cong-Cu/kiem_tra_he_thong.py` sau mọi chỉnh sửa skill.

---
*Nguồn dựng: Moc-Han.md (13/11/2026), git log 7 ngày, cây `30-Ket-Qua/`. Dự thảo chỉ mang tính tổng hợp; số liệu nghiệp vụ tuần phải do người phụ trách bổ sung và duyệt.*
