# Công cụ của Skill ktc-ra-soat-897 v4.6.4 (03/11/2026 – bản hoàn thiện sau nghiệm thu lần 3 và quyết định Q1–Q5; tự kiểm của người sửa; CHƯA duyệt phát hành)

Bốn script, chạy theo thứ tự cố định, cùng một mô-đun dùng chung `nhan_dien_chung.py` (v4.6). Yêu cầu: Python 3, `lxml`, `python-docx`; `soffice` (LibreOffice) và `pdftotext`/`pdfinfo` (poppler) cho phần dựng trang và kiểm PDF – thiếu thì script vẫn chạy, phần liên quan ghi “chưa kiểm”.

| Bước | Script | Việc làm | Kết quả |
|---|---|---|---|
| 1 | `kiem_ke_ho_so.py` | Cổng hồ sơ: định dạng tệp (ảnh, scan, tệp nén, Word chứa ảnh chụp), nhận diện vai trò tệp theo nội dung, đối chiếu mọi văn bản được dự thảo đề cập (cả viết tắt, dạng rút gọn, chú thích) với hồ sơ và Kho, phụ lục, văn bản kèm theo, lần rà soát; `--tac-vu ra-soat|so-sanh|chuan-hoa`; `--vai-tro TỆP=VAI_TRÒ` chỉ định vai trò; `--xuat-anh DIR` xuất ảnh cỡ lớn để AI xem (tệp nhiều chữ có ảnh ≥ 1/4 trang → “PHẢI XEM ẢNH”); v4.3: nhận phụ lục/văn bản kèm theo nộp thành tệp riêng (vai trò kem_theo), quét viện dẫn cả trong các tệp đó, khớp viện dẫn chỉ có số (“NĐ 356”), so sánh đòi đúng hai bản, ghi mã băm SHA-256 từng tệp | Mã thoát 0 = ĐỦ; 2 = CHẶN (kèm thông báo dùng nguyên văn) |
| 2 | `kiem_tra_the_thuc.py` | Đo thể thức từ XML .docx theo bảng thông số KTC; dựng trang bằng LibreOffice để biết trang bắt đầu từng section | Bảng phát hiện (mã TT/TB/TD/CC + mức), mục đạt kèm số đo, mục chưa kiểm |
| 3 | `so_sanh_ban.py` | So sánh hai bản .docx theo đoạn (Thêm/Xóa/Sửa ghép cặp theo độ giống, chi tiết từ ngữ, vị trí “Quy định – Điều N”/“Văn bản chính – Điều N”/“Phụ lục …”/“Chú thích”) – tác vụ so sánh và chế độ ĐC | Bảng thay đổi (Markdown, JSON) |
| 4 | `tao_bao_cao.py` | Nhập kết quả bước 1–2 và dữ liệu rà soát nội dung (JSON); kiểm hợp lệ (mã phải có trong bảng 02; yeu_to_khop dạng bảng; vị trí so theo Điều/khoản); tự tính Bảng 1, Bảng 2, mức tuân thủ, nhãn; `kieu_bao_cao` chinh_thuc/nhanh/so_sanh (nhanh, so_sanh không gán nhãn trình ký; so_sanh cần `--so-sanh ss.json`); v4.3: kết quả đo phải khớp mã băm tệp của hồ sơ đã qua cổng và đủ mọi tệp dự thảo/kèm theo, `xem_anh` bắt buộc khi có “PHẢI XEM ẢNH”, ma trận trỏ đúng DC-01/02/03, bỏ qua dương tính giả từng vị trí; dựng .docx | Báo cáo .docx cấu trúc cố định, hoặc danh sách lỗi dữ liệu |

