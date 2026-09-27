# -*- coding: utf-8 -*-
"""Thong ke van hanh thuc te cua Bo cong cu KTC-Quan-tri tu nhat ky tu dong + san pham 30-Ket-Qua + git.

Dung cho: (1) bang chung "du lieu van hanh that" (tham dinh lan 4 — nguoi phu trach da dung thuong xuyen tu 18/9/2026);
(2) bao cao hau thi diem (ChatGPT L4 muc VIII, Copilot, Grok: so phien, ky nang kich hoat, san pham, loi).
Chi doc; KHONG in noi dung loi nhan hay cau lenh (nhat ky 1.3.1 da khong luu).

    python 29-Cong-Cu/thong_ke_van_hanh.py [--tu 2026-09-18] [--den 2026-09-27] [--ra <tep.md>]
"""
import argparse
import collections
import datetime as dt
import glob
import io
import json
import os
import re
import subprocess

DU_AN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(DU_AN, "90-Nhat-Ky-Van-Hanh", "04-Nhat-Ky-Tu-Dong")
KQ = os.path.join(DU_AN, "30-Ket-Qua")
# thu muc san pham phuc vu tham dinh chinh Bo cong cu — tach rieng khoi san pham nghiep vu
TU_THAN = re.compile(r"(Plugin|Nghiem-thu|Ho-So-Tham-Dinh|log-hoi-quy|chi-tiet|1-Plugin|2-Nghiem-thu|3-Ra-soat-897|4-Van-ban|"
                     r"ban-nen|De-Xuat-Kho)", re.I)
