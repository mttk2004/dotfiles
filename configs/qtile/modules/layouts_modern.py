"""
Cấu hình bố cục cửa sổ hiện đại cho Qtile.

Sử dụng bảng màu từ themes/colors.py và cài đặt từ settings.py.
"""

from libqtile import layout
from libqtile.config import Match

from themes.colors import colors
from modules.settings import (
    LAYOUT_MARGIN, LAYOUT_BORDER_WIDTH, LAYOUT_RATIO, LAYOUT_MIN_RATIO,
    LAYOUT_MAX_RATIO, LAYOUT_CHANGE_RATIO, LAYOUT_GROW_AMOUNT,
    TREETAB_FONTSIZE, TREETAB_SECTION_FONTSIZE, TREETAB_PADDING,
    TREETAB_PANEL_WIDTH, TREETAB_SECTION_TOP, FONT_FAMILY
)

def init_layouts():
    """Khởi tạo danh sách layouts.

    Sử dụng các layout hiện đại với thiết kế tối giản và hiệu quả.
    """
    layouts = [
        # Layout Columns - Bố cục cột, phù hợp cho nhiều cửa sổ
        layout.Columns(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=LAYOUT_BORDER_WIDTH,
            border_on_single=False,
            margin=LAYOUT_MARGIN,
            margin_on_single=LAYOUT_MARGIN,
            grow_amount=LAYOUT_GROW_AMOUNT,
            insert_position=1,  # Thêm cửa sổ mới vào vị trí sau cửa sổ hiện tại
        ),

        # Layout Max - Phóng to cửa sổ hiện tại
        layout.Max(),

        # Layout MonadTall - Bố cục cửa sổ chính ở bên trái, các cửa sổ khác ở bên phải
        layout.MonadTall(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=LAYOUT_BORDER_WIDTH,
            margin=LAYOUT_MARGIN,
            ratio=LAYOUT_RATIO,
            min_ratio=LAYOUT_MIN_RATIO,
            max_ratio=LAYOUT_MAX_RATIO,
            change_ratio=LAYOUT_CHANGE_RATIO,
        ),

        # Layout MonadWide - Bố cục cửa sổ chính ở trên, các cửa sổ khác ở dưới
        layout.MonadWide(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=LAYOUT_BORDER_WIDTH,
            margin=LAYOUT_MARGIN,
            ratio=LAYOUT_RATIO,
        ),

        # Layout Matrix - Bố cục dạng lưới
        layout.Matrix(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=LAYOUT_BORDER_WIDTH,
            margin=LAYOUT_MARGIN,
        ),

        # Layout TreeTab - Bố cục dạng cây
        layout.TreeTab(
            active_bg=colors["green_primary"],
            active_fg=colors["bg"],
            bg_color=colors["bg"],
            font=FONT_FAMILY,
            fontsize=TREETAB_FONTSIZE,
            inactive_bg=colors["inactive"],
            inactive_fg=colors["fg"],
            padding_left=TREETAB_PADDING,
            padding_x=TREETAB_PADDING,
            padding_y=TREETAB_PADDING,
            sections=["Tabs"],
            section_fontsize=TREETAB_SECTION_FONTSIZE,
            section_fg=colors["green_accent"],
            section_top=TREETAB_SECTION_TOP,
            panel_width=TREETAB_PANEL_WIDTH,
        ),
    ]
    return layouts

def init_floating_layout():
    """Khởi tạo layout nổi.

    Cấu hình cho các cửa sổ nổi.
    """
    floating_layout = layout.Floating(
        border_focus=colors["border_focus"],
        border_normal=colors["border_normal"],
        border_width=LAYOUT_BORDER_WIDTH,
        float_rules=[
            # Thêm các quy tắc cho các cửa sổ nổi
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
            Match(wm_class="Galculator"),  # Calculator
            Match(wm_class="Gpick"),  # Color picker
            Match(wm_class="Nitrogen"),  # Wallpaper setter
            Match(wm_class="Lxappearance"),  # Theme setter
            Match(wm_class="Pavucontrol"),  # Audio control
            Match(wm_class="Xfce4-terminal"),  # Terminal with specific class
            Match(wm_class="Thunar", title="File Operation Progress"),  # Thunar file operations
        ],
    )
    return floating_layout
