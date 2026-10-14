# -*- coding: utf-8 -*-
"""Phông nền dùng chung cho video trình diễn 17/10/2026: Màu theo trang cdkontum.edu.vn (xanh #0d4e96, cam #f69528),
họa tiết mạng nơ-ron (điểm sáng nối nhau) cho ra chất trí tuệ nhân tạo. Chỉ dùng PIL, kết quả cố định theo hạt giống."""
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

XANH, XANH_DAM, XANH_NHAT = (13, 78, 150), (5, 30, 72), (230, 240, 251)
CAM, CAM_DAM, DEN, XAM = (246, 149, 40), (237, 101, 4), (28, 32, 40), (96, 104, 118)


def F(c, dam=False):
    return ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf' if dam else 'C:/Windows/Fonts/segoeui.ttf', c)


def _doc(w, h, tren, duoi, cheo=0.35):
    """Nền chuyển sắc từ góc trên trái (tren) xuống góc dưới phải (duoi)."""
    nho = Image.new('RGB', (64, 64)); px = nho.load()
    for y in range(64):
        for x in range(64):
            t = min(max((y + x * cheo) / (63 * (1 + cheo)), 0), 1)
            px[x, y] = tuple(int(a + (b - a) * t) for a, b in zip(tren, duoi))
    return nho.resize((w, h), Image.BICUBIC)


def mang(w, h, so_nut, hat, vung=None, do_dam=1.0, nut_cam=0.18):
    """Lớp trong suốt vẽ mạng nơ-ron: Nút sáng và đường nối các nút gần nhau. vung = (x0, y0, x1, y1) giới hạn chỗ đặt nút."""
    r = random.Random(hat)
    x0, y0, x1, y1 = vung or (0, 0, w, h)
    nut = [(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(2.5, 6.5)) for _ in range(so_nut)]
    lop = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lop)
    xa = ((x1 - x0) * (y1 - y0) / so_nut) ** 0.5 * 1.55
    for i, (ax, ay, _) in enumerate(nut):
        for bx, by, _ in nut[i + 1:]:
            k = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
            if k < xa:
                d.line([ax, ay, bx, by], fill=(150, 200, 255, int(110 * (1 - k / xa) * do_dam)), width=2)
    sang = Image.new('RGBA', (w, h), (0, 0, 0, 0)); ds = ImageDraw.Draw(sang)
    for x, y, b in nut:
        mau = CAM if r.random() < nut_cam else (170, 215, 255)
        ds.ellipse([x - b * 3, y - b * 3, x + b * 3, y + b * 3], fill=mau + (int(70 * do_dam),))
        d.ellipse([x - b, y - b, x + b, y + b], fill=mau + (int(235 * do_dam),))
    return Image.alpha_composite(sang.filter(ImageFilter.GaussianBlur(9)), lop)


def nen_toan_man(w=1920, h=1080, hat=7):
    """Nền thẻ mở đầu, chuyển phần: Xanh đậm chuyển sắc, mạng nơ-ron dày ở nửa phải, vệt sáng cam ở góc."""
    a = _doc(w, h, (16, 90, 168), XANH_DAM).convert('RGBA')
    vet = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(vet).ellipse([w - 620, h - 520, w + 260, h + 300], fill=CAM_DAM + (70,))
    ImageDraw.Draw(vet).ellipse([-300, -380, 520, 300], fill=(60, 150, 255, 60))
    a = Image.alpha_composite(a, vet.filter(ImageFilter.GaussianBlur(150)))
    a = Image.alpha_composite(a, mang(w, h, 46, hat, (w * 0.50, 30, w - 30, h - 30), 0.9))
    a = Image.alpha_composite(a, mang(w, h, 16, hat + 1, (0, h * 0.62, w * 0.5, h), 0.35))
    return a.convert('RGB')


def thanh_tieu_de(im, cao=190, hat=3):
    """Vẽ thanh tiêu đề lên đầu ảnh im: Xanh chuyển sắc, mạng nơ-ron ở nửa phải, vạch cam phía dưới."""
    w = im.width
    t = _doc(w, cao, (16, 92, 172), (7, 44, 100), cheo=2.0).convert('RGBA')
    t = Image.alpha_composite(t, mang(w, cao, 24, hat, (w * 0.56, 8, w - 12, cao - 8), 0.7))
    im.paste(t.convert('RGB'), (0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, cao, w, cao + 7], fill=CAM)
    d.rectangle([0, cao, int(w * 0.34), cao + 7], fill=CAM_DAM)
    return d


def hoa_van_goc(im, hat=11):
    """Họa tiết mạng nơ-ron rất nhạt ở góc dưới phải nền trắng."""
    w, h = im.size
    m = mang(w, h, 22, hat, (w * 0.66, h * 0.58, w - 20, h - 110), 1.0, nut_cam=0.3)
    nhat = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    r, g, b, al = m.split()
    xanh = Image.merge('RGBA', (Image.new('L', (w, h), 13), Image.new('L', (w, h), 78), Image.new('L', (w, h), 150), al.point(lambda v: v // 6)))
    cam = Image.merge('RGBA', (r, g, b, al.point(lambda v: v // 5)))
    # nút cam giữ màu, phần còn lại ngả xanh nhạt
    mat = r.point(lambda v: 255 if v > 220 else 0)
    nhat = Image.composite(cam, xanh, mat)
    return Image.alpha_composite(im.convert('RGBA'), nhat).convert('RGB')
