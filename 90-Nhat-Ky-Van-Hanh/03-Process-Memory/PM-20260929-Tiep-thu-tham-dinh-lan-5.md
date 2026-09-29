# PM-20260929 — Tiếp thu thẩm định lần 5, plugin 1.3.13, rà soát 897 vòng 5

**Ca:** 04 báo cáo thẩm định lần 5 (ChatGPT 76, Grok 83 - 88, Copilot 94, Gemini 92) trên plugin 1.3.12 và hồ sơ vòng 5.
**Kết quả:** 21 ý kiến — 12 tiếp thu, 3 tiếp thu một phần, 6 không tiếp thu có bằng chứng. Plugin 1.3.13 (dựng lại được từ
commit), nghiệm thu 15 ca trên chính tệp zip, BC tiếp thu lần 5, TB v8, HD v8, BC quá trình v7, phiếu 897 vòng 5, hồ sơ
`30-Ket-Qua/2026-09-29/Ho-So-Tham-Dinh-Vong-6/`.

## Bài học

1. **Kiểm từng nhận định trên tệp thật trước khi xếp loại bên thẩm định.** Ban đầu tưởng Gemini bịa tên tệp (`kpi_calc.py`,
   `ktc_guard.py`, `fill_bc736.py`) — tệp có thật trong gói; chỉ **nội dung nhận định** sai (hệ số đọc từ CSV, guard 2,3 giây
   với 2,7 MB, NĐ 334 không nói về minh chứng, 6 mẫu Excel thống nhất ngày). Giải trình "không tiếp thu" phải kèm số đo.
2. **"Dựng lặp lại được" phải thử bằng checkout sạch, không phải dựng hai lần trên thư mục làm việc.** Hai lần dựng cùng
   thư mục cho cùng băm vẫn che lỗi `core.autocrlf` (thư mục lẫn LF/CRLF). Cách thử: `git -c core.longpaths=true worktree add
   --detach <scratch>/wt <commit>` rồi dựng, so băm (không có `longpaths` thì checkout lỗi vì đường dẫn dài).
3. **Nghiệm thu dùng chung hạn mức với phiên làm việc.** Đợt 10 chạm giới hạn phiên từ lượt 2 — công cụ vẫn ghi kết quả như
   đợt thật (0/15). Nay dò trước bằng một lệnh nhỏ và gắn mã 4 cho đợt có lượt lỗi; đợt lỗi giữ riêng, không xóa.
4. **Lượt trượt do giám khảo chấm oan: ghi rõ, không sửa tiêu chí rồi chạy lại để lấy 15/15** — đó là chọn đợt đẹp. Chỉ
   sửa bộ chấm khi lỗi chấm có tính hệ thống (như regex ca 15 ở đợt 9), và chạy lại **cả bộ**.
5. **Ma trận mô hình phát hiện điều eval một mô hình không thấy:** Haiku 4.5 nhận "Checklist 07" làm căn cứ (2/2 lượt) trong
   khi Opus, Sonnet từ chối đúng — thành khuyến nghị sử dụng, không phải sửa plugin trong thí điểm.
6. **Câu điều kiện về dữ liệu nội bộ lại bị viết rộng hơn Thông báo** ("sau G1 thì xử lý dữ liệu nội bộ" — thiếu điều kiện
   nền tảng đã nghiệm thu). Lặp lại bài học PM-20260927 mục 1: mọi câu "được … khi …" đối chiếu điểm a Mục 3 Phần I Dự thảo
   Thông báo.
7. **Nội dung dài thêm làm khối chữ ký tách trang** (TB v8, BC v7) — sửa bằng `cantSplit` + `keepNext` (hàm `giu_khoi_ky`
   trong `scratchpad/dung_1313.py`); luôn xuất PDF xem trang cuối sau mỗi lần sửa Track Changes.
