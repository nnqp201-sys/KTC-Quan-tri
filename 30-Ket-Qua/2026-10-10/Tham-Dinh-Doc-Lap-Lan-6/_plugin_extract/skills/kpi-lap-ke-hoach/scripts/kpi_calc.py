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
