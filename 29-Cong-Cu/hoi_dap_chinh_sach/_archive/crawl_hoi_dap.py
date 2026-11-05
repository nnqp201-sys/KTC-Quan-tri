#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Công cụ thu thập hỏi đáp chính sách - KTC-Quan-tri
Phiên bản: 1.1.0 (04/11/2026)
Cải tiến:
  - Lưu trữ tăng dần (merge với dữ liệu cũ)
  - Phân loại theo 6 Trục TB 817
  - Bổ sung nguồn moet.gov.vn
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
import pandas as pd
from urllib.parse import urljoin
import json
import os
import time
import hashlib
from pathlib import Path

# Mapping 6 Trục TB 817/TB-CĐKT
SAU_TRUC = {
    1: "Thực hiện mục tiêu phát triển KT-XH và nhiệm vụ chính trị",
    2: "Hoàn thiện thể chế, phân cấp, phân quyền",
    3: "Khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số",
    4: "Xây dựng Đảng và hệ thống chính trị",
    5: "Phát triển văn hóa, con người, an sinh xã hội",
    6: "Quốc phòng, an ninh, đối ngoại và hội nhập"
}

# Từ khóa phân loại theo Trục
TU_KHOA_TRUC = {
    1: ['đào tạo', 'tuyển sinh', 'giảng dạy', 'chương trình', 'sinh viên',
        'học sinh', 'giáo viên', 'nhà giáo', 'bằng cấp', 'chứng chỉ',
        'kiểm định', 'chất lượng giáo dục', 'nghề nghiệp', 'kỹ năng'],
    2: ['quy chế', 'quy định', 'thể chế', 'phân cấp', 'ủy quyền',
        'thủ tục hành chính', 'cải cách', 'thanh tra', 'kiểm tra',
        'văn thư', 'lưu trữ', 'công khai', 'minh bạch'],
    3: ['khoa học', 'công nghệ', 'nghiên cứu', 'sáng kiến', 'đổi mới',
        'chuyển đổi số', 'công nghệ thông tin', 'phần mềm', 'dữ liệu',
        'an toàn thông tin', 'sở hữu trí tuệ'],
    4: ['đảng viên', 'chi bộ', 'đảng bộ', 'tổ chức đảng', 'kỷ luật đảng',
        'kiểm tra đảng', 'dân vận', 'đoàn thể', 'công đoàn', 'đoàn thanh niên',
        'thi đua', 'khen thưởng', 'danh hiệu'],
    5: ['văn hóa', 'thương hiệu', 'tài chính', 'ngân sách', 'thuế',
        'kế toán', 'tài sản', 'mua sắm', 'đấu thầu', 'đầu tư công',
        'tiền lương', 'bảo hiểm', 'lao động', 'hợp đồng', 'viên chức',
        'biên chế', 'môi trường'],
    6: ['quốc phòng', 'an ninh', 'bảo vệ', 'đối ngoại', 'hợp tác quốc tế',
        'nước ngoài', 'du học', 'liên kết quốc tế']
}


