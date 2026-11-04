# -*- coding: utf-8 -*-
"""Dựng hai bảng quy trình riêng cho hai gói tư vấn chuẩn bị đầu tư (KS-BCKTKT và QLDA).

Mẫu thể thức lấy từ tệp nền _base.docx của bản "Quy trình dự án nhóm C" (A4 ngang, lề 2-2-3-2, TNR 14).
Số liệu gói thầu đọc từ du-an_CLC-2026-2030.yaml; chữ của bảng ở qt_tu_van_noi_dung.py.

Chạy:  python -X utf8 lap_quy_trinh_tu_van.py [--out THƯ_MỤC] [--goi KS|QLDA]
"""
import argparse
import os
import re
import sys
import unicodedata
from copy import deepcopy

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.text.paragraph import Paragraph

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from du_an import ket_qua, tai  # noqa: E402
import qt_tu_van_noi_dung as N  # noqa: E402

D = tai()
KS = D["goi_thau"]["KS"]
QL = D["goi_thau"]["QLDA"]
NGAY = "28 tháng 10 năm 2026"
GOC_NEN = ket_qua("2026-10-28", "Quy-trinh-du-an-nhom-C-CLC", "_base.docx")

# ---------------------------------------------------------------- Nguồn (nhãn, liên kết)
CB = "https://congbao.chinhphu.vn/van-ban/"
NGUON = {
    "QD2374": ("QĐ 2374/QĐ-CĐKT ngày 27/10/2026", None),
    "QD2375": ("QĐ 2375/QĐ-CĐKT ngày 27/10/2026", None),
    "QD2158": ("QĐ 2158/QĐ-CĐKT ngày 29/9/2026", None),
    "DT": ("Luật Đấu thầu ngày 23/6/2023 (VBHN 74/VBHN-VPQH)", CB + "van-ban-hop-nhat-so-74-vbhn-vpqh-469204.htm"),
    "DTC": ("Luật Đầu tư công ngày 29/11/2024 (VBHN 03/VBHN-VPQH ngày 05/02/2026)", CB + "van-ban-hop-nhat-so-03-vbhn-vpqh-468932.htm"),
    "214": ("NĐ 214/2025/NĐ-CP đã sửa đổi (VBHN 36/2026/VBHN-NĐ-BTC)", "https://chinhphu.vn/?docid=219604&pageid=27160"),
    "XD": ("Luật Xây dựng ngày 10/12/2025", CB + "luat-so-135-2025-qh15-468695.htm"),
    "217": ("NĐ 217/2026/NĐ-CP (đọc VBHN 91/2026/VBHN-NĐ-BXD)", "https://xdcs.cdnchinhphu.vn/446259493575335936/2026/9/29/91-vbhn-bxd-signed-1790654585945447247778.pdf"),
    "206": ("NĐ 206/2026/NĐ-CP", CB + "nghi-dinh-so-206-2026-nd-cp-469768.htm"),
    "207": ("NĐ 207/2026/NĐ-CP", CB + "nghi-dinh-so-207-2026-nd-cp-469769.htm"),
    "210": ("NĐ 210/2026/NĐ-CP", CB + "nghi-dinh-so-210-2026-nd-cp-469772.htm"),
    "212": ("NĐ 212/2026/NĐ-CP", None),
    "254": ("NĐ 254/2025/NĐ-CP — phần thanh toán còn hiệu lực", CB + "nghi-dinh-so-254-2025-nd-cp-46303.htm"),
    "193": ("NĐ 193/2026/NĐ-CP", CB + "nghi-dinh-so-193-2026-nd-cp-469703.htm"),
    "73": ("TT 73/2026/TT-BTC", CB + "thong-tu-so-73-2026-tt-btc-469924.htm"),
    "1040": ("QĐ 1040/QĐ-BXD ngày 26/6/2026 (mẫu hợp đồng xây dựng)", "https://luatvietnam.vn/xay-dung/quyet-dinh-1040-qd-bxd-2026-cong-bo-mau-hop-dong-xay-dung-438880-d1.html"),
    "TT36": ("TT 36/2026/TT-BXD", "https://luatvietnam.vn/dau-tu/thong-tu-36-2026-tt-bxd-huong-dan-xac-dinh-va-quan-ly-chi-phi-dau-tu-xay-dung-438882-d1.html"),
    "TT79": ("TT 79/2025/TT-BTC", None),
    "QD64": ("QĐ 64/2026/QĐ-UBND ngày 25/5/2026", None),
    "QD32": ("QĐ 32/2025/QĐ-UBND ngày 15/10/2025 (Quảng Ngãi)", "https://congbao.quangngai.gov.vn/cong-bao/quyet-dinh-so-32-2025-qd-ubnd-quy-dinh-ve-mot-so-noi-dung-quan-ly-hoat-dong-xay-dung-tren-dia-ban-tinh-quang-ngai.html"),
    "QD15": ("QĐ 15/2026/QĐ-UBND ngày 07/02/2026 (Quảng Ngãi)", "https://congbao.quangngai.gov.vn/cong-bao/quyet-dinh-so-15-2026-qd-ubnd-quy-dinh-ve-phan-cap-quan-ly-chat-luong-thi-cong-xay-dung-va-bao-tri-cong-trinh-xay-dung-t.html"),
    "QD08": ("QĐ 08/2026/QĐ-UBND ngày 20/01/2026 (Quảng Ngãi)", "https://congbao.quangngai.gov.vn/cong-bao/quy-dinh-ve-quan-ly-trat-tu-xay-dung-trach-nhiem-phoi-hop-quan-ly-trat-tu-xay-dung-phan-cap-quan-ly-trat-tu-xay-dung-va-.html"),
    "QD14": ("QĐ 14/2026/QĐ-UBND ngày 07/02/2026 (Quảng Ngãi)", None),
    "QD152": ("QĐ 152/2026/QĐ-UBND ngày 22/9/2026 (Quảng Ngãi)", "https://luatvietnam.vn/chinh-sach-moi-hang-thang/danh-sach-vb-co-hieu-luc-thang-10-2026-559-112979-article.html"),
    "QD871": ("QĐ 871/QĐ-UBND ngày 17/3/2026 (Quảng Ngãi)", "https://stc.quangngai.gov.vn/thong-tin-hoat-dong-nganh/phe-duyet-quy-che-chi-tieu-cho-cong-tac-tham-tra-phe-duyet-quyet-toan-von-dau-tu-du-an-hoan-thanh.html"),
    "NQ72": ("NQ 72/2026/NQ-HĐND ngày 17/7/2026 (Quảng Ngãi)", "https://luatvietnam.vn/dau-tu/nghi-quyet-72-2026-nq-hdnd-quang-ngai-phan-cap-tham-quyen-phan-bo-ke-hoach-dau-tu-cong-441115-d2.html"),
    "SXD7946": ("CV 7946/SXD-HĐXD ngày 05/10/2026 của Sở Xây dựng Quảng Ngãi", "https://sxd.quangngai.gov.vn/chi-dao-dieu-hanh/van-ban-so-xay-dung/v-v-bo-sung-va-hoan-thien-ho-so-tham-dinh-bao-cao-kinh-te-ky-thuat-dau-tu-xay-dung-du-an-cai-tao-nang-cap-san-van-dong-h.html"),
    "QD148": ("QĐ 148/2026/QĐ-CTUBND ngày 11/9/2026 (Quảng Ngãi)", "https://congbao.quangngai.gov.vn/upload/2007098/20261007/hoan_chinh__QD_148_63392.pdf"),
}


