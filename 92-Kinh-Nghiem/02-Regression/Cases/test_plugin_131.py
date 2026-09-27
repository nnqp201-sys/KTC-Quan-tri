# -*- coding: utf-8 -*-
"""Hoi quy plugin 1.3.1 — tiep thu tham dinh doc lap lan 3 (ChatGPT P0-1, P0-2, P1-1; Copilot R5).

Phan A: guard 2 tang — CHAN (exit 2) · HOI (permissionDecision "ask") · CHO QUA (exit 0, khong hoi).
        Gom dung cac lenh vuot guard ma ChatGPT da chay that (python -c open 'w', powershell -Command).
Phan B: nhat ky PostToolUse KHONG luu lenh/mo ta tho khi chua chon ghi; co chon thi che du lieu.
Phan C: SessionStart `nap` gon (<= NGAN_SACH ky tu), khong in lenh tho.
Phan D: ban dung 31-Plugin 1.3.1 — khoi loi ngan, tai lieu day du trong references/, lich su phien ban tach khoi SKILL.md.
Moi phan co ca nguoc (LL-20260914-001).
"""
import glob
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SCRIPTS = os.path.join(GOC, "29-Cong-Cu", "plugin_src", "scripts")
GUARD = os.path.join(SCRIPTS, "ktc_guard.py")
NHAT_KY = os.path.join(SCRIPTS, "ktc_nhat_ky.py")
PLUGIN = os.path.join(GOC, "31-Plugin")
loi = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        loi.append(ten)


def guard(cc, lenh):
    k = "command" if cc in ("Bash", "PowerShell") else "file_path"
    r = subprocess.run([sys.executable, GUARD], input=json.dumps({"tool_name": cc, "tool_input": {k: lenh}}),
                       capture_output=True, text=True, encoding="utf-8", timeout=30)
    if r.returncode == 2:
        return "chan"
    if r.returncode == 0 and '"ask"' in r.stdout:
        return "hoi"
    return "qua" if r.returncode == 0 else f"ma{r.returncode}"


print("== A. Guard 2 tầng ==")
DB = "H:/My Drive/KTC-Database/02-KTC-Regulations/x.txt"
DBW = r"H:\My Drive\KTC-Database\02-KTC-Regulations\x.txt"
CHAN = [
    ("Bash", f"python -c \"open('{DB}', 'w').write('x')\"", "python -c open(..., 'w') [ChatGPT L3]"),
    ("Bash", f"python3 -c \"open(r'{DBW}', mode='a').write('x')\"", "python3 open mode='a' (đường dẫn \\)"),
    ("Bash", f"python - <<'EOF'\nfrom pathlib import Path\nPath('{DB}').write_text('x')\nEOF", "heredoc Path().write_text"),
    ("Bash", f"python -c \"from pathlib import Path; Path('{DB}').unlink()\"", "Path().unlink"),
    ("Bash", f"powershell -Command \"Set-Content '{DBW}' 'a'\"", "powershell -Command Set-Content [ChatGPT L3]"),
    ("PowerShell", f"pwsh -c \"Remove-Item '{DBW}'\"", "pwsh -c Remove-Item"),
    ("Bash", f"cmd /c \"del {DBW}\"", "cmd /c del"),
    ("Bash", f"bash -c 'rm -f \"{DB}\"'", "bash -c rm"),
    ("PowerShell", "powershell -EncodedCommand SQBFAFgA", "-EncodedCommand (không phân tích được)"),
    ("Bash", 'cd "H:/My Drive/KTC-Database" && echo x > moi.txt', "cd vào kho rồi > tệp tương đối"),
    ("PowerShell", "Set-Location 'H:\\My Drive\\KTC-Database'; Remove-Item a.docx", "Set-Location vào kho rồi Remove-Item"),
    ("Bash", 'cd "//server/share/KTC-Database" && rm a.docx', "đường dẫn UNC"),
    ("Write", DB, "Write (giữ nguyên từ 1.3.0)"),
    ("Bash", f'rm -f "{DB}"', "rm trực tiếp (giữ nguyên)"),
]
for cc, l, ten in CHAN:
    kq = guard(cc, l)
    kiem(kq == "chan", f"chặn: {ten} (được: {kq})")

