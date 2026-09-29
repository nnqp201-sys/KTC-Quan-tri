# -*- coding: utf-8 -*-
"""Hoi quy kiem_the_thuc.py + hook ktc_the_thuc_hook.py — DL-20260919-003.

Ca THU NGUOC (biet chac sai) va ca DUNG — LL-20260914-001. Tu tao tep, khong phu thuoc Drive;
neu Drive co san thi do them 03-Templates(1) that (mau dung phai dat).
"""
import json
import os
import subprocess
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import docx  # noqa: E402
import openpyxl  # noqa: E402
from docx.shared import Cm, Pt  # noqa: E402
import kiem_the_thuc as k  # noqa: E402

sai = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


def ma(p):
    return {x[1] for x in k.kiem_tep(p)}


TMP = tempfile.mkdtemp(prefix="ktc_tt_")

# 1. Document() rong — loi da mac 18/9/2026 (kho Letter)
p_rong = os.path.join(TMP, "rong.docx")
d = docx.Document()
d.add_paragraph("Nội dung báo cáo " * 10)
d.save(p_rong)
m = ma(p_rong)
kiem("TT01" in m, "TT01 Document() rỗng bị bắt khổ Letter")
kiem("TT02" in m, "TT02 lề mặc định (trái 3,18 / 2,54 cm) bị bắt")
kiem("TT03" in m, "TT03 phông Calibri mặc định bị bắt")

# 2. Van ban dung chuan
# Tu 28/9/2026: dung tu khung (--khung, dung tu TB 1060 da ban hanh) — bang tieu de tay khong con dat (TT12-TT15)
import copy  # noqa: E402
p_dung = k.tao_khung(os.path.join(TMP, "dung.docx"), "BC", 2026)
d = docx.Document(p_dung)
p_nd = next(p for p in d.paragraphs if p.text.startswith("[Nội dung"))
p_nd.runs[0].text = "Nhà trường triển khai nhiệm vụ trọng tâm theo kế hoạch đã ban hành, bảo đảm tiến độ. " * 2
for _ in range(2):
    p_nd._p.addnext(copy.deepcopy(p_nd._p))
d.save(p_dung)
kq = k.kiem_tep(p_dung)
kiem(not kq, f"văn bản dựng từ khung: 0 gợi ý (được: {kq})")
kiem("BÁO CÁO" in [p.text for p in docx.Document(p_dung).paragraphs] and "/BC-CĐKT" in
     " ".join(p.text for p in k._doan_trong_bang(docx.Document(p_dung))), "--khung BC: đổi tên loại và ký hiệu")

# 3. Ca thu nguoc tung loi
d = docx.Document(p_dung)
d.tables[0].cell(0, 0).paragraphs[0].runs[0].text = "UBND TỈNH KON TUM"
d.tables[0].cell(0, 1).paragraphs[0].runs[0].font.size = Pt(12)
[p for p in d.paragraphs if p.runs][0].runs[0].font.name = ".VnTime"
for p in d.paragraphs:
    for r in p.runs:
        r.font.size = Pt(13)
p_sai = os.path.join(TMP, "sai.docx")
d.save(p_sai)
m = ma(p_sai)
kiem("TT08" in m, "TT08 cơ quan chủ quản “UBND TỈNH KON TUM” bị bắt")
kiem("TT09" in m, "TT09 Quốc hiệu cỡ 12 bị bắt")
kiem("TT03" in m, "TT03 .VnTime bị bắt")
kiem("TT04" in m, "TT04 nội dung cỡ 13 bị bắt")

# 3b. Bang tieu de dung tay (loi TB Cowork 28/9/2026) — tung loi mot, tren ban dung tu khung
W_ = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def bien(ten, sua):
    d = docx.Document(p_dung)
    sua(d)
    p = os.path.join(TMP, ten + ".docx")
    d.save(p)
    return ma(p)


def chia_doi(d):
    t = d.tables[0]
    for c in t._tbl.tblGrid.gridCol_lst:
        c.w = Cm(8)
    for r in t.rows:
        for c in r.cells:
            c.width = Cm(8)


