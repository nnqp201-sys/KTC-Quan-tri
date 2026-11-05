# -*- coding: utf-8 -*-
"""SessionStart doctor cho plugin ktc-quan-tri — in phien ban plugin va phien ban tu khai cua moi skill dang bat.

Doc truc tiep tu SKILL.md tu khai (khong suy dien tu ten thu muc/ten file), dung
bai hoc da ghi 18/9/2026: "Khong suy dien phien ban tu ten tep."
"""
import io
import os
import re

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(GOC, "skills")

# Uu tien 1: dong ghi tuong minh "Phien ban: X.Y" (ke-hoach, soan-thao-vb, theo-doi-cv).
# Uu tien 2: dong tieu de ket thuc bang "vX.Y" (bao-cao dang "# ... KTC-RIS v3.7").
MAU_TUONG_MINH = re.compile(r"Phi[eê]n b[aả]n:?\s*v?([0-9]+\.[0-9]+(?:\.[0-9]+)?)", re.IGNORECASE)
MAU_TIEU_DE_CUOI_DONG = re.compile(r"^#.*\bv([0-9]+\.[0-9]+(?:\.[0-9]+)?)\s*$", re.MULTILINE)


def doc_phien_ban(skill_md: str) -> str:
    try:
        s = io.open(skill_md, encoding="utf-8").read()
    except OSError:
        return "?"
    m = MAU_TUONG_MINH.search(s)
    if m:
        return m.group(1)
    m = MAU_TIEU_DE_CUOI_DONG.search(s)
    if m:
        return m.group(1)
    return "(không tự khai)"


def main():
    print("=" * 60)
    pb_plugin = "?"
    try:
        import json
        pb_plugin = json.load(io.open(os.path.join(GOC, ".claude-plugin", "plugin.json"), encoding="utf-8"))["version"]
    except Exception:
        pass
    print(f"KTC-Quan-tri Plugin {pb_plugin} — SessionStart doctor")
    print("=" * 60)
    if not os.path.isdir(SKILLS_DIR):
        print("  ✗ Không thấy thư mục skills/ — plugin có thể chưa build đúng.")
        return
    for ten in sorted(os.listdir(SKILLS_DIR)):
        skill_md = os.path.join(SKILLS_DIR, ten, "SKILL.md")
        if not os.path.exists(skill_md):
            print(f"  ✗ {ten:14s} thiếu SKILL.md")
            continue
        pb = doc_phien_ban(skill_md)
        print(f"  ✓ {ten:14s} phiên bản tự khai: {pb}")
    print("-" * 60)
    kiem_guard()
    kiem_phu_thuoc()
    kiem_thu_muc()
    kiem_897()
    print("=" * 60)


# Ban chinh thuc toan Truong tai 5/11/2026 (TB P-QLKHCN&HTPT, cai 4/11/2026).
# Doi khi co ban moi: sua MOT cho nay.
PB_897_CHINH_THUC = "4.6.4"


# 897 duoc phat hanh theo HAI cach, khai phien ban o HAI cho khac nhau:
#   a) goi plugin (ban cu, vd 1.0.3): rules/*.md ghi "KTC-Ra-Soat-897-v3-Core", "...-v2.24-BASELINE"
#   b) goi .skill (ban chinh thuc v4.6.4): SKILL.md tieu de ghi "... (v4.6.4, 03/11/2026 ...)"
# Phep kiem phai doc duoc CA HAI — bat duoc 5/11/2026: ban dau chi doc (a) nen se bao gia
# "CHUA CAI" ngay sau khi nguoi dung cai dung ban v4.6.4.
MAU_PB_897 = (
    re.compile(r"KTC-Ra-Soat-897[ _-]?v([0-9]+(?:\.[0-9]+){1,2})"),
    re.compile(r"R[àa] so[áa]t 897[^\n]{0,80}?\(v([0-9]+(?:\.[0-9]+){1,2})"),
    re.compile(r"Phi[êe]n b[ảa]n:?\*{0,2}\s*v?([0-9]+(?:\.[0-9]+){1,2})"),
)


def _pb_897(thu_muc):
    """Doc phien ban bo quy tac 897 tu NOI DUNG tep — KHONG suy dien tu ten thu muc
    (bai hoc 18/9/2026). Tra ve chuoi vd '4.6.4', hoac None neu khong doc duoc."""
    import glob
    ung_vien = []
    for mau in ("SKILL.md", "00-README.md", "rules/*.md", "core/*.md",
                "skills/*/SKILL.md", "*/SKILL.md"):
        ung_vien += glob.glob(os.path.join(thu_muc, mau))
    cao_nhat = None
    for p in sorted(set(ung_vien)):
        try:
            s = io.open(p, encoding="utf-8", errors="ignore").read(20000)
        except OSError:
            continue
        for mau in MAU_PB_897:
            for m in mau.finditer(s):
                bo = tuple(int(x) for x in m.group(1).split("."))
                if cao_nhat is None or bo > cao_nhat:
                    cao_nhat = bo
    return ".".join(str(x) for x in cao_nhat) if cao_nhat else None


