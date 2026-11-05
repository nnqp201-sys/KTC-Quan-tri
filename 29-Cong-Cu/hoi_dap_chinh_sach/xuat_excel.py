# -*- coding: utf-8 -*-
"""
Xuất dữ liệu hỏi đáp từ JSON ra Excel với dashboard
Chạy: python xuat_excel.py
"""
import json
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from duong_dan import ktc_database

try:
    import pandas as pd
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
    from openpyxl.utils.dataframe import dataframe_to_rows
except ImportError:
    print("Cần cài: pip install pandas openpyxl")
    sys.exit(1)


def main():
    # Đọc JSON
    kho = Path(ktc_database()) / '07-Hoi-Dap-Chinh-Sach'
    json_path = kho / 'hoi_dap_index.json'

    if not json_path.exists():
        print(f"Không tìm thấy {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = data.get('records', [])
    if not records:
        print("Không có dữ liệu")
        return

    df = pd.DataFrame(records)

    # Tạo workbook
    wb = Workbook()

    # === Sheet DASHBOARD ===
    ws_dash = wb.active
    ws_dash.title = "DASHBOARD"

    # Thống kê theo Trục
    truc_count = {}
    for i in range(1, 7):
        truc_count[f'Trục {i}'] = 0
    truc_count['Khác'] = 0

    for r in records:
        truc = str(r.get('Trục', ''))
        matched = False
        for i in range(1, 7):
            if f'Trục {i}' in truc or f'({i})' in truc:
                truc_count[f'Trục {i}'] += 1
                matched = True
                break
        if not matched:
            truc_count['Khác'] += 1

    # Style
    header_fill = PatternFill(start_color="0070C0", end_color="0070C0", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=12)
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # Tiêu đề
    ws_dash['A1'] = "THỐNG KÊ HỎI ĐÁP CHÍNH SÁCH"
    ws_dash['A1'].font = Font(bold=True, size=16, color="0070C0")
    ws_dash['A2'] = f"Cập nhật: {data.get('updated', '')[:10]}"
    ws_dash['A3'] = f"Tổng số: {len(records)} bản ghi"

    # Bảng thống kê
    ws_dash['A5'] = "Trục"
    ws_dash['B5'] = "Số lượng"
    ws_dash['C5'] = "Tỷ lệ"
    for cell in ['A5', 'B5', 'C5']:
        ws_dash[cell].fill = header_fill
        ws_dash[cell].font = header_font
        ws_dash[cell].border = border

    row = 6
    total = len(records)
    for truc, count in truc_count.items():
        if count > 0 or 'Trục' in truc:
            ws_dash[f'A{row}'] = truc
            ws_dash[f'B{row}'] = count
            ws_dash[f'C{row}'] = f"{count/total*100:.1f}%" if total > 0 else "0%"
            for col in ['A', 'B', 'C']:
                ws_dash[f'{col}{row}'].border = border
            row += 1

    # Tổng
    ws_dash[f'A{row}'] = "TỔNG"
    ws_dash[f'B{row}'] = total
    ws_dash[f'C{row}'] = "100%"
    for col in ['A', 'B', 'C']:
        ws_dash[f'{col}{row}'].font = Font(bold=True)
        ws_dash[f'{col}{row}'].border = border

    ws_dash.column_dimensions['A'].width = 20
    ws_dash.column_dimensions['B'].width = 12
    ws_dash.column_dimensions['C'].width = 10

    # === Sheet TẤT CẢ ===
    ws_all = wb.create_sheet("TẤT CẢ")

    # Header
    cols = ['Tiêu đề', 'Nội dung câu hỏi', 'Nội dung trả lời', 'Trục', 'Nguồn', 'Ngày']
    for col_idx, col_name in enumerate(cols, 1):
        cell = ws_all.cell(row=1, column=col_idx, value=col_name)
        cell.fill = header_fill
        cell.font = header_font
        cell.border = border

    # Data
    for row_idx, record in enumerate(records, 2):
        for col_idx, col_name in enumerate(cols, 1):
            val = record.get(col_name, '')
            if isinstance(val, str) and len(val) > 32000:
                val = val[:32000] + "..."
            cell = ws_all.cell(row=row_idx, column=col_idx, value=val)
            cell.border = border
            cell.alignment = Alignment(wrap_text=True, vertical='top')

    # Column widths
    ws_all.column_dimensions['A'].width = 40
    ws_all.column_dimensions['B'].width = 50
    ws_all.column_dimensions['C'].width = 60
    ws_all.column_dimensions['D'].width = 15
    ws_all.column_dimensions['E'].width = 30
    ws_all.column_dimensions['F'].width = 12

    # === Sheets theo Trục ===
    for i in range(1, 7):
        ws_truc = wb.create_sheet(f"Trục {i}")

        # Filter
        truc_records = [r for r in records if f'Trục {i}' in str(r.get('Trục', '')) or f'({i})' in str(r.get('Trục', ''))]

        # Header
        for col_idx, col_name in enumerate(cols, 1):
            cell = ws_truc.cell(row=1, column=col_idx, value=col_name)
            cell.fill = header_fill
            cell.font = header_font

        # Data
        for row_idx, record in enumerate(truc_records, 2):
            for col_idx, col_name in enumerate(cols, 1):
                val = record.get(col_name, '')
                if isinstance(val, str) and len(val) > 32000:
                    val = val[:32000] + "..."
                ws_truc.cell(row=row_idx, column=col_idx, value=val)

    # Lưu
    excel_path = kho / 'Hoi_dap_chinh_sach.xlsx'
    wb.save(excel_path)
    print(f"✓ Đã xuất: {excel_path}")
    print(f"  - DASHBOARD: thống kê theo Trục")
    print(f"  - TẤT CẢ: {len(records)} bản ghi")
    for i in range(1, 7):
        count = truc_count[f'Trục {i}']
        if count > 0:
            print(f"  - Trục {i}: {count} bản ghi")


if __name__ == '__main__':
    main()
