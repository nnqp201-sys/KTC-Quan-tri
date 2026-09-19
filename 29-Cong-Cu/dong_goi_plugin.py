# -*- coding: utf-8 -*-
"""Dong goi KTC-Quan-tri thanh MOT plugin Claude Code/Cowork (5 skill con chung 1 plugin).

Nguon: tai dung nguyen ven noi dung 5 goi .skill DA XAC MINH — khong doc lai tu
20-Chuan-Chung/references roi/ de tranh nguy co lech ban giua hai duong dong goi
song song. Chi doi ten thu muc + frontmatter `name:` — bo tien to "ktc-" (goi da
la namespace).

Lich su: ban dau (18/9/2026) ktc-soan-thao-vb-v1.1 thieu 3 tham chieu that
(14-Nguyen-Tac-Soan-Thao-Bat-Bien.md, 15-Skill-Track-Changes.md,
29-Cong-Cu/ktc_trackchanges.py) nen script nay tung phai tu va rieng. Da sua tan goc
trong ktc-soan-thao-vb-v1.2 (them 3 tep vao chinh references/Skill-Library/ cua
he do) — script nay khong can va nua, chi giai nen thuan tuy nhu 4 he con lai.

Chay: python 29-Cong-Cu/dong_goi_plugin.py
"""
import io
import json
import os
import re
import shutil
import sys
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_DIR = os.path.join(DU_AN, "31-Plugin")

# (goi .skill nguon, ten thu muc trong goi .skill, ten skill moi trong plugin)
GOI_NGUON = [
    (os.path.join(DU_AN, "22-KTC-Dieu-Phoi", "ktc-quan-tri.skill"), "ktc-quan-tri", "quan-tri"),
    (os.path.join(DU_AN, "25-KTC-Bao-Cao", "ktc-bao-cao-v3.13.skill"), "ktc-bao-cao", "bao-cao"),
    (os.path.join(DU_AN, "23-KTC-Ke-Hoach", "ktc-ke-hoach-v3.8.skill"), "ktc-ke-hoach", "ke-hoach"),
    (os.path.join(DU_AN, "26-KTC-Soan-Thao-VB", "ktc-soan-thao-vb-v1.8.skill"), "ktc-soan-thao-vb", "soan-thao-vb"),
    (os.path.join(DU_AN, "24-KTC-Theo-doi-CV", "ktc-theo-doi-cv-v1.6.skill"), "ktc-theo-doi-cv", "theo-doi-cv"),
]

PLUGIN_VERSION = "0.5.4"  # 0.2.0: them agent tu cai tien, tu ghi nhat ky, tu backup GitHub


# Chi don cac thu muc SINH TU DONG. README.md/CHANGELOG.md o goc 31-Plugin/ la viet
# tay, KHONG duoc dong o day — bai hoc 18/9/2026: lan dau don ca thu muc goc da
# xoa mat ca hai tep nay.
THU_MUC_SINH_TU_DONG = ["skills", ".claude-plugin", "hooks", "scripts", "agents"]
# Nguon viet tay cua script/agent them vao plugin (khong sua trong 31-Plugin/)
PLUGIN_SRC = os.path.join(DU_AN, "29-Cong-Cu", "plugin_src")


def don_sach(p: str):
    os.makedirs(p, exist_ok=True)
    for ten in THU_MUC_SINH_TU_DONG:
        con = os.path.join(p, ten)
        if os.path.exists(con):
            shutil.rmtree(con)


def giai_nen_skill(goi: str, ten_goc: str, dich: str):
    """Giai nen 1 goi .skill, dua noi dung ben trong thu muc goc vao `dich`."""
    with zipfile.ZipFile(goi) as z:
        for member in z.namelist():
            if not member.startswith(ten_goc + "/"):
                continue
            rel = member[len(ten_goc) + 1:]
            if not rel:
                continue
            out = os.path.join(dich, rel)
            if member.endswith("/"):
                os.makedirs(out, exist_ok=True)
                continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with z.open(member) as src, open(out, "wb") as dst:
                dst.write(src.read())


def doi_ten_frontmatter(skill_md: str, ten_cu: str, ten_moi: str):
    s = io.open(skill_md, encoding="utf-8").read()
    s2 = re.sub(rf"^name:\s*{re.escape(ten_cu)}\s*$", f"name: {ten_moi}",
                s, count=1, flags=re.M)
    if s2 == s:
        raise SystemExit(f"KHONG doi duoc name: trong {skill_md} (tim '{ten_cu}')")
    io.open(skill_md, "w", encoding="utf-8").write(s2)


def build_skills():
    print("── Giai nen 5 goi .skill da xac minh vao 31-Plugin/skills/ ──")
    for goi, ten_goc, ten_moi in GOI_NGUON:
        if not os.path.exists(goi):
            raise SystemExit(f"KHONG tim thay goi nguon: {goi}")
        dich = os.path.join(PLUGIN_DIR, "skills", ten_moi)
        os.makedirs(dich, exist_ok=True)
        giai_nen_skill(goi, ten_goc, dich)
        doi_ten_frontmatter(os.path.join(dich, "SKILL.md"), ten_goc, ten_moi)
        n = sum(len(fs) for _, _, fs in os.walk(dich))
        print(f"  ✓ {ten_moi:14s} <- {os.path.relpath(goi, DU_AN)}  ({n} tep)")


