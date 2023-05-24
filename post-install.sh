#!/usr/bin/env bash

echo "[davrOS]: stage 0: Repository Configuration"

# add chaotic aur (because why not, right?... right?)
pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
pacman-key --lsign-key FBA220DFC880C036
pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'
echo "[chaotic-aur]
Include = /etc/pacman.d/chaotic-mirrorlist " >> /etc/pacman.conf

echo "[davrOS]: stage 1: Package Installation"

# install all the packages listed in the pkg.txt file using pacman
pacman -Syu - < pkg.txt

echo "[davrOS]: stage 2: Configuration"
echo "[davrOS]: stage 2.1: Configuring neovim"

# install nvchad (because its epic)
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim

echo "[davrOS]: stage 2.2: configuring zsh"

# install zsh4humans (because its epic)
if command -v curl >/dev/null 2>&1; then
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"
else
  sh -c "$(wget -O- https://raw.githubusercontent.com/romkatv/zsh4humans/v5/install)"
fi