def bo_duong_ke(d):
    for e in list(d.tables[0]._tbl.iter()):
        if e.tag in (W_ + "drawing", W_ + "pict") or e.tag.endswith("}AlternateContent"):
            if e.getparent() is not None:
                e.getparent().remove(e)


def dam(bat_dau):
    def f(d):
        for p in k._doan_trong_bang(d):
            if p.text.strip().startswith(bat_dau):
                for r in p.runs:
                    r.bold = True
    return f


def can_cu_khong_thut(d):
    p = next(p for p in d.paragraphs if p.text.startswith("Căn cứ"))
    p.paragraph_format.first_line_indent = Cm(0)
    p_nd = next(p for p in d.paragraphs if p.text.startswith("Nhà trường"))
    p_nd.paragraph_format.first_line_indent = Cm(1.25)


kiem("TT12" in bien("chia_doi", chia_doi), "TT12 bảng tiêu đề chia đôi 8 + 8 cm bị bắt")
kiem("TT14" in bien("bo_ke", bo_duong_ke), "TT14 thiếu đường kẻ dưới tên Trường, tiêu ngữ bị bắt")
kiem("TT13" in bien("ubnd_dam", dam("UBND")), "TT13 “UBND TỈNH QUẢNG NGÃI” in đậm bị bắt")
kiem("TT15" in bien("ngay_dam", dam("Quảng Ngãi, ngày")), "TT15 dòng địa danh in đậm bị bắt")
kiem("TT16" in bien("can_cu", can_cu_khong_thut), "TT16 đoạn căn cứ không thụt đầu dòng bị bắt")


# 3c. Anh xa 897 Checklist 01 muc 1, 08 muc 4-5 (TT17-TT19)
def bo_ke_trich_yeu(d):
    for p in d.paragraphs[:6]:
        for e in list(p._p.iter()):
            if e.tag in (W_ + "drawing", W_ + "pict") and e.getparent() is not None:
                e.getparent().remove(e)


def co_ubnd_14(d):
    for p in k._doan_trong_bang(d):
        if p.text.strip().startswith("UBND"):
            for r in p.runs:
                r.font.size = Pt(14)


def nguoi_ky(ten, chuc=None):
    def f(d):
        # khoi chu ky: moi doan co chu o cot phai cua moi hang (mau 03A: ho ten o hang 2)
        ps = [p for r in d.tables[-1].rows for p in r.cells[1].paragraphs if p.text.strip()]
        ps[-1].runs[0].text = ten
        if chuc:
            ps[0].runs[0].text = chuc
    return f


def mau_22(dam_phong):
    """Mau 2.2 (van ban cua don vi): TRUONG CAO DANG KON TUM (chu quan, khong dam) / PHONG ... (ban hanh, dam)."""
    def f(d):
        ps = [p for p in d.tables[0].rows[0].cells[0].paragraphs if p.text.strip()]
        ps[0].runs[0].text = "TRƯỜNG CAO ĐẲNG KON TUM"
        for r in ps[0].runs:
            r.bold = False
        ps[1].runs[0].text = "PHÒNG TH-HC&QT"
        for r in ps[1].runs[1:]:
            r.text = ""
        for r in ps[1].runs:
            r.bold = dam_phong
    return f


kiem("TT17" not in bien("m22_dung", mau_22(True)),
     "mẫu 2.2: tên Trường là chủ quản (không đậm) + Phòng đậm → không báo (lỗi báo nhầm BC quá trình 29/9)")
kiem("TT17" in bien("m22_sai", mau_22(False)), "mẫu 2.2: tên Phòng (đơn vị ban hành) không đậm → TT17")


def so_trang_1(d):
    h = d.sections[0].first_page_header
    (h.paragraphs[0] if h.paragraphs else h.add_paragraph()).add_run("1")


