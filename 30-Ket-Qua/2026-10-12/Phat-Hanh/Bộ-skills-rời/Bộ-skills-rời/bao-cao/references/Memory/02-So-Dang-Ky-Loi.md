# SỔ ĐĂNG KÝ LỖI KTC-RIS

Tra file này khi script chạy ra kết quả lạ, trước khi kết luận "dữ liệu đơn vị sai".
Nhiều lỗi trong danh sách này **không báo lỗi ra màn hình** — chúng trả về kết quả sai một cách im lặng.

Chú thích trạng thái: ✅ đã vá · ❌ còn lỗi · ⬜ chưa kiểm

## Bảng tổng hợp

| Mã | Mức | Mô tả ngắn | v2.3 | v3.0 | v2.5.1 | v3.1 (dự kiến) |
|---|---|---|---|---|---|---|
| BUG-01 | Nghiêm trọng | Không nhận diện được Phụ lục KQ khi chữ "KPI" ở hàng gộp phía trên | ❌ | ❌ | ✅ | ✅ |
| BUG-02 | Nghiêm trọng | Nhãn `Trục 1.` không có số dẫn đầu → đọc ra 0 nhiệm vụ | ❌ | ✅ | ✅ | ✅ |
| BUG-03 | Nghiêm trọng | Dòng "Tổng cộng" bị tính thành nhiệm vụ → KPI cộng gấp đôi | ❌ | ❌ | ✅ | ✅ |
| BUG-04 | Cao | `truc_tong` lấy từ dòng tiêu đề Trục (rỗng) thay vì dòng SUM | ❌ | ❌ | ✅ | ✅ |
| BUG-05 | Cao | Đọc 0 dòng vẫn báo thành công, không cảnh báo | ❌ | ❌ | ✅ | ✅ |
| BUG-06 | Cao | Chỉ kiểm công thức cột (9), bỏ qua (10)(12)(14)(16) | ❌ | ❌ | ✅ | ✅ |
| BUG-07 | Trung bình | Báo lỗi giả với ghi chú hợp lệ "Kết luận giao ban" | ❌ | ❌ | ✅ | ✅ |
| BUG-08 | Trung bình | Ghi chú thừa dấu cách → bị loại khỏi báo cáo Trường | ❌ | ❌ | ✅ | ✅ |
| BUG-09 | Thấp | Không chặn số Trục ngoài 1-6 → `KeyError` | ❌ | ❌ | ✅ | ✅ |
| BUG-10 | Nghiêm trọng | Khóa ngắn chiếm chỗ khóa dài → **điền sai nội dung** | ❌ | ❌ | ✅ | ✅ |
| BUG-11 | Nghiêm trọng | Xóa mất nhãn in đậm "* Công tác ...: " → sai thể thức | ❌ | ❌ | ✅ | ✅ |
| BUG-12 | Cao | Không quét đoạn nằm trong bảng | ❌ | ❌ | ✅ | ✅ |
| BUG-13 | Cao | Không báo khóa `content_map` gõ sai → nội dung im lặng biến mất | ❌ | ❌ | ✅ | ✅ |
| BUG-14 | Trung bình | Nhận diện dòng ngày ký chỉ bắt dạng `[…]`, lệ thuộc chữ "Quảng Ngãi" | ❌ | ❌ | ✅ | ✅ |
| **BUG-15** | **Nghiêm trọng** | **Nhiệm vụ Mục II (chưa hoàn thành) bị gộp vào Trục cuối của Mục I → báo việc chưa xong thành đã xong** | ❌ | ✅ | **❌** | ✅ |
| **BUG-16** | **Nghiêm trọng** | **Nội dung Phần I (kết quả) bị chép sang Phần III (kế hoạch) khi nhãn trùng nhau** | ❌ | ✅ | **❌** | ✅ |

## Lỗi đang MỞ cần lưu ý ngay

- **BUG-15 và BUG-16 đang mở trên bản v2.5.1 đang cài.** Nếu dùng v2.5.1 để xuất báo cáo
  mà chưa gộp v3.1: phải **kiểm tra thủ công** hai chỗ — (a) Trục cuối cùng có bị lẫn việc
  chưa hoàn thành không, (b) mục Nhiệm vụ trọng tâm tháng sau có bị chép nội dung kết quả không.

## Cách kiểm nhanh khi nghi ngờ

| Triệu chứng | Nghi lỗi | Kiểm bằng cách |
|---|---|---|
| `kind=None` | BUG-01 | Xem chữ "KPI" nằm ở hàng nào so với hàng chứa "TT" |
| `so_nhiem_vu=0` | BUG-02 | Xem nhãn Trục trong file có đúng dạng `Trục <số>` không |
| KPI cao gấp ~2 lần | BUG-03 | Đếm xem dòng "Tổng cộng" có bị tính là nhiệm vụ không |
| Trục 6 nhiều việc bất thường | **BUG-15** | Xem có việc nào thuộc Mục II bị kéo vào không |
| Phần III giống hệt Phần I | **BUG-16** | Đối chiếu nội dung 2 phần |
| Nội dung điền sai chỗ | BUG-10 | Xem có 2 nhãn mà nhãn này là tiền tố nhãn kia không |

Chạy lại toàn bộ kiểm thử: `python3 references/Skill-Library/test_regression_v251.py`

## Cách thêm lỗi mới

Cấp mã tiếp theo (BUG-17...), ghi đủ: mức độ · mô tả **hậu quả thực tế** (không chỉ mô tả kỹ thuật) ·
bản nào dính · cách nhận biết. Nếu chưa vá, thêm vào mục "Lỗi đang MỞ" ở trên.
