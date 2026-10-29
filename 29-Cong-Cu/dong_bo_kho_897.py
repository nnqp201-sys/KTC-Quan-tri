# -*- coding: utf-8 -*-
"""Doi chieu Kho-Du-Lieu-897 (kho_manifest.json cua loi ktc-ra-soat-897 v4.5) voi KTC-Database.

CHI DOC. Khong sua goi skill, khong ghi vao KTC-Database. Lech -> in bang va ghi
30-Ket-Qua/<ngay>/dong-bo-kho-897/Bao-cao-lech.md; chi DE XUAT gui don vi quan ly Skill
(Phong QLKHCN&HTPT, noi luu TB 1206) — khong tu cap nhat kho trong loi (LENH B5).

Voi tung van ban trong manifest: tim tep trong KTC-Database theo so hieu (khop moi thanh phan
cua so hieu, khong dau), so ngay ban hanh va trang thai hieu luc theo metadata cua kho; voi van ban
het hieu luc va VBHN: kiem tra van ban thay the / VBHN khac trong kho.

Chay: python 29-Cong-Cu/dong_bo_kho_897.py [--kho <thu muc KTC-Database>] [--ngay yyyy-mm-dd]
Ma thoat 0 = chay xong (co the co lech; xem bao cao) · 2 = khong doc duoc kho / manifest.
"""
from __future__ import annotations

import datetime
import json
import os
import re
import sys
import unicodedata

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(DU_AN, "2A-KTC-Ra-Soat-897", "ktc-ra-soat-897", "references",
                        "Kho-Du-Lieu-897", "kho_manifest.json")
THU_MUC_QUET = ("01-Legal-Database", "02-KTC-Regulations")
DUOI_VAN_BAN = (".docx", ".doc", ".pdf", ".xlsx")


def bo_dau(s: str) -> str:
    s = s.replace("Đ", "D").replace("đ", "d")
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def tach(s: str) -> list[str]:
    return [t for t in re.split(r"[^0-9A-Za-z]+", bo_dau(s).upper()) if t]


def chuan_ngay(s: str) -> str | None:
    """Tra ve dd/mm/yyyy tu 'd/m/yyyy' hoac 'ngay d thang m nam yyyy'."""
    m = re.search(r"(\d{1,2})\s*/\s*(\d{1,2})\s*/\s*(\d{4})", s) or \
        re.search(r"(\d{1,2})\s*tháng\s*(\d{1,2})\s*năm\s*(\d{4})", s)
    return f"{int(m.group(1)):02d}/{int(m.group(2)):02d}/{m.group(3)}" if m else None


def lap_chi_muc(kho: str):
    """(tep van ban, tep metadata) duoi 01, 02 — duong dan tuyet doi."""
    vb, md = [], []
    for ten in THU_MUC_QUET:
        for r, ds, fs in os.walk(os.path.join(kho, ten)):
            for f in fs:
                p = os.path.join(r, f)
                low = f.lower()
                if low.endswith(".md") and "metadata" in low:
                    md.append(p)
                elif low.endswith(DUOI_VAN_BAN) and not f.startswith("~$"):
                    vb.append(p)
    return vb, md


def khop_so_hieu(so_hieu: str, ten_tep: str) -> bool:
    tk = tach(so_hieu)
    ts = set(tach(os.path.splitext(ten_tep)[0]))
    return bool(tk) and all(t in ts for t in tk)


def doc_metadata(p: str) -> dict:
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            txt = f.read(6000)
    except OSError:
        return {}
    kq = {}
    for nhan, khoa in (("Ngày ban hành", "ngay"), ("Hiệu lực", "hieu_luc")):
        m = re.search(r"(?:^\||^[-*\d.\s]*)\**\s*(?:\d+\s*\|\s*)?\**" + nhan + r"\**\s*[:|]\s*\|?\s*(.+)$", txt, re.M)
        if m:
            kq[khoa] = m.group(1).strip(" |*")
    return kq


