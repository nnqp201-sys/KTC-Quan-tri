# -*- coding: utf-8 -*-
"""Kiểm thử đầy đủ 45/45 vị trí thật trong mẫu TB736 — mỗi vị trí 1 token duy nhất
để phát hiện chính xác nếu có lẫn lộn giữa các vị trí (dù cùng Phần hay khác Phần)."""

PHAN_I_LABELS = [
    "Công tác tuyển sinh", "Công tác đào tạo", "Công tác khảo thí",
    "Công tác bảo đảm chất lượng", "Công tác kế hoạch, tổng hợp",
    "Công tác tổ chức, cán bộ", "Về thể chế", "Công tác Kiểm tra, giám sát",
    "Thúc đẩy phát triển KH-CN, đổi mới sáng tạo và chuyển đổi số",
    "Công tác xây dựng Đảng", "Chấp hành kỷ cương hành chính",
    "Công tác Đảng, Công đoàn, Đoàn Thanh niên",
    "Công tác quản lý cơ sở vật chất", "Công tác Tài chính",
    "Công tác an sinh giáo dục", "Công tác truyền thông",
    "Về Quốc phòng - An ninh", "Về hoạt động Đối ngoại và Hợp tác",
    "Về hoạt động hợp tác phát triển",
    "Nghị quyết số 59-NQ/TW", "Nghị quyết số 66-NQ/TW", "Nghị quyết số 68-NQ/TW",
    "Nghị quyết số 79-NQ/TW", "Nghị quyết số 70-NQ/TW", "Nghị quyết số 71-NQ/TW",
    "Nghị quyết số 72-NQ/TW", "Nghị quyết số 80-NQ/TW",
]
PHAN_II_LABELS = ["kết quả đạt được", "tồn tại, hạn chế"]
PHAN_III_LABELS = [
    "Công tác tuyển sinh", "Công tác đào tạo", "Công tác khảo thí",
    "Công tác bảo đảm chất lượng", "Công tác kế hoạch, tổng hợp",
    "Công tác tổ chức, cán bộ", "Về thể chế", "Công tác Kiểm tra, giám sát",
    "Thúc đẩy phát triển KH-CN, đổi mới sáng tạo và chuyển đổi số",
    "Công tác xây dựng Đảng", "Công tác Công đoàn, Đoàn Thanh niên",
    "Công tác Quản lý cơ sở vật chất", "Công tác Tài chính",
    "Về công tác an sinh, giáo dục", "Về công tác Truyền thông",
    "Củng cố quốc phòng, an ninh",
]

assert len(PHAN_I_LABELS) == 27
assert len(PHAN_II_LABELS) == 2
assert len(PHAN_III_LABELS) == 16


def _mk_token(prefix, i, label):
    """1 HÀM DUY NHẤT sinh token — dùng chung cho cả lúc ghi lẫn lúc kiểm tra,
    tránh lệch nhau như lỗi vừa gặp (do viết token generation ở 2 chỗ khác nhau)."""
    safe = label[:15].replace(" ", "_").replace(",", "").replace("/", "")
    return f"TOKEN_{prefix}_{i:02d}_{safe}"


def build_content_by_phase():
    content_by_phase = {"PHAN_I": {}, "PHAN_II": {}, "PHAN_III": {}}
    for i, label in enumerate(PHAN_I_LABELS, 1):
        content_by_phase["PHAN_I"][label] = _mk_token("I", i, label)
    for i, label in enumerate(PHAN_II_LABELS, 1):
        content_by_phase["PHAN_II"][label] = _mk_token("II", i, label)
    for i, label in enumerate(PHAN_III_LABELS, 1):
        content_by_phase["PHAN_III"][label] = _mk_token("III", i, label)
    return content_by_phase


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '.')
    from fill_bc736 import fill_report
    from docx import Document

    content_by_phase = build_content_by_phase()
    result = fill_report(
        "00__Mau_bao_cao_thang__cap_Truong_.docx",
        "TEST_full45.docx",
        content_by_phase, 7, 8, 2026,
    )
    print("Đã điền:", result["filled"], "| Còn thiếu:", result["missing"])
    print("Cảnh báo:", len(result["canh_bao"]))
    for w in result["canh_bao"]:
        print("  -", w)

    doc = Document("TEST_full45.docx")
    full_text = "\n".join(p.text for p in doc.paragraphs)

    ok, fail = 0, 0
    for ph_key, labels in [("PHAN_I", PHAN_I_LABELS), ("PHAN_II", PHAN_II_LABELS), ("PHAN_III", PHAN_III_LABELS)]:
        prefix = {"PHAN_I": "I", "PHAN_II": "II", "PHAN_III": "III"}[ph_key]
        for i, label in enumerate(labels, 1):
            token = _mk_token(prefix, i, label)
            count = full_text.count(token)
            if count == 1:
                ok += 1
            else:
                fail += 1
                print(f"❌ FAIL [{ph_key}] '{label}' -> token xuất hiện {count} lần (kỳ vọng 1): {token}")

    print(f"\n=== KẾT QUẢ: {ok}/45 ĐÚNG, {fail}/45 SAI ===")
    sys.exit(1 if fail else 0)
