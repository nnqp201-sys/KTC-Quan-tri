# -*- coding: utf-8 -*-
"""Dung Bao cao thang 8 + Ke hoach thang 9 cap Truong.

NT-1: PHAT TRIEN TU chinh BC-375 da ban hanh (mo file that, thay noi dung)
      -> ke thua tuyet doi style, le, phong chu, bang the thuc.
Nguon noi dung: 13 bao cao TUONG THUAT (Phu luc IIa) cua don vi.
Chuan phan loai: TB 817 (38 noi ham) — KHONG dung ten truc trong file danh muc
      Excel vi file do la du thao lan 4, ten truc lech voi TB 817.
"""
import copy, json, os, re, sys
from docx import Document
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from vanphong import cap_truong, kiem_tra                      # noqa: E402
from noi_ham import trich, PhanLoai                            # noqa: E402
import chuan_bao_cao as CBC                                    # noqa: E402

GOC = (r"D:\.CLAUDE code\KTC-Database\02-KTC-Regulations"
       r"\BC-375_Bao-cao-ket-qua-thang-8-2026_20260906_v1.docx")
NAR = os.path.join(HERE, "_trung_gian", "narrative.json")
OUTDIR = r"D:\.CLAUDE code\KTC-Quan-tri\12-Output\2026-09-14"

TEN_TRUC = {                       # TB 817 — dung y nhu BC-375 dat tieu de
    1: "Thực hiện mục tiêu phát triển kinh tế - xã hội và nhiệm vụ chính trị",
    2: "Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát",
    3: "Thúc đẩy phát triển KH-CN, đổi mới sáng tạo và chuyển đổi số",
    4: "Xây dựng Đảng và hệ thống chính trị; phòng, chống tham nhũng, tiêu cực",
    5: "Phát triển văn hóa, con người, bảo đảm an sinh xã hội, nâng cao đời sống Nhân dân",
    6: "Củng cố quốc phòng, an ninh, giữ vững ổn định chính trị - xã hội, "
       "nâng cao hiệu quả đối ngoại và hội nhập quốc tế",
}
TEN_NQ = {   # thu tu va ten y nhu BC-375
    "59": "Nghị quyết số 59-NQ/TW ngày 24/01/2025 hội nhập quốc tế trong tình hình mới",
    "66": "Nghị quyết số 66-NQ/TW ngày 30/4/2025 đổi mới công tác xây dựng và thi hành pháp luật",
    "68": "Nghị quyết số 68-NQ/TW ngày 04/5/2025 phát triển kinh tế tư nhân",
    "79": "Nghị quyết số 79-NQ/TW ngày 06/01/2026 phát triển kinh tế nhà nước",
    "70": "Nghị quyết số 70-NQ/TW ngày 20/8/2025 bảo đảm an ninh năng lượng quốc gia",
    "71": "Nghị quyết số 71-NQ/TW ngày 22/8/2025 về đột phá phát triển giáo dục và đào tạo",
    "72": "Nghị quyết số 72-NQ/TW ngày 09/9/2025 bảo vệ, chăm sóc sức khỏe nhân dân",
    "80": "Nghị quyết số 80-NQ/TW ngày 07/01/2026 phát triển văn hóa Việt Nam",
}
THU_TU_NQ = ["59", "66", "68", "79", "70", "71", "72", "80"]


# --------------------------------------------------------------- van ban
# Bo tien to "Cong tac X:" don vi tu dat o dau y -> tranh nhan long nhan
TIEN_TO = re.compile(r"^\s*(Công tác|Về công tác|Về)\s+[^:]{2,45}:\s*", re.I)


def gon(s: str) -> str:
    s = TIEN_TO.sub("", s.strip())
    s = cap_truong(s)
    s = re.sub(r"^\s*[-+•*]\s*", "", s).strip(" .;,")
    s = re.sub(r"\s{2,}", " ", s)
    return s


def ghep(items: list, gioi_han: int = 6) -> str:
    """Ghep nhieu y thanh mot cau ghep kieu BC-375, bo trung lap."""
    ra, thay = [], set()
    for it in items:
        t = gon(it)
        if len(t) < 15:
            continue
        khoa = re.sub(r"[^\w]", "", t.lower())[:45]
        if khoa in thay:
            continue
        thay.add(khoa)
        ra.append(t[0].upper() + t[1:] if ra == [] else t[0].lower() + t[1:])
    if not ra:
        return ""
    if len(ra) > gioi_han:
        ra = ra[:gioi_han]
    return "; ".join(ra) + "."


