# -*- coding: utf-8 -*-
"""Bo kiem nhat quan NQ01-NQ10 cho tu danh gia KPI ca nhan (lenh 28/10/2026, muc 2.1).

Sinh ra tu phien lam ho so Quy III/2026: cong cu tin truong "Ket qua nhiem vu" nguoi dung khai ma khong doi
chieu voi % tien do, SL thuc te (viec B25 khai "Hoan thanh dung han" trong khi 75%, SL 5/7 van duoc dem la
"dung han"). Bo kiem nay doi chieu CHEO cac truong trong cung mot dong viec va giua sheet B voi sheet C.

Muc:
  LOI       -> chan xuat san pham chinh thuc (ma thoat 2), nguoi dung phai sua bang hoi
  CANH_BAO  -> van xuat, nhung ghi trong bang dieu kien de nguoi co tham quyen xem

KHONG tu sua so lieu cua nguoi dung, KHONG tu chon phuong an khi hai dieu khoan mau thuan.
"""
import datetime
import re
import unicodedata

EPS = 1e-6
LOI, CANH_BAO = "LỖI", "CẢNH_BÁO"

# Chuoi khong duoc con trong ban nop (muc 3.4 cua lenh) — bai hoc 1/10/2026: "DỰ THẢO", "em đã…" lot vao bang
CHUOI_CAM = ("CẦN BỔ SUNG", "DỰ THẢO", "em đã", "TODO", "[CẦN", "XXX", "???")

LOAI_VUOT = ("số lượng", "chất lượng", "tiến độ", "hiệu quả")
VUOT, DUNG_HAN, CHAM, KHONG_HT = "Vượt mức", "Hoàn thành đúng hạn", "Hoàn thành chậm tiến độ", "Không hoàn thành"
HTXS = "Hoàn thành xuất sắc nhiệm vụ"


def _kd(s):
    t = unicodedata.normalize("NFD", str(s or "").lower())
    return " ".join("".join(c for c in t if unicodedata.category(c) != "Mn").replace("đ", "d").split())


def _so(v):
    if v in (None, ""):
        return None
    try:
        return float(str(v).replace(",", ".").replace("%", "").strip())
    except (TypeError, ValueError):
        return None


def ngay(v):
    """Doc ngay tu o Excel. Tra ve date hoac None khi khong phai ngay (vd 'Quý III/2026', 'Tháng 9/2026')."""
    if isinstance(v, datetime.datetime):
        return v.date()
    if isinstance(v, datetime.date):
        return v
    s = str(v or "").strip()
    for mau in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%d/%m/%y"):
        try:
            return datetime.datetime.strptime(s, mau).date()
        except ValueError:
            continue
    return None


def tron_ven(v):
    """Viec duoc coi la hoan thanh tron ven: SL thuc >= SL ke hoach, chat luong va tien do >= 100%."""
    G, L, N, P = v.get("G"), v.get("L"), v.get("N"), v.get("P")
    if None in (L, N, P):
        return None                      # thieu du lieu — khong ket luan
    if G is not None and L < G - EPS:
        return False
    return N >= 100 - EPS and P >= 100 - EPS


def suy_c08(viec):
    """Suy dieu kien 'hoan thanh 100% nhiem vu' tu sheet B (muc 2.2 cua lenh).

    Tra ve {'tong', 'tron', 'chua_tron': [(ma, noi_dung, ly_do)], 'thieu': [ma], 'ket_luan': 'Có'|'Không'|None}."""
    tong, tron, chua, thieu = 0, 0, [], []
    for v in viec:
        tong += 1
        t = tron_ven(v)
        if t is None:
            thieu.append(v.get("ma"))
        elif t:
            tron += 1
        else:
            chua.append((v.get("ma"), str(v.get("noi_dung") or "")[:60], str(v.get("ly_do_chua") or "").strip()))
    ket = None if thieu else ("Có" if not chua else "Không")
    return {"tong": tong, "tron": tron, "chua_tron": chua, "thieu": thieu, "ket_luan": ket}


