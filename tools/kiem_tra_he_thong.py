# -*- coding: utf-8 -*-
"""Kiem tra tinh toan ven toan he hệ thống KTC — TANG 1 (tinh, tat dinh).

Chay: python tools/kiem_tra_he_thong.py
      python tools/kiem_tra_he_thong.py --chi-tiet

Bat dung nhung lop loi DA XAY RA THAT trong qua trinh van hanh, khong phai
loi gia dinh. Moi phep kiem deu ghi ro "da mac ngay nao".

Ma thoat: 0 = khong loi | 1 = co loi | (canh bao khong lam that bai)
"""
from __future__ import annotations

import hashlib
import io
import os
import re
import sys
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NGOAI = os.path.dirname(DU_AN)

# He dang dung -> (thu muc, goi .skill)
HE = {
    "ktc-bao-cao":      ("KTC-Bao-Cao", "KTC-Bao-Cao/ktc-bao-cao-v3.7.skill"),
    "ktc-ke-hoach":     ("KTC-Ke-Hoach", "KTC-Ke-Hoach/ktc-ke-hoach-v3.3.skill"),
    "ktc-soan-thao-vb": ("KTC-Soan-Thao-VB", "KTC-Soan-Thao-VB/ktc-soan-thao-vb-v1.1.skill"),
    "ktc-theo-doi-cv":  ("KTC-Theo-doi-CV", "KTC-Theo-doi-CV/ktc-theo-doi-cv-v1.1.skill"),
    "ktc-quan-tri":     (".", "ktc-quan-tri.skill"),
}
# He da thay the — bo qua, khong bat loi
# KTC-DIS-Tong-Hop-VB da chuyen vao 99-Luu-Tru/He-da-thay-the/ ngay 14/9/2026,
# nen 99-Luu-Tru bao tron no. Giu ten cu trong danh sach de an toan neu ai do
# chuyen nguoc ra.
BO_QUA = ("KTC-DIS-Tong-Hop-VB", "99-Luu-Tru", "__pycache__", ".git")

CHUNG = ["00-Nguyen-Tac-Chung.md", "00-Metadata-Schema.md",
         "04-Nguyen-Tac-Nap-Van-Ban-Tu-Internet.md", "30-Skill-Phan-Loai-6-Truc.md",
         "Skill-Vien-Dan-Van-Ban-Hop-Nhat.md",
         # Ban sao chi co o goi cap du an — van la tep dung chung, van phai khop
         "10-Tu-Dien-Truong-Du-Lieu.md", "11-Quy-Tac-Task-ID.md",
         "12-Vong-Doi-Trang-Thai.md", "13-Bang-Ma-Don-Vi.md"]

# Goi cap du an DOI TEN ban sao cua tep dung chung. Anh xa ten goc -> duong dan
# trong he. He nao khong co ten trong bang thi dung mac dinh
# references/Skill-Library/<ten goc>; tra ve None = he do khong mang tep nay.
DOI_TEN = {
    "ktc-quan-tri": {
        "00-Nguyen-Tac-Chung.md":       "references/01-Nguyen-Tac-Chung.md",
        "30-Skill-Phan-Loai-6-Truc.md": "references/11-Skill-Phan-Loai-6-Truc.md",
        "13-Bang-Ma-Don-Vi.md":         "references/12-Bang-Ma-Don-Vi.md",
        "10-Tu-Dien-Truong-Du-Lieu.md": "references/20-Tu-Dien-Truong-Du-Lieu.md",
        "11-Quy-Tac-Task-ID.md":        "references/21-Quy-Tac-Task-ID.md",
        "12-Vong-Doi-Trang-Thai.md":    "references/22-Vong-Doi-Va-Canh-Bao.md",
    },
}


def duong_dan_chung(ten_he, f):
    """Duong dan tuong doi cua tep dung chung `f` trong he `ten_he`.
    None = he nay khong mang tep do (hop le, khong phai loi)."""
    bang = DOI_TEN.get(ten_he)
    if bang is not None:
        return bang.get(f)
    return f"references/Skill-Library/{f}"

