# -*- coding: utf-8 -*-
"""
Merge các file hoi_dap_moi_*.json vào index + xuất Excel
Chạy: python merge_va_xuat.py
"""
import json
import glob
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from duong_dan import ktc_database

try:
    import pandas as pd
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
except ImportError:
    print("Cần cài: pip install pandas openpyxl")
    sys.exit(1)


def merge_json():
    """Merge các file hoi_dap_moi_*.json vào hoi_dap_index.json"""
    kho = Path(ktc_database()) / '07-Hoi-Dap-Chinh-Sach'
    index_path = kho / 'hoi_dap_index.json'

    # Đọc index hiện tại
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"version": "1.2.0", "updated": "", "count": 0, "records": []}

    records = data.get('records', [])
    seen_titles = {r.get('Tiêu đề', '') for r in records}

    # Tìm các file mới
    new_files = sorted(glob.glob(str(kho / 'hoi_dap_moi_*.json')))

    if not new_files:
        print("Không có file mới để merge")
        return records

    added = 0
    for fpath in new_files:
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                new_data = json.load(f)

            new_records = new_data.get('new_records', [])
            for r in new_records:
                title = r.get('Tiêu đề', '')
                if title and title not in seen_titles:
                    records.append(r)
                    seen_titles.add(title)
                    added += 1

            # Di chuyển file đã xử lý vào archive
            archive_dir = kho / '_archive'
            archive_dir.mkdir(exist_ok=True)
            Path(fpath).rename(archive_dir / Path(fpath).name)
            print(f"  Đã xử lý: {Path(fpath).name}")

        except Exception as e:
            print(f"  Lỗi đọc {fpath}: {e}")

    # Cập nhật index
    data['records'] = records
    data['count'] = len(records)
    data['updated'] = datetime.now().isoformat()

    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✓ Đã merge {added} bản ghi mới → Tổng: {len(records)}")
    return records


def xuat_excel(records):
    """Xuất Excel có dashboard"""
    kho = Path(ktc_database()) / '07-Hoi-Dap-Chinh-Sach'

    if not records:
        print("Không có dữ liệu để xuất")
        return

    # Thống kê theo Trục
    truc_count = {f'Trục {i}': 0 for i in range(1, 7)}
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

    # Tạo workbook
    wb = Workbook()

    # Style
    header_fill = PatternFill(start_color="0070C0", end_color="0070C0", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=12)
    border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )

    # === Sheet DASHBOARD ===
    ws_dash = wb.active
    ws_dash.title = "DASHBOARD"

    ws_dash['A1'] = "THỐNG KÊ HỎI ĐÁP PHÁP LUẬT, CHÍNH SÁCH"
    ws_dash['A1'].font = Font(bold=True, size=16, color="0070C0")
    ws_dash['A2'] = f"Cập nhật: {datetime.now().strftime('%d/%m/%Y')}"
    ws_dash['A3'] = f"Tổng số: {len(records)} bản ghi"

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
        ws_dash[f'A{row}'] = truc
        ws_dash[f'B{row}'] = count
        ws_dash[f'C{row}'] = f"{count/total*100:.1f}%" if total > 0 else "0%"
        for col in ['A', 'B', 'C']:
            ws_dash[f'{col}{row}'].border = border
        row += 1

    ws_dash.column_dimensions['A'].width = 20
    ws_dash.column_dimensions['B'].width = 12
    ws_dash.column_dimensions['C'].width = 10

    # === Sheet TẤT CẢ ===
    ws_all = wb.create_sheet("TẤT CẢ")
    cols = ['Tiêu đề', 'Nội dung câu hỏi', 'Nội dung trả lời', 'Trục', 'Nguồn', 'Ngày']

    for col_idx, col_name in enumerate(cols, 1):
        cell = ws_all.cell(row=1, column=col_idx, value=col_name)
        cell.fill = header_fill
        cell.font = header_font
        cell.border = border

    for row_idx, record in enumerate(records, 2):
        for col_idx, col_name in enumerate(cols, 1):
            val = record.get(col_name, '')
            if isinstance(val, str) and len(val) > 32000:
                val = val[:32000] + "..."
            cell = ws_all.cell(row=row_idx, column=col_idx, value=val)
            cell.border = border
            cell.alignment = Alignment(wrap_text=True, vertical='top')

    ws_all.column_dimensions['A'].width = 40
    ws_all.column_dimensions['B'].width = 50
    ws_all.column_dimensions['C'].width = 60
    ws_all.column_dimensions['D'].width = 15
    ws_all.column_dimensions['E'].width = 30
    ws_all.column_dimensions['F'].width = 12

    # Lưu
    excel_path = kho / 'Hoi_dap_chinh_sach.xlsx'
    wb.save(excel_path)
    print(f"✓ Đã xuất Excel: {excel_path}")

    # Thống kê
    for truc, count in truc_count.items():
        if count > 0:
            print(f"  {truc}: {count}")


def main():
    print("=== MERGE VÀ XUẤT HỎI ĐÁP CHÍNH SÁCH ===\n")
    records = merge_json()
    print()
    xuat_excel(records)
    print("\n✓ Hoàn tất!")


if __name__ == '__main__':
    main()