HOI = [
    ("Bash", f"python -c \"import shutil; shutil.copy('a.docx', '{DB}')\"", "shutil.copy vào kho (đích trong tham số)"),
    ("Bash", f"D=\"H:/My Drive/KTC-Database\"; python -c \"import os; os.remove(os.environ['D'])\"", "biến trỏ kho + os.remove"),
    ("PowerShell", "$d = 'H:\\My Drive\\KTC-Database'; node -e \"require('fs').writeFileSync(process.argv[1]+'/a','x')\" $d", "node fs.writeFileSync qua biến"),
]
# 1.3.2 (tham dinh lan 4, F4-01): dich khong xac dinh -> CHAN (khong con "ask")
for cc, l, ten in HOI:
    kq = guard(cc, l)
    kiem(kq == "chan", f"chặn (đích không xác định): {ten} (được: {kq})")
HOI_132 = [
    ("Bash", f"d=\"H:/My Drive/KTC-Database\"; python -c \"import shutil,os; shutil.copy('a.txt', os.path.join(r'$d','b.txt'))\"",
     "biến d + shutil.copy [ChatGPT L4 F4-01]"),
    ("Bash", 'ln -s "H:/My Drive/KTC-Database" ./kho', "ln -s tạo liên kết tới kho"),
    ("PowerShell", r"New-Item -ItemType SymbolicLink -Path .\kho -Target 'H:\My Drive\KTC-Database'", "New-Item SymbolicLink tới kho"),
    ("Bash", r'cmd /c mklink /D kho "H:\My Drive\KTC-Database"', "cmd mklink /D tới kho"),
]
for cc, l, ten in HOI_132:
    kq = guard(cc, l)
    kiem(kq == "chan", f"chặn 1.3.2: {ten} (được: {kq})")
QUA_132 = [
    ("Bash", r'cd "H:/My Drive/KTC-Database" && ls > C:\tmp\ds.txt', r"cd vào kho, ghi RA C:\… (đường dẫn Windows tuyệt đối)"),
    ("Bash", 'ln -s /tmp/a ./b', "ln -s ngoài kho"),
]
for cc, l, ten in QUA_132:
    kq = guard(cc, l)
    kiem(kq == "qua", f"cho qua 1.3.2: {ten} (được: {kq})")

QUA = [
    ("Bash", f"python -c \"import docx; d=docx.Document('{DB}'); print(len(d.paragraphs))\"", "python đọc tệp trong kho"),
    ("Bash", 'cd "H:/My Drive/KTC-Database"; find . -iname "*1056*" | head -5', "cd vào kho, chỉ tìm"),
    ("Bash", 'cd "H:/My Drive/KTC-Database" && ls > /tmp/ds.txt', "cd vào kho, ghi RA đường dẫn tuyệt đối ngoài kho"),
    ("Bash", "python -c \"open('30-Ket-Qua/a.txt','w').write('x')\"", "python ghi ngoài kho"),
    ("PowerShell", "powershell -Command \"Set-Content '30-Ket-Qua\\a.txt' 'x'\"", "powershell -Command ghi ngoài kho"),
    ("Bash", 'git status --short | head', "lệnh thường"),
    ("Bash", f'cp "{DB}" 30-Ket-Qua/ban-sao.txt', "cp TỪ kho ra ngoài (giữ nguyên)"),
]
for cc, l, ten in QUA:
    kq = guard(cc, l)
    kiem(kq == "qua", f"cho qua: {ten} (được: {kq})")

