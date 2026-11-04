# -*- coding: utf-8 -*-
"""Tim duong dan du an va kho KTC-Database — KHONG ghi cung o dia (DL-20260918-005, Quy uoc 2).

KTC-Quan-tri chay tai may (ban lam viec cuc bo). KTC-Database chi con BAN GOC tren Google Drive
(ban chep o may se bi xoa — ban chep da cu: 18/9/2026 thieu 163/1171 tep so voi Drive). Thu tu tim:
  1. Bien moi truong KTC_DATABASE_DIR.
  2. O Google Drive for Desktop: <o>:\\My Drive\\KTC-Database (hoac "Drive của tôi", Shared drives\\*\\).
  3. Thu muc NGANG CAP <cha cua KTC-Quan-tri>/KTC-Database — ban chep cuc bo, CO THE CU (canh bao).
  4. Khong tim thay -> nem loi ro rang (skill phai DUNG VA HOI, khong suy dien).
"""
import glob
import os
import string
import sys

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEN = "KTC-Database"


def _tren_drive(ten=TEN):
    for o in string.ascii_uppercase:
        goc = f"{o}:\\"
        if not os.path.isdir(goc):
            continue
        for mau in ("My Drive", "Drive của tôi", os.path.join("Shared drives", "*"),
                    os.path.join("Bộ nhớ dùng chung", "*")):
            for p in glob.glob(os.path.join(goc, mau, ten)):
                if os.path.isdir(p):
                    yield p


def ktc_database(canh_bao_ban_cu: bool = True) -> str:
    env = os.environ.get("KTC_DATABASE_DIR")
    if env and os.path.isdir(env):
        return env
    for p in _tren_drive():
        return p
    p = os.path.join(os.path.dirname(DU_AN), TEN)
    if os.path.isdir(p):
        if canh_bao_ban_cu:
            print(f"⚠ Đang dùng bản chép cục bộ {p} — có thể cũ hơn bản gốc trên Google Drive.",
                  file=sys.stderr)
        return p
    raise FileNotFoundError(
        "Không tìm thấy KTC-Database. Đặt biến môi trường KTC_DATABASE_DIR trỏ tới thư mục "
        "KTC-Database trên Google Drive (ví dụ <ổ Drive>\\My Drive\\KTC-Database).")


def he_ngoai(ten):
    """Tim mot he KTC khac (vi du KTC-Ra-Soat-897-Universal-Plugin) — tra ve duong dan hoac None.

    Thu tu: bien moi truong KTC_<TEN> -> thu muc ngang cap voi du an -> moi o Google Drive.
    Cac he KTC khong nam cung mot o dia: KTC-Quan-tri o D:, kho 897 o Google Drive (I:).
    Vi vay khong duoc gia dinh "ngang cap" nhu truoc (Nguyen tac 4.2: khong ghi cung o dia).
    """
    mt = os.environ.get("KTC_" + ten.upper().replace("-", "_"))
    if mt and os.path.isdir(mt):
        return mt
    ngang = os.path.join(os.path.dirname(DU_AN), ten)
    if os.path.isdir(ngang):
        return ngang
    for p in _tren_drive(ten):
        return p
    return None
