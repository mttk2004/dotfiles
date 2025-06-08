"""
Widget hiện đại cho Qtile.

Cung cấp các widget với thiết kế hiện đại, tối giản và thống nhất.
Sử dụng bảng màu từ themes/colors.py.
"""

from libqtile import widget, qtile
import subprocess
import os

from themes.colors import colors
from modules.settings import (
    FONT_FAMILY, FONT_SIZE, ICON_SIZE, ICON_SIZE_SMALL, TERMINAL, APP_LAUNCHER, SCRIPTS_DIR, ICONS_DIR,
    WIDGET_PADDING, WIDGET_PADDING_SMALL, WIDGET_PADDING_LARGE, WIDGET_GROUPBOX_FONTSIZE, WIDGET_SEPARATOR_LINEWIDTH,
    WIDGET_UPDATE_INTERVAL, WIDGET_BATTERY_UPDATE_INTERVAL, WIDGET_MAX_CHARS, SYSTRAY_ICON_SIZE
)

# Đường dẫn đến thư mục icons
ICONS_PATH = os.path.expanduser(ICONS_DIR)

# Utility functions
def open_launcher():
    """Mở app launcher."""
    qtile.cmd_spawn(APP_LAUNCHER)

def open_terminal():
    """Mở terminal."""
    qtile.cmd_spawn(TERMINAL)

def open_btop():
    """Mở btop trong terminal."""
    qtile.cmd_spawn(f"{TERMINAL} --hold -e btop")

def open_powermenu():
    """Mở power menu."""
    script_path = os.path.expanduser(f"{SCRIPTS_DIR}powermenu.sh")
    subprocess.Popen([script_path])

def init_widgets_defaults():
    """Khởi tạo các giá trị mặc định cho widgets."""
    return dict(
        font=FONT_FAMILY,
        fontsize=FONT_SIZE,
        padding=WIDGET_PADDING,
        background=colors["bg"],
        foreground=colors["fg"],
    )

