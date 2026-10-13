# -*- coding: utf-8 -*-
"""Tạo nhạc nền không lời (tự tổng hợp bằng máy, không dùng bản nhạc có bản quyền) rồi trộn nhỏ dưới giọng đọc của video.
Nhạc: Tiếng đệm êm theo vòng hợp âm chậm (Đô trưởng - La thứ - Fa trưởng - Sol trưởng), thêm nốt rải nhẹ; lặp liền mạch.
Cách dùng: python nhac_nen.py <video vào> <video ra> [âm lượng nhạc, mặc định 0.06] [tệp nhạc riêng]"""
import os, subprocess, sys, wave
import numpy as np
import imageio_ffmpeg
sys.stdout.reconfigure(encoding='utf-8')
FF = imageio_ffmpeg.get_ffmpeg_exe()
SR, NHIP = 44100, 6.0   # mỗi hợp âm 6 giây


def tan_so(n):   # số nốt MIDI -> Hz
    return 440.0 * 2 ** ((n - 69) / 12)


def tao_nhac(tep):
    hop_am = [[48, 55, 60, 64, 67], [45, 52, 57, 60, 64], [41, 48, 53, 57, 60], [43, 50, 55, 59, 62],
              [48, 55, 60, 64, 67], [45, 52, 57, 60, 64], [41, 48, 53, 57, 65], [43, 50, 55, 59, 67]]
    N = int(SR * NHIP); tong = N * len(hop_am)
    trai, phai = np.zeros(tong + N), np.zeros(tong + N)
    t = np.arange(2 * N) / SR
    bao = np.clip(t / 2.5, 0, 1) * np.clip((2 * NHIP - t) / 5.0, 0, 1)        # vào chậm, tan chậm, gối sang hợp âm sau
    for k, ha in enumerate(hop_am):
        d = np.zeros(2 * N)
        for j, n in enumerate(ha):
            f = tan_so(n)
            d += (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t + 0.5) + 0.12 * np.sin(2 * np.pi * 3 * f * t)) * (0.9 if j else 1.2)
            d += 0.5 * np.sin(2 * np.pi * f * 1.004 * t)                          # lệch nhẹ cho tiếng dày
        d *= bao
        a, b = k * N, k * N + 2 * N
        doan = d[:min(b, tong + N) - a]
        trai[a:a + len(doan)] += doan; phai[a:a + len(doan)] += doan
        for i, n in enumerate([ha[2] + 12, ha[3] + 12, ha[4] + 12, ha[3] + 12]):  # 4 nốt rải nhẹ mỗi hợp âm
            tn = np.arange(int(SR * 2.4)) / SR
            not_ = np.sin(2 * np.pi * tan_so(n) * tn) * np.exp(-tn * 2.2) * np.clip(tn / 0.02, 0, 1) * 1.6
            vt = a + int(SR * (0.4 + i * 1.5))
            lech = 0.35 + 0.3 * (i % 2)
            trai[vt:vt + len(not_)] += not_[:len(trai[vt:vt + len(not_)])] * (1 - lech)
            phai[vt:vt + len(not_)] += not_[:len(phai[vt:vt + len(not_)])] * lech
    for x in (trai, phai):   # phần tràn cuối gập về đầu để lặp không có vết nối
        x[:N] += x[tong:tong + N]
    am = np.stack([trai[:tong], phai[:tong]], axis=1)
    am = am / np.abs(am).max() * 0.8
    with wave.open(tep, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((am * 32767).astype(np.int16).tobytes())


def tron(vao, ra, muc=0.06, nhac_ngoai=None):
    """nhac_ngoai: Tệp nhạc không lời do người dùng cung cấp (dùng thay nhạc tự tổng hợp); muc khi đó là hệ số âm lượng của tệp ấy."""
    nhac = nhac_ngoai or os.path.join(os.path.dirname(os.path.abspath(ra)), '_nhac-nen.wav')
    if not nhac_ngoai:
        tao_nhac(nhac)
    r = subprocess.run([FF, '-i', vao], capture_output=True, text=True, encoding='utf-8', errors='ignore').stderr
    h, m, s = next(x for x in r.splitlines() if 'Duration' in x).split('Duration:')[1].split(',')[0].strip().split(':')
    T = int(h) * 3600 + int(m) * 60 + float(s)
    logo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo-truong.png')   # logo Trường, góc trên trái
    co_logo = os.path.exists(logo)
    loc = (f"[1:a]volume={muc},lowpass=f=3500,afade=t=in:d=3,afade=t=out:st={T - 4:.2f}:d=4[n];"
           f"[0:a][n]amix=inputs=2:duration=first:normalize=0[a]" + (";[0:v][2:v]overlay=10:8[v]" if co_logo else ''))
    hinh = (['-map', '[v]', '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p'] if co_logo else ['-map', '0:v', '-c:v', 'copy'])
    subprocess.run([FF, '-y', '-loglevel', 'error', '-i', vao, '-stream_loop', '-1', '-i', nhac] + (['-i', logo] if co_logo else [])
                   + ['-filter_complex', loc] + hinh + ['-map', '[a]', '-c:a', 'aac', '-b:a', '192k', '-t', f'{T:.2f}', ra], check=True)
    if not nhac_ngoai:
        os.remove(nhac)
    print('→', ra)


if __name__ == '__main__':
    tron(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 0.06, sys.argv[4] if len(sys.argv) > 4 else None)
