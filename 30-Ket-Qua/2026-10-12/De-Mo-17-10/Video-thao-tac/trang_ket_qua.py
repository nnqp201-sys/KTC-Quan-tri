# -*- coding: utf-8 -*-
"""Video T1, T2, T3: Chiếu lần lượt từng trang tệp kết quả, mỗi trang có lời mô tả riêng (T4: xem trang_t4.py).
Tạo anh_kq/<mã>_trang_N.png (rộng 1920, ghep_video.py cuộn dọc) và anh_kq/<mã>_trang_N.mp3. PDF nguồn do anh_ket_qua.py tạo."""
import asyncio, os, sys, time
import edge_tts, pymupdf
from PIL import Image, ImageOps
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
K = 'CQA_Ke-hoach-quy-IV-2026_tong-hop_du-thao.pdf'
B = '00_Bao-cao-thang-9-2026_Co-quan-A_du-thao.pdf'
P = '00_Phu-luc-doi-chieu-KH-KQ-thang-9-2026.pdf'
# mã video: [(pdf, trang, lời)]
DS = {
 'T1': [
  (K, 0, 'Kết quả thứ nhất là dự thảo kế hoạch quý bốn của cơ quan, theo mẫu phụ lục, ba trang. Trang một: nhiệm vụ xếp theo sáu trục, mỗi dòng có người chỉ đạo, '
         'đơn vị chủ trì, sản phẩm, thời gian hoàn thành và hệ số. Lưu ý, một số dòng bị trống: đây là lỗi của công cụ khi dựng bảng, sáu dòng mất dữ liệu, '
         'người tổng hợp phải kiểm tra lại.'),
  (K, 1, 'Trang hai: cột ghi chú là phần đáng giá nhất. Công cụ ghi rõ nhiệm vụ xây dựng Quy chế tài sản công bị trùng giữa hai đơn vị; nhiệm vụ rà soát vị trí việc làm '
         'chưa có thời hạn, công cụ tạm xác định tháng mười một theo công văn của cấp trên; nhiệm vụ kiểm tra chuyên môn đã có kế hoạch chính thức.'),
  (K, 2, 'Trang ba: các nhiệm vụ của Phòng Nghiệp vụ hai được ghi chú là đơn vị nộp theo mẫu kế hoạch tháng, chưa đúng mẫu kế hoạch quý.'),
  ('Phan-1_Tong-hop-ke-hoach-quy-IV-2026_ket-qua-chay-truoc1-Bang-kiem.pdf', 0,
         'Kết quả thứ hai là bảng kiểm hồ sơ sáu đơn vị. Mỗi đơn vị một dòng: tệp nộp, mẫu nhận diện, số nhiệm vụ, vấn đề phát hiện và kết luận. '
         'Hai đơn vị đủ điều kiện tổng hợp; ba đơn vị cần bổ sung thời hạn hoặc sản phẩm; Phòng Nghiệp vụ hai trả lại vì nộp sai mẫu.')],
 'T2': [
  ('Phan-1_Tong-hop-ke-hoach-quy-IV-2026_ket-qua-chay-truoc4-Doi-chieu-van-ban.pdf', 0,
         'Kết quả là bảng đối chiếu. Mỗi văn bản chỉ đạo một dòng: số ký hiệu, thời hạn nêu trong văn bản, đơn vị đã đăng ký, nhiệm vụ gần nhất trong dự thảo kế hoạch '
         'và độ giống. Ví dụ, công văn về rà soát vị trí việc làm, hạn ba mươi tháng mười một, đã có trong dự thảo. Những dòng ghi chưa đơn vị nào đăng ký '
         'là việc cần bổ sung vào kế hoạch: báo cáo tiết kiệm, chống lãng phí, và sắp xếp trụ sở. Lưu ý: cần chạy đối chiếu trong cùng cuộc hội thoại '
         'có dự thảo kế hoạch, nếu không công cụ chỉ thấy một nửa hồ sơ.')],
 'T3': [
  (B, 0, 'Kết quả thứ nhất là dự thảo báo cáo tháng chín, ba trang, đúng thể thức báo cáo của cơ quan. Trang một: kết quả theo từng trục, có số liệu cụ thể, '
         'có số và ngày của văn bản đã ban hành để làm minh chứng.'),
  (B, 1, 'Trang hai: các trục còn lại. Nhiệm vụ đánh giá mức độ chuyển đổi số được ghi là chưa có báo cáo kết quả, chứ không kết luận là chưa làm. '
         'Tiếp theo là phần đối chiếu kết quả với kế hoạch tháng.'),
  (B, 2, 'Trang ba: tồn tại, hạn chế, trong đó nêu số liệu hai đơn vị lệch nhau, một trăm mười hai và một trăm hai mươi lượt người. '
         'Nhiệm vụ trọng tâm tháng mười đưa lên đầu hai việc đã chậm hai tháng liên tiếp. Phần ký để người có thẩm quyền quyết định.'),
  (P, 0, 'Kết quả thứ hai là phụ lục đối chiếu hai mươi bốn nhiệm vụ. Mỗi dòng có kế hoạch, kết quả thực hiện, tỷ lệ hoàn thành và đánh giá, '
         'ví dụ: hoàn thành đầy đủ, trước hạn một ngày.'),
  (P, 1, 'Trang hai của phụ lục: chữ ký số đạt mười trên mười hai; hỗ trợ kỹ thuật vượt kế hoạch; nhiệm vụ chưa có kết quả ghi không phần trăm, '
         'kèm đề nghị làm rõ nguyên nhân. Hạn chế của lượt chạy này: công cụ chưa nhận ra có hai đơn vị cùng báo cáo một kết quả.')],
}
for ma, ds in DS.items():
    for i, (pdf, tr, loi) in enumerate(ds):
        pix = pymupdf.open(os.path.join(D, 'anh_kq', pdf))[tr].get_pixmap(dpi=200)
        a = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        h = ImageOps.invert(a.convert('L')).point(lambda v: 255 if v > 20 else 0).getbbox()
        a = a.crop((max(h[0] - 30, 0), max(h[1] - 30, 0), min(h[2] + 30, a.width), min(h[3] + 30, a.height)))
        if a.height > a.width:   # trang dọc: Thu hẹp để một khung hình thấy được nửa trang, đặt giữa nền trắng
            a = a.resize((1300, int(a.height * 1300 / a.width)), Image.LANCZOS)
            n = Image.new('RGB', (1920, a.height), 'white'); n.paste(a, (310, 0)); a = n
        else:
            a = a.resize((1920, int(a.height * 1920 / a.width)), Image.LANCZOS)
        if a.height < 1080:
            n = Image.new('RGB', (1920, 1080), 'white'); n.paste(a, (0, 0)); a = n
        a.save(os.path.join(D, 'anh_kq', f'{ma}_trang_{i + 1}.png'))
        m = os.path.join(D, 'anh_kq', f'{ma}_trang_{i + 1}.mp3')
        if not (os.path.exists(m) and os.path.getsize(m) > 1000):
            for lan in range(8):
                try:
                    asyncio.run(edge_tts.Communicate(loi, 'vi-VN-NamMinhNeural', rate='-4%').save(m)); break
                except Exception as e:
                    print('lỗi', ma, i + 1, type(e).__name__); time.sleep(3)
        print(ma, 'trang', i + 1, a.size)
