# -*- coding: utf-8 -*-
"""Trich Bo chi so KPI chinh thuc (QD 2164/QD-CDKT ngay 30/9/2026, 55 phu luc) thanh du lieu dan xuat:

    11-Du-lieu-Cong-Viec/CHI SO KPI/bo-chi-so-kpi-QD2164.csv      moi chi so mot dong (phu luc, doi tuong, Truc, STT,
                                                                   tieu chi/nhiem vu, chi so KPI, don vi do, ...)
    11-Du-lieu-Cong-Viec/CHI SO KPI/00-MUC-LUC-BO-CHI-SO-KPI-QD2164.md   muc luc 55 phu luc + kiem tra chat luong

Nguon: 11-Du-lieu-Cong-Viec/CHI SO KPI/Bo-chi-so-KPIs/ (ban nguoi phu trach nap ngay 30/9/2026, du 55 phu luc; kho 02
KTC-Database da co Quyet dinh va 51/55 phu luc tu 30/9/2026). Khong sua tep goc. Chay lai khi phu luc duoc dieu chinh (Dieu 3, 4 QD 2164).

    python 29-Cong-Cu/trich_bo_chi_so_kpi.py
"""
import csv, glob, hashlib, io, os, re, sys, unicodedata
import openpyxl

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOC = os.path.join(DU_AN, "11-Du-lieu-Cong-Viec", "CHI SO KPI", "Bo-chi-so-KPIs")
RA = os.path.join(DU_AN, "11-Du-lieu-Cong-Viec", "CHI SO KPI")
QD = "Quyết định số 2164/QĐ-CĐKT ngày 30/9/2026"
N = lambda s: unicodedata.normalize("NFC", str(s)).strip() if s is not None else ""  # noqa: E731
LA_MA = {"I": 1, "V": 5, "X": 10}
# Phu luc tap the -> ma don vi chuan (20-Chuan-Chung/13-Bang-Ma-Don-Vi.md)
MA_TAP_THE = {"I": "P-TCCB", "II": "P-QLDT", "III": "P-THHC", "IV": "P-QLKH", "V": "P-TCKT", "VI": "K-KHCB",
              "VII": "K-SUPH", "VIII": "K-KTNL", "IX": "K-KTCN", "X": "K-YDUOC", "XI": "K-DTSHLX"}


def so_la_ma(s):
    t = 0
    for i, c in enumerate(s):
        v = LA_MA[c]
        t += -v if i + 1 < len(s) and LA_MA[s[i + 1]] > v else v
    return t


def ma_phu_luc(ten):
    m = re.match(r"Phu luc ([IVX]+)(?:[._ ]\s*(\d+))?", ten)
    return m.group(1), (m.group(2) or "")


def doc(f):
    ws = openpyxl.load_workbook(f).worksheets[0]
    rows = [[N(x) for x in r] for r in ws.iter_rows(values_only=True)]
    rows = [r for r in rows if any(r)]
    tieu_de = " ".join(rows[0][0].split()) if rows else ""
    i_hdr = next(i for i, r in enumerate(rows) if "STT" in r)
    hdr = [h for h in rows[i_hdr] if h]
    out, truc, stt, tc = [], "", "", ""
    for r in rows[i_hdr + 1:]:
        r = r + [""] * (8 - len(r))
        if re.match(r"^Trục \d", r[1]):
            truc, stt, tc = r[1][:6].replace("Trục ", ""), "", ""
            continue
        if r[0] and r[0] != "-":
            stt, tc = r[0], r[1] or tc
        elif r[1]:
            tc = r[1]
        if r[2]:
            out.append({"truc": truc, "stt": stt, "tieu_chi": " ".join(tc.split()), "kpi": " ".join(r[2].split()),
                        "don_vi_do": r[3], "chiu_trach_nhiem": r[4] if len(hdr) > 4 else "",
                        "lanh_dao_chu_tri": r[5] if len(hdr) > 5 else "", "don_vi_dau_moi": r[6] if len(hdr) > 6 else "",
                        "don_vi_phoi_hop": r[7] if len(hdr) > 7 else ""})
    return tieu_de, hdr, out


