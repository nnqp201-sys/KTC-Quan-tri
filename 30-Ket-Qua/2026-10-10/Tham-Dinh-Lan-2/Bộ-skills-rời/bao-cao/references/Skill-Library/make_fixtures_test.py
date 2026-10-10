# -*- coding: utf-8 -*-
"""Sinh fixture Excel mô phỏng Phụ lục TB736 thật, gồm cả tình huống biên."""
from openpyxl import Workbook

OUT = "/home/claude/qa/"

# ---------- Phụ lục IIb (kết quả tháng, 16 cột, có KPI) ----------
def make_iib(path, truc_label_style="plain", put_sum_row=True, kpi_in_merged_header=True):
    wb = Workbook(); ws = wb.active; ws.title = "IIb"
    ws.append(["PHỤ LỤC IIb"])
    ws.append(["BÁO CÁO KẾT QUẢ CÔNG TÁC THÁNG 7 NĂM 2026"])
    # Hàng cha (merged) chứa chữ KPI — thực tế nằm TRÊN hàng có 'TT'
    if kpi_in_merged_header:
        ws.append([None, None, None, None, None, None, None, None, None, None,
                   "KPI số lượng", None, "KPI chất lượng", None, "KPI tiến độ", None])
    ws.append(["TT", "Nội dung công việc", "Người trực tiếp chỉ đạo", "Đơn vị chủ trì",
               "Sản phẩm/công việc", "Số lượng", "Độ khó", "Điểm chấm công việc",
               "Hệ số quy đổi", "Số lượng quy đổi",
               "Thực tế", "Quy đổi", "Thực tế", "Quy đổi", "Thực tế", "Quy đổi"])
    ws.append(["I", "NHIỆM VỤ THEO KẾ HOẠCH", None, None, None, None, None, None,
               None, None, None, None, None, None, None, None])

    if truc_label_style == "plain":
        truc1 = "Trục 1. Thực hiện mục tiêu phát triển kinh tế - xã hội"
        truc2 = "Trục 2. Hoàn thiện thể chế"
    else:  # có số thứ tự dẫn đầu
        truc1 = "1. Trục 1. Thực hiện mục tiêu phát triển kinh tế - xã hội"
        truc2 = "2. Trục 2. Hoàn thiện thể chế"

    ws.append([None, truc1] + [None] * 14)
    # 2 nhiệm vụ Trục 1
    ws.append([1, "Ban hành ngưỡng đầu vào ngành GDMN", "Hiệu trưởng", "Phòng QLĐT",
               "Quyết định", 1, "Cao", 200, 2.0, 2.0, 1, 2.0, 1, 2.0, 1, 2.0])
    ws.append([2, "Xây dựng chiến lược Khoa Sư phạm", "P. Hiệu trưởng", "Khoa Sư phạm",
               "Chiến lược", 1, "Cao", 150, 1.5, 1.5, 1, 1.5, 0.75, 1.125, 1, 1.5])
    if put_sum_row:
        ws.append([None, "Tổng cộng Trục 1", None, None, None, 2, None, None, None, 3.5,
                   2, 3.5, 1.75, 3.125, 2, 3.5])

    ws.append([None, truc2] + [None] * 14)
    ws.append([3, "Ban hành Quy chế bổ nhiệm", "Hiệu trưởng", "Phòng TC-HC",
               "Quy chế", 1, "Cao", 100, 1.0, 1.0, 1, 1.0, 1, 1.0, 1, 1.0])
    # Dòng SAI công thức hệ số (điểm 200 -> phải 2.0, nhưng ghi 1.0)
    ws.append([4, "Nhiệm vụ có hệ số sai", "Hiệu trưởng", "Phòng TC-KT",
               "Báo cáo", 1, "Cao", 200, 1.0, 1.0, 1, 1.0, 1, 1.0, 1, 1.0])
    if put_sum_row:
        ws.append([None, "Tổng cộng Trục 2", None, None, None, 2, None, None, None, 2.0,
                   2, 2.0, 2, 2.0, 2, 2.0])
    wb.save(path)


# ---------- Phụ lục Ib (kế hoạch tháng, 11 cột) ----------
def make_ib(path):
    wb = Workbook(); ws = wb.active; ws.title = "Ib"
    ws.append(["PHỤ LỤC Ib"])
    ws.append(["TT", "Nội dung công việc", "Người trực tiếp chỉ đạo", "Đơn vị chủ trì",
               "Sản phẩm/công việc", "Số lượng", "Độ khó", "Thời gian hoàn thành",
               "Điểm chấm công việc", "Hệ số quy đổi", "Ghi chú"])
    ws.append([None, "Trục 1. Thực hiện mục tiêu phát triển kinh tế - xã hội"] + [None] * 9)
    ws.append([1, "Tuyển sinh đợt 2", "Hiệu trưởng", "Phòng QLĐT", "Kế hoạch", 1, "Cao",
               "30/8/2026", 200, 2.0, "Đưa vào KH Trường"])
    ws.append([2, "Họp giao ban tuần", "Trưởng phòng", "Phòng TH-HC", "Biên bản", 4, "TB",
               "Hằng tuần", 100, 1.0, "Thường xuyên của đơn vị"])
    # Ghi chú hợp lệ theo SKILL.md nhưng script hiện coi là "lạ"
    ws.append([3, "Nhiệm vụ phát sinh theo kết luận", "Hiệu trưởng", "Phòng TH-HC",
               "Báo cáo", 1, "Cao", "15/8/2026", 150, 1.5, "Kết luận giao ban"])
    ws.append([4, "Nhiệm vụ bổ sung", "Hiệu trưởng", "Phòng TC-KT", "Tờ trình", 1, "Cao",
               "20/8/2026", 150, 1.5, "Bổ sung ngoài KH quý"])
    # Ghi chú có khoảng trắng thừa - phải vẫn lọc được
    ws.append([5, "Nhiệm vụ có ghi chú thừa dấu cách", "Hiệu trưởng", "Khoa KT-CN",
               "Đề án", 1, "Cao", "25/8/2026", 200, 2.0, " Đưa vào KH Trường "])
    wb.save(path)


if __name__ == "__main__":
    make_iib(OUT + "iib_chuan.xlsx", truc_label_style="plain", put_sum_row=True)
    make_iib(OUT + "iib_co_stt.xlsx", truc_label_style="numbered", put_sum_row=True)
    make_iib(OUT + "iib_khong_sum.xlsx", truc_label_style="plain", put_sum_row=False)
    make_iib(OUT + "iib_kpi_cung_hang.xlsx", truc_label_style="numbered",
             put_sum_row=False, kpi_in_merged_header=False)
    make_ib(OUT + "ib_chuan.xlsx")
    print("Đã tạo fixture xong.")