def ghi_json(path: str, obj: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def build_manifest():
    print("── Ghi .claude-plugin/plugin.json ──")
    manifest = {
        "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
        "name": "ktc-quan-tri",
        "displayName": "KTC Quản trị",
        "version": PLUGIN_VERSION,
        "description": (
            "Chu trình quản trị nhiệm vụ khép kín của Trường Cao đẳng Kon Tum: "
            "Kế hoạch → Theo dõi → Báo cáo → Soạn thảo văn bản, dùng chung một plugin "
            "cho Claude Cowork và Claude Code. Gồm 5 skill: quan-tri (điều phối), "
            "bao-cao, ke-hoach, soan-thao-vb, theo-doi-cv; agent ktc-tu-cai-tien; hook tự ghi nhật ký "
            "và nạp lại vào context; tự backup GitHub hằng ngày."
        ),
        "author": {
            "name": "Trường Cao đẳng Kon Tum - Phòng Tổng hợp - Hành chính và Quản trị"
        },
        "keywords": ["ktc", "vietnam", "quan-tri", "ke-hoach", "bao-cao", "soan-thao-van-ban"],
        "defaultEnabled": False,
        "metadata": {
            "builtFrom": "5 gói .skill đã xác minh 18/9/2026 (DL-20260918-001; soan-thao-vb nâng lên v1.2 "
                         "cùng ngày để vá 3 tham chiếu gãy)",
            "claudeStrictValidation": "CHƯA CHẠY — môi trường build không có `claude` CLI trên PATH; "
                                       "bắt buộc chạy `claude plugin validate ./31-Plugin --strict` trước khi bật.",
            "parallelWith": ["ktc-quan-tri.skill", "ktc-bao-cao-v3.13.skill", "ktc-ke-hoach-v3.8.skill",
                              "ktc-soan-thao-vb-v1.8.skill", "ktc-theo-doi-cv-v1.6.skill"],
        },
    }
    ghi_json(os.path.join(PLUGIN_DIR, ".claude-plugin", "plugin.json"), manifest)
    print("  ✓ plugin.json")


def lenh(script: str, *args: str) -> dict:
    tham_so = "".join(f" {a}" for a in args)
    return {"type": "command",
            "command": f'python "${{CLAUDE_PLUGIN_ROOT}}/scripts/{script}"{tham_so}'}


def build_hooks():
    print("── Ghi hooks/hooks.json (doctor + nhật ký + backup bù; không lặp guard 897) ──")
    hooks = {
        "hooks": {
            "SessionStart": [{"hooks": [
                lenh("ktc_quan_tri_doctor.py"),
                lenh("ktc_nhat_ky.py", "nap"),
                {**lenh("ktc_backup_github.py", "--neu-can"), "timeout": 120},
            ]}],
            # Khong ghi Read/Grep/Glob de log khong bi ngap; chi thao tac co tac dung.
            "PostToolUse": [{"matcher": "Write|Edit|Bash|PowerShell|Skill|Agent",
                             "hooks": [lenh("ktc_nhat_ky.py", "ghi")]}],
            "SessionEnd": [{"hooks": [lenh("ktc_nhat_ky.py", "ket-phien")]}],
        }
    }
    ghi_json(os.path.join(PLUGIN_DIR, "hooks", "hooks.json"), hooks)
    print("  ✓ hooks.json")


def chep_nguon_viet_tay():
    print("── Chép script/agent viết tay từ 29-Cong-Cu/plugin_src/ ──")
    for thu_muc in ("scripts", "agents"):
        src = os.path.join(PLUGIN_SRC, thu_muc)
        if not os.path.isdir(src):
            continue
        dst = os.path.join(PLUGIN_DIR, thu_muc)
        os.makedirs(dst, exist_ok=True)
        for f in sorted(os.listdir(src)):
            if f.endswith((".py", ".md")):
                shutil.copyfile(os.path.join(src, f), os.path.join(dst, f))
                print(f"  ✓ {thu_muc}/{f}")


DOCTOR_SCRIPT = r'''# -*- coding: utf-8 -*-
"""SessionStart doctor cho plugin ktc-quan-tri — in banner phien ban 5 skill dang bat.

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
    print("KTC-Quan-tri Plugin — SessionStart doctor")
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
    print("Lưu ý: guard chặn ghi KTC-Database dùng chung với plugin ktc-ra-soat-897")
    print("nếu đã cài; nếu chưa cài plugin đó, KTC-Database vẫn chỉ nên đọc theo quy")
    print("ước dự án (xem CLAUDE.md), plugin này không tự chặn ghi.")
    print("=" * 60)


if __name__ == "__main__":
    main()
'''


def build_doctor_script():
    print("── Ghi scripts/ktc_quan_tri_doctor.py ──")
    path = os.path.join(PLUGIN_DIR, "scripts", "ktc_quan_tri_doctor.py")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(DOCTOR_SCRIPT)
    print("  ✓ ktc_quan_tri_doctor.py")


if __name__ == "__main__":
    don_sach(PLUGIN_DIR)
    build_skills()
    build_manifest()
    build_hooks()
    build_doctor_script()
    chep_nguon_viet_tay()
    print()
    print(f"Đã dựng 31-Plugin tại: {PLUGIN_DIR}")
