---
name: ktc-ioffice
description: Quét cổng iOffice (QLVB&ĐH) tỉnh Quảng Ngãi của Trường Cao đẳng Kon Tum trong Claude in Chrome — tra cứu Kế hoạch KH-CĐKT và Thông báo TB-CĐKT, tải tệp đính kèm, xuất tệp CSV để cập nhật CSDL theo dõi nhiệm vụ. Dùng khi người dùng nói "quét iOffice", "cập nhật văn bản mới", "/ioffice", hoặc đang mở office.quangngai.gov.vn và muốn lấy kế hoạch, thông báo kết luận mới.
---

# Quét iOffice — lấy văn bản mới cho CSDL theo dõi nhiệm vụ

Chạy trong **Claude in Chrome**, trên tab `office.quangngai.gov.vn` mà người dùng **đã tự đăng nhập**.
Kết quả là tệp `ioffice-quet_<yyyymmdd-hhmm>.csv` và các tệp đính kèm trong thư mục Downloads.
Người dùng sau đó bấm đúp `Cap-nhat-CSDL.bat` để ghi CSDL. Phân loại, chống trùng và khớp biểu mẫu
do script trên máy làm (`29-Cong-Cu/cap_nhat_csdl.py` + `phanloai.py`). **Skill này không phân loại,
không bỏ văn bản nào theo nội dung.**

## Ràng buộc bất biến — đọc trước khi làm

1. **Chỉ ĐỌC.** Không bấm Gửi, Duyệt, Xử lý, Chuyển, Trả lại, Kết thúc, Đánh dấu, Lưu hay bất kỳ nút nào
   làm thay đổi trạng thái văn bản. Chỉ dùng: ô tìm kiếm, nút Tìm kiếm, chọn số bản ghi, phân trang,
   mở chi tiết văn bản, liên kết tải tệp.
2. **Không đăng nhập hộ.** Gặp màn hình đăng nhập → DỪNG, trả lời đúng một câu:
   "Phiên đăng nhập iOffice đã hết hạn, cần đăng nhập lại bằng tay trong Chrome rồi chạy lại."
   Không gõ tên đăng nhập, mật khẩu, mã OTP.
3. **Không bịa dữ liệu.** Chỉ ghi giá trị đọc được từ trang. Tải tệp lỗi → ghi lỗi, không ghi tên giả.
4. Không chép, không gửi nội dung văn bản ra ngoài trình duyệt (trừ tệp CSV và tệp tải về máy).

## Tham số (mặc định nếu người dùng không nói)

| Tham số | Mặc định |
|---|---|
| Từ ngày | 28/09/2026 |
| Tải tệp | Chỉ **văn bản chính** (hàng "File đính kèm") của mọi văn bản chưa tải (sổ nhớ `ktc_da_tai_v2`); "không tải" để bỏ qua |

## Bước 1 — Mở Tra cứu văn bản

Ở menu trái bấm **"Tra cứu văn bản"**. Nếu thấy form đăng nhập → áp dụng ràng buộc 2.

## Bước 2 — Tra hai lượt

Với mỗi từ khóa `KH-CĐKT`, rồi `TB-CĐKT`:
1. Điền ô Số ký hiệu (id `txt_so_kyhieu`), đặt `selectPageRec` = 50, bấm Tìm kiếm.
2. Đọc bảng bằng javascript (không chụp màn hình):

```javascript
(() => [...document.querySelectorAll('tr[onclick*="showDocDetail"]')].map(tr => {
  const td = [...tr.querySelectorAll('td')].map(x => x.innerText.trim().replace(/\s+/g, ' '));
  return { doc_id: (tr.getAttribute('onclick').match(/showDocDetail\(\s*'?(\d+)/) || [])[1],
           trich_yeu: td[2], so_di: td[3], so_ky_hieu: td[4], ngay: td[7],
           do_khan: td[10], dv_ban_hanh: td[11], xu_ly: td[12] };
}))()
```

3. **Đọc HẾT các trang**: chừng nào dòng cuối trang còn có ngày ≥ "Từ ngày" thì bấm trang sau, đọc
   tiếp. Không dừng ở 2 trang hay 100 dòng.
   Kiểm tra trước khi sang bước 3: số ký hiệu nhỏ nhất đọc được phải có ngày < hoặc = "Từ ngày"
   (tức đã chạm mốc). Nếu chưa chạm mốc mà hết trang → ghi rõ trong báo cáo "Chưa quét đủ:
   <KH|TB> mới đọc tới số …, ngày …".
