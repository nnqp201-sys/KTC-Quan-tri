# -*- coding: utf-8 -*-
"""Lap 2 Phieu trinh ky + 2 Quyet dinh phe duyet ket qua lua chon nha thau (chi dinh thau rut gon)
cho 02 goi thau giai doan chuan bi dau tu Du an CLC 2026-2030.

Mau: Phieu trinh  -> KTC-Database 04-13 (PhieuTrinh_Bao-cao-lam-ro-kinh-phi-sua-chua-mua-sam, theo QD 1622/QD-CDKT)
     Quyet dinh   -> QD 2236/QD-CDKT (ban v9-sach da ky) - giu dung the thuc, bo phan Phu luc.
"""
import copy
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from du_an import tai, kho, onedrive_cbdt, ket_qua  # noqa: E402

KHO = kho("04-Good-Documents", "04-13- Phieu trinh",
          "PhieuTrinh_Bao-cao-lam-ro-kinh-phi-sua-chua-mua-sam_20260720_v1.docx")
QD2236 = onedrive_cbdt("LCNT Chuan-bi-dau-tu", "QD-KHLCNT-giai-doan-CBDT_Du-an-CLC-2026-2030_20261007_v9-sach.docx")
OUT = ket_qua("2026-10-26", "Soan-Thao-VB")

# --- Số liệu lấy từ du-an_CLC-2026-2030.yaml (nguồn sự thật duy nhất) ---

_D = tai()
DA = _D["du_an"]["ten"]
CTMTQG = _D["du_an"]["chuong_trinh"]
GOI = _D["goi_thau"]


# ---------------------------------------------------------------- tiện ích
def _strip(rpr):
    if rpr is None:
        return
    for tag in ("w:b", "w:bCs", "w:i", "w:iCs"):
        for e in rpr.findall(qn(tag)):
            rpr.remove(e)


def set_runs(p, parts, proto_run=None):
    """parts: [(text, bold, italic)]; giữ phông, cỡ chữ của run mẫu."""
    el = p._element if hasattr(p, "_element") else p
    runs = el.findall(qn("w:r"))
    proto = proto_run if proto_run is not None else (runs[0] if runs else None)
    proto = copy.deepcopy(proto)
    for r in el.findall(qn("w:r")) + el.findall(qn("w:ins")) + el.findall(qn("w:del")) + el.findall(qn("w:hyperlink")):
        el.remove(r)
    for t in el.findall(qn("w:proofErr")):
        el.remove(t)
    for text, b, i in parts:
        r = copy.deepcopy(proto)
        for ch in list(r):
            if ch.tag != qn("w:rPr"):
                r.remove(ch)
        rpr = r.find(qn("w:rPr"))
        _strip(rpr)
        if rpr is None:
            rpr = OxmlElement("w:rPr")
            r.insert(0, rpr)
        # w:b, w:i phải đứng trước w:sz theo schema -> chèn đầu rPr (sau rFonts nếu có)
        pos = 1 if rpr.find(qn("w:rFonts")) is not None else 0
        if i:
            rpr.insert(pos, OxmlElement("w:i"))
        if b:
            rpr.insert(pos, OxmlElement("w:b"))
        t = OxmlElement("w:t")
        t.text = text
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        r.append(t)
        el.append(r)


def clone_after(ref_el, proto_p, parts, proto_run=None):
    new = copy.deepcopy(proto_p._element if hasattr(proto_p, "_element") else proto_p)
    ref_el.addnext(new)
    set_runs(new, parts, proto_run)
    return new


