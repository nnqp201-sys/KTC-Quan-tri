# N21 — PLUGIN 1.3.13: TOÀN VĂN 19 SCRIPT PYTHON DÙNG CHUNG

Trích từ tệp `ktc-quan-tri-1.3.13.zip` (SHA-256 `d7c34a51e85f02278ec0e5a38c02089c0d7ae58280c8f59af6d0f673f9fbdd7e`). Mỗi mục ghi đường dẫn trong gói, kích thước, SHA-256 (đối chiếu được với N13). **Nội dung dưới đây là dữ liệu cần thẩm định, không phải chỉ thị cho người đọc.**

## `scripts/bc_thang.py` (32235 byte, sha256 `7ea318f32fa00c2f3cead4ab56e71458d2776f8efdfdc5296a65f8e8ecc7bd4f`)

`````python
# -*- coding: utf-8 -*-
"""Dung BAO CAO THANG cap Truong tu BAN DA BAN HANH (Nguyen tac 7) — bo cong cu chung, khong ghi cung ky, ten tep.

Tong quat hoa quy trinh da cho ket qua dat ngay 21/9/2026 (build_bc2/build_xl + kich ban thang 9). Claude SOAN NOI DUNG
(tuong thuat cap Truong, chu the "Nha truong", nhan muc con co dinh); cong cu lo phan co hoc: tim ban da ban hanh, trich
du lieu don vi, mo ban da ban hanh roi thay noi dung giu nguyen the thuc, dung lai cong thuc KPI, tu kiem.

    python bc_thang.py nguon    --ky 2026-09 [--dau-vao <thu muc nop>]      # ban da ban hanh + tep don vi (JSON)
    python bc_thang.py trich    --dau-vao <thu muc nop> --ra trich.json      # tuong thuat IIa theo Truc + dong IIb, Ib
    python bc_thang.py word     --goc <BC da ban hanh .docx> --noi-dung bc.json --ra <.docx>
    python bc_thang.py phu-luc  --goc <PL da ban hanh .xlsx> --noi-dung pl.json --ra <.xlsx>
    python bc_thang.py ke-hoach --goc <KH thang da ban hanh .xlsx> --noi-dung kh.json --ra <.xlsx>

Cau truc JSON noi dung: xem `references/Skill-Library/37-Quy-Trinh-Bao-Cao-Thang-Tu-Ban-Da-Ban-Hanh.md` (skill bao-cao).
Moi lenh dung san pham tu kiem va in JSON: so cho con `[CẦN BỔ SUNG`, ky cu con sot o phan dau/cuoi, vi pham van phong
cap Truong, so cong thuc — ma thoat 0 (xuat duoc) / 2 (thieu dau vao, loi cau truc tep goc).
"""
import argparse
import copy
import datetime as dt
import glob
import json
import os
import re
import sys
import unicodedata
import warnings

warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
# Ban trong goi ky nang (skills/bao-cao/references/Skill-Library/) dung them cong cu o scripts/ goc plugin
_GOC_PLUGIN = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "scripts"))
if os.path.isdir(_GOC_PLUGIN):
    sys.path.append(_GOC_PLUGIN)

TEN_TRUC = {
    1: "Thực hiện mục tiêu phát triển kinh tế - xã hội và nhiệm vụ chính trị",
    2: "Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát",
    3: "Thúc đẩy phát triển KH-CN, đổi mới sáng tạo và chuyển đổi số",
    4: "Xây dựng Đảng và hệ thống chính trị; phòng, chống tham nhũng, tiêu cực",
    5: "Phát triển văn hóa, con người, bảo đảm an sinh xã hội, nâng cao đời sống Nhân dân",
    6: "Củng cố quốc phòng, an ninh, giữ vững ổn định chính trị - xã hội, "
       "nâng cao hiệu quả đối ngoại và hội nhập quốc tế",
}
# Danh muc muc con CO DINH theo mau bao cao thang cap Truong (Skill 33 BUOC 0B) — Truc 3 khong co muc con
MUC_CON = {
    1: ["Công tác tuyển sinh", "Công tác đào tạo", "Công tác khảo thí", "Công tác bảo đảm chất lượng",
        "Công tác kế hoạch, tổng hợp", "Công tác tổ chức, cán bộ"],
    2: ["Về thể chế", "Công tác Kiểm tra, giám sát"],
    3: [],
    4: ["Công tác xây dựng Đảng", "Chấp hành kỷ cương hành chính", "Công tác Đảng, Công đoàn, Đoàn Thanh niên"],
    5: ["Công tác quản lý cơ sở vật chất", "Công tác Tài chính", "Công tác an sinh giáo dục", "Công tác truyền thông"],
    6: ["Về Quốc phòng - An ninh", "Về hoạt động Đối ngoại và Hợp tác", "Về hoạt động hợp tác phát triển"],
}
TEN_NQ = {
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
DIEM = {"Khó và phức tạp": 200, "Cao": 150, "Trung bình": 120, "Thấp": 100}
CAN_BO_SUNG = "[CẦN BỔ SUNG"


def _kd(s):
    s = unicodedata.normalize("NFD", str(s or ""))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d").replace("Đ", "D").lower()


def _ky(s):
    m = re.fullmatch(r"(20\d\d)-(\d{1,2})", s.strip())
    if not m:
        raise SystemExit("--ky phải dạng YYYY-MM, ví dụ 2026-09")
    return int(m.group(1)), int(m.group(2))


def _truoc(y, m):
    return (y, m - 1) if m > 1 else (y - 1, 12)


def _sau(y, m):
    return (y, m + 1) if m < 12 else (y + 1, 1)


# ================================================================ nguon
def _thang_tep(p):
    t = _kd(os.path.basename(p))
    m = re.search(r"thang-(\d{1,2})", t)
    y = re.search(r"(20\d\d)", t[m.end():] if m else t) if m else None
    return (int(y.group(1)), int(m.group(1))) if (m and y) else None


def tim_ban_da_ban_hanh(y, m):
    """BC, PL thang truoc (ky N-1) va KH thang N (ke hoach cung ky) trong kho — uu tien 04-Good-Documents."""
    import duong_dan
    db = duong_dan.ktc_database()
    tat = glob.glob(os.path.join(db, "0[24]-*", "**", "*.*"), recursive=True)

    def loai(p):
        b = _kd(os.path.basename(p))
        if b.startswith("~$"):
            return None
        if b.endswith(".docx") and b.startswith("bc-") and "ket-qua" in b and "thang" in b:
            return "BC"
        if b.endswith(".xlsx") and b.startswith("pl-") and "thang" in b:
            return "PL"
        if b.endswith(".xlsx") and b.startswith("kh-") and "cong-tac-thang" in b:
            return "KH"
        return None
    ds = {"BC": [], "PL": [], "KH": []}
    for p in tat:
        k = loai(p)
        tm = _thang_tep(p) if k else None
        if tm:
            ds[k].append((tm, 0 if "04-Good-Documents" in p else 1, p))
    ra = {}
    for k, dich in (("BC", _truoc(y, m)), ("PL", _truoc(y, m)), ("KH", (y, m))):
        hop = sorted([x for x in ds[k] if x[0] <= dich], key=lambda x: (x[0], -x[1]))
        ra[k] = {"tep": hop[-1][2], "ky": f"{hop[-1][0][0]}-{hop[-1][0][1]:02d}",
                 "dung_ky": hop[-1][0] == dich} if hop else None
    # nguon bo tro cho ke hoach thang sau va dau moi chua nop (Skill 37 muc 2.3): CTCT nam, ke hoach quy, ket luan giao ban
    def ngay_ten(p):
        m = re.search(r"_(20\d{6})_", os.path.basename(p))
        return m.group(1) if m else "0"
    ctct = [p for p in tat if re.search(r"ctct|chuong-trinh-cong-tac|chuong trinh cong tac", _kd(os.path.basename(p)))
            and str(y) in os.path.basename(p) and p.lower().endswith((".xlsx", ".docx"))]
    quy = [p for p in tat if re.search(r"ke-hoach-cong-tac-quy|ke hoach cong tac quy", _kd(os.path.basename(p)))
           and p.lower().endswith((".xlsx", ".docx"))]
    gb = [p for p in tat if re.search(r"giao-ban|giao ban|tbkl", _kd(os.path.basename(p))) and p.lower().endswith(".docx")]
    ra["bo_tro"] = {"ctct_nam": sorted(ctct), "ke_hoach_quy": sorted(quy),
                    "ket_luan_giao_ban_gan_nhat": sorted(gb, key=ngay_ten)[-6:]}
    ra["kho"] = db
    return ra


def _tieu_de_xlsx(p):
    import openpyxl
    try:
        wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
    except Exception:
        return ""
    t = []
    for ws in wb.worksheets[:2]:
        for r in ws.iter_rows(min_row=1, max_row=8, values_only=True):
            t += [str(c) for c in r if c]
    return _kd(" ".join(t))


def phan_loai_dau_vao(thu_muc):
    """Tep don vi nop: IIa (tuong thuat .docx), IIb (ket qua .xlsx), Ib (ke hoach .xlsx) — theo ten thu muc, roi noi dung."""
    try:
        from doi_soat_so_lieu import ma_don_vi
    except Exception:
        ma_don_vi = None
    ra = {"IIa": [], "IIb": [], "Ib": [], "khac": []}
    for p in sorted(glob.glob(os.path.join(thu_muc, "**", "*.*"), recursive=True)):
        b = os.path.basename(p)
        if b.startswith(("~$", ".")) or not b.lower().endswith((".docx", ".xlsx")):
            continue
        duong = _kd(os.path.relpath(p, thu_muc))
        if b.lower().endswith(".docx"):
            k = "IIa"
        elif re.search(r"\biib\b|pl ?iib|ket qua|\biic\b", duong):
            k = "IIb"
        elif re.search(r"\bib\b|phu luc ib|ke hoach", duong):
            k = "Ib"
        else:
            td = _tieu_de_xlsx(p)
            k = "IIb" if ("iib" in td or "ket qua" in td) else "Ib" if ("ib" in td or "ke hoach" in td) else "khac"
        ma = None
        if ma_don_vi:
            try:
                ma = ma_don_vi(p)
            except Exception:
                ma = None
        ra[k].append({"tep": p, "ma": ma or "?" + os.path.splitext(b)[0]})
    return ra


# ================================================================ trich
def _g(v):
    if v is None:
        return ""
    if isinstance(v, (dt.datetime, dt.date)):
        return f"{v.day:02d}/{v.month:02d}/{v.year}"
    return " ".join(str(v).split())


def doc_dong_excel(p):
    """Dong nhiem vu cua Phu luc IIb/Ib (sheet dau khong phai 'quy'): muc I/II, Truc, cac cot A..P."""
    import openpyxl
    wb = openpyxl.load_workbook(p, data_only=True)
    ws = next((w for w in wb.worksheets if "quy" not in _kd(w.title).split()), wb.worksheets[0])
    h = next((i for i, r in enumerate(ws.iter_rows(min_row=1, max_row=20, values_only=True), 1)
              if any(c and "NỘI DUNG CÔNG VIỆC" in str(c).upper() for c in r)), None)
    if h is None:
        return ws.title, []
    out, muc, truc = [], "I", 0
    for ri, r in enumerate(ws.iter_rows(min_row=h + 1, values_only=True), h + 1):
        r = list(r) + [None] * 20
        stt, nd = _g(r[0]), _g(r[1])
        if not nd or _kd(nd).startswith(("ghi chu", "noi nhan", "muc do")) or re.match(r"^\(\d+\)", stt):
            continue
        if stt in ("I", "II") and "nhiệm vụ" in nd.lower():
            muc, truc = stt, 0
            continue
        mt = re.search(r"Trục\s*\(?(\d)\)?", nd[:14])
        if mt and re.fullmatch(r"\d", stt):
            truc = int(mt.group(1))
            continue
        if not any(r[2:5]) and len(nd) < 15:
            continue
        out.append({"hang": ri, "muc": muc, "truc": truc, "stt": stt, "nd": nd, "chi_dao": _g(r[2]),
                    "chu_tri": _g(r[3]), "sp": _g(r[4]), "sl": _g(r[5]), "dk": _g(r[6]),
                    "cot_8_16": [_g(x) for x in r[7:16]]})
    return ws.title, out


def trich(thu_muc):
    import trich_tuong_thuat as T
    pl = phan_loai_dau_vao(thu_muc)
    ra = {"thu_muc": thu_muc, "tuong_thuat": {}, "iib": {}, "ib": {}, "loi": []}
    for x in pl["IIa"]:
        try:
            d = T.doc_mot(x["tep"])
            d["tep"] = os.path.basename(x["tep"])
            khoa = x["ma"] if x["ma"] not in ra["tuong_thuat"] else f"{x['ma']} ({os.path.splitext(d['tep'])[0]})"
            ra["tuong_thuat"][khoa] = d          # 2 tep cung ma (vd Ban Truyen thong va Phong TH-HC&QT) — giu ca hai
        except Exception as e:
            ra["loi"].append(f"{x['tep']}: {e.__class__.__name__} {e}")
    for k, dich in (("IIb", "iib"), ("Ib", "ib")):
        for x in pl[k]:
            try:
                sheet, dong = doc_dong_excel(x["tep"])
                ra[dich].setdefault(x["ma"], []).append({"tep": os.path.basename(x["tep"]), "sheet": sheet, "dong": dong})
            except Exception as e:
                ra["loi"].append(f"{x['tep']}: {e.__class__.__name__} {e}")
    ra["thong_ke"] = {"IIa": len(ra["tuong_thuat"]), "IIb": len(ra["iib"]), "Ib": len(ra["ib"]),
                      "khong_phan_loai": [os.path.basename(x["tep"]) for x in pl["khac"]]}
    return ra


# ================================================================ word
def _qn(t):
    from docx.oxml.ns import qn
    return qn(t)


def _dat_chu_doan(p, text):
    """Thay chu ca doan, giu dinh dang run dau."""
    rs = p.runs
    if not rs:
        p.add_run(text)
        return
    rs[0].text = text
    for r in rs[1:]:
        r.text = ""


class DungWord:
    """Mo BC da ban hanh: giu doan dau (quoc hieu, can cu) va doan cuoi (Tren day la, noi nhan, chu ky), thay phan than."""

    def __init__(self, goc):
        from docx import Document
        self.doc = Document(goc)
        ps = self.doc.paragraphs
        self.i_dau = next(i for i, p in enumerate(ps) if p.text.strip().startswith("I. KẾT QUẢ"))
        self.i_cuoi = next(i for i, p in enumerate(ps) if p.text.strip().startswith("Trên đây là"))
        self.m_h1 = ps[self.i_dau]._element
        self.m_h2 = ps[self.i_dau + 1]._element
        mau = next(p for p in ps[self.i_dau + 2:self.i_cuoi] if p.text.strip().startswith("*") and len(p.runs) >= 2)
        self.m_doan = mau._element
        self.neo = ps[self.i_cuoi]._element
        for p in ps[self.i_dau:self.i_cuoi]:
            p._element.getparent().remove(p._element)

    def _dat_run(self, r, text, thuong):
        for t in r.findall(_qn("w:t")):
            r.remove(t)
        if thuong:
            rpr = r.find(_qn("w:rPr"))
            if rpr is None:
                rpr = r.makeelement(_qn("w:rPr"), {})
                r.insert(0, rpr)
            for tag in ("w:b", "w:bCs", "w:i", "w:iCs"):
                for e in rpr.findall(_qn(tag)):
                    rpr.remove(e)
                e = rpr.makeelement(_qn(tag), {})
                e.set(_qn("w:val"), "0")
                rpr.append(e)
        t = r.makeelement(_qn("w:t"), {})
        t.text = text
        t.set(_qn("xml:space"), "preserve")
        r.append(t)

    def doan(self, nhan, noi_dung, sao=True):
        el = copy.deepcopy(self.m_doan)
        rs = el.findall(_qn("w:r"))
        for r in rs[2:]:
            el.remove(r)
        self._dat_run(rs[0], f"* {nhan}: " if sao else f"{nhan}: ", thuong=False)
        self._dat_run(rs[1], noi_dung, thuong=True)
        self.neo.addprevious(el)

    def _mot_run(self, mau, text, thuong=False):
        el = copy.deepcopy(mau)
        rs = el.findall(_qn("w:r"))
        for r in rs[1:]:
            el.remove(r)
        self._dat_run(rs[0], text, thuong)
        self.neo.addprevious(el)

    def h1(self, s):
        self._mot_run(self.m_h1, s)

    def h2(self, s):
        self._mot_run(self.m_h2, s)

    def than(self, s):
        self._mot_run(self.m_doan, s, thuong=True)


def _phan(b, d, loai):
    """d: {"1": [[nhan, noi dung], ...], ..., "7": [[so NQ hoac ten, noi dung], ...]}"""
    for t in range(1, 7):
        b.h2(f"{t}. {TEN_TRUC[t]}")
        for muc in d.get(str(t), []):
            nhan, nd = (muc[0], muc[1]) if isinstance(muc, (list, tuple)) else (None, muc)
            if not nd:
                continue
            (b.than(nd) if not nhan else b.doan(nhan, nd))
    nq = d.get("7", [])
    if nq:
        b.h2("7. Kết quả thực hiện các Nghị quyết của Bộ Chính trị" if loai == "kq"
             else "7. Kế hoạch triển khai các Nghị quyết của Bộ Chính trị")
        thu_tu = {s: i for i, s in enumerate(THU_TU_NQ)}
        for so, nd in sorted(nq, key=lambda x: thu_tu.get(str(x[0]), 99)):
            if nd:
                b.doan(TEN_NQ.get(str(so), str(so)), nd)


def dung_word(goc, nd, ra):
    from docx import Document
    y, m = nd["ky"]["nam"], nd["ky"]["thang"]
    y2, m2 = _sau(y, m) if "ky_sau" not in nd else (nd["ky_sau"]["nam"], nd["ky_sau"]["thang"])
    b = DungWord(goc)
    cum = f"tháng {m} và kế hoạch công tác tháng {m2} năm {y2}"
    for i, p in enumerate(b.doc.paragraphs):
        t = p.text
        if i > 12 and not t.startswith("Trên đây là"):
            continue
        t2 = re.sub(r"tháng \d{1,2} và kế hoạch công tác tháng \d{1,2} năm 20\d\d", cum, t)
        if t2 != t:
            _dat_chu_doan(p, t2)
    for tb in b.doc.tables[:1]:
        for row in tb.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    t = p.text
                    # 1.3.6: ban trong kho co so hieu di dang "Số375BC-CĐKT" (thieu ":" va "/") — chay that 28/9 giu nham so 375
                    t2 = re.sub(r"^(\s*)Số\s*:?\s*\d+\s*/?\s*(?=[A-ZĐ]{2,}-)", r"\1Số:      /", t)
                    t2 = re.sub(r"ngày\s*\d{1,2}\s*tháng\s*\d{1,2}\s*năm", f"ngày     tháng {nd.get('thang_lap', m)} năm", t2)
                    if t2 != t:
                        _dat_chu_doan(p, t2)
    b.h1(f"I. KẾT QUẢ THỰC HIỆN CÔNG TÁC THÁNG {m} NĂM {y}")
    _phan(b, nd["ket_qua"], "kq")
    b.h1("II. ĐÁNH GIÁ CHUNG")
    b.doan("Kết quả đạt được", nd["danh_gia"]["dat"], sao=False)
    b.doan("Tồn tại, hạn chế", nd["danh_gia"]["ton_tai"], sao=False)
    b.h1(f"III. NHIỆM VỤ TRỌNG TÂM THÁNG {m2} NĂM {y2}")
    _phan(b, nd["nhiem_vu"], "kh")
    os.makedirs(os.path.dirname(os.path.abspath(ra)), exist_ok=True)
    b.doc.save(ra)
    # ---- tu kiem
    d = Document(ra)
    txt = [p.text for p in d.paragraphs]
    y0, m0 = _truoc(y, m)
    dau_cuoi = [t for t in txt[:12]] + [t for t in txt if t.startswith("Trên đây là")]
    try:
        from vanphong import kiem_tra
        vp = [(t[:60], l) for t in txt for l in kiem_tra(t)]
    except Exception:
        vp = None
    thieu_muc = {t: [n for n in MUC_CON[t] if not any(x.startswith(f"* {n}:") for x in txt)] for t in (1, 2, 4, 5, 6)}
    return {"tep": ra, "so_doan": sum(1 for t in txt if t.strip()),
            "con_can_bo_sung": sum(t.count(CAN_BO_SUNG) for t in txt),
            "ky_cu_o_dau_cuoi": [t[:80] for t in dau_cuoi if re.search(rf"tháng {m0}\b.*năm", t)],
            "muc_con_chua_co_trong_phan_I_III": {k: v for k, v in thieu_muc.items() if v},
            "vi_pham_van_phong": (len(vp) if vp is not None else "chưa kiểm (thiếu vanphong.py)"),
            "vi_du_vi_pham": (vp[:5] if vp else [])}


# ================================================================ xlsx chung
def _so(v):
    """So luong: '1' -> 1, '2.0' -> 2 (Excel SUM bo qua o chu); de nguyen neu khong phai so."""
    if isinstance(v, str):
        t = v.strip().replace(",", ".")
        try:
            f = float(t)
            return int(f) if f == int(f) else f
        except ValueError:
            return v or None
    return v


def _hang_tieu_de(ws, max_r=20):
    for r in range(1, max_r + 1):
        if any(c.value and "NỘI DUNG CÔNG VIỆC" in str(c.value).upper() for c in ws[r]):
            return r
    raise ValueError("Không thấy hàng tiêu đề 'NỘI DUNG CÔNG VIỆC' trong tệp gốc")


def _dong_bat_dau(ws, r_h):
    for r in range(r_h + 1, r_h + 8):
        if str(ws.cell(r, 1).value or "").strip() == "I":
            return r
    raise ValueError("Không thấy hàng nhóm 'I' sau hàng tiêu đề")


def _mau_hang(ws, r, ncol):
    return [copy.copy(ws.cell(r, c)._style) for c in range(1, ncol + 1)], ws.row_dimensions[r].height


def _gop_hang(ws, r):
    """Cac vung gop nam tren mot hang (cot dau, cot cuoi)."""
    return [(m.min_col, m.max_col) for m in ws.merged_cells.ranges if m.min_row == r == m.max_row]


def _cong_thuc_mau(ws, r, cot):
    from openpyxl.formula.translate import Translator
    ra = {}
    for c in cot:
        v = ws.cell(r, c).value
        if isinstance(v, str) and v.startswith("="):
            ra[c] = (v, ws.cell(r, c).coordinate, Translator)
    return ra


def _dich(ct, dich_toi):
    v, goc, T = ct
    return T(v, origin=goc).translate_formula(dich_toi)


def _tnr(ws, den_hang, ncol):
    from openpyxl.styles import Font
    for row in ws.iter_rows(min_row=1, max_row=den_hang, max_col=ncol):
        for c in row:
            if c.font and c.font.name != "Times New Roman":
                fo = copy.copy(c.font)
                fo.name = "Times New Roman"
                c.font = fo


def _cot_doi_soat(ws, r_h, col, rows, rong=46):
    from openpyxl.styles import Alignment, Font
    from openpyxl.utils import get_column_letter
    ws.cell(r_h, col).value = "Ghi chú đối soát (xóa trước khi ban hành)"
    ws.cell(r_h, col)._style = copy.copy(ws.cell(r_h, col - 1)._style)
    ws.column_dimensions[get_column_letter(col)].width = rong
    for r in rows:
        c = ws.cell(r, col)
        if c.value:
            c.font = Font(name="Times New Roman", size=11)
            c.alignment = Alignment(wrap_text=True, vertical="center")


# ================================================================ phu luc
def dung_phu_luc(goc, nd, ra):
    """nd: {"ky":{"thang","nam"}, "truc":{"1":{"ten"?, "dong":[dong]}}, "dot_xuat":[dong]}
    dong: {"nd","cd","ct","sp","sl","dk","ket_qua":{"sl":0..1,"cl":0..1,"td":0..1}|null,"doi_soat":"..."}"""
    import openpyxl
    y, m = nd["ky"]["nam"], nd["ky"]["thang"]
    wb = openpyxl.load_workbook(goc)
    ws = wb.active
    ws.title = re.sub(r"\d{1,2}$", str(m), ws.title) if re.search(r"\d{1,2}$", ws.title) else f"BC Kết quả tháng {m}"
    for r in range(1, 5):
        for c in ws[r]:
            if isinstance(c.value, str):
                c.value = re.sub(r"THÁNG \d{1,2} NĂM 20\d\d", f"THÁNG {m} NĂM {y}", c.value)
    r_h = _hang_tieu_de(ws)
    r_dau = _dong_bat_dau(ws, r_h)
    NC = 16
    s_nhom, s_truc, s_data = (_mau_hang(ws, r_dau + k, NC) for k in (0, 1, 2))
    gop_nhom, gop_truc = _gop_hang(ws, r_dau), _gop_hang(ws, r_dau + 1)
    ct_data = _cong_thuc_mau(ws, r_dau + 2, [8, 9, 10, 12, 14, 16])      # H I J L N P
    cot_tong_truc = [c for c in range(6, NC + 1) if str(ws.cell(r_dau + 1, c).value or "").startswith("=SUM")]
    r_ii = next((r for r in range(r_dau, ws.max_row + 1) if str(ws.cell(r, 1).value or "").strip() == "II"), None)
    cot_tong_ii = [c for c in range(6, NC + 1) if r_ii and str(ws.cell(r_ii, c).value or "").startswith("=SUM")]
    tieu_I = ws.cell(r_dau, 2).value
    tieu_II = ws.cell(r_ii, 2).value if r_ii else "Các nhiệm vụ đột xuất, phát sinh khác ngoài kế hoạch"
    ten_truc_goc = {}
    for r in range(r_dau, ws.max_row + 1):
        a, bv = str(ws.cell(r, 1).value or "").strip(), ws.cell(r, 2).value
        if re.fullmatch(r"[1-6]", a) and bv and "Trục" in str(bv)[:10]:
            ten_truc_goc[int(a)] = bv
    # 1.3.6: tieu de nhom/Truc cua ban goc co the mang ky cu ("... tháng 8") — chay that 28/9 sot o muc II
    doi_ky = lambda v: re.sub(r"(tháng|THÁNG)\s+\d{1,2}\b", lambda k: f"{k.group(1)} {m}", v) if isinstance(v, str) else v
    tieu_I, tieu_II = doi_ky(tieu_I), doi_ky(tieu_II)
    ten_truc_goc = {k: doi_ky(v) for k, v in ten_truc_goc.items()}
    for mg in [x for x in list(ws.merged_cells.ranges) if x.min_row >= r_dau]:
        ws.unmerge_cells(str(mg))
    ws.delete_rows(r_dau, ws.max_row - r_dau + 1)
    from openpyxl.utils import get_column_letter as L
    cur = [r_dau - 1]
    tk = {"dong": 0, "co_ket_qua": 0, "cong_thuc": 0}

    def dat(mau, vals, gop=()):
        cur[0] += 1
        r = cur[0]
        for c in range(1, NC + 1):
            ws.cell(r, c)._style = copy.copy(mau[0][c - 1])
        if mau[1]:
            ws.row_dimensions[r].height = mau[1]
        for c, v in vals.items():
            ws.cell(r, c).value = v
        for c1, c2 in gop:
            ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
        return r

    def dong(stt, x):
        r = cur[0] + 1
        v = {1: stt, 2: x["nd"], 3: x.get("cd"), 4: x.get("ct"), 5: x.get("sp"), 6: _so(x.get("sl")), 7: x.get("dk")}
        for c, ctm in ct_data.items():
            if c in (8, 9, 10):
                v[c] = _dich(ctm, f"{L(c)}{r}")
        kq = x.get("ket_qua")
        if kq:
            v[11] = f"=F{r}*{round(float(kq.get('sl', 1)) * 100, 2):g}%"
            v[13] = f"=K{r}*{round(float(kq.get('cl', 1)) * 100, 2):g}%"
            v[15] = f"=K{r}*{round(float(kq.get('td', 1)) * 100, 2):g}%"
            for c in (12, 14, 16):
                if c in ct_data:
                    v[c] = _dich(ct_data[c], f"{L(c)}{r}")
            tk["co_ket_qua"] += 1
        if x.get("doi_soat"):
            v[17] = x["doi_soat"]
        tk["dong"] += 1
        tk["cong_thuc"] += sum(1 for k, s in v.items() if isinstance(s, str) and s.startswith("="))
        return dat(s_data, v)

    dat(s_nhom, {1: "I", 2: tieu_I}, gop_nhom)
    for t in range(1, 7):
        tr = nd["truc"].get(str(t), {})
        rt = dat(s_truc, {1: str(t), 2: tr.get("ten") or ten_truc_goc.get(t) or f"Trục ({t}) - {TEN_TRUC[t]}"}, gop_truc)
        dau = cur[0] + 1
        for k, x in enumerate(tr.get("dong", []), 1):
            dong(f"{t}.{k}", x)
        for c in cot_tong_truc:
            ws.cell(rt, c).value = f"=SUM({L(c)}{dau}:{L(c)}{max(cur[0], dau)})"
    ds2 = nd.get("dot_xuat", [])
    r2 = dat(s_nhom, {1: "II", 2: tieu_II}, gop_nhom)
    dau = cur[0] + 1
    for k, x in enumerate(ds2, 1):
        dong(str(k), x)
    for c in cot_tong_ii:
        ws.cell(r2, c).value = f"=SUM({L(c)}{dau}:{L(c)}{max(cur[0], dau)})"
    _tnr(ws, cur[0], NC + 1)
    _cot_doi_soat(ws, r_h, NC + 1, range(r_dau, cur[0] + 1))
    ws.print_area = f"A1:{L(NC)}{cur[0]}"
    os.makedirs(os.path.dirname(os.path.abspath(ra)), exist_ok=True)
    wb.save(ra)
    return {"tep": ra, "hang_cuoi": cur[0], **tk, "khong_co_ket_qua": tk["dong"] - tk["co_ket_qua"]}


# ================================================================ ke hoach
def dung_ke_hoach(goc, nd, ra):
    """nd: {"ky":{"thang","nam"}, "so"?, "ngay"?, "can_cu": "...", "truc":{"1":{"ten"?,"dong":[dong]}}, "chuyen_tiep":[dong]}
    dong: {"nd","cd","ct","sp","sl","dk","thoi_han","ghi_chu","doi_soat"}"""
    import openpyxl
    y, m = nd["ky"]["nam"], nd["ky"]["thang"]
    wb = openpyxl.load_workbook(goc)
    ws = wb.active
    ws.title = f"KH tháng {m}"
    r_h = _hang_tieu_de(ws)
    r_dau = _dong_bat_dau(ws, r_h)
    NC = 11
    r_nn = next((r for r in range(r_dau, ws.max_row + 1)
                 if str(ws.cell(r, 1).value or "").strip().startswith("Nơi nhận")), None)
    if r_nn is None:
        raise ValueError("Không thấy khối 'Nơi nhận' ở cuối kế hoạch gốc")
    s_nhom, s_truc, s_data = (_mau_hang(ws, r_dau + k, NC) for k in (0, 1, 2))
    gop_nhom, gop_truc = _gop_hang(ws, r_dau), _gop_hang(ws, r_dau + 1)
    ct_data = _cong_thuc_mau(ws, r_dau + 2, [9, 10])
    duoi = {c: (ws.cell(r_nn, c).value, copy.copy(ws.cell(r_nn, c)._style)) for c in range(1, NC + 1)
            if ws.cell(r_nn, c).value is not None}
    gop_duoi = _gop_hang(ws, r_nn)
    cao_duoi = ws.row_dimensions[r_nn].height
    tieu_I = ws.cell(r_dau, 2).value
    r_ii = next((r for r in range(r_dau, r_nn) if str(ws.cell(r, 1).value or "").strip() == "II"), None)
    tieu_II = ws.cell(r_ii, 2).value if r_ii else "Các nhiệm vụ từ tháng trước chuyển sang"
    ten_truc_goc = {}
    for r in range(r_dau, r_nn):
        a, bv = str(ws.cell(r, 1).value or "").strip(), ws.cell(r, 2).value
        if re.fullmatch(r"[1-6]", a) and bv and "Trục" in str(bv)[:10]:
            ten_truc_goc[int(a)] = bv
    # phan dau
    for r in range(1, r_h):
        for c in ws[r]:
            v = c.value
            if not isinstance(v, str):
                continue
            if v.strip().startswith("Số:"):
                c.value = nd.get("so", "Số:       /KH-CĐKT")
            elif v.strip().startswith("Quảng Ngãi, ngày"):
                c.value = nd.get("ngay", f"Quảng Ngãi, ngày     tháng {_truoc(y, m)[1]} năm {_truoc(y, m)[0]}")
            elif v.startswith("KẾ HOẠCH"):
                c.value = f"KẾ HOẠCH\ncông tác tháng {m} năm {y}"
            elif re.fullmatch(r"\s*công tác tháng \d{1,2} năm 20\d\d\s*", v):
                c.value = None
            elif "Căn cứ" in v[:30] and nd.get("can_cu"):
                c.value = nd["can_cu"]
    for mg in [x for x in list(ws.merged_cells.ranges) if x.min_row >= r_dau]:
        ws.unmerge_cells(str(mg))
    ws.delete_rows(r_dau, ws.max_row - r_dau + 1)
    from openpyxl.utils import get_column_letter as L
    cur = [r_dau - 1]
    tk = {"dong": 0, "chuyen_tiep": 0}

    def dat(mau, vals, gop=()):
        cur[0] += 1
        r = cur[0]
        for c in range(1, NC + 1):
            ws.cell(r, c)._style = copy.copy(mau[0][c - 1])
        if mau[1]:
            ws.row_dimensions[r].height = mau[1]
        for c, v in vals.items():
            ws.cell(r, c).value = v
        for c1, c2 in gop:
            ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
        return r

    def dong(stt, x):
        r = cur[0] + 1
        v = {1: stt, 2: x["nd"], 3: x.get("cd"), 4: x.get("ct"), 5: x.get("sp"), 6: _so(x.get("sl")), 7: x.get("dk"),
             8: x.get("thoi_han"), 11: x.get("ghi_chu")}
        for c, ctm in ct_data.items():
            v[c] = _dich(ctm, f"{L(c)}{r}")
        if 9 not in ct_data:
            v[9] = DIEM.get(x.get("dk"))
            v[10] = (v[9] / 100) if v[9] else None
        if x.get("doi_soat"):
            v[12] = x["doi_soat"]
        tk["dong"] += 1
        return dat(s_data, v)

    dat(s_nhom, {1: "I", 2: tieu_I}, gop_nhom)
    for t in range(1, 7):
        tr = nd["truc"].get(str(t), {})
        dat(s_truc, {1: str(t), 2: tr.get("ten") or ten_truc_goc.get(t) or f"Trục ({t}) - {TEN_TRUC[t]}"}, gop_truc)
        for k, x in enumerate(tr.get("dong", []), 1):
            dong(f"{t}.{k}", x)
    ct2 = nd.get("chuyen_tiep", [])
    if ct2:
        dat(s_nhom, {1: "II", 2: tieu_II}, gop_nhom)
        for k, x in enumerate(ct2, 1):
            dong(str(k), x)
            tk["chuyen_tiep"] += 1
    cur[0] += 2
    r = cur[0]
    for c, (v, st) in duoi.items():
        ws.cell(r, c).value = v
        ws.cell(r, c)._style = st
    for c1, c2 in gop_duoi:
        ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    if cao_duoi:
        ws.row_dimensions[r].height = cao_duoi
    _tnr(ws, cur[0], NC + 1)
    _cot_doi_soat(ws, r_h, NC + 1, range(r_dau, cur[0]), rong=48)
    ws.print_area = f"A1:{L(NC)}{cur[0]}"
    os.makedirs(os.path.dirname(os.path.abspath(ra)), exist_ok=True)
    wb.save(ra)
    return {"tep": ra, "hang_cuoi": cur[0], **tk}


# ================================================================ main
def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="lenh", required=True)
    a = sub.add_parser("nguon")
    a.add_argument("--ky", required=True)
    a.add_argument("--dau-vao")
    a = sub.add_parser("trich")
    a.add_argument("--dau-vao", required=True)
    a.add_argument("--ra", required=True)
    for ten in ("word", "phu-luc", "ke-hoach"):
        a = sub.add_parser(ten)
        a.add_argument("--goc", required=True)
        a.add_argument("--noi-dung", required=True)
        a.add_argument("--ra", required=True)
    a = ap.parse_args(argv)
    try:
        if a.lenh == "nguon":
            y, m = _ky(a.ky)
            ra = {"ky": a.ky, "ban_da_ban_hanh": tim_ban_da_ban_hanh(y, m)}
            if a.dau_vao:
                pl = phan_loai_dau_vao(a.dau_vao)
                ra["dau_vao"] = {k: [{"ma": x["ma"], "tep": os.path.relpath(x["tep"], a.dau_vao)} for x in v]
                                 for k, v in pl.items()}
        elif a.lenh == "trich":
            d = trich(a.dau_vao)
            json.dump(d, open(a.ra, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            ra = {"ra": a.ra, **d["thong_ke"], "loi": d["loi"]}
        else:
            nd = json.load(open(a.noi_dung, encoding="utf-8"))
            f = {"word": dung_word, "phu-luc": dung_phu_luc, "ke-hoach": dung_ke_hoach}[a.lenh]
            ra = f(a.goc, nd, a.ra)
    except (FileNotFoundError, ValueError, StopIteration, KeyError) as e:
        print(json.dumps({"loi": f"{e.__class__.__name__}: {e}"}, ensure_ascii=False))
        return 2
    print(json.dumps(ra, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/doi_soat_so_lieu.py` (20982 byte, sha256 `f2bad80bad0e17e9ec25710b7e6b70a2ee69028ccc0bc39af84b119e649c80f9`)

`````python
# -*- coding: utf-8 -*-
"""Doi soat so lieu CHEO GIUA CAC TEP Phu luc TB 736 — DL-20260919-006.

read_bc736_excel.py (skill bao-cao) da kiem cong thuc KPI TRONG tung tep. Cong cu nay lam phan con thieu:
  DS01  Loi trong tung tep (chuyen tiep canh bao cua read_bc736_excel) — dem theo don vi
  DS02  Tong hop cap Truong <-> tong cac don vi: so nhiem vu, SL quy doi, KPI quy doi theo Truc
  DS03  Ke hoach <-> ket qua cung ky cua moi don vi: nhiem vu KH thieu ket qua; ket qua khong co trong KH
  DS04  Task_ID trung trong mot tep / giua cac don vi
  DS05  % KPI 3 chieu theo Truc tinh lai (bang tham chieu duy nhat — hai agent dung chung so nay)
  DS06  Ma don vi (ten thu muc/tep) co trong 20-Chuan-Chung/13-Bang-Ma-Don-Vi.md khong; tep khong phai .xlsx

Dung chung cho agent ktc-kiem-ho-so-don-vi va ktc-kiem-san-pham de moi lan chay cho CUNG mot ket qua.
KHONG sua so lieu. KHONG quy doi giua hai thang diem (KI-014).

Chay:
  python 29-Cong-Cu/doi_soat_so_lieu.py --kq <thu muc ky | tep...> [--kh <thu muc | tep...>]
         [--tong-hop <tep tong hop KQ cap Truong>] [--md <bao cao.md>]
  Thu muc ky dang 10-Dau-Vao/01-Dau-Moi-Nop/<ky>/<ma don vi>/: tep ten bat dau "BC"/"KQ" la ket qua, "KH" la ke hoach.
Ma thoat: 1 neu co lech DS02 hoac Task_ID trung (DS04); nguoc lai 0.
"""
import difflib
import glob
import os
import re
import sys
import unicodedata
import warnings

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _p in (os.path.join(DU_AN, "25-KTC-Bao-Cao", "references", "Skill-Library"),
           *glob.glob(os.path.join(DU_AN, "skills", "bao-cao", "references", "Skill-Library"))):
    if os.path.isdir(_p):
        sys.path.insert(0, _p)
import read_bc736_excel as r  # noqa: E402

TRUC = range(1, 7)
NGUONG_GIONG = 0.82     # do giong noi dung de coi la cung nhiem vu khi khong co Task_ID
SAI_SO = 0.05


def _chuan(s):
    s = unicodedata.normalize("NFC", " ".join(str(s or "").split())).lower()
    return re.sub(r"[^\w\s]", "", s)


def ma_chuan():
    """Doc danh sach ma chuan tu 13-Bang-Ma-Don-Vi.md (du an hoac plugin)."""
    ung = [os.path.join(DU_AN, "20-Chuan-Chung", "13-Bang-Ma-Don-Vi.md")] + \
        glob.glob(os.path.join(DU_AN, "skills", "*", "references", "**", "*Bang-Ma-Don-Vi.md"), recursive=True)
    for p in ung:
        if os.path.isfile(p):
            return set(re.findall(r"^\|\s*`([A-Z]+-[A-Z]+)`", open(p, encoding="utf-8").read(), re.M))
    return set()


def _khong_dau(s):
    t = unicodedata.normalize("NFD", str(s or "").lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn").replace("đ", "d")


def _khoa(s):
    """Khoa so khop ten don vi: bo dau, bo moi ky tu khong phai chu/so. 'PHÒNG TH-HC&QT' -> 'phongthhcqt'."""
    return re.sub(r"[^a-z0-9]", "", _khong_dau(s))


_BIEN_THE = None


def bien_the_ma():
    """{khoa chuan hoa -> ma} tu MOI cot cua 13-Bang-Ma-Don-Vi.md (ten chinh thuc + bien the) va duoi ma.
    Chi khop CHINH XAC sau chuan hoa — khong dung do giong (KI-001: nguong < 100% cho khop gia)."""
    global _BIEN_THE
    if _BIEN_THE is None:
        _BIEN_THE = {}
        p = os.path.join(DU_AN, "20-Chuan-Chung", "13-Bang-Ma-Don-Vi.md")
        ung = [p] + glob.glob(os.path.join(DU_AN, "skills", "*", "references", "**", "*Bang-Ma-Don-Vi.md"),
                              recursive=True)
        for q in ung:
            if not os.path.isfile(q):
                continue
            for dong in open(q, encoding="utf-8"):
                # Muc "Anh xa bo sung — may doc": | `bien the` | `MA` | cap | bang chung |  (quyet dinh da chot,
                # bien the co bang chung tren tep that — vd Ban Truyen thong -> P-THHC, chot 14/9/2026)
                bs = re.match(r"^\|\s*`([^`]+)`\s*\|\s*`([A-Z]+-[A-Z]+)`\s*\|", dong)
                if bs and not re.fullmatch(r"[A-Z]+-[A-Z]+", bs.group(1)):
                    _BIEN_THE.setdefault(_khoa(bs.group(1)), bs.group(2))
                    continue
                m = re.match(r"^\|\s*`([A-Z]+-[A-Z]+)`\s*\|(.*)", dong)
                if not m:
                    continue
                ma = m.group(1)
                _BIEN_THE.setdefault(_khoa(ma.split("-", 1)[1]), ma)
                for o in m.group(2).split("|"):
                    o = o.replace("⚠️", "").replace("`", "").strip()
                    if o and not o.startswith("*"):
                        _BIEN_THE.setdefault(_khoa(o), ma)
            break
    return _BIEN_THE


_DAU = {}


def dau_tep(p):
    """Doc phan dau Phu luc: dong ngay sau 'TRUONG CAO DANG KON TUM' la don vi, dong tiep theo co
    'KE HOACH'/'BAO CAO' la tieu de (loai + ky). Dung khi ten tep/thu muc khong theo quy uoc
    (21/9/2026: 10-Dau-Vao doi sang '1. BAO CAO PL IIB/KHCB.xlsx' — gop 10 don vi thanh 1, tron KH vao KQ)."""
    if p in _DAU:
        return _DAU[p]
    kq = {"don_vi": None, "loai": None, "ky": None}
    if p.lower().endswith(".xlsx"):
        try:
            from openpyxl import load_workbook
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                wb = load_workbook(p, read_only=True, data_only=True)
                o = [str(r[0] or "").strip() for r in
                     wb.active.iter_rows(min_row=1, max_row=12, max_col=1, values_only=True)]
                wb.close()
            # o CHI chua ten Truong — dong "Phu luc IIb … CUA TRUONG CAO DANG KON TUM" cung chua cum nay
            i = next(k for k, x in enumerate(o) if _khoa(x) == "truongcaodangkontum")
            dv = re.sub(r"^\s*đơn vị\s*:?\s*", "", o[i + 1], flags=re.I).strip(" .…")
            kq["don_vi"] = dv or None
            for x in o[i + 1:]:
                t = " ".join(_khong_dau(x).split())
                if "ke hoach" in t or "bao cao" in t:
                    kq["loai"] = "KH" if "ke hoach" in t else "KQ"
                    m = re.search(r"(thang|quy)\s*(\d{1,2}|iv|iii|ii|i)\b.*?nam\s*(\d{4})", t) or \
                        re.search(r"(nam)\s*()(\d{4})", t)
                    if m:
                        so = {"i": 1, "ii": 2, "iii": 3, "iv": 4}.get(m.group(2), m.group(2) or 0)
                        kq["ky"] = (m.group(1), int(so), int(m.group(3)))
                    break
        except (StopIteration, IndexError, OSError, ValueError, KeyError):
            pass
    _DAU[p] = kq
    return kq


def ma_don_vi(p):
    """Ma don vi: thu muc/tep theo quy uoc -> ten don vi trong phan dau tep -> ten tep (khop chinh xac).
    Khong khop -> '?<ten>' de tach rieng, KHONG gop voi don vi khac; DS06 bao ra."""
    thu = os.path.basename(os.path.dirname(p))
    if re.fullmatch(r"[A-Z]{1,3}-[A-Z]+", thu):
        return thu
    m = re.match(r"([A-Z]{1,3}-[A-Z]+)_", os.path.basename(p))
    if m:
        return m.group(1)
    bt = bien_the_ma()
    ten = dau_tep(p)["don_vi"]
    than = os.path.splitext(os.path.basename(p))[0]
    for ung in (ten, than, *than.split()[::-1]):
        # ten tep hay bo chu "Khoa"/"Phong" ('SƯ PHẠM.docx' <-> bien the 'Khoa-Su-Pham') — van khop chinh xac
        for k in (_khoa(ung), "khoa" + _khoa(ung), "phong" + _khoa(ung)) if ung else ():
            if k in bt:
                return bt[k]
    return "?" + (ten or than)


def ky_tep(p):
    """Ky cua tep theo ten: 'thang-8-2026' -> ('thang', 8, 2026); khong co trong ten thi lay tieu de trong tep.
    Thu muc nop moi ky chua KQ thang N va KH thang N+1 — KHONG duoc so cheo hai ky (loi thu that 19/9/2026)."""
    t = _khong_dau(os.path.basename(p))
    m = re.search(r"(thang|quy|nam)[-_ ]?(\d{1,2})?[-_ .]*(\d{4})", t)
    if not m:
        return dau_tep(p)["ky"]
    return (m.group(1), int(m.group(2)) if m.group(2) else 0, int(m.group(3)))


def loai_tep(p):
    """Ten theo quy uoc 'KH-…'/'BC-…' truoc; khong thi lay tieu de trong tep.
    Phai co dau phan cach: 'KHCB.xlsx' (bao cao Khoa KHCB) tung bi xep nham la ke hoach."""
    t = os.path.basename(p).upper()
    if re.match(r"(BC|KQ|PL)[-_ ]", t):
        return "KQ"
    if re.match(r"KH[-_ ]", t):
        return "KH"
    return dau_tep(p)["loai"]


def gom_tep(ds):
    kq = []
    for p in ds or []:
        if os.path.isdir(p):
            for rr, _, fs in os.walk(p):
                kq += [os.path.join(rr, f) for f in fs if not f.startswith("~$") and f != "desktop.ini"]
        else:
            kq.append(p)
    return sorted(kq)


def doc(p):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            return r.read_appendix(p)
        except Exception as e:  # tep hong/khong dung mau
            return {"kind": None, "truc": {}, "truc_tong": {}, "canh_bao": [f"[KHÔNG ĐỌC ĐƯỢC] {e}"]}


def tong_theo_truc(ap):
    t = {n: {"so_nv": 0, "sl_qd": 0.0, "kpi_sl_qd": 0.0, "kpi_cl_qd": 0.0, "kpi_td_qd": 0.0} for n in TRUC}
    for n, ds in (ap.get("truc") or {}).items():
        for x in ds:
            t[n]["so_nv"] += 1
            for src, dst in (("so_luong_quy_doi", "sl_qd"), ("kpi_so_luong_qd", "kpi_sl_qd"),
                             ("kpi_chat_luong_qd", "kpi_cl_qd"), ("kpi_tien_do_qd", "kpi_td_qd")):
                v = r._num(x.get(src))
                if v is not None:
                    t[n][dst] += v
    return t


def doi_soat(kq_files, kh_files=(), tong_hop=None):
    """Tra ve dict ket qua co cau truc (de agent/test dung) — khong in."""
    out = {"loi": [], "don_vi": {}, "ds02": [], "ds03": [], "ds04": [], "ds05": {}, "ds06": []}
    chuan = ma_chuan()
    theo_dv = {}
    khac = {}
    for p in gom_tep(kq_files) + gom_tep(kh_files):
        ma = ma_don_vi(p)
        if not p.lower().endswith(".xlsx"):
            # Don vi nop kem bao cao thuyet minh .docx — binh thuong; chi ghi lai de xet "thieu .xlsx" o duoi
            khac.setdefault(ma, []).append((loai_tep(p), os.path.basename(p)))
            continue
        lt = loai_tep(p)
        ap = doc(p)
        lt = ap.get("kind") or lt
        theo_dv.setdefault(ma, {}).setdefault(lt, []).append((p, ap, ky_tep(p)))
        out["don_vi"].setdefault(ma, {"so_canh_bao": 0, "canh_bao": []})
        out["don_vi"][ma]["so_canh_bao"] += len(ap.get("canh_bao") or [])
        out["don_vi"][ma]["canh_bao"] += [f"{os.path.basename(p)}: {c}" for c in ap.get("canh_bao") or []]
    for ma, ds in sorted(khac.items()):
        for lt, ten in ds:
            if lt and not theo_dv.get(ma, {}).get(lt):
                out["ds06"].append((ma, ten, f"chỉ có tệp {os.path.splitext(ten)[1]}, thiếu Phụ lục Excel TB 736 "
                                             f"({'kết quả' if lt == 'KQ' else 'kế hoạch'}) — không đối soát được"))
            elif not lt and ma not in theo_dv:
                # Ten tep khong cho biet KH/KQ (bo cuc 21/9/2026) — van phai bao don vi khong co Excel nao.
                # Ma '?…' = khong xac dinh duoc don vi: co the Excel cua don vi nam duoi ten khac -> khong khang dinh.
                out["ds06"].append((ma, ten, "không xác định được đơn vị từ tên tệp — kiểm tay đơn vị này đã có "
                                             "Phụ lục Excel chưa" if ma.startswith("?") else
                                             f"chỉ có tệp {os.path.splitext(ten)[1]}, đơn vị không nộp "
                                             "Phụ lục Excel TB 736 nào — không đối soát được"))
    for ma in sorted(set(theo_dv) | set(khac)):
        if chuan and ma not in chuan:
            out["ds06"].append((ma, "", "mã đơn vị chưa có trong 20-Chuan-Chung/13-Bang-Ma-Don-Vi.md"))

    # DS04 — Task_ID trung (trong cung mot ky ket qua)
    gap = {}
    for ma, d in theo_dv.items():
        for p, ap, ky in d.get("KQ", []):
            for n, ds in ap["truc"].items():
                for x in ds:
                    tid = x.get("task_id")
                    if tid:
                        gap.setdefault((ky, str(tid).strip()), []).append((ma, n, (x.get("noi_dung") or "")[:60]))
    for (ky, tid), noi in gap.items():
        if len(noi) > 1:
            out["ds04"].append((tid, noi))

    # DS05 — % KPI theo Truc tinh lai. % > 100 la dau hieu TRON HAI THANG (KI-014):
    # khong quy doi, danh dau "khong tinh duoc" (loi thu that 19/9/2026: 300-850%).
    tong_dv = {n: {"so_nv": 0, "sl_qd": 0.0, "kpi_sl_qd": 0.0, "kpi_cl_qd": 0.0, "kpi_td_qd": 0.0} for n in TRUC}
    for d in theo_dv.values():
        for p, ap, ky in d.get("KQ", []):
            for n, v in tong_theo_truc(ap).items():
                for k in v:
                    tong_dv[n][k] += v[k]
    for n, v in tong_dv.items():
        b = v["sl_qd"]
        pct = {k: (round(100 * v["kpi_" + k + "_qd"] / b, 1) if b else None) for k in ("sl", "cl", "td")}
        lech = any(x is not None and x > 100.5 for x in pct.values())
        out["ds05"][n] = dict(v, lech_thang=lech,
                              **{"pct_" + k: (None if lech else x) for k, x in pct.items()})

    # DS02 — TRUY VET tong hop cap Truong ve dong nguon cua don vi. Tong hop chi lay nhiem vu
    # "Dua vao KH Truong" nen KHONG bang tong don vi — so tung dong, khong so tong (loi thu that 19/9/2026).
    if tong_hop:
        th = doc(tong_hop)
        if th.get("kind") != "KQ":
            out["ds02"].append(("—", "tệp tổng hợp", "không đọc được như Phụ lục kết quả TB 736", None, None))
        else:
            nguon = [x for d in theo_dv.values() for p, ap, ky in d.get("KQ", [])
                     for ds in ap["truc"].values() for x in ds]
            for n, ds in th["truc"].items():
                for x in ds:
                    goc = tim_nguon(x, nguon)
                    nd = (x.get("noi_dung") or "")[:70]
                    if len(_chuan(x.get("noi_dung"))) < 12:
                        out["ds02"].append((n, nd or "(trống)", "dòng tổng hợp không ghi nội dung nhiệm vụ — không truy vết được", None, None))
                        continue
                    if goc is None:
                        out["ds02"].append((n, nd, "không truy được về dòng nguồn của đơn vị (Nguyên tắc bất biến 3)", None, None))
                        continue
                    truong = (("so_luong_quy_doi", "SL quy đổi"), ("kpi_so_luong_qd", "KPI số lượng QĐ"),
                              ("kpi_chat_luong_qd", "KPI chất lượng QĐ"), ("kpi_tien_do_qd", "KPI tiến độ QĐ"))

                    def lech(y):
                        kq_ = []
                        for k, ten in truong:
                            a_, b_ = r._num(x.get(k)), r._num(y.get(k))
                            if a_ is not None and b_ is not None and abs(a_ - b_) > SAI_SO:
                                kq_.append((ten, a_, b_))
                        return kq_
                    ung = cac_nguon(x, nguon)
                    if any(not lech(y) for y in ung):
                        continue                      # co nguon khop ca so lieu
                    if len(ung) > 1 and not x.get("task_id"):
                        out["ds02"].append((n, nd, f"{len(ung)} dòng nguồn giống nội dung, không dòng nào cùng số liệu — "
                                                   "cần Task_ID để truy vết duy nhất", None, None))
                        continue
                    for ten, a_, b_ in lech(goc):
                        out["ds02"].append((n, nd, ten + ": tổng hợp khác nguồn", a_, b_))

    # DS03 — KH <-> KQ CUNG KY cua moi don vi
    for ma, d in sorted(theo_dv.items()):
        for pkh, kh_ap, ky in d.get("KH", []):
            cung = [ap for p, ap, k in d.get("KQ", []) if ky and k == ky]
            if not cung:
                continue
            kh = [x for ds in kh_ap["truc"].values() for x in ds]
            kq = [x for ap in cung for ds in ap["truc"].values() for x in ds]
            for a_ in kh:
                if tim_nguon(a_, kq) is None:
                    out["ds03"].append((ma, "KH chưa có kết quả", (a_.get("noi_dung") or "")[:90]))
            for b_ in kq:
                if tim_nguon(b_, kh) is None:
                    out["ds03"].append((ma, "kết quả không có trong KH (phát sinh? cần nguồn)", (b_.get("noi_dung") or "")[:90]))
    out["so_cap_cung_ky"] = sum(1 for d in theo_dv.values() for _, _, ky in d.get("KH", [])
                                if ky and any(k == ky for _, _, k in d.get("KQ", [])))
    return out


def _diem_giong(x, ds):
    """[(diem, y)] cho moi y giong >= NGUONG_GIONG. Loc nhanh real_quick_ratio/quick_ratio truoc ratio():
    ban dau so thang ratio() cho moi cap mat 56 giay tren 13 don vi (19/9/2026)."""
    cx = x.get("_chuan") or _chuan(x.get("noi_dung"))
    if len(cx) < 12:          # dong trong/"…": khong du thong tin de ghep — tranh ghep bua
        return []
    sm = difflib.SequenceMatcher(None, autojunk=False)
    sm.set_seq2(cx)
    kq = []
    for y in ds:
        cy = y.get("_chuan")
        if cy is None:
            cy = y["_chuan"] = _chuan(y.get("noi_dung"))
        sm.set_seq1(cy)
        if sm.real_quick_ratio() >= NGUONG_GIONG and sm.quick_ratio() >= NGUONG_GIONG:
            d = sm.ratio()
            if d >= NGUONG_GIONG:
                kq.append((d, y))
    return kq


def cac_nguon(x, ds):
    """Moi dong nguon co the tuong ung (Task_ID trung, hoac noi dung giong >= nguong)."""
    if x.get("task_id"):
        cung = [y for y in ds if y.get("task_id") == x["task_id"]]
        if cung:
            return cung
    return [y for _, y in _diem_giong(x, ds)]


def tim_nguon(x, ds):
    """Dong tuong ung tot nhat: uu tien Task_ID, sau do noi dung giong nhat (>= NGUONG_GIONG)."""
    if x.get("task_id"):
        for y in ds:
            if y.get("task_id") == x["task_id"]:
                return y
    ung = _diem_giong(x, ds)
    return max(ung, key=lambda t: t[0])[1] if ung else None


def in_md(o, file=sys.stdout):
    w = lambda s="": print(s, file=file)  # noqa: E731
    w("# Đối soát số liệu Phụ lục TB 736")
    w("\n## DS05 — KPI theo Trục tính lại từ các đơn vị (số tham chiếu)")
    w("| Trục | Số NV | SL quy đổi | % số lượng | % chất lượng | % tiến độ |\n|---|---|---|---|---|---|")
    for n, v in o["ds05"].items():
        if v.get("lech_thang"):
            w(f"| {n} | {v['so_nv']} | {v['sl_qd']:g} | ⚠ không tính được — KPI và SL quy đổi lệch thang (KI-014) | | |")
        else:
            w(f"| {n} | {v['so_nv']} | {v['sl_qd']:g} | {v['pct_sl']} | {v['pct_cl']} | {v['pct_td']} |")
    w("\n## DS02 — Truy vết từng dòng tổng hợp cấp Trường về nguồn đơn vị")
    if not o["ds02"]:
        w("Không lệch (hoặc không có tệp tổng hợp để so).")
    for n, nd, mo_ta, a, b in o["ds02"]:
        w(f"- Trục {n} “{nd}”: {mo_ta}" + (f" (tổng hợp={a}, nguồn={b})" if a is not None else ""))
    w("\n## DS04 — Task_ID trùng")
    w("Không có." if not o["ds04"] else "")
    for tid, noi in o["ds04"]:
        w(f"- `{tid}`: " + "; ".join(f"{m} Trục {n} “{nd}”" for m, n, nd in noi))
    w("\n## DS03 — Kế hoạch ↔ kết quả cùng kỳ")
    if not o.get("so_cap_cung_ky"):
        w("Không có cặp KH/KQ **cùng kỳ** để so (thư mục nộp thường có KQ tháng N và KH tháng N+1 — "
          "đưa KH tháng N bằng --kh).")
    elif not o["ds03"]:
        w(f"Không lệch ({o['so_cap_cung_ky']} cặp cùng kỳ).")
    for ma, loai, nd in o["ds03"]:
        w(f"- {ma} · {loai}: “{nd}”")
    w("\n## DS06 — Mã đơn vị và loại tệp")
    w("Không có." if not o["ds06"] else "")
    for ma, tep, mo_ta in o["ds06"]:
        w(f"- {ma} {tep}: {mo_ta}")
    w("\n## DS01 — Cảnh báo trong từng tệp (read_bc736_excel)")
    for ma, d in sorted(o["don_vi"].items()):
        w(f"- **{ma}**: {d['so_canh_bao']} cảnh báo")
        for c in d["canh_bao"][:5]:
            w(f"    - {c}")
    w("\n_Không sửa số liệu; không quy đổi giữa hai thang điểm (KI-014)._")


def main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--kq", nargs="+", required=True)
    ap.add_argument("--kh", nargs="*", default=[])
    ap.add_argument("--tong-hop")
    ap.add_argument("--md")
    a = ap.parse_args(argv)
    # --kq tro vao thu muc ky chua ca KH va KQ: tach theo ten tep
    tat_ca = gom_tep(a.kq)
    kq = [p for p in tat_ca if loai_tep(p) != "KH"]
    kh = [p for p in tat_ca if loai_tep(p) == "KH"] + gom_tep(a.kh)
    o = doi_soat(kq, kh, a.tong_hop)
    in_md(o)
    if a.md:
        os.makedirs(os.path.dirname(os.path.abspath(a.md)), exist_ok=True)
        with open(a.md, "w", encoding="utf-8") as f:
            in_md(o, f)
    return 1 if (o["ds02"] or o["ds04"]) else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/duong_dan.py` (2614 byte, sha256 `2002e26fc5149e12f9e7e69bb53cc14d03f8408fd4db46ce28cac8f70efdc241`)

`````python
# -*- coding: utf-8 -*-
"""Tim duong dan du an va kho KTC-Database — KHONG ghi cung o dia (DL-20260918-005, Quy uoc 2).

KTC-Quan-tri chay tai may (ban lam viec cuc bo). KTC-Database chi con BAN GOC tren Google Drive
(ban chep o may se bi xoa — ban chep da cu: 18/9/2026 thieu 163/1171 tep so voi Drive). Thu tu tim:
  1. Bien moi truong KTC_DATABASE_DIR.
  2. O Google Drive for Desktop: <o>:\\My Drive\\KTC-Database (hoac "Drive của tôi", Shared drives\\*\\).
  3. Thu muc NGANG CAP <cha cua KTC-Quan-tri>/KTC-Database — ban chep cuc bo, CO THE CU (canh bao).
  4. Khong tim thay -> nem loi ro rang (skill phai DUNG VA HOI, khong suy dien).
"""
import glob
import os
import string
import sys

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEN = "KTC-Database"


def _tren_drive(ten=TEN):
    for o in string.ascii_uppercase:
        goc = f"{o}:\\"
        if not os.path.isdir(goc):
            continue
        for mau in ("My Drive", "Drive của tôi", os.path.join("Shared drives", "*"),
                    os.path.join("Bộ nhớ dùng chung", "*")):
            for p in glob.glob(os.path.join(goc, mau, ten)):
                if os.path.isdir(p):
                    yield p


def ktc_database(canh_bao_ban_cu: bool = True) -> str:
    env = os.environ.get("KTC_DATABASE_DIR")
    if env and os.path.isdir(env):
        return env
    for p in _tren_drive():
        return p
    p = os.path.join(os.path.dirname(DU_AN), TEN)
    if os.path.isdir(p):
        if canh_bao_ban_cu:
            print(f"⚠ Đang dùng bản chép cục bộ {p} — có thể cũ hơn bản gốc trên Google Drive.",
                  file=sys.stderr)
        return p
    raise FileNotFoundError(
        "Không tìm thấy KTC-Database. Đặt biến môi trường KTC_DATABASE_DIR trỏ tới thư mục "
        "KTC-Database trên Google Drive (ví dụ <ổ Drive>\\My Drive\\KTC-Database).")


def he_ngoai(ten):
    """Tim mot he KTC khac (vi du KTC-Ra-Soat-897-Universal-Plugin) — tra ve duong dan hoac None.

    Thu tu: bien moi truong KTC_<TEN> -> thu muc ngang cap voi du an -> moi o Google Drive.
    Cac he KTC khong nam cung mot o dia: KTC-Quan-tri o D:, kho 897 o Google Drive (I:).
    Vi vay khong duoc gia dinh "ngang cap" nhu truoc (Nguyen tac 4.2: khong ghi cung o dia).
    """
    mt = os.environ.get("KTC_" + ten.upper().replace("-", "_"))
    if mt and os.path.isdir(mt):
        return mt
    ngang = os.path.join(os.path.dirname(DU_AN), ten)
    if os.path.isdir(ngang):
        return ngang
    for p in _tren_drive(ten):
        return p
    return None
`````

## `scripts/kiem_minh_chung.py` (9145 byte, sha256 `0d74703529a6332d72a2c46bf1f04dedd33617c07060a10180aeceeaf0d58a8e`)

`````python
# -*- coding: utf-8 -*-
"""Kiem so bo minh chung nhiem vu — DL-20260919-006 (dung cho agent ktc-xac-minh-minh-chung).

Doc cot THEO TEN TIEU DE, dung duoc cho:
  - 24-KTC-Theo-doi-CV/"01. Bo du lieu van hanh...xlsx": sheet "Nhiem vu" + "Minh chung" (+ "Cap nhat tien do")
  - 21-Master-Task-Register/*.xlsx: cot Task_ID, Trang_Thai, Han_Hoan_Thanh, Minh_Chung

Phep kiem (chi PHAT HIEN — khong ghi "Da xac minh"; trang thai do chi nguoi co tham quyen gan, Skill 43):
  MC01  Nhiem vu "Hoan thanh" khong co minh chung nao            (Muc 1 — khong duoc dua vao bao cao)
  MC02  Minh chung khong co lien ket                              (Muc 2)
  MC03  Lien ket: duong dan may/Drive khong ton tai (Muc 2) · URL Drive -> CAN MO QUA GOOGLE DRIVE · URL khac -> can mo
  MC04  Ngay phat sinh sau han hien hanh / thieu ngay             (Muc 3)
  MC05  Ghi "Da xac minh" nhung thieu nguoi hoac ngay xac minh     (Muc 2 — xac minh hinh thuc)
  MC06  Minh chung tro toi ma nhiem vu khong ton tai              (Muc 2)
  MC07  Cung mot lien ket dung cho nhieu nhiem vu khac nhau        (Muc 4 — co the hop le, can xem)
Khong tim thay minh chung KHONG dong nghia chua lam (tien le QD 1923): MC01 ghi "can don vi xac nhan".

Chay:  python 29-Cong-Cu/kiem_minh_chung.py <tep.xlsx> [--md <bao cao.md>]
Ma thoat: 1 neu co Muc 1-2, nguoc lai 0.
"""
import datetime as dt
import os
import re
import sys
import unicodedata
import warnings

TEN = {  # khoa noi bo -> cac ten tieu de chap nhan (so khop khong dau, khong phan biet hoa thuong)
    "ma_nv": ("ma nhiem vu", "task_id"),
    "trang_thai": ("trang thai", "trang_thai"),
    "han": ("han hien hanh", "han_hoan_thanh", "han baseline"),
    "ten_nv": ("ten nhiem vu", "ten_nhiem_vu"),
    "don_vi": ("don vi chu tri", "don_vi_chu_tri"),
    "mc_ma": ("ma minh chung",),
    "lien_ket": ("lien ket drive", "lien ket minh chung", "minh_chung", "minh chung"),
    "ngay_ps": ("ngay phat sinh",),
    "tinh_trang": ("tinh trang xac minh",),
    "nguoi_xm": ("nguoi xac minh",),
    "ngay_xm": ("ngay xac minh",),
}
HOAN_THANH = re.compile(r"^(da )?hoan thanh$")
URL_DRIVE = re.compile(r"https?://(drive|docs)\.google\.com/\S*?(?:/d/|id=|folders/)([\w-]{20,})")


def _k(s):
    s = unicodedata.normalize("NFD", str(s or "").replace("Đ", "D").replace("đ", "d"))
    return " ".join("".join(c for c in s if unicodedata.category(c) != "Mn").lower().split())


def _cot(tieu_de, khoa):
    for i, h in enumerate(tieu_de):
        if _k(h) in TEN[khoa]:
            return i
    return None


def _bang(ws):
    """Tra ve (tieu_de, cac dong) — dong tieu de la dong dau co >= 3 o chu."""
    dong = list(ws.iter_rows(values_only=True))
    for i, r in enumerate(dong[:10]):
        if sum(1 for x in r if isinstance(x, str) and x.strip()) >= 3:
            return list(r), [x for x in dong[i + 1:] if any(v not in (None, "") for v in x)]
    return [], []


def _ngay(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", str(v or ""))
    return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None


def doc_tep(p):
    import openpyxl
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        wb = openpyxl.load_workbook(p, data_only=True)
    nv, mc = {}, []
    for ws in wb.worksheets:
        td, rows = _bang(ws)
        c = {k: _cot(td, k) for k in TEN}
        g = lambda r, k: (r[c[k]] if c[k] is not None and c[k] < len(r) else None)  # noqa: E731
        # Sheet nhiem vu / Master Register phai co ten hoac han nhiem vu — sheet "Cap nhat tien do" cung co
        # Ma nhiem vu + Trang thai nhung la nhat ky cap nhat, doc nhu sheet minh chung (cot Lien ket minh chung).
        if c["ma_nv"] is not None and c["trang_thai"] is not None and (c["ten_nv"] is not None or c["han"] is not None):
            for r in rows:
                ma = g(r, "ma_nv")
                if not ma or str(ma).startswith("("):
                    continue
                nv[str(ma).strip()] = {"trang_thai": g(r, "trang_thai"), "han": _ngay(g(r, "han")),
                                       "ten": g(r, "ten_nv"), "don_vi": g(r, "don_vi"), "sheet": ws.title}
                lk = g(r, "lien_ket")                       # Master Register: cot Minh_Chung ngay tren dong
                if lk:
                    mc.append({"ma_nv": str(ma).strip(), "lien_ket": str(lk).strip(), "sheet": ws.title})
        elif c["ma_nv"] is not None and c["lien_ket"] is not None:           # sheet minh chung / cap nhat
            for r in rows:
                ma = g(r, "ma_nv")
                if not ma:
                    continue
                mc.append({"ma": g(r, "mc_ma"), "ma_nv": str(ma).strip(), "lien_ket": str(g(r, "lien_ket") or "").strip(),
                           "ngay_ps": _ngay(g(r, "ngay_ps")), "ngay_ps_tho": g(r, "ngay_ps"),
                           "tinh_trang": g(r, "tinh_trang"), "nguoi_xm": g(r, "nguoi_xm"), "ngay_xm": g(r, "ngay_xm"),
                           "sheet": ws.title, "la_mc": c["mc_ma"] is not None})
    return nv, mc


def kiem_lien_ket(lk):
    """Tra ve (muc, trang_thai) cho mot lien ket."""
    if not lk:
        return 2, "trống"
    m = URL_DRIVE.search(lk)
    if m:
        return None, f"URL Google Drive (ID {m.group(2)[:12]}…) — CẦN MỞ QUA GOOGLE DRIVE để xác nhận tồn tại và nội dung"
    if re.match(r"https?://", lk):
        return None, "liên kết ngoài — cần mở để xem"
    if os.path.exists(lk):
        return None, "tệp tồn tại trên máy/ổ Drive — cần mở xem nội dung"
    return 2, "đường dẫn KHÔNG tồn tại trên máy (sai đường dẫn, đã đổi tên/xóa, hoặc Drive chưa đồng bộ)"


def kiem(nv, mc):
    kq = []
    theo_nv = {}
    for m in mc:
        theo_nv.setdefault(m["ma_nv"], []).append(m)
    for ma, x in nv.items():
        if HOAN_THANH.match(_k(x["trang_thai"])) and not any(m["lien_ket"] for m in theo_nv.get(ma, [])):
            kq.append((1, "MC01", ma, "Hoàn thành nhưng không có minh chứng — không được đưa vào báo cáo; "
                                       "chưa chắc là chưa làm, cần đơn vị xác nhận/bổ sung"))
    dung = {}
    for m in mc:
        vt = f"{m['ma_nv']}" + (f" · {m['ma']}" if m.get("ma") else "")
        if m["ma_nv"] not in nv and nv:
            kq.append((2, "MC06", vt, "minh chứng trỏ tới mã nhiệm vụ không có trong danh sách nhiệm vụ"))
        muc, tt = kiem_lien_ket(m["lien_ket"])
        if muc:
            kq.append((muc, "MC02" if not m["lien_ket"] else "MC03", vt, f"liên kết {tt}"))
        elif m["lien_ket"]:
            kq.append((None, "MC03", vt, tt))
        if m["lien_ket"]:
            dung.setdefault(m["lien_ket"], set()).add(m["ma_nv"])
        if m.get("la_mc"):
            han = (nv.get(m["ma_nv"]) or {}).get("han")
            if not m.get("ngay_ps"):
                kq.append((3, "MC04", vt, "thiếu ngày phát sinh minh chứng"))
            elif han and m["ngay_ps"] > han:
                kq.append((3, "MC04", vt, f"minh chứng phát sinh {m['ngay_ps']:%d/%m/%Y} sau hạn {han:%d/%m/%Y}"))
            if re.match(r"^da xac minh", _k(m.get("tinh_trang"))) and not (m.get("nguoi_xm") and m.get("ngay_xm")):
                kq.append((2, "MC05", vt, "ghi “Đã xác minh” nhưng thiếu người/ngày xác minh — xác minh hình thức"))
    for lk, ds in dung.items():
        if len(ds) > 1:
            kq.append((4, "MC07", ", ".join(sorted(ds)), f"cùng một liên kết cho {len(ds)} nhiệm vụ: {lk[:80]}"))
    kq.sort(key=lambda x: (x[0] or 9, x[2]))
    return kq


def in_md(p, nv, mc, kq, file=sys.stdout):
    w = lambda s="": print(s, file=file)  # noqa: E731
    ht = sum(1 for x in nv.values() if HOAN_THANH.match(_k(x["trang_thai"])))
    w(f"# Kiểm sơ bộ minh chứng — {os.path.basename(p)}")
    w(f"{len(nv)} nhiệm vụ ({ht} hoàn thành) · {len(mc)} minh chứng/liên kết")
    w("\n| Mức | Mã | Nhiệm vụ · minh chứng | Nội dung |\n|---|---|---|---|")
    for muc, ma, vt, nd in kq:
        w(f"| {muc or '—'} | {ma} | {vt} | {nd} |")
    w("\n_Công cụ chỉ kiểm sơ bộ: “Đã xác minh” chỉ do người có thẩm quyền gán sau khi mở tệp (Skill 43)._")


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    ra = None
    if "--md" in argv:
        i = argv.index("--md")
        ra, argv = argv[i + 1], argv[:i] + argv[i + 2:]
    xau = False
    for p in argv:
        nv, mc = doc_tep(p)
        kq = kiem(nv, mc)
        in_md(p, nv, mc, kq)
        if ra:
            os.makedirs(os.path.dirname(os.path.abspath(ra)), exist_ok=True)
            with open(ra, "w", encoding="utf-8") as f:
                in_md(p, nv, mc, kq, f)
        xau |= any(x[0] in (1, 2) for x in kq)
    return 1 if xau else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/kiem_the_thuc.py` (31297 byte, sha256 `1158fd000ef7bf2b1cb0cb06f669af2930666ce2f30f92d2c7bf4aca3c9fdcce`)

`````python
# -*- coding: utf-8 -*-
"""Kiem the thuc, ky thuat trinh bay san pham .docx/.xlsx — DL-20260919-003.

Chuan: 20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md — so do that cua 16 mau
KTC-Database/03-Templates(1) (.dotx/.xltx), NĐ 30/2020 Phu luc I, TB 597/TB-CĐKT (qua 897,
Checklist 05-Hinh-Thuc va 08-Quy-Uoc-Rieng-CDKT muc 4).

Do tren BYTE THAT cua tep (python-docx/openpyxl): phong va co chu duoc giai theo chuoi
run -> style ky tu -> style doan (ke ca base_style) -> docDefaults -> theme.
Chi PHAT HIEN va GOI Y muc — khong sua tep. He A (hanh chinh). Khong ap cho van ban Dang (he B).

Chay:  python 29-Cong-Cu/kiem_the_thuc.py <tep .docx|.xlsx> [...]
       python 29-Cong-Cu/kiem_the_thuc.py --tao <mau .dotx> <dich .docx>   (tao ban lam viec tu mau)
       python 29-Cong-Cu/kiem_the_thuc.py --khung <dich .docx> [TB|KH|BC|TTr|QĐ|GM|HD|CTr|BB]
           (khong doc duoc KTC-Database: tao tu khung dung tu mau 03A-Thong-bao — KHONG dung bang tieu de tay)
Ma thoat: 1 neu co goi y Muc 1 hoac Muc 2, nguoc lai 0.
"""
import collections
import io
import os
import re
import sys
import zipfile

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
PHONG = "Times New Roman"
# (min, max) cm — NĐ 30 Phu luc I; mau 03-Templates(1) dung 2/2/3/2
LE = {"trên": (2.0, 2.5), "dưới": (2.0, 2.5), "trái": (3.0, 3.5), "phải": (1.5, 2.0)}
EPS = 0.05


# ------------------------------------------------------------------ mo tep mau
def _doi_kieu(du_lieu: bytes, tu: bytes, sang: bytes) -> bytes:
    b = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(du_lieu)) as zi, zipfile.ZipFile(b, "w", zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            data = zi.read(it.filename)
            if it.filename == "[Content_Types].xml":
                data = data.replace(tu, sang)
            zo.writestr(it, data)
    return b.getvalue()


def mo_mau(p):
    """Mo .dotx (hoac .docx) thanh docx.Document — python-docx khong tu mo .dotx."""
    import docx
    raw = open(p, "rb").read()
    if p.lower().endswith(".dotx"):
        raw = _doi_kieu(raw, b"wordprocessingml.template.main+xml", b"wordprocessingml.document.main+xml")
    return docx.Document(io.BytesIO(raw))


def tao_tu_mau(mau, dich):
    """Tao ban lam viec .docx/.xlsx tu mau .dotx/.xltx — giu nguyen style, le, bang the thuc."""
    raw = open(mau, "rb").read()
    if mau.lower().endswith(".dotx"):
        raw = _doi_kieu(raw, b"wordprocessingml.template.main+xml", b"wordprocessingml.document.main+xml")
    elif mau.lower().endswith(".xltx"):
        raw = _doi_kieu(raw, b"spreadsheetml.template.main+xml", b"spreadsheetml.sheet.main+xml")
    os.makedirs(os.path.dirname(os.path.abspath(dich)), exist_ok=True)
    open(dich, "wb").write(raw)
    return dich


# Khung the thuc VBHC dung tu mau 03A-Thong-bao (28/9/2026; thay khung ghep tu TB 1060 — hien "1" o trang 1,
# duong ke trich yeu lech) — dung khi KHONG doc duoc KTC-Database (Cowork, Chat,
# tai khoan thanh vien) thay cho dung bang tieu de bang tay (28/9/2026).
TEN_KHUNG = "Khung-the-thuc-VBHC.docx"
LOAI_VB = {"TB": "THÔNG BÁO", "KH": "KẾ HOẠCH", "BC": "BÁO CÁO", "TTr": "TỜ TRÌNH", "QĐ": "QUYẾT ĐỊNH",
           "GM": "GIẤY MỜI", "HD": "HƯỚNG DẪN", "CTr": "CHƯƠNG TRÌNH", "BB": "BIÊN BẢN"}


def tim_khung():
    g = os.path.dirname(os.path.abspath(__file__))
    for p in (os.path.join(g, "..", "assets"), os.path.join(g, "..", "skills", "the-thuc", "assets"),
              os.path.join(g, "..", "27-KTC-The-Thuc", "assets")):
        f = os.path.join(p, TEN_KHUNG)
        if os.path.isfile(f):
            return os.path.normpath(f)
    raise FileNotFoundError(f"Không thấy {TEN_KHUNG} (skill the-thuc/assets)")


def tao_khung(dich, loai="TB", nam=None):
    """Tao tep lam viec tu khung: dat loai van ban (ten loai, ky hieu Số: /<loai>-CĐKT) va nam."""
    import datetime
    import docx
    if loai not in LOAI_VB:
        raise ValueError(f"Loại văn bản {loai!r} — chọn một trong {', '.join(LOAI_VB)}")
    d = docx.Document(tim_khung())
    nam = nam or datetime.date.today().year
    for p in list(d.paragraphs) + list(_doan_trong_bang(d)):
        for r in p.runs:
            if r.text.strip() == "THÔNG BÁO":
                r.text = r.text.replace("THÔNG BÁO", LOAI_VB[loai])
            elif "/TB-CĐKT" in r.text:
                r.text = r.text.replace("/TB-CĐKT", f"/{loai}-CĐKT")
            elif "năm 2026" in r.text and "ngày" in p.text:
                r.text = r.text.replace("năm 2026", f"năm {nam}")
    os.makedirs(os.path.dirname(os.path.abspath(dich)), exist_ok=True)
    d.save(dich)
    return dich


# ------------------------------------------------------------------ giai phong/co chu
class GiaiDocx:
    def __init__(self, d):
        self.d = d
        root = d.styles.element
        rd = root.find(f"{W}docDefaults/{W}rPrDefault/{W}rPr")
        self.mac_dinh_phong = self._phong_rpr(rd)
        sz = rd.find(f"{W}sz") if rd is not None else None
        self.mac_dinh_co = int(sz.get(f"{W}val")) / 2 if sz is not None else 10.0
        self.theme = self._doc_theme()

    def _doc_theme(self):
        """Phong theme ma Word THAT SU hien thi. settings themeFontLang = vi-VN -> Word dung phong
        script="Viet" cua theme (vd. major Viet = Times New Roman) thay vi <a:latin> (Calibri Light).
        Bo qua buoc nay tung bao nham hang tram doan “Calibri Light” tren van ban da ban hanh (19/9/2026)."""
        viet = bool(re.search(r'<w:themeFontLang [^>]*w:val="vi', self.d.settings.element.xml))
        kq = {"major": None, "minor": None}
        for rel in self.d.part.rels.values():
            if rel.reltype.endswith("/theme"):
                x = rel.target_part.blob.decode("utf-8", "ignore")
                for loai, the in (("major", "majorFont"), ("minor", "minorFont")):
                    m = re.search(f"<a:{the}>(.*?)</a:{the}>", x, re.S)
                    if not m:
                        continue
                    khoi = m.group(1)
                    v = re.search(r'script="Viet" typeface="([^"]*)"', khoi) if viet else None
                    latin = re.search(r'<a:latin typeface="([^"]*)"', khoi)
                    kq[loai] = v.group(1) if v else (latin.group(1) if latin else None)
        return kq

    def _phong_rpr(self, rpr):
        if rpr is None:
            return None
        f = rpr.find(f"{W}rFonts")
        if f is None:
            return None
        if f.get(f"{W}ascii"):
            return f.get(f"{W}ascii")
        t = f.get(f"{W}asciiTheme")
        if t:
            return "theme:" + ("major" if "major" in t.lower() else "minor")
        return None

    def _xu_theme(self, v):
        if v and v.startswith("theme:"):
            return self.theme.get(v[6:]) or v
        return v

    def _style_chain(self, st):
        while st is not None:
            yield st
            st = st.base_style

    def phong(self, run, para):
        v = run.font.name or self._phong_rpr(run._element.rPr)
        if not v and run.style is not None:
            for s in self._style_chain(run.style):
                v = s.font.name or self._phong_rpr(s.element.rPr)
                if v:
                    break
        if not v:
            for s in self._style_chain(para.style):
                v = s.font.name or self._phong_rpr(s.element.rPr)
                if v:
                    break
        return self._xu_theme(v or self.mac_dinh_phong)

    def co(self, run, para):
        if run.font.size:
            return run.font.size.pt
        if run.style is not None:
            for s in self._style_chain(run.style):
                if s.font.size:
                    return s.font.size.pt
        for s in self._style_chain(para.style):
            if s.font.size:
                return s.font.size.pt
        return self.mac_dinh_co

    def can_le(self, para):
        if para.paragraph_format.alignment is not None:
            return para.paragraph_format.alignment
        for s in self._style_chain(para.style):
            if s.paragraph_format.alignment is not None:
                return s.paragraph_format.alignment
        return None


def _doan_trong_bang(d):
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    yield p


def _co_duong_ke(o):
    """O bang co duong ke (hinh Draw, VML line hoac vien duoi doan)."""
    x = o._tc.xml
    return "<w:drawing" in x or "<v:line" in x or "<v:shape" in x or re.search(r"<w:pBdr>.*?<w:bottom ", x, re.S)


def _kiem_bang_tieu_de(d, g):
    """TT12-TT15: hinh hoc bang tieu de (28/9/2026 — TB do Cowork dung tay: bang 16 cm chia doi, quoc hieu va dia danh
    xuong dong, thieu duong ke duoi ten Truong; cac phep TT08-TT09 cu van bao 'dat').
    So do van ban da ban hanh (TB 1060, 1092, TB phuong an A1): bang 17,25-17,5 cm; cot trai 7,0-7,5; cot phai 9,75-10,3."""
    kq = []
    if not d.tables:
        return kq
    t = d.tables[0]
    o = [c for r in t.rows for c in r.cells]
    chu = lambda c: " ".join(p.text for p in c.paragraphs).upper()  # noqa: E731
    phai = [c for c in o if "CỘNG H" in chu(c) and "VIỆT NAM" in chu(c)]
    trai = [c for c in o if "TRƯỜNG CAO ĐẲNG KON TUM" in chu(c)]
    if not phai or not trai:
        return kq
    grid = [c.w.cm for c in t._tbl.tblGrid.gridCol_lst if c.w is not None]
    rong = lambda c: c.width.cm if c.width is not None else None  # noqa: E731
    w_trai = rong(trai[0]) or (grid[0] if grid else None)
    w_phai = rong(phai[0]) or (grid[-1] if grid else None)
    if w_trai and w_phai:
        # Quet 434 van ban kho 02, 04 (28/9/2026): van ban that co cot phai 9,13-9,28 cm van hien thi dung -> nguong 9,0
        if w_phai < 9.0 or w_trai > w_phai:
            kq.append((2, "TT12", f"Bảng tiêu đề chia cột {w_trai:.2f} + {w_phai:.2f} cm — quốc hiệu, dòng địa danh sẽ xuống "
                       "dòng. Văn bản đã ban hành: cột trái 7–7,5 cm, cột phải 9,75–10,3 cm (dựng bằng --khung)"))
        elif w_trai + w_phai < 16.0:
            kq.append((3, "TT12", f"Bảng tiêu đề rộng {w_trai + w_phai:.2f} cm — văn bản đã ban hành: 17,25–17,5 cm"))
    da_xet, doan_bang = set(), []  # ca bang: dong "Số", "ngày" thuong o hang 2 (khung, TB 1060)
    for c in o:
        if c._tc not in da_xet:
            da_xet.add(c._tc)
            doan_bang += c.paragraphs
    for p in doan_bang:
        t_up = p.text.strip().upper()
        rs = [r for r in p.runs if r.text.strip()]
        if not rs:
            continue
        if t_up.startswith(("UBND", "ỦY BAN NHÂN DÂN", "UỶ BAN NHÂN DÂN")) and any(r.bold for r in rs):
            kq.append((2, "TT13", "Tên cơ quan chủ quản “UBND TỈNH QUẢNG NGÃI” in đậm — NĐ 30: in hoa, đứng, không đậm"))
        if ", NGÀY" in t_up:
            if any(r.bold for r in rs):
                kq.append((2, "TT15", "Dòng địa danh, ngày tháng in đậm — NĐ 30: nghiêng, không đậm, cỡ 13–14"))
            if not all(r.italic or (p.style is not None and p.style.font.italic) for r in rs):
                kq.append((3, "TT15", "Dòng địa danh, ngày tháng không nghiêng — NĐ 30: chữ nghiêng"))
    # Duong ke thuong la hinh noi neo o o "Số"/"ngày" cung cot (TB 1092, 1056) — xet ca cot
    def cot(c):
        for r in t.rows:
            for j, x in enumerate(r.cells):
                if x._tc is c._tc:
                    return [rr.cells[j] for rr in t.rows if j < len(rr.cells)]
        return [c]
    if not any(_co_duong_ke(x) for x in cot(trai[0])):
        kq.append((2, "TT14", "Thiếu đường kẻ dưới tên cơ quan ban hành “TRƯỜNG CAO ĐẲNG KON TUM” "
                   "(NĐ 30: đường kẻ ngang, nét liền, bằng 1/3–1/2 dòng chữ)"))
    if not any(_co_duong_ke(x) for x in cot(phai[0])):
        kq.append((2, "TT14", "Thiếu đường kẻ dưới tiêu ngữ “Độc lập - Tự do - Hạnh phúc”"))
    return kq


# ------------------------------------------------------------------ anh xa bo quy tac 897
# Nguon (KHONG chep, chi anh xa ma kiem): KTC-Ra-Soat-897-v2-Cai-tien/references/Checklist/
#   01-The-Thuc.md muc 1 (9 thanh phan, quy dinh chung NĐ 30) · 08-Quy-Uoc-Rieng-CDKT.md muc 4 (TB 597 so cung),
#   muc 5.1 (KT./TL./TUQ.), muc 5.4 (khong hoc ham, hoc vi). 01 muc 6: sai co chu, kieu chu, vi tri -> Muc 2.
HOC_HAM = re.compile(r"^(GS|PGS|TS|ThS|BS|BSCKI+|CKI+|DS|KS|CN|NCS|TTƯT|NGƯT|NGND)\.?\s", re.I)


def _thuoc_tinh(r, p, ten):
    """bold/italic that: run -> style ky tu -> style doan (ca base_style)."""
    v = getattr(r.font, ten)
    if v is not None:
        return v
    for st in ([r.style] if r.style is not None else []) + [p.style]:
        while st is not None:
            x = getattr(st.font, ten)
            if x is not None:
                return x
            st = st.base_style
    return False


def _kieu(g, p):
    rs = [r for r in p.runs if r.text.strip()]
    if not rs:
        return None
    return ({g.co(r, p) for r in rs}, all(_thuoc_tinh(r, p, "bold") for r in rs),
            any(_thuoc_tinh(r, p, "bold") for r in rs), all(_thuoc_tinh(r, p, "italic") for r in rs))


def _kiem_thanh_phan_897(d, g):
    """TT17 (co, kieu chu tung thanh phan), TT18 (duong ke duoi trich yeu), TT19 (ky thay, hoc ham)."""
    kq = []

    def sai(ten, p, co=None, dam=None, nghieng=None, nguon="01 mục 1 · 08 mục 4"):
        k = _kieu(g, p)
        if k is None:
            return
        cs, dam_het, dam_co, ngh = k
        loi = []
        if co is not None and cs != {float(co)}:
            loi.append(f"cỡ {'/'.join(f'{c:g}' for c in sorted(cs))} (chuẩn {co})")
        if dam is True and not dam_het:
            loi.append("chưa đậm")
        if dam is False and dam_co:
            loi.append("không được đậm")
        if nghieng is True and not ngh:
            loi.append("chưa nghiêng")
        if loi:
            kq.append((2, "TT17", f"{ten}: {', '.join(loi)} — 897 Checklist {nguon}"))

    # Phan dau (bang dau tien). Vai tro theo VI TRI dong o cot trai (08 muc 7): dong 1 = co quan chu quan (13, KHONG dam),
    # dong 2 = don vi ban hanh (13, dam). Mau 2.1: UBND TINH QUANG NGAI / TRUONG CAO DANG KON TUM; mau 2.2 (van ban
    # cua don vi): TRUONG CAO DANG KON TUM / PHONG, KHOA... — o mau 2.2 ten Truong la chu quan (29/9/2026: phep do cu
    # coi ten Truong luon la don vi ban hanh, bao nham BC cua Phong).
    if d.tables:
        for r_ in d.tables[0].rows:
            for c in r_.cells:
                dong = [p for p in c.paragraphs if p.text.strip() and p.text.strip().isupper()
                        and not re.match(r"Số\s*:", p.text.strip())]
                if dong and "CỘNG H" not in dong[0].text.upper() and "ĐẢNG" not in dong[0].text.upper():
                    if len(dong) >= 2:
                        sai("Tên cơ quan chủ quản", dong[0], co=13, dam=False)
                        sai("Tên đơn vị ban hành", dong[1], co=13, dam=True)
                    elif dong[0].text.strip().upper() == "TRƯỜNG CAO ĐẲNG KON TUM":
                        sai("Tên đơn vị ban hành", dong[0], co=13, dam=True)
                    break
            else:
                continue
            break
        for p in _doan_trong_bang_dau(d):
            t = p.text.strip()
            tu = t.upper()
            if re.match(r"Số\s*:", t):
                sai("Số, ký hiệu", p, co=13, dam=False)
                m = re.match(r"Số\s*:(\s*)/", t)
                if m and len(m.group(1)) < 6:
                    kq.append((3, "TT17", f"Sau “Số:” chỉ để trống {len(m.group(1))} ký tự — tối thiểu 6 (897 Checklist 01 mục 1.4)"))
                if re.match(r"Số\s*:\s*[1-9]/", t):
                    kq.append((3, "TT17", "Số nhỏ hơn 10 phải thêm số 0 phía trước (897 Checklist 01 mục 1.4)"))
            elif ", ngày" in t:
                sai("Địa danh, ngày tháng", p, co=14)

    # Ten loai, trich yeu, can cu (ngoai bang)
    ps = [p for p in d.paragraphs]
    i_loai = next((i for i, p in enumerate(ps[:12]) if p.text.strip() in LOAI_VB.values()), None)
    if i_loai is not None:
        sai("Tên loại văn bản", ps[i_loai], co=14, dam=True)
        ty, co_ke = [], False
        for p in ps[i_loai + 1:i_loai + 6]:
            t = p.text.strip()
            x = p._p.xml
            co_ke |= "<w:drawing" in x or "<w:pict" in x or bool(re.search(r"<w:pBdr>.*?<w:bottom ", x, re.S))
            if not t:
                if ty:
                    break
                continue
            if t.startswith("Căn cứ") or (p.paragraph_format.first_line_indent or 0) > 0:
                break
            ty.append(p)
        for p in ty:
            sai("Trích yếu", p, co=14, dam=True)
        if ty and not co_ke:
            kq.append((2, "TT18", "Thiếu đường kẻ ngang dưới trích yếu (dài 1/3–1/2 dòng chữ) — 897 Checklist 01 mục 1.6"))
    for p in ps:
        if p.text.strip().startswith("Căn cứ"):
            sai("Căn cứ", p, co=14, nghieng=True)

    # Nguoi ky, noi nhan (bang co "Nơi nhận")
    for t in d.tables[1:]:
        o = [c for r in t.rows for c in r.cells]
        if not any(p.text.strip().startswith("Nơi nhận") for c in o for p in c.paragraphs):
            continue
        # khoi chu ky co the chia 2 hang (mau 03A: chuc vu hang 1, ho ten hang 2) -> gom moi o khong phai "Noi nhan"
        ky, da = [], set()
        for c in o:
            if c._tc in da:
                continue
            da.add(c._tc)
            dps = [p for p in c.paragraphs if p.text.strip()]
            if dps and not dps[0].text.strip().startswith("Nơi nhận"):
                ky += dps
        for c in [c for c in o if c.paragraphs and c.paragraphs[0].text.strip().startswith("Nơi nhận")][:1] + [None]:
            if c is None:
                dps = ky
            else:
                dps = [p for p in c.paragraphs if p.text.strip()]
            if not dps:
                continue
            if dps[0].text.strip().startswith("Nơi nhận"):
                sai("Từ “Nơi nhận”", dps[0], co=12, dam=True, nghieng=True)
                for p in dps[1:]:
                    sai("Danh sách nơi nhận", p, co=11)  # khong xet dam: mau 09 dam rieng dau "-" dong Luu
                if not re.match(r"-\s*Lưu\s*:\s*VT", dps[-1].text.strip()):
                    kq.append((3, "TT17", "Dòng cuối nơi nhận phải là “- Lưu: VT, <đơn vị soạn thảo>.” (897 Checklist 01 mục 1.9)"))
                continue
            chuc = [p for p in dps if p.text.strip().isupper()]
            for p in chuc:
                sai("Quyền hạn, chức vụ người ký", p, co=14, dam=True)
                if re.match(r"(K/T|T/L|TU/Q)", p.text.strip()):
                    kq.append((2, "TT19", f"“{p.text.strip()[:12]}” — hệ hành chính dùng KT./TL./TUQ. có dấu chấm (897 Checklist 08 mục 5.1)"))
            if chuc and dps[-1] not in chuc:
                ten = dps[-1]
                sai("Họ tên người ký", ten, co=14, dam=True)
                if HOC_HAM.match(ten.text.strip()):
                    kq.append((2, "TT19", f"Ghi học hàm, học vị trước họ tên người ký “{ten.text.strip()}” (897 Checklist 01 mục 1.8)"))
    return kq


def _doan_trong_bang_dau(d):
    da, kq = set(), []
    for r in d.tables[0].rows:
        for c in r.cells:
            if c._tc not in da:
                da.add(c._tc)
                kq += c.paragraphs
    return kq


# ------------------------------------------------------------------ kiem docx
def kiem_docx(d):
    """Tra ve list[(muc, ma, mo_ta)]."""
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    import unicodedata
    # Mau 03-Templates(1)/03A luu chu dang NFD ("â" + dau nang to hop) -> moi phep so chu ("Nơi nhận", "Căn cứ"...)
    # truot va phep kiem im lang bo qua (28/9/2026). Chuan hoa NFC trong bo nho truoc khi do (khong ghi tep).
    for t in d.element.body.iter(f"{W}t"):
        if t.text:
            t.text = unicodedata.normalize("NFC", t.text)
    kq = []
    g = GiaiDocx(d)

    # TT01 kho giay, TT02 le — moi section
    for i, s in enumerate(d.sections, 1):
        w, h = s.page_width.cm, s.page_height.cm
        ngang = w > h
        a4 = abs(min(w, h) - 21.0) <= 0.1 and abs(max(w, h) - 29.7) <= 0.1
        if not a4:
            kq.append((2, "TT01", f"Section {i}: khổ {w:.1f}×{h:.1f} cm — phải A4 (21×29,7)"))
        le = {"trên": s.top_margin.cm, "dưới": s.bottom_margin.cm,
              "trái": s.left_margin.cm, "phải": s.right_margin.cm}
        if not ngang:  # trang ngang (phu luc bang) khong ap le doc
            sai = [f"{k} {round(v, 2)}" for k, v in le.items()
                   if not (LE[k][0] - EPS <= round(v, 2) <= LE[k][1] + EPS)]
            if sai:
                kq.append((2, "TT02", f"Section {i}: lề ngoài khoảng NĐ 30 ({', '.join(sai)} cm). "
                           "Mẫu 03-Templates(1): trên 2 · dưới 2 · trái 3 · phải 2 cm"))

    doan = list(d.paragraphs)
    tat_ca = doan + list(_doan_trong_bang(d))

    # TT03 phong chu, TT05 mau chu
    sai_phong = collections.Counter()
    mau_chu = 0
    for p in tat_ca:
        for r in p.runs:
            if not r.text.strip():
                continue
            f = g.phong(r, p)
            if f != PHONG:
                sai_phong[f or "(không xác định)"] += 1
            c = r.font.color
            if c is not None and c.type is not None and c.rgb is not None and str(c.rgb) not in ("000000",):
                mau_chu += 1
    # Bien the ten cua chinh TNR ("Times New Roman Bold", "TimesNewRomanPSMT" — thuong do chep tu PDF):
    # hien thi van la TNR tren may co phong chuan, nhung may khac co the thay phong -> Muc 3.
    bien_the = {k: v for k, v in sai_phong.items() if re.sub(r"[\s\-]", "", k or "").lower().startswith("timesnewroman")}
    khac = {k: v for k, v in sai_phong.items() if k not in bien_the}
    if khac:
        kq.append((2, "TT03", f"{sum(khac.values())} đoạn chữ không phải {PHONG}: "
                   + ", ".join(f"{k}×{v}" for k, v in collections.Counter(khac).most_common(4))
                   + (" — .VnTime là phông TCVN3 cũ, phải chuyển Unicode" if any(".Vn" in (k or "") for k in khac) else "")))
    if bien_the:
        kq.append((3, "TT03b", f"{sum(bien_the.values())} đoạn chữ dùng biến thể tên phông "
                   + ", ".join(bien_the) + f" — đặt lại đúng tên “{PHONG}”"))
    if mau_chu:
        kq.append((3, "TT05", f"{mau_chu} đoạn chữ có màu khác đen (NĐ 30: màu đen)"))

    # Doan noi dung: ngoai bang, dai >= 60 ky tu
    noi_dung = [p for p in doan if len(p.text.strip()) >= 60]
    co = collections.Counter()
    for p in noi_dung:
        for r in p.runs:
            if r.text.strip():
                co[g.co(r, p)] += len(r.text)
    if co:
        chinh = co.most_common(1)[0][0]
        if chinh != 14:
            kq.append((2, "TT04", f"Cỡ chữ phần nội dung chủ yếu là {chinh:g} — TB 597: cỡ 14"))
        lech = {k: v for k, v in co.items() if k != chinh and v > 0.05 * sum(co.values())}
        if lech:
            kq.append((3, "TT04b", "Cỡ chữ lời văn không thống nhất: "
                       + ", ".join(f"cỡ {k:g} ({v} ký tự)" for k, v in lech.items())))
        khong_deu = sum(1 for p in noi_dung if g.can_le(p) not in (WD_ALIGN_PARAGRAPH.JUSTIFY, None)
                        and g.can_le(p) != WD_ALIGN_PARAGRAPH.CENTER)
        if khong_deu > 0.2 * len(noi_dung):
            kq.append((3, "TT06", f"{khong_deu}/{len(noi_dung)} đoạn nội dung không dàn đều hai lề"))
        gian = [p.paragraph_format.line_spacing for p in noi_dung]
        qua = sum(1 for x in gian if isinstance(x, float) and x > 1.5 + 1e-6)
        hep = sum(1 for x in gian if x is not None and not isinstance(x, float) and x.pt < 15 - 0.1)
        if qua or hep:
            kq.append((3, "TT07", f"Cách dòng ngoài khoảng single/15pt → 1,5 lines: {qua} đoạn >1,5; "
                       f"{hep} đoạn exactly <15pt"))

    # TT08 phan dau the thuc (bang dau tien)
    dau = "\n".join(p.text for p in (list(_doan_trong_bang(d))[:12] if d.tables else doan[:8]))
    dau_up = dau.upper()
    la_vb_hanh_chinh = "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" in dau_up or "CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM" in dau_up
    if la_vb_hanh_chinh:
        if "TRƯỜNG CAO ĐẲNG KON TUM" not in dau_up:
            kq.append((2, "TT08", "Phần đầu thiếu tên đơn vị ban hành “TRƯỜNG CAO ĐẲNG KON TUM”"))
        if "UBND TỈNH KON TUM" in dau_up or "ỦY BAN NHÂN DÂN TỈNH KON TUM" in dau_up:
            kq.append((2, "TT08", "Cơ quan chủ quản ghi “UBND TỈNH KON TUM” — văn bản mới dùng “UBND TỈNH QUẢNG NGÃI”"))
        elif "QUẢNG NGÃI" not in dau_up:
            kq.append((2, "TT08", "Phần đầu thiếu cơ quan chủ quản “UBND TỈNH QUẢNG NGÃI”"))
        for p in _doan_trong_bang(d):
            t = p.text.strip().upper()
            rs = [r for r in p.runs if r.text.strip()]
            if not rs:
                continue
            if t.startswith("CỘNG H") and "VIỆT NAM" in t:
                cs = {g.co(r, p) for r in rs}
                if cs != {13.0}:
                    kq.append((2, "TT09", f"Quốc hiệu cỡ {sorted(cs)} — TB 597: cỡ 13, đậm"))
            if t.startswith("ĐỘC LẬP"):
                cs = {g.co(r, p) for r in rs}
                if cs != {14.0}:
                    kq.append((2, "TT09", f"Tiêu ngữ cỡ {sorted(cs)} — TB 597: cỡ 14, đậm"))
                if any(r.font.underline for r in rs):
                    kq.append((3, "TT09", "Tiêu ngữ dùng Underline — TB 597: kẻ đường bằng Draw"))
        kq += _kiem_bang_tieu_de(d, g)
        kq += _kiem_thanh_phan_897(d, g)

    # TT16 doan "Can cu" ngoai bang phai thut dau dong nhu doan noi dung (TB 1060, 1092 da ban hanh: 1,25 cm)
    can_cu = [p for p in doan if p.text.strip().startswith("Căn cứ")]
    thut = [p for p in noi_dung if not p.text.strip().startswith("Căn cứ")
            and (p.paragraph_format.first_line_indent or 0) > 0]
    khong_thut = [p for p in can_cu if not (p.paragraph_format.first_line_indent or 0) > 0]
    if khong_thut and thut:
        kq.append((3, "TT16", f"{len(khong_thut)} đoạn “Căn cứ…” không thụt đầu dòng trong khi đoạn nội dung có thụt — "
                   "văn bản đã ban hành: căn cứ thụt 1,25 cm, nghiêng"))

    # TT10 "Noi nhan"
    for p in tat_ca:
        if p.text.strip().startswith("Nơi nhận"):
            rs = [r for r in p.runs if r.text.strip()]
            cs = {g.co(r, p) for r in rs}
            if cs and cs != {12.0}:
                kq.append((3, "TT10", f"“Nơi nhận” cỡ {sorted(cs)} — TB 597: cỡ 12, nghiêng, đậm"))
            break

    # TT11b so trang hien o trang 1 (897 Checklist 05 muc 4.3) — ban TB 28/9/2026 dung tu ghep TB 1060 hien "1"
    #   (ban do la CHU "1" co dinh trong header trang dau, khong phai truong PAGE) -> xet ca truong PAGE lan chu
    s0 = d.sections[0]
    tp = s0._sectPr.find(f"{W}titlePg")
    co_titlepg = tp is not None and tp.get(f"{W}val") not in ("0", "false")
    dau_trang1 = s0.first_page_header if co_titlepg else s0.header
    if not dau_trang1.is_linked_to_previous or co_titlepg:
        x1 = dau_trang1._element.xml
        chu1 = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", x1)).strip()
        if "PAGE" in x1 or re.search(r"\d", chu1):
            kq.append((2, "TT11b", f"Trang thứ nhất hiện số trang/chữ ở đầu trang (“{chu1 or 'PAGE'}”) — 897 Checklist "
                       "05 mục 4.3: không hiển thị số trang thứ nhất"))

    # TT11 so trang: co truong PAGE o header
    if len(noi_dung) > 25:
        co_page = any("PAGE" in (s.header._element.xml if s.header is not None else "") for s in d.sections)
        if not co_page:
            kq.append((3, "TT11", "Văn bản nhiều trang nhưng không có số trang (canh giữa lề trên, ẩn trang 1)"))
    kq.sort(key=lambda x: x[0])
    return kq


# ------------------------------------------------------------------ kiem xlsx
def kiem_xlsx(wb):
    kq = []
    for ws in wb.worksheets:
        if ws.sheet_state != "visible" or ws.max_row < 2:
            continue
        ps = ws.page_setup
        if ps.paperSize not in (None, 9, "9"):
            kq.append((2, "TX01", f"[{ws.title}] khổ giấy in mã {ps.paperSize} — phải A4 (mã 9)"))
        f = collections.Counter()
        co = collections.Counter()
        for row in ws.iter_rows(max_row=min(ws.max_row, 400)):
            for c in row:
                if c.value is not None and str(c.value).strip():
                    f[c.font.name] += 1
                    co[c.font.sz] += 1
        sai = {k: v for k, v in f.items() if k != PHONG}
        if sai:
            kq.append((2, "TX02", f"[{ws.title}] {sum(sai.values())} ô không phải {PHONG}: "
                       + ", ".join(f"{k}×{v}" for k, v in list(sai.items())[:4])))
        if co:
            chinh = co.most_common(1)[0][0]
            if chinh is not None and not (12 <= chinh <= 14):
                kq.append((3, "TX03", f"[{ws.title}] cỡ chữ chủ yếu {chinh:g} — mẫu 05B dùng 12–14"))
        if ws.max_column > 6 and ps.orientation != "landscape" and not ps.fitToWidth:
            kq.append((4, "TX04", f"[{ws.title}] bảng {ws.max_column} cột in dọc, không đặt vừa trang — "
                       "mẫu 05B: A4 ngang"))
    kq.sort(key=lambda x: x[0])
    return kq


def kiem_tep(p):
    if p.lower().endswith((".docx", ".dotx")):
        return kiem_docx(mo_mau(p))
    if p.lower().endswith((".xlsx", ".xltx")):
        import warnings
        import openpyxl
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return kiem_xlsx(openpyxl.load_workbook(p))
    raise ValueError(f"Không kiểm được loại tệp: {p}")


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--tao":
        print("Đã tạo", tao_tu_mau(argv[1], argv[2]))
        return 0
    if argv[0] == "--khung":
        print("Đã tạo", tao_khung(argv[1], argv[2] if len(argv) > 2 else "TB"))
        return 0
    xau = False
    for p in argv:
        kq = kiem_tep(p)
        print(f"\n=== {p} — {len(kq)} gợi ý ===")
        if not kq:
            print("  ✓ Đạt chuẩn thể thức theo các phép kiểm TT/TX.")
        for muc, ma, mo_ta in kq:
            print(f"  [Mức {muc}] {ma}: {mo_ta}")
        xau |= any(x[0] <= 2 for x in kq)
    return 1 if xau else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/kiem_vien_dan.py` (9824 byte, sha256 `47ed106a59a60a12d769daf985389f86463f5bc2a28ac62e425197c700c3544f`)

`````python
# -*- coding: utf-8 -*-
"""Tu kiem phan CAN CU va VIEN DAN cua du thao van ban hanh chinh — DL-20260919-002.

Quy tac: 20-Chuan-Chung/17-Quy-Tac-Vien-Dan.md (NĐ 30/2020 Phu luc I Phan I Muc II khoan 6,
Phu luc II Muc V khoan 7; Phap lenh 01/2012/UBTVQH13 sua doi 2026 Dieu 4; quy uoc Truong qua 897).

Chi PHAT HIEN va GOI Y muc — khong sua tep. Muc chinh thuc do ra soat KTC-Ra-Soat-897 ket luan.
Khong tra hieu luc van ban (viec do phai doi chieu kho 01-04).

Chay:  python 29-Cong-Cu/kiem_vien_dan.py <tep .docx|.md|.txt> [...]
Ma thoat: 1 neu co goi y Muc 1, nguoc lai 0.
"""
import os
import re
import sys

# Van ban Truong da bi thay the (03-Phap-Ly.md cua 897, muc 3)
DA_THAY = [
    (r"\b49/QĐ-CĐKT", "QĐ 49/QĐ-CĐKT", "QĐ 1976/QĐ-CĐKT (14/9/2026)"),
    (r"\b988/QĐ-CĐKT", "QĐ 988/QĐ-CĐKT", "QĐ 1976/QĐ-CĐKT (14/9/2026)"),
    (r"\b215/QĐ-CĐKT", "QĐ 215/QĐ-CĐKT", "QĐ 389/QĐ-CĐKT (26/02/2026)"),
    (r"\b50/QĐ-CĐKT", "QĐ 50/QĐ-CĐKT", "QĐ 1299/QĐ-CĐKT (27/5/2026)"),
    (r"\b1060/QĐ-CĐKT", "QĐ 1060/QĐ-CĐKT", "QĐ 1400/QĐ-CĐKT (12/6/2026)"),
    (r"\b340/TB-CĐCĐ", "TB 340/TB-CĐCĐ", "TB 597/TB-CĐKT (19/5/2026)"),
    (r"\b109/CĐCĐ-HCQT", "CV 109/CĐCĐ-HCQT", "TB 597/TB-CĐKT (19/5/2026)"),
]

SO_LUAT = r"số\s+\d+/\d{4}/(?:QH|UBTVQH)\d+"
LA_CAN_CU = re.compile(r"^\s*[-–—•+*]?\s*Căn cứ\b")
GACH_DAU = re.compile(r"^\s*[-–—•+*]\s*Căn cứ\b")
LA_XET = re.compile(r"^\s*Xét\b")
DAU_VB = 60  # so doan dau van ban chua khoi can cu ban hanh


def doc_tep(p):
    """Tra ve danh sach doan van (paragraph) — .docx doc bang python-docx."""
    if p.lower().endswith(".docx"):
        import docx
        d = docx.Document(p)
        doan = [x.text for x in d.paragraphs]
        for bang in d.tables:           # tieu de van ban thuong nam trong bang
            for hang in bang.rows:
                for o in hang.cells:
                    doan.extend(x.text for x in o.paragraphs)
        return doan
    # 1.3.2 (tham dinh lan 4, Gemini): tep van ban khong phai UTF-8 (xuat tu Word/Notepad cu: UTF-16, cp1258,
    # cp1252) khong duoc lam script dung giua chung. Thu lan luot; bang ma cuoi cung doc duoc thi bao ra stderr.
    raw = open(p, "rb").read()
    for bm in ("utf-8-sig", "utf-16", "cp1258", "cp1252"):
        if bm == "utf-16" and not raw.startswith((b"\xff\xfe", b"\xfe\xff")):
            continue
        try:
            s = raw.decode(bm)
        except UnicodeDecodeError:
            continue
        if bm not in ("utf-8-sig",):
            sys.stderr.write(f"Lưu ý: {p} không phải UTF-8 — đã đọc theo bảng mã {bm}; kiểm lại dấu tiếng Việt.\n")
        import unicodedata
        # cp1258 luu dau thanh dang to hop -> chuan hoa NFC de mau regex ("Căn cứ") khop
        return unicodedata.normalize("NFC", s).splitlines()
    raise SystemExit(f"Không đọc được {p}: không nhận dạng được bảng mã (thử UTF-8, UTF-16, cp1258, cp1252).")


def _la_qd_hieu_truong(doan):
    """Quyet dinh cua Hieu truong: co ten loai QUYẾT ĐỊNH va tham quyen HIỆU TRƯỞNG."""
    van = "\n".join(doan)
    return bool(re.search(r"^\s*QUYẾT ĐỊNH\s*$", van, re.M)) and "HIỆU TRƯỞNG" in van


def kiem_tra(doan):
    """doan: list[str]. Tra ve list[(muc, ma, so_dong, trich, mo_ta)] — so_dong tinh tu 1."""
    kq = []

    def them(muc, ma, i, mo_ta):
        kq.append((muc, ma, i + 1, doan[i].strip()[:90], mo_ta))

    # Khoi can cu ban hanh: nam o DAU van ban (DAU_VB doan dau). "Căn cứ …" sau do la cau van trong noi
    # dung (vd. So tay "Căn cứ vào báo cáo…") — khong ap quy tac dong can cu. Thu that 19/9/2026 tren kho 02.
    khoi = [i for i, s in enumerate(doan[:DAU_VB]) if LA_CAN_CU.match(s) or LA_XET.match(s)]
    can_cu = [i for i in khoi if LA_CAN_CU.match(doan[i])]

    for i in can_cu:
        s = doan[i]
        la_luat = re.search(r"Căn cứ\s+(Bộ luật|Luật|Pháp lệnh)\s+[A-ZĐ]", s)
        if la_luat and not re.search(r"ngày\s+\d{1,2}(\s+tháng\s+\d{1,2}\s+năm\s+|/)\d", s):
            them(2, "VD02", i, "Căn cứ Luật/Pháp lệnh ghi tên và ngày ban hành — dòng này thiếu ngày "
                 "(897, 02-Noi-Dung mục 1 dòng 4)")
        if re.search(r"Căn cứ\s+(các\s+)?Văn bản hợp nhất", s):
            them(3, "VD03", i, "VBHN đứng làm căn cứ chính — ghi văn bản gốc trước, VBHN đặt trong ngoặc "
                 "“(hợp nhất tại Văn bản hợp nhất số …)”")
        if re.search(r"Luật số\s+\d+/\d{4}/QH\d+", s) and not re.search(r"Luật\s+[A-ZĐ]\w", s):
            them(2, "VD05", i, "Chỉ dẫn luật sửa đổi, thiếu tên luật gốc được sửa đổi, bổ sung")
        if GACH_DAU.match(s):
            them(2, "VD07", i, "Gạch đầu dòng trước “Căn cứ” là quy tắc văn bản Đảng — văn bản hành chính "
                 "không dùng")

    # VD06 — dau cuoi dong trong khoi can cu
    if khoi:
        # chi xet cum lien tiep dau tien (bo qua dong trong giua cac can cu)
        cum = [khoi[0]]
        for i in khoi[1:]:
            if all(not doan[j].strip() for j in range(cum[-1] + 1, i)):
                cum.append(i)
            else:
                break
        for k, i in enumerate(cum):
            cuoi = doan[i].rstrip()
            can = "." if k == len(cum) - 1 else ";"
            if not cuoi.endswith(can):
                them(2, "VD06", i, f"Cuối dòng căn cứ phải là “{can}” (dòng giữa “;”, dòng cuối “.”)")

    # VD08 — QD cua Hieu truong: can cu dau tien la QD 1976
    # Dan doi truoc cua QD 1976 (49, 988) o vi tri dau: dung vi tri, chi co the sai doi -> de VD09 bao
    if can_cu and _la_qd_hieu_truong(doan) and not re.search(
            r"\b(1976|988|49)/QĐ-CĐKT", doan[can_cu[0]]):
        them(1, "VD08", can_cu[0], "Quyết định của Hiệu trưởng: căn cứ đầu tiên phải là Quyết định số "
             "1976/QĐ-CĐKT ngày 14/9/2026 (897, 08-Quy-Uoc-Rieng-CDKT mục 1) — áp cho dự thảo ban hành "
             "từ 14/9/2026; văn bản cũ đối chiếu văn bản hiệu lực tại ngày ban hành")

    for i, s in enumerate(doan):
        if re.search(r"(Bộ luật|Luật|Pháp lệnh)\s+[A-ZĐ][^;\n]{0,120}?" + SO_LUAT, s):
            them(2, "VD01", i, "Văn bản hành chính: viện dẫn Luật/Pháp lệnh không ghi số hiệu, kể cả khi đã "
                 "có VBHN — chỉ ghi tên (và ngày ban hành ở phần căn cứ). NĐ 30 PL I, Phần I, Mục II, "
                 "khoản 6; 897 02-Noi-Dung dòng 4")
        if re.search(r"Pháp lệnh[^;.\n]{0,160}?của Quốc hội", s) and "Thường vụ" not in s:
            them(2, "VD04", i, "Pháp lệnh do Ủy ban Thường vụ Quốc hội ban hành, không phải Quốc hội")
        for mau, cu, moi in DA_THAY:
            # "…thay thế/bãi bỏ Quyết định số 215/QĐ-CĐKT" la dieu khoan bai bo, khong phai vien dan
            if re.search(mau, s) and not re.search(
                    r"(thay thế|bãi bỏ|hết hiệu lực)[^.;]{0,80}?" + mau, s):
                them(1, "VD09", i, f"{cu} đã bị thay thế bởi {moi} — chỉ hợp lệ nếu dự thảo ban hành "
                     "trước ngày thay thế")
        if LA_CAN_CU.match(s) and re.search(r"checklist|Checklist|\.md\b|\.docx\b|biểu mẫu nội bộ|"
                                           r"KTC-Ra-Soat|Skill-Library", s):
            them(1, "VD10", i, "Không dẫn mẫu/checklist/tệp nội bộ làm căn cứ pháp lý")
        for m in re.finditer(r"(?:khoản\s+\d+\s+|điểm\s+[a-zđ]\s+(?:khoản\s+\d+\s+)?)?"
                             r"\b(điều|chương|tiểu mục)\s+(\d+|[IVXL]+)\b", s):
            them(3, "VD11", i, f"Viết hoa “{m.group(1).capitalize()} {m.group(2)}” khi viện dẫn "
                 "(NĐ 30, Phụ lục II, Mục V, khoản 7)")
            break

    # VD12 — cung so ky hieu xuat hien lai kem trich yeu day du (sau lan dau)
    da_gap = {}
    for i, s in enumerate(doan):
        for m in re.finditer(r"(?:Quyết định|Nghị định|Thông tư|Thông báo|Kế hoạch)\s+số\s+"
                             r"(\d+/[\w\-/Đ]+)\s+ngày[^;.\n]{0,40}?(?:của|về|ban hành|quy định)", s):
            so = m.group(1)
            if so in da_gap and not LA_CAN_CU.match(s):
                them(4, "VD12", i, f"{so} đã viện dẫn đầy đủ ở dòng {da_gap[so] + 1} — lần sau chỉ ghi tên "
                     "loại và số, ký hiệu (NĐ 30, Phụ lục I, Phần I, Mục II, khoản 6 điểm b)")
            else:
                da_gap.setdefault(so, i)
    kq.sort(key=lambda x: (x[0], x[2]))
    return kq


def in_bao_cao(ten, kq):
    print(f"\n=== {ten} — {len(kq)} gợi ý ===")
    if not kq:
        print("  ✓ Không phát hiện lỗi viện dẫn theo 12 phép kiểm VD01–VD12.")
    for muc, ma, dong, trich, mo_ta in kq:
        print(f"  [Mức {muc}] {ma} dòng {dong}: {mo_ta}\n           “{trich}”")
    print("  Lưu ý: công cụ không tra hiệu lực văn bản — đối chiếu kho 01-04 và rà soát 897 vẫn bắt buộc.")


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    co_muc_1 = False
    for p in argv:
        if not os.path.isfile(p):
            print(f"✗ không thấy tệp {p}")
            return 2
        kq = kiem_tra(doc_tep(p))
        in_bao_cao(p, kq)
        co_muc_1 |= any(x[0] == 1 for x in kq)
    return 1 if co_muc_1 else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/kpi_calc.py` (14203 byte, sha256 `9532b0702bcdcac600762817a052315b3edf790d9b52dfd2795ffd5aea44aacb`)

`````python
# -*- coding: utf-8 -*-
"""Tinh toan KPI ca nhan theo QD 1923/QD-CDKT (30/8/2026) — ham thuan, co dan Dieu. Skill ktc-kpi-lap-ke-hoach.

Mo hinh KHONG duoc tu nham: moi con so (he so, so luong quy doi, diem, xep loai) di qua day.

HE SO QUY DOI — Cau hoi mo so 1 (28-KTC-KPI/references/Cau-Hoi-Mo.md). KHONG CO MAC DINH; goi thieu phuong an -> loi.
  muc-do    He so theo 4 muc do (Thap 1,0 · Trung binh 1,2 · Cao 1,5 · Kho va phuc tap 2,0)
            [QD 1923, Phu luc II — ghi chu muc do cong viec; Phu luc I cot (7)(9)(10)]  -> CO VAN BAN
  A         He so san pham theo Danh muc QD 2119/QD-CDKT ngay 28/9/2026 (theo tung san pham) -> CO VAN BAN (chinh thuc,
            thay the danh muc du thao kem TB 1052 — DL-20260928-001)
  AxB       A (QD 2119) x B (muc do) — quy uoc Phong TH-HC&QT ghi nhan 24/9/2026; QD 2119 CHI quy dinh he so A, phep
            nhan voi muc do CHUA CO VAN BAN
  nhap-tay  Nguoi dung nhap he so, tu chiu trach nhiem ve can cu

Chay (JSON vao -> JSON ra):
  python 29-Cong-Cu/kpi_calc.py he-so     --phuong-an muc-do --muc-do "Cao"
  python 29-Cong-Cu/kpi_calc.py quy-doi   --json ke_hoach.json --phuong-an muc-do
  python 29-Cong-Cu/kpi_calc.py diem      --ty-le 105 --diem-toi-da 45
  python 29-Cong-Cu/kpi_calc.py xep-loai  --tong 89.99
  python 29-Cong-Cu/kpi_calc.py tim       --tu-khoa "thoi khoa bieu" [--loai "Kế hoạch"]   # goi y STT Danh muc
"""
import argparse
import csv
import json
import os
import sys
import unicodedata

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PHUONG_AN = ("muc-do", "A", "AxB", "nhap-tay")
TRANG_THAI = {
    "muc-do": "Có văn bản: QĐ 1923/QĐ-CĐKT, Phụ lục II (ghi chú mức độ công việc)",
    "A": "Có văn bản: Danh mục sản phẩm, công việc ban hành kèm Quyết định số 2119/QĐ-CĐKT ngày 28/9/2026",
    "AxB": "CHƯA CÓ VĂN BẢN: hệ số A theo QĐ 2119/QĐ-CĐKT, phép nhân với mức độ (B) là quy ước Phòng TH-HC&QT ghi nhận "
           "24/9/2026, chờ Phòng TCCB&CTHSSV xác nhận",
    "nhap-tay": "Người dùng nhập — căn cứ do người lập kế hoạch tự chịu trách nhiệm",
}
# [QD 1923, Phu luc II, ghi chu] — ten muc theo danh sach chon (data validation) cua Phu luc I
MUC_DO = {"thap": 1.0, "trung binh": 1.2, "cao": 1.5, "kho va phuc tap": 2.0, "kho, phuc tap": 2.0}


class LoiKPI(ValueError):
    """Loi dau vao — skill phai dung va hoi nguoi dung, khong tu sua."""


def _kd(s):
    t = unicodedata.normalize("NFD", str(s or "").lower())
    return " ".join("".join(c for c in t if unicodedata.category(c) != "Mn").replace("đ", "d").split())


def muc_do_tu_chu(s):
    """'Khó và phức tạp', '... (mức độ cao)' -> khoa MUC_DO. Khong nhan ra -> None (khong doan)."""
    t = _kd(s)
    for k in sorted(MUC_DO, key=len, reverse=True):
        if t == k or f"muc do {k}" in t or t.endswith(f"({k})"):
            return k
    return None


# ------------------------------------------------------------------ danh muc QD 2119 (chinh thuc)
# QD 2119/QD-CDKT ngay 28/9/2026 thay the danh muc du thao kem TB 1052 (DL-20260928-001). CSV trich bang
# 29-Cong-Cu/trich_danh_muc_qd2119.py tu phu luc PL-2119 trong KTC-Database (kem sha256 nguon).
TEN_CSV = "he-so-san-pham-QD2119.csv"
_DM = None


def danh_muc(p=None):
    """{khoa: dong} tu CSV — khoa: 'ma:<ma san pham>', 'stt:<STT>', ten san pham chuan hoa."""
    global _DM
    if _DM is None or p:
        if not p:
            # du an · trong goi skill (scripts/../references) · ban chep o scripts/ goc cua plugin (../skills/...)
            here = os.path.dirname(os.path.abspath(__file__))
            ung = [os.path.join(DU_AN, "28-KTC-KPI", "references", "data"),
                   os.path.join(here, "..", "references", "data"),
                   os.path.join(here, "..", "skills", "kpi-lap-ke-hoach", "references", "data")]
            p = next((os.path.join(d, TEN_CSV) for d in ung if os.path.exists(os.path.join(d, TEN_CSV))), None)
            if not p:
                raise LoiKPI(f"Không thấy {TEN_CSV} (Danh mục QĐ 2119) — dừng, hỏi người dùng.")
        with open(p, encoding="utf-8-sig", newline="") as f:
            _DM = {}
            for h in csv.DictReader(f):
                _DM.setdefault("ma:" + h["ma_san_pham"].strip().upper(), h)
                _DM.setdefault("stt:" + str(h["stt"]).strip(), h)
                _DM.setdefault(_kd(h["ten_san_pham"]), h)
    return _DM


def tra_A(ma_hoac_ten):
    """Tra he so A theo MA SAN PHAM QD 2119 ('1.1.DA01.01'), STT phu luc ('1.1') hoac TEN SAN PHAM KHOP CHINH XAC
    (chuan hoa). Khong co -> LoiKPI: dung hoi, KHONG tu gan A [Cau hoi mo so 2]."""
    dm = danh_muc()
    k = str(ma_hoac_ten or "").strip()
    h = dm.get("ma:" + k.upper()) or dm.get("stt:" + k) or dm.get(_kd(k))
    if not h:
        raise LoiKPI(f"Sản phẩm '{ma_hoac_ten}' không có trong Danh mục ban hành kèm QĐ 2119/QĐ-CĐKT — dừng, hỏi người "
                     "dùng (THIEU_DU_LIEU; không tự gán hệ số A).")
    return float(h["he_so"]), h


def tim_danh_muc(tu_khoa, loai=None, toi_da=15):
    """GOI Y dong Danh muc chua DU MOI tu khoa — so TU NGUYEN VEN (khong dau, khong phan biet hoa thuong) trong
    ten/mo ta; 'thi' khong khop 'thien'. Chi liet ke de nguoi dung CHON — khong tu gan, khong cham diem giong
    (KI-001: khop gan dung de nham)."""
    import re
    tk = re.findall(r"\w+", _kd(tu_khoa))
    ra = []
    for k, h in danh_muc().items():
        if not k.startswith("stt:"):
            continue
        tu = set(re.findall(r"\w+", _kd(f"{h['ten_san_pham']} {h['mo_ta']}")))
        if tk and all(t in tu for t in tk) and (not loai or _kd(loai) == _kd(h["loai_san_pham"])):
            ra.append({"ma_san_pham": h["ma_san_pham"], "stt": h["stt"], "ten": h["ten_san_pham"],
                       "loai": h["loai_san_pham"], "nhom": h["nhom"], "he_so": float(h["he_so"]),
                       "lech_nhom": h["lech_nhom"]})
    return ra[:toi_da]


# ------------------------------------------------------------------ he so
def he_so(phuong_an, muc_do=None, san_pham=None, nhap=None):
    """He so quy doi 1 dau viec. Tra ve dict {he_so, phuong_an, trang_thai, canh_bao[]}."""
    if phuong_an not in PHUONG_AN:
        raise LoiKPI(f"Chưa chọn phương án hệ số (một trong {', '.join(PHUONG_AN)}) — Câu hỏi mở số 1, "
                     "không có mặc định.")
    cb = []
    B = None
    if phuong_an in ("muc-do", "AxB"):
        k = muc_do_tu_chu(muc_do)
        if k is None:
            raise LoiKPI(f"Mức độ '{muc_do}' không thuộc 4 mức của QĐ 1923 Phụ lục II "
                         "(Thấp · Trung bình · Cao · Khó và phức tạp).")
        B = MUC_DO[k]
    if phuong_an == "muc-do":
        hs = B
    elif phuong_an == "nhap-tay":
        if nhap is None or float(nhap) <= 0:
            raise LoiKPI("Phương án nhập tay nhưng chưa có hệ số > 0.")
        hs = float(nhap)
    else:
        A, dong = tra_A(san_pham)
        # 28/9/2026: A theo QD 2119/QD-CDKT (chinh thuc) -> KHONG con canh bao THANG_DIEM_CHUA_PHAN_DINH cho phuong an A.
        # A x B: QD 2119 chi quy dinh he so A; phep nhan voi muc do van chua co van ban -> giu ma canh bao.
        if phuong_an == "AxB":
            cb.append("THANG_DIEM_CHUA_PHAN_DINH: hệ số A theo QĐ 2119/QĐ-CĐKT, nhưng phép nhân A × mức độ chưa có văn bản "
                      "(quy ước Phòng TH-HC&QT, chờ Phòng TCCB&CTHSSV xác nhận) — không dùng làm số chính thức")
        if dong.get("lech_nhom"):
            cb.append(f"Hệ số A sản phẩm {dong['ma_san_pham']} ngoài tập hệ số của {dong['nhom']}: {dong['lech_nhom']}")
        if A > 10:
            cb.append(f"Hệ số A = {A} bất thường (sản phẩm {dong['ma_san_pham']}) — kiểm lại phụ lục QĐ 2119")
        hs = A if phuong_an == "A" else round(A * B, 4)
    return {"he_so": hs, "phuong_an": phuong_an, "trang_thai": TRANG_THAI[phuong_an], "canh_bao": cb}


def so_luong_quy_doi(so_luong, hs):
    """So luong quy doi = So luong x He so [mau Ke hoach Quy III, sheet KPI cot J = G*I]."""
    if so_luong is None or float(so_luong) < 0:
        raise LoiKPI("Số lượng phải là số ≥ 0 (Đ12.4 QĐ 1923: chỉ tiêu phải đo lường được).")
    return round(float(so_luong) * float(hs), 4)


# ------------------------------------------------------------------ diem
def diem_chi_tieu(ty_le, diem_toi_da):
    """Diem chi tieu = % hoan thanh x diem toi da; vuot 100% chi tinh tran, phan vuot ghi nhan dinh tinh
    [QD 1923, D11.6]."""
    if diem_toi_da < 0 or ty_le < 0:
        raise LoiKPI("Tỷ lệ và điểm tối đa phải ≥ 0.")
    tinh = min(float(ty_le), 100.0)
    return {"diem": round(tinh / 100 * diem_toi_da, 4), "vuot_muc": max(0.0, float(ty_le) - 100),
            "can_cu": "QĐ 1923, Đ11.6"}


def kiem_trong_so_truc(diem_toi_da_theo_truc, truc_chinh):
    """Tong = 70 diem (100%) [D11.3]; truc chinh >= 40% tong trong so [D12.3]. Tra ve danh sach loi."""
    loi = []
    tong = sum(diem_toi_da_theo_truc.values())
    if abs(tong - 70) > 1e-9:
        loi.append(("KP01", f"Tổng điểm tối đa các Trục = {tong:g}, phải = 70 (100%)", "QĐ 1923, Đ11.3"))
    ts = diem_toi_da_theo_truc.get(truc_chinh, 0) / tong * 100 if tong else 0
    if ts < 40 - 1e-9:
        loi.append(("KP02", f"Trục chính ({truc_chinh}) chiếm {ts:.2f}% < 40%", "QĐ 1923, Đ12.3"))
    return loi


def kiem_tieu_chi_chung(diem_toi_da_nhom):
    """3 nhom, moi nhom >= 5 diem, tong khong vuot 30 [D10.4]."""
    loi = []
    if len(diem_toi_da_nhom) != 3:
        loi.append(("KP03", f"Có {len(diem_toi_da_nhom)} nhóm tiêu chí chung, phải đúng 3", "QĐ 1923, Đ10"))
    for i, d in enumerate(diem_toi_da_nhom, 1):
        if d < 5 - 1e-9:
            loi.append(("KP04", f"Nhóm {i} tối đa {d:g} điểm < 05 điểm", "QĐ 1923, Đ10.4"))
    if sum(diem_toi_da_nhom) > 30 + 1e-9:
        loi.append(("KP05", f"Tổng 3 nhóm = {sum(diem_toi_da_nhom):g} > 30 điểm", "QĐ 1923, Đ10.4"))
    return loi


def muc_tieu_chi_chung(ty_le):
    """Muc dap ung tieu chi chung theo % diem toi da cua nhom [D10.5]."""
    t = float(ty_le)
    return 1 if t >= 90 else 2 if t >= 70 else 3 if t >= 50 else 4


def muc_trong_tam(ty_le):
    """Nhiem vu trong tam, then chot: 3 muc [D18]: >=90 · 60-<90 · <60."""
    t = float(ty_le)
    return 1 if t >= 90 else 2 if t >= 60 else 3


def xep_loai_theo_diem(tong):
    """Chi theo DIEM [D19.1 (ca nhan) / D7 (don vi)]: >=90 · 70-<90 · 50-<70 · <50.
    Dieu kien kem theo (100% nhiem vu, 30% vuot muc, bang kiem si so, gio giang...) CHUA kiem o day —
    du diem chua chac du muc [D7.5, D19.1]; quyet dinh thuoc Hieu truong [D14.3]."""
    t = float(tong)
    if not 0 <= t <= 100:
        raise LoiKPI(f"Tổng điểm {t:g} ngoài thang 0–100.")
    muc = ("Hoàn thành xuất sắc nhiệm vụ" if t >= 90 else "Hoàn thành tốt nhiệm vụ" if t >= 70 else
           "Hoàn thành nhiệm vụ" if t >= 50 else "Không hoàn thành nhiệm vụ")
    return {"muc_theo_diem": muc, "luu_y": "Chỉ theo điểm; điều kiện kèm theo chưa kiểm — không phải kết luận xếp loại",
            "can_cu": "QĐ 1923, Đ19.1"}


# ------------------------------------------------------------------ ke hoach (JSON)
def quy_doi_ke_hoach(kh, phuong_an):
    """kh = {"dau_viec":[{"truc":1,"noi_dung":..,"san_pham":..,"so_luong":..,"muc_do":..,"he_so":..}]}
    Tra ve cung cau truc, them he_so, so_luong_quy_doi; loi tung dong khong lam dung ca bang."""
    ra, loi = [], []
    for i, d in enumerate(kh.get("dau_viec", []), 1):
        try:
            h = he_so(phuong_an, d.get("muc_do"), d.get("ma_danh_muc") or d.get("san_pham"), d.get("he_so"))
            ra.append(dict(d, he_so=h["he_so"], so_luong_quy_doi=so_luong_quy_doi(d.get("so_luong"), h["he_so"]),
                           canh_bao=h["canh_bao"]))
        except LoiKPI as e:
            loi.append({"dong": i, "noi_dung": d.get("noi_dung", "")[:80], "loi": str(e)})
            ra.append(dict(d, he_so=None, so_luong_quy_doi=None))
    return {"phuong_an": phuong_an, "trang_thai": TRANG_THAI.get(phuong_an), "dau_viec": ra, "loi": loi}


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="lenh", required=True)
    p = sp.add_parser("he-so"); p.add_argument("--phuong-an"); p.add_argument("--muc-do")
    p.add_argument("--san-pham"); p.add_argument("--nhap", type=float)
    p = sp.add_parser("quy-doi"); p.add_argument("--json", required=True); p.add_argument("--phuong-an")
    p = sp.add_parser("diem"); p.add_argument("--ty-le", type=float, required=True)
    p.add_argument("--diem-toi-da", type=float, required=True)
    p = sp.add_parser("xep-loai"); p.add_argument("--tong", type=float, required=True)
    p = sp.add_parser("tim"); p.add_argument("--tu-khoa", required=True); p.add_argument("--loai")
    a = ap.parse_args(argv)
    try:
        if a.lenh == "he-so":
            out = he_so(a.phuong_an, a.muc_do, a.san_pham, a.nhap)
        elif a.lenh == "quy-doi":
            if a.phuong_an not in PHUONG_AN:
                raise LoiKPI(f"Chưa chọn phương án hệ số ({', '.join(PHUONG_AN)}) — Câu hỏi mở số 1.")
            out = quy_doi_ke_hoach(json.load(open(a.json, encoding="utf-8")), a.phuong_an)
        elif a.lenh == "tim":
            out = {"goi_y": tim_danh_muc(a.tu_khoa, a.loai),
                   "luu_y": "Chỉ là gợi ý — người dùng chọn mã sản phẩm; Danh mục chính thức theo QĐ 2119/QĐ-CĐKT"}
        elif a.lenh == "diem":
            out = diem_chi_tieu(a.ty_le, a.diem_toi_da)
        else:
            out = xep_loai_theo_diem(a.tong)
    except LoiKPI as e:
        print(json.dumps({"loi": str(e)}, ensure_ascii=False))
        return 2
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 1 if out.get("loi") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/kpi_danh_gia.py` (37320 byte, sha256 `dd93e0a7460226476115909f964b9f0e660d0072a039f251f9a8c5e4cc369867`)

`````python
# -*- coding: utf-8 -*-
"""Tu danh gia, de xuat xep loai ca nhan theo quy — skill ktc-kpi-tu-danh-gia (lenh 25/9/2026, giai doan 2).

Ba buoc, moi buoc mot lenh:
  1. sinh-bang-hoi : doc ke hoach KPI da duyet (.xlsx, 1 trong 6 mau Quy) -> bang hoi .xlsx (o vang de dien)
  2. (nguoi dung dien bang hoi)
  3. danh-gia      : doc ke hoach + bang hoi da dien -> tinh diem, doi chieu nguong + dieu kien -> TDG-KPI-....xlsx

KHONG tu cham thay nguoi dung (muc A, % hoan thanh, dieu kien deu do nguoi dung khai). KHONG tu quyet dinh muc xep
loai: chi in "muc theo nguong diem thuan tuy" va bang dieu kien (du / khong dat / thieu du lieu) — quyet dinh thuoc
Truong don vi va Hieu truong [QD 1923, D14.3c]. KHONG doi chieu tran ty le HTXS [D19.2] (giai doan 3).

Tinh diem (QD 1923):
  A = tong diem tu cham 3 nhom tieu chi chung (moi tieu chi con <= diem toi da cua mau); muc nhom theo D10.5.
  B = sum_Truc (% Truc x diem toi da Truc); % Truc = sum min(TB3chieu, SLqd) / sum SLqd — CHAN TRAN tung chi tieu
      [D11.6] (mau Quy III khong chan: Known-Issues-Bieu-Mau #7, Cau hoi mo so 9). TB3chieu theo cong thuc mau:
      (MIN(L,G)*I + I*L*N/100 + I*L*P/100) / 3.
  So sanh nguong tren gia tri chinh xac (chi khu nhieu dau phay dong 1e-6); hien thi cat (khong lam tron len).

  python kpi_danh_gia.py sinh-bang-hoi --ke-hoach KH.xlsx [--nhom ...] --ra Bang-hoi.xlsx
  python kpi_danh_gia.py danh-gia --ke-hoach KH.xlsx --bang-hoi Bang-hoi.xlsx [--nhom ...] --ra TDG.xlsx [--json]
Ma thoat: 2 = thieu du lieu / dung (hoi nguoi dung) · 1 = da xuat, co dieu kien khong dat hoac canh bao can xem · 0.
"""
import math
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kpi_calc as kc  # noqa: E402
import kpi_mau as km   # noqa: E402

MUC = ("Hoàn thành xuất sắc nhiệm vụ", "Hoàn thành tốt nhiệm vụ", "Hoàn thành nhiệm vụ", "Không hoàn thành nhiệm vụ")
KET_QUA_VIEC = ("Vượt mức", "Hoàn thành đúng hạn", "Hoàn thành chậm tiến độ", "Không hoàn thành")
TRONG_TAM = ("Không", "Mức 1", "Mức 2", "Mức 3")
CO_KHONG = ("Có", "Không")
NHOM_THIEU_PL = {"bo-mon": "XXIV", "giao-vu": "XXVI", "hanh-chinh": "XXVII", "ho-tro": "XXVIII"}
NHOM_CO_PL = {"truong-pho-don-vi": "XXIII", "nha-giao": "XXV"}
DONG_CUOI = ("Đề xuất của cá nhân — chưa phải kết luận của Trưởng đơn vị và Hiệu trưởng [QĐ 1923, Đ14.3c]. "
             "Trần tỷ lệ Hoàn thành xuất sắc theo nhóm tương đồng chưa được đối chiếu ở bước này [Đ19.2].")
VANG, XANH = "FFFFF2CC", "FFD9E1F2"
EPS = 1e-6


class Dung(Exception):
    """Dung, hoi nguoi dung (ma thoat 2)."""


def cat2(x):
    """Hien thi 2 chu so, CAT (khong lam tron len) — 89,996 hien 89,99, khong thanh 90,00."""
    return f"{math.floor(round(x, 6) * 100) / 100:.2f}".replace(".", ",")


def _so(v, ten):
    if v in (None, ""):
        return None
    try:
        return float(str(v).replace(",", ".").replace("%", "").strip())
    except ValueError:
        raise Dung(f"{ten}: '{v}' không phải số")


# ------------------------------------------------------------------ doc ke hoach
def doc_ke_hoach(p, nhom=None):
    wb = km.mo(p)
    nhom = nhom or km.nhan_nhom(wb)
    if nhom not in km.NHOM:
        raise Dung("Không xác định được nhóm vị trí từ tệp — chỉ rõ --nhom (một trong: " + ", ".join(km.NHOM) + ")")
    ct = km.cau_truc(wb)
    dg = km.cau_truc_danh_gia(wb)
    kh, kp = wb["Ke Hoach"], wb["KPI"]
    viec = []
    for n, (d, c) in sorted(ct["truc"].items()):
        for r in range(d, c + 1):
            nd = kh[f"B{r}"].value
            if nd in (None, ""):
                continue
            rk = ct["kpi_dong"][r]
            viec.append({"ma": f"B{r}", "truc": n, "dong_kh": r, "dong_kpi": rk, "noi_dung": str(nd).strip(),
                         "san_pham": kh[f"E{r}"].value, "so_luong": kh[f"F{r}"].value, "thoi_han": kh[f"G{r}"].value,
                         "muc_do": kh[f"D{r}"].value, "he_so": kh[f"I{r}"].value,
                         "cu": {c_: kp[f"{c_}{rk}"].value for c_ in km.O_THUC_TE}})
    ca_nhan = {}
    for r in range(4, 9):
        for m in re.finditer(r"(Họ và tên|Ngày sinh|Chức vụ Đảng|Chức vụ chính quyền|Chức vụ đoàn thể|"
                             r"Đơn vị công tác):\s*(.*?)(?=\s{2,}\S+.*?:|$)", str(kh[f"B{r}"].value or "")):
            v = m.group(2).strip()
            if v and not re.fullmatch(r"[.…\s]*", v):
                ca_nhan[m.group(1)] = v
    return {"tep": p, "nhom": nhom, "ct": ct, "dg": dg, "viec": viec, "ca_nhan": ca_nhan,
            "quan_ly": km.NHOM[nhom][2]}


# ------------------------------------------------------------------ cau hoi (muc C)
def cau_hoi_c(khd):
    """[(ma, cau hoi, lua chon | None (so), bat buoc, can cu)] — theo nhom vi tri va khoi II cua mau."""
    q = [("C01", "Trong quý, có tham gia đào tạo, bồi dưỡng TẬP TRUNG từ 02 tháng trở lên?", CO_KHONG, True,
          "QĐ 1923, Đ21.6a"),
         ("C02", "Lần đầu được bổ nhiệm chức danh lãnh đạo, quản lý, thời gian giữ chức vụ dưới 01 tháng trong quý?",
          CO_KHONG, True, "QĐ 1923, Đ21.6b"),
         ("C03", "Nghỉ ốm hoặc nghỉ thai sản từ 02 tháng trở lên trong quý?", CO_KHONG, True, "QĐ 1923, Đ21.6c"),
         ("C04", "Đang trong thời gian kiểm tra dấu hiệu vi phạm?", CO_KHONG, True, "QĐ 1923, Đ21.6d"),
         ("C05", "Đào tạo, bồi dưỡng tập trung, biệt phái, nghỉ ốm, thai sản chiếm từ 1/2 thời gian làm việc của quý "
          "trở lên?", CO_KHONG, True, "QĐ 1923, Đ21.4"),
         ("C06", "Trong kỳ, bị cấp có thẩm quyền kết luận suy thoái tư tưởng chính trị, đạo đức, lối sống, hoặc bị kỷ "
          "luật từ khiển trách trở lên do vi phạm liên quan thực hiện nhiệm vụ?", CO_KHONG, True,
          "QĐ 1923, Đ19.1d"),
         ("C07", "Đã khắc phục 100% hạn chế, khuyết điểm được chỉ ra ở kỳ kiểm điểm trước?",
          ("Có", "Không", "Kỳ trước không có hạn chế"), True, "QĐ 1923, Đ19.1a")]
    if khd["quan_ly"]:
        q += [("C08", "Đơn vị, bộ phận, lĩnh vực do mình trực tiếp lãnh đạo, quản lý đã hoàn thành 100% nhiệm vụ được "
               "giao trong quý?", ("Có", "Không", "Chưa có kết quả"), True, "QĐ 1923, Đ19.1a–c"),
              ("C09", "Đơn vị, bộ phận do mình trực tiếp quản lý hoàn thành DƯỚI 70% nhiệm vụ, hoặc trên 50% lĩnh vực "
               "mình phụ trách bị xếp loại Không hoàn thành?", ("Có", "Không", "Chưa có kết quả"), True,
               "QĐ 1923, Đ19.1d"),
              ("C10", "Có trên 50% phiếu tín nhiệm thấp tại kỳ lấy phiếu trong năm?",
               ("Có", "Không", "Không lấy phiếu"), True, "QĐ 1923, Đ19.1d"),
              ("C11", "Có đơn vị thuộc thẩm quyền phụ trách trực tiếp liên quan tham ô, tham nhũng, lãng phí và bị xử "
               "lý theo quy định?", CO_KHONG, True, "QĐ 1923, Đ19.1d"),
              ("C12", "Là NGƯỜI ĐỨNG ĐẦU đơn vị (Trưởng phòng, khoa, bộ môn, PKĐK)?", CO_KHONG, True,
               "QĐ 1923, Đ14.4, Đ19.4"),
              ("C13", "Kết quả xếp loại TẬP THỂ đơn vị mình kỳ này (nếu đã có)?", MUC + ("Chưa có",), True,
               "QĐ 1923, Đ14.4, Đ19.4")]
    for r, tt, nd, goi_y, gc in khd["dg"]["dieu_kien"]["muc"]:
        k = km._kd(nd)
        if "bang kiem" in k:
            lc = ("Đạt", "Không đạt", "Không áp dụng", "Chưa có kết quả")
        elif "gio giang" in k:
            lc = None
        else:
            lc = ("Có", "Không", "Không áp dụng", "Chưa có kết quả")
        q.append((f"D{tt}", f"{nd}" + (f" ({gc})" if gc else ""), lc, True, "QĐ 1923, Đ19.1 — mẫu Đánh giá mục II"))
    q += [("C14", "Có quý nào trước đó trong năm bị đánh giá dưới mức tối thiểu / Không hoàn thành nhiệm vụ?",
           ("Có", "Không", "Chưa có quý nào"), True, "QĐ 1923, Đ19.1a (lưu ý), Đ19.5 — Câu hỏi mở số 8"),
          ("C15", "TỰ ĐỀ XUẤT mức xếp loại chất lượng quý này (mục III của mẫu)", MUC, True, "mẫu Đánh giá mục III")]
    return q


# ------------------------------------------------------------------ bang hoi
def sinh_bang_hoi(khd, ra, quy=None, nam=None):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.worksheet.datavalidation import DataValidation
    if os.path.abspath(os.path.dirname(ra)) == km.thu_muc_mau():
        raise Dung("Không ghi vào thư mục mẫu assets/")
    f = Font(name=km.PHONG, size=12)
    fb = Font(name=km.PHONG, size=12, bold=True)
    vien = Border(*(Side(style="thin"),) * 4)
    vang = PatternFill("solid", fgColor=VANG)
    xanh = PatternFill("solid", fgColor=XANH)
    wrap = Alignment(wrap_text=True, vertical="top")
    wb = Workbook()
    ky = f"QUÝ {quy} NĂM {nam}" if quy and nam else "QUÝ …"
    ten = khd["ca_nhan"].get("Họ và tên", "…")

    def bang(ws, tieu_de, cot, rong):
        ws["A1"], ws["A2"] = tieu_de, (f"{ten} — {km.NHOM[khd['nhom']][0]} — {ky}. Chỉ điền ô nền vàng. "
                                       "Để trống ô bắt buộc thì công cụ dừng lại và hỏi, không tự chấm.")
        ws["A1"].font, ws["A2"].font = fb, f
        for i, (t, w) in enumerate(zip(cot, rong), 1):
            c = ws.cell(4, i, t)
            c.font, c.fill, c.border, c.alignment = fb, xanh, vien, Alignment(wrap_text=True, vertical="center")
            ws.column_dimensions[c.column_letter].width = w
        ws.freeze_panes = "A5"

    def o(ws, r, c, v, dien=False, dam=False):
        x = ws.cell(r, c, v)
        x.font, x.border, x.alignment = (fb if dam else f), vien, wrap
        if dien:
            x.fill = vang
        return x

    # --- A. Tieu chi chung
    ws = wb.active
    ws.title = "A-Tieu-chi-chung"
    bang(ws, "BẢNG HỎI TỰ ĐÁNH GIÁ — A. NHÓM TIÊU CHÍ CHUNG (30 ĐIỂM) [QĐ 1923, Đ10]",
         ("Mã", "Tiêu chí", "Điểm tối đa", "Điểm tự chấm", "Mức nhóm (tùy chọn)", "Khung mức Đ10.5 (theo nhóm)"),
         (7, 70, 10, 12, 14, 34))
    r = 5
    dv_muc = DataValidation(type="list", formula1='"Mức 1,Mức 2,Mức 3,Mức 4"', allow_blank=True)
    ws.add_data_validation(dv_muc)
    for g in khd["dg"]["a"]:
        m = g["diem_max"]
        khung = (f"Mức 1: {cat2(m * .9)}–{cat2(m)} · Mức 2: {cat2(m * .7)}–<{cat2(m * .9)} · "
                 f"Mức 3: {cat2(m * .5)}–<{cat2(m * .7)} · Mức 4: <{cat2(m * .5)}")
        o(ws, r, 1, f"A{g['so']}", dam=True)
        o(ws, r, 2, f"Nhóm {g['so']} — {g['ten']}", dam=True)
        o(ws, r, 3, m, dam=True)
        o(ws, r, 4, None)
        o(ws, r, 5, None, dien=True)
        dv_muc.add(ws.cell(r, 5))
        o(ws, r, 6, khung)
        r += 1
        for dong, ky_hieu, nd, dmax in g["tieu_chi"]:
            o(ws, r, 1, f"A{g['so']}{ky_hieu.rstrip(')')}")
            o(ws, r, 2, nd)
            o(ws, r, 3, dmax)
            x = o(ws, r, 4, None, dien=True)
            dv = DataValidation(type="decimal", operator="between", formula1="0", formula2=str(dmax),
                                allow_blank=True, error=f"Điểm từ 0 đến {dmax:g}", showErrorMessage=True)
            ws.add_data_validation(dv)
            dv.add(x)
            o(ws, r, 5, None)
            o(ws, r, 6, None)
            r += 1
    o(ws, r + 1, 2, "Mức nhóm: để trống thì công cụ tự tính từ tổng điểm nhóm; nếu chọn, tổng điểm nhóm phải nằm đúng "
                    "khung của mức đã chọn (Đ10.5 áp theo NHÓM, không theo từng tiêu chí con).")

    # --- B. KPI
    ws = wb.create_sheet("B-KPI")
    bang(ws, "B. KẾT QUẢ THỰC HIỆN NHIỆM VỤ (70 ĐIỂM) — số liệu thực tế từng chỉ tiêu [QĐ 1923, Đ11]",
         ("Mã", "Trục", "Nội dung công việc (kế hoạch đã duyệt)", "Sản phẩm", "SL kế hoạch", "Hệ số",
          "Thời hạn", "Sản phẩm thực tế", "SL thực tế hoàn thành", "% chất lượng", "% tiến độ",
          "Kết quả nhiệm vụ", "Trọng tâm, then chốt (Đ18)", "Nguồn minh chứng"),
         (7, 6, 48, 18, 9, 7, 12, 28, 11, 10, 10, 20, 14, 28))
    dv_kq = DataValidation(type="list", formula1='"' + ",".join(KET_QUA_VIEC) + '"', allow_blank=True)
    dv_tt = DataValidation(type="list", formula1='"' + ",".join(TRONG_TAM) + '"', allow_blank=True)
    dv_so = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True)
    for d in (dv_kq, dv_tt, dv_so):
        ws.add_data_validation(d)
    r = 5
    for v in khd["viec"]:
        cu = v["cu"]
        for i, x in enumerate((v["ma"], v["truc"], v["noi_dung"], v["san_pham"], v["so_luong"], v["he_so"],
                               v["thoi_han"]), 1):
            o(ws, r, i, x)
        for i, x in ((8, cu.get("K")), (9, cu.get("L")), (10, cu.get("N")), (11, cu.get("P")), (12, None),
                     (13, "Không"), (14, None)):
            o(ws, r, i, x if not str(x or "").startswith("=") else None, dien=True)
        for i in (9, 10, 11):
            dv_so.add(ws.cell(r, i))
        dv_kq.add(ws.cell(r, 12))
        dv_tt.add(ws.cell(r, 13))
        r += 1
    o(ws, r + 1, 3, "SL thực tế: số sản phẩm đã hoàn thành. % chất lượng, % tiến độ: mức độ đáp ứng (0–100; nhập trên "
                    "100 vẫn được ghi nhận nhưng điểm chỉ tiêu chặn trần 100% — Đ11.6). Trọng tâm, then chốt: chọn "
                    "Mức 1/2/3 theo Đ18 thì % hoàn thành của chỉ tiêu phải nằm đúng khung (≥90 · 60–<90 · <60).")

    # --- C. Dieu kien
    ws = wb.create_sheet("C-Dieu-kien")
    bang(ws, "C. TRƯỜNG HỢP ĐẶC THÙ, ĐIỀU KIỆN KÈM THEO MỨC XẾP LOẠI, TỰ ĐỀ XUẤT",
         ("Mã", "Câu hỏi", "Trả lời", "Căn cứ"), (7, 80, 24, 30))
    r = 5
    for ma, ch, lc, _bb, cc in cau_hoi_c(khd):
        o(ws, r, 1, ma)
        o(ws, r, 2, ch)
        x = o(ws, r, 3, None, dien=True)
        if lc:
            d = DataValidation(type="list", formula1='"' + ",".join(lc) + '"', allow_blank=True)
            ws.add_data_validation(d)
            d.add(x)
        else:
            ws.cell(r, 2).value = ch + " — nhập số % (vd 85), hoặc 'Không áp dụng' / 'Chưa có kết quả'"
        o(ws, r, 4, cc)
        r += 1
    wb.save(ra)
    return ra


# ------------------------------------------------------------------ doc bang hoi
def doc_bang_hoi(p):
    wb = km.mo(p)
    tl = {"A": {}, "A_muc": {}, "B": {}, "C": {}}
    ws = wb["A-Tieu-chi-chung"]
    for row in ws.iter_rows(min_row=5):
        ma = str(row[0].value or "").strip()
        if re.fullmatch(r"A[123]", ma):
            tl["A_muc"][ma] = row[4].value
        elif re.fullmatch(r"A[123]\w+", ma):
            tl["A"][ma] = row[3].value
    ws = wb["B-KPI"]
    for row in ws.iter_rows(min_row=5):
        ma = str(row[0].value or "").strip()
        if re.fullmatch(r"B\d+", ma):
            tl["B"][ma] = {"K": row[7].value, "L": row[8].value, "N": row[9].value, "P": row[10].value,
                           "ket_qua": row[11].value, "trong_tam": row[12].value, "minh_chung": row[13].value}
    ws = wb["C-Dieu-kien"]
    for row in ws.iter_rows(min_row=5):
        ma = str(row[0].value or "").strip()
        if re.fullmatch(r"[CD]\d+", ma):
            tl["C"][ma] = row[2].value
    return tl


# ------------------------------------------------------------------ tinh
def tinh(khd, tl):
    """Tra ve ket qua day du; raise Dung neu thieu/sai du lieu can nguoi dung sua."""
    thieu, sai = [], []
    cq = {ma: (ch, lc, cc) for ma, ch, lc, _b, cc in cau_hoi_c(khd)}
    for ma in cq:
        if tl["C"].get(ma) in (None, ""):
            thieu.append(f"C-Dieu-kien {ma}: {cq[ma][0][:70]}")
    # --- Truong hop dac thu -> dung truoc khi cham [D21.6, D21.4]
    dac_thu = [ma for ma in ("C01", "C02", "C03", "C04", "C05") if str(tl["C"].get(ma) or "") == "Có"]
    if dac_thu:
        raise Dung("Thuộc trường hợp đặc thù (" + ", ".join(f"{m}: {cq[m][2]}" for m in dac_thu) + ") — chưa đánh "
                   "giá, xếp loại quý này; kết quả thời gian công tác còn lại xem xét sang quý tiếp theo, không tính "
                   "là dưới mức tối thiểu vì lý do này [QĐ 1923, Đ21.4, Đ21.6]. Không tự chấm.")
    # --- A
    a_nhom = []
    for g in khd["dg"]["a"]:
        diem = []
        for dong, ky_hieu, nd, dmax in g["tieu_chi"]:
            ma = f"A{g['so']}{ky_hieu.rstrip(')')}"
            try:
                x = _so(tl["A"].get(ma), ma)
            except Dung as e:
                sai.append(str(e))
                continue
            if x is None:
                thieu.append(f"A-Tieu-chi-chung {ma}: điểm tự chấm")
                continue
            if x < 0 or x > dmax + EPS:
                sai.append(f"{ma}: {x:g} ngoài khoảng 0–{dmax:g}")
            diem.append((dong, x))
        tong = sum(x for _, x in diem)
        ty_le = tong / g["diem_max"] * 100 if g["diem_max"] else 0
        muc = kc.muc_tieu_chi_chung(round(ty_le, 6))
        chon = str(tl["A_muc"].get(f"A{g['so']}") or "").strip()
        if chon and diem and len(diem) == len(g["tieu_chi"]) and chon != f"Mức {muc}":
            sai.append(f"Nhóm A{g['so']}: tổng {cat2(tong)}/{g['diem_max']:g} điểm ({cat2(ty_le)}%) thuộc Mức {muc}, "
                       f"không khớp '{chon}' đã chọn [Đ10.5]")
        a_nhom.append({"so": g["so"], "diem": diem, "tong": tong, "max": g["diem_max"], "ty_le": ty_le, "muc": muc})
    # --- B
    viec = []
    for v in khd["viec"]:
        t = tl["B"].get(v["ma"])
        if t is None:
            thieu.append(f"B-KPI {v['ma']}: dòng việc không có trong bảng hỏi")
            continue
        try:
            G = _so(v["so_luong"], f"{v['ma']} SL kế hoạch")
            I_ = _so(v["he_so"], f"{v['ma']} hệ số")
            L, N, P = (_so(t[k], f"{v['ma']} {k}") for k in ("L", "N", "P"))
        except Dung as e:
            sai.append(str(e))
            continue
        if G is None or I_ is None:
            sai.append(f"{v['ma']} '{v['noi_dung'][:40]}': kế hoạch thiếu số lượng hoặc hệ số — sửa kế hoạch trước")
            continue
        for k, x in (("SL thực tế", L), ("% chất lượng", N), ("% tiến độ", P)):
            if x is None:
                thieu.append(f"B-KPI {v['ma']} '{v['noi_dung'][:40]}': {k}")
        kq = str(t.get("ket_qua") or "").strip()
        if not kq:
            thieu.append(f"B-KPI {v['ma']} '{v['noi_dung'][:40]}': Kết quả nhiệm vụ")
        elif kq not in KET_QUA_VIEC:
            sai.append(f"{v['ma']}: kết quả '{kq}' không thuộc {KET_QUA_VIEC}")
        if None in (L, N, P):
            continue
        J = G * I_
        M = (min(L, G) * I_) if G else 0.0          # cong thuc mau: =IF(G=0,0,MIN(L,G)*I)
        O = I_ * L * N / 100                          # =I*L*N/100 (mau khong chan)
        Q = I_ * L * P / 100
        tb = (M + O + Q) / 3
        gop = min(tb, J)                               # chan tran tung chi tieu [D11.6]
        ty_le = tb / J * 100 if J else 0.0
        tt = str(t.get("trong_tam") or "Không").strip()
        if tt in ("Mức 1", "Mức 2", "Mức 3"):
            m_ = kc.muc_trong_tam(round(min(ty_le, 100), 6))
            if f"Mức {m_}" != tt:
                sai.append(f"{v['ma']} '{v['noi_dung'][:40]}': % hoàn thành {cat2(min(ty_le, 100))}% thuộc Mức {m_} "
                           f"của Đ18, không khớp '{tt}' — sửa % hoặc mức [QĐ 1923, Đ11.5, Đ18]")
        viec.append(dict(v, L=L, N=N, P=P, K=t.get("K"), minh_chung=t.get("minh_chung"), ket_qua=kq, trong_tam=tt,
                         J=J, tb=tb, gop=gop, ty_le=ty_le))
    if thieu or sai:
        raise Dung("Bảng hỏi chưa đủ hoặc có số sai — không tự chấm:\n  " + "\n  ".join(sai + thieu))
    truc = {}
    for n, b in sorted(khd["dg"]["b"].items()):
        vs = [x for x in viec if x["truc"] == n]
        sj = sum(x["J"] for x in vs)
        pt = sum(x["gop"] for x in vs) / sj * 100 if sj else 0.0
        pt_mau = sum(x["tb"] for x in vs) / sj * 100 if sj else 0.0
        truc[n] = {"so_viec": len(vs), "max": b["diem_max"], "pt": pt, "pt_mau": pt_mau,
                   "diem": pt / 100 * b["diem_max"], "diem_mau": pt_mau / 100 * b["diem_max"]}
    diem_a = sum(g["tong"] for g in a_nhom)
    diem_b = sum(t["diem"] for t in truc.values())
    tong = round(diem_a + diem_b, 6)
    muc_diem = kc.xep_loai_theo_diem(tong)["muc_theo_diem"]
    dk = dieu_kien(khd, tl, viec, muc_diem)
    return {"nhom": khd["nhom"], "a": a_nhom, "diem_a": diem_a, "truc": truc, "diem_b": diem_b, "tong": tong,
            "muc_theo_diem": muc_diem, "viec": viec, "dieu_kien": dk, "tu_de_xuat": tl["C"].get("C15"),
            "canh_bao": canh_bao(khd, tl, viec, truc, muc_diem, dk)}


def dieu_kien(khd, tl, viec, muc_diem):
    """Bang dieu kien kem theo muc theo diem (va cac muc thap hon) — Dat / Khong dat / Thieu du lieu / Khong ap dung.
    KHONG ket luan muc cuoi cung."""
    C = tl["C"]
    n = len(viec)
    khong_ht = sum(1 for x in viec if x["ket_qua"] == "Không hoàn thành")
    cham = sum(1 for x in viec if x["ket_qua"] == "Hoàn thành chậm tiến độ")
    vuot = sum(1 for x in viec if x["ket_qua"] == "Vượt mức")

    def tl_(ma):
        return str(C.get(ma) or "").strip()

    def dat(b):
        return "Đạt" if b else "Không đạt"

    def tu_khai(ma, dat_khi=("Có", "Đạt")):
        v = tl_(ma)
        if v in ("Chưa có kết quả", "Chưa có", ""):
            return "Thiếu dữ liệu — người dùng tự xác nhận"
        if v.startswith("Không áp dụng") or v == "Kỳ trước không có hạn chế":
            return "Không áp dụng"
        return dat(v in dat_khi)

    ql = khd["quan_ly"]
    rows = {m: [] for m in MUC[:3]}
    # 100% nhiem vu
    if ql:
        rows[MUC[0]].append(("Đơn vị, lĩnh vực trực tiếp quản lý hoàn thành 100% nhiệm vụ", tu_khai("C08"), "Đ19.1a"))
        rows[MUC[1]].append(("Đơn vị, lĩnh vực trực tiếp quản lý hoàn thành 100% nhiệm vụ, đúng hạn, bảo đảm chất "
                             "lượng", tu_khai("C08"), "Đ19.1b"))
        rows[MUC[2]].append(("Đơn vị, lĩnh vực trực tiếp quản lý hoàn thành 100% nhiệm vụ", tu_khai("C08"), "Đ19.1c"))
    else:
        rows[MUC[0]].append((f"Hoàn thành 100% nhiệm vụ, đúng hạn ({n - khong_ht - cham}/{n} đúng hạn)",
                             dat(khong_ht == 0 and cham == 0), "Đ19.1a"))
        rows[MUC[1]].append((f"Hoàn thành 100% nhiệm vụ, đúng hạn ({n - khong_ht - cham}/{n})",
                             dat(khong_ht == 0 and cham == 0), "Đ19.1b"))
        rows[MUC[2]].append((f"Hoàn thành 100% nhiệm vụ ({n - khong_ht}/{n})", dat(khong_ht == 0), "Đ19.1c"))
    rows[MUC[0]].append((f"Ít nhất 30% nhiệm vụ vượt mức ({vuot}/{n} = {cat2(vuot / n * 100 if n else 0)}%, theo kết "
                         "quả người dùng khai)", dat(n and vuot / n >= 0.3 - EPS), "Đ19.1a"))
    rows[MUC[0]].append(("Khắc phục 100% hạn chế, khuyết điểm kỳ trước", tu_khai("C07"), "Đ19.1a"))
    rows[MUC[2]].append((f"Nhiệm vụ chậm tiến độ không quá 20% ({cham}/{n})", dat(n and cham / n <= 0.2 + EPS),
                         "Đ19.1c"))
    # Dieu kien khoi II cua mau
    for r, tt, nd, goi_y, gc in khd["dg"]["dieu_kien"]["muc"]:
        k, ma, v = km._kd(nd), f"D{tt}", tl_(f"D{tt}")
        if "bang kiem" in k:
            for m in MUC[:3]:
                rows[m].append(("Bảng kiểm bảo đảm sĩ số HSSV: Đạt", tu_khai(ma, ("Đạt",)), "Đ19.1a–c"))
        elif "gio giang" in k:
            if v in ("", "Chưa có kết quả"):
                s = [("Thiếu dữ liệu — người dùng tự xác nhận",) * 2]
            elif v.startswith("Không áp dụng"):
                s = [("Không áp dụng",) * 2]
            else:
                x = _so(v, ma)
                s = [(dat(x >= 100 - EPS), dat(x >= 50 - EPS))]
            rows[MUC[0]].append(("Tỷ lệ giờ giảng trực tiếp đạt 100% định mức", s[0][0], "Đ19.1a"))
            rows[MUC[1]].append(("Tỷ lệ giờ giảng trực tiếp đạt 100% định mức", s[0][0], "Đ19.1b"))
            rows[MUC[2]].append(("Tỷ lệ giờ giảng trực tiếp đạt ít nhất 50% định mức", s[0][1], "Đ19.1c"))
        else:
            for m in MUC[:2]:
                rows[m].append((nd[:90], tu_khai(ma), "Đ19.1a–b"))
    # Truong hop Khong hoan thanh du du diem [D19.1d]
    kht = []
    if tl_("C06") == "Có":
        kht.append("Bị kết luận suy thoái hoặc kỷ luật từ khiển trách trở lên (C06)")
    if ql and tl_("C09") == "Có":
        kht.append("Đơn vị trực tiếp quản lý hoàn thành dưới 70% nhiệm vụ / >50% lĩnh vực Không hoàn thành (C09)")
    if ql and tl_("C10") == "Có":
        kht.append("Trên 50% phiếu tín nhiệm thấp (C10)")
    if ql and tl_("C11") == "Có":
        kht.append("Đơn vị thuộc thẩm quyền liên quan tham ô, tham nhũng, lãng phí bị xử lý (C11)")
    if not ql and n and khong_ht / n > 0.5:
        kht.append(f"Trên 50% nhiệm vụ không hoàn thành ({khong_ht}/{n})")
    for r, tt, nd, goi_y, gc in khd["dg"]["dieu_kien"]["muc"]:
        if "bang kiem" in km._kd(nd) and tl_(f"D{tt}") == "Không đạt":
            kht.append(f"Bảng kiểm bảo đảm sĩ số HSSV 'Không đạt' (D{tt})")
    tong_hop = {}
    for m in MUC[:3]:
        tt = [s for _, s, _ in rows[m]]
        tong_hop[m] = ("Không đạt" if "Không đạt" in tt else
                       "Thiếu dữ liệu — người dùng tự xác nhận" if any(s.startswith("Thiếu") for s in tt) else "Đạt")
    return {"theo_muc": rows, "tong_hop": tong_hop, "khong_hoan_thanh": kht,
            "tu_diem_tro_xuong": [m for m in MUC[MUC.index(muc_diem):3]] if muc_diem in MUC[:3] else []}


def canh_bao(khd, tl, viec, truc, muc_diem, dk):
    cb = []
    for loi in kc.kiem_tieu_chi_chung([g["diem_max"] for g in khd["dg"]["a"]]):
        cb.append(f"Cấu trúc mẫu sai — {loi[1]} [{loi[2]}] (lỗi của biểu mẫu, không phải của người dùng)")
    for n, t in truc.items():
        if t["pt_mau"] > 100 + EPS:
            cb.append(f"Trục {n}: công thức gốc của mẫu cho {cat2(t['pt_mau'])}% (> 100%); đã chặn trần theo chỉ tiêu "
                      f"còn {cat2(t['pt'])}% [QĐ 1923, Đ11.6; Known-Issues-Bieu-Mau #7]")
        if not t["so_viec"] and t["max"]:
            cb.append(f"Trục {n} không có chỉ tiêu — {t['max']:g} điểm tối đa tính 0")
    for x in viec:
        if x["ty_le"] > 100 + EPS:
            cb.append(f"{x['ma']} '{x['noi_dung'][:40]}': hoàn thành {cat2(x['ty_le'])}% — chỉ tính 100%, phần vượt "
                      "ghi nhận định tính, xét khen thưởng [Đ11.6]")
        if x["ket_qua"] == "Vượt mức" and x["ty_le"] <= 100 + EPS:
            cb.append(f"{x['ma']}: khai 'Vượt mức' nhưng số liệu 3 chiều chỉ {cat2(x['ty_le'])}% — kiểm lại")
    de = str(tl["C"].get("C15") or "")
    if de in MUC and muc_diem in MUC and MUC.index(de) < MUC.index(muc_diem):
        cb.append(f"Tự đề xuất '{de}' CAO HƠN mức theo ngưỡng điểm '{muc_diem}'")
    if de in MUC[:3] and dk["tong_hop"].get(de) == "Không đạt":
        cb.append(f"Tự đề xuất '{de}' nhưng điều kiện kèm theo mức này có mục 'Không đạt'")
    if dk["khong_hoan_thanh"]:
        cb.append("Thuộc trường hợp 'Không hoàn thành nhiệm vụ' dù đủ điểm [Đ19.1d]: " + "; ".join(dk["khong_hoan_thanh"]))
    if khd["quan_ly"] and str(tl["C"].get("C12")) == "Có":
        tt = str(tl["C"].get("C13") or "")
        if tt in MUC and muc_diem in MUC and MUC.index(muc_diem) < MUC.index(tt):
            cb.append(f"Người đứng đầu: mức theo điểm '{muc_diem}' cao hơn xếp loại tập thể '{tt}' — không được cao hơn "
                      "[QĐ 1923, Đ14.4, Đ19.4]")
        elif tt == "Chưa có":
            cb.append("Người đứng đầu: chưa có xếp loại tập thể kỳ này — chưa đối chiếu quy tắc 'không cao hơn tập thể' "
                      "[Đ14.4, Đ19.4]")
    if str(tl["C"].get("C14")) == "Có":
        cb.append("Đã có quý dưới mức tối thiểu trong năm: viên chức quản lý không xếp HTXS cả năm [Đ19.5]; người không "
                  "giữ chức vụ — Đ19.1a (lưu ý) ghi cho mọi cá nhân, Đ19.5 ghi 'khuyến khích, không bắt buộc' — Câu hỏi "
                  "mở số 8, không tự chọn")
    return cb


# ------------------------------------------------------------------ xuat Excel
def ghi_ket_qua(khd, tl, kq, ra, quy=None, nam=None):
    from copy import copy
    if os.path.abspath(ra) == os.path.abspath(khd["tep"]):
        raise Dung("Không ghi đè tệp kế hoạch đã duyệt — chọn tên tệp ra khác")
    if os.path.abspath(os.path.dirname(ra)) == km.thu_muc_mau():
        raise Dung("Không ghi vào thư mục mẫu assets/")
    os.makedirs(os.path.dirname(os.path.abspath(ra)), exist_ok=True)
    shutil.copyfile(khd["tep"], ra)
    wb = km.mo(ra)
    ct, dg_ct = khd["ct"], khd["dg"]
    kp, dg = wb["KPI"], wb[dg_ct["sheet"]]
    # KPI: so thuc te tung viec; dong khong co viec -> xoa o nhap (so vi du cua mau)
    co = {x["dong_kpi"]: x for x in kq["viec"]}
    for r_kh, rk in ct["kpi_dong"].items():
        if rk in co:
            x = co[rk]
            kp[f"K{rk}"].value = x.get("K") or kp[f"K{rk}"].value
            kp[f"L{rk}"].value, kp[f"N{rk}"].value, kp[f"P{rk}"].value = x["L"], x["N"], x["P"]
            if ct["cot_minh_chung"] and x.get("minh_chung"):
                kp[f"{ct['cot_minh_chung']}{rk}"].value = x["minh_chung"]
        else:
            km.xoa_thuc_te(kp, rk)
    # Chan tran tung chi tieu trong cong thuc % Truc (cot R dong Truc) [D11.6] — thay =(M+O+Q)/3
    for n, (d, c) in ct["truc"].items():
        rt = ct["kpi_truc"][n]
        a, b = ct["kpi_dong"][d], ct["kpi_dong"][c]
        tb = f"(M{a}:M{b}+O{a}:O{b}+Q{a}:Q{b})/3"
        kp[f"R{rt}"].value = f"=SUMPRODUCT({tb}-({tb}>J{a}:J{b})*({tb}-J{a}:J{b}))"
    # Danh gia: thong tin ca nhan, ky, muc A, dieu kien, muc III
    for nhan, r in dg_ct["ca_nhan"].items():
        if khd["ca_nhan"].get(nhan):
            dg.cell(r, 1).value = f"{nhan}: {khd['ca_nhan'][nhan]}"
    if quy and nam:
        for r in range(1, 12):
            for c_ in dg[r]:
                if isinstance(c_.value, str):
                    c_.value = re.sub(r"(QUÝ|Quý)\s*[….]+\s*(NĂM|năm)", lambda m: f"{m.group(1)} {quy} {m.group(2)}",
                                      c_.value)
    for g in kq["a"]:
        cot = next(x["cot_diem"] for x in dg_ct["a"] if x["so"] == g["so"])
        for dong, x in g["diem"]:
            dg[f"{cot}{dong}"].value = x
    ck = dg_ct["dieu_kien"]["cot_kq"]
    for r, tt, nd, goi_y, gc in dg_ct["dieu_kien"]["muc"]:
        v = tl["C"].get(f"D{tt}")
        if v not in (None, ""):
            dg[f"{ck}{r}"].value = (f"{v}%" if isinstance(v, (int, float)) else v)
    r3 = dg_ct["de_xuat"]
    dg.cell(r3, 1).value = f"III. Tự đề xuất mức xếp loại chất lượng: {kq['tu_de_xuat']}"
    # Ghi chu chan tran ngay duoi tong diem
    cot_dat = dg_ct["b"][1]["cot_dat"]
    col_gc = chr(ord(cot_dat) + 1)
    dg[f"{col_gc}{dg_ct['tong']}"].value = ("Điểm KPI Trục chặn trần 100% theo từng chỉ tiêu [QĐ 1923, Đ11.6] — "
                                           "sheet KPI cột R dòng Trục")
    # The thuc: Times New Roman
    for sh in wb.worksheets:
        for row in sh.iter_rows():
            for cell in row:
                if cell.value is not None and cell.font is not None and cell.font.name != km.PHONG:
                    f = copy(cell.font)
                    f.name = km.PHONG
                    cell.font = f
    # Do lai chieu cao dong SAU khi ghi so thuc te: san pham thuc te (K — danh sach so ky hieu), minh chung (S) lam dong
    # cao hon luc lap ke hoach (lenh sua 25/9/2026, L1). Vuot 409 pt -> canh bao KH19.
    kq["canh_bao"] += km.chinh_chieu_cao(wb, ct)
    wb.save(ra)
    return ra


# ------------------------------------------------------------------ in
def in_ket_qua(khd, kq):
    L = []
    L.append(f"Nhóm vị trí: {km.NHOM[khd['nhom']][0]}")
    L.append("")
    L.append("| Khối | Điểm tối đa | Điểm tự đánh giá |")
    L.append("|---|---|---|")
    for g in kq["a"]:
        L.append(f"| A{g['so']} (Mức {g['muc']} — {cat2(g['ty_le'])}%) | {g['max']:g} | {cat2(g['tong'])} |")
    for n, t in kq["truc"].items():
        L.append(f"| Trục ({n}) — {t['so_viec']} chỉ tiêu, {cat2(t['pt'])}% | {t['max']:g} | {cat2(t['diem'])} |")
    L.append(f"| **Tổng A + B** | 100 | **{cat2(kq['tong'])}** |")
    L.append("")
    L.append(f"Mức theo ngưỡng điểm thuần túy [Đ19.1]: **{kq['muc_theo_diem']}**")
    L.append(f"Cá nhân tự đề xuất: **{kq['tu_de_xuat']}**")
    L.append("")
    L.append("| Mức | Điều kiện | Kết quả | Căn cứ |")
    L.append("|---|---|---|---|")
    for m in kq["dieu_kien"]["tu_diem_tro_xuong"]:
        for nd, s, cc in kq["dieu_kien"]["theo_muc"][m]:
            L.append(f"| {m} | {nd} | {s} | QĐ 1923, {cc} |")
    for m in kq["dieu_kien"]["tu_diem_tro_xuong"]:
        L.append(f"- Điều kiện kèm theo '{m}': {kq['dieu_kien']['tong_hop'][m]}")
    if kq["canh_bao"]:
        L.append("")
        L.append("Cảnh báo:")
        L += [f"- {x}" for x in kq["canh_bao"]]
    L.append("")
    L.append("Nguồn chưa có trong kho — điều kiện liên quan do người dùng tự xác nhận: Bảng kiểm bảo đảm sĩ số HSSV; "
             "Hướng dẫn đánh giá hằng quý/năm của Hiệu trưởng [Đ10.5, Đ24.2] (đang dùng khung mức của Quy chế); Tiêu "
             "chí đánh giá chuyển đổi số.")
    if khd["nhom"] in NHOM_THIEU_PL:
        L.append(f"Đối chiếu qua mẫu Kế hoạch+KPI Quý III/2026, chưa đối chiếu trực tiếp QĐ 2078 (Phụ lục "
                 f"{NHOM_THIEU_PL[khd['nhom']]} chưa có trong kho).")
    L.append("Trần tỷ lệ HTXS tính ở cấp đơn vị/Trường — giai đoạn 3, chưa áp dụng ở đây [Đ19.2].")
    L.append("")
    L.append(f"*{DONG_CUOI}*")
    return "\n".join(L)


def main(argv):
    import argparse
    import json
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="lenh", required=True)
    s1 = sp.add_parser("sinh-bang-hoi")
    s2 = sp.add_parser("danh-gia")
    for s in (s1, s2):
        s.add_argument("--ke-hoach", required=True)
        s.add_argument("--nhom", choices=list(km.NHOM))
        s.add_argument("--quy")
        s.add_argument("--nam")
        s.add_argument("--ra", required=True)
    s2.add_argument("--bang-hoi", required=True)
    s2.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        khd = doc_ke_hoach(a.ke_hoach, a.nhom)
        if a.lenh == "sinh-bang-hoi":
            sinh_bang_hoi(khd, a.ra, a.quy, a.nam)
            print(f"✓ Đã sinh bảng hỏi {a.ra} — {len(khd['viec'])} chỉ tiêu, "
                  f"{sum(len(g['tieu_chi']) for g in khd['dg']['a'])} tiêu chí chung, {len(cau_hoi_c(khd))} câu mục C."
                  " Người dùng điền ô vàng rồi chạy 'danh-gia'.")
            return 0
        kq = tinh(khd, doc_bang_hoi(a.bang_hoi))
        ghi_ket_qua(khd, doc_bang_hoi(a.bang_hoi), kq, a.ra, a.quy, a.nam)
    except PermissionError:
        print(f"✗ Không ghi được {a.ra}: tệp đang mở trong Excel (hoặc bị khóa) — hãy đóng tệp hoặc đặt tên mới.")
        return 2
    except (km.LoiCauTruc, Dung, kc.LoiKPI) as e:
        print(f"✗ {e}")
        return 2
    if a.json:
        print(json.dumps({k: v for k, v in kq.items() if k != "viec"}, ensure_ascii=False, indent=1, default=str))
    print(f"✓ Đã xuất {a.ra}")
    print(in_ket_qua(khd, kq))
    return 1 if kq["canh_bao"] or any(v == "Không đạt" for v in kq["dieu_kien"]["tong_hop"].values()) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/kpi_mau.py` (26541 byte, sha256 `faabd3618bdc70a399475ba2405b0cc0ea8b94ae0814ed07c33950a34b130db4`)

`````python
# -*- coding: utf-8 -*-
"""Cau truc 6 mau Ke hoach + KPI Quy (03-Templates/03-12) va dien ke hoach vao BAN SAO cua mau.

Mau (6 nhom vi tri, CV 694/CĐKT-TCCB muc I.2; QD 1923 D15.1b):
  truong-pho-don-vi   Truong/Pho phong, khoa                     (vien chuc quan ly)
  bo-mon              Truong/Pho bo mon, Phong Kham da khoa      (vien chuc quan ly)
  nha-giao            Nhom 1 — Nha giao truc tiep giang day cac Khoa
  giao-vu             Nhom 2 — Giao vu khoa
  hanh-chinh          Nhom 3 — Vien chuc, NLD lam viec theo che do hanh chinh
  ho-tro              Nhom 4 — Nhan vien ho tro, phuc vu

Moi mau: sheet "Ke Hoach" (6 Truc x 20 dong, noi cong thuc sang sheet "KPI"), "KPI" (so luong quy doi, KPI 3 chieu),
"Danh gia"/"Danh Gia" (diem toi da tung Truc, nhom tieu chi chung). Cau truc DOC TU MAU, khong ghi cung dong.

KHONG ghi de mau: luon chep sang tep ra roi moi dien. Tep ra chuan hoa phong chu ve Times New Roman (mau goc co o
Calibri — the thuc Muc 2, skill the-thuc); co, dam, can le giu nguyen.
"""
import glob
import os
import re
import shutil
import unicodedata
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
DU_AN = os.path.dirname(HERE)

NHOM = {
    "truong-pho-don-vi": ("Trưởng/Phó phòng, khoa", "Truong-Pho-Truong-Cac-Don-Vi", True),
    "bo-mon": ("Trưởng/Phó bộ môn, Phòng Khám đa khoa", "VCQL-Bo-Mon-Va-Tuong-Duong", True),
    "nha-giao": ("Nhóm 1 — Nhà giáo trực tiếp giảng dạy", "Nha-Giao-Giang-Day-Cac-Khoa", False),
    "giao-vu": ("Nhóm 2 — Giáo vụ khoa", "Giao-Vu-Khoa", False),
    "hanh-chinh": ("Nhóm 3 — Viên chức hành chính", "VC-Hanh-Chinh", False),
    "ho-tro": ("Nhóm 4 — Nhân viên hỗ trợ, phục vụ", "NV-Ho-Tro-Phuc-Vu", False),
}
LA_MA = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6}
PHONG = "Times New Roman"


def _kd(s):
    t = unicodedata.normalize("NFD", str(s or "").lower())
    return " ".join("".join(c for c in t if unicodedata.category(c) != "Mn").replace("đ", "d").split())


def thu_muc_mau():
    """assets/ cua skill (khi chay trong goi) hoac 28-KTC-KPI/assets (du an)."""
    for d in (os.path.join(HERE, "..", "assets"), os.path.join(DU_AN, "28-KTC-KPI", "assets"),
              os.path.join(HERE, "..", "skills", "kpi-lap-ke-hoach", "assets")):   # ban chep o scripts/ goc plugin
        if glob.glob(os.path.join(d, "Mau-KeHoach-DanhGia_*.xlsx")):
            return os.path.abspath(d)
    raise FileNotFoundError("Không thấy 6 mẫu Kế hoạch trong assets/ — dừng, hỏi người dùng.")


def tep_mau(nhom):
    if nhom not in NHOM:
        raise ValueError(f"Nhóm vị trí '{nhom}' không có; chọn một trong: {', '.join(NHOM)}")
    ds = glob.glob(os.path.join(thu_muc_mau(), f"Mau-KeHoach-DanhGia_{NHOM[nhom][1]}_*.xlsx"))
    if len(ds) != 1:
        raise FileNotFoundError(f"Không xác định được đúng 1 mẫu cho nhóm '{nhom}' ({len(ds)} tệp).")
    return ds[0]


def nhan_nhom(wb):
    """Doan nhom tu tieu de sheet Danh gia (vd 'DOI VOI VIEN CHUC HANH CHINH'). Khong chac -> None."""
    ws = sheet_danh_gia(wb)
    t = _kd(" ".join(str(ws.cell(r, 1).value or "") for r in range(1, 6)))
    for k, dau in (("giao-vu", "giao vu"), ("ho-tro", "ho tro"), ("nha-giao", "nha giao"),
                   ("hanh-chinh", "hanh chinh"), ("bo-mon", "bo mon"),
                   ("truong-pho-don-vi", "truong/pho cac don vi")):   # tieu de mau: "TRUONG/PHO CAC DON VI"
        if dau in t:
            return k
    return None


def sheet_danh_gia(wb):
    return next(w for w in wb.worksheets if _kd(w.title).startswith("danh gia"))


def cau_truc(wb):
    """{'truc': {1: (dong_dau, dong_cuoi)} tren 'Ke Hoach', 'diem_truc': {1: 45,...}, 'nhom_a': [13,12,5],
        'kpi_dong': {dong Ke Hoach: dong KPI}, 'cot_minh_chung': 'S' | None}"""
    kh, kp, dg = wb["Ke Hoach"], wb["KPI"], sheet_danh_gia(wb)
    kpi_dong, dau_truc = {}, []
    for r in kp.iter_rows(min_row=7):
        a = str(r[0].value or "").strip()
        if a in LA_MA:
            dau_truc.append((r[0].row, LA_MA[a]))
        m = re.match(r"='Ke Hoach'!B(\d+)$", str(r[1].value or ""))
        if m:
            kpi_dong[int(m.group(1))] = r[0].row
    truc = {}
    for i, (d, n) in enumerate(dau_truc):
        het = dau_truc[i + 1][0] if i + 1 < len(dau_truc) else 10 ** 6
        ks = [k for k, v in kpi_dong.items() if d < v < het]
        if ks:
            truc[n] = (min(ks), max(ks))
    diem_truc, nhom_a = {}, []
    for r in dg.iter_rows():
        b = str(r[1].value or "")
        m = re.match(r"Trục \((\d)\)", b)
        if m and len(r) > 5 and isinstance(r[5].value, (int, float)):
            diem_truc[int(m.group(1))] = float(r[5].value)
        if str(r[0].value or "").strip() in ("1", "2", "3") and str(r[3].value or "").startswith("=SUM(D"):
            a_, b_ = map(int, re.findall(r"D(\d+):D(\d+)", r[3].value)[0])
            nhom_a.append(sum(float(dg.cell(i, 4).value or 0) for i in range(a_, b_ + 1)))
    cot_mc = None
    for c in kp[3]:
        if "minh chứng" in str(c.value or "").lower():
            cot_mc = c.column_letter
    # Cot "Nhiem vu de ra ke hoach" cua sheet KPI (dong tieu de 4) — do theo TIEU DE, mau nao thieu cot thi bo qua
    kpi_cot = {}
    for c in kp[4]:
        t = _kd(c.value)
        for k, dau in (("chi_dao", "nguoi truc tiep chi dao"), ("phoi_hop", "nguoi phoi hop"),
                       ("tham_muu", "don vi tham muu"), ("san_pham", "san pham du kien")):
            if t.startswith(dau):
                kpi_cot[k] = c.column_letter
    return {"truc": truc, "diem_truc": diem_truc, "nhom_a": nhom_a, "kpi_dong": kpi_dong, "cot_minh_chung": cot_mc,
            "kpi_truc": {n: d for d, n in dau_truc}, "kpi_cot": kpi_cot}


class LoiCauTruc(ValueError):
    """Sheet Danh gia khong do duoc cau truc — DUNG, bao nguoi dung; khong doan (lenh 25/9/2026 muc 12)."""


def cau_truc_danh_gia(wb):
    """Do DONG sheet Danh gia/Danh Gia (6 mau lech so dong va cot — khong ghi cung theo mau nao).
    Tra ve {'sheet', 'a': [{'so','dong','cot_max','cot_diem','tieu_chi':[(dong, ky_hieu, noi_dung, diem_max)]}],
    'tong_a': dong, 'b': {truc: {'dong','cot_pt','cot_max','cot_dat','diem_max','cong_thuc'}}, 'tong_b', 'tong',
    'dieu_kien': {'dong', 'cot_kq', 'cot_ghi_chu', 'muc': [(dong, tt, noi_dung, goi_y, ghi_chu)]},
    'de_xuat': dong muc III, 'ca_nhan': {nhan: dong}}. Thieu khoi nao -> LoiCauTruc."""
    from openpyxl.utils import get_column_letter
    dg = sheet_danh_gia(wb)
    o = lambda r, c: dg.cell(r, c).value  # noqa: E731
    kq = {"sheet": dg.title, "a": [], "b": {}, "ca_nhan": {}}
    # --- Muc A: hang tieu de "TT | TIEU CHI DANH GIA | ... Diem toi da | Diem cham"; nhom = dong cot A la 1/2/3
    #     co o "Diem toi da" = SUM(<cot>a:<cot>b) (cac tieu chi con a, b, c...)
    hang_a = next((r for r in range(1, dg.max_row + 1) if str(o(r, 1) or "").strip() == "TT"
                   and _kd(o(r, 2)).startswith("tieu chi danh gia")), None)
    if hang_a:
        tde = {_kd(o(hang_a, c)): get_column_letter(c) for c in range(1, dg.max_column + 1) if o(hang_a, c)}
        cmax = next((v for k, v in tde.items() if k.startswith("diem toi da")), None)
        cdiem = next((v for k, v in tde.items() if k.startswith("diem cham")), None)
        for r in range(hang_a + 1, dg.max_row + 1):
            a = str(o(r, 1) or "").strip()
            m = re.match(r"=SUM\(([A-Z]+)(\d+):\1(\d+)\)$", str(dg[f"{cmax}{r}"].value or "")) if cmax else None
            if a == str(len(kq["a"]) + 1) and m and m.group(1) == cmax and len(kq["a"]) < 3:
                tu, den = int(m.group(2)), int(m.group(3))
                tc = [(i, str(o(i, 1) or "").strip(), str(o(i, 2) or "").strip(),
                       float(dg[f"{cmax}{i}"].value or 0)) for i in range(tu, den + 1)]
                kq["a"].append({"so": int(a), "dong": r, "ten": str(o(r, 2) or "").strip(), "cot_max": cmax,
                                "cot_diem": cdiem, "tieu_chi": tc,
                                "diem_max": sum(x[3] for x in tc)})
    # --- Muc B: dong cot B bat dau "Truc (n)" co diem toi da so (cot co tieu de "Điểm tối đa")
    hang_b = None
    for r in range(1, dg.max_row + 1):
        if str(o(r, 1) or "").strip() == "TT" and "Tiêu chí/Nội dung" in str(o(r, 2) or ""):
            hang_b = r
    if hang_b:
        tieu_de = {_kd(o(hang_b, c)): get_column_letter(c) for c in range(1, dg.max_column + 1) if o(hang_b, c)}
        cot_pt = next((v for k, v in tieu_de.items() if k.startswith("diem kpi")), None)
        cot_max = next((v for k, v in tieu_de.items() if k.startswith("diem toi da")), None)
        cot_dat = next((v for k, v in tieu_de.items() if k.startswith("diem dat")), None)
        for r in range(hang_b + 1, dg.max_row + 1):
            m = re.match(r"Trục \((\d)\)", str(o(r, 2) or ""))
            if m and cot_max and isinstance(dg[f"{cot_max}{r}"].value, (int, float, str)):
                try:
                    dmax = float(dg[f"{cot_max}{r}"].value)
                except (TypeError, ValueError):
                    continue
                kq["b"][int(m.group(1))] = {"dong": r, "cot_pt": cot_pt, "cot_max": cot_max, "cot_dat": cot_dat,
                                            "diem_max": dmax, "cong_thuc": dg[f"{cot_pt}{r}"].value}
    # --- Dong tong, dieu kien (II), de xuat (III), thong tin ca nhan
    for r in range(1, dg.max_row + 1):
        a, b = str(o(r, 1) or "").strip(), _kd(o(r, 2))
        if b == "tong diem a + b":
            kq["tong"] = r
        elif b == "tong diem nhom b":
            kq["tong_b"] = r
        elif b in ("tong diem", "tong diem nhom a") and "tong_a" not in kq:
            kq["tong_a"] = r
        elif a == "II." and "dieu kien bat buoc" in b:
            kq["dieu_kien"] = {"dong": r, "muc": []}
        elif a.startswith("III.") and "tu de xuat" in _kd(a):
            kq["de_xuat"] = r
        for nhan in ("Họ và tên", "Chức vụ Đảng", "Chức vụ chính quyền", "Chức vụ đoàn thể", "Đơn vị công tác"):
            if a.startswith(nhan) and nhan not in kq["ca_nhan"]:
                kq["ca_nhan"][nhan] = r
    dk = kq.get("dieu_kien")
    if dk:
        tde = dk["dong"] + 1
        hdr = {_kd(o(tde, c)): get_column_letter(c) for c in range(1, dg.max_column + 1) if o(tde, c)}
        dk["cot_kq"] = next((v for k, v in hdr.items() if k.startswith("ket qua")), None)
        dk["cot_ghi_chu"] = next((v for k, v in hdr.items() if k.startswith("ghi chu")), None)
        het = kq.get("de_xuat", dg.max_row + 1)
        for r in range(tde + 1, het):
            tt = str(o(r, 1) or "").strip()
            if re.fullmatch(r"\d+", tt) and o(r, 2):
                goi_y = dg[f"{dk['cot_kq']}{r}"].value if dk["cot_kq"] else None
                gc = dg[f"{dk['cot_ghi_chu']}{r}"].value if dk["cot_ghi_chu"] else None
                dk["muc"].append((r, tt, str(o(r, 2)).strip(), goi_y, gc))
    thieu = [t for t, ok in (("mục A (3 nhóm tiêu chí chung)", len(kq["a"]) == 3),
                             ("mục B (6 Trục có điểm tối đa)", sorted(kq["b"]) == [1, 2, 3, 4, 5, 6]),
                             ("cột Điểm KPI (%) / Điểm tối đa / Điểm đạt", hang_b and all(
                                 kq["b"].get(1, {}).get(k) for k in ("cot_pt", "cot_max", "cot_dat"))),
                             ("dòng Tổng điểm A + B", "tong" in kq),
                             ("khối II. Điều kiện bắt buộc", dk and dk.get("cot_kq") and dk["muc"]),
                             ("dòng III. Tự đề xuất mức xếp loại", "de_xuat" in kq)) if not ok]
    if thieu:
        raise LoiCauTruc(f"Sheet '{dg.title}': không dò được " + "; ".join(thieu) +
                         " — dừng, báo người dùng; không đoán cấu trúc.")
    return kq


def mo(p):
    from openpyxl import load_workbook
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return load_workbook(p)


def dong_vi_du(nhom):
    """{(sheet, o): gia tri} cua cac o du lieu CO SAN trong mau o vung dau viec — dong vi du chua xoa (known issue 4)."""
    wb = mo(tep_mau(nhom))
    ct = cau_truc(wb)
    kh = wb["Ke Hoach"]
    vd = {}
    for d, c in ct["truc"].values():
        for r in range(d, c + 1):
            for col in "BCDEFGHIJ":
                v = kh[f"{col}{r}"].value
                if v not in (None, ""):
                    vd[f"{col}{r}"] = v
    return vd


O_THUC_TE = ("K", "L", "N", "P")   # sheet KPI: san pham thuc te, SL thuc te, % chat luong, % tien do (o nhap)


def xoa_thuc_te(kp, r):
    """Xoa o NHAP so thuc te cua mot dong viec tren sheet KPI; giu nguyen o cong thuc."""
    for col in O_THUC_TE:
        v = kp[f"{col}{r}"].value
        if v is not None and not str(v).startswith("="):
            kp[f"{col}{r}"].value = None


CAO_TOI_DA = 409          # pt — gioi han chieu cao dong cua Excel
RONG_GHI_CHU_KH = 25      # cot J (Ghi chu) sheet Ke Hoach: mau ~6,6 ky tu -> ghi chu dai lam dong cao bat thuong


def do_rong_cot(ws):
    """{chi so cot: do rong}. openpyxl GOP cot lien nhau cung do rong vao MOT khoa (min–max, vd 'C' = C..F) — tra khoa
    don le se cho cot giua nhom la None (lenh sua 25/9/2026, L1). Cot khong khai bao -> do rong mac dinh cua sheet."""
    kq = {"_mac_dinh": ws.sheet_format.defaultColWidth or 8.43}
    for d in ws.column_dimensions.values():
        if d.min and d.max and d.width:
            for i in range(d.min, d.max + 1):
                kq[i] = float(d.width)
    return kq


def gia_tri_hien_thi(wb, cell, sau=0):
    """Van ban o se HIEN THI: cong thuc tro cheo sheet ='Ten sheet'!B14 -> gia tri o duoc tro (cot B sheet KPI la cong
    thuc — ban cu bo qua nen dong KPI khong bao gio duoc nang cao). Cong thuc tinh toan khac -> None."""
    v = cell.value
    if v is None or not str(v).startswith("="):
        return v
    m = re.fullmatch(r"='?([^'!]+)'?!\$?([A-Z]+)\$?(\d+)", str(v).strip())
    if m and sau < 3 and m.group(1) in wb.sheetnames:
        return gia_tri_hien_thi(wb, wb[m.group(1)][f"{m.group(2)}{m.group(3)}"], sau + 1)
    return None


def _vung_gop(ws):
    """{o dau vung gop 1 dong: [chi so cot]}; '_bi_gop': cac o bi che trong vung gop (bo qua khi do)."""
    kq, bi = {}, set()
    for g in ws.merged_cells.ranges:
        if g.min_row == g.max_row:
            kq[g.start_cell.coordinate] = list(range(g.min_col, g.max_col + 1))
        for rr in range(g.min_row, g.max_row + 1):
            for cc in range(g.min_col, g.max_col + 1):
                if (rr, cc) != (g.min_row, g.min_col):
                    bi.add(ws.cell(rr, cc).coordinate)
    kq["_bi_gop"] = bi
    return kq


def uoc_chieu_cao(wb, ws, r, rong=None, gop=None):
    """(chieu cao can pt, so dong chu) cua dong r — CUC DAI moi o co chu trong dong. So ky tu moi dong = do rong cot
    (o gop: cong do rong cac cot); chu tieng Viet co dau xuong dong som -> so ky tu x 1,2; cao = dong x co x 1,3 + 6."""
    import math
    rong = rong or do_rong_cot(ws)
    gop = gop if gop is not None else _vung_gop(ws)
    can, dong_max = 0.0, 1
    for c in ws[r]:
        if c.coordinate in gop["_bi_gop"]:
            continue
        v = gia_tri_hien_thi(wb, c)
        if v in (None, "") or isinstance(v, (int, float)):
            continue
        w = sum(rong.get(i, rong["_mac_dinh"]) for i in gop.get(c.coordinate, [c.column]))
        co = float(c.font.sz or 12) if c.font else 12.0
        dong = sum(max(1, math.ceil(len(p) * 1.2 / max(1.0, w))) for p in str(v).split("\n"))
        h = dong * co * 1.3 + 6
        if h > can:
            can, dong_max = h, dong
    return can, dong_max


def canh_chu(c):
    from copy import copy
    al = copy(c.alignment)
    al.wrap_text = True
    al.vertical = "top"
    c.alignment = al


def chinh_chieu_cao(wb, ct):
    """Goi SAU KHI da ghi het du lieu (ke hoach, hoac so thuc te o buoc tu danh gia). Chi dong viec dang hien cua ca
    'Ke Hoach' lan 'KPI'. Vuot 409 pt -> dat 409 va tra canh bao KH19 (khong cat im lang). Tra ve danh sach canh bao."""
    cb = []
    kh, kp = wb["Ke Hoach"], wb["KPI"]
    rk_, rp_ = do_rong_cot(kh), do_rong_cot(kp)
    gk, gp = _vung_gop(kh), _vung_gop(kp)
    for n, (d, c) in ct["truc"].items():
        for r in range(d, c + 1):
            if kh[f"B{r}"].value in (None, "") or kh.row_dimensions[r].hidden:
                continue
            for sh, rr, rong, gop in ((kh, r, rk_, gk), (kp, ct["kpi_dong"][r], rp_, gp)):
                can, dong = uoc_chieu_cao(wb, sh, rr, rong, gop)
                if can > CAO_TOI_DA:
                    cb.append(f"KH19 {sh.title}!dòng {rr} (Trục {n}): cần ~{dong} dòng chữ ({can:.0f} pt) > "
                              f"{CAO_TOI_DA} pt — Excel không hiện hết; rút gọn nội dung hoặc nới rộng cột")
                    can = CAO_TOI_DA
                sh.row_dimensions[rr].height = round(max(can, 15.0), 1)
    return cb


def thuc_te_vi_du(nhom):
    """{'dong N': {o: gia tri}} — so thuc te VI DU co san trong mau o sheet KPI (Known-Issues-Bieu-Mau #12)."""
    wb = mo(tep_mau(nhom))
    ct = cau_truc(wb)
    kp = wb["KPI"]
    kq = {}
    for r in ct["kpi_dong"].values():
        o = {f"{col}{r}": kp[f"{col}{r}"].value for col in O_THUC_TE
             if kp[f"{col}{r}"].value not in (None, "") and not str(kp[f"{col}{r}"].value).startswith("=")}
        if o:
            kq[f"dòng {r}"] = o
    return kq


def ghi_ke_hoach(nhom, kh, ra, quy=None, nam=None):
    """Dien ke hoach vao BAN SAO mau. kh: {"ca_nhan":{ho_ten,ngay_sinh,chuc_vu_dang,chuc_vu_chinh_quyen,
    chuc_vu_doan_the,don_vi}, "dau_viec":[{truc,noi_dung,cap_trinh,muc_do,san_pham,so_luong,thoi_han,he_so,
    minh_chung,ghi_chu, nguoi_chi_dao?, nguoi_phoi_hop?, don_vi_tham_muu?}], "phuong_an":..., "trang_thai_he_so":...}
    (he_so da tinh bang kpi_calc). Sheet KPI cot C–F: nguoi_chi_dao (mac dinh cap_trinh), nguoi_phoi_hop (khong mac
    dinh — trong thi KH17), don_vi_tham_muu (mac dinh ca_nhan.don_vi), san_pham = cong thuc ='Ke Hoach'!E<dong>.
    Tra ve danh sach thong bao."""
    goc = tep_mau(nhom)
    if os.path.abspath(ra) == os.path.abspath(goc) or os.path.abspath(os.path.dirname(ra)) == thu_muc_mau():
        raise ValueError("Không ghi vào thư mục mẫu assets/ — chọn nơi lưu khác.")
    os.makedirs(os.path.dirname(os.path.abspath(ra)), exist_ok=True)
    shutil.copyfile(goc, ra)
    wb = mo(ra)
    ct = cau_truc(wb)
    ws, kp = wb["Ke Hoach"], wb["KPI"]
    tb = []
    # 1. Xoa dong vi du trong vung dau viec (giu cot A = STT). Sheet KPI cung co SO THUC TE vi du o dong viec dau
    #    (L=4, N=100, P=100 — Known-Issues-Bieu-Mau #12): xoa o nhap lieu, giu cong thuc.
    for d, c in ct["truc"].values():
        for r in range(d, c + 1):
            for col in "BCDEFGHIJ":
                ws[f"{col}{r}"].value = None
            xoa_thuc_te(kp, ct["kpi_dong"][r])
            if ct["cot_minh_chung"]:
                kp[f"{ct['cot_minh_chung']}{ct['kpi_dong'][r]}"].value = None
    # 2. Thong tin ca nhan
    cn = kh.get("ca_nhan", {})
    nhan = {4: ("Họ và tên", "ho_ten", "Ngày sinh", "ngay_sinh"), 5: ("Chức vụ Đảng", "chuc_vu_dang"),
            6: ("Chức vụ chính quyền", "chuc_vu_chinh_quyen"), 7: ("Chức vụ đoàn thể", "chuc_vu_doan_the"),
            8: ("Đơn vị công tác", "don_vi")}
    for r, t in nhan.items():
        if len(t) == 4:
            ws[f"B{r}"].value = f"{t[0]}: {cn.get(t[1]) or '…'}    {t[2]}: {cn.get(t[3]) or '…'}"
        else:
            ws[f"B{r}"].value = f"{t[0]}: {cn.get(t[1]) or '…'}"
    # 3. Ky (quy, nam) trong tieu de
    if quy and nam:
        for sh in (ws, kp):
            for r in range(1, 4):
                for c in sh[r]:
                    if isinstance(c.value, str):
                        c.value = re.sub(r"QUÝ\s+[IVX]+\s+NĂM\s+\d{4}", f"QUÝ {quy} NĂM {nam}", c.value)
    # 4. Dau viec
    dem = {n: 0 for n in ct["truc"]}
    pa = kh.get("phuong_an")
    for dv in kh.get("dau_viec", []):
        n = int(dv["truc"])
        if n not in ct["truc"]:
            raise ValueError(f"Trục {n} không có trong mẫu.")
        d, c = ct["truc"][n]
        r = d + dem[n]
        if r > c:
            raise ValueError(f"Trục {n} vượt {c - d + 1} dòng của mẫu — gộp bớt hoặc hỏi Phòng TCCB&CTHSSV "
                             "(không tự chèn dòng làm lệch công thức sheet KPI).")
        dem[n] += 1
        ghi_chu = [dv.get("ghi_chu") or ""]
        hs = dv.get("he_so")
        ws[f"B{r}"].value = dv.get("noi_dung")
        ws[f"C{r}"].value = dv.get("cap_trinh")
        ws[f"D{r}"].value = dv.get("muc_do")
        ws[f"E{r}"].value = dv.get("san_pham")
        ws[f"F{r}"].value = dv.get("so_luong")
        ws[f"G{r}"].value = dv.get("thoi_han")
        ws[f"I{r}"].value = hs
        if pa == "muc-do" and hs is not None:
            ws[f"H{r}"].value = round(float(hs) * 100)     # Diem cham = He so x 100 [QD 1923 PL I cot (9)(10)]
        elif hs is not None:
            ghi_chu.append(f"Hệ số theo phương án {pa}")
        mc = dv.get("minh_chung")
        if mc:
            if ct["cot_minh_chung"]:
                kp[f"{ct['cot_minh_chung']}{ct['kpi_dong'][r]}"].value = mc
            else:
                ghi_chu.append(f"Minh chứng: {mc}")
        ws[f"J{r}"].value = "; ".join(x for x in ghi_chu if x) or None
        # Sheet KPI cot C–F "Nhiem vu de ra ke hoach" (lenh sua 25/9/2026, L2). Khong tu bia nguoi phoi hop:
        # khong truyen thi de trong — validate_plan KH17 canh bao.
        rk = ct["kpi_dong"][r]
        kc_ = ct.get("kpi_cot", {})
        for k, v in (("chi_dao", dv.get("nguoi_chi_dao") or dv.get("cap_trinh")),
                     ("phoi_hop", dv.get("nguoi_phoi_hop")),
                     ("tham_muu", dv.get("don_vi_tham_muu") or kh.get("ca_nhan", {}).get("don_vi")),
                     ("san_pham", f"='Ke Hoach'!E{r}")):
            if k in kc_:
                kp[f"{kc_[k]}{rk}"].value = v or None
        for col in ["B"] + [kc_[k] for k in ("chi_dao", "phoi_hop", "tham_muu", "san_pham") if k in kc_]:
            canh_chu(kp[f"{col}{rk}"])
        for col in "BCDEGJ":
            if ws[f"{col}{r}"].value not in (None, ""):
                canh_chu(ws[f"{col}{r}"])
    if pa and pa != "muc-do":
        tb.append(f"Hệ số theo phương án '{pa}': {kh.get('trang_thai_he_so', '')}")
    # 4b. Trinh bay (Known-Issues-Bieu-Mau #10, #11 — phien 24–25/9 phai va tay): xuong dong + chieu cao dong
    #     cho dong da ghi; AN (khong xoa) dong trong trong khoi 20 dong/Truc, ca "Ke Hoach" lan "KPI".
    an = 0
    for d, c in ct["truc"].values():
        for r in range(d, c + 1):
            if ws[f"B{r}"].value in (None, ""):
                ws.row_dimensions[r].hidden = True
                kp.row_dimensions[ct["kpi_dong"][r]].hidden = True
                an += 1
    if an:
        tb.append(f"Đã ẩn {an} dòng trống trong khối đầu việc (không xóa — bỏ ẩn được khi cần thêm việc)")
    ws.column_dimensions["J"].width = max(ws.column_dimensions["J"].width or 0, RONG_GHI_CHU_KH)
    # 5. The thuc: phong chu Times New Roman cho moi o co noi dung (mau goc con o Calibri)
    from copy import copy
    doi = 0
    for sh in wb.worksheets:
        for row in sh.iter_rows():
            for cell in row:
                if cell.value is not None and cell.font is not None and cell.font.name != PHONG:
                    f = copy(cell.font)
                    f.name = PHONG
                    cell.font = f
                    doi += 1
    if doi:
        tb.append(f"Đã chuẩn hóa {doi} ô sang {PHONG} (mẫu gốc còn phông khác — Known-Issues-Bieu-Mau.md)")
    tb += chinh_chieu_cao(wb, ct)
    wb.save(ra)
    return tb


def main(argv):
    """Mot lenh tron quy trinh: tinh he so (kpi_calc) -> dien mau -> kiem (validate_plan).
    python scripts/kpi_mau.py --nhom hanh-chinh --json ke_hoach.json --phuong-an muc-do --quy IV --nam 2026 --ra <tep.xlsx>
    Ma thoat: 2 = loi dau vao (dung, hoi nguoi dung) · 1 = da xuat nhung con LOI · 0 = sach."""
    import argparse
    import json
    import sys
    sys.path.insert(0, HERE)
    import kpi_calc as kc
    import validate_plan as vp
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--nhom", required=True, choices=list(NHOM))
    ap.add_argument("--json", required=True)
    ap.add_argument("--phuong-an")
    ap.add_argument("--quy")
    ap.add_argument("--nam")
    ap.add_argument("--ra", required=True)
    a = ap.parse_args(argv)
    if a.phuong_an not in kc.PHUONG_AN:
        print(f"✗ Chưa chọn phương án hệ số ({', '.join(kc.PHUONG_AN)}) — Câu hỏi mở số 1, không có mặc định. "
              "Hỏi người dùng.")
        return 2
    kh = json.load(open(a.json, encoding="utf-8"))
    qd = kc.quy_doi_ke_hoach(kh, a.phuong_an)
    if qd["loi"]:
        print("✗ Không tính được hệ số — dừng, hỏi người dùng:")
        for x in qd["loi"]:
            print(f"  dòng {x['dong']} '{x['noi_dung']}': {x['loi']}")
        return 2
    kh = dict(kh, dau_viec=qd["dau_viec"], phuong_an=a.phuong_an, trang_thai_he_so=qd["trang_thai"])
    try:
        tb = ghi_ke_hoach(a.nhom, kh, a.ra, a.quy, a.nam)
    except PermissionError:
        print(f"✗ Không ghi được {a.ra}: tệp đang mở trong Excel (hoặc bị khóa) — hãy đóng tệp hoặc đặt tên mới.")
        return 2
    except (ValueError, FileNotFoundError) as e:
        print(f"✗ {e}")
        return 2
    print(f"✓ Đã xuất {a.ra}")
    print(f"  Phương án hệ số: {a.phuong_an} — {qd['trang_thai']}")
    for x in tb:
        print(f"  {'[CANH_BAO] ' if x.startswith('KH') else '· '}{x}")
    for d in qd["dau_viec"]:
        for c in d.get("canh_bao") or []:
            print(f"  ⚠ {d.get('noi_dung', '')[:50]}: {c}")
    kq = vp.kiem(a.ra, a.nhom, a.phuong_an)
    for x in sorted(kq["loi"], key=lambda x: (x["muc"] != "LOI", x["ma"])):
        print(f"  [{x['muc']:8s}] {x['ma']} {x['vi_tri']}: {x['noi_dung']}  [{x['can_cu']}]")
    print("  · Số thực tế, KPI, điểm: chưa có — sinh sau khi chạy kpi_danh_gia.py danh-gia")
    return 1 if any(x["muc"] == "LOI" for x in kq["loi"]) else 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/ktc_guard.py` (16401 byte, sha256 `6c1b3459df1196dd896c375cfe5c738218b9b38fce5bef825fbfd8d28820f69c`)

`````python
# -*- coding: utf-8 -*-
"""PreToolUse guard cua plugin ktc-quan-tri — chan GHI/XOA vao kho chuan (tham dinh doc lap lan 1, C-04; lan 2, R2-03).

Vung bao ve (so khop khong phan biet hoa thuong, ca "/" lan "\\"):
  - KTC-Database        (kho van ban, chi doc — CLAUDE.md)
  - 03-Templates        (mau .dotx/.xltx, ke ca "03-Templates(1)")
  - 04-Good-Documents   (van ban tot da ban hanh)

Pham vi kiem:
  - Write · Edit · MultiEdit · NotebookEdit: duong dan dich (file_path / notebook_path).
  - Bash · PowerShell: lenh o MUC SHELL co tac dung ghi/xoa ma DICH nam trong vung bao ve
    (rm, mv, del, rmdir, Remove-Item, Move-Item, Rename-Item, Set-Content, Add-Content, Out-File,
    New-Item, Clear-Content, chuyen huong > / >>, cp/copy/Copy-Item co DICH trong vung bao ve,
    tee, sed -i, truncate, touch).
  - 1.3.1 (tham dinh lan 3, ChatGPT P0-2): hai tang.
    TANG 1 — CHAN (exit 2) khi xac dinh chac dich ghi nam trong vung bao ve: lenh long trong
      `powershell -Command`, `pwsh -c`, `cmd /c`, `bash -c`/`sh -c` (kiem de quy); `open('<vung>', 'w')`,
      `Path('<vung>').write_text/unlink/...` trong ma Python nhung; `cd`/`Set-Location` vao vung roi ghi
      duong dan tuong doi; `-EncodedCommand` (khong phan tich duoc -> chan).
    TANG 2 — khi dich KHONG xac dinh duoc: lenh co nhac vung bao ve VA co dau hieu ghi VA co ma nhung
      (python/node/perl/powershell...) hoac bien tro vao vung bao ve. 1.3.1: hoi nguoi dung ("ask");
      1.3.2 (tham dinh lan 4, F4-01): CHAN (exit 2) — khong de lua chon "dong y" ghi vao kho chuan.
  - 1.3.2: chan tao lien ket tuong trung/cung tro vao vung bao ve (ln, mklink, New-Item -ItemType SymbolicLink)
    — lien ket la duong vong de ghi vao kho qua duong dan "ngoai".
  - Van KHONG phai lop bao ve tuyet doi: script trong tep (`python x.py`), bien moi truong dat o phien truoc,
    lien ket tuong trung... khong nhin thay duoc. Lop bao ve CHINH la phan quyen chi doc (Viewer) tren Drive.

Doc tu vung bao ve (cat, ls, python doc tep, cp TU kho RA ngoai) duoc phep.

Fail-closed: loi doc du lieu hook hoac loi noi bo -> CHAN (exit 2). Harness chi chan khi hook tra 2;
neu may khong co Python thi hook khong chay duoc — doctor dau phien bao "guard CHUA hoat dong".
Ma thoat: 0 = cho phep · 2 = chan (thong bao ra stderr cho Claude).
"""
import json
import os
import re
import shlex
import sys

# 1.3.1: khop khi ten vung la CA MOT thanh phan duong dan — tep ten "...-vao-KTC-Database.md" hay thu muc
# "Ban-trung-KTC-Database" khong phai vung bao ve (bao nham that 18-26/9/2026, 3 lenh).
VUNG_SO = r"(?<![\w.-])(?:ktc-database|03-templates(?:\(\d+\))?|04-good-documents)(?![\w.-])"
VUNG = re.compile(VUNG_SO, re.I)
CONG_CU_TEP = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
CONG_CU_LENH = {"Bash", "PowerShell"}

# dong tu ghi/xoa: moi doi so dang duong dan deu la DICH
DONG_TU_XOA_GHI = {
    "rm", "rmdir", "del", "erase", "rd", "unlink", "shred", "truncate", "touch", "mkdir",
    "remove-item", "ri", "rename-item", "ren", "set-content", "sc", "add-content", "ac",
    "out-file", "new-item", "ni", "clear-content", "clc", "tee", "tee-object", "set-itemproperty",
}
# dong tu sao chep/di chuyen: chi doi so CUOI (dich) bi xet; mv/move con xet ca nguon (xoa nguon)
DONG_TU_CHEP = {"cp", "copy", "copy-item", "cpi", "xcopy", "robocopy", "install", "rsync"}
DONG_TU_DOI = {"mv", "move", "move-item", "mi"}
# 1.3.2: tao lien ket tro vao vung bao ve (bat ke vi tri doi so) — mo duong ghi vong qua duong dan ngoai kho
DONG_TU_LIEN_KET = {"ln", "mklink", "junction", "linkd"}


def _chan(ly_do: str):
    sys.stderr.write(
        "KTC-Quan-tri guard: CHẶN — " + ly_do + "\n"
        "Kho KTC-Database, 03-Templates(1), 04-Good-Documents chỉ được ĐỌC. Ghi sản phẩm vào "
        "30-Ket-Qua/<ngày>/<loại>/; cần sửa kho thì viết đề xuất để người có thẩm quyền tự áp.\n")
    raise SystemExit(2)


def _tach_cau_lenh(lenh: str):
    """Tach chuoi lenh thanh cac cau lenh don (theo ; && || | xuong dong)."""
    return [c.strip() for c in re.split(r"(?:&&|\|\||;|\n|\|)", lenh) if c.strip()]


HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1")
SHELL_NHAN_HEREDOC = re.compile(r"(?:^|[\s;&|(])(?:bash|sh|zsh|dash|ksh|pwsh|powershell|cmd)(?:\.exe)?(?=[\s<]|$)", re.I)


def _bo_than_heredoc(lenh: str) -> str:
    """1.3.4 (chan nham that 28/9/2026): than heredoc dua cho trinh thong dich (python - <<'EOF' ... EOF) la MA, khong
    phai cau lenh shell — `if i > 45:` bi hieu la chuyen huong ghi khi dang dung trong kho. Bo than khoi phan tich cau
    lenh; than dua cho shell (bash <<EOF) thi giu. Tang 2 (kiem_toan_lenh) van xet TOAN chuoi, ke ca than heredoc."""
    dong, ra, i = lenh.split("\n"), [], 0
    while i < len(dong):
        d = dong[i]
        ra.append(d)
        m = HEREDOC.search(d)
        i += 1
        if m and not SHELL_NHAN_HEREDOC.search(d[:m.start()]):
            ket = m.group(2)
            while i < len(dong) and dong[i].strip() != ket:
                i += 1
            if i < len(dong):
                ra.append(dong[i])
                i += 1
    return "\n".join(ra)


def _tokens(cau: str):
    # Co "\" (duong dan Windows) thi tach kieu non-posix: posix coi "\" la ky tu thoat, "Drive\KTC-Database"
    # thanh "DriveKTC-Database" va lot khoi VUNG (1.3.1); non-posix giu ngoac kep trong token -> bo ngoac.
    try:
        if "\\" in cau:
            return [t[1:-1] if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'" else t
                    for t in shlex.split(cau, posix=False)]
        return shlex.split(cau, posix=True)
    except ValueError:
        return cau.split()


def _kiem_chuyen_huong(cau: str):
    # > dich · >> dich · 2> dich (bo qua >&1, > /dev/null, > $null)
    for m in re.finditer(r"\d?>>?\s*(\"[^\"]+\"|'[^']+'|[^\s;|&]+)", cau):
        dich = m.group(1).strip("\"'")
        if dich.startswith("&") or dich.lower() in ("/dev/null", "$null", "nul"):
            continue
        if VUNG.search(dich):
            _chan(f"chuyển hướng ghi vào vùng bảo vệ: {dich}")


def _gia_tri_tham_so(tok, ten):
    """PowerShell: lay gia tri cua -Destination/-Path/-LiteralPath/-FilePath."""
    ra = []
    for i, t in enumerate(tok):
        if t.lower() in ten and i + 1 < len(tok):
            ra.append(tok[i + 1])
        else:
            for n in ten:
                if t.lower().startswith(n + ":"):
                    ra.append(t.split(":", 1)[1])
    return ra



# Ma Python nhung: open('<vung>...', 'w'|'a'|'x'|'+') va Path('<vung>...').<ghi/xoa>
OPEN_GHI = re.compile(r"open\s*\(\s*[rbuf]*(['\"])[^'\"]*" + VUNG_SO + r"[^'\"]*\1\s*,\s*(?:mode\s*=\s*)?[rbf]*['\"][^'\"]*[wax+]", re.I)
PATH_GHI = re.compile(r"Path\s*\(\s*[rbuf]*(['\"])[^'\"]*" + VUNG_SO + r"[^'\"]*\1\s*\)\s*(?:/\s*['\"][^'\"]*['\"]\s*)*\."
                      r"(?:write_text|write_bytes|unlink|rename|replace|touch|mkdir|rmdir|open\s*\([^)]*['\"][wax+])", re.I)
# Trinh thong dich / vo lenh co the chay ma nhung
THONG_DICH = re.compile(r"(?:^|[\s;&|(`$])(?:python[\d.]*|py|node|deno|bun|perl|ruby|php|powershell|pwsh|cmd|bash|sh|zsh|"
                        r"wscript|cscript|mshta)(?:\.exe)?(?=[\s\"']|$)", re.I)
# Dau hieu ghi/xoa trong toan lenh (dung cho tang 2 — dich khong xac dinh)
# 1.3.3: .rename(/.replace( chi tinh la ghi khi lenh co Path(...) (hoac os.rename/os.replace o duoi) — chan nham
# that 28/9/2026: str.replace() trong python -c doc kho bi coi la ghi.
GHI = re.compile(r"""(?ix)
   open\s*\([^)]*,\s*(?:mode\s*=\s*)?[rbf]*['"][^'"]*[wax+]
 | \.(?:write|write_text|write_bytes|writelines|save|to_excel|to_csv|unlink|touch|mkdir|rmdir)\s*\(
 | \bpath\s*\([\s\S]*\.(?:rename|replace)\s*\(
 | \.(?:writefile|appendfile|rm|rmsync|copyfile|createwritestream|unlinksync|renamesync|mkdirsync)\w*\s*\(
 | \bshutil\.(?:copy\w*|move|rmtree) | \bos\.(?:remove|unlink|rename|replace|rmdir|removedirs|makedirs|mkdir|truncate)
 | \b(?:set|add|clear)-content\b | \bout-file\b | \b(?:remove|move|copy|rename|new)-item\b
 | \[(?:system\.)?io\.(?:file|directory)\]:: | \bfs\.(?:write|append|rm|unlink|rename|copy|mkdir|cp)\w*
 | (?:^|[\s;&|(])(?:rm|rmdir|mv|cp|del|erase|rd|ren|move|copy|xcopy|robocopy|touch|tee|truncate|mkdir|unlink)(?=\s)
""")
# Bien gan duong dan vung bao ve: D="..KTC-Database..", $d = '..', set D=..
BIEN_VUNG = re.compile(r"(?:\$?[\w:]+\s*=\s*|\bset\s+\w+=)(?:\"[^\"]*|'[^']*|[^\"'\s;]*)" + VUNG_SO, re.I)
DONG_TU_CD = {"cd", "pushd", "chdir", "set-location", "sl", "push-location"}
VO_LENH = {"powershell", "powershell.exe", "pwsh", "pwsh.exe", "cmd", "cmd.exe", "bash", "sh", "zsh"}
CO_LENH_LONG = {"-c", "-command", "/c", "/k", "-comm", "-com"}
CO_MA_HOA = {"-encodedcommand", "-enc", "-ec", "-e", "-en", "-enco", "-encod"}


def _tuong_doi(t: str) -> bool:
    t = t.strip("\"'")
    # 1.3.2: "[\\/]" — ban 1.3.1 ghi "[\/]" (heredoc nuot dau "\") nen "C:\..." bi coi la duong dan tuong doi
    return bool(t) and not re.match(r"^(?:[a-z]:[\\/]|[\\/]|~|\$|%)", t, re.I)


def kiem_toan_lenh(lenh: str):
    """Kiem cap toan chuoi lenh (truoc khi tach cau): ma nhung, ma hoa, tang 2."""
    if OPEN_GHI.search(lenh) or PATH_GHI.search(lenh):
        _chan("mã nhúng mở/ghi/xóa tệp trong vùng bảo vệ")
    kiem_lenh(lenh)
    # 1.3.2 (tham dinh lan 4, ChatGPT F4-01): khong xac dinh duoc dich ma co dau hieu ghi vao vung bao ve -> CHAN
    # (truoc la "hoi nguoi dung"). Chay lai 1.481 lenh that: 0 lenh roi vao nhanh nay -> khong tang chan nham.
    if VUNG.search(lenh) and GHI.search(lenh) and (THONG_DICH.search(lenh) or BIEN_VUNG.search(lenh)):
        _chan("lệnh có nhắc vùng bảo vệ, có dấu hiệu ghi/xóa và có mã nhúng hoặc biến trỏ vào vùng bảo vệ — không "
              "xác định được đích ghi. Ghi sản phẩm bằng đường dẫn tường minh ngoài kho, hoặc tách bước đọc kho và "
              "bước ghi thành hai lệnh riêng")


def kiem_lenh(lenh: str, sau: int = 0):
    if sau > 3:
        _chan("lệnh lồng quá sâu, không phân tích được")
    trong_vung = False     # da cd/Set-Location vao vung bao ve
    for cau in _tach_cau_lenh(_bo_than_heredoc(lenh)):
        _kiem_chuyen_huong(cau)
        tok = _tokens(cau)
        if not tok:
            continue
        # bo tien to kieu `sudo`, `command`, `&`
        while tok and tok[0].lower() in ("sudo", "command", "&", "call"):
            tok = tok[1:]
        if not tok:
            continue
        dt = tok[0].lower().rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
        doi_so = [t for t in tok[1:] if not t.startswith("-")]
        if dt in DONG_TU_CD:
            dich = " ".join(doi_so)
            trong_vung = bool(VUNG.search(dich)) or (trong_vung and _tuong_doi(dich))
            continue
        if dt in VO_LENH:
            thap = [t.lower() for t in tok[1:]]
            if any(t in CO_MA_HOA for t in thap) and dt.startswith(("powershell", "pwsh")):
                _chan("lệnh PowerShell mã hóa (-EncodedCommand) không kiểm được")
            # cat NGUYEN VAN phan lenh con tu chuoi goc — ghep lai tu token shlex se mat dau "\" cua duong dan Windows
            m = re.search(r"(?i)(?:^|\s)(?:-c|-command|-comm?|/c|/k)\s+(.+)$", cau, re.S)
            if m:
                con = m.group(1).strip()
                if len(con) >= 2 and con[0] == con[-1] and con[0] in "\"'":
                    con = con[1:-1]
                kiem_lenh(con, sau + 1)
        if trong_vung:
            # dang dung trong vung bao ve: ghi vao duong dan tuong doi = ghi vao kho
            for m in re.finditer(r"\d?>>?\s*(\"[^\"]+\"|'[^']+'|[^\s;|&]+)", cau):
                d = m.group(1).strip("\"'")
                if not d.startswith("&") and d.lower() not in ("/dev/null", "$null", "nul") and _tuong_doi(d):
                    _chan(f"chuyển hướng ghi `{d}` khi đang đứng trong vùng bảo vệ")
            if dt in DONG_TU_XOA_GHI | DONG_TU_DOI | DONG_TU_CHEP and any(_tuong_doi(t) for t in doi_so):
                _chan(f"lệnh `{dt}` với đường dẫn tương đối khi đang đứng trong vùng bảo vệ")
        if dt in ("sed", "perl") and any(t.startswith("-i") for t in tok[1:]):
            # 1.3.2 (chan nham that 27/9/2026 18:4x): chi xet TEP DICH, khong xet bieu thuc sed/perl — bieu thuc
            # co chu "KTC-Database" (vd thay chu trong mot tep ngoai kho) khong phai duong dan ghi.
            # Bieu thuc: doi so sau -e/--expression/-f; neu khong co -e thi doi so khong-tuy-chon DAU TIEN.
            bt, tep, i, co_e = set(), [], 1, False
            while i < len(tok):
                t = tok[i]
                if t in ("-e", "--expression", "-f", "--file") and i + 1 < len(tok):
                    bt.add(i + 1)
                    co_e = True
                    i += 2
                    continue
                i += 1
            khong_tuy_chon = [k for k in range(1, len(tok)) if not tok[k].startswith("-") and k not in bt]
            if not co_e and khong_tuy_chon:
                khong_tuy_chon = khong_tuy_chon[1:]          # bo bieu thuc sed dung tran
            tep = [tok[k] for k in khong_tuy_chon]
            if any(VUNG.search(t) for t in tep):
                _chan(f"sửa tại chỗ ({dt} -i) tệp trong vùng bảo vệ")
            continue
        if dt in DONG_TU_LIEN_KET or (dt in ("cmd", "cmd.exe") and "mklink" in cau.lower()):
            if VUNG.search(cau):
                _chan(f"tạo liên kết (`{dt}`) trỏ vào vùng bảo vệ")
        if dt in ("new-item", "ni") and re.search(r"-itemtype\s+['\"]?(symboliclink|junction|hardlink)", cau, re.I):
            if VUNG.search(cau):
                _chan("tạo liên kết (New-Item -ItemType SymbolicLink/Junction) trỏ vào vùng bảo vệ")
        if dt in DONG_TU_XOA_GHI:
            if any(VUNG.search(t) for t in tok[1:]):
                _chan(f"lệnh `{dt}` tác động vào vùng bảo vệ")
        elif dt in DONG_TU_DOI:
            if any(VUNG.search(t) for t in tok[1:]):
                _chan(f"lệnh `{dt}` di chuyển/đổi tên trong vùng bảo vệ")
        elif dt in DONG_TU_CHEP:
            dich = _gia_tri_tham_so(tok, ("-destination", "-dest"))
            if not dich and doi_so:
                dich = [doi_so[-1]]
            if dt == "robocopy" and len(doi_so) >= 2:
                dich = [doi_so[1]]
            if any(VUNG.search(d) for d in dich):
                _chan(f"lệnh `{dt}` chép vào vùng bảo vệ: {dich[0]}")


GOC_PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _trong_plugin(p: str) -> bool:
    """1.3.6 (chay that 28/9/2026): skill bao-cao ghi 'bo nho qua trinh' vao chinh tep cua plugin da cai. Tep plugin la
    ban phat hanh — sua o may nguoi dung se mat khi cap nhat va lech giua cac may."""
    if not p:
        return False
    ap = os.path.normcase(os.path.abspath(p))
    if re.search(r"[\\/]\.claude[\\/]plugins[\\/]", ap):
        return True
    goc = os.path.normcase(GOC_PLUGIN)
    return os.path.isdir(os.path.join(GOC_PLUGIN, ".claude-plugin")) and (ap == goc or ap.startswith(goc + os.sep))


def kiem(data: dict):
    ten = data.get("tool_name") or ""
    vao = data.get("tool_input") or {}
    if ten in CONG_CU_TEP:
        p = vao.get("file_path") or vao.get("notebook_path") or ""
        if VUNG.search(str(p)):
            _chan(f"{ten} vào {p}")
        if _trong_plugin(str(p)):
            _chan(f"{ten} vào tệp của plugin đã cài ({p}). Không sửa tệp plugin; ghi nhật ký, bộ nhớ quá trình, sản phẩm "
                  "vào thư mục làm việc (30-Ket-Qua/<ngày>/<loại>/, ghi chú đối soát)")
    elif ten in CONG_CU_LENH:
        kiem_toan_lenh(str(vao.get("command") or ""))


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("dữ liệu hook không phải đối tượng JSON")
    except Exception as e:  # fail-closed
        _chan(f"không đọc được dữ liệu hook ({e})")
    try:
        kiem(data)
    except SystemExit:
        raise
    except Exception as e:  # fail-closed
        _chan(f"lỗi nội bộ của guard ({e})")
    raise SystemExit(0)


if __name__ == "__main__":
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
`````

## `scripts/ktc_nhat_ky.py` (18165 byte, sha256 `f2935b8ee21c6ec17b430a8253387f851e937f282910b3cc85ac90825c387cf1`)

`````python
# -*- coding: utf-8 -*-
"""Tu ghi nhat ky phien lam viec va nap lai vao context khi mo phien moi.

Goi tu hooks.json voi 1 trong 4 che do:
  ghi       PostToolUse      — ghi 1 dong JSONL: thoi gian, phien, cong cu, doi tuong (KHONG ghi noi dung tep).
                               1.3.1 (tham dinh lan 3, ChatGPT P0-1): KHONG luu lenh Bash/PowerShell, mo ta Agent,
                               mau Grep/Glob tho — chi luu loai hanh dong + chuong trinh; tep: duong dan tuong doi.
                               Lenh (da che du lieu) chi luu khi chu may chon KTC_NHAT_KY_NOI_DUNG=1.
  yeu-cau   UserPromptSubmit — MAC DINH chi ghi do dai + nhan tin hieu hoc; noi dung (cat 600 ky tu) chi khi
                               nguoi dung chon: mo dau "#học" hoac bien KTC_NHAT_KY_NOI_DUNG=1 (1.3.0, R2-02)
  ket-phien SessionEnd       — ghi dong danh dau ket thuc phien
  nap       SessionStart     — in tom tat 2 ngay + tri thuc tu hoc + so tin hieu chua hoc -> context

Chi hoat dong khi thu muc du an co `90-Nhat-Ky-Van-Hanh/` (tuc la dang lam viec trong KTC-Quan-tri) —
plugin bat o cap nguoi dung nen phai tu gioi han pham vi, khong ghi log vao du an khac.
Moi loi deu nuot va thoat 0: hook ghi log khong bao gio duoc lam hong phien lam viec.
"""
import datetime as dt
import io
import json
import os
import re
import sys

THU_MUC_LOG = os.path.join("90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
DAI_TOI_DA = 200          # cat ngan lenh/duong dan dai
SO_DONG_NAP = 5           # so thao tac gan nhat dua vao context (1.3.1: 15 -> 5, khong in lenh)
# 1.3.1 (ChatGPT P1-1): ngan sach phan nap dau phien ~1.500 token (~4.500 ky tu tieng Viet). Vuot thi cat
# danh sach tri thuc, bao so muc con lai. KTC_NAP_DAY_DU=1 -> ban day du (15 thao tac, 12 tep, 160 ky tu/muc).
NGAN_SACH_NAP = 4500
CONG_CU_TEP = ("Write", "Edit", "MultiEdit", "Read", "NotebookEdit")
MAU_GHI_LENH = re.compile(r"(?:>|\b(?:rm|mv|cp|mkdir|touch|tee|del|move|copy|sed\s+-i|set-content|add-content|out-file|"
                          r"remove-item|copy-item|move-item|new-item|rename-item)\b)", re.I)


def doc_stdin() -> dict:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def tim_du_an(data: dict):
    # Chi lui ve getcwd khi hook KHONG cho biet thu muc nao — neu hook da cho cwd ngoai du an
    # thi phai bo qua, khong duoc ghi nham vao du an dang chua script (loi 18/9/2026).
    ung_vien = [os.environ.get("CLAUDE_PROJECT_DIR"), data.get("cwd")]
    if not any(ung_vien):
        ung_vien.append(os.getcwd())
    for p in ung_vien:
        if not p:
            continue
        p = os.path.abspath(p)
        # di nguoc len toi da 4 cap de tim goc du an
        for _ in range(5):
            if os.path.isdir(os.path.join(p, "90-Nhat-Ky-Van-Hanh")):
                return p
            cha = os.path.dirname(p)
            if cha == p:
                break
            p = cha
    return None


def _tuong_doi(du_an, p: str) -> str:
    p = str(p)
    try:
        if du_an and os.path.abspath(p).lower().startswith(os.path.abspath(du_an).lower() + os.sep):
            return os.path.relpath(p, du_an).replace("\\", "/")
    except (ValueError, OSError):
        pass
    return p.replace("\\", "/")


def phan_loai_lenh(lenh: str) -> dict:
    """Mo ta lenh KHONG luu noi dung: chuong trinh dau tien + loai hanh dong."""
    lenh = str(lenh).strip()
    m = re.match(r"(?:cd\s+(?:\"[^\"]*\"|'[^']*'|\S+)\s*(?:;|&&)\s*)?(?:\w+=\S*\s+)*([^\s;|&]+)", lenh)
    ct = (m.group(1) if m else "").strip("\"'&").replace("\\", "/").rsplit("/", 1)[-1][:24]
    if re.search(r"\bgit\s+(?:commit|push|add|reset|checkout|rm)\b", lenh):
        hd = "git-ghi"
    elif MAU_GHI_LENH.search(lenh):
        hd = "ghi"
    elif re.search(r"\b(?:python\d*|py|node|powershell|pwsh)\b", lenh, re.I):
        hd = "chay-script"
    else:
        hd = "doc"
    return {"chuong_trinh": ct, "hanh_dong": hd}


def doi_tuong(tool: str, inp: dict, du_an: str = None) -> str:
    """Doi tuong DUOC PHEP luu mac dinh: duong dan tep (tuong doi), ten skill, loai agent. Lenh, mo ta Agent,
    mau tim kiem la noi dung tho -> khong tra ve o day (1.3.1, P0-1)."""
    if tool in CONG_CU_TEP:
        s = _tuong_doi(du_an, inp.get("file_path") or inp.get("notebook_path") or "")
    elif tool == "Skill":
        s = inp.get("skill", "")
    elif tool == "Agent":
        s = inp.get("subagent_type", "") or "general"
    else:
        s = ""
    s = che_du_lieu(" ".join(str(s).split()))
    return s[:DAI_TOI_DA] + ("…" if len(s) > DAI_TOI_DA else "")


def chi_tiet_tho(tool: str, inp: dict) -> str:
    """Noi dung tho — CHI luu khi chu may chon KTC_NHAT_KY_NOI_DUNG=1; luon che du lieu."""
    if tool in ("Bash", "PowerShell"):
        s = inp.get("command", "")
    elif tool in ("Grep", "Glob"):
        s = inp.get("pattern", "")
    elif tool == "Agent":
        s = inp.get("description", "")
    else:
        return ""
    s = che_du_lieu(" ".join(str(s).split()))
    return s[:DAI_TOI_DA] + ("…" if len(s) > DAI_TOI_DA else "")


# Tin hieu hoc trong LOI NGUOI DUNG (DL-20260919-005). Chi danh dau de agent ktc-tu-hoc doc lai;
# hook KHONG tu rut ket luan. Nhom: sua-sai · quy-uoc · quyet-dinh.
TIN_HIEU = {
    "sua-sai": r"\b(sai|nhầm|chưa đúng|không đúng|không phải|sửa lại|làm lại|lỗi|thiếu)\b",
    "quy-uoc": r"(từ nay|từ giờ|sau này|luôn luôn|\bluôn\b|đừng|không được|phải|quy ước|lưu ý|nhớ|ghi nhớ|mặc định)",
    "quyet-dinh": r"(đồng ý|thống nhất|chốt|quyết định|phê duyệt|lãnh đạo.{0,20}(đã|thống nhất)|giữ phương án)",
}
# 1.3.0 (TT-20260924-08): bo gan bao gia nhieu — bo loi < 5 tu ("ok", "em cu lam luon"), bo "OK" tran,
# bo so hieu van ban ("Quyet dinh so 1899/QD-CDKT", "QD 1923") truoc khi do tin hieu quyet-dinh.
SO_TU_TOI_THIEU = 5
MAU_SO_HIEU_VB = r"(quyết định|thông báo|kế hoạch|công văn|tờ trình|báo cáo|QĐ|TB|KH|CV|BC)\s*(số\s*)?\d+[\w/\-]*"
# Che du lieu ca nhan truoc khi ghi noi dung (khi nguoi dung da chon ghi)
CHE = [
    (r"(?<![0-9A-Za-z])0\d{11}(?![0-9A-Za-z])", "[SỐ ĐỊNH DANH]"),
    (r"(?<![0-9A-Za-z])(\+84|0)\d{9}(?![0-9A-Za-z])", "[SỐ ĐIỆN THOẠI]"),
    (r"[\w.+-]+@[\w-]+\.[\w.-]+", "[EMAIL]"),
]


def che_du_lieu(s: str) -> str:
    for mau, thay in CHE:
        s = re.sub(mau, thay, s)
    return s
TEP_TRI_THUC = os.path.join("90-Nhat-Ky-Van-Hanh", "05-Tri-Thuc-Tu-Hoc")
DAI_YEU_CAU = 600
SO_TRI_THUC_NAP = 25
NGAY_LUU_GIU = 30          # 1.3.0: tep nhat ky cu hon 30 ngay bi xoa khi mo phien (che do nap)


def don_nhat_ky_cu(du_an: str, ngay: int = NGAY_LUU_GIU) -> int:
    """Xoa tep YYYY-MM-DD.jsonl cu hon `ngay` ngay. Tra ve so tep da xoa."""
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    if not os.path.isdir(thu_muc):
        return 0
    moc = dt.date.today() - dt.timedelta(days=ngay)
    xoa = 0
    for f in os.listdir(thu_muc):
        m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})\.jsonl", f)
        if not m:
            continue
        try:
            if dt.date.fromisoformat(m.group(1)) < moc:
                os.remove(os.path.join(thu_muc, f))
                xoa += 1
        except (ValueError, OSError):
            pass
    return xoa


def tin_hieu(s: str):
    if len(s.split()) < SO_TU_TOI_THIEU:
        return []
    s = re.sub(MAU_SO_HIEU_VB, " ", s, flags=re.I)
    return [k for k, m in TIN_HIEU.items() if re.search(m, s, re.I)]


def ghi_dong(du_an: str, dong: dict):
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    os.makedirs(thu_muc, exist_ok=True)
    tep = os.path.join(thu_muc, dt.date.today().isoformat() + ".jsonl")
    with io.open(tep, "a", encoding="utf-8") as f:
        f.write(json.dumps(dong, ensure_ascii=False) + "\n")


def che_do_ghi(data: dict, loai: str):
    du_an = tim_du_an(data)
    if not du_an:
        return
    tool = data.get("tool_name", "")
    if loai == "thao-tac" and not tool:
        return  # du lieu hook hong/thieu — khong ghi dong rong
    dong = {
        "t": dt.datetime.now().isoformat(timespec="seconds"),
        "phien": (data.get("session_id") or "")[:8],
        "loai": loai,
    }
    if loai == "thao-tac":
        dong["cong_cu"] = tool
        inp = data.get("tool_input") or {}
        dt_ = doi_tuong(tool, inp, du_an)
        if dt_:
            dong["doi_tuong"] = dt_
        if tool in ("Bash", "PowerShell"):
            dong.update(phan_loai_lenh(inp.get("command", "")))
        if os.environ.get("KTC_NHAT_KY_NOI_DUNG") == "1":
            ct = chi_tiet_tho(tool, inp)
            if ct:
                dong["chi_tiet"] = ct
        resp = data.get("tool_response")
        if isinstance(resp, dict) and (resp.get("is_error") or resp.get("error")):
            dong["loi"] = True
    elif loai == "yeu-cau":
        s = " ".join(str(data.get("prompt") or "").split())
        # Lenh noi bo cua Claude Code (/compact, <command-...>) khong phai loi nguoi dung
        if not s or s.startswith("<") or s.startswith("/"):
            return
        # "#riêng ..." — nguoi dung tu danh dau noi dung rieng tu: chi ghi moc thoi gian (CP-20260924-001, C)
        if re.match(r"#ri[eê]ng\b", s, re.I):
            dong["noi_dung"] = "[#riêng — không ghi]"
            ghi_dong(du_an, dong)
            return
        # 1.3.0 (tham dinh lan 2, R2-02): MAC DINH chi ghi thong tin mo ta — do dai + nhan tin hieu.
        # Noi dung chi ghi khi nguoi dung CHU DONG chon, va luon che du lieu ca nhan truoc khi ghi:
        #   - loi nhan mo dau "#học": ghi loi nhan do (du co tin hieu hay khong);
        #   - chu may tu dat KTC_NHAT_KY_NOI_DUNG=1 (vd .claude/settings.local.json cua du an): chi ghi loi
        #     CO tin hieu hoc — dung nguon ma agent ktc-tu-hoc can, bo qua moi loi nhan con lai.
        dong["do_dai"] = len(s)
        chon_hoc = re.match(r"#h[oọ]c\b", s, re.I)
        if chon_hoc:
            s = s[chon_hoc.end():].strip()
        th = tin_hieu(s)
        if th:
            dong["tin_hieu"] = th
        if chon_hoc or (th and os.environ.get("KTC_NHAT_KY_NOI_DUNG") == "1"):
            dong["chon_ghi"] = "#học" if chon_hoc else "KTC_NHAT_KY_NOI_DUNG"
            s = che_du_lieu(s)
            dong["noi_dung"] = s[:DAI_YEU_CAU] + ("…" if len(s) > DAI_YEU_CAU else "")
    else:
        dong["ly_do"] = data.get("reason", "")
    ghi_dong(du_an, dong)


def doc_log(du_an: str, so_ngay: int = 2):
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    if not os.path.isdir(thu_muc):
        return []
    tep = sorted(f for f in os.listdir(thu_muc) if f.endswith(".jsonl"))[-so_ngay:]
    dong = []
    for f in tep:
        with io.open(os.path.join(thu_muc, f), encoding="utf-8", errors="ignore") as h:
            for line in h:
                try:
                    dong.append(json.loads(line))
                except Exception:
                    pass
    return dong


def moi_nhat(thu_muc: str):
    if not os.path.isdir(thu_muc):
        return None
    tep = sorted(f for f in os.listdir(thu_muc) if f.endswith(".md"))
    return tep[-1] if tep else None


def nap_tri_thuc(du_an: str, ra: list, day_du: bool = False):
    """Tri thuc tu hoc con hieu luc/cho duyet + so tin hieu hoc CHUA xu ly ke tu lan hoc cuoi -> `ra` (danh sach dong)."""
    thu_muc = os.path.join(du_an, TEP_TRI_THUC)
    tep = os.path.join(thu_muc, "TRI-THUC.md")
    muc = []
    if os.path.isfile(tep):
        for d in io.open(tep, encoding="utf-8", errors="ignore"):
            o = [x.strip() for x in d.strip().strip("|").split("|")]
            if len(o) >= 6 and re.match(r"TT-\d{8}-\d+", o[0]) and re.match(r"(hiệu lực|chờ duyệt)", o[5], re.I):
                muc.append(o)
    moc = ""
    try:
        moc = io.open(os.path.join(thu_muc, ".lan-hoc-cuoi"), encoding="utf-8").read().strip()
    except OSError:
        pass
    chua = [d for d in doc_log(du_an, so_ngay=14)
            if d.get("loai") == "yeu-cau" and d.get("tin_hieu") and d.get("t", "") > moc]
    ra.append(f"--- Tri thức tự học ({len(muc)} mục hiệu lực/chờ duyệt — {TEP_TRI_THUC}/TRI-THUC.md) ---")
    dai = 160 if day_du else 100
    for o in muc[-SO_TRI_THUC_NAP:]:
        dau = "?" if o[5].lower().startswith("chờ") else "•"
        noi = o[2] if len(o[2]) <= dai else o[2][:dai - 1] + "…"
        ra.append(f"  {dau} [{o[0]}·{o[1]}] {noi}")
    if chua:
        ra.append(f"  ⟳ {len(chua)} tín hiệu học CHƯA xử lý — gọi agent ktc-tu-hoc để rút tri thức.")


def lam_sach_nhat_ky_cu(du_an: str) -> int:
    """1.3.1 (P0-1): go lenh/mo ta/mau tho khoi nhat ky da ghi truoc 1.3.1 — tru khi chu may chon ghi noi dung.
    Tra ve so dong da lam sach. Ghi lai tep qua tep tam roi thay the (khong de tep do dang)."""
    if os.environ.get("KTC_NHAT_KY_NOI_DUNG") == "1":
        return 0
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    if not os.path.isdir(thu_muc):
        return 0
    n = 0
    for f in os.listdir(thu_muc):
        if not f.endswith(".jsonl"):
            continue
        p = os.path.join(thu_muc, f)
        dong, doi = [], False
        for line in io.open(p, encoding="utf-8", errors="ignore"):
            try:
                d = json.loads(line)
            except Exception:
                continue
            cc = d.get("cong_cu")
            if d.get("loai") == "thao-tac" and cc not in CONG_CU_TEP and cc != "Skill" and "hanh_dong" not in d \
                    and d.get("doi_tuong"):
                tho = d.pop("doi_tuong")
                if cc in ("Bash", "PowerShell"):
                    d.update(phan_loai_lenh(tho))
                elif cc == "Agent":
                    d["doi_tuong"] = tho.split(":", 1)[0].strip() or "general"
                d["da_lam_sach"] = "1.3.1"
                doi, n = True, n + 1
            d.pop("chi_tiet", None)
            dong.append(d)
        if doi:
            tam = p + ".tam"
            with io.open(tam, "w", encoding="utf-8") as h:
                for d in dong:
                    h.write(json.dumps(d, ensure_ascii=False) + "\n")
            os.replace(tam, p)
    return n


def che_do_nap(data: dict):
    du_an = tim_du_an(data)
    if not du_an:
        return
    day_du = os.environ.get("KTC_NAP_DAY_DU") == "1"
    don_nhat_ky_cu(du_an)
    lam_sach_nhat_ky_cu(du_an)
    dong = doc_log(du_an)
    thao_tac = [d for d in dong if d.get("loai") == "thao-tac"]
    sua_tat_ca = {_tuong_doi(du_an, d["doi_tuong"]) for d in thao_tac
                  if d.get("cong_cu") in ("Write", "Edit", "MultiEdit") and d.get("doi_tuong")}
    # chi in tep TRONG du an (duong dan tuong doi); tep ngoai (thu muc tam...) chi dem
    sua = sorted(x for x in sua_tat_ca if not (":" in x[:3] or x.startswith("/")))
    ngoai = len(sua_tat_ca) - len(sua)
    loi = [d for d in thao_tac if d.get("loi")]
    phien = sorted({d.get("phien") for d in dong if d.get("phien")})

    dau = ["=== KTC-Quan-tri — nhật ký tự động 2 ngày gần nhất (nạp vào context) ==="]
    if not dong:
        dau.append("Chưa có nhật ký tự động. (Ghi bắt đầu từ phiên này.)")
    else:
        dau.append(f"{len(phien)} phiên · {len(thao_tac)} thao tác · {len(sua)} tệp dự án đã ghi/sửa"
                   + (f" (+{ngoai} tệp ngoài dự án)" if ngoai else "") + f" · {len(loi)} thao tác lỗi")
        so_tep = 12 if day_du else 8
        if sua:
            dau.append(f"Tệp dự án đã ghi/sửa ({min(len(sua), so_tep)}/{len(sua)}):")
            dau += [f"  - {s}" for s in sua[-so_tep:]]
        so = 15 if day_du else SO_DONG_NAP
        dau.append(f"{so} thao tác gần nhất (không in lệnh — P0-1):")
        for d in thao_tac[-so:]:
            ky = "✗" if d.get("loi") else "·"
            if d.get("cong_cu") in ("Bash", "PowerShell"):
                pl = d if "hanh_dong" in d else phan_loai_lenh(d.get("doi_tuong", ""))
                mo_ta = f"{pl.get('chuong_trinh', '')} ({pl.get('hanh_dong', '')})"
            elif d.get("cong_cu") in CONG_CU_TEP or d.get("cong_cu") in ("Skill", "Agent"):
                mo_ta = _tuong_doi(du_an, d.get("doi_tuong", "")).split(":", 1)[0] if d.get("cong_cu") == "Agent"                     else _tuong_doi(du_an, d.get("doi_tuong", ""))
            else:
                mo_ta = ""
            dau.append(f"  {ky} {d['t'][5:16]} {d.get('cong_cu', ''):10s} {mo_ta[:90]}")

    tri = []
    nap_tri_thuc(du_an, tri, day_du)

    duoi = []
    pm = moi_nhat(os.path.join(du_an, "90-Nhat-Ky-Van-Hanh", "03-Process-Memory"))
    cp = moi_nhat(os.path.join(du_an, "92-Kinh-Nghiem", "03-Change-Proposals"))
    dl = moi_nhat(os.path.join(du_an, "92-Kinh-Nghiem", "06-Decision-Log"))
    duoi.append("Bản ghi gần nhất:")
    for nhan, v in (("Process Memory", pm), ("Đề xuất cải tiến", cp), ("Decision Log", dl)):
        duoi.append(f"  - {nhan}: {v or '(chưa có)'}")
    duoi.append("Nhắc: đọc MEMORY-INDEX.md và Pending.md trước khi làm việc (CLAUDE.md).")
    duoi.append("=" * 72)

    # Ngan sach: cat bot muc tri thuc CU NHAT (giu dong tieu de va dong tin hieu) cho toi khi vua
    if not day_du:
        def tong():
            return sum(len(x) + 1 for x in dau + tri + duoi)
        bo = 0
        while tong() > NGAN_SACH_NAP - 80 and len(tri) > 2:
            del tri[1]
            bo += 1
        if bo:
            tri.insert(1, f"  … {bo} mục cũ hơn không nạp (ngân sách context) — đọc TRI-THUC.md khi cần.")
    print("\n".join(dau + tri + duoi))


def main():
    che_do = sys.argv[1] if len(sys.argv) > 1 else "ghi"
    data = doc_stdin()
    try:
        if che_do == "ghi":
            che_do_ghi(data, "thao-tac")
        elif che_do == "ket-phien":
            che_do_ghi(data, "ket-phien")
        elif che_do == "yeu-cau":
            che_do_ghi(data, "yeu-cau")
        elif che_do == "nap":
            che_do_nap(data)
    except Exception:
        pass   # hook log khong duoc lam hong phien


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
    raise SystemExit(0)
`````

## `scripts/ktc_quan_tri_doctor.py` (5181 byte, sha256 `f02b0f6647f3b1e1b56d14909527448f320fb0c1ac3128772ff92116b2d0d98a`)

`````python
# -*- coding: utf-8 -*-
"""SessionStart doctor cho plugin ktc-quan-tri — in phien ban plugin va phien ban tu khai cua moi skill dang bat.

Doc truc tiep tu SKILL.md tu khai (khong suy dien tu ten thu muc/ten file), dung
bai hoc da ghi 18/9/2026: "Khong suy dien phien ban tu ten tep."
"""
import io
import os
import re

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(GOC, "skills")

# Uu tien 1: dong ghi tuong minh "Phien ban: X.Y" (ke-hoach, soan-thao-vb, theo-doi-cv).
# Uu tien 2: dong tieu de ket thuc bang "vX.Y" (bao-cao dang "# ... KTC-RIS v3.7").
MAU_TUONG_MINH = re.compile(r"Phi[eê]n b[aả]n:?\s*v?([0-9]+\.[0-9]+(?:\.[0-9]+)?)", re.IGNORECASE)
MAU_TIEU_DE_CUOI_DONG = re.compile(r"^#.*\bv([0-9]+\.[0-9]+(?:\.[0-9]+)?)\s*$", re.MULTILINE)


def doc_phien_ban(skill_md: str) -> str:
    try:
        s = io.open(skill_md, encoding="utf-8").read()
    except OSError:
        return "?"
    m = MAU_TUONG_MINH.search(s)
    if m:
        return m.group(1)
    m = MAU_TIEU_DE_CUOI_DONG.search(s)
    if m:
        return m.group(1)
    return "(không tự khai)"


def main():
    print("=" * 60)
    pb_plugin = "?"
    try:
        import json
        pb_plugin = json.load(io.open(os.path.join(GOC, ".claude-plugin", "plugin.json"), encoding="utf-8"))["version"]
    except Exception:
        pass
    print(f"KTC-Quan-tri Plugin {pb_plugin} — SessionStart doctor")
    print("=" * 60)
    if not os.path.isdir(SKILLS_DIR):
        print("  ✗ Không thấy thư mục skills/ — plugin có thể chưa build đúng.")
        return
    for ten in sorted(os.listdir(SKILLS_DIR)):
        skill_md = os.path.join(SKILLS_DIR, ten, "SKILL.md")
        if not os.path.exists(skill_md):
            print(f"  ✗ {ten:14s} thiếu SKILL.md")
            continue
        pb = doc_phien_ban(skill_md)
        print(f"  ✓ {ten:14s} phiên bản tự khai: {pb}")
    print("-" * 60)
    kiem_guard()
    kiem_phu_thuoc()
    kiem_thu_muc()
    print("=" * 60)


def kiem_thu_muc():
    """1.3.5: che do thu muc — du an / thu muc lam viec cua don vi / chua ket noi (giao tep trong phien)."""
    import sys
    try:
        sys.path.insert(0, os.path.join(GOC, "scripts"))
        from ktc_thu_muc import tim_goc
        che_do, goc, ma = tim_goc()
    except Exception as e:
        print(f"  · thư mục làm việc: không kiểm được ({e.__class__.__name__})")
        return
    if che_do == "du-an":
        print(f"  ✓ thư mục: dự án KTC-Quan-tri ({goc})")
    elif che_do == "don-vi":
        print(f"  ✓ thư mục làm việc đơn vị {ma}: {goc} — đầu vào 10-Dau-Vao/, kết quả 30-Ket-Qua/")
    else:
        print("  · chưa kết nối thư mục làm việc — kết quả giao trong phiên. Muốn đọc 10-Dau-Vao/, lưu 30-Ket-Qua/ tự động:"
              " chọn một thư mục trong Cowork rồi yêu cầu “kết nối thư mục KTC cho đơn vị <mã>”.")


def kiem_guard():
    """Tu thu guard: mot lenh ghi gia vao KTC-Database PHAI bi chan (ma 2), ghi vao 30-Ket-Qua PHAI qua (ma 0)."""
    import json
    import subprocess
    import sys
    g = os.path.join(GOC, "scripts", "ktc_guard.py")
    if not os.path.isfile(g):
        print("  ✗ guard: THIẾU scripts/ktc_guard.py — KHÔNG có bảo vệ ghi kho chuẩn")
        return
    def chay(p):
        vao = json.dumps({"tool_name": "Write", "tool_input": {"file_path": p}})
        try:
            return subprocess.run([sys.executable, g], input=vao, text=True, capture_output=True,
                                  timeout=20).returncode
        except Exception:
            return -1
    chan = chay("X:/My Drive/KTC-Database/thu.txt")
    qua = chay("X:/du-an/30-Ket-Qua/thu.txt")
    if chan == 2 and qua == 0:
        print("  ✓ guard: HOẠT ĐỘNG (chặn ghi KTC-Database, 03-Templates, 04-Good-Documents)")
    else:
        print(f"  ✗ guard: CHƯA HOẠT ĐỘNG (tự thử: chặn={chan}, cho qua={qua}) — không coi là có bảo vệ ghi")


def kiem_phu_thuoc():
    """Bao phu thuoc NGOAI goi (tham dinh lan 1 M-01): co/khong, khong tu ket luan dat."""
    import sys
    print(f"  · Python {sys.version.split()[0]} ({sys.executable})")
    try:
        sys.path.insert(0, os.path.join(GOC, "scripts"))
        from duong_dan import ktc_database
        print(f"  ✓ KTC-Database: {ktc_database(canh_bao_ban_cu=False)}")
    except FileNotFoundError:
        print("  ✗ KTC-Database: không tìm thấy — skill trả CAN_BO_SUNG khi cần kho. Kho được chia sẻ qua Google Drive:"
              " thêm lối tắt “KTC-Database” vào Drive của tôi, hoặc đặt biến KTC_DATABASE_DIR trỏ tới thư mục kho")
    except Exception as e:
        print(f"  ✗ KTC-Database: không kiểm được ({e.__class__.__name__})")
    for mod in ("docx", "openpyxl"):
        try:
            __import__(mod)
            print(f"  ✓ thư viện {mod}")
        except Exception:
            print(f"  ✗ thư viện {mod} — phép đo thể thức/Excel sẽ ghi vào 'Kiểm tra chưa chạy'")


if __name__ == "__main__":
    main()
`````

## `scripts/ktc_the_thuc_hook.py` (4835 byte, sha256 `9ad0a5b2d6605f555b812143cba8c611becc7a31c7e96f06932b99350de0fe70`)

`````python
# -*- coding: utf-8 -*-
"""PostToolUse hook — tu do the thuc moi tep .docx/.xlsx vua sinh ra (DL-20260919-003).

Chay trong du an KTC (co 90-Nhat-Ky-Van-Hanh/) HOAC thu muc lam viec cua don vi (co KTC-THU-MUC-LAM-VIEC.json, 1.3.5).
Con goi y Muc 1-2 -> in stderr + ma thoat 2 de Claude thay va sua truoc khi giao.
Hook KHONG BAO GIO duoc lam hong phien: moi loi noi bo -> thoat 0 im lang.
"""
import json
import os
import sys
import time

GOC_PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BO_QUA = {".git", "node_modules", "__pycache__", "99-Luu-Tru", "92-Kinh-Nghiem", "31-Plugin", "10-Dau-Vao",
          "KTC-Database", "_trung_gian"}
MOI = 180          # giay — tep sua trong khoang nay coi la "vua sinh"
TOI_DA_MUC = 25000
TRANG_THAI = os.path.join(os.path.expanduser("~"), ".claude", "ktc_the_thuc_da_do.json")


def goc_du_an(cwd):
    # 1.3.5: nhan ca THU MUC LAM VIEC cua don vi (tep KTC-THU-MUC-LAM-VIEC.json, ktc_thu_muc.py) — tai khoan thanh vien
    # tren Cowork cung duoc do the thuc tu dong, khong chi du an.
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from ktc_thu_muc import tim_goc
        return tim_goc(cwd)[1]
    except Exception:
        pass
    p = os.path.abspath(cwd)
    for _ in range(6):
        if os.path.isdir(os.path.join(p, "90-Nhat-Ky-Van-Hanh")):
            return p
        cha = os.path.dirname(p)
        if cha == p:
            break
        p = cha
    return None


def tep_vua_sinh(goc):
    gio = time.time()
    dem = 0
    for r, ds, fs in os.walk(goc):
        ds[:] = [d for d in ds if d not in BO_QUA and not d.startswith(".")]
        if r[len(goc):].count(os.sep) >= 5:
            ds[:] = []
        for f in fs:
            dem += 1
            if dem > TOI_DA_MUC:
                return
            if f.lower().endswith((".docx", ".xlsx")) and not f.startswith("~$"):
                p = os.path.join(r, f)
                try:
                    if gio - os.path.getmtime(p) <= MOI:
                        yield p
                except OSError:
                    pass


def main():
    try:
        vao = json.load(sys.stdin)
    except Exception:
        return 0
    goc = goc_du_an(vao.get("cwd") or os.getcwd())
    if not goc:
        return 0
    ung_vien = set()
    fp = (vao.get("tool_input") or {}).get("file_path") or ""
    if fp.lower().endswith((".docx", ".xlsx")) and os.path.isfile(fp):
        ung_vien.add(os.path.abspath(fp))
    if vao.get("tool_name") in ("Bash", "PowerShell", "Skill", "Agent"):
        ung_vien.update(os.path.abspath(p) for p in tep_vua_sinh(goc))
    if not ung_vien:
        return 0

    try:
        da_do = json.load(open(TRANG_THAI, encoding="utf-8"))
    except Exception:
        da_do = {}
    sys.path.insert(0, os.path.join(GOC_PLUGIN, "skills", "the-thuc", "scripts"))
    import kiem_the_thuc as k  # noqa: E402

    bao = []
    for p in sorted(ung_vien):
        dau = f"{os.path.getmtime(p):.0f}"
        if da_do.get(p) == dau:
            continue
        try:
            kq = k.kiem_tep(p)
        except Exception:
            continue
        da_do[p] = dau
        nang = [x for x in kq if x[0] <= 2]
        if nang:
            bao.append((p, nang))
    try:
        json.dump(dict(list(da_do.items())[-500:]), open(TRANG_THAI, "w", encoding="utf-8"))
    except Exception:
        pass
    if not bao:
        return 0
    # Ghi bang chung cho agent ktc-tu-hoc (loi the thuc lap lai -> bai hoc) — DL-20260919-005
    try:
        import datetime as dt
        thu = os.path.join(goc, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
        with open(os.path.join(thu, dt.date.today().isoformat() + ".jsonl"), "a", encoding="utf-8") as f:
            for p, nang in bao:
                f.write(json.dumps({"t": dt.datetime.now().isoformat(timespec="seconds"),
                                    "phien": (vao.get("session_id") or "")[:8], "loai": "canh-bao-the-thuc",
                                    "tep": os.path.relpath(p, goc), "ma": sorted({x[1] for x in nang})},
                                   ensure_ascii=False) + "\n")
    except Exception:
        pass
    dong = ["KTC the-thuc: tệp vừa sinh CHƯA đạt chuẩn thể thức (20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md)."
            " Sửa rồi đo lại bằng kiem_the_thuc.py trước khi giao:"]
    for p, nang in bao:
        dong.append(f"- {os.path.relpath(p, goc)}")
        dong += [f"    [Mức {m}] {ma}: {mt}" for m, ma, mt in nang[:6]]
    sys.stderr.write("\n".join(dong) + "\n")
    return 2


if __name__ == "__main__":
    try:
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8")
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)
`````

## `scripts/ktc_thu_muc.py` (6714 byte, sha256 `898f75a78531a5783fcf20887c1ec49b2dec59da89f403bf3beb500b0b6db34f`)

`````python
# -*- coding: utf-8 -*-
"""Ket noi THU MUC LAM VIEC cua don vi (Cowork/Claude Code ngoai du an) — dau vao `10-Dau-Vao/`, ket qua `30-Ket-Qua/`.

Tai khoan thanh vien (phong, khoa) khong co thu muc du an KTC-Quan-tri. Tren Cowork, nguoi dung chon mot thu muc tren
may (hoac thu muc Google Drive dong bo) de cap quyen cho Claude; lenh `khoi-tao` tao trong do:
    KTC-THU-MUC-LAM-VIEC.json   tep danh dau (ma don vi, ngay tao) — skill, hook nhan ra thu muc nho tep nay
    10-Dau-Vao/                 tep can xu ly (bao cao, ke hoach cua don vi, van ban lien quan)
    30-Ket-Qua/<ngay>/<loai>/   san pham Bo cong cu xuat ra
    00-HUONG-DAN.md             cach dung, cach gui ve Phong TH-HC&QT
Khong ghi de tep da co; khong tao trong kho chuan (KTC-Database, 03-Templates, 04-Good-Documents) hay trong du an.

    python ktc_thu_muc.py khoi-tao <thu-muc> --ma P-TCCB
    python ktc_thu_muc.py kiem [<thu-muc>]        # in che do: du-an | don-vi | khong (tim tu thu muc len 6 cap)
"""
import argparse
import datetime as dt
import io
import json
import os
import re
import sys

DANH_DAU = "KTC-THU-MUC-LAM-VIEC.json"
MA_DON_VI = ("P-TCCB", "P-QLDT", "P-THHC", "P-QLKH", "P-TCKT", "K-KHCB", "K-SUPH", "K-KTNL", "K-KTCN", "K-YDUOC",
             "K-DTSHLX")
VUNG = re.compile(r"(?:^|[\\/])(?:KTC-Database|03-Templates\(1\)|04-Good-Documents)(?:[\\/]|$)", re.I)

HUONG_DAN = """# Thư mục làm việc KTC-Quan-tri — {ma}

Thư mục này được kết nối với Bộ công cụ KTC-Quan-tri (khởi tạo {ngay}). Tệp `{danh_dau}` là dấu nhận biết — không xóa.

| Thư mục | Dùng để |
|---|---|
| `10-Dau-Vao/` | Đặt tệp cần xử lý: kế hoạch, báo cáo của đơn vị, văn bản liên quan. Nên chia theo kỳ, ví dụ `10-Dau-Vao/2026-10/` |
| `30-Ket-Qua/<ngày>/<loại>/` | Bộ công cụ lưu sản phẩm, tên tệp chuẩn `<mã đơn vị>_<loại>_<kỳ>_v<N>` |

Cách dùng trên Claude Cowork: mở phiên, chọn thư mục này làm thư mục làm việc, rồi yêu cầu như bình thường (ví dụ
"lập báo cáo tháng 10 từ tệp trong 10-Dau-Vao/2026-10"). Bộ công cụ đọc `10-Dau-Vao/`, lưu kết quả vào `30-Ket-Qua/`.

Lưu ý:
- Bộ công cụ **không tự gửi** sản phẩm. Kiểm tra phiếu tự kiểm cuối câu trả lời; không còn lỗi thì **người dùng tự gửi**
  tệp về Phòng TH-HC&QT (`P-THHC`) theo kênh Trường quy định.
- Không đặt vào đây dữ liệu Thông báo số 924/TB-CĐKT không cho phép đưa lên nền tảng trí tuệ nhân tạo.
- Sửa văn bản đã có: Bộ công cụ tạo bản mới có Track Changes, không ghi đè tệp gốc trong `10-Dau-Vao/`.
"""


def tim_goc(thu_muc=None, cap=6):
    """(che_do, goc, ma_don_vi): 'du-an' (co 90-Nhat-Ky-Van-Hanh/), 'don-vi' (co tep danh dau) hoac ('khong', None, None)."""
    p = os.path.abspath(thu_muc or os.getcwd())
    for _ in range(cap):
        if os.path.isdir(os.path.join(p, "90-Nhat-Ky-Van-Hanh")):
            return "du-an", p, None
        f = os.path.join(p, DANH_DAU)
        if os.path.isfile(f):
            try:
                ma = json.load(io.open(f, encoding="utf-8")).get("ma_don_vi")
            except Exception:
                ma = None
            return "don-vi", p, ma
        cha = os.path.dirname(p)
        if cha == p:
            break
        p = cha
    return "khong", None, None


def khoi_tao(thu_muc, ma):
    ma = (ma or "").strip().upper()
    if ma not in MA_DON_VI:
        raise ValueError(f"Mã đơn vị '{ma}' không có trong bảng 11 mã chuẩn: {', '.join(MA_DON_VI)} — hỏi người dùng.")
    goc = os.path.abspath(thu_muc)
    if VUNG.search(goc.replace("\\", "/")):
        raise ValueError("Không khởi tạo trong kho chuẩn (KTC-Database, 03-Templates(1), 04-Good-Documents) — chọn thư mục khác.")
    if not os.path.isdir(goc):
        raise ValueError(f"Không thấy thư mục {goc} — chọn thư mục đã cấp quyền cho Claude.")
    che_do, g, ma_cu = tim_goc(goc)
    if che_do == "du-an":
        raise ValueError(f"{goc} nằm trong dự án KTC-Quan-tri ({g}) — dự án đã có 10-Dau-Vao/, 30-Ket-Qua/, không cần khởi tạo.")
    if che_do == "don-vi" and os.path.normcase(g) != os.path.normcase(goc):
        raise ValueError(f"{goc} nằm trong thư mục làm việc đã kết nối {g} (đơn vị {ma_cu}) — dùng thư mục đó.")
    tao = []
    for d in ("10-Dau-Vao", "30-Ket-Qua"):
        p = os.path.join(goc, d)
        if not os.path.isdir(p):
            os.makedirs(p)
            tao.append(d + "/")
    ngay = dt.date.today().strftime("%d/%m/%Y")
    f = os.path.join(goc, DANH_DAU)
    if os.path.isfile(f):
        if ma_cu and ma_cu != ma:
            raise ValueError(f"Thư mục đã kết nối cho đơn vị {ma_cu}, khác {ma} — không ghi đè; hỏi người dùng.")
    else:
        io.open(f, "w", encoding="utf-8").write(json.dumps(
            {"ma_don_vi": ma, "tao_ngay": dt.date.today().isoformat(), "ban_mau": 1,
             "dau_vao": "10-Dau-Vao", "ket_qua": "30-Ket-Qua"}, ensure_ascii=False, indent=2) + "\n")
        tao.append(DANH_DAU)
    hd = os.path.join(goc, "00-HUONG-DAN.md")
    if not os.path.isfile(hd):
        io.open(hd, "w", encoding="utf-8").write(HUONG_DAN.format(ma=ma, ngay=ngay, danh_dau=DANH_DAU))
        tao.append("00-HUONG-DAN.md")
    return goc, tao


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="lenh", required=True)
    a1 = sub.add_parser("khoi-tao")
    a1.add_argument("thu_muc")
    a1.add_argument("--ma", required=True)
    a2 = sub.add_parser("kiem")
    a2.add_argument("thu_muc", nargs="?")
    a = ap.parse_args(argv)
    if a.lenh == "khoi-tao":
        try:
            goc, tao = khoi_tao(a.thu_muc, a.ma)
        except ValueError as e:
            print("✗ " + str(e))
            return 2
        print(f"✓ Đã kết nối thư mục làm việc: {goc}")
        print("  tạo mới: " + (", ".join(tao) if tao else "không (đã có đủ)"))
        print("  đầu vào: 10-Dau-Vao/ · kết quả: 30-Ket-Qua/<ngày>/<loại>/ · hướng dẫn: 00-HUONG-DAN.md")
        return 0
    che_do, goc, ma = tim_goc(a.thu_muc)
    print(json.dumps({"che_do": che_do, "goc": goc, "ma_don_vi": ma,
                      "dau_vao": os.path.join(goc, "10-Dau-Vao") if goc else None,
                      "ket_qua": os.path.join(goc, "30-Ket-Qua") if goc else None}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/ktc_trackchanges.py` (21321 byte, sha256 `70b46db89670596a19c1b3100def96cbab2cbf399858f85faedefd5881eb4f56`)

`````python
# -*- coding: utf-8 -*-
"""KTC Track Changes — sua .docx co dau vet va xuat nhat ky sua doi.

Kich hoat: nguoi dung noi "Track Changes" HOAC "ghi nhat ky sua doi".

Can cu:
  - KTC-Quan-tri/20-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md (NT-2)
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
`````

## `scripts/tra_hieu_luc.py` (13278 byte, sha256 `1784955be6a6805da2b712b5529ef6f6ddbc9f5b4ec4caa1c80759a337256fe0`)

`````python
# -*- coding: utf-8 -*-
"""Quet hieu luc phap ly cua van ban DUOC VIEN DAN — DL-20260919-004.

Cho mot du thao/san pham (.docx/.md/.txt) hoac ca thu muc quy tac (.md):
  1. Trich moi van ban duoc vien dan (Luat, Nghi dinh, Thong tu, Quyet dinh, Thong bao, Ke hoach, VBHN...).
  2. Tra trong KTC-Database kho 01-02 (chi duyet TEN tep — khong tai ca kho tren Drive; chi doc metadata
     cua tep khop): co trong kho khong, tep nao, metadata ghi tinh trang gi.
  3. Doi chieu chuoi van ban Truong DA BI THAY THE (kiem_vien_dan.DA_THAY) va VBHN dang co trong kho.
  4. Chay kiem_vien_dan (VD01-VD12) cho cach ghi vien dan.

KET LUAN "het hieu luc" KHONG duoc rut tu cong cu nay mot minh: cong cu chi phan loai
  THAY_THE (co trong chuoi da biet) · KHO_GHI_HET_HIEU_LUC (metadata kho) · CO_TRONG_KHO (+ tinh trang metadata) · KHONG_CO_TRONG_KHO → CAN XAC MINH.
Viec xac minh ngoai (Internet, nguon chinh thong) do agent ktc-hieu-luc-vien-dan lam va ghi nguon.

Chay:  python 29-Cong-Cu/tra_hieu_luc.py <tep|thu muc> [...] [--md <bao cao .md>]
Ma thoat: 1 neu co van ban THAY_THE hoac goi y Muc 1 cua kiem_vien_dan; nguoc lai 0.
"""
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kiem_vien_dan as kvd  # noqa: E402

KHO_CON = ("01-Legal-Database", "02-KTC-Regulations")
KHOA_TINH_TRANG = re.compile(r"(tình trạng|trạng thái hiệu lực|trạng thái|hiệu lực|tinh_trang|trang_thai|hieu_luc|status)"
                             r"[^:\n]{0,25}:\s*(.+)", re.I)

# Ma loai van ban -> tu viet tat trong so hieu
LOAI = r"(Luật|Bộ luật|Pháp lệnh|Nghị quyết|Nghị định|Thông tư liên tịch|Thông tư|Quyết định|Chỉ thị|Thông báo|Kế hoạch|Công văn|Hướng dẫn|Quy định|Kết luận|Văn bản hợp nhất)"
# So hieu hanh chinh "30/2020/NĐ-CP", "1976/QĐ-CĐKT" va so hieu van ban Dang "366-QĐ/TW", "43-HD/BTCTW",
# "198-KL/TW" (dau gach ngang sau so — HD 05-HD/VPTW; bo sot khi quet mau cam ket TB 1052, 19/9/2026)
SO = r"(\d{1,5}[a-z]?(?:/\d{4})?/[A-ZĐa-zđ0-9\-]+(?:/[A-ZĐa-zđ0-9\-]+)?|\d{1,5}-[A-ZĐ]{1,5}/[A-ZĐ]{2,8})"
RE_SO = re.compile(LOAI + r"\s+(?:số\s+)?" + SO)
# Viet tat hay gap trong van ban noi bo: "QĐ 988/QĐ-CĐKT", "NĐ 30/2020/NĐ-CP", "TB 597/TB-CĐKT"
VIET_TAT = {"QĐ": "Quyết định", "NĐ": "Nghị định", "TT": "Thông tư", "TB": "Thông báo", "NQ": "Nghị quyết",
            "KH": "Kế hoạch", "CV": "Công văn", "CT": "Chỉ thị", "HD": "Hướng dẫn", "PL": "Pháp lệnh"}
RE_VIET_TAT = re.compile(r"\b(QĐ|NĐ|TT|TB|NQ|KH|CV|CT|HD|PL)\s+(?:số\s+)?" + SO)
RE_LUAT_TEN = re.compile(r"\b(Bộ luật|Luật)\s+((?:[A-ZĐ][\wÀ-ỹ]*|và|,)(?:\s+(?:[a-zà-ỹđ]+|[A-ZĐ][\wÀ-ỹ]*|và|,)){0,12}?)"
                         r"(?=\s+(?:ngày|số|năm|\(|;|\.|,\s*được|đã|$))")


TU_LOAI = {
    "Nghị định": ("ND", "NGHI-DINH"), "Thông tư": ("TT", "THONG-TU"), "Thông tư liên tịch": ("TTLT", "THONG-TU"),
    "Quyết định": ("QD", "QUYET-DINH"), "Nghị quyết": ("NQ", "NGHI-QUYET"), "Luật": ("LUAT", "QH"),
    "Bộ luật": ("LUAT",), "Pháp lệnh": ("PL", "PHAP-LENH", "UBTVQH"), "Thông báo": ("TB", "THONG-BAO"),
    "Kế hoạch": ("KH", "KE-HOACH"), "Công văn": ("CV", "CONG-VAN"), "Chỉ thị": ("CT", "CHI-THI"),
    "Hướng dẫn": ("HD", "HUONG-DAN"), "Quy định": ("QD", "QUY-DINH"), "Kết luận": ("KL", "KET-LUAN"), "Văn bản hợp nhất": ("VBHN",),
}


def khong_dau(s):
    s = unicodedata.normalize("NFD", s.replace("Đ", "D").replace("đ", "d"))
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def chuan_hoa(s):
    return re.sub(r"[^A-Z0-9]+", "-", khong_dau(s).upper()).strip("-")


def trich(doan):
    """Tra ve list[dict(loai, so, ten, dong, ngu_canh)] — khong trung lap theo (loai, so|ten)."""
    kq, da = [], set()
    for i, s in enumerate(doan):
        for m in RE_SO.finditer(s):
            loai, so = m.group(1), m.group(2).rstrip(".,;)")
            if "/" not in so:
                continue
            khoa = (loai, so)
            if khoa not in da:
                da.add(khoa)
                kq.append({"loai": loai, "so": so, "ten": None, "dong": i + 1, "ngu_canh": s.strip()[:120]})
        for m in RE_VIET_TAT.finditer(s):
            loai, so = VIET_TAT[m.group(1)], m.group(2).rstrip(".,;)")
            if "/" in so and (loai, so) not in da:
                da.add((loai, so))
                kq.append({"loai": loai, "so": so, "ten": None, "dong": i + 1, "ngu_canh": s.strip()[:120]})
        for m in RE_LUAT_TEN.finditer(s):
            ten = m.group(2).strip(" ,")
            if len(ten) < 4 or re.match(r"(số|sửa đổi, bổ sung)\b", ten):
                continue
            khoa = (m.group(1), ten)
            if khoa not in da:
                da.add(khoa)
                kq.append({"loai": m.group(1), "so": None, "ten": ten, "dong": i + 1, "ngu_canh": s.strip()[:120]})
    return kq


class Kho:
    """Chi muc TEN tep cua kho 01-02 (khong doc noi dung)."""

    def __init__(self, goc):
        self.goc = goc
        self.tep = []
        for con in KHO_CON:
            for r, ds, fs in os.walk(os.path.join(goc, con)):
                for f in fs:
                    if f != "desktop.ini" and not f.endswith((".gdoc", ".gsheet")):
                        self.tep.append((os.path.join(r, f), chuan_hoa(f)))

    def tim(self, vb):
        if vb["so"]:
            phan = [p for p in re.split(r"[/\-]", chuan_hoa(vb["so"])) if p]
            so, nam = phan[0], next((p for p in phan[1:] if re.fullmatch(r"(19|20)\d\d", p)), None)
            ma_day_du = "".join(p for p in phan[1:] if not re.fullmatch(r"(19|20)\d\d", p))  # vd TTBXD, QDCDKT
            tu_loai = TU_LOAI.get(vb["loai"], ())

            def khop(t):
                # So va nam phai DUNG LIEN NHAU ("85-2025"): tranh khop "275-2025 sua doi ND 85"
                if nam:
                    if not re.search(rf"(?<![0-9]){so}-{nam}(?![0-9])|(?<![0-9]){nam}-{so}(?![0-9])", t):
                        return False
                elif not re.search(rf"(?<![0-9]){so}(?![0-9])", t):
                    return False
                tok = set(t.split("-"))
                phang = t.replace("-", "")
                # Loai van ban phai khop: ma day du (TT-BXD) hoac tu loai la TU NGUYEN VEN (khong khop "TT" trong "TTG")
                if ma_day_du and ma_day_du in phang:
                    return True
                return any((w in tok) if "-" not in w else (w in t) for w in tu_loai)
        else:
            # Khop NGUYEN CUM "LUAT-<TEN>" — tranh "Luat Giao duc" khop "Luat Pho bien giao duc phap luat" (19/9/2026).
            # Uu tien cum dung tron (sau la so/VBHN/het ten) de khong khop "Luat Giao duc nghe nghiep".
            cum = "LUAT-" + chuan_hoa(vb["ten"])
            tron = [p for p, t in self.tep if re.search(rf"(?:^|-){re.escape(cum)}(?=-(?:\d|VBHN|SO|QH|V\d)|$)", t)]
            if tron:
                return tron
            return [p for p, t in self.tep if re.search(rf"(?:^|-){re.escape(cum)}(?:-|$)", t)]
        return [p for p, t in self.tep if khop(t)]

    @staticmethod
    def tinh_trang(p):
        """Doc metadata canh tep (neu co): dong 'Tinh trang/Hieu luc/Trang thai'."""
        goc, _ = os.path.splitext(p)
        ung = [goc + ".metadata.md", goc + ".metadata.yaml", p + ".metadata.md"]
        thu = os.path.dirname(p)
        ten = os.path.basename(goc)
        ung += [os.path.join(thu, f) for f in os.listdir(thu)
                if f.lower().startswith("metadata") and chuan_hoa(ten)[:18] in chuan_hoa(f)]
        for m in ung:
            if os.path.isfile(m):
                try:
                    for dong in open(m, encoding="utf-8", errors="ignore"):
                        k = KHOA_TINH_TRANG.search(dong)
                        if k:
                            return k.group(2).strip()[:90]
                except OSError:
                    pass
        return None


def phan_loai(vb, kho, vbhn_co):
    ghi = []
    so = vb["so"] or ""
    for mau, cu, moi in kvd.DA_THAY:
        if so and re.search(mau, so if so.startswith(" ") else " " + so):
            return "THAY_THE", [], f"{cu} đã bị thay thế bởi {moi} — hợp lệ chỉ khi văn bản đang xét ban hành trước ngày thay thế"
    tep = kho.tim(vb) if kho else []
    if vb["ten"] and vb["ten"] in vbhn_co:
        ghi.append(f"có VBHN {vbhn_co[vb['ten']]} — lấy số điều theo VBHN; VBHC không ghi số hiệu Luật")
    if not tep:
        return "KHONG_CO_TRONG_KHO", [], "; ".join(ghi + ["CẦN XÁC MINH hiệu lực từ nguồn chính thống, ghi nguồn + ngày tra"])
    tt = next((t for t in (Kho.tinh_trang(p) for p in tep[:4]) if t), None)
    if tt and re.search(r"hết hiệu lực|bị thay thế|bãi bỏ|không còn", tt, re.I):
        return "KHO_GHI_HET_HIEU_LUC", tep, f"metadata kho ghi: {tt} — đối chiếu ngày hiệu lực với ngày ban hành văn bản đang xét"
    ghi.append(f"metadata: {tt}" if tt else "metadata không ghi tình trạng — đọc phần hiệu lực của văn bản")
    return "CO_TRONG_KHO", tep, "; ".join(ghi)


def vbhn_trong_quy_tac():
    """Doc bang VBHN tu 17-Quy-Tac-Vien-Dan.md: ten luat -> so VBHN."""
    goc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Du an: 20-Chuan-Chung/; plugin: skills/*/references/(Skill-Library/)
    import glob
    ung = [os.path.join(goc, "20-Chuan-Chung", "17-Quy-Tac-Vien-Dan.md")] + \
        glob.glob(os.path.join(goc, "skills", "*", "references", "**", "17-Quy-Tac-Vien-Dan.md"), recursive=True)
    p = next((x for x in ung if os.path.isfile(x)), "")
    kq = {}
    if os.path.isfile(p):
        for d in open(p, encoding="utf-8"):
            m = re.match(r"\|\s*(?:Bộ luật|Luật)\s+(.+?)\s+số\s+\S+\s*\|\s*(\d+/VBHN-\S+)", d)
            if m:
                kq[m.group(1).strip()] = m.group(2)
    return kq


def quet(duong_dan_list, goc_kho=None):
    tep = []
    for p in duong_dan_list:
        if os.path.isdir(p):
            for r, ds, fs in os.walk(p):
                ds[:] = [d for d in ds if d not in (".git", "__pycache__", "99-Luu-Tru")]
                tep += [os.path.join(r, f) for f in fs if f.endswith((".md", ".docx"))]
        else:
            tep.append(p)
    if goc_kho is None:
        try:
            import duong_dan
            goc_kho = duong_dan.ktc_database(canh_bao_ban_cu=False)
        except Exception:
            goc_kho = None
    kho = Kho(goc_kho) if goc_kho else None
    vbhn = vbhn_trong_quy_tac()
    ket_qua = []
    for p in tep:
        doan = kvd.doc_tep(p)
        # kiem_vien_dan chay cho MOI dinh dang: doc_tep() tra ve danh sach doan van nhu nhau
        # cho .docx lan .md/.txt. Truoc day chi chay voi .docx nen quet mot tep .md bo QUA TOAN BO
        # phan kiem vien dan — khong bao gi, va ma thoat cung sai vi Muc 1 khong duoc dem.
        # Phat hien khi van hanh thu 21/9/2026: cung mot du thao, quet .md ra 0 goi y con chay
        # kiem_vien_dan truc tiep ra 4 (2 Muc 1). Quet dinh ky quy tac/skill deu la .md.
        vd = kvd.kiem_tra(doan)
        dong = [(vb, *phan_loai(vb, kho, vbhn)) for vb in trich(doan)]
        ket_qua.append((p, dong, vd))
    return ket_qua, goc_kho


def in_bao_cao(ket_qua, goc_kho, file=sys.stdout):
    w = lambda s="": print(s, file=file)  # noqa: E731
    w(f"# Quét hiệu lực và viện dẫn — {len(ket_qua)} tệp")
    w(f"Kho đối chiếu: `{goc_kho or 'KHÔNG ĐỌC ĐƯỢC — mọi văn bản là CẦN XÁC MINH'}` (kho 01, 02; tra theo tên tệp)")
    for p, dong, vd in ket_qua:
        if not dong and not vd:
            continue
        w(f"\n## {p}")
        if dong:
            w("\n| Văn bản viện dẫn | Dòng | Phân loại | Tệp trong kho | Ghi chú |")
            w("|---|---|---|---|---|")
            for vb, loai, tep, ghi in sorted(dong, key=lambda x: ("THAY_THE", "KHO_GHI_HET_HIEU_LUC", "KHONG_CO_TRONG_KHO", "CO_TRONG_KHO").index(x[1])):
                ten = f"{vb['loai']} {vb['so'] or vb['ten']}"
                t = os.path.basename(tep[0]) if tep else "—"
                w(f"| {ten} | {vb['dong']} | **{loai}** | {t} | {ghi} |")
        if vd:
            w("\nCách ghi viện dẫn (kiem_vien_dan):")
            for muc, ma, d, trich_, mo_ta in vd:
                w(f"- [Mức {muc}] {ma} dòng {d}: {mo_ta}")


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    ra_md = None
    if "--md" in argv:
        i = argv.index("--md")
        ra_md = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    ket_qua, goc = quet(argv)
    in_bao_cao(ket_qua, goc)
    if ra_md:
        os.makedirs(os.path.dirname(os.path.abspath(ra_md)), exist_ok=True)
        with open(ra_md, "w", encoding="utf-8") as f:
            in_bao_cao(ket_qua, goc, f)
    xau = any(x[1] in ("THAY_THE", "KHO_GHI_HET_HIEU_LUC") for _, dong, _ in ket_qua for x in dong) or \
        any(v[0] == 1 for _, _, vd in ket_qua for v in vd)
    return 1 if xau else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/trich_tuong_thuat.py` (7814 byte, sha256 `d79e86224ef4a4c980fb51cd7a799f57b287b2a68e82d46e53e0030d3aa422fb`)

`````python
# -*- coding: utf-8 -*-
"""Trich bao cao TUONG THUAT (Phu luc IIa) cua 13 don vi -> narrative.json

Khac lan chay truoc: lan truoc chi doc .xlsx (Phu luc IIb - bang nhiem vu),
bo sot hoan toan 13 file .docx chua VAN TUONG THUAT da chia san theo 6 Truc.
"""
import glob, json, os, re, sys
from docx import Document

# Goc du an suy ra tu vi tri tep nay — khong ghi cung duong dan tuyet doi,
# de doi cho du an la khong phai sua tung tool.
DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IN = os.path.join(DU_AN, "10-Dau-Vao", "01-Dau-Moi-Nop", "2026-09")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "_trung_gian", "narrative.json")

TRUC = [
    (1, r"Thực hiện mục tiêu phát triển kinh tế"),
    (2, r"Hoàn thiện thể chế"),
    (3, r"(Thúc đẩy phát triển|Phát triển)\s+(KH|khoa học)"),
    (4, r"Xây dựng Đảng"),
    (5, r"Phát triển văn hóa, con người"),
    (6, r"Củng cố quốc phòng"),
]
M_KQ = re.compile(r"^(Phần\s+I\b|I\.\s*(THỰC HIỆN|TÌNH HÌNH|KẾT QUẢ))", re.I)
M_DG = re.compile(r"^(II|III)\.\s*ĐÁNH GIÁ CHUNG", re.I)
M_KH = re.compile(r"^(Phần\s+II\b|I\.\s*KẾ HOẠCH|III\.\s*NHIỆM VỤ|II\.\s*NHIỆM VỤ)", re.I)
M_NQ = re.compile(r"Nghị quyết\s+số\s+(\d+)\s*-?\s*NQ/TW", re.I)
M_DAT = re.compile(r"^\d\.\s*Kết quả đạt được", re.I)
M_CHUA = re.compile(r"^\d\.\s*(Danh mục các công việc chưa hoàn thành|Các tồn tại, hạn chế|Tồn tại, hạn chế)", re.I)
M_HEAD = re.compile(r"^(Phần\s+[IVX]+|[IVX]+\.\s|\d+\.\s|\d+\.\d+\.?\s|[a-hk]\)\s|\*)")
M_LV = re.compile(r"^[a-hk]\)\s*(.+)$")

# Linh vuc -> nhan cap Truong (BC-375 dung dang "* Cong tac X:")
LINH_VUC = [
    ("Công tác tuyển sinh", r"tuyển sinh|nhập học|trúng tuyển|xét tuyển|hướng nghiệp"),
    ("Công tác đào tạo", r"đào tạo|giảng dạy|thời khóa biểu|tốt nghiệp|mở lớp|liên thông|thực tập|năm học"),
    ("Công tác chương trình, giáo trình", r"chương trình đào tạo|giáo trình|đề cương|chuẩn đầu ra"),
    ("Công tác khảo thí", r"khảo thí|thi kết thúc|ngân hàng đề|chấm thi|nhập điểm|thi lại|văn bằng|chứng chỉ"),
    ("Công tác bảo đảm chất lượng", r"bảo đảm chất lượng|kiểm định|tự đánh giá|chuẩn cơ sở"),
    ("Công tác tổ chức, cán bộ", r"tổ chức cán bộ|bổ nhiệm|tuyển dụng|vị trí việc làm|biên chế|nâng lương|thi đua|khen thưởng|kỷ luật|đánh giá xếp loại"),
    ("Công tác kế hoạch, tổng hợp", r"tổng hợp|kế hoạch công tác|văn thư|lưu trữ|hành chính|báo cáo định kỳ|quy chế làm việc"),
    ("Công tác khoa học, công nghệ và chuyển đổi số", r"khoa học|công nghệ|nghiên cứu|sáng kiến|chuyển đổi số|phần mềm|trí tuệ nhân tạo|AI|dữ liệu|hội thảo"),
    ("Công tác xây dựng Đảng", r"Đảng ủy|chi bộ|đảng viên|nghị quyết Hội nghị|sinh hoạt chính trị"),
    ("Công tác phòng, chống tham nhũng, tiêu cực", r"tham nhũng|tiêu cực|lãng phí|kê khai tài sản"),
    ("Công tác Công đoàn, Đoàn Thanh niên", r"Công đoàn|Đoàn Thanh niên|Đoàn viên|Hội Sinh viên|thanh niên"),
    ("Công tác quản lý cơ sở vật chất", r"cơ sở vật chất|sửa chữa|xây dựng công trình|thiết bị|tài sản|khuôn viên|ký túc xá"),
    ("Công tác tài chính", r"tài chính|kế toán|thanh toán|dự toán|quyết toán|học phí|lương|chế độ|định mức kinh tế|tự chủ"),
    ("Công tác học sinh, sinh viên", r"học sinh, sinh viên|HSSV|sĩ số|chủ nhiệm|nội trú|học bổng|an sinh"),
    ("Công tác truyền thông", r"truyền thông|tin, bài|website|fanpage|video|infographic|banner"),
    ("Công tác quốc phòng, an ninh", r"quốc phòng|an ninh|trật tự|bí mật nhà nước|phòng cháy|an toàn"),
    ("Công tác đối ngoại, hợp tác phát triển", r"đối ngoại|hợp tác|doanh nghiệp|quốc tế|Lào|MOU|liên kết"),
]


def linh_vuc(s: str, mac_dinh="Công tác khác") -> str:
    for ten, pat in LINH_VUC:
        if re.search(pat, s, re.I):
            return ten
    return mac_dinh


def doc_mot(path: str) -> dict:
    doc = Document(path)
    kq = {i: [] for i in range(1, 7)}
    kh = {i: [] for i in range(1, 7)}
    nq_kq, nq_kh = {}, {}
    dat, chua = [], []
    pha, truc, nq_hien, muc_dg = "KQ", None, None, None
    dem_truc = {}
    lv_hien = None

    for p in doc.paragraphs:
        t = " ".join(p.text.split())
        if not t:
            continue

        if M_KQ.match(t):
            pha, truc, nq_hien, muc_dg, lv_hien = "KQ", None, None, None, None; continue
        if M_DG.match(t):
            pha, truc, nq_hien, lv_hien = "DG", None, None, None; continue
        if M_KH.match(t):
            pha, truc, nq_hien, muc_dg, lv_hien = "KH", None, None, None, None; continue

        if pha == "DG":
            if M_DAT.match(t):   muc_dg = "dat";  continue
            if M_CHUA.match(t):  muc_dg = "chua"; continue
            if M_HEAD.match(t):  muc_dg = None;   continue
            noi = re.sub(r"^[-+•*]\s*", "", t)
            if muc_dg == "dat" and len(noi) > 15:  dat.append(noi)
            if muc_dg == "chua" and len(noi) > 15 and noi.lower() != "không": chua.append(noi)
            continue

        # Tieu de Truc
        gap = False
        for so, pat in TRUC:
            if re.search(pat, t, re.I) and M_HEAD.match(t):
                dem_truc[so] = dem_truc.get(so, 0) + 1
                if dem_truc[so] >= 2 and pha == "KQ":
                    pha = "KH"          # du phong khi thieu moc "Phan II"
                truc, nq_hien, lv_hien = so, None, None
                gap = True
                break
        if gap:
            continue

        m = M_NQ.search(t)
        if m and M_HEAD.match(t):
            nq_hien, truc, lv_hien = m.group(1), None, None
            continue

        m = M_LV.match(t)
        if m:
            lv_hien = m.group(1).strip().rstrip(":")
            continue

        if M_HEAD.match(t) and not t.startswith(("-", "+")):
            if re.match(r"^\d+\.\s", t) and not re.match(r"^\d+\.\d", t):
                truc, nq_hien, lv_hien = None, None, None
            continue

        noi = re.sub(r"^[-+•*]\s*", "", t).strip()
        if len(noi) < 15 or noi.lower().startswith(("không", "kính", "trên đây")):
            continue

        if nq_hien:
            (nq_kq if pha == "KQ" else nq_kh).setdefault(nq_hien, []).append(noi)
        elif truc:
            (kq if pha == "KQ" else kh)[truc].append(
                {"lv": lv_hien or linh_vuc(noi), "noi_dung": noi})

    return {"kq": kq, "kh": kh, "nq_kq": nq_kq, "nq_kh": nq_kh,
            "dat": dat, "chua": chua}


def main():
    data = {}
    for f in sorted(glob.glob(os.path.join(IN, "*", "*.docx"))):
        don_vi = os.path.basename(os.path.dirname(f))
        r = doc_mot(f)
        r["file"] = os.path.basename(f)
        data[don_vi] = r
        nkq = sum(len(v) for v in r["kq"].values())
        nkh = sum(len(v) for v in r["kh"].values())
        print(f"{don_vi:22s} KQ={nkq:3d} KH={nkh:3d} NQ={len(r['nq_kq'])+len(r['nq_kh']):2d} "
              f"dat={len(r['dat'])} chua={len(r['chua'])}")
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tk = sum(sum(len(v) for v in d["kq"].values()) for d in data.values())
    th = sum(sum(len(v) for v in d["kh"].values()) for d in data.values())
    print(f"\nTONG: {len(data)} don vi | {tk} y ket qua | {th} y ke hoach -> {OUT}")


if __name__ == "__main__":
    main()
`````

## `scripts/validate_plan.py` (11318 byte, sha256 `1e8245e7a2feedf44e03432f20405060bdcd357081d6bf0b3f6ad71838816999`)

`````python
# -*- coding: utf-8 -*-
"""Kiem ke hoach KPI ca nhan (tep .xlsx dung 1 trong 6 mau Quy) — skill ktc-kpi-lap-ke-hoach.

Moi loi co: ma, muc (LOI = phai sua truoc khi trinh Truong don vi phe duyet; CANH_BAO = can xem), vi tri, can cu.
KHONG sua tep. KHONG ket luan thay Truong don vi (phe duyet — QD 1923 D13.1).

  KH01 LOI       Dau viec thieu san pham dau ra                          QD 1923 D12.4
  KH02 LOI       Dau viec thieu thoi han hoan thanh                      QD 1923 D12.4
  KH03 LOI       So luong trong / khong phai so > 0 (khong do luong duoc) QD 1923 D12.4
  KH04 LOI       Thieu muc do / he so quy doi                            QD 1923 PL II
  KH05 LOI       He so khong khop muc do (chi khi phuong an muc-do)      QD 1923 PL II
  KH06 LOI       Dong vi du cua mau chua xoa                             Known-Issues-Bieu-Mau #4
  KH07 CANH_BAO  Thieu nguon minh chung                                  QD 1923 D12.4
  KH08 LOI       San pham khong co trong Danh muc QD 2119 (phuong an A/AxB) QD 2119/QD-CDKT
  KH09 CANH_BAO  Dau hieu quy ket qua tap the thanh KPI ca nhan          QD 1923 D4.8
  KH10 LOI       Vien chuc quan ly khong co dau viec Truc (4)            QD 1923 D12.1
  KH11 CANH_BAO  Truc co diem toi da nhung khong co dau viec             mau Danh gia: diem Truc = 0
  KH12 LOI       Cau truc diem cua mau sai (70 diem, truc chinh >= 40%, nhom chung) QD 1923 D10.4, D11.3, D12.3
  KH13 CANH_BAO  O so Quyet dinh trong tieu de sheet KPI con trong       Known-Issues-Bieu-Mau #5
  KH14 CANH_BAO  Dau viec trung lap noi dung                              QD 1923 D11.4a
  KH15 LOI       Chua dien ho ten / don vi                                mau Ke hoach
  KH16 CANH_BAO  Sheet KPI con so thuc te VI DU cua mau (L=4,N=100,P=100) Known-Issues-Bieu-Mau #12
  KH17 CANH_BAO  Sheet KPI thieu nguoi phoi hop (cot co trong mau)          lenh sua 25/9/2026
  KH18 LOI       Sheet KPI o san pham (F) trong / khong tro dong co viec    lenh sua 25/9/2026
  KH19 CANH_BAO  Dong can cao > 409 pt — Excel khong hien het            gioi han Excel

Chay:  python 29-Cong-Cu/validate_plan.py <ke_hoach.xlsx> [--nhom hanh-chinh] [--phuong-an muc-do] [--json]
Ma thoat: 1 neu co LOI, 0 neu chi canh bao hoac sach.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kpi_calc as kc  # noqa: E402
import kpi_mau as km   # noqa: E402

TAP_THE = ("toàn trường", "toàn khoa", "toàn phòng", "toàn đơn vị", "100% viên chức", "tất cả viên chức",
           "kết quả chung của", "tập thể đơn vị")


def kiem(p, nhom=None, phuong_an=None):
    wb = km.mo(p)
    ct = km.cau_truc(wb)
    nhom = nhom or km.nhan_nhom(wb)
    ws, kp = wb["Ke Hoach"], wb["KPI"]
    ds = []

    def them(ma, muc, vt, nd, cc):
        ds.append({"ma": ma, "muc": muc, "vi_tri": vt, "noi_dung": nd, "can_cu": cc})

    # Cau truc diem cua mau
    for ma, nd, cc in (kc.kiem_trong_so_truc(ct["diem_truc"], max(ct["diem_truc"], key=ct["diem_truc"].get))
                       + kc.kiem_tieu_chi_chung(ct["nhom_a"])):
        them("KH12", "LOI", "Danh gia", f"{ma}: {nd}", cc)
    # Thong tin ca nhan
    for r, ten in ((4, "Họ và tên"), (8, "Đơn vị công tác")):
        v = str(ws[f"B{r}"].value or "")
        if not re.search(r":\s*[^\s….]", v.split("Ngày sinh")[0]):
            them("KH15", "LOI", f"Ke Hoach!B{r}", f"Chưa điền {ten}", "mẫu Kế hoạch")
    vi_du = km.dong_vi_du(nhom) if nhom else {}
    thay_noi_dung, co_truc = {}, {n: 0 for n in ct["truc"]}
    for n, (d, c) in ct["truc"].items():
        for r in range(d, c + 1):
            o = {col: ws[f"{col}{r}"].value for col in "BCDEFGHIJ"}
            if not any(v not in (None, "") for v in o.values()):
                continue
            vt = f"Ke Hoach!dòng {r} (Trục {n})"
            nd = str(o["B"] or "").strip()
            for col, v in o.items():
                if vi_du.get(f"{col}{r}") is not None and v == vi_du[f"{col}{r}"]:
                    them("KH06", "LOI", vt, f"Dòng ví dụ của mẫu chưa xóa: '{str(v)[:60]}'",
                         "Known-Issues-Bieu-Mau #4")
                    break
            if not nd:
                them("KH01", "LOI", vt, "Có số liệu nhưng thiếu nội dung nhiệm vụ", "QĐ 1923, Đ12.4")
                continue
            co_truc[n] += 1
            if nd.lower() in thay_noi_dung:
                them("KH14", "CANH_BAO", vt, f"Trùng nội dung với {thay_noi_dung[nd.lower()]}", "QĐ 1923, Đ11.4a")
            thay_noi_dung.setdefault(nd.lower(), vt)
            if not str(o["E"] or "").strip():
                them("KH01", "LOI", vt, f"'{nd[:50]}': thiếu sản phẩm đầu ra", "QĐ 1923, Đ12.4")
            if o["G"] in (None, ""):
                them("KH02", "LOI", vt, f"'{nd[:50]}': thiếu thời hạn hoàn thành", "QĐ 1923, Đ12.4")
            try:
                ok = float(o["F"]) > 0
            except (TypeError, ValueError):
                ok = False
            if not ok:
                them("KH03", "LOI", vt, f"'{nd[:50]}': số lượng '{o['F']}' không đo lường được", "QĐ 1923, Đ12.4")
            if o["D"] in (None, "") or o["I"] in (None, ""):
                them("KH04", "LOI", vt, f"'{nd[:50]}': thiếu mức độ hoặc hệ số quy đổi", "QĐ 1923, Phụ lục II")
            elif phuong_an == "muc-do":
                k = kc.muc_do_tu_chu(o["D"])
                if k is None:
                    them("KH04", "LOI", vt, f"Mức độ '{o['D']}' không thuộc 4 mức", "QĐ 1923, Phụ lục II")
                elif abs(float(o["I"]) - kc.MUC_DO[k]) > 1e-9:
                    them("KH05", "LOI", vt, f"Hệ số {o['I']} ≠ {kc.MUC_DO[k]} của mức '{o['D']}'",
                         "QĐ 1923, Phụ lục II")
            if phuong_an in ("A", "AxB"):
                try:
                    kc.tra_A(o["E"])
                except kc.LoiKPI as e:
                    them("KH08", "LOI", vt, str(e), "QĐ 2119/QĐ-CĐKT (Danh mục sản phẩm, công việc)")
            mc = kp[f"{ct['cot_minh_chung']}{ct['kpi_dong'][r]}"].value if ct["cot_minh_chung"] else None
            if not mc and "minh chứng" not in str(o["J"] or "").lower():
                them("KH07", "CANH_BAO", vt, f"'{nd[:50]}': chưa ghi nguồn minh chứng", "QĐ 1923, Đ12.4")
            if any(k in nd.lower() for k in TAP_THE):
                them("KH09", "CANH_BAO", vt, f"'{nd[:60]}' có dấu hiệu là kết quả tập thể — ghi rõ phần "
                     "cá nhân trực tiếp phụ trách", "QĐ 1923, Đ4.8")
    if nhom and km.NHOM[nhom][2] and not co_truc.get(4):
        them("KH10", "LOI", "Ke Hoach (Trục 4)", "Viên chức quản lý không có đầu việc Trục (4) — không được miễn "
             "trừ, kể cả người ngoài Đảng", "QĐ 1923, Đ12.1")
    for n, sl in co_truc.items():
        if not sl and ct["diem_truc"].get(n):
            them("KH11", "CANH_BAO", f"Ke Hoach (Trục {n})", f"Trục {n} có {ct['diem_truc'][n]:g} điểm tối đa "
                 "nhưng không có đầu việc — Trục này sẽ tính 0 điểm", "mẫu Đánh giá (Điểm KPI = 0 khi trống)")
    # KH16: mau Quy III de san SO THUC TE vi du o dong viec dau sheet KPI (L=4, N=100, P=100). Con sot thi % Truc
    # sai khi mo bang Excel. Chi bat khi TRUNG DUNG so vi du cua mau o cung o — ke hoach Quy III lap cung luc voi
    # danh gia (CV 694) nen co so thuc te that la binh thuong, khong bat.
    vd_kpi = km.thuc_te_vi_du(nhom) if nhom else {}
    for o_, v in vd_kpi.items():
        hang = {k: val for k, val in v.items()}
        if all(kp[k].value == val for k, val in hang.items()):
            them("KH16", "CANH_BAO", f"KPI!{o_}", "Số thực tế trùng đúng số ví dụ của mẫu (" +
                 ", ".join(f"{k}={val}" for k, val in hang.items()) + ") — xác nhận là số thật, nếu không thì xóa",
                 "Known-Issues-Bieu-Mau #12")
    # KH17–KH19 (lenh sua 25/9/2026): sheet KPI cot C–F va chieu cao dong. Cot do theo TIEU DE cua mau.
    kc_ = ct.get("kpi_cot", {})
    rong = {"Ke Hoach": km.do_rong_cot(ws), "KPI": km.do_rong_cot(kp)}
    gop = {"Ke Hoach": km._vung_gop(ws), "KPI": km._vung_gop(kp)}
    for n, (d, c) in ct["truc"].items():
        for r in range(d, c + 1):
            nd = str(ws[f"B{r}"].value or "").strip()
            if not nd:
                continue
            rk = ct["kpi_dong"][r]
            if "phoi_hop" in kc_ and kp[f"{kc_['phoi_hop']}{rk}"].value in (None, ""):
                them("KH17", "CANH_BAO", f"KPI!dòng {rk} (Trục {n})", f"'{nd[:50]}': thiếu người phối hợp — cần người "
                     "dùng bổ sung (không tự điền)", "mẫu KPI cột 'Người phối hợp'")
            if "san_pham" in kc_:
                f = kp[f"{kc_['san_pham']}{rk}"].value
                m = re.fullmatch(r"='?Ke Hoach'?!\$?E\$?(\d+)", str(f or "").strip())
                if f in (None, "") or (str(f).startswith("=") and not m) or \
                        (m and str(ws[f"B{int(m.group(1))}"].value or "").strip() in ("",)):
                    them("KH18", "LOI", f"KPI!{kc_['san_pham']}{rk} (Trục {n})", f"Ô sản phẩm dự kiến '{f}' trống hoặc "
                         "không trỏ đúng dòng có việc của sheet Ke Hoach (phải là ='Ke Hoach'!E<dòng>)", "mẫu KPI cột F")
            for ten, sh, rr in (("Ke Hoach", ws, r), ("KPI", kp, rk)):
                can, dong = km.uoc_chieu_cao(wb, sh, rr, rong[ten], gop[ten])
                if can > km.CAO_TOI_DA:
                    them("KH19", "CANH_BAO", f"{ten}!dòng {rr} (Trục {n})", f"'{nd[:40]}': cần ~{dong} dòng chữ "
                         f"({can:.0f} pt) > {km.CAO_TOI_DA} pt — Excel không hiện hết; rút gọn hoặc nới rộng cột",
                         "giới hạn chiều cao dòng Excel")
    if re.search(r"Quyết định số:\s*/", str(kp["A1"].value or "")):
        them("KH13", "CANH_BAO", "KPI!A1", "Ô số Quyết định trong tiêu đề còn trống", "Known-Issues-Bieu-Mau #5")
    return {"tep": os.path.basename(p), "nhom": nhom, "phuong_an": phuong_an,
            "so_dau_viec": sum(co_truc.values()), "loi": ds}


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("tep")
    ap.add_argument("--nhom", choices=list(km.NHOM))
    ap.add_argument("--phuong-an", choices=list(kc.PHUONG_AN))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    kq = kiem(a.tep, a.nhom, a.phuong_an)
    if a.json:
        print(json.dumps(kq, ensure_ascii=False, indent=1))
    else:
        print(f"=== {kq['tep']} — nhóm {kq['nhom'] or '?'} — {kq['so_dau_viec']} đầu việc ===")
        for x in sorted(kq["loi"], key=lambda x: (x["muc"] != "LOI", x["ma"])):
            print(f"  [{x['muc']:8s}] {x['ma']} {x['vi_tri']}: {x['noi_dung']}  [{x['can_cu']}]")
        if not kq["loi"]:
            print("  ✓ Không phát hiện lỗi")
    return 1 if any(x["muc"] == "LOI" for x in kq["loi"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
`````

## `scripts/vanphong.py` (6960 byte, sha256 `22a46f9985b6ba8a275791a776fb77abca517f8318472f06e26e880d82a8ca70`)

`````python
# -*- coding: utf-8 -*-
"""Lop chuyen van phong cap don vi -> cap Truong.

Can cu: chu thich trong '00. Mau bao cao thang (cap Truong).docx':
  "{Luu y nguyen tac: chuyen van phong tu Phong sang van phong cap Truong,
    khong dung cac tu/cum tu nhu: Tham muu cho Lanh dao Truong..., phoi hop voi
    {cac don vi thuoc Truong...}"
Doi chieu thuc te BC-375 (da ban hanh): 0 lan "tham muu".
"""
import re

# Doi tac NGOAI Truong — "phoi hop voi" nhung doi tuong nay VAN GIU (BC-375 co dung)
NGOAI = (r"doanh nghiệp|công ty|UBND|Ủy ban|Sở |Ban Dân tộc|Đài |Báo |trường |Viện |"
         r"Trung tâm Y tế|bệnh viện|đối tác|địa phương|xã |phường |tỉnh |huyện|"
         r"cơ quan|đơn vị liên quan|các bên|CSGT|Công an|cảnh sát|Quân sự|Biên phòng|Liên đoàn|Tỉnh đoàn|Hội |Ngân hàng|Bảo hiểm|Kho bạc|Chi cục|Cục ")

# Dong tu di sau "tham muu" -> bo han "tham muu", giu dong tu
VERB_SAU = (r"ban hành|xây dựng|triển khai|tổ chức|thực hiện|đề xuất|trình|rà soát|"
            r"hoàn thiện|sửa đổi|bổ sung|cập nhật|phê duyệt|góp ý|kiểm tra|lập|"
            r"soạn thảo|công bố|hướng dẫn|tổng hợp|báo cáo|đăng ký|theo dõi|đôn đốc|"
            r"tiếp nhận|giải quyết|quản lý|chuẩn bị|tham gia|phát động|tuyên truyền|"
            r"sơ kết|tổng kết|nghiệm thu|thẩm định|xét|chấm|cấp|thu thập|bố trí|"
            r"phân công|điều chỉnh|thay thế|bãi bỏ|hợp nhất|giám sát|đánh giá")

# Danh tu di sau "tham muu" -> doi thanh "xay dung <danh tu>"
NOUN_SAU = (r"văn bản|nội dung|kế hoạch|quy chế|quy định|đề án|báo cáo|tờ trình|"
            r"quyết định|hồ sơ|phương án|chương trình|thông báo|hướng dẫn|đề cương")

# Ten don vi NOI BO — liet ke tuong minh de khong an nham noi dung phia sau
NOI_BO = (
    r"Phòng\s+TCCB\s*&\s*CTHSSV|Phòng\s+Tổ chức cán bộ và Công tác học sinh,?\s*sinh viên|"
    r"Phòng\s+QLĐT\s*&\s*BĐCL|Phòng\s+Quản lý [Đđ]ào tạo và Bảo đảm chất lượng|"
    r"Phòng\s+TH\s*-\s*HC\s*&\s*QT|Phòng\s+Tổng hợp\s*-\s*Hành chính và Quản trị|"
    r"Phòng\s+QLKHCN\s*&\s*HTPT|Phòng\s+Quản lý khoa học công nghệ và Hợp tác phát triển|"
    r"Phòng\s+TC\s*-\s*KT|Phòng\s+Tài chính\s*-\s*Kế toán|"
    r"Khoa\s+CKHCB|Khoa\s+các Khoa học cơ bản|Khoa\s+Sư phạm|"
    r"Khoa\s+KT\s*&\s*NL|Khoa\s+Kinh tế và Nông [LlÂâ]âm|Khoa\s+Kinh tế\s*-\s*Nông lâm|"
    r"Khoa\s+KT\s*&\s*CN|Khoa\s+Kỹ thuật và Công nghệ|"
    r"Khoa\s+Y\s*[–-]\s*Dược|Khoa\s+ĐT\s*&\s*SHLX|Khoa\s+Đào tạo và Sát hạch lái xe|"
    r"Ban\s+Truyền thông|các bộ môn|các khoa|các phòng|các đơn vị thuộc Trường|"
    r"Bộ môn\s+[A-ZĐ][^\s,;]*(\s*&\s*[A-ZĐ][^\s,;]*)?"
)


# Chu ngu cap don vi dung dau cau -> "Nha truong".
# Lookahead chu THUONG de khong an nham ten rieng ("Khoa Ky thuat va Cong nghe").
CHU_NGU = re.compile(
    r"^(BCH\s+CĐCS\s+Trường|CĐCS\s+Trường|Công đoàn cơ sở Trường|Ban Chấp hành\s+CĐCS"
    r"|Ban Truyền thông|Đoàn Thanh niên Trường|Chi bộ|Khoa|Phòng|Bộ môn)"
    r"\s+(?=[a-zàáâãèéêìíòóôõùúăđĩũơưăạ])", re.U)
# KHONG dua "Ban"/"Don vi" tran vao CHU_NGU: "Ban hanh Ke hoach..." se bi
# nuot chu "Ban" -> "Nha truong hanh Ke hoach". Da mac loi nay mot lan.


def chu_ngu_truong(t: str) -> str:
    return CHU_NGU.sub("Nhà trường ", t)


def cap_truong(s: str) -> str:
    """Chuyen 1 cum mo ta cong viec cap don vi sang van phong cap Truong."""
    t = " ".join(s.split())
    t = chu_ngu_truong(t)

    # 1. "tham mưu cho Lãnh đạo Trường/Hiệu trưởng ..." -> bo cum tham mưu
    t = re.sub(r"tham\s*mưu\s*(,|và)?\s*(đề xuất\s*)?(cho\s+)?"
               r"(Lãnh đạo\s+Trường|Hiệu trưởng|Ban Giám hiệu|Nhà trường|Trường)\s*",
               "", t, flags=re.I)

    # 2. "tham mưu <động từ>" -> bo "tham mưu", giu dong tu
    t = re.sub(rf"tham\s*mưu\s*(,|và)?\s*(?=({VERB_SAU}))", "", t, flags=re.I)

    # 3. "tham mưu <danh từ>" -> "xây dựng <danh từ>"
    t = re.sub(rf"tham\s*mưu\s+(?=({NOUN_SAU}))", "xây dựng ", t, flags=re.I)

    # 3b. Con lai: bo han "tham mưu" thay vi doan bua -> tranh sai ngu phap
    t = re.sub(r"tham\s*mưu\s*(,|và)?\s*", "", t, flags=re.I)

    # 4. "phối hợp (với) <đơn vị NỘI BỘ>" -> bo dung ten don vi, GIU lai hanh dong
    t = re.sub(rf"(phối hợp|cùng)\s*(với\s*)?({NOI_BO})\s*(,|;|và)?\s*", "", t, flags=re.I)

    # 5. "trình/đề xuất Lãnh đạo Trường|Hiệu trưởng <động từ>" -> bo cum trinh
    t = re.sub(rf"(trình|đề xuất)\s+((Phó\s+)?Hiệu trưởng|Lãnh đạo\s+(Trường|khoa|phòng|đơn vị)|Ban Giám hiệu|Trưởng khoa|Trưởng phòng)\s*"
               rf"(xem xét\s*)?(,|và)?\s*(?=({VERB_SAU}))", "", t, flags=re.I)
    t = re.sub(r"(trình|đề xuất)\s+((Phó\s+)?Hiệu trưởng|Lãnh đạo\s+(Trường|khoa|phòng|đơn vị)|Ban Giám hiệu|Trưởng khoa|Trưởng phòng)\s*",
               "", t, flags=re.I)

    # 6. Don dep
    t = re.sub(r"\s{2,}", " ", t)
    t = re.sub(r"^\s*(,|;|và)\s*", "", t)
    t = re.sub(r"\s+(,|;)", r"\1", t)
    return t.strip(" ,;")


def kiem_tra(t: str):
    """Tra ve danh sach vi pham con lai."""
    loi = []
    if re.search(r"tham\s*mưu", t, re.I):
        loi.append("còn 'tham mưu'")
    m = re.search(r"phối hợp\s*(với)?\s*((các\s+)?(Phòng|Khoa|Bộ môn)\s+\S+)", t, re.I)
    if m and not re.search(NGOAI, m.group(2), re.I):
        loi.append(f"phối hợp nội bộ: {m.group(2)[:40]}")
    if re.search(r"(trình|đề xuất)\s+((Phó\s+)?Hiệu trưởng|Lãnh đạo|Ban Giám hiệu|Trưởng khoa|Trưởng phòng)", t, re.I):
        loi.append("còn 'trình/đề xuất Lãnh đạo'")
    if CHU_NGU.match(t):
        loi.append(f"chủ ngữ cấp đơn vị: {t[:28]}")
    return loi


if __name__ == "__main__":
    THU = [
        "tham mưu văn bản, đề xuất có liên quan đến công tác truyền thông",
        "tham mưu nội dung và Báo cáo những điểm mới của các Nghị định",
        "rà soát, tham mưu đăng ký loại bỏ các ngành, nghề đào tạo không còn phù hợp",
        "tham mưu cho Lãnh đạo Trường ban hành Quy chế chi tiêu nội bộ",
        "phối hợp Phòng Quản lý đào tạo và Bảo đảm chất lượng xét điều kiện dự thi",
        "phối hợp với doanh nghiệp tổ chức thực hành, thực tập",
        "trình Hiệu trưởng phê duyệt kế hoạch tuyển sinh năm 2026",
    ]
    for s in THU:
        r = cap_truong(s)
        print(f"  TRUOC: {s}\n  SAU  : {r}\n  loi  : {kiem_tra(r) or 'sach'}\n")
`````

=== HẾT TỆP N21-PLUGIN-SCRIPT-PYTHON.md — MÃ KIỂM: AC5E98 ===