TEN_DA_BO = {
    "ktc-van-ban": "đổi thành ktc-soan-thao-vb (14/9/2026)",
    "ktc-dis-tong-hop-vb": "đã thay bằng ktc-soan-thao-vb (14/9/2026)",
}

# Cum tu ha cap chot chan bat buoc thanh tuy chon
CUM_CAM = [
    (r"897[^.\n]{0,60}(nếu cần|tùy chọn|khuyến nghị)(?![^.\n]{0,40}không phải)",
     "hạ cấp chốt chặn 897 thành tùy chọn"),
    (r"(nếu cần|tùy chọn)[^.\n]{0,40}897(?![^.\n]{0,40}không phải)",
     "hạ cấp chốt chặn 897 thành tùy chọn"),
]

# Neu trong chinh doan khop co tu phu dinh -> KHONG phai vi pham.
# (vd "897 la chot chan bat buoc, KHONG PHAI buoc tuy chon")
MIEN = re.compile(r"không phải|bắt buộc|chốt chặn|không bỏ qua|không được bỏ", re.I)


loi: list[str] = []
canh_bao: list[str] = []
CHI_TIET = "--chi-tiet" in sys.argv


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


def doc(p):
    return io.open(p, encoding="utf-8", errors="ignore").read()


def cac_tep_md(goc):
    for r, ds, fs in os.walk(goc):
        ds[:] = [d for d in ds if d not in BO_QUA]
        for f in fs:
            if f.endswith((".md", ".py")):
                yield os.path.join(r, f)


def tieu_de(s):
    print(f"\n{'─' * 76}\n{s}\n{'─' * 76}")


# --------------------------------------------------------------- C1
def c1_goi():
    tieu_de("C1. Gói .skill — cấu trúc và frontmatter")
    for ten, (thu_muc, goi) in HE.items():
        p = os.path.join(DU_AN, goi)
        if not os.path.exists(p):
            loi.append(f"C1 {ten}: KHÔNG có gói {goi}")
            print(f"  ✗ {ten:18s} thiếu gói"); continue
        z = zipfile.ZipFile(p)
        ds = [x for x in z.namelist() if not x.endswith("/")]
        v = []
        if z.testzip():
            v.append("zip hỏng")
        roots = {x.split("/")[0] for x in ds}
        if roots != {ten}:
            v.append(f"thư mục gốc {roots} ≠ name '{ten}'")
        tu = [x for x in ds if x.endswith(".skill")]
        if tu:
            v.append(f"gói tự chứa chính nó ({len(tu)} tệp)")
        try:
            s = z.read(f"{ten}/SKILL.md").decode("utf-8")
        except KeyError:
            v.append("thiếu SKILL.md"); s = ""
        if s:
            m = re.match(r"^---\r?\n(.*?)\r?\n---", s, re.S)
            if not m:
                v.append("thiếu YAML frontmatter")
            else:
                fm = m.group(1)
                khoa = set(re.findall(r"^([A-Za-z_-]+):", fm, re.M))
                if khoa != {"name", "description"}:
                    v.append(f"khóa frontmatter = {khoa}, phải đúng name+description")
                mn = re.search(r'^name:\s*"?([^"\n]+)"?', fm, re.M)
                if mn and mn.group(1).strip() != ten:
                    v.append(f"name='{mn.group(1).strip()}' ≠ '{ten}'")
                md_ = re.search(r'^description:\s*"(.+?)"\s*$', fm, re.M | re.S)
                if not md_:
                    v.append("description thiếu hoặc không đặt trong dấu nháy kép")
                elif len(md_.group(1)) > 1024:
                    v.append(f"description {len(md_.group(1))} ký tự > 1024")
        if v:
            loi.extend(f"C1 {ten}: {x}" for x in v)
            print(f"  ✗ {ten:18s} {' · '.join(v)}")
        else:
            print(f"  ✓ {ten:18s} {len(ds)} tệp, hợp lệ")


