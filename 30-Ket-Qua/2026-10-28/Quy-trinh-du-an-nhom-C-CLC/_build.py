from pathlib import Path
from copy import deepcopy
import json,unicodedata
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'Quy-trinh-du-an-nhom-C_Truong-CLC_CTMTQG_20261028.docx'
NAME='Đầu tư, cải tạo các công trình phục vụ người học, nhà giáo và mua sắm bổ sung thiết bị đáp ứng mục tiêu xây dựng Trường Cao đẳng Kon Tum trở thành trường cao đẳng chất lượng cao giai đoạn 2026 - 2030'
S={
'ĐTC':('Luật Đầu tư công ngày 29/11/2024 (VBHN 03/VBHN-VPQH ngày 05/02/2026)','https://congbao.chinhphu.vn/van-ban/van-ban-hop-nhat-so-03-vbhn-vpqh-468932.htm'),
'358':('NĐ 358/2025/NĐ-CP','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-358-2025-nd-cp-468567.htm'),
'387':('NĐ 387/2026/NĐ-CP','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-387-2026-nd-cp-470814.htm'),
'XD':('Luật Xây dựng ngày 10/12/2025','https://congbao.chinhphu.vn/van-ban/luat-so-135-2025-qh15-468695.htm'),
'217':('NĐ 217/2026/NĐ-CP (đọc VBHN 91/2026/VBHN-NĐ-BXD)','https://xdcs.cdnchinhphu.vn/446259493575335936/2026/9/29/91-vbhn-bxd-signed-1790654585945447247778.pdf'),
'206':('NĐ 206/2026/NĐ-CP','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-206-2026-nd-cp-469768.htm'),
'207':('NĐ 207/2026/NĐ-CP','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-207-2026-nd-cp-469769.htm'),
'210':('NĐ 210/2026/NĐ-CP','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-210-2026-nd-cp-469772.htm'),
'ĐT':('Luật Đấu thầu ngày 23/6/2023 (VBHN 74/VBHN-VPQH)','https://congbao.chinhphu.vn/van-ban/van-ban-hop-nhat-so-74-vbhn-vpqh-469204.htm'),
'214':('NĐ 214/2025/NĐ-CP đã sửa đổi (VBHN 36/2026/VBHN-NĐ-BTC)','https://chinhphu.vn/?docid=219604&pageid=27160'),
'254':('NĐ 254/2025/NĐ-CP — phần thanh toán còn hiệu lực','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-254-2025-nd-cp-46303.htm'),
'193':('NĐ 193/2026/NĐ-CP','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-193-2026-nd-cp-469703.htm'),
'73':('TT 73/2026/TT-BTC','https://congbao.chinhphu.vn/van-ban/thong-tu-so-73-2026-tt-btc-469924.htm')}
INV={x['id']:x for x in json.loads((ROOT/'_research/inventory.json').read_text(encoding='utf-8')) if 'id' in x}
for key,sid,label in [('2158','S011','QĐ 2158/QĐ-CĐKT ngày 29/9/2026'),('2161','S024','QĐ 2161/QĐ-CĐKT ngày 29/9/2026 và phụ lục S022'),('2236','S019','QĐ 2236/QĐ-CĐKT ngày 07/10/2026'),('2374','S033','Kết quả trên Hệ thống — QĐ 2374/QĐ-CĐKT ngày 27/10/2026'),('2375','S027','Kết quả trên Hệ thống — QĐ 2375/QĐ-CĐKT ngày 27/10/2026'),('805','S060','QĐ 805/QĐ-UBND ngày 11/9/2026'),('56','S062','NQ 56/NQ-HĐND ngày 28/8/2026'),('64','S055','QĐ 64/2026/QĐ-UBND ngày 25/5/2026'),('BC','S006','Báo cáo giải ngân lập tháng 10/2026'),('HĐ','S031','Dự thảo hợp đồng tư vấn khảo sát và lập BCKTKT')]:
 S[key]=(label,Path(INV[sid]['path']).as_uri())

doc=Document(ROOT/'_base.docx')
ordinary=deepcopy(doc.paragraphs[9]._p)
# Keep the original template's heading table and its drawing/rule runs.
head=doc.tables[0]
def replace_text(p,text):
 runs=[r for r in p.runs if r.text]
 if runs:
  runs[0].text=text
  for r in runs[1:]:r.text=''
 else:p.add_run(text)
replace_text(head.cell(0,0).paragraphs[0],'UBND TỈNH QUẢNG NGÃI')
replace_text(head.cell(0,0).paragraphs[1],'TRƯỜNG CAO ĐẲNG KON TUM')
replace_text(head.cell(1,0).paragraphs[0],'DỰ THẢO HƯỚNG DẪN')
replace_text(head.cell(1,1).paragraphs[0],'Quảng Ngãi, ngày 28 tháng 10 năm 2026')
head.autofit=False
for rowh in head.rows:
 for ch in rowh.cells:ch.width=Cm(12.35)
for colh in head.columns:colh.width=Cm(12.35)
for g in head._tbl.tblGrid.gridCol_lst:g.set(qn('w:w'),str(round(12.35/2.54*1440)))
hw=head._tbl.tblPr.find(qn('w:tblW'))
if hw is not None:hw.set(qn('w:type'),'dxa');hw.set(qn('w:w'),str(round(24.7/2.54*1440)))
bodyel=doc._element.body
for e in list(bodyel):
 if e is not head._tbl and e.tag!=qn('w:sectPr'):bodyel.remove(e)
for sec in doc.sections:
 sec.page_width=Cm(29.7);sec.page_height=Cm(21)
 sec.top_margin=Cm(2);sec.bottom_margin=Cm(2);sec.left_margin=Cm(3);sec.right_margin=Cm(2)
 sec.header_distance=Cm(.8);sec.footer_distance=Cm(.8);sec.different_first_page_header_footer=True
 # Clear inherited page numbering and use centered top page numbers except page 1.
 for part in [sec.header,sec.footer,sec.first_page_header,sec.first_page_footer]:
  for child in list(part._element):part._element.remove(child)
  part.add_paragraph()
 hp=sec.header.paragraphs[0] if sec.header.paragraphs else sec.header.add_paragraph();hp.alignment=WD_ALIGN_PARAGRAPH.CENTER
 fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');hp._p.append(fld)
for st in doc.styles:
 if st.type in (1,2):
  st.font.name='Times New Roman';st.font.size=Pt(14);st.font.color.rgb=RGBColor(0,0,0)

def para(t='',bold=False,center=False):
 e=deepcopy(ordinary)
 for c in list(e):
  if c.tag!=qn('w:pPr'):e.remove(c)
 bodyel.insert(len(bodyel)-1,e)
 from docx.text.paragraph import Paragraph
 p=Paragraph(e,doc._body);p.add_run(t).bold=bold
 p.paragraph_format.first_line_indent=Cm(1)
 p.paragraph_format.space_after=Pt(6);p.paragraph_format.line_spacing=1.04
 p.paragraph_format.keep_with_next=False
 p.alignment=WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.JUSTIFY
 if center:p.paragraph_format.first_line_indent=Cm(0)
 return p
def title(t):
 p=para(t,True,True);p.paragraph_format.keep_with_next=True;return p
def heading(t):
 p=para(t,True);p.paragraph_format.first_line_indent=Cm(0);p.paragraph_format.keep_with_next=True;return p
def link(p,label,url):
 h=OxmlElement('w:hyperlink');h.set(qn('r:id'),p.part.relate_to(url,RT.HYPERLINK,is_external=True))
 r=OxmlElement('w:r');pr=OxmlElement('w:rPr');f=OxmlElement('w:rFonts')
 for a in ['ascii','hAnsi','eastAsia','cs']:f.set(qn('w:'+a),'Times New Roman')
 pr.append(f);sz=OxmlElement('w:sz');sz.set(qn('w:val'),'28');pr.append(sz)
 r.append(pr);tx=OxmlElement('w:t');tx.text=label;r.append(tx);h.append(r);p._p.append(h)
def refs(p,items,inline=False):
 for i,(k,cl) in enumerate(items):
  if i:p.add_run('; ' if inline else '\n')
  link(p,S[k][0],S[k][1]);p.add_run('; '+cl+'.')
def text(t,items=[]):
 p=para(t)
 if items:p.add_run(' ');refs(p,items,inline=True)
 return p

