# -*- coding: utf-8 -*-
"""Tham dinh lan 5 (29/9/2026): goi phat hanh dung lap lai duoc; guard chiu tai noi dung Markdown lon.

L5-04 (ChatGPT), 2.1 (Grok): dung 1.3.12 tu ban checkout sach cua commit phat hanh ra sha256 khac — git tren Windows
(core.autocrlf=true) checkout ra CRLF, thu muc lam viec lan LF/CRLF. Tu 1.3.13 cong cu dong goi chuan hoa xuong dong.
Gemini L5 1.2: "guard treo khi xu ly tep .md co bang phuc tap" — khong tai hien; giu ca thu de canh gioi thoi gian.

Chay: python 92-Kinh-Nghiem/02-Regression/Cases/test_dung_lap_lai.py
"""
import glob
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "29-Cong-Cu"))

import dong_goi_plugin as D          # noqa: E402

GUARD = os.path.join(DU_AN, "29-Cong-Cu", "plugin_src", "scripts", "ktc_guard.py")
that_bai = []


def kiem(ten, dieu_kien, mo_ta=""):
    print(f"  {'✓' if dieu_kien else '✗'} {ten:58s} {mo_ta}")
    if not dieu_kien:
        that_bai.append(ten)


print("── Chuẩn hóa xuống dòng ──")
tmp = tempfile.mkdtemp()
try:
    tep = {"a.md": b"x\r\ny\r\n", "b.py": b"x\ny\n", "c.cmd": b"x\ny\n", "d.docx": b"PK\r\n\x00", "e.json": b"{}\r\n"}
    for t, b in tep.items():
        io.open(os.path.join(tmp, t), "wb").write(b)
    cu, D.PLUGIN_DIR = D.PLUGIN_DIR, tmp
    try:
        D.chuan_hoa_xuong_dong()
    finally:
        D.PLUGIN_DIR = cu
    doc = lambda t: io.open(os.path.join(tmp, t), "rb").read()  # noqa: E731
    kiem(".md CRLF → LF", doc("a.md") == b"x\ny\n")
    kiem(".json CRLF → LF", doc("e.json") == b"{}\n")
    kiem(".py LF giữ nguyên", doc("b.py") == b"x\ny\n")
    kiem(".cmd → CRLF (Windows cần)", doc("c.cmd") == b"x\r\ny\r\n")
    kiem("tệp nhị phân không đụng tới", doc("d.docx") == b"PK\r\n\x00")
    io.open(os.path.join(tmp, "f.md"), "wb").write(b"x\r\ny\r\n")
    kiem("so băm bảng đối chiếu bỏ qua CR", D._bam_lf(os.path.join(tmp, "f.md")) == D._bam_lf(os.path.join(tmp, "a.md")))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

print("── Gói phát hành hiện hành ──")
goi = sorted(glob.glob(os.path.join(DU_AN, "30-Ket-Qua", "*", "Plugin", f"ktc-quan-tri-{D.PLUGIN_VERSION}.zip")))
if not goi:
    print(f"  ! bỏ qua: chưa có ktc-quan-tri-{D.PLUGIN_VERSION}.zip trong 30-Ket-Qua/*/Plugin (chưa đóng gói)")
else:
    z = zipfile.ZipFile(goi[-1])
    crlf = [n for n in z.namelist() if os.path.splitext(n)[1].lower() in D.DUOI_VAN_BAN and b"\r\n" in z.read(n)]
    kiem("không tệp văn bản nào mang CRLF", not crlf, str(crlf[:3]))
    bd = z.read("skills/quan-tri/references/BAN-DO-TEP.md").decode("utf-8")
    so = bd.count("| `20-Chuan-Chung/")
    kiem("BAN-DO-TEP đủ dòng 20-Chuan-Chung (≥ 14)", so >= 14, f"{so} dòng")

print("── Guard chịu tải nội dung Markdown lớn (Gemini L5 1.2) ──")
DICH = os.path.join(DU_AN, "30-Ket-Qua", "thu-tai.md")
KHO = os.path.join("H:" + os.sep, "My Drive", "KTC-" + "Database", "x.md")
bang = "| " + " | ".join(f"Cot {i}" for i in range(30)) + " |\n|" + "---|" * 30 + "\n"
bang += "".join("| " + " | ".join(f"o {r}-{c} \\| `x` **y** [z](a)" for c in range(30)) + " |\n" for r in range(3000))
di_dang = "|" * 200000 + "\\" * 50000 + "`" * 50000 + "| a | b\n" * 20000 + "(" * 30000
ca = [
    ("Write bảng 3000×30 (~2,7 MB)", {"tool_name": "Write", "tool_input": {"file_path": DICH, "content": bang}}, 0),
    ("Write nội dung dị dạng", {"tool_name": "Write", "tool_input": {"file_path": DICH, "content": di_dang}}, 0),
    ("Edit bảng lớn", {"tool_name": "Edit", "tool_input": {"file_path": DICH, "old_string": bang[:50000],
                                                           "new_string": bang}}, 0),
    ("Bash heredoc bảng lớn", {"tool_name": "Bash", "tool_input": {"command": "cat > thu.md <<'X'\n" + bang + "X"}}, 0),
    ("PowerShell here-string bảng lớn", {"tool_name": "PowerShell",
                                         "tool_input": {"command": "@'\n" + bang + "\n'@ | Out-File thu.md"}}, 0),
    ("Write bảng lớn vào kho → vẫn CHẶN", {"tool_name": "Write", "tool_input": {"file_path": KHO, "content": bang}}, 2),
]
for ten, v, ma in ca:
    t = time.time()
    p = subprocess.run([sys.executable, GUARD], input=json.dumps(v, ensure_ascii=False).encode("utf-8"),
                       capture_output=True, timeout=60)
    s = time.time() - t
    kiem(ten, p.returncode == ma and s < 10, f"mã {p.returncode}, {s:.2f} giây (giới hạn hook 30 giây)")

print()
if that_bai:
    print(f"KHÔNG ĐẠT {len(that_bai)}: {that_bai}")
    sys.exit(1)
print("ĐẠT")
