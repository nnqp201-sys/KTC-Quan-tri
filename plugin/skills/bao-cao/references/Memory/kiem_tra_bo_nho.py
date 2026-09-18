# -*- coding: utf-8 -*-
"""
kiem_tra_bo_nho.py — Kiểm tra sức khỏe lớp bộ nhớ quá trình KTC-RIS.
Chạy ĐẦU MỖI PHIÊN: python3 references/Memory/kiem_tra_bo_nho.py

In ra: phiên bản đang cài · việc đang treo · lỗi đang mở · đơn vị cần lưu ý ·
cảnh báo nếu bộ nhớ lâu chưa cập nhật.

Bộ nhớ không được cập nhật còn tệ hơn không có bộ nhớ — nó tạo cảm giác an tâm giả.
Script này tồn tại để phát hiện chính tình huống đó.
"""
import os
import re
import sys
from datetime import datetime, date

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
NGUONG_NGAY_CU = 45  # quá số ngày này chưa cập nhật -> cảnh báo


def doc(ten):
    p = os.path.join(HERE, ten)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return f.read()


def phien_ban_dang_cai():
    p = os.path.join(SKILL_ROOT, "SKILL.md")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        head = f.read(4000)
    m = re.search(r"KTC-RIS\s+v([\d.]+)", head)
    return m.group(1) if m else None


def ngay_cap_nhat(noi_dung):
    if not noi_dung:
        return None
    m = re.search(r"Cập nhật lần cuối:\s*\*\*(\d{2})/(\d{2})/(\d{4})\*\*", noi_dung)
    if not m:
        return None
    d, mo, y = (int(x) for x in m.groups())
    try:
        return date(y, mo, d)
    except ValueError:
        return None


def main():
    canh_bao = []
    print("=" * 68)
    print("KIỂM TRA BỘ NHỚ QUÁ TRÌNH KTC-RIS")
    print("=" * 68)

    # 1. Đủ file chưa
    can_co = ["README.md", "TRANG-THAI.md", "01-Nhat-Ky-Chay.md",
              "02-So-Dang-Ky-Loi.md", "03-Chat-Luong-Du-Lieu-Don-Vi.md",
              "04-Nhat-Ky-Quyet-Dinh.md", "05-Bai-Hoc.md"]
    thieu = [f for f in can_co if not os.path.exists(os.path.join(HERE, f))]
    if thieu:
        canh_bao.append("Thiếu file bộ nhớ: " + ", ".join(thieu))
        print("\n[!] THIẾU FILE:", ", ".join(thieu))
    else:
        print("\n[OK] Đủ %d file bộ nhớ." % len(can_co))

    # 2. Phiên bản
    tt = doc("TRANG-THAI.md")
    pb_cai = phien_ban_dang_cai()
    print("\n--- PHIÊN BẢN ---")
    print("  SKILL.md đang ghi: v%s" % (pb_cai or "KHÔNG ĐỌC ĐƯỢC"))
    if tt:
        m = re.search(r"Bản cài trong thư mục skill \|\s*\*\*v([\d.]+)\*\*", tt)
        pb_ghi_nho = m.group(1) if m else None
        if pb_ghi_nho:
            print("  Bộ nhớ ghi nhận:   v%s" % pb_ghi_nho)
            if pb_cai and pb_ghi_nho != pb_cai:
                canh_bao.append(
                    "LỆCH PHIÊN BẢN: SKILL.md = v%s nhưng bộ nhớ ghi v%s. "
                    "Nhiều khả năng bản vá phiên trước đã MẤT (xem BH-06) — cài lại file .skill."
                    % (pb_cai, pb_ghi_nho))

    # 3. Độ mới
    print("\n--- ĐỘ MỚI ---")
    nc = ngay_cap_nhat(tt)
    if nc:
        so_ngay = (date.today() - nc).days
        print("  TRANG-THAI.md cập nhật: %s (%d ngày trước)" % (nc.strftime("%d/%m/%Y"), so_ngay))
        if so_ngay > NGUONG_NGAY_CU:
            canh_bao.append("TRANG-THAI.md đã %d ngày chưa cập nhật — nội dung có thể không còn đúng. "
                            "Rà lại trước khi tin." % so_ngay)
    else:
        canh_bao.append("Không đọc được ngày cập nhật của TRANG-THAI.md.")

    # 4. Việc treo
    print("\n--- VIỆC ĐANG TREO ---")
    if tt:
        treo = re.findall(r"^\|\s*\d+\s*\|\s*(.+?)\s*\|\s*([⏸❌✅⬜][^|]*)\|", tt, re.M)
        if treo:
            for viec, tt_ in treo:
                print("  %-52s %s" % (viec.replace("**", "")[:52], tt_.strip()))
        else:
            print("  (không đọc được bảng việc treo)")

    # 5. Lỗi đang mở
    print("\n--- LỖI ĐANG MỞ TRÊN BẢN ĐANG DÙNG ---")
    sdl = doc("02-So-Dang-Ky-Loi.md")
    if sdl:
        mo = re.findall(r"\*\*(BUG-\d+)[^\n]*?\*\*\s*\|[^\n]*", sdl)
        muc = re.search(r"## Lỗi đang MỞ cần lưu ý ngay\n(.*?)(?=\n## )", sdl, re.S)
        if muc:
            for dong in muc.group(1).strip().splitlines():
                if dong.strip():
                    print("  " + dong.strip().lstrip("- ")[:100])
        if mo:
            canh_bao.append("Có lỗi đang mở: " + ", ".join(sorted(set(mo))))

    # 6. Đơn vị cần lưu ý
    print("\n--- ĐƠN VỊ CẦN LƯU Ý KỲ TỚI ---")
    cl = doc("03-Chat-Luong-Du-Lieu-Don-Vi.md")
    if cl:
        for m in re.finditer(r"^### ([🔴🟡⬜])\s*(.+)$", cl, re.M):
            print("  %s %s" % (m.group(1), m.group(2)[:60]))
        chua_xm = len(re.findall(r"\[CHƯA XÁC MINH\]", cl))
        if chua_xm:
            print("  → có %d mục [CHƯA XÁC MINH] cần đối chiếu file gốc trước khi dùng" % chua_xm)

    # 7. Kết luận
    print("\n" + "=" * 68)
    if canh_bao:
        print("CẦN XỬ LÝ (%d):" % len(canh_bao))
        for c in canh_bao:
            print("  ! " + c)
    else:
        print("Bộ nhớ ở trạng thái tốt. Đọc TRANG-THAI.md rồi bắt đầu làm việc.")
    print("=" * 68)
    return 1 if canh_bao else 0


if __name__ == "__main__":
    sys.exit(main())