# --------------------------------------------------------------- C2
def c2_lien_ket():
    tieu_de("C2. Liên kết trong gói — đường dẫn references/ có tồn tại không")
    for ten, (_, goi) in HE.items():
        p = os.path.join(DU_AN, goi)
        if not os.path.exists(p):
            continue
        z = zipfile.ZipFile(p)
        co = {x.split("/", 1)[1] for x in z.namelist() if "/" in x}
        thieu = set()
        for n in z.namelist():
            if not n.endswith(".md"):
                continue
            s = z.read(n).decode("utf-8", "ignore")
            for m in re.findall(r"`(references/[A-Za-z0-9_./()-]+\.(?:md|py))`", s):
                if m not in co:
                    thieu.add(f"{n.split('/')[-1]} → {m}")
        if thieu:
            loi.extend(f"C2 {ten}: {x}" for x in sorted(thieu))
            print(f"  ✗ {ten:18s} {len(thieu)} liên kết gãy")
            for x in sorted(thieu)[:5]:
                print(f"      {x}")
        else:
            print(f"  ✓ {ten:18s} không có liên kết gãy")


# --------------------------------------------------------------- C3
def c3_duong_dan_du_an():
    tieu_de("C3. Đường dẫn nêu trong tài liệu cấp dự án có thật không")
    for f in ["CLAUDE.md", "00-README.md", "SKILL.md",
              "01-Chuan-Chung/00-README.md", "03-Nhat-Ky-Van-Hanh/MEMORY-INDEX.md"]:
        p = os.path.join(DU_AN, f)
        if not os.path.exists(p):
            canh_bao.append(f"C3: không có {f}")
            continue
        s = doc(p)
        thieu = []
        for m in re.findall(r"`([0-9A-Za-zĐ][A-Za-z0-9ĐÀ-ỹ_./()&-]*\.(?:md|py|xlsx|docx|skill))`", s):
            if "/" not in m:
                continue
            if not os.path.exists(os.path.join(DU_AN, m)) and \
               not os.path.exists(os.path.join(NGOAI, m)):
                thieu.append(m)
        if thieu:
            canh_bao.extend(f"C3 {f}: không tìm thấy `{x}`" for x in sorted(set(thieu)))
            print(f"  ⚠ {f:40s} {len(set(thieu))} đường dẫn không tìm thấy")
            if CHI_TIET:
                for x in sorted(set(thieu)):
                    print(f"      {x}")
        else:
            print(f"  ✓ {f:40s} mọi đường dẫn đều tồn tại")


# --------------------------------------------------------------- C4
def c4_nguon_roi_vs_goi():
    """Đã mắc 14/9/2026: gói chứa Skill 33 v3.0 còn nguồn rời chỉ v2.3."""
    tieu_de("C4. Nguồn rời ↔ nội dung trong gói (gói CÓ THỂ mới hơn nguồn rời)")
    for ten, (thu_muc, goi) in HE.items():
        p = os.path.join(DU_AN, goi)
        if not os.path.exists(p):
            continue
        z = zipfile.ZipFile(p)
        lech = []
        for n in z.namelist():
            if n.endswith("/"):
                continue
            rel = n.split("/", 1)[1]
            f = os.path.join(DU_AN, thu_muc, rel)
            if not os.path.exists(f):
                lech.append(f"{rel} — chỉ có trong gói"); continue
            if hashlib.md5(z.read(n)).hexdigest() != md5(f):
                a, b = len(z.read(n)), os.path.getsize(f)
                lech.append(f"{rel} — gói {a}b ≠ rời {b}b "
                            f"({'GÓI mới hơn?' if a > b else 'rời mới hơn?'})")
        if lech:
            canh_bao.extend(f"C4 {ten}: {x}" for x in lech)
            print(f"  ⚠ {ten:18s} {len(lech)} tệp lệch — KHÔNG ghi đè, phải GỘP")
            for x in lech[:6]:
                print(f"      {x}")
        else:
            print(f"  ✓ {ten:18s} đồng bộ hoàn toàn")