class HoiDapCrawler:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = Path(__file__).parent / 'config.json'
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept-Language': 'vi-VN,vi;q=0.9'
        })
        self.results = []
        self.seen_hashes = set()
        self.cutoff = datetime.now() - timedelta(days=self.config.get('days_back', 365))

        # Load dữ liệu cũ nếu có
        self._load_existing()

    def _load_existing(self):
        """Đọc dữ liệu cũ để merge tăng dần"""
        outdir = self._get_output_dir()
        outfile = outdir / self.config['output_file']
        if outfile.exists():
            try:
                df = pd.read_excel(outfile, sheet_name='TẤT CẢ')
                for _, row in df.iterrows():
                    h = self._hash_content(str(row.get('Nội dung câu hỏi', '')))
                    self.seen_hashes.add(h)
                    self.results.append(row.to_dict())
                print(f"Đã nạp {len(self.results)} bản ghi cũ")
            except Exception as e:
                print(f"Không đọc được dữ liệu cũ: {e}")

    def _get_output_dir(self):
        """Lấy thư mục đầu ra"""
        base = Path(__file__).parent
        outdir = base / self.config['output_dir']
        outdir.mkdir(parents=True, exist_ok=True)
        return outdir

    def _hash_content(self, text):
        """Tạo hash để khử trùng"""
        return hashlib.md5(text.encode('utf-8')).hexdigest()[:16]

    def phan_loai_truc(self, text):
        """Phân loại theo 6 Trục TB 817"""
        tl = text.lower()
        scores = {i: 0 for i in range(1, 7)}

        for truc, keywords in TU_KHOA_TRUC.items():
            for kw in keywords:
                if kw in tl:
                    scores[truc] += 1

        # Chọn Trục có điểm cao nhất
        best = max(scores, key=scores.get)
        if scores[best] == 0:
            return 5, "Trục 5 — Phát triển văn hóa, con người, an sinh xã hội"
        return best, f"Trục {best} — {SAU_TRUC[best]}"

    def _parse_date(self, date_str):
        """Parse ngày từ chuỗi"""
        m = re.search(r'(\d{1,2})/(\d{1,2})/(\d{4})', date_str)
        if m:
            try:
                return datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)))
            except:
                pass
        return None

    def crawl_chinhsachonline(self, max_pages=30):
        """Thu thập từ chinhsachonline.chinhphu.vn"""
        base = 'https://chinhsachonline.chinhphu.vn'
        new_count = 0

        for page in range(1, max_pages + 1):
            try:
                url = base + '/danh-sach-cau-hoi.htm' if page == 1 else base + f'/danh-sach-cau-hoi/trang-{page}.htm'
                r = self.session.get(url, timeout=30)
                if r.status_code != 200:
                    break

                soup = BeautifulSoup(r.text, 'html.parser')
                links = []
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if not re.search(r'-\d{4,}\.htm$', href):
                        continue
                    if any(x in href for x in ['/danh-sach', '/trang-', '/hoi-dap-ve', '/cau-hoi-thuong-gap']):
                        continue
                    links.append(urljoin(base, href))

                for durl in links:
                    rec = self._crawl_detail_chinhsach(durl)
                    if rec:
                        new_count += 1

                print(f"[chinhsachonline] Trang {page}: {len(links)} link, {new_count} mới")
                time.sleep(1)
            except Exception as e:
                print(f"Lỗi trang {page}: {e}")
                break

        return new_count

    def _crawl_detail_chinhsach(self, url):
        """Lấy chi tiết một câu hỏi từ chinhsachonline"""
        try:
            r = self.session.get(url, timeout=30)
            soup = BeautifulSoup(r.text, 'html.parser')

            for tag in soup(['script', 'style', 'nav', 'header', 'footer']):
                tag.decompose()

            text = soup.get_text('\n', strip=True)

            # Tìm ngày
            dates = re.findall(r'(\d{1,2}/\d{1,2}/\d{4})', text)
            if len(dates) < 1:
                return None

            adate = dates[-1]
            dt = self._parse_date(adate)
            if not dt or dt < self.cutoff:
                return None

            # Tìm nội dung câu hỏi
            qm = re.search(r'Chi tiết câu hỏi\s*\n+(.*?)(?:\n\s*Trả lời)', text, re.S | re.I)
            if not qm:
                qm = re.search(r'Nội dung câu hỏi[:\s]+(.*?)(?:Trả lời|$)', text, re.S | re.I)
            qcontent = qm.group(1).strip() if qm else ''

            # Khử trùng
            h = self._hash_content(qcontent)
            if h in self.seen_hashes:
                return None

            # Tìm nội dung trả lời
            am = re.search(r'(?:\n\s*Trả lời\s*\n+)(.*?)(?:\n\s*Chia sẻ|\Z)', text, re.S | re.I)
            if not am:
                am = re.search(r'Trả lời[:\s]+(.*?)$', text, re.S | re.I)
            acontent = am.group(1).strip() if am else ''

            if not qcontent or not acontent:
                return None

            # Phân loại Trục
            truc_so, truc_ten = self.phan_loai_truc(qcontent + ' ' + acontent)

            # Cơ quan trả lời
            agency = ''
            for ag in ['Tổng cục Thuế', 'Bảo hiểm xã hội', 'Bộ Tài chính',
                       'Bộ Giáo dục và Đào tạo', 'Bộ Lao động', 'Bộ Nội vụ']:
                if ag in text:
                    agency = ag
                    break

            rec = {
                'TT': len(self.results) + 1,
                'Hash': h,
                'Người hỏi': '',
                'Nội dung câu hỏi': qcontent[:2000],
                'Ngày hỏi': dates[0] if dates else '',
                'Cơ quan trả lời': agency,
                'Nội dung trả lời': acontent[:5000],
                'Ngày trả lời': adate,
                'Trục TB 817': truc_so,
                'Lĩnh vực': truc_ten,
                'Nguồn': 'chinhsachonline.chinhphu.vn',
                'Link': url,
                'Ngày thu thập': datetime.now().strftime('%d/%m/%Y'),
                'Ghi chú': 'Nguồn chính thức',
                'Khả năng áp dụng': 'Cần rà soát | Cần xác minh'
            }

            self.results.append(rec)
            self.seen_hashes.add(h)
            return rec
        except Exception as e:
            return None

    def crawl_moet(self, max_pages=20):
        """Thu thập từ moet.gov.vn"""
        base = 'https://moet.gov.vn'
        new_count = 0

        # Các trang hỏi đáp của Bộ GD&ĐT
        sections = [
            '/gioi-thieu/hoi-dap.html',
            '/tin-tuc/hoi-dap-phap-luat.html'
        ]

        for section in sections:
            try:
                url = base + section
                r = self.session.get(url, timeout=30)
                if r.status_code != 200:
                    continue

                soup = BeautifulSoup(r.text, 'html.parser')

                # Tìm các bài viết hỏi đáp
                for article in soup.find_all(['article', 'div'], class_=re.compile(r'news|article|item')):
                    a = article.find('a', href=True)
                    if not a:
                        continue
                    href = urljoin(base, a['href'])
                    rec = self._crawl_detail_moet(href)
                    if rec:
                        new_count += 1

                print(f"[moet.gov.vn] {section}: {new_count} mới")
                time.sleep(1)
            except Exception as e:
                print(f"Lỗi {section}: {e}")

        return new_count

    def _crawl_detail_moet(self, url):
        """Lấy chi tiết từ moet.gov.vn"""
        try:
            if url in [r.get('Link') for r in self.results]:
                return None

            r = self.session.get(url, timeout=30)
            soup = BeautifulSoup(r.text, 'html.parser')

            for tag in soup(['script', 'style', 'nav', 'header', 'footer']):
                tag.decompose()

            # Tìm tiêu đề và nội dung
            title = soup.find('h1')
            title_text = title.get_text(strip=True) if title else ''

            content_div = soup.find(['div', 'article'], class_=re.compile(r'content|body|detail'))
            content = content_div.get_text('\n', strip=True) if content_div else ''

            if not content or len(content) < 100:
                return None

            h = self._hash_content(title_text + content[:500])
            if h in self.seen_hashes:
                return None

            # Tìm ngày
            dates = re.findall(r'(\d{1,2}/\d{1,2}/\d{4})', content)
            pub_date = dates[0] if dates else datetime.now().strftime('%d/%m/%Y')

            dt = self._parse_date(pub_date)
            if dt and dt < self.cutoff:
                return None

            truc_so, truc_ten = self.phan_loai_truc(title_text + ' ' + content)

            rec = {
                'TT': len(self.results) + 1,
                'Hash': h,
                'Người hỏi': '',
                'Nội dung câu hỏi': title_text,
                'Ngày hỏi': pub_date,
                'Cơ quan trả lời': 'Bộ Giáo dục và Đào tạo',
                'Nội dung trả lời': content[:5000],
                'Ngày trả lời': pub_date,
                'Trục TB 817': truc_so,
                'Lĩnh vực': truc_ten,
                'Nguồn': 'moet.gov.vn',
                'Link': url,
                'Ngày thu thập': datetime.now().strftime('%d/%m/%Y'),
                'Ghi chú': 'Nguồn chính thức — Bộ GD&ĐT',
                'Khả năng áp dụng': 'Áp dụng trực tiếp | Liên quan đến đào tạo'
            }

            self.results.append(rec)
            self.seen_hashes.add(h)
            return rec
        except:
            return None

    def export(self):
        """Xuất kết quả ra Excel"""
        if not self.results:
            print("Không có dữ liệu để xuất")
            return None

        df = pd.DataFrame(self.results)
        df = df.drop_duplicates(subset=['Hash'])
        df['TT'] = range(1, len(df) + 1)

        # Sắp xếp theo ngày mới nhất
        df['_sort_date'] = pd.to_datetime(df['Ngày trả lời'], format='%d/%m/%Y', errors='coerce')
        df = df.sort_values('_sort_date', ascending=False)
        df = df.drop('_sort_date', axis=1)
        df['TT'] = range(1, len(df) + 1)

        outdir = self._get_output_dir()
        outfile = outdir / self.config['output_file']

        with pd.ExcelWriter(outfile, engine='openpyxl') as writer:
            # Sheet tất cả
            df.to_excel(writer, sheet_name='TẤT CẢ', index=False)

            # Sheet theo Trục
            for truc in range(1, 7):
                df_truc = df[df['Trục TB 817'] == truc]
                if not df_truc.empty:
                    sheet_name = f"Trục {truc}"
                    df_truc.to_excel(writer, sheet_name=sheet_name, index=False)

            # Sheet tổng quan
            stats = []
            for truc in range(1, 7):
                count = len(df[df['Trục TB 817'] == truc])
                stats.append({
                    'Trục': f"Trục {truc}",
                    'Tên': SAU_TRUC[truc],
                    'Số bản ghi': count
                })
            stats.append({'Trục': 'TỔNG', 'Tên': '', 'Số bản ghi': len(df)})

            df_stats = pd.DataFrame(stats)
            df_stats.to_excel(writer, sheet_name='TỔNG QUAN', index=False)

            # Metadata
            meta = pd.DataFrame({
                'Thông tin': ['Ngày cập nhật', 'Tổng số bản ghi', 'Nguồn', 'Phiên bản'],
                'Giá trị': [
                    datetime.now().strftime('%d/%m/%Y %H:%M'),
                    len(df),
                    ', '.join(df['Nguồn'].unique()),
                    '1.1.0'
                ]
            })
            meta.to_excel(writer, sheet_name='METADATA', index=False)

        print(f"Đã xuất: {outfile} ({len(df)} bản ghi)")
        return str(outfile)

    def export_ktc_database(self):
        """Xuất ra KTC-Database (nếu có quyền ghi)"""
        # Lấy đường dẫn KTC-Database
        try:
            import sys
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from duong_dan import ktc_database

            output_dir = Path(ktc_database()) / '07-Hoi-Dap-Chinh-Sach'
            output_dir.mkdir(parents=True, exist_ok=True)

            # Xuất JSON để agent tra cứu
            df = pd.DataFrame(self.results)
            records = df.to_dict('records')

            json_file = output_dir / 'hoi_dap_index.json'
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'version': '1.1.0',
                    'updated': datetime.now().isoformat(),
                    'count': len(records),
                    'records': records
                }, f, ensure_ascii=False, indent=2)

            print(f"Đã xuất KTC-Database: {json_file}")
            return str(json_file)
        except Exception as e:
            print(f"Không xuất được KTC-Database: {e}")
            return None

    def run_all(self):
        """Chạy tất cả nguồn"""
        print("=" * 60)
        print("BẮT ĐẦU THU THẬP HỎI ĐÁP CHÍNH SÁCH")
        print("=" * 60)

        total_new = 0

        # Nguồn 1: chinhsachonline.chinhphu.vn
        if self.config.get('sources', {}).get('chinhsachonline', {}).get('enabled', True):
            n = self.crawl_chinhsachonline(max_pages=self.config.get('max_pages', 30))
            total_new += n

        # Nguồn 2: moet.gov.vn
        if self.config.get('sources', {}).get('moet', {}).get('enabled', True):
            n = self.crawl_moet(max_pages=self.config.get('max_pages', 20))
            total_new += n

        print("=" * 60)
        print(f"TỔNG: {len(self.results)} bản ghi ({total_new} mới)")
        print("=" * 60)

        # Xuất kết quả
        self.export()
        self.export_ktc_database()


if __name__ == '__main__':
    crawler = HoiDapCrawler()
    crawler.run_all()