def init_widgets_list():
    """Khởi tạo danh sách widgets cho bar."""
    widgets_list = [
        # Logo/Menu button
        # widget.TextBox(
        #     text=" ",  # Icon cho menu (nếu có font awesome)
        #     foreground=colors["green_accent"],
        #     fontsize=ICON_SIZE,
        #     padding=WIDGET_PADDING,
        #     mouse_callbacks={'Button1': open_launcher},
        # ),

        # Separator
        # widget.Sep(
        #     linewidth=0,
        #     padding=WIDGET_PADDING,
        # ),

        # Group Box - Hiển thị các workspace
        widget.GroupBox(
            font=FONT_FAMILY,
            fontsize=WIDGET_GROUPBOX_FONTSIZE,
            margin_y=5,
            margin_x=2,
            padding_y=8,
            padding_x=5,
            borderwidth=3,
            active=colors["active"],
            inactive=colors["inactive_group"],
            rounded=True,
            highlight_color=colors["bg"],
            highlight_method="line",
            this_current_screen_border=colors["green_accent"],
            this_screen_border=colors["green_secondary"],
            other_current_screen_border=colors["green_dark"],
            other_screen_border=colors["inactive"],
            urgent_border=colors["error"],
            urgent_text=colors["error"],
            disable_drag=True,
        ),

        # Separator
        widget.Sep(
            linewidth=WIDGET_SEPARATOR_LINEWIDTH,
            padding=WIDGET_PADDING_LARGE,
            foreground=colors["inactive"],
        ),

        # Current Layout Icon
        # widget.CurrentLayoutIcon(
        #     scale=0.5,
        #     padding=0,
        # ),

        # Current Layout
        widget.CurrentLayout(
            font=FONT_FAMILY,
            padding=WIDGET_PADDING_SMALL,
            foreground=colors["green_light"],
            fontsize=FONT_SIZE,
        ),

        # Separator
        widget.Sep(
            linewidth=WIDGET_SEPARATOR_LINEWIDTH,
            padding=WIDGET_PADDING_LARGE,
            foreground=colors["inactive"],
        ),

        # Window Name
        widget.WindowName(
            font=FONT_FAMILY,
            format="{name}",
            max_chars=WIDGET_MAX_CHARS,
            empty_group_string="Desktop",
            foreground=colors["fg"],
            padding=WIDGET_PADDING,
            fontsize=FONT_SIZE,
        ),

        # Separator
        widget.Sep(
            linewidth=WIDGET_SEPARATOR_LINEWIDTH,
            padding=WIDGET_PADDING_LARGE,
            foreground=colors["inactive"],
        ),

        # Systray
        widget.Systray(
            icon_size=SYSTRAY_ICON_SIZE,
        ),

        # Separator
        widget.Sep(
            linewidth=WIDGET_SEPARATOR_LINEWIDTH,
            padding=WIDGET_PADDING_LARGE,
            foreground=colors["inactive"],
        ),

        # CPU Widget với icon
        widget.TextBox(
            text="󰘚",  # Icon CPU (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.CPU(
            font=FONT_FAMILY,
            format="{load_percent:.0f}%",
            foreground=colors["fg"],
            padding=WIDGET_PADDING_SMALL,
            update_interval=WIDGET_UPDATE_INTERVAL,
            mouse_callbacks={'Button1': open_btop},
            fontsize=FONT_SIZE,
        ),

        # Memory Widget với icon
        widget.TextBox(
            text=" 󰍛",  # Icon RAM (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=WIDGET_PADDING,
        ),
        widget.Memory(
            font=FONT_FAMILY,
            format="{MemUsed:.0f}MB",
            foreground=colors["fg"],
            update_interval=WIDGET_UPDATE_INTERVAL,
            mouse_callbacks={'Button1': open_btop},
            fontsize=FONT_SIZE,
        ),

        # Battery Widget với icon
        widget.TextBox(
            text=" 󰁹",  # Icon Pin (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE_SMALL,
            padding=WIDGET_PADDING,
        ),
        widget.Battery(
            font=FONT_FAMILY,
            format="{percent:2.0%}",
            foreground=colors["fg"],
            update_interval=WIDGET_BATTERY_UPDATE_INTERVAL,
            charge_char="󰂄",
            discharge_char="󰂃",
            full_char="󰁹",
            empty_char="󰂎",
            show_short_text=False,
            low_foreground=colors["warning"],
            low_percentage=0.15,
            fontsize=FONT_SIZE,
        ),

        # Volume Widget với icon
        widget.TextBox(
            text=" 󰕾",  # Icon Volume (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.PulseVolume(
            font=FONT_FAMILY,
            foreground=colors["fg"],
            limit_max_volume=True,
            fontsize=FONT_SIZE,
        ),

        # Brightness Widget với icon
        widget.TextBox(
            text=" 󰃠",  # Icon Brightness (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.Backlight(
            backlight_name="amdgpu_bl0",
            font=FONT_FAMILY,
            format="{percent:2.0%}",
            foreground=colors["fg"],
            change_command="brightnessctl s {0}%",
            step=5,
            fontsize=FONT_SIZE,
        ),

        # Date Widget với icon
        widget.TextBox(
            text=" 󰸗",  # Icon Calendar (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.Clock(
            font=FONT_FAMILY,
            format="%d/%m/%y",
            foreground=colors["fg"],
            fontsize=FONT_SIZE,
        ),

        # Time Widget với icon
        widget.TextBox(
            text=" 󰥔",  # Icon Clock (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.Clock(
            font=FONT_FAMILY,
            format="%H:%M",
            foreground=colors["fg"],
            fontsize=FONT_SIZE,
        ),

        # Separator
        widget.Sep(
            linewidth=WIDGET_SEPARATOR_LINEWIDTH,
            padding=WIDGET_PADDING_LARGE,
            foreground=colors["inactive"],
        ),

        # Power Menu Button
        widget.TextBox(
            text="⏻",  # Icon Power (nếu có font awesome)
            foreground=colors["error"],
            fontsize=ICON_SIZE,
            mouse_callbacks={'Button1': open_powermenu},
        ),
    ]
    return widgets_list

def init_secondary_widgets_list():
    """Khởi tạo danh sách widgets cho màn hình thứ hai."""
    # Đơn giản hóa widgets cho màn hình thứ hai
    widgets_list = init_widgets_list()
    # Loại bỏ systray vì chỉ nên hiển thị trên một màn hình
    for widget in widgets_list:
        if isinstance(widget, widget.Systray):
            widgets_list.remove(widget)
    return widgets_list
