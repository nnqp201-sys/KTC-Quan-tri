# -*- coding: utf-8 -*-
"""
fill_bc736.py — Điền nội dung vào mẫu Báo cáo tháng cấp Trường (TB736).
Phiên bản: v3.2 (19/08/2026) — GHÉP v2.5.1 (đối chiếu độc lập, sửa BUG-10..14,
xem PATCH-NOTES-v2.5.1.md) + cơ chế content_by_phase của v3.1 (xác nhận file
thật 18/08/2026: nhiều đoạn bôi vàng GIỐNG HỆT NHAU ở Phần I và Phần III —
VD "công tác tuyển sinh" xuất hiện y hệt ở cả 2 Phần, và cả 8 Nghị quyết Bộ
Chính trị dùng chung 1 đoạn bôi vàng — nếu dùng 1 content_map chung sẽ điền
NHẦM nội dung kết quả sang kế hoạch. Đã kiểm chứng: khóa (Phần, nhãn) cho ra
45/45 vị trí duy nhất trên file mẫu thật.

Giữ nguyên định dạng gốc (font, quốc hiệu, bảng ký tên) VÀ giữ nguyên
nhãn in đậm đầu dòng (VD "* Công tác tuyển sinh: ").

3 loại đoạn xử lý khác nhau:
1. Đoạn có bôi vàng -> chỉ thay phần BÔI VÀNG bằng nội dung thật (nhãn đen giữ nguyên)
2. Đoạn đỏ chứa "tháng […] ... năm 20[…]" (không bôi vàng) -> điền kỳ báo cáo
3. Khối "Số: […]/BC-CĐKT" và "ngày … tháng … năm 20…" -> GIỮ NGUYÊN (Văn thư cấp khi phát hành)
"""
import re
import unicodedata
from docx import Document
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

RED = "EE0000"
GRAY_ITALIC = RGBColor(0x80, 0x80, 0x80)
BLACK = RGBColor(0, 0, 0)

# [GHÉP v3.1] 3 Phần của báo cáo — nhiều đoạn bôi vàng GIỐNG HỆT NHAU giữa các Phần
# (đã kiểm chứng trên file thật), nên PHẢI phân biệt content theo Phần, không dùng
# chung 1 content_map — nếu không nội dung Phần I sẽ bị chèn nhầm sang Phần III.
PHASE_HEADERS = {
    "I. KẾT QUẢ": "PHAN_I",
    "II. ĐÁNH GIÁ": "PHAN_II",
    "III. NHIỆM VỤ": "PHAN_III",
}





def _norm(s):
    return unicodedata.normalize("NFC", " ".join(str(s or "").split())).lower()


def iter_all_paragraphs(doc):
    """[VÁ BUG-12] Duyệt CẢ đoạn trong bảng (kể cả bảng lồng nhau) — mẫu TB736
    có quốc hiệu, khối ký tên và đôi khi cả nội dung nằm trong bảng."""
    for p in doc.paragraphs:
        yield p
    def walk(tables):
        for tb in tables:
            for row in tb.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        yield p
                    for p in walk(cell.tables):
                        yield p
    for p in walk(doc.tables):
        yield p


def is_placeholder_paragraph(p):
    for r in p.runs:
        col = r.font.color
        if col is not None and col.type is not None and col.rgb is not None \
                and str(col.rgb) == RED:
            return True
    return False


def has_yellow(p):
    return any(r.font.highlight_color for r in p.runs)


def is_document_control_line(text):
    """[VÁ BUG-14] Số hiệu văn bản / ngày ký — KHÔNG tự điền.
    Nhận cả dạng ngoặc vuông '[…]' lẫn dạng chấm lửng '…'."""
    t = " ".join(str(text or "").split())
    if re.match(r"^\s*Số\s*[:.]?\s", t):
        return True
    # "Quảng Ngãi, ngày ... tháng ... năm 20..." (địa danh + ngày ký)
    if re.search(r"ngày\s*[\[\u2026.\]]+\s*tháng\s*[\[\u2026.\]]+\s*năm", t):
        return True
    return False


def clear_paragraph_runs(p):
    for r in list(p.runs):
        r._element.getparent().remove(r._element)


def _style_run(run, italic=False, color=BLACK, bold=None):
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), "Times New Roman")
    run.font.name = "Times New Roman"
    run.font.color.rgb = color
    run.font.italic = italic
    if bold is not None:
        run.font.bold = bold
    run.font.highlight_color = None
    return run


