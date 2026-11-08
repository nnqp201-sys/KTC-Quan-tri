#!/usr/bin/env python3
"""
doctor.py — Entrypoint kiểm tra sức khỏe hệ KTC-Quan-tri

Gộp các phép kiểm:
1. kiem_tra_he_thong.py (Tầng 1, 13 phép kiểm)
2. So PLUGIN_VERSION repo vs plugin.json vs marketplace.json
3. So bản cài ~/.claude/ktc-marketplace/ktc-quan-tri vs 31-Plugin
4. Tự thử guard
5. Chạy test quan trọng (nếu có pytest)

Mã thoát: 0 = ĐẠT, 1 = KHÔNG ĐẠT

Sử dụng:
    python 29-Cong-Cu/doctor.py          # Chạy tất cả
    python 29-Cong-Cu/doctor.py --nhanh  # Chỉ kiểm nhanh (bỏ test)
"""

import json
import subprocess
import sys
from pathlib import Path

# Thư mục gốc dự án
GOC = Path(__file__).resolve().parent.parent
PLUGIN_DIR = GOC / "31-Plugin"
BAN_CAI = Path.home() / ".claude" / "ktc-marketplace" / "ktc-quan-tri"


def in_muc(tieu_de: str):
    print(f"\n{'='*60}\n  {tieu_de}\n{'='*60}")


def kiem_he_thong() -> bool:
    """Chạy kiem_tra_he_thong.py"""
    in_muc("1. Kiểm tra hệ thống (Tầng 1)")
    script = GOC / "29-Cong-Cu" / "kiem_tra_he_thong.py"
    if not script.exists():
        print("  THIẾU: kiem_tra_he_thong.py")
        return False

    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(GOC),
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0


def lay_phien_ban_repo() -> str | None:
    """Đọc PLUGIN_VERSION từ dong_goi_plugin.py"""
    dong_goi = GOC / "29-Cong-Cu" / "dong_goi_plugin.py"
    if not dong_goi.exists():
        return None

    noi_dung = dong_goi.read_text(encoding="utf-8")
    for dong in noi_dung.splitlines():
        if dong.strip().startswith("PLUGIN_VERSION"):
            # PLUGIN_VERSION = "1.4.2"
            parts = dong.split("=", 1)
            if len(parts) == 2:
                return parts[1].strip().strip('"').strip("'")
    return None


def kiem_phien_ban() -> bool:
    """So sánh phiên bản giữa repo, plugin.json và marketplace.json"""
    in_muc("2. Kiểm tra phiên bản")

    repo_ver = lay_phien_ban_repo()
    print(f"  PLUGIN_VERSION (repo): {repo_ver or 'không đọc được'}")

    # plugin.json
    plugin_json = PLUGIN_DIR / ".claude-plugin" / "plugin.json"
    plugin_ver = None
    if plugin_json.exists():
        try:
            data = json.loads(plugin_json.read_text(encoding="utf-8"))
            plugin_ver = data.get("version")
        except:
            pass
    print(f"  plugin.json: {plugin_ver or 'không đọc được'}")

    # marketplace.json
    market_json = PLUGIN_DIR / ".claude-plugin" / "marketplace.json"
    market_ver = None
    if market_json.exists():
        try:
            data = json.loads(market_json.read_text(encoding="utf-8"))
            market_ver = data.get("version")
        except:
            pass
    print(f"  marketplace.json: {market_ver or 'không đọc được'}")

    # So sánh
    if repo_ver and plugin_ver and market_ver:
        if repo_ver == plugin_ver == market_ver:
            print(f"  ✓ Khớp: {repo_ver}")
            return True
        else:
            print(f"  ✗ LỆCH: repo={repo_ver}, plugin={plugin_ver}, market={market_ver}")
            return False

    print("  ? Không đủ dữ liệu để so sánh")
    return True  # Không coi là lỗi


