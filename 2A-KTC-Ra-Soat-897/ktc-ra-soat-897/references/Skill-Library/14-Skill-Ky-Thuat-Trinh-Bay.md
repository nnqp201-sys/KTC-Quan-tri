# 14-Skill-Ky-Thuat-Trinh-Bay

## Purpose
Kiểm tra kỹ thuật trình bày chi tiết của văn bản (khác với thể thức tổng thể ở Skill 02): font, cỡ chữ, khoảng cách dòng, heading, đánh số, bullet, viết hoa, canh lề, số trang, số mục.

## When to use
- Trước khi trình ký, sau khi nội dung đã ổn định.
- Khi văn bản có nhiều cấp mục (Điều/Khoản/Điểm, Phần/Mục) cần đánh số nhất quán.

## Inputs
- Toàn văn bản (định dạng .docx nếu có thể, hoặc text)
- Loại văn bản; chuẩn trình bày: `references/Quy-Tac-KTC/01-Bang-Thong-So-The-Thuc-KTC.md` (TB 597/TB-CĐKT, QĐ 1355/QĐ-CĐKT trước, NĐ 30/2020 sau)

## Checklist logic
- Đo bằng `tools/kiem_tra_the_thuc.py`; thông số cố định theo bảng KTC: A4; lề trên/dưới 2 cm, trái 3 cm, phải 2 cm; header/footer 1,27 cm; lời văn cỡ 14; Before/After ≥ 6 pt; giãn dòng từ Single đến 1,5 lines, chỉ kiểu theo dòng (TB 597 mục 6 đính chính 27/10/2026: không dùng Exactly/At least); thụt đầu dòng 1–1,27 cm
- Số trang: giữa lề trên, cỡ 14; văn bản kèm theo section mới, đánh liên tục; phụ lục đánh riêng từ 1, hiện số trang đầu, phụ lục 1 trang không đánh số
- Phụ lục: “Phụ lục I, II…” (La Mã, “Phụ lục” in thường); tiêu đề in hoa, căn giữa, dòng cuối riêng “CỦA TRƯỜNG CAO ĐẲNG KON TUM”; đường kẻ 1/3–1/2; không có dòng “(Kèm theo …)”
- Bảng: canh giữa trang; ô canh giữa theo chiều dọc
- Đánh số Điều/Khoản/Điểm hoặc 1./1.1./a) nhất quán trong toàn văn bản
- Heading/tiêu đề in hoa, đậm, căn giữa đúng cấp độ
- Số trang, số mục đúng vị trí (giữa, dưới, hoặc theo mẫu)

## Output
- Bảng lỗi trình bày theo từng mục (vị trí, lỗi, đề xuất sửa)
- Mức độ: theo bảng mã `references/Quy-Tac-KTC/02-Quy-Tac-Xep-Muc.md` (thể thức TT = Mức 2; kỹ thuật soạn thảo TB = Mức 3/4)

## Must not do
- Không sửa nội dung khi chỉ đang kiểm tra trình bày.
- Không bỏ qua lỗi đánh số không nhất quán dù nhỏ.

## Related
- Skill: `02-Skill-Kiem-Tra-The-Thuc.md` (thể thức tổng thể)
- Checklist: `references/Checklist/05-Hinh-Thuc.md`, `01-The-Thuc.md`
