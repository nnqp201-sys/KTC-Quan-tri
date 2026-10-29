# Bài học và đề xuất từ phiên làm việc Đề án Trung tâm Đăng kiểm (21/10 - 27/10/2026)

Phạm vi:
- Đề án thành lập Trung tâm Đăng kiểm xe cơ giới trực thuộc Trường (lần 5, lần 6), kèm Tờ trình, dự thảo QĐ UBND, Báo cáo tiếp thu giải trình và CV đề nghị xin ý kiến Bộ.
- 3 vòng thẩm định AI độc lập và rà soát 897 chính thức (24/10).
- BC 498/BC-CĐKT và CV 775/CĐKT-THHCQT đã ký (27/10).
- CV báo cáo rà soát NĐ 373 theo CV 10900/UBND-KTTH.

Trạng thái: **đề xuất, chưa kích hoạt**. Bộ này đi song song với bộ `De-xuat-dau-tu-cong` và dùng chung agent `ktc-kiem-nhat-quan-bo-van-ban`.

## 1. Chuỗi việc của một Đề án trình UBND tỉnh (đã chạy thật)

| Bước | Văn bản/việc | Ghi chú |
|---|---|---|
| 1 | Dự thảo Đề án + Tờ trình + dự thảo QĐ UBND | Ba văn bản phải khớp nhau đến từng con số. |
| 2 | Lấy ý kiến sở, ngành | STP 2533 và STC 8766 đều nêu: chưa có hướng dẫn của Bộ. |
| 3 | Báo cáo tiếp thu, giải trình (bảng ý kiến - tiếp thu - vị trí sửa) | Mỗi dòng trỏ được tới mục/trang cụ thể của Đề án. |
| 4 | Thẩm định độc lập (nhiều hệ AI, nhiều vòng) | Gửi **bản sạch**. Ý kiến AI không mặc nhiên đúng. |
| 5 | Rà soát 897 chính thức | Chỉ trình khi không còn vấn đề Mức 1. |
| 6 | Văn bản xin ý kiến cấp trên (BC 498, CV 775) | Sau khi ký, bản PDF đã ký là nguồn sự thật; không sửa nữa. |
| 7 | Văn bản khác phát sinh cùng lĩnh vực (CV 10900 về NĐ 373) | Phải đối chiếu với Đề án đang trình để tránh mâu thuẫn. |

## 2. Lỗi/vướng đã xảy ra và nguyên nhân gốc

