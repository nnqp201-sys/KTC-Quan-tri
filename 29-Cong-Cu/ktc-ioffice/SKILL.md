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

## Bước 3 — Tải tệp trong ô "File đính kèm" (ĐOẠN MÃ CỐ ĐỊNH — không tự viết lại)

**Chỉ tải các tệp trong ô bên phải nhãn "File đính kèm"** — đó là văn bản của chính văn bản đang xem (bản
`.docx`/`.xlsx` soạn thảo + bản `.pdf` ký số; một công văn có thể kèm dự thảo đề án, phụ lục). **Không** tải
"Văn bản liên quan", "Tài liệu liên quan", "Lịch họp liên quan", nút "Nén và tải tất cả".

Bản `.docx`/`.xlsx` **không có số ký hiệu** (soạn trước khi cấp số) — số được gắn vào **tên tệp lúc tải**
(`<số>-<KH|TB|CV>__CHINH__<tên gốc>`) từ ô "Số ký hiệu" của iOffice. Bản `.pdf` ký số là bản pháp lý có số.

**Cách làm — bắt buộc đúng 3 lệnh, không ứng biến:**

1. Dán **nguyên văn** đoạn mã dưới vào trang iOffice (javascript). Kết quả phải là `ktcTai sẵn sàng`.
2. Chạy thử **1 văn bản**: `await ktcTai([window.__kq[0]])` → báo người dùng danh sách tệp in ra, đối chiếu
   với ô "File đính kèm" trên màn hình. Sai (thiếu tệp, có tệp văn bản khác) → DỪNG, báo người dùng.
3. Người dùng xác nhận → `await ktcTai(window.__kq)`. Đoạn mã tự: mở từng văn bản, chờ đúng số ký hiệu hiện
   lên, lấy đủ tệp trong ô, tải, kiểm đủ số tệp, ghi sổ nhớ `ktc_da_tai_v2`, ghi tên tệp vào `window.__kq`
   (cột `ten_file` cho CSV). Văn bản lỗi in `LỖI …` và không ghi sổ nhớ → lần sau tự tải lại.

Lần đầu Chrome hỏi "Cho phép tải nhiều tệp" → báo người dùng bấm **Cho phép**.
"tải lại hết" → `await ktcTai(window.__kq, {tai_lai: true})`. "không tải" → bỏ qua bước này.

