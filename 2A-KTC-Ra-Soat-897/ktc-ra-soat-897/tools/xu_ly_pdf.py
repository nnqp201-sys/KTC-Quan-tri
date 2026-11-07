#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
xu_ly_pdf.py – Xử lý PDF scan và PDF có chữ ký số cho KTC-Ra-Soat-897 v4.6.13-KTC

Phần D: Bản scan (không có text layer)
- Nhận diện PDF scan bằng pdffonts/pdfinfo
- OCR vùng số hiệu, ngày tháng để tạo bản chữ có đánh dấu
- Tích hợp logic từ skill chuyen-pdf

Phần E: PDF có chữ ký số
- Đọc thông tin chữ ký số (người ký, thời gian, chứng thư)
- Xác minh tính toàn vẹn (signature intact)
- Trích xuất metadata chữ ký cho báo cáo

Cách dùng:
  python xu_ly_pdf.py --kiem-tra <file.pdf>     # Kiểm tra loại PDF
  python xu_ly_pdf.py --chu-ky <file.pdf>       # Đọc chữ ký số
  python xu_ly_pdf.py --ocr <file.pdf> [--ra <output.txt>]  # OCR bản scan
"""
import sys
import os
import subprocess
import json
import re
import argparse
from datetime import datetime

# Reconfigure stdout cho Windows UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PHIEN_BAN = 'v4.6.13-KTC-D-E'


def chay_lenh(cmd, timeout=30):
    """Chạy lệnh shell, trả về (stdout, stderr, returncode)."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=timeout)
        return r.stdout, r.stderr, r.returncode
    except subprocess.TimeoutExpired:
        return '', 'Timeout', -1
    except Exception as e:
        return '', str(e), -1


def kiem_tra_pdf(duong_dan):
    """Kiểm tra loại PDF: có text layer không, có chữ ký số không.

    Trả về dict:
    {
        'loai': 'text' | 'scan' | 'hon_hop',
        'co_text_layer': True/False,
        'co_chu_ky_so': True/False,
        'so_trang': int,
        'fonts': [...],
        'chi_tiet': str
    }
    """
    kq = {
        'duong_dan': duong_dan,
        'loai': 'khong_xac_dinh',
        'co_text_layer': False,
        'co_chu_ky_so': False,
        'so_trang': 0,
        'fonts': [],
        'chi_tiet': ''
    }

    if not os.path.exists(duong_dan):
        kq['chi_tiet'] = 'Tệp không tồn tại'
        return kq

    # Kiểm tra pdfinfo
    stdout, stderr, rc = chay_lenh(f'pdfinfo "{duong_dan}"')
    if rc == 0:
        # Đọc số trang
        m = re.search(r'Pages:\s+(\d+)', stdout)
        if m:
            kq['so_trang'] = int(m.group(1))

    # Kiểm tra pdffonts - có font nhúng = có text layer
    stdout, stderr, rc = chay_lenh(f'pdffonts "{duong_dan}"')
    if rc == 0:
        lines = stdout.strip().split('\n')
        # Bỏ 2 dòng header
        font_lines = [l for l in lines[2:] if l.strip()]
        kq['fonts'] = font_lines
        kq['co_text_layer'] = len(font_lines) > 0

    # Kiểm tra chữ ký số bằng pdfsig (poppler-utils)
    stdout, stderr, rc = chay_lenh(f'pdfsig "{duong_dan}"')
    if rc == 0:
        kq['co_chu_ky_so'] = 'Signature' in stdout or 'Chữ ký' in stdout
        if kq['co_chu_ky_so']:
            kq['chi_tiet_chu_ky'] = stdout.strip()

    # Phân loại
    if kq['co_text_layer']:
        kq['loai'] = 'text'
    else:
        kq['loai'] = 'scan'

    kq['chi_tiet'] = f"Trang: {kq['so_trang']}, Font: {len(kq['fonts'])}, Ký số: {kq['co_chu_ky_so']}"

    return kq