kiem("TT11b" in bien("trang1", so_trang_1), "TT11b chữ số “1” ở đầu trang thứ nhất bị bắt (lỗi bản v2 ngày 28/9)")
kiem("TT11b" not in ma(p_dung), "TT11b không báo nhầm văn bản dựng từ khung (ẩn số trang 1)")
kiem("TT18" in bien("ke_ty", bo_ke_trich_yeu), "TT18 thiếu đường kẻ dưới trích yếu bị bắt")
kiem("TT17" in bien("ubnd14", co_ubnd_14), "TT17 tên cơ quan chủ quản cỡ 14 (TB 597: 13) bị bắt")
kiem("TT19" in bien("hoc_ham", nguoi_ky("TS. Nguyễn Văn A")), "TT19 học hàm, học vị trước họ tên người ký bị bắt")
kiem("TT19" in bien("kt_gach", nguoi_ky("Nguyễn Văn A", "K/T HIỆU TRƯỞNG")), "TT19 ký thay “K/T” (hệ Đảng) bị bắt")
kiem("TT19" not in bien("ky_dung", nguoi_ky("Nguyễn Văn A", "KT. HIỆU TRƯỞNG")), "“KT. HIỆU TRƯỞNG” không bị bắt nhầm")
FX = os.path.join(GOC, "92-Kinh-Nghiem", "02-Regression", "Fixtures", "the-thuc",
                  "TB-bang-tieu-de-dung-tay_Cowork_20260928.docx")
m = ma(FX) if os.path.isfile(FX) else None  # Fixtures/ khong len git (.gitignore)
if m is None:
    print("  ⚠ BỎ QUA ca tệp thật Cowork 28/9: không có Fixtures/the-thuc/ trên máy này")
else:
    kiem({"TT12", "TT13", "TT14", "TT15", "TT16", "TT17", "TT18"} <= m,
         f"tệp thật Cowork 28/9 (bảng tiêu đề dựng tay): bắt đủ 7 loại lỗi (được {sorted(m)})")

# 4. Bien the ten TNR -> Muc 3, khong phai Muc 2
d = docx.Document(p_dung)
[p for p in d.paragraphs if p.runs][0].runs[0].font.name = "TimesNewRomanPSMT"
p_bt = os.path.join(TMP, "bienthe.docx")
d.save(p_bt)
kq = k.kiem_tep(p_bt)
kiem(any(x[1] == "TT03b" and x[0] == 3 for x in kq) and not any(x[1] == "TT03" for x in kq),
     "TT03b biến thể TimesNewRomanPSMT chỉ Mức 3")

# 5. xlsx
p_x = os.path.join(TMP, "kh.xlsx")
wb = openpyxl.Workbook()
ws = wb.active
from openpyxl.styles import Font  # noqa: E402
for i in range(1, 6):
    for j in range(1, 9):
        c = ws.cell(i, j, f"ô {i}-{j}")
        c.font = Font(name="Arial", sz=11)
wb.save(p_x)
m = ma(p_x)
kiem("TX02" in m, "TX02 xlsx phông Arial bị bắt (skill xlsx cho phép, KTC thì không)")
for row in ws.iter_rows():
    for c in row:
        c.font = Font(name="Times New Roman", sz=14)
ws.page_setup.paperSize = 9
ws.page_setup.orientation = "landscape"
wb.save(p_x)
kiem(not [x for x in k.kiem_tep(p_x) if x[0] <= 2], "xlsx TNR, A4 ngang đạt")

# 6. tao_tu_mau: .dotx -> .docx mo duoc, giu le
p_mau = os.path.join(TMP, "mau.dotx")
raw = open(p_dung, "rb").read()
open(p_mau, "wb").write(k._doi_kieu(raw, b"wordprocessingml.document.main+xml",
                                     b"wordprocessingml.template.main+xml"))
p_tu_mau = k.tao_tu_mau(p_mau, os.path.join(TMP, "tu_mau.docx"))
d2 = docx.Document(p_tu_mau)
kiem(abs(d2.sections[0].left_margin.cm - 3) < 0.01, "tao_tu_mau giữ lề trái 3 cm của mẫu")

