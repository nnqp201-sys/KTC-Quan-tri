# -*- coding: utf-8 -*-
"""Hoi quy vong tu hoc — DL-20260919-005: hook ghi loi nguoi dung + tin hieu, nap TRI-THUC.md + dem tin hieu chua hoc.

Du an gia trong thu muc tam; ca thu nguoc; kiem khong ghi nham vao log THAT.
"""
import io
import json
import os
import subprocess
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
NK = os.path.join(GOC, "29-Cong-Cu", "plugin_src", "scripts", "ktc_nhat_ky.py")
THAT = os.path.join(GOC, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
sai = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


def chay(che_do, data):
    e = dict(os.environ)
    e.pop("KTC_NHAT_KY_NOI_DUNG", None)  # ca mac dinh 1.3.0: khong chon ghi noi dung
    e.pop("CLAUDE_PROJECT_DIR", None)
    return subprocess.run([sys.executable, NK, che_do], input=json.dumps(data, ensure_ascii=False),
                          capture_output=True, text=True, encoding="utf-8", env=e, cwd=GOC)


anh = {f: os.path.getsize(os.path.join(THAT, f)) for f in os.listdir(THAT)} if os.path.isdir(THAT) else {}
DA = tempfile.mkdtemp(prefix="ktc_hoc_")
os.makedirs(os.path.join(DA, "90-Nhat-Ky-Van-Hanh", "05-Tri-Thuc-Tu-Hoc"))
LOG = os.path.join(DA, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")


def dong_log():
    kq = []
    if os.path.isdir(LOG):
        for f in os.listdir(LOG):
            kq += [json.loads(x) for x in io.open(os.path.join(LOG, f), encoding="utf-8")]
    return [d for d in kq if d.get("loai") == "yeu-cau"]


chay("yeu-cau", {"cwd": DA, "session_id": "abc12345",
                 "prompt": "Lưu ý: từ nay văn bản hành chính viện dẫn Luật không ghi số hiệu"})
chay("yeu-cau", {"cwd": DA, "prompt": "Báo cáo này sai số liệu Trục 3, sửa lại giúp anh"})
chay("yeu-cau", {"cwd": DA, "prompt": "Mở tệp kế hoạch tháng 9"})
chay("yeu-cau", {"cwd": DA, "prompt": "/compact"})
chay("yeu-cau", {"cwd": DA, "prompt": "<command-name>/compact</command-name>"})
chay("yeu-cau", {"cwd": DA, "prompt": "#học " + "x" * 2000})
d = dong_log()
kiem(len(d) == 4, f"ghi 4 lời người dùng, bỏ lệnh nội bộ /compact và <command…> (được {len(d)})")
kiem("quy-uoc" in d[0].get("tin_hieu", []), "“từ nay… lưu ý” → tín hiệu quy-uoc")
kiem("sua-sai" in d[1].get("tin_hieu", []), "“sai… sửa lại” → tín hiệu sua-sai")
kiem("tin_hieu" not in d[2], "lời thường không gắn tín hiệu (thử ngược)")
kiem("noi_dung" not in d[0] and "noi_dung" not in d[1],
     "1.3.0: mặc định không ghi nội dung, kể cả khi có tín hiệu học (R2-02)")
kiem(len(d[3]["noi_dung"]) <= 601, "#học + lời dài: ghi nội dung, cắt ≤ 600 ký tự")

ngoai = tempfile.mkdtemp(prefix="ktc_ngoai_")
chay("yeu-cau", {"cwd": ngoai, "prompt": "từ nay luôn làm vậy"})
kiem(not os.path.exists(os.path.join(ngoai, "90-Nhat-Ky-Van-Hanh")), "ngoài dự án KTC: không ghi")

TT = os.path.join(DA, "90-Nhat-Ky-Van-Hanh", "05-Tri-Thuc-Tu-Hoc", "TRI-THUC.md")
io.open(TT, "w", encoding="utf-8").write(
    "| Mã | Loại | Điều đã học | Bằng chứng | Phạm vi | Trạng thái | Chuyển |\n|---|---|---|---|---|---|---|\n"
    "| TT-20260919-01 | quy ước | VBHC không ghi số hiệu Luật | lời người dùng | viện dẫn | hiệu lực | — |\n"
    "| TT-20260919-02 | kỹ thuật | Tránh heredoc với dấu gạch chéo ngược | log | Code | chờ duyệt | — |\n"
    "| TT-20260919-03 | quy ước | Điều cũ đã bỏ | lời người dùng | x | bị bác | — |\n"
    "| TT-20260919-04 | quy ước | Điều cũ bị thay | x | x | đã thay (TT-20260919-01) | — |\n")
out = chay("nap", {"cwd": DA}).stdout
kiem("TT-20260919-01" in out and "TT-20260919-02" in out, "nạp mục hiệu lực và chờ duyệt vào context")
kiem("TT-20260919-03" not in out and "TT-20260919-04" not in out, "không nạp mục bị bác/đã thay (thử ngược)")
kiem("⟳ 2 tín hiệu" in out, "đếm đúng 2 tín hiệu học chưa xử lý và nhắc gọi ktc-tu-hoc")
io.open(os.path.join(DA, "90-Nhat-Ky-Van-Hanh", "05-Tri-Thuc-Tu-Hoc", ".lan-hoc-cuoi"), "w").write("9999-12-31T00:00:00")
kiem("⟳" not in chay("nap", {"cwd": DA}).stdout, "sau lượt học (mốc mới) không còn nhắc")

sau = {f: os.path.getsize(os.path.join(THAT, f)) for f in os.listdir(THAT)} if os.path.isdir(THAT) else {}
moi = {f for f in sau if sau[f] != anh.get(f)}
# Phien that van dang chay nen log hom nay co the tang do chinh hook; chi bao loi neu co dong "yeu-cau" gia
gia = []
for f in moi:
    for x in io.open(os.path.join(THAT, f), encoding="utf-8", errors="ignore"):
        if "Báo cáo này sai số liệu Trục 3" in x or "x" * 50 in x:
            gia.append(f)
kiem(not gia, "không ghi nhầm lời thử vào nhật ký THẬT")

print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
