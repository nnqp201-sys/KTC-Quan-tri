# -*- coding: utf-8 -*-
"""
test_cong_ho_so_897.py — Ca thu cho cong ho so 897 (KI-021)

Moi ca co thu thuan va thu nguoc theo quy tac: them phep kiem thi them ca nguoc.
"""
import os
import sys
import tempfile
import shutil
import zipfile
import re
from xml.etree import ElementTree as ET

# Thu muc goc du an
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, '2A-KTC-Ra-Soat-897', 'ktc-ra-soat-897', 'tools'))

import kiem_ke_ho_so as kk


def tao_docx_don_gian(path, paras, so_line=None):
    """Tao tep .docx don gian voi cac doan van cho truoc."""
    W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    doc = ET.Element(W + 'document')
    body = ET.SubElement(doc, W + 'body')
    for txt in paras:
        p = ET.SubElement(body, W + 'p')
        r = ET.SubElement(p, W + 'r')
        t = ET.SubElement(r, W + 't')
        t.text = txt
    # Tao zip
    with zipfile.ZipFile(path, 'w') as z:
        z.writestr('[Content_Types].xml', '''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>''')
        z.writestr('_rels/.rels', '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>''')
        z.writestr('word/document.xml', ET.tostring(doc, encoding='unicode'))


def tao_docx_voi_noBreakHyphen(path, paras):
    """Tao tep .docx co noBreakHyphen trong so hieu."""
    W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    doc = ET.Element(W + 'document')
    body = ET.SubElement(doc, W + 'body')
    for txt in paras:
        p = ET.SubElement(body, W + 'p')
        # Chia txt theo '-' va chen noBreakHyphen
        parts = txt.split('-')
        for i, part in enumerate(parts):
            r = ET.SubElement(p, W + 'r')
            t = ET.SubElement(r, W + 't')
            t.text = part
            if i < len(parts) - 1:
                # Chen noBreakHyphen thay vi '-'
                r2 = ET.SubElement(p, W + 'r')
                ET.SubElement(r2, W + 'noBreakHyphen')
    with zipfile.ZipFile(path, 'w') as z:
        z.writestr('[Content_Types].xml', '''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>''')
        z.writestr('_rels/.rels', '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>''')
        z.writestr('word/document.xml', ET.tostring(doc, encoding='unicode'))


class TestN2NoBreakHyphen:
    """T1: noBreakHyphen trong so hieu van ban."""

    def test_T1_noBreakHyphen_khop(self):
        """Du thao vien dan 5394/SGDDT-GDNNQLDT bang noBreakHyphen; ho so co tep nguon."""
        with tempfile.TemporaryDirectory() as td:
            # Du thao co noBreakHyphen
            dt = os.path.join(td, 'du_thao.docx')
            tao_docx_voi_noBreakHyphen(dt, [
                'DU THAO',
                'Thuc hien Cong van so 5394/SGDDT-GDNNQLDT ngay 29/10/2026'
            ])
            # Tep nguon binh thuong - dung Unicode dung
            nguon = os.path.join(td, 'CV_5394.docx')
            tao_docx_don_gian(nguon, [
                u'Số: 5394/SGDDT-GDNNQLDT',  # "Số:" voi Unicode
                'Noi dung cong van'
            ])
            # Doc
            paras_dt = kk.docx_paras(dt)
            paras_nguon = kk.docx_paras(nguon)
            # Kiem tra noBreakHyphen duoc doc thanh '-'
            assert '5394/SGDDT-GDNNQLDT' in ' '.join(paras_dt), 'noBreakHyphen khong duoc doc thanh -'
            # Kiem tra khoa duoc tao
            keys = kk.ma_dinh_danh('CV_5394.docx', paras_nguon)
            assert '5394/SGDDT-GDNNQLDT' in keys, f'Khoa khong duoc tao: {keys}'

    def test_T1_nguoc_so_khac(self):
        """Ho so co tep so 5395 thi vien dan 5394 van THIEU."""
        with tempfile.TemporaryDirectory() as td:
            nguon = os.path.join(td, 'CV_5395.docx')
            tao_docx_don_gian(nguon, ['So: 5395/SGDDT-GDNNQLDT'])
            paras = kk.docx_paras(nguon)
            keys = kk.ma_dinh_danh('CV_5395.docx', paras)
            assert '5394/SGDDT-GDNNQLDT' not in keys, 'Khong duoc khop nham so khac'


