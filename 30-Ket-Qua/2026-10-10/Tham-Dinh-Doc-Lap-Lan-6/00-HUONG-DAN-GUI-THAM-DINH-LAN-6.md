# Hướng dẫn gửi thẩm định độc lập lần 6 — KTC-Quan-tri 1.3.13

**Căn cứ:** Ý kiến Hiệu trưởng ngày 04/10/2026 tại Phiếu trình ngày 03/10/2026 của Phòng QLKHCN&HTPT (“đề nghị lấy ý kiến thẩm
định thêm qua các hệ thống AI độc lập khác: NotebookLM, Copilot, Work”); điểm b Mục 8 Thông báo số 1056/TB-CĐKT.

## 1. Năm hệ thống, bốn nhà cung cấp

| Hệ thống | Nhà cung cấp | Vai trò | Gửi | Câu lệnh |
|---|---|---|---|---|
| NotebookLM | Google | Đối chiếu văn bản: Đọc toàn bộ 36 nguồn, trích dẫn chính xác | 36 tệp `Goi-A-Doc/` | `Cau-lenh/P1-NotebookLM.md` |
| Copilot | Microsoft | Thẩm định tổng hợp trên bản gộp | 05 tệp `Goi-Gop-Copilot/` | `Cau-lenh/P2-Copilot.md` |
| ChatGPT Work | OpenAI | Kiểm tra kỹ thuật: Mã băm, danh mục tệp, chạy thao tác chặn ghi | `Goi-day-du-tham-dinh-lan-6.zip` | `Cau-lenh/P3-ChatGPT-Work.md` |
| Grok | xAI | Thẩm định tổng hợp trên bản gộp (đã tham gia lần 1 - 5) | 05 tệp `Goi-Gop-Copilot/` | `Cau-lenh/P4-Grok.md` |
| Gemini | Google | Thẩm định tổng hợp trên bản gộp (đã tham gia lần 1 - 5) | 05 tệp `Goi-Gop-Copilot/` | `Cau-lenh/P5-Gemini.md` |
| Grok | xAI | Thẩm định tổng hợp trên bản gộp (đã tham gia lần 1 - 5) | 05 tệp `Goi-Gop-Copilot/` | `Cau-lenh/P4-Grok.md` |
| Gemini | Google | Thẩm định tổng hợp trên bản gộp (đã tham gia lần 1 - 5) | 05 tệp `Goi-Gop-Copilot/` | `Cau-lenh/P5-Gemini.md` |

**Về “Work”:** Điểm b Mục 8 Thông báo số 1056/TB-CĐKT liệt kê các hệ thống “ChatGPT, **ChatGPT Work**, Gemini, Copilot,
NotebookLM, Grok, Dola”, nên em hiểu “Work” là **ChatGPT Work** (bản ChatGPT dành cho tổ chức). Cùng điểm đó quy định tính độc lập
xác định **theo nhà cung cấp mô hình**: Copilot bản cá nhân và Microsoft 365 Copilot (thẻ Work) là cùng Microsoft, chỉ tính một
hệ. Nếu anh xác định “Work” là Microsoft 365 Copilot thì dùng cách A tại `P2-Copilot.md` và vẫn nên gửi ChatGPT để có một bên kiểm
kỹ thuật (lần 1 - 5 chỉ ChatGPT tìm ra lỗi thật qua chạy kiểm tra).

Năm hệ thuộc bốn nhà cung cấp (Google: NotebookLM, Gemini — tính một; Microsoft; OpenAI; xAI), đều độc lập với Anthropic (Claude — hệ dùng để xây dựng Bộ công cụ), đáp ứng yêu cầu tối
thiểu 2 vòng, nhiều hệ độc lập tại điểm b Mục 8 Thông báo số 1056/TB-CĐKT.

## 2. Trước khi gửi (Mục 7 Thông báo số 1056/TB-CĐKT)

- Xem `KIEM-TRA-BAO-MAT.md`: Không có số điện thoại, số căn cước, mã khóa; chỉ có 02 địa chỉ thư của Trường, Phòng nằm sẵn trong
  nội dung plugin (đã gửi ở lần 1 - 5). Gói **không** chứa thư mục dự án, nhật ký, dữ liệu KPI cá nhân.
- Dùng tài khoản của Trường, không dùng tài khoản cá nhân.
- Phiếu trình ngày 03/10/2026 đưa vào dạng **chép lời** (N02), không gửi bản quét có chữ ký.
- Không mở rồi lưu lại các tệp trong gói (bài học vòng 4: Word tự thêm đoạn trống làm lệch mã băm). Đối chiếu bằng `00-DANH-MUC.md`.

## 3. Tiến độ đề xuất (để kịp trình ban hành đầu tuần 12 - 13/10/2026)

| Việc | Hạn |
|---|---|
| Gửi 5 hệ thống | 10/10/2026 |
| Nhận báo cáo, lưu vào `00. CONG CU AI\Tham-dinh-AI-plugin\2 Cac AI khac\Lan 6\` | 11/10/2026 |
| Claude tiếp thu, giải trình lần 6 | 12/10/2026 |

## 4. Sau khi có kết quả — câu lệnh gửi Claude

```text
Các hệ thống AI độc lập (NotebookLM, Copilot, ChatGPT Work, Grok, Gemini) đã có Báo cáo thẩm định lần 6 về bộ công cụ KTC-Quan-tri 1.3.13 và các văn bản kèm theo (thư mục D:\OneDrive - Trường Cao Đẳng Kon Tum\00. CONG CU AI\Tham-dinh-AI-plugin\2 Cac AI khac\Lan 6). Đề nghị em phân tích thấu đáo, kiểm từng phát hiện trên mã nguồn, tệp plugin và kho KTC-Database, rồi lập Báo cáo tiếp thu, giải trình lần 6; sửa các văn bản (Thông báo, Hướng dẫn, Báo cáo) bằng Track Changes, lưu trong 30-Ket-Qua/<ngày>.
```

## 5. Thành phần gói

| Thư mục, tệp | Nội dung |
|---|---|
| `Goi-A-Doc/` | 36 nguồn N00 - N35 (danh mục tại N00 mục 7) |
| `Goi-Gop-Copilot/` | GOP-0 nhiệm vụ · GOP-1 văn bản trình, dự thảo (PDF) · GOP-2 bằng chứng · GOP-3 plugin cốt lõi · GOP-4 báo cáo lần 5 |
| `Goi-day-du-tham-dinh-lan-6.zip` | Gói A + plugin 1.3.13 (.zip, .sha256) + kết quả nghiệm thu gốc (.json) |
| `Cau-lenh/` | 05 câu lệnh (P1 - P5) |
| `01-CACH-DOC-TEP-TUNG-HE.md` | Cách từng hệ đọc tệp, cách kiểm, xử lý khi bị cắt — **đọc trước khi gửi** |
| `MA-KIEM-DOC-TEP.md` | Bảng mã kiểm từng tệp để đối chiếu Bước 0 — **không tải lên hệ AI** |
| `Goi-Gop-nho/` | Bản gộp chia nhỏ (11 tệp) cho hệ cắt tệp dài |
| `KIEM-TRA-BAO-MAT.md` · `00-DANH-MUC.md` | Quét dữ liệu cá nhân · SHA-256 từng tệp |

Dựng lại gói: `python 29-Cong-Cu/lap_goi_tham_dinh_doc.py` (cần Microsoft Word để xuất PDF).
