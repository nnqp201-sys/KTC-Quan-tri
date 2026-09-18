# -*- coding: utf-8 -*-
"""Trich 38 noi ham 6 truc tu TB 817 va dung bo phan loai.

Nguon: KTC-Database/02-KTC-Regulations/05. TB-817-Noi-ham-06-Truc-...docx
Bo phan loai dung CHINH mo ta noi ham lam tu vung (khong tu dat tu khoa).
"""
import json, math, os, re
from docx import Document

TB817 = (r"D:\.CLAUDE code\KTC-Database\02-KTC-Regulations"
         r"\05. TB-817-Noi-ham-06-Truc-Ket-qua-trong-tam-Truong-CDKT.docx")
HERE = os.path.dirname(os.path.abspath(__file__))

STOP = set("""va của cho các được theo trong với tại về những một số như là có không
đã và/hoặc khi từ đến trên dưới ra vào này đó nếu thì mà nhưng hoặc cùng bằng
việc công tác thực hiện triển khai tổ chức quản lý xây dựng bảo đảm nâng cao
tăng cường tiếp tục hoàn thành đơn vị nhà trường trường""".split())


def chuan(s: str) -> list:
    s = re.sub(r"[^\w\sÀ-ỹ]", " ", s.lower())
    return [w for w in s.split() if len(w) > 2 and w not in STOP]


def trich() -> list:
    d = Document(TB817)
    tb = max(d.tables, key=lambda t: len(t.rows))
    ra, truc = [], None
    for r in tb.rows[1:]:
        c = [x.text.strip() for x in r.cells]
        m = re.match(r"Trục\s+(\d)\s*:\s*(.+?)\s*\(có", c[1], re.S)
        if m:
            truc = int(m.group(1))
            ten_truc = " ".join(m.group(2).split())
            continue
        m = re.match(r"Nội hàm\s+(\d+)\.\s*(.+?):\s*(.+)", " ".join(c[1].split()), re.S)
        if m and truc:
            ra.append({"truc": truc, "ten_truc": ten_truc, "so": int(m.group(1)),
                       "ten": m.group(2).strip(), "mo_ta": m.group(3).strip(),
                       "chi_so": " ".join(c[2].split())})
    return ra


# Luat phan loai — neo vao CHINH TEN 38 noi ham cua TB 817, xep tu cu the
# den tong quat. Da thu bang tui-tu + IDF tren mo ta noi ham: SAI ro ret voi
# cau hanh chinh ngan (vd "tiep sinh, nhap hoc thi sinh trung tuyen" -> Truc 5),
# vi cum tu chuyen nganh bi tach thanh tu don. Khong dung cach do.
LUAT = [
    (1, 2, r"tuyển sinh|trúng tuyển|nhập học|tiếp sinh|xét tuyển|hướng nghiệp|chỉ tiêu tuyển"),
    (1, 4, r"bảo đảm chất lượng|kiểm định|tự đánh giá|minh chứng|chuẩn cơ sở giáo dục"),
    (1, 3, r"chương trình đào tạo|giáo trình|chuẩn đầu ra|học liệu|thời khóa biểu|"
           r"phân công giảng dạy|tiến độ đào tạo|tốt nghiệp|mở lớp|liên thông|"
           r"thực hành, thực tập|đào tạo|giảng dạy|dạy và học|kết quả học tập"),
    (1, 6, r"doanh nghiệp|gắn kết|tuyển dụng lao động"),
    (1, 1, r"chiến lược|quy hoạch|kế hoạch phát triển|đề án"),

    (2, 3, r"cải cách hành chính|thủ tục hành chính"),
    (2, 6, r"công khai|minh bạch|giải trình"),
    (2, 5, r"văn thư|lưu trữ|thống kê|báo cáo định kỳ|chuẩn hóa dữ liệu|cơ sở dữ liệu"),
    (2, 4, r"kiểm tra|giám sát|thanh tra|pháp chế|kiểm soát nội bộ|sĩ số"),
    (2, 1, r"quy chế|quy định|ban hành văn bản|sửa đổi, bổ sung|dự thảo văn bản|góp ý"),
    (2, 2, r"kế hoạch công tác|giao ban|phân công nhiệm vụ|danh mục công việc"),

    (3, 6, r"sở hữu trí tuệ|bản quyền"),
    (3, 5, r"an toàn thông tin|an ninh mạng|năng lực số|kỹ năng số"),
    (3, 3, r"chuyển đổi số|số hóa"),
    (3, 4, r"trí tuệ nhân tạo|\bAI\b|phần mềm|hạ tầng|công nghệ thông tin|nền tảng số"),
    (3, 2, r"sáng kiến|đổi mới sáng tạo|khởi nghiệp|cải tiến"),
    (3, 1, r"nghiên cứu khoa học|đề tài|hội thảo khoa học|chuyển giao công nghệ|khoa học"),

    (4, 7, r"thi đua|khen thưởng|danh hiệu|điển hình tiên tiến"),
    (4, 6, r"Công đoàn|Đoàn Thanh niên|Hội Sinh viên|đoàn viên|thanh niên"),
    (4, 5, r"dân vận|dân chủ|đối thoại"),
    (4, 4, r"khiếu nại|tố cáo|kỷ luật đảng"),
    (4, 3, r"bổ nhiệm|vị trí việc làm|biên chế|quy hoạch cán bộ|đánh giá xếp loại|"
           r"nâng lương|kỷ luật|tổ chức cán bộ|viên chức, người lao động"),
    (4, 2, r"Đảng ủy|chi bộ|đảng viên"),
    (4, 1, r"quán triệt|tuyên truyền|chính trị, tư tưởng|nghị quyết|"
           r"tham nhũng|tiêu cực|lãng phí"),

    (5, 6, r"môi trường|xanh hóa|tiết kiệm điện|tiết kiệm năng lượng"),
    (5, 3, r"tài chính|thanh toán|dự toán|quyết toán|học phí|tiền lương|tự chủ|"
           r"định mức kinh tế|kế toán|kinh phí|giá dịch vụ|chế độ, chính sách"),
    (5, 4, r"cơ sở vật chất|tài sản|thiết bị|sửa chữa|phòng học|xưởng|bảo dưỡng|"
           r"mua sắm|đất đai|ký túc xá"),
    (5, 2, r"học sinh, sinh viên|HSSV|chủ nhiệm|rèn luyện|học bổng|nội trú|ngoại trú|"
           r"người học|tân sinh viên|bếp ăn"),
    (5, 1, r"văn hóa công sở|văn hóa học đường|thương hiệu|quy tắc ứng xử|hệ giá trị"),
    (5, 7, r"an sinh|cộng đồng|từ thiện|địa phương|lao động nông thôn|xã hội"),

    (6, 4, r"hội nhập quốc tế|người nước ngoài|đoàn ra|đoàn vào"),
    (6, 3, r"đối ngoại|hợp tác quốc tế|\bMOU\b|Nam Lào|\bLào\b|quốc tế"),
    (6, 1, r"quốc phòng|quân sự"),
    (6, 2, r"an ninh|trật tự|bí mật nhà nước|phòng cháy|bảo vệ|an toàn trường học"),
]


