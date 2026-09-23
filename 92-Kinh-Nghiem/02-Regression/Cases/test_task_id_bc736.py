# -*- coding: utf-8 -*-
"""Hoi quy KI-001 (DL-20260918-003): read_bc736_excel.py v3.3 doc cot Task_ID.

Dung ho so THAT cua don vi (chep sang thu muc tam, khong sua tep goc):
  1. Tep chua co cot Task_ID -> ket qua GIONG HET ban v3.2 (khong hoi to, khong vo).
  2. Them cot Task_ID vao CUOI bang -> doc dung ma; ca nguoc: ma sai dinh dang / trung ma -> canh bao.
"""
import glob, os, shutil, subprocess, sys, tempfile, warnings
warnings.filterwarnings("ignore")
GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
LIB = os.path.join(GOC, "25-KTC-Bao-Cao", "references", "Skill-Library")
sys.path.insert(0, LIB)
import read_bc736_excel as moi
from openpyxl import load_workbook
loi = []
def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk: loi.append(ten)

def bo_task_id(kq):
    for ds in list(kq["truc"].values()) + [kq["muc_ii_items"]]:
        for t in ds: t.pop("task_id", None)
    return kq

# ban cu v3.2 tu git (commit 33f2f3d — ngay truoc khi them Task_ID, truoc khi doi ten thu muc)
cu_src = subprocess.run(["git", "-C", GOC, "show", "33f2f3d:KTC-Bao-Cao/references/Skill-Library/read_bc736_excel.py"],
                        capture_output=True).stdout
with tempfile.TemporaryDirectory() as t:
    if b"_doc_task_id" in cu_src:
        print("  (HEAD da la v3.3 — bo qua so sanh voi v3.2)"); cu = None
    else:
        open(os.path.join(t, "bc736_cu.py"), "wb").write(cu_src); sys.path.insert(0, t)
        import bc736_cu as cu
    # Ho so that GHIM tu git (commit fa096af — ngay truoc 54a2476 sap xep lai 10-Dau-Vao/01-Dau-Moi-Nop/2026-09
    # thanh "1. BAO CAO PL IIB"/"2. Phu luc Ib", doi ten tep va xoa bot don vi). Doc thu muc dang song thi ca thu
    # vo moi lan dau vao thay doi; "them == 2" chi dung tren dung bo 26 tep nay.
    GHIM, THU = "fa096af", "10-Dau-Vao/01-Dau-Moi-Nop/2026-09"
    ds = subprocess.run(["git", "-C", GOC, "-c", "core.quotepath=off", "ls-tree", "-r", "--name-only", GHIM, "--", THU],
                        capture_output=True, text=True, encoding="utf-8").stdout.split("\n")
    for n in ds:
        if n.endswith(".xlsx") and n.count("/") == THU.count("/") + 2:
            dich = os.path.join(t, "ho_so", *n.split("/")[-2:])
            os.makedirs(os.path.dirname(dich), exist_ok=True)
            open(dich, "wb").write(subprocess.run(["git", "-C", GOC, "show", f"{GHIM}:{n}"], capture_output=True).stdout)
    tep = sorted(glob.glob(os.path.join(t, "ho_so", "*", "*.xlsx")))
    kiem(len(tep) >= 4, f"có hồ sơ thật để thử ({len(tep)} tệp)")
    if cu:
        # Chi duoc khac o cho: v3.3 lay LAI nhiem vu "Tong hop/Tong ket…" co so TT ma v3.2 bo mat
        def dem(k): return k["thong_ke"].get("so_nhiem_vu", 0)
        khac, them = [], 0
        for f in tep:
            a, b = bo_task_id(moi.read_appendix(f)), cu.read_appendix(f)
            if a != b:
                if dem(a) > dem(b): them += dem(a) - dem(b)
                else: khac.append(os.path.basename(os.path.dirname(f)) + "/" + os.path.basename(f))
        kiem(not khac, f"tệp chưa có cột Task_ID: không mất gì so với v3.2 {khac[:3]}")
        kiem(them == 2, f"lấy lại đúng 2 nhiệm vụ 'Tổng hợp/Tổng kết…' v3.2 bỏ sót (thực tế: {them})")
    # them cot Task_ID vao cuoi bang cua 1 tep KH that
    kh = next(f for f in tep if os.path.basename(f).startswith("KH-"))
    ban = os.path.join(t, "kh.xlsx"); shutil.copyfile(kh, ban)
    wb = load_workbook(ban); ws = wb.active
    hdr = next(r for r in range(1, 30) if str(ws.cell(r, 1).value or "").strip().upper() == "TT")
    cot = ws.max_column + 1
    ws.cell(hdr, cot, "Task_ID")
    # chon dong nhiem vu KHONG bat dau bang "Tong" de ca thu doc lap voi loi dong cong
    dong = [r for r in range(hdr + 1, ws.max_row + 1)
            if ws.cell(r, 2).value and not str(ws.cell(r, 2).value).strip().lower().startswith("tổng") and "." in str(ws.cell(r, 1).value or "")][:3]  # dong nhiem vu "1.1", khong phai nhan Truc
    ma = ["KTC-2026-T09-00001", "KTC-2026-T09-00001", "sai-ma"]
    for r, m in zip(dong, ma): ws.cell(r, cot, m)
    wb.save(ban)
    kq = moi.read_appendix(ban)
    tat = [x for ds in kq["truc"].values() for x in ds] + kq["muc_ii_items"]
    doc = [x["task_id"] for x in tat if x.get("task_id")]
    kiem("KTC-2026-T09-00001" in doc, "đọc được Task_ID ở cột cuối (dò theo tên tiêu đề)")
    kiem(any("TASK_ID TRÙNG" in c for c in kq["canh_bao"]), "ca ngược: mã trùng -> cảnh báo")
    kiem(any("TASK_ID SAI ĐỊNH DẠNG" in c for c in kq["canh_bao"]), "ca ngược: mã sai định dạng -> cảnh báo")
    kiem(not any("TASK_ID" in c for c in moi.read_appendix(kh)["canh_bao"]), "tệp gốc không có cột -> không cảnh báo Task_ID")
print("KET LUAN:", "CO LOI " + str(loi) if loi else "SACH")
sys.exit(1 if loi else 0)
