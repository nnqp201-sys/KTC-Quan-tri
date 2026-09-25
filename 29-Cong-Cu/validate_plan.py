# -*- coding: utf-8 -*-
"""Kiem ke hoach KPI ca nhan (tep .xlsx dung 1 trong 6 mau Quy) — skill ktc-kpi-lap-ke-hoach.

Moi loi co: ma, muc (LOI = phai sua truoc khi trinh Truong don vi phe duyet; CANH_BAO = can xem), vi tri, can cu.
KHONG sua tep. KHONG ket luan thay Truong don vi (phe duyet — QD 1923 D13.1).

  KH01 LOI       Dau viec thieu san pham dau ra                          QD 1923 D12.4
  KH02 LOI       Dau viec thieu thoi han hoan thanh                      QD 1923 D12.4
  KH03 LOI       So luong trong / khong phai so > 0 (khong do luong duoc) QD 1923 D12.4
  KH04 LOI       Thieu muc do / he so quy doi                            QD 1923 PL II
  KH05 LOI       He so khong khop muc do (chi khi phuong an muc-do)      QD 1923 PL II
  KH06 LOI       Dong vi du cua mau chua xoa                             Known-Issues-Bieu-Mau #4
  KH07 CANH_BAO  Thieu nguon minh chung                                  QD 1923 D12.4
  KH08 LOI       San pham khong co trong Danh muc TB 1052 (phuong an A/AxB) Cau hoi mo so 2
  KH09 CANH_BAO  Dau hieu quy ket qua tap the thanh KPI ca nhan          QD 1923 D4.8
  KH10 LOI       Vien chuc quan ly khong co dau viec Truc (4)            QD 1923 D12.1
  KH11 CANH_BAO  Truc co diem toi da nhung khong co dau viec             mau Danh gia: diem Truc = 0
  KH12 LOI       Cau truc diem cua mau sai (70 diem, truc chinh >= 40%, nhom chung) QD 1923 D10.4, D11.3, D12.3
  KH13 CANH_BAO  O so Quyet dinh trong tieu de sheet KPI con trong       Known-Issues-Bieu-Mau #5
  KH14 CANH_BAO  Dau viec trung lap noi dung                              QD 1923 D11.4a
  KH15 LOI       Chua dien ho ten / don vi                                mau Ke hoach
  KH16 CANH_BAO  Sheet KPI con so thuc te VI DU cua mau (L=4,N=100,P=100) Known-Issues-Bieu-Mau #12

Chay:  python 29-Cong-Cu/validate_plan.py <ke_hoach.xlsx> [--nhom hanh-chinh] [--phuong-an muc-do] [--json]
Ma thoat: 1 neu co LOI, 0 neu chi canh bao hoac sach.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kpi_calc as kc  # noqa: E402
import kpi_mau as km   # noqa: E402

TAP_THE = ("toàn trường", "toàn khoa", "toàn phòng", "toàn đơn vị", "100% viên chức", "tất cả viên chức",
           "kết quả chung của", "tập thể đơn vị")


def kiem(p, nhom=None, phuong_an=None):
    wb = km.mo(p)
    ct = km.cau_truc(wb)
    nhom = nhom or km.nhan_nhom(wb)
    ws, kp = wb["Ke Hoach"], wb["KPI"]
    ds = []

    def them(ma, muc, vt, nd, cc):
        ds.append({"ma": ma, "muc": muc, "vi_tri": vt, "noi_dung": nd, "can_cu": cc})

    # Cau truc diem cua mau
    for ma, nd, cc in (kc.kiem_trong_so_truc(ct["diem_truc"], max(ct["diem_truc"], key=ct["diem_truc"].get))
                       + kc.kiem_tieu_chi_chung(ct["nhom_a"])):
        them("KH12", "LOI", "Danh gia", f"{ma}: {nd}", cc)
    # Thong tin ca nhan
    for r, ten in ((4, "Họ và tên"), (8, "Đơn vị công tác")):
        v = str(ws[f"B{r}"].value or "")
        if not re.search(r":\s*[^\s….]", v.split("Ngày sinh")[0]):
            them("KH15", "LOI", f"Ke Hoach!B{r}", f"Chưa điền {ten}", "mẫu Kế hoạch")
    vi_du = km.dong_vi_du(nhom) if nhom else {}
    thay_noi_dung, co_truc = {}, {n: 0 for n in ct["truc"]}
    for n, (d, c) in ct["truc"].items():
        for r in range(d, c + 1):
            o = {col: ws[f"{col}{r}"].value for col in "BCDEFGHIJ"}
            if not any(v not in (None, "") for v in o.values()):
                continue
            vt = f"Ke Hoach!dòng {r} (Trục {n})"
            nd = str(o["B"] or "").strip()
            for col, v in o.items():
                if vi_du.get(f"{col}{r}") is not None and v == vi_du[f"{col}{r}"]:
                    them("KH06", "LOI", vt, f"Dòng ví dụ của mẫu chưa xóa: '{str(v)[:60]}'",
                         "Known-Issues-Bieu-Mau #4")
                    break
            if not nd:
                them("KH01", "LOI", vt, "Có số liệu nhưng thiếu nội dung nhiệm vụ", "QĐ 1923, Đ12.4")
                continue
            co_truc[n] += 1
            if nd.lower() in thay_noi_dung:
                them("KH14", "CANH_BAO", vt, f"Trùng nội dung với {thay_noi_dung[nd.lower()]}", "QĐ 1923, Đ11.4a")
            thay_noi_dung.setdefault(nd.lower(), vt)
            if not str(o["E"] or "").strip():
                them("KH01", "LOI", vt, f"'{nd[:50]}': thiếu sản phẩm đầu ra", "QĐ 1923, Đ12.4")
            if o["G"] in (None, ""):
                them("KH02", "LOI", vt, f"'{nd[:50]}': thiếu thời hạn hoàn thành", "QĐ 1923, Đ12.4")
            try:
                ok = float(o["F"]) > 0
            except (TypeError, ValueError):
                ok = False
            if not ok:
                them("KH03", "LOI", vt, f"'{nd[:50]}': số lượng '{o['F']}' không đo lường được", "QĐ 1923, Đ12.4")
            if o["D"] in (None, "") or o["I"] in (None, ""):
                them("KH04", "LOI", vt, f"'{nd[:50]}': thiếu mức độ hoặc hệ số quy đổi", "QĐ 1923, Phụ lục II")
            elif phuong_an == "muc-do":
                k = kc.muc_do_tu_chu(o["D"])
                if k is None:
                    them("KH04", "LOI", vt, f"Mức độ '{o['D']}' không thuộc 4 mức", "QĐ 1923, Phụ lục II")
                elif abs(float(o["I"]) - kc.MUC_DO[k]) > 1e-9:
                    them("KH05", "LOI", vt, f"Hệ số {o['I']} ≠ {kc.MUC_DO[k]} của mức '{o['D']}'",
                         "QĐ 1923, Phụ lục II")
            if phuong_an in ("A", "AxB"):
                try:
                    kc.tra_A(o["E"])
                except kc.LoiKPI as e:
                    them("KH08", "LOI", vt, str(e), "Câu hỏi mở số 2")
            mc = kp[f"{ct['cot_minh_chung']}{ct['kpi_dong'][r]}"].value if ct["cot_minh_chung"] else None
            if not mc and "minh chứng" not in str(o["J"] or "").lower():
                them("KH07", "CANH_BAO", vt, f"'{nd[:50]}': chưa ghi nguồn minh chứng", "QĐ 1923, Đ12.4")
            if any(k in nd.lower() for k in TAP_THE):
                them("KH09", "CANH_BAO", vt, f"'{nd[:60]}' có dấu hiệu là kết quả tập thể — ghi rõ phần "
                     "cá nhân trực tiếp phụ trách", "QĐ 1923, Đ4.8")
    if nhom and km.NHOM[nhom][2] and not co_truc.get(4):
        them("KH10", "LOI", "Ke Hoach (Trục 4)", "Viên chức quản lý không có đầu việc Trục (4) — không được miễn "
             "trừ, kể cả người ngoài Đảng", "QĐ 1923, Đ12.1")
    for n, sl in co_truc.items():
        if not sl and ct["diem_truc"].get(n):
            them("KH11", "CANH_BAO", f"Ke Hoach (Trục {n})", f"Trục {n} có {ct['diem_truc'][n]:g} điểm tối đa "
                 "nhưng không có đầu việc — Trục này sẽ tính 0 điểm", "mẫu Đánh giá (Điểm KPI = 0 khi trống)")
    # KH16: mau Quy III de san SO THUC TE vi du o dong viec dau sheet KPI (L=4, N=100, P=100). Con sot thi % Truc
    # sai khi mo bang Excel. Chi bat khi TRUNG DUNG so vi du cua mau o cung o — ke hoach Quy III lap cung luc voi
    # danh gia (CV 694) nen co so thuc te that la binh thuong, khong bat.
    vd_kpi = km.thuc_te_vi_du(nhom) if nhom else {}
    for o_, v in vd_kpi.items():
        hang = {k: val for k, val in v.items()}
        if all(kp[k].value == val for k, val in hang.items()):
            them("KH16", "CANH_BAO", f"KPI!{o_}", "Số thực tế trùng đúng số ví dụ của mẫu (" +
                 ", ".join(f"{k}={val}" for k, val in hang.items()) + ") — xác nhận là số thật, nếu không thì xóa",
                 "Known-Issues-Bieu-Mau #12")
    if re.search(r"Quyết định số:\s*/", str(kp["A1"].value or "")):
        them("KH13", "CANH_BAO", "KPI!A1", "Ô số Quyết định trong tiêu đề còn trống", "Known-Issues-Bieu-Mau #5")
    return {"tep": os.path.basename(p), "nhom": nhom, "phuong_an": phuong_an,
            "so_dau_viec": sum(co_truc.values()), "loi": ds}


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("tep")
    ap.add_argument("--nhom", choices=list(km.NHOM))
    ap.add_argument("--phuong-an", choices=list(kc.PHUONG_AN))
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    kq = kiem(a.tep, a.nhom, a.phuong_an)
    if a.json:
        print(json.dumps(kq, ensure_ascii=False, indent=1))
    else:
        print(f"=== {kq['tep']} — nhóm {kq['nhom'] or '?'} — {kq['so_dau_viec']} đầu việc ===")
        for x in sorted(kq["loi"], key=lambda x: (x["muc"] != "LOI", x["ma"])):
            print(f"  [{x['muc']:8s}] {x['ma']} {x['vi_tri']}: {x['noi_dung']}  [{x['can_cu']}]")
        if not kq["loi"]:
            print("  ✓ Không phát hiện lỗi")
    return 1 if any(x["muc"] == "LOI" for x in kq["loi"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
