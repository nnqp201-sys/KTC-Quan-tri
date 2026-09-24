# Sổ mốc hạn — việc đang mở có hạn cụ thể

Nguồn cho `29-Cong-Cu/kiem_moc_han.py` (tự chạy đầu mỗi phiên trong dự án, qua `.claude/settings.json`).
Chỉ ghi **mốc hạn thật** đã có trong văn bản hoặc quyết định — không ghi hạn gợi ý trong dự thảo.

Quy ước:
- **Hạn** ghi `dd/mm/yyyy`. Mốc không có ngày cụ thể thì không đưa vào sổ.
- **Trạng thái**: `Mở` · `Chưa rõ` (chưa xác nhận đã làm hay chưa) · `Xong` · `Hủy`. Script chỉ cảnh báo `Mở` và `Chưa rõ`.
- Khi đóng một mốc: đổi trạng thái, ghi ngày và căn cứ vào cột Ghi chú — **không xóa dòng** (Nguyên tắc 5).
- Đơn vị ghi bằng mã chuẩn (`20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`).

| Mã | Việc | Đơn vị | Hạn | Trạng thái | Nguồn | Ghi chú |
|---|---|---|---|---|---|---|
| MH-001 | Rà soát, góp ý Danh mục sản phẩm/công việc; gửi P-TCCB qua Office | P-THHC | 20/09/2026 | Xong | TB 1052/TB-CĐKT (15/9/2026), mục 3.1 | Bản góp ý đã soạn: `30-Ket-Qua/2026-09-19/De-xuat/Gop-y-Danh-muc-SP-TB-1052.md` · **Xong** — người phụ trách hệ xác nhận đã làm (24/9/2026; ngày gửi chưa ghi) |
| MH-002 | Triển khai viên chức ký cam kết thực hiện nhiệm vụ theo KPI; gửi P-TCCB qua Office | P-THHC | 21/09/2026 | Xong | TB 1052/TB-CĐKT (15/9/2026), mục 3.1 | Mẫu Bản cam kết đã có trong kho từ 23/9/2026: `02-KTC-Regulations/02-01-…/TB-1052-TB-CDKT_Mau-Ban-cam-ket-thuc-hien-nhiem-vu-KPI.docx` (trước đó thiếu — `DL-20260919-007`) · **Xong** — người phụ trách hệ xác nhận đã làm (24/9/2026; ngày gửi chưa ghi) |
| MH-003 | Rà soát, trình ký các Bản cam kết KPI toàn Trường | P-TCCB | 25/09/2026 | Mở | TB 1052/TB-CĐKT (15/9/2026), mục 3.2 | Việc của đơn vị khác — theo dõi vì phụ thuộc MH-002 |
| MH-004 | Gửi kế hoạch công tác Quý IV/2026 theo mẫu PL I, PL II (QĐ 1923) về Phòng TCCB&CTHSSV | P-THHC | 04/10/2026 | Mở | QĐ 1923/QĐ-CĐKT, Đ15.3a ("trước ngày 05 tháng đầu quý") | Chưa có hướng dẫn Quý IV; mâu thuẫn mốc với MH-005 — Câu hỏi mở số 4 (`28-KTC-KPI/references/Cau-Hoi-Mo.md`) |
| MH-005 | Viên chức trình chỉ tiêu KPI Quý IV/2026 (Phụ lục kèm Bản cam kết) cho Trưởng đơn vị phê duyệt | P-THHC | 07/10/2026 | Mở | QĐ 1923/QĐ-CĐKT, Đ13.1 (05 ngày làm việc đầu quý) | Công cụ: skill `ktc-kpi-lap-ke-hoach` |
