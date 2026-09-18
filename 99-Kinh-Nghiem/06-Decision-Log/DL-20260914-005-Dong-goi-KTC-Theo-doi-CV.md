# DL-20260914-005 — Đóng gói `ktc-theo-doi-cv` v1.0

**Ngày:** 14/9/2026 · **Loại:** APPLY

## Bối cảnh

`KTC-Theo-doi-CV` là hệ duy nhất trong năm hệ **chưa có `SKILL.md` và chưa có gói `.skill`** — nên chưa
chạy được trên Claude Chat/Cowork, dù nó là mắt xích giữa Kế hoạch và Báo cáo. Chính `00-README.md` của
hệ đã ghi việc này ở mục "Việc cần làm tiếp", số 3.

## Quyết định

Đóng gói `ktc-theo-doi-cv-v1.0.skill` — 10 tệp, dựng **hoàn toàn từ chuẩn đã có**, không phát minh thêm:

| Nguồn | Dùng để |
|---|---|
| `01-Chuan-Chung/12-Vong-Doi-Trang-Thai.md` | 7 trạng thái chính, 5 trạng thái phụ, 8 cảnh báo |
| `01-Chuan-Chung/11-Quy-Tac-Task-ID.md` | Quy tắc cấp và dùng Task_ID |
| 19+11+10+14 cột của `01. Bộ dữ liệu vận hành` | Trường bắt buộc của từng skill |
| `KTC-Theo-doi-CV/00-README.md` | Vai trò, quyền ghi nhóm F/G, chốt chặn 897 |

**Năm skill:** 40 Tiếp nhận · 41 Cập nhật tiến độ · 42 Cảnh báo · 43 Minh chứng ·
44 Điều chỉnh và bàn giao. Kèm quy trình 6 bước.

## Ba điều cố ý viết vào skill

1. **Hệ không sinh nhiệm vụ.** Gặp việc chưa có trong kế hoạch thì ghi đủ 7 trường phát sinh rồi trả về
   `ktc-ke-hoach` cấp mã — không tự thêm. Đây là nguyên tắc bất biến 2.
2. **Khóa baseline.** `Hạn baseline` và `Hạn hiện hành` tách riêng; chênh lệch giữa hai cột chính là số
   lần trượt tiến độ. Mất baseline là mất khả năng nói "việc này đã lùi hạn mấy lần".
3. **Tự khai độ tin cậy.** Bộ dữ liệu vận hành đang **rỗng** (0 dòng ở cả 4 bảng), nên mọi kết quả của hệ
   hiện là **dữ liệu mẫu**. Skill bắt buộc ghi rõ điều đó ở đầu kết quả — nếu không, người đọc sẽ tưởng
   đó là số thật.

## Chống lặp lại lỗi đã biết

Skill 42 (Cảnh báo) có một mục riêng về **chống nhiễu**, dẫn `BUG-07` của hệ Báo cáo: cảnh báo giả lặp
lại khiến người nhận bỏ qua cả cảnh báo thật. Quy tắc đặt ra: điều kiện cảnh báo mới phải thử trên dữ
liệu thật, **báo nhầm > 20% thì không đưa vào**.

Skill 43 (Minh chứng) dẫn tiền lệ nhiệm vụ 2.8 — hoàn thành thật bằng QĐ 1923/QĐ-CĐKT nhưng không xuất
hiện trong báo cáo đơn vị: *"không tìm thấy minh chứng" không đồng nghĩa "chưa làm"*.

Skill 44 dẫn `KI-001`: khớp theo tên sinh khớp giả ở ngưỡng 63–80%, **không dùng ngưỡng dưới 100% cho
kết luận tự động**.

## Việc chưa làm

Quy trình 6 bước **chưa chạy thử trên dữ liệu thật** — vì chưa có dữ liệu. Đây là việc chặn: nạp nhiệm vụ
thật vào bộ dữ liệu vận hành trước, rồi mới chạy thử và ghi Process Memory.

**Liên quan:** `DL-20260914-004` · `KTC-Theo-doi-CV/00-README.md` · `01-Chuan-Chung/12-Vong-Doi-Trang-Thai.md`
