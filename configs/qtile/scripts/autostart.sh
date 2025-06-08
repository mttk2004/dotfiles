#!/bin/fish

# Khởi động feh để hiển thị hình nền
feh --bg-fill $HOME/.config/qtile/Wallpaper/bird.jpg &

# Khởi động picom với cấu hình từ file picom.conf
picom --daemon --config $HOME/.config/qtile/scripts/picom.conf &

# Khởi động polkit-gnome-authentication-agent-1
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Khởi động wired
/usr/bin/wired &

# Khởi động gnome-keyring-daemon
eval (gnome-keyring-daemon --start)

# Khởi động nm-applet
nm-applet &

# Khởi động ibus-daemon
$HOME/.config/qtile/scripts/ibus.sh &

# Khởi động redshift
$HOME/.config/qtile/scripts/redshift.sh &
