# -*- coding: utf-8 -*-
"""Ca thu plugin 1.3.5 — ket noi THU MUC LAM VIEC cua don vi (ktc_thu_muc.py) va hook do the thuc ngoai du an.

Chay:  python 92-Kinh-Nghiem/02-Regression/Cases/test_thu_muc.py      (ma thoat 0 = sach)
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(DU_AN, "29-Cong-Cu", "plugin_src", "scripts")
sys.path.insert(0, SRC)
import ktc_thu_muc as tm  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
loi = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        loi.append(ten)


def bao_loi(f, *a, **k):
    try:
        f(*a, **k)
    except ValueError as e:
        return str(e)
    return None


tam = tempfile.mkdtemp(prefix="ktc_thu_muc_")
try:
    print("== A. Khởi tạo, nhận diện ==")
    dv = os.path.join(tam, "Phong TCCB")
    os.makedirs(dv)
    kiem(tm.tim_goc(dv)[0] == "khong", "thư mục chưa kết nối → chế độ 'khong'")
    goc, tao = tm.khoi_tao(dv, "p-tccb")
    kiem(all(os.path.isdir(os.path.join(dv, d)) for d in ("10-Dau-Vao", "30-Ket-Qua")), "tạo 10-Dau-Vao/, 30-Ket-Qua/")
    dd = json.load(io.open(os.path.join(dv, tm.DANH_DAU), encoding="utf-8"))
    kiem(dd["ma_don_vi"] == "P-TCCB", "tệp đánh dấu ghi mã chuẩn (chữ hoa) P-TCCB")
    kiem(os.path.isfile(os.path.join(dv, "00-HUONG-DAN.md")), "có 00-HUONG-DAN.md")
    con = os.path.join(dv, "30-Ket-Qua", "2026-10-01", "BC")
    os.makedirs(con)
    kiem(tm.tim_goc(con) == ("don-vi", os.path.abspath(dv), "P-TCCB"), "thư mục con nhận đúng gốc đơn vị (tìm lên cha)")
    hd = os.path.join(dv, "00-HUONG-DAN.md")
    io.open(hd, "w", encoding="utf-8").write("ban sua cua don vi")
    goc, tao = tm.khoi_tao(dv, "P-TCCB")
    kiem(tao == [] and io.open(hd, encoding="utf-8").read() == "ban sua cua don vi", "khởi tạo lại: không ghi đè tệp đã có")

    print("== B. Ca ngược — phải từ chối ==")
    kiem(bao_loi(tm.khoi_tao, dv, "P-QLDT") is not None, "NGƯỢC: thư mục đã của P-TCCB, khởi tạo mã khác → từ chối")
    kiem(bao_loi(tm.khoi_tao, os.path.join(tam, "x"), "P-TCCB") is not None, "NGƯỢC: thư mục không tồn tại → từ chối")
    k2 = os.path.join(tam, "k2"); os.makedirs(k2)
    kiem(bao_loi(tm.khoi_tao, k2, "PHONG-TCCB") is not None, "NGƯỢC: mã ngoài 11 mã chuẩn → từ chối, không đoán")
    kho = os.path.join(tam, "My Drive", "KTC-Database", "x"); os.makedirs(kho)
    kiem(bao_loi(tm.khoi_tao, kho, "P-TCCB") is not None, "NGƯỢC: trong KTC-Database → từ chối")
    kiem(not os.path.exists(os.path.join(kho, tm.DANH_DAU)), "NGƯỢC: không tạo tệp nào trong kho")
    kiem(bao_loi(tm.khoi_tao, os.path.join(DU_AN, "30-Ket-Qua"), "P-THHC") is not None, "NGƯỢC: trong dự án KTC-Quan-tri → từ chối")
    kiem(tm.tim_goc(os.path.join(DU_AN, "29-Cong-Cu"))[0] == "du-an", "dự án vẫn nhận là 'du-an' (ưu tiên)")
    kiem(bao_loi(tm.khoi_tao, con, "P-TCCB") is not None, "NGƯỢC: thư mục con của thư mục đã kết nối → từ chối (dùng gốc)")

    print("== C. CLI ==")
    r = subprocess.run([sys.executable, os.path.join(SRC, "ktc_thu_muc.py"), "kiem", con], capture_output=True, text=True,
                       encoding="utf-8")
    j = json.loads(r.stdout)
    kiem(j["che_do"] == "don-vi" and j["ma_don_vi"] == "P-TCCB" and j["ket_qua"].endswith("30-Ket-Qua"), "CLI kiem trả JSON đúng")
    r = subprocess.run([sys.executable, os.path.join(SRC, "ktc_thu_muc.py"), "khoi-tao", k2, "--ma", "XX"],
                       capture_output=True, text=True, encoding="utf-8")
    kiem(r.returncode == 2, "NGƯỢC: CLI khởi tạo mã sai → mã thoát 2")

    print("== D. Hook đo thể thức chạy trong thư mục đơn vị ==")
    import docx  # noqa: E402
    hook = os.path.join(DU_AN, "31-Plugin", "scripts", "ktc_the_thuc_hook.py")   # ban dung: co skills/the-thuc de do
    tep = os.path.join(con, "P-TCCB_BC-thang_2026-10_v1.docx")
    d = docx.Document()
    d.add_paragraph("Nội dung thử")
    d.save(tep)

    def chay_hook(cwd, fp):
        return subprocess.run([sys.executable, hook], input=json.dumps({"tool_name": "Write", "cwd": cwd,
                                                                         "tool_input": {"file_path": fp}}),
                              capture_output=True, text=True, encoding="utf-8", timeout=120)
    tt = os.path.join(os.path.expanduser("~"), ".claude", "ktc_the_thuc_da_do.json")
    try:
        du_lieu = json.load(io.open(tt, encoding="utf-8"))
        du_lieu.pop(os.path.abspath(tep), None)
        io.open(tt, "w", encoding="utf-8").write(json.dumps(du_lieu))
    except Exception:
        pass
    r = chay_hook(dv, tep)
    kiem(r.returncode == 2 and r.stderr.strip() != "", "tệp .docx lệch chuẩn trong thư mục đơn vị → hook đo, báo (mã 2)")
    ngoai = os.path.join(tam, "ngoai"); os.makedirs(ngoai)
    tep2 = os.path.join(ngoai, "a.docx"); d.save(tep2)
    r = chay_hook(ngoai, tep2)
    kiem(r.returncode == 0, "NGƯỢC: thư mục chưa kết nối → hook im lặng như trước (mã 0)")

    print("== E. Bản sao trong kỹ năng điều phối khớp nguồn ==")
    b = open(os.path.join(DU_AN, "22-KTC-Dieu-Phoi", "scripts", "ktc_thu_muc.py"), "rb").read()
    kiem(b == open(os.path.join(SRC, "ktc_thu_muc.py"), "rb").read(),
         "22-KTC-Dieu-Phoi/scripts/ktc_thu_muc.py trùng byte với 29-Cong-Cu/plugin_src/scripts/")
finally:
    shutil.rmtree(tam, ignore_errors=True)

print("\nKET LUAN:", "SACH" if not loi else f"{len(loi)} ca sai")
sys.exit(1 if loi else 0)