title('QUY TRÌNH THỰC HIỆN DỰ ÁN NHÓM C')
title('Đầu tư xây dựng và mua sắm thiết bị — vốn đầu tư công thuộc CTMTQG')
text('Áp dụng cho Dự án “'+NAME+'”.')
text('Nguồn vốn: Vốn đầu tư thuộc Chương trình mục tiêu quốc gia xây dựng nông thôn mới, giảm nghèo bền vững và phát triển kinh tế - xã hội vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026 - 2035, giai đoạn I: Từ năm 2026 đến năm 2030; cơ cấu ngân sách trung ương và ngân sách tỉnh theo kế hoạch vốn do cấp có thẩm quyền giao.')
text('Tài liệu làm việc cập nhật đến ngày 28/10/2026; gồm 5 phần, bảng 8 cột và 6 giai đoạn. Đây là dự thảo hướng dẫn để hoàn thiện hồ sơ, không thay quyết định đầu tư, quyết định giao vốn hoặc văn bản phân cấp. Trạng thái hồ sơ chỉ phản ánh tài liệu đọc được, không xác nhận thay bản gốc có chữ ký số/chữ ký hợp lệ.')
heading('PHẦN 1. CƠ SỞ ÁP DỤNG VÀ MỐC HỒ SƠ CỦA DỰ ÁN')
heading('1. Phân loại và phạm vi công việc')
text('Theo Quyết định 2158, sơ bộ tổng mức đầu tư dự kiến 24.894.000.000 đồng; cải tạo 03 ký túc xá (nhà G và H, mỗi nhà khoảng 2.640 m²; ký túc xá tại cơ sở Khoa Kỹ thuật - Công nghệ và Đào tạo - Sát hạch lái xe khoảng 2.400 m²), mua 02 mô hình xe ô tô con số tự động phục vụ đào tạo. Phạm vi cuối cùng phải theo quyết định đầu tư/BCKTKT được duyệt. Không dùng quy mô đề xuất cũ hoặc hiểu mô hình đào tạo là xe ô tô phục vụ công tác.',[('2158','Điều 1')])
text('Dự án giáo dục thuộc nhóm C khi tổng mức đầu tư dưới 90 tỷ đồng theo khoản 4 Điều 11 Luật Đầu tư công. Với tổng mức sơ bộ nêu trên, đối chiếu điều kiện lập BCKTKT tại điểm b khoản 2 Điều 27 Nghị định 217 (không quá 40 tỷ đồng, loại trừ các khoản luật quy định). BCKTKT thiết kế một bước phải có bản vẽ thi công và dự toán xây dựng, cùng chi phí thiết bị và các chi phí của toàn dự án; ngưỡng nhóm C và ngưỡng BCKTKT là hai phép kiểm khác nhau.',[('ĐTC','khoản 4 Điều 11'),('217','khoản 2 Điều 27; Điều 30–31'),('206','khoản 6 Điều 5; Điều 12')])
heading('2. Chủ trương đầu tư, thẩm quyền và chuyển tiếp CTMTQG')
text('Dự án thuộc chương trình mục tiêu quốc gia không phải quyết định chủ trương đầu tư riêng theo điểm d khoản 6 Điều 19 Luật Đầu tư công; nhiệm vụ chuẩn bị đầu tư cũng thuộc điểm a cùng khoản. Phải có căn cứ xác định đúng dự án nằm trong Chương trình, danh mục và kế hoạch vốn hợp pháp. Việc miễn bước chủ trương riêng không miễn lập, thẩm định, quyết định đầu tư, kế hoạch vốn, lựa chọn nhà thầu và quyết toán.',[('ĐTC','khoản 6 Điều 19; Điều 39; Điều 43')])
text('Trường được ghi là cơ quan tổ chức chuẩn bị dự án tại Quyết định 2158; phụ lục vốn kèm Quyết định 2161 có tên Trường ở cột chủ đầu tư. Cần tập hợp văn bản giao/phân cấp đầy đủ để xác nhận tư cách ở từng giai đoạn. Không suy từ quyền Hiệu trưởng duyệt dự toán chuẩn bị và KHLCNT sang quyền duyệt đầu tư/BCKTKT. Quyền của đơn vị sự nghiệp đối với nguồn thu hợp pháp dành đầu tư không tự áp cho vốn NSNN của dự án này. Cơ quan thẩm định, người quyết định đầu tư và người duyệt quyết toán phải theo pháp luật cùng văn bản phân cấp hiện hành của tỉnh.',[('2158','Điều 1–2'),('2161','quyết định và phụ lục'),('ĐTC','Điều 38; Điều 43'),('217','Điều 31; Điều 39')])
text('Nghị định 387 có hiệu lực 12/10/2026, hợp nhất nội dung 04 CTMTQG. Khoản 1 Điều 53 cho tiếp tục cơ chế Nghị định 358 và hướng dẫn trước hợp nhất đối với kế hoạch, dự toán, nhiệm vụ, dự án, hợp đồng… đã được phê duyệt trong năm 2026 trước ngày có hiệu lực. Hồ sơ chuẩn bị của Trường có mốc 29/9 và 07/10; cần lập phiếu chuyển tiếp gắn từng quyết định và nguồn vốn. Không mặc định mọi dự án/phần việc mới được duyệt sau 12/10 đều chuyển tiếp chỉ vì có nhiệm vụ chuẩn bị trước đó. Kế hoạch trung ương bổ sung sau ngày này thuộc khoản 2 Điều 53 phải được cấp có thẩm quyền lựa chọn cơ chế thống nhất; không trộn hai cơ chế cho cùng nhiệm vụ và nguồn kinh phí.',[('387','Điều 52; khoản 1, 2 Điều 53'),('358','Điều 6–11')])
text('Tên dự án và nguồn vốn trong tài liệu này giữ đúng yêu cầu và hồ sơ đã có. Khi phê duyệt dự án hoặc điều chỉnh kế hoạch sau hợp nhất, cơ quan quản lý Chương trình xác nhận việc tiếp tục tên/mã nội dung cũ hay chuyển sang nội dung tương ứng. Chưa đủ căn cứ để tự đổi tên dự án hoặc tự gán mã hợp phần mới. Dự án của Trường không tự thuộc cơ chế dự án nhỏ, kỹ thuật đơn giản có sự tham gia cộng đồng tại Điều 16–22 Nghị định 358.',[('387','Điều 53'),('358','Điều 16–17')])
heading('3. Bốn con số và ba mốc thời gian cần quản lý riêng')
text('24.894.000.000 đồng là tổng mức sơ bộ dự kiến; 1.519.778.268 đồng là dự toán chuẩn bị đầu tư; 260.000.000 đồng là kế hoạch vốn năm 2026 đã nhận diện (NSTW 200.000.000, ngân sách tỉnh 60.000.000); số thực trả phải đối chiếu chứng từ và Kho bạc. Hai gói chuẩn bị: khảo sát + BCKTKT 852.345.246 đồng; QLDA 667.433.022 đồng, cộng đúng dự toán chuẩn bị. Chưa được lấy tỷ lệ 200/60 của kế hoạch 2026 làm tỷ lệ cố định của tổng dự án.',[('2158','Điều 1'),('2236','phụ lục'),('805','phụ lục kế hoạch'),('2161','phụ lục')])
text('Tên dự án ghi giai đoạn 2026–2030; phụ lục kế hoạch 2026 ghi thời gian 2026–2028; hợp đồng QLDA dự kiến không quá 3 năm. Phải làm rõ và thống nhất trong BCKTKT/quyết định đầu tư và kế hoạch, không tự sửa một mốc theo mốc còn lại. Theo Điều 57 Luật Đầu tư công, thời gian bố trí vốn thực hiện nhóm C không quá 3 năm, tính liên tục từ năm đầu được bố trí vốn thực hiện, không kể vốn chuẩn bị đầu tư và quyết toán. Không lấy riêng 260 triệu vốn chuẩn bị năm 2026 để tự ấn định năm cuối vốn thực hiện; kéo dài nếu cần phải đúng thẩm quyền, điều kiện và nguồn vốn.',[('ĐTC','khoản 1, 2, 3 Điều 57'),('2161','phụ lục'),('2236','thời gian hợp đồng')])
heading('4. Trạng thái chứng cứ và việc tiếp theo')
text('Đã nhận diện: QĐ 2158 ngày 29/9/2026 thay QĐ 1899; QĐ 2161 giao chi tiết vốn; QĐ 2236 ngày 07/10/2026 phê duyệt KHLCNT. Bản kết quả trên Hệ thống thể hiện QĐ 2374 và QĐ 2375 cùng ngày 27/10/2026: Trường Phát Land trúng gói khảo sát/BCKTKT 852.345.246 đồng, công bố 11:08:55; Thành Vinh trúng gói QLDA 667.433.022 đồng, công bố 14:27:48. Không ghi lại là đang chờ đăng tải.',[('2374','bản thông tin kết quả'),('2375','bản thông tin kết quả')])
text('Chưa thấy trong nhóm tài liệu đọc được: hợp đồng cuối cùng đã ký và ngày hiệu lực; chứng từ tạm ứng/thực trả sau 30/9; BCKTKT hoàn chỉnh và quyết định đầu tư cuối cùng; hồ sơ phân cấp đầy đủ, mã dự án NSNN. Bản hợp đồng hiện thấy là dự thảo. Báo cáo tháng 10 nêu thực hiện đến 30/9 bằng 0 và ước tháng 10 là 260 triệu; phần ước không phải bằng chứng đã giải ngân. Số 093 trong phụ lục vốn là mã ngành kinh tế, không thay mã dự án.',[('HĐ','nhãn dự thảo'),('BC','số thực hiện và ước thực hiện'),('2161','phụ lục')])
text('Ưu tiên ngay: đối chiếu bản ký và hiệu lực hai hợp đồng; xác nhận tư cách giao nhiệm vụ/CĐT và thẩm quyền duyệt BCKTKT; xác nhận cơ chế chuyển tiếp; kiểm tra mã dự án, tài khoản và vốn Kho bạc; duyệt nhiệm vụ/phương án khảo sát; chốt đề cương BCKTKT và danh mục thiết bị; lập tiến độ 120 ngày từ hiệu lực hợp đồng tư vấn, gắn điều kiện vốn và các mốc thẩm định. Các bước đã có vẫn được giữ trong bảng để truy vết, không yêu cầu làm lại nếu hồ sơ hợp lệ.')

R=[]
def row(ph,work,own,ct,con,other,ref,note):R.append([ph,work,own,ct,con,other,ref,note])
def add(ph,work,ref,note,own='C',ct='–',con='P',other='–'):
 items=[]
 for r in ref.split('|'):
  k,cl=r.split(':',1);items.append((k,cl))
 row(ph,work,own,ct,con,other,items,note)

