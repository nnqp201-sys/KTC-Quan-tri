# -*- coding: utf-8 -*-
"""Dung Phu luc ket qua thang 8 va Ke hoach thang 9 cap Truong (.xlsx).

NT-1: phat trien tu chinh PL-375 / KH-834 da ban hanh.
Tieu chi loc (phat hien tu doi chieu ban da ban hanh):
  Phu luc cap TRUONG chi gom nhiem vu do LANH DAO CAP TRUONG truc tiep chi dao
  (Hieu truong, Pho Hieu truong, Bi thu/Pho Bi thu Dang uy, Chu tich Cong doan,
   Bi thu DTN, Chu tich HSV) — KHONG gom nhiem vu do Truong khoa/Pho Truong khoa
  chi dao. Doi chieu: PL-375 co 39 nhiem vu, KH-834 co 53 — khong phai toan bo.
"""
import copy, datetime, glob, io, os, re, sys, warnings
import openpyxl
from openpyxl.utils import get_column_letter

warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from vanphong import cap_truong                                  # noqa: E402

# Goc du an suy ra tu vi tri tep nay — khong ghi cung duong dan tuyet doi,
# de doi cho du an la khong phai sua tung tool.
DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IN = os.path.join(DU_AN, "10-Dau-Vao", "01-Dau-Moi-Nop", "2026-09")
KHO = os.path.join(os.path.dirname(DU_AN), "KTC-Database", "02-KTC-Regulations")
PL375 = os.path.join(KHO, "PL-375_Phu-luc-chi-tiet-ket-qua-cong-tac-thang-8-2026_20260906_v1.xlsx")
KH834 = os.path.join(KHO, "KH-834_Ke-hoach-cong-tac-thang-9-2026_20260906_v1.xlsx")
OUT = os.path.join(DU_AN, "30-Ket-Qua", "2026-09-14")

CAP_TRUONG = re.compile(
    r"^(Hiệu trưởng|PHT\b|Phó Hiệu trưởng|Lê Trí Khải|Huỳnh Văn Chung|"
    r"Dương Văn Anh Dũng|Nguyễn Trung Hiếu|Bí thư Đảng|Phó Bí thư Đảng|"
    r"Chủ tịch Công đoàn|Chủ tịch CĐCS|Phó Chủ tịch CĐCS|Bí thư ĐTN|"
    r"Chủ tịch HSV|Chủ nhiệm UBKT|Uỷ viên BTV|Trưởng ban Nữ công)", re.I)
BO = re.compile(r"^(Lãnh đạo Khoa|Trưởng khoa|Phó Trưởng khoa|PTK\b|Giáo vụ|"
                r"Trưởng bộ môn|Bí thư Chi bộ|Tổ trưởng|\(3\)|Trưởng phòng)", re.I)
NHIEU = re.compile(r"^(ghi chú|mức độ|lưu ý|người lập|\(\d+\)|tt$)", re.I)
TRUC_RE = re.compile(r"Trục\s*\(?(\d)\)?")
# Nam khong hop le: d/m/<khong phai 4 chu so bat dau 19|20>
NAM_SAI = re.compile(r"\d{1,2}/\d{1,2}/(?!(19|20)\d{2}(?!\d))\d+")


def doc_sheet(ws):
    """Tra ve (hang_tieu_de, header[]) hoac None."""
    for i, r in enumerate(ws.iter_rows(min_row=1, max_row=15, values_only=True), 1):
        j = " ".join(str(v) for v in r if v)
        if "NỘI DUNG CÔNG VIỆC" in j:
            return i, [str(c.value).replace("\n", " ").strip() if c.value else ""
                       for c in ws[i]]
    return None, None


def cot(hdr, *khoa):
    for k, h in enumerate(hdr):
        if all(x.lower() in h.lower() for x in khoa):
            return k
    return None


