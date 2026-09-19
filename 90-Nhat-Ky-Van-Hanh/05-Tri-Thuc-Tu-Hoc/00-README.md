# 05-Tri-Thuc-Tu-Hoc — Vòng tự học của hệ (DL-20260919-005)

```
Người dùng gõ yêu cầu ──hook UserPromptSubmit──▶ 04-Nhat-Ky-Tu-Dong/*.jsonl  (loai: yeu-cau + tin_hieu)
Thao tác, lỗi, cảnh báo thể thức ──hook PostToolUse──▶ cùng tệp jsonl
                     │
        agent ktc-tu-hoc (cuối phiên / khi hook nhắc "⟳ N tín hiệu chưa xử lý")
                     ▼
        TRI-THUC.md  ──hook SessionStart──▶ nạp vào context phiên sau
        Nhat-Ky-Hoc.md (mỗi lượt học: đã đọc gì, rút được gì)
        .lan-hoc-cuoi  (mốc thời gian — tín hiệu sau mốc mới là "chưa xử lý")
                     │  mục cần sửa quy tắc/skill (cột Chuyển = → CP)
                     ▼
        agent ktc-tu-cai-tien ──▶ 92-Kinh-Nghiem/03-Change-Proposals/ (chờ người duyệt)
```

- **Tự học** gồm quy ước, sửa sai, sự thật đã kiểm chứng, kỹ thuật. Mục được ghi ngay và nạp lại ở phiên sau.
- **Tự cải tiến** là sửa quy tắc hoặc skill. Việc này luôn qua đề xuất và người duyệt (Nguyên tắc bất biến 6).
- Nhật ký lưu lời người dùng, tối đa 600 ký tự mỗi lượt, trong repo GitHub **riêng tư**. Không gõ mật khẩu hoặc
  token vào khung chat.
