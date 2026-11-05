# -*- coding: utf-8 -*-
"""
Xuất Từ điển pháp lý ra Excel với dashboard.
"""

import json
from pathlib import Path
from datetime import datetime
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from duong_dan import ktc_database

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    print("Cần cài openpyxl: pip install openpyxl")
    sys.exit(1)


def xuat_excel(output_path: str = None):
    """Xuất từ điển pháp lý ra file Excel."""

    # Đọc dữ liệu
    index_path = Path(ktc_database()) / '08-Tu-Dien-Phap-Ly/tu_dien_index.json'
    if not index_path.exists():
        print(f"Chưa có dữ liệu tại {index_path}")
        return None

    with open(index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = data.get('records', [])
    if not records:
        print("Không có thuật ngữ nào trong kho.")
        return None

    # Tạo workbook
    wb = Workbook()

    # === Sheet 1: Dữ liệu ===
    ws = wb.active
    ws.title = "Từ điển pháp lý"

    # Header
    headers = ['STT', 'Thuật ngữ', 'Mô tả', 'Định nghĩa', 'Tình trạng hiệu lực',
               'Nguồn', 'Trục', 'Lĩnh vực', 'Ghi chú']
    header_fill = PatternFill(start_color="0070C0", end_color="0070C0", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")

    for col, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=h)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

    # Dữ liệu
    for i, r in enumerate(records, 1):
        ws.cell(row=i+1, column=1, value=i)
        ws.cell(row=i+1, column=2, value=r.get('Thuật ngữ', ''))
        ws.cell(row=i+1, column=3, value=r.get('Mô tả', ''))
        ws.cell(row=i+1, column=4, value=r.get('Định nghĩa', ''))
        ws.cell(row=i+1, column=5, value=r.get('Tình trạng hiệu lực', ''))
        ws.cell(row=i+1, column=6, value=r.get('Nguồn', ''))
        ws.cell(row=i+1, column=7, value=r.get('Trục', ''))
        ws.cell(row=i+1, column=8, value=r.get('Lĩnh vực', ''))
        ws.cell(row=i+1, column=9, value=r.get('Ghi chú', ''))

    # Độ rộng cột
    col_widths = [6, 25, 40, 60, 15, 30, 12, 15, 30]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # === Sheet 2: Dashboard ===
    ws2 = wb.create_sheet("Thống kê")

    # Thống kê theo Trục
    by_truc = {}
    for r in records:
        truc = r.get('Trục', 'Chưa phân loại')
        by_truc[truc] = by_truc.get(truc, 0) + 1

    ws2.cell(row=1, column=1, value="Thống kê theo Trục").font = Font(bold=True, size=14)
    ws2.cell(row=2, column=1, value="Trục")
    ws2.cell(row=2, column=2, value="Số lượng")
    row = 3
    for truc, count in sorted(by_truc.items()):
        ws2.cell(row=row, column=1, value=truc)
        ws2.cell(row=row, column=2, value=count)
        row += 1

    # Thống kê theo lĩnh vực
    by_lv = {}
    for r in records:
        lv = r.get('Lĩnh vực', 'Chưa phân loại')
        by_lv[lv] = by_lv.get(lv, 0) + 1

    ws2.cell(row=row+1, column=1, value="Thống kê theo Lĩnh vực").font = Font(bold=True, size=14)
    ws2.cell(row=row+2, column=1, value="Lĩnh vực")
    ws2.cell(row=row+2, column=2, value="Số lượng")
    row += 3
    for lv, count in sorted(by_lv.items()):
        ws2.cell(row=row, column=1, value=lv)
        ws2.cell(row=row, column=2, value=count)
        row += 1

    ws2.column_dimensions['A'].width = 25
    ws2.column_dimensions['B'].width = 12

    # Lưu file
    if not output_path:
        output_dir = Path(__file__).parent / 'output'
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"Tu-dien-phap-ly_{datetime.now().strftime('%Y%m%d')}.xlsx"

    wb.save(output_path)
    print(f"Đã xuất {len(records)} thuật ngữ ra: {output_path}")
    return str(output_path)


if __name__ == '__main__':
    xuat_excel()
