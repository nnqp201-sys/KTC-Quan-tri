# -*- coding: utf-8 -*-
"""
read_bc736_excel.py — Đọc Phụ lục Excel TB736 (Ia/Ib/IIb/IIc).
Phiên bản: v3.3 (18/09/2026) — thêm đọc cột Task_ID (KI-001). Trước đó: v3.2 (19/08/2026) — GHÉP v2.5.1 (đối chiếu độc lập, sửa BUG-01..09,
xem PATCH-NOTES-v2.5.1.md) + logic tách Mục II của v3.1 (xác nhận từ file thật
18/08/2026 — nhiệm vụ "chưa hoàn thành, chuyển sang tháng sau" ở Mục II KHÔNG
được gán vào Trục cuối cùng của Mục I).

Chức năng:
  1. Nhận diện loại Phụ lục (KH hay KQ) — quét cả hàng tiêu đề gộp phía trên.
  2. Trích xuất nhiệm vụ theo từng Trục (1-6), kèm Đơn vị chủ trì.
  3. Với IIb/IIc: kiểm tra TOÀN BỘ chuỗi công thức KPI cascade, tính % theo Trục.
  4. Với Ia/Ib: lọc theo cột Ghi chú (chuẩn hoá khoảng trắng/hoa-thường).
  5. Tách riêng dòng "Tổng cộng" khỏi danh sách nhiệm vụ (tránh cộng dồn 2 lần).
  6. Dựng khung content_map thô cho fill_bc736.py.

NGUYÊN TẮC: KHÔNG tự sửa số liệu. Phát hiện sai -> ghi vào "canh_bao" để đơn vị chỉnh.
"""
import re
import unicodedata
from openpyxl import load_workbook

TRUC_NAMES = {
    1: "Thực hiện mục tiêu phát triển kinh tế - xã hội và nhiệm vụ chính trị được giao",
    2: "Hoàn thiện thể chế, đẩy mạnh phân cấp, phân quyền gắn với kiểm tra, giám sát",
    3: "Thúc đẩy phát triển khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số",
    4: "Xây dựng Đảng và hệ thống chính trị trong sạch, vững mạnh; phòng, chống tham nhũng, lãng phí, tiêu cực",
    5: "Phát triển văn hóa, con người, bảo đảm an sinh xã hội, nâng cao đời sống Nhân dân",
    6: "Củng cố quốc phòng, an ninh, giữ vững ổn định chính trị - xã hội, nâng cao hiệu quả đối ngoại và hội nhập quốc tế",
}

# [VÁ BUG-02] Cho phép nhãn Trục có HOẶC KHÔNG có số thứ tự dẫn đầu:
#   "Trục 1. ..." | "1. Trục 1. ..." | "1) Trục (1)" | "TRỤC 1 -"
TRUC_HEADER_RE = re.compile(
    r"^\s*(?:\d+\s*[.,)\-]?\s*)?Trục\s*\(?\s*([1-6])\s*\)?\s*[.,)\-:]?", re.IGNORECASE)

# Ghi chú hợp lệ theo SKILL.md (2 giá trị chuẩn để lọc + 2 dạng phát sinh hợp lệ)
GHI_CHU_LOC_LEN_TRUONG = "đưa vào kh trường"
GHI_CHU_HOP_LE = {
    "đưa vào kh trường",
    "thường xuyên của đơn vị",
    "bổ sung ngoài kh quý",
    "kết luận giao ban",
}


def _norm(s):
    """Chuẩn hoá: bỏ khoảng trắng thừa, đưa về chữ thường, chuẩn Unicode NFC."""
    if s is None:
        return ""
    return unicodedata.normalize("NFC", " ".join(str(s).split())).lower()


def _is_sum_row(col0, col1):
    """[VÁ BUG-03] Nhận diện dòng Tổng/Cộng để KHÔNG tính là nhiệm vụ.
    [v3.3] Dòng có số thứ tự nhiệm vụ (1.1, 2.3…) KHÔNG BAO GIỜ là dòng cộng — trước đây nhiệm vụ
    "Tổng hợp…", "Tổng kết…" bị bỏ mất (2 nhiệm vụ thật của DT-CDCS kỳ 9/2026)."""
    if re.match(r"^\d+(\.\d+)+\.?$", str(col0).strip()):
        return False
    t = _norm(col1) or _norm(col0)
    return t.startswith("tổng") or t.startswith("cộng") or t.startswith("tổng cộng")