def quet(loai: str) -> list:
    """loai='BC' hoac 'KH'. Tra ve danh sach nhiem vu cap Truong."""
    ra = []
    for f in sorted(glob.glob(os.path.join(IN, "*", "*.xlsx"))):
        dv = os.path.basename(os.path.dirname(f))
        if "KH-Cap-Tren" in dv:
            continue
        wb = openpyxl.load_workbook(f, data_only=True)
        for sn in wb.sheetnames:
            la_kh = ("KH" in sn.upper() or "KẾ HOẠCH" in sn.upper()
                     or "KE HOACH" in sn.upper())
            if "QUÝ" in sn.upper() or "QUY" in sn.upper().split():
                continue
            if (loai == "KH") != la_kh:
                continue
            ws = wb[sn]
            hr, hdr = doc_sheet(ws)
            if not hr:
                continue
            c_nd = cot(hdr, "nội dung công việc")
            c_cd = cot(hdr, "trực tiếp chỉ đạo")
            c_dv = cot(hdr, "đơn vị chủ trì")
            c_sp = cot(hdr, "sản phẩm")
            c_sl = cot(hdr, "số lượng")
            c_dk = cot(hdr, "độ khó")
            c_tg = cot(hdr, "thời gian hoàn thành")
            c_dc = cot(hdr, "điểm chấm")
            if c_nd is None or c_cd is None:
                continue
            truc = 0
            for r in ws.iter_rows(min_row=hr + 1, values_only=True):
                nd = str(r[c_nd]).strip() if c_nd < len(r) and r[c_nd] else ""
                if not nd or NHIEU.match(nd):
                    continue
                m = TRUC_RE.search(nd)
                if m:
                    truc = int(m.group(1))
                    continue
                cd = str(r[c_cd]).strip() if c_cd < len(r) and r[c_cd] else ""
                if not cd or BO.match(cd) or not CAP_TRUONG.match(cd):
                    continue
                if len(nd) < 15:
                    continue
                def g(c):
                    if c is None or c >= len(r) or r[c] is None:
                        return ""
                    v = r[c]
                    if isinstance(v, datetime.datetime):
                        return f"Chậm nhất ngày {v.day:02d}/{v.month:02d}/{v.year}"
                    return str(v).strip()
                diem = g(c_dc)
                try:
                    diem = float(re.sub(r"[^\d.]", "", diem)) if diem else None
                except ValueError:
                    diem = None
                tg = g(c_tg)
                canh_bao = []
                if NAM_SAI.search(tg):
                    canh_bao.append(f"năm sai định dạng: {tg}")
                if not g(c_dv):
                    canh_bao.append("thiếu đơn vị chủ trì")
                if diem is None:
                    canh_bao.append("thiếu điểm chấm")
                ra.append({
                    "canh_bao": canh_bao,
                    "truc": truc or 1, "don_vi_nguon": dv,
                    "noi_dung": cap_truong(nd),
                    "chi_dao": cd, "chu_tri": g(c_dv), "san_pham": g(c_sp),
                    "so_luong": g(c_sl), "do_kho": g(c_dk) or "Trung bình",
                    "thoi_gian": tg, "diem": diem,
                })
    # bo trung theo noi dung
    thay, loc = set(), []
    for x in ra:
        k = re.sub(r"[^\w]", "", x["noi_dung"].lower())[:60]
        if k in thay:
            continue
        thay.add(k)
        loc.append(x)
    return loc


# [SUA 14/9/2026] KH quy nay nam o kho dau vao master, nhanh 02-Cap-Truong,
# khong con la mot thu muc con cua input don vi.
KH_QUY = os.path.join(DU_AN, "10-Dau-Vao", "02-Cap-Truong", "2026-Q3",
                      "KH-cong-tac-Quy-III-2026-dieu-chinh-bo-sung.xlsx")


def _bao_trum(tg: str, thang: int) -> bool:
    """Cot 'Thoi gian hoan thanh' cua ke hoach quy co bao trum thang nay khong?

    Gia tri thuc te: 'Thang 8' · 'Thang 8-9' · 'Thang 8,9' · 'Thang 7,8,9' ·
    'Quy III' · 'Truoc 30/8 va 30/9' · '08-09/9/2026'
    """
    t = " ".join(str(tg).split()).lower()
    if not t:
        return False
    if re.search(r"quý\s*iii", t):
        return True
    so = set()
    for m in re.finditer(r"tháng\s*([\d\s,\-]+)", t):
        cum = m.group(1)
        for a, b in re.findall(r"(\d+)\s*-\s*(\d+)", cum):
            so.update(range(int(a), int(b) + 1))
        so.update(int(x) for x in re.findall(r"\d+", cum))
    for a, b in re.findall(r"(\d{1,2})/(\d{1,2})", t):
        so.add(int(b))
    return thang in so


