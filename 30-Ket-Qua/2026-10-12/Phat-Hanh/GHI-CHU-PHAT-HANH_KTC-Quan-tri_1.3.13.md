# Ghi chú phát hành — Bộ công cụ KTC-Quan-tri, phiên bản 1.3.13

Đơn vị phát hành: Phòng TH-HC&QT, Trường Cao đẳng Kon Tum · Ngày phát hành: 13/10/2026 (dự kiến, theo ngày ký Thông báo)

## Tệp phát hành

| Tệp | Mã SHA-256 |
|---|---|
| `ktc-quan-tri-1.3.13.zip` (plugin) | `d7c34a51e85f02278ec0e5a38c02089c0d7ae58280c8f59af6d0f673f9fbdd7e` |
| Bộ 8 kỹ năng rời (`Bộ-skills-rời.zip`) | Trùng byte 8/8 tệp SKILL.md với plugin (xác nhận tại Báo cáo thẩm định lần 2) |

Tệp plugin **giữ nguyên** bản đã qua thẩm định độc lập lần 6 và thẩm định lần 2 của Phòng QLKHCN&HTPT; mã SHA-256 không đổi.
Đối chiếu mã trước khi cài (PowerShell): `Get-FileHash .\ktc-quan-tri-1.3.13.zip -Algorithm SHA256`. Không trùng thì không cài, báo Phòng TH-HC&QT.

## Thành phần

8 kỹ năng: ke-hoach 3.12 · bao-cao 3.20 · theo-doi-cv 1.10 · quan-tri 1.16 · kpi-lap-ke-hoach 1.4 · kpi-tu-danh-gia 1.3 ·
soan-thao-vb 1.15 · the-thuc 1.3. 7 tác tử kiểm tra. Thao tác tự động (hooks) trên Claude Cowork, Claude Code (cần Python).

## Cài đặt, cập nhật (theo trang hỗ trợ Anthropic, truy cập 12/10/2026)

- Cấp tổ chức: Organization settings > Plugins & skills > Upload a plugin; tệp .zip dưới 200 MB. Tải plugin cùng tên thì tự ghi đè bản trước, không cần gỡ.
- Chế độ phân phối khi ban hành: **Available to install** (người dùng tự cài).
- Sau khi cài: Mở cuộc hội thoại mới; đầu phiên hiện "KTC-Quan-tri Plugin 1.3.13 — SessionStart doctor".

## Giới hạn đã biết (đọc trước khi dùng)

1. **Task_ID chưa áp dụng.** Nhiệm vụ đối chiếu theo mã sản phẩm QĐ 2119/QĐ-CĐKT và tên nhiệm vụ (mã cảnh báo `DOI_CHIEU_GAN_DUNG`
   — đơn vị đối chiếu thủ công trước khi ký). Quy tắc Task_ID trong gói là dự thảo, chờ Trường ban hành quy định mã nhiệm vụ phù hợp
   phần mềm quản lý KPI của tỉnh.
2. **Không chứa Skill `ktc-ra-soat-897`.** Rà soát trước trình ký dùng Skill riêng theo TB 948/TB-CĐKT.
3. **Thao tác chặn ghi (guard) chỉ là lớp hỗ trợ** cho một số thao tác ghi trên máy; không áp dụng qua kết nối Google Drive. Phân quyền chỉ đọc trên Drive là biện pháp bảo vệ chính.
4. **Kết quả kiểm thử là thử nghiệm sơ bộ** trên Claude Code (Opus 5.5: 29/30 lượt; Sonnet 5: 6/6; Haiku 4.5: 4/6 — không dùng Haiku 4.5 để soạn văn bản, phần căn cứ).
5. Nhật ký: Mặc định không ghi nội dung; không dùng `#học` với dữ liệu cá nhân; biến `KTC_NHAT_KY_NOI_DUNG` mặc định tắt, không bật trên máy đơn vị.
6. Dữ liệu đưa vào Claude được xử lý trên hạ tầng nhà cung cấp theo điều khoản tài khoản Claude AI Team; tối thiểu hóa, ưu tiên ẩn danh.

## Lộ trình nâng cấp (không phải điều kiện ban hành)

Ma trận dữ liệu × nền tảng × chế độ; cơ chế cấp Task_ID khi có quy định mã nhiệm vụ; bỏ biến ghi nội dung nhật ký khỏi bản đơn vị;
mở rộng kiểm thử trên Claude (trò chuyện), Cowork; Skill 38 (tra cứu kết quả cá nhân trên Hệ thống QLVB&ĐH, bao-cao 3.21) đóng gói ở 1.3.14.

## Văn bản kèm theo

Thông báo hướng dẫn sử dụng (bản 10) · Tài liệu hướng dẫn sử dụng chi tiết (bản 10) · Báo cáo tiếp thu, giải trình Báo cáo thẩm định lần 2.
