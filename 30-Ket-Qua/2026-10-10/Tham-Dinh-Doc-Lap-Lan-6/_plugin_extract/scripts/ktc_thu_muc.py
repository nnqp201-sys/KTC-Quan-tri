# -*- coding: utf-8 -*-
"""Ket noi THU MUC LAM VIEC cua don vi (Cowork/Claude Code ngoai du an) — dau vao `10-Dau-Vao/`, ket qua `30-Ket-Qua/`.

Tai khoan thanh vien (phong, khoa) khong co thu muc du an KTC-Quan-tri. Tren Cowork, nguoi dung chon mot thu muc tren
may (hoac thu muc Google Drive dong bo) de cap quyen cho Claude; lenh `khoi-tao` tao trong do:
    KTC-THU-MUC-LAM-VIEC.json   tep danh dau (ma don vi, ngay tao) — skill, hook nhan ra thu muc nho tep nay
    10-Dau-Vao/                 tep can xu ly (bao cao, ke hoach cua don vi, van ban lien quan)
    30-Ket-Qua/<ngay>/<loai>/   san pham Bo cong cu xuat ra
    00-HUONG-DAN.md             cach dung, cach gui ve Phong TH-HC&QT
Khong ghi de tep da co; khong tao trong kho chuan (KTC-Database, 03-Templates, 04-Good-Documents) hay trong du an.

    python ktc_thu_muc.py khoi-tao <thu-muc> --ma P-TCCB
    python ktc_thu_muc.py kiem [<thu-muc>]        # in che do: du-an | don-vi | khong (tim tu thu muc len 6 cap)
"""
import argparse
import datetime as dt
import io
import json
import os
import re
import sys

DANH_DAU = "KTC-THU-MUC-LAM-VIEC.json"
MA_DON_VI = ("P-TCCB", "P-QLDT", "P-THHC", "P-QLKH", "P-TCKT", "K-KHCB", "K-SUPH", "K-KTNL", "K-KTCN", "K-YDUOC",
             "K-DTSHLX")
VUNG = re.compile(r"(?:^|[\\/])(?:KTC-Database|03-Templates\(1\)|04-Good-Documents)(?:[\\/]|$)", re.I)

HUONG_DAN = """# Thư mục làm việc KTC-Quan-tri — {ma}

Thư mục này được kết nối với Bộ công cụ KTC-Quan-tri (khởi tạo {ngay}). Tệp `{danh_dau}` là dấu nhận biết — không xóa.

| Thư mục | Dùng để |
|---|---|
| `10-Dau-Vao/` | Đặt tệp cần xử lý: kế hoạch, báo cáo của đơn vị, văn bản liên quan. Nên chia theo kỳ, ví dụ `10-Dau-Vao/2026-10/` |
| `30-Ket-Qua/<ngày>/<loại>/` | Bộ công cụ lưu sản phẩm, tên tệp chuẩn `<mã đơn vị>_<loại>_<kỳ>_v<N>` |

Cách dùng trên Claude Cowork: mở phiên, chọn thư mục này làm thư mục làm việc, rồi yêu cầu như bình thường (ví dụ
"lập báo cáo tháng 10 từ tệp trong 10-Dau-Vao/2026-10"). Bộ công cụ đọc `10-Dau-Vao/`, lưu kết quả vào `30-Ket-Qua/`.

Lưu ý:
- Bộ công cụ **không tự gửi** sản phẩm. Kiểm tra phiếu tự kiểm cuối câu trả lời; không còn lỗi thì **người dùng tự gửi**
  tệp về Phòng TH-HC&QT (`P-THHC`) theo kênh Trường quy định.
- Không đặt vào đây dữ liệu Thông báo số 924/TB-CĐKT không cho phép đưa lên nền tảng trí tuệ nhân tạo.
- Sửa văn bản đã có: Bộ công cụ tạo bản mới có Track Changes, không ghi đè tệp gốc trong `10-Dau-Vao/`.
"""


