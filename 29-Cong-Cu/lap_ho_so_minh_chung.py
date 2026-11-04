# -*- coding: utf-8 -*-
"""Dung Bang tong hop ho so, minh chung phuc vu ra soat xep loai quy (lenh 28/10/2026, muc 3).

Thay cac script roi viet tam trong phien 1/10/2026 (bai hoc: script o thu muc tam -> do rong cot sai don vi EMU,
co chu bang khac 14, mat dropdown cua mau; chuoi "DỰ THẢO", "em đã..." lot vao ban nop).

Dau vao : TDG (.xlsx, ban tu danh gia da xuat) + bang hoi (.xlsx) + bang tra minh chung (CSV: ma_viec, so_hieu, nguon)
Dau ra  : hai tep .docx
  - BAN NOI BO : co co [CẦN XÁC NHẬN], [SUY LUẬN], [THIẾU DỮ LIỆU] kem nguon tung o
  - BAN NOP    : sach — CHI sinh duoc khi khong con co nao; con co thi dung va in danh sach o chua xu ly

The thuc theo 20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md: A4, le 2-2-3-2 cm, Times New Roman 14 cho MOI chu
ke ca trong bang, doan noi dung dan deu hai le + thut dau dong 1,25 cm, so trang giua le tren va an o trang 1,
bang co dinh do rong cot (twips), dong tieu de lap lai moi trang, dong khong bi tach trang.

Chay:
  python 29-Cong-Cu/lap_ho_so_minh_chung.py --tdg TDG.xlsx --bang-hoi BH.xlsx [--tra-minh-chung mc.csv] \
      --ky "Quý III năm 2026" --ra-noi-bo <noi-bo.docx> [--ra-nop <nop.docx>]
Ma thoat: 2 = du lieu chua du / con co (khong sinh ban nop) · 1 = da sinh, con canh bao · 0 = sach.
"""
import argparse
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kpi_danh_gia as kd    # noqa: E402
import kpi_nhat_quan as nq   # noqa: E402

PHONG = "Times New Roman"
CO_CHU = 14
CO = ("[CẦN XÁC NHẬN]", "[SUY LUẬN]", "[THIẾU DỮ LIỆU]")
NGUON_MAC_DINH = ("bản điện tử trên Hệ thống Quản lý văn bản và điều hành (QLVB&ĐH) của Trường; "
                  "bản giấy lưu Văn thư Trường và hồ sơ công việc của đơn vị")


# ------------------------------------------------------------------ bang tra minh chung
def doc_tra_minh_chung(p):
    """CSV: ma_viec, so_hieu, nguon. Khoa LUON chuan hoa ve CHUOI (bai hoc 1/10: khoa so lan khoa chuoi ->
    hang loat dong bao 'CẦN BỔ SUNG' oan)."""
    if not p:
        return {}
    with open(p, encoding="utf-8-sig", newline="") as f:
        ds = list(csv.DictReader(f))
    if ds and "ma_viec" not in ds[0]:
        raise SystemExit(f"✗ {p}: thiếu cột 'ma_viec' (các cột: ma_viec, so_hieu, nguon).")
    ra = {}
    for r in ds:
        k = khoa(r.get("ma_viec"))
        if k:
            ra[k] = {"so_hieu": (r.get("so_hieu") or "").strip(), "nguon": (r.get("nguon") or "").strip()}
    return ra


def khoa(v):
    """Chuan hoa khoa tra cuu: 'B25', 25, '25', ' b25 ' -> 'B25'."""
    s = str(v if v is not None else "").strip().upper()
    if not s:
        return ""
    if s.isdigit():
        return "B" + s
    return s