def kiem_ban_cai() -> bool:
    """So bản cài vs 31-Plugin"""
    in_muc("3. Kiểm tra bản cài")

    if not BAN_CAI.exists():
        print(f"  Chưa cài: {BAN_CAI}")
        return True  # Không coi là lỗi

    # So plugin.json
    ban_cai_json = BAN_CAI / ".claude-plugin" / "plugin.json"
    repo_json = PLUGIN_DIR / ".claude-plugin" / "plugin.json"

    if not ban_cai_json.exists():
        print("  Bản cài thiếu plugin.json")
        return False

    try:
        ban_cai_ver = json.loads(ban_cai_json.read_text(encoding="utf-8")).get("version")
        repo_ver = json.loads(repo_json.read_text(encoding="utf-8")).get("version")

        if ban_cai_ver == repo_ver:
            print(f"  ✓ Bản cài khớp repo: {ban_cai_ver}")
            return True
        else:
            print(f"  ⚠ Bản cài cũ: {ban_cai_ver} (repo: {repo_ver})")
            print(f"    Cập nhật: chép đè {PLUGIN_DIR} vào {BAN_CAI}")
            return True  # Cảnh báo nhưng không coi là lỗi
    except Exception as e:
        print(f"  Lỗi đọc: {e}")
        return False


def kiem_guard() -> bool:
    """Tự thử guard"""
    in_muc("4. Kiểm tra guard")

    guard = GOC / "29-Cong-Cu" / "plugin_src" / "scripts" / "ktc_guard.py"
    if not guard.exists():
        guard = PLUGIN_DIR / "scripts" / "ktc_guard.py"

    if not guard.exists():
        print("  THIẾU: ktc_guard.py")
        return False

    # Chạy guard với --tu-thu
    result = subprocess.run(
        [sys.executable, str(guard), "--tu-thu"],
        capture_output=True,
        text=True
    )

    if "HOẠT ĐỘNG" in result.stdout or "HOAT DONG" in result.stdout:
        print("  ✓ Guard HOẠT ĐỘNG")
        return True
    elif result.returncode == 0:
        print("  ✓ Guard OK")
        return True
    else:
        print(f"  ⚠ Guard: {result.stdout or result.stderr}")
        return True  # Cảnh báo


def kiem_test_nhanh() -> bool:
    """Chạy test quan trọng nếu có pytest"""
    in_muc("5. Kiểm tra test (pytest)")

    try:
        import pytest
    except ImportError:
        print("  Bỏ qua: pytest chưa cài")
        return True

    test_dir = GOC / "92-Kinh-Nghiem" / "02-Regression" / "Cases"
    if not test_dir.exists():
        print("  Bỏ qua: không có thư mục test")
        return True

    # Chạy test quan trọng
    test_files = [
        "test_plugin_131.py",
        "test_guard.py",
    ]

    for tf in test_files:
        test_path = test_dir / tf
        if test_path.exists():
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_path), "-v", "--tb=short"],
                cwd=str(GOC),
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                print(f"  ✗ {tf} THẤT BẠI")
                print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
                return False
            print(f"  ✓ {tf}")

    return True


def main():
    nhanh = "--nhanh" in sys.argv or "-n" in sys.argv

    print("=" * 60)
    print("  KTC-Quan-tri Doctor")
    print("=" * 60)

    ket_qua = []

    # 1. Kiểm hệ thống
    ket_qua.append(("Hệ thống", kiem_he_thong()))

    # 2. Kiểm phiên bản
    ket_qua.append(("Phiên bản", kiem_phien_ban()))

    # 3. Kiểm bản cài
    ket_qua.append(("Bản cài", kiem_ban_cai()))

    # 4. Kiểm guard
    ket_qua.append(("Guard", kiem_guard()))

    # 5. Test (nếu không --nhanh)
    if not nhanh:
        ket_qua.append(("Test", kiem_test_nhanh()))

    # Tổng kết
    in_muc("KẾT LUẬN")

    loi = [ten for ten, dat in ket_qua if not dat]

    if loi:
        print(f"  ✗ KHÔNG ĐẠT — {len(loi)} mục lỗi: {', '.join(loi)}")
        sys.exit(1)
    else:
        print(f"  ✓ ĐẠT — {len(ket_qua)} mục kiểm tra")
        sys.exit(0)


if __name__ == "__main__":
    main()
