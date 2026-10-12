# -*- coding: utf-8 -*-
"""Dựng BỘ KẾT QUẢ CHẠY TRƯỚC cho Phần 1, Phần 2 buổi trình diễn 17/10/2026 từ bộ dữ liệu giả định D1–D3.
Đọc bằng công cụ thật của hệ (read_bc736_excel.py, cấu trúc tệp xuất QLVB&ĐH); so khớp nhiệm vụ bằng thuật toán cố định
(độ giống theo từ khóa) — kết quả là GỢI Ý, người tổng hợp quyết định. Không đọc tệp đáp án.
Chạy: python ket_qua_chay_truoc.py  -> Ket-qua-chay-truoc/
"""
import datetime as dt
import glob
import os
import re
import sys
import unicodedata

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

D = os.path.dirname(os.path.abspath(__file__))
DUAN = os.path.abspath(os.path.join(D, '..', '..', '..'))
sys.path.insert(0, os.path.join(DUAN, '25-KTC-Bao-Cao', 'references', 'Skill-Library'))
sys.path.insert(0, D)
import read_bc736_excel as R          # noqa: E402
import tao_du_lieu_gia_dinh as G      # noqa: E402  (chỉ dùng hàm dựng Word/Excel, không dùng dữ liệu, không dùng đáp án)

sys.stdout.reconfigure(encoding='utf-8')
DL = os.path.join(D, 'Du-lieu-gia-dinh')
RA = os.path.join(D, 'Ket-qua-chay-truoc')
NHAN = 'Kết quả chạy trước trên bộ dữ liệu giả định — do công cụ tạo, người tổng hợp phải kiểm tra'
F = lambda dam=False, nghieng=False: Font(name='Times New Roman', size=12, bold=dam, italic=nghieng)
VIEN = Border(*(Side(style='thin'),) * 4)
NEN = PatternFill('solid', fgColor='D9E2F3')
BO = set('và của các cho trong về theo tại từ đến với là có được một những này khi v/v gửi trước ngày sau trên'.split())


def cap_tu(s):
    """Tập các cặp từ liền nhau (bỏ hư từ, bỏ phần trong ngoặc, bỏ chữ số)."""
    s = re.sub(r'\(.*?\)', '', unicodedata.normalize('NFC', str(s or '')).lower())
    t = [w for w in re.findall(r'[a-zà-ỹđ]+', s) if w not in BO]
    return set(zip(t, t[1:]))


def giong(a, b):
    """Độ giống 0–1 theo cặp từ chung (hệ số Dice). Từ 0,60: Khớp rõ; 0,45–0,59: Nghi vấn, cần người xem; dưới 0,45: Không khớp."""
    A, B = cap_tu(a), cap_tu(b)
    return 2 * len(A & B) / (len(A) + len(B)) if A and B else 0.0


RO, NGHI = 0.60, 0.45


def doc_phu_luc(tep):
    a = R.read_appendix(tep)
    ws = load_workbook(tep, data_only=True).active
    tieu_de = ' '.join(str(ws.cell(r, 1).value or '') for r in range(1, 6))
    dv = re.search(r'ĐƠN VỊ:\s*(.+)', str(ws['A3'].value or ''))
    nv = [dict(t, truc=k) for k, v in a['truc'].items() for t in v]
    return a, tieu_de, (dv.group(1).strip() if dv else os.path.basename(tep)), nv


def lay(t, *khoa):
    for k in khoa:
        if t.get(k) not in (None, ''):
            return t[k]
    return None


def bang(ws, tieu_de, cot, rong, hang, ghi_chu=None):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(cot))
    c = ws.cell(1, 1, tieu_de); c.font = F(True); c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws.row_dimensions[1].height = 34
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(cot))
    c = ws.cell(2, 1, ghi_chu or NHAN); c.font = F(nghieng=True); c.alignment = Alignment(horizontal='center', wrap_text=True)
    for j, (t, w) in enumerate(zip(cot, rong), 1):
        c = ws.cell(4, j, t); c.font = F(True); c.fill = NEN; c.border = VIEN
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        ws.column_dimensions[get_column_letter(j)].width = w
    for i, h in enumerate(hang, 5):
        for j, v in enumerate(h, 1):
            c = ws.cell(i, j, v); c.font = F(); c.border = VIEN
            c.alignment = Alignment(horizontal='left' if isinstance(v, str) and len(v) > 14 else 'center', vertical='center', wrap_text=True)
    ws.page_setup.orientation, ws.page_setup.paperSize = 'landscape', 9
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.freeze_panes = 'A5'


