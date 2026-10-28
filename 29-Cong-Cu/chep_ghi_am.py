# -*- coding: utf-8 -*-
"""Chep ghi am cuoc hop thanh chu (faster-whisper, chay tren may, khong gui ra ngoai) — 28/10/2026.

    python 29-Cong-Cu/chep_ghi_am.py <thu_muc_ra> <tep1.m4a> [tep2 ...] [--mo-hinh large-v3]

Thong so DA KIEM (phien De an Hang A 26/10/2026):
  - KHONG dung initial_prompt: am thanh nho/vang -> mo hinh lap lai nguyen cau goi y (3/4 tep hong lan 1).
  - condition_on_previous_text=False, no_repeat_ngram_size=3: chan vong lap "nam 7, nam 8, ...".
  - PyAV phai < 16 (faster-whisper 1.2.1 goi av.open(metadata_errors=...) — PyAV 19 bo tham so nay).
  - Loc cau rac YouTube ("dang ky kenh", "subscribe", "lalaschool") — mo hinh sinh ra khi gap khoang lang.
GIOI HAN: ghi am hoi truong chi nghe duoc khoang 30% y. Ban chep la DE KIEM, khong lam nguon duy nhat
(rule 24 muc 14). Moi doan ghi kem [mm:ss] de tra lai.
Cai dat lan dau (can nguoi dung dong y tai ~1,6 GB):  pip install faster-whisper "av>=14,<16"
"""
import os
import re
import sys
import time

RAC = re.compile(r"đăng ký kênh|subscribe|lalaschool|theo dõi và hẹn gặp lại|video hấp dẫn", re.I)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    mo_hinh = "large-v3"
    if "--mo-hinh" in argv:
        i = argv.index("--mo-hinh"); mo_hinh = argv[i + 1]; del argv[i:i + 2]
    out, tep = argv[0], argv[1:]
    import av
    if int(av.__version__.split(".")[0]) >= 16:
        print(f"PyAV {av.__version__} khong tuong thich — chay: pip install \"av>=14,<16\"")
        return 1
    from faster_whisper import WhisperModel
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    os.makedirs(out, exist_ok=True)
    m = WhisperModel(mo_hinh, device="cpu", compute_type="int8")
    for f in tep:
        t0 = time.time()
        segs, info = m.transcribe(f, language="vi", vad_filter=True, beam_size=5, condition_on_previous_text=False,
                                  no_repeat_ngram_size=3, temperature=[0.0, 0.2, 0.4])
        dich = os.path.join(out, os.path.splitext(os.path.basename(f))[0] + ".txt")
        n = bo = 0
        with open(dich, "w", encoding="utf-8") as o:
            for s in segs:
                if RAC.search(s.text):
                    bo += 1
                    continue
                o.write(f"[{int(s.start // 60):02d}:{int(s.start % 60):02d}] {s.text.strip()}\n"); o.flush(); n += 1
        print(f"{os.path.basename(f)}: {round(info.duration)} s am thanh, {n} doan, bo {bo} doan rac, {round(time.time() - t0)} s",
              flush=True)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