# 7. Hook: trong du an KTC, tep sai -> ma 2; tep dung -> 0; ngoai du an -> 0
HOOK = os.path.join(GOC, "31-Plugin", "scripts", "ktc_the_thuc_hook.py")
du_an = os.path.join(TMP, "du_an")
os.makedirs(os.path.join(du_an, "90-Nhat-Ky-Van-Hanh"))
os.makedirs(os.path.join(du_an, "30-Ket-Qua"))
env = dict(os.environ, USERPROFILE=TMP, HOME=TMP)
os.makedirs(os.path.join(TMP, ".claude"), exist_ok=True)


def chay_hook(tep, cwd):
    vao = json.dumps({"tool_name": "Write", "tool_input": {"file_path": tep}, "cwd": cwd})
    return subprocess.run([sys.executable, HOOK], input=vao.encode(), capture_output=True, env=env)


import shutil  # noqa: E402
t_sai = shutil.copy(p_sai, os.path.join(du_an, "30-Ket-Qua", "sai.docx"))
t_dung = shutil.copy(p_dung, os.path.join(du_an, "30-Ket-Qua", "dung.docx"))
r = chay_hook(t_sai, du_an)
kiem(r.returncode == 2 and "TT08" in r.stderr.decode("utf-8", "ignore"), "hook: tệp sai trong dự án KTC → mã 2, báo TT08")
kiem(chay_hook(t_dung, du_an).returncode == 0, "hook: tệp đúng → mã 0")
kiem(chay_hook(p_sai, TMP).returncode == 0, "hook: ngoài dự án KTC → không can thiệp")

# 8. Mau that tren Drive (neu co)
try:
    import duong_dan
    mau_dir = os.path.join(duong_dan.ktc_database(canh_bao_ban_cu=False), "03-Templates(1)")
except Exception:
    mau_dir = None
if mau_dir and os.path.isdir(mau_dir):
    loi_mau = {}
    for f in sorted(os.listdir(mau_dir)):
        if f.endswith((".dotx", ".xltx")) and not f.startswith(("01-", "10-", "02A-", "06D-", "07-")):  # loi mau da biet (chuan 18 muc 6)
            nang = [x for x in k.kiem_tep(os.path.join(mau_dir, f)) if x[0] <= 2]
            if nang:
                loi_mau[f] = nang
    kiem(not loi_mau, f"11 mẫu 03-Templates(1) (trừ 5 mẫu có lỗi đã biết) không bị báo Mức 1–2: {loi_mau}")
    kiem("TT11b" in ma(os.path.join(mau_dir, "06D-Huong-dan-xay-dung-ke-hoach-bao-cao.dotx")),
         "lỗi đã biết của 06D (số trang ở trang 1) vẫn bị bắt")
    kiem(not [x for x in k.kiem_tep(os.path.join(mau_dir, "06A-Bao-cao-noi-bo.dotx")) if x[0] <= 2],
         "06A (mẫu 2.2: tên Trường là chủ quản, không đậm) không bị báo nhầm")
    for f in ("01-Quyet-dinh-ban-hanh-Quy-che.dotx", "07-To-trinh.dotx"):
        kiem("TT17" in ma(os.path.join(mau_dir, f)), f"lỗi đã biết của {f} (tên Trường sai cỡ/kiểu) vẫn bị bắt")
    kiem("TT08" in ma(os.path.join(mau_dir, "10-Giay-moi.dotx")), "lỗi đã biết của 10-Giay-moi vẫn bị bắt")
    kiem("TT14" in ma(os.path.join(mau_dir, "02A-Quyet-dinh-ca-biet-Phe-duyet-nhiem-vu-du-toan.dotx")),
         "lỗi đã biết của 02A (thiếu đường kẻ dưới tên Trường) vẫn bị bắt")
else:
    print("  -- bỏ qua ca mẫu thật: không đọc được Drive")

print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
