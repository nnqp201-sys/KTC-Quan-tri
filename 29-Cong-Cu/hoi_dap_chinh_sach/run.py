#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Điểm khởi động công cụ thu thập hỏi đáp chính sách
Sử dụng: python run.py [--full | --quick | --export-only]
"""
import subprocess
import sys
import os
import argparse

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    parser = argparse.ArgumentParser(description='Thu thập hỏi đáp chính sách')
    parser.add_argument('--full', action='store_true', help='Thu thập đầy đủ (30 trang)')
    parser.add_argument('--quick', action='store_true', help='Thu thập nhanh (5 trang)')
    parser.add_argument('--export-only', action='store_true', help='Chỉ xuất từ dữ liệu cũ')
    args = parser.parse_args()

    if args.export_only:
        # Chỉ xuất
        from crawl_hoi_dap import HoiDapCrawler
        c = HoiDapCrawler()
        c.export()
    elif args.quick:
        # Nhanh
        import json
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        config['max_pages'] = 5
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

        from crawl_hoi_dap import HoiDapCrawler
        c = HoiDapCrawler()
        c.run_all()
    else:
        # Đầy đủ
        from crawl_hoi_dap import HoiDapCrawler
        c = HoiDapCrawler()
        c.run_all()

if __name__ == '__main__':
    main()
