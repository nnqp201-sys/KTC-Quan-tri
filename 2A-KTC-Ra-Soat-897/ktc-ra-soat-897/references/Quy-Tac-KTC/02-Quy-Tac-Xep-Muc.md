# 02 – Quy tắc xếp mức và gán nhãn kết luận cố định (v4.5, 27/10/2026)

Mục đích: cùng một hồ sơ, mọi lần chạy, mọi tài khoản phải cho **cùng mức** cho cùng một phát hiện và **cùng nhãn** kết luận. Người rà soát (AI) **không tự chọn mức** ngoài bảng này.

## 1. Thang 4 mức
- **Mức 1 – Bắt buộc sửa**: trái pháp luật hoặc văn bản cấp trên; viện dẫn sai hoặc văn bản hết hiệu lực/bị thay thế; sai thẩm quyền; sai căn cứ ban hành; thiếu điều khoản bắt buộc; mâu thuẫn làm thay đổi nội dung quy phạm.
- **Mức 2 – Cần sửa**: sai thể thức, kỹ thuật trình bày theo bảng thông số KTC; sai logic; sai viện dẫn nội bộ; thiếu thống nhất trong văn bản; lệch (mâu thuẫn, hẹp hơn/chặt hơn, rộng hơn) với văn bản đang có hiệu lực của Trường cùng chủ đề; sai tên đơn vị, tên cơ sở, tên tổ chức đảng.
- **Mức 3 – Nên sửa**: văn phong, câu chữ, cách diễn đạt, khả năng đọc hiểu; lỗi kỹ thuật soạn thảo không làm sai hiển thị (đoạn trống thay ngắt trang, số trang đặt cứng nhưng hiển thị đúng).
- **Mức 4 – Góp ý nâng cao**: đề xuất hoàn thiện, không bắt buộc; thuộc tính tệp.