def _num(v):
    """Ép kiểu số an toàn, chấp nhận '1,5' kiểu Việt Nam. Trả None nếu không phải số."""
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.strip().replace("%", "")
        if "," in s and "." not in s:
            s = s.replace(",", ".")
        try:
            return float(s)
        except ValueError:
            return None
    return None


def _close(a, b, tol=0.011):
    return a is not None and b is not None and abs(a - b) <= tol


def _detect_kind(rows, header_idx):
    """
    [VÁ BUG-01] Nhận diện loại Phụ lục.
    Quét cửa sổ 3 hàng (2 hàng trên + hàng TT) vì tiêu đề 'KPI' thường nằm ở
    hàng gộp (merged) PHÍA TRÊN hàng chứa 'TT'. Có nhánh dự phòng theo số cột.
    """
    lo = max(0, header_idx - 2)
    window = rows[lo:header_idx + 1]
    text = _norm(" ".join(str(c) for r in window if r for c in r if c))
    header = rows[header_idx]
    ncol = len([c for c in header if c is not None]) if header else 0

    if "kpi" in text:
        return "KQ", None
    if "ghi chú" in text and ("điểm chấm" in text or "hệ số" in text):
        return "KH", None
    # Dự phòng theo số cột thực tế (KQ = 16 cột, KH = 11 cột)
    if ncol >= 15:
        return "KQ", "Không thấy chữ 'KPI' ở tiêu đề — suy ra Phụ lục KẾT QUẢ theo số cột (%d cột). Cần xác nhận." % ncol
    if 10 <= ncol <= 12:
        return "KH", "Không thấy tiêu đề chuẩn — suy ra Phụ lục KẾ HOẠCH theo số cột (%d cột). Cần xác nhận." % ncol
    return None, "KHÔNG nhận diện được loại Phụ lục (số cột=%d). Kiểm tra lại file có đúng mẫu TB736 không." % ncol


MAU_TASK_ID = re.compile(r"^KTC-\d{4}-(Q[1-4]|T(0[1-9]|1[0-2])|NAM|CD)-\d{5}$")


def _doc_task_id(row, col, task, canh_bao, da_gap):
    """[v3.3] Doc Task_ID neu co cot. Chi CANH BAO khi sai dinh dang/trung — khong tu sua, khong tu cap ma."""
    if col is None or len(row) <= col or row[col] is None or not str(row[col]).strip():
        return None
    v = str(row[col]).strip().upper()
    ten = str(task["noi_dung"])[:45]
    if not MAU_TASK_ID.match(v):
        canh_bao.append(f"[TASK_ID SAI ĐỊNH DẠNG] '{ten}': {v!r} — đúng dạng KTC-2026-Q3-00125 "
                        f"(01-Chuan-Chung/11-Quy-Tac-Task-ID.md).")
    if v in da_gap:
        canh_bao.append(f"[TASK_ID TRÙNG] {v} dùng cho cả '{da_gap[v]}' và '{ten}'.")
    da_gap.setdefault(v, ten)
    return v


