# -*- coding: utf-8 -*-
"""
Kiểm thuật ngữ pháp lý trong văn bản — đối chiếu kho 08-Tu-Dien-Phap-Ly.

Lớp kiểm ĐỘC LẬP, chạy song song KTC-Ra-Soat-897 (không sửa lõi 897).

Phép kiểm:
  TN01 — Thuật ngữ gần đúng: văn bản dùng biến thể của một thuật ngữ chuẩn
  TN02 — Thuật ngữ từ văn bản HẾT HIỆU LỰC hoặc cần đối chiếu
  TN03 — Không nhất quán: cùng khái niệm dùng nhiều cách viết trong một văn bản
  TN04 — Có hỏi đáp chính sách liên quan (gợi ý tham khảo, không phải lỗi)

Mức vấn đề theo quy ước KTC: 1 bắt buộc sửa → 4 góp ý.

Dùng:
    python 29-Cong-Cu/kiem_thuat_ngu.py <tệp.docx|.md|.txt> [--linh-vuc giao-duc] [--xuat bao-cao.md]
"""

import argparse
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from duong_dan import ktc_database  # noqa: E402

# ─────────────────────────────────────────────────────────────
# Ngưỡng và hằng số
# ─────────────────────────────────────────────────────────────

# Thuật ngữ ngắn hơn ngưỡng này bị bỏ qua — quá nhiều dương tính giả
DO_DAI_TOI_THIEU = 6

# Độ giống tối thiểu để coi là "biến thể gần đúng" (TN01)
NGUONG_GAN_DUNG = 0.86

# Tình trạng hiệu lực coi là có vấn đề
HET_HIEU_LUC = ('hết hiệu lực', 'hết hiệu lực một phần')
# "Cần đối chiếu" kèm lý do cụ thể (Luật đã sửa đổi…) — rủi ro thật cho văn bản
CAN_DOI_CHIEU = ('cần đối chiếu',)
# "Chưa xác minh" — kho chưa kiểm xong, KHÔNG phải lỗi của văn bản đang soạn
CHUA_XAC_MINH = ('chưa xác minh', 'chưa xác định')

MUC_TEN = {
    1: 'Mức 1 — bắt buộc sửa',
    2: 'Mức 2 — cần sửa',
    3: 'Mức 3 — nên sửa',
    4: 'Mức 4 — góp ý',
}

# Hư từ: cụm đứng cạnh các từ này thì coi là trọn vẹn, không bị cắt giữa chừng
HU_TU = {
    'của', 'trong', 'về', 'theo', 'và', 'cho', 'với', 'tại', 'từ', 'đến',
    'do', 'bởi', 'khi', 'nếu', 'là', 'các', 'những', 'một', 'này', 'đó',
    'được', 'bị', 'có', 'không', 'để', 'mà', 'thì', 'hoặc', 'hay', 'như',
    'trên', 'dưới', 'sau', 'trước', 'giữa', 'ngoài', 'cùng', 'nhằm', 'vì',
}

# Thuật ngữ quá phổ thông — vẫn liệt kê nhưng không nâng mức cảnh báo
THUAT_NGU_PHO_THONG = {
    'tiêu chuẩn', 'chương trình', 'kế hoạch', 'quyết định', 'đánh giá',
    'quản lý', 'tổ chức', 'hoạt động', 'nội dung', 'kết quả', 'thực hiện',
    'nhiệm vụ', 'báo cáo', 'hồ sơ', 'văn bản', 'quy định', 'đào tạo',
}


# ─────────────────────────────────────────────────────────────
# Đọc văn bản
# ─────────────────────────────────────────────────────────────

def doc_van_ban(duong_dan: Path) -> str:
    """Đọc nội dung text từ .docx, .md, .txt."""
    hau_to = duong_dan.suffix.lower()

    if hau_to == '.docx':
        try:
            from docx import Document
        except ImportError:
            raise SystemExit('Cần cài python-docx: pip install python-docx')

        doc = Document(str(duong_dan))
        phan = [p.text for p in doc.paragraphs]
        # Lấy cả nội dung trong bảng
        for bang in doc.tables:
            for hang in bang.rows:
                for o in hang.cells:
                    phan.append(o.text)
        return '\n'.join(phan)

    if hau_to in ('.md', '.txt'):
        return duong_dan.read_text(encoding='utf-8', errors='replace')

    raise SystemExit(f'Không hỗ trợ định dạng {hau_to} — dùng .docx, .md hoặc .txt')


