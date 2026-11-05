from pathlib import Path
from copy import deepcopy
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

OUT=Path(__file__).parent
TEMPLATE=Path(r'D:\OneDrive - Trường Cao Đẳng Kon Tum\1. Tong hop - Hanh chinh\15. Đi công tác\2026\Di Hue\BC Ket qua du Hoi nghi tai Hue.docx')

reports=[('2312841','BC_Ket-qua_Hoi-nghi-hop-tac-giao-duc_Ha-Noi.docx',
'kết quả tham dự Hội nghị quốc tế về hợp tác giáo dục trong kỷ nguyên số và Triển lãm Giáo dục và Công nghệ giáo dục tại Hà Nội',[
('body','Căn cứ Công văn số 843/HTQT-QHQT ngày 01/6/2026 của Cục Hợp tác quốc tế về việc mời tham gia Hội nghị quốc tế về Hợp tác giáo dục và Triển lãm Giáo dục và Công nghệ giáo dục;'),
('body','Thực hiện Kế hoạch số 1001/KH-CĐKT ngày 06/10/2026 của Trường Cao đẳng Kon Tum tham dự Hội nghị quốc tế về Hợp tác giáo dục và Triển lãm Giáo dục và Công nghệ giáo dục, Đoàn công tác báo cáo kết quả chuyến công tác từ ngày 07/10/2026 đến ngày 10/10/2026 như sau:'),
('head','I. THÀNH PHẦN THAM DỰ'),
('body','1. Ông Nguyễn Ngọc Quang Phục, Phó Trưởng phòng Tổng hợp - Hành chính và Quản trị.'),
('body','2. Ông Nguyễn Thành Hiền, Phó Trưởng phòng Quản lý khoa học công nghệ và Hợp tác phát triển.'),
('body','3. Bà Bùi Như Quỳnh, viên chức phòng Tổng hợp - Hành chính và Quản trị.'),
('head','II. MỤC ĐÍCH HỘI NGHỊ'),
('body','Cập nhật chính sách, mô hình hợp tác quốc tế và giải pháp công nghệ phục vụ chuyển đổi số, đổi mới sáng tạo trong giáo dục; tìm hiểu ứng dụng trí tuệ nhân tạo (AI) trong dạy học, đánh giá và quản trị; tiếp cận các định hướng phát triển giáo dục nghề nghiệp trong hệ sinh thái nhân lực số, phục vụ tham mưu triển khai tại Trường.'),
('head','III. KẾT QUẢ THAM DỰ HỘI NGHỊ'),
('sub','1. Thời gian, địa điểm'),
('body','- Thời gian hội nghị và triển lãm: Ngày 08 và 09/10/2026. Thời gian chuyến công tác: Từ ngày 07/10/2026 đến ngày 10/10/2026, tính cả ngày đi và về.'),
('body','- Địa điểm: Khách sạn Grand Plaza Hà Nội, số 117 Trần Duy Hưng, phường Yên Hòa, thành phố Hà Nội.'),
('sub','2. Đơn vị tổ chức và thành phần hội nghị'),
('body','Hội nghị do Bộ Giáo dục và Đào tạo tổ chức, với sự tham gia của đại diện cơ quan quản lý, cơ sở giáo dục, tổ chức quốc tế, chuyên gia và doanh nghiệp công nghệ trong và ngoài nước. Hoạt động hội nghị, triển lãm và kết nối đối tác được tổ chức gắn với yêu cầu đổi mới giáo dục trong kỷ nguyên số.'),
('sub','3. Nội dung trọng tâm'),
('body','a) Chính sách, mô hình và công nghệ: Chương trình tập trung vào hệ sinh thái đổi mới sáng tạo trong giáo dục; ứng dụng AI trong đánh giá, phát triển nguồn nhân lực và đổi mới tổ chức hoạt động của cơ sở giáo dục; nâng cao năng lực ngoại ngữ và năng lực cạnh tranh trong môi trường quốc tế.'),
('body','b) Chuyển đổi số và hợp tác quốc tế: Các chuyên đề đề cập chuyển đổi số trong giáo dục phổ thông, giáo dục đại học số và quốc tế hóa; hợp tác giữa cơ sở giáo dục với doanh nghiệp, tổ chức quốc tế; quản trị thông minh, dữ liệu và học liệu số. Chương trình có phiên kết nối B2B, tạo cơ hội trao đổi nhu cầu đào tạo, nghiên cứu và giải pháp công nghệ.'),
('body','c) Giáo dục nghề nghiệp trong hệ sinh thái nhân lực số: Chuyên đề được bố trí sáng 09/10/2026, tập trung vào yêu cầu phát triển kỹ năng và nguồn nhân lực trước tác động của công nghệ số; tăng cường liên kết đào tạo với nhu cầu sử dụng lao động. Đây là nhóm nội dung có liên quan trực tiếp đến định hướng đào tạo của Trường.'),
('body','d) Triển lãm và giới thiệu giải pháp: Các hoạt động giới thiệu công nghệ bao quát AI, dữ liệu lớn, cá nhân hóa học tập, số hóa quản lý học đường, lớp học tương lai, khảo thí số và chứng chỉ nghề nghiệp quốc tế; đồng thời đề cập kết nối đào tạo với việc làm, kỹ năng số và học tập suốt đời.'),
('sub','4. Nội dung tiếp thu và khả năng vận dụng tại Trường'),
('body','Qua nội dung hội nghị và tài liệu chương trình, Đoàn công tác nhận thấy chuyển đổi số cần xuất phát từ yêu cầu thực tế của người học, nhà giáo và đơn vị quản lý; lựa chọn công nghệ gắn với chuẩn hóa quy trình, dữ liệu và khả năng sử dụng của đội ngũ. Việc ứng dụng AI cần có người kiểm tra, chịu trách nhiệm về kết quả, bảo đảm an toàn dữ liệu và chất lượng chuyên môn.'),
('body','Các hướng có thể nghiên cứu vận dụng gồm: hỗ trợ tổng hợp báo cáo, kế hoạch và xử lý công việc hành chính; phát triển học liệu số, hỗ trợ thiết kế bài giảng; phân tích thông tin phục vụ quản trị, bảo đảm chất lượng; kết nối doanh nghiệp để cập nhật kỹ năng nghề và tìm hiểu giải pháp đào tạo phù hợp điều kiện của Trường.'),
('head','IV. KIẾN NGHỊ, ĐỀ XUẤT'),
('body','Đoàn công tác đề xuất Lãnh đạo Trường xem xét, chỉ đạo:'),
('body','1. Giao phòng Quản lý khoa học công nghệ và Hợp tác phát triển chủ trì, phối hợp các đơn vị tổng hợp nhu cầu hợp tác, chuyển đổi số; lựa chọn nội dung, đối tác phù hợp để tham mưu phương án làm việc cụ thể, xác định rõ mục tiêu, sản phẩm, nguồn lực và trách nhiệm thực hiện.'),
('body','2. Giao phòng Tổng hợp - Hành chính và Quản trị phối hợp các đơn vị rà soát quy trình tổng hợp báo cáo, kế hoạch và quản lý công việc; đề xuất thí điểm ứng dụng AI đối với công việc phù hợp, có bước kiểm tra của viên chức phụ trách và theo dõi hiệu quả thực hiện.'),
('body','3. Giao phòng Quản lý Đào tạo và Bảo đảm chất lượng phối hợp các khoa nghiên cứu phát triển học liệu số, đổi mới phương pháp dạy học và đánh giá năng lực; chú trọng năng lực số, kỹ năng nghề và yêu cầu của doanh nghiệp, bảo đảm phù hợp từng ngành, nghề đào tạo.'),
('body','4. Tổ chức chia sẻ nội dung hội nghị cho đội ngũ có liên quan; bồi dưỡng kỹ năng sử dụng AI có trách nhiệm, kiểm chứng thông tin, bảo vệ dữ liệu và bản quyền. Việc lựa chọn nền tảng, phần mềm cần đánh giá nhu cầu, tính tương thích, chi phí và hiệu quả trước khi đề xuất đầu tư.'),
('body','Trên đây là Báo cáo kết quả tham dự Hội nghị quốc tế về hợp tác giáo dục trong kỷ nguyên số và Triển lãm Giáo dục và Công nghệ giáo dục tại Hà Nội. Đoàn công tác kính báo Lãnh đạo Trường xem xét, chỉ đạo./.')]),
('2312880','BC_Ket-qua_Hoi-thao-SEAMEO-RETRAC_TP-HCM.docx',
'kết quả tham dự Hội thảo quốc tế về Lãnh đạo và Quản lý giáo dục tại Thành phố Hồ Chí Minh',[
('body','Căn cứ Công văn số 226/SEA-BGD ngày 30/7/2026 của Trung tâm Đào tạo khu vực của SEAMEO tại Việt Nam về việc Hội thảo Quốc tế về Lãnh đạo và Quản lý giáo dục;'),
('body','Thực hiện Kế hoạch số 1000/KH-CĐKT ngày 02/10/2026 của Trường Cao đẳng Kon Tum tham dự Hội thảo Quốc tế về Lãnh đạo và Quản lý giáo dục, Đoàn công tác báo cáo kết quả chuyến công tác từ ngày 13/10/2026 đến ngày 16/10/2026 như sau:'),
('head','I. THÀNH PHẦN THAM DỰ'),
('body','1. Ông Nguyễn Ngọc Quang Phục, Phó Trưởng phòng Tổng hợp - Hành chính và Quản trị.'),
('body','2. Ông Đỗ Thành Công, chuyên viên phòng Tổng hợp - Hành chính và Quản trị.'),
('head','II. MỤC ĐÍCH HỘI THẢO'),
('body','Cập nhật kiến thức, kinh nghiệm về lãnh đạo, quản lý và đổi mới sáng tạo trong bối cảnh phát triển AI; tìm hiểu phương pháp ra quyết định dựa trên dữ liệu, bảo đảm chất lượng và phát triển năng lực đội ngũ. Tiếp cận kinh nghiệm quốc tế để nghiên cứu vận dụng phù hợp trong quản trị, công tác hành chính và hỗ trợ hoạt động đào tạo tại Trường.'),
('head','III. KẾT QUẢ THAM DỰ HỘI THẢO'),
('sub','1. Thời gian, địa điểm'),
('body','- Thời gian hội thảo: Ngày 14 và 15/10/2026. Thời gian chuyến công tác: Từ ngày 13/10/2026 đến ngày 16/10/2026, tính cả ngày đi và về.'),
('body','- Địa điểm: Trung tâm SEAMEO RETRAC, số 35 Lê Thánh Tôn, phường Sài Gòn, Thành phố Hồ Chí Minh.'),
('sub','2. Chủ đề, đơn vị tổ chức và thành phần'),
('body','Hội thảo có chủ đề “Nâng cao năng lực lãnh đạo và quản lý trong giáo dục đại học: Hướng tới đổi mới sáng tạo trong kỷ nguyên AI” (Advancing Excellence in Higher Education Leadership and Management: Toward AI-Driven Practice and Innovation).'),
('body','Theo Công văn số 226/SEA-BGD, Trung tâm SEAMEO RETRAC phối hợp với các tổ chức giáo dục quốc tế của Canada gồm ABIE, BCCIE, CBIE và Trung tâm SEAMEO RIHED tại Thái Lan tổ chức. Thành phần gồm cán bộ lãnh đạo, quản lý giáo dục, nhà nghiên cứu, giảng viên và chuyên gia trong nước, quốc tế. Ngôn ngữ hội thảo là tiếng Anh.'),
('sub','3. Nội dung trọng tâm'),
('body','a) Lãnh đạo, quản trị và ứng dụng AI: Chương trình có các báo cáo chính về tiếp nhận AI trong giáo dục đại học của TS. Justin Williams và lãnh đạo, quản lý với AI có trách nhiệm của TS. Airini. Các phiên chuyên đề đề cập lựa chọn của người lãnh đạo trước thay đổi công nghệ, duy trì sứ mệnh giáo dục và vai trò quyết định của con người.'),
('body','b) Quản trị dựa trên dữ liệu và bảo đảm chất lượng: Các tham luận giới thiệu khung bảo đảm chất lượng nội bộ có ứng dụng AI, sử dụng dữ liệu phục vụ lãnh đạo dựa trên minh chứng, kinh nghiệm quản lý chất lượng và đổi mới nghiên cứu. Nội dung gợi mở việc liên kết mục tiêu, dữ liệu, kết quả thực hiện và hoạt động cải tiến trong cơ sở giáo dục.'),
('body','c) Đổi mới dạy học và đánh giá: Chương trình đề cập học tập trải nghiệm có hỗ trợ AI, cá nhân hóa học tập, tư duy phản biện, giáo dục hòa nhập và đánh giá thực chất trong kỷ nguyên AI. Các vấn đề được đặt ra gồm sự phụ thuộc vào AI, thiên lệch của công nghệ, liêm chính học thuật và trách nhiệm của nhà giáo trong thiết kế, hướng dẫn, đánh giá hoạt động học tập.'),
('body','d) Phát triển năng lực đội ngũ: Các phiên chuyên đề tập trung vào mức độ sẵn sàng của giảng viên, phát triển năng lực số, phương pháp sử dụng AI tạo sinh trong dạy học và ứng xử với việc người học sử dụng AI. Việc triển khai công nghệ cần đi cùng bồi dưỡng chuyên môn, hướng dẫn sử dụng và cơ chế giám sát, điều chỉnh.'),
('sub','4. Nội dung tiếp thu và khả năng vận dụng tại Trường'),
('body','Các nội dung hội thảo cho thấy ứng dụng AI cần gắn với đổi mới phương thức quản trị, chất lượng dữ liệu và năng lực của đội ngũ. Đối với Trường Cao đẳng Kon Tum, có thể nghiên cứu vận dụng vào chuẩn hóa quy trình xử lý công việc; tổng hợp báo cáo, kế hoạch; quản lý hồ sơ, minh chứng; theo dõi tiến độ và hỗ trợ cung cấp thông tin phục vụ lãnh đạo.'),
('body','Kinh nghiệm của các cơ sở giáo dục đại học cần được lựa chọn, điều chỉnh theo chức năng, quy mô và điều kiện của Trường. Công nghệ hỗ trợ xử lý thông tin, còn viên chức phụ trách phải kiểm tra nguồn, tính chính xác, thẩm quyền và chịu trách nhiệm trước khi sử dụng kết quả trong công việc.'),
('head','IV. KIẾN NGHỊ, ĐỀ XUẤT'),
('body','Đoàn công tác đề xuất Lãnh đạo Trường xem xét, chỉ đạo:'),
('body','1. Giao phòng Tổng hợp - Hành chính và Quản trị phối hợp các đơn vị rà soát quy trình tiếp nhận, xử lý, tổng hợp và báo cáo công việc; đề xuất thí điểm AI đối với các khâu phù hợp. Xác định rõ đầu vào, đầu ra, người kiểm tra, quyền truy cập và cách lưu hồ sơ, minh chứng.'),
('body','2. Giao phòng Quản lý khoa học công nghệ và Hợp tác phát triển phối hợp các đơn vị tham mưu hướng dẫn sử dụng AI có trách nhiệm; chú trọng bảo mật thông tin, bảo vệ dữ liệu cá nhân, bản quyền, kiểm chứng nguồn và nhận diện sai lệch trong kết quả do AI tạo ra.'),
('body','3. Tổ chức chia sẻ, bồi dưỡng theo nhóm vị trí công việc; ưu tiên kỹ năng khai thác tài liệu, tổng hợp thông tin, soạn thảo và kiểm tra kết quả AI. Đánh giá hiệu quả bằng chất lượng sản phẩm, thời gian xử lý và mức độ đáp ứng yêu cầu công việc.'),
('body','4. Giao phòng Quản lý Đào tạo và Bảo đảm chất lượng phối hợp các khoa nghiên cứu kinh nghiệm về học tập trải nghiệm, đánh giá năng lực và liêm chính học thuật khi sử dụng AI; lựa chọn nội dung phù hợp với đào tạo nghề, triển khai có kiểm tra và rút kinh nghiệm trước khi mở rộng.'),
('body','Trên đây là Báo cáo kết quả tham dự Hội thảo quốc tế về Lãnh đạo và Quản lý giáo dục tại Thành phố Hồ Chí Minh. Đoàn công tác kính báo Lãnh đạo Trường xem xét, chỉ đạo./.')])]

