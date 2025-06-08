local wezterm = require 'wezterm'
local act = wezterm.action

-- Sử dụng config_builder để cấu hình dễ dàng hơn
local config = wezterm.config_builder()

-- Font và kích thước
config.font = wezterm.font("CaskaydiaCove Nerd Font", {weight = "Light"})
config.font_size = 13.0

-- Màu sắc và theme
config.color_scheme = "Tokyo Night" -- Theme hiện đại và dễ nhìn
config.window_background_opacity = 0.95 -- Tăng độ đậm một chút để dễ đọc hơn

-- Tùy chỉnh màu sắc
config.colors = {
  selection_fg = '#e6e6fa',
  selection_bg = '#2b3045',
}

-- Background với hình ảnh mờ (uncomment nếu muốn sử dụng)
-- config.background = {
--   {
--     source = {
--       File = os.getenv("HOME") .. "/.config/wezterm/background.jpg",
--     },
--     width = "100%",
--     height = "100%",
--     opacity = 0.15,
--     attachment = "Fixed",
--   },
-- }

-- Tắt thanh tab để tối giản giao diện
config.enable_tab_bar = false

-- Shell mặc định
config.default_prog = {"/usr/bin/fish"}

-- Padding cửa sổ để tạo cảm giác thoáng hơn
config.window_padding = {
  left = 20,
  right = 20,
  top = 20,
  bottom = 20,
}

-- Viền cửa sổ
config.window_decorations = "RESIZE" -- Chỉ hiển thị viền để resize, không có thanh tiêu đề
config.window_close_confirmation = "AlwaysPrompt" -- Xác nhận khi đóng cửa sổ

-- Cursor
config.cursor_blink_rate = 500 -- Tốc độ nhấp nháy con trỏ
config.default_cursor_style = "SteadyBar" -- Kiểu con trỏ thanh đứng

-- Hiệu ứng cửa sổ và font
-- config.window_frame = {
--   font = wezterm.font { family = "Roboto", weight = "Bold" },
--   font_size = 11.0,
--   border_left_width = '0.5cell',
--   border_right_width = '0.5cell',
--   border_bottom_height = '0.25cell',
--   border_top_height = '0.25cell',
--   border_left_color = '#2b3045',
--   border_right_color = '#2b3045',
--   border_bottom_color = '#2b3045',
--   border_top_color = '#2b3045',
-- }

-- Animation
config.animation_fps = 60 -- Tốc độ khung hình cho animation
config.cursor_blink_ease_in = "Constant"
config.cursor_blink_ease_out = "Constant"

-- Phím tắt
config.keys = {
  -- Phím tắt để tăng/giảm kích thước font
  {
    key = '=',
    mods = 'CTRL',
    action = act.IncreaseFontSize,
  },
  {
    key = '-',
    mods = 'CTRL',
    action = act.DecreaseFontSize,
  },
  {
    key = '0',
    mods = 'CTRL',
    action = act.ResetFontSize,
  },

  -- Phím tắt để điều chỉnh kích thước pane
  {
    key = '[',
    mods = 'CTRL|SHIFT',
    action = act.AdjustPaneSize { "Left", 5 },
  },
  {
    key = ']',
    mods = 'CTRL|SHIFT',
    action = act.AdjustPaneSize { "Right", 5 },
  },
  {
    key = 'UpArrow',
    mods = 'CTRL|SHIFT',
    action = act.AdjustPaneSize { "Up", 5 },
  },
  {
    key = 'DownArrow',
    mods = 'CTRL|SHIFT',
    action = act.AdjustPaneSize { "Down", 5 },
  },

  -- Thêm phím tắt hữu ích
  {
    key = 'c',
    mods = 'CTRL|SHIFT',
    action = act.CopyTo "Clipboard",
  },
  {
    key = 'v',
    mods = 'CTRL|SHIFT',
    action = act.PasteFrom "Clipboard",
  },
  {
    key = 'f',
    mods = 'CTRL|SHIFT',
    action = act.Search { CaseSensitiveString = "" },
  },
}

-- Hiệu ứng khởi động
config.initial_cols = 110
config.initial_rows = 28

-- Làm mờ nền khi không focus
config.inactive_pane_hsb = {
  saturation = 0.8,
  brightness = 0.7,
}

-- Hiệu ứng chuyển cảnh
config.enable_scroll_bar = false
config.use_fancy_tab_bar = false

-- Màu sắc cho hyperlinks
config.hyperlink_rules = wezterm.default_hyperlink_rules()
table.insert(config.hyperlink_rules, {
  regex = [[\b([\w-]+/[\w-]+)\b]],
  format = 'https://github.com/$1',
})

-- Hiệu ứng khi khởi động
config.exit_behavior = 'Close'
config.skip_close_confirmation_for_processes_named = {
  'bash', 'sh', 'zsh', 'fish', 'tmux',
}

-- Hiệu ứng khi nhấn phím
config.audible_bell = "Disabled"
config.visual_bell = {
  fade_in_duration_ms = 75,
  fade_out_duration_ms = 75,
  target = "CursorColor",
}

-- Hiệu ứng khi cuộn
config.scrollback_lines = 10000
config.enable_kitty_keyboard = true

-- Hiệu ứng khi terminal không hoạt động
config.automatically_reload_config = true

return config
