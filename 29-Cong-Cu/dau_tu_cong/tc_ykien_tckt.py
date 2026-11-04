# -*- coding: utf-8 -*-
"""Hoàn thiện hợp đồng theo ý kiến Track Changes và Comment của phòng TC-KT (chị Phạm Thị Thoa, 03/11/2026).

Xuất phát từ CHÍNH tệp chị Thoa đã sửa (giữ nguyên dấu vết và comment của chị), chỉ thêm dấu vết riêng của mình
(author "Hoàn thiện theo ý kiến phòng TC-KT (Claude)"). Việc chuyển dòng/section/hình vẽ không có dấu vết được trong Word thì làm trực tiếp.

Các việc:
 1. Sửa tham chiếu sai ở khoản 3.1.4 ("Điều 11 và Điều 11" → "Điều 11 và Điều 12") — ở Phần 3 và ở bản sao trong Phần 4.
 2. Viết lại khoản 2.1 (Phần 3) và điền khoản 2.1 (Phần 4) đúng các loại Hồ sơ của hợp đồng này (comment "Viết lại đúng các loại Hồ sơ", "Lấy ở Phần 3 copy vào nội dung này").
 3. Phụ lục theo NĐ 30 và quy tắc của Hệ: "Phụ lục I…V" (La Mã, chữ P hoa), tiêu đề in hoa, dòng "CỦA TRƯỜNG CAO ĐẲNG KON TUM", đường kẻ dưới tiêu đề,
    mỗi phụ lục một section, số trang từ 1 hiện ở trang đầu (phụ lục 1 trang không đánh số).
 4. Cập nhật số trang ghi ở Điều 20 (comment "Sửa lại sau khi hoàn thiện").
"""
import copy
import datetime
import re
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

AU = "Hoàn thiện theo ý kiến phòng TC-KT (Claude)"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
LA_MA = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V"}
_id = [90000]


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _nid():
    _id[0] += 1
    return str(_id[0])


def _stamp(e, author=AU):
    e.set(qn("w:id"), _nid())
    e.set(qn("w:author"), author)
    e.set(qn("w:date"), _now())
    return e


def _el(tag):
    return OxmlElement(tag)


def run_text(r):
    return "".join(t.text or "" for t in r.findall(qn("w:t")))


def _cua_toi(e):
    """Run nằm trong <w:ins> do chính mình chèn (không xử lý lại)."""
    a = e.getparent()
    while a is not None:
        if a.tag == qn("w:ins") and a.get(qn("w:author")) == AU:
            return True
        a = a.getparent()
    return False


def _chi_chu(r):
    return all(ch.tag in (qn("w:rPr"), qn("w:t"), qn("w:lastRenderedPageBreak")) for ch in r)


def _trong_del(e):
    a = e.getparent()
    while a is not None:
        if a.tag == qn("w:del"):
            return True
        a = a.getparent()
    return False


def _run_moi(r, text):
    n = copy.deepcopy(r)
    for ch in list(n):
        if ch.tag != qn("w:rPr"):
            n.remove(ch)
    t = _el("w:t")
    t.text = text
    t.set(XML_SPACE, "preserve")
    n.append(t)
    return n


def _sang_deltext(r):
    for t in r.findall(qn("w:t")):
        t.tag = qn("w:delText")
        t.set(XML_SPACE, "preserve")


def thay_p(p, pattern, repl):
    """Thay chữ có dấu vết trong đoạn p (kể cả chữ nằm trong <w:ins> của người khác). Trả số lần thay."""
    n = 0
    while True:
        found = None
        for r in p.iter(qn("w:r")):
            if _trong_del(r) or _cua_toi(r) or not _chi_chu(r):
                continue
            m = re.search(pattern, run_text(r))
            if m:
                found = (r, m)
                break
        if not found:
            return n
        r, m = found
        txt = run_text(r)
        pre, old, post = txt[:m.start()], m.group(0), txt[m.end():]
        new = repl(m) if callable(repl) else m.expand(repl)
        d = _stamp(_el("w:del"))
        ro = _run_moi(r, old)
        _sang_deltext(ro)
        d.append(ro)
        seq_mid = [d]
        if new:
            i_ = _stamp(_el("w:ins"))
            i_.append(_run_moi(r, new))
            seq_mid.append(i_)
        parent = r.getparent()
        if parent.tag == qn("w:ins"):
            kids = list(parent)
            k = kids.index(r)
            truoc, sau = kids[:k], kids[k + 1:]
            grand = parent.getparent()
            pos = grand.index(parent)
            seq = []

            def ins_copy(children):
                c = _el("w:ins")
                for key, val in parent.attrib.items():
                    c.set(key, val)
                c.set(qn("w:id"), _nid())
                for ch in children:
                    c.append(ch)
                return c
            truoc_all = truoc + ([_run_moi(r, pre)] if pre else [])
            if truoc_all:
                seq.append(ins_copy(truoc_all))
            wrap = ins_copy([seq_mid[0]])  # xóa chữ do người khác chèn: <w:ins><w:del>…
            seq.append(wrap)
            seq += seq_mid[1:]
            sau_all = ([_run_moi(r, post)] if post else []) + sau
            if sau_all:
                seq.append(ins_copy(sau_all))
            grand.remove(parent)
            for j, e in enumerate(seq):
                grand.insert(pos + j, e)
        else:
            pos = parent.index(r)
            seq = ([_run_moi(r, pre)] if pre else []) + seq_mid + ([_run_moi(r, post)] if post else [])
            parent.remove(r)
            for j, e in enumerate(seq):
                parent.insert(pos + j, e)
        n += 1


