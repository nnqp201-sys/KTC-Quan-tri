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
import datetime as dt
import hashlib
import zipfile

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_DIR = os.path.join(DU_AN, "31-Plugin")

# (goi .skill nguon, ten thu muc trong goi .skill, ten skill moi trong plugin)
GOI_NGUON = [
    (os.path.join(DU_AN, "22-KTC-Dieu-Phoi", "ktc-quan-tri-v1.17.skill"), "ktc-quan-tri", "quan-tri"),
    (os.path.join(DU_AN, "25-KTC-Bao-Cao", "ktc-bao-cao-v3.21.skill"), "ktc-bao-cao", "bao-cao"),
    (os.path.join(DU_AN, "23-KTC-Ke-Hoach", "ktc-ke-hoach-v3.13.skill"), "ktc-ke-hoach", "ke-hoach"),
    (os.path.join(DU_AN, "26-KTC-Soan-Thao-VB", "ktc-soan-thao-vb-v1.17.skill"), "ktc-soan-thao-vb", "soan-thao-vb"),
    (os.path.join(DU_AN, "24-KTC-Theo-doi-CV", "ktc-theo-doi-cv-v1.11.skill"), "ktc-theo-doi-cv", "theo-doi-cv"),
    (os.path.join(DU_AN, "27-KTC-The-Thuc", "ktc-the-thuc-v1.4.skill"), "ktc-the-thuc", "the-thuc"),
    (os.path.join(DU_AN, "28-KTC-KPI", "ktc-kpi-lap-ke-hoach-v1.5.skill"), "ktc-kpi-lap-ke-hoach", "kpi-lap-ke-hoach"),
    (os.path.join(DU_AN, "28-KTC-KPI", "Tu-Danh-Gia", "ktc-kpi-tu-danh-gia-v1.4.skill"), "ktc-kpi-tu-danh-gia",
     "kpi-tu-danh-gia"),
]

