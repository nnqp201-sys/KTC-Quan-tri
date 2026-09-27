# -*- coding: utf-8 -*-
"""PreToolUse guard cua plugin ktc-quan-tri — chan GHI/XOA vao kho chuan (tham dinh doc lap lan 1, C-04; lan 2, R2-03).

Vung bao ve (so khop khong phan biet hoa thuong, ca "/" lan "\\"):
  - KTC-Database        (kho van ban, chi doc — CLAUDE.md)
  - 03-Templates        (mau .dotx/.xltx, ke ca "03-Templates(1)")
  - 04-Good-Documents   (van ban tot da ban hanh)

Pham vi kiem:
  - Write · Edit · MultiEdit · NotebookEdit: duong dan dich (file_path / notebook_path).
  - Bash · PowerShell: lenh o MUC SHELL co tac dung ghi/xoa ma DICH nam trong vung bao ve
    (rm, mv, del, rmdir, Remove-Item, Move-Item, Rename-Item, Set-Content, Add-Content, Out-File,
    New-Item, Clear-Content, chuyen huong > / >>, cp/copy/Copy-Item co DICH trong vung bao ve,
    tee, sed -i, truncate, touch).
  - 1.3.1 (tham dinh lan 3, ChatGPT P0-2): hai tang.
    TANG 1 — CHAN (exit 2) khi xac dinh chac dich ghi nam trong vung bao ve: lenh long trong
      `powershell -Command`, `pwsh -c`, `cmd /c`, `bash -c`/`sh -c` (kiem de quy); `open('<vung>', 'w')`,
      `Path('<vung>').write_text/unlink/...` trong ma Python nhung; `cd`/`Set-Location` vao vung roi ghi
      duong dan tuong doi; `-EncodedCommand` (khong phan tich duoc -> chan).
    TANG 2 — HOI NGUOI DUNG (permissionDecision "ask") khi dich KHONG xac dinh duoc: lenh co nhac vung bao ve
      VA co dau hieu ghi VA co ma nhung (python/node/perl/powershell...) hoac bien tro vao vung bao ve.
  - Van KHONG phai lop bao ve tuyet doi: script trong tep (`python x.py`), bien moi truong dat o phien truoc,
    lien ket tuong trung... khong nhin thay duoc. Lop bao ve CHINH la phan quyen chi doc (Viewer) tren Drive.

Doc tu vung bao ve (cat, ls, python doc tep, cp TU kho RA ngoai) duoc phep.

Fail-closed: loi doc du lieu hook hoac loi noi bo -> CHAN (exit 2). Harness chi chan khi hook tra 2;
neu may khong co Python thi hook khong chay duoc — doctor dau phien bao "guard CHUA hoat dong".
Ma thoat: 0 = cho phep · 2 = chan (thong bao ra stderr cho Claude).
"""
import json
import re
import shlex
import sys

# 1.3.1: khop khi ten vung la CA MOT thanh phan duong dan — tep ten "...-vao-KTC-Database.md" hay thu muc
# "Ban-trung-KTC-Database" khong phai vung bao ve (bao nham that 18-26/9/2026, 3 lenh).
VUNG_SO = r"(?<![\w.-])(?:ktc-database|03-templates(?:\(\d+\))?|04-good-documents)(?![\w.-])"
VUNG = re.compile(VUNG_SO, re.I)
CONG_CU_TEP = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
CONG_CU_LENH = {"Bash", "PowerShell"}

# dong tu ghi/xoa: moi doi so dang duong dan deu la DICH
DONG_TU_XOA_GHI = {
    "rm", "rmdir", "del", "erase", "rd", "unlink", "shred", "truncate", "touch", "mkdir",
    "remove-item", "ri", "rename-item", "ren", "set-content", "sc", "add-content", "ac",
    "out-file", "new-item", "ni", "clear-content", "clc", "tee", "tee-object", "set-itemproperty",
}
# dong tu sao chep/di chuyen: chi doi so CUOI (dich) bi xet; mv/move con xet ca nguon (xoa nguon)
DONG_TU_CHEP = {"cp", "copy", "copy-item", "cpi", "xcopy", "robocopy", "install", "rsync"}
DONG_TU_DOI = {"mv", "move", "move-item", "mi"}


