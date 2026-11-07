#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sinh_nhat_ky_pham_vi.py – Sinh khung nhật ký phạm vi từ kết quả cổng hồ sơ (v4.6.13-KTC, C)

Đọc cong.json do kiem_ke_ho_so.py tạo, sinh khung nhat_ky_pham_vi cho du_lieu.json:
  - so_dieu_da_doc: đếm tiêu đề "Điều N." trong văn bản
  - trich_dau, trich_cuoi: 60 ký tự đầu/cuối đã chuẩn hóa
  - da_doc: "toan_van" nếu đọc đủ
  - hieu_luc: để trống, NGƯỜI RÀ SOÁT PHẢI ĐIỀN

Cách dùng:
  python sinh_nhat_ky_pham_vi.py cong.json [--ra nhat_ky.json]
"""
import sys, os, json, re, argparse, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nhan_dien_chung as ND
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def doc_docx(path):
    """Đọc nội dung text từ file .docx."""
    try:
        with zipfile.ZipFile(path) as z:
            root = ET.fromstring(z.read('word/document.xml'))
            txt = []
            for p in root.iter(W + 'p'):
                line = ''.join((e.text or '') for e in p.iter(W + 't'))
                if line.strip(): txt.append(line)
            return '\n'.join(txt)
    except Exception:
        return ''

def dem_dieu(txt):
    """Đếm số tiêu đề "Điều N." theo quy tắc của tao_bao_cao.py."""
    return len(re.findall(r'\bĐiều\s+\d+[a-z]?\s*\.', txt or ''))

def trich(txt, dau=True, do_dai=60):
    """Trích nguyên văn đầu hoặc cuối, chuẩn hóa khoảng trắng."""
    s = ND.chuan_trinh_bay(txt or '')
    if not s: return ''
    if dau:
        return s[:do_dai].strip()
    else:
        return s[-do_dai:].strip()

def sinh(cong_json_path):
    with open(cong_json_path, 'r', encoding='utf-8') as f:
        cong = json.load(f)

    nk = []
    # Lấy từ nguon_can_doi_chieu (văn bản được dẫn và đã có toàn văn)
    for e in cong.get('nguon_can_doi_chieu', []):
        if not isinstance(e, dict): continue
        nguon = e.get('so_hieu') or e.get('ten') or ''
        if not nguon: continue

        # Đọc nội dung từ đường dẫn tệp
        duong_dan = e.get('duong_dan')
        txt = ''
        if duong_dan and os.path.exists(duong_dan):
            if duong_dan.lower().endswith('.docx'):
                txt = doc_docx(duong_dan)
            # PDF: cần pdftotext, bỏ qua ở đây

        entry = {
            'nguon': nguon,
            'da_doc': 'toan_van' if txt else 'chua_doc',
            'pham_vi_da_doc': 'Toàn văn' if txt else '',
            'so_dieu_da_doc': dem_dieu(txt),
            'trich_dau': trich(txt, dau=True),
            'trich_cuoi': trich(txt, dau=False),
            'hieu_luc': {
                '_CANH_BAO': 'NGƯỜI RÀ SOÁT PHẢI KIỂM TRA VÀ ĐIỀN',
                'da_kiem': False,
                'ket_qua': ''
            }
        }
        nk.append(entry)

    return nk

def main():
    parser = argparse.ArgumentParser(description='Sinh khung nhật ký phạm vi từ cong.json')
    parser.add_argument('cong', help='Đường dẫn cong.json')
    parser.add_argument('--ra', '-o', default=None, help='Đường dẫn tệp JSON đầu ra (mặc định: in ra stdout)')
    args = parser.parse_args()

    nk = sinh(args.cong)

    out = {'_ghi_chu': 'Khung sinh tự động — NGƯỜI RÀ SOÁT PHẢI KIỂM TRA hieu_luc và phan_chua_doc',
           'nhat_ky_pham_vi': nk}

    if args.ra:
        with open(args.ra, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print('Đã ghi %d mục vào %s' % (len(nk), args.ra))
    else:
        print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
