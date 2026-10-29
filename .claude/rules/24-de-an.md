---
paths: ["**/*De-an*", "**/DA_*", "**/de_an/**"]
---
# Quy ước Đề án trình cấp trên

1. **Nguồn sự thật**: `29-Cong-Cu/de_an/de-an_<ten>.yaml`. Số liệu trong văn bản lấy từ tệp này; cần sửa số thì sửa yaml trước.
2. **Chủ thể ban hành** phải ghi trước khi dựng văn bản, gồm 3 trường hợp:
   - Trường: Hiệu trưởng ký.
   - Tổ xây dựng Đề án: Tổ trưởng ký.
   - Dự thảo văn bản của UBND tỉnh: không dùng ký hiệu của Trường, không áp TT08/TT17.
3. **Gửi thẩm định (AI hoặc người) luôn dùng bản sạch** đã accept Track Changes. Bản Track Changes chỉ dành cho người duyệt xem.
4. Ý kiến thẩm định không mặc nhiên đúng. Mỗi ý phải có kết luận Tiếp thu / Giải trình / Không tiếp thu, kèm căn cứ.
5. **Căn cứ tài chính** tách theo chế độ tài sản:
   - Tài sản của doanh nghiệp góp vốn: TT 45/2013/TT-BTC (còn hiệu lực theo QĐ 1760/QĐ-BTC ngày 01/7/2026).
   - Tài sản công của ĐVSNCL: NĐ 178, TT 151.
   - Không dùng lẫn hai chế độ.
6. ĐVSNCL góp vốn lập DN **không phải** là chuyển đổi theo NĐ 373/2026. Mọi văn bản về NĐ 373 đều phải phân định rõ điểm này.
7. **Phiên bản**: `lan-N` là vòng gửi lấy ý kiến; `vM` là bản sửa nội bộ. Với văn bản đã ký, bản PDF đã ký là nguồn; không sửa lại docx.
8. Kính gửi khổ dọc: dòng "Kính gửi:" thụt đầu dòng 4,0 cm; các dòng "- ..." lề trái 6,5 cm.
9. Báo giả 897 đã biết:
   - TT08/TT17 trên dự thảo văn bản của UBND.
   - VD06 trên phần căn cứ của QĐ, khi căn cứ kết thúc bằng ";" ngay trước "Theo đề nghị".
10. Mỗi con số chỉ định nghĩa một lần trong Đề án. Chỗ khác dẫn lại chỗ đó, không nhắc lại kèm diễn giải mới.
11. **Đề án nội bộ** (`cap: noi-bo` trong yaml, ví dụ Hạng A): Hiệu trưởng phê duyệt (điểm a khoản 7 Điều 7 NĐ 334/2026). Không có dự thảo văn bản UBND tỉnh; các văn bản do Tổ hoặc Trường ban hành.
12. **Mẫu gốc theo văn bản** — dùng văn bản gốc, không dùng mẫu trống khi đã có:

    | Văn bản | Chủ thể | Phát triển từ | Ký, lưu |
    |---|---|---|---|
    | BC tiếp thu, giải trình | Tổ xây dựng Đề án | BC 344/BC-CĐKT (kho 05, Đề án Đăng kiểm lần 3; bảng 3 cột TT · Nội dung ý kiến · Nội dung tiếp thu, giải trình) | TM. Tổ – Tổ trưởng; "Lưu: VT, Tổ XDĐA." |
    | Biên bản họp góp ý | Trường | mẫu `09-Bien-ban.dotx` | Thư ký + Chủ trì |
    | Tờ trình | theo yaml | Tờ trình Đề án đã ban hành, sau đó mẫu `07-To-trinh.dotx` | theo yaml |

    Khi đổi tên cơ quan ban hành, đường kẻ dưới tên phải là **hình vẽ đường thẳng** (như trong mẫu), không dùng viền đoạn: người dùng không sửa được viền đoạn.
13. **Mỗi cuộc họp góp ý sinh trọn bộ**: Biên bản + BC tiếp thu của Tổ, lấy từ cùng một bảng ý kiến (skill `ktc-cuoc-hop`). Kết luận của chủ trì là một nhóm riêng trong BC tiếp thu.
14. **Bản tóm tắt cuộc họp do AI khác lập là dữ liệu cần kiểm, không phải nguồn.** Phải đối chiếu với ghi âm, ghi chép và chính văn bản (bảng số liệu, Tờ trình) trước khi dùng.