## 2. Bảng mã → mức (bắt buộc dùng)
| Nhóm mã | Nội dung | Mức cố định | Ghi chú |
|---|---|---|---|
| TT-01 … TT-51 | Thể thức, kỹ thuật trình bày đo bằng script (trừ hai ngoại lệ bên dưới); văn bản Đảng đo theo bảng 01 mục B | **Mức 2** | theo `01-Bang-Thong-So-The-Thuc-KTC.md` |
| TT-46 | Văn bản Đảng: thiếu chỉ dẫn phụ lục dưới tiêu đề phụ lục | **Mức 2** | HD 05 Phần II mục 1.2 |
| TT-24 | Lời văn dài hơn một dòng không dàn đều hai lề (v4.2; phạm vi theo quyết định D2 ngày 27/10/2026) | **Mức 2** | TB 597 mục 6; văn bản Đảng: HD 05 Phần II mục 6.2.2 |
| TT-34 (cách thiết lập) | Số trang văn bản kèm theo đặt cứng `start = N` nhưng **hiển thị đúng** số liên tục | Mức 3 | hiển thị sai → Mức 2 |
| TB-01 | ≥ 5 đoạn trống liên tiếp (dùng Enter thay ngắt trang/section) | Mức 3 | |
| TB-03 | Dấu câu cuối căn cứ | Mức 3 | |
| TB-02 | Thuộc tính tệp (Title còn tên cơ quan cũ) | Mức 4 | |
| TD-01 | Viết sai tên đơn vị, tổ chức (Ban Truyền thông, Ban Văn – Thể – Mỹ, Tổ Quản trị hệ thống thông tin, Phòng khám Đa khoa, Nhà thuốc Phòng khám Đa khoa, Hội Sinh viên, Đoàn Thanh niên…) | **Mức 2** | TB 597 mục 3.1.c; QĐ 1355 Điều 2 |
| TD-02 | Viết hoa “Phòng/Khoa/Bộ môn” giữa câu khi chỉ đơn vị của Trường | **Mức 2** | TB 597 mục 3.1.c |
| TD-05 | “phụ lục I” viết thường khi gắn số | **Mức 2** | Chỉ đạo 26/10/2026 |
| TD-06 | Sai tên, địa chỉ cơ sở (Trụ sở chính, Cơ sở 2…5) | **Mức 2** | QĐ 1355 Điều 1, 2 |
| TD-07 | Liệt kê tên đơn vị trong một đoạn dùng “;” thay “,” | Mức 3 | TB 597 mục 3.1.c |
| TD-03, TD-04 | “Nhà trường” viết hoa giữa câu; “đảm bảo” thay “bảo đảm” | Mức 3 | văn phong |
| CC-01 | Căn cứ/viện dẫn văn bản đã hết hiệu lực hoặc bị thay thế | **Mức 1** | danh sách tại `kho_manifest.json` |
| CC-02 | Luật/pháp lệnh đã sửa đổi, đã có VBHN nhưng không viện dẫn theo VBHN mới nhất | **Mức 2** | `04-Vien-Dan-Van-Ban-Hop-Nhat.md` |
| CC-03 | Viện dẫn sai số, ký hiệu, ngày, cơ quan ban hành, trích yếu của văn bản được dẫn | **Mức 1** | phải có nguyên văn văn bản được dẫn |
| CC-04 | Trích dẫn sai nội dung điều, khoản của văn bản được dẫn | **Mức 1** | phải có nguyên văn hai phía |
| CC-05 | Căn cứ thừa, không liên quan, hoặc thiếu căn cứ thẩm quyền | Mức 2 (thiếu căn cứ thẩm quyền: Mức 1) | |
| CC-06 | Văn bản hành chính: căn cứ là Luật/Pháp lệnh có ghi số, ký hiệu (mẫu của Trường không ghi) | **Mức 2** | NĐ 30 PL I Phần II mục 6.a; TB 597 mục 6; quyết định của Hiệu trưởng 26/10/2026 điểm 1 |
| TQ-01 | Sai thẩm quyền ban hành/ký (QĐ 1976 Điều 21–22; QĐ 2073 Điều 6 k3, Điều 19) | **Mức 1** | |
| TQ-02 | Giao nhiệm vụ cho đơn vị không có chức năng đó theo quyết định chức năng, nhiệm vụ (QĐ 2041…2054, 794, 969, 1997, 101) | **Mức 2** | |
| DC-01 | Ma trận: **Mâu thuẫn** với văn bản của Trường đang có hiệu lực | **Mức 2** | Mức 1 nếu trái pháp luật/văn bản cấp trên |
| DC-02 | Ma trận: **Hẹp hơn** (chặt hơn) văn bản đã ban hành của Trường, kể cả chặt hơn QĐ 2307 | **Mức 2** | trả lời điểm 4 ngày 26/10/2026 |
| DC-03 | Ma trận: **Rộng hơn** văn bản đã ban hành của Trường | **Mức 2** | Mức 1 nếu rộng hơn pháp luật cho phép |
| DC-04 | Thuật ngữ định nghĩa khác văn bản của Trường cùng chủ đề | Mức 2 | |
| DC-05 | Thiếu cơ chế thực hiện cho quy định đã đặt ra (không có đơn vị chủ trì, thời hạn, biểu mẫu) | Mức 2 | |
| DC-06 | Dự thảo dùng mức, nhóm, tên phân loại không có trong văn bản liên quan cùng chủ đề (ví dụ mức phân loại tài liệu khác Danh mục QĐ 2307) | Mức 2 | B2 đề xuất 3 (M2-5 của V1) |
| ND-01 | Sai logic, mâu thuẫn nội tại giữa các điều, khoản của dự thảo | Mức 2 | Mức 1 nếu làm thay đổi nội dung quy phạm |
| ND-02 | Thiếu điều khoản bắt buộc (hiệu lực, trách nhiệm thi hành, thay thế văn bản cũ…) | **Mức 1** | |
| ND-03 | Đánh số điều, khoản, điểm sai; viện dẫn nội bộ sai | Mức 2 | |
| VP-01 | Văn phong, câu chữ, chính tả, dấu câu | Mức 3 | lỗi chính tả làm sai nghĩa: Mức 2 |
| GY-01 | Góp ý nâng cao | Mức 4 | |
| DG-01 | Văn bản Đảng: sai tên cấp tổ chức đảng (Đảng bộ Trường là **đảng bộ trực thuộc cơ sở**; đầu văn bản theo mẫu Phụ lục TB 597) | **Mức 2** | không hỏi lại người dùng |
| DG-02 | Văn bản Đảng: áp thể thức hành chính (NĐ 30) cho văn bản Đảng | Mức 2 | |

