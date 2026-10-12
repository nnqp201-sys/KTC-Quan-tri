# -*- coding: utf-8 -*-
"""Ghép đoạn quay màn hình với giọng thuyết minh và dòng chú thích -> video thao tác hoàn chỉnh.
Cách dùng: đặt tệp quay vào thư mục quay/ với tên T1.mp4, T2.mp4, T3.mp4, T4.mp4 (hoặc .mkv, .mov) rồi chạy:  python ghep_video.py
Kết quả: xuat/T1_...mp4 …  Video ngắn hơn lời đọc thì giữ khung hình cuối đến hết lời; dài hơn thì giữ tối đa 45 giây.
Tiếng gốc của đoạn quay bị bỏ. Khung hình đưa về 1920x1080."""
import glob, os, subprocess, sys
import imageio_ffmpeg
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
FF = imageio_ffmpeg.get_ffmpeg_exe()
CHU = 'Dữ liệu giả định phục vụ trình diễn'


def do_dai(tep):
    r = subprocess.run([FF, '-i', tep], capture_output=True, text=True, encoding='utf-8', errors='ignore').stderr
    h, m, s = next(x for x in r.splitlines() if 'Duration' in x).split('Duration:')[1].split(',')[0].strip().split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


def main():
    os.makedirs(os.path.join(D, 'xuat'), exist_ok=True)
    chu = os.path.join(D, 'xuat', '_chu.txt'); open(chu, 'w', encoding='utf-8').write(CHU)
    n = 0
    for mp3 in sorted(glob.glob(os.path.join(D, 'T?_*.mp3'))):
        ma = os.path.basename(mp3)[:2]
        quay = [x for x in glob.glob(os.path.join(D, 'quay', ma + '.*')) if x.lower().endswith(('.mp4', '.mkv', '.mov', '.webm'))]
        if not quay:
            print(f'{ma}: chưa có tệp quay (quay/{ma}.mp4) — bỏ qua'); continue
        loi = do_dai(mp3)
        dai = max(loi + 1.0, min(do_dai(quay[0]), 45.0))   # đủ lời đọc; đoạn quay dài thì giữ tối đa 45 giây
        ra = os.path.join(D, 'xuat', os.path.basename(mp3)[:-4] + '.mp4')
        loc = ("[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white,"
               "tpad=stop_mode=clone:stop_duration=120,"
               r"drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':textfile='_chu.txt':fontsize=30:fontcolor=white:"
               "box=1:boxcolor=black@0.55:boxborderw=12:x=w-tw-40:y=h-th-36[v]")
        subprocess.run([FF, '-y', '-loglevel', 'error', '-i', quay[0], '-i', mp3, '-filter_complex', loc, '-map', '[v]', '-map', '1:a',
                        '-af', 'apad=pad_dur=1', '-t', f'{dai:.2f}', '-r', '25', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', ra],
                       check=True, cwd=os.path.join(D, 'xuat'))
        print(f'{ma}: quay {do_dai(quay[0]):.0f} giây, lời đọc {loi:.0f} giây -> {os.path.basename(ra)} ({do_dai(ra):.0f} giây)'); n += 1
    print(f'Đã ghép {n} đoạn. Chiếu thử trước khi dùng.')


if __name__ == '__main__':
    main()
