#!/bin/fish

# Đọc nhiệt độ màu từ file cấu hình
set CONFIG_FILE "$HOME/.config/qtile/modules/settings.py"
set TEMP_NIGHT 4500 # Giá trị mặc định

if test -f "$CONFIG_FILE"
    # Lấy giá trị từ file cấu hình
    set TEMP_VALUE (grep "redshift_temp_night" "$CONFIG_FILE" | grep -o '[0-9]\+')
    if test -n "$TEMP_VALUE"
        set TEMP_NIGHT $TEMP_VALUE
    end
end

# Lấy giờ hiện tại (định dạng 24 giờ)
set CURRENT_HOUR (date +%H)

# Kiểm tra xem có phải ban đêm không (từ 18:00 tối đến 6:00 sáng)
if test $CURRENT_HOUR -ge 18 -o $CURRENT_HOUR -lt 6
    # Kiểm tra xem redshift đã chạy chưa
    if not pgrep -x "redshift" > /dev/null
        # Nếu chưa chạy, khởi động redshift với nhiệt độ màu cấu hình
        redshift -O {$TEMP_NIGHT}K &
    else
        # Nếu đã chạy, thiết lập lại nhiệt độ màu
        redshift -O {$TEMP_NIGHT}K &
    end
else
    # Ban ngày, thiết lập lại nhiệt độ màu mặc định (6500K)
    if pgrep -x "redshift" > /dev/null
        redshift -x
    end
end
