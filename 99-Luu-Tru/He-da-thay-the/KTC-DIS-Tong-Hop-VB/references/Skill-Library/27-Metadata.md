# 27-Metadata — Skill Library Index

Bảng tra cứu toàn bộ Skill (26 skill), nhóm theo chức năng.

## Nhóm A — Skill nền (Core)
| ID | Skill | Chức năng |
|----|-------|-----------|
| 01 | Skill-Soan-Thao | Soạn thảo bản nháp đầu tiên |
| 02 | Skill-Kiem-Tra-The-Thuc | Kiểm tra thể thức tổng thể theo NĐ 30 |
| 03 | Skill-Kiem-Tra-Can-Cu | Kiểm tra/đề xuất căn cứ pháp lý |
| 04 | Skill-Chuan-Hoa-Van-Ban | Chuẩn hóa văn phong hành chính |
| 05 | Skill-Phan-Tich-Yeu-Cau | Phân tích yêu cầu, chọn loại văn bản |
| 06 | Skill-Tong-Hop-Noi-Dung | Tổng hợp nội dung từ nhiều nguồn |

## Nhóm B — Skill theo loại văn bản
| ID | Skill | Loại văn bản |
|----|-------|--------------|
| 07 | Skill-Van-Ban-Quyet-Dinh | Quyết định |
| 08 | Skill-Van-Ban-Ke-Hoach | Kế hoạch |
| 09 | Skill-Van-Ban-Thong-Bao | Thông báo |
| 10 | Skill-Van-Ban-Bao-Cao | Báo cáo |
| 11 | Skill-Van-Ban-To-Trinh | Tờ trình |
| 12 | Skill-Van-Ban-Cong-Van | Công văn |
| 13 | Skill-Van-Ban-Bien-Ban | Biên bản |

## Nhóm C — Skill kiểm tra xuyên suốt
| ID | Skill | Chức năng |
|----|-------|-----------|
| 14 | Skill-Ky-Thuat-Trinh-Bay | Kiểm tra trình bày chi tiết (font, lề, đánh số) |
| 15 | Skill-Kiem-Tra-Logic | Kiểm tra chuỗi logic mục tiêu-nhiệm vụ-giải pháp |
| 16 | Skill-De-Xuat-Quy-Trinh-Trinh-Ky | Đề xuất quy trình trình ký |
| 17 | Skill-Kiem-Tra-Tham-Quyen | Kiểm tra thẩm quyền người ký |
| 18 | Skill-Kiem-Tra-Tinh-Thong-Nhat | Kiểm tra tính thống nhất tên gọi |
| 19 | Skill-Danh-Gia-Chat-Luong-Van-Ban | Chấm điểm/xếp hạng chất lượng văn bản |

## Nhóm D — Skill nghiệp vụ
| ID | Skill | Lĩnh vực |
|----|-------|----------|
| 20 | Skill-Nghiep-Vu-Dao-Tao | Đào tạo |
| 21 | Skill-Nghiep-Vu-Tuyen-Sinh | Tuyển sinh |
| 22 | Skill-Nghiep-Vu-Can-Bo | Tổ chức - Cán bộ |
| 23 | Skill-Nghiep-Vu-Tai-Chinh | Tài chính - Kế toán |
| 24 | Skill-Dam-Bao-Chat-Luong | Đảm bảo chất lượng - Kiểm định |
| 25 | Skill-Van-Ban-Cap-Phong | Văn bản nội bộ cấp Phòng/Khoa |
| 26 | Skill-Van-Ban-Doi-Ngoai | Đối ngoại - Hợp tác |

## Nhóm E — Skill tổng hợp đầu ra (Reporting)
| ID | Skill | Chức năng |
|----|-------|-----------|
| 28 | Skill-Bao-Cao-Ra-Soat-Chuan | Tạo Báo cáo rà soát văn bản đầy đủ 7 phần, có căn cứ, có mức độ nghiêm trọng — chuẩn đầu ra bắt buộc cho mọi yêu cầu rà soát văn bản quan trọng |

## Nhóm F — Skill theo hệ văn bản khác (ngoài Nghị định 30)
| ID | Skill | Hệ văn bản |
|----|-------|-----------|
| 29 | Skill-Van-Ban-Dang | Văn bản của Đảng (cấp uỷ, tổ chức, cơ quan đảng) — theo Quy định 399-QĐ/TW (thể loại, thẩm quyền) + Hướng dẫn 05-HD/VPTW (thể thức), KHÔNG dùng skill 02/07-13/14 (thiết kế cho NĐ30) cho văn bản Đảng |

## Nhóm G — Skill phân loại/khung đánh giá
| ID | Skill | Chức năng |
|----|-------|-----------|
| 30 | Skill-Phan-Loai-6-Truc | Phân loại nhiệm vụ vào 6 trục kết quả trọng tâm (38 nội hàm) khi soạn/rà soát Kế hoạch và Báo cáo công tác — theo Thông báo 817/TB-CĐKT |

## Trình tự sử dụng khuyến nghị (pipeline)
**Văn bản hành chính nhà nước:** `05 (Phân tích yêu cầu)` → chọn skill Nhóm B theo loại văn bản → `20-26` nếu thuộc lĩnh vực chuyên môn → `01 (Soạn thảo)` → `02, 14 (Thể thức/trình bày)` → `03 (Căn cứ)` → `15 (Logic, nếu là Kế hoạch/Đề án)` → `17 (Thẩm quyền)` → `18 (Thống nhất)` → `04 (Chuẩn hóa văn phong)` → `16 (Quy trình trình ký)` → `19 (Đánh giá chất lượng)` → **`28 (đóng gói thành Báo cáo rà soát chuẩn, nếu yêu cầu là rà soát toàn diện một văn bản/dự thảo quan trọng)`**.

**Văn bản của Đảng:** dùng riêng `29 (Skill-Van-Ban-Dang)` làm lớp thể thức/kiểm tra chính (thay cho 02/07-13/14); có thể kết hợp `28` cho khung báo cáo rà soát 7 phần, nhưng phần căn cứ thể thức phải lấy từ `29`, không lấy từ NĐ30.

**Kế hoạch/Báo cáo công tác (năm/quý/tháng):** kết hợp `08 (Skill-Van-Ban-Ke-Hoach)` hoặc `10 (Skill-Van-Ban-Bao-Cao)` với `30 (Skill-Phan-Loai-6-Truc)` để phân loại đúng nhiệm vụ vào 6 trục trước khi hoàn thiện văn bản.

## Ghi chú mở rộng
Theo kế hoạch tổng thể (Kế hoạch xây dựng Trợ lý AI), quy mô mục tiêu là 30-40 skill ở Giai đoạn 3, và có thể mở rộng tới 200-300 skill chuyên sâu ở tầm nhìn KTC Governance Knowledge Platform (KTC-GKP). Bộ 26 skill hiện tại đã bao phủ đủ 7 loại văn bản hành chính chính, 6 lớp kiểm tra chất lượng xuyên suốt, và 7 lĩnh vực nghiệp vụ cốt lõi — đủ để vận hành Stage 2. Việc mở rộng tiếp theo (ví dụ: skill cho Đề án, Chương trình, Giấy mời, Quy chế/Quy định — xem `03-Templates`) nên bổ sung khi có nhu cầu thực tế cụ thể, tránh tạo skill không có input/output rõ ràng.