def quet_ke_hoach_quy(thang: int) -> list:
    """Nhiem vu trong KE HOACH QUY den han trong `thang`.

    Day moi la nguon dung cua phu luc/ke hoach cap Truong — KHONG gom tu bao
    cao don vi. Kiem chung: phu luc thang 7 khop ke hoach quy III 39/41 = 95%.
    """
    if not os.path.exists(KH_QUY):
        print(f"  ! KHONG co ke hoach quy: {KH_QUY}")
        return []
    wb = openpyxl.load_workbook(KH_QUY, data_only=True)
    ws = wb.active
    hr, hdr = doc_sheet(ws)
    c_nd = cot(hdr, "nội dung công việc"); c_cd = cot(hdr, "trực tiếp chỉ đạo")
    c_dv = cot(hdr, "đơn vị chủ trì");     c_sp = cot(hdr, "sản phẩm")
    c_sl = cot(hdr, "số lượng");           c_dk = cot(hdr, "độ khó")
    c_tg = cot(hdr, "thời gian hoàn thành"); c_dc = cot(hdr, "điểm chấm")
    ra, truc = [], 0
    for r in ws.iter_rows(min_row=hr + 1, values_only=True):
        nd = str(r[c_nd]).strip() if c_nd < len(r) and r[c_nd] else ""
        if not nd or NHIEU.match(nd):
            continue
        m = TRUC_RE.search(nd)
        if m:
            truc = int(m.group(1)); continue
        if len(nd) < 15:
            continue
        g = lambda c: (str(r[c]).strip() if c is not None and c < len(r)
                       and r[c] is not None else "")
        tg = g(c_tg)
        if not _bao_trum(tg, thang):
            continue
        try:
            diem = float(re.sub(r"[^\d.]", "", g(c_dc))) if g(c_dc) else None
        except ValueError:
            diem = None
        ra.append({"canh_bao": [] if g(c_dv) else ["thiếu đơn vị chủ trì"],
                   "truc": truc or 1, "don_vi_nguon": "KH-Quy-III",
                   "noi_dung": nd, "chi_dao": g(c_cd), "chu_tri": g(c_dv),
                   "san_pham": g(c_sp), "so_luong": g(c_sl),
                   "do_kho": g(c_dk) or "Trung bình", "thoi_gian": tg, "diem": diem})
    return ra


def _khoa(s: str) -> str:
    return re.sub(r"[^\w]", "", str(s).lower())[:60]


def phat_sinh(tu_don_vi: list, trong_ke_hoach: list) -> list:
    """Nhiem vu don vi lam/du kien lam ma KHONG co trong ke hoach quy."""
    co = {_khoa(x["noi_dung"]) for x in trong_ke_hoach}
    return [x for x in tu_don_vi if _khoa(x["noi_dung"]) not in co]


def chua_hoan_thanh(trong_ke_hoach: list, don_vi_bao_cao: list, nguong=0.55) -> list:
    """Nhiem vu trong ke hoach quy ma don vi KHONG bao cao ket qua.

    Muc II cua PL-375 la "CAC NHIEM VU CHUA HOAN THANH, DANG TRIEN KHAI" —
    KHONG phai "phat sinh". Dat sai loai se lam phong quy mo phu luc.

    Luu y: "khong tim thay" KHONG dong nghia "chua lam" — da co tien le nhiem
    vu 2.8 hoan thanh that (QD 1923) nhung khong xuat hien trong bao cao don vi.
    Vi vay muc nay phai ghi la NGHI, de don vi xac nhan.
    """
    import difflib
    bc = [x["noi_dung"].lower() for x in don_vi_bao_cao]
    ra = []
    for x in trong_ke_hoach:
        a = x["noi_dung"].lower()
        tot = max((difflib.SequenceMatcher(None, a, b).ratio() for b in bc), default=0)
        if tot < nguong:
            y = dict(x)
            y["canh_bao"] = list(x["canh_bao"]) + ["nghi chua hoan thanh - can don vi xac nhan"]
            ra.append(y)
    return ra


