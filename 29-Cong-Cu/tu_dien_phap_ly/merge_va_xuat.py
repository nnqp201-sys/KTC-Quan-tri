# -*- coding: utf-8 -*-
"""
Merge các file JSON tăng dần và xuất Excel cho Từ điển pháp lý.
Chạy sau khi routine cập nhật dữ liệu mới.
"""

import json
from pathlib import Path
from datetime import datetime
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from duong_dan import ktc_database

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
except ImportError:
    print("Cần cài openpyxl: pip install openpyxl")
    sys.exit(1)


def thu_tu_van_ban(nguon: str) -> tuple:
    """
    Xác định thứ tự ưu tiên văn bản theo Luật BHVBQPPL.
    Trả về (cấp, năm) — cấp thấp hơn = ưu tiên cao hơn.
    """
    import re
    nguon_lower = nguon.lower()

    # Xác định cấp văn bản
    if 'hiến pháp' in nguon_lower:
        cap = 0
    elif 'luật' in nguon_lower and 'nghị định' not in nguon_lower:
        cap = 1
    elif 'pháp lệnh' in nguon_lower:
        cap = 2
    elif 'nghị định' in nguon_lower:
        cap = 3
    elif 'quyết định' in nguon_lower and ('thủ tướng' in nguon_lower or 'ttcp' in nguon_lower):
        cap = 4
    elif 'thông tư' in nguon_lower:
        cap = 5
    else:
        cap = 9

    # Trích năm ban hành
    match = re.search(r'(19|20)\d{2}', nguon)
    nam = int(match.group()) if match else 1900

    return (cap, -nam)  # năm mới hơn = số âm nhỏ hơn = ưu tiên


