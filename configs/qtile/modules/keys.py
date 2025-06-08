from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from modules.settings import (
    MOD, MOD_ALT, TERMINAL, FILEMANAGER, POWERMENU_SCRIPT,
    APP_LAUNCHER, GPU_SCREEN_RECORDER, KSNIPMENU_SCRIPT,
    STICKY_WINDOWS
)

# Backward compatibility
mod = MOD
mod1 = MOD_ALT

@lazy.function
def toggle_sticky_windows(qtile, window=None):
    if window is None:
        window = qtile.current_screen.group.current_window
    if window in STICKY_WINDOWS:
        STICKY_WINDOWS.remove(window)
    else:
        STICKY_WINDOWS.append(window)
    return window

@lazy.function
def switch_to_prev_group(qtile):
    """Chuyển đến workspace trước đó"""
    current_group_index = qtile.groups.index(qtile.current_group)
    # Nếu đang ở workspace đầu tiên, chuyển đến workspace cuối cùng
    if current_group_index == 0:
        qtile.current_screen.set_group(qtile.groups[-1])
    else:
        qtile.current_screen.set_group(qtile.groups[current_group_index - 1])

@lazy.function
def switch_to_next_group(qtile):
    """Chuyển đến workspace tiếp theo"""
    current_group_index = qtile.groups.index(qtile.current_group)
    # Nếu đang ở workspace cuối cùng, chuyển đến workspace đầu tiên
    if current_group_index == len(qtile.groups) - 1:
        qtile.current_screen.set_group(qtile.groups[0])
    else:
        qtile.current_screen.set_group(qtile.groups[current_group_index + 1])

def init_keys():
    keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([MOD], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([MOD], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([MOD], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([MOD], "Up", lazy.layout.up(), desc="Move focus up"),
        Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
        Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
        Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([MOD, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([MOD, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([MOD, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([MOD, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([MOD, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([MOD, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="Toggle focused window to fullscreen"),
        Key([MOD], "v", lazy.window.toggle_floating(), desc="Toggle focused window to floating"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [MOD, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
        Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

        # Window switcher với Alt+Tab sử dụng Rofi
        # Key([MOD_ALT], "Tab", lazy.spawn("rofi -theme ~/.config/qtile/themes/rofi/modern-green-window.rasi -show window -show-icons"), desc="Chuyển đổi cửa sổ với Rofi"),

        Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([MOD], "d", lazy.spawn(APP_LAUNCHER), desc="Open application launcher"),

        # Chuyển đổi giữa các workspace liền kề
        Key([MOD, MOD_ALT], "Left", switch_to_prev_group(), desc="Chuyển đến workspace bên trái"),
        Key([MOD, MOD_ALT], "Right", switch_to_next_group(), desc="Chuyển đến workspace bên phải"),

    ##CUSTOM
        Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +1%"), desc='Volume Up'),
        Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -1%"), desc='volume down'),
        Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc='Volume Mute'),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc='brightness UP'),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc='brightness Down'),

    ##Misc keybinds
        Key([], "Print", lazy.spawn(f"fish -c 'flameshot'"), desc='Screenshot with Flameshot'),
        Key([MOD, "control"], "p", lazy.spawn(f"fish -c '{KSNIPMENU_SCRIPT}'"), desc='Screenshot Menu'),
        Key([MOD], "e", lazy.spawn(FILEMANAGER), desc="Open file manager"),
        Key([MOD], "s", toggle_sticky_windows(), desc="Toggle state of sticky for current window"),
        Key([MOD], "x", lazy.spawn(f"fish -c '{POWERMENU_SCRIPT}'"), desc="Show power menu"),
        Key([MOD], "g", lazy.spawn(GPU_SCREEN_RECORDER), desc="Open GPU Screen Recorder"),
    ]
    return keys
