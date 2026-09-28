# -*- coding: utf-8 -*-
"""Ca thu TU DU cua ban dung plugin (1.3.9) — plugin phai chay duoc ma khong can thu muc du an.

Bai hoc 28/9/2026: Cowork xin them CA thu muc du an vao phien de doc "ban goc"; ban dung thieu goi tu hoc ke hoach (goi
.skill long bi loai), thieu mau dinh tuyen theo doi CV; chuan chung doi ten trong goi -> tim theo ten goc khong thay.

Chay:  python 92-Kinh-Nghiem/02-Regression/Cases/test_tu_du_plugin.py   (can da dung 31-Plugin)
"""
import glob
import os
import re
import sys
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = os.path.join(DU_AN, "31-Plugin")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
loi = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        loi.append(ten)


if not os.path.isdir(os.path.join(P, ".claude-plugin")):
    print("  ⚠ BỎ QUA: chưa dựng 31-Plugin")
    sys.exit(0)
tat = [os.path.relpath(p, P).replace("\\", "/") for p in glob.glob(os.path.join(P, "**", "*"), recursive=True) if os.path.isfile(p)]
ten = {os.path.basename(t) for t in tat}

print("== A. Không có SKILL.md lồng, không còn gói .skill lồng trong zip ==")
skill_md = [t for t in tat if t.endswith("/SKILL.md") and t.count("/") != 2]
kiem(not skill_md, f"chỉ có SKILL.md ở skills/<tên>/ (lồng: {skill_md[:3]})")
z = sorted(glob.glob(os.path.join(DU_AN, "30-Ket-Qua", "*", "Plugin", "ktc-quan-tri-*.zip")), key=os.path.getmtime)[-1]
kiem(not any(n.endswith(".skill") for n in zipfile.ZipFile(z).namelist()), f"zip {os.path.basename(z)} không mang gói .skill lồng")

print("== B. Phần trước chỉ có trong dự án nay có trong gói ==")
for t in ("skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/references/output-contract.md",
          "skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/references/template-format-dna.md",
          "skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/scripts/analyze_plan_templates.py",
          "skills/theo-doi-cv/assets/00-Template-Routing-KTC-Theo-doi-CV.docx",
          "skills/bao-cao/assets/00. Mau bao cao thang (cap Truong).docx",
          "scripts/bc_thang.py", "scripts/ktc_trackchanges.py", "scripts/ktc_thu_muc.py",
          "skills/quan-tri/references/BAN-DO-TEP.md"):
    kiem(t in tat, f"có {t}")

print("== C. Bảng đối chiếu tên tệp ==")
bd = open(os.path.join(P, "skills", "quan-tri", "references", "BAN-DO-TEP.md"), encoding="utf-8").read()
kiem("20-Chuan-Chung/13-Bang-Ma-Don-Vi.md" in bd and "12-Bang-Ma-Don-Vi.md" in bd,
     "bảng đối chiếu: 13-Bang-Ma-Don-Vi (gốc) → 12-Bang-Ma-Don-Vi (trong gói)")
kiem(len(re.findall(r"^\| `20-Chuan-Chung/", bd, re.M)) >= 10, "bảng đối chiếu có ≥ 10 chuẩn chung")
kiem("ktc-ra-soat-897" in bd and "KTC-Database" in bd, "bảng ghi rõ tệp ở plugin 897 và kho KTC-Database")

print("== D. Công cụ .py được kỹ năng, tác tử bảo chạy phải có trong gói ==")
PHAT_TRIEN = {"kiem_tra_he_thong.py", "dong_goi_plugin.py", "dong_goi_kpi.py", "dong_goi_skill.py", "kiem_ho_so.py",
              "trich_danh_muc_qd2119.py", "ktc_backup_github.py", "build_bc2.py", "soffice.py", "x.py"}
thieu = set()
for f in glob.glob(os.path.join(P, "skills", "*", "SKILL.md")) + glob.glob(os.path.join(P, "agents", "*.md")):
    for m in re.finditer(r"python3?\s+[\"']?(?:[^\s\"']*/)?([A-Za-z0-9_]+\.py)", open(f, encoding="utf-8").read()):
        n = m.group(1)
        if n not in ten and n not in PHAT_TRIEN and not n.startswith("test_"):
            thieu.add(f"{os.path.relpath(f, P)} → {n}")
kiem(not thieu, f"mọi lệnh `python …py` trong SKILL.md, tác tử đều có công cụ trong gói (thiếu: {sorted(thieu)[:5]})")

print("== E. Khối đường dẫn, phạm vi tác tử chỉ-dự-án ==")
for f in glob.glob(os.path.join(P, "skills", "*", "SKILL.md")) + glob.glob(os.path.join(P, "agents", "*.md")):
    s = open(f, encoding="utf-8").read()
    kiem("<plugin_paths>" in s and "BAN-DO-TEP.md" in s, f"{os.path.relpath(f, P)}: khối <plugin_paths> trỏ BAN-DO-TEP")
for a in ("ktc-tu-hoc.md", "ktc-tu-cai-tien.md"):
    s = open(os.path.join(P, "agents", a), encoding="utf-8").read()
    kiem("Phạm vi (1.3.9)" in s and "không** xin quyền" in s, f"agents/{a}: ghi rõ chỉ chạy trong dự án, không xin quyền thư mục")

print("== F. Không giữ bản sao bộ quy tắc 897 ==")
dup = [t for t in tat if os.path.basename(t) in ("17-Skill-Kiem-Tra-Tham-Quyen.md", "29-Skill-Van-Ban-Dang.md",
                                                  "02-Noi-Dung.md", "03-Phap-Ly.md", "08-Quy-Uoc-Rieng-CDKT.md")]
kiem(not dup, f"không có tệp của bộ quy tắc 897 trong gói (có: {dup[:3]})")

print("\nKET LUAN:", "SACH" if not loi else f"{len(loi)} ca sai")
sys.exit(1 if loi else 0)