def chuan_hoa(s: str) -> str:
    """Chuẩn hóa chuỗi: NFC, thường, gộp khoảng trắng."""
    s = unicodedata.normalize('NFC', s or '')
    return re.sub(r'\s+', ' ', s).strip().lower()


# ─────────────────────────────────────────────────────────────
# Nạp kho dữ liệu
# ─────────────────────────────────────────────────────────────

def nap_tu_dien() -> list:
    """Nạp Từ điển pháp lý từ KTC-Database (chỉ đọc)."""
    p = Path(ktc_database()) / '08-Tu-Dien-Phap-Ly' / 'tu_dien_index.json'
    if not p.exists():
        print(f'⚠️  Không đọc được Từ điển pháp lý tại {p}', file=sys.stderr)
        return []
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f).get('records', [])


def nap_hoi_dap() -> list:
    """Nạp Hỏi đáp chính sách từ KTC-Database (chỉ đọc)."""
    p = Path(ktc_database()) / '07-Hoi-Dap-Chinh-Sach' / 'hoi_dap_index.json'
    if not p.exists():
        return []
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f).get('records', [])


# ─────────────────────────────────────────────────────────────
# Tìm thuật ngữ trong văn bản
# ─────────────────────────────────────────────────────────────

def tim_xuat_hien(text_thuong: str, thuat_ngu: str) -> int:
    """
    Đếm số lần thuật ngữ xuất hiện, có ranh giới từ.
    Tiếng Việt không dùng \\b được vì dấu — dùng lookaround ký tự chữ.
    """
    mau = re.escape(chuan_hoa(thuat_ngu))
    # Ranh giới: không đứng liền chữ/số ở hai đầu
    bieu_thuc = r'(?<![^\W\d_])' + mau + r'(?![^\W\d_])'
    try:
        return len(re.findall(bieu_thuc, text_thuong, flags=re.UNICODE))
    except re.error:
        return text_thuong.count(chuan_hoa(thuat_ngu))


def quet_tu_dien(text: str, tu_dien: list) -> list:
    """
    Tìm các thuật ngữ của từ điển xuất hiện trong văn bản.
    Trả về danh sách (bản ghi, số lần).
    """
    text_thuong = chuan_hoa(text)
    ket_qua = []

    for r in tu_dien:
        tn = (r.get('Thuật ngữ') or '').strip()
        if len(tn) < DO_DAI_TOI_THIEU:
            continue
        if chuan_hoa(tn) not in text_thuong:
            continue
        so_lan = tim_xuat_hien(text_thuong, tn)
        if so_lan:
            ket_qua.append((r, so_lan))

    # Thuật ngữ dài đứng trước — để báo cáo ưu tiên khái niệm cụ thể
    ket_qua.sort(key=lambda x: -len(x[0].get('Thuật ngữ', '')))
    return ket_qua


def loai_bi_bao_phu(da_tim: list) -> list:
    """
    Bỏ thuật ngữ ngắn nằm trọn trong thuật ngữ dài hơn đã tìm thấy
    với số lần bằng nhau (vd: "viên chức" bên trong "viên chức quản lý").
    """
    giu = []
    for rec, so_lan in da_tim:
        tn = chuan_hoa(rec.get('Thuật ngữ', ''))
        bi_phu = False
        for rec_dai, so_lan_dai in giu:
            tn_dai = chuan_hoa(rec_dai.get('Thuật ngữ', ''))
            if tn != tn_dai and tn in tn_dai and so_lan <= so_lan_dai:
                bi_phu = True
                break
        if not bi_phu:
            giu.append((rec, so_lan))
    return giu


# ─────────────────────────────────────────────────────────────
# Các phép kiểm
# ─────────────────────────────────────────────────────────────

