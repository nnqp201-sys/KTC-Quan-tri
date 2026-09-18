# -*- coding: utf-8 -*-
"""Tim duong dan du an va kho KTC-Database — KHONG ghi cung o dia (DL-20260918-005, Quy uoc 2).

Du an se chi con tren Google Drive (khong con ban sao o D:). Moi script lay duong dan qua day:
  1. Bien moi truong KTC_DATABASE_DIR (neu may co dat).
  2. Thu muc NGANG CAP voi du an: <cha cua KTC-Quan-tri>/KTC-Database
     (dung ca khi Drive gan o G:\\My Drive\\..., o D:\\..., hay thu muc Cowork mo thu muc cha).
  3. Khong tim thay -> nem loi ro rang (skill phai DUNG VA HOI, khong suy dien).
"""
import os

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ktc_database() -> str:
    ung_vien = [os.environ.get("KTC_DATABASE_DIR"),
                os.path.join(os.path.dirname(DU_AN), "KTC-Database")]
    for p in ung_vien:
        if p and os.path.isdir(p):
            return p
    raise FileNotFoundError(
        "Không tìm thấy KTC-Database. Đặt biến môi trường KTC_DATABASE_DIR, hoặc để thư mục "
        "KTC-Database ngang cấp với KTC-Quan-tri (cùng thư mục cha trên Google Drive).")
