"""
Cấu hình chuột cho Qtile.

Định nghĩa các hành động chuột như kéo thả cửa sổ, thay đổi kích thước, v.v.
"""

from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from modules.settings import MOD

def init_mouse():
    """Khởi tạo danh sách các hành động chuột.

    Returns:
        list: Danh sách các hành động chuột đã cấu hình
    """
    mouse = [
        Drag([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([MOD], "Button2", lazy.window.bring_to_front()),
    ]
    return mouse
