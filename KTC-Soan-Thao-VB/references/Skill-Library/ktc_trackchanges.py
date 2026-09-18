# -*- coding: utf-8 -*-
"""KTC Track Changes — sua .docx co dau vet va xuat nhat ky sua doi.

Kich hoat: nguoi dung noi "Track Changes" HOAC "ghi nhat ky sua doi".

Can cu:
  - KTC-Quan-tri/01-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md (NT-2)
  - KTC-Ra-Soat-897-v2-Cai-tien/references/Skill-Library/
      Bo-Sung-Chuan-Hoa-TrackChanges-MauChu-PhienBanSkill_20260825.md

Ba nhom API:
  1. TrackChanges(path)  -> sua co dau vet, .luu(out)
  2. kiem_tra(path)      -> validator OOXML (thay cho validate.py con thieu, KI-009)
  3. nhat_ky_sua_doi(p)  -> doc BAT KY .docx co track changes -> bang ke thay doi

Vi du:
    tc = TrackChanges("BC-375.docx")
    tc.thay("2.000 hoc sinh", "2.150 hoc sinh")        # dieu chinh
    tc.them_sau("Muc 3", "3.1. Noi dung bo sung.")     # bo sung
    tc.xoa_cum("da tham muu cho Lanh dao Truong ")     # bo
    tc.luu("BC-375_sua.docx")
    print(tc.bao_cao())
"""
from __future__ import annotations

import copy
import datetime as _dt
import re
from typing import Iterable

from docx import Document
from docx.oxml.ns import qn

# --- Quy uoc ten author: Word to mau theo author, khong ep duoc ma mau qua XML ---
BO = "Nội dung bỏ (Claude)"
BO_SUNG = "Nội dung bổ sung (Claude)"
DIEU_CHINH = "Nội dung điều chỉnh (Claude)"

_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _now() -> str:
    return _dt.datetime.now().replace(microsecond=0).isoformat() + "Z"


def _el(tag: str):
    from docx.oxml import OxmlElement
    return OxmlElement(tag)


# ----------------------------------------------------------------------------
# Tach run sao cho doan text can xu ly chiem tron mot so run
# ----------------------------------------------------------------------------
def _runs_text(para) -> str:
    return "".join(r.text for r in para.runs)


def _tach_run(para, dau: int, cuoi: int) -> list:
    """Tach cac run cua para sao cho [dau, cuoi) trung khop bien run.

    Tra ve danh sach run nam tron trong khoang do, theo dung thu tu.
    """
    vi_tri, ket_qua = 0, []
    for run in list(para.runs):
        n = len(run.text)
        d, c = vi_tri, vi_tri + n
        vi_tri = c
        if n == 0 or c <= dau or d >= cuoi:
            continue

        cat_trai = max(dau - d, 0)
        cat_phai = min(cuoi - d, n)

        # Cat phan duoi cuoi truoc, de offset phan dau khong doi
        if cat_phai < n:
            sau = copy.deepcopy(run._element)
            run._element.addnext(sau)
            _dat_text(sau, run.text[cat_phai:])
            _dat_text(run._element, run.text[:cat_phai])

        if cat_trai > 0:
            truoc = copy.deepcopy(run._element)
            run._element.addprevious(truoc)
            _dat_text(truoc, run.text[:cat_trai])
            _dat_text(run._element, run.text[cat_trai:])

        ket_qua.append(run._element)
    return ket_qua


def _text_day_du(el, chap_nhan: bool = True) -> str:
    """Text that ra tu MOT phan tu, ke ca run nam trong <w:ins>/<w:del>.

    `paragraph.text` cua python-docx chi doc <w:r> la con TRUC TIEP nen bo sot
    toan bo noi dung da danh dau — khong dung duoc cho file co track changes.

    chap_nhan=True  -> ban sau khi CHAP NHAN het thay doi (giu ins, bo del)
    chap_nhan=False -> ban goc truoc khi sua      (bo ins, giu del)
    """
    ra = []
    for t in el.iter(qn("w:t"), qn("w:delText")):
        trong_del = trong_ins = False
        cha = t.getparent()
        while cha is not None:
            if cha.tag == qn("w:del"):
                trong_del = True
            elif cha.tag == qn("w:ins"):
                trong_ins = True
            cha = cha.getparent()
        giu = (not trong_del) if chap_nhan else (not trong_ins)
        if giu:
            ra.append(t.text or "")
    return "".join(ra)