def vnd(n):
    return f"{int(n):,}".replace(",", ".")


def so(s):
    return int(re.sub(r"\D", "", s))


def lam_tron(x, ti_le):
    return (x * ti_le + 50) // 100


_RE_HOA = re.compile(r"(:\s+)([^\W\d_])")


def cap(t):
    """Viết hoa chữ đầu sau dấu hai chấm (quy ước của Trường)."""
    t = unicodedata.normalize("NFC", t)
    return _RE_HOA.sub(lambda m: m.group(1) + (m.group(2).upper() if m.group(2).islower() else m.group(2)), t)


# ---------------------------------------------------------------- Phần chung của tài liệu
def mo_nen():
    doc = Document(GOC_NEN)
    ordinary = deepcopy(doc.paragraphs[9]._p)
    head = doc.tables[0]

    def thay(p, text):
        runs = [r for r in p.runs if r.text]
        if runs:
            runs[0].text = text
            for r in runs[1:]:
                r.text = ""
        else:
            p.add_run(text)

    thay(head.cell(0, 0).paragraphs[0], "UBND TỈNH QUẢNG NGÃI")
    thay(head.cell(0, 0).paragraphs[1], "TRƯỜNG CAO ĐẲNG KON TUM")
    thay(head.cell(1, 0).paragraphs[0], "DỰ THẢO HƯỚNG DẪN")
    thay(head.cell(1, 1).paragraphs[0], "Quảng Ngãi, ngày " + NGAY)
    head.autofit = False
    for rowh in head.rows:
        for ch in rowh.cells:
            ch.width = Cm(12.35)
    for colh in head.columns:
        colh.width = Cm(12.35)
    for g in head._tbl.tblGrid.gridCol_lst:
        g.set(qn("w:w"), str(round(12.35 / 2.54 * 1440)))
    hw = head._tbl.tblPr.find(qn("w:tblW"))
    if hw is not None:
        hw.set(qn("w:type"), "dxa")
        hw.set(qn("w:w"), str(round(24.7 / 2.54 * 1440)))
    body = doc._element.body
    for e in list(body):
        if e is not head._tbl and e.tag != qn("w:sectPr"):
            body.remove(e)
    for sec in doc.sections:
        sec.page_width = Cm(29.7)
        sec.page_height = Cm(21)
        sec.top_margin = Cm(2)
        sec.bottom_margin = Cm(2)
        sec.left_margin = Cm(3)
        sec.right_margin = Cm(2)
        sec.header_distance = Cm(0.8)
        sec.footer_distance = Cm(0.8)
        sec.different_first_page_header_footer = True
        for part in [sec.header, sec.footer, sec.first_page_header, sec.first_page_footer]:
            for child in list(part._element):
                part._element.remove(child)
            part.add_paragraph()
        hp = sec.header.paragraphs[0] if sec.header.paragraphs else sec.header.add_paragraph()
        hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), "PAGE")
        hp._p.append(fld)
    for st in doc.styles:
        if st.type in (1, 2):
            st.font.name = "Times New Roman"
            st.font.size = Pt(14)
            st.font.color.rgb = RGBColor(0, 0, 0)
    return doc, ordinary, body


class Dung:
    def __init__(self):
        self.doc, self.ordinary, self.body = mo_nen()

    # --- đoạn văn
    def para(self, t="", bold=False, center=False):
        e = deepcopy(self.ordinary)
        for c in list(e):
            if c.tag != qn("w:pPr"):
                e.remove(c)
        self.body.insert(len(self.body) - 1, e)
        p = Paragraph(e, self.doc._body)
        if t:
            p.add_run(cap(t)).bold = bold
        p.paragraph_format.first_line_indent = Cm(0 if center else 1)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.04
        p.paragraph_format.keep_with_next = False
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.JUSTIFY
        return p

    def title(self, t):
        p = self.para(t, True, True)
        p.paragraph_format.keep_with_next = True
        return p

    def heading(self, t):
        p = self.para(t, True)
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.keep_with_next = True
        return p

    def link(self, p, label, url):
        if not url:
            r = p.add_run(label)
            return
        h = OxmlElement("w:hyperlink")
        h.set(qn("r:id"), p.part.relate_to(url, RT.HYPERLINK, is_external=True))
        r = OxmlElement("w:r")
        pr = OxmlElement("w:rPr")
        f = OxmlElement("w:rFonts")
        for a in ["ascii", "hAnsi", "eastAsia", "cs"]:
            f.set(qn("w:" + a), "Times New Roman")
        pr.append(f)
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), "28")
        pr.append(sz)
        r.append(pr)
        tx = OxmlElement("w:t")
        tx.text = label
        r.append(tx)
        h.append(r)
        p._p.append(h)

    def refs(self, p, spec):
        for i, it in enumerate(spec.split("|")):
            k, cl = it.split(":", 1)
            if i:
                p.add_run("\n")
            label, url = NGUON[k]
            self.link(p, label, url)
            p.add_run("; " + cl + ".")

    # --- bảng
    @staticmethod
    def _shade(c, color):
        e = OxmlElement("w:shd")
        e.set(qn("w:fill"), color)
        c._tc.get_or_add_tcPr().append(e)

    def _hoan_thien(self, T, widths, cant_split=False):
        for i, r in enumerate(T.rows):
            if cant_split:
                r._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
            for j, c in enumerate(r.cells):
                c.width = Cm(widths[j])
                c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP if i else WD_CELL_VERTICAL_ALIGNMENT.CENTER
                for p in c.paragraphs:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    p.paragraph_format.first_line_indent = Cm(0)
                    p.paragraph_format.space_after = Pt(2)
                    p.paragraph_format.space_before = Pt(0)
                    p.paragraph_format.line_spacing = 1
                    if i == 0:
                        for rr in p.runs:
                            rr.bold = True
                    for rr in p.runs:
                        rr.font.name = "Times New Roman"
                        rr.font.size = Pt(14)
        for c, w in zip(T.columns, widths):
            c.width = Cm(w)
        for gc, w in zip(T._tbl.tblGrid.gridCol_lst, widths):
            gc.set(qn("w:w"), str(round(w / 2.54 * 1440)))
        tp = T._tbl.tblPr
        tw = tp.find(qn("w:tblW"))
        tw.set(qn("w:type"), "dxa")
        tw.set(qn("w:w"), str(round(sum(widths) / 2.54 * 1440)))
        borders = OxmlElement("w:tblBorders")
        for edge in ["top", "bottom", "left", "right", "insideH", "insideV"]:
            e = OxmlElement("w:" + edge)
            e.set(qn("w:val"), "single")
            e.set(qn("w:sz"), "4")
            e.set(qn("w:color"), "808080")
            borders.append(e)
        tp.append(borders)

    def bang(self, tieu_de, widths, hang, dam_hang_cuoi=False):
        T = self.doc.add_table(rows=1, cols=len(tieu_de))
        T.autofit = False
        T.alignment = WD_TABLE_ALIGNMENT.CENTER
        for c, t in zip(T.rows[0].cells, tieu_de):
            c.text = cap(t)
        T.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
        for h in hang:
            cells = T.add_row().cells
            for c, t in zip(cells, h):
                c.text = cap(str(t))
        self._hoan_thien(T, widths)
        if dam_hang_cuoi:
            for c in T.rows[-1].cells:
                for p in c.paragraphs:
                    for rr in p.runs:
                        rr.bold = True
        return T

    def bang_quy_trinh(self, pha, dong):
        widths = [1.35, 3.6, 1.3, 1.5, 1.7, 2.3, 4.3, 8.65]
        tieu_de = ["STT", "Công việc/Sản phẩm", "Chủ đầu tư", "Nhà thầu tư vấn", "Tư vấn khác", "Cơ quan khác", "Căn cứ/nguồn", "Ghi chú"]
        T = self.doc.add_table(rows=1, cols=8)
        T.autofit = False
        T.alignment = WD_TABLE_ALIGNMENT.CENTER
        for c, t in zip(T.rows[0].cells, tieu_de):
            c.text = t
        T.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
        last = None
        for n, (ph, cv, cdt, nt, tv, ck, nguon, gc) in enumerate(dong, 1):
            if ph != last:
                cells = T.add_row().cells
                cells[0].text = ph
                cells[1].text = pha[ph]
                for c in cells:
                    self._shade(c, "E7E6E6")
                    for p in c.paragraphs:
                        p.paragraph_format.keep_with_next = True
                last = ph
            cells = T.add_row().cells
            for c, t in zip(cells, [str(n), cv, cdt, nt, tv, ck, "", gc]):
                c.text = cap(t)
            self.refs(cells[6].paragraphs[0], nguon)
            if n % 2 == 0:
                for c in cells:
                    self._shade(c, "F5F5F5")
        self._hoan_thien(T, widths)
        for r in T.rows:
            if r.cells[0].text in pha:
                r._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        return T

    def luu(self, duong_dan, tieu_de_tai_lieu):
        for el in list(self.doc._element.iter()) + list(self.doc.styles.element.iter()):
            if el.tag == qn("w:t") and el.text:
                el.text = unicodedata.normalize("NFC", el.text)
            if el.tag == qn("w:rFonts"):
                for a in list(el.attrib):
                    if "Theme" in a:
                        del el.attrib[a]
                for a in ["ascii", "hAnsi", "eastAsia", "cs"]:
                    el.set(qn("w:" + a), "Times New Roman")
            if el.tag == qn("w:color"):
                for a in list(el.attrib):
                    if "theme" in a.lower():
                        del el.attrib[a]
                el.set(qn("w:val"), "000000")
            if el.tag.endswith("}srgbClr"):
                el.set("val", "000000")
            if el.tag.endswith("}schemeClr"):
                el.tag = el.tag.replace("schemeClr", "srgbClr")
                el.set("val", "000000")
                for child in list(el):
                    el.remove(child)
            if el.tag.endswith("}stroke"):
                el.set("color", "black")
            if el.tag.endswith("}line") and "strokecolor" in el.attrib:
                el.set("strokecolor", "black")
        for p in self.doc.paragraphs:
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(14)
        self.doc.core_properties.title = tieu_de_tai_lieu
        self.doc.core_properties.author = "Trường Cao đẳng Kon Tum — dự thảo tư vấn"
        self.doc.save(duong_dan)


