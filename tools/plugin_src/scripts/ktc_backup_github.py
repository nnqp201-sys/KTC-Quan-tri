# -*- coding: utf-8 -*-
"""Tu backup du an KTC-Quan-tri len GitHub moi ngay.

Cach chay:
  python ktc_backup_github.py --du-an "D:\\.CLAUDE code\\KTC-Quan-tri"            # Task Scheduler 21:00
  python ktc_backup_github.py --du-an ... --neu-can                                # SessionStart: chi chay
                                                                                   # neu >24h chua backup
  python ktc_backup_github.py --du-an ... --trang-thai                             # xem lan backup cuoi

Nguyen tac an toan:
  - Chi `commit` + `push` thuong. KHONG BAO GIO force-push, rebase, reset.
  - Chua co remote `origin` -> bao va thoat, khong lam gi.
  - Che do --neu-can chi chay khi DA co it nhat 1 lan push thanh cong (tranh bat hop dang nhap giua phien).
  - GIT_TERMINAL_PROMPT=0: khong bao gio treo cho nhap mat khau trong tac vu chay ngam.
  - Chan commit neu phat hien tep co ten giong bi mat (credential, .env, token, key...).
  - Trang thai luu trong .git/ktc-backup.json — khong nam trong cay theo doi, khong sinh commit rac.
"""
import argparse
import datetime as dt
import io
import json
import os
import re
import subprocess
import sys

MAU_BI_MAT = re.compile(
    r"(^|/)(\.env(\..*)?|.*credential.*|.*secret.*|.*token.*\.json|id_rsa.*|.*\.pem|.*\.key|\.netrc)$",
    re.IGNORECASE,
)
GIO_TOI_THIEU = 24


def git(du_an, *args, timeout=120):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    r = subprocess.run(["git", "-C", du_an, *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout, env=env)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def tep_trang_thai(du_an):
    return os.path.join(du_an, ".git", "ktc-backup.json")


def doc_trang_thai(du_an):
    try:
        return json.load(io.open(tep_trang_thai(du_an), encoding="utf-8"))
    except Exception:
        return {}


def ghi_trang_thai(du_an, **kw):
    s = doc_trang_thai(du_an)
    s.update(kw)
    io.open(tep_trang_thai(du_an), "w", encoding="utf-8").write(
        json.dumps(s, ensure_ascii=False, indent=2))


def ghi_nhat_ky(du_an, ket_qua, chi_tiet=""):
    thu_muc = os.path.join(du_an, "03-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
    try:
        os.makedirs(thu_muc, exist_ok=True)
        with io.open(os.path.join(thu_muc, dt.date.today().isoformat() + ".jsonl"), "a",
                     encoding="utf-8") as f:
            f.write(json.dumps({"t": dt.datetime.now().isoformat(timespec="seconds"),
                                "loai": "backup", "ket_qua": ket_qua,
                                "chi_tiet": chi_tiet[:300]}, ensure_ascii=False) + "\n")
    except Exception:
        pass


def backup(du_an):
    rc, out = git(du_an, "remote", "get-url", "origin")
    if rc != 0:
        msg = "Chưa có remote 'origin' — bỏ qua. Nối repo: git remote add origin <URL-repo-PRIVATE>"
        ghi_nhat_ky(du_an, "bo-qua", msg)
        print(msg)
        return 0

    # 1) gom thay doi
    git(du_an, "add", "-A")
    rc, staged = git(du_an, "diff", "--cached", "--name-only")
    tep = [t for t in staged.splitlines() if t.strip()]

    nghi_van = [t for t in tep if MAU_BI_MAT.search(t.replace("\\", "/"))]
    if nghi_van:
        git(du_an, "reset", "-q")     # chi bo stage, khong dung toi noi dung tep
        msg = f"DỪNG: {len(nghi_van)} tệp tên giống bí mật, cần người kiểm: {nghi_van[:5]}"
        ghi_nhat_ky(du_an, "dung-an-toan", msg)
        print(msg)
        return 1

    # 2) commit neu co thay doi
    if tep:
        now = dt.datetime.now()
        rc, out = git(du_an, "commit", "-q", "-m",
                      f"backup: tự động {now:%d/%m/%Y %H:%M} ({len(tep)} tệp)")
        if rc != 0:
            ghi_nhat_ky(du_an, "loi-commit", out)
            print("Lỗi commit:\n" + out)
            return 1

    # 3) push (ke ca khi khong co commit moi — de day not commit tay chua push)
    rc, out = git(du_an, "push", "-u", "origin", "HEAD", timeout=300)
    if rc != 0:
        ghi_nhat_ky(du_an, "loi-push", out)
        print("Lỗi push (chưa đăng nhập GitHub lần đầu? chạy tay 1 lần để Git Credential Manager lưu):\n" + out)
        return 1

    ghi_trang_thai(du_an, lan_cuoi=dt.datetime.now().isoformat(timespec="seconds"), da_tung_push=True)
    ghi_nhat_ky(du_an, "thanh-cong", f"{len(tep)} tệp mới")
    print(f"Backup xong: {len(tep)} tệp thay đổi đã đẩy lên origin.")
    return 0


def can_chay(du_an):
    s = doc_trang_thai(du_an)
    if not s.get("da_tung_push"):
        return False          # chua tung push tay thanh cong -> khong tu chay giua phien
    try:
        cuoi = dt.datetime.fromisoformat(s["lan_cuoi"])
    except Exception:
        return True
    return (dt.datetime.now() - cuoi).total_seconds() > GIO_TOI_THIEU * 3600


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--du-an", default=os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    ap.add_argument("--neu-can", action="store_true")
    ap.add_argument("--trang-thai", action="store_true")
    a = ap.parse_args()
    du_an = os.path.abspath(a.du_an)

    if not os.path.isdir(os.path.join(du_an, "03-Nhat-Ky-Van-Hanh")) or \
       not os.path.isdir(os.path.join(du_an, ".git")):
        return 0              # khong phai du an KTC-Quan-tri -> im lang

    if a.trang_thai:
        s = doc_trang_thai(du_an)
        print(f"Backup GitHub — lần cuối: {s.get('lan_cuoi', 'chưa từng')}")
        return 0
    if a.neu_can:
        if not can_chay(du_an):
            return 0
        print("KTC-Quan-tri: đã quá 24h chưa backup — chạy backup bù...")
        backup(du_an)
        return 0              # che do hook: loi da ghi nhat ky, khong lam hong phien
    return backup(du_an)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.TimeoutExpired:
        print("Backup quá thời gian chờ — bỏ qua lần này.")
        raise SystemExit(0)
