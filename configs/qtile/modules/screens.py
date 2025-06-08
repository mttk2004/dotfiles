from libqtile.config import Screen
from libqtile import bar

from modules.settings import bar_height, bar_margin
from modules.widgets import init_widgets_list

def init_screens():
    screens = [
        Screen(
            top=bar.Bar(
                init_widgets_list(),
                bar_height,
                margin=bar_margin
            ),
        ),
    ]
    return screens