4. **Cổng có thể chỉ trả tối đa 100 dòng/lượt tra.** Nếu một lượt đọc được đúng 100 dòng (hoặc bội số
   của 50) mà chưa chạm mốc ngày → tra lại **chia khoảng ngày** bằng các ô ngày văn bản "Từ ngày /
   Đến ngày" của form (đọc id thật của ô bằng javascript trước khi điền), ví dụ 28/09–10/10 rồi
   11/10–hôm nay, sao cho mỗi lượt < 100 dòng. Gộp kết quả, bỏ dòng trùng Doc ID.
4. Giữ các dòng có `ngay` ≥ "Từ ngày". Nếu cột không đúng thứ tự (trích yếu rỗng, ngày không dạng
   dd/mm/yyyy) → dừng, báo người dùng thứ tự tiêu đề cột thật, không đoán.

## Bước 3 — Tải VĂN BẢN CHÍNH (chỉ hàng "File đính kèm")

### Cấu trúc trang chi tiết (đã xác nhận trên KH 1073, 25/10/2026)

| Hàng bảng (cột nhãn bên trái) | Là gì | Tải? |
|---|---|---|
| **File đính kèm** | **Văn bản chính**: bản `.docx` (người ký gửi) + bản `.pdf` ký số (Văn thư); kèm "Thông tin ký số" | **CÓ — chỉ hàng này** |
| Văn bản liên quan | Liên kết sang **văn bản KHÁC** (báo cáo rà soát, quyết định, kế hoạch trước…) | **KHÔNG** — không bấm, không mở, không tải |
| Tài liệu liên quan | Tài liệu phụ | **KHÔNG** |
| Nút "Nén và tải tất cả" | Tải gộp | **KHÔNG** |

> Lỗi lần chạy 25/10/2026: skill đã đi theo cả "Văn bản liên quan" và tải tệp của các văn bản đó → 44/45
> văn bản bị ghi nhận nhầm báo cáo 897, phiếu, Thông tư, công văn UBND làm văn bản chính. Không lặp lại.

### Danh sách cần tải — sổ nhớ v2

Sổ nhớ cũ `ktc_da_tai` ghi nhận cả những lần tải nhầm → **bỏ, dùng `ktc_da_tai_v2`** (lần chạy đầu tiên với
bản này sẽ tải lại bản chính cho toàn bộ văn bản, đúng ý đồ).

```javascript
(() => { const da = new Set(JSON.parse(localStorage.getItem('ktc_da_tai_v2') || '[]'));
  return window.__kq.filter(r => !da.has(r.doc_id)).map(r => r.doc_id); })()
```

### Lấy đúng liên kết trong hàng "File đính kèm"

Hàm dùng cho cả trang đang mở (`document`) lẫn HTML chi tiết lấy bằng `fetch` (`new DOMParser().parseFromString(html,'text/html')`):

```javascript
window.__fileChinh = (doc) => {
  const nhan = [...doc.querySelectorAll('td,th')].find(td =>
    td.textContent.replace(/\s+/g, ' ').trim().toLowerCase() === 'file đính kèm');
  if (!nhan) return null;                       // khong thay hang -> bao loi, KHONG tai thay
  const o = nhan.nextElementSibling;            // o noi dung ben phai nhan
  return [...o.querySelectorAll('a, [onclick*="filedownload"]')]
    .map(e => { const m = (e.getAttribute('onclick') || e.getAttribute('href') || '')
                  .match(/filedownload\(\s*'([^']*)'\s*,\s*'([^']*)'/);
                return m ? { path: m[1], name: m[2] } : null; })
    .filter(Boolean)
    .filter((x, i, a) => a.findIndex(y => y.path === x.path) === i);   // nut "Xem" va ten tep trung nhau
};
```

Chạy thử trên **văn bản đầu tiên** và báo người dùng danh sách tệp tìm được (phải là tệp văn bản chính,
thường 1 `.docx` + 1 `.pdf`). Danh sách chứa tên văn bản khác → DỪNG, báo người dùng.

