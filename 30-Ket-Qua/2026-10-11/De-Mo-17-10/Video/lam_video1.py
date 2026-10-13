# -*- coding: utf-8 -*-
"""Dựng Video 1 — Giới thiệu nhanh 03 hệ (trang hình + giọng đọc AI tiếng Việt) -> .mp4
Chạy: python lam_video1.py            (cần: Pillow, edge-tts, imageio-ffmpeg)
Sửa lời đọc, nội dung trang ngay trong danh sách CANH rồi chạy lại.
Giọng đọc: dịch vụ Microsoft Edge TTS (lời đọc được gửi lên máy chủ Microsoft) — chỉ đưa nội dung công khai.
"""
import asyncio, os, subprocess, sys
import edge_tts
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')
THU_MUC = os.path.dirname(os.path.abspath(__file__))
TAM = os.path.join(THU_MUC, '_tam')
RA = os.path.join(THU_MUC, 'Video-1_Gioi-thieu-nhanh-03-he_v3.mp4')
GIONG = 'vi-VN-NamMinhNeural'
TOC_DO = '-4%'
W, H = 1920, 1080
XANH, XANH_NHAT, DEN, XAM, DO = (13, 59, 102), (232, 240, 249), (25, 25, 25), (95, 95, 95), (170, 30, 30)
F = lambda c, dam=False: ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf' if dam else r'C:\Windows\Fonts\arial.ttf', c)