PLUGIN_VERSION = "1.4.2"  # 1.4.2 (5/11/2026): mo ta plugin TU DEM so agent (ban 1.4.1 ghi tay "36 agent" trong khi goi co 38 — mo ta nay hien tren thu vien to chuc); doctor tim 897 ca o skill DONG BO tu tai khoan (~/.claude/skills/synced) va marketplace cuc bo, lay ban cao nhat — truoc chi tim trong .claude/plugins nen gap plugin v3.0 cu va BAO SAI "CU" du tai khoan da co v4.6.4. 1.4.1 (5/11/2026): nhan ban quy tac dung chung 20-Chuan-Chung ban 29/10 vao NGUON ROI va dong lai 7 goi .skill — truoc do goi roi (tai khoan Chat/Cowork nhan .skill truc tiep) mang 17-Quy-Tac-Vien-Dan, 18-Chuan-The-Thuc-San-Pham, 00-Nguyen-Tac-Chung, 19-Quy-Tac-KPI ban 29/9, lech mot thang; them doctor kiem phien ban ktc-ra-soat-897 (bat ban cu/chua cai). quan-tri 1.17, bao-cao 3.21, ke-hoach 3.13, soan-thao-vb 1.17, theo-doi-cv 1.11, the-thuc 1.4, kpi-lap-ke-hoach 1.5. 1.4.0 (5/11/2026): lop kiem thuat ngu phap ly TN01-TN04 (20-Chuan-Chung/21-Quy-Tac-Thuat-Ngu.md, kiem_thuat_ngu.py) + 29 agent dung chung tu .claude/agents/ vao goi: ktc-kiem-thuat-ngu, ktc-tu-dien-phap-ly + 13 ktc-tdpl-*, ktc-hoi-dap-chinh-sach + 12 ktc-hdcs-*, ktc-kiem-nhat-quan-bo-van-ban; doc 2 kho moi KTC-Database 08-Tu-Dien-Phap-Ly, 07-Hoi-Dap-Chinh-Sach (chi doc). 1.3.13 (29/9/2026, tiep thu tham dinh lan 5 L5-04): dung lap lai duoc tu ban checkout sach cua commit — chuan hoa xuong dong LF truoc khi nen, BAN-DO-TEP so bam bo qua CR; noi dung chuc nang giong 1.3.12. 1.3.12 (29/9/2026): TT17 nhan vai tro phan dau theo vi tri dong (mau 2.2: ten Truong la co quan chu quan, khong dam) — sua bao nham BC cua Phong khi lap ho so vong 5; dinh chinh loi mau 06A, 06D; the-thuc 1.3. 1.3.11 (29/9/2026): nguyen tac sua van ban tuong tu / rap noi dung vao mau (chi dao 28/9); khung dung lai tu mau 03A (khung ghep tu TB 1060 hien "1" o trang 1, lech duong ke trich yeu); TT11b so trang o trang 1; chuan hoa NFC (mau luu NFD, phep so chu im lang truot); TT19 khoi chu ky 2 hang; loi mau 01, 03A; the-thuc 1.2, soan-thao-vb 1.15. 1.3.10 (28/9/2026): khung the thuc VBHC (tu TB 1060 da ban hanh, --khung) khi khong doc duoc kho; phep do TT12-TT19 anh xa 897 Checklist 01, 05, 08 (bang tieu de, duong ke, co/kieu tung thanh phan, ky thay, hoc ham); the-thuc 1.1, soan-thao-vb 1.14 — sua loi TB dung bang tieu de tay tren Cowork. 1.3.9 (28/9/2026): ra soat tu du — goi tu hoc ke hoach, mau dinh tuyen theo doi CV, mau trang bao cao vao goi; BAN-DO-TEP.md; agent tu-hoc/tu-cai-tien ghi pham vi chi du an; soan-thao sua duong dan cu, tro 17/29 ve plugin 897. 1.3.8 (28/9/2026): khoi <plugin_paths> chen vao moi skill, agent — khong xin quyen them thu muc du an vao phien (Cowork xin ca KTC-Quan-tri de doc ban goc 20-Chuan-Chung). 1.3.7 (28/9/2026): sua tu chay that 1.3.6 — so hieu di dang, ky cu o tieu de phu luc, guard chan Write/Edit vao tep plugin da cai, hook the thuc bo qua 10-Dau-Vao; bao-cao 3.19. 1.3.6 (28/9/2026): bao cao thang cap Truong dung tu ban DA BAN HANH (bc_thang.py, skill bao-cao v3.18, Skill 37) — khac phuc chay thu 28/9 kem ban 21/9; dong vao plugin bc_thang, vanphong, trich_tuong_thuat, ktc_trackchanges; mau trang sua 3 loi; agent kiem ho so: tra lai don vi khong loai khoi bao cao. 1.3.5 (28/9/2026): ket noi thu muc lam viec cua don vi (ktc_thu_muc.py, Nguyen tac 3) — tai khoan thanh vien tren Cowork doc 10-Dau-Vao/, luu 30-Ket-Qua/; hook do the thuc chay ca trong thu muc don vi; doctor bao che do thu muc, huong dan loi tat kho. ke-hoach 3.11, theo-doi-cv 1.9, bao-cao 3.17, soan-thao-vb 1.12, quan-tri 1.16, kpi-lap-ke-hoach 1.4, kpi-tu-danh-gia 1.3. 1.3.4 (28/9/2026): chuan 6 Truc — can cu QD 1923 PL I, II cho cot Diem cham/He so, quan he voi Danh muc QD 2119 (DL-20260928-002); ke-hoach 3.10, theo-doi-cv 1.8, bao-cao 3.16, soan-thao-vb 1.11, quan-tri 1.15; guard bo than heredoc dua cho trinh thong dich khoi phan tich cau lenh. 1.3.3 (28/9/2026): Danh muc san pham CHINH THUC QD 2119/QD-CDKT thay du thao TB 1052 (kpi_calc phuong an A co van ban, KH08, quan-tri 1.14, kpi-lap-ke-hoach 1.3, kpi-tu-danh-gia 1.2); guard: .replace/.rename chi la ghi khi co Path(...)/os. 1.3.2 (27/9/2026, tiep thu tham dinh lan 4): guard tang 2 CHAN thay vi hoi (F4-01); chan tao lien ket tro vao kho; sua nhan dang duong dan tuyet doi C:\; duong dan quy tac day du cho agent; kiem_vien_dan doc nhieu bang ma. 1.3.1 (27/9/2026, tiep thu tham dinh lan 3): guard 2 tang chan/hoi (ma nhung, vo lenh long, cd vao kho, UNC; vung = ca thanh phan duong dan); nhat ky khong luu lenh/mo ta tho, nap dau phien <= 4.500 ky tu; khoi chuan chung loi ~2.460 ky tu + ban day du trong references/; lich su phien ban tach khoi SKILL.md; quy tac bat dong skill-agent. 1.3.0 (26/9/2026, tiep thu tham dinh lan 1-2): go backup GitHub khoi plugin; PreToolUse guard chan ghi kho chuan (ktc_guard.py, fail-closed); nhat ky mac dinh chi ghi mo ta, noi dung chi khi chon #học / KTC_NHAT_KY_NOI_DUNG=1, xoa sau 30 ngay; chen chuan chung 20-Chuan-Chung/20-Quy-Tac-Bat-Bien-Va-Khuon-Dau-Ra.md vao 8 skill + 7 agent; quan-tri 1.13. 1.2.1 (25/9/2026): sheet KPI het che chu, du cot C–F; kpi-lap-ke-hoach 1.2, kpi-tu-danh-gia 1.1. 1.2.0 (25/9/2026): skill moi kpi-tu-danh-gia (giai doan 2); kpi-lap-ke-hoach 1.1. 1.1.2 (24/9/2026): nhat ky tu dong ra khoi git, "#riêng" khong ghi (CP-20260924-001). 1.1.1 (24/9/2026): doi_soat doc anh xa bo sung bang ma don vi; quan-tri 1.11. 1.1.0 (24/9/2026): skill moi kpi-lap-ke-hoach (QD 1923). 1.0.1: doi_soat; 1.0.0 (21/9): ban chinh thuc


