#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
so_sanh_ban.py – So sánh hai bản dự thảo .docx theo đoạn (Skill ktc-ra-soat-897 v4.5)

Dùng cho: tác vụ (c) so sánh hai bản; chế độ ĐC (Bước 5) – liệt kê mọi đoạn thay đổi
giữa bản lần trước và bản hiện hành. Thuật toán cố định (difflib, so theo đoạn đã chuẩn
hóa khoảng trắng), nên mọi lần chạy cho cùng kết quả.

Cách dùng:
  python3 so_sanh_ban.py <ban_cu.docx> <ban_moi.docx> [--json out.json] [--md out.md]
Kết quả: bảng các thay đổi – Thêm / Xóa / Sửa – kèm số đoạn hai bản và chi tiết từ ngữ
thay đổi (dạng [-bỏ-] {+thêm+}); thống kê; danh sách Điều/khoản bị ảnh hưởng.
"""
import sys, re, json, zipfile, argparse, difflib, unicodedata
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def norm(s): return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s or '').replace('\xa0', ' ')).strip()


def doan(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('word/document.xml'))
        out = []
        for p in root.iter(W + 'p'):
            t = norm(''.join((x.text or '') if x.tag == W + 't' else ' ' for x in p.iter() if x.tag in (W + 't', W + 'tab', W + 'br')))
            if t: out.append(t)
        for nm in ('word/footnotes.xml', 'word/endnotes.xml'):
            if nm in z.namelist():
                for p in ET.fromstring(z.read(nm)).iter(W + 'p'):
                    t = norm(''.join(x.text or '' for x in p.iter(W + 't')))
                    if t: out.append('[Chú thích] ' + t)
    return out


def tu_diff(a, b):
    wa, wb = a.split(' '), b.split(' ')
    sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            seg = wa[i1:i2]
            out.append(' '.join(seg) if len(seg) <= 8 else ' '.join(seg[:3]) + ' … ' + ' '.join(seg[-3:]))
        else:
            if i2 > i1: out.append('[-' + ' '.join(wa[i1:i2]) + '-]')
            if j2 > j1: out.append('{+' + ' '.join(wb[j1:j2]) + '+}')
    return ' '.join(out)


def dieu_cua(ds, i):
    """Vị trí: phần văn bản (Quyết định / Quy định… / Phụ lục) + Điều gần nhất; chú thích ghi riêng (PB2-16)."""
    if ds[i].startswith('[Chú thích]'): return 'Chú thích'
    dieu = None
    for k in range(i, -1, -1):
        if dieu is None:
            m = re.match(r'^(Điều\s+\d+)', ds[k])
            if m: dieu = m.group(1)
        m2 = re.match(r'^(QUY ĐỊNH|QUY CHẾ|ĐIỀU LỆ|NỘI QUY|QUY TRÌNH|HƯỚNG DẪN)$', ds[k])
        m3 = re.match(r'^(phụ lục\s+[IVXLC\d]+)', ds[k], re.I)
        if m2 or m3:
            phan = (m2.group(1).capitalize() if m2 else m3.group(1).capitalize())
            return phan + (' – ' + dieu if dieu else '')
    return ('Văn bản chính – ' + dieu) if dieu else '(phần đầu)'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cu'); ap.add_argument('moi'); ap.add_argument('--json'); ap.add_argument('--md')
    a = ap.parse_args()
    A, B = doan(a.cu), doan(a.moi)
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    rows = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': continue
        if op == 'replace':
            # ghép cặp theo độ giống lớn nhất (giữ thứ tự), không ghép theo vị trí (PB2-16)
            cap, j0 = {}, j1
            for ia in range(i1, i2):
                best, bj = 0.0, None
                for jb in range(j0, j2):
                    r = difflib.SequenceMatcher(None, A[ia], B[jb]).ratio()
                    if r > best: best, bj = r, jb
                if bj is not None and best >= 0.5:
                    cap[ia] = (bj, best); j0 = bj + 1
            used = {v[0] for v in cap.values()}
            jb_ptr = j1
            for ia in range(i1, i2):
                if ia in cap:
                    bj, r = cap[ia]
                    for jb in range(jb_ptr, bj):
                        if jb not in used: rows.append(dict(loai='Thêm', doan_cu=None, doan_moi=jb + 1, vi_tri=dieu_cua(B, jb), noi_dung=B[jb], ty_le_giong=None))
                    jb_ptr = bj + 1
                    rows.append(dict(loai='Sửa', doan_cu=ia + 1, doan_moi=bj + 1, vi_tri=dieu_cua(B, bj), noi_dung=tu_diff(A[ia], B[bj]), ty_le_giong=round(r, 2)))
                else:
                    rows.append(dict(loai='Xóa', doan_cu=ia + 1, doan_moi=None, vi_tri=dieu_cua(A, ia), noi_dung=A[ia], ty_le_giong=None))
            for jb in range(jb_ptr, j2):
                if jb not in used: rows.append(dict(loai='Thêm', doan_cu=None, doan_moi=jb + 1, vi_tri=dieu_cua(B, jb), noi_dung=B[jb], ty_le_giong=None))
        elif op == 'delete':
            for ia in range(i1, i2):
                rows.append(dict(loai='Xóa', doan_cu=ia + 1, doan_moi=None, vi_tri=dieu_cua(A, ia), noi_dung=A[ia], ty_le_giong=None))
        elif op == 'insert':
            for jb in range(j1, j2):
                rows.append(dict(loai='Thêm', doan_cu=None, doan_moi=jb + 1, vi_tri=dieu_cua(B, jb), noi_dung=B[jb], ty_le_giong=None))
    tk = {k: sum(1 for r in rows if r['loai'] == k) for k in ('Sửa', 'Thêm', 'Xóa')}
    vt = sorted(set(r['vi_tri'] for r in rows), key=lambda x: (len(x), x))
    out = ['# So sánh hai bản dự thảo', '', '- Bản cũ: %s (%d đoạn)' % (a.cu.rsplit('/', 1)[-1], len(A)),
           '- Bản mới: %s (%d đoạn)' % (a.moi.rsplit('/', 1)[-1], len(B)),
           '- Thay đổi: %d sửa, %d thêm, %d xóa; tỷ lệ giống toàn văn %.2f' % (tk['Sửa'], tk['Thêm'], tk['Xóa'], sm.ratio()),
           '- Vị trí bị ảnh hưởng: %s' % (', '.join(vt) or 'không có'), '',
           '| # | Loại | Đoạn cũ | Đoạn mới | Vị trí | Nội dung thay đổi |', '|---|---|---|---|---|---|']
    for i, r in enumerate(rows, 1):
        out.append('| %d | %s | %s | %s | %s | %s |' % (i, r['loai'], r['doan_cu'] or '', r['doan_moi'] or '', r['vi_tri'], r['noi_dung'].replace('|', '/')[:600]))
    out.append('')
    out.append('Ghi chú: [-…-] là chữ bị bỏ, {+…+} là chữ thêm. Định dạng (cỡ chữ, lề, số trang) không so ở đây – đo bằng kiem_tra_the_thuc.py trên từng bản.')
    md = '\n'.join(out)
    print(md)
    if a.md: open(a.md, 'w', encoding='utf-8').write(md)
    if a.json:  # v4.5 (PB5-WORK-16): ghi mã băm hai tệp để tao_bao_cao.py kiểm đúng cặp đã qua cổng hồ sơ
        import hashlib
        sh_ = lambda p_: hashlib.sha256(open(p_, 'rb').read()).hexdigest()
        json.dump(dict(cu=a.cu, moi=a.moi, sha256_cu=sh_(a.cu), sha256_moi=sh_(a.moi), thong_ke=tk, vi_tri=vt, thay_doi=rows), open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