def _co_can_cu_vuot(v):
    loai = str(v.get("loai_vuot") or "").strip()
    can_cu = str(v.get("can_cu_vuot") or "").strip()
    hop_le = any(_kd(loai) == _kd(x) for x in LOAI_VUOT)
    return hop_le and len(can_cu) >= 5


def kiem(khd, tl, viec, truc=None, tu_de_xuat=None, ban_nop=False, ban_cu=False):
    """Tra ve [(ma, muc, thong_diep)] — da sap theo ma. `viec` la danh sach dict co G, L, N, P, ket_qua...

    `ban_nop=True` thi bat NQ06 (chuoi cam) o muc LOI; ban noi bo chi CANH_BAO.
    `ban_cu=True` (bang hoi v1.3 thieu 6 cot moi) thi cac phep kiem CAN COT MOI chi CANH_BAO — tuong thich nguoc
    (lenh 28/10/2026, muc 2.2)."""
    ds = []
    CAN_COT_MOI = ("NQ03", "NQ05", "NQ07")

    def them(ma, muc, tin):
        if ban_cu and ma in CAN_COT_MOI and muc == LOI:
            muc, tin = CANH_BAO, tin + " — bảng hỏi bản cũ chưa có cột này, hạ xuống cảnh báo"
        ds.append((ma, muc, tin))

    n = len(viec)
    vuot = [v for v in viec if str(v.get("ket_qua") or "").strip() == VUOT]

    for v in viec:
        ma, nd = v.get("ma"), str(v.get("noi_dung") or "")[:46]
        kq = str(v.get("ket_qua") or "").strip()
        G, L, P = v.get("G"), v.get("L"), v.get("P")
        # NQ01 — khai dat/vuot nhung so lieu chua tron
        if kq in (VUOT, DUNG_HAN):
            ly = []
            if P is not None and P < 100 - EPS:
                ly.append(f"% tiến độ {P:g} < 100")
            if G is not None and L is not None and L < G - EPS:
                ly.append(f"SL thực {L:g} < SL kế hoạch {G:g}")
            if ly:
                them("NQ01", LOI, f"{ma} “{nd}” — khai “{kq}” nhưng {', '.join(ly)}; sửa kết quả nhiệm vụ "
                                  "hoặc sửa số liệu, không để công cụ đếm là đúng hạn")
        # NQ02 — khai cham nhung tien do 100%
        if kq == CHAM and P is not None and P >= 100 - EPS:
            them("NQ02", CANH_BAO, f"{ma} “{nd}” — khai “{CHAM}” nhưng % tiến độ = {P:g}; kiểm lại một trong hai")
        # NQ03 — vuot muc khong co can cu
        if kq == VUOT and not _co_can_cu_vuot(v):
            them("NQ03", LOI, f"{ma} “{nd}” — khai “{VUOT}” nhưng thiếu Loại vượt "
                              f"({' / '.join(LOAI_VUOT)}) hoặc Căn cứ vượt mức kèm số liệu [TB 1105, mục 2.3]")
        # NQ05 — vuot muc ma hoan thanh muon hon thoi han
        if kq == VUOT:
            nt, nh = ngay(v.get("thoi_han")), ngay(v.get("ngay_hoan_thanh"))
            if nt and nh and nh > nt:
                them("NQ05", LOI, f"{ma} “{nd}” — khai “{VUOT}” nhưng ngày hoàn thành thực tế {nh:%d/%m/%Y} muộn "
                                  f"hơn thời hạn {nt:%d/%m/%Y}")
        # NQ07 — khong co so hieu minh chung, khong ghi ly do
        so_hieu = str(v.get("so_hieu") or v.get("minh_chung") or "").strip()
        ly_do_mc = _kd(v.get("ly_do_chua")) + " " + _kd(v.get("noi_luu"))
        if not so_hieu and "khong yeu cau minh chung" not in ly_do_mc:
            them("NQ07", CANH_BAO, f"{ma} “{nd}” — chưa có số hiệu văn bản minh chứng và chưa ghi lý do "
                                   "“không yêu cầu minh chứng”")

    # NQ04 — tu de xuat HTXS nhung ty le vuot muc duoi 30%
    if str(tu_de_xuat or "").strip() == HTXS:
        tl_vuot = len(vuot) / n * 100 if n else 0.0
        if tl_vuot < 30 - EPS:
            them("NQ04", LOI, f"Tự đề xuất “{HTXS}” nhưng chỉ {len(vuot)}/{n} nhiệm vụ vượt mức "
                              f"({tl_vuot:.2f}% < 30%) [QĐ 1923, Đ19.1a; TB 1105, mục 2.2]")

    # NQ06 — chuoi cam
    for v in viec:
        for truong in ("K", "minh_chung", "can_cu_vuot", "ly_do_chua", "noi_luu", "so_hieu"):
            s = str(v.get(truong) or "")
            for c in CHUOI_CAM:
                if c.lower() in s.lower():
                    them("NQ06", LOI if ban_nop else CANH_BAO,
                         f"{v.get('ma')} — còn chuỗi “{c}” ở cột {truong}; bản nộp không được còn dấu vết nháp")
                    break

    # NQ08 — tong % theo Truc phai khop khi tinh lai
    if truc:
        for sotruc, t in truc.items():
            vs = [v for v in viec if v.get("truc") == sotruc and v.get("J") is not None]
            sj = sum(v["J"] for v in vs)
            lai = (sum(min(v["tb"], v["J"]) for v in vs) / sj * 100) if sj else 0.0
            if abs(lai - t.get("pt", 0)) > 0.01:
                them("NQ08", LOI, f"Trục ({sotruc}) — % tính lại {lai:.4f}% lệch {abs(lai - t['pt']):.4f} điểm "
                                  f"phần trăm so với {t['pt']:.4f}% đã ghi — kiểm lại công thức chặn trần [Đ11.6]")

    # NQ09 — tu de xuat cao hon muc theo nguong diem
    MUC = (HTXS, "Hoàn thành tốt nhiệm vụ", "Hoàn thành nhiệm vụ", "Không hoàn thành nhiệm vụ")
    muc_diem = str((tl or {}).get("_muc_theo_diem") or "")
    de = str(tu_de_xuat or "").strip()
    if de in MUC and muc_diem in MUC and MUC.index(de) < MUC.index(muc_diem):
        them("NQ09", CANH_BAO, f"Tự đề xuất “{de}” cao hơn mức theo ngưỡng điểm “{muc_diem}” — nêu cả hai, "
                               "quyết định thuộc Trưởng đơn vị và Hiệu trưởng [QĐ 1923, Đ14.3c]")

    # NQ10 — C08 khai "Co"/"Xac nhan" nhung con viec chua tron
    c08 = str((tl or {}).get("C", {}).get("C08") or "").strip()
    if c08:
        sy = suy_c08(viec)
        khai_co = c08 == "Có" or _kd(c08).startswith("xac nhan")
        if khai_co and sy["chua_tron"]:
            ds_ = ", ".join(f"{m} ({ld or 'chưa ghi lý do'})" for m, _nd, ld in sy["chua_tron"][:5])
            them("NQ10", CANH_BAO, f"C08 khai “{c08}” nhưng {len(sy['chua_tron'])}/{sy['tong']} nhiệm vụ chưa trọn "
                                   f"100%: {ds_}. Nêu cả hai, không tự chọn — điều kiện Đ19.1 áp cho cả ba mức, "
                                   "gỡ hay không thuộc người có thẩm quyền")
    return sorted(ds, key=lambda x: (x[0], x[2]))


def bang(ds):
    """In bo ket qua kiem thanh bang Markdown."""
    if not ds:
        return "Bộ kiểm nhất quán NQ01–NQ10: **không phát hiện vấn đề**."
    L = ["| Mã | Mức | Nội dung |", "|---|---|---|"]
    L += [f"| {m} | {muc} | {tin} |" for m, muc, tin in ds]
    n_loi = sum(1 for _, muc, _ in ds if muc == LOI)
    L.append("")
    L.append(f"Tổng: {n_loi} LỖI (chặn xuất bản chính thức) · {len(ds) - n_loi} CẢNH_BÁO.")
    return "\n".join(L)


def co_loi(ds):
    return any(muc == LOI for _, muc, _ in ds)
