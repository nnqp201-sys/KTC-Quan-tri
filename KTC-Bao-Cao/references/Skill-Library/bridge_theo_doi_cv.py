# -*- coding: utf-8 -*-
"""
bridge_theo_doi_cv.py — Cầu nối thử nghiệm KTC-Theo-dõi-CV <-> KTC-Bao-Cao
Mục đích: kiểm chứng xem 2 khóa liên kết đã có sẵn (Mã nhiệm vụ, Trục TB817)
có thực sự đủ để đối chiếu dữ liệu giữa 2 hệ hay không — TRƯỚC KHI bàn hợp nhất.

Nguồn cấu trúc: "01. Bộ dữ liệu vận hành KTC-Theo-dõi-CV" (Google Sheet, đọc 19/08/2026).
Dữ liệu thật trong sheet hiện đang RỖNG (Trạng thái: Thiết kế) — script dưới đây
dùng dữ liệu MẪU (đánh dấu rõ) để kiểm thử logic, không phải dữ liệu vận hành thật.

KHÔNG tự suy diễn dữ liệu thiếu — mọi phát hiện về khả năng tương thích đều
dựa trên đối chiếu SCHEMA (cấu trúc cột) thật, không phải đoán.
"""

# ===== Cấu trúc cột THẬT của bảng "Nhiệm vụ" trong KTC-Theo-dõi-CV =====
NHIEM_VU_COLUMNS = [
    "Mã nhiệm vụ", "Mã KH nguồn", "Kỳ kế hoạch", "Trục TB 817", "Nhóm nhiệm vụ",
    "Tên nhiệm vụ", "Đơn vị chủ trì", "Đơn vị phối hợp", "Sản phẩm/kết quả",
    "Hạn baseline", "Hạn hiện hành", "Trạng thái", "% hoàn thành", "Mức rủi ro",
    "Người cập nhật", "Ngày cập nhật", "Liên kết minh chứng", "Ghi chú", "Khóa baseline",
]

TRUC_MAP = {
    "Trục 1": 1, "Trục 2": 2, "Trục 3": 3, "Trục 4": 4, "Trục 5": 5, "Trục 6": 6,
}


def parse_trục(trục_text):
    """Chuyển 'Trục 1' (định dạng Theo-dõi-CV) -> số 1 (định dạng KTC-Bao-Cao)."""
    return TRUC_MAP.get(trục_text.strip(), None)


def summarize_tien_do_theo_truc(nhiem_vu_list):
    """
    Tổng hợp tiến độ theo Trục từ danh sách nhiệm vụ Theo-dõi-CV.
    Trả về: { so_truc: {"tong_nv": n, "hoan_thanh": n, "dang_thuc_hien": n,
                          "cham_tien_do": n, "trung_binh_%": x, "rui_ro_cao": n} }
    """
    agg = {n: {"tong_nv": 0, "hoan_thanh": 0, "dang_thuc_hien": 0,
               "cham_tien_do": 0, "rui_ro_cao": 0, "tong_pct": 0} for n in range(1, 7)}

    canh_bao = []
    for nv in nhiem_vu_list:
        truc_so = parse_trục(nv.get("Trục TB 817", ""))
        if truc_so is None:
            canh_bao.append(f"[CẢNH BÁO] Nhiệm vụ '{nv.get('Mã nhiệm vụ')}' có Trục không hợp lệ: "
                             f"{nv.get('Trục TB 817')!r}")
            continue

        agg[truc_so]["tong_nv"] += 1
        agg[truc_so]["tong_pct"] += nv.get("% hoàn thành", 0) or 0

        trang_thai = nv.get("Trạng thái", "")
        if trang_thai == "Hoàn thành":
            agg[truc_so]["hoan_thanh"] += 1
        elif trang_thai == "Đang thực hiện":
            agg[truc_so]["dang_thuc_hien"] += 1
        elif trang_thai == "Chậm tiến độ":
            agg[truc_so]["cham_tien_do"] += 1

        if nv.get("Mức rủi ro") == "Cao":
            agg[truc_so]["rui_ro_cao"] += 1

    for truc_so, d in agg.items():
        d["trung_binh_%"] = round(d["tong_pct"] / d["tong_nv"], 1) if d["tong_nv"] else None
        del d["tong_pct"]

    return agg, canh_bao


def cross_check_don_vi_naming(theo_doi_don_vi_set, bao_cao_don_vi_set):
    """
    Kiểm tra tên đơn vị chủ trì có VIẾT GIỐNG NHAU giữa 2 hệ không —
    đây là điều kiện cần để đối chiếu chéo mà không cần bảng ánh xạ riêng.
    """
    khop_hoan_toan = theo_doi_don_vi_set & bao_cao_don_vi_set
    chi_co_theo_doi = theo_doi_don_vi_set - bao_cao_don_vi_set
    chi_co_bao_cao = bao_cao_don_vi_set - theo_doi_don_vi_set
    return {
        "khop_hoan_toan": khop_hoan_toan,
        "chi_co_o_theo_doi_cv": chi_co_theo_doi,
        "chi_co_o_bao_cao": chi_co_bao_cao,
        "ty_le_khop": round(100 * len(khop_hoan_toan) / len(theo_doi_don_vi_set), 1) if theo_doi_don_vi_set else 0,
    }


def check_ma_nhiem_vu_bridge(nhiem_vu_list, bc736_da_co_cot_ma_nhiem_vu=False):
    """
    Kiểm tra điều kiện TIÊN QUYẾT để đối chiếu CHÍNH XÁC theo Mã nhiệm vụ:
    Phụ lục TB736 (Ia/Ib/IIb/IIc) của KTC-Bao-Cao hiện KHÔNG có cột 'Mã nhiệm vụ'.
    => Chỉ có thể đối chiếu GẦN ĐÚNG (theo Trục + tên nhiệm vụ), KHÔNG THỂ đối chiếu
       CHÍNH XÁC 1-1 cho đến khi 1 trong 2 hệ bổ sung cột này.
    """
    if bc736_da_co_cot_ma_nhiem_vu:
        return {"co_the_doi_chieu_chinh_xac": True, "ghi_chu": "Đã có Mã nhiệm vụ ở cả 2 hệ."}
    return {
        "co_the_doi_chieu_chinh_xac": False,
        "ghi_chu": ("Phụ lục TB736 (Ia/Ib/IIb/IIc) của KTC-Bao-Cao KHÔNG có cột 'Mã nhiệm vụ'. "
                    "Đối chiếu hiện tại chỉ làm được ở mức GẦN ĐÚNG (Trục + so khớp tên nhiệm vụ), "
                    "không đối chiếu được CHÍNH XÁC 1-1 cho đến khi bổ sung cột này vào 1 trong 2 hệ."),
    }