# ---------------------------------------------------------------- Nội dung dùng chung
def phan_von(d):
    ks, ql = so(KS["gia"]), so(QL["gia"])
    v26 = D["du_an"]["von_2026_trieu_dong"]
    von = v26["tong"] * 1_000_000
    cbdt = D["du_an"]["du_toan_cbdt_dong"]
    tu_ks = lam_tron(ks, 30)
    tu_ql = 200_229_906  # số thống nhất trong biên bản thương thảo QLDA
    ks26 = round(von * ks / (ks + ql))  # chia vốn 2026 theo tỷ lệ giá hợp đồng
    ql26 = von - ks26
    ks27, ql27 = tu_ks - ks26, tu_ql - ql26
    d.heading("PHẦN 2. VỐN VÀ PHƯƠNG ÁN TẠM ỨNG ĐÃ CHỐT")
    d.heading("2.1. Vốn năm 2026 và mức tạm ứng của hai hợp đồng tư vấn")
    d.para(
        f"Vốn kế hoạch năm 2026 của dự án là {vnd(von)} đồng (ngân sách trung ương {vnd(v26['ngan_sach_trung_uong'] * 1_000_000)}; ngân sách tỉnh đối ứng {vnd(v26['ngan_sach_tinh_doi_ung'] * 1_000_000)}), "
        f"chỉ bằng khoảng {von * 100 / cbdt:.1f}% dự toán chuẩn bị đầu tư {vnd(cbdt)} đồng; phần chưa có kế hoạch vốn năm 2026 là {vnd(cbdt - von)} đồng (số so sánh do người lập tính, không phải số trong văn bản). "
        "Hai hợp đồng tư vấn cộng đúng dự toán chuẩn bị đầu tư nên mọi khoản tạm ứng và thanh toán của hai gói cùng nằm trong một hạn mức vốn. Vốn năm 2027 đã được xác nhận có."
    )
    hang = [
        ("Gói khảo sát, lập BCKTKT (Trường Phát Land)", vnd(ks), vnd(tu_ks), vnd(ks26), vnd(ks27)),
        ("Gói tư vấn QLDA (Thành Vinh)", vnd(ql), vnd(tu_ql), vnd(ql26), vnd(ql27)),
        ("Cộng hai hợp đồng", vnd(ks + ql), vnd(tu_ks + tu_ql), vnd(ks26 + ql26), vnd(ks27 + ql27)),
    ]
    d.bang(["Hợp đồng", "Giá hợp đồng (đồng)", "Tạm ứng 30% (đồng)", "Tạm ứng năm 2026 (đồng)", "Tạm ứng năm 2027 (đồng)"],
           [6.2, 4.0, 4.0, 4.3, 4.2], hang, dam_hang_cuoi=True)
    d.para(
        f"Phương án đã chốt: Mỗi hợp đồng tạm ứng 30% giá hợp đồng. Năm 2026 căn cứ vốn {vnd(von)} đồng, chia cho hai hợp đồng theo tỷ lệ giá hợp đồng (gói khảo sát, lập BCKTKT {vnd(ks26)} đồng; gói QLDA {vnd(ql26)} đồng, mỗi gói tương ứng cùng một tỷ lệ khoảng {ks26 * 100 / tu_ks:.2f}% mức tạm ứng 30%). "
        f"Năm 2027 tạm ứng phần còn lại để đủ 30% (gói khảo sát, lập BCKTKT {vnd(ks27)} đồng; gói QLDA {vnd(ql27)} đồng). Các số làm tròn đến đồng."
    )
    d.para(
        "Đối chiếu quy định: Mức 30% nằm trong khoảng 20% đến 30% giá hợp đồng tư vấn có giá trị đến 10 tỷ đồng (NĐ 210/2026/NĐ-CP, Điều 12.3.g, 12.3.h). "
        "Tổng tạm ứng năm 2026 không vượt kế hoạch vốn năm đã phân bổ (NĐ 254/2025/NĐ-CP, Điều 9.4); vốn năm được tạm ứng đến hết 31/12 năm kế hoạch (Điều 12.1). "
        "Hợp đồng thuê tư vấn QLDA không yêu cầu bảo lãnh tạm ứng (Điều 9.2.b.iii); tạm ứng gói khảo sát không quá 01 tỷ đồng nên không bắt buộc bảo lãnh (NĐ 210, Điều 12.3.c)."
    )
    d.para(
        "Việc còn lại: Ghi phân kỳ tạm ứng vào hợp đồng; lập hồ sơ tạm ứng năm 2027 ngay khi kế hoạch vốn năm 2027 được giao (NQ 72/2026/NQ-HĐND quy định thẩm quyền phân bổ, điều chỉnh; cần đọc toàn văn)."
    )