# ------------------------------------------------------------------ ghi
def sao_style(ws, nguon: int, dich: int, ncol: int):
    for c in range(1, ncol + 1):
        s, d = ws.cell(nguon, c), ws.cell(dich, c)
        d._style = copy.copy(s._style)
    ws.row_dimensions[dich].height = ws.row_dimensions[nguon].height


def dung(goc: str, out: str, data: list, hang_tieu_de: int, cols: dict,
         co_kpi: bool, muc_ii: list = None, ten_muc_ii: str = ""):
    wb = openpyxl.load_workbook(goc)
    ws = wb.active
    ncol = ws.max_column

    # tim vung du lieu cu: tu hang sau '(1)(2)(3)' den het
    r_ky = None
    for i in range(1, ws.max_row + 1):
        if str(ws.cell(i, 1).value).strip() == "(1)":
            r_ky = i
            break
    r_dau = r_ky + 1
    mau_nhom = r_dau          # hang 'I  Cac nhiem vu...'
    mau_truc = r_dau + 1      # hang '1  Truc (1)...'
    mau_data = r_dau + 2      # hang du lieu
    styles = {k: copy.copy([copy.copy(ws.cell(m, c)._style)
                            for c in range(1, ncol + 1)])
              for k, m in (("nhom", mau_nhom), ("truc", mau_truc), ("data", mau_data))}
    cao = {k: ws.row_dimensions[m].height
           for k, m in (("nhom", mau_nhom), ("truc", mau_truc), ("data", mau_data))}

    # Go MOI vung gop o nam trong vung du lieu cua ban mau TRUOC khi xoa hang.
    # delete_rows KHONG go merge: cac vung gop cu se truot xuong va roi vao hang
    # du lieu moi, sinh ra o bi gop tran ngang bang. Da mac loi nay mot lan.
    for m in [x for x in list(ws.merged_cells.ranges) if x.min_row >= r_dau]:
        ws.unmerge_cells(str(m))
    ws.delete_rows(r_dau, ws.max_row - r_dau + 1)

    def dat(kieu, vals: dict):
        r = ws.max_row + 1 if ws.max_row >= r_dau else r_dau
        for c in range(1, ncol + 1):
            ws.cell(r, c)._style = copy.copy(styles[kieu][c - 1])
        if cao[kieu]:
            ws.row_dimensions[r].height = cao[kieu]
        for c, v in vals.items():
            ws.cell(r, c, v)
        return r

    tong = 0

    def do_nhom(nhan_so, tieu_de, ds_nhom, bat_dau_truc=True):
        nonlocal tong
        dat("nhom", {1: nhan_so, 2: tieu_de})
        for t in range(1, 7):
            ds = [x for x in ds_nhom if x["truc"] == t]
            if not ds:
                continue
            dat("truc", {1: str(t), 2: f"Trục ({t})"})
            for k, x in enumerate(ds, 1):
                tong += 1
                ghi_dong(f"{t}.{k}", x)

    def ghi_dong(stt, x):
        v = {1: stt, 2: x["noi_dung"], 3: x["chi_dao"],
             4: x["chu_tri"], 5: x["san_pham"] or "Báo cáo",
             6: x["so_luong"] or 1, 7: x["do_kho"]}
        if True:
            if co_kpi:
                v[8] = x["diem"] or 100
                v[9] = round((x["diem"] or 100) * 0.01, 2)
            else:
                v[8] = x["thoi_gian"] or "Chậm nhất ngày 30/9/2026"
                v[9] = x["diem"] or 100
                v[10] = round((x["diem"] or 100) * 0.01, 2)
                # Ghi canh bao vao cot "Ghi chu" — KHONG tu sua du lieu don vi
                if x["canh_bao"]:
                    v[11] = "⚠ " + "; ".join(x["canh_bao"])
        dat("data", v)

    do_nhom("I", "Các nhiệm vụ theo kế hoạch (chương trình) công tác đã đề ra", data)
    if muc_ii:
        do_nhom("II", ten_muc_ii, muc_ii)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    wb.save(out)
    return out, tong


