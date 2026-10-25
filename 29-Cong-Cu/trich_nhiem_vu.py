# -*- coding: utf-8 -*-
"""Trich NHIEM VU CHI TIET tu noi dung van ban (TB ket luan, KH) da ghi trong CSDL theo doi.

Moi dong CSDL nhom 'Nhiem vu' co cot 'File da tai' (.docx) -> doc noi dung -> tach tung nhiem vu:
noi dung, don vi chu tri (ten goc + ma chuan), don vi phoi hop, han, san pham, vi tri trong van ban.
Ghi vao sheet "Chi tiet nhiem vu" cua CSDL (tao neu chua co). Chong trung theo (So ky hieu, Vi tri).

Nguyen tac:
- May TRICH, nguoi DUYET: cot Trang thai = "Máy trích — chờ duyệt"; Task_ID de trong (chi cap sau khi
  duyet, theo 20-Chuan-Chung/11-Quy-Tac-Task-ID.md).
- Ma don vi chi gan khi khop CHINH XAC bang bien the da biet (13-Bang-Ma-Don-Vi.md, KI-001), con lai de trong.
- Khong doan han: chi lay ngay viet ro trong cau ("trước ngày", "hoàn thành", "chậm nhất", "trong ngày").
- PDF khong doc duoc bang python-docx -> bao "Chỉ có PDF", khong bia noi dung.

Chay:  python 29-Cong-Cu/trich_nhiem_vu.py [--thu] [--tat-ca]
  --thu     in ket qua, khong ghi
  --tat-ca  trich ca nhom khac 'Nhiem vu' (vd 'Cho phan loai') neu co file
"""
import argparse
import os
import re
import shutil
import sys
import unicodedata
from datetime import datetime

import openpyxl
from docx import Document
from openpyxl.styles import Alignment, Font, PatternFill

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THU_MUC = os.path.join(GOC, '10-Dau-Vao', '01-Dau-Moi-Nop')
TEN_CSDL = 'CSDL-Theo-doi-nhiem-vu_20260929_v1.xlsx'
THU_MUC_FILE = '2026-09'
SHEET = 'Chi tiết nhiệm vụ'
COT = ['STT', 'Số ký hiệu', 'Loại', 'Ngày ban hành', 'Vị trí trong VB', 'Nội dung nhiệm vụ',
       'Đơn vị chủ trì (nguyên văn)', 'Mã đơn vị', 'Đơn vị phối hợp', 'Hạn hoàn thành', 'Sản phẩm',
       'Trạng thái', 'Task_ID', 'Ghi chú', 'Ngày trích']
RONG = [5, 15, 6, 12, 10, 70, 28, 10, 28, 13, 22, 20, 18, 30, 12]


def khong_dau(s):
    s = unicodedata.normalize('NFD', str(s or ''))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('đ', 'd').replace('Đ', 'D').lower()


# Bien the ten don vi -> ma chuan (13-Bang-Ma-Don-Vi.md). Khop theo tien to, sau khi bo dau.
DON_VI = [
    ('P-TCCB', ['phong tccb&cthssv', 'phong tccb & cthssv', 'phong tccb', 'phong to chuc can bo']),
    ('P-QLDT', ['phong qldt&bdcl', 'phong qldt & bdcl', 'phong qldt', 'phong quan ly dao tao']),
    ('P-THHC', ['phong th-hc&qt', 'phong th - hc&qt', 'phong th-hc & qt', 'phong thhc&qt',
                'phong tong hop - hanh chinh', 'ban truyen thong']),
    ('P-QLKH', ['phong qlkhcn&htpt', 'phong qlkhcn & htpt', 'phong qlkhcn', 'phong quan ly khoa hoc']),
    ('P-TCKT', ['phong tc-kt', 'phong tc - kt', 'phong tai chinh']),
    ('K-KHCB', ['khoa cac khoa hoc co ban', 'khoa khcb']),
    ('K-SUPH', ['khoa su pham']),
    ('K-KTNL', ['khoa kinh te va nong lam', 'khoa kt&nl', 'khoa ktnl']),
    ('K-KTCN', ['khoa ky thuat va cong nghe', 'khoa kt&cn', 'khoa ktcn']),
    ('K-YDUOC', ['khoa y - duoc', 'khoa y-duoc', 'khoa y duoc']),
    ('K-DTSHLX', ['khoa dao tao va sat hach lai xe', 'khoa dt&shlx', 'khoa dtshlx']),
]
# Chu the hay gap o dau cau nhung khong phai don vi cap mot -> giu nguyen van, khong gan ma
CHU_THE = r'(phong [^,:;.]{2,40}?|khoa [^,:;.]{2,40}?|bo mon [^,:;.]{2,40}?|ban [^,:;.]{2,40}?|' \
          r'to [^,:;.]{2,30}?|bo phan [^,:;.]{2,40}?|van phong [^,:;.]{2,30}?|cac don vi[^,:;.]{0,40}?|' \
          r'cac chi bo[^,:;.]{0,40}?|doan thanh nien[^,:;.]{0,30}?|cong doan[^,:;.]{0,30}?)'