## Lệnh mẫu
```bash
S=<thư mục skill>/tools
python3 $S/kiem_ke_ho_so.py --kiem-moi-truong                                      # v4.6: kiểm python-docx, pdftotext, pdfinfo, soffice (v4.6.1: chạy được không cần đường dẫn)
python3 $S/kiem_ke_ho_so.py /mnt/user-data/uploads --tac-vu ra-soat --json cong.json   # so sánh: --tac-vu so-sanh; thêm --vong 2, --du-thao <tệp>, --vai-tro "<tệp>=bc_tiep_thu", --xuat-anh anh/ khi cần
python3 $S/kiem_tra_the_thuc.py "<dự thảo>.docx" --json tt.json                  # --he dang cho văn bản Đảng (mặc định tự nhận)
python3 $S/kiem_tra_the_thuc.py "<phụ lục tệp riêng>.docx" --json tt_pl.json     # nếu phụ lục là tệp riêng
python3 $S/so_sanh_ban.py "<bản cũ>.docx" "<bản mới>.docx" --json ss.json          # ĐC, so sánh
python3 $S/tao_bao_cao.py du_lieu.json --cong cong.json --the-thuc tt.json [--the-thuc tt_pl.json] --chi-kiem
python3 $S/tao_bao_cao.py du_lieu.json --cong cong.json --the-thuc tt.json -o "Bao-cao-ra-soat_<ten>.docx"
python3 $S/tao_bao_cao.py du_lieu.json --cong cong.json --the-thuc tt.json --so-sanh ss.json -o "Bao-cao-so-sanh_<ten>.docx"   # tác vụ (c)
python3 $S/tao_bao_cao.py du_lieu.json --cong cong.json --the-thuc tt.json --so-sanh ss_cu_moi.json --chi-kiem               # v4.6: chế độ ĐC bắt buộc --so-sanh (bản lần trước → bản hiện hành)
```
Mẫu `du_lieu.json`: `assets/Mau-Du-Lieu-Bao-Cao.json`.

## Nguyên tắc
- Không sửa mức của phát hiện do script đo. Phát hiện sai (dương tính giả) → đưa vào `bo_qua_the_thuc` kèm lý do cụ thể; lý do được in trong báo cáo.
- v4.4: `bo_qua_the_thuc` ghi `tep` (bắt buộc khi có từ hai tệp đã đo); Mức 1 phải có `nguyen_van` đúng là chữ của đoạn script báo (kết quả đo ghi `doan_goc`); Mức 1 đã loại in ở Bảng 2a. `tao_bao_cao.py` đối chiếu kết quả đo với cổng theo **mã băm** từng tệp (tệp trùng tên ở hai thư mục con được cổng ghi bằng đường dẫn tương đối).
- v4.5: cổng có `--xac-nhan-kem "<tệp>=<lý do ≥ 20 ký tự>"` (quyết định F1) – xác nhận thủ công văn bản kèm theo cùng tên loại khi trích yếu không khớp/không có; ghi vào `xac_nhan_kem_thu_cong` và báo cáo I.7. `--vai-tro "<tệp>=kem_theo"` chỉ sửa vai trò, không bỏ kiểm khớp. `so_sanh_ban.py` ghi mã băm hai tệp; báo cáo so sánh chỉ nhận bảng thay đổi của đúng hai bản đã qua cổng. Ma trận “Khớp” có dấu hiệu khác nhau cần `giai_trinh_khop` (quyết định F2), in ở Bảng 3.
- v4.4: `kiem_tra_the_thuc.py` đếm số dòng thật của đoạn bằng bảng độ rộng chữ `do_rong_chu_TNR.json` (Liberation Serif – số đo tương thích Times New Roman, SIL OFL 1.1) để áp TT-24 cho đoạn nhiều dòng; đoạn sát ngưỡng ghi “chưa kiểm”. Tệp phụ lục/văn bản kèm theo nộp riêng được đo theo vai trò phụ lục/văn bản kèm theo, không theo văn bản chính.
- v4.6.4 (quyết định Q5 ngày 03/11/2026): cổng có `--xac-nhan-toan-van "<tệp>=<lý do ≥ 20 ký tự>"` – xác nhận thủ công toàn văn văn bản nguồn rất ngắn (05-Cong-Ho-So mục 2e); kết quả ghi `xac_nhan_toan_van_thu_cong`, I.7 chữ đỏ; phiên bản dữ liệu v4.6.4.
- v4.6.3 (sau nghiệm thu độc lập lần 3 – xem references/CHANGELOG.md):
  - Đọc JSON có kiểm soát (`nhan_dien_chung.doc_json_an_toan`, dùng cho dữ liệu báo cáo, kết quả cổng/đo/so sánh, danh mục Kho): ≤ 16 MB dữ liệu báo cáo, ≤ 64 MB JSON trung gian, lồng ≤ 64 cấp, số nguyên ≤ 15 chữ số, số thực hữu hạn (NaN/Infinity bị từ chối), không khóa lặp, không ký tự điều khiển/nửa cặp thay thế – lỗi nêu đường dẫn trường và giới hạn.
  - Trường bắt buộc có nội dung kiểm SAU chuẩn hóa khoảng trắng (bỏ zero-width, mọi khoảng trắng Unicode); `so_anh_da_xem` chỉ chữ số ASCII.
  - Dòng dẫn: kiểm TẤT CẢ tên tệp, số hiệu, tên luật (mỗi cụm tên luật không chồng lấn là một định danh; tên luật chỉ khớp phần đầu của một tên dài hơn → không xác định); đồng nghĩa thật của cùng nguồn được nhận.
  - D2: `--kho` khác Kho của gói → cổng CHẶN, trình dựng từ chối JSON cổng ghi Kho ngoài gói. D10: tác vụ so sánh bắt buộc tên tệp ở vị trí phía dự thảo.
  - F11: trình dựng dùng kết quả TÍNH LẠI của cổng, đo, so sánh (không dùng JSON người đưa); `so_sanh_ban.py` ghi đường dẫn tuyệt đối; tên/đường dẫn bản cũ – mới phải đúng tệp thật của mã băm; II.D in tên tệp như cổng ghi. Lỗi tiến trình con kèm chẩn đoán (stderr, quá thời gian).
  - Cổng toàn văn (N12): `05-Cong-Ho-So.md` mục 2d. `.xlsx` đọc theo từng hàng.
  - Tệp kết quả (`-o`, `--json`, `--md`): không trùng tệp đầu vào/hồ sơ, thư mục phải có, ghi qua tệp tạm rồi thay thế. Tệp .docx hỏng/không có → lỗi có kiểm soát (mã 2), không Traceback.
  - Đo thể thức: LibreOffice chạy với hồ sơ người dùng riêng mỗi lần dựng (không xung đột phiên đang mở/tiến trình song song – giảm từ chối nhầm khi tính lại, D3).
