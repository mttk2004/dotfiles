"""
Cấu hình nhóm cửa sổ cho Qtile.

Định nghĩa các nhóm (workspace) và phím tắt để điều hướng giữa chúng.
"""

from libqtile.config import Group, Key
from libqtile.lazy import lazy

from modules.settings import MOD, GROUP_LABELS

def init_groups():
    """Khởi tạo danh sách các nhóm (workspace).

    Returns:
        list: Danh sách các nhóm đã khởi tạo
    """
    groups = [Group(f"{i+1}", label=GROUP_LABELS[i]) for i in range(9)]
    return groups

def init_group_keys(groups, keys):
    """Khởi tạo các phím tắt cho các nhóm.

    Args:
        groups (list): Danh sách các nhóm
        keys (list): Danh sách các phím tắt hiện có

    Returns:
        list: Danh sách các phím tắt đã cập nhật
    """
    for i in groups:
        keys.extend(
            [
                Key(
                    [MOD],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc=f"Switch to group {i.name}",
                ),
                Key(
                    [MOD, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc=f"Switch to & move focused window to group {i.name}",
                ),
            ]
        )
    return keys