# (tiêu đề, [dòng nội dung], lời đọc) — dòng bắt đầu bằng "#" là số liệu nổi bật, "!" là dòng nhấn mạnh
CANH = [
 ('Ba hệ hỗ trợ tham mưu bằng trí tuệ nhân tạo',
  ['Kho dữ liệu nền KTC-Database', 'Hệ rà soát văn bản KTC-Ra-Soat-897', 'Bộ công cụ quản trị nhiệm vụ KTC-Quan-tri',
   '!Phòng Tổng hợp – Hành chính và Quản trị, Trường Cao đẳng Kon Tum'],
  'Kính thưa các đồng chí. Phòng Tổng hợp, Hành chính và Quản trị xin giới thiệu nhanh ba hệ đang được sử dụng hằng ngày tại Trường Cao đẳng Kon Tum: '
  'kho dữ liệu nền, hệ rà soát văn bản, và bộ công cụ quản trị nhiệm vụ.'),
 ('Nguyên tắc: Nền móng trước, công cụ sau',
  ['Kho dữ liệu nền  →  Công cụ AI  →  Người kiểm tra  →  Ban hành', 'AI đọc, đối chiếu, dự thảo', 'Người có thẩm quyền quyết định',
   '!Mọi kết quả truy được về văn bản nguồn'],
  'Nguyên tắc của chúng tôi là: nền móng trước, công cụ sau. Trí tuệ nhân tạo chỉ tham mưu đúng khi được đọc đúng văn bản của chính cơ quan. '
  'Công cụ đọc, đối chiếu và dự thảo. Người có thẩm quyền quyết định.'),
 ('1. Kho dữ liệu nền KTC-Database',
  ['#557   Văn bản pháp luật', '#582   Quy chế, kế hoạch, báo cáo của Trường', '#  41   Mẫu văn bản', '#130   Văn bản tốt làm mẫu văn phong',
   '#  49   Đề án, đề tài', '!Mỗi văn bản có tệp mô tả: Số hiệu, ngày, hiệu lực, văn bản thay thế'],
  'Kho dữ liệu nền được lưu trên Google Drive, gồm năm kho: văn bản pháp luật; quy chế, kế hoạch, báo cáo của Trường; mẫu văn bản; '
  'văn bản tốt làm mẫu văn phong; và đề án, đề tài. Tổng cộng khoảng một nghìn ba trăm văn bản. Mỗi văn bản có tệp mô tả số hiệu, ngày ban hành, '
  'hiệu lực và văn bản thay thế.'),
 ('Vì sao kho dữ liệu nền là ưu việt',
  ['Đúng căn cứ: Dẫn đúng số hiệu, ngày ban hành; cảnh báo văn bản hết hiệu lực', 'Đúng văn phong: Dựng từ văn bản cơ quan đã ban hành',
   'Kiểm tra lại được: Mỗi nội dung chỉ về một văn bản trong kho', 'An toàn: Người dùng chỉ được đọc; công cụ có cơ chế chặn ghi',
   '!Một nguồn dùng chung cho mọi công cụ, mọi đơn vị'],
  'Nhờ có kho, khi soạn một kế hoạch, công cụ tìm căn cứ ngay trong kho, dẫn đúng số hiệu, đúng ngày ban hành, và cảnh báo văn bản đã hết hiệu lực. '
  'Văn bản mới được dựng từ văn bản tương tự đã ban hành, nên giữ đúng văn phong của cơ quan. Kho chỉ cho phép đọc, và công cụ có cơ chế chặn ghi.'),
 ('Đề xuất cho Đảng ủy Ủy ban nhân dân tỉnh: Lập kho trước',
  ['Văn bản chỉ đạo của cấp trên còn hiệu lực', 'Quy chế làm việc, chương trình công tác', 'Văn bản đã ban hành tốt làm mẫu',
   'Mẫu văn bản theo thể thức của Đảng', 'Danh mục đơn vị, đầu mối', '!Không đưa tài liệu thuộc bí mật nhà nước vào kho'],
  'Đối với Đảng ủy Ủy ban nhân dân tỉnh, chúng tôi đề xuất thiết lập kho tương tự trước khi triển khai công cụ: văn bản chỉ đạo của cấp trên, '
  'quy chế làm việc, chương trình công tác, văn bản đã ban hành tốt, mẫu văn bản theo thể thức của Đảng. Không đưa tài liệu thuộc bí mật nhà nước vào kho.'),
 ('2. Hệ rà soát văn bản KTC-Ra-Soat-897 (bản 2.25)',
  ['Rà soát dự thảo trước khi trình ký, dùng chung toàn Trường', '04 hệ quy chiếu, có riêng văn bản của Đảng', '09 bảng kiểm tra  ·  23 kỹ năng  ·  19 câu lệnh mẫu',
   'Báo cáo rà soát 08 phần, vấn đề xếp theo 04 mức', '!Còn vấn đề Mức 1 thì không trình ký'],
  'Hệ thứ hai là hệ rà soát văn bản, dùng chung cho toàn Trường. Hệ có bốn hệ quy chiếu, trong đó có riêng văn bản của Đảng; chín bảng kiểm tra; '
  'và báo cáo rà soát tám phần. Còn vấn đề mức một thì không trình ký. Hệ này sẽ được trình diễn kỹ ở phần ba.'),
 ('3. Bộ công cụ KTC-Quan-tri (bản 1.3.13)',
  ['Kế hoạch → Giao việc → Theo dõi → Báo cáo → Rà soát → Trình ký', '08 kỹ năng  ·  07 trợ lý AI kiểm tra độc lập  ·  cơ chế chặn ghi kho',
   '#10 ngày làm việc  ·  26 phiên  ·  924 thao tác', '#35 văn bản, 04 bảng tính được hỗ trợ dựng', '!Đã qua 06 vòng thẩm định độc lập; đang trình thẩm định lần 2 tại Trường'],
  'Hệ thứ ba là bộ công cụ quản trị nhiệm vụ, khép kín chu trình từ kế hoạch, giao việc, theo dõi, báo cáo, đến rà soát và trình ký. '
  'Bộ công cụ gồm tám kỹ năng và bảy trợ lý trí tuệ nhân tạo kiểm tra độc lập. Trong mười ngày làm việc gần đây, phòng đã dùng thật hai mươi sáu phiên, '
  'chín trăm hai mươi bốn thao tác, hỗ trợ dựng ba mươi lăm văn bản.'),
 ('08 kỹ năng: Mỗi kỹ năng là một quy trình nghiệp vụ đã viết sẵn',
  ['Kế hoạch: Tổng hợp kế hoạch công tác năm, quý, tháng', 'Theo dõi công việc: Tiến độ, minh chứng, cảnh báo quá hạn',
   'Báo cáo: Tổng hợp, kiểm tra báo cáo tháng, quý, năm', 'Quản trị: Chuẩn hóa nhiệm vụ, đối chiếu kế hoạch với kết quả',
   'Soạn thảo văn bản: Dựng từ văn bản tương tự đã ban hành', 'Thể thức: Chuẩn trình bày mọi tệp Word, Excel',
   'Lập KPI cá nhân: Kế hoạch, chỉ tiêu KPI theo quý', 'Tự đánh giá KPI: Chấm điểm, đề xuất mức xếp loại'],
  'Tám kỹ năng là tám quy trình nghiệp vụ đã được viết sẵn, người dùng chỉ cần gọi tên. Bốn kỹ năng cho chu trình nhiệm vụ: kế hoạch, theo dõi công việc, '
  'báo cáo, và quản trị. Hai kỹ năng cho văn bản: soạn thảo từ văn bản tương tự đã ban hành, và chuẩn thể thức mọi tệp Word, Excel. '
  'Hai kỹ năng cho cá nhân: lập kế hoạch chỉ tiêu theo quý, và tự đánh giá, chấm điểm cuối quý.'),
 ('07 trợ lý AI: Người kiểm tra thứ hai, chạy độc lập với người soạn',
  ['Kiểm hồ sơ đơn vị: Đúng mẫu, đủ cột, đúng công thức', 'Tra cứu căn cứ: Tìm sâu trong kho văn bản, kèm hiệu lực',
   'Quét hiệu lực, viện dẫn: Văn bản được dẫn còn hiệu lực không', 'Kiểm sản phẩm: Kiểm tra cuối trước khi giao',
   'Xác minh minh chứng: Việc “hoàn thành” có minh chứng thật không', 'Tự học: Ghi lại điều người dùng đã sửa',
   'Tự cải tiến: Đề xuất sửa quy tắc, chờ người duyệt', '!Trợ lý không tự sửa sản phẩm, không tự phê duyệt'],
  'Bảy trợ lý trí tuệ nhân tạo đóng vai người kiểm tra thứ hai, chạy độc lập với người soạn. Trợ lý kiểm hồ sơ đơn vị nộp. Trợ lý tra cứu căn cứ trong kho. '
  'Trợ lý quét hiệu lực các văn bản được viện dẫn. Trợ lý kiểm sản phẩm trước khi giao. Trợ lý xác minh minh chứng. '
  'Và hai trợ lý tự học, tự cải tiến: ghi lại điều người dùng đã sửa, rồi đề xuất cải tiến để con người duyệt. Trợ lý không tự sửa sản phẩm, và không tự phê duyệt.'),
 ('Tiếp theo: Trình diễn trên tình huống cụ thể',
  ['Phần 1.  Tổng hợp kế hoạch công tác quý, tháng', 'Phần 2.  Xây dựng báo cáo tháng, quý', 'Phần 3.  Rà soát văn bản bằng KTC-Ra-Soat-897',
   '!Dữ liệu trình diễn là dữ liệu giả định'],
  'Sau đây, chúng tôi xin trình diễn ba nội dung trên một tình huống cụ thể: tổng hợp kế hoạch công tác, xây dựng báo cáo, và rà soát văn bản. '
  'Dữ liệu trình diễn là dữ liệu giả định.'),
]