add('A','Khóa danh mục, tên, mục tiêu và đối tượng thụ hưởng → phiếu nhận diện dự án','2158:Điều 1|805:phụ lục','Đã có hồ sơ chuẩn bị. Đối chiếu danh mục Chương trình và nhu cầu ký túc xá, thiết bị đào tạo; không dùng đề xuất quy mô cũ. Trường TH-HC&QT phối hợp TC-KT và đơn vị sử dụng.',other='P: cơ quan quản lý Chương trình')
add('A','Xác định nhóm C và hình thức hồ sơ → bản phân loại','ĐTC:khoản 4 Điều 11|217:khoản 2 Điều 27','Sơ bộ 24,894 tỷ: đối chiếu nhóm C và BCKTKT ≤40 tỷ theo khoản được viện dẫn. Rà lại nếu điều chỉnh quy mô; không chia dự án để giữ ngưỡng.')
add('A','Xác nhận thuộc CTMTQG → căn cứ không lập chủ trương riêng','ĐTC:điểm a, d khoản 6 Điều 19','Không đặt thêm quyết định chủ trương riêng cho dự án thuộc Chương trình. Lưu căn cứ danh mục, nguồn vốn và phạm vi; nếu tách ra ngoài Chương trình phải phân loại lại.',other='P: Sở Tài chính/cơ quan Chương trình')
add('A','Lập phiếu chuyển tiếp và mã nội dung Chương trình','387:Điều 52; khoản 1, 2 Điều 53','Mốc 12/10/2026; đối chiếu riêng nhiệm vụ, kế hoạch, dự án, hợp đồng. Xác nhận phần được tiếp tục theo NĐ 358 và phần phát sinh mới; không tự trộn cơ chế.',other='C/D: cấp có thẩm quyền; P: cơ quan Chương trình')
add('A','Xác lập chủ thể chuẩn bị, CĐT, người quyết định đầu tư → hồ sơ giao/phân cấp','2158:Điều 2|XD:Điều 9|ĐTC:Điều 38; Điều 43','Cần bổ sung trọn bộ căn cứ giao/phân cấp. Trước khi được giao CĐT, Trường thực hiện vai trò cơ quan chuẩn bị trong phạm vi được giao. Không suy thẩm quyền từ người ký QĐ 2158.',own='P sau khi giao',other='C/D: cấp giao nhiệm vụ/quyết định đầu tư')
add('A','Đối chiếu kế hoạch trung hạn và điều kiện bố trí vốn → bảng nguồn vốn','ĐTC:Điều 55–58|358:Điều 6; Điều 9','Phân biệt vốn chuẩn bị với vốn thực hiện. Xác nhận khả năng cân đối NSTW và ngân sách tỉnh theo kế hoạch được giao; không tự ấn định tỷ lệ toàn dự án.',other='C/D: cơ quan có thẩm quyền kế hoạch vốn')
add('A','Giao, phân bổ chi tiết vốn năm 2026 → quyết định/phụ lục','805:phụ lục|2161:phụ lục','Đã có mốc 260 triệu: trung ương 200, tỉnh 60. Kiểm tra tiếp nhận trên hệ thống Kho bạc và phần được chi; không coi đây là tổng vốn dự án.',own='C/P',other='D: cấp giao vốn; P: KBNN')
add('A','Thống nhất tiến độ và mốc bố trí vốn nhóm C → tiến độ cơ sở','ĐTC:Điều 57|2161:phụ lục|2236:thời gian hợp đồng','Làm rõ 2026–2030 trong tên với 2026–2028 ở phụ lục. Đồng hồ vốn thực hiện ≤3 năm không gồm vốn chuẩn bị; 120 ngày tư vấn tính từ hiệu lực hợp đồng.')
add('A','Xác nhận đất, hồ sơ công trình, tài sản và khu vực đang sử dụng','XD:Điều 19; Điều 25|2158:phạm vi nhiệm vụ','Thu bản vẽ cũ, pháp lý đất, hiện trạng kết cấu, điện nước, PCCC; khảo sát hoạt động ký túc xá để có phương án di chuyển, cách ly người học.',other='P: đơn vị sử dụng; cơ quan đất đai nếu cần')
add('A','Đăng ký mã dự án và tài khoản giao dịch → mã, hồ sơ giao dịch','254:Điều 8','Kiểm tra với TC-KT, Sở Tài chính và KBNN khu vực XV – Phòng giao dịch 23. Không dùng mã ngành 093 thay mã dự án; hồ sơ đăng ký cụ thể theo thủ tục Kho bạc hiện hành.',other='C/P: TC-KT; P: Sở Tài chính, KBNN')

add('B','Phê duyệt nhiệm vụ và dự toán chuẩn bị đầu tư → QĐ 2158','206:Điều 11|2158:Điều 1–3','Đã có 29/9/2026, thay QĐ 1899. Tổng 1.519.778.268 đồng; cập nhật vào TMĐT. Giữ căn cứ vốn, không dùng dự toán cũ 6,249 tỷ.',own='C/D theo tư cách chuẩn bị')
add('B','Lập, duyệt KHLCNT gói chuẩn bị → QĐ 2236','ĐT:khoản 5 Điều 37; khoản 2 Điều 40|2236:quyết định/phụ lục','Đã có 07/10: khảo sát+BCKTKT 852.345.246; QLDA 667.433.022; chỉ định rút gọn. Không thêm thẩm định KHLCNT theo khoản cũ đã bãi bỏ.',own='C/D theo tư cách chuẩn bị')
add('B','Lựa chọn và đăng kết quả hai gói tư vấn → hồ sơ kết quả','214:Điều 78–80|2374:thông tin công bố|2375:thông tin công bố','Đã nhận diện kết quả và đăng tải ngày 27/10/2026. Lưu bản ký, dấu thời gian, hồ sơ đánh giá/hoàn thiện; không làm lại bước công bố.',own='C/D',con='C/P: tư vấn dự kiến trúng')
add('B','Ký và xác lập hiệu lực hợp đồng chuẩn bị → hợp đồng cuối cùng','ĐT:Điều 65–68|210:Điều 4–7; Điều 13','Chưa thấy bản đã ký trong tài liệu đọc được. Đối chiếu quyết định, giá, nhân sự, phạm vi, tiến độ, điều kiện vốn; không tính 120 ngày từ ngày duyệt kết quả nếu hợp đồng quy định từ hiệu lực.',con='C: bên nhận thầu tư vấn')
add('B','Thiết lập quản lý dự án và cơ chế phối hợp → phân công, kế hoạch','XD:Điều 32|217:Điều 44|2375:phạm vi gói QLDA','Tư vấn QLDA hỗ trợ theo hợp đồng; CĐT giữ trách nhiệm pháp lý và thẩm quyền quyết định. Phân rõ TH-HC&QT, TC-KT, đơn vị sử dụng và tư vấn.',con='C: QLDA')
add('B','Phê duyệt nhiệm vụ khảo sát/đánh giá hiện trạng','XD:Điều 21–22|217:Điều 10–11','Công việc tiếp theo. Xác định nhu cầu khảo sát, đo vẽ, kiểm định chịu lực và điều kiện sử dụng dữ liệu cũ; chỉ thực hiện khối lượng có căn cứ.',own='C/D',con='C: lập nhiệm vụ')
add('B','Duyệt phương án kỹ thuật khảo sát → phương án và kế hoạch an toàn','217:Điều 12','Theo nhiệm vụ được duyệt; kiểm tra thiết bị, khối lượng, tiêu chuẩn, nhân sự và an toàn tại ký túc xá đang hoạt động.',own='D/P',con='C: khảo sát')
add('B','Khảo sát, giám sát và nghiệm thu kết quả → báo cáo, dữ liệu gốc','217:Điều 13–15','CĐT tổ chức kiểm soát; nghiệm thu và phê duyệt kết quả trước dùng thiết kế. Lưu ảnh, số đo, thí nghiệm và kết luận khả năng tận dụng công trình.',own='C/D',con='C: khảo sát; P: giám sát')
add('B','Chốt nhu cầu thiết bị → danh mục, cấu hình và căn cứ giá','2158:Điều 1|206:Điều 5–6|ĐT:Điều 39','02 mô hình xe số tự động phục vụ đào tạo. Phân biệt mô hình, phương tiện thực hành và tài sản khác theo cấu hình thật; xác minh tiêu chuẩn/định mức, báo giá, thuế, vận chuyển, lắp đặt và đào tạo.',con='C: tư vấn; P: đơn vị đào tạo')
add('B','Lập BCKTKT → thuyết minh, BVTC, dự toán, TMĐT','XD:Điều 19; Điều 25|217:Điều 30|206:khoản 6 Điều 5; Điều 12','Bao quát cả 03 ký túc xá và 02 mô hình, chi phí QLDA/tư vấn/dự phòng. Tách bảng thiết bị để tổ chức gói và nghiệm thu; không để dự toán chuẩn bị nằm ngoài TMĐT.',con='C: khảo sát/thiết kế; P: QLDA')
add('B','Hoàn thiện yêu cầu quy hoạch, PCCC, môi trường, giấy phép','XD:Điều 19; Điều 26; Điều 42–47','Có điều kiện theo công năng, cấp công trình và mức can thiệp. Tư vấn lập phiếu xác định thủ tục/miễn có căn cứ chuyên ngành; không miễn toàn bộ vì là cải tạo.',other='C/T: cơ quan chuyên ngành khi thuộc diện')
add('B','Thẩm tra thiết kế/dự toán nếu thuộc diện → báo cáo thẩm tra','XD:khoản 5 Điều 26|206:Điều 7','Xác định theo an toàn công trình và yêu cầu thẩm định. Tư vấn độc lập, đủ năng lực và bảo đảm cạnh tranh; chọn tư vấn qua vòng C khi cần, không giao đơn vị lập tự thẩm tra.',con='T: tư vấn thẩm tra độc lập')
add('B','Thẩm định BCKTKT và phần trách nhiệm CĐT → kết quả thẩm định','217:Điều 31|206:Điều 7','Cơ quan chủ trì theo phân công của người quyết định đầu tư; tổng hợp phần CĐT tại khoản 7 Điều 31. Không nhầm với thẩm định BCNCKT hoặc lấy báo cáo tư vấn thay kết quả thẩm định.',own='C/T phần trách nhiệm',con='P: giải trình',other='C/T: cơ quan chủ trì thẩm định')
add('B','Phê duyệt đầu tư/BCKTKT và đóng dấu hồ sơ thiết kế','XD:Điều 28|217:Điều 39','Chưa thấy quyết định đầu tư cuối trong tài liệu đọc được. Người có thẩm quyền quyết định; ghi đủ nguồn, tổng mức, tiến độ, CĐT, quản lý dự án. CĐT đóng dấu thiết kế theo khoản 5 Điều 39 sau duyệt.',own='C: trình, đóng dấu',other='D: người quyết định đầu tư')
add('B','Cập nhật danh mục, kế hoạch vốn thực hiện, chỉ tiêu Chương trình','ĐTC:Điều 55–58|358:Điều 9–10|387:Điều 53','Quyết định đầu tư không tự thay giao vốn. Xác nhận mã nội dung và chỉ tiêu đầu ra; thực hiện điều chỉnh kế hoạch đúng cơ chế chuyển tiếp, không tự nâng vốn từ dự toán chuẩn bị.',other='C/D: cấp kế hoạch vốn, cơ quan Chương trình')

