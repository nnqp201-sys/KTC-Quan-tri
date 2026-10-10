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
    print("=" * 60)


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
