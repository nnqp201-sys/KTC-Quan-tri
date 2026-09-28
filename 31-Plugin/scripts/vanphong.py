# -*- coding: utf-8 -*-
"""Lop chuyen van phong cap don vi -> cap Truong.

Can cu: chu thich trong '00. Mau bao cao thang (cap Truong).docx':
  "{Luu y nguyen tac: chuyen van phong tu Phong sang van phong cap Truong,
    khong dung cac tu/cum tu nhu: Tham muu cho Lanh dao Truong..., phoi hop voi
    {cac don vi thuoc Truong...}"
Doi chieu thuc te BC-375 (da ban hanh): 0 lan "tham muu".
"""
import re

# Doi tac NGOAI Truong — "phoi hop voi" nhung doi tuong nay VAN GIU (BC-375 co dung)
NGOAI = (r"doanh nghiệp|công ty|UBND|Ủy ban|Sở |Ban Dân tộc|Đài |Báo |trường |Viện |"
         r"Trung tâm Y tế|bệnh viện|đối tác|địa phương|xã |phường |tỉnh |huyện|"
         r"cơ quan|đơn vị liên quan|các bên|CSGT|Công an|cảnh sát|Quân sự|Biên phòng|Liên đoàn|Tỉnh đoàn|Hội |Ngân hàng|Bảo hiểm|Kho bạc|Chi cục|Cục ")

# Dong tu di sau "tham muu" -> bo han "tham muu", giu dong tu
VERB_SAU = (r"ban hành|xây dựng|triển khai|tổ chức|thực hiện|đề xuất|trình|rà soát|"
            r"hoàn thiện|sửa đổi|bổ sung|cập nhật|phê duyệt|góp ý|kiểm tra|lập|"
            r"soạn thảo|công bố|hướng dẫn|tổng hợp|báo cáo|đăng ký|theo dõi|đôn đốc|"
            r"tiếp nhận|giải quyết|quản lý|chuẩn bị|tham gia|phát động|tuyên truyền|"
            r"sơ kết|tổng kết|nghiệm thu|thẩm định|xét|chấm|cấp|thu thập|bố trí|"
            r"phân công|điều chỉnh|thay thế|bãi bỏ|hợp nhất|giám sát|đánh giá")

# Danh tu di sau "tham muu" -> doi thanh "xay dung <danh tu>"
NOUN_SAU = (r"văn bản|nội dung|kế hoạch|quy chế|quy định|đề án|báo cáo|tờ trình|"
            r"quyết định|hồ sơ|phương án|chương trình|thông báo|hướng dẫn|đề cương")

# Ten don vi NOI BO — liet ke tuong minh de khong an nham noi dung phia sau
NOI_BO = (
    r"Phòng\s+TCCB\s*&\s*CTHSSV|Phòng\s+Tổ chức cán bộ và Công tác học sinh,?\s*sinh viên|"
    r"Phòng\s+QLĐT\s*&\s*BĐCL|Phòng\s+Quản lý [Đđ]ào tạo và Bảo đảm chất lượng|"
    r"Phòng\s+TH\s*-\s*HC\s*&\s*QT|Phòng\s+Tổng hợp\s*-\s*Hành chính và Quản trị|"
    r"Phòng\s+QLKHCN\s*&\s*HTPT|Phòng\s+Quản lý khoa học công nghệ và Hợp tác phát triển|"
    r"Phòng\s+TC\s*-\s*KT|Phòng\s+Tài chính\s*-\s*Kế toán|"
    r"Khoa\s+CKHCB|Khoa\s+các Khoa học cơ bản|Khoa\s+Sư phạm|"
    r"Khoa\s+KT\s*&\s*NL|Khoa\s+Kinh tế và Nông [LlÂâ]âm|Khoa\s+Kinh tế\s*-\s*Nông lâm|"
    r"Khoa\s+KT\s*&\s*CN|Khoa\s+Kỹ thuật và Công nghệ|"
    r"Khoa\s+Y\s*[–-]\s*Dược|Khoa\s+ĐT\s*&\s*SHLX|Khoa\s+Đào tạo và Sát hạch lái xe|"
    r"Ban\s+Truyền thông|các bộ môn|các khoa|các phòng|các đơn vị thuộc Trường|"
    r"Bộ môn\s+[A-ZĐ][^\s,;]*(\s*&\s*[A-ZĐ][^\s,;]*)?"
)


# Chu ngu cap don vi dung dau cau -> "Nha truong".
# Lookahead chu THUONG de khong an nham ten rieng ("Khoa Ky thuat va Cong nghe").
CHU_NGU = re.compile(
    r"^(BCH\s+CĐCS\s+Trường|CĐCS\s+Trường|Công đoàn cơ sở Trường|Ban Chấp hành\s+CĐCS"
    r"|Ban Truyền thông|Đoàn Thanh niên Trường|Chi bộ|Khoa|Phòng|Bộ môn)"
    r"\s+(?=[a-zàáâãèéêìíòóôõùúăđĩũơưăạ])", re.U)