| # | Việc đã xảy ra | Nguyên nhân gốc | Cách chặn |
|---|---|---|---|
| 1 | AI thẩm định báo "thiếu nội dung" trong khi bản Track Changes đã có. | Công cụ đọc `p.text` của python-docx bỏ qua chữ nằm trong `w:ins`. | Rule: luôn gửi thẩm định bản sạch (`accept_all`), tên tệp có hậu tố `_ban-sach`. |
| 2 | Câu nêu giá thừa, lạc ngữ cảnh (anh phát hiện). | Sửa cục bộ theo từng ý kiến, không đọc lại cả đoạn. | Agent tài chính kiểm "mỗi con số chỉ định nghĩa một chỗ". Đọc lại cả đoạn sau mỗi lần sửa. |
| 3 | Báo cáo tiếp thu dựng theo thể thức của Trường, trong khi đúng ra là của Tổ xây dựng Đề án. | Không xác định chủ thể ban hành trước khi dựng. | Bước 0 của skill: ghi chủ thể ban hành, người ký, nơi nhận. |
| 4 | Kính gửi sai kỹ thuật trình bày (thụt lề chép từ BC khổ ngang). | Chép định dạng từ văn bản tương đồng nhưng khác khổ giấy. | Ghi cố định thông số Kính gửi khổ dọc trong rule (4,0 cm / 6,5 cm). |
| 5 | Căn cứ khấu hao chưa chuẩn (lẫn TT 45/2013 với NĐ 178, TT 151). | Không tách tài sản doanh nghiệp với tài sản công của ĐVSNCL. | Bảng căn cứ tài chính trong rule 24. |
| 6 | Thiếu dữ liệu: Tổ trưởng, nhân sự đăng kiểm viên, số thu. | — | Hỏi anh ngay, không ghi "chuyển đơn vị khác". Cách làm này đã đúng, giữ nguyên. |
| 7 | Tệp trong kho đặt sai tên (NĐ 165/2026 ghi "phòng bệnh"). | Metadata kho sai. | Đọc nội dung thay vì dựa vào tên tệp; viết đề xuất sửa kho vào 30-Ket-Qua. |
| 8 | Bản docx của BC 498 khác bản PDF đã ký (ngày, nơi nhận). | Anh sửa lúc trình ký, docx không được cập nhật theo. | Sau khi ký: lấy PDF làm nguồn, cập nhật tệp yaml. |
| 9 | CV 10900 (không chuyển đổi thành DN) và Đề án (góp vốn lập DN) dễ bị hiểu là mâu thuẫn. | Hai luồng việc do hai người soạn. | Agent điều phối kiểm mỗi văn bản mới đến có chạm Đề án đang mở không. |
| 10 | Phải sửa hàng chục chỗ "viết hoa sau dấu :" ở vòng 897. | Không kiểm ngay khi đang viết. | Thêm phép kiểm vào `kiem_the_thuc.py` (cảnh báo Mức 3). |
| 11 | Tên phiên bản rối (Đề án lần 6 - v5/v6, QĐ lần 5, BC v7/v8). | Số vòng xin ý kiến bị lẫn với số bản sửa. | Quy ước: `lan-N` là vòng gửi sở ngành, `vM` là bản sửa nội bộ; ghi trong yaml. |
| 12 | Trang trắng cuối, khối chữ ký bị tách sang trang sau. | Có đoạn trống cuối văn bản, thiếu keep-with-next. | Giữ bước xem PDF; thêm phép kiểm tự động trong `kiem_the_thuc.py`. |
| 13 | Track Changes: neo vào chữ vừa chèn thì không tìm thấy; công cụ tìm thân bài trước rồi mới tìm bảng. | Hành vi của `tc_lib`. | Ghi vào `15-Skill-Track-Changes.md`; chuyển `tc_lib`, `accept_all` từ scratchpad vào `29-Cong-Cu/`. |
| 14 | 897 báo giả TT08/TT17 (văn bản của UBND) và VD06 (căn cứ QĐ). | Quy tắc chưa phân biệt chủ thể ban hành. | Ghi danh sách báo giả đã biết trong rule 24. |

## 3. Đề xuất thành phần

| Thành phần | Tệp | Việc |
|---|---|---|
| Skill | `skill-ktc-de-an/SKILL.md` | Quy trình 9 bước (0–8) để soạn, sửa và trình một Đề án. |
| Rule | `rules/24-de-an.md` | Các quy ước cứng: bản sạch, chủ thể ban hành, căn cứ tài chính, phiên bản, báo giả. |
| Dữ liệu sự thật | `du-lieu/de-an_Dang-kiem-XCG.yaml` | Mọi con số, số hiệu và trạng thái của Đề án, gom về một nguồn. |
| Agent 1 | `ktc-de-an-dieu-phoi` | Cho biết bước đã xong, bước kế tiếp; xét văn bản mới đến có chạm Đề án không. |
| Agent 2 | `ktc-tiep-nhan-tham-dinh` | Gộp nhiều báo cáo thẩm định, phân loại Tiếp thu/Giải trình/Không tiếp thu, kèm căn cứ. |
| Agent 3 | `ktc-kiem-tai-chinh-de-an` | Tính lại bảng tài chính, đối chiếu với yaml và cả bộ hồ sơ. |
| Dùng lại | `ktc-kiem-nhat-quan-bo-van-ban` | Đối chiếu Đề án, Tờ trình, QĐ và BC tiếp thu. |
| Script | `29-Cong-Cu/tc_lib.py`, `accept_all.py` | Chuyển từ scratchpad vào dự án, kèm kiểm thử. |

## 4. Kích hoạt (sau khi anh duyệt)

1. Chép `agents/*.md` vào `.claude/agents/` và `rules/24-de-an.md` vào `.claude/rules/`. Skill đặt vào `.claude/skills/ktc-de-an/`.
2. Chép `du-lieu/de-an_Dang-kiem-XCG.yaml` vào `29-Cong-Cu/de_an/`, rồi anh soát lại số liệu.
3. Chuyển `tc_lib.py` và `v3.accept_all` vào `29-Cong-Cu/`; thêm 2 phép kiểm (viết hoa sau dấu ":", trang trắng/khối ký) vào `kiem_the_thuc.py`.
4. Chạy `python 29-Cong-Cu/kiem_tra_he_thong.py`. Thử agent 2 trên 4 báo cáo AI vòng 3 và agent 1 trên CV 10900 để đối chứng.
