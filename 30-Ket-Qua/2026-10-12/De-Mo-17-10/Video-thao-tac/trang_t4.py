# -*- coding: utf-8 -*-
"""Video T4: Chiếu lần lượt 08 trang báo cáo rà soát do Cowork tạo, mỗi trang có lời mô tả riêng.
Tạo anh_kq/T4_trang_N.png (rộng 1920, cao theo trang — ghep_video.py cuộn dọc) và anh_kq/T4_trang_N.mp3."""
import asyncio, glob, os, sys, time
import edge_tts, pymupdf
from PIL import Image, ImageOps
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
pdf = glob.glob(os.path.join(D, 'anh_kq', 'Bao_cao_Ra_soat_897*.pdf'))[0]
LOI = [
 'Kết quả là báo cáo rà soát chính thức, tám trang. Trang một, thông tin chung: công cụ xác định đây là văn bản của Đảng, áp Hướng dẫn số 05 '
 'của Văn phòng Trung ương và Quy định số 399; không áp Nghị định 30 về công tác văn thư.',
 'Trang hai ghi rõ cách đo thể thức trên tệp thật và phần không thuộc phạm vi xác minh. Phần hai bắt đầu các phát hiện. Phát hiện thứ nhất: '
 'văn bản của cùng một cấp ủy nhưng dùng hai ký hiệu khác nhau, TU và ĐU.',
 'Trang ba: căn cứ cuối cùng phải kết thúc bằng dấu chấm; tên cơ quan viết chưa thống nhất giữa Đảng ủy phường và Đảng ủy Ủy ban nhân dân phường; '
 'tên loại văn bản cỡ chữ mười bốn, quy định là mười lăm đến mười sáu. Mỗi phát hiện đều có kiến nghị sửa, căn cứ và mức độ.',
 'Trang bốn: phát hiện số năm về cỡ chữ phần ký là chưa chính xác, vì công cụ không tính định dạng kế thừa từ kiểu chữ; người kiểm tra cần loại bỏ. '
 'Phần ba liệt kê nội dung đạt: đúng thẩm quyền ban hành, hai nghị quyết viện dẫn đã đối chiếu với văn bản gốc trong kho.',
 'Trang năm: lề, dấu gạch dưới trích yếu, nơi nhận, cách đề ký đều đúng. Phần bốn là bảng tổng hợp, sáu vấn đề chia theo nhóm nội dung.',
 'Trang sáu: không có lỗi mức một; ba mức hai, hai mức ba, một mức bốn. Đánh giá tổng thể: đạt có điều kiện, cần chỉnh sửa trước khi trình ký.',
 'Trang bảy: thứ tự ưu tiên xử lý, mức độ rủi ro nếu không sửa, và phần kiểm tra chất lượng cuối cùng.',
 'Trang cuối: thông tin trách nhiệm. Ô người kiểm tra để trống, chờ người thật điền; trạng thái là bản nháp, chỉ có giá trị tham khảo cho đến khi được phê duyệt.',
]
doc = pymupdf.open(pdf)
for i, p in enumerate(doc):
    pix = p.get_pixmap(dpi=200)
    a = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    h = ImageOps.invert(a.convert('L')).point(lambda v: 255 if v > 20 else 0).getbbox()
    a = a.crop((max(h[0] - 30, 0), max(h[1] - 30, 0), min(h[2] + 30, a.width), min(h[3] + 30, a.height)))
    a = a.resize((1920, int(a.height * 1920 / a.width)), Image.LANCZOS)
    if a.height < 1080:
        n = Image.new("RGB", (1920, 1080), 'white'); n.paste(a, (0, 0)); a = n
    a.save(os.path.join(D, 'anh_kq', f'T4_trang_{i + 1}.png'))
    m = os.path.join(D, 'anh_kq', f'T4_trang_{i + 1}.mp3')
    if not (os.path.exists(m) and os.path.getsize(m) > 1000):
        for lan in range(8):
            try:
                asyncio.run(edge_tts.Communicate(LOI[i], 'vi-VN-NamMinhNeural', rate='-4%').save(m)); break
            except Exception as e:
                print('lỗi', i + 1, type(e).__name__); time.sleep(3)
    print('trang', i + 1, a.size)