def nguon_dia_phuong(d, goi):
    d.heading("PHẦN 4. VĂN BẢN CỦA TỈNH QUẢNG NGÃI VÀ TRẠNG THÁI ÁP DỤNG")
    d.para(
        "Đã tra trên Công báo và cổng thông tin của tỉnh, Sở Xây dựng, Sở Tài chính đến ngày 28/10/2026. "
        "Điểm chung cần lưu ý: Từ 01/7/2026, NĐ 217/2026/NĐ-CP thay NĐ 175/2024/NĐ-CP (Điều 75.2) và bãi bỏ Điều 4, Điều 5, Điều 6, Điều 7 của NĐ 140/2025/NĐ-CP, "
        "Điều 10, Điều 11 và Phụ lục III của NĐ 144/2025/NĐ-CP (Điều 75.3.b, Điều 75.3.c). Đây là cơ sở của QĐ 32/2025/QĐ-UBND và QĐ 15/2026/QĐ-UBND, nên hai quyết định này cần xác nhận còn áp dụng phần nào cho đến khi tỉnh ban hành văn bản thay thế."
    )
    hang = []
    chung = [
        ("QD32", "Quy định thẩm quyền thẩm định và quy trình thẩm định, phê duyệt, điều chỉnh BCKTKT dự án đầu tư công do UBND các cấp quyết định đầu tư: Chủ tịch UBND tỉnh quyết định đầu tư thì Sở Xây dựng chủ trì thẩm định (Điều 3); bổ sung hồ sơ một lần trong 07 ngày, 15 ngày không bổ sung thì dừng (Điều 7); thời gian thẩm định không quá 05 ngày (Điều 7.9).",
         "Đã đọc toàn văn trên Công báo. Dựa Luật Xây dựng 2014 và NĐ 175/2024; dự thảo quyết định thay thế đã lấy ý kiến 13–23/7/2026, thẩm định 27/7–26/8/2026, chưa thấy bản ban hành.",
         {"KS": "Tham chiếu quy trình trình thẩm định (bước 16–18); hỏi Sở Xây dựng văn bản đang áp dụng.", "QLDA": "Tham chiếu khi hỗ trợ hồ sơ thẩm định (bước 11)."}),
        ("SXD7946", "Sở Xây dựng yêu cầu bổ sung hồ sơ thẩm định BCKTKT một dự án cải tạo, nâng cấp.",
         "Đã đọc tiêu đề và số hiệu trên trang Sở Xây dựng; chưa đọc nội dung.",
         {"KS": "Chứng cứ Sở Xây dựng vẫn tiếp nhận thẩm định BCKTKT sau 01/7/2026 (bước 16).", "QLDA": None}),
        ("QD15", "Phân cấp kiểm tra công tác nghiệm thu: Sở Xây dựng kiểm tra nghiệm thu công trình vốn đầu tư công thuộc thẩm quyền thẩm định của cơ quan chuyên môn về xây dựng thuộc UBND tỉnh theo QĐ 32/2025 (Điều 5.1.a).",
         "Đã đọc trích toàn văn. Dẫn NĐ 06/2021 (đã hết hiệu lực theo NĐ 207/2026); dự thảo thay thế lấy ý kiến 06–21/9/2026 và thẩm định từ 01/10/2026, chưa ban hành.",
         {"KS": None, "QLDA": "Xác định cơ quan kiểm tra nghiệm thu giai đoạn thi công (bước 19)."}),
        ("QD08", "Quản lý trật tự xây dựng và tiếp nhận thông báo khởi công xây dựng công trình.",
         "Chỉ thấy tiêu đề, ngày ban hành 20/01/2026, hiệu lực 31/01/2026 trên Công báo. Dự thảo thay thế đang thẩm định (23/8–22/9/2026).",
         {"KS": None, "QLDA": "Cơ quan nhận thông báo khởi công (bước 13); hỏi lại mẫu và đầu mối."}),
        ("QD14", "Phân cấp thẩm quyền cấp giấy phép xây dựng, quy mô và thời hạn tồn tại của công trình cấp giấy phép có thời hạn.",
         "Chỉ thấy tiêu đề và ngày ban hành 07/02/2026 trong báo cáo của Sở Xây dựng; chưa đọc nội dung.",
         {"KS": "Xác định thủ tục giấy phép xây dựng khi cải tạo (bước 15).", "QLDA": "Kiểm tra điều kiện khởi công có giấy phép (bước 13)."}),
        ("QD152", "Phân cấp cho Sở Xây dựng cấp chứng chỉ hành nghề hoạt động xây dựng cho cá nhân.",
         "Chỉ thấy tiêu đề, ban hành 22/09/2026, hiệu lực 01/10/2026 trong danh sách văn bản có hiệu lực tháng 10/2026; chưa đọc nội dung.",
         {"KS": "Nơi cấp, cấp lại chứng chỉ khi thay nhân sự (bước 8).", "QLDA": None}),
        ("NQ72", "Phân cấp thẩm quyền quyết định phân bổ kế hoạch đầu tư công trung hạn, hằng năm và điều chỉnh kế hoạch vốn ngân sách trung ương các chương trình mục tiêu quốc gia 2026–2030.",
         "Chỉ thấy tiêu đề và ngày 17/7/2026; chưa đọc nội dung.",
         {"KS": "Xác định ai quyết định bổ sung hoặc điều chỉnh vốn chuẩn bị đầu tư (Phần 2).", "QLDA": "Xác định ai quyết định bổ sung hoặc điều chỉnh vốn (Phần 2)."}),
        ("QD871", "Quy chế chi tiêu cho công tác thẩm tra, phê duyệt quyết toán vốn đầu tư dự án hoàn thành thuộc thẩm quyền quyết định đầu tư của Chủ tịch UBND tỉnh.",
         "Thông tin từ trang Sở Tài chính; chưa đọc toàn văn.",
         {"KS": None, "QLDA": "Chi phí thẩm tra, phê duyệt quyết toán (bước 21)."}),
        ("QD148", "Phân cấp lập, thẩm định, phê duyệt dự toán nhiệm vụ chuẩn bị đầu tư đối với dự án KHÔNG có cấu phần xây dựng thuộc thẩm quyền quyết định đầu tư của Chủ tịch UBND tỉnh.",
         "Đã đọc toàn văn; hiệu lực 11/9/2026. Không áp dụng cho dự án này vì có cấu phần xây dựng.",
         {"KS": "Không viện dẫn.", "QLDA": "Không viện dẫn."}),
    ]
    for k, nd, tt, dung in chung:
        u = dung[goi]
        if u is None:
            continue
        label, url = NGUON[k]
        hang.append((label, nd, tt, u))
    T = d.bang(["Văn bản", "Nội dung liên quan", "Trạng thái đọc và hiệu lực", "Dùng trong bảng"], [5.4, 8.3, 6.0, 5.0], hang)
    # chuyển nhãn văn bản thành liên kết
    for i, (k, *_r) in enumerate([c for c in chung if c[3][goi] is not None], 1):
        label, url = NGUON[k]
        if url:
            cell = T.rows[i].cells[0]
            p = cell.paragraphs[0]
            for r in list(p.runs):
                r._r.getparent().remove(r._r)
            d.link(p, label, url)
    d.para(
        "Không dùng trang thủ tục hành chính “Thủ tục thẩm định Báo cáo nghiên cứu khả thi, Báo cáo kinh tế - kỹ thuật” của Sở Xây dựng (còn dẫn NĐ 15/2021, QĐ 32/2021/QĐ-UBND, TT 209/2016/TT-BTC): Nội dung cũ, "
        "mức phí và thời hạn phải hỏi trực tiếp bộ phận một cửa."
    )