# --------------------------------------------------------------- noi dung
def soan(nar: dict, pl: PhanLoai, pha: str) -> dict:
    """pha = 'kq' hoac 'kh'. Tra ve {truc: [(linh_vuc, van), ...]}"""
    gom = {i: {} for i in range(1, 7)}
    for dv, d in nar.items():
        for truc_s, ds in d[pha].items():
            truc = int(truc_s)
            for it in ds:
                # Nhan muc con LUON lay tu noi ham CUA CHINH TRUC do (TB 817),
                # khong lay nhan tu do cua don vi -> nhan luon nhat quan voi muc.
                # Nhan muc con lay tu DANH MUC CO DINH trong tep mau chinh
                # thuc (chuan_bao_cao.py), KHONG tu sinh tu ten noi ham TB 817.
                # Loi da mac: tu sinh -> chi 5/28 nhan nam trong danh muc mau.
                nh, _ = pl(it["noi_dung"], truc)
                # BC-375 gom truyen thong ve muc 5, ky cuong hanh chinh ve muc 4
                if nh and nh["so"] == 90:
                    truc = 5
                elif nh and nh["so"] == 91:
                    truc = 4
                lv = CBC.nhan(it["noi_dung"], truc)
                ds = CBC.danh_muc(truc)
                so = ds.index(lv) if lv in ds else 99
                gom[truc].setdefault((so, lv), []).append(it["noi_dung"])
    ra = {}
    for t in range(1, 7):
        muc = [(lv, ghep(v)) for (so, lv), v in sorted(gom[t].items())]
        ra[t] = [(lv, v) for lv, v in muc if v]
    return ra


def soan_nq(nar: dict, pha: str) -> list:
    gom = {}
    for dv, d in nar.items():
        for so, ds in d[pha].items():
            gom.setdefault(so, []).extend(ds)
    ra = []
    for so in THU_TU_NQ:
        if so in gom:
            v = ghep(gom[so], 4)
            if v:
                ra.append((TEN_NQ[so], v))
    return ra


# --------------------------------------------------------------- dung docx
class Builder:
    """Phat trien tu BC-375: giu nguyen doan dau/cuoi, thay phan than."""

    def __init__(self, goc: str):
        self.doc = Document(goc)
        ps = self.doc.paragraphs
        self.i_dau = next(i for i, p in enumerate(ps)
                          if p.text.strip().startswith("I. KẾT QUẢ"))
        self.i_cuoi = next(i for i, p in enumerate(ps)
                           if p.text.strip().startswith("Trên đây là"))
        # mau style: tieu de muc La Ma, tieu de so, doan noi dung
        self.m_h1 = ps[self.i_dau]._element
        self.m_h2 = ps[self.i_dau + 1]._element
        self.m_body = ps[self.i_dau + 2]._element
        self.neo = ps[self.i_cuoi]._element        # chen TRUOC neo
        self.xoa_than(ps)

    def xoa_than(self, ps):
        for p in ps[self.i_dau:self.i_cuoi]:
            p._element.getparent().remove(p._element)

    @staticmethod
    def _dat_run(r, text: str, thuong: bool):
        """Dat text cho 1 run; thuong=True -> tat dam/nghieng (b=0, i=0)."""
        for t in r.findall(qn("w:t")):
            r.remove(t)
        rPr = r.find(qn("w:rPr"))
        if thuong:
            if rPr is None:
                rPr = r.makeelement(qn("w:rPr"), {})
                r.insert(0, rPr)
            for tag in ("w:b", "w:bCs", "w:i", "w:iCs"):
                for e in rPr.findall(qn(tag)):
                    rPr.remove(e)
                e = rPr.makeelement(qn(tag), {})
                e.set(qn("w:val"), "0")
                rPr.append(e)
        t = r.makeelement(qn("w:t"), {})
        t.text = text
        t.set(qn("xml:space"), "preserve")
        r.append(t)

    def doan(self, nhan: str, noi_dung: str, sao: bool = True):
        """Doan noi dung kieu BC-375: run 1 = nhan (dam nghieng), run 2 = noi
        dung (THUONG). Ban goc tach lam 2 run; gop 1 run se lam ca doan dam."""
        el = copy.deepcopy(self.m_body)
        rs = el.findall(qn("w:r"))
        if len(rs) < 2:
            rs.append(copy.deepcopy(rs[0]))
            rs[0].addnext(rs[1])
        for r in el.findall(qn("w:r"))[2:]:
            el.remove(r)
        self._dat_run(rs[0], (f"* {nhan}: " if sao else f"{nhan}: "), thuong=False)
        self._dat_run(rs[1], noi_dung, thuong=True)
        self.neo.addprevious(el)

    def _them(self, mau, text: str):
        el = copy.deepcopy(mau)
        for r in el.findall(qn("w:r"))[1:]:
            el.remove(r)
        rs = el.findall(qn("w:r"))
        if not rs:
            return
        r = rs[0]
        for t in r.findall(qn("w:t")):
            r.remove(t)
        t = r.makeelement(qn("w:t"), {})
        t.text = text
        t.set(qn("xml:space"), "preserve")
        r.append(t)
        self.neo.addprevious(el)

    def h1(self, s): self._them(self.m_h1, s)
    def h2(self, s): self._them(self.m_h2, s)
    def body(self, s): self._them(self.m_body, s)

    def luu(self, p):
        os.makedirs(os.path.dirname(p), exist_ok=True)
        self.doc.save(p)
        return p


