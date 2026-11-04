# KTC-Soan-Thao-VB — Hệ soạn thảo văn bản hành chính

**Lập:** 14/9/2026 · **Kế thừa từ:** `KTC-DIS-Tong-Hop-VB` (thu hẹp có chủ đích)
**Căn cứ quyết định:** `92-Kinh-Nghiem/06-Decision-Log/DL-20260914-001-Vai-tro-KTC-DIS-Tong-Hop-VB.md`

## Hệ này làm gì

Soạn thảo văn bản hành chính **mới** cho Trường: Quyết định · Kế hoạch · Thông báo · Báo cáo · Tờ trình ·
Công văn · Biên bản — theo 6 lĩnh vực nghiệp vụ (đào tạo, tuyển sinh, tổ chức cán bộ, tài chính, HSSV,
bảo đảm chất lượng) và văn bản đối ngoại. Kèm chuẩn hóa văn phong, tạo dàn ý, trích xuất thông tin, gắn
metadata, và vòng đời trình ký – ban hành – lưu trữ.

## Hệ này KHÔNG làm gì

| Việc | Chuyển sang |
|---|---|
| Rà soát dự thảo trước khi trình ký | `ktc-ra-soat-897` |
| Dựng kế hoạch công tác theo 6 Trục | `ktc-ke-hoach` |
| Tổng hợp báo cáo công tác định kỳ | `ktc-bao-cao` |
| Nạp, phân loại, quản trị kho dữ liệu | `ktc-database` |
| Văn bản của Đảng (hệ quy chiếu B) | `ktc-ra-soat-897` |

## Vì sao thu hẹp

Bản tiền nhiệm `KTC-DIS-Tong-Hop-VB` tự khai là *"hệ tổng hợp, đầy đủ nhất"* và hướng dẫn *"chưa rõ dùng hệ
nào thì dùng hệ này"*. Để làm được điều đó, nó **sao chép bộ quy tắc rà soát** của `ktc-ra-soat-897`.

Khảo sát md5 ngày 14/9/2026:

| Phép đo | Kết quả |
|---|---|
| Tệp trùng tên với hệ khác | 34/76 |
| Trong đó trùng md5 (giống y hệt) | **chỉ 8** |
| Tệp trùng tên với `ktc-ra-soat-897` khác nội dung | 28 |
| Trong đó **897 mới hơn** | **28/28 — không ngoại lệ** |
| `03-Phap-Ly.md` | 357 b so với **10.513 b** của bản gốc |

Nghĩa là người dùng phân vân sẽ bị đẩy tới **bộ quy tắc rà soát cũ nhất và sơ sài nhất**. Tuyên bố "đầy đủ
nhất" đúng về số tệp nhưng sai về chất lượng.

> **Quy tắc rút ra, áp cho cả họ skill KTC:** không hệ nào được sao chép bộ quy tắc của hệ khác để "cho đầy
> đủ". Bản sao không có cơ chế đồng bộ **chắc chắn sẽ lệch**, và bản lệch nguy hiểm hơn bản thiếu vì nó
> trông như có. Ghi ở `references/Workflow/06-Cap-Nhat.md` Bước 3.

**Ngoại lệ đã biết:** 5 tệp dùng chung bắt buộc nhân bản vào `references/Skill-Library/` vì `.skill` là zip
tự chứa. Bản gốc ở `KTC-Quan-tri/20-Chuan-Chung/`, nhân bản lại tại bước đóng gói.

## Cấu trúc

```
26-KTC-Soan-Thao-VB/
├── SKILL.md                      Bộ định tuyến — đọc trước
├── ktc-soan-thao-vb.skill        Gói chạy trên Claude Chat/Cowork
├── assets/                       Mẫu prompt do Lãnh đạo Trường ban hành
└── references/
    ├── Skill-Library/            29 tệp — soạn thảo, theo loại VB, theo nghiệp vụ, 5 tệp dùng chung
    ├── Prompt-Library/           Soạn thảo (7) · Chuẩn hóa (7) · 7 thư mục nghiệp vụ · trích xuất, dàn ý, metadata
    ├── Workflow/                 Soạn thảo → Trình ký → Ban hành → Lưu trữ → Cập nhật
    ├── Knowledge-Graph/          Entities · Relations · Rules · Mappings · Use-Cases
    ├── KTC-Regulations-Reference/  TB 817 — nội hàm 6 Trục
    ├── Legal-Reference/          QĐ 399-QĐ/TW — thể thức văn bản Đảng (tham chiếu)
    ├── Nguyen-Tac/               Quy tắc khai thác Internet
    └── Input-Output/             Giới hạn thật của Drive connector
```

## Bốn nguyên tắc soạn thảo bắt buộc

Đặc tả đầy đủ ở `KTC-Quan-tri/20-Chuan-Chung/14-Nguyen-Tac-Soan-Thao-Bat-Bien.md`:

1. **Phát triển từ văn bản cùng loại đã ban hành**, không dựng từ mẫu trống.
2. **Bật Track Changes** khi soạn trên văn bản đã có, xuất phát từ chính tệp gốc.
3. **Dùng bộ quy tắc `ktc-ra-soat-897` ngay từ lúc bắt đầu viết.**
4. **`KTC-Database` là cơ sở dữ liệu tham mưu** — tra sâu chiến lược, đề án, chuyên đề.

## Việc còn lại

- **Hệ cũ `KTC-DIS-Tong-Hop-VB/` vẫn còn nguyên** — theo quy ước của dự án, tệp trên Drive chỉ do người
  dùng xóa thủ công. Danh sách tệp cần dọn: `30-Ket-Qua/2026-09-14/Danh-muc-can-don-KTC-DIS-Tong-Hop-VB.md`.
- Sau khi xác nhận hệ mới chạy đúng trên Claude Chat, xóa hệ cũ để tránh hai hệ song song.
- `Knowledge-Graph/06-Metadata.md` còn sơ sài (187 byte) — chưa hoàn thiện.