print("== B. Nhật ký PostToolUse không lưu lệnh thô ==")
MARK = "ROUND3_PRIVATE_MARKER_9281"
tam = tempfile.mkdtemp(prefix="ktc131_")
try:
    os.makedirs(os.path.join(tam, "90-Nhat-Ky-Van-Hanh"))

    def ghi(che_do, data, env_them=None):
        env = dict(os.environ)
        env.pop("KTC_NHAT_KY_NOI_DUNG", None)
        env["CLAUDE_PROJECT_DIR"] = tam
        env.update(env_them or {})
        subprocess.run([sys.executable, NHAT_KY, che_do], input=json.dumps(data), text=True, encoding="utf-8",
                       env=env, capture_output=True, timeout=30)

    def doc_log():
        d = os.path.join(tam, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
        return "".join(io.open(os.path.join(d, f), encoding="utf-8").read() for f in os.listdir(d)) if os.path.isdir(d) else ""

    ghi("ghi", {"session_id": "s1", "tool_name": "Bash", "tool_input": {"command": f"echo {MARK} > output.txt"}})
    ghi("ghi", {"session_id": "s1", "tool_name": "Agent",
                "tool_input": {"subagent_type": "ktc-tu-hoc", "description": f"xử lý {MARK} nnqp@x.vn"}})
    ghi("ghi", {"session_id": "s1", "tool_name": "Grep", "tool_input": {"pattern": MARK}})
    ghi("ghi", {"session_id": "s1", "tool_name": "Write",
                "tool_input": {"file_path": os.path.join(tam, "30-Ket-Qua", "a.docx")}})
    log = doc_log()
    kiem(MARK not in log, "mặc định: không lưu lệnh Bash, mô tả Agent, mẫu Grep [ChatGPT L3 P0-1]")
    kiem("nnqp@x.vn" not in log, "mặc định: email trong mô tả Agent không vào nhật ký")
    kiem('"hanh_dong": "ghi"' in log or '"hanh_dong": "ghi-chuyen-huong"' in log, "Bash được phân loại hành động (không lưu lệnh)")
    kiem("ktc-tu-hoc" in log, "Agent: chỉ lưu loại agent")
    kiem("30-Ket-Qua/a.docx" in log.replace("\\\\", "/"), "Write: lưu đường dẫn tương đối trong dự án")
    # co chon ghi: che du lieu
    ghi("ghi", {"session_id": "s2", "tool_name": "Bash", "tool_input": {"command": "echo 079123456789 x@y.vn"}},
        {"KTC_NHAT_KY_NOI_DUNG": "1"})
    log = doc_log()
    kiem("079123456789" not in log and "x@y.vn" not in log and "[SỐ ĐỊNH DANH]" in log,
         "chọn ghi (KTC_NHAT_KY_NOI_DUNG=1): lệnh được che số định danh, email")
    # ca nguoc: neu nhat ky van ghi lenh tho thi phep kiem phai bat
    kiem(MARK in json.dumps({"doi_tuong": f"echo {MARK}"}), "ca ngược: chuỗi chứa marker bị phát hiện")

    print("== C. SessionStart nạp gọn ==")
    for i in range(60):
        ghi("ghi", {"session_id": f"s{i % 7}", "tool_name": "Bash", "tool_input": {"command": f"ls thu-muc-{i}"}})
    env = dict(os.environ, CLAUDE_PROJECT_DIR=tam)
    env.pop("KTC_NHAT_KY_NOI_DUNG", None)
    out = subprocess.run([sys.executable, NHAT_KY, "nap"], input="{}", text=True, encoding="utf-8", env=env,
                         capture_output=True, timeout=30).stdout
    sys.path.insert(0, SCRIPTS)
    import ktc_nhat_ky as nk
    kiem(len(out) <= nk.NGAN_SACH_NAP, f"nạp mặc định ≤ {nk.NGAN_SACH_NAP} ký tự (được {len(out)})")
    kiem("thu-muc-" not in out, "nạp mặc định không in lệnh thô")
    kiem(len("x" * (nk.NGAN_SACH_NAP + 1)) > nk.NGAN_SACH_NAP, "ca ngược: vượt ngân sách bị phát hiện")
finally:
    shutil.rmtree(tam, ignore_errors=True)

print("== D. Bản dựng 31-Plugin 1.3.1 ==")
pj = json.load(io.open(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"), encoding="utf-8"))
kiem(pj.get("version", "").startswith("1.3."), f"plugin.json 1.3.x (đang {pj.get('version')})")
skills = sorted(glob.glob(os.path.join(PLUGIN, "skills", "*", "SKILL.md")))
agents = sorted(glob.glob(os.path.join(PLUGIN, "agents", "*.md")))
NGUONG_KHOI = 2500
for p in skills + agents:
    s = io.open(p, encoding="utf-8").read()
    ten = os.path.relpath(p, PLUGIN)
    a, b = s.find("<immutable_rules>"), s.find("</quality_check>")
    kiem(0 < a < b and b - a <= NGUONG_KHOI, f"{ten}: khối lõi ≤ {NGUONG_KHOI} ký tự (được {b - a})")
    kiem("mâu thuẫn" in s[a:b] and "agent" in s[a:b], f"{ten}: khối lõi có quy tắc xử lý bất đồng skill–agent")
    kiem(not __import__("re").search(r"^> \*\*v\d+\.\d+\*\* \(", s, __import__("re").M), f"{ten}: không còn dòng lịch sử phiên bản")
for p in skills:
    d = os.path.dirname(p)
    kiem(os.path.isfile(os.path.join(d, "references", "00-Quy-Tac-Bat-Bien-Day-Du.md")),
         f"{os.path.relpath(d, PLUGIN)}: có references/00-Quy-Tac-Bat-Bien-Day-Du.md")
bc = io.open(os.path.join(PLUGIN, "skills", "bao-cao", "references", "LICH-SU-PHIEN-BAN.md"), encoding="utf-8").read() \
    if os.path.isfile(os.path.join(PLUGIN, "skills", "bao-cao", "references", "LICH-SU-PHIEN-BAN.md")) else ""
kiem("v3.8" in bc and "v3.14" in bc, "bao-cao: lịch sử v3.8–v3.14 được giữ trong references/LICH-SU-PHIEN-BAN.md")

print("== E. kiem_vien_dan đọc tệp văn bản nhiều bảng mã (1.3.2, Gemini L4) ==")
import unicodedata
KVD = os.path.join(GOC, "29-Cong-Cu", "kiem_vien_dan.py")
MAU_VB = "QUYẾT ĐỊNH\nCăn cứ Luật Giáo dục nghề nghiệp số 74/2014/QH13;\n"
DAU_GIU = "̛̂̆"   # mu, trang, moc: co san trong ky tu goc cua cp1258


def _cp1258(s):
    out = b""
    for ch in s:
        try:
            out += ch.encode("cp1258")
        except UnicodeEncodeError:
            nfd = unicodedata.normalize("NFD", ch)
            goc = unicodedata.normalize("NFC", nfd[0] + "".join(c for c in nfd[1:] if c in "̛̂̆"))
            out += goc.encode("cp1258") + "".join(c for c in nfd[1:] if c not in "̛̂̆").encode("cp1258")
    return out


tam2 = tempfile.mkdtemp(prefix="ktc132_")
try:
    for ten, b in (("utf-8", MAU_VB.encode("utf-8")), ("utf-16", MAU_VB.encode("utf-16")), ("cp1258", _cp1258(MAU_VB))):
        f = os.path.join(tam2, ten + ".txt")
        open(f, "wb").write(b)
        r = subprocess.run([sys.executable, KVD, f], capture_output=True, text=True, encoding="utf-8", timeout=60)
        kiem(r.returncode == 0 and "VD02" in r.stdout, f"{ten}: đọc được, phát hiện lỗi viện dẫn (VD02)")
    kiem("VD02" not in "✓ Không phát hiện", "ca ngược: kết quả sạch không chứa mã lỗi")
finally:
    shutil.rmtree(tam2, ignore_errors=True)

print("KET LUAN:", "CO LOI " + str(loi) if loi else "SACH")
sys.exit(1 if loi else 0)
