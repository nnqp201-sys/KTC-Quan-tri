# -*- coding: utf-8 -*-
"""Tu ghi nhat ky phien lam viec va nap lai vao context khi mo phien moi.

Goi tu hooks.json voi 1 trong 4 che do:
  ghi       PostToolUse      — ghi 1 dong JSONL: thoi gian, phien, cong cu, doi tuong (KHONG ghi noi dung tep).
                               1.3.1 (tham dinh lan 3, ChatGPT P0-1): KHONG luu lenh Bash/PowerShell, mo ta Agent,
                               mau Grep/Glob tho — chi luu loai hanh dong + chuong trinh; tep: duong dan tuong doi.
                               Lenh (da che du lieu) chi luu khi chu may chon KTC_NHAT_KY_NOI_DUNG=1.
  yeu-cau   UserPromptSubmit — MAC DINH chi ghi do dai + nhan tin hieu hoc; noi dung (cat 600 ky tu) chi khi
                               nguoi dung chon: mo dau "#học" hoac bien KTC_NHAT_KY_NOI_DUNG=1 (1.3.0, R2-02)
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
SO_DONG_NAP = 5           # so thao tac gan nhat dua vao context (1.3.1: 15 -> 5, khong in lenh)
# 1.3.1 (ChatGPT P1-1): ngan sach phan nap dau phien ~1.500 token (~4.500 ky tu tieng Viet). Vuot thi cat
# danh sach tri thuc, bao so muc con lai. KTC_NAP_DAY_DU=1 -> ban day du (15 thao tac, 12 tep, 160 ky tu/muc).
NGAN_SACH_NAP = 4500
CONG_CU_TEP = ("Write", "Edit", "MultiEdit", "Read", "NotebookEdit")
MAU_GHI_LENH = re.compile(r"(?:>|\b(?:rm|mv|cp|mkdir|touch|tee|del|move|copy|sed\s+-i|set-content|add-content|out-file|"
                          r"remove-item|copy-item|move-item|new-item|rename-item)\b)", re.I)


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


def _tuong_doi(du_an, p: str) -> str:
    p = str(p)
    try:
        if du_an and os.path.abspath(p).lower().startswith(os.path.abspath(du_an).lower() + os.sep):
            return os.path.relpath(p, du_an).replace("\\", "/")
    except (ValueError, OSError):
        pass
    return p.replace("\\", "/")


def phan_loai_lenh(lenh: str) -> dict:
    """Mo ta lenh KHONG luu noi dung: chuong trinh dau tien + loai hanh dong."""
    lenh = str(lenh).strip()
    m = re.match(r"(?:cd\s+(?:\"[^\"]*\"|'[^']*'|\S+)\s*(?:;|&&)\s*)?(?:\w+=\S*\s+)*([^\s;|&]+)", lenh)
    ct = (m.group(1) if m else "").strip("\"'&").replace("\\", "/").rsplit("/", 1)[-1][:24]
    if re.search(r"\bgit\s+(?:commit|push|add|reset|checkout|rm)\b", lenh):
        hd = "git-ghi"
    elif MAU_GHI_LENH.search(lenh):
        hd = "ghi"
    elif re.search(r"\b(?:python\d*|py|node|powershell|pwsh)\b", lenh, re.I):
        hd = "chay-script"
    else:
        hd = "doc"
    return {"chuong_trinh": ct, "hanh_dong": hd}


def doi_tuong(tool: str, inp: dict, du_an: str = None) -> str:
    """Doi tuong DUOC PHEP luu mac dinh: duong dan tep (tuong doi), ten skill, loai agent. Lenh, mo ta Agent,
    mau tim kiem la noi dung tho -> khong tra ve o day (1.3.1, P0-1)."""
    if tool in CONG_CU_TEP:
        s = _tuong_doi(du_an, inp.get("file_path") or inp.get("notebook_path") or "")
    elif tool == "Skill":
        s = inp.get("skill", "")
    elif tool == "Agent":
        s = inp.get("subagent_type", "") or "general"
    else:
        s = ""
    s = che_du_lieu(" ".join(str(s).split()))
    return s[:DAI_TOI_DA] + ("…" if len(s) > DAI_TOI_DA else "")


def chi_tiet_tho(tool: str, inp: dict) -> str:
    """Noi dung tho — CHI luu khi chu may chon KTC_NHAT_KY_NOI_DUNG=1; luon che du lieu."""
    if tool in ("Bash", "PowerShell"):
        s = inp.get("command", "")
    elif tool in ("Grep", "Glob"):
        s = inp.get("pattern", "")
    elif tool == "Agent":
        s = inp.get("description", "")
    else:
        return ""
    s = che_du_lieu(" ".join(str(s).split()))
    return s[:DAI_TOI_DA] + ("…" if len(s) > DAI_TOI_DA else "")


# Tin hieu hoc trong LOI NGUOI DUNG (DL-20260919-005). Chi danh dau de agent ktc-tu-hoc doc lai;
# hook KHONG tu rut ket luan. Nhom: sua-sai · quy-uoc · quyet-dinh.
TIN_HIEU = {
    "sua-sai": r"\b(sai|nhầm|chưa đúng|không đúng|không phải|sửa lại|làm lại|lỗi|thiếu)\b",
    "quy-uoc": r"(từ nay|từ giờ|sau này|luôn luôn|\bluôn\b|đừng|không được|phải|quy ước|lưu ý|nhớ|ghi nhớ|mặc định)",
    "quyet-dinh": r"(đồng ý|thống nhất|chốt|quyết định|phê duyệt|lãnh đạo.{0,20}(đã|thống nhất)|giữ phương án)",
}
# 1.3.0 (TT-20260924-08): bo gan bao gia nhieu — bo loi < 5 tu ("ok", "em cu lam luon"), bo "OK" tran,
# bo so hieu van ban ("Quyet dinh so 1899/QD-CDKT", "QD 1923") truoc khi do tin hieu quyet-dinh.
SO_TU_TOI_THIEU = 5
MAU_SO_HIEU_VB = r"(quyết định|thông báo|kế hoạch|công văn|tờ trình|báo cáo|QĐ|TB|KH|CV|BC)\s*(số\s*)?\d+[\w/\-]*"
# Che du lieu ca nhan truoc khi ghi noi dung (khi nguoi dung da chon ghi)
CHE = [
    (r"(?<![0-9A-Za-z])0\d{11}(?![0-9A-Za-z])", "[SỐ ĐỊNH DANH]"),
    (r"(?<![0-9A-Za-z])(\+84|0)\d{9}(?![0-9A-Za-z])", "[SỐ ĐIỆN THOẠI]"),
    (r"[\w.+-]+@[\w-]+\.[\w.-]+", "[EMAIL]"),
]


def che_du_lieu(s: str) -> str:
    for mau, thay in CHE:
        s = re.sub(mau, thay, s)
    return s
TEP_TRI_THUC = os.path.join("90-Nhat-Ky-Van-Hanh", "05-Tri-Thuc-Tu-Hoc")
DAI_YEU_CAU = 600
SO_TRI_THUC_NAP = 25
NGAY_LUU_GIU = 30          # 1.3.0: tep nhat ky cu hon 30 ngay bi xoa khi mo phien (che do nap)


def don_nhat_ky_cu(du_an: str, ngay: int = NGAY_LUU_GIU) -> int:
    """Xoa tep YYYY-MM-DD.jsonl cu hon `ngay` ngay. Tra ve so tep da xoa."""
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    if not os.path.isdir(thu_muc):
        return 0
    moc = dt.date.today() - dt.timedelta(days=ngay)
    xoa = 0
    for f in os.listdir(thu_muc):
        m = re.fullmatch(r"(\d{4}-\d{2}-\d{2})\.jsonl", f)
        if not m:
            continue
        try:
            if dt.date.fromisoformat(m.group(1)) < moc:
                os.remove(os.path.join(thu_muc, f))
                xoa += 1
        except (ValueError, OSError):
            pass
    return xoa


def tin_hieu(s: str):
    if len(s.split()) < SO_TU_TOI_THIEU:
        return []
    s = re.sub(MAU_SO_HIEU_VB, " ", s, flags=re.I)
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
        inp = data.get("tool_input") or {}
        dt_ = doi_tuong(tool, inp, du_an)
        if dt_:
            dong["doi_tuong"] = dt_
        if tool in ("Bash", "PowerShell"):
            dong.update(phan_loai_lenh(inp.get("command", "")))
        if os.environ.get("KTC_NHAT_KY_NOI_DUNG") == "1":
            ct = chi_tiet_tho(tool, inp)
            if ct:
                dong["chi_tiet"] = ct
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
        # 1.3.0 (tham dinh lan 2, R2-02): MAC DINH chi ghi thong tin mo ta — do dai + nhan tin hieu.
        # Noi dung chi ghi khi nguoi dung CHU DONG chon, va luon che du lieu ca nhan truoc khi ghi:
        #   - loi nhan mo dau "#học": ghi loi nhan do (du co tin hieu hay khong);
        #   - chu may tu dat KTC_NHAT_KY_NOI_DUNG=1 (vd .claude/settings.local.json cua du an): chi ghi loi
        #     CO tin hieu hoc — dung nguon ma agent ktc-tu-hoc can, bo qua moi loi nhan con lai.
        dong["do_dai"] = len(s)
        chon_hoc = re.match(r"#h[oọ]c\b", s, re.I)
        if chon_hoc:
            s = s[chon_hoc.end():].strip()
        th = tin_hieu(s)
        if th:
            dong["tin_hieu"] = th
        if chon_hoc or (th and os.environ.get("KTC_NHAT_KY_NOI_DUNG") == "1"):
            dong["chon_ghi"] = "#học" if chon_hoc else "KTC_NHAT_KY_NOI_DUNG"
            s = che_du_lieu(s)
            dong["noi_dung"] = s[:DAI_YEU_CAU] + ("…" if len(s) > DAI_YEU_CAU else "")
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


def nap_tri_thuc(du_an: str, ra: list, day_du: bool = False):
    """Tri thuc tu hoc con hieu luc/cho duyet + so tin hieu hoc CHUA xu ly ke tu lan hoc cuoi -> `ra` (danh sach dong)."""
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
    ra.append(f"--- Tri thức tự học ({len(muc)} mục hiệu lực/chờ duyệt — {TEP_TRI_THUC}/TRI-THUC.md) ---")
    dai = 160 if day_du else 100
    for o in muc[-SO_TRI_THUC_NAP:]:
        dau = "?" if o[5].lower().startswith("chờ") else "•"
        noi = o[2] if len(o[2]) <= dai else o[2][:dai - 1] + "…"
        ra.append(f"  {dau} [{o[0]}·{o[1]}] {noi}")
    if chua:
        ra.append(f"  ⟳ {len(chua)} tín hiệu học CHƯA xử lý — gọi agent ktc-tu-hoc để rút tri thức.")


def lam_sach_nhat_ky_cu(du_an: str) -> int:
    """1.3.1 (P0-1): go lenh/mo ta/mau tho khoi nhat ky da ghi truoc 1.3.1 — tru khi chu may chon ghi noi dung.
    Tra ve so dong da lam sach. Ghi lai tep qua tep tam roi thay the (khong de tep do dang)."""
    if os.environ.get("KTC_NHAT_KY_NOI_DUNG") == "1":
        return 0
    thu_muc = os.path.join(du_an, THU_MUC_LOG)
    if not os.path.isdir(thu_muc):
        return 0
    n = 0
    for f in os.listdir(thu_muc):
        if not f.endswith(".jsonl"):
            continue
        p = os.path.join(thu_muc, f)
        dong, doi = [], False
        for line in io.open(p, encoding="utf-8", errors="ignore"):
            try:
                d = json.loads(line)
            except Exception:
                continue
            cc = d.get("cong_cu")
            if d.get("loai") == "thao-tac" and cc not in CONG_CU_TEP and cc != "Skill" and "hanh_dong" not in d \
                    and d.get("doi_tuong"):
                tho = d.pop("doi_tuong")
                if cc in ("Bash", "PowerShell"):
                    d.update(phan_loai_lenh(tho))
                elif cc == "Agent":
                    d["doi_tuong"] = tho.split(":", 1)[0].strip() or "general"
                d["da_lam_sach"] = "1.3.1"
                doi, n = True, n + 1
            d.pop("chi_tiet", None)
            dong.append(d)
        if doi:
            tam = p + ".tam"
            with io.open(tam, "w", encoding="utf-8") as h:
                for d in dong:
                    h.write(json.dumps(d, ensure_ascii=False) + "\n")
            os.replace(tam, p)
    return n


def che_do_nap(data: dict):
    du_an = tim_du_an(data)
    if not du_an:
        return
    day_du = os.environ.get("KTC_NAP_DAY_DU") == "1"
    don_nhat_ky_cu(du_an)
    lam_sach_nhat_ky_cu(du_an)
    dong = doc_log(du_an)
    thao_tac = [d for d in dong if d.get("loai") == "thao-tac"]
    sua_tat_ca = {_tuong_doi(du_an, d["doi_tuong"]) for d in thao_tac
                  if d.get("cong_cu") in ("Write", "Edit", "MultiEdit") and d.get("doi_tuong")}
    # chi in tep TRONG du an (duong dan tuong doi); tep ngoai (thu muc tam...) chi dem
    sua = sorted(x for x in sua_tat_ca if not (":" in x[:3] or x.startswith("/")))
    ngoai = len(sua_tat_ca) - len(sua)
    loi = [d for d in thao_tac if d.get("loi")]
    phien = sorted({d.get("phien") for d in dong if d.get("phien")})

    dau = ["=== KTC-Quan-tri — nhật ký tự động 2 ngày gần nhất (nạp vào context) ==="]
    if not dong:
        dau.append("Chưa có nhật ký tự động. (Ghi bắt đầu từ phiên này.)")
    else:
        dau.append(f"{len(phien)} phiên · {len(thao_tac)} thao tác · {len(sua)} tệp dự án đã ghi/sửa"
                   + (f" (+{ngoai} tệp ngoài dự án)" if ngoai else "") + f" · {len(loi)} thao tác lỗi")
        so_tep = 12 if day_du else 8
        if sua:
            dau.append(f"Tệp dự án đã ghi/sửa ({min(len(sua), so_tep)}/{len(sua)}):")
            dau += [f"  - {s}" for s in sua[-so_tep:]]
        so = 15 if day_du else SO_DONG_NAP
        dau.append(f"{so} thao tác gần nhất (không in lệnh — P0-1):")
        for d in thao_tac[-so:]:
            ky = "✗" if d.get("loi") else "·"
            if d.get("cong_cu") in ("Bash", "PowerShell"):
                pl = d if "hanh_dong" in d else phan_loai_lenh(d.get("doi_tuong", ""))
                mo_ta = f"{pl.get('chuong_trinh', '')} ({pl.get('hanh_dong', '')})"
            elif d.get("cong_cu") in CONG_CU_TEP or d.get("cong_cu") in ("Skill", "Agent"):
                mo_ta = _tuong_doi(du_an, d.get("doi_tuong", "")).split(":", 1)[0] if d.get("cong_cu") == "Agent"                     else _tuong_doi(du_an, d.get("doi_tuong", ""))
            else:
                mo_ta = ""
            dau.append(f"  {ky} {d['t'][5:16]} {d.get('cong_cu', ''):10s} {mo_ta[:90]}")

    tri = []
    nap_tri_thuc(du_an, tri, day_du)

    duoi = []
    pm = moi_nhat(os.path.join(du_an, "90-Nhat-Ky-Van-Hanh", "03-Process-Memory"))
    cp = moi_nhat(os.path.join(du_an, "92-Kinh-Nghiem", "03-Change-Proposals"))
    dl = moi_nhat(os.path.join(du_an, "92-Kinh-Nghiem", "06-Decision-Log"))
    duoi.append("Bản ghi gần nhất:")
    for nhan, v in (("Process Memory", pm), ("Đề xuất cải tiến", cp), ("Decision Log", dl)):
        duoi.append(f"  - {nhan}: {v or '(chưa có)'}")
    duoi.append("Nhắc: đọc MEMORY-INDEX.md và Pending.md trước khi làm việc (CLAUDE.md).")
    duoi.append("=" * 72)

    # Ngan sach: cat bot muc tri thuc CU NHAT (giu dong tieu de va dong tin hieu) cho toi khi vua
    if not day_du:
        def tong():
            return sum(len(x) + 1 for x in dau + tri + duoi)
        bo = 0
        while tong() > NGAN_SACH_NAP - 80 and len(tri) > 2:
            del tri[1]
            bo += 1
        if bo:
            tri.insert(1, f"  … {bo} mục cũ hơn không nạp (ngân sách context) — đọc TRI-THUC.md khi cần.")
    print("\n".join(dau + tri + duoi))


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
