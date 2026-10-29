---
name: ktc-trich-nhiem-vu
description: Trích nhiệm vụ chi tiết từ nội dung văn bản giao việc (Thông báo kết luận TB-CĐKT, Kế hoạch KH-CĐKT) của Trường Cao đẳng Kon Tum vào Master Task Register — AI đọc toàn văn, script kiểm, người duyệt, nạp, tổng hợp. Dùng khi người dùng nói "trích nhiệm vụ", "lấy nhiệm vụ trong văn bản", "nạp nhiệm vụ vào Master", "tổng hợp nhiệm vụ theo đơn vị", sau khi đã chạy Cap-nhat-CSDL.bat.
---

# Trích nhiệm vụ từ văn bản giao việc → Master Task Register

Chạy trong **Claude Code / Cowork trên máy** có thư mục `KTC-Quan-tri`. Quy trình 6 bước; skill này lo bước 2–6.

```
1 Thu thập (ktc-ioffice + Cap-nhat-CSDL.bat) → 2 AI trích → 3 Script kiểm → 4 Người duyệt → 5 Nạp Master → 6 Tổng hợp
```

## Nguyên tắc bất biến

1. **AI trích, người duyệt.** Không nạp Master khi chưa có quyết định của người duyệt. Không tự điền cột "Quyết định".
2. **Không bịa.** Mọi nhiệm vụ phải có `Trich_Dan` là câu **nguyên văn** trong văn bản và `Dong` là số dòng `L…` thật. Script sẽ bắt mọi trích dẫn không có trong văn bản.
3. **Không bỏ im lặng.** Mục nào trong phần giao việc không lấy làm nhiệm vụ → ghi vào `Loai_Tru` kèm lý do.
4. **Mã đơn vị chỉ dùng 11 mã chuẩn** (`20-Chuan-Chung/13-Bang-Ma-Don-Vi.md`). Không có mã → để trống `Don_Vi_Chu_Tri`, ghi nguyên văn vào `Don_Vi_Chu_Tri_Goc`.
5. **Không ép phân loại.** `Ma_NV_Chuan` chỉ điền khi khớp rõ `A01`–`S04`; không chắc → trống.
6. **Dự thảo văn bản cần trình ký phải qua rà soát.** Khi nhiệm vụ trích ra là "dự thảo văn bản cần trình ký", sản phẩm phải qua `ktc-ra-soat-897` v4.5 (`2A-KTC-Ra-Soat-897/`) trước khi đánh dấu hoàn thành.

## Bước 2 — Chuẩn bị và AI trích

```bash
python 29-Cong-Cu/kiem_trich_nhiem_vu.py --chuan-bi
```
In danh sách văn bản chờ trích và ghi toàn văn có số dòng vào `29-Cong-Cu/_trung_gian/van-ban/<SO>.txt`
(đoạn văn, bảng `[Bảng b.r]`, phụ lục Excel; số mục tự động của Word đã được dựng lại).

Với **từng** tệp `.txt`: đọc **toàn bộ**, rồi ghi `30-Ket-Qua/<YYYY-MM-DD>/trich-nhiem-vu/<SO>.json` theo khuôn
dưới. Mẫu chuẩn đã duyệt tay: `29-Cong-Cu/ktc-trich-nhiem-vu/vi-du/1092-TB-CDKT.json` — **đọc mẫu trước khi trích văn bản đầu tiên**.

### Khuôn JSON

```json
{
 "So_Ky_Hieu": "1092/TB-CĐKT", "Ngay_Ban_Hanh": "28/09/2026", "Co_Quan": "Trường Cao đẳng Kon Tum",
 "Tep": "<tên tệp chính>", "Pham_Vi_Giao_Viec": [26, 38],
 "Nhiem_Vu": [{
   "Ma_Tam": "N3", "Parent": "",
   "Ten_Nhiem_Vu": "Tham mưu kế hoạch triển khai Thông tư 76/2026/TT-BGDĐT (Quy chế tuyển sinh GDNN)",
   "Mo_Ta": "…", "San_Pham_Yeu_Cau": "Kế hoạch triển khai thực hiện Thông tư 76/2026/TT-BGDĐT", "So_Luong": null,
   "Don_Vi_Chu_Tri": "P-QLDT", "Don_Vi_Chu_Tri_Goc": "Phòng QLĐT&BĐCL",
   "Don_Vi_Phoi_Hop": "P-QLKH", "Don_Vi_Phoi_Hop_Goc": "phòng QLKHCN&HTPT", "Nguoi_Chi_Dao": "",
   "Han_Hoan_Thanh": "16/10/2026", "Ky_Ke_Hoach": "2026-T10",
   "Can_Cu_Dieu_Khoan": "II.3 gạch 1", "Dong": [29, 30],
   "Truc": 1, "Noi_Ham": "Trục 1 – (2) Tuyển sinh", "Ma_NV_Chuan": "",
   "Trich_Dan": "tham mưu kế hoạch triển khai thực hiện Thông tư số 76/2026/TT-BGDĐT",
   "Do_Tin_Cay": "Cao", "Ghi_Chu": ""
 }],
 "Loai_Tru": [{"Dong": [37], "Noi_Dung": "…", "Ly_Do": "Lưu ý chung, không có sản phẩm, không có hạn"}]
}
```

### Quy tắc trích (đọc kỹ — đây là phần quyết định chất lượng)