DONG_TU = r'(?=\s+(?:chu tri|tham muu|phoi hop|thuc hien|trien khai|to chuc|xay dung|hoan thanh|' \
          r'thong bao|rà|ra soat|bao cao|chuan bi|lap|du thao|theo doi|kiem tra|cap nhat|tiep tuc|' \
          r'khan truong|lam viec|dang ky|gui|nop|phan cong|huong dan|chi dao)\b|\s*[:,])'


def ma_don_vi(ten):
    k = khong_dau(ten).strip()
    for ma, bien_the in DON_VI:
        if any(k.startswith(b) for b in bien_the):
            return ma
    return ''


def tach_chu_the(cau):
    """Tra ve (ten chu the nguyen van, phan con lai) neu cau mo dau bang mot don vi."""
    k = khong_dau(cau)
    m = re.match(CHU_THE + DONG_TU, k)
    if not m:
        return '', cau
    n = len(m.group(1))
    return cau[:n].strip(), cau[n:].lstrip(' :–-').strip()


def phoi_hop(cau):
    k = khong_dau(cau)
    m = re.search(r'phoi hop (?:voi )?(.+?)(?= tham muu| thuc hien| to chuc| xay dung| trien khai|[;.]|$)', k)
    return cau[m.start(1):m.end(1)].strip(' ,') if m else ''


NGAY = r'(\d{1,2})\s*/\s*(\d{1,2})(?:\s*/\s*(\d{4}))?'


VIEN_DAN = r'(so|thong tu|nghi dinh|nghi quyet|quyet dinh|ke hoach|cong van|bao cao|thong bao|chi thi|' \
           r'huong dan)\s+(so\s+)?[\w/.&-]*\d[\w/.&-]*\s+ngay\s+\d{1,2}\s*/\s*\d{1,2}(\s*/\s*\d{4})?'
# Uu tien: moc hoan thanh > ngay to chuc. Ngay cua van ban duoc vien dan bi loai truoc.
MOC_HAN = [r'(?:truoc ngay|cham nhat (?:la |truoc )?(?:ngay )?|hoan thanh (?:truoc |trong |vao )?ngay|'
           r'han (?:cuoi|chot)\s*:?\s*(?:ngay )?)',
           r'(?:vao (?:luc [^,;]{1,15} )?ngay|trong ngay|tu ngay)']


def han(cau, nam_mac_dinh):
    k = re.sub(VIEN_DAN, ' ', khong_dau(cau))
    for moc in MOC_HAN:
        m = re.search(moc + r'\s*' + NGAY, k)
        if m:
            d, mth, y = m.group(1), m.group(2), m.group(3) or str(nam_mac_dinh)
            try:
                return datetime(int(y), int(mth), int(d)).strftime('%d/%m/%Y')
            except ValueError:
                return ''
    return ''


# ---------- Doc van ban ----------

def doan_van(doc):
    """Doan van theo dung thu tu, gom ca o bang (tru bang tieu de/ky)."""
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]


TIEU_DE_GIAO = r'^(ii|iii|iv|v|vi)\.\s*(ke hoach|nhiem vu|noi dung|giao nhiem vu|to chuc thuc hien|' \
               r'cong viec|phan cong|y kien chi dao|ket luan|cac nhiem vu)'
KET_THUC = r'^(truong cao dang kon tum (thong bao|tran trong)|tren day la|noi nhan)'


