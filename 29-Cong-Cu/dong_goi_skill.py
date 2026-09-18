# -*- coding: utf-8 -*-
"""Dong goi lai .skill cho KTC-Bao-Cao va KTC-Ke-Hoach + kiem tra hop le.

Xu ly luon KI-005: hop nhat hai nhanh ktc-bao-cao thanh MOT goi v3.5
  - nen  = v3.4 (co Skill 31 doc Excel TB736, xac dinh cap bao cao, 6 skill chuyen biet)
  - cong = lop references/Memory/ + assets/ cua nhanh v2.5.1-memory
  - cong = cac tep nguon da sua 14/9/2026

QUY TAC: nguon roi va noi dung trong goi KHONG mac nhien dong bo.
Truoc khi ghi de, phai so tung tep; tep nao trong goi moi hon thi GOP, khong ghi de.
"""
import io, os, re, shutil, sys, tempfile, zipfile

DU_AN = r"D:\.CLAUDE code\KTC-Quan-tri"


def giai_nen(skill: str, dich: str) -> str:
    with zipfile.ZipFile(skill) as z:
        z.extractall(dich)
    return os.path.join(dich, os.listdir(dich)[0])


def kiem_frontmatter(skill_md: str) -> list:
    """Tra ve danh sach loi. Yeu cau: dung 2 khoa name + description."""
    s = io.open(skill_md, encoding="utf-8").read()
    loi = []
    m = re.match(r"^---\r?\n(.*?)\r?\n---", s, re.S)
    if not m:
        return ["Thiếu YAML frontmatter"]
    fm = m.group(1)
    khoa = re.findall(r"^([A-Za-z_-]+):", fm, re.M)
    if set(khoa) != {"name", "description"}:
        loi.append(f"Khóa frontmatter phải đúng name+description, đang có {khoa}")
    mn = re.search(r'^name:\s*"?([^"\n]+)"?', fm, re.M)
    if not mn:
        loi.append("Thiếu name")
    else:
        ten = mn.group(1).strip()
        if not re.fullmatch(r"[a-z0-9-]{1,64}", ten):
            loi.append(f"name không hợp lệ: {ten!r}")
    md = re.search(r'^description:\s*"?(.+?)"?\s*$', fm, re.M | re.S)
    if not md:
        loi.append("Thiếu description")
    elif len(md.group(1)) > 1024:
        loi.append(f"description dài {len(md.group(1))} > 1024")
    return loi


def kiem_lien_ket(goc: str) -> list:
    """Kiem moi duong dan references/... duoc nhac trong .md co ton tai khong."""
    co = set()
    for r, _, fs in os.walk(goc):
        for f in fs:
            co.add(os.path.relpath(os.path.join(r, f), goc).replace("\\", "/"))
    thieu = []
    for r, _, fs in os.walk(goc):
        for f in fs:
            if not f.endswith(".md"):
                continue
            s = io.open(os.path.join(r, f), encoding="utf-8", errors="ignore").read()
            for m in re.findall(r"`(references/[A-Za-z0-9_./()-]+\.(?:md|py))`", s):
                if m not in co:
                    thieu.append(f"{f} -> {m}")
    return sorted(set(thieu))


def dong_goi(goc: str, out: str, ten_goc: str = None) -> str:
    """ten_goc = ten thu muc goc trong zip. PHAI trung voi `name` cua frontmatter."""
    if ten_goc is None:
        ten_goc = os.path.basename(goc)
    if os.path.exists(out):
        os.remove(out)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for r, _, fs in os.walk(goc):
            for f in sorted(fs):
                # Bo qua chinh goi .skill — neu khong, goi se tu chua ban cu cua no
                if (f in ("desktop.ini", ".DS_Store") or f.endswith(".pyc")
                        or f.endswith(".skill")):
                    continue
                p = os.path.join(r, f)
                z.write(p, os.path.join(ten_goc, os.path.relpath(p, goc)))
    return out


def sao_nguon(goc: str, thu_muc_nguon: str, tep: list) -> list:
    """Chep tep nguon roi vao goi. Tra ve nhat ky."""
    nk = []
    for t in tep:
        src = os.path.join(DU_AN, thu_muc_nguon, t)
        dst = os.path.join(goc, t)
        if not os.path.exists(src):
            nk.append(f"  ! KHÔNG có nguồn rời: {t}")
            continue
        cu = os.path.getsize(dst) if os.path.exists(dst) else 0
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
        nk.append(f"  ✓ {t.split('/')[-1][:46]:48s} {cu} → {os.path.getsize(dst)} byte")
    return nk


def bao_cao(goc: str, out: str):
    loi = kiem_frontmatter(os.path.join(goc, "SKILL.md"))
    thieu = kiem_lien_ket(goc)
    n = sum(len(fs) for _, _, fs in os.walk(goc))
    with zipfile.ZipFile(out) as z:
        roots = {x.split("/")[0] for x in z.namelist()}
        sl = len(z.namelist())
    sk = os.path.getsize(os.path.join(goc, "SKILL.md"))
    tong = sum(os.path.getsize(os.path.join(r, f))
               for r, _, fs in os.walk(goc) for f in fs)
    print(f"  frontmatter      : {'HỢP LỆ' if not loi else loi}")
    print(f"  liên kết gãy     : {len(thieu)} {thieu[:4] if thieu else ''}")
    print(f"  thư mục gốc duy nhất: {roots}")
    print(f"  {n} tệp → {sl} mục trong zip | {os.path.getsize(out)//1024} KB")
    print(f"  Progressive Disclosure: SKILL.md {sk} / {tong} byte = {100*sk/tong:.1f}%")
    return not loi and not thieu