def ngat(d, chu, font, rong):
    ra, dong = [], ''
    for tu in chu.split(' '):
        thu = (dong + ' ' + tu).strip()
        if d.textlength(thu, font=font) <= rong:
            dong = thu
        else:
            ra.append(dong); dong = tu
    return ra + [dong]


def ve(i, tieu_de, dong, tep):
    im = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 190], fill=XANH)
    ft = F(64, True)
    td = ngat(d, tieu_de, ft, W - 200)
    if len(td) > 1:
        ft = F(52, True); td = ngat(d, tieu_de, ft, W - 200)
    y = 95 - len(td) * (ft.size + 8) // 2
    for t in td:
        d.text((100, y), t, font=ft, fill='white'); y += ft.size + 8
    y = 250
    for x in dong:
        if x.startswith('!'):
            f = F(42, True); ds = ngat(d, x[1:], f, W - 280)
            cao = len(ds) * 56 + 36
            d.rounded_rectangle([100, y + 6, W - 100, y + 6 + cao], 18, fill=XANH_NHAT)
            yy = y + 24
            for t in ds:
                d.text((140, yy), t, font=f, fill=XANH); yy += 56
            y += cao + 30
        elif x.startswith('#'):
            f = F(50, True)
            d.text((140, y), x[1:], font=f, fill=DO); y += 82
        else:
            f = F(46)
            d.ellipse([112, y + 20, 130, y + 38], fill=XANH)
            for t in ngat(d, x, f, W - 300):
                d.text((160, y), t, font=f, fill=DEN); y += 62
            y += 24
    d.line([100, H - 84, W - 100, H - 84], fill=(200, 200, 200), width=2)
    d.text((100, H - 66), 'Trường Cao đẳng Kon Tum  ·  Phòng TH-HC&QT', font=F(28), fill=XAM)
    so = f'{i}/{len(CANH)}'
    d.text((W - 100 - d.textlength(so, font=F(28)), H - 66), so, font=F(28), fill=XAM)
    im.save(tep)


