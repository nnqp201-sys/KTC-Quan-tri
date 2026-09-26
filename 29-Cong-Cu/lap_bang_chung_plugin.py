# -*- coding: utf-8 -*-
"""Lap ho so BANG CHUNG kiem thu cho ban plugin vua dung — moi con so lay tu nhat ky that, khong chep tay.

Chay SAU `python 29-Cong-Cu/dong_goi_plugin.py`:
    python 29-Cong-Cu/lap_bang_chung_plugin.py [--claude <duong dan claude.exe>]

Ghi vao 30-Ket-Qua/<ngay>/Plugin/:
    log-hoi-quy/<bo>.txt + 00-TONG-HOP.txt   nhat ky rieng tung bo hoi quy (ket luan theo MA THOAT)
    log-kiem-tra-he-thong-<pb>.txt           kiem tra tinh toan he
    log-validate-strict-<pb>.txt             claude plugin validate --strict (co dong lenh, phien ban CLI)
    DANH-MUC-TEP-<pb>.md                     moi tep trong zip + SHA-256 tung tep
    GHI-CHU-PHAT-HANH-<pb>.md                ma SHA-256 cua goi (de NGOAI zip)
    BANG-CHUNG-KIEM-THU-<pb>.md              tong hop: artifact, hooks truoc/sau, moi truong, ket qua, viec chua lam
Nguon goc yeu cau: tham dinh doc lap lan 2 (ChatGPT R2-04, muc 9), kiem san pham doc lap C3, C7, C21.
"""
import argparse
import datetime as dt
import glob
import hashlib
import io
import json
import os
import platform
import re
import subprocess
import sys
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(DU_AN, "92-Kinh-Nghiem", "02-Regression", "Cases")
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")
ENV.pop("KTC_NHAT_KY_NOI_DUNG", None)   # ca thu chay o che do mac dinh


def chay(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=ENV, cwd=DU_AN, **kw)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def tim_claude(chi_dinh):
    if chi_dinh:
        return chi_dinh
    ung = sorted(glob.glob(os.path.expanduser(
        r"~\.vscode\extensions\anthropic.claude-code-*\resources\native-binary\claude.exe")))
    return ung[-1] if ung else "claude"


def phien_ban_plugin():
    return json.load(io.open(os.path.join(DU_AN, "31-Plugin", ".claude-plugin", "plugin.json"), encoding="utf-8"))["version"]