# Chi don cac thu muc SINH TU DONG. README.md/CHANGELOG.md o goc 31-Plugin/ la viet
# tay, KHONG duoc dong o day — bai hoc 18/9/2026: lan dau don ca thu muc goc da
# xoa mat ca hai tep nay.
THU_MUC_SINH_TU_DONG = ["skills", ".claude-plugin", "hooks", "scripts", "agents"]
# Nguon viet tay cua script/agent them vao plugin (khong sua trong 31-Plugin/)
PLUGIN_SRC = os.path.join(DU_AN, "29-Cong-Cu", "plugin_src")
CONG_CU_CHO_AGENT = ["tra_hieu_luc.py", "kiem_vien_dan.py", "duong_dan.py",
                     "doi_soat_so_lieu.py", "kiem_minh_chung.py",
                     # kiem_the_thuc.py: phep kiem SO 1 cua ktc-kiem-san-pham va ktc-kiem-ho-so-don-vi;
                     # thieu tu 19/9/2026 -> hai agent do hong lang le khi chay NGOAI thu muc du an
                     "kiem_the_thuc.py",
                     # 24/9/2026: bo cong cu KPI ca nhan (skill kpi-lap-ke-hoach mang ban sao rieng trong goi)
                     "kpi_calc.py", "kpi_mau.py", "validate_plan.py",
                     # 25/9/2026: tu danh gia KPI ca nhan (skill kpi-tu-danh-gia)
                     "kpi_danh_gia.py",
                     # 28/10/2026: kiem nhat quan, ho so minh chung, doi chieu cheo — 3 agent moi goi
                     "kpi_nhat_quan.py", "lap_ho_so_minh_chung.py", "kpi_doi_chieu_cheo.py",
                     # 28/9/2026 (1.3.6): bo dung bao cao thang tu ban da ban hanh (skill bao-cao v3.18) va Track Changes
                     # (Nguyen tac 8) — truoc chi co trong du an, plugin phan phoi thieu -> san pham kem (chay thu 28/9)
                     "bc_thang.py", "vanphong.py", "trich_tuong_thuat.py", "ktc_trackchanges.py",
                     # 5/11/2026 (1.4.0): kiem thuat ngu phap ly TN01-TN04 (agent ktc-kiem-thuat-ngu)
                     "kiem_thuat_ngu.py",
                     # 5/11/2026 (1.4.1): skill ke-hoach va kpi-lap-ke-hoach bao chay cong cu nay
                     # (xuat tep nap phan mem KPI tinh, 27/10/2026) nhung no CHUA TUNG duoc dong vao
                     # goi — goi .skill dong 29/9 con cu nen khong ai thay. Lo ra khi dong goi lai.
                     "xuat_mau_import_kpi.py"]
# Script chi chay tren may phat trien (Task Scheduler), KHONG dong vao plugin phan phoi (1.3.0, C-01/R2-01)
CHI_DUNG_NOI_BO = {"ktc_backup_github.py"}
# Chuan chung chen vao moi SKILL.md va agent khi dung (20-Chuan-Chung/20-..., 1.3.0)
CHUAN_CHUNG = os.path.join(DU_AN, "20-Chuan-Chung", "20-Quy-Tac-Bat-Bien-Va-Khuon-Dau-Ra.md")
# Gioi han cua Claude khi tai plugin/skill (loi that 19/9/2026: mo ta plugin 554 ky tu bi tu choi)
GIOI_HAN_MO_TA_PLUGIN = 500
GIOI_HAN_MO_TA_SKILL = 1024


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
    print(f"── Giai nen {len(GOI_NGUON)} goi .skill da xac minh vao 31-Plugin/skills/ ──")
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


def so_agent() -> int:
    """Dem agent THAT SU se duoc dong vao goi. Khong ghi tay con so vao mo ta:
    5/11/2026 mo ta ghi "36 agent" trong khi goi co 38 — viet tay luc du kien, sau do
    go mot agent ma quen sua. Mo ta nay hien tren thu vien to chuc cho moi don vi doc."""
    d = os.path.join(PLUGIN_SRC, "agents")
    if not os.path.isdir(d):
        return 0
    return len([f for f in os.listdir(d) if f.endswith(".md") and f not in CHI_DUNG_NOI_BO])