def doc_chu_ky_so(duong_dan):
    """Đọc thông tin chữ ký số từ PDF.

    Trả về list các chữ ký:
    [{
        'nguoi_ky': str,
        'thoi_gian': str,
        'chung_thu': str,
        'hop_le': True/False,
        'toan_ven': True/False,
        'chi_tiet': str
    }]
    """
    chu_ky = []

    if not os.path.exists(duong_dan):
        return chu_ky

    # Dùng pdfsig để đọc chữ ký
    stdout, stderr, rc = chay_lenh(f'pdfsig -nocert "{duong_dan}"')
    if rc != 0:
        # Thử cách khác: qpdf hoặc pdfcpu
        stdout, stderr, rc = chay_lenh(f'pdfcpu info "{duong_dan}"')

    if rc == 0 and stdout:
        # Parse kết quả pdfsig
        # Mẫu: "Signature #1: ... Signer Certificate Common Name: ... Signing Time: ..."
        sig_blocks = re.split(r'Signature #\d+:', stdout)
        for i, block in enumerate(sig_blocks[1:], 1):
            sig = {
                'so_thu_tu': i,
                'nguoi_ky': '',
                'thoi_gian': '',
                'chung_thu': '',
                'hop_le': False,
                'toan_ven': False,
                'chi_tiet': block.strip()[:500]
            }

            # Trích xuất thông tin
            m = re.search(r'Signer Certificate Common Name:\s*(.+?)(?:\n|$)', block)
            if m:
                sig['nguoi_ky'] = m.group(1).strip()

            m = re.search(r'Signing Time:\s*(.+?)(?:\n|$)', block)
            if m:
                sig['thoi_gian'] = m.group(1).strip()

            m = re.search(r'Certificate Issuer:\s*(.+?)(?:\n|$)', block)
            if m:
                sig['chung_thu'] = m.group(1).strip()

            sig['hop_le'] = 'valid' in block.lower() or 'hợp lệ' in block.lower()
            sig['toan_ven'] = 'intact' in block.lower() or 'toàn vẹn' in block.lower()

            chu_ky.append(sig)

    # Nếu không có pdfsig, thử dùng PyPDF2/pikepdf
    if not chu_ky:
        try:
            import pikepdf
            with pikepdf.open(duong_dan) as pdf:
                if '/AcroForm' in pdf.Root:
                    form = pdf.Root.AcroForm
                    if '/SigFlags' in form:
                        chu_ky.append({
                            'so_thu_tu': 1,
                            'nguoi_ky': '(Có chữ ký - cần pdfsig để đọc chi tiết)',
                            'thoi_gian': '',
                            'chung_thu': '',
                            'hop_le': None,
                            'toan_ven': None,
                            'chi_tiet': 'PDF có trường chữ ký AcroForm'
                        })
        except ImportError:
            pass
        except Exception:
            pass

    return chu_ky


def ocr_pdf_scan(duong_dan, ra=None):
    """OCR bản scan PDF, trích xuất văn bản.

    Ưu tiên: tesseract > ocrmypdf > Google Vision

    Trả về dict:
    {
        'thanh_cong': True/False,
        'van_ban': str,
        'so_hieu': str (nếu tìm được),
        'ngay_thang': str (nếu tìm được),
        'loi': str
    }
    """
    kq = {
        'thanh_cong': False,
        'van_ban': '',
        'so_hieu': '',
        'ngay_thang': '',
        'loi': ''
    }

    if not os.path.exists(duong_dan):
        kq['loi'] = 'Tệp không tồn tại'
        return kq

    # Thử ocrmypdf (tạo PDF có text layer)
    import tempfile
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
        tmp_path = tmp.name

    stdout, stderr, rc = chay_lenh(
        f'ocrmypdf -l vie+eng --skip-text --output-type pdf "{duong_dan}" "{tmp_path}"',
        timeout=120
    )

    if rc == 0 and os.path.exists(tmp_path):
        # Trích xuất text từ PDF đã OCR
        stdout, stderr, rc = chay_lenh(f'pdftotext "{tmp_path}" -')
        if rc == 0:
            kq['thanh_cong'] = True
            kq['van_ban'] = stdout
    else:
        # Fallback: convert sang ảnh rồi tesseract
        stdout, stderr, rc = chay_lenh(
            f'pdftoppm -png -r 300 "{duong_dan}" - | tesseract stdin stdout -l vie+eng',
            timeout=120
        )
        if rc == 0:
            kq['thanh_cong'] = True
            kq['van_ban'] = stdout
        else:
            kq['loi'] = f'OCR thất bại: {stderr}'

    # Dọn dẹp
    try:
        os.unlink(tmp_path)
    except:
        pass

    # Trích xuất số hiệu, ngày tháng
    if kq['van_ban']:
        # Tìm số hiệu văn bản: Số: 123/XX-YY hoặc Số: 123/QĐ-...
        m = re.search(r'Số[:\s]+(\d+[/\-][A-Za-z0-9\-/]+)', kq['van_ban'])
        if m:
            kq['so_hieu'] = m.group(1).strip()

        # Tìm ngày tháng: ngày ... tháng ... năm ...
        m = re.search(r'ngày\s+(\d{1,2})\s+tháng\s+(\d{1,2})\s+năm\s+(\d{4})', kq['van_ban'], re.I)
        if m:
            kq['ngay_thang'] = f"{m.group(1)}/{m.group(2)}/{m.group(3)}"

    # Ghi ra tệp nếu yêu cầu
    if ra and kq['van_ban']:
        with open(ra, 'w', encoding='utf-8') as f:
            f.write(kq['van_ban'])
        print(f'Đã ghi OCR ra: {ra}')

    return kq


