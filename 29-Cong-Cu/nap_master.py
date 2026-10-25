# -*- coding: utf-8 -*-
"""Buoc 5 quy trinh trich nhiem vu: nap dong DA DUYET tu so cho duyet vao Master Task Register.

Chi nap dong co cot "Quyết định" = "Đồng ý" hoac "Sửa" (nguoi duyet da sua truc tiep o) va Mức khac ĐỎ.
Cap Task_ID KTC-<nam>-<ky>-<5 so> lien tuc toan Truong (20-Chuan-Chung/11-Quy-Tac-Task-ID.md), khong dung
lai so. Ghi 03-Lich-su-thay-doi. Ghi nguoc Task_ID vao so cho duyet. Sao luu Master truoc khi ghi.
Chong nap hai lan: khoa (Can_Cu_So_Hieu, Can_Cu_Dieu_Khoan, Don_Vi_Chu_Tri/Goc).
Ghi chú duyệt "đã xong 1007/KH-CĐKT" -> Trang_Thai Đã hoàn thành, Minh_Chung = văn bản đó.

  python 29-Cong-Cu/nap_master.py --nguoi "Nguyễn Ngọc Quang Phục" [--so-duyet <tệp>] [--thu]
"""
import argparse
import glob
import os
import re
import shutil
import sys
from datetime import datetime

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kiem_trich_nhiem_vu import MASTER, MASTER_DIR, doc_ngay  # noqa: E402

DONG_DAU = 4          # Master: hang 1 ten truong, 2 nhom, 3 bat buoc, du lieu tu hang 4
DUYET = ('Đồng ý', 'Sửa')


def ky_id(ky):
    """'2026-T10' -> ('2026', 'T10'); '2026-Q4' -> ('2026', 'Q4')."""
    m = re.match(r'^(\d{4})-(T\d{2}|Q[1-4]|NAM|CD)$', str(ky or ''))
    return (m.group(1), m.group(2)) if m else (None, None)


