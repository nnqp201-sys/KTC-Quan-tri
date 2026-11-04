from pathlib import Path
p=Path(__file__).with_name('_build_quy_trinh.py');s=p.read_text(encoding='utf-8')
s=s.replace("('DT','Điều 7; khoản 4 Điều 8'),('214','Điều 8')","('DT','Điều 7; khoản 4 Điều 8')")
s=s.replace("('DT','Điều 7; khoản 4 Điều 8'),('214','Điều 8; Điều 80')","('DT','Điều 7; khoản 4 Điều 8'),('214','Điều 80')")
s=s.replace('Căn cứ: Điều 8, 78–80 và quy trình tương ứng hình thức được chọn.','Căn cứ: Điều 78–80 và quy trình tương ứng hình thức được chọn.')
s=s.replace("p.add_run(', '+clause+'.')","p.add_run(', '+clause+'.')")
# State precise basis instead of assigning a nonexistent specific NSNN provision.
s=s.replace("('NS','các quy định lập và quyết định dự toán ngân sách')","('NS','Cần xác minh điều khoản và thẩm quyền ngân sách cụ thể của cấp áp dụng')")
s=s.replace("('NS','các quy định kế toán và quyết toán NSNN')","('NS','Cần xác minh điều khoản, mẫu và thời hạn quyết toán năm theo cấp ngân sách, loại đơn vị')")
s=s.replace("('XD','khoản 1 Điều 19; Điều 25; Điều 26; khoản 2 Điều 76'),('217','Điều 30; Điều 31'),('206','Điều 6; Điều 7')","('XD','khoản 1 Điều 19; Điều 25; Điều 26'),('217','Điều 30; Điều 31'),('206','khoản 6 Điều 5; Điều 6; Điều 7; Điều 12')")
# Add separate submission/opening control before evaluation.
needle="row('C','Tiếp nhận, đánh giá hồ sơ và làm rõ"
idx=s.index(needle)
new="""row('C','Đóng thầu, mở thầu theo hình thức cạnh tranh → biên bản và dữ liệu mở thầu','C','C: nộp hồ sơ đúng hạn','P: tổ chuyên gia/tư vấn','–',[('DT','Điều 43'),('214','quy trình tương ứng tại Chương II–IV hoặc Điều 81')],'Có điều kiện khi áp dụng hình thức cạnh tranh; không phát sinh mở thầu cạnh tranh trong chỉ định. HSMT phải xác định hạn nộp, hiệu lực, bảo đảm dự thầu nếu thuộc diện; tuân thủ thao tác trên Hệ thống. Cần xác minh điều khoản và thời hạn cụ thể của phương thức được chọn trước phát hành.')
"""
s=s[:idx]+new+s[idx:]
p.write_text(s,encoding='utf-8')
