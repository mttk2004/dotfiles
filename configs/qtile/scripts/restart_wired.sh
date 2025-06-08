#!/bin/fish

# Khởi động lại dịch vụ Wired
echo "Đang khởi động lại dịch vụ thông báo Wired..."

# Tắt Wired nếu đang chạy
killall wired 2>/dev/null || true

# Đợi 1 giây
sleep 1

# Khởi động lại Wired
/usr/bin/wired &

echo "Đã khởi động lại dịch vụ thông báo Wired thành công!"
