# -*- coding: utf-8 -*-
"""Chuan hoa chu viet theo quy uoc cua Truong (21/10/2026, nguoi dung chot):
1) "phong", "khoa" viet THUONG trong loi van, ke ca khi di voi ten viet tat (phong TC-KT, khoa DT&SHLX);
   chi viet hoa o dau cau, dau dong, sau dau hai cham.
2) Chu dau sau MOI dau hai cham viet hoa — ke ca khi sau dau hai cham la muc liet ke "(1) ...", "a) ...";
   cac muc "(n) ..." tiep theo (sau dau cham phay) cung viet hoa.
"""
import re

THUONG = "a-zđàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ"
DON_VI = (r"(?:TH-HC&QT|TC-KT|TCCB&CTHSSV|QLĐT&BĐCL|QLKHCN&HTPT|ĐT&SHLX|KT&CN|KT&NL|"
          r"Tổng hợp - Hành chính|Tổng hợp – Hành chính|Tài chính - Kế toán|Tài chính – Kế toán|Tổ chức cán bộ|"
          r"Quản lý Đào tạo|Quản lý khoa học|Đào tạo và Sát hạch lái xe|Kỹ thuật và Công nghệ)")
_giua_cau = re.compile(r"(?<=[" + THUONG + r"0-9,;(] )(Phòng|Khoa)(?= " + DON_VI + r")")
_sau_2cham = re.compile(r"(?<![\d/])(:\s+)((?:\(\d+\)|[a-zđ]\))\s+)?([" + THUONG + r"])")
_liet_ke = re.compile(r"(;\s+\(\d+\)\s+)([" + THUONG + r"])")


def chuan(s):
    if not s:
        return s
    s = _giua_cau.sub(lambda m: m.group(1).lower(), s)
    s = _sau_2cham.sub(lambda m: m.group(1) + (m.group(2) or "") + m.group(3).upper(), s)
    s = _liet_ke.sub(lambda m: m.group(1) + m.group(2).upper(), s)
    return s


def vi_tri_can_hoa(t):
    """Vi tri cac ky tu thuong can viet hoa trong t (de sua bang Track Changes)."""
    out = [m.start(3) for m in _sau_2cham.finditer(t) if not re.search(r"https?$", t[:m.start()])]
    out += [m.start(2) for m in _liet_ke.finditer(t)]
    return sorted(set(out))


def vi_tri_can_thuong(t):
    return [m.start(1) for m in _giua_cau.finditer(t)]


if __name__ == "__main__":
    for x in ["phối hợp với Phòng TH-HC&QT, Phòng TC-KT và các đơn vị", "Chờ Phòng TC-KT", "b) Phòng TC-KT bổ sung",
              "gồm 03 nhóm (Điều 3): (1) hoạt động đào tạo; (2) hoạt động sát hạch", "Hình thức: văn bản ký số",
              "Nguồn thu: học phí Hạng A: 2.800.000", "lúc 8:30 sáng", "https://a.b"]:
        print(x, "=>", chuan(x))
