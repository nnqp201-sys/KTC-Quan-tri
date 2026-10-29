"""accept_all(src, dst): chấp nhận mọi Track Changes, xuất bản sạch (gửi thẩm định AI phải dùng bản sạch — rule 24)."""
import docx
from docx.oxml.ns import qn

def accept_all(src, dst):
    d = docx.Document(src); b = d.element
    for tag in ("w:del", "w:moveFrom"):
        for el in list(b.iter(qn(tag))):
            par = el.getparent()
            if par is not None and par.tag in (qn("w:rPr"), qn("w:trPr")):
                continue
            par.remove(el)
    for tag in ("w:ins", "w:moveTo"):
        for el in list(b.iter(qn(tag))):
            par = el.getparent()
            if par is None or par.tag in (qn("w:rPr"), qn("w:trPr")):
                continue
            for ch in list(el):
                el.addprevious(ch)
            par.remove(el)
    # hàng bảng bị xóa
    for tr in list(b.iter(qn("w:tr"))):
        trPr = tr.find(qn("w:trPr"))
        if trPr is not None and trPr.find(qn("w:del")) is not None:
            tr.getparent().remove(tr)
        elif trPr is not None:
            for x in trPr.findall(qn("w:ins")): trPr.remove(x)
    # đoạn có dấu đoạn bị xóa: gộp vào đoạn sau (đơn giản: nếu rỗng thì xóa)
    for p in list(b.iter(qn("w:p"))):
        pPr = p.find(qn("w:pPr"))
        if pPr is None: continue
        rPr = pPr.find(qn("w:rPr"))
        if rPr is not None:
            for x in rPr.findall(qn("w:del")):
                rPr.remove(x)
                if not "".join(t.text or "" for t in p.iter(qn("w:t"))).strip():
                    p.getparent().remove(p); break
            for x in rPr.findall(qn("w:ins")): rPr.remove(x)
    for tag in ("w:rPrChange", "w:pPrChange", "w:tblPrChange", "w:trPrChange", "w:tcPrChange", "w:sectPrChange"):
        for el in list(b.iter(qn(tag))):
            el.getparent().remove(el)
    d.save(dst)
    s = open(dst, "rb").read()
    return dst


if __name__ == "__main__":
    import sys
    accept_all(sys.argv[1], sys.argv[2]); print("ban sach:", sys.argv[2])
