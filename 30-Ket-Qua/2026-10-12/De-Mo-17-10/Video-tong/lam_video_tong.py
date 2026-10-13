# -*- coding: utf-8 -*-
"""Dựng MỘT video hoàn chỉnh cho buổi trình diễn 17/10/2026: Trang trình chiếu có lời đọc, Video 1, 04 video thao tác,
thẻ chuyển phần (giọng nam), các đoạn hỏi - đáp (nam hỏi, nữ đáp). Mỗi cảnh mờ dần vào, mờ dần ra.
Cách dùng: python lam_video_tong.py <thư mục BAN-TRINH-DIEN-17-10> [thư mục tạm]
Kết quả: <thư mục BAN-TRINH-DIEN-17-10>/A_VIDEO-TOAN-BO_Trinh-dien-AI_17.10.2026.mp4
Giọng: Microsoft Edge TTS — nữ vi-VN-HoaiMyNeural, nam vi-VN-NamMinhNeural (lời đọc gửi lên máy chủ Microsoft: Chỉ nội dung công khai)."""
import asyncio, hashlib, os, subprocess, sys, time
import edge_tts, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.abspath(sys.argv[1])
TAM = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(BAN, '..', 'Video-tong', '_tam')
os.makedirs(TAM, exist_ok=True)
TRANG = os.path.join(D, '..', 'Trinh-chieu', 'trang')
FF = imageio_ffmpeg.get_ffmpeg_exe()
GIONG = {'nu': ('vi-VN-HoaiMyNeural', '-4%'), 'nam': ('vi-VN-NamMinhNeural', '+0%')}
XANH, VANG, NHAT = (13, 59, 102), (255, 213, 74), (232, 240, 249)
F = lambda c, dam=False: ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf' if dam else 'C:/Windows/Fonts/arial.ttf', c)
MA = '-c:v libx264 -crf 20 -pix_fmt yuv420p -r 25 -c:a aac -b:a 160k -ar 44100 -ac 2'.split()
MO = 0.4   # giây mờ dần đầu, cuối mỗi cảnh