# ------------------------------------------------------------------ noi dung
def gom_noi_dung(khd, tl, kq, tra, ky, muc_de_xuat=None):
    """Tra ve (thong_tin, muc_I, muc_II, ghi_chu, co) — moi o la (chu, co|None)."""
    ca_nhan = khd["ca_nhan"]
    muc = muc_de_xuat or str(kq.get("tu_de_xuat") or "").strip()
    sy = kq["suy_c08"]
    tt = [("Họ và tên", ca_nhan.get("Họ và tên", "")),
          ("Chức vụ, đơn vị", ", ".join(x for x in (ca_nhan.get("Chức vụ chính quyền"),
                                                    ca_nhan.get("Đơn vị công tác")) if x)),
          ("Mức cá nhân tự đề xuất", muc),
          ("Kết quả tự đánh giá", f"{kd.cat2(kq['tong'])}/100 điểm — mức theo ngưỡng điểm: "
                                  f"{kq['muc_theo_diem']}")]

    # --- Muc I: dieu kien
    I = [("Tổng điểm đánh giá đạt từ 90 điểm trở lên",
          ("Đạt" if kq["tong"] >= 90 else "Không đạt") + f" — {kd.cat2(kq['tong'])}/100 điểm",
          "Bản tự đánh giá, mục A + B", None)]
    for nd, kl, cc in kq["dieu_kien"]["theo_muc"].get(muc, []):
        co = "[THIẾU DỮ LIỆU]" if kl.startswith("Thiếu") else None
        I.append((nd, kl, f"QĐ 1923, {cc}", co))
    I.append(("Tỷ lệ cá nhân xếp loại Hoàn thành xuất sắc nhiệm vụ không vượt quá 20% nhóm tương đồng",
              "Do phòng Tổ chức cán bộ và Công tác học sinh – sinh viên tổng hợp, đối chiếu ở cấp Trường",
              "TB 1105 mục 1.3; QĐ 1923, Đ19.2", None))

    # --- Muc II: danh muc viec va minh chung
    II, co_ds = [], []
    for v in kq["viec"]:
        m = khoa(v["ma"])
        t = tra.get(m, {})
        so_hieu = t.get("so_hieu") or str(v.get("so_hieu") or "").strip()
        nguon = t.get("nguon") or str(v.get("minh_chung") or "").strip()
        co_o = None
        if so_hieu and not nguon:
            nguon = f"Văn bản {so_hieu} — {NGUON_MAC_DINH}"
        elif so_hieu and nguon and so_hieu not in nguon:
            nguon = f"Văn bản {so_hieu} — {nguon}"
        if not nguon:
            ly = str(v.get("ly_do_chua") or "") + " " + str(v.get("noi_luu") or "")
            if "không yêu cầu minh chứng" in ly.lower():
                nguon = "Không yêu cầu minh chứng (theo ghi chú của người tự đánh giá)"
            else:
                nguon, co_o = "Chưa có nguồn minh chứng", "[CẦN XÁC NHẬN]"
        elif m not in tra and not str(v.get("so_hieu") or "").strip():
            co_o = "[SUY LUẬN]"          # lay tu cot minh chung tu do, chua doi chieu bang tra
        if str(v.get("ket_qua") or "").strip() == nq.VUOT:
            cc = str(v.get("can_cu_vuot") or "").strip()
            if cc:
                nguon += f" Căn cứ vượt mức yêu cầu: {cc[0].upper() + cc[1:] if cc else cc}"
            else:
                nguon += " Căn cứ vượt mức yêu cầu: Chưa ghi"
                co_o = "[CẦN XÁC NHẬN]"
        G, L = v.get("G"), v.get("L")
        sl = f"{L:g}/{G:g}" if None not in (G, L) else "—"
        II.append((str(v["truc"]), v["noi_dung"], sl, str(v.get("ket_qua") or ""), nguon, co_o))
        if co_o:
            co_ds.append((v["ma"], co_o, v["noi_dung"][:50]))

    ghi_chu = [f"Tổng hợp từ Bản tự đánh giá {os.path.basename(khd['tep'])}; số liệu do người tự đánh giá khai "
               f"trong bảng hỏi, công cụ không tự chấm.",
               f"Nhiệm vụ trọn 100% (số lượng đủ, chất lượng và tiến độ đạt từ 100%): {sy['tron']}/{sy['tong']}."
               + (" Chưa trọn: " + "; ".join(f"{m} ({ld or 'chưa ghi lý do'})" for m, _n, ld in sy["chua_tron"])
                  if sy["chua_tron"] else ""),
               "Kết quả tự đánh giá là đề xuất của cá nhân, chưa phải kết luận của Trưởng đơn vị và Hiệu trưởng "
               "(QĐ 1923/QĐ-CĐKT, Điều 14.3c). Trần tỷ lệ Hoàn thành xuất sắc theo nhóm tương đồng do cấp Trường "
               "đối chiếu (Điều 19.2)."]
    for m, muc_nq, tin in kq.get("nhat_quan", []):
        ghi_chu.append(f"[{m}] {tin}")
        co_ds.append((m, "[CẦN XÁC NHẬN]", tin[:60]))
    return tt, I, II, ghi_chu, co_ds


