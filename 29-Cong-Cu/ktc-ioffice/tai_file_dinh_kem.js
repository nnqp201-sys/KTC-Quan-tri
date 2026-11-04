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
