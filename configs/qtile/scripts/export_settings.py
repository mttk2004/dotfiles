#!/usr/bin/env python3
"""
Script để xuất các biến từ settings.py thành các biến môi trường cho bash/fish.

Cách sử dụng:
- Bash: eval $(python3 ~/.config/qtile/scripts/export_settings.py bash)
- Fish: eval (python3 ~/.config/qtile/scripts/export_settings.py fish)
"""

import os
import sys
import importlib.util

def get_settings():
    """Lấy các biến từ settings.py."""
    # Lấy đường dẫn đến settings.py
    settings_path = os.path.expanduser("~/.config/qtile/modules/settings.py")

    # Load module settings.py
    spec = importlib.util.spec_from_file_location("settings", settings_path)
    settings = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings)

    return settings

def export_bash(settings):
    """Xuất các biến cho bash."""
    for var_name in dir(settings):
        # Chỉ lấy các biến viết hoa (constants)
        if var_name.isupper():
            value = getattr(settings, var_name)
            # Chỉ xuất các kiểu dữ liệu cơ bản
            if isinstance(value, (str, int, float, bool)):
                # Đảm bảo giá trị được bao bởi dấu nháy đơn cho bash
                if isinstance(value, str):
                    print(f"export QTILE_{var_name}='{value}'")
                else:
                    print(f"export QTILE_{var_name}={value}")

def export_fish(settings):
    """Xuất các biến cho fish."""
    for var_name in dir(settings):
        # Chỉ lấy các biến viết hoa (constants)
        if var_name.isupper():
            value = getattr(settings, var_name)
            # Chỉ xuất các kiểu dữ liệu cơ bản
            if isinstance(value, (str, int, float, bool)):
                # Đảm bảo giá trị được bao bởi dấu nháy đơn cho fish
                if isinstance(value, str):
                    print(f"set -x QTILE_{var_name} '{value}'")
                else:
                    print(f"set -x QTILE_{var_name} {value}")

def main():
    """Hàm chính."""
    if len(sys.argv) != 2 or sys.argv[1] not in ["bash", "fish"]:
        print("Sử dụng: python3 export_settings.py [bash|fish]")
        sys.exit(1)

    settings = get_settings()

    if sys.argv[1] == "bash":
        export_bash(settings)
    else:
        export_fish(settings)

if __name__ == "__main__":
    main()