# ---- KỊCH BẢN: ('the', nhãn, tiêu đề, phụ đề, lời) · ('trang', số trang, lời) · ('video', tên tệp trong BAN) · ('hoi', câu hỏi, câu đáp)
# lời = [(giọng, câu đọc), …]
KB = [
 ('the', '17/10/2026', 'Ứng dụng trí tuệ nhân tạo trong công tác tham mưu, tổng hợp', 'Trường Cao đẳng Kon Tum  ·  Phòng Tổng hợp - Hành chính và Quản trị',
  [('nam', 'Kính thưa các đồng chí. Đây là phần trình bày của Phòng Tổng hợp, Hành chính và Quản trị, Trường Cao đẳng Kon Tum, về ứng dụng trí tuệ nhân tạo trong công tác tham mưu, tổng hợp.'),
   ('nu', 'Toàn bộ dữ liệu trong phần trình diễn là dữ liệu giả định; văn bản đưa ra rà soát đã được ẩn danh.')]),
 ('trang', 1, [('nu', 'Phần trình bày gồm ba nội dung, theo đề nghị của Đoàn công tác. Một, quản lý, theo dõi, đôn đốc nhiệm vụ, qua việc tổng hợp kế hoạch công tác quý. '
                      'Hai, tổng hợp số liệu, xây dựng báo cáo tháng. Ba, soạn thảo và rà soát văn bản.')]),
 ('trang', 2, [('nam', 'Trước khi vào từng phần, xin nêu ba nguyên tắc sử dụng.'),
               ('nu', 'Thứ nhất, công cụ chỉ đọc, đối chiếu và dự thảo; người có thẩm quyền mới là người quyết định. Thứ hai, mọi kết quả phải truy được về văn bản nguồn, dữ liệu nguồn. '
                      'Thứ ba, không đưa tài liệu thuộc bí mật nhà nước vào công cụ.'),
               ('nam', 'Tóm lại là: nền móng trước, công cụ sau.')]),
 ('the', 'GIỚI THIỆU', 'Ba hệ hỗ trợ đang dùng tại Trường', 'Kho dữ liệu nền  ·  Hệ rà soát văn bản  ·  Bộ công cụ quản trị nhiệm vụ',
  [('nam', 'Tiếp theo, xin giới thiệu nhanh ba hệ hỗ trợ đang dùng tại Trường.')]),
 ('video', '02_Video-1_Gioi-thieu-03-he.mp4'),
 ('the', 'PHẦN 1', 'Tổng hợp kế hoạch công tác quý từ dự thảo của các đơn vị', 'Quản lý, theo dõi, đôn đốc nhiệm vụ',
  [('nam', 'Phần một: tổng hợp kế hoạch công tác quý từ dự thảo của các đơn vị.')]),
 ('trang', 3, [('nu', 'Tình huống giả định: bộ phận tổng hợp nhận dự thảo kế hoạch quý bốn của sáu đơn vị, sáu mươi nhiệm vụ, trong sáu tệp bảng tính. '
                      'Trong đó đã cài sẵn các lỗi thường gặp: một đơn vị nộp nhầm mẫu, một số nhiệm vụ thiếu thời hạn hoặc sản phẩm, có nhiệm vụ trùng giữa các đơn vị. '
                      'Mời các đồng chí xem công cụ xử lý.')]),
 ('video', '10_Video-T1_Tong-hop-ke-hoach.mp4'),
 ('hoi', 'Công cụ dựng bảng nhanh như vậy, có cần kiểm tra lại không?',
         'Có. Ngay trong lượt chạy vừa xem, sáu dòng của bảng tính bị mất dữ liệu. Vì vậy, bảng do công cụ dựng luôn phải được người tổng hợp kiểm tra trước khi trình.'),
 ('hoi', 'Công cụ có tự sửa nội dung của đơn vị không?',
         'Không. Công cụ chỉ ghi chú và đề xuất, ví dụ đề xuất thời hạn theo công văn của cấp trên. Việc sửa và quyết định thuộc về đơn vị và người tổng hợp.'),
 ('trang', 4, [('nam', 'Tiếp theo là tra cứu hệ thống quản lý văn bản và điều hành.'),
               ('nu', 'Công cụ lấy danh mục văn bản chỉ đạo, kế hoạch, thông báo kết luận trong kỳ, đối chiếu với dự thảo kế hoạch để chỉ ra việc đã giao mà chưa ai nhận. '
                      'Công cụ chỉ đọc trong phiên người dùng đã đăng nhập; không nhập mật khẩu, không bấm nút xử lý.')]),
 ('video', '13_Video-T2_Doi-chieu-van-ban-chi-dao.mp4'),
 ('hoi', 'Nếu chỉ đưa cho công cụ danh mục văn bản, không đưa dự thảo kế hoạch thì sao?',
         'Chúng tôi đã thử. Khi thiếu dự thảo kế hoạch, công cụ nêu tới chín việc chưa ai nhận, trong khi thực tế chỉ có hai. Bài học là: người dùng phải đưa đủ hồ sơ.'),
 ('the', 'PHẦN 2', 'Xây dựng báo cáo tháng từ báo cáo của các đơn vị', 'Tổng hợp số liệu, đối chiếu kế hoạch với kết quả',
  [('nam', 'Phần hai: xây dựng báo cáo tháng từ báo cáo của các đơn vị.')]),
 ('trang', 5, [('nu', 'Tình huống: báo cáo tháng chín của sáu đơn vị, kế hoạch tháng có hai mươi bốn nhiệm vụ, và báo cáo tháng tám đã ban hành. '
                      'Hai mươi mốt nhiệm vụ có báo cáo, ba nhiệm vụ chưa có thông tin. Có một số liệu không thống nhất giữa hai đơn vị, và một kết quả được hai đơn vị cùng nhận.')]),
 ('video', '20_Video-T3_Bao-cao-thang.mp4'),
 ('hoi', 'Nhiệm vụ không thấy trong báo cáo, công cụ kết luận thế nào?',
         'Công cụ ghi là chưa có thông tin, không tự kết luận là chưa làm. Nếu đưa thêm danh mục văn bản đã ban hành, công cụ còn tìm được quyết định làm minh chứng cho việc đơn vị quên báo cáo.'),
 ('hoi', 'Lượt chạy này còn bỏ sót gì không?',
         'Có. Công cụ chưa nhận ra hai đơn vị cùng báo cáo một kết quả. Lượt chạy đầy đủ, có thêm dữ liệu đối chiếu, mới bắt được điểm này.'),
 ('the', 'PHẦN 3', 'Soạn thảo, rà soát văn bản trước khi trình ký', 'Hệ rà soát dùng chung KTC-Ra-Soat-897',
  [('nam', 'Phần ba: soạn thảo và rà soát văn bản trước khi trình ký.')]),
 ('trang', 8, [('nu', 'Trước hết là vài kinh nghiệm thực tế tại phòng. Thông báo kết luận được ráp ngay khi cuộc họp đang diễn ra. '
                      'Một quyết định đi từ tra cứu đến khi ký khoảng mười ngày, và chính người có nghiệp vụ đã bắt được hai lỗi căn cứ của công cụ. '
                      'Có đợt sửa một trăm ba mươi hai vị trí trong bốn văn bản, đều để lại dấu vết cho người duyệt xem từng chỗ.')]),
 ('trang', 6, [('nam', 'Bây giờ là rà soát văn bản trước khi trình ký.'),
               ('nu', 'Văn bản đưa vào rà soát là một dự thảo văn bản của Đảng, đã đổi tên cơ quan để ẩn danh. Công cụ tự nhận ra đây là văn bản của Đảng, '
                      'nên áp Hướng dẫn số 05 của Văn phòng Trung ương, không áp Nghị định 30.')]),
 ('video', '30_Video-T4_Ra-soat-van-ban-Dang.mp4'),
 ('hoi', 'Cùng một văn bản, mỗi lần rà soát có cho kết quả như nhau không?',
         'Không hẳn. Lượt chạy nhanh vừa xem nêu sáu phát hiện, trong đó một phát hiện sai. Lượt rà soát đầy đủ nêu hai mươi lăm phát hiện. '
         'Vì vậy, rà soát chính thức phải chạy đủ quy trình và luôn có người kiểm tra.'),
 ('trang', 7, [('nu', 'Bộ công cụ công khai cả giới hạn của mình. Kiểm thử định kỳ trên tệp cài sẵn ba mươi lỗi: phát hiện đúng hai mươi bốn, sai mức hai, bỏ sót bốn. '
                      'Ô người kiểm tra luôn là người thật; công cụ không tự phê duyệt.'),
               ('nam', 'Và còn vấn đề mức một thì không trình ký.')]),
 ('the', 'KẾT THÚC', 'Đề xuất để bắt đầu', 'Bắt đầu nhỏ  ·  Làm thật  ·  Có người kiểm tra',
  [('nam', 'Phần cuối: đề xuất để bắt đầu.')]),
 ('trang', 9, [('nu', 'Thứ nhất, lập kho dữ liệu nền trước: văn bản chỉ đạo còn hiệu lực, quy chế, chương trình công tác, văn bản tốt, mẫu văn bản của Đảng. '
                      'Thứ hai, chọn một đến hai việc lặp lại hằng tháng để làm trước. Thứ ba, quy định rõ loại dữ liệu không đưa vào công cụ, và ai là người kiểm tra.'),
               ('nam', 'Bắt đầu nhỏ, làm thật, có người kiểm tra.')]),
 ('trang', 10, [('nam', 'Trường Cao đẳng Kon Tum sẵn sàng chia sẻ, hỗ trợ mọi công cụ khi nhận được:'),
                ('nu', 'Một, thông tin, dữ liệu đầu vào: nghị quyết, quy định, quy chế, chương trình, kế hoạch, quy trình. '
                       'Hai, yêu cầu sản phẩm đầu ra: biểu mẫu, dữ liệu, thể thức, sản phẩm tốt đã có. '
                       'Ba, phần xử lý về kỹ thuật, công cụ, phương pháp: đã có trí tuệ nhân tạo và con người hỗ trợ.')]),
 ('trang', 11, [('nam', 'Xin trân trọng cảm ơn các đồng chí đã theo dõi.'),
                ('nu', 'Ở phần thảo luận, Đoàn công tác có thể đề nghị chạy trực tiếp một thao tác.')]),
]