# ---------------------------------------------------------------- Gói 1
def dung_ks(thu_muc):
    d = Dung()
    ten = D["du_an"]["ten"]
    d.title("BẢNG QUY TRÌNH THỰC HIỆN HỢP ĐỒNG TƯ VẤN")
    d.title("Gói thầu số 1: Tư vấn khảo sát xây dựng, lập Báo cáo kinh tế - kỹ thuật")
    d.para("Áp dụng cho hợp đồng tư vấn thuộc Dự án “" + ten + "”. Bảng tách từ “Quy trình thực hiện dự án nhóm C” (bản nền ngày 28/10/2026), giữ ký hiệu và số bước nền để truy vết (ghi “Nền n” ở cột Ghi chú), bổ sung đối chiếu pháp luật hiện hành và văn bản của tỉnh Quảng Ngãi đến ngày 28/10/2026.")
    d.para("Đây là dự thảo hướng dẫn, không thay hợp đồng, quyết định đầu tư hoặc văn bản của cấp có thẩm quyền. Tài liệu chưa thực hiện rà soát theo KTC-Ra-Soat-897; chưa xác thực chữ ký số của các văn bản đã ký.")
    d.heading("PHẦN 1. THÔNG TIN GÓI THẦU")
    nhansu = "; ".join(f"{a}: {b}" for a, b in KS["nhansu"])
    hang = [
        ("Gói thầu", KS["ten"] + ". Hình thức: Chỉ định thầu rút gọn theo kế hoạch lựa chọn nhà thầu tại QĐ " + D["van_ban"]["qd_2236"]["so"] + " ngày " + D["van_ban"]["qd_2236"]["ngay"] + "."),
        ("Quyết định kết quả", "QĐ " + D["van_ban"]["qd_2374"]["so"] + " ngày " + D["van_ban"]["qd_2374"]["ngay"] + " (đăng tải theo bản thông tin kết quả trên Hệ thống mạng đấu thầu quốc gia)."),
        ("Nhà thầu", KS["nt"] + "; mã số thuế " + KS["mst"] + "; " + KS["dc"] + "; đại diện " + KS["dd"] + "."),
        ("Giá và thời gian", "{} đồng (bằng chữ: {}); {}. Gồm khảo sát xây dựng {} đồng và lập BCKTKT (kể cả thiết kế bản vẽ thi công) {} đồng.".format(
            KS["gia"], KS["chu"], KS["tgian_dai"], *re.findall(r"\d{1,3}(?:\.\d{3})+", KS["pt_tom_tat"])[:2])),
        ("Nhân sự chủ chốt theo hồ sơ năng lực", nhansu),
        ("Điều kiện đã ghi trong hồ sơ", " ".join(KS["luu_y"])),
        ("Hồ sơ hợp đồng hiện có", "Dự thảo hợp đồng tư vấn xây dựng và dự thảo thương thảo hợp đồng (mẫu chưa điền, chưa phải bản ký). Chưa có hợp đồng đã ký."),
        ("Mã đơn vị trong bảng", "P-THHC — Phòng Tổng hợp - Hành chính và Quản trị; P-TCKT — Phòng Tài chính - Kế toán; KBNN — Kho bạc Nhà nước."),
    ]
    d.bang(["Chỉ tiêu", "Nội dung"], [5.4, 19.3], hang)
    phan_von(d)
    d.heading("2.2. Tiến độ đề xuất trong 120 ngày")
    d.para("Tiến độ dưới đây do người lập đề xuất để chốt khi thương thảo, không phải mốc hợp đồng. T0 là ngày hợp đồng có hiệu lực.")
    d.bang(["Mốc", "Thời điểm đề xuất", "Điều kiện và ghi chú"], [9.0, 5.7, 10.0], [
        ("Hợp đồng có hiệu lực", "T0", "Chốt ngày hiệu lực và điều kiện hiệu lực trong hợp đồng."),
        ("Nhiệm vụ và phương án kỹ thuật khảo sát được duyệt", "T0 + 07 ngày", "Bước 9–10; CĐT duyệt nhiệm vụ trước khi nhà thầu lập phương án."),
        ("Khảo sát hiện trường", "T0 + 08 đến T0 + 35 ngày", "Bước 11; tránh giờ nghỉ và hoạt động của người học."),
        ("Nghiệm thu, phê duyệt báo cáo kết quả khảo sát", "T0 + 40 ngày", "Bước 12; làm căn cứ thanh toán đợt khảo sát."),
        ("Hoàn thành BCKTKT và thủ tục kèm theo", "T0 + 85 ngày", "Bước 14–16; gồm thẩm định nội bộ của CĐT."),
        ("Nộp hồ sơ trình thẩm định", "T0 + 90 ngày", "Bước 17; hồ sơ phải đủ điều kiện để cơ quan chủ trì tiếp nhận."),
        ("Thẩm định, giải trình, hoàn chỉnh hồ sơ", "T0 + 90 đến T0 + 120 ngày", "Bước 17–18; phụ thuộc cơ quan thẩm định; phải chốt 120 ngày có tính thời gian thẩm định hay không."),
        ("Phê duyệt dự án", "Sau T0 + 120 ngày", "Bước 19; do người quyết định đầu tư, ngoài tiến độ hợp đồng."),
    ])
    d.heading("PHẦN 3. BẢNG QUY TRÌNH 8 CỘT")
    d.para("Ký hiệu: C — chủ trì; P — phối hợp; T — thẩm tra/thẩm định; D — quyết định/phê duyệt; – — không trực tiếp tham gia. Cột “Nhà thầu tư vấn” là Công ty TNHH XD DV & TM Trường Phát Land (bên nhận thầu của gói này); cột “Tư vấn khác” là các tư vấn còn lại của dự án, gồm Công ty cổ phần Thành Vinh (tư vấn QLDA). Cột Chủ đầu tư áp dụng khi Trường có tư cách được giao; trước đó Trường thực hiện phần việc của cơ quan chuẩn bị dự án, không tự nhận quyền của người quyết định đầu tư. “Nền n” là số bước của bản nền.")
    d.bang_quy_trinh(N.KS_PHA, N.KS_DONG)
    nguon_dia_phuong(d, "KS")
    d.heading("PHẦN 5. CHECKLIST HỒ SƠ LƯU TRỮ CỦA HỢP ĐỒNG")
    for h, t in [
        ("01. Kết quả lựa chọn nhà thầu và hợp đồng", "QĐ 2374 và ảnh chụp Hệ thống có dấu thời gian; đơn xin nhận thầu, hồ sơ năng lực, chứng chỉ nhân sự; biên bản đối chiếu tài liệu (Phụ lục 4A TT 79/2025/TT-BTC); biên bản thương thảo (Phụ lục 4C); hợp đồng đã ký và phụ lục; thông báo ngày hiệu lực; Bảng thông tin hợp đồng Mẫu 02.a/TT. Tách bản dự thảo khỏi bản chính."),
        ("02. Vốn và thanh toán", "Kế hoạch vốn năm, quyết định giao nhiệm vụ; giấy đề nghị thanh toán vốn Mẫu 04.a/TT, giấy rút vốn 05.a/TT, đề nghị thu hồi tạm ứng 04.b/TT, bảng xác định giá trị khối lượng 03.a/TT; biên bản nghiệm thu từng giai đoạn; chứng từ Kho bạc; bảng theo dõi tạm ứng và thu hồi."),
        ("03. Khảo sát", "Nhiệm vụ khảo sát đã duyệt; phương án kỹ thuật; nhật ký, số liệu gốc, ảnh, kết quả thí nghiệm; biên bản nghiệm thu khối lượng; báo cáo kết quả khảo sát được phê duyệt."),
        ("04. BCKTKT", "Nhiệm vụ thiết kế; thuyết minh; hồ sơ thiết kế bản vẽ thi công; dự toán và tổng mức đầu tư; danh mục quy chuẩn, tiêu chuẩn; danh mục, cấu hình, báo giá thiết bị; phiếu xác định thủ tục quy hoạch, PCCC, môi trường, giấy phép; báo cáo thẩm tra (nếu có); kết quả thẩm định của CĐT."),
        ("05. Thẩm định và phê duyệt", "Tờ trình thẩm định; hồ sơ trình; văn bản yêu cầu bổ sung; thông báo kết quả thẩm định; báo cáo giải trình, hồ sơ chỉnh sửa; quyết định phê duyệt dự án; hồ sơ thiết kế đã đóng dấu phê duyệt; bản chụp PDF nộp lại cơ quan thẩm định."),
        ("06. Quyết toán và thanh lý hợp đồng", "Biên bản nghiệm thu hoàn thành; bảng quyết toán A - B; biên bản thanh lý; biên bản bàn giao hồ sơ, dữ liệu; sổ mốc hạn và lịch sử thay đổi."),
    ]:
        d.heading(h)
        d.para("☐ " + t)
    d.heading("PHẦN 6. RỦI RO VÀ ĐIỂM KIỂM SOÁT")
    for i, (h, t) in enumerate([
        ("Hợp đồng dùng căn cứ và mẫu cũ", "Dự thảo hiện có viện dẫn văn bản đã hết hiệu lực hoặc bị thay thế. Ký như vậy làm hợp đồng thiếu cơ sở và khó thanh toán, quyết toán. Sửa theo bước 2 trước khi ký."),
        ("Tạm ứng năm 2026 đã dùng hết vốn", "Tổng tạm ứng hai hợp đồng năm 2026 đúng bằng 260.000.000 đồng (gói khảo sát, lập BCKTKT 145.817.169 đồng; gói QLDA 114.182.831 đồng); không còn dư địa cho chi phí chuẩn bị đầu tư khác trong năm 2026 (thẩm định, lệ phí, thẩm tra). Kiểm tra với P-TCKT trước khi tạm ứng (Phần 2)."),
        ("Nhầm người quyết định đầu tư và cơ quan thẩm định", "Chưa có quyết định đầu tư. Điều 31.3 NĐ 217 để người quyết định đầu tư giao cơ quan chủ trì thẩm định; QĐ 32/2025 của tỉnh dựa trên nghị định đã hết hiệu lực. Không nhầm với thẩm định báo cáo nghiên cứu khả thi (Điều 36–37) và không dùng QĐ 148/2026/QĐ-CTUBND dành cho dự án không có cấu phần xây dựng."),
        ("Thiếu thiết bị trong BCKTKT", "Dự án có 02 mô hình xe ô tô con số tự động. Nếu hợp đồng không giao lập danh mục, cấu hình, giá thiết bị thì BCKTKT thiếu chi phí thiết bị, tổng mức sai. Chốt ở bước 4 và 13."),
        ("120 ngày không kiểm soát được", "Thời gian thẩm định, giải trình thuộc cơ quan nhà nước. Nếu hợp đồng tính cả thẩm định vào 120 ngày thì nhà thầu có thể bị phạt chậm do việc ngoài tầm kiểm soát. Ghi rõ trong hợp đồng."),
        ("Nhân sự chủ chốt và chứng chỉ", "Chứng chỉ sớm nhất hết hạn 08/7/2027. Thay nhân sự phải được CĐT chấp thuận bằng văn bản và bảo đảm điều kiện tương đương. Một nhà thầu làm cả khảo sát và thiết kế nên cần kiểm tra độc lập báo cáo khảo sát."),
        ("Khảo sát tại ký túc xá đang hoạt động", "Phải có phương án an toàn điện, khu vực cách ly, giờ làm việc và người phụ trách của đơn vị quản lý ký túc xá. Dừng việc khi thiếu điều kiện an toàn."),
        ("Không đủ vốn thanh toán đợt cuối", "Sản phẩm hoàn thành khoảng tháng 3/2027 nếu hợp đồng hiệu lực trong tháng 11/2026, trong khi vốn đã giao chỉ 260.000.000 đồng cho năm 2026. Không nghiệm thu thanh toán vượt kế hoạch vốn; đề nghị vốn năm 2027 đúng hạn."),
    ], 1):
        d.para(f"{i}. {h}: {t}")
    ket_thuc(d, "KS")
    out = os.path.join(thu_muc, "QT_Goi-KS-BCKTKT_Truong-Phat-Land_20261028_v2.docx")
    d.luu(out, "Bảng quy trình hợp đồng tư vấn khảo sát xây dựng, lập BCKTKT — Dự án CLC 2026-2030")
    return out