def build_manifest():
    print("── Ghi .claude-plugin/plugin.json ──")
    manifest = {
        "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
        "name": "ktc-quan-tri",
        "displayName": "KTC Quản trị",
        "version": PLUGIN_VERSION,
        # Cowork tu choi mo ta > 500 ky tu (loi upload 0.8.0, 19/9/2026) — build_manifest() tu chan.
        "description": (
            "Quản trị nhiệm vụ khép kín của Trường Cao đẳng Kon Tum: Kế hoạch → Theo dõi → Báo cáo → "
            "Soạn thảo văn bản. 8 skill (quan-tri, ke-hoach, theo-doi-cv, bao-cao, soan-thao-vb, the-thuc, "
            f"kpi-lap-ke-hoach, kpi-tu-danh-gia); {so_agent()} agent — tra cứu căn cứ, kiểm hồ sơ đơn vị, kiểm sản phẩm, "
            "quét hiệu lực viện dẫn, xác minh minh chứng, kiểm thuật ngữ pháp lý TN01–TN04, tra Từ điển pháp lý "
            "và Hỏi đáp chính sách 13 lĩnh vực, tự học, tự cải tiến; "
            "hook chặn ghi kho chuẩn, nhật ký không lưu nội dung, đo thể thức."
        ),
        "author": {
            "name": "Trường Cao đẳng Kon Tum - Phòng Tổng hợp - Hành chính và Quản trị"
        },
        "keywords": ["ktc", "vietnam", "quan-tri", "ke-hoach", "bao-cao", "soan-thao-van-ban"],
        "defaultEnabled": False,
        "metadata": {
            "builtFrom": f"{len(GOI_NGUON)} gói .skill hiện hành (GOI_NGUON trong 29-Cong-Cu/dong_goi_plugin.py, "
                         "danh sách ở parallelWith); lần dựng đầu 18/9/2026 từ 5 gói (DL-20260918-001)",
            "claudeStrictValidation": "ĐẠT 26/9/2026 (bản 1.3.0, claude.exe 2.1.283) — `claude plugin validate "
                                       "./31-Plugin --strict`; bản 1.2.1 KHÔNG đạt với CLI 2.1.283 (YAML mô tả agent "
                                       "ktc-kiem-san-pham, đã sửa ở 1.3.0); chạy lại mỗi lần dựng.",
            "parallelWith": ["ktc-quan-tri-v1.17.skill", "ktc-bao-cao-v3.21.skill", "ktc-ke-hoach-v3.13.skill",
                              "ktc-soan-thao-vb-v1.17.skill", "ktc-theo-doi-cv-v1.11.skill",
                              "ktc-the-thuc-v1.4.skill", "ktc-kpi-lap-ke-hoach-v1.5.skill",
                              "ktc-kpi-tu-danh-gia-v1.4.skill"],
        },
    }
    if len(manifest["description"]) > GIOI_HAN_MO_TA_PLUGIN:
        raise SystemExit(f"Mo ta plugin {len(manifest['description'])} ky tu > {GIOI_HAN_MO_TA_PLUGIN} — Cowork se tu choi")
    ghi_json(os.path.join(PLUGIN_DIR, ".claude-plugin", "plugin.json"), manifest)
    print("  ✓ plugin.json")


def lenh(script: str, *args: str) -> dict:
    tham_so = "".join(f" {a}" for a in args)
    return {"type": "command",
            "command": f'python "${{CLAUDE_PLUGIN_ROOT}}/scripts/{script}"{tham_so}'}