def doi_chieu_van_ban(vb: dict, tep_vb, tep_md):
    so = vb["so_hieu"]
    if so.startswith("Phụ lục"):
        return "BO_QUA", "Phụ lục của văn bản khác, đối chiếu cùng văn bản mẹ", None, []
    tim = [p for p in tep_vb if khop_so_hieu(so, os.path.basename(p))]
    if not tim:
        return "KHONG_THAY", "không có tệp nào trong 01, 02 của KTC-Database khớp số hiệu", None, []
    md = [p for p in tep_md if khop_so_hieu(so, os.path.basename(p))]
    thongtin = {}
    for p in md:
        thongtin.update({k: v for k, v in doc_metadata(p).items() if k not in thongtin})
    ghi = []
    kq = "KHOP"
    nk = chuan_ngay(vb.get("ngay", ""))
    nm = chuan_ngay(thongtin.get("ngay", "")) if thongtin.get("ngay") else None
    if nm and nk and nm != nk:
        kq = "LECH"
        ghi.append(f"ngày ban hành: manifest {nk} ≠ metadata kho {nm}")
    elif not nm:
        ghi.append("metadata kho không có/không đọc được ngày ban hành")
    hl = thongtin.get("hieu_luc", "")
    low = bo_dau(hl).lower()
    manifest_hl = bo_dau(vb.get("hieu_luc", "")).lower()
    if hl:
        het = any(x in low for x in ("het hieu luc", "bi thay the", "da bi thay"))             and "dang co hieu luc" not in low
        if het and "dang co hieu luc" in manifest_hl:
            kq = "LECH"
            ghi.append(f"hiệu lực: manifest “{vb.get('hieu_luc','')[:40]}” ≠ kho “{hl[:80]}”")
        elif "can xac minh" in low:
            ghi.append("kho ghi hiệu lực “Cần xác minh”")
    else:
        ghi.append("metadata kho không có trường hiệu lực")
    if len(tim) > 1:
        ghi.append(f"{len(tim)} tệp cùng số hiệu trong kho")
        if kq == "KHOP":
            kq = "KHOP*"
    return kq, "; ".join(ghi) or "khớp", tim, md


def doi_chieu_het_hieu_luc(m: dict, tep_vb, tep_md):
    tim = [p for p in tep_vb if khop_so_hieu(m["so_hieu"], os.path.basename(p))]
    md = [p for p in tep_md if khop_so_hieu(m["so_hieu"], os.path.basename(p))]
    hl = ""
    for p in md:
        hl = doc_metadata(p).get("hieu_luc", hl)
    if not tim:
        return "KHONG_THAY", "văn bản hết hiệu lực không có trong 01, 02 (bình thường với văn bản đã thay thế)"
    low = bo_dau(hl).lower()
    if "thay the" in low and "dang co hieu luc" in low:   # tep khop la van ban THAY THE (ten tep dan so cu)
        return "KHONG_THAY", "chỉ thấy văn bản thay thế trong kho (bình thường); văn bản cũ không còn trong 01, 02"
    if hl and not any(x in low for x in ("het hieu luc", "bi thay the", "da bi thay", "lich su")):
        return "LECH", f"manifest ghi hết hiệu lực/bị thay thế bằng {m['thay_bang'][:50]}, kho ghi “{hl[:80]}”"
    return "KHOP", f"kho có tệp; hiệu lực kho: {hl[:60] or 'không có'}"


def slug_luat(ten: str) -> list[str]:
    bo = {"LUAT", "VA", "CUA", "SO"}
    return [t for t in tach(ten) if t not in bo]