def kiem_tn02_hieu_luc(da_tim: list) -> list:
    """TN02 — thuật ngữ lấy từ văn bản hết hiệu lực hoặc chưa xác minh."""
    phat_hien = []
    for rec, so_lan in da_tim:
        tt = chuan_hoa(rec.get('Tình trạng hiệu lực', ''))
        if any(k in tt for k in HET_HIEU_LUC):
            muc = 2
            loai = 'Văn bản nguồn HẾT HIỆU LỰC — phải thay định nghĩa'
        elif any(k in tt for k in CAN_DOI_CHIEU):
            muc = 3
            loai = 'Nguồn đã sửa đổi — cần đối chiếu bản hợp nhất'
        elif any(k in tt for k in CHUA_XAC_MINH):
            muc = 4
            loai = 'Kho chưa xác minh nguồn (hạn chế của kho, không phải lỗi văn bản)'
        else:
            continue

        # Thuật ngữ phổ thông xuất hiện ở mọi văn bản — hạ xuống góp ý
        if chuan_hoa(rec.get('Thuật ngữ', '')) in THUAT_NGU_PHO_THONG:
            muc = max(muc, 4)

        phat_hien.append({
            'ma': 'TN02',
            'muc': muc,
            'thuat_ngu': rec.get('Thuật ngữ'),
            'so_lan': so_lan,
            'loai': loai,
            'tinh_trang': rec.get('Tình trạng hiệu lực'),
            'nguon': rec.get('Nguồn'),
            'ghi_chu': rec.get('Ghi chú', ''),
        })
    return phat_hien


def kiem_tn01_gan_dung(text: str, tu_dien: list, da_tim: list) -> list:
    """
    TN01 — cụm từ trong văn bản gần giống một thuật ngữ chuẩn nhưng không khớp.
    Chỉ xét các cụm danh từ ứng viên để tránh quét toàn bộ văn bản.
    """
    da_khop = {chuan_hoa(r.get('Thuật ngữ', '')) for r, _ in da_tim}
    chuan = {chuan_hoa(r.get('Thuật ngữ', '')): r
             for r in tu_dien
             if len(r.get('Thuật ngữ') or '') >= DO_DAI_TOI_THIEU}

    # Ứng viên: cụm 2–5 từ, chỉ nhận cụm TRỌN VẸN — hai đầu phải là ranh giới
    # câu hoặc hư từ. Nếu không, cụm chỉ là mảnh bị cắt giữa một cụm dài hơn
    # (vd "đào tạo lái" cắt từ "đào tạo lái xe") và sẽ sinh cảnh báo giả.
    cum = set()
    for doan in re.split(r'[.;:!?\n\r()\[\]"“”]+', chuan_hoa(text)):
        tu = doan.split()
        for n in range(2, 6):
            for i in range(len(tu) - n + 1):
                truoc = tu[i - 1] if i > 0 else None
                sau = tu[i + n] if i + n < len(tu) else None
                if truoc is not None and truoc not in HU_TU:
                    continue
                if sau is not None and sau not in HU_TU:
                    continue
                c = ' '.join(tu[i:i + n])
                if len(c) >= DO_DAI_TOI_THIEU and not re.search(r'\d', c):
                    cum.add(c)

    phat_hien = []
    da_bao = set()
    for c in cum:
        if c in chuan or c in da_khop:
            continue
        gan = difflib.get_close_matches(c, chuan.keys(), n=1, cutoff=NGUONG_GAN_DUNG)
        if not gan:
            continue
        goc = gan[0]
        if goc in da_khop or (c, goc) in da_bao:
            continue
        # Bỏ trường hợp chỉ khác hậu tố số nhiều/giới từ không đáng kể
        if c.replace(' ', '') == goc.replace(' ', ''):
            continue
        # Chỉ báo khi cùng số từ — khác biệt là lỗi chính tả/dấu, không phải
        # cụm khác nghĩa. Khác số từ thường là trùng hợp ngẫu nhiên.
        if len(c.split()) != len(goc.split()):
            continue
        if goc in THUAT_NGU_PHO_THONG:
            continue
        da_bao.add((c, goc))
        rec = chuan[goc]
        phat_hien.append({
            'ma': 'TN01',
            'muc': 3,
            'trong_van_ban': c,
            'thuat_ngu_chuan': rec.get('Thuật ngữ'),
            'do_giong': round(difflib.SequenceMatcher(None, c, goc).ratio(), 3),
            'nguon': rec.get('Nguồn'),
            'dinh_nghia': (rec.get('Định nghĩa') or '')[:200],
        })

    phat_hien.sort(key=lambda x: -x['do_giong'])
    return phat_hien[:20]


