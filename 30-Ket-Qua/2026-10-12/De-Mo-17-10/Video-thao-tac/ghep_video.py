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
# Phần tử thứ tư: Tỷ lệ chiều rộng bên trái cần làm mờ khung hình (khung điều hướng của hộp thoại chọn thư mục có tên tài khoản Drive).
# Bản 13/10/2026: Thêm lại đoạn trỏ thư mục trong D:\.00. DE MO 17-10 (đã làm mờ) và nối ảnh tệp kết quả (anh_kq/, do anh_ket_qua.py tạo).
CAT = {
    'T1': [[12.0, 22.0, 1.6, 0.22], [34.0, 46.0, 1.6, 0.22], [48.5, 93.0, 4.0], [93.0, 126.8, 1.0]],  # trỏ 2 thư mục -> gõ lệnh -> làm việc
    'T2': [[8.0, 18.0, 1.4, 0.34], [26.0, 85.4, 1.4]],                         # trỏ thư mục D2 -> dán lệnh -> đọc tệp
    'T3': [[6.0, 15.0, 1.3, 0.34], [19.0, 62.0, 1.0]],                         # trỏ thư mục D3 -> dán lệnh -> làm việc
    'T4': [[6.0, 12.0, 1.0, 0.34], [26.0, 88.2, 1.45]],                        # trỏ thư mục D4 -> gọi kỹ năng rà soát -> làm việc
}
GIAY_ANH = 6.0   # mỗi ảnh kết quả hiện 6 giây


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
        anh = sorted(glob.glob(os.path.join(D, 'anh_kq', ma + '_*.png')))
        hinh = sum((x[1] - x[0]) / x[2] for x in doan)
        dai = max(loi + 1.0, hinh) + GIAY_ANH * len(anh)
        ra = os.path.join(D, 'xuat', os.path.basename(mp3)[:-4] + '.mp4')
        chuan = "fps=25,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white,setsar=1"
        cat = ''
        for k, x in enumerate(doan):
            a, b, v = x[:3]
            cat += f"[0:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{v},{chuan}"
            cat += (f",split[g{k}][h{k}];[h{k}]crop=iw*{x[3]}:ih:0:0,boxblur=30:5[m{k}];[g{k}][m{k}]overlay=0:0[s{k}];" if len(x) > 3 and x[3] else f"[s{k}];")
        # Đoạn quay ngắn hơn lời đọc: Giữ khung hình cuối cho hết lời, rồi mới tới ảnh kết quả.
        thua = max(loi + 1.0 - hinh, 0)
        cat += ''.join(f'[s{k}]' for k in range(len(doan))) + f'concat=n={len(doan)}:v=1:a=0,tpad=stop_mode=clone:stop_duration={thua:.2f}[q];'
        cat += ''.join(f"[{j + 2}:v]{chuan},trim=duration={GIAY_ANH}[r{j}];" for j in range(len(anh)))
        noi = '[q]' + ''.join(f'[r{j}]' for j in range(len(anh))) + f'concat=n={len(anh) + 1}:v=1:a=0[c];'
        loc = (cat + noi + "[c]tpad=stop_mode=clone:stop_duration=5,"
               r"drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':textfile='_chu.txt':fontsize=30:fontcolor=white:"
               "box=1:boxcolor=black@0.55:boxborderw=12:x=w-tw-40:y=h-th-36[v]")
        vao = sum((['-loop', '1', '-framerate', '25', '-t', str(GIAY_ANH), '-i', x] for x in anh), [])
        subprocess.run([FF, '-y', '-loglevel', 'error', '-i', quay[0], '-i', mp3] + vao + ['-filter_complex', loc, '-map', '[v]', '-map', '1:a',
                        '-af', 'apad=pad_dur=200', '-t', f'{dai:.2f}', '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', ra],
                       check=True, cwd=os.path.join(D, 'xuat'))
        print(f'{ma}: giữ {len(doan)} đoạn = {hinh:.0f} giây hình, lời đọc {loi:.0f} giây -> {os.path.basename(ra)} ({do_dai(ra):.0f} giây)'); n += 1
    print(f'Đã ghép {n} đoạn. Chiếu thử trước khi dùng.')


if __name__ == '__main__':
    main()
