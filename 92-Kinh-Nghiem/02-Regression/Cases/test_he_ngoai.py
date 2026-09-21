# -*- coding: utf-8 -*-
"""Thu NGUOC: C3 giai duoc duong dan sang HE KTC KHAC, va khong nhan bua.

Ly do ton tai: cac he KTC khong nam cung mot o dia (KTC-Quan-tri o D:, kho 897 tren Google
Drive). C3 truoc day chi thu thu muc ngang cap nen moi tham chieu HOP LE sang he khac deu bi
bao "khong tim thay" (21/9/2026, MEMORY-INDEX dan deployment-team cua kho 897). Canh bao sai
lam nguoi ta quen nhin bang canh bao — nen phai chan ca hai huong: bo sot VA bao nham.

Chay: python 92-Kinh-Nghiem/02-Regression/Cases/test_he_ngoai.py
"""
import os
import sys

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "29-Cong-Cu"))
import duong_dan as dd          # noqa: E402
import kiem_tra_he_thong as K   # noqa: E402

sai = []


def kiem(ten, dk, mo_ta):
    print(f"  {'OK ' if dk else ' X '} {ten:38s} {mo_ta}")
    if not dk:
        sai.append(ten)


# --- he_ngoai ---
kiem("ten_bia_tra_None", dd.he_ngoai("KTC-Khong-Ton-Tai-XYZ") is None,
     "tên hệ không có thật -> None, không đoán bừa")

mt = "KTC_KTC_THU_NGHIEM_MT"
os.environ[mt] = DU_AN
kiem("uu_tien_bien_moi_truong", dd.he_ngoai("KTC-Thu-Nghiem-MT") == DU_AN,
     "biến môi trường KTC_<TEN> được ưu tiên trước")
del os.environ[mt]

# --- _co_o_he_ngoai ---
kiem("khong_phai_he_ngoai", K._co_o_he_ngoai("20-Chuan-Chung/11-Quy-Tac-Task-ID.md") is False,
     "đường dẫn trong chính dự án -> không xử như hệ ngoài")
kiem("mot_doan_khong_tinh", K._co_o_he_ngoai("KTC-Quan-tri") is False,
     "chỉ mỗi tên hệ, không có tệp -> False")
kiem("he_ngoai_khong_co_tep", K._co_o_he_ngoai("KTC-Ra-Soat-897-Universal-Plugin/khong-co-tep-nay.md") is False,
     "ca ngược: hệ có thật nhưng tệp KHÔNG có -> vẫn phải báo thiếu")

that = "KTC-Ra-Soat-897-Universal-Plugin/CLAUDE.md"
co_kho = dd.he_ngoai("KTC-Ra-Soat-897-Universal-Plugin") is not None
if co_kho:
    kiem("he_ngoai_co_tep", K._co_o_he_ngoai(that) is True,
         "hệ ngoài có thật + tệp có thật -> nhận")
else:
    print("  -- bỏ qua ca 'hệ ngoài có tệp': máy này không có kho 897")

print(f"\n{'ĐẠT' if not sai else 'KHÔNG ĐẠT'}: {len(sai)} ca sai")
sys.exit(1 if sai else 0)