TAI_LIEU_BO_CONG_CU = re.compile(r"(KTC-Quan-tri|tham-dinh|Tham-dinh|SKILL_)", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tu", default="2026-09-01")
    ap.add_argument("--den", default=dt.date.today().isoformat())
    ap.add_argument("--ra")
    a = ap.parse_args()

    ngay = collections.Counter()
    phien_ngay = collections.defaultdict(set)
    cong_cu = collections.Counter()
    skill = collections.Counter()
    agent = collections.Counter()
    tin_hieu = collections.Counter()
    loi = yeu_cau = 0
    for f in sorted(glob.glob(os.path.join(LOG, "*.jsonl"))):
        n = os.path.basename(f)[:10]
        if not (a.tu <= n <= a.den):
            continue
        for line in io.open(f, encoding="utf-8", errors="ignore"):
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("phien"):
                phien_ngay[n].add(d["phien"])
            if d.get("loai") == "thao-tac":
                ngay[n] += 1
                cong_cu[d.get("cong_cu")] += 1
                loi += 1 if d.get("loi") else 0
                if d.get("cong_cu") == "Skill":
                    skill[d.get("doi_tuong", "")] += 1
                if d.get("cong_cu") == "Agent":
                    agent[(d.get("doi_tuong") or "").split(":")[0] or "general"] += 1
            elif d.get("loai") == "yeu-cau":
                yeu_cau += 1
                for t in d.get("tin_hieu", []):
                    tin_hieu[t] += 1
    phien = set().union(*phien_ngay.values()) if phien_ngay else set()

    sp = collections.defaultdict(lambda: collections.Counter())
    for p in glob.glob(os.path.join(KQ, "2026-*", "**", "*.*"), recursive=True):
        n = os.path.relpath(p, KQ).split(os.sep)
        if not (a.tu <= n[0] <= a.den) or not p.lower().endswith((".docx", ".xlsx", ".md")):
            continue
        nhom = "Tự thân Bộ công cụ (thẩm định, bằng chứng)" if (TU_THAN.search("/".join(n[1:-1]))
                                                             or TAI_LIEU_BO_CONG_CU.search(n[-1])) \
            else (n[1] if len(n) > 2 else "(gốc ngày)")
        sp[nhom][os.path.splitext(p)[1].lower()] += 1

    try:
        so_commit = subprocess.run(["git", "rev-list", "--count", f"--since={a.tu}", "HEAD"], cwd=DU_AN,
                                   capture_output=True, text=True).stdout.strip()
    except Exception:
        so_commit = "?"

    d = [f"# Thống kê vận hành thực tế Bộ công cụ KTC-Quan-tri ({a.tu} → {a.den})", "",
         "Nguồn: nhật ký tự động `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/` (chỉ thông tin mô tả — không có nội dung lời nhắn,",
         "câu lệnh), sản phẩm trong `30-Ket-Qua/`, lịch sử git. Sinh bằng `29-Cong-Cu/thong_ke_van_hanh.py` (lặp lại được).",
         "**Phạm vi:** vận hành của người phụ trách xây dựng trên Claude Code (máy Phòng TH-HC&QT), việc thật của Phòng —",
         "**không** phải thí điểm tại các đơn vị; không suy ra kết quả cho Claude (trò chuyện), Cowork.", "",
         "## 1. Tổng quan", "",
         "| Chỉ số | Giá trị |", "|---|---:|",
         f"| Số ngày có làm việc | {len(ngay)} |", f"| Số phiên làm việc | {len(phien)} |",
         f"| Số thao tác công cụ | {sum(cong_cu.values()):,} |", f"| Số lượt yêu cầu của người dùng | {yeu_cau} |",
         f"| Thao tác báo lỗi (hook ghi nhận) | {loi} |", f"| Lần cập nhật mã nguồn (git) | {so_commit} |",
         f"| Tín hiệu học (sửa sai / quy ước / quyết định) | {tin_hieu.get('sua-sai', 0)} / {tin_hieu.get('quy-uoc', 0)} / {tin_hieu.get('quyet-dinh', 0)} |",
         "", "## 2. Theo ngày", "", "| Ngày | Phiên | Thao tác |", "|---|---:|---:|"]
    for n in sorted(ngay):
        d.append(f"| {n} | {len(phien_ngay[n])} | {ngay[n]} |")
    d += ["", "## 3. Công cụ, kỹ năng, tác tử được gọi", "", "| Loại | Số lần |", "|---|---:|"]
    d += [f"| {k} | {v} |" for k, v in cong_cu.most_common()]
    d += ["", "| Kỹ năng gọi đích danh (Skill) | Số lần |", "|---|---:|"] + [f"| `{k}` | {v} |" for k, v in skill.most_common()]
    d += ["", "| Tác tử (Agent) | Số lần |", "|---|---:|"] + [f"| `{k}` | {v} |" for k, v in agent.most_common()]
    d += ["", "Lưu ý: kỹ năng được nạp tự động theo mô tả không luôn hiện thành một lần gọi `Skill` trong nhật ký; số trên là",
          "**cận dưới** của số lần dùng kỹ năng.", "", "## 4. Sản phẩm tạo ra (tệp .docx, .xlsx, .md trong 30-Ket-Qua)", "",
          "| Nhóm (thư mục loại việc) | .docx | .xlsx | .md |", "|---|---:|---:|---:|"]
    for k in sorted(sp, key=lambda x: (x.startswith("Tự thân"), x)):
        c = sp[k]
        d.append(f"| {k} | {c['.docx']} | {c['.xlsx']} | {c['.md']} |")
    d += ["", "## 5. Giới hạn của số liệu", "",
          "- Nhật ký chỉ ghi khi làm việc trong thư mục dự án; phiên trên Claude (trò chuyện), Cowork không có ở đây.",
          "- Hook `loi` chỉ bắt lỗi công cụ mà ứng dụng báo về; lỗi nghiệp vụ (số liệu sai) phát hiện qua rà soát, kiểm thử.",
          "- Chưa đo token thực tế theo tác vụ (ứng dụng không trả số token cho hook) — thí điểm cần ghi theo phiếu."]
    out = "\n".join(d) + "\n"
    if a.ra:
        io.open(a.ra, "w", encoding="utf-8").write(out)
    print(out)


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