# --------------------------------------------------------------- C5
def _noi_dung_goi(goi_rel):
    """Tra ve {duong_dan_trong_goi: (md5, so_byte)} cua mot .skill."""
    p = os.path.join(DU_AN, goi_rel)
    if not os.path.exists(p):
        return {}
    with zipfile.ZipFile(p) as z:
        ra = {}
        for n in z.namelist():
            if n.endswith("/") or "/" not in n:
                continue
            b = z.read(n)
            ra[n.split("/", 1)[1]] = (hashlib.md5(b).hexdigest(), len(b))
    return ra


def c5_tep_dung_chung():
    """C5 v2 (14/9/2026) — soi CẢ bản rời LẪN bản nằm trong .skill.

    Đã mắc: C5 v1 chỉ so bản rời nên in "khớp ở mọi hệ" trong khi 3/5 tệp dùng
    chung bên trong gói là bản cũ — 30-Skill-Phan-Loai-6-Truc.md gốc 9.034 B
    mà trong ktc-bao-cao-v3.5.skill chỉ 4.515 B, gọi Trục 4 bằng tên cũ.
    Bản rời KHÔNG phải thứ chạy trên Chat/Cowork; gói mới là. Vì vậy:
      lệch ở bản rời      -> cảnh báo (còn kịp sửa trước khi đóng gói)
      lệch ở trong gói    -> LỖI (đang chạy sai thật)
    """
    tieu_de("C5. 5 tệp dùng chung — khớp bản gốc 01-Chuan-Chung "
            "(soi cả bản rời lẫn bản TRONG GÓI)")
    goi_ct = {ten: _noi_dung_goi(goi) for ten, (_, goi) in HE.items()}
    for f in CHUNG:
        goc = os.path.join(DU_AN, "01-Chuan-Chung", f)
        if not os.path.exists(goc):
            loi.append(f"C5: thiếu bản gốc 01-Chuan-Chung/{f}")
            print(f"  ✗ {f[:44]:46s} THIẾU BẢN GỐC"); continue
        h = md5(goc); n_goc = os.path.getsize(goc)
        nhe, nang, trong_goi = [], [], 0
        for ten, (thu_muc, _) in HE.items():
            rel = duong_dan_chung(ten, f)
            if rel is None:      # he nay khong mang tep dung chung do
                continue
            d = os.path.join(DU_AN, thu_muc, *rel.split("/"))
            g = goi_ct.get(ten, {}).get(rel)
            # Vang mat o CA HAI noi = he nay khong dung tep do. Hop le, bo qua.
            if g is None and not os.path.exists(d):
                continue
            if not os.path.exists(d):
                nhe.append(f"{ten}: rời không có")
            elif md5(d) != h:
                nhe.append(f"{ten}: rời LỆCH")
            # Co ban roi nhung khong nam trong goi cung la hop le.
            if g is None:
                continue
            trong_goi += 1
            if g[0] != h:
                nang.append(f"{ten}: TRONG GÓI lệch ({g[1]}b ≠ gốc {n_goc}b)")
        if nang:
            loi.extend(f"C5 {f}: {x}" for x in nang)
            print(f"  ✗ {f[:44]:46s} {' · '.join(nang)}")
        if nhe:
            canh_bao.extend(f"C5 {f}: {x}" for x in nhe)
            print(f"  ⚠ {f[:44]:46s} {' · '.join(nhe)}")
        if not nang and not nhe:
            print(f"  ✓ {f[:44]:46s} khớp ở mọi bản rời"
                  f"{f' và {trong_goi} gói' if trong_goi else ' (không gói nào mang tệp này)'}")