def kiem_tn03_nhat_quan(da_tim: list) -> list:
    """
    TN03 — cùng một khái niệm được gọi bằng nhiều thuật ngữ khác nhau.
    Nhận diện qua các thuật ngữ có định nghĩa rất giống nhau.
    """
    phat_hien = []
    ds = [(r, n) for r, n in da_tim if (r.get('Định nghĩa') or '').strip()]

    for i in range(len(ds)):
        for j in range(i + 1, len(ds)):
            a, b = ds[i][0], ds[j][0]
            tn_a, tn_b = a.get('Thuật ngữ', ''), b.get('Thuật ngữ', '')
            if chuan_hoa(tn_a) in chuan_hoa(tn_b) or chuan_hoa(tn_b) in chuan_hoa(tn_a):
                continue
            dn_a = chuan_hoa(a.get('Định nghĩa', ''))[:300]
            dn_b = chuan_hoa(b.get('Định nghĩa', ''))[:300]
            if not dn_a or not dn_b:
                continue
            giong = difflib.SequenceMatcher(None, dn_a, dn_b).ratio()
            if giong >= 0.80:
                phat_hien.append({
                    'ma': 'TN03',
                    'muc': 3,
                    'cap': (tn_a, tn_b),
                    'do_giong_dinh_nghia': round(giong, 3),
                    'nguon_a': a.get('Nguồn'),
                    'nguon_b': b.get('Nguồn'),
                })

    phat_hien.sort(key=lambda x: -x['do_giong_dinh_nghia'])
    return phat_hien[:10]


def kiem_tn04_hoi_dap(da_tim: list, hoi_dap: list, toi_da: int = 8) -> list:
    """TN04 — gợi ý hỏi đáp chính sách liên quan tới thuật ngữ trong văn bản."""
    if not hoi_dap:
        return []

    # Chỉ dùng thuật ngữ đặc thù (dài, không phổ thông)
    tu_khoa = [r.get('Thuật ngữ', '') for r, _ in da_tim
               if len(r.get('Thuật ngữ') or '') >= 10
               and chuan_hoa(r.get('Thuật ngữ', '')) not in THUAT_NGU_PHO_THONG]

    cham_diem = []
    for hd in hoi_dap:
        cau_hoi = str(hd.get('Nội dung câu hỏi', '') or '')
        tra_loi = str(hd.get('Nội dung trả lời', '') or '')
        noi_dung = chuan_hoa(cau_hoi + ' ' + tra_loi)
        if not noi_dung:
            continue

        khop = [tn for tn in tu_khoa if chuan_hoa(tn) in noi_dung]
        if not khop:
            continue

        # Một thuật ngữ chung chung khớp là trùng hợp. Chỉ nhận khi khớp nhiều
        # thuật ngữ, hoặc khớp một thuật ngữ rất đặc thù.
        dac_thu = max(len(t) for t in khop)
        if len(khop) < 2 and dac_thu < 18:
            continue

        tom_tat = re.sub(r'\s+', ' ', cau_hoi).strip()
        if len(tom_tat) > 130:
            tom_tat = tom_tat[:130].rsplit(' ', 1)[0] + '…'

        cham_diem.append((len(khop), dac_thu, {
            'ma': 'TN04',
            'muc': 4,
            'thuat_ngu': ', '.join(sorted(khop, key=len, reverse=True)[:3]),
            'so_khop': len(khop),
            'tom_tat': tom_tat or '(không có nội dung câu hỏi)',
            'co_quan': hd.get('Cơ quan trả lời', ''),
            'nguon': hd.get('Nguồn', ''),
            'link': hd.get('Link', ''),
            'truc': hd.get('Trục TB 817', ''),
        }))

    cham_diem.sort(key=lambda x: (-x[0], -x[1]))
    return [x[2] for x in cham_diem[:toi_da]]


# ─────────────────────────────────────────────────────────────
# Báo cáo
# ─────────────────────────────────────────────────────────────