def _chan(ly_do: str):
    sys.stderr.write(
        "KTC-Quan-tri guard: CHẶN — " + ly_do + "\n"
        "Kho KTC-Database, 03-Templates(1), 04-Good-Documents chỉ được ĐỌC. Ghi sản phẩm vào "
        "30-Ket-Qua/<ngày>/<loại>/; cần sửa kho thì viết đề xuất để người có thẩm quyền tự áp.\n")
    raise SystemExit(2)


def _tach_cau_lenh(lenh: str):
    """Tach chuoi lenh thanh cac cau lenh don (theo ; && || | xuong dong)."""
    return [c.strip() for c in re.split(r"(?:&&|\|\||;|\n|\|)", lenh) if c.strip()]


def _tokens(cau: str):
    # Co "\" (duong dan Windows) thi tach kieu non-posix: posix coi "\" la ky tu thoat, "Drive\KTC-Database"
    # thanh "DriveKTC-Database" va lot khoi VUNG (1.3.1); non-posix giu ngoac kep trong token -> bo ngoac.
    try:
        if "\\" in cau:
            return [t[1:-1] if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'" else t
                    for t in shlex.split(cau, posix=False)]
        return shlex.split(cau, posix=True)
    except ValueError:
        return cau.split()


def _kiem_chuyen_huong(cau: str):
    # > dich · >> dich · 2> dich (bo qua >&1, > /dev/null, > $null)
    for m in re.finditer(r"\d?>>?\s*(\"[^\"]+\"|'[^']+'|[^\s;|&]+)", cau):
        dich = m.group(1).strip("\"'")
        if dich.startswith("&") or dich.lower() in ("/dev/null", "$null", "nul"):
            continue
        if VUNG.search(dich):
            _chan(f"chuyển hướng ghi vào vùng bảo vệ: {dich}")


def _gia_tri_tham_so(tok, ten):
    """PowerShell: lay gia tri cua -Destination/-Path/-LiteralPath/-FilePath."""
    ra = []
    for i, t in enumerate(tok):
        if t.lower() in ten and i + 1 < len(tok):
            ra.append(tok[i + 1])
        else:
            for n in ten:
                if t.lower().startswith(n + ":"):
                    ra.append(t.split(":", 1)[1])
    return ra



# Ma Python nhung: open('<vung>...', 'w'|'a'|'x'|'+') va Path('<vung>...').<ghi/xoa>
OPEN_GHI = re.compile(r"open\s*\(\s*[rbuf]*(['\"])[^'\"]*" + VUNG_SO + r"[^'\"]*\1\s*,\s*(?:mode\s*=\s*)?[rbf]*['\"][^'\"]*[wax+]", re.I)
PATH_GHI = re.compile(r"Path\s*\(\s*[rbuf]*(['\"])[^'\"]*" + VUNG_SO + r"[^'\"]*\1\s*\)\s*(?:/\s*['\"][^'\"]*['\"]\s*)*\."
                      r"(?:write_text|write_bytes|unlink|rename|replace|touch|mkdir|rmdir|open\s*\([^)]*['\"][wax+])", re.I)
# Trinh thong dich / vo lenh co the chay ma nhung
THONG_DICH = re.compile(r"(?:^|[\s;&|(`$])(?:python[\d.]*|py|node|deno|bun|perl|ruby|php|powershell|pwsh|cmd|bash|sh|zsh|"
                        r"wscript|cscript|mshta)(?:\.exe)?(?=[\s\"']|$)", re.I)
