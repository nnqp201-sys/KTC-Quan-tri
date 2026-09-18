# -*- coding: utf-8 -*-
"""Tu ghi nhat ky phien lam viec va nap lai vao context khi mo phien moi.

Goi tu hooks.json voi 1 trong 3 che do:
  ghi       PostToolUse  — ghi 1 dong JSONL: thoi gian, phien, cong cu, doi tuong (KHONG ghi noi dung)
  ket-phien SessionEnd   — ghi dong danh dau ket thuc phien
  nap       SessionStart — in tom tat 2 ngay gan nhat ra stdout -> Claude Code dua vao context

Chi hoat dong khi thu muc du an co `90-Nhat-Ky-Van-Hanh/` (tuc la dang lam viec trong KTC-Quan-tri) —
plugin bat o cap nguoi dung nen phai tu gioi han pham vi, khong ghi log vao du an khac.
Moi loi deu nuot va thoat 0: hook ghi log khong bao gio duoc lam hong phien lam viec.
"""
import datetime as dt
import io
import json
import os
import sys

THU_MUC_LOG = os.path.join("90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
DAI_TOI_DA = 200          # cat ngan lenh/duong dan dai
SO_DONG_NAP = 15          # so thao tac gan nhat dua vao context


def doc_stdin() -> dict:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def tim_du_an(data: dict):
    # Chi lui ve getcwd khi hook KHONG cho biet thu muc nao — neu hook da cho cwd ngoai du an
    # thi phai bo qua, khong duoc ghi nham vao du an dang chua script (loi 18/9/2026).
    ung_vien = [os.environ.get("CLAUDE_PROJECT_DIR"), data.get("cwd")]
    if not any(ung_vien):
        ung_vien.append(os.getcwd())
    for p in ung_vien:
        if not p:
            continue
        p = os.path.abspath(p)
        # di nguoc len toi da 4 cap de tim goc du an
        for _ in range(5):
            if os.path.isdir(os.path.join(p, "90-Nhat-Ky-Van-Hanh")):
                return p
            cha = os.path.dirname(p)
            if cha == p:
                break
            p = cha
    return None


def doi_tuong(tool: str, inp: dict) -> str:
    if tool in ("Write", "Edit", "Read", "NotebookEdit"):
        s = inp.get("file_path", "")
    elif tool in ("Bash", "PowerShell"):
        s = inp.get("command", "")
    elif tool in ("Grep", "Glob"):
        s = inp.get("pattern", "")
    elif tool == "Skill":
        s = inp.get("skill", "")
    elif tool == "Agent":
        s = f'{inp.get("subagent_type", "")}: {inp.get("description", "")}'
    else:
        s = ""
    s = " ".join(str(s).split())
    return s[:DAI_TOI_DA] + ("…" if len(s) > DAI_TOI_DA else "")


def ghi_dong(du_an: str, dong: dict):
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    os.makedirs(thu_muc, exist_ok=True)
    tep = os.path.join(thu_muc, dt.date.today().isoformat() + ".jsonl")
    with io.open(tep, "a", encoding="utf-8") as f:
        f.write(json.dumps(dong, ensure_ascii=False) + "\n")


def che_do_ghi(data: dict, loai: str):
    du_an = tim_du_an(data)
    if not du_an:
        return
    tool = data.get("tool_name", "")
    if loai == "thao-tac" and not tool:
        return  # du lieu hook hong/thieu — khong ghi dong rong
    dong = {
        "t": dt.datetime.now().isoformat(timespec="seconds"),
        "phien": (data.get("session_id") or "")[:8],
        "loai": loai,
    }
    if loai == "thao-tac":
        dong["cong_cu"] = tool
        dong["doi_tuong"] = doi_tuong(tool, data.get("tool_input") or {})
        resp = data.get("tool_response")
        if isinstance(resp, dict) and (resp.get("is_error") or resp.get("error")):
            dong["loi"] = True
    else:
        dong["ly_do"] = data.get("reason", "")
    ghi_dong(du_an, dong)


def doc_log(du_an: str, so_ngay: int = 2):
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    if not os.path.isdir(thu_muc):
        return []
    tep = sorted(f for f in os.listdir(thu_muc) if f.endswith(".jsonl"))[-so_ngay:]
    dong = []
    for f in tep:
        with io.open(os.path.join(thu_muc, f), encoding="utf-8", errors="ignore") as h:
            for line in h:
                try:
                    dong.append(json.loads(line))
                except Exception:
                    pass
    return dong


def moi_nhat(thu_muc: str):
    if not os.path.isdir(thu_muc):
        return None
    tep = sorted(f for f in os.listdir(thu_muc) if f.endswith(".md"))
    return tep[-1] if tep else None


def che_do_nap(data: dict):
    du_an = tim_du_an(data)
    if not du_an:
        return
    dong = doc_log(du_an)
    thao_tac = [d for d in dong if d.get("loai") == "thao-tac"]
    sua = sorted({d["doi_tuong"] for d in thao_tac
                  if d.get("cong_cu") in ("Write", "Edit") and d.get("doi_tuong")})
    loi = [d for d in thao_tac if d.get("loi")]
    phien = sorted({d.get("phien") for d in dong if d.get("phien")})

    print("=== KTC-Quan-tri — nhật ký tự động 2 ngày gần nhất (nạp vào context) ===")
    if not dong:
        print("Chưa có nhật ký tự động. (Ghi bắt đầu từ phiên này.)")
    else:
        print(f"{len(phien)} phiên · {len(thao_tac)} thao tác · {len(sua)} tệp đã ghi/sửa · "
              f"{len(loi)} thao tác lỗi")
        if sua:
            print("Tệp đã ghi/sửa:")
            for s in sua[-12:]:
                print(f"  - {s}")
        print(f"{SO_DONG_NAP} thao tác gần nhất:")
        for d in thao_tac[-SO_DONG_NAP:]:
            dau = "✗" if d.get("loi") else "·"
            print(f"  {dau} {d['t'][5:16]} {d.get('cong_cu', ''):10s} {d.get('doi_tuong', '')[:110]}")

    pm = moi_nhat(os.path.join(du_an, "90-Nhat-Ky-Van-Hanh", "03-Process-Memory"))
    cp = moi_nhat(os.path.join(du_an, "92-Kinh-Nghiem", "03-Change-Proposals"))
    dl = moi_nhat(os.path.join(du_an, "92-Kinh-Nghiem", "06-Decision-Log"))
    print("Bản ghi gần nhất:")
    for nhan, v in (("Process Memory", pm), ("Đề xuất cải tiến", cp), ("Decision Log", dl)):
        print(f"  - {nhan}: {v or '(chưa có)'}")
    print("Nhắc: đọc MEMORY-INDEX.md và Pending.md trước khi làm việc (CLAUDE.md).")
    print("=" * 72)


def main():
    che_do = sys.argv[1] if len(sys.argv) > 1 else "ghi"
    data = doc_stdin()
    try:
        if che_do == "ghi":
            che_do_ghi(data, "thao-tac")
        elif che_do == "ket-phien":
            che_do_ghi(data, "ket-phien")
        elif che_do == "nap":
            che_do_nap(data)
    except Exception:
        pass   # hook log khong duoc lam hong phien


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
    raise SystemExit(0)
