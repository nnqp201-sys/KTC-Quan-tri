# -*- coding: utf-8 -*-
"""Hoi quy doi_soat_so_lieu.py — DL-20260919-006. Du lieu gia (thay ham doc), khong phu thuoc tep that.

Ca thu nguoc lay tu loi that khi chay tren 10-Dau-Vao/01-Dau-Moi-Nop/2026-09 (19/9/2026):
- so cheo KH thang 9 voi KQ thang 8 (khac ky)
- % KPI 300-850% do tron hai thang (KI-014) — phai danh dau, khong in so
- so tong hop cap Truong voi TONG don vi (sai phep: tong hop chi lay nhiem vu dua len Truong)
- noi dung chung chung ghep nham don vi khac
- tep thuyet minh .docx bi coi la loi
"""
import os
import sys
import tempfile

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(GOC, "29-Cong-Cu"))
import doi_soat_so_lieu as ds  # noqa: E402

sai = []


def kiem(dk, ten):
    print(("  OK " if dk else "  X  ") + ten)
    if not dk:
        sai.append(ten)


def nv(nd, sl=1.0, kpi=1.0, tid=None):
    return {"noi_dung": nd, "so_luong_quy_doi": sl, "kpi_so_luong_qd": kpi, "kpi_chat_luong_qd": kpi,
            "kpi_tien_do_qd": kpi, "task_id": tid}


DU_LIEU = {}


def gia_doc(p):
    return DU_LIEU[os.path.basename(os.path.dirname(p)) + "/" + os.path.basename(p)]


ds.doc = gia_doc
T = tempfile.mkdtemp(prefix="ktc_ds_")


def tao(ma, ten, kind, truc, canh_bao=()):
    os.makedirs(os.path.join(T, ma), exist_ok=True)
    p = os.path.join(T, ma, ten)
    open(p, "wb").write(b"x")
    DU_LIEU[ma + "/" + ten] = {"kind": kind, "truc": truc, "truc_tong": {}, "canh_bao": list(canh_bao)}
    return p


tao("K-KTCN", "BC-KQ-thang-8-2026.xlsx", "KQ", {1: [
    nv("Xây dựng kế hoạch đào tạo năm học 2026-2027 của Khoa", 1.2, 1.2, "KTC-2026-Q3-00001"),
    nv("Tổ chức nhập học tân sinh viên cao đẳng khóa mới", 1.0, 1.0)]})
tao("K-KTCN", "KH-thang-8-2026.xlsx", "KH", {1: [
    nv("Xây dựng kế hoạch đào tạo năm học 2026-2027 của Khoa", tid="KTC-2026-Q3-00001"),
    nv("Rà soát chuẩn đầu ra các ngành nghề trình độ cao đẳng")]})
tao("K-KTCN", "KH-thang-9-2026.xlsx", "KH", {1: [nv("Việc hoàn toàn mới của tháng chín chưa báo cáo")]})
tao("K-KTCN", "BC-KQ-thang-8-2026.docx", None, {})           # thuyet minh kem .xlsx: binh thuong
tao("K-SUPH", "BC-KQ-thang-8-2026.xlsx", "KQ", {2: [
    nv("Phân công giảng dạy các học phần, môn học thuộc bộ môn", 12.0, 12.0, "KTC-2026-Q3-00001")]})
tao("K-KHCB", "BC-KQ-thang-8-2026.xlsx", "KQ", {2: [
    nv("Phân công giảng dạy các học phần, môn học thuộc bộ môn", 6.0, 6.0)]})
tao("P-TCKT", "BC-KQ-thang-8-2026.docx", None, {})            # chi co .docx: thieu Excel
tao("DT-CDCS", "BC-KQ-thang-8-2026.xlsx", "KQ", {5: [nv("Tổ chức Tết Trung thu cho con viên chức", 1.2, 120.0)]})