def write_plain_text(p, text, italic=False, color=BLACK, bold=None):
    return _style_run(p.add_run(text), italic=italic, color=color, bold=bold)


def _replace_yellow_runs(p, text, italic=False, color=BLACK):
    """[VÁ BUG-11 + SỬA v3.2] Thay TOÀN BỘ run màu ĐỎ (không chỉ phần bôi vàng),
    giữ nguyên nhãn đen in đậm đầu dòng.

    Lý do sửa: trên file mẫu THẬT, cụm đỏ hướng dẫn thường DÀI HƠN phần bôi vàng
    (VD "[…lấy kết quả thực hiện" + "công tác tuyển sinh" (bôi vàng) + "của phòng X]. "
    + "{Lưu ý nguyên tắc: ...}" — tất cả đều đỏ, chỉ 1 đoạn giữa được bôi vàng thêm).
    Nếu chỉ xoá run bôi vàng (cách cũ), phần đỏ bao quanh KHÔNG BÔI VÀNG sẽ bị sót lại
    nguyên trong báo cáo cuối — lỗi phát hiện 19/08/2026 khi kiểm thử trên file thật.
    Nội dung được ghi vào run đỏ ĐẦU TIÊN; các run đỏ còn lại bị xoá."""
    red_runs = [r for r in p.runs
                if r.font.color and r.font.color.type and str(r.font.color.rgb) == RED]
    if not red_runs:
        return False
    first = red_runs[0]
    first.text = text
    _style_run(first, italic=italic, color=color)
    for r in red_runs[1:]:
        r._element.getparent().remove(r._element)
    return True


def _match_key(key_norm, norm_map):
    """[VÁ BUG-10] Khớp khóa an toàn, tránh khớp nhầm chuỗi con.
    Thứ tự ưu tiên: (1) khớp tuyệt đối -> (2) khớp chuỗi con DÀI NHẤT, và chỉ
    chấp nhận nếu không có khóa nào khác cùng độ dài gây nhập nhằng.
    Trả về (giá_trị, khóa_gốc, cảnh_báo)."""
    if key_norm in norm_map:
        k, v = norm_map[key_norm]
        return v, k, None

    cands = [(kn, k, v) for kn, (k, v) in norm_map.items()
             if kn and (kn in key_norm or key_norm in kn)]
    if not cands:
        return None, None, None
    cands.sort(key=lambda x: len(x[0]), reverse=True)
    best_len = len(cands[0][0])
    tied = [c for c in cands if len(c[0]) == best_len]
    warn = None
    if len(tied) > 1:
        warn = (f"Khóa '{key_norm[:50]}' khớp nhập nhằng với {len(tied)} khóa "
                f"cùng độ dài — đã dùng '{tied[0][1][:40]}'. Nên đặt khóa khớp tuyệt đối.")
    elif len(cands) > 1:
        warn = (f"Khóa '{key_norm[:50]}' khớp chuỗi con (không tuyệt đối) với "
                f"'{cands[0][1][:40]}'. Kiểm tra lại cho chắc.")
    return cands[0][2], cands[0][1], warn