add('C','Phân chia gói triển khai → danh mục, giá và tiến độ các gói','ĐT:Điều 16; Điều 37; Điều 39','Lặp cho xây lắp, thiết bị, giám sát, thẩm tra, bảo hiểm/kiểm toán nếu cần. Tách theo kỹ thuật và tiến độ hợp lý, không chia để chỉ định thầu. Giá thiết bị không mặc định gộp hết vào xây lắp.')
add('C','Phê duyệt KHLCNT triển khai → kế hoạch được duyệt','ĐT:Điều 40–41','Sau căn cứ dự án/nguồn vốn phù hợp. CĐT phê duyệt đúng quyền; không coi KHLCNT chuẩn bị tại QĐ 2236 đã bao phủ các gói xây lắp, thiết bị chưa có.',own='C/D')
add('C','Xác định hình thức, phương thức, loại hợp đồng và qua mạng','ĐT:Điều 21; Điều 23–24; Điều 43|214:Điều 78–81','Hạn mức hiện hành: tư vấn thuộc dự án ≤3 tỷ; hàng hóa/phi tư vấn/xây lắp/hỗn hợp thuộc dự án ≤5 tỷ (Điều 78.4 đã sửa). Vẫn kiểm tra điều kiện và hiệu quả; không mặc định mọi gói nhóm C đều chỉ định.')
add('C','Đăng tải KHLCNT và thông tin → dữ liệu Hệ thống','ĐT:Điều 7–8','Lưu thông tin đăng tải và bản kế hoạch. Dùng mẫu, quy trình điện tử hiện hành tại ngày triển khai, kiểm tra hướng dẫn TT 79/2025 và văn bản sửa đổi; không dùng mẫu cũ chỉ vì dự án nhỏ.')
add('C','Lập, duyệt HSMT/HSYC hoặc dự thảo hợp đồng rút gọn','ĐT:Điều 39; Điều 43; Điều 78|214:quy trình hình thức tương ứng; Điều 80','Theo hình thức đã duyệt. Chỉ định rút gọn không áp phương thức một giai đoạn một túi hồ sơ; kiểm tra cơ chế gửi dự thảo qua Hệ thống. Tiêu chí thiết bị theo chức năng, không cài nhãn hiệu hạn chế cạnh tranh.',own='C/D',con='C/P: lập hồ sơ')
add('C','Mời thầu, nhận/mở hồ sơ hoặc gửi dự thảo và kiểm tra năng lực','ĐT:Điều 43; Điều 78|214:Điều 79–80 hoặc quy trình cạnh tranh','Nhánh cạnh tranh có hạn nộp, mở thầu và bảo đảm theo diện áp dụng; nhánh rút gọn kiểm tra tư cách, năng lực và hoàn thiện dự thảo. Không dựng hồ sơ dự thầu giả cho nhánh rút gọn.',ct='C: dự thầu/giải trình',con='C/P: tổ chuyên gia')
add('C','Đánh giá, làm rõ, thương thảo/hoàn thiện → báo cáo và biên bản','ĐT:Điều 43; Điều 78|214:Điều 79–80','Kiểm tra năng lực, kinh nghiệm, kỹ thuật, giá và tiến độ. Đàm phán giá có căn cứ; không tự trừ 5% cho mọi tư vấn. Mức tối thiểu 5% cần đối chiếu đúng trường hợp xây lắp tại điểm e khoản 2 Điều 78.',ct='C/P',con='C: chuyên gia')
add('C','Thẩm định kết quả khi quy trình yêu cầu → báo cáo','ĐT:Điều 78|214:quy trình áp dụng; Điều 80','Có điều kiện. Không thêm thẩm định kết quả bắt buộc cho nhánh rút gọn khi quy định không yêu cầu; bảo đảm độc lập giữa đánh giá và thẩm định khi có.',con='T: bộ phận/tư vấn thẩm định')
add('C','Phê duyệt và công bố kết quả → quyết định, thông báo','ĐT:điểm d khoản 1 Điều 78; khoản 4 Điều 8','Kết quả thuộc khoản 4 Điều 8 công khai chậm nhất 05 ngày làm việc từ ngày ban hành. Lưu bản ký, thông báo nhà thầu, dữ liệu đăng; hai gói chuẩn bị đã có dấu thời gian 27/10.',own='C/D',ct='P: nhận thông báo')
add('C','Ký và quản lý hợp đồng → hợp đồng, phụ lục, bảo đảm','ĐT:Điều 65–68|210:Điều 4–13','Phân biệt hợp đồng tư vấn, xây lắp và cung cấp hàng hóa; NĐ 210 điều chỉnh hợp đồng xây dựng. Kiểm tra bảo đảm thực hiện theo đối tượng/ngoại lệ, thẩm quyền ký, điều kiện hiệu lực, thuế, tạm ứng và bảo hành.',ct='C: bên nhận thầu',con='P hoặc C: bên tư vấn ký')
add('C','Lập hồ sơ tạm ứng và lịch thu hồi → bảo lãnh, chứng từ','254:Điều 8–9|210:Điều 13','Trong kế hoạch vốn, hợp đồng và điều kiện hợp lệ; mức, bảo lãnh, ngoại lệ và thu hồi theo từng loại hợp đồng. Không coi kết quả trúng thầu hoặc số ước báo cáo là đã tạm ứng.',ct='C/P: đề nghị, bảo lãnh',other='C: TC-KT; T/xử lý: KBNN')

