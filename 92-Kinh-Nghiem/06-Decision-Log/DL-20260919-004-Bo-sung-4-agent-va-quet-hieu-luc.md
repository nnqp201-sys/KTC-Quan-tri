# DL-20260919-004 — Bổ sung 4 agent (tổng 5) và công cụ quét hiệu lực pháp lý, viện dẫn

**Ngày:** 19/9/2026 · **Người quyết định:** người dùng (chủ dự án)

**Bối cảnh:** plugin mới có 1 agent (`ktc-tu-cai-tien`). Mình đề xuất thêm 3 agent theo tiêu chí:
- việc đọc nhiều tệp, cần ngữ cảnh riêng; hoặc
- việc cần bên thứ hai kiểm độc lập.

Người dùng đồng ý và yêu cầu thêm: *"bổ sung 1 scan kiểm tra hiệu lực pháp lý của văn bản, kiểm tra viện dẫn"*.

**Quyết định — 5 agent:**

| Agent | Việc | Ghi được vào |
|---|---|---|
| `ktc-tu-cai-tien` (đã có) | Đề xuất cải tiến hệ từ nhật ký | `92-Kinh-Nghiem/03-Change-Proposals/` |
| `ktc-kiem-ho-so-don-vi` | Kiểm hồ sơ TB 736 của từng đơn vị; kết luận đủ điều kiện tổng hợp hay trả lại | `30-Ket-Qua/<ngày>/Kiem-Ho-So/` |
| `ktc-tra-cuu-can-cu` | Tra sâu KTC-Database; trả khối căn cứ đúng quy tắc viện dẫn | `30-Ket-Qua/<ngày>/Tra-Cuu-Can-Cu/` |
| `ktc-kiem-san-pham` | Kiểm cuối độc lập: thể thức, số liệu, Task_ID, truy vết | `30-Ket-Qua/<ngày>/Kiem-San-Pham/` |
| `ktc-hieu-luc-vien-dan` | Quét hiệu lực và viện dẫn khi soạn, trước khi giao, và định kỳ quét cả bộ quy tắc | `30-Ket-Qua/<ngày>/Ra-Soat-Hieu-Luc/` |

Cả 5 agent đều **không sửa tệp** (`disallowedTools: Edit`), chỉ tạo báo cáo trong đúng thư mục của mình.
**Không** lặp các reviewer của 897. `legal-reviewer` của 897 vẫn là chốt pháp lý trước trình ký; agent quét hiệu lực
làm sớm hơn và định kỳ.

**Công cụ mới `29-Cong-Cu/tra_hieu_luc.py`**:
- trích văn bản viện dẫn, kể cả viết tắt "QĐ 988/QĐ-CĐKT", "NĐ 30/2020/NĐ-CP";
- tra **tên tệp** trong kho 01–02, không tải cả kho trên Drive (0,7 giây);
- đọc metadata của tệp khớp;
- phân loại: `THAY_THE` · `KHO_GHI_HET_HIEU_LUC` · `CO_TRONG_KHO` · `KHONG_CO_TRONG_KHO` (CẦN XÁC MINH);
- chạy kèm `kiem_vien_dan`.
Công cụ **không tự kết luận hết hiệu lực**; việc xác minh ngoài do agent làm, có ghi nguồn Mức 1.

Plugin chép `tra_hieu_luc.py`, `kiem_vien_dan.py`, `duong_dan.py` vào `scripts/` để agent chạy được ngoài dự án.

**Lỗi khớp nhầm đã sửa khi thử thật (có ca hồi quy `test_tra_hieu_luc.py`):**
- "NĐ 85/2025" khớp tệp "NĐ 275-2025 sửa đổi NĐ 85". Nay số và năm phải đứng liền nhau.
- "TT 36/2026/TT-BXD" khớp "QĐ 36/2026/QĐ-TTg", vì "TT" nằm trong "TTG". Nay loại văn bản phải khớp nguyên từ.
- "Luật Giáo dục" khớp "Luật Phổ biến, giáo dục pháp luật". Nay khớp nguyên cụm tên và ưu tiên cụm đứng trọn.

**Phát hiện thật khi thử** (chỉ báo, không sửa kho): `QD-1951-QD-CDKT…_20260907_v1.docx` dẫn **Luật Xây dựng**. Metadata
kho ghi luật này **hết hiệu lực toàn bộ từ 01/7/2026**, trong khi quyết định ký ngày 07/9/2026. Cần người có thẩm
quyền xem lại căn cứ; có thể đã có Luật Xây dựng mới, cần tra nguồn chính thống.

**Chưa kiểm chứng:** Cowork có chạy agent của plugin hay không. Trong Claude Code thì chạy được.

**Phiên bản:** plugin **0.7.0**. Skill không đổi phiên bản, vì agent nằm ở cấp plugin.
