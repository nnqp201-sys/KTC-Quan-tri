# 2A-KTC-Ra-Soat-897 — ktc-ra-soat-897 v4.6.13-KTC (bản bổ sung cá nhân)

**Phiên bản:** v4.6.13-KTC (07/11/2026) — sửa cổng hồ sơ C1–C6, UTF-8 subprocess  
**Cài đặt:** 07/11/2026  
**Mã thư mục:** `2A-` (giữ nguyên từ v4.5)

## Nguồn gốc

| Phiên bản | Nguồn | Ghi chú |
|-----------|-------|---------|
| **v4.6.12** | `ktc-ra-soat-897_v4.6.12.zip` (Hiệu trưởng) | Bản chính thức toàn Trường |

## Thay đổi chính v4.6.12

Căn cứ CHANGELOG.md trong gói:

- **L5:** Sửa lỗi tác giả Comment cũ trong Track Changes — chỉ dấu sửa/Comment đã có trong bản gốc được giữ tên cũ; mọi dấu sửa/Comment mới phải mang tên "KTC Rà soát 897 (AI)"
- Kế thừa v4.6.11: sửa L1–L4 (dấu hiệu chủ đề AI, tác giả Track Changes, mã thoát xac-minh)
- Kế thừa v4.6.10: bỏ hẳn miễn nguồn theo chủ đề, không cần xác nhận
- Kế thừa v4.6.5–v4.6.9: QĐ 2520, nhật ký phạm vi, Bước 8 Track Changes

## Thay thế

- **v4.5 + KI-021:** Bản cá nhân v4.5-ca-nhan.1 (30/10/2026) hết hiệu lực. Các fix N1–N8 của KI-021 đã được P-QLKHCN&HTPT xem xét khi phát triển v4.6.x; không còn lớp bổ sung cá nhân.
- **Decision Log:** `DL-20261030-001-Sua-cong-ho-so-897.md` — trạng thái: ĐÓNG (thay bằng v4.6.4 chính thức)

## Lớp kiểm thuật ngữ pháp lý — chạy SONG SONG, không nhúng vào 897

Lõi v4.6.4 khóa băm từng byte và **không còn lớp bổ sung cá nhân**, nên phép kiểm thuật ngữ
pháp lý (TN01–TN04) được dựng thành lớp độc lập, **không sửa gì trong `ktc-ra-soat-897/`**:

| Thành phần | Đường dẫn |
|---|---|
| Quy tắc gốc | `20-Chuan-Chung/21-Quy-Tac-Thuat-Ngu.md` |
| Công cụ | `29-Cong-Cu/kiem_thuat_ngu.py` |
| Agent | `ktc-kiem-thuat-ngu` |
| Kho nguồn | `KTC-Database/08-Tu-Dien-Phap-Ly` · `07-Hoi-Dap-Chinh-Sach` (chỉ đọc) |

Thứ tự dùng: **đang soạn** → `kiem_thuat_ngu.py` phát hiện sớm (gần đúng, hết hiệu lực nguồn,
không nhất quán) → **trước trình ký** → rà soát 897 đầy đủ. Lớp này **không thay 897**;
còn vấn đề Mức 1 của 897 thì vẫn không được trình.

Giao nhau một điểm: **hỏi đáp chính sách không bao giờ là "Căn cứ"** — đưa vào phần căn cứ là
lỗi **Mức 1** theo 897, giống mọi tài liệu nội bộ, mẫu, checklist.

## Cấu trúc

```
2A-KTC-Ra-Soat-897/
├── 00-README.md
├── .gitattributes                     ← "* -text": giữ nguyên byte
├── SHA256SUMS                         ← băm từng tệp của gói v4.6.12
├── ktc-ra-soat-897-v4.6.12.skill      ← gói .skill v4.6.12
└── ktc-ra-soat-897/                   ← gói v4.6.12 giải nén nguyên
```

## Kiểm lõi

```bash
cd "D:/.CLAUDE code/KTC-Quan-tri/2A-KTC-Ra-Soat-897"
sha256sum -c SHA256SUMS                # kiểm toàn bộ tệp
```

## Cài đặt

- **Tài khoản Team của Trường:** P-QLKHCN&HTPT đã cài (03/11/2026)
- **Tài khoản cá nhân:** Cài skill từ gói zip để đồng bộ với Team

## Khi có bản mới

Thay `ktc-ra-soat-897/` bằng gói mới, sinh lại `LOI-V<phiên bản>.sha256`.

## Nhóm 6 sub-agent điều phối 897 (v4.6.13-KTC)

Nhóm agent **nằm ngoài lõi 897** (không nằm trong `ktc-ra-soat-897/`), dùng để điều phối đợt rà soát
cả bộ hồ sơ nhiều văn bản. Lõi 897 vẫn khóa băm từng byte; các agent này chỉ **gọi** công cụ của lõi.

| Agent | Vai trò | Quyền sửa tệp |
|---|---|---|
| `ktc-897-dieu-phoi` | Điều phối đợt rà soát cả bộ; giao việc song song, tổng hợp, dừng ở chốt chặn | Không |
| `ktc-897-nap-nguon` | Tìm toàn văn trong kho, xử lý PDF ký số / scan; lập danh sách còn thiếu | Chỉ ghi thư mục làm việc |
| `ktc-897-ra-soat-van-ban` | Rà soát chính thức đúng một văn bản (chạy song song mỗi văn bản một agent) | Chỉ ghi báo cáo |
| `ktc-897-sua-the-thuc` | Sửa thể thức, không đổi nội dung, một tệp | Sửa tệp được giao |
| `ktc-897-sua-noi-dung` | Thực hiện bảng sửa/tiếp thu đã được duyệt, một tệp | Sửa tệp được giao |
| `ktc-897-dong-bo-bo-ho-so` | Đối chiếu chéo cả bộ sau sửa; kiểm bản gửi thẩm định | Không |

**Thứ tự đợt rà soát:** nạp nguồn → rà soát (song song) → người dùng duyệt bảng sửa → sửa →
rà soát lại tệp đã sửa → đồng bộ cả bộ → báo người dùng.

**Chốt chặn không được bỏ:**
- Ý kiến thẩm định **không mặc nhiên đúng** — tiếp thu / giải trình do người dùng duyệt.
- Không ghi vào `KTC-Database`, `03-Templates(1)`, `04-Good-Documents`.
- Còn Mức 1 thì **không trình**.

Đường dẫn: `.claude/agents/ktc-897-*.md` và `29-Cong-Cu/plugin_src/agents/ktc-897-*.md`.
