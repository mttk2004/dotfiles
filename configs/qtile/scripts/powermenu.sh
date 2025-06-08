#!/bin/fish

# Lấy các biến môi trường từ settings.py
eval (python3 ~/.config/qtile/scripts/export_settings.py fish)

# Power menu sử dụng Rofi với theme rounded-green-dark phù hợp với cấu hình hiện tại của Qtile

# Lựa chọn menu
set options "  Lock" "  Logout" "  Reboot" "  Shutdown" "  Suspend"

# Tạo menu với rofi
set selected (printf "%s\n" $options | rofi -theme ~/.config/qtile/themes/rofi/modern-green.rasi -dmenu -i -p "Power Menu")

# Thực hiện hành động tương ứng
switch "$selected"
    case "  Lock"
        i3lock -c 000000
    case "  Logout"
        qtile cmd-obj -o cmd -f shutdown
    case "  Reboot"
        systemctl reboot
    case "  Shutdown"
        systemctl poweroff
    case "  Suspend"
        systemctl suspend
    case "*"
        # Nếu không chọn gì
        echo "No action was chosen"
end
