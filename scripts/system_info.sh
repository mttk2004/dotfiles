#!/bin/bash
# System Information Script for Dotfiles Debugging
# Collects system info to help troubleshoot configuration issues

set -e

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

print_header() {
    echo -e "${CYAN}============================================${NC}"
    echo -e "${CYAN}  DOTFILES SYSTEM INFORMATION${NC}"
    echo -e "${CYAN}============================================${NC}"
    echo
}

print_section() {
    echo -e "${BLUE}[$1]${NC}"
    echo "----------------------------------------"
}

check_command() {
    if command -v "$1" &> /dev/null; then
        echo -e "${GREEN}✓${NC} $1: $(command -v "$1")"
        if [[ "$2" == "version" ]]; then
            echo "  Version: $($1 --version 2>/dev/null | head -n1 || echo "Unknown")"
        fi
    else
        echo -e "${RED}✗${NC} $1: Not installed"
    fi
}

check_file() {
    if [[ -f "$1" ]]; then
        echo -e "${GREEN}✓${NC} $1"
    elif [[ -d "$1" ]]; then
        echo -e "${GREEN}✓${NC} $1 (directory)"
    else
        echo -e "${RED}✗${NC} $1"
    fi
}

check_service() {
    if systemctl is-active --quiet "$1" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $1: Active"
    elif systemctl is-enabled --quiet "$1" 2>/dev/null; then
        echo -e "${YELLOW}!${NC} $1: Enabled but not active"
    else
        echo -e "${RED}✗${NC} $1: Not found or disabled"
    fi
}

