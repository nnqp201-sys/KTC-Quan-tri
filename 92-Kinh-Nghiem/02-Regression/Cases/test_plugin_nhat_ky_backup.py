# -*- coding: utf-8 -*-
"""Hoi quy cho 2 hook cua plugin ktc-quan-tri: tu ghi nhat ky va tu backup GitHub.

Moi ca deu co ca THU NGUOC (biet chac sai) — bai hoc LL-20260914-001: phep kiem bao "sach"
ngay lan dau thi phai nghi chinh phep kiem. Chay trong thu muc tam, khong dung repo that.
"""
import json
import io
import os
import subprocess
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
NK = os.path.join(GOC, "29-Cong-Cu", "plugin_src", "scripts", "ktc_nhat_ky.py")
BK = os.path.join(GOC, "29-Cong-Cu", "plugin_src", "scripts", "ktc_backup_github.py")
loi = []


THAT = os.path.join(GOC, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")


def anh_log_that():
    """Anh chup nhat ky THAT — chi dem dong do CHINH BO THU nay co the sinh ra.

    KHONG so kich thuoc tep: hook PostToolUse cua phien lam viec dang chay cung ghi vao
    day khi lenh chay trong thu muc du an, nen so byte doi lien tuc vi ly do khong lien
    quan den bo thu. So byte tung lam ca kiem nay TRUOT ngau nhien — that bai gia, va la
    loai that bai te nhat vi no day nguoi ta di sua thu khong hong.

    Rui ro thuc su can chan: script backup hoac script nhat ky ghi NHAM vao du an that.
    Ca hai deu ghi dong co loai 'backup' hoac 'yeu-cau'/'thao-tac' — dem rieng loai
    'backup' la du, vi bo thu chi chay script backup.
    """
    if not os.path.isdir(THAT):
        return {}
    dem = {}
    for f in os.listdir(THAT):
        if not f.endswith('.jsonl'):
            continue
        n = 0
        for dong in io.open(os.path.join(THAT, f), encoding='utf-8', errors='replace'):
            try:
                if json.loads(dong).get('loai') == 'backup':
                    n += 1
            except Exception:
                pass
        dem[f] = n
    return dem


def chay(args, stdin=""):
    e = dict(os.environ)
    e.pop("CLAUDE_PROJECT_DIR", None)   # de script tu tim du an theo cwd trong input
    e.pop("KTC_NHAT_KY_NOI_DUNG", None)  # ca mac dinh: khong chon ghi noi dung
    return subprocess.run([sys.executable, *args], input=stdin, capture_output=True, text=True,
                          encoding="utf-8", env=e, cwd=GOC)  # cwd = du an THAT: bat loi ghi nham


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        loi.append(ten)


def git(*a):
    subprocess.run(["git", *a], capture_output=True)


truoc = anh_log_that()
with tempfile.TemporaryDirectory() as t:
    du_an = os.path.join(t, "du_an"); khac = os.path.join(t, "khac")
    os.makedirs(os.path.join(du_an, "90-Nhat-Ky-Van-Hanh")); os.makedirs(khac)
    log_dir = os.path.join(du_an, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")

    print("== ktc_nhat_ky.py ==")
    chay([NK, "ghi"], json.dumps({"session_id": "s1", "cwd": du_an, "tool_name": "Write",
                                  "tool_input": {"file_path": "x.md", "content": "NOI-DUNG-BI-MAT"}}))
    noi = "".join(open(os.path.join(log_dir, f), encoding="utf-8").read() for f in os.listdir(log_dir))
    kiem('"cong_cu": "Write"' in noi, "ghi được thao tác trong dự án")
    kiem("NOI-DUNG-BI-MAT" not in noi, "không ghi nội dung tệp vào log")
    chay([NK, "ghi"], json.dumps({"cwd": khac, "tool_name": "Write", "tool_input": {"file_path": "a"}}))
    kiem(not os.listdir(khac), "ca ngược: ngoài dự án không tạo log")
    r = chay([NK, "ghi"], "khong-phai-json")
    kiem(r.returncode == 0, "ca ngược: stdin hỏng vẫn thoát 0")
    r = chay([NK, "nap"], json.dumps({"cwd": du_an}))
    kiem("x.md" in r.stdout, "nạp context liệt kê tệp đã sửa")
    # CP-20260924-001 (C): "#riêng" -> khong ghi noi dung; loi nhan thuong van ghi
    chay([NK, "yeu-cau"], json.dumps({"session_id": "s1", "cwd": du_an,
                                      "prompt": "#riêng Diem KPI cua ong X la 87, xep loai sai"}))
    chay([NK, "yeu-cau"], json.dumps({"session_id": "s1", "cwd": du_an, "prompt": "#rieng DIEM-RIENG-2"}))
    chay([NK, "yeu-cau"], json.dumps({"session_id": "s1", "cwd": du_an,
                                      "prompt": "lap ke hoach thang 10 #riêng o giua"}))
    noi = "".join(open(os.path.join(log_dir, f), encoding="utf-8").read() for f in os.listdir(log_dir))
    kiem("87" not in noi and "DIEM-RIENG-2" not in noi, "#riêng/#rieng: không ghi nội dung lời nhắn")
    kiem(noi.count("[#riêng — không ghi]") == 2, "#riêng: vẫn ghi mốc thời gian, không tín hiệu học")
    # 1.3.0 (tham dinh lan 2, R2-02): MAC DINH chi ghi mo ta; noi dung chi khi nguoi dung chu dong chon
    kiem("lap ke hoach thang 10" not in noi, "1.3.0: lời nhắn thường KHÔNG ghi nội dung (mặc định)")
    kiem('"do_dai"' in noi, "1.3.0: lời nhắn thường vẫn ghi độ dài (thông tin mô tả)")
    chay([NK, "yeu-cau"], json.dumps({"session_id": "s1", "cwd": du_an,
                                      "prompt": "sửa lại Diem KPI Nguyen A la 90 CANH-BAO-TT"}))
    noi = "".join(open(os.path.join(log_dir, f), encoding="utf-8").read() for f in os.listdir(log_dir))
    kiem("CANH-BAO-TT" not in noi and "sua-sai" in noi,
         "1.3.0: có tín hiệu học vẫn KHÔNG ghi nội dung, chỉ ghi nhãn tín hiệu")
    chay([NK, "yeu-cau"], json.dumps({"session_id": "s1", "cwd": du_an, "prompt": "#học từ nay dùng mã P-THHC HOC-1"}))
    noi = "".join(open(os.path.join(log_dir, f), encoding="utf-8").read() for f in os.listdir(log_dir))
    kiem("HOC-1" in noi and '"chon_ghi": "#học"' in noi and "#học từ nay" not in noi,
         "ca ngược: mở đầu #học -> ghi nội dung (bỏ nhãn #học)")
    env_bat = {**{k: v for k, v in os.environ.items() if k != "CLAUDE_PROJECT_DIR"}, "KTC_NHAT_KY_NOI_DUNG": "1"}

    def chay_bat(prompt):
        subprocess.run([sys.executable, NK, "yeu-cau"], input=json.dumps(
            {"session_id": "s1", "cwd": du_an, "prompt": prompt}), capture_output=True, text=True,
            encoding="utf-8", cwd=GOC, env=env_bat)
    chay_bat("từ nay luôn ghi mã đơn vị chuẩn ENV-2 trong bảng")
    chay_bat("mở giúp anh tệp kế hoạch tháng mười ENV-3")
    chay_bat("sửa lại giúp anh, số 0912345678, CCCD " + "0520930" + "01234" + ", mail a.b@ktc.edu.vn ENV-4")
    noi = "".join(open(os.path.join(log_dir, f), encoding="utf-8").read() for f in os.listdir(log_dir))
    kiem("ENV-2" in noi, "chọn ghi (biến môi trường) + có tín hiệu học -> ghi nội dung")
    kiem("ENV-3" not in noi, "ca ngược: chọn ghi nhưng KHÔNG có tín hiệu học -> không ghi nội dung")
    kiem("ENV-4" in noi and "0912345678" not in noi and ("0520930" + "01234") not in noi and "a.b@ktc" not in noi
         and "[SỐ ĐIỆN THOẠI]" in noi and "[SỐ ĐỊNH DANH]" in noi and "[EMAIL]" in noi,
         "nội dung được ghi đã che số điện thoại, số định danh, email")
    # Bo gan tin hieu bot bao gia (TT-20260924-08)
    chay_bat("ok chốt nhé")
    chay_bat("Căn cứ Quyết định số 1899/QĐ-CĐKT ngày 5/9 lập bảng ENV-5")
    noi = "".join(open(os.path.join(log_dir, f), encoding="utf-8").read() for f in os.listdir(log_dir))
    kiem("ENV-5" not in noi, "số hiệu văn bản \"Quyết định số …\" không bị tính là tín hiệu quyết định")
    dong_cuoi = [json.loads(x) for f in os.listdir(log_dir) for x in open(os.path.join(log_dir, f), encoding="utf-8")]
    kiem(not any(d.get("do_dai") == len("ok chốt nhé") and d.get("tin_hieu") for d in dong_cuoi),
         "lời dưới 5 từ (\"ok chốt nhé\") không gắn tín hiệu")
    # luu giu 30 ngay: tep cu bi xoa khi nap, tep moi giu lai
    open(os.path.join(log_dir, "2020-01-01.jsonl"), "w").write("{}\n")
    chay([NK, "nap"], json.dumps({"cwd": du_an}))
    kiem(not os.path.exists(os.path.join(log_dir, "2020-01-01.jsonl")), "1.3.0: nhật ký cũ hơn 30 ngày bị xóa khi mở phiên")
    kiem(len(os.listdir(log_dir)) >= 1, "ca ngược: nhật ký hôm nay không bị xóa")

    print("== ktc_backup_github.py ==")
    repo = os.path.join(t, "repo"); remote = os.path.join(t, "remote.git")
    git("init", "-q", repo); os.makedirs(os.path.join(repo, "90-Nhat-Ky-Van-Hanh"))
    git("-C", repo, "config", "user.email", "t@t"); git("-C", repo, "config", "user.name", "t")
    open(os.path.join(repo, "a.md"), "w").write("a")
    r = chay([BK, "--du-an", repo])
    kiem(r.returncode == 0 and "Chưa có remote" in r.stdout, "chưa có remote: bỏ qua, thoát 0")
    git("init", "-q", "--bare", remote); git("-C", repo, "remote", "add", "origin", remote)
    r = chay([BK, "--du-an", repo])
    kiem(r.returncode == 0 and "Backup xong" in r.stdout, "có remote: commit + push thành công")
    r = chay([BK, "--du-an", repo, "--neu-can"])
    kiem(r.stdout.strip() == "", "--neu-can trong 24h: không chạy lại")
    open(os.path.join(repo, "my-credentials.json"), "w").write("x")
    r = chay([BK, "--du-an", repo])
    so_commit = subprocess.run(["git", "-C", remote, "rev-list", "--count", "HEAD"],
                               capture_output=True, text=True).stdout.strip()
    kiem(r.returncode == 1 and "DỪNG" in r.stdout and so_commit == "1",
         "ca ngược: tệp tên giống bí mật -> dừng, không push")
    kiem(os.path.exists(os.path.join(repo, "my-credentials.json")), "không xóa tệp của người dùng khi dừng")
    os.remove(os.path.join(repo, "my-credentials.json"))
    # 1.3.0: quet NOI DUNG — tep ten binh thuong nhung chua so dinh danh ca nhan -> dung
    open(os.path.join(repo, "ghi-chu.md"), "w").write("CCCD " + "0520930" + "01234, cua vien chuc")
    r = chay([BK, "--du-an", repo])
    so_commit = subprocess.run(["git", "-C", remote, "rev-list", "--count", "HEAD"],
                               capture_output=True, text=True).stdout.strip()
    kiem(r.returncode == 1 and "định danh" in r.stdout and so_commit == "1",
         "1.3.0: tệp tên thường chứa số định danh -> dừng, không push")
    os.remove(os.path.join(repo, "ghi-chu.md"))
    open(os.path.join(repo, "my-credentials.json"), "w").write("x")

    # --- pythonw: Task Scheduler chay bang pythonw.exe, KHONG co std handle hop le ---
    # Loi that 18-20/9/2026: tien trinh con thua ke stdin hong -> Git Credential Manager khong
    # trao doi duoc thong tin dang nhap -> `git push` that bai va KHONG in ra loi nao. Backup
    # 21:00 hong LANG LE hai ngay, trong khi chay tay luc nao cung duoc.
    #
    # Ca (a) la kiem TINH: remote cuc bo trong bo thu nay khong dung credential helper nen
    # khong tai hien duoc loi that. Doc thang nguon de it nhat chan viec go co stdin ra.
    nguon_bk = open(BK, encoding="utf-8").read()
    kiem("stdin=subprocess.DEVNULL" in nguon_bk,
         "git() truyền stdin=DEVNULL (bắt buộc cho pythonw/Task Scheduler)")

    # --- Ca nguoc: chay tren kho KHONG PHAI KTC-Quan-tri thi khong duoc de lai thu muc la ---
    # repo trong bo thu nay khong co 90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong (chi co thu muc cha),
    # nen nhat ky phai roi vao .git/, va tuyet doi khong sinh 04-Nhat-Ky-Tu-Dong/.
    kiem(not os.path.isdir(os.path.join(repo, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")),
         "ca ngược: không tạo thư mục 04-Nhat-Ky-Tu-Dong trong kho khác")
    kiem(os.path.isfile(os.path.join(repo, ".git", "ktc-backup-log.jsonl")),
         "kho khác: nhật ký backup rơi vào .git/ (không bị theo dõi)")

    # --- Chot bao ve theo che do goi ---
    # Hook SessionStart chay trong BAT KY du an nao nguoi dung mo. Neu khong chi dinh ro
    # --du-an thi chi duoc backup du an mang hinh dang KTC-Quan-tri; khong duoc tu y day
    # kho cua nguoi khac len remote cua ho. Con khi Task Scheduler chi dinh ro --du-an thi
    # day la y dinh tuong minh cua nguoi van hanh -> chi can la kho git.
    r3 = subprocess.run([sys.executable, BK, "--neu-can"], cwd=repo, capture_output=True,
                        text=True, timeout=120, stdin=subprocess.DEVNULL)
    kiem(r3.returncode == 0 and r3.stdout.strip() == "",
         "ca ngược: không chỉ định --du-an, kho thiếu 90-Nhat-Ky-Van-Hanh -> im lặng, không đẩy")
    repo2 = os.path.join(t, "repo2"); remote2 = os.path.join(t, "remote2.git")
    git("init", "-q", repo2); git("init", "-q", "--bare", remote2)
    git("-C", repo2, "config", "user.email", "t@t"); git("-C", repo2, "config", "user.name", "t")
    git("-C", repo2, "remote", "add", "origin", remote2)
    open(os.path.join(repo2, "c.md"), "w").write("c")
    r4 = subprocess.run([sys.executable, BK, "--du-an", repo2], capture_output=True,
                        text=True, timeout=180, stdin=subprocess.DEVNULL)
    kiem(r4.returncode == 0 and "Backup xong" in r4.stdout,
         "chỉ định rõ --du-an: backup được kho không phải KTC-Quan-tri")
    r5 = subprocess.run([sys.executable, BK, "--du-an", os.path.join(t, "khong-phai-git")],
                        capture_output=True, text=True, timeout=60, stdin=subprocess.DEVNULL)
    kiem(r5.returncode == 1 and "Không phải kho git" in r5.stdout,
         "ca ngược: chỉ định thư mục không phải kho git -> báo lỗi, thoát 1")

    # Ca (b) la kiem DONG: script phai chay tron ven duoi pythonw, khong vang loi nao.
    pythonw = os.path.join(os.path.dirname(sys.executable), "pythonw.exe")
    if os.path.isfile(pythonw):
        open(os.path.join(repo, "b.md"), "w").write("b")
        os.remove(os.path.join(repo, "my-credentials.json"))
        r2 = subprocess.run([pythonw, BK, "--du-an", repo], capture_output=True,
                            text=True, timeout=180, stdin=subprocess.DEVNULL)
        so_commit2 = subprocess.run(["git", "-C", remote, "rev-list", "--count", "HEAD"],
                                    capture_output=True, text=True).stdout.strip()
        kiem(r2.returncode == 0 and so_commit2 == "2",
             f"chạy dưới pythonw.exe: push thành công (mã {r2.returncode}, {so_commit2} commit)")
    else:
        print("  -- bỏ qua ca pythonw: không tìm thấy pythonw.exe")

kiem(anh_log_that() == truoc, "ca ngược: kiểm thử không ghi gì vào nhật ký THẬT của dự án")
# CP-20260924-001 (A): nhat ky that cua du an khong duoc git theo doi (loi nguoi dung -> GitHub)
r = subprocess.run(["git", "-C", GOC, "check-ignore", "-q",
                    "90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/2026-01-01.jsonl"])
kiem(r.returncode == 0, "nhật ký tự động nằm trong .gitignore")
r = subprocess.run(["git", "-C", GOC, "ls-files", "90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong"],
                   capture_output=True, text=True)
kiem(not r.stdout.strip(), "không còn tệp nhật ký tự động nào được git theo dõi")

print("KET LUAN:", "CO LOI " + str(loi) if loi else "SACH")
sys.exit(1 if loi else 0)
