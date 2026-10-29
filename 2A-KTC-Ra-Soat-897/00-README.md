# 2A-KTC-Ra-Soat-897 — Bản tích hợp cá nhân "ktc-ra-soat-897 v4.5"

**Mã thư mục tạm** `2A-` (người giao có thể đổi). **Lệnh giao:** `30-Ket-Qua/2026-10-29/Lenh/LENH-Tich-hop-KTC-Ra-Soat-897-v4.5.md`.
**Quyết định:** `92-Kinh-Nghiem/06-Decision-Log/DL-20261029-001-Ra-Soat-897-v4.5-ca-nhan.md`.

## Nguồn gốc

| Vai trò | Gói gốc (trong `99-Luu-Tru/KTC-Ra-Soat-897-goc/`) | SHA256 |
|---|---|---|
| **Nền (lõi)** — bản Trường ban hành theo TB 1206/TB-CĐKT | `ktc-ra-soat-897-v4.5.skill` | `562600294d76be9d36d227f7d67558df4c9fa616d1e8777626d5547afb1cd9b2` |
| Lấy mô-đun (lớp bổ sung) | `KTC-Ra-soat-897-v3.0.zip` | `ec65b248cfdb15937c5a34f6354a99d03017cbd4ca5d035d03dec75edf21448d` |
| Lấy mô-đun, bộ hồi quy, bộ nhớ | `KTC-Ra-Soat-897-v2.25-Cai-tien.zip` | `168da17688e0cf3b51c6fd1e2048f847a8dd0a319ac0611c2c743f385851a75d` |

## Nguyên tắc: LÕI NGUYÊN BẢN + LỚP BỔ SUNG

- **Lõi v4.5 giữ nguyên từng byte**: `tools/`, `references/Quy-Tac-KTC/`, `references/Kho-Du-Lieu-897/`, `references/Checklist/`,
  `references/Prompt-Library/`, `references/Skill-Library/`, `assets/`, và mọi nội dung `SKILL.md` từ đầu đến hết mục
  "Quan hệ với hệ khác và giới hạn". Căn cứ: TB 1206/TB-CĐKT mục 6 — không tự ý sửa đổi bộ quy tắc của Skill; chỉ đạo của
  Hiệu trưởng 28/10/2026 — mọi báo cáo rà soát chạy trên v4.5.
- **Ngoại lệ duy nhất của `SKILL.md`**: (1) dòng tiêu đề số 1 đổi thành "v4.5 (lõi nguyên bản…) + lớp bổ sung cá nhân";
  (2) thêm mục `## Lớp bổ sung cá nhân (không thay đổi kết luận v4.5)` ở **cuối tệp**.
- **Lớp bổ sung** chỉ nằm trong `ktc-ra-soat-897/references/Bo-Sung-Ca-Nhan/` (v2.25, v3.0) và chỉ sinh **ghi chú tham khảo**
  `[Bổ sung – tham khảo]`. **Không** thêm mã lỗi, **không** đổi mức, **không** đổi nhãn trình ký, **không** nới cổng hồ sơ.
- Báo cáo chạy trên bản này phải cho **cùng nhãn, cùng số lỗi theo mức** như bản Trường với cùng hồ sơ.
- Gặp tình huống buộc phải sửa lõi → **dừng, báo người giao**.

## Cấu trúc

```
2A-KTC-Ra-Soat-897/
├── 00-README.md
├── .gitattributes                     ← "* -text": giữ nguyên byte, không đổi xuống dòng khi git checkout
├── LOI-V45.sha256                     ← băm từng tệp của gói v4.5 gốc (137 tệp). KHÔNG sửa tay
├── ktc-ra-soat-897/                   ← gói v4.5 giải nén nguyên + references/Bo-Sung-Ca-Nhan/
└── ktc-ra-soat-897-v4.5-ca-nhan.skill ← sản phẩm đóng gói (sinh bởi dong_goi_ra_soat_897.py) + SHA256SUMS
```

## Kiểm lõi và đóng gói

```bash
python 29-Cong-Cu/dong_goi_ra_soat_897.py            # kiểm lõi khớp LOI-V45.sha256, rồi đóng gói; mã thoát 0/1
python 29-Cong-Cu/dong_goi_ra_soat_897.py --chi-kiem # chỉ kiểm, không đóng gói
python 29-Cong-Cu/dong_bo_kho_897.py                 # đối chiếu kho_manifest.json với KTC-Database (chỉ đọc)
```

Phép kiểm "C-897" trong `29-Cong-Cu/kiem_tra_he_thong.py` gọi cùng bước kiểm lõi.

## Cài đặt

Cài trên **tài khoản Claude cá nhân**. **Không** cài vào tài khoản Team của Trường (đã có bản chính thức cùng tên `ktc-ra-soat-897`;
hai skill trùng tên trong một tài khoản sẽ tranh kích hoạt).

## Khi có bản mới của Trường

Thay `ktc-ra-soat-897/` bằng gói mới, sinh lại `LOI-V45.sha256` từ gói gốc mới (đổi tên theo phiên bản), rà lại lớp bổ sung
theo `Bo-Sung-Ca-Nhan/00-Doi-Chieu.md`.
