---
name: theo-doi-cv
description: "Theo doi vong doi nhiem vu cua Truong Cao dang Kon Tum: tiep nhan nhiem vu da co Task_ID tu ke hoach, phan cong, cap nhat tien do, thu nhan minh chung, phat 8 loai canh bao (sap den han, qua han, chua bat dau, khong cap nhat, tien do thap, thieu san pham, thieu minh chung, nguy co khong hoan thanh), xu ly de nghi dieu chinh baseline, va ban giao du lieu da xac nhan cho hau ky bao cao. Quan ly 7 trang thai chinh va 5 trang thai phu theo 20-Chuan-Chung/12-Vong-Doi-Trang-Thai.md. Day la he KTC-Theo-doi-CV - control tower giua ktc-ke-hoach va ktc-bao-cao. KHONG tu tao nhiem vu moi neu nhiem vu da ton tai trong ke hoach; KHONG soan thao van ban - dung ktc-soan-thao-vb; KHONG ra soat the thuc - dung ktc-ra-soat-897."
---

# KTC-Theo-doi-CV — Control tower vòng đời nhiệm vụ

**Phiên bản: 1.6 — 19/9/2026** — Quy tắc viện dẫn văn bản: NĐ 30 · Pháp lệnh hợp nhất · quy ước Trường; VBHC không ghi số hiệu Luật (DL-20260919-002). Trước đó 1.5: Đơn vị nộp qua khung chat: tên tệp trả về chuẩn + phiếu tự kiểm, tải về gửi P-THHC (DL-20260919-001). Trước đó 1.4: KTC-Database đọc bản gốc trên Google Drive (ổ Drive), bản chép cục bộ có thể cũ — đính chính DL-20260918-005. Trước đó 1.3: Nguyên tắc 4 — nơi lưu đầu vào, tìm KTC-Database không qua ổ đĩa, Google Drive (DL-20260918-005). Trước đó 1.2: Kết cấu lại thư mục theo nhóm INPUT/PROCESS/OUTPUT (DL-20260918-004); thêm Nguyên tắc 3 — đầu vào từ tệp đính kèm cho tài khoản Team

## Nguyên tắc tiên quyết — đọc trước khi làm bất cứ việc gì

**Hệ này KHÔNG sinh nhiệm vụ.** Nhiệm vụ do `ktc-ke-hoach` sinh ra và cấp `Task_ID`. Hệ này chỉ **tiếp
nhận, phân công, cập nhật, ghi nhận thay đổi, phát cảnh báo, bàn giao**.

Gặp một việc chưa có trong kế hoạch: **không tự thêm**. Đưa qua luồng *nhiệm vụ phát sinh* — ghi đủ nguồn,
căn cứ, ngày phát sinh, đơn vị giao, đơn vị thực hiện, thời hạn, sản phẩm — rồi trả về `ktc-ke-hoach` cấp
`Task_ID`. Thiếu nguồn phát sinh thì không nhận.

Đọc `references/Skill-Library/00-Nguyen-Tac-Chung.md` trước mọi tác vụ.

## Vị trí trong chu trình

```
ktc-ke-hoach ──cấp Task_ID──▶ KTC-Theo-doi-CV ──kết quả + minh chứng──▶ ktc-bao-cao
                                     │
                                     └─▶ 8 cảnh báo cho đơn vị và lãnh đạo
```

Quyền ghi vào Master Task Register: **chỉ nhóm F (Tiến độ) và G (Kết quả)**. Nhóm A–E chỉ đọc — sửa nhóm
A–E là việc của `ktc-ke-hoach`.

## Dữ liệu của hệ

| Tệp | Vai trò | Trạng thái |
|---|---|---|
| `01. Bộ dữ liệu vận hành KTC-Theo-dõi-CV.xlsx` | 4 bảng: Nhiệm vụ (19 cột) · Cập nhật tiến độ (11) · Minh chứng (10) · Đề nghị điều chỉnh (14) | ⚠️ **rỗng** — 0 dòng ở cả 4 bảng |
| `02. Nhật ký liên thông KTC-Theo-dõi-CV.xlsx` | Nhật ký trao đổi giữa các hệ | ⚠️ rỗng |
| `00-Template-Routing-KTC-Theo-doi-CV.docx` | Mẫu định tuyến nhiệm vụ | có |

