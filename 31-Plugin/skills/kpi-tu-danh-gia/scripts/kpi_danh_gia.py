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
