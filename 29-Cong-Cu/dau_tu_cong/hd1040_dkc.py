# -*- coding: utf-8 -*-
"""Điều kiện chung (ĐKC) của hợp đồng — lấy NGUYÊN VĂN từ mẫu QĐ 1040/QĐ-BXD, chỉ điền chỗ trống và gỡ chú thích hướng dẫn.

Nguyên tắc (Hướng dẫn kèm QĐ 1040, mục 4.1.c): Phần 3 "Điều kiện chung" là thành phần "cứng" — không viết lại, không rút gọn.
Mọi chỗ khác mẫu đều nằm trong bảng THAY dưới đây để người kiểm tra thấy rõ từng chỗ đã điều chỉnh cho đúng gói thầu.
"""
import re

# ---------------------------------------------------------------- tham chiếu "Điều [tên]" → số Điều
def _chuan(s):
    return re.sub(r"\s+", " ", s.strip().lower())


ALIAS = {"tạm dừng hợp đồng": "tạm dừng và chấm dứt", "tạm dừng và chấm dứt hợp đồng": "tạm dừng và chấm dứt"}


def so_dieu_theo_ten(dkc, ten):
    t = _chuan(ten)
    t = ALIAS.get(t, t)
    for n, v in dkc.items():
        if _chuan(v["ten"]).startswith(t) or t.startswith(_chuan(v["ten"])[:25]):
            return n
    raise KeyError(ten)


PHU_LUC_SO = {  # "Phụ lục số ... [tên]" → số phụ lục của hợp đồng
    "tiến độ thực hiện công việc": 2,
    "tiến độ thực hiện hợp đồng": 2,
    "nhân lực của bên nhận thầu": 4,
    "nhân sự chủ đầu tư": 5,
}


def giai_tham_chieu(dong, dkc):
    dong = re.sub(r"Điều\s*\[([^\]]+)\]", lambda m: "Điều %d" % so_dieu_theo_ten(dkc, m.group(1)), dong)

    def pl(m):
        k = _chuan(m.group(1))
        for ten, so in PHU_LUC_SO.items():
            if k.startswith(ten):
                return "Phụ lục số %d" % so
        return m.group(0)

    dong = re.sub(r"Phụ lục số\s*\.{2,}\s*\[([^\]]+)\]", pl, dong)
    dong = dong.replace("[ĐKCT]", "ĐKCT")
    return dong


def lay_dkc(mau, dkc_dict, thay=None, bo=None):
    """Trả danh sách [(so_dieu, ten_dieu, [dong...])] đã giải tham chiếu.

    thay: danh sách (regex bắt đầu dòng, nội dung mới | callable) — thay cả dòng. Mỗi quy tắc phải khớp ≥ 1 dòng.
    bo:   danh sách regex bắt đầu dòng cần bỏ (chú thích hướng dẫn trong ngoặc vuông). Quy tắc mặc định: bỏ dòng '[...]'.
    """
    thay = list(thay or [])
    dung = {i: 0 for i in range(len(thay))}
    ra = []
    for n in sorted(dkc_dict):
        ten = dkc_dict[n]["ten"]
        dong_ra = []
        for d in dkc_dict[n]["dong"]:
            if re.match(r"^\[.*\]$", d):  # chú thích hướng dẫn của mẫu
                continue
            if bo and any(re.match(b, d) for b in bo):
                continue
            moi = None
            for i, (mau_re, nd) in enumerate(thay):
                if re.match(mau_re, d):
                    moi = nd(d) if callable(nd) else nd
                    dung[i] += 1
                    break
            d = moi if moi is not None else d
            if d == "":
                continue
            dong_ra.append(giai_tham_chieu(d, dkc_dict))
        ra.append((n, giai_tham_chieu(ten, dkc_dict), dong_ra))
    chua = [thay[i][0] for i, k in dung.items() if k == 0]
    if chua:
        raise RuntimeError("Quy tắc THAY không khớp dòng nào của mẫu: %s" % chua)
    return ra


def con_trong(ra):
    """Liệt kê chỗ còn ngoặc vuông / dấu '...' chưa điền."""
    kq = []
    for n, ten, ds in ra:
        for d in ds:
            if "[" in d or "..." in d or "…" in d:
                kq.append((n, d[:200]))
    return kq