def read_appendix(path, sheet_name=None):
    """
    Đọc 1 sheet Phụ lục TB736.
    Trả về dict: kind / truc / truc_tong / muc_ii_items / canh_bao / thong_ke
    """
    wb = load_workbook(path, data_only=True)
    ws = wb[sheet_name] if sheet_name else wb.active

    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return {"kind": None, "truc": {}, "truc_tong": {}, "muc_ii_items": [],
                "canh_bao": ["Sheet rỗng."], "thong_ke": {}}

    header_idx = None
    for i, row in enumerate(rows):
        if row and row[0] is not None and _norm(row[0]) == "tt":
            header_idx = i
            break
    if header_idx is None:
        return {"kind": None, "truc": {}, "truc_tong": {}, "muc_ii_items": [],
                "canh_bao": ["Không tìm thấy dòng tiêu đề cột (ô đầu tiên = 'TT'). "
                             "Kiểm tra lại file có đúng mẫu TB736 không."],
                "thong_ke": {}}

    kind, kind_note = _detect_kind(rows, header_idx)
    canh_bao = []
    # [v3.3 — KI-001, Lãnh đạo thống nhất 18/9/2026] Cột Task_ID thêm vào CUỐI bảng (Ia/Ib: L, IIb/IIc: R).
    # Dò theo TÊN tiêu đề (dòng tiêu đề + dòng kế tiếp vì IIb/IIc gộp 2 dòng), không theo chỉ số cố định.
    # File kỳ cũ không có cột -> task_id = None -> giữ đường đối chiếu gần đúng như trước.
    col_task_id = None
    for hr in rows[header_idx:header_idx + 2]:
        for j, v in enumerate(hr or ()):
            if v is not None and _norm(v).replace("_", "").replace(" ", "") in ("taskid", "mataskid"):
                col_task_id = j
    task_ids_da_gap = {}
    if kind_note:
        canh_bao.append("[NHẬN DIỆN] " + kind_note)
    if kind is None:
        canh_bao.append("[DỪNG] Không xác định được KH/KQ — các bước tính KPI và lọc "
                        "Ghi chú sẽ KHÔNG chạy. Không dùng kết quả này để tổng hợp.")

    result_truc = {n: [] for n in range(1, 7)}
    result_tong = {}
    muc_ii_items = []   # [GHÉP v3.1] Nhiệm vụ Mục II — KHÔNG gán Trục tự động
    in_muc_ii = False
    current_truc = None
    n_task = 0
    n_sum_row = 0
    n_formula_none = 0

    for row in rows[header_idx + 1:]:
        if not row or all(c is None for c in row):
            continue
        col0 = str(row[0]).strip() if row[0] is not None else ""
        col1 = str(row[1]).strip() if row[1] is not None else ""

        # [VÁ BUG-02] Nhãn Trục có thể nằm ở cột 0 HOẶC cột 1
        m = TRUC_HEADER_RE.match(col1) or TRUC_HEADER_RE.match(col0)
        if m:
            truc_no = int(m.group(1))
            in_muc_ii = False   # [GHÉP v3.1] gặp Trục mới -> chắc chắn không còn ở Mục II
            if 1 <= truc_no <= 6:          # [VÁ BUG-09] chặn KeyError
                current_truc = truc_no
            else:
                canh_bao.append(f"Số Trục ngoài phạm vi 1-6: {truc_no!r} — bỏ qua.")
                current_truc = None
            continue

        # [VÁ BUG-03][VÁ BUG-04] Dòng Tổng -> lưu riêng, KHÔNG tính là nhiệm vụ
        if _is_sum_row(col0, col1):
            n_sum_row += 1
            if current_truc and kind == "KQ" and len(row) >= 16:
                result_tong[current_truc] = {
                    "so_luong": _num(row[5]), "so_luong_quy_doi": _num(row[9]),
                    "kpi_so_luong_tt": _num(row[10]), "kpi_so_luong_qd": _num(row[11]),
                    "kpi_chat_luong_tt": _num(row[12]), "kpi_chat_luong_qd": _num(row[13]),
                    "kpi_tien_do_tt": _num(row[14]), "kpi_tien_do_qd": _num(row[15]),
                }
            continue

        # Dòng tiêu đề Mục I/II (VD "I | NHIỆM VỤ THEO KẾ HOẠCH")
        if col0.upper() in ("I", "II") and ("NHIỆM VỤ" in col1.upper() or not col1):
            # [GHÉP v3.1] Mục II — ý nghĩa khác nhau theo loại Phụ lục (xác nhận file thật):
            #   KH (Ia/Ib): "phát sinh ngoài KH + từ kỳ trước chuyển sang"
            #   KQ (IIb/IIc): "CHƯA HOÀN THÀNH, đang triển khai (chuyển sang tháng sau)"
            # Trong file KQ thật, Mục II liệt kê tuần tự KHÔNG kèm Trục con -> KHÔNG được
            # gán bừa vào current_truc (Trục cuối cùng còn hiệu lực của Mục I).
            if col0.upper() == "II":
                in_muc_ii = True
                current_truc = None
            continue

        if not col1:                        # không có nội dung công việc -> bỏ
            continue

        task = {"noi_dung": row[1], "nguoi_chi_dao": row[2] if len(row) > 2 else None,
                "don_vi": row[3] if len(row) > 3 else None,
                "san_pham": row[4] if len(row) > 4 else None,
                "so_luong": row[5] if len(row) > 5 else None,
                "do_kho": row[6] if len(row) > 6 else None}
        task["task_id"] = _doc_task_id(row, col_task_id, task, canh_bao, task_ids_da_gap)

        # [GHÉP v3.1] Nhiệm vụ Mục II -> thu riêng, KHÔNG ép vào Trục nào
        if in_muc_ii:
            if kind == "KH" and len(row) > 7:
                task.update({"thoi_gian_ht": row[7] if len(row) > 7 else None,
                             "diem": row[8] if len(row) > 8 else None,
                             "he_so": row[9] if len(row) > 9 else None,
                             "ghi_chu": row[10] if len(row) > 10 else None})
            elif kind == "KQ" and len(row) >= 16:
                task.update({"diem": row[7], "he_so": row[8], "so_luong_quy_doi": row[9]})
            muc_ii_items.append(task)
            continue

        if current_truc is None:
            continue

        if kind == "KH":
            task.update({"thoi_gian_ht": row[7] if len(row) > 7 else None,
                         "diem": row[8] if len(row) > 8 else None,
                         "he_so": row[9] if len(row) > 9 else None,
                         "ghi_chu": row[10] if len(row) > 10 else None})
            gc = _norm(task["ghi_chu"])
            # [VÁ BUG-07] "Bổ sung ngoài KH quý"/"Kết luận giao ban" là HỢP LỆ
            if gc and gc not in GHI_CHU_HOP_LE:
                canh_bao.append(
                    f"[GHI CHÚ KHÔNG CHUẨN] '{str(task['noi_dung'])[:45]}': "
                    f"{task['ghi_chu']!r} — không thuộc 4 giá trị hợp lệ.")
            elif not gc:
                canh_bao.append(
                    f"[THIẾU GHI CHÚ] '{str(task['noi_dung'])[:45]}': cột Ghi chú để trống "
                    f"— không xác định được có đưa lên cấp Trường hay không.")
            d, h = _num(task["diem"]), _num(task["he_so"])
            if d is not None and h is not None and not _close(h, d * 0.01):
                canh_bao.append(
                    f"[SAI CÔNG THỨC] '{str(task['noi_dung'])[:45]}': Hệ số={h} "
                    f"nhưng Điểm×1%={round(d * 0.01, 4)}")

        elif kind == "KQ":
            task.update({
                "diem": row[7] if len(row) > 7 else None,
                "he_so": row[8] if len(row) > 8 else None,
                "so_luong_quy_doi": row[9] if len(row) > 9 else None,
                "kpi_so_luong_tt": row[10] if len(row) > 10 else None,
                "kpi_so_luong_qd": row[11] if len(row) > 11 else None,
                "kpi_chat_luong_tt": row[12] if len(row) > 12 else None,
                "kpi_chat_luong_qd": row[13] if len(row) > 13 else None,
                "kpi_tien_do_tt": row[14] if len(row) > 14 else None,
                "kpi_tien_do_qd": row[15] if len(row) > 15 else None,
            })
            if len(row) < 16:
                canh_bao.append(
                    f"[THIẾU CỘT] '{str(task['noi_dung'])[:45]}': chỉ có {len(row)} cột "
                    f"(mẫu IIb/IIc cần 16 cột) — không kiểm được KPI.")
            else:
                if all(task[k] is None for k in
                       ("so_luong_quy_doi", "kpi_so_luong_qd", "kpi_chat_luong_qd")):
                    n_formula_none += 1
                # [VÁ BUG-06] Kiểm TOÀN BỘ chuỗi cascade, không chỉ hệ số
                nl, d, h = _num(task["so_luong"]), _num(task["diem"]), _num(task["he_so"])
                sl_qd = _num(task["so_luong_quy_doi"])
                k11, k12 = _num(task["kpi_so_luong_tt"]), _num(task["kpi_so_luong_qd"])
                k13, k14 = _num(task["kpi_chat_luong_tt"]), _num(task["kpi_chat_luong_qd"])
                k15, k16 = _num(task["kpi_tien_do_tt"]), _num(task["kpi_tien_do_qd"])
                nd = str(task["noi_dung"])[:45]
                if d is not None and h is not None and not _close(h, d * 0.01):
                    canh_bao.append(f"[SAI CT (9)] '{nd}': Hệ số={h}, đúng phải = Điểm×1% = {round(d*0.01,4)}")
                if nl is not None and h is not None and sl_qd is not None and not _close(sl_qd, nl * h):
                    canh_bao.append(f"[SAI CT (10)] '{nd}': SL quy đổi={sl_qd}, đúng phải = SL×Hệ số = {round(nl*h,4)}")
                if h is not None and k11 is not None and k12 is not None and not _close(k12, h * k11):
                    canh_bao.append(f"[SAI CT (12)] '{nd}': KPI SL-QĐ={k12}, đúng phải = Hệ số×(11) = {round(h*k11,4)}")
                if h is not None and k13 is not None and k14 is not None and not _close(k14, h * k13):
                    canh_bao.append(f"[SAI CT (14)] '{nd}': KPI CL-QĐ={k14}, đúng phải = Hệ số×(13) = {round(h*k13,4)}")
                if h is not None and k15 is not None and k16 is not None and not _close(k16, h * k15):
                    canh_bao.append(f"[SAI CT (16)] '{nd}': KPI TĐ-QĐ={k16}, đúng phải = Hệ số×(15) = {round(h*k15,4)}")
                if k11 is not None and nl is not None and k11 > nl + 0.011:
                    canh_bao.append(f"[BẤT THƯỜNG] '{nd}': KPI SL thực tế={k11} > Số lượng kế hoạch={nl}")

        result_truc[current_truc].append(task)
        n_task += 1

    # [VÁ BUG-05] Cảnh báo file rỗng dữ liệu — tránh "im lặng trả về 0 dòng"
    if n_task == 0:
        canh_bao.append("[DỪNG] Đọc được 0 nhiệm vụ. Nguyên nhân thường gặp: nhãn Trục "
                        "không đúng dạng 'Trục <số>', hoặc dữ liệu nằm ở sheet khác. "
                        "Kiểm tra lại trước khi tổng hợp.")
    if n_formula_none and n_formula_none == n_task:
        canh_bao.append("[CÔNG THỨC CHƯA TÍNH] Toàn bộ ô KPI trả về rỗng — file có thể chứa "
                        "công thức chưa được Excel tính sẵn. Mở file bằng Excel/LibreOffice, "
                        "lưu lại rồi đọc lại.")

    # Đối chiếu dòng Tổng của đơn vị với tổng tính lại (không tự sửa)
    if kind == "KQ":
        for truc, tong in result_tong.items():
            calc = sum(_num(t.get("so_luong_quy_doi")) or 0 for t in result_truc[truc])
            declared = tong.get("so_luong_quy_doi")
            if declared is not None and not _close(declared, calc, tol=0.05):
                canh_bao.append(
                    f"[LỆCH DÒNG TỔNG] Trục {truc}: dòng Tổng ghi SL quy đổi={declared} "
                    f"nhưng cộng các dòng chi tiết={round(calc,3)}. Đơn vị cần rà lại.")

    return {"kind": kind, "truc": result_truc, "truc_tong": result_tong,
            "muc_ii_items": muc_ii_items,
            "canh_bao": canh_bao,
            "thong_ke": {"so_nhiem_vu": n_task, "so_dong_tong": n_sum_row,
                         "so_muc_ii": len(muc_ii_items),
                         "dong_tieu_de": header_idx + 1}}


