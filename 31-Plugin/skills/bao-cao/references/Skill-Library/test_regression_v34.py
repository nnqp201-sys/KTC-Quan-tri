# -*- coding: utf-8 -*-
"""Bộ kiểm thử hồi quy v3.3 — đầy đủ nhất: 15 test gốc v2.5.1 + 2 test Mục II +
4 test API mới + 6 test tách Phần I/III mẫu nhỏ + ĐỦ 45/45 VỊ TRÍ THẬT trong mẫu."""
import os, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_fixtures_test as MK
import read_bc736_excel as R

TMP = tempfile.mkdtemp(prefix="ktc_qa33_")
MK.OUT = TMP + "/"
ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    if cond: ok += 1; print(f"  PASS  {name}")
    else:    fail += 1; print(f"  FAIL  {name}  {detail}")

MK.make_iib(TMP+"/a.xlsx", truc_label_style="plain", put_sum_row=True)
MK.make_iib(TMP+"/b.xlsx", truc_label_style="numbered", put_sum_row=True)
MK.make_ib(TMP+"/c.xlsx")

print("== read_bc736_excel (11 test gốc v2.5.1) ==")
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

print("== [v3.1] Logic Mục II trên file THẬT ==")
r_real = R.read_appendix(HERE + "/test_real_format.xlsx", "PL IIb - Test That")
check("Mục II tách riêng đúng 2 việc", len(r_real["muc_ii_items"]) == 2, len(r_real["muc_ii_items"]))
check("Trục 2 KHÔNG lẫn việc của Mục II", len(r_real["truc"][2]) == 1, len(r_real["truc"][2]))

print("== fill_bc736 (4 test API mới) ==")
try:
    from docx import Document
    from docx.shared import RGBColor
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
                        {"HEADER": {"Nội dung công tác đào tạo": "AAA",
                                     "Nội dung công tác đào tạo nghề nông thôn": "BBB",
                                     "Khóa thừa": "X"}}, 7, 8, 2026)
    d = Document(TMP+"/o.docx")
    texts = [p.text for p in F.iter_all_paragraphs(d) if p.text.strip()]
    check("BUG-11 giữ nhãn in đậm", any(t.startswith("* Công tác đào tạo: AAA") for t in texts), texts)
    check("BUG-10 khóa dài không bị khóa ngắn chiếm chỗ",
          any("nghề nông thôn: BBB" in t for t in texts), texts)
    check("BUG-12 quét được bảng (giữ nguyên dòng Số:)", res["skipped_control"] == 1, res["skipped_control"])
    check("BUG-13 báo khóa thừa", res["unused_keys"] == [("HEADER", "Khóa thừa")], res["unused_keys"])
except ImportError:
    print("  BỎ QUA (thiếu python-docx)")

print("== [v3.2, ĐẦY ĐỦ] Toàn bộ 45/45 vị trí thật trong mẫu TB736 ==")
import build_full_45_test as FULL45
content_by_phase_45 = FULL45.build_content_by_phase()
res45 = F.fill_report(HERE + "/00__Mau_bao_cao_thang__cap_Truong_.docx", TMP+"/o45.docx",
                      content_by_phase_45, 7, 8, 2026)
d45 = Document(TMP+"/o45.docx")
full_text_45 = "\n".join(p.text for p in d45.paragraphs)
n_ok_45 = 0
for ph_key, labels in [("PHAN_I", FULL45.PHAN_I_LABELS), ("PHAN_II", FULL45.PHAN_II_LABELS), ("PHAN_III", FULL45.PHAN_III_LABELS)]:
    prefix = {"PHAN_I":"I","PHAN_II":"II","PHAN_III":"III"}[ph_key]
    for i, label in enumerate(labels, 1):
        token = FULL45._mk_token(prefix, i, label)
        if full_text_45.count(token) == 1:
            n_ok_45 += 1
check("Đủ 45/45 vị trí thật đều điền đúng, không lẫn lộn", n_ok_45 == 45, f"{n_ok_45}/45")

print("== [v3.4] Kiểm thử SÂU — xung đột API & bảo vệ đầu vào ==")
# XUNG ĐỘT 1: skeleton phải tương thích trực tiếp với fill_report
r_skel = R.read_appendix(HERE + "/test_real_format.xlsx", "PL IIb - Test That")
skel = R.build_content_map_skeleton(r_skel)
check("build_content_map_skeleton trả về đúng 3 tầng PHAN_I/II/III",
      set(skel.keys()) == {"PHAN_I", "PHAN_II", "PHAN_III"}, list(skel.keys()))
try:
    F.fill_report(HERE + "/00__Mau_bao_cao_thang__cap_Truong_.docx", TMP+"/oskel.docx",
                  skel, 7, 8, 2026)
    check("skeleton -> fill_report KHÔNG còn crash", True)
except Exception as e:
    check("skeleton -> fill_report KHÔNG còn crash", False, f"{type(e).__name__}: {e}")

# XUNG ĐỘT 2: Mục II phải xuất hiện trong khung nháp (không bị bỏ quên)
check("Mục II được đưa vào khung nháp (không bị bỏ quên)",
      any("MucII" in k for k in skel["PHAN_I"]), list(skel["PHAN_I"].keys()))

# XUNG ĐỘT 1b: truyền dict phẳng phải báo lỗi RÕ RÀNG, không crash khó hiểu
try:
    F.fill_report(HERE + "/00__Mau_bao_cao_thang__cap_Truong_.docx", TMP+"/oflat.docx",
                  {"khóa phẳng": "giá trị"}, 7, 8, 2026)
    check("Dict phẳng bị chặn với thông báo rõ ràng", False, "không báo lỗi")
except TypeError as e:
    check("Dict phẳng bị chặn với thông báo rõ ràng",
          "build_content_map_skeleton" in str(e), str(e)[:80])
except Exception as e:
    check("Dict phẳng bị chặn với thông báo rõ ràng", False, f"sai loại lỗi: {type(e).__name__}")

# XUNG ĐỘT 5: tên Phần sai phải cảnh báo đúng nguyên nhân
r_wrong = F.fill_report(HERE + "/00__Mau_bao_cao_thang__cap_Truong_.docx", TMP+"/owrong.docx",
                        {"phan_i": {"Công tác tuyển sinh": "Y"}}, 7, 8, 2026)
check("Tên Phần sai -> cảnh báo đúng nguyên nhân (không đổ lỗi cho tên khóa)",
      any("TÊN PHẦN SAI" in w for w in r_wrong["canh_bao"]), r_wrong["canh_bao"][:2])

# Nội dung THẬT có dấu câu/số/ký tự đặc biệt phải giữ nguyên
r_real_content = F.fill_report(
    HERE + "/00__Mau_bao_cao_thang__cap_Truong_.docx", TMP+"/oreal.docx",
    {"PHAN_I": {"Công tác tuyển sinh": "Đạt 1.049/1.200 chỉ tiêu (87,4%); tăng <5% & ổn định."},
     "PHAN_II": {}, "PHAN_III": {}}, 7, 8, 2026)
d_real = Document(TMP+"/oreal.docx")
txt_real = "\n".join(p.text for p in d_real.paragraphs)
check("Nội dung thật (số, %, ngoặc, &, <) giữ nguyên không bị lỗi XML",
      "1.049/1.200" in txt_real and "87,4%" in txt_real and "<5% &" in txt_real)

print(f"\nKẾT QUẢ: {ok} PASS / {fail} FAIL")
sys.exit(1 if fail else 0)
