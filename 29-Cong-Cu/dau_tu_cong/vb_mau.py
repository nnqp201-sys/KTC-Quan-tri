# -*- coding: utf-8 -*-
"""Dựng văn bản của Trường TỪ MẪU 03-Templates (biên bản), không dựng bảng tiêu đề/chữ ký bằng tay.

Quy trình của skill the-thuc: sao mẫu → thay chữ trong run có sẵn → nhân bản đoạn cùng vai trò → xóa đoạn giữ chỗ.
Mẫu dùng: 03-Templates/03-09- Bien Ban/BB hop thong qua QC kiem tra HDDH.docx (đọc, không ghi).
"""
import os
import re
import sys
import unicodedata
from copy import deepcopy

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt
from docx.text.paragraph import Paragraph

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from du_an import kho  # noqa: E402

MAU_BB = kho("03-Templates", "03-09- Bien Ban", "BB hop thong qua QC kiem tra HDDH.docx")
_RE_HOA = re.compile(r"(:\s+)([^\W\d_])")


def cap(t):
    t = unicodedata.normalize("NFC", t)
    return _RE_HOA.sub(lambda m: m.group(1) + (m.group(2).upper() if m.group(2).islower() else m.group(2)), t)


def _set_runs(p_el, parts):
    """Đặt chữ vào các run sẵn có của đoạn: parts = [(text, bold)] — dùng lại run đầu làm khuôn."""
    p = Paragraph(p_el, None)
    runs = [r for r in p.runs]
    base = runs[0]._r
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    first = True
    for text, bold, italic in parts:
        if first:
            r_el = base
            first = False
        else:
            r_el = deepcopy(base)
            p_el.append(r_el)
        for t in r_el.findall(qn("w:t")):
            r_el.remove(t)
        t = OxmlElement("w:t")
        t.text = unicodedata.normalize("NFC", text)
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        r_el.append(t)
        rpr = r_el.find(qn("w:rPr"))
        if rpr is None:
            rpr = OxmlElement("w:rPr")
            r_el.insert(0, rpr)
        for tag, val in (("w:b", bold), ("w:i", italic)):
            for e in rpr.findall(qn(tag)):
                rpr.remove(e)
            if val:
                rpr.append(OxmlElement(tag))
    return p


