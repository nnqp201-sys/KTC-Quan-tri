# -*- coding: utf-8 -*-
"""Thu nguoc phep kiem 897 cua doctor (plugin 1.4.0).

Su co that 5/11/2026: tai khoan ca nhan cai ktc-ra-soat-897 ban 1.0.3 (23/9/2026) nap bo quy tac
v2.24, trong khi ban chinh thuc toan Truong la v4.6.4. Soan thao va tu kiem im lang dung chuan cu
suot hon mot thang — KHONG co phep kiem nao bao.

Phep kiem moi phai:
  1. BAO THIEU khi khong cai 897        -> "CHƯA CÀI"
  2. BAO CU   khi cai ban v2.24         -> "CŨ"
  3. IM LANG  khi cai dung v4.6.4       -> "✓"
  4. KHONG suy dien phien ban tu TEN THU MUC (bai hoc 18/9/2026) — thu muc ten "v4.6.4" nhung
     noi dung v2.24 thi phai bao CU.
"""
import io
import os
import subprocess
import sys
import tempfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "29-Cong-Cu"))

loi = []


def kiem(ten, dieu_kien, chi_tiet=""):
    print(("  OK " if dieu_kien else "  X  ") + ten + (f"  ({chi_tiet})" if chi_tiet else ""))
    if not dieu_kien:
        loi.append(ten)


def dung_gia_lap(tmp, ten_thu_muc=None, phien_ban=None, kieu="plugin"):
    """Dung cay thu muc gia lap: <tmp>/plugins/<mp>/ktc-quan-tri/{scripts,.claude-plugin}
    va (neu co) <tmp>/plugins/<mp>/<ten_thu_muc> chua bo quy tac 897."""
    mp = os.path.join(tmp, "plugins", "mp")
    qt = os.path.join(mp, "ktc-quan-tri")
    os.makedirs(os.path.join(qt, "scripts"), exist_ok=True)
    os.makedirs(os.path.join(qt, ".claude-plugin"), exist_ok=True)
    os.makedirs(os.path.join(qt, "skills"), exist_ok=True)
    io.open(os.path.join(qt, ".claude-plugin", "plugin.json"), "w", encoding="utf-8").write(
        '{"name":"ktc-quan-tri","version":"1.4.0"}')
    # doctor that tu ban dung
    goc_doctor = os.path.join(DU_AN, "31-Plugin", "scripts", "ktc_quan_tri_doctor.py")
    if not os.path.isfile(goc_doctor):
        raise SystemExit("✗ Chua dung 31-Plugin — chay 29-Cong-Cu/dong_goi_plugin.py truoc")
    noi_dung = io.open(goc_doctor, encoding="utf-8").read()
    io.open(os.path.join(qt, "scripts", "ktc_quan_tri_doctor.py"), "w", encoding="utf-8").write(noi_dung)
    if ten_thu_muc:
        d897 = os.path.join(mp, ten_thu_muc)
        if kieu == "plugin":
            # Cach phat hanh (a) — goi plugin ban cu: phien ban nam trong rules/
            os.makedirs(os.path.join(d897, "rules"), exist_ok=True)
            io.open(os.path.join(d897, "rules", "20-BASELINE.md"), "w", encoding="utf-8").write(
                f"# Bo quy tac KTC-Ra-Soat-897-v{phien_ban}-BASELINE\n")
        else:
            # Cach phat hanh (b) — goi .skill CHINH THUC cua Hieu truong: KHONG co rules/, core/;
            # phien ban khai o tieu de SKILL.md
            os.makedirs(os.path.join(d897, "references", "Quy-Tac-KTC"), exist_ok=True)
            io.open(os.path.join(d897, "SKILL.md"), "w", encoding="utf-8").write(
                "---\nname: \"ktc-ra-soat-897\"\ndescription: \"Ra soat\"\n---\n"
                f"# KTC Rà soát 897 — rà soát dự thảo trước khi trình ký (v{phien_ban}, 03/11/2026)\n")
    return os.path.join(qt, "scripts", "ktc_quan_tri_doctor.py")


def chay(doctor, goc_nd):
    """Chay doctor TRONG CO LAP: CLAUDE_CONFIG_DIR tro vao thu muc tam, de doctor khong doc
    ~/.claude that cua may (may nay dang co 4 ban 897 — se lam moi ca thu sai)."""
    env = dict(os.environ, CLAUDE_CONFIG_DIR=goc_nd)
    r = subprocess.run([sys.executable, doctor], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    return (r.stdout or "") + (r.stderr or "")


print("== Thu nguoc: phep kiem 897 cua doctor ==")

# Ca 1: khong cai 897 -> phai bao CHUA CAI
with tempfile.TemporaryDirectory() as t:
    out = chay(dung_gia_lap(t), t)
    kiem("bắt: chưa cài 897 → báo CHƯA CÀI", "CHƯA CÀI" in out)
    kiem("ca này KHÔNG được báo là bản chính thức", "bản chính thức toàn Trường" not in out)

# Ca 2: cai ban cu v2.24 -> phai bao CU
with tempfile.TemporaryDirectory() as t:
    out = chay(dung_gia_lap(t, "ktc-ra-soat-897", "2.24"), t)
    kiem("bắt: cài v2.24 → báo CŨ", "CŨ" in out and "2.24" in out)
    kiem("nêu rõ bản chính thức phải dùng", "4.6.4" in out)

# Ca 3: cai dung v4.6.4 -> phai IM LANG (khong canh bao)
with tempfile.TemporaryDirectory() as t:
    out = chay(dung_gia_lap(t, "ktc-ra-soat-897", "4.6.4"), t)
    kiem("bỏ qua: cài đúng v4.6.4 → không cảnh báo", "CŨ" not in out and "CHƯA CÀI" not in out)
    kiem("xác nhận là bản chính thức", "bản chính thức toàn Trường" in out)

# Ca 4: ten thu muc noi "v4.6.4" nhung noi dung la v2.24 -> VAN phai bao CU
with tempfile.TemporaryDirectory() as t:
    out = chay(dung_gia_lap(t, "ktc-ra-soat-897-v4.6.4", "2.24"), t)
    kiem("bắt: tên thư mục nói v4.6.4 nhưng nội dung v2.24 → vẫn báo CŨ",
         "CŨ" in out, "không suy diễn phiên bản từ tên tệp")

# Ca 5-6: goi .skill CHINH THUC cua Hieu truong — cau truc KHAC (khong rules/, khong core/),
# phien ban khai o tieu de SKILL.md. Ban dau phep kiem chi doc rules/ nen bao gia "CHUA CAI"
# ngay sau khi nguoi dung cai dung ban v4.6.4 (bat duoc 5/11/2026).
with tempfile.TemporaryDirectory() as t:
    out = chay(dung_gia_lap(t, "ktc-ra-soat-897", "4.6.4", kieu="skill"), t)
    kiem("nhận đúng gói .skill v4.6.4 (không có rules/, core/)",
         "4.6.4" in out and "CHƯA CÀI" not in out and "CŨ" not in out)

with tempfile.TemporaryDirectory() as t:
    out = chay(dung_gia_lap(t, "ktc-ra-soat-897", "4.5", kieu="skill"), t)
    kiem("bắt: gói .skill nhưng là v4.5 → báo CŨ", "CŨ" in out and "4.5" in out)

print()
if loi:
    print("KHONG DAT:", loi)
    sys.exit(1)
print("DAT — phep kiem 897 bat dung ca sai va bo qua dung ca dung")