def fill_report(template_path, output_path, content_by_phase, thang_ket_qua, thang_ke_hoach, nam,
                missing_note_prefix="[CẦN BỔ SUNG"):
    """
    Điền báo cáo. Trả về dict thống kê + danh sách cảnh báo để người tổng hợp rà lại.

    content_by_phase: dict 3 khóa con — BẮT BUỘC tách riêng theo Phần:
        {
          "PHAN_I":   { "<nhãn>": "<nội dung KẾT QUẢ, chủ thể Nhà trường>", ... },
          "PHAN_II":  { "kết quả đạt được": "...", "tồn tại, hạn chế": "..." },
          "PHAN_III": { "<nhãn>": "<nội dung KẾ HOẠCH, chủ thể Nhà trường>", ... },
        }
        Nhãn nên lấy nguyên văn hoặc gần đúng cụm bôi vàng/tiêu đề mục trong mẫu.
    """
    # [SỬA v3.4 — XUNG ĐỘT 1] Kiểm tra CẤU TRÚC đầu vào trước khi chạy.
    # Bug cũ: truyền nhầm dict phẳng (VD kết quả build_content_map_skeleton()) sẽ
    # crash với "AttributeError: 'str' object has no attribute 'items'" — thông báo
    # vô nghĩa với người dùng. Giờ báo lỗi rõ ràng, chỉ đúng cách sửa.
    VALID_PHASES = {"PHAN_I", "PHAN_II", "PHAN_III", "HEADER"}
    if not isinstance(content_by_phase, dict):
        raise TypeError(
            "content_by_phase phải là dict 3 tầng {'PHAN_I': {...}, 'PHAN_II': {...}, "
            f"'PHAN_III': {{...}}}}, nhận được {type(content_by_phase).__name__}.")
    for ph, cmap in content_by_phase.items():
        if not isinstance(cmap, dict):
            raise TypeError(
                f"content_by_phase['{ph}'] phải là dict {{nhãn: nội dung}}, nhận được "
                f"{type(cmap).__name__}. Nếu đang dùng build_content_map_skeleton(), "
                "hàm đó trả về dict PHẲNG — phải phân loại lại vào PHAN_I/PHAN_II/PHAN_III "
                "trước khi gọi fill_report(). Xem README-fill_bc736.md.")

    doc = Document(template_path)
    filled = missing = skipped_control = 0
    missing_list, warnings = [], []

    # [SỬA v3.4 — XUNG ĐỘT 5] Cảnh báo NGAY nếu tên Phần sai (VD 'phan_i' viết thường,
    # 'PHANI' thiếu gạch dưới). Bug cũ: im lặng bỏ qua toàn bộ nội dung của Phần đó,
    # chỉ báo mơ hồ "gõ sai tên KHÓA" trong khi lỗi thật là sai tên PHẦN.
    for ph in content_by_phase:
        if ph not in VALID_PHASES:
            warnings.append(
                f"[TÊN PHẦN SAI] '{ph}' không hợp lệ — phải là PHAN_I / PHAN_II / PHAN_III "
                f"(viết HOA, có gạch dưới). Toàn bộ {len(content_by_phase[ph])} nội dung "
                "trong phần này sẽ KHÔNG được điền.")

    norm_maps = {}
    used_keys = {}
    for ph, cmap in content_by_phase.items():
        nm = {_norm(k): (k, v) for k, v in cmap.items()}
        if len(nm) < len(cmap):
            warnings.append(f"[{ph}] Có khóa content_map trùng nhau sau khi chuẩn hoá — kiểm tra lại.")
        norm_maps[ph] = nm
        used_keys[ph] = set()

    # [SỬA v3.2] Theo dõi Phần NGAY TRONG vòng lặp chính (1 lần duyệt duy nhất) —
    # KHÔNG dùng pre-pass riêng: doc.paragraphs tạo Paragraph wrapper MỚI mỗi lần
    # gọi property, khiến id(p) VÀ id(p._element) không đáng tin cậy để đối chiếu
    # giữa 2 lần duyệt khác nhau (đã kiểm chứng bằng lỗi thật trên file mẫu 19/08/2026).
    phase = "HEADER"
    last_heading = ""   # [GHÉP v3.1] nhãn gần nhất — CẦN để phân biệt các placeholder
    # dùng CHUNG 1 đoạn bôi vàng (VD 8 Nghị quyết Bộ Chính trị đều bôi vàng giống hệt
    # nhau, chỉ phân biệt được nhờ đoạn tiêu đề "* Nghị quyết số NN-NQ/TW..." RIÊNG
    # đứng ngay phía trước — xác nhận lỗi thật 19/08/2026 khi kiểm thử trên file mẫu).
    for p in iter_all_paragraphs(doc):
        text_check = p.text.strip()
        for marker, ph_new in PHASE_HEADERS.items():
            if text_check.startswith(marker):
                phase = ph_new
                break
        if not is_placeholder_paragraph(p):
            if text_check and any(r.bold for r in p.runs) and len(text_check) > 3:
                last_heading = text_check
            continue
        full_text = "".join(r.text for r in p.runs)

        # (3) Số hiệu / ngày ký — không đụng
        if is_document_control_line(full_text):
            skipped_control += 1
            continue

        # (2) Câu boilerplate kỳ báo cáo (không bôi vàng)
        if not has_yellow(p) and "tháng" in full_text and ("[" in full_text or "…" in full_text):
            was_bold = any(r.bold for r in p.runs)
            new_text = (full_text
                        .replace("tháng […]", f"tháng {thang_ket_qua}", 1)
                        .replace("tháng […]", f"tháng {thang_ke_hoach}", 1)
                        .replace("tháng [...]", f"tháng {thang_ket_qua}", 1)
                        .replace("tháng [...]", f"tháng {thang_ke_hoach}", 1)
                        .replace("20[…]", str(nam)).replace("20[...]", str(nam)))
            clear_paragraph_runs(p)
            write_plain_text(p, new_text, bold=was_bold if was_bold else None)
            filled += 1
            continue

        # (1) Nội dung báo cáo thật — phần bôi vàng
        if not has_yellow(p):
            continue
        key_norm = _norm("".join(r.text for r in p.runs if r.font.highlight_color))
        if not key_norm:
            continue

        # [GHÉP v3.1 — SỬA LẦN 2] Nhãn nhận diện — cấu trúc mẫu thật KHÔNG đồng nhất
        # giữa các vị trí Nghị quyết (xác nhận 19/08/2026): có vị trí nhãn nằm CHUNG
        # đoạn với placeholder (VD NQ59, NQ66), có vị trí nhãn nằm ở đoạn RIÊNG phía
        # trước (VD NQ68, NQ70, NQ71, NQ79).
        #
        # ⚠️ KHÔNG được nối black_prefix + last_heading rồi tìm chung — nếu 2 Nghị quyết
        # liên tiếp đều thuộc kiểu "đoạn riêng", last_heading còn sót giá trị CŨ (từ NQ
        # trước) khi xử lý placeholder của NQ hiện tại. Nối chung 2 nguồn khiến CẢ 2 số
        # NQ (đúng lẫn sai) cùng khớp được trong _match_key, và vì độ dài nhãn bằng nhau
        # (2 chữ số), hàm chọn nhầm theo thứ tự khai báo trong dict thay vì đúng ngữ cảnh
        # — lỗi thật đã phát hiện qua kiểm thử 8/8 Nghị quyết (trước đó chỉ test 2/8 nên
        # không lộ ra). SỬA: ưu tiên black_prefix (nhãn CÙNG đoạn, luôn đúng ngữ cảnh);
        # CHỈ dùng last_heading khi black_prefix không đủ nghĩa (đoạn placeholder không
        # tự mang nhãn) — không bao giờ dùng cả hai cùng lúc.
        black_prefix = "".join(
            r.text for r in p.runs
            if not (r.font.color and r.font.color.type and str(r.font.color.rgb) == RED)
        ).strip()
        meaningful = black_prefix.strip(" *.:")
        label = black_prefix if len(meaningful) > 3 else last_heading
        search_text = _norm(label + " " + key_norm)
        value, orig_key, warn = _match_key(search_text, norm_maps.get(phase, {}))
        if warn:
            warnings.append(f"[{phase}] " + warn)

        if value:
            _replace_yellow_runs(p, str(value))
            used_keys.setdefault(phase, set()).add(orig_key)
            filled += 1
        else:
            _replace_yellow_runs(p, f"{missing_note_prefix} [{phase}]: {key_norm}]",
                                 italic=True, color=GRAY_ITALIC)
            missing += 1
            missing_list.append((phase, key_norm))

    # (4) Tiêu đề Mục I / III — ngoặc tháng có thể không tô đỏ trong mẫu gốc
    for p in iter_all_paragraphs(doc):
        t = p.text.strip()
        if not (("…" in t) or ("[" in t)):
            continue
        if t.startswith("I. KẾT QUẢ THỰC HIỆN"):
            thang = thang_ket_qua
        elif t.startswith("III. NHIỆM VỤ TRỌNG TÂM"):
            thang = thang_ke_hoach
        else:
            continue
        new_text = re.sub(r"THÁNG\s*[\[\u2026\].]+", f"THÁNG {thang}", t)
        new_text = re.sub(r"NĂM\s*20[\[\u2026\].]+", f"NĂM {nam}", new_text)
        clear_paragraph_runs(p)
        write_plain_text(p, new_text, bold=True)
        filled += 1

    # [VÁ BUG-13, ghép theo Phần] Báo khóa content_map không dùng đến -> phát hiện gõ sai khóa
    unused_all = []
    for ph, cmap in content_by_phase.items():
        unused_ph = [k for k in cmap if k not in used_keys.get(ph, set())]
        if unused_ph:
            warnings.append(f"[{ph}] Khóa content_map KHÔNG được dùng (có thể gõ sai tên khóa): "
                            + "; ".join(str(u)[:45] for u in unused_ph))
            unused_all.extend((ph, u) for u in unused_ph)

    doc.save(output_path)
    return {"filled": filled, "missing": missing, "skipped_control": skipped_control,
            "missing_list": missing_list, "unused_keys": unused_all, "canh_bao": warnings}