Mã TD-06, TD-07, CC-03…CC-05, TQ, DC, ND, VP, GY, DG do người rà soát gán khi đọc nội dung; mã TT, TB, TD-01…05, CC-01, CC-02, CC-06 do script phát hiện và người rà soát **giữ nguyên mức**. CC-02 chỉ có khi đã biết VBHN (Kho hoặc hồ sơ); chưa biết thì script ghi “chưa kiểm”.

## 3. Quy tắc bằng chứng gắn với mức
1. Mức 1 và Mức 2 chỉ được ghi khi có **bằng chứng hai phía**: (a) nguyên văn hoặc thông số đo của dự thảo, và (b) nguyên văn văn bản căn cứ (hoặc dòng trong bảng thông số KTC). Thiếu một phía → không được ghi lỗi; ghi “Chưa kiểm – lý do” ở Phần I.8.
2. Suy luận, phỏng đoán, trí nhớ không phải bằng chứng.
3. Script báo “chưa kiểm” → không ghi Đạt, không ghi lỗi.
4. Không hạ mức để đạt nhãn tốt hơn; không nâng mức ngoài bảng.
5. Một vấn đề = một dòng ở Phần II (gộp các vị trí cùng lỗi vào ô Vị trí); không tách một lỗi thành nhiều dòng để tăng số đếm, không gộp hai lỗi khác mã vào một dòng.

## 4. Ma trận đối chiếu chéo – chỉ 6 giá trị
| Giá trị | Nghĩa | Điều kiện ghi |
|---|---|---|
| Khớp | cùng **chủ thể, hành vi, mức/thời hạn** (không phải chỉ trùng từ khóa) | nguyên văn hai phía trong ngoặc kép “…” + trường `yeu_to_khop` dạng `{chu_the, hanh_vi, muc_thoi_han}`, mỗi yếu tố trích hai phía trong ngoặc kép (ghi “trùng từ khóa”, “tương tự” hoặc không trích hai phía bị script từ chối); vị trí đã có phát hiện ở Phần II – kể cả vị trí cha/con (“Điều 7” và “Điều 7 khoản 2”) – thì không được ghi Khớp hay Đạt. v4.4–v4.5 (PB4-GPT-07, PB5-GPT-03, PB5-WORK-15): script so hai phía từng yếu tố theo **dãy (số, đơn vị) THEO THỨ TỰ** (bỏ số dẫn Điều/khoản/điểm/Chương/Mục/Phụ lục/số hiệu và năm; “năm ngày” = 5 ngày), **phủ định theo từng vế** (không/chưa/chẳng/cấm/thiếu) và cặp trái nghĩa (cấm/cho phép, bắt buộc/khuyến khích, tối đa/tối thiểu, tăng/giảm); có khác biệt → từ chối Khớp, trừ khi dòng có `giai_trinh_khop` {<yếu tố>: lý do ≥ 20 ký tự} – giải trình in ở Bảng 3 để người ký xem lại (**quyết định F2** ngày 27/10/2026). Script chỉ bắt dấu hiệu bề mặt; AI vẫn phải đọc nghĩa hai phía |
| Mâu thuẫn | hai bên quy định trái nhau | nguyên văn hai phía → DC-01 (trường `ma_phat_hien` phải là DC-01, Mức 1–2; phát hiện DC-01 phải đặt **cùng vị trí hoặc vị trí cha – con** với dòng ma trận – v4.4, PB4-GPT-06, PB4-WORK-10; quy tắc vị trí này áp cả Hẹp hơn, Rộng hơn; v4.5 (PB5-WORK-14): vị trí ghi tên tệp thì phải **cùng tệp**; tác vụ so sánh hai bản: dòng ma trận phải ghi tên tệp như cổng hồ sơ ghi, ví dụ “Du thao_V2.docx – Điều 7 khoản 2”) |
| Hẹp hơn | dự thảo chặt hơn: phạm vi cho phép hẹp hơn, điều kiện nhiều hơn, thời hạn ngắn hơn | nguyên văn hai phía → DC-02 (`ma_phat_hien` = DC-02) |
| Rộng hơn | dự thảo lỏng hơn | nguyên văn hai phía → DC-03 (`ma_phat_hien` = DC-03) |
| Văn bản liên quan không quy định | đã đọc toàn văn, không có nội dung cùng chủ đề | ghi rõ đã tìm theo từ khóa nào |
| Chưa kiểm (lý do) | chưa mở được nguyên văn | chỉ hợp lệ khi cổng đã ĐỦ mà vẫn không tìm được điều khoản; ghi vào I.8 |