def trich_tb(ps, nam):
    """Thong bao ket luan: lay muc giao viec (II. KE HOACH/NHIEM VU...), tach tung so muc va gach dau."""
    ds, trong, chu_the, so_muc = [], False, '', ''
    for p in ps:
        k = khong_dau(p)
        if re.match(TIEU_DE_GIAO, k):
            trong = True
            continue
        if not trong:
            continue
        if re.match(KET_THUC, k) or re.match(r'^(i|ii|iii|iv|v|vi)\.\s', k):
            if re.match(KET_THUC, k):
                break
            continue
        m = re.match(r'^(\d+(?:\.\d+)*)[.)]\s*(.*)$', p)
        if m:
            so_muc, than = m.group(1), m.group(2).strip()
            ct, con = tach_chu_the(than)
            if ct and (not con or than.rstrip().endswith(':')):
                chu_the = ct           # "3. Phong QLDT&BDCL:" -> chu the cho cac gach dau ben duoi
                continue
            chu_the = ct
            ds.append((so_muc, than, ct))
            continue
        m = re.match(r'^[-–+•*]\s*(.*)$', p)
        if m and so_muc:
            ds.append(('%s.%s' % (so_muc, sum(1 for x in ds if x[0].startswith(so_muc + '.')) + 1),
                       m.group(1).strip(), chu_the))
    return [ban_ghi(v, nd, ct, nam) for v, nd, ct in ds]


def ban_ghi(vi_tri, noi_dung, chu_the, nam, san_pham='', han_bang=''):
    ct, _ = tach_chu_the(noi_dung) if not chu_the else (chu_the, '')
    return {'vi_tri': vi_tri, 'noi_dung': noi_dung, 'chu_tri': ct, 'ma': ma_don_vi(ct),
            'phoi_hop': phoi_hop(noi_dung), 'han': han_bang or han(noi_dung, nam),
            'san_pham': san_pham}


def tim_cot(tieu_de, mau):
    for i, t in enumerate(tieu_de):
        if re.search(mau, t):
            return i
    return None


def trich_bang(doc, nam):
    """Ke hoach thuong co bang: Noi dung/Nhiem vu | Don vi chu tri | Phoi hop | Thoi gian | San pham."""
    ds = []
    for sb, bang in enumerate(doc.tables, 1):
        if len(bang.rows) < 2:
            continue
        td = [khong_dau(c.text) for c in bang.rows[0].cells]
        c_nd = tim_cot(td, r'noi dung|nhiem vu|cong viec|hoat dong')
        c_ct = tim_cot(td, r'chu tri|don vi thuc hien|phu trach|thuc hien')
        if c_nd is None or c_ct is None or c_nd == c_ct:
            continue
        c_ph = tim_cot(td, r'phoi hop')
        c_tg = tim_cot(td, r'thoi gian|thoi han|han|tien do')
        c_sp = tim_cot(td, r'san pham|ket qua')
        for sr, hang in enumerate(bang.rows[1:], 2):
            o = [c.text.strip() for c in hang.cells]
            nd = o[c_nd] if c_nd < len(o) else ''
            if len(nd) < 8 or nd == o[0] and len(set(o)) == 1:   # dong tieu de nhom (gop o)
                continue
            ct = o[c_ct] if c_ct < len(o) else ''
            r = ban_ghi('Bảng %d dòng %d' % (sb, sr), nd, ct, nam,
                        san_pham=o[c_sp] if c_sp is not None and c_sp < len(o) else '',
                        han_bang=han('ngay ' + o[c_tg], nam) if c_tg is not None and c_tg < len(o) else '')
            if c_ph is not None and c_ph < len(o):
                r['phoi_hop'] = o[c_ph]
            if c_tg is not None and not r['han'] and c_tg < len(o):
                r['han'] = o[c_tg]           # "Thang 10/2026", "Quy IV" -> giu nguyen van
            ds.append(r)
    return ds


def trich_kh(doc, ps, nam):
    ds = trich_bang(doc, nam)
    return ds if ds else trich_tb(ps, nam)   # khong co bang -> doc muc so nhu thong bao


# ---------- Chuong trinh chinh ----------

def sheet_chi_tiet(wb):
    if SHEET in wb.sheetnames:
        return wb[SHEET]
    ws = wb.create_sheet(SHEET, 1)
    ws.append(COT)
    for j, w in enumerate(RONG, 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(j)].width = w
        o = ws.cell(1, j)
        o.font = Font(bold=True)
        o.fill = PatternFill('solid', fgColor='D9E1F2')
        o.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    ws.freeze_panes = 'A2'
    return ws


