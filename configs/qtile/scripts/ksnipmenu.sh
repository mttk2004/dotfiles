#!/bin/fish

# Lấy các biến môi trường từ settings.py
eval (python3 ~/.config/qtile/scripts/export_settings.py fish)

# Định dạng tên file ảnh
set timestamp (date '+%y%m%d_%H%M%S')
set save_path "$HOME/Pictures/$timestamp.png"

# Các tùy chọn menu
set options "  Capture Full Screen" "  Capture Selected Area" "  Capture Current Window" "  Cancel"

# Tạo menu với rofi
set selected (printf "%s\n" $options | rofi -theme ~/.config/qtile/themes/rofi/modern-green.rasi -dmenu -i -p "Ksnip Menu")

# Thực hiện hành động tương ứng
switch "$selected"
    case "  Capture Full Screen"
        sleep 0.3  # Thêm delay để menu kịp đóng
        ksnip -f -p $save_path
    case "  Capture Selected Area"
        sleep 0.3  # Thêm delay để menu kịp đóng
        ksnip -r -p $save_path
    case "  Capture Current Window"
        sleep 0.3  # Thêm delay để menu kịp đóng
        ksnip -a -p $save_path
    case "*"
        # Không làm gì cả khi hủy
        echo "No action was chosen"
end