def settext(p,text):
    runs=p.runs
    if runs:
        runs[0].text=text
        for r in runs[1:]:
            if r._r.xpath('.//w:drawing | .//w:pict'): continue
            r.text=''
    else:p.add_run(text)

def fmt(p,bold=False,size=14,align=WD_ALIGN_PARAGRAPH.JUSTIFY,indent=True):
    p.alignment=align
    f=p.paragraph_format
    f.first_line_indent=Cm(1) if indent else Cm(0)
    f.left_indent=Cm(0);f.right_indent=Cm(0)
    f.space_before=Pt(6);f.space_after=Pt(6);f.line_spacing=1
    f.keep_with_next=bold
    f.keep_together=True
    f.widow_control=True
    for r in p.runs:
        r.font.name='Times New Roman';r.font.size=Pt(size);r.bold=bold;r.italic=False
        r.font.color.rgb=None
        r._r.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'),'Times New Roman')

for folder,name,title,items in reports:
    d=Document(TEMPLATE)
    bodyproto=deepcopy(d.paragraphs[8]._p)
    headproto=deepcopy(d.paragraphs[9]._p)
    subproto=deepcopy(d.paragraphs[15]._p)
    titleproto=deepcopy(d.paragraphs[1]._p)
    subtitleproto=deepcopy(d.paragraphs[2]._p)
    lineproto=deepcopy(d.paragraphs[3]._p)
    for p in list(d.paragraphs): p._p.getparent().remove(p._p)
    endtable=d.tables[-1]._tbl
    def add(text,kind):
        el=deepcopy({'title':titleproto,'subtitle':subtitleproto,'head':headproto,'sub':subproto}.get(kind,bodyproto))
        endtable.addprevious(el);p=Paragraph(el,d._body);settext(p,text)
        fmt(p,bold=kind in ['title','subtitle','head','sub'],align=WD_ALIGN_PARAGRAPH.CENTER if kind in ['title','subtitle','greet'] else WD_ALIGN_PARAGRAPH.JUSTIFY,indent=kind not in ['title','subtitle','greet'])
        if kind=='subtitle':p.paragraph_format.keep_with_next=True
        return p
    add('BÁO CÁO','title');add(title,'subtitle')
    endtable.addprevious(deepcopy(lineproto))
    add('Kính gửi: Lãnh đạo Trường.','greet')
    for kind,t in items:
        p=add(t.replace('vận dụng gồm: hỗ trợ','vận dụng gồm hỗ trợ'),kind)
        if t.startswith('Căn cứ '):
            for r in p.runs:r.italic=True
    top=d.tables[0]
    settext(top.cell(2,1).paragraphs[0],'Quảng Ngãi, ngày      tháng 11 năm 2026')
    # Preserve template drawings and table widths while normalizing textual roles.
    for row in top.rows:
        for c in row.cells:
            for p in c.paragraphs:
                text=p.text.strip()
                if not text:continue
                size=14 if ('Độc lập' in text or 'Quảng Ngãi,' in text) else 13
                fmt(p,bold=('TRƯỜNG CAO' in text or 'CỘNG H' in text or 'Độc lập' in text),size=size,align=WD_ALIGN_PARAGRAPH.CENTER,indent=False)
                p.paragraph_format.space_before=Pt(0);p.paragraph_format.space_after=Pt(0)
                if 'Quảng Ngãi,' in text:
                    for r in p.runs:r.italic=True
    left=d.tables[-1].cell(0,0);right=d.tables[-1].cell(0,1)
    # Reuse original cell paragraphs, with explicit size for each recipient line.
    left.text=''
    p=left.paragraphs[0]
    for r in list(p.runs):r._r.getparent().remove(r._r)
    for i,t in enumerate(['Nơi nhận:','- Như trên;','- Các đơn vị thuộc Trường;','- Lưu: VT, THHCQT.']):
        if i:p=left.add_paragraph()
        r=p.add_run(t);r.font.name='Times New Roman';r.font.size=Pt(12 if i==0 else 11);r.bold=i==0;r.italic=i==0
        p.paragraph_format.space_before=Pt(0);p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1
    p.paragraph_format.line_spacing=1;p.paragraph_format.space_after=Pt(0)
    right.text='ĐẠI DIỆN ĐOÀN CÔNG TÁC\n\n\n\n\n'
    for p in right.paragraphs:fmt(p,True,align=WD_ALIGN_PARAGRAPH.CENTER,indent=False)
    for row in d.tables[-1].rows:
        pr=row._tr.get_or_add_trPr();pr.append(OxmlElement('w:cantSplit'))
    for s in d.sections:
        s.page_width=Cm(21);s.page_height=Cm(29.7)
        s.top_margin=Cm(2);s.bottom_margin=Cm(2);s.left_margin=Cm(3);s.right_margin=Cm(2)
        s.header_distance=Cm(1.27);s.footer_distance=Cm(1.27);s.different_first_page_header_footer=True
    d.core_properties.title=title
    d.core_properties.subject='Báo cáo kết quả chuyến công tác theo hồ sơ và nguồn hội nghị'
    d.core_properties.author=''
    d.core_properties.last_modified_by=''
    d.save(OUT/name)
    print(OUT/name)