add('D','Bàn giao mặt bằng, hiện trạng và bố trí người học','XD:Điều 48–49|207:Điều 12','Lập biên bản tài sản, đường điện/nước, vùng thi công, lối thoát nạn và phương án chuyển chỗ ở. Chỉ phát sinh GPMB/thu hồi đất nếu thực tế yêu cầu.',ct='C/P: nhận',other='P: đơn vị ký túc xá')
add('D','Kiểm tra điều kiện khởi công và thủ tục chuyên ngành','XD:Điều 48|207:Điều 12','Có mặt bằng, thiết kế được duyệt, giấy phép nếu phải có, hợp đồng, biện pháp an toàn/môi trường. Hoàn thành PCCC/chuyên ngành đúng giai đoạn; không dùng miễn giấy phép thay miễn thiết kế.',ct='P',con='P: giám sát')
add('D','Thông báo khởi công và lập biển công trường','XD:Điều 48–49|207:Điều 12–13','Thông báo trước khởi công theo khoản 2 Điều 12 và mẫu áp dụng, không tự đặt mốc chung 03 ngày làm việc từ luật cũ. Gửi cơ quan quản lý trật tự xây dựng đúng địa bàn.',ct='C/P: biển công trình',other='P: cơ quan quản lý địa bàn')
add('D','Kiểm tra huy động, nhân sự và bảo hiểm theo diện áp dụng','XD:Điều 10; Điều 61; Điều 63|207:Điều 15–16','Kiểm tra năng lực, phân công, thiết bị và thay nhân sự theo hợp đồng. Lập phiếu xác định bảo hiểm công trình, người lao động, bên thứ ba và nghề nghiệp; đối chiếu quy định bảo hiểm chuyên ngành.',ct='C: huy động/bảo hiểm',con='C/P theo phạm vi')
add('D','Duyệt/kiểm soát biện pháp, tiến độ và an toàn','XD:Điều 50–52|207:Điều 15–19','Chú ý phá dỡ, làm việc trên cao, điện, bụi, tiếng ồn và an toàn người học. Nếu phá dỡ thuộc diện phải lập phương án, thực hiện thủ tục riêng; tổ chức lối đi, rào chắn và ứng cứu.',ct='C: lập, thực hiện',con='C/P: kiểm soát')
add('D','Thi công và ghi nhật ký → nhật ký, hồ sơ công việc','XD:Điều 50; Điều 61|207:Điều 15','Theo BVTC, chỉ dẫn và hợp đồng; cập nhật hằng ngày. Công việc chưa đủ điều kiện hoặc sai thiết kế phải xử lý, không hợp thức hóa bằng nhật ký lập sau.',ct='C',con='P: giám sát')
add('D','Giám sát thi công và giám sát tác giả → chỉ dẫn, báo cáo','XD:Điều 56; Điều 60; Điều 62–63|207:Điều 20–21','Tách giám sát thi công, thiết kế và QLDA. Chỉ dẫn tại hiện trường không thay phê duyệt điều chỉnh thiết kế thuộc diện bắt buộc.',ct='P',con='C: giám sát; C: thiết kế theo phần việc')
add('D','Kiểm tra vật liệu, cấu kiện và thiết bị lắp đặt → hồ sơ đầu vào','207:Điều 6; Điều 14–15','Kiểm tra đúng chủng loại, chất lượng, hợp quy/thí nghiệm khi phải có. CO/CQ theo loại hàng và hợp đồng; không dùng bộ giấy chung thay thí nghiệm bắt buộc.',ct='C: cung cấp, tự kiểm',con='C/P: giám sát')
add('D','Thí nghiệm, quan trắc, kiểm định theo yêu cầu','207:Điều 6–8','Theo thiết kế, kế hoạch thí nghiệm và dấu hiệu bất thường. Lưu kết quả gốc và đánh giá; chọn đơn vị đủ điều kiện khi phát sinh, không bỏ kiểm tra vì cải tạo hoặc gói nhỏ.',ct='C/P',con='C/P',other='C: đơn vị thí nghiệm đủ điều kiện')
add('D','Nghiệm thu công việc, bộ phận/giai đoạn → biên bản','207:Điều 22–23','Công việc nghiệm thu không quá 24 giờ từ đề nghị, từ chối nêu lý do bằng văn bản; đúng người ký. Nghiệm thu trước che khuất/chuyển bước; nghiệm thu giai đoạn theo nhu cầu, không lập trùng vô ích.',ct='C: phụ trách kỹ thuật',con='C: trực tiếp giám sát')
add('D','Kiểm soát khối lượng, dự toán và thay đổi thiết kế','XD:Điều 28; Điều 31|206:Điều 8; Điều 16–18','Lập hồ sơ phát sinh, kiểm tra căn cứ, nguồn và thẩm quyền trước thực hiện. Nếu vượt TMĐT, thay mục tiêu/phạm vi hoặc tiến độ phải xử lý đúng cấp; không lấy dự phòng làm quyền tự thay đổi dự án.',ct='P: đề xuất',con='C/P: thiết kế, QLDA',other='D: cấp có thẩm quyền khi vượt quyền')
add('D','Điều chỉnh hợp đồng hợp pháp → phụ lục, bảo đảm cập nhật','XD:Điều 84|210:Điều 21–28','Trong phạm vi và trường hợp cho phép; đối chiếu loại hợp đồng. Tách điều chỉnh dự án, vốn, thiết kế và hợp đồng; quyết định điều chỉnh dự án không tự thay phụ lục hợp đồng.',ct='C/P',con='P')
add('D','Chuẩn bị và xác nhận hồ sơ thanh toán khối lượng','254:Điều 8; Điều 10|210:Điều 29','Căn cứ hợp đồng, nghiệm thu, giá trị và thu hồi tạm ứng. Đơn vị lưu đủ hồ sơ chất lượng/chứng từ dù Kho bạc không yêu cầu nộp hết. Không thanh toán khối lượng chưa có thật.',ct='C: đề nghị',con='C/P: xác nhận phạm vi')
add('D','Gửi Kho bạc, kiểm soát và hạch toán theo từng nguồn','254:Điều 8–10|2161:phụ lục vốn','TC-KT đối chiếu mã dự án, mục lục NSNN, số được giao, số tạm ứng/thu hồi/thanh toán, NSTW và tỉnh. Không chuyển nguồn hoặc bù tỷ lệ bằng bảng nội bộ.',ct='P',other='C: TC-KT; T/xử lý: KBNN')
add('D','Theo dõi hạn giải ngân, điều chỉnh/kéo dài kế hoạch vốn','ĐTC:Điều 57; Điều 67–68|358:Điều 9–10','Đối chiếu thời hạn từng nguồn và văn bản giao; lập đề nghị đúng hạn, đúng điều kiện/thẩm quyền. Kéo dài giải ngân năm và kéo dài thời gian bố trí vốn nhóm C là hai việc khác nhau.',other='C/D: cấp kế hoạch vốn; P: KBNN')
add('D','Theo dõi đầu ra, giám sát đầu tư và báo cáo CTMTQG','ĐTC:Điều 75–80|358:Điều 45–50|64:Điều 4; khoản 2 Điều 6','Theo dõi tiến độ, vốn, chất lượng và thụ hưởng; báo cáo qua đầu mối tỉnh theo cơ chế được xác nhận. Vốn đầu tư dùng 04a/CTMTQG-ĐT khi áp QĐ 64; không dùng mẫu vốn thường xuyên.',other='P: Sở Tài chính/cơ quan Chương trình')
add('D','Công khai, kiểm tra, thanh tra và giám sát cộng đồng','358:Điều 45–50|ĐTC:Điều 78–80','Cung cấp hồ sơ hợp lệ, ghi kiến nghị và kết quả xử lý. Giám sát cộng đồng không thay tư vấn giám sát, nghiệm thu hoặc thẩm tra quyết toán; không tự áp cơ chế giao cộng đồng thi công cho Trường.',other='C/P: cơ quan kiểm tra, MTTQ và cộng đồng')

add('E','Nhận hàng thiết bị → biên bản giao nhận, danh mục serial','ĐT:Điều 65–67|2158:danh mục thiết bị','Tách thiết bị đào tạo khỏi vật liệu xây lắp. Kiểm tra cấu hình thực tế, số lượng, số máy/serial, xuất xứ, hồ sơ pháp lý theo loại hàng, vận chuyển và bảo quản.',ct='C: cung cấp',con='P: tư vấn kỹ thuật',other='P: đơn vị đào tạo, TC-KT')
add('E','Lắp đặt, chạy thử và nghiệm thu thiết bị → kết quả thử','207:Điều 14; Điều 24|ĐT:Điều 65–67','Theo loại hàng: mô hình độc lập nghiệm thu theo hợp đồng hàng hóa; thiết bị công trình phải kết hợp hồ sơ xây dựng. Đo tính năng, an toàn và tương thích, không chỉ đếm số lượng.',ct='C',con='C/P: kiểm tra',other='P: đơn vị sử dụng')
add('E','Đào tạo vận hành và chuyển giao → tài liệu, biên bản','ĐT:Điều 65–67|207:Điều 30','Thu hướng dẫn tiếng Việt, bảo hành, bảo trì, vật tư thay thế/phần mềm nếu có. Người nhận vận hành xác nhận khả năng dùng đúng mục tiêu đào tạo.',ct='C',other='C/P: đơn vị đào tạo nhận')
add('E','Rà hồ sơ hoàn thành và tồn tại → danh mục hoàn thành','207:Điều 24; Điều 28','Tập hợp BVTC/hoàn công, khảo sát, nghiệm thu, thí nghiệm, thay đổi được duyệt, chuyên ngành, quy trình vận hành/bảo trì. Lập danh sách tồn tại, người xử lý và hạn rõ ràng.',ct='C: hoàn công',con='C/P: giám sát/QLDA')
add('E','Xác định và thực hiện kiểm tra nghiệm thu nhà nước nếu thuộc diện','207:Điều 25–27','Xác định từ giai đoạn D theo loại/cấp/công năng, gửi hồ sơ đúng cơ quan và thời điểm. Không bắt mọi công trình vốn NSNN phải kiểm tra; không miễn chỉ vì là nhóm C.',con='P',other='C/T: cơ quan có thẩm quyền kiểm tra')
add('E','Nghiệm thu hoàn thành → biên bản đủ điều kiện sử dụng','207:Điều 24; Điều 29','Đúng thành phần ký, hồ sơ chất lượng và điều kiện an toàn/chuyên ngành. Không đưa ký túc xá vào ở khi chưa đủ điều kiện; nghiệm thu có điều kiện chỉ trong phạm vi pháp luật cho phép.',ct='C/P',con='C/P: giám sát, thiết kế')
add('E','Bàn giao công trình và tài sản → biên bản, hồ sơ vận hành','207:Điều 28–30','Tách từng ký túc xá, thiết bị, đơn vị nhận và chi phí tạm tính; chốt tài sản, chìa khóa, điện nước, điều kiện khai thác. Cập nhật theo giá trị quyết toán sau duyệt.',ct='C/P',con='P',other='C/P: đơn vị quản lý/sử dụng, TC-KT')
add('E','Đưa vào sử dụng, bảo trì và theo dõi mục tiêu thụ hưởng','207:Điều 29; Điều 34–39|358:Điều 46–49','Giao người quản lý, kế hoạch và kinh phí vận hành/bảo trì; theo dõi chỗ ở, mức sử dụng và thiết bị thực hành. Không coi biên bản bàn giao là kết thúc mọi trách nhiệm.',other='C: đơn vị vận hành')
add('E','Thiết lập bảo hành, bảo đảm và xử lý khiếm khuyết','207:Điều 32–33|210:Điều 12; Điều 31','Tách bảo hành công trình và hàng hóa. Công trình vốn đầu tư công: thời hạn/tỷ lệ theo cấp (thông thường ≥12 tháng, ≥5%; đặc biệt/I ≥24 tháng, ≥3%) theo Điều 32. Thiết bị theo hợp đồng và nhà sản xuất, không áp máy móc 12 tháng/5%.',ct='C: bảo hành',con='P')