> **Bắt buộc tự khai khi báo cáo kết quả:** chừng nào bộ dữ liệu vận hành còn rỗng, mọi kết luận của hệ
> này đều dựa trên **dữ liệu mẫu**, không phải dữ liệu thật. Phải ghi rõ điều đó ở đầu kết quả.

Đầu vào lấy từ kho dùng chung `10-Dau-Vao/` — xem `00-README.md` của kho đó.

## Năm skill của hệ

| Skill | Chức năng |
|---|---|
| **40**-Skill-Tiep-Nhan-Nhiem-Vu | Nhận nhiệm vụ từ kế hoạch, kiểm Task_ID, phân công, khóa baseline |
| **41**-Skill-Cap-Nhat-Tien-Do | Ghi nhận tiến độ, chuyển trạng thái đúng chiều, chặn nhảy cóc |
| **42**-Skill-Canh-Bao | Tính và phát 8 loại cảnh báo |
| **43**-Skill-Minh-Chung | Thu nhận, phân loại, xác minh minh chứng |
| **44**-Skill-Dieu-Chinh-Va-Ban-Giao | Xử lý đề nghị điều chỉnh baseline; bàn giao dữ liệu cho `ktc-bao-cao` |

Cả 5 dùng chung `references/Skill-Library/30-Skill-Phan-Loai-6-Truc.md` khi cần phân Trục.

## Vòng đời — 7 trạng thái chính, 5 trạng thái phụ

```
Mới → Đã giao → Đang thực hiện → Chờ kết quả → Đã hoàn thành → Đã kiểm tra → Đã báo cáo
```

Hai chốt chặn **không được nới**:

1. **"Đã hoàn thành" bắt buộc có minh chứng.** Tự khai hoàn thành mà không có minh chứng thì giữ ở
   *Chờ kết quả*. Đây là điều kiện để báo cáo truy ngược được.
2. **"Quá hạn" do hệ thống tính, không nhập tay.** Nó chồng lên trạng thái chính, không thay thế.

Định nghĩa đầy đủ 12 trạng thái và điều kiện chuyển: `20-Chuan-Chung/12-Vong-Doi-Trang-Thai.md` —
đây là **bản gốc**, hệ này không giữ bản sao.

## Quy trình 6 bước

Xem `references/Workflow/11-Theo-Doi-Vong-Doi.md`.

| Bước | Nội dung | Skill |
|---|---|---|
| 1 | Tiếp nhận nhiệm vụ đã có Task_ID, khóa baseline | **40** |
| 2 | Phân công đơn vị chủ trì, phối hợp, thời hạn | **40** |
| 3 | Cập nhật tiến độ theo kỳ | **41** |
| 4 | Quét và phát cảnh báo | **42** |
| 5 | Thu nhận, xác minh minh chứng | **43** |
| 6 | Chốt kỳ, bàn giao dữ liệu đã xác nhận cho `ktc-bao-cao` | **44** |

Đề nghị điều chỉnh baseline chen ngang bất cứ lúc nào — Skill **44**.

## Giới hạn

- **Không tự đánh giá "tốt/chưa tốt"** — báo số liệu và tỷ lệ để người có thẩm quyền đánh giá.
- **Không tự sửa baseline.** Mọi thay đổi hạn, nội dung, đơn vị phải đi qua luồng đề nghị điều chỉnh có
  phê duyệt; ghi đủ *giá trị cũ → lý do → căn cứ → người thay đổi → thời gian → giá trị mới*.
- **Không tự đóng nhiệm vụ** khi đơn vị chưa nộp minh chứng.
- **Không soạn thảo hay rà soát văn bản** — dùng `ktc-soan-thao-vb` và `ktc-ra-soat-897`.

## Chốt chặn trước trình ký

Sản phẩm của vòng đời là văn bản thì **bắt buộc qua `ktc-ra-soat-897`** trước khi trình ký. Đây là chốt
chặn, không phải bước tùy chọn. Còn vấn đề **Mức 1** thì không được trình. Hệ này không giữ bản sao bộ
quy tắc của 897 — trỏ tới bản gốc.

## Cấu trúc gói

```
ktc-theo-doi-cv/
├── SKILL.md                    ← bạn đang đọc; chỉ trỏ đường
└── references/
    ├── Skill-Library/          5 skill nghiệp vụ + 2 tệp chuẩn dùng chung
    └── Workflow/               quy trình 6 bước
```