def dung_bao_cao(ten_tep: str, da_tim: list, kq: dict, tong_tu_dien: int) -> str:
    """Dựng báo cáo Markdown."""
    d = []
    d.append(f'# Báo cáo kiểm thuật ngữ pháp lý — {ten_tep}\n')
    d.append(f'Đối chiếu kho `08-Tu-Dien-Phap-Ly` ({tong_tu_dien} thuật ngữ) '
             f'và `07-Hoi-Dap-Chinh-Sach`.\n')
    d.append('> Lớp kiểm độc lập, **không thay** rà soát KTC-Ra-Soat-897 trước trình ký.\n')

    tn01, tn02, tn03, tn04 = kq['TN01'], kq['TN02'], kq['TN03'], kq['TN04']
    loi = [x for x in tn02 if x['muc'] <= 2]

    d.append('\n## Tổng hợp\n')
    d.append('| Phép kiểm | Nội dung | Số phát hiện |')
    d.append('|---|---|---|')
    d.append(f'| TN01 | Thuật ngữ gần đúng, chưa chuẩn | {len(tn01)} |')
    tn02_that = [x for x in tn02 if x['muc'] <= 3]
    tn02_kho = [x for x in tn02 if x['muc'] == 4]
    d.append(f'| TN02 | Nguồn hết hiệu lực / đã sửa đổi | {len(tn02_that)} |')
    d.append(f'| TN02b | Kho chưa xác minh nguồn (tham khảo) | {len(tn02_kho)} |')
    d.append(f'| TN03 | Không nhất quán thuật ngữ | {len(tn03)} |')
    d.append(f'| TN04 | Hỏi đáp chính sách liên quan | {len(tn04)} |')
    d.append(f'\n**Thuật ngữ nhận diện được trong văn bản:** {len(da_tim)}\n')

    ket_luan = ('⚠️ CÓ vấn đề Mức 1–2 — cần sửa trước khi trình ký'
                if loi else '✓ Không có vấn đề Mức 1–2 về thuật ngữ')
    d.append(f'**Kết luận:** {ket_luan}\n')

    if tn02_that:
        d.append('\n## TN02 — Hiệu lực nguồn thuật ngữ (cần xử lý)\n')
        for x in sorted(tn02_that, key=lambda i: i['muc']):
            d.append(f"### {x['thuat_ngu']} — {MUC_TEN[x['muc']]}")
            d.append(f"- **Vấn đề:** {x['loai']}")
            d.append(f"- **Tình trạng:** {x['tinh_trang']}")
            d.append(f"- **Nguồn:** {x['nguon']}")
            d.append(f"- **Số lần dùng:** {x['so_lan']}")
            if x['ghi_chu']:
                d.append(f"- **Ghi chú kho:** {x['ghi_chu']}")
            d.append('')

    if tn02_kho:
        d.append('\n## TN02b — Thuật ngữ kho chưa xác minh nguồn\n')
        d.append('Đây là **hạn chế của kho từ điển**, không phải lỗi của văn bản. '
                 'Nếu thuật ngữ là khái niệm then chốt, nên tự đối chiếu văn bản gốc.\n')
        d.append('| Thuật ngữ | Lần dùng | Nguồn kho ghi |')
        d.append('|---|---|---|')
        for x in sorted(tn02_kho, key=lambda i: -i['so_lan']):
            d.append(f"| {x['thuat_ngu']} | {x['so_lan']} | {x['nguon']} |")
        d.append('')

    if tn01:
        d.append('\n## TN01 — Thuật ngữ gần đúng\n')
        d.append('| Trong văn bản | Thuật ngữ chuẩn | Giống | Nguồn chuẩn |')
        d.append('|---|---|---|---|')
        for x in tn01:
            d.append(f"| {x['trong_van_ban']} | **{x['thuat_ngu_chuan']}** | "
                     f"{x['do_giong']} | {x['nguon']} |")
        d.append('\n> Kiểm lại từng dòng: khác biệt có thể là cố ý theo ngữ cảnh.\n')

    if tn03:
        d.append('\n## TN03 — Nhất quán thuật ngữ\n')
        for x in tn03:
            a, b = x['cap']
            d.append(f"- **{a}** ↔ **{b}** (định nghĩa giống {x['do_giong_dinh_nghia']})")
            d.append(f"  - {a}: {x['nguon_a']}")
            d.append(f"  - {b}: {x['nguon_b']}")
        d.append('\n> Cùng một khái niệm nên dùng thống nhất một thuật ngữ trong toàn văn bản.\n')

    if tn04:
        d.append('\n## TN04 — Hỏi đáp chính sách liên quan (tham khảo)\n')
        for x in tn04:
            d.append(f"- 💬 **{x['thuat_ngu']}** ({x['so_khop']} thuật ngữ khớp) — {x['tom_tat']}")
            if x.get('co_quan'):
                d.append(f"  - Cơ quan trả lời: {x['co_quan']}")
            if x.get('link'):
                d.append(f"  - {x['link']}")
            elif x.get('nguon'):
                d.append(f"  - Nguồn: {x['nguon']}")
        d.append('\n> Hỏi đáp là **tham khảo**, không phải căn cứ pháp lý để viện dẫn.\n')

    if da_tim:
        d.append('\n## Phụ lục — Thuật ngữ nhận diện được\n')
        d.append('| Thuật ngữ | Lần | Lĩnh vực | Tình trạng | Nguồn |')
        d.append('|---|---|---|---|---|')
        for r, n in da_tim[:60]:
            d.append(f"| {r.get('Thuật ngữ')} | {n} | {r.get('Lĩnh vực', '')} | "
                     f"{r.get('Tình trạng hiệu lực', '')} | {r.get('Nguồn', '')} |")
        if len(da_tim) > 60:
            d.append(f'\n_… còn {len(da_tim) - 60} thuật ngữ nữa._')

    d.append('\n---\n')
    d.append('📖 Nguồn đối chiếu: `KTC-Database/08-Tu-Dien-Phap-Ly`, '
             '`KTC-Database/07-Hoi-Dap-Chinh-Sach`')
    return '\n'.join(d)