add('F','Quyết toán từng hợp đồng → quyết toán A–B, công nợ','210:Điều 30|193:Điều 7','Đối chiếu phạm vi, giá, khối lượng, phát sinh hợp lệ, tạm ứng, phạt/bồi thường và bảo hành. Mẫu 01/QTDA của NĐ 193 là A–B, khác mẫu cùng số của TT 73.',ct='C: lập/đối chiếu',con='P theo hợp đồng')
add('F','Thanh toán cuối và thu hồi tạm ứng → đối chiếu Kho bạc','254:Điều 9–10|193:Điều 7','Đối chiếu số vốn từng nguồn, giá trị thanh toán và công nợ. Chưa thanh toán đủ không cản lập quyết toán theo chế độ; kê khai đúng nợ và nguồn, không gộp phần chưa trả thành đã giải ngân.',ct='C/P',other='C/P: TC-KT, KBNN')
add('F','Đối chiếu, quyết toán vốn đầu tư theo niên độ','254:phần quyết toán vốn theo năm|64:Điều 4; Điều 6','Theo mẫu và lịch niên độ còn hiệu lực, kiểm tra phần TT 91/2025 chưa bị bãi bỏ. Không dùng quyết toán dự án hoàn thành thay quyết toán năm và báo cáo Chương trình.',other='C/P: TC-KT, Sở Tài chính, KBNN')
add('F','Lập hồ sơ quyết toán dự án hoàn thành → báo cáo, tờ trình','193:Điều 6–8; Điều 21|73:Điều 3–4','Nhóm C: tối đa 04 tháng từ ngày hoàn thành được bàn giao đưa vào khai thác, sử dụng đến ngày nộp đủ hồ sơ (hoặc mốc dừng dự án theo Điều 21). Mẫu 01–07/QTDA TT 73, pháp lý/chi phí/công nợ/tài sản; không chờ hết bảo hành.',con='C/P: QLDA')
add('F','Kiểm toán độc lập nếu thuộc diện/quyết định hợp pháp','193:Điều 9','Không mặc định bắt buộc kiểm toán độc lập cho nhóm C. Kiểm tra yêu cầu của người có thẩm quyền, nguồn tài trợ hoặc hồ sơ cụ thể; nếu thuê phải có căn cứ, chi phí, lựa chọn và báo cáo, không thay thẩm tra.',con='C: kiểm toán nếu thuê',other='D: cấp có thẩm quyền khi cần')
add('F','Nộp, tiếp nhận và hoàn thiện hồ sơ → phiếu giao nhận','193:Điều 7–8|73:Mẫu 12/QTDA','Xác định đúng cơ quan chủ trì thẩm tra theo quyết định/phân cấp. Gửi đúng bộ hồ sơ; theo dõi yêu cầu bổ sung, thời điểm đủ hồ sơ và giải trình.',con='P',other='C/T: cơ quan thẩm tra')
add('F','Thẩm tra quyết toán → báo cáo kết quả, dự thảo quyết định','193:Điều 10–19; Điều 21','Nhóm C tối đa 02 tháng thẩm tra từ khi nhận đủ hồ sơ theo chế độ; kiểm tra pháp lý, vốn, chi phí, tài sản và nợ. Bám phạm vi riêng khi có báo cáo kiểm toán.',own='P: giải trình',con='P',other='C/T: cơ quan chủ trì thẩm tra')
add('F','Phê duyệt quyết toán → quyết định, phụ lục','193:Điều 8; Điều 19; Điều 21|73:Mẫu 10/QTDA','Nhóm C thời gian phê duyệt tối đa 07 ngày theo mốc Điều 21, không tự đổi thành ngày làm việc. Người có thẩm quyền theo phân cấp ký; Hiệu trưởng không mặc nhiên có quyền do là CĐT.',own='P',other='D: người có thẩm quyền')
add('F','Xử lý sau quyết toán → thu hồi, thanh toán, cập nhật tài sản','193:Điều 25–28','Thực hiện kiến nghị, khoản giảm trừ, nợ, vốn dư; cập nhật nguyên giá và bàn giao theo giá trị được duyệt. Phân biệt tài sản mới, nâng cấp, sửa chữa và tiêu chuẩn ghi nhận theo chế độ kế toán/tài sản công.',ct='C/P: nghĩa vụ liên quan',other='C: TC-KT; P: đơn vị tài sản, KBNN')
add('F','Báo cáo kết thúc dự án và đóng góp Chương trình','ĐTC:Điều 75–80|358:Điều 47–49|387:Điều 53','Tổng hợp sản phẩm thực tế, đối tượng hưởng lợi, vốn NSTW/tỉnh, tồn tại và vận hành. Báo cáo dự án thành phần không thay báo cáo đánh giá kết thúc toàn Chương trình của cấp chủ trì.',con='P',other='P: cơ quan Chương trình')
add('F','Thanh lý hợp đồng, đóng giao dịch khi đủ điều kiện','210:Điều 31|193:Điều 25–28','Theo hợp đồng và nghĩa vụ thực tế; giữ nghĩa vụ bảo hành/chưa hoàn thành khi thanh lý theo quy định. Chỉ tất toán tài khoản, dự án khi đủ căn cứ, không thực hiện tự động ngay khi bàn giao.',ct='C/P',other='C/P: TC-KT, KBNN')
add('F','Xác nhận hết bảo hành và giải tỏa bảo đảm','207:Điều 33','Kiểm tra khiếm khuyết, sửa chữa, xác nhận của bên giao thầu/đơn vị sử dụng theo chế độ. Theo dõi cả khi đã quyết toán và thanh lý các nghĩa vụ khác.',ct='C: hoàn thành bảo hành',other='P: đơn vị vận hành')
add('F','Lập mục lục, bàn giao và lưu trữ hồ sơ toàn vòng đời','207:Điều 28|ĐT:Điều 7–8|193:Điều 7','Gắn mã hồ sơ với bản ký, dữ liệu Hệ thống, nghiệm thu, thanh toán và quyết toán. Xác định bản gốc/điện tử, nơi lưu, người giữ và thời hạn từng nhóm theo quy định lưu trữ, kế toán, xây dựng; không đặt một hạn chung.')

heading('PHẦN 2. BẢNG QUY TRÌNH 8 CỘT')
text('Ký hiệu: C — chủ trì; P — phối hợp; T — thẩm tra/thẩm định; D — quyết định/phê duyệt; – — không trực tiếp tham gia. Cột Chủ đầu tư áp dụng khi có tư cách được giao; trước đó Trường thực hiện phần việc cơ quan chuẩn bị theo thẩm quyền, không tự nhận quyền CĐT. “Nhà thầu” chủ yếu chỉ bên xây lắp/cung cấp; tư vấn là bên nhận thầu đối với hợp đồng tư vấn. Các dòng ghi điều kiện chỉ thực hiện khi đủ điều kiện phát sinh. Mục “Căn cứ/nguồn” có liên kết; nguồn hồ sơ nội bộ được liệt kê lại tại Phần 5.')
text('Phân công nội bộ đề xuất theo QĐ 2158: TH-HC&QT đầu mối quản lý và hồ sơ; TC-KT đầu mối nguồn vốn, Kho bạc, thanh quyết toán; đơn vị sử dụng nhận bàn giao/vận hành; tư vấn thực hiện đúng hợp đồng. Vòng C lặp cho các gói cần thiết; gói tư vấn chuẩn bị được thực hiện sớm tại B, không chờ duyệt BCKTKT mới chọn đơn vị lập BCKTKT.')
widths=[1.2,4.0,1.35,1.35,1.55,2.7,5.0,7.55] # exactly 24.7cm
headers=['STT','Công việc/Sản phẩm','Chủ đầu tư','Nhà thầu','Tư vấn','Cơ quan khác','Căn cứ/nguồn','Ghi chú']
T=doc.add_table(rows=1,cols=8);T.autofit=False;T.alignment=WD_TABLE_ALIGNMENT.CENTER
for c,w,t in zip(T.rows[0].cells,widths,headers):c.width=Cm(w);c.text=t
T.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
phases={'A':'Nhận diện, nguồn vốn và tổ chức chuẩn bị','B':'Khảo sát, BCKTKT và quyết định đầu tư','C':'Lựa chọn nhà thầu và ký hợp đồng','D':'Thực hiện, kiểm soát chất lượng, vốn và báo cáo','E':'Nghiệm thu, thiết bị và bàn giao','F':'Quyết toán, tài sản, bảo hành và lưu trữ'}
def shade(c,color):
 e=OxmlElement('w:shd');e.set(qn('w:fill'),color);c._tc.get_or_add_tcPr().append(e)
last=None
for n,r in enumerate(R,1):
 ph,work,own,ct,con,other,items,note=r
 if ph!=last:
  cells=T.add_row().cells;cells[0].text=ph;cells[1].text=phases[ph]
  for c in cells:shade(c,'E7E6E6')
  for c in cells:
   for p in c.paragraphs:p.paragraph_format.keep_with_next=True
  last=ph
 cells=T.add_row().cells
 for c,t in zip(cells,[str(n),work,own,ct,con,other,'',note]):c.text=t
 refs(cells[6].paragraphs[0],items)
 if n%2==0:
  for c in cells:shade(c,'F5F5F5')
for i,r in enumerate(T.rows):
 r._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
 for j,c in enumerate(r.cells):
  c.width=Cm(widths[j]);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
  for p in c.paragraphs:
   p.alignment=WD_ALIGN_PARAGRAPH.LEFT;p.paragraph_format.first_line_indent=Cm(0)
   p.paragraph_format.space_after=Pt(2);p.paragraph_format.space_before=Pt(0);p.paragraph_format.line_spacing=1
   if i==0:
    for rr in p.runs:rr.bold=True
   for rr in p.runs:rr.font.name='Times New Roman';rr.font.size=Pt(14)