def filter_truong_level(appendix_kh):
    """Chỉ giữ nhiệm vụ có Ghi chú = 'Đưa vào KH Trường' (Phụ lục Ia/Ib).
    [VÁ BUG-08] So khớp sau khi chuẩn hoá khoảng trắng/hoa-thường."""
    if appendix_kh.get("kind") != "KH":
        raise ValueError("filter_truong_level chỉ áp dụng cho Phụ lục kế hoạch (Ia/Ib). "
                         f"Nhận được kind={appendix_kh.get('kind')!r}.")
    out = {n: [] for n in range(1, 7)}
    for truc, tasks in appendix_kh["truc"].items():
        out[truc] = [t for t in tasks if _norm(t.get("ghi_chu")) == GHI_CHU_LOC_LEN_TRUONG]
    return out


def summarize_truc_kpi(appendix_kq):
    """Tổng hợp % KPI 3 chiều theo Trục, cộng dồn nhiều đơn vị.
    Nhận 1 appendix hoặc list nhiều appendix."""
    if not isinstance(appendix_kq, list):
        appendix_kq = [appendix_kq]

    agg = {n: {"so_luong": 0.0, "so_luong_quy_doi": 0.0,
               "kpi_sl_tt": 0.0, "kpi_sl_qd": 0.0,
               "kpi_cl_tt": 0.0, "kpi_cl_qd": 0.0,
               "kpi_td_tt": 0.0, "kpi_td_qd": 0.0, "so_nhiem_vu": 0} for n in range(1, 7)}

    bo_qua = []
    for i, ap in enumerate(appendix_kq):
        if ap.get("kind") != "KQ":
            bo_qua.append(i)
            continue
        for truc, tasks in ap["truc"].items():
            for t in tasks:
                agg[truc]["so_nhiem_vu"] += 1
                for src, dst in [
                    ("so_luong", "so_luong"), ("so_luong_quy_doi", "so_luong_quy_doi"),
                    ("kpi_so_luong_tt", "kpi_sl_tt"), ("kpi_so_luong_qd", "kpi_sl_qd"),
                    ("kpi_chat_luong_tt", "kpi_cl_tt"), ("kpi_chat_luong_qd", "kpi_cl_qd"),
                    ("kpi_tien_do_tt", "kpi_td_tt"), ("kpi_tien_do_qd", "kpi_td_qd"),
                ]:
                    v = _num(t.get(src))
                    if v is not None:
                        agg[truc][dst] += v

    for truc, d in agg.items():
        base = d["so_luong_quy_doi"] or 0
        d["pct_so_luong"] = round(100 * d["kpi_sl_qd"] / base, 1) if base else None
        d["pct_chat_luong"] = round(100 * d["kpi_cl_qd"] / base, 1) if base else None
        d["pct_tien_do"] = round(100 * d["kpi_td_qd"] / base, 1) if base else None

    if bo_qua:
        agg["_canh_bao"] = [f"Đã bỏ qua {len(bo_qua)} file không phải Phụ lục kết quả "
                            f"(vị trí {bo_qua}) — kiểm tra lại đầu vào."]
    return agg


