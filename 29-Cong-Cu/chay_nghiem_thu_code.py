# -*- coding: utf-8 -*-
"""Chay bo ca nghiem thu plugin KTC-Quan-tri tren Claude Code bang `claude plugin eval`.

Bo ca: 92-Kinh-Nghiem/02-Regression/Evals-Nghiem-Thu/ (15 ca — 01-06 tham dinh lan 2; 07-15 tham dinh lan 3: KPI,
bao cao, soan thao, co bo cham regex tat dinh).
`--eval-dir` phai nam BEN TRONG thu muc plugin, nen chep 31-Plugin + bo ca sang thu muc tam
29-Cong-Cu/_trung_gian/eval-run/ — 31-Plugin/ va goi zip khong bi lan ket qua.

    python 29-Cong-Cu/chay_nghiem_thu_code.py [--runs 1] [--max-cost-usd 5] [--case <glob>]
        [--goi 30-Ket-Qua/<ngay>/Plugin/ktc-quan-tri-<pb>.zip] [--model opus]

--goi (tham dinh lan 5, L5-03/L5-04): nghiem thu tren CHINH goi phat hanh — kiem sha256 voi tep .sha256 di kem, giai nen
thay vi chep 31-Plugin. --model: ghi ro mo hinh (khong co thi dung mac dinh cua tai khoan).

Ket qua: 30-Ket-Qua/<ngay>/Nghiem-thu/ (ket-qua.json, bao-cao.html, tom-tat.md). Ma thoat = ma cua `claude plugin eval`;
4 = loi ha tang (cham gioi han su dung, loi khi chay) — dot do khong dung lam ket qua nghiem thu.
"""
import argparse
import datetime as dt
import glob
import io
import json
import os
import shutil
import subprocess
import sys
import hashlib
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BO_CA = os.path.join(DU_AN, "92-Kinh-Nghiem", "02-Regression", "Evals-Nghiem-Thu")
TAM = os.path.join(DU_AN, "29-Cong-Cu", "_trung_gian", "eval-run", "ktc-quan-tri")


def tim_claude():
    ung = sorted(glob.glob(os.path.expanduser(
        r"~\.vscode\extensions\anthropic.claude-code-*\resources\native-binary\claude.exe")))
    return ung[-1] if ung else "claude"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="1")
    ap.add_argument("--max-cost-usd", default="5")
    ap.add_argument("--case")
    # --chi 05 06 07: chi chep cac ca co tien to nay (`--case` cua CLI 2.1.283 khong nhan [..] hay {..})
    ap.add_argument("--chi", nargs="*")
    ap.add_argument("--nhan", default="", help="tien to ten tep ket qua, vd dot2-")
    ap.add_argument("--goi", help="goi zip phat hanh (kiem sha256 voi <goi>.sha256 roi giai nen)")
    ap.add_argument("--model", help="mo hinh chay ca (vd opus, sonnet, haiku hoac ma day du)")
    a = ap.parse_args()
    if os.path.isdir(TAM):
        shutil.rmtree(TAM)
    nguon = "31-Plugin/"
    if a.goi:
        sha = hashlib.sha256(io.open(a.goi, "rb").read()).hexdigest()
        ky_vong = io.open(a.goi + ".sha256", encoding="utf-8").read().split()[0]
        if sha != ky_vong:
            print(f"DỪNG: sha256 gói {sha} khác tệp .sha256 {ky_vong}")
            return 3
        with zipfile.ZipFile(a.goi) as z:
            z.extractall(TAM)
        nguon = f"{os.path.basename(a.goi)} (sha256 {sha}, đã kiểm khớp .sha256)"
    else:
        shutil.copytree(os.path.join(DU_AN, "31-Plugin"), TAM)
    shutil.copytree(BO_CA, os.path.join(TAM, "evals"),
                    ignore=(lambda d, ten: [t for t in ten if os.path.isdir(os.path.join(d, t)) and d == BO_CA
                                            and not any(t.startswith(c) for c in a.chi)]) if a.chi else None)
    # Manifest phat hanh dat defaultEnabled=false -> sandbox eval se KHONG nap plugin. Chi tren BAN SAO TAM nay
    # bat len de nghiem thu dung plugin; goi zip va 31-Plugin/ giu nguyen.
    pj = os.path.join(TAM, ".claude-plugin", "plugin.json")
    m = json.load(io.open(pj, encoding="utf-8"))
    m["defaultEnabled"] = True
    io.open(pj, "w", encoding="utf-8").write(json.dumps(m, ensure_ascii=False, indent=2) + "\n")
    ra = os.path.join(DU_AN, "30-Ket-Qua", dt.date.today().isoformat(), "Nghiem-thu")
    os.makedirs(ra, exist_ok=True)
    cl = tim_claude()
    ver = subprocess.run([cl, "--version"], capture_output=True, text=True).stdout.strip()
    # 29/9/2026: dot10 chay luc tai khoan cham gioi han phien -> 37/38 luot loi ha tang. Thu truoc mot lenh nho.
    thu = subprocess.run([cl, "-p", "Trả lời đúng một chữ: ok", "--model", "haiku"], capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    if "limit" in (thu.stdout + thu.stderr).lower() or thu.returncode:
        print("DỪNG: tài khoản đang chạm giới hạn sử dụng — chạy lại sau giờ phục hồi:", (thu.stdout + thu.stderr).strip()[:200])
        return 4
    cmd = [cl, "plugin", "eval", TAM, "--runs", a.runs, "--ablation", "none", "--trust-plugin",
           "--allow-tools", "Write", "Edit", "--no-publish", "--threshold", "1",
           "--max-cost-usd", a.max_cost_usd,
           "--json", os.path.join(ra, a.nhan + "ket-qua.json"), "--report", os.path.join(ra, a.nhan + "bao-cao.html"),
           "--output-dir", os.path.join(ra, "chi-tiet")]
    if a.case:
        cmd += ["--case", a.case]
    if a.model:
        cmd += ["--model", a.model]
    env = dict(os.environ)
    env.pop("KTC_NHAT_KY_NOI_DUNG", None)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, cwd=DU_AN)
    io.open(os.path.join(ra, a.nhan + "log-eval.txt"), "w", encoding="utf-8").write(
        f"# Lệnh: {' '.join(cmd)}\n# CLI: {ver}\n# Nguồn plugin: {nguon}\n# Mô hình: {a.model or 'mặc định của tài khoản'}\n# Thời điểm: {dt.datetime.now():%d/%m/%Y %H:%M}\n"
        f"{r.stdout}\n{r.stderr}\n# Mã thoát: {r.returncode}\n")
    # Luot loi do gioi han su dung / ha tang: khong tinh la plugin truot, khong dung lam nghiem thu
    ma = r.returncode
    try:
        j = json.load(io.open(os.path.join(ra, a.nhan + "ket-qua.json"), encoding="utf-8"))
        loi = [c["name"] for c in j["cases"] for x in c["arms"]["with"] if x.get("error")]
        if loi:
            gh = f"# LỖI HẠ TẦNG: {len(loi)} lượt lỗi khi chạy (vd {loi[0]}) — đợt này KHÔNG dùng làm kết quả nghiệm thu, chạy lại"
            io.open(os.path.join(ra, a.nhan + "log-eval.txt"), "a", encoding="utf-8").write(gh + "\n")
            print(gh)
            ma = 4
    except (OSError, ValueError, KeyError):
        pass
    print(r.stdout[-3000:])
    print(r.stderr[-1500:])
    print("Mã thoát:", ma, "→", ra)
    return ma


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