async def doc(loi, tep):
    await edge_tts.Communicate(loi, GIONG, rate=TOC_DO).save(tep)


def doc_lai(loi, tep, lan=8):
    """Dịch vụ giọng đọc đôi khi không trả âm thanh — thử lại; cảnh đã có tệp tiếng cùng lời thì dùng lại."""
    import time
    dau = tep + '.txt'
    if os.path.exists(tep) and os.path.getsize(tep) > 1000 and os.path.exists(dau) and open(dau, encoding='utf-8').read() == loi:
        return
    for i in range(lan):
        try:
            asyncio.run(doc(loi, tep)); open(dau, 'w', encoding='utf-8').write(loi); return
        except Exception as e:
            print('   thử lại giọng đọc', i + 1, type(e).__name__); time.sleep(3)
    raise SystemExit('Không tạo được giọng đọc: ' + tep)


def main():
    os.makedirs(TAM, exist_ok=True)
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    ds = []
    for i, (td, dong, loi) in enumerate(CANH, 1):
        png, mp3, mp4 = (os.path.join(TAM, f'c{i:02d}.{x}') for x in ('png', 'mp3', 'mp4'))
        ve(i, td, dong, png)
        doc_lai(loi, mp3)
        # hình tĩnh + lời đọc, thêm 0,7 giây lặng cuối cảnh
        subprocess.run([ff, '-y', '-loglevel', 'error', '-loop', '1', '-i', png, '-i', mp3, '-af', 'apad=pad_dur=0.7', '-shortest',
                        '-c:v', 'libx264', '-tune', 'stillimage', '-pix_fmt', 'yuv420p', '-r', '25', '-c:a', 'aac', '-b:a', '160k',
                        '-ar', '44100', '-ac', '2', mp4], check=True)
        ds.append(mp4)
        print(f'  cảnh {i}: {td}')
    lst = os.path.join(TAM, 'ds.txt')
    open(lst, 'w', encoding='utf-8').write(''.join(f"file '{os.path.basename(x)}'\n" for x in ds))
    subprocess.run([ff, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', RA], check=True, cwd=TAM)
    r = subprocess.run([ff, '-i', RA], capture_output=True, text=True, encoding='utf-8', errors='ignore').stderr
    print('→', RA, '|', next((x.strip() for x in r.splitlines() if 'Duration' in x), ''))


if __name__ == '__main__':
    main()
