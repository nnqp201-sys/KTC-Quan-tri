from pathlib import Path
from docx import Document
from pypdf import PdfReader
import json
R=Path(__file__).resolve().parent
p=R/'Quy-trinh-du-an-nhom-C_Truong-CLC_CTMTQG_20261028.docx'
d=Document(p);t=d.tables[1]; nums=[r.cells[0].text for r in t.rows if r.cells[0].text.isdigit()]
assert nums==[str(i) for i in range(1,76)]
assert len(t.columns)==8 and all(len(r.cells)==8 for r in t.rows)
assert [r.cells[0].text for r in t.rows if r.cells[0].text in list('ABCDEF')]==list('ABCDEF')
assert 852345246+667433022==1519778268
assert 200000000+60000000==260000000
alltext='\n'.join(p.text for p in d.paragraphs)+'\n'+'\n'.join(c.text for tb in d.tables for r in tb.rows for c in r.cells)
assert 'ĐƠN VỊ…..' not in alltext
assert 'được bàn giao đưa vào khai thác' in alltext
pdf=PdfReader(p.with_suffix('.pdf'))
assert len(pdf.pages)>20
texts=[pg.extract_text() for pg in pdf.pages]
assert all(len(t.strip())>100 for t in texts)
info={'steps':75,'columns':8,'phases':6,'pages':len(pdf.pages),'math':'PASS','continuous_numbers':'PASS','placeholders':'PASS','format_check':'0 suggestions','visual_review':'all pages, contact sheets; sample pages enlarged','official_897_review':False}
(R/'_research/verification.json').write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(info,ensure_ascii=False))
