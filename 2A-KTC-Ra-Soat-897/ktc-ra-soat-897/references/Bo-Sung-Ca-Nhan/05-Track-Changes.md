# 05 – Track Changes khi sửa trực tiếp tệp .docx

**Nguồn:** `20-Chuan-Chung/15-Skill-Track-Changes.md` của dự án KTC-Quan-tri (ban hành 13/9/2026; thi hành Nguyên tắc 7–10 trong `20-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`, NT-2); công cụ `29-Cong-Cu/ktc_trackchanges.py`. Không lấy từ v2.25.
**Phạm vi:** **chỉ khi người dùng yêu cầu sửa trực tiếp tệp** dự thảo (hoặc tác vụ (d) chuẩn hóa văn phong trên tệp Word đã có). Rà soát chỉ xuất báo cáo thì **không** dùng và không giả lập Track Changes vào dự thảo.
*Ghi chú tham khảo — không thay đổi mã, mức, nhãn của v4.5.*

v4.5 không có bước sửa tệp. Mô-đun này không thay đổi Bước 0–7 và không tạo phát hiện; nó chỉ nhắc cách sửa khi người dùng đã yêu cầu sửa.

## Nguyên tắc

1. Xuất phát từ **chính tệp gốc** người dùng gửi. Không soạn lại rồi trình bày như bản sửa. Không có tệp gốc → dừng và hỏi.
2. Mọi thay đổi để lại dấu vết (xóa / thay / bổ sung) trong Word; mỗi đợt sửa có tính chất riêng dùng `w:author` riêng.
3. Chạy kiểm tra cấu trúc (`kiem_tra`) và đối chiếu bản sửa với bản gốc (`doi_chieu_goc`) trước khi giao.
4. Tệp ra ghi ở thư mục kết quả với hậu tố phân biệt, **không ghi đè** tệp gốc.

## Điều kiện nền tảng

Công cụ cần `python-docx` và `lxml`, chạy trên Claude Code trong dự án KTC-Quan-tri. Môi trường không chạy được (Chat, Cowork không có `29-Cong-Cu/`) → nói thẳng là không thi hành được; **không** mô tả suông rồi giao tệp sửa trắng.

## Quy trình, API, danh sách lỗi `kiem_tra`

Xem toàn văn `20-Chuan-Chung/15-Skill-Track-Changes.md` (bản gốc duy nhất; không chép lại ở đây để không lệch). Bài kỹ thuật chuẩn hóa Track Changes: `Bo-Sung-Chuan-Hoa-TrackChanges-MauChu-PhienBanSkill_20260825.md` của gói v2.25 (lưu ngoài gói này).

## Quan hệ với báo cáo rà soát

Việc sửa theo kiến nghị của báo cáo là việc **sau** Bước 7, do người dùng yêu cầu. Bản sửa không thay đổi nhãn đã gán cho bản dự thảo cũ; muốn gán nhãn cho bản mới phải rà soát lại (chế độ ĐC, Bước 5).