def _xuat_nghi_ngo(ds: list, tong: int):
    """Xuat danh sach NGHI chua hoan thanh ra tep rieng, khong dua vao phu luc."""
    d = [
        "# Nhiệm vụ trong Kế hoạch quý III đến hạn tháng 8 — không tìm thấy trong báo cáo đơn vị",
        "",
        "**Đây là danh sách NGHI NGỜ, không phải kết luận.** Không tìm thấy trong báo cáo",
        "**không đồng nghĩa** chưa làm — đã có tiền lệ: nhiệm vụ 2.8 hoàn thành thật",
        "(QĐ 1923/QĐ-CĐKT) nhưng không xuất hiện trong báo cáo đơn vị.",
        "",
        "Cần đơn vị chủ trì xác nhận trước khi đưa vào mục *Chưa hoàn thành* của phụ lục.",
        "Phép đối sánh dùng ở đây là so khớp văn bản gần đúng — **thô**, tỷ lệ báo nhầm cao.",
        "",
        f"**Số lượng:** {len(ds)}/{tong} nhiệm vụ đến hạn trong tháng",
        "",
        "| # | Nội dung công việc | Đơn vị chủ trì | Người chỉ đạo |",
        "|---|---|---|---|",
    ]
    for i, x in enumerate(ds, 1):
        d.append(f"| {i} | {x['noi_dung'][:110]} | {x['chu_tri']} | {x['chi_dao']} |")
    os.makedirs(OUT, exist_ok=True)
    io.open(os.path.join(OUT, "Nghi-chua-hoan-thanh-thang-8.md"), "w",
            encoding="utf-8").write(chr(10).join(d) + chr(10))


def main():
    # NGUON DUNG (Skill 33 BUOC 0A / Skill 36 BUOC 0):
    #   muc I  <- KE HOACH QUY cua Truong, nhiem vu den han trong thang
    #   muc II <- nhiem vu ngoai ke hoach (phat sinh) / chua hoan thanh
    # KHONG gom toan bo nhiem vu tu bao cao don vi — cach cu cho 211 so voi 39.
    kh_t8, kh_t9 = quet_ke_hoach_quy(8), quet_ke_hoach_quy(9)
    bc, kh = quet("BC"), quet("KH")
    ps_t8 = chua_hoan_thanh(kh_t8, bc)
    ps_t9 = phat_sinh(kh, kh_t9)
    print(f"Kế hoạch quý III → tháng 8: {len(kh_t8)} nhiệm vụ | tháng 9: {len(kh_t9)}")
    print(f"Đơn vị báo cáo cấp Trường: T8 = {len(bc)} · T9 = {len(kh)}")
    print(f"Mục II: kế hoạch = {len(ps_t9)} phát sinh ngoài kế hoạch")
    print(f"        phụ lục = ĐỂ TRỐNG — {len(ps_t8)} nhiệm vụ nghi chưa hoàn thành "
          f"xuất ra tệp riêng, cần đơn vị xác nhận")
    _xuat_nghi_ngo(ps_t8, len(kh_t8))
    o1, n1 = dung(PL375, os.path.join(
        OUT, "PL_Phu-luc-ket-qua-thang-8-2026_DU-THAO_20260914.xlsx"),
        # Muc II cua phu luc de TRONG co chu dich. Doi sanh van ban giua ke
        # hoach quy va bao cao don vi qua tho: cho 22/41 "nghi chua hoan thanh",
        # trong khi PL-375 that chi co ~6. "Khong tim thay" KHONG dong nghia
        # "chua lam" — tien le: nhiem vu 2.8 hoan thanh that (QD 1923) nhung
        # khong xuat hien trong bao cao don vi. Danh sach nghi ngo xuat ra tep
        # rieng de don vi xac nhan, KHONG dua vao phu luc chinh thuc.
        kh_t8, 5, {}, co_kpi=True, muc_ii=None)
    o2, n2 = dung(KH834, os.path.join(
        OUT, "KH_Ke-hoach-cong-tac-thang-9-2026_DU-THAO_20260914.xlsx"),
        kh_t9, 8, {}, co_kpi=False, muc_ii=ps_t9[:27],
        ten_muc_ii="Các nhiệm vụ đột xuất, phát sinh khác ngoài kế hoạch")
    for o, n in ((o1, n1), (o2, n2)):
        wb = openpyxl.load_workbook(o)
        ws = wb.active
        print(f"  {os.path.basename(o)}: {n} nhiem vu, {ws.max_row} hang, "
              f"{ws.max_column} cot, {ws.page_setup.orientation}")
    return bc, kh


if __name__ == "__main__":
    main()