def main():
    ap = argparse.ArgumentParser(description='Nạp nhiệm vụ đã duyệt vào Master Task Register')
    ap.add_argument('--nguoi', required=True, help='Người duyệt/nạp (ghi vào lịch sử)')
    ap.add_argument('--so-duyet', help='Tệp Cho-duyet_*.xlsx (mặc định: mới nhất)')
    ap.add_argument('--master', default=MASTER)
    ap.add_argument('--thu', action='store_true', help='Chạy thử, không ghi')
    a = ap.parse_args()

    so_duyet = a.so_duyet or max(glob.glob(os.path.join(MASTER_DIR, 'Cho-duyet_*.xlsx')) or [''],
                                 key=lambda p: os.path.getmtime(p) if p else 0)
    if not so_duyet:
        print('Không có sổ chờ duyệt.')
        return 1
    wd = openpyxl.load_workbook(so_duyet)
    wsd = wd['Chờ duyệt']
    hd = [c.value for c in wsd[1]]
    cd = {t: i + 1 for i, t in enumerate(hd)}

    wm = openpyxl.load_workbook(a.master)
    wsm = wm['01-Master-Task-Register']
    hm = [c.value for c in wsm[1]]
    cm = {t: i + 1 for i, t in enumerate(hm) if t}
    ls = wm['03-Lich-su-thay-doi']

    da_co, so_max = set(), 0
    for r in range(DONG_DAU, wsm.max_row + 1):
        tid = wsm.cell(r, cm['Task_ID']).value
        if not tid:
            continue
        so_max = max(so_max, int(str(tid)[-5:]) if str(tid)[-5:].isdigit() else 0)
        da_co.add((wsm.cell(r, cm['Can_Cu_So_Hieu']).value, wsm.cell(r, cm['Can_Cu_Dieu_Khoan']).value,
                   wsm.cell(r, cm['Don_Vi_Chu_Tri']).value or ''))

    bay_gio = datetime.now()
    nap, bo, ma_tam_id = [], [], {}
    hang_duyet = [r for r in range(2, wsd.max_row + 1)
                  if wsd.cell(r, cd['Quyết định']).value in DUYET and not wsd.cell(r, cd['Task_ID']).value]
    # Cha truoc con: dong khong co Parent nap truoc de con tro duoc Parent_Task_ID
    hang_duyet.sort(key=lambda r: bool(wsd.cell(r, cd['Parent']).value))
    for r in hang_duyet:
        g = {t: wsd.cell(r, c).value for t, c in cd.items()}
        so = g['Số ký hiệu']
        if g['Mức'] == 'ĐỎ':
            bo.append('%s %s: còn cờ ĐỎ — sửa và chạy lại kiem_trich_nhiem_vu.py' % (so, g['Ma_Tam']))
            continue
        nam, ky = ky_id(g['Ky_Ke_Hoach'])
        if not nam:
            bo.append('%s %s: Kỳ kế hoạch sai (%s)' % (so, g['Ma_Tam'], g['Ky_Ke_Hoach']))
            continue
        khoa = (so, g['Can_Cu_Dieu_Khoan'], g['Don_Vi_Chu_Tri'] or '')
        if khoa in da_co:
            bo.append('%s %s: đã có trong Master' % (so, g['Ma_Tam']))
            continue
        so_max += 1
        tid = 'KTC-%s-%s-%05d' % (nam, ky, so_max)
        ma_tam_id[(so, g['Ma_Tam'])] = tid
        han = g['Han_Hoan_Thanh']
        ghi_chu_ct = '' if g['Don_Vi_Chu_Tri'] else ' · chủ trì nguyên văn: %s' % g['Don_Vi_Chu_Tri_Goc']
        hang = {
            'Task_ID': tid,
            'Parent_Task_ID': ma_tam_id.get((so, g['Parent'])) if g['Parent'] else None,
            'Ma_NV_Chuan': g['Ma_NV_Chuan'] or None,
            'Plan_ID': so,
            'Ten_Nhiem_Vu': g['Ten_Nhiem_Vu'],
            'Mo_Ta': (g['Mo_Ta'] or '') + ghi_chu_ct,
            'San_Pham_Yeu_Cau': g['San_Pham_Yeu_Cau'],
            'So_Luong': g['So_Luong'],
            'Can_Cu_So_Hieu': so,
            'Can_Cu_Ngay': g['Ngay_Ban_Hanh'],
            'Can_Cu_Co_Quan': g['Co_Quan'],
            'Can_Cu_Dieu_Khoan': g['Can_Cu_Dieu_Khoan'],
            'Nguon_Phat_Sinh': 'Văn bản iOffice %s — dòng %s' % (so, g['Dong']),
            'Don_Vi_Chu_Tri': g['Don_Vi_Chu_Tri'] or None,
            'Don_Vi_Phoi_Hop': g['Don_Vi_Phoi_Hop'] or None,
            'Nguoi_Chi_Dao': g['Nguoi_Chi_Dao'] or None,
            'Ky_Ke_Hoach': g['Ky_Ke_Hoach'],
            'Han_Hoan_Thanh': han,
            'Trang_Thai': 'Đã giao' if g['Don_Vi_Chu_Tri'] and doc_ngay(han) else 'Mới',
            'Phan_Tram_Tien_Do': 0,
            'Truc': g['Truc'],
            'Noi_Ham': g['Noi_Ham'],
            'Da_Bao_Cao': 'Không',
            'Ngay_Cap_Nhat': bay_gio.strftime('%d/%m/%Y'),
            'Nguoi_Cap_Nhat': a.nguoi,
            'Lich_Su': '%s: tạo từ %s mục %s (duyệt: %s%s)' % (
                bay_gio.strftime('%d/%m/%Y'), so, g['Can_Cu_Dieu_Khoan'], g['Quyết định'],
                ' — ' + g['Ghi chú duyệt'] if g['Ghi chú duyệt'] else ''),
        }
        # Nguoi duyet xac nhan "đã xong <số VB>" (thuong tu co CÓ THỂ ĐÃ XONG) -> hoan thanh, minh chung = VB do
        m = re.search(r'đã xong\W*(\d+/[A-ZĐ]+-[A-ZĐ]+)', str(g['Ghi chú duyệt'] or ''), re.I)
        if m:
            hang.update(Trang_Thai='Đã hoàn thành', Phan_Tram_Tien_Do=100, Minh_Chung=m.group(1),
                        San_Pham_Dat_Duoc=m.group(1))
        nap.append((r, hang))
        da_co.add(khoa)

    if not a.thu and nap:
        sao_luu = os.path.join(MASTER_DIR, '_sao-luu')
        os.makedirs(sao_luu, exist_ok=True)
        shutil.copy2(a.master, os.path.join(sao_luu, '%s_%s.xlsx' % (
            os.path.splitext(os.path.basename(a.master))[0], bay_gio.strftime('%Y%m%d-%H%M%S'))))
        for r, hang in nap:
            dm = max(wsm.max_row + 1, DONG_DAU)
            for t, v in hang.items():
                if t in cm:
                    wsm.cell(dm, cm[t], v)
            ls.append([hang['Task_ID'], '(tạo mới)', None, 'Nạp từ văn bản giao việc đã duyệt',
                       '%s mục %s' % (hang['Can_Cu_So_Hieu'], hang['Can_Cu_Dieu_Khoan']), a.nguoi,
                       bay_gio.strftime('%d/%m/%Y %H:%M'), hang['Ten_Nhiem_Vu']])
            wsd.cell(r, cd['Task_ID'], hang['Task_ID'])
        wm.save(a.master)
        wd.save(so_duyet)

    print('=== %sNẠP MASTER — %d nhiệm vụ · bỏ qua %d ===' % ('[CHẠY THỬ] ' if a.thu else '', len(nap), len(bo)))
    for _, h in nap:
        print('  %s  %-8s %-10s %s' % (h['Task_ID'], h['Don_Vi_Chu_Tri'] or '?', h['Han_Hoan_Thanh'] or '—',
                                       h['Ten_Nhiem_Vu'][:70]))
    for x in bo:
        print('  - bỏ qua: ' + x)
    return 0


if __name__ == '__main__':
    sys.exit(main())
