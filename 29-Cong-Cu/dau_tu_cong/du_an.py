# -*- coding: utf-8 -*-
"""Nạp tệp nguồn dữ liệu dự án (YAML) cho các script dựng văn bản đầu tư công.

Dùng:  from du_an import tai
       D = tai()                      # mặc định du-an_CLC-2026-2030.yaml cạnh tệp này
       D["du_an"]["ten"]; D["goi_thau"]["KS"]["gia"]

Quy tắc: số liệu, số/ngày văn bản, tên nhà thầu chỉ sửa trong tệp YAML, không gõ vào script.
"""
import os
import yaml

MAC_DINH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "du-an_CLC-2026-2030.yaml")


def tai(duong_dan=None):
    p = duong_dan or os.environ.get("KTC_DU_AN") or MAC_DINH
    with open(p, encoding="utf-8") as f:
        d = yaml.safe_load(f)
    for k in ("du_an", "van_ban", "goi_thau"):
        if k not in d:
            raise SystemExit(f"{p}: thiếu khối '{k}'")
    return d


def cau_hinh_qd(d, ma):
    """Trả 'Quyết định số X/QĐ-CĐKT ngày dd/mm/yyyy' của văn bản có mã (vd 'qd_2236')."""
    v = d["van_ban"][ma]
    return f"Quyết định số {v['so']} ngày {v['ngay']}"


# --- Đường dẫn dùng chung (không ghi cứng ổ đĩa, phép kiểm C13) ---
import sys as _sys  # noqa: E402

_sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import duong_dan as _dd  # noqa: E402

GOC = _dd.DU_AN


def _p(*phan):
    return os.path.join(*phan).replace("\\", "/")


def ket_qua(*phan):
    """Đường dẫn trong thư mục kết quả của dự án."""
    return _p(GOC, "30-Ket-Qua", *phan)


def kho(*phan):
    """Đường dẫn trong kho dữ liệu nền (chỉ đọc)."""
    return _p(_dd.ktc_database(False), *phan)


def tai_ve(ten):
    return _p(os.path.expanduser("~"), "Downloads", ten)


def onedrive_cbdt(*phan):
    """Thư mục hồ sơ Chuẩn bị đầu tư trên OneDrive của P-THHC (biến KTC_CBDT_DIR hoặc suy từ OneDrive)."""
    goc = os.environ.get("KTC_CBDT_DIR") or _p(
        os.environ.get("OneDriveCommercial") or os.environ.get("OneDrive") or os.path.expanduser("~/OneDrive"),
        "1. Tong hop - Hanh chinh", "2. Bao cao chuyen de", "2026", "De xuat CTMTQG tich hop", "Chuan-bi-dau-tu")
    return _p(goc, *phan)