def _dat_text(r_el, text: str) -> None:
    for t in r_el.findall(qn("w:t")) + r_el.findall(qn("w:delText")):
        r_el.remove(t)
    t = _el("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    r_el.append(t)


# ----------------------------------------------------------------------------
class TrackChanges:
    """Mo .docx GOC va sua co dau vet. Khong bao gio ghi de file goc."""

    def __init__(self, duong_dan: str):
        self.goc = duong_dan
        self.doc = Document(duong_dan)
        self._id = 1000
        self.thay_doi: list[dict] = []

    # -- ha tang ------------------------------------------------------------
    def _next_id(self) -> str:
        self._id += 1
        return str(self._id)

    def _bao(self, loai: str, cu: str, moi: str, author: str, vi_tri: str) -> None:
        self.thay_doi.append({
            "stt": len(self.thay_doi) + 1, "loai": loai, "cu": cu,
            "moi": moi, "author": author, "vi_tri": vi_tri,
        })

    def _danh_dau_xoa(self, r_el, author: str) -> None:
        """Boc run vao <w:del> va doi <w:t> -> <w:delText>."""
        for t in r_el.findall(qn("w:t")):
            t.tag = qn("w:delText")
        d = _el("w:del")
        d.set(qn("w:id"), self._next_id())
        d.set(qn("w:author"), author)
        d.set(qn("w:date"), _now())
        r_el.addprevious(d)
        d.append(r_el)

    def _danh_dau_them(self, r_el, author: str) -> None:
        i = _el("w:ins")
        i.set(qn("w:id"), self._next_id())
        i.set(qn("w:author"), author)
        i.set(qn("w:date"), _now())
        r_el.addprevious(i)
        i.append(r_el)

    def _doan(self) -> Iterable:
        """Duyet MOI doan, ke ca doan trong bang."""
        for p in self.doc.paragraphs:
            yield p
        for tb in self.doc.tables:
            for row in tb.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        yield p

    def _tim(self, cum: str):
        for idx, p in enumerate(self._doan()):
            noi_dung = _runs_text(p)
            vt = noi_dung.find(cum)
            if vt >= 0:
                return p, vt, idx
        return None, -1, -1

    # -- thao tac -----------------------------------------------------------
    def xoa_cum(self, cum: str, author: str = BO, tat_ca: bool = False) -> int:
        """Xoa mot cum tu, danh dau <w:del>. Tra ve so cho da xoa."""
        n = 0
        while True:
            p, vt, idx = self._tim(cum)
            if p is None:
                break
            for r in _tach_run(p, vt, vt + len(cum)):
                self._danh_dau_xoa(r, author)
            self._bao("Bỏ", cum, "", author, f"đoạn {idx + 1}")
            n += 1
            if not tat_ca:
                break
        if n == 0:
            raise ValueError(f"Không tìm thấy cụm: {cum!r}")
        return n

    def thay(self, cu: str, moi: str, author: str = DIEU_CHINH,
             tat_ca: bool = False) -> int:
        """Thay noi dung: cap <w:del> + <w:ins> lien nhau, CUNG author."""
        n = 0
        while True:
            p, vt, idx = self._tim(cu)
            if p is None:
                break
            runs = _tach_run(p, vt, vt + len(cu))
            moc = runs[-1]
            r_moi = copy.deepcopy(runs[0])
            # go bo boc <w:ins>/<w:del> neu run goc da nam trong do
            _dat_text(r_moi, moi)
            moc.addnext(r_moi)
            for r in runs:
                self._danh_dau_xoa(r, author)
            self._danh_dau_them(r_moi, author)
            self._bao("Điều chỉnh", cu, moi, author, f"đoạn {idx + 1}")
            n += 1
            if not tat_ca:
                break
        if n == 0:
            raise ValueError(f"Không tìm thấy cụm: {cu!r}")
        return n

    def them_sau(self, moc: str, text: str, author: str = BO_SUNG):
        """Chen mot DOAN moi ngay sau doan chua `moc`."""
        p, vt, idx = self._tim(moc)
        if p is None:
            raise ValueError(f"Không tìm thấy mốc: {moc!r}")
        p_moi = copy.deepcopy(p._element)
        for r in p_moi.findall(qn("w:r")):
            p_moi.remove(r)
        for ins in p_moi.findall(qn("w:ins")) + p_moi.findall(qn("w:del")):
            p_moi.remove(ins)
        p._element.addnext(p_moi)

        mau = p.runs[0]._element if p.runs else _el("w:r")
        r_moi = copy.deepcopy(mau)
        _dat_text(r_moi, text)
        p_moi.append(r_moi)
        self._danh_dau_them(r_moi, author)
        self._bao("Bổ sung", "", text, author, f"sau đoạn {idx + 1}")
        return p_moi

    def xoa_doan(self, cum: str, author: str = BO, so_doan: int = 1) -> int:
        """Xoa NGUYEN doan (ke ca dau doan), bat dau tu doan chua `cum`.

        Khac `xoa_cum`: `xoa_cum` chi gach text, dau doan van con — chap nhan
        thay doi xong se con lai hang loat doan rong. Xoa nguyen doan phai danh
        dau ca DAU DOAN bang <w:rPr><w:del/></w:rPr> trong <w:pPr>.

        Thu tu phan tu trong <w:pPr> theo schema: <w:pStyle>, <w:numPr>, ...,
        <w:rPr> nam O CUOI. Dat sai cho lam hong tep — Word bao "unreadable".

        so_doan: xoa lien tiep may doan ke tu doan tim duoc (de xoa ca muc).
        """
        p, _, idx = self._tim(cum)
        if p is None:
            raise ValueError(f"Không tìm thấy cụm: {cum!r}")
        els = [p._element]
        cur = p._element
        for _ in range(so_doan - 1):
            cur = cur.getnext()
            while cur is not None and cur.tag != qn("w:p"):
                cur = cur.getnext()
            if cur is None:
                break
            els.append(cur)

        for el in els:
            for r in el.findall(qn("w:r")):
                self._danh_dau_xoa(r, author)
            # danh dau DAU DOAN la da xoa
            pPr = el.find(qn("w:pPr"))
            if pPr is None:
                pPr = _el("w:pPr")
                el.insert(0, pPr)
            rPr = pPr.find(qn("w:rPr"))
            if rPr is None:
                rPr = _el("w:rPr")
                pPr.append(rPr)          # rPr phai o CUOI pPr
            if rPr.find(qn("w:del")) is None:
                d = _el("w:del")
                d.set(qn("w:id"), self._next_id())
                d.set(qn("w:author"), author)
                d.set(qn("w:date"), _now())
                rPr.insert(0, d)         # del la phan tu DAU trong rPr
        self._bao("Bỏ", f"[{len(els)} đoạn] {cum[:60]}", "", author,
                  f"đoạn {idx + 1}")
        return len(els)

    def xoa_tu_den(self, cum_dau: str, cum_cuoi: str, author: str = BO) -> int:
        """Xoa cac doan TU doan chua `cum_dau` DEN TRUOC doan chua `cum_cuoi`.

        An toan hon `xoa_doan(so_doan=N)`: khong phai dem tay, va khong troi
        qua moc ket thuc khi giua chung co bang (<w:tbl> khong phai <w:p>).
        """
        ds = list(self.doc.paragraphs)
        i = next((k for k, p in enumerate(ds) if cum_dau in _runs_text(p)), None)
        if i is None:
            raise ValueError(f"Không tìm thấy mốc đầu: {cum_dau!r}")
        j = next((k for k in range(i + 1, len(ds)) if cum_cuoi in _runs_text(ds[k])), None)
        if j is None:
            raise ValueError(f"Không tìm thấy mốc cuối: {cum_cuoi!r}")

        n = 0
        for p in ds[i:j]:
            el = p._element
            for r in el.findall(qn("w:r")):
                self._danh_dau_xoa(r, author)
            pPr = el.find(qn("w:pPr"))
            if pPr is None:
                pPr = _el("w:pPr")
                el.insert(0, pPr)
            rPr = pPr.find(qn("w:rPr"))
            if rPr is None:
                rPr = _el("w:rPr")
                pPr.append(rPr)
            if rPr.find(qn("w:del")) is None:
                d = _el("w:del")
                d.set(qn("w:id"), self._next_id())
                d.set(qn("w:author"), author)
                d.set(qn("w:date"), _now())
                rPr.insert(0, d)
            n += 1
        self._bao("Bỏ", f"[{n} đoạn] {cum_dau[:50]} … đến trước {cum_cuoi[:40]}",
                  "", author, f"đoạn {i + 1}–{j}")
        return n

    def xoa_bang(self, bang: int, author: str = BO) -> int:
        """Xoa nguyen mot bang: danh dau xoa moi hang."""
        tb = self.doc.tables[bang]
        for i in range(len(tb.rows)):
            self.xoa_hang(bang, i, author)
        return len(tb.rows)

    def xoa_hang(self, bang: int, hang: int, author: str = BO) -> None:
        """Xoa hang bang dung co che OOXML.

        <w:del> phai la phan tu CUOI CUNG trong <w:trPr> (sau <w:trHeight>) —
        sai thu tu lam hong schema. Dong thoi boc text trong hang bang <w:del>
        de hien gach ngang khi xem truoc.
        """
        row = self.doc.tables[bang].rows[hang]
        tr = row._tr
        trPr = tr.find(qn("w:trPr"))
        if trPr is None:
            trPr = _el("w:trPr")
            tr.insert(0, trPr)
        d = _el("w:del")
        d.set(qn("w:id"), self._next_id())
        d.set(qn("w:author"), author)
        d.set(qn("w:date"), _now())
        trPr.append(d)                      # CUOI CUNG — bat buoc

        noi_dung = " | ".join(c.text.strip() for c in row.cells)
        for cell in row.cells:
            for p in cell.paragraphs:
                for r in list(p.runs):
                    self._danh_dau_xoa(r._element, author)
        self._bao("Bỏ hàng bảng", noi_dung, "", author,
                  f"bảng {bang + 1}, hàng {hang + 1}")

    # -- ket xuat -----------------------------------------------------------
    def luu(self, duong_dan: str) -> str:
        if str(duong_dan) == str(self.goc):
            raise ValueError("Không được ghi đè file gốc — đổi tên đầu ra.")
        self.doc.save(duong_dan)
        return duong_dan

    def bao_cao(self) -> str:
        """Nhat ky sua doi cua chinh phien lam viec nay (Markdown)."""
        return _bang_md(self.thay_doi, self.goc)


# ----------------------------------------------------------------------------
def _bang_md(rows: list[dict], nguon: str) -> str:
    if not rows:
        return f"# Nhật ký sửa đổi — `{nguon}`\n\nKhông có thay đổi nào.\n"
    out = [f"# Nhật ký sửa đổi — `{nguon}`", "",
           f"**Tổng số thay đổi:** {len(rows)}", ""]
    dem: dict[str, int] = {}
    for r in rows:
        dem[r["loai"]] = dem.get(r["loai"], 0) + 1
    out.append(" · ".join(f"{k}: **{v}**" for k, v in sorted(dem.items())))
    out += ["", "| # | Loại | Vị trí | Nội dung cũ | Nội dung mới |",
            "|---|---|---|---|---|"]
    for r in rows:
        cu = (r["cu"] or "—").replace("|", "\\|")[:120]
        moi = (r["moi"] or "—").replace("|", "\\|")[:120]
        out.append(f"| {r['stt']} | {r['loai']} | {r['vi_tri']} | {cu} | {moi} |")
    return "\n".join(out) + "\n"


def nhat_ky_sua_doi(duong_dan: str) -> str:
    """Doc BAT KY .docx co track changes -> bang ke thay doi (Markdown).

    Dung duoc ca voi file do NGUOI sua trong Word, khong chi file do mo-dun nay
    sinh ra. Ghep <w:del> + <w:ins> lien ke cung author thanh 1 dong 'Dieu chinh'.
    """
    doc = Document(duong_dan)
    rows: list[dict] = []

    def quet(para, nhan: str):
        con = list(para._element)
        i = 0
        while i < len(con):
            e = con[i]
            if e.tag == qn("w:del"):
                cu = "".join(t.text or "" for t in e.iter(qn("w:delText")))
                au = e.get(qn("w:author")) or ""
                ke = con[i + 1] if i + 1 < len(con) else None
                if (ke is not None and ke.tag == qn("w:ins")
                        and (ke.get(qn("w:author")) or "") == au):
                    moi = "".join(t.text or "" for t in ke.iter(qn("w:t")))
                    rows.append({"stt": len(rows) + 1, "loai": "Điều chỉnh",
                                 "cu": cu, "moi": moi, "author": au, "vi_tri": nhan})
                    i += 2
                    continue
                rows.append({"stt": len(rows) + 1, "loai": "Bỏ", "cu": cu,
                             "moi": "", "author": au, "vi_tri": nhan})
            elif e.tag == qn("w:ins"):
                moi = "".join(t.text or "" for t in e.iter(qn("w:t")))
                rows.append({"stt": len(rows) + 1, "loai": "Bổ sung", "cu": "",
                             "moi": moi, "author": e.get(qn("w:author")) or "",
                             "vi_tri": nhan})
            i += 1

    for n, p in enumerate(doc.paragraphs, 1):
        quet(p, f"đoạn {n}")
    for tb_i, tb in enumerate(doc.tables, 1):
        for r_i, row in enumerate(tb.rows, 1):
            trPr = row._tr.find(qn("w:trPr"))
            if trPr is not None and trPr.find(qn("w:del")) is not None:
                rows.append({"stt": len(rows) + 1, "loai": "Bỏ hàng bảng",
                             "cu": " | ".join(_text_day_du(c._tc, False).strip()
                                              for c in row.cells),
                             "moi": "", "author": trPr.find(qn("w:del")).get(qn("w:author")) or "",
                             "vi_tri": f"bảng {tb_i}, hàng {r_i}"})
                continue
            for c_i, cell in enumerate(row.cells, 1):
                for p in cell.paragraphs:
                    quet(p, f"bảng {tb_i}, hàng {r_i}, cột {c_i}")
    return _bang_md(rows, duong_dan)


# ----------------------------------------------------------------------------
def kiem_tra(duong_dan: str) -> dict:
    """Validator OOXML — chay TRUOC khi giao file. Thay cho validate.py con thieu.

    Tra ve {"dat": bool, "loi": [...], "canh_bao": [...], "thong_ke": {...}}
    """
    doc = Document(duong_dan)
    body = doc.element.body
    loi, canh_bao = [], []

    # 1. <w:del> phai la phan tu CUOI CUNG trong <w:trPr>
    for i, trPr in enumerate(body.iter(qn("w:trPr")), 1):
        con = list(trPr)
        for j, e in enumerate(con):
            if e.tag == qn("w:del") and j != len(con) - 1:
                sau = con[j + 1].tag.split("}")[-1]
                loi.append(f"<w:del> trong <w:trPr> #{i} không nằm cuối "
                           f"(còn <w:{sau}> phía sau) — hỏng schema")

    # 2. Run trong <w:del> phai dung <w:delText>, khong duoc con <w:t>
    for d in body.iter(qn("w:del")):
        if d.getparent() is not None and d.getparent().tag == qn("w:trPr"):
            continue
        for r in d.iter(qn("w:r")):
            if r.find(qn("w:t")) is not None:
                loi.append("Run trong <w:del> còn <w:t> — phải là <w:delText>")

    # 3. Run trong <w:ins> khong duoc dung <w:delText>
    for ins in body.iter(qn("w:ins")):
        for r in ins.iter(qn("w:r")):
            if r.find(qn("w:delText")) is not None:
                loi.append("Run trong <w:ins> có <w:delText> — sai loại")

    # 4. rPr long nhau
    for rPr in body.iter(qn("w:rPr")):
        if rPr.find(qn("w:rPr")) is not None:
            loi.append("<w:rPr> lồng trong <w:rPr>")

    # 5. Run vua co w:t vua co w:delText
    for r in body.iter(qn("w:r")):
        if r.find(qn("w:t")) is not None and r.find(qn("w:delText")) is not None:
            loi.append("Một run chứa cả <w:t> và <w:delText>")

    # 6. Thieu thuoc tinh bat buoc
    for tag in ("w:ins", "w:del"):
        for e in body.iter(qn(tag)):
            for attr in ("w:id", "w:author", "w:date"):
                if e.get(qn(attr)) is None:
                    loi.append(f"<{tag}> thiếu thuộc tính {attr}")

    # 7. Trung w:id
    ids: dict[str, int] = {}
    for tag in ("w:ins", "w:del"):
        for e in body.iter(qn(tag)):
            k = e.get(qn("w:id"))
            ids[k] = ids.get(k, 0) + 1
    trung = [k for k, v in ids.items() if v > 1]
    if trung:
        canh_bao.append(f"Trùng w:id: {', '.join(sorted(trung)[:10])}")

    # Thong ke theo author
    theo_author: dict[str, int] = {}
    for tag in ("w:ins", "w:del"):
        for e in body.iter(qn(tag)):
            a = e.get(qn("w:author")) or "(không rõ)"
            theo_author[a] = theo_author.get(a, 0) + 1
    if not theo_author:
        canh_bao.append("File KHÔNG có dấu vết track changes nào")

    return {
        "dat": not loi,
        "loi": sorted(set(loi)),
        "canh_bao": canh_bao,
        "thong_ke": {"theo_author": theo_author,
                     "tong_danh_dau": sum(theo_author.values())},
    }


def doi_chieu_goc(goc: str, sua: str) -> dict:
    """So sanh van ban HIEN THI cua ban sua (da chap nhan het) voi ban goc.

    Muc dich: bat truong hop soan lai tu dau roi trinh bay nhu ban sua —
    dieu NT-2 cam. Neu so doan lech qua nhieu ma so danh dau lai it, la dau hieu.
    """
    d1, d2 = Document(goc), Document(sua)
    n1 = [t for t in (_text_day_du(p._element).strip() for p in d1.paragraphs) if t]
    # Ban sua doc theo goc-truoc-khi-sua: bo <w:ins>, giu <w:del>
    n2 = [t for t in (_text_day_du(p._element, False).strip()
                      for p in d2.paragraphs) if t]
    kt = kiem_tra(sua)
    khop = len(set(n1) & set(n2))
    ty_le = khop / len(n1) if n1 else 0.0
    return {
        "doan_goc": len(n1), "doan_sau_khi_tu_choi_het": len(n2),
        "doan_khop": khop, "ty_le_khoi_phuc": round(ty_le, 3),
        "danh_dau": kt["thong_ke"]["tong_danh_dau"],
        # Tu choi het thay doi PHAI ra dung ban goc. Lech nhieu = da soan lai
        # tu dau roi trinh bay nhu ban sua — dieu NT-2 cam.
        "nghi_soan_lai_tu_dau": ty_le < 0.9,
    }
