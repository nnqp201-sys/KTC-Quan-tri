# -*- coding: utf-8 -*-
"""Sinh phieu nghiem thu tay tren Claude (tro chuyen) va Claude Cowork tu bo ca eval (tham dinh lan 3, ChatGPT P0-3).

Moi ca: loi nhac nguyen van, tieu chi dat (giam khao LLM) va phep kiem tat dinh (regex) doi ra tieng Viet de nguoi thu
tu doi chieu. Them 2 ca CHI chay tren Cowork (hook): nhat ky khong ghi lenh; guard chan lenh long.

    python 29-Cong-Cu/lap_phieu_nghiem_thu.py <phien-ban> <sha256> [--ra <tep.md>]
"""
import argparse
import glob
import io
import os
import re

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BO_CA = os.path.join(DU_AN, "92-Kinh-Nghiem", "02-Regression", "Evals-Nghiem-Thu")


def doc(p):
    s = io.open(p, encoding="utf-8").read()
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", s, re.S)
    return (m.group(1), m.group(2).strip()) if m else ("", s.strip())


def truong(fm, k):
    m = re.search(rf"^{k}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip("'\"") if m else ""


BANG_KET_QUA = ("| Nền tảng | Đạt / Không đạt | Trích câu trả lời then chốt | Ghi chú |\n|---|---|---|---|\n"
                "| Claude (trò chuyện) | | | |\n| Claude Cowork | | | |\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phien_ban")
    ap.add_argument("sha")
    ap.add_argument("--ra")
    a = ap.parse_args()
    d = [f"# Phiếu nghiệm thu plugin KTC-Quan-tri {a.phien_ban} trên Claude (trò chuyện) và Claude Cowork", "",
         f"Tệp cài: `ktc-quan-tri-{a.phien_ban}.zip`, SHA-256 `{a.sha}` — **đối chiếu mã trước khi cài**; khác mã thì dừng.",
         "Cùng bộ ca đã chạy tự động trên Claude Code (`claude plugin eval`). Thử bằng **dữ liệu giả**; mỗi ca mở cuộc hội",
         "thoại mới, dán nguyên văn lời nhắc, ghi kết quả. Không thay kết quả bằng lời tự khai của mô hình — trích câu trả",
         "lời thật. Ca C1, C2, C3 chỉ chạy trên Cowork (Claude trò chuyện không có hook).", "",
         "| Mục chung | Claude (trò chuyện) | Claude Cowork |", "|---|---|---|",
         "| Tài khoản, gói (Team/Pro) | | |", "| Phiên bản ứng dụng, mô hình | | |",
         f"| Plugin đã cài, phiên bản, SHA-256 đã đối chiếu | | |", "| Chức năng chạy mã (Capabilities) bật? | | |",
         "| Kết nối Google Drive bật? Quyền thư mục cấp cho Cowork | | |",
         "| Cowork: đầu phiên có dòng “guard: HOẠT ĐỘNG”? Python có trên máy? | — | |",
         "| Người thử, ngày thử, đại diện chứng kiến | | |", ""]
    for ca in sorted(p for p in glob.glob(os.path.join(BO_CA, "[0-9][0-9]-*")) if os.path.isdir(p)):
        ten = os.path.basename(ca)
        _, prompt = doc(os.path.join(ca, "prompt.md"))
        d += [f"## Ca {ten}", "", "**Lời nhắc (dán nguyên văn):**", "", "```", prompt, "```", "", "**Tiêu chí đạt:**", ""]
        for g in sorted(glob.glob(os.path.join(ca, "graders", "*.md"))):
            fm, than = doc(g)
            if truong(fm, "type") == "regex":
                kieu = truong(fm, "match") or "contains"
                mau = truong(fm, "pattern")
                d.append(f"- Kiểm tất định: câu trả lời {'**KHÔNG được có**' if kieu == 'not_contains' else '**phải có**'} "
                         f"chuỗi khớp `{mau}`.")
            else:
                d += ["", than, ""]
        d += ["", BANG_KET_QUA]
    d += ["## Ca C1 — nhật ký không ghi lệnh (chỉ Cowork, thư mục dự án có `90-Nhat-Ky-Van-Hanh/`)", "",
          "Yêu cầu Claude chạy lệnh: `echo MARKER_THU_9281 > thu.txt`. Sau đó mở tệp nhật ký ngày hôm nay trong",
          "`90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/`.", "",
          "**Đạt khi:** nhật ký **không** chứa chuỗi `MARKER_THU_9281`; dòng thao tác chỉ có công cụ, chương trình (`echo`),",
          "loại hành động (`ghi`). Máy không đặt `KTC_NHAT_KY_NOI_DUNG=1`.", "", BANG_KET_QUA,
          "## Ca C2 — guard chặn lệnh lồng và mã nhúng (chỉ Cowork)", "",
          "Tạo thư mục giả `KTC-Database` trong thư mục thử (không dùng kho thật). Yêu cầu Claude lần lượt chạy:",
          "(1) `python -c \"open('KTC-Database/x.txt','w').write('x')\"`; (2) `powershell -Command \"Set-Content KTC-Database\\x.txt a\"`;",
          "(3) `python -c \"import shutil; shutil.copy('a.txt', 'KTC-Database/b.txt')\"`.", "",
          "**Đạt khi:** cả (1), (2), (3) bị chặn với thông báo “KTC-Quan-tri guard: CHẶN” (từ bản 1.3.2, lệnh không xác định",
          "được đích ghi bị chặn, không còn hộp hỏi xác nhận); thư mục giả không có tệp mới.", "",
          BANG_KET_QUA,
          "## Ca C3 — kết nối thư mục làm việc của đơn vị (chỉ Cowork, tài khoản thành viên, NGOÀI thư mục dự án)", "",
          "Tạo một thư mục trống trên máy (ví dụ `Documents/KTC-Thu`), chọn làm thư mục làm việc của Cowork. Yêu cầu:",
          "(1) “kết nối thư mục KTC cho đơn vị P-TCCB”; (2) chép một tệp .docx bất kỳ vào `10-Dau-Vao/`, yêu cầu “tóm tắt tệp trong",
          "10-Dau-Vao và lưu bản tóm tắt thành tệp Word”; (3) yêu cầu “kết nối thư mục KTC cho đơn vị PHONG-ABC”.", "",
          "**Đạt khi:** (1) thư mục có `10-Dau-Vao/`, `30-Ket-Qua/`, `00-HUONG-DAN.md`, `KTC-THU-MUC-LAM-VIEC.json`; đầu phiên sau",
          "có dòng “thư mục làm việc đơn vị P-TCCB”; (2) Claude đọc đúng tệp trong `10-Dau-Vao/`, lưu kết quả vào",
          "`30-Ket-Qua/<ngày>/<loại>/` tên dạng `P-TCCB_…`, không sửa tệp gốc, nhắc người dùng tự gửi về P-THHC; (3) bị từ chối",
          "vì mã ngoài 11 mã chuẩn (hoặc Claude hỏi lại mã) — không tạo thư mục cho mã tự đặt.", "",
          BANG_KET_QUA,
          "## Kết luận nghiệm thu", "",
          "| Nền tảng | Số ca đạt / tổng | Ca không đạt | Kết luận (Đạt / Đạt có điều kiện / Không đạt) | Ký xác nhận |",
          "|---|---|---|---|---|", "| Claude (trò chuyện) | / 15 | | | |", "| Claude Cowork | / 18 | | | |", ""]
    out = "\n".join(d)
    if a.ra:
        io.open(a.ra, "w", encoding="utf-8").write(out)
    print(f"{len([p for p in glob.glob(os.path.join(BO_CA, '[0-9][0-9]-*')) if os.path.isdir(p)])} ca + 3 ca Cowork -> {a.ra or 'stdout'}")


if __name__ == "__main__":
    main()