- v4.6.2 (sau nghiệm thu độc lập lần 2, F01–F11 – xem references/CHANGELOG.md): `kiem_kieu_du_lieu.py` kiểm kiểu mọi trường dữ liệu báo cáo trước khi xử lý (đường dẫn trường, kiểu hợp lệ; không Traceback); dòng dẫn chỉ tới MỘT nguồn (tên tệp quy tắc `.md` không bị hiểu là số hiệu; “A hoặc B”, tên trùng, tên lạ, từ chung bị từ chối); nhiều Điều, Điều lặp theo phần/Chương; khóa “_” kiểm mọi cấp; cổng nhận trích yếu nhiều đoạn; cổng/đo ghi `tham_so`, trình dựng TÍNH LẠI cổng, đo thể thức, bảng thay đổi và từ chối JSON sửa tay; bố cục bảng (cột tối thiểu, hàng tiêu đề đi cùng dữ liệu, không trang cuối trống); I.7 in đường dẫn tệp gộp, tham số chạy cổng, ghi chú cổng.
- v4.6.1 (nghiệm thu độc lập 02/11/2026 – 12 ca): một bộ phân giải tên tệp cho mọi tùy chọn; nguồn chỉ có phần định danh → CHẶN; gộp tệp trùng phần nội dung; trích dẫn gắn đúng văn bản được dẫn và đúng Điều; khóa “_” dành cho script; `che_do` ĐL/ĐC, `yeu_cau_doc_lap`; danh mục mã cũ phủ hai chiều; kết quả cổng có `dinh_danh`, `gop_trung_noi_dung`.
- v4.6 (báo cáo kiểm toán 01/11/2026, 28 mã KTS và PH-01, PH-02):
  - `nhan_dien_chung.py`: chuẩn hóa trình bày theo thuộc tính Unicode (bỏ ký tự Cf, mọi khoảng trắng Z* → dấu cách, mọi gạch Pd → “-”), `chuan_so_hieu` (bỏ khoảng trắng quanh “/”, “-” trong số hiệu), `la_in_hoa`, `loai_tieu_de_kem` (một cách nhận tiêu đề văn bản kèm theo cho cả tệp dự thảo và tệp riêng), `tim_trich_dan`, `doc_chu`. Các script gọi chung các hàm này – không sửa riêng từng script.
  - Cổng: viện dẫn khớp theo số hiệu đã chuẩn hóa; Kho/hồ sơ dạng nhiều ứng viên – từ hai tệp khác nội dung → “MƠ HỒ” (CHẶN); tên luật khớp đúng; VBHN thay Luật gốc khi khớp số, ngày, luật (quy tắc xác nhận 02/11/2026); ghép phụ lục 1:1 tối ưu; kiểm đầu vào; thiếu pdftotext → lỗi môi trường; JSON thêm `duong_dan`, `kho`, `vbhn_thay_luat_goc`, `phien_ban`.
  - Dựng báo cáo: từ chối kết quả cổng/đo của phiên bản khác (không trộn bản vá rời v4.5.2); tính lại mã băm tệp; đối chiếu trích dẫn với tệp thật; trường bắt buộc, phát hiện trùng; mức chỉ nhận 1/2/3; trùng vị trí theo cấu trúc (Phụ lục/Chương/Mục/Điều/khoản/điểm, tên tệp); ma trận chính thức/so sánh phải có QĐ 1976, QĐ 2073; ĐC cần du_thao_cu và `--so-sanh`; “Chưa kiểm” trọng yếu ở I.8 tính vào nhãn; bảng có hàng tiêu đề lặp lại, không tách dòng qua trang.
  - Đo thể thức: đo cả đoạn trong `w:sdt`; TT-20 xét mọi run có chữ; nhãn “Nơi nhận:” văn bản Đảng cỡ 14, đứng, gạch chân; không dựng được trang → mục số trang “chưa kiểm”; dạng rút gọn CC-01 chỉ khớp cùng loại văn bản. Cổng đọc căn lề theo kế thừa kiểu (style) khi nhận vai trò tệp (KTS-08).
  - Tùy chọn `--dinh-danh` của bản rời v4.5.2 **không** đưa vào (chưa có căn cứ – chờ người phụ trách quyết định).
