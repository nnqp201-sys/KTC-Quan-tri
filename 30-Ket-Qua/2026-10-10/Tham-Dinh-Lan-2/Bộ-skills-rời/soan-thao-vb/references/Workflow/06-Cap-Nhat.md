# 06-Cap-Nhat — Cập nhật bộ quy tắc của hệ

**Viết lại 14/9/2026.**

## Mục đích
Đưa bài học từ vận hành thật vào đúng tệp quy tắc, để lỗi đã mắc không lặp lại.

## Bước 1 — Ghi nhận sự việc, không ghi cảm nhận
Ghi: làm gì · đầu vào nào · kết quả sai ở đâu · phát hiện bằng cách nào. Phân biệt rõ **ĐÃ XÁC MINH** và
**CHƯA XÁC MINH**. Ghi cả lý do, không chỉ ghi kết luận.

## Bước 2 — Xác định đúng tầng sửa

| Hiện tượng | Sửa ở |
|---|---|
| Câu lệnh cho một loại văn bản chưa đủ rõ | `Prompt-Library/` |
| Quy tắc nghiệp vụ sai hoặc thiếu | `Skill-Library/` |
| Thứ tự các bước sai, thiếu chốt chặn | `Workflow/` |
| Quy tắc dùng chung cho nhiều hệ | **`20-Chuan-Chung/` của KTC-Quan-tri** — không sửa riêng ở hệ này |

**Sai tầng là nguyên nhân gốc của việc lệch giữa các hệ.** Sửa một quy tắc dùng chung ở riêng một hệ sẽ làm
hệ đó lệch với bốn hệ còn lại.

## Bước 3 — Không sao chép quy tắc của hệ khác
Cần quy tắc rà soát thì **trỏ tới** `KTC-Ra-Soat-897`, không chép sang đây. Bản sao không có cơ chế đồng bộ
**chắc chắn sẽ lệch**, và bản lệch nguy hiểm hơn bản thiếu vì nó trông như có.

*Tiền lệ:* hệ `KTC-DIS-Tong-Hop-VB` từng chép bộ checklist của 897. Sau một tháng, **28/28** tệp đều tụt lại
sau bản gốc — trong đó `03-Phap-Ly.md` chỉ còn **357 byte** so với **10.513 byte** của bản gốc. Chính vì lỗi
này mà hệ đó phải thu hẹp thành hệ soạn thảo (xem `DL-20260914-001`).

**Ngoại lệ duy nhất:** 5 tệp dùng chung bắt buộc nhân bản vào `references/Skill-Library/` vì `.skill` là zip
tự chứa. Với chúng, bản gốc ở `20-Chuan-Chung/` và nhân bản lại **tại bước đóng gói**.

## Bước 4 — Ghi phiên bản và ngày
Mọi tệp sửa phải có dòng phiên bản. Ghi rõ sửa gì, vì sao — nêu bằng chứng đo được nếu có.

## Bước 5 — Đóng gói lại và kiểm
`.skill` là zip đã đóng; sửa nguồn rời **không** tự động cập nhật gói.

⚠️ **Nguồn rời và nội dung trong gói KHÔNG mặc nhiên đồng bộ — gói có thể MỚI HƠN.** Trước khi đóng gói phải
so từng tệp; tệp nào trong gói mới hơn thì **gộp**, không ghi đè. Dùng `KTC-Quan-tri/tools/dong_goi_skill.py`
— kiểm frontmatter, kiểm liên kết gãy, và đối chiếu danh sách tệp trước/sau.

## Bước 6 — Chạy lại ca đã sai
Bài học chỉ được coi là đã tiếp thu khi **chạy lại đúng ca từng sai** và kết quả đã đúng.

## Đầu ra
Tệp quy tắc đã sửa (có phiên bản) · ghi chú thay đổi · gói `.skill` đóng lại và đã kiểm · kết quả chạy lại.