BO_SUNG = [
    (90, "Công tác truyền thông",
     r"(công tác )?truyền thông|biên tập ảnh, tin, bài|sản phẩm truyền thông|"
     r"infographic|banner, poster|fanpage|thước phim"),
    (91, "Chấp hành kỷ cương hành chính",
     r"kỷ cương hành chính|kỷ luật, kỷ cương"),
]


class PhanLoai:
    """Chon noi ham bang luat tuong minh, uu tien luat dung truoc."""

    def __init__(self, nh: list):
        self.tra = {(x["truc"], x["so"]): x for x in nh}
        luat = list(LUAT)
        # Nhan BC-375 co dung ma TB 817 khong dat thanh noi ham rieng.
        # Dua vao BANG LUAT (so >= 90) de canh tranh theo vi tri khop nhu moi
        # luat khac — neu xet truoc thi bat ca cau chi thoang nhac "video".
        for t in range(1, 7):
            for so, ten, pat in BO_SUNG:
                self.tra[(t, so)] = {"truc": t, "so": so, "ten": ten}
                luat.append((t, so, pat))
        self.luat = [(t, s, re.compile(p, re.I)) for t, s, p in luat]

    def __call__(self, s: str, truc: int = 0):
        """truc=0: xet moi luat. truc=1..6: CHI xet noi ham cua truc do.

        Han che theo truc la bat buoc khi dat nhan muc con trong bao cao:
        neu khong, muc "Xay dung Dang" co the nhan nhan "Cong tac dao tao".
        """
        # Chon luat co vi tri khop SOM NHAT trong cau, khong phai luat dung
        # truoc trong bang: dau cau moi la chu de that cua y.
        tot = None
        for uu, (t, so, rx) in enumerate(self.luat):
            if truc and t != truc:
                continue
            m = rx.search(s)
            if m and (tot is None or (m.start(), uu) < tot[0]):
                tot = ((m.start(), uu), (t, so), m.group(0))
        if tot:
            return self.tra[tot[1]], tot[2]
        return None, ""

    # Nhan BC-375 co dung nhung TB 817 khong dat thanh noi ham rieng.
    # Xet TRUOC noi ham vi day la nhan chuyen biet, de bi luat chung nuot.
    def nhan(self, s: str, truc: int) -> str:
        """Nhan muc con kieu BC-375: '* Cong tac ...'"""
        nh, _ = self(s, truc)
        if not nh:
            return "Công tác khác"
        if nh["so"] >= 90:              # nhan bo sung kieu BC-375
            return nh["ten"]
        ten = nh["ten"]
        return ten if ten.lower().startswith("công tác") else "Công tác " + ten[0].lower() + ten[1:]


if __name__ == "__main__":
    nh = trich()
    json.dump(nh, open(os.path.join(HERE, "noi_ham.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    dem = {}
    for x in nh:
        dem[x["truc"]] = dem.get(x["truc"], 0) + 1
    print("Tong noi ham:", len(nh), "| theo truc:", dem)

    pl = PhanLoai(nh)
    THU = [
        "Phối hợp triển khai tiếp sinh, nhập học thí sinh trúng tuyển trình độ cao đẳng",
        "Triển khai chuẩn hóa dữ liệu cơ sở vật chất, diện tích, chỗ ngồi của các phòng học",
        "Phân công nhà giáo chủ nhiệm các lớp tuyển sinh năm 2026",
        "Tiếp tục thu thập, nộp minh chứng tự đánh giá chất lượng chương trình đào tạo",
        "Triển khai cập nhật chương trình đào tạo đối với các lớp K9",
        "Tích cực tham gia góp ý các dự thảo văn bản của Trường",
        "Bảo đảm an toàn, an ninh trường học và bảo mật thông tin",
        "Thực hiện thanh toán lương và các chế độ chính sách cho viên chức",
    ]
    for s in THU:
        x, kw = pl(s)
        ten = f"T{x['truc']}.{x['so']} {x['ten']}" if x else "(khong khop)"
        print(f"  {ten[:44]:46s} [{kw[:20]:20s}] <- {s[:48]}")
