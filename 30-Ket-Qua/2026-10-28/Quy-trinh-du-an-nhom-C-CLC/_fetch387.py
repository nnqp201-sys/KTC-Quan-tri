from pathlib import Path
import urllib.request,ssl,re,html
from docx import Document
ssl._create_default_https_context=ssl._create_unverified_context
root=Path(__file__).resolve().parent/'_research'
url='https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-387-2026-nd-cp-470814.htm'
s=urllib.request.urlopen(url,timeout=40).read().decode()
links=[html.unescape(x) for x in re.findall(r'href=[\"\x27]([^\"\x27]+)',s) if 'file_name=' in x and '.docx' in x]
b=urllib.request.urlopen(links[0],timeout=40).read()
p=root/'387.docx';p.write_bytes(b)
d=Document(p)
t='\n'.join(p.text for p in d.paragraphs)+'\n'+'\n'.join(' | '.join(c.text for c in r.cells) for tb in d.tables for r in tb.rows)
(root/'387.txt').write_text(t,encoding='utf-8')
print(len(t),links[0])