# ------------------------------------------------------------------ dung .docx
def _chu(run, dam=False, nghieng=False):
    from docx.shared import Pt
    run.font.name = PHONG
    run.font.size = Pt(CO_CHU)
    run.bold = dam
    run.italic = nghieng
    rpr = run._r.get_or_add_rPr()
    rf = rpr.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts")
    if rf is not None:
        for k in ("ascii", "hAnsi", "cs", "eastAsia"):
            rf.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}" + k, PHONG)
    return run


def _doan(d, text, dam=False, nghieng=False, giua=False, thut=True, co=None):
    from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
    from docx.shared import Cm, Pt
    p = d.add_paragraph()
    p.alignment = AL.CENTER if giua else AL.JUSTIFY
    pf = p.paragraph_format
    pf.space_after = Pt(6)
    pf.first_line_indent = Cm(0 if giua or not thut else 1.25)
    _chu(p.add_run(text), dam, nghieng)
    if co:
        _chu(p.add_run(" " + co), dam=True)
    return p


def _o(cell, text, dam=False, giua=False, co=None):
    from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
    from docx.shared import Pt
    p = cell.paragraphs[0]
    p.alignment = AL.CENTER if giua else AL.JUSTIFY
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.first_line_indent = Pt(0)
    _chu(p.add_run(str(text)), dam)
    if co:
        _chu(p.add_run(" " + co), dam=True)


def _bang(d, tieu_de, hang, rong_cm, giua_cot=()):
    """Bang co dinh do rong cot theo TWIPS (bai hoc 1/10: python-docx ghi EMU -> do rong sai),
    dong tieu de lap lai moi trang, dong khong tach trang."""
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docx.shared import Cm
    t = d.add_table(rows=1, cols=len(tieu_de))
    t.style = "Table Grid"
    t.autofit = False
    for j, (ten, w) in enumerate(zip(tieu_de, rong_cm)):
        _o(t.rows[0].cells[j], ten, dam=True, giua=True)
        for r in (t.rows[0],):
            r.cells[j].width = Cm(w)
    # lap lai dong tieu de
    trpr = t.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader")
    th.set(qn("w:val"), "true")
    trpr.append(th)
    for h in hang:
        row = t.add_row()
        cs = OxmlElement("w:cantSplit")
        row._tr.get_or_add_trPr().append(cs)
        for j, v in enumerate(h[:len(tieu_de)]):
            co = h[len(tieu_de)] if len(h) > len(tieu_de) else None
            _o(row.cells[j], v, giua=(j in giua_cot), co=(co if j == len(tieu_de) - 1 else None))
            row.cells[j].width = Cm(rong_cm[j])
    # khoa do rong theo twips cho moi o
    for row in t.rows:
        for j, c in enumerate(row.cells):
            tcpr = c._tc.get_or_add_tcPr()
            for cu in tcpr.findall(qn("w:tcW")):
                tcpr.remove(cu)
            w = OxmlElement("w:tcW")
            w.set(qn("w:w"), str(int(round(rong_cm[j] * 567))))   # 1 cm = 567 twips
            w.set(qn("w:type"), "dxa")
            tcpr.append(w)
    return t


