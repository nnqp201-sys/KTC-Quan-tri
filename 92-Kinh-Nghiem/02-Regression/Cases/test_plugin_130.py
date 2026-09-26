# -*- coding: utf-8 -*-
"""Hoi quy plugin 1.3.0 — tiep thu tham dinh doc lap lan 1, lan 2 (C-01, C-03, C-04, R2-01, R2-03, R2-08).

Phan A: guard PreToolUse (ktc_guard.py) — moi nhom co ca CHAN (biet chac phai chan) va ca CHO QUA
        (biet chac phai qua), cong ca fail-closed. Bai hoc LL-20260914-001: phep kiem chi co ca "sach"
        la phep kiem hong.
Phan B: ban dung 31-Plugin/ — 8/8 skill va 7/7 agent co khoi chuan chung, du 6 trang thai; hooks khong
        con backup, co PreToolUse; script backup khong nam trong plugin; plugin.json 1.3.0.
"""
import glob
import io
import json
import os
import subprocess
import sys

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GUARD = os.path.join(GOC, "29-Cong-Cu", "plugin_src", "scripts", "ktc_guard.py")
PLUGIN = os.path.join(GOC, "31-Plugin")
loi = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        loi.append(ten)


def guard(ten_cc, vao=None, raw=None):
    s = raw if raw is not None else json.dumps({"tool_name": ten_cc, "tool_input": vao})
    return subprocess.run([sys.executable, GUARD], input=s, capture_output=True, text=True,
                          encoding="utf-8", timeout=30).returncode


print("== A. ktc_guard.py ==")
DB = "H:/My Drive/KTC-Database/02-KTC-Regulations/1056.docx"
CHAN = [
    ("Write", {"file_path": DB}, "Write vào KTC-Database"),
    ("Edit", {"file_path": r"H:\My Drive\KTC-Database\03-Templates(1)\06A.dotx"}, "Edit mẫu 03-Templates(1) (dấu \\)"),
    ("MultiEdit", {"file_path": "x/04-Good-Documents/a.docx"}, "MultiEdit 04-Good-Documents"),
    ("NotebookEdit", {"notebook_path": "ktc-database/n.ipynb"}, "NotebookEdit (chữ thường)"),
    ("Bash", {"command": f'rm -f "{DB}"'}, "Bash rm"),
    ("Bash", {"command": f'cd /tmp && echo x > "{DB}"'}, "Bash chuyển hướng >"),
    ("Bash", {"command": f'cat a.txt >> "H:/My Drive/KTC-Database/log.txt"'}, "Bash chuyển hướng >>"),
    ("Bash", {"command": f'cp 30-Ket-Qua/a.docx "{DB}"'}, "Bash cp VÀO kho"),
    ("Bash", {"command": f'mv "{DB}" 30-Ket-Qua/'}, "Bash mv RA khỏi kho (xóa nguồn)"),
    ("Bash", {"command": f"sed -i 's/a/b/' \"{DB}\""}, "Bash sed -i"),
    ("PowerShell", {"command": f'Remove-Item -LiteralPath "{DB}"'}, "PowerShell Remove-Item"),
    ("PowerShell", {"command": f'Set-Content -Path "{DB}" -Value x'}, "PowerShell Set-Content"),
    ("PowerShell", {"command": f'Copy-Item a.docx -Destination "{DB}"'}, "PowerShell Copy-Item -Destination vào kho"),
    ("PowerShell", {"command": f'"x" | Out-File "{DB}"'}, "PowerShell Out-File sau ống"),
]
for cc, vao, ten in CHAN:
    kiem(guard(cc, vao) == 2, "chặn: " + ten)

QUA = [
    ("Write", {"file_path": "D:/du-an/30-Ket-Qua/2026-09-26/a.docx"}, "Write vào 30-Ket-Qua"),
    ("Bash", {"command": f'cat "{DB}"'}, "Bash đọc kho"),
    ("Bash", {"command": 'ls "H:/My Drive/KTC-Database" 2>/dev/null | head'}, "Bash liệt kê kho, 2>/dev/null"),
    ("Bash", {"command": f'cp "{DB}" 30-Ket-Qua/ban-sao.docx'}, "Bash cp TỪ kho ra ngoài"),
    ("PowerShell", {"command": f'Copy-Item "{DB}" -Destination 30-Ket-Qua/'}, "PowerShell Copy-Item từ kho ra ngoài"),
    ("Bash", {"command": "python 29-Cong-Cu/kiem_tra_he_thong.py > 30-Ket-Qua/log.txt"}, "Bash ghi log ngoài kho"),
    ("Read", {"file_path": DB}, "Read (không thuộc phạm vi guard)"),
]
for cc, vao, ten in QUA:
    kiem(guard(cc, vao) == 0, "cho qua: " + ten)