# --------------------------------------------------------------- C6
def c6_ten_he_da_bo():
    """Đã mắc 14/9/2026: skill trỏ tới ktc-van-ban — hệ không còn tồn tại."""
    tieu_de("C6. Tên hệ đã bỏ còn sót (định tuyến gãy)")
    thay = {}
    for ten, (thu_muc, goi) in HE.items():
        p = os.path.join(DU_AN, goi)
        if not os.path.exists(p):
            continue
        z = zipfile.ZipFile(p)
        for n in z.namelist():
            if not n.endswith((".md", ".py")):
                continue
            s = z.read(n).decode("utf-8", "ignore")
            for cu, ghi in TEN_DA_BO.items():
                # Chi tinh la loi khi dung lam DICH DEN dinh tuyen ("dung X",
                # "chuyen sang X", "-> X") hoac nam trong frontmatter.
                # Nhac lai lich su ("ke thua tu X", "tien le: X") la hop le.
                dinh_tuyen = re.search(
                    rf"(dùng|dung|chuyển sang|chuyen sang|chuyển qua|gọi|goi|→|->)\s*`?{cu}", s, re.I)
                trong_fm = n.endswith("SKILL.md") and cu in s.split("---")[1].lower()
                if dinh_tuyen or trong_fm:
                    thay.setdefault((ten, cu, ghi), []).append(n.split("/")[-1])
    if thay:
        for (ten, cu, ghi), fs in sorted(thay.items()):
            loi.append(f"C6 {ten}: còn '{cu}' ({ghi}) ở {', '.join(sorted(set(fs)))}")
            print(f"  ✗ {ten:18s} còn '{cu}' ở {len(set(fs))} tệp — {ghi}")
            for x in sorted(set(fs)):
                print(f"      {x}")
    else:
        print("  ✓ không hệ nào còn trỏ tới tên đã bỏ")


# --------------------------------------------------------------- C7
def c7_cum_cam():
    """Đã mắc 14/9/2026: 897 bị ghi là 'nếu cần' ở 4 chỗ."""
    tieu_de("C7. Cụm từ hạ cấp chốt chặn bắt buộc")
    n = 0
    for goc in [DU_AN] + [os.path.join(DU_AN, t) for t, _ in HE.values()]:
        for p in cac_tep_md(goc):
            if any(b in p for b in BO_QUA):
                continue
            # Bo kiem va bo thu nguoc chua chinh cac mau sai lam DU LIEU THU
            if (os.path.basename(p) == "kiem_tra_he_thong.py"
                    or "02-Regression" in p):
                continue
            s = doc(p)
            for rx, mo_ta in CUM_CAM:
                for m in re.finditer(rx, s, re.I):
                    if MIEN.search(m.group(0)):
                        continue
                    rel = os.path.relpath(p, DU_AN)
                    loi.append(f"C7 {rel}: {mo_ta} — “{m.group(0)[:60]}”")
                    print(f"  ✗ {rel}\n      “{m.group(0)[:70]}”")
                    n += 1
    if not n:
        print("  ✓ không có chỗ nào hạ cấp 897 thành tùy chọn")


