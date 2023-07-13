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
pacman -Syyu --needed - < pkg.txt

# install some stuff from the aur using paru
paru -Su eww

echo "[davrOS]: stage 2: Configuration"

mkdir ~/.config
read -p "what is your user account?: " username
echo "username: $username"

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

echo "[davrOS]: stage 2.3: configuring hyprland"
if command -v curl >/dev/null 2>&1; then
  curl -fsSL https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/hypr/hyprland.conf
else
  wget -O- https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/hypr/hyprland.conf
fi

mkdir ~/.config/hypr
mv hyprland.conf ~/.config/hypr/hyprland.conf

echo "[davrOS]: stage 2.4: configuring neofetch"

wget -O- https://raw.githubusercontent.com/yuckdevchan/davrOS/main/custom/config/neofetch/config.conf
rm -rf ~/.config/neofetch
mkdir ~/.config/neofetch
mv config.conf ~/.config/neofetch

echo "[davrOS]: stage 3.0: system config"
echo "[davrOS]: stage 3.1: display manager / login manager"

read -p "Which display manager should be autostarted?
1) SDDM (recommended - works fine with Hyprland)
2) LightDM
3) ly (not recommended due to poor compatibility with Hyprland)
4) None

> " dm

if [ $dm = "1" ]; then
  echo "[davrOS]: Setting SDDM Symlink with systemd"
  systemctl enable sddm
elif [ $dm = "2" ]; then
  echo "[davrOS]: Setting LightDM Symlink with systemd"
  systemctl enable lightdm
elif [ $dm = "3" ]; then
  echo "[davrOS]: Setting ly Symlink with systemd"
  systemctl enable ly
elif [ $dm = "4" ]; then
  echo "[davrOS]: Setting no display manager"
fi

# move configs from root user's .config to the other one
mv ~/.config/zsh /home/$username/.config
mv ~/.config/hyprland /home/$username/.config
mv ~/.config/nvim /home/$username/.config
mv ~/.config/neofetch /home/$username/.config
