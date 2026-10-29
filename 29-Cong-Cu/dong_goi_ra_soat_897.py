# -*- coding: utf-8 -*-
"""Kiem LOI NGUYEN BAN va dong goi ban tich hop ca nhan "ktc-ra-soat-897 v4.5".

Nguyen tac (LENH-Tich-hop-KTC-Ra-Soat-897-v4.5.md; TB 1206/TB-CDKT muc 6: khong tu y sua doi
bo quy tac cua Skill): LOI v4.5 giu nguyen tung byte; chi duoc them LOP BO SUNG.

Kiem (ma thoat 1 neu sai):
  1. Moi tep loi khop LOI-V45.sha256. Ngoai le DUY NHAT: SKILL.md. Voi SKILL.md: bo dong tieu de
     so 1 va muc "Lop bo sung ca nhan" o cuoi -> phan con lai phai khop TUNG BYTE SKILL.md goc.
  2. Tep ngoai loi chi duoc nam trong references/Bo-Sung-Ca-Nhan/.
  3. Frontmatter SKILL.md co dung 2 khoa `name`, `description`; name = ten thu muc goc.
  4. Moi tep Bo-Sung-Ca-Nhan mo dau bang khoi Nguon / Pham vi + dong co dinh "Ghi chu tham khao".
  5. Goi nguon goc (.skill v4.5 trong 99-Luu-Tru) dung ma bam ghi trong SHA256SUMS.txt.
Sau do dong goi: ktc-ra-soat-897-v4.5-ca-nhan.skill (zip, thu muc goc ktc-ra-soat-897/, lap lai
duoc) + SHA256SUMS canh goi.

Chay:  python 29-Cong-Cu/dong_goi_ra_soat_897.py              # kiem + dong goi
       python 29-Cong-Cu/dong_goi_ra_soat_897.py --chi-kiem   # chi kiem
       python 29-Cong-Cu/dong_goi_ra_soat_897.py --du-an <thu muc>   # du an khac (dung cho ca thu nguoc)
"""
from __future__ import annotations

import hashlib
import os
import re
import sys
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HE = "2A-KTC-Ra-Soat-897"
TEN_SKILL = "ktc-ra-soat-897"
GOI_RA = "ktc-ra-soat-897-v4.5-ca-nhan.skill"
GOC_DIR = os.path.join("99-Luu-Tru", "KTC-Ra-Soat-897-goc")
GOC_SKILL = "ktc-ra-soat-897-v4.5.skill"
LOP_BO_SUNG = "references/Bo-Sung-Ca-Nhan/"
TIEU_DE_TIEN_TO = "# KTC Rà soát 897 — v4.5 (lõi nguyên bản, TB 1206/TB-CĐKT) + lớp bổ sung cá nhân "
MUC_BO_SUNG = "## Lớp bổ sung cá nhân (không thay đổi kết luận v4.5)"
DONG_CO_DINH = "Ghi chú tham khảo — không thay đổi mã, mức, nhãn của v4.5"
BO_QUA_TEP = ("desktop.ini", "Thumbs.db", ".DS_Store")   # tep do Drive / he dieu hanh sinh ra
BO_QUA_THU_MUC = ("__pycache__",)
MOC_ZIP = (2026, 10, 29, 0, 0, 0)                          # mốc cố định → gói lặp lại được


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def doc_loi_sha(du_an: str) -> dict[str, str]:
    p = os.path.join(du_an, HE, "LOI-V45.sha256")
    kq = {}
    with open(p, encoding="utf-8") as f:
        for dong in f:
            dong = dong.rstrip("\r\n")
            if not dong:
                continue
            m = re.match(r"^([0-9a-f]{64})  (.+)$", dong)
            if not m:
                raise ValueError(f"LOI-V45.sha256: dòng sai định dạng: {dong[:80]}")
            kq[m.group(2)] = m.group(1)
    return kq


def liet_ke_tep(goc: str) -> list[str]:
    """Duong dan tuong doi (dau '/') cua moi tep trong thu muc skill, bo tep he thong."""
    ra = []
    for r, ds, fs in os.walk(goc):
        ds[:] = [d for d in ds if d not in BO_QUA_THU_MUC]
        for f in fs:
            if f in BO_QUA_TEP or f.endswith(".pyc"):
                continue
            ra.append(os.path.relpath(os.path.join(r, f), goc).replace(os.sep, "/"))
    return sorted(ra)