# --------------------------------------------------------------- C8
def c8_sao_chep_cheo_he():
    """Đã mắc: Tong-Hop-VB chép checklist 897, sau 1 tháng lệch 28/28 tệp."""
    tieu_de("C8. Sao chép chéo hệ — tệp trùng tên khác nội dung")
    kho = {}
    ngoai = {"ktc-ra-soat-897": os.path.join(NGOAI, "KTC-Ra-Soat-897-v2-Cai-tien", "references"),
             "ktc-database": os.path.join(NGOAI, "KTC-Database", "references")}
    for ten, (thu_muc, _) in HE.items():
        kho[ten] = os.path.join(DU_AN, thu_muc, "references")
    kho.update({k: v for k, v in ngoai.items() if os.path.isdir(v)})

    idx = {}
    for he, d in kho.items():
        if not os.path.isdir(d):
            continue
        for r, _, fs in os.walk(d):
            for f in fs:
                if f == "desktop.ini":
                    continue
                idx.setdefault(f, []).append((he, os.path.join(r, f)))
    lech = []
    for f, ds in sorted(idx.items()):
        if f in CHUNG:
            continue
        # Moi he lay 1 dai dien; trung ten TRONG CUNG mot he la chuyen binh
        # thuong (vd 01-Soan-Thao.md co o moi thu muc nghiep vu) — bo qua.
        dai_dien = {}
        for he, p in ds:
            dai_dien.setdefault(he, p)
        if len(dai_dien) < 2:
            continue
        hs = {md5(p) for p in dai_dien.values()}
        if len(hs) > 1:
            lech.append((f, list(dai_dien),
                         {he: os.path.getsize(p) for he, p in dai_dien.items()}))
    if lech:
        print(f"  ⚠ {len(lech)} tệp trùng tên nhưng KHÁC nội dung giữa các hệ:")
        for f, hes, sz in lech[:12]:
            print(f"      {f[:44]:46s} {' · '.join(f'{h}={sz[h]}b' for h in hes)}")
        canh_bao.extend(f"C8 {f}: lệch giữa {', '.join(h)}" for f, h, _ in lech)
        print("    → Bản sao không có cơ chế đồng bộ chắc chắn sẽ lệch. Trỏ tới bản gốc.")
    else:
        print("  ✓ không có tệp trùng tên khác nội dung giữa các hệ")


# --------------------------------------------------------------- C9
def c9_cong_cu():
    tieu_de("C9. Công cụ Python — import và tự kiểm")
    sys.path.insert(0, os.path.join(DU_AN, "tools"))
    for mod, ham in [("ktc_trackchanges", "kiem_tra"), ("vanphong", "cap_truong"),
                     ("noi_ham", "trich"), ("dong_goi_skill", "kiem_frontmatter")]:
        try:
            m = __import__(mod)
            assert hasattr(m, ham), f"thiếu hàm {ham}()"
            print(f"  ✓ {mod:20s} import được, có {ham}()")
        except Exception as e:
            loi.append(f"C9 {mod}: {e}")
            print(f"  ✗ {mod:20s} {e}")
    # kiem tra thuc: chuyen van phong
    try:
        from vanphong import cap_truong, kiem_tra as kt
        ca = [("tham mưu cho Lãnh đạo Trường ban hành Quy chế", "ban hành"),
              ("Khoa tiếp tục triển khai kế hoạch", "Nhà trường"),
              ("Ban hành Kế hoạch triển khai", "Ban hành")]
        sai = [(a, cap_truong(a)) for a, b in ca if b not in cap_truong(a)]
        sai += [(a, r) for a in [x for x, _ in ca] for r in [cap_truong(a)] if kt(r)]
        if sai:
            loi.append(f"C9 vanphong: {len(sai)} ca thử sai")
            print(f"  ✗ vanphong: {len(sai)} ca thử SAI")
            for a, r in sai:
                print(f"      “{a}” → “{r}”")
        else:
            print(f"  ✓ vanphong: {len(ca)}/{len(ca)} ca thử đạt")
    except Exception as e:
        loi.append(f"C9 vanphong self-test: {e}")


# --------------------------------------------------------------- C10
def c10_regression():
    tieu_de("C10. Bộ hồi quy có chạy được không")
    d = os.path.join(DU_AN, "99-Kinh-Nghiem", "02-Regression", "Cases")
    cs = sorted(f for f in os.listdir(d) if f.startswith("test_")) if os.path.isdir(d) else []
    if not cs:
        canh_bao.append("C10: chưa có ca hồi quy nào")
        print("  ⚠ chưa có ca hồi quy nào trong 02-Regression/Cases/")
        return
    import subprocess
    for f in cs:
        r = subprocess.run([sys.executable, os.path.join(d, f)],
                           capture_output=True, text=True, cwd=DU_AN)
        if r.returncode == 0:
            print(f"  ✓ {f:34s} chạy xong (mã 0)")
        else:
            loi.append(f"C10 {f}: mã thoát {r.returncode}")
            print(f"  ✗ {f:34s} mã {r.returncode}: {(r.stderr or '')[-160:]}")


