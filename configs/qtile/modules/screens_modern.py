"""
Cấu hình màn hình hiện đại cho Qtile.

Sử dụng widgets hiện đại từ widgets_modern.py và cài đặt từ settings.py.
"""

from libqtile.config import Screen
from libqtile import bar
import os

from modules.settings import BAR_HEIGHT, BAR_MARGIN, DEFAULT_WALLPAPER
from modules.widgets_modern import init_widgets_list, init_secondary_widgets_list
from themes.colors import colors

def init_screens():
    """Khởi tạo danh sách màn hình.

    Hỗ trợ nhiều màn hình với cấu hình khác nhau.
    """
    # Cấu hình thanh bar hiện đại
    bar_config = {
        "size": BAR_HEIGHT,
        "background": colors["bg"],
        "margin": BAR_MARGIN,  # [Top, Right, Bottom, Left]
        "border_width": [0, 10, 0, 10],  # [Top, Right, Bottom, Left]
    }

    # Danh sách màn hình
    screens = [
        # Màn hình chính
        Screen(
            top=bar.Bar(
                init_widgets_list(),
                **bar_config,
            ),
            wallpaper=os.path.expanduser(DEFAULT_WALLPAPER),
            wallpaper_mode="fill",
        ),
    ]

    # Thêm màn hình thứ hai nếu có
    # Kiểm tra xem có màn hình thứ hai không bằng cách kiểm tra xrandr hoặc các file trong /sys/class/drm
    connected_displays = []
    try:
        # Kiểm tra các card màn hình đã kết nối
        for card in os.listdir("/sys/class/drm"):
            card_path = f"/sys/class/drm/{card}/status"
            if os.path.isfile(card_path):
                with open(card_path, "r") as f:
                    if f.read().strip() == "connected":
                        connected_displays.append(card)

        # Nếu có nhiều hơn 1 màn hình đã kết nối
        if len(connected_displays) > 1:
            screens.append(
                Screen(
                    top=bar.Bar(
                        init_secondary_widgets_list(),
                        **bar_config,
                    ),
                    wallpaper=os.path.expanduser(DEFAULT_WALLPAPER),
                    wallpaper_mode="fill",
                )
            )
    except (FileNotFoundError, IOError, OSError):
        # Nếu không thể kiểm tra, chỉ sử dụng một màn hình
        pass

    return screens