def build_hooks():
    print("── Ghi hooks/hooks.json (doctor + nhật ký + guard chặn ghi kho chuẩn) ──")
    hooks = {
        "hooks": {
            # 1.3.0: KHONG con backup GitHub trong plugin (tham dinh lan 1 C-01, lan 2 R2-01) — backup la
            # tac vu theo lich cua quan tri vien tren may phat trien, chay tu 29-Cong-Cu/plugin_src/scripts/.
            "SessionStart": [{"hooks": [
                lenh("ktc_quan_tri_doctor.py"),
                lenh("ktc_nhat_ky.py", "nap"),
            ]}],
            # 1.3.0: guard doc lap chan ghi/xoa KTC-Database, 03-Templates, 04-Good-Documents (C-04, R2-03)
            "PreToolUse": [{"matcher": "Write|Edit|MultiEdit|NotebookEdit|Bash|PowerShell",
                            "hooks": [{**lenh("ktc_guard.py"), "timeout": 30}]}],
            # Khong ghi Read/Grep/Glob de log khong bi ngap; chi thao tac co tac dung.
            "PostToolUse": [{"matcher": "Write|Edit|Bash|PowerShell|Skill|Agent",
                             "hooks": [lenh("ktc_nhat_ky.py", "ghi"),
                                       # DL-20260919-003: tu do the thuc .docx/.xlsx vua sinh
                                       {**lenh("ktc_the_thuc_hook.py"), "timeout": 60}]}],
            # DL-20260919-005: ghi loi nguoi dung + tin hieu hoc cho agent ktc-tu-hoc
            "UserPromptSubmit": [{"hooks": [lenh("ktc_nhat_ky.py", "yeu-cau")]}],
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
            if f in CHI_DUNG_NOI_BO:
                print(f"  - {thu_muc}/{f} (chỉ dùng nội bộ, không đóng vào plugin)")
                continue
            if f.endswith((".py", ".md")):
                shutil.copyfile(os.path.join(src, f), os.path.join(dst, f))
                print(f"  ✓ {thu_muc}/{f}")
    # Cong cu dung cho agent khi chay NGOAI du an (DL-20260919-004) — ban goc o 29-Cong-Cu/, khong sua ban trong plugin
    for f in CONG_CU_CHO_AGENT:
        shutil.copyfile(os.path.join(DU_AN, "29-Cong-Cu", f), os.path.join(PLUGIN_DIR, "scripts", f))
        print(f"  ✓ scripts/{f} (từ 29-Cong-Cu)")


DOCTOR_SCRIPT = r'''# -*- coding: utf-8 -*-
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
'''


def build_doctor_script():
    print("── Ghi scripts/ktc_quan_tri_doctor.py ──")
    path = os.path.join(PLUGIN_DIR, "scripts", "ktc_quan_tri_doctor.py")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(DOCTOR_SCRIPT)
    print("  ✓ ktc_quan_tri_doctor.py")


def khoi_chuan_chung() -> str:
    s = io.open(CHUAN_CHUNG, encoding="utf-8").read()
    m = re.search(r"<!-- KHOI-CHEN-BAT-DAU -->\s*\n(.*?)\n<!-- KHOI-CHEN-KET-THUC -->", s, re.S)
    if not m:
        raise SystemExit(f"Khong tim thay khoi chen trong {CHUAN_CHUNG}")
    return m.group(1).strip() + "\n"


def chen_vao(path: str, khoi: str) -> str:
    """Chen khoi ngay truoc tieu de cap 2 dau tien sau frontmatter. Da co <immutable_rules> thi bo qua."""
    s = io.open(path, encoding="utf-8").read()
    if "<immutable_rules>" in s:
        return "đã có"
    m_fm = re.match(r"^---\r?\n.*?\r?\n---\r?\n", s, re.S)
    dau = m_fm.end() if m_fm else 0
    m = re.search(r"^## ", s[dau:], re.M)
    vt = dau + m.start() if m else len(s)
    s2 = s[:vt] + khoi + "\n" + s[vt:]
    io.open(path, "w", encoding="utf-8").write(s2)
    return "đã chèn"


def khoi_day_du() -> str:
    """Ban day du (dien giai, vi du, bang ma canh bao) — ghi thanh references/, chi nap khi can (1.3.1)."""
    s = io.open(CHUAN_CHUNG, encoding="utf-8").read()
    m = re.search(r"<!-- KHOI-DAY-DU-BAT-DAU -->\s*\n(.*?)\n<!-- KHOI-DAY-DU-KET-THUC -->", s, re.S)
    if not m:
        raise SystemExit(f"Khong tim thay khoi day du trong {CHUAN_CHUNG}")
    return m.group(1).strip() + "\n"


TEN_DAY_DU = "00-Quy-Tac-Bat-Bien-Day-Du.md"
TEN_LICH_SU = "LICH-SU-PHIEN-BAN.md"


def tach_lich_su(skill_md: str) -> int:
    """1.3.1 (ChatGPT L3 muc 4): chuyen cac doan trich dan lich su "> **vX.Y** (ngay) — ..." o dau SKILL.md sang
    references/LICH-SU-PHIEN-BAN.md; SKILL.md con 1 dong tro toi. Khong dong den dong "Phien ban: X" ma doctor doc.
    Tra ve so muc da chuyen."""
    s = io.open(skill_md, encoding="utf-8").read()
    doan = re.split(r"(\n\s*\n)", s)
    giu, lich_su = [], []
    for d in doan:
        if re.match(r"\s*> \*\*v\d+(\.\d+)+\*\* \(", d):
            lich_su.append(d.strip())
        else:
            giu.append(d)
    if not lich_su:
        return 0
    s2 = "".join(giu)
    # dong tro toi ngay sau tieu de cap 1 dau tien
    m = re.search(r"^# .*$", s2, re.M)
    tro = f"\n\n> Lịch sử phiên bản: `references/{TEN_LICH_SU}` (không cần đọc khi làm việc)."
    s2 = s2[:m.end()] + tro + s2[m.end():] if m else s2
    s2 = re.sub(r"\n{3,}", "\n\n", s2)
    io.open(skill_md, "w", encoding="utf-8").write(s2)
    d = os.path.join(os.path.dirname(skill_md), "references")
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, TEN_LICH_SU), "w", encoding="utf-8").write(
        "# Lịch sử phiên bản (tách khỏi SKILL.md khi dựng plugin 1.3.1 — không nạp khi làm việc)\n\n"
        + "\n\n".join(lich_su) + "\n")
    return len(lich_su)


# 1.3.8 (Cowork 28/9/2026): skill soan-thao-vb xin quyen them CA thu muc du an KTC-Quan-tri vao phien (du lieu roi may,
# co KPI ca nhan, nhat ky) chi de doc "ban goc" 20-Chuan-Chung/, 26-KTC-Soan-Thao-VB/... — ban sao da nam trong goi.
KHOI_DUONG_DAN = """
<plugin_paths>
**Đường dẫn trong plugin.** Tên thư mục dự án trong tài liệu (`20-Chuan-Chung/`, `2x-KTC-…/`, `29-Cong-Cu/`,
`92-Kinh-Nghiem/`…) là nơi đặt **bản gốc trên máy phát triển**. Chạy qua plugin, Cowork, Claude trò chuyện: tìm **bản sao
trong gói** theo tên tệp (thư mục kỹ năng, `skills/*/references/`, `scripts/` ở gốc plugin); tên khác bản gốc thì tra
`skills/quan-tri/references/BAN-DO-TEP.md` (có cả danh mục tệp nằm ở kho KTC-Database, plugin 897). **Không xin quyền, không thêm
thư mục dự án KTC-Quan-tri vào phiên** để đọc quy tắc — thư mục đó có dữ liệu cá nhân và không cần cho việc chạy. Không
thấy tệp → làm theo SKILL.md, ghi `THIEU_DU_LIEU`, không đoán. Đầu vào, đầu ra: thư mục làm việc của người dùng (Nguyên tắc 3).
</plugin_paths>
"""


