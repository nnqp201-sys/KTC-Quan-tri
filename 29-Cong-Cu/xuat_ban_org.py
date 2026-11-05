# -*- coding: utf-8 -*-
"""Xuat ban plugin ktc-quan-tri sang kho GitHub cua to chuc — KHONG mang du lieu ca nhan.

VAN DE: kho KTC-Quan-tri chua du lieu ca nhan dang duoc git theo doi — 15 Ban cam ket KPI
2026 CO HO TEN THAT trong ten tep (30-Ket-Qua/2026-09-21/Ban-cam-ket-KPI-THHCQT/) va hang
tram tep ho so De an, dau tu cong. QD 1923 Dieu 23.2: KPI ca nhan chi nguoi co tham quyen va
nguoi duoc danh gia duoc xem. Kho ca nhan thi con duoc; day sang TO CHUC la mo cho moi thanh
vien to chuc.

CACH LAM: `git subtree split --prefix=31-Plugin` tach ra mot nhanh CHI gom lich su cua
31-Plugin — 45 commit, 3,8 MB, 0 ten nguoi that (da kiem 5/11/2026). Giu nguyen lich su phat
trien plugin (Nguyen tac 5), KHONG viet lai lich su kho chinh, khong day du lieu ca nhan.

Khong dung `git filter-repo`: no doi ma bam ca 228 commit (ai da clone phai clone lai) va
620 MB lich su van mang ho so De an, dau tu cong — khong can thiet de phat hanh plugin.

Chay:
    python 29-Cong-Cu/xuat_ban_org.py --kiem            # kiem truoc, khong tao gi
    python 29-Cong-Cu/xuat_ban_org.py                   # tach nhanh phat-hanh-plugin
    python 29-Cong-Cu/xuat_ban_org.py --day <remote>    # tach roi DAY len remote do

Luon chay --kiem truoc. Buoc day KHONG tu dong: nguoi dung tu quyet dinh.
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIEN_TO = "31-Plugin"
NHANH = "phat-hanh-plugin"

# Dau hieu du lieu ca nhan trong ten tep — neu thay trong nhanh phat hanh thi DUNG.
DAU_HIEU_CA_NHAN = (
    re.compile(r"Ban-cam-ket-KPI", re.I),
    re.compile(r"KPI-ca-nhan", re.I),
    re.compile(r"Tu-Danh-Gia.*\.xlsx$", re.I),
    # ho ten tieng Viet co dau trong ten tep (mau trong thi khong co dau nhan dang nay)
    re.compile(r"[ễầạỗữịợệ]"),
)
# Mau TRONG theo nhom vi tri — trung chu "Tu-Danh-Gia" nhung KHONG phai du lieu ca nhan
NGOAI_LE = re.compile(r"skills/kpi-tu-danh-gia/assets/Mau-", re.I)


def git(*a, kiem_loi=True):
    r = subprocess.run(["git"] + list(a), cwd=DU_AN, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if kiem_loi and r.returncode != 0:
        print((r.stderr or r.stdout).strip()[:800])
        raise SystemExit(f"✗ git {' '.join(a)} — mã thoát {r.returncode}")
    return (r.stdout or "").strip()


def kiem_sach(ref):
    """Liet ke tep co dau hieu du lieu ca nhan trong toan bo lich su cua `ref`."""
    ra = git("log", "--all", "--name-only", "--format=", ref) if ref else ""
    ban = set()
    for dong in ra.split("\n"):
        d = dong.strip()
        if not d or NGOAI_LE.search(d):
            continue
        if any(m.search(d) for m in DAU_HIEU_CA_NHAN):
            ban.add(d)
    return sorted(ban)


def kiem_phien_ban():
    """marketplace.json va plugin.json phai cung phien ban (marketplace tung dung o 1.2.1
    suot 12 ban phat hanh — ai cai tu to chuc van thay mo ta cu)."""
    mp = json.load(io.open(os.path.join(DU_AN, ".claude-plugin", "marketplace.json"),
                           encoding="utf-8"))["plugins"][0]
    pj = json.load(io.open(os.path.join(DU_AN, TIEN_TO, ".claude-plugin", "plugin.json"),
                           encoding="utf-8"))
    return mp["version"], pj["version"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kiem", action="store_true", help="chi kiem, khong tach nhanh")
    ap.add_argument("--day", metavar="REMOTE", help="day nhanh len remote nay (vd org)")
    a = ap.parse_args()

    print("── 1. Phiên bản marketplace.json ↔ plugin.json ──")
    v_mp, v_pj = kiem_phien_ban()
    if v_mp != v_pj:
        raise SystemExit(f"✗ LỆCH: marketplace.json {v_mp} ≠ plugin.json {v_pj} — sửa trước khi phát hành")
    print(f"  ✓ cả hai {v_pj}")

    print("── 2. Cây làm việc sạch chưa ──")
    ban = git("status", "--porcelain")
    if ban:
        print(f"  ✗ còn {len(ban.splitlines())} tệp chưa commit — subtree split chỉ lấy phần ĐÃ COMMIT,")
        print("    nên bản phát hành sẽ THIẾU thay đổi mới nhất. Commit rồi chạy lại.")
        if not a.kiem:
            raise SystemExit(1)

    print(f"── 3. Lịch sử {TIEN_TO} có dữ liệu cá nhân không ──")
    xau = kiem_sach("HEAD -- " + TIEN_TO if False else "HEAD")
    xau = [x for x in xau if x.startswith(TIEN_TO + "/")]
    if xau:
        print(f"  ✗ DỪNG: {len(xau)} tệp có dấu hiệu dữ liệu cá nhân trong {TIEN_TO}:")
        for x in xau[:10]:
            print("    " + x)
        raise SystemExit(1)
    print("  ✓ sạch — không tệp nào mang họ tên thật hoặc KPI cá nhân")

    if a.kiem:
        print()
        print(f"(--kiem) Sẵn sàng tách nhánh `{NHANH}`. Chạy lại không có --kiem để tách.")
        return 0

    print(f"── 4. Tách nhánh {NHANH} ──")
    git("branch", "-D", NHANH, kiem_loi=False)
    bam = git("subtree", "split", f"--prefix={TIEN_TO}", "-b", NHANH)
    so = git("rev-list", "--count", NHANH)
    print(f"  ✓ {NHANH} — {so} commit, đầu nhánh {bam[:12]}")
    print("  Lưu ý: nhánh này KHÔNG có .claude-plugin/marketplace.json (tệp đó ở gốc kho).")
    print("  Kho tổ chức cần marketplace.json trỏ source \".\" — thêm trên nhánh đó một lần.")

    if a.day:
        print(f"── 5. Đẩy lên {a.day} ──")
        git("push", a.day, f"{NHANH}:main")
        print(f"  ✓ đã đẩy {NHANH} → {a.day}/main")
    else:
        print()
        print("Chưa đẩy. Khi đã kiểm nhánh, tự đẩy bằng:")
        print(f"  git push <remote-to-chuc> {NHANH}:main")
    return 0


if __name__ == "__main__":
    sys.exit(main())