# Dau hieu ghi/xoa trong toan lenh (dung cho tang 2 — dich khong xac dinh)
GHI = re.compile(r"""(?ix)
   open\s*\([^)]*,\s*(?:mode\s*=\s*)?[rbf]*['"][^'"]*[wax+]
 | \.(?:write|write_text|write_bytes|writelines|save|to_excel|to_csv|unlink|rename|replace|touch|mkdir|rmdir)\s*\(
 | \.(?:writefile|appendfile|rm|rmsync|copyfile|createwritestream|unlinksync|renamesync|mkdirsync)\w*\s*\(
 | \bshutil\.(?:copy\w*|move|rmtree) | \bos\.(?:remove|unlink|rename|replace|rmdir|removedirs|makedirs|mkdir|truncate)
 | \b(?:set|add|clear)-content\b | \bout-file\b | \b(?:remove|move|copy|rename|new)-item\b
 | \[(?:system\.)?io\.(?:file|directory)\]:: | \bfs\.(?:write|append|rm|unlink|rename|copy|mkdir|cp)\w*
 | (?:^|[\s;&|(])(?:rm|rmdir|mv|cp|del|erase|rd|ren|move|copy|xcopy|robocopy|touch|tee|truncate|mkdir|unlink)(?=\s)
""")
# Bien gan duong dan vung bao ve: D="..KTC-Database..", $d = '..', set D=..
BIEN_VUNG = re.compile(r"(?:\$?[\w:]+\s*=\s*|\bset\s+\w+=)(?:\"[^\"]*|'[^']*|[^\"'\s;]*)" + VUNG_SO, re.I)
DONG_TU_CD = {"cd", "pushd", "chdir", "set-location", "sl", "push-location"}
VO_LENH = {"powershell", "powershell.exe", "pwsh", "pwsh.exe", "cmd", "cmd.exe", "bash", "sh", "zsh"}
CO_LENH_LONG = {"-c", "-command", "/c", "/k", "-comm", "-com"}
CO_MA_HOA = {"-encodedcommand", "-enc", "-ec", "-e", "-en", "-enco", "-encod"}


def _tuong_doi(t: str) -> bool:
    t = t.strip("\"'")
    return bool(t) and not re.match(r"^(?:[a-z]:[\/]|[\/]|~|\$|%)", t, re.I)


def _hoi(ly_do: str):
    """Tang 2: khong chan cung — yeu cau nguoi dung xac nhan (Claude Code/Cowork PreToolUse 'ask')."""
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": "KTC-Quan-tri guard: " + ly_do + " — không xác định được đích ghi; kho "
        "KTC-Database, 03-Templates(1), 04-Good-Documents chỉ được ĐỌC. Chỉ đồng ý nếu chắc chắn lệnh KHÔNG ghi vào kho."}},
        ensure_ascii=False))
    raise SystemExit(0)


def kiem_toan_lenh(lenh: str):
    """Kiem cap toan chuoi lenh (truoc khi tach cau): ma nhung, ma hoa, tang 2."""
    if OPEN_GHI.search(lenh) or PATH_GHI.search(lenh):
        _chan("mã nhúng mở/ghi/xóa tệp trong vùng bảo vệ")
    kiem_lenh(lenh)
    if VUNG.search(lenh) and GHI.search(lenh) and (THONG_DICH.search(lenh) or BIEN_VUNG.search(lenh)):
        _hoi("lệnh có nhắc vùng bảo vệ, có dấu hiệu ghi/xóa và có mã nhúng hoặc biến trỏ vào vùng bảo vệ")


