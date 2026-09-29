# -*- coding: utf-8 -*-
"""Luật phân loại văn bản cho CSDL theo dõi nhiệm vụ (Trường CĐ Kon Tum).
Luật KHÁC NHAU theo loại văn bản — sửa ở đây là sửa cả bản dựng lẫn agent chạy 2 giờ/lần.

KH-CĐKT : lấy kế hoạch THỰC HIỆN (có nhiệm vụ/sản phẩm theo Phụ lục TB 736).
          Loại ra kế hoạch vận hành đào tạo: giảng dạy, khai/bế giảng, mở lớp,
          tổ chức lớp, lớp lái xe, vật tư, tham dự sự kiện — và MỌI kế hoạch
          nhắc tới mã lớp cụ thể (K7C, K8T, K9N...).
TB-CĐKT : CHỈ lấy Thông báo KẾT LUẬN (giao ban, cuộc họp, hội đồng) — loại
          thông báo có giao nhiệm vụ. Mọi thông báo khác đều bỏ.
"""
import re, unicodedata

def _kd(s):
    s = unicodedata.normalize('NFD', s or '')
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('đ','d').replace('Đ','D').lower()

MA_LOP = r'\blop k\d[cnt]\b|\bk\d[cnt] [a-z]|\blop k\d\b'

KH_LOAI_RA = [
 (r'giang day thuc hanh|giang day tich hop|tach lop|phan cong chia nhom|dieu chinh phan cong giang day','Giảng dạy theo lớp'),
 (r'khai giang lop|be giang lop|to chuc lop|mo lop|don hoc sinh','Tổ chức lớp'),
 (r'\bdao tao lop\b|lai xe (mo to|o to)|hang a1|hang b|hang c1','Lớp lái xe / lớp nghề cụ thể'),
 (r'dao tao thuc hanh toan khoa|tien do dao tao lop','Kế hoạch đào tạo theo lớp'),
 (r'vat tu, dung cu giang day|vat thuc hanh|vat tu giang day','Vật tư giảng dạy'),
 (r'ke hoach tham du|tham du le|tham du phien hop','Tham dự sự kiện'),
]
KH_GIU_LAI = [
 (r'trien khai thuc hien (nghi quyet|quyet dinh|thong tu|cong van|thong bao|ke hoach|chi thi)','Triển khai VB cấp trên'),
 (r'xay dung chuong trinh|bien soan giao trinh|tham dinh','Xây dựng CT/GT, thẩm định'),
 (r'hoi giang|hoi nghi so ket|hoi thao|toa dam|so ket|tong ket','Hội nghị, hội giảng'),
 (r'khoa hoc, cong nghe|doi moi sang tao|nghien cuu khoa hoc|de tai','KHCN, đổi mới sáng tạo'),
 (r'bo nhiem|tuyen dung|danh gia vien chuc|kpi|quy hoach can bo','Tổ chức - cán bộ'),
 (r'kiem dinh|bao dam chat luong|chat luong cao|tu danh gia','Đảm bảo chất lượng'),
 (r'truyen thong|tu van huong nghiep|quang ba','Truyền thông, hướng nghiệp'),
 (r'lien ket dao tao voi doanh nghiep nam hoc|cu nha gia?o .*doanh nghiep','Gắn kết doanh nghiệp'),
 (r'an toan thong tin|an ninh mang|bi mat nha nuoc|phong, chong tham nhung|chuyen doi so|lms|co so du lieu','CĐS, ATTT, nội chính'),
 (r'khao thi nam hoc','Khảo thí năm học'),
 (r'giai the thao|van nghe|tuan le|ngay hoi|le tot nghiep|le khai giang nam hoc','Hoạt động, sự kiện Trường'),
 (r'phat quang|don dep|sua chua|cai tao|dau tu|co so vat chat','Cơ sở vật chất'),
 (r'tap huan|boi duong (nghiep vu|chuyen sau)','Tập huấn, bồi dưỡng'),
 (r'lam viec voi doan|cuoc hop lanh dao|hop ban chi dao','Làm việc với đoàn, họp chỉ đạo'),
]
# TB: chỉ giữ thông báo kết luận có giao nhiệm vụ
TB_GIU_LAI = [
 (r'ket luan .*giao ban','Kết luận giao ban'),
 (r'ket luan cua (bi thu|hieu truong|chu tich|pho hieu truong)','Kết luận của lãnh đạo'),
 (r'ket luan .*(cuoc hop|hoi nghi|hoi dong|toa dam|buoi lam viec)','Kết luận cuộc họp / hội đồng'),
 (r'\bket luan\b.*(giao|phan cong) (nhiem vu|cong viec)','Kết luận có giao nhiệm vụ'),
]

def phan_loai(trich_yeu, so_ky_hieu=''):
    s = _kd(trich_yeu)
    la_tb = 'TB-' in (so_ky_hieu or '').upper()

    if la_tb:
        # Thông báo điều chỉnh/bổ sung một kết luận đã có thì không phải kết luận mới
        if re.search(r'dieu chinh|bo sung thanh phan|gia han|dung cuoc hop', s):
            return 'Không theo dõi', 'Thông báo điều chỉnh hành chính'
        for rx, ly in TB_GIU_LAI:
            if re.search(rx, s):
                return 'Nhiệm vụ', ly
        return 'Không theo dõi', 'Thông báo không phải kết luận giao nhiệm vụ'

    # Kế hoạch
    if re.search(MA_LOP, s):
        return 'Vận hành đào tạo', 'Gắn với lớp cụ thể'
    giu  = [ly for rx, ly in KH_GIU_LAI if re.search(rx, s)]
    loai = [ly for rx, ly in KH_LOAI_RA if re.search(rx, s)]
    if giu and not loai: return 'Nhiệm vụ', '; '.join(giu[:2])
    if loai and not giu: return 'Vận hành đào tạo', '; '.join(loai[:2])
    if giu and loai:     return 'Cần xem lại', 'Giữ: %s | Loại: %s' % (giu[0], loai[0])
    return 'Cần xem lại', 'Không khớp luật nào'
