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
