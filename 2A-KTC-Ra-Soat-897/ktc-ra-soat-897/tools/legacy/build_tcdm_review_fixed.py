"""
build_tcdm_review_20260810.py — v2.1 (13/8/2026)
Tạo file .docx Báo cáo Rà soát chính thức KTC-897
Sử dụng: python build_tcdm_review_fixed.py [--out /đường/dẫn/output.docx]
Mặc định: lưu thẳng vào ./12-Output/Bao_cao_ra_soat_<ho-so>_<ngày>.docx
Thay đổi v2.1: bỏ thư mục con ngày/tên trong 12-Output — file ra thẳng thư mục gốc
"""
import sys
import argparse
from datetime import datetime
from pathlib import Path
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# ── Cấu hình mặc định ─────────────────────────────────────────────────────────
DEFAULT_OUT_DIR = Path("12-Output")   # tương đối với thư mục chạy script

def resolve_output(arg_out, ho_so_name="ra-soat-chinh-thuc"):
    """Xác định đường dẫn file đầu ra — thẳng vào 12-Output/, không tạo thư mục con."""
    if arg_out:
        p = Path(arg_out)
    else:
        date_str = datetime.now().strftime("%Y%m%d")
        p = DEFAULT_OUT_DIR / f"Bao_cao_ra_soat_{ho_so_name}_{date_str}.docx"
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

# ── Hàm tiện ích định dạng ────────────────────────────────────────────────────
def font(run, size=14, bold=False, italic=False, color=None):
    run.font.name = "Times New Roman"
    pr = run._element.get_or_add_rPr()
    pr.rFonts.set(qn("w:ascii"), "Times New Roman")
    pr.rFonts.set(qn("w:hAnsi"), "Times New Roman")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)

