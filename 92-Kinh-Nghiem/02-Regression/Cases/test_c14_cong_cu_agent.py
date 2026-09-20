# -*- coding: utf-8 -*-
"""Thu NGUOC phep kiem C14 — script agent vien dan co that su duoc dong goi khong?

Ly do ton tai: 19/9/2026 CONG_CU_CHO_AGENT thieu kiem_the_thuc.py, ma hai agent
(ktc-kiem-san-pham, ktc-kiem-ho-so-don-vi) lai lay no lam PHEP KIEM SO 1. Khi chay
ngoai thu muc du an, agent khong tim thay script -> phep kiem the thuc bien mat,
KHONG bao loi. Day dung kieu loi "bao sach vi hong", nen C14 phai duoc thu nguoc.

Chay: python 92-Kinh-Nghiem/02-Regression/Cases/test_c14_cong_cu_agent.py
"""
import io
import os
import sys
import tempfile

DU_AN = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(DU_AN, "29-Cong-Cu"))
import kiem_tra_he_thong as K  # noqa: E402

that_bai = []


def kiem(ten, dk, mo_ta):
    print(f"  {'OK ' if dk else ' X '} {ten:52s} {mo_ta}")
    if not dk:
        that_bai.append(ten)


def du_an_gia(cong_cu, than_agent, ten_agent="ktc-kiem-san-pham.md"):
    """Dung mot du an gia toi thieu du cho C14 chay."""
    g = tempfile.mkdtemp(prefix="ktc_c14_")
    os.makedirs(os.path.join(g, "29-Cong-Cu", "plugin_src", "agents"))
    os.makedirs(os.path.join(g, "31-Plugin"))
    io.open(os.path.join(g, "29-Cong-Cu", "dong_goi_plugin.py"), "w", encoding="utf-8").write(
        "CONG_CU_CHO_AGENT = [" + ", ".join(f'"{c}"' for c in cong_cu) + "]\n")
    io.open(os.path.join(g, "29-Cong-Cu", "plugin_src", "agents", ten_agent),
            "w", encoding="utf-8").write(than_agent)
    return g


def so_loi(g):
    truoc = len(K.loi)
    K.c14_cong_cu_agent_duoc_dong_goi(du_an=g)
    return len(K.loi) - truoc


# --- CA BIET CHAC LA SAI: agent goi script khong duoc dong goi ---
n = so_loi(du_an_gia(["tra_hieu_luc.py"],
                     "1. **Thể thức**: `python 29-Cong-Cu/kiem_the_thuc.py <tệp>`.\n"))
kiem("bat_thieu_script", n == 1, "agent gọi kiem_the_thuc.py chưa đóng gói -> phải báo 1 lỗi")

# --- CA DUNG: da co trong CONG_CU_CHO_AGENT ---
n = so_loi(du_an_gia(["tra_hieu_luc.py", "kiem_the_thuc.py"],
                     "1. **Thể thức**: `python 29-Cong-Cu/kiem_the_thuc.py <tệp>`.\n"))
kiem("khong_bao_nham", n == 0, "script đã trong CONG_CU_CHO_AGENT -> không báo lỗi")

# --- CA DUNG: script di theo references cua skill trong cay 31-Plugin ---
g = du_an_gia(["tra_hieu_luc.py"], "Đọc Excel: `read_bc736_excel.py` (v3.3).\n")
sub = os.path.join(g, "31-Plugin", "skills", "bao-cao", "references", "Skill-Library")
os.makedirs(sub)
io.open(os.path.join(sub, "read_bc736_excel.py"), "w", encoding="utf-8").write("# x\n")
kiem("chap_nhan_trong_31_plugin", so_loi(g) == 0,
     "script nằm sẵn trong 31-Plugin/ -> tính là đã đóng gói")

# --- CA DUNG: agent noi bo duoc mien ---
n = so_loi(du_an_gia(["tra_hieu_luc.py"],
                     "Bash chỉ dùng để đọc: `python 29-Cong-Cu/kiem_tra_he_thong.py`.\n",
                     ten_agent="ktc-tu-cai-tien.md"))
kiem("mien_agent_noi_bo", n == 0, "ktc-tu-cai-tien chỉ chạy trong dự án -> được miễn")

# --- Du an THAT phai sach ---
kiem("du_an_that_sach", so_loi(DU_AN) == 0, "dự án thật: 0 script agent thiếu")

print(f"\n{'ĐẠT' if not that_bai else 'KHÔNG ĐẠT'}: {len(that_bai)} ca sai")
sys.exit(1 if that_bai else 0)
