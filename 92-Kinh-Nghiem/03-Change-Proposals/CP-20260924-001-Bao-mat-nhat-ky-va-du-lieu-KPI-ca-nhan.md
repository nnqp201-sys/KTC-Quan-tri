# CP-20260924-001 — Bảo mật nhật ký tự động và dữ liệu KPI cá nhân

**Ngày:** 24/9/2026 · **Trạng thái:** CHỜ DUYỆT — chưa sửa hook, chưa đổi `.gitignore` cho nhật ký
**Nguồn:** lệnh sửa bộ skill KPI mục 6.2; `DL-20260924-001`
**Căn cứ:** QĐ 1923/QĐ-CĐKT Đ23.2 — điểm chi tiết, nhận xét, biên bản, minh chứng chỉ cung cấp cho người có thẩm
quyền, người được đánh giá và người liên quan theo chức năng; Bản cam kết KPI Điều 8.1.

## 1. Hiện trạng (đo ngày 24/9/2026)

| Nơi | Ghi gì | Git | GitHub |
|---|---|---|---|
| `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/<ngày>.jsonl` (hook `ktc_nhat_ky.py`) | **Nguyên văn lời người dùng** ≤ 600 ký tự (`yeu-cau`); câu lệnh Bash, đường dẫn tệp ≤ 200 ký tự (`thao-tac`) | **Có theo dõi** | Đẩy lên mỗi tối (`ktc_backup_github.py`, `git add -A`) |
| `.ktc897/nhat-ky/` (hệ 897) | Tương tự | **Loại khỏi git** — `.gitignore`: "ghi lại nguyên văn lời người dùng … không đưa lên kho chung" | Không |
| `30-Ket-Qua/*/KPI-ca-nhan/` (skill KPI) | Tệp kế hoạch, điểm cá nhân | Loại khỏi git (24/9/2026, có ca thử) | Không |

**Rủi ro:** người dùng dán điểm, nhận xét, xếp loại của một viên chức vào khung chat → nằm trong `.jsonl` → lên GitHub.
Tên tệp `KH-KPI-Q4-2026_<họ-tên>.xlsx` cũng lọt vào nhật ký qua đường dẫn. Hai hệ đang xử lý **không thống nhất**
cùng một loại dữ liệu.

Quét 24/9/2026 các tệp `.jsonl` theo cụm "chấm điểm", "xếp loại", "tự đánh giá", "KPI-ca-nhan": chỉ 1 tệp (24/9) có
khớp, và đó là nội dung lệnh xây skill cùng lệnh chạy thử với tên giả định ("Nguyễn Văn A", "Trần Thị B") — chưa thấy
điểm, nhận xét của người thật. Quét theo cụm từ nên không loại trừ hoàn toàn.

## 2. Đề xuất — ba lớp, chọn một hoặc kết hợp

| # | Thay đổi | Được | Mất | Công sức |
|---|---|---|---|---|
| **A** | Đưa `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/` vào `.gitignore` (thống nhất với `.ktc897/`) | Chặn toàn bộ lời người dùng lên GitHub | Mất bản sao lưu nhật ký trên GitHub; lịch sử cũ **vẫn còn** trong git (muốn xóa phải viết lại lịch sử — việc riêng, cần duyệt riêng) | Nhỏ |
| **B** | Hook **không ghi nội dung** khi lời nhắn hoặc đối tượng thao tác chạm dữ liệu KPI cá nhân: đường dẫn chứa `KPI-ca-nhan`, hoặc lời nhắn có cụm "tự đánh giá", "chấm điểm", "xếp loại", "điểm KPI" kèm số điểm → chỉ ghi `"noi_dung": "[KPI cá nhân — không ghi]"` | Giữ nhật ký cho việc khác | Nhận diện theo cụm từ có thể sót | Vừa; cần ca thử ngược |
| **C** | Người dùng tự đánh dấu: lời nhắn bắt đầu `#riêng` → hook không ghi nội dung | Người dùng chủ động, chắc chắn | Phụ thuộc thói quen | Nhỏ |

**Khuyến nghị:** A + C ngay; B khi skill tự đánh giá (giai đoạn 2) ra đời — lúc đó dữ liệu điểm mới thật sự đi qua
khung chat nhiều.

## 3. Việc kèm theo nếu duyệt

- Sửa nguồn `29-Cong-Cu/plugin_src/scripts/ktc_nhat_ky.py` (không sửa bản trong `31-Plugin/`), dựng lại plugin.
- Ca thử trong `92-Kinh-Nghiem/02-Regression/Cases/test_plugin_nhat_ky_backup.py`: lời nhắn `#riêng …` không vào
  `.jsonl`; lời nhắn thường vẫn ghi; `git check-ignore` với thư mục nhật ký (nếu chọn A).
- Hook đầu phiên (`nap`) và agent `ktc-tu-hoc` vẫn đọc được nhật ký cục bộ — A không ảnh hưởng.
- Xác minh repo GitHub `nnqp201-sys/KTC-Quan-tri` đang **Private** (chưa làm được: máy chưa đăng nhập `gh`).

## 4. Người quyết

Người phụ trách hệ (Phòng TH-HC&QT). Việc xóa lịch sử nhật ký cũ trên GitHub, nếu cần, là quyết định riêng.
