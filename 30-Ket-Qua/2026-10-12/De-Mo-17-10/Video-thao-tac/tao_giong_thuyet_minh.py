# -*- coding: utf-8 -*-
"""Tạo giọng thuyết minh (AI, tiếng Việt) cho 04 đoạn video thao tác T1–T4. Chạy: python tao_giong_thuyet_minh.py
Giọng: Microsoft Edge TTS vi-VN-HoaiMyNeural (lời đọc gửi lên máy chủ Microsoft — chỉ nội dung công khai, không có dữ liệu nội bộ)."""
import asyncio, os, sys, time
import edge_tts
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
# Bản 13/10/2026: Lời dài, phủ kín video (chọn thư mục -> giao việc -> công cụ làm việc -> kết quả), kể thêm điểm hay của từng chức năng.
# Lời phần kết quả (từng trang): trang_ket_qua.py (T1, T2, T3) và trang_t4.py (T4).
LOI = {
 'T1_Tong-hop-ke-hoach': 'Bước đầu tiên, người dùng chỉ cho công cụ thư mục chứa hồ sơ: dự thảo kế hoạch quý của sáu đơn vị và danh mục văn bản chỉ đạo. '
    'Công cụ chỉ làm việc trong thư mục được cho phép. |Sau đó, người dùng giao việc bằng một câu lệnh tiếng Việt thông thường. |'
    'Công cụ kiểm tra từng hồ sơ: nộp đúng mẫu kế hoạch quý chưa, nhiệm vụ nào thiếu thời hạn, thiếu sản phẩm, nhiệm vụ nào trùng giữa hai đơn vị. |'
    'Với nhiệm vụ thiếu thời hạn, công cụ đề xuất mốc dựa trên công văn của cấp trên, và ghi rõ đây là đề xuất để người tổng hợp quyết định.',
 'T2_Doi-chieu-van-ban-chi-dao': 'Ở phần này, người dùng chọn thư mục danh mục văn bản xuất từ hệ thống quản lý văn bản và điều hành. '
    'Công cụ chỉ đọc tệp đã xuất, hoặc đọc trong phiên người dùng đã đăng nhập; không nhập mật khẩu, không bấm nút xử lý. |'
    'Công cụ phân loại hai mươi tám văn bản: văn bản chỉ đạo của cấp trên, kế hoạch năm, kế hoạch quý, thông báo kết luận, văn bản chuyên đề, '
    'và tự tính còn bao nhiêu ngày đến hạn. |Sau đó đối chiếu với dự thảo kế hoạch, chỉ ra nhiệm vụ cấp trên đã giao, có thời hạn, '
    'nhưng chưa đơn vị nào đăng ký.',
 'T3_Bao-cao-thang': 'Với báo cáo tháng, người dùng chọn thư mục gồm báo cáo của sáu đơn vị, kế hoạch tháng và báo cáo tháng trước đã ban hành. '
    'Công cụ phát triển từ báo cáo tháng trước, giữ bố cục và lời văn quen thuộc của cơ quan, không dựng từ mẫu trống. |'
    'Mỗi nhiệm vụ trong kế hoạch được đối chiếu với kết quả đơn vị báo cáo. Nhiệm vụ nào không thấy trong báo cáo, công cụ ghi là chưa có thông tin, '
    'không tự kết luận là chưa làm. |Số liệu hai đơn vị báo cáo khác nhau được đánh dấu để người tổng hợp xác minh. |'
    'Công cụ còn nhận ra việc tồn từ tháng trước và đưa vào nhiệm vụ trọng tâm tháng tới. Mọi con số đều truy được về báo cáo của đơn vị.',
 'T4_Ra-soat-van-ban-Dang': 'Phần cuối là rà soát văn bản trước khi trình ký. Người dùng chọn thư mục chứa dự thảo, rồi gọi kỹ năng rà soát '
    'của hệ rà soát dùng chung của Trường. Công cụ nhận ra đây là văn bản của Đảng, nên áp hướng dẫn về thể thức văn bản của Đảng, '
    'không áp quy định của văn bản hành chính. Công cụ đo thể thức trên tệp thật: lề, cỡ chữ, phông chữ; đối chiếu từng văn bản được viện dẫn '
    'với kho dữ liệu, và ghi rõ phần chưa xác minh được. ',
}
# Dấu "|" trong lời: Đổi người đọc — luân phiên nam, nữ (bắt đầu bằng giọng nam). Lời không có "|": Một giọng nữ.
import subprocess, imageio_ffmpeg
GIONG = [('vi-VN-NamMinhNeural', '+0%'), ('vi-VN-HoaiMyNeural', '-4%')]


def doc(loi, giong, toc, tep):
    for lan in range(10):   # dịch vụ đôi khi không trả âm thanh — thử lại
        try:
            asyncio.run(edge_tts.Communicate(loi, giong, rate=toc).save(tep)); return
        except Exception as e:
            print('lỗi lần', lan + 1, type(e).__name__); time.sleep(3)
    raise SystemExit('Không tạo được giọng đọc')


for ten, loi in LOI.items():
    tep = os.path.join(D, ten + '.mp3')
    if os.path.exists(tep) and os.path.getsize(tep) > 1000:
        print('đã có', ten); continue
    phan = [x.strip() for x in loi.split('|')]
    if len(phan) == 1:
        doc(phan[0], *GIONG[1], tep)
    else:
        tam = []
        for i, x in enumerate(phan):
            t = os.path.join(D, f'_{ten}_{i}.mp3'); doc(x, *GIONG[i % 2], t); tam.append(t)
        loc = ''.join(f'[{i}:a]apad=pad_dur=0.3[a{i}];' for i in range(len(tam))) + ''.join(f'[a{i}]' for i in range(len(tam))) + f'concat=n={len(tam)}:v=0:a=1[a]'
        subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error'] + sum((['-i', t] for t in tam), []) + ['-filter_complex', loc, '-map', '[a]', '-b:a', '96k', tep], check=True)
        for t in tam:
            os.remove(t)
    print('OK', ten, len(phan), 'đoạn')