def c11_ban_goc_trong_zip():
    """Đã mắc 14/9/2026: 9 tệp tri thức gốc của ktc-quan-tri (~490 dòng — đối
    chiếu ba hệ, chốt kỳ, quy đổi KPI) chỉ tồn tại BÊN TRONG ktc-quan-tri.skill.
    Không có bản sao ở đâu khác. Sửa một quy tắc phải giải nén ra; tệp .skill
    hỏng hoặc mất trên Drive là mất trắng phần tri thức đó.
    Quy ước của dự án là bản gốc nằm ở thư mục nguồn, gói chỉ là bản đóng."""
    tieu_de("C11. Không tệp nào chỉ tồn tại bên trong gói .skill")
    for ten, (thu_muc, goi) in HE.items():
        p = os.path.join(DU_AN, goi)
        if not os.path.exists(p):
            continue
        z = zipfile.ZipFile(p)
        mo_coi = []
        for n in z.namelist():
            if n.endswith("/") or "/" not in n:
                continue
            rel = n.split("/", 1)[1]
            if not os.path.exists(os.path.join(DU_AN, thu_muc, *rel.split("/"))):
                mo_coi.append(rel)
        if mo_coi:
            canh_bao.extend(f"C11 {ten}: {x} chỉ có trong zip" for x in mo_coi)
            print(f"  ⚠ {ten:18s} {len(mo_coi)} tệp không có bản nguồn ngoài zip")
            for x in mo_coi[:6]:
                print(f"      {x}")
        else:
            print(f"  ✓ {ten:18s} mọi tệp đều có bản nguồn ngoài zip")


def main():
    print("=" * 76)
    print("KIỂM TRA TOÀN HỆ hệ thống KTC — Tầng 1 (tĩnh, tất định)")
    print(f"Dự án: {DU_AN}")
    print("=" * 76)
    for f in (c1_goi, c2_lien_ket, c3_duong_dan_du_an, c4_nguon_roi_vs_goi,
              c5_tep_dung_chung, c6_ten_he_da_bo, c7_cum_cam,
              c8_sao_chep_cheo_he, c9_cong_cu, c11_ban_goc_trong_zip,
              c10_regression):
        try:
            f()
        except Exception as e:
            loi.append(f"{f.__name__} NGOẠI LỆ: {e}")
            print(f"  ✗ {f.__name__} ngoại lệ: {e}")
    print("\n" + "=" * 76)
    print(f"KẾT LUẬN: {len(loi)} LỖI · {len(canh_bao)} cảnh báo")
    print("=" * 76)
    if loi:
        print("\nLỖI — phải sửa:")
        for x in loi:
            print("  ✗", x)
    # Da mac 14/9/2026: mot viec dang chan nam lan trong 73 dong canh bao ma
    # nguoi chay khong bat buoc mo --chi-tiet ra xem. In phan bo theo phep kiem
    # de khoi lung nao phinh to thi nhin thay ngay.
    if canh_bao:
        dem = {}
        for x in canh_bao:
            dem[x.split(":")[0].split()[0]] = dem.get(x.split(":")[0].split()[0], 0) + 1
        print("\nPhân bố cảnh báo: "
              + " · ".join(f"{k}={v}" for k, v in sorted(dem.items())))
    if canh_bao and CHI_TIET:
        print("\nCẢNH BÁO — xem xét:")
        for x in canh_bao:
            print("  ⚠", x)
    elif canh_bao:
        print(f"\n({len(canh_bao)} cảnh báo — chạy với --chi-tiet để xem)")
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