# KHONG dua "Ban"/"Don vi" tran vao CHU_NGU: "Ban hanh Ke hoach..." se bi
# nuot chu "Ban" -> "Nha truong hanh Ke hoach". Da mac loi nay mot lan.


def chu_ngu_truong(t: str) -> str:
    return CHU_NGU.sub("Nhà trường ", t)


def cap_truong(s: str) -> str:
    """Chuyen 1 cum mo ta cong viec cap don vi sang van phong cap Truong."""
    t = " ".join(s.split())
    t = chu_ngu_truong(t)

    # 1. "tham mưu cho Lãnh đạo Trường/Hiệu trưởng ..." -> bo cum tham mưu
    t = re.sub(r"tham\s*mưu\s*(,|và)?\s*(đề xuất\s*)?(cho\s+)?"
               r"(Lãnh đạo\s+Trường|Hiệu trưởng|Ban Giám hiệu|Nhà trường|Trường)\s*",
               "", t, flags=re.I)

    # 2. "tham mưu <động từ>" -> bo "tham mưu", giu dong tu
    t = re.sub(rf"tham\s*mưu\s*(,|và)?\s*(?=({VERB_SAU}))", "", t, flags=re.I)

    # 3. "tham mưu <danh từ>" -> "xây dựng <danh từ>"
    t = re.sub(rf"tham\s*mưu\s+(?=({NOUN_SAU}))", "xây dựng ", t, flags=re.I)

    # 3b. Con lai: bo han "tham mưu" thay vi doan bua -> tranh sai ngu phap
    t = re.sub(r"tham\s*mưu\s*(,|và)?\s*", "", t, flags=re.I)

    # 4. "phối hợp (với) <đơn vị NỘI BỘ>" -> bo dung ten don vi, GIU lai hanh dong
    t = re.sub(rf"(phối hợp|cùng)\s*(với\s*)?({NOI_BO})\s*(,|;|và)?\s*", "", t, flags=re.I)

    # 5. "trình/đề xuất Lãnh đạo Trường|Hiệu trưởng <động từ>" -> bo cum trinh
    t = re.sub(rf"(trình|đề xuất)\s+((Phó\s+)?Hiệu trưởng|Lãnh đạo\s+(Trường|khoa|phòng|đơn vị)|Ban Giám hiệu|Trưởng khoa|Trưởng phòng)\s*"
               rf"(xem xét\s*)?(,|và)?\s*(?=({VERB_SAU}))", "", t, flags=re.I)
    t = re.sub(r"(trình|đề xuất)\s+((Phó\s+)?Hiệu trưởng|Lãnh đạo\s+(Trường|khoa|phòng|đơn vị)|Ban Giám hiệu|Trưởng khoa|Trưởng phòng)\s*",
               "", t, flags=re.I)

    # 6. Don dep
    t = re.sub(r"\s{2,}", " ", t)
    t = re.sub(r"^\s*(,|;|và)\s*", "", t)
    t = re.sub(r"\s+(,|;)", r"\1", t)
    return t.strip(" ,;")


def kiem_tra(t: str):
    """Tra ve danh sach vi pham con lai."""
    loi = []
    if re.search(r"tham\s*mưu", t, re.I):
        loi.append("còn 'tham mưu'")
    m = re.search(r"phối hợp\s*(với)?\s*((các\s+)?(Phòng|Khoa|Bộ môn)\s+\S+)", t, re.I)
    if m and not re.search(NGOAI, m.group(2), re.I):
        loi.append(f"phối hợp nội bộ: {m.group(2)[:40]}")
    if re.search(r"(trình|đề xuất)\s+((Phó\s+)?Hiệu trưởng|Lãnh đạo|Ban Giám hiệu|Trưởng khoa|Trưởng phòng)", t, re.I):
        loi.append("còn 'trình/đề xuất Lãnh đạo'")
    if CHU_NGU.match(t):
        loi.append(f"chủ ngữ cấp đơn vị: {t[:28]}")
    return loi


if __name__ == "__main__":
    THU = [
        "tham mưu văn bản, đề xuất có liên quan đến công tác truyền thông",
        "tham mưu nội dung và Báo cáo những điểm mới của các Nghị định",
        "rà soát, tham mưu đăng ký loại bỏ các ngành, nghề đào tạo không còn phù hợp",
        "tham mưu cho Lãnh đạo Trường ban hành Quy chế chi tiêu nội bộ",
        "phối hợp Phòng Quản lý đào tạo và Bảo đảm chất lượng xét điều kiện dự thi",
        "phối hợp với doanh nghiệp tổ chức thực hành, thực tập",
        "trình Hiệu trưởng phê duyệt kế hoạch tuyển sinh năm 2026",
    ]
    for s in THU:
        r = cap_truong(s)
        print(f"  TRUOC: {s}\n  SAU  : {r}\n  loi  : {kiem_tra(r) or 'sach'}\n")
