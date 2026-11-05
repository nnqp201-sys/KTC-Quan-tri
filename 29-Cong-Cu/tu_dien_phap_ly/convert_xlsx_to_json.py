# -*- coding: utf-8 -*-
"""
Convert file Excel từ điển pháp lý thành JSON để merge.
"""

import json
from pathlib import Path
from datetime import datetime
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from duong_dan import ktc_database

try:
    from openpyxl import load_workbook
except ImportError:
    print("Cần cài openpyxl: pip install openpyxl")
    sys.exit(1)


def convert_xlsx_to_json(xlsx_name: str):
    """Convert file Excel thành JSON format chuẩn."""

    kho_path = Path(ktc_database()) / '08-Tu-Dien-Phap-Ly'
    xlsx_path = kho_path / xlsx_name

    if not xlsx_path.exists():
        print(f"Không tìm thấy file: {xlsx_path}")
        return None

    print(f"Đọc file: {xlsx_path}")
    wb = load_workbook(xlsx_path, read_only=True)

    # Tìm sheet dữ liệu chính
    sheet_name = None
    for name in ['Từ điển pháp lý', 'Tu dien phap ly', 'Sheet1']:
        if name in wb.sheetnames:
            sheet_name = name
            break

    if not sheet_name:
        sheet_name = wb.sheetnames[0]

    ws = wb[sheet_name]
    print(f"Sheet: {sheet_name}")

    # Đọc header
    headers = []
    for cell in ws[1]:
        if cell.value:
            headers.append(str(cell.value).strip())
        else:
            headers.append(f"Col{len(headers)}")

    print(f"Headers: {headers[:5]}...")

    # Map cột
    col_map = {}
    field_names = ['STT', 'Thuật ngữ', 'Mô tả', 'Định nghĩa', 'Tình trạng hiệu lực',
                   'Nguồn', 'Trục', 'Lĩnh vực', 'Ghi chú']
    for i, h in enumerate(headers):
        for f in field_names:
            if f.lower() in h.lower():
                col_map[f] = i
                break

    # Đọc dữ liệu
    records = []
    for row_num, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        # Lấy thuật ngữ
        thuat_ngu_idx = col_map.get('Thuật ngữ', 1)
        thuat_ngu = row[thuat_ngu_idx] if thuat_ngu_idx < len(row) else None

        if not thuat_ngu:
            continue

        rec = {}
        for field in field_names:
            idx = col_map.get(field)
            if idx is not None and idx < len(row):
                val = row[idx]
                rec[field] = str(val).strip() if val else ''
            else:
                rec[field] = ''

        records.append(rec)

    wb.close()

    # Tạo JSON output
    output = {
        "date": datetime.now().strftime('%Y-%m-%d'),
        "source": xlsx_name,
        "pages_crawled": f"Converted from {xlsx_name}",
        "new_records": records
    }

    # Lưu file JSON
    json_name = xlsx_name.replace('.xlsx', '.json')
    json_path = kho_path / json_name

    # Ghi ra thư mục dự án thay vì KTC-Database
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)
    json_path = output_dir / json_name

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Đã convert: {len(records)} thuật ngữ")
    print(f"Lưu tại: {json_path}")

    return json_path


if __name__ == '__main__':
    if len(sys.argv) > 1:
        xlsx_name = sys.argv[1]
    else:
        xlsx_name = 'Tu-dien-phap-ly_v2_2026-11-05.xlsx'

    convert_xlsx_to_json(xlsx_name)
