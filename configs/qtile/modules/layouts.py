from libqtile import layout
from libqtile.config import Match

from modules.settings import theme

def init_layouts():
    layouts = [
        layout.Columns(
            margin=0,
            border_focus=theme["focus"],
            border_normal=theme["normal"],
            border_width=3,
        ),
        layout.Max(
            border_focus=theme["focus"],
            border_normal=theme["normal"],
            margin=0,
            border_width=0,
        ),
        layout.Floating(
            border_focus=theme["focus"],
            border_normal=theme["normal"],
            margin=0,
            border_width=3,
        ),
        layout.Matrix(
            border_focus=theme["focus"],
            border_normal=theme["normal"],
            margin=0,
            border_width=3,
        ),
        layout.MonadWide(
            border_focus=theme["focus"],
            border_normal=theme["normal"],
            margin=0,
            border_width=3,
        ),
        layout.Tile(
            border_focus=theme["focus"],
            border_normal=theme["normal"],
            margin=0,
            border_width=3,
        ),
    ]
    return layouts

def init_floating_layout():
    floating_layout = layout.Floating(
        border_focus=theme["focus"],
        border_normal=theme["normal"],
        border_width=3,
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ]
    )
    return floating_layout