def cell_set(cell, idx, text):
    """Đổi chữ nhưng GIỮ run mang hình vẽ (đường kẻ dưới tiêu ngữ/tên cơ quan)."""
    p = cell.paragraphs[idx]
    first = True
    for r in p._element.findall(qn("w:r")):
        has_draw = (r.find(".//" + qn("w:drawing")) is not None or r.find(".//" + qn("w:pict")) is not None
                    or r.find(".//{http://schemas.openxmlformats.org/markup-compatibility/2006}AlternateContent") is not None)
        ts = r.findall(qn("w:t"))
        if has_draw or not ts:
            continue
        if first:
            ts[0].text = text
            ts[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            for t in ts[1:]:
                r.remove(t)
            first = False
        else:
            p._element.remove(r)


# ===================================================================== QUYẾT ĐỊNH
def build_qd(key):
    g = GOI[key]
    d = Document(QD2236)
    body = d.element.body
    kids = list(body)
    # tìm mốc
    tbl_nn = kids[38]
    assert tbl_nn.tag == qn("w:tbl")
    sect_par = kids[40]
    sect1 = copy.deepcopy(sect_par.find(".//" + qn("w:sectPr")))
    # bỏ phụ lục
    for el in kids[39:49]:
        body.remove(el)
    final = body.find(qn("w:sectPr"))
    body.remove(final)
    body.append(sect1)

    P = d.paragraphs
    # mẫu
    p_can_cu = copy.deepcopy(P[5]._element)
    p_dieu = copy.deepcopy(P[19]._element)
    p_khoan = copy.deepcopy(P[20]._element)
    p_dieu2 = copy.deepcopy(P[28]._element)
    run_can = P[5].runs[0]._element
    run_norm = P[20].runs[0]._element
    run_bold = P[19].runs[0]._element
    # xóa từ p5 đến hết trước bảng nơi nhận
    for p in list(d.paragraphs)[5:]:
        body.remove(p._element)
    # trích yếu
    set_runs(P[2], [("phê duyệt kết quả lựa chọn nhà thầu gói thầu “" + g["ten"] + "” thuộc Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư Dự án “" + DA + "”", True, None)],
             proto_run=P[2].runs[0]._element)

    # bảng
    t0, t1 = d.tables
    cell_set(t0.rows[1].cells[0], 0, "Số:        /QĐ-CĐKT")
    cell_set(t0.rows[1].cells[1], 0, "Quảng Ngãi, ngày       tháng 10 năm 2026")
    cn = t1.rows[0].cells[0]
    cell_set(cn, 1, "- Như Điều 4;")
    newp = copy.deepcopy(cn.paragraphs[2]._element)
    cn.paragraphs[2]._element.addnext(newp)
    set_runs(cn.paragraphs[3], [("- " + g["nt_ngan"] + ";", None, None)], proto_run=cn.paragraphs[2].runs[0]._element)

    anchor = tbl_nn
    items = []

    def can_cu(t):
        items.append(("cc", [(t, None, True)]))

    can_cu("Căn cứ Quyết định số 1976/QĐ-CĐKT ngày 14/9/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum ban hành Quy chế tổ chức và hoạt động của Trường Cao đẳng Kon Tum;")
    can_cu("Căn cứ Luật Đấu thầu ngày 23/6/2023 (hợp nhất tại Văn bản hợp nhất số 74/VBHN-VPQH ngày 25/3/2026);")
    can_cu("Căn cứ Luật Đầu tư công ngày 29/11/2024 (hợp nhất tại Văn bản hợp nhất số 03/VBHN-VPQH ngày 05/2/2026);")
    can_cu("Căn cứ Nghị định số 214/2025/NĐ-CP ngày 04/8/2025 của Chính phủ quy định chi tiết một số điều và biện pháp thi hành Luật Đấu thầu về lựa chọn nhà thầu (hợp nhất tại Văn bản hợp nhất số 36/2026/VBHN-NĐ-BTC ngày 23/9/2026);")
    can_cu("Căn cứ Nghị định số 387/2026/NĐ-CP ngày 12/10/2026 của Chính phủ quy định nội dung, cơ chế, chính sách thực hiện Chương trình mục tiêu quốc gia phát triển văn hóa - xã hội, nông thôn, dân tộc và miền núi giai đoạn 2026 - 2035; Nghị định số 358/2025/NĐ-CP ngày 31/12/2025 của Chính phủ quy định cơ chế quản lý, tổ chức thực hiện các chương trình mục tiêu quốc gia (tiếp tục áp dụng theo khoản 1 Điều 53 Nghị định số 387/2026/NĐ-CP);")
    can_cu("Căn cứ Thông tư số 79/2025/TT-BTC ngày 04/8/2025 của Bộ trưởng Bộ Tài chính hướng dẫn việc cung cấp, đăng tải thông tin về đấu thầu và mẫu hồ sơ đấu thầu trên Hệ thống mạng đấu thầu quốc gia;")
    can_cu("Căn cứ Nghị quyết số 56/NQ-HĐND ngày 28/8/2026 của Hội đồng nhân dân tỉnh Quảng Ngãi về việc phân bổ kế hoạch đầu tư công và kinh phí thường xuyên năm 2026 thực hiện " + CTMTQG.replace("Từ năm", "từ năm") + " trên địa bàn tỉnh Quảng Ngãi;")
    can_cu("Căn cứ Quyết định số 805/QĐ-UBND ngày 11/9/2026 của Ủy ban nhân dân tỉnh Quảng Ngãi phân bổ kế hoạch vốn đầu tư công và kinh phí thường xuyên năm 2026 thực hiện " + CTMTQG.replace("Từ năm", "từ năm") + " trên địa bàn tỉnh Quảng Ngãi (Nguồn vốn: Ngân sách trung ương và ngân sách tỉnh);")
    can_cu("Căn cứ Quyết định số 2161/QĐ-CĐKT ngày 29/9/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum phân bổ chi tiết kế hoạch đầu tư công năm 2026 thực hiện " + CTMTQG.replace("Từ năm", "từ năm") + ";")
    can_cu("Căn cứ Quyết định số 2158/QĐ-CĐKT ngày 29/9/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum phê duyệt nhiệm vụ và dự toán kinh phí chuẩn bị đầu tư Dự án “" + DA + "”;")
    can_cu("Căn cứ Quyết định số 2236/QĐ-CĐKT ngày 07/10/2026 của Hiệu trưởng Trường Cao đẳng Kon Tum phê duyệt Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư Dự án “" + DA + "”;")
    items.append(("cc", [("Xét đề nghị của Trưởng phòng Tổng hợp - Hành chính và Quản trị tại Phiếu trình ký ngày 26/10/2026; hồ sơ đề nghị chỉ định thầu của " + g["nt"] + " (" + g["don"] + "); kết quả thương thảo, hoàn thiện hợp đồng và ý kiến của Trưởng phòng Tài chính - Kế toán.", None, True)]))
    items.append(("ct", [("QUYẾT ĐỊNH:", True, None)]))
    items.append(("d", [("Điều 1.", True, None), (" Phê duyệt kết quả lựa chọn nhà thầu của gói thầu “" + g["ten"] + "” thuộc Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư Dự án “" + DA + "”, bao gồm:", None, None)]))
    k = [
        "1. Thông tin về gói thầu:",
        "- Mã kế hoạch lựa chọn nhà thầu: PL2600341242 (Quyết định số 2236/QĐ-CĐKT ngày 07/10/2026).",
        "- Tên gói thầu: " + g["ten"] + ".",
        "- Giá gói thầu: " + g["gia"] + " đồng.",
        "- Tên chủ đầu tư: Trường Cao đẳng Kon Tum.",
        "- Hình thức lựa chọn nhà thầu: Chỉ định thầu rút gọn (khoản 4 Điều 78 và Điều 80 Nghị định số 214/2025/NĐ-CP).",
        "- Loại hợp đồng: Trọn gói.",
        "- Thời gian thực hiện gói thầu: " + g["tgian"] + ".",
        "- Nguồn vốn: Vốn đầu tư thuộc " + CTMTQG + "; cơ cấu ngân sách trung ương và ngân sách tỉnh theo kế hoạch vốn do cấp có thẩm quyền giao.",
        "2. Thông tin về nhà thầu trúng thầu:",
        "- Tên nhà thầu: " + g["nt"] + ".",
        "- Mã số thuế (mã số doanh nghiệp): " + g["mst"] + ".",
        "- Địa chỉ: " + g["dc"] + ".",
        "- Người đại diện theo pháp luật: " + g["dd"] + ".",
        "- Giá trúng thầu: " + g["gia"] + " đồng (bằng chữ: " + g["chu"] + "), không vượt giá gói thầu.",
        "- Thời gian thực hiện hợp đồng: " + g["tgian_dai"] + ".",
        "3. Thông tin về nhà thầu không trúng thầu: Không có (gói thầu chỉ định thầu rút gọn đối với một nhà thầu).",
        "4. Các nội dung cần lưu ý:",
    ]
    for t in k:
        items.append(("k", [(t, None, None)]))
    for i, t in enumerate(g["luu_y"]):
        items.append(("k", [("- " + t, None, None)]))
    items.append(("d2", [("Điều 2. Tổ chức thực hiện:", True, None)]))
    tc = [
        "1. Phòng Tổng hợp - Hành chính và Quản trị hoàn thiện, trình Hiệu trưởng ký hợp đồng với nhà thầu đúng nội dung của Quyết định này và dự thảo hợp đồng đã gửi trên Hệ thống mạng đấu thầu quốc gia; đăng tải thông tin về kết quả lựa chọn nhà thầu trên Hệ thống mạng đấu thầu quốc gia trong thời hạn 05 ngày làm việc kể từ ngày ký Quyết định này theo quy định tại khoản 5 Điều 33 Nghị định số 214/2025/NĐ-CP và khoản 2 Điều 20 Thông tư số 79/2025/TT-BTC; lập, lưu trữ hồ sơ lựa chọn nhà thầu.",
        "2. Phòng Tài chính - Kế toán kiểm soát nguồn vốn, thủ tục thanh toán, quyết toán hợp đồng trong phạm vi kế hoạch vốn do cấp có thẩm quyền giao và dự toán đã được phê duyệt.",
        "3. " + g["nt"] + " có trách nhiệm hoàn thiện, ký kết và thực hiện hợp đồng theo đúng cam kết, hồ sơ năng lực và quy định của pháp luật.",
    ]
    for t in tc:
        items.append(("k", [(t, None, None)]))
    items.append(("d2", [("Điều 3. Quyết định này có hiệu lực thi hành kể từ ngày ký.", True, None)]))
    items.append(("d2", [("Điều 4. Trưởng phòng Tổng hợp - Hành chính và Quản trị, Trưởng phòng Tài chính - Kế toán, Trưởng các đơn vị thuộc Trường, " + g["nt"] + " và các tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này./.", True, None)]))

    proto = {"cc": (p_can_cu, run_can), "ct": (P[4]._element, P[4].runs[0]._element),
             "d": (p_dieu, run_norm), "k": (p_khoan, run_norm), "d2": (p_dieu2, run_bold)}
    for typ, parts in items:
        pe, rr = proto[typ]
        new = copy.deepcopy(pe)
        anchor.addprevious(new)
        set_runs(new, parts, proto_run=rr)
    # đoạn trống trước bảng nơi nhận giữ như bản gốc
    fn = f"{OUT}/QD_Phe-duyet-KQLCNT_{g['ma']}_20261026_v1.docx"
    d.save(fn)
    return fn


# ===================================================================== PHIẾU TRÌNH
def set_borders(tbl):
    tblPr = tbl._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{side}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), "000000")
        b.append(e)
    tblPr.append(b)