# ─────────────────────────────────────────────────────────────
# Giao diện dòng lệnh
# ─────────────────────────────────────────────────────────────

def kiem_tra(duong_dan: Path, linh_vuc: str = None) -> dict:
    """Chạy toàn bộ phép kiểm, trả kết quả dạng dict."""
    text = doc_van_ban(duong_dan)
    tu_dien = nap_tu_dien()

    if linh_vuc:
        tu_dien = [r for r in tu_dien if r.get('Lĩnh vực') == linh_vuc]

    hoi_dap = nap_hoi_dap()

    da_tim = loai_bi_bao_phu(quet_tu_dien(text, tu_dien))

    return {
        'text': text,
        'tu_dien': tu_dien,
        'da_tim': da_tim,
        'TN01': kiem_tn01_gan_dung(text, tu_dien, da_tim),
        'TN02': kiem_tn02_hieu_luc(da_tim),
        'TN03': kiem_tn03_nhat_quan(da_tim),
        'TN04': kiem_tn04_hoi_dap(da_tim, hoi_dap),
    }


def main():
    ap = argparse.ArgumentParser(
        description='Kiểm thuật ngữ pháp lý trong văn bản, đối chiếu kho 08-Tu-Dien-Phap-Ly')
    ap.add_argument('tep', help='Tệp cần kiểm (.docx, .md, .txt)')
    ap.add_argument('--linh-vuc', help='Chỉ đối chiếu 1 lĩnh vực (giao-duc, vien-chuc, …)')
    ap.add_argument('--xuat', help='Ghi báo cáo ra tệp .md')
    ap.add_argument('--json', action='store_true', help='In kết quả dạng JSON')
    args = ap.parse_args()

    tep = Path(args.tep)
    if not tep.exists():
        raise SystemExit(f'Không tìm thấy tệp: {tep}')

    kq = kiem_tra(tep, args.linh_vuc)

    if args.json:
        ra = {k: v for k, v in kq.items() if k.startswith('TN')}
        ra['so_thuat_ngu_nhan_dien'] = len(kq['da_tim'])
        print(json.dumps(ra, ensure_ascii=False, indent=2))
        return

    bao_cao = dung_bao_cao(tep.name, kq['da_tim'], kq, len(kq['tu_dien']))

    if args.xuat:
        p = Path(args.xuat)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(bao_cao, encoding='utf-8')
        print(f'Đã ghi báo cáo: {p}')
    else:
        print(bao_cao)

    # Mã thoát: 1 nếu có vấn đề Mức 1–2
    if any(x['muc'] <= 2 for x in kq['TN02']):
        sys.exit(1)


if __name__ == '__main__':
    main()