def chen_chuan_chung():
    print("── Chèn chuẩn chung (lõi) vào mọi skill và agent; bản đầy đủ vào references/ của skill ──")
    import glob
    khoi = khoi_chuan_chung() + KHOI_DUONG_DAN
    day_du = khoi_day_du()
    for p in sorted(glob.glob(os.path.join(PLUGIN_DIR, "skills", "*", "SKILL.md")) +
                    glob.glob(os.path.join(PLUGIN_DIR, "agents", "*.md"))):
        ghi_chu = chen_vao(p, khoi)
        if os.path.basename(p) == "SKILL.md":
            d = os.path.join(os.path.dirname(p), "references")
            os.makedirs(d, exist_ok=True)
            io.open(os.path.join(d, TEN_DAY_DU), "w", encoding="utf-8").write(day_du)
            n = tach_lich_su(p)
            ghi_chu += f" · {TEN_DAY_DU}" + (f" · tách {n} mục lịch sử" if n else "")
        print(f"  ✓ {os.path.relpath(p, PLUGIN_DIR):40s} {ghi_chu}")


def kiem_mo_ta():
    """Chan truoc khi dong goi: mo ta skill/agent vuot gioi han thi Claude tu choi khi tai len."""
    print("── Kiểm độ dài mô tả (plugin ≤ 500, skill/agent ≤ 1024 ký tự) ──")
    sai = []
    for loai, mau in (("skill", os.path.join(PLUGIN_DIR, "skills", "*", "SKILL.md")),
                      ("agent", os.path.join(PLUGIN_DIR, "agents", "*.md"))):
        import glob
        for p in sorted(glob.glob(mau)):
            s = io.open(p, encoding="utf-8").read()
            m = re.search(r"^description:\s*(.*)$", s, re.M)
            tho = m.group(1).strip() if m else ""
            d = tho.strip('"') if m else ""
            if not d or len(d) > GIOI_HAN_MO_TA_SKILL:
                sai.append(f"{loai} {os.path.relpath(p, PLUGIN_DIR)}: {len(d)} ký tự")
            # Loi that 19-26/9/2026: mo ta agent khong dat ngoac ma chua ": " -> YAML hong, luc chay
            # agent mat toan bo truong frontmatter (claude plugin validate --strict 2.1.283 phat hien)
            if tho and not tho.startswith(("'", '"')) and ": " in tho:
                sai.append(f"{loai} {os.path.relpath(p, PLUGIN_DIR)}: mô tả không đặt trong ngoặc mà có ': ' — YAML hỏng")
    if sai:
        raise SystemExit("Mô tả không hợp lệ:\n  " + "\n  ".join(sai))
    print("  ✓ mọi mô tả trong giới hạn")