def main():
    ap = argparse.ArgumentParser(description='Trích nhiệm vụ chi tiết từ nội dung văn bản')
    ap.add_argument('--thu', action='store_true', help='Chạy thử, không ghi')
    ap.add_argument('--tat-ca', action='store_true', help='Trích cả văn bản ngoài nhóm Nhiệm vụ')
    ap.add_argument('--thu-muc', default=THU_MUC)
    a = ap.parse_args()

    bay_gio = datetime.now()
    duong = os.path.join(a.thu_muc, TEN_CSDL)
    wb = openpyxl.load_workbook(duong)
    ws = wb['CSDL']
    r0 = next(r for r in range(1, 12) if str(ws.cell(r, 1).value or '').strip() == 'STT')
    ten = [ws.cell(r0, c).value for c in range(1, ws.max_column + 1)]
    cot = {t: ten.index(t) + 1 for t in ten if t}
    ct = sheet_chi_tiet(wb)
    da_co = {(str(r[1]), str(r[4])) for r in ct.iter_rows(min_row=2, values_only=True) if r[1]}
    stt = sum(1 for r in ct.iter_rows(min_row=2, values_only=True) if r[1])

    them, bo_qua, so_vb = [], [], 0
    for r in range(r0 + 1, ws.max_row + 1):
        so = ws.cell(r, cot['Số ký hiệu']).value
        nhom = ws.cell(r, cot['Nhóm']).value
        tep = ws.cell(r, cot['File đã tải']).value
        if not so or (nhom != 'Nhiệm vụ' and not a.tat_ca):
            continue
        if not tep:
            bo_qua.append('%s: chưa có tệp' % so)
            continue
        if any(k[0] == so for k in da_co):
            continue
        duong_tep = os.path.join(a.thu_muc, THU_MUC_FILE, tep)
        if not os.path.isfile(duong_tep):
            bo_qua.append('%s: không thấy tệp %s' % (so, tep))
            continue
        if not tep.lower().endswith('.docx'):
            bo_qua.append('%s: chỉ có %s — cần bản .docx để trích' % (so, os.path.splitext(tep)[1]))
            continue
        ngay = str(ws.cell(r, cot['Ngày ban hành']).value or '')
        nam = int(ngay[-4:]) if re.search(r'\d{4}$', ngay) else bay_gio.year
        try:
            doc = Document(duong_tep)
        except Exception as e:  # tep hong, khong phai docx that
            bo_qua.append('%s: không mở được tệp (%s)' % (so, e.__class__.__name__))
            continue
        ps = doan_van(doc)
        loai = 'TB' if '/TB-' in str(so) else 'KH'
        ds = trich_tb(ps, nam) if loai == 'TB' else trich_kh(doc, ps, nam)
        so_vb += 1
        if not ds:
            bo_qua.append('%s: không nhận diện được mục giao nhiệm vụ — cần người đọc' % so)
            continue
        for d in ds:
            stt += 1
            ghi_chu = '; '.join(x for x in (
                '' if d['chu_tri'] else 'thiếu đơn vị chủ trì',
                '' if d['ma'] or not d['chu_tri'] else 'đơn vị chưa có mã chuẩn',
                '' if d['han'] else 'không ghi hạn') if x)
            them.append([stt, so, loai, ngay, d['vi_tri'], d['noi_dung'], d['chu_tri'], d['ma'],
                         d['phoi_hop'], d['han'], d['san_pham'], 'Máy trích — chờ duyệt', None,
                         ghi_chu, bay_gio.strftime('%d/%m/%Y')])

    if not a.thu and them:
        sao_luu = os.path.join(a.thu_muc, '_sao-luu')
        os.makedirs(sao_luu, exist_ok=True)
        shutil.copy2(duong, os.path.join(sao_luu, 'CSDL_%s.xlsx' % bay_gio.strftime('%Y%m%d-%H%M%S')))
        for h in them:
            ct.append(h)
            for c in (6, 7, 9, 14):
                ct.cell(ct.max_row, c).alignment = Alignment(wrap_text=True, vertical='top')
        wb.save(duong)

    print('=== %sTRÍCH NHIỆM VỤ CHI TIẾT — %s ===' % ('[CHẠY THỬ] ' if a.thu else '',
                                                   bay_gio.strftime('%d/%m/%Y %H:%M')))
    print('Đọc %d văn bản · trích %d nhiệm vụ · thiếu đơn vị %d · thiếu hạn %d' % (
        so_vb, len(them), sum(1 for h in them if not h[6]), sum(1 for h in them if not h[9])))
    for h in them:
        print('  %-13s %-8s [%-7s] %-10s %s' % (h[1], h[4], h[7] or '?', h[9] or '—', h[5][:80]))
    if bo_qua:
        print('Chưa trích được:')
        for x in bo_qua:
            print('  - ' + x)
    return 0


if __name__ == '__main__':
    sys.exit(main())