# ---------------------------------------------------------------- Gói 2
def dung_ql(thu_muc):
    d = Dung()
    ten = D["du_an"]["ten"]
    d.title("BẢNG QUY TRÌNH THỰC HIỆN HỢP ĐỒNG TƯ VẤN")
    d.title("Gói thầu số 2: Tư vấn quản lý dự án")
    d.para("Áp dụng cho hợp đồng tư vấn thuộc Dự án “" + ten + "”. Bảng tách từ “Quy trình thực hiện dự án nhóm C” (bản nền ngày 28/10/2026), giữ ký hiệu và số bước nền để truy vết (ghi “Nền n” ở cột Ghi chú), bổ sung đối chiếu pháp luật hiện hành và văn bản của tỉnh Quảng Ngãi đến ngày 28/10/2026.")
    d.para("Đây là dự thảo hướng dẫn, không thay hợp đồng, quyết định đầu tư hoặc văn bản của cấp có thẩm quyền. Tài liệu chưa thực hiện rà soát theo KTC-Ra-Soat-897; chưa xác thực chữ ký số của các văn bản đã ký.")
    d.heading("PHẦN 1. THÔNG TIN GÓI THẦU")
    nhansu = "; ".join(f"{a}: {b}" for a, b in QL["nhansu"])
    hang = [
        ("Gói thầu", QL["ten"] + ". Hình thức: Chỉ định thầu rút gọn theo kế hoạch lựa chọn nhà thầu tại QĐ " + D["van_ban"]["qd_2236"]["so"] + " ngày " + D["van_ban"]["qd_2236"]["ngay"] + "."),
        ("Quyết định kết quả", "QĐ " + D["van_ban"]["qd_2375"]["so"] + " ngày " + D["van_ban"]["qd_2375"]["ngay"] + " (đăng tải theo bản thông tin kết quả trên Hệ thống mạng đấu thầu quốc gia)."),
        ("Nhà thầu", QL["nt"] + "; mã số thuế " + QL["mst"] + "; " + QL["dc"] + "; đại diện " + QL["dd"] + "."),
        ("Giá và thời hạn", f"{QL['gia']} đồng (bằng chữ: {QL['chu']}); {QL['tgian_dai']}."),
        ("Nhân sự theo hồ sơ năng lực", nhansu),
        ("Điều kiện đã ghi trong hồ sơ", " ".join(QL["luu_y"])),
        ("Hồ sơ hợp đồng hiện có", "Dự thảo hợp đồng tư vấn quản lý dự án ngày 19/10/2026 (tệp .doc, chưa phải bản ký). Chưa có hợp đồng đã ký."),
        ("Mã đơn vị trong bảng", "P-THHC — Phòng Tổng hợp - Hành chính và Quản trị; P-TCKT — Phòng Tài chính - Kế toán; KBNN — Kho bạc Nhà nước."),
    ]
    d.bang(["Chỉ tiêu", "Nội dung"], [5.4, 19.3], hang)
    phan_von(d)
    d.heading("2.2. Khoảng trống của dự thảo hợp đồng ngày 19/10/2026")
    for i, t in enumerate([
        "Căn cứ pháp lý còn Luật Xây dựng 2014, NĐ 06/2021, NĐ 175/2024, TT 11/2021 và 12/2021 của Bộ Xây dựng; NĐ 24/2024, NĐ 17/2025, NĐ 349 và TT 22/2024/TT-BKHĐT viện dẫn riêng lẻ thay vì NĐ 214 đã sửa đổi (VBHN 36/2026/VBHN-NĐ-BTC) và TT 79/2025/TT-BTC.",
        "Điều 9 chỉ liệt kê nhiệm vụ của giai đoạn thực hiện (lựa chọn nhà thầu, khởi công, quản lý hợp đồng, nghiệm thu, quyết toán), không có nhiệm vụ cho giai đoạn chuẩn bị đầu tư dù hợp đồng thực hiện “từ giai đoạn chuẩn bị đầu tư”.",
        "Điều 7 ghi tạm ứng 30% (200.229.906 đồng) ngay sau ký, chưa tính khả năng cân đối vốn năm 2026; Điều 8 chưa chia giai đoạn thanh toán theo tỷ lệ giá hợp đồng.",
        "Điều 6 ghi giá hợp đồng “sẽ được chuẩn xác sau khi dự toán được phê duyệt”, trái với hợp đồng trọn gói theo giá trúng thầu của QĐ 2375.",
        "Điều 3 ghi thời gian “đến khi công trình hoàn thành dự án”, chưa bám thời hạn không quá 03 năm kể từ hiệu lực của QĐ 2375.",
        "Điều khoản vốn năm sau mới nêu chung “trên cơ sở kế hoạch vốn bố trí”; phải ghi thành điều kiện tạm dừng thanh toán và quyền của hai bên.",
        "Lỗi trình bày cần sửa trước khi ký: Sai dấu ở các cụm “bổ sung”, “chi tiết” trong phần căn cứ và ngày ghi “07/0/2026” ở căn cứ QĐ 2236.",
    ], 1):
        d.para(f"{i}. {t}")
    d.heading("PHẦN 3. BẢNG QUY TRÌNH 8 CỘT")
    d.para("Ký hiệu: C — chủ trì; P — phối hợp; T — thẩm tra/thẩm định; D — quyết định/phê duyệt; – — không trực tiếp tham gia. Cột “Nhà thầu tư vấn” là Công ty cổ phần Thành Vinh (bên nhận thầu của gói này); cột “Tư vấn khác” là các tư vấn và nhà thầu còn lại của dự án, gồm Trường Phát Land (khảo sát, lập BCKTKT), tư vấn giám sát và nhà thầu thi công, thiết bị khi có. Cột Chủ đầu tư áp dụng khi Trường có tư cách được giao; trước đó Trường thực hiện phần việc của cơ quan chuẩn bị dự án. “Nền n” là số bước của bản nền. Tư vấn QLDA hỗ trợ CĐT theo hợp đồng, không thay CĐT về trách nhiệm pháp lý và thẩm quyền quyết định.")
    d.bang_quy_trinh(N.QL_PHA, N.QL_DONG)
    nguon_dia_phuong(d, "QLDA")
    d.heading("PHẦN 5. CHECKLIST HỒ SƠ LƯU TRỮ CỦA HỢP ĐỒNG")
    for h, t in [
        ("01. Kết quả lựa chọn nhà thầu và hợp đồng", "QĐ 2375 và ảnh chụp Hệ thống có dấu thời gian; hồ sơ năng lực, chứng chỉ nhân sự; biên bản đối chiếu tài liệu (Phụ lục 4A TT 79/2025/TT-BTC); biên bản thương thảo (Phụ lục 4C); hợp đồng đã ký và phụ lục; thông báo hiệu lực; Bảng thông tin hợp đồng Mẫu 02.a/TT. Tách dự thảo khỏi bản chính."),
        ("02. Căn cứ hình thức quản lý dự án", "Văn bản của người quyết định đầu tư hoặc CĐT về hình thức quản lý dự án; văn bản thông báo nhiệm vụ, quyền hạn người đại diện và bộ máy của tư vấn; quy chế phối hợp."),
        ("03. Kế hoạch và báo cáo quản lý dự án", "Kế hoạch quản lý dự án; báo cáo công tác quản lý điều hành dự án theo chu kỳ; ý kiến bằng văn bản của tư vấn; báo cáo tiến độ, chất lượng, chi phí, an toàn; số liệu phục vụ báo cáo giải ngân tháng."),
        ("04. Giám sát chuẩn bị đầu tư", "Biên bản kiểm tra nhiệm vụ, phương án khảo sát; biên bản kiểm tra hiện trường; ý kiến về báo cáo khảo sát và BCKTKT; hồ sơ trình thẩm định, văn bản yêu cầu bổ sung, giải trình."),
        ("05. Giai đoạn thực hiện", "Biên bản kiểm tra điều kiện khởi công; thông báo khởi công và bằng chứng gửi; nhật ký, biên bản nghiệm thu; hồ sơ phát sinh, thay đổi thiết kế; hồ sơ nhận hàng, chạy thử, đào tạo thiết bị; hồ sơ kiểm tra nghiệm thu của cơ quan nhà nước nếu thuộc diện."),
        ("06. Vốn, quyết toán và thanh lý", "Giấy đề nghị thanh toán vốn Mẫu 04.a/TT, giấy rút vốn 05.a/TT, đề nghị thu hồi tạm ứng 04.b/TT, bảng giá trị khối lượng 03.a/TT; hồ sơ quyết toán dự án hoàn thành; bảng quyết toán A - B của hợp đồng QLDA; biên bản thanh lý; mục lục hồ sơ bàn giao."),
    ]:
        d.heading(h)
        d.para("☐ " + t)
    d.heading("PHẦN 6. RỦI RO VÀ ĐIỂM KIỂM SOÁT")
    for i, (h, t) in enumerate([
        ("Thiếu văn bản hình thức quản lý dự án", "Dự án đầu tư công mặc định dùng Ban quản lý dự án đầu tư xây dựng. Muốn thuê tư vấn thay cho Ban phải có quyết định của người quyết định đầu tư (Điều 44 NĐ 217). Thiếu văn bản này thì hợp đồng có nguy cơ bị xem là sai hình thức."),
        ("Dự thảo không phủ giai đoạn chuẩn bị đầu tư", "Hợp đồng tính từ giai đoạn chuẩn bị nhưng nhiệm vụ chỉ nêu giai đoạn thực hiện, nên tư vấn không có nghĩa vụ giám sát khảo sát, soát BCKTKT. Bổ sung theo bước 10."),
        ("Tạm ứng năm 2027 cần lập đúng hạn", "Mỗi hợp đồng còn phần tạm ứng năm 2027 để đủ 30% (gói khảo sát, lập BCKTKT 109.886.405 đồng; gói QLDA 86.047.075 đồng). Vốn năm 2027 đã được xác nhận có; lập hồ sơ tạm ứng ngay khi kế hoạch vốn được giao và theo dõi mốc trong sổ mốc hạn."),
        ("Hợp đồng ngắn hơn vòng đời dự án", "Tối đa 03 năm kể từ hiệu lực, nhưng quyết toán dự án nhóm C có thể sau khi bố trí vốn 03 năm; bảo hành còn dài hơn. Chốt phương án gia hạn hoặc ký phụ lục sớm, không để hợp đồng hết hạn khi chưa quyết toán."),
        ("Một người giữ nhiều vai trò", "Giám đốc quản lý dự án đồng thời phụ trách chi phí, rủi ro và giám sát. Kiểm tra khả năng bố trí thực tế, quy định thay người, và điều kiện của từng vai trò theo Điều 45.5 NĐ 217."),
        ("Tư vấn thay CĐT quyết định", "Tư vấn kiểm tra, đề xuất, tổng hợp. CĐT ký phê duyệt, nghiệm thu, thanh toán và chịu trách nhiệm pháp lý. Ghi rõ ranh giới trong hợp đồng và quy chế phối hợp."),
        ("Dùng quy định tỉnh đã lỗi thời", "QĐ 08/2026 và QĐ 15/2026 ban hành theo Luật Xây dựng cũ và đang có dự thảo thay thế. Hỏi cơ quan tiếp nhận trước khi nộp thông báo khởi công hoặc hồ sơ kiểm tra nghiệm thu."),
        ("Quyết toán dùng chế độ cũ", "Từ 01/7/2026 quyết toán dự án hoàn thành theo NĐ 193 và TT 73; không dùng NĐ 99/2021 hoặc Điều 30–47 NĐ 254/2025 đã bị bãi bỏ. Lịch nhóm C: 04 tháng lập, 02 tháng thẩm tra, 07 ngày phê duyệt."),
    ], 1):
        d.para(f"{i}. {h}: {t}")
    ket_thuc(d, "QLDA")
    out = os.path.join(thu_muc, "QT_Goi-QLDA_Thanh-Vinh_20261028_v2.docx")
    d.luu(out, "Bảng quy trình hợp đồng tư vấn quản lý dự án — Dự án CLC 2026-2030")
    return out


