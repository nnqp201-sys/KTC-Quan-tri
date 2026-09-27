# Bộ ca nghiệm thu plugin KTC-Quan-tri (Claude Code)

**15 ca** từ 1.3.1: ca 01–06 (thẩm định lần 2) + ca 07–15 (thẩm định lần 3, ChatGPT P1-3 — 3 ca cho mỗi luồng rủi ro
cao: KPI 07–09, báo cáo 10–12, soạn thảo 13–15). Ca 07–15 có **bộ chấm tất định** (`type: regex` — mã cảnh báo,
trạng thái, chuỗi bắt buộc có/không có) chạy cùng giám khảo LLM; ca 14 chấm hoàn toàn bằng regex.

6 ca theo yêu cầu thẩm định độc lập lần 2 (ChatGPT mục 5.2.7, 8-P1.3): kích hoạt đúng · không kích hoạt · câu lệnh độc
hại trong dữ liệu · thiếu nguồn "cứ làm" · thang điểm chưa ban hành · ghi vào kho chuẩn (thư mục KTC-Database GIẢ trong
thư mục tạm — không đụng kho thật).

Chạy: `python 29-Cong-Cu/chay_nghiem_thu_code.py` — chép 31-Plugin + bộ ca sang `29-Cong-Cu/_trung_gian/eval-run/`,
chạy `claude plugin eval`, lưu kết quả vào `30-Ket-Qua/<ngày>/Nghiem-thu/`. Trên Claude (trò chuyện) và Cowork, dùng
cùng 6 lời nhắc này làm kịch bản thử tay, ghi kết quả vào biên bản.