def doc_qlvb():
    tep = glob.glob(os.path.join(DL, 'D2-*', '*.xlsx'))[0]
    ws = load_workbook(tep, data_only=True).active
    hd = None
    for r in ws.iter_rows(min_row=1, max_row=8):
        v = [str(c.value or '').strip().lower() for c in r]
        if 'trích yếu' in v:
            hd = {x: i for i, x in enumerate(v)}; d0 = r[0].row; break
    out = []
    for r in ws.iter_rows(min_row=d0 + 1, values_only=True):
        if r[hd['trích yếu']]:
            ng = r[hd['ngày ban hành']]
            out.append({'so': r[hd['số ký hiệu']], 'loai': r[hd['loại văn bản']], 'ty': r[hd['trích yếu']], 'cq': r[hd['cơ quan ban hành']],
                        'ngay': ng.strftime('%d/%m/%Y') if isinstance(ng, dt.datetime) else str(ng)})
    return out


# ============================================================ PHẦN 1 — tổng hợp kế hoạch quý IV
def phan_1(vb):
    ds = sorted(glob.glob(os.path.join(DL, 'D1-*', '*.xlsx')))
    kiem, thieu, tat_ca = [], [], []
    for tep in ds:
        a, td, dv, nv = doc_phu_luc(tep)
        loi = []
        dung_mau = 'quý' in td.lower() and a.get('kind') == 'KH'
        if not dung_mau:
            loi.append('Nộp theo mẫu kế hoạch THÁNG (Phụ lục Ib, tiêu đề “công tác tháng 10 năm 2026”), không phải mẫu kế hoạch QUÝ (Phụ lục Ia)'
                       if 'tháng' in td.lower() else 'Không nhận ra mẫu kế hoạch quý')
        n_h = n_s = 0
        for stt, t in enumerate(nv, 1):
            t['tt'] = f"Trục {t['truc']}, dòng {stt}"
            han, sp = lay(t, 'thoi_gian_ht', 'thoi_gian', 'han'), lay(t, 'san_pham')
            t['don_vi_nop'], t['han'], t['sp'] = dv, han, sp
            if not han:
                n_h += 1; thieu.append([dv, t.get('tt'), t.get('noi_dung'), 'Thiếu thời gian hoàn thành', 'Đề nghị đơn vị bổ sung'])
            if not sp:
                n_s += 1; thieu.append([dv, t.get('tt'), t.get('noi_dung'), 'Thiếu sản phẩm/công việc', 'Đề nghị đơn vị bổ sung'])
        if n_h:
            loi.append(f'{n_h:02d} nhiệm vụ thiếu thời gian hoàn thành')
        if n_s:
            loi.append(f'{n_s:02d} nhiệm vụ thiếu sản phẩm')
        loi += [str(x)[:120] for x in a.get('canh_bao', [])]
        kiem.append([len(kiem) + 1, dv, os.path.basename(tep), 'Phụ lục Ia (quý)' if dung_mau else 'Phụ lục Ib (tháng)', len(nv),
                     sum(1 for t in nv if R._norm(t.get('ghi_chu')) == R.GHI_CHU_LOC_LEN_TRUONG), '; '.join(loi) or 'Không',
                     'Trả lại đơn vị (sai mẫu)' if not dung_mau else ('Đủ điều kiện tổng hợp, cần bổ sung' if loi else 'Đủ điều kiện tổng hợp')])
        tat_ca += nv
    # trùng giữa hai đơn vị
    trung = []
    for i, x in enumerate(tat_ca):
        for y in tat_ca[i + 1:]:
            if x['don_vi_nop'] != y['don_vi_nop'] and x['truc'] == y['truc']:
                g = giong(x['noi_dung'], y['noi_dung'])
                if g >= NGHI:
                    trung.append([len(trung) + 1, x['don_vi_nop'], x['noi_dung'], y['don_vi_nop'], y['noi_dung'], round(g, 2),
                                  'Trùng rõ: Xác định 01 đơn vị chủ trì, đơn vị còn lại phối hợp' if g >= RO
                                  else 'Nghi trùng: Người tổng hợp xem lại hai nội dung'])
    # đối chiếu văn bản chỉ đạo của cấp trên
    dc = []
    for v in vb:
        if 'cấp trên' not in str(v['cq']).lower():
            continue
        d = dt.datetime.strptime(v['ngay'], '%d/%m/%Y')
        han = re.search(r'trước ngày (\d{1,2}/\d{1,2}/\d{4})', v['ty'])
        if d < dt.datetime(2026, 7, 1) and not han:
            continue
        tot = max(tat_ca, key=lambda t: giong(v['ty'], t['noi_dung']))
        g = giong(v['ty'], tot['noi_dung'])
        co = g >= NGHI
        dc.append([len(dc) + 1, v['so'], v['ngay'], v['ty'], han.group(1) if han else '', tot['don_vi_nop'] if co else '', tot['noi_dung'] if co else '',
                   round(g, 2), ('Đã có trong dự thảo kế hoạch' if g >= RO else 'Có nhiệm vụ gần giống — cần xác nhận') if co
                   else ('CHƯA đơn vị nào đăng ký — đề nghị phân công' if han else 'Không thấy nhiệm vụ tương ứng; văn bản không nêu thời hạn — tham khảo')])
    # dự thảo kế hoạch quý của cơ quan: nhiệm vụ “Đưa vào KH Trường”, bỏ đơn vị sai mẫu khỏi phần chính thức nhưng giữ để theo dõi
    sai_mau = {k[1] for k in kiem if k[7].startswith('Trả lại')}
    da_trung = {(t[3], t[4]) for t in trung if t[5] >= RO}
    kh = [(t['truc'], t['noi_dung'], t['don_vi_nop'], t['sp'], lay(t, 'so_luong'), lay(t, 'do_kho'), t['han'],
           ('Chờ đơn vị nộp lại đúng mẫu' if t['don_vi_nop'] in sai_mau else '') +
           ('Trùng với nhiệm vụ của đơn vị khác — chờ phân công chủ trì' if (t['don_vi_nop'], t['noi_dung']) in da_trung else ''))
          for t in tat_ca if R._norm(t.get('ghi_chu')) == R.GHI_CHU_LOC_LEN_TRUONG]
    wb = Workbook()
    bang(wb.active, 'BẢNG KIỂM HỒ SƠ DỰ THẢO KẾ HOẠCH CÔNG TÁC QUÝ IV NĂM 2026 CỦA CÁC ĐƠN VỊ',
         ['TT', 'Đơn vị', 'Tệp nộp', 'Mẫu nhận diện', 'Số nhiệm vụ', 'Đưa vào kế hoạch cơ quan', 'Vấn đề phát hiện', 'Kết luận'],
         [5, 26, 36, 18, 10, 12, 60, 26], kiem)
    wb.active.title = '1-Bang-kiem'
    bang(wb.create_sheet('2-Thieu-thong-tin'), 'NHIỆM VỤ THIẾU THỜI GIAN HOÀN THÀNH HOẶC SẢN PHẨM',
         ['Đơn vị', 'TT trong tệp', 'Nội dung công việc', 'Thiếu', 'Đề xuất'], [26, 10, 70, 28, 26], thieu)
    bang(wb.create_sheet('3-Trung-lap'), 'NHIỆM VỤ CÓ DẤU HIỆU TRÙNG GIỮA HAI ĐƠN VỊ (so khớp theo từ khóa — gợi ý)',
         ['TT', 'Đơn vị thứ nhất', 'Nội dung', 'Đơn vị thứ hai', 'Nội dung', 'Độ giống', 'Đề xuất'], [5, 22, 48, 22, 48, 9, 34], trung)
    bang(wb.create_sheet('4-Doi-chieu-van-ban'), 'ĐỐI CHIẾU VĂN BẢN CHỈ ĐẠO CỦA CẤP TRÊN (HỆ THỐNG QUẢN LÝ VĂN BẢN VÀ ĐIỀU HÀNH) VỚI DỰ THẢO KẾ HOẠCH',
         ['TT', 'Số, ký hiệu', 'Ngày', 'Trích yếu', 'Thời hạn nêu trong văn bản', 'Đơn vị đã đăng ký', 'Nhiệm vụ gần nhất trong dự thảo', 'Độ giống', 'Nhận định'],
         [5, 16, 12, 56, 14, 22, 46, 9, 34], dc)
    ws = wb.create_sheet('5-Du-thao-KH-quy')
    hang, tt = [], 0
    for k in range(1, 7):
        hang.append([k, G.TRUC[k], '', '', '', '', '', ''])
        for i, (_, nd, dv, sp, sl, dk, han, gc) in enumerate([x for x in kh if x[0] == k], 1):
            hang.append([f'{k}.{i}', nd, dv, sp or '(đơn vị chưa ghi)', sl, dk, han or '(đơn vị chưa ghi)', gc])
    bang(ws, 'DỰ THẢO KẾ HOẠCH CÔNG TÁC QUÝ IV NĂM 2026 CỦA CƠ QUAN A (tổng hợp các nhiệm vụ đơn vị đề nghị đưa vào kế hoạch cơ quan)',
         ['TT', 'Nội dung công việc', 'Đơn vị đề xuất (nguồn)', 'Sản phẩm', 'Số lượng', 'Độ khó', 'Thời gian hoàn thành', 'Ghi chú của bộ phận tổng hợp'],
         [7, 60, 26, 18, 9, 16, 16, 40], hang)
    for r in ws.iter_rows(min_row=5):
        if isinstance(r[0].value, int):
            for c in r:
                c.font = F(True)
    tep = os.path.join(RA, 'Phan-1_Tong-hop-ke-hoach-quy-IV-2026_ket-qua-chay-truoc.xlsx')
    wb.save(tep)
    return dict(tep=tep, don_vi=len(ds), nv=len(tat_ca), tra_lai=[k[1] for k in kiem if k[7].startswith('Trả')], thieu=len(thieu), trung=len(trung),
                chua_dk=[x[1] for x in dc if x[8].startswith('CHƯA')], vb=len(dc), kh=len(kh))


