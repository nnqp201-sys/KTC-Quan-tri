# -*- coding: utf-8 -*-
"""Bộ kiểm thử hồi quy KTC-RIS v2.5.1 — chạy: python3 test_regression_v251.py
Tự sinh fixture, chạy 14 phép kiểm, in PASS/FAIL."""
import os, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_fixtures_test as MK
import read_bc736_excel as R

TMP = tempfile.mkdtemp(prefix="ktc_qa_")
MK.OUT = TMP + "/"
ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    if cond: ok += 1; print(f"  PASS  {name}")
    else:    fail += 1; print(f"  FAIL  {name}  {detail}")

MK.make_iib(TMP+"/a.xlsx", truc_label_style="plain", put_sum_row=True)
MK.make_iib(TMP+"/b.xlsx", truc_label_style="numbered", put_sum_row=True)
MK.make_ib(TMP+"/c.xlsx")

print("== read_bc736_excel ==")
a = R.read_appendix(TMP+"/a.xlsx")
check("BUG-01 nhận diện KQ khi KPI ở hàng gộp", a["kind"] == "KQ", a["kind"])
check("BUG-02 nhận nhãn 'Trục 1.' không số dẫn đầu", a["thong_ke"]["so_nhiem_vu"] == 4, a["thong_ke"])
check("BUG-03 dòng Tổng không tính là nhiệm vụ", len(a["truc"][1]) == 2, len(a["truc"][1]))
check("BUG-04 truc_tong đọc từ dòng Tổng", a["truc_tong"].get(1, {}).get("so_luong_quy_doi") == 3.5)
check("BUG-06 phát hiện hệ số sai", any("SAI CT (9)" in w for w in a["canh_bao"]))
b = R.read_appendix(TMP+"/b.xlsx")
check("BUG-02b nhãn có số dẫn đầu vẫn chạy", b["thong_ke"]["so_nhiem_vu"] == 4)
agg = R.summarize_truc_kpi(a)
check("BUG-03b cộng dồn không nhân đôi", agg[1]["so_luong_quy_doi"] == 3.5, agg[1]["so_luong_quy_doi"])
agg2 = R.summarize_truc_kpi([a, b])
check("cộng dồn 2 đơn vị", agg2[1]["so_luong_quy_doi"] == 7.0, agg2[1]["so_luong_quy_doi"])
c = R.read_appendix(TMP+"/c.xlsx")
check("nhận diện KH", c["kind"] == "KH", c["kind"])
check("BUG-07 ghi chú hợp lệ không báo lỗi giả",
      not any("KHÔNG CHUẨN" in w for w in c["canh_bao"]), c["canh_bao"])
f = R.filter_truong_level(c)
check("BUG-08 lọc được cả ghi chú thừa dấu cách",
      sum(len(v) for v in f.values()) == 2, sum(len(v) for v in f.values()))

print("== fill_bc736 ==")
try:
    from docx import Document
    from docx.shared import RGBColor, Pt
    from docx.enum.text import WD_COLOR_INDEX
    import fill_bc736 as F
    doc = Document()
    tb = doc.add_table(rows=1, cols=1)
    r = tb.cell(0,0).paragraphs[0].add_run("Số: […]/BC-CĐKT"); r.font.color.rgb = RGBColor(0xEE,0,0)
    p = doc.add_paragraph(); rr = p.add_run("* Công tác đào tạo: "); rr.bold = True
    r2 = p.add_run("Nội dung công tác đào tạo"); r2.font.color.rgb = RGBColor(0xEE,0,0); r2.font.highlight_color = WD_COLOR_INDEX.YELLOW
    p2 = doc.add_paragraph(); r3 = p2.add_run("* Công tác đào tạo nghề nông thôn: "); r3.bold = True
    r4 = p2.add_run("Nội dung công tác đào tạo nghề nông thôn"); r4.font.color.rgb = RGBColor(0xEE,0,0); r4.font.highlight_color = WD_COLOR_INDEX.YELLOW
    doc.save(TMP+"/t.docx")
    res = F.fill_report(TMP+"/t.docx", TMP+"/o.docx",
                        {"Nội dung công tác đào tạo": "AAA",
                         "Nội dung công tác đào tạo nghề nông thôn": "BBB",
                         "Khóa thừa": "X"}, 7, 8, 2026)
    d = Document(TMP+"/o.docx")
    texts = [p.text for p in F.iter_all_paragraphs(d) if p.text.strip()]
    check("BUG-11 giữ nhãn in đậm", any(t.startswith("* Công tác đào tạo: AAA") for t in texts), texts)
    check("BUG-10 khóa dài không bị khóa ngắn chiếm chỗ",
          any("nghề nông thôn: BBB" in t for t in texts), texts)
    check("BUG-12 quét được bảng (giữ nguyên dòng Số:)", res["skipped_control"] == 1, res["skipped_control"])
    check("BUG-13 báo khóa thừa", res["unused_keys"] == ["Khóa thừa"], res["unused_keys"])
except ImportError:
    print("  BỎ QUA (thiếu python-docx)")

print(f"\nKẾT QUẢ: {ok} PASS / {fail} FAIL")
sys.exit(1 if fail else 0)