th = tao("TONG", "PL-tong-hop-thang-8-2026.xlsx", "KQ", {
    1: [nv("Xây dựng kế hoạch đào tạo năm học 2026-2027 của Khoa", 1.2, 1.2),     # khop
        nv("Tổ chức nhập học tân sinh viên cao đẳng khóa mới", 3.0, 3.0),           # 1 nguon, lech
        nv("…"),                                                                    # khong noi dung
        nv("Nhiệm vụ không hề có ở đơn vị nào trong kỳ báo cáo này")],              # khong nguon
    2: [nv("Phân công giảng dạy các học phần, môn học thuộc bộ môn", 6.0, 6.0),     # nhieu nguon, 1 khop
        nv("Phân công giảng dạy các học phần, môn học thuộc bộ môn", 9.0, 9.0)]})   # nhieu nguon, khong khop
DU_LIEU["TONG/PL-tong-hop-thang-8-2026.xlsx"] = DU_LIEU.pop("TONG/PL-tong-hop-thang-8-2026.xlsx")

don_vi = [os.path.join(T, m) for m in ("K-KTCN", "K-SUPH", "K-KHCB", "P-TCKT", "DT-CDCS")]
tat = ds.gom_tep(don_vi)
o = ds.doi_soat([p for p in tat if ds.loai_tep(p) != "KH"], [p for p in tat if ds.loai_tep(p) == "KH"], th)

kiem(ds.ky_tep("KH-thang-9-2026.xlsx") == ("thang", 9, 2026) and ds.ky_tep("KH-quy-3-2026.xlsx") == ("quy", 3, 2026)
     and ds.ky_tep("BC-Tháng-8-2026.xlsx") == ("thang", 8, 2026), "nhận kỳ từ tên tệp (tháng/quý, có dấu)")
ds03 = [x for x in o["ds03"] if x[0] == "K-KTCN"]
kiem(any("Rà soát chuẩn đầu ra" in x[2] and x[1].startswith("KH chưa") for x in ds03),
     "DS03: nhiệm vụ KH tháng 8 chưa có kết quả tháng 8 bị bắt")
kiem(any("nhập học" in x[2] and "không có trong KH" in x[1] for x in ds03), "DS03: kết quả không có trong KH bị bắt")
kiem(not any("tháng chín" in x[2] for x in o["ds03"]), "DS03: KH tháng 9 KHÔNG bị so với KQ tháng 8 (khác kỳ)")

m02 = [x[2] for x in o["ds02"]]
nd02 = [x[1] for x in o["ds02"]]
kiem(not any("Xây dựng kế hoạch đào tạo" in x for x in nd02), "DS02: dòng tổng hợp khớp nguồn không bị báo")
kiem(any("nhập học" in x[1] and "khác nguồn" in x[2] for x in o["ds02"]), "DS02: một nguồn, lệch số liệu → báo lệch")
kiem(any("không ghi nội dung" in x for x in m02), "DS02: dòng “…” → không truy vết được")
kiem(any("không truy được về dòng nguồn" in x for x in m02), "DS02: dòng không có nguồn → Nguyên tắc bất biến 3")
pc = [x for x in o["ds02"] if "Phân công" in x[1]]
kiem(len(pc) == 1 and "cần Task_ID" in pc[0][2],
     "DS02: nội dung chung ở nhiều đơn vị — có nguồn cùng số thì khớp; không có thì đòi Task_ID, không kết luận lệch")

kiem(any(x[0] == "KTC-2026-Q3-00001" for x in o["ds04"]), "DS04: Task_ID trùng giữa K-KTCN và K-SUPH bị bắt")
kiem(o["ds05"][5]["lech_thang"] and o["ds05"][5]["pct_sl"] is None, "DS05: KPI 120 / SL 1,2 → đánh dấu lệch thang, không in %")
kiem(not o["ds05"][1]["lech_thang"] and o["ds05"][1]["pct_sl"] == 100.0, "DS05: Trục đúng thang tính % bình thường")
m06 = " | ".join(f"{a} {b} {c}" for a, b, c in o["ds06"])
kiem("DT-CDCS" in m06 and "chưa có trong" in m06, "DS06: mã đoàn thể DT-CDCS chưa có trong bảng mã bị báo")
kiem("P-TCKT" in m06 and "thiếu Phụ lục Excel" in m06, "DS06: đơn vị chỉ nộp .docx bị báo thiếu Excel")
kiem("K-KTCN BC-KQ-thang-8-2026.docx" not in m06, "DS06: .docx thuyết minh nộp kèm .xlsx KHÔNG bị báo")

print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
