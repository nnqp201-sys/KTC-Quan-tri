# -*- coding: utf-8 -*-
"""Dựng hợp đồng tư vấn đúng bố cục 4 phần của mẫu hợp đồng xây dựng công bố kèm QĐ 1040/QĐ-BXD ngày 26/6/2026.

Bìa · Mục lục · Danh mục từ viết tắt · Phần 1 Thông tin giao dịch · Phần 2 Căn cứ giao kết ·
Phần 3 Điều kiện chung (NGUYÊN VĂN mẫu, chỉ điền chỗ trống) · Phần 4 Điều kiện cụ thể (điền theo gói thầu) · Phụ lục.

  QLDA  → mẫu Phụ lục III (hợp đồng tư vấn quản lý dự án)
  KS    → mẫu Phụ lục II (tư vấn thiết kế xây dựng) + Phụ lục V (tư vấn khảo sát xây dựng)
          (hướng dẫn sử dụng QĐ 1040, mục 5.2: loại hợp đồng chưa có mẫu riêng thì vận dụng các mẫu đã công bố)

Chạy:  python -X utf8 lap_hop_dong_1040.py --out THƯ_MỤC [--goi KS|QLDA]
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lap_hop_dong_tu_van as L  # noqa: E402
import mau_1040  # noqa: E402
from hd1040_dkc import lay_dkc, con_trong  # noqa: E402
from vb_lib import bang_chu, vnd  # noqa: E402
from vb_mau import VanBanMau  # noqa: E402

TEN_DA, VB, CH, BEN_A = L.TEN_DA, L.VB, L.CH, L.BEN_A
HOA = lambda s: s[0].upper() + s[1:]  # noqa: E731


def chu_tien(n):
    return HOA(bang_chu(n))


# ============================================================ phần 3 — điều kiện chung nguyên văn mẫu
def lay_mau(ma):
    dg = mau_1040.doc_dong()
    t = {"II": mau_1040.tach(dg, "II"), "III": mau_1040.tach(dg, "III"), "V": mau_1040.tach(dg, "V")}
    return t


def _so_dong(t):
    return lambda d: d


def quy_tac_thay(c):
    """Các chỗ ĐKC khác mẫu — mỗi dòng là một chỗ điền/ điều chỉnh có chủ đích (xem bảng đối chiếu giao kèm)."""
    b = c["b"]
    ten_goi = c["ten_goi"]
    ks = c["ma"] == "KS"
    cong_trinh = ("Công trình là 03 ký túc xá (nhà G, nhà H và ký túc xá tại cơ sở Khoa Kỹ thuật - Công nghệ và Đào tạo - Sát hạch lái xe) và hạng mục thiết bị thuộc Dự án."
                  if ks else "Công trình là các hạng mục công trình xây dựng và thiết bị thuộc Dự án.")

    def sau_so(noi_dung):
        return lambda d: re.match(r"^(\d+\.\d+\.)\s", d).group(1) + " " + noi_dung

    r = [
        (r"^1\.1\. Bên giao thầu là", sau_so("Bên giao thầu là Trường Cao đẳng Kon Tum.")),
        (r"^1\.2\. Bên nhận thầu là", sau_so(f"Bên nhận thầu là {b['ten']}.")),
        (r"^1\.4\. Công trình là", sau_so(cong_trinh)),
        (r"^1\.5\. Dự án là", sau_so(f"Dự án là Dự án “{TEN_DA}”.")),
        (r"^1\.(9|10)\. Gói thầu là", sau_so(f"Gói thầu là gói thầu “{ten_goi}” thuộc Kế hoạch lựa chọn nhà thầu giai đoạn chuẩn bị đầu tư của Dự án.")),
        (r"^1\.\d+\. HSDT hoặc HSĐX", sau_so(f"HSDT hoặc HSĐX (nếu có) của Bên nhận thầu là {c['don']} kèm hồ sơ năng lực của Bên nhận thầu (gói thầu chỉ định thầu rút gọn).")),
        (r"^1\.\d+\. HSMT hoặc HSYC", sau_so("HSMT hoặc HSYC (nếu có) của Bên giao thầu: không áp dụng đối với hợp đồng này vì gói thầu thực hiện theo hình thức chỉ định thầu rút gọn; yêu cầu của gói thầu thể hiện tại Phụ lục số 1 và Biên bản thương thảo, hoàn thiện hợp đồng.")),
        (r"^6\.1\. Nội dung và khối lượng", lambda d: d.replace("[HSMT (hoặc HSYC) của Bên giao thầu]", "Phụ lục số 1 của hợp đồng")),
        (r"^12\.2\.4\.", lambda d: re.sub(r"thời hạn \.\.\. \(\.\.\.\) ngày làm việc", "thời hạn 07 (bảy) ngày làm việc", d)),
        (r"^a\) Bên nhận thầu không tuân thủ về bảo đảm thực hiện hợp đồng",
         "a) Bên nhận thầu không tuân thủ về bảo đảm thực hiện hợp đồng (không áp dụng đối với hợp đồng này vì Bên nhận thầu là nhà thầu cung cấp dịch vụ tư vấn, các bên không thỏa thuận bảo đảm thực hiện hợp đồng)."),
        (r"^19\.2\.", lambda d: d.replace("hoàn tất trong thời hạn ... ngày", "hoàn tất trong thời hạn 45 (bốn mươi lăm) ngày")),
        (r"^\(Trường hợp thời gian hiệu lực của hợp đồng khác", ""),
    ]
    return r


def dkc_theo_goi(c, T):
    """Trả danh sách [(số điều, tên, [dòng])] của Phần 3."""
    thay = quy_tac_thay(c)
    if c["ma"] == "QLDA":
        return lay_dkc("III", T["III"]["dkc"], thay)
    # KS: nền Phụ lục II (thiết kế) + bổ sung phần khảo sát của Phụ lục V
    dkc = {n: {"ten": v["ten"], "dong": list(v["dong"])} for n, v in T["II"]["dkc"].items()}
    # Điều 6: 6.1 (thiết kế) + các đầu việc khảo sát của mẫu V đánh số tiếp
    d6 = dkc[6]["dong"]
    i62 = next(i for i, d in enumerate(d6) if d.startswith("6.2."))
    kham = [d for d in T["V"]["dkc"][6]["dong"] if re.match(r"^6\.1\.\d+\.", d)]
    moi = []
    base_n = len([d for d in d6 if re.match(r"^6\.1\.\d+\.", d)])
    for k, d in enumerate(kham, 1):
        moi.append(re.sub(r"^6\.1\.\d+\.", "6.1.%d." % (base_n + k), d))
    dkc[6]["dong"] = d6[:i62] + moi + d6[i62:]
    thay += [
        (r"^10\.2\.1\.", lambda d: d.replace("nhiệm vụ tư vấn thiết kế xây dựng", "nhiệm vụ tư vấn khảo sát xây dựng và thiết kế xây dựng")),
        (r"^8\.2\.", lambda d: d.replace("Phụ lục số ... [Tiến độ thực hiện hợp đồng]", "Phụ lục số 2")),
    ]
    return lay_dkc("II", dkc, thay)


# ============================================================ phần 4 — điều kiện cụ thể
def tien(n):
    return f"{vnd(n)} đồng (bằng chữ: {chu_tien(n)} đồng)"


def chia_thanh_toan_qlda(gia, tu):
    """Thanh toán QLDA theo khối lượng công việc hoàn thành của 3 giai đoạn (tỷ lệ 25% - 50% - 25%: ĐỀ XUẤT, người có thẩm quyền chốt)."""
    t1, t2 = 25, 50
    p1 = (gia * t1 + 50) // 100
    p2 = (gia * t2 + 50) // 100
    p3 = gia - p1 - p2
    r1 = (tu * 40 + 50) // 100
    r2 = tu - r1
    assert r1 <= p1 and r2 <= p2
    return dict(t1=t1, t2=t2, p1=p1, p2=p2, p3=p3, r1=r1, r2=r2, n1=p1 - r1, n2=p2 - r2, n3=p3)


def dkct_chung(c):
    """Các điều chung cho cả hai gói (13–20) — điền theo mẫu và NĐ 210/2026."""
    return [
        (13, "Giải quyết tranh chấp, khiếu nại trong quá trình thực hiện hợp đồng", [
            "13.1.1. Phương thức giải quyết tranh chấp hợp đồng: Tranh chấp được giải quyết bằng thương lượng, hòa giải; nếu không thành, mỗi bên có quyền đề nghị Tòa án nhân dân có thẩm quyền giải quyết theo quy định tại khoản 5 Điều 86 Luật Xây dựng. Khi giải quyết tranh chấp, các bên tôn trọng các thỏa thuận hợp đồng và các cam kết trong quá trình thực hiện hợp đồng, bảo đảm khách quan, bình đẳng và hợp tác.",
            "13.1.3. Việc áp dụng mô hình giải quyết tranh chấp theo thông lệ quốc tế (mô hình ban xử lý tranh chấp):",
            "a) Thời điểm thành lập ban xử lý tranh chấp: Không áp dụng mô hình ban xử lý tranh chấp đối với hợp đồng này.",
            "b) Chi phí chi trả cho các thành viên tham gia ban xử lý tranh chấp và các chi phí khác có liên quan: Không áp dụng.",
            "13.2. Khiếu nại trong quá trình thực hiện hợp đồng",
            "13.2.4. Thời gian trả lời khiếu nại: 07 ngày làm việc kể từ ngày nhận được khiếu nại bằng văn bản; văn bản trả lời nêu rõ chấp thuận hoặc không chấp thuận nội dung khiếu nại; trường hợp không chấp thuận phải nêu rõ lý do.",
        ]),
        (14, "Rủi ro, sự kiện bất khả kháng và hoàn cảnh thay đổi cơ bản", [
            "14.1. Các trường hợp rủi ro có thể lường trước được: thay đổi nhân sự chủ chốt của Bên nhận thầu; Bên giao thầu cung cấp tài liệu, thông tin chậm; cơ quan nhà nước thẩm định, phê duyệt chậm; chưa bố trí hoặc chưa đủ kế hoạch vốn. Rủi ro do bên nào có khả năng kiểm soát tốt hơn thì bên đó quản lý, xử lý và chịu chi phí khắc phục.",
            "14.2.7. Các trường hợp bất khả kháng: chiến tranh, bạo loạn, đình công, hỏa hoạn, lũ lụt, thiên tai, dịch bệnh, cách ly do kiểm dịch hoặc các chính sách, quy định của Nhà nước ban hành sau khi giao kết hợp đồng mà các bên không thể lường trước và không thể khắc phục được.",
            "14.3.1. Các sự kiện được coi là hoàn cảnh thay đổi cơ bản: Nhà nước thay đổi chính sách, pháp luật (kể cả quy định về quản lý vốn đầu tư công) ảnh hưởng trực tiếp đến nội dung hợp đồng, và các trường hợp khác đáp ứng các điều kiện nêu tại khoản 14.3.1 Điều 14 phần Điều kiện chung, phù hợp các tiêu chí của Bộ luật Dân sự.",
            "14.3.2. Thông báo về hoàn cảnh thay đổi cơ bản: Bên nhận được thông báo phải trả lời đồng ý, không đồng ý hoặc ý kiến khác trong thời hạn 07 ngày làm việc kể từ ngày nhận được thông báo.",
        ]),
        (15, "Nhà thầu phụ (nếu có)", [
            "15.1. Việc sử dụng nhà thầu phụ, nhà thầu phụ do Bên giao thầu chỉ định: " + (
                "Bên nhận thầu không giao thầu phụ phần việc chính của hợp đồng. Việc thuê đơn vị thí nghiệm, đo đạc đủ điều kiện năng lực cho một phần công việc khảo sát phải được Bên giao thầu chấp thuận bằng văn bản trên cơ sở Điều 19 Nghị định số 210/2026/NĐ-CP; Bên nhận thầu chịu trách nhiệm trước Bên giao thầu về công việc do nhà thầu phụ thực hiện; Bên giao thầu không chỉ định nhà thầu phụ."
                if c["ma"] == "KS" else
                "Bên nhận thầu không giao thầu phụ phần việc của hợp đồng này. Việc thuê chuyên gia hoặc đơn vị hỗ trợ cho một phần công việc phải được Bên giao thầu chấp thuận bằng văn bản trên cơ sở Điều 19 Nghị định số 210/2026/NĐ-CP; Bên nhận thầu chịu trách nhiệm trước Bên giao thầu về công việc đó; Bên giao thầu không chỉ định nhà thầu phụ."),
            "15.3. Các tình huống Bên giao thầu được chỉ định nhà thầu phụ: Không có.",
            "15.4. Bên giao thầu được thanh toán trực tiếp cho nhà thầu phụ trên cơ sở đề xuất của nhà thầu chính và các thỏa thuận trong hợp đồng: Không được.",
        ]),
        (16, "Nhân lực của Bên nhận thầu", [
            "16.3. Bên nhận thầu phải gửi văn bản thông báo cho Bên giao thầu trong vòng 07 ngày kể từ ngày nhận được yêu cầu của Bên giao thầu về việc thay đổi nhân sự.",
        ]),
        (17, "Sửa đổi hợp đồng", [
            "17.1. Nội dung, phạm vi và các trường hợp được sửa đổi hợp đồng; quy trình, thủ tục sửa đổi hợp đồng: Hợp đồng chỉ được sửa đổi bằng phụ lục hoặc văn bản sửa đổi do hai bên ký, phù hợp Điều 84 Luật Xây dựng và Điều 22, 23, 24, 25 Nghị định số 210/2026/NĐ-CP, trong các trường hợp: thay đổi phạm vi, khối lượng công việc; thay đổi thời gian, tiến độ; bất khả kháng; hoàn cảnh thay đổi cơ bản; thay đổi chính sách, pháp luật; các trường hợp khác do hai bên thỏa thuận phù hợp pháp luật. Bên đề nghị sửa đổi gửi đề nghị bằng văn bản nêu rõ nội dung, lý do; bên kia trả lời trong thời hạn quy định tại khoản 4.1 Điều 4.",
            "17.2. Các trường hợp được điều chỉnh khối lượng, phạm vi và trình tự, thủ tục điều chỉnh khối lượng: Khi Bên giao thầu yêu cầu hoặc Bên nhận thầu đề nghị điều chỉnh khối lượng, phạm vi công việc và được Bên giao thầu chấp thuận bằng văn bản trước khi thực hiện; phần giá trị phát sinh xác định theo dự toán được Bên giao thầu phê duyệt, trong phạm vi chi phí đã được duyệt của Dự án (Điều 84 Luật Xây dựng, Điều 23 Nghị định số 210/2026/NĐ-CP).",
            "17.3.1. Các trường hợp được điều chỉnh thời gian, tiến độ thực hiện và thời hạn hoàn thành các công việc, sản phẩm cụ thể của hợp đồng: do bất khả kháng; hoàn cảnh thay đổi cơ bản; Bên giao thầu hoặc cơ quan nhà nước chậm cung cấp tài liệu, chậm thẩm định, phê duyệt; thay đổi phạm vi công việc; trường hợp khác do hai bên thỏa thuận. Bên gây chậm do lỗi của mình chịu trách nhiệm đối với thiệt hại do chậm theo thỏa thuận tại hợp đồng.",
            "17.3.2. Trường hợp điều chỉnh thời gian hoặc tiến độ thực hiện và thời hạn hoàn thành các công việc, sản phẩm cụ thể của hợp đồng làm vượt thời gian thực hiện Dự án thì Bên giao thầu báo cáo người quyết định đầu tư xem xét, quyết định trước khi điều chỉnh hợp đồng.",
            "17.4. Điều chỉnh giá hợp đồng trọn gói: Giá hợp đồng trọn gói chỉ được điều chỉnh khi phát sinh hợp lý khối lượng, công việc (tăng hoặc giảm) do điều chỉnh phạm vi công việc theo yêu cầu của Bên giao thầu hoặc đề nghị của Bên nhận thầu được Bên giao thầu chấp thuận, hoặc khi xảy ra sự kiện bất khả kháng, hoàn cảnh thay đổi cơ bản theo quy định tại Điều 14.",
        ]),
        (18, "Tạm dừng và chấm dứt hợp đồng", [
            "18.1.1. đ) Một bên được tạm dừng thực hiện hợp đồng: Bên giao thầu chưa bảo đảm kế hoạch vốn để thanh toán theo thỏa thuận tại Điều 9; Bên giao thầu không thanh toán khoản đến hạn quá 28 ngày kể từ ngày hết hạn thanh toán (Điều 26 Nghị định số 210/2026/NĐ-CP). Phạm vi tạm dừng là toàn bộ hoặc một phần công việc tùy theo vốn và mức độ ảnh hưởng.",
            "18.1.2. Bên tạm dừng hợp đồng phải thông báo trước cho bên kia bằng văn bản trước 28 ngày, trừ trường hợp bất khả kháng. Bên không thực hiện nghĩa vụ thông báo mà gây thiệt hại thì bồi thường trên cơ sở toàn bộ thiệt hại thực tế.",
            "18.2.1. Bên giao thầu có thể chấm dứt hợp đồng sau 28 ngày kể từ ngày gửi văn bản kết thúc hợp đồng đến Bên nhận thầu. Thời hạn quy định tại điểm b khoản 18.2.1: 28 ngày; thời hạn quy định tại điểm c khoản 18.2.1: 28 ngày liên tục không thực hiện công việc theo hợp đồng.",
            "18.2.2. Bên nhận thầu có thể chấm dứt hợp đồng nhưng phải thông báo bằng văn bản trước cho Bên giao thầu tối thiểu 28 ngày. Thời gian công việc bị ngừng do lỗi của Bên giao thầu quy định tại điểm a: 56 ngày; thời gian Bên giao thầu không thanh toán quy định tại điểm b: 56 ngày kể từ ngày nhận đủ hồ sơ thanh toán hợp lệ; thời gian quy định tại điểm d (sự kiện bất khả kháng): 56 ngày.",
            "18.3. Thưởng, phạt hợp đồng và bồi thường thiệt hại (khoản 1, 2, 3 Điều 86 Luật Xây dựng): Thưởng, phạt do vi phạm hợp đồng thực hiện ở mức tối thiểu theo quy định của Nhà nước: các bên không thỏa thuận mức thưởng ngoài giá hợp đồng; mức phạt do vi phạm nghĩa vụ hợp đồng không vượt 12% giá trị phần hợp đồng bị vi phạm và chỉ áp dụng khi có biên bản xác nhận của hai bên. Ngoài mức phạt, bên vi phạm bồi thường thiệt hại thực tế cho bên kia theo quy định của pháp luật.",
        ]),
    ]


def dkct_20(c, so_trang):
    return (20, "Điều khoản chung", [
        "Hợp đồng này có hiệu lực kể từ ngày hai bên ký.",
        f"Hợp đồng này bao gồm {so_trang} trang và 05 Phụ lục, được ký bằng chữ ký số và lập bằng tiếng Việt, có giá trị pháp lý như nhau; mỗi bên giữ 01 bản điện tử có chữ ký số của cả hai bên.",
    ])


def dkct_goi(c):
    ks = c["ma"] == "KS"
    gia = c["gia"]
    qd = c["qd"]
    tu = c["tu"]
    don = c["don"]
    L1 = []  # điều 2, 4
    L1.append((2, "Hồ sơ hợp đồng và thứ tự ưu tiên", [
        f"2.2. Thứ tự ưu tiên áp dụng các tài liệu của Hồ sơ hợp đồng: (1) Văn bản hợp đồng này (Phần 1, Phần 2, Điều kiện cụ thể, Điều kiện chung) và các Phụ lục; (2) Quyết định số {qd['so']} ngày {qd['ngay']} phê duyệt kết quả lựa chọn nhà thầu (chỉ định thầu); (3) Biên bản thương thảo, hoàn thiện hợp đồng và Biên bản đối chiếu tài liệu ngày {L.NGAY_TT}; (4) {don} và hồ sơ năng lực của Bên nhận thầu; (5) Các tài liệu khác có liên quan do hai bên thống nhất. Nội dung trái pháp luật không có hiệu lực.",
    ]))
    L1.append((4, "Trao đổi thông tin", [
        "4.2. Thời hạn thông báo khi thay đổi thông tin giao dịch: 07 ngày kể từ ngày phát sinh thay đổi.",
        "Đại diện quản lý thực hiện hợp đồng: Bên giao thầu cử lãnh đạo phòng Tổng hợp - Hành chính và Quản trị; Bên nhận thầu cử " + ("chủ nhiệm khảo sát và chủ nhiệm lập BCKTKT" if ks else "giám đốc quản lý dự án") + " ghi tại Phụ lục số 4; thông tin nhân sự của Bên giao thầu tại Phụ lục số 5.",
    ]))
    if ks:
        L1.append((6, "Nội dung, khối lượng công việc và sản phẩm của hợp đồng", [
            "6.2. Sản phẩm của hợp đồng gồm: (1) Nhiệm vụ khảo sát (hỗ trợ lập) và phương án kỹ thuật khảo sát xây dựng; (2) Báo cáo kết quả khảo sát xây dựng (Điều 14 Nghị định số 217/2026/NĐ-CP); (3) Thuyết minh Báo cáo kinh tế - kỹ thuật (Điều 30 Nghị định số 217/2026/NĐ-CP); (4) Hồ sơ thiết kế bản vẽ thi công 03 ký túc xá và chỉ dẫn kỹ thuật (Điều 23 Nghị định số 217/2026/NĐ-CP); (5) Danh mục, cấu hình kỹ thuật, chi phí 02 mô hình xe ô tô con số tự động; (6) Dự toán xây dựng, tổng mức đầu tư và bảng tính chi phí (Nghị định số 206/2026/NĐ-CP); (7) Hồ sơ phục vụ thủ tục kèm theo; (8) Báo cáo giải trình, hồ sơ chỉnh sửa theo kết quả thẩm định và bộ hồ sơ chính thức sau phê duyệt; bao gồm nhưng không giới hạn các nội dung quy định tại Nghị định quy định chi tiết một số điều của Luật Xây dựng về quản lý hoạt động xây dựng. Chi tiết, số lượng và quy cách tại Phụ lục số 1.",
            "6.3. Phạm vi không thuộc hợp đồng: giám sát tác giả, thẩm tra độc lập thiết kế và dự toán, thủ tục xin giấy phép (khoản 11.2.15 Điều 11 phần Điều kiện chung không áp dụng đối với giám sát tác giả); khi Bên giao thầu yêu cầu, hai bên ký phụ lục hoặc hợp đồng riêng.",
            "6.4. Khảo sát xây dựng phải hoàn thành và được Bên giao thầu phê duyệt kết quả trước khi lập thiết kế bản vẽ thi công.",
        ]))
        L1.append((7, "Yêu cầu về chất lượng, số lượng sản phẩm", [
            "7.2. Số lượng hồ sơ sản phẩm tư vấn xây dựng của hợp đồng: 01 bộ hồ sơ điện tử có chữ ký số (định dạng .pdf) kèm tệp gốc (.dwg, .docx, .xlsx) cho từng sản phẩm; số lượng theo từng sản phẩm tại Phụ lục số 1.",
        ]))
        L1.append((8, "Thời gian và tiến độ thực hiện hợp đồng", [
            "8.1. Thời gian thực hiện các công việc của hợp đồng là 120 ngày kể từ ngày hợp đồng có hiệu lực, đến khi Bên nhận thầu nộp hồ sơ BCKTKT đủ điều kiện để Bên giao thầu trình thẩm định. Thời gian thẩm định, phê duyệt của cơ quan nhà nước không tính vào thời gian này; việc giải trình, chỉnh sửa theo yêu cầu thực hiện trong thời hạn Bên giao thầu yêu cầu, không quá 15 ngày kể từ ngày nhận được yêu cầu.",
            "8.3. Tiến độ chi tiết: Thời gian và phần công việc hoàn thành theo Phụ lục số 2.",
        ]))
    else:
        L1.append((6, "Nội dung, khối lượng công việc và sản phẩm của hợp đồng", [
            "6.1. Phạm vi thuê tư vấn quản lý dự án (khoản 1 Điều 46 Nghị định số 217/2026/NĐ-CP): Bên giao thầu thuê Bên nhận thầu thực hiện một phần nội dung quản lý dự án, từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án; các công việc nêu tại khoản 6.1 Điều 6 phần Điều kiện chung do Bên nhận thầu thực hiện hoặc hỗ trợ Bên giao thầu thực hiện phù hợp từng giai đoạn của Dự án, theo Phụ lục số 1.",
            "Bên giao thầu giữ lại, không giao cho Bên nhận thầu, các công việc thuộc thẩm quyền và trách nhiệm của chủ đầu tư, gồm: (a) Quyết định, phê duyệt các nội dung thuộc thẩm quyền (kế hoạch lựa chọn nhà thầu, kết quả lựa chọn nhà thầu, điều chỉnh, phát sinh, thay đổi nhân sự chủ chốt của Bên nhận thầu); (b) Tổ chức lựa chọn nhà thầu; ký kết, sửa đổi, chấm dứt hợp đồng với các nhà thầu khác của Dự án; (c) Nghiệm thu, xác nhận khối lượng, quyết định thanh toán, quyết toán và đề nghị giải ngân; (d) Làm việc với cơ quan nhà nước, chính quyền địa phương; xử lý các vấn đề giữa Bên nhận thầu với các nhà thầu và chính quyền địa phương; giám sát việc thực hiện hợp đồng này (khoản 4 Điều 46 Nghị định số 217/2026/NĐ-CP). Đối với các công việc tại các khoản 6.1.1, 6.1.2, 6.1.8 và 6.1.9 Điều 6 phần Điều kiện chung, Bên nhận thầu chỉ tham mưu, hỗ trợ; Bên giao thầu quyết định và chịu trách nhiệm theo thẩm quyền.",
            "Bên nhận thầu không đồng thời thực hiện tư vấn khảo sát, lập BCKTKT của Dự án. Tổng chi phí quản lý dự án do Bên giao thầu và Bên nhận thầu thực hiện không vượt chi phí quản lý dự án đã được phê duyệt (khoản 5 Điều 25 Nghị định số 206/2026/NĐ-CP); phần chi phí quản lý dự án của Bên giao thầu được xác định riêng trong dự toán chi phí quản lý dự án đã được phê duyệt.",
            "Trong thời hạn 07 ngày kể từ ngày hợp đồng có hiệu lực, Bên nhận thầu gửi Bên giao thầu và các nhà thầu có liên quan văn bản thông báo nhiệm vụ, quyền hạn của người đại diện và bộ máy trực tiếp quản lý dự án; giám đốc quản lý dự án và người phụ trách bộ phận chuyên môn bảo đảm điều kiện theo khoản 2 Điều 46 Nghị định số 217/2026/NĐ-CP.",
            "6.2. Sản phẩm của hợp đồng gồm: (1) Kế hoạch quản lý dự án; (2) Ý kiến bằng văn bản về nhiệm vụ, phương án, báo cáo khảo sát và BCKTKT; (3) Đề xuất phân gói thầu, dự thảo kế hoạch và hồ sơ lựa chọn nhà thầu các gói tiếp theo; (4) Báo cáo công tác quản lý điều hành dự án hằng quý; (5) Số liệu phục vụ báo cáo giải ngân hằng tháng; (6) Biên bản, nhật ký, ý kiến kiểm soát chất lượng, khối lượng, thanh toán các hợp đồng; (7) Hồ sơ hoàn thành, hồ sơ quyết toán dự án hoàn thành (phần tư vấn hỗ trợ); (8) Hồ sơ bàn giao toàn bộ hồ sơ quản lý dự án; bao gồm nhưng không giới hạn hồ sơ về quản lý tiến độ, quản lý chi phí, quản lý chất lượng công trình, quản lý hợp đồng xây dựng, quản lý an toàn lao động và các báo cáo theo quy định. Chi tiết, số lượng và quy cách tại Phụ lục số 1.",
        ]))
        L1.append((7, "Yêu cầu về chất lượng, số lượng sản phẩm", [
            "7.2. Số lượng hồ sơ sản phẩm tư vấn xây dựng của hợp đồng: 01 bộ hồ sơ điện tử có chữ ký số cho từng sản phẩm; báo cáo định kỳ nộp hằng quý; chi tiết tại Phụ lục số 1.",
        ]))
        L1.append((8, "Thời gian và tiến độ thực hiện hợp đồng", [
            "8.1. Thời gian thực hiện các công việc của hợp đồng không quá 03 năm kể từ ngày hợp đồng có hiệu lực, từ giai đoạn chuẩn bị đầu tư đến khi quyết toán hoàn thành dự án.",
            "8.3. Tiến độ chi tiết: Thời gian và phần công việc hoàn thành bám theo tiến độ của Dự án và các mốc nêu tại Phụ lục số 2.",
        ]))
    # điều 9
    d9 = [f"9.1.2. Giá hợp đồng được xác định với số tiền: {tien(gia)}" + (f", gồm khảo sát xây dựng {tien(c['a_ks'])} và lập BCKTKT (kể cả thiết kế bản vẽ thi công) {tien(c['a_tk'])}." if ks else ", bằng giá trúng thầu tại Quyết định số %s." % qd["so"]),
          "9.2.1. Tạm ứng:",
          f"a) Mức tạm ứng, số lần tạm ứng: {c['ty_le_tu']}% giá hợp đồng, bằng {tien(tu)}, tạm ứng làm 02 lần: lần 1 năm 2026 là {tien(c['tu26'])} (phần kế hoạch vốn năm 2026 của Dự án 260.000.000 đồng chia cho hai hợp đồng tư vấn chuẩn bị đầu tư theo tỷ lệ giá hợp đồng); lần 2 năm 2027 là {tien(c['tu27'])} (phần còn lại để đủ mức {c['ty_le_tu']}% giá hợp đồng, theo kế hoạch vốn năm 2027 được cấp có thẩm quyền giao). Mức tạm ứng nằm trong khoảng tối thiểu 20% và tối đa 30% giá hợp đồng đối với hợp đồng tư vấn có giá trị đến 10 tỷ đồng (điểm g, h khoản 3 Điều 12 Nghị định số 210/2026/NĐ-CP). Tổng tạm ứng không vượt kế hoạch vốn đầu tư công hằng năm của Dự án (khoản 4 Điều 9 Nghị định số 254/2025/NĐ-CP).",
          ]
    if ks:
        a_ks, a_tk = c["a_ks"], c["a_tk"]
        d2 = (a_tk * 60 + 50) // 100
        d3 = a_tk - d2
        th1 = (a_ks + 1) // 2
        th2 = tu - th1
        n1, n2, n3 = a_ks - th1, d2 - th2, d3
        d9 += [f"b) Cách thức hoàn trả tiền tạm ứng: Tiền tạm ứng được thu hồi qua các lần thanh toán khối lượng hoàn thành: lần thanh toán thứ 1 thu hồi {vnd(th1)} đồng, lần thanh toán thứ 2 thu hồi {vnd(th2)} đồng; thu hồi hết trước khi giá trị thanh toán thực tế (kể cả tạm ứng) đạt 80% giá trị hợp đồng (khoản 5 Điều 9 Nghị định số 254/2025/NĐ-CP).",
               "c) Thời điểm tạm ứng lần đầu và thời hạn: Trong thời hạn 07 ngày làm việc kể từ ngày hợp đồng có hiệu lực, Bên giao thầu nhận đủ đề nghị tạm ứng hợp lệ của Bên nhận thầu và đã có kế hoạch vốn tương ứng, Bên giao thầu hoàn tất thủ tục tạm ứng với Kho bạc Nhà nước; số tiền tạm ứng từng lần nêu tại điểm a. Phần tạm ứng chưa thực hiện do chưa có kế hoạch vốn được thực hiện khi có kế hoạch vốn; Bên nhận thầu không có quyền yêu cầu lãi hoặc bồi thường do việc chưa tạm ứng vì chưa có vốn.",
               "d) Bảo lãnh tạm ứng: Bên nhận thầu không phải nộp bảo lãnh tạm ứng vì giá trị tạm ứng không vượt 01 tỷ đồng (điểm c khoản 3 Điều 12 Nghị định số 210/2026/NĐ-CP; điểm b khoản 2 Điều 9 Nghị định số 254/2025/NĐ-CP). Bên nhận thầu sử dụng tiền tạm ứng đúng mục đích, đúng đối tượng; nếu phát sinh rủi ro không thu hồi được vốn tạm ứng thì chủ đầu tư và tổ chức, cá nhân liên quan chịu trách nhiệm hoàn trả ngân sách nhà nước theo quy định.",
               "9.2.2. Thanh toán",
               "a) Tiến độ thanh toán",
               f"(i) Số lần thanh toán: 03 lần. Lần thanh toán cuối cùng sau khi Bên nhận thầu hoàn thành các công việc theo nghĩa vụ trong hợp đồng.",
               f"(ii) Giá trị Bên giao thầu thanh toán cho Bên nhận thầu theo các lần (số tiền thanh toán sau khi trừ tiền tạm ứng thu hồi): Lần 1 (Báo cáo kết quả khảo sát xây dựng được nghiệm thu, phê duyệt): giá trị công việc {vnd(a_ks)} đồng, thu hồi tạm ứng {vnd(th1)} đồng, thanh toán {vnd(n1)} đồng. Lần 2 (BCKTKT đủ điều kiện trình thẩm định, được nghiệm thu; 60% giá trị phần lập BCKTKT): giá trị công việc {vnd(d2)} đồng, thu hồi tạm ứng {vnd(th2)} đồng, thanh toán {vnd(n2)} đồng. Lần 3 (hồ sơ hoàn chỉnh sau thẩm định, dự án được phê duyệt, nghiệm thu hoàn thành; 40% giá trị phần lập BCKTKT): thanh toán {vnd(n3)} đồng. Chi tiết tại Phụ lục số 3.",
               ]
    else:
        q = chia_thanh_toan_qlda(gia, tu)
        d9 += ["b) Cách thức hoàn trả tiền tạm ứng: Tiền tạm ứng được thu hồi qua các lần thanh toán khối lượng hoàn thành: lần thanh toán thứ 1 thu hồi " + vnd(q["r1"]) + " đồng, lần thanh toán thứ 2 thu hồi " + vnd(q["r2"]) + " đồng; thu hồi hết trước khi giá trị thanh toán thực tế (kể cả tạm ứng) đạt 80% giá trị hợp đồng (khoản 5 Điều 9 Nghị định số 254/2025/NĐ-CP).",
               "c) Thời điểm tạm ứng lần đầu và thời hạn: Trong thời hạn 07 ngày làm việc kể từ ngày hợp đồng có hiệu lực, Bên giao thầu nhận đủ đề nghị tạm ứng hợp lệ của Bên nhận thầu và đã có kế hoạch vốn tương ứng, Bên giao thầu hoàn tất thủ tục tạm ứng với Kho bạc Nhà nước; số tiền tạm ứng từng lần nêu tại điểm a. Phần tạm ứng chưa thực hiện do chưa có kế hoạch vốn được thực hiện khi có kế hoạch vốn; Bên nhận thầu không có quyền yêu cầu lãi hoặc bồi thường do việc chưa tạm ứng vì chưa có vốn.",
               "d) Bảo lãnh tạm ứng: Bên nhận thầu không phải nộp bảo lãnh tạm ứng vì đây là hợp đồng thuê tư vấn quản lý dự án (mục (iii) điểm b khoản 2 Điều 9 Nghị định số 254/2025/NĐ-CP) và giá trị tạm ứng không vượt 01 tỷ đồng (điểm c khoản 3 Điều 12 Nghị định số 210/2026/NĐ-CP). Bên nhận thầu sử dụng tiền tạm ứng đúng mục đích, đúng đối tượng; nếu phát sinh rủi ro không thu hồi được vốn tạm ứng thì chủ đầu tư và tổ chức, cá nhân liên quan chịu trách nhiệm hoàn trả ngân sách nhà nước theo quy định.",
               "9.2.2. Thanh toán",
               "a) Tiến độ thanh toán",
               "(i) Số lần thanh toán: 03 lần, căn cứ khối lượng công việc hoàn thành được nghiệm thu của từng giai đoạn. Lần thanh toán cuối cùng sau khi Bên nhận thầu hoàn thành các công việc theo nghĩa vụ trong hợp đồng.",
               f"(ii) Giá trị Bên giao thầu thanh toán cho Bên nhận thầu theo các lần (số tiền thanh toán sau khi trừ tiền tạm ứng thu hồi): Lần 1 (khối lượng công việc giai đoạn chuẩn bị đầu tư hoàn thành, dự án được phê duyệt; {q['t1']}% giá hợp đồng): giá trị công việc {vnd(q['p1'])} đồng, thu hồi tạm ứng {vnd(q['r1'])} đồng, thanh toán {vnd(q['n1'])} đồng. Lần 2 (khối lượng công việc giai đoạn thực hiện đầu tư hoàn thành, công trình được nghiệm thu hoàn thành và bàn giao; {q['t2']}% giá hợp đồng): giá trị công việc {vnd(q['p2'])} đồng, thu hồi tạm ứng {vnd(q['r2'])} đồng, thanh toán {vnd(q['n2'])} đồng. Lần 3 (khối lượng công việc giai đoạn kết thúc hoàn thành, quyết toán dự án hoàn thành được phê duyệt; phần còn lại): thanh toán {vnd(q['p3'])} đồng. Chi tiết tại Phụ lục số 3.",
               ]
    d9 += ["(iii) Trong khoảng thời gian 07 ngày làm việc, không quá 14 ngày làm việc, kể từ ngày Bên giao thầu nhận đủ hồ sơ đề nghị thanh toán hợp lệ của Bên nhận thầu, Bên giao thầu phải thanh toán cho Bên nhận thầu (điểm l khoản 4 Điều 28 Nghị định số 210/2026/NĐ-CP). Mọi khoản thanh toán thực hiện trong phạm vi kế hoạch vốn do cấp có thẩm quyền giao hằng năm; Bên giao thầu chậm thanh toán thì trả lãi theo lãi suất quá hạn do ngân hàng thương mại nơi Bên nhận thầu mở tài khoản công bố.",
           "b) Hồ sơ thanh toán: Khi đến thời hạn của mỗi lần thanh toán hoặc tạm thanh toán, Bên nhận thầu nộp cho Bên giao thầu 01 bộ hồ sơ điện tử có chữ ký số gồm: biên bản nghiệm thu khối lượng hoàn thành của giai đoạn thanh toán; bảng tính giá trị công việc phát sinh (nếu có); giấy đề nghị thanh toán nêu giá trị hoàn thành, giá trị phát sinh, giảm trừ tiền tạm ứng, giá trị đề nghị thanh toán; hóa đơn hợp lệ (khoản 2 Điều 29 Nghị định số 210/2026/NĐ-CP). Bên giao thầu lập bảng xác định giá trị khối lượng công việc hoàn thành (Mẫu số 03.a/TT) và bảng tổng hợp thông tin hợp đồng gửi Kho bạc Nhà nước theo Nghị định số 254/2025/NĐ-CP.",
           "c) Hình thức thanh toán: Chuyển khoản vào tài khoản của Bên nhận thầu ghi tại Phần 1; đồng tiền thanh toán là đồng Việt Nam.",
           "Trường hợp chưa bảo đảm kế hoạch vốn cho các năm sau, Bên giao thầu thông báo bằng văn bản và hai bên thỏa thuận tạm dừng thanh toán theo Điều 18; Bên giao thầu thanh toán ngay khi có vốn."]
    L1.append((9, "Giá hợp đồng, tạm ứng, thanh toán", d9))
    # điều 10
    if ks:
        d10 = ["10.2.1. Nghiệm thu sản phẩm được tiến hành 03 lần: Lần 1: Báo cáo kết quả khảo sát xây dựng được phê duyệt. Lần 2: BCKTKT đủ điều kiện trình thẩm định. Lần cuối (lần 3): Sau khi nhận đầy đủ hồ sơ, tài liệu, sản phẩm thiết kế được phê duyệt và hồ sơ hoàn chỉnh sau thẩm định, phê duyệt dự án. Biên bản nghiệm thu khối lượng hoàn thành xác nhận Bên nhận thầu hoàn thành công việc đúng phạm vi hợp đồng (khoản 2 Điều 29 Nghị định số 210/2026/NĐ-CP). Bên giao thầu tổ chức nghiệm thu trong 07 ngày làm việc kể từ ngày nhận đủ hồ sơ nghiệm thu hợp lệ."]
    else:
        d10 = ["10.2.1. Nghiệm thu sản phẩm được tiến hành 03 lần theo giai đoạn: Lần 1: khối lượng công việc giai đoạn chuẩn bị đầu tư (kế hoạch quản lý dự án, kiểm tra báo cáo khảo sát và BCKTKT, hồ sơ trình thẩm định, phê duyệt dự án, lựa chọn nhà thầu). Lần 2: khối lượng công việc giai đoạn thực hiện đầu tư (quản lý các hợp đồng thi công, thiết bị, giám sát; nghiệm thu hoàn thành, bàn giao). Lần cuối (lần 3): Sau khi nhận đầy đủ hồ sơ, tài liệu, sản phẩm tư vấn được phê duyệt, gồm hồ sơ quản lý dự án và hồ sơ quyết toán dự án hoàn thành được cấp có thẩm quyền phê duyệt (hoặc khi hợp đồng chấm dứt theo Điều 18). Báo cáo công tác quản lý điều hành dự án hằng quý được Bên giao thầu xem xét, xác nhận trong từng giai đoạn. Bên giao thầu tổ chức nghiệm thu trong 07 ngày làm việc kể từ ngày nhận đủ hồ sơ nghiệm thu hợp lệ."]
    L1.append((10, "Nghiệm thu sản phẩm", d10))
    return sorted(L1, key=lambda x: x[0]) + dkct_chung(c)


# ============================================================ dựng văn bản
def _bp(v, text, size=14, bold=True, before=0, after=0, italic=False, underline=False):
    """Đoạn bìa: canh giữa, không thụt đầu dòng, giãn dòng đơn."""
    from copy import deepcopy
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Cm, Pt
    from vb_mau import _set_runs
    el = deepcopy(v.k_plain)
    para = _set_runs(el, [(text, bold, italic)])
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = para.paragraph_format
    pf.first_line_indent = Cm(0)
    pf.left_indent = Cm(0)
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.0
    pf.keep_with_next = True
    for r in para.runs:
        r.font.size = Pt(size)
        if underline:
            r.font.underline = True
    v._chen_para(el, para)
    return para


def trang_bia(v, c, so_hd):
    """Bìa trình bày như bìa Đề án (khung viền trang, tên lớn giữa trang), nội dung theo mẫu QĐ 1040/QĐ-BXD:
    Quốc hiệu · Tên hợp đồng · Số · Gói thầu (số, tên) · thuộc Dự án (tên, mã định danh) · giữa Bên giao thầu và Bên nhận thầu · Địa danh, ngày."""
    from copy import deepcopy
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    ten = {"KS": ["TƯ VẤN KHẢO SÁT XÂY DỰNG", "VÀ LẬP BÁO CÁO KINH TẾ - KỸ THUẬT"],
           "QLDA": ["TƯ VẤN QUẢN LÝ DỰ ÁN"]}[c["ma"]]
    # bỏ khối tiêu đề của mẫu biên bản (bảng cơ quan - quốc hiệu, tên loại, trích yếu): bìa hợp đồng dựng riêng
    for el in list(v.body.iterchildren()):
        if el is v.t_ky._tbl:
            break
        v.body.remove(el)
    _bp(v, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", 14, True)
    _bp(v, "Độc lập - Tự do - Hạnh phúc", 14, True, underline=True, after=80)
    _bp(v, "HỢP ĐỒNG", 36, True, before=30, after=8)
    for k, d in enumerate(ten):
        _bp(v, d, 16, True, after=(30 if k == len(ten) - 1 else 0))
    _bp(v, "Số: ……/2026/…… (ký hiệu hợp đồng)", 14, False, after=34)
    _bp(v, f"Gói thầu số …………: {c['ten_goi']}", 14, True, after=8)
    _bp(v, f"thuộc Dự án “{TEN_DA}”", 14, True, after=2)
    _bp(v, f"(mã định danh Dự án: {CH})", 14, False, after=44)
    _bp(v, "giữa", 14, False, after=16)
    _bp(v, BEN_A["ten"].upper(), 14, True, after=16)
    _bp(v, "và", 14, False, after=16)
    _bp(v, c["b"]["ten"].upper(), 14, True, after=90)
    _bp(v, "Quảng Ngãi, ngày       tháng       năm 2026", 14, True, before=0)
    # kết thúc phần bìa: ngắt section kèm khung viền trang như bìa Đề án
    cuoi = v.k_plain.__class__  # noqa
    sp = deepcopy(v.body.find(qn("w:sectPr")))
    for tag in ("w:headerReference", "w:footerReference", "w:titlePg", "w:pgNumType"):
        for e in sp.findall(qn(tag)):
            sp.remove(e)
    bd = OxmlElement("w:pgBorders")
    for canh, kc in (("top", "1"), ("left", "4"), ("bottom", "1"), ("right", "4")):
        e = OxmlElement("w:" + canh)
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "12")
        e.set(qn("w:space"), kc)
        e.set(qn("w:color"), "auto")
        bd.append(e)
    mar = sp.find(qn("w:pgMar"))
    mar.addnext(bd)
    v.giu_cuoi()
    ult = v._last
    # đoạn cuối bìa mang sectPr (ngắt section sang trang kế)
    ppr = ult.find(qn("w:pPr"))
    if ppr is None:
        ppr = OxmlElement("w:pPr")
        ult.insert(0, ppr)
    ppr.append(sp)
    kp = ppr.find(qn("w:keepNext"))
    if kp is not None:
        ppr.remove(kp)
    # section nội dung: trang đầu của phần này (mục lục) cũng hiện số trang; đánh số bắt đầu từ 1
    fin = v.body.find(qn("w:sectPr"))
    for e in fin.findall(qn("w:titlePg")):
        fin.remove(e)
    for e in fin.findall(qn("w:pgNumType")):
        fin.remove(e)
    pg = OxmlElement("w:pgNumType")
    pg.set(qn("w:start"), "1")
    fin.find(qn("w:pgMar")).addnext(pg)
    return "HỢP ĐỒNG " + " ".join(ten)


def muc_luc(v, dkc, dkct):
    v.tieu_de("MỤC LỤC")
    v.p("DANH MỤC CÁC TỪ VIẾT TẮT", bold=True)
    v.p("PHẦN 1. THÔNG TIN GIAO DỊCH", bold=True)
    v.p("PHẦN 2. CÁC CĂN CỨ GIAO KẾT HỢP ĐỒNG", bold=True)
    v.p("PHẦN 3. ĐIỀU KIỆN CHUNG CỦA HỢP ĐỒNG", bold=True)
    for n, ten, _ in dkc:
        v.p(f"Điều {n}. {ten}")
    v.p("PHẦN 4. ĐIỀU KIỆN CỤ THỂ CỦA HỢP ĐỒNG", bold=True)
    for n, ten, _ in dkct:
        v.p(f"Điều {n}. {ten}")
    v.p("PHỤ LỤC SỐ 1 đến PHỤ LỤC SỐ 5", bold=True)


def viet_tat(v):
    v.tieu_de("DANH MỤC CÁC TỪ VIẾT TẮT")
    v.bang(["Từ viết tắt", "Nghĩa"], [4.0, 13.0], [
        ("ĐKC", "Điều kiện chung"), ("ĐKCT", "Điều kiện cụ thể"), ("HSMT", "Hồ sơ mời thầu"), ("HSYC", "Hồ sơ yêu cầu"),
        ("HSDT", "Hồ sơ dự thầu"), ("HSĐX", "Hồ sơ đề xuất"), ("BCKTKT", "Báo cáo kinh tế - kỹ thuật đầu tư xây dựng"),
    ])


def phan_1_2(v, c):
    v.tieu_de("PHẦN 1. THÔNG TIN GIAO DỊCH")
    v.p("Hôm nay, ngày       tháng       năm 2026, tại Trụ sở chính Trường Cao đẳng Kon Tum, chúng tôi gồm các bên dưới đây:")
    for vai, a, kieu in (("1. Bên giao thầu:", BEN_A, "A"), ("Và bên kia là: 2. Bên nhận thầu:", c["b"], "B")):
        v.p(vai, bold=True, giu=True, sau=2)
        dong = [("Tên giao dịch", a["ten"]), ("Đại diện (hoặc người được ủy quyền) là", f"{a['dd']}  -  Chức vụ: {a['cv']}"),
                ("Địa chỉ", a["dc"]), ("Tài khoản", f"{a['tk']}, tại {a['nh']}")]
        if a.get("qhns"):
            dong.append(("Mã quan hệ ngân sách", a["qhns"]))
        dong.append(("Mã số thuế", a["mst"]))
        if a.get("gcn"):
            dong.append(("Đăng ký kinh doanh (nếu có)", a["gcn"]))
        dong.append(("Điện thoại", a["dt"] + (f";  Fax: {a['fax']}" if a.get("fax") else "") + (f";  E-mail: {a['mail']}" if a.get("mail") else "")))
        for k, t in dong:
            v.p(f"{k}: {t}", sau=1)
    v.p(f"Hai bên cùng thống nhất ký hợp đồng tư vấn {('khảo sát xây dựng và lập báo cáo kinh tế - kỹ thuật' if c['ma']=='KS' else 'quản lý dự án')} gói thầu “{c['ten_goi']}” thuộc Dự án “{TEN_DA}” như sau:")
    v.tieu_de("PHẦN 2. CÁC CĂN CỨ GIAO KẾT HỢP ĐỒNG")
    for t in L.can_cu_chung(c) + L.can_cu_ket_qua(c):
        v.p(t, italic=True, sau=3)


def dung(c, thu_muc, so_trang="………"):
    T = lay_mau(c["ma"])
    dkc = dkc_theo_goi(c, T)
    dkct = dkct_goi(c) + [dkct_20(c, so_trang)]
    v = VanBanMau()
    trang_bia(v, c, c["so_hd"])
    muc_luc_dau = v  # noqa
    # mục lục + từ viết tắt trên trang 2
    muc_luc(v, dkc, dkct)
    v.ngat_trang()
    viet_tat(v)
    v.ngat_trang()
    phan_1_2(v, c)
    v.tieu_de("PHẦN 3. ĐIỀU KIỆN CHUNG CỦA HỢP ĐỒNG")
    for n, ten, ds in dkc:
        v.dieu(f"Điều {n}. {ten}")
        for d in ds:
            v.p(d)
    v.tieu_de("PHẦN 4. ĐIỀU KIỆN CỤ THỂ CỦA HỢP ĐỒNG")
    for n, ten, ds in dkct:
        v.dieu(f"Điều {n}. {ten}")
        for d in ds:
            v.p(d)
    v.giu_cuoi()
    L.chu_ky_hd(v, c)
    phu_luc(v, c)
    out = os.path.join(thu_muc, c["file_hd"])
    v.luu(out, f"Hợp đồng tư vấn — {c['ten_goi']} — Dự án CLC 2026-2030")
    return out, dkc, dkct


def phu_luc(v, c):
    """Phụ lục số 1–5 (giữ nội dung đã thương thảo; sản phẩm giao bằng tệp điện tử có chữ ký số)."""
    ks = c["ma"] == "KS"
    g, gia, tu = c["g"], c["gia"], c["tu"]
    v.phu_luc_section()
    v.tieu_de("PHỤ LỤC SỐ 1")
    v.tieu_de("NỘI DUNG, KHỐI LƯỢNG CÔNG VIỆC VÀ SẢN PHẨM CỦA HỢP ĐỒNG")
    if ks:
        v.bang(["STT", "Công việc, sản phẩm", "Số lượng, quy cách", "Ghi chú"], [1.5, 7.2, 4.2, 4.1], [
            ("1", "Nhiệm vụ khảo sát (hỗ trợ lập), phương án kỹ thuật khảo sát", "01 bộ điện tử có chữ ký số", "Bên giao thầu phê duyệt"),
            ("2", "Báo cáo kết quả khảo sát xây dựng (đo vẽ hiện trạng, đánh giá kết cấu, điện, cấp - thoát nước, PCCC; địa hình, địa chất nếu có)", "01 bộ điện tử có chữ ký số (.pdf, .dwg)", "Điều 14 NĐ 217/2026"),
            ("3", "Thuyết minh BCKTKT", "01 bộ điện tử có chữ ký số (.pdf, .docx)", "Điều 30 NĐ 217/2026"),
            ("4", "Hồ sơ thiết kế bản vẽ thi công 03 ký túc xá và chỉ dẫn kỹ thuật", "01 bộ điện tử có chữ ký số (.pdf, .dwg)", "Điều 23 NĐ 217/2026"),
            ("5", "Danh mục, cấu hình kỹ thuật, chi phí 02 mô hình xe ô tô con số tự động", "01 bộ điện tử có chữ ký số", "Đưa vào dự toán, tổng mức đầu tư"),
            ("6", "Dự toán xây dựng, tổng mức đầu tư và bảng tính chi phí", "01 bộ điện tử có chữ ký số (.pdf, .xlsx)", "NĐ 206/2026"),
            ("7", "Hồ sơ phục vụ thủ tục kèm theo (quy hoạch, PCCC, môi trường, giấy phép nếu có)", "01 bộ điện tử", "Bên giao thầu thực hiện thủ tục"),
            ("8", "Báo cáo giải trình, hồ sơ chỉnh sửa theo kết quả thẩm định; bộ hồ sơ chính thức sau phê duyệt", "01 bộ điện tử có chữ ký số", "Không tính thêm chi phí"),
        ], can_giua=(0,))
    else:
        v.bang(["STT", "Công việc, sản phẩm", "Số lượng, quy cách", "Ghi chú"], [1.5, 7.2, 4.2, 4.1], [
            ("1", "Kế hoạch quản lý dự án", "01 bộ điện tử có chữ ký số", "Trong 15 ngày kể từ hiệu lực; Bên giao thầu phê duyệt"),
            ("2", "Ý kiến bằng văn bản về nhiệm vụ, phương án, báo cáo khảo sát và BCKTKT", "Theo từng lần", "Giai đoạn chuẩn bị đầu tư"),
            ("3", "Đề xuất phân gói thầu, dự thảo kế hoạch và hồ sơ lựa chọn nhà thầu các gói tiếp theo", "Theo từng gói", "Bên giao thầu phê duyệt"),
            ("4", "Báo cáo công tác quản lý điều hành dự án", "Hằng quý; tệp điện tử có chữ ký số", "Tiến độ, chất lượng, chi phí, vốn, an toàn"),
            ("5", "Số liệu phục vụ báo cáo giải ngân hằng tháng của Bên giao thầu", "Hằng tháng; tệp điện tử", "Gửi trước ngày 25 hằng tháng"),
            ("6", "Biên bản, nhật ký, ý kiến kiểm soát chất lượng, khối lượng, thanh toán các hợp đồng", "Theo từng lần", "Giai đoạn thực hiện"),
            ("7", "Hồ sơ hoàn thành, hồ sơ quyết toán dự án hoàn thành (phần tư vấn hỗ trợ)", "Theo mục lục", "Điều 6 ĐKC"),
            ("8", "Bàn giao toàn bộ hồ sơ quản lý dự án", "Theo mục lục bàn giao", "Khi kết thúc hợp đồng"),
        ], can_giua=(0,))
    v.tieu_de("PHỤ LỤC SỐ 2")
    v.tieu_de("TIẾN ĐỘ THỰC HIỆN HỢP ĐỒNG")
    if ks:
        v.p("T0 là ngày hợp đồng có hiệu lực. Các mốc tính theo ngày kể từ T0.")
        v.bang(["STT", "Mốc công việc", "Thời hạn hoàn thành"], [1.5, 10.8, 4.7], [
            ("1", "Bên giao thầu phê duyệt nhiệm vụ khảo sát; Bên nhận thầu nộp phương án kỹ thuật khảo sát", "T0 + 07 ngày"),
            ("2", "Hoàn thành khảo sát hiện trường", "T0 + 35 ngày"),
            ("3", "Nộp báo cáo kết quả khảo sát để nghiệm thu, phê duyệt", "T0 + 40 ngày"),
            ("4", "Hoàn thành thuyết minh, thiết kế bản vẽ thi công, dự toán, tổng mức đầu tư và hồ sơ thủ tục kèm theo", "T0 + 85 ngày"),
            ("5", "Nộp hồ sơ BCKTKT đủ điều kiện để Bên giao thầu trình thẩm định", "T0 + 90 ngày"),
            ("6", "Giải trình, chỉnh sửa, hoàn chỉnh hồ sơ sau thẩm định", "Trong 15 ngày kể từ ngày nhận yêu cầu"),
            ("7", "Thời gian thực hiện công việc của hợp đồng (khoản 8.1 ĐKCT)", "120 ngày kể từ T0"),
        ], can_giua=(0, 2))
    else:
        v.bang(["STT", "Giai đoạn, mốc", "Thời hạn"], [1.5, 10.8, 4.7], [
            ("1", "Lập kế hoạch quản lý dự án", "Trong 15 ngày kể từ ngày hợp đồng có hiệu lực"),
            ("2", "Giám sát hợp đồng khảo sát và lập BCKTKT; ý kiến về báo cáo khảo sát, BCKTKT", "Theo tiến độ hợp đồng khảo sát - lập BCKTKT (120 ngày)"),
            ("3", "Hỗ trợ trình thẩm định, phê duyệt dự án; phân gói thầu, kế hoạch lựa chọn nhà thầu", "Theo yêu cầu của Bên giao thầu"),
            ("4", "Quản lý thực hiện các hợp đồng thi công, thiết bị, giám sát", "Theo tiến độ của Dự án"),
            ("5", "Báo cáo công tác quản lý điều hành dự án", "Hằng quý, chậm nhất ngày 05 của tháng đầu quý sau"),
            ("6", "Hỗ trợ nghiệm thu hoàn thành, bàn giao, quyết toán dự án", "Theo quy định về quyết toán (nhóm C: 04 tháng lập, 02 tháng thẩm tra, 07 ngày phê duyệt)"),
            ("7", "Thời hạn hợp đồng (khoản 8.1 ĐKCT)", "Không quá 03 năm kể từ ngày hợp đồng có hiệu lực"),
        ], can_giua=(0,))
    v.tieu_de("PHỤ LỤC SỐ 3")
    v.tieu_de("GIÁ HỢP ĐỒNG VÀ TIẾN ĐỘ THANH TOÁN")
    if ks:
        a_ks, a_tk = c["a_ks"], c["a_tk"]
        d2 = (a_tk * 60 + 50) // 100
        d3 = a_tk - d2
        th1 = (a_ks + 1) // 2
        th2 = tu - th1
        n1, n2, n3 = a_ks - th1, d2 - th2, d3
        assert tu + n1 + n2 + n3 == gia and a_ks + d2 + d3 == gia
        v.p("Hợp đồng trọn gói, giá hợp đồng " + vnd(gia) + " đồng. Số tiền làm tròn đến đồng.")
        v.bang(["Lần", "Điều kiện thanh toán", "Giá trị công việc (đồng)", "Thu hồi tạm ứng (đồng)", "Số tiền thanh toán (đồng)"], [1.9, 5.7, 3.2, 3.0, 3.2], [
            ("Tạm ứng năm 2026", "Sau khi hợp đồng có hiệu lực; phần vốn năm 2026 chia theo tỷ lệ giá hợp đồng (điểm a khoản 9.2.1)", "—", "—", vnd(c["tu26"])),
            ("Tạm ứng năm 2027", "Phần tạm ứng còn lại để đủ 30% giá hợp đồng, theo kế hoạch vốn năm 2027 (điểm a khoản 9.2.1)", "—", "—", vnd(c["tu27"])),
            ("1", "Báo cáo kết quả khảo sát xây dựng được nghiệm thu, phê duyệt", vnd(a_ks), vnd(th1), vnd(n1)),
            ("2", "BCKTKT đủ điều kiện trình thẩm định, được nghiệm thu (60% giá trị phần lập BCKTKT)", vnd(d2), vnd(th2), vnd(n2)),
            ("3", "Hồ sơ hoàn chỉnh sau thẩm định, dự án được phê duyệt, nghiệm thu hoàn thành (40% giá trị phần lập BCKTKT)", vnd(d3), "0", vnd(n3)),
            ("Cộng", "", vnd(gia), vnd(tu), vnd(gia)),
        ], can_giua=(0,), dam_cuoi=True)
        v.p(f"Giá trị phần khảo sát xây dựng {vnd(a_ks)} đồng; giá trị phần lập BCKTKT {vnd(a_tk)} đồng. Tạm ứng được thu hồi ở lần thanh toán thứ 1 (một nửa giá trị lần thanh toán) và thu hồi hết ở lần thanh toán thứ 2, trước khi giá trị thanh toán cộng dồn đạt 80% giá hợp đồng.")
    else:
        q = chia_thanh_toan_qlda(gia, tu)
        v.p("Hợp đồng trọn gói, giá hợp đồng " + vnd(gia) + " đồng. Thanh toán 03 lần theo khối lượng công việc hoàn thành được nghiệm thu của từng giai đoạn; số tiền làm tròn đến đồng.")
        v.bang(["Lần", "Điều kiện thanh toán", "Giá trị (đồng)", "Thu hồi tạm ứng (đồng)", "Số tiền thanh toán (đồng)"], [1.9, 5.7, 3.2, 3.0, 3.2], [
            ("Tạm ứng năm 2026", "Sau khi hợp đồng có hiệu lực; phần vốn năm 2026 chia theo tỷ lệ giá hợp đồng (điểm a khoản 9.2.1)", "—", "—", vnd(c["tu26"])),
            ("Tạm ứng năm 2027", "Phần tạm ứng còn lại để đủ 30% giá hợp đồng, theo kế hoạch vốn năm 2027 (điểm a khoản 9.2.1)", "—", "—", vnd(c["tu27"])),
            ("1", f"Khối lượng công việc giai đoạn chuẩn bị đầu tư hoàn thành, dự án được phê duyệt ({q['t1']}% giá hợp đồng)", vnd(q["p1"]), vnd(q["r1"]), vnd(q["n1"])),
            ("2", f"Khối lượng công việc giai đoạn thực hiện đầu tư hoàn thành, công trình được nghiệm thu hoàn thành và bàn giao ({q['t2']}% giá hợp đồng)", vnd(q["p2"]), vnd(q["r2"]), vnd(q["n2"])),
            ("3", "Khối lượng công việc giai đoạn kết thúc hoàn thành, quyết toán dự án hoàn thành được phê duyệt (phần còn lại)", vnd(q["p3"]), "0", vnd(q["n3"])),
            ("Cộng", "", vnd(gia), vnd(tu), vnd(gia)),
        ], can_giua=(0,), dam_cuoi=True)
    v.tieu_de("PHỤ LỤC SỐ 4")
    v.tieu_de("NHÂN LỰC CỦA BÊN NHẬN THẦU")
    v.p("Nhân sự chủ chốt theo hồ sơ năng lực của Bên nhận thầu; thay đổi nhân sự thực hiện theo Điều 16.")
    hang = [(str(i), a, b_.rstrip(".")) for i, (a, b_) in enumerate(g["nhansu"], 1)]
    v.bang(["STT", "Vị trí, chức danh", "Nhân sự, chứng chỉ (hạng, thời hạn)"], [1.5, 5.5, 10.0], hang, can_giua=(0,))
    v.tieu_de("PHỤ LỤC SỐ 5")
    v.tieu_de("NHÂN SỰ CỦA BÊN GIAO THẦU")
    v.p("Bên giao thầu chỉ định bằng văn bản người đại diện và bố trí nhân sự phối hợp với Bên nhận thầu (khoản 12.2.2 Điều 12 ĐKC).")
    v.bang(["STT", "Vai trò", "Họ tên, chức vụ"], [1.5, 7.0, 8.5], [
        ("1", "Người đại diện ký hợp đồng", f"{BEN_A['dd']}, {BEN_A['cv']}"),
        ("2", "Đại diện quản lý thực hiện hợp đồng", f"{CH} (lãnh đạo phòng Tổng hợp - Hành chính và Quản trị)"),
        ("3", "Cán bộ phụ trách chuyên môn, hồ sơ", CH),
        ("4", "Cán bộ phụ trách thanh toán, vốn", CH),
    ], can_giua=(0,))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--goi", choices=["KS", "QLDA"])
    ap.add_argument("--so-trang", default="………")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for ma in ([a.goi] if a.goi else ["KS", "QLDA"]):
        c = L.cau_hinh(ma)
        c["file_hd"] = c["file_hd"].replace("_v2", "_v3")
        out, dkc, dkct = dung(c, a.out, a.so_trang)
        print(out)
        for n, d in con_trong(dkc):
            print("   [còn trống ĐKC]", n, d[:110])


if __name__ == "__main__":
    main()
