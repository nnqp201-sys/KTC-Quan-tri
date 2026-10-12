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


# Đoạn giữ lại của từng tệp quay: [bắt đầu (giây), kết thúc (giây), tốc độ]. Không khai thì lấy từ đầu, tối đa 45 giây.
# Bản quay ngày 12/10/2026: Bỏ hộp thoại chọn thư mục (lộ tên tài khoản, thư mục cá nhân), bỏ cửa sổ Word hướng dẫn,
# bỏ đoạn mở trình đơn ở cuối; tua nhanh đoạn gõ phím.
CAT = {
    'T1': [[48.5, 93.0, 4.0], [93.0, 126.8, 1.0]],     # gõ lệnh (tua 4 lần) -> công cụ làm việc
    'T2': [[26.0, 85.4, 1.4]],                          # dán lệnh -> công cụ đọc tệp D2
    'T3': [[19.0, 62.0, 1.0]],                          # dán lệnh -> công cụ làm việc
    'T4': [[26.0, 88.2, 1.45]],                         # dán lệnh, gọi kỹ năng rà soát -> công cụ làm việc
}


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
        doan = CAT.get(ma) or [[0.0, min(do_dai(quay[0]), 45.0), 1.0]]
        hinh = sum((b - a) / v for a, b, v in doan)
        dai = max(loi + 1.0, hinh)
        ra = os.path.join(D, 'xuat', os.path.basename(mp3)[:-4] + '.mp4')
        cat = ''.join(f"[0:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{v}[s{k}];" for k, (a, b, v) in enumerate(doan))
        noi = ''.join(f'[s{k}]' for k in range(len(doan))) + f'concat=n={len(doan)}:v=1:a=0[c];'
        loc = (cat + noi + "[c]fps=25,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white,"
               "tpad=stop_mode=clone:stop_duration=120,"
               r"drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':textfile='_chu.txt':fontsize=30:fontcolor=white:"
               "box=1:boxcolor=black@0.55:boxborderw=12:x=w-tw-40:y=h-th-36[v]")
        subprocess.run([FF, '-y', '-loglevel', 'error', '-i', quay[0], '-i', mp3, '-filter_complex', loc, '-map', '[v]', '-map', '1:a',
                        '-af', 'apad=pad_dur=120', '-t', f'{dai:.2f}', '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', ra],
                       check=True, cwd=os.path.join(D, 'xuat'))
        print(f'{ma}: giữ {len(doan)} đoạn = {hinh:.0f} giây hình, lời đọc {loi:.0f} giây -> {os.path.basename(ra)} ({do_dai(ra):.0f} giây)'); n += 1
    print(f'Đã ghép {n} đoạn. Chiếu thử trước khi dùng.')


if __name__ == '__main__':
    main()
