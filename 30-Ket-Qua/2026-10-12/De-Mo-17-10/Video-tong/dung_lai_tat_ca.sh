#!/usr/bin/env bash
# Dựng lại toàn bộ chuỗi video trình diễn 17/10/2026 sau khi đổi phông nền, giọng đọc hoặc nội dung:
# Video 1 -> 04 video thao tác -> chèn khung chân dung -> video toàn bộ (kèm nhạc nền, logo).
# Cách dùng (Git Bash):  bash dung_lai_tat_ca.sh
set -e -o pipefail
G="/d/.CLAUDE code/KTC-Quan-tri/30-Ket-Qua"
T="$G/2026-10-12/De-Mo-17-10/Video-thao-tac"
R="/d/.00. DE MO 17-10"; Q="$R/Video-thao-tac"; B="$R/BAN-TRINH-DIEN-17-10"; X="$Q/xuat"
echo "== 1. Video 1"; (cd "$G/2026-10-11/De-Mo-17-10/Video" && python lam_video1.py | tail -1)
V1=$(ls "$G/2026-10-11/De-Mo-17-10/Video"/Video-1_*_v*.mp4 | sort -V | tail -1)
echo "== 2. Trang trình chiếu"; (cd "$G/2026-10-12/De-Mo-17-10/Trinh-chieu" && python lam_trang_trinh_chieu.py && cp Trinh-chieu_*_v3.pdf "$B/01_Trang-trinh-chieu-11-trang.pdf")
echo "== 3. Video thao tác T1-T4"; cp "$T"/*.py "$Q/"; (cd "$Q" && python ghep_video.py | tail -5)
m() { (cd "$X" && python -c "import json;print(json.load(open('moc.json'))['$1'])"); }
echo "== 4. Chèn khung chân dung"
(cd "$Q" && python chen_hinh.py "$R/Chan-dung-Phuc.png" \
  $(m T1) "$X/T1_Tong-hop-ke-hoach.mp4" "$B/10_Video-T1_Tong-hop-ke-hoach.mp4" \
  $(m T2) "$X/T2_Doi-chieu-van-ban-chi-dao.mp4" "$B/13_Video-T2_Doi-chieu-van-ban-chi-dao.mp4" \
  $(m T3) "$X/T3_Bao-cao-thang.mp4" "$B/20_Video-T3_Bao-cao-thang.mp4" \
  $(m T4) "$X/T4_Ra-soat-van-ban-Dang.mp4" "$B/30_Video-T4_Ra-soat-van-ban-Dang.mp4" \
  tieu-de "$V1" "$B/02_Video-1_Gioi-thieu-03-he.mp4" | tail -5)
echo "== 5. Video toàn bộ"; (cd "$G/2026-10-12/De-Mo-17-10/Video-tong" && python lam_video_tong.py "$B" 2>&1 | grep -v "thử lại" | tail -4)
echo "== XONG"
