from pathlib import Path
from docx import Document
from pypdf import PdfReader
from openpyxl import load_workbook
import re,json,unicodedata,hashlib
ROOT=Path(__file__).resolve().parent; DEST=ROOT/'_research';DEST.mkdir(exist_ok=True)
EXT=Path(r'D:\OneDrive - Trường Cao Đẳng Kon Tum\1. Tong hop - Hanh chinh\2. Bao cao chuyen de\2026\De xuat CTMTQG tich hop')
DB=Path(r'H:\My Drive\KTC-Database')
targets=[]
for p in EXT.rglob('*'):
 if not p.is_file():continue
 if any(v in str(p) for v in ['NĂNG LỰC','Nang-luc','NL Cty']):continue
 if p.suffix.lower() not in ['.docx','.pdf','.xlsx']:continue
 if '2257980' in str(p):continue
 if any(v in str(p) for v in ['Chuan-bi-dau-tu','Báo cáo','1160','358']):targets.append(p)
for p in DB.rglob('*'):
 if not p.is_file() or p.suffix.lower() not in ['.docx','.pdf','.xlsx','.dotx']:continue
 if any(v in p.name.lower() for v in ['dau tu cong','đầu tư công','358-2025','275-2025','85-2025','805-qd','5387','2845','64-2026-qd','257-2025','56-nq-hdnd','55-nq-hdnd','46-nq-hdnd','155-2025','1976','597','06d-huong']):targets.append(p)
def extract(p):
 if p.suffix.lower()=='.docx':
  d=Document(p);return '\n'.join(x.text for x in d.paragraphs)+'\n'+'\n'.join(' | '.join(c.text for c in r.cells) for t in d.tables for r in t.rows)
 if p.suffix.lower()=='.pdf':return '\n'.join(f'\n[Trang {i+1}]\n'+(pg.extract_text() or '') for i,pg in enumerate(PdfReader(p).pages))
 if p.suffix.lower()=='.xlsx':
  wb=load_workbook(p,data_only=True);return '\n'.join('\n[Sheet '+sh.title+']\n'+'\n'.join(' | '.join(str(v) if v is not None else '' for v in row) for row in sh.values) for sh in wb)
 return ''
inventory=[]
for i,p in enumerate(targets,1):
 try:
  tx=unicodedata.normalize('NFC',extract(p)); key=f'S{i:03d}';(DEST/(key+'.txt')).write_text(tx,encoding='utf-8')
  inventory.append({'id':key,'path':str(p),'chars':len(tx),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 except Exception as e:inventory.append({'path':str(p),'error':str(e)})
(DEST/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
for item in inventory:print(item.get('id','ERR'),item.get('chars',''),item['path'])