def do_dai(tep):
    r = subprocess.run([FF, '-i', tep], capture_output=True, text=True, encoding='utf-8', errors='ignore').stderr
    h, m, s = next(x for x in r.splitlines() if 'Duration' in x).split('Duration:')[1].split(',')[0].strip().split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


def doc(giong, loi):
    tep = os.path.join(TAM, 'loi_' + hashlib.md5((giong + loi).encode('utf-8')).hexdigest()[:12] + '.mp3')
    if os.path.exists(tep) and os.path.getsize(tep) > 1000:
        return tep
    ten, toc = GIONG[giong]
    for lan in range(10):   # dịch vụ đôi khi không trả âm thanh
        try:
            asyncio.run(edge_tts.Communicate(loi, ten, rate=toc).save(tep)); return tep
        except Exception as e:
            print('   thử lại giọng đọc', lan + 1, type(e).__name__); time.sleep(3)
    raise SystemExit('Không tạo được giọng đọc')


def ngat(d, chu, font, rong):
    dong, hien = [], ''
    for tu in chu.split():
        if d.textlength((hien + ' ' + tu).strip(), font=font) <= rong:
            hien = (hien + ' ' + tu).strip()
        else:
            dong.append(hien); hien = tu
    return dong + [hien]


def the(nhan, td, phu, tep):
    a = Image.new('RGB', (1920, 1080), XANH); d = ImageDraw.Draw(a)
    for i in range(1080):   # nền chuyển sắc nhẹ
        d.line([(0, i), (1920, i)], fill=(13 + i // 60, 59 + i // 40, 102 + i // 22))
    d.rectangle([150, 330, 162, 760], fill=VANG)
    d.text((200, 330), nhan, font=F(52, True), fill=VANG)
    y = 420
    for x in ngat(d, td, F(78, True), 1500):
        d.text((200, y), x, font=F(78, True), fill='white'); y += 100
    d.text((200, y + 30), phu, font=F(40), fill=(205, 222, 240))
    a.save(tep)


def the_hoi(hoi, dap, tep):
    a = Image.new('RGB', (1920, 1080), 'white'); d = ImageDraw.Draw(a)
    d.rectangle([0, 0, 1920, 150], fill=XANH); d.text((90, 42), 'Hỏi - đáp', font=F(64, True), fill='white')
    d.rounded_rectangle([90, 220, 1500, 220 + 70 + 70 * len(ngat(d, hoi, F(50, True), 1180))], radius=30, fill=NHAT)
    d.ellipse([120, 245, 230, 355], fill=XANH); d.text((140, 272), 'HỎI', font=F(36, True), fill='white')
    y = 255
    for x in ngat(d, hoi, F(50, True), 1180):
        d.text((270, y), x, font=F(50, True), fill=XANH); y += 70
    if dap:
        y0 = y + 90; dg = ngat(d, dap, F(46), 1280)
        d.rounded_rectangle([330, y0, 1830, y0 + 70 + 64 * len(dg)], radius=30, fill=(255, 246, 214))
        d.ellipse([1690, y0 + 25 + 64 * len(dg) - 90, 1800, y0 + 25 + 64 * len(dg) + 20], fill=(190, 120, 0))
        d.text((1708, y0 + 25 + 64 * len(dg) - 62), 'ĐÁP', font=F(34, True), fill='white')
        y = y0 + 35
        for x in dg:
            d.text((370, y), x, font=F(46), fill=(40, 40, 40)); y += 64
    a.save(tep)


def canh_tinh(so, anh, loi, phong=False):
    """Một ảnh tĩnh + chuỗi lời đọc -> mp4; phong=True: Phóng to rất chậm (thẻ chuyển phần)."""
    ra = os.path.join(TAM, f'c{so:03d}.mp4')
    mp3 = [doc(g, l) for g, l in loi]
    T = 0.5 + sum(do_dai(m) + 0.4 for m in mp3) + 0.3
    vao, am = [], ''
    for i, m in enumerate(mp3):
        vao += ['-i', m]
        am += f"[{i + 1}:a]aresample=44100,{'adelay=500|500,' if i == 0 else ''}apad=pad_dur=0.4[a{i}];"
    am += ''.join(f'[a{i}]' for i in range(len(mp3))) + f"concat=n={len(mp3)}:v=0:a=1,apad=pad_dur=2,afade=t=in:d=0.2,afade=t=out:st={T - MO:.2f}:d={MO}[a];"
    n = int(T * 25) + 1
    hinh = (f"[0:v]scale=3840:2160,zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps=25" if phong
            else "[0:v]scale=1920:1080,fps=25")
    hinh += f",fade=t=in:d={MO},fade=t=out:st={T - MO:.2f}:d={MO},format=yuv420p[v]"
    dau = ['-i', anh] if phong else ['-loop', '1', '-framerate', '25', '-t', f'{T:.2f}', '-i', anh]
    subprocess.run([FF, '-y', '-loglevel', 'error'] + dau + vao + ['-filter_complex', am + hinh, '-map', '[v]', '-map', '[a]', '-t', f'{T:.2f}'] + MA + [ra], check=True)
    return ra


def canh_video(so, tep):
    ra = os.path.join(TAM, f'c{so:03d}.mp4'); T = do_dai(tep)
    subprocess.run([FF, '-y', '-loglevel', 'error', '-i', tep, '-vf', f"scale=1920:1080,fps=25,fade=t=in:d={MO},fade=t=out:st={T - MO:.2f}:d={MO}",
                    '-af', f"afade=t=in:d=0.2,afade=t=out:st={T - MO:.2f}:d={MO}"] + MA + [ra], check=True)
    return ra


def main():
    ds, so, moc, t = [], 0, [], 0.0
    for muc in KB:
        so += 1
        if muc[0] == 'the':
            p = os.path.join(TAM, f'the{so:03d}.png'); the(muc[1], muc[2], muc[3], p); c = [canh_tinh(so, p, muc[4], phong=True)]; ten = f'{muc[1]}: {muc[2]}'
        elif muc[0] == 'trang':
            c = [canh_tinh(so, os.path.join(TRANG, f'trang-{muc[1]:02d}.png'), muc[2])]; ten = f'Trang trình chiếu {muc[1]}'
        elif muc[0] == 'video':
            c = [canh_video(so, os.path.join(BAN, muc[1]))]; ten = muc[1]
        else:   # hỏi - đáp: Hiện câu hỏi (giọng nam), rồi hiện thêm câu đáp (giọng nữ)
            p1, p2 = os.path.join(TAM, f'hoi{so:03d}a.png'), os.path.join(TAM, f'hoi{so:03d}b.png')
            the_hoi(muc[1], '', p1); the_hoi(muc[1], muc[2], p2)
            c = [canh_tinh(so, p1, [('nam', muc[1])])]; so += 1; c.append(canh_tinh(so, p2, [('nu', muc[2])])); ten = 'Hỏi - đáp: ' + muc[1]
        moc.append((t, ten)); t += sum(do_dai(x) for x in c); ds += c
        print(f'  {int(moc[-1][0]) // 60:02d}:{int(moc[-1][0]) % 60:02d}  {ten}')
    lst = os.path.join(TAM, 'ds.txt'); open(lst, 'w', encoding='utf-8').write(''.join(f"file '{os.path.basename(x)}'\n" for x in ds))
    ra = os.path.join(BAN, 'A_VIDEO-TOAN-BO_Trinh-dien-AI_17.10.2026.mp4')
    subprocess.run([FF, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', ra], check=True, cwd=TAM)
    open(os.path.join(BAN, 'A_VIDEO-TOAN-BO_moc-thoi-gian.txt'), 'w', encoding='utf-8').write(
        'Mốc thời gian video toàn bộ\n' + ''.join(f'{int(a) // 60:02d}:{int(a) % 60:02d}  {b}\n' for a, b in moc))
    T = do_dai(ra); print(f'→ {ra} | {int(T) // 60} phút {int(T) % 60} giây')


if __name__ == '__main__':
    main()
