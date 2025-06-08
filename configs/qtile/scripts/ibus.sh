#!/bin/fish

# Kiểm tra xem ibus-daemon đã chạy chưa
if not pgrep -x "ibus-daemon" > /dev/null
    # Nếu chưa chạy, khởi động ibus-daemon
    ibus-daemon -drx
end
