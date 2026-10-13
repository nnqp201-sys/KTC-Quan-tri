# -*- coding: utf-8 -*-
"""Chèn hình người trình bày (khung tròn nhỏ) kèm dải sóng âm chạy theo giọng đọc vào video đã ghép; vị trí đổi theo phân cảnh
để không che nội dung.
Cách dùng: python chen_hinh.py <ảnh chân dung> <kiểu> <video vào> <video ra> [<kiểu> <video vào> <video ra> …]
  kiểu = số giây (ví dụ 33.5): Video thao tác — trước mốc đó hình ở góc dưới trái (trên thanh bên của Cowork), từ mốc đó
         (phần chiếu trang kết quả) hình ở cột trắng bên phải, phía trên. Mốc lấy từ xuat/moc.json do ghep_video.py ghi.
  kiểu = tieu-de: Video 1 — chỉ khung tròn, đặt trong thanh tiêu đề, góc trên phải.
Ảnh chân dung là ảnh cá nhân: KHÔNG đưa vào git; để ở thư mục trình diễn ngoài dự án."""
import os, subprocess, sys
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding='utf-8')
FF = imageio_ffmpeg.get_ffmpeg_exe()
TEN, DV = 'Nguyễn Ngọc Quang Phục', 'Phòng TH-HC&QT'
KHUNG_MAT = (105, 15, 365, 275)   # vùng khuôn mặt trong ảnh Chan-dung-Phuc.png (449x451)


def tam_nen(anh, ra, co_ten):
    """Tấm nền: Có tên (220x232, ảnh tròn 130) hoặc chỉ ảnh tròn (150x170, ảnh tròn 116). Trả (rộng, cao, y sóng âm, rộng sóng)."""
    k = 3  # vẽ gấp 3 rồi thu lại cho mịn
    RONG, CAO, R = (220, 232, 130) if co_ten else (150, 170, 116)
    n = Image.new('RGBA', (RONG * k, CAO * k), (0, 0, 0, 0))
    d = ImageDraw.Draw(n)
    d.rounded_rectangle([0, 0, RONG * k - 1, CAO * k - 1], radius=20 * k, fill=(13, 59, 102, 225 if co_ten else 0))
    m = Image.open(anh).convert('RGB').crop(KHUNG_MAT).resize((R * k, R * k), Image.LANCZOS)
    mat = Image.new('L', (R * k, R * k), 0); ImageDraw.Draw(mat).ellipse([0, 0, R * k - 1, R * k - 1], fill=255)
    x0, y0 = (RONG - R) // 2 * k, 10 * k
    d.ellipse([x0 - 4 * k, y0 - 4 * k, x0 + R * k + 4 * k, y0 + R * k + 4 * k], fill=(255, 255, 255, 255))
    n.paste(m, (x0, y0), mat)
    if co_ten:
        f1, f2 = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 15 * k), ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 14 * k)
        for chu, f, y in ((TEN, f1, 150), (DV, f2, 171)):
            w = d.textlength(chu, font=f); d.text(((RONG * k - w) / 2, y * k), chu, font=f, fill='white')
    n.resize((RONG, CAO), Image.LANCZOS).save(ra)
    return RONG, CAO, (196 if co_ten else 136), RONG - 30


def chen(anh, kieu, vao, ra):
    nen = os.path.join(os.path.dirname(os.path.abspath(anh)), '_tam-nen-nguoi-trinh-bay.png')
    rong, cao, yw, rw = tam_nen(anh, nen, kieu != 'tieu-de')
    if kieu == 'tieu-de':
        x, y = f'W-{rong}-24', '10'
    else:   # trước mốc: Góc dưới trái; từ mốc: Cột trắng bên phải (rộng 260), phía trên
        x, y = f"if(lt(t,{kieu}),24,W-240)", f"if(lt(t,{kieu}),H-{cao}-70,40)"
    loc = (f"[0:a]asplit[a1][a2];[a1]showwaves=s={rw}x28:mode=cline:rate=25:colors=0xFFD54A:scale=sqrt,format=rgba[w];"
           f"[1:v]format=rgba[n];[n][w]overlay=15:{yw}:shortest=1[p];[0:v][p]overlay=x='{x}':y='{y}':shortest=1[v]")
    subprocess.run([FF, '-y', '-loglevel', 'error', '-i', vao, '-loop', '1', '-framerate', '25', '-i', nen, '-filter_complex', loc,
                    '-map', '[v]', '-map', '[a2]', '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', ra], check=True)
    print('→', ra)


if __name__ == '__main__':
    for i in range(2, len(sys.argv) - 2, 3):
        chen(sys.argv[1], sys.argv[i], sys.argv[i + 1], sys.argv[i + 2])
