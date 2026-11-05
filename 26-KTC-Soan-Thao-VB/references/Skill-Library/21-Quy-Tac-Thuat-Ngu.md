# 21 — Quy tắc dùng thuật ngữ pháp lý

**Bản gốc.** Các hệ giữ bản sao khi đóng gói; sửa ở đây trước.

Áp dụng cho mọi sản phẩm soạn thảo, rà soát, báo cáo của KTC-Quan-tri.

## 1. Nguồn chuẩn

| Kho | Nội dung | Vai trò |
|---|---|---|
| `KTC-Database/08-Tu-Dien-Phap-Ly` | 1370+ thuật ngữ, 13 lĩnh vực, có hiệu lực nguồn | Định nghĩa chuẩn |
| `KTC-Database/07-Hoi-Dap-Chinh-Sach` | Hỏi đáp của Bộ, ngành | **Tham khảo** |

Khi hai kho mâu thuẫn với văn bản gốc trong `01-Legal-Documents`, **lấy theo văn bản gốc**.
Từ điển là bản tổng hợp, không thay văn bản quy phạm pháp luật.

## 2. Bốn phép kiểm TN

| Mã | Nội dung | Mức |
|---|---|---|
| **TN01** | Cụm từ gần giống thuật ngữ chuẩn nhưng viết khác | 3 |
| **TN02** | Thuật ngữ lấy từ văn bản **hết hiệu lực** | 2 |
| **TN02** | Thuật ngữ từ văn bản **đã sửa đổi** — chưa đối chiếu bản hợp nhất | 3 |
| **TN02b** | Kho chưa xác minh nguồn — hạn chế của kho | 4 |
| **TN03** | Cùng khái niệm gọi bằng nhiều thuật ngữ trong một văn bản | 3 |
| **TN04** | Có hỏi đáp chính sách liên quan | 4 |

Công cụ: `29-Cong-Cu/kiem_thuat_ngu.py` · Agent: `ktc-kiem-thuat-ngu`

```bash
python 29-Cong-Cu/kiem_thuat_ngu.py "<tệp>" --xuat "30-Ket-Qua/<ngày>/kiem-thuat-ngu/<tên>.md"
```

## 3. Ba ràng buộc bất biến

1. **Hỏi đáp chính sách không bao giờ là "Căn cứ".** Đưa hỏi đáp vào phần căn cứ của văn bản
   hành chính là **lỗi Mức 1** theo KTC-Ra-Soat-897 — giống mọi tài liệu nội bộ, mẫu, checklist.
   Hỏi đáp chỉ dùng để hiểu cách cơ quan có thẩm quyền đang áp dụng quy định.

2. **Định nghĩa viện dẫn phải khớp văn bản còn hiệu lực.** Trích định nghĩa từ văn bản đã bị
   thay thế là lỗi Mức 2. Luật đã sửa đổi thì viện dẫn theo quy tắc văn bản hợp nhất
   (`17-Quy-Tac-Vien-Dan.md`).

3. **Một khái niệm — một thuật ngữ** trong toàn văn bản. Không đổi cách gọi giữa các mục.

## 4. Thứ tự dùng khi soạn thảo

```
Đang soạn  →  tra Từ điển lấy định nghĩa chuẩn
           →  kiem_thuat_ngu.py phát hiện sớm
           →  sửa khi còn dễ sửa
Trước ký   →  KTC-Ra-Soat-897 (chốt chặn, không thay thế được)
```

Lớp kiểm thuật ngữ chạy **sớm và song song**, không thay 897.

## 5. Khi kho thiếu thuật ngữ

Kho chỉ đọc. Thiếu hoặc sai thì:
- Bỏ tài liệu nguồn vào `KTC-Database/08-Tu-Dien-Phap-Ly/input/` để routine thu thập xử lý, hoặc
- Viết đề xuất ra `30-Ket-Qua/<ngày>/` để người có thẩm quyền áp vào kho.

Không tự ghi vào kho — hook `ktc_guard` chặn mọi thao tác ghi.

## 6. Phân loại thuật ngữ

6 Trục TB 817 (`30-Skill-Phan-Loai-6-Truc.md`) và 13 lĩnh vực:

`giao-duc` · `hssv` · `vien-chuc` · `tien-luong` · `thue-phi` · `bao-hiem` · `dau-thau` ·
`tai-san` · `xay-dung` · `thi-dua` · `khcn` · `hanh-chinh` · `khac`

Lĩnh vực `khac` dành cho triết học, lý luận chính trị, văn hóa, đối ngoại, an ninh và các
lĩnh vực liên ngành — ghi rõ chủ đề cụ thể trong cột Ghi chú.

Tra cứu chuyên sâu: agent `ktc-tu-dien-phap-ly` (tự điều phối sang 13 sub-agent `ktc-tdpl-*`).
