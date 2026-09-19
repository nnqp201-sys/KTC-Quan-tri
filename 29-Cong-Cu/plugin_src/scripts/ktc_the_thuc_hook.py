# -*- coding: utf-8 -*-
"""PostToolUse hook — tu do the thuc moi tep .docx/.xlsx vua sinh ra (DL-20260919-003).

Chi chay trong du an KTC (co thu muc 90-Nhat-Ky-Van-Hanh o cwd hoac thu muc cha).
Con goi y Muc 1-2 -> in stderr + ma thoat 2 de Claude thay va sua truoc khi giao.
Hook KHONG BAO GIO duoc lam hong phien: moi loi noi bo -> thoat 0 im lang.
"""
import json
import os
import sys
import time

GOC_PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BO_QUA = {".git", "node_modules", "__pycache__", "99-Luu-Tru", "92-Kinh-Nghiem", "31-Plugin",
          "KTC-Database", "_trung_gian"}
MOI = 180          # giay — tep sua trong khoang nay coi la "vua sinh"
TOI_DA_MUC = 25000
TRANG_THAI = os.path.join(os.path.expanduser("~"), ".claude", "ktc_the_thuc_da_do.json")


def goc_du_an(cwd):
    p = os.path.abspath(cwd)
    for _ in range(6):
        if os.path.isdir(os.path.join(p, "90-Nhat-Ky-Van-Hanh")):
            return p
        cha = os.path.dirname(p)
        if cha == p:
            break
        p = cha
    return None


def tep_vua_sinh(goc):
    gio = time.time()
    dem = 0
    for r, ds, fs in os.walk(goc):
        ds[:] = [d for d in ds if d not in BO_QUA and not d.startswith(".")]
        if r[len(goc):].count(os.sep) >= 5:
            ds[:] = []
        for f in fs:
            dem += 1
            if dem > TOI_DA_MUC:
                return
            if f.lower().endswith((".docx", ".xlsx")) and not f.startswith("~$"):
                p = os.path.join(r, f)
                try:
                    if gio - os.path.getmtime(p) <= MOI:
                        yield p
                except OSError:
                    pass


def main():
    try:
        vao = json.load(sys.stdin)
    except Exception:
        return 0
    goc = goc_du_an(vao.get("cwd") or os.getcwd())
    if not goc:
        return 0
    ung_vien = set()
    fp = (vao.get("tool_input") or {}).get("file_path") or ""
    if fp.lower().endswith((".docx", ".xlsx")) and os.path.isfile(fp):
        ung_vien.add(os.path.abspath(fp))
    if vao.get("tool_name") in ("Bash", "PowerShell", "Skill", "Agent"):
        ung_vien.update(os.path.abspath(p) for p in tep_vua_sinh(goc))
    if not ung_vien:
        return 0

    try:
        da_do = json.load(open(TRANG_THAI, encoding="utf-8"))
    except Exception:
        da_do = {}
    sys.path.insert(0, os.path.join(GOC_PLUGIN, "skills", "the-thuc", "scripts"))
    import kiem_the_thuc as k  # noqa: E402

    bao = []
    for p in sorted(ung_vien):
        dau = f"{os.path.getmtime(p):.0f}"
        if da_do.get(p) == dau:
            continue
        try:
            kq = k.kiem_tep(p)
        except Exception:
            continue
        da_do[p] = dau
        nang = [x for x in kq if x[0] <= 2]
        if nang:
            bao.append((p, nang))
    try:
        json.dump(dict(list(da_do.items())[-500:]), open(TRANG_THAI, "w", encoding="utf-8"))
    except Exception:
        pass
    if not bao:
        return 0
    dong = ["KTC the-thuc: tệp vừa sinh CHƯA đạt chuẩn thể thức (20-Chuan-Chung/18-Chuan-The-Thuc-San-Pham.md)."
            " Sửa rồi đo lại bằng kiem_the_thuc.py trước khi giao:"]
    for p, nang in bao:
        dong.append(f"- {os.path.relpath(p, goc)}")
        dong += [f"    [Mức {m}] {ma}: {mt}" for m, ma, mt in nang[:6]]
    sys.stderr.write("\n".join(dong) + "\n")
    return 2


if __name__ == "__main__":
    try:
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8")
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)
