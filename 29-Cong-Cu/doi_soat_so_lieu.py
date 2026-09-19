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


def ma_don_vi(p):
    thu = os.path.basename(os.path.dirname(p))
    if re.fullmatch(r"[A-Z]{1,3}-[A-Z]+", thu):
        return thu
    m = re.match(r"([A-Z]{1,3}-[A-Z]+)_", os.path.basename(p))
    return m.group(1) if m else thu


def ky_tep(p):
    """Ky cua tep theo ten: 'thang-8-2026' -> ('thang', 8, 2026); khong doan duoc -> None.
    Thu muc nop moi ky chua KQ thang N va KH thang N+1 — KHONG duoc so cheo hai ky (loi thu that 19/9/2026)."""
    t = unicodedata.normalize("NFD", os.path.basename(p).lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn").replace("đ", "d")
    m = re.search(r"(thang|quy|nam)[-_ ]?(\d{1,2})?[-_ .]*(\d{4})", t)
    if not m:
        return None
    return (m.group(1), int(m.group(2)) if m.group(2) else 0, int(m.group(3)))


def loai_tep(p):
    t = os.path.basename(p).upper()
    if re.match(r"(BC|KQ|PL)", t):
        return "KQ"
    if t.startswith("KH"):
        return "KH"
    return None


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
