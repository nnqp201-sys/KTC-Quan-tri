# -*- coding: utf-8 -*-
"""Tinh toan KPI ca nhan theo QD 1923/QD-CDKT (30/8/2026) — ham thuan, co dan Dieu. Skill ktc-kpi-lap-ke-hoach.

Mo hinh KHONG duoc tu nham: moi con so (he so, so luong quy doi, diem, xep loai) di qua day.

HE SO QUY DOI — Cau hoi mo so 1 (28-KTC-KPI/references/Cau-Hoi-Mo.md). KHONG CO MAC DINH; goi thieu phuong an -> loi.
  muc-do    He so theo 4 muc do (Thap 1,0 · Trung binh 1,2 · Cao 1,5 · Kho va phuc tap 2,0)
            [QD 1923, Phu luc II — ghi chu muc do cong viec; Phu luc I cot (7)(9)(10)]  -> CO VAN BAN
  A         He so san pham theo Danh muc kem TB 1052 (Nhom 1..5)                        -> DU THAO, chua ban hanh
  AxB       A (TB 1052) x B (muc do)  — quy uoc Phong TH-HC&QT ghi nhan 24/9/2026       -> CHUA CO VAN BAN (KI-014)
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
    "A": "DỰ THẢO: Danh mục kèm TB 1052/TB-CĐKT chưa ban hành (KI-014)",
    "AxB": "CHƯA CÓ VĂN BẢN: quy ước Phòng TH-HC&QT ghi nhận 24/9/2026, chờ Phòng TCCB&CTHSSV xác nhận (KI-014)",
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


# ------------------------------------------------------------------ danh muc TB 1052
_DM = None


def danh_muc(p=None):
    """{ten san pham chuan hoa: dong} tu CSV da trich (trich_danh_muc_tb1052.py)."""
    global _DM
    if _DM is None or p:
        if not p:
            # du an · trong goi skill (scripts/../references) · ban chep o scripts/ goc cua plugin (../skills/...)
            here = os.path.dirname(os.path.abspath(__file__))
            ung = [os.path.join(DU_AN, "28-KTC-KPI", "references", "data"),
                   os.path.join(here, "..", "references", "data"),
                   os.path.join(here, "..", "skills", "kpi-lap-ke-hoach", "references", "data")]
            p = next((os.path.join(d, "he-so-san-pham-TB1052.csv") for d in ung
                      if os.path.exists(os.path.join(d, "he-so-san-pham-TB1052.csv"))), None)
            if not p:
                raise LoiKPI("Không thấy he-so-san-pham-TB1052.csv — dừng, hỏi người dùng.")
        with open(p, encoding="utf-8-sig", newline="") as f:
            _DM = {}
            for h in csv.DictReader(f):
                _DM.setdefault(_kd(h["ten_san_pham"]), h)
                _DM.setdefault("stt:" + str(h["stt"]).strip(), h)
    return _DM


def tra_A(ma_hoac_ten):
    """Tra he so A theo STT danh muc ('3.12') hoac TEN SAN PHAM KHOP CHINH XAC (chuan hoa).
    Khong co -> LoiKPI: dung hoi, KHONG tu gan A [Cau hoi mo so 2]."""
    dm = danh_muc()
    h = dm.get("stt:" + str(ma_hoac_ten).strip()) or dm.get(_kd(ma_hoac_ten))
    if not h:
        raise LoiKPI(f"Sản phẩm '{ma_hoac_ten}' không có trong Danh mục TB 1052 — dừng, hỏi người dùng "
                     "(không tự gán hệ số A).")
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
            ra.append({"stt": h["stt"], "ten": h["ten_san_pham"], "loai": h["loai_san_pham"], "nhom": h["nhom"],
                       "he_so": float(h["he_so"]), "lech_nhom": h["lech_nhom"]})
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
        if dong.get("lech_nhom"):
            cb.append(f"Hệ số A dòng {dong['stt']} lệch Nhóm: {dong['lech_nhom']} (KI-014)")
        if A > 10:
            cb.append(f"Hệ số A = {A} bất thường (dòng {dong['stt']}) — có thể lỗi nhập liệu của Danh mục")
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
                   "luu_y": "Chỉ là gợi ý — người dùng chọn STT; Danh mục là DỰ THẢO (TB 1052)"}
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
