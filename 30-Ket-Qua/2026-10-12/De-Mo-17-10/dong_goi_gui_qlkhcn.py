# -*- coding: utf-8 -*-
"""Đóng gói kịch bản và dữ liệu mẫu gửi phòng QLKHCN&HTPT (hạn 15/10/2026). KHÔNG đưa tệp đáp án và tệp mẫu gốc chưa ẩn danh."""
import glob, os, sys, zipfile
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
DUAN = os.path.abspath(os.path.join(D, '..', '..', '..'))
RA = os.path.join(DUAN, '30-Ket-Qua', '2026-10-13', 'Gui-QLKHCN')
os.makedirs(RA, exist_ok=True)
z = os.path.join(RA, 'Kich-ban-va-du-lieu-mau_Trinh-dien-AI_17.10.2026_P-THHC.zip')
TEP = [(sorted(glob.glob(os.path.join(DUAN, '30-Ket-Qua', '2026-10-13', 'Soan-Thao', 'PA_*v7.docx')))[-1], '01_Phuong-an-trinh-dien_v7.docx'),
       (os.path.join(D, 'KICH-BAN-LOI-TRINH-BAY_17.10.2026.docx'), '02_Kich-ban-loi-trinh-bay.docx'),
       (sorted(glob.glob(os.path.join(D, 'Trinh-chieu', '*_v3.pdf')))[-1], '03_Trang-trinh-chieu.pdf')]
n = 0
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as f:
    for src, dst in TEP:
        f.write(src, dst); n += 1
    goc = os.path.join(D, 'Du-lieu-gia-dinh')
    for root, _, fs in os.walk(goc):
        if '_Dap-an' in root:
            continue
        for x in fs:
            if x.startswith('4. ') or x.startswith('BaoCao_RaSoat_CTr') or x == 'desktop.ini':
                continue
            p = os.path.join(root, x)
            f.write(p, '04_Du-lieu-mau/' + os.path.relpath(p, goc).replace(os.sep, '/')); n += 1
ds = zipfile.ZipFile(z).namelist()
print(n, 'tệp ->', z, os.path.getsize(z) // 1024, 'KB')
print('lọt đáp án/tệp gốc:', [i for i in ds if 'Dap-an' in i or i.split('/')[-1].startswith(('4. ', 'BaoCao_RaSoat_CTr'))] or 'không')
for i in ds:
    print('  ', i)