for c,w in zip(T.columns,widths):c.width=Cm(w)
for gc,w in zip(T._tbl.tblGrid.gridCol_lst,widths):gc.set(qn('w:w'),str(round(w/2.54*1440)))
tp=T._tbl.tblPr;tw=tp.find(qn('w:tblW'));tw.set(qn('w:type'),'dxa');tw.set(qn('w:w'),str(round(24.7/2.54*1440)))
borders=OxmlElement('w:tblBorders')
for edge in ['top','bottom','left','right','insideH','insideV']:
 e=OxmlElement('w:'+edge);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),'808080');borders.append(e)
tp.append(borders)

heading('PHẦN 3. CHECKLIST HỒ SƠ LƯU TRỮ')
groups=[
('01. Pháp lý và nguồn vốn','Danh mục dự án thuộc Chương trình; văn bản giao nhiệm vụ/CĐT, phân cấp; phiếu chuyển tiếp 12/10/2026; kế hoạch trung hạn/năm và điều chỉnh; NQ 56, QĐ 805, QĐ 2161 cùng phụ lục; mã dự án, tài khoản, dữ liệu vốn. Đối chiếu tên, nguồn NSTW/tỉnh và mốc bố trí vốn.'),
('02. Chuẩn bị đầu tư','QĐ 2158 và hồ sơ lập/thẩm định dự toán; ghi nhận thay QĐ 1899; QĐ 2236, tờ trình; kết quả 2374/2375 và bằng chứng đăng Hệ thống; hồ sơ năng lực, dự thảo/hoàn thiện, bản hợp đồng ký, phụ lục và hiệu lực. Dự thảo phải tách khỏi bản chính.'),
('03. Khảo sát và thiết kế','Nhiệm vụ, phương án kỹ thuật, số liệu/ảnh gốc, nhật ký, kết quả kiểm định/thí nghiệm nếu có, nghiệm thu/phê duyệt khảo sát; BCKTKT, BVTC và dự toán; danh mục cấu hình/giá thiết bị; thẩm tra, thẩm định, giải trình; quyết định đầu tư và hồ sơ được đóng dấu.'),
('04. Điều kiện chuyên ngành','Pháp lý đất, công trình hiện hữu; phiếu xác định thủ tục quy hoạch, giấy phép/miễn, PCCC, môi trường, bảo hiểm, cấp/loại công trình. Lưu kết quả thủ tục khi phát sinh; không chỉ lưu kết luận “không cần” thiếu căn cứ.'),
('05. Lựa chọn nhà thầu triển khai','KHLCNT/phê duyệt/đăng tải; căn cứ hình thức; HSMT/HSYC hoặc dự thảo rút gọn; hồ sơ dự thầu/đề xuất theo diện; mở thầu, đánh giá, làm rõ, thương thảo; thẩm định nếu phải có; kết quả/phê duyệt/đăng tải; hợp đồng, bảo đảm, thay đổi hợp pháp.'),
('06. Thi công và giám sát','Bàn giao mặt bằng; di chuyển người học; điều kiện/thông báo khởi công; nhân sự và năng lực; biện pháp, an toàn, bảo hiểm; nhật ký; giám sát/tác giả; hồ sơ đầu vào/thí nghiệm/kiểm định; nghiệm thu công việc/giai đoạn, hoàn công; hồ sơ phát sinh và điều chỉnh.'),
('07. Thiết bị đào tạo','Danh mục mã hàng/serial, cấu hình, giao nhận, kiểm tra chất lượng/xuất xứ theo diện, chạy thử và nghiệm thu; tài liệu hướng dẫn, chuyển giao/đào tạo, bảo hành/bảo trì; đơn vị nhận và hồ sơ ghi nhận tài sản. Không dùng riêng hóa đơn thay nghiệm thu tính năng.'),
('08. Vốn và báo cáo','Hồ sơ pháp lý gửi Kho bạc, đề nghị tạm ứng/bảo lãnh, nghiệm thu/giá trị thanh toán, thu hồi ứng, sao kê/đối chiếu từng nguồn; lịch giải ngân/kéo dài/điều chỉnh; báo cáo tháng, niên độ, giám sát đầu tư, CTMTQG và chứng cứ gửi/tiếp nhận; kiểm tra/kiến nghị/xử lý.'),
('09. Hoàn thành và quyết toán','Hồ sơ hoàn thành, kiểm tra nghiệm thu nhà nước nếu thuộc diện, chuyên ngành và nghiệm thu đưa vào dùng; bàn giao, vận hành/bảo trì; quyết toán A–B theo NĐ 193, báo cáo theo mẫu TT 73, kiểm toán nếu có, giao nhận/thẩm tra, giải trình, quyết định quyết toán; công nợ, nguồn vốn, tài sản và thu hồi sau duyệt.'),
('10. Sau bàn giao','Sổ bảo hành, thông báo khiếm khuyết và sửa chữa, xác nhận hết bảo hành/giải tỏa; thanh lý, tất toán đủ điều kiện; báo cáo hiệu quả và thụ hưởng; mục lục lưu, bản gốc/bản điện tử, nơi giữ, người nhận và thời hạn từng nhóm theo chế độ hiện hành.')]
for h,t in groups:heading(h);text('☐ '+t)
text('Checklist là công cụ quản lý nội bộ, không tự tạo thêm hồ sơ bắt buộc phải nộp Kho bạc hoặc thủ tục hành chính. Chọn bản gốc hoặc bản điện tử hợp lệ theo chế độ tương ứng; duy trì liên kết truy vết với hệ thống đấu thầu và hồ sơ lưu của Trường. Không áp một thời hạn bảo quản chung cho toàn bộ nhóm tài liệu.')

heading('PHẦN 4. RỦI RO VÀ ĐIỂM KIỂM SOÁT')
risks=[
('Sai cơ chế nguồn','Đây là vốn đầu tư công, không áp quy trình chi thường xuyên dưới 3 tỷ, TT 60 về kinh phí thường xuyên hoặc mẫu 04b/CTMTQG-TX cho dòng vốn đầu tư.'),
('Chủ trương và thẩm quyền','Không bổ sung chủ trương riêng khi thuộc Điều 19.6.d; cũng không từ đó bỏ quyết định đầu tư. Xác nhận căn cứ giao/phân cấp trước khi điền tên người ký BCKTKT và quyết toán.'),
('Chuyển tiếp 12/10 chưa đủ căn cứ','QĐ nhiệm vụ chuẩn bị trước ngày hiệu lực là một chứng cứ, chưa tự chứng minh mọi phần của dự án tương lai đều thuộc chuyển tiếp. Trình đầu mối tỉnh xác nhận phạm vi; áp thống nhất với nguồn bổ sung theo Điều 53.2.'),
('Số liệu cũ ghi đè số mới','QĐ 2158 thay 1899: không dùng dự toán chuẩn bị 6,249 tỷ hoặc quy mô đề xuất 238 tỷ. 24,894 tỷ vẫn là số sơ bộ, không trình bày như TMĐT cuối được duyệt.'),
('Nhầm giao vốn với giải ngân','260 triệu là vốn 2026; báo cáo tháng 10 có số ước, không phải thực trả. Đối chiếu chứng từ và KBNN trước kết luận; cơ cấu 200/60 chỉ phản ánh vốn đã nhận diện của năm này.'),
('Lệch thời gian nhóm C','Tên 2026–2030, phụ lục 2026–2028 và hợp đồng QLDA ≤3 năm cần giải trình thống nhất. Không tự tính thời gian vốn thực hiện từ năm có vốn chuẩn bị; không hiểu CTMTQG 10 năm cho phép mọi nhóm C kéo dài 10 năm.'),
('Nhầm trạng thái đấu thầu','Hai kết quả đã đăng 27/10. Tập hợp bản ký và hợp đồng cuối, không yêu cầu đăng lại hoặc coi bản dự thảo là hợp đồng hiệu lực. Thời gian tư vấn 120 ngày chỉ bắt đầu theo điều kiện hiệu lực hợp đồng.'),
('Chỉ định mặc định/ép tiết kiệm 5%','Kiểm tra điều kiện và hình thức mỗi gói; không chia nhỏ. Hai gói tư vấn trúng theo thông tin hiện có không bị tự động giảm 5%; nghĩa vụ tối thiểu cần đúng trường hợp xây lắp tại Điều 78.2.e, không suy rộng từ văn bản khuyến khích.'),
('Bỏ dự toán hoặc gộp sai thiết bị','BCKTKT thiết kế một bước vẫn có dự toán. Kiểm tra mô hình đào tạo, cấu hình và tài sản; không áp tiêu chuẩn xe công vụ cho mọi mô hình hoặc chỉ nhận đủ số lượng mà bỏ thử tính năng.'),
('Thi công khi người học còn ở thiếu cách ly','Bàn giao theo khu vực, phương án di chuyển, lối thoát và kiểm soát điện/bụi/tiếng ồn. Dừng phần việc khi thiếu điều kiện an toàn; nghiệm thu chất lượng không thay điều kiện đưa vào sử dụng.'),
('Bỏ quyết toán, dùng chế độ cũ','Từ 01/7/2026 quyết toán hoàn thành dùng NĐ 193/TT 73, không dùng Điều 30–47 NĐ 254 hoặc Điều 58 NĐ 358 đã bị bãi bỏ. Lịch nhóm C 4 tháng lập, 2 tháng thẩm tra, 7 ngày phê duyệt theo đúng mốc Điều 21.'),
('Báo cáo sai kỳ/sai thực hiện','Theo QĐ 64, báo cáo tháng gửi trước ngày 02 của tháng báo cáo, gồm thực hiện kỳ trước và ước tháng báo cáo theo cấu trúc quy định; không tự diễn giải thành ngày 02 tháng sau. Theo dõi lịch yêu cầu bổ sung của đầu mối Chương trình.'),
('Bỏ phần việc sau quyết toán','Theo dõi công nợ, thu hồi, cập nhật nguyên giá, khai thác, bảo trì và hết bảo hành; quyết toán phê duyệt không xóa nghĩa vụ sửa chữa của nhà thầu.')]
for i,(h,t) in enumerate(risks,1):text(f'{i}. {h}: {t}')