Ngoại lệ: dự thảo nêu rõ thay thế/sửa đổi văn bản kia và đúng thẩm quyền → “Khớp – có điều khoản thay thế” kèm nguyên văn điều khoản thay thế (trường `nguyen_van_thay_the`, trong ngoặc kép; không cần `yeu_to_khop` – v4.5).

## 5. Nhãn kết luận – 4 nhãn cho dự thảo (áp theo thứ tự, dừng ở dòng đầu tiên thỏa)
| Thứ tự | Điều kiện | Nhãn |
|---|---|---|
| 1 | Số Mức 1 ≥ 1 | **Chưa đủ điều kiện ban hành** |
| 2 | Số Mức 2 ≥ 1, hoặc ma trận còn “Chưa kiểm” ở chủ đề trọng yếu (thẩm quyền, thời hạn, điều cấm/cho phép, đối tượng, hiệu lực) | **Cần chỉnh sửa trước khi trình ký** |
| 3 | Số Mức 3 ≥ 1 | **Có thể ban hành sau khi chỉnh sửa nhỏ** |
| 4 | Còn lại (0 Mức 1, 0 Mức 2, 0 Mức 3) | **Có thể ban hành ngay** |

- Tác vụ (b) rà soát nhanh và (c) so sánh hai bản (`kieu_bao_cao` = `nhanh` / `so_sanh`): **không gán nhãn trình ký**; script ghi “Rà soát nhanh – không gán nhãn trình ký” / “So sánh hai bản – không gán nhãn trình ký” kèm số lượng theo mức (v4.2, PB2-21).
- Mã phát hiện chỉ được lấy trong bảng mục 2; `tao_bao_cao.py` từ chối mã không có trong bảng (v4.2, PB2-11).
- Bỏ qua dương tính giả của script (`bo_qua_the_thuc`): chỉ từng phát hiện, đúng **tệp** (`tep` – bắt buộc khi hồ sơ có từ hai tệp đã đo; ghi tên tệp như cổng hồ sơ ghi; tên ngắn chỉ được nhận khi chỉ đúng MỘT tệp – v4.5, PB5-WORK-06), đúng vị trí script ghi, lý do cụ thể (≥ 20 ký tự); không bỏ cả một mã ở mọi vị trí (v4.3, TH-05). Phát hiện **Mức 1** (CC-01) được loại khi script kiểm được: `nguyen_van` trong ngoặc kép, ≥ 15 ký tự, **đúng là chữ của đoạn script báo** trong đúng tệp đó; báo cáo in riêng **Bảng 2a “Phát hiện Mức 1 của script đã loại khỏi kết luận”** (tệp, mã, vị trí, nguyên văn, lý do) để người ký xem lại (quyết định E2 của Hiệu trưởng ngày 27/10/2026; PB4-GPT-02, PB4-WORK-06).
- Hồ sơ bị cổng CHẶN → **không lập báo cáo, không gán nhãn**; chỉ gửi thông báo của cổng (`05-Cong-Ho-So.md`).
- Không dùng nhãn khác (bỏ hẳn “CHƯA KẾT LUẬN ĐIỀU KIỆN TRÌNH KÝ”, “nhãn tối thiểu”, “có điều kiện”…).
- Nhãn phải khớp Bảng 2 (số lượng theo mức) – kiểm bằng `tools/tao_bao_cao.py` (tự tính nhãn; `--chi-kiem` để kiểm).
- Còn Mức 1 thì ghi thêm câu: “Văn bản chưa nên phát hành cho đến khi các lỗi bắt buộc được khắc phục.”
- Văn bản đã ban hành (không phải dự thảo): vẫn tính theo bảng, nhưng script thay nhãn bằng **“Kiến nghị sửa đổi, bổ sung”** kèm số lượng theo mức (dữ liệu báo cáo ghi `"da_ban_hanh": true`). Đây là nhãn riêng của trường hợp này, không dùng cho dự thảo.
- Một vị trí không được vừa ghi lỗi ở Phần II vừa ghi Đạt ở Phần III (script kiểm).
- Mức độ tuân thủ pháp luật (Phần V) gán cố định: **Chưa đạt** (≥ 1 Mức 1) / **Đạt** (0 Mức 1, ≥ 1 Mức 2) / **Tốt** (0 Mức 1–2, ≥ 1 Mức 3) / **Rất tốt** (0 Mức 1–3).