kiem(guard(None, raw="khong-phai-json") == 2, "fail-closed: dữ liệu hook hỏng -> chặn")
kiem(guard(None, raw="[1,2]") == 2, "fail-closed: JSON không phải đối tượng -> chặn")

print("== B. Bản dựng 31-Plugin ==")
pj = json.load(io.open(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"), encoding="utf-8"))
kiem(pj.get("version") == "1.3.0", f"plugin.json version 1.3.0 (đang {pj.get('version')})")
kiem("backup" not in pj.get("description", "").lower(), "mô tả plugin không còn nói backup")
hk = io.open(os.path.join(PLUGIN, "hooks", "hooks.json"), encoding="utf-8").read()
kiem("ktc_backup_github" not in hk, "hooks.json không còn gọi backup GitHub")
kiem('"PreToolUse"' in hk and "ktc_guard.py" in hk, "hooks.json có PreToolUse gọi ktc_guard.py")
h = json.loads(hk)
mt = h["hooks"]["PreToolUse"][0]["matcher"]
kiem(all(x in mt.split("|") for x in ("Write", "Edit", "MultiEdit", "NotebookEdit", "Bash", "PowerShell")),
     "matcher guard phủ Write, Edit, MultiEdit, NotebookEdit, Bash, PowerShell")
kiem(not os.path.exists(os.path.join(PLUGIN, "scripts", "ktc_backup_github.py")),
     "script backup KHÔNG nằm trong plugin phân phối")
kiem(os.path.isfile(os.path.join(PLUGIN, "scripts", "ktc_guard.py")), "script guard có trong plugin")

TRANG_THAI = ("DAT", "DAT_CO_DIEU_KIEN", "CAN_BO_SUNG", "CAN_XAC_MINH", "DUNG", "KHONG_DAT")
skills = sorted(glob.glob(os.path.join(PLUGIN, "skills", "*", "SKILL.md")))
agents = sorted(glob.glob(os.path.join(PLUGIN, "agents", "*.md")))
kiem(len(skills) == 8 and len(agents) == 7, f"đủ 8 skill, 7 agent (đang {len(skills)}, {len(agents)})")
for p in skills + agents:
    s = io.open(p, encoding="utf-8").read()
    ten = os.path.relpath(p, PLUGIN)
    du = all(t in s for t in ("<immutable_rules>", "<output_contract>", "<quality_check>")) and \
        all(f"`{t}`" in s for t in TRANG_THAI)
    kiem(du, f"{ten}: có khối chuẩn chung + 6 trạng thái")
    kiem(s.count("<immutable_rules>") == 1, f"{ten}: khối chuẩn chung không bị chèn lặp")
    kiem(s.startswith("---") and s.index("<immutable_rules>") > s.index("---", 3), f"{ten}: khối nằm sau frontmatter")


def yaml_hong(s):
    """Mo ta khong dat ngoac ma chua ': ' -> YAML hong (loi that ktc-kiem-san-pham 19-26/9/2026)."""
    import re
    m = re.search(r"^description:\s*(.*)$", s, re.M)
    tho = m.group(1).strip() if m else ""
    return bool(tho) and not tho.startswith(("'", '"')) and ": " in tho


for p in skills + agents:
    kiem(not yaml_hong(io.open(p, encoding="utf-8").read()), f"{os.path.relpath(p, PLUGIN)}: frontmatter description hợp lệ YAML")
kiem(yaml_hong("---\nname: a\ndescription: Nguoi soan khong tu cham bai: agent nay\n---\n"),
     "ca ngược: mô tả có ': ' không trong ngoặc bị phát hiện")
kiem(not yaml_hong('---\nname: a\ndescription: "co: trong ngoac"\n---\n'), "ca ngược: mô tả trong ngoặc được chấp nhận")

# Ca nguoc cho phep kiem B: mot SKILL.md gia thieu khoi phai bi phat hien
gia = "---\nname: x\ndescription: y\n---\n# X\n## A\n"
kiem(not all(t in gia for t in ("<immutable_rules>", "<output_contract>")), "ca ngược: tệp thiếu khối bị phát hiện")

print("KET LUAN:", "CO LOI " + str(loi) if loi else "SACH")
sys.exit(1 if loi else 0)