def dong_goi_zip():
    """Dong goi 31-Plugin thanh .zip LAP LAI DUOC de tai len Cowork / Claude Chat.

    Lap lai duoc = cung nguon thi cung sha256. Dat moc thoi gian co dinh trong ZipInfo va
    duyet tep theo thu tu da sap xep; neu khong, moi lan dong goi ra mot sha khac va khong
    ai kiem chung duoc goi dang chay co dung tu nguon nay hay khong.

    Loai tru: desktop.ini (tep cua Google Drive), __pycache__, .pyc, va MOI archive long
    (.zip/.skill) — goi long trong goi chi lam phinh ban tai ve, khong co tac dung luc chay.
    """
    BO_TEN = {"desktop.ini", ".DS_Store"}
    BO_DUOI = {".pyc", ".pyo", ".zip", ".skill"}
    ra = os.path.join(DU_AN, "30-Ket-Qua", dt.date.today().isoformat(), "Plugin")
    os.makedirs(ra, exist_ok=True)
    dich = os.path.join(ra, "ktc-quan-tri-" + PLUGIN_VERSION + ".zip")
    tep = []
    for r, ds, fs in os.walk(PLUGIN_DIR):
        ds[:] = sorted(x for x in ds if x != "__pycache__")
        for f in sorted(fs):
            if f in BO_TEN or os.path.splitext(f)[1].lower() in BO_DUOI:
                continue
            q = os.path.join(r, f)
            tep.append((q, os.path.relpath(q, PLUGIN_DIR).replace(os.sep, "/")))
    tep.sort(key=lambda x: x[1])
    with zipfile.ZipFile(dich, "w") as z:
        for q, rel in tep:
            zi = zipfile.ZipInfo(rel, date_time=(2026, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.create_system = 3
            zi.external_attr = 0o100644 << 16
            z.writestr(zi, io.open(q, "rb").read())
    sha = hashlib.sha256(io.open(dich, "rb").read()).hexdigest()
    io.open(dich + ".sha256", "w", encoding="utf-8").write(sha + "  " + os.path.basename(dich) + '\n')
    print("  ✓ " + os.path.relpath(dich, DU_AN) + "  (%d tệp, %d bytes)" % (len(tep), os.path.getsize(dich)))
    print("    sha256 " + sha)
    return dich


def giai_nen_goi_long():
    """1.3.9: goi .skill long trong ky nang (vd ke-hoach/references/ktc-tu-hoc-ke-hoach.skill) bi BO_DUOI loai khi dong
    zip -> plugin thieu phan tu hoc ke hoach. Giai nen thanh references/<ten>/ (bo agents/ cua ben thu ba)."""
    import glob
    print("── Giải nén gói .skill lồng trong kỹ năng ──")
    for p in sorted(glob.glob(os.path.join(PLUGIN_DIR, "skills", "**", "*.skill"), recursive=True)):
        dich = os.path.join(os.path.dirname(p), os.path.splitext(os.path.basename(p))[0])
        with zipfile.ZipFile(p) as z:
            ten = [n for n in z.namelist() if not n.endswith("/") and not n.startswith("agents/")]
            goc = os.path.commonprefix([n.split("/")[0] + "/" for n in ten]) if all("/" in n for n in ten) else ""
            for n in ten:
                rel = n[len(goc):] if goc and n.startswith(goc) and not n.startswith(("references/", "scripts/")) else n
                out = os.path.join(dich, *rel.split("/"))
                os.makedirs(os.path.dirname(out), exist_ok=True)
                io.open(out, "wb").write(z.read(n))
        print(f"  ✓ {os.path.relpath(p, PLUGIN_DIR)} → {os.path.relpath(dich, PLUGIN_DIR)}/ ({len(ten)} tệp)")


TEN_BAN_DO = "BAN-DO-TEP.md"

# 1.3.13 (thẩm định lần 5, L5-04): git trên Windows (core.autocrlf=true) checkout ra CRLF, thư mục làm việc lẫn LF/CRLF
# -> dựng từ bản checkout sạch của cùng commit ra sha256 khác (17 tệp khác xuống dòng, BAN-DO-TEP mất 10 dòng vì so
# băm). Chuẩn hóa: tệp văn bản về LF (.cmd/.bat về CRLF) trước khi nén; so băm bỏ qua CR.
DUOI_VAN_BAN = {".md", ".py", ".json", ".txt", ".csv", ".yaml", ".yml", ".ps1", ".sh", ".html", ".xml", ".toml"}
DUOI_CRLF = {".cmd", ".bat"}


def _bam_lf(q):
    return hashlib.sha256(io.open(q, "rb").read().replace(b"\r\n", b"\n")).hexdigest()


def chuan_hoa_xuong_dong():
    print("── Chuẩn hóa xuống dòng (dựng lặp lại được từ mọi bản checkout) ──")
    doi = 0
    for r, ds, fs in os.walk(PLUGIN_DIR):
        for f in fs:
            duoi = os.path.splitext(f)[1].lower()
            if duoi not in DUOI_VAN_BAN and duoi not in DUOI_CRLF:
                continue
            q = os.path.join(r, f)
            b = io.open(q, "rb").read()
            n = b.replace(b"\r\n", b"\n")
            if duoi in DUOI_CRLF:
                n = n.replace(b"\n", b"\r\n")
            if n != b:
                io.open(q, "wb").write(n)
                doi += 1
    print(f"  ✓ {doi} tệp đổi xuống dòng")


def lap_ban_do_tep():
    """1.3.9: bang doi chieu ten tep BAN GOC (du an) -> vi tri trong plugin, lap tu dong bang so noi dung (sha256).
    Cowork 28/9: skill tim '13-Bang-Ma-Don-Vi.md' theo ten goc, khong thay (trong goi ten la 12-Bang-Ma-Don-Vi.md) ->
    xin quyen ca thu muc du an."""
    import glob
    print("── Lập bảng đối chiếu tên tệp (bản gốc dự án → vị trí trong plugin) ──")
    theo_bam = {}
    for q in glob.glob(os.path.join(PLUGIN_DIR, "**", "*.*"), recursive=True):
        if os.path.isfile(q):
            theo_bam.setdefault(_bam_lf(q), []).append(os.path.relpath(q, PLUGIN_DIR).replace("\\", "/"))
    dong = []
    for src in sorted(glob.glob(os.path.join(DU_AN, "20-Chuan-Chung", "*.md"))):
        h = _bam_lf(src)
        vt = sorted(theo_bam.get(h, []))
        if vt:
            dong.append(f"| `20-Chuan-Chung/{os.path.basename(src)}` | " + " · ".join(f"`{v}`" for v in vt[:3])
                        + (f" (+{len(vt) - 3})" if len(vt) > 3 else "") + " |")
    for goc, noi in (("20-Chuan-Chung/20-Quy-Tac-Bat-Bien-Va-Khuon-Dau-Ra.md", "`skills/*/references/00-Quy-Tac-Bat-Bien-Day-Du.md`"),
                     ("29-Cong-Cu/<công cụ>.py", "`scripts/<công cụ>.py` (và bản trong kỹ năng nếu có)"),
                     ("23-KTC-Ke-Hoach/references/ktc-tu-hoc-ke-hoach.skill", "`skills/ke-hoach/references/ktc-tu-hoc-ke-hoach/`")):
        dong.append(f"| `{goc}` | {noi} |")
    nd = ("# Bảng đối chiếu tên tệp — bản gốc (dự án) → vị trí trong plugin\n\n"
          f"Sinh tự động khi dựng plugin {PLUGIN_VERSION} (`dong_goi_plugin.py`, so nội dung sha256). Tài liệu nhắc tên thư mục\n"
          "dự án (`20-Chuan-Chung/…`, `29-Cong-Cu/…`): tra bảng này, **không xin quyền thư mục dự án**.\n\n"
          "| Bản gốc trên máy phát triển | Bản sao trong plugin |\n|---|---|\n" + "\n".join(dong) + "\n\n"
          "## Không nằm trong plugin — đúng thiết kế\n\n"
          "| Loại | Ở đâu | Khi không có |\n|---|---|---|\n"
          "| Mẫu `.dotx`/`.xltx`, `00-Template-Registry-KTC-DIS.docx`, `KTC-DIS-Master-Index_*.xlsx`, văn bản đã ban hành "
          "(BC/PL/KH tháng, TB giao ban, CTCT năm) | Kho **KTC-Database** (Google Drive, chỉ đọc) — `scripts/duong_dan.py` | "
          "Hỏi người dùng đính kèm; `THIEU_DU_LIEU` |\n"
          "| Checklist, Skill-Library của rà soát 897 (`Checklist/0x-….md`, `19-Skill-Danh-Gia-Chat-Luong-Van-Ban.md`, "
          "`31-Quy-Tac-Van-Hanh-Theo-Tinh-Huong.md`, `17-Skill-Kiem-Tra-Tham-Quyen.md`, `29-Skill-Van-Ban-Dang.md`, mẫu prompt 897) | Plugin **ktc-ra-soat-897** cài kèm | Nêu rõ chưa rà "
          "soát theo 897 |\n"
          "| `MEMORY-INDEX.md`, `Pending.md`, `TRI-THUC.md`, `90-Nhat-Ky-Van-Hanh/`, `92-Kinh-Nghiem/`, `10-Dau-Vao/` của dự án, "
          "công cụ phát triển (`kiem_tra_he_thong.py`, `dong_goi_*.py`, `test_*.py`) | Chỉ máy quản trị P-THHC | Bỏ qua — "
          "không cần khi chạy |\n")
    p = os.path.join(PLUGIN_DIR, "skills", "quan-tri", "references", TEN_BAN_DO)
    io.open(p, "w", encoding="utf-8").write(nd)
    print(f"  ✓ {os.path.relpath(p, PLUGIN_DIR)} ({len(dong)} dòng)")


def nhan_ban_chuan_chung():
    """Nhan ban quy tac dung chung tu 20-Chuan-Chung/ XUONG ban sao trong moi goi skill (CLAUDE.md:
    "Sua o 20-Chuan-Chung/ truoc, roi nhan ban xuong tai buoc build").

    Truoc 1.4.0 KHONG co buoc nay: ban sao trong .skill cu dan, lech ban goc ma khong ai thay
    (phat hien 5/11/2026 — 00-Nguyen-Tac-Chung, 17-Quy-Tac-Vien-Dan, 18-Chuan-The-Thuc-San-Pham
    deu cu hon ban goc, BAN-DO-TEP mat 3 dong vi khong khop so bam).
    """
    print("── Nhân bản quy tắc dùng chung 20-Chuan-Chung/ xuống các gói skill ──")
    goc_dir = os.path.join(DU_AN, "20-Chuan-Chung")
    # "00-README.md" trung ten nhung KHAC noi dung (moi skill co README rieng) — khop ten tran
    # se ghi de README cua skill. Chi nhan ban tep co so thu tu quy tac, va chi trong references/.
    BO_QUA = {"00-README.md"}
    ban_goc = {f: os.path.join(goc_dir, f) for f in os.listdir(goc_dir)
               if f.endswith(".md") and f not in BO_QUA and re.match(r"^\d\d-", f)}
    so = 0
    for r, _ds, fs in os.walk(os.path.join(PLUGIN_DIR, "skills")):
        if "references" not in os.path.relpath(r, PLUGIN_DIR).split(os.sep):
            continue
        for f in fs:
            if f not in ban_goc:
                continue
            dich = os.path.join(r, f)
            if _bam_lf(dich) == _bam_lf(ban_goc[f]):
                continue
            shutil.copyfile(ban_goc[f], dich)
            so += 1
            print(f"  ✓ {os.path.relpath(dich, PLUGIN_DIR)} ← 20-Chuan-Chung/{f}")
    print(f"  {so} bản sao đã cập nhật" if so else "  ✓ mọi bản sao đã khớp bản gốc")


if __name__ == "__main__":
    don_sach(PLUGIN_DIR)
    build_skills()
    giai_nen_goi_long()
    nhan_ban_chuan_chung()
    build_manifest()
    build_hooks()
    build_doctor_script()
    chep_nguon_viet_tay()
    lap_ban_do_tep()
    chen_chuan_chung()
    kiem_mo_ta()
    chuan_hoa_xuong_dong()
    print("── Đóng gói .zip (lặp lại được) ──")
    dong_goi_zip()
    print()
    print(f"Đã dựng 31-Plugin tại: {PLUGIN_DIR}")
