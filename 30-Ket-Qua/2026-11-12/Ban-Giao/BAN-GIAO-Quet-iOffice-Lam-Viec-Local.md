# Bàn giao riêng: Quét iOffice → CSDL theo dõi nhiệm vụ (làm việc trên máy)

**Ngày:** 12/11/2026 · **Người nhận:** Nguyễn Ngọc Quang Phục · **Làm tại:** máy cá nhân, thư mục `D:\.CLAUDE code\KTC-Quan-tri`

## 1. Lấy mã nguồn về máy

Các tệp quét iOffice **đã có trên nhánh `main`** (giống hệt nhánh `claude/charming-cray-lhv264`, kiểm 12/11/2026).
Không cần gộp PR #2.

```
cd /d "D:\.CLAUDE code\KTC-Quan-tri"
git checkout main
git pull origin main
```

## 2. Bộ tệp

| Tệp | Vai trò |
|---|---|
| `29-Cong-Cu/ktc-ioffice/SKILL.md` | Skill chạy trong **Claude in Chrome**: tra cứu KH-CĐKT, TB-CĐKT, tải tệp, xuất CSV |
| `29-Cong-Cu/ktc-ioffice/tai_file_dinh_kem.js` | **Đoạn mã tải cố định** — chỉ tải ô "File đính kèm"; đã nhúng nguyên văn trong SKILL.md |
| `29-Cong-Cu/ktc-ioffice/ktc-ioffice.zip` | Gói để upload lên claude.ai (bản mới nhất) |
| `29-Cong-Cu/cap_nhat_csdl.py` | Đọc CSV → lọc ngày, chống trùng, phân loại, ghi CSDL, nhận tệp tải về, khớp biểu mẫu QLĐT |
| `29-Cong-Cu/Cap-nhat-CSDL.bat` | Bấm đúp để chạy `cap_nhat_csdl.py` với CSV mới nhất trong Downloads |
| `10-Dau-Vao/01-Dau-Moi-Nop/phanloai.py` | **Luật phân loại dùng thật** (script import từ thư mục này) |
| `10-Dau-Vao/01-Dau-Moi-Nop/CSDL-Theo-doi-nhiem-vu_20260929_v1.xlsx` | CSDL theo dõi (sheet CSDL, Nhật ký chạy) |

> ⚠️ Trên main còn `29-Cong-Cu/phanloai.py` (bản trùng) và `29-Cong-Cu/_to_delete/*.moi`. Script **không** dùng các
> tệp này. Sửa luật thì sửa `10-Dau-Vao/01-Dau-Moi-Nop/phanloai.py`; hai tệp kia Anh tự xóa khi tiện.

## 3. Cài một lần

1. `pip install openpyxl python-docx pypdf`
2. claude.ai (tài khoản dùng trên Chrome) → **Settings → Capabilities → Skills**: xóa `ktc-ioffice` cũ, **Upload**
   `29-Cong-Cu/ktc-ioffice/ktc-ioffice.zip`, bật lên.
3. Chuột phải `Cap-nhat-CSDL.bat` → Send to → Desktop (create shortcut).

## 4. Quy trình mỗi lần quét

| Bước | Làm ở đâu | Thao tác |
|---|---|---|
| 1 | Chrome, iOffice **đã đăng nhập** | Mở khung Claude, gõ **"quét iOffice"** |
| 2 | Chrome | Skill tra cứu, đọc hết trang (tự chia khoảng ngày khi chạm 100 dòng) |
| 3 | Chrome | Skill **chạy thử 1 văn bản**, in danh sách tệp → Anh đối chiếu với ô "File đính kèm" trên màn hình → đúng thì cho chạy hàng loạt |
| 4 | Chrome | Lần đầu Chrome hỏi "Cho phép tải nhiều tệp" → **Cho phép** |
| 5 | Downloads | Có `ioffice-quet_<ngày-giờ>.csv` + các tệp `<số>-<KH|TB>__CHINH__<tên>` |
| 6 | Máy | **Đóng Excel**, bấm đúp **Cap-nhat-CSDL** |
| 7 | Máy | Đọc báo cáo trên cửa sổ đen: văn bản mới, tệp đã nhận, việc cần người xử lý |

Chạy thử không ghi gì: `Cap-nhat-CSDL.bat --thu`.

## 5. Quy tắc đã chốt (đừng đổi khi không có lý do)

- **Chỉ đọc iOffice**: chỉ xem và tải; cấm bấm Chuyển xử lý, Trả lại, Kết thúc, Đánh dấu.
- **Chỉ tải ô "File đính kèm"**; không tải "Văn bản liên quan", "Tài liệu liên quan", "Nén và tải tất cả".
- Số ký hiệu gắn vào tên tệp **lúc tải** (bản .docx chưa có số). `.docx`/`.xlsx` làm nguồn trích; `.pdf` ký số ghi cột
  **"Bản ký số"**.
- Phân loại: KH thực hiện → Nhiệm vụ; KH vận hành đào tạo/mã lớp → Vận hành đào tạo; TB kết luận → Nhiệm vụ; TB khác →
  **Chờ phân loại** (vẫn ghi, vẫn tải). Dòng "Cần xem lại" tự phân loại lại khi luật được bổ sung.
- CSDL **sao lưu tự động** vào `01-Dau-Moi-Nop/_sao-luu/` trước mỗi lần ghi.

## 6. Việc còn mở của phần quét

1. **Đoạn mã tải mới chưa chạy trên iOffice thật** (mới thử trên trang mô phỏng 6/6). Lần chạy đầu: nếu skill báo
   "không mở được trang chi tiết đúng văn bản" → ô "Số ký hiệu" trên trang thật hiển thị khác (khoảng trắng, xuống dòng);
   sửa hàm `so_tren_trang()` trong `tai_file_dinh_kem.js`, nhúng lại vào SKILL.md, đóng gói lại zip.
2. Tệp tải nhầm cũ (văn bản liên quan) trong `10-Dau-Vao/01-Dau-Moi-Nop/2026-09/`: liệt kê bằng
   `python 29-Cong-Cu/kiem_trich_nhiem_vu.py --tep-nham`, Anh tự xóa.
3. KH 956–969 (28/9–01/10): lần quét cũ không lấy được; quét lại bằng skill bản mới (chia khoảng ngày).
4. 23 văn bản "Cần xem lại" (tham dự sự kiện, thể thao, lớp bồi dưỡng ngắn hạn): chờ Anh chốt chủ trương rồi bổ sung luật.

## 7. Nối tiếp (không bắt buộc)

Sau khi CSDL có tệp chính đúng: trích nhiệm vụ chi tiết bằng skill `29-Cong-Cu/ktc-trich-nhiem-vu/`
(`kiem_trich_nhiem_vu.py --chuan-bi` → AI trích JSON → kiểm → duyệt → `nap_master.py`). Các tệp này cũng **đã có trên main**.
