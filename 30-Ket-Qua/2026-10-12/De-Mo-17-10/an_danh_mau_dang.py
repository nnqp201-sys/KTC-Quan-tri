# -*- coding: utf-8 -*-
"""Ẩn danh 02 tệp mẫu văn bản Đảng (dự thảo Chương trình công tác tháng 10/2026 và Báo cáo rà soát KTC-897 v2.25)
để trình diễn ngày 17/10/2026. Thay tên tỉnh, tên người, số ký hiệu văn bản của địa phương; GIỮ NGUYÊN định dạng,
giữ số ký hiệu văn bản của Trung ương (đã công khai). Không sửa tệp gốc.
"""
import os, sys
import docx
from docx.oxml.ns import qn
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
GOC = os.path.join(D, 'Du-lieu-gia-dinh')
CHUNG = [  # (cũ, mới) — thứ tự: cụm dài trước
 ('ĐẢNG ỦY ỦY BAN NHÂN DÂN TỈNH', 'ĐẢNG ỦY ỦY BAN NHÂN DÂN PHƯỜNG XYZ'), ('Đảng ủy Ủy ban nhân dân tỉnh', 'Đảng ủy Ủy ban nhân dân phường XYZ'),
 ('Đảng ủy UBND tỉnh', 'Đảng ủy UBND phường XYZ'), ('Đảng bộ UBND tỉnh', 'Đảng bộ UBND phường XYZ'), ('DU-UBND-tinh', 'DU-UBND-phuong-XYZ'),
 ('UBND tỉnh', 'UBND phường'),
 ('ĐẢNG BỘ TỈNH QUẢNG NGÃI', 'ĐẢNG BỘ TỈNH A'), ('TỈNH ỦY QUẢNG NGÃI', 'TỈNH ỦY A'), ('Quảng Ngãi, ngày', 'Tỉnh A, ngày'),
 ('tỉnh Quảng Ngãi', 'tỉnh A'), ('(Quảng Ngãi)', '(tỉnh A)'), ('Quảng Ngãi', 'tỉnh A'),
 ('Phạm Xuân Duệ', 'Nguyễn Văn A'), ('PhongKinhTe7', 'ChuyenVien7'),
 ('(06, 13, 27-CTr/ĐU)', '(05, 11, 25-CTr/ĐU)'),
 ('; kho 01-04 có KH-532 (siêu dữ liệu nhắc 13-CTr/ĐU)', ''),
 ('06-CTr/ĐU', '05-CTr/ĐU'), ('08-CTr/TU', '09-CTr/TU'), ('27-CTr/ĐU', '25-CTr/ĐU'), ('13-CTr/ĐU', '11-CTr/ĐU'),
 ('1394-KL/ĐU', '1286-KL/ĐU'), ('98-KH/TU', '87-KH/TU'), ('12-QC/ĐU', '10-QC/ĐU'),
 ('Kết luận 1394', 'Kết luận 1286'), ('Số hiệu 1394', 'Số hiệu 1286'), ('Quy chế 12-QC', 'Quy chế 10-QC'),
 ('Đảng ủy.Lệ', 'Đảng ủy.Th'), ('ký tự "Lệ"', 'ký tự "Th"'),
]


def thay_doan(p, cu, moi):
    """Thay trong một đoạn, kể cả khi cụm cần thay nằm vắt qua nhiều run; giữ định dạng run đầu."""
    n = 0
    while True:
        ts = [t for t in p.iter(qn('w:t'))]
        full = ''.join(t.text or '' for t in ts)
        i = full.find(cu)
        if i < 0:
            return n
        j, pos, dau = i + len(cu), 0, True
        for t in ts:
            s = t.text or ''; a, b = pos, pos + len(s); pos = b
            if b <= i or a >= j:
                continue
            trai, phai = s[:max(0, i - a)], s[max(0, j - a):] if j < b else ''
            t.text = trai + (moi if dau else '') + phai
            t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); dau = False
        n += 1


def an_danh(vao, ra, them=()):
    d = docx.Document(vao)
    goc = [d.element.body] + [x._element for s in d.sections for x in (s.header, s.footer, s.first_page_header, s.first_page_footer)]
    dem = {}
    for g in goc:
        for p in g.iter(qn('w:p')):
            for cu, moi in list(CHUNG) + list(them):
                k = thay_doan(p, cu, moi)
                if k:
                    dem[cu] = dem.get(cu, 0) + k
    cp = d.core_properties
    for th in ('title', 'author', 'last_modified_by', 'subject', 'comments', 'keywords', 'category'):
        v = getattr(cp, th) or ''
        for cu, moi in CHUNG:
            v = v.replace(cu, moi)
        setattr(cp, th, v)
    if cp.last_modified_by and 'python' not in (cp.author or '') and 'BaoCao' not in os.path.basename(ra):
        cp.last_modified_by = 'ChuyenVien7'
    os.makedirs(os.path.dirname(ra), exist_ok=True); d.save(ra)
    import zipfile                                   # thuộc tính ẩn trong docProps/app.xml
    tam = ra + '.tmp'
    with zipfile.ZipFile(ra) as zi, zipfile.ZipFile(tam, 'w', zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            b = zi.read(it.filename)
            if it.filename == 'docProps/app.xml':
                x = b.decode('utf-8')
                for cu, moi in CHUNG:
                    x = x.replace(cu, moi)
                b = x.encode('utf-8')
            zo.writestr(it, b)
    os.replace(tam, ra)
    con = ''.join(t.text or '' for g in goc for t in g.iter(qn('w:t')))
    sot = [x for x in ('Quảng Ngãi', 'QUẢNG NGÃI', 'Xuân Duệ', '1394', '06-CTr', '08-CTr', '27-CTr', '13-CTr', '98-KH', '12-QC', 'KH-532', 'PhongKinhTe', 'UBND tỉnh', 'nhân dân tỉnh', 'NHÂN DÂN TỈNH', 'phường XYZ XYZ', 'phường phường') if x in con]
    print(os.path.basename(ra), '| đã thay', sum(dem.values()), 'chỗ | còn sót:', sot or 'không', '| thuộc tính:', cp.title, '/', cp.author, '/', cp.last_modified_by)


# Tệp gốc (chưa ẩn danh) do người phụ trách giữ ngoài thư mục dữ liệu. Có tệp gốc thì ẩn danh từ gốc; không có thì áp tiếp
# bảng thay thế lên bản đã ẩn danh (các phép thay đều không đổi kết quả khi chạy lại).
CT = os.path.join(GOC, 'D4-Du-thao-can-ra-soat', 'Du-thao_Chuong-trinh-cong-tac-thang-10-2026_van-ban-Dang_an-danh.docx')
BC = os.path.join(D, 'Ket-qua-chay-truoc', 'BaoCao_RaSoat-897-v2.25_Chuong-trinh-cong-tac-thang-10-2026_van-ban-Dang_an-danh.docx')
G1 = os.path.join(GOC, '4. Chương trình công tác tháng 10.2026.docx')
G2 = os.path.join(GOC, 'BaoCao_RaSoat_CTr-Thang-10-2026-BTV-DU-UBND-tinh_20261011_v1.docx')
an_danh(G1 if os.path.exists(G1) else CT, CT, them=[('Lệ', 'Th')] if os.path.exists(G1) else ())
an_danh(G2 if os.path.exists(G2) else BC, BC)