def bo_tieu_de_va_muc(skill_md: bytes) -> tuple[bytes | None, str]:
    """Bo dong tieu de so 1 va muc 'Lop bo sung ca nhan' cuoi tep. Tra ve (phan con lai, loi)."""
    txt = skill_md.decode("utf-8")
    mau = "\n" + MUC_BO_SUNG
    if txt.count(mau) != 1:
        return None, f"SKILL.md phải có đúng 1 mục “{MUC_BO_SUNG}” (đang có {txt.count(mau)})"
    i = txt.index(mau)
    phan_muc = txt[i + 1:]
    if re.findall(r"^## ", phan_muc, re.M) != ["## "]:   # muc phai la muc '## ' cuoi cung
        return None, "mục “Lớp bổ sung cá nhân” phải là mục ## cuối cùng của SKILL.md"
    than = txt[:i]                                       # = noi dung goc (ket thuc bang \n)
    dong = than.split("\n")
    # dong tieu de so 1 = dong dau tien bat dau bang '# ' (khong phai '##')
    for k, d in enumerate(dong):
        if d.startswith("# "):
            if not d.startswith(TIEU_DE_TIEN_TO):
                return None, f"dòng tiêu đề số 1 phải bắt đầu bằng “{TIEU_DE_TIEN_TO}”"
            del dong[k]
            return "\n".join(dong).encode("utf-8"), ""
    return None, "SKILL.md không có dòng tiêu đề số 1"


def goc_skill_md(du_an: str) -> tuple[bytes | None, str]:
    """SKILL.md nguyen ban lay thang tu goi .skill goc (da kiem ma bam trong SHA256SUMS.txt)."""
    goc = os.path.join(du_an, GOC_DIR)
    p = os.path.join(goc, GOC_SKILL)
    if not os.path.isfile(p):
        return None, f"thiếu gói gốc {GOC_DIR}/{GOC_SKILL}"
    with open(p, "rb") as f:
        b = f.read()
    ps = os.path.join(goc, "SHA256SUMS.txt")
    if os.path.isfile(ps):
        ghi = None
        with open(ps, encoding="utf-8") as f:
            for dong in f:
                m = re.match(r"^([0-9a-f]{64})\s+\*?(\S.*?)\s*$", dong.strip("\r\n"))
                if m and m.group(2) == GOC_SKILL:
                    ghi = m.group(1)
        if ghi and ghi != sha256(b):
            return None, f"gói gốc {GOC_SKILL} không khớp mã băm ghi trong SHA256SUMS.txt"
    z = zipfile.ZipFile(p)
    try:
        return z.read(f"{TEN_SKILL}/SKILL.md"), ""
    except KeyError:
        return None, f"gói gốc không có {TEN_SKILL}/SKILL.md"


def kiem_loi(du_an: str = DU_AN) -> list[str]:
    """Danh sach loi (rong = loi nguyen ban). Dung chung cho CLI va kiem_tra_he_thong.py (C-897)."""
    loi: list[str] = []
    thu_muc = os.path.join(du_an, HE, TEN_SKILL)
    if not os.path.isdir(thu_muc):
        return [f"thiếu thư mục {HE}/{TEN_SKILL}/"]
    try:
        chuan = doc_loi_sha(du_an)
    except (OSError, ValueError) as e:
        return [f"không đọc được LOI-V45.sha256: {e}"]
    co = liet_ke_tep(thu_muc)
    co_set = set(co)
    # --- 2. tep ngoai loi ---
    for t in co:
        if t not in chuan and not t.startswith(LOP_BO_SUNG):
            loi.append(f"tệp lạ ngoài lõi và ngoài {LOP_BO_SUNG}: {t}")
    # --- 1. loi khop ---
    for t, h in sorted(chuan.items()):
        if t not in co_set:
            loi.append(f"thiếu tệp lõi: {t}")
            continue
        if t == "SKILL.md":
            continue
        with open(os.path.join(thu_muc, *t.split("/")), "rb") as f:
            if sha256(f.read()) != h:
                loi.append(f"tệp lõi bị sửa (lệch mã băm): {t}")
    # --- SKILL.md ---
    p_skill = os.path.join(thu_muc, "SKILL.md")
    if os.path.isfile(p_skill):
        with open(p_skill, "rb") as f:
            moi = f.read()
        goc, e = goc_skill_md(du_an)
        if goc is None:
            loi.append(f"SKILL.md: không có bản gốc để so — {e}")
        else:
            if sha256(goc) != chuan.get("SKILL.md"):
                loi.append("SKILL.md gốc trong gói .skill không khớp mã băm trong LOI-V45.sha256")
            con_lai_moi, e = bo_tieu_de_va_muc(moi)
            if con_lai_moi is None:
                loi.append(f"SKILL.md: {e}")
            else:
                # ban goc khong co muc bo sung: chi can bo dong tieu de so 1 (goc ghi 'v4.4')
                dong_goc = goc.decode("utf-8").split("\n")
                for k, d in enumerate(dong_goc):
                    if d.startswith("# "):
                        del dong_goc[k]
                        break
                con_lai_goc = "\n".join(dong_goc).encode("utf-8")
                if con_lai_moi != con_lai_goc:
                    loi.append("SKILL.md: phần ngoài dòng tiêu đề số 1 và mục “Lớp bổ sung cá nhân” "
                               "KHÔNG khớp từng byte với SKILL.md gốc v4.5")
            # --- 3. frontmatter ---
            txt = moi.decode("utf-8")
            m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
            if not m:
                loi.append("SKILL.md: thiếu frontmatter")
            else:
                khoa = re.findall(r"^([A-Za-z_][\w-]*):", m.group(1), re.M)
                if sorted(khoa) != ["description", "name"]:
                    loi.append(f"SKILL.md: frontmatter phải có đúng 2 khóa name, description (đang có {khoa})")
                mn = re.search(r'^name:\s*"?([^"\n]+)"?\s*$', m.group(1), re.M)
                if not mn or mn.group(1).strip() != TEN_SKILL:
                    loi.append(f"SKILL.md: name phải là “{TEN_SKILL}”")
            # muc bo sung phai dan toi cac tep ton tai
            for ref in sorted(set(re.findall(r"`(\d\d-[\w-]+\.md)`", txt[txt.find(MUC_BO_SUNG):]))):
                if LOP_BO_SUNG + ref not in co_set:
                    loi.append(f"SKILL.md dẫn tới tệp không có: {LOP_BO_SUNG}{ref}")
    else:
        loi.append("thiếu SKILL.md")
    # --- 4. khoi mo dau cac tep bo sung ---
    for t in co:
        if not t.startswith(LOP_BO_SUNG) or not t.endswith(".md"):
            continue
        with open(os.path.join(thu_muc, *t.split("/")), encoding="utf-8") as f:
            dau = f.read(3000)
        for dau_hieu in ("**Nguồn:**", "**Phạm vi:**", DONG_CO_DINH):
            if dau_hieu not in dau:
                loi.append(f"{t}: khối mở đầu thiếu “{dau_hieu}”")
    return loi


