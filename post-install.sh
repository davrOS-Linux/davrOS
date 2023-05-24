#!/usr/bin/env bash

echo "Commencing Stage 1: Package Installation"
pacman -Syu - < pkg.txt
echo "Stage 1 Complete: Package Installation"
echo "Commencing Stage 2: Configuration"
echo "Stage 2.1: Configuring neovim"
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim
