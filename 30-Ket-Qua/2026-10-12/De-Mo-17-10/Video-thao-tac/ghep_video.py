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
# Phần tử thứ tư (nếu có): Tỷ lệ chiều rộng bên trái cần làm mờ. Bản 13/10/2026 (lần 2): Không làm mờ (người dùng cho phép
# hiện địa chỉ thư); thêm lại đoạn trỏ thư mục và ảnh tệp kết quả (anh_kq/); tốc độ đặt cho hình khớp lời thuyết minh.
CAT = {
    'T1': [[12.0, 22.0, 2.5], [34.0, 46.0, 2.5], [48.5, 93.0, 6.0], [93.0, 126.8, 2.0]],  # trỏ 2 thư mục -> gõ lệnh -> làm việc
    'T2': [[8.0, 18.0, 2.0], [26.0, 85.4, 2.1]],                          # trỏ thư mục D2 -> dán lệnh -> đọc tệp
    'T3': [[6.0, 15.0, 1.8], [19.0, 62.0, 1.45]],                         # trỏ thư mục D3 -> dán lệnh -> làm việc
    'T4': [[6.0, 12.0, 1.5], [26.0, 88.2, 2.7]],                          # trỏ thư mục D4 -> gọi kỹ năng rà soát -> làm việc
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
        anh = sorted(glob.glob(os.path.join(D, 'anh_kq', ma + '_*.png')), key=lambda x: (len(x), x))
        # Ảnh có tệp lời riêng (cùng tên .mp3): Hiện đúng hết lời, cuộn dọc nếu ảnh cao hơn khung; ảnh không có lời: GIAY_ANH giây.
        loi_anh = [x[:-4] + '.mp3' if os.path.exists(x[:-4] + '.mp3') else None for x in anh]
        t_anh = [do_dai(m) + 0.6 if m else GIAY_ANH for m in loi_anh]
        hinh = sum((x[1] - x[0]) / x[2] for x in doan)
        if any(loi_anh):
            hinh = max(hinh, loi + 0.5)   # lời chính đọc hết trước khi sang ảnh kết quả
        dai = max(loi + 1.0, hinh + sum(t_anh))
        ra = os.path.join(D, 'xuat', os.path.basename(mp3)[:-4] + '.mp4')
        chuan = "fps=25,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white,setsar=1"
        cat = ''
        for k, x in enumerate(doan):
            a, b, v = x[:3]
            cat += f"[0:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)/{v},{chuan}"
            cat += (f",split[g{k}][h{k}];[h{k}]crop=iw*{x[3]}:ih:0:0,boxblur=30:5[m{k}];[g{k}][m{k}]overlay=0:0[s{k}];" if len(x) > 3 and x[3] else f"[s{k}];")
        # Lời dài hơn hình: Giữ khung cuối của ảnh kết quả (tpad ở cuối chuỗi lọc).
        hq = sum((x[1] - x[0]) / x[2] for x in doan)
        cat += ''.join(f'[s{k}]' for k in range(len(doan))) + f'concat=n={len(doan)}:v=1:a=0,tpad=stop_mode=clone:stop_duration={max(hinh - hq, 0):.2f}[q];'
        for j, t in enumerate(t_anh):
            if loi_anh[j]:
                cat += (f"[{j + 2}:v]fps=25,scale=1920:-2,crop=1920:1080:0:'(ih-1080)*min(t/{t:.2f},1)',setsar=1,trim=duration={t:.2f}[r{j}];")
            else:
                cat += f"[{j + 2}:v]{chuan},trim=duration={t:.2f}[r{j}];"
        noi = '[q]' + ''.join(f'[r{j}]' for j in range(len(anh))) + f'concat=n={len(anh) + 1}:v=1:a=0[c];'
        loc = (cat + noi + "[c]tpad=stop_mode=clone:stop_duration=60,"
               r"drawtext=fontfile='C\:/Windows/Fonts/arial.ttf':textfile='_chu.txt':fontsize=30:fontcolor=white:"
               "box=1:boxcolor=black@0.55:boxborderw=12:x=w-tw-40:y=h-th-36[v]")
        vao = sum((['-loop', '1', '-framerate', '25', '-t', f'{t:.2f}', '-i', x] for x, t in zip(anh, t_anh)), [])
        am, so = '', 0
        if any(loi_anh):   # ghép tiếng: lời chính đệm tới hết phần quay, rồi lời từng ảnh đệm đúng thời lượng ảnh
            am = f"[1:a]apad=whole_dur={hinh:.2f}[a0];"
            vt = len(anh) + 2
            for j, m in enumerate(loi_anh):
                so += 1
                if m:
                    vao += ['-i', m]; am += f"[{vt}:a]apad=whole_dur={t_anh[j]:.2f}[a{so}];"; vt += 1
                else:
                    am += f"anullsrc=r=24000:cl=mono,atrim=duration={t_anh[j]:.2f}[a{so}];"
            am += ''.join(f'[a{k}]' for k in range(so + 1)) + f'concat=n={so + 1}:v=0:a=1,apad=pad_dur=200[am];'
        subprocess.run([FF, '-y', '-loglevel', 'error', '-i', quay[0], '-i', mp3] + vao + ['-filter_complex', am + loc, '-map', '[v]', '-map', '[am]' if am else '1:a']
                       + ([] if am else ['-af', 'apad=pad_dur=200']) + ['-t', f'{dai:.2f}', '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', ra],
                       check=True, cwd=os.path.join(D, 'xuat'))
        print(f'{ma}: giữ {len(doan)} đoạn = {hinh:.0f} giây hình, lời đọc {loi:.0f} giây -> {os.path.basename(ra)} ({do_dai(ra):.0f} giây)'); n += 1
    print(f'Đã ghép {n} đoạn. Chiếu thử trước khi dùng.')


if __name__ == '__main__':
    main()
