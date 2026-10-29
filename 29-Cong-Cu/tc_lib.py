"""Tiện ích bổ sung cho ktc_trackchanges: sửa trong một đoạn cụ thể, chèn hàng bảng có dấu vết."""
import sys, copy, unicodedata
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ktc_trackchanges as K
from docx.oxml.ns import qn

N = lambda x: unicodedata.normalize("NFC", x)
LOI = []


class TC(K.TrackChanges):
    def __init__(self, path):
        super().__init__(path)
        # chuẩn hóa NFC toàn bộ text để tìm kiếm ổn định
        for t in self.doc.element.body.iter(qn("w:t")):
            if t.text:
                t.text = N(t.text)

    # --- tìm, bỏ qua mục lục ---
    def _la_muc_luc(self, p):
        try:
            s = (p.style.name or "").lower()
        except Exception:
            s = ""
        return s.startswith("toc") or "table of figures" in s

    def doan_chua(self, cum, bat_dau_sau=None):
        cum = N(cum); da_qua = bat_dau_sau is None
        for p in self._doan():
            if self._la_muc_luc(p):
                continue
            t = K._runs_text(p)
            if not da_qua:
                if N(bat_dau_sau) in t:
                    da_qua = True
                continue
            if cum in t:
                return p
        return None

    def thay_trong(self, p, cu, moi, author=K.DIEU_CHINH):
        cu = N(cu); t = K._runs_text(p); vt = t.find(cu)
        if vt < 0:
            raise ValueError("khong co trong doan: " + cu[:60])
        runs = K._tach_run(p, vt, vt + len(cu))
        if moi:
            r_moi = copy.deepcopy(runs[0]); K._dat_text(r_moi, moi)
            runs[-1].addnext(r_moi)
        for r in runs:
            self._danh_dau_xoa(r, author)
        if moi:
            self._danh_dau_them(r_moi, author)
        self._bao("Điều chỉnh" if moi else "Bỏ", cu, moi, author, "")

    def T(self, cu, moi, bat_dau_sau=None, tat_ca=False, bat_buoc=True):
        """Thay có dấu vết, bỏ qua mục lục."""
        n = 0
        while True:
            p = self.doan_chua(cu, bat_dau_sau)
            if p is None:
                break
            self.thay_trong(p, cu, moi, K.DIEU_CHINH if moi else K.BO); n += 1
            if not tat_ca:
                break
        if n == 0 and bat_buoc:
            LOI.append(("T", cu[:80]))
        return n

    def S(self, moc, text, bat_dau_sau=None, bat_buoc=True):
        """Chèn đoạn mới sau đoạn chứa moc."""
        p = self.doan_chua(moc, bat_dau_sau)
        if p is None:
            if bat_buoc: LOI.append(("S", moc[:80]))
            return None
        p_moi = copy.deepcopy(p._element)
        for r in list(p_moi.iter(qn("w:r"))):
            r.getparent().remove(r)
        for x in p_moi.findall(qn("w:ins")) + p_moi.findall(qn("w:del")) + p_moi.findall(qn("w:hyperlink")):
            p_moi.remove(x)
        p._element.addnext(p_moi)
        mau = p.runs[0]._element if p.runs else K._el("w:r")
        r_moi = copy.deepcopy(mau)
        K._dat_text(r_moi, text)
        p_moi.append(r_moi)
        self._danh_dau_them(r_moi, K.BO_SUNG)
        self._bao("Bổ sung", "", text, K.BO_SUNG, "")
        return p_moi

    # --- bảng ---
    def bang_chua(self, *cums):
        for i, tb in enumerate(self.doc.tables):
            t = N(" ".join(c.text for r in tb.rows for c in r.cells))
            if all(N(x) in t for x in cums):
                return i, tb
        LOI.append(("BANG", str(cums)[:80])); return None, None

    def hang_chua(self, tb, cum, cot=None):
        for j, r in enumerate(tb.rows):
            cells = r.cells if cot is None else [r.cells[cot]]
            if any(N(cum) in N(c.text) for c in cells):
                return j, r
        LOI.append(("HANG", cum[:80])); return None, None

    def o(self, row, cot, cu, moi):
        for p in row.cells[cot].paragraphs:
            if N(cu) in K._runs_text(p):
                self.thay_trong(p, cu, moi); return
        LOI.append(("O", cu[:80]))

    def chen_hang(self, tb, sau_hang, gia_tri):
        """Chèn hàng mới (có dấu vết) sau hàng chỉ số sau_hang; gia_tri: list text theo ô."""
        mau = tb.rows[sau_hang]._tr
        tr = copy.deepcopy(mau)
        for x in tr.iter(qn("w:ins")):
            pass
        # xóa bọc ins/del cũ
        for el in list(tr.iter(qn("w:del"))):
            el.getparent().remove(el)
        for el in list(tr.iter(qn("w:ins"))):
            par = el.getparent()
            for ch in list(el):
                el.addprevious(ch)
            par.remove(el)
        tcs = tr.findall(qn("w:tc"))
        for k, tc_el in enumerate(tcs):
            ps = tc_el.findall(qn("w:p"))
            for p in ps[1:]:
                tc_el.remove(p)
            p0 = ps[0]
            rs = p0.findall(qn("w:r"))
            for r in rs[1:]:
                p0.remove(r)
            if rs:
                r0 = rs[0]
            else:
                r0 = K._el("w:r"); p0.append(r0)
            for t in r0.findall(qn("w:t")) + r0.findall(qn("w:delText")):
                r0.remove(t)
            text = gia_tri[k] if k < len(gia_tri) else ""
            K._dat_text(r0, text)
            self._danh_dau_them(r0, K.BO_SUNG)
        trPr = tr.find(qn("w:trPr"))
        if trPr is None:
            trPr = K._el("w:trPr"); tr.insert(0, trPr)
        ins = K._el("w:ins")
        ins.set(qn("w:id"), self._next_id()); ins.set(qn("w:author"), K.BO_SUNG); ins.set(qn("w:date"), K._now())
        trPr.append(ins)
        mau.addnext(tr)
        self._bao("Bổ sung", "", " | ".join(gia_tri), K.BO_SUNG, "hàng bảng")
        return tr