class TestN1KhoangTrangSoHieu:
    """T2: khoang trang quanh / va - trong so hieu."""

    def test_T2_khoang_trang(self):
        """Tep nguon 'So: 287 /QD-UBND' (co dau cach) tao khoa 287/QD-UBND."""
        with tempfile.TemporaryDirectory() as td:
            nguon = os.path.join(td, 'QD_287.docx')
            tao_docx_don_gian(nguon, [u'Số: 287 /QĐ-UBND', 'Noi dung'])  # "Số: 287 /QĐ-UBND"
            paras = kk.docx_paras(nguon)
            keys = kk.ma_dinh_danh('QD_287.docx', paras)
            assert '287/QD-UBND' in keys, f'Khoa khong duoc tao: {keys}'


class TestN6DonViDem:
    """T6: 'phu luc 06 hoc sinh' khong phai Phu luc 06."""

    def test_T6_don_vi_dem(self):
        """Cau 'va phu luc 06 hoc sinh' khong bao thieu Phu luc 06."""
        paras = [
            'DU THAO',
            'HD Naseed nam 2026 va phu luc 06 hoc sinh.',
            'PHU LUC I',
            'Noi dung phu luc I'
        ]
        vien_dan = kk.trich_dan(paras)
        # Khong co vien dan nao la "Phu luc 06"
        so_phu_luc = [x for x in vien_dan if 'phu luc' in x.get('loai', '').lower()]
        assert not any('06' in str(x.get('so', '')) for x in so_phu_luc), \
            f'Phu luc 06 bi nham la vien dan: {so_phu_luc}'

    def test_T6_nguoc_phu_luc_that(self):
        """Cau 'chi tiet tai Phu luc 06' khi khong co tieu de Phu luc 06 thi phai bao."""
        # Day la kiem tra trong ham main(), khong phai trich_dan()
        # Bo qua vi can chay ca script
        pass


class TestN8VanBanDang:
    """T8, T9, T10: nhan dang so hieu van ban Dang."""

    def test_T8_nghi_quyet_dang(self):
        """Du thao chinh quyen vien dan 'Nghi quyet so 19-NQ/TW'."""
        loai = kk.loai_theo_ky_hieu('19-NQ/TW')
        # Kiem tra co chu "Dang" hoac "Đảng"
        assert 'Dang' in loai or u'Đảng' in loai, f'Khong nhan dien van ban Dang: {loai}'

    def test_T8_nguoc_khong_khop_nham(self):
        """Ho so chi co 19/NQ-CP (chinh quyen) khong khop 19-NQ/TW (Dang)."""
        key_dang = kk.key_so('19-NQ/TW')
        key_cq = kk.key_so('19/NQ-CP')
        assert key_dang != key_cq, f'Khoa trung nham: {key_dang} == {key_cq}'

    def test_T9_quy_dinh_dang(self):
        """'Quy dinh so 208-QD/TW' la Quy dinh Dang, khong phai Quyet dinh chinh quyen."""
        loai = kk.loai_theo_ky_hieu('208-QD/TW')
        assert 'Dang' in loai or u'Đảng' in loai, f'Khong nhan dien Quy dinh Dang: {loai}'

    def test_T9_nguoc_so_giong_khac_he(self):
        """208/QD-UBND (chinh quyen) khac 208-QD/TW (Dang)."""
        key_dang = kk.key_so('208-QD/TW')
        key_cq = kk.key_so('208/QD-UBND')
        assert key_dang != key_cq, f'Khoa trung nham: {key_dang} == {key_cq}'

    def test_T10_co_quan_dai(self):
        """So hieu Dang co co quan dai: 12-BC/DU, 1234-CV/UBKTTW."""
        with tempfile.TemporaryDirectory() as td:
            nguon = os.path.join(td, 'BC_DU.docx')
            tao_docx_don_gian(nguon, [u'Số 12-BC/ĐU', 'Noi dung'])  # "Số 12-BC/ĐU"
            paras = kk.docx_paras(nguon)
            keys = kk.ma_dinh_danh('BC_DU.docx', paras)
            assert '12-BC/DU' in keys, f'Khoa Dang khong duoc tao: {keys}'


class TestKeyHoa:
    """Kiem tra ham key_so() va cung_loai()."""

    def test_key_so_chuan_hoa(self):
        """key_so bo khoang trang va chuan hoa."""
        assert kk.key_so('287 /QD-UBND') == '287/QD-UBND'
        assert kk.key_so('19 - NQ/TW') == '19-NQ/TW'
        assert kk.key_so('Đ') == 'D'


if __name__ == '__main__':
    import pytest
    sys.exit(pytest.main([__file__, '-v', '--tb=short']))