```javascript
// ktc-ioffice — tai DUNG o "File đính kèm" cua tung van ban tren iOffice (QLVB&DH Quang Ngai).
// Dan NGUYEN VAN doan nay vao trang iOffice (javascript_tool), KHONG viet lai, KHONG sua.
//
//   await ktcTai([{doc_id:'2326501', so_ky_hieu:'1073/KH-CĐKT'}])   // thu 1 van ban, xem ket qua
//   await ktcTai(window.__kq)                                        // hang loat (bo qua VB da tai)
//
// Chi DOC: chi goi showDocDetail (xem) va filedownload (tai). Khong bam nut xu ly nao.
// Chi lay lien ket trong O BEN PHAI nhan "File đính kèm"; bo "Văn bản liên quan", "Tài liệu liên quan",
// "Nén và tải tất cả". Ten tep luu: <so>-<KH|TB|CV>__CHINH__<ten goc> (so ky hieu lay tu iOffice, vi
// ban .docx/.xlsx chua co so). Tra ve bang ke de ghi cot "Tên file đính kèm" cua CSV.
(() => {
  const SO_NHO = 'ktc_da_tai_v2';
  const ngu = ms => new Promise(r => setTimeout(r, ms));
  const sach = s => (s || '').replace(/\s+/g, ' ').trim();
  const loai = so => /\/KH-/i.test(so) ? 'KH' : /\/TB-/i.test(so) ? 'TB' : 'CV';
  const tien_to = so => `${(so.match(/^\s*(\d+)/) || [, 'x'])[1]}-${loai(so)}__CHINH__`;

  // O noi dung ben phai nhan "File đính kèm" -> [{path,name}] (bo trung nut Xem/ten tep)
  window.ktcFileChinh = (doc = document) => {
    const nhan = [...doc.querySelectorAll('td,th')].find(td => sach(td.textContent).toLowerCase() === 'file đính kèm');
    if (!nhan || !nhan.nextElementSibling) return null;
    const ds = [];
    nhan.nextElementSibling.querySelectorAll('[onclick],[href]').forEach(e => {
      const m = ((e.getAttribute('onclick') || '') + ' ' + (e.getAttribute('href') || ''))
        .match(/filedownload\(\s*['"]([^'"]*)['"]\s*,\s*['"]([^'"]*)['"]\s*(?:,\s*['"]?([^'")]*)['"]?)?/);
      if (m && !ds.some(x => x.path === m[1])) ds.push({ path: m[1], name: m[2], type: m[3] || '' });
    });
    return ds;
  };

  // So ky hieu dang hien tren trang chi tiet (de chac chan trang da chuyen sang dung van ban)
  const so_tren_trang = () => {
    const nhan = [...document.querySelectorAll('td,th')].find(td => sach(td.textContent).toLowerCase() === 'số ký hiệu');
    return nhan && nhan.nextElementSibling ? sach(nhan.nextElementSibling.textContent) : '';
  };

  // Goi filedownload cua trang nhung CHAN lai dia chi tai (window.open / a.click / form.submit) de tu tai
  // bang fetch va dat ten co tien to. Khong bat duoc -> de trang tu tai voi ten goc (ghi nhan 'ten_goc').
  async function tai_mot(f, ten_moi) {
    let bat = null;
    const goc = { open: window.open, click: HTMLAnchorElement.prototype.click, submit: HTMLFormElement.prototype.submit };
    window.open = u => { bat = { url: u }; return null; };
    HTMLAnchorElement.prototype.click = function () { if (this.href && !bat) bat = { url: this.href }; else goc.click.call(this); };
    HTMLFormElement.prototype.submit = function () { bat = { url: this.action, method: (this.method || 'post').toUpperCase(), body: new FormData(this) }; };
    try { window.filedownload(f.path, f.name, f.type); await ngu(400); }
    finally { window.open = goc.open; HTMLAnchorElement.prototype.click = goc.click; HTMLFormElement.prototype.submit = goc.submit; }
    if (!bat) { window.filedownload(f.path, f.name, f.type); await ngu(800); return { ten: f.name, cach: 'ten_goc' }; }
    const r = await fetch(bat.url, { credentials: 'include', method: bat.method || 'GET', body: bat.body });
    const b = await r.blob();
    if (!r.ok || !b.size || /text\/html/i.test(b.type)) throw new Error(`tải ${f.name}: HTTP ${r.status}, ${b.size} byte, ${b.type || '?'}`);
    const a = document.createElement('a');
    a.href = URL.createObjectURL(b); a.download = ten_moi; goc.click.call(a);
    await ngu(600); URL.revokeObjectURL(a.href);
    return { ten: ten_moi, cach: 'tien_to' };
  }

  window.ktcTai = async function (ds, { tai_lai = false } = {}) {
    const da = new Set(JSON.parse(localStorage.getItem(SO_NHO) || '[]'));
    const ket_qua = [];
    for (const vb of ds) {
      const row = { doc_id: vb.doc_id, so_ky_hieu: vb.so_ky_hieu, tep_trong_o: [], da_tai: [], loi: '' };
      if (!tai_lai && da.has(vb.doc_id)) { row.loi = 'đã tải trước đó'; ket_qua.push(row); continue; }
      try {
        window.showDocDetail(vb.doc_id, '', '2');
        let tep = null;
        for (let i = 0; i < 40; i++) {                 // cho toi 20 giay trang chi tiet DUNG van ban nay
          await ngu(500);
          const so = so_tren_trang();
          tep = ktcFileChinh(document);
          if (tep && so && sach(so) === sach(vb.so_ky_hieu)) break;
          tep = null;
        }
        if (!tep) throw new Error('không mở được trang chi tiết đúng văn bản hoặc không thấy ô "File đính kèm"');
        if (!tep.length) throw new Error('ô "File đính kèm" rỗng');
        row.tep_trong_o = tep.map(x => x.name);
        for (const f of tep) {
          const kq = await tai_mot(f, tien_to(vb.so_ky_hieu) + f.name);
          row.da_tai.push(kq.ten);
          await ngu(500);
        }
        if (row.da_tai.length !== tep.length) throw new Error(`tải ${row.da_tai.length}/${tep.length} tệp`);
        da.add(vb.doc_id); localStorage.setItem(SO_NHO, JSON.stringify([...da]));
      } catch (e) { row.loi = String(e.message || e); }
      ket_qua.push(row);
    }
    // Ghi ten tep vao ban ghi CSV (window.__kq) de buoc xuat CSV dung luon
    (window.__kq || []).forEach(r => { const k = ket_qua.find(x => x.doc_id === r.doc_id);
      if (k && k.da_tai.length) { r.ten_file = k.tep_trong_o.join(' | '); r.loi = k.loi; } });
    window.__ktc_tai = ket_qua;
    return ket_qua.map(k => `${k.so_ky_hieu}: ${k.loi ? 'LỖI ' + k.loi : k.da_tai.length + ' tệp'}${k.tep_trong_o.length ? ' — ' + k.tep_trong_o.join(' | ') : ''}`).join('\n');
  };
  return 'ktcTai sẵn sàng';
})();
```

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