def kiem_897():
    """1.4.0: bao ro plugin ktc-ra-soat-897 da cai chua va PHIEN BAN NAO.

    Ly do: 5/11/2026 phat hien tai khoan ca nhan dang cai ban 1.0.3 (23/9/2026) nap bo quy tac
    v2.24, trong khi ban chinh thuc toan Truong la v4.6.4 — soan thao va tu kiem im lang dung
    chuan cu. Khong co phep kiem nao bao.
    """
    import glob
    # Hai plugin co the nam o HAI nhanh khac nhau duoi .claude/plugins/:
    #   cache/<marketplace>/<ten>/<phien ban>/     (ktc-quan-tri)
    #   marketplaces/<marketplace>/<ten>/          (ktc-ra-soat-897)
    # Nen phai leo den dung thu muc "plugins" roi moi tim, khong leo co dinh 3 cap
    # (bao gia "CHUA CAI" khi thuc te da cai — bat duoc 5/11/2026 khi chay tren ban that).
    goc_tim = None
    d = GOC
    for _ in range(8):
        cha = os.path.dirname(d)
        if cha == d:
            break
        if os.path.basename(d) == "plugins":
            goc_tim = d
            break
        d = cha
    # 897 co the den tu BA nguon khac nhau tren cung mot may (phat hien 5/11/2026):
    #   1. skill DONG BO tu tai khoan claude.ai -> ~/.claude/skills/synced/<bucket>/ktc-ra-soat-897
    #   2. plugin cai tay            -> ~/.claude/plugins/marketplaces/<mp>/ktc-ra-soat-897
    #   3. marketplace cuc bo        -> ~/.claude/ktc-marketplace/ktc-ra-soat-897
    # Ban dau chi tim (2)(3) nen gap plugin v3.0 cu truoc va BAO SAI "CU", trong khi tai khoan
    # da co v4.6.4 qua (1). Phai gom HET roi lay ban CAO NHAT.
    goc_nd = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(
        os.path.expanduser("~"), ".claude")
    tim = []
    for muc in filter(None, (goc_tim, os.path.dirname(GOC),
                             os.path.join(goc_nd, "skills"),
                             os.path.join(goc_nd, "ktc-marketplace"))):
        for x in glob.glob(os.path.join(muc, "**", "*ra-soat-897*"), recursive=True):
            if not os.path.isdir(x):
                continue
            # Chi nhan thu muc THAT su chua bo quy tac, khong nhan thu muc trung ten.
            # Ca hai cach phat hanh: goi plugin (rules/, core/) va goi .skill (SKILL.md).
            if (os.path.isdir(os.path.join(x, "rules")) or os.path.isdir(os.path.join(x, "core"))
                    or os.path.isfile(os.path.join(x, "SKILL.md"))):
                tim.append(x)
    # Lay ban CAO NHAT trong moi nguon tim duoc (khong phai ban tim thay dau tien):
    # may nay dang co ba ban song song, bao theo ban nao gap truoc la vo nghia.
    xep = []
    for d in sorted(set(tim)):
        pb = _pb_897(d)
        if pb:
            xep.append((tuple(int(x) for x in pb.split(".")), pb, d))
    if xep:
        xep.sort()
        cao = xep[-1]
        if len(xep) > 1:
            print(f"  · 897: thấy {len(xep)} bản trên máy — lấy bản cao nhất v{cao[1]}")
            for _, pb, d in xep[:-1]:
                print(f"    (còn v{pb} tại {os.path.basename(os.path.dirname(d))}/{os.path.basename(d)})")
        if cao[1] == PB_897_CHINH_THUC:
            print(f"  ✓ ktc-ra-soat-897 v{cao[1]} (bản chính thức toàn Trường)")
        else:
            print(f"  ✗ ktc-ra-soat-897 v{cao[1]} — CŨ. Bản chính thức toàn Trường: v{PB_897_CHINH_THUC}")
            print("    Soạn thảo và tự kiểm đang theo chuẩn cũ. Cài lại gói v"
                  + PB_897_CHINH_THUC + " trước khi soạn văn bản trình ký.")
        return

    tim = sorted(set(tim), key=len)
    if not tim:
        print("  ✗ ktc-ra-soat-897: CHƯA CÀI — Nguyên tắc 9 (dùng bộ quy tắc 897 từ lúc bắt đầu viết)")
        print("    không tự kiểm được thể thức, không rà soát trước trình ký. Cài gói v"
              + PB_897_CHINH_THUC + " rồi mở lại phiên.")
        return
    for d in tim[:1]:
        pb = _pb_897(d)
        if pb is None:
            print(f"  · ktc-ra-soat-897: đã cài, không đọc được phiên bản ({os.path.basename(d)})")
        elif pb == PB_897_CHINH_THUC:
            print(f"  ✓ ktc-ra-soat-897 v{pb} (bản chính thức toàn Trường)")
        else:
            print(f"  ✗ ktc-ra-soat-897 v{pb} — CŨ. Bản chính thức toàn Trường: v{PB_897_CHINH_THUC}")
            print("    Soạn thảo và tự kiểm đang theo chuẩn cũ. Cài lại gói v"
                  + PB_897_CHINH_THUC + " trước khi soạn văn bản trình ký.")


