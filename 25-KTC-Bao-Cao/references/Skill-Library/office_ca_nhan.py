# -*- coding: utf-8 -*-
"""office_ca_nhan.py — Chuẩn hóa kết quả tra cứu cá nhân trên Hệ thống QLVB&ĐH (Skill 38, KTC-Bao-Cao v3.21).

Đầu vào (một hoặc nhiều tệp, tự nhận dạng):
  - .xlsx "Văn bản đã xử lý"  (dòng tiêu đề có "Số ký hiệu" và "Trích yếu")
  - .xlsx "Danh sách công việc đã giao" (dòng tiêu đề có "Tên công việc" và "Chủ trì")
  - .json bản chụp do Claude đọc trên trang (lược đồ tại Skill 38, mục 5)
Đầu ra: một tệp .xlsx 4 sheet (Van-ban-da-xu-ly · Cong-viec · Tong-hop · Nguon).

Công cụ CHỈ đọc tệp, lọc, đếm. Không truy cập mạng, không đăng nhập, không suy diễn Trục/sản phẩm.

Ví dụ:
  python office_ca_nhan.py --nguoi "Nguyễn Ngọc Quang Phục" --tu 01/07/2026 --den 30/09/2026 \
      --vai-tro tat-ca --ra Ket-qua-ca-nhan_Q3-2026.xlsx  Van_ban_da_xu_ly.xlsx DanhSachCongViecDaGiao.xlsx
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import unicodedata

import openpyxl
from openpyxl.styles import Alignment, Border, Font, Side
from openpyxl.utils import get_column_letter

PHIEN_BAN = "1.0"
LOAI_THEO_KY_HIEU = [
    ("QĐ", "Quyết định"), ("QyĐ", "Quy định"), ("QC", "Quy chế"), ("KH", "Kế hoạch"), ("BC", "Báo cáo"),
    ("TTr", "Tờ trình"), ("TB", "Thông báo"), ("HD", "Hướng dẫn"), ("CTr", "Chương trình"), ("PA", "Phương án"),
    ("ĐA", "Đề án"), ("DA", "Dự án"), ("BB", "Biên bản"), ("GM", "Giấy mời"), ("PC", "Phiếu chuyển/Văn bản phối hợp"),
    ("HĐ", "Hợp đồng"), ("CV", "Công văn"),
]
VB_COT = {  # khóa chuẩn -> các cách ghi tiêu đề cột gặp trên hệ thống / tệp xuất
    "so_ky_hieu": ["số ký hiệu", "số, ký hiệu", "số/ký hiệu"], "loai": ["loại văn bản", "hình thức"],
    "trich_yeu": ["trích yếu"], "ngay_soan": ["ngày soạn thảo", "ngày tạo"], "ngay_ban_hanh": ["ngày ban hành", "ngày phát hành"],
    "nguoi_soan": ["người soạn thảo", "người soạn"], "vai_tro": ["vai trò", "vai trò xử lý"], "do_mat": ["độ mật"],
    "stt_he_thong": ["stt trên hệ thống"], "ghi_chu": ["ghi chú"],
}
CV_COT = {
    "ten": ["tên công việc"], "ngay_giao": ["ngày giao việc", "ngày giao"], "han": ["ngày hết hạn", "hạn xử lý"],
    "chu_tri": ["chủ trì", "người chủ trì", "xử lý chính"], "phoi_hop": ["phối hợp", "người phối hợp"],
    "muc_do": ["mức độ công việc"], "tinh_trang": ["tình trạng"], "ket_qua": ["kết quả thực hiện"],
    "danh_gia": ["kết quả đánh giá"], "nguoi_giao": ["người giao", "người giao việc"],
}


def chuan(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", str(s or ""))).strip()


def khoa(s):
    return chuan(s).casefold()


def ngay(v):
    """Trả về datetime.date hoặc None. Nhận datetime, date, 'dd/mm/yyyy', 'yyyy-mm-dd'."""
    if v is None or v == "":
        return None
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    s = chuan(v)
    m = re.search(r"(\d{1,2})[/\-.](\d{1,2})[/\-.](\d{4})", s)
    if m:
        try:
            return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            return None
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", s)
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    return None


def loai_tu_ky_hieu(skh):
    """'945/KH-CĐKT' -> 'Kế hoạch'. Không nhận ra -> '' (không đoán)."""
    m = re.match(r"\s*\d+[a-zA-Z]?\s*/\s*([^\s\-/]+)", chuan(skh))
    if not m:
        return ""
    ma = m.group(1)
    for k, ten in LOAI_THEO_KY_HIEU:
        if ma == k:
            return ten
    return "Công văn" if ma.isupper() and ma not in dict(LOAI_THEO_KY_HIEU) else ""


def _do_tieu_de(ws, bat_buoc, bang_cot):
    """Dò dòng tiêu đề động: dòng đầu tiên có đủ các cột bắt buộc. Trả (số dòng, {khóa: chỉ số cột})."""
    for i, r in enumerate(ws.iter_rows(min_row=1, max_row=min(ws.max_row, 30), values_only=True), 1):
        o = [khoa(x) for x in r]
        cot = {}
        for k, ds in bang_cot.items():
            for j, x in enumerate(o):
                if x in ds:
                    cot[k] = j
                    break
        if all(b in cot for b in bat_buoc):
            return i, cot
    return None, {}


def doc_xlsx(p):
    """Trả (van_ban, cong_viec, ghi_chu_doc) từ một tệp xuất của hệ thống."""
    vb, cv, gc = [], [], []
    wb = openpyxl.load_workbook(p, data_only=True)
    for ws in wb:
        d, cot = _do_tieu_de(ws, ["so_ky_hieu", "trich_yeu"], VB_COT)
        if d:
            for r in ws.iter_rows(min_row=d + 1, values_only=True):
                x = {k: r[j] if j < len(r) else None for k, j in cot.items()}
                if chuan(x.get("trich_yeu")) or chuan(x.get("so_ky_hieu")):
                    vb.append(x)
            gc.append(f"{os.path.basename(p)} · sheet {ws.title}: văn bản, tiêu đề dòng {d}")
            continue
        d, cot = _do_tieu_de(ws, ["ten", "chu_tri"], CV_COT)
        if d:
            for r in ws.iter_rows(min_row=d + 1, values_only=True):
                x = {k: r[j] if j < len(r) else None for k, j in cot.items()}
                if chuan(x.get("ten")):
                    cv.append(x)
            gc.append(f"{os.path.basename(p)} · sheet {ws.title}: công việc, tiêu đề dòng {d}")
    if not gc:
        gc.append(f"{os.path.basename(p)}: KHÔNG nhận ra cấu trúc (thiếu cột bắt buộc) — bỏ qua")
    return vb, cv, gc


def doc_json(p):
    d = json.load(open(p, encoding="utf-8"))
    bl = d.get("bo_loc") or {}
    gc = [f"{os.path.basename(p)}: bản chụp trang · đọc lúc {d.get('thoi_diem_doc', '?')} · nguồn {d.get('nguon', '?')}"
          f" · bộ lọc trên trang: {json.dumps(bl, ensure_ascii=False)}"]
    for muc in ("van_ban", "cong_viec"):
        bao = (d.get("so_dong_trang_bao") or {}).get(muc)
        if bao is not None and bao != len(d.get(muc) or []):
            gc.append(f"  ⚠ {muc}: trang báo {bao} dòng, bản chụp có {len(d.get(muc) or [])} dòng — ĐỌC THIẾU, cần đọc lại")
    return d.get("van_ban") or [], d.get("cong_viec") or [], gc


def khop_nguoi(ten, ds_nguoi):
    k = khoa(ten)
    return next((n for n in ds_nguoi if khoa(n) == k), None)


def co_trong(van_ban, ds):
    k = khoa(van_ban)
    return next((x for x in ds if khoa(x) and khoa(x) in k), None)


def xu_ly(vb, cv, nguoi, don_vi, tu, den, vai_tro):
    ra_vb, ra_cv, dem = [], [], {"vb_doc": len(vb), "cv_doc": len(cv), "vb_mat": 0, "vb_ngoai_ky": 0, "vb_khac_nguoi": 0,
                                 "vb_trung": 0, "cv_ngoai_ky": 0, "cv_khac_nguoi": 0, "cv_trung": 0}
    thay = set()
    for x in vb:
        if chuan(x.get("do_mat")) and khoa(x.get("do_mat")) not in ("thường", "không", "bình thường"):
            dem["vb_mat"] += 1          # văn bản có độ mật: không đưa nội dung vào kết quả
            continue
        nbh, nst = ngay(x.get("ngay_ban_hanh")), ngay(x.get("ngay_soan"))
        moc = nbh or nst
        if moc is None or not (tu <= moc <= den):
            dem["vb_ngoai_ky"] += 1
            continue
        ns = khop_nguoi(x.get("nguoi_soan"), nguoi)
        vt = chuan(x.get("vai_tro"))
        if ns:
            vt = vt or "Soạn thảo (xử lý chính)"
            ten = ns
        elif vt and nguoi and len(nguoi) == 1:   # bản chụp đã lọc theo người trên trang, có cột vai trò
            ten = nguoi[0]
        else:
            dem["vb_khac_nguoi"] += 1
            continue
        chinh = "phối hợp" not in khoa(vt)
        if (vai_tro == "chu-tri" and not chinh) or (vai_tro == "phoi-hop" and chinh):
            dem["vb_khac_nguoi"] += 1
            continue
        skh = chuan(x.get("so_ky_hieu"))
        kt = khoa(skh) or hashlib.md5((khoa(x.get("trich_yeu")) + str(moc)).encode()).hexdigest()
        if kt in thay:
            dem["vb_trung"] += 1
            continue
        thay.add(kt)
        co = []
        if not skh:
            co.append("Chưa có số ký hiệu")
        if nbh is None:
            co.append("Chưa có ngày ban hành")
        ra_vb.append({"so_ky_hieu": skh, "loai": chuan(x.get("loai")) or loai_tu_ky_hieu(skh), "trich_yeu": chuan(x.get("trich_yeu")),
                      "ngay_soan": nst, "ngay_ban_hanh": nbh, "nguoi": ten, "vai_tro": vt, "stt": x.get("stt_he_thong"),
                      "co": "; ".join(co), "ghi_chu": chuan(x.get("ghi_chu"))})
    ra_vb.sort(key=lambda r: (r["ngay_ban_hanh"] or r["ngay_soan"], r["so_ky_hieu"]), reverse=True)
    thay = set()
    for x in cv:
        ng, han = ngay(x.get("ngay_giao")), ngay(x.get("han"))
        if not ((ng and tu <= ng <= den) or (han and tu <= han <= den)):
            dem["cv_ngoai_ky"] += 1
            continue
        ten_cv = chuan(x.get("ten"))
        ct = khop_nguoi(x.get("chu_tri"), nguoi)
        ph = co_trong(x.get("phoi_hop"), nguoi)
        if ct:
            vt, ten = "Chủ trì", ct
        elif ph:
            vt, ten = "Phối hợp", ph
        elif don_vi and co_trong(ten_cv, don_vi) and re.search(r"phối hợp", ten_cv, re.I):
            vt, ten = "Phối hợp (suy từ nội dung — cần xác nhận)", "(đơn vị)"
        else:
            dem["cv_khac_nguoi"] += 1
            continue
        chinh = vt == "Chủ trì"
        if (vai_tro == "chu-tri" and not chinh) or (vai_tro == "phoi-hop" and chinh):
            dem["cv_khac_nguoi"] += 1
            continue
        kt = (str(ng), khoa(x.get("chu_tri")), hashlib.md5(khoa(ten_cv).encode()).hexdigest())
        if kt in thay:
            dem["cv_trung"] += 1
            continue
        thay.add(kt)
        tt, kq = chuan(x.get("tinh_trang")), chuan(x.get("ket_qua"))
        co = []
        if "quá hạn" in khoa(tt):
            co.append("Quá hạn")
        if not kq:
            co.append("Chưa có kết quả trên hệ thống")
        ra_cv.append({"ten": ten_cv, "ngay_giao": ng, "han": han, "chu_tri": chuan(x.get("chu_tri")), "phoi_hop": chuan(x.get("phoi_hop")),
                      "nguoi": ten, "vai_tro": vt, "tinh_trang": tt, "ket_qua": kq, "danh_gia": chuan(x.get("danh_gia")), "co": "; ".join(co)})
    ra_cv.sort(key=lambda r: (r["han"] or dt.date.max, r["ten"]))
    return ra_vb, ra_cv, dem


# ---------------------------------------------------------------- xuất .xlsx
F = Font(name="Times New Roman", size=12)
FB = Font(name="Times New Roman", size=12, bold=True)
FT = Font(name="Times New Roman", size=13, bold=True)
FI = Font(name="Times New Roman", size=12, italic=True)
VIEN = Border(*(Side(style="thin"),) * 4)


def _bang(ws, d0, tieu_de, rong, dong, giua=()):
    for j, (t, w) in enumerate(zip(tieu_de, rong), 1):
        c = ws.cell(d0, j, t)
        c.font, c.border = FB, VIEN
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(j)].width = w
    for i, r in enumerate(dong, d0 + 1):
        for j, v in enumerate(r, 1):
            c = ws.cell(i, j, v)
            c.font, c.border = F, VIEN
            c.alignment = Alignment(horizontal="center" if j in giua else "left", vertical="top", wrap_text=True)
            if isinstance(v, dt.date):
                c.number_format = "DD/MM/YYYY"
    ws.freeze_panes = ws.cell(d0 + 1, 1)
    ws.print_title_rows = f"{d0}:{d0}"
    ws.page_setup.orientation, ws.page_setup.paperSize, ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = "landscape", 9, 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left, ws.page_margins.right, ws.page_margins.top, ws.page_margins.bottom = 0.79, 0.59, 0.79, 0.79


def _dau(ws, dong1, dong2, so_cot):
    ws.cell(1, 1, dong1).font = FT
    ws.cell(2, 1, dong2).font = FI
    for d in (1, 2):
        ws.merge_cells(start_row=d, start_column=1, end_row=d, end_column=so_cot)
        ws.cell(d, 1).alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height, ws.row_dimensions[2].height = 22, 34


def xuat(ra, ra_vb, ra_cv, dem, nguoi, tu, den, vai_tro, ghi_chu_doc):
    wb = openpyxl.Workbook()
    ky = f"từ ngày {tu:%d/%m/%Y} đến ngày {den:%d/%m/%Y}"
    ai = ", ".join(nguoi).upper()
    nhan_vt = {"tat-ca": "xử lý chính và phối hợp", "chu-tri": "xử lý chính", "phoi-hop": "phối hợp"}[vai_tro]
    ws = wb.active
    ws.title = "Van-ban-da-xu-ly"
    td = ["STT", "Số ký hiệu", "Loại văn bản", "Trích yếu", "Ngày soạn thảo", "Ngày ban hành", "Người xử lý", "Vai trò",
          "Trục (đề xuất)", "Nội hàm (đề xuất)", "Sản phẩm chuẩn QĐ 2119 (đề xuất)", "Hệ số", "Nhiệm vụ liên quan (gợi ý)",
          "Cờ dữ liệu", "Xác nhận của người báo cáo"]
    _dau(ws, f"DANH MỤC VĂN BẢN ĐÃ XỬ LÝ CỦA {ai}",
         f"Nguồn: Hệ thống quản lý văn bản và điều hành, mục “Văn bản đã xử lý”; {ky}; vai trò: {nhan_vt}. "
         "Các cột “đề xuất”, “gợi ý” do công cụ AI điền, người báo cáo xác nhận trước khi dùng.", len(td))
    _bang(ws, 3, td, [6, 16, 14, 60, 13, 13, 22, 18, 10, 22, 24, 8, 30, 20, 16],
          [[i, r["so_ky_hieu"], r["loai"], r["trich_yeu"], r["ngay_soan"], r["ngay_ban_hanh"], r["nguoi"], r["vai_tro"],
            "", "", "", "", "", r["co"], ""] for i, r in enumerate(ra_vb, 1)], giua=(1, 5, 6, 9, 12))
    ws = wb.create_sheet("Cong-viec")
    td = ["STT", "Tên công việc", "Ngày giao", "Hạn", "Chủ trì", "Phối hợp", "Vai trò của người báo cáo", "Tình trạng trên hệ thống",
          "Kết quả thực hiện", "Kết quả đánh giá", "Văn bản kết quả (gợi ý)", "Cờ dữ liệu", "Xác nhận của người báo cáo"]
    _dau(ws, f"DANH MỤC CÔNG VIỆC ĐƯỢC GIAO CỦA {ai}",
         f"Nguồn: Hệ thống quản lý văn bản và điều hành, mục “Quản lý công việc”; công việc có ngày giao hoặc hạn {ky}; vai trò: {nhan_vt}.", len(td))
    _bang(ws, 3, td, [6, 60, 12, 12, 20, 20, 20, 20, 30, 14, 26, 20, 16],
          [[i, r["ten"], r["ngay_giao"], r["han"], r["chu_tri"], r["phoi_hop"], r["vai_tro"], r["tinh_trang"], r["ket_qua"],
            r["danh_gia"], "", r["co"], ""] for i, r in enumerate(ra_cv, 1)], giua=(1, 3, 4))
    ws = wb.create_sheet("Tong-hop")
    _dau(ws, "TỔNG HỢP KẾT QUẢ TRA CỨU", f"{ky}; vai trò: {nhan_vt}", 3)
    dong = []
    for n in nguoi + (["(đơn vị)"] if any(r["nguoi"] == "(đơn vị)" for r in ra_cv) else []):
        dong.append([f"Người xử lý: {n}", sum(r["nguoi"] == n for r in ra_vb), sum(r["nguoi"] == n for r in ra_cv)])
    for vt in sorted({r["vai_tro"] for r in ra_vb} | {r["vai_tro"] for r in ra_cv}):
        dong.append([f"Vai trò: {vt}", sum(r["vai_tro"] == vt for r in ra_vb), sum(r["vai_tro"] == vt for r in ra_cv)])
    for l in sorted({r["loai"] or "(chưa rõ loại)" for r in ra_vb}):
        dong.append([f"Loại văn bản: {l}", sum((r["loai"] or "(chưa rõ loại)") == l for r in ra_vb), ""])
    for t in sorted({r["tinh_trang"] or "(không ghi)" for r in ra_cv}):
        dong.append([f"Tình trạng công việc: {t}", "", sum((r["tinh_trang"] or "(không ghi)") == t for r in ra_cv)])
    dong.append(["TỔNG", len(ra_vb), len(ra_cv)])
    _bang(ws, 3, ["Tiêu chí", "Số văn bản", "Số công việc"], [50, 14, 14], dong, giua=(2, 3))
    for j in (1, 2, 3):
        ws.cell(3 + len(dong), j).font = FB
    ws = wb.create_sheet("Nguon")
    _dau(ws, "NGUỒN DỮ LIỆU VÀ PHÉP LỌC", f"Công cụ office_ca_nhan.py bản {PHIEN_BAN}; lập lúc {dt.datetime.now():%H:%M ngày %d/%m/%Y}", 2)
    dong = [["Người tra cứu", "; ".join(nguoi)], ["Khoảng thời gian", ky], ["Vai trò", nhan_vt],
            ["Văn bản: đọc được / đưa vào", f"{dem['vb_doc']} / {len(ra_vb)}"],
            ["Văn bản loại ra", f"ngoài kỳ {dem['vb_ngoai_ky']}; không thuộc người, vai trò tra cứu {dem['vb_khac_nguoi']}; "
                               f"trùng {dem['vb_trung']}; có độ mật (không đưa vào) {dem['vb_mat']}"],
            ["Công việc: đọc được / đưa vào", f"{dem['cv_doc']} / {len(ra_cv)}"],
            ["Công việc loại ra", f"ngoài kỳ {dem['cv_ngoai_ky']}; không thuộc người, vai trò tra cứu {dem['cv_khac_nguoi']}; trùng {dem['cv_trung']}"],
            ["Giới hạn", "Chỉ gồm việc có trên Hệ thống quản lý văn bản và điều hành. Việc không phát hành qua hệ thống (dạy học, họp, "
                         "việc giao trực tiếp…) phải bổ sung từ nguồn khác. Đây là MỘT nguồn của báo cáo cá nhân, không phải toàn bộ."]]
    dong += [["Tệp nguồn", g] for g in ghi_chu_doc]
    _bang(ws, 3, ["Mục", "Nội dung"], [34, 110], dong)
    os.makedirs(os.path.dirname(os.path.abspath(ra)), exist_ok=True)
    wb.save(ra)


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a = argparse.ArgumentParser(description="Chuẩn hóa kết quả tra cứu cá nhân trên Hệ thống QLVB&ĐH (Skill 38)")
    a.add_argument("tep", nargs="+", help="tệp .xlsx xuất từ hệ thống hoặc .json bản chụp trang")
    a.add_argument("--nguoi", action="append", required=True, help="họ tên đầy đủ đúng như trên hệ thống; lặp lại được")
    a.add_argument("--don-vi", action="append", default=[], help="tên đơn vị (để nhận việc phối hợp ghi trong nội dung); lặp lại được")
    a.add_argument("--tu", required=True, help="dd/mm/yyyy")
    a.add_argument("--den", required=True, help="dd/mm/yyyy")
    a.add_argument("--vai-tro", choices=["tat-ca", "chu-tri", "phoi-hop"], default="tat-ca")
    a.add_argument("--ra", required=True, help="tệp .xlsx kết quả")
    o = a.parse_args(argv)
    tu, den = ngay(o.tu), ngay(o.den)
    if not tu or not den or tu > den:
        print("LỖI: khoảng thời gian không hợp lệ (dd/mm/yyyy, từ ≤ đến)")
        return 2
    vb, cv, gc = [], [], []
    for p in o.tep:
        if not os.path.exists(p):
            gc.append(f"{p}: KHÔNG TÌM THẤY")
            continue
        v, c, g = doc_json(p) if p.lower().endswith(".json") else doc_xlsx(p)
        vb += v; cv += c; gc += g
    if not vb and not cv:
        print("THIEU_DU_LIEU: không đọc được dòng nào từ tệp đầu vào")
        for g in gc:
            print("  ", g)
        return 1
    ra_vb, ra_cv, dem = xu_ly(vb, cv, o.nguoi, o.don_vi, tu, den, o.vai_tro)
    xuat(o.ra, ra_vb, ra_cv, dem, o.nguoi, tu, den, o.vai_tro, gc)
    print(f"Văn bản: đọc {dem['vb_doc']}, đưa vào {len(ra_vb)} (ngoài kỳ {dem['vb_ngoai_ky']}, khác người/vai trò {dem['vb_khac_nguoi']}, "
          f"trùng {dem['vb_trung']}, có độ mật {dem['vb_mat']})")
    print(f"Công việc: đọc {dem['cv_doc']}, đưa vào {len(ra_cv)} (ngoài kỳ {dem['cv_ngoai_ky']}, khác người/vai trò {dem['cv_khac_nguoi']}, trùng {dem['cv_trung']})")
    for g in gc:
        print("  ", g)
    print("→", o.ra)
    return 0


if __name__ == "__main__":
    sys.exit(main())
