#!/bin/bash

# Script để chuyển đổi giữa cấu hình Qtile cũ và mới
# Sử dụng: ./toggle_config.sh

CONFIG_DIR="$HOME/.config/qtile"
CURRENT_CONFIG="$CONFIG_DIR/config.py"
MODERN_CONFIG="$CONFIG_DIR/config_modern.py"
CLASSIC_CONFIG="$CONFIG_DIR/config_classic.py"
BACKUP_CONFIG="$CONFIG_DIR/config_backup.py"

# Kiểm tra xem đã có bản sao lưu config_classic.py chưa
if [ ! -f "$CLASSIC_CONFIG" ]; then
    echo "Tạo bản sao lưu cấu hình cũ thành config_classic.py..."
    cp "$CURRENT_CONFIG" "$CLASSIC_CONFIG"
fi

# Tạo bản sao lưu config.py hiện tại
cp "$CURRENT_CONFIG" "$BACKUP_CONFIG"

# Kiểm tra cấu hình hiện tại là gì
if grep -q "screens_modern" "$CURRENT_CONFIG"; then
    echo "Đang sử dụng cấu hình hiện đại. Chuyển sang cấu hình cũ..."
    cp "$CLASSIC_CONFIG" "$CURRENT_CONFIG"
    echo "Đã chuyển sang cấu hình cũ. Khởi động lại Qtile để áp dụng."
else
    echo "Đang sử dụng cấu hình cũ. Chuyển sang cấu hình hiện đại..."
    cp "$MODERN_CONFIG" "$CURRENT_CONFIG"
    echo "Đã chuyển sang cấu hình hiện đại. Khởi động lại Qtile để áp dụng."
fi

echo "Bạn có thể khởi động lại Qtile bằng cách nhấn Mod+Ctrl+R hoặc chạy 'qtile cmd-obj -o cmd -f restart'"