def _so_trang(d):
    """So trang giua le tren, AN o trang 1 (NĐ 30 — chuan the thuc muc 4)."""
    from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    s = d.sections[0]
    s.different_first_page_header_footer = True
    p = s.header.paragraphs[0]
    p.alignment = AL.CENTER
    r = p.add_run()
    _chu(r)
    for mau, giatri in (("begin", None), ("instrText", "PAGE"), ("end", None)):
        el = OxmlElement("w:fldChar" if mau != "instrText" else "w:instrText")
        if mau == "instrText":
            el.set(qn("xml:space"), "preserve")
            el.text = " PAGE "
        else:
            el.set(qn("w:fldCharType"), mau)
        r._r.append(el)
    s.first_page_header.paragraphs[0].text = ""


def dung_docx(ra, tt, I, II, ghi_chu, ky, noi_bo):
    import docx
    from docx.shared import Cm, Pt
    d = docx.Document()
    st = d.styles["Normal"]
    st.font.name = PHONG
    st.font.size = Pt(CO_CHU)
    st.element.rPr.rFonts.set(docx.oxml.ns.qn("w:eastAsia"), PHONG)
    s = d.sections[0]
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.top_margin, s.bottom_margin = Cm(2), Cm(2)
    s.left_margin, s.right_margin = Cm(3), Cm(2)
    _so_trang(d)

    if noi_bo:
        _doan(d, "TÀI LIỆU LÀM VIỆC NỘI BỘ — CHƯA NỘP", dam=True, giua=True)
    _doan(d, "BẢNG TỔNG HỢP HỒ SƠ, MINH CHỨNG", dam=True, giua=True)
    _doan(d, f"Phục vụ rà soát, đánh giá, xếp loại chất lượng {ky}", giua=True)
    _doan(d, "(Kèm theo Thông báo số 1105/TB-CĐKT ngày 30 tháng 9 năm 2026 của Trường Cao đẳng Kon Tum)",
          nghieng=True, giua=True)
    for nhan, v in tt:
        _doan(d, f"{nhan}: {v}")

    _doan(d, "I. ĐỐI CHIẾU ĐIỀU KIỆN THEO THÔNG BÁO SỐ 1105/TB-CĐKT (MỤC 2.2)", dam=True, thut=False)
    _bang(d, ("Điều kiện", "Kết quả đối chiếu", "Căn cứ"),
          [(a, b, c) + ((co,) if (noi_bo and co) else ()) for a, b, c, co in I], (5.5, 6.5, 4.0))
    _doan(d, "")
    _doan(d, f"II. DANH MỤC NHIỆM VỤ VÀ MINH CHỨNG {ky.upper()}", dam=True, thut=False)
    _bang(d, ("Trục", "Nội dung công việc", "SL TT/KH", "Kết quả", "Nguồn minh chứng"),
          [(a, b, c, e, f) + ((co,) if (noi_bo and co) else ()) for a, b, c, e, f, co in II],
          (1.2, 5.3, 1.6, 2.4, 5.5), giua_cot=(0, 2))
    _doan(d, "")
    _doan(d, "Ghi chú", dam=True, thut=False)
    for g in ghi_chu:
        _doan(d, "- " + g, thut=False)
    _doan(d, "")
    _doan(d, "NGƯỜI TỰ ĐÁNH GIÁ", dam=True, giua=True)
    os.makedirs(os.path.dirname(os.path.abspath(ra)) or ".", exist_ok=True)
    d.save(ra)
    return ra


