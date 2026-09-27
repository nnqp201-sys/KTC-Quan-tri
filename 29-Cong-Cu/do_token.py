# -*- coding: utf-8 -*-
"""Do chi phi context cua plugin KTC-Quan-tri (tham dinh doc lap lan 3, ChatGPT muc 4, P1-1).

So sanh hai goi .zip (vd 1.3.0 va 1.3.1) theo cac muc:
  - metadata nap dau moi phien: description cua moi skill + agent;
  - than SKILL.md / agent (nap khi duoc goi); rieng khoi chuan chung chen vao;
  - phan in ra dau phien cua hook SessionStart `nap` tren du lieu that cua du an (neu co).
Token uoc tinh = ky tu / 4 (cung quy uoc bao cao tham dinh); day la uoc luong so sanh, KHONG phai so token tinh phi.

    python 29-Cong-Cu/do_token.py <goi-cu.zip> <goi-moi.zip> [--ra <tep.md>]
"""
import argparse
import io
import os
import re
import subprocess
import sys
import tempfile
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def tk(n):
    return round(n / 4)


def do_goi(zp):
    z = zipfile.ZipFile(zp)
    kq = {"mo_ta": 0, "than": {}, "khoi": {}}
    for n in sorted(z.namelist()):
        la_skill = re.fullmatch(r"skills/[^/]+/SKILL\.md", n)
        la_agent = re.fullmatch(r"agents/[^/]+\.md", n)
        if not (la_skill or la_agent):
            continue
        s = z.read(n).decode("utf-8")
        m = re.search(r"^description:\s*(.*)$", s, re.M)
        kq["mo_ta"] += len(m.group(1).strip().strip("\"'")) if m else 0
        kq["than"][n] = len(s)
        a = s.find("<immutable_rules>")
        # ket thuc khoi: </quality_check> (1.3.1) hoac </examples> NGAY SAU no (1.3.0) — skill co the co muc
        # <examples> rieng o xa hon, khong duoc tinh vao khoi
        e2 = s.find("</quality_check>", a)
        e1 = s.find("</examples>", e2) if e2 > 0 else -1
        b = e1 if 0 < e1 and e1 - e2 < 2500 else e2
        # tinh tu tieu de khoi (dong "## ..." ngay truoc <immutable_rules>)
        h = s.rfind("\n## ", 0, a) if a > 0 else -1
        kq["khoi"][n] = (b - (h if h >= 0 else a)) if a > 0 and b > a else 0
    return kq


def do_nap(zp):
    """Chay `ktc_nhat_ky.py nap` cua goi tren du lieu that cua du an; tra ve so ky tu in ra."""
    z = zipfile.ZipFile(zp)
    with tempfile.TemporaryDirectory() as t:
        p = os.path.join(t, "ktc_nhat_ky.py")
        io.open(p, "wb").write(z.read("scripts/ktc_nhat_ky.py"))
        env = dict(os.environ, CLAUDE_PROJECT_DIR=DU_AN, PYTHONIOENCODING="utf-8")
        env.pop("KTC_NHAT_KY_NOI_DUNG", None)
        env.pop("KTC_NAP_DAY_DU", None)
        # KHONG lam sach nhat ky that khi do: dat co chon ghi cho ban moi (ham lam sach bo qua khi co co)
        env["KTC_NHAT_KY_NOI_DUNG"] = "1"
        r = subprocess.run([sys.executable, p, "nap"], input="{}", capture_output=True, text=True,
                           encoding="utf-8", env=env, timeout=60)
        return len(r.stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cu")
    ap.add_argument("moi")
    ap.add_argument("--ra")
    a = ap.parse_args()
    c, m = do_goi(a.cu), do_goi(a.moi)
    nc, nm = do_nap(a.cu), do_nap(a.moi)
    ten_c, ten_m = os.path.basename(a.cu), os.path.basename(a.moi)
    d = [f"# Đo chi phí context — {ten_c} → {ten_m}", "",
         "Token ước tính = ký tự / 4 (cùng quy ước báo cáo thẩm định lần 3); dùng để **so sánh**, không phải số tính phí.",
         f"Phần nạp đầu phiên đo trên nhật ký thật của dự án, cùng thời điểm, bằng script `nap` của từng gói.", "",
         "| Hạng mục | Khi nào nạp | Cũ (ký tự / ~token) | Mới (ký tự / ~token) | Giảm |",
         "|---|---|---:|---:|---:|"]

    def dong(ten, khi, x, y):
        g = f"{(x - y) / x * 100:.0f}%" if x else "—"
        d.append(f"| {ten} | {khi} | {x:,} / {tk(x):,} | {y:,} / {tk(y):,} | {g} |")

    dong("Mô tả 8 skill + 7 agent", "mọi phiên", c["mo_ta"], m["mo_ta"])
    dong("Phần nạp đầu phiên (`nap`)", "mọi phiên trong dự án", nc, nm)
    kc, km = sum(c["khoi"].values()), sum(m["khoi"].values())
    dong("Khối chuẩn chung, cộng 15 bản sao", "khi skill/agent được gọi", kc, km)
    dong("Khối chuẩn chung, 1 bản", "mỗi lần gọi 1 skill/agent", max(c["khoi"].values()), max(m["khoi"].values()))
    tc, tm = sum(c["than"].values()), sum(m["than"].values())
    dong("Thân 8 SKILL.md + 7 agent, cộng", "khi được gọi", tc, tm)
    d += ["", "## Từng skill/agent (ký tự)", "", "| Tệp | Cũ | Mới | Khối cũ | Khối mới |", "|---|---:|---:|---:|---:|"]
    for n in sorted(set(c["than"]) | set(m["than"])):
        d.append(f"| `{n}` | {c['than'].get(n, 0):,} | {m['than'].get(n, 0):,} | {c['khoi'].get(n, 0):,} | {m['khoi'].get(n, 0):,} |")
    d += ["", "Ngưỡng vận hành (ChatGPT L3 P1-1): phần nạp đầu phiên ≤ 1.500 token ≈ 4.500 ký tự — "
          + ("**ĐẠT**" if nm <= 4500 else "**VƯỢT**") + f" ({nm:,} ký tự).",
          "Mô tả skill/agent **chưa rút gọn** trong 1.3.1: mô tả quyết định việc kích hoạt skill; rút gọn cần đo lại tỷ lệ "
          "kích hoạt đúng/sai trên bộ ca nghiệm thu — để sau thí điểm (Báo cáo tiếp thu lần 3)."]
    out = "\n".join(d) + "\n"
    if a.ra:
        io.open(a.ra, "w", encoding="utf-8").write(out)
    print(out)


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