def xoa_doan(p):
    """Xóa cả đoạn (có dấu vết): từng run và dấu đoạn."""
    for r in list(p.iter(qn("w:r"))):
        if _trong_del(r) or _cua_toi(r) or not _chi_chu(r):
            continue
        _sang_deltext(r)
        parent = r.getparent()
        d = _stamp(_el("w:del"))
        pos = parent.index(r)
        parent.remove(r)
        d.append(r)
        parent.insert(pos, d)
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        ppr = _el("w:pPr")
        p.insert(0, ppr)
    rpr = ppr.find(qn("w:rPr"))
    if rpr is None:
        rpr = _el("w:rPr")
        ppr.append(rpr)
    rpr.insert(0, _stamp(_el("w:del")))


def chen_doan_sau(p_ref, text, bold=None, giua=False):
    """Chèn một đoạn mới (có dấu vết) ngay sau p_ref, mượn định dạng của p_ref. Trả phần tử đoạn mới."""
    n = copy.deepcopy(p_ref)
    for ch in list(n):
        if ch.tag != qn("w:pPr"):
            n.remove(ch)
    ppr = n.find(qn("w:pPr"))
    if ppr is None:
        ppr = _el("w:pPr")
        n.insert(0, ppr)
    for s in ppr.findall(qn("w:sectPr")):
        ppr.remove(s)
    rpr = ppr.find(qn("w:rPr"))
    if rpr is None:
        rpr = _el("w:rPr")
        ppr.append(rpr)
    for e in rpr.findall(qn("w:ins")) + rpr.findall(qn("w:del")):
        rpr.remove(e)
    rpr.insert(0, _stamp(_el("w:ins")))
    mau = next((r for r in p_ref.iter(qn("w:r")) if _chi_chu(r)), None)
    i_ = _stamp(_el("w:ins"))
    r = _run_moi(mau, text) if mau is not None else None
    if r is None:
        r = _el("w:r")
        t = _el("w:t")
        t.text = text
        t.set(XML_SPACE, "preserve")
        r.append(t)
    if bold is not None:
        rp = r.find(qn("w:rPr"))
        if rp is None:
            rp = _el("w:rPr")
            r.insert(0, rp)
        for b in rp.findall(qn("w:b")):
            rp.remove(b)
        if bold:
            rp.insert(0, _el("w:b"))
    if giua:
        for jc in ppr.findall(qn("w:jc")):
            ppr.remove(jc)
        jc = _el("w:jc")
        jc.set(qn("w:val"), "center")
        # w:jc phải đứng trước w:rPr
        ppr.insert(list(ppr).index(rpr), jc)
        for ind in ppr.findall(qn("w:ind")):
            ppr.remove(ind)
    i_.append(r)
    n.append(i_)
    p_ref.addnext(n)
    return n


def van_ban_day_du(p):
    t = []
    for e in p.iter(qn("w:t")):
        t.append(e.text or "")
    return "".join(t)


