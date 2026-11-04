# -*- coding: utf-8 -*-
"""Báo cáo rà soát hợp đồng QLDA (v3) — DỰNG THỦ CÔNG theo cấu trúc skill KTC-Ra-Soat-897 v4.5 khi cổng hồ sơ được miễn theo quyết định của người phụ trách.

Số liệu đo thể thức lấy từ tools/kiem_tra_the_thuc.py của skill (tt.json). Nhãn tự tính theo quy tắc 6 của SKILL.md.
Chạy: python -X utf8 lap_bao_cao_ra_soat_hd.py --out THƯ_MỤC
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vb_mau import VanBanMau  # noqa: E402

TEN = "KTC-Ra-Soat-897_HD-QLDA-Thanh-Vinh_29102026_BanNhap.docx"

PHAT_HIEN = [
    # (STT, vị trí, vấn đề, căn cứ, kiến nghị, mức)
    ("1", "Điều kiện cụ thể mục 9.2.2, 10.2.1 và Phụ lục số 3 (thanh toán theo khối lượng)",
     "Đã xử lý theo quyết định ngày 29/10/2026: thanh toán 03 lần theo khối lượng công việc hoàn thành của ba giai đoạn. Tỷ lệ 25% - 50% - 25% và tỷ lệ thu hồi tạm ứng 40% - 60% là đề xuất của người dựng, chưa có chỉ đạo; tạm ứng thu hồi hết khi giải ngân đạt 75% (nhỏ hơn 80%).",
     "Nghị định số 254/2025/NĐ-CP, khoản 5 và điểm d khoản 6 Điều 9",
     "Người có thẩm quyền chốt tỷ lệ từng giai đoạn.", "Mức 3"),
    ("2", "Điều kiện cụ thể mục 18.3 (thưởng, phạt)",
     "Đã bổ sung theo quyết định ngày 29/10/2026: thưởng, phạt ở mức tối thiểu theo quy định của Nhà nước. Pháp luật chỉ quy định mức phạt tối đa (12%), không có mức tối thiểu; cụm \"mức tối thiểu\" chưa được định lượng nên khó thi hành.",
     "Luật Xây dựng, khoản 1 và khoản 3 Điều 86",
     "Ghi một con số cụ thể (hoặc \"không phạt\") thay cho \"mức tối thiểu\".", "Mức 3"),
    ("3", "Bìa, Phần 1, Phụ lục số 5",
     "Còn chỗ trống chưa điền: số hợp đồng và ký hiệu, số gói thầu, mã định danh Dự án, ngày ký, điện thoại và e-mail của Bên nhận thầu, nhân sự Bên giao thầu.",
     "Mẫu hợp đồng QĐ 1040/QĐ-BXD, Phần 1 và bìa mẫu", "Điền đủ trước khi ký.", "Mức 2"),
    ("4", "Điều kiện cụ thể mục 18.2.1",
     "Ngưỡng 28 ngày liên tục không thực hiện công việc để Bên giao thầu chấm dứt hợp đồng ngắn hơn mức 56 ngày của Nghị định 210; chặt hơn đối với Bên nhận thầu.",
     "Nghị định số 210/2026/NĐ-CP, điểm b khoản 2 Điều 27 (56 ngày liên tục, trừ khi các bên có thỏa thuận khác)",
     "Xác nhận chủ ý thỏa thuận 28 ngày hoặc đưa về 56 ngày.", "Mức 3"),
    ("5", "Phần 2 (căn cứ) và Phần 1",
     "Ngày thương thảo, đối chiếu ghi 22/10/2026 (lấy từ Hệ thống mạng đấu thầu quốc gia) trước ngày Quyết định số 2375/QĐ-CĐKT (27/10/2026). Giấy chứng nhận đăng ký doanh nghiệp của Bên nhận thầu ghi thay đổi lần 3 ngày 17/9/2025, bản nháp trước ghi 13/9/2025. Địa chỉ ghi \"Đăk Cấm\" (Bên giao thầu) và \"Đắk Cấm\" (Bên nhận thầu).",
     "Hồ sơ dự án (đơn xin nhận thầu, Quyết định số 2375/QĐ-CĐKT)", "Đối chiếu bản gốc và thống nhất cách ghi.", "Mức 3"),
    ("6", "Điều kiện chung (8 chỗ dùng từ \"đảm bảo\")",
     "Nguyên văn mẫu BXD dùng \"đảm bảo\"; quy tắc dùng từ của Trường là \"bảo đảm\".",
     "Mẫu prompt chính thức mục 4 (TD-04); Hướng dẫn kèm QĐ 1040 mục 4.1.c (Điều kiện chung là phần \"cứng\")",
     "Giữ nguyên văn mẫu BXD ở Điều kiện chung; chỉ sửa trong phần do Trường soạn (đã sửa).", "Mức 3"),
    ("7", "Phụ lục số 1–5 (TT-32, 34, 39, 40, 43, 44)",
     "Script đo theo quy tắc phụ lục của văn bản hành chính Trường: chưa có đường kẻ và dòng \"CỦA TRƯỜNG CAO ĐẲNG KON TUM\", \"Phụ lục\" ghi hoa và số thường, năm phụ lục chung một section; bìa tách section nên phát sinh báo số trang. Hợp đồng dựng theo mẫu BXD (ĐKC dẫn \"Phụ lục số …\").",
     "Chỉ đạo của Hiệu trưởng ngày 26/10/2026 (bảng thông số KTC); Hướng dẫn kèm QĐ 1040",
     "Đề nghị người có thẩm quyền xác nhận giữ theo mẫu BXD cho hợp đồng. Chưa kết luận Đạt.", "Mức 2"),
]

DAT = [
    ("Khổ giấy, lề, header/footer (3 section)", "A4; lề 2/2/3/2 cm; header, footer 1,27 cm"),
    ("Phông, cỡ chữ lời văn", "Times New Roman; 435/435 đoạn cỡ 14"),
    ("Canh đều, khoảng cách đoạn, giãn dòng, thụt đầu dòng", "265/265 đoạn nhiều dòng canh đều; 435/435 đoạn thỏa Before, After ≥ 6 pt, giãn dòng, thụt 1,27 cm"),
    ("Canh giữa ô bảng, viết hoa \"phòng\"", "Đã sửa sau lần đo đầu (TT-51 và TD-02 hết báo)"),
    ("Số trang phụ lục", "Bắt đầu từ 1, hiển thị trang đầu"),
    ("Viện dẫn điều khoản Nghị định 210, 254, 217, 206", "Đối chiếu toàn văn: khớp (Điều 12.3.c, g, h; 13.2.c; 26.2.a; 27.2; 28.4.l; 30.3; 31.3.b; Điều 9 NĐ 254; Điều 25.5 NĐ 206; Điều 46 NĐ 217)"),
]

CHUA_KIEM = [
    "Ma trận đối chiếu chéo với Quyết định số 1976, 2073/QĐ-CĐKT và các văn bản nội bộ về thẩm quyền ký hợp đồng chưa thực hiện.",
    "Lời văn trong bảng (90 đoạn) không đo TT-20 đến TT-24 theo quyết định D2 ngày 27/10/2026.",
    "Số trang của phụ lục: không dựng được bản PDF bằng LibreOffice để đếm.",
    "Mã phát hiện theo bảng 02 chưa gán cho các mục nội dung (dựng thủ công); mức do người rà soát đề xuất.",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    v = VanBanMau()
    v.dau("Số:        /BC-RS897", "Quảng Ngãi, ngày 29 tháng 10 năm 2026", "BÁO CÁO RÀ SOÁT HỢP ĐỒNG",
          "Hợp đồng tư vấn quản lý dự án giữa Trường Cao đẳng Kon Tum và Công ty cổ phần Thành Vinh\n(bản nháp rà soát, dựng thủ công, cổng hồ sơ được miễn)")
    v.p("BẢN NHÁP RÀ SOÁT – CHƯA ĐƯỢC PHÊ DUYỆT CHÍNH THỨC", bold=True, center=True)
    v.tieu_de("KẾT LUẬN ĐIỀU HÀNH")
    v.p("Nhãn (tự tính theo quy tắc 6 SKILL.md, không do script gán): Cần chỉnh sửa trước khi trình ký. Lý do: còn 02 phát hiện Mức 2 (chỗ trống chưa điền, định dạng phụ lục chờ xác nhận) và 05 phát hiện Mức 3. Không có phát hiện Mức 1.")
    v.p("Rà soát lần 1, chế độ độc lập. Chưa thực hiện ma trận đối chiếu chéo với văn bản nội bộ về thẩm quyền (xem Phần I.8).")
    v.tieu_de("PHẦN I. THÔNG TIN CHUNG")
    v.p("I.1. Văn bản rà soát: HD_Goi-QLDA_Thanh-Vinh_20261028_v3.docx (46 trang; dựng theo mẫu Phụ lục III kèm QĐ 1040/QĐ-BXD).")
    v.p("I.2. Phiên bản skill: KTC-Ra-Soat-897 v4.5 (lõi nguyên bản, TB 1206/TB-CĐKT) và lớp bổ sung cá nhân ngày 29/10/2026. Script đo thể thức kiem_tra_the_thuc.py (mã băm tệp đo: e1fbe5aa4280f397…).")
    v.p("I.3. Cổng hồ sơ: CHẶN theo script (còn 8 mục: hai tệp PDF scan, Quyết định số 2375 chưa có bản có số, Luật Lao động chưa nhận diện, hai cụm từ \"Luật áp dụng\" và \"Luật được áp dụng\" là dương tính giả từ nguyên văn mẫu BXD). Người phụ trách (anh Phục, P-THHC) đã quyết định miễn cổng ngày 29/10/2026. Báo cáo này vì vậy dựng thủ công, không đạt đủ quy trình chuẩn.")
    v.p("I.4. Tài liệu đã đối chiếu: 19 tệp pháp luật và quyết định trong hồ sơ tạm (Luật Xây dựng, Luật Đấu thầu, Bộ luật Dân sự, Nghị định 210, 207, 217, 206, 212, 214/2025, 254, VBHN 36, 74, 18; Thông tư 79; Quyết định số 2158, 2161, 2236). Chưa có toàn văn Quyết định 805/QĐ-UBND, Quyết định 2375/QĐ-CĐKT bản có số, đơn xin nhận thầu.")
    v.tieu_de("PHẦN II. PHÁT HIỆN")
    v.bang(["STT", "Vị trí", "Mô tả vấn đề", "Căn cứ", "Kiến nghị", "Mức"], [0.9, 2.6, 5.4, 3.6, 3.4, 1.3],
           PHAT_HIEN, can_giua=(0, 5), size=11)
    v.tieu_de("PHẦN III. CÁC MỤC ĐẠT")
    v.bang(["Hạng mục", "Số đo, bằng chứng"], [6.0, 11.0], DAT, size=11)
    v.tieu_de("PHẦN V. MỨC TUÂN THỦ VÀ NHÃN")
    v.p("Mức 1: 0; Mức 2: 2 (phát hiện 3, 7); Mức 3: 5 (phát hiện 1, 2, 4, 5, 6). Nhãn: Cần chỉnh sửa trước khi trình ký.")
    v.tieu_de("PHẦN VI. VẤN ĐỀ ƯU TIÊN")
    for t in ["Chốt tỷ lệ thanh toán theo giai đoạn của Hợp đồng QLDA (đang đề xuất 25% - 50% - 25%) trước khi làm việc với Kho bạc.",
              "Định lượng \"mức tối thiểu\" của thưởng, phạt (Luật Xây dựng Điều 86).",
              "Điền đủ chỗ trống của bìa, Phần 1 và Phụ lục số 5; xác nhận giữ định dạng phụ lục theo mẫu BXD.",
              "Cho phép dùng bản có số của Quyết định số 2375/QĐ-CĐKT để hoàn tất ma trận đối chiếu."]:
        v.p("- " + t)
    v.tieu_de("KIỂM TRA CHẤT LƯỢNG CUỐI CÙNG")
    v.p("Chưa chạy được: phản biện độc lập theo Bước 6 ở mức đầy đủ (chỉ tự soát lại các điều khoản viện dẫn). Phần I.8 – nội dung chưa kiểm:")
    for t in CHUA_KIEM:
        v.p("- " + t)
    v.p("[Bổ sung – tham khảo] Phiên bản: v4.5 — lõi khớp mã băm gói TB 1206; có lớp bổ sung cá nhân (ghi chú tham khảo).", italic=True)
    v.p("[Bổ sung – tham khảo] Bảo mật tài liệu: hợp đồng, hồ sơ nhà thầu chỉ dùng trong tài khoản Team của Trường.", italic=True)
    v.p("[Bổ sung – tham khảo] Quy ước riêng CĐKT: văn bản ký số, không đề cập bản giấy; phòng, khoa viết thường trong lời văn.", italic=True)
    v.giu_cuoi()
    v.ky("NGƯỜI KIỂM TRA", "", "(chưa ký)", "TRẠNG THÁI PHÊ DUYỆT", "", "(chờ người có thẩm quyền)", None)
    os.makedirs(a.out, exist_ok=True)
    out = os.path.join(a.out, TEN)
    v.luu(out, "Báo cáo rà soát hợp đồng QLDA — bản nháp (dựng thủ công)")
    print(out)


if __name__ == "__main__":
    main()
