# -*- coding: utf-8 -*-
"""Hoi quy cho 2 hook cua plugin ktc-quan-tri: tu ghi nhat ky va tu backup GitHub.

Moi ca deu co ca THU NGUOC (biet chac sai) — bai hoc LL-20260914-001: phep kiem bao "sach"
ngay lan dau thi phai nghi chinh phep kiem. Chay trong thu muc tam, khong dung repo that.
"""
import json
import os
import subprocess
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
NK = os.path.join(GOC, "29-Cong-Cu", "plugin_src", "scripts", "ktc_nhat_ky.py")
BK = os.path.join(GOC, "29-Cong-Cu", "plugin_src", "scripts", "ktc_backup_github.py")
loi = []


THAT = os.path.join(GOC, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")


def anh_log_that():
    if not os.path.isdir(THAT):
        return {}
    return {f: os.path.getsize(os.path.join(THAT, f)) for f in os.listdir(THAT)}


def chay(args, stdin=""):
    e = dict(os.environ)
    e.pop("CLAUDE_PROJECT_DIR", None)   # de script tu tim du an theo cwd trong input
    return subprocess.run([sys.executable, *args], input=stdin, capture_output=True, text=True,
                          encoding="utf-8", env=e, cwd=GOC)  # cwd = du an THAT: bat loi ghi nham


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        loi.append(ten)


def git(*a):
    subprocess.run(["git", *a], capture_output=True)


truoc = anh_log_that()
with tempfile.TemporaryDirectory() as t:
    du_an = os.path.join(t, "du_an"); khac = os.path.join(t, "khac")
    os.makedirs(os.path.join(du_an, "90-Nhat-Ky-Van-Hanh")); os.makedirs(khac)
    log_dir = os.path.join(du_an, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")

    print("== ktc_nhat_ky.py ==")
    chay([NK, "ghi"], json.dumps({"session_id": "s1", "cwd": du_an, "tool_name": "Write",
                                  "tool_input": {"file_path": "x.md", "content": "NOI-DUNG-BI-MAT"}}))
    noi = "".join(open(os.path.join(log_dir, f), encoding="utf-8").read() for f in os.listdir(log_dir))
    kiem('"cong_cu": "Write"' in noi, "ghi được thao tác trong dự án")
    kiem("NOI-DUNG-BI-MAT" not in noi, "không ghi nội dung tệp vào log")
    chay([NK, "ghi"], json.dumps({"cwd": khac, "tool_name": "Write", "tool_input": {"file_path": "a"}}))
    kiem(not os.listdir(khac), "ca ngược: ngoài dự án không tạo log")
    r = chay([NK, "ghi"], "khong-phai-json")
    kiem(r.returncode == 0, "ca ngược: stdin hỏng vẫn thoát 0")
    r = chay([NK, "nap"], json.dumps({"cwd": du_an}))
    kiem("x.md" in r.stdout, "nạp context liệt kê tệp đã sửa")

    print("== ktc_backup_github.py ==")
    repo = os.path.join(t, "repo"); remote = os.path.join(t, "remote.git")
    git("init", "-q", repo); os.makedirs(os.path.join(repo, "90-Nhat-Ky-Van-Hanh"))
    git("-C", repo, "config", "user.email", "t@t"); git("-C", repo, "config", "user.name", "t")
    open(os.path.join(repo, "a.md"), "w").write("a")
    r = chay([BK, "--du-an", repo])
    kiem(r.returncode == 0 and "Chưa có remote" in r.stdout, "chưa có remote: bỏ qua, thoát 0")
    git("init", "-q", "--bare", remote); git("-C", repo, "remote", "add", "origin", remote)
    r = chay([BK, "--du-an", repo])
    kiem(r.returncode == 0 and "Backup xong" in r.stdout, "có remote: commit + push thành công")
    r = chay([BK, "--du-an", repo, "--neu-can"])
    kiem(r.stdout.strip() == "", "--neu-can trong 24h: không chạy lại")
    open(os.path.join(repo, "my-credentials.json"), "w").write("x")
    r = chay([BK, "--du-an", repo])
    so_commit = subprocess.run(["git", "-C", remote, "rev-list", "--count", "HEAD"],
                               capture_output=True, text=True).stdout.strip()
    kiem(r.returncode == 1 and "DỪNG" in r.stdout and so_commit == "1",
         "ca ngược: tệp tên giống bí mật -> dừng, không push")
    kiem(os.path.exists(os.path.join(repo, "my-credentials.json")), "không xóa tệp của người dùng khi dừng")

    # --- pythonw: Task Scheduler chay bang pythonw.exe, KHONG co std handle hop le ---
    # Loi that 18-20/9/2026: tien trinh con thua ke stdin hong -> Git Credential Manager khong
    # trao doi duoc thong tin dang nhap -> `git push` that bai va KHONG in ra loi nao. Backup
    # 21:00 hong LANG LE hai ngay, trong khi chay tay luc nao cung duoc.
    #
    # Ca (a) la kiem TINH: remote cuc bo trong bo thu nay khong dung credential helper nen
    # khong tai hien duoc loi that. Doc thang nguon de it nhat chan viec go co stdin ra.
    nguon_bk = open(BK, encoding="utf-8").read()
    kiem("stdin=subprocess.DEVNULL" in nguon_bk,
         "git() truyền stdin=DEVNULL (bắt buộc cho pythonw/Task Scheduler)")

    # Ca (b) la kiem DONG: script phai chay tron ven duoi pythonw, khong vang loi nao.
    pythonw = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
    if os.path.isfile(pythonw):
        open(os.path.join(repo, "b.md"), "w").write("b")
        os.remove(os.path.join(repo, "my-credentials.json"))
        r2 = subprocess.run([pythonw, BK, "--du-an", repo], capture_output=True,
                            text=True, timeout=180, stdin=subprocess.DEVNULL)
        so_commit2 = subprocess.run(["git", "-C", remote, "rev-list", "--count", "HEAD"],
                                    capture_output=True, text=True).stdout.strip()
        kiem(r2.returncode == 0 and so_commit2 == "2",
             f"chạy dưới pythonw.exe: push thành công (mã {r2.returncode}, {so_commit2} commit)")
    else:
        print("  -- bỏ qua ca pythonw: không tìm thấy pythonw.exe")

kiem(anh_log_that() == truoc, "ca ngược: kiểm thử không ghi gì vào nhật ký THẬT của dự án")
print("KET LUAN:", "CO LOI " + str(loi) if loi else "SACH")
sys.exit(1 if loi else 0)