def merge_json_files():
    """
    Gộp tất cả file tu_dien_moi_*.json vào tu_dien_index.json.
    Xử lý trùng theo nguyên tắc pháp lý: văn bản cấp cao + mới hơn ưu tiên.
    """

    kho_path = Path(ktc_database()) / '08-Tu-Dien-Phap-Ly'
    if not kho_path.exists():
        print(f"Chưa có thư mục {kho_path}")
        return None

    # Đọc index hiện tại (nếu có)
    index_path = kho_path / 'tu_dien_index.json'
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
    else:
        index_data = {"records": [], "last_updated": None, "total": 0}

    existing = {r.get('Thuật ngữ', '').lower(): r for r in index_data.get('records', [])}

    # Tìm và merge các file tăng dần (cả tu_dien_moi_* và Tu-dien-phap-ly_v*)
    new_files = sorted(list(kho_path.glob('tu_dien_moi_*.json')) + list(kho_path.glob('Tu-dien-phap-ly_v*.json')))
    added = 0
    updated = 0

    for f in new_files:
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                data = json.load(fp)

            for rec in data.get('new_records', []):
                key = rec.get('Thuật ngữ', '').lower()
                if not key:
                    continue

                if key not in existing:
                    existing[key] = rec
                    added += 1
                else:
                    # So sánh ưu tiên: văn bản cấp cao + mới hơn thắng
                    old_rec = existing[key]
                    old_priority = thu_tu_van_ban(old_rec.get('Nguồn', ''))
                    new_priority = thu_tu_van_ban(rec.get('Nguồn', ''))

                    if new_priority < old_priority:
                        # Ghi chú nguồn cũ bị thay thế
                        ghi_chu = rec.get('Ghi chú', '') or ''
                        ghi_chu += f" [THAY THẾ: {old_rec.get('Nguồn', '')}]"
                        rec['Ghi chú'] = ghi_chu.strip()
                        rec['_xung_dot'] = True
                        existing[key] = rec
                        updated += 1
                    elif new_priority > old_priority:
                        # Giữ bản cũ, ghi chú có nguồn khác
                        ghi_chu = old_rec.get('Ghi chú', '') or ''
                        if '[THAM KHẢO:' not in ghi_chu:
                            ghi_chu += f" [THAM KHẢO: {rec.get('Nguồn', '')}]"
                            old_rec['Ghi chú'] = ghi_chu.strip()
                            old_rec['_xung_dot'] = True
        except Exception as e:
            print(f"Lỗi đọc {f.name}: {e}")

    # Cập nhật index
    index_data['records'] = list(existing.values())
    index_data['total'] = len(index_data['records'])
    index_data['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Lưu index
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    print(f"Đã merge: {added} mới, {updated} cập nhật, tổng {index_data['total']}")
    return index_data


def xuat_excel(index_data: dict):
    """Xuất từ điển ra Excel với dashboard."""

    kho_path = Path(ktc_database()) / '08-Tu-Dien-Phap-Ly'
    records = index_data.get('records', [])

    if not records:
        print("Không có dữ liệu để xuất.")
        return

    wb = Workbook()
    header_fill = PatternFill(start_color="0070C0", end_color="0070C0", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")

    # === Sheet 1: Dashboard ===
    ws_dash = wb.active
    ws_dash.title = "Dashboard"

    ws_dash.cell(row=1, column=1, value="TỪ ĐIỂN PHÁP LÝ").font = Font(bold=True, size=16)
    ws_dash.cell(row=2, column=1, value=f"Cập nhật: {index_data.get('last_updated', 'N/A')}")
    ws_dash.cell(row=3, column=1, value=f"Tổng: {len(records)} thuật ngữ").font = Font(bold=True)

    # Thống kê Trục
    by_truc = {}
    for r in records:
        truc = r.get('Trục', 'Chưa phân loại')
        by_truc[truc] = by_truc.get(truc, 0) + 1

    ws_dash.cell(row=5, column=1, value="THEO TRỤC").font = Font(bold=True, color="0070C0")
    row = 6
    for truc in ['Trục 1', 'Trục 2', 'Trục 3', 'Trục 4', 'Trục 5', 'Trục 6']:
        ws_dash.cell(row=row, column=1, value=truc)
        ws_dash.cell(row=row, column=2, value=by_truc.get(truc, 0))
        row += 1

    # Thống kê lĩnh vực
    by_lv = {}
    for r in records:
        lv = r.get('Lĩnh vực', 'Chưa phân loại')
        by_lv[lv] = by_lv.get(lv, 0) + 1

    ws_dash.cell(row=row+1, column=1, value="THEO LĨNH VỰC").font = Font(bold=True, color="0070C0")
    row += 2
    for lv in sorted(by_lv.keys()):
        ws_dash.cell(row=row, column=1, value=lv)
        ws_dash.cell(row=row, column=2, value=by_lv[lv])
        row += 1

    ws_dash.column_dimensions['A'].width = 20
    ws_dash.column_dimensions['B'].width = 10

    # Chú giải màu
    xung_dot_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
    ws_dash.cell(row=row+2, column=1, value="CHÚ GIẢI MÀU").font = Font(bold=True, color="0070C0")
    ws_dash.cell(row=row+3, column=1, value="Vàng nhạt").fill = xung_dot_fill
    ws_dash.cell(row=row+3, column=2, value="Có xung đột/thay thế — xem cột Ghi chú")

    # === Sheet 2: Dữ liệu ===
    ws = wb.create_sheet("Từ điển pháp lý")

    # Màu cho xung đột
    xung_dot_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")  # Vàng nhạt

    headers = ['STT', 'Thuật ngữ', 'Mô tả', 'Định nghĩa', 'Tình trạng hiệu lực',
               'Nguồn', 'Trục', 'Lĩnh vực', 'Ghi chú']

    for col, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=h)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

    for i, r in enumerate(records, 1):
        is_xung_dot = r.get('_xung_dot', False)
        ws.cell(row=i+1, column=1, value=i)
        ws.cell(row=i+1, column=2, value=r.get('Thuật ngữ', ''))
        ws.cell(row=i+1, column=3, value=r.get('Mô tả', ''))
        ws.cell(row=i+1, column=4, value=r.get('Định nghĩa', ''))
        ws.cell(row=i+1, column=5, value=r.get('Tình trạng hiệu lực', ''))
        ws.cell(row=i+1, column=6, value=r.get('Nguồn', ''))
        ws.cell(row=i+1, column=7, value=r.get('Trục', ''))
        ws.cell(row=i+1, column=8, value=r.get('Lĩnh vực', ''))
        ws.cell(row=i+1, column=9, value=r.get('Ghi chú', ''))

        # Tô màu vàng nếu có xung đột
        if is_xung_dot:
            for col in range(1, 10):
                ws.cell(row=i+1, column=col).fill = xung_dot_fill

    col_widths = [6, 25, 40, 60, 15, 30, 12, 15, 30]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # === Sheet 3-14: Theo lĩnh vực ===
    linh_vuc_map = {
        'giao-duc': 'Giáo dục-Đào tạo',
        'hssv': 'Học sinh-Sinh viên',
        'vien-chuc': 'Viên chức',
        'tien-luong': 'Tiền lương',
        'thue-phi': 'Thuế-Phí',
        'bao-hiem': 'Bảo hiểm',
        'dau-thau': 'Đấu thầu',
        'tai-san': 'Tài sản',
        'xay-dung': 'Xây dựng',
        'thi-dua': 'Thi đua-KT',
        'khcn': 'KHCN',
        'hanh-chinh': 'Hành chính',
        'khac': 'Lĩnh vực khác'
    }

    for lv_code, lv_name in linh_vuc_map.items():
        lv_records = [r for r in records if r.get('Lĩnh vực') == lv_code]
        if not lv_records:
            continue

        ws_lv = wb.create_sheet(lv_name[:20])  # Tên sheet tối đa 31 ký tự

        for col, h in enumerate(headers, 1):
            cell = ws_lv.cell(row=1, column=col, value=h)
            cell.fill = header_fill
            cell.font = header_font

        for i, r in enumerate(lv_records, 1):
            is_xung_dot = r.get('_xung_dot', False)
            ws_lv.cell(row=i+1, column=1, value=i)
            ws_lv.cell(row=i+1, column=2, value=r.get('Thuật ngữ', ''))
            ws_lv.cell(row=i+1, column=3, value=r.get('Mô tả', ''))
            ws_lv.cell(row=i+1, column=4, value=r.get('Định nghĩa', ''))
            ws_lv.cell(row=i+1, column=5, value=r.get('Tình trạng hiệu lực', ''))
            ws_lv.cell(row=i+1, column=6, value=r.get('Nguồn', ''))
            ws_lv.cell(row=i+1, column=7, value=r.get('Trục', ''))
            ws_lv.cell(row=i+1, column=8, value=r.get('Lĩnh vực', ''))
            ws_lv.cell(row=i+1, column=9, value=r.get('Ghi chú', ''))

            if is_xung_dot:
                for col in range(1, 10):
                    ws_lv.cell(row=i+1, column=col).fill = xung_dot_fill

        for i, w in enumerate(col_widths, 1):
            ws_lv.column_dimensions[get_column_letter(i)].width = w

    output_path = kho_path / 'Tu-dien-phap-ly.xlsx'
    wb.save(output_path)
    print(f"Đã xuất Excel: {output_path}")


def main():
    print("=== Merge và xuất Từ điển pháp lý ===")
    index_data = merge_json_files()
    if index_data:
        xuat_excel(index_data)


if __name__ == '__main__':
    main()