class VanBanMau:
    def __init__(self, mau=MAU_BB):
        self.doc = Document(mau)
        self.body = self.doc.element.body
        els = list(self.body.iterchildren())
        self.t_dau = self.doc.tables[0]
        self.t_ky = self.doc.tables[1]
        # khuôn đoạn: tiêu đề (1), đoạn có chữ dẫn đậm (5), đoạn thường (16)
        self.k_tieu_de = deepcopy(els[1])
        self.k_lead = deepcopy(els[5])
        self.k_plain = deepcopy(els[16])
        self.p_loai = Paragraph(els[1], self.doc._body)
        self.p_trich = Paragraph(els[2], self.doc._body)
        # xóa đoạn giữ chỗ giữa khối tiêu đề (đoạn 3 chứa đường kẻ) và bảng chữ ký
        for e in els[4:-3]:
            if e.tag == qn("w:p"):
                self.body.remove(e)
        self.anchor = self.t_ky._tbl
        self._last = None  # số trang: mẫu đã có sẵn ở đầu trang (không hiện ở trang 1)

    # ---- số trang: canh giữa lề trên, không hiện ở trang 1 (titlePg đã bật trong mẫu)
    @staticmethod
    def _so_trang(sec):
        hp = sec.header.paragraphs[0] if sec.header.paragraphs else sec.header.add_paragraph()
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

    # ---- phần đầu
    def dau(self, so_text, ngay_text, loai, trich):
        c0 = self.t_dau.cell(1, 0).paragraphs[0]
        _set_runs(c0._p, [(so_text, False, False)])
        c1 = self.t_dau.cell(1, 1).paragraphs[0]
        _set_runs(c1._p, [(ngay_text, False, True)])
        _set_runs(self.p_loai._p, [(loai, True, False)])
        p = _set_runs(self.p_trich._p, [(trich.split("\n")[0], True, False)])
        for dong in trich.split("\n")[1:]:  # các dòng sau: xuống dòng trong cùng đoạn trích yếu
            base = p.runs[-1]._r
            br = deepcopy(base)
            for t in br.findall(qn("w:t")):
                br.remove(t)
            br.append(OxmlElement("w:br"))
            t = OxmlElement("w:t")
            t.text = unicodedata.normalize("NFC", dong)
            br.append(t)
            self.p_trich._p.append(br)

    # ---- đoạn
    def _chen(self, el):
        self.anchor.addprevious(el)
        self._last = el
        return Paragraph(el, self.doc._body)

    def p(self, text="", *, bold=False, italic=False, center=False, indent=1.0, justify=True,
          sau=6, truoc=0, giu=False, size=None, trai=0.0, **_):
        el = deepcopy(self.k_plain)
        para = _set_runs(el, [(cap(text) if text else "", bold, italic)])
        if size:
            for r in para.runs:
                r.font.size = Pt(size)
        # Kiểu đoạn chuẩn (như mẫu): dàn đều hai lề · thụt đầu dòng 1,27 cm · trước/sau 6 pt · giãn dòng 1,4.
        # Mọi đoạn lời văn đều theo đúng một kiểu; chỉ dòng giữa trang (tiêu đề phần) mới canh giữa.
        pf = para.paragraph_format
        if center:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.first_line_indent = Cm(0)
        pf.keep_with_next = giu
        return self._chen_para(el, para)

    def ngat_trang(self):
        """Đoạn kế tiếp bắt đầu ở trang mới."""
        self._pb = True

    def _chen_para(self, el, para):
        if getattr(self, "_pb", False):
            para.paragraph_format.page_break_before = True
            self._pb = False
        self.anchor.addprevious(el)
        self._last = el
        return para

    def tieu_de(self, t, size=None):
        el = deepcopy(self.k_lead)
        para = _set_runs(el, [(cap(t), True, False)])
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para.paragraph_format.first_line_indent = Cm(0)
        para.paragraph_format.keep_with_next = True
        return self._chen_para(el, para)

    def dieu(self, t):
        el = deepcopy(self.k_lead)
        para = _set_runs(el, [(cap(t), True, False)])
        para.paragraph_format.keep_with_next = True  # thụt đầu dòng 1,27 như tiêu đề mục của mẫu
        return self._chen_para(el, para)

    def giu_cuoi(self):
        if self._last is not None:
            Paragraph(self._last, self.doc._body).paragraph_format.keep_with_next = True

    # ---- bảng dữ liệu (phụ lục, bảng kê) — bảng dữ liệu được phép dựng; bảng tiêu đề/chữ ký thì không
    def bang(self, tieu_de, widths, hang, can_giua=(), dam_cuoi=False, size=13):
        T = self.doc.add_table(rows=1, cols=len(tieu_de))
        T.alignment = WD_TABLE_ALIGNMENT.CENTER
        T.autofit = False
        for c, t in zip(T.rows[0].cells, tieu_de):
            c.text = cap(t)
        T.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
        for h in hang:
            cells = T.add_row().cells
            for c, t in zip(cells, h):
                c.text = cap(str(t))
        for i, r in enumerate(T.rows):
            r._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
            for j, c in enumerate(r.cells):
                c.width = Cm(widths[j])
                va = OxmlElement("w:vAlign")  # canh giữa theo chiều dọc ô (bảng thông số KTC, TT-51)
                va.set(qn("w:val"), "center")
                c._tc.get_or_add_tcPr().append(va)
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
        self.anchor.addprevious(T._tbl)
        self._last = T._tbl
        return T

    # ---- bảng chữ ký (nhân bản của mẫu; chỉ thay chữ)
    def ky(self, trai_vai, trai_chuc, trai_ten, phai_vai, phai_chuc, phai_ten, noi_nhan):
        t = self.t_ky
        _set_runs(t.cell(0, 0).paragraphs[0]._p, [(trai_vai, True, False)])
        _set_runs(t.cell(0, 1).paragraphs[0]._p, [(phai_vai, True, False)])
        c10 = t.cell(1, 0)
        if c10.paragraphs[0].runs:
            _set_runs(c10.paragraphs[0]._p, [(trai_chuc, True, False)])
        else:
            self._them_run(c10.paragraphs[0], trai_chuc)
        _set_runs(c10.paragraphs[1]._p, [(trai_ten, True, False)])
        c11 = t.cell(1, 1)
        _set_runs(c11.paragraphs[0]._p, [(phai_chuc, True, False)])
        _set_runs(c11.paragraphs[1]._p, [(phai_ten, True, False)])
        cn = t.cell(2, 0)
        ps = cn.paragraphs
        if noi_nhan is None:  # không có khối "Nơi nhận": xóa chữ giữ chỗ của mẫu
            for p_ in ps:
                for r_ in list(p_.runs):
                    r_._r.getparent().remove(r_._r)
            noi_nhan = []
        for k, dong in enumerate(noi_nhan):
            idx = k + 1
            if idx < len(ps) - 1:
                _set_runs(ps[idx]._p, [(dong, False, False)])
        return t

    def sau_ky(self, text, *, bold=False, italic=False, size=None):
        """Đoạn nằm SAU bảng chữ ký (ghi chú của biểu mẫu)."""
        el = deepcopy(self.k_plain)
        para = _set_runs(el, [(cap(text), bold, italic)])
        if size:
            for r in para.runs:
                r.font.size = Pt(size)
        prev = getattr(self, "_sau", None)
        (prev if prev is not None else self.t_ky._tbl).addnext(el)
        self._sau = el
        return para

    @staticmethod
    def _them_run(p, text):
        r = p.add_run(text)
        r.bold = True

    # ---- phụ lục: section riêng, số trang từ 1, không trang trắng
    def phu_luc_section(self):
        s = self.doc.add_section(WD_SECTION.NEW_PAGE)
        s.different_first_page_header_footer = False
        pg = OxmlElement("w:pgNumType")
        pg.set(qn("w:start"), "1")
        s._sectPr.append(pg)
        self.anchor = self.body.find(qn("w:sectPr"))
        return s

    def luu(self, duong_dan, tieu_de):
        for el in self.doc.element.iter():
            if el.tag == qn("w:t") and el.text:
                el.text = unicodedata.normalize("NFC", el.text)
        self.doc.core_properties.title = tieu_de
        self.doc.core_properties.author = "Trường Cao đẳng Kon Tum — dự thảo tư vấn"
        self.doc.save(duong_dan)
