# -*- coding: utf-8 -*-
"""Tu ghi nhat ky phien lam viec va nap lai vao context khi mo phien moi.

Goi tu hooks.json voi 1 trong 4 che do:
  ghi       PostToolUse      — ghi 1 dong JSONL: thoi gian, phien, cong cu, doi tuong (KHONG ghi noi dung tep)
  yeu-cau   UserPromptSubmit — ghi loi nguoi dung (cat 600 ky tu) + tin hieu hoc (DL-20260919-005)
  ket-phien SessionEnd       — ghi dong danh dau ket thuc phien
  nap       SessionStart     — in tom tat 2 ngay + tri thuc tu hoc + so tin hieu chua hoc -> context

Chi hoat dong khi thu muc du an co `90-Nhat-Ky-Van-Hanh/` (tuc la dang lam viec trong KTC-Quan-tri) —
plugin bat o cap nguoi dung nen phai tu gioi han pham vi, khong ghi log vao du an khac.
Moi loi deu nuot va thoat 0: hook ghi log khong bao gio duoc lam hong phien lam viec.
"""
import datetime as dt
import io
import json
import os
import re
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


# Tin hieu hoc trong LOI NGUOI DUNG (DL-20260919-005). Chi danh dau de agent ktc-tu-hoc doc lai;
# hook KHONG tu rut ket luan. Nhom: sua-sai · quy-uoc · quyet-dinh.
TIN_HIEU = {
    "sua-sai": r"\b(sai|nhầm|chưa đúng|không đúng|không phải|sửa lại|làm lại|lỗi|thiếu)\b",
    "quy-uoc": r"(từ nay|từ giờ|sau này|luôn luôn|\bluôn\b|đừng|không được|phải|quy ước|lưu ý|nhớ|ghi nhớ|mặc định)",
    "quyet-dinh": r"(đồng ý|thống nhất|chốt|quyết định|phê duyệt|lãnh đạo.{0,20}(đã|thống nhất)|giữ phương án|\bOK\b)",
}
TEP_TRI_THUC = os.path.join("90-Nhat-Ky-Van-Hanh", "05-Tri-Thuc-Tu-Hoc")
DAI_YEU_CAU = 600
SO_TRI_THUC_NAP = 25


def tin_hieu(s: str):
    import re
    return [k for k, m in TIN_HIEU.items() if re.search(m, s, re.I)]


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
    elif loai == "yeu-cau":
        s = " ".join(str(data.get("prompt") or "").split())
        # Lenh noi bo cua Claude Code (/compact, <command-...>) khong phai loi nguoi dung
        if not s or s.startswith("<") or s.startswith("/"):
            return
        # "#riêng ..." — nguoi dung tu danh dau noi dung rieng tu: chi ghi moc thoi gian (CP-20260924-001, C)
        if re.match(r"#ri[eê]ng\b", s, re.I):
            dong["noi_dung"] = "[#riêng — không ghi]"
            ghi_dong(du_an, dong)
            return
        dong["noi_dung"] = s[:DAI_YEU_CAU] + ("…" if len(s) > DAI_YEU_CAU else "")
        th = tin_hieu(s)
        if th:
            dong["tin_hieu"] = th
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


def nap_tri_thuc(du_an: str):
    """In tri thuc tu hoc con hieu luc/cho duyet + so tin hieu hoc CHUA xu ly ke tu lan hoc cuoi."""
    import re
    thu_muc = os.path.join(du_an, TEP_TRI_THUC)
    tep = os.path.join(thu_muc, "TRI-THUC.md")
    muc = []
    if os.path.isfile(tep):
        for d in io.open(tep, encoding="utf-8", errors="ignore"):
            o = [x.strip() for x in d.strip().strip("|").split("|")]
            if len(o) >= 6 and re.match(r"TT-\d{8}-\d+", o[0]) and re.match(r"(hiệu lực|chờ duyệt)", o[5], re.I):
                muc.append(o)
    moc = ""
    try:
        moc = io.open(os.path.join(thu_muc, ".lan-hoc-cuoi"), encoding="utf-8").read().strip()
    except OSError:
        pass
    chua = [d for d in doc_log(du_an, so_ngay=14)
            if d.get("loai") == "yeu-cau" and d.get("tin_hieu") and d.get("t", "") > moc]
    print(f"--- Tri thức tự học ({len(muc)} mục hiệu lực/chờ duyệt — {TEP_TRI_THUC}/TRI-THUC.md) ---")
    for o in muc[-SO_TRI_THUC_NAP:]:
        dau = "?" if o[5].lower().startswith("chờ") else "•"
        print(f"  {dau} [{o[0]}·{o[1]}] {o[2][:160]}")
    if chua:
        print(f"  ⟳ {len(chua)} tín hiệu học CHƯA xử lý (lời người dùng có sửa sai/quy ước/quyết định) — "
              "gọi agent ktc-tu-hoc để rút tri thức.")


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

    nap_tri_thuc(du_an)

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
        elif che_do == "yeu-cau":
            che_do_ghi(data, "yeu-cau")
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
