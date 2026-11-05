# -*- coding: utf-8 -*-
"""
Tra cứu Từ điển pháp lý — CHỈ ĐỌC
Dùng cho các agent tra cứu thuật ngữ pháp lý từ kho KTC-Database.
"""

import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from duong_dan import ktc_database


def load_index() -> dict:
    """Đọc file index từ điển pháp lý."""
    index_path = Path(ktc_database()) / '08-Tu-Dien-Phap-Ly/tu_dien_index.json'
    if not index_path.exists():
        return {"records": [], "last_updated": None, "total": 0}
    with open(index_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def tim_thuat_ngu(keyword: str, truc: str = None, linh_vuc: str = None, limit: int = 20) -> list:
    """
    Tìm thuật ngữ theo từ khóa.

    Args:
        keyword: Từ khóa tìm kiếm (trong Thuật ngữ, Mô tả, Định nghĩa)
        truc: Lọc theo Trục (1-6)
        linh_vuc: Lọc theo lĩnh vực (giao-duc, hssv, vien-chuc, ...)
        limit: Số kết quả tối đa

    Returns:
        Danh sách thuật ngữ phù hợp
    """
    data = load_index()
    results = []
    kw_lower = keyword.lower()

    for r in data.get('records', []):
        # Tìm trong thuật ngữ, mô tả, định nghĩa
        text = ' '.join([
            r.get('Thuật ngữ', ''),
            r.get('Mô tả', ''),
            r.get('Định nghĩa', '')
        ]).lower()

        if kw_lower not in text:
            continue

        # Lọc theo Trục
        if truc and r.get('Trục') != f'Trục {truc}':
            continue

        # Lọc theo lĩnh vực
        if linh_vuc and r.get('Lĩnh vực') != linh_vuc:
            continue

        results.append(r)
        if len(results) >= limit:
            break

    return results


def lay_theo_linh_vuc(linh_vuc: str, limit: int = 50) -> list:
    """Lấy tất cả thuật ngữ theo lĩnh vực."""
    data = load_index()
    results = []

    for r in data.get('records', []):
        if r.get('Lĩnh vực') == linh_vuc:
            results.append(r)
            if len(results) >= limit:
                break

    return results


def lay_theo_truc(truc: str, limit: int = 50) -> list:
    """Lấy tất cả thuật ngữ theo Trục."""
    data = load_index()
    results = []

    for r in data.get('records', []):
        if r.get('Trục') == f'Trục {truc}':
            results.append(r)
            if len(results) >= limit:
                break

    return results


def thong_ke() -> dict:
    """Thống kê tổng quan từ điển."""
    data = load_index()
    records = data.get('records', [])

    # Đếm theo Trục
    by_truc = {}
    for r in records:
        truc = r.get('Trục', 'Chưa phân loại')
        by_truc[truc] = by_truc.get(truc, 0) + 1

    # Đếm theo lĩnh vực
    by_linh_vuc = {}
    for r in records:
        lv = r.get('Lĩnh vực', 'Chưa phân loại')
        by_linh_vuc[lv] = by_linh_vuc.get(lv, 0) + 1

    # Đếm theo tình trạng hiệu lực
    by_hieu_luc = {}
    for r in records:
        hl = r.get('Tình trạng hiệu lực', 'Chưa xác định')
        by_hieu_luc[hl] = by_hieu_luc.get(hl, 0) + 1

    return {
        "total": len(records),
        "last_updated": data.get('last_updated'),
        "by_truc": by_truc,
        "by_linh_vuc": by_linh_vuc,
        "by_hieu_luc": by_hieu_luc
    }


if __name__ == '__main__':
    # Test
    print("=== Thống kê Từ điển pháp lý ===")
    stats = thong_ke()
    print(f"Tổng số thuật ngữ: {stats['total']}")
    print(f"Cập nhật lần cuối: {stats['last_updated']}")
