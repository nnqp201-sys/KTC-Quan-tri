# -*- coding: utf-8 -*-
"""Tu backup du an KTC-Quan-tri len GitHub moi ngay.

Cach chay:
  python ktc_backup_github.py --du-an "<thu muc KTC-Quan-tri>"                    # Task Scheduler 21:00
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
# CCCD: 12 chu so, bat dau bang 0 (ma tinh), khong dinh lien chu so khac
MAU_SO_DINH_DANH = re.compile(r"(?<![0-9A-Za-z])0\d{11}(?![0-9A-Za-z])")


def git(du_an, *args, timeout=120):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    # stdin=DEVNULL la BAT BUOC: Task Scheduler chay bang pythonw.exe, ma pythonw KHONG co
    # std handle hop le. Tien trinh con thua ke stdin hong -> Git Credential Manager khong trao
    # doi duoc thong tin dang nhap, `git push` that bai va KHONG in ra loi nao (chi_tiet rong).
    # Loi that 18-20/9/2026: backup tu dong 21:00 that bai lang le 2 ngay, chay tay thi luon duoc.
    r = subprocess.run(["git", "-C", du_an, *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout, env=env,
                       stdin=subprocess.DEVNULL)
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


def tep_nhat_ky(du_an):
    """Noi ghi nhat ky backup — TUY DU AN, khong tao thu muc la trong du an khac.

    Script nay dung chung cho nhieu kho (KTC-Quan-tri, KTC-Ra-Soat-897-Universal-Plugin...).
    Truoc day no makedirs("90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong") vo dieu kien, nen chay
    tren kho khac se de lai mot thu muc mang hinh dang cua KTC-Quan-tri — va chinh lan backup
    do se commit thu muc rac ay len GitHub.
    """
    ktc = os.path.join(du_an, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
    if os.path.isdir(ktc):
        return os.path.join(ktc, dt.date.today().isoformat() + ".jsonl")
    k897 = os.path.join(du_an, ".ktc897", "nhat-ky")
    if os.path.isdir(os.path.dirname(k897)):
        os.makedirs(k897, exist_ok=True)
        return os.path.join(k897, dt.date.today().isoformat() + ".jsonl")
    # Mac dinh: trong .git/ — luon ton tai voi repo git, khong bao gio bi theo doi
    return os.path.join(du_an, ".git", "ktc-backup-log.jsonl")


def ghi_nhat_ky(du_an, ket_qua, chi_tiet=""):
    try:
        with io.open(tep_nhat_ky(du_an), "a", encoding="utf-8") as f:
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

    # 1b) quet NOI DUNG tep van ban da stage: so dinh danh ca nhan (CCCD 12 so bat dau 0) -> dung
    #     (tiep thu tham dinh lan 1 C-01: quet ten tep khong du)
    co_so_dinh_danh = []
    for t in tep:
        if os.path.splitext(t)[1].lower() not in (".md", ".txt", ".json", ".jsonl", ".csv", ".py", ".yaml", ".yml"):
            continue
        try:
            with io.open(os.path.join(du_an, t), encoding="utf-8", errors="ignore") as h:
                if MAU_SO_DINH_DANH.search(h.read()):
                    co_so_dinh_danh.append(t)
        except OSError:
            pass
    if co_so_dinh_danh:
        git(du_an, "reset", "-q")
        msg = f"DỪNG: {len(co_so_dinh_danh)} tệp có chuỗi giống số định danh cá nhân, cần người kiểm: {co_so_dinh_danh[:5]}"
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
    ap.add_argument("--du-an", default=None)
    ap.add_argument("--neu-can", action="store_true")
    ap.add_argument("--trang-thai", action="store_true")
    a = ap.parse_args()
    # Nguoi goi co CHI DINH RO kho hay khong — quyet dinh muc do chat cua chot bao ve duoi.
    chi_dinh_ro = a.du_an is not None
    du_an = os.path.abspath(a.du_an or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())

    if not os.path.isdir(os.path.join(du_an, ".git")):
        if chi_dinh_ro:
            print(f"Không phải kho git: {du_an}")
            return 1
        return 0
    # Khi KHONG chi dinh ro (hook SessionStart chay trong bat ky du an nao nguoi dung mo),
    # chi backup du an mang hinh dang KTC-Quan-tri: khong duoc tu y day kho cua nguoi khac
    # len remote cua ho. Khi da chi dinh ro --du-an (Task Scheduler) thi day la y dinh tuong
    # minh cua nguoi van hanh -> chi can la kho git.
    if not chi_dinh_ro and not os.path.isdir(os.path.join(du_an, "90-Nhat-Ky-Van-Hanh")):
        return 0

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