def doi_chieu_vbhn(m: dict, tep_vb, tep_md):
    ts = slug_luat(m["luat"])
    cung_luat = [p for p in tep_vb + tep_md
                 if ts and all(t in set(tach(os.path.basename(p))) for t in ts)]
    vbhn_trong_kho = sorted({x for p in cung_luat
                             for x in re.findall(r"\d+-VBHN-VPQH", bo_dau(os.path.basename(p)).upper())})
    so_m = m["vbhn"].replace("/", "-")
    if not cung_luat:
        return "KHONG_THAY", f"không có tệp “{m['luat']}” trong 01, 02 (manifest dẫn {m['vbhn']} ngày {m['ngay_vbhn']})"
    khac = [x for x in vbhn_trong_kho if x != so_m.upper()]
    if so_m.upper() in vbhn_trong_kho:
        return "KHOP", f"kho có {m['vbhn']}" + (f"; cùng cụm tên còn VBHN {', '.join(khac)} (có thể là luật khác)" if khac else "")
    return "LECH", f"manifest {m['vbhn']}; kho có VBHN: {', '.join(vbhn_trong_kho) or 'không rõ'} — kiểm VBHN mới hơn"


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    kho = argv[argv.index("--kho") + 1] if "--kho" in argv else None
    if not kho:
        import duong_dan
        try:
            kho = duong_dan.ktc_database(canh_bao_ban_cu=False)
        except Exception as e:  # noqa: BLE001
            print(f"✗ không tìm thấy KTC-Database: {e}")
            return 2
    ngay = argv[argv.index("--ngay") + 1] if "--ngay" in argv else datetime.date.today().isoformat()
    try:
        with open(MANIFEST, encoding="utf-8") as f:
            man = json.load(f)
    except OSError as e:
        print(f"✗ không đọc được kho_manifest.json: {e}")
        return 2
    if not os.path.isdir(os.path.join(kho, THU_MUC_QUET[0])):
        print(f"✗ KTC-Database không có {THU_MUC_QUET[0]}: {kho}")
        return 2
    tep_vb, tep_md = lap_chi_muc(kho)
    hang = []
    for v in man["van_ban"]:
        kq, gc, tep, _ = doi_chieu_van_ban(v, tep_vb, tep_md)
        hang.append(("Văn bản", v["so_hieu"], v.get("ngay", ""), kq, gc, tep or []))
    for v in man["van_ban_het_hieu_luc_hay_gap"]:
        kq, gc = doi_chieu_het_hieu_luc(v, tep_vb, tep_md)
        hang.append(("Hết hiệu lực", v["so_hieu"], v.get("ngay", ""), kq, gc, []))
    for v in man["van_ban_hop_nhat_da_biet"]:
        kq, gc = doi_chieu_vbhn(v, tep_vb, tep_md)
        hang.append(("VBHN", v["luat"], v["ngay_vbhn"], kq, gc, []))

    dem = {}
    for h in hang:
        dem[h[3]] = dem.get(h[3], 0) + 1
    print(f"Kho: {kho}\nManifest: {man.get('phien_ban_kho','')}\n")
    for nhom, so, nd, kq, gc, _ in hang:
        if kq not in ("KHOP", "BO_QUA"):
            print(f"  {kq:10s} [{nhom}] {so} — {gc}")
    print("\nTổng hợp: " + " · ".join(f"{k}={v}" for k, v in sorted(dem.items())))

    out = os.path.join(DU_AN, "30-Ket-Qua", ngay, "dong-bo-kho-897")
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, "Bao-cao-lech.md")
    L = ["# Báo cáo đối chiếu Kho-Du-Lieu-897 với KTC-Database", "",
         f"**Ngày:** {ngay} · **Manifest lõi:** {man.get('phien_ban_kho','')}",
         "**Chế độ:** chỉ đọc. Không sửa gói skill, không ghi vào KTC-Database.", "",
         "Tổng hợp: " + " · ".join(f"{k} = {v}" for k, v in sorted(dem.items())), "",
         "Ý nghĩa: `KHOP` khớp · `KHOP*` khớp nhưng có nhiều tệp cùng số hiệu · `LECH` ngày/hiệu lực/VBHN lệch · "
         "`KHONG_THAY` không tìm thấy trong 01, 02 (chưa chắc là lỗi: kho 03 đơn vị trực thuộc không quét; số hiệu có thể ghi khác) · "
         "`BO_QUA` phụ lục.", "",
         "| Nhóm | Số hiệu / văn bản | Ngày | Kết quả | Ghi chú | Tệp trong kho |", "|---|---|---|---|---|---|"]
    for nhom, so, nd, kq, gc, tep in hang:
        L.append(f"| {nhom} | {so} | {nd} | {kq} | {gc.replace('|', '/')} | {'; '.join(os.path.basename(t) for t in tep)[:120]} |")
    ld = [h for h in hang if h[3] in ("LECH", "KHONG_THAY")]
    L += ["", "## Đề xuất (không tự thực hiện)", ""]
    if ld:
        L += ["Gửi **đơn vị quản lý Skill** (Phòng QLKHCN&HTPT, nơi lưu TB 1206/TB-CĐKT) xem xét cập nhật `kho_manifest.json` "
              "và bảng 04 của bản chính thức kế tiếp đối với các dòng `LECH`, `KHONG_THAY` ở trên. Kho trong lõi bản cá nhân "
              "**giữ nguyên** (lõi nguyên bản — `dong_goi_ra_soat_897.py` sẽ báo lỗi nếu sửa).",
              "Dòng `KHONG_THAY` là văn bản có trong Kho của Skill nhưng không tìm thấy bằng số hiệu trong 01, 02 của KTC-Database: "
              "người quản lý kho kiểm tra có phải do kho chưa nạp hay do đặt tên tệp khác."]
    else:
        L.append("Không có lệch.")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print(f"\nĐã ghi {os.path.relpath(p, DU_AN)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
