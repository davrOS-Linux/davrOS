#!/usr/bin/env bash

echo "Commencing Stage 0: Repository Configuration"

# Add chaotic AUR (because why not, right?... right?)
pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
pacman-key --lsign-key FBA220DFC880C036
pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
echo "[chaotic-aur]
Include = /etc/pacman.d/chaotic-mirrorlist " >> /etc/pacman.conf

echo "Commencing Stage 1: Package Installation"

# Install all the packages listed in the pkg.txt file using pacman
pacman -Syu - < pkg.txt

echo "Commencing Stage 2: Configuration"
echo "Stage 2.1: Configuring neovim"

# Install nvchad (because its epic)
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim
