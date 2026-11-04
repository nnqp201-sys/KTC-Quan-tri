# -*- coding: utf-8 -*-
"""Thư viện dựng văn bản A4 dọc theo thể thức Trường (NĐ 30): lề 2-2-3-2, Times New Roman 14.

Dùng cho hợp đồng, biên bản của hồ sơ đầu tư công (không có khối cơ quan ban hành).
"""
import re
import unicodedata

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

_ONES = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]


def _doc3(n, day_du):
    tram, chuc, dv = n // 100, (n // 10) % 10, n % 10
    p = []
    if tram > 0 or day_du:
        p.append(_ONES[tram] + " trăm")
    if chuc > 1:
        p.append(_ONES[chuc] + " mươi")
        if dv == 1:
            p.append("mốt")
        elif dv == 5:
            p.append("lăm")
        elif dv > 0:
            p.append(_ONES[dv])
    elif chuc == 1:
        p.append("mười")
        if dv == 5:
            p.append("lăm")
        elif dv > 0:
            p.append(_ONES[dv])
    elif dv > 0:
        if tram > 0 or day_du:
            p.append("lẻ")
        p.append(_ONES[dv])
    return " ".join(p)


def bang_chu(n):
    """Số tiền (đồng) → chữ, kiểu 'tám trăm năm mươi hai triệu, ba trăm bốn mươi lăm nghìn, hai trăm bốn mươi sáu đồng'."""
    n = int(n)
    nhom = []
    for ten, giatri in (("tỷ", 10**9), ("triệu", 10**6), ("nghìn", 10**3), ("", 1)):
        nhom.append((ten, n // giatri))
        n %= giatri
    out, dau = [], True
    for ten, v in nhom:
        if v == 0:
            continue
        s = _doc3(v, day_du=not dau)
        out.append((s + " " + ten).strip())
        dau = False
    return ", ".join(out) + " đồng"


def vnd(n):
    return f"{int(n):,}".replace(",", ".")


_RE_HOA = re.compile(r"(:\s+)([^\W\d_])")


def cap(t):
    """Viết hoa chữ đầu sau dấu hai chấm (quy ước của Trường)."""
    t = unicodedata.normalize("NFC", t)
    return _RE_HOA.sub(lambda m: m.group(1) + (m.group(2).upper() if m.group(2).islower() else m.group(2)), t)


class VanBan:
    def __init__(self):
        self.ls = 1.15
        self.doc = Document()
        s = self.doc.sections[0]
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.top_margin, s.bottom_margin = Cm(2), Cm(2)
        s.left_margin, s.right_margin = Cm(3), Cm(2)
        s.header_distance = s.footer_distance = Cm(1)
        s.different_first_page_header_footer = True
        self._so_trang(s)
        st = self.doc.styles["Normal"]
        st.font.name = "Times New Roman"
        st.font.size = Pt(14)
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
        st.paragraph_format.space_after = Pt(0)

    @staticmethod
    def _so_trang(sec):
        hp = sec.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if not hp._p.findall(qn("w:fldSimple")):
            f = OxmlElement("w:fldSimple")
            f.set(qn("w:instr"), "PAGE")
            r = OxmlElement("w:r")
            rp = OxmlElement("w:rPr")
            rf = OxmlElement("w:rFonts")
            for a in ("ascii", "hAnsi", "eastAsia", "cs"):
                rf.set(qn("w:" + a), "Times New Roman")
            rp.append(rf)
            sz = OxmlElement("w:sz")
            sz.set(qn("w:val"), "28")
            rp.append(sz)
            r.append(rp)
            t = OxmlElement("w:t")
            t.text = "1"
            r.append(t)
            f.append(r)
            hp._p.append(f)

    # ---- đoạn văn
    def p(self, text="", *, bold=False, italic=False, center=False, indent=1.0, justify=True,
          sau=6, truoc=0, giu=False, size=14, trai=0.0):
        para = self.doc.add_paragraph()
        if text:
            r = para.add_run(cap(text))
            r.bold, r.italic = bold, italic
            r.font.size = Pt(size)
            r.font.name = "Times New Roman"
        pf = para.paragraph_format
        pf.first_line_indent = Cm(0 if center else indent)
        if trai:
            pf.left_indent = Cm(trai)
        pf.space_after, pf.space_before = Pt(sau), Pt(truoc)
        pf.line_spacing = self.ls
        pf.keep_with_next = giu
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else (WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT)
        return para

    def nhieu_run(self, parts, *, indent=1.0, sau=6, justify=True, trai=0.0):
        """parts: [(text, bold, italic)]"""
        para = self.doc.add_paragraph()
        for t, b, i in parts:
            r = para.add_run(cap(t) if t[:1].isalpha() else t)
            r.bold, r.italic = b, i
            r.font.name = "Times New Roman"
            r.font.size = Pt(14)
        pf = para.paragraph_format
        pf.first_line_indent = Cm(indent)
        if trai:
            pf.left_indent = Cm(trai)
        pf.space_after = Pt(sau)
        pf.line_spacing = 1.15
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if justify else WD_ALIGN_PARAGRAPH.LEFT
        return para

    def quoc_hieu(self):
        a = self.p("CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", bold=True, center=True, sau=0, size=13)
        b = self.p("Độc lập - Tự do - Hạnh phúc", bold=True, center=True, sau=0, size=14)
        pPr = b._p.get_or_add_pPr()
        bd = OxmlElement("w:pBdr")
        bt = OxmlElement("w:bottom")
        for k, v in (("val", "single"), ("sz", "6"), ("space", "1"), ("color", "000000")):
            bt.set(qn("w:" + k), v)
        bd.append(bt)
        pPr.append(bd)
        b.paragraph_format.left_indent = Cm(3.2)
        b.paragraph_format.right_indent = Cm(3.2)
        self.p("", sau=6)
        return a

    def dia_danh_ngay(self, text):
        return self.p(text, italic=True, center=True, sau=10)

    def tieu_de(self, t, size=14):
        return self.p(t, bold=True, center=True, sau=4, giu=True, size=size)

    def dieu(self, t):
        return self.p(t, bold=True, indent=0, sau=4, truoc=6, giu=True)

    # ---- bảng
    def bang(self, tieu_de, widths, hang, can_giua=(), dam_cuoi=False, size=13):
        T = self.doc.add_table(rows=1, cols=len(tieu_de))
        T.alignment = WD_TABLE_ALIGNMENT.CENTER
        T.autofit = False
        for c, t in zip(T.rows[0].cells, tieu_de):
            c.text = cap(t)
        trpr = T.rows[0]._tr.get_or_add_trPr()
        trpr.append(OxmlElement("w:tblHeader"))
        for h in hang:
            cells = T.add_row().cells
            for c, t in zip(cells, h):
                c.text = cap(str(t))
        for i, r in enumerate(T.rows):
            r._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
            for j, c in enumerate(r.cells):
                c.width = Cm(widths[j])
                for para in c.paragraphs:
                    para.paragraph_format.space_after = Pt(2)
                    para.paragraph_format.line_spacing = 1.0
                    para.paragraph_format.first_line_indent = Cm(0)
                    para.alignment = WD_ALIGN_PARAGRAPH.CENTER if (j in can_giua or i == 0) else WD_ALIGN_PARAGRAPH.LEFT
                    for rr in para.runs:
                        rr.font.name = "Times New Roman"
                        rr.font.size = Pt(size)
                        if i == 0 or (dam_cuoi and i == len(T.rows) - 1):
                            rr.bold = True
        for gc, w in zip(T._tbl.tblGrid.gridCol_lst, widths):
            gc.set(qn("w:w"), str(round(w / 2.54 * 1440)))
        tp = T._tbl.tblPr
        tw = tp.find(qn("w:tblW"))
        if tw is None:
            tw = OxmlElement("w:tblW")
            tp.append(tw)
        tw.set(qn("w:type"), "dxa")
        tw.set(qn("w:w"), str(round(sum(widths) / 2.54 * 1440)))
        bd = OxmlElement("w:tblBorders")
        for e in ("top", "bottom", "left", "right", "insideH", "insideV"):
            x = OxmlElement("w:" + e)
            x.set(qn("w:val"), "single")
            x.set(qn("w:sz"), "4")
            x.set(qn("w:color"), "000000")
            bd.append(x)
        tp.append(bd)
        self.p("", sau=4)
        return T

    def chu_ky(self, trai, phai, ten_trai="", ten_phai=""):
        """Hai khối ký (trái, phải); mỗi khối là list dòng, dòng đầu in đậm."""
        T = self.doc.add_table(rows=1, cols=2)
        T.autofit = False
        for c, blk, ten in zip(T.rows[0].cells, (trai, phai), (ten_trai, ten_phai)):
            c.width = Cm(8.5)
            c.paragraphs[0].text = ""
            for k, dong in enumerate(blk):
                para = c.paragraphs[0] if k == 0 else c.add_paragraph()
                r = para.add_run(dong)
                r.bold = k == 0
                r.italic = k > 0
                r.font.name = "Times New Roman"
                r.font.size = Pt(14)
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_after = Pt(0)
            for _ in range(4):
                c.add_paragraph().paragraph_format.space_after = Pt(0)
            if ten:
                para = c.add_paragraph()
                r = para.add_run(ten)
                r.bold = True
                r.font.name = "Times New Roman"
                r.font.size = Pt(14)
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for gc, w in zip(T._tbl.tblGrid.gridCol_lst, (8.5, 8.5)):
            gc.set(qn("w:w"), str(round(w / 2.54 * 1440)))
        T.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        return T

    def phu_luc_section(self):
        """Phụ lục là section riêng, đánh số trang lại từ 1, không trang trắng."""
        s = self.doc.add_section(WD_SECTION.NEW_PAGE)
        s.different_first_page_header_footer = False
        pg = OxmlElement("w:pgNumType")
        pg.set(qn("w:start"), "1")
        s._sectPr.append(pg)
        s.header.is_linked_to_previous = False
        self._so_trang(s)
        return s

    def luu(self, duong_dan, tieu_de):
        for el in self.doc.element.iter():
            if el.tag == qn("w:t") and el.text:
                el.text = unicodedata.normalize("NFC", el.text)
        self.doc.core_properties.title = tieu_de
        self.doc.core_properties.author = "Trường Cao đẳng Kon Tum — dự thảo tư vấn"
        self.doc.save(duong_dan)


if __name__ == "__main__":
    # tự kiểm hàm đọc số
    assert bang_chu(852345246) == "tám trăm năm mươi hai triệu, ba trăm bốn mươi lăm nghìn, hai trăm bốn mươi sáu đồng", bang_chu(852345246)
    assert bang_chu(667433022) == "sáu trăm sáu mươi bảy triệu, bốn trăm ba mươi ba nghìn, không trăm hai mươi hai đồng", bang_chu(667433022)
    assert bang_chu(200229906) == "hai trăm triệu, hai trăm hai mươi chín nghìn, chín trăm lẻ sáu đồng", bang_chu(200229906)
    assert bang_chu(1519778268) == "một tỷ, năm trăm mười chín triệu, bảy trăm bảy mươi tám nghìn, hai trăm sáu mươi tám đồng"
    print("ok", bang_chu(8761456), "|", bang_chu(170469049))