def _duong_ke(chieu_rong_emu=1500000, pos_emu=2130000):
    """Đoạn chứa đường kẻ (Drawing/Shape) dài ~4 cm, căn giữa dưới tiêu đề phụ lục (như bìa Đề án)."""
    xml = (
        '<w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" '
        'xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
        'xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing">'
        '<w:pPr><w:keepNext/><w:spacing w:before="0" w:after="120" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>'
        '<w:r><w:rPr><w:noProof/></w:rPr><mc:AlternateContent><mc:Choice Requires="wps"><w:drawing>'
        '<wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0" relativeHeight="251661312" behindDoc="0" locked="0" layoutInCell="1" allowOverlap="1">'
        '<wp:simplePos x="0" y="0"/>'
        '<wp:positionH relativeFrom="margin"><wp:posOffset>%d</wp:posOffset></wp:positionH>'
        '<wp:positionV relativeFrom="paragraph"><wp:posOffset>60000</wp:posOffset></wp:positionV>'
        '<wp:extent cx="%d" cy="0"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/>'
        '<wp:docPr id="%d" name="Straight Connector %d"/><wp:cNvGraphicFramePr/>'
        '<a:graphic><a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">'
        '<wps:wsp><wps:cNvCnPr/><wps:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="0"/></a:xfrm><a:prstGeom prst="line"><a:avLst/></a:prstGeom>'
        '<a:ln w="9525"><a:solidFill><a:srgbClr val="000000"/></a:solidFill></a:ln></wps:spPr><wps:bodyPr/></wps:wsp>'
        '</a:graphicData></a:graphic></wp:anchor></w:drawing></mc:Choice>'
        '<mc:Fallback><w:pict/></mc:Fallback></mc:AlternateContent></w:r></w:p>'
    )
    from lxml import etree
    k = _nid()
    return etree.fromstring(xml % (pos_emu, chieu_rong_emu, int(k) % 30000 + 100, int(k) % 30000 + 100, chieu_rong_emu))


def _sect_ngat(body_sectpr, bat_dau_1=True):
    sp = copy.deepcopy(body_sectpr)
    for tag in ("w:titlePg", "w:pgNumType", "w:headerReference", "w:footerReference", "w:type"):
        for e in sp.findall(qn(tag)):
            sp.remove(e)
    pg = _el("w:pgNumType")
    pg.set(qn("w:start"), "1")
    sp.find(qn("w:pgMar")).addnext(pg)
    p = _el("w:p")
    ppr = _el("w:pPr")
    sz = _el("w:spacing")
    sz.set(qn("w:before"), "0")
    sz.set(qn("w:after"), "0")
    sz.set(qn("w:line"), "20")
    sz.set(qn("w:lineRule"), "exact")
    ppr.append(sz)
    rp = _el("w:rPr")
    s = _el("w:sz")
    s.set(qn("w:val"), "2")
    rp.append(s)
    ppr.append(rp)
    ppr.append(sp)
    p.append(ppr)
    return p