def kiem_lenh(lenh: str, sau: int = 0):
    if sau > 3:
        _chan("lệnh lồng quá sâu, không phân tích được")
    trong_vung = False     # da cd/Set-Location vao vung bao ve
    for cau in _tach_cau_lenh(lenh):
        _kiem_chuyen_huong(cau)
        tok = _tokens(cau)
        if not tok:
            continue
        # bo tien to kieu `sudo`, `command`, `&`
        while tok and tok[0].lower() in ("sudo", "command", "&", "call"):
            tok = tok[1:]
        if not tok:
            continue
        dt = tok[0].lower().rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
        doi_so = [t for t in tok[1:] if not t.startswith("-")]
        if dt in DONG_TU_CD:
            dich = " ".join(doi_so)
            trong_vung = bool(VUNG.search(dich)) or (trong_vung and _tuong_doi(dich))
            continue
        if dt in VO_LENH:
            thap = [t.lower() for t in tok[1:]]
            if any(t in CO_MA_HOA for t in thap) and dt.startswith(("powershell", "pwsh")):
                _chan("lệnh PowerShell mã hóa (-EncodedCommand) không kiểm được")
            # cat NGUYEN VAN phan lenh con tu chuoi goc — ghep lai tu token shlex se mat dau "\" cua duong dan Windows
            m = re.search(r"(?i)(?:^|\s)(?:-c|-command|-comm?|/c|/k)\s+(.+)$", cau, re.S)
            if m:
                con = m.group(1).strip()
                if len(con) >= 2 and con[0] == con[-1] and con[0] in "\"'":
                    con = con[1:-1]
                kiem_lenh(con, sau + 1)
        if trong_vung:
            # dang dung trong vung bao ve: ghi vao duong dan tuong doi = ghi vao kho
            for m in re.finditer(r"\d?>>?\s*(\"[^\"]+\"|'[^']+'|[^\s;|&]+)", cau):
                d = m.group(1).strip("\"'")
                if not d.startswith("&") and d.lower() not in ("/dev/null", "$null", "nul") and _tuong_doi(d):
                    _chan(f"chuyển hướng ghi `{d}` khi đang đứng trong vùng bảo vệ")
            if dt in DONG_TU_XOA_GHI | DONG_TU_DOI | DONG_TU_CHEP and any(_tuong_doi(t) for t in doi_so):
                _chan(f"lệnh `{dt}` với đường dẫn tương đối khi đang đứng trong vùng bảo vệ")
        if dt in ("sed", "perl") and any(t.startswith("-i") for t in tok[1:]):
            if any(VUNG.search(t) for t in doi_so):
                _chan(f"sửa tại chỗ ({dt} -i) tệp trong vùng bảo vệ")
            continue
        if dt in DONG_TU_XOA_GHI:
            if any(VUNG.search(t) for t in tok[1:]):
                _chan(f"lệnh `{dt}` tác động vào vùng bảo vệ")
        elif dt in DONG_TU_DOI:
            if any(VUNG.search(t) for t in tok[1:]):
                _chan(f"lệnh `{dt}` di chuyển/đổi tên trong vùng bảo vệ")
        elif dt in DONG_TU_CHEP:
            dich = _gia_tri_tham_so(tok, ("-destination", "-dest"))
            if not dich and doi_so:
                dich = [doi_so[-1]]
            if dt == "robocopy" and len(doi_so) >= 2:
                dich = [doi_so[1]]
            if any(VUNG.search(d) for d in dich):
                _chan(f"lệnh `{dt}` chép vào vùng bảo vệ: {dich[0]}")


def kiem(data: dict):
    ten = data.get("tool_name") or ""
    vao = data.get("tool_input") or {}
    if ten in CONG_CU_TEP:
        p = vao.get("file_path") or vao.get("notebook_path") or ""
        if VUNG.search(str(p)):
            _chan(f"{ten} vào {p}")
    elif ten in CONG_CU_LENH:
        kiem_toan_lenh(str(vao.get("command") or ""))


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("dữ liệu hook không phải đối tượng JSON")
    except Exception as e:  # fail-closed
        _chan(f"không đọc được dữ liệu hook ({e})")
    try:
        kiem(data)
    except SystemExit:
        raise
    except Exception as e:  # fail-closed
        _chan(f"lỗi nội bộ của guard ({e})")
    raise SystemExit(0)


if __name__ == "__main__":
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
