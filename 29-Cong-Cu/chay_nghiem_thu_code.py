# -*- coding: utf-8 -*-
"""Chay bo ca nghiem thu plugin KTC-Quan-tri tren Claude Code bang `claude plugin eval`.

Bo ca: 92-Kinh-Nghiem/02-Regression/Evals-Nghiem-Thu/ (6 ca — tham dinh lan 2, ChatGPT 5.2.7 va P1.3).
`--eval-dir` phai nam BEN TRONG thu muc plugin, nen chep 31-Plugin + bo ca sang thu muc tam
29-Cong-Cu/_trung_gian/eval-run/ — 31-Plugin/ va goi zip khong bi lan ket qua.

    python 29-Cong-Cu/chay_nghiem_thu_code.py [--runs 1] [--max-cost-usd 5] [--case <glob>]

Ket qua: 30-Ket-Qua/<ngay>/Nghiem-thu/ (ket-qua.json, bao-cao.html, tom-tat.md). Ma thoat = ma cua `claude plugin eval`.
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
    a = ap.parse_args()
    if os.path.isdir(TAM):
        shutil.rmtree(TAM)
    shutil.copytree(os.path.join(DU_AN, "31-Plugin"), TAM)
    shutil.copytree(BO_CA, os.path.join(TAM, "evals"))
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
    cmd = [cl, "plugin", "eval", TAM, "--runs", a.runs, "--ablation", "none", "--trust-plugin",
           "--allow-tools", "Write", "Edit", "--no-publish", "--threshold", "1",
           "--max-cost-usd", a.max_cost_usd,
           "--json", os.path.join(ra, "ket-qua.json"), "--report", os.path.join(ra, "bao-cao.html"),
           "--output-dir", os.path.join(ra, "chi-tiet")]
    if a.case:
        cmd += ["--case", a.case]
    env = dict(os.environ)
    env.pop("KTC_NHAT_KY_NOI_DUNG", None)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, cwd=DU_AN)
    io.open(os.path.join(ra, "log-eval.txt"), "w", encoding="utf-8").write(
        f"# Lệnh: {' '.join(cmd)}\n# CLI: {ver}\n# Thời điểm: {dt.datetime.now():%d/%m/%Y %H:%M}\n"
        f"{r.stdout}\n{r.stderr}\n# Mã thoát: {r.returncode}\n")
    print(r.stdout[-3000:])
    print(r.stderr[-1500:])
    print("Mã thoát:", r.returncode, "→", ra)
    return r.returncode


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
