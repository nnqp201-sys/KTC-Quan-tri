# -*- coding: utf-8 -*-
"""
Tra cứu hỏi đáp chính sách từ KTC-Database/07-Hoi-Dap-Chinh-Sach
Dữ liệu được cập nhật tự động bởi routine ở tài khoản KTC-Database (phongthhcqt@gmail.com)
"""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from duong_dan import ktc_database


def load_index():
    """Đọc index hỏi đáp từ KTC-Database"""
    index_path = Path(ktc_database()) / '07-Hoi-Dap-Chinh-Sach' / 'hoi_dap_index.json'
    if not index_path.exists():
        return {"records": [], "count": 0}
    with open(index_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def tim_kiem(tu_khoa: str, truc: int = None):
    """Tìm kiếm hỏi đáp theo từ khóa và/hoặc Trục

    Args:
        tu_khoa: Từ khóa tìm kiếm (trong tiêu đề, câu hỏi, trả lời)
        truc: Số Trục (1-6), None = tất cả

    Returns:
        list: Danh sách bản ghi khớp
    """
    data = load_index()
    ket_qua = []
    tu_khoa_lower = tu_khoa.lower()

    for r in data.get('records', []):
        # Lọc theo Trục
        if truc:
            truc_str = r.get('Trục', '')
            if f'Trục {truc}' not in truc_str and f'({truc})' not in truc_str:
                continue

        # Tìm theo từ khóa
        text = ' '.join([
            str(r.get('Tiêu đề', '')),
            str(r.get('Nội dung câu hỏi', '')),
            str(r.get('Nội dung trả lời', ''))
        ]).lower()

        if tu_khoa_lower in text:
            ket_qua.append(r)

    return ket_qua


def thong_ke():
    """Thống kê số lượng theo Trục"""
    data = load_index()
    dem = {f'Trục {i}': 0 for i in range(1, 7)}
    dem['Khác'] = 0

    for r in data.get('records', []):
        truc = r.get('Trục', '')
        matched = False
        for i in range(1, 7):
            if f'Trục {i}' in truc or f'({i})' in truc:
                dem[f'Trục {i}'] += 1
                matched = True
                break
        if not matched:
            dem['Khác'] += 1

    return {
        'tong': data.get('count', 0),
        'cap_nhat': data.get('updated', ''),
        'theo_truc': dem
    }


if __name__ == '__main__':
    # Demo
    stats = thong_ke()
    print(f"Tổng: {stats['tong']} bản ghi")
    print(f"Cập nhật: {stats['cap_nhat']}")
    print("Theo Trục:")
    for k, v in stats['theo_truc'].items():
        if v > 0:
            print(f"  {k}: {v}")
