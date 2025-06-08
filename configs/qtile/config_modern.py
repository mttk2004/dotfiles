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
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False  # This puts your mouse in the center on the screen after you switch to another workspace
auto_fullscreen = True
focus_on_window_activation = "smart"  # or focus
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None

# LG3D is a 3D non-reparenting WM written in java that happens to be on java's whitelist.
wmname = "LG3D"