**Phạm vi** `Pham_Vi_Giao_Viec` = dòng đầu–dòng cuối của phần giao việc (TB: mục "Kế hoạch công tác thời gian
tới / Nhiệm vụ…"; KH: "Nội dung", "Nhiệm vụ, giải pháp", "Tổ chức thực hiện", bảng phân công, phụ lục).
Không lấy phần "Đánh giá kết quả tuần trước", "Mục đích, yêu cầu", "Căn cứ".

**Hạt nhiệm vụ:**
1. Một nhiệm vụ = **một đơn vị chủ trì + một sản phẩm/kết quả**.
2. Gạch đầu dòng là **các bước của cùng một sản phẩm** → gộp vào một nhiệm vụ, chi tiết vào `Mo_Ta`.
   Gạch đầu dòng là **sản phẩm khác nhau** (như 4 kế hoạch triển khai 4 văn bản khác nhau) → tách riêng.
3. Một câu giao cho **nhiều đơn vị làm phần riêng** → mỗi đơn vị một nhiệm vụ, cùng `Parent` (nhiệm vụ tổng `P1`).
   "Phòng A chủ trì, phối hợp B, C" → **một** nhiệm vụ, B và C vào phối hợp.
4. Tiêu đề đơn vị ("3. Phòng QLĐT&BĐCL:") là chủ thể của các gạch bên dưới — đưa số dòng tiêu đề vào `Dong`.
5. KH có **bảng phân công/phụ lục** → bảng là nguồn chính, mỗi hàng nội dung là một ứng viên nhiệm vụ; hàng
   tiêu đề nhóm (gộp ô) không phải nhiệm vụ.
6. **Loại trừ** (ghi `Loai_Tru`): lưu ý/nhắc nhở chung không sản phẩm; nội dung chỉ để biết; mục đích, yêu cầu.

**Trường:**
- `Ten_Nhiem_Vu`: động từ + đối tượng, ≤ 25 từ, có số hiệu văn bản liên quan nếu có.
- `San_Pham_Yeu_Cau`: văn bản/hồ sơ/sự kiện cụ thể đầu ra. Không suy ra được → `THIEU_DU_LIEU`.
- `Han_Hoan_Thanh`: `dd/mm/yyyy`, hoặc `Tháng m/yyyy`, `Quý IV/2026` nếu văn bản chỉ ghi vậy. **Ngày ban hành của văn
  bản được viện dẫn không phải hạn.** Thời điểm tổ chức họp/sự kiện là hạn của việc chuẩn bị. Không ghi hạn → để trống.
- `Ky_Ke_Hoach`: `2026-T10` theo tháng của hạn; không có hạn → tháng ban hành.
- `Truc`/`Noi_Ham`: theo `20-Chuan-Chung/30-Skill-Phan-Loai-6-Truc.md`; `Noi_Ham` bắt đầu bằng `Trục <n> – (<số>) <tên>`.
- `Don_Vi_Phoi_Hop`: chỉ mã chuẩn, ngăn bởi `;`; nhóm chung ("các khoa", "các đơn vị") → chỉ ghi ở `_Goc`.
- `Do_Tin_Cay`: `Cao` / `Trung bình` / `Thấp` — hạ mức khi phải suy luận sản phẩm, hạn, chủ trì; ghi lý do ở `Ghi_Chu`.

**Tự kiểm trước khi lưu JSON:** mọi dòng đánh số/gạch đầu trong phạm vi đều thuộc `Dong` của một nhiệm vụ
hoặc của một `Loai_Tru`.

## Bước 3 — Kiểm

```bash
python 29-Cong-Cu/kiem_trich_nhiem_vu.py
```
Lập `21-Master-Task-Register/Cho-duyet_<ngày>.xlsx` (sheet Chờ duyệt · Văn bản · Loại trừ).
- **ĐỎ** (nghi bịa, sai mã, sai cấu trúc, sót dòng): AI **sửa JSON rồi chạy lại** cho đến hết ĐỎ. Không chuyển cho người duyệt khi còn ĐỎ.
- **VÀNG**: để người duyệt xem — đặc biệt `CÓ THỂ ĐÃ XONG: <số KH>` (nhiệm vụ "tham mưu kế hoạch X" mà KH X đã ban hành) và `CÓ THỂ TRÙNG`.
Chạy lại an toàn: quyết định người duyệt đã nhập được giữ nguyên.

## Bước 4 — Người duyệt (không phải AI)

Báo người dùng mở sổ chờ duyệt, cột **Quyết định**: `Đồng ý` · `Sửa` (sửa thẳng ô rồi ghi Sửa) · `Loại`.
Nhiệm vụ đã có văn bản kết quả: ghi **Ghi chú duyệt** = `đã xong <số VB>` (vd `đã xong 1007/KH-CĐKT`).

## Bước 5 — Nạp

```bash
python 29-Cong-Cu/nap_master.py --nguoi "<tên người duyệt>" --thu    # xem trước
python 29-Cong-Cu/nap_master.py --nguoi "<tên người duyệt>"
```
Cấp Task_ID `KTC-<năm>-<kỳ>-<5 số>` liên tục toàn Trường, ghi lịch sử, sao lưu Master, ghi Task_ID ngược vào sổ duyệt. Không nạp trùng.

## Bước 6 — Tổng hợp

```bash
python 29-Cong-Cu/tong_hop_nhiem_vu.py --ngay 7
```
→ `30-Ket-Qua/<ngày>/tong-hop/Tong-hop-nhiem-vu_<ngày>.xlsx`: theo đơn vị · đến hạn · quá hạn · theo Trục.

## Báo cáo cuối phiên (tiếng Việt, ngắn)

Số văn bản trích · số nhiệm vụ · số loại trừ · còn ĐỎ/VÀNG gì · đường dẫn sổ chờ duyệt · việc người dùng cần làm tiếp.
