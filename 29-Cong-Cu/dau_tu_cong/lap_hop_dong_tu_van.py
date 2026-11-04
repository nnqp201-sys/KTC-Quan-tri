# -*- coding: utf-8 -*-
"""Dựng hợp đồng tư vấn (theo NĐ 210/2026, mẫu QĐ 1040/QĐ-BXD) và biên bản thương thảo (Phụ lục 4C TT 79/2025/TT-BTC)
cho hai gói tư vấn chuẩn bị đầu tư: KS (khảo sát, lập BCKTKT) và QLDA.

Số liệu gói thầu đọc từ du-an_CLC-2026-2030.yaml. Chỗ chưa có nguồn để trống dạng "…………" (xem báo cáo giao kèm).
Chạy:  python -X utf8 lap_hop_dong_tu_van.py [--out THƯ_MỤC] [--goi KS|QLDA] [--chi hd|bb]
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from du_an import ket_qua, tai  # noqa: E402
from vb_lib import bang_chu, vnd  # noqa: E402
from vb_mau import VanBanMau as VanBan  # noqa: E402

D = tai()
TEN_DA = D["du_an"]["ten"]
VB = D["van_ban"]
CH = "…………"  # chỗ trống chờ điền

BEN_A = dict(
    ten="Trường Cao đẳng Kon Tum", dd="Ông Lê Trí Khải", cv="Hiệu trưởng",
    dc="Số 14, đường Ngụy Như Kon Tum, phường Đăk Cấm, tỉnh Quảng Ngãi",
    tk="9552.2.8222808.51", nh="Kho bạc Nhà nước khu vực XV - Phòng giao dịch số 23",
    qhns="1049264", mst="6101241450", dt="02603 915039", fax="02603 915039")

NGAY_TT = "22/10/2026"  # ngày hoàn thiện hợp đồng ghi trên Hệ thống mạng đấu thầu quốc gia


def _dd(s):
    ten, cv = s.split(" - ", 1)
    return ten, cv


def ben_b(g):
    ten, cv = _dd(g["dd"])
    return dict(ten=g["nt"], mst=g["mst"], dc=g["dc"], dd=ten, cv=cv, gcn=g["gcn"])


def _so_tien(g):
    return so(g["gia"])


def so(s):
    return int(re.sub(r"\D", "", s))


# ---------------------------------------------------------------- cấu hình từng gói
_GKS, _GQL = so(D['goi_thau']['KS']['gia']), so(D['goi_thau']['QLDA']['gia'])
KS26 = round(260_000_000 * _GKS / (_GKS + _GQL))  # vốn 2026 (260 triệu) chia theo tỷ lệ giá hợp đồng
QL26 = 260_000_000 - KS26


def cau_hinh(ma):
    if ma == "KS":
        g = D["goi_thau"]["KS"]
        b = ben_b(g)
        b.update(tk=CH, nh=CH, dt=CH, mail=CH)
        gia = so(g["gia"])
        a_ks, a_tk = [int(x.replace(".", "")) for x in re.findall(r"\d{1,3}(?:\.\d{3})+", g["pt_tom_tat"])[:2]]
        tu = (gia * 30 + 50) // 100  # 30% giá hợp đồng, tạm ứng hết trong năm 2026
        return dict(
            ma="KS", g=g, b=b, gia=gia, ten_goi="Tư vấn khảo sát xây dựng, lập Báo cáo kinh tế - kỹ thuật Dự án",
            qd=VB["qd_2374"], don="Đơn xin nhận thầu số 07/ĐNT-TPL ngày 14/10/2026", ten_ngan="Trường Phát Land",
            a_ks=a_ks, a_tk=a_tk, tu=tu, ty_le_tu=30, tu26=KS26, tu27=tu - KS26, ql_tu26=QL26, so_hd="Số:        /2026/HĐ-TV",
            dia_diem_tt="Phòng họp, Khu Hiệu bộ, Trụ sở chính Trường Cao đẳng Kon Tum, " + BEN_A["dc"],
            file_hd="HD_Goi-KS-BCKTKT_Truong-Phat-Land_20261028_v2.docx",
            file_bb="BBTT_Goi-KS-BCKTKT_Truong-Phat-Land_20261028_v2.docx",
            file_dc="BBDC_Goi-KS-BCKTKT_Truong-Phat-Land_20261028_v2.docx",
            ghi_nhan=["Nhà thầu có tên trên Hệ thống mạng đấu thầu quốc gia (mã định danh vn6101274368).",
                      "Nhà thầu đã bổ sung hồ sơ bản giấy.",
                      "Gói thầu là cải tạo, sửa chữa nên không yêu cầu nhân sự thiết kế kiến trúc.",
                      "Nhân sự chủ chốt, chứng chỉ hành nghề cá nhân và chứng chỉ năng lực của tổ chức kê khai trong hồ sơ năng lực khớp với bản chụp tài liệu nhà thầu cung cấp."])
    g = D["goi_thau"]["QLDA"]
    b = ben_b(g)
    b.update(tk="115002992933", nh="Ngân hàng TMCP Công thương Việt Nam (VietinBank) - Chi nhánh Kon Tum", dt=CH, mail=CH)
    gia = so(g["gia"])
    tu = 200_229_906  # 30% giá hợp đồng — số Bên A và Bên B đã thống nhất trong biên bản thương thảo QLDA
    gia_ks = so(D['goi_thau']['KS']['gia'])
    tu_ks = (gia_ks * 30 + 50) // 100
    tu26 = QL26  # năm 2026: phần vốn 260 triệu chia theo tỷ lệ giá hợp đồng
    tu27 = tu - tu26  # năm 2027: phần còn lại để đủ 30%
    return dict(
        ma="QLDA", g=g, b=b, gia=gia, ten_goi="Tư vấn quản lý dự án", qd=VB["qd_2375"],
        don="Đơn xin nhận thầu số 09/ĐNT-QLDA ngày 19/10/2026", ten_ngan="Thành Vinh", tu=tu, ty_le_tu=30, tu_ks=tu_ks, tu26=tu26, tu27=tu27, ks_tu26=KS26,
        so_hd="Số:        /2026/HĐ-TVQLDA",
        dia_diem_tt="Phòng họp tầng 2, Khu Hiệu bộ, Trụ sở chính Trường Cao đẳng Kon Tum, " + BEN_A["dc"],
        file_hd="HD_Goi-QLDA_Thanh-Vinh_20261028_v2.docx", file_bb="BBTT_Goi-QLDA_Thanh-Vinh_20261028_v2.docx",
        file_dc="BBDC_Goi-QLDA_Thanh-Vinh_20261028_v2.docx",
        ghi_nhan=["Nhà thầu có tên trên Hệ thống mạng đấu thầu quốc gia (mã định danh vn6100895732).",
                  "Nhà thầu đã bổ sung hồ sơ bản giấy.",
                  "Ông Ngô Thanh Hùng đồng thời là Chủ tịch Hội đồng quản trị và Giám đốc, là người đại diện theo pháp luật của Công ty.",
                  "Nhân sự chủ chốt, chứng chỉ hành nghề cá nhân và chứng chỉ năng lực của tổ chức kê khai trong hồ sơ năng lực khớp với bản chụp tài liệu nhà thầu cung cấp."])


def can_cu_chung(c):
    ten_goi = c["ten_goi"]
    return [
        "Căn cứ Bộ luật Dân sự ngày 24/11/2015;",
        "Căn cứ Luật Xây dựng ngày 10/12/2025;",
        "Căn cứ Luật Đấu thầu ngày 23/6/2023 (hợp nhất tại Văn bản hợp nhất số 74/VBHN-VPQH ngày 25/3/2026);",
        "Căn cứ Nghị định số 210/2026/NĐ-CP ngày 15/6/2026 của Chính phủ quy định chi tiết và hướng dẫn thi hành một số điều của Luật Xây dựng về hợp đồng xây dựng;",
        "Căn cứ Nghị định số 207/2026/NĐ-CP ngày 15/6/2026 của Chính phủ quy định chi tiết một số nội dung về quản lý chất lượng, thi công xây dựng và bảo trì công trình xây dựng;",
        "Căn cứ Nghị định số 217/2026/NĐ-CP ngày 19/6/2026 của Chính phủ quy định chi tiết một số điều của Luật Xây dựng về quản lý hoạt động xây dựng;",
        "Căn cứ Nghị định số 206/2026/NĐ-CP ngày 15/6/2026 của Chính phủ quy định chi tiết về quản lý chi phí đầu tư xây dựng;",
        "Căn cứ Nghị định số 212/2026/NĐ-CP ngày 17/6/2026 của Chính phủ quy định về điều kiện năng lực hoạt động xây dựng, Hệ thống thông tin, Cơ sở dữ liệu quốc gia về hoạt động xây dựng;",
        "Căn cứ Nghị định số 214/2025/NĐ-CP ngày 04/8/2025 của Chính phủ quy định chi tiết một số điều và biện pháp thi hành Luật Đấu thầu về lựa chọn nhà thầu (hợp nhất tại Văn bản hợp nhất số 36/2026/VBHN-NĐ-BTC ngày 23/9/2026);",
        "Căn cứ Nghị định số 254/2025/NĐ-CP ngày 26/9/2025 của Chính phủ quy định về quản lý, thanh toán vốn đầu tư công;",
        "Căn cứ Thông tư số 79/2025/TT-BTC ngày 04/8/2025 của Bộ trưởng Bộ Tài chính hướng dẫn việc cung cấp, đăng tải thông tin về đấu thầu và mẫu hồ sơ đấu thầu trên Hệ thống mạng đấu thầu quốc gia;",
        f"Căn cứ Quyết định số {VB['qd_805']['so']} ngày {VB['qd_805']['ngay']} của Ủy ban nhân dân tỉnh Quảng Ngãi phân bổ kế hoạch vốn đầu tư công và kinh phí thường xuyên năm 2026 thực hiện Chương trình mục tiêu quốc gia xây dựng nông thôn mới, giảm nghèo bền vững và phát triển kinh tế - xã hội vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026 - 2035, giai đoạn I: Từ năm 2026 đến năm 2030 trên địa bàn tỉnh Quảng Ngãi;",
        f"Căn cứ Quyết định số {VB['qd_2161']['so']} ngày {VB['qd_2161']['ngay']} của Hiệu trưởng Trường Cao đẳng Kon Tum phân bổ chi tiết kế hoạch đầu tư công năm 2026 thực hiện Chương trình mục tiêu quốc gia xây dựng nông thôn mới, giảm nghèo bền vững và phát triển kinh tế - xã hội vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026 - 2035, giai đoạn I: Từ năm 2026 đến năm 2030;",
        f"Căn cứ Quyết định số {VB['qd_2158']['so']} ngày {VB['qd_2158']['ngay']} của Hiệu trưởng Trường Cao đẳng Kon Tum phê duyệt nhiệm vụ và dự toán kinh phí chuẩn bị đầu tư Dự án “{TEN_DA}”;",
        f"Căn cứ Quyết định số {VB['qd_2236']['so']} ngày {VB['qd_2236']['ngay']} của Hiệu trưởng Trường Cao đẳng Kon Tum phê duyệt Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư Dự án “{TEN_DA}”;",
    ]


def can_cu_ket_qua(c):
    q = c["qd"]
    return [
        f"Căn cứ Quyết định số {q['so']} ngày {q['ngay']} của Hiệu trưởng Trường Cao đẳng Kon Tum phê duyệt kết quả lựa chọn nhà thầu gói thầu “{c['ten_goi']}” thuộc Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư Dự án “{TEN_DA}”;",
        f"Căn cứ {c['don']} kèm hồ sơ năng lực của {c['b']['ten']};",
        f"Căn cứ Biên bản đối chiếu tài liệu ngày {NGAY_TT} giữa Trường Cao đẳng Kon Tum và {c['b']['ten']};",
        f"Căn cứ Biên bản thương thảo, hoàn thiện hợp đồng ngày {NGAY_TT} giữa Trường Cao đẳng Kon Tum và {c['b']['ten']};",
        "Căn cứ các quy định pháp luật, văn bản liên quan khác.",
    ]


# ---------------------------------------------------------------- tiện ích dựng
def khoi_ben(v, a, ten_vai, kieu="HD"):
    v.p(f"{ten_vai}", bold=True, indent=0, sau=2, giu=True)
    if kieu == "HD":
        dong = [("Tên giao dịch", a["ten"]),
                ("Đại diện", f"{a['dd']}  -  Chức vụ: {a['cv']}"),
                ("Địa chỉ", a["dc"])]
    else:  # đúng bố cục Phụ lục 4C: Đại diện, Chức vụ, Địa chỉ, Điện thoại
        dong = [("Đại diện", a["dd"]), ("Chức vụ", a["cv"]), ("Địa chỉ", a["dc"])]
    if kieu == "HD":
        dong += [("Tài khoản", f"{a['tk']}, tại {a['nh']}")]
        if a.get("qhns"):
            dong += [("Mã quan hệ ngân sách", a["qhns"])]
        dong += [("Mã số thuế", a["mst"])]
        if a.get("gcn"):
            dong += [("Đăng ký kinh doanh", a["gcn"])]
        dong += [("Điện thoại", a["dt"] + (f";  Fax: {a['fax']}" if a.get("fax") else "") + (f";  E-mail: {a['mail']}" if a.get("mail") else ""))]
    else:
        dong += [("Điện thoại", a["dt"] + (f";  Fax: {a['fax']}" if a.get("fax") else ""))]
    for k, t in dong:
        v.p(f"{k}: {t}", indent=0, trai=0.8, sau=1, justify=False)


def muc(v, items, tien_to=None):
    """items: danh sách chuỗi; chuỗi bắt đầu bằng '  ' (2 dấu cách) là mục con thụt vào."""
    for t in items:
        if t.startswith("  "):
            v.p(t.strip(), indent=0, trai=1.0, sau=3)
        else:
            v.p(t, indent=1.0, sau=4)


def chu_ky_hd(v, c, bb=False):
    a_lbl = "ĐẠI DIỆN CHỦ ĐẦU TƯ" if bb else "ĐẠI DIỆN BÊN GIAO THẦU"
    b_lbl = "ĐẠI DIỆN NHÀ THẦU" if bb else "ĐẠI DIỆN BÊN NHẬN THẦU"
    cv_b = c["b"]["cv"].split(" kiêm ")[-1] if " kiêm " in c["b"]["cv"] else c["b"]["cv"]
    # bố cục theo mẫu của Trường: người đứng đầu Trường ở bên phải
    v.ky(b_lbl, cv_b.upper(), c["b"]["dd"].replace("Ông ", ""),
         a_lbl, "HIỆU TRƯỞNG", BEN_A["dd"].replace("Ông ", ""),
         None)  # phòng TC-KT (29/10): bỏ khối "Nơi nhận" khỏi hợp đồng, biên bản


# ---------------------------------------------------------------- hợp đồng
def dung_hd(c, thu_muc):
    v = VanBan()
    b = c["b"]
    g = c["g"]
    gia = c["gia"]
    ks = c["ma"] == "KS"
    v.dau(c["so_hd"], "Quảng Ngãi, ngày       tháng       năm 2026", "HỢP ĐỒNG TƯ VẤN XÂY DỰNG",
          f"Gói thầu: {c['ten_goi']}\nThuộc Dự án “{TEN_DA}”")

    v.tieu_de("PHẦN 1. THÔNG TIN GIAO DỊCH")
    v.p("Hôm nay, ngày       tháng       năm 2026, tại Trụ sở chính Trường Cao đẳng Kon Tum, chúng tôi gồm các bên dưới đây:")
    khoi_ben(v, BEN_A, "1. Bên giao thầu (gọi tắt là Bên A):")
    khoi_ben(v, b, "2. Bên nhận thầu (gọi tắt là Bên B):")
    v.p(f"Hai bên cùng thống nhất ký hợp đồng tư vấn xây dựng gói thầu “{c['ten_goi']}” thuộc Dự án “{TEN_DA}” như sau:")

    v.tieu_de("PHẦN 2. CÁC CĂN CỨ GIAO KẾT HỢP ĐỒNG")
    for t in can_cu_chung(c) + can_cu_ket_qua(c):
        v.p(t, italic=True, indent=1.0, sau=3)

    v.tieu_de("PHẦN 3. CÁC ĐIỀU KHOẢN CỦA HỢP ĐỒNG")
    v.dieu("Điều 1. Giải thích từ ngữ")
    muc(v, [
        "1.1. “Hợp đồng” là văn bản này cùng các phụ lục kèm theo và các tài liệu quy định tại Điều 2.",
        f"1.2. “Dự án” là Dự án “{TEN_DA}”.",
        "1.3. “Công việc” là toàn bộ công việc Bên B phải thực hiện theo Điều 6 và Phụ lục số 1; “Sản phẩm” là báo cáo, hồ sơ, tài liệu Bên B phải lập và bàn giao theo hợp đồng.",
        "1.4. “Ngày” là ngày dương lịch; “ngày làm việc” là các ngày theo dương lịch, trừ ngày thứ bảy, chủ nhật, ngày nghỉ lễ, tết theo quy định của pháp luật.",
        "1.5. “BCKTKT” là Báo cáo kinh tế - kỹ thuật đầu tư xây dựng; “Kho bạc” là Kho bạc Nhà nước nơi Bên A giao dịch.",
    ])
    v.dieu("Điều 2. Hồ sơ hợp đồng và thứ tự ưu tiên")
    ho_so = ["văn bản hợp đồng này;", "các Phụ lục số 1, 2, 3, 4 kèm theo;",
             f"Quyết định số {c['qd']['so']} ngày {c['qd']['ngay']} phê duyệt kết quả lựa chọn nhà thầu;",
             f"Biên bản thương thảo, hoàn thiện hợp đồng và Biên bản đối chiếu tài liệu cùng ngày {NGAY_TT};", f"{c['don']} và hồ sơ năng lực của Bên B;",
             "Quyết định số 2158/QĐ-CĐKT ngày 29/9/2026 và " + ("nhiệm vụ khảo sát, nhiệm vụ thiết kế do Bên A phê duyệt;" if ks else "nhiệm vụ quản lý dự án do Bên A giao;"),
             "các tài liệu khác có liên quan do hai bên thống nhất."]
    muc(v, ["2.1. Hồ sơ hợp đồng gồm:"] + [f"  {chr(97 + i)}) {t}" for i, t in enumerate(ho_so)])
    muc(v, ["2.2. Thứ tự ưu tiên áp dụng khi các tài liệu có nội dung khác nhau là thứ tự liệt kê tại khoản 2.1. Nội dung trái pháp luật không có hiệu lực."])

    v.dieu("Điều 3. Sử dụng tài liệu, thông tin liên quan đến hợp đồng và bản quyền")
    muc(v, [
        "3.1. Bên B không được tiết lộ thông tin, tài liệu của Bên A và của Dự án cho bên thứ ba khi chưa có sự đồng ý bằng văn bản của Bên A, trừ trường hợp pháp luật có quy định.",
        "3.2. Sản phẩm của hợp đồng thuộc quyền sở hữu và sử dụng của Bên A sau khi Bên A thanh toán đủ giá trị tương ứng; Bên B bảo đảm quyền tác giả theo quy định của pháp luật và không vi phạm quyền sở hữu trí tuệ của bên thứ ba.",
        "3.3. Tài liệu, phương tiện do Bên A cung cấp phải được Bên B bảo quản và hoàn trả khi kết thúc công việc.",
    ])
    v.dieu("Điều 4. Trao đổi thông tin")
    muc(v, [
        "4.1. Mọi kiến nghị, đề xuất, yêu cầu của các bên trong quá trình thực hiện hợp đồng phải bằng văn bản (hoặc thông điệp dữ liệu theo quy định về giao dịch điện tử), gửi đúng địa chỉ giao dịch ghi tại Phần 1. Bên nhận phải trả lời bằng văn bản về việc chấp thuận hoặc không chấp thuận trong thời hạn 05 ngày làm việc, không quá 07 ngày làm việc kể từ ngày nhận được; nếu không chấp thuận phải nêu rõ lý do.",
        "4.2. Đại diện quản lý thực hiện hợp đồng: Bên A cử lãnh đạo phòng Tổng hợp - Hành chính và Quản trị; Bên B cử " + ("chủ nhiệm khảo sát và chủ nhiệm lập BCKTKT" if ks else "giám đốc quản lý dự án") + " ghi tại Phụ lục số 4. Mỗi bên thông báo bằng văn bản về người đại diện, phạm vi và quyền hạn của người đó.",
        "4.3. Khi thay đổi thông tin giao dịch, bên có thay đổi phải thông báo bằng văn bản trong thời hạn 07 ngày kể từ ngày phát sinh thay đổi; thay đổi làm ảnh hưởng tư cách pháp lý hoặc việc thực hiện hợp đồng thì ký phụ lục hợp đồng.",
    ])
    v.dieu("Điều 5. Luật áp dụng và ngôn ngữ sử dụng trong hợp đồng")
    muc(v, ["5.1. Hợp đồng này chịu sự điều chỉnh của pháp luật Việt Nam.", "5.2. Ngôn ngữ của hợp đồng là tiếng Việt."])

    v.dieu("Điều 6. Nội dung, khối lượng công việc và sản phẩm của hợp đồng")
    if ks:
        muc(v, [
            "6.1. Khảo sát xây dựng (theo Điều 10 đến Điều 15 Nghị định số 217/2026/NĐ-CP):",
            "  a) Lập phương án kỹ thuật khảo sát phù hợp với nhiệm vụ khảo sát do Bên A phê duyệt, trình Bên A kiểm tra và phê duyệt trước khi thực hiện;",
            "  b) Thực hiện khảo sát hiện trạng 03 ký túc xá (nhà G, nhà H và ký túc xá tại cơ sở Khoa Kỹ thuật - Công nghệ và Đào tạo - Sát hạch lái xe) gồm đo vẽ, đánh giá hiện trạng kết cấu, hệ thống điện, cấp - thoát nước, phòng cháy chữa cháy; khảo sát địa hình, địa chất khi nhiệm vụ khảo sát yêu cầu;",
            "  c) Lập Báo cáo kết quả khảo sát xây dựng theo Điều 14 Nghị định số 217/2026/NĐ-CP, trình Bên A nghiệm thu, phê duyệt. Khảo sát phải hoàn thành và được phê duyệt trước khi lập thiết kế bản vẽ thi công.",
            "6.2. Lập BCKTKT (thiết kế một bước là thiết kế bản vẽ thi công):",
            "  a) Lập thuyết minh BCKTKT theo Điều 30 Nghị định số 217/2026/NĐ-CP: mục tiêu, địa điểm, sự phù hợp quy hoạch, cấp công trình, phòng cháy chữa cháy, môi trường, thời gian và hình thức quản lý dự án, tổng mức đầu tư, nguồn vốn, hiệu quả, vận hành và bảo trì;",
            "  b) Lập thiết kế bản vẽ thi công theo Điều 23 Nghị định số 217/2026/NĐ-CP kèm chỉ dẫn kỹ thuật cho việc cải tạo 03 ký túc xá nêu trên, phù hợp quy mô và nhiệm vụ đã được phê duyệt tại Quyết định số 2158/QĐ-CĐKT ngày 29/9/2026;",
            "  c) Lập danh mục, cấu hình kỹ thuật và xác định chi phí 02 mô hình xe ô tô con số tự động phục vụ đào tạo để đưa vào dự toán và tổng mức đầu tư, trên cơ sở thông tin giá hợp lệ do Bên B thu thập và Bên A chấp thuận;",
            "  d) Lập dự toán xây dựng và tổng mức đầu tư theo Nghị định số 206/2026/NĐ-CP và hướng dẫn của Bộ Xây dựng; chi phí quản lý dự án, tư vấn, dự phòng nằm trong tổng mức đầu tư;",
            "  đ) Lập hồ sơ phục vụ các thủ tục kèm theo (phiếu xác định thủ tục về quy hoạch, phòng cháy chữa cháy, môi trường, giấy phép xây dựng nếu thuộc diện) để Bên A thực hiện.",
            "6.3. Phối hợp, giải trình, chỉnh sửa hồ sơ theo yêu cầu của Bên A, cơ quan chủ trì thẩm định và người quyết định đầu tư trong quá trình thẩm định, phê duyệt dự án mà không tính thêm chi phí; bàn giao bộ hồ sơ chính thức sau phê duyệt để Bên A đóng dấu phê duyệt hồ sơ thiết kế.",
            "6.4. Sản phẩm của hợp đồng, số lượng và quy cách được quy định tại Phụ lục số 1.",
            "6.5. Hợp đồng không bao gồm giám sát tác giả, thẩm tra độc lập thiết kế và dự toán, thủ tục xin giấy phép. Khi Bên A yêu cầu, hai bên ký phụ lục hoặc hợp đồng riêng.",
        ])
    else:
        muc(v, [
            "6.1. Bên B thực hiện tư vấn quản lý dự án từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án theo hình thức chủ đầu tư thuê tư vấn quản lý dự án (Điều 46 Nghị định số 217/2026/NĐ-CP), gồm các công việc chủ yếu:",
            "  a) Lập kế hoạch quản lý dự án (tiến độ, vốn, chất lượng, an toàn, rủi ro, hồ sơ) trình Bên A phê duyệt;",
            "  b) Giai đoạn chuẩn bị đầu tư: giám sát việc thực hiện hợp đồng khảo sát và lập BCKTKT (nhiệm vụ, phương án khảo sát, tiến độ, nghiệm thu); kiểm tra báo cáo kết quả khảo sát và BCKTKT; hỗ trợ Bên A lập hồ sơ trình thẩm định, giải trình và phê duyệt dự án;",
            "  c) Hỗ trợ Bên A phân chia gói thầu, lập kế hoạch lựa chọn nhà thầu và hồ sơ lựa chọn nhà thầu cho các gói tiếp theo; Bên A tổ chức lựa chọn nhà thầu, ký kết hợp đồng;",
            "  d) Giai đoạn thực hiện: phối hợp tổ chức khởi công; tổ chức quản lý các hợp đồng do Bên A ký (chất lượng, khối lượng, tiến độ, chi phí, an toàn và vệ sinh môi trường); phối hợp kiểm tra vật liệu, kiểm định chất lượng khi Bên A yêu cầu; phối hợp nghiệm thu giai đoạn, hạng mục, hoàn thành và bàn giao, kể cả việc kiểm tra nghiệm thu của cơ quan nhà nước nếu thuộc diện;",
            "  đ) Kiểm tra, kiểm soát hồ sơ thanh toán, quyết toán các hợp đồng; phối hợp thanh toán, quyết toán vốn đầu tư; hỗ trợ lập hồ sơ quyết toán dự án hoàn thành, kiểm toán, thẩm tra, phê duyệt quyết toán;",
            "  e) Lập báo cáo định kỳ và cung cấp số liệu phục vụ báo cáo giải ngân hằng tháng của Bên A; thực hiện các công việc quản lý khác phù hợp quy định pháp luật khi Bên A yêu cầu.",
            "6.2. Bên B hỗ trợ Bên A, không thay Bên A về trách nhiệm pháp lý và thẩm quyền quyết định, ký phê duyệt, nghiệm thu, thanh toán. Bên B không đồng thời thực hiện tư vấn khảo sát, lập BCKTKT của Dự án.",
            "6.3. Tổng chi phí quản lý dự án do Bên A và Bên B thực hiện không vượt chi phí quản lý dự án đã được phê duyệt (Điều 25 Nghị định số 206/2026/NĐ-CP).",
            "6.4. Sản phẩm của hợp đồng, số lượng và quy cách được quy định tại Phụ lục số 1.",
        ])
    v.dieu("Điều 7. Yêu cầu về chất lượng, số lượng sản phẩm")
    if ks:
        muc(v, [
            "7.1. Sản phẩm phải phù hợp nhiệm vụ đã được duyệt và nội dung hợp đồng; tuân thủ pháp luật về quản lý hoạt động xây dựng, quản lý chất lượng, quy chuẩn kỹ thuật và tiêu chuẩn áp dụng được Bên A chấp thuận; đủ điều kiện để trình cơ quan chủ trì thẩm định và người quyết định đầu tư phê duyệt.",
            "7.2. Bên B chịu trách nhiệm toàn diện trước pháp luật về chất lượng khảo sát và chất lượng thiết kế do mình thực hiện; việc Bên A kiểm tra, phê duyệt không làm giảm trách nhiệm của Bên B (Điều 15 Nghị định số 217/2026/NĐ-CP).",
            "7.3. Số lượng, định dạng hồ sơ sản phẩm theo Phụ lục số 1.",
        ])
    else:
        muc(v, [
            "7.1. Sản phẩm, ý kiến và báo cáo của Bên B phải đúng nội dung hợp đồng, đúng quy định về quản lý dự án đầu tư xây dựng và quản lý chất lượng công trình, kịp thời và có căn cứ.",
            "7.2. Báo cáo công tác quản lý điều hành dự án gồm tiến độ, chất lượng, khối lượng, chi phí, vốn, an toàn, các vấn đề tồn tại và kiến nghị; số liệu thống nhất với hồ sơ của Bên A.",
            "7.3. Số lượng, định dạng hồ sơ sản phẩm theo Phụ lục số 1.",
        ])
    v.dieu("Điều 8. Thời gian và tiến độ thực hiện hợp đồng")
    if ks:
        muc(v, [
            "8.1. Thời gian thực hiện các công việc của hợp đồng là 120 ngày kể từ ngày hợp đồng có hiệu lực, tính đến khi Bên B nộp hồ sơ BCKTKT đủ điều kiện để Bên A trình thẩm định. Thời gian thẩm định, phê duyệt của cơ quan nhà nước không tính vào thời gian này; việc giải trình, chỉnh sửa theo khoản 6.3 thực hiện trong thời hạn Bên A yêu cầu, không quá 15 ngày kể từ ngày nhận được yêu cầu.",
            "8.2. Tiến độ và các mốc hoàn thành công việc chủ yếu theo Phụ lục số 2.",
        ])
    else:
        muc(v, [
            "8.1. Thời gian thực hiện hợp đồng không quá 03 năm kể từ ngày hợp đồng có hiệu lực, từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án.",
            "8.2. Tiến độ thực hiện bám theo tiến độ của Dự án và các mốc nêu tại Phụ lục số 2.",
        ])
    muc(v, [
        "8.3. Bên gặp khó khăn có thể làm chậm tiến độ phải thông báo ngay bằng văn bản cho bên kia, nêu lý do và thời gian dự kiến kéo dài. Bên nhận thông báo xem xét, quyết định; nếu chấp thuận gia hạn, hai bên ký văn bản sửa đổi hợp đồng theo Điều 17.",
        "8.4. Chậm tiến độ do lỗi của Bên B không làm tăng giá hợp đồng.",
    ])

    v.dieu("Điều 9. Giá hợp đồng, tạm ứng, thanh toán")
    gia_chu = bang_chu(gia)
    muc(v, [
        "9.1. Hình thức giá hợp đồng: Hợp đồng trọn gói (khoản 2 Điều 6 Nghị định số 210/2026/NĐ-CP).",
        f"9.2. Giá hợp đồng: {vnd(gia)} đồng (bằng chữ: {gia_chu[0].upper() + gia_chu[1:]}), bằng giá trúng thầu tại Quyết định số {c['qd']['so']}" + (f", gồm khảo sát xây dựng {vnd(c['a_ks'])} đồng và lập BCKTKT (kể cả thiết kế bản vẽ thi công) {vnd(c['a_tk'])} đồng." if ks else "."),
        "9.3. Giá hợp đồng đã bao gồm toàn bộ chi phí để thực hiện công việc (nhân công, đi lại, thiết bị, hoàn thiện sản phẩm sau rà soát, thẩm định và các chi phí khác) và các khoản thuế, phí, lệ phí Bên B phải nộp theo quy định. Bên B trực tiếp kê khai và nộp thuế. Giá hợp đồng không bao gồm phí thẩm định, chi phí thẩm tra độc lập và chi phí các cuộc họp của Bên A.",
        "9.4. Giá hợp đồng trọn gói không thay đổi trong suốt thời gian thực hiện, trừ các trường hợp quy định tại Điều 17 (thay đổi phạm vi công việc, bất khả kháng, hoàn cảnh thay đổi cơ bản và trường hợp khác do hai bên thỏa thuận phù hợp pháp luật).",
        "9.5. Bảo đảm: Bên B là nhà thầu cung cấp dịch vụ tư vấn nên không phải nộp bảo đảm thực hiện hợp đồng (điểm a khoản 2 Điều 68 Luật Đấu thầu; điểm c khoản 2 Điều 13 Nghị định số 210/2026/NĐ-CP). " + ("Khoản tạm ứng không vượt 01 tỷ đồng nên không bắt buộc bảo lãnh tạm ứng (điểm c khoản 3 Điều 12 Nghị định số 210/2026/NĐ-CP)." if ks else "Hợp đồng thuê tư vấn quản lý dự án không yêu cầu bảo lãnh tạm ứng (điểm b khoản 2 Điều 9 Nghị định số 254/2025/NĐ-CP)."),
    ])
    tu = c["tu"]
    tu_chu = bang_chu(tu)
    muc(v, [
        "9.6. Tạm ứng:",
        f"  a) Mức tạm ứng: {c['ty_le_tu']}% giá hợp đồng, bằng {vnd(tu)} đồng (bằng chữ: {tu_chu[0].upper() + tu_chu[1:]}), phù hợp mức tối thiểu 20% và mức tối đa 30% đối với hợp đồng tư vấn có giá trị đến 10 tỷ đồng (điểm g, h khoản 3 Điều 12 Nghị định số 210/2026/NĐ-CP);",
        (f"  b) Tạm ứng theo hai năm: Năm 2026 tạm ứng {vnd(c['tu26'])} đồng (bằng chữ: {bang_chu(c['tu26'])}), là phần kế hoạch vốn năm 2026 của Dự án (260.000.000 đồng) chia cho hai hợp đồng tư vấn chuẩn bị đầu tư theo tỷ lệ giá hợp đồng; năm 2027 tạm ứng phần còn lại {vnd(c['tu27'])} đồng (bằng chữ: {bang_chu(c['tu27'])}) để đủ mức {c['ty_le_tu']}% giá hợp đồng, theo kế hoạch vốn năm 2027 được cấp có thẩm quyền giao;"),
        "  c) Việc tạm ứng thực hiện sau khi hợp đồng có hiệu lực, một hoặc nhiều lần, trong phạm vi kế hoạch vốn đã được cấp có thẩm quyền giao cho Bên A và theo thông báo bằng văn bản của Bên A. Trong 07 ngày làm việc kể từ ngày nhận đủ đề nghị tạm ứng của Bên B và khi đã có kế hoạch vốn tương ứng, Bên A hoàn tất thủ tục tạm ứng với Kho bạc (giấy đề nghị thanh toán vốn Mẫu số 04.a/TT, giấy rút vốn Mẫu số 05.a/TT). Tổng tạm ứng không vượt kế hoạch vốn năm của Dự án (khoản 4 Điều 9 Nghị định số 254/2025/NĐ-CP);",
        "  d) Phần tạm ứng chưa thực hiện do chưa có kế hoạch vốn được thực hiện khi kế hoạch vốn được bổ sung hoặc từ năm tiếp theo; Bên B không có quyền yêu cầu lãi hoặc bồi thường do việc chưa tạm ứng vì chưa có vốn;",
        "  đ) Tiền tạm ứng được thu hồi dần qua các lần thanh toán theo Phụ lục số 3 và phải thu hồi hết khi giá trị thanh toán (kể cả tạm ứng) cộng dồn đạt 80% giá hợp đồng; Bên B sử dụng tạm ứng đúng mục đích, đúng đối tượng.",
        "9.7. Thanh toán:",
        "  a) Số lần thanh toán và giá trị mỗi lần theo Phụ lục số 3; mọi khoản thanh toán thực hiện trong phạm vi kế hoạch vốn do cấp có thẩm quyền giao hằng năm;",
        "  b) Hồ sơ thanh toán gồm: biên bản nghiệm thu khối lượng hoàn thành của giai đoạn thanh toán; bảng tính giá trị công việc phát sinh (nếu có); giấy đề nghị thanh toán của Bên B nêu giá trị hoàn thành, giá trị phát sinh, giảm trừ tiền tạm ứng, giá trị đề nghị thanh toán; hóa đơn hợp lệ (khoản 2 Điều 29 Nghị định số 210/2026/NĐ-CP);",
        "  c) Trong 07 ngày làm việc, không quá 14 ngày làm việc, kể từ ngày nhận đủ hồ sơ thanh toán hợp lệ, Bên A thanh toán cho Bên B (điểm l khoản 4 Điều 28 Nghị định số 210/2026/NĐ-CP). Bên A chậm thanh toán thì trả lãi theo lãi suất quá hạn do ngân hàng thương mại nơi Bên B mở tài khoản công bố;",
        "  d) Hình thức thanh toán: chuyển khoản; đồng tiền thanh toán: đồng Việt Nam;",
        "  đ) Trường hợp chưa bảo đảm kế hoạch vốn cho các năm sau, Bên A thông báo bằng văn bản và hai bên thỏa thuận tạm dừng thanh toán theo Điều 18; Bên A thanh toán ngay khi có vốn.",
    ])
    v.dieu("Điều 10. Nghiệm thu sản phẩm")
    if ks:
        muc(v, [
            "10.1. Căn cứ nghiệm thu: hồ sơ hợp đồng; nhiệm vụ khảo sát, nhiệm vụ thiết kế đã được Bên A phê duyệt; danh mục quy chuẩn, tiêu chuẩn áp dụng; báo cáo kết quả khảo sát được phê duyệt; thông báo kết quả thẩm định của cơ quan chủ trì thẩm định; quyết định phê duyệt dự án.",
            "10.2. Nghiệm thu theo ba giai đoạn: (1) Báo cáo kết quả khảo sát xây dựng được phê duyệt; (2) BCKTKT đủ điều kiện trình thẩm định; (3) Hồ sơ hoàn chỉnh sau thẩm định và phê duyệt dự án. Biên bản nghiệm thu khối lượng hoàn thành xác nhận Bên B hoàn thành công việc đúng phạm vi hợp đồng (khoản 2 Điều 29 Nghị định số 210/2026/NĐ-CP).",
        ])
    else:
        muc(v, [
            "10.1. Căn cứ nghiệm thu: hồ sơ hợp đồng; kế hoạch quản lý dự án đã được Bên A phê duyệt; báo cáo công tác quản lý điều hành dự án và các ý kiến bằng văn bản của Bên B; hồ sơ bàn giao.",
            "10.2. Bên A nghiệm thu từng báo cáo định kỳ và nghiệm thu hoàn thành hợp đồng khi Bên B hoàn thành toàn bộ công việc, bàn giao đầy đủ hồ sơ quản lý dự án và hồ sơ quyết toán dự án hoàn thành được cấp có thẩm quyền phê duyệt (hoặc khi hợp đồng chấm dứt theo Điều 18).",
        ])
    muc(v, [
        "10.3. Bên A tổ chức nghiệm thu trong 07 ngày làm việc kể từ ngày nhận đủ hồ sơ nghiệm thu hợp lệ. Thành phần gồm đại diện Bên A, Bên B và các bên liên quan do Bên A mời. Sản phẩm có sai sót phải được Bên B khắc phục, chi phí do bên gây ra sai sót chịu (khoản 2 Điều 9 Nghị định số 210/2026/NĐ-CP).",
    ])
    v.dieu("Điều 11. Quyền, nghĩa vụ và trách nhiệm của Bên nhận thầu")
    muc(v, [
        "11.1. Quyền của Bên B: (a) Yêu cầu Bên A cung cấp thông tin, tài liệu liên quan; (b) Đề xuất khối lượng công việc phát sinh hợp lý; (c) Được bảo đảm quyền tác giả theo quy định; (d) Từ chối thực hiện công việc ngoài phạm vi hợp đồng hoặc yêu cầu trái pháp luật; (đ) Yêu cầu Bên A nghiệm thu, thanh toán đúng hạn và trả lãi chậm thanh toán.",
        "11.2. Nghĩa vụ và trách nhiệm của Bên B: (a) Thực hiện công việc đúng pháp luật, đúng chất lượng, tiến độ, bố trí đúng nhân sự chủ chốt đã nêu tại Phụ lục số 4 và bảo đảm điều kiện năng lực theo quy định; (b) Chịu trách nhiệm về kết quả, chất lượng sản phẩm; (c) Nộp báo cáo, tài liệu đúng số lượng và thời hạn, thông báo kịp thời mọi thông tin có thể làm chậm tiến độ và đề xuất giải pháp; (d) Cử đại diện đủ thẩm quyền giải quyết công việc; (đ) Giữ bí mật thông tin; (e) Bồi thường thiệt hại do lỗi của mình; (g) Mua bảo hiểm trách nhiệm nghề nghiệp theo quy định (nếu thuộc đối tượng bắt buộc); (h) Thực hiện nghĩa vụ thuế, phí; (i) Ứng dụng công nghệ thông tin, chuyển đổi số trong thực hiện công việc theo yêu cầu của Bên A.",
    ])
    v.dieu("Điều 12. Quyền, nghĩa vụ và trách nhiệm của Bên giao thầu")
    muc(v, [
        "12.1. Quyền của Bên A: (a) Yêu cầu Bên B bàn giao hồ sơ, tài liệu; yêu cầu sửa đổi, bổ sung sản phẩm không đạt chất lượng; (b) Kiểm tra chất lượng, tiến độ nhưng không cản trở hoạt động bình thường của Bên B; (c) Từ chối đề xuất không hợp lý, từ chối nghiệm thu sản phẩm không đúng hợp đồng; (d) Sở hữu và sử dụng sản phẩm theo hợp đồng; (đ) Yêu cầu thay nhân sự không đáp ứng yêu cầu năng lực.",
        "12.2. Nghĩa vụ và trách nhiệm của Bên A: (a) Cung cấp kịp thời hồ sơ, tài liệu theo thỏa thuận và chịu trách nhiệm về tính chính xác của tài liệu đã cung cấp; (b) Tra cứu, kiểm tra thông tin năng lực hoạt động xây dựng của Bên B; (c) Giải quyết kiến nghị của Bên B đúng thời hạn quy định tại Điều 4; (d) Tổ chức nghiệm thu, nhận bàn giao sản phẩm; (đ) Thanh toán đầy đủ, đúng hạn trong phạm vi kế hoạch vốn; trả lãi khi chậm thanh toán; (e) Giữ bí mật thông tin; (g) Xem xét chấp thuận hoặc từ chối đề xuất của Bên B về khối lượng phát sinh ngoài hợp đồng.",
    ])
    v.dieu("Điều 13. Giải quyết tranh chấp, khiếu nại trong quá trình thực hiện hợp đồng")
    muc(v, [
        "13.1. Tranh chấp được giải quyết bằng thương lượng, hòa giải. Nếu không thành, mỗi bên có quyền đề nghị Tòa án nhân dân có thẩm quyền giải quyết theo quy định của pháp luật. Trong thời gian giải quyết tranh chấp, hai bên tiếp tục thực hiện các nghĩa vụ không bị ảnh hưởng, trừ trường hợp được tạm dừng theo Điều 18. Hợp đồng này không áp dụng mô hình ban xử lý tranh chấp.",
        "13.2. Khi một bên phát hiện bên kia thực hiện không đúng hợp đồng thì có quyền khiếu nại bằng văn bản gửi đúng địa chỉ giao dịch; bên bị khiếu nại phải đưa ra căn cứ, dẫn chứng và trả lời trong thời hạn 07 ngày làm việc; trường hợp không chấp thuận phải nêu rõ lý do.",
    ])
    v.dieu("Điều 14. Rủi ro, sự kiện bất khả kháng và hoàn cảnh thay đổi cơ bản")
    muc(v, [
        "14.1. Rủi ro có thể lường trước khi giao kết hợp đồng do bên nào có khả năng kiểm soát tốt hơn thì bên đó quản lý, xử lý và chịu chi phí khắc phục; các rủi ro lường trước gồm thay đổi nhân sự, chậm cung cấp tài liệu, chậm thẩm định của cơ quan nhà nước và chưa bố trí vốn.",
        "14.2. Sự kiện bất khả kháng là sự kiện không thể lường trước, không thể tránh được và không thể khắc phục dù đã áp dụng mọi biện pháp cần thiết, gồm chiến tranh, bạo loạn, thiên tai, hỏa hoạn, dịch bệnh hoặc chính sách của Nhà nước. Bên bị ảnh hưởng phải thông báo bằng văn bản trong 14 ngày kể từ ngày xảy ra sự kiện, kèm xác nhận của cơ quan có thẩm quyền, và áp dụng mọi biện pháp hợp lý để hạn chế hậu quả. Thời hạn hoàn thành công việc được gia hạn bằng thời gian bị ảnh hưởng. Nếu việc thực hiện hợp đồng bị dừng vượt thời hạn thông báo thì mỗi bên có quyền chấm dứt hợp đồng; Bên A thanh toán công việc đã hoàn thành theo giá hợp đồng.",
        "14.3. Hoàn cảnh thay đổi cơ bản là thay đổi do nguyên nhân khách quan xảy ra sau khi giao kết hợp đồng, lớn đến mức nếu biết trước thì các bên đã không giao kết hoặc giao kết với nội dung khác, gồm Nhà nước thay đổi chính sách, pháp luật. Bên bị ảnh hưởng thông báo nêu rõ công việc bị ảnh hưởng, biện pháp và đề xuất sửa đổi; bên nhận thông báo trả lời trong 07 ngày làm việc. Nếu không thỏa thuận được, bên bị ảnh hưởng có quyền đề nghị Tòa án giải quyết.",
    ])
    v.dieu("Điều 15. Nhà thầu phụ")
    muc(v, [
        ("15.1. Bên B không giao thầu phụ phần việc chính của hợp đồng. Việc thuê đơn vị thí nghiệm, đo đạc đủ điều kiện năng lực cho một phần công việc khảo sát phải được Bên A chấp thuận bằng văn bản; Bên B chịu trách nhiệm trước Bên A về công việc do nhà thầu phụ thực hiện." if ks else "15.1. Bên B không giao thầu phụ phần việc của hợp đồng này. Việc thuê chuyên gia hoặc đơn vị hỗ trợ cho một phần công việc phải được Bên A chấp thuận bằng văn bản; Bên B chịu trách nhiệm trước Bên A về công việc đó."),
        "15.2. Bên A có quyền từ chối nhà thầu phụ do Bên B đề xuất khi không đáp ứng điều kiện năng lực.",
    ])
    v.dieu("Điều 16. Nhân lực của Bên nhận thầu")
    muc(v, [
        "16.1. Nhân lực của Bên B phải đủ điều kiện năng lực theo quy định, cụ thể tại Phụ lục số 4. Nhân sự chủ chốt thực hiện đúng như hồ sơ năng lực đã nộp.",
        "16.2. Khi cần thay đổi nhân sự chủ chốt, Bên B gửi văn bản nêu lý do và hồ sơ người thay thế; người thay thế phải có trình độ, kinh nghiệm và chứng chỉ hành nghề tương đương hoặc cao hơn. Bên A trả lời trong 05 ngày làm việc; quá thời hạn mà Bên A không có ý kiến thì coi như chấp thuận. Chi phí thay đổi nhân sự do Bên B chịu, thù lao người thay thế không vượt thù lao người bị thay.",
        "16.3. Bên A có quyền yêu cầu Bên B thay nhân sự không đáp ứng yêu cầu; Bên B phải trả lời bằng văn bản trong 07 ngày kể từ ngày nhận yêu cầu.",
        "16.4. Bên B tổ chức thực hiện đúng tiến độ; giờ làm việc, ngày nghỉ theo Bộ luật Lao động; giá hợp đồng đã bao gồm chi phí làm ngoài giờ.",
    ])
    v.dieu("Điều 17. Sửa đổi hợp đồng")
    muc(v, [
        "17.1. Hợp đồng chỉ được sửa đổi bằng phụ lục hoặc văn bản sửa đổi do hai bên ký, theo Điều 22 đến Điều 25 Nghị định số 210/2026/NĐ-CP, trong các trường hợp: thay đổi phạm vi, khối lượng công việc; thay đổi thời gian, tiến độ; bất khả kháng; hoàn cảnh thay đổi cơ bản; thay đổi chính sách, pháp luật; trường hợp khác do hai bên thỏa thuận phù hợp pháp luật.",
        "17.2. Việc điều chỉnh khối lượng, phạm vi công việc phải có đề xuất bằng văn bản, được Bên A chấp thuận trước khi thực hiện; phần giá trị phát sinh được xác định theo dự toán được Bên A phê duyệt và trong phạm vi chi phí đã được duyệt của Dự án.",
        "17.3. Điều chỉnh thời gian, tiến độ dẫn đến vượt thời gian thực hiện Dự án thì Bên A phải báo cáo người quyết định đầu tư xem xét trước khi điều chỉnh hợp đồng.",
    ])
    v.dieu("Điều 18. Tạm dừng và chấm dứt hợp đồng")
    muc(v, [
        "18.1. Tạm dừng thực hiện hợp đồng khi: một bên vi phạm nghiêm trọng nghĩa vụ; sự kiện bất khả kháng; yêu cầu của cơ quan nhà nước có thẩm quyền; thay đổi pháp luật ảnh hưởng trực tiếp; Bên A chưa bảo đảm kế hoạch vốn thanh toán theo thỏa thuận tại khoản 9.7; Bên A không thanh toán khoản đến hạn quá 28 ngày kể từ ngày hết hạn thanh toán (Điều 26 Nghị định số 210/2026/NĐ-CP). Bên tạm dừng thông báo trước bằng văn bản nêu lý do, thời điểm và hậu quả, thời hạn thông báo không quá 28 ngày, trừ trường hợp bất khả kháng.",
        "18.2. Bên A có quyền chấm dứt hợp đồng khi Bên B: (a) không sửa chữa được sai sót nghiêm trọng trong thời hạn Bên A ấn định; (b) không có lý do chính đáng mà ngừng thực hiện công việc quá 28 ngày; (c) bị phá sản, giải thể; (d) cố ý cung cấp tài liệu không đúng sự thật gây thiệt hại cho Bên A; (đ) không tuân theo phán quyết đã có hiệu lực; (e) bất khả kháng theo khoản 14.2.",
        "18.3. Bên B có quyền chấm dứt hợp đồng khi: (a) công việc bị ngừng do lỗi của Bên A quá 56 ngày; (b) Bên A không thanh toán theo hợp đồng quá 56 ngày kể từ ngày nhận đủ hồ sơ hợp lệ mà không thuộc đối tượng tranh chấp; (c) Bên A bị giải thể, phá sản; (d) bất khả kháng theo khoản 14.2. Bên chấm dứt thông báo bằng văn bản trước tối thiểu 28 ngày.",
        "18.4. Khi chấm dứt hợp đồng, Bên B nhanh chóng kết thúc công việc và bàn giao hồ sơ đã thực hiện; Bên A thanh toán phần công việc hoàn thành trước ngày chấm dứt có hiệu lực; việc thanh lý hoàn tất trong 56 ngày, riêng hợp đồng thuộc dự án đầu tư công thực hiện theo điểm b khoản 3 Điều 31 Nghị định số 210/2026/NĐ-CP.",
    ])
    v.dieu("Điều 19. Quyết toán và thanh lý hợp đồng")
    muc(v, [
        "19.1. Bên B lập hồ sơ quyết toán hợp đồng gồm: biên bản nghiệm thu hoàn thành toàn bộ công việc thuộc phạm vi hợp đồng và công việc phát sinh; bảng tính giá trị quyết toán A - B nêu giá trị hoàn thành, giá trị phát sinh, giá trị đã thanh toán hoặc tạm ứng và giá trị còn lại; sản phẩm của hợp đồng; tài liệu khác theo thỏa thuận. Thời hạn quyết toán tối đa 60 ngày kể từ ngày toàn bộ công việc hoàn thành và được nghiệm thu (khoản 3 Điều 30 Nghị định số 210/2026/NĐ-CP).",
        "19.2. Hợp đồng được thanh lý khi các bên hoàn thành nghĩa vụ hoặc hợp đồng chấm dứt; Bên B lập biên bản thanh lý trình Bên A xác nhận trong thời hạn tối đa 45 ngày kể từ ngày hoàn thành nghĩa vụ hoặc chấm dứt hợp đồng (điểm b khoản 3 Điều 31 Nghị định số 210/2026/NĐ-CP).",
    ])
    v.dieu("Điều 20. Điều khoản chung")
    muc(v, [
        "20.1. Hợp đồng có hiệu lực kể từ ngày hai bên ký. Các bên cam kết thực hiện trung thực, bình đẳng, hợp tác và chịu trách nhiệm trước pháp luật về nội dung đã ký.",
        "20.2. Phụ lục số 1, 2, 3, 4 là một phần không tách rời của hợp đồng. Mọi sửa đổi, bổ sung phải bằng văn bản có chữ ký của hai bên.",
        "20.3. Hợp đồng được lập bằng tiếng Việt thành 06 bản có giá trị pháp lý như nhau, Bên A giữ 04 bản, Bên B giữ 02 bản.",
    ])
    v.giu_cuoi()
    chu_ky_hd(v, c)

    # ---------- phụ lục (section riêng, số trang từ 1)
    v.phu_luc_section()
    v.tieu_de("PHỤ LỤC SỐ 1")
    v.tieu_de("NỘI DUNG, KHỐI LƯỢNG CÔNG VIỆC VÀ SẢN PHẨM CỦA HỢP ĐỒNG")
    if ks:
        v.bang(["STT", "Công việc, sản phẩm", "Số lượng, quy cách", "Ghi chú"], [1.5, 7.2, 4.2, 4.1], [
            ("1", "Nhiệm vụ khảo sát (hỗ trợ lập), phương án kỹ thuật khảo sát", "05 bộ giấy; 01 bộ tệp điện tử", "Bên A phê duyệt"),
            ("2", "Báo cáo kết quả khảo sát xây dựng (đo vẽ hiện trạng, đánh giá kết cấu, điện, cấp - thoát nước, PCCC; địa hình, địa chất nếu có)", "05 bộ giấy; 01 bộ tệp điện tử (.pdf, .dwg)", "Điều 14 NĐ 217/2026"),
            ("3", "Thuyết minh BCKTKT", "07 bộ giấy; 01 bộ tệp điện tử (.pdf, .docx)", "Điều 30 NĐ 217/2026"),
            ("4", "Hồ sơ thiết kế bản vẽ thi công 03 ký túc xá và chỉ dẫn kỹ thuật", "07 bộ giấy; 01 bộ tệp điện tử (.pdf, .dwg)", "Điều 23 NĐ 217/2026"),
            ("5", "Danh mục, cấu hình kỹ thuật, chi phí 02 mô hình xe ô tô con số tự động", "07 bộ giấy; 01 bộ tệp điện tử", "Đưa vào dự toán, tổng mức đầu tư"),
            ("6", "Dự toán xây dựng, tổng mức đầu tư và bảng tính chi phí", "07 bộ giấy; 01 bộ tệp điện tử (.pdf, .xlsx)", "NĐ 206/2026"),
            ("7", "Hồ sơ phục vụ thủ tục kèm theo (quy hoạch, PCCC, môi trường, giấy phép nếu có)", "01 bộ", "Bên A thực hiện thủ tục"),
            ("8", "Báo cáo giải trình, hồ sơ chỉnh sửa theo kết quả thẩm định; bộ hồ sơ chính thức sau phê duyệt", "07 bộ giấy; 01 bộ tệp điện tử", "Không tính thêm chi phí"),
        ], can_giua=(0,))
    else:
        v.bang(["STT", "Công việc, sản phẩm", "Số lượng, quy cách", "Ghi chú"], [1.5, 7.2, 4.2, 4.1], [
            ("1", "Kế hoạch quản lý dự án", "03 bộ giấy; tệp điện tử", "Trong 15 ngày kể từ hiệu lực; Bên A phê duyệt"),
            ("2", "Ý kiến bằng văn bản về nhiệm vụ, phương án, báo cáo khảo sát và BCKTKT", "Theo từng lần", "Giai đoạn chuẩn bị đầu tư"),
            ("3", "Đề xuất phân gói thầu, dự thảo kế hoạch và hồ sơ lựa chọn nhà thầu các gói tiếp theo", "Theo từng gói", "Bên A phê duyệt"),
            ("4", "Báo cáo công tác quản lý điều hành dự án", "Hằng quý; 02 bộ giấy; tệp điện tử", "Tiến độ, chất lượng, chi phí, vốn, an toàn"),
            ("5", "Số liệu phục vụ báo cáo giải ngân hằng tháng của Bên A", "Hằng tháng; tệp điện tử", "Gửi trước ngày 25 hằng tháng"),
            ("6", "Biên bản, nhật ký, ý kiến kiểm soát chất lượng, khối lượng, thanh toán các hợp đồng", "Theo từng lần", "Giai đoạn thực hiện"),
            ("7", "Hồ sơ hoàn thành, hồ sơ quyết toán dự án hoàn thành (phần tư vấn hỗ trợ)", "Theo mục lục", "Điều 6.1 đ"),
            ("8", "Bàn giao toàn bộ hồ sơ quản lý dự án", "Theo mục lục bàn giao", "Khi kết thúc hợp đồng"),
        ], can_giua=(0,))
    v.tieu_de("PHỤ LỤC SỐ 2")
    v.tieu_de("TIẾN ĐỘ THỰC HIỆN HỢP ĐỒNG")
    if ks:
        v.p("T0 là ngày hợp đồng có hiệu lực. Các mốc tính theo ngày kể từ T0.", indent=0, sau=4)
        v.bang(["STT", "Mốc công việc", "Thời hạn hoàn thành"], [1.5, 10.8, 4.7], [
            ("1", "Bên A phê duyệt nhiệm vụ khảo sát; Bên B nộp phương án kỹ thuật khảo sát", "T0 + 07 ngày"),
            ("2", "Hoàn thành khảo sát hiện trường", "T0 + 35 ngày"),
            ("3", "Nộp báo cáo kết quả khảo sát để nghiệm thu, phê duyệt", "T0 + 40 ngày"),
            ("4", "Hoàn thành thuyết minh, thiết kế bản vẽ thi công, dự toán, tổng mức đầu tư và hồ sơ thủ tục kèm theo", "T0 + 85 ngày"),
            ("5", "Nộp hồ sơ BCKTKT đủ điều kiện để Bên A trình thẩm định", "T0 + 90 ngày"),
            ("6", "Giải trình, chỉnh sửa, hoàn chỉnh hồ sơ sau thẩm định", "Trong 15 ngày kể từ ngày nhận yêu cầu; trong thời gian 120 ngày nếu thẩm định hoàn thành"),
            ("7", "Thời gian thực hiện công việc của hợp đồng (Điều 8.1)", "120 ngày kể từ T0"),
        ], can_giua=(0, 2))
    else:
        v.bang(["STT", "Giai đoạn, mốc", "Thời hạn"], [1.5, 10.8, 4.7], [
            ("1", "Lập kế hoạch quản lý dự án", "Trong 15 ngày kể từ ngày hợp đồng có hiệu lực"),
            ("2", "Giám sát hợp đồng khảo sát và lập BCKTKT; ý kiến về báo cáo khảo sát, BCKTKT", "Theo tiến độ hợp đồng khảo sát - lập BCKTKT (120 ngày)"),
            ("3", "Hỗ trợ trình thẩm định, phê duyệt dự án; phân gói thầu, kế hoạch lựa chọn nhà thầu", "Theo yêu cầu của Bên A"),
            ("4", "Quản lý thực hiện các hợp đồng thi công, thiết bị, giám sát", "Theo tiến độ của Dự án"),
            ("5", "Báo cáo công tác quản lý điều hành dự án", "Hằng quý, chậm nhất ngày 05 của tháng đầu quý sau"),
            ("6", "Hỗ trợ nghiệm thu hoàn thành, bàn giao, quyết toán dự án", "Theo quy định về quyết toán (nhóm C: 04 tháng lập, 02 tháng thẩm tra, 07 ngày phê duyệt)"),
            ("7", "Thời hạn hợp đồng (Điều 8.1)", "Không quá 03 năm kể từ ngày hợp đồng có hiệu lực"),
        ], can_giua=(0,))
    v.tieu_de("PHỤ LỤC SỐ 3")
    v.tieu_de("GIÁ HỢP ĐỒNG VÀ TIẾN ĐỘ THANH TOÁN")
    if ks:
        a_ks, a_tk = c["a_ks"], c["a_tk"]
        d2 = (a_tk * 60 + 50) // 100
        d3 = a_tk - d2
        th1 = (a_ks + 1) // 2  # lần 1 thu hồi một nửa giá trị lần thanh toán
        th2 = tu - th1
        assert th1 <= a_ks and th2 <= d2
        n1, n2, n3 = a_ks - th1, d2 - th2, d3
        assert tu + n1 + n2 + n3 == gia and a_ks + d2 + d3 == gia
        v.p("Hợp đồng trọn gói, giá hợp đồng " + vnd(gia) + " đồng. Số tiền làm tròn đến đồng.", indent=0, sau=4)
        v.bang(["Lần", "Điều kiện thanh toán", "Giá trị công việc (đồng)", "Thu hồi tạm ứng (đồng)", "Số tiền thanh toán (đồng)"],
               [1.9, 5.7, 3.2, 3.0, 3.2], [
            ("Tạm ứng năm 2026", "Sau khi hợp đồng có hiệu lực; phần vốn năm 2026 chia theo tỷ lệ giá hợp đồng (khoản 9.6)", "—", "—", vnd(c["tu26"])),
            ("Tạm ứng năm 2027", "Phần tạm ứng còn lại để đủ 30% giá hợp đồng, theo kế hoạch vốn năm 2027 (khoản 9.6)", "—", "—", vnd(c["tu27"])),
            ("1", "Báo cáo kết quả khảo sát xây dựng được nghiệm thu, phê duyệt", vnd(a_ks), vnd(th1), vnd(n1)),
            ("2", "BCKTKT đủ điều kiện trình thẩm định, được nghiệm thu (60% giá trị phần lập BCKTKT)", vnd(d2), vnd(th2), vnd(n2)),
            ("3", "Hồ sơ hoàn chỉnh sau thẩm định, dự án được phê duyệt, nghiệm thu hoàn thành (40% giá trị phần lập BCKTKT)", vnd(d3), "0", vnd(n3)),
            ("Cộng", "", vnd(gia), vnd(tu), vnd(gia)),
        ], can_giua=(0,), dam_cuoi=True)
        v.p(f"Giá trị phần khảo sát xây dựng {vnd(a_ks)} đồng; giá trị phần lập BCKTKT {vnd(a_tk)} đồng. Tạm ứng được thu hồi ở lần thanh toán thứ 1 (một nửa giá trị lần thanh toán) và thu hồi hết ở lần thanh toán thứ 2, trước khi giá trị thanh toán cộng dồn đạt 80% giá hợp đồng.", indent=0, sau=4)
    else:
        n_cuoi = gia - tu
        v.p("Hợp đồng trọn gói, giá hợp đồng " + vnd(gia) + " đồng. Thanh toán một lần sau khi Bên B hoàn thành toàn bộ công việc theo hợp đồng, theo thỏa thuận của hai bên tại biên bản thương thảo.", indent=0, sau=4)
        v.bang(["Lần", "Điều kiện thanh toán", "Giá trị (đồng)", "Thu hồi tạm ứng (đồng)", "Số tiền thanh toán (đồng)"],
               [1.9, 5.7, 3.2, 3.0, 3.2], [
            ("Tạm ứng năm 2026", "Sau khi hợp đồng có hiệu lực; phần vốn năm 2026 chia theo tỷ lệ giá hợp đồng (khoản 9.6)", "—", "—", vnd(c["tu26"])),
            ("Tạm ứng năm 2027", "Phần tạm ứng còn lại để đủ 30% giá hợp đồng, theo kế hoạch vốn năm 2027 (khoản 9.6)", "—", "—", vnd(c["tu27"])),
            ("1", "Bên B hoàn thành toàn bộ công việc, bàn giao đầy đủ hồ sơ; Bên A nghiệm thu hoàn thành hợp đồng", vnd(gia), vnd(tu), vnd(n_cuoi)),
            ("Cộng", "", vnd(gia), vnd(tu), vnd(gia)),
        ], can_giua=(0,), dam_cuoi=True)
    v.tieu_de("PHỤ LỤC SỐ 4")
    v.tieu_de("NHÂN LỰC CỦA BÊN NHẬN THẦU")
    v.p("Nhân sự chủ chốt theo hồ sơ năng lực của Bên B; thay đổi nhân sự thực hiện theo Điều 16.", indent=0, sau=4)
    hang = [(str(i), a, b_.rstrip(".")) for i, (a, b_) in enumerate(g["nhansu"], 1)]
    v.bang(["STT", "Vị trí, chức danh", "Nhân sự, chứng chỉ (hạng, thời hạn)"], [1.5, 5.5, 10.0], hang, can_giua=(0,))
    out = os.path.join(thu_muc, c["file_hd"])
    v.luu(out, f"Hợp đồng tư vấn — {c['ten_goi']} — Dự án CLC 2026-2030")
    return out


# ---------------------------------------------------------------- biên bản thương thảo (Phụ lục 4C TT 79/2025/TT-BTC)
def dung_bb(c, thu_muc):
    v = VanBan()
    b = c["b"]
    ks = c["ma"] == "KS"
    g = c["g"]
    v.dau("Số:        /BB-CĐKT", "Quảng Ngãi, ngày 22 tháng 10 năm 2026", "BIÊN BẢN THƯƠNG THẢO HỢP ĐỒNG",
          f"(đối với gói thầu cung cấp dịch vụ tư vấn)\nGói thầu: {c['ten_goi']}, thuộc Dự án “{TEN_DA}”")
    v.p(f"Căn cứ pháp lý: Luật Đấu thầu ngày 23/6/2023 (hợp nhất tại Văn bản hợp nhất số 74/VBHN-VPQH ngày 25/3/2026); Nghị định số 214/2025/NĐ-CP ngày 04/8/2025 của Chính phủ quy định chi tiết một số điều và biện pháp thi hành Luật Đấu thầu về lựa chọn nhà thầu (hợp nhất tại Văn bản hợp nhất số 36/2026/VBHN-NĐ-BTC ngày 23/9/2026); Thông tư số 79/2025/TT-BTC ngày 04/8/2025 của Bộ trưởng Bộ Tài chính; Luật Xây dựng ngày 10/12/2025; Nghị định số 210/2026/NĐ-CP ngày 15/6/2026 của Chính phủ quy định chi tiết và hướng dẫn thi hành một số điều của Luật Xây dựng về hợp đồng xây dựng; Quyết định số {VB['qd_2158']['so']} ngày {VB['qd_2158']['ngay']} phê duyệt nhiệm vụ và dự toán kinh phí chuẩn bị đầu tư Dự án; Quyết định số {VB['qd_2236']['so']} ngày {VB['qd_2236']['ngay']} phê duyệt Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư; {c['don']} kèm hồ sơ năng lực của {b['ten']}; dự thảo hợp đồng đã gửi trên Hệ thống mạng đấu thầu quốc gia.", italic=True, sau=6)
    v.p(f"Hôm nay, ngày {NGAY_TT}, tại {c['dia_diem_tt']}, chúng tôi, đại diện cho các bên thương thảo hợp đồng, gồm có:")
    khoi_ben(v, BEN_A, "Chủ đầu tư: Trường Cao đẳng Kon Tum", kieu="BB")
    khoi_ben(v, b, f"Nhà thầu: {b['ten'].replace('cổ phần', 'Cổ phần')}", kieu="BB")
    v.p("Hai bên đã thương thảo và thống nhất những nội dung trong hợp đồng như sau:")
    gia = c["gia"]
    gia_chu = bang_chu(gia)
    tu = c["tu"]
    nhansu = "; ".join(f"{a}: {t.rstrip('.')}" for a, t in g["nhansu"] if "Không yêu cầu" not in t and "Chứng chỉ năng lực" not in a)
    if ks:
        noi_dung = [
            "a) Thảo luận về điều khoản tham chiếu, phương pháp luận đề xuất, điều kiện cụ thể của hợp đồng và hoàn thiện phần “Mô tả dịch vụ”: Hai bên thống nhất phạm vi gồm khảo sát hiện trạng 03 ký túc xá (nhà G, nhà H, ký túc xá cơ sở Khoa Kỹ thuật - Công nghệ và Đào tạo - Sát hạch lái xe); lập BCKTKT gồm thuyết minh, thiết kế bản vẽ thi công, dự toán, tổng mức đầu tư và xác định chi phí 02 mô hình xe ô tô con số tự động phục vụ đào tạo; phối hợp thẩm định, giải trình, chỉnh sửa hồ sơ. Không bao gồm giám sát tác giả và thẩm tra độc lập. Việc hoàn thiện không làm thay đổi đáng kể phạm vi dịch vụ ban đầu;",
            f"b) Kế hoạch công tác và bố trí nhân sự: Nhà thầu bố trí đúng nhân sự chủ chốt đã nêu trong hồ sơ năng lực ({nhansu}); khảo sát xây dựng thực hiện và được Chủ đầu tư phê duyệt kết quả trước khi lập thiết kế bản vẽ thi công;",
            "c) Tiến độ: Thời gian thực hiện hợp đồng 120 ngày kể từ ngày hợp đồng có hiệu lực, đến khi nộp hồ sơ BCKTKT đủ điều kiện trình thẩm định; các mốc chủ yếu theo Phụ lục II của hợp đồng; thời gian thẩm định của cơ quan nhà nước không tính vào 120 ngày;",
            "d) Giải quyết thay đổi nhân sự: Thay đổi nhân sự chủ chốt phải được Chủ đầu tư chấp thuận bằng văn bản; nhân sự thay thế phải có trình độ, kinh nghiệm và chứng chỉ hành nghề tương đương hoặc cao hơn;",
            "đ) Bố trí điều kiện làm việc: Chủ đầu tư cung cấp tài liệu hiện có về công trình và phối hợp đơn vị quản lý ký túc xá bố trí điều kiện khảo sát an toàn; Nhà thầu tự bố trí phương tiện, thiết bị, điều kiện làm việc của nhân sự thuộc quyền quản lý của mình và chịu trách nhiệm về an toàn lao động;",
            f"e) Chi phí dịch vụ tư vấn: Hợp đồng trọn gói, giá {vnd(gia)} đồng (bằng chữ: {gia_chu[0].upper() + gia_chu[1:]}), bằng giá gói thầu, gồm khảo sát xây dựng {vnd(c['a_ks'])} đồng và lập BCKTKT {vnd(c['a_tk'])} đồng. Giá đã bao gồm các khoản thuế, phí, lệ phí; Nhà thầu trực tiếp kê khai và nộp thuế theo quy định của pháp luật về thuế. Tạm ứng 30% giá hợp đồng ({vnd(tu)} đồng), trong đó năm 2026 tạm ứng {vnd(c['tu26'])} đồng (kế hoạch vốn năm 2026 của Dự án 260.000.000 đồng chia cho hai hợp đồng theo tỷ lệ giá hợp đồng), năm 2027 tạm ứng phần còn lại {vnd(c['tu27'])} đồng; việc tạm ứng thực hiện sau khi hợp đồng có hiệu lực và trong phạm vi kế hoạch vốn được giao; thanh toán theo ba lần gắn với nghiệm thu khảo sát, nghiệm thu BCKTKT và phê duyệt dự án; thời hạn thanh toán không quá 14 ngày làm việc kể từ ngày nhận đủ hồ sơ hợp lệ; thưởng, phạt hợp đồng thực hiện ở mức tối thiểu theo quy định của Nhà nước;",
            "g) Các vấn đề phát sinh trong quá trình lựa chọn nhà thầu: Không có. Gói thầu chỉ định thầu rút gọn cho một nhà thầu; dự thảo hợp đồng đã được gửi trên Hệ thống mạng đấu thầu quốc gia;",
            "h) Các sai lệch do nhà thầu phát hiện, đề xuất, phương án thay thế: Không có;",
            "i) Các nội dung cần thiết khác: Hợp đồng được hoàn thiện theo Nghị định số 210/2026/NĐ-CP ngày 15/6/2026 của Chính phủ quy định chi tiết và hướng dẫn thi hành một số điều của Luật Xây dựng về hợp đồng xây dựng và mẫu hợp đồng xây dựng công bố tại Quyết định số 1040/QĐ-BXD ngày 26/6/2026 của Bộ trưởng Bộ Xây dựng về việc công bố mẫu hợp đồng xây dựng; Nhà thầu không phải nộp bảo đảm thực hiện hợp đồng (nhà thầu cung cấp dịch vụ tư vấn); căn cứ giao kết hợp đồng ghi số, ngày Quyết định phê duyệt kết quả lựa chọn nhà thầu sau khi được ban hành.",
        ]
    else:
        noi_dung = [
            "a) Thảo luận về điều khoản tham chiếu, phương pháp luận đề xuất, điều kiện cụ thể của hợp đồng và hoàn thiện phần “Mô tả dịch vụ”: Hai bên thống nhất Nhà thầu thực hiện tư vấn quản lý dự án từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án, gồm lập kế hoạch quản lý dự án; giám sát hợp đồng khảo sát và lập BCKTKT; hỗ trợ thẩm định, phê duyệt dự án và lựa chọn nhà thầu; quản lý chất lượng, khối lượng, tiến độ, chi phí, an toàn các hợp đồng thi công và thiết bị; kiểm tra thanh toán, quyết toán; hỗ trợ quyết toán dự án hoàn thành. Nhà thầu hỗ trợ Chủ đầu tư, không thay Chủ đầu tư về thẩm quyền và trách nhiệm pháp lý (Chủ đầu tư giữ lại, không giao: quyết định, phê duyệt; tổ chức lựa chọn nhà thầu và ký hợp đồng với nhà thầu khác; nghiệm thu, xác nhận khối lượng, quyết định thanh toán, quyết toán; làm việc với cơ quan nhà nước, chính quyền địa phương; giám sát việc thực hiện hợp đồng; Nhà thầu gửi văn bản thông báo nhiệm vụ, quyền hạn của người đại diện và bộ máy quản lý dự án trong 07 ngày kể từ ngày hợp đồng có hiệu lực; chi phí quản lý dự án của Chủ đầu tư và chi phí tư vấn không vượt chi phí quản lý dự án đã được phê duyệt); không đồng thời thực hiện tư vấn khảo sát, lập BCKTKT của Dự án;",
            f"b) Kế hoạch công tác và bố trí nhân sự: Nhà thầu bố trí đúng nhân sự chủ chốt đã nêu trong hồ sơ năng lực ({nhansu}), bảo đảm điều kiện năng lực theo quy định;",
            "c) Tiến độ: Thời gian thực hiện hợp đồng không quá 03 năm kể từ ngày hợp đồng có hiệu lực, từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án; hợp đồng có hiệu lực kể từ ngày ký; tiến độ chi tiết bám theo tiến độ của Dự án và Phụ lục II của hợp đồng;",
            "d) Giải quyết thay đổi nhân sự: Thay đổi nhân sự chủ chốt phải được Chủ đầu tư chấp thuận bằng văn bản; nhân sự thay thế phải có trình độ chuyên môn và kinh nghiệm tương đương hoặc tốt hơn;",
            "đ) Bố trí điều kiện làm việc: Nhà thầu tự bố trí điều kiện làm việc của nhân sự thuộc quyền quản lý và chịu trách nhiệm trước pháp luật về hành vi của nhân sự mình; Chủ đầu tư cung cấp tài liệu, thông tin cần thiết cho công việc;",
            f"e) Chi phí dịch vụ tư vấn: Hợp đồng trọn gói, giá {vnd(gia)} đồng (bằng chữ: {gia_chu[0].upper() + gia_chu[1:]}), bằng giá gói thầu; giá không thay đổi theo dự toán (trừ trường hợp điều chỉnh hợp đồng theo quy định). Giá đã bao gồm các khoản thuế, phí, lệ phí; Nhà thầu trực tiếp kê khai và nộp thuế. Tạm ứng {vnd(tu)} đồng (30% giá hợp đồng), trong đó năm 2026 tạm ứng {vnd(c['tu26'])} đồng (kế hoạch vốn năm 2026 của Dự án 260.000.000 đồng chia cho hai hợp đồng theo tỷ lệ giá hợp đồng), năm 2027 tạm ứng phần còn lại {vnd(c['tu27'])} đồng; việc tạm ứng thực hiện sau khi hợp đồng có hiệu lực và trong phạm vi kế hoạch vốn được giao; thanh toán 03 lần theo khối lượng công việc hoàn thành được nghiệm thu của ba giai đoạn (chuẩn bị đầu tư; thực hiện đầu tư; kết thúc, quyết toán), trong phạm vi kế hoạch vốn do cấp có thẩm quyền giao; thời hạn thanh toán không quá 14 ngày làm việc kể từ ngày nhận đủ hồ sơ hợp lệ; hình thức chuyển khoản, đồng tiền Việt Nam; thưởng, phạt hợp đồng thực hiện ở mức tối thiểu theo quy định của Nhà nước;",
            "g) Các vấn đề phát sinh trong quá trình lựa chọn nhà thầu: Không có. Gói thầu chỉ định thầu rút gọn cho một nhà thầu; dự thảo hợp đồng đã được gửi trên Hệ thống mạng đấu thầu quốc gia;",
            "h) Các sai lệch do nhà thầu phát hiện, đề xuất, phương án thay thế: Không có;",
            "i) Các nội dung cần thiết khác: Hợp đồng được hoàn thiện theo Nghị định số 210/2026/NĐ-CP ngày 15/6/2026 của Chính phủ quy định chi tiết và hướng dẫn thi hành một số điều của Luật Xây dựng về hợp đồng xây dựng và mẫu hợp đồng xây dựng công bố tại Quyết định số 1040/QĐ-BXD ngày 26/6/2026 của Bộ trưởng Bộ Xây dựng về việc công bố mẫu hợp đồng xây dựng; Nhà thầu không phải nộp bảo đảm thực hiện hợp đồng và bảo lãnh tạm ứng; nếu chưa bảo đảm vốn các năm sau thì hai bên thỏa thuận tạm dừng thanh toán theo hợp đồng; căn cứ giao kết hợp đồng ghi số, ngày Quyết định phê duyệt kết quả lựa chọn nhà thầu sau khi được ban hành.",
        ]
    for t in noi_dung:
        v.p(t, indent=1.0, sau=4)
    gio_kt = "16 giờ 30 phút" if c["ma"] == "QLDA" else "       giờ        "  # QLDA: anh đã điền 16 giờ 30 phút
    v.p(f"Việc thương thảo hợp đồng kết thúc vào {gio_kt} ngày 22/10/2026. Biên bản thương thảo hợp đồng được lập thành 04 bản, Chủ đầu tư giữ 02 bản, nhà thầu giữ 02 bản, các biên bản có giá trị pháp lý như nhau./.", indent=1.0, sau=8)
    v.giu_cuoi()
    chu_ky_hd(v, c, bb=True)
    out = os.path.join(thu_muc, c["file_bb"])
    v.luu(out, f"Biên bản thương thảo hợp đồng — {c['ten_goi']} — Dự án CLC 2026-2030")
    return out


# ---------------------------------------------------------------- biên bản đối chiếu tài liệu (Phụ lục 4A TT 79/2025/TT-BTC)
def dung_dc(c, thu_muc):
    v = VanBan()
    b = c["b"]
    v.dau("", "Quảng Ngãi, ngày 22 tháng 10 năm 2026", "BIÊN BẢN ĐỐI CHIẾU TÀI LIỆU",
          f"Gói thầu: {c['ten_goi']}\nThuộc Dự án “{TEN_DA}”")
    v.p(f"Thời gian, địa điểm đối chiếu: Ngày {NGAY_TT}, tại {c['dia_diem_tt']}.")
    v.p(f"1. Tên nhà thầu được đối chiếu tài liệu: {b['ten']}.", bold=False)
    v.p(f"Đại diện nhà thầu được đối chiếu tài liệu là {b['dd']}, {b['cv']} (người đại diện theo pháp luật).")
    v.p("2. Tên cá nhân được phân công đối chiếu tài liệu:")
    # nhân sự đối chiếu: anh Phục đã cập nhật trực tiếp vào bản v2 ngày 28/10/2026 — kế thừa, không để trống
    v.p("Ông: Nguyễn Ngọc Quang Phục, Phó Trưởng phòng TH-HC&QT.")
    v.p("Ông: Đỗ Thành Công, Chuyên viên phòng TH-HC&QT.")
    v.p("Bà: Phạm Thị Thoa, Viên chức phòng TC-KT.")
    v.p("3. Kết quả đối chiếu tài liệu:")
    v.p("a) Thông tin về tính hợp lệ của hồ sơ nhà thầu (đơn xin nhận thầu, giấy chứng nhận đăng ký doanh nghiệp, hồ sơ năng lực): Thống nhất.")
    v.p("Các nội dung không thống nhất: Không có.")
    v.p("b) Thông tin về năng lực, kinh nghiệm: Thống nhất.")
    v.p("Các nội dung không thống nhất: Không có. Nội dung đã đối chiếu:")
    for t in c["ghi_nhan"]:
        v.p("- " + t, indent=0, trai=1.27)
    v.p("4. Kết luận về việc đối chiếu tài liệu:")
    v.p("☒ Thống nhất với thông tin kê khai, được mời vào thương thảo hợp đồng.")
    v.p("☐ Không thống nhất với thông tin kê khai.")
    v.p("Ý kiến khác (nếu có): Không có.")
    v.giu_cuoi()
    v.ky("ĐẠI DIỆN NHÀ THẦU", b["cv"].split(" kiêm ")[-1].upper() if " kiêm " in b["cv"] else b["cv"].upper(),
         b["dd"].replace("Ông ", ""), "ĐẠI DIỆN CHỦ ĐẦU TƯ", "HIỆU TRƯỞNG", BEN_A["dd"].replace("Ông ", ""),
         None)
    out = os.path.join(thu_muc, c["file_dc"])
    v.luu(out, f"Biên bản đối chiếu tài liệu — {c['ten_goi']} — Dự án CLC 2026-2030")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=ket_qua("2026-10-28", "Hop-dong-tu-van"))
    ap.add_argument("--goi", choices=["KS", "QLDA"])
    ap.add_argument("--chi", choices=["hd", "bb", "dc"])
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for ma in ([a.goi] if a.goi else ["KS", "QLDA"]):
        c = cau_hinh(ma)
        if a.chi in (None, "dc"):
            print(dung_dc(c, a.out))
        if a.chi in (None, "hd"):
            print(dung_hd(c, a.out))
        if a.chi in (None, "bb"):
            print(dung_bb(c, a.out))

