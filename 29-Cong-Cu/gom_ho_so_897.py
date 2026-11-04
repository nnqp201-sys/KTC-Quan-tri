# -*- coding: utf-8 -*-
"""Tự gom hồ sơ cho cổng KTC-Ra-Soat-897 (lớp ngoài lõi — KHÔNG sửa lõi v4.5).

Vấn đề: cổng 897 (Bước 1) chặn khi thiếu toàn văn văn bản được viện dẫn, kể cả văn bản đã có sẵn trong
KTC-Database hoặc thư mục làm việc → người dùng bị yêu cầu gửi lại tệp mà hệ đã có.

Công cụ này làm phần "chuẩn bị hồ sơ" trước khi gọi cổng:
  1. Chép dự thảo (+ tệp kèm) vào thư mục hồ sơ; nếu dự thảo có <w:noBreakHyphen> thì báo
     (cổng đọc mất dấu này → ký hiệu sai, không khớp kho) — dùng --chuan-hoa-gach để tạo bản đã đổi.
  2. Chạy cổng lần 1, đọc danh sách văn bản "THIẾU".
  3. Tìm từng văn bản trong KTC-Database và các thư mục --tim (theo số + ký hiệu ở dòng "Số:" đầu tệp,
     hoặc tên tệp), chỉ nhận .docx/.xlsx/PDF có lớp chữ; chép vào hồ sơ.
  4. Chạy cổng lần 2, in danh sách CÒN THIẾU thật sự (chỉ những văn bản này mới phải hỏi người dùng).

Cách dùng:
  python 29-Cong-Cu/gom_ho_so_897.py <du_thao.docx> --ra <thu_muc_ho_so> [--tim <thư mục> ...] [--chuan-hoa-gach]
"""
import argparse, json, os, re, shutil, subprocess, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))
from duong_dan import ktc_database  # noqa

SKILL_GOC = os.path.expandvars(r'%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin')
DUOI = ('.docx', '.xlsx', '.pdf')


def tim_cong():
    for goc, _, fs in os.walk(SKILL_GOC):
        if goc.endswith(os.path.join('ktc-ra-soat-897', 'tools')) and 'kiem_ke_ho_so.py' in fs:
            return os.path.join(goc, 'kiem_ke_ho_so.py')
    sys.exit('Không tìm thấy kiem_ke_ho_so.py của skill ktc-ra-soat-897.')


def khong_dau(s):
    s = unicodedata.normalize('NFD', s or '').replace('đ', 'd').replace('Đ', 'D')
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').upper()


def chuan_hoa_gach(src, dst):
    import docx
    from docx.oxml.ns import qn
    d = docx.Document(src); n = 0
    for nb in list(d.element.body.iter(qn('w:noBreakHyphen'))):
        t = d.element.makeelement(qn('w:t'), {}); t.text = '-'
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        nb.addprevious(t); nb.getparent().remove(nb); n += 1
    d.save(dst); return n


def doc_dau(p):
    """Văn bản đầu tệp (để tìm dòng 'Số: …')."""
    try:
        if p.lower().endswith('.docx'):
            import docx
            return '\n'.join(x.text for x in docx.Document(p).paragraphs[:60]) + '\n' + '\n'.join(
                c.text for t in docx.Document(p).tables[:2] for r in t.rows for c in r.cells)
        if p.lower().endswith('.pdf'):
            import pymupdf
            d = pymupdf.open(p)
            return ''.join(d[i].get_text() for i in range(min(2, len(d))))
    except Exception:
        return ''
    return ''


def pdf_co_chu(p):
    try:
        import pymupdf
        d = pymupdf.open(p)
        return sum(len(x.get_text().strip()) for x in d) / max(len(d), 1) > 200
    except Exception:
        return False


def chay_cong(cong, ho_so, out_json):
    subprocess.run([sys.executable, '-X', 'utf8', cong, ho_so, '--tac-vu', 'ra-soat', '--json', out_json],
                   capture_output=True, text=True, encoding='utf-8')
    return json.load(open(out_json, encoding='utf-8'))


def lap_chi_muc(goc_list):
    tep = []
    for g in goc_list:
        for r, _, fs in os.walk(g):
            if os.sep + '.' in r: continue
            for f in fs:
                if f.lower().endswith(DUOI) and not f.startswith('~$'):
                    tep.append(os.path.join(r, f))
    return tep


def tim_van_ban(x, chi_muc):
    so = re.match(r'\d+', x['so'] or '')
    if not so: return None
    so = so.group(0)
    ky = re.sub(r'[^A-Z]', '', khong_dau(x['so'].split('/', 1)[-1]))[:6]  # vd SGDDTG, QDUBND
    ung = []
    for p in chi_muc:
        ten = khong_dau(os.path.basename(p))
        if not re.search(r'(?<!\d)0*%s(?!\d)' % so, ten): continue
        diem = sum(1 for k in re.findall(r'[A-Z]{2,}', khong_dau(x['so'])) if k in ten)
        ung.append((diem, p))
    for _, p in sorted(ung, reverse=True)[:8]:
        if p.lower().endswith('.pdf') and not pdf_co_chu(p): continue
        dau = re.sub(r'[\s\-–]', '', khong_dau(doc_dau(p)))
        ky_day_du = re.sub(r'[^A-Z0-9/]', '', khong_dau(x['so']))  # vd 287/QDUBND — khớp đủ ký hiệu, không chỉ số
        if ('SO:' + ky_day_du) in dau or ('SO' + ky_day_du) in dau:
            return p
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('du_thao'); ap.add_argument('--ra', required=True)
    ap.add_argument('--tim', action='append', default=[])
    ap.add_argument('--kem', action='append', default=[])
    ap.add_argument('--chuan-hoa-gach', action='store_true')
    a = ap.parse_args()
    hs = os.path.join(a.ra, 'hs'); os.makedirs(hs, exist_ok=True)
    dt = os.path.join(hs, os.path.basename(a.du_thao))
    if a.chuan_hoa_gach:
        print('Đổi', chuan_hoa_gach(a.du_thao, dt), 'gạch nối không ngắt → gạch nối thường (bản trong hồ sơ).')
    else:
        shutil.copy2(a.du_thao, dt)
    for k in a.kem: shutil.copy2(k, hs)
    cong = tim_cong()
    c1 = chay_cong(cong, hs, os.path.join(a.ra, 'cong_lan1.json'))
    thieu = [x for x in c1['van_ban_de_cap'] if x['trang_thai'] == 'THIẾU']
    print('Cổng lần 1: %s — thiếu %d văn bản.' % (c1['ket_luan'], len(thieu)))
    chi_muc = lap_chi_muc([ktc_database(False)] + a.tim)
    da_gom = []
    for x in thieu:
        p = tim_van_ban(x, chi_muc)
        if p:
            shutil.copy2(p, hs); da_gom.append((x['so'], p))
    for so, p in da_gom: print('  + gom %-28s ← %s' % (so, p))
    c2 = chay_cong(cong, hs, os.path.join(a.ra, 'cong.json'))
    con = [x for x in c2['van_ban_de_cap'] if x['trang_thai'] == 'THIẾU']
    print('Cổng lần 2: %s — đã gom %d, còn thiếu %d.' % (c2['ket_luan'], len(da_gom), len(con)))
    for l in c2['ly_do_chan']: print('  - ' + l[:200])


if __name__ == '__main__':
    main()
