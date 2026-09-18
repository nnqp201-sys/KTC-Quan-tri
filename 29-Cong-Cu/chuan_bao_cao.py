# -*- coding: utf-8 -*-
"""Danh muc NHAN MUC CON co dinh cua bao cao thang cap Truong.

Nguon: `25-KTC-Bao-Cao/00. Mau bao cao thang (cap Truong).docx` — mau chinh thuc,
quy dinh SAN tung muc con va lay tu don vi nao. Danh muc duoc RUT THANG TU MAU,
khong go tay, de mau doi thi code doi theo.

Loi da mac 13-14/9/2026: tu sinh nhan tu ten noi ham TB 817 -> ra
"Cong tac phap che, thanh tra, kiem tra va kiem soat noi bo", "Cong tac khac"
(12 lan)... Chi 5/28 nhan nam trong danh muc mau. Dap an da co san trong mau.
"""
from __future__ import annotations

import os
import re

from docx import Document

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAU = os.path.join(DU_AN, "25-KTC-Bao-Cao", "00. Mau bao cao thang (cap Truong).docx")

# Tu khoa chon nhan TRONG PHAM VI tung muc. Xep tu cu the den tong quat;
# phan tu cuoi moi muc la nhan MAC DINH khi khong khop gi.
LUAT = {
    1: [("Công tác tuyển sinh",
         r"tuyển sinh|trúng tuyển|nhập học|tiếp sinh|xét tuyển|hướng nghiệp|chỉ tiêu tuyển"),
        ("Công tác bảo đảm chất lượng",
         r"bảo đảm chất lượng|kiểm định|tự đánh giá|minh chứng|chuẩn cơ sở giáo dục"),
        ("Công tác khảo thí",
         r"khảo thí|ngân hàng đề|chấm thi|nhập điểm|thi kết thúc|thi lại|sát hạch|"
         r"văn bằng|chứng chỉ|xét tốt nghiệp"),
        ("Công tác tổ chức, cán bộ",
         r"tổ chức cán bộ|bổ nhiệm|vị trí việc làm|biên chế|tuyển dụng viên chức|"
         r"nâng lương|thi đua|khen thưởng|viên chức, người lao động|đào tạo, bồi dưỡng"),
        ("Công tác đào tạo",
         r"đào tạo|giảng dạy|thời khóa biểu|tốt nghiệp|chương trình|giáo trình|"
         r"liên thông|thực tập|mở lớp|kết quả học tập|học kỳ|năm học|học liệu"),
        ("Công tác kế hoạch, tổng hợp", r".")],
    2: [("Công tác Kiểm tra, giám sát",
         r"kiểm tra|giám sát|thanh tra|sĩ số|dự giờ|kiểm soát nội bộ|pháp chế"),
        ("Về thể chế", r".")],
    3: [],                                   # mau KHONG chia muc con o muc 3
    4: [("Chấp hành kỷ cương hành chính",
         r"kỷ cương hành chính|kỷ luật, kỷ cương|giờ giấc làm việc|văn hóa công sở"),
        ("Công tác Đảng, Công đoàn, Đoàn Thanh niên",
         r"Công đoàn|Đoàn Thanh niên|Hội Sinh viên|đoàn viên|thanh niên|nữ công|CĐCS"),
        ("Công tác xây dựng Đảng", r".")],
    5: [("Công tác truyền thông",
         r"truyền thông|biên tập ảnh, tin, bài|tin, bài|infographic|banner|"
         r"fanpage|thước phim|video|sản phẩm truyền thông"),
        ("Công tác Tài chính",
         r"tài chính|thanh toán|tiền lương|dự toán|quyết toán|học phí|kinh phí|"
         r"kế toán|định mức kinh tế|giá dịch vụ|tự chủ"),
        ("Công tác quản lý cơ sở vật chất",
         r"cơ sở vật chất|tài sản|sửa chữa|thiết bị|phòng học|xưởng|đất đai|"
         r"ký túc xá|mua sắm|bảo dưỡng|môi trường|xanh hóa|tiết kiệm điện"),
        ("Công tác an sinh giáo dục", r".")],
    6: [("Về hoạt động Đối ngoại và Hợp tác",
         r"đối ngoại|hợp tác quốc tế|quốc tế|\bLào\b|\bMOU\b|người nước ngoài|hội nhập"),
        ("Về hoạt động hợp tác phát triển",
         r"doanh nghiệp|hợp tác phát triển|dân vận|địa phương|nông nghiệp|"
         r"lao động nông thôn|cộng đồng|khởi nghiệp"),
        ("Về Quốc phòng - An ninh", r".")],
}