def lenh_hook(h):
    ra = []
    for ev, arr in h["hooks"].items():
        for g in arr:
            for x in g["hooks"]:
                ra.append(f"{ev}: " + x["command"].split("/scripts/")[-1].replace('"', ""))
    return ra


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claude")
    ap.add_argument("--truoc", help="zip ban truoc de so sanh (mac dinh: tim ban gan nhat khac phien ban)")
    a = ap.parse_args()
    pb = phien_ban_plugin()
    ra = os.path.join(DU_AN, "30-Ket-Qua", dt.date.today().isoformat(), "Plugin")
    zp = os.path.join(ra, f"ktc-quan-tri-{pb}.zip")
    if not os.path.isfile(zp):
        raise SystemExit(f"Chua co {zp} — chay dong_goi_plugin.py truoc")
    ma = sha(zp)
    ghi = open(zp + ".sha256", encoding="utf-8").read().split()[0]
    if ma != ghi:
        raise SystemExit(f"SHA-256 tinh lai ({ma}) khac tep .sha256 ({ghi})")

    # 1) hoi quy tung bo
    thu_muc_hq = os.path.join(ra, "log-hoi-quy")
    os.makedirs(thu_muc_hq, exist_ok=True)
    kq_bo = []
    for f in sorted(glob.glob(os.path.join(REG, "test_*.py"))):
        ten = os.path.splitext(os.path.basename(f))[0]
        rc, out = chay([sys.executable, f], timeout=900)
        io.open(os.path.join(thu_muc_hq, ten + ".txt"), "w", encoding="utf-8").write(out)
        ok = len(re.findall(r"^\s*OK\b", out, re.M))
        kq_bo.append((ten, rc, ok))
    tong = ["# Tổng hợp bộ hồi quy — kết luận theo MÃ THOÁT (0 = đạt). Cột OK đếm dòng 'OK' in ra;",
            "# bộ in theo định dạng khác (OK=0) xem nhật ký riêng. Dòng ✗ trong ca thử ngược là lỗi cài cố ý."]
    tong += [f"{t} ma={rc} OK={ok}" for t, rc, ok in kq_bo]
    io.open(os.path.join(thu_muc_hq, "00-TONG-HOP.txt"), "w", encoding="utf-8").write("\n".join(tong) + "\n")
    so_dat = sum(1 for _, rc, _ in kq_bo if rc == 0)

    # 2) kiem tra tinh
    rc_kt, out_kt = chay([sys.executable, os.path.join(DU_AN, "29-Cong-Cu", "kiem_tra_he_thong.py")], timeout=1800)
    io.open(os.path.join(ra, f"log-kiem-tra-he-thong-{pb}.txt"), "w", encoding="utf-8").write(out_kt)
    kl_kt = (re.search(r"KẾT LUẬN: .*", out_kt) or [""])[0] if re.search(r"KẾT LUẬN: .*", out_kt) else "(không đọc được kết luận)"

    # 3) validate --strict
    cl = tim_claude(a.claude)
    _, ver = chay([cl, "--version"])
    rc_v, out_v = chay([cl, "plugin", "validate", "./31-Plugin", "--strict"], timeout=300)
    io.open(os.path.join(ra, f"log-validate-strict-{pb}.txt"), "w", encoding="utf-8").write(
        f"# Lệnh: claude plugin validate ./31-Plugin --strict\n# CLI: {ver.strip()}\n"
        f"# Thời điểm: {dt.datetime.now():%d/%m/%Y %H:%M}\n{out_v}\n# Mã thoát: {rc_v}\n")

    # 4) danh muc tep
    z = zipfile.ZipFile(zp)
    ten_tep = sorted(z.namelist())
    dm = ["# Danh mục tệp — " + os.path.basename(zp), "", "| Tệp | Byte | SHA-256 |", "|---|---:|---|"]
    for n in ten_tep:
        b = z.read(n)
        dm.append(f"| `{n}` | {len(b)} | `{hashlib.sha256(b).hexdigest()}` |")
    io.open(os.path.join(ra, f"DANH-MUC-TEP-{pb}.md"), "w", encoding="utf-8").write("\n".join(dm) + "\n")
    cam = {"`.git/`": any(".git/" in n for n in ten_tep), "`KPI-ca-nhan/`": any("KPI-ca-nhan" in n for n in ten_tep),
           "`*.jsonl`": any(n.endswith(".jsonl") for n in ten_tep),
           "`ktc_backup_github.py`": any(n.endswith("ktc_backup_github.py") for n in ten_tep)}

    # 5) so voi ban truoc
    truoc = a.truoc
    if not truoc:
        ung = [p for p in glob.glob(os.path.join(DU_AN, "30-Ket-Qua", "*", "Plugin", "ktc-quan-tri-*.zip"))
               if not p.endswith(f"-{pb}.zip")]
        truoc = max(ung, key=os.path.getmtime) if ung else None
    so_sanh, hook_bang = "(không có bản trước)", []
    if truoc:
        zt = zipfile.ZipFile(truoc)
        nt, nm = set(zt.namelist()), set(ten_tep)
        so_sanh = (f"`{os.path.basename(truoc)}` SHA-256 `{sha(truoc)}`; thêm {len(nm - nt)} tệp: "
                   + (", ".join(f"`{x}`" for x in sorted(nm - nt)) or "—") + f"; bỏ {len(nt - nm)} tệp: "
                   + (", ".join(f"`{x}`" for x in sorted(nt - nm)) or "—"))
        a1, b1 = lenh_hook(json.loads(zt.read("hooks/hooks.json"))), lenh_hook(json.loads(z.read("hooks/hooks.json")))
        hook_bang = ["| Bản trước | Bản này |", "|---|---|"] + [
            f"| {a1[i] if i < len(a1) else ''} | {b1[i] if i < len(b1) else ''} |" for i in range(max(len(a1), len(b1)))]

    # 6) moi truong
    def pb_mod(m):
        try:
            mod = __import__(m)
            return getattr(mod, "__version__", "?")
        except Exception:
            return "không có"
    _, head = chay(["git", "rev-parse", "--short", "HEAD"])
    # Chi xet NGUON dung plugin (tru 30-Ket-Qua/ — noi chinh ho so nay duoc ghi); tep chua theo doi o goc
    # khong thuoc nguon dung cung duoc bo qua neu nam ngoai cac thu muc nguon.
    nguon = ["20-Chuan-Chung", "22-KTC-Dieu-Phoi", "23-KTC-Ke-Hoach", "24-KTC-Theo-doi-CV", "25-KTC-Bao-Cao",
             "26-KTC-Soan-Thao-VB", "27-KTC-The-Thuc", "28-KTC-KPI", "29-Cong-Cu", "31-Plugin",
             "92-Kinh-Nghiem/02-Regression"]
    _, trang = chay(["git", "status", "--short", "--", *nguon])
    so_thay = len([x for x in trang.splitlines() if x.strip()])
    git_dong = (f"`{head.strip()}` — mã nguồn dựng plugin sạch (không có thay đổi chưa commit trong "
                f"{len(nguon)} thư mục nguồn): bản dựng truy về đúng commit này" if so_thay == 0 else
                f"`{head.strip()}` + {so_thay} tệp nguồn thay đổi chưa commit — chưa truy về được một commit")

    io.open(os.path.join(ra, f"GHI-CHU-PHAT-HANH-{pb}.md"), "w", encoding="utf-8").write(f"""# Ghi chú phát hành — plugin KTC-Quan-tri {pb}

**Trạng thái:** đã dựng, kiểm thử ({dt.date.today():%d/%m/%Y}) — **chưa phân phối**. Chỉ phân phối sau nghiệm thu 3 nền tảng và rà
soát 897 (Dự thảo Thông báo hướng dẫn sử dụng).

| Mục | Giá trị |
|---|---|
| Tệp | `{os.path.basename(zp)}` ({len(ten_tep)} tệp) |
| SHA-256 | `{ma}` |
| Đối chiếu (PowerShell) | `Get-FileHash {os.path.basename(zp)} -Algorithm SHA256` — phải trùng mã trên |
| Thay đổi | `31-Plugin/CHANGELOG.md` mục {pb} (có trong zip) |
| Bằng chứng | `BANG-CHUNG-KIEM-THU-{pb}.md`, `DANH-MUC-TEP-{pb}.md`, `log-*.txt`, `log-hoi-quy/` |

Mã SHA-256 để ngoài zip vì ghi mã vào trong gói sẽ làm đổi chính mã đó.
""")

    L = [f"# Bằng chứng kiểm thử — plugin ktc-quan-tri {pb}", "",
         f"**Lập tự động** bởi `29-Cong-Cu/lap_bang_chung_plugin.py` lúc {dt.datetime.now():%d/%m/%Y %H:%M} — mọi con số lấy "
         "từ nhật ký trong thư mục này.", "",
         "## 1. Artifact", "", "| Mục | Giá trị |", "|---|---|",
         f"| Tệp | `{os.path.basename(zp)}` ({len(ten_tep)} tệp) |", f"| SHA-256 | `{ma}` (tính lại khớp tệp `.sha256`) |",
         "| Lặp lại được | `log-dung-*-lan-2.txt` nếu có (dòng cuối ghi mã của hai lần dựng) |",
         f"| Danh mục tệp | `DANH-MUC-TEP-{pb}.md` (SHA-256 từng tệp) |", f"| So với bản trước | {so_sanh} |",
         "| Không chứa | " + ", ".join(k for k, v in cam.items() if not v) +
         (" — **CÓ:** " + ", ".join(k for k, v in cam.items() if v) if any(cam.values()) else "") + " |", ""]
    if hook_bang:
        L += ["## 2. Hooks — trước và sau", ""] + hook_bang + [""]
    L += ["## 3. Môi trường", "", "| Thành phần | Phiên bản |", "|---|---|",
          f"| Hệ điều hành | {platform.platform()} |", f"| Python | {sys.version.split()[0]} |",
          f"| python-docx | {pb_mod('docx')} |", f"| openpyxl | {pb_mod('openpyxl')} |", f"| lxml | {pb_mod('lxml')} |",
          f"| Claude Code CLI | {ver.strip() or 'không chạy được'} |", f"| Git | {git_dong} |", "",
          "## 4. Kết quả", "", "| Phép kiểm | Kết quả | Nhật ký |", "|---|---|---|",
          f"| `claude plugin validate ./31-Plugin --strict` | {'ĐẠT' if rc_v == 0 else 'KHÔNG ĐẠT'} (mã {rc_v}) | `log-validate-strict-{pb}.txt` |",
          f"| Kiểm tra tĩnh toàn hệ | {kl_kt} (mã {rc_kt}) | `log-kiem-tra-he-thong-{pb}.txt` |",
          f"| Bộ hồi quy | {so_dat}/{len(kq_bo)} bộ mã thoát 0 | `log-hoi-quy/` |", "",
          "| Bộ | Mã thoát | Dòng OK |", "|---|---:|---:|"] + [f"| `{t}` | {rc} | {ok} |" for t, rc, ok in kq_bo]
    L += ["", "## 5. Chưa thực hiện (không trình bày như đã đạt)", "",
          "- Nghiệm thu trên Claude (trò chuyện) và Claude Cowork.",
          "- Kiểm kê, thu hồi bản cũ ở cấp tổ chức (Phòng QLKHCN&HTPT, quyền Owner).",
          "- Guard không phân tích mã Python/JS nhúng trong lệnh shell; máy không có Python thì hook không chạy.",
          "- Kiểm thử dùng dữ liệu giả lập hoặc mẫu biểu; chưa có dữ liệu vận hành thật."]
    io.open(os.path.join(ra, f"BANG-CHUNG-KIEM-THU-{pb}.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"SHA-256 {ma} · {len(ten_tep)} tệp · hồi quy {so_dat}/{len(kq_bo)} · {kl_kt} · validate mã {rc_v}")
    return 0 if (so_dat == len(kq_bo) and rc_kt == 0 and rc_v == 0) else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