### Tải và đặt tên

Mọi tệp trong hàng "File đính kèm" đặt tên **`<số>-<KH|TB>__CHINH__<tên gốc>`**
(vd `1073-KH__CHINH__Ke hoach xet ho so NLTHN_NLSP nguoi day nghe 2026.pdf`).

**Cách A — ưu tiên (không mở từng trang):**
1. `showDocDetail.toString()`, `filedownload.toString()` → địa chỉ trang chi tiết và địa chỉ tải.
2. Mỗi Doc ID: `fetch(<địa chỉ chi tiết>, {credentials:'include'})` → `DOMParser` → `__fileChinh(doc)`.
3. Mỗi tệp: `fetch(<địa chỉ tải từ path>, {credentials:'include'})` → `blob` → thẻ `<a download=...>` → `click()`. Nghỉ ~1 giây.
4. Kiểm blob: kích thước > 0, `blob.type` không phải `text/html` (trang đăng nhập). Sai → ghi `loi`, KHÔNG lưu.

**Cách B — dự phòng:** mở `showDocDetail(<doc_id>,'','2')`, chạy `__fileChinh(document)`, bấm **chỉ** các liên
kết đó (đổi tên khi lưu nếu được; không đổi được thì ghi tên gốc vào `ten_file`), quay lại kết quả.

Ghi `ten_file` = các tên gốc trong hàng "File đính kèm", nối bằng `" | "`.
Hàng "File đính kèm" rỗng/không thấy → `loi` = "không có File đính kèm", không tải gì khác.

Sau mỗi văn bản tải **đủ** tệp của hàng "File đính kèm":
```javascript
((id) => { const k = 'ktc_da_tai_v2', s = new Set(JSON.parse(localStorage.getItem(k) || '[]'));
  s.add(id); localStorage.setItem(k, JSON.stringify([...s])); })('<doc_id>')
```
Văn bản lỗi KHÔNG ghi vào sổ nhớ → lần sau tự tải lại.

Lần đầu Chrome có thể hỏi "Cho phép tải nhiều tệp" → báo người dùng bấm **Cho phép**.
"tải lại hết" → `localStorage.removeItem('ktc_da_tai_v2')`. "không tải" → bỏ qua bước này.

Chỉ đọc: chỉ dùng hàm/địa chỉ XEM và TẢI; không gọi hàm hay địa chỉ nào có tên gợi ý xử lý, chuyển,
duyệt, trả lại, cập nhật trạng thái.

## Bước 4 — Xuất CSV về Downloads

Gộp mọi dòng của hai lượt, gán vào `window.__kq` (mảng object như bước 2, thêm `ten_file` = các tên
tệp nối bằng `" | "`, và `loi`), rồi chạy:

```javascript
(() => {
  const cot = [['doc_id','Doc ID'],['trich_yeu','Trích yếu'],['so_di','Số đi'],['so_ky_hieu','Số ký hiệu'],
    ['ngay','Ngày văn bản'],['do_khan','Độ khẩn'],['dv_ban_hanh','Đơn vị ban hành'],
    ['xu_ly','Đơn vị/người xử lý chính'],['ten_file','Tên file đính kèm'],['loi','Lỗi tải']];
  const q = v => '"' + String(v ?? '').replace(/"/g, '""') + '"';
  const csv = '﻿' + [cot.map(c => q(c[1])).join(',')]
    .concat(window.__kq.map(r => cot.map(c => q(r[c[0]])).join(','))).join('\r\n');
  const d = new Date(), p = n => String(n).padStart(2, '0');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv;charset=utf-8' }));
  a.download = `ioffice-quet_${d.getFullYear()}${p(d.getMonth()+1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}.csv`;
  a.click(); return a.download;
})()
```

## Bước 5 — Báo cáo ngắn (tiếng Việt)

- Số văn bản đọc được: KH …, TB … (từ ngày …).
- Tên tệp CSV đã xuất.
- Số tệp đính kèm đã tải; danh sách lỗi tải (nếu có).
- Câu cuối cố định: **"Bấm đúp `Cap-nhat-CSDL.bat` để ghi vào CSDL."**

Không có dòng nào từ ngày đã chọn → chỉ trả lời "Không có văn bản mới trên iOffice." và không xuất CSV.
