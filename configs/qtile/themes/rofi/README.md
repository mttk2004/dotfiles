# Theme Rofi Hiện Đại cho Qtile

Tập hợp các theme Rofi hiện đại với tông màu xanh lá chủ đạo, được thiết kế đồng bộ với bảng màu của Qtile (`themes/colors.py`).

## Các theme có sẵn

1. **modern-green.rasi**: Theme cơ bản cho các menu và hộp thoại đơn giản.
2. **modern-green-launcher.rasi**: Theme tối ưu cho launcher ứng dụng (`mod+d`), hiển thị dạng lưới với icon lớn.
3. **modern-green-window.rasi**: Theme tối ưu cho window switcher (`alt+tab`), hiển thị danh sách cửa sổ.

## Sử dụng

Các theme này được cấu hình sẵn trong `modules/settings.py` và các phím tắt trong `modules/keys.py`:

- **Launcher ứng dụng**: Nhấn `mod+d` để hiển thị menu ứng dụng với theme `modern-green-launcher.rasi`
- **Window switcher**: Nhấn `alt+tab` để chuyển đổi giữa các cửa sổ với theme `modern-green-window.rasi`
- **Power menu**: Nhấn `mod+x` để hiển thị menu nguồn với theme `modern-green.rasi`
- **Ksnip menu**: Nhấn `mod+ctrl+p` để hiển thị menu chụp màn hình với theme `modern-green.rasi`

## Tùy chỉnh

Bạn có thể tùy chỉnh các theme này bằng cách chỉnh sửa trực tiếp các file `.rasi`. Mỗi file đều có cấu trúc sau:

1. **Định nghĩa màu sắc**: Các biến màu được khai báo ở đầu file, dễ dàng thay đổi
2. **Thuộc tính cơ bản**: Các thiết lập chung cho toàn bộ theme
3. **Các phần tử giao diện**: Cấu hình chi tiết cho từng thành phần (window, mainbox, inputbar, v.v.)

## Cập nhật bảng màu

Nếu bạn thay đổi bảng màu trong `themes/colors.py`, hãy đảm bảo cập nhật cả các file theme Rofi để giữ tính nhất quán cho giao diện.

## Tạo theme mới

Để tạo theme mới, bạn có thể:

1. Sao chép một trong các file `.rasi` hiện có
2. Chỉnh sửa các thuộc tính theo ý muốn
3. Lưu với tên mới và cập nhật đường dẫn trong `modules/settings.py` hoặc phím tắt

## Nguồn tham khảo

- [Tài liệu Rofi](https://github.com/davatorium/rofi/wiki/Themes)
- [Bảng màu Qtile](../colors.py)
