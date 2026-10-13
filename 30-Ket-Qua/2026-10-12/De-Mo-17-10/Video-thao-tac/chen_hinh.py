# -*- coding: utf-8 -*-
"""Chèn hình người trình bày (khung tròn, góc dưới trái) kèm dải sóng âm chạy theo giọng đọc vào video đã ghép.
Cách dùng: python chen_hinh.py <ảnh chân dung> <video vào> <video ra> [<video vào> <video ra> …]
Ảnh chân dung là ảnh cá nhân: KHÔNG đưa vào git; để ở thư mục trình diễn ngoài dự án."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
FF = imageio_ffmpeg.get_ffmpeg_exe()
TEN, DV = 'Nguyễn Ngọc Quang Phục', 'Phòng TH-HC&QT'
KHUNG_MAT = (105, 15, 365, 275)   # vùng khuôn mặt trong ảnh Chan-dung-Phuc.png (449x451)
R, RONG, CAO = 200, 300, 330       # đường kính ảnh tròn; kích thước tấm nền


def tam_nen(anh, ra):
    k = 3  # vẽ gấp 3 rồi thu lại cho mịn
    n = Image.new('RGBA', (RONG * k, CAO * k), (0, 0, 0, 0))
    d = ImageDraw.Draw(n)
    d.rounded_rectangle([0, 0, RONG * k - 1, CAO * k - 1], radius=26 * k, fill=(13, 59, 102, 225))
    m = Image.open(anh).convert('RGB').crop(KHUNG_MAT).resize((R * k, R * k), Image.LANCZOS)
    mat = Image.new('L', (R * k, R * k), 0); ImageDraw.Draw(mat).ellipse([0, 0, R * k - 1, R * k - 1], fill=255)
    x0, y0 = (RONG - R) // 2 * k, 14 * k
    d.ellipse([x0 - 5 * k, y0 - 5 * k, x0 + R * k + 5 * k, y0 + R * k + 5 * k], fill=(255, 255, 255, 255))
    n.paste(m, (x0, y0), mat)
    f1, f2 = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 21 * k), ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 18 * k)
    for chu, f, y in ((TEN, f1, 226), (DV, f2, 254)):
        w = d.textlength(chu, font=f); d.text(((RONG * k - w) / 2, y * k), chu, font=f, fill='white')
    n.resize((RONG, CAO), Image.LANCZOS).save(ra)


def chen(nen, vao, ra):
    loc = (f"[0:a]asplit[a1][a2];[a1]showwaves=s=260x40:mode=cline:rate=25:colors=0xFFD54A:scale=sqrt,format=rgba[w];"
           f"[0:v][1:v]overlay=36:H-h-36[b];[b][w]overlay=56:H-36-46:shortest=1[v]")
    subprocess.run([FF, '-y', '-loglevel', 'error', '-i', vao, '-i', nen, '-filter_complex', loc, '-map', '[v]', '-map', '[a2]',
                    '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', ra], check=True)
    print('→', ra)


if __name__ == '__main__':
    nen = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), '_tam-nen-nguoi-trinh-bay.png')
    tam_nen(sys.argv[1], nen)
    for i in range(2, len(sys.argv) - 1, 2):
        chen(nen, sys.argv[i], sys.argv[i + 1])