def group_by_don_vi(tasks_in_truc):
    """Gom nhiệm vụ trong 1 Trục theo Đơn vị chủ trì."""
    grouped = {}
    for t in tasks_in_truc:
        dv = t.get("don_vi") or "[CHƯA RÕ ĐƠN VỊ]"
        grouped.setdefault(str(dv).strip(), []).append(t)
    return grouped


def build_content_map_skeleton(appendix_kq, top_n_examples=3, phase="PHAN_I"):
    """
    Dựng khung nháp theo (Trục, Đơn vị) từ Phụ lục kết quả.

    [SỬA v3.4 — XUNG ĐỘT 1] Trả về ĐÚNG cấu trúc 3 tầng mà fill_report() yêu cầu
    ({"PHAN_I": {...}, "PHAN_II": {}, "PHAN_III": {}}), thay vì dict phẳng như bản cũ.
    Bản cũ trả dict phẳng khiến truyền thẳng vào fill_report() crash với
    "AttributeError: 'str' object has no attribute 'items'" — trong khi Skill 33 lại
    hướng dẫn dùng chuỗi skeleton -> fill_report. Nay đã tương thích trực tiếp.

    ⚠️ VẪN LÀ BẢN NHÁP — khóa dạng "__DRAFT__ TrụcN__ĐơnVị" KHÔNG khớp với nhãn thật
    trong mẫu TB736 (VD "Công tác tuyển sinh"), nên nếu đưa thẳng vào fill_report()
    sẽ KHÔNG điền được gì và mọi vị trí bị đánh [CẦN BỔ SUNG]. Người tổng hợp BẮT BUỘC:
      (1) đọc từng mục nháp, gán vào đúng nhãn thật (xem 45 nhãn ở README-fill_bc736.md);
      (2) chuyển văn phong sang chủ thể "Nhà trường" (Skill-Tu-hoc Mục 0);
      (3) tách riêng nội dung KẾT QUẢ (PHAN_I) và KẾ HOẠCH (PHAN_III) — không dùng chung.

    phase: đặt khung nháp vào Phần nào (mặc định PHAN_I vì Phụ lục KQ là dữ liệu kết quả).
    """
    drafts = {}
    for truc, tasks in appendix_kq["truc"].items():
        for dv, dv_tasks in group_by_don_vi(tasks).items():
            if not dv_tasks:
                continue
            examples = [t.get("san_pham") or t.get("noi_dung") for t in dv_tasks[:top_n_examples]]
            examples_txt = "; ".join(str(e) for e in examples if e)
            drafts[f"__DRAFT__ Trục{truc}__{dv}"] = (
                f"[NHÁP - Trục {truc} ({TRUC_NAMES[truc]}) - {dv}] "
                f"Hoàn thành {len(dv_tasks)} nhiệm vụ trong kỳ, tiêu biểu: {examples_txt}. "
                f"[CẦN: điền % KPI tổng hợp + biên tập văn phong cấp Trường trước khi dùng]")

    # [SỬA v3.4] Nhiệm vụ Mục II (chưa hoàn thành) — trước đây bị BỎ QUÊN hoàn toàn
    # (read_appendix tách ra nhưng không hàm nào tiêu thụ). Nay đưa vào khung nháp
    # như 1 mục riêng để người tổng hợp không bỏ sót khi viết báo cáo.
    muc_ii = appendix_kq.get("muc_ii_items") or []
    if muc_ii:
        ten_viec = "; ".join(str(t.get("noi_dung"))[:60] for t in muc_ii[:top_n_examples])
        drafts["__DRAFT__ MucII__ChuaHoanThanh"] = (
            f"[NHÁP - MỤC II: {len(muc_ii)} nhiệm vụ CHƯA HOÀN THÀNH, chuyển sang kỳ sau] "
            f"Gồm: {ten_viec}. "
            f"[CẦN: đưa vào phần 'Tồn tại, hạn chế' (PHAN_II) hoặc 'Nhiệm vụ trọng tâm "
            f"kỳ tới' (PHAN_III) tuỳ ngữ cảnh — KHÔNG báo cáo là đã hoàn thành]")

    out = {"PHAN_I": {}, "PHAN_II": {}, "PHAN_III": {}}
    out[phase] = drafts
    return out


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Dùng: python read_bc736_excel.py <đường_dẫn_file.xlsx> [tên_sheet]")
        sys.exit(1)
    data = read_appendix(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print(f"Loại Phụ lục: {data['kind']}   |   Thống kê: {data['thong_ke']}")
    for truc, tasks in data["truc"].items():
        if tasks:
            print(f"  Trục {truc}: {len(tasks)} nhiệm vụ")
    if data["truc_tong"]:
        print("  Dòng Tổng đọc được ở Trục:", sorted(data["truc_tong"].keys()))
    if data["canh_bao"]:
        print("Cảnh báo (%d):" % len(data["canh_bao"]))
        for w in data["canh_bao"]:
            print("  -", w)
