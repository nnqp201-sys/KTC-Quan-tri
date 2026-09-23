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
| MH-001 | Rà soát, góp ý Danh mục sản phẩm/công việc; gửi P-TCCB qua Office | P-THHC | 20/09/2026 | Chưa rõ | TB 1052/TB-CĐKT (15/9/2026), mục 3.1 | Bản góp ý đã soạn: `30-Ket-Qua/2026-09-19/De-xuat/Gop-y-Danh-muc-SP-TB-1052.md` — chưa xác nhận đã gửi |
| MH-002 | Triển khai viên chức ký cam kết thực hiện nhiệm vụ theo KPI; gửi P-TCCB qua Office | P-THHC | 21/09/2026 | Chưa rõ | TB 1052/TB-CĐKT (15/9/2026), mục 3.1 | Thiếu mẫu Bản cam kết "kèm theo" (`DL-20260919-007`) |
| MH-003 | Rà soát, trình ký các Bản cam kết KPI toàn Trường | P-TCCB | 25/09/2026 | Mở | TB 1052/TB-CĐKT (15/9/2026), mục 3.2 | Việc của đơn vị khác — theo dõi vì phụ thuộc MH-002 |
