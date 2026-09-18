# -*- coding: utf-8 -*-
"""Trich bao cao TUONG THUAT (Phu luc IIa) cua 13 don vi -> narrative.json

Khac lan chay truoc: lan truoc chi doc .xlsx (Phu luc IIb - bang nhiem vu),
bo sot hoan toan 13 file .docx chua VAN TUONG THUAT da chia san theo 6 Truc.
"""
import glob, json, os, re, sys
from docx import Document

# Goc du an suy ra tu vi tri tep nay — khong ghi cung duong dan tuyet doi,
# de doi cho du an la khong phai sua tung tool.
DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IN = os.path.join(DU_AN, "11-Du-Lieu-Dau-Vao", "01-Dau-Moi-Nop", "2026-09")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "_trung_gian", "narrative.json")

TRUC = [
    (1, r"Thực hiện mục tiêu phát triển kinh tế"),
    (2, r"Hoàn thiện thể chế"),
    (3, r"(Thúc đẩy phát triển|Phát triển)\s+(KH|khoa học)"),
    (4, r"Xây dựng Đảng"),
    (5, r"Phát triển văn hóa, con người"),
    (6, r"Củng cố quốc phòng"),
]
M_KQ = re.compile(r"^(Phần\s+I\b|I\.\s*(THỰC HIỆN|TÌNH HÌNH|KẾT QUẢ))", re.I)
M_DG = re.compile(r"^(II|III)\.\s*ĐÁNH GIÁ CHUNG", re.I)
M_KH = re.compile(r"^(Phần\s+II\b|I\.\s*KẾ HOẠCH|III\.\s*NHIỆM VỤ|II\.\s*NHIỆM VỤ)", re.I)
M_NQ = re.compile(r"Nghị quyết\s+số\s+(\d+)\s*-?\s*NQ/TW", re.I)
M_DAT = re.compile(r"^\d\.\s*Kết quả đạt được", re.I)
M_CHUA = re.compile(r"^\d\.\s*(Danh mục các công việc chưa hoàn thành|Các tồn tại, hạn chế|Tồn tại, hạn chế)", re.I)
M_HEAD = re.compile(r"^(Phần\s+[IVX]+|[IVX]+\.\s|\d+\.\s|\d+\.\d+\.?\s|[a-hk]\)\s|\*)")
M_LV = re.compile(r"^[a-hk]\)\s*(.+)$")

# Linh vuc -> nhan cap Truong (BC-375 dung dang "* Cong tac X:")
LINH_VUC = [
    ("Công tác tuyển sinh", r"tuyển sinh|nhập học|trúng tuyển|xét tuyển|hướng nghiệp"),
    ("Công tác đào tạo", r"đào tạo|giảng dạy|thời khóa biểu|tốt nghiệp|mở lớp|liên thông|thực tập|năm học"),
    ("Công tác chương trình, giáo trình", r"chương trình đào tạo|giáo trình|đề cương|chuẩn đầu ra"),
    ("Công tác khảo thí", r"khảo thí|thi kết thúc|ngân hàng đề|chấm thi|nhập điểm|thi lại|văn bằng|chứng chỉ"),
    ("Công tác bảo đảm chất lượng", r"bảo đảm chất lượng|kiểm định|tự đánh giá|chuẩn cơ sở"),
    ("Công tác tổ chức, cán bộ", r"tổ chức cán bộ|bổ nhiệm|tuyển dụng|vị trí việc làm|biên chế|nâng lương|thi đua|khen thưởng|kỷ luật|đánh giá xếp loại"),
    ("Công tác kế hoạch, tổng hợp", r"tổng hợp|kế hoạch công tác|văn thư|lưu trữ|hành chính|báo cáo định kỳ|quy chế làm việc"),
    ("Công tác khoa học, công nghệ và chuyển đổi số", r"khoa học|công nghệ|nghiên cứu|sáng kiến|chuyển đổi số|phần mềm|trí tuệ nhân tạo|AI|dữ liệu|hội thảo"),
    ("Công tác xây dựng Đảng", r"Đảng ủy|chi bộ|đảng viên|nghị quyết Hội nghị|sinh hoạt chính trị"),
    ("Công tác phòng, chống tham nhũng, tiêu cực", r"tham nhũng|tiêu cực|lãng phí|kê khai tài sản"),
    ("Công tác Công đoàn, Đoàn Thanh niên", r"Công đoàn|Đoàn Thanh niên|Đoàn viên|Hội Sinh viên|thanh niên"),
    ("Công tác quản lý cơ sở vật chất", r"cơ sở vật chất|sửa chữa|xây dựng công trình|thiết bị|tài sản|khuôn viên|ký túc xá"),
    ("Công tác tài chính", r"tài chính|kế toán|thanh toán|dự toán|quyết toán|học phí|lương|chế độ|định mức kinh tế|tự chủ"),
    ("Công tác học sinh, sinh viên", r"học sinh, sinh viên|HSSV|sĩ số|chủ nhiệm|nội trú|học bổng|an sinh"),
    ("Công tác truyền thông", r"truyền thông|tin, bài|website|fanpage|video|infographic|banner"),
    ("Công tác quốc phòng, an ninh", r"quốc phòng|an ninh|trật tự|bí mật nhà nước|phòng cháy|an toàn"),
    ("Công tác đối ngoại, hợp tác phát triển", r"đối ngoại|hợp tác|doanh nghiệp|quốc tế|Lào|MOU|liên kết"),
]