def tim_goc(thu_muc=None, cap=6):
    """(che_do, goc, ma_don_vi): 'du-an' (co 90-Nhat-Ky-Van-Hanh/), 'don-vi' (co tep danh dau) hoac ('khong', None, None)."""
    p = os.path.abspath(thu_muc or os.getcwd())
    for _ in range(cap):
        if os.path.isdir(os.path.join(p, "90-Nhat-Ky-Van-Hanh")):
            return "du-an", p, None
        f = os.path.join(p, DANH_DAU)
        if os.path.isfile(f):
            try:
                ma = json.load(io.open(f, encoding="utf-8")).get("ma_don_vi")
            except Exception:
                ma = None
            return "don-vi", p, ma
        cha = os.path.dirname(p)
        if cha == p:
            break
        p = cha
    return "khong", None, None


def khoi_tao(thu_muc, ma):
    ma = (ma or "").strip().upper()
    if ma not in MA_DON_VI:
        raise ValueError(f"Mã đơn vị '{ma}' không có trong bảng 11 mã chuẩn: {', '.join(MA_DON_VI)} — hỏi người dùng.")
    goc = os.path.abspath(thu_muc)
    if VUNG.search(goc.replace("\\", "/")):
        raise ValueError("Không khởi tạo trong kho chuẩn (KTC-Database, 03-Templates(1), 04-Good-Documents) — chọn thư mục khác.")
    if not os.path.isdir(goc):
        raise ValueError(f"Không thấy thư mục {goc} — chọn thư mục đã cấp quyền cho Claude.")
    che_do, g, ma_cu = tim_goc(goc)
    if che_do == "du-an":
        raise ValueError(f"{goc} nằm trong dự án KTC-Quan-tri ({g}) — dự án đã có 10-Dau-Vao/, 30-Ket-Qua/, không cần khởi tạo.")
    if che_do == "don-vi" and os.path.normcase(g) != os.path.normcase(goc):
        raise ValueError(f"{goc} nằm trong thư mục làm việc đã kết nối {g} (đơn vị {ma_cu}) — dùng thư mục đó.")
    tao = []
    for d in ("10-Dau-Vao", "30-Ket-Qua"):
        p = os.path.join(goc, d)
        if not os.path.isdir(p):
            os.makedirs(p)
            tao.append(d + "/")
    ngay = dt.date.today().strftime("%d/%m/%Y")
    f = os.path.join(goc, DANH_DAU)
    if os.path.isfile(f):
        if ma_cu and ma_cu != ma:
            raise ValueError(f"Thư mục đã kết nối cho đơn vị {ma_cu}, khác {ma} — không ghi đè; hỏi người dùng.")
    else:
        io.open(f, "w", encoding="utf-8").write(json.dumps(
            {"ma_don_vi": ma, "tao_ngay": dt.date.today().isoformat(), "ban_mau": 1,
             "dau_vao": "10-Dau-Vao", "ket_qua": "30-Ket-Qua"}, ensure_ascii=False, indent=2) + "\n")
        tao.append(DANH_DAU)
    hd = os.path.join(goc, "00-HUONG-DAN.md")
    if not os.path.isfile(hd):
        io.open(hd, "w", encoding="utf-8").write(HUONG_DAN.format(ma=ma, ngay=ngay, danh_dau=DANH_DAU))
        tao.append("00-HUONG-DAN.md")
    return goc, tao


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="lenh", required=True)
    a1 = sub.add_parser("khoi-tao")
    a1.add_argument("thu_muc")
    a1.add_argument("--ma", required=True)
    a2 = sub.add_parser("kiem")
    a2.add_argument("thu_muc", nargs="?")
    a = ap.parse_args(argv)
    if a.lenh == "khoi-tao":
        try:
            goc, tao = khoi_tao(a.thu_muc, a.ma)
        except ValueError as e:
            print("✗ " + str(e))
            return 2
        print(f"✓ Đã kết nối thư mục làm việc: {goc}")
        print("  tạo mới: " + (", ".join(tao) if tao else "không (đã có đủ)"))
        print("  đầu vào: 10-Dau-Vao/ · kết quả: 30-Ket-Qua/<ngày>/<loại>/ · hướng dẫn: 00-HUONG-DAN.md")
        return 0
    che_do, goc, ma = tim_goc(a.thu_muc)
    print(json.dumps({"che_do": che_do, "goc": goc, "ma_don_vi": ma,
                      "dau_vao": os.path.join(goc, "10-Dau-Vao") if goc else None,
                      "ket_qua": os.path.join(goc, "30-Ket-Qua") if goc else None}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