def _khoa(t: str) -> str:
    """Khoa chuan hoa de gop bien the cua CUNG mot nhan.

    Mau dung chu khac nhau giua Phan I (ket qua) va Phan III (ke hoach):
    "Cong tac Truyen thong" / "Ve cong tac Truyen thong";
    "Cong tac quan ly co so vat chat" / "Cong tac Quan ly co so vat chat".
    """
    t = re.sub(r"^(về|vế)\s+", "", t.strip(), flags=re.I)
    return re.sub(r"[^\w]", "", t.lower())


def _rut_tu_mau() -> dict:
    """Rut danh muc nhan theo tung muc tu tep mau chinh thuc."""
    if not os.path.exists(MAU):
        return {}
    d = Document(MAU)
    ra, muc = {}, None
    for p in d.paragraphs:
        t = " ".join(p.text.split())
        m = re.match(r"^([1-7])\.\s+\S", t)
        if m:
            muc = int(m.group(1))
            ra.setdefault(muc, [])
            continue
        if muc:
            m = re.match(r"^\*\s*([^:\[]{3,60}):", t)
            if m:
                ten = m.group(1).strip()
                if ten.startswith("Nghị quyết"):
                    continue
                if _khoa(ten) not in {_khoa(x) for x in ra[muc]}:
                    ra[muc].append(ten)     # giu dang o Phan I lam chinh
    return ra


DANH_MUC_MAU = _rut_tu_mau()


def danh_muc(truc: int) -> list:
    """Nhan hop le cua mot muc — uu tien danh muc rut tu MAU."""
    tu_mau = DANH_MUC_MAU.get(truc, [])
    if tu_mau:
        return tu_mau
    return [t for t, _ in LUAT.get(truc, [])]


def co_muc_con(truc: int) -> bool:
    return bool(danh_muc(truc))


def nhan(s: str, truc: int) -> str | None:
    """Chon nhan muc con cho mot y, TRONG PHAM VI danh muc cua muc do.

    Tra ve None neu muc khong chia muc con (muc 3 theo mau).
    """
    luat = LUAT.get(truc, [])
    if not luat:
        return None
    hop_le = danh_muc(truc)
    tra = {_khoa(x): x for x in hop_le}
    for ten, pat in luat:
        if pat == r".":
            continue
        if re.search(pat, s, re.I):
            return tra.get(_khoa(ten), hop_le[-1])
    mac_dinh = next((t for t, p in luat if p == r"."), None)
    return tra.get(_khoa(mac_dinh or ""), hop_le[-1] if hop_le else None)


def kiem_danh_muc() -> list:
    """Doi chieu LUAT voi danh muc rut tu mau. Tra ve danh sach lech."""
    lech = []
    for truc in range(1, 7):
        mau = {_khoa(x) for x in DANH_MUC_MAU.get(truc, [])}
        code = {_khoa(t) for t, _ in LUAT.get(truc, [])}
        if mau and code != mau:
            for x in sorted(code - mau):
                lech.append(f"mục {truc}: code có '{x}' — mẫu KHÔNG có")
            for x in sorted(mau - code):
                lech.append(f"mục {truc}: mẫu có '{x}' — code THIẾU")
    return lech


if __name__ == "__main__":
    print("Danh mục nhãn mục con rút từ mẫu chính thức:\n")
    for truc in range(1, 8):
        ds = DANH_MUC_MAU.get(truc, [])
        print(f"  Mục {truc}: {len(ds)} mục con" + (" (không chia mục con)" if not ds else ""))
        for x in ds:
            print(f"      * {x}")
    lech = kiem_danh_muc()
    print(f"\nĐối chiếu LUẬT ↔ MẪU: {'KHỚP' if not lech else f'{len(lech)} chỗ lệch'}")
    for x in lech:
        print("   !", x)
