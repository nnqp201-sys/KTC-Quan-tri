# Đo chi phí context — ktc-quan-tri-1.3.0.zip → ktc-quan-tri-1.3.1.zip

Token ước tính = ký tự / 4 (cùng quy ước báo cáo thẩm định lần 3); dùng để **so sánh**, không phải số tính phí.
Phần nạp đầu phiên đo trên nhật ký thật của dự án, cùng thời điểm, bằng script `nap` của từng gói.

| Hạng mục | Khi nào nạp | Cũ (ký tự / ~token) | Mới (ký tự / ~token) | Giảm |
|---|---|---:|---:|---:|
| Mô tả 8 skill + 7 agent | mọi phiên | 10,446 / 2,612 | 10,446 / 2,612 | 0% |
| Phần nạp đầu phiên (`nap`) | mọi phiên trong dự án | 7,738 / 1,934 | 4,341 / 1,085 | 44% |
| Khối chuẩn chung, cộng 15 bản sao | khi skill/agent được gọi | 70,410 / 17,602 | 38,387 / 9,597 | 45% |
| Khối chuẩn chung, 1 bản | mỗi lần gọi 1 skill/agent | 4,694 / 1,174 | 2,564 / 641 | 45% |
| Thân 8 SKILL.md + 7 agent, cộng | khi được gọi | 161,194 / 40,298 | 128,053 / 32,013 | 21% |

## Từng skill/agent (ký tự)

| Tệp | Cũ | Mới | Khối cũ | Khối mới |
|---|---:|---:|---:|---:|
| `agents/ktc-hieu-luc-vien-dan.md` | 8,936 | 6,811 | 4,694 | 2,564 |
| `agents/ktc-kiem-ho-so-don-vi.md` | 8,163 | 6,038 | 4,694 | 2,564 |
| `agents/ktc-kiem-san-pham.md` | 7,877 | 5,752 | 4,694 | 2,564 |
| `agents/ktc-tra-cuu-can-cu.md` | 7,367 | 5,242 | 4,694 | 2,564 |
| `agents/ktc-tu-cai-tien.md` | 8,153 | 6,028 | 4,694 | 2,564 |
| `agents/ktc-tu-hoc.md` | 8,577 | 6,452 | 4,694 | 2,564 |
| `agents/ktc-xac-minh-minh-chung.md` | 8,051 | 5,926 | 4,694 | 2,564 |
| `skills/bao-cao/SKILL.md` | 14,818 | 11,427 | 4,694 | 2,491 |
| `skills/ke-hoach/SKILL.md` | 12,798 | 10,673 | 4,694 | 2,564 |
| `skills/kpi-lap-ke-hoach/SKILL.md` | 13,675 | 11,550 | 4,694 | 2,564 |
| `skills/kpi-tu-danh-gia/SKILL.md` | 13,449 | 11,324 | 4,694 | 2,564 |
| `skills/quan-tri/SKILL.md` | 15,464 | 13,339 | 4,694 | 2,564 |
| `skills/soan-thao-vb/SKILL.md` | 14,871 | 12,746 | 4,694 | 2,564 |
| `skills/the-thuc/SKILL.md` | 8,256 | 6,131 | 4,694 | 2,564 |
| `skills/theo-doi-cv/SKILL.md` | 10,739 | 8,614 | 4,694 | 2,564 |

Ngưỡng vận hành (ChatGPT L3 P1-1): phần nạp đầu phiên ≤ 1.500 token ≈ 4.500 ký tự — **ĐẠT** (4,341 ký tự).
Mô tả skill/agent **chưa rút gọn** trong 1.3.1: mô tả quyết định việc kích hoạt skill; rút gọn cần đo lại tỷ lệ kích hoạt đúng/sai trên bộ ca nghiệm thu — để sau thí điểm (Báo cáo tiếp thu lần 3).
