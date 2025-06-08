# Qtile Configuration

Cấu hình Qtile hiện đại với thiết kế tối giản và hiệu quả.

## Tính năng

- Thiết kế hiện đại với tông màu xanh lá chủ đạo
- Hỗ trợ nhiều màn hình tự động
- Widget hiện đại với các icon và thông tin hữu ích
- Layouts đa dạng và tùy biến cao
- Tối ưu hiệu suất và trải nghiệm người dùng

## Cấu trúc thư mục

```
qtile/
├── config.py              # File cấu hình hiện tại đang sử dụng
├── config_modern.py       # Cấu hình hiện đại mới
├── config_classic.py      # Cấu hình cũ (sao lưu)
├── modules/               # Thư mục chứa các module chức năng
│   ├── keys.py            # Cấu hình phím tắt
│   ├── groups.py          # Cấu hình nhóm cửa sổ
│   ├── layouts.py         # Cấu hình bố cục cửa sổ (cũ)
│   ├── layouts_modern.py  # Cấu hình bố cục cửa sổ hiện đại
│   ├── screens.py         # Cấu hình màn hình (cũ)
│   ├── screens_modern.py  # Cấu hình màn hình hiện đại
│   ├── widgets.py         # Cấu hình widget (cũ)
│   ├── widgets_modern.py  # Cấu hình widget hiện đại
│   ├── hooks.py           # Các hook và callback
│   ├── mouse.py           # Cấu hình chuột
│   └── settings.py        # Các cài đặt chung
├── themes/                # Thư mục chứa theme
│   ├── __init__.py        # Export theme
│   └── colors.py          # Định nghĩa màu sắc
├── scripts/               # Scripts tiện ích
│   ├── autostart.sh       # Script khởi động các ứng dụng
│   ├── powermenu.sh       # Script menu nguồn
│   ├── ksnipmenu.sh       # Script menu chụp màn hình
│   ├── toggle_config.sh   # Script chuyển đổi giữa cấu hình cũ và mới
│   └── ...
├── Assets/                # Thư mục chứa tài nguyên
└── Wallpaper/             # Thư mục chứa hình nền
```

## Cách sử dụng

### Chuyển đổi giữa cấu hình cũ và mới

```bash
./scripts/toggle_config.sh
```

Sau khi chạy script, khởi động lại Qtile bằng cách nhấn `Mod+Ctrl+R` hoặc chạy lệnh:

```bash
qtile cmd-obj -o cmd -f restart
```

## Tùy chỉnh

### Thay đổi màu sắc

Chỉnh sửa file `themes/colors.py` để thay đổi bảng màu.

### Thay đổi widget

Chỉnh sửa file `modules/widgets_modern.py` để thay đổi các widget trên thanh bar.

### Thay đổi layout

Chỉnh sửa file `modules/layouts_modern.py` để thay đổi các layout cửa sổ.

## Phím tắt

- `Mod+Enter`: Mở terminal
- `Mod+w`: Đóng cửa sổ hiện tại
- `Mod+Tab`: Chuyển đổi giữa các layout
- `Mod+[1-9]`: Chuyển đổi giữa các workspace
- `Mod+Shift+[1-9]`: Di chuyển cửa sổ hiện tại đến workspace khác
- `Mod+h/j/k/l`: Di chuyển giữa các cửa sổ
- `Mod+Shift+h/j/k/l`: Thay đổi kích thước cửa sổ
- `Mod+Ctrl+r`: Khởi động lại Qtile
- `Mod+Ctrl+q`: Đăng xuất khỏi Qtile
