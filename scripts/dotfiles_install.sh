#!/bin/bash

# Dotfiles Installation Script for CachyOS
# Author: Your Name
# Description: Install and symlink dotfiles configuration

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directories
DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKUP_DIR="$HOME/.dotfiles-backup-$(date +%Y%m%d-%H%M%S)"

# Logging functions
log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Create backup directory
create_backup() {
    log_info "Creating backup directory: $BACKUP_DIR"
    mkdir -p "$BACKUP_DIR"
}

# Backup existing config if it exists
backup_config() {
    local source="$1"
    local config_name="$2"
    
    if [[ -e "$source" ]]; then
        log_warning "Backing up existing $config_name"
        cp -r "$source" "$BACKUP_DIR/"
        rm -rf "$source"
    fi
}

# Create symlink
create_symlink() {
    local source="$1"
    local target="$2"
    local config_name="$3"
    
    if [[ -f "$source" || -d "$source" ]]; then
        log_info "Linking $config_name"
        mkdir -p "$(dirname "$target")"
        ln -sf "$source" "$target"
        log_success "$config_name linked successfully"
    else
        log_warning "$source does not exist, skipping $config_name"
    fi
}

# Install packages
install_packages() {
    log_info "Installing packages..."
    
    # Check if packages list exists
    if [[ -f "$DOTFILES_DIR/packages/arch-packages.txt" ]]; then
        log_info "Installing Arch packages..."
        sudo pacman -S --needed - < "$DOTFILES_DIR/packages/arch-packages.txt"
    fi
    
    if [[ -f "$DOTFILES_DIR/packages/aur-packages.txt" ]]; then
        log_info "Installing AUR packages..."
        # Assuming yay is installed
        if command -v yay &> /dev/null; then
            yay -S --needed - < "$DOTFILES_DIR/packages/aur-packages.txt"
        else
            log_warning "yay not found, please install AUR packages manually"
        fi
    fi
}

# Main installation function
main() {
    log_info "Starting dotfiles installation..."
    
    create_backup
    
    # Qtile configuration
    backup_config "$HOME/.config/qtile" "Qtile config"
    create_symlink "$DOTFILES_DIR/configs/qtile" "$HOME/.config/qtile" "Qtile"
    
    # Xmonad configuration
    backup_config "$HOME/.xmonad" "Xmonad config"
    create_symlink "$DOTFILES_DIR/configs/xmonad" "$HOME/.xmonad" "Xmonad"
    
    # WezTerm configuration
    backup_config "$HOME/.config/wezterm" "WezTerm config"
    create_symlink "$DOTFILES_DIR/configs/wezterm" "$HOME/.config/wezterm" "WezTerm"
    
    # Fish shell configuration
    backup_config "$HOME/.config/fish" "Fish config"
    create_symlink "$DOTFILES_DIR/configs/fish" "$HOME/.config/fish" "Fish"
    
    # Git configuration
    backup_config "$HOME/.gitconfig" "Git config"
    create_symlink "$DOTFILES_DIR/configs/git/.gitconfig" "$HOME/.gitconfig" "Git"
    
    # Neovim configuration (if exists)
    if [[ -d "$DOTFILES_DIR/configs/nvim" ]]; then
        backup_config "$HOME/.config/nvim" "Neovim config"
        create_symlink "$DOTFILES_DIR/configs/nvim" "$HOME/.config/nvim" "Neovim"
    fi
    
    # Install packages
    read -p "Do you want to install packages? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        install_packages
    fi
    
    # Set Fish as default shell
    if command -v fish &> /dev/null; then
        log_info "Setting Fish as default shell..."
        chsh -s "$(which fish)"
    fi
    
    log_success "Dotfiles installation completed!"
    log_info "Backup created at: $BACKUP_DIR"
    log_info "Please restart your terminal or re-login to apply all changes"
}

# Show help
show_help() {
    echo "Dotfiles Installation Script"
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  -b, --backup   Create backup only"
    echo "  -r, --restore  Restore from backup"
}

# Handle command line arguments
case "${1:-}" in
    -h|--help)
        show_help
        exit 0
        ;;
    -b|--backup)
        create_backup
        log_success "Backup created at: $BACKUP_DIR"
        exit 0
        ;;
    -r|--restore)
        if [[ -n "${2:-}" && -d "$2" ]]; then
            log_info "Restoring from $2"
            cp -r "$2"/* "$HOME/"
            log_success "Restore completed"
        else
            log_error "Please specify backup directory"
            exit 1
        fi
        ;;
    "")
        main
        ;;
    *)
        log_error "Unknown option: $1"
        show_help
        exit 1
        ;;
esac