def dong_goi(du_an: str = DU_AN) -> str:
    thu_muc = os.path.join(du_an, HE, TEN_SKILL)
    dich = os.path.join(du_an, HE, GOI_RA)
    tep = liet_ke_tep(thu_muc)
    thu_muc_con = sorted({os.path.dirname(t) for t in tep if os.path.dirname(t)}
                         | {os.path.dirname(os.path.dirname(t)) for t in tep
                            if os.path.dirname(os.path.dirname(t))})
    if os.path.exists(dich):
        os.remove(dich)
    with zipfile.ZipFile(dich, "w", zipfile.ZIP_DEFLATED) as z:
        zi = zipfile.ZipInfo(TEN_SKILL + "/", MOC_ZIP)
        zi.external_attr = (0o40755 << 16) | 0x10
        z.writestr(zi, b"")
        for d in thu_muc_con:
            zi = zipfile.ZipInfo(f"{TEN_SKILL}/{d}/", MOC_ZIP)
            zi.external_attr = (0o40755 << 16) | 0x10
            z.writestr(zi, b"")
        for t in tep:
            zi = zipfile.ZipInfo(f"{TEN_SKILL}/{t}", MOC_ZIP)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o100644 << 16
            with open(os.path.join(thu_muc, *t.split("/")), "rb") as f:
                z.writestr(zi, f.read())
    with open(dich, "rb") as f:
        h = sha256(f.read())
    with open(os.path.join(du_an, HE, "SHA256SUMS"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"{h}  {GOI_RA}\n")
    return h


def kiem_goi(du_an: str = DU_AN) -> list[str]:
    """Doc lai chinh tep .skill vua dong: loi khop LOI-V45.sha256, thu muc goc dung."""
    loi = []
    z = zipfile.ZipFile(os.path.join(du_an, HE, GOI_RA))
    chuan = doc_loi_sha(du_an)
    ten = {i.filename[len(TEN_SKILL) + 1:]: i for i in z.infolist()
           if not i.is_dir() and i.filename.startswith(TEN_SKILL + "/")}
    if len(ten) != len([i for i in z.infolist() if not i.is_dir()]):
        loi.append("gói có tệp ngoài thư mục gốc " + TEN_SKILL + "/")
    for t, h in chuan.items():
        if t == "SKILL.md":
            continue
        if t not in ten:
            loi.append(f"gói thiếu tệp lõi {t}")
        elif sha256(z.read(ten[t])) != h:
            loi.append(f"gói: tệp lõi lệch mã băm {t}")
    for t in ten:
        if t not in chuan and not t.startswith(LOP_BO_SUNG) and t != "SKILL.md":
            loi.append(f"gói có tệp lạ {t}")
    return loi


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    du_an = DU_AN
    if "--du-an" in argv:
        du_an = os.path.abspath(argv[argv.index("--du-an") + 1])
    print(f"Kiểm lõi v4.5 nguyên bản — {HE}/{TEN_SKILL}")
    loi = kiem_loi(du_an)
    if loi:
        print(f"✗ {len(loi)} LỖI — KHÔNG đóng gói:")
        for x in loi:
            print("  ✗", x)
        return 1
    n = len(doc_loi_sha(du_an))
    print(f"✓ lõi khớp LOI-V45.sha256 ({n} tệp; SKILL.md: khớp từng byte ngoài tiêu đề số 1 và mục cuối)")
    if "--chi-kiem" in argv:
        return 0
    h = dong_goi(du_an)
    loi = kiem_goi(du_an)
    if loi:
        print(f"✗ gói vừa đóng không đạt ({len(loi)}):")
        for x in loi:
            print("  ✗", x)
        return 1
    print(f"✓ đã đóng {HE}/{GOI_RA}")
    print(f"  SHA256 {h}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
