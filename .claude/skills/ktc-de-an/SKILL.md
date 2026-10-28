---
name: ktc-de-an
description: Soạn, sửa, tiếp thu ý kiến thẩm định và trình bộ hồ sơ Đề án của Trường Cao đẳng Kon Tum — Đề án trình UBND tỉnh và Đề án nội bộ do Hiệu trưởng phê duyệt — gồm Đề án, Tờ trình, dự thảo QĐ, Báo cáo tiếp thu giải trình của Tổ xây dựng Đề án, biên bản họp góp ý và văn bản xin ý kiến Bộ. Dùng khi người dùng nhắc "Đề án", "tiếp thu ý kiến", "thẩm định độc lập", "báo cáo giải trình", "trình lại Đề án".
---
# Quy trình

0. Đọc `.claude/rules/24-de-an.md` và `29-Cong-Cu/de_an/de-an_<ten>.yaml`. Xác định `cap` (tinh/noi-bo), chủ thể ban hành, người ký, nơi nhận và mẫu gốc của từng văn bản (rule 24 mục 12). Thiếu dữ liệu thì hỏi anh ngay.
1. Phát triển từ bản hiện hành (Nguyên tắc 7). Sửa bằng Track Changes (`29-Cong-Cu/tc_lib.py`) và xuất kèm bản sạch.
2. Khi nhận ý kiến thẩm định: giao agent `ktc-tiep-nhan-tham-dinh` phân loại, rồi trình anh duyệt các ý cần quyết.
3. Cập nhật yaml trước, sau đó áp sửa vào cả bộ cùng lúc (Đề án, Tờ trình, QĐ, BC tiếp thu).
4. Chạy agent `ktc-kiem-tai-chinh-de-an` và `ktc-kiem-nhat-quan-bo-van-ban` trên bản sạch.
5. Chạy `kiem_the_thuc.py` và `kiem_vien_dan.py`. Xem PDF từng trang, chú ý trang trắng và khối chữ ký.
6. Rà soát 897 chính thức. Chỉ trình khi không còn vấn đề Mức 1.
7. Sau khi ký: cập nhật yaml (số, ngày, nguồn PDF), tri thức chuyên đề và MEMORY. Không sửa văn bản đã phát hành.
8. Sau cuộc họp góp ý (ghi âm, ghi chép, tóm tắt của AI khác): dùng skill `ktc-cuoc-hop` để lập bảng ý kiến, sau đó sinh Biên bản và BC tiếp thu của Tổ cùng lúc.
9. Khi có văn bản mới đến cùng lĩnh vực: giao agent `ktc-de-an-dieu-phoi` xét cần phân định gì.
