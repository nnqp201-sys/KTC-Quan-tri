<!-- N34: chép nguyên văn từ `THONG-KE-VAN-HANH-THUC-TE-20260929-20261010.md` (sha256 8739987397940b527c05d20cbc00eeae4a88acff1c5c55c44c9a9fc825212493) -->

# Thống kê vận hành thực tế Bộ công cụ KTC-Quan-tri (2026-09-29 → 2026-10-10)

Nguồn: nhật ký tự động `90-Nhat-Ky-Van-Hanh/04-Nhat-Ky-Tu-Dong/` (chỉ thông tin mô tả — không có nội dung lời nhắn,
câu lệnh), sản phẩm trong `30-Ket-Qua/`, lịch sử git. Sinh bằng `29-Cong-Cu/thong_ke_van_hanh.py` (lặp lại được).
**Phạm vi:** vận hành của người phụ trách xây dựng trên Claude Code (máy Phòng TH-HC&QT), việc thật của Phòng —
**không** phải thí điểm tại các đơn vị; không suy ra kết quả cho Claude (trò chuyện), Cowork.

## 1. Tổng quan

| Chỉ số | Giá trị |
|---|---:|
| Số ngày có làm việc | 10 |
| Số phiên làm việc | 26 |
| Số thao tác công cụ | 924 |
| Số lượt yêu cầu của người dùng | 76 |
| Thao tác báo lỗi (hook ghi nhận) | 0 |
| Lần cập nhật mã nguồn (git) | 26 |
| Tín hiệu học (sửa sai / quy ước / quyết định) | 5 / 15 / 13 |

## 2. Theo ngày

| Ngày | Phiên | Thao tác |
|---|---:|---:|
| 2026-09-29 | 12 | 454 |
| 2026-09-30 | 2 | 25 |
| 2026-10-01 | 2 | 103 |
| 2026-10-04 | 1 | 7 |
| 2026-10-05 | 5 | 92 |
| 2026-10-06 | 4 | 61 |
| 2026-10-07 | 4 | 155 |
| 2026-10-08 | 2 | 12 |
| 2026-10-09 | 1 | 11 |
| 2026-10-10 | 3 | 4 |

## 3. Công cụ, kỹ năng, tác tử được gọi

| Loại | Số lần |
|---|---:|
| Bash | 668 |
| Edit | 112 |
| Write | 87 |
| PowerShell | 48 |
| Agent | 5 |
| Skill | 4 |

| Kỹ năng gọi đích danh (Skill) | Số lần |
|---|---:|
| `ktc-ra-soat-897:review` | 3 |
| `ktc-quan-tri:kpi-tu-danh-gia` | 1 |

| Tác tử (Agent) | Số lần |
|---|---:|
| `ktc-ra-soat-897` | 5 |

Lưu ý: kỹ năng được nạp tự động theo mô tả không luôn hiện thành một lần gọi `Skill` trong nhật ký; số trên là
**cận dưới** của số lần dùng kỹ năng.

## 4. Sản phẩm tạo ra (tệp .docx, .xlsx, .md trong 30-Ket-Qua)

| Nhóm (thư mục loại việc) | .docx | .xlsx | .md |
|---|---:|---:|---:|
| Bao-cao | 1 | 0 | 1 |
| Import-ke-hoach | 0 | 1 | 0 |
| KPI-ca-nhan | 2 | 3 | 0 |
| Ke-Hoach | 4 | 0 | 0 |
| Ra-Soat | 5 | 0 | 2 |
| Soan-Thao-VB | 16 | 0 | 1 |
| Soan-thao | 6 | 0 | 0 |
| Tham-Dinh-Doc-Lap-Lan-6 | 0 | 0 | 26 |
| Tra-cuu-van-ban-Hang-A | 0 | 0 | 1 |
| Track-Changes | 1 | 0 | 1 |
| Van-hanh | 0 | 0 | 1 |
| Tự thân Bộ công cụ (thẩm định, bằng chứng) | 186 | 97 | 759 |

## 5. Giới hạn của số liệu

- Nhật ký chỉ ghi khi làm việc trong thư mục dự án; phiên trên Claude (trò chuyện), Cowork không có ở đây.
- Hook `loi` chỉ bắt lỗi công cụ mà ứng dụng báo về; lỗi nghiệp vụ (số liệu sai) phát hiện qua rà soát, kiểm thử.
- Chưa đo token thực tế theo tác vụ (ứng dụng không trả số token cho hook) — thí điểm cần ghi theo phiếu.