- Script không đo được một hạng mục (ví dụ độ dài đường kẻ, vị trí đối tượng vẽ) → ghi vào I.8 “Chưa kiểm”, hoặc thêm phát hiện TT với `thu_cong_ly_do` và số đo cụ thể.
- Số trang tính bằng LibreOffice; ghi rõ có thể lệch khi mở bằng Word.
- `legacy/build_tcdm_review_fixed.py`: script dựng báo cáo của hồ sơ cũ (v2.x) – chỉ để tham khảo, không dùng.

## Mã quy tắc của `kiem_tra_the_thuc.py`
TT-01 khổ giấy · TT-02 lề · TT-03 header/footer · TT-04 phông · TT-10…19 phần đầu, căn cứ, nơi nhận · TT-20…24 cỡ chữ, khoảng cách đoạn, giãn dòng, thụt đầu dòng, canh lề – đo trên mọi đoạn lời văn sau khi phân vùng (TT-24 chỉ đoạn dài hơn một dòng; bảng ghi “chưa kiểm”) · TT-30…39 section và số trang · TT-40…45 phụ lục · TT-50, 51 bảng · TT-46 chỉ dẫn phụ lục (văn bản Đảng) · TB-01…03 kỹ thuật soạn thảo · TD-01…05 tên đơn vị, viết hoa, từ ngữ · CC-01 văn bản đã bị thay thế (quét mọi đoạn và chú thích, nhận cả dạng rút gọn “Nghị định 13/2023”; danh sách từ `kho_manifest.json`) · CC-02 văn bản hợp nhất (chỉ khi đã biết VBHN) · CC-06 Luật/Pháp lệnh ghi số trong căn cứ. Văn bản Đảng: các quy tắc riêng 26/10/2026 của văn bản chính quyền không áp; lời văn đo theo HD 05 Phần II mục 6.2.2 (khoảng cách thực giữa hai đoạn ≥ 6 pt, giãn dòng kiểu Exactly 18–22 pt, thụt khoảng 10 mm, dàn đều). Mức theo `references/Quy-Tac-KTC/02-Quy-Tac-Xep-Muc.md`.