def linh_vuc(s: str, mac_dinh="Công tác khác") -> str:
    for ten, pat in LINH_VUC:
        if re.search(pat, s, re.I):
            return ten
    return mac_dinh


def doc_mot(path: str) -> dict:
    doc = Document(path)
    kq = {i: [] for i in range(1, 7)}
    kh = {i: [] for i in range(1, 7)}
    nq_kq, nq_kh = {}, {}
    dat, chua = [], []
    pha, truc, nq_hien, muc_dg = "KQ", None, None, None
    dem_truc = {}
    lv_hien = None

    for p in doc.paragraphs:
        t = " ".join(p.text.split())
        if not t:
            continue

        if M_KQ.match(t):
            pha, truc, nq_hien, muc_dg, lv_hien = "KQ", None, None, None, None; continue
        if M_DG.match(t):
            pha, truc, nq_hien, lv_hien = "DG", None, None, None; continue
        if M_KH.match(t):
            pha, truc, nq_hien, muc_dg, lv_hien = "KH", None, None, None, None; continue

        if pha == "DG":
            if M_DAT.match(t):   muc_dg = "dat";  continue
            if M_CHUA.match(t):  muc_dg = "chua"; continue
            if M_HEAD.match(t):  muc_dg = None;   continue
            noi = re.sub(r"^[-+•*]\s*", "", t)
            if muc_dg == "dat" and len(noi) > 15:  dat.append(noi)
            if muc_dg == "chua" and len(noi) > 15 and noi.lower() != "không": chua.append(noi)
            continue

        # Tieu de Truc
        gap = False
        for so, pat in TRUC:
            if re.search(pat, t, re.I) and M_HEAD.match(t):
                dem_truc[so] = dem_truc.get(so, 0) + 1
                if dem_truc[so] >= 2 and pha == "KQ":
                    pha = "KH"          # du phong khi thieu moc "Phan II"
                truc, nq_hien, lv_hien = so, None, None
                gap = True
                break
        if gap:
            continue

        m = M_NQ.search(t)
        if m and M_HEAD.match(t):
            nq_hien, truc, lv_hien = m.group(1), None, None
            continue

        m = M_LV.match(t)
        if m:
            lv_hien = m.group(1).strip().rstrip(":")
            continue

        if M_HEAD.match(t) and not t.startswith(("-", "+")):
            if re.match(r"^\d+\.\s", t) and not re.match(r"^\d+\.\d", t):
                truc, nq_hien, lv_hien = None, None, None
            continue

        noi = re.sub(r"^[-+•*]\s*", "", t).strip()
        if len(noi) < 15 or noi.lower().startswith(("không", "kính", "trên đây")):
            continue

        if nq_hien:
            (nq_kq if pha == "KQ" else nq_kh).setdefault(nq_hien, []).append(noi)
        elif truc:
            (kq if pha == "KQ" else kh)[truc].append(
                {"lv": lv_hien or linh_vuc(noi), "noi_dung": noi})

    return {"kq": kq, "kh": kh, "nq_kq": nq_kq, "nq_kh": nq_kh,
            "dat": dat, "chua": chua}


def main():
    data = {}
    for f in sorted(glob.glob(os.path.join(IN, "*", "*.docx"))):
        don_vi = os.path.basename(os.path.dirname(f))
        r = doc_mot(f)
        r["file"] = os.path.basename(f)
        data[don_vi] = r
        nkq = sum(len(v) for v in r["kq"].values())
        nkh = sum(len(v) for v in r["kh"].values())
        print(f"{don_vi:22s} KQ={nkq:3d} KH={nkh:3d} NQ={len(r['nq_kq'])+len(r['nq_kh']):2d} "
              f"dat={len(r['dat'])} chua={len(r['chua'])}")
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tk = sum(sum(len(v) for v in d["kq"].values()) for d in data.values())
    th = sum(sum(len(v) for v in d["kh"].values()) for d in data.values())
    print(f"\nTONG: {len(data)} don vi | {tk} y ket qua | {th} y ke hoach -> {OUT}")


if __name__ == "__main__":
    main()