def main():
    nar = json.load(open(NAR, encoding="utf-8"))
    pl = PhanLoai(trich())
    kq, kh = soan(nar, pl, "kq"), soan(nar, pl, "kh")
    nq_kq, nq_kh = soan_nq(nar, "nq_kq"), soan_nq(nar, "nq_kh")

    b = Builder(GOC)

    # ---- I. KET QUA THANG 8
    b.h1("I. KẾT QUẢ THỰC HIỆN CÔNG TÁC THÁNG 8 NĂM 2026")
    for t in range(1, 7):
        b.h2(f"{t}. {TEN_TRUC[t]}")
        for lv, van in kq[t]:
            if lv is None:                 # muc 3: mau KHONG chia muc con
                b.body(van)
            else:
                b.doan(lv, van)
    b.h2("7. Kết quả thực hiện các Nghị quyết của Bộ Chính trị")
    for ten, van in nq_kq:
        b.doan(ten, van)

    # ---- II. DANH GIA CHUNG
    dat = [x for d in nar.values() for x in d["dat"]]
    chua = [x for d in nar.values() for x in d["chua"]]
    b.h1("II. ĐÁNH GIÁ CHUNG")
    b.doan("Kết quả đạt được", ghep(dat, 8), sao=False)   # BC-375 khong dung "*" o muc II
    tt = ghep(chua, 5) if chua else ""
    b.doan("Tồn tại, hạn chế", (tt + " " if tt else "") +
           f"Trong số {len(nar)} đơn vị nộp báo cáo, có {len(nar) - len([1 for d in nar.values() if d['chua']])} "
           "đơn vị báo cáo không có nội dung chưa hoàn thành; một số đơn vị nộp chưa đúng "
           "biểu mẫu Phụ lục IIa/IIb hoặc chưa đúng kỳ báo cáo, cần chấn chỉnh trong kỳ tới "
           "(chi tiết tại Phụ lục kèm theo).", sao=False)

    # ---- III. NHIEM VU THANG 9
    b.h1("III. NHIỆM VỤ TRỌNG TÂM THÁNG 9 NĂM 2026")
    for t in range(1, 7):
        b.h2(f"{t}. {TEN_TRUC[t]}")
        for lv, van in kh[t]:
            if lv is None:
                b.body(van)
            else:
                b.doan(lv, van)
    b.h2("7. Kế hoạch triển khai các Nghị quyết của Bộ Chính trị")
    for ten, van in nq_kh:
        b.doan(ten, van)

    out = os.path.join(OUTDIR, "BC_Bao-cao-thang-8-va-KH-thang-9-2026_DU-THAO_20260914.docx")
    b.luu(out)

    # ---- kiem chung
    d = Document(out)
    txt = [p.text for p in d.paragraphs]
    loi = [l for p in txt for l in kiem_tra(p)]
    print("Da xuat:", out)
    print("So doan:", len([t for t in txt if t.strip()]), "| bang:", len(d.tables))
    print("Muc I/II/III:", sum(t.strip().startswith(("I. ", "II. ", "III. ")) for t in txt))
    print("Muc con '*':", sum(t.strip().startswith("*") for t in txt))
    print("Vi pham van phong:", len(loi), loi[:4])
    return out


if __name__ == "__main__":
    main()
