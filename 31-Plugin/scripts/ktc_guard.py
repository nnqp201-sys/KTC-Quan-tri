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
  - KHONG phan tich ma Python/JS nhung trong lenh — gioi han da ghi ro trong README/Thong bao.

Doc tu vung bao ve (cat, ls, python doc tep, cp TU kho RA ngoai) duoc phep.

Fail-closed: loi doc du lieu hook hoac loi noi bo -> CHAN (exit 2). Harness chi chan khi hook tra 2;
neu may khong co Python thi hook khong chay duoc — doctor dau phien bao "guard CHUA hoat dong".
Ma thoat: 0 = cho phep · 2 = chan (thong bao ra stderr cho Claude).
"""
import json
import re
import shlex
import sys

VUNG = re.compile(r"(ktc-database|03-templates|04-good-documents)", re.I)
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
    try:
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


def kiem_lenh(lenh: str):
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
        kiem_lenh(str(vao.get("command") or ""))


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
