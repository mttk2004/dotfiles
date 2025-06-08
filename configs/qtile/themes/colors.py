"""
Định nghĩa màu sắc cho Qtile.

Bảng màu hiện đại với tông xanh lá làm chủ đạo.
"""

# Bảng màu hiện đại với tông xanh lá
colors = {
    # Màu nền và văn bản
    "bg": "#1a1b26",             # Màu nền tối
    "fg": "#c0caf5",             # Màu văn bản chính

    # Màu xanh lá chủ đạo với các sắc độ
    "green_primary": "#9ece6a",  # Màu xanh lá chính
    "green_secondary": "#73daca", # Màu xanh lá phụ
    "green_dark": "#2b7a78",     # Màu xanh lá tối
    "green_light": "#a6e3a1",    # Màu xanh lá nhạt
    "green_accent": "#00dc82",   # Màu xanh lá nhấn mạnh

    # Màu tương phản và nhấn mạnh
    "accent": "#7dcfff",         # Màu nhấn mạnh (xanh dương)
    "warning": "#ff9e64",        # Màu cảnh báo (cam)
    "error": "#f7768e",          # Màu lỗi (đỏ)
    "inactive": "#565f89",       # Màu không hoạt động

    # Màu cho các thành phần giao diện
    "border_focus": "#9ece6a",   # Màu viền cửa sổ focus
    "border_normal": "#1a1b26",  # Màu viền cửa sổ bình thường
    "bar_bg": "#1a1b26",         # Màu nền thanh bar
    "bar_fg": "#c0caf5",         # Màu chữ trên thanh bar

    # Màu cho GroupBox
    "active": "#9ece6a",         # Màu workspace đang hoạt động
    "inactive_group": "#565f89", # Màu workspace không hoạt động
    "highlight": "#a6e3a1",      # Màu highlight
    "this_current": "#00dc82",   # Màu workspace hiện tại

    # Màu gradient cho thanh bar
    "gradient": [
        "#1a1b26",  # Tối
        "#24283b",  # Hơi sáng hơn
        "#2b7a78",  # Xanh tối
        "#3a7c73",  # Xanh vừa
        "#73daca",  # Xanh sáng
    ],
}