def tao_ban_chu_danh_dau(duong_dan, thu_muc_ra):
    """Tạo bản chữ có đánh dấu từ PDF scan.

    Xuất:
    - <ten>_ocr.txt: văn bản OCR
    - <ten>_metadata.json: thông tin trích xuất (số hiệu, ngày, chữ ký)
    """
    ten_goc = os.path.splitext(os.path.basename(duong_dan))[0]

    # Kiểm tra loại PDF
    info = kiem_tra_pdf(duong_dan)

    # Đọc chữ ký số
    chu_ky = doc_chu_ky_so(duong_dan) if info['co_chu_ky_so'] else []

    # OCR nếu là scan
    ocr_kq = None
    if info['loai'] == 'scan':
        txt_path = os.path.join(thu_muc_ra, f'{ten_goc}_ocr.txt')
        ocr_kq = ocr_pdf_scan(duong_dan, ra=txt_path)

    # Tạo metadata
    metadata = {
        'nguon': duong_dan,
        'thoi_gian_xu_ly': datetime.now().isoformat(),
        'phien_ban': PHIEN_BAN,
        'thong_tin_pdf': info,
        'chu_ky_so': chu_ky,
        'ocr': ocr_kq
    }

    json_path = os.path.join(thu_muc_ra, f'{ten_goc}_metadata.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f'Đã tạo metadata: {json_path}')
    return metadata


def main():
    parser = argparse.ArgumentParser(description='Xử lý PDF scan và chữ ký số cho 897')
    parser.add_argument('--kiem-tra', metavar='PDF', help='Kiểm tra loại PDF')
    parser.add_argument('--chu-ky', metavar='PDF', help='Đọc chữ ký số')
    parser.add_argument('--ocr', metavar='PDF', help='OCR bản scan')
    parser.add_argument('--ra', '-o', default=None, help='Đường dẫn đầu ra')
    parser.add_argument('--danh-dau', metavar='PDF', help='Tạo bản chữ có đánh dấu')
    parser.add_argument('--thu-muc', default='.', help='Thư mục đầu ra cho --danh-dau')
    args = parser.parse_args()

    if args.kiem_tra:
        kq = kiem_tra_pdf(args.kiem_tra)
        print(json.dumps(kq, ensure_ascii=False, indent=2))
    elif args.chu_ky:
        kq = doc_chu_ky_so(args.chu_ky)
        print(json.dumps(kq, ensure_ascii=False, indent=2))
    elif args.ocr:
        kq = ocr_pdf_scan(args.ocr, ra=args.ra)
        if not args.ra:
            print(json.dumps(kq, ensure_ascii=False, indent=2))
    elif args.danh_dau:
        os.makedirs(args.thu_muc, exist_ok=True)
        kq = tao_ban_chu_danh_dau(args.danh_dau, args.thu_muc)
        print(json.dumps(kq, ensure_ascii=False, indent=2))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