def fill_cell(cell, text, bold=False, size=11, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.name = "Times New Roman"
    r._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    r.bold = bold
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.first_line_indent = Cm(0)
    if align:
        p.alignment = align


def build_pt(key):
    g = GOI[key]
    d = Document(KHO)
    t0, t1 = d.tables[0], d.tables[1]
    P = d.paragraphs
    run_norm = P[10].runs[0]._element
    run_bold = P[9].runs[0]._element
    run_it = P[7].runs[1]._element
    p_body = copy.deepcopy(P[10]._element)

    # tiêu đề + trích yếu
    set_runs(P[2], [("Quyết định phê duyệt kết quả lựa chọn nhà thầu gói thầu “" + g["ten"] + "” thuộc Dự án “" + DA + "”", True, None)],
             proto_run=P[2].runs[0]._element)
    set_runs(P[4], [("Kính gửi: Hiệu trưởng nhà trường.", None, None)], proto_run=P[4].runs[0]._element)
    set_runs(P[6], [("* Đơn vị trình: Phòng TH-HC&QT", True, None)], proto_run=run_bold)
    set_runs(P[7], [("1. Loại văn bản: ", True, None), ("Quyết định.", None, None)], proto_run=run_norm)
    set_runs(P[8], [("2. Tóm tắt nội dung trình: ", True, None),
                    ("Hiệu trưởng đã phê duyệt Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư Dự án tại Quyết định số 2236/QĐ-CĐKT ngày 07/10/2026 (mã KHLCNT PL2600341242, đã đăng tải trên Hệ thống mạng đấu thầu quốc gia). " +
                     g["pt_tom_tat"] + " Hình thức lựa chọn nhà thầu: chỉ định thầu rút gọn; giá gói thầu " + g["gia"] + " đồng; loại hợp đồng trọn gói; thời gian thực hiện " + g["tgian"].lower() + ". " +
                     "Phòng TH-HC&QT đã gửi dự thảo hợp đồng cho nhà thầu trên Hệ thống mạng đấu thầu quốc gia (" + g["dthao"] + "), nhà thầu có " + g["don"] + " và hai bên đã hoàn thiện hợp đồng ngày 22/10/2026. " +
                     "Để có cơ sở ký kết hợp đồng, Phòng TH-HC&QT trình Hiệu trưởng ký Quyết định phê duyệt kết quả lựa chọn nhà thầu: " + g["nt"] + " (mã số doanh nghiệp " + g["mst"] + "), giá trúng thầu " + g["gia"] + " đồng (bằng giá gói thầu).", None, None)],
             proto_run=run_norm)
    set_runs(P[9], [("3. Ý kiến/Đề xuất của đơn vị trình:", True, None)], proto_run=run_bold)

    # xóa P[10], P[11] để dựng lại
    anchor = P[9]._element
    for p in (P[10], P[11]):
        p._element.getparent().remove(p._element)

    seq = []

    def add(parts, proto=p_body):
        seq.append(("p", parts))

    add([("a) Căn cứ pháp lý, thẩm quyền và hồ sơ trình: ", True, None),
         ("Gói thầu áp dụng chỉ định thầu rút gọn theo khoản 4 Điều 78 và Điều 80 Nghị định số 214/2025/NĐ-CP (hợp nhất tại Văn bản hợp nhất số 36/2026/VBHN-NĐ-BTC); Hiệu trưởng là người đứng đầu đơn vị được giao nhiệm vụ chuẩn bị dự án có thẩm quyền phê duyệt (điểm a khoản 1 Điều 38, khoản 2 Điều 40 Luật Đấu thầu). Văn bản phê duyệt kết quả có đủ nội dung theo khoản 3 Điều 33 Nghị định số 214/2025/NĐ-CP (tên nhà thầu, giá trúng thầu, loại hợp đồng, thời gian thực hiện, nội dung cần lưu ý) và được xây dựng theo cấu trúc Phụ lục 5 Thông tư số 79/2025/TT-BTC (Thông tư chưa ban hành mẫu riêng cho chỉ định thầu rút gọn); đăng tải kết quả trong 05 ngày làm việc kể từ ngày phê duyệt (khoản 2 Điều 20 Thông tư số 79/2025/TT-BTC). Điều 80 không quy định lập hồ sơ yêu cầu, tổ chuyên gia đánh giá đối với chỉ định thầu rút gọn; hồ sơ trình gồm Đơn xin nhận thầu, hồ sơ pháp nhân và năng lực, dự thảo hợp đồng và kết quả hoàn thiện hợp đồng, dự thảo Quyết định.", None, None)])
    add([("b) Mức độ đáp ứng yêu cầu và điều kiện phê duyệt: ", True, None),
         ("Kết quả đối chiếu hồ sơ của nhà thầu với quy định như sau (bảng dưới đây):", None, None)])
    seq.append(("table", None))

    add([("c) Về mức tiết kiệm 5% giá gói thầu: ", True, None),
         ("Không thực hiện giảm giá 5% do gói thầu không thuộc đối tượng phải giảm giá. Theo điểm b khoản 3 Điều 80 Nghị định số 214/2025/NĐ-CP, mức tiết kiệm tối thiểu 5% giá gói thầu chỉ áp dụng đối với gói thầu xây lắp chỉ định thầu theo điểm e khoản 2 Điều 78; gói thầu này là gói tư vấn thuộc khoản 4 Điều 78. Cục Quản lý đấu thầu (Bộ Tài chính) đã hướng dẫn nội dung này tại Công văn số 2845/QLĐT-ĐT ngày 19/12/2025 gửi Sở Tài chính tỉnh Quảng Ngãi và Sở Tài chính chuyển các đơn vị tại Công văn số 5387/STC-ĐTĐT ngày 24/12/2025; Bộ Tài chính nhắc lại tại Công văn số 3306/BTC-QLĐT ngày 19/3/2026 và Công văn số 5557/BTC-QLĐT ngày 05/5/2026. Đối với các trường hợp chỉ định thầu khác, chủ đầu tư và nhà thầu thương thảo giá bảo đảm tiết kiệm, hiệu quả; nội dung này đã được thực hiện: dự toán gói thầu được lập theo nhiệm vụ, định mức đã duyệt tại Quyết định số 2158/QĐ-CĐKT, nội dung công việc và khối lượng trong dự thảo hợp đồng bám sát dự toán, hai bên thống nhất giá hợp đồng bằng giá gói thầu, không vượt giá gói thầu và không có khoản chi phí nâng khống.", None, None)])
    add([("d) Đề xuất: ", True, None),
         ("Từ những cơ sở, yêu cầu nêu trên, Phòng TH-HC&QT kính trình Hiệu trưởng nhà trường xem xét, ký Quyết định phê duyệt kết quả lựa chọn nhà thầu gói thầu “" + g["ten"] + "” để Trường ký kết hợp đồng, đăng tải kết quả lựa chọn nhà thầu trên Hệ thống mạng đấu thầu quốc gia và triển khai thực hiện./.", None, None)])

    # bảng mức độ đáp ứng
    rows = [
        ("Nội dung kiểm tra (căn cứ)", "Hồ sơ, kết quả kiểm tra", "Đánh giá"),
        ("1. Hình thức chỉ định thầu rút gọn (khoản 4 Điều 78, khoản 2 Điều 80 Nghị định số 214/2025/NĐ-CP)",
         "Gói thầu dịch vụ tư vấn thuộc dự án, giá gói thầu " + g["gia"] + " đồng, không quá 03 tỷ đồng; đã nêu trong Kế hoạch lựa chọn nhà thầu (Quyết định số 2236/QĐ-CĐKT).", "Đáp ứng"),
        ("2. Điều kiện khoản 2 Điều 79 (áp dụng theo khoản 2 Điều 80): a) có Kế hoạch lựa chọn nhà thầu được phê duyệt",
         "Quyết định số 2236/QĐ-CĐKT ngày 07/10/2026; đã đăng tải trên Hệ thống mạng đấu thầu quốc gia (mã PL2600341242).", "Đáp ứng"),
        ("b) Có kế hoạch bố trí vốn để thực hiện gói thầu",
         "Kế hoạch vốn đầu tư công năm 2026: 260 triệu đồng (ngân sách trung ương 200 triệu đồng, ngân sách tỉnh 60 triệu đồng) theo Quyết định số 805/QĐ-UBND ngày 11/9/2026 và Quyết định số 2161/QĐ-CĐKT ngày 29/9/2026. Phần còn lại của hợp đồng thanh toán theo kế hoạch vốn các năm tiếp theo do cấp có thẩm quyền giao; hợp đồng ghi rõ thanh toán trong phạm vi vốn được giao.", "Đáp ứng (lưu ý phạm vi vốn)"),
        ("c) Có dự toán gói thầu được phê duyệt",
         "Dự toán kinh phí chuẩn bị đầu tư " + "1.519.778.268 đồng đã được phê duyệt tại Quyết định số 2158/QĐ-CĐKT ngày 29/9/2026; giá gói thầu " + g["gia"] + " đồng nằm trong dự toán và Kế hoạch lựa chọn nhà thầu.", "Đáp ứng"),
        ("3. Tư cách hợp lệ của nhà thầu (các điểm a, b, c, d, e, g, i khoản 1 Điều 5 Luật Đấu thầu theo điểm a khoản 3 Điều 80)",
         g["nt"] + ": " + g["gcn"] + "; hoạt động theo pháp luật Việt Nam, hạch toán tài chính độc lập; có tên trên Hệ thống mạng đấu thầu quốc gia (đã xác minh); không thuộc trường hợp giải thể, thu hồi giấy chứng nhận đăng ký doanh nghiệp, mất khả năng thanh toán, đang bị cấm tham dự thầu hoặc bị truy cứu trách nhiệm hình sự (theo kết quả tra cứu của Phòng). Người đại diện theo pháp luật: " + g["dd"] + ".", "Đáp ứng"),
    ]
    for lbl, txt in g["nhansu"]:
        rows.append(("4. Nhân sự, năng lực: " + lbl if lbl == g["nhansu"][0][0] else lbl, txt, "Đáp ứng"))
    rows += [
        ("5. Đề nghị của nhà thầu và dự thảo hợp đồng",
         g["don"] + ", nội dung (giá gói thầu, thời gian thực hiện) khớp Kế hoạch lựa chọn nhà thầu. Dự thảo hợp đồng gửi trên Hệ thống mạng đấu thầu quốc gia (" + g["dthao"] + "); hoàn thiện hợp đồng ngày 22/10/2026 (khoản 3 Điều 80); " + g["kn"], "Đáp ứng"),
        ("6. Giá trúng thầu",
         "Bằng giá gói thầu: " + g["gia"] + " đồng; loại hợp đồng trọn gói; không vượt giá gói thầu; không áp dụng giảm giá 5% (xem điểm c).", "Đáp ứng"),
    ]

    # chèn
    prev = anchor
    tbl_el = None
    for typ, parts in seq:
        if typ == "p":
            new = copy.deepcopy(p_body)
            prev.addnext(new)
            set_runs(new, parts, proto_run=run_norm)
            prev = new
        else:
            t = d.add_table(rows=len(rows), cols=3)
            set_borders(t)
            t.autofit = False
            widths = [Cm(4.6), Cm(9.2), Cm(2.2)]
            for ri, row in enumerate(rows):
                for ci, txt in enumerate(row):
                    c = t.rows[ri].cells[ci]
                    c.width = widths[ci]
                    fill_cell(c, txt, bold=(ri == 0), align=WD_ALIGN_PARAGRAPH.CENTER if (ri == 0 or ci == 2) else WD_ALIGN_PARAGRAPH.JUSTIFY)
            prev.addnext(t._tbl)
            prev = t._tbl
            sp = copy.deepcopy(p_body)
            prev.addnext(sp)
            set_runs(sp, [("", None, None)], proto_run=run_norm)
            prev = sp

    # bảng chữ ký
    # ngày đề
    cell_dt = t0.rows[1].cells[1]
    set_runs(cell_dt.paragraphs[0], [("Quảng Ngãi, ngày 26 tháng 10 năm 2026", None, True)], proto_run=cell_dt.paragraphs[0].runs[0]._element)
    # ý kiến lãnh đạo đơn vị: giữ lời trình; ngày
    c = t1.rows[0].cells[1]
    set_runs(c.paragraphs[1], [("Ngày 26/10/2026", None, True)], proto_run=c.paragraphs[1].runs[0]._element)
    for r in (1, 2):  # TC-KT, Hiệu trưởng: để trống để người có thẩm quyền ghi ý kiến, ngày
        cc = t1.rows[r].cells[1]
        set_runs(cc.paragraphs[0], [("Ngày       /      /2026", None, True)], proto_run=cc.paragraphs[0].runs[0]._element)
    for tr in t1.rows:
        trpr = tr._tr.get_or_add_trPr()
        if trpr.find(qn("w:cantSplit")) is None:
            trpr.insert(0, OxmlElement("w:cantSplit"))
        for c in tr.cells:
            for pp in c.paragraphs:
                pp.paragraph_format.keep_with_next = True
    for pp in d.paragraphs:
        if pp.text.startswith("d) Đề xuất"):
            pp.paragraph_format.keep_with_next = True
    fn = f"{OUT}/PT_Trinh-ky-QD-phe-duyet-KQLCNT_{g['ma']}_20261026_v1.docx"
    d.save(fn)
    return fn


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Dựng Phiếu trình + QĐ phê duyệt KQLCNT từ du-an_*.yaml")
    ap.add_argument("--out", default=OUT, help="thư mục xuất (mặc định 30-Ket-Qua/2026-10-26/Soan-Thao-VB)")
    ap.add_argument("--goi", default="all", help="KS | QLDA | all")
    ap.add_argument("--chi", default="all", choices=["all", "pt", "qd"], help="chỉ dựng Phiếu trình hoặc Quyết định")
    a = ap.parse_args()
    OUT = a.out
    os.makedirs(OUT, exist_ok=True)
    for k in (list(GOI) if a.goi == "all" else [a.goi]):
        if a.chi in ("all", "pt"):
            print(build_pt(k))
        if a.chi in ("all", "qd"):
            print(build_qd(k))