def kiem_thu_muc():
    """1.3.5: che do thu muc — du an / thu muc lam viec cua don vi / chua ket noi (giao tep trong phien)."""
    import sys
    try:
        sys.path.insert(0, os.path.join(GOC, "scripts"))
        from ktc_thu_muc import tim_goc
        che_do, goc, ma = tim_goc()
    except Exception as e:
        print(f"  · thư mục làm việc: không kiểm được ({e.__class__.__name__})")
        return
    if che_do == "du-an":
        print(f"  ✓ thư mục: dự án KTC-Quan-tri ({goc})")
    elif che_do == "don-vi":
        print(f"  ✓ thư mục làm việc đơn vị {ma}: {goc} — đầu vào 10-Dau-Vao/, kết quả 30-Ket-Qua/")
    else:
        print("  · chưa kết nối thư mục làm việc — kết quả giao trong phiên. Muốn đọc 10-Dau-Vao/, lưu 30-Ket-Qua/ tự động:"
              " chọn một thư mục trong Cowork rồi yêu cầu “kết nối thư mục KTC cho đơn vị <mã>”.")


def kiem_guard():
    """Tu thu guard: mot lenh ghi gia vao KTC-Database PHAI bi chan (ma 2), ghi vao 30-Ket-Qua PHAI qua (ma 0)."""
    import json
    import subprocess
    import sys
    g = os.path.join(GOC, "scripts", "ktc_guard.py")
    if not os.path.isfile(g):
        print("  ✗ guard: THIẾU scripts/ktc_guard.py — KHÔNG có bảo vệ ghi kho chuẩn")
        return
    def chay(p):
        vao = json.dumps({"tool_name": "Write", "tool_input": {"file_path": p}})
        try:
            return subprocess.run([sys.executable, g], input=vao, text=True, capture_output=True,
                                  timeout=20).returncode
        except Exception:
            return -1
    chan = chay("X:/My Drive/KTC-Database/thu.txt")
    qua = chay("X:/du-an/30-Ket-Qua/thu.txt")
    if chan == 2 and qua == 0:
        print("  ✓ guard: HOẠT ĐỘNG (chặn ghi KTC-Database, 03-Templates, 04-Good-Documents)")
    else:
        print(f"  ✗ guard: CHƯA HOẠT ĐỘNG (tự thử: chặn={chan}, cho qua={qua}) — không coi là có bảo vệ ghi")


def kiem_phu_thuoc():
    """Bao phu thuoc NGOAI goi (tham dinh lan 1 M-01): co/khong, khong tu ket luan dat."""
    import sys
    print(f"  · Python {sys.version.split()[0]} ({sys.executable})")
    try:
        sys.path.insert(0, os.path.join(GOC, "scripts"))
        from duong_dan import ktc_database
        print(f"  ✓ KTC-Database: {ktc_database(canh_bao_ban_cu=False)}")
    except FileNotFoundError:
        print("  ✗ KTC-Database: không tìm thấy — skill trả CAN_BO_SUNG khi cần kho. Kho được chia sẻ qua Google Drive:"
              " thêm lối tắt “KTC-Database” vào Drive của tôi, hoặc đặt biến KTC_DATABASE_DIR trỏ tới thư mục kho")
    except Exception as e:
        print(f"  ✗ KTC-Database: không kiểm được ({e.__class__.__name__})")
    for mod in ("docx", "openpyxl"):
        try:
            __import__(mod)
            print(f"  ✓ thư viện {mod}")
        except Exception:
            print(f"  ✗ thư viện {mod} — phép đo thể thức/Excel sẽ ghi vào 'Kiểm tra chưa chạy'")


if __name__ == "__main__":
    main()