def ket_thuc(d, goi):
    d.heading("PHẦN 7. NGUỒN VÀ NỘI DUNG CẦN XÁC NHẬN")
    d.para("Chốt nghiên cứu ngày 28/10/2026 (Perplexity, Exa, cổng thông tin tỉnh Quảng Ngãi, Công báo). Kết quả tìm kiếm chỉ dùng để phát hiện nguồn; căn cứ nội dung là toàn văn chính thức. Văn bản hợp nhất phục vụ đọc, không có hiệu lực độc lập.")
    d.para("Đã đọc toàn văn trong kho KTC-Database: NĐ 210/2026, NĐ 217/2026, NĐ 206/2026, NĐ 207/2026, NĐ 212/2026, NĐ 254/2025 (Điều 7–12), Luật Đấu thầu (Điều 68). Chưa có trong kho hoặc chưa đọc toàn văn: QĐ 1040/QĐ-BXD, TT 36/2026/TT-BXD, NĐ 193/2026, TT 73/2026/TT-BTC, các văn bản của tỉnh nêu ở Phần 4 chỉ thấy tiêu đề; số liệu từ NĐ 193 và TT 73 lấy theo bản nền, cần đối chiếu khi áp dụng.")
    chung = ["210", "217", "206", "207", "212", "254", "DT", "214", "XD", "1040", "TT36", "193", "73", "QD64", "DTC"]
    for i, k in enumerate(chung, 1):
        p = d.para()
        p.add_run(f"{i}. ").bold = True
        label, url = NGUON[k]
        d.link(p, label, url)
    d.heading("Những việc cần xác nhận để áp dụng vào quyết định cụ thể")
    if goi == "KS":
        xm = "(1) Người quyết định đầu tư và cơ quan chủ trì thẩm định BCKTKT; QĐ 32/2025 còn áp dụng phần nào sau 01/7/2026; (2) hợp đồng đã ký, ngày hiệu lực, phạm vi có gồm thiết bị hay không, 120 ngày có gồm thẩm định hay không; (3) mức, thời điểm tạm ứng và nguồn vốn bổ sung; (4) tư cách CĐT hay cơ quan chuẩn bị dự án khi phê duyệt nhiệm vụ khảo sát và thiết kế; (5) thủ tục PCCC, quy hoạch, môi trường, giấy phép; (6) mã dự án và tài khoản tại Kho bạc."
    else:
        xm = "(1) Văn bản quyết định hình thức quản lý dự án; (2) hợp đồng đã ký, ngày hiệu lực, phạm vi giai đoạn chuẩn bị đầu tư; (3) mức, thời điểm tạm ứng và nguồn vốn bổ sung; (4) có giao giám sát khảo sát hay không; (5) cơ quan nhận thông báo khởi công và cơ quan kiểm tra nghiệm thu theo văn bản tỉnh hiện hành; (6) người quyết định đầu tư và người phê duyệt quyết toán; (7) thẩm quyền điều chỉnh vốn theo NQ 72/2026/NQ-HĐND."
    d.para("CAN_XAC_MINH: " + xm + " Người hoặc cơ quan có thẩm quyền xác nhận theo từng phần; tư vấn không tự quyết thay.")
    d.para("Tự kiểm: Số liệu hai gói cộng đúng dự toán chuẩn bị đầu tư; mức tạm ứng tính theo NĐ 210 và làm tròn đến đồng; bảng giữ 8 cột như bản nền. Tài liệu chưa rà soát theo KTC-Ra-Soat-897, chưa có kiểm tra hiện trường hoặc xác nhận của Kho bạc.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=ket_qua("2026-10-28", "Quy-trinh-tu-van-2-goi"))
    ap.add_argument("--goi", choices=["KS", "QLDA"])
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    if a.goi in (None, "KS"):
        print(dung_ks(a.out))
    if a.goi in (None, "QLDA"):
        print(dung_ql(a.out))
