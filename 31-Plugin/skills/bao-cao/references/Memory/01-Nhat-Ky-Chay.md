# NHẬT KÝ CHẠY KTC-RIS

Ghi lại **từng kỳ đã chạy**: làm gì, lệch chuẩn ở đâu, xử lý ra sao.
Mục mới thêm lên **đầu file**. Mẫu ghi: `assets/mau-nhat-ky-chay.md`.

Đây là phần trả lời được câu hỏi "tháng trước mình làm thế nào?" — câu hỏi hay gặp nhất đầu mỗi kỳ.

---

## 2026-08-19 — Bảo trì công cụ (ngoài chu kỳ báo cáo)

**Loại:** Bảo trì · **Người thực hiện:** Phòng TH-HC&QT + Claude

**Đã làm:**
1. Kiểm tra phiên bản skill đang cài — phát hiện phần mô tả ghi v2.5 nhưng nội dung thực tế là v2.3.
2. Dựng 5 fixture Excel + 1 fixture Word mô phỏng cấu trúc TB736, chạy kiểm thử sâu.
3. Phát hiện và vá **14 lỗi** (9 ở `read_bc736_excel.py`, 5 ở `fill_bc736.py`) → bản v2.5.1.
4. Viết bộ kiểm thử hồi quy `test_regression_v251.py` — đạt 15/15.
5. So sánh đối chứng v2.5.1 với v3.0 người dùng cung cấp → phát hiện thêm BUG-15, BUG-16.
6. Dựng lớp bộ nhớ quá trình `references/Memory/`.

**Lệch chuẩn / bất thường:**
- Kết luận sai ở đầu phiên rằng thư mục skill không ghi được → đã đính chính (xem BH-04).
- Mục D của `PATCH-NOTES-v2.5.1.md` nêu 4 đơn vị có lỗi dữ liệu tháng 8, nhưng chỉ 2 đơn vị
  xác minh được từ ngữ cảnh; 2 đơn vị còn lại (TC-KT, Khoa Sư phạm) **chưa đối chiếu file gốc**.
  Đã đánh dấu `[CHƯA XÁC MINH]` trong `03-Chat-Luong-Du-Lieu-Don-Vi.md`.

**Còn treo:** Gộp v3.1 (QĐ-05) · cài vĩnh viễn · chạy kiểm thử trên file thật.

---

## 2026-08-14 (khoảng) — Báo cáo tháng 7/2026

**Loại:** Kỳ báo cáo tháng · **Sản phẩm:** `BC_thang_7_2026_cap_Truong.docx`

**Đã làm:** Đọc mẫu Word + Phụ lục Excel cấp Trường thật từ Drive; chuyển văn phong sang chủ ngữ
"Nhà trường"; dựng báo cáo theo cấu trúc TB736 (I: 6 Trục + Mục 7 Nghị quyết → II: Đánh giá chung
→ III: Nhiệm vụ trọng tâm tháng 8).

**Lệch chuẩn:** Dựng **thủ công bằng docx-js**, không qua `fill_bc736.py`.
→ *Hệ quả có lợi:* sản phẩm không dính 14 lỗi phát hiện ngày 19/08, **không cần làm lại**.

**Bỏ qua:** Bước 3 (tính % KPI theo Trục) và Bước 4 (đối chiếu Kế hoạch quý) — chưa chạy.

**Vấn đề:** Nhiều mục thiếu dữ liệu (khảo thí, bảo đảm chất lượng, kiểm tra giám sát, truyền thông,
đối ngoại, 8 Nghị quyết Bộ Chính trị, tồn tại-hạn chế) → đánh dấu `[CẦN BỔ SUNG]` theo QĐ-01.

---

## 2026-08 — Báo cáo tháng 8/2026

**Loại:** Kỳ báo cáo tháng · **Trạng thái:** đã có sản phẩm, còn tồn đọng

**Vấn đề dữ liệu:** Phòng TH-HC&QT chỉ nộp báo cáo Ban Truyền thông; Khoa Kỹ thuật và Công nghệ
nộp IIb sai cấu trúc, không tính được cascade KPI. Chi tiết: `03-Chat-Luong-Du-Lieu-Don-Vi.md`.

> *Ghi chú:* mục này dựng lại từ ngữ cảnh, chưa đủ chi tiết như mẫu chuẩn. Kỳ sau ghi ngay trong phiên.
