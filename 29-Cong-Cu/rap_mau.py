# -*- coding: utf-8 -*-
"""Thu vien rap noi dung vao mau / van ban tuong tu (28/10/2026).

Gom cac thao tac lap lai khi dung van ban tu 03-Templates(1) hoac van ban da ban hanh (Nguyen tac 7):
  dat(p, [...])                  thay chu trong cac run co san (giu dinh dang), run thua -> rong
  xoa(p)                         xoa doan / phan tu
  nhan_ban(mau, sau, [...])      nhan ban doan mau, chen sau doan `sau`, dat chu
  nhan_ban_dong(bang, dong_mau)  nhan ban mot dong bang (tr), noi vao cuoi bang, tra ve list _Cell
  ke_duoi_doan(p, dai_cm)        duong ke la HINH duong thang (sua duoc trong Word) — khong dung vien doan
  bo_trang_trang_cuoi(d)         xoa doan rong cuoi, thu nho doan cuoi bat buoc de khong sinh trang trang
  xuat_pdf(docx) -> (pdf, so_trang)   Word COM qua PowerShell
  chup_trang(pdf, [0, -1], thu_muc)   PNG de xem trang truoc khi giao

Bai hoc goc: phien De an Hang A 26/10/2026 — viet 4 script dung rieng, duong ke vien doan nguoi dung khong sua duoc,
trang trang cuoi bien ban.
"""
import copy
import os
import subprocess
import sys

import docx
import docx.table
import docx.text.paragraph
from docx.oxml import parse_xml
from docx.oxml.ns import qn
from docx.shared import Pt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from chuan_vb import chuan
except ImportError:  # pragma: no cover
    def chuan(s):
        return s

EMU_CM = 360000


def dat(p, texts, chuan_hoa=True):
    """Gan lan luot texts vao cac run cua p; run thua de rong. Thieu run thi don phan con lai vao run cuoi."""
    rs = p.runs
    if not rs:
        p.add_run("")
        rs = p.runs
    texts = [chuan(t) if chuan_hoa else t for t in texts]
    if len(texts) > len(rs):
        texts = texts[:len(rs) - 1] + ["".join(texts[len(rs) - 1:])]
    for i, r in enumerate(rs):
        r.text = texts[i] if i < len(texts) else ""


def xoa(p):
    e = p._element if hasattr(p, "_element") else p
    e.getparent().remove(e)


def nhan_ban(mau, sau, texts, chuan_hoa=True):
    e = copy.deepcopy(mau._element)
    sau._element.addnext(e)
    p = docx.text.paragraph.Paragraph(e, mau._parent)
    dat(p, texts, chuan_hoa)
    return p


def nhan_ban_dong(bang, dong_mau_tr):
    tr = copy.deepcopy(dong_mau_tr)
    bang._tbl.append(tr)
    return [docx.table._Cell(tc, bang) for tc in tr.findall(qn("w:tc"))]


_HINH = (
    '<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
    'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">'
    '<w:drawing><wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0" relativeHeight="251659264" '
    'behindDoc="0" locked="0" layoutInCell="1" allowOverlap="1"><wp:simplePos x="0" y="0"/>'
    '<wp:positionH relativeFrom="column"><wp:posOffset>{x}</wp:posOffset></wp:positionH>'
    '<wp:positionV relativeFrom="paragraph"><wp:posOffset>{y}</wp:posOffset></wp:positionV>'
    '<wp:extent cx="{cx}" cy="0"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/>'
    '<wp:docPr id="{id}" name="Duong ke {id}"/><wp:cNvGraphicFramePr/>'
    '<a:graphic><a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">'
    '<wps:wsp><wps:cNvCnPr/><wps:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="0"/></a:xfrm>'
    '<a:prstGeom prst="line"><a:avLst/></a:prstGeom><a:ln w="9525"><a:solidFill><a:srgbClr val="000000"/></a:solidFill>'
    '</a:ln></wps:spPr><wps:bodyPr/></wps:wsp></a:graphicData></a:graphic></wp:anchor></w:drawing></w:r>')


def ke_duoi_doan(p, dai_cm=2.5, rong_o_cm=None, cach_duoi_cm=0.74, id_hinh=901):
    """Ke duong thang (hinh ve, sua duoc) duoi doan p, can giua trong o/cot rong `rong_o_cm`.
    Bo vien duoi doan va thut le cu (neu co). Do 26/10: dai 2,5 cm, cach 0,74 cm dep voi chu dam co 13."""
    pPr = p._p.get_or_add_pPr()
    for t in ("w:pBdr", "w:ind"):
        e = pPr.find(qn(t))
        if e is not None:
            pPr.remove(e)
    if rong_o_cm is None:
        tc = p._p.getparent()
        w = tc.find(qn("w:tcPr")).find(qn("w:tcW")) if tc.tag == qn("w:tc") and tc.find(qn("w:tcPr")) is not None else None
        rong_o_cm = int(w.get(qn("w:w"))) / 567 if w is not None and w.get(qn("w:type")) == "dxa" else 8.5
    x = int(((rong_o_cm - dai_cm) / 2 - 0.19) * EMU_CM)
    p._p.append(parse_xml(_HINH.format(x=x, y=int(cach_duoi_cm * EMU_CM), cx=int(dai_cm * EMU_CM), id=id_hinh)))


def bo_trang_trang_cuoi(d):
    body = d.element.body
    cuoi = body[-2] if body[-1].tag == qn("w:sectPr") else body[-1]
    while (cuoi.tag == qn("w:p") and cuoi.getprevious() is not None and cuoi.getprevious().tag == qn("w:p")
           and not "".join(cuoi.itertext()).strip() and cuoi.find(".//" + qn("w:sectPr")) is None):
        truoc = cuoi.getprevious()
        body.remove(cuoi)
        cuoi = truoc
    if cuoi.tag == qn("w:p") and not "".join(cuoi.itertext()).strip():
        p = docx.text.paragraph.Paragraph(cuoi, d._body)
        pf = p.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing = Pt(1)
        for r in p.runs:
            r.font.size = Pt(1)


def xuat_pdf(duong_docx):
    """Xuat PDF bang Word (COM, qua PowerShell). Tra ve (duong_pdf, so_trang)."""
    f = os.path.abspath(duong_docx)
    pdf = os.path.splitext(f)[0] + ".pdf"
    ps = ("$w=New-Object -ComObject Word.Application;"
          f"$d=$w.Documents.Open('{f}',$false,$true);$d.ExportAsFixedFormat('{pdf}',17);"
          "$n=$d.ComputeStatistics(2);$d.Close(0);$w.Quit();Write-Output $n")
    kq = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True)
    so = int(kq.stdout.strip().splitlines()[-1]) if kq.stdout.strip() else None
    return pdf, so


def chup_trang(pdf, trang=(0, -1), thu_muc=None, dpi=70):
    import pymupdf
    d = pymupdf.open(pdf)
    thu_muc = thu_muc or os.path.dirname(pdf)
    out = []
    for i in trang:
        i = i % len(d)
        f = os.path.join(thu_muc, f"_xem_{os.path.splitext(os.path.basename(pdf))[0][:40]}_{i + 1}.png")
        d[i].get_pixmap(dpi=dpi).save(f)
        out.append(f)
    return out
