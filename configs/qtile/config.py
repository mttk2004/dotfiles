"""
Cấu hình Qtile hiện đại.

Sử dụng các module hiện đại với thiết kế tối giản và hiệu quả.
"""

# Import modules
from modules.keys import init_keys
from modules.groups import init_groups, init_group_keys
from modules.layouts_modern import init_layouts, init_floating_layout
from modules.mouse import init_mouse
from modules.screens_modern import init_screens
from modules.settings import (
    FOLLOW_MOUSE_FOCUS, BRING_FRONT_CLICK, CURSOR_WARP,
    AUTO_FULLSCREEN, FOCUS_ON_WINDOW_ACTIVATION,
    RECONFIGURE_SCREENS, AUTO_MINIMIZE, WM_NAME
)
import modules.hooks

# Initialize Qtile components
keys = init_keys()
groups = init_groups()
keys = init_group_keys(groups, keys)
layouts = init_layouts()
floating_layout = init_floating_layout()
mouse = init_mouse()
screens = init_screens()

# Additional configuration
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = FOLLOW_MOUSE_FOCUS
bring_front_click = BRING_FRONT_CLICK
cursor_warp = CURSOR_WARP
auto_fullscreen = AUTO_FULLSCREEN
focus_on_window_activation = FOCUS_ON_WINDOW_ACTIVATION
reconfigure_screens = RECONFIGURE_SCREENS
auto_minimize = AUTO_MINIMIZE
wl_input_rules = None

# LG3D is a 3D non-reparenting WM written in java that happens to be on java's whitelist.
wmname = WM_NAME
