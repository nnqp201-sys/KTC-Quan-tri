from pathlib import Path
p=Path(__file__).with_name('_build_quy_trinh.py')
s=p.read_text(encoding='utf-8')
replacements={
'Với BCKTKT không tách dự toán công trình khi khoản 2 Điều 76 Luật Xây dựng quy định không phải lập; chi phí xây dựng xác định theo thiết kế BVTC trong tổng mức đầu tư.':'BCKTKT phải có dự toán xây dựng công trình trong tổng mức đầu tư theo khoản 6 Điều 5 NĐ 206; xác định theo Điều 12. Không bỏ dự toán với lý do chỉ thiết kế một bước.',
'Với BCKTKT không yêu cầu một dự toán công trình tách riêng ngoài tổng mức đầu tư theo khoản 2 Điều 76 Luật Xây dựng; vẫn phải có đủ cơ sở tính toán chi phí xây dựng từ thiết kế.':'Khoản 6 Điều 5 Nghị định 206 quy định tổng mức đầu tư của BCKTKT gồm dự toán xây dựng công trình theo Điều 12, chi phí bồi thường, hỗ trợ, tái định cư nếu có và các chi phí liên quan tính chung cho dự án. Vì vậy phải lập đủ dự toán thành phần trong BCKTKT; không suy từ thiết kế một bước để miễn lập dự toán.',
'Đối chiếu khoản 1 Điều 48 về thời hạn gửi thông báo ít nhất 03 ngày làm việc; không hiểu thông báo là giấy chấp thuận khởi công.':'Gửi trước khi khởi công theo khoản 2 Điều 12 NĐ 207, Mẫu Phụ lục V. Quy định này không đặt mốc chung 03 ngày làm việc; không hiểu thông báo là giấy chấp thuận khởi công.',
'KHLCNT thuộc diện đăng tải trong 05 ngày làm việc từ ngày ban hành theo khoản 1 Điều 8 Luật.':'KHLCNT đăng tải chậm nhất 05 ngày làm việc từ ngày ban hành theo khoản 4 Điều 8 Luật.',
'kết quả thuộc thông tin theo khoản 1 Điều 8 Luật thì công khai trong 05 ngày làm việc từ ngày ban hành.':'kết quả thuộc thông tin quy định tại khoản 4 Điều 8 Luật phải công khai chậm nhất 05 ngày làm việc từ ngày ban hành.',
"('206','Điều 5; Điều 6; Điều 12; Điều 22')":"('206','khoản 6 Điều 5; Điều 6; Điều 12; Điều 22')",
"('DT','Điều 7; Điều 8'),('214','Điều 8')":"('DT','Điều 7; khoản 4 Điều 8'),('214','Điều 8')",
"('DT','Điều 7; Điều 8'),('214','Điều 8; Điều 80')":"('DT','Điều 7; khoản 4 Điều 8'),('214','Điều 8; Điều 80')",
}
for a,b in replacements.items():
 if a not in s: print('MISSING REPLACEMENT',a[:80])
 s=s.replace(a,b)
# Add reliable statutory archival duration, without assigning it to other categories.
s=s.replace("Cần xác minh thời hạn bảo quản theo từng nhóm hồ sơ xây dựng, kế toán, đấu thầu và quy chế lưu trữ áp dụng.","Hồ sơ lựa chọn nhà thầu tối thiểu 05 năm từ quyết toán hợp đồng theo khoản 6 Điều 9 Luật Đấu thầu, trừ nhóm hồ sơ luật quy định khác; hồ sơ hủy thầu theo khoản 4. Cần xác minh thời hạn xây dựng/kế toán riêng.")
s=s.replace("('DT','khoản 8 Điều 78')","('DT','khoản 4–6 Điều 9; khoản 8 Điều 78')")
p.write_text(s,encoding='utf-8')
print('Corrected legal citations and requirements')
