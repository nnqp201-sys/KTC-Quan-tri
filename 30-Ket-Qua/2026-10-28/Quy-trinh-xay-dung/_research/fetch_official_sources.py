from pathlib import Path
import urllib.request,re,html,concurrent.futures,ssl
ssl._create_default_https_context=ssl._create_unverified_context
from docx import Document
from pypdf import PdfReader
ROOT=Path('30-Ket-Qua/2026-10-28/Quy-trinh-xay-dung/_research'); ROOT.mkdir(parents=True,exist_ok=True)
sources={
'206':'https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-206-2026-nd-cp-469768.htm',
'135':'https://congbao.chinhphu.vn/van-ban/luat-so-135-2025-qh15-468695.htm',
'347':'https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-347-2025-nd-cp-468311.htm',
'89':'https://congbao.chinhphu.vn/van-ban/luat-so-89-2025-qh15-45572.htm',
'210':'https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-210-2026-nd-cp-469772.htm',
'104':'https://congbao.cdnchinhphu.vn/180507251028987904/2026/4/20/cong-bao-so-236-639123026208222311-ngay-20-04-47154_1776681061_signed.pdf',
'207':'https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-207-2026-nd-cp-469769.htm',
'217':'https://xdcs.cdnchinhphu.vn/446259493575335936/2026/9/29/91-vbhn-bxd-signed-1790654585945447247778.pdf',
'214':'https://congbao.chinhphu.vn/tai-ve-van-ban-so-214-2025-nd-cp-45774-58104',
'193':'https://congbao.chinhphu.vn/van-ban-dang-cong-bao/nghi-dinh-l1/trang-20.htm',
'349':'https://congbao.chinhphu.vn/van-ban-dang-cong-bao/chinh-phu-c1/trang-5.htm',
'73':'https://congbao.chinhphu.vn/van-ban/thong-tu-so-73-2026-tt-btc-469924.htm',
'74':'https://congbao.chinhphu.vn/van-ban/van-ban-hop-nhat-so-74-vbhn-vpqh-469204.htm',
'254':'https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-254-2025-nd-cp-46303.htm'}
def fetch(k,u):
 try:
  b=urllib.request.urlopen(u,timeout=35).read()
  if b[:4]==b'%PDF': ext='pdf'
  elif '.pdf' not in u:
   s=b.decode(); links=re.findall(r'href=[\"\x27]([^\"\x27]+)',s)
   links=[html.unescape(x) for x in links if 'file_name=' in x and '.docx' in x]
   if k in ['207','193','349']: links=[x for x in links if k in x.split('file_name=')[-1]]
   if not links: links=[html.unescape(x) for x in re.findall(r'href=[\"\x27]([^\"\x27]+)',s) if '.pdf' in x or ('file_name=' in x and '.pdf' in x)]
   u=links[0]; b=urllib.request.urlopen(u,timeout=35).read(); ext='pdf' if b[:4]==b'%PDF' else 'docx'
  else: ext='pdf'
  p=ROOT/(k+'.'+ext);p.write_bytes(b)
  if ext=='docx':
   d=Document(p); text='\n'.join(x.text for x in d.paragraphs)+'\n'+'\n'.join(' | '.join(c.text for c in r.cells) for t in d.tables for r in t.rows)
  else: text='\n'.join(p.extract_text() or '' for p in PdfReader(p).pages)
  (ROOT/(k+'.txt')).write_text(text,encoding='utf-8');return k,len(text),u
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for r in ex.map(lambda kv:fetch(*kv),[(k,u) for k,u in sources.items() if k in ['73','74','254']]):print(r)