# ------------------------------------------------------------------ kiem dau ra (muc 3.4)
def kiem_dau_ra(p, so_viec, ban_nop):
    """Mo lai tep, dem dong, quet chuoi cam. Tra ve danh sach loi — KHONG bao 'xong' khi chua doc lai."""
    import docx
    loi = []
    d = docx.Document(p)
    if len(d.tables) < 2:
        return [f"{os.path.basename(p)}: thiếu bảng (cần mục I và mục II)"]
    n = len(d.tables[1].rows) - 1
    if n != so_viec:
        loi.append(f"{os.path.basename(p)}: bảng mục II có {n} dòng việc, đầu vào {so_viec}")
    chu = "\n".join([p_.text for p_ in d.paragraphs]
                    + [c.text for t in d.tables for r in t.rows for c in r.cells])
    if ban_nop:
        for c in nq.CHUOI_CAM + CO:
            if c.lower() in chu.lower():
                loi.append(f"{os.path.basename(p)}: bản nộp còn chuỗi cấm “{c}”")
    for t in d.tables:
        for r in t.rows:
            for c in r.cells:
                if not c.text.strip():
                    loi.append(f"{os.path.basename(p)}: còn ô trống trong bảng (dòng {r._tr.getparent().index(r._tr)})")
                    break
    return loi


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tdg", required=True, help="tệp TDG/kế hoạch đã có số thực tế")
    ap.add_argument("--bang-hoi", required=True)
    ap.add_argument("--tra-minh-chung", help="CSV: ma_viec, so_hieu, nguon")
    ap.add_argument("--ky", default="Quý … năm …")
    ap.add_argument("--muc-de-xuat")
    ap.add_argument("--nhom", choices=list(kd.km.NHOM))
    ap.add_argument("--ra-noi-bo", required=True)
    ap.add_argument("--ra-nop")
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    try:
        khd = kd.doc_ke_hoach(a.tdg, a.nhom)
        tl = kd.doc_bang_hoi(a.bang_hoi)
        kq = kd.tinh(khd, tl)
    except (kd.Dung, kd.km.LoiCauTruc, kd.kc.LoiKPI) as e:
        print(f"✗ {e}")
        print("\nChưa dựng hồ sơ — sửa dữ liệu nguồn rồi chạy lại. Không dựng hồ sơ từ số liệu chưa đạt.")
        return 2

    tra = doc_tra_minh_chung(a.tra_minh_chung)
    tt, I, II, ghi_chu, co_ds = gom_noi_dung(khd, tl, kq, tra, a.ky, a.muc_de_xuat)
    dung_docx(a.ra_noi_bo, tt, I, II, ghi_chu, a.ky, noi_bo=True)
    loi = kiem_dau_ra(a.ra_noi_bo, len(II), ban_nop=False)
    print(f"✓ Bản nội bộ: {a.ra_noi_bo} — {len(II)} dòng việc, {len(I)} điều kiện, {len(co_ds)} ô còn cờ.")
    for m, c, nd in co_ds:
        print(f"   {c} {m}: {nd}")
    for x in loi:
        print(f"   ✗ {x}")

    if a.ra_nop:
        if co_ds:
            print(f"\n✗ CHƯA sinh bản nộp: còn {len(co_ds)} ô cần xử lý (liệt kê ở trên). "
                  "Bổ sung bảng tra minh chứng, căn cứ vượt mức, hoặc xác nhận điều kiện thiếu dữ liệu rồi chạy lại.")
            return 2
        dung_docx(a.ra_nop, tt, I, II, ghi_chu, a.ky, noi_bo=False)
        loi += kiem_dau_ra(a.ra_nop, len(II), ban_nop=True)
        print(f"✓ Bản nộp: {a.ra_nop}")
    if loi:
        print("\n".join(f"✗ {x}" for x in loi))
        return 2
    print("\nĐã đọc lại tệp đầu ra: đếm đủ số dòng việc, không còn ô trống"
          + (", không còn chuỗi cấm trong bản nộp." if a.ra_nop else "."))
    return 1 if kq.get("nhat_quan") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
