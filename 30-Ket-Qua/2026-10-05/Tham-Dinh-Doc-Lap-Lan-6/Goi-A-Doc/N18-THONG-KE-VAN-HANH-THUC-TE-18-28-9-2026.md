<!-- N18: chép nguyên văn từ `THONG-KE-VAN-HANH-THUC-TE-20260918-20260928.md` (sha256 f467c831d048ee8d6bd7a03b8185d5af7fbec99a0ba97381af79604aafcabfb4) -->

# Thống kê vận hành thực tế Bộ công cụ KTC-Quan-tri (2026-09-18 → 2026-09-28)

Nguồn: nhật ký tự động `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/` (chỉ thông tin mô tả — không có nội dung lời nhắn,
câu lệnh), sản phẩm trong `30-Ket-Qua/`, lịch sử git. Sinh bằng `29-Cong-Cu/thong_ke_van_hanh.py` (lặp lại được).
**Phạm vi:** vận hành của người phụ trách xây dựng trên Claude Code (máy Phòng TH-HC&QT), việc thật của Phòng —
**không** phải thí điểm tại các đơn vị; không suy ra kết quả cho Claude (trò chuyện), Cowork.

## 1. Tổng quan

| Chỉ số | Giá trị |
|---|---:|
| Số ngày có làm việc | 11 |
| Số phiên làm việc | 38 |
| Số thao tác công cụ | 2,274 |
| Số lượt yêu cầu của người dùng | 103 |
| Thao tác báo lỗi (hook ghi nhận) | 0 |
| Lần cập nhật mã nguồn (git) | 93 |
| Tín hiệu học (sửa sai / quy ước / quyết định) | 10 / 22 / 18 |

## 2. Theo ngày

| Ngày | Phiên | Thao tác |
|---|---:|---:|
| 2026-09-18 | 6 | 112 |
| 2026-09-19 | 7 | 266 |
| 2026-09-20 | 8 | 148 |
| 2026-09-21 | 5 | 114 |
| 2026-09-22 | 2 | 93 |
| 2026-09-23 | 4 | 86 |
| 2026-09-24 | 4 | 290 |
| 2026-09-25 | 15 | 266 |
| 2026-09-26 | 7 | 282 |
| 2026-09-27 | 3 | 482 |
| 2026-09-28 | 2 | 135 |

## 3. Công cụ, kỹ năng, tác tử được gọi

| Loại | Số lần |
|---|---:|
| Bash | 1834 |
| Edit | 217 |
| Write | 179 |
| Skill | 17 |
| PowerShell | 17 |
| Agent | 10 |

| Kỹ năng gọi đích danh (Skill) | Số lần |
|---|---:|
| `ktc-ra-soat-897:review` | 11 |
| `update-config` | 2 |
| `ktc-quan-tri:bao-cao` | 1 |
| `ktc-quan-tri:the-thuc` | 1 |
| `ktc-quan-tri:ke-hoach` | 1 |
| `ktc-quan-tri:kpi-tu-danh-gia` | 1 |

| Tác tử (Agent) | Số lần |
|---|---:|
| `general-purpose` | 6 |
| `ktc-quan-tri` | 3 |
| `Explore` | 1 |

Lưu ý: kỹ năng được nạp tự động theo mô tả không luôn hiện thành một lần gọi `Skill` trong nhật ký; số trên là
**cận dưới** của số lần dùng kỹ năng.

## 4. Sản phẩm tạo ra (tệp .docx, .xlsx, .md trong 30-Ket-Qua)

| Nhóm (thư mục loại việc) | .docx | .xlsx | .md |
|---|---:|---:|---:|
| Ban-cam-ket-KPI-THHCQT | 15 | 0 | 0 |
| Bao-cao-thang-9 | 1 | 2 | 1 |
| Cong-Van | 2 | 0 | 0 |
| De-an-Hang-A | 2 | 0 | 1 |
| De-cuong-Hang-A | 3 | 0 | 2 |
| De-xuat | 2 | 1 | 13 |
| KPI-ca-nhan | 0 | 19 | 0 |
| Ke-Hoach | 1 | 0 | 0 |
| Nhiem-vu-phat-sinh | 0 | 0 | 1 |
| Ra-Soat | 10 | 0 | 6 |
| Ra-soat | 2 | 1 | 1 |
| Soan-thao | 1 | 0 | 0 |
| Track-Changes | 1 | 3 | 2 |
| Van-hanh | 0 | 0 | 3 |
| Tự thân Bộ công cụ (thẩm định, bằng chứng) | 47 | 0 | 54 |

## 5. Giới hạn của số liệu

- Nhật ký chỉ ghi khi làm việc trong thư mục dự án; phiên trên Claude (trò chuyện), Cowork không có ở đây.
- Hook `loi` chỉ bắt lỗi công cụ mà ứng dụng báo về; lỗi nghiệp vụ (số liệu sai) phát hiện qua rà soát, kiểm thử.
- Chưa đo token thực tế theo tác vụ (ứng dụng không trả số token cho hook) — thí điểm cần ghi theo phiếu.