def main():
    tep = sorted(glob.glob(os.path.join(GOC, "Phu luc*.xlsx")),
                 key=lambda f: (so_la_ma(ma_phu_luc(os.path.basename(f))[0]), int(ma_phu_luc(os.path.basename(f))[1] or 0)))
    dong, muc, canh_bao = [], [], []
    for f in tep:
        ten = unicodedata.normalize("NFC", os.path.basename(f))
        la, con = ma_phu_luc(ten)
        so = la + ("." + con if con else "")
        tieu_de, hdr, rows = doc(f)
        doi_tuong = "Tập thể" if "TẬP THỂ" in tieu_de else ("Lãnh đạo Trường" if la == "XII" else "Cá nhân")
        m_td = re.match(r"Ph\S* l\S* ([IVX]+(?:\.\d+)?)", tieu_de)
        if not tieu_de.startswith("Phụ lục "):
            canh_bao.append(f"Phụ lục {so}: tiêu đề viết “{tieu_de.split()[0]} {tieu_de.split()[1]}” (chính tả “Phụ lục”)")
        if not m_td or m_td.group(1) != so:
            canh_bao.append(f"Phụ lục {so}: tiêu đề trong tệp ghi “{tieu_de[:40]}…” (số phụ lục hoặc chữ “Phụ lục” lệch tên tệp)")
        chuc_danh = re.sub(r"^.*?CHỈ SỐ KPI\s*(TẬP THỂ\s*)?", "", tieu_de)
        chuc_danh = re.sub(r"\s*CỦA TRƯỜNG CAO ĐẲNG KON TUM\s*$", "", chuc_danh).strip()
        ma = MA_TAP_THE.get(la, "") if doi_tuong == "Tập thể" else ""
        truc = {}
        for r in rows:
            truc[r["truc"]] = truc.get(r["truc"], 0) + 1
            dong.append({"phu_luc": so, "doi_tuong": doi_tuong, "ma_don_vi": ma, "chuc_danh_don_vi": chuc_danh, **r,
                         "tep": ten})
        muc.append((so, doi_tuong, ma, chuc_danh, len(rows), truc, len(hdr), ten,
                    hashlib.sha256(open(f, "rb").read()).hexdigest()[:12]))
    cot = ["phu_luc", "doi_tuong", "ma_don_vi", "chuc_danh_don_vi", "truc", "stt", "tieu_chi", "kpi", "don_vi_do",
           "chiu_trach_nhiem", "lanh_dao_chu_tri", "don_vi_dau_moi", "don_vi_phoi_hop", "tep"]
    with io.open(os.path.join(RA, "bo-chi-so-kpi-QD2164.csv"), "w", encoding="utf-8-sig", newline="") as g:
        w = csv.DictWriter(g, fieldnames=cot)
        w.writeheader()
        w.writerows(dong)
    qd = os.path.join(GOC, "2164. Quyet dinh ban hanh bo Chi so KPI_Truong.docx")
    L = [f"# Bộ chỉ số KPI tập thể, cá nhân — {QD} (CHÍNH THỨC)", "",
         "Tệp **dẫn xuất**, sinh tự động bằng `29-Cong-Cu/trich_bo_chi_so_kpi.py` từ 55 phụ lục trong `Bo-chi-so-KPIs/` — "
         "không sửa tay. Khi trích dẫn làm căn cứ: dẫn **Quyết định và phụ lục**, không dẫn tệp này.", "",
         f"- Quyết định: `Bo-chi-so-KPIs/2164. Quyet dinh ban hanh bo Chi so KPI_Truong.docx` (sha256 "
         f"`{hashlib.sha256(open(qd, 'rb').read()).hexdigest()}`), Hiệu trưởng Lê Trí Khải ký, hiệu lực từ ngày ký. Bản gốc "
         "kho 02: `02-KTC-Regulations/02-01- Quy che - quy dinh - huong dan chung/QD-2164-QD-CDKT_…_2026.docx` (trùng mã băm), "
         "phụ lục trong thư mục con `02-01-KPI_Phu-luc-ca-nhan-theo-vi-tri-2026/`.",
         "- Mục đích (Điều 2): xây dựng, ký Bản cam kết KPI hằng năm; theo dõi, đánh giá, xếp loại hằng quý, hằng năm theo "
         "Quy chế đánh giá KPI (Quyết định số 1923/QĐ-CĐKT); quản lý viên chức. Áp dụng: tập thể các phòng, khoa; toàn thể "
         "viên chức, người lao động, nhà giáo.",
         "- Nguyên tắc (Điều 3): SMART; **tổng trọng số mỗi bộ KPI bằng 100%**; điều chỉnh qua Phòng TCCB&CTHSSV trình Hiệu "
         "trưởng. **Phụ lục không có cột trọng số, chỉ tiêu** — trọng số, chỉ tiêu xác định khi lập, ký Bản cam kết KPI "
         "(mẫu Phụ lục Quyết định số 1923/QĐ-CĐKT).",
         f"- Dữ liệu: `bo-chi-so-kpi-QD2164.csv` — {len(dong)} chỉ số, mỗi dòng một chỉ số (phụ lục, đối tượng, mã đơn vị, "
         "Trục, STT, tiêu chí/nhiệm vụ, chỉ số KPI, đơn vị đo; Phụ lục XII thêm người chịu trách nhiệm, lãnh đạo chủ trì, "
         "đơn vị đầu mối, phối hợp).", "",
         "## Mục lục 55 phụ lục", "",
         "| Phụ lục | Đối tượng | Mã ĐV | Chức danh / đơn vị (theo tiêu đề phụ lục) | Số KPI | Theo Trục (1…6) | Cột | Tệp | sha256 (12 ký tự) |",
         "|---|---|---|---|---:|---|---:|---|---|"]
    for so, dt, ma, cd, n, truc, nc, ten, h in muc:
        t = " · ".join(str(truc.get(str(k), 0)) for k in range(1, 7))
        L.append(f"| {so} | {dt} | {ma} | {cd} | {n} | {t} | {nc} | `{ten}` | `{h}` |")
    L += ["", "## Kiểm tra chất lượng khi trích (không sửa văn bản đã ban hành)", ""]
    L += [f"- {c}" for c in canh_bao] or ["- Không phát hiện lệch tiêu đề."]
    io.open(os.path.join(RA, "00-MUC-LUC-BO-CHI-SO-KPI-QD2164.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(L) + "\n")
    print(f"{len(muc)} phụ lục, {len(dong)} chỉ số, {len(canh_bao)} cảnh báo tiêu đề")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