def shade(cell, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell(c, value, bold=False, size=8, center=False):
    c.text = ""
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    font(p.add_run(str(value)), size, bold)
    c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP

def add_title(doc, text, size=14):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(3)
    font(p.add_run(text), size, True)

def add_heading(doc, text, minor=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7 if not minor else 4)
    p.paragraph_format.space_after = Pt(3)
    font(p.add_run(text), 14, True)

def add_para(doc, text, indent=True):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if indent:
        p.paragraph_format.first_line_indent = Cm(1)
    font(p.add_run(text), 14)

def add_bullet(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(.7)
    p.paragraph_format.first_line_indent = Cm(-.4)
    p.paragraph_format.space_after = Pt(2)
    font(p.add_run("- "), 14)
    font(p.add_run(text), 14)

def add_table(doc, headers, rows, size=8):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        set_cell(t.rows[0].cells[i], h, True, size, True)
        shade(t.rows[0].cells[i], "D9EAF7")
    for row in rows:
        cs = t.add_row().cells
        for i, value in enumerate(row):
            set_cell(cs[i], value, False, size)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

# ── Dữ liệu vấn đề rà soát ────────────────────────────────────────────────────
ISSUES = [
    ("1","Nội dung/hiệu lực","PL III, Mục B",
     "Vẫn giữ toàn bộ thiết bị chuyên dùng đã được cơ quan có thẩm quyền ban hành trước đây, dù QĐ 44/2025/QĐ-UBND đã cho hết hiệu lực các QĐ cũ của tỉnh Kon Tum.",
     "Khoản 2 Điều 5 QĐ 44/2025/QĐ-UBND; BB 151 mục IV.2.đ.",
     "Loại Mục B; thẩm định và ban hành thiết bị chuyên dùng bằng hồ sơ riêng.",
     "Mức 1"),
    ("2","Số lượng","PL II: scan, hủy, photocopy",
     "Dự thảo làm tròn tại từng đơn vị nên mỗi loại có 20 chiếc. Với 224 người ghi trong PL II, mức tối đa toàn Trường là ceil(224/15)=15; vượt 5 chiếc mỗi loại.",
     "Ghi chú Mục B Phụ lục QĐ 10/2026/QĐ-TTg.",
     "Tính một lần trên tổng số người đủ điều kiện toàn Trường, rồi phân bổ.",
     "Mức 1"),
    ("3","Số lượng","PL II: máy in",
     "Dự thảo tính 78 máy bằng tổng người/3. Định mức máy in chỉ áp dụng nhóm VIII. Theo PL I có 188 người không giữ chức vụ, tối đa 63 máy; dự thảo vượt ít nhất 15 máy.",
     "Ghi chú Mục B Phụ lục QĐ 10/2026/QĐ-TTg.",
     "Chốt danh sách nhóm VIII, tính tổng toàn Trường và loại lãnh đạo đã có máy in theo chức danh.",
     "Mức 1"),
    ("4","Mức giá","PL I: bàn ghế tại 11 đơn vị",
     "Mức 11,5 triệu đồng/bộ áp dụng chung cả lãnh đạo và người không giữ chức vụ. Trần nhóm VIII là 7 triệu đồng; mức dự thảo tăng 64,3%, vượt giới hạn 30% được phân cấp.",
     "Mục A Phụ lục QĐ 10/2026; khoản 1 Điều 3 QĐ 44/2025.",
     "Tách giá theo nhóm; nhóm VIII tối đa 9,1 triệu đồng nếu dùng biên độ 30%.",
     "Mức 1"),
    ("5","Dữ liệu","PL I–II/QĐ 1370",
     "PL ghi 224 người tại đơn vị; QĐ 1370 giao 226 biên chế toàn Trường, gồm 4 lãnh đạo, tức 222 tại đơn vị, cộng 1 HĐ CMNV trong chỉ tiêu = 223. Lệch rõ tại TH-HC&QT, Khoa SP, Y–Dược.",
     "Điểm b khoản 2 Điều 5 QĐ 15/2025; QĐ 1370/QĐ-CĐKT.",
     "Lập phụ biểu từng người đủ điều kiện; chốt mẫu số trước khi tính thiết bị.",
     "Mức 1"),
    ("6","Phạm vi","QĐ Điều 1.3; PL III",
     "Tên QĐ bao quát chức danh và hoạt động chung nhưng khoản 3/PL III vẫn đưa thiết bị chuyên dùng; trái hướng Hội đồng yêu cầu tách riêng.",
     "BB 151 mục IV.2.đ; Điều 6 QĐ 15/2025.",
     "Bỏ thiết bị chuyên dùng khỏi QĐ này; lập quyết định riêng.",
     "Mức 1"),
    ("7","Trùng định mức","PL IV so với PL I–II",
     "PL IV ghi số lượng '1' nhưng không xác định 1/người, 1/phòng hay 1/đơn vị; chưa có nguyên tắc cấm trang bị trùng thiết bị tương ứng tại PL I–II.",
     "Khoản 8 Điều 3 QĐ 15 được bổ sung bởi QĐ 10/2026.",
     "Xác định đối tượng/đơn vị tính; bổ sung nguyên tắc loại trừ trang bị trùng.",
     "Mức 1"),
    ("8","BMNN","PL V",
     "Số lượng '1' không rõ phạm vi. Giá máy tính 20–45 triệu, két 60 triệu không kèm yêu cầu kỹ thuật/khảo sát giá.",
     "Điều 5a QĐ 15 được bổ sung bởi QĐ 10/2026.",
     "Chỉ định chức danh/đơn vị xử lý BMNN; dùng một mức tối đa xác định và lưu hồ sơ khảo sát giá.",
     "Mức 1"),
    ("9","Căn cứ","QĐ: NĐ 286/2025",
     "Ghi NĐ 286/2025/NĐ-CP 'của Thủ tướng Chính phủ'; Nghị định do Chính phủ ban hành.",
     "Văn bản gốc NĐ 286/2025/NĐ-CP.",
     "Sửa thành 'của Chính phủ'.",
     "Mức 2"),
    ("10","Căn cứ","PL VI mục 6.a–b",
     "Dẫn Mục A/B Phụ lục II QĐ 15, trong khi QĐ 10 đã thay hoàn toàn hai phụ lục cũ bằng một Phụ lục mới.",
     "Khoản 4 Điều 2 QĐ 10/2026/QĐ-TTg.",
     "Dẫn Mục A/B Phụ lục QĐ 15 được thay thế tại QĐ 10.",
     "Mức 2"),
    ("11","Quy trình","PL VI mục 2",
     "Ghi 'trình tự, thủ tục rút gọn' nhưng không có căn cứ, thẩm quyền và giới hạn.",
     "Yêu cầu rõ ràng của văn bản quản lý nội bộ.",
     "Bỏ hoặc quy định rõ chỉ rút gọn cập nhật phụ lục, không rút gọn thủ tục mua sắm.",
     "Mức 2"),
    ("12","Tiếp thu","TTGT mục 5",
     "TTGT ghi 'đã rà soát, điều chỉnh', nhưng PL III vẫn còn vật tư tiêu hao, chuyên dùng, văn bản hết hiệu lực và lỗi dữ liệu.",
     "BB 151 mục IV.2.đ; PL III sau họp.",
     "Dùng bảng: ý kiến – tiếp thu/bảo lưu – vị trí sửa – nội dung sau sửa – chứng cứ.",
     "Mức 2"),
    ("13","Thể thức/quy trình","TTGT; căn cứ QĐ",
     "Báo cáo cấp phòng không có số không mặc nhiên là vi phạm. Tuy nhiên phải nhận diện duy nhất tài liệu.",
     "NĐ 30/2020/NĐ-CP; bối cảnh hồ sơ.",
     "Không bắt buộc cấp số; ghi đủ ngày, tên, đơn vị lập.",
     "Mức 2"),
    ("14","Thẩm quyền","Câu kết TTGT",
     "'Kính trình Hội đồng xem xét, phê duyệt' không khớp TB 847: Hội đồng đã thông qua có điều kiện; Phòng phải trình Hiệu trưởng xem xét, quyết định.",
     "Mục 2 TB 847/TB-CĐKT.",
     "Sửa luồng trình: báo cáo Hội đồng để theo dõi, trình Hiệu trưởng xem xét quyết định.",
     "Mức 2"),
    ("15","Soạn thảo","PL I–IV",
     "Còn 'Mức gia', '1..300', trùng bàn hội trường 60 chiếc, 'Phụ lục II và Phụ lục II', đơn vị tính không thống nhất và nhiều tên thiết bị sai.",
     "BB 151; yêu cầu trình bày NĐ 30.",
     "Sửa chính tả/dẫn chiếu; chuẩn hóa tên và đơn vị tính; khử dòng trùng.",
     "Mức 2"),
    ("16","Phân loại","PL III Mục A",
     "Còn nhiều vật tư/tiêu hao/linh kiện: dây, nẹp, ống, vật tư phụ, rèm, khăn, ga chăn gối, hóa chất, thuốc thử, chip RFID...",
     "BB 151 mục IV.2.đ.",
     "Tách tài sản/công cụ/vật tư; cấu phần hệ thống chỉ ghi trong thuyết minh cấu hình.",
     "Mức 2"),
]

# ── Hàm tạo báo cáo ────────────────────────────────────────────────────────────
def build_report(out_path, ho_so_name="TCDMTB", ngay_ra_soat=None):
    if ngay_ra_soat is None:
        ngay_ra_soat = datetime.now().strftime("%-d/%-m/%Y")

    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Cm(2)
    sec.bottom_margin = Cm(2)
    sec.left_margin = Cm(2)
    sec.right_margin = Cm(2)

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal._element.rPr.rFonts.set(qn("w:ascii"), "Times New Roman")
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Times New Roman")
    normal.font.size = Pt(14)

    add_title(doc, "TRUONG CAO DANG KON TUM", 13)
    add_title(doc, "BAO CAO RA SOAT CHINH THUC TRUOC KHI TRINH KY", 15)
    add_title(doc, "Bo ho so tieu chuan, dinh muc su dung may moc, thiet bi", 14)
    add_title(doc, "(Doi chieu du thao goc, Bien ban 151, san pham sau hop va 02 vong GROK)", 12)
    add_para(doc,
        f"Ngay ra soat: {ngay_ra_soat}. "
        "Don vi soan thao: Phong Tong hop - Hanh chinh va Quan tri. "
        "Tham quyen du kien: Hieu truong Truong Cao dang Kon Tum.")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    font(p.add_run("KET LUAN DIEU HANH: CHUA SAN SANG TRINH KY"),
         14, True, color=(192, 0, 0))
    add_para(doc,
        "Ho so con 08 van de Muc 1 lien quan gioi han so luong, muc gia, "
        "hieu luc can cu, pham vi chuyen dung va nguy co trang bi trung. "
        "Phai tinh lai so lieu va tham dinh lai truoc khi trinh Hieu truong.")

    add_heading(doc, "PHAN I. THONG TIN CHUNG")
    add_para(doc, "1. He quy chieu: Quyet dinh ca biet va ho so hanh chinh noi bo cua don vi su nghiep cong lap; ap dung Nghi dinh 30/2020/ND-CP va phap luat quan ly, su dung tai san cong.")
    add_para(doc, "2. Pham vi: du thao goc; BB 151/BB-CDKT; TB 847/TB-CDKT; Bao cao TTGT ngay 10/8/2026; QD va PL I-VI sau hop; hai bao cao GROK; tham dinh sau so luong, gia va bac chuc danh.")
    add_para(doc, "3. So QD de trong o ban du thao la phu hop. Bao cao TTGT cap phong khong bi coi la sai chi vi chua co so.")
    add_para(doc, "4. Nguon du lieu 01-04 da doi chieu:")
    for s in [
        "01-Legal-Database: QD 15/2025/QD-TTg, QD 10/2026/QD-TTg, QD 44/2025/QD-UBND, QD 585-QD/TU.",
        "02-KTC-Regulations: QD 988/QD-CDKT va QD 1370/QD-CDKT.",
        "03-Templates: Mau Quyet dinh ban hanh quy che, quy dinh; cau truc bao cao ra soat chuan.",
        "04-Good-Documents: van ban quyet dinh tot cua Truong, dung doi chieu bo cuc va van phong.",
        "Hai bao cao GROK chi dung kiem tra diem da neu/bo sot, khong dung lam can cu phap ly.",
    ]:
        add_bullet(doc, s)
    add_para(doc, "5. Bac chuc danh: Hieu truong Bac 6 va Pho Hieu truong Bac 7 tai PL I phu hop QD 585-QD/TU. QD 10/2026 da thay the hoan toan Phu luc I-II cu cua QD 15.")

    add_heading(doc, "PHAN II. KET QUA RA SOAT CHI TIET")
    add_table(doc,
        ["STT", "Nhom", "Vi tri", "Van de", "Can cu", "Kien nghi", "Muc"],
        ISSUES, 7)

    add_heading(doc, "PHAN III. NOI DUNG DAT / KHONG PHAT HIEN VAN DE")
    for s in [
        "Ten QD sau hop da bo sung pham vi phuc vu cong tac cac chuc danh va hoat dong chung.",
        "Da bo QD 287 va TB 527; da bo sung dung chu the Ban Thuong vu Tinh uy doi voi QD 585.",
        "Giu 'may tinh bang' khong trai QD 10/2026; dieu bat buoc la chong trang bi trung.",
        "Gia Hieu truong Bac 6 va Pho Hieu truong Bac 7 nam trong bien do toi da 30% theo QD 44.",
        "PL VI da co nguyen tac kiem nhiem, dieu chuyen, xu ly nguoi tien nhiem va thay the.",
    ]:
        add_bullet(doc, s)

    add_heading(doc, "PHAN IV. BANG KIEM CHUNG CHUYEN MON")
    add_heading(doc, "1. So luong thiet bi phong lam viec", True)
    add_table(doc,
        ["Thiet bi", "Cong thuc", "Mau so", "Toi da", "Du thao", "Vuot"],
        [
            ("May in", "1/3 nguoi Nhom VIII", "188", "63", "78", "15"),
            ("May scan", "1/15 toan bo", "224", "15", "20", "5"),
            ("May huy", "1/15 toan bo", "224", "15", "20", "5"),
            ("May photocopy", "1/15 toan bo", "224", "15", "20", "5"),
            ("Gia tai lieu", "1/10 toan bo", "224", "23", "27", "4"),
        ], 9)

    add_heading(doc, "2. Muc gia chuc danh", True)
    add_table(doc,
        ["Doi tuong", "Thiet bi", "Tran QD10", "Du thao", "Ty le", "Ket luan"],
        [
            ("Hieu truong - Bac 6", "Ban ghe", "13,0", "15,0", "+15,4%", "Trong bien do QD 44"),
            ("Hieu truong - Bac 6", "Laptop/tablet", "25,0", "28,8", "+15,2%", "Trong bien do QD 44"),
            ("Lanh dao don vi - Bac 7 tro di", "Ban ghe", "10,0", "11,5", "+15,0%", "Phu hop"),
            ("Nhom VIII", "Ban ghe", "7,0", "11,5", "+64,3%", "Vuot 30%"),
            ("Nhom VIII", "May tinh", "20,0", "23,0", "+15,0%", "Phu hop neu khong trung PL IV"),
            ("Nhom VIII", "Dien thoai", "1,0", "1,2", "+20,0%", "Trong bien do QD 44"),
        ], 9)

    add_heading(doc, "PHAN V. DANH GIA TONG THE")
    add_para(doc, "1. Muc do tuan thu phap luat: CHUA DAT. Con van de Muc 1 anh huong truc tiep gioi han so luong, gia, hieu luc can cu va pham vi danh muc.")
    add_para(doc, "2. Muc do san sang phat hanh: CHUA SAN SANG. Khong the chi sua chinh ta; phai tinh lai PL I-II, tach chuyen dung khoi PL III, viet lai PL IV-V va cap nhat TTGT.")
    add_para(doc, "3. Diem chat luong: The thuc 15/20; can cu 10/20; noi dung & logic 8/20; tham quyen & quy trinh 10/20; ngon ngu & thong nhat 12/20. Tong 55/100 - Chua dat.")

    add_heading(doc, "PHAN VI. KET LUAN VA THU TU XU LY")
    for s in [
        "Khoa so lieu nhan su theo QD 1370 va danh sach hop dong du dieu kien.",
        "Tinh lai PL II tren tong toan Truong; may in chi tinh Nhom VIII.",
        "Tach gia ban ghe Nhom VIII; khong vuot 9,1 trieu dong neu dung bien do 30%.",
        "Loai thiet bi chuyen dung va can cu cu khoi PL III; lap ho so rieng.",
        "Viet lai PL IV-V theo doi tuong, so luong, gia, chong trung va khao sat gia.",
        "Cap nhat QD, PL VI, TTGT roi to chuc tham dinh vong cuoi doc lap.",
    ]:
        add_bullet(doc, s)
    add_para(doc, "Rui ro neu khong sua: tao can cu mua sam vuot dinh muc, dung van ban het hieu luc, trung dinh muc va kho bao ve khi thanh tra, kiem toan.")

    add_heading(doc, "PHAN VII. PHAN TICH KHA THI VA RUI RO (TU VAN)")
    add_para(doc, "Nhan dinh phan nay mang tinh tu van. Viec hoan thien kha thi neu tach ho so thanh hai nhanh: chuc danh + hoat dong chung; thiet bi chuyen dung. Kham lon nhat la chuan hoa du lieu nhan su va phan loai hon 500 dong PL III. Can xac nhan cheo cua Phong TCCB&CTHSSV, Phong TCKT va don vi quan tri tai san.")

    add_heading(doc, "KIEM TRA CHAT LUONG CUOI CUNG")
    for s in [
        "Da ra du 4 nhom tieu chi va doi chieu 3 lop ho so.",
        "Da dung Phu luc moi cua QD 10, khong dung phu luc cu cua QD 15 de tinh.",
        "Da kiem chung so luong bang phep tinh va chi ro mau so can xac minh.",
        "Da tach loi, noi dung dat va nhan dinh tu van; GROK chi la tham khao.",
        "Khong ket luan TTGT thieu so la vi pham trong boi canh da duoc nguoi dung xac nhan.",
    ]:
        add_bullet(doc, s)
    add_para(doc,
        "Nguon du lieu da dung: ghi tai Phan I. "
        "Nguoi kiem tra: AI ho tro theo KTC-Ra-Soat-897-v2; "
        "de nghi TH-HC&QT, TCKT va TCCB&CTHSSV kiem tra cheo. "
        "Trang thai phe duyet: BAN NHAP RA SOAT - CHUA DUOC PHE DUYET CHINH THUC.")

    for section in doc.sections:
        footer_p = section.footer.paragraphs[0]
        footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        font(footer_p.add_run("Trang "), 10)
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), "PAGE")
        footer_p._p.append(fld)

    doc.save(out_path)
    return out_path


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tao Bao cao Ra soat KTC-897 (.docx)")
    parser.add_argument("--out", help="Duong dan file dau ra (.docx)", default=None)
    parser.add_argument("--ho-so", help="Ten ho so (dung dat ten file mac dinh)",
                        default="ra-soat-chinh-thuc")
    parser.add_argument("--ngay", help="Ngay ra soat (vd: 13/8/2026)", default=None)
    args = parser.parse_args()

    out_path = resolve_output(args.out, args.ho_so)
    result = build_report(out_path, args.ho_so, args.ngay)
    print(f"OK Da xuat: {result}")