## 6. Chế độ đối chiếu việc sửa (ĐC) – trạng thái cố định
| Trạng thái | Điều kiện |
|---|---|
| Đã sửa đạt | tệp hiện hành đã khắc phục **nguyên nhân cốt lõi** của mục mở (đo lại bằng script hoặc trích nguyên văn mới); không phát sinh lỗi mới cùng vị trí |
| Sửa một phần | khắc phục được một phần; **phần còn lại ghi thành một phát hiện ở Phần II** (mã, mức theo bảng) và nối qua trường `ma_phat_hien` |
| Chưa sửa | tệp hiện hành giữ nguyên; ghi lại thành phát hiện ở Phần II (`ma_phat_hien`) |
| Không tiếp thu – có giải trình | Báo cáo tiếp thu, giải trình có nêu lý do; người rà soát đánh giá lý do: hợp lệ → đóng mục; không hợp lệ → giữ mức cũ, nêu căn cứ |
| Không còn áp dụng | nội dung liên quan đã bị xóa hợp lệ khỏi dự thảo |
| Kiến nghị lần trước không còn phù hợp | kiến nghị cũ sai căn cứ; ghi căn cứ đúng (trường `can_cu_dung`), không bắt đơn vị sửa theo kiến nghị sai |

- Chế độ ĐC bắt buộc có II.C Kiểm hồi quy (mỗi dòng đủ `ma_cu`, `ket_qua`; in sau II.B); chỉ dùng khi cổng xác định lần rà soát ≥ 2.
- Không lấy lời khẳng định trong Báo cáo tiếp thu, giải trình thay cho việc kiểm tệp thực.
- Trước khi kế thừa một kiến nghị của báo cáo lần trước, kiểm lại kiến nghị đó với văn bản nguồn; kiến nghị cũ sai căn cứ → ghi “Kiến nghị lần trước không còn phù hợp” và nêu căn cứ đúng (không bắt đơn vị sửa theo kiến nghị sai).
