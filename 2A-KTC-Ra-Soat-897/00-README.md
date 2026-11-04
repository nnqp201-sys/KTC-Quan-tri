# 2A-KTC-Ra-Soat-897 — ktc-ra-soat-897 v4.6.4 (bản chính thức)

**Phiên bản:** v4.6.4 (03/11/2026) — Hiệu trưởng phê duyệt chính thức  
**Cài đặt:** 04/11/2026 theo thông báo P-QLKHCN&HTPT  
**Mã thư mục:** `2A-` (giữ nguyên từ v4.5)

## Nguồn gốc

| Phiên bản | Nguồn | Ghi chú |
|-----------|-------|---------|
| **v4.6.4** | `ktc-ra-soat-897_v4.6.4_DaPheDuyet.zip` (P-QLKHCN&HTPT) | Bản chính thức toàn Trường |

## Thay đổi chính v4.6.4

Căn cứ CHANGELOG.md trong gói:

- **Q1:** Ma trận đối chiếu AI gồm thêm QĐ 2487/QĐ-CĐKT (Danh mục AI)
- **Q2:** Đối chiếu Danh mục AI — ngoài/trái → DC-01; rộng hơn → DC-03; tên/mức khác → DC-06
- **Q3:** Lưu ý bảo mật dẫn thêm QĐ 2487 — Claude thuộc Danh mục, dữ liệu theo QĐ 2307
- **Q4:** Kho v4.3 bổ sung Luật An ninh mạng 116, Luật GDNN 124, Luật AI 134 (10/12/2025)
- **Q5:** Cổng `--xac-nhan-toan-van` cho văn bản nguồn rất ngắn
- **Kỹ thuật:** D2 (--kho khác Kho gói → CHẶN), D10 (so sánh đúng tệp), F01-F11 sửa lỗi

## Thay thế

- **v4.5 + KI-021:** Bản cá nhân v4.5-ca-nhan.1 (30/10/2026) hết hiệu lực. Các fix N1–N8 của KI-021 đã được P-QLKHCN&HTPT xem xét khi phát triển v4.6.x; không còn lớp bổ sung cá nhân.
- **Decision Log:** `DL-20261030-001-Sua-cong-ho-so-897.md` — trạng thái: ĐÓNG (thay bằng v4.6.4 chính thức)

## Cấu trúc

```
2A-KTC-Ra-Soat-897/
├── 00-README.md
├── .gitattributes                     ← "* -text": giữ nguyên byte
├── LOI-V464.sha256                    ← băm từng tệp của gói v4.6.4 (147 tệp)
└── ktc-ra-soat-897/                   ← gói v4.6.4 giải nén nguyên
```

## Kiểm lõi

```bash
cd "D:/.CLAUDE code/KTC-Quan-tri/2A-KTC-Ra-Soat-897"
sha256sum -c LOI-V464.sha256           # kiểm toàn bộ 147 tệp
```

Phép kiểm "C-897" trong `29-Cong-Cu/kiem_tra_he_thong.py` cần cập nhật để đọc `LOI-V464.sha256`.

## Cài đặt

- **Tài khoản Team của Trường:** P-QLKHCN&HTPT đã cài (03/11/2026)
- **Tài khoản cá nhân:** Cài skill từ gói zip để đồng bộ với Team

## Khi có bản mới

Thay `ktc-ra-soat-897/` bằng gói mới, sinh lại `LOI-V<phiên bản>.sha256`.
