"""
Hooks và callbacks cho Qtile.

Cung cấp các hooks để tự động hóa các tác vụ và xử lý các sự kiện.
"""

import os
import subprocess
from libqtile import hook

from modules.settings import STICKY_WINDOWS, AUTOSTART_SCRIPT

@hook.subscribe.setgroup
def move_sticky_windows():
    """Di chuyển các cửa sổ sticky khi chuyển workspace."""
    for window in STICKY_WINDOWS:
        window.togroup()
    return

@hook.subscribe.client_killed
def remove_sticky_windows(window):
    """Xóa cửa sổ khỏi danh sách sticky khi cửa sổ bị đóng."""
    if window in STICKY_WINDOWS:
        STICKY_WINDOWS.remove(window)

@hook.subscribe.client_managed
def auto_sticky_windows(window):
    """Tự động thêm một số loại cửa sổ vào danh sách sticky."""
    info = window.info()
    if (info['wm_class'] == ['Toolkit', 'firefox']
            and info['name'] == 'Picture-in-Picture'):
        STICKY_WINDOWS.append(window)

@hook.subscribe.startup_once
def autostart():
    """Khởi động các ứng dụng khi Qtile khởi động."""
    home = os.path.expanduser(AUTOSTART_SCRIPT)
    subprocess.call([home])
