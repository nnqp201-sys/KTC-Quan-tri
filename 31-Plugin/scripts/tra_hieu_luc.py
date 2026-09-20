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
        vd = kvd.kiem_tra(doan) if p.endswith(".docx") else []
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