def hoan_thien(nguon, dich, qd, don, so_trang=None, phu_luc_1_trang=()):
    """nguon: tệp chị Thoa; dich: tệp Track Changes xuất ra.
    qd, don: câu mô tả Quyết định chỉ định thầu và Đơn xin nhận thầu (dùng ở khoản 2.1).
    phu_luc_1_trang: tập số thứ tự (1–5) phụ lục chỉ có 1 trang (không đánh số trang)."""
    d = Document(nguon)
    body = d.element.body
    paras = lambda: [p for p in body.iter(qn("w:p"))]  # noqa: E731

    # ---- 1. sửa tham chiếu 3.1.4
    for p in paras():
        thay_p(p, r"Điều 11 và Điều 11", "Điều 11 và Điều 12")

    # ---- 2. khoản 2.1
    dong21 = [
        "2.1.1. Thỏa thuận hợp đồng xây dựng: Văn bản hợp đồng này (Phần 1 đến Phần 4);",
        f"2.1.2. Văn bản chỉ định thầu: {qd.split(' ngày ')[0]} phê duyệt kết quả lựa chọn nhà thầu;",
        "2.1.3. Điều kiện cụ thể của hợp đồng xây dựng (Phần 4) và điều khoản tham chiếu đối với hợp đồng (nội dung, khối lượng công việc tại Phụ lục I);",
        "2.1.4. Điều kiện chung của hợp đồng xây dựng (Phần 3);",
        f"2.1.5. Hồ sơ đề xuất của Bên nhận thầu: {don} kèm hồ sơ năng lực;",
        "2.1.6. Biên bản đàm phán hợp đồng: Biên bản đối chiếu tài liệu và Biên bản thương thảo, hoàn thiện hợp đồng ngày 22/10/2026; văn bản sửa đổi, bổ sung hợp đồng (nếu có);",
        "2.1.7. Các phụ lục của hợp đồng: Phụ lục I đến Phụ lục V;",
        "2.1.8. Các tài liệu khác có liên quan.",
    ]
    tieu21 = [p for p in paras() if van_ban_day_du(p).strip() == "2.1. Hồ sơ hợp đồng bao gồm các tài liệu sau:"]
    # Phần 3 (đoạn thường, chữ nguyên văn mẫu): thay 8 dòng đầu, xóa 2 dòng cuối
    p3 = tieu21[0]
    cur = p3.getnext()
    cu = []
    while cur is not None and re.match(r"^2\.1\.\d+\.", van_ban_day_du(cur).strip()):
        cu.append(cur)
        cur = cur.getnext()
    for k, pp in enumerate(cu):
        if k < len(dong21):
            thay_p(pp, r"^.*$", dong21[k])
        else:
            xoa_doan(pp)
    # Phần 4 (bản chị Thoa chèn): xóa dấu "…" và chèn danh sách
    if len(tieu21) > 1:
        p4 = tieu21[1]
        nxt = p4.getnext()
        ref = p4
        for t in dong21:
            ref = chen_doan_sau(ref, t)
        # đoạn "…" nằm sau p4 ban đầu: xóa dấu vết
        if nxt is not None and van_ban_day_du(nxt).strip() == "…":
            xoa_doan(nxt)

    # ---- 3. phụ lục
    heads = {}
    for p in paras():
        m = re.match(r"^PHỤ LỤC SỐ (\d)$", van_ban_day_du(p).strip())
        if m:
            heads[m.group(1)] = p
    final_sect = body.find(qn("w:sectPr"))
    for n in sorted(heads):
        h1 = heads[n]
        h2 = h1.getnext()
        # dòng "Phụ lục I" (La Mã, chữ P hoa)
        thay_p(h1, r"PHỤ LỤC SỐ (\d)", lambda m: "Phụ lục " + LA_MA[m.group(1)])
        # dòng cuối tiêu đề + đường kẻ
        p_cua = chen_doan_sau(h2, "CỦA TRƯỜNG CAO ĐẲNG KON TUM", bold=True, giua=True)
        p_cua.addnext(_duong_ke())
        # ngắt section trước phụ lục 2..5 (phụ lục 1 đã có section riêng từ trước)
        if int(n) >= 2:
            h1.addprevious(_sect_ngat(final_sect))
    # phụ lục 1 cũng cần pgNumType start=1 (đã có ở section 3 cũ); đảm bảo section của phụ lục cuối
    for e in final_sect.findall(qn("w:pgNumType")):
        final_sect.remove(e)
    pg = _el("w:pgNumType")
    pg.set(qn("w:start"), "1")
    final_sect.find(qn("w:pgMar")).addnext(pg)
    for e in final_sect.findall(qn("w:titlePg")):
        final_sect.remove(e)

    # ---- 3b. mọi chỗ "Phụ lục số N" còn lại (lời văn, bảng, mục lục) → "Phụ lục <La Mã>"
    for p in paras():
        thay_p(p, r"Phụ lục số (\d)", lambda m: "Phụ lục " + LA_MA[m.group(1)])
        thay_p(p, r"PHỤ LỤC SỐ (\d)", lambda m: "Phụ lục " + LA_MA[m.group(1)])

    # ---- 4. số trang ở Điều 20
    if so_trang:
        for p in paras():
            if re.search(r"bao gồm \d+ trang", van_ban_day_du(p)):
                if not thay_p(p, r"bao gồm \d+ trang", f"bao gồm {so_trang} trang"):
                    thay_p(p, r"^\d+$", str(so_trang))  # số trang nằm riêng một run (chị Thoa gắn comment vào số này)

    # ---- ngày ký hợp đồng để trống (anh Phục 03/11/2026): bỏ ngày 26/10 chị Thoa điền
    for p in paras():
        if van_ban_day_du(p).startswith("Hôm nay, ngày 26 tháng 10 năm 2026"):
            thay_p(p, r"^26$", "      ")
            thay_p(p, r"^10$", "     ")

    # ---- đánh số trang liên tục từ bìa: bìa là trang 1 (ẩn số), mục lục là trang 2 (TT-32, TT-34)
    s0, s1 = d.sections[0], d.sections[1]
    s0.different_first_page_header_footer = True
    s0.header.is_linked_to_previous = False
    for e in list(s0.header._element):
        s0.header._element.remove(e)
    for e in s1.header._element:
        s0.header._element.append(copy.deepcopy(e))
    for e in s1._sectPr.findall(qn("w:pgNumType")):
        s1._sectPr.remove(e)

    # ---- số trang của phụ lục 1 trang: bỏ khỏi header
    if phu_luc_1_trang:
        secs = d.sections
        for n in phu_luc_1_trang:
            s = secs[1 + int(n)]  # section 0 bìa, 1 nội dung, 2 = phụ lục I …
            s.header.is_linked_to_previous = False
            for hp in s.header.paragraphs:
                for r in list(hp.runs):
                    r._r.getparent().remove(r._r)
                for f in hp._p.findall(qn("w:fldSimple")):
                    hp._p.remove(f)
    d.save(dest := dich)
    return dest


if __name__ == "__main__":
    print("module")