heading('PHẦN 5. SỔ NGUỒN, HIỆU LỰC VÀ NỘI DUNG CẦN XÁC NHẬN')
text('Chốt nghiên cứu ngày 28/10/2026. Đã bổ sung tìm kiếm Exa; kết quả tìm chỉ dùng phát hiện nguồn, căn cứ nội dung là toàn văn chính thức và hồ sơ cụ thể. Văn bản hợp nhất phục vụ đọc, không có hiệu lực độc lập. Với thủ tục phát sinh sau ngày chốt phải kiểm tra lại hiệu lực, mẫu, phân cấp và chuyển tiếp tại thời điểm làm.')
laws=[
('ĐTC','VBHN 03 ngày 05/02/2026; dùng Điều 11, 19, 38–43, 55–58, 67–68, 75–80. Dự án CTMTQG miễn chủ trương riêng nhưng phải quyết định đầu tư và quản lý vốn đúng chế độ.'),
('387','Ban hành và hiệu lực 12/10/2026. Điều 52 hợp nhất/bãi bỏ theo danh mục; Điều 53 chuyển tiếp. Không bỏ qua văn bản này khi lập quy trình sau 12/10; phải xác nhận cơ chế dự án/phần việc mới.'),
('358','Ban hành 31/12/2025. Sử dụng với nhiệm vụ, kế hoạch, hồ sơ đủ điều kiện chuyển tiếp tại Điều 53 NĐ 387; Điều 6–11, 45–50 cho kế hoạch, vốn, giám sát/báo cáo. Không dùng Điều 58 về quyết toán đã bị NĐ 193 bãi bỏ; không tự áp Điều 16–22 cho dự án của Trường.'),
('XD','Ban hành 10/12/2025, hiệu lực chung 01/7/2026. Điều 9, 19–28, 32, 42–65, 81–90; chuyển tiếp Điều 95. Hồ sơ mới không mặc định áp Luật Xây dựng cũ.'),
('217','Ban hành 19/6/2026, hiệu lực 01/7/2026, đọc cùng sửa đổi tại bản hợp nhất tháng 9/2026. Điều 10–15 khảo sát; 27, 30–31 BCKTKT; 39 duyệt; 44 quản lý dự án; thủ tục giấy phép khi thuộc diện.'),
('206','Ban hành 15/6/2026, hiệu lực 01/7/2026. Điều 5–8 TMĐT, 11 chuẩn bị, 12 và 16–18 dự toán/điều chỉnh; Điều 36 chuyển tiếp. Không dùng như chế độ thanh toán vốn Kho bạc.'),
('207','Ban hành 15/6/2026, hiệu lực 01/7/2026. Điều 6–8, 12–30 quản lý thi công/chất lượng/nghiệm thu; 32–39 bảo hành/bảo trì; Điều 53 chuyển tiếp. Kiểm tra nghiệm thu nhà nước theo đúng đối tượng Điều 25.'),
('210','Ban hành 15/6/2026, hiệu lực 01/7/2026. Điều 4–13 hợp đồng/tạm ứng/bảo đảm, 21–31 điều chỉnh/thanh quyết toán/thanh lý; Điều 33 chuyển tiếp. Hợp đồng cung cấp hàng hóa độc lập theo Luật Đấu thầu và chế độ hợp đồng tương ứng.'),
('ĐT','Đọc VBHN 74/VBHN-VPQH ngày 25/3/2026. Điều 7–8 thông tin, 16 cấm chia nhỏ/vi phạm, 37–43 kế hoạch/quy trình, 65–68 hợp đồng, 78 trách nhiệm CĐT. Không đặt thêm thẩm định KHLCNT theo khoản đã bãi bỏ.'),
('214','NĐ 214 hiệu lực 04/8/2025, dùng nội dung đã sửa, đọc VBHN 36/2026/VBHN-NĐ-BTC ngày 23/9/2026. Hạn mức Điều 78.4 được sửa bởi NĐ 349 ngày 09/9/2026: gói dự án tư vấn 3 tỷ, hàng hóa/phi tư vấn/xây lắp/hỗn hợp 5 tỷ; Điều 79–80 điều kiện/quy trình.'),
('254','Hiệu lực 26/9/2025. Điều 8–10 cho hồ sơ/tạm ứng/thanh toán; phần quyết toán vốn theo niên độ còn hiệu lực. Điều 30–47 và nội dung quyết toán hoàn thành liên quan đã bị NĐ 193 bãi bỏ từ 01/7/2026.'),
('193','Ban hành 01/6/2026, hiệu lực 01/7/2026. Điều 6–9 hồ sơ/chủ thể/kiểm toán; 10–21 thẩm tra, phê duyệt và thời hạn; 25–28 trách nhiệm/xử lý; 29 chuyển tiếp; 31 bãi bỏ. Dùng trực tiếp cho vốn đầu tư công.'),
('73','Ban hành 25/6/2026, hiệu lực 01/7/2026. Điều 3–4 và phụ lục mẫu quyết toán hoàn thành; Điều 5 thay TT 27/2025 và phần mẫu liên quan của TT 91/2025; hồ sơ nộp trước hiệu lực đối chiếu khoản chuyển tiếp.')]
for i,(k,t) in enumerate(laws,1):
 p=para();p.add_run(str(i)+'. ').bold=True;link(p,S[k][0],S[k][1]);p.add_run('. '+t)
heading('Hồ sơ địa phương và hồ sơ dự án đã đối chiếu')
for k in ['56','805','2158','2161','2236','2374','2375','64','BC','HĐ']:
 p=para();link(p,S[k][0],S[k][1])
 p.add_run(' — bản trong hồ sơ đầu vào; liên kết đến tệp gốc, không chỉnh sửa. Với dự thảo chỉ dùng xác định trạng thái và phần cần bổ sung.')
text('Dấu vết trích đọc: bộ inventory.json và các bản trích S001–S072 trong thư mục nghiên cứu của lần lập; dùng S011 cho QĐ 2158, S019 cho KHLCNT, S022 cho phụ lục 260 triệu, S033/S027 cho kết quả đã đăng; S061 đối chiếu phân bổ 200/60. Căn cứ toàn văn NĐ 387 tải từ Công báo được lưu riêng. Hồ sơ đã đọc không đồng nghĩa đã kiểm chứng chữ ký số trực tuyến hoặc xác nhận hiệu lực mọi bản ký.')
heading('Những việc cần xác nhận để áp dụng vào quyết định cụ thể')
text('CAN_XAC_MINH / THIEU_DU_LIEU: (1) căn cứ giao CĐT, phân cấp người duyệt BCKTKT/quyết toán và cơ quan thẩm định; (2) phạm vi chuyển tiếp Điều 53 và mã nội dung Chương trình; (3) hợp đồng đã ký/hiệu lực và số thực giải ngân; (4) nguồn trung hạn, vốn thực hiện, mã dự án và mốc tiến độ thống nhất; (5) cấp/loại công trình, thủ tục chuyên ngành, định mức tài sản thiết bị và chế độ kế toán/lưu trữ cụ thể. Người/cơ quan có thẩm quyền xác nhận theo từng phần, tư vấn không tự quyết thay.')
text('Tự kiểm: bảng giữ đúng 8 cột, 6 giai đoạn, số liên tục; số liệu hai gói bằng dự toán chuẩn bị và cơ cấu vốn năm 2026 cộng đúng tổng. Tài liệu chưa thực hiện rà soát theo KTC-Ra-Soat-897; chưa xác thực chữ ký số trực tuyến, chưa có kiểm tra hiện trường hoặc xác nhận Kho bạc. Kết quả đo thể thức và xem trang được lập thành phiếu riêng kèm bản giao.')

# Remove hidden theme font overrides and normalize Unicode throughout.
for el in list(doc._element.iter())+list(doc.styles.element.iter()):
 if el.tag==qn('w:t') and el.text:el.text=unicodedata.normalize('NFC',el.text)
 if el.tag==qn('w:rFonts'):
  for a in list(el.attrib):
   if 'Theme' in a:del el.attrib[a]
  for a in ['ascii','hAnsi','eastAsia','cs']:el.set(qn('w:'+a),'Times New Roman')
 if el.tag==qn('w:color'):
  for a in list(el.attrib):
   if 'theme' in a.lower():del el.attrib[a]
  el.set(qn('w:val'),'000000')
 if el.tag.endswith('}srgbClr'):el.set('val','000000')
 if el.tag.endswith('}schemeClr'):
  el.tag=el.tag.replace('schemeClr','srgbClr');el.set('val','000000')
  for child in list(el):el.remove(child)
 if el.tag.endswith('}stroke'):
  el.set('color','black')
 if el.tag.endswith('}line') and 'strokecolor' in el.attrib:el.set('strokecolor','black')
for p in doc.paragraphs:
 for r in p.runs:r.font.name='Times New Roman';r.font.size=Pt(14)
doc.core_properties.title='Quy trình dự án nhóm C — Trường cao đẳng chất lượng cao — CTMTQG'
doc.core_properties.author='Trường Cao đẳng Kon Tum — dự thảo tư vấn'
doc.save(OUT)
(ROOT/'_research/rows.json').write_text(json.dumps(R,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'file':str(OUT),'steps':len(R),'columns':len(T.columns)},ensure_ascii=False))
