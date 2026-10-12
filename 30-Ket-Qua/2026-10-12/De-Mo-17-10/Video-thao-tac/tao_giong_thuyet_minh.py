# -*- coding: utf-8 -*-
"""Tạo giọng thuyết minh (AI, tiếng Việt) cho 04 đoạn video thao tác T1–T4. Chạy: python tao_giong_thuyet_minh.py
Giọng: Microsoft Edge TTS vi-VN-HoaiMyNeural (lời đọc gửi lên máy chủ Microsoft — chỉ nội dung công khai, không có dữ liệu nội bộ)."""
import asyncio, os, sys, time
import edge_tts
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
LOI = {
 'T1_Tong-hop-ke-hoach': 'Người dùng đưa dự thảo kế hoạch quý của sáu đơn vị. Công cụ kiểm tra từng hồ sơ: đúng mẫu chưa, nhiệm vụ nào thiếu thời hạn, '
    'thiếu sản phẩm, nhiệm vụ nào trùng giữa hai đơn vị, rồi mới tổng hợp thành dự thảo kế hoạch của cơ quan, có ghi rõ nguồn từng nhiệm vụ.',
 'T2_Doi-chieu-van-ban-chi-dao': 'Tiếp theo, công cụ đọc danh mục văn bản trên hệ thống quản lý văn bản và điều hành: văn bản chỉ đạo của cấp trên, kế hoạch năm, '
    'kế hoạch quý, thông báo kết luận. Công cụ chỉ ra nhiệm vụ cấp trên đã giao, có thời hạn, nhưng chưa đơn vị nào đưa vào kế hoạch. '
    'Công cụ chỉ đọc, không thao tác trên hệ thống.',
 'T3_Bao-cao-thang': 'Với báo cáo tháng, công cụ đọc báo cáo của sáu đơn vị, đối chiếu với kế hoạch tháng, và phát triển từ báo cáo tháng trước đã ban hành. '
    'Nhiệm vụ nào không thấy trong báo cáo, công cụ ghi là chưa có thông tin, không tự kết luận là chưa làm. Số liệu hai đơn vị báo cáo khác nhau '
    'được đánh dấu để người tổng hợp xác minh.',
 'T4_Ra-soat-van-ban-Dang': 'Trước khi trình ký, dự thảo được rà soát bằng hệ rà soát dùng chung của Trường. Công cụ nhận ra đây là văn bản của Đảng, nên áp hướng dẫn '
    'về thể thức văn bản của Đảng, không áp quy định của văn bản hành chính. Công cụ đo thể thức trên tệp thật, đối chiếu từng văn bản được viện dẫn, '
    'và ghi rõ phần chưa xác minh được.',
}
for ten, loi in LOI.items():
    tep = os.path.join(D, ten + '.mp3')
    if os.path.exists(tep) and os.path.getsize(tep) > 1000:
        print('đã có', ten); continue
    for lan in range(8):   # dịch vụ đôi khi không trả âm thanh — thử lại
        try:
            asyncio.run(edge_tts.Communicate(loi, 'vi-VN-HoaiMyNeural', rate='-4%').save(os.path.join(D, ten + '.mp3')))
            print('OK', ten); break
        except Exception as e:
            print('lỗi lần', lan + 1, ten, type(e).__name__); time.sleep(3)