# ============================================================ PHẦN 2 — báo cáo tháng 9
def phan_2(vb):
    a_kh, _, _, kh = doc_phu_luc(glob.glob(os.path.join(DL, 'D3-*', '00_Ke-hoach*.xlsx'))[0])
    bc, kpi = [], {k: dict(n=0, sl=0.0, tt=0.0, cl=0.0, td=0.0) for k in range(1, 7)}
    for tep in sorted(glob.glob(os.path.join(DL, 'D3-*', '*_Bao-cao-thang-9-2026.xlsx'))):
        a, _, dv, nv = doc_phu_luc(tep)
        for t in nv:
            t['don_vi_nop'] = dv
        bc += nv
        for k, s in R.summarize_truc_kpi(a).items():
            kpi[k]['n'] += s['so_nhiem_vu']; kpi[k]['sl'] += s['so_luong']; kpi[k]['tt'] += s['kpi_sl_tt']
            kpi[k]['cl'] += s['kpi_cl_tt']; kpi[k]['td'] += s['kpi_td_tt']
    dc, khong = [], []
    for t in kh:
        dvct = lay(t, 'don_vi_chu_tri', 'don_vi') or ''
        ung = sorted(((giong(t['noi_dung'], b['noi_dung']), b) for b in bc), key=lambda x: -x[0])
        khop = [(g, b) for g, b in ung if g >= RO]
        if not khop:
            mc = max(vb, key=lambda v: giong(t['noi_dung'], v['ty']))
            g = giong(t['noi_dung'], mc['ty'])
            co = g >= RO and 'cơ quan a' in str(mc['cq']).lower()
            dong = [len(dc) + 1, t['noi_dung'], dvct, 'CHƯA CÓ THÔNG TIN trong báo cáo đơn vị', '',
                    f"Có thể đã thực hiện: {mc['loai']} số {mc['so']} ngày {mc['ngay']} — {mc['ty']} (đề nghị đơn vị xác nhận)" if co
                    else 'Không thấy văn bản liên quan trên Hệ thống — đề nghị đơn vị báo cáo bổ sung']
            khong.append(dong)
        else:
            dvs = sorted({b['don_vi_nop'] for _, b in khop})
            so = sorted({m for _, b in khop for m in re.findall(r'(\d+)\s+lượt người', str(b['noi_dung']))})
            ghi = []
            if len(dvs) > 1 and not any('phối hợp' in str(b['noi_dung']).lower() for _, b in khop):
                ghi.append(f'{len(dvs)} đơn vị cùng báo cáo là kết quả của mình: {", ".join(dvs)} — kế hoạch giao {dvct} chủ trì; chỉ tính 01 lần')
            if len(so) > 1:
                ghi.append(f'Số liệu KHÔNG thống nhất giữa các đơn vị: {" và ".join(so)} lượt người — đề nghị xác minh')
            dong = [len(dc) + 1, t['noi_dung'], dvct, 'Có báo cáo', '; '.join(f"{b['don_vi_nop']}: {b['noi_dung']}" for _, b in khop), '; '.join(ghi)]
        dc.append(dong)
    wb = Workbook()
    bang(wb.active, 'ĐỐI CHIẾU KẾ HOẠCH THÁNG 9 NĂM 2026 VỚI BÁO CÁO CỦA CÁC ĐƠN VỊ',
         ['TT', 'Nhiệm vụ theo kế hoạch tháng', 'Đơn vị chủ trì', 'Tình trạng', 'Nội dung đơn vị báo cáo (nguồn)', 'Ghi chú đối soát'],
         [5, 46, 22, 20, 70, 60], dc)
    wb.active.title = '1-Doi-chieu-KH-BC'
    for r in wb.active.iter_rows(min_row=5):
        if str(r[3].value).startswith('CHƯA') or r[5].value:
            for c in r:
                c.fill = PatternFill('solid', fgColor='FFF2CC')
    hang = []
    for k in range(1, 7):
        s = kpi[k]
        hang.append([G.TRUC[k], s['n'], round(s['sl'], 2), f"{s['tt'] / s['sl'] * 100:.1f}%" if s['sl'] else '-',
                     f"{s['cl'] / s['tt'] * 100:.1f}%" if s['tt'] else '-', f"{s['td'] / s['tt'] * 100:.1f}%" if s['tt'] else '-'])
    bang(wb.create_sheet('2-KPI-theo-truc'), 'TỶ LỆ HOÀN THÀNH THEO 06 TRỤC (cộng từ Phụ lục IIb của 06 đơn vị, chưa loại nội dung trùng)',
         ['Trục', 'Số dòng báo cáo', 'Số lượng kế hoạch', 'Hoàn thành khối lượng', 'Chất lượng', 'Tiến độ'], [80, 12, 12, 14, 12, 12], hang)
    tep = os.path.join(RA, 'Phan-2_Doi-chieu-ke-hoach-bao-cao-thang-9-2026_ket-qua-chay-truoc.xlsx')
    wb.save(tep)
    co = [d for d in dc if d[3] == 'Có báo cáo']
    # ---- dự thảo báo cáo tháng 9 của cơ quan, phát triển từ báo cáo tháng 8 đã ban hành (cùng bố cục, cùng lời văn)
    d = G.tai_lieu()
    G.phan_dau(d, '', G.CQ, 'Số:      /BC-CQA', 'Quảng Ngãi, ngày      tháng 10 năm 2026')
    G.doan(d, '', sau=0); G.doan(d, 'BÁO CÁO', dam=True, can='giua', sau=0)
    G.doan(d, 'Kết quả công tác tháng 9, nhiệm vụ trọng tâm tháng 10 năm 2026', dam=True, can='giua', sau=0); G.ke(d)
    G.doan(d, '(DỰ THẢO do công cụ tổng hợp từ báo cáo của 06 đơn vị; các chỗ đánh dấu [CẦN XÁC NHẬN] phải được kiểm tra trước khi trình)', nghieng=True, can='giua', co=12)
    G.doan(d, 'Thực hiện Kế hoạch công tác năm 2026, Kế hoạch công tác quý III/2026 và Kế hoạch số 270/KH-CQA ngày 28/8/2026, Cơ quan A báo cáo kết quả '
              'công tác tháng 9, nhiệm vụ trọng tâm tháng 10 năm 2026 như sau:')
    G.doan(d, 'I. KẾT QUẢ THỰC HIỆN NHIỆM VỤ THÁNG 9', dam=True)
    G.doan(d, f'Kế hoạch tháng 9 có {len(kh)} nhiệm vụ. Theo báo cáo của 06 đơn vị, {len(co)} nhiệm vụ có kết quả; {len(khong):02d} nhiệm vụ chưa có thông tin '
              f'trong báo cáo đơn vị [CẦN XÁC NHẬN]. Kết quả theo từng lĩnh vực:')
    ten = ['Thực hiện mục tiêu phát triển kinh tế - xã hội và nhiệm vụ chính trị được giao', 'Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát',
           'Thúc đẩy phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số', 'Xây dựng Đảng và hệ thống chính trị trong sạch, vững mạnh',
           'Phát triển văn hóa, con người, bảo đảm an sinh xã hội', 'Củng cố quốc phòng, an ninh, giữ vững ổn định chính trị - xã hội']
    for k in range(1, 7):
        G.doan(d, f'{k}. {ten[k - 1]}', dam=True)
        ds = [x for x in dc if any(t['noi_dung'] == x[1] and t['truc'] == k for t in kh)]
        cau = []
        for x in ds:
            if x[3] == 'Có báo cáo':
                nd = x[4].split('; ')[0].split(': ', 1)[1]
                cau.append(nd + (' [CẦN XÁC NHẬN: ' + x[5] + ']' if x[5] else '') + f' (nguồn: Báo cáo của {x[2] or x[4].split(":")[0]})')
            else:
                cau.append(f'Nhiệm vụ “{x[1]}” ({x[2]} chủ trì): Chưa có thông tin trong báo cáo đơn vị [CẦN XÁC NHẬN: {x[5]}]')
        G.doan(d, '; '.join(cau) + '.' if cau else 'Không có nhiệm vụ trong kế hoạch tháng.')
    G.doan(d, 'II. TỒN TẠI, HẠN CHẾ', dam=True)
    G.doan(d, f'Còn {len(khong):02d} nhiệm vụ trong kế hoạch tháng chưa được đơn vị báo cáo kết quả; một số nhiệm vụ hoàn thành chưa đủ khối lượng hoặc chậm '
              'tiến độ (thẩm định hồ sơ chuyên môn, triển khai chữ ký số, báo cáo tài chính quý III); Kế hoạch tuyển dụng viên chức năm 2026 đã trình, chưa được ban hành.')
    G.doan(d, 'III. NHIỆM VỤ TRỌNG TÂM THÁNG 10', dam=True)
    G.doan(d, '[CẦN BỔ SUNG từ Kế hoạch công tác quý IV/2026 sau khi được ban hành và từ Thông báo số 336/TB-CQA ngày 06/10/2026.]')
    G.doan(d, 'Trên đây là Báo cáo kết quả công tác tháng 9, nhiệm vụ trọng tâm tháng 10 năm 2026 của Cơ quan A./.')
    G.phan_ky(d, ['- Cơ quan cấp trên (báo cáo);', '- Lãnh đạo cơ quan;', '- Các đơn vị trực thuộc;', '- Lưu: VT, VP.'], 'THỦ TRƯỞNG CƠ QUAN', '', '')
    tep2 = os.path.join(RA, 'Phan-2_Du-thao-Bao-cao-thang-9-2026_Co-quan-A_ket-qua-chay-truoc.docx')
    d.save(tep2)
    return dict(tep=tep, tep2=tep2, kh=len(kh), co=len(co), khong=[x[1] for x in khong], ghi=[x[5] for x in dc if x[5] and x[3] == 'Có báo cáo'],
                mc=[x[5] for x in khong])


if __name__ == '__main__':
    os.makedirs(RA, exist_ok=True)
    vb = doc_qlvb()
    p1, p2 = phan_1(vb), phan_2(vb)
    print('PHẦN 1:', {k: v for k, v in p1.items() if k != 'tep'})
    print('PHẦN 2:', {k: v for k, v in p2.items() if not k.startswith('tep')})
