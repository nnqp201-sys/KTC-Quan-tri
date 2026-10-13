# -*- coding: utf-8 -*-
"""Chụp trang đầu các tệp kết quả thật (Cowork 12/10/2026 và kết quả chạy trước) thành ảnh 1920x1080 có dòng tiêu đề,
để ghep_video.py nối vào cuối từng video thao tác. Kết quả: anh_kq/T1_1.png, T1_2.png …"""
import os, subprocess, sys
import fitz
from PIL import Image, ImageDraw, ImageFont, ImageOps
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
G = os.path.dirname(D)
CW, CT = os.path.join(G, 'Ket-qua-cowork-12-10'), os.path.join(G, 'Ket-qua-chay-truoc')
# (mã video, tệp, trang tính, tiêu đề, trang pdf)
DS = [
    ('T1', os.path.join(CW, 'CQA_Ke-hoach-quy-IV-2026_tong-hop_du-thao.xlsx'), '', 'Kết quả: Dự thảo kế hoạch quý IV tổng hợp (Phụ lục Ia) do công cụ tạo', 0),
    ('T1', os.path.join(CT, 'Phan-1_Tong-hop-ke-hoach-quy-IV-2026_ket-qua-chay-truoc.xlsx'), '1-Bang-kiem', 'Kết quả: Bảng kiểm hồ sơ 06 đơn vị (sai mẫu, thiếu thời hạn, thiếu sản phẩm)', 0),
    ('T2', os.path.join(CT, 'Phan-1_Tong-hop-ke-hoach-quy-IV-2026_ket-qua-chay-truoc.xlsx'), '4-Doi-chieu-van-ban', 'Kết quả: Đối chiếu văn bản chỉ đạo với dự thảo kế hoạch', 0),
    ('T3', os.path.join(CW, '00_Bao-cao-thang-9-2026_Co-quan-A_du-thao.docx'), '', 'Kết quả: Dự thảo báo cáo tháng 9/2026 do công cụ tạo', 0),
    ('T3', os.path.join(CW, '00_Phu-luc-doi-chieu-KH-KQ-thang-9-2026.xlsx'), '', 'Kết quả: Phụ lục đối chiếu kế hoạch - kết quả 24 nhiệm vụ', 0),
    ('T4', os.path.join(CW, 'Bao_cao_Ra_soat_897_Du-thao_Chuong-trinh-cong-tac-thang10-2026_Dang-uy-UBND-phuong-XYZ_20261012.docx'), '', 'Kết quả: Báo cáo rà soát 897 - thông tin chung', 0),
    ('T4', os.path.join(CW, 'Bao_cao_Ra_soat_897_Du-thao_Chuong-trinh-cong-tac-thang10-2026_Dang-uy-UBND-phuong-XYZ_20261012.docx'), '', 'Kết quả: Báo cáo rà soát 897 - các phát hiện', 1),
]
ra = os.path.join(D, 'anh_kq'); os.makedirs(ra, exist_ok=True)
F = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 40)
dem = {}
for ma, tep, trang, td, so in DS:
    pdf = os.path.join(ra, os.path.splitext(os.path.basename(tep))[0] + (trang or '') + '.pdf')
    if not os.path.exists(pdf):
        subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(D, 'sang_pdf.ps1'), tep, pdf, trang], check=True)
    doc = fitz.open(pdf); so = min(so, len(doc) - 1)
    pix = doc[so].get_pixmap(dpi=150)
    anh = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    hop = ImageOps.invert(anh.convert('L')).point(lambda v: 255 if v > 20 else 0).getbbox()  # cắt lề trắng
    if hop:
        anh = anh.crop((max(hop[0] - 20, 0), max(hop[1] - 20, 0), min(hop[2] + 20, anh.width), min(hop[3] + 20, anh.height)))
    nen = Image.new('RGB', (1920, 1080), (236, 239, 243))
    ImageDraw.Draw(nen).rectangle([0, 0, 1920, 90], fill=(23, 63, 120))
    ImageDraw.Draw(nen).text((40, 22), td, font=F, fill='white')
    # Ảnh ngang: Vừa chiều rộng, lấy phần trên; ảnh dọc: Vừa chiều cao.
    k = 1840 / anh.width if anh.height * 1840 / anh.width <= 970 or anh.width > anh.height * 1.2 else max(970 / anh.height, min(1840 / anh.width, 1.6 * 970 / anh.height))
    k = min(k, 1840 / anh.width)
    anh = anh.resize((int(anh.width * k), int(anh.height * k)), Image.LANCZOS).crop((0, 0, int(anh.width * k), min(int(anh.height * k), 970)))
    nen.paste(anh, ((1920 - anh.width) // 2, 100))
    dem[ma] = dem.get(ma, 0) + 1
    p = os.path.join(ra, f'{ma}_{dem[ma]}.png'); nen.save(p); print(p)