main() {
    print_header

    # System Information
    print_section "SYSTEM INFORMATION"
    echo "OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"
    echo "Kernel: $(uname -r)"
    echo "Architecture: $(uname -m)"
    echo "Hostname: $(hostname)"
    echo "Uptime: $(uptime -p)"
    echo "Shell: $SHELL"
    echo "User: $USER"
    echo "Home: $HOME"
    echo

    # Hardware Information
    print_section "HARDWARE"
    echo "CPU: $(lscpu | grep 'Model name' | cut -d':' -f2 | xargs)"
    echo "Memory: $(free -h | grep Mem | awk '{print $2}')"
    echo "Graphics: $(lspci | grep VGA | cut -d':' -f3 | xargs)"
    echo

    # Display Information
    print_section "DISPLAY"
    if [[ -n "$DISPLAY" ]]; then
        echo "Display: $DISPLAY"
        echo "Resolution: $(xdpyinfo 2>/dev/null | grep dimensions | awk '{print $2}' || echo "Unknown")"
        echo "Window Manager: $(wmctrl -m 2>/dev/null | grep Name | cut -d':' -f2 | xargs || echo "Unknown")"
    else
        echo "No display detected (running in TTY?)"
    fi
    echo

    # Essential Commands
    print_section "ESSENTIAL COMMANDS"
    check_command "git" "version"
    check_command "fish" "version"
    check_command "qtile"
    check_command "xmonad"
    check_command "wezterm" "version"
    check_command "nvim" "version"
    check_command "node" "version"
    check_command "npm" "version"
    check_command "python" "version"
    check_command "pip" "version"
    echo

    # Package Managers
    print_section "PACKAGE MANAGERS"
    check_command "pacman" "version"
    check_command "yay" "version"
    check_command "paru" "version"
    check_command "flatpak" "version"
    echo

    # Configuration Files
    print_section "CONFIGURATION FILES"
    check_file "$HOME/.config/qtile/config.py"
    check_file "$HOME/.wezterm.lua"
    check_file "$HOME/.config/fish/config.fish"
    check_file "$HOME/.gitconfig"
    check_file "$HOME/.bashrc"
    check_file "$HOME/.vimrc"
    check_file "$HOME/.config/nvim"
    echo

    # Dotfiles Status
    print_section "DOTFILES STATUS"
    if [[ -d "$HOME/.dotfiles" ]]; then
        echo -e "${GREEN}✓${NC} Dotfiles directory exists"
        cd "$HOME/.dotfiles"
        if [[ -d ".git" ]]; then
            echo "Git status:"
            git status --porcelain | head -5
            echo "Last commit: $(git log -1 --format="%h %s (%cr)" 2>/dev/null || echo "No commits")"
        else
            echo -e "${YELLOW}!${NC} Not a git repository"
        fi
    else
        echo -e "${RED}✗${NC} Dotfiles directory not found"
    fi
    echo

    # Services
    print_section "SERVICES"
    check_service "NetworkManager"
    check_service "pipewire"
    check_service "pipewire-pulse"
    if command -v tlp &> /dev/null; then
        check_service "tlp"
    fi
    echo

    # Environment Variables
    print_section "ENVIRONMENT VARIABLES"
    echo "EDITOR: ${EDITOR:-Not set}"
    echo "BROWSER: ${BROWSER:-Not set}"
    echo "TERMINAL: ${TERMINAL:-Not set}"
    echo "PATH entries: $(echo $PATH | tr ':' '\n' | wc -l)"
    echo

    # Font Information
    print_section "FONTS"
    if command -v fc-list &> /dev/null; then
        echo "Total fonts: $(fc-list | wc -l)"
        echo "JetBrains Mono: $(fc-list | grep -i jetbrains | wc -l) variants"
        echo "Nerd Fonts: $(fc-list | grep -i nerd | wc -l) variants"
    else
        echo "fontconfig not available"
    fi
    echo

    # Network Status
    print_section "NETWORK"
    if command -v nmcli &> /dev/null; then
        echo "Network Manager status:"
        nmcli general status | head -2
        echo "Active connections:"
        nmcli connection show --active | head -3
    else
        echo "NetworkManager not available"
    fi
    echo

    # Disk Usage
    print_section "DISK USAGE"
    df -h / | tail -1 | awk '{print "Root: " $3 "/" $2 " (" $5 " used)"}'
    if [[ -d "$HOME" ]]; then
        echo "Home: $(du -sh "$HOME" 2>/dev/null | awk '{print $1}' || echo "Unknown")"
    fi
    echo

    # Recent Logs (potential issues)
    print_section "RECENT LOGS"
    if command -v journalctl &> /dev/null; then
        echo "Recent errors (last 24h):"
        journalctl --priority=err --since="24 hours ago" --no-pager | tail -5 || echo "No recent errors"
    else
        echo "journalctl not available"
    fi
    echo

    print_section "RECOMMENDATIONS"

    # Check for missing components
    missing_components=()

    if ! command -v qtile &> /dev/null; then
        missing_components+=("qtile")
    fi

    if ! command -v wezterm &> /dev/null; then
        missing_components+=("wezterm")
    fi

    if ! command -v fish &> /dev/null; then
        missing_components+=("fish")
    fi

    if [[ ${#missing_components[@]} -gt 0 ]]; then
        echo -e "${YELLOW}Missing components:${NC}"
        for component in "${missing_components[@]}"; do
            echo "  - $component"
        done
        echo "Run: sudo pacman -S ${missing_components[*]}"
        echo
    fi

    # Check for AUR helper
    if ! command -v yay &> /dev/null && ! command -v paru &> /dev/null; then
        echo -e "${YELLOW}Recommendation:${NC} Install an AUR helper (yay or paru)"
        echo
    fi

    # Check shell
    if [[ "$SHELL" != *"fish" ]]; then
        echo -e "${YELLOW}Recommendation:${NC} Set Fish as default shell with: chsh -s \$(which fish)"
        echo
    fi

    echo -e "${GREEN}System information collection complete!${NC}"
}

# Handle command line arguments
case "${1:-}" in
    -h|--help)
        echo "System Information Script"
        echo "Usage: $0 [--save]"
        echo ""
        echo "Options:"
        echo "  --save    Save output to system-info.txt"
        echo "  -h, --help Show this help"
        ;;
    --save)
        main | tee "system-info-$(date +%Y%m%d-%H%M%S).txt"
        echo "System information saved to system-info-$(date +%Y%m%d-%H%M%S).txt"
        ;;
    "")
        main
        ;;
    *)
        echo "Unknown option: $1"
        exit 1
        ;;
esac
