# Cấu hình Wired cho Qtile

## Giới thiệu

[Wired](https://github.com/Toqozz/wired-notify) là một trình quản lý thông báo hiện đại cho Linux. File này ghi lại cách cấu hình Wired để phù hợp với theme hiện đại của Qtile.

## Cài đặt

Cấu hình Wired được lưu tại `~/.config/wired/wired.ron`. Chúng ta đã cập nhật cấu hình này để sử dụng bảng màu hiện đại với tông xanh lá làm chủ đạo.

## Màu sắc

Các màu sắc được sử dụng trong cấu hình Wired:

- Màu nền: `#1a1b26` - Phù hợp với màu nền chính của Qtile
- Màu viền chính: `#9ece6a` - Màu xanh lá chính (green_primary)
- Màu viền thông báo thấp: `#2b7a78` - Màu xanh lá tối (green_dark)
- Màu viền thông báo quan trọng: `#f7768e` - Màu lỗi (error)
- Màu viền thông báo tạm dừng: `#565f89` - Màu không hoạt động (inactive)
- Màu chữ chính: `#c0caf5` - Màu văn bản chính (fg)
- Màu chữ khi hover tiêu đề: `#9ece6a` - Màu xanh lá chính (green_primary)
- Màu chữ khi hover nội dung: `#7dcfff` - Màu nhấn mạnh (accent)

## Font chữ

- Font tiêu đề: `CaskaydiaCove Nerd Font Bold 15`
- Font nội dung: `CaskaydiaCove Nerd Font 13`

## Khởi động lại Wired

Để khởi động lại Wired sau khi thay đổi cấu hình, bạn có thể sử dụng script:

```bash
~/.config/qtile/scripts/restart_wired.sh
```

Hoặc thủ công:

```bash
killall wired
sleep 1
/usr/bin/wired &
```

## Tự động khởi động

Wired được cấu hình để tự động khởi động trong `~/.config/qtile/scripts/autostart.sh`.